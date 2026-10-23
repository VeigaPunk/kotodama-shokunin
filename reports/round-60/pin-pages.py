#!/usr/bin/env python3
"""Pin the page bytes of every row the amulets entry cites (round 60, revision 7 EVIDENCE leg).
Run from the lane root: python3 -B /fast/scratch/hyaku/kotodama-r60a3/L1/pin-pages.py
Writes reports/round-60/captures/pages/<sid>.bin and pages/manifest.json; plain requests only."""
import concurrent.futures as cf
import datetime
import hashlib
import importlib.util
import json
import os
import re
import subprocess

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
OUT = "reports/round-60/captures/pages"
spec = importlib.util.spec_from_file_location("loc", "reports/round-60/reopen-quote.py")
loc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(loc)
entry = open("corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md", encoding="utf-8").read()
cited = sorted(set(re.findall(r"\bS\d{3,}\b", entry)))
rows = {}
for line in open("corpus/SOURCES.md", encoding="utf-8"):
    m = re.match(r"^\|\s*(S\d{3,})\s*\|", line)
    if m:
        rows[m.group(1)] = line.split("|")
os.makedirs(OUT, exist_ok=True)


def fetch(url, path):
    r = subprocess.run(["timeout", "90", "curl", "-sSL", "-A", UA, "-o", path, "-w", "%{http_code}\t%{content_type}", url],
                       capture_output=True, text=True)
    code, _, ctype = r.stdout.partition("\t")
    return code, ctype


def pin(sid):
    urls, quote = loc.row_target(rows[sid])
    tries = list(urls)
    for u in urls:
        if not u.startswith("https://web.archive.org/"):
            tries.append("https://web.archive.org/web/2026id_/" + u)
    path = os.path.join(OUT, f"{sid}.bin")
    log = []
    for url in tries:
        code, ctype = fetch(url, path)
        data = open(path, "rb").read() if os.path.exists(path) else b""
        ok = code == "200" and bool(quote) and loc.locate_in(loc.to_text(data, ctype), quote)
        log.append(f"{url} {code} {len(data)} located={ok}")
        if ok:
            return sid, {"url": url, "file": f"{sid}.bin", "sha256": hashlib.sha256(data).hexdigest(), "content_type": ctype,
                         "http": int(code), "bytes": len(data),
                         "fetched_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}, log
    if os.path.exists(path):
        os.remove(path)
    return sid, None, log


manifest, fails = {}, []
with cf.ThreadPoolExecutor(8) as ex:
    for sid, item, log in ex.map(pin, cited):
        print(sid, "PINNED" if item else "NOT-PINNED", " | ".join(log))
        if item:
            manifest[sid] = item
        else:
            fails.append(sid)
json.dump(manifest, open(os.path.join(OUT, "manifest.json"), "w"), indent=1, sort_keys=True)
print(f"cited={len(cited)} pinned={len(manifest)} not_pinned={fails}")
