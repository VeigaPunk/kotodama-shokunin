#!/usr/bin/env python3
"""Round-26 O seat — verify the declared-in-r4 machine twin (R26-O29..O32).

The round-25 remainder this seat dispositions: the v3 revision
`reports/round-25/v3-supersession/declared-in-r4/` landed packet-only. The twin
now lives as a **new row** at `reports/round-26/remainders/r4-twin/twin.json`;
the filed round-25 directory is not written (rounds 8-25 are frozen).

What this checker binds, and to what:

1. **Identity.** `expected.json`'s `twin_sha256` key pins the twin's bytes, the
   same binding mechanism the r20 and r22 siblings use
   (`reports/round-22/handoff/declared-in-r2/expected.json`).
2. **Derivation.** The twin is re-derived from the filed r4 packet by
   `build-twin.py` and must equal the filed twin byte-for-byte — so the twin is
   a pure function of the packet, not a hand-written artifact.
3. **Projection control.** The same builder, run against the two filed
   predecessor packets, must reproduce `reports/round-20/handoff/twin.json` and
   `reports/round-22/handoff/declared-in-r2/twin.json` byte-for-byte. This is
   the load-bearing control: it proves the projection rule is the renderer's own
   `v3_build_twin`, including the header-adaptive `declared_in` column.
4. **Content.** The twin carries the corrected D4 rows (the r4 revision's whole
   purpose), is clean under the filed round-25 checker's own stale-prose
   detector, fires that detector on the r22 predecessor, and preserves the D2
   rows verbatim.
5. **Frozen verify.** The frozen round-20 harness judges are re-run on the twin
   (uncertainty + links), and the frozen sibling checks are re-run unchanged:
   `reports/round-25/v3-supersession/v3-supersession-check.py` (the r4 checker)
   and `reports/round-23/wording/wording-check.py`.

Commands (from the lane root, `export TMPDIR=$PWD/.scratch`):
    python3 reports/round-26/remainders/r4-twin/verify-twin.py --root <clone> --selftest
    python3 reports/round-26/remainders/r4-twin/verify-twin.py --root <clone> --check
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
COMMAND = "python3 reports/round-26/remainders/r4-twin/verify-twin.py"

BUILDER = "reports/round-26/remainders/r4-twin/build-twin.py"
TWIN = "reports/round-26/remainders/r4-twin/twin.json"
BASELINE = "reports/round-26/remainders/r4-twin/expected.json"
R4_PACKET = "reports/round-25/v3-supersession/declared-in-r4/packet.md"
R4_PACKET_SHA256 = "5f58db4a52b688568eac054b1c75e9bd110843370a1943cf4353fff75b46aa03"
R4_DIR = "reports/round-25/v3-supersession/declared-in-r4"
R22_TWIN = "reports/round-22/handoff/declared-in-r2/twin.json"
R20_TWIN = "reports/round-20/handoff/twin.json"
R25_CHECKER = "reports/round-25/v3-supersession/v3-supersession-check.py"
R23_CHECKER = "reports/round-23/wording/wording-check.py"
UNCERTAINTY = "tools/harness/packet_uncertainty.py"
LINKS = "tools/harness/packet_links.py"
R4_FIVE = ("D4-CL05", "D4-CL06", "D4-CL07", "D4-CL09", "OQ-V3-05")


def sha256_of(path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(root, source_root=None):
    """Rebuild the twin from `root`'s filed packet with the filed builder."""
    return load_module("r26_r4_builder", BUILDER).build_twin(
        Path(root), source_root=Path(source_root) if source_root else None)


def render(twin) -> str:
    return json.dumps(twin, indent=1, sort_keys=True, ensure_ascii=False) + "\n"


def twin_surface(document):
    """The claim/OQ surface the filed stale detector reads, from a twin dict."""
    surface = {row["claim_id"]: row["statement"] + " " + row["uncertainty"]["basis"]
               for row in document["claim_ledger"]}
    surface.update({row["id"]: row["question"] for row in document["open_questions"]})
    return surface


def harness(tool, twin_path, extra=(), repo_root=None):
    """Run a frozen harness judge on the twin; returns (exit, payload)."""
    arguments = [sys.executable, str(ROOT / tool), "--packet", str(twin_path), *extra]
    if repo_root is not None:
        arguments.extend(["--repo-root", str(repo_root)])
    arguments.append("--json")
    run = subprocess.run(
        arguments, cwd=str(ROOT), capture_output=True, text=True,
        env={**os.environ, "TMPDIR": str(ROOT / ".scratch"),
             "PYTHONDONTWRITEBYTECODE": "1"})
    try:
        payload = json.loads(run.stdout)
    except json.JSONDecodeError:
        payload = {"error": (run.stdout or run.stderr).strip()[:200]}
    return run.returncode, payload


def verify_tree(root, controls, source_root=None):
    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    live_packet = sha256_of(ROOT / R4_PACKET)
    check("filed-r4-packet-digest-pinned", live_packet == R4_PACKET_SHA256,
          sha256=live_packet)
    expected = json.loads((ROOT / BASELINE).read_text(encoding="utf-8"))
    live_twin = sha256_of(ROOT / TWIN)
    check("twin-pin-matches-live-bytes",
          expected.get("twin_sha256") == live_twin, twin_sha256=live_twin)
    check("twin-pins-its-source-packet",
          expected.get("packet_sha256") == R4_PACKET_SHA256,
          packet_sha256=expected.get("packet_sha256"))
    # the new row is copied into the clone (the clone may predate it), exactly as
    # the filed r25 checker copies its own revision into the clone.
    for relative in (BUILDER, BASELINE, TWIN):
        target = Path(root) / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((ROOT / relative).read_bytes())
    for relative in (BUILDER, TWIN, BASELINE, R4_PACKET):
        clone_path = Path(root) / relative
        check(f"clone-matches-live:{relative}",
              clone_path.is_file() and sha256_of(clone_path) == sha256_of(ROOT / relative))
    rebuilt = render(build(ROOT, source_root))
    filed = (ROOT / TWIN).read_text(encoding="utf-8")
    check("twin-is-re-derived-from-the-packet", rebuilt == filed,
          bytes=len(filed.encode("utf-8")))
    return expected


def projection_control(controls, source_root=None):
    """The load-bearing control: the filed predecessor twins must reproduce."""
    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    for row in load_module("r26_r4_builder2", BUILDER).reproduce_filed(source_root):
        check(f"reproduces-filed-twin:{row['twin']}", row["byte_identical"],
              declared=row["declared"], observed=row["observed"])


def content_controls(root, controls):
    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    detector = load_module("r26_r4_detector", R25_CHECKER)
    twin = json.loads((Path(root) / TWIN).read_text(encoding="utf-8"))
    predecessor = json.loads((Path(root) / R22_TWIN).read_text(encoding="utf-8"))
    check("twin-shape-3.1.1",
          twin["packet_version"] == "3.1.1"
          and twin["profile"] == "kotodama-handoff-e2e/3"
          and twin["packet_id"] == "kotodama.handoff.d2d3d4-e2e"
          and "declared_in" in twin["coupling_edges"][0],
          packet_version=twin["packet_version"], profile=twin["profile"])
    check("twin-census-58-27-88-10",
          len(twin["artifact_manifest"]) == 58 and len(twin["claim_ledger"]) == 27
          and len(twin["coupling_edges"]) == 88 and len(twin["open_questions"]) == 10,
          manifest=len(twin["artifact_manifest"]), claims=len(twin["claim_ledger"]),
          edges=len(twin["coupling_edges"]), open_questions=len(twin["open_questions"]))
    check("twin-carries-no-inline-glossary-row",
          all(not row["path"].startswith("§") for row in twin["artifact_manifest"]))
    old_rows = {row["claim_id"]: json.dumps(row) for row in predecessor["claim_ledger"]}
    new_rows = {row["claim_id"]: json.dumps(row) for row in twin["claim_ledger"]}
    watched = ("D4-CL05", "D4-CL06", "D4-CL07", "D4-CL09")
    check("twin-carries-the-corrected-d4-rows",
          all(new_rows[cid] != old_rows[cid] for cid in watched),
          changed=[cid for cid in watched if new_rows[cid] != old_rows[cid]])
    old_oq = {row["id"]: row["question"] for row in predecessor["open_questions"]}
    new_oq = {row["id"]: row["question"] for row in twin["open_questions"]}
    check("twin-carries-the-corrected-oq-passenger",
          "zero rank holds" in new_oq.get("OQ-V3-05", "")
          and new_oq.get("OQ-V3-05") != old_oq.get("OQ-V3-05"))
    check("twin-clean-under-the-filed-stale-detector",
          detector.stale_hits(twin_surface(twin)) == [],
          hits=detector.stale_hits(twin_surface(twin))[:8])
    predecessor_hits = detector.stale_hits(twin_surface(predecessor))
    check("detector-fires-on-the-r22-predecessor-twin",
          sorted({row_id for row_id, _ in predecessor_hits}) == sorted(R4_FIVE),
          rows=sorted({row_id for row_id, _ in predecessor_hits}),
          hits=len(predecessor_hits))
    v2 = ("D2-CL01", "D2-CL02") + tuple(f"CL{i:02d}" for i in range(1, 14))
    check("twin-preserves-the-15-v2-rows-verbatim",
          [row for row in twin["claim_ledger"] if row["claim_id"] in v2]
          == [row for row in predecessor["claim_ledger"] if row["claim_id"] in v2],
          rows=len([row for row in twin["claim_ledger"] if row["claim_id"] in v2]))
    return twin


def harness_controls(root, controls, repo_root=None):
    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    # The judges are run with the twin inside the clone that carries the packet's
    # pinned read set, so the manifest digest re-measurement resolves against
    # those bytes rather than a live tree a concurrent seat may be rewriting.
    base = Path(repo_root) if repo_root else Path(root)
    twin_path = base / TWIN
    twin_path.parent.mkdir(parents=True, exist_ok=True)
    twin_path.write_bytes((ROOT / TWIN).read_bytes())
    exit_code, payload = harness(UNCERTAINTY, twin_path, ["--require-oq"])
    check("frozen-uncertainty-judge-green",
          exit_code == 0 and not payload.get("findings"),
          exit=exit_code, claims=payload.get("claims"),
          findings=payload.get("findings"))
    exit_code, payload = harness(LINKS, twin_path, repo_root=base)
    check("frozen-links-judge-green",
          exit_code == 0 and not payload.get("findings")
          and payload.get("resolved") == payload.get("links_checked"),
          exit=exit_code, links_checked=payload.get("links_checked"),
          resolved=payload.get("resolved"), findings=payload.get("findings"))
    return payload


def frozen_verify(root, controls, run_siblings, frozen_root=None):
    """Re-run the frozen sibling checks unchanged (the 'frozen verify' clause).

    The siblings are run against their **own** declared baseline clone
    (`frozen_root`), because their verdict is a property of the state they pin,
    not of this seat's twin: the r25 r4 checker pins the round-24 admit where
    the round-25 argot leg does not yet exist, so it is green (52/52) there and
    carries two declared sibling-pin tails. Running it on the live round-26 tree
    would surface the round-26 argot leg (gate 20/20 vs its pinned 19/19), which
    is a third inherited tail owned by the D seat, not by this one.
    """
    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    frozen_root = Path(frozen_root) if frozen_root else Path(root)
    # the filed round-25 r4 directory must be byte-unchanged by this seat
    live = {path.relative_to(ROOT).as_posix(): sha256_of(path)
            for path in (ROOT / R4_DIR).rglob("*") if path.is_file()}
    expected = {path.relative_to(Path(root)).as_posix(): sha256_of(path)
                for path in (Path(root) / R4_DIR).rglob("*") if path.is_file()}
    check("filed-r25-r4-directory-untouched", live == expected,
          files=len(live), changed=sorted(set(live) ^ set(expected))[:5]
          or sorted(p for p in live if live[p] != expected.get(p))[:5])
    check("twin-is-a-new-row-not-a-r25-write",
          not (ROOT / R4_DIR / "twin.json").exists(),
          note="the twin lives under reports/round-26/remainders/; the filed "
               "round-25 revision stays exactly as filed")

    if not run_siblings:
        return {}
    out = {}
    for label, script, arg in (("r25-r4-checker", R25_CHECKER, "--check"),
                               ("r23-wording-checker", R23_CHECKER, "--check")):
        receipt = ROOT / ".scratch" / f"r26-o29-{label}-receipt.json"
        if receipt.is_file():
            receipt.unlink()
        run = subprocess.run(
            [sys.executable, str(ROOT / script), "--root", str(frozen_root), arg,
             "--receipt", str(receipt)],
            cwd=str(ROOT), capture_output=True, text=True,
            env={**os.environ, "TMPDIR": str(ROOT / ".scratch"),
                 "PYTHONDONTWRITEBYTECODE": "1"})
        payload = json.loads(receipt.read_text(encoding="utf-8")) if receipt.is_file() else {}
        failures = [item["control"] for item in payload.get("controls", [])
                    if not item["passed"]]
        out[label] = {"exit": run.returncode, "passed": payload.get("passed"),
                      "passed_controls": payload.get("passed_controls"),
                      "total_controls": payload.get("total_controls"),
                      "failing_controls": failures,
                      "positive_failures": (payload.get("positive") or {}).get("failures")}
    # the frozen checker's verdict is a property of its own declared baseline,
    # not of this seat's twin: it must stay green with its declared open tails.
    r25 = out["r25-r4-checker"]
    check("frozen-r25-r4-checker-still-green", r25["passed"] is True,
          exit=r25["exit"], passed_controls=r25["passed_controls"],
          total_controls=r25["total_controls"], failing_controls=r25["failing_controls"],
          note="the r4 checker is green (52/52) at its declared round-25 baseline; "
               "its two declared open tails are sibling pins it does not own")
    r23 = out["r23-wording-checker"]
    check("frozen-r23-wording-checker-unaffected",
          r23["passed"] is True
          or r23["failing_controls"]
          == ["positive-control-remaining-failures-are-declared-open-tails-only"],
          exit=r23["exit"], passed_controls=r23["passed_controls"],
          total_controls=r23["total_controls"], failing_controls=r23["failing_controls"])
    return out


def selftest(root, source_root=None):
    controls = []

    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    expected = verify_tree(root, controls, source_root)
    projection_control(controls, source_root)
    content_controls(root, controls)
    harness_controls(root, controls, source_root)

    # builder must refuse a drifted packet rather than emit a silent twin
    with tempfile.TemporaryDirectory(prefix="r26-r4-", dir=Path(root) / ".scratch") as temp:
        fixture = Path(temp)
        (fixture / R4_DIR).mkdir(parents=True)
        good = (ROOT / R4_PACKET).read_bytes()
        (fixture / R4_PACKET).write_bytes(good)
        check("builder-reproduces-filed-twin",
              render(build(fixture, source_root)) == (ROOT / TWIN).read_text(encoding="utf-8"))
        (fixture / R4_PACKET).write_bytes(good + b"\nstray\n")
        try:
            build(fixture, source_root)
            refused = False
        except SystemExit:
            refused = True
        check("builder-refuses-drifted-packet", refused)
    passed = all(item["passed"] for item in controls)
    return {"date": dt.datetime.now(dt.timezone.utc).isoformat(),
            "command": f"{COMMAND} --root {root} --selftest", "root": str(root),
            "twin_sha256": expected.get("twin_sha256"), "controls": controls,
            "passed": passed,
            "passed_controls": sum(item["passed"] for item in controls),
            "total_controls": len(controls)}


def check(root, frozen_root=None, source_root=None):
    controls = []

    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    expected = verify_tree(root, controls, source_root)
    projection_control(controls, source_root)
    twin = content_controls(root, controls)
    links = harness_controls(root, controls, source_root)
    siblings = frozen_verify(root, controls, run_siblings=True, frozen_root=frozen_root)
    passed = all(item["passed"] for item in controls)
    return {"date": dt.datetime.now(dt.timezone.utc).isoformat(),
            "command": f"{COMMAND} --root {root} --check", "root": str(root),
            "frozen_root": str(frozen_root) if frozen_root else None,
            "source_root": str(source_root) if source_root else None,
            "twin_sha256": expected.get("twin_sha256"),
            "twin_counts": {"manifest": len(twin["artifact_manifest"]),
                            "claims": len(twin["claim_ledger"]),
                            "edges": len(twin["coupling_edges"]),
                            "open_questions": len(twin["open_questions"])},
            "links_resolved": f"{links.get('resolved')}/{links.get('links_checked')}",
            "frozen_siblings": siblings, "controls": controls, "passed": passed,
            "passed_controls": sum(item["passed"] for item in controls),
            "total_controls": len(controls)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=(
        "Round-26 O seat: verify the declared-in-r4 machine twin in an isolated clone."))
    parser.add_argument("--root", type=Path, required=True,
                        help="isolated clone under the lane's .scratch")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--selftest", action="store_true")
    group.add_argument("--check", action="store_true")
    parser.add_argument("--frozen-root", type=Path,
                        help="isolated clone at the frozen siblings' own declared "
                             "baseline (default: --root)")
    parser.add_argument("--source-root", type=Path,
                        help="isolated clone holding the packet's pinned read set; "
                             "the record index and the harness digest checks resolve "
                             "against it (default: --root). Pass it when a concurrent "
                             "seat is rewriting the live tree.")
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    source_root = args.source_root.resolve() if args.source_root else None
    frozen_root = args.frozen_root.resolve() if args.frozen_root else None
    for label, candidate in (("--root", root), ("--frozen-root", frozen_root),
                             ("--source-root", source_root)):
        if candidate is None:
            continue
        if not (candidate.is_relative_to(ROOT / ".scratch") and (candidate / ".git").is_dir()):
            parser.error(f"{label} must be an isolated clone with .git under the lane's .scratch")
    os.environ["TMPDIR"] = str(root / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    (root / ".scratch").mkdir(exist_ok=True)
    payload = (selftest(root, source_root) if args.selftest
               else check(root, frozen_root, source_root))
    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
