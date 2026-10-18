# R23-X05 — spot-check audit: pins table vs live shas

Date: 2026-10-18. Seat: R23-X05 (scribe/audit fragment; the parent integrates into
LOG.md). Scope: read-only audit of the sha-pinned resolution channel
(`tools/gates/typed-pipelines.json`) and its sibling live/frozen pin rows against
bytes measured in the working tree at round-23 baseline `7b181a5` (declared round-23
baseline revision `0e81d9d9…`; one uncommitted filed-artifact overlay observed, see
Finding F5). No filed round-8–22 artifact was modified by this seat; no round
validator was executed; nothing here is round acceptance or canon clearance.

Scratch discipline: `export TMPDIR=$PWD/.scratch` before every scratch-writing
command; evidence transcripts under `.scratch/x05-*` (ignored paths, lane-internal).

## Method and counts (command + date on each)

1. Pins table sweep — `python3` classify script over
   `tools/gates/typed-pipelines.json` (2026-10-18; transcript
   `.scratch/x05-table-sweep.txt`): **10** distinct 64-hex digests; **5** live
   profile pin rows; **3** `repin_history` rows; **4** historical/superseded
   digests correctly absent from live bytes.
2. Live digests — `sha256sum` of the 7 D4-family and 7 D2-family candidate files
   (2026-10-18; transcripts `.scratch/x05-live-shas-d4.txt`,
   `.scratch/x05-live-shas-d2.txt`).
3. v2-07 alias-only baseline — digest-verify script over all 28 `inputs` of
   `reports/round-22/fixes/alias-coercion-v2-07.json` (2026-10-18; transcript
   `.scratch/x05-v2-07-check.txt`).
4. d4-repin receipt — digest-verify script over all 33
   `live_tool_and_input_pins` of `reports/round-22/bleed/repin.json`
   (2026-10-18; transcript `.scratch/x05-repin-receipt-check.txt`).
5. r22-post projection baseline — digest-verify over the 4 `inputs` and
   `gate_sha256` of `tools/gates/expected/d4-typed-labels-check-gate/r22-post/expected.json`
   (2026-10-18).
6. Operational corroboration — `python3 tools/gates/typed-pipeline-gate.py
   examples/culture-d4/packet.d4.yml` (2026-10-18): **19/19 legs, exit 0**;
   `python3 tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.yml`
   (2026-10-18): **16/16 legs, exit 0**.

## Results

| Pin row (source) | Pinned | Live | Verdict |
|---|---|---|---|
| d4 packet `examples/culture-d4/packet.d4.yml` | `e7ecd204…` | `e7ecd204…` | match |
| d4 assembler `tools/assemble-culture-d4.py` | `943f487b…` | `943f487b…` | match |
| d4 projection `examples/culture-d4/typed-labels.d4.yml` | `60b526b0…` | `60b526b0…` | match |
| d4 adapter `tools/assemble-d4-typed.py` | `92f5460b…` | `92f5460b…` | match |
| d4 expected `examples/culture-d4/expected-holds.json` | `3826ba68…` | `3826ba68…` | match |
| d4 expected→projector (D4 `expected-holds.json` field) | `2819f687…` | `2819f687…` (`tools/d2-typed-labels.py`) | match |
| d4 expected `supersedes_pins` | projection `cbcf997f…`, projector `76536a92…` | — | consistent with `repin_history` (both historical) |
| D2 expected `examples/culture-d2/expected-holds.json` packet/projection | `e0f21509…` / `a3aa452c…` | same | match |
| **D2 expected `projector_sha256`** | `76536a92…` | `2819f687…` | **STALE — see F1** |
| v2-07 baseline inputs (28) | — | 27 match, 1 drift = `tools/d2-typed-labels.py` (`a10861f0…` vs live `2819f687…`) | as-declared — see F2 |
| d4-repin receipt `live_tool_and_input_pins` (33) | — | **33/33** match | match |
| r22-post `inputs` (4) + `gate_sha256` | `05f99629…` | all match | match |

`repin_history` provenance: all three rows' `recorded_in` files exist
(`reports/round-20/wart/shard-4.md`, `reports/round-22/bleed/repin.json` ×2); the
final row (2026-10-18T14:53:59Z) records the combined projector `2819f687…`.

## Findings

- **F1 — D2 live projector pin is one generation stale (confirmed, expected
  tail).** `examples/culture-d2/expected-holds.json` pins
  `projector_sha256 = 76536a924280…`; live `tools/d2-typed-labels.py` measures
  `2819f68769df…` (command: `sha256sum`, 2026-10-18,
  `.scratch/x05-live-shas-d2.txt`). The D2 gate leg does not currently enforce
  this field (16/16 exit 0 above), so the row is stale-but-latent, not a live
  failure. Disposition: exactly the round-23 O-claim premise — the O-successor-pins
  seats must land the combined-source successor as NEW rows (D2 live row + D4
  profile row); this seat does not edit the pins table. The D4 side of the same
  tail is already green (D4 `expected-holds.json` binds `2819f687…`, and
  `tools/exercise-handoff-e2e.py:2247` enforces exactly that binding).
- **F2 — v2-07 alias-only baseline drift is exactly the declared one.** 27/28
  inputs match live; the single drift is `tools/d2-typed-labels.py`
  (`a10861f0…` → live `2819f687…`), matching its own
  "alias-only baseline, live channel requires final combined-source integration"
  disposition (`reports/round-22/fixes/alias-coercion-repin.json`). No
  undocumented drift. Combined successor rows remain required (same owner as F1).
- **F3 — combined projector has no live pin row in the pins table.**
  `tools/gates/typed-pipelines.json` records `projector_sha256 = 2819f687…` only
  inside `repin_history[2]` (and prose); the d4 profile has live pin rows for
  packet/assembler/projection/adapter/expected but none for the projector.
  Disposition: same round-23 successor-row landing (F1 owner); recorded here so
  the new row's before/after digest is unambiguous
  (before `76536a92…` on the D2 live row / absent on the D4 profile row; after
  `2819f687…`).
- **F4 — all green everywhere else.** 5/5 d4 profile pins, 33/33 receipt pins,
  4/4 r22-post inputs + gate sha, D4 `expected-holds` 3/3 pins, canonical gates
  19/19 and 16/16 both exit 0 (commands+dates in Method).
- **F5 — one uncommitted overlay on a filed round-22 artifact (observed, not
  owned).** `git status` shows `M reports/round-22/fixes/regression.md`
  (+122/−54 vs `7b181a5`): the R22-O12 regression report moving from its filed
  "IN PROGRESS" state to a closing GREEN verdict. This seat did not touch it;
  flagged for the orchestrator to confirm the owning seat lands it deliberately
  (it post-dates the round-23 declared baseline `0e81d9d9…`).

## Control

Drift-detection control (2026-10-18): a scratch copy of
`examples/culture-d4/expected-holds.json` with one appended byte measures
`adb7353e68e1…` and is correctly rejected against pin `3826ba68…`
(`False`; script in transcript `.scratch/x05-tamper/…`, copy under
`.scratch/x05-tamper/`). The F1 stale-pin detection is the same checker run
against a real drifted row, so the audit method demonstrably fires on both a
synthetic and an actual mismatch.

## Limits

Byte-level digest audit only: no gate semantics were re-derived, no v2/v3 handoff
rerun, no `gate_stdout_sha256` replay for the v2-07 baseline (would require
rerunning the frozen verify), no PLACEHOLDER_RE wording check (O-wording seats
own that tail). Frozen snapshots under `tools/gates/frozen/` were sampled via the
d4-repin receipt only, not exhaustively.
