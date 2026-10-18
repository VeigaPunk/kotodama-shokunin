# R23-O07 — D2 frozen rows: new snapshot generation (combined sources)

Date: 2026-10-18. Seat: O07 of the round-23 combined successor pins. Status: landed, replay green.

## Generation

New frozen generation `tools/gates/frozen/round-23/repin-d2/` — successor of
`tools/gates/frozen/round-20/repin-d2/` (whose run-receipt carries the round-22
alias-only row `a10861f0…`) and of `tools/gates/frozen/round-18/repin-d2/`.
Every file in the directory is NEW; no historical manifest or snapshot is
touched. `freeze.txt` (frozen_at 2026-10-18T15:17:38Z) binds the combined
sources: projector `tools/d2-typed-labels.py` = `2819f68769df…`, D2 adapter
`tools/assemble-d2-typed.py` = `c7e5a749…`, re-pinned expected-holds
`9dd1a105…`, and the unchanged packet/typed-packet/projection trio.

- `MANIFEST.tsv` sha256 `8f8184665102561e5962ae65de1685f56e3af2148e649b5eb0015cc4dece9002`
- 11 rows: `typed-pipeline-gate.py` + the five D2 gates on
  `examples/culture-d2/packet.d2.typed.yml` (fresh snapshot under
  `inputs/examples/culture-d2/`), plus the same five gates on the legacy
  `examples/culture-d2/packet.d2.yml` (outputs under `legacy/`).
- Command: 11 measured gate runs at 2026-10-18 (immediately before the
  15:17:38Z freeze note), each recorded with gate/input/output SHA-256, exit
  code and `^FINDING` census in the manifest.

## Recorded verdicts (all newly measured 2026-10-18)

| gate | packet | exit | findings |
|---|---|---|---|
| typed-pipeline-gate.py | packet.d2.typed.yml | 0 | 15 |
| naming-collision-gate.py | packet.d2.typed.yml | 1 | 7 |
| phonology-sanity-gate.py | packet.d2.typed.yml | 1 | 3 |
| costume-era-consistency-gate.py | packet.d2.typed.yml | 0 | 0 |
| lexicon-coverage-audit.py | packet.d2.typed.yml | 0 | 0 |
| myth-consistency-gate.py | packet.d2.typed.yml | 0 | 0 |
| naming-collision-gate.py | packet.d2.yml (legacy) | 1 | 17 |
| phonology-sanity-gate.py | packet.d2.yml (legacy) | 1 | 3 |
| costume-era-consistency-gate.py | packet.d2.yml (legacy) | 0 | 0 |
| lexicon-coverage-audit.py | packet.d2.yml (legacy) | 0 | 0 |
| myth-consistency-gate.py | packet.d2.yml (legacy) | 0 | 0 |

The verdict pattern is byte-consistent with the round-11/18/20 predecessors:
the nonzero rows are the recorded open design holds, not failures of this
landing. Reproduction, not cleanliness, is what a frozen row asserts.

## Replays (command + date, all 2026-10-18)

- After: `python3 tools/replay-frozen.py tools/gates/frozen/round-23/repin-d2/MANIFEST.tsv --json`
  — exit 0, `{"rows": 11, "reproduced": 11, "mismatch": 0, "could_not_evaluate": 0, "exit": 0}`.
- Before controls: same command on `tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv`
  and `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` — exit 0, 11/11
  reproduced each.
- Replay environment note: the replay tool refuses an in-repository temporary
  root (`mirror_unsafe`); mirrors run from the lane-sibling scratch root
  (`TMPDIR=/home/vgpnk/Projects/shokunin/.scratch/r23-replay-mirrors`), the
  same outside-the-clone arrangement filed in round 22. First replay attempt
  with `TMPDIR=$PWD/.scratch` was refused before any gate launched and is
  preserved as the negative control for this note.

## Limits

- The generic TSV replay binds gate, primary input snapshot and output bytes;
  the peer sources above are bound by `freeze.txt` digests and the live-gate
  regression sweep, not by the TSV alone.
- This generation is a reproduction record of the current D2 verdicts; it
  resolves no hold and claims no round admission.
