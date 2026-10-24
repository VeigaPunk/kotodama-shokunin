#!/usr/bin/env python3
r"""Round-69 operability capability: lane-shaped supersession-settlement fixture harness.

Contract
--------
Builds a synthetic *lane-shaped* registry (an 11-column ``## Registry`` table
inside a ``corpus/SOURCES.md`` that also carries ``## Paths`` and ``## Search
log`` sections), runs the lane's settlement checker against it and asserts the
settlement verdict. Three cases, all required:

* ``green``    — the used-by knowledge file EXISTS: the checker must report
  ``pending=0 missing_paths=0`` and exit 0.
* ``negative`` — the used-by knowledge file is ABSENT (the round-68 counter
  fixture defect, R68-M1: the fixture never created ``corpus/knowledge/a.md``,
  so the scan answered ``missing_paths=1`` in every run): the checker must
  report ``missing_paths=1``. This case is what the lane never had.
* ``pending``  — the correction chain is unsettled: the checker must report
  ``pending=1`` and exit 1.

Usage
-----
  --selftest        run the three fixture cases; print one PASS line per case
                    and ``FIXTURE: 3/3``; exit 0 iff all three hold.
  --root DIR        run the three fixture cases AND scan DIR's own
                    ``corpus/SOURCES.md``; print ``LANE: pending=N
                    missing_paths=M``; exit 0 iff the three cases hold and the
                    scanned root has no pending chain and no missing used-by
                    path.
  --checker PATH    override the settlement checker to exercise (default:
                    ``tools/check-supersession-settlement.py`` beside this
                    file).

Exit codes: 0 clean · 1 failure · 2 usage/env.
This tool reads and builds temporary fixtures only; it never mutates the lane
tree and never touches the network.
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)

FIXTURE_REGISTRY = """# SOURCES — where the fixture lane learns

A lane-shaped registry: the same section order and the same 11-column table
as the live `corpus/SOURCES.md`, so the checker is exercised on the shape it
actually reads.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | Fixture base source — https://example.invalid/base | docs | B | the base row's scope | §1 | the base claim | {s001} | 2026-10-24 | 90d | — |
| S002 | Fixture successor source — https://example.invalid/next | docs | A | the successor row's scope | §1 | supersedes S001 — the correction that replaces the base claim | mined | 2026-10-24 | 90d | corpus/knowledge/a.md |

## Paths

- fixture — S001 → S002: the correction replaces the base claim, so the
  successor is read first.

## Search log

- 2026-10-24 — fixture lane; no network; the two rows are synthetic.
"""

USEDBY_FILE = "cites S002 now\n"

SUMMARY_RE = re.compile(
    r"SETTLEMENT:\s*pending=(\d+)\s+chains=(\d+)\s+usedby_paths=(\d+)\s+"
    r"missing_paths=(\d+)")


def write_fixture(root, *, create_usedby, unsettled):
    """Materialise one fixture lane under *root*."""
    s001 = "mined" if unsettled else "queued"
    reg = os.path.join(root, "corpus", "SOURCES.md")
    os.makedirs(os.path.dirname(reg), exist_ok=True)
    with open(reg, "w", encoding="utf-8") as fh:
        fh.write(FIXTURE_REGISTRY.format(s001=s001))
    if create_usedby:
        kb = os.path.join(root, "corpus", "knowledge", "a.md")
        os.makedirs(os.path.dirname(kb), exist_ok=True)
        with open(kb, "w", encoding="utf-8") as fh:
            fh.write(USEDBY_FILE)


def run_checker(checker, root):
    """Run the settlement checker on *root*; return (rc, stdout)."""
    proc = subprocess.run(
        [sys.executable, "-B", checker, "--scan", "--root", root],
        capture_output=True, text=True, check=False)
    return proc.returncode, proc.stdout


def parse_summary(out):
    m = SUMMARY_RE.search(out)
    if not m:
        return None
    return {"pending": int(m.group(1)), "chains": int(m.group(2)),
            "usedby_paths": int(m.group(3)),
            "missing_paths": int(m.group(4))}


def check_cases(checker):
    """Run the three fixture cases; return a list of (name, ok, detail)."""
    results = []
    with tempfile.TemporaryDirectory(prefix="settlement-fixture-") as td:
        green = os.path.join(td, "green")
        write_fixture(green, create_usedby=True, unsettled=False)
        rc, out = run_checker(checker, green)
        s = parse_summary(out)
        ok = rc == 0 and s is not None and s["pending"] == 0 \
            and s["missing_paths"] == 0
        results.append(("green", ok,
                        "rc=%d pending=%s missing_paths=%s" % (
                            rc, s["pending"] if s else "?",
                            s["missing_paths"] if s else "?")))

        neg = os.path.join(td, "negative")
        write_fixture(neg, create_usedby=False, unsettled=False)
        rc, out = run_checker(checker, neg)
        s = parse_summary(out)
        ok = s is not None and s["pending"] == 0 and s["missing_paths"] == 1
        results.append(("negative", ok,
                        "rc=%d pending=%s missing_paths=%s" % (
                            rc, s["pending"] if s else "?",
                            s["missing_paths"] if s else "?")))

        pend = os.path.join(td, "pending")
        write_fixture(pend, create_usedby=True, unsettled=True)
        rc, out = run_checker(checker, pend)
        s = parse_summary(out)
        ok = rc == 1 and s is not None and s["pending"] == 1
        results.append(("pending", ok,
                        "rc=%d pending=%s missing_paths=%s" % (
                            rc, s["pending"] if s else "?",
                            s["missing_paths"] if s else "?")))
    return results


def lane_summary(checker, root):
    rc, out = run_checker(checker, root)
    s = parse_summary(out)
    if s is None:
        return None, rc, out
    return s, rc, out


def main():
    ap = argparse.ArgumentParser(
        description="lane-shaped supersession-settlement fixture harness")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--root", default=None,
                    help="lane root to scan in addition to the fixtures")
    ap.add_argument("--checker", default=None)
    args = ap.parse_args()
    checker = args.checker or os.path.join(
        LANE, "tools", "check-supersession-settlement.py")
    if not os.path.exists(checker):
        print(f"CHECKER_MISSING {checker}")
        return 2
    results = check_cases(checker)
    for name, ok, detail in results:
        print(f"{'PASS' if ok else 'FAIL'} fixture-{name} {detail}")
    passed = sum(1 for _, ok, _ in results if ok)
    print(f"FIXTURE: {passed}/{len(results)}")
    rc = 0 if passed == len(results) else 1
    if args.root:
        root = os.path.abspath(args.root)
        s, scan_rc, out = lane_summary(checker, root)
        if s is None:
            print(f"LANE_ERROR rc={scan_rc}")
            return 2
        print("LANE: pending=%d missing_paths=%d" % (
            s["pending"], s["missing_paths"]))
        if s["pending"] or s["missing_paths"]:
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
