#!/usr/bin/env python3
"""Isolate the pattern-split failure and probe the round-76 H2 guard's `-C` rule."""
import importlib.util, json, os, shlex, subprocess, sys

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
LED = json.load(open(os.path.join(LANE, "reports/round-76/ledger.json"), encoding="utf-8"))
BASE, CWD = LED["base"], os.path.abspath(sys.argv[1])
PAIR = {p["id"]: p for p in LED["pairs"]}

toks = shlex.split(PAIR["L76-19"]["rederive"])
print("CASE D2 the shlex-split token list executed inside the repo (cwd=lane)")
p = subprocess.run(toks, cwd=LANE, capture_output=True, text=True)
print("  argv=%s" % json.dumps(toks, ensure_ascii=False))
print("  exit=%d" % p.returncode)
print("  stderr=%r" % (p.stderr.strip().splitlines()[0][:200] if p.stderr.strip() else ""))
print()

spec = importlib.util.spec_from_file_location(
    "accept_ca_76", os.path.join(LANE, "reports/round-76/accept-ca.py"))
mod = importlib.util.module_from_spec(spec)
sys.modules["accept_ca_76"] = mod
spec.loader.exec_module(mod)
mod.CTX["fleet_root"] = "/home/vgpnk/Projects/shokunin"

no_c = PAIR["L76-01"]["observe_cmd"]
with_c = ["git", "-C", LANE] + no_c[1:]
print("CASE F round-76 H2 guard, mod.observe_problem(argv, clone=<lane>)")
for label, argv in (("without -C", no_c), ("with -C <lane> first", with_c)):
    print("  %-22s -> %r" % (label, mod.observe_problem(argv, LANE)))
