#!/usr/bin/env python3
"""Round-79 junk control: a constant printer masquerading as the ledger-token
guard. It accepts the same --ledger/--repo/--base/--work arguments, never
opens the repository, and for every pair prints `observed=<stated_token>` -
an echo of the claim's own stated text dressed up as an observation. It then
prints a PASS line and exits 0 regardless of what the committed bytes say.

The NOSTUB leg of accept-o.py runs this stub on a fresh-nonce ledger: the
stub dutifully echoes the stated nonce as its "observation" while the real
guard reports the independently observed token. That is the contrast the
oracle leg exists to measure: echoing stated values is not observing.

Deliberately wrong. Do not ship as the real guard.
"""

import argparse
import json
import re
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger")
    ap.add_argument("--repo")
    ap.add_argument("--base")
    ap.add_argument("--work")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        print("SELFTEST: PASS")
        return 0
    doc = json.load(open(args.ledger))
    for pair in doc.get("pairs", []):
        m = re.search(pair.get("stated_parse", r"(.*)"),
                      pair.get("stated_text", ""))
        token = m.group(1) if m and m.groups() else (m.group(0) if m else "?")
        print("pair %s: ok observed=%s" % (pair.get("id", "?"), token))
    print("LEDGER-TOKEN-GUARD: PASS pairs=%d" % len(doc.get("pairs", [])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
