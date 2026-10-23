#!/usr/bin/env python3
"""Diagnostic only: use the unchanged frozen locator against unrelated public pages."""
import concurrent.futures
import hashlib
import importlib.util
import json
from pathlib import Path

root = Path.cwd()
spec = json.loads((root / "reports/round-59/d-fixes.json").read_text())
loader = importlib.util.spec_from_file_location("carry_offsite_rowcheck", root / "reports/round-59/rowcheck.py")
rowcheck = importlib.util.module_from_spec(loader)
loader.loader.exec_module(rowcheck)
urls = [
    "https://example.com/",
    "https://www.iana.org/domains/reserved",
    "https://www.rfc-editor.org/rfc/rfc2119.txt",
    "https://docs.python.org/3/library/functions.html",
]


def probe(url):
    results = []
    for fix in spec["kongo"]["fixes"]:
        ok, detail = rowcheck.locator.locate([url], fix["support_quote"])
        results.append((fix["id"], ok, detail))
    return url, results


with concurrent.futures.ThreadPoolExecutor(4) as pool:
    checked = list(pool.map(probe, urls))

hits, absent, errors = [], 0, []
for url, results in checked:
    located = [fid for fid, ok, _ in results if ok]
    missing = [fid for fid, ok, detail in results if not ok and detail.endswith(" quote-absent")]
    other = [(fid, detail) for fid, ok, detail in results if not ok and not detail.endswith(" quote-absent")]
    print(f"URL {url} located={located} quote_absent={missing} other={other}")
    hits.extend((fid, url) for fid in located)
    absent += len(missing)
    errors.extend(other)
print(f"OFFSITE-QUOTE-PROBE: located={len(hits)}/56 quote_absent={absent}/56 other={len(errors)}/56 hits={hits}")
