#!/usr/bin/env python3
r"""naming-collision-gate.py — executable kernel of the naming-collision gate.

Spec:  corpus/knowledge/verification/naming-collision-gate.md
       (§4 Gate A uniqueness, §5 similarity triage, §6 Gate B
        pronounceability, §7 Gate C derivational validity, §9 Gate D
        bounded cross-cultural review, §10 regression fixture).

Usage:
    python3 tools/gates/naming-collision-gate.py <culture-packet.yml>
    python3 tools/gates/naming-collision-gate.py --selftest

Output:  one finding per line, `FINDING <id>: <LEVEL> — <message>`,
         LEVEL in FAIL / HOLD / REVIEW per the spec verdict table.
Exit:    0 = clean (no findings); 1 = findings; 2 = could-not-evaluate
         (unreadable file, YAML outside the declared subset, root neither a
         mapping nor a list of mappings, or a packet without `name`).

Missing sections are tolerated as could-not-evaluate and surface as HOLD
findings (PHON-PROFILE, NAME-INVENTORY, CROSS-HOLD); they do not abort the
run, because the remaining checks are still evidence. Only input that
cannot be interpreted at all exits 2. A sibling gate whose whole kernel
is one section (phonology-sanity-gate.py) may map a missing profile to
exit 2; this gate keeps it at exit 1 as a HOLD so the other three check
families still report in the same run.

Finding ids
    G-DATA          input could not be evaluated (exit 2)
    NAME-INVENTORY  no usable name-use inventory (missing/empty/malformed)
    NAME-ENTITY     name use without a stable entity link; a collision
                    cannot be classified as identity or coincidence
    NAME-REUSE      different entity ids share one unqualified key (exact,
                    NFC, declared case, declared separators, or spoken
                    form) and no per-party reuse decision is recorded [FAIL]
    NAME-CASE       case-only overlap with no declared casing rule     [REVIEW]
    NAME-COMPAT     NFKC-only overlap of distinct stored forms       [REVIEW]
    NAME-FOLD       diacritic-reduced (lossy, labeled) overlap       [REVIEW]
    NAME-VISUAL     confusable-skeleton overlap                      [REVIEW]
    NAME-SCRIPT     mixed scripts or control/format characters       [REVIEW]
    NAME-NEAR       edit distance <= declared threshold              [REVIEW]
    NAME-LEXEME     a name equals a lexicon term                     [REVIEW]
    PHON-PROFILE    no usable phonology profile                      [HOLD]
    PHON-HOLD       non-native stage without profile/adaptation path [HOLD]
    PHON-INVENTORY  symbol outside the declared inventory            [FAIL]
    PHON-ONSET / PHON-CODA / PHON-NUCLEUS / PHON-STRUCTURE           [FAIL]
    DERIV-AFFIX     affix or rule id not licensed by the morphology  [FAIL]
    DERIV-REPLAY    the stated chain does not yield the candidate    [FAIL]
    DERIV-HOLD      formation claim without replayable evidence      [HOLD]
    CROSS-HOLD      missing/empty/unresolved bounded review record   [HOLD]
    CROSS-HIT       recorded cultural/legal hit needs qualified review
    CROSS-REVIEW    ordinary resemblance recorded                    [REVIEW]

Calibration (craft policy, declaring what this implementation does)
- Thresholds, key layers, and the toy fixture are this gate's engineering
  choices, not conclusions of the cited scholarship (spec §1, §5, §10).
  Findings are review evidence for lore-shokunin, never canon rulings.
- YAML subset: block mappings/sequences, flow [..]/{..}, quoted scalars
  with \uXXXX escapes, `#` comments, `|`/`>` blocks. No anchors, tags,
  multi-document streams, or tab indentation; input outside the subset
  exits 2 instead of being guessed.
- Gate A indexes entity classes (names, pantheon, symbols, costumes,
  eras). Lexicon terms are tested separately (NAME-LEXEME): an ordinary
  word and a personal name sharing a form is common in real naming
  systems, a review prompt rather than an identity collision.
- Case folding for identity keys happens only when the packet declares
  `orthography.case: display-only` (no universal lowercasing). Sound
  tokenization folds case unless the orthography declares it contrastive.
- Confusable skeletons use a small hand-checked subset of UTS #39
  confusables (Latin/Greek/Cyrillic letter lookalikes); it is NOT the
  full UTS #39 data — (to-verify) before any reproducibility claim.
- Similarity triage default is edit distance <= 1 (spec §5 craft default,
  matching naming-canon-workflow.md); it is recall-oriented retrieval,
  not a confusion verdict. The "shared distinctive beginnings/endings"
  heuristic stays a human review step.
- Declared entry keys beyond the shared schema: `id`/`entity_id`,
  `alias_of`, `relation`, `reuse_decision` (or `disposition:
  retain-intentional|disambiguate|intentional`), `opaque`, `formation`
  {stem, rule, affix, gloss}, `stage`, `profile`, `adaptation`,
  `compare_only` (mechanism-fixture record: key-equivalence checks only),
  `coda`/`onset`/`onset_clusters` inside `phonology`, `orthography`
  {script, case, separators}, `similarity` {max_distance},
  `cross_culture_review` {languages: [{language, result, note}],
  unresolved: []}.
- Wider audit, deliberately NOT machine-checked here (a kernel pass is
  not a full clearance, spec §1, §5, §6, §7): transliteration schemes and
  localized reader forms; prosody realization and stress/tone assignment;
  connected-use forms (address, possessive/case, clitics, titles);
  "missing glyph" rendering checks, which need the actual display
  pipeline; reader-channel trials and community/specialist review; and
  real-language search evidence for Gate D, which only a recorded bounded
  sweep can supply.
- No network, no writes at run time; `--selftest` reads the two committed
  fixture files beside this script.
"""

import re
import sys
import unicodedata
from collections import Counter
from itertools import combinations
from pathlib import Path

EXIT_CLEAN = 0
EXIT_FINDINGS = 1
EXIT_UNEVALUATED = 2

# --------------------------------------------------------------------------
# minimal YAML subset loader
# --------------------------------------------------------------------------

_ESCAPES = {"n": "\n", "t": "\t", "r": "\r", "\\": "\\", '"': '"', "/": "/", "0": "\0"}


class YamlError(Exception):
    """Input is outside the declared YAML subset (-> exit 2)."""


def _strip_comment(line):
    out = []
    quote = None
    i = 0
    while i < len(line):
        ch = line[i]
        if quote:
            out.append(ch)
            if quote == '"' and ch == "\\" and i + 1 < len(line):
                out.append(line[i + 1])
                i += 2
                continue
            if ch == quote:
                quote = None
            i += 1
            continue
        if ch in "\"'":
            quote = ch
            out.append(ch)
            i += 1
            continue
        if ch == "#" and (i == 0 or line[i - 1] in " \t"):
            break
        out.append(ch)
        i += 1
    return "".join(out)


def _split_lines(text):
    lines = []
    for raw in text.splitlines():
        line = _strip_comment(raw).rstrip()
        if not line.strip():
            continue
        if line.strip() in ("---", "..."):
            continue
        indent = len(line) - len(line.lstrip(" "))
        rest = line[indent:]
        if rest.startswith("\t"):
            raise YamlError("tab indentation is not supported by this subset")
        lines.append((indent, rest))
    return lines


def _unescape_double(text):
    out = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "\\" and i + 1 < len(text):
            nxt = text[i + 1]
            if nxt in _ESCAPES:
                out.append(_ESCAPES[nxt])
                i += 2
                continue
            if nxt in ("u", "U"):
                width = 4 if nxt == "u" else 8
                hexdigits = text[i + 2 : i + 2 + width]
                if len(hexdigits) == width:
                    try:
                        out.append(chr(int(hexdigits, 16)))
                        i += 2 + width
                        continue
                    except ValueError:
                        pass
            out.append(nxt)
            i += 2
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def _parse_scalar(text):
    s = text.strip()
    if s == "" or s in ("null", "Null", "NULL", "~"):
        return None
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"' and (len(s) == 2 or s[-2] != "\\"):
        return _unescape_double(s[1:-1])
    if len(s) >= 2 and s[0] == "'" and s[-1] == "'":
        return s[1:-1].replace("''", "'")
    low = s.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    if re.fullmatch(r"-?\d+\.\d+", s):
        return float(s)
    return s


def _split_flow(text):
    parts = []
    depth = 0
    quote = None
    cur = []
    i = 0
    while i < len(text):
        ch = text[i]
        if quote:
            cur.append(ch)
            if quote == '"' and ch == "\\" and i + 1 < len(text):
                cur.append(text[i + 1])
                i += 2
                continue
            if ch == quote:
                quote = None
            i += 1
            continue
        if ch in "\"'":
            quote = ch
            cur.append(ch)
            i += 1
            continue
        if ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        elif ch == "," and depth == 0:
            parts.append("".join(cur))
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    tail = "".join(cur)
    if tail.strip():
        parts.append(tail)
    return [p.strip() for p in parts if p.strip()]


def _key_of(text):
    s = text.strip()
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        return _unescape_double(s[1:-1])
    if len(s) >= 2 and s[0] == "'" and s[-1] == "'":
        return s[1:-1].replace("''", "'")
    return s


def _split_key(text):
    depth = 0
    quote = None
    i = 0
    while i < len(text):
        ch = text[i]
        if quote:
            if quote == '"' and ch == "\\":
                i += 2
                continue
            if ch == quote:
                quote = None
            i += 1
            continue
        if ch in "\"'":
            quote = ch
            i += 1
            continue
        if ch in "[{":
            depth += 1
            i += 1
            continue
        if ch in "]}":
            depth -= 1
            i += 1
            continue
        if ch == ":" and depth == 0 and (i + 1 == len(text) or text[i + 1] in " \t"):
            return _key_of(text[:i]), text[i + 1 :].strip()
        i += 1
    raise YamlError(f"expected 'key: value', got {text[:60]!r}")


def _looks_like_key(text):
    depth = 0
    quote = None
    i = 0
    while i < len(text):
        ch = text[i]
        if quote:
            if quote == '"' and ch == "\\":
                i += 2
                continue
            if ch == quote:
                quote = None
            i += 1
            continue
        if ch in "\"'":
            quote = ch
            i += 1
            continue
        if ch in "[{":
            depth += 1
            i += 1
            continue
        if ch in "]}":
            depth -= 1
            i += 1
            continue
        if ch == ":" and depth == 0 and (i + 1 == len(text) or text[i + 1] in " \t"):
            return True
        i += 1
    return False


def _parse_value(text):
    s = text.strip()
    if s.startswith("[") or s.startswith("{"):
        return _parse_flow(s)
    return _parse_scalar(s)


def _parse_flow(text):
    s = text.strip()
    if s.startswith("["):
        if not s.endswith("]"):
            raise YamlError(f"unterminated flow sequence: {s[:40]!r}")
        return [_parse_value(part) for part in _split_flow(s[1:-1])]
    if s.startswith("{"):
        if not s.endswith("}"):
            raise YamlError(f"unterminated flow mapping: {s[:40]!r}")
        out = {}
        for part in _split_flow(s[1:-1]):
            key, rest = _split_key(part)
            out[key] = _parse_value(rest)
        return out
    raise YamlError(f"not a flow collection: {s[:40]!r}")


def _parse_block(lines, i, indent):
    if i >= len(lines):
        return None, i
    ind, text = lines[i]
    if ind != indent:
        raise YamlError(f"unexpected indentation at input line {i + 1}")
    if text.startswith("[") or text.startswith("{"):
        return _parse_value(text), i + 1
    if text == "-" or text.startswith("- "):
        return _parse_seq(lines, i, indent)
    return _parse_map(lines, i, indent)


def _parse_seq(lines, i, indent):
    items = []
    while i < len(lines) and lines[i][0] == indent:
        text = lines[i][1]
        if not (text == "-" or text.startswith("- ")):
            raise YamlError(f"sequence item where not expected at input line {i + 1}")
        inner = text[1:]
        inner_off = indent + 1
        while inner.startswith(" "):
            inner = inner[1:]
            inner_off += 1
        item_lines = []
        if inner:
            item_lines.append((inner_off, inner))
        j = i + 1
        while j < len(lines) and lines[j][0] > indent:
            item_lines.append(lines[j])
            j += 1
        if not item_lines:
            items.append(None)
        else:
            first = item_lines[0][1]
            if first.startswith("[") or first.startswith("{"):
                if len(item_lines) > 1:
                    raise YamlError(f"unexpected content after flow item at input line {i + 1}")
                items.append(_parse_value(first))
            elif _looks_like_key(first):
                node, k = _parse_block(item_lines, 0, item_lines[0][0])
                if k != len(item_lines):
                    raise YamlError(f"unparsed content in list item near input line {i + 1}")
                items.append(node)
            else:
                if len(item_lines) > 1:
                    raise YamlError(f"multi-line plain scalar is outside this subset (input line {i + 1})")
                items.append(_parse_scalar(first))
        i = j
    if i < len(lines) and lines[i][0] == indent:
        raise YamlError(f"mixed block content at input line {i + 1}")
    return items, i


def _parse_map(lines, i, indent):
    node = {}
    while i < len(lines):
        ind, text = lines[i]
        if ind < indent:
            break
        if ind > indent:
            raise YamlError(f"unexpected indentation at input line {i + 1}")
        if text == "-" or text.startswith("- "):
            raise YamlError(f"sequence item where mapping expected at input line {i + 1}")
        key, rest = _split_key(text)
        if rest in ("|", "|-", "|+", ">", ">-", ">+"):
            parts = []
            j = i + 1
            while j < len(lines) and lines[j][0] > indent:
                parts.append(lines[j][1])
                j += 1
            node[key] = ("\n" if rest.startswith("|") else " ").join(parts)
            i = j
            continue
        if rest == "":
            if i + 1 < len(lines) and lines[i + 1][0] > indent:
                child, i = _parse_block(lines, i + 1, lines[i + 1][0])
                node[key] = child
            else:
                node[key] = None
                i += 1
        else:
            node[key] = _parse_value(rest)
            i += 1
    return node, i


def load_yaml(text):
    lines = _split_lines(text)
    if not lines:
        raise YamlError("empty input")
    node, i = _parse_block(lines, 0, lines[0][0])
    if i != len(lines):
        raise YamlError(f"unparsed content at input line {i + 1}")
    return node


# --------------------------------------------------------------------------
# text utilities
# --------------------------------------------------------------------------


def _s(value):
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def _has_text(value):
    return isinstance(value, str) and value.strip() != ""


def _nfc(text):
    return unicodedata.normalize("NFC", text)


# A bounded, hand-checked subset of UTS #39 confusables (Latin/Greek/
# Cyrillic letter lookalikes and common quote/dash alternates). NOT the
# full UTS #39 data; (to-verify) before claiming reproducibility.
_CONFUSABLES = {
    "\u0430": "a", "\u0435": "e", "\u043e": "o", "\u0440": "p", "\u0441": "c",
    "\u0445": "x", "\u0443": "y", "\u0456": "i", "\u0455": "s", "\u0458": "j",
    "\u04bb": "h",
    "\u03b1": "a", "\u03b5": "e", "\u03bf": "o", "\u03c1": "p", "\u03b9": "i",
    "\u03ba": "k", "\u03bd": "v", "\u03c4": "t", "\u03c5": "u", "\u03c7": "x",
    "\u2019": "'", "\u2018": "'", "\u02bc": "'", "\u2032": "'",
    "\u2013": "-", "\u2014": "-", "\u2212": "-",
}


def _skeleton(text):
    folded = text.casefold()
    return "".join(_CONFUSABLES.get(ch, ch) for ch in folded)


_SCRIPT_HEADS = {
    "LATIN": "latin", "GREEK": "greek", "CYRILLIC": "cyrillic", "ARABIC": "arabic",
    "HEBREW": "hebrew", "CJK": "cjk", "HIRAGANA": "hiragana", "KATAKANA": "katakana",
    "HANGUL": "hangul", "DEVANAGARI": "devanagari", "BENGALI": "bengali",
    "THAI": "thai", "ARMENIAN": "armenian", "GEORGIAN": "georgian", "ETHIOPIC": "ethiopic",
}


def _script_check(form):
    scripts = set()
    control = False
    for ch in form:
        category = unicodedata.category(ch)
        if category[0] == "C":
            control = True
            continue
        if not ch.isalpha():
            continue
        try:
            head = unicodedata.name(ch).split()[0]
        except ValueError:
            scripts.add("unnamed")
            continue
        scripts.add(_SCRIPT_HEADS.get(head, "other"))
    return sorted(scripts), control


def _edit_distance(seq_a, seq_b, cap=None):
    if cap is not None and abs(len(seq_a) - len(seq_b)) > cap:
        return cap + 1
    prev = list(range(len(seq_b) + 1))
    for i, ca in enumerate(seq_a, 1):
        cur = [i] + [0] * len(seq_b)
        for j, cb in enumerate(seq_b, 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (0 if ca == cb else 1))
        prev = cur
    return prev[-1]


# --------------------------------------------------------------------------
# packet reading
# --------------------------------------------------------------------------


def _case_policy(packet):
    orth = packet.get("orthography")
    if isinstance(orth, dict):
        case = _s(orth.get("case")).casefold()
        if case in ("display-only", "display_only", "case-insensitive", "case_insensitive", "fold"):
            return True
    return False


def _case_contrastive(packet):
    orth = packet.get("orthography")
    if isinstance(orth, dict):
        case = _s(orth.get("case")).casefold()
        if case in ("contrastive", "significant", "case-sensitive", "case_sensitive"):
            return True
    return False


def _separators(packet):
    orth = packet.get("orthography")
    if isinstance(orth, dict):
        seps = orth.get("separators")
        if isinstance(seps, list):
            return [_s(x) for x in seps if _has_text(_s(x))]
        if _has_text(_s(seps)):
            return [_s(seps)]
    return []


def _decision_of(entry):
    if not isinstance(entry, dict):
        return None
    decision = _s(entry.get("reuse_decision")).strip()
    if decision:
        return decision
    disposition = _s(entry.get("disposition")).strip().casefold().replace("_", "-")
    if disposition in ("retain-intentional", "keep-intentional", "intentional", "disambiguate"):
        return disposition
    return None


def _make_record(entry, cls, fallback_eid, form=None, form_key="name"):
    form = _s(entry.get(form_key)) if form is None else form
    eid = None
    declared = False
    for key in ("id", "entity_id", "entity"):
        if _has_text(_s(entry.get(key))):
            eid = _s(entry.get(key)).strip()
            declared = True
            break
    if eid is None:
        link = _s(entry.get("alias_of") or entry.get("same_as")).strip()
        if link:
            eid = link
            declared = True
    return {
        "form": form,
        "eid": eid if eid else fallback_eid,
        "declared_id": declared,
        "cls": cls,
        "entry": entry,
    }


def _collect_records(packet):
    records = []
    notes = []
    names = packet.get("names")
    names_present = isinstance(names, list)
    if isinstance(names, list):
        for index, entry in enumerate(names):
            if not isinstance(entry, dict):
                notes.append(f"names[{index + 1}] is not a mapping; skipped")
                continue
            form = _s(entry.get("name")).strip()
            if not form:
                notes.append(f"names[{index + 1}] has no usable `name`; skipped")
                continue
            record = _make_record(entry, "names", f"name#{index + 1}")
            relation = _s(entry.get("relation") or entry.get("alias_of")).casefold()
            if "alias" in relation and not record["declared_id"]:
                notes.append(f"name use {form!r} declares an alias relation without an entity link")
            records.append(record)
    for key, cls, form_key in (
        ("pantheon", "deity", "name"),
        ("symbols", "symbol", "sign"),
        ("costumes", "garment", "garment"),
    ):
        section = packet.get(key)
        if not isinstance(section, list):
            continue
        for index, entry in enumerate(section):
            if not isinstance(entry, dict):
                continue
            form = _s(entry.get(form_key)).strip()
            if not form:
                continue
            records.append(_make_record(entry, cls, f"{cls}#{index + 1}", form=form))
    eras = packet.get("eras")
    if isinstance(eras, list):
        for index, entry in enumerate(eras):
            form = _s(entry).strip()
            if form:
                records.append(_make_record({}, "era", f"era#{index + 1}", form=form))
    return records, notes, names_present


def _build_keys(form, case_policy, seps):
    nfc = _nfc(form)
    cased = nfc.casefold() if case_policy else nfc
    primary = cased
    for sep in seps:
        primary = primary.replace(sep, "")
    compat = _nfc(unicodedata.normalize("NFKC", form))
    if case_policy:
        compat = compat.casefold()
    stripped = "".join(ch for ch in unicodedata.normalize("NFD", cased) if not unicodedata.combining(ch))
    return {
        "raw": form,
        "primary": primary,
        "casefold": nfc.casefold(),
        "compat": compat,
        "diacritic": _nfc(stripped),
        "skeleton": _skeleton(cased),
    }


def _layer_reason(forms, case_policy):
    if len(set(forms)) == 1:
        return "exact code-point sequence"
    if len({_nfc(f) for f in forms}) == 1:
        return "canonically equivalent sequences (NFC)"
    cased = set()
    for form in forms:
        folded = _nfc(form)
        if case_policy:
            folded = folded.casefold()
        cased.add(folded)
    if len(cased) == 1:
        return "case-only difference under the declared display-only casing rule"
    return "separator-normalized retrieval key (declared separators)"


# --------------------------------------------------------------------------
# phonology: template, tokenization, syllabification
# --------------------------------------------------------------------------

_TEMPLATE_TOKEN = re.compile(r"\(([CV]+)\)|([CV])")


def _parse_template(pattern):
    slots = []
    pos = 0
    for match in _TEMPLATE_TOKEN.finditer(pattern):
        if match.start() != pos:
            raise YamlError(f"unexpected characters in template {pattern!r}")
        optional = match.group(1) is not None
        group = match.group(1) or match.group(2)
        for ch in group:
            slots.append((ch, optional))
        pos = match.end()
    if pos != len(pattern) or not slots:
        raise YamlError(f"empty or trailing characters in template {pattern!r}")
    kinds = [kind for kind, _ in slots]
    index = 0
    while index < len(kinds) and kinds[index] == "C":
        index += 1
    nucleus_start = index
    while index < len(kinds) and kinds[index] == "V":
        index += 1
    coda_start = index
    while index < len(kinds) and kinds[index] == "C":
        index += 1
    if index != len(kinds) or nucleus_start == coda_start:
        raise YamlError(f"template {pattern!r} is not of the shape C*V+C*")
    onset_slots = slots[:nucleus_start]
    nucleus_slots = slots[nucleus_start:coda_start]
    coda_slots = slots[coda_start:]
    if not any(not optional for _, optional in nucleus_slots):
        raise YamlError(f"template {pattern!r} allows a nucleus-less syllable")
    return {
        "onset_min": sum(1 for _, optional in onset_slots if not optional),
        "onset_max": len(onset_slots),
        "nuc_min": sum(1 for _, optional in nucleus_slots if not optional),
        "nuc_max": len(nucleus_slots),
        "coda_min": sum(1 for _, optional in coda_slots if not optional),
        "coda_max": len(coda_slots),
    }


def _build_profile(source):
    if not isinstance(source, dict):
        return None, "profile is not a mapping"
    consonants = [_s(x) for x in source.get("consonants") or [] if _has_text(_s(x))]
    vowels = [_s(x) for x in source.get("vowels") or [] if _has_text(_s(x))]
    pattern = _s(source.get("phonotactics")).strip()
    if not consonants or not vowels or not pattern:
        return None, "phonology needs `consonants`, `vowels`, and a `phonotactics` template"
    try:
        template = _parse_template(pattern)
    except YamlError as exc:
        return None, f"unsupported phonotactics template: {exc}"
    coda = source.get("coda")
    coda_set = {_s(x) for x in coda if _has_text(_s(x))} if isinstance(coda, list) else None
    onset = source.get("onset")
    onset_set = {_s(x) for x in onset if _has_text(_s(x))} if isinstance(onset, list) else None
    if source.get("onset_clusters") is False and template["onset_max"] > 1:
        template["onset_max"] = 1
    return {
        "pattern": pattern,
        "consonants": consonants,
        "vowels": vowels,
        "cons_set": set(consonants),
        "vow_set": set(vowels),
        "inventory": sorted(set(consonants) | set(vowels), key=len, reverse=True),
        "coda_set": coda_set,
        "onset_set": onset_set,
        **template,
    }, None


def _phonology(packet):
    phonology = packet.get("phonology")
    if not isinstance(phonology, dict):
        return None, None, "packet declares no `phonology` mapping"
    profile, error = _build_profile(phonology)
    if profile is None:
        return None, {}, error
    profiles = {}
    raw_profiles = phonology.get("profiles")
    if isinstance(raw_profiles, dict):
        for name, source in raw_profiles.items():
            sub, _ = _build_profile(source)
            if sub is not None:
                profiles[_s(name)] = sub
    return profile, profiles, None


def _tokenize(sound_form, inventory):
    tokens = []
    pos = 0
    while pos < len(sound_form):
        for token in inventory:
            if sound_form.startswith(token, pos):
                tokens.append(token)
                pos += len(token)
                break
        else:
            return None, pos
    return tokens, None


def _syllable_ends(tokens, start, profile):
    ends = []
    total = len(tokens)
    cons = profile["cons_set"]
    vows = profile["vow_set"]
    for onset_len in range(profile["onset_min"], profile["onset_max"] + 1):
        pos = start + onset_len
        if pos > total:
            break
        onset = tokens[start:pos]
        if not all(token in cons for token in onset):
            continue
        if profile["onset_set"] is not None and not all(token in profile["onset_set"] for token in onset):
            continue
        for nuc_len in range(profile["nuc_min"], profile["nuc_max"] + 1):
            npos = pos + nuc_len
            if npos > total:
                break
            nucleus = tokens[pos:npos]
            if not all(token in vows for token in nucleus):
                continue
            for coda_len in range(profile["coda_min"], profile["coda_max"] + 1):
                cpos = npos + coda_len
                if cpos > total:
                    break
                coda = tokens[npos:cpos]
                if not all(token in cons for token in coda):
                    continue
                if profile["coda_set"] is not None and not all(token in profile["coda_set"] for token in coda):
                    continue
                ends.append(cpos)
    return ends


def _parse_word(tokens, profile):
    total = len(tokens)
    reachable = [False] * (total + 1)
    reachable[0] = True
    for i in range(total):
        if not reachable[i]:
            continue
        for end in _syllable_ends(tokens, i, profile):
            reachable[end] = True
    if reachable[total]:
        return None
    for i in range(total):
        if reachable[i] and not _syllable_ends(tokens, i, profile):
            return i
    return total


def _diagnose(tokens, stall, profile):
    token = tokens[stall]
    if token in profile["vow_set"]:
        return "PHON-STRUCTURE", f"cannot parse at token {stall + 1} ({token!r})"
    run = 0
    while stall + run < len(tokens) and tokens[stall + run] in profile["cons_set"]:
        run += 1
    if stall > 0 and tokens[stall - 1] in profile["vow_set"]:
        if profile["coda_max"] == 0:
            return "PHON-CODA", (
                f"/{token}/ cannot close the preceding syllable: template {profile['pattern']} licenses no coda"
            )
        if profile["coda_set"] is not None and token not in profile["coda_set"]:
            coda_list = ", ".join(sorted(profile["coda_set"]))
            return "PHON-CODA", f"/{token}/ cannot close the preceding syllable: declared coda set {{{coda_list}}}"
    if run > profile["onset_max"]:
        cluster = "".join(tokens[stall : stall + run])
        return "PHON-ONSET", (
            f"consonant cluster /{cluster}/ ({run} tokens) exceeds the licensed onset of "
            f"{profile['onset_max']} under template {profile['pattern']}"
        )
    return "PHON-NUCLEUS", f"/{token}/ at token {stall + 1} has no licensed vowel nucleus"


def _sound_form(form, separators, fold_case):
    sound = form
    for sep in separators:
        sound = sound.replace(sep, "")
    sound = sound.replace(" ", "")
    return sound.casefold() if fold_case else sound


# --------------------------------------------------------------------------
# gate A — uniqueness across the inventory
# --------------------------------------------------------------------------


def _finding(fid, level, message):
    return {"id": fid, "level": level, "message": message}


def _pair(a, b):
    return frozenset((a, b))


def _gate_a(records, packet, case_policy, seps):
    findings = []
    reported = set()

    # Layer 1: exact / canonical / case-policy / separator key.
    groups = {}
    for record in records:
        groups.setdefault(record["keys"]["primary"], []).append(record)
    for key in sorted(groups):
        group = groups[key]
        eids = []
        for record in group:
            if record["eid"] not in eids:
                eids.append(record["eid"])
        if len(eids) < 2:
            continue
        for a, b in combinations(eids, 2):
            reported.add(_pair(a, b))
        unidentified = [
            eid
            for eid in eids
            if any(r["cls"] == "names" and not r["declared_id"] for r in group if r["eid"] == eid)
        ]
        missing = [
            eid
            for eid in eids
            if not any(_decision_of(r["entry"]) for r in group if r["eid"] == eid)
        ]
        if unidentified:
            findings.append(
                _finding(
                    "NAME-ENTITY",
                    "HOLD",
                    f"collision at key {key!r} involves a name use without a stable entity "
                    f"id ({', '.join(unidentified)}); identity or coincidence cannot be decided",
                )
            )
            continue
        if missing:
            forms = sorted({record["form"] for record in group})
            reason = _layer_reason(forms, case_policy)
            findings.append(
                _finding(
                    "NAME-REUSE",
                    "FAIL",
                    f"entities {', '.join(eids)} share the unqualified key {key!r} ({reason}); "
                    f"no reuse/disambiguation decision recorded for {', '.join(missing)}; "
                    "record a decision or qualify the reference",
                )
            )

    # Layer 1b: case-only overlaps when no casing rule is declared.
    if not case_policy:
        groups = {}
        for record in records:
            groups.setdefault(record["keys"]["casefold"], []).append(record)
        for key in sorted(groups):
            group = groups[key]
            eids = []
            for record in group:
                if record["eid"] not in eids:
                    eids.append(record["eid"])
            pairs = [_pair(a, b) for a, b in combinations(eids, 2) if _pair(a, b) not in reported]
            if not pairs:
                continue
            for pair in pairs:
                reported.add(pair)
            involved = sorted({eid for pair in pairs for eid in pair})
            forms = sorted({record["form"] for record in group if record["eid"] in involved})
            findings.append(
                _finding(
                    "NAME-CASE",
                    "REVIEW",
                    f"entities {', '.join(involved)} differ only in letter case "
                    f"({', '.join(repr(f) for f in forms)}); the packet declares no casing rule — "
                    "decide whether case is display-only or contrastive for identity keys",
                )
            )

    # Layers 2-4: NFKC-only, diacritic-reduced, confusable skeleton.
    for key_name, fid, level, note in (
        ("compat", "NAME-COMPAT", "REVIEW", "NFKC compatibility overlap; never silently replace the stored form"),
        ("diacritic", "NAME-FOLD", "REVIEW", "lossy diacritic-reduced retrieval key; tone/length contrasts stay real"),
        ("skeleton", "NAME-VISUAL", "REVIEW", "UTS #39-style confusables subset: review visual channels, not linguistic equivalence"),
    ):
        groups = {}
        for record in records:
            groups.setdefault(record["keys"][key_name], []).append(record)
        for key in sorted(groups):
            group = groups[key]
            eids = []
            for record in group:
                if record["eid"] not in eids:
                    eids.append(record["eid"])
            pairs = [_pair(a, b) for a, b in combinations(eids, 2) if _pair(a, b) not in reported]
            if not pairs:
                continue
            for pair in pairs:
                reported.add(pair)
            involved = sorted({eid for pair in pairs for eid in pair})
            forms = sorted({record["form"] for record in group if record["eid"] in involved})
            findings.append(
                _finding(
                    fid,
                    level,
                    f"entities {', '.join(involved)} overlap on {key_name} key {key!r} "
                    f"(stored forms: {', '.join(repr(f) for f in forms)}); {note}",
                )
            )

    # Layer 5: spoken form under the declared reading rules.
    groups = {}
    for record in records:
        if record.get("compare_only") or not record.get("tokens"):
            continue
        groups.setdefault(tuple(record["tokens"]), []).append(record)
    for token_key in sorted(groups):
        group = groups[token_key]
        eids = []
        for record in group:
            if record["eid"] not in eids:
                eids.append(record["eid"])
        pairs = [_pair(a, b) for a, b in combinations(eids, 2) if _pair(a, b) not in reported]
        if not pairs:
            continue
        for pair in pairs:
            reported.add(pair)
        involved = sorted({eid for pair in pairs for eid in pair})
        findings.append(
            _finding(
                "NAME-REUSE",
                "FAIL",
                f"entities {', '.join(involved)} are homophones /{'/'.join(token_key)}/ "
                "under the declared reading rules; no reuse decision recorded",
            )
        )

    # Layer 6: recall-oriented edit distance.
    similarity = packet.get("similarity")
    threshold = 1
    enabled = True
    if isinstance(similarity, dict):
        if "max_distance" in similarity:
            try:
                threshold = int(similarity["max_distance"])
            except (TypeError, ValueError):
                threshold = 1
        if similarity.get("enabled") is False:
            enabled = False
    if enabled and threshold > 0:
        representatives = {}
        for record in records:
            representatives.setdefault(record["eid"], record)
        eids = sorted(representatives)
        for eid_a, eid_b in combinations(eids, 2):
            if _pair(eid_a, eid_b) in reported:
                continue
            rec_a, rec_b = representatives[eid_a], representatives[eid_b]
            if rec_a.get("compare_only") or rec_b.get("compare_only"):
                continue
            if rec_a.get("tokens") and rec_b.get("tokens"):
                seq_a, seq_b, channel = rec_a["tokens"], rec_b["tokens"], "phoneme tokens"
            else:
                seq_a = list(_nfc(rec_a["form"]).casefold())
                seq_b = list(_nfc(rec_b["form"]).casefold())
                channel = "display graphemes"
            if _edit_distance(seq_a, seq_b, cap=threshold) <= threshold:
                distance = _edit_distance(seq_a, seq_b)
                findings.append(
                    _finding(
                        "NAME-NEAR",
                        "REVIEW",
                        f"entities {eid_a} and {eid_b} are {distance} edit{'s' if distance != 1 else ''} "
                        f"apart on {channel} ({rec_a['form']!r} vs {rec_b['form']!r}, threshold <= {threshold}); "
                        "recall-oriented retrieval, not a confusion verdict",
                    )
                )

    # NAME-LEXEME: names vs the ordinary lexicon.
    lexicon = packet.get("lexicon")
    if isinstance(lexicon, list):
        terms = []
        for entry in lexicon:
            if not isinstance(entry, dict):
                continue
            term = _s(entry.get("term")).strip()
            if term:
                terms.append((term, _build_keys(term, case_policy, seps)["primary"]))
        for record in records:
            if record["cls"] != "names" or record.get("compare_only"):
                continue
            for term, term_key in terms:
                if term_key == record["keys"]["primary"] and not _decision_of(record["entry"]):
                    gloss = ""
                    for entry in lexicon:
                        if isinstance(entry, dict) and _s(entry.get("term")).strip() == term:
                            gloss = _s(entry.get("gloss"))
                            break
                    findings.append(
                        _finding(
                            "NAME-LEXEME",
                            "REVIEW",
                            f"name {record['eid']} {record['form']!r} equals lexicon term {term!r}"
                            + (f" ({gloss})" if gloss else "")
                            + "; decide intended namesake use or add a disambiguation",
                        )
                    )
                    break

    return findings


# --------------------------------------------------------------------------
# gate B — pronounceability under the named phonotactics
# --------------------------------------------------------------------------


def _prepare_sounds(records, packet, profile, profiles, case_fold, seps, findings):
    for record in records:
        record["tokens"] = None
        if record["cls"] not in ("names", "deity", "garment"):
            continue
        if record.get("compare_only"):
            continue
        entry = record["entry"]
        stage = _s(entry.get("stage")).strip().casefold() or "native"
        active = profile
        if stage not in ("native", "standard", "ordinary"):
            profile_name = _s(entry.get("profile")).strip()
            if profile_name and profile_name in profiles:
                active = profiles[profile_name]
            elif _has_text(_s(entry.get("adaptation"))) or entry.get("adapted") is True:
                active = profile
            else:
                findings.append(
                    _finding(
                        "PHON-HOLD",
                        "HOLD",
                        f"{record['cls']} {record['eid']} {record['form']!r} declares stage {stage!r} "
                        "without a declared profile or adaptation pathway; variant strata need their own profile",
                    )
                )
                continue
        sound = _sound_form(record["form"], seps, case_fold)
        if not sound:
            continue
        tokens, bad_pos = _tokenize(sound, active["inventory"])
        if tokens is None:
            symbol = sound[bad_pos]
            findings.append(
                _finding(
                    "PHON-INVENTORY",
                    "FAIL",
                    f"name {record['eid']} {record['form']!r}: symbol /{symbol}/ at position {bad_pos + 1} "
                    "is not in the declared inventory "
                    f"(consonants {{{', '.join(active['consonants'])}}}, vowels {{{', '.join(active['vowels'])}}})",
                )
            )
            continue
        record["tokens"] = tokens
        stall = _parse_word(tokens, active)
        if stall is None:
            continue
        fid, detail = _diagnose(tokens, stall, active)
        findings.append(
            _finding(fid, "FAIL", f"name {record['eid']} {record['form']!r} cannot be syllabified: {detail}")
        )


# --------------------------------------------------------------------------
# gate C — derivational validity
# --------------------------------------------------------------------------


def _derivation_rules(packet):
    morphology = packet.get("morphology")
    if not isinstance(morphology, dict):
        return None
    rules = morphology.get("derivation_rules")
    if not isinstance(rules, list):
        return None
    table = {}
    for entry in rules:
        if not isinstance(entry, dict):
            continue
        rid = _s(entry.get("id")).strip()
        if rid:
            table[rid] = entry
    return table or None


def _gate_c(records, packet):
    findings = []
    rules = _derivation_rules(packet)
    licensed_affixes = {}
    if rules:
        for rid, rule in rules.items():
            affix = _s(rule.get("affix")).strip()
            if affix:
                licensed_affixes.setdefault(affix, rid)
    for record in records:
        if record["cls"] != "names":
            continue
        entry = record["entry"]
        formation = entry.get("formation")
        if formation is None:
            formation = entry.get("derivation")
        opaque = entry.get("opaque") is True
        if formation is None:
            if not opaque and _has_text(_s(entry.get("etymology"))):
                findings.append(
                    _finding(
                        "DERIV-HOLD",
                        "HOLD",
                        f"name {record['eid']} {record['form']!r} claims an etymology but declares no formation "
                        "record or explicit opacity; derivation cannot be replayed",
                    )
                )
            continue
        if not isinstance(formation, dict):
            findings.append(
                _finding(
                    "DERIV-HOLD",
                    "HOLD",
                    f"name {record['eid']} {record['form']!r}: `formation` must be a mapping "
                    "(stem, rule/affix, gloss)",
                )
            )
            continue
        stem = _s(formation.get("stem")).strip()
        rule_id = _s(formation.get("rule") or formation.get("rule_id")).strip()
        affix = _s(formation.get("affix")).strip()
        if not stem:
            findings.append(
                _finding(
                    "DERIV-HOLD",
                    "HOLD",
                    f"name {record['eid']} {record['form']!r}: formation record has no stem lexeme; "
                    "the rule chain is not replayable",
                )
            )
            continue
        if rules is None:
            findings.append(
                _finding(
                    "DERIV-HOLD",
                    "HOLD",
                    f"name {record['eid']} {record['form']!r} claims a formation but the packet declares "
                    "no `morphology.derivation_rules`; cannot replay the chain",
                )
            )
            continue
        if rule_id:
            if rule_id not in rules:
                licensed = ", ".join(sorted(f"{a} ({r})" for a, r in licensed_affixes.items())) or "none"
                findings.append(
                    _finding(
                        "DERIV-AFFIX",
                        "FAIL",
                        f"name {record['eid']} {record['form']!r}: rule id {rule_id!r} is not licensed; "
                        f"licensed rules: {', '.join(sorted(rules)) or 'none'}; licensed affixes: {licensed}",
                    )
                )
                continue
            rule = rules[rule_id]
        elif affix:
            if affix not in licensed_affixes:
                licensed = ", ".join(sorted(f"{a} ({r})" for a, r in licensed_affixes.items())) or "none"
                findings.append(
                    _finding(
                        "DERIV-AFFIX",
                        "FAIL",
                        f"name {record['eid']} {record['form']!r}: affix {affix!r} is not licensed; "
                        f"licensed affixes: {licensed}; no rule produces this form",
                    )
                )
                continue
            rule = rules[licensed_affixes[affix]]
        else:
            findings.append(
                _finding(
                    "DERIV-HOLD",
                    "HOLD",
                    f"name {record['eid']} {record['form']!r}: formation record declares neither a rule nor an affix",
                )
            )
            continue
        pattern = _s(rule.get("pattern")).strip()
        output = _s(rule.get("output")).strip()
        rule_name = _s(rule.get("id")).strip() or affix or "rule"
        if not pattern or not output:
            findings.append(
                _finding(
                    "DERIV-HOLD",
                    "HOLD",
                    f"name {record['eid']} {record['form']!r}: rule {rule_name!r} lacks a machine-readable "
                    "`pattern`/`output` pair; replay is not possible",
                )
            )
            continue
        try:
            match = re.fullmatch(pattern, stem)
        except re.error as exc:
            findings.append(
                _finding(
                    "DERIV-HOLD",
                    "HOLD",
                    f"name {record['eid']} {record['form']!r}: rule {rule_name!r} pattern is not usable: {exc}",
                )
            )
            continue
        if match is None:
            findings.append(
                _finding(
                    "DERIV-REPLAY",
                    "FAIL",
                    f"name {record['eid']} {record['form']!r}: rule {rule_name!r} does not apply to stem {stem!r}; "
                    "the stated inputs and rules do not yield the candidate",
                )
            )
            continue
        try:
            replayed = output.format(**match.groupdict())
        except (KeyError, IndexError) as exc:
            findings.append(
                _finding(
                    "DERIV-HOLD",
                    "HOLD",
                    f"name {record['eid']} {record['form']!r}: rule {rule_name!r} output template cannot be "
                    f"resolved ({exc}); replay is not possible",
                )
            )
            continue
        expected = _nfc(replayed)
        actual = _nfc(record["form"])
        if _case_policy(packet):
            expected, actual = expected.casefold(), actual.casefold()
        if expected != actual:
            findings.append(
                _finding(
                    "DERIV-REPLAY",
                    "FAIL",
                    f"name {record['eid']} {record['form']!r}: declared chain {rule_name!r} applied to "
                    f"{stem!r} yields {replayed!r}; the stated inputs and rules do not yield the candidate",
                )
            )
    return findings


# --------------------------------------------------------------------------
# gate D — bounded cross-cultural collision review
# --------------------------------------------------------------------------


def _gate_d(packet):
    review = packet.get("cross_culture_review")
    if not isinstance(review, dict):
        review = packet.get("culture_review")
    if not isinstance(review, dict):
        return [
            _finding(
                "CROSS-HOLD",
                "HOLD",
                "packet declares no bounded cross-cultural review; D HOLD — a constructed string is not "
                "evidence of cross-cultural clearance (spec §9.6)",
            )
        ]
    findings = []
    open_items = review.get("unresolved") or review.get("open_questions")
    if isinstance(open_items, str):
        open_items = [open_items] if open_items.strip() else []
    if isinstance(open_items, list) and open_items:
        findings.append(
            _finding(
                "CROSS-HOLD",
                "HOLD",
                "review record keeps unresolved item(s): "
                + "; ".join(sorted(_s(item) for item in open_items if _has_text(_s(item)))),
            )
        )
    languages = review.get("languages")
    if languages is None:
        languages = review.get("reviewed_languages")
    if isinstance(languages, str):
        languages = [languages]
    if not isinstance(languages, list) or not languages:
        findings.append(
            _finding(
                "CROSS-HOLD",
                "HOLD",
                "review record names no priority language/community; 'no material hit in a bounded sweep' "
                "requires the languages, channels, and date actually searched",
            )
        )
        return findings
    for item in languages:
        if isinstance(item, str):
            continue
        if not isinstance(item, dict):
            findings.append(_finding("CROSS-HOLD", "HOLD", f"unrecognized review record: {_s(item)!r}"))
            continue
        language = _s(item.get("language") or item.get("name") or item.get("community")).strip() or "unnamed"
        result = _s(item.get("result") or item.get("finding")).casefold().replace("_", "-")
        note = _s(item.get("note") or item.get("evidence")).strip()
        suffix = f" ({note})" if note else ""
        if result in ("", "no-material-hit", "no-hit", "clear", "none", "reviewed-no-hit"):
            continue
        if result in (
            "hit", "flagged", "hold", "restricted", "sacred", "slur", "person",
            "endorsement", "franchise", "mark", "product",
        ):
            findings.append(
                _finding(
                    "CROSS-HIT",
                    "HOLD",
                    f"{language}: recorded hit {result!r}{suffix}; qualified contextual review is required "
                    "before public-facing use (spec §9.4)",
                )
            )
        elif result in ("resemblance", "ordinary", "word", "common-word", "review"):
            findings.append(
                _finding(
                    "CROSS-REVIEW",
                    "REVIEW",
                    f"{language}: ordinary resemblance recorded{suffix}; REVIEW, not automatic rejection",
                )
            )
        else:
            findings.append(
                _finding("CROSS-HOLD", "HOLD", f"{language}: unrecognized review result {result!r}; cannot evaluate")
            )
    return findings


# --------------------------------------------------------------------------
# packet evaluation
# --------------------------------------------------------------------------


def evaluate_packet(packet):
    findings = []
    records, record_notes, names_present = _collect_records(packet)
    case_policy = _case_policy(packet)
    seps = _separators(packet)
    for record in records:
        record["keys"] = _build_keys(record["form"], case_policy, seps)
        record["compare_only"] = record["entry"].get("compare_only") is True

    name_records = [record for record in records if record["cls"] == "names"]
    if not name_records:
        if names_present:
            findings.append(
                _finding(
                    "NAME-INVENTORY",
                    "HOLD",
                    "name-use inventory is present but empty; Gate A cannot compare anything",
                )
            )
        else:
            findings.append(
                _finding(
                    "NAME-INVENTORY",
                    "HOLD",
                    "packet supplies no `names` inventory; Gate A cannot evaluate uniqueness",
                )
            )
    for note in record_notes:
        findings.append(_finding("NAME-INVENTORY", "HOLD", note))

    for record in records:
        scripts, control = _script_check(record["form"])
        if control:
            findings.append(
                _finding(
                    "NAME-SCRIPT",
                    "REVIEW",
                    f"name use {record['eid']} {record['form']!r} contains control/format characters; "
                    "flag for inspection, do not delete indiscriminately",
                )
            )
        elif len(scripts) > 1:
            findings.append(
                _finding(
                    "NAME-SCRIPT",
                    "REVIEW",
                    f"name use {record['eid']} {record['form']!r} mixes scripts ({', '.join(scripts)}); "
                    "flag for inspection",
                )
            )

    profile, profiles, profile_error = _phonology(packet)
    phon_findings = []
    if profile is None:
        phon_findings.append(
            _finding("PHON-PROFILE", "HOLD", f"Gate B cannot evaluate: {profile_error}; record the missing evidence")
        )
    else:
        _prepare_sounds(
            records, packet, profile, profiles, not _case_contrastive(packet), seps, phon_findings
        )

    findings.extend(_gate_a(records, packet, case_policy, seps))
    findings.extend(phon_findings)
    findings.extend(_gate_c(records, packet))
    findings.extend(_gate_d(packet))
    return findings


def evaluate_text(text):
    try:
        root = load_yaml(text)
    except YamlError as exc:
        return EXIT_UNEVALUATED, [
            _finding("G-DATA", "HOLD", f"input could not be evaluated: {exc}")
        ]
    if isinstance(root, dict):
        packets = [root]
    elif isinstance(root, list):
        packets = root
    else:
        return EXIT_UNEVALUATED, [
            _finding("G-DATA", "HOLD", "input could not be evaluated: root is neither a mapping nor a list of mappings")
        ]
    if not packets:
        return EXIT_UNEVALUATED, [_finding("G-DATA", "HOLD", "input could not be evaluated: empty packet list")]
    findings = []
    multiple = len(packets) > 1
    for index, packet in enumerate(packets):
        if not isinstance(packet, dict):
            return EXIT_UNEVALUATED, [
                _finding("G-DATA", "HOLD", f"input could not be evaluated: packet {index + 1} is not a mapping")
            ]
        if not _has_text(_s(packet.get("name"))):
            return EXIT_UNEVALUATED, [
                _finding("G-DATA", "HOLD", f"input could not be evaluated: packet {index + 1} has no `name`")
            ]
        label = _s(packet.get("name")).strip()
        for finding in evaluate_packet(packet):
            if multiple:
                finding["message"] = f"[packet {label!r}] " + finding["message"]
            findings.append(finding)
    return (EXIT_CLEAN if not findings else EXIT_FINDINGS), findings


def format_finding(finding):
    return f"FINDING {finding['id']}: {finding['level']} — {finding['message']}"


# --------------------------------------------------------------------------
# selftest
# --------------------------------------------------------------------------

FIXTURE_EXPECTED = Counter(
    {
        "NAME-REUSE": 2,
        "NAME-VISUAL": 1,
        "NAME-NEAR": 1,
        "NAME-LEXEME": 1,
        "PHON-ONSET": 1,
        "PHON-CODA": 1,
        "PHON-INVENTORY": 1,
        "DERIV-AFFIX": 1,
        "DERIV-REPLAY": 1,
        "DERIV-HOLD": 1,
        "CROSS-HOLD": 1,
    }
)

POSITIVE_CONTROL = {
    "name": "F-positive-control",
    "phonology": {
        "consonants": ["p", "t", "k", "m", "n", "s", "l", "r"],
        "vowels": ["a", "i", "u"],
        "phonotactics": "(C)V(C)",
        "coda": ["n", "s"],
        "onset_clusters": False,
    },
    "orthography": {"case": "display-only"},
    "morphology": {
        "derivation_rules": [
            {
                "id": "R1",
                "kind": "suffix",
                "affix": "-in",
                "pattern": "^(?P<stem>.+)a$",
                "output": "{stem}in",
            }
        ]
    },
    "names": [
        {"name": "talin", "id": "F01", "type": "person", "formation": {"stem": "tala", "rule": "R1"}},
        {"name": "Talin", "alias_of": "F01", "relation": "alias", "type": "person"},
    ],
    "cross_culture_review": {
        "reviewed": "2026-10-17",
        "languages": [{"language": "F-toy (fixture-only)", "result": "no-material-hit"}],
    },
}


def selftest():
    here = Path(__file__).resolve().parent
    fixture_path = here / "fixtures" / "naming-collision-gate.yml"
    expected_path = here / "fixtures" / "naming-collision-gate.expected"

    text = fixture_path.read_text(encoding="utf-8")
    code, findings = evaluate_text(text)
    got = Counter(finding["id"] for finding in findings)
    expected_ids = [line.strip() for line in expected_path.read_text(encoding="utf-8").splitlines() if line.strip()]

    assert code == EXIT_FINDINGS, f"fixture must exit 1, got {code}: {[format_finding(f) for f in findings]}"
    assert set(expected_ids) == set(got), (
        f"expected-file ids {sorted(set(expected_ids))} != emitted ids {sorted(got)}"
    )
    assert set(FIXTURE_EXPECTED) == set(expected_ids), (
        "in-code expected counts and the committed .expected file disagree"
    )
    assert got == FIXTURE_EXPECTED, f"fixture finding counts changed: {dict(got)}"

    # F01's alias must not read as a second entity: the talin group names F01/F02 only.
    reuse_messages = [f["message"] for f in findings if f["id"] == "NAME-REUSE"]
    talin_messages = [m for m in reuse_messages if "'talin'" in m]
    assert len(talin_messages) == 1 and "F01" in talin_messages[0] and "F02" in talin_messages[0], reuse_messages
    assert "F03" not in talin_messages[0], reuse_messages

    # Positive control: complete stated derivation + recorded bounded review.
    positive_code, positive_findings = evaluate_text(_dump_yaml(POSITIVE_CONTROL))
    assert positive_code == EXIT_CLEAN, [format_finding(f) for f in positive_findings]
    assert positive_findings == [], positive_findings

    # Malformed input -> exit 2.
    bad_code, bad = evaluate_text("just a string")
    assert bad_code == EXIT_UNEVALUATED and bad[0]["id"] == "G-DATA", (bad_code, bad)
    bad_code, bad = evaluate_text("name: F\nnames: [\n")
    assert bad_code == EXIT_UNEVALUATED and bad[0]["id"] == "G-DATA", (bad_code, bad)
    bad_code, bad = evaluate_text("\tname: F\n")
    assert bad_code == EXIT_UNEVALUATED and bad[0]["id"] == "G-DATA", (bad_code, bad)

    # Missing phonology is tolerated as HOLD, not a crash, and other gates still run.
    lenient_code, lenient = evaluate_text(
        "name: F\nphonology: oops\nnames:\n  - name: tl\n    id: X1\n    type: place\n    opaque: true\n"
    )
    lenient_ids = {f["id"] for f in lenient}
    assert lenient_code == EXIT_FINDINGS, (lenient_code, lenient)
    assert {"PHON-PROFILE", "CROSS-HOLD"} <= lenient_ids, lenient_ids

    # Case policy is a declared rule: undeclared -> NAME-CASE REVIEW,
    # display-only -> NAME-REUSE FAIL (the F01/F02 path).
    case_probe = (
        "name: C\n"
        'phonology: {consonants: [p], vowels: [a], phonotactics: "(C)V"}\n'
        "names:\n"
        "  - {name: pa, id: A1, type: person, opaque: true}\n"
        "  - {name: Pa, id: A2, type: place, opaque: true}\n"
    )
    probe_code, probe = evaluate_text(case_probe)
    assert probe_code == EXIT_FINDINGS and "NAME-CASE" in {f["id"] for f in probe}, probe
    probe_declared_code, probe_declared = evaluate_text(
        "orthography: {case: display-only}\n" + case_probe
    )
    assert probe_declared_code == EXIT_FINDINGS, probe_declared
    assert "NAME-CASE" not in {f["id"] for f in probe_declared}, probe_declared
    assert "NAME-REUSE" in {f["id"] for f in probe_declared}, probe_declared

    print(
        f"selftest: OK — fixture findings {sum(got.values())} across {len(got)} ids "
        f"({', '.join(sorted(got))}); positive control clean; malformed inputs exit 2; "
        "missing profile held; case policy routed"
    )
    return EXIT_CLEAN


def _dump_yaml(node, indent=0):
    """Serialize the simple control dicts used by the selftest (no fixture dependency)."""
    pad = " " * indent
    if isinstance(node, dict):
        out = []
        for key, value in node.items():
            if isinstance(value, (dict, list)):
                out.append(f"{pad}{key}:")
                out.append(_dump_yaml(value, indent + 2))
            else:
                out.append(f"{pad}{key}: {_dump_scalar(value)}")
        return "\n".join(out)
    if isinstance(node, list):
        out = []
        for item in node:
            if isinstance(item, dict):
                rendered = _dump_yaml(item, indent + 2).splitlines()
                out.append(f"{pad}- {rendered[0].strip()}")
                out.extend(rendered[1:])
            elif isinstance(item, list):
                out.append(f"{pad}-")
                out.append(_dump_yaml(item, indent + 2))
            else:
                out.append(f"{pad}- {_dump_scalar(item)}")
        return "\n".join(out)
    return f"{pad}{_dump_scalar(node)}"


def _dump_scalar(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "" or any(ch in text for ch in ":#,{}[]\"'") or text != text.strip():
        return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return text


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv):
    args = list(argv[1:])
    if args and args[0] in ("--selftest", "--self-test"):
        return selftest()
    if len(args) != 1:
        sys.stderr.write("usage: naming-collision-gate.py <culture-packet.yml> | --selftest\n")
        return EXIT_UNEVALUATED
    path = Path(args[0])
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(format_finding(_finding("G-DATA", "HOLD", f"input could not be evaluated: {exc}")))
        return EXIT_UNEVALUATED
    except UnicodeDecodeError as exc:
        print(format_finding(_finding("G-DATA", "HOLD", f"input could not be evaluated: not UTF-8 text: {exc}")))
        return EXIT_UNEVALUATED
    code, findings = evaluate_text(text)
    for finding in findings:
        print(format_finding(finding))
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))