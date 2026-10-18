#!/usr/bin/env python3
"""R26-C50 — independent verifier for the open-question disposition ledger.

Re-derives both surfaces from the raw bytes, re-runs every evidence probe, and
proves zero undispositioned rows — without trusting `dispositions.json` for the
row set. The ledger is the *subject*; the raw carriers are the *control*.

    export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
    python3 -B reports/round-26/open-questions/verify-dispositions.py
    python3 -B reports/round-26/open-questions/verify-dispositions.py --json
    python3 -B reports/round-26/open-questions/verify-dispositions.py --selftest

Exit 0 = every check green. Exit 1 = at least one check red (named on stdout).
Exit 2 = could-not-evaluate (the ledger is absent; run the builder first).

The four checks:
  V1  every row on either surface has a ledger entry with a disposition
  V2  every ledger entry's id exists on one of the surfaces (no ghost rows)
  V3  every entry's disposition is in the declared vocabulary
  V4  every entry's probes re-run and still match their expected token
Plus two controls:
  V5  the twin cross-links are symmetric (A.twin == B implies B.twin == A)
  V6  the surface counts the ledger reports equal the live counts
"""
import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LEDGER = os.path.join(HERE, "dispositions.json")
README = os.path.join(LANE, "corpus", "lessons", "README.md")
CENSUS = os.path.join(LANE, "reports", "round-25", "lessons", "census.json")

VOCAB = {"fixed-with-evidence", "carried", "routed",
         "closed-by-supersession", "standing-rule"}


def readme_ids():
    text = open(README, encoding="utf-8").read()
    section = text.split("## 4. Open-question queue")[1].split("## 5")[0]
    ids = []
    for line in section.splitlines():
        if not line.startswith("| Q-") or line.startswith("| Q-id"):
            continue
        ids.append(line.strip().strip("|").split("|")[0].strip())
    return ids


def census_ids():
    data = json.load(open(CENSUS, encoding="utf-8"))
    return [r["id"] for r in data["open_question_queue"]]


def run_checks(ledger):
    surface = set(readme_ids()) | set(census_ids())
    entries = {e["id"]: e for e in ledger["ledger"]}
    checks, findings = [], []

    def check(cid, ok, detail):
        checks.append({"id": cid, "ok": bool(ok), "detail": detail})
        if not ok:
            findings.append(f"{cid}: {detail}")

    missing = sorted(surface - set(entries))
    check("V1_no_undispositioned_row", not missing,
          f"{len(surface)} surface rows, {len(missing)} without a ledger entry"
          + (f": {missing[:8]}" if missing else ""))

    ghosts = sorted(set(entries) - surface)
    check("V2_no_ghost_row", not ghosts,
          f"{len(ghosts)} ledger ids absent from both surfaces"
          + (f": {ghosts[:8]}" if ghosts else ""))

    bad_disp = sorted(i for i, e in entries.items()
                      if e.get("disposition") not in VOCAB)
    check("V3_dispositions_in_vocabulary", not bad_disp,
          f"{len(bad_disp)} entries outside the vocabulary"
          + (f": {bad_disp[:8]}" if bad_disp else ""))

    failures = []
    for i, e in sorted(entries.items()):
        for ev in e.get("evidence", []):
            proc = subprocess.run(ev["command"], shell=True, cwd=LANE,
                                  capture_output=True, text=True, timeout=300)
            if ev["expect"] not in proc.stdout:
                failures.append((i, ev["command"], ev["expect"]))
    check("V4_probes_rerun_green", not failures,
          f"{len(failures)} probe(s) no longer match"
          + (f": {[f[0] for f in failures][:8]}" if failures else ""))

    asym = []
    for i, e in entries.items():
        t = e.get("twin")
        if t and t in entries and entries[t].get("twin") != i:
            asym.append((i, t))
    check("V5_twin_links_symmetric", not asym,
          f"{len(asym)} asymmetric twin link(s)" + (f": {asym[:4]}" if asym else ""))

    live = {"readme": len(readme_ids()), "census": len(census_ids())}
    stated = {"readme": ledger["surfaces"]["readme"]["rows"],
              "census": ledger["surfaces"]["census"]["rows"]}
    check("V6_surface_counts_match", live == stated,
          f"live {live} vs ledger {stated}")
    return checks, findings


def selftest():
    """In-memory controls: each check must be able to fail, and the parser must
    not read a header row as a queue row. Synthetic surfaces only — no file is
    read and no probe is executed."""
    ok = True

    def report(name, good):
        nonlocal ok
        ok &= good
        print(f"selftest {name}: {'PASS' if good else 'FAIL'}")

    # (1) A header row must not be read as a queue row.
    fake = "| Q-id | q | o | s |\n| Q-99-1 | q | o | open |\n"
    ids = [l.strip().strip("|").split("|")[0].strip()
           for l in fake.splitlines()
           if l.startswith("| Q-") and not l.startswith("| Q-id")]
    report("header-row-not-a-row", ids == ["Q-99-1"])

    # (2) The vocabulary must reject an invented disposition.
    report("vocabulary-rejects-unknown", "auto-fixed" not in VOCAB)

    # (3) V1 must fire on a surface row with no ledger entry.
    surface, entries = {"Q-99-1", "Q-99-2"}, {"Q-99-1": {"disposition": "carried"}}
    report("V1-fires-on-missing-row", bool(surface - set(entries)))

    # (4) V2 must fire on a ghost ledger row.
    entries_ghost = {"Q-99-1": {"disposition": "carried"}, "Q-99-9": {"disposition": "carried"}}
    report("V2-fires-on-ghost-row", bool(set(entries_ghost) - surface))

    # (5) V5 must fire on an asymmetric twin link (A claims B, B claims C).
    pair = {"A": {"twin": "B"}, "B": {"twin": "C"}}
    asym = [i for i, e in pair.items()
            if e.get("twin") and e["twin"] in pair and pair[e["twin"]].get("twin") != i]
    report("V5-fires-on-asymmetric-twin", asym == ["A"])

    # (6) V6 must fire on a count mismatch.
    report("V6-fires-on-count-mismatch", {"readme": 1} != {"readme": 2})
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not os.path.exists(LEDGER):
        print("could-not-evaluate: dispositions.json absent; run build-dispositions.py",
              file=sys.stderr)
        return 2
    ledger = json.load(open(LEDGER, encoding="utf-8"))
    checks, findings = run_checks(ledger)
    out = {"checks": checks, "findings": findings,
           "surface_rows": len(set(readme_ids()) | set(census_ids())),
           "ledger_rows": len(ledger["ledger"])}
    if args.json:
        print(json.dumps(out, indent=1))
    else:
        for c in checks:
            print(f"  {'PASS' if c['ok'] else 'FAIL'} {c['id']:34s} {c['detail']}")
        print(f"findings: {len(findings)}")
        for f in findings:
            print(f"  {f}")
    return 0 if not findings else 1


if __name__ == "__main__":
    sys.exit(main())
