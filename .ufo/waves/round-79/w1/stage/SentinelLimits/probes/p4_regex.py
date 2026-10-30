# Probe P4: ledger parse/stated_parse are compiled and run by Python re with no time bound.
# Each measurement runs in a child with a 10 s wall cap so the probe itself cannot run away.
import subprocess, sys, json
CASES = [
    (r"(a|aa)+$", "a" * 26 + "!", "nested alternation, growing input"),
    (r"^(\w+\s?)+:$", "word " * 8 + "!", "nested quantifier over words, 8 words"),
    (r"^(\w+\s?)+:$", "word " * 12 + "!", "nested quantifier over words, 12 words"),
    (r"([0-9]+)$", "1" * 60000 + "x", "historical shape ([0-9]+)$ on 60000 digits"),
]
CHILD = r'''
import re, sys, time, json
pat, text = json.loads(sys.stdin.read())
t = time.perf_counter()
m = re.compile(pat, re.M | re.S).search(text)
print(json.dumps({"match": bool(m), "secs": round(time.perf_counter() - t, 4)}))
'''
for pat, text, label in CASES:
    try:
        p = subprocess.run([sys.executable, "-B", "-c", CHILD], input=json.dumps([pat, text]),
                           capture_output=True, text=True, timeout=10)
        res = p.stdout.strip() or ("rc=%d %s" % (p.returncode, p.stderr.strip()[:80]))
    except subprocess.TimeoutExpired:
        res = "WALL-CAP 10s exceeded (killed by probe)"
    print("%-44s len=%-6d %s" % (label, len(text), res))
