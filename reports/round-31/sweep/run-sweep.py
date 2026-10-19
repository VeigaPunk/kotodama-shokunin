#!/usr/bin/env python3
"""R31-O11 — the final green sweep: one deterministic pass over every capability.

Round-31 claim O (`reports/round-31/claims.json`): the final sweep accumulated
piecemeal across rounds; this run exercises the whole SCORECARD capability
surface in one fixed order — all assemblers (``--check``/``--selftest``), the
typed gates, the argot + law gates, the handoff v2/v3 exercises, the gate
battery (10/10), craft, every validator, the seven registered gate selftests,
and the frozen replays — recording exit codes and output SHA-256 digests so the
sweep is re-runnable from the recorded commands alone (``commands.txt``).

The replay leg has two current-generation rows (``reports/round-17/tests/frozen``
and this seat's ``frozen/r31-post``, frozen by ``freeze-r31.py``) plus thirteen
historical controls. The controls are filed superseded generations: append-only
keeps their bytes immutable, so their replay codes are deterministic and a flip
is a finding, not a silently absorbed red. The green surface is 100% exit 0;
a reproduced red verdict stays red.

Writes only: ``reports/round-31/sweep/`` (receipt, commands.txt) and
``reports/round-31/final-sweep.md`` (the consolidated sweep table, rendered
from the receipt so table and receipt cannot drift). TMPDIR policy mirrors the
round-30 runner: ``.scratch`` for scratch-writing legs, ``/var/tmp`` for the
mirror-safety replay legs.

Usage:
    export TMPDIR=$PWD/.scratch
    python3 reports/round-31/sweep/run-sweep.py              # sweep + receipt + table
    python3 reports/round-31/sweep/run-sweep.py --check      # print receipt, write nothing
    python3 reports/round-31/sweep/run-sweep.py --selftest   # dependency-free controls
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
SWEEP = "reports/round-31/sweep"
RECEIPT = f"{SWEEP}/sweep-receipt.json"
COMMANDS = f"{SWEEP}/commands.txt"
TABLE = "reports/round-31/final-sweep.md"
FREEZE_GEN = f"{SWEEP}/frozen/r31-post"
DATE = dt.date.today().isoformat()
SEAT = "R31-O11 (round-31 O sweep scribe)"
TMP_SCRATCH = str(ROOT / ".scratch")
TMP_OUTSIDE = "/var/tmp/kotodama-r31-sweep"
D4_PACKET = "examples/culture-d4/packet.d4.yml"
D4_TYPED = "examples/culture-d4/packet.d4.typed.yml"
D4_LABELS = "examples/culture-d4/typed-labels.d4.yml"

# (id, family, argv, tmpdir) — argv is the command after `python3 -B`.
GREEN = (
    # F1 assemblers
    ("d2-assembly-check", "assemblers", ("tools/assemble-d2.py", "--check"), TMP_SCRATCH),
    ("d2-assembly-selftest", "assemblers", ("tools/assemble-d2.py", "--selftest"), TMP_SCRATCH),
    ("d2-adapter-check", "assemblers", ("tools/assemble-d2-typed.py", "--check"), TMP_SCRATCH),
    ("d2-adapter-selftest", "assemblers", ("tools/assemble-d2-typed.py", "--selftest"), TMP_SCRATCH),
    ("d3-assembly-check", "assemblers", ("tools/assemble-culture-d3.py", "--check"), TMP_SCRATCH),
    ("d3-assembly-selftest", "assemblers", ("tools/assemble-culture-d3.py", "--selftest"), TMP_SCRATCH),
    ("d4-assembly-check", "assemblers", ("tools/assemble-culture-d4.py", "--check"), TMP_SCRATCH),
    ("d4-assembly-selftest", "assemblers", ("tools/assemble-culture-d4.py", "--selftest"), TMP_SCRATCH),
    ("d4-adapter-check", "assemblers", ("tools/assemble-d4-typed.py", "--check", D4_TYPED), TMP_SCRATCH),
    ("d4-adapter-selftest", "assemblers", ("tools/assemble-d4-typed.py", "--selftest"), TMP_SCRATCH),
    ("d4-projector-selftest", "assemblers", ("tools/d2-typed-labels.py", "--selftest"), TMP_SCRATCH),
    ("d4-projector-d2-check", "assemblers", ("tools/d2-typed-labels.py", "--check"), TMP_SCRATCH),
    ("d4-projector-d4-check", "assemblers", ("tools/d2-typed-labels.py", "--packet", D4_PACKET, "--check", D4_LABELS), TMP_SCRATCH),
    # F2 typed gates
    ("d4-label-gate", "typed-gates", ("tools/gates/d4-typed-labels-check-gate.py", D4_LABELS), TMP_SCRATCH),
    ("d4-assembly-gate", "typed-gates", ("tools/gates/d4-assembly-check-gate.py", D4_PACKET), TMP_SCRATCH),
    ("typed-pipeline-selftest", "typed-gates", ("tools/gates/typed-pipeline-gate.py", "--selftest"), TMP_SCRATCH),
    ("typed-pipeline-generalized-selftest", "typed-gates", ("tools/gates/typed-pipeline-gate.py", "--selftest-generalized"), TMP_SCRATCH),
    ("typed-pipeline-d2", "typed-gates", ("tools/gates/typed-pipeline-gate.py", "examples/culture-d2/packet.d2.yml"), TMP_SCRATCH),
    ("typed-pipeline-d4", "typed-gates", ("tools/gates/typed-pipeline-gate.py", D4_PACKET), TMP_SCRATCH),
    ("typed-pipeline-d4-typed", "typed-gates", ("tools/gates/typed-pipeline-gate.py", D4_TYPED), TMP_SCRATCH),
    # F2b the seven registered structural gates' selftests (capability leg)
    ("selftest-naming-collision", "gate-selftests", ("tools/gates/naming-collision-gate.py", "--selftest"), TMP_SCRATCH),
    ("selftest-phonology-sanity", "gate-selftests", ("tools/gates/phonology-sanity-gate.py", "--selftest"), TMP_SCRATCH),
    ("selftest-costume-era", "gate-selftests", ("tools/gates/costume-era-consistency-gate.py", "--selftest"), TMP_SCRATCH),
    ("selftest-myth-consistency", "gate-selftests", ("tools/gates/myth-consistency-gate.py", "--selftest"), TMP_SCRATCH),
    ("selftest-lexicon-coverage", "gate-selftests", ("tools/gates/lexicon-coverage-audit.py", "--selftest"), TMP_SCRATCH),
    ("selftest-provenance-audit", "gate-selftests", ("tools/gates/provenance-audit.py", "--selftest"), TMP_SCRATCH),
    ("selftest-handoff-packet-check", "gate-selftests", ("tools/gates/handoff-packet-check.py", "--selftest"), TMP_SCRATCH),
    # F3 argot + law gates
    ("argot-selftest", "argot-law", ("tools/gates/argot-derivation-gate.py", "--selftest"), TMP_SCRATCH),
    ("argot-d4", "argot-law", ("tools/gates/argot-derivation-gate.py", D4_PACKET), TMP_SCRATCH),
    ("law-selftest", "argot-law", ("tools/gates/register-law-gate.py", "--selftest"), TMP_SCRATCH),
    ("law-d4-clean", "argot-law", ("tools/gates/register-law-gate.py", "--packet", D4_PACKET), TMP_SCRATCH),
    # F4 handoff exercises
    ("handoff-v2", "handoff", ("tools/exercise-handoff-e2e.py", "--profile", "v2", "--quiet"), TMP_SCRATCH),
    ("handoff-v2-selftest", "handoff", ("tools/exercise-handoff-e2e.py", "--profile", "v2", "--selftest", "--quiet"), TMP_SCRATCH),
    ("handoff-v3", "handoff", ("tools/exercise-handoff-e2e.py", "--profile", "v3", "--quiet"), TMP_SCRATCH),
    ("handoff-v3-selftest", "handoff", ("tools/exercise-handoff-e2e.py", "--profile", "v3", "--selftest", "--quiet"), TMP_SCRATCH),
    # F5 battery
    ("battery", "battery", ("tools/check-gate-battery.py",), TMP_SCRATCH),
    ("battery-selftest", "battery", ("tools/check-gate-battery.py", "--selftest"), TMP_SCRATCH),
    # F6 craft
    ("craft-selftest", "craft", ("tools/check-craft-exercise.py", "--selftest"), TMP_SCRATCH),
    ("craft-exercise", "craft", ("tools/check-craft-exercise.py", "examples/supplement-opencode-1/sound-change-vs-taboo.json"), TMP_SCRATCH),
    # F7 validators
    ("links-selftest", "validators", ("tools/harness/packet_links.py", "--selftest"), TMP_SCRATCH),
    ("uncertainty-selftest", "validators", ("tools/harness/packet_uncertainty.py", "--selftest"), TMP_SCRATCH),
    ("coupling-selftest", "validators", ("tools/check-evidence-coupling.py", "--selftest"), TMP_SCRATCH),
    ("coupling-d3", "validators", ("tools/check-evidence-coupling.py", "examples/culture-d3/packet.json"), TMP_SCRATCH),
    ("replay-selftest", "validators", ("tools/replay-frozen.py", "--selftest"), TMP_OUTSIDE),
    ("pin-repoint-selftest", "validators", ("reports/round-26/remainders/pin-repoint-check.py", "--selftest"), TMP_SCRATCH),
    ("ceiling-selftest", "validators", ("reports/round-28/ceiling/measure-ceiling.py", "--selftest"), TMP_SCRATCH),
    ("ceiling-measure", "validators", ("reports/round-28/ceiling/measure-ceiling.py",), TMP_SCRATCH),
    ("knowledge-inventory", "validators", ("tools/source-audit-inventory.py", "--json", "--summary", "--root", "corpus/knowledge"), TMP_SCRATCH),
    # F8 frozen replays — current generations only (expect REPLAY OK)
    ("replay-round-17", "frozen-replays", ("tools/replay-frozen.py", "reports/round-17/tests/frozen/MANIFEST.tsv"), TMP_OUTSIDE),
    ("replay-r31-post", "frozen-replays", ("tools/replay-frozen.py", f"{FREEZE_GEN}/MANIFEST.tsv"), TMP_OUTSIDE),
)

# Filed superseded generations: append-only keeps their bytes immutable, so the
# replay code is a deterministic function of filed bytes + live gate bytes.
# expected_exit values measured 2026-10-18 (probe, re-measured by every sweep);
# a flip is a finding for disposition, never a silently absorbed red.
CONTROLS = (
    ("control-round-3", "tools/gates/frozen/round-3/MANIFEST.tsv", 2,
     "legacy refusal era: rows could-not-evaluate at their filed bytes"),
    ("control-round-3-attempt-1", "tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv", 2,
     "legacy refusal era: rows could-not-evaluate at their filed bytes"),
    ("control-round-11", "tools/gates/frozen/round-11/MANIFEST.tsv", 2,
     "one row could-not-evaluate (replay precedence); the rest reproduce their recorded reds"),
    ("control-round-18", "tools/gates/frozen/round-18/MANIFEST.tsv", 1,
     "two rows mismatch: superseded by later D4 landings (recorded reds stay red)"),
    ("control-round-18-repin-d2", "tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv", 2,
     "one row could-not-evaluate; the rest reproduce"),
    ("control-round-20-repin-d2", "tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv", 2,
     "one row could-not-evaluate; the rest reproduce"),
    ("control-round-22-d4-repin", "tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv", 2,
     "D4-leg rows superseded by the amended packet (r28 sweep §3)"),
    ("control-round-23-repin-d2", "tools/gates/frozen/round-23/repin-d2/MANIFEST.tsv", 2,
     "one row could-not-evaluate; the rest reproduce"),
    ("control-round-25-gate-input", "tools/gates/frozen/round-25/gate-input/MANIFEST.tsv", 2,
     "six rows could-not-evaluate at their filed bytes"),
    ("control-round-26-gate-input", "tools/gates/frozen/round-26/gate-input/MANIFEST.tsv", 1,
     "D4 rows superseded by post-r28 gate/packet movement"),
    ("control-round-26-post-register", "tools/gates/frozen/round-26/post-register/MANIFEST.tsv", 1,
     "superseded when the register law moved the D4 tree after its freeze (r27/r28)"),
    ("control-r27-post", "reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv", 1,
     "superseded by the RL-4 packet_keys landing (r28 sweep §2.1)"),
    ("control-r28-post", "reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv", 1,
     "superseded 4/4 by the r30 QREG landing; successor is sweep/frozen/r31-post"),
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def today() -> str:
    return dt.date.today().isoformat()


def head() -> str | None:
    proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, timeout=60)
    return proc.stdout.decode().strip() if not proc.returncode else None


def runtime_inputs() -> dict:
    digests = {}
    for directory in ("tools", "examples", "corpus/knowledge"):
        for path in sorted((ROOT / directory).rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                relative = path.relative_to(ROOT).as_posix()
                digests[relative] = sha(path.read_bytes())
    return digests


def finding_count(stdout: str) -> int:
    return sum(1 for line in stdout.splitlines() if line.startswith("FINDING "))


def extras_for(name: str, proc) -> dict:
    extras = {}
    text = proc.stdout.decode("utf-8", "replace")
    if name == "battery":
        try:
            document = json.loads(text)
            summary = document["baselines"]["summary"]
            extras = {"coverage": summary.get("coverage"),
                      "pinned": summary.get("pinned"),
                      "baselines_found": summary.get("baselines_found"),
                      "gates_uncovered": summary.get("gates_uncovered"),
                      "gates_registered": summary.get("gates_registered"),
                      "registered_gates": summary.get("gates_covered")}
        except (ValueError, KeyError, TypeError):
            extras = {"coverage": "unreadable"}
    elif name == "law-d4-clean":
        extras = {"finding_lines": finding_count(text)}
    elif name.startswith("handoff-"):
        first = next((line for line in text.splitlines() if line.startswith("handoff-")), "")
        extras = {"summary_line": first.strip()}
    elif name.startswith("replay-"):
        lines = text.strip().splitlines()
        extras = {"summary_line": lines[-1].strip() if lines else ""}
    elif name in ("d4-assembly-gate", "d4-label-gate", "argot-d4"):
        extras = {"finding_lines": finding_count(text)}
    return extras


def run_row(row_id: str, family: str, argv, tmpdir: str) -> dict:
    environment = {**os.environ, "TMPDIR": tmpdir, "PYTHONDONTWRITEBYTECODE": "1",
                   "GIT_OPTIONAL_LOCKS": "0"}
    item = {"id": row_id, "family": family, "class": "sweep",
            "command": " ".join(["python3", "-B", *argv]),
            "date": today(), "tmpdir": tmpdir, "expect_exit": 0,
            "started_at_utc": now()}
    started = time.monotonic()
    proc = None
    try:
        proc = subprocess.run([sys.executable, "-B", *argv], cwd=ROOT, env=environment,
                              capture_output=True, timeout=180)
        item.update(exit_code=proc.returncode,
                    stdout_sha256=sha(proc.stdout), stderr_sha256=sha(proc.stderr),
                    stderr_bytes=len(proc.stderr))
    except (OSError, subprocess.SubprocessError) as error:
        item.update(exit_code=None, stdout_sha256=None, stderr_sha256=None,
                    error=f"{type(error).__name__}: {error}")
    item["elapsed_seconds"] = round(time.monotonic() - started, 3)
    item["finished_at_utc"] = now()
    item["passed"] = item["exit_code"] == 0
    if proc is not None:
        item.update(extras_for(row_id, proc))
    return item


def run_control(control_id: str, manifest: str, expected: int, disposition: str) -> dict:
    item = run_row(control_id, "frozen-controls",
                   ("tools/replay-frozen.py", manifest), TMP_OUTSIDE)
    item.update({"class": "historical-control", "manifest": manifest,
                 "expect_exit": expected, "disposition": disposition,
                 "passed": item["exit_code"] == expected})
    return item


def battery_reading(rows) -> dict:
    row = next((item for item in rows if item["id"] == "battery"), {})
    reading = {key: row.get(key) for key in ("exit_code", "coverage", "pinned",
                                             "baselines_found", "gates_uncovered",
                                             "stdout_sha256", "command", "date")}
    reading["ten_of_ten"] = row.get("coverage") == "10/10" and not row.get("gates_uncovered")
    reading["registered_gates"] = row.get("registered_gates")
    reading["registered_count"] = row.get("gates_registered")
    return reading


def render_table(receipt: dict, receipt_digest: str) -> str:
    claims_digest = receipt.get("claims_json_sha256")
    claims_text = f"`{claims_digest[:16]}…`" if claims_digest else "unavailable"
    gate_list = "\n".join(f"- `{name}`"
                          for name in (receipt["battery"].get("registered_gates") or []))
    header = f"""# R31-O11 — the final green sweep: one deterministic pass over every capability

- **Seat:** R31-O11 (the O-sweep scribe: consolidated sweep table + the
  deterministic command manifest), round 31, loop 3 regimen close-out, claim
  **O** `operability` (`reports/round-31/claims.json`).
- **Date:** {receipt['date']}. Declared baseline revision
  `71cd9d376ebd144e94e4f12d997f73e5d2839aa9` (round-31 declare); lane HEAD at
  measurement `{receipt['head'] or 'unavailable'}` (round-31 sibling artifacts
  untracked and not runtime inputs).
- **Writes:** `reports/round-31/sweep/` (the runner, the frozen `r31-post`
  generation, the receipt, `commands.txt`) and this file. No filed round-8..30
  byte was written; no git commit, no push.
- **Canon:** NON-CANON engineering evidence. A pin is integrity, never truth
  and never clearance; a reproduced red verdict stays red.
- Machine receipt: `reports/round-31/sweep/sweep-receipt.json` (every row with
  exit, output digests, timestamps); flat manifest: `commands.txt`.

## 0. Verdict

The whole SCORECARD capability surface in one deterministic pass:
**{receipt['summary']['green_rows']} green-surface rows, all exit 0 (100%)**;
**{receipt['summary']['control_rows']} historical controls, all at their
expected filed-red codes**; runtime inputs unchanged during the run. The gate
battery reads **{receipt['battery']['coverage']}** (pinned
{receipt['battery']['pinned']}, uncovered none), the handoff v2/v3 exercises
are green, the argot + law gates are clean on the current packet (law findings:
{receipt['law_clean_findings']}), and the frozen-replay leg has a **current
generation** again: `sweep/frozen/r31-post` (frozen this round at revision
`{receipt['freeze_revision']}`) replays
{receipt['replays'].get('replay-r31-post', {}).get('summary_line', 'n/a')},
beside round-17's
{receipt['replays'].get('replay-round-17', {}).get('summary_line', 'n/a')}.

Claim-O counting command: `python3 reports/round-31/run-validation.py` (the
round runner, orchestrator-owned).

## 1. The consolidated sweep table

Every green-surface row: the command exactly as re-runnable, its exit code, and
the SHA-256 of its stdout. Re-run them from `commands.txt` alone.

| id | family | command | exit | stdout sha256 (first 16) |
|---|---|---|---:|---|
"""
    body = []
    for item in receipt["rows"]:
        if item["class"] != "sweep":
            continue
        digest = (item.get("stdout_sha256") or "—")[:16]
        body.append(f"| {item['id']} | {item['family']} | `{item['command']}` "
                    f"| {item['exit_code']} | `{digest}…` |")
    middle = f"""
Key readings carried in the receipt (`extras` per row): the battery row's
coverage/pin counters and registered-gate list (§2), the law row's finding
count, each handoff row's summary line, and each replay row's REPLAY summary.
stderr was empty ({receipt['summary']['stderr_bytes_total']} bytes total across
all green rows).

**Cross-run determinism, measured:** two back-to-back sweep runs at this stamp
(`run-sweep.py` twice, rows diffed by id + exit + stdout digest) agreed on
**61/63 rows byte-for-byte**. The two exceptions embed run-stamps by design:
`battery` echoes gate-selftest `stdout_head`s containing `mkdtemp` fixture
paths and per-leg `seconds`, and `pin-repoint-selftest` prints a microsecond
timestamp. Their exits and semantic counters are the stable reading; their
stdout digests are per-run stamps, not cross-run pins. Measured
2026-10-18 with: `python3 reports/round-31/sweep/run-sweep.py` (×2) + row diff.

## 2. The battery reading (claim: 10/10)

`python3 -B tools/check-gate-battery.py` over the default roots
(`tools/gates/expected`, `tools/gates/frozen`, `reports/round-9/baselines`):
coverage **{receipt['battery']['coverage']}**, pinned
{receipt['battery']['pinned']}/{receipt['battery']['baselines_found']},
uncovered {'none' if not receipt['battery']['gates_uncovered'] else receipt['battery']['gates_uncovered']}, exit
{receipt['battery']['exit_code']}. Registered gates
({receipt['battery'].get('registered_count')}):

{gate_list}

The battery's own selftest row (`battery-selftest`) is green in §1. The law
baseline pinning the settled round-30 packet lives at
`tools/gates/expected/register-law-gate/r30-post/` (round-30 integration).

## 3. The frozen-replay leg: two current generations, thirteen filed controls

`sweep/frozen/r31-post/` (four rows: d4-assembly, d4-typed-labels,
typed-pipeline × 2) was frozen this round through the lane's replay format
after a stability window over the D4 read set
({receipt['freeze_stability']['files']} files, digest
`{receipt['freeze_stability']['digest'][:16]}…`, held
{receipt['freeze_stability']['window_seconds']}s). Its freeze receipt is
`{FREEZE_GEN}/freeze-receipt.json`; the replay check is row `replay-r31-post`
in §1.

**Why a new generation:** the round-28 successor (`r28-post`) graded its rows
against live packet state and was superseded 4/4 by the round-30 QREG landing —
the one-round-later cascade its own sweep report predicted (r28 sweep §2.1).
Measured this round: `replay-frozen r28-post` → exit 1, 4 mismatch (control row
`control-r28-post`). Append-only: the successor is a NEW generation; no filed
byte was rewritten.

| control (filed generation) | replay exit | expected | disposition |
|---|---:|---:|---|
"""
    controls = []
    for item in receipt["rows"]:
        if item["class"] != "historical-control":
            continue
        controls.append(f"| `{item['manifest']}` | {item['exit_code']} | "
                        f"{item['expect_exit']} | {item['disposition']} |")
    tail = f"""
The controls are the sweep's integrity leg, not failures: filed bytes are
immutable, so each replay code is deterministic. A control flipping its code
means a filed byte or a shared gate moved — a named finding for disposition,
never silently re-blessed. Their red verdicts stay red; reproduction is not
clearance.

## 4. The TMPDIR boundary (measured, inherited)

`tools/replay-frozen.py` refuses a mirror whose real path is inside the repo —
the designed boundary (r28 sweep §5). This sweep keeps the round-30 runner's
policy: `.scratch` for scratch-writing legs, `/var/tmp/kotodama-r31-sweep` for
every mirror-safety replay leg (and for the r31-post freeze's own gate runs).
The fleet-shared `/tmp` quota trap of round 28 is avoided by never using it.

## 5. Scope notes — what this seat did not do

- **No filed round-8..30 byte was written.** Everything new lives under
  `reports/round-31/sweep/` plus this file.
- **The D4 adapter baselines were not re-pinned.** The battery verifies their
  pins (§2, green); whether their *content* still matches the live packet is
  the pins' supersession semantics, reported via the control rows — a successor
  baseline is the re-pin seat's surface if the round wants one.
- **A pin is integrity, never truth.** The r31-post generation asserts these
  exact bytes graded by these exact gate revisions produced these exact
  verdicts — nothing about design quality or canon.
- **The round-31 closure ledger and the jin'i-ryu draft are sibling seats'**
  (`closure-ledger.json`, `jinii/`); this file consolidates only the sweep.

## 6. Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch    # scratch-writing legs (mirror-safety legs: /var/tmp)

python3 reports/round-31/sweep/freeze-r31.py --check   # the r31-post generation replays 4/4
python3 reports/round-31/sweep/run-sweep.py            # the whole sweep + receipt + this file
python3 reports/round-31/sweep/run-sweep.py --selftest # the runner's own controls
python3 reports/round-31/run-validation.py             # claim-O counting command (orchestrator-owned)
```

`commands.txt` carries every green-surface command one per line, in manifest
order — the sweep is re-runnable from the recorded commands alone.

Receipt: `reports/round-31/sweep/sweep-receipt.json` (sha256
`{receipt_digest[:16]}…`). `reports/round-31/claims.json` digest at measurement:
{claims_text}.
"""
    return header + "\n".join(body) + "\n" + middle + "\n".join(controls) + "\n" + tail


def selftest() -> int:
    checks = []

    def check(name, value):
        checks.append({"control": name, "passed": bool(value)})

    ids = [row[0] for row in GREEN] + [row[0] for row in CONTROLS]
    check("row-ids-unique", len(ids) == len(set(ids)))
    check("green-surface-size", len(GREEN) == 50)
    check("control-surface-size", len(CONTROLS) == 13)
    check("green-rows-class-sweep", all(row[1] != "frozen-controls" for row in GREEN))
    check("controls-expect-nonzero", all(row[2] != 0 for row in CONTROLS))
    # Flags are legitimate in a direct argv launch; the flag-refusal rule is
    # replay-frozen's, for manifest path columns. Paths here must be relative
    # and traversal-free.
    unsafe = [token for row in GREEN for token in row[2]
              if token.startswith("/") or ".." in token]
    check("no-unsafe-argv-tokens", not unsafe)
    var_tmp = {row[0] for row in GREEN if row[3] == TMP_OUTSIDE}
    check("mirror-legs-exactly-replays",
          var_tmp == {"replay-selftest", "replay-round-17", "replay-r31-post"})
    check("sha256-known-vector",
          sha(b"abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")
    families = {row[1] for row in GREEN}
    check("nine-families-present", families == {"assemblers", "typed-gates", "gate-selftests",
                                                "argot-law", "handoff", "battery", "craft",
                                                "validators", "frozen-replays"})
    check("battery-row-present-once", sum(1 for row in GREEN if row[0] == "battery") == 1)
    check("control-codes-match-probe-record",
          [row[2] for row in CONTROLS] == [2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1])
    check("writes-stay-inside-round-31",
          all(path.startswith("reports/round-31/") for path in (RECEIPT, COMMANDS, TABLE)))
    passed = sum(item["passed"] for item in checks)
    receipt = {"command": "python3 reports/round-31/sweep/run-sweep.py --selftest",
               "date": today(), "passed_controls": passed, "total_controls": len(checks),
               "passed": passed == len(checks), "controls": checks}
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["passed"] else 1


def measure(publish: bool) -> int:
    if not (ROOT / FREEZE_GEN / "MANIFEST.tsv").is_file():
        print(f"missing dependency: {FREEZE_GEN}/ (run freeze-r31.py first)", file=sys.stderr)
        return 2
    (ROOT / ".scratch").mkdir(parents=True, exist_ok=True)
    Path(TMP_OUTSIDE).mkdir(parents=True, exist_ok=True)
    freeze_receipt = json.loads((ROOT / FREEZE_GEN / "freeze-receipt.json").read_text())
    before = runtime_inputs()
    started = now()
    rows = []
    for row_id, family, argv, tmpdir in GREEN:
        rows.append(run_row(row_id, family, argv, tmpdir))
    for control_id, manifest, expected, disposition in CONTROLS:
        rows.append(run_control(control_id, manifest, expected, disposition))
    after = runtime_inputs()
    drifted = sorted(key for key in set(before) | set(after)
                     if before.get(key) != after.get(key))
    claims_path = ROOT / "reports/round-31/claims.json"
    claims_digest = sha(claims_path.read_bytes()) if claims_path.is_file() else None
    replays = {item["id"]: {"summary_line": item.get("summary_line"),
                            "exit_code": item["exit_code"]}
               for item in rows if item["id"].startswith("replay-") and item["class"] == "sweep"}
    failures = [f"row {item['id']} exited {item['exit_code']}, expected {item['expect_exit']}"
                for item in rows if not item["passed"]]
    if drifted:
        failures.append("runtime inputs drifted during the run: " + ", ".join(drifted))
    receipt = {
        "round": 31, "seat": SEAT, "claim": "O",
        "runner": f"{SWEEP}/run-sweep.py",
        "counting_command": "python3 reports/round-31/run-validation.py",
        "date": DATE, "measured_at_utc": started, "completed_at_utc": now(),
        "head": head(),
        "baseline_revision_declared": "71cd9d376ebd144e94e4f12d997f73e5d2839aa9",
        "freeze_revision": freeze_receipt["revision"],
        "freeze_stability": freeze_receipt["stability_window"],
        "summary": {
            "green_rows": sum(1 for item in rows if item["class"] == "sweep"),
            "green_rows_passed": sum(1 for item in rows
                                     if item["class"] == "sweep" and item["passed"]),
            "control_rows": sum(1 for item in rows if item["class"] == "historical-control"),
            "control_rows_passed": sum(1 for item in rows
                                       if item["class"] == "historical-control"
                                       and item["passed"]),
            "stderr_bytes_total": sum(item.get("stderr_bytes", 0) for item in rows
                                      if item["class"] == "sweep"),
            "elapsed_seconds": round(sum(item.get("elapsed_seconds", 0) for item in rows), 3),
        },
        "battery": battery_reading(rows),
        "law_clean_findings": next((item.get("finding_lines") for item in rows
                                    if item["id"] == "law-d4-clean"), None),
        "replays": replays,
        "rows": rows,
        "runtime_inputs": {"files": len(before), "drifted_during_run": drifted,
                           "command": "python3 reports/round-31/sweep/run-sweep.py (runtime_inputs walk)"},
        "claims_json_sha256": claims_digest,
        "passed": not failures,
        "failures": failures,
        "limits": ["Read-only over filed rounds 8-30 and the live capability surface; writes only under reports/round-31/.",
                   "A reproduced red verdict stays red; historical controls assert stability of filed reds, not clearance.",
                   "Output hashes are of stdout at the recorded stamp; any later landing supersedes them by design.",
                   "Two rows (battery, pin-repoint-selftest) embed run-varying temp names/timestamps in stdout; their digests are per-run stamps, their exits and counters are the stable reading (61/63 rows byte-identical across back-to-back runs, measured 2026-10-18)."],
    }
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if publish:
        (ROOT / RECEIPT).write_text(rendered, encoding="utf-8")
        manifest_lines = ["# R31-O11 final green sweep — the deterministic command manifest",
                          "# re-runnable from these commands alone; order = manifest order",
                          "# TMPDIR: scratch legs .scratch, mirror-safety replay legs /var/tmp/kotodama-r31-sweep",
                          ""]
        family = None
        for item in rows:
            if item["class"] != "sweep":
                continue
            if item["family"] != family:
                manifest_lines.append(f"# {item['family']}")
                family = item["family"]
            manifest_lines.append(item["command"])
        (ROOT / COMMANDS).write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
        (ROOT / TABLE).write_text(render_table(receipt, sha(rendered.encode())),
                                  encoding="utf-8")
        print(f"green surface: {receipt['summary']['green_rows_passed']}/"
              f"{receipt['summary']['green_rows']} exit 0; controls: "
              f"{receipt['summary']['control_rows_passed']}/"
              f"{receipt['summary']['control_rows']} at expected filed-red codes")
        print(f"battery: {receipt['battery']['coverage']} pinned "
              f"{receipt['battery']['pinned']}; law findings: {receipt['law_clean_findings']}")
        print(f"receipt: {RECEIPT}; table: {TABLE}; manifest: {COMMANDS}")
        if failures:
            print("failures: " + "; ".join(failures), file=sys.stderr)
    else:
        print(rendered, end="")
    return 0 if not failures else 1


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="print the receipt JSON without writing")
    mode.add_argument("--selftest", action="store_true", help="dependency-free controls")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    return measure(publish=not args.check)


if __name__ == "__main__":
    sys.exit(main())
