#!/usr/bin/env python3
"""X27 — corpus/README.md index vs on-disk files (read-only).

Parses the index sections of corpus/README.md, extracts the indexed rows
(``- `name.md` — ...``) per partition, and compares them against the files
actually present under corpus/knowledge/<partition>/. Emits a JSON receipt
plus a human summary. Never writes to the corpus.

Usage:
    python3 reports/round-19/audit/coverage-audit.py            # summary
    python3 reports/round-19/audit/coverage-audit.py --json     # full receipt
    python3 reports/round-19/audit/coverage-audit.py --selftest # planted controls
"""
import argparse
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CORPUS = os.path.join(LANE, "corpus")
README = os.path.join(CORPUS, "README.md")
KNOWLEDGE = os.path.join(CORPUS, "knowledge")

PARTITIONS = [
    "linguistics",
    "myth-symbol",
    "culture-material",
    "synthesis",
    "verification",
    "civilizations",
]

SECTION_RE = re.compile(r"^##\s+([a-z-]+)/\s*\((\d+)\)\s*$")
ROW_RE = re.compile(r"^-\s+`([^`]+\.md)`\s+—")


def parse_readme(text):
    """Return {partition: {"declared": int, "rows": [name, ...]}}."""
    sections = {}
    current = None
    for line in text.splitlines():
        m = SECTION_RE.match(line)
        if m:
            current = m.group(1)
            sections[current] = {"declared": int(m.group(2)), "rows": []}
            continue
        if line.startswith("## "):
            current = None
            continue
        if current is None:
            continue
        rm = ROW_RE.match(line)
        if rm:
            sections[current]["rows"].append(rm.group(1))
    return sections


def disk_files(partition):
    d = os.path.join(KNOWLEDGE, partition)
    if not os.path.isdir(d):
        return None
    return sorted(f for f in os.listdir(d) if f.endswith(".md"))


def audit(readme_path=README, knowledge=KNOWLEDGE):
    with open(readme_path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8")
    sections = parse_readme(text)
    report = {
        "schema": "kotodama-coverage-audit-v1",
        "readme": os.path.relpath(readme_path, LANE),
        "readme_sha256": hashlib.sha256(raw).hexdigest(),
        "partitions": {},
        "totals": {},
    }
    grand_rows = 0
    grand_files = 0
    for part in PARTITIONS:
        sec = sections.get(part)
        rows = sec["rows"] if sec else []
        declared = sec["declared"] if sec else None
        files = disk_files(part) if knowledge == KNOWLEDGE else _files_under(knowledge, part)
        files = files or []
        rows_set = set(rows)
        files_set = set(files)
        entry = {
            "declared_header_count": declared,
            "index_rows": len(rows),
            "duplicate_rows": sorted({r for r in rows if rows.count(r) > 1}),
            "disk_files": len(files),
            "missing_from_index": sorted(files_set - rows_set),
            "index_only_ghosts": sorted(rows_set - files_set),
            "header_vs_rows_delta": (declared - len(rows)) if declared is not None else None,
            "header_vs_disk_delta": (declared - len(files)) if declared is not None else None,
        }
        entry["clean"] = (
            not entry["duplicate_rows"]
            and not entry["missing_from_index"]
            and not entry["index_only_ghosts"]
            and entry["header_vs_disk_delta"] == 0
        )
        report["partitions"][part] = entry
        grand_rows += len(rows)
        grand_files += len(files)
    report["totals"] = {
        "index_rows": grand_rows,
        "disk_files": grand_files,
        "partitions_clean": sum(1 for p in report["partitions"].values() if p["clean"]),
        "partitions": len(PARTITIONS),
    }
    return report


def _files_under(root, partition):
    d = os.path.join(root, partition)
    if not os.path.isdir(d):
        return None
    return sorted(f for f in os.listdir(d) if f.endswith(".md"))


def selftest():
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        if not cond:
            ok = False
        print(("PASS " if cond else "FAIL ") + name + (" " + detail if detail else ""))

    sample = """# t

## linguistics/ (2)

- `a.md` — first
- `b.md` — second

## verification/ (1)

- `c.md` — only
"""
    sec = parse_readme(sample)
    check("parse: two sections", set(sec) == {"linguistics", "verification"})
    check("parse: declared count", sec["linguistics"]["declared"] == 2, str(sec["linguistics"]["declared"]))
    check("parse: rows", sec["linguistics"]["rows"] == ["a.md", "b.md"], str(sec["linguistics"]["rows"]))
    check("parse: ignores non-rows", sec["verification"]["rows"] == ["c.md"])
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--readme", default=README)
    ap.add_argument("--knowledge", default=KNOWLEDGE)
    args = ap.parse_args(argv)
    if args.selftest:
        return 0 if selftest() else 1
    rep = audit(args.readme, args.knowledge)
    if args.json:
        print(json.dumps(rep, indent=2, sort_keys=True))
    else:
        for part, e in rep["partitions"].items():
            flag = "clean" if e["clean"] else "DIRTY"
            print(
                f"{part:16s} {flag:5s} declared={e['declared_header_count']} "
                f"rows={e['index_rows']} disk={e['disk_files']} "
                f"missing={len(e['missing_from_index'])} ghosts={len(e['index_only_ghosts'])}"
            )
            if e["missing_from_index"]:
                print("    missing:", e["missing_from_index"])
            if e["index_only_ghosts"]:
                print("    ghosts :", e["index_only_ghosts"])
        t = rep["totals"]
        print(f"TOTAL rows={t['index_rows']} disk={t['disk_files']} "
              f"clean={t['partitions_clean']}/{t['partitions']}")
    return 0 if rep["totals"]["partitions_clean"] == rep["totals"]["partitions"] else 2


if __name__ == "__main__":
    sys.exit(main())
