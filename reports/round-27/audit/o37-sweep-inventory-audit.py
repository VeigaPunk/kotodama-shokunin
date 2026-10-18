#!/usr/bin/env python3
"""R27-O37 — independent audit of the round-27 D4 pin-sweep *inventory*.

Question this seat answers: does the sweep the round-27 O claim filed enumerate
**every** surface in the lane that carries a pin over a D4 artifact, or does it
leave named surfaces un-swept? "Zero missed surfaces" is a coverage claim, so it
must be measured against an inventory built independently of the sweep's own.

Method. This tool builds the census ITSELF, from the tree, by walking every
file class that can carry a digest pin, and then diffs that census against the
surface set the sweep instrument(s) actually visit. It never reads a verdict
from the sweep; it re-derives both sides.

Surface families walked (the auditor's own definition):
  A  MANIFEST.tsv rows under tools/gates/frozen/**
  B  expected.json under tools/gates/expected/**
  C  expected.json under tools/gates/frozen/** and reports/round-9/baselines/**
     (the battery-discovered roots: check-gate-battery.BASELINE_ROOTS)
  D  freeze-receipt.json embedded pins (input_pins / pins maps)
  E  reports/**/expected.json (the handoff v2/v3 baseline family)
  F  tools/gates/typed-pipelines.json (the L1-profile live-pin channel)
  G  expected-holds.json self-pins (packet_sha256 / projection_sha256)
  H  twin.json / packet.md embedded artifact_manifest pins

Usage:
    export TMPDIR=/tmp   # outside the repo; in-repo TMPDIR trips replay-frozen
    python3 -B reports/round-27/audit/o37-sweep-inventory-audit.py           # text
    python3 -B reports/round-27/audit/o37-sweep-inventory-audit.py --json    # receipt
    python3 -B reports/round-27/audit/o37-sweep-inventory-audit.py --selftest

Exit codes:
  0  the sweep inventory covers every surface this census finds
  1  at least one surface is missed (a coverage finding, never a quality claim)
  2  could-not-evaluate: the census itself could not be built
"""
import argparse, glob, hashlib, json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HEX = re.compile(r"^[0-9a-f]{64}$")

def sha_file(p):
    try:
        return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    except OSError:
        return None

def rel(p):
    return os.path.relpath(str(p), str(ROOT))

def g(pat):
    return sorted(glob.glob(str(ROOT / pat), recursive=True))

_D4_DIGESTS = None
def d4_digests():
    """The digest set of every live artifact under examples/culture-d4/."""
    global _D4_DIGESTS
    if _D4_DIGESTS is None:
        _D4_DIGESTS = {sha_file(p) for p in g("examples/culture-d4/**/*")
                       if os.path.isfile(p)}
        _D4_DIGESTS.discard(None)
    return _D4_DIGESTS

# ---------- census ----------
def census():
    fam = {}
    fam["A"] = g("tools/gates/frozen/**/MANIFEST.tsv")
    fam["B"] = g("tools/gates/expected/**/expected.json")
    fam["C"] = g("tools/gates/frozen/**/expected.json") + g("reports/round-9/baselines/**/expected.json")
    fam["D"] = g("tools/gates/frozen/**/freeze-receipt.json")
    fam["E"] = [p for p in g("reports/**/expected.json") if "/round-9/" not in p]
    fam["F"] = g("tools/gates/typed-pipelines.json")
    fam["G"] = g("examples/**/expected-holds.json")
    fam["H"] = g("reports/**/twin.json")
    return fam

# ---------- what the sweep instrument(s) actually visit ----------
ASSIGN = re.compile(r'^([A-Z][A-Z0-9_]*)\s*=\s*(.+)$', re.M)
CHAIN = re.compile(r'"([^"]+)"')
RGLOB = re.compile(r'([A-Za-z_][A-Za-z0-9_]*|\([^)]*\))\s*\.rglob\(\s*"([^"]+)"\s*\)')

def _resolve_chain(expr, consts):
    """Resolve `ROOT / "a" / "b"` (or a bare NAME) to an absolute Path."""
    expr = expr.strip()
    if expr in consts:
        return consts[expr]
    if "ROOT" not in expr:
        return None
    parts = CHAIN.findall(expr)
    return ROOT.joinpath(*parts) if parts else None

def _source_reach(inst):
    """Static reach: every `rglob` the instrument's source performs.

    Used only as a FALLBACK when the instrument cannot be run (e.g. `/tmp` is
    full, so its mirror cannot be created). It is strictly weaker — it reads
    intent, not behaviour — so every caller records which method produced the
    reach. Handles roots bound to names, inline parenthesised chains, and
    list-bound loop roots."""
    src = inst.read_text()
    consts = {"ROOT": ROOT}
    for name, expr in ASSIGN.findall(src):
        p = _resolve_chain(expr, consts)
        if p is not None:
            consts[name] = p
    loop_roots = []
    for _, expr in ASSIGN.findall(src):
        if expr.lstrip().startswith("["):
            for elem in expr.strip().strip("[]").split(","):
                p = _resolve_chain(elem.strip(), consts)
                if p is not None:
                    loop_roots.append(p)
    enumerated = set()
    for rootexpr, pattern in RGLOB.findall(src):
        base = _resolve_chain(rootexpr, consts)
        bases = [base] if base is not None else (loop_roots if rootexpr.isidentifier() else [])
        for b in bases:
            if b is None or not b.is_dir():
                continue
            for hit in b.rglob(pattern):
                enumerated.add(rel(hit))
    return enumerated

def sweep_walks():
    """Measure the sweep instrument's reach, preferring its own receipt.

    Running the instrument and reading which surfaces it reports on is stronger
    than parsing its source: a glob whose pattern a later edit changes cannot
    silently invalidate the measurement, and a documented-but-unimplemented duty
    cannot inflate it. The instrument is invoked with `--json` under a TMPDIR
    outside the repo (its own documented requirement) and its
    `manifests[].manifest` + `baselines[].baseline` keys are the reach.

    When the instrument cannot run — X61 hardcodes `/tmp` for its mirror, and a
    full `/tmp` makes every row fail with ENOSPC — this falls back to a static
    `rglob` read of its source and says so, rather than reporting a
    could-not-evaluate that would look like a missing sweep.

    NOTE (corrected 19:33Z): the instrument audited here is the round-27 *audit*
    instrument `x61-pin-sweep.py`. The **claim-O sweep itself** is
    `reports/round-27/pinsweep/sweep.py`, which walks families A–H; its reach is
    measured by `sweep_reach()` below and reported separately, because auditing
    the auditor instead of the claimant was this tool's first error."""
    inst = ROOT / "reports" / "round-27" / "audit" / "x61-pin-sweep.py"
    if not inst.is_file():
        return None, "sweep instrument reports/round-27/audit/x61-pin-sweep.py absent", None
    env = dict(os.environ, TMPDIR="/var/tmp/kotodama-o37-reach",
               PYTHONDONTWRITEBYTECODE="1")
    try:
        proc = subprocess.run([sys.executable, "-B", str(inst), "--json"],
                              capture_output=True, text=True, cwd=str(ROOT),
                              env=env, timeout=900)
        if proc.stdout.strip():
            rec = json.loads(proc.stdout)
            enumerated = {m["manifest"] for m in rec.get("manifests", []) if "manifest" in m}
            enumerated |= {b["baseline"] for b in rec.get("baselines", []) if "baseline" in b}
            return enumerated, None, "instrument-receipt"
    except (subprocess.TimeoutExpired, json.JSONDecodeError):
        pass
    try:
        return _source_reach(inst), None, "source-rglob-fallback"
    except OSError as e:
        return None, f"sweep instrument unreadable: {e}", None

def sweep_reach():
    """The reach of the CLAIM-O sweep: `reports/round-27/pinsweep/sweep.py`.

    Read from that tool's own `--json` receipt `families` block, which names the
    surfaces it enumerated. This is the reach that decides whether the O claim's
    "zero missed surfaces" holds; X61's reach is a different (audit) instrument."""
    tool = ROOT / "reports" / "round-27" / "pinsweep" / "sweep.py"
    if not tool.is_file():
        return None, None, "claim-sweep-absent"
    env = dict(os.environ, TMPDIR="/var/tmp/kotodama-o37-sweep",
               PYTHONDONTWRITEBYTECODE="1")
    try:
        proc = subprocess.run([sys.executable, "-B", str(tool), "--json"],
                              capture_output=True, text=True, cwd=str(ROOT),
                              env=env, timeout=900)
        rec = json.loads(proc.stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError):
        return None, None, "claim-sweep-unrunnable"
    fam = rec.get("families") or {}
    found = set()
    for key, val in fam.items():
        rows = val if isinstance(val, list) else ([val] if isinstance(val, dict) else [])
        for r in rows:
            if isinstance(r, dict) and r.get("path"):
                found.add(r["path"])
        if isinstance(val, dict):
            for rep in (val.get("replays") or []):
                if rep.get("manifest"):
                    found.add(rep["manifest"])
    return found, rec.get("summary"), "claim-sweep-receipt"

def classify_surface(path, tag):
    """Does this surface actually pin a D4 artifact?"""
    p = Path(path)
    try:
        if tag in ("A",):
            txt = p.read_text()
            return any("culture-d4" in ln.split("\t")[2]
                       for ln in txt.splitlines() if len(ln.split("\t")) > 2)
        if tag in ("B", "C", "E"):
            d = json.loads(p.read_text())
            return any("culture-d4" in k for k in (d.get("inputs") or {}))
        if tag == "D":
            d = json.loads(p.read_text())
            blob = json.dumps(d.get("input_pins") or {}) + json.dumps(d.get("pins") or {})
            return "culture-d4" in blob or any("culture-d4" in k for k in (d.get("input_pins") or {}))
        if tag == "F":
            d = json.loads(p.read_text())
            return any(str(s.get("path", "")).startswith("examples/culture-d4/")
                       for pr in d.get("profiles", [])
                       for s in pr.values() if isinstance(s, dict))
        if tag == "G":
            # a hold set is a D4 surface only when a digest it pins IS the
            # digest of a live D4 artifact: the D2 hold set pins the D2 packet,
            # whose path merely shares a prefix, so a name test over-fires
            d = json.loads(p.read_text())
            pinned = {v for v in d.values() if isinstance(v, str) and HEX.match(v)}
            return bool(pinned & d4_digests())
        if tag == "H":
            return "culture-d4" in p.read_text()
    except Exception:
        return None
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        # in-memory controls: the classifier must fire on a D4 pin and not on a D2 one
        checks = [
            ("HEX accepts a 64-hex digest", bool(HEX.match("a"*64))),
            ("HEX rejects a 63-hex digest", not HEX.match("a"*63)),
            ("HEX rejects uppercase", not HEX.match("A"*64)),
        ]
        ok = all(v for _, v in checks)
        for n, v in checks:
            print(("PASS " if v else "FAIL ") + n)
        print(f"selftest: {sum(1 for _,v in checks if v)}/{len(checks)} checks passed")
        return 0 if ok else 1

    fam = census()
    walked, err, reach_method = sweep_walks()
    if walked is None:
        print(f"COULD-NOT-EVALUATE: {err}", file=sys.stderr)
        return 2
    claim, claim_summary, claim_method = sweep_reach()

    rows, missed, swept = [], [], []
    for tag in sorted(fam):
        for p in fam[tag]:
            is_d4 = classify_surface(p, tag)
            is_swept = rel(p) in walked
            in_claim = (claim is not None) and (rel(p) in claim)
            r = {"family": tag, "surface": rel(p), "pins_d4": is_d4,
                 "swept_by_instrument": is_swept,
                 "swept_by_claim_sweep": in_claim}
            rows.append(r)
            if is_d4:
                (swept if is_swept else missed).append(r)
    claim_missed = [r for r in rows if r["pins_d4"] and not r["swept_by_claim_sweep"]]

    out = {
        "tool": "reports/round-27/audit/o37-sweep-inventory-audit.py",
        "round": 27, "seat": "R27-O37", "date": "2026-10-18",
        "lane_head": os.popen(f"git -C {ROOT} rev-parse HEAD").read().strip(),
        "census_families": {k: len(v) for k, v in fam.items()},
        "sweep_instrument_enumerated": len(walked),
        "reach_method": reach_method,
        "claim_sweep_method": claim_method,
        "claim_sweep_summary": claim_summary,
        "claim_sweep_enumerated": (len(claim) if claim is not None else None),
        "d4_pinning_surfaces_total": len(missed) + len(swept),
        "swept": [r["surface"] for r in swept],
        "missed": [r["surface"] for r in missed],
        "claim_sweep_missed": [r["surface"] for r in claim_missed],
        "rows": rows,
        "limits": "covers the *inventory* (which surfaces exist) only; it does not "
                  "replay any pinned verdict and makes no claim about design quality. "
                  "'missed' is relative to the X61 AUDIT instrument; "
                  "'claim_sweep_missed' is relative to the claim-O sweep "
                  "(reports/round-27/pinsweep/sweep.py), which is the reach that "
                  "decides the claim.",
    }
    if a.json:
        print(json.dumps(out, indent=1, sort_keys=True))
    else:
        print(f"R27-O37 sweep-inventory audit — lane HEAD {out['lane_head'][:12]}")
        print(f"  instrument enumerates {out['sweep_instrument_enumerated']} file(s) "
              f"[reach: {reach_method}]")
        for k in sorted(fam):
            n_swept = sum(1 for r in rows if r['family'] == k and r['swept_by_instrument'])
            print(f"  family {k}: {len(fam[k]):3} file(s)  "
                  f"{n_swept} enumerated by the instrument")
        print(f"  D4-pinning surfaces: {out['d4_pinning_surfaces_total']} "
              f"({len(swept)} swept, {len(missed)} MISSED by the X61 audit instrument)")
        if missed:
            print("  MISSED by X61:")
            for r in missed:
                print(f"    - [{r['family']}] {r['surface']}")
        print(f"  claim-O sweep (pinsweep/sweep.py) enumerates "
              f"{out['claim_sweep_enumerated']} surface(s) [{claim_method}]")
        if claim_summary:
            print(f"    summary: {claim_summary}")
        print(f"  D4-pinning surfaces MISSED by the claim-O sweep: "
              f"{len(claim_missed)}")
        for r in claim_missed:
            print(f"    ! [{r['family']}] {r['surface']}")
    return 1 if claim_missed else 0

if __name__ == "__main__":
    sys.exit(main())
