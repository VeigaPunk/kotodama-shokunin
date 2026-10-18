# R23-O05 — combined-source successor pins: before/after digest table

Date: 2026-10-18. Seat: O05, index table for the round-23 combined successor
pins (O05..O10). Baseline: `HEAD=7b181a52eb74319e5e5c40cdb1f0a1a1dc652079`,
declared round-23 baseline revision
`0e81d9d99514631d6717e1ff354d5a5a759aa980`. This table extends the round-22
before/after discipline (`reports/round-22/fixes/alias-coercion-repin.json`)
to the final combined sources. Every row is a NEW row; no historical pin is
overwritten.

## Projector source chain (the "combined" lineage)

| generation | tools/d2-typed-labels.py sha256 | where recorded |
|---|---|---|
| pre-round-20 | `0da0015f…` | `examples/culture-d2/expected-holds.json` round-20 revision note (superseded) |
| round-20 per-family alias leg | `76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb` | was the live D2 `projector_sha256` pin until this round |
| round-22 alias-only intermediate | `a10861f039f7e80a2f38a11fe1d72d4ef6fa5f48987f5fff96185b1875924a7b` | `reports/round-22/fixes/alias-coercion-repin.json` rows (published, never landed live; preserved as history) |
| **round-22 final combined (live now)** | **`2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3`** | `sha256sum tools/d2-typed-labels.py` 2026-10-18T15:13:48Z / 15:21:30Z; D4 expected field; r22 d4-repin receipt |

The D2 adapter `tools/assemble-d2-typed.py` =
`c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071` (unchanged
since round 11; re-measured 2026-10-18T15:13:48Z).

## Before/after digest table (this round's landings)

| # | channel / row | before (r22 state) | after (r23 landing) | command + date | control |
|---|---|---|---|---|---|
| 1 | D2 live expected-holds `examples/culture-d2/expected-holds.json` | file `7b9439c4d695b50b…`, `projector_sha256` `76536a92…` | file `9dd1a1050d93045cc…`, `projector_sha256` `2819f68769df…`, supersedes block added; counts/holds byte-unchanged | `sha256sum` before 15:13:48Z / after 15:14:49Z | gate selftest 12/12 constant==committed; `--check` byte-identical before+after; 16/16 before+after (pins/r2-live.md) |
| 2 | D2 frozen generation | latest D2 frozen rows = r20 `repin-d2` (tool_pins row `a10861f0…`, r22) | NEW `tools/gates/frozen/round-23/repin-d2/` (MANIFEST `8f8184665102561e…`, 11 rows, freeze.txt 15:17:38Z) | replay `--json` 2026-10-18: 11/11 reproduced exit 0 | r18 + r20 manifests 11/11 each; first in-repo-TMPDIR replay refused `mirror_unsafe` (pins/frozen.md) |
| 3 | v2 handoff baseline row | r22 alias-era capture `reports/round-22/fixes/alias-coercion-v2-07.json` (projector `a10861f0…`) | fresh dated v2 run 15:21:30Z exit 0 over live projector `2819f68769df…`; round-15 baseline + both captures untouched | `python3 tools/exercise-handoff-e2e.py --profile v2` 2026-10-18T15:21:30Z | 50/50 links, 16/16 fields, 2 named drift rows; v3 105/105 same stamp (pins/v2.md) |
| 4 | D4 profile row `tools/gates/typed-pipelines.json` | round-22 re-pin (14:53:59Z), expected `3826ba68…` | unchanged by design — all seven pin targets re-measured equal 15:21:01Z; row filed here, file not edited (r22 require-live pins its digest `396f4678…`) | `sha256sum` + field read 2026-10-18T15:21:01Z | d4 gate 19/19 incl. L1-profile; require-live 33 peers True (pins/d4profile.md) |
| 5 | D4 frozen rows | r22 `d4-repin` manifest (3 rows) | replay green re-witnessed: 3/3 generic + peer-bound 33 peers + 3/3 nested-clone 15:19:16Z; no new manifest (bytes identical) | both replay commands 2026-10-18 | d4 check/adapter/assembly byte-identical ×3 (pins/d4frozen.md) |

## Regression sweep after the landing (all exit 0, 2026-10-18)

`python3` invocations from the lane root: check-gate-battery `--selftest`
35/35 and plain (**19/19 baselines pinned, 0 unevaluable, 0 fail**, re-run
15:23:41Z post-landing); craft `--selftest` 18/18 CLI cases + production run
(audits 7, mech 11, derivations 9, runner checks 37); assemble-d2 42/42;
assemble-d2-typed `--selftest` 11/11 and `--check` byte-identical;
assemble-culture-d3 85/85; assemble-culture-d4 81/81; d2-typed-labels
`--selftest` 163/163 and `--check` byte-identical; typed-pipeline-gate
`--selftest` 12/12 and `--selftest-generalized` 14/14; d4-typed-labels
check-gate `--selftest` 163/163 and live byte-identical; d4 assembly gate
byte-identical; assemble-d4-typed `--selftest` 12/12; evidence-coupling
`--selftest` + d3 packet clean; replay-frozen `--selftest` 79/79; handoff v2
exit 0; handoff v3 exit 0 (105/105) and `--selftest` exit 0; packet_links 38;
packet_uncertainty 19. Full tails: `.scratch/r23-o05/after/regressions.txt`.

## Limits

- Pins are reproducibility rows, not debt resolutions: 15 D2 holds + 1 note and
  the 12 D4 garment/slot holds all remain open; no lore acceptance or canon
  standing is claimed anywhere in this landing.
- The wording-false-positive tail (PLACEHOLDER_RE / D4-CL08) belongs to the
  O-wording seats, not this table.
- `reports/round-22/fixes/regression.md` carries a pre-existing uncommitted
  working-tree edit relative to the declared baseline; this seat did not touch
  it and flags it for the parent integrator.
- Scratch transcripts live under `.scratch/r23-o05/` (lane scratch, TMPDIR
  exported before every scratch-writing command); the filed record is this
  table plus the five seat reports named above.
