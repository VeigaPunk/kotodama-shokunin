"""RevCounterCa probe 2:
(a) LEDGER ">= 10 unique pairs" — 10 content-identical pairs, distinct ids.
(b) STAMP `measured` fallback — unresolved --main falls back to the worktree
    HEAD of the graded root; a lane whose main has moved past lands still
    passes when the worktree sits at lands.
"""
import importlib.util
import json
import os
import subprocess
import tempfile

os.environ["HYAKU_SCRATCH"] = "/fast/scratch/hyaku/kotodama-r77/RevCounterCa/work2"

ACA = ("/home/vgpnk/Projects/shokunin/kotodama-shokunin"
       "/.ufo/waves/round-77/w1/stage/ExecAdaptCa/accept-ca.py")
PROBE = ("/home/vgpnk/Projects/shokunin/kotodama-shokunin"
         "/.ufo/waves/round-77/w1/stage/ExecAdaptCa/probe-real-ledger.json")
BASE = "211f9526800906e0c585d878d265c37e5e090c15"
LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
ACA_DIR = "/fast/scratch/hyaku/kotodama-r77/RevCounterCa"

spec = importlib.util.spec_from_file_location("aca", ACA)
aca = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aca)

# ---- (a) duplicate-content padding -------------------------------------
led = json.load(open(PROBE))
d01 = led["pairs"][0]
pad = []
for i in range(1, 11):
    p = json.loads(json.dumps(d01))
    p["id"] = "PAD%02d" % i
    pad.append(p)
led2 = {"round": 77, "claim": "Ca", "base": BASE,
        "status": "RevCounterCa scratch probe 3: 10 content-identical pairs",
        "pairs": pad}
out = os.path.join(ACA_DIR, "probe-dup.json")
json.dump(led2, open(out, "w"), indent=1)
env = dict(os.environ)
r = subprocess.run(
    ["python3", "-B", ACA, "--ledger-check", out, "--root", LANE,
     "--base", BASE],
    capture_output=True, text=True, env=env)
print("=== (a) 10 content-identical pairs, distinct ids")
print("exit=%d" % r.returncode)
print(r.stdout.strip())
print(r.stderr.strip())

# ---- (b) STAMP measured fallback ---------------------------------------
os.makedirs(os.path.join(ACA_DIR, "work2"), exist_ok=True)
td = tempfile.mkdtemp(prefix="fallback-", dir=os.path.join(ACA_DIR, "work2"))
lane, fleet, base, freeze, clean, combined = aca._build(td, "fb")
# lands = the clean Ca landing; worktree HEAD pinned there; --main unresolved
aca._at(lane, clean)
code, states, text = aca._run_check(lane, clean, freeze, fleet,
                                    "no-such-branch", combined=combined)
print("=== (b) --main unresolved, lane worktree HEAD at lands")
print("exit=%d states=%s" % (code, states))
for line in text.splitlines():
    if line.startswith(("LEG ", "ACCEPT-CA-77", "# measured", "     NOTE")):
        print(line)
