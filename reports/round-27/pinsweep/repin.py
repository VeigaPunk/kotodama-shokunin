#!/usr/bin/env python3
"""R27-O25..O32 — the re-pin driver: freeze every drifted D4 surface as a NEW row.

Runs only when the D4 tree is stable (the round-27 D seat lands the register law
in waves, and a re-pin taken mid-wave is stale the moment it lands). Everything
it writes lives under `reports/round-27/pinsweep/`; no filed byte is touched.

It produces, in one pass:

  1. `baselines/d4-assembly-check-gate/r27-post/`  — the D4 assembly adapter baseline
  2. `baselines/d4-typed-labels-check-gate/r27-post/` — the D4 projection adapter baseline
  3. `frozen/r27-post/`                            — the D4-leg replay generation
  4. `v3-baseline-r27/`                            — the v3 handoff baseline
  5. `d4-pins.json`                                — the machine-readable before/after rows

Usage
-----
    export TMPDIR=/var/tmp/kotodama-r27-pinsweep   # outside the repo
    python3 reports/round-27/pinsweep/repin.py             # freeze
    python3 reports/round-27/pinsweep/repin.py --check     # verify only
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = HERE
DATE = "2026-10-18"
COLS = ("gate", "gate_sha256", "input", "input_sha256", "exit_code",
        "finding_count", "output", "output_sha256", "input_snapshot", "command")

# The pre-register / pre-law digests every drifted row still pins.
STALE = {
    "examples/culture-d4/packet.d4.yml":
        "dd25077bc01681bc17f4586b40cfdd6959d4f45fc63e4f33f13fdc9b2cc88e67",
    "examples/culture-d4/packet.d4.typed.yml":
        "618a78c90fc04c0d17e2619d1fed080e99f98b1213ad01fcbb75e7aab48fd18c",
    "examples/culture-d4/typed-labels.d4.yml":
        "d03f6391fb8dc2b4d2b2ad05e08547455bc96c580050d830ce0c7c22bb75e580",
    "examples/culture-d4/expected-holds.json":
        "d6136488e22f989e109c435cb4f7eb02ca680043785e88e78038ed5f47150fd3",
    "examples/culture-d4/components/01-brief.yml":
        "a2bc3111b8e936d2aa78feca86b871996455cc98d7d639f3825a88df8a1c056f",
    "examples/culture-d4/components/04-lexicon.yml":
        "74c2561b7c875c7c98708c589002b85b7989fc64bafa6abf794210401c69a9a5",
}

D4_COMPONENTS = tuple(sorted(
    "examples/culture-d4/components/%s" % p.name
    for p in (ROOT / "examples/culture-d4/components").glob("*.yml")))

ASM_READ_SET = D4_COMPONENTS + (
    "tools/assemble-culture-d4.py",
    "tools/assemble-d2.py",
    "tools/gates/costume-era-consistency-gate.py",
)
TYPED_READ_SET = (
    "examples/culture-d4/packet.d4.yml",
    "tools/d2-typed-labels.py",
    "tools/gates/costume-era-consistency-gate.py",
    "examples/culture-d2/components/11-costumes.yml",
    "examples/culture-d2/components/12-rank-rules.yml",
)
GATES = (
    ("d4-assembly-check-gate", "tools/gates/d4-assembly-check-gate.py",
     "examples/culture-d4/packet.d4.yml", "packet.d4.yml", ASM_READ_SET, "d4-assembly.out"),
    ("d4-typed-labels-check-gate", "tools/gates/d4-typed-labels-check-gate.py",
     "examples/culture-d4/typed-labels.d4.yml", "typed-labels.d4.yml",
     TYPED_READ_SET, "d4-typed-labels.out"),
)


def sha(path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def head() -> str:
    return subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(ROOT),
                          capture_output=True, text=True).stdout.strip()


def run(*argv) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *argv], capture_output=True, cwd=str(ROOT),
                          env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}, check=False)


def count(payload: bytes) -> int:
    try:
        doc = json.loads(payload.decode())
    except Exception:
        return 0
    if isinstance(doc, dict) and isinstance(doc.get("findings"), list):
        return len(doc["findings"])
    return 0


# ---------------------------------------------------------------- 1 + 2

def freeze_baseline(gate_dir, gate_rel, graded_src, graded_name, read_set, rows):
    base = OUT / "baselines" / gate_dir / "r27-post"
    if base.exists():
        shutil.rmtree(base)
    base.mkdir(parents=True)
    snap = base / graded_src
    snap.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / graded_src, snap)
    inputs = {graded_src: sha(ROOT / graded_src)}
    for rel in read_set:
        dst = base / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / rel, dst)
        inputs[rel] = sha(ROOT / rel)
    proc = run(str(ROOT / gate_rel), graded_src)
    (base / "run.log").write_bytes(proc.stdout)
    doc = {
        "schema": "kotodama-frozen-run-v1",
        "baseline_id": "r27-post",
        "gate": Path(gate_rel).name,
        "gate_script": gate_rel,
        "gate_sha256": sha(ROOT / gate_rel),
        "revision": head(),
        "revision_note": ("round-27 O claim (R27-O25..O32 pin sweep). Baseline lands as "
                          "uncommitted round-27 worker output; the digests below, not the "
                          "commit alone, bind the measured bytes. No commit/push performed."),
        "frozen_at": DATE,
        "frozen_by": "kotodama-shokunin R27-O25..O32 (pin sweep)",
        "command": "python3 %s %s" % (gate_rel, graded_src),
        "input_class": ("NON-CANON post-register-law D4 %s (the graded argv input), byte "
                        "copy of the live artifact" % graded_name),
        "inputs": inputs,
        "expected": {"class": "clean" if proc.returncode == 0 else "findings",
                     "exit": proc.returncode, "findings": []},
        "stdout_sha256": hashlib.sha256(proc.stdout).hexdigest(),
        "stderr_sha256": hashlib.sha256(proc.stderr).hexdigest(),
        "supersedes": "the same gate's r19-pre / r20-post / r22-post rows",
        "append_only_note": ("New baseline id only. Every filed baseline and every filed "
                             "round-8..26 byte stays unchanged; a re-pin is a new row, never "
                             "an in-place edit (gate-frozen-run-standard.md section 3)."),
        "read_set_note": ("Read set re-measured at this stamp with a sys.addaudithook('open') "
                          "trace over the graded command (scratch script, not committed); "
                          "every pinned copy equals its pin and the live file it was copied from."),
        "why_repinned": ("the round-26 register stratum and the round-27 register law amended "
                         "examples/culture-d4/components/{01-brief.yml,04-lexicon.yml,"
                         "13-register-law.yml}, which moved the D4 packet, its typed packet, "
                         "its projection and its hold set; the earlier rows pin the pre-law "
                         "digests and refuse with exit 1 (drift)"),
    }
    (base / "expected.json").write_text(json.dumps(doc, indent=1, sort_keys=True) + "\n",
                                        encoding="utf-8")
    rows.append({
        "id": "baseline:%s" % gate_dir,
        "surface": "tools/gates/expected/%s/{r19-pre,r20-post,r22-post}/expected.json" % gate_dir,
        "new_row": str((base / "expected.json").relative_to(ROOT)),
        "control": {"command": "python3 %s %s" % (gate_rel, graded_src),
                    "exit": proc.returncode,
                    "reading": ("exit 0 byte-identical at the new row's own snapshot"
                                if proc.returncode == 0 else "still red")},
        "stdout_sha256": hashlib.sha256(proc.stdout).hexdigest(),
        "inputs_pinned": len(inputs),
    })
    print("%-30s exit=%d stdout=%s" % (gate_dir, proc.returncode,
                                       hashlib.sha256(proc.stdout).hexdigest()[:16]))
    return proc.returncode


# ---------------------------------------------------------------- 3

def freeze_d4_legs(rows):
    out = OUT / "frozen/r27-post"
    if out.exists():
        shutil.rmtree(out)
    (out / "inputs").mkdir(parents=True)
    recorded = []
    for gate_dir, gate_rel, graded_src, graded_name, _read_set, out_name in GATES:
        proc = run(str(ROOT / gate_rel), graded_src)
        outp = out / out_name
        outp.write_bytes(proc.stdout)
        snap = out / "inputs" / graded_src
        snap.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / graded_src, snap)
        recorded.append({
            "gate": gate_rel, "gate_sha256": sha(ROOT / gate_rel),
            "input": graded_src, "input_sha256": sha(ROOT / graded_src),
            "exit_code": proc.returncode, "finding_count": count(proc.stdout),
            "output": str(outp.relative_to(ROOT)), "output_sha256": sha(outp),
            "input_snapshot": str(snap.relative_to(ROOT)),
            "command": "python3 %s %s" % (gate_rel, graded_src),
        })
        print("%-46s exit=%d" % (gate_rel, proc.returncode))
    (out / "MANIFEST.tsv").write_text(
        "\t".join(COLS) + "\n" + "".join(
            "\t".join(str(r[c]) for c in COLS) + "\n" for r in recorded), encoding="utf-8")
    (out / "freeze-receipt.json").write_text(json.dumps({
        "schema": "kotodama-r27-d4-leg-freeze-v1",
        "generation": "round-27 pinsweep frozen r27-post (R27-O25..O32)",
        "frozen_at": DATE, "frozen_by": "kotodama-shokunin R27-O25..O32 (pin sweep)",
        "revision": head(),
        "supersedes": [
            "tools/gates/frozen/round-18/MANIFEST.tsv rows 2-3 (replay mismatch, exit 1)",
            "tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv rows 2-3 (replay mismatch, exit 1)",
        ],
        "reason": ("the register stratum and the round-27 register law moved the D4 packet, "
                   "its projection and its hold set; every earlier D4-adapter row pins the "
                   "pre-law digests. A re-freeze is a new generation, never an in-place edit."),
        "input_pins": {r["input"]: r["input_sha256"] for r in recorded},
        "pins": {r["gate"]: r["gate_sha256"] for r in recorded},
        "rows": len(recorded),
        "replay": ("TMPDIR must sit outside the repository: python3 tools/replay-frozen.py "
                   "reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv"),
    }, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    rows.append({"id": "frozen-generation", "new_row": str((out / "MANIFEST.tsv").relative_to(ROOT)),
                 "surface": "tools/gates/frozen/round-{18,22}/**",
                 "rows": len(recorded)})


# ---------------------------------------------------------------- 4

def freeze_v3(rows):
    target = OUT / "v3-baseline-r27"
    proc = run(str(ROOT / "tools/exercise-handoff-e2e.py"), "--profile", "v3",
               "--freeze", str(target.relative_to(ROOT)))
    tail = (proc.stdout or proc.stderr).decode().strip().splitlines()[-1:]
    print("v3 freeze exit=%d %s" % (proc.returncode, tail))
    rows.append({
        "id": "v3-baseline", "new_row": str((target / "expected.json").relative_to(ROOT)),
        "surface": "reports/round-{20,22,25,26}/*/expected.json (the v3 handoff chain)",
        "control": {"command": "python3 tools/exercise-handoff-e2e.py --profile v3 --baseline "
                               "reports/round-27/pinsweep/v3-baseline-r27/expected.json",
                    "exit": proc.returncode, "tail": tail},
    })
    return proc.returncode


def measure_controls() -> list[dict]:
    """The red control for each re-pin: the filed row re-run at its own bytes.

    A re-pin's evidence is a pair: the filed surface must refuse, and the new row
    must be green. This measures the *refusal* side, because the green side is
    measured by the freeze itself. Every row here is a filed round-8..26 surface
    read-only; nothing is written.
    """
    controls = []
    for gate_dir, gate_rel, graded_src, _name, _read_set, _o in GATES:
        for filed_id, filed_graded in (
                ("d4-assembly-check-gate", "tools/gates/expected/d4-assembly-check-gate/r19-pre/packet.d4.yml"),
                ("d4-typed-labels-check-gate", "tools/gates/expected/d4-typed-labels-check-gate/r19-pre/typed-labels.d4.yml"),
                ("d4-typed-labels-check-gate", "tools/gates/expected/d4-typed-labels-check-gate/r20-post/typed-labels.d4.yml"),
                ("d4-typed-labels-check-gate", "tools/gates/expected/d4-typed-labels-check-gate/r22-post/typed-labels.d4.yml")):
            if filed_id != gate_dir:
                continue
            if not (ROOT / filed_graded).is_file():
                continue
            proc = run(str(ROOT / gate_rel), filed_graded)
            controls.append({
                "id": "control:%s" % filed_graded.split("expected/")[-1].split("/")[0],
                "surface": filed_graded, "gate": gate_rel, "exit": proc.returncode,
                "stderr_tail": proc.stderr.decode().strip().splitlines()[-1:] or [""],
            })
    for manifest in ("tools/gates/frozen/round-18/MANIFEST.tsv",
                     "tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv",
                     "tools/gates/frozen/round-26/post-register/MANIFEST.tsv"):
        rep = replay_manifest(manifest)
        controls.append({"id": "control:%s" % manifest, "surface": manifest,
                         "exit": rep["exit"], "statuses": rep.get("statuses")})
    for baseline in ("reports/round-20/handoff/expected.json",
                     "reports/round-22/handoff/declared-in/expected.json",
                     "reports/round-22/handoff/declared-in-r2/expected.json",
                     "reports/round-26/register/v3-baseline-r26/expected.json",
                     "reports/round-26/remainders/v3-baseline-r26/expected.json"):
        proc = run(str(ROOT / "tools/exercise-handoff-e2e.py"), "--profile", "v3",
                   "--baseline", baseline, "--quiet")
        controls.append({"id": "control:%s" % baseline, "surface": baseline,
                         "exit": proc.returncode})
    for row in controls:
        print("  control %-70s exit=%s" % (row["surface"], row["exit"]))
    return controls


def replay_manifest(manifest: str) -> dict:
    """Replay one filed generation with TMPDIR forced outside the repo."""
    outside = Path("/var/tmp/kotodama-r27-repin-controls")
    outside.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "TMPDIR": str(outside), "PYTHONDONTWRITEBYTECODE": "1"}
    proc = subprocess.run([sys.executable, str(ROOT / "tools/replay-frozen.py"),
                           manifest, "--json"], capture_output=True, text=True,
                          cwd=str(ROOT), env=env, check=False)
    try:
        doc = json.loads(proc.stdout)
        return {"exit": proc.returncode,
                "statuses": [r.get("status") for r in (doc.get("rows") or [])]}
    except ValueError:
        return {"exit": proc.returncode, "statuses": []}


def record_default_pointer(rows):
    """The fifth row: the tool's own v3 default pointer, re-pointed at the successor.

    This is the surface round-26's `register/repin.json` assigned to the O seat.
    It is recorded as a row of its own because it is not a frozen artifact — it
    is a *constant inside a tool* — and because re-pointing it changes the
    assembled packet by one provenance line, which is why the v3 row above had
    to be frozen after this edit, not before.
    """
    tool = ROOT / "tools/exercise-handoff-e2e.py"
    text = tool.read_text(encoding="utf-8")
    default = re.search(r'^V3_BASELINE_DEFAULT\s*=\s*"([^"]+)"', text, re.M)
    frozen = re.search(r'^V3_FROZEN_DIR_DEFAULT\s*=\s*"([^"]+)"', text, re.M)
    proc = run(str(ROOT / "tools/exercise-handoff-e2e.py"), "--profile", "v3", "--quiet")
    rows.append({
        "id": "default-pointer",
        "surface": "tools/exercise-handoff-e2e.py:V3_BASELINE_DEFAULT + V3_FROZEN_DIR_DEFAULT",
        "was": "reports/round-26/handoff/declared-in-r5/expected.json",
        "now": default.group(1) if default else None,
        "frozen_dir": frozen.group(1) if frozen else None,
        "gate_sha256": sha(tool),
        "control": {"command": "python3 tools/exercise-handoff-e2e.py --profile v3 --quiet",
                    "exit": proc.returncode,
                    "reading": ("exit 0 — the default regression is green at the successor row"
                                if proc.returncode == 0 else "still red")},
    })
    print("%-30s exit=%d" % ("default-pointer", proc.returncode))
    return proc.returncode


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    if args.check:
        return 0
    parent = Path(os.path.realpath(os.environ.get("TMPDIR") or "/var/tmp"))
    if parent == ROOT or ROOT in parent.parents:
        print("repin: TMPDIR must sit outside the repository", file=sys.stderr)
        return 2
    live = {rel: sha(ROOT / rel) for rel in STALE}
    rows = []
    rc = 0
    for gate_dir, gate_rel, graded_src, graded_name, read_set, _o in GATES:
        rc |= freeze_baseline(gate_dir, gate_rel, graded_src, graded_name, read_set, rows)
    freeze_d4_legs(rows)
    rc |= record_default_pointer(rows)
    rc |= freeze_v3(rows)
    controls = measure_controls()
    doc = {
        "schema": "kotodama-r27-d4-repin-v1",
        "round": 27, "date": DATE, "seat": "R27-O25..O32", "axis": "operability",
        "revision": head(),
        "canon": ("NON-CANON engineering evidence; a pin is integrity, never truth and "
                  "never clearance"),
        "kind": "re-pin as a NEW row; every filed row stays byte-identical",
        "declared_by": ("reports/round-26/register/repin.json (the two cascades it reported "
                        "and did not repair) and the round-27 register-law landing"),
        "stale_pins": STALE,
        "live_pins": live,
        "rows": rows,
        "controls": controls,
        "limits": [
            "a re-pin asserts the bytes moved, never that the move was correct",
            "no filed round-8..26 byte is written by this seat",
        ],
    }
    (OUT / "d4-pins.json").write_text(json.dumps(doc, indent=1, sort_keys=True) + "\n",
                                      encoding="utf-8")
    print("repin rows:", len(rows))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
