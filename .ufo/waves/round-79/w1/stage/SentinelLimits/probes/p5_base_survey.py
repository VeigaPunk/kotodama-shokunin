# Probe P5: read-only survey of tracked bytes at base via git cat-file --batch (no worktree reads).
# Reports sizes (to set caps against real history) and UTF-8/NUL/BOM status of text-like blobs.
import subprocess, collections
REPO = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE = "44f76d456c1b326a71ffdb381590af825cbf11be"
ls = subprocess.run(["git", "-C", REPO, "ls-tree", "-r", "-z", "--long", BASE], capture_output=True).stdout
entries = []
for rec in ls.split(b"\0"):
    if not rec: continue
    meta, path = rec.split(b"\t", 1)
    parts = meta.split()
    if parts[1] != b"blob": continue
    entries.append((parts[2].decode(), path.decode("utf-8", "surrogateescape")))
want = [e for e in entries if e[1].endswith((".md", ".json", ".txt", ".py", ".tsv", ".sh", ".jsonl"))]
inp = "".join(sha + "\n" for sha, _ in want).encode()
p = subprocess.run(["git", "-C", REPO, "cat-file", "--batch"], input=inp, capture_output=True)
buf = p.stdout; pos = 0
stats = collections.Counter(); sizes = []; bad = []; nul = []; bom = []
for sha, path in want:
    nl = buf.index(b"\n", pos); hdr = buf[pos:nl].split(); size = int(hdr[2]); pos = nl + 1
    data = buf[pos:pos + size]; pos += size + 1
    sizes.append((size, path)); stats["files"] += 1
    if b"\0" in data: nul.append(path)
    if data.startswith(b"\xef\xbb\xbf"): bom.append(path)
    try: data.decode("utf-8"); stats["utf8_ok"] += 1
    except UnicodeDecodeError as e: bad.append((path, str(e)[:70]))
sizes.sort(reverse=True)
print("text-like blobs:", stats["files"], "utf8_ok:", stats["utf8_ok"], "invalid utf8:", len(bad))
print("largest 5:", [(s, p) for s, p in sizes[:5]])
print("files > 64KiB:", sum(1 for s, _ in sizes if s > 65536), " > 2MiB:", sum(1 for s, _ in sizes if s > 2 * 1024 * 1024))
print("ledger-like sizes:", [(s, p) for s, p in sizes if p.endswith("ledger.json")][:8])
print("NUL-containing:", nul[:10])
print("BOM-prefixed:", bom[:10])
for b in bad[:10]: print("INVALID", b)
