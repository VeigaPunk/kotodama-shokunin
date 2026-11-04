#!/usr/bin/env python3
"""DRAFT for QUALITY 34 (not filed; L1 decides integration). Read-only.

Usage: python3 -B check34-draft.py <round-87 constant-pass.json> <round-87 counter-selftest.json>

Prints one line `COUNTERFEIT-KILL: PASS|FAIL ...` and exits 0 only when the
committed non-reader control (`constant-pass`) and the blanket-refusal control
(`constant-reject`) are both scored below the battery total. A control that
reaches the total is a counter red, whatever the claim's own verdict says.
"""
import json
import sys
from pathlib import Path


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("COUNTERFEIT-KILL: FAIL usage", file=sys.stderr)
        return 2
    run = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    body = json.loads(run["stdout"])
    passed, total = body["passed"], body["total"]
    run_ok = run.get("rc") != 0 and passed < total

    selftest = json.loads(Path(argv[2]).read_text(encoding="utf-8"))
    scores = {c["case"]: c["observed_passed"]
              for c in json.loads(selftest["stdout"])["checks"]}
    refuse = scores.get("constant-reject")
    refuse_ok = refuse is not None and refuse < total
    ok = run_ok and scores.get("constant-pass") is not None and refuse_ok
    print(f"COUNTERFEIT-KILL: {'PASS' if ok else 'FAIL'} "
          f"non-reader={passed}/{total} rc={run.get('rc')} "
          f"blanket-refusal={refuse}/{total}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
