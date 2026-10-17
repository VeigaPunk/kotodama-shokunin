#!/usr/bin/env python3
"""Phonology sanity gate — executable kernel for
corpus/knowledge/verification/phonology-sanity-gate.md.

Interface
---------
    python3 tools/gates/phonology-sanity-gate.py <culture-packet.yml>
        Prints one finding per line as `FINDING <id>: <message>` on stdout;
        the message opens with its spec §1 level (`FAIL` or `REVIEW`) and
        carries a witness. Clean input prints nothing.
        Exit codes (no other codes are used here):
            0  clean              — every check this kernel implements passed
            1  findings           — at least one FAIL or REVIEW finding
            2  could-not-evaluate — unreadable/unparseable packet, or no
               usable `phonology` block (one G-DATA finding is printed)
        The finite-segment kernel's own 0/2/1 verdict numbers (spec §6) are
        deliberately not reused: this gate's exit 1 covers both spec levels,
        which stay visible in each finding's message.
    python3 tools/gates/phonology-sanity-gate.py -            # packet on stdin
    python3 tools/gates/phonology-sanity-gate.py --selftest
        (`--self-test` accepted as an alias.) Verifies the committed fixture
        pair tools/gates/fixtures/phonology-sanity-gate.yml and .expected
        against this file's embedded constants, regenerating a file
        atomically only when it is absent and refusing to overwrite divergent
        bytes; runs the gate on that fixture as a subprocess, asserts exit 1
        with every planted finding ID present, then runs the control cases
        below: a clean packet (exit 0), malformed packets (exit 2), and one
        case for each check the fixture does not plant.

Finding IDs (family / level / condition)
----------------------------------------
  G-DATA      REVIEW/exit 2  structural input failure: missing phonology key
  I-DUPLICATE FAIL   kernel §6 "I-DUPLICATE": duplicate or C∩V-overlapping token
  I-ALIAS     FAIL   kernel §6 "I-ALIAS": tokens that collide under NFC
  I-CANON     REVIEW §2 'g'/'ɡ' look-alikes need an explicit canonicalization
  I-SYM       REVIEW token is not a single IPA segment (orthography digraph,
                     undeclared letter sequence) — corpus §9.2
  I-SYLLABIC  REVIEW syllabic diacritic in the inventory (wider audit, spec §2)
  I-ROLE      FAIL   a consonant symbol is listed as a vowel (or vice versa)
  T-C         REVIEW distinct consonant count outside the WALS sample bands
  T-V         REVIEW distinct vowel qualities outside the observed bands
  T-TONE      REVIEW 5+ lexical tones declared (2-tone systems are most common)
  T-SYL       REVIEW template is complex (>=3 onset or >=2 coda slots)
  P-PATTERN   REVIEW phonotactics is absent or not a C/V syllable template
  P-NUCLEUS   FAIL   template with no vowel core (a margin may be empty,
                     never the nucleus — spec §2)
  P-CODA      REVIEW codas declared but no sonorant in the inventory
  P-ONSET     REVIEW two-consonant onset declared, under two consonants listed
  A-PARSE     REVIEW rule not recognizable as `src → dst / environment`
  A-CLASS     REVIEW rule conditions on a natural class, not finite contexts
  A-TONE      FAIL   tone rule declared while the packet says tones: 0
  M-ROUND     REVIEW front rounded vowel without same-height front unrounded
                     and back rounded peers (WALS ch. 11: "in most cases")
  M-VOICE     REVIEW voiced fricative with no voiceless fricative anywhere
                     (not required per place — WALS ch. 4)
  M-NASAL     REVIEW nasal with no oral consonant at that place (WALS ch. 18,
                     exception-aware: Aleut)
  M-EJECT     REVIEW ejective with no plain stop at that place (corpus §4)
  M-MID       REVIEW mid vowel qualities with no high vowel quality (corpus §4)
  M-CLASS     REVIEW no phonemic nasals, fricatives or bilabials in the
                     inventory (attested absences — WALS ch. 18)
  M-SONORITY  REVIEW complex onset: inspect sonority rise / explicit licensing
  I-UNKNOWN   FAIL   rule token (source or environment) is not a phoneme here
  A-ORDER     REVIEW same source, same environment, different outputs
  A-NEUTRAL   REVIEW rule neutralizes a phoneme into another phoneme's phone
  A-VACUOUS   REVIEW the declared template makes the rule's adjacency
                     environment impossible (spec §5 rule-coverage prompt)
  X-NAME      REVIEW apostrophe in an entity name: decorative punctuation does
                     not supply a phonemic contrast (spec §7)

Scope that stays outside this kernel (spec §§2, 5, 7)
-----------------------------------------------------
 * Spec §6's finite-segment kernel takes a different input contract
   (inventory/phones/qualities/legal/rules/examples/priors). The culture
   packet carries no example corpus, so derivation checks (A-DERIVE), surface
   role spans (P-SR), empirical rule coverage (A-COVER witnesses) and the §6
   NFC kernel are not run here.
 * Syllabic consonants, tone/stress systems, vowel harmony, moras,
   epenthesis/deletion, optional or probabilistic rules, morpheme boundaries,
   cross-word sandhi, boundary/prosody audits: outside the kernel (spec §2);
   syllabic inventory entries are flagged (I-SYLLABIC) so they are not lost.
 * Prose or class-based rules are REVIEW (A-CLASS / A-PARSE), never silently
   accepted; expansion into finite contextual rules stays a human step.

Engineering choices (this kernel's, not linguistic universals — spec §1)
------------------------------------------------------------------------
 * Band thresholds follow Maddieson 2013, WALS chs. 1–2, 12 (verified against
   wals.info/chapter/1 on 2026-10-17: 6–14 small, 15–18 moderately small,
   19–25 average, 26–33 moderately large, >=34 large, sample range 6–122).
   Outside-band results are REVIEW, never automatic rejection (spec §3).
 * Markedness priors are REVIEW prompts instantiated from spec §4 plus
   corpus §4's implication list (M-EJECT, M-MID); none is a hard universal.
 * `phonotactics` is read as one C/V syllable template (`(C)(C)V(C)(C)`);
   alternants split on `/` or `|` are merged at their widest margin.
 * Feature tables simplify the IPA chart (three vowel heights, coarse places,
   no feature geometry); they drive prompts, not claims about real languages.
 * Segment classification decomposes tokens with NFD so precomposed diacritic
   letters (ĩ ẽ õ) land on their base symbol; the inventory's own NFC policy
   is checked separately (I-ALIAS), and Latin umlaut spellings are flagged as
   orthography (I-SYM).
 * Glottal /h ɦ/ is not counted as a fricative for M-VOICE / M-CLASS,
   following WALS ch. 18's explicit exclusion.
 * A-VACUOUS fires only when the template makes the rule's adjacent
   environment impossible in any role (e.g. consonant adjacency with no CC
   onset and no coda) — a deliberately conservative approximation.

Sources: Maddieson 2013 (WALS chs. 1, 2, 4, 11, 12, 18); Hayes 2009;
Greenberg 1963 / Maddieson 1984 (via corpus §4); Yip 2002 (via corpus §6);
International Phonetic Association 1999. stdlib only; no network.
"""

import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE_PATH = os.path.join(HERE, "fixtures", "phonology-sanity-gate.yml")
EXPECTED_PATH = os.path.join(HERE, "fixtures", "phonology-sanity-gate.expected")

# --------------------------------------------------------------------------
# reference tables — an engineering simplification of the IPA chart
# --------------------------------------------------------------------------

# quality: (height, backness, rounding); three heights, coarse backness
VOWEL_FEATURES = {
    "i": ("high", "front", "unrounded"),
    "y": ("high", "front", "rounded"),
    "ɨ": ("high", "central", "unrounded"),
    "ʉ": ("high", "central", "rounded"),
    "ɯ": ("high", "back", "unrounded"),
    "u": ("high", "back", "rounded"),
    "ɪ": ("high", "near-front", "unrounded"),
    "ʏ": ("high", "near-front", "rounded"),
    "ʊ": ("high", "near-back", "rounded"),
    "e": ("mid", "front", "unrounded"),
    "ø": ("mid", "front", "rounded"),
    "ɘ": ("mid", "central", "unrounded"),
    "ɵ": ("mid", "central", "rounded"),
    "ɤ": ("mid", "back", "unrounded"),
    "o": ("mid", "back", "rounded"),
    "ə": ("mid", "central", "unrounded"),
    "ɛ": ("mid", "front", "unrounded"),
    "œ": ("mid", "front", "rounded"),
    "ɜ": ("mid", "central", "unrounded"),
    "ɞ": ("mid", "central", "rounded"),
    "ʌ": ("mid", "back", "unrounded"),
    "ɔ": ("mid", "back", "rounded"),
    "æ": ("low", "front", "unrounded"),
    "ɐ": ("low", "central", "unrounded"),
    "a": ("low", "central", "unrounded"),
    "ɑ": ("low", "back", "unrounded"),
    "ɒ": ("low", "back", "rounded"),
    "ɶ": ("low", "front", "rounded"),
    "ɚ": ("mid", "central", "unrounded"),
    "ɝ": ("mid", "central", "unrounded"),
}

# consonant: (place, manner, voicing); manner set below
CONSONANT_FEATURES = {
    "p": ("bilabial", "plosive", "voiceless"),
    "b": ("bilabial", "plosive", "voiced"),
    "t": ("alveolar", "plosive", "voiceless"),
    "d": ("alveolar", "plosive", "voiced"),
    "ʈ": ("retroflex", "plosive", "voiceless"),
    "ɖ": ("retroflex", "plosive", "voiced"),
    "c": ("palatal", "plosive", "voiceless"),
    "ɟ": ("palatal", "plosive", "voiced"),
    "k": ("velar", "plosive", "voiceless"),
    "ɡ": ("velar", "plosive", "voiced"),
    "g": ("velar", "plosive", "voiced"),
    "q": ("uvular", "plosive", "voiceless"),
    "ɢ": ("uvular", "plosive", "voiced"),
    "ʡ": ("epiglottal", "plosive", "voiceless"),
    "ʔ": ("glottal", "plosive", "voiceless"),
    "m": ("bilabial", "nasal", "voiced"),
    "ɱ": ("labiodental", "nasal", "voiced"),
    "n": ("alveolar", "nasal", "voiced"),
    "ɳ": ("retroflex", "nasal", "voiced"),
    "ɲ": ("palatal", "nasal", "voiced"),
    "ŋ": ("velar", "nasal", "voiced"),
    "ɴ": ("uvular", "nasal", "voiced"),
    "ʙ": ("bilabial", "trill", "voiced"),
    "r": ("alveolar", "trill", "voiced"),
    "ʀ": ("uvular", "trill", "voiced"),
    "ⱱ": ("labiodental", "tap", "voiced"),
    "ɾ": ("alveolar", "tap", "voiced"),
    "ɽ": ("retroflex", "tap", "voiced"),
    "ɸ": ("bilabial", "fricative", "voiceless"),
    "β": ("bilabial", "fricative", "voiced"),
    "f": ("labiodental", "fricative", "voiceless"),
    "v": ("labiodental", "fricative", "voiced"),
    "θ": ("dental", "fricative", "voiceless"),
    "ð": ("dental", "fricative", "voiced"),
    "s": ("alveolar", "fricative", "voiceless"),
    "z": ("alveolar", "fricative", "voiced"),
    "ʃ": ("postalveolar", "fricative", "voiceless"),
    "ʒ": ("postalveolar", "fricative", "voiced"),
    "ʂ": ("retroflex", "fricative", "voiceless"),
    "ʐ": ("retroflex", "fricative", "voiced"),
    "ç": ("palatal", "fricative", "voiceless"),
    "ʝ": ("palatal", "fricative", "voiced"),
    "x": ("velar", "fricative", "voiceless"),
    "ɣ": ("velar", "fricative", "voiced"),
    "χ": ("uvular", "fricative", "voiceless"),
    "ʁ": ("uvular", "fricative", "voiced"),
    "ħ": ("pharyngeal", "fricative", "voiceless"),
    "ʕ": ("pharyngeal", "fricative", "voiced"),
    "ʜ": ("epiglottal", "fricative", "voiceless"),
    "ʢ": ("epiglottal", "fricative", "voiced"),
    "h": ("glottal", "fricative", "voiceless"),
    "ɦ": ("glottal", "fricative", "voiced"),
    "ɬ": ("alveolar", "lateral-fricative", "voiceless"),
    "ɮ": ("alveolar", "lateral-fricative", "voiced"),
    "ʋ": ("labiodental", "approximant", "voiced"),
    "ɹ": ("alveolar", "approximant", "voiced"),
    "ɻ": ("retroflex", "approximant", "voiced"),
    "j": ("palatal", "approximant", "voiced"),
    "ɰ": ("velar", "approximant", "voiced"),
    "ɥ": ("labial-palatal", "approximant", "voiced"),
    "w": ("labial-velar", "approximant", "voiced"),
    "ʍ": ("labial-velar", "fricative", "voiceless"),
    "l": ("alveolar", "lateral", "voiced"),
    "ɭ": ("retroflex", "lateral", "voiced"),
    "ʎ": ("palatal", "lateral", "voiced"),
    "ʟ": ("velar", "lateral", "voiced"),
    "ɺ": ("alveolar", "tap", "voiced"),
    "ɓ": ("bilabial", "implosive", "voiced"),
    "ɗ": ("alveolar", "implosive", "voiced"),
    "ᶑ": ("retroflex", "implosive", "voiced"),
    "ʄ": ("palatal", "implosive", "voiced"),
    "ɠ": ("velar", "implosive", "voiced"),
    "ʛ": ("uvular", "implosive", "voiced"),
    "ʘ": ("bilabial", "click", "voiceless"),
    "ǀ": ("dental", "click", "voiceless"),
    "ǃ": ("alveolar", "click", "voiceless"),
    "ǂ": ("postalveolar", "click", "voiceless"),
    "ǁ": ("alveolar", "click", "voiceless"),
}

SONORANT_MANNERS = {"nasal", "trill", "tap", "approximant", "lateral"}
FRICATIVE_MANNERS = {"fricative", "lateral-fricative"}
EJECTIVE_MARKS = set("ʼ’'ˀ")
# modifier letters that stay part of a segment token (aspiration, labialization,
# tie bars are combining marks and pass the category test below)
EXTRA_MODIFIERS = set("ʰʱʲʷˠˤˀʼːˑ˥˦˧˨˩ᵐⁿᵑˡ'’")
SYLLABIC_MARKS = {"\u0329", "\u030d", "\u0311"}
ORTHOGRAPHY_DIGRAPHS = {
    "th", "sh", "ch", "ph", "gh", "wh", "ck", "ng", "qu", "tch", "dg", "zh",
}
CLASS_LETTERS = set("VCNSPTKGLAUIR")
TONE_WORDS = re.compile(r"\btones?\b|\btone[sd]\b|\bpitch\b", re.I)
TONE_MARKS = set("˥˦˧˨˩") | {"\u0301", "\u0300", "\u0304", "\u030c",
                              "\u030b", "\u0302", "\u0306"}
NAME_APOSTROPHES = {"'", "’"}
RULE_ARROW = re.compile(r"→|⟶|⇒|->|=>|>")
RULE_RE = re.compile(
    r"^\s*(?P<src>.+?)\s*(?:→|⟶|⇒|->|=>|>)\s*(?P<dst>[^/]*?)\s*(?:/\s*(?P<env>.*))?$"
)
DELETION_TOKENS = {"∅", "⌀", "-", "0", "Ø"}


# --------------------------------------------------------------------------
# a lenient reader for the shared culture-packet YAML subset
#
# The subset is closed: input outside it (tab indentation, anchor/alias/tag
# syntax, unbalanced flow collections, duplicate mapping keys in block
# mappings, flow mappings or sequence mapping entries) raises PacketError and
# exits 2 — a colliding key is a packet the author must fix, never a silent
# last-wins merge.
# --------------------------------------------------------------------------

class PacketError(Exception):
    pass


def _strip_comment(line):
    out, quote = [], None
    for i, ch in enumerate(line):
        if quote is not None:
            out.append(ch)
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            out.append(ch)
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            break
        else:
            out.append(ch)
    return "".join(out).rstrip()


def _preprocess(text):
    lines = []
    for lineno, raw in enumerate(text.splitlines(), 1):
        if "\t" in raw[: len(raw) - len(raw.lstrip(" \t"))]:
            raise PacketError("tab indentation is not supported by this subset "
                              "(line %d)" % lineno)
        line = _strip_comment(raw.replace("\t", "  "))
        if not line.strip():
            continue
        lines.append((len(line) - len(line.lstrip(" ")), line.strip(), lineno))
    return lines


MAX_FLOW_DEPTH = 64


def _flow_parts(body):
    parts, depth, quote, cur = [], 0, None, ""
    for ch in body:
        if depth > MAX_FLOW_DEPTH:
            raise PacketError(
                "flow nesting deeper than the supported %d levels" % MAX_FLOW_DEPTH)
        if quote is not None:
            cur += ch
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
            cur += ch
        elif ch in "[{":
            depth += 1
            cur += ch
        elif ch in "]}":
            depth -= 1
            cur += ch
        elif ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur)
    return parts


def _parse_scalar(s):
    s = s.strip()
    if s.startswith("["):
        if not s.endswith("]"):
            raise PacketError("unterminated flow sequence: %r" % s[:40])
        body = s[1:-1]
        return [_parse_scalar(p) for p in _flow_parts(body)]
    if s.startswith("{"):
        if not s.endswith("}"):
            raise PacketError("unterminated flow mapping: %r" % s[:40])
        body = s[1:-1]
        result = {}
        for part in _flow_parts(body):
            key, sep, val = part.partition(":")
            if not sep:
                raise PacketError("flow mapping entry without ':'")
            key = str(_parse_scalar(key))
            if key in result:
                raise PacketError("duplicate key %r in flow mapping" % key)
            result[key] = _parse_scalar(val)
        return result
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    if s[:1] in ("&", "*", "!"):
        raise PacketError("anchor/alias/tag syntax is outside the declared subset: %r" % s[:40])
    if s in ("null", "~", "None"):
        return None
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    if s in ("true", "false", "True", "False"):
        return s.lower() == "true"
    return s


def _is_seq_item(content):
    return content == "-" or content.startswith("- ")


def _parse_sequence(lines, i, indent):
    items = []
    while i < len(lines):
        cur_indent, content, lineno = lines[i]
        if cur_indent < indent:
            break
        if not _is_seq_item(content):
            break
        if cur_indent > indent:
            raise PacketError("unexpected indent at line %d" % lineno)
        rest = content[1:].strip()
        if not rest:
            i += 1
            if i < len(lines) and lines[i][0] > indent:
                item, i = _parse_block(lines, i, lines[i][0])
            else:
                item = None
            items.append(item)
            continue
        if rest.startswith("{") or rest.startswith("["):
            items.append(_parse_scalar(rest))
            i += 1
            continue
        if re.match(r"^[^:\s][^:]*:(\s|$)", rest):
            entry = {}
            key, _, val = rest.partition(":")
            key = str(_parse_scalar(key.strip()))
            val = val.strip()
            i += 1
            if val:
                entry[key] = _parse_scalar(val)
            elif i < len(lines) and lines[i][0] > indent:
                entry[key], i = _parse_block(lines, i, lines[i][0])
            else:
                entry[key] = None
            while i < len(lines) and lines[i][0] > indent and not _is_seq_item(lines[i][1]):
                sub, i = _parse_block(lines, i, lines[i][0])
                if isinstance(sub, dict):
                    clash = sorted(set(sub) & set(entry))
                    if clash:
                        raise PacketError("duplicate key %r in mapping entry"
                                          % clash[0])
                    entry.update(sub)
                else:
                    break
            items.append(entry)
            continue
        items.append(_parse_scalar(rest))
        i += 1
    return items, i


def _parse_mapping(lines, i, indent):
    result = {}
    while i < len(lines):
        cur_indent, content, lineno = lines[i]
        if cur_indent < indent:
            break
        if cur_indent > indent:
            raise PacketError("unexpected indent at line %d" % lineno)
        if _is_seq_item(content):
            break
        key, sep, val = content.partition(":")
        if not sep:
            raise PacketError("missing ':' at line %d" % lineno)
        key = str(_parse_scalar(key.strip()))
        if key in result:
            raise PacketError("duplicate key %r at line %d" % (key, lineno))
        val = val.strip()
        if val:
            result[key] = _parse_scalar(val)
            i += 1
            continue
        i += 1
        if i < len(lines) and lines[i][0] > indent:
            result[key], i = _parse_block(lines, i, lines[i][0])
        elif i < len(lines) and lines[i][0] == indent and _is_seq_item(lines[i][1]):
            result[key], i = _parse_sequence(lines, i, indent)
        else:
            result[key] = None
    return result, i


def _parse_block(lines, i, indent):
    if _is_seq_item(lines[i][1]):
        return _parse_sequence(lines, i, indent)
    return _parse_mapping(lines, i, indent)


def parse_packet(text):
    lines = _preprocess(text)
    if not lines:
        raise PacketError("empty document")
    value, i = _parse_block(lines, 0, lines[0][0])
    if i != len(lines):
        raise PacketError("unparsed content at line %d" % lines[i][2])
    return value


# --------------------------------------------------------------------------
# token classification
# --------------------------------------------------------------------------

def clean_token(value):
    if not isinstance(value, str):
        return None
    return value.strip().strip("/[]").strip()


def as_token_list(value):
    if value is None:
        return None
    if isinstance(value, str):
        items = [p for p in re.split(r"[,\s]+", value) if p]
        return items or None
    if isinstance(value, list):
        out = []
        for item in value:
            token = clean_token(item)
            if token:
                # lenient: a list item may itself carry several tokens
                out.extend(p for p in re.split(r"[,\s]+", token) if p)
            elif isinstance(item, (int, float)):
                out.append(str(item))
        return out or None
    return None


def split_token(token):
    """(base, marks); marks are combining diacritics / modifier letters.

    NFD is used so precomposed diacritic letters (ẽ ĩ õ ṽ …) decompose onto
    their base symbol instead of reading as unknown segments.
    """
    marks, base = [], []
    for ch in unicodedata.normalize("NFD", token):
        if unicodedata.category(ch) in ("Mn", "Me") or ch in EXTRA_MODIFIERS:
            marks.append(ch)
        else:
            base.append(ch)
    return "".join(base), "".join(marks)


def classify(token):
    """Return a feature dict, or {'kind': 'unknown'|'orthography', 'base':...}."""
    base, marks = split_token(token)
    if not base:
        return {"kind": "unknown", "base": token}
    ejective = any(m in EJECTIVE_MARKS for m in marks)
    if len(base) == 1:
        ch = base
        if ch in VOWEL_FEATURES:
            height, backness, rounding = VOWEL_FEATURES[ch]
            return {"kind": "vowel", "token": token, "base": ch,
                    "height": height, "backness": backness,
                    "rounding": rounding}
        if ch in CONSONANT_FEATURES:
            place, manner, voice = CONSONANT_FEATURES[ch]
            return {"kind": "consonant", "token": token, "base": ch,
                    "place": place, "manner": manner, "voice": voice,
                    "ejective": ejective}
        return {"kind": "unknown", "base": base}
    if base in ORTHOGRAPHY_DIGRAPHS:
        return {"kind": "orthography", "base": base}
    if len(base) == 2:
        first = CONSONANT_FEATURES.get(base[0])
        second = CONSONANT_FEATURES.get(base[1])
        if (first and second and first[1] == "plosive"
                and second[1] in ("fricative", "lateral-fricative")):
            return {"kind": "consonant", "token": token, "base": base,
                    "place": second[0], "manner": "affricate",
                    "voice": first[2], "ejective": ejective}
    return {"kind": "unknown", "base": base}


def is_syllabic(token):
    return any(m in SYLLABIC_MARKS for m in split_token(token)[1])


def place_family(place):
    if place in ("dental", "alveolar"):
        return "dental-alveolar"
    if place in ("postalveolar", "retroflex"):
        return "postalveolar-retroflex"
    return place


def is_fricative(feat):
    # WALS ch. 18 excludes glottal /h ɦ/ from the fricative class
    return feat["manner"] in FRICATIVE_MANNERS and feat["place"] != "glottal"


def label(feat):
    return "/%s/" % feat["token"]


def names_of(feats):
    return " ".join(sorted(label(f) for f in feats))


# --------------------------------------------------------------------------
# phonotactics template
# --------------------------------------------------------------------------

def parse_template(pattern):
    """Return {'onset': n, 'nucleus': n, 'coda': n} or None."""
    if not isinstance(pattern, str) or not pattern.strip():
        return None
    best = None
    for alt in re.split(r"[|/]", pattern.strip()):
        if not alt.strip():
            continue
        symbols = []
        for ch in alt:
            if ch in " \t":
                continue
            if ch in "()":   # parentheses mark optionality, not a slot
                continue
            upper = ch.upper()
            if upper in ("C", "V"):
                symbols.append(upper)
            else:
                return None
        if not symbols:
            return None
        runs = []
        for sym in symbols:
            if runs and runs[-1][0] == sym:
                runs[-1][1] += 1
            else:
                runs.append([sym, 1])
        onset = max((r[1] for i, r in enumerate(runs)
                     if r[0] == "C" and i + 1 < len(runs) and runs[i + 1][0] == "V"),
                    default=0)
        nucleus = max((r[1] for r in runs if r[0] == "V"), default=0)
        coda = runs[-1][1] if runs[-1][0] == "C" else 0
        shape = {"onset": onset, "nucleus": nucleus, "coda": coda}
        if best is None or shape["onset"] + shape["coda"] > best["onset"] + best["coda"]:
            best = shape
    return best


# --------------------------------------------------------------------------
# allophony rules
# --------------------------------------------------------------------------

def parse_rule(text):
    if not isinstance(text, str):
        return None
    match = RULE_RE.match(text)
    if not match:
        return None
    src = (match.group("src") or "").strip()
    dst = (match.group("dst") or "").strip()
    env = (match.group("env") or "").strip()
    if not src or not dst:
        return None
    left, right = "", ""
    if env:
        if "_" in env:
            left, right = env.split("_", 1)
        else:
            left = env
    def side_tokens(side):
        return [t for t in (clean_token(p) for p in re.split(r"[\s,+]+", side)) if t]
    return {"raw": text, "src": clean_token(src), "dst": clean_token(dst),
            "env": env, "left": side_tokens(left), "right": side_tokens(right)}


def is_class_token(token):
    if not token:
        return False
    if token in ("#", "$", "∅", "⌀", "-"):
        return False
    if token.startswith("[") or "+" in token or "-" in token or "±" in token:
        return True
    # uppercase only: lowercase /i u a t r l/ are concrete IPA segments
    if len(token) == 1 and token in CLASS_LETTERS:
        return True
    return False


# --------------------------------------------------------------------------
# the gate
# --------------------------------------------------------------------------

def evaluate(packet):
    findings = []

    def add(level, fid, msg):
        findings.append((level, fid, msg))

    if not isinstance(packet, dict):
        return 2, [("UNEVALUABLE", "G-DATA",
                    "packet root is not a mapping — nothing to evaluate")]
    phonology = packet.get("phonology")
    if not isinstance(phonology, dict):
        return 2, [("UNEVALUABLE", "G-DATA",
                    "no usable 'phonology' mapping in the packet — nothing to evaluate")]

    cons_raw = as_token_list(phonology.get("consonants"))
    vow_raw = as_token_list(phonology.get("vowels"))
    if not cons_raw and not vow_raw:
        return 2, [("UNEVALUABLE", "G-DATA",
                    "phonology declares neither 'consonants' nor 'vowels' — "
                    "inventory checks could not evaluate")]
    if cons_raw is None:
        add("REVIEW", "G-DATA",
            "phonology.consonants is missing — consonant checks could not evaluate")
        cons_raw = []
    if vow_raw is None:
        add("REVIEW", "G-DATA",
            "phonology.vowels is missing — vowel quality checks could not evaluate")
        vow_raw = []

    # ---- inventory hygiene ------------------------------------------------
    all_raw = cons_raw + vow_raw
    def duplicates(tokens):
        seen = {}
        for token in tokens:
            seen[token] = seen.get(token, 0) + 1
        return sorted(t for t, n in seen.items() if n > 1)

    dup = duplicates(cons_raw) + duplicates(vow_raw)
    overlap = sorted(set(cons_raw) & set(vow_raw))
    if dup or overlap:
        witness = ", ".join("'%s' x%d" % (t, cons_raw.count(t) + vow_raw.count(t))
                            for t in dup) or ", ".join("'%s'" % t for t in overlap)
        add("FAIL", "I-DUPLICATE",
            "duplicate token(s) in the inventory: %s — each phoneme is listed "
            "once; C and V must not overlap (kernel §6 I-DUPLICATE)" % witness)

    nfc_pairs = {}
    for token in all_raw:
        nfc_pairs.setdefault(unicodedata.normalize("NFC", token), set()).add(token)
    for normalized, variants in sorted(nfc_pairs.items()):
        if len(variants) > 1:
            add("FAIL", "I-ALIAS",
                "distinct tokens %s normalize to the same IPA under NFC — "
                "canonicalize before counting contrasts (kernel §6 I-ALIAS)"
                % " ".join(sorted("'%s'" % v for v in variants)))
    non_nfc = sorted(t for t in all_raw if unicodedata.normalize("NFC", t) != t)
    if non_nfc:
        add("FAIL", "I-ALIAS",
            "token(s) not in NFC form: %s — normalize spellings, do not split "
            "combining marks or affricates (spec §2)" % " ".join(non_nfc))

    lookalikes = [("g", "ɡ"), ("ʔ", "Ɂ")]
    for left, right in lookalikes:
        if left in all_raw and right in all_raw:
            add("REVIEW", "I-CANON",
                "'%s' and '%s' (U+%04X) are both listed: look-alike codepoints "
                "need an explicit canonicalization decision, not silent "
                "substitution (spec §2)" % (left, right, ord(right)))

    umlaut = sorted({t for t in all_raw
                     if any(ch in "äëïöüÿÄËÏÖÜŸ"
                            for ch in unicodedata.normalize("NFC", t))})
    if umlaut:
        add("REVIEW", "I-SYM",
            "token(s) %s use Latin umlaut spellings: 'ü ö ä' are orthography, "
            "not IPA symbols — write /y ø œ/ (or invoke the centralization "
            "diacritic deliberately) so the inventory can be charted "
            "[IPA 1999; corpus §9.2]"
            % " ".join("'%s'" % t for t in umlaut))

    cons_feats, vow_feats = [], []
    for token in cons_raw:
        feat = classify(token)
        if is_syllabic(token):
            add("REVIEW", "I-SYLLABIC",
                "token '%s' carries the syllabic diacritic: syllabic-consonant "
                "nuclei are outside this kernel's checks (wider audit — spec §2)"
                % token)
            continue
        if feat["kind"] == "vowel":
            add("FAIL", "I-ROLE",
                "token '%s' is a vowel symbol listed among the consonants — "
                "fix the C/V role split (kernel §6 inventory roles)" % token)
            continue
        if feat["kind"] == "orthography":
            add("REVIEW", "I-SYM",
                "token '%s' is not a single IPA segment (English-orthography "
                "digraph); IPA has no such symbol — declare the analysis or "
                "write the IPA segment (corpus §9.2)" % token)
            continue
        if feat["kind"] == "unknown":
            add("REVIEW", "I-SYM",
                "token '%s' is not recognized as one IPA segment or affricate; "
                "letters are not phonemes — declare the analysis (corpus §9.2)"
                % token)
            continue
        cons_feats.append(feat)
    for token in vow_raw:
        feat = classify(token)
        if feat["kind"] == "consonant":
            add("FAIL", "I-ROLE",
                "token '%s' is a consonant symbol listed among the vowels — "
                "fix the C/V role split (kernel §6 inventory roles)" % token)
            continue
        if feat["kind"] in ("orthography", "unknown"):
            add("REVIEW", "I-SYM",
                "token '%s' is not recognized as an IPA vowel segment; declare "
                "the analysis (corpus §9.2)" % token)
            continue
        vow_feats.append(feat)

    distinct_cons = sorted({f["token"] for f in cons_feats})
    qualities = {}
    for feat in vow_feats:
        qualities.setdefault((feat["height"], feat["backness"], feat["rounding"]),
                             []).append(feat)

    # ---- typology bands (spec §3) ----------------------------------------
    # (the WALS ch. 1 sample runs from 6 to 122 consonants)
    if distinct_cons and (len(distinct_cons) < 6 or len(distinct_cons) >= 34):
        add("REVIEW", "T-C",
            "%d distinct consonants — outside the WALS sample bands (6–14 "
            "small; 15–18 moderately small; 19–25 average; 26–33 moderately "
            "large; >=34 large); outside-sample size requires investigation, "
            "never automatic rejection [Maddieson 2013, WALS ch. 1]"
            % len(distinct_cons))
    if len(qualities) < 2 and vow_feats:
        add("REVIEW", "T-V",
            "%d basic vowel quality/qualities %s — below the observed bands "
            "(<=4 small; 5–6 average; >=7 large); report phonemic vowel "
            "contrasts separately [Maddieson 2013, WALS ch. 2]"
            % (len(qualities), " ".join(sorted(f["token"] for f in vow_feats))))
    elif len(qualities) > 9:
        add("REVIEW", "T-V",
            "%d basic vowel qualities — very large; check whether length, "
            "nasality or phonation variants were counted as new timbres "
            "(count /i iː ĩ/ once if the basic quality is the same) "
            "[Maddieson 2013, WALS ch. 2]" % len(qualities))

    tones = phonology.get("tones")
    if tones is None:
        add("REVIEW", "G-DATA",
            "phonology.tones is missing — the tone-structure check could not evaluate")
    else:
        # a YAML boolean is an int in Python but is not a tone count
        if isinstance(tones, bool) or not isinstance(tones, int):
            try:
                tones = int(str(tones).strip())
            except (TypeError, ValueError):
                tones = None
        if tones is None:
            add("REVIEW", "G-DATA",
                "phonology.tones is not an integer — the tone-structure check "
                "could not evaluate")
        elif tones < 0:
            add("REVIEW", "G-DATA",
                "phonology.tones is negative — the tone-structure check could "
                "not evaluate")
        elif tones >= 5:
            add("REVIEW", "T-TONE",
                "%d lexical tones declared — 2-tone systems are the most common "
                "and 5+ are rare; not an automatic rejection [Yip 2002, via "
                "corpus §6]" % tones)

    # ---- phonotactics legality -------------------------------------------
    template_raw = phonology.get("phonotactics")
    template = parse_template(template_raw)
    if template is None:
        if isinstance(template_raw, str) and template_raw.strip():
            add("REVIEW", "P-PATTERN",
                "phonotactics '%s' could not be parsed as a C/V syllable "
                "template — legality checks could not evaluate" % template_raw)
        else:
            add("REVIEW", "P-PATTERN",
                "phonotactics is missing or not a pattern string — legality "
                "checks could not evaluate (schema: phonology.phonotactics)")
    else:
        if template["nucleus"] < 1:
            add("FAIL", "P-NUCLEUS",
                "syllable template '%s' has no vowel core — a margin may be "
                "empty, never the nucleus (spec §2)" % template_raw)
        if template["onset"] >= 3 or template["coda"] >= 2:
            add("REVIEW", "T-SYL",
                "syllable template '%s' is complex (%d onset, %d coda slots): "
                "inspect the allowed combinations, not the maximum length "
                "[Maddieson 2013, WALS ch. 12]"
                % (template_raw, template["onset"], template["coda"]))
        if template["onset"] >= 2:
            sonorant_bases = sorted({f["token"] for f in cons_feats
                                     if f["manner"] in SONORANT_MANNERS
                                     and f["manner"] != "nasal"})
            note = ("" if sonorant_bases else
                    "; the inventory offers no liquid/glide/approximant, so "
                    "only obstruent sequences or an explicit licence are available")
            add("REVIEW", "M-SONORITY",
                "complex onset declared (%d slots): check the sonority rise "
                "toward the nucleus — /s/+stop licensing or another explicit "
                "analysis may be needed [Hayes 2009; spec §4]%s"
                % (template["onset"], note))
        if template["coda"] >= 1:
            sonorants = [f for f in cons_feats if f["manner"] in SONORANT_MANNERS]
            if cons_feats and not sonorants:
                add("REVIEW", "P-CODA",
                    "coda slots are declared but no sonorant (nasal, liquid, "
                    "glide) is in the inventory: codas are typically restricted "
                    "to sonorants — licence the coda or restrict the template "
                    "[Maddieson 2013, WALS ch. 12; corpus §3]")
        if template["onset"] >= 2 and len(distinct_cons) < 2:
            add("REVIEW", "P-ONSET",
                "a two-consonant onset is declared but fewer than two distinct "
                "consonants are listed in the inventory")

    # ---- markedness priors (spec §4; corpus §4) --------------------------
    for feat in vow_feats:
        if (feat["backness"] in ("front", "near-front")
                and feat["rounding"] == "rounded"):
            peers = [p for p in vow_feats if p["height"] == feat["height"]]
            missing = []
            if not any(p["backness"] in ("front", "near-front")
                       and p["rounding"] == "unrounded" for p in peers):
                missing.append("front unrounded")
            if not any(p["backness"] in ("back", "near-back")
                       and p["rounding"] == "rounded" for p in peers):
                missing.append("back rounded")
            if missing:
                add("REVIEW", "M-ROUND",
                    "front rounded %s (%s height) without a same-height %s "
                    "vowel: the implication holds 'in most cases', not "
                    "universally — add a peer or record the exception "
                    "[Maddieson 2013, WALS ch. 11]"
                    % (label(feat), feat["height"], " and ".join(missing)))

    voiced_fric = [f for f in cons_feats if is_fricative(f) and f["voice"] == "voiced"]
    voiceless_fric = [f for f in cons_feats if is_fricative(f) and f["voice"] == "voiceless"]
    if voiced_fric and not voiceless_fric:
        add("REVIEW", "M-VOICE",
            "voiced fricative(s) %s with no voiceless fricative anywhere in "
            "the inventory: ch. 4 documents inventories with only voiced "
            "fricatives, so a voiceless counterpart at every place is NOT "
            "required — record the analysis [Maddieson 2013, WALS ch. 4]"
            % names_of(voiced_fric))

    for feat in cons_feats:
        if feat["manner"] != "nasal":
            continue
        family = place_family(feat["place"])
        peers = [o for o in cons_feats if o is not feat and o["manner"] != "nasal"
                 and place_family(o["place"]) == family]
        if not peers:
            add("REVIEW", "M-NASAL",
                "nasal %s with no oral consonant at the %s place: "
                "exception-aware — Aleut has bilabial nasals without bilabial "
                "oral stops or fricatives; note the analysis and allophones "
                "[Maddieson 2013, WALS ch. 18]" % (label(feat), feat["place"]))

    for feat in cons_feats:
        if not feat["ejective"]:
            continue
        if not any(o["manner"] == "plosive" and not o["ejective"]
                   and place_family(o["place"]) == place_family(feat["place"])
                   for o in cons_feats):
            add("REVIEW", "M-EJECT",
                "ejective %s with no plain stop at the %s place: ejectives "
                "imply plain stops (a statistical tendency, not a universal) — "
                "add the peer or record the exception [Greenberg 1963; "
                "Maddieson 1984, via corpus §4]"
                % (label(feat), feat["place"]))

    if any(f["height"] == "mid" for f in vow_feats) and \
            not any(f["height"] == "high" for f in vow_feats):
        add("REVIEW", "M-MID",
            "mid vowel qualities without any high vowel quality: mid vowels "
            "imply high (a statistical tendency) [Greenberg 1963; Maddieson "
            "1984, via corpus §4]")

    if cons_feats:
        absent = []
        if not any(f["manner"] == "nasal" for f in cons_feats):
            absent.append("nasals")
        if not any(is_fricative(f) for f in cons_feats):
            absent.append("fricatives")
        if not any(f["place"] == "bilabial" for f in cons_feats):
            absent.append("bilabials")
        if absent:
            add("REVIEW", "M-CLASS",
                "no phonemic %s in the inventory: such absences are attested "
                "(a language with nasal phones need not have nasal phonemes) — "
                "inspect the analysis and allophones before repairing "
                "[Maddieson 2013, WALS ch. 18]" % ", ".join(absent))

    # ---- allophony consistency against the packet ------------------------
    rules_raw = phonology.get("notable_rules")
    rules = []
    if rules_raw is None:
        add("REVIEW", "G-DATA",
            "phonology.notable_rules is missing — allophony consistency could "
            "not evaluate")
    elif not isinstance(rules_raw, list) or not rules_raw:
        add("REVIEW", "G-DATA",
            "phonology.notable_rules is empty or not a list — allophony "
            "consistency could not evaluate")
    else:
        phonemes = set(cons_raw) | set(vow_raw)
        for index, raw_rule in enumerate(rules_raw, 1):
            if not isinstance(raw_rule, str):
                add("REVIEW", "A-PARSE",
                    "notable_rules[%d] is not a string — expand the rule into "
                    "'src → dst / environment' (spec §2)" % index)
                continue
            rule = parse_rule(raw_rule)
            if rule is None:
                add("REVIEW", "A-PARSE",
                    "notable_rules[%d] '%s' is not recognizable as "
                    "'src → dst / environment': expand it or record the "
                    "analysis — missing expansion is REVIEW, not permission to "
                    "ignore the rule (spec §2)" % (index, raw_rule.strip()))
                continue
            rule["index"] = index
            rules.append(rule)
            witness = "notable_rules[%d] '%s'" % (index, raw_rule.strip())
            src_class = is_class_token(rule["src"])
            dst_class = is_class_token(rule["dst"])
            env_classes = [t for t in rule["left"] + rule["right"]
                           if is_class_token(t)]
            if src_class or dst_class or env_classes:
                detail = src_class and "source" or dst_class and "output" or "environment"
                add("REVIEW", "A-CLASS",
                    "%s conditions on a natural class (%s): expand the class "
                    "into finite contextual rules for this scoped stratum and "
                    "list the expansion — missing expansion is REVIEW (spec §2)"
                    % (witness, detail))
            if not src_class:
                if rule["src"] not in phonemes:
                    add("FAIL", "I-UNKNOWN",
                        "%s rewrites '%s', which is not a phoneme of this "
                        "inventory — every underlying token must be a phoneme "
                        "of the scoped stratum (spec §5)"
                        % (witness, rule["src"]))
            if not dst_class and rule["dst"] not in DELETION_TOKENS:
                dst_feat = classify(rule["dst"])
                if dst_feat["kind"] in ("unknown", "orthography"):
                    add("REVIEW", "I-SYM",
                        "%s outputs '%s', which is not recognized as an IPA "
                        "segment — declare the surface token (corpus §9.2)"
                        % (witness, rule["dst"]))
                elif (rule["dst"] in phonemes and not src_class
                      and rule["dst"] != rule["src"]):
                    add("REVIEW", "A-NEUTRAL",
                        "%s neutralizes '%s' to the phoneme '%s': permitted, "
                        "but the phonemic distinction in that same context "
                        "still needs a contrast witness or a reanalysis (spec §5)"
                        % (witness, rule["src"], rule["dst"]))
            for token in rule["left"] + rule["right"]:
                if is_class_token(token) or token in ("#", "$", "∅", "⌀", "-"):
                    continue
                if token not in phonemes:
                    add("FAIL", "I-UNKNOWN",
                        "%s conditions on '%s', which is not a phoneme of this "
                        "inventory (spec §5)" % (witness, token))

        # A-ORDER: same source, same environment, different outputs
        seen = {}
        for rule in rules:
            key = (rule["src"], rule["env"])
            seen.setdefault(key, []).append(rule)
        for (src, env), group in sorted(seen.items()):
            outputs = sorted({r["dst"] for r in group})
            if len(outputs) > 1:
                add("REVIEW", "A-ORDER",
                    "rules %s all rewrite /%s/ in the same environment '%s' "
                    "with different outputs (%s): undeclared choice between "
                    "distinct outputs (spec §5)"
                    % (", ".join("notable_rules[%d]" % r["index"] for r in group),
                       src, env or "unconditioned", ", ".join(outputs)))

        # A-VACUOUS: the template makes the adjacent environment impossible
        if template and template["nucleus"] >= 1:
            adjacency_ok = template["onset"] >= 2 or template["coda"] >= 1
            for rule in rules:
                if rule["src"] in DELETION_TOKENS:
                    continue
                neighbours = [t for t in (rule["left"][-1:] + rule["right"][:1])
                              if t and not is_class_token(t)
                              and t not in ("#", "$", "∅", "⌀", "-")]
                cons_neighbours = [t for t in neighbours
                                   if classify(t).get("kind") == "consonant"]
                if cons_neighbours and not adjacency_ok:
                    add("REVIEW", "A-VACUOUS",
                        "notable_rules[%d] '%s' needs adjacent consonants, but "
                        "template '%s' licenses no consonant adjacency (no CC "
                        "onset, no coda): no triggering site exists — re-condition "
                        "the rule or license the cluster (spec §5 rule coverage)"
                        % (rule["index"], rule["raw"].strip(), template_raw))

        # A-TONE: tone manipulation while the packet says tones: 0
        if tones == 0 and isinstance(rules_raw, list):
            for index, raw_rule in enumerate(rules_raw, 1):
                if not isinstance(raw_rule, str):
                    continue
                if (TONE_WORDS.search(raw_rule)
                        or any(ch in TONE_MARKS for ch in raw_rule)):
                    add("FAIL", "A-TONE",
                        "notable_rules[%d] '%s' manipulates tone while the "
                        "packet declares tones: 0 — the profile contradicts its "
                        "declared tone structure (corpus §6)"
                        % (index, raw_rule.strip()))

    # ---- culture-packet coupling: names ----------------------------------
    names_raw = packet.get("names")
    if isinstance(names_raw, list):
        for item in names_raw:
            name = None
            if isinstance(item, str):
                name = item
            elif isinstance(item, dict):
                candidate = item.get("name")
                if isinstance(candidate, str):
                    name = candidate
            if name and any(ch in NAME_APOSTROPHES for ch in name):
                add("REVIEW", "X-NAME",
                    "name '%s' carries an apostrophe: decorative punctuation "
                    "does not supply a phonemic contrast — test the name "
                    "without it through the same scoped system (spec §7)" % name)

    return (1 if findings else 0), findings


def emit(findings):
    order = {"FAIL": 0, "REVIEW": 1, "UNEVALUABLE": 2}
    seen, out = set(), []
    for level, fid, msg in findings:
        key = (level, fid, msg)
        if key in seen:
            continue
        seen.add(key)
        out.append((level, fid, msg))
    out.sort(key=lambda f: (order.get(f[0], 9), f[1], f[2]))
    return out


def run_text(text):
    try:
        packet = parse_packet(text)
    except PacketError as error:
        return 2, [("UNEVALUABLE", "G-DATA",
                    "packet could not be parsed: %s" % error)]
    except RecursionError:
        return 2, [("UNEVALUABLE", "G-DATA",
                    "packet could not be evaluated: flow nesting exceeds the supported depth")]
    return evaluate(packet)


# --------------------------------------------------------------------------
# selftest
# --------------------------------------------------------------------------

FIXTURE_TEXT = """\
# synthetic fixture for tools/gates/phonology-sanity-gate.py --selftest
# not canon, not a fictional-world fact, not a language design: every defect
# below is planted on purpose to exercise the finding IDs.
name: gate-selftest-phonology
phonology:
  consonants: [p, t, v, ɲ, qʼ, t]        # t listed twice -> I-DUPLICATE
  vowels: [a, i, e, y]                   # /y/ with no back rounded peer -> M-ROUND
  phonotactics: (C)(C)V(C)(C)            # complex: CC onset, CC coda -> T-SYL, M-SONORITY
  tones: 0                               # contradicted by the tone rule below -> A-TONE
  notable_rules:
    - "t → ts / _i"
    - "t → d / _i"                       # same src+environment, two outputs -> A-ORDER
    - "q → k / _u"                       # q and u are not in the inventory -> I-UNKNOWN
    - "v → s / V_V"                      # natural class, not finite context -> A-CLASS
    - "p → t / _#"                       # neutralizes into the phoneme /t/ -> A-NEUTRAL
    - "tones rise on the final syllable" # no arrow -> A-PARSE, and tones: 0 -> A-TONE
names:
  - {name: "Aren'tal", type: place, era: "First Era"}   # apostrophe -> X-NAME
eras: [First Era]
"""

PLANTED = [
    "A-CLASS", "A-NEUTRAL", "A-ORDER", "A-PARSE", "A-TONE",
    "I-DUPLICATE", "I-UNKNOWN",
    "M-EJECT", "M-NASAL", "M-ROUND", "M-SONORITY", "M-VOICE",
    "T-C", "T-SYL",
    "X-NAME",
]

CLEAN_PACKET = """\
name: gate-selftest-clean
phonology:
  consonants: [p, t, k, m, n, s, l]
  vowels: [a, e, i, o, u]
  phonotactics: (C)V(C)
  tones: 0
  notable_rules:
    - "t → ts / _i"
    - "n → ŋ / _k"
names:
  - {name: "Senna", type: place, era: "First Era"}
eras: [First Era]
"""


def _packet(**overrides):
    base = {
        "name": "gate-control",
        "phonology": {
            "consonants": ["p", "t", "k", "m", "n", "s", "l"],
            "vowels": ["a", "e", "i", "o", "u"],
            "phonotactics": "(C)V(C)",
            "tones": 0,
            "notable_rules": ["t → ts / _i"],
        },
        "names": [{"name": "Senna", "type": "place"}],
    }
    for key, value in overrides.items():
        if key == "phonology" and isinstance(value, dict):
            base["phonology"].update(value)
        else:
            base[key] = value
    return base


CONTROL_CASES = [
    ("clean packet is silent", CLEAN_PACKET, 0, []),
    ("packet root is a list", [1, 2, 3], 2, ["G-DATA"]),
    ("no phonology block", {"name": "x"}, 2, ["G-DATA"]),
    ("phonology without consonants/vowels", {"phonology": {"tones": 0}}, 2, ["G-DATA"]),
    ("vowels missing", _packet(phonology={"vowels": None}), 1, ["G-DATA"]),
    ("phonotactics unparseable", _packet(phonology={"phonotactics": "CV+V"}), 1,
     ["P-PATTERN"]),
    ("template without a vowel core", _packet(phonology={"phonotactics": "CCC"}), 1,
     ["P-NUCLEUS"]),
    ("one vowel quality", _packet(phonology={"vowels": ["a"]}), 1, ["T-V"]),
    ("large tone inventory", _packet(phonology={"tones": 7}), 1, ["T-TONE"]),
    ("coda without any sonorant",
     _packet(phonology={"consonants": ["p", "t", "k", "s", "x", "f"]}), 1,
     ["P-CODA"]),
    ("no nasals or fricatives",
     _packet(phonology={"consonants": ["p", "t", "k"], "vowels": ["a", "i", "u"],
                        "phonotactics": "(C)V"}), 1, ["M-CLASS"]),
    ("look-alike codepoints",
     _packet(phonology={"consonants": ["p", "t", "k", "g", "ɡ", "m", "n", "s"]}),
     1, ["I-CANON"]),
    ("orthography digraph",
     _packet(phonology={"consonants": ["p", "t", "k", "s", "sh", "m", "n", "l"]}),
     1, ["I-SYM"]),
    ("syllabic consonant token",
     _packet(phonology={"consonants": ["p", "t", "k", "n̩", "s", "l", "m"]}), 1,
     ["I-SYLLABIC"]),
    ("consonant listed as a vowel",
     _packet(phonology={"consonants": ["p", "t", "k", "m", "n", "s", "l"],
                        "vowels": ["a", "e", "i", "o", "s"]}), 1, ["I-ROLE"]),
    ("NFC alias pair",
     _packet(phonology={"vowels": ["a", "e\u0301", "é", "i", "o", "u"]}), 1,
     ["I-ALIAS"]),
    ("neutralizing rule",
     _packet(phonology={"notable_rules": ["p → t / _i"]}), 1, ["A-NEUTRAL"]),
    ("impossible adjacency for a rule",
     _packet(phonology={"consonants": ["p", "t", "k", "m", "n", "s", "l"],
                        "phonotactics": "V",
                        "notable_rules": ["t → d / _k"]}), 1, ["A-VACUOUS"]),
    ("asymmetric ejective",
     _packet(phonology={"consonants": ["p", "t", "k", "qʼ", "m", "n", "s"]}), 1,
     ["M-EJECT"]),
    ("voiced fricatives only",
     _packet(phonology={"consonants": ["p", "t", "k", "v", "z", "m", "n"]}), 1,
     ["M-VOICE"]),
    ("nasal without an oral peer at its place",
     _packet(phonology={"consonants": ["p", "t", "k", "ɲ", "s", "l", "m"],
                        "vowels": ["a", "e", "i", "o", "u"]}), 1, ["M-NASAL"]),
    ("apostrophe in a name",
     _packet(names=[{"name": "Oru'ka", "type": "place"}]), 1, ["X-NAME"]),
    ("precomposed nasal vowels stay IPA segments",
     _packet(phonology={"vowels": ["a", "e", "i", "ĩ", "o", "u"]}), 0, []),
    ("umlaut spelling is orthography, not IPA",
     _packet(phonology={"vowels": ["a", "i", "ü", "o", "u"]}), 1, ["I-SYM"]),
    ("boolean tone count",
     _packet(phonology={"tones": True}), 1, ["G-DATA"]),
    ("duplicate block mapping key",
     "name: t\nphonology:\n  consonants: [p, t, k, m, n, s, l]\n"
     "  vowels: [a, e, i, o, u]\n  phonotactics: (C)V(C)\n  tones: 0\n"
     "phonology:\n  consonants: [p, t, k, m, n, s, l, qʼ]\n"
     "  vowels: [a, e, i, o, u]\n  phonotactics: (C)V(C)\n  tones: 0\n",
     2, ["G-DATA"]),
    ("duplicate flow mapping key",
     "name: t\nphonology: {consonants: [p], consonants: [k]}\n", 2, ["G-DATA"]),
    ("duplicate key in a sequence mapping entry",
     "name: t\nphonology:\n  consonants: [p, t, k, m, n, s, l]\n"
     "  vowels: [a, e, i, o, u]\n  phonotactics: (C)V(C)\n  tones: 0\n"
     "names:\n  - name: A\n    name: B\n", 2, ["G-DATA"]),
]


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
    os.makedirs(os.path.dirname(FIXTURE_PATH), exist_ok=True)
    if not _pin_fixture_or_fail(FIXTURE_PATH, FIXTURE_TEXT):
        return 1
    if not _pin_fixture_or_fail(EXPECTED_PATH, "\n".join(sorted(PLANTED)) + "\n"):
        return 1

    import subprocess
    proc = subprocess.run(
        [sys.executable, os.path.abspath(__file__), FIXTURE_PATH],
        capture_output=True, text=True)
    assert proc.returncode == 1, (
        "fixture exit %r, expected 1; stdout:\n%s\nstderr:\n%s"
        % (proc.returncode, proc.stdout, proc.stderr))
    got = set(re.findall(r"(?m)^FINDING (\S+):", proc.stdout))
    missing = [fid for fid in PLANTED if fid not in got]
    assert not missing, "planted IDs missing from fixture output: %s\n%s" % (
        missing, proc.stdout)

    checks = 0
    for name, payload, want_code, want_ids in CONTROL_CASES:
        text = payload if isinstance(payload, str) else None
        if text is not None:
            code, findings = run_text(text)
        else:
            code, findings = evaluate(payload)
        assert code == want_code, "%s: exit %r, expected %r (%s)" % (
            name, code, want_code, findings)
        ids = {fid for _, fid, _ in findings}
        for fid in want_ids:
            assert fid in ids, "%s: finding %s missing (%s)" % (name, fid, findings)
        if want_code == 0:
            assert not findings, "%s: expected silence, got %s" % (name, findings)
        checks += 1

    assert run_text("name: x\n    stray: y\n")[0] == 2, "indent error must exit 2"
    checks += 1
    print("selftest: fixture exit 1; %d/%d planted finding IDs present; "
          "%d control cases passed" % (len(PLANTED), len(PLANTED), checks))
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv):
    args = argv[1:]
    if args in (["--selftest"], ["--self-test"]):
        return selftest()
    if len(args) != 1:
        sys.stderr.write(
            "usage: phonology-sanity-gate.py <culture-packet.yml>|-\n"
            "       phonology-sanity-gate.py --selftest\n")
        return 2
    path = args[0]
    try:
        if path == "-":
            text = sys.stdin.read()
        else:
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
    except UnicodeDecodeError as error:
        print("FINDING G-DATA: UNEVALUABLE — packet is not UTF-8 text: %s"
              % error)
        return 2
    except OSError as error:
        print("FINDING G-DATA: UNEVALUABLE — packet could not be read: %s"
              % error)
        return 2
    code, findings = run_text(text)
    for level, fid, msg in emit(findings):
        print("FINDING %s: %s — %s" % (fid, level, msg))
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))