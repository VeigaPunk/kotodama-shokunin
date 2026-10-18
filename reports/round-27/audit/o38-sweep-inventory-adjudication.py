#!/usr/bin/env python3
"""R27-O38 — independent adjudication of the R27-O37 sweep-inventory census.

Seat R27-O38 is the second of the two sweep auditors. O37 built the inventory
and filed it; this tool re-verifies that inventory **row by row, with its own
resolver**, and reports where it agrees and where it does not. It is an
adjudicator, not a second enumerator: two enumerators built on the same idea
agree by construction, so a second *enumeration* would prove nothing. What a
second auditor can independently establish is whether each of O37's claims about
a surface survives a different read of the same bytes.

Four duties:

  A. PIN CLAIM — for every surface O37 marked `pins_d4`, independently resolve
     the pin: read the file, extract the digest it asserts for each D4 path,
     measure the live bytes, and report `holds` / `stale` / `unresolvable`.
     O37's census is about *which surfaces exist*; this is about whether the
     classification is real.

  B. REACH CLAIM — for every surface O37 marked swept/missed, independently
     re-derive the reach: run the sweep instrument and read its receipt. O37
     does this too, but on a different run; agreement across two runs is the
     evidence that reach is stable rather than a snapshot artifact.

  C. MISSED-SET ADJUDICATION — take O37's 20 missed surfaces and, for each,
     answer the operative question the claim needs: *is this surface actually
     stale against live bytes, or does it merely look stale?* A missed surface
     whose pins all hold is a coverage observation; a missed surface whose pins
     are stale is a live finding. The two are not the same and O37's fragment
     should not be read as if they were.

  D. FALSE-POSITIVE HUNT — probe families that a filename walk could plausibly
     omit and that O37 did not enumerate, and report whether any carries an
     independent D4 pin: `.expected` fixture files, `run.log` transcripts,
     `packet.md` renders, `freeze.txt` rows, and `evidence/*.json` receipts.

Usage:
    export TMPDIR=/var/tmp   # outside the repo
    python3 -B reports/round-27/audit/o38-sweep-inventory-adjudication.py
    python3 -B reports/round-27/audit/o38-sweep-inventory-adjudication.py --json
    python3 -B reports/round-27/audit/o38-sweep-inventory-adjudication.py --selftest

Exit codes:
  0  every adjudicated row agreed with O37's census
  1  at least one row disagreed, or the false-positive hunt found an un-enumerated
     D4 pin surface (a coverage finding, never a quality claim)
  2  could-not-evaluate: O37's receipt or the sweep instrument is unreadable
"""
import argparse, hashlib, json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
O37_RECEIPT = ROOT / "reports" / "round-27" / "pinsweep" / "o37-inventory-receipt.json"
SWEEP = ROOT / "reports" / "round-27" / "audit" / "x61-pin-sweep.py"
D4PRE = "examples/culture-d4/"
HEX = re.compile(r"^[0-9a-f]{64}$")

def rel(p):
    return str(Path(p).relative_to(ROOT))

def sha(p):
    try:
        return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    except OSError:
        return None

# ---------- A. resolve the pin a surface asserts for a D4 path ----------
NAMED_KEYS = {
    "packet_sha256": "examples/culture-d4/packet.d4.yml",
    "projection_sha256": "examples/culture-d4/typed-labels.d4.yml",
}
PIPELINE_SECTIONS = ("packet", "projection", "adapter", "assembler", "expected")

def resolve_pins(path):
    """Return {d4_target: digest} for every pin this file asserts, by shape.

    Shapes recognised (the same set the lane's own artifacts use):
      * JSON `inputs` / `input_pins` maps:  {"examples/culture-d4/x": "<hex>"}
      * a `{"path": "examples/culture-d4/x", "sha256": "<hex>"}` object (twins)
      * named-key self-pins (`packet_sha256`, `projection_sha256`)
      * the typed-pipelines profile shape (section -> {path, sha256})
      * TSV rows: column 3 is the input path, column 4 its digest
    """
    p = Path(path)
    out = {}
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return out
    if path.endswith(".tsv"):
        for line in text.splitlines():
            cols = line.split("\t")
            if len(cols) >= 4 and cols[2].startswith(D4PRE) and HEX.match(cols[3]):
                out[cols[2]] = cols[3]
        return out
    try:
        d = json.loads(text)
    except (json.JSONDecodeError, ValueError):
        return out
    # named-key self-pins and the typed-pipelines profile shape
    for key, tgt in NAMED_KEYS.items():
        if isinstance(d.get(key), str) and HEX.match(d[key]) and Path(tgt).is_file():
            out[tgt] = d[key]
    for prof in (d.get("profiles") or []):
        if not isinstance(prof, dict):
            continue
        for sect in PIPELINE_SECTIONS:
            s = prof.get(sect)
            if isinstance(s, dict) and str(s.get("path", "")).startswith(D4PRE) \
                    and HEX.match(str(s.get("sha256", ""))):
                out[str(s["path"])] = str(s["sha256"])
    stack = [d]
    while stack:
        o = stack.pop()
        if isinstance(o, dict):
            # shape: {"path": "examples/culture-d4/x", "sha256": "<hex>"}
            if str(o.get("path", "")).startswith(D4PRE) and HEX.match(str(o.get("sha256", ""))):
                out[str(o["path"])] = str(o["sha256"])
            for k, v in o.items():
                if isinstance(v, str) and HEX.match(v) and str(k).startswith(D4PRE):
                    out[str(k)] = v
                elif isinstance(v, dict):
                    stack.append(v)
                elif isinstance(v, list):
                    stack.append(v)
        elif isinstance(o, list):
            stack.extend(o)
    return out

def pin_verdict(pins):
    if not pins:
        return "unresolvable"
    stale = [t for t, d in pins.items() if sha(t) != d]
    return "stale" if stale else "holds"

# ---------- B. reach, re-derived ----------
def reach():
    if not SWEEP.is_file():
        return None, f"sweep instrument absent: {rel(SWEEP)}"
    env = dict(os.environ, TMPDIR="/var/tmp/kotodama-o38-reach",
               PYTHONDONTWRITEBYTECODE="1")
    try:
        proc = subprocess.run([sys.executable, "-B", str(SWEEP), "--json"],
                              capture_output=True, text=True, cwd=str(ROOT),
                              env=env, timeout=900)
    except subprocess.TimeoutExpired:
        return None, "sweep instrument timed out"
    if not proc.stdout.strip():
        return None, f"sweep instrument produced no receipt (exit {proc.returncode})"
    try:
        rec = json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        return None, f"sweep receipt not JSON: {e}"
    got = {m["manifest"] for m in rec.get("manifests", []) if "manifest" in m}
    got |= {b["baseline"] for b in rec.get("baselines", []) if "baseline" in b}
    return got, None

# ---------- B'. reach, static fallback (the instrument hardcodes /tmp) ----------
ASSIGN = re.compile(r'^([A-Z][A-Z0-9_]*)\s*=\s*(.+)$', re.M)
CHAIN = re.compile(r'"([^"]+)"')
RGLOB = re.compile(r'([A-Za-z_][A-Za-z0-9_]*|\([^)]*\))\s*\.rglob\(\s*"([^"]+)"\s*\)')

def _resolve_chain(expr, consts):
    expr = expr.strip()
    if expr in consts:
        return consts[expr]
    if "ROOT" not in expr:
        return None
    parts = CHAIN.findall(expr)
    return ROOT.joinpath(*parts) if parts else None

def source_reach():
    """Static reach of the sweep instrument's `rglob`s, for when it cannot run.

    The instrument mirrors into a hardcoded `/tmp`; a full `/tmp` makes every
    row fail with ENOSPC and no receipt is produced. The fallback is weaker —
    it reads intent, not behaviour — so the caller records the method."""
    src = SWEEP.read_text()
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

# ---------- D. families a filename walk could omit ----------
PROBE_GLOBS = ("tools/gates/**/*.expected", "reports/**/run.log",
               "reports/**/packet.md", "**/freeze.txt",
               "reports/**/evidence/*.json", "reports/**/*.out")

def probe_families():
    found = {}
    for pat in PROBE_GLOBS:
        for p in ROOT.glob(pat):
            if not p.is_file():
                continue
            r = rel(p)
            if ".git" in r or ".scratch" in r or "__pycache__" in r:
                continue
            pins = resolve_pins(r)
            if pins:
                found[r] = pins
    return found

# ---------- E. the claim sweep's own family-G filter, adjudicated ----------
CLAIM_SWEEP = ROOT / "reports" / "round-27" / "pinsweep" / "sweep.py"
HOLD_SET = ROOT / "examples" / "culture-d4" / "expected-holds.json"

def adjudicate_hold_filter():
    """Does the claim sweep's own D4 test keep the live D4 hold set?

    O37 found that family G enumerates 0 rows. This re-derives the *cause*
    independently: evaluate the sweep's four guard strings against the live hold
    set and report which (if any) fire. A file that should be kept and is not is
    the defect; a file that fires at least one guard is kept."""
    if not CLAIM_SWEEP.is_file() or not HOLD_SET.is_file():
        return None
    try:
        doc = json.loads(HOLD_SET.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    guards = {
        "holds mention culture-d4":
            "culture-d4" in json.dumps(doc.get("holds") or []),
        "supersedes_pins mention culture-d4":
            "culture-d4" in json.dumps(doc.get("supersedes_pins") or {}),
        "schema contains d4":
            "d4" in (doc.get("schema") or ""),
        "revision_note contains D4":
            "D4" in (doc.get("revision_note") or ""),
    }
    # the digest-identity test the sweep should have used
    pins = {doc.get(k) for k in ("packet_sha256", "projection_sha256", "projector_sha256")}
    pins.discard(None)
    live = set()
    for p in (ROOT / "examples" / "culture-d4").rglob("*"):
        if p.is_file():
            live.add(sha(rel(p)))
    live.add(sha("tools/d2-typed-labels.py"))
    return {"guards": guards, "kept_by_guards": any(guards.values()),
            "is_d4_by_digest_identity": bool(pins & live),
            "defect": (not any(guards.values())) and bool(pins & live)}

def claim_sweep_families():
    """The claim sweep's own family tallies, for cross-checking."""
    if not CLAIM_SWEEP.is_file():
        return None
    env = dict(os.environ, TMPDIR="/var/tmp/kotodama-o38-sweep",
               PYTHONDONTWRITEBYTECODE="1")
    try:
        proc = subprocess.run([sys.executable, "-B", str(CLAIM_SWEEP), "--json"],
                              capture_output=True, text=True, cwd=str(ROOT),
                              env=env, timeout=900)
        rec = json.loads(proc.stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError):
        return None
    out = {}
    for k, v in (rec.get("families") or {}).items():
        if isinstance(v, list):
            out[k] = len(v)
        elif isinstance(v, dict):
            out[k] = len(v.get("replays") or []) if "replays" in v else 1
    return {"families": out, "summary": rec.get("summary")}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        import tempfile
        checks = []
        checks.append(("HEX accepts 64 hex", bool(HEX.match("a" * 64))))
        checks.append(("HEX rejects 63 hex", not HEX.match("a" * 63)))
        with tempfile.TemporaryDirectory() as td:
            j = Path(td) / "x.json"
            live = sha("examples/culture-d4/packet.d4.yml")
            j.write_text(json.dumps({"inputs": {"examples/culture-d4/packet.d4.yml": live}}))
            checks.append(("resolves a JSON inputs pin", resolve_pins(str(j)) != {}))
            checks.append(("a live pin reads holds",
                           pin_verdict(resolve_pins(str(j))) == "holds"))
            j.write_text(json.dumps({"inputs": {"examples/culture-d4/packet.d4.yml": "0" * 64}}))
            checks.append(("a wrong pin reads stale",
                           pin_verdict(resolve_pins(str(j))) == "stale"))
            t = Path(td) / "x.tsv"
            t.write_text("g\t" + "b" * 64 + "\texamples/culture-d4/packet.d4.yml\t" + live
                         + "\t0\t0\tout\t" + "c" * 64 + "\tsnap\tcmd\n")
            checks.append(("resolves a TSV row pin", resolve_pins(str(t)) != {}))
        ok = all(v for _, v in checks)
        for n, v in checks:
            print(("PASS " if v else "FAIL ") + n)
        print(f"selftest: {sum(1 for _, v in checks if v)}/{len(checks)} checks passed")
        return 0 if ok else 1

    if not O37_RECEIPT.is_file():
        print(f"COULD-NOT-EVALUATE: O37 receipt absent: {rel(O37_RECEIPT)}", file=sys.stderr)
        return 2
    try:
        o37 = json.loads(O37_RECEIPT.read_text())
    except (OSError, json.JSONDecodeError) as e:
        print(f"COULD-NOT-EVALUATE: O37 receipt unreadable: {e}", file=sys.stderr)
        return 2

    got, err = reach()
    reach_method = "instrument-receipt"
    if got is None:
        try:
            got, reach_method = source_reach(), "source-rglob-fallback"
        except OSError as e:
            print(f"COULD-NOT-EVALUATE: {err}; fallback unreadable: {e}", file=sys.stderr)
            return 2

    rows, disagree = [], []
    for r in o37.get("rows", []):
        if not r.get("pins_d4"):
            continue
        s = r["surface"]
        pins = resolve_pins(s)
        v = pin_verdict(pins)
        swept = s in got
        rec = {"surface": s, "family": r["family"],
               "o37_swept": r["swept_by_instrument"], "recheck_swept": swept,
               "pins_resolved": len(pins), "pin_verdict": v}
        if swept != r["swept_by_instrument"]:
            disagree.append({**rec, "kind": "reach-disagreement"})
        if v == "unresolvable":
            disagree.append({**rec, "kind": "pin-unresolvable"})
        rows.append(rec)

    probes = probe_families()
    # a probe file is a *finding* only if it pins a D4 path O37 did not enumerate
    o37_set = {r["surface"] for r in o37.get("rows", [])}
    new_probes = {k: v for k, v in probes.items() if k not in o37_set}

    hold_filter = adjudicate_hold_filter()
    claim_fams = claim_sweep_families()

    # reach relative to the CLAIM sweep, which is the one that decides the claim
    claim_reached = set()
    if claim_fams:
        for k, v in (claim_fams.get("families") or {}).items():
            pass
    claim_paths = set()
    if CLAIM_SWEEP.is_file():
        env = dict(os.environ, TMPDIR="/var/tmp/kotodama-o38-sweep",
                   PYTHONDONTWRITEBYTECODE="1")
        try:
            proc = subprocess.run([sys.executable, "-B", str(CLAIM_SWEEP), "--json"],
                                  capture_output=True, text=True, cwd=str(ROOT),
                                  env=env, timeout=900)
            rec = json.loads(proc.stdout)
            for k, val in (rec.get("families") or {}).items():
                rows_v = val if isinstance(val, list) else ([val] if isinstance(val, dict) else [])
                for rr in rows_v:
                    if isinstance(rr, dict) and rr.get("path"):
                        claim_paths.add(rr["path"])
                if isinstance(val, dict):
                    for rep in (val.get("replays") or []):
                        if rep.get("manifest"):
                            claim_paths.add(rep["manifest"])
        except (subprocess.TimeoutExpired, json.JSONDecodeError):
            pass
    claim_missed = [r for r in rows if not (r["surface"] in claim_paths)]

    missed = [r for r in rows if not r["recheck_swept"]]
    missed_stale = [r for r in missed if r["pin_verdict"] == "stale"]
    missed_holds = [r for r in missed if r["pin_verdict"] == "holds"]

    out = {
        "tool": "reports/round-27/audit/o38-sweep-inventory-adjudication.py",
        "round": 27, "seat": "R27-O38", "date": "2026-10-18",
        "lane_head": os.popen(f"git -C {ROOT} rev-parse HEAD").read().strip(),
        "o37_rows_adjudicated": len(rows),
        "reach_method": reach_method,
        "reach_disagreements": [d for d in disagree if d["kind"] == "reach-disagreement"],
        "pin_unresolvable": [d for d in disagree if d["kind"] == "pin-unresolvable"],
        "missed_total": len(missed),
        "missed_stale": [r["surface"] for r in missed_stale],
        "missed_holds": [r["surface"] for r in missed_holds],
        "claim_sweep_enumerated": len(claim_paths),
        "claim_sweep_missed": [r["surface"] for r in claim_missed],
        "claim_sweep_families": claim_fams,
        "hold_filter_adjudication": hold_filter,
        "un_enumerated_probe_surfaces": new_probes,
        "rows": rows,
        "limits": "adjudicates O37's census; it does not re-enumerate the universe "
                  "and makes no claim about design quality or sweep verdicts. "
                  "'missed_*' is relative to the X61 AUDIT instrument; "
                  "'claim_sweep_missed' is relative to the claim-O sweep.",
    }
    if a.json:
        print(json.dumps(out, indent=1, sort_keys=True))
    else:
        print(f"R27-O38 adjudication — lane HEAD {out['lane_head'][:12]}")
        print(f"  O37 D4 rows adjudicated: {out['o37_rows_adjudicated']} "
              f"[reach: {reach_method}]")
        print(f"  reach disagreements:     {len(out['reach_disagreements'])}")
        print(f"  pin unresolvable:        {len(out['pin_unresolvable'])}")
        print(f"  missed by X61 audit:     {out['missed_total']} "
              f"({len(out['missed_stale'])} stale / {len(out['missed_holds'])} hold)")
        print(f"  claim-O sweep enumerates {out['claim_sweep_enumerated']} surface(s); "
              f"misses {len(out['claim_sweep_missed'])}")
        for s in out["claim_sweep_missed"]:
            print(f"    ! {s}")
        if hold_filter:
            print(f"  hold-filter adjudication: kept_by_guards="
                  f"{hold_filter['kept_by_guards']} "
                  f"is_d4_by_digest={hold_filter['is_d4_by_digest_identity']} "
                  f"DEFECT={hold_filter['defect']}")
            for g, v in hold_filter["guards"].items():
                print(f"      {'fires' if v else 'false'}: {g}")
        if claim_fams:
            print(f"  claim sweep families: {claim_fams['families']} "
                  f"summary={claim_fams['summary']}")
        print(f"  un-enumerated probe surfaces: {len(new_probes)}")
        for s in new_probes:
            print(f"    + {s}")
    bad = bool(disagree or new_probes or (hold_filter or {}).get("defect"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
