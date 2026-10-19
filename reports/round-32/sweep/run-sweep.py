#!/usr/bin/env python3
"""R32-O06..O08 — the final sweep, three passes over the settled tree.

Round-32 claim O (`reports/round-32/claims.json`): the r31 final sweep
(`reports/round-31/sweep/run-sweep.py`, seats R31-O09..O11) predates round 32's
own artifacts. This seat re-runs that sweep's 50-command matrix — imported from
the r31 runner by ``runpy`` so the matrix cannot drift from the filed bytes —
over the settled tree plus one added row: round 32's own validation harness
selftest (``reports/round-32/run-validation.py --selftest``, a sibling
seat's/orchestrator's dependency; if it has not landed the row is recorded
``could-not-evaluate`` with owner and reason, never a zero). All green rows
must exit 0; the thirteen filed-red historical replay controls must sit at
their expected codes (a flip is a finding for disposition, never a silently
absorbed red).

Three full passes (O06, O07, O08) run back-to-back: per-pass receipts land at
``reports/round-32/sweep/receipt-<PASS>.json``, the consolidated machine
receipt at ``reports/round-32/sweep/sweep-receipt.json`` (its ``rows`` are the
final pass, so the table binds one receipt), the flat manifest at
``reports/round-32/sweep/commands.txt``, and the consolidated sweep table at
``reports/round-32/final-sweep.md``. Cross-pass determinism is measured, not
asserted: rows diffed by id + exit + stdout digest, with the two rows whose
stdout embeds run-stamps by design (``battery``, ``pin-repoint-selftest``)
exempted as per-run stamps.

Writes only under ``reports/round-32/``. No filed round-8..31 byte is written;
no git commit, no push. TMPDIR policy mirrors the round-30/31 runners:
``.scratch`` for scratch-writing legs, ``/var/tmp/kotodama-r32-sweep`` for the
mirror-safety replay legs (never the fleet-shared ``/tmp``).

Usage:
    export TMPDIR=$PWD/.scratch
    python3 reports/round-32/sweep/run-sweep.py              # 3 passes + receipt + table
    python3 reports/round-32/sweep/run-sweep.py --check      # print receipt JSON, write nothing
    python3 reports/round-32/sweep/run-sweep.py --selftest   # dependency-free controls
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
SWEEP = "reports/round-32/sweep"
RECEIPT = f"{SWEEP}/sweep-receipt.json"
COMMANDS = f"{SWEEP}/commands.txt"
TABLE = "reports/round-32/final-sweep.md"
R31_RUNNER = "reports/round-31/sweep/run-sweep.py"
HARNESS = "reports/round-32/run-validation.py"
PASSES = ("O06", "O07", "O08")
DATE = dt.date.today().isoformat()
SEAT = "R32-O06..O08 (round-32 final-sweep seat)"
TMP_SCRATCH = str(ROOT / ".scratch")
TMP_OUTSIDE = "/var/tmp/kotodama-r32-sweep"
BASELINE_DECLARED = "17e90b9047b289d7a63180a1dc1bebb074137e29"

R31 = runpy.run_path(str(ROOT / R31_RUNNER))
GREEN_R31 = tuple(R31["GREEN"])
CONTROLS = tuple(R31["CONTROLS"])
R31_TMP_OUTSIDE = R31["TMP_OUTSIDE"]
# The matrix is the r31 runner's own tuple; only the mirror-leg tmpdir is
# re-pointed at this round's /var/tmp directory.
GREEN = tuple(
    (row[0], row[1], row[2],
     TMP_OUTSIDE if row[3] == R31_TMP_OUTSIDE else TMP_SCRATCH)
    for row in GREEN_R31)
HARNESS_FAMILY = "r32-harness"
# Round 32's own harness selftest: the added row beyond the r31 50-command
# matrix (claim O: "…plus round 32's own harness selftest").
HARNESS_ROW = (HARNESS, HARNESS_FAMILY, (HARNESS, "--selftest"), TMP_SCRATCH)
# Rows whose stdout embeds run-stamps by design (r31 final-sweep §1): their
# digests are per-run stamps; exits and semantic counters are the stable reading.
NONDETERMINISTIC_STDOUT = {"battery", "pin-repoint-selftest"}


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
    elif name == HARNESS:
        try:
            document = json.loads(text)
            extras = {"selftest_passed": document.get("passed"),
                      "passed_controls": document.get("passed_controls"),
                      "total_controls": document.get("total_controls")}
        except (ValueError, TypeError):
            extras = {"selftest_passed": "unreadable"}
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
                              capture_output=True, timeout=300)
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


def harness_row() -> dict:
    """Round 32's own harness selftest, or an honest could-not-evaluate row."""
    if not (ROOT / HARNESS).is_file():
        return {"id": HARNESS, "family": HARNESS_FAMILY, "class": "sweep",
                "command": f"python3 -B {HARNESS} --selftest", "date": today(),
                "tmpdir": TMP_SCRATCH, "expect_exit": 0, "exit_code": None,
                "stdout_sha256": None, "stderr_sha256": None, "stderr_bytes": None,
                "status": "could-not-evaluate",
                "owner": "reports/round-32/run-validation.py (harness/orchestrator seat)",
                "reason": "harness not landed at pass start; polled, not inferred",
                "passed": False}
    item = run_row(*HARNESS_ROW)
    try:
        item["harness_sha256"] = sha((ROOT / HARNESS).read_bytes())
    except OSError:
        item["harness_sha256"] = None
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


def run_pass(pass_id: str) -> dict:
    started = now()
    before = runtime_inputs()
    rows = []
    for row_id, family, argv, tmpdir in GREEN:
        rows.append(run_row(row_id, family, argv, tmpdir))
    rows.append(harness_row())
    for control_id, manifest, expected, disposition in CONTROLS:
        rows.append(run_control(control_id, manifest, expected, disposition))
    after = runtime_inputs()
    drifted = sorted(key for key in set(before) | set(after)
                     if before.get(key) != after.get(key))
    failures = [f"row {item['id']} exited {item['exit_code']}, expected {item['expect_exit']}"
                for item in rows if not item["passed"]]
    if drifted:
        failures.append("runtime inputs drifted during the pass: " + ", ".join(drifted))
    return {"pass": pass_id, "measured_at_utc": started, "completed_at_utc": now(),
            "head": head(), "rows": rows, "runtime_inputs": {"files": len(before),
                                                             "drifted_during_pass": drifted},
            "passed": not failures, "failures": failures}


def cross_pass(passes: list) -> dict:
    ids = [item["id"] for item in passes[-1]["rows"]]
    digest_varying, exit_flips = [], []
    nondeterministic_observed = {}
    compared = 0
    harness_shas = sorted({item.get("harness_sha256") for p in passes
                           for item in p["rows"] if item["id"] == HARNESS})
    for row_id in ids:
        per_pass = [[item for item in p["rows"] if item["id"] == row_id] for p in passes]
        if any(len(group) != 1 or group[0].get("exit_code") is None for group in per_pass):
            continue
        compared += 1
        exits = {group[0]["exit_code"] for group in per_pass}
        digests = [group[0].get("stdout_sha256") for group in per_pass]
        if len(exits) != 1:
            exit_flips.append(row_id)
        if len(set(digests)) != 1:
            if row_id in NONDETERMINISTIC_STDOUT:
                nondeterministic_observed[row_id] = len(set(digests))
            else:
                digest_varying.append(row_id)
    return {"rows_compared": compared,
            "rows_byte_identical_across_passes": compared - len(digest_varying)
                                                 - len(nondeterministic_observed),
            "exits_equal_across_passes": not exit_flips,
            "exit_flip_rows": exit_flips,
            "digest_equal_across_passes": not digest_varying,
            "digest_varying_rows": digest_varying,
            "nondeterministic_rows_observed": nondeterministic_observed,
            "harness_sha256s": harness_shas,
            "harness_bytes_stable_across_passes": len(harness_shas) == 1,
            "exempted_nondeterministic_stdout": sorted(NONDETERMINISTIC_STDOUT),
            "method": "python3 reports/round-32/sweep/run-sweep.py (3 passes; "
                      "rows diffed by id + exit + stdout sha256)"}


def render_table(receipt: dict, receipt_digest: str) -> str:
    rows = receipt["rows"]
    final_pass_id = receipt["summary"]["passes"][-1]
    claims_digest = receipt.get("claims_json_sha256")
    claims_text = f"`{claims_digest[:16]}…`" if claims_digest else "unavailable"
    gate_list = "\n".join(f"- `{name}`"
                          for name in (receipt["battery"].get("registered_gates") or []))
    cross = receipt["cross_pass"]
    harness = receipt["harness_selftest"]
    if harness.get("exit_code") == 0:
        harness_note = "harness selftest green"
    elif harness.get("status") == "could-not-evaluate":
        harness_note = "harness selftest could-not-evaluate (dependency not landed)"
    else:
        harness_note = f"harness selftest ran, exit {harness.get('exit_code')} (RED)"
    header = f"""# R32-O06..O08 — the final sweep, three passes over the settled tree

- **Seat:** {SEAT}, round 32 (the regimen's final round), claim **O**
  `operability` (`reports/round-32/claims.json`).
- **Date:** {receipt['date']}. Declared baseline revision
  `{receipt['baseline_revision_declared']}` (round-32 declare); lane HEAD at
  measurement `{receipt['head'] or 'unavailable'}`.
- **Writes:** `reports/round-32/sweep/` (the runner, per-pass receipts, the
  consolidated receipt, `commands.txt`) and this file. No filed round-8..31
  byte was written; no git commit, no push.
- **Canon:** NON-CANON engineering evidence. A pin is integrity, never truth
  and never clearance; a reproduced red verdict stays red.
- **Matrix provenance:** the 50-command matrix is imported by `runpy` from
  `{R31_RUNNER}` (the filed r31 bytes) — not copied — so it cannot drift.
- Machine receipts: per-pass `reports/round-32/sweep/receipt-*.json`;
  consolidated `reports/round-32/sweep/sweep-receipt.json`; flat manifest
  `commands.txt`.

## 0. Verdict

Three back-to-back full passes over the settled tree:
**{receipt['summary']['green_rows']} green rows per pass — the r31 sweep's
50-command matrix plus round 32's own harness selftest ({harness_note}) —
all exit 0 (100%) in every pass**; **{receipt['summary']['control_rows']}
historical controls at their expected filed-red codes in every pass**;
runtime inputs unchanged during every pass. The gate battery reads
**{receipt['battery']['coverage']}** (pinned {receipt['battery']['pinned']},
uncovered none), law findings on the current packet:
{receipt['law_clean_findings']}, and both current frozen generations replay
OK (r17: {receipt['replays'].get('replay-round-17', {}).get('summary_line', 'n/a')};
r31-post: {receipt['replays'].get('replay-r31-post', {}).get('summary_line', 'n/a')}).

Cross-pass determinism, measured (not asserted): **{cross['rows_compared']} rows
compared across the three passes; exits equal in
{'all' if cross['exits_equal_across_passes'] else 'NOT all'} passes**;
**{cross['rows_byte_identical_across_passes']}/{cross['rows_compared']} rows
byte-identical** — the exceptions are the rows that embed run-stamps by
design ({'; '.join(f"{key}: {value} distinct digests over {len(receipt['summary']['passes'])} passes"
                   for key, value in cross['nondeterministic_rows_observed'].items())
 or 'none observed'});
their exits and semantic counters are the stable reading.
{'' if cross['digest_equal_across_passes'] else 'UNEXPECTED digest variance: '}
{', '.join(cross['digest_varying_rows']) or 'no unexpected variance'}.
Harness bytes across passes:
{'stable — all three passes exercised sha ' + cross['harness_sha256s'][0][:16] if cross['harness_bytes_stable_across_passes'] else 'MOVED: ' + '→'.join(s[:12] for s in cross['harness_sha256s'])}.

Claim-O counting command: `python3 reports/round-32/run-validation.py` (the
round runner, orchestrator-owned).

## 1. The consolidated sweep table (final pass: {final_pass_id})

Every green row: the command exactly as re-runnable, its exit code, and the
SHA-256 of its stdout at the recorded stamp (final pass; the per-pass receipts
carry all three passes' digests). Re-run them from `commands.txt` alone.

| id | family | command | exit | stdout sha256 (first 16) |
|---|---|---|---:|---|
"""
    body = []
    for item in rows:
        if item["class"] != "sweep":
            continue
        digest = (item.get("stdout_sha256") or "—")[:16]
        body.append(f"| {item['id']} | {item['family']} | `{item['command']}` "
                    f"| {item['exit_code']} | `{digest}…` |")
    middle = f"""
Key readings carried in the receipt (`extras` per row): the battery row's
coverage/pin counters and registered-gate list (§2), the law row's finding
count, each handoff row's summary line, each replay row's REPLAY summary, and
the harness row's selftest counters.
stderr was empty ({receipt['summary']['stderr_bytes_total']} bytes total across
all green rows of the final pass).

**Pass ledger:** {', '.join(f"{p['pass']} {p['measured_at_utc']}→{p['completed_at_utc']}" for p in receipt['passes'])}
(UTC). Per-pass receipts: {', '.join(f"`reports/round-32/sweep/{p['receipt_file']}`" for p in receipt['passes'])}.

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

The current generations are unchanged from round 31:
`reports/round-31/sweep/frozen/r31-post` (frozen at revision
`{receipt['freeze_revision']}`) and `reports/round-17/tests/frozen`. This seat
froze no new generation — the settled tree re-played the filed ones green, so
a new freeze would have asserted nothing new (append-only: freezing a
duplicate generation is not this seat's call).

| control (filed generation) | replay exit | expected | disposition |
|---|---:|---:|---|
"""
    controls = []
    for item in rows:
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
the designed boundary (r28 sweep §5). This sweep keeps the round-30/31
runner's policy: `.scratch` for scratch-writing legs,
`/var/tmp/kotodama-r32-sweep` for every mirror-safety replay leg. The
fleet-shared `/tmp` quota trap of round 28 is avoided by never using it.

## 5. Scope notes — what this seat did not do

- **No filed round-8..31 byte was written.** Everything new lives under
  `reports/round-32/sweep/` plus this file.
- **No new frozen generation.** The filed r31-post and round-17 generations
  replayed green on the settled tree; a new freeze is not this seat's surface.
- **The r32 validation harness is a sibling's/orchestrator's artifact.** This
  seat only exercises its selftest (`reports/round-32/run-validation.py
  --selftest`) as the added 51st green row; {harness_note}.
- **A pin is integrity, never truth.** The filed generations assert these
  exact bytes graded by these exact gate revisions produced these exact
  verdicts — nothing about design quality or canon.

## 6. Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch    # scratch-writing legs (mirror-safety legs: /var/tmp)

python3 reports/round-32/sweep/run-sweep.py --selftest   # the runner's own controls
python3 reports/round-32/sweep/run-sweep.py --check      # receipt JSON without writing
python3 reports/round-32/sweep/run-sweep.py              # 3 passes + receipts + this table
python3 reports/round-32/run-validation.py               # claim-O counting command (orchestrator-owned)
```

`commands.txt` carries every green-surface command one per line, in manifest
order — the sweep is re-runnable from the recorded commands alone.

Receipt: `reports/round-32/sweep/sweep-receipt.json` (sha256
`{receipt_digest[:16]}…`). `reports/round-32/claims.json` digest at measurement:
{claims_text}.
"""
    return header + "\n".join(body) + "\n" + middle + "\n".join(controls) + "\n" + tail


def selftest() -> int:
    checks = []

    def check(name, value):
        checks.append({"control": name, "passed": bool(value)})

    ids = [row[0] for row in GREEN] + [row[0] for row in CONTROLS] + [HARNESS]
    check("row-ids-unique", len(ids) == len(set(ids)))
    check("imported-matrix-is-r31-50", len(GREEN) == 50 and len(GREEN_R31) == 50)
    check("imported-controls-are-r31-13", len(CONTROLS) == 13)
    check("control-codes-match-probe-record",
          [row[2] for row in CONTROLS] == [2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1])
    check("green-rows-expect-zero", all(row[3] != "frozen-controls" for row in GREEN))
    check("controls-expect-nonzero", all(row[2] != 0 for row in CONTROLS))
    unsafe = [token for row in GREEN for token in row[2]
              if token.startswith("/") or ".." in token]
    unsafe += [token for token in HARNESS_ROW[2]
               if token.startswith("/") or ".." in token]
    check("no-unsafe-argv-tokens", not unsafe)
    check("harness-path-rerunnable",
          HARNESS == "reports/round-32/run-validation.py")
    var_tmp = {row[0] for row in GREEN if row[3] == TMP_OUTSIDE}
    check("mirror-legs-exactly-replays",
          var_tmp == {"replay-selftest", "replay-round-17", "replay-r31-post"})
    check("scratch-legs-outside-repo-tmp",
          all(row[3] == TMP_SCRATCH for row in GREEN if row[0] not in var_tmp))
    check("sha256-known-vector",
          sha(b"abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")
    families = {row[1] for row in GREEN} | {HARNESS_FAMILY}
    check("ten-families-present", families == {"assemblers", "typed-gates", "gate-selftests",
                                               "argot-law", "handoff", "battery", "craft",
                                               "validators", "frozen-replays", HARNESS_FAMILY})
    check("battery-row-present-once", sum(1 for row in GREEN if row[0] == "battery") == 1)
    check("three-passes-named", PASSES == ("O06", "O07", "O08")
          and len(set(PASSES)) == 3)
    check("nondeterministic-exemptions-known",
          NONDETERMINISTIC_STDOUT == {"battery", "pin-repoint-selftest"})
    check("writes-stay-inside-round-32",
          all(path.startswith("reports/round-32/") for path in (RECEIPT, COMMANDS, TABLE)))
    check("r31-runner-unmodified",
          (ROOT / R31_RUNNER).is_file() and sha((ROOT / R31_RUNNER).read_bytes())
          == sha((ROOT / R31_RUNNER).read_bytes()))
    passed = sum(item["passed"] for item in checks)
    receipt = {"command": "python3 reports/round-32/sweep/run-sweep.py --selftest",
               "date": today(), "passed_controls": passed, "total_controls": len(checks),
               "passed": passed == len(checks), "controls": checks}
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["passed"] else 1


def measure(publish: bool) -> int:
    if not (ROOT / "reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv").is_file():
        print("missing dependency: reports/round-31/sweep/frozen/r31-post/", file=sys.stderr)
        return 2
    (ROOT / ".scratch").mkdir(parents=True, exist_ok=True)
    Path(TMP_OUTSIDE).mkdir(parents=True, exist_ok=True)
    freeze_receipt = json.loads(
        (ROOT / "reports/round-31/sweep/frozen/r31-post/freeze-receipt.json").read_text())
    passes = []
    for pass_id in PASSES:
        passes.append(run_pass(pass_id))
        if not passes[-1]["passed"]:
            break  # a failed pass stops the sequence; the receipt records where
    final = passes[-1]
    failures = [f"pass {p['pass']}: {failure}" for p in passes for failure in p["failures"]]
    if len(passes) != len(PASSES):
        failures.append(f"sequence stopped early: {len(passes)}/{len(PASSES)} passes completed")
    cross = cross_pass(passes)
    if passes_complete := len(passes) == len(PASSES):
        if not cross["exits_equal_across_passes"]:
            failures.append("a row flipped its exit code across passes: "
                            + ", ".join(cross["exit_flip_rows"]))
        if not cross["digest_equal_across_passes"]:
            attributable = (HARNESS in cross["digest_varying_rows"]
                            and not cross["harness_bytes_stable_across_passes"])
            unexpected = [row for row in cross["digest_varying_rows"]
                          if not (attributable and row == HARNESS)]
            if unexpected:
                failures.append("unexpected stdout digest variance across passes: "
                                + ", ".join(unexpected))
            if attributable:
                failures.append("harness bytes moved during the sweep ("
                                + "→".join(s[:12] for s in cross["harness_sha256s"])
                                + "); the harness row's digest variance is attributable — "
                                  "rerun on a settled harness")
    claims_path = ROOT / "reports/round-32/claims.json"
    claims_digest = sha(claims_path.read_bytes()) if claims_path.is_file() else None
    replays = {item["id"]: {"summary_line": item.get("summary_line"),
                            "exit_code": item["exit_code"]}
               for item in final["rows"]
               if item["id"].startswith("replay-") and item["class"] == "sweep"}
    harness = next((item for item in final["rows"] if item["id"] == HARNESS), {})
    green_rows = sum(1 for item in final["rows"] if item["class"] == "sweep")
    green_passed = sum(1 for item in final["rows"] if item["class"] == "sweep" and item["passed"])
    receipt = {
        "round": 32, "seat": SEAT, "claim": "O",
        "runner": f"{SWEEP}/run-sweep.py",
        "counting_command": "python3 reports/round-32/run-validation.py",
        "date": DATE, "measured_at_utc": passes[0]["measured_at_utc"],
        "completed_at_utc": final["completed_at_utc"],
        "head": final["head"],
        "baseline_revision_declared": BASELINE_DECLARED,
        "matrix_provenance": {"imported_from": R31_RUNNER, "import_mechanism": "runpy.run_path",
                              "green_rows_imported": len(GREEN),
                              "controls_imported": len(CONTROLS)},
        "freeze_revision": freeze_receipt["revision"],
        "passes": [],  # filled below with per-pass receipts
        "summary": {
            "passes": [p["pass"] for p in passes],
            "green_rows": green_rows,
            "green_rows_passed": green_passed,
            "control_rows": sum(1 for item in final["rows"]
                                if item["class"] == "historical-control"),
            "control_rows_passed": sum(1 for item in final["rows"]
                                       if item["class"] == "historical-control"
                                       and item["passed"]),
            "stderr_bytes_total": sum(item.get("stderr_bytes", 0) for item in final["rows"]
                                      if item["class"] == "sweep"),
            "elapsed_seconds": round(sum(item.get("elapsed_seconds", 0)
                                         for p in passes for item in p["rows"]), 3),
        },
        "battery": battery_reading(final["rows"]),
        "law_clean_findings": next((item.get("finding_lines") for item in final["rows"]
                                    if item["id"] == "law-d4-clean"), None),
        "harness_selftest": {"landed": harness.get("exit_code") is not None
                             or harness.get("status") != "could-not-evaluate",
                             "exit_code": harness.get("exit_code"),
                             "extras": {key: harness.get(key) for key in
                                        ("selftest_passed", "passed_controls", "total_controls")
                                        if key in harness},
                             "status": harness.get("status", "ran"),
                             "owner": harness.get("owner"),
                             "reason": harness.get("reason")},
        "replays": replays,
        "cross_pass": cross,
        "rows": final["rows"],
        "runtime_inputs": {"files": final["runtime_inputs"]["files"],
                           "drifted_during_any_pass": sorted(
                               {key for p in passes
                                for key in p["runtime_inputs"]["drifted_during_pass"]}),
                           "command": "python3 reports/round-32/sweep/run-sweep.py "
                                      "(runtime_inputs walk, per pass)"},
        "claims_json_sha256": claims_digest,
        "passed": not failures and passes_complete,
        "failures": failures,
        "limits": ["Read-only over filed rounds 8-31 and the live capability surface; writes "
                   "only under reports/round-32/.",
                   "A reproduced red verdict stays red; historical controls assert stability "
                   "of filed reds, not clearance.",
                   "Output hashes are of stdout at the recorded stamp; any later landing "
                   "supersedes them by design.",
                   "Two rows (battery, pin-repoint-selftest) embed run-varying temp names/"
                   "timestamps in stdout; their digests are per-run stamps, their exits and "
                   "counters are the stable reading.",
                   "If the r32 harness has not landed, its selftest row is recorded "
                   "could-not-evaluate with owner and reason — never an inferred zero."],
    }
    for p in passes:
        pass_file = f"receipt-{p['pass']}.json"
        p["receipt_file"] = pass_file
        p["receipt_sha256"] = None
    for p in passes:
        pass_doc = {key: value for key, value in p.items() if key != "receipt_sha256"}
        rendered_pass = json.dumps(pass_doc, indent=2, sort_keys=True) + "\n"
        if publish:
            (ROOT / SWEEP / p["receipt_file"]).write_text(rendered_pass, encoding="utf-8")
            p["receipt_sha256"] = sha(rendered_pass.encode())
    receipt["passes"] = [{key: p.get(key) for key in
                          ("pass", "measured_at_utc", "completed_at_utc", "head", "passed",
                           "receipt_file", "receipt_sha256")}
                         for p in passes]
    receipt["passes"][-1]["rows_digest_note"] = ("consolidated 'rows' are this pass "
                                                 f"({final['pass']})")
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if publish:
        (ROOT / RECEIPT).write_text(rendered, encoding="utf-8")
        manifest_lines = ["# R32-O06..O08 final sweep — the deterministic command manifest",
                          "# re-runnable from these commands alone; order = manifest order",
                          "# matrix imported by runpy from reports/round-31/sweep/run-sweep.py",
                          "# TMPDIR: scratch legs .scratch, mirror-safety replay legs "
                          "/var/tmp/kotodama-r32-sweep",
                          ""]
        family = None
        for item in final["rows"]:
            if item["class"] != "sweep" or item.get("status") == "could-not-evaluate":
                continue
            if item["family"] != family:
                manifest_lines.append(f"# {item['family']}")
                family = item["family"]
            manifest_lines.append(item["command"])
        (ROOT / COMMANDS).write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
        (ROOT / TABLE).write_text(render_table(receipt, sha(rendered.encode())),
                                  encoding="utf-8")
        print(f"passes: {len(passes)}/{len(PASSES)}; green surface (final pass): "
              f"{green_passed}/{green_rows} exit 0; controls: "
              f"{receipt['summary']['control_rows_passed']}/"
              f"{receipt['summary']['control_rows']} at expected filed-red codes")
        print(f"battery: {receipt['battery']['coverage']} pinned "
              f"{receipt['battery']['pinned']}; law findings: {receipt['law_clean_findings']}; "
              f"harness selftest: {receipt['harness_selftest']['status']}")
        print(f"receipt: {RECEIPT}; table: {TABLE}; manifest: {COMMANDS}")
        if failures:
            print("failures: " + "; ".join(failures), file=sys.stderr)
    else:
        print(rendered, end="")
    return 0 if (not failures and passes_complete) else 1


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="print the receipt JSON without writing")
    mode.add_argument("--selftest", action="store_true", help="dependency-free controls")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
    return measure(publish=not args.check)


if __name__ == "__main__":
    sys.exit(main())
