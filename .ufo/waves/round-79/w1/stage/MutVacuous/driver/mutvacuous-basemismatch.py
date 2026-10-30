#!/usr/bin/env python3
"""MutVacuous probe (round 79 W1): exercises the round-77 stage counter's
BASEMISMATCH leg and its --ledger-check path on mutated ledgers.

Read-only with respect to the lane: the counter is imported from --counter, the
lane is only read through `git -C <lane> ...` clones made under --work.
Usage:
  python3 -B mutvacuous-basemismatch.py --counter <accept-ca.py> --lane <lane> \
      --work <scratch dir> --fixtures <dir with pristine.json, clean-control-v2.json, L-*.json>
Prints raw evidence to stdout; the caller tees it into the stage.
"""
import argparse, copy, importlib.util, json, os, subprocess, sys, tempfile

BASE = "211f9526800906e0c585d878d265c37e5e090c15"
ap = argparse.ArgumentParser()
ap.add_argument("--counter", required=True)
ap.add_argument("--lane", required=True)
ap.add_argument("--work", required=True)
ap.add_argument("--fixtures", required=True)
args = ap.parse_args()
os.makedirs(args.work, exist_ok=True)

spec = importlib.util.spec_from_file_location("acca", args.counter)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
m.CTX["root"] = os.path.abspath(args.lane)
m.CTX["fleet_root"] = None
m.RUN_STATE["work"] = os.path.abspath(args.work)
cfg = {"base": BASE, "root": m.CTX["root"], "fleet_root": None,
       "repair_mutable": list(m.REPAIR_MUTABLE), "annotate_append": list(m.ANNOTATE_ALLOW),
       "lane_row_ids": [], "c_families": [], "min_pairs": m.MIN_PAIRS_FLOOR}
m.CTX["cfg"] = cfg
tmp = tempfile.mkdtemp(prefix="mutvac-", dir=os.path.abspath(args.work))
clone = m.materialize(m.CTX["root"], BASE, tmp, "base")
if clone is None:
    sys.exit(2)
PRISTINE = json.load(open(os.path.join(args.fixtures, "pristine.json")))["pairs"]

def load(name):
    return json.load(open(os.path.join(args.fixtures, name)))["pairs"]

def run(label, pairs, rows=True):
    print("=== %s" % label)
    ev = m.evaluate_pairs(pairs, clone, clone)
    if rows:
        for p, e in zip(pairs, ev):
            print("  %-4s stated=%r stated_ok=%s base_obs=%r parsed=%s why=%r" % (
                p["id"], e["stated"], e["stated_ok"], e["base"][0], e["base"][1], e["base"][2]))
    out = []
    m.leg_basemismatch(out, cfg, pairs, ev)
    for name, passed, detail in out:
        print("  VERDICT %s passed=%s detail=%s" % (name, passed, detail))
    print()

def by(pairs, pid):
    return next(p for p in pairs if p["id"] == pid)

def no_obs_rec(pairs):
    for p in pairs:
        p.pop("observed_at_base", None)

OBS = {}
for p in PRISTINE:
    OBS[p["id"]] = m.observed_token(p, clone["path"])[0]
print("OBSERVED-AT-BASE via counter observed_token:", json.dumps(OBS, sort_keys=True))
print()

# --- pristine and controls -------------------------------------------------
run("V0 committed R77 probe as-is", copy.deepcopy(PRISTINE))
x = copy.deepcopy(PRISTINE); no_obs_rec(x)
run("V0b R77 probe minus observed_at_base", x)
run("CTRL clean-control-v2 (10 truthful pairs, observed_at_base present)", load("clean-control-v2.json"))

# --- mutation: stated token equals observed --------------------------------
x = copy.deepcopy(PRISTINE); no_obs_rec(x)
p = by(x, "D11"); p.pop("stated_parse", None); p["stated_token"] = OBS["D11"]
run("M1 D11 stated_token := actual observed %r (new==observed, one pair)" % OBS["D11"], x)
x = copy.deepcopy(PRISTINE); no_obs_rec(x)
for p in x:
    p.pop("stated_parse", None); p["stated_token"] = OBS[p["id"]]
run("M2 every pair stated_token := actual observed", x, rows=False)

# --- vacuity: stated token derived from whole stated_text ------------------
x = copy.deepcopy(PRISTINE); no_obs_rec(x)
for p in x:
    p.pop("stated_parse", None); p.pop("stated_token", None)
run("M3 no stated_token/stated_parse (whole stated_text becomes the token), no observed_at_base", x, rows=False)

# --- invalid stated tokens counted as red ----------------------------------
x = copy.deepcopy(PRISTINE); no_obs_rec(x)
for p in x:
    p.pop("stated_parse", None); p["stated_token"] = "9" + p["id"]
by(x, "D02")["stated_token"] = "   "
by(x, "D03")["stated_token"] = ""
run("M4 D02 stated_token='   ' and D03 stated_token='' (invalid), others valid-but-wrong", x, rows=True)

# --- invalid observations must not count as red ----------------------------
x = copy.deepcopy(PRISTINE); no_obs_rec(x)
for p in x:
    p.pop("stated_parse", None); p["stated_token"] = "9" + p["id"]
by(x, "D04")["parse"] = r"^NOPE:([0-9]+)$"
run("M5 D04 parse-miss (invalid observation), others valid-but-wrong", x, rows=False)
x = copy.deepcopy(PRISTINE); no_obs_rec(x)
for p in x:
    p.pop("stated_parse", None); p["stated_token"] = "9" + p["id"]
by(x, "D05")["observe_cmd"] = ["git", "-C", ".", "grep", "-c", "-E", "^#", "0" * 40, "--", "LOG.md"]
run("M6 D05 observe_cmd pinned to a non-object (dead pin)", x, rows=False)

# --- truncation boundary: observed is norm(out)[:200] for parse-less pairs --
full_cmd = ["git", "-C", ".", "grep", "-h", "-E", "^#", BASE, "--", "LOG.md"]
raw, why = m.run_observe(clone["path"], full_cmd)
full = m.norm(raw)
print("TRUNC full observation length=%d; counter's observed token length=%d"
      % (len(full), len(m.norm(raw)[:200])))
t = {"id": "T01", "observe_cmd": full_cmd, "stated_text": full, "stated_token": full}
rest = [dict(p, stated_token="9" + p["id"]) for p in copy.deepcopy(PRISTINE)[:9]]
for q in rest:
    q.pop("stated_parse", None); q.pop("observed_at_base", None)
run("M7 T01 parse-less, stated_token := FULL observed text", [t] + rest, rows=True)
t2 = dict(t, stated_token=full[:200])
run("M7b T01 parse-less, stated_token := 200-char prefix", [t2] + rest, rows=True)

# --- first-match vs live footer (D11 observation) --------------------------
x = copy.deepcopy(PRISTINE); no_obs_rec(x)
ev = m.evaluate_pairs([by(x, "D11")], clone, clone)
print("D11 observation: parse is rx.search (first match); observed=%r; stated=%r"
      % (ev[0]["base"][0], ev[0]["stated"]))
print()

# --- --ledger-check (pre-freeze path) on mutated ledger files ---------------
print("=== --ledger-check (pre-freeze build check; no BASEMISMATCH leg) on fixture files")
for name in ["pristine.json", "clean-control-v2.json", "L-whole-sentence.json",
             "L-empty-token-D02.json", "L-ws-token-D02.json",
             "L-stated-eq-observed-D11.json", "L-no-observed-rec.json"]:
    r = subprocess.run([sys.executable, "-B", args.counter, "--ledger-check",
                        os.path.join(args.fixtures, name), "--root", m.CTX["root"],
                        "--base", BASE, "--work", os.path.abspath(args.work)],
                       capture_output=True, text=True)
    print("== %s exit=%d stdout=%s" % (name, r.returncode, r.stdout.strip()))
