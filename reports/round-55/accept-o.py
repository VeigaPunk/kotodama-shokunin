#!/usr/bin/env python3
"""Round-55 claim O acceptance (operability, capability: Gate-line shape checker). Run from the
lane root:

  python3 -B reports/round-55/accept-o.py [--root DIR]

The checker under test is tools/check-gate-quotes.py. A finding line is
`<path>:<line> <S-id> <detail>`; the classes this claim adds print their class word as the detail
(`doubled-locator`, `truncated-grounds`); the existing over-cap / ellipsis-joined findings keep
their `words=<n>` detail. One leg per mechanical clause of claim O
(reports/round-55/claims.json), each printed with PASS or FAIL:
  DOUBLED   on corpus/lessons/round-54.md the S-ids carrying a `doubled-locator` finding are
            exactly the 13 the round-54 closure routed (DOUBLED_WANT below)
  TRUNC     on corpus/lessons/round-54.md the S-ids carrying a `truncated-grounds` finding are
            exactly the 17 the round-54 closure routed (TRUNC_WANT below)
  NOFALSE   on corpus/lessons/round-54.md no finding of any class names an S-id outside the
            union of those two sets
  EXIT      the round-54 run exits 1 and the adversarial-fixture run exits 1 (findings), not 0 or 2
  ESCAPE    on reports/round-55/fixtures/adversarial.md (the round-54 ReviewGateQuoteTool
            fixture, copied unchanged) the S-ids with any finding are exactly S901 (hard-wrapped
            quote), S902 (guillemets), S904 (ellipsis between two spans) and S905 (`* ` bullet);
            S903 (hyphenated tokens, 25 whitespace words) stays unreported because the lane's
            word rule is a whitespace split
  KEEP53    on corpus/lessons/round-53.md the `words=<n>` finding lines are exactly the lines of
            reports/round-55/base-gate-r53.txt (the base tool's output there, summary excluded)
  SELFTEST  `python3 -B tools/check-gate-quotes.py --selftest` exits 0
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
Every tool's exit status is read directly (no pipe, no shell).
Review-only (no leg): whether each class's rule is documented in the tool's docstring, and
whether the rule generalises beyond the routed shapes.
"""
import argparse
import os
import re
import subprocess
import sys

TOOL = "tools/check-gate-quotes.py"
R54 = "corpus/lessons/round-54.md"
R53 = "corpus/lessons/round-53.md"
FIX = "reports/round-55/fixtures/adversarial.md"
BASE53 = "reports/round-55/base-gate-r53.txt"
DOUBLED_WANT = {f"S{n}" for n in (239, 240, 243, 246, 249, 259, 262, 265, 266, 267, 268, 275, 277)}
TRUNC_WANT = {f"S{n}" for n in (241, 242, 244, 248, 250, 251, 253, 255, 259, 263, 264, 265, 275,
                                276, 277, 278, 279)}
ESCAPE_WANT = {"S901", "S902", "S904", "S905"}
FINDING = re.compile(r"^(\S+):(\d+) (S\d+) (\S+)$")


def run(root, argv):
    try:
        return subprocess.run([sys.executable, "-B"] + argv, cwd=root, capture_output=True, text=True,
                              timeout=300)
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f"ACCEPT_O_INPUT_ERROR {' '.join(argv)} {error}", file=sys.stderr)
        return None


def findings(result):
    return [m.groups() for m in map(FINDING.match, result.stdout.splitlines()) if m]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    try:
        base53 = [l.rstrip("\n") for l in open(os.path.join(root, BASE53), encoding="utf-8")
                  if FINDING.match(l.rstrip("\n"))]
    except OSError as error:
        print(f"ACCEPT_O_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    r54, adv, r53, st = (run(root, [TOOL, R54]), run(root, [TOOL, FIX]), run(root, [TOOL, R53]),
                         run(root, [TOOL, "--selftest"]))
    if None in (r54, adv, r53, st):
        return 2
    f54 = findings(r54)
    doubled = {s for _, _, s, d in f54 if d == "doubled-locator"}
    trunc = {s for _, _, s, d in f54 if d == "truncated-grounds"}
    stray = sorted({s for _, _, s, _ in f54} - DOUBLED_WANT - TRUNC_WANT)
    esc = {s for _, _, s, _ in findings(adv)}
    kept = [l for l in r53.stdout.splitlines() if FINDING.match(l) and FINDING.match(l).group(4).startswith("words=")]
    legs = [
        ("DOUBLED", doubled == DOUBLED_WANT,
         f"count={len(doubled)} missing={sorted(DOUBLED_WANT - doubled)} extra={sorted(doubled - DOUBLED_WANT)}"),
        ("TRUNC", trunc == TRUNC_WANT,
         f"count={len(trunc)} missing={sorted(TRUNC_WANT - trunc)} extra={sorted(trunc - TRUNC_WANT)}"),
        ("NOFALSE", not stray, f"stray={stray}"),
        ("EXIT", r54.returncode == 1 and adv.returncode == 1, f"round54={r54.returncode} adversarial={adv.returncode}"),
        ("ESCAPE", esc == ESCAPE_WANT, f"found={sorted(esc)} want={sorted(ESCAPE_WANT)}"),
        ("KEEP53", kept == base53, f"lines={len(kept)} base={len(base53)}"),
        ("SELFTEST", st.returncode == 0, f"exit={st.returncode} {(st.stdout.strip().splitlines() or ['?'])[-1]}"),
    ]
    for name, ok, detail in legs:
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
    return 0 if all(ok for _, ok, _ in legs) else 1


if __name__ == "__main__":
    sys.exit(main())
