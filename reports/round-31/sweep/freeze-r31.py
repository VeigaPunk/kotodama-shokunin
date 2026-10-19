#!/usr/bin/env python3
"""R31-O11 — freeze the current-generation D4 replay leg (`frozen/r31-post/`).

The round-28 generation (`reports/round-28/pinsweep/frozen/r28-post/`) graded
its rows against live packet state and was superseded 4/4-mismatch by the
round-30 QREG landing — the same one-round-later cascade its own sweep report
predicted (§2.1). This seat supplies the successor, so the round-31 final
sweep has a current D4-leg replay row instead of a gap.

Append-only: everything is written under `reports/round-31/sweep/frozen/r31-post/`;
no filed byte from rounds 8-30 is read for anything but measurement. A run
refuses to re-freeze over an existing generation; it re-verifies instead.

Usage:
    export TMPDIR=/var/tmp/kotodama-r31-sweep    # outside the repo (mirror safety)
    python3 reports/round-31/sweep/freeze-r31.py            # stability-guard + freeze + replay check
    python3 reports/round-31/sweep/freeze-r31.py --check    # verify the frozen generation only
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
GEN = HERE / "frozen" / "r31-post"
DATE = dt.date.today().isoformat()
FINDING_RE = re.compile(r"^FINDING ", re.M)
SEAT = "R31-O11 (round-31 O sweep scribe)"
TMP_OUTSIDE = "/var/tmp/kotodama-r31-sweep"

# The read set whose stability the freeze demands: every byte the four rows
# grade, plus the gate revisions that grade them.
ROWS = (
    ("d4-assembly", "tools/gates/d4-assembly-check-gate.py",
     "examples/culture-d4/packet.d4.yml"),
    ("d4-typed-labels", "tools/gates/d4-typed-labels-check-gate.py",
     "examples/culture-d4/typed-labels.d4.yml"),
    ("typed-source", "tools/gates/typed-pipeline-gate.py",
     "examples/culture-d4/packet.d4.yml"),
    ("typed-typed", "tools/gates/typed-pipeline-gate.py",
     "examples/culture-d4/packet.d4.typed.yml"),
)
EXTRA_STABILITY = ("tools/gates/d4-assembly-check-gate.py",
                   "tools/gates/d4-typed-labels-check-gate.py",
                   "tools/gates/typed-pipeline-gate.py")
COLUMNS = ("gate", "gate_sha256", "input", "input_sha256", "exit_code",
           "finding_count", "output", "output_sha256", "input_snapshot", "command")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def head() -> str:
    proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                          capture_output=True, timeout=60)
    if proc.returncode:
        raise SystemExit(f"cannot read lane HEAD: {proc.stderr.decode()}")
    return proc.stdout.decode().strip()


def read_set():
    root = ROOT / "examples" / "culture-d4"
    files = sorted(path.relative_to(ROOT).as_posix() for path in root.rglob("*")
                   if path.is_file() and "__pycache__" not in path.parts)
    return files + [extra for extra in EXTRA_STABILITY if extra not in files]


def tree_digest() -> str:
    digest = hashlib.sha256()
    for relative in read_set():
        digest.update(relative.encode())
        digest.update(sha((ROOT / relative).read_bytes()).encode())
    return digest.hexdigest()


def stability_guard(pause_seconds: int) -> dict:
    first, stamp = tree_digest(), now()
    time.sleep(pause_seconds)
    second = tree_digest()
    if first != second:
        raise SystemExit("D4 read set moved during the stability window; "
                         "re-run when the wave has settled")
    return {"window_seconds": pause_seconds, "digest": first,
            "opened_at_utc": stamp, "closed_at_utc": now(),
            "files": len(read_set())}


def run_gate(gate: str, input_rel: str) -> subprocess.CompletedProcess:
    environment = {**os.environ, "TMPDIR": TMP_OUTSIDE,
                   "PYTHONDONTWRITEBYTECODE": "1"}
    return subprocess.run([sys.executable, "-B", gate, input_rel], cwd=ROOT,
                          capture_output=True, timeout=180, env=environment)


def freeze() -> dict:
    revision = head()
    stability = stability_guard(pause_seconds=20)
    GEN.mkdir(parents=True, exist_ok=False)
    (GEN / "inputs").mkdir()
    measured = []
    for name, gate, input_rel in ROWS:
        gate_bytes = (ROOT / gate).read_bytes()
        input_bytes = (ROOT / input_rel).read_bytes()
        proc = run_gate(gate, input_rel)
        out_rel = f"reports/round-31/sweep/frozen/r31-post/{name}.out"
        snapshot_rel = (f"reports/round-31/sweep/frozen/r31-post/inputs/"
                        f"{input_rel}")
        (GEN / f"{name}.out").write_bytes(proc.stdout)
        snapshot = GEN / "inputs" / input_rel
        snapshot.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / input_rel, snapshot)
        if sha(snapshot.read_bytes()) != sha(input_bytes):
            raise SystemExit(f"snapshot copy drifted: {input_rel}")
        row = {
            "name": name, "gate": gate, "gate_sha256": sha(gate_bytes),
            "input": input_rel, "input_sha256": sha(input_bytes),
            "exit_code": proc.returncode,
            "finding_count": len(FINDING_RE.findall(proc.stdout.decode("utf-8", "replace"))),
            "output": out_rel, "output_sha256": sha(proc.stdout),
            "input_snapshot": snapshot_rel,
            "command": f"python3 {gate} {input_rel}",
            "measured_at_utc": now(),
        }
        measured.append(row)
    lines = ["\t".join(COLUMNS)]
    for row in measured:
        lines.append("\t".join(str(row[column]) for column in COLUMNS))
    (GEN / "MANIFEST.tsv").write_text("\n".join(lines) + "\n", encoding="utf-8")
    receipt = {
        "schema": "kotodama-frozen-run-v1", "generation": "r31-post",
        "frozen_by": SEAT, "frozen_at_utc": now(), "date": DATE,
        "revision": revision,
        "command": "python3 reports/round-31/sweep/freeze-r31.py",
        "counting_command": "python3 reports/round-31/run-validation.py",
        "tmpdir": TMP_OUTSIDE,
        "stability_window": stability,
        "supersedes": ("reports/round-28/pinsweep/frozen/r28-post/ "
                       "(D4-leg rows superseded 4/4 mismatch by the round-30 "
                       "QREG landing; measured 2026-10-18, exit 1, "
                       "reports/round-31/sweep/ controls rows)"),
        "append_only_note": ("new rows only; no filed round-8..30 byte written; "
                             "a reproduced red verdict stays red"),
        "rows": measured,
    }
    replay = verify()
    receipt["check"] = replay
    (GEN / "freeze-receipt.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not replay["all_reproduced"]:
        shutil.rmtree(GEN)
        raise SystemExit("frozen generation does not reproduce; nothing filed")
    return receipt


def verify() -> dict:
    proc = subprocess.run(
        [sys.executable, "-B", "tools/replay-frozen.py",
         str(GEN / "MANIFEST.tsv"), "--json"],
        cwd=ROOT, capture_output=True, timeout=300,
        env={**os.environ, "TMPDIR": TMP_OUTSIDE, "PYTHONDONTWRITEBYTECODE": "1"})
    try:
        document = json.loads(proc.stdout)
    except ValueError:
        raise SystemExit(f"replay did not emit JSON: {proc.stderr.decode()[:400]}")
    summary = document.get("summary", document)
    reproduced = sum(1 for row in document.get("rows", [])
                     if row.get("status") == "reproduced")
    total = len(document.get("rows", []))
    return {"command": f"python3 tools/replay-frozen.py {GEN / 'MANIFEST.tsv'}",
            "date": DATE, "exit_code": proc.returncode,
            "reproduced": reproduced, "rows": total,
            "all_reproduced": proc.returncode == 0 and reproduced == total and total == len(ROWS)}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="verify the existing generation, never freeze")
    args = parser.parse_args(argv)
    os.environ.setdefault("TMPDIR", TMP_OUTSIDE)
    Path(TMP_OUTSIDE).mkdir(parents=True, exist_ok=True)
    if args.check or GEN.is_dir():
        if not (GEN / "MANIFEST.tsv").is_file():
            raise SystemExit("no frozen generation at frozen/r31-post/")
        replay = verify()
        print(json.dumps(replay, indent=2, sort_keys=True))
        return 0 if replay["all_reproduced"] else 1
    receipt = freeze()
    print(json.dumps({"frozen": str(GEN), "revision": receipt["revision"],
                      "rows": len(receipt["rows"]),
                      "check": receipt["check"]}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
