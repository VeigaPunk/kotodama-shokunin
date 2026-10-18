#!/usr/bin/env python3
"""R20-D23 — round-20 fragment-ledger generator (read-time census of reports/round-20/**).

Emits the machine twin `reports/round-20/integration/fragment-ledger.json` and
the Markdown ledger `reports/round-20/integration/fragment-ledger.md` from one
census pass over the live tree. Read-only over everything it censuses; writes
only the two ledger files named above (and only when invoked without --json).

Usage:
    python3 reports/round-20/integration/ledger-gen.py            # write both files
    python3 reports/round-20/integration/ledger-gen.py --json     # stdout only
    python3 reports/round-20/integration/ledger-gen.py --selftest # in-memory controls

The owner-seat column is inferred from the path shape (the seat groups declared
in `reports/round-20/targets.json`); an unknown shape reads `unassigned` and is
never guessed. The census is point-in-time: re-run on the settled tree.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ROUND_DIR = "reports/round-20"
OUT_MD = HERE / "fragment-ledger.md"
OUT_JSON = HERE / "fragment-ledger.json"

SEAT_BY_PREFIX = (
    ("handoff/", "D-handoff (frozen+scribe group where D21..D24)"),
    ("entries/R20-D", "D-handoff entry fragment"),
    ("entries/", "entry fragment"),
    ("readme/", "C-readme"),
    ("audit/", "auditors"),
    ("wart/", "O-wart (per-family era-alias)"),
    ("knowledge/", "knowledge seat"),
    ("integration/", "integration (R20-D23 fragment ledger)"),
    ("repin/", "O repin"),
)

SEAT_BY_NAME = (
    (r"^audit-\d+\.md$", "auditors"),
    (r"^claims\.json$|^targets\.json$", "declaration (parent)"),
    (r"^run-validation\.py$|^validation\.json$", "acceptance runner"),
    (r"^report-draft\.md$|^rerun\.json$|^fragment-index\.md$|^ledger-snapshot\.md$|^fragment-index-x\d+\.md$", "X scribes (report/index)"),
    (r"^regression\.md$", "regression seat"),
    (r"^scope(-a\d+)?\.md$", "scope auditor"),
    (r"^adjacency\.md$", "adjacency scribe"),
    (r"^handoff/expected\.json$|^handoff/packet\.md$|^handoff/twin\.json$|"
     r"^handoff/run\.log$|^handoff/freeze\.txt$|^handoff/frozen\.md$", "R20-D21 (freeze)"),
)


def owner_seat(rel):
    for pattern, seat in SEAT_BY_NAME:
        if re.match(pattern, rel):
            return seat
    for prefix, seat in SEAT_BY_PREFIX:
        if rel.startswith(prefix):
            m = re.match(r"entries/(R20-[A-Z]+\d+)\.md$", rel)
            if m:
                return f"{m.group(1)} ({seat})"
            return seat
    return "unassigned"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def census(root=ROOT):
    base = Path(root) / ROUND_DIR
    rows = []
    for path in sorted(base.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(base).as_posix()
        if rel.startswith("__pycache__/") or rel.endswith(".pyc") or rel.endswith(".log"):
            continue
        stat = path.stat()
        rows.append({
            "path": f"{ROUND_DIR}/{rel}",
            "bytes": stat.st_size,
            "sha256": sha256_file(path),
            "mtime_utc": datetime.datetime.fromtimestamp(
                stat.st_mtime, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "owner_seat": owner_seat(rel),
        })
    return rows


def git_rev(rev):
    import subprocess
    return subprocess.run(["git", "rev-parse", rev], cwd=ROOT, capture_output=True,
                          text=True).stdout.strip()


def build(rows):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "round": 20,
        "date": now[:10],
        "baseline_revision": git_rev("HEAD^"),
        "declare_revision": git_rev("HEAD"),
        "census_utc": now,
        "census_command": "python3 reports/round-20/integration/ledger-gen.py",
        "fragment_count": len(rows),
        "note": ("Read-time census of a live 64-worker wave. Not a completeness claim; "
                 "re-run on the settled tree."),
        "fragments": rows,
    }


def render_md(doc):
    lines = [
        "# R20-D23 — round-20 fragment ledger (read-time census of `reports/round-20/**`)",
        "",
        "- round: 20 (operator: loop 2 of 3, build round 4 of 4; `reports/round-20/claims.json`).",
        f"- seat **R20-D23** (fragment ledger). Census `{doc['census_utc']}`.",
        f"- baseline revision `{doc['baseline_revision']}` (round-19 admit); declare revision",
        f"  `{doc['declare_revision']}`.",
        "- canon: **NON-CANON integration ledger.** It admits nothing, certifies no round, and",
        "  edits no byte outside `reports/round-20/integration/`.",
        "",
        "## Census",
        "",
        f"{doc['fragment_count']} files at `{doc['census_utc']}` (`__pycache__/`, `*.pyc`, `*.log` excluded).",
        "",
        "| path | bytes | sha256 (12) | mtime UTC | owner seat |",
        "|---|---:|---|---|---|",
    ]
    for row in doc["fragments"]:
        lines.append(
            f"| `{row['path']}` | {row['bytes']} | `{row['sha256'][:12]}` | "
            f"{row['mtime_utc'][11:19]} | {row['owner_seat']} |")
    lines += [
        "",
        "## Reading",
        "",
        "- The census is point-in-time; the wave was still writing when it was taken.",
        "  A file arriving after it needs a dated refresh, not an inferred worker failure.",
        "- Owner-seat is inferred from the path shape; `unassigned` is never guessed.",
        "- The two ledger files are themselves censused: their rows record the",
        "  pre-write version (self-reference); re-run the generator to refresh.",
        "- This ledger is the index the parent uses to integrate fragments into",
        "  `LOG.md` / `SCORECARD.md`; it is not a verdict and not a completeness claim.",
        "",
    ]
    return "\n".join(lines)


def selftest():
    import tempfile
    checks = []
    with tempfile.TemporaryDirectory(prefix="r20-ledger-") as workdir:
        base = Path(workdir) / ROUND_DIR
        (base / "handoff").mkdir(parents=True)
        (base / "entries").mkdir()
        (base / "__pycache__").mkdir()
        (base / "handoff" / "expected.json").write_text("{}\n")
        (base / "entries" / "R20-D21.md").write_text("x\n")
        (base / "__pycache__" / "junk.pyc").write_text("junk")
        rows = census(workdir)
        checks.append(("pyc excluded", all("__pycache__" not in r["path"] for r in rows)))
        checks.append(("two rows", len(rows) == 2))
        checks.append(("entry seat named", any("R20-D21" in r["owner_seat"] for r in rows)))
        checks.append(("handoff seat named", any("D-handoff" in r["owner_seat"] for r in rows)))
        digests = {r["path"]: r["sha256"] for r in rows}
        checks.append(("digest 64 hex", all(len(d) == 64 for d in digests.values())))
        rows2 = census(workdir)
        checks.append(("deterministic rows", [r["sha256"] for r in rows] == [r["sha256"] for r in rows2]))
    bad = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print(f"{'ok' if ok else 'FAIL'} {name}")
    print(f"selftest: {len(checks) - len(bad)}/{len(checks)} checks passed")
    return 0 if not bad else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="stdout only, write nothing")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        sys.exit(selftest())
    doc = build(census())
    if args.json:
        print(json.dumps(doc, indent=1, ensure_ascii=False))
        return
    OUT_MD.write_text(render_md(doc), encoding="utf-8")
    OUT_JSON.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"ledger: {doc['fragment_count']} fragments at {doc['census_utc']}")


if __name__ == "__main__":
    main()
