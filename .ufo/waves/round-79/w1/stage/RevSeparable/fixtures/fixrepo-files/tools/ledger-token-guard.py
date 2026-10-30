#!/usr/bin/env python3
"""FIXTURE ledger-token guard (toy model of the round-79 O claim's guard).

Real contract being modeled (round-79 CLAIMS-DRAFT, O): a bounded guard over
calibration-record ledger pairs. It re-runs approved read-only observations
against immutable committed bytes and refuses:
  * observed_at_base differing from the actual observation (the R77 D01-D10
    fabricated-base-observation class, grounded in R78-M1), and
  * stated_token equal to the actual observation (the R77 D11 green-pair /
    no-op class).
This toy prints the two refusals for the fixture's red pair and accepts the
green pair. It is not the real r79 guard.
"""
import json
import sys

def check_pair(pair, observe):
    stated = pair["stated_token"]
    observed_at_base = pair["observed_at_base"]
    actual = observe(pair)
    if observed_at_base != actual:
        return f"REJECT observed_at_base={observed_at_base!r} != actual={actual!r}"
    if stated == actual:
        return f"REJECT stated_token == actual observation {actual!r} (no-op pair)"
    return None

def main(path):
    with open(path, encoding="utf-8") as fh:
        pairs = json.load(fh)["pairs"]
    observe = lambda p: p["ACTUAL_TOKEN"]  # toy: real guard re-runs the pinned observation
    bad = []
    for p in pairs:
        verdict = check_pair(p, observe)
        if verdict:
            bad.append(f"{p['id']}: {verdict}")
    if bad:
        print("GUARD: FAIL")
        for b in bad:
            print("  " + b)
        return 1
    print("GUARD: PASS pairs all green")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
