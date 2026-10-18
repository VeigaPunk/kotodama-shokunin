# Round 21 — Regression runner evidence (O19–O20)

- **Assignment:** operability regression runners: battery, craft, typed/assembly selftests, frozen replays.
- **Observation date:** 2026-10-18, local time UTC−03:00. Commands ran from **10:50:15 through 10:50:50**; each row below carries its command and start stamp.
- **Revision:** `8115eaaeb57c9dce157fe291337cb52dd914c6cf`, read with `git rev-parse HEAD` at 2026-10-18 10:49:39−03:00. The source worktree was clean at that point.
- **Isolation:** `TMPDIR=$PWD/.scratch` was exported from the lane root. Tests ran from a scratch `git archive HEAD` tree at `.scratch/r21-o19-ops/repo`; command outputs were saved under `.scratch/r21-o19-ops/results/`. Frozen-replay runs used the lane’s `.scratch` as the temporary root, outside the scratch repository but still inside this lane. Because `git archive` omits ignored `*.log` files, the existing round-11 and re-pin `run.log` receipts were copied into the scratch tree before the final replay runs. No replay result below relies on the incomplete archive-only attempt.
- **Write boundary:** this report is the only filed output of this seat. No round-8–20 artifact was edited; `git diff --quiet -- reports/round-8 reports/round-9 reports/round-10 reports/round-11 reports/round-12 reports/round-13 reports/round-14 reports/round-15 reports/round-16 reports/round-17 reports/round-18 reports/round-19 reports/round-20 tools/gates/frozen` returned exit 0 at 2026-10-18 10:53:01−03:00. No commit or push.

## Verdict

Battery, craft, every runnable typed/assembly selftest, the associated production checks, and `replay-frozen.py --selftest` are green on the measured tree. The two specifically requested original historical replay manifests are **not both exit-0**: round-18 still has its previously identified superseded D4 projection mismatch, and round-11 still refuses its superseded typed-pipeline digest. The latter is the documented expected result; the former remains an open re-pin/supersession note for the loop-2 defect queue. The append-only round-18 and round-20 D2 re-pin manifests both replay cleanly.

## Battery and craft

| Command | Result (command started at 2026-10-18, UTC−03:00) |
|---|---|
| `python3 tools/check-gate-battery.py` | **Exit 0** at 10:50:15: `battery_exit=0`, `pass=7`, `fail=0`, `unevaluable=0`; baseline coverage `9/9`, all `18` baselines pinned; originals preserved (`30` files hashed before and after, `0` modified/added/deleted). |
| `python3 tools/check-gate-battery.py --selftest` | **Exit 0** at 10:50:15: `SELFTEST OK 35/35`. |
| `python3 tools/check-craft-exercise.py --selftest` | **Exit 0** at 10:50:15: `10/10` tamper cases and `18/18` CLI cases. |

## Typed / assembly selftests

All runnable typed/assembly selftest entry points were exercised. `d4-assembly-check-gate.py` has no `--selftest` mode (its CLI is `[PACKET]`; see `tools/gates/d4-assembly-check-gate.py:38-43`), so its normal packet check is recorded in the following section instead.

| Command | Result (command started at 2026-10-18, UTC−03:00) |
|---|---|
| `python3 tools/gates/typed-pipeline-gate.py --selftest` | **Exit 0** at 10:50:15: `12/12` checks. |
| `python3 tools/gates/typed-pipeline-gate.py --selftest-generalized` | **Exit 0** at 10:50:15: `14/14` checks. |
| `python3 tools/gates/d4-typed-labels-check-gate.py --selftest` | **Exit 0** at 10:50:15: `50/50` checks. |
| `python3 tools/d2-typed-labels.py --selftest` | **Exit 0** at 10:50:15: `50/50` checks. |
| `python3 tools/assemble-d2-typed.py --selftest` | **Exit 0** at 10:50:15: `11/11` checks. |
| `python3 tools/assemble-d2.py --selftest` | **Exit 0** at 10:50:15: `42/42` checks. |
| `python3 tools/assemble-culture-d3.py --selftest` | **Exit 0** at 10:50:15: `85/85` checks. |
| `python3 tools/assemble-culture-d4.py --selftest` | **Exit 0** at 10:50:15: `81/81` checks. |
| `python3 tools/assemble-d4-typed.py --selftest` | **Exit 0** at 10:50:16: `12/12` checks. This reproduces the round-20 repair of the earlier selftest failure. |

## Typed / assembly production checks

| Command | Result (command started at 2026-10-18, UTC−03:00) |
|---|---|
| `python3 tools/gates/typed-pipeline-gate.py` | **Exit 0** at 10:50:15: `16/16` legs passed (D2). |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | **Exit 0** at 10:50:15: `19/19` legs passed (D4). |
| `python3 tools/gates/d4-typed-labels-check-gate.py` | **Exit 0** at 10:50:15: committed projection byte-identical. |
| `python3 tools/d2-typed-labels.py --check` | **Exit 0** at 10:50:15: D2 projection byte-identical. |
| `python3 tools/assemble-d2-typed.py --check` | **Exit 0** at 10:50:15: D2 typed packet byte-identical. |
| `python3 tools/assemble-d2.py --check` | **Exit 0** at 10:50:15: D2 assembly byte-identical. |
| `python3 tools/assemble-culture-d3.py --check` | **Exit 0** at 10:50:15: `packet.json` and `packet.gates.yml` byte-identical. |
| `python3 tools/assemble-culture-d4.py --check` | **Exit 0** at 10:50:15: D4 assembly byte-identical. |
| `python3 tools/assemble-d4-typed.py --check` | **Exit 0** at 10:50:16: D4 typed packet byte-identical. |
| `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | **Exit 0** at 10:50:16: D4 assembly byte-identical. |

## Frozen replay measurements

The replay runner’s own guard/control suite also passed: `python3 tools/replay-frozen.py --selftest` → **exit 0, 79/79 checks**, started 2026-10-18 10:50:16−03:00.

| Replay command | Result (command started at 2026-10-18, UTC−03:00) |
|---|---|
| `python3 tools/replay-frozen.py tools/gates/frozen/round-18/MANIFEST.tsv --json` | **Exit 1** at 10:50:16: `1` of `2` rows reproduced; row 2 (`d4-typed-labels-check-gate.py`) is `replay_mismatch` (recorded exit `0`, observed exit `1`); row 3 (`d4-assembly-check-gate.py`) reproduced. The recorded projection is `a59990bb…`; current `examples/culture-d4/typed-labels.d4.yml` is `cbcf997f…` (`sha256sum` at 10:51:32−03:00). This is the already documented round-20 supersession, not an unexplained runner discrepancy; it still needs a new append-only frozen row or an explicit supersession treatment. No old manifest was changed. |
| `python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv --json` | **Exit 2** at 10:50:50: `10` of `11` rows reproduced; row 2 is `could-not-evaluate / gate_digest_mismatch` for the old typed-pipeline pin `d102fd1d…`. Current gate digest is `04ad4bb4…` (`sha256sum` at 10:51:32−03:00). This is the previously documented, expected round-11 supersession; the filed round-11 bytes remain untouched. |
| `python3 tools/replay-frozen.py tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv --json` | **Exit 0** at 10:50:50: `11/11` rows reproduced. |
| `python3 tools/replay-frozen.py tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv --json` | **Exit 0** at 10:50:50: `11/11` rows reproduced. |

The first archive-only round-11 replay at 10:50:16 was discarded: it could not find the ignored `run.log` because `git archive` does not include ignored files. The final round-11 measurement above ran after that existing receipt was copied into the scratch tree; it reproduced the expected `gate_digest_mismatch`, not `output_missing`.

## Findings and routing

- **R21-O-REG-1 — round-18 original D4 replay remains superseded (still nonzero).** Evidence: the command and 10:50:16 measurement above; manifest digest `3688e8bc…` and projection digests were read by `sha256sum` at 10:51:32−03:00. This was already identified in `reports/round-20/regression.md` §4 as F-O15-1. The loop-2 regression sweep confirms it remains present. Do not edit the round-18 manifest; route an append-only re-pin or explicit supersession note to the round-22 owner.
- **Round-11 replay refusal is expected, not a new defect.** Evidence: command and 10:50:50 measurement above; the append-only re-pin controls at the round-18 and round-20 paths both exit 0 with `11/11` rows. This preserves the documented round-11 supersession instead of silently rewriting its frozen row.
- All typed/assembly selftests and production checks in this report exited 0. No new battery or craft regression was observed.

## Reproduction and preservation

Every command above was run against the scratch tree derived from revision `8115eaa…`, with `TMPDIR` rooted at this lane’s `.scratch`; replay mirror tempdirs remained outside the scratch repository root. Result captures and replay outputs are under `.scratch/r21-o19-ops/`. The filed rounds 8–20 and frozen manifests were not edited, and no commit or push was made.
