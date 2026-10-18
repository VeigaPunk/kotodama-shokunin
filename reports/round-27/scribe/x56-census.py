#!/usr/bin/env python3
"""R27-X56 census — read-only walk of reports/round-27/** (stdout only).

Emits a Markdown census table (bytes, sha8, mtime UTC, inferred owner,
conformance-state cell) or a JSON receipt with `--json`, or the round tree's
top-level directory shape with `--dirs`. Opens no file for writing; `--selftest`
is in-memory only.

    export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
    python3 -B reports/round-27/scribe/x56-census.py --selftest   # in-memory controls
    python3 -B reports/round-27/scribe/x56-census.py              # markdown table
    python3 -B reports/round-27/scribe/x56-census.py --json       # receipt
    python3 -B reports/round-27/scribe/x56-census.py --dirs       # directory shape

Owner inference is directory/name based and stated in the index; `unassigned`
is never guessed. The index file itself is excluded (self row).
"""
import argparse
import datetime
import hashlib
import json
import sys
from pathlib import Path

BASE = Path("reports/round-27")
SELF = BASE / "fragment-index-x56.md"
EXCLUDE_PARTS = {"__pycache__"}
EXCLUDE_SUFFIX = (".pyc", ".log")


def owner(rel: str) -> str:
    p = rel
    if p.endswith("claims.json") or p.endswith("targets.json"):
        return "declaration (parent)"
    if "/audit/" in p:
        return "auditors (X5x/X6x)"
    # C — register-strata knowledge entry + corpus/README reconciliation
    if "/readme/" in p:
        return "C (corpus-README reconciliation seats)"
    if "/knowledge/" in p or "/corpus/" in p or "/entry/" in p:
        return "C (register-knowledge entry seats)"
    if "/lessons/" in p:
        return "C (lessons-entry / index seats)"
    # D — register law landing (D4 component, syllabify fix)
    if "/register/" in p or "/law/" in p or "/d4/" in p or "/argot/" in p:
        return "D (register-law seats)"
    if "/gate-tests/" in p:
        return "D/O (gate test fixtures + runner)"
    # O — D4 pin sweep + regressions
    if "/pinsweep/" in p or "/pins/" in p or "/sweep/" in p or "/repin/" in p:
        return "O (pin-sweep seats)"
    if "/remainders/" in p or "/regression/" in p:
        return "O (regression seats)"
    if "/integration/" in p:
        return "integration (parent-owned)"
    if p.endswith("run-validation.py"):
        return "acceptance runner"
    if p.endswith("validation.json"):
        return "acceptance runner/receipt"
    if p.endswith("availability.json"):
        return "X (availability seat)"
    if "/scribe/" in p:
        return "X (scribe seats)"
    if p.endswith("scope.md") or "report-draft" in p or p.endswith("rerun.json"):
        return "X (scribe seats)"
    if "/zzz-lessons-index-revision" in p:
        return "C (lessons-index revision seats)"
    if p.endswith("adjacency.md"):
        return "X (adjacency/scribe seats)"
    return "unassigned"


def state(rel: str) -> str:
    p = rel
    if p.endswith("claims.json") or p.endswith("targets.json"):
        return "Declared thresholds and seat allocation, not achieved outcomes."
    if p.endswith("run-validation.py"):
        return ("Executable runner; existence is not a green end-to-end "
                "acceptance (the receipt is the verdict).")
    if p.endswith("validation.json"):
        return "Primary receipt; written by the runner. Binding checked below."
    if p.endswith("availability.json"):
        return "Availability record; a route/liveness measurement, not acceptance."
    if "/integration/" in p:
        return "NON-CANON integration draft (LOG/SCORECARD); parent-owned landing."
    if "/audit/" in p:
        return ("Audit fragment (read-only tool/report/receipt); attributed "
                "evidence, not independently re-executed here.")
    if "/readme/" in p:
        return ("C fragment (corpus/README reconciliation sweep); attributed "
                "evidence; the landed README is outside this subtree.")
    if "/knowledge/" in p or "/corpus/" in p or "/entry/" in p:
        return ("C fragment (register-strata knowledge entry); attributed "
                "evidence; the landed corpus entry is outside this subtree.")
    if "/lessons/" in p:
        return ("C fragment (census/tool/report/revision draft); attributed "
                "evidence; the landed index is outside this subtree.")
    if "/register/" in p or "/law/" in p or "/d4/" in p or "/argot/" in p:
        return ("D fragment (register-law derivation); attributed evidence, "
                "not independently re-executed here.")
    if "/gate-tests/" in p:
        return ("Gate negative/positive fixture set + its runner/receipt; "
                "attributed evidence, not re-executed here.")
    if "/pinsweep/" in p or "/pins/" in p or "/sweep/" in p or "/repin/" in p:
        return ("O fragment (D4 pin sweep / new pin row); attributed evidence; "
                "a pin is a measurement, not a claim.")
    if "/remainders/" in p or "/regression/" in p:
        return "O fragment (regression battery / remainder disposition); attributed evidence."
    if "/scribe/" in p:
        return "X scribe fragment; attributed evidence."
    if "/zzz-lessons-index-revision" in p:
        return ("C lessons-index revision (new file, not an edit of the filed "
                "`corpus/lessons/README.md`); attributed evidence, read here.")
    return "Presence recorded; not independently re-executed here."


def walk(base: Path):
    files = []
    if not base.is_dir():
        return files
    for p in base.rglob("*"):
        if not p.is_file():
            continue
        if EXCLUDE_PARTS & set(p.parts):
            continue
        if p.name.endswith(EXCLUDE_SUFFIX):
            continue
        if p == SELF:
            continue
        files.append(p)
    return sorted(files)


def rows_of(base: Path):
    out = []
    for p in walk(base):
        data = p.read_bytes()
        mt = datetime.datetime.fromtimestamp(
            p.stat().st_mtime, datetime.timezone.utc).strftime("%H:%M:%S")
        out.append({
            "path": str(p),
            "bytes": len(data),
            "lines": data.count(b"\n"),
            "sha256": hashlib.sha256(data).hexdigest(),
            "sha8": hashlib.sha256(data).hexdigest()[:8],
            "mtime_utc": mt,
            "owner": owner(str(p)),
            "state": state(str(p)),
        })
    return out


def census_utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")


def emit_markdown(rows):
    print("| artifact | bytes | sha8 | mtime UTC | inferred owner | "
          "conformance state / limit |")
    print("|---|---:|---|---|---|---|")
    for r in rows:
        print(f"| `{r['path']}` | {r['bytes']} | `{r['sha8']}` | "
              f"{r['mtime_utc']} | {r['owner']} | {r['state']} |")
    print(f"CENSUS_COUNT={len(rows)}")


def emit_dirs():
    if not BASE.is_dir():
        print("(no round-27 tree)")
        return
    subs = {}
    for p in walk(BASE):
        rel = p.relative_to(BASE)
        top = rel.parts[0] if len(rel.parts) > 1 else "(root)"
        subs.setdefault(top, []).append(str(rel))
    for top in sorted(subs):
        print(f"{top}: {len(subs[top])} file(s)")
        for f in sorted(subs[top]):
            print(f"    {f}")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--dirs", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()
    if args.dirs:
        emit_dirs()
        return 0

    rows = rows_of(BASE)
    if args.json:
        print(json.dumps({
            "schema": "kotodama-r27-census-v1",
            "census_utc": census_utc(),
            "base": str(BASE),
            "excluded": {"parts": sorted(EXCLUDE_PARTS),
                         "suffix": list(EXCLUDE_SUFFIX),
                         "self": str(SELF)},
            "count": len(rows),
            "rows": rows,
        }, indent=1, sort_keys=True))
    else:
        emit_markdown(rows)
    return 0


def selftest():
    """In-memory controls. No file is opened for writing."""
    checks = []

    def ck(name, cond, observed=None):
        checks.append((name, bool(cond), observed))

    ck("owner-declaration", owner("reports/round-27/claims.json")
       == "declaration (parent)")
    ck("owner-audit", owner("reports/round-27/audit/x58-foo.md")
       == "auditors (X5x/X6x)")
    ck("owner-knowledge", owner("reports/round-27/knowledge/entry.md")
       == "C (register-knowledge entry seats)")
    ck("owner-register", owner("reports/round-27/register/law.md")
       == "D (register-law seats)")
    ck("owner-pins", owner("reports/round-27/pins/rows.json")
       == "O (pin-sweep seats)")
    ck("owner-unknown", owner("reports/round-27/mystery.bin") == "unassigned")
    ck("state-runner-not-green",
       "not a green" in state("reports/round-27/run-validation.py"))
    ck("state-receipt", "Primary receipt" in state("reports/round-27/validation.json"))

    ck("excl-pycache", "__pycache__" in EXCLUDE_PARTS)
    ck("excl-pyc", ".pyc".endswith(EXCLUDE_SUFFIX))
    ck("excl-log", ".log".endswith(EXCLUDE_SUFFIX))
    ck("self-excluded", SELF.name == "fragment-index-x56.md")

    data = b"a\nb\n"
    ck("lines-count", data.count(b"\n") == 2)
    ck("sha8-len", len(hashlib.sha256(data).hexdigest()[:8]) == 8)

    ck("base-scoped", str(SELF).startswith(str(BASE)))

    bad = [c for c in checks if not c[1]]
    for name, ok, obs in checks:
        print(f"  {'PASS' if ok else 'FAIL'} {name}"
              + (f" observed={obs!r}" if not ok and obs is not None else ""))
    print(f"SELFTEST {'OK' if not bad else 'FAILED'}: "
          f"{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
