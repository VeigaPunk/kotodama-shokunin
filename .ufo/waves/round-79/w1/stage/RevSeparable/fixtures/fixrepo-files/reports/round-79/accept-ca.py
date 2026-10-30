#!/usr/bin/env python3
"""FIXTURE counter for RevSeparable's round-79 O/Ca separability model — Ca side.

Models the round-79 Ca draft contract at toy scale over REAL r78 evidence bytes
copied into this fixture (receipt sha256 05b5011a..., registry with S884 row).

Contract modeled: one recorded mismatch — r78 census-end.txt's S884 used-by
token differs from the registry at its recorded revision. Correction appends
{original receipt digest, measured revision, old token, actual token} without
rewriting the historical receipt. This counter re-derives the mismatch at any
lands and fails while the correction is absent/unresolved.

Constants come from the FROZEN claims.json (QUALITY 25/26 shape): receipt
path, expected receipt digest, measured revision, correction path. Old/actual
tokens are RE-DERIVED by this counter (old from the receipt, actual from the
registry at the measured revision), never frozen as strings here.

Legs: RECEIPT (receipt bytes at lands == digest frozen at freeze, i.e. the
historical receipt unchanged), MISMATCH (stated token re-derived from the
receipt != actual token re-derived from the registry at the measured
revision), CORRECTION (the lands correction binds digest+rev+old+actual and
each field re-derives), RESOLVED (CORRECTION pass => unresolved=0).
Printed at every grade: `MISMATCH: stated=<tok> actual=<tok> count=1` and
`UNRESOLVED: <n>`.

Controls per draft: do-nothing (lands==freeze) graded-never-passed; lying
correction (actual field wrong) fails CORRECTION; wrong revision fails
CORRECTION; changed receipt fails RECEIPT.

Refusals mirror fixture accept-o.py (QUALITY 25(a) shape).
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys

LEGS = ["RECEIPT", "MISMATCH", "CORRECTION", "RESOLVED"]

def die_refuse(msg):
    print(f"FIXTURE-CA: FAIL legs=0/{len(LEGS)} (refused: {msg})")
    return 2

def show(root, rev, path):
    r = subprocess.run(["git", "-C", root, "show", f"{rev}:{path}"],
                       capture_output=True, text=True)
    return r.returncode, r.stdout

def ancestor(root, a, b):
    r = subprocess.run(["git", "-C", root, "merge-base", "--is-ancestor", a, b])
    return r.returncode == 0

def s884_usedby(text):
    for line in text.splitlines():
        if re.match(r"\| S884 \|", line):
            cells = [c.strip() for c in line.split("|")]
            # row: '|' id ... used-by '|' -> 13 split parts; used-by is index 11
            return cells[11] if len(cells) > 12 else None
    return None

def receipt_stated(text):
    for line in text.splitlines():
        m = re.search(r"W01[ \t]S884 tierC mined used-by=(\S+)", line)
        if m:
            return m.group(1)
    return None

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
        import hashlib as hl
        import pathlib
        cfg = json.loads(pathlib.Path("reports/round-79/claims.json").read_text())
        ca = cfg["ca"]
        receipt = pathlib.Path(ca["receipt"])
        stated = receipt_stated(receipt.read_text()) if receipt.is_file() else None
        reg = pathlib.Path("corpus/SOURCES.md")
        actual = s884_usedby(reg.read_text()) if reg.is_file() else None
        digest = hl.sha256(receipt.read_bytes()).hexdigest() if receipt.is_file() else None
        print(f"MISMATCH: stated={stated} actual={actual} count={1 if stated and stated != actual else 0}")
        corr = pathlib.Path(ca["correction"])
        fields = {}
        if corr.is_file():
            for line in corr.read_text().splitlines():
                m = re.match(r"^(receipt-digest|measured-revision|old-token|actual-token): (\S+)$", line)
                if m:
                    fields[m.group(1)] = m.group(2)
        legs = [("RECEIPT", digest == ca["expected_sha"]),
                ("MISMATCH", stated is not None and stated != actual),
                ("CORRECTION", fields.get("receipt-digest") == ca["expected_sha"]
                 and fields.get("measured-revision") == ca["measured_rev"]
                 and fields.get("old-token") == stated
                 and fields.get("actual-token") == actual),
                ("RESOLVED", fields.get("receipt-digest") == ca["expected_sha"]
                 and fields.get("actual-token") == actual)]
        npass = sum(1 for _, ok in legs if ok)
        for name, ok in legs:
            print(f"LEG {'PASS' if ok else 'FAIL'} {name}")
        print(f"UNRESOLVED: {0 if legs[2][1] else (1 if legs[1][1] else 0)}")
        print(f"FIXTURE-CA: {'PASS' if npass == len(LEGS) else 'FAIL'} legs={npass}/{len(LEGS)}")
        return 0 if npass == len(LEGS) else 1

    for rev in (a.lands, a.freeze):
        if not re.fullmatch(r"[0-9a-f]{40}", rev):
            return die_refuse("non-40-hex revision")
    rc, cfg = show(a.root, a.freeze, "reports/round-79/claims.json")
    if rc != 0:
        return die_refuse("frozen claims.json unreadable")
    cfg = json.loads(cfg)
    frozen_legs = cfg["legs"]["Ca"]
    if frozen_legs != LEGS:
        return die_refuse(f"LEGCOUNT frozen={frozen_legs} own={LEGS}")
    if a.lands == cfg["base"]:
        return die_refuse("lands equals frozen base")
    if not ancestor(a.root, a.freeze, a.lands):
        return die_refuse("freeze not ancestor of lands")
    ca = cfg["ca"]
    receipt_path = ca["receipt"]
    expected_sha = ca["expected_sha"]
    measured_rev = ca["measured_rev"]

    results = []
    # RECEIPT: historical receipt at lands equals the frozen digest.
    rc, receipt = show(a.root, a.lands, receipt_path)
    digest = hashlib.sha256(receipt.encode()).hexdigest() if rc == 0 else None
    receipt_ok = digest == expected_sha
    results.append(("RECEIPT", receipt_ok))

    # MISMATCH: stated (receipt) vs actual (registry at measured rev).
    stated = receipt_stated(receipt) if rc == 0 else None
    rc2, reg = show(a.root, measured_rev, "corpus/SOURCES.md")
    actual = s884_usedby(reg) if rc2 == 0 else None
    mismatch = (stated is not None and stated != actual)
    print(f"MISMATCH: stated={stated} actual={actual} count={1 if mismatch else 0}")
    results.append(("MISMATCH", mismatch))

    # CORRECTION: the lands file binds digest + measured rev + old + actual,
    # each field parsed exactly (whole value after the key) and re-derived
    # against this counter's own re-derivation.
    rc3, corr = show(a.root, a.lands, ca["correction"])
    fields = {}
    if rc3 == 0:
        for line in corr.splitlines():
            m = re.match(r"^(receipt-digest|measured-revision|old-token|actual-token): (\S+)$", line)
            if m:
                fields[m.group(1)] = m.group(2)
    corr_ok = rc3 == 0 and \
        fields.get("receipt-digest") == expected_sha and \
        fields.get("measured-revision") == measured_rev and \
        fields.get("old-token") == stated and \
        fields.get("actual-token") == actual
    results.append(("CORRECTION", corr_ok))
    results.append(("RESOLVED", corr_ok))

    npass = sum(1 for _, ok in results if ok)
    for name, ok in results:
        print(f"LEG {'PASS' if ok else 'FAIL'} {name}")
    unresolved = 0 if corr_ok else (1 if mismatch else 0)
    print(f"UNRESOLVED: {unresolved}")
    print(f"FIXTURE-CA: {'PASS' if npass == len(LEGS) else 'FAIL'} legs={npass}/{len(LEGS)}")
    return 0 if npass == len(LEGS) else 1

if __name__ == "__main__":
    sys.exit(main())
