#!/usr/bin/env python3
"""In-memory checker for the non-canon exercise examples/supplement-opencode-1/sound-change-vs-taboo.json.

Stdlib only. Rebuilds the toy law engine from the JSON's law_list.order, recomputes
every declared derivation, verifies the data-level assertions (name avoidance,
register partition, loan strata, symbol readings), the audit-row schema, and the
report file's required headings. Exit codes: 0 clean, 1 findings, 2 usage or
input errors (stable CRAFT-CLI-* diagnostic on stderr, never a traceback):
  CRAFT-CLI-USAGE          missing/extra/unknown argument
  CRAFT-CLI-NOT-FOUND      exercise file cannot be read
  CRAFT-CLI-UTF8           exercise file is not valid UTF-8
  CRAFT-CLI-JSON           exercise file is not valid JSON
  CRAFT-CLI-SHAPE          exercise root is not a JSON object
  CRAFT-CLI-REPORT-VALUE   --report given without a path value
  CRAFT-CLI-REPORT-OPEN    --report file cannot be read
  CRAFT-CLI-REPORT-UTF8    --report file is not valid UTF-8

Usage:
  python3 tools/check-craft-exercise.py <exercise.json> [--report <report.md>]
  python3 tools/check-craft-exercise.py <exercise.json> --counts
  python3 tools/check-craft-exercise.py --selftest [exercise.json]

--selftest reruns the ten in-process tamper detections, then drives this
script as a real subprocess over positive and malformed-input CLI cases in an
isolated temp directory; both parts work from any working directory. It takes
at most one optional exercise path after --selftest and no other tokens;
anything else exits 2.
A selftest target must carry the structure the tamper battery mutates.
Loaded documents are shape-validated at the boundary: wrong-typed containers
or fields the checker reads as strings/keys (e.g. {"audits": [3]}) exit 2 with
CRAFT-CLI-SHAPE before any check runs, keeping domain findings at exit 1.
Option values (such as the --report path) must not begin with "-".
"""
import copy
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

VOWELS = set("aeiou")

# --- toy law engine -------------------------------------------------------
# Rule semantics mirror law_list in the JSON. L3 fires word-initially before a
# vowel or intervocalically; L4 deletes a word-final vowel.


def law_l1(w):
    return "".join(
        "v" if (c == "p" and 0 < i < len(w) - 1 and w[i - 1] in VOWELS and w[i + 1] in VOWELS) else c
        for i, c in enumerate(w)
    )


def law_l2(w):
    return "".join(
        "r" if (c == "l" and 0 < i < len(w) - 1 and w[i - 1] in VOWELS and w[i + 1] in VOWELS) else c
        for i, c in enumerate(w)
    )


def law_l3(w):
    return "".join(
        "h" if (c == "k" and i + 1 < len(w) and w[i + 1] in VOWELS and (i == 0 or w[i - 1] in VOWELS)) else c
        for i, c in enumerate(w)
    )


def law_l4(w):
    return w[:-1] if w and w[-1] in VOWELS else w


LAW_FUNCS = {"L1": law_l1, "L2": law_l2, "L3": law_l3, "L4": law_l4}

UNIVERSAL_PHRASES = [
    "always means",
    "universally means",
    "means the same to all",
    "in every culture",
    "to everyone",
    "same to every audience",
]
SACRED_TERMS = [
    "Tetragrammaton",
    "YHWH",
    "Mishnah",
    "Eucharist",
    "Bible",
    "Quran",
    "Torah",
    "Christ",
    "God's wounds",
    "Explicit Name",
    "High Priest",
]
AUDIT_KEYS = {
    "id",
    "claim",
    "entry_locator",
    "source_url",
    "retrieval_status",
    "source_locator",
    "source_excerpt",
    "verdict",
    "basis",
    "access_limit",
}
VERDICTS = {"supported", "contradicted", "unresolved"}
RETRIEVALS = {"full_text", "partial", "blocked"}


class Findings:
    def __init__(self):
        self.items = []

    def add(self, fid, detail):
        self.items.append((fid, detail))


def iter_strings(obj, skip_key=None):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == skip_key:
                continue
            yield from iter_strings(v, skip_key=skip_key)
    elif isinstance(obj, list):
        for v in obj:
            yield from iter_strings(v, skip_key=skip_key)
    elif isinstance(obj, str):
        yield obj


def run_checks(doc, report_text=None):
    f = Findings()
    ex = doc.get("exercise", {})

    # --- audit rows -------------------------------------------------------
    audits = doc.get("audits", [])
    if len(audits) < 2:
        f.add("AUDIT-COUNT", "fewer than 2 audits")
    coupling = 0
    for a in audits:
        aid = a.get("id", "?")
        missing = AUDIT_KEYS - set(a.keys())
        if missing:
            f.add("AUDIT-SCHEMA", f"{aid} missing keys: {sorted(missing)}")
        if a.get("verdict") not in VERDICTS:
            f.add("AUDIT-VERDICT", f"{aid} has verdict {a.get('verdict')!r}")
        if a.get("retrieval_status") not in RETRIEVALS:
            f.add("AUDIT-RETRIEVAL", f"{aid} has retrieval_status {a.get('retrieval_status')!r}")
        ex_ = a.get("source_excerpt", "")
        words = len(ex_.split())
        if words > 40:
            f.add("AUDIT-EXCERPT-LONG", f"{aid} excerpt {words} words")
        if a.get("retrieval_status") == "full_text" and words == 0:
            f.add("AUDIT-EXCERPT-MISSING", f"{aid} claims full_text but has no excerpt")
        if a.get("retrieval_status") in ("blocked",) and not a.get("access_limit"):
            f.add("AUDIT-LIMIT-MISSING", f"{aid} blocked without access_limit")
        if "coupling" in a.get("basis", "").lower():
            coupling += 1
    if coupling < 1:
        f.add("AUDIT-COUPLING", "no audit basis names a coupling test")

    counts = doc.get("audit_counts", {})
    if audits:
        got = {
            "total": len(audits),
            "retrieval_status_full_text": sum(1 for a in audits if a.get("retrieval_status") == "full_text"),
            "retrieval_status_blocked": sum(1 for a in audits if a.get("retrieval_status") == "blocked"),
            "verdict_supported": sum(1 for a in audits if a.get("verdict") == "supported"),
            "verdict_unresolved": sum(1 for a in audits if a.get("verdict") == "unresolved"),
            "verdict_contradicted": sum(1 for a in audits if a.get("verdict") == "contradicted"),
        }
        for k, v in got.items():
            if counts.get(k) != v:
                f.add("AUDIT-COUNT-MISMATCH", f"{k}: declared {counts.get(k)} measured {v}")
        if len(audits) != counts.get("verdict_supported", 0) + counts.get("verdict_unresolved", 0) + counts.get("verdict_contradicted", 0):
            f.add("AUDIT-COUNT-MISMATCH", "verdict tally does not sum to total")

    # --- derivations and law engine --------------------------------------
    derivations = ex.get("derivations", [])
    if len(derivations) < 6:
        f.add("DERIVATION-COUNT", f"{len(derivations)} derivations (need >= 6)")
    for d in derivations:
        did = d.get("id", "?")
        for ctrl in ("positive_control", "negative_control"):
            c = d.get(ctrl)
            if not isinstance(c, dict) or not c.get("assert"):
                f.add("CONTROL-MISSING", f"{did} lacks {ctrl}")

    order_names = ex.get("law_list", {}).get("order", [])
    if sorted(order_names) != ["L1", "L2", "L3", "L4"]:
        f.add("LAW-ORDER", f"law_list.order is {order_names}")
        return f, counts
    mech = ex.get("mech_expectations", {})
    declared = [LAW_FUNCS[n] for n in order_names]
    reversed_ = list(reversed(declared))
    for case in mech.get("cases", []):
        cid = case.get("id", "?")
        funcs = declared if case.get("order") == "declared" else reversed_
        for word, exp in case.get("cases", {}).items():
            if case.get("mode") == "post_laws":
                out = word
            else:
                out = word
                for fn in funcs:
                    out = fn(out)
            if out != exp:
                f.add("MECH-RECOMPUTE", f"{cid} {word} -> {out}, declared {exp} (order {case.get('order')})")

    # --- name avoidance data assertions ----------------------------------
    na = ex.get("name_avoidance", {})
    roll = na.get("distribution_test", {}).get("public_roll_year_340", {})
    if roll.get("founder_designation") != "en":
        f.add("NAME-AVOIDANCE", "founder designation in year-340 roll is not 'en'")
    if roll.get("harvest_line_dawn_word") != "har":
        f.add("NAME-AVOIDANCE", "dawn word in year-340 roll is not 'har' (homophone control)")
    if roll.get("founder_designation") == roll.get("harvest_line_dawn_word"):
        f.add("NAME-AVOIDANCE", "substitution and homophone control collapsed")

    # --- register partition (D8) -----------------------------------------
    d8 = next((d for d in derivations if d.get("id") == "D8"), None)
    if d8 is None:
        f.add("REGISTER-PARTITION", "D8 missing")
    else:
        blob = json.dumps(d8)
        if "aku" not in blob or "vesav" not in blob:
            f.add("REGISTER-PARTITION", "D8 does not mention both aku and vesav")

    # --- loan strata ------------------------------------------------------
    terms = {t.get("term"): t for t in ex.get("borrowed_garment_terms", {}).get("terms", [])}
    if "avih" not in terms or "apika" not in terms:
        f.add("LOAN-STRATA", "avih/apika strata missing")
    else:
        for name, must_contain in (("avih", "S1"), ("apika", "S2")):
            stratum = terms[name].get("stratum", "")
            if must_contain not in stratum:
                f.add("LOAN-STRATA", f"{name} stratum does not name {must_contain}: {stratum!r}")

    # --- symbol readings --------------------------------------------------
    sr = ex.get("symbol_readings", {})
    readings = sr.get("readings", [])
    if len(readings) < 3:
        f.add("SYMBOL-READINGS", f"{len(readings)} readings (need >= 3)")
    meanings = {r.get("reading") for r in readings}
    audiences = {r.get("audience") for r in readings}
    if len(meanings) < 2:
        f.add("SYMBOL-READINGS", "fewer than 2 distinct readings")
    if len(audiences) < 3:
        f.add("SYMBOL-READINGS", "fewer than 3 distinct audiences")
    note = (sr.get("constraint", "") + " " + sr.get("motif", "")).lower()
    if "no universal" not in note and "not asserted" not in note:
        f.add("SYMBOL-UNIVERSAL", "constraint does not bar universal one-symbol-one-domain claims")

    # --- banned phrasing and real-sacred terms in exercise ----------------
    for s in iter_strings(ex, skip_key="forbidden_claims"):
        low = s.lower()
        for phrase in UNIVERSAL_PHRASES:
            if phrase in low:
                f.add("UNIVERSAL-PHRASE", f"text contains {phrase!r}: {s[:60]!r}")
        for term in SACRED_TERMS:
            for m in re.finditer(r"\b" + re.escape(term) + r"\b", s, re.IGNORECASE):
                if term.lower() == "bible" and s[max(0, m.start() - 6):m.start()].lower().endswith("world "):
                    continue
                f.add("SACRED-TERM", f"text contains {term!r}: {s[:60]!r}")

    # --- canon hygiene ----------------------------------------------------
    if doc.get("canon_status") != "non-canon" or ex.get("fiction_notice") is None:
        f.add("CANON-HYGIENE", "canon_status/fiction notice missing")
    for d in derivations:
        if not d.get("method_trace"):
            f.add("METHOD-TRACE", f"{d.get('id')} lacks method_trace")

    # --- report headings --------------------------------------------------
    if report_text is not None:
        for heading in (
            "## Commands",
            "## Design assumptions",
            "## Derivations",
            "## Source rechecks",
            "## Lore handoff limits",
        ):
            if heading not in report_text:
                f.add("REPORT-HEADING", f"report lacks {heading!r}")
        for phrase in UNIVERSAL_PHRASES:
            if phrase in report_text.lower():
                f.add("REPORT-UNIVERSAL", f"report contains {phrase!r}")

    return f, counts


def tamper_tests(doc):
    """Negative controls for the checker itself: each tamper must be detected."""
    cases = []

    t = copy.deepcopy(doc)
    t["exercise"]["mech_expectations"]["cases"][0]["cases"]["tapa"] = "tava"
    cases.append(("MECH-RECOMPUTE", t))

    t = copy.deepcopy(doc)
    t["exercise"]["derivations"][0].pop("negative_control")
    cases.append(("CONTROL-MISSING", t))

    t = copy.deepcopy(doc)
    t["exercise"]["symbol_readings"]["readings"] = t["exercise"]["symbol_readings"]["readings"][:1]
    cases.append(("SYMBOL-READINGS", t))

    t = copy.deepcopy(doc)
    t["exercise"]["era_staging"]["note"] = "the loop-and-notch always means a completed apprenticeship"
    cases.append(("UNIVERSAL-PHRASE", t))

    t = copy.deepcopy(doc)
    t["audits"][0]["source_excerpt"] = " ".join(["word"] * 41)
    cases.append(("AUDIT-EXCERPT-LONG", t))

    t = copy.deepcopy(doc)
    t["audits"][0]["verdict"] = "probably"
    cases.append(("AUDIT-VERDICT", t))

    t = copy.deepcopy(doc)
    t["audit_counts"]["verdict_supported"] = 99
    cases.append(("AUDIT-COUNT-MISMATCH", t))

    t = copy.deepcopy(doc)
    t["exercise"]["name_avoidance"]["distribution_test"]["public_roll_year_340"]["founder_designation"] = "har"
    cases.append(("NAME-AVOIDANCE", t))

    t = copy.deepcopy(doc)
    t["exercise"]["borrowed_garment_terms"]["terms"][4]["stratum"] = "some stratum"
    cases.append(("LOAN-STRATA", t))

    t = copy.deepcopy(doc)
    t["exercise"]["fiction_notice"] = None
    cases.append(("CANON-HYGIENE", t))

    failures = []
    for expect_id, tampered in cases:
        f, _ = run_checks(tampered)
        ids = {i for i, _ in f.items}
        if expect_id not in ids:
            failures.append(f"tamper {expect_id!r} not detected (ids seen: {sorted(ids)})")
    return len(cases), failures


EXIT_OK = 0
EXIT_FINDINGS = 1
EXIT_USAGE = 2
DEFAULT_EXERCISE = "examples/supplement-opencode-1/sound-change-vs-taboo.json"
DEFAULT_REPORT = "reports/supplement-opencode-1/32-craft-exercise.md"


class CliError(Exception):
    def __init__(self, diag_id, message):
        super().__init__(message)
        self.diag_id = diag_id


def resolve_repo_path(rel):
    if os.path.exists(rel):
        return rel
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cand = os.path.join(repo, rel)
    return cand if os.path.exists(cand) else rel


def read_json_file(path, open_id, utf8_id, json_id, shape_id):
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except OSError as exc:
        raise CliError(open_id, f"cannot read {path!r}: {exc.strerror or exc}") from exc
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise CliError(utf8_id, f"{path!r} is not valid UTF-8: {exc}") from exc
    try:
        doc = json.loads(text)
    except json.JSONDecodeError as exc:
        raise CliError(json_id, f"{path!r} is not valid JSON: {exc}") from exc
    if not isinstance(doc, dict):
        raise CliError(shape_id, f"{path!r} root must be a JSON object, got {type(doc).__name__}")
    return doc


def read_report_text(path):
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except OSError as exc:
        raise CliError("CRAFT-CLI-REPORT-OPEN", f"cannot read report {path!r}: {exc.strerror or exc}") from exc
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise CliError("CRAFT-CLI-REPORT-UTF8", f"report {path!r} is not valid UTF-8: {exc}") from exc


def require(cond, message):
    if not cond:
        raise CliError("CRAFT-CLI-SHAPE", message)


def is_str_or_absent(value):
    return value is None or isinstance(value, str)


def validate_shape(doc):
    """Reject, at the boundary, any shape a run_checks dereference would crash on."""
    require(isinstance(doc.get("exercise", {}), dict), "'exercise' must be a JSON object")
    counts = doc.get("audit_counts", {})
    require(isinstance(counts, dict), "'audit_counts' must be a JSON object")
    for k in ("verdict_supported", "verdict_unresolved", "verdict_contradicted"):
        require(isinstance(counts.get(k, 0), int), f"'audit_counts.{k}' must be a number")
    audits = doc.get("audits", [])
    require(isinstance(audits, list), "'audits' must be a JSON array")
    for i, a in enumerate(audits):
        require(isinstance(a, dict), f"'audits[{i}]' must be a JSON object")
        require(isinstance(a.get("source_excerpt", ""), str), f"'audits[{i}].source_excerpt' must be a string")
        require(isinstance(a.get("basis", ""), str), f"'audits[{i}].basis' must be a string")
    ex = doc.get("exercise", {})
    derivations = ex.get("derivations", [])
    require(isinstance(derivations, list), "'exercise.derivations' must be a JSON array")
    for i, d in enumerate(derivations):
        require(isinstance(d, dict), f"'exercise.derivations[{i}]' must be a JSON object")
    law_list = ex.get("law_list", {})
    require(isinstance(law_list, dict), "'exercise.law_list' must be a JSON object")
    order = law_list.get("order", [])
    require(isinstance(order, list), "'exercise.law_list.order' must be a JSON array")
    require(all(isinstance(n, str) for n in order), "'exercise.law_list.order' entries must be strings")
    mech = ex.get("mech_expectations", {})
    require(isinstance(mech, dict), "'exercise.mech_expectations' must be a JSON object")
    mech_cases = mech.get("cases", [])
    require(isinstance(mech_cases, list), "'exercise.mech_expectations.cases' must be a JSON array")
    for i, case in enumerate(mech_cases):
        require(isinstance(case, dict), f"'exercise.mech_expectations.cases[{i}]' must be a JSON object")
        words = case.get("cases", {})
        require(isinstance(words, dict), f"'exercise.mech_expectations.cases[{i}].cases' must be a JSON object")
        require(all(isinstance(w, str) for w in words), f"'exercise.mech_expectations.cases[{i}].cases' keys must be strings")
    na = ex.get("name_avoidance", {})
    require(isinstance(na, dict), "'exercise.name_avoidance' must be a JSON object")
    dt = na.get("distribution_test", {})
    require(isinstance(dt, dict), "'exercise.name_avoidance.distribution_test' must be a JSON object")
    require(isinstance(dt.get("public_roll_year_340", {}), dict),
            "'exercise.name_avoidance.distribution_test.public_roll_year_340' must be a JSON object")
    bgt = ex.get("borrowed_garment_terms", {})
    require(isinstance(bgt, dict), "'exercise.borrowed_garment_terms' must be a JSON object")
    terms = bgt.get("terms", [])
    require(isinstance(terms, list), "'exercise.borrowed_garment_terms.terms' must be a JSON array")
    for i, t in enumerate(terms):
        require(isinstance(t, dict), f"'exercise.borrowed_garment_terms.terms[{i}]' must be a JSON object")
        require(is_str_or_absent(t.get("term")), f"'exercise.borrowed_garment_terms.terms[{i}].term' must be a string")
        require(isinstance(t.get("stratum", ""), str), f"'exercise.borrowed_garment_terms.terms[{i}].stratum' must be a string")
    sr = ex.get("symbol_readings", {})
    require(isinstance(sr, dict), "'exercise.symbol_readings' must be a JSON object")
    readings = sr.get("readings", [])
    require(isinstance(readings, list), "'exercise.symbol_readings.readings' must be a JSON array")
    for i, r in enumerate(readings):
        require(isinstance(r, dict), f"'exercise.symbol_readings.readings[{i}]' must be a JSON object")
        require(is_str_or_absent(r.get("reading")), f"'exercise.symbol_readings.readings[{i}].reading' must be a string")
        require(is_str_or_absent(r.get("audience")), f"'exercise.symbol_readings.readings[{i}].audience' must be a string")
    require(isinstance(sr.get("constraint", ""), str), "'exercise.symbol_readings.constraint' must be a string")
    require(isinstance(sr.get("motif", ""), str), "'exercise.symbol_readings.motif' must be a string")


def require_selftest_target(doc):
    """The ten-tamper battery indexes fixed slots; the target must carry them."""
    msg = "selftest target lacks a slot the tamper battery mutates"
    ex = doc.get("exercise", {})
    require(doc.get("audits"), msg + ": audits[0]")
    require("audit_counts" in doc, msg + ": audit_counts")
    require(bool(ex.get("derivations", [])), msg + ": derivations[0]")
    require("negative_control" in ex["derivations"][0], msg + ": derivations[0].negative_control")
    cases = ex.get("mech_expectations", {}).get("cases", [])
    require(bool(cases) and isinstance(cases[0].get("cases"), dict), msg + ": mech_expectations.cases[0].cases")
    require(isinstance(ex.get("symbol_readings", {}).get("readings"), list), msg + ": symbol_readings.readings")
    require(isinstance(ex.get("era_staging"), dict), msg + ": exercise.era_staging")
    require(len(ex.get("borrowed_garment_terms", {}).get("terms", [])) >= 5, msg + ": borrowed_garment_terms.terms[4]")
    roll = ex.get("name_avoidance", {}).get("distribution_test", {}).get("public_roll_year_340", {})
    require(isinstance(roll, dict), msg + ": name_avoidance.distribution_test.public_roll_year_340")


def parse_args(argv):
    path = None
    counts = False
    report = None
    i = 1
    while i < len(argv):
        tok = argv[i]
        if tok == "--counts":
            counts = True
        elif tok == "--report":
            if i + 1 >= len(argv) or argv[i + 1].startswith("-"):
                raise CliError("CRAFT-CLI-REPORT-VALUE", "--report needs a report file path")
            report = argv[i + 1]
            i += 1
        elif tok.startswith("-") and tok != "-":
            raise CliError("CRAFT-CLI-USAGE", f"unknown option {tok!r}")
        elif path is None:
            path = tok
        else:
            raise CliError("CRAFT-CLI-USAGE", f"unexpected extra argument {tok!r}")
        i += 1
    if path is None:
        raise CliError("CRAFT-CLI-USAGE", "expected <exercise.json> argument")
    return path, counts, report


def run_cli_selftest(doc):
    """Drive this script as a real subprocess over isolated fixtures."""
    script = os.path.abspath(__file__)
    repo = os.path.dirname(os.path.dirname(script))
    exercise = os.path.join(repo, DEFAULT_EXERCISE)
    report = os.path.join(repo, DEFAULT_REPORT)
    tmp = tempfile.mkdtemp(prefix="craft-cli-selftest-")
    try:
        bad_json = os.path.join(tmp, "malformed.json")
        with open(bad_json, "wb") as fh:
            fh.write(b'{"audits": [')
        bad_utf8 = os.path.join(tmp, "binary.json")
        with open(bad_utf8, "wb") as fh:
            fh.write(b"\xff\xfe\x00not-utf8")
        array_root = os.path.join(tmp, "array-root.json")
        with open(array_root, "wb") as fh:
            fh.write(b"[1, 2]")
        shape_audits_scalar = os.path.join(tmp, "shape-audits-scalar.json")
        with open(shape_audits_scalar, "w", encoding="utf-8") as fh:
            json.dump({"audits": [3]}, fh)
        shape_audits_object = os.path.join(tmp, "shape-audits-object.json")
        with open(shape_audits_object, "w", encoding="utf-8") as fh:
            json.dump({"audits": {"x": 1}}, fh)
        shape_exercise_container = os.path.join(tmp, "shape-exercise-container.json")
        with open(shape_exercise_container, "w", encoding="utf-8") as fh:
            json.dump({"exercise": [1]}, fh)
        missing = os.path.join(tmp, "absent.json")
        selftest_thin = os.path.join(tmp, "selftest-thin.json")
        with open(selftest_thin, "w", encoding="utf-8") as fh:
            json.dump({"audits": []}, fh)
        tampered = os.path.join(tmp, "tampered.json")
        t = copy.deepcopy(doc)
        t["exercise"]["derivations"][0].pop("negative_control")
        with open(tampered, "w", encoding="utf-8") as fh:
            json.dump(t, fh)

        cases = [
            ("positive-run", [exercise], repo, 0, "OK all checks passed", False),
            ("positive-counts", [exercise, "--counts"], repo, 0, '"total"', False),
            ("positive-report", [exercise, "--report", report], repo, 0, "OK all checks passed", False),
            ("positive-other-cwd", [exercise], tmp, 0, "OK all checks passed", False),
            ("missing-argument", [], repo, 2, "CRAFT-CLI-USAGE", True),
            ("missing-file", [missing], repo, 2, "CRAFT-CLI-NOT-FOUND", True),
            ("malformed-json", [bad_json], repo, 2, "CRAFT-CLI-JSON", True),
            ("non-utf8", [bad_utf8], repo, 2, "CRAFT-CLI-UTF8", True),
            ("wrong-root-shape", [array_root], repo, 2, "CRAFT-CLI-SHAPE", True),
            ("missing-report-value", [exercise, "--report"], repo, 2, "CRAFT-CLI-REPORT-VALUE", True),
            ("report-flag-value", [exercise, "--report", "--counts"], repo, 2, "CRAFT-CLI-REPORT-VALUE", True),
            ("shape-audits-scalar", [shape_audits_scalar], repo, 2, "CRAFT-CLI-SHAPE", True),
            ("shape-audits-object", [shape_audits_object], repo, 2, "CRAFT-CLI-SHAPE", True),
            ("shape-exercise-container", [shape_exercise_container], repo, 2, "CRAFT-CLI-SHAPE", True),
            ("selftest-conflicting-mode", ["--selftest", exercise, "--counts"], repo, 2, "CRAFT-CLI-USAGE", True),
            ("selftest-positional-before", [exercise, "--selftest"], repo, 2, "CRAFT-CLI-USAGE", True),
            ("selftest-thin-target", ["--selftest", selftest_thin], repo, 2, "CRAFT-CLI-SHAPE", True),
            ("finding-exit1", [tampered], repo, 1, "FAIL CONTROL-MISSING", False),
        ]
        failures = []
        for name, args, cwd, want_code, want_token, block_traceback in cases:
            proc = subprocess.run(
                [sys.executable, script] + args, capture_output=True, text=True, cwd=cwd
            )
            blob = proc.stdout + proc.stderr
            if proc.returncode != want_code:
                tail = proc.stderr.strip().splitlines()[-1] if proc.stderr.strip() else ""
                failures.append(f"{name}: exit {proc.returncode}, want {want_code} ({tail!r})")
            elif want_token not in blob:
                failures.append(f"{name}: exit {proc.returncode} but {want_token!r} absent")
            elif block_traceback and "Traceback" in blob:
                failures.append(f"{name}: traceback leaked")
        return len(cases), failures
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def run_selftest(argv):
    try:
        idx = argv.index("--selftest")
        if argv[1:idx]:
            raise CliError("CRAFT-CLI-USAGE", f"unexpected argument before --selftest: {argv[1]!r}")
        target = None
        for tok in argv[idx + 1:]:
            if target is None and not tok.startswith("-"):
                target = tok
            else:
                raise CliError(
                    "CRAFT-CLI-USAGE",
                    f"--selftest takes at most one optional exercise path after --selftest and no other tokens, got {tok!r}",
                )
        path = target if target is not None else resolve_repo_path(DEFAULT_EXERCISE)
        doc = read_json_file(
            path, "CRAFT-CLI-NOT-FOUND", "CRAFT-CLI-UTF8", "CRAFT-CLI-JSON", "CRAFT-CLI-SHAPE"
        )
        validate_shape(doc)
        require_selftest_target(doc)
    except CliError as exc:
        print(f"CLI-ERROR {exc.diag_id}: {exc}", file=sys.stderr)
        return EXIT_USAGE

    n, failures = tamper_tests(doc)
    if failures:
        for x in failures:
            print("SELFTEST FAIL", x)
    else:
        print(f"SELFTEST OK {n}/{n} tamper cases detected")

    cli_n, cli_failures = run_cli_selftest(doc)
    if cli_failures:
        for x in cli_failures:
            print("CLI-SELFTEST FAIL", x)
    else:
        print(f"CLI-SELFTEST OK {cli_n}/{cli_n} cases passed")

    return EXIT_OK if not failures and not cli_failures else EXIT_FINDINGS


def main(argv):
    if "--selftest" in argv:
        return run_selftest(argv)
    try:
        path, counts_flag, report_path = parse_args(argv)
        doc = read_json_file(
            path, "CRAFT-CLI-NOT-FOUND", "CRAFT-CLI-UTF8", "CRAFT-CLI-JSON", "CRAFT-CLI-SHAPE"
        )
        validate_shape(doc)
        report_text = read_report_text(report_path) if report_path is not None else None
    except CliError as exc:
        print(f"CLI-ERROR {exc.diag_id}: {exc}", file=sys.stderr)
        return EXIT_USAGE

    f, counts = run_checks(doc, report_text)

    if counts_flag:
        print(json.dumps(counts, indent=2, sort_keys=True))
        return EXIT_OK if not f.items else EXIT_FINDINGS

    if f.items:
        for fid, detail in f.items:
            print(f"FAIL {fid}: {detail}")
        print(f"{len(f.items)} finding(s)")
        return EXIT_FINDINGS

    n_checks = (
        len(doc.get("audits", []))
        + len(doc.get("exercise", {}).get("mech_expectations", {}).get("cases", []))
        + len(doc.get("exercise", {}).get("derivations", []))
        + 10
    )
    print(f"OK all checks passed (audits={len(doc.get('audits', []))}, "
          f"mech_cases={len(doc.get('exercise', {}).get('mech_expectations', {}).get('cases', []))}, "
          f"derivations={len(doc.get('exercise', {}).get('derivations', []))}, "
          f"approx_checks_runner={n_checks})")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main(sys.argv))
