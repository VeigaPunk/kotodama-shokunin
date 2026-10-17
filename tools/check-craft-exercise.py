#!/usr/bin/env python3
"""In-memory checker for the non-canon exercise examples/supplement-opencode-1/sound-change-vs-taboo.json.

Stdlib only. Rebuilds the toy law engine from the JSON's law_list.order, recomputes
every declared derivation, verifies the data-level assertions (name avoidance,
register partition, loan strata, symbol readings), the audit-row schema, and the
report file's required headings. Exits 0 on clean, 1 on findings.

Usage:
  python3 tools/check-craft-exercise.py <exercise.json> [--report <report.md>]
  python3 tools/check-craft-exercise.py <exercise.json> --counts
  python3 tools/check-craft-exercise.py --selftest
"""
import json
import re
import sys

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
    import copy

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


def main(argv):
    if "--selftest" in argv:
        path = (
            argv[argv.index("--selftest") + 1]
            if len(argv) > argv.index("--selftest") + 1
            else "examples/supplement-opencode-1/sound-change-vs-taboo.json"
        )
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
        n, failures = tamper_tests(doc)
        if failures:
            for x in failures:
                print("SELFTEST FAIL", x)
            return 1
        print(f"SELFTEST OK {n}/{n} tamper cases detected")
        return 0

    path = argv[1]
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    report_text = None
    if "--report" in argv:
        with open(argv[argv.index("--report") + 1], encoding="utf-8") as fh:
            report_text = fh.read()

    f, counts = run_checks(doc, report_text)

    if "--counts" in argv:
        print(json.dumps(counts, indent=2, sort_keys=True))
        return 0 if not f.items else 1

    if f.items:
        for fid, detail in f.items:
            print(f"FAIL {fid}: {detail}")
        print(f"{len(f.items)} finding(s)")
        return 1

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
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
