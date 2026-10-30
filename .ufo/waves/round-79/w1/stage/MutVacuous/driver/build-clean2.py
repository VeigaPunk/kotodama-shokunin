# Truthful control v2: every stated_text is a verbatim base line (LEDGER-valid),
# the stated token is the first digit run on that line, observed is a distinct
# git-grep count over the same base file, observed_at_base == actual observation.
import json, re, subprocess
W = "/fast/scratch/hyaku/kotodama-r79/MutVacuous"
LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE = "211f9526800906e0c585d878d265c37e5e090c15"
def show(path):
    return subprocess.run(["git", "-C", LANE, "show", "%s:%s" % (BASE, path)],
                          capture_output=True, text=True).stdout.splitlines()
def count(pattern, path):
    r = subprocess.run(["git", "-C", LANE, "grep", "-c", "-E", pattern, BASE, "--", path],
                       capture_output=True, text=True)
    return r.stdout.strip().rsplit(":", 1)[1] if r.returncode == 0 and r.stdout.strip() else None
PATTERNS = ["^#", "round", "TRIAGE", "GATE", "mint", "^- ", "^## ", "[0-9]", "^\\|", "[Cc]ounts"]
files = ["LOG.md", "SCORECARD.md", "corpus/lessons/round-75.md", "corpus/lessons/round-76.md"]
pairs = []
used = set()
for path in files:
    lines = show(path)
    for ln, text in enumerate(lines, 1):
        if len(pairs) >= 10: break
        m = re.search(r"[0-9]+", text)
        if not m or len(text) > 180 or "`" in text or "|" in text or "\\" in text:
            continue
        if not text.strip() or path + str(ln) in used: continue
        n = m.group(0)
        pat = PATTERNS[len(pairs) % len(PATTERNS)]
        obs = count(pat, path)
        if obs is None or obs == n:
            continue
        used.add(path + str(ln))
        i = len(pairs) + 1
        pairs.append({
            "id": "C%02d" % i, "disposition": "ANNOTATE",
            "stated_at": "%s:%d" % (path, ln), "stated_text": text,
            "stated_token": n,
            "observe_cmd": ["git", "-C", ".", "grep", "-c", "-E", pat, BASE, "--", path],
            "parse": ":([0-9]+)$", "observed_at_base": obs,
            "expected_after": obs,
            "rederive": "git -C . grep -c -E '%s' %s -- %s" % (pat, BASE, path),
            "why": "truthful control v2: verbatim base line, stated token != observed"})
print(len(pairs), "pairs")
led = {"round": 77, "claim": "Ca", "base": BASE,
       "status": "CONTROL-clean v2 (MutVacuous probe; not a frozen ledger)", "pairs": pairs}
json.dump(led, open(W + "/ledgers/clean-control-v2.json", "w"), ensure_ascii=False, indent=1)
for p in pairs: print(p["id"], p["stated_at"], repr(p["stated_token"]), p["observed_at_base"], repr(p["observe_cmd"][6]))
