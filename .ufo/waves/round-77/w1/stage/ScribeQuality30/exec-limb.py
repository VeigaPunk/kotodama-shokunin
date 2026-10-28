#!/usr/bin/env python3
"""Execution-limb probe on real lane bytes (read-only): shows why `git -C <repo>`
first and an argv-valued rederive are the difference between a command a re-runner
can execute and one that only runs from one working directory."""
import json, os, shlex, subprocess, sys

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
LED = json.load(open(os.path.join(LANE, "reports/round-76/ledger.json"), encoding="utf-8"))
BASE = LED["base"]
CWD = os.path.abspath(sys.argv[1])
PAIR = {p["id"]: p for p in LED["pairs"]}

def run(label, argv):
    p = subprocess.run(argv, cwd=CWD, capture_output=True, text=True)
    print("CASE %s" % label)
    print("  argv=%s" % json.dumps(argv, ensure_ascii=False))
    print("  cwd=%s" % CWD)
    print("  exit=%d" % p.returncode)
    print("  stdout=%r" % p.stdout.strip()[:200])
    print("  stderr=%r" % (p.stderr.strip().splitlines()[0][:160] if p.stderr.strip() else ""))
    print()

run("A r76 L76-01 observe_cmd as recorded (no -C)",
    PAIR["L76-01"]["observe_cmd"])
run("B the same command with `git -C <lane>` first",
    ["git", "-C", LANE] + PAIR["L76-01"]["observe_cmd"][1:])
red = PAIR["L76-19"]["rederive"]
toks = shlex.split(red)
print("CASE C L76-19 rederive, tokenized the way reports/round-76/accept-ca.py:rederive_argv does")
print("  rederive=%r" % red)
print("  shlex.split -> %s" % json.dumps(toks, ensure_ascii=False))
print()
run("D that token list executed", toks)
run("E L76-19 rederive as an argv with -C first and the pattern kept whole",
    ["git", "-C", LANE, "grep", "-h", "-E", "^window: chars=", BASE,
     "--", "reports/round-75/evidence/S892.txt"])
