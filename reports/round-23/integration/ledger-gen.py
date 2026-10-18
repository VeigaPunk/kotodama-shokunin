#!/usr/bin/env python3
"""R23-D04 — round-23 fragment-ledger generator (read-time census of reports/round-23/**).

Emits the machine twin `reports/round-23/integration/fragment-ledger.json` and
the Markdown ledger `reports/round-23/integration/fragment-ledger.md` from one
census pass over the live tree. Read-only over everything it censuses; writes
only the two ledger files named above (and only when invoked without --json).

Usage:
    python3 reports/round-23/integration/ledger-gen.py            # write both files
    python3 reports/round-23/integration/ledger-gen.py --json     # stdout only
    python3 reports/round-23/integration/ledger-gen.py --selftest # in-memory controls

The owner-seat column is inferred from the path shape (the seat groups declared
in `reports/round-23/targets.json`: O-successor-pins 8, O-wording 4, D-rule 4);
an unknown shape reads `unassigned` and is never guessed. The census is
point-in-time over a live 16-worker wave: re-run it on the settled tree before
quoting counts.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ROUND_DIR = "reports/round-23"
OUT_MD = HERE / "fragment-ledger.md"
OUT_JSON = HERE / "fragment-ledger.json"

# Declared seat plan (reports/round-23/targets.json); kept for the md plan table
# and for reconciling planned vs censused seats. Path shapes are inferred, not
# pre-assigned: a shape that matches no rule reads `unassigned`.
SEAT_PLAN = (
    ("O-successor-pins", 8,
     "combined-source successor pins for the final projector/adapter sources "
     "(D2 live + frozen pins, v2, D4 profile rows), new rows with before/after digests"),
    ("O-wording", 4,
     "PLACEHOLDER_RE wording false positive ('unchanged-foreign-path control' "
     "in D4-CL08) dispositioned without weakening any placeholder rule"),
    ("D-rule", 4,
     "family-clean projection rule drafted for SKILL.md from "
     "reports/round-22/bleed/design.md; orchestrator lands it"),
)

SEAT_BY_PREFIX = (
    ("integration/", "integration (R23-D04 fragment ledger)"),
    ("wording/", "O-wording"),
    ("pins/", "O successor pins"),
    ("successors/", "O successor pins"),
    ("repin/", "O successor pins"),
    ("skill-rule/", "D-rule"),
    ("rule/", "D-rule"),
    ("d-rule/", "D-rule"),
    ("audit/", "auditors"),
)

SEAT_BY_NAME = (
    (r"^claims\.json$|^targets\.json$", "declaration (parent)"),
    (r"^run-validation\.py$|^validation\.json$", "acceptance runner"),
    (r"^scope(-a\d+)?\.md$", "scope auditor"),
    (r"^audit.*\.md$|^retrospective-audit-.*\.md$", "auditors"),
    (r"^adjacency\.md$", "adjacency scribe"),
    (r"^report-draft\.md$|^rerun\.json$|^fragment-index.*\.md$|^ledger-snapshot\.md$",
     "X scribes (report/index)"),
    (r".*wording.*", "O-wording"),
    (r".*(successor|combined).*", "O successor pins"),
    (r".*(skill-rule|family-clean|projection-rule).*", "D-rule"),
)


def owner_seat(rel):
    for pattern, seat in SEAT_BY_NAME:
        if re.match(pattern, rel):
            return seat
    for prefix, seat in SEAT_BY_PREFIX:
        if rel.startswith(prefix):
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
    unassigned = sum(1 for r in rows if r["owner_seat"] == "unassigned")
    return {
        "round": 23,
        "date": now[:10],
        "baseline_revision": git_rev("HEAD^"),
        "declare_revision": git_rev("HEAD"),
        "census_utc": now,
        "census_command": "python3 reports/round-23/integration/ledger-gen.py",
        "fragment_count": len(rows),
        "unassigned_count": unassigned,
        "note": ("Read-time census of a live 16-worker wave (O-successor-pins 8, "
                 "O-wording 4, D-rule 4). Not a completeness claim; re-run on the "
                 "settled tree."),
        "fragments": rows,
    }


def render_md(doc):
    lines = [
        "# R23-D04 — round-23 fragment ledger (read-time census of `reports/round-23/**`)",
        "",
        "- round: 23 (operator: loop 2, GLM round 1 of 2; 16 workers, zai glm-5.3-flash MAX;",
        "  `reports/round-23/claims.json`, `reports/round-23/targets.json`).",
        f"- seat **R23-D04** (fragment ledger). Census `{doc['census_utc']}`.",
        f"- baseline revision `{doc['baseline_revision']}` (round-22 close); declare revision",
        f"  `{doc['declare_revision']}`.",
        "- canon: **NON-CANON integration ledger.** It admits nothing, certifies no round, and",
        "  edits no byte outside `reports/round-23/integration/`.",
        "",
        "## Declared seat plan",
        "",
        "| seat group | workers | assignment |",
        "|---|---:|---|",
    ]
    for name, workers, task in SEAT_PLAN:
        lines.append(f"| {name} | {workers} | {task} |")
    lines += [
        "",
        "## Census",
        "",
        f"{doc['fragment_count']} files at `{doc['census_utc']}` "
        f"(`__pycache__/`, `*.pyc`, `*.log` excluded; "
        f"{doc['unassigned_count']} unassigned).",
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
        "- Owner-seat is inferred from the path shape (prefix and name rules; the",
        "  round-23 targets declare seat counts, not paths); `unassigned` is never",
        "  guessed and any `unassigned` row is a parent reconciliation item.",
        "- The two ledger files are themselves censused: their rows record the",
        "  pre-write version (self-reference); re-run the generator to refresh.",
        "- The counting command for both round-23 claims is",
        "  `python3 reports/round-23/run-validation.py` (declared in",
        "  `reports/round-23/claims.json`); until that runner and its receipt land,",
        "  no claim outcome is certified by this ledger.",
        "- This ledger is the index the parent uses to integrate fragments into",
        "  `LOG.md` / `SCORECARD.md` (drafts: `reports/round-23/integration/log-draft.md`,",
        "  `reports/round-23/integration/scorecard-draft.md`); it is not a verdict and",
        "  not a completeness claim.",
        "",
    ]
    return "\n".join(lines)


def selftest():
    import tempfile
    checks = []
    with tempfile.TemporaryDirectory(prefix="r23-ledger-") as workdir:
        base = Path(workdir) / ROUND_DIR
        (base / "integration").mkdir(parents=True)
        (base / "wording").mkdir()
        (base / "successors").mkdir()
        (base / "skill-rule").mkdir()
        (base / "__pycache__").mkdir()
        (base / "claims.json").write_text("{}\n")
        (base / "wording" / "disposition.md").write_text("x\n")
        (base / "successors" / "pin-v2.json").write_text("x\n")
        (base / "skill-rule" / "rule.md").write_text("x\n")
        (base / "__pycache__" / "junk.pyc").write_text("junk")
        rows = census(workdir)
        checks.append(("pyc excluded", all("__pycache__" not in r["path"] for r in rows)))
        checks.append(("four rows (one fixture .pyc excluded)", len(rows) == 4))
        checks.append(("claims = declaration",
                       any(r["owner_seat"] == "declaration (parent)"
                           for r in rows if r["path"].endswith("claims.json"))))
        checks.append(("wording seat named",
                       any(r["owner_seat"] == "O-wording"
                           for r in rows if "wording/" in r["path"])))
        checks.append(("successor-pins seat named",
                       any(r["owner_seat"] == "O successor pins"
                           for r in rows if "successors/" in r["path"])))
        checks.append(("d-rule seat named",
                       any(r["owner_seat"] == "D-rule"
                           for r in rows if "skill-rule/" in r["path"])))
        digests = {r["path"]: r["sha256"] for r in rows}
        checks.append(("digest 64 hex", all(len(d) == 64 for d in digests.values())))
        checks.append(("unassigned never guessed",
                       all(r["owner_seat"] != "unassigned" for r in rows)))
        rows2 = census(workdir)
        checks.append(("deterministic rows",
                       [r["sha256"] for r in rows] == [r["sha256"] for r in rows2]))
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
