#!/usr/bin/env python3
"""Evidence-coupling guard for the bounded NON-CANON D3 culture packet
(kotodama round 7, contract reports/round-7/d3-contract.json,
profile kotodama-d3-evidence-coupling/1).

Stdlib only. No network, no eval/exec, no shell interpolation, and no writes
in normal runs: the guard only reads the packet given on argv, the frozen
expectation file when --frozen is given, and the five CLOSED round-6 ledger
paths embedded below (never an input-supplied path). Path handling is closed:
frozen manifest keys must be relative, slash-separated, dot-free and resolve
inside this repository root; reference ledgers are opened only at their
embedded closed paths.

Usage:
  python3 tools/check-evidence-coupling.py <packet.json> [--frozen <expected.json>]
  python3 tools/check-evidence-coupling.py --selftest

Stdout is always one JSON object: {profile, exit, findings:[{id, record_id,
message}], counts}. Exit codes: 0 = valid bounded model, 1 = demonstrated
profile contradiction (findings listed), 2 = could-not-evaluate (malformed
input, usage error, or frozen snapshot rejection). No traceback is ever
printed; unexpected internal failures are reported as D3-DATA on stdout.

Diagnostics (stable ids; value/semantics violations are exit 1 unless noted):
  D3-CANON      canon_status other than NON-CANON, handoff claiming acceptance,
                scope notes missing a required limit statement
  D3-REFERENCE  missing/unknown record or source ids, broken bridge
                target/ref, duplicate ids, unknown era or material references
  D3-DIGEST     reference ledger hash disagrees with actual closed-path bytes
                (exit 1); closed ledger itself unreadable is D3-DATA (exit 2)
  D3-SCOPE      reference kind/URL/support scope/ledger path/audit id differs
                from the effective round-6 parent reconciliation row; unread
                whole-claim promotion (e.g. full-support); screening
                clearance-scope contradictions (status other than unresolved,
                sweep-flag claiming a real-language sweep, missing limits)
  D3-NATIVE     native form violates the declared symbol/syllable profile, or
                the phonology inventory itself is malformed; translated
                display labels are NEVER phonotactically tested
  D3-DERIVATION E1 lexeme SC1 computation or name concat does not yield the
                actual native form / declared expected output
  D3-UTTERANCE  spoken/written form fails the context/register law versus the
                limited AV1 substitution; unexpected generalized taboo rule
  D3-TIMING     chosen offset outside the discrete allowed integer set (bools
                rejected), wrong timing unit
  D3-MYTH       belief promoted to world-fact/certified truth; timing rule
                claiming historical prescription
  D3-OBJECT     ground surface worn, costume bound to non-worn/mismatched
                object, material identity or gate-name anchor mismatch,
                uninterpretable claimed_status
  D3-ERA        material or route unavailable in the costume's declared era,
                provenance disagreement, deviating era model or availability pin
  D3-RANK       unexempted prohibited use falsely claimed lawful; RR1 shape or
                C03 prohibited-case bindings deviating
  D3-BRIDGE     reference-to-invention bridge not the declared design-only
                method/analogy mapping, or wrong bound source
  D3-SYMBOL     symbol audience/era scope absent or universal meaning asserted
  D3-DATA       malformed file/UTF-8/JSON/root or nested essential schema
                (exit 2, no traceback)
  D3-SNAPSHOT   frozen input digest or manifest unreadable/mismatched
                (exit 2, no traceback; --frozen only)

Boundary vs domain: presence/type of contract-required keys is validated at
the boundary (D3-DATA, exit 2) so domain checks never crash; contract-value
violations on present keys are domain findings (exit 1) under the family
diagnostics above.

--frozen <expected.json>: expected.json = {"profile": <profile>,
"manifest": {"<repo-relative/path>": "<sha256>", ...}, "expected_exit": 0|1
(strict integer; booleans rejected),
"finding_ids": [..]}. The guard verifies EVERY manifest digest first
(packet included; the packet path must be covered by the manifest); any
unreadable/mismatched/unsafe entry exits 2 with D3-SNAPSHOT before any
verdict. If digests verify, the normal verdict is computed and compared to
the predeclared expectation; a mismatch is D3-SNAPSHOT exit 2. The parent
creates expected.json after inputs land (predeclared expected_exit=0,
finding_ids=[]); it is not a printed self-blessing checksum.

--selftest drives this script as a real subprocess over the COMMITTED positive
packet examples/culture-d3/packet.json and the INDEPENDENT controls file
examples/culture-d3/controls.json, in an isolated temporary directory
(copies only; live inputs are never edited), including foreign-cwd calls, and
prints JSON {profile, selftest_passed, positive_controls, domain_controls,
malformed_controls, frozen_checks, results, missing_inputs, ...}. Missing or
insufficient committed inputs are reported honestly (exit 2) instead of being
synthesized or weakened.

D3-SCOPE authority: the effective values below are embedded from
reports/round-6/parent-reconciliation.json rows R6-05-A, R6-03-B, R6-13-A,
R6-13-B, R6-09-A (effective_source_kind / effective_source_url overrides) at
baseline revision 30caac66a2a382f1c46ba31f0c3c93da62d0762c. Raw worker labels
are deliberately NOT the expectation (S01's raw label repository-scholarly is
effectively secondary-scholarly; S03's effective URL is the pinned archived
capture)."""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

PROFILE = "kotodama-d3-evidence-coupling/1"
PACKET_NAME = "D3 source-bounded culture drill (NON-CANON)"
EXIT_OK = 0
EXIT_FINDINGS = 1
EXIT_ERROR = 2

REPO_ROOT = os.path.realpath(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

# --- closed source bindings (effective round-6 reconciliation) --------------
SOURCE_BINDINGS = {
    "S01": {
        "ledger_path": "corpus/lessons/round-6-sources/05.json",
        "audit_id": "R6-05-A",
        "source_url": "https://lrc.la.utexas.edu/eieol/hitol/20",
        "source_kind": "secondary-scholarly",
        "support_scope": "partial-support",
    },
    "S02": {
        "ledger_path": "corpus/lessons/round-6-sources/03.json",
        "audit_id": "R6-03-B",
        "source_url": "https://collections.louvre.fr/en/ark:/53355/cl010005890",
        "source_kind": "museum-object",
        "support_scope": "scoped-support",
    },
    "S03": {
        "ledger_path": "corpus/lessons/round-6-sources/13.json",
        "audit_id": "R6-13-A",
        "source_url": "https://web.archive.org/web/20231003011254/https://sacred-texts.com/hin/sbe30/sbe30020.htm",
        "source_kind": "primary-text",
        "support_scope": "scoped-support",
    },
    "S04": {
        "ledger_path": "corpus/lessons/round-6-sources/13.json",
        "audit_id": "R6-13-B",
        "source_url": "https://www.wisdomlib.org/hinduism/book/satapatha-brahmana-english/d/doc63185.html",
        "source_kind": "primary-text",
        "support_scope": "scoped-support",
    },
    "S05": {
        "ledger_path": "corpus/lessons/round-6-sources/09.json",
        "audit_id": "R6-09-A",
        "source_url": "http://www.achemenet.com/document/2007.001-Stolper-Tavernier.pdf",
        "source_kind": "secondary-scholarly",
        "support_scope": "partial-support",
    },
}

# --- interface anchors (d3-contract.json interface_anchors + fixed records) -
LEXICON_IDS = ["L%02d" % i for i in range(1, 21)]
NAME_IDS = ["N%02d" % i for i in range(1, 7)]
UTTERANCE_ANCHORS = {
    "U01": {"lexeme_id": "L01", "register": "ordinary", "place": "market", "era": "E1"},
    "U02": {"lexeme_id": "L01", "register": "ritual", "place": "hall", "era": "E1"},
    "U03": {"lexeme_id": "L03", "register": "ordinary", "era": "E1"},
    "U04": {"lexeme_id": "L03", "register": "ritual", "era": "E1"},
}
COSTUME_LEXEMES = {"C01": "L17", "C02": "L18", "C03": "L19", "C04": "L20"}
COSTUME_CASES = {
    "C01": {"object_id": "O02", "material_id": "M01", "era": "E0"},
    "C02": {"object_id": "O02", "material_id": "M01", "era": "E1"},
    "C03": {
        "object_id": "O03", "material_id": "M02", "era": "E1",
        "wearer_rank": "visitor", "rite": "assembly", "place": "hall",
    },
    "C04": {"object_id": "O04", "material_id": "M03", "era": "E1",
            "rite": "assembly", "place": "hall"},
}
OBJECT_CASES = {
    "O01": {"material_id": "M01", "object_kind": "ground-surface", "worn": False},
    "O02": {"material_id": "M01", "worn": True},
    "O03": {"material_id": "M02", "worn": True},
    "O04": {"material_id": "M03", "worn": True},
}
GATE_NAMES = {"M01": "felt", "M02": "plant-cloth", "M03": "horn"}
MATERIAL_CASES = {
    "M01": {"available_from": "E0", "provenance": "local-production"},
    "M02": {"available_from": "E1", "provenance": "import"},
    "M03": {"available_from": "E0", "provenance": "local-production"},
}
ERA_ORDINAL = {"E0": 0, "E1": 1}
CODA_SET = {"n", "l", "r", "s"}
BRIDGE_CASES = {
    "BR01": {"source_id": "S01", "targets": ["U01", "U02"]},
    "BR02": {"source_id": "S02", "targets": ["C01", "C02"]},
    "BR03": {"source_id": "S03", "targets": ["NR1"]},
    "BR04": {"source_id": "S04", "targets": ["O01", "O04"]},
    "BR05": {"source_id": "S05", "targets": ["SY01", "B01"]},
}
COMPONENT_PATHS = [
    "examples/culture-d3/components/04-language.json",
    "examples/culture-d3/components/05-ritual.json",
    "examples/culture-d3/components/06-material.json",
    "examples/culture-d3/components/07-evidence.json",
]
LAWFUL_TOKENS = ("lawful", "permitted", "allowed", "compliant")
VIOLATION_TOKENS = ("viol", "prohibit", "forbid", "unlawful", "illegal", "noncompliant")
UNIVERSAL_PHRASES = (
    "always means",
    "means the same to all",
    "in every culture",
    "to everyone",
    "for all peoples",
    "universally signifies",
    "universal colour code",
    "universal color code",
)
SCOPE_NOTE_TOPICS = (
    ("invented genealogy", ("genealog",)),
    ("cultural-permission limit", ("permission",)),
    ("no lore receipt", ("lore",)),
    ("unresolved residuals", ("residual", "unresolved")),
)
PROVENANCE_TO_ROUTE = {"local-production": "local", "import": "import"}


# --- output helpers ----------------------------------------------------------
def finding(fid, record_id, message):
    return {"id": fid, "record_id": record_id, "message": message}


class Findings(object):
    def __init__(self):
        self.items = []

    def add(self, fid, record_id, message):
        self.items.append(finding(fid, record_id, message))

    def __len__(self):
        return len(self.items)


def emit(findings, code):
    counts = {"total": len(findings)}
    for f in findings:
        counts[f["id"]] = counts.get(f["id"], 0) + 1
    sys.stdout.write(
        json.dumps(
            {"profile": PROFILE, "exit": code, "findings": findings, "counts": counts},
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    sys.stdout.flush()
    return code


# --- input reading -----------------------------------------------------------
def read_file_bytes(path):
    with open(path, "rb") as fh:
        return fh.read()


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def load_json_document(path, data_id, read_msg_prefix):
    """Read + decode + parse a JSON file. Returns (doc, error_finding)."""
    try:
        raw = read_file_bytes(path)
    except OSError as exc:
        return None, finding(
            data_id, "-", "%s cannot be read: %s" % (read_msg_prefix, exc.strerror or exc)
        )
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        return None, finding(
            data_id, "-", "%s is not valid UTF-8: %s" % (read_msg_prefix, exc)
        )
    try:
        doc = json.loads(text)
    except (ValueError, RecursionError) as exc:
        return None, finding(
            data_id, "-", "%s is not valid JSON: %s" % (read_msg_prefix, exc)
        )
    if not isinstance(doc, dict):
        return None, finding(
            data_id,
            "-",
            "%s root must be a JSON object, got %s" % (read_msg_prefix, type(doc).__name__),
        )
    return doc, None


# --- boundary schema validation (D3-DATA) ------------------------------------
def _is_str(v):
    return isinstance(v, str)


def _is_bool(v):
    return isinstance(v, bool)


def _is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)


def _is_strlist(v):
    return isinstance(v, list) and all(isinstance(x, str) for x in v)


def _is_intlist(v):
    return isinstance(v, list) and all(_is_int(x) for x in v)


def check_object_shape(errors, where, obj, schema, optional=()):
    if not isinstance(obj, dict):
        errors.append("%s must be a JSON object, got %s" % (where, type(obj).__name__))
        return False
    ok = True
    for key, kind in sorted(schema.items()):
        if key not in obj:
            errors.append("%s missing required key %r" % (where, key))
            ok = False
            continue
        val = obj[key]
        good = {
            "str": _is_str,
            "bool": _is_bool,
            "int": _is_int,
            "strlist": _is_strlist,
            "intlist": _is_intlist,
            "list": lambda v: isinstance(v, list),
            "any": lambda v: True,
            "dict": lambda v: isinstance(v, dict),
        }[kind](val)
        if not good:
            errors.append("%s.%s must be %s, got %r" % (where, key, kind, val))
            ok = False
    for key in optional:
        if key in obj and not _is_str(obj[key]):
            errors.append("%s.%s must be a string when present" % (where, key))
            ok = False
    return ok


def validate_shape(doc):
    """Presence/type boundary checks. Returns a list of D3-DATA messages."""
    errors = []

    def top(key, kind):
        if key not in doc:
            errors.append("packet missing required key %r" % key)
            return None
        val = doc[key]
        good = {
            "str": _is_str,
            "bool": _is_bool,
            "int": _is_int,
            "strlist": _is_strlist,
            "intlist": _is_intlist,
            "list": lambda v: isinstance(v, list),
            "any": lambda v: True,
            "dict": lambda v: isinstance(v, dict),
        }[kind](val)
        if not good:
            errors.append("packet.%s must be %s, got %r" % (key, kind, val))
            return None
        return val

    top("profile", "str")
    top("name", "str")
    if doc.get("profile") != PROFILE:
        errors.append("packet.profile must be %r, got %r" % (PROFILE, doc.get("profile")))
    if doc.get("name") != PACKET_NAME:
        errors.append("packet.name must be %r, got %r" % (PACKET_NAME, doc.get("name")))
    top("canon_status", "str")
    top("handoff_status", "str")
    top("scope_notes", "strlist")
    assembly = top("assembly", "dict")
    if isinstance(assembly, dict):
        if check_object_shape(
            errors, "packet.assembly", assembly, {"generator": "str"}, optional=()
        ):
            source_sha = assembly.get("source_sha256")
            if not (
                _is_str(source_sha)
                or (
                    isinstance(source_sha, dict)
                    and all(
                        isinstance(k, str) and _is_str(v)
                        for k, v in source_sha.items()
                    )
                )
            ):
                errors.append(
                    "packet.assembly.source_sha256 must be a string or a mapping of "
                    "path -> digest strings (the D3 manifest), got %r" % (source_sha,)
                )
    screening = top("screening", "dict")
    if isinstance(screening, dict):
        check_object_shape(
            errors,
            "packet.screening",
            screening,
            {"status": "str", "real_language_sweep_performed": "bool", "limits": "str"},
        )
    naming_rule = top("naming_rule", "dict")
    if isinstance(naming_rule, dict):
        check_object_shape(
            errors,
            "packet.naming_rule",
            naming_rule,
            {
                "id": "str",
                "allowed_offsets": "list",
                "unit": "str",
                "chosen_offset": "any",
                "status": "str",
                "source_id": "str",
            },
        )

    list_schemas = {
        "lexicon": (
            {"id": "str", "native_form": "str", "gloss": "str", "status": "str",
             "available_from": "str"},
            [],
        ),
        "names": (
            {"id": "str", "native_form": "str", "display_label": "str", "type": "str",
             "era": "str"},
            [],
        ),
        "sound_changes": ({"id": "str"}, []),
        "utterances": (
            {"id": "str", "lexeme_id": "str", "era": "str", "register": "str",
             "place": "str", "spoken_form": "str", "written_form": "str"},
            [],
        ),
        "beliefs": (
            {"id": "str", "speaker": "str", "era": "str", "claim_kind": "str",
             "truth_status": "str", "proposition": "str"},
            [],
        ),
        "speech_rules": (
            {"id": "str", "lexeme_id": "str", "era": "str", "register": "str",
             "place": "str", "substitute_lexeme_id": "str", "claim_kind": "str"},
            [],
        ),
        "symbols": (
            {"id": "str", "display_label": "str", "era": "str", "audience": "str",
             "reading": "str", "claim_kind": "str"},
            [],
        ),
        "eras": ({"id": "str", "ordinal": "int", "display_label": "str"}, []),
        "materials": (
            {"id": "str", "gate_name": "str", "composition": "str",
             "available_from": "str", "provenance": "str"},
            [],
        ),
        "objects": (
            {"id": "str", "material_id": "str", "object_kind": "str",
             "display_label": "str", "worn": "bool"},
            [],
        ),
        "costumes": (
            {"id": "str", "object_id": "str", "native_form": "str",
             "display_label": "str", "material_id": "str", "era": "str",
             "wearer_rank": "str", "rite": "str", "place": "str",
             "claimed_status": "str", "provenance": "str"},
            ["lexeme_id"],
        ),
        "rank_rules": (
            {"id": "str", "authority": "str", "jurisdiction": "str", "effect": "str",
             "property": "dict"},
            [],
        ),
        "references": (
            {"id": "str", "ledger_path": "str", "audit_id": "str", "file_sha256": "str",
             "source_url": "str", "source_kind": "str", "support_scope": "str",
             "limits": "str"},
            [],
        ),
        "bridges": (
            {"id": "str", "source_id": "str", "relation": "str",
             "asserted_scope": "str", "claim_kind": "str", "mechanism": "str",
             "limits": "str", "target_ids": "strlist"},
            [],
        ),
    }
    for key in ("lexicon", "names", "sound_changes", "utterances", "beliefs",
                "speech_rules", "symbols", "eras", "materials", "objects",
                "costumes", "rank_rules", "references", "bridges", "phonology"):
        if key not in doc:
            errors.append("packet missing required key %r" % key)
        elif key != "phonology" and not isinstance(doc[key], list):
            errors.append(
                "packet.%s must be a JSON array, got %s"
                % (key, type(doc[key]).__name__)
            )
    for key, (schema, optional) in list_schemas.items():
        records = doc.get(key)
        if not isinstance(records, list):
            continue
        for i, rec in enumerate(records):
            check_object_shape(errors, "packet.%s[%d]" % (key, i), rec, schema, optional)
        if key == "materials":
            for i, rec in enumerate(records):
                if isinstance(rec, dict):
                    routes = rec.get("routes")
                    if not isinstance(routes, list):
                        errors.append("packet.materials[%d].routes must be a JSON array" % i)
                        continue
                    for j, route in enumerate(routes):
                        check_object_shape(
                            errors,
                            "packet.materials[%d].routes[%d]" % (i, j),
                            route,
                            {"kind": "str", "stage": "str", "eras": "strlist"},
                        )
        if key == "rank_rules":
            for i, rec in enumerate(records):
                if isinstance(rec, dict):
                    prop = rec.get("property")
                    if isinstance(prop, dict):
                        check_object_shape(
                            errors,
                            "packet.rank_rules[%d].property" % i,
                            prop,
                            {"kind": "str", "value": "str"},
                        )
                    for lk in ("eras", "rites", "wearer_ranks", "exempt_ranks"):
                        if not _is_strlist(rec.get(lk)):
                            errors.append(
                                "packet.rank_rules[%d].%s must be an array of strings" % (i, lk)
                            )
        if key == "names":
            for i, rec in enumerate(records):
                if isinstance(rec, dict):
                    formation = rec.get("formation")
                    if not isinstance(formation, dict):
                        errors.append("packet.names[%d].formation must be a JSON object" % i)
                        continue
                    check_object_shape(
                        errors,
                        "packet.names[%d].formation" % i,
                        formation,
                        {"operation": "str", "expected": "str", "bases": "strlist"},
                    )
    phon = doc.get("phonology")
    if not isinstance(phon, dict):
        errors.append("packet.phonology must be a JSON object")
    else:
        check_object_shape(
            errors,
            "packet.phonology",
            phon,
            {"consonants": "strlist", "vowels": "strlist", "phonotactics": "str",
             "coda_subset": "strlist", "onset_clusters": "bool"},
        )
        if isinstance(doc.get("lexicon"), list):
            for i, rec in enumerate(doc["lexicon"]):
                if isinstance(rec, dict):
                    forms = rec.get("forms")
                    if not isinstance(forms, dict):
                        errors.append("packet.lexicon[%d].forms must be a JSON object" % i)
                    else:
                        for ek, ev in sorted(forms.items()):
                            if not _is_str(ev):
                                errors.append(
                                    "packet.lexicon[%d].forms.%s must be a string" % (i, ek)
                                )
    return errors


# --- phonology / derivation engine ------------------------------------------
def syllabify(word, cons, vows, codas):
    """Validate a native spelling against (C)V(C) with the declared coda subset.
    Returns None when the form syllabifies, else a short reason. A consonant
    directly after a vowel is an onset when the next letter is a vowel, a coda
    when it ends the word or precedes another consonant."""
    if not word:
        return "empty native form"
    i, n = 0, len(word)
    while i < n:
        if word[i] in cons:
            i += 1
            if i < n and word[i] in cons:
                return "onset cluster %r not allowed (onset_clusters=false)" % word[i - 1:i + 1]
        if i >= n or word[i] not in vows:
            return "no syllable vowel at position %d" % i
        i += 1
        if i < n and word[i] in cons:
            if i + 1 < n and word[i + 1] in vows:
                pass  # onset of the next syllable (e.g. su-ma)
            elif word[i] in codas:
                i += 1  # syllable coda (e.g. min-ta, holam)
            else:
                return (
                    "consonant %r after a vowel is neither a declared coda nor a "
                    "following onset" % word[i]
                )
    return None


def apply_sc1(e0_form):
    """SC1: initial p -> f, once, word-initially only (ordinary E1 speech)."""
    if e0_form.startswith("p"):
        return "f" + e0_form[1:]
    return e0_form


def interpret_claimed_status(value):
    low = value.strip().lower()
    if low in LAWFUL_TOKENS:
        return "lawful"
    if any(tok in low for tok in VIOLATION_TOKENS):
        return "violation"
    return None


# --- domain checks -----------------------------------------------------------
EXACT_ID_SETS = {
    "lexicon": LEXICON_IDS,
    "names": NAME_IDS,
    "beliefs": ["B01", "B02"],
    "speech_rules": ["AV1"],
    "symbols": ["SY01", "SY02"],
    "eras": ["E0", "E1"],
    "materials": ["M01", "M02", "M03"],
    "objects": ["O01", "O02", "O03", "O04"],
    "costumes": ["C01", "C02", "C03", "C04"],
    "rank_rules": ["RR1"],
    "sound_changes": ["SC1"],
    "references": ["S01", "S02", "S03", "S04", "S05"],
    "bridges": ["BR01", "BR02", "BR03", "BR04", "BR05"],
}


def build_indexes(doc, f):
    """Id-set/duplicate checks (D3-REFERENCE) and per-family id->record maps."""
    idx = {}
    known = set()
    for family, required in EXACT_ID_SETS.items():
        records = doc.get(family)
        records = records if isinstance(records, list) else []
        seen = {}
        for rec in records:
            rid = rec.get("id")
            if isinstance(rid, str):
                if rid in seen:
                    f.add("D3-REFERENCE", rid,
                          "duplicate id %r in %s (also at %s)" % (rid, family, seen[rid]))
                seen[rid] = family
        want = set(required)
        got = set(seen)
        for missing in sorted(want - got):
            f.add("D3-REFERENCE", missing, "missing required %s record %r" % (family, missing))
        for extra in sorted(got - want):
            f.add("D3-REFERENCE", extra, "unknown %s record id %r" % (family, extra))
        idx[family] = {r.get("id"): r for r in records if isinstance(r.get("id"), str)}
    utterances = doc.get("utterances")
    utterances = utterances if isinstance(utterances, list) else []
    useen = {}
    for rec in utterances:
        rid = rec.get("id")
        if isinstance(rid, str):
            if rid in useen:
                f.add("D3-REFERENCE", rid, "duplicate utterance id %r" % rid)
            useen[rid] = rec
    for uid in sorted(set(UTTERANCE_ANCHORS) - set(useen)):
        f.add("D3-REFERENCE", uid, "missing required utterance record %r" % uid)
    idx["utterances"] = useen
    for family in ("lexicon", "names", "utterances", "beliefs", "speech_rules",
                   "symbols", "eras", "materials", "objects", "costumes", "rank_rules"):
        known.update(idx.get(family, {}).keys())
    nr = doc.get("naming_rule")
    if isinstance(nr, dict) and isinstance(nr.get("id"), str):
        known.add(nr["id"])
    idx["known_ids"] = known
    return idx


def check_cross_references(doc, idx, f):
    lex = idx["lexicon"]

    def need(record_id, target, kind):
        if target not in lex:
            f.add("D3-REFERENCE", record_id,
                  "%s references unknown lexeme id %r" % (kind, target))

    for nid, rec in sorted(idx["names"].items()):
        formation = rec.get("formation")
        bases = formation.get("bases") if isinstance(formation, dict) else None
        if isinstance(bases, list):
            if len(bases) != 2:
                f.add("D3-REFERENCE", nid,
                      "formation.bases must hold exactly two lexeme ids, got %r" % (bases,))
            for b in bases:
                need(nid, b, "name formation base")
    for uid, rec in sorted(idx["utterances"].items()):
        need(uid, rec.get("lexeme_id"), "utterance")
    for rid, rec in sorted(idx["speech_rules"].items()):
        need(rid, rec.get("lexeme_id"), "speech rule target")
        need(rid, rec.get("substitute_lexeme_id"), "speech rule substitute")
    nr = doc.get("naming_rule")
    if isinstance(nr, dict):
        sid = nr.get("source_id")
        if sid not in idx["references"]:
            f.add("D3-REFERENCE", nr.get("id", "NR1"),
                  "naming_rule.source_id %r is not a declared reference id" % (sid,))
    for oid, rec in sorted(idx["objects"].items()):
        mid = rec.get("material_id")
        if mid not in idx["materials"]:
            f.add("D3-REFERENCE", oid, "object references unknown material id %r" % (mid,))
    for cid, rec in sorted(idx["costumes"].items()):
        if rec.get("object_id") not in idx["objects"]:
            f.add("D3-REFERENCE", cid,
                  "costume references unknown object id %r" % (rec.get("object_id"),))
        if rec.get("material_id") not in idx["materials"]:
            f.add("D3-REFERENCE", cid,
                  "costume references unknown material id %r" % (rec.get("material_id"),))
        lid = rec.get("lexeme_id")
        if lid is not None:
            need(cid, lid, "costume lexeme binding")
    for rid, rec in sorted(idx["rank_rules"].items()):
        prop = rec.get("property")
        value = prop.get("value") if isinstance(prop, dict) else None
        if value not in {m.get("gate_name") for m in idx["materials"].values()}:
            f.add("D3-REFERENCE", rid,
                  "rank rule property.value %r matches no declared material gate_name" % (value,))
    for bid, rec in sorted(idx["bridges"].items()):
        sid = rec.get("source_id")
        if sid not in idx["references"]:
            f.add("D3-REFERENCE", bid, "bridge references unknown source id %r" % (sid,))
        for t in rec.get("target_ids", []):
            if t not in idx["known_ids"]:
                f.add("D3-REFERENCE", bid,
                      "bridge target %r is not an existing D3 record id" % (t,))


def check_canon(doc, f):
    if doc.get("canon_status") != "NON-CANON":
        f.add("D3-CANON", "-",
              "canon_status must be NON-CANON, got %r" % (doc.get("canon_status"),))
    if doc.get("handoff_status") != "prepared-not-accepted":
        f.add("D3-CANON", "-",
              "handoff_status must be prepared-not-accepted, got %r (acceptance claims are forbidden)"
              % (doc.get("handoff_status"),))
    notes = doc.get("scope_notes")
    notes = notes if isinstance(notes, list) else []
    joined = " \n ".join(x for x in notes if isinstance(x, str)).lower()
    for topic, needles in SCOPE_NOTE_TOPICS:
        if not any(needle in joined for needle in needles):
            f.add("D3-CANON", "-",
                  "scope_notes do not state the %s" % topic)


def check_screening(doc, f):
    screening = doc.get("screening")
    if not isinstance(screening, dict):
        return
    if screening.get("status") != "unresolved":
        f.add("D3-SCOPE", "screening",
              "screening.status must be unresolved, got %r (clearance scope contradicts "
              "the declared unperformed sweep; no fake real-language clearance)"
              % (screening.get("status"),))
    if screening.get("real_language_sweep_performed") is not False:
        f.add("D3-SCOPE", "screening",
              "real_language_sweep_performed must be exactly false in this bounded drill "
              "(a claimed sweep is a clearance-scope contradiction)")
    if not screening.get("limits", "").strip():
        f.add("D3-SCOPE", "screening",
              "screening.limits must state the clearance-scope limit explicitly")


def check_phonology(doc, f):
    phon = doc.get("phonology")
    if not isinstance(phon, dict):
        return
    cons_list = phon.get("consonants")
    vow_list = phon.get("vowels")
    cons_list = cons_list if isinstance(cons_list, list) else []
    vow_list = vow_list if isinstance(vow_list, list) else []
    cons, vows = set(cons_list), set(vow_list)
    for name, inventory in (("consonants", cons_list), ("vowels", vow_list)):
        for sym in inventory:
            if not (isinstance(sym, str) and len(sym) == 1 and "a" <= sym <= "z"):
                f.add("D3-NATIVE", "phonology",
                      "%s symbol %r is not a single ASCII lowercase letter" % (name, sym))
    if not cons or not vows:
        f.add("D3-NATIVE", "phonology", "consonants and vowels must be nonempty")
    if cons & vows:
        f.add("D3-NATIVE", "phonology",
              "consonant and vowel inventories overlap: %r" % sorted(cons & vows))
    if phon.get("phonotactics") != "(C)V(C)":
        f.add("D3-NATIVE", "phonology",
              "phonotactics must be '(C)V(C)', got %r" % (phon.get("phonotactics"),))
    coda = phon.get("coda_subset")
    coda = set(coda) if isinstance(coda, list) else set()
    if coda != CODA_SET:
        f.add("D3-NATIVE", "phonology",
              "coda_subset must be exactly ['n','l','r','s'], got %r" % sorted(coda))
    if coda - cons:
        f.add("D3-NATIVE", "phonology",
              "coda symbols not declared as consonants: %r" % sorted(coda - cons))
    if phon.get("onset_clusters") is not False:
        f.add("D3-NATIVE", "phonology", "onset_clusters must be exactly false")
    for sym in ("p", "f"):
        if sym not in cons:
            f.add("D3-NATIVE", "phonology",
                  "consonant %r missing from the declared union-stage inventory" % sym)
    return cons, vows, coda


def check_sound_change(doc, idx, f):
    changes = doc.get("sound_changes")
    changes = changes if isinstance(changes, list) else []
    exact = {
        "id": "SC1", "from": "p", "to": "f", "environment": "initial",
        "from_era": "E0", "to_era": "E1", "register": "ordinary",
    }
    if len(changes) != 1:
        f.add("D3-DERIVATION", "SC1",
              "exactly one declared sound change is required, got %d" % len(changes))
        return None
    law = changes[0]
    for key, want in sorted(exact.items()):
        if law.get(key) != want:
            f.add("D3-DERIVATION", law.get("id", "SC1"),
                  "declared law field %r must be %r, got %r" % (key, want, law.get(key)))
    return law


def check_lexicon(doc, idx, f):
    for lid in sorted(idx["lexicon"]):
        rec = idx["lexicon"][lid]
        forms = rec.get("forms")
        forms = forms if isinstance(forms, dict) else {}
        if set(forms.keys()) != {"E0", "E1"}:
            f.add("D3-DERIVATION", lid,
                  "forms must declare exactly the eras E0 and E1, got %r" % sorted(forms))
            continue
        e0, e1 = forms["E0"], forms["E1"]
        if rec.get("native_form") != e0:
            f.add("D3-DERIVATION", lid,
                  "native_form %r is not the E0 citation form %r"
                  % (rec.get("native_form"), e0))
        expected_e1 = apply_sc1(e0)
        if e1 != expected_e1:
            f.add("D3-DERIVATION", lid,
                  "E1 form %r does not equal the SC1 computation of E0 form %r (expected %r)"
                  % (e1, e0, expected_e1))
        if rec.get("status") != "constructed":
            f.add("D3-DERIVATION", lid,
                  "lexeme status must be 'constructed' (real-language genealogy is unclaimed), got %r"
                  % (rec.get("status"),))
        if rec.get("available_from") not in ERA_ORDINAL:
            f.add("D3-REFERENCE", lid,
                  "available_from %r is not a declared era id" % (rec.get("available_from"),))
    p_initial = sum(1 for r in idx["lexicon"].values() if r.get("forms", {}).get("E0", "").startswith("p"))
    unchanged = sum(
        1 for r in idx["lexicon"].values()
        if r.get("forms", {}).get("E0") is not None
        and r.get("forms", {}).get("E0") == r.get("forms", {}).get("E1")
    )
    if p_initial < 3:
        f.add("D3-DERIVATION", "lexicon",
              "fewer than three initial-p lexemes (%d declared)" % p_initial)
    if unchanged < 3:
        f.add("D3-DERIVATION", "lexicon",
              "fewer than three lexemes unchanged by SC1 (%d declared)" % unchanged)


def check_names(doc, idx, f):
    lex = idx["lexicon"]
    computed_forms = []
    for nid in sorted(idx["names"]):
        rec = idx["names"][nid]
        formation = rec.get("formation")
        if not isinstance(formation, dict):
            continue
        bases = formation.get("bases")
        if not isinstance(bases, list) or len(bases) != 2 or any(b not in lex for b in bases):
            continue
        if formation.get("operation") != "concat":
            f.add("D3-DERIVATION", nid,
                  "formation.operation must be 'concat', got %r" % (formation.get("operation"),))
        e1_forms = []
        for b in bases:
            forms = lex[b].get("forms", {})
            e1_forms.append(forms.get("E1"))
        if any(x is None for x in e1_forms):
            continue
        computed = "".join(e1_forms)
        computed_forms.append((nid, computed))
        if formation.get("expected") != computed:
            f.add("D3-DERIVATION", nid,
                  "formation.expected %r does not equal the concat of E1 base forms %r (computed %r)"
                  % (formation.get("expected"), e1_forms, computed))
        if rec.get("native_form") != computed:
            f.add("D3-DERIVATION", nid,
                  "native_form %r does not equal the computed concat %r"
                  % (rec.get("native_form"), computed))
        if rec.get("era") != "E1":
            f.add("D3-DERIVATION", nid,
                  "names are staged in era E1, got %r" % (rec.get("era"),))
        for b in bases:
            base_e1 = lex[b].get("forms", {}).get("E1")
            if rec.get("native_form") == base_e1:
                f.add("D3-DERIVATION", nid,
                      "name equals its base lexeme %s form %r" % (b, base_e1))
    forms_seen = {}
    for nid, computed in computed_forms:
        if computed in forms_seen:
            f.add("D3-NATIVE", nid,
                  "name form %r duplicates %s (names must be mutually distinct)"
                  % (computed, forms_seen[computed]))
        forms_seen[computed] = nid


def check_native_forms(doc, idx, f, cons, vows, codas):
    if not cons or not vows:
        return
    samples = []
    for lid in sorted(idx["lexicon"]):
        rec = idx["lexicon"][lid]
        samples.append((lid, rec.get("native_form")))
        for era in ("E0", "E1"):
            forms = rec.get("forms", {})
            if era in forms:
                samples.append((lid, forms[era]))
    for nid in sorted(idx["names"]):
        rec = idx["names"][nid]
        samples.append((nid, rec.get("native_form")))
        formation = rec.get("formation")
        if isinstance(formation, dict):
            samples.append((nid, formation.get("expected")))
    for uid in sorted(idx["utterances"]):
        rec = idx["utterances"][uid]
        samples.append((uid, rec.get("spoken_form")))
        samples.append((uid, rec.get("written_form")))
    for cid in sorted(idx["costumes"]):
        samples.append((cid, idx["costumes"][cid].get("native_form")))
    # Only native_form/spoken_form/written_form/forms/expected values are
    # phonotactically tested; display_label/gloss/proposition and every other
    # translated English field are deliberately never tested here.
    for record_id, value in samples:
        if not isinstance(value, str):
            continue
        reason = syllabify(value, cons, vows, codas)
        if reason is not None:
            f.add("D3-NATIVE", record_id,
                  "native form %r violates the declared profile: %s" % (value, reason))


def check_speech_rules(doc, idx, f):
    rules = idx["speech_rules"]
    for rid in sorted(rules):
        rec = rules[rid]
        exact = {
            "lexeme_id": "L01", "era": "E1", "register": "ritual",
            "place": "hall", "substitute_lexeme_id": "L02",
            "claim_kind": "constructed-rule",
        }
        for key, want in sorted(exact.items()):
            if rec.get(key) != want:
                f.add("D3-UTTERANCE", rid,
                      "avoidance rule field %r must be %r, got %r" % (key, want, rec.get(key)))
    if "AV1" not in rules:
        f.add("D3-UTTERANCE", "AV1", "the fixed avoidance rule AV1 is missing")


def check_utterances(doc, idx, f):
    lex = idx["lexicon"]
    rules = list(idx["speech_rules"].values())
    for uid in sorted(idx["utterances"]):
        rec = idx["utterances"][uid]
        anchor = UTTERANCE_ANCHORS.get(uid)
        if anchor is not None:
            for key, want in sorted(anchor.items()):
                if rec.get(key) != want:
                    f.add("D3-UTTERANCE", uid,
                          "fixed utterance field %r must be %r, got %r"
                          % (key, want, rec.get(key)))
        if rec.get("era") != "E1":
            f.add("D3-UTTERANCE", uid,
                  "utterances are staged in era E1, got %r" % (rec.get("era"),))
        if rec.get("register") not in ("ordinary", "ritual"):
            f.add("D3-UTTERANCE", uid,
                  "register must be 'ordinary' or 'ritual', got %r" % (rec.get("register"),))
        lid = rec.get("lexeme_id")
        source = lex.get(lid)
        if not isinstance(source, dict):
            continue
        forms = source.get("forms", {})
        e0 = forms.get("E0")
        e1 = forms.get("E1")
        if rec.get("written_form") != e0:
            f.add("D3-UTTERANCE", uid,
                  "written_form %r must retain the original lexeme's E0 form %r"
                  % (rec.get("written_form"), e0))
        match = None
        for rule in rules:
            if (
                rule.get("lexeme_id") == lid
                and rule.get("era") == rec.get("era")
                and rule.get("register") == rec.get("register")
                and rule.get("place") == rec.get("place")
            ):
                match = rule
                break
        substitute = lex.get(match.get("substitute_lexeme_id"), {}) if match else {}
        want_spoken = substitute.get("forms", {}).get("E0") if match else None
        if match is None:
            want_spoken = e1 if rec.get("register") == "ordinary" else e0
        if rec.get("spoken_form") != want_spoken:
            f.add("D3-UTTERANCE", uid,
                  "spoken_form %r fails the %s context law (expected %r; exact-match avoidance rule: %s)"
                  % (rec.get("spoken_form"), rec.get("register"), want_spoken, bool(match)))


def check_naming_rule(doc, idx, f):
    nr = doc.get("naming_rule")
    if not isinstance(nr, dict):
        return
    rid = nr.get("id", "NR1")
    offsets = nr.get("allowed_offsets")
    offsets = offsets if isinstance(offsets, list) else []
    if not offsets:
        f.add("D3-TIMING", rid, "allowed_offsets must be a nonempty integer set")
    else:
        if any(not _is_int(x) for x in offsets):
            f.add("D3-TIMING", rid,
                  "allowed_offsets must hold integers only (bools rejected), got %r" % (offsets,))
        if len(set(map(str, offsets))) != len(offsets):
            f.add("D3-TIMING", rid, "allowed_offsets must be unique, got %r" % (offsets,))
    chosen = nr.get("chosen_offset")
    if not _is_int(chosen):
        f.add("D3-TIMING", rid,
              "chosen_offset must be an integer (bools rejected), got %r" % (chosen,))
    elif not any(_is_int(x) and x == chosen for x in offsets):
        f.add("D3-TIMING", rid,
              "chosen_offset %r is outside the discrete allowed set %r" % (chosen, offsets))
    if nr.get("unit") != "fictional-nights":
        f.add("D3-TIMING", rid,
              "unit must be 'fictional-nights', got %r" % (nr.get("unit"),))
    if nr.get("status") != "constructed-not-historical":
        f.add("D3-MYTH", rid,
              "naming_rule.status must be 'constructed-not-historical', got %r "
              "(the fictional numbers must not claim historical prescription)"
              % (nr.get("status"),))
    if nr.get("source_id") != "S03":
        f.add("D3-BRIDGE", rid,
              "naming_rule must stay bridged to its declared source S03, got %r"
              % (nr.get("source_id"),))


def check_beliefs(doc, idx, f):
    propositions = {}
    for bid in sorted(idx["beliefs"]):
        rec = idx["beliefs"][bid]
        if rec.get("claim_kind") != "attributed-belief":
            f.add("D3-MYTH", bid,
                  "claim_kind must be 'attributed-belief', got %r" % (rec.get("claim_kind"),))
        if rec.get("truth_status") != "unresolved":
            f.add("D3-MYTH", bid,
                  "truth_status must remain 'unresolved', got %r "
                  "(no world-fact or supernatural certification)" % (rec.get("truth_status"),))
        if rec.get("era") != "E1":
            f.add("D3-MYTH", bid, "belief accounts are staged in era E1, got %r" % (rec.get("era"),))
        if not rec.get("speaker", "").strip():
            f.add("D3-MYTH", bid, "belief account must be explicitly attributed to a speaker")
        prop = rec.get("proposition", "")
        if not prop.strip():
            f.add("D3-MYTH", bid, "attributed proposition must be nonempty")
        propositions[bid] = prop
    if len(set(propositions.values())) < len(propositions):
        f.add("D3-MYTH", "-",
              "the two attributed accounts do not disagree (identical propositions)")


def check_symbols(doc, idx, f):
    for sid in sorted(idx["symbols"]):
        rec = idx["symbols"][sid]
        if rec.get("era") != "E1":
            f.add("D3-SYMBOL", sid,
                  "symbol era scope must be E1, got %r" % (rec.get("era"),))
        if not rec.get("audience", "").strip():
            f.add("D3-SYMBOL", sid, "symbol audience scope must be nonempty")
        if rec.get("claim_kind") != "constructed-rule":
            f.add("D3-SYMBOL", sid,
                  "claim_kind must be 'constructed-rule', got %r" % (rec.get("claim_kind"),))
        blob = ("%s %s" % (rec.get("display_label", ""), rec.get("reading", ""))).lower()
        for phrase in UNIVERSAL_PHRASES:
            if phrase in blob:
                f.add("D3-SYMBOL", sid,
                      "symbol asserts a universal meaning (%r present); no universal colour/meaning key"
                      % phrase)


def check_eras(doc, idx, f):
    for eid in ("E0", "E1"):
        rec = idx["eras"].get(eid)
        if not isinstance(rec, dict):
            continue
        if rec.get("ordinal") != ERA_ORDINAL[eid]:
            f.add("D3-ERA", eid,
                  "era %r must carry the relative ordinal %d, got %r "
                  "(fictional relative coordinates only)"
                  % (eid, ERA_ORDINAL[eid], rec.get("ordinal")))


def check_materials(doc, idx, f):
    for mid in ("M01", "M02", "M03"):
        rec = idx["materials"].get(mid)
        if not isinstance(rec, dict):
            continue
        case = MATERIAL_CASES[mid]
        if rec.get("available_from") != case["available_from"]:
            f.add("D3-ERA", mid,
                  "material availability must be %r, got %r"
                  % (case["available_from"], rec.get("available_from")))
        if rec.get("provenance") != case["provenance"]:
            f.add("D3-ERA", mid,
                  "material provenance must be %r, got %r"
                  % (case["provenance"], rec.get("provenance")))
        if rec.get("gate_name") != GATE_NAMES[mid]:
            f.add("D3-OBJECT", mid,
                  "gate_name must stay the declared interface anchor %r, got %r"
                  % (GATE_NAMES[mid], rec.get("gate_name")))
        routes = rec.get("routes")
        routes = routes if isinstance(routes, list) else []
        avail_ord = ERA_ORDINAL.get(rec.get("available_from"))
        matched_kind = False
        for j, route in enumerate(routes):
            if not isinstance(route, dict):
                continue
            kind = route.get("kind")
            if kind not in ("local", "import"):
                f.add("D3-ERA", mid, "routes[%d].kind must be 'local' or 'import', got %r"
                      % (j, kind))
            if route.get("stage") not in ("cloth", "trim"):
                f.add("D3-ERA", mid, "routes[%d].stage must be 'cloth' or 'trim', got %r"
                      % (j, route.get("stage")))
            eras = route.get("eras")
            eras = eras if isinstance(eras, list) else []
            if not eras:
                f.add("D3-ERA", mid, "routes[%d].eras must be nonempty" % j)
            for era in eras:
                if era not in ERA_ORDINAL:
                    f.add("D3-REFERENCE", mid,
                          "route era %r is not a declared era id" % (era,))
                elif avail_ord is not None and ERA_ORDINAL[era] < avail_ord:
                    f.add("D3-ERA", mid,
                          "route active in %r before the material's declared availability %r"
                          % (era, rec.get("available_from")))
            if kind == PROVENANCE_TO_ROUTE.get(rec.get("provenance")) and eras:
                matched_kind = True
        if routes and not matched_kind:
            f.add("D3-ERA", mid,
                  "no declared route agrees with the material's provenance %r"
                  % (rec.get("provenance"),))


def check_objects(doc, idx, f):
    for oid in ("O01", "O02", "O03", "O04"):
        rec = idx["objects"].get(oid)
        if not isinstance(rec, dict):
            continue
        case = OBJECT_CASES[oid]
        if rec.get("material_id") != case["material_id"]:
            f.add("D3-OBJECT", oid,
                  "object must stay bound to material %r, got %r"
                  % (case["material_id"], rec.get("material_id")))
        if rec.get("worn") != case["worn"]:
            f.add("D3-OBJECT", oid,
                  "object worn flag must be %r, got %r" % (case["worn"], rec.get("worn")))
        if oid == "O01" and rec.get("object_kind") != "ground-surface":
            f.add("D3-OBJECT", oid,
                  "O01 must remain a ground-surface, got %r" % (rec.get("object_kind"),))
        if rec.get("object_kind") == "ground-surface" and rec.get("worn"):
            f.add("D3-OBJECT", oid, "a ground-surface object is marked worn")


def check_costumes(doc, idx, f, name_forms):
    cons_rules = list(idx["rank_rules"].values())
    for cid in ("C01", "C02", "C03", "C04"):
        rec = idx["costumes"].get(cid)
        if not isinstance(rec, dict):
            continue
        case = COSTUME_CASES[cid]
        for key in ("object_id", "material_id", "era"):
            if rec.get(key) != case[key]:
                diag = "D3-ERA" if key == "era" else "D3-OBJECT"
                f.add(diag, cid,
                      "costume %s must be %r for its declared case, got %r"
                      % (key, case[key], rec.get(key)))
        for key in ("wearer_rank", "rite", "place"):
            if key in case and rec.get(key) != case[key]:
                f.add("D3-RANK", cid,
                      "prohibited-case binding %r must be %r, got %r"
                      % (key, case[key], rec.get(key)))
        obj = idx["objects"].get(rec.get("object_id"))
        if isinstance(obj, dict):
            if rec.get("material_id") != obj.get("material_id"):
                f.add("D3-OBJECT", cid,
                      "costume material %r does not match its object's material %r"
                      % (rec.get("material_id"), obj.get("material_id")))
            if obj.get("worn") is not True:
                f.add("D3-OBJECT", cid,
                      "costume bound to a non-worn object %r" % (rec.get("object_id"),))
        # native form must equal the anchored costume lexeme's era form
        anchored = COSTUME_LEXEMES[cid]
        lid = rec.get("lexeme_id", anchored)
        if lid != anchored:
            f.add("D3-REFERENCE", cid,
                  "costume lexeme binding must be %r, got %r" % (anchored, lid))
        lex = idx["lexicon"].get(anchored)
        if isinstance(lex, dict):
            want = lex.get("forms", {}).get(rec.get("era"))
            if rec.get("native_form") != want:
                f.add("D3-NATIVE", cid,
                      "native_form %r is not lexeme %s's %r form %r"
                      % (rec.get("native_form"), anchored, rec.get("era"), want))
        if rec.get("native_form") in name_forms:
            f.add("D3-NATIVE", cid,
                  "costume native_form %r collides with a declared name form"
                  % (rec.get("native_form"),))
        claim = interpret_claimed_status(rec.get("claimed_status", ""))
        if claim is None:
            f.add("D3-OBJECT", cid,
                  "claimed_status %r is not an interpretable lawful/violation declaration"
                  % (rec.get("claimed_status"),))
        # provenance and era availability against the material and its routes
        mat = idx["materials"].get(rec.get("material_id"))
        if isinstance(mat, dict):
            if rec.get("provenance") != mat.get("provenance"):
                f.add("D3-ERA", cid,
                      "declared provenance %r disagrees with the material's provenance %r"
                      % (rec.get("provenance"), mat.get("provenance")))
            avail = ERA_ORDINAL.get(mat.get("available_from"))
            era_ord = ERA_ORDINAL.get(rec.get("era"))
            if avail is not None and era_ord is not None and era_ord < avail:
                f.add("D3-ERA", cid,
                      "material %r is not available in the costume's declared era %r"
                      % (mat.get("id"), rec.get("era")))
            routes = mat.get("routes")
            routes = routes if isinstance(routes, list) else []
            covered = False
            for route in routes:
                if not isinstance(route, dict):
                    continue
                eras = route.get("eras")
                eras = eras if isinstance(eras, list) else []
                if (
                    rec.get("era") in eras
                    and route.get("kind") == PROVENANCE_TO_ROUTE.get(mat.get("provenance"))
                ):
                    covered = True
            if routes and not covered:
                f.add("D3-ERA", cid,
                      "no active provenance route covers the costume's declared era %r"
                      % (rec.get("era"),))
        # rank guard: reject only falsely claimed lawful entitlement to a
        # prohibited use; a declared violation stays visible.
        if claim == "lawful":
            for rule in cons_rules:
                prop = rule.get("property")
                prop = prop if isinstance(prop, dict) else {}
                mat_gate = mat.get("gate_name") if isinstance(mat, dict) else None
                if (
                    rule.get("effect") == "prohibit"
                    and rec.get("era") in (rule.get("eras") or [])
                    and rec.get("rite") in (rule.get("rites") or [])
                    and rec.get("place") == rule.get("jurisdiction")
                    and rec.get("wearer_rank") in (rule.get("wearer_ranks") or [])
                    and rec.get("wearer_rank") not in (rule.get("exempt_ranks") or [])
                    and prop.get("kind") == "material"
                    and mat_gate is not None
                    and mat_gate == prop.get("value")
                ):
                    f.add("D3-RANK", cid,
                          "falsely claims lawful entitlement to a use prohibited by %r "
                          "(material %r, %r in %r as %r)"
                          % (rule.get("id"), mat_gate, rec.get("rite"), rec.get("place"),
                             rec.get("wearer_rank")))


def check_rank_rules(doc, idx, f):
    rec = idx["rank_rules"].get("RR1")
    if not isinstance(rec, dict):
        return
    exact = {
        "jurisdiction": "hall",
        "effect": "prohibit",
    }
    for key, want in sorted(exact.items()):
        if rec.get(key) != want:
            f.add("D3-RANK", "RR1",
                  "rank rule field %r must be %r, got %r" % (key, want, rec.get(key)))
    if rec.get("eras") != ["E1"]:
        f.add("D3-RANK", "RR1",
              "rank rule eras must be ['E1'], got %r" % (rec.get("eras"),))
    if rec.get("rites") != ["assembly"]:
        f.add("D3-RANK", "RR1",
              "rank rule rites must be ['assembly'], got %r" % (rec.get("rites"),))
    if rec.get("wearer_ranks") != ["visitor"]:
        f.add("D3-RANK", "RR1",
              "rank rule wearer_ranks must be ['visitor'], got %r" % (rec.get("wearer_ranks"),))
    if rec.get("exempt_ranks") != []:
        f.add("D3-RANK", "RR1",
              "rank rule exempt_ranks must be empty, got %r" % (rec.get("exempt_ranks"),))
    if not rec.get("authority", "").strip():
        f.add("D3-RANK", "RR1", "rank rule authority must name the fictional hall authority")
    prop = rec.get("property")
    prop = prop if isinstance(prop, dict) else {}
    if prop.get("kind") != "material":
        f.add("D3-RANK", "RR1",
              "rank rule property.kind must be 'material', got %r" % (prop.get("kind"),))
    m02 = idx["materials"].get("M02")
    if isinstance(m02, dict) and prop.get("value") != m02.get("gate_name"):
        f.add("D3-RANK", "RR1",
              "rank rule must target the declared prohibited material (M02 gate_name %r), got %r"
              % (m02.get("gate_name"), prop.get("value")))


def check_references(doc, idx, f):
    for sid in ("S01", "S02", "S03", "S04", "S05"):
        rec = idx["references"].get(sid)
        if not isinstance(rec, dict):
            continue
        binding = SOURCE_BINDINGS[sid]
        for key in ("ledger_path", "audit_id", "source_url", "source_kind", "support_scope"):
            if rec.get(key) != binding[key]:
                f.add("D3-SCOPE", sid,
                      "reference %s %r differs from the effective round-6 reconciliation value %r"
                      % (key, rec.get(key), binding[key]))
        if not rec.get("limits", "").strip():
            f.add("D3-SCOPE", sid,
                  "reference limits must stay explicit (no unread whole-claim promotion)")
        declared = rec.get("file_sha256", "")
        closed = os.path.realpath(os.path.join(REPO_ROOT, binding["ledger_path"]))
        if closed != REPO_ROOT and not closed.startswith(REPO_ROOT + os.sep):
            f.add("D3-DATA", sid, "closed ledger path resolves outside the repository root")
            continue
        try:
            actual = sha256_bytes(read_file_bytes(closed))
        except OSError as exc:
            f.add("D3-DATA", sid,
                  "closed ledger %s cannot be read: %s"
                  % (binding["ledger_path"], exc.strerror or exc))
            continue
        if declared.strip().lower() != actual:
            f.add("D3-DIGEST", sid,
                  "declared file_sha256 %r disagrees with actual bytes of %s (%s)"
                  % (declared, binding["ledger_path"], actual))


def check_bridges(doc, idx, f):
    for bid in ("BR01", "BR02", "BR03", "BR04", "BR05"):
        rec = idx["bridges"].get(bid)
        if not isinstance(rec, dict):
            continue
        case = BRIDGE_CASES[bid]
        if rec.get("source_id") != case["source_id"]:
            f.add("D3-BRIDGE", bid,
                  "bridge must be bound to source %r, got %r"
                  % (case["source_id"], rec.get("source_id")))
        targets = rec.get("target_ids")
        targets = targets if isinstance(targets, list) else []
        if sorted(targets) != sorted(case["targets"]):
            f.add("D3-BRIDGE", bid,
                  "bridge targets %r differ from the declared design-only mapping %r"
                  % (targets, case["targets"]))
        if rec.get("relation") not in ("method-transfer", "analogy"):
            f.add("D3-BRIDGE", bid,
                  "relation must be 'method-transfer' or 'analogy', got %r"
                  % (rec.get("relation"),))
        if rec.get("asserted_scope") != "design-only":
            f.add("D3-BRIDGE", bid,
                  "asserted_scope must be 'design-only', got %r (no historical reconstruction claim)"
                  % (rec.get("asserted_scope"),))
        if rec.get("claim_kind") != "constructed-rule":
            f.add("D3-BRIDGE", bid,
                  "claim_kind must be 'constructed-rule', got %r" % (rec.get("claim_kind"),))
        for key in ("mechanism", "limits"):
            if not rec.get(key, "").strip():
                f.add("D3-BRIDGE", bid, "bridge %s must be a nonempty statement" % key)


def run_checks(doc):
    f = Findings()
    check_canon(doc, f)
    check_screening(doc, f)
    idx = build_indexes(doc, f)
    check_cross_references(doc, idx, f)
    phon = check_phonology(doc, f)
    cons, vows, codas = phon if isinstance(phon, tuple) else (set(), set(), set())
    check_sound_change(doc, idx, f)
    check_lexicon(doc, idx, f)
    check_names(doc, idx, f)
    check_native_forms(doc, idx, f, cons, vows, codas)
    check_speech_rules(doc, idx, f)
    check_utterances(doc, idx, f)
    check_naming_rule(doc, idx, f)
    check_beliefs(doc, idx, f)
    check_symbols(doc, idx, f)
    check_eras(doc, idx, f)
    check_materials(doc, idx, f)
    check_objects(doc, idx, f)
    name_forms = {rec.get("native_form") for rec in idx["names"].values()}
    check_costumes(doc, idx, f, name_forms)
    check_rank_rules(doc, idx, f)
    check_references(doc, idx, f)
    check_bridges(doc, idx, f)
    return f.items


# --- frozen snapshot mode ----------------------------------------------------
def snapshot_finding(message):
    return finding("D3-SNAPSHOT", "-", message)


def load_expected(path):
    doc, err = load_json_document(path, "D3-SNAPSHOT", "frozen expectation")
    if err is not None:
        return None, err
    if doc.get("profile") != PROFILE:
        return None, snapshot_finding(
            "frozen expectation profile %r is not %r" % (doc.get("profile"), PROFILE))
    manifest = doc.get("manifest")
    if not isinstance(manifest, dict) or not manifest:
        return None, snapshot_finding("frozen expectation manifest must be a nonempty object")
    for key, value in sorted(manifest.items()):
        if not isinstance(key, str) or not key:
            return None, snapshot_finding("manifest keys must be nonempty strings")
        if not isinstance(value, str) or len(value) != 64 or any(
            c not in "0123456789abcdef" for c in value.lower()
        ):
            return None, snapshot_finding(
                "manifest digest for %r must be a 64-hex sha256 string" % key)
    expected_exit = doc.get("expected_exit")
    if type(expected_exit) is not int or expected_exit not in (EXIT_OK, EXIT_FINDINGS):
        return None, snapshot_finding(
            "expected_exit must be the integer 0 or 1 (booleans rejected), got %r"
            % (expected_exit,))
    finding_ids = doc.get("finding_ids")
    if not isinstance(finding_ids, list) or not all(isinstance(x, str) for x in finding_ids):
        return None, snapshot_finding("finding_ids must be an array of diagnostic id strings")
    return doc, None


def safe_repo_path(key):
    """Resolve a manifest key inside REPO_ROOT only. Returns realpath or None."""
    if not isinstance(key, str) or not key or key.startswith("/"):
        return None
    if "\\" in key or ":" in key:
        return None
    parts = key.split("/")
    if any(p in ("", ".", "..") for p in parts):
        return None
    candidate = os.path.realpath(os.path.join(REPO_ROOT, *parts))
    if candidate != REPO_ROOT and not candidate.startswith(REPO_ROOT + os.sep):
        return None
    return candidate


def verify_manifest(expected, packet_path):
    errors = []
    manifest = expected.get("manifest", {})
    resolved = {}
    for key in sorted(manifest):
        path = safe_repo_path(key)
        if path is None:
            errors.append(snapshot_finding(
                "manifest path %r is not a safe repository-relative path" % key))
            continue
        try:
            actual = sha256_bytes(read_file_bytes(path))
        except OSError as exc:
            errors.append(snapshot_finding(
                "manifest input %r cannot be read: %s" % (key, exc.strerror or exc)))
            continue
        if actual != manifest[key].lower():
            errors.append(snapshot_finding(
                "manifest digest mismatch for %r: declared %s, actual %s"
                % (key, manifest[key], actual)))
        resolved[os.path.realpath(path)] = key
    packet_real = os.path.realpath(packet_path)
    if packet_real not in resolved:
        errors.append(snapshot_finding(
            "packet %r is not covered by the frozen manifest" % packet_path))
    return errors


# --- CLI ---------------------------------------------------------------------
class UsageError(Exception):
    pass


def parse_args(args):
    packet = None
    frozen = None
    i = 0
    while i < len(args):
        tok = args[i]
        if tok == "--frozen":
            if frozen is not None:
                raise UsageError("--frozen given twice")
            if i + 1 >= len(args) or args[i + 1].startswith("-"):
                raise UsageError("--frozen needs an expected.json path")
            frozen = args[i + 1]
            i += 2
        elif tok.startswith("-") and tok != "-":
            raise UsageError("unknown option %r" % tok)
        elif packet is None:
            packet = tok
            i += 1
        else:
            raise UsageError("unexpected extra argument %r" % tok)
    if packet is None:
        raise UsageError("expected <packet.json> [--frozen <expected.json>]")
    return packet, frozen


def run_cli(args):
    try:
        packet, frozen = parse_args(args)
    except UsageError as exc:
        sys.stderr.write("CLI-ERROR D3-DATA usage: %s\n" % exc)
        return emit([finding("D3-DATA", "-", "usage: %s" % exc)], EXIT_ERROR)

    doc, err = load_json_document(packet, "D3-DATA", "packet")

    expected = None
    if frozen is not None:
        # Snapshot mode verifies every persisted input digest FIRST; a tampered
        # or unreadable manifest input reports D3-SNAPSHOT before any verdict.
        expected, err2 = load_expected(frozen)
        if err2 is not None:
            return emit([err2], EXIT_ERROR)
        snap_errors = verify_manifest(expected, packet)
        if snap_errors:
            return emit(snap_errors, EXIT_ERROR)
    if err is not None:
        return emit([err], EXIT_ERROR)
    shape_errors = validate_shape(doc)
    if shape_errors:
        return emit(
            [finding("D3-DATA", "-", msg) for msg in shape_errors], EXIT_ERROR
        )

    findings = run_checks(doc)
    if any(x["id"] == "D3-DATA" for x in findings):
        code = EXIT_ERROR
    elif findings:
        code = EXIT_FINDINGS
    else:
        code = EXIT_OK
    if expected is not None:
        want = (
            expected.get("expected_exit"),
            sorted({x for x in expected.get("finding_ids", [])}),
        )
        got = (code, sorted({x["id"] for x in findings}))
        if want != got:
            return emit(
                [
                    snapshot_finding(
                        "frozen expectation mismatch: declared expected_exit/finding_ids %r, "
                        "actual verdict %r" % (want, got)
                    )
                ],
                EXIT_ERROR,
            )
    return emit(findings, code)


# --- JSON-pointer patches (selftest fixtures only) ----------------------------
class PatchError(Exception):
    pass


def _unescape(token):
    return token.replace("~1", "/").replace("~0", "~")


def apply_patch(doc, op):
    if not isinstance(op, dict):
        raise PatchError("patch entry must be an object")
    action = op.get("op")
    if action not in ("add", "replace", "remove"):
        raise PatchError("unsupported op %r" % (action,))
    path = op.get("path")
    if not isinstance(path, str) or not path.startswith("/"):
        raise PatchError("patch path must be a JSON pointer string")
    tokens = [_unescape(t) for t in path.split("/")[1:]]
    if not tokens:
        raise PatchError("patch path must point inside the document")
    container = doc
    for token in tokens[:-1]:
        if isinstance(container, list):
            try:
                container = container[int(token)]
            except (ValueError, IndexError):
                raise PatchError("bad list index %r in path %r" % (token, path))
        elif isinstance(container, dict):
            if token not in container:
                raise PatchError("missing key %r in path %r" % (token, path))
            container = container[token]
        else:
            raise PatchError("cannot descend into %r at %r" % (container, token))
    last = tokens[-1]
    if isinstance(container, list):
        try:
            position = int(last)
        except ValueError:
            raise PatchError("bad list index %r" % last)
        if action == "add":
            if not 0 <= position <= len(container):
                raise PatchError("add index %d out of range" % position)
            container.insert(position, op.get("value"))
        else:
            if not 0 <= position < len(container):
                raise PatchError("index %d out of range" % position)
            if action == "remove":
                container.pop(position)
            else:
                container[position] = op.get("value")
    elif isinstance(container, dict):
        if action == "add":
            container[last] = op.get("value")
        elif action == "remove":
            if last not in container:
                raise PatchError("cannot remove missing key %r" % last)
            del container[last]
        else:
            if last not in container:
                raise PatchError("cannot replace missing key %r" % last)
            container[last] = op.get("value")
    else:
        raise PatchError("patch target container is not a list or object")


def patched_copy(doc, patches):
    work = json.loads(json.dumps(doc))
    for op in patches or []:
        apply_patch(work, op)
    return work


# --- selftest -----------------------------------------------------------------
SELFTEST_PACKET = "examples/culture-d3/packet.json"
SELFTEST_CONTROLS = "examples/culture-d3/controls.json"


def selftest_result(results, name, kind, passed, expected, actual, detail=None):
    entry = {"name": name, "kind": kind, "passed": passed,
             "expected": expected, "actual": actual}
    if detail:
        entry["detail"] = detail
    results.append(entry)
    return passed


def run_subprocess(args, cwd):
    return subprocess.run(
        [sys.executable, os.path.abspath(__file__)] + args,
        capture_output=True, text=True, cwd=cwd,
    )


def parse_cli_stdout(proc):
    try:
        return json.loads(proc.stdout)
    except ValueError:
        return None


def run_case(results, name, kind, args, cwd, want_exit, want_ids=None,
             empty_findings=False, spec=None):
    proc = run_subprocess(args, cwd)
    blob = proc.stdout + proc.stderr
    passed = True
    detail = None
    if "Traceback" in blob:
        passed = False
        detail = "traceback leaked"
    if passed and proc.returncode != want_exit:
        passed = False
        tail = proc.stderr.strip().splitlines()[-1] if proc.stderr.strip() else ""
        detail = "exit %d, want %d (%s)" % (proc.returncode, want_exit, tail[-200:])
    parsed = None
    if passed and kind != "cli-usage":
        parsed = parse_cli_stdout(proc)
        if parsed is None:
            passed = False
            detail = "stdout is not the contract JSON object"
    if passed and parsed is not None and parsed.get("exit") != want_exit:
        passed = False
        detail = "json exit %r, want %r" % (parsed.get("exit"), want_exit)
    if passed and empty_findings and parsed is not None and parsed.get("findings") != []:
        passed = False
        detail = "expected a clean verdict, got findings %r"
        detail = detail % ([x.get("id") for x in parsed.get("findings", [])],)
    if passed and want_ids and parsed is not None:
        got = {x.get("id") for x in parsed.get("findings", [])}
        missing = sorted(set(want_ids) - got)
        if missing:
            passed = False
            detail = "expected diagnostic ids %r absent (got %r)" % (missing, sorted(got))
    if spec is not None and passed and not spec.get("ok", True):
        passed = False
        detail = spec.get("detail")
    return selftest_result(results, name, kind, passed, want_exit,
                           proc.returncode, detail)


def build_malformed_file(directory, kind, packet_bytes):
    path = os.path.join(directory, "malformed-%s.json" % kind)
    if kind == "invalid-json":
        data = packet_bytes[: max(1, len(packet_bytes) // 2)]
    elif kind == "invalid-utf8":
        data = b"\xff\xfe\x00" + packet_bytes[:24]
    elif kind == "wrong-root":
        data = b"[]"
    elif kind == "missing-file":
        return None
    else:
        return None
    with open(path, "wb") as fh:
        fh.write(data)
    return path


def run_selftest(argv):
    result = {
        "profile": PROFILE,
        "selftest_passed": False,
        "positive_controls": {"total": 0, "passed": 0},
        "domain_controls": {"total": 0, "passed": 0},
        "malformed_controls": {"total": 0, "passed": 0},
        "frozen_checks": {"total": 0, "passed": 0},
        "results": [],
        "missing_inputs": [],
    }
    extra = [t for t in argv[1:] if t != "--selftest"]
    if extra:
        result["error"] = "--selftest takes no other arguments, got %r" % (extra,)
        sys.stderr.write("CLI-ERROR D3-DATA usage: %s\n" % result["error"])
        print(json.dumps(result, indent=2, sort_keys=True))
        return EXIT_ERROR

    packet_path = os.path.join(REPO_ROOT, SELFTEST_PACKET)
    controls_path = os.path.join(REPO_ROOT, SELFTEST_CONTROLS)
    missing = [
        rel for rel, path in (
            (SELFTEST_PACKET, packet_path),
            (SELFTEST_CONTROLS, controls_path),
        ) if not os.path.isfile(path)
    ]
    result["missing_inputs"] = missing

    tmp = tempfile.mkdtemp(prefix="d3-evidence-coupling-selftest-")
    exit_code = EXIT_ERROR
    try:
        if missing:
            result["note"] = (
                "committed selftest inputs absent; run what is runnable and report the "
                "unrun dependencies honestly"
            )
            print(json.dumps(result, indent=2, sort_keys=True))
            return EXIT_ERROR

        packet_bytes = read_file_bytes(packet_path)
        packet_doc, err = load_json_document(packet_path, "D3-DATA", "packet")
        packet_copy = os.path.join(tmp, "packet.json")
        with open(packet_copy, "wb") as fh:
            fh.write(packet_bytes)

        results = result["results"]
        foreign = tempfile.mkdtemp(prefix="d3-selftest-foreign-", dir=tmp)

        # positive packet over both the repo cwd and a foreign cwd
        run_case(results, "positive-repo-cwd", "positive",
                 [packet_copy], REPO_ROOT, EXIT_OK, empty_findings=True)
        run_case(results, "positive-foreign-cwd", "positive",
                 [packet_copy], foreign, EXIT_OK, empty_findings=True)

        # usage battery (JSON stdout, exit 2, never a traceback)
        run_case(results, "usage-no-arguments", "cli-usage", [], tmp, EXIT_ERROR)
        run_case(results, "usage-unknown-option", "cli-usage",
                 [packet_copy, "--bogus"], tmp, EXIT_ERROR)

        controls, err = load_json_document(controls_path, "D3-DATA", "controls")
        controls_ok = err is None
        if not controls_ok:
            selftest_result(results, "controls-file", "controls", False,
                            "readable independent controls", "unreadable",
                            err["message"] if isinstance(err, dict) else str(err))
        shortfall = None
        positive_controls, domain_controls, malformed_controls = [], [], []
        if controls_ok:
            positive_controls = controls.get("positive") or []
            domain_controls = controls.get("domain") or []
            malformed_controls = controls.get("malformed") or []
            shortfall = {}
            if len(positive_controls) < 1:
                shortfall["positive"] = "at least one positive control required"
            if len(domain_controls) < 12:
                shortfall["domain"] = "at least twelve domain negatives required"
            if len(malformed_controls) < 4:
                shortfall["malformed"] = "at least four malformed controls required"
            if shortfall:
                result["control_shortfall"] = shortfall

        for control in positive_controls:
            name = str(control.get("name", "positive-?"))
            spec = {"ok": True}
            if control.get("expected_exit") not in (EXIT_OK, None):
                spec = {"ok": False,
                        "detail": "positive control expected_exit must be 0"}
            try:
                work = patched_copy(packet_doc, control.get("patches"))
                path = os.path.join(tmp, "positive-%s.json" % name.replace("/", "_"))
                with open(path, "w", encoding="utf-8") as fh:
                    json.dump(work, fh, indent=2)
                run_case(results, "positive:%s" % name, "positive",
                         [path], foreign, EXIT_OK, empty_findings=True, spec=spec)
            except PatchError as exc:
                selftest_result(results, "positive:%s" % name, "positive", False,
                                "patched copy runs clean", "patch failed", str(exc))

        for control in domain_controls:
            name = str(control.get("name", "domain-?"))
            want_exit = control.get("expected_exit")
            want_ids = control.get("expected_ids") or []
            spec = {"ok": True}
            if want_exit != EXIT_FINDINGS or not want_ids:
                spec = {"ok": False,
                        "detail": "domain control must expect exit 1 with stable expected_ids"}
            try:
                work = patched_copy(packet_doc, control.get("patches"))
                path = os.path.join(tmp, "domain-%s.json" % name.replace("/", "_"))
                with open(path, "w", encoding="utf-8") as fh:
                    json.dump(work, fh, indent=2)
                run_case(results, "domain:%s" % name, "domain",
                         [path], foreign, EXIT_FINDINGS, want_ids=want_ids, spec=spec)
            except PatchError as exc:
                selftest_result(results, "domain:%s" % name, "domain", False,
                                want_ids, "patch failed", str(exc))

        for control in malformed_controls:
            name = str(control.get("name", "malformed-?"))
            kind = control.get("kind")
            want_ids = control.get("expected_ids") or ["D3-DATA"]
            path = build_malformed_file(tmp, kind, packet_bytes)
            if path is None:
                if kind == "missing-file":
                    path = os.path.join(tmp, "absent-malformed-input.json")
                else:
                    selftest_result(results, "malformed:%s" % name, "malformed", False,
                                    EXIT_ERROR, "unknown malformed kind %r" % (kind,))
                    continue
            run_case(results, "malformed:%s" % name, "malformed",
                     [path], foreign, EXIT_ERROR, want_ids=want_ids)

        # frozen snapshot verification over live digests (copies stay in tmp)
        component_entries = {}
        absent_components = []
        for rel in COMPONENT_PATHS:
            abs_path = os.path.join(REPO_ROOT, rel)
            if os.path.isfile(abs_path):
                component_entries[rel] = sha256_bytes(read_file_bytes(abs_path))
            else:
                absent_components.append(rel)
        if absent_components:
            result["frozen_component_note"] = (
                "component files absent from the frozen manifest: %s" % ", ".join(absent_components)
            )
        good_manifest = {SELFTEST_PACKET: sha256_bytes(packet_bytes)}
        good_manifest.update(component_entries)
        expected_good = os.path.join(tmp, "expected-good.json")
        with open(expected_good, "w", encoding="utf-8") as fh:
            json.dump({"profile": PROFILE, "manifest": good_manifest,
                       "expected_exit": EXIT_OK, "finding_ids": []}, fh, indent=2)
        run_case(results, "frozen-good", "frozen",
                 [packet_path, "--frozen", expected_good], foreign, EXIT_OK,
                 empty_findings=True)

        tampered = dict(good_manifest)
        first_key = sorted(tampered)[0]
        digest = tampered[first_key]
        flipped = "0" if digest[0] != "0" else "1"
        tampered[first_key] = flipped + digest[1:]
        expected_tampered = os.path.join(tmp, "expected-tampered.json")
        with open(expected_tampered, "w", encoding="utf-8") as fh:
            json.dump({"profile": PROFILE, "manifest": tampered,
                       "expected_exit": EXIT_OK, "finding_ids": []}, fh, indent=2)
        run_case(results, "frozen-tampered-digest", "frozen",
                 [packet_path, "--frozen", expected_tampered], foreign, EXIT_ERROR,
                 want_ids=["D3-SNAPSHOT"])

        unknown_manifest = dict(good_manifest)
        unknown_manifest["examples/culture-d3/components/99-absent.json"] = "0" * 64
        expected_unknown = os.path.join(tmp, "expected-unknown.json")
        with open(expected_unknown, "w", encoding="utf-8") as fh:
            json.dump({"profile": PROFILE, "manifest": unknown_manifest,
                       "expected_exit": EXIT_OK, "finding_ids": []}, fh, indent=2)
        run_case(results, "frozen-unknown-manifest-entry", "frozen",
                 [packet_path, "--frozen", expected_unknown], foreign, EXIT_ERROR,
                 want_ids=["D3-SNAPSHOT"])

        # recorded defect fix: boolean frozen verdict labels must not alias to
        # integers; true/false expected_exit both reject with D3-SNAPSHOT
        for label, value in (("false", False), ("true", True)):
            expected_bool = os.path.join(tmp, "expected-bool-%s.json" % label)
            with open(expected_bool, "w", encoding="utf-8") as fh:
                json.dump({"profile": PROFILE, "manifest": good_manifest,
                           "expected_exit": value, "finding_ids": []}, fh, indent=2)
            run_case(results, "frozen-bool-expected-exit-%s" % label, "frozen",
                     [packet_path, "--frozen", expected_bool], foreign, EXIT_ERROR,
                     want_ids=["D3-SNAPSHOT"])

        # counts computed from executed results
        for key, kind in (("positive_controls", "positive"),
                          ("domain_controls", "domain"),
                          ("malformed_controls", "malformed"),
                          ("frozen_checks", "frozen")):
            rows = [r for r in results if r["kind"] == kind]
            result[key]["total"] = len(rows)
            result[key]["passed"] = sum(1 for r in rows if r["passed"])

        failures = [r for r in results if not r["passed"]]
        if failures:
            exit_code = EXIT_FINDINGS
            result["note"] = "executed selftest cases failed; see results"
        elif missing or shortfall or not controls_ok:
            exit_code = EXIT_ERROR
            result["note"] = "independent controls incomplete; unrun dependencies reported"
        else:
            exit_code = EXIT_OK
            result["note"] = "all committed-input selftest cases passed"
        result["selftest_passed"] = not failures and not missing and not shortfall and controls_ok
        print(json.dumps(result, indent=2, sort_keys=True))
        return exit_code
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv):
    try:
        if "--selftest" in argv:
            return run_selftest(argv)
        return run_cli(argv[1:])
    except SystemExit:
        raise
    except Exception as exc:  # never leak a traceback
        sys.stderr.write("CLI-ERROR D3-DATA internal: %r\n" % (exc,))
        return emit(
            [finding("D3-DATA", "-", "internal evaluation failure: %s" % exc)],
            EXIT_ERROR,
        )


if __name__ == "__main__":
    sys.exit(main(sys.argv))
