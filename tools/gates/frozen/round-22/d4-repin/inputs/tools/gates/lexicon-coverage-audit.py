#!/usr/bin/env python3
"""lexicon-coverage-audit — executable release gate for kotodama-shokunin.

Audits one culture packet (one declared language stage / dialect / register
set) for semantic-field coverage, derivational consistency, and loan-layer
coherence, per `corpus/knowledge/verification/lexicon-coverage-audit.md`
(checks C, D, L) and the seven field briefs in
`corpus/knowledge/linguistics/semantic-fields-lexicon-building.md` §4.

Interface
---------
    python3 tools/gates/lexicon-coverage-audit.py <culture-packet.yml>
    python3 tools/gates/lexicon-coverage-audit.py --selftest
    (`--self-test` is accepted as an alias, matching the sibling gates.)

One finding per line on stdout:

    FINDING <id>: <message>

Exit codes (only these three):

    0   clean — no findings printed
    1   one or more findings printed
    2   could-not-evaluate — the input is missing or malformed; the reason is
        printed to stderr as one or more `ERROR: <message>` lines and no
        FINDING line is printed for the whole packet

Input
-----
The culture packet is the shared fleet schema: name, phonology, morphology,
lexicon, pantheon, symbols, costumes, names, eras. Only `lexicon` is
mandatory here (a list of entries with term, gloss, field, etymology,
layer). A JSON packet (leading `{`) is accepted as well; anything else is
read with the small YAML subset parser below (block mappings and sequences,
flow `[...]`/`{...}`, quoted scalars, `#` comments, `---`/`...` markers).
Parsing is lenient: absent optional keys do not crash, they simply make the
affected check unevaluated.

Optional keys recognised by this gate
-------------------------------------
packet level
    eras            ordered era names; enables ordering checks (D, L)
    constructions   list (or name->record mapping) of word-building rules;
                    keys: name, pattern, base_classes, output_class,
                    description, productivity, base_eligibility
                    (`native-only`), available_from
    layers          list of contact layers; keys: name, donor, donor_stage,
                    entry_stage, channel, contact_window [era, era],
                    substitutions {donor: recipient}, referent_available_from
lexicon entry level
    route           inherited|root|derived|compound|borrowed|calque|
                    unresolved|lexicalized|irregular (absent: inferred from
                    the etymology text)
    bases           list of base terms for derived/compound entries
    construction    construction name (must resolve in `constructions`)
    class           word class of the entry (compared with base_classes)
    stage (or formation_stage)   era when the claim/formation holds
    noncompositional: true       requires a sense note
    sense_note / note / history / explanation    the note
    irregular / exception: true  requires a note (D-exception-unlicensed)
    loan_layer      name of the layer a borrowed entry belongs to
    donor_form      the donor-stage form (enables adaptation reproduction)

`pattern` templates use `B1`, `B2`, ... for bases in order; `-` and `+` mark
morpheme boundaries and are removed from the surface form (so pattern
`B1-sa` + base `vatha` must yield `vathasa`).

Finding IDs
-----------
Named in the spec (`verification/lexicon-coverage-audit.md`):
    C-required-gap            a required field or need has no expression
    C-contrast-lost           a required distinction is not recorded
    D-route-missing           §4 · no formation route recorded
    D-rule-underspecified     §4 · construction signature not reproducible
    D-form-mismatch           §4 · cannot rebuild form from recorded bases
    D-meaning-mismatch        §4 · noncompositional reading unrecorded
    D-stage-mismatch          §4 · base/construction not eligible at stage
    D-exception-unlicensed    §4 · exception without an explanation/scope
    D-rule-violation          §8 · rule applied to an excluded base
    L-contact-unsupported     §6 · declared contact history rules out route
    L-adaptation-mismatch     §6 · inconsistent with declared adaptation
    L-chronology-conflict     §6 · impossible event order
    L-integration-mismatch    §6 · borrowed base through ineligible rule
    L-material-anachronism    §6 · referent used before declared availability
Gate-level extensions (not named in the spec; same semantics of "blocking
until repaired or explicitly resolved"):
    C-count-inflation         spelling variants inflating a field inventory
    C-entry-unevaluable       entry without term, gloss, or field
    L-layer-unregistered      borrowed lexeme without a declared layer
    L-layer-incomplete        layer missing an indispensable record
                              (per-claim could-not-evaluate, reported as a
                              finding so a missing record never reads clean)

Scope limits (declared, not silently skipped)
---------------------------------------------
- F (frequency discipline, spec §5) is NOT implemented: this gate reads a
  lexicon packet, not a corpus, so no token/dispersion measurement exists to
  audit. A frequency claim cannot be certified by this gate.
- C is reduced to what a packet can show: the seven-field review-row
  inventory, recorded contrasts, and inventory hygiene. Per-need rows,
  critical-need classification, and exclusion acceptance live in the manual
  audit (spec §3, §8).
- C-count-inflation compares terms with diacritics folded away only when the
  packet declares no tone system; when `phonology.tones` is a positive
  integer, tone-marked forms are kept distinct, so a genuine minimal pair is
  never counted as an inventory duplicate.
- Fields outside the seven-field matrix and the declared extensions
  (costume, trade) are not audited and produce no finding.
- Ordering checks run only when the packet declares `eras`; absent era
  lists make the affected checks unevaluated and silent.
- This gate certifies consistency with the declared design. It never
  establishes canon, naturalness, or real-world attestation; canon and the
  world bible belong to lore-shokunin.
"""

import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

GATE_NAME = "lexicon-coverage-audit"
HERE = Path(__file__).resolve().parent
FIXTURE_PATH = HERE / "fixtures" / (GATE_NAME + ".yml")
EXPECTED_PATH = HERE / "fixtures" / (GATE_NAME + ".expected")

SEVEN_FIELDS = (
    "body",
    "kinship",
    "weather",
    "landscape",
    "subsistence",
    "war",
    "religion",
)
EXTENSION_FIELDS = ("costume", "trade")
FIELD_ALIASES = {
    "body": "body",
    "kinship": "kinship",
    "kin": "kinship",
    "weather": "weather",
    "landscape": "landscape",
    "subsistence": "subsistence",
    "war": "war",
    "warfare": "war",
    "religion": "religion",
    "costume": "costume",
    "dress": "costume",
    "garment": "costume",
    "trade": "trade",
    "exchange": "trade",
}
DERIVED_ROUTES = ("derived", "compound")
NOTE_KEYS = ("sense_note", "note", "history", "explanation")
ROUTE_KEYWORDS = (
    ("calque", r"\bcalque|loan[ -]?translation\b"),
    ("borrowed", r"\b(loan|borrow|borrowed|donor)\b"),
    ("compound", r"\bcompound\b"),
    ("derived", r"\b(deriv|suffix|prefix|affix)\b|[+\u2190]"),
    ("inherited", r"\b(inherit|reflex|descend)\b"),
    ("root", r"\b(root|coinage|coined|underived|invented)\b"),
    ("unresolved", r"\b(unresolved|unknown|opaque|uncertain|to-verify)\b"),
)


class PacketError(Exception):
    """Malformed packet or YAML subset parse failure (exit code 2)."""


# --------------------------------------------------------------------------
# YAML subset parser (block mappings/sequences, flow collections, comments)
# --------------------------------------------------------------------------


def _strip_comment(line):
    out = []
    quote = None
    i = 0
    n = len(line)
    while i < n:
        ch = line[i]
        if quote:
            out.append(ch)
            if quote == '"' and ch == "\\" and i + 1 < n:
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


def _unquote_scalar(token):
    s = token.strip()
    if len(s) >= 2 and s[0] == s[-1] == "'":
        return s[1:-1].replace("''", "'")
    if len(s) >= 2 and s[0] == s[-1] == '"':
        try:
            return json.loads(s)
        except ValueError:
            return s[1:-1]
    if s[:1] in ("&", "*", "!"):
        raise PacketError("anchor/alias/tag syntax is outside the declared subset: %r" % s[:40])
    if s in ("", "~", "null", "Null", "NULL"):
        return None
    if s in ("true", "True", "TRUE"):
        return True
    if s in ("false", "False", "FALSE"):
        return False
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    if re.fullmatch(r"-?\d+\.\d+", s):
        return float(s)
    return s


def _unquote_key(token):
    s = token.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        value = _unquote_scalar(s)
        return str(value)
    if s[:1] in ("&", "*", "!"):
        raise PacketError("anchor/alias/tag syntax is outside the declared subset: %r" % s[:40])
    return s


def _split_key(content):
    """Return (key, rest) for a mapping line, or (None, None)."""
    quote = None
    i = 0
    n = len(content)
    while i < n:
        ch = content[i]
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
        if ch == ":" and (i + 1 >= n or content[i + 1] in " \t"):
            key = content[:i].strip()
            if not key:
                raise PacketError("empty mapping key")
            return _unquote_key(key), content[i + 1:].strip()
        i += 1
    return None, None


def _flow_complete(text):
    depth = 0
    quote = None
    i = 0
    n = len(text)
    while i < n:
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
        elif ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        i += 1
    return depth <= 0 and quote is None


def _skip_ws(s, pos):
    while pos < len(s) and s[pos] in " \t":
        pos += 1
    return pos


def _flow_quoted(s, pos):
    quote = s[pos]
    start = pos
    pos += 1
    while pos < len(s):
        ch = s[pos]
        if quote == '"' and ch == "\\":
            pos += 2
            continue
        if ch == quote:
            if quote == "'" and pos + 1 < len(s) and s[pos + 1] == "'":
                pos += 2
                continue
            pos += 1
            return _unquote_scalar(s[start:pos]), pos
        pos += 1
    raise PacketError("unterminated quoted scalar in flow value")


def _flow_key(s, pos):
    """Return (key, pos_at_colon) for a flow-mapping key."""
    pos = _skip_ws(s, pos)
    if pos >= len(s):
        raise PacketError("unexpected end of flow mapping")
    if s[pos] in "\"'":
        value, pos = _flow_quoted(s, pos)
        return str(value), _skip_ws(s, pos)
    start = pos
    while pos < len(s) and s[pos] not in ":,]}":
        pos += 1
    key = s[start:pos].strip()
    if not key:
        raise PacketError("empty key in flow mapping")
    return _unquote_key(key), _skip_ws(s, pos)


def _flow_value(s, pos):
    pos = _skip_ws(s, pos)
    if pos >= len(s):
        raise PacketError("unexpected end of flow value")
    ch = s[pos]
    if ch == "[":
        items = []
        pos = _skip_ws(s, pos + 1)
        if pos < len(s) and s[pos] == "]":
            return items, pos + 1
        while True:
            value, pos = _flow_value(s, pos)
            items.append(value)
            pos = _skip_ws(s, pos)
            if pos >= len(s):
                raise PacketError("unterminated flow sequence")
            if s[pos] == ",":
                pos = _skip_ws(s, pos + 1)
                continue
            if s[pos] == "]":
                return items, pos + 1
            raise PacketError("expected ',' or ']' in flow sequence")
    if ch == "{":
        out = {}
        pos = _skip_ws(s, pos + 1)
        if pos < len(s) and s[pos] == "}":
            return out, pos + 1
        while True:
            key, pos = _flow_key(s, pos)
            if pos >= len(s) or s[pos] != ":":
                raise PacketError("expected ':' in flow mapping")
            pos = _skip_ws(s, pos + 1)
            value, pos = _flow_value(s, pos)
            flow_key = str(key)
            if flow_key in out:
                raise PacketError("duplicate key %r in flow mapping" % flow_key)
            out[flow_key] = value
            pos = _skip_ws(s, pos)
            if pos >= len(s):
                raise PacketError("unterminated flow mapping")
            if s[pos] == ",":
                pos = _skip_ws(s, pos + 1)
                continue
            if s[pos] == "}":
                return out, pos + 1
            raise PacketError("expected ',' or '}' in flow mapping")
    if ch in "\"'":
        return _flow_quoted(s, pos)
    start = pos
    while pos < len(s) and s[pos] not in ",]}":
        pos += 1
    return _unquote_scalar(s[start:pos]), pos


MAX_FLOW_DEPTH = 64


def _flow_nesting_too_deep(text, limit=MAX_FLOW_DEPTH):
    depth, quote = 0, None
    for ch in text:
        if quote:
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
        elif ch in "[{":
            depth += 1
            if depth > limit:
                return True
        elif ch in "]}":
            depth -= 1
    return False


def _parse_flow(text):
    if _flow_nesting_too_deep(text):
        raise PacketError(
            "flow nesting deeper than the supported %d levels" % MAX_FLOW_DEPTH)
    value, pos = _flow_value(text, 0)
    pos = _skip_ws(text, pos)
    if pos != len(text):
        raise PacketError("trailing characters in flow value: %r" % text[pos:])
    return value


class _Lines:
    __slots__ = ("rows",)

    def __init__(self, rows):
        self.rows = rows


def _collect_lines(text):
    rows = []
    for raw in text.splitlines():
        if "\t" in raw[: len(raw) - len(raw.lstrip("\t"))]:
            raise PacketError("tabs are not allowed for indentation")
        content = _strip_comment(raw).rstrip()
        if not content.strip():
            continue
        stripped = content.strip()
        if stripped in ("---", "..."):
            continue
        indent = len(content) - len(content.lstrip(" "))
        rows.append([indent, content.strip()])
    return _Lines(rows)


def _read_value(lines, row_index, rest):
    """Parse the value text `rest` taken from rows[row_index].

    Returns (value, next_row_index); a flow value may continue on the
    following rows.
    """
    if rest.startswith("[") or rest.startswith("{"):
        buf = rest
        i = row_index
        while not _flow_complete(buf):
            i += 1
            if i >= len(lines.rows):
                raise PacketError("unterminated flow value")
            buf += " " + lines.rows[i][1]
        return _parse_flow(buf), i + 1
    if rest == "":
        return None, row_index + 1
    return _unquote_scalar(rest), row_index + 1


def _parse_block(lines, i, indent):
    if i >= len(lines.rows):
        return None, i
    content = lines.rows[i][1]
    if content == "-" or content.startswith("- "):
        return _parse_seq(lines, i, indent)
    if content.startswith("[") or content.startswith("{"):
        return _read_value(lines, i, content)
    key, rest = _split_key(content)
    if key is None:
        return _unquote_scalar(content), i + 1
    return _parse_map(lines, i, indent)


def _parse_map(lines, i, indent):
    out = {}
    while i < len(lines.rows):
        row_indent, content = lines.rows[i]
        if row_indent < indent:
            break
        if row_indent > indent:
            raise PacketError("bad indentation near %r" % content)
        if content == "-" or content.startswith("- "):
            break
        key, rest = _split_key(content)
        if key is None:
            raise PacketError("expected a mapping entry near %r" % content)
        if key in out:
            raise PacketError("duplicate key %r" % key)
        row_index = i
        i += 1
        if rest == "" and i < len(lines.rows) and lines.rows[i][0] > indent:
            value, i = _parse_block(lines, i, lines.rows[i][0])
        else:
            value, i = _read_value(lines, row_index, rest)
        out[key] = value
    return out, i


def _parse_seq(lines, i, indent):
    out = []
    while i < len(lines.rows):
        row_indent, content = lines.rows[i]
        if row_indent < indent:
            break
        if row_indent > indent:
            raise PacketError("bad indentation near %r" % content)
        if not (content == "-" or content.startswith("- ")):
            break
        body = content[1:]
        lead = len(body) - len(body.lstrip(" "))
        after = body.strip()
        item_indent = row_indent + 1 + lead
        i += 1
        if after == "":
            if i < len(lines.rows) and lines.rows[i][0] > row_indent:
                value, i = _parse_block(lines, i, lines.rows[i][0])
            else:
                value = None
        else:
            lines.rows[i - 1] = [item_indent, after]
            value, i = _parse_block(lines, i - 1, item_indent)
        out.append(value)
    return out, i


def _json_object_no_duplicates(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("duplicate key %r in JSON mapping" % key)
        out[key] = value
    return out


def load_packet(text):
    """Parse a culture packet from YAML-subset text or JSON."""
    stripped = text.lstrip("\ufeff \r\n\t")
    if stripped.startswith("{") or stripped.startswith("["):
        try:
            return json.loads(stripped, object_pairs_hook=_json_object_no_duplicates)
        except ValueError as exc:
            raise PacketError("JSON packet did not parse: %s" % exc)
    lines = _collect_lines(text)
    if not lines.rows:
        raise PacketError("packet is empty")
    value, index = _parse_block(lines, 0, lines.rows[0][0])
    if index != len(lines.rows):
        raise PacketError("unparsed trailing content near %r" % lines.rows[index][1])
    return value


# --------------------------------------------------------------------------
# Normalisation helpers
# --------------------------------------------------------------------------


def _text(value):
    if value is None or isinstance(value, (dict, list)):
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value).strip()


def _compact(value):
    s = unicodedata.normalize("NFD", _text(value))
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", s).strip().casefold()


def _term_key(value, tones_declared):
    """Inventory key: tone marks stay distinct when the packet declares tones."""
    if tones_declared:
        s = unicodedata.normalize("NFC", _text(value))
        return re.sub(r"\s+", " ", s).strip().casefold()
    return _compact(value)


def _declares_tones(packet):
    phonology = packet.get("phonology")
    if not isinstance(phonology, dict):
        return False
    tones = phonology.get("tones")
    return isinstance(tones, int) and not isinstance(tones, bool) and tones > 0


def _as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        if "+" in value:
            return [part.strip() for part in value.split("+") if part.strip()]
        return [value] if value.strip() else []
    return [value]


def _era_index(eras, era):
    key = _compact(era)
    for idx, name in enumerate(eras):
        if _compact(name) == key:
            return idx
    return None


def _route_of(entry):
    """Return (route, source) where source is 'key', 'etymology', or 'none'."""
    explicit = _compact(entry.get("route"))
    if explicit:
        return explicit, "key"
    text = _text(entry.get("etymology"))
    if not text:
        return "", "none"
    low = text.casefold()
    for route, pattern in ROUTE_KEYWORDS:
        if re.search(pattern, low):
            return route, "etymology"
    if _compact(entry.get("layer")) in ("loan", "borrowed"):
        return "borrowed", "etymology"
    return "recorded", "etymology"


def _note_of(entry):
    for key in NOTE_KEYS:
        if _text(entry.get(key)):
            return True
    return False


def _flag(entry, *keys):
    for key in keys:
        value = entry.get(key)
        if value is True or _compact(value) in ("true", "yes", "1"):
            return True
    return False


# --------------------------------------------------------------------------
# The audit
# --------------------------------------------------------------------------


def audit_packet(packet):
    """Return a list of (finding_id, message) pairs for a parsed packet."""
    findings = []

    def add(fid, message):
        findings.append((fid, message))

    raw_entries = packet.get("lexicon")
    entries = []
    for item in raw_entries if isinstance(raw_entries, list) else []:
        entries.append(item if isinstance(item, dict) else None)

    eras = [name for name in _as_list(packet.get("eras")) if _text(name)]
    constructions = []
    raw_constructions = packet.get("constructions")
    if isinstance(raw_constructions, dict):
        for name, record in raw_constructions.items():
            merged = dict(record) if isinstance(record, dict) else {}
            merged.setdefault("name", name)
            constructions.append(merged)
    elif isinstance(raw_constructions, list):
        constructions = [c for c in raw_constructions if isinstance(c, dict)]
    construction_index = {_compact(c.get("name")): c for c in constructions if _text(c.get("name"))}

    raw_layers = packet.get("layers")
    layers = [l for l in raw_layers if isinstance(l, dict)] if isinstance(raw_layers, list) else []
    layer_index = {_compact(l.get("name")): l for l in layers if _text(l.get("name"))}

    tones_declared = _declares_tones(packet)

    # ----- C: seven-field coverage matrix --------------------------------
    field_buckets = {}
    for position, entry in enumerate(entries):
        label = "lexicon[%d]" % position
        if entry is None:
            add("C-entry-unevaluable", "%s is not a mapping; cannot be placed in a review row" % label)
            continue
        term = _text(entry.get("term"))
        gloss = _text(entry.get("gloss"))
        raw_field = _compact(entry.get("field"))
        field = FIELD_ALIASES.get(raw_field, "")
        missing = []
        if not term:
            missing.append("term")
        if not gloss:
            missing.append("gloss")
        if not raw_field:
            missing.append("field")
        if missing:
            add(
                "C-entry-unevaluable",
                "%s (%s) lacks %s; no review row can evaluate it"
                % (label, term or "unnamed entry", " and ".join(missing)),
            )
        if field in SEVEN_FIELDS or field in EXTENSION_FIELDS:
            bucket = field_buckets.setdefault(field, {"entries": [], "seen": {}})
            key = (_term_key(term, tones_declared), _compact(gloss))
            if key in bucket["seen"]:
                add(
                    "C-count-inflation",
                    "field '%s' counts '%s' and '%s' with the same gloss '%s'; spelling "
                    "variants or inflected forms must not inflate the inventory"
                    % (field, bucket["seen"][key], term, gloss),
                )
            else:
                bucket["seen"][key] = term
            bucket["entries"].append((term, gloss, _compact(entry.get("layer")) or "native"))

    for field in SEVEN_FIELDS:
        if field not in field_buckets:
            add(
                "C-required-gap",
                "field '%s' has no entries; every needed meaning there is a gap "
                "(unevaluated, not N/A)" % field,
            )

    for field, bucket in sorted(field_buckets.items()):
        by_gloss = {}
        for term, gloss, layer in bucket["entries"]:
            by_gloss.setdefault((gloss.casefold(), layer), []).append(term)
        for (gloss, layer), terms in by_gloss.items():
            distinct = sorted({_compact(t) for t in terms})
            if len(distinct) < 2:
                continue
            add(
                "C-contrast-lost",
                "field '%s' (layer '%s') records %s with the same gloss '%s'; the required "
                "contrast is not recorded" % (field, layer, " and ".join(sorted(terms)), gloss),
            )

    # ----- D: derivational consistency -----------------------------------
    term_index = {}
    record_index = {}
    for entry in entries:
        if isinstance(entry, dict):
            key = _compact(entry.get("term"))
            if key:
                term_index.setdefault(key, entry)
                record_index.setdefault(key, _text(entry.get("term")))

    derived_entries = []
    for position, entry in enumerate(entries):
        if not isinstance(entry, dict):
            continue
        label = _text(entry.get("term")) or "lexicon[%d]" % position
        route, source = _route_of(entry)
        if source == "none":
            add(
                "D-route-missing",
                "'%s' records no formation route (inherited, root, derived, compound, "
                "borrowed, calqued, or explicitly unresolved)" % label,
            )
            continue

        construction_name = _text(entry.get("construction"))
        construction = construction_index.get(_compact(construction_name)) if construction_name else None

        if route in DERIVED_ROUTES:
            derived_entries.append(entry)
            if not construction_name:
                if constructions:
                    add(
                        "D-rule-underspecified",
                        "'%s' is %s but names no construction; its formation rule cannot be "
                        "reproduced" % (label, route),
                    )
            elif construction is None and constructions:
                add(
                    "D-rule-underspecified",
                    "'%s' is built with construction '%s', which is not declared in the "
                    "packet's constructions registry" % (label, construction_name),
                )

        bases = [b for b in _as_list(entry.get("bases")) if _text(b)]
        for base in bases:
            if _compact(base) not in term_index:
                add(
                    "D-form-mismatch",
                    "'%s' lists base '%s', which is not a recorded lexeme or root; the "
                    "derivation cannot be rebuilt" % (label, base),
                )

        if construction is not None:
            pattern = _text(construction.get("pattern"))
            if pattern and bases:
                expected = pattern
                for index, base in enumerate(bases, start=1):
                    replacement = record_index.get(_compact(base), _text(base))
                    expected = re.sub(r"\bB%d\b" % index, lambda _m, r=replacement: r, expected)
                expected = expected.replace("+", "").replace("-", "")
                if _compact(expected) != _compact(label):
                    add(
                        "D-form-mismatch",
                        "'%s' does not reproduce from bases %s under construction '%s' "
                        "(expected '%s'); recorded form and rule disagree"
                        % (label, ", ".join(bases), construction_name, expected),
                    )
            allowed_classes = [_compact(c) for c in _as_list(construction.get("base_classes")) if _text(c)]
            if allowed_classes and bases:
                for base in bases:
                    base_entry = term_index.get(_compact(base))
                    base_class = _compact(base_entry.get("class")) if base_entry else ""
                    if base_class and base_class not in allowed_classes:
                        add(
                            "D-rule-violation",
                            "construction '%s' is restricted to base classes %s, but '%s' "
                            "applies it to '%s' (class '%s')"
                            % (
                                construction_name,
                                "/".join(allowed_classes),
                                label,
                                base,
                                base_class,
                            ),
                        )

        if _flag(entry, "noncompositional", "non_compositional") or re.search(
            r"\b(idiom|lexicali[sz]ed|fossili[sz]ed)\b", _text(entry.get("etymology")).casefold()
        ):
            if not _note_of(entry):
                add(
                    "D-meaning-mismatch",
                    "'%s' carries a noncompositional reading without a lexicalized sense or "
                    "history note" % label,
                )

        if route in ("irregular", "exception", "suppletive", "suppletion") or _flag(
            entry, "irregular", "exception", "suppletion"
        ):
            if not _note_of(entry):
                add(
                    "D-exception-unlicensed",
                    "'%s' is marked irregular/suppletive without an explanation (analogy, "
                    "taboo replacement, fossilization, or dialect mixture)" % label,
                )

        stage = entry.get("stage") if _text(entry.get("stage")) else entry.get("formation_stage")
        stage_at = _era_index(eras, stage) if eras and _text(stage) else None
        if stage_at is not None and construction is not None:
            available = _text(construction.get("available_from"))
            available_at = _era_index(eras, available) if available else None
            if available_at is not None and stage_at < available_at:
                add(
                    "D-stage-mismatch",
                    "'%s' is formed in '%s' but construction '%s' is only available from '%s'"
                    % (label, _text(stage), construction_name, available),
                )
        if stage_at is not None:
            for base in bases:
                base_entry = term_index.get(_compact(base))
                base_stage = _text(base_entry.get("stage")) if base_entry else ""
                base_at = _era_index(eras, base_stage) if base_stage else None
                if base_at is not None and base_at > stage_at:
                    add(
                        "D-stage-mismatch",
                        "'%s' is formed in '%s' but its base '%s' enters in '%s'"
                        % (label, _text(stage), base, base_stage),
                    )

    if derived_entries and not constructions:
        add(
            "D-rule-underspecified",
            "no constructions registry is declared; %d derived/compound lexeme(s) cannot be "
            "reproduced (could-not-evaluate for their formation rules)" % len(derived_entries),
        )

    # ----- L: loan-layer coherence ---------------------------------------
    for layer in layers:
        name = _text(layer.get("name")) or "unnamed layer"
        missing = [
            key
            for key in ("donor", "donor_stage", "entry_stage", "channel")
            if not _text(layer.get(key))
        ]
        if missing:
            add(
                "L-layer-incomplete",
                "layer '%s' lacks %s; could-not-evaluate the loans that depend on it"
                % (name, " and ".join(missing)),
            )
        window = [w for w in _as_list(layer.get("contact_window")) if _text(w)]
        entry_stage_at = _era_index(eras, layer.get("entry_stage")) if eras else None
        if len(window) == 2 and eras and entry_stage_at is not None:
            lo = _era_index(eras, window[0])
            hi = _era_index(eras, window[1])
            if lo is not None and hi is not None and not (lo <= entry_stage_at <= hi):
                add(
                    "L-contact-unsupported",
                    "layer '%s' declares contact only in '%s'-'%s' but its borrowing stage is "
                    "'%s'; the declared history rules out the required route"
                    % (name, window[0], window[1], _text(layer.get("entry_stage"))),
                )

    for position, entry in enumerate(entries):
        if not isinstance(entry, dict):
            continue
        label = _text(entry.get("term")) or "lexicon[%d]" % position
        is_loan = _compact(entry.get("layer")) in ("loan", "borrowed")
        bases = [b for b in _as_list(entry.get("bases")) if _text(b)]
        construction_name = _text(entry.get("construction"))
        construction = construction_index.get(_compact(construction_name)) if construction_name else None

        if is_loan:
            layer_name = _text(entry.get("loan_layer"))
            layer = layer_index.get(_compact(layer_name)) if layer_name else None
            if layer is None:
                add(
                    "L-layer-unregistered",
                    "borrowed lexeme '%s' references layer '%s', which is not declared; its "
                    "contact, adaptation, and chronology records are unevaluated"
                    % (label, layer_name or "(none)"),
                )
            else:
                layer_label = _text(layer.get("name"))
                entry_stage = entry.get("stage") if _text(entry.get("stage")) else entry.get("formation_stage")
                entry_at = _era_index(eras, entry_stage) if eras and _text(entry_stage) else None
                borrowing = _text(layer.get("entry_stage"))
                borrowing_at = _era_index(eras, borrowing) if eras and borrowing else None
                if entry_at is not None and borrowing_at is not None and entry_at < borrowing_at:
                    add(
                        "L-chronology-conflict",
                        "'%s' has its recorded form in '%s' but layer '%s' entered at '%s'; "
                        "the local form precedes the borrowing"
                        % (label, _text(entry_stage), layer_label, borrowing),
                    )
                available = _text(layer.get("referent_available_from"))
                available_at = _era_index(eras, available) if eras and available else None
                if entry_at is not None and available_at is not None and entry_at < available_at:
                    add(
                        "L-material-anachronism",
                        "'%s' is used in '%s' but layer '%s' dates its referent's availability "
                        "to '%s'" % (label, _text(entry_stage), layer_label, available),
                    )
                donor_form = _text(entry.get("donor_form"))
                substitutions = layer.get("substitutions")
                if donor_form and isinstance(substitutions, dict) and substitutions:
                    pairs = sorted(
                        ((_text(k), _text(v)) for k, v in substitutions.items() if _text(k)),
                        key=lambda pair: len(pair[0]),
                        reverse=True,
                    )
                    expected = donor_form
                    for donor_part, recipient_part in pairs:
                        expected = expected.replace(donor_part, recipient_part)
                    if _compact(expected) != _compact(label):
                        add(
                            "L-adaptation-mismatch",
                            "donor form '%s' adapted under layer '%s' yields '%s', but the "
                            "recorded form is '%s'; the adaptation record is inconsistent"
                            % (donor_form, layer_label, expected, label),
                        )

        if construction is not None and bases:
            native_only = _compact(construction.get("base_eligibility")) in ("native-only", "native only")
            if native_only:
                borrowed_base = [
                    base
                    for base in bases
                    if _compact(term_index.get(_compact(base), {}).get("layer")) in ("loan", "borrowed")
                ]
                if borrowed_base:
                    add(
                        "L-integration-mismatch",
                        "'%s' builds on borrowed base '%s' with construction '%s', which is "
                        "declared native-only"
                        % (label, ", ".join(borrowed_base), construction_name),
                    )

    return sorted(findings)


# --------------------------------------------------------------------------
# Command line
# --------------------------------------------------------------------------


def _run_on_text(text):
    if not isinstance(text, str):
        raise PacketError("packet did not parse to a mapping")
    packet = load_packet(text)
    if not isinstance(packet, dict):
        raise PacketError("packet root is not a mapping")
    lexicon = packet.get("lexicon")
    if lexicon is None:
        raise PacketError("required key 'lexicon' is missing")
    if not isinstance(lexicon, list):
        raise PacketError("'lexicon' must be a list of entries")
    if not lexicon:
        raise PacketError("'lexicon' is empty; nothing can be audited")
    return audit_packet(packet)


USAGE = """usage: lexicon-coverage-audit.py <culture-packet.yml>
       lexicon-coverage-audit.py --selftest

prints one finding per line as `FINDING <id>: <message>`;
exit 0 = clean, 1 = findings, 2 = could-not-evaluate (see docstring)"""


def main(argv):
    if not argv:
        sys.stderr.write("ERROR: missing packet path\n" + USAGE + "\n")
        return 2
    first = argv[0]
    if first in ("-h", "--help"):
        print(USAGE)
        return 0
    if first in ("--selftest", "--self-test"):
        return selftest()
    try:
        text = Path(first).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        sys.stderr.write("ERROR: cannot read %s: %s\n" % (first, exc))
        return 2
    try:
        findings = _run_on_text(text)
    except PacketError as exc:
        sys.stderr.write("ERROR: %s: %s\n" % (first, exc))
        return 2
    except RecursionError:
        sys.stderr.write(
            "ERROR: %s: flow nesting exceeds the supported depth\n" % first)
        return 2
    for fid, message in findings:
        print("FINDING %s: %s" % (fid, message))
    return 1 if findings else 0


# --------------------------------------------------------------------------
# Fixture and selftest
# --------------------------------------------------------------------------

FIXTURE_YAML = """\
# Fixture: lexicon-coverage-audit -- generated by `--selftest`; do not edit by hand.
# Culture is fictional; every form below is a design choice, not a real-world claim.
# Planted violation IDs (one of each unless noted):
#   C-required-gap, C-count-inflation, C-contrast-lost, C-entry-unevaluable (x2),
#   D-route-missing, D-rule-underspecified, D-form-mismatch, D-meaning-mismatch,
#   D-stage-mismatch (x2: base eligibility and construction availability),
#   D-exception-unlicensed, D-rule-violation,
#   L-layer-unregistered, L-layer-incomplete, L-contact-unsupported,
#   L-adaptation-mismatch, L-chronology-conflict, L-integration-mismatch,
#   L-material-anachronism
name: Vethari (gate fixture)
phonology:
  consonants: [p, t, k, s, m, n, l, r, v]
  vowels: [a, e, i, o, u]
  phonotactics: (C)V(C)
  tones: 0
  notable_rules:
    - "word-final vowel loss before the suffix -k"
morphology:
  type: agglutinative
  alignment: nom-acc
  word_order: SOV
eras: [Old Veth, Middle Veth, Late Veth]
constructions:
  - name: AGENT
    pattern: "B1-sa"
    base_classes: [verb]
    output_class: noun
    productivity: productive
    description: "agent noun from a verb base"
  - name: PLANT
    pattern: "B1-ku"
    base_classes: [noun]
    output_class: noun
    base_eligibility: native-only
    available_from: Middle Veth
    productivity: restricted
    description: "plant or material part term from a noun base"
layers:
  - name: Kulvan trade layer
    donor: Kulvan
    donor_stage: Kulvan Middle
    entry_stage: Middle Veth
    channel: river trade
    substitutions: {"ph": "p", "kh": "k"}
    referent_available_from: Middle Veth
  - name: Northern raids layer
    donor: Nordu
    donor_stage: Nordu Old
    entry_stage: Late Veth
    channel: raids and ransoms
  - name: Late liturgical layer
    donor: Kulvan
    donor_stage: Kulvan Late
    entry_stage: Late Veth
    # `channel` deliberately absent -> L-layer-incomplete
  - name: Coastal contact layer
    donor: Sarem
    donor_stage: Sarem Middle
    entry_stage: Middle Veth
    channel: coastal shipping
    contact_window: [Late Veth, Late Veth]   # excludes entry_stage -> L-contact-unsupported
  - name: Southern cloth import
    donor: Isku
    donor_stage: Isku Late
    entry_stage: Middle Veth
    channel: caravan
    referent_available_from: Late Veth     # term used before availability -> L-material-anachronism
pantheon:
  - name: Vetha
    role: hearth deity
    domain: weaving and grain
    era: Old Veth
symbols:
  - sign: loom-sign
    domain: subsistence
    era: Middle Veth
    notes: "design choice: weaver guild emblem"
costumes:
  - garment: tamik
    material: imported linen
    wearer_rank: merchant
    rite: market opening
    era: Middle Veth
names:
  - name: Kalupol
    type: place
    etymology: "kalu 'blood' + pol 'hill' (design choice)"
    era: Old Veth
lexicon:
  # body -- sahu/sahu(with macron) duplicate the same gloss -> C-count-inflation
  - {term: sahu, gloss: hand, field: body, layer: native, route: root, stage: Old Veth, class: noun}
  - {term: "sah\u016b", gloss: hand, field: body, layer: native, route: root, stage: Old Veth, class: noun}
  - term: kalu
    gloss: blood
    field: body
    layer: native
    route: root
    stage: Old Veth
    class: noun
  # kinship -- two terms, one gloss -> C-contrast-lost
  - term: hama
    gloss: kinsman
    field: kinship
    layer: native
    route: root
    class: noun
  - term: tiru
    gloss: kinsman
    field: kinship
    layer: native
    route: root
    class: noun
  # weather -- nema has no gloss -> C-entry-unevaluable
  - term: miwa
    gloss: rain
    field: weather
    layer: native
    route: root
    class: noun
  - term: nema
    field: weather
    layer: native
    route: root
    class: noun
  # landscape
  - term: tira
    gloss: stone
    field: landscape
    layer: native
    route: root
    stage: Old Veth
    class: noun
  # PLANT is only available from Middle Veth, tiraku is formed in Old Veth -> D-stage-mismatch
  - term: tiraku
    gloss: stone shard
    field: landscape
    layer: native
    route: derived
    construction: PLANT
    bases: [tira]
    stage: Old Veth
    class: noun
  - term: saru
    gloss: river
    field: landscape
    layer: native
    route: root
    class: noun
  # no route and no etymology -> D-route-missing
  - term: naku
    gloss: ford
    field: landscape
    layer: native
    class: noun
  - term: mish
    gloss: went (suppletive past)
    field: landscape
    layer: native
    route: irregular
    class: verb
    # no explanation note -> D-exception-unlicensed
  # subsistence
  - term: vatha
    gloss: to weave
    field: subsistence
    layer: native
    route: root
    stage: Old Veth
    class: verb
  # AGENT expects vatha-sa -> surface "vathasa", record has "vathas" -> D-form-mismatch
  - term: vathas
    gloss: weaver
    field: subsistence
    layer: native
    route: derived
    construction: AGENT
    bases: [vatha]
    stage: Old Veth
    class: noun
  - term: sara
    gloss: flax
    field: subsistence
    layer: native
    route: root
    stage: Old Veth
    class: noun
  # AGENT is restricted to verb bases, sara is a noun -> D-rule-violation
  - term: sarasa
    gloss: flax worker
    field: subsistence
    layer: native
    route: derived
    construction: AGENT
    bases: [sara]
    stage: Old Veth
    class: noun
  - term: mira
    gloss: to herd
    field: subsistence
    layer: native
    route: root
    stage: Late Veth
    class: verb
  # base mira enters in Late Veth but mirasa is formed in Old Veth -> D-stage-mismatch
  - term: mirasa
    gloss: herder
    field: subsistence
    layer: native
    route: derived
    construction: AGENT
    bases: [mira]
    stage: Old Veth
    class: noun
  # construction GERUND is not declared -> D-rule-underspecified
  - term: nemira
    gloss: haul (n.)
    field: subsistence
    layer: native
    route: derived
    construction: GERUND
    class: noun
  - term: parnu
    gloss: ingot
    field: subsistence
    layer: loan
    route: borrowed
    loan_layer: Kulvan trade layer
    donor_form: pharnu
    stage: Middle Veth
    class: noun
  # layer substitutions turn kharu into "karu"; recorded form keeps "kh" -> L-adaptation-mismatch
  - term: kharu
    gloss: charcoal
    field: subsistence
    layer: loan
    route: borrowed
    loan_layer: Kulvan trade layer
    donor_form: kharu
    stage: Middle Veth
    class: noun
  # costume
  - term: suru
    gloss: imported cloth
    field: costume
    layer: loan
    route: borrowed
    loan_layer: Kulvan trade layer
    donor_form: suru
    stage: Middle Veth
    class: noun
  # PLANT is native-only and suru is a borrowed base -> L-integration-mismatch
  - term: suruku
    gloss: cloth scrap
    field: costume
    layer: native
    route: derived
    construction: PLANT
    bases: [suru]
    stage: Middle Veth
    class: noun
  # referent available only from Late Veth, term used in Middle Veth -> L-material-anachronism
  - term: tamik
    gloss: patterned wrap
    field: costume
    layer: loan
    route: borrowed
    loan_layer: Southern cloth import
    donor_form: tamik
    stage: Middle Veth
    class: noun
  # contact_window excludes Middle Veth -> L-contact-unsupported
  - term: sirek
    gloss: shell bead
    field: costume
    layer: loan
    route: borrowed
    loan_layer: Coastal contact layer
    donor_form: sirek
    stage: Middle Veth
    class: noun
  # recorded form in Old Veth, layer entered in Late Veth -> L-chronology-conflict
  - term: kaldru
    gloss: silver band (payment)
    field: costume
    layer: loan
    route: borrowed
    loan_layer: Northern raids layer
    donor_form: kaldru
    stage: Old Veth
    class: noun
  # layer not declared anywhere -> L-layer-unregistered
  - term: hergu
    gloss: raider belt
    field: costume
    layer: loan
    route: borrowed
    loan_layer: Mountain confederation layer
    donor_form: hergu
    stage: Late Veth
    class: noun
  # religion
  # noncompositional reading with no note -> D-meaning-mismatch
  - term: palu
    gloss: sacred grove
    field: religion
    layer: native
    route: lexicalized
    noncompositional: true
    class: noun
  # layer lacks `channel` -> L-layer-incomplete
  - term: virta
    gloss: hymn
    field: religion
    layer: loan
    route: borrowed
    loan_layer: Late liturgical layer
    donor_form: virta
    stage: Late Veth
    class: noun
  # no field -> C-entry-unevaluable (second occurrence)
  - term: wilu
    gloss: song
    layer: native
    route: root
    class: noun
  # the war field is deliberately absent -> C-required-gap
"""

EXPECTED_IDS = (
    "C-count-inflation",
    "C-contrast-lost",
    "C-entry-unevaluable",
    "C-required-gap",
    "D-exception-unlicensed",
    "D-form-mismatch",
    "D-meaning-mismatch",
    "D-route-missing",
    "D-rule-underspecified",
    "D-rule-violation",
    "D-stage-mismatch",
    "L-adaptation-mismatch",
    "L-chronology-conflict",
    "L-contact-unsupported",
    "L-integration-mismatch",
    "L-layer-incomplete",
    "L-layer-unregistered",
    "L-material-anachronism",
)

CLEAN_PACKET_YAML = """\
name: Clean control (gate selftest)
eras: [Early, Late]
lexicon:
  - {term: a, gloss: hand, field: body, layer: native, route: root}
  - {term: b, gloss: kin, field: kinship, layer: native, route: root}
  - {term: c, gloss: rain, field: weather, layer: native, route: root}
  - {term: d, gloss: stone, field: landscape, layer: native, route: root}
  - {term: e, gloss: to sow, field: subsistence, layer: native, route: root}
  - {term: f, gloss: spear, field: war, layer: native, route: root}
  - {term: g, gloss: rite, field: religion, layer: native, route: root}
"""

NO_REGISTRY_PACKET_YAML = """\
name: No-registry control (gate selftest)
lexicon:
  - {term: a, gloss: hand, field: body, layer: native, route: derived}
"""

TONELESS_DUPLICATE_YAML = """\
name: Toneless duplicate control (gate selftest)
lexicon:
  - {term: ma, gloss: hand, field: body, layer: native, route: root}
  - {term: "m\\u00e1", gloss: hand, field: body, layer: native, route: root}
"""

TONAL_MINIMAL_PAIR_YAML = """\
name: Tonal minimal pair control (gate selftest)
phonology:
  tones: 3
lexicon:
  - {term: ma, gloss: hand, field: body, layer: native, route: root}
  - {term: "m\\u00e1", gloss: hand, field: body, layer: native, route: root}
"""

JSON_CONTROL = (
    '{"name": "JSON control", "lexicon": ['
    '{"term": "a", "gloss": "hand", "field": "body", "route": "root"}]}'
)


def _finding_ids(lines):
    ids = []
    for line in lines:
        if line.startswith("FINDING "):
            ids.append(line[len("FINDING "):].split(":", 1)[0].strip())
    return ids


def _pin_fixture(path, body):
    """Regenerate a committed fixture only when absent; never overwrite.

    The embedded constant is the pin; the committed file is a deterministic
    artifact of it. A present file is verified byte-for-byte and a divergent
    file is reported instead of overwritten, so tampering cannot be erased;
    regeneration writes atomically (temp file + rename).
    """
    data = body.encode("utf-8")
    if os.path.exists(path):
        with open(path, "rb") as handle:
            if handle.read() != data:
                return "divergent"
        return "verified"
    tmp = "%s.tmp-%d" % (path, os.getpid())
    with open(tmp, "wb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp, path)
    return "regenerated"


def _pin_fixture_or_fail(path, body):
    if _pin_fixture(path, body) == "divergent":
        print("SELFTEST FAIL: %s diverges from the embedded constant; "
              "refusing to overwrite (delete the file to regenerate it)" % path)
        return False
    return True


def selftest():
    checks = []

    def check(name, ok, detail=""):
        checks.append((name, ok, detail))

    FIXTURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not _pin_fixture_or_fail(FIXTURE_PATH, FIXTURE_YAML):
        return 1
    if not _pin_fixture_or_fail(EXPECTED_PATH, "".join(fid + "\n" for fid in EXPECTED_IDS)):
        return 1

    try:
        proc = subprocess.run(
            [sys.executable, str(Path(__file__).resolve()), str(FIXTURE_PATH)],
            capture_output=True,
            text=True,
        )
    except OSError as exc:  # pragma: no cover - environment failure
        proc = None
        print("SELFTEST FAIL: cannot spawn gate: %s" % exc)
        return 1

    lines = proc.stdout.splitlines()
    ids = _finding_ids(lines)
    got = set(ids)
    expected = set(EXPECTED_IDS)
    check("fixture exit code 1", proc.returncode == 1, "got exit %d" % proc.returncode)
    missing = sorted(expected - got)
    extra = sorted(got - expected)
    check("every planted finding ID appears", not missing, "missing: %s" % ", ".join(missing))
    check("no unplanned finding IDs", not extra, "extra: %s" % ", ".join(extra))
    check("fixture expected file matches", EXPECTED_PATH.read_text(encoding="utf-8").split() == list(EXPECTED_IDS))
    check(
        "fixture findings are self-describing",
        all(line.startswith("FINDING ") and len(line.split(":", 1)[1].strip()) > 8 for line in lines),
    )

    clean_ids = []
    clean_code = None
    try:
        clean_ids = _finding_ids_text(_run_on_text(CLEAN_PACKET_YAML))
        clean_code = 0 if not clean_ids else 1
    except PacketError as exc:
        clean_code = 2
        clean_ids = ["PACKETERROR:%s" % exc]
    check("clean control packet passes", clean_code == 0, "findings: %s" % ", ".join(clean_ids))

    try:
        no_registry = _finding_ids_text(_run_on_text(NO_REGISTRY_PACKET_YAML))
        check(
            "missing constructions registry is reported",
            "D-rule-underspecified" in no_registry,
            "findings: %s" % ", ".join(no_registry),
        )
    except PacketError as exc:
        check("missing constructions registry is reported", False, "PacketError: %s" % exc)

    try:
        json_ids = _finding_ids_text(_run_on_text(JSON_CONTROL))
        check(
            "JSON packet is accepted",
            "D-route-missing" not in json_ids and "C-entry-unevaluable" not in json_ids,
            "findings: %s" % ", ".join(json_ids),
        )
    except PacketError as exc:
        check("JSON packet is accepted", False, "PacketError: %s" % exc)

    try:
        toneless_ids = _finding_ids_text(_run_on_text(TONELESS_DUPLICATE_YAML))
        check(
            "toneless diacritic variant counts as inflation",
            "C-count-inflation" in toneless_ids,
            "findings: %s" % ", ".join(toneless_ids),
        )
    except PacketError as exc:
        check("toneless diacritic variant counts as inflation", False, "PacketError: %s" % exc)

    try:
        tonal_ids = _finding_ids_text(_run_on_text(TONAL_MINIMAL_PAIR_YAML))
        check(
            "tonal minimal pair is not counted as inflation",
            "C-count-inflation" not in tonal_ids,
            "findings: %s" % ", ".join(tonal_ids),
        )
    except PacketError as exc:
        check("tonal minimal pair is not counted as inflation", False, "PacketError: %s" % exc)

    for bad_text, why in (("lexicon:\n  - term: a\n", "missing gloss is a finding, not a crash"),):
        try:
            ids_bad = _finding_ids_text(_run_on_text(bad_text))
            check(why, "C-entry-unevaluable" in ids_bad, "findings: %s" % ", ".join(ids_bad))
        except PacketError as exc:
            check(why, False, "PacketError: %s" % exc)

    for bad_text, why in (
        ("name: x\n", "missing lexicon"),
        ("name: [unclosed\n", "malformed yaml"),
        ("just a scalar\n", "root is not a mapping"),
    ):
        try:
            _run_on_text(bad_text)
            check("could-not-evaluate: %s" % why, False, "no PacketError raised")
        except PacketError:
            check("could-not-evaluate: %s" % why, True)

    failures = [name for name, ok, _ in checks if not ok]
    for name, ok, detail in checks:
        print("%s %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + detail) if detail and not ok else ""))
    print("selftest: %d/%d checks passed" % (len(checks) - len(failures), len(checks)))
    if failures:
        print("failed: %s" % ", ".join(failures))
        return 1
    return 0


def _finding_ids_text(findings):
    return [fid for fid, _ in findings]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))