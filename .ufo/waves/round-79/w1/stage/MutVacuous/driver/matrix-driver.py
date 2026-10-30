#!/usr/bin/env python3
"""Runs the round-77 stage counter's --ledger-check (subprocess) and its
BASEMISMATCH leg (in-process, base clone) over every fixture file.
Raw output only; the expected guard verdicts live in expected-verdicts.json."""
import argparse, glob, importlib.util, json, os, subprocess, sys, tempfile
BASE = "211f9526800906e0c585d878d265c37e5e090c15"
ap = argparse.ArgumentParser()
ap.add_argument("--counter", required=True); ap.add_argument("--lane", required=True)
ap.add_argument("--work", required=True); ap.add_argument("--fixtures", required=True)
a = ap.parse_args()
os.makedirs(a.work, exist_ok=True)
spec = importlib.util.spec_from_file_location("acca", a.counter)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
lane = os.path.abspath(a.lane); work = os.path.abspath(a.work)
m.CTX["root"] = lane; m.CTX["fleet_root"] = None; m.RUN_STATE["work"] = work
cfg = {"base": BASE, "root": lane, "fleet_root": None,
       "repair_mutable": list(m.REPAIR_MUTABLE), "annotate_append": list(m.ANNOTATE_ALLOW),
       "lane_row_ids": [], "c_families": [], "min_pairs": m.MIN_PAIRS_FLOOR}
m.CTX["cfg"] = cfg
tmp = tempfile.mkdtemp(prefix="matrix-", dir=work)
clone = m.materialize(lane, BASE, tmp, "base")
assert clone is not None
for path in sorted(glob.glob(os.path.join(a.fixtures, "*.json"))):
    name = os.path.basename(path)
    led = json.load(open(path))
    print("##### %s" % name)
    print("status: %s" % led.get("status"))
    r = subprocess.run([sys.executable, "-B", a.counter, "--ledger-check", path, "--root", lane,
                        "--base", BASE, "--work", work], capture_output=True, text=True)
    print("ledger-check exit=%d stdout=%s" % (r.returncode, r.stdout.strip().replace("\n", " | ")))
    if r.stderr.strip():
        print("ledger-check stderr=%s" % r.stderr.strip()[:300])
    pairs = [p for p in led.get("pairs") or [] if isinstance(p, dict)]
    ev = m.evaluate_pairs(pairs, clone, clone)
    out = []
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        m.leg_basemismatch(out, cfg, pairs, ev)
    for pid, e in zip([p["id"] for p in pairs], ev):
        print("  %-4s stated=%r stated_ok=%s base_obs=%r parsed=%s why=%r" % (
            pid, (e["stated"] or "")[:60], e["stated_ok"], (e["base"][0] or "")[:60], e["base"][1], e["base"][2]))
    for n, passed, detail in out:
        print("BASEMISMATCH(R77 stage) passed=%s detail=%s" % (passed, detail[:700]))
    print()
