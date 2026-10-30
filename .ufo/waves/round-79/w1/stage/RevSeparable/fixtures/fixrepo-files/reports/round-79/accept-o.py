#!/usr/bin/env python3
"""FIXTURE counter for RevSeparable's round-79 O/Ca separability model.

This is a toy-scale model of the round-79 CLAIMS-DRAFT contracts, NOT the real
r79 counters. It exists so the only-claim counterfactual matrix and the
check-claim-separability.py legs can be executed against real evidence bytes.

O contract modeled (draft): a ledger-token guard for calibration records;
refuses mutable revisions / constant printers; rejects observed_at_base
differing from the actual observation; rejects stated_token equal to the
actual observation. Legs here: GUARD, S897ROW, REDGREEN, SELFTEST.

Refusals (QUALITY 25(a) shape): non-40-hex lands/freeze; frozen claims.json
unreadable; LEGCOUNT frozen legs != own leg table; lands equals frozen base;
freeze not an ancestor of lands on the lands first-parent chain.
Do-nothing: lands == freeze is graded, never passed.
"""
import argparse
import json
import re
import subprocess
import sys

LEGS = ["GUARD", "S897ROW", "REDGREEN", "SELFTEST"]

def die_refuse(msg):
    print(f"FIXTURE-O: FAIL legs=0/{len(LEGS)} (refused: {msg})")
    return 2

def show(root, rev, path):
    r = subprocess.run(["git", "-C", root, "show", f"{rev}:{path}"],
                       capture_output=True, text=True)
    return r.returncode, r.stdout

def ancestor(root, a, b):
    r = subprocess.run(["git", "-C", root, "merge-base", "--is-ancestor", a, b])
    return r.returncode == 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--lands", default="overlay")
    ap.add_argument("--freeze", default="overlay")
    ap.add_argument("--work", default="/tmp")
    ap.add_argument("--overlay", action="store_true",
                    help="grade the working tree at cwd (separability-checker overlay mode)")
    a = ap.parse_args()

    if a.overlay:
        import pathlib
        legs = []
        g = pathlib.Path("tools/ledger-token-guard.py")
        legs.append(("GUARD", g.is_file() and "observed_at_base" in g.read_text()
                     and "stated_token" in g.read_text()))
        reg = pathlib.Path("corpus/SOURCES.md")
        legs.append(("S897ROW", reg.is_file() and "| S897 |" in reg.read_text()))
        rg = pathlib.Path("reports/round-79/telemetry/guard-redgreen.txt")
        legs.append(("REDGREEN", rg.is_file() and "RED observed_at_base" in rg.read_text()))
        st = pathlib.Path("reports/round-79/telemetry/selftest-o.txt")
        legs.append(("SELFTEST", st.is_file() and "selftest: 2/2" in st.read_text()))
        npass = sum(1 for _, ok in legs if ok)
        for name, ok in legs:
            print(f"LEG {'PASS' if ok else 'FAIL'} {name}")
        print(f"FIXTURE-O: {'PASS' if npass == len(LEGS) else 'FAIL'} legs={npass}/{len(LEGS)}")
        return 0 if npass == len(LEGS) else 1

    for rev in (a.lands, a.freeze):
        if not re.fullmatch(r"[0-9a-f]{40}", rev):
            return die_refuse("non-40-hex revision")
    rc, cfg = show(a.root, a.freeze, "reports/round-79/claims.json")
    if rc != 0:
        return die_refuse("frozen claims.json unreadable")
    cfg = json.loads(cfg)
    frozen_legs = cfg["legs"]["O"]
    if frozen_legs != LEGS:
        return die_refuse(f"LEGCOUNT frozen={frozen_legs} own={LEGS}")
    if a.lands == cfg["base"]:
        return die_refuse("lands equals frozen base")
    if not ancestor(a.root, a.freeze, a.lands):
        return die_refuse("freeze not ancestor of lands")

    results = []
    rc, guard = show(a.root, a.lands, "tools/ledger-token-guard.py")
    ok = rc == 0 and "observed_at_base" in guard and "stated_token" in guard \
        and "ACTUAL_TOKEN" in guard
    results.append(("GUARD", ok))
    rc, reg = show(a.root, a.lands, "corpus/SOURCES.md")
    ok = rc == 0 and re.search(r"\| S897 \|", reg) is not None and "own-work" in reg
    results.append(("S897ROW", ok))
    rc, rg = show(a.root, a.lands, "reports/round-79/telemetry/guard-redgreen.txt")
    ok = rc == 0 and "RED observed_at_base" in rg and "GREEN stated_token" in rg
    results.append(("REDGREEN", ok))
    rc, st = show(a.root, a.lands, "reports/round-79/telemetry/selftest-o.txt")
    ok = rc == 0 and "selftest: 2/2" in st
    results.append(("SELFTEST", ok))

    npass = sum(1 for _, ok in results if ok)
    for name, ok in results:
        print(f"LEG {'PASS' if ok else 'FAIL'} {name}")
    print(f"FIXTURE-O: {'PASS' if npass == len(LEGS) else 'FAIL'} legs={npass}/{len(LEGS)}")
    return 0 if npass == len(LEGS) else 1

if __name__ == "__main__":
    sys.exit(main())
