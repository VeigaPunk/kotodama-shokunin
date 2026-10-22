#!/usr/bin/env python3
"""Round-55 QUALITY criterion 11 controls for claim O, built before dispatch.

  python3 -B reports/round-55/criterion11-controls-o.py <lane-repo> <tree-ish> > reports/round-55/telemetry/criterion11-controls-o.txt

Read-only on the lane: `git archive <tree-ish>` is extracted into a mktemp directory, and every
control copy is built there. Each copy runs the declared argv verbatim from its own root:
  python3 -B reports/round-55/accept-o.py
GREEN  every mechanical clause holds through a stand-in landing that is never landed: the copy's
       tools/check-gate-quotes.py is replaced by a stand-in that prints the expected findings for
       corpus/lessons/round-54.md and the adversarial fixture and hands every other call
       (round-53, --selftest) to the base tool kept beside it. Expected exit 0.
One RED per mechanical clause, each the GREEN stand-in with that clause alone changed by its
nearest near-miss; expected exit 1 with that clause's leg FAIL and every other leg PASS:
  DOUBLED   12 of the 13 doubled-locator S-ids (S277 dropped; it keeps its truncated finding)
  TRUNC     S239 (a doubled-only row) gains a truncated-grounds finding: 18, one extra
  NOFALSE   S245 (a clean row) gains a `words=26` finding
  EXIT      the round-54 run prints the same findings and exits 0
  ESCAPE    S903 (hyphenated, 25 whitespace words) is reported as well
  KEEP53    the round-53 run drops its last `words=` line (S236)
  SELFTEST  `--selftest` exits 1
The script prints sha256 of each instrument it ran. Lines carry no `$ ` prefix, so criterion 9's
two-way dry-run check does not read this receipt.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ARGV = ["python3", "-B", "reports/round-55/accept-o.py"]
INSTRUMENTS = ["reports/round-55/accept-o.py", "tools/check-gate-quotes.py",
               "reports/round-55/fixtures/adversarial.md", "reports/round-55/base-gate-r53.txt",
               "reports/round-55/criterion11-controls-o.py"]
DOUBLED = [239, 240, 243, 246, 249, 259, 262, 265, 266, 267, 268, 275, 277]
TRUNC = [241, 242, 244, 248, 250, 251, 253, 255, 259, 263, 264, 265, 275, 276, 277, 278, 279]
ESC = [901, 902, 904, 905]

STANDIN = r'''#!/usr/bin/env python3
# Stand-in landing for a criterion-11 control copy only; never landed.
import json, os, subprocess, sys
CFG = json.loads(%r)
HERE = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1:]
if args == ["--selftest"]:
    if CFG["selftest_fail"]:
        print("SELFTEST stand-in FAIL"); sys.exit(1)
    sys.exit(subprocess.run([sys.executable, "-B", os.path.join(HERE, "check-gate-quotes-base.py")] + args).returncode)
if args and args[0].endswith("round-54.md"):
    out = [f"{args[0]}:1 S{n} doubled-locator" for n in CFG["doubled"]]
    out += [f"{args[0]}:1 S{n} truncated-grounds" for n in CFG["trunc"]]
    out += [f"{args[0]}:1 S{n} words=26" for n in CFG["stray"]]
    print("\n".join(out)); print(f"GATE_QUOTES: {len(out)} findings"); sys.exit(CFG["exit54"])
if args and args[0].endswith("adversarial.md"):
    out = [f"{args[0]}:1 S{n} words=26" for n in CFG["esc"]]
    print("\n".join(out)); print(f"GATE_QUOTES: {len(out)} findings"); sys.exit(1)
r = subprocess.run([sys.executable, "-B", os.path.join(HERE, "check-gate-quotes-base.py")] + args, capture_output=True, text=True)
lines = r.stdout.splitlines()
if CFG["drop53"] and args and args[0].endswith("round-53.md"):
    idx = max(i for i, l in enumerate(lines) if " words=" in l)
    lines.pop(idx)
print("\n".join(lines)); sys.stderr.write(r.stderr); sys.exit(r.returncode)
'''

GREEN = {"doubled": DOUBLED, "trunc": TRUNC, "stray": [], "exit54": 1, "esc": ESC,
         "drop53": False, "selftest_fail": False}
CONTROLS = [
    ("GREEN", {}, 0, []),
    ("RED-DOUBLED", {"doubled": [n for n in DOUBLED if n != 277]}, 1, ["DOUBLED"]),
    ("RED-TRUNC", {"trunc": TRUNC + [239]}, 1, ["TRUNC"]),
    ("RED-NOFALSE", {"stray": [245]}, 1, ["NOFALSE"]),
    ("RED-EXIT", {"exit54": 0}, 1, ["EXIT"]),
    ("RED-ESCAPE", {"esc": ESC + [903]}, 1, ["ESCAPE"]),
    ("RED-KEEP53", {"drop53": True}, 1, ["KEEP53"]),
    ("RED-SELFTEST", {"selftest_fail": True}, 1, ["SELFTEST"]),
]


def main():
    lane, tree = sys.argv[1], sys.argv[2]
    rev = subprocess.run(["git", "-C", lane, "rev-parse", tree], capture_output=True, text=True, check=True).stdout.strip()
    tmp = tempfile.mkdtemp(prefix="kotodama-r55-c11o-")
    try:
        base = os.path.join(tmp, "base")
        os.mkdir(base)
        archive = subprocess.run(["git", "-C", lane, "archive", rev], capture_output=True, check=True).stdout
        subprocess.run(["tar", "-x", "-C", base], input=archive, check=True)
        print(f"tree {rev}")
        for p in INSTRUMENTS:
            print(f"sha256 {hashlib.sha256(open(os.path.join(base, p), 'rb').read()).hexdigest()}  {p}")
        print("argv (run from each copy's root): python3 -B reports/round-55/accept-o.py")
        base_run = subprocess.run(ARGV, cwd=base, capture_output=True, text=True)
        print(f"\n## BASE (all-false where the claim adds behaviour; not a control): exit {base_run.returncode}")
        print((base_run.stdout + base_run.stderr).rstrip())
        failures = 0
        for name, delta, want, expect in CONTROLS:
            copy = os.path.join(tmp, name)
            shutil.copytree(base, copy)
            tool = os.path.join(copy, "tools/check-gate-quotes.py")
            os.rename(tool, os.path.join(copy, "tools/check-gate-quotes-base.py"))
            cfg = dict(GREEN, **delta)
            open(tool, "w", encoding="utf-8").write(STANDIN % json.dumps(cfg))
            r = subprocess.run(ARGV, cwd=copy, capture_output=True, text=True)
            legs = re.findall(r"^(\w+) (PASS|FAIL)", r.stdout, re.M)
            failing = [l for l, v in legs if v == "FAIL"]
            ok = r.returncode == want and failing == expect and len(legs) == 7
            failures += not ok
            print(f"\n## {name}: exit {r.returncode} (expected {want}); failing legs {failing}; "
                  f"{'AS EXPECTED' if ok else 'NOT AS EXPECTED'}")
            print((r.stdout + r.stderr).rstrip())
        print(f"\nCONTROLS {len(CONTROLS) - failures}/{len(CONTROLS)} as expected")
        return 1 if failures else 0
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    sys.exit(main())
