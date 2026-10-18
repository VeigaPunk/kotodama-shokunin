# R30-O11–O12 — availability-telemetry durability convention

Date: 2026-10-18. Owner: R30-O11..O12 telemetry-convention worker.
Axes: operability, reproducibility, scope safety.

## Disposition

**Convention: fixed-with-control.** `AGENTS.md` now requires availability samples and dispatch evidence in `reports/round-<N>/telemetry/`, never only `.scratch`. It requires durable raw evidence, source digests, observation boundaries, owner, counting command and date; distinguishes requested from observed counters; and requires unavailable values to remain `null` with an owner and reason. Corrections/final-wave updates are new snapshots, not rewrites. Credentials and private payloads must not be persisted. Provider liveness does not decide round acceptance.

Source of the defect: `reports/round-29/devin-availability-disposition.md:3-22`. The earlier availability summaries survived, but the wave-time raw samples did not. This fix does not recover those samples, rerun their historical windows, or turn their could-not-evaluate disposition into a pass. Filed rounds 8–29 are untouched.

**Round-30 demonstration: durable partial dispatch snapshot, not full-wave availability verification.** `reports/round-30/telemetry/dispatch-stats.json` is backed by byte-exact durable copies of this round's `claims.json` and `targets.json` under `telemetry/inputs/`, plus `telemetry/worker-observation.json`. Its source paths and SHA-256 digests bind the raw inputs; it has no scratch dependency. The worker observation is explicitly a self-observation, not an independent census.

On 2026-10-18, `python3 reports/round-30/telemetry/dispatch-telemetry.py --capture` reports **32 requested workers** (O-routed 12, C-retro 10, D-craft 10), requested `openai-codex/gpt-6.1-sol (max effort)`, and **one observed active worker session as a lower bound only**. The observation time is 2026-10-18T21:53:06Z. No launch total, completion total, failure count, actual served route, runtime concurrency, full-wave elapsed time, HTTP-attempt count or completion rate is inferred from declarations, file counts or scratch markers.

Full-wave measurement is **could-not-evaluate** at this worker's observation. Owner: round-30 orchestrator, which holds native dispatch/results. Reason: native full-wave execution/traffic receipts were not exposed in this worker's assigned inputs. The orchestrator should add a **new** final-wave snapshot and redacted native dispatch/result evidence under this telemetry directory, with its own closed boundaries, counts, command and date. Do not replace this partial observation or substitute requested workers for completed workers. This is a telemetry-measurement follow-up, not a missing durability rule.

## Controls and reproduction

Run from the lane root with `export TMPDIR="$PWD/.scratch"`. Do not redirect a new capture over a filed snapshot; the capture command prints to stdout.

```sh
python3 reports/round-30/telemetry/dispatch-telemetry.py --check
python3 reports/round-30/telemetry/dispatch-telemetry.py --selftest
cmp reports/round-30/claims.json reports/round-30/telemetry/inputs/claims.json
cmp reports/round-30/targets.json reports/round-30/telemetry/inputs/targets.json
git diff --check
```

Results on 2026-10-18:

- `--check`: exit 0, no findings; durable snapshot is reproducible while full-wave status remains could-not-evaluate. Filed evidence: `telemetry/check.json`.
- `--selftest`: exit 0, **10/10 controls**, counted by that command and dated in `telemetry/controls.json`. Positive controls validate the live snapshot and an isolated durable copy after deleting that copy's scratch directory. Negative controls reject a scratch-only evidence path, missing raw evidence, changed raw bytes, requested-as-completed count inflation, missing counting command, missing count date, unsupported full-wave pass, and missing operating rule.
- Both `cmp` commands: exit 0; durable declaration copies are byte-exact, including the originals' lack of a final newline. An initial extra-newline copy mismatch was caught and corrected before final capture; no source declaration was changed.
- Python `ast.parse` of `telemetry/dispatch-telemetry.py` and JSON parsing of the telemetry records succeeded. `git check-ignore -- <path>` returned 1 for the assigned telemetry files, so they are not excluded by `.gitignore`. `git diff --check`: exit 0.

The paired scratch-only rejection and scratch-removal replay are the closure controls for the process defect. The counter-inflation and unsupported-pass controls prevent a successful durability check from laundering unavailable execution data into a success rate. Round-wide regressions/admission and append-only `LOG.md` integration remain the parent orchestrator's responsibility.

FILES: AGENTS.md; reports/round-30/telemetry/dispatch-telemetry.py; reports/round-30/telemetry/dispatch-stats.json; reports/round-30/telemetry/worker-observation.json; reports/round-30/telemetry/inputs/claims.json; reports/round-30/telemetry/inputs/targets.json; reports/round-30/telemetry/check.json; reports/round-30/telemetry/controls.json; reports/round-30/fixes/telemetry-convention.md | SUMMARY: Lands the durable telemetry convention and a source-bound round-30 partial dispatch snapshot with 10 controls; full-wave execution counters remain explicitly unavailable to the worker.
