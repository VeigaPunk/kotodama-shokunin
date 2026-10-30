# Read-only survey of committed ledger bytes at base via git cat-file (no worktree reads).
import subprocess, json, sys, collections
REPO = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE = "44f76d456c1b326a71ffdb381590af825cbf11be"
def git(*a):
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True)
ls = git("ls-tree", "-r", "-z", "--name-only", BASE).stdout.split(b"\0")
paths = [p.decode() for p in ls if p.endswith(b"ledger.json") or p.endswith(b"probe-real-ledger.json")]
print("ledger-like paths at base:", len(paths))
parse_vals = collections.Counter(); sparse_vals = collections.Counter(); bin_ = collections.Counter()
sizes = []; bad = []
def dup_hook(pairs):
    keys = [k for k, _ in pairs]
    d = [k for k, c in collections.Counter(keys).items() if c > 1]
    if d: bad.append(("dupkeys", d))
    return dict(pairs)
def pc(s): bad.append(("nonstd-const", s)); raise ValueError(s)
for p in paths:
    raw = git("show", "%s:%s" % (BASE, p)).stdout
    sizes.append((len(raw), p))
    try:
        raw.decode("utf-8")
    except UnicodeDecodeError as e:
        bad.append(("utf8", p, str(e)[:80]))
        continue
    try:
        d = json.loads(raw, object_pairs_hook=dup_hook, parse_constant=pc)
    except Exception as e:
        bad.append(("json", p, type(e).__name__, str(e)[:80])); continue
    pairs = d.get("pairs", d) if isinstance(d, dict) else d
    if not isinstance(pairs, list): continue
    for pr in pairs:
        if not isinstance(pr, dict): continue
        parse_vals[str(pr.get("parse"))] += 1
        sparse_vals[str(pr.get("stated_parse"))[:60]] += 1
        oc = pr.get("observe_cmd")
        if isinstance(oc, list) and oc:
            bin_[(oc[0], oc[1] if len(oc) > 1 else None)] += 1
        else:
            bin_[("NONLIST", type(oc).__name__)] += 1
print("max bytes", max(sizes))
print("parse values", parse_vals.most_common())
print("stated_parse values", sparse_vals.most_common(20))
print("observe_cmd (argv0,argv1) shapes", bin_.most_common(20))
print("problems", len(bad))
for b in bad[:40]: print(" ", b)
