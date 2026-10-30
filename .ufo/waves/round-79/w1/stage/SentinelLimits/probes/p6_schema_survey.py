# Probe P6: which committed ledgers are Ca-schema (pairs carry observe_cmd argv), and their parse modes.
import subprocess, json, collections
REPO = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE = "44f76d456c1b326a71ffdb381590af825cbf11be"
def show(p):
    return subprocess.run(["git", "-C", REPO, "show", "%s:%s" % (BASE, p)], capture_output=True).stdout
ls = subprocess.run(["git", "-C", REPO, "ls-tree", "-r", "-z", "--name-only", BASE], capture_output=True).stdout.split(b"\0")
paths = [p.decode() for p in ls if p.endswith((b"ledger.json", b"probe-real-ledger.json"))]
modes = collections.Counter(); per_file = {}; maxpairs = 0
for p in paths:
    raw = show(p)
    try: d = json.loads(raw)
    except Exception as e: per_file[p] = "unparseable: %s" % type(e).__name__; continue
    pairs = d.get("pairs") if isinstance(d, dict) else d
    if not isinstance(pairs, list): continue
    ca = [x for x in pairs if isinstance(x, dict) and isinstance(x.get("observe_cmd"), list)]
    if not ca: continue
    maxpairs = max(maxpairs, len(ca))
    per_file[p] = "ca-pairs=%d" % len(ca)
    for x in ca:
        modes[str(x.get("parse"))] += 1
        if x.get("stated_parse"): modes["stated_parse:" + str(x["stated_parse"])] += 1
        if str(x.get("parse")).startswith("python") or x["observe_cmd"][0] in ("python3", "sh", "bash"):
            modes["INTERPRETER-OBSERVE"] += 1
for k, v in per_file.items(): print(k, v)
print("max ca pairs in one ledger:", maxpairs)
print("parse / stated_parse modes:")
for k, v in modes.most_common(): print("  %4d  %s" % (v, k))
