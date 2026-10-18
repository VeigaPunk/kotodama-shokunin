# R22-O12 — regression sweep

**Status: IN PROGRESS — integration dependencies are still landing.** This is a regression measurement, not round acceptance or canon clearance. The only filed write of this seat is this report; all execution and captures are under `.scratch/r22-o12-regression/`.

## Isolation and commands

- Observation date: **2026-10-18**; timestamps below use UTC−03:00.
- Before scratch commands: `export TMPDIR=$PWD/.scratch; export PYTHONDONTWRITEBYTECODE=1` from the lane root.
- Driver: `python3 .scratch/r22-o12-regression/sweep.py initial` at **2026-10-18T11:40:55−03:00**. The driver creates a real scratch Git clone, overlays the measured working-tree bytes, and copies manifest-referenced ignored receipts before replay. All checks run inside the clone. Replay temporary roots are siblings of the clone, still inside the lane, avoiding the replay tool's in-repository-mirror refusal.
- Initial snapshot: `HEAD=cd9c8e4cb62896a8b5d0d642cd04966d41dd4d13`; working-tree readings, not a claim that HEAD contains the pending fixes. Snapshot manifest and source status: `.scratch/r22-o12-regression/initial/{source-manifest,snapshot}.json`.
- Evidence: `.scratch/r22-o12-regression/initial/results.json` and per-command `*.stdout.txt` / `*.stderr.txt`. Each result records its exact command, dated start/end, exit, and stream digests.

## Initial control sweep — not the integrated verdict

Commands started **2026-10-18T11:40:56–11:40:57−03:00**. Counts below are measured by the stated commands, not copied acceptance claims.

| Command | Initial result |
|---|---|
| `python3 tools/check-gate-battery.py` | exit 0; seven structural selftests pass; nine-gate baseline coverage; originals preserved |
| `python3 tools/check-gate-battery.py --selftest` | exit 0; 35/35 positive/negative controls |
| `python3 tools/check-craft-exercise.py --selftest` | exit 0; 10/10 tamper + 18/18 CLI cases |
| `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json --report reports/supplement-opencode-1/32-craft-exercise.md` | exit 0; all checks pass |
| `python3 tools/assemble-d2.py --selftest` | exit 0; 42/42 |
| `python3 tools/assemble-d2-typed.py --selftest` | exit 0; 11/11 |
| `python3 tools/assemble-culture-d3.py --selftest` | exit 0; 85/85 |
| `python3 tools/assemble-culture-d4.py --selftest` | exit 0; 81/81 |
| `python3 tools/d2-typed-labels.py --selftest` | exit 0; 50/50 |
| `python3 tools/gates/typed-pipeline-gate.py --selftest` | exit 0; 12/12 |
| `python3 tools/gates/typed-pipeline-gate.py --selftest-generalized` | exit 0; 14/14 |
| `python3 tools/gates/d4-typed-labels-check-gate.py --selftest` | exit 0; 50/50 |
| `python3 tools/assemble-d4-typed.py --selftest` | exit 0; 12/12 |
| `python3 tools/gates/typed-pipeline-gate.py` | exit 0; D2 16/16 |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit 0; D4 19/19 |
| `python3 tools/exercise-handoff-e2e.py --profile v2` | exit 0; claims 15; links 50/50 |
| `python3 tools/exercise-handoff-e2e.py --profile v3` | exit 1; `E2E-DIGEST`: recorded projector pin `76536a924280…` does not match measured `51bff2848d19…` |
| `python3 tools/exercise-handoff-e2e.py --profile v3 --selftest` | exit 1; same stale projector pin while the integration cascade is in flight |
| `python3 tools/replay-frozen.py --selftest` | exit 0; 79/79 controls |

The associated production assembly/projector checks all exit 0 in the initial capture. `d4-assembly-check-gate.py` has no selftest mode; its real packet check exits 0 instead. Evidence-coupling and both packet-harness selftests also exit 0.

## Initial frozen-replay controls

All commands below are `python3 tools/replay-frozen.py <manifest> --json`, started **2026-10-18T11:40:57−03:00**. These originals are historical controls, not silently re-pinned current rows.

| Manifest | Initial observed result |
|---|---|
| `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` | exit 0; 11/11 reproduced |
| `tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv` | exit 0; 11/11 reproduced |
| `tools/gates/frozen/round-18/MANIFEST.tsv` | exit 1; 1/2 reproduced; superseded D4 projection row 2 is `replay_mismatch` |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | exit 2; 10/11 reproduced; old typed-pipeline row 2 refuses `gate_digest_mismatch` |
| `tools/gates/frozen/round-3/MANIFEST.tsv` | exit 2; 0/7 reproduced; seven old gate digest pins refuse before launch |
| `tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` | exit 2; 0/7 reproduced; seven old gate digest pins refuse before launch |

## Preservation and remaining work

The initial driver compared every copied path after execution: **zero clone input changes**. It compared **1,156** locked report/frozen paths against their initial source hashes: **zero changed** (command/date: initial driver above). Projector and handoff-runner source bytes moved in the live lane during execution, so the first snapshot cannot certify the finished integration.

The second full sweep, `python3 .scratch/r22-o12-regression/sweep.py integrated-candidate`, began **2026-10-18T11:50:54−03:00**; commands ran **11:50:55–11:51:32−03:00**. All typed/assembly selftests pass, now **163/163** for the projector and D4 projection-gate entrypoint. The v3 selftest also passes its positive run plus **39** controls. The D4 production gate correctly refuses the intermediate profile pin (`88c21ff3cd31…` versus final expected-holds bytes `3826ba68d705…`, exit 2 / `L1-profile`); production v3 correctly reports two baseline input changes (the final projector and expected holds, exit 1 / `E2E-DIGEST`). New D4 frozen rows were not yet present at this snapshot. This is a measured re-pin dependency, not a waived regression. Captures: `.scratch/r22-o12-regression/integrated-candidate/`; zero copied clone-input changes and zero locked-path changes.

### Additional semantic dependency, observed 2026-10-18T11:53:37−03:00

The re-pin owner's `reports/round-22/bleed/repin.md:26-37` records that the new handoff packet still copies historical D4 claim text. This seat independently rechecked the delivered packet with the exact content-search pattern `D4-CL05|D4-CL06|D4-CL07|D4-CL09|OQ-V3-05` on **2026-10-18 at 11:53−03:00**:

- `reports/round-22/handoff/declared-in/packet.md:148-152` still states 16 findings / 15 holds / one note, four conflicts and three quarantine handles, and thirteen inherited unresolved rank items.
- Its `OQ-V3-05` at line 307 still says those inherited findings remain D4-owned. The corrected D4 expected holds instead declare twelve form holds, zero notes and zero fails.
- A new superseding claim map plus packet/baseline is required from the assigned handoff/integration owner; do not edit the historical round-20 claim map. Structural link equality does not make stale numeric/ownership wording true. This seat does not race the renderer writer or re-pin owner.

Pending: the 60-second dependency watcher waits for the final re-pin and new frozen-generation cascade, with a bounded wait of at most 20 minutes from the first sweep. Take a fresh isolated snapshot after they land, rerun the complete matrix and current re-pins, and record an honest final verdict here. No round validator has run in the live lane; no filed round-8–21 artifact was changed by this seat; no commit or push.
