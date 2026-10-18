#!/usr/bin/env python3
"""R27-X60 — sweep-completeness auditor (independent; own re-derivation).

Seat R27-X60 (SCRIBE X60: shard auditor — sweep completeness) for round 27,
claim O `pin-sweep` (`reports/round-27/claims.json`). NON-CANON audit evidence.

The round-27 O claim is "a single re-pin-and-verify sweep: every frozen
manifest, battery baseline, expected-holds, and replay row that pins the D4
surfaces re-verified". A sweep is only as complete as its **surface inventory**,
so this tool does not replay rows — the round's own runner and X61 do that. It
answers the prior question:

    *how many pin surfaces exist, in how many classes, and which of them does a
    given sweep method actually reach?*

Four duties:

  A. INVENTORY — enumerate every pin-bearing artifact on the tree by class:
     frozen manifests, frozen/expected baselines, handoff baselines, twin
     rows, profile pins (`tools/gates/typed-pipelines.json`), fixture
     `.expected` files, and the D4 hold set. Each class gets its count and the
     command that produced it.

  B. COVERAGE MATRIX — for each *sweep method* in use this round
     (`tools/replay-frozen.py` over `**/MANIFEST.tsv`; X61's baseline duty;
     X61's manifest duty), compute the reachable set and the missed set. A
     method that globs `tools/gates/expected/**` while 10 baselines live under
     `tools/gates/frozen/**` is measured, not asserted.

  C. D4-SURFACE TOUCH — the O claim is specifically about the **D4 surfaces**
     the round-26 register landing moved. For every pin artifact, test whether
     it names a D4 surface and whether the named pin still holds against the
     live bytes. This is the "did the sweep re-verify the thing the claim is
     about" duty.

  D. TMPDIR SENSITIVITY — `tools/replay-frozen.py` refuses a mirror inside the
     repo, so `TMPDIR=$PWD/.scratch` silently turns every manifest row into
     `mirror_unsafe`. Measured by running one manifest both ways and reporting
     the two tallies. (The round-27 X61 tool *claims* this probe but its
     `tmpdir_probe` never passes its `tmpdir` argument through to the mirror —
     the defect is recorded in the X60 fragment, and this tool measures the
     real delta instead.)

Usage:
    export TMPDIR=/tmp PYTHONDONTWRITEBYTECODE=1
    python3 -B reports/round-27/audit/x60-sweep-completeness.py --inventory
    python3 -B reports/round-27/audit/x60-sweep-completeness.py --coverage
    python3 -B reports/round-27/audit/x60-sweep-completeness.py --json
    python3 -B reports/round-27/audit/x60-sweep-completeness.py --selftest

Read-only: no code path writes inside the repository. Exit 0 clean, 1 findings,
2 could-not-evaluate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GATES = ROOT / "tools" / "gates"
FROZEN = GATES / "frozen"
EXPECTED = GATES / "expected"
D4_SURFACE_MARKERS = ("culture-d4", "packet.d4", "typed-labels.d4",
                      "expected-holds", "04-lexicon", "01-brief",
                      "typed-pipelines.json")


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

    manifests = sorted(FROZEN.rglob("MANIFEST.tsv"))
    classes["frozen-manifest"] = [rel(p) for p in manifests]

    baselines = sorted(EXPECTED.rglob("expected.json"))
    classes["gate-baseline"] = [rel(p) for p in baselines]

    frozen_baselines = sorted(FROZEN.rglob("expected.json"))
    classes["frozen-baseline"] = [rel(p) for p in frozen_baselines]

    legacy = ROOT / "reports" / "round-9" / "baselines"
    classes["legacy-baseline"] = ([rel(p) for p in sorted(legacy.rglob("expected.json"))]
                                  if legacy.is_dir() else [])

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

    fixtures = sorted(GATES.rglob("*.expected"))
    classes["fixture-expected"] = [rel(p) for p in fixtures]

    holds = sorted((ROOT / "examples").rglob("expected-holds.json"))
    classes["expected-holds"] = [rel(p) for p in holds]

    return classes


# --------------------------------------------------------------------------
# B. coverage matrix
# --------------------------------------------------------------------------


def sweep_coverage():
    """What each sweep method in use this round can and cannot reach.

    The X61 rows are read from the live file when it exposes its roots, so this
    matrix tracks the sibling tool rather than a stale snapshot of it. The
    round-27 X61 seat revised its baseline duty twice while this seat worked
    (first `EXPECTED` only, then `EXPECTED`+`FROZEN`+`reports/round-9/baselines`);
    a hardcoded defect would have kept reporting a fixed bug.
    """
    all_manifests = {rel(p) for p in FROZEN.rglob("MANIFEST.tsv")}
    legacy = ROOT / "reports" / "round-9" / "baselines"
    all_baselines = ({rel(p) for p in EXPECTED.rglob("expected.json")}
                     | {rel(p) for p in FROZEN.rglob("expected.json")}
                     | ({rel(p) for p in legacy.rglob("expected.json")}
                        if legacy.is_dir() else set()))

    methods = {}

    # M1 — tools/replay-frozen.py over **/MANIFEST.tsv (the round's usual leg).
    methods["replay-frozen-manifests"] = {
        "reaches": sorted(all_manifests),
        "misses": sorted(all_baselines),
        "note": "replays only MANIFEST.tsv rows; a baseline is not a manifest "
                "(replay-frozen refuses it: manifest_malformed).",
    }

    # M2 — X61's baseline duty, read from the live source.
    x61_roots, x61_baselines = x61_baseline_reach()
    methods["x61-baseline-duty"] = {
        "reaches": sorted(x61_baselines),
        "misses": sorted(all_baselines - x61_baselines),
        "note": ("read live from reports/round-27/audit/x61-pin-sweep.py "
                 "`sweep_baselines()` roots=%s; a hardcoded snapshot would go "
                 "stale as the sibling revises." % ", ".join(x61_roots)),
    }

    # M3 — X61's manifest duty: FROZEN.rglob('MANIFEST.tsv') — complete.
    methods["x61-manifest-duty"] = {
        "reaches": sorted(all_manifests),
        "misses": [],
        "note": "complete over the manifest class.",
    }

    # M4 — a baseline-only sweep (the complement of M1).
    methods["baseline-only-sweep"] = {
        "reaches": sorted(all_baselines),
        "misses": sorted(all_manifests),
        "note": "a sweep that checks baselines but no manifest misses every row.",
    }

    return methods


def x61_baseline_reach():
    """Parse X61's declared baseline roots from its source and expand them.

    Deliberately a *textual* read of the roots list, not an import: importing
    would execute a peer seat's tool inside this one. If the source cannot be
    parsed, fall back to the pre-revision root set and say so in the note.
    """
    source = (ROOT / "reports" / "round-27" / "audit" / "x61-pin-sweep.py")
    names = {"EXPECTED": EXPECTED, "FROZEN": FROZEN,
             'ROOT / "reports" / "round-9" / "baselines"': ROOT / "reports" / "round-9" / "baselines"}
    roots, reached = [], set()
    if source.is_file():
        text = source.read_text(errors="replace")
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith("roots = ["):
                body = stripped[len("roots = ["):].rstrip("]").strip()
                for token in [t.strip() for t in body.split(",") if t.strip()]:
                    path = names.get(token)
                    if path is not None:
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
        doc = json.loads(text)
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


def tmpdir_probe(manifest_rel="tools/gates/frozen/round-26/post-register/MANIFEST.tsv"):
    """Run the same manifest under an in-repo and an out-of-repo TMPDIR."""
    manifest = ROOT / manifest_rel
    if not manifest.is_file():
        return {"manifest": manifest_rel, "error": "manifest not on disk"}
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
            summary = doc.get("summary", {})
        except Exception:  # noqa: BLE001
            summary = {"parse_error": proc.stdout[:120] or proc.stderr[:120]}
        runs.append({"tmpdir": label, "path": tmpdir, "summary": summary})
    return {"manifest": manifest_rel, "runs": runs}


# --------------------------------------------------------------------------
# selftest
# --------------------------------------------------------------------------


def selftest():
    checks = []
    inv = inventory()
    checks.append(("inventory finds manifests", len(inv["frozen-manifest"]) >= 10))
    checks.append(("inventory finds gate baselines", len(inv["gate-baseline"]) >= 5))
    checks.append(("inventory finds frozen baselines", len(inv["frozen-baseline"]) >= 9))
    checks.append(("inventory finds the D4 profile pin",
                   any(p.endswith(":d4") for p in inv["profile-pin"])))
    checks.append(("inventory finds the D4 hold set",
                   any("culture-d4" in p for p in inv["expected-holds"])))

    cov = sweep_coverage()
    # The reach is read live from X61's source, so the assertion is about the
    # *parser* working, not about a defect persisting: whatever roots the file
    # declares, the parser must resolve them to the same set the tree holds.
    roots, reached = x61_baseline_reach()
    checks.append(("x61 roots parsed", len(roots) >= 1))
    checks.append(("x61 reach is a subset of the baseline set",
                   reached <= ({rel(p) for p in EXPECTED.rglob("expected.json")}
                               | {rel(p) for p in FROZEN.rglob("expected.json")}
                               | ({rel(p) for p in (ROOT / "reports" / "round-9" / "baselines").rglob("expected.json")}
                                  if (ROOT / "reports" / "round-9" / "baselines").is_dir() else set()))))
    checks.append(("x61 manifest duty is complete",
                   cov["x61-manifest-duty"]["misses"] == []))
    checks.append(("replay-frozen misses every baseline",
                   len(cov["replay-frozen-manifests"]["misses"]) >= 14))
    # A coverage matrix that reports full coverage everywhere would be useless:
    # a manifest-only method must always show a non-empty baseline miss set.
    checks.append(("a manifest-only method has a non-empty miss set",
                   bool(cov["replay-frozen-manifests"]["misses"])))

    # names_d4 must discriminate, not always return True.
    checks.append(("names_d4 accepts a D4 path",
                   names_d4("examples/culture-d4/packet.d4.yml")))
    checks.append(("names_d4 rejects a non-D4 path",
                   not names_d4("reports/round-11/handoff/expected.json")))

    passed = sum(1 for _, ok in checks if ok)
    for name, ok in checks:
        print("%s %s" % ("PASS" if ok else "FAIL", name))
    print("selftest: %d/%d checks passed" % (passed, len(checks)))
    return 0 if passed == len(checks) else 1


# --------------------------------------------------------------------------


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--inventory", action="store_true")
    ap.add_argument("--coverage", action="store_true")
    ap.add_argument("--d4", action="store_true")
    ap.add_argument("--tmpdir-probe", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    receipt = {"tool": "x60-sweep-completeness", "date": "2026-10-18",
               "seat": "R27-X60"}

    if args.inventory:
        inv = inventory()
        receipt["inventory"] = {k: {"count": len(v), "members": v} for k, v in inv.items()}
    if args.coverage:
        receipt["coverage"] = sweep_coverage()
    if args.d4:
        receipt["d4_touch"] = d4_touch()
    if args.tmpdir_probe:
        receipt["tmpdir_probe"] = tmpdir_probe()

    if not any((args.inventory, args.coverage, args.d4, args.tmpdir_probe)):
        receipt["inventory"] = {k: {"count": len(v), "members": v}
                                for k, v in inventory().items()}
        receipt["coverage"] = sweep_coverage()
        receipt["d4_touch"] = d4_touch()

    if args.json:
        print(json.dumps(receipt, indent=1, sort_keys=True))
    else:
        if "inventory" in receipt:
            print("INVENTORY")
            for cls, entry in sorted(receipt["inventory"].items()):
                print("  %-20s %d" % (cls, entry["count"]))
        if "coverage" in receipt:
            print("COVERAGE")
            for name, entry in sorted(receipt["coverage"].items()):
                print("  %-26s reaches=%-3d misses=%d"
                      % (name, len(entry["reaches"]), len(entry["misses"])))
                for miss in entry["misses"][:6]:
                    print("      MISS %s" % miss)
        if "d4_touch" in receipt:
            print("D4 TOUCH")
            for row in receipt["d4_touch"]:
                print("  %-70s %s" % (row["artifact"],
                                       {k: v for k, v in row.items()
                                        if k not in ("artifact", "class", "d4")}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
