#!/usr/bin/env python3
"""Round-55 claim O acceptance (operability, capability: Gate-line shape checker). Run from the
lane root:

  python3 -B reports/round-55/accept-o.py [--root DIR]

The checker under test is tools/check-gate-quotes.py. A finding line is
`<path>:<line> <S-id> <detail>`; the classes this claim adds print their class word as the detail
(`doubled-locator`, `truncated-grounds`); over-cap and ellipsis-joined findings keep their
`words=<n>` detail. The last stdout line of a lesson run is `GATE_QUOTES: <n> findings`.
One leg per mechanical clause of claim O (reports/round-55/claims.json), each printed with PASS or
FAIL:
  DOUBLED   on corpus/lessons/round-54.md the S-ids carrying a `doubled-locator` finding are
            exactly the 13 named in the round-54 closure's routed defect 2 (DOUBLED_WANT)
  TRUNC     on corpus/lessons/round-54.md the S-ids carrying a `truncated-grounds` finding are
            exactly the 17 named in the round-54 closure's routed defect 1 (TRUNC_WANT)
  NOFALSE   on corpus/lessons/round-54.md no finding of any class names an S-id outside the
            union of those two sets
  EXIT      the round-54 run and the adversarial-fixture run each exit 1 (findings), not 0 or 2
  ESCAPE    on reports/round-55/fixtures/adversarial.md (the round-54 ReviewGateQuoteTool
            fixture, copied unchanged) the (S-id, detail) findings are exactly S901 words=26
            (quote hard-wrapped onto a continuation line), S902 words=26 (guillemets), S904
            words=22 (ellipsis between two spans of one run) and S905 words=26 (a `- ` row whose
            first token is `*`, fixture line 10); S903 (hyphenated tokens, 25 whitespace words)
            stays unreported because the lane's word rule is a whitespace split
  KEEP53    on corpus/lessons/round-53.md the run exits 1 and its `words=<n>` finding lines are
            exactly the lines of reports/round-55/base-gate-r53.txt (the base tool's output there,
            summary excluded)
  FORMAT    the round-54, adversarial and round-53 runs each write nothing to stderr, every stdout
            line is a finding line or the summary, and the summary's <n> equals the finding lines
  SELFTEST  `python3 -B tools/check-gate-quotes.py --selftest` exits 0
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input, including a pinned
input (the fixture, base-gate-r53.txt) whose sha256 differs from PINS. Every tool's exit status is
read directly (no pipe, no shell).
Review-only (no leg): whether each new class's rule is documented in the tool's docstring with its
false-positive boundary; whether the selftest carries a red and a green case for each new class;
whether the rules generalise beyond the routed lines (the S903 hyphen convention stays
documented, not fixed).
"""
import argparse
import hashlib
import os
import re
import subprocess
import sys

TOOL = "tools/check-gate-quotes.py"
R54 = "corpus/lessons/round-54.md"
R53 = "corpus/lessons/round-53.md"
FIX = "reports/round-55/fixtures/adversarial.md"
BASE53 = "reports/round-55/base-gate-r53.txt"
PINS = {FIX: "e31e602f9e1e069b1fef4eff9652320c541ce2ab6f34442154770cd22ffaa01b",
        BASE53: "77fd00f478136724b24a12cb4b798f8e841800c0b0475547f2fa402870a57076"}
DOUBLED_WANT = {f"S{n}" for n in (239, 240, 243, 246, 249, 259, 262, 265, 266, 267, 268, 275, 277)}
TRUNC_WANT = {f"S{n}" for n in (241, 242, 244, 248, 250, 251, 253, 255, 259, 263, 264, 265, 275,
                                276, 277, 278, 279)}
ESCAPE_WANT = {("S901", "words=26"), ("S902", "words=26"), ("S904", "words=22"), ("S905", "words=26")}
FINDING = re.compile(r"^(\S+):(\d+) (S\d+) (\S+)$")
SUMMARY = re.compile(r"^GATE_QUOTES: (\d+) findings$")


def run(root, argv):
    try:
        return subprocess.run([sys.executable, "-B"] + argv, cwd=root, capture_output=True, text=True,
                              timeout=300)
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f"ACCEPT_O_INPUT_ERROR {' '.join(argv)} {error}", file=sys.stderr)
        return None


def findings(result):
    return [m.groups() for m in map(FINDING.match, result.stdout.splitlines()) if m]


def well_formed(result):
    lines = result.stdout.splitlines()
    found = [l for l in lines if FINDING.match(l)]
    other = [l for l in lines if not FINDING.match(l)]
    summary = SUMMARY.match(other[-1]) if len(other) == 1 else None
    return (not result.stderr and summary is not None and lines and lines[-1] == other[0]
            and int(summary.group(1)) == len(found))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    try:
        for path, digest in PINS.items():
            seen = hashlib.sha256(open(os.path.join(root, path), "rb").read()).hexdigest()
            if seen != digest:
                print(f"ACCEPT_O_INPUT_ERROR {path} sha256 {seen} != pinned {digest}", file=sys.stderr)
                return 2
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
    esc = {(s, d) for _, _, s, d in findings(adv)}
    kept = [l for l in r53.stdout.splitlines() if FINDING.match(l) and FINDING.match(l).group(4).startswith("words=")]
    first_diff = next((f"{a!r} vs {b!r}" for a, b in zip(kept + ["<none>"] * len(base53), base53 + ["<none>"] * len(kept))
                       if a != b), "none")
    bad_format = [name for name, r in (("round54", r54), ("adversarial", adv), ("round53", r53)) if not well_formed(r)]
    legs = [
        ("DOUBLED", doubled == DOUBLED_WANT,
         f"count={len(doubled)} missing={sorted(DOUBLED_WANT - doubled)} extra={sorted(doubled - DOUBLED_WANT)}"),
        ("TRUNC", trunc == TRUNC_WANT,
         f"count={len(trunc)} missing={sorted(TRUNC_WANT - trunc)} extra={sorted(trunc - TRUNC_WANT)}"),
        ("NOFALSE", not stray, f"stray={stray}"),
        ("EXIT", r54.returncode == 1 and adv.returncode == 1, f"round54={r54.returncode} adversarial={adv.returncode}"),
        ("ESCAPE", esc == ESCAPE_WANT, f"missing={sorted(ESCAPE_WANT - esc)} extra={sorted(esc - ESCAPE_WANT)}"),
        ("KEEP53", r53.returncode == 1 and kept == base53,
         f"exit={r53.returncode} lines={len(kept)} base={len(base53)} first_diff={first_diff}"),
        ("FORMAT", not bad_format, f"malformed_runs={bad_format}"),
        ("SELFTEST", st.returncode == 0, f"exit={st.returncode} {(st.stdout.strip().splitlines() or ['?'])[-1]}"),
    ]
    for name, ok, detail in legs:
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
    return 0 if all(ok for _, ok, _ in legs) else 1


if __name__ == "__main__":
    sys.exit(main())
