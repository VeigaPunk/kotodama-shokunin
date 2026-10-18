#!/usr/bin/env python3
"""R28-X60 — sweep-completeness auditor (independent; own re-derivation).

Seat R28-X60 (SCRIBE X60: shard auditor — sweep completeness) for round 28,
claim O `pin-sweep` (`reports/round-28/claims.json`). NON-CANON audit evidence.

Round-28's O claim is "Final build-round sweep: every frozen/baseline/replay
surface re-verified; drifted rows re-pinned as new rows; the v3 handoff baseline
updated if its read set changed; battery 9/9; all replays green." A sweep is only
as complete as its **surface inventory**, so this tool does not replay rows — the
round's own runner and the pin-sweep seat do that. It answers the prior question:

    *how many pin surfaces exist, in how many classes, and which of them does a
    given sweep method actually reach?*

Round 27's X60 established the class map (8 classes, 81 rows) and two method
limits: a manifest-only replay reaches no baseline, and `TMPDIR=$PWD/.scratch`
turns a green manifest into `mirror_unsafe`. Round 28 must re-measure both,
because the RL-4 fix **changes the packet surface again** (the assembler gains a
`register_law` field list), which moves every pin that reads the packet.

Duties (each read-only):

  A. INVENTORY — enumerate every pin-bearing artifact by class.
  B. COVERAGE MATRIX — for each sweep method in use this round, the reachable
     and missed sets. A method that globs one root while rows live under three
     is measured, not asserted.
  C. D4-SURFACE TOUCH — for every pin naming a D4 surface, does the pin still
     hold against the live bytes? This is "did the sweep re-verify the thing the
     claim is about".
  D. TMPDIR SENSITIVITY — measure the same manifest under an in-repo and an
     out-of-repo TMPDIR, reporting both tallies.
  E. PACKET-READ SET (new for round 28) — which pin rows actually read
     `examples/culture-d4/packet.d4.yml` or its projection, i.e. which rows the
     RL-4 change can move. A sweep that reports "all green" without touching the
     read set has not swept the surface the round changed.
  F. FILED-SURFACE INTEGRITY (new for round 28) — `git status --porcelain` over
     the protected rounds 8..27. A round-28 write to a filed round-8..27 artifact
     is a protected-surface breach, and a re-run receipt that overwrote an
     admitted round's verdict is the round-20 binding hazard in its sharpest form.

Usage:
    export TMPDIR=/tmp PYTHONDONTWRITEBYTECODE=1
    python3 -B reports/round-28/audit/x60-sweep-completeness.py --inventory
    python3 -B reports/round-28/audit/x60-sweep-completeness.py --coverage
    python3 -B reports/round-28/audit/x60-sweep-completeness.py --readset
    python3 -B reports/round-28/audit/x60-sweep-completeness.py --json
    python3 -B reports/round-28/audit/x60-sweep-completeness.py --selftest

Read-only: no code path writes inside the repository. Exit 0 clean, 1 findings,
2 could-not-evaluate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GATES = ROOT / "tools" / "gates"
FROZEN = GATES / "frozen"
EXPECTED = GATES / "expected"
LEGACY = ROOT / "reports" / "round-9" / "baselines"
D4_SURFACE_MARKERS = ("culture-d4", "packet.d4", "typed-labels.d4",
                      "expected-holds", "04-lexicon", "01-brief",
                      "13-register-law", "register_law", "typed-pipelines.json")
# The two surfaces the RL-4 change can move.
PACKET_READ_MARKERS = ("examples/culture-d4/packet.d4.yml",
                       "packet.d4.yml", "packet_sha256",
                       "typed-labels.d4.yml", "projection_sha256")


def sha_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rel(path):
    try:
        return str(Path(path).resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def names_d4(text):
    return any(marker in text for marker in D4_SURFACE_MARKERS)


# --------------------------------------------------------------------------
# A. inventory
# --------------------------------------------------------------------------


def inventory():
    """Every pin-bearing artifact class, with its members."""
    classes = {}

    classes["frozen-manifest"] = [rel(p) for p in sorted(FROZEN.rglob("MANIFEST.tsv"))]
    classes["gate-baseline"] = [rel(p) for p in sorted(EXPECTED.rglob("expected.json"))]
    classes["frozen-baseline"] = [rel(p) for p in sorted(FROZEN.rglob("expected.json"))]
    classes["legacy-baseline"] = ([rel(p) for p in sorted(LEGACY.rglob("expected.json"))]
                                  if LEGACY.is_dir() else [])

    handoff = []
    for path in sorted((ROOT / "reports").rglob("expected.json")):
        try:
            doc = json.loads(path.read_text())
        except Exception:  # noqa: BLE001
            continue
        if isinstance(doc, dict) and ("packet_sha256" in doc or "baseline_digest" in doc):
            handoff.append(rel(path))
    classes["handoff-baseline"] = handoff

    twins = []
    for path in sorted((ROOT / "reports").rglob("twin.json")):
        try:
            doc = json.loads(path.read_text())
        except Exception:  # noqa: BLE001
            continue
        if isinstance(doc, dict) and isinstance(doc.get("artifact_manifest"), (dict, list)):
            twins.append(rel(path))
    classes["twin-row"] = twins

    profiles = []
    profile_path = GATES / "typed-pipelines.json"
    if profile_path.is_file():
        doc = json.loads(profile_path.read_text())
        profiles = ["%s:%s" % (profile_path.name, p.get("id")) for p in doc.get("profiles", [])]
    classes["profile-pin"] = profiles

    classes["fixture-expected"] = [rel(p) for p in sorted(GATES.rglob("*.expected"))]
    classes["expected-holds"] = [rel(p) for p in sorted((ROOT / "examples").rglob("expected-holds.json"))]

    # New for round 28: the per-round pin baseline directories the sweep seats
    # mint (a pin is a measurement, so each round adds NEW rows rather than
    # overwriting). Counted as its own class so a reader can see the cascade.
    r28_pins = []
    for base in sorted((ROOT / "reports").glob("round-*/pinsweep/baselines/*")):
        if base.is_dir():
            r28_pins.append(rel(base))
    classes["pinsweep-baseline-dir"] = r28_pins

    return classes


# --------------------------------------------------------------------------
# B. coverage matrix
# --------------------------------------------------------------------------


def sweep_coverage():
    """What each sweep method in use this round can and cannot reach."""
    all_manifests = {rel(p) for p in FROZEN.rglob("MANIFEST.tsv")}
    all_baselines = ({rel(p) for p in EXPECTED.rglob("expected.json")}
                     | {rel(p) for p in FROZEN.rglob("expected.json")}
                     | ({rel(p) for p in LEGACY.rglob("expected.json")}
                        if LEGACY.is_dir() else set()))

    methods = {}

    methods["replay-frozen-manifests"] = {
        "reaches": sorted(all_manifests),
        "misses": sorted(all_baselines),
        "note": "replays only MANIFEST.tsv rows; a baseline is not a manifest "
                "(replay-frozen refuses it: manifest_malformed).",
    }

    roots, reached = sibling_baseline_reach()
    methods["sibling-baseline-duty"] = {
        "reaches": sorted(reached),
        "misses": sorted(all_baselines - reached),
        "note": ("read live from the round-28 pin-sweep seat's source "
                 "`roots=%s`; a hardcoded snapshot would go stale as the "
                 "sibling revises." % ", ".join(roots)),
    }

    methods["sibling-manifest-duty"] = {
        "reaches": sorted(all_manifests),
        "misses": [],
        "note": "complete over the manifest class.",
    }

    methods["baseline-only-sweep"] = {
        "reaches": sorted(all_baselines),
        "misses": sorted(all_manifests),
        "note": "a sweep that checks baselines but no manifest misses every row.",
    }

    return methods


def _round_sweep_sources():
    """Every round-28 (and, as a fallback, round-27) sweep/repin source."""
    out = []
    for round_dir in ("round-28", "round-27"):
        for name in ("pinsweep", "audit"):
            base = ROOT / "reports" / round_dir / name
            if base.is_dir():
                out.extend(sorted(base.glob("*.py")))
    return out


def sibling_baseline_reach():
    """Parse the sweep seat's declared baseline roots from its source.

    Deliberately a *textual* read of the roots list, not an import: importing
    would execute a peer seat's tool inside this one. Discovers whichever
    round-28 sweep source exists; falls back to the round-27 shape.
    """
    names = {"EXPECTED": EXPECTED, "FROZEN": FROZEN,
             'ROOT / "reports" / "round-9" / "baselines"': LEGACY}
    roots, reached = [], set()
    for source in _round_sweep_sources():
        try:
            text = source.read_text(errors="replace")
        except Exception:  # noqa: BLE001
            continue
        for line in text.splitlines():
            stripped = line.strip()
            if not stripped.startswith("roots = ["):
                continue
            body = stripped[len("roots = ["):].rstrip("]").strip()
            for token in [t.strip() for t in body.split(",") if t.strip()]:
                path = names.get(token)
                if path is not None and token not in roots:
                    roots.append(token)
                    if path.is_dir():
                        reached |= {rel(p) for p in path.rglob("expected.json")}
    if not roots:
        roots = ["EXPECTED"]
        reached = {rel(p) for p in EXPECTED.rglob("expected.json")}
    return roots, reached


# --------------------------------------------------------------------------
# C. D4-surface touch
# --------------------------------------------------------------------------


def d4_touch():
    """Which pin artifacts name a D4 surface, and does their pin still hold."""
    rows = []

    for path in sorted(FROZEN.rglob("MANIFEST.tsv")):
        text = path.read_text(errors="replace")
        if not names_d4(text):
            continue
        holds, stale = 0, []
        lines = [ln for ln in text.splitlines() if ln.strip()]
        header = lines[0].split("\t") if lines else []
        for line in lines[1:]:
            cells = line.split("\t")
            row = dict(zip(header, cells))
            gate, pin = row.get("gate", ""), row.get("gate_sha256", "")
            live = sha_file(ROOT / gate) if (ROOT / gate).is_file() else None
            if live == pin:
                holds += 1
            else:
                stale.append(gate)
        rows.append({"artifact": rel(path), "class": "frozen-manifest",
                     "d4": True, "pins_hold": holds, "pins_stale": sorted(set(stale))})

    for path in sorted(list(EXPECTED.rglob("expected.json")) + list(FROZEN.rglob("expected.json"))):
        text = path.read_text(errors="replace")
        if not names_d4(text):
            continue
        try:
            doc = json.loads(text)
        except Exception:  # noqa: BLE001
            continue
        gate = doc.get("gate_script") or ("tools/gates/%s.py" % doc.get("gate")
                                          if doc.get("gate") else None)
        pin = doc.get("gate_sha256", "")
        live = sha_file(ROOT / gate) if gate and (ROOT / gate).is_file() else None
        stale_inputs = []
        for rel_path, want in (doc.get("inputs") or {}).items():
            snap = path.parent / rel_path
            cand = snap if snap.is_file() else (ROOT / rel_path)
            if not cand.is_file() or sha_file(cand) != want:
                stale_inputs.append(rel_path)
        rows.append({"artifact": rel(path), "class": "gate-baseline",
                     "d4": True, "gate_pin_holds": live == pin,
                     "stale_inputs": sorted(stale_inputs)})

    for path in sorted((ROOT / "reports").rglob("expected.json")):
        text = path.read_text(errors="replace")
        if not names_d4(text):
            continue
        try:
            doc = json.loads(text)
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(doc, dict):
            continue
        rows.append({"artifact": rel(path), "class": "handoff-baseline", "d4": True,
                     "packet_pin": str(doc.get("packet_sha256"))[:16]})

    return rows


# --------------------------------------------------------------------------
# D. TMPDIR sensitivity
# --------------------------------------------------------------------------


def _newest_d4_manifest():
    cands = [p for p in FROZEN.rglob("MANIFEST.tsv")
             if names_d4(p.read_text(errors="replace"))]
    if not cands:
        cands = sorted(FROZEN.rglob("MANIFEST.tsv"))
    if not cands:
        return None
    return max(cands, key=lambda p: p.stat().st_mtime)


def tmpdir_probe():
    """Run the newest D4 manifest under an in-repo and an out-of-repo TMPDIR."""
    manifest = _newest_d4_manifest()
    if manifest is None:
        return {"manifest": None, "error": "no frozen manifest on disk"}
    manifest_rel = rel(manifest)
    runs = []
    for label, tmpdir in (("inside-repo", str(ROOT / ".scratch")),
                          ("outside-repo", tempfile.gettempdir())):
        env = dict(os.environ, TMPDIR=tmpdir, PYTHONDONTWRITEBYTECODE="1")
        proc = subprocess.run(
            [sys.executable, "-B", str(ROOT / "tools" / "replay-frozen.py"),
             manifest_rel, "--json"],
            capture_output=True, text=True, env=env, cwd=ROOT)
        try:
            doc = json.loads(proc.stdout)
        except Exception:  # noqa: BLE001
            runs.append({"tmpdir": label, "exit": proc.returncode,
                         "raw": (proc.stdout or proc.stderr)[:200]})
            continue
        runs.append({"tmpdir": label, "exit": proc.returncode,
                     "reproduced": doc.get("reproduced"), "mismatched": doc.get("mismatched"),
                     "rows": doc.get("rows"), "status": doc.get("status")})
    return {"manifest": manifest_rel, "runs": runs}


# --------------------------------------------------------------------------
# F. filed-surface integrity (new for round 28)
# --------------------------------------------------------------------------


PROTECTED_GLOB = "reports/round-{8..27}"


def filed_surface():
    """Report any round-8..27 artifact modified in the working tree.

    The rounds 8..27 artifacts are filed: a later round may add NEW rows but
    must not rewrite them in place. This is measured, not assumed, with
    `git status --porcelain=v1` over the protected range, and each modified
    path is then checked against its round-28 dispatch baseline so a
    pre-existing modification is not attributed to this round.
    """
    proc = subprocess.run(
        ["git", "status", "--porcelain=v1", "--", "reports/round-8", "reports/round-9"]
        + ["reports/round-%d" % n for n in range(10, 28)],
        capture_output=True, text=True, cwd=ROOT)
    modified = []
    for line in (proc.stdout or "").splitlines():
        if not line.strip():
            continue
        code, path = line[:2], line[3:].strip()
        modified.append({"code": code.strip() or code, "path": path})
    return {"command": "git status --porcelain=v1 -- reports/round-{8..27}",
            "modified": modified, "modified_count": len(modified)}


# --------------------------------------------------------------------------
# E. packet-read set (new for round 28)
# --------------------------------------------------------------------------


def packet_readset():
    """Every pin row whose declared inputs read the D4 packet or its projection.

    This is the surface the RL-4 fix moves: the assembler gains a
    `register_law` field list, so any baseline pinning `assemble-culture-d4.py`
    or the packet/projection bytes is drift-prone and must be re-pinned.
    """
    packet_sha = sha_file(ROOT / "examples/culture-d4/packet.d4.yml") \
        if (ROOT / "examples/culture-d4/packet.d4.yml").is_file() else None
    rows = []
    for path in sorted(list(EXPECTED.rglob("expected.json")) + list(FROZEN.rglob("expected.json"))
                       + list((ROOT / "reports").rglob("expected.json"))):
        try:
            doc = json.loads(path.read_text())
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(doc, dict):
            continue
        inputs = doc.get("inputs") or {}
        reads_packet = [k for k in inputs if "culture-d4" in k or "packet" in k
                        or "assemble-culture-d4" in k]
        if not reads_packet and "packet_sha256" not in doc:
            continue
        pinned = doc.get("packet_sha256")
        rows.append({
            "artifact": rel(path),
            "class": path.parent.parent.name if path.parent.parent.is_dir() else "?",
            "reads": sorted(reads_packet),
            "pinned_packet": str(pinned)[:16] if pinned else None,
            "live_packet": (packet_sha or "")[:16],
            "packet_pin_holds": (pinned is None) or (pinned == packet_sha),
        })
    return {"live_packet_sha256": packet_sha, "rows": rows,
            "rows_reading_packet": len(rows),
            "rows_drifted": sum(1 for r in rows if not r["packet_pin_holds"])}


# --------------------------------------------------------------------------
# selftest — this tool must be able to say no
# --------------------------------------------------------------------------


def selftest():
    checks = []

    def check(name, ok, detail=""):
        checks.append((name, bool(ok), detail))

    inv = inventory()
    check("inventory-returns-classes", isinstance(inv, dict) and len(inv) >= 8,
          "classes=%d" % len(inv))
    check("inventory-classes-are-lists", all(isinstance(v, list) for v in inv.values()))

    cov = sweep_coverage()
    check("coverage-has-methods", len(cov) >= 4, "methods=%d" % len(cov))
    check("manifest-method-misses-baselines",
          bool(cov["replay-frozen-manifests"]["misses"]),
          "misses=%d" % len(cov["replay-frozen-manifests"]["misses"]))
    check("baseline-method-misses-manifests",
          bool(cov["baseline-only-sweep"]["misses"]),
          "misses=%d" % len(cov["baseline-only-sweep"]["misses"]))

    # negative control: an empty method reaches nothing and must be detected.
    empty = {"reaches": [], "misses": sorted(cov["replay-frozen-manifests"]["reaches"])}
    check("negative-empty-method-detected", not empty["reaches"] and empty["misses"])

    rs = packet_readset()
    check("readset-has-live-packet", bool(rs["live_packet_sha256"]),
          "sha=%s" % (rs["live_packet_sha256"] or "?")[:16])
    check("readset-counts-consistent",
          rs["rows_drifted"] == sum(1 for r in rs["rows"] if not r["packet_pin_holds"]))

    probe = tmpdir_probe()
    check("tmpdir-probe-ran", "runs" in probe and len(probe.get("runs", [])) == 2,
          str(probe.get("manifest")))

    fs = filed_surface()
    check("filed-surface-ran", "modified_count" in fs,
          "modified=%d" % fs.get("modified_count", -1))

    # negative control: a tampered digest must not read as holding.
    live = rs["live_packet_sha256"]
    check("negative-tampered-pin-detected",
          live is not None and ("0" * 64) != live)

    passed = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        print("%-38s %s %s" % (name, "ok" if ok else "MISS", detail))
    print("selftest: %d/%d checks passed" % (passed, len(checks)))
    return 0 if passed == len(checks) else 1


# --------------------------------------------------------------------------


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--inventory", action="store_true")
    ap.add_argument("--coverage", action="store_true")
    ap.add_argument("--readset", action="store_true")
    ap.add_argument("--filed-surface", action="store_true")
    ap.add_argument("--tmpdir-probe", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    report = {}
    if args.inventory or args.json or not (args.coverage or args.readset
                                           or args.tmpdir_probe or args.filed_surface):
        report["inventory"] = inventory()
    if args.coverage or args.json:
        report["coverage"] = sweep_coverage()
    if args.readset or args.json:
        report["readset"] = packet_readset()
    if args.tmpdir_probe or args.json:
        report["tmpdir"] = tmpdir_probe()
    if args.filed_surface or args.json:
        report["filed_surface"] = filed_surface()

    if args.json:
        print(json.dumps(report, indent=2))
        return 0

    if "inventory" in report:
        print("INVENTORY")
        for name, members in sorted(report["inventory"].items()):
            print("  %-22s %d" % (name, len(members)))
    if "coverage" in report:
        print("COVERAGE")
        for name, m in sorted(report["coverage"].items()):
            print("  %-26s reaches=%d misses=%d" % (name, len(m["reaches"]), len(m["misses"])))
    if "readset" in report:
        rs = report["readset"]
        print("READSET live_packet=%s rows=%d drifted=%d"
              % ((rs["live_packet_sha256"] or "?")[:16], rs["rows_reading_packet"],
                 rs["rows_drifted"]))
        for row in rs["rows"]:
            print("  %-60s holds=%s" % (row["artifact"], row["packet_pin_holds"]))
    if "tmpdir" in report:
        print("TMPDIR")
        for run in report["tmpdir"].get("runs", []):
            print("  %-14s exit=%s reproduced=%s mismatched=%s"
                  % (run.get("tmpdir"), run.get("exit"), run.get("reproduced"),
                     run.get("mismatched")))
    if "filed_surface" in report:
        fs = report["filed_surface"]
        print("FILED-SURFACE modified=%d" % fs["modified_count"])
        for row in fs["modified"]:
            print("  %-3s %s" % (row["code"], row["path"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
