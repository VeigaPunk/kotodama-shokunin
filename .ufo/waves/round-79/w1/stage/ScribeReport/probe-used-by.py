# Read-only probe: compare census used-by tokens with the committed registry at a revision.
# Usage: python3 probe-used-by.py <repo> <rev> <census-receipt-path-at-rev>
import subprocess, sys, re
repo, rev, receipt = sys.argv[1], sys.argv[2], sys.argv[3]
def show(path):
    return subprocess.run(["git", "-C", repo, "show", f"{rev}:{path}"], capture_output=True, text=True, check=True).stdout
reg = show("corpus/SOURCES.md").splitlines()
rows = {}
for line in reg:
    m = re.match(r"^\| *(S\d+) \|", line)
    if m:
        cells = [c.strip() for c in line.split("|")]
        rows[m.group(1)] = cells
mism = 0
for line in show(receipt).splitlines():
    m = re.search(r"(S\d+) tierC mined used-by=(\S+)", line)
    if not m:
        continue
    sid, token = m.group(1), m.group(2)
    cells = rows.get(sid)
    if cells is None:
        print(f"NO-ROW {sid}"); mism += 1; continue
    reg_used = cells[-2]  # used-by is the last populated cell before the trailing empty cell
    status = "MATCH" if reg_used == token else "MISMATCH"
    if status == "MISMATCH":
        mism += 1
    print(f"{status} {sid} receipt={token} registry={reg_used}")
print(f"mismatch={mism}")
