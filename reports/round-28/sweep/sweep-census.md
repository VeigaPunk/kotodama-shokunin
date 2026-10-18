# R28-O25..O32 — D4 pin sweep (machine census)

- revision: `69cecbc7dcf575a29f29660ecac470e05260fd86`; date 2026-10-18
- surfaces enumerated: 121; findings: 39

| family | what | surfaces | drifted |
|---|---|---:|---:|
| A | MANIFEST.tsv rows under tools/gates/frozen/** | 12 manifests / 86 rows (16 D4) | 11 |
| B/C | committed expected.json (battery roots) | 4 | 4 |
| D | freeze-receipt.json embedded pins | 3 | 3 |
| E | reports/**/expected*.json handoff baselines | 11 | 9 |
| G | expected-holds self-pins | 1 | 0 |
| H | twin.json artifact_manifest pins | 8 | 8 |
| J | round-27 pinsweep rows (filed, superseded) | 4 | 4 |
| F | tools/gates/typed-pipelines.json | 1 | 0 |
| I | reports/**/evidence/*.json embedded D4 pairs (historical) | 3 | 14 stale pins |

## Replay of every frozen generation

| manifest | exit | reproduced | mismatch | could-not-evaluate |
|---|---:|---:|---:|---:|
| `reports/round-17/tests/frozen/MANIFEST.tsv` | 0 | 5 | 0 | 0 |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | 2 | 10 | 0 | 1 |
| `tools/gates/frozen/round-18/MANIFEST.tsv` | 1 | 0 | 2 | 0 |
| `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` | 2 | 10 | 0 | 1 |
| `tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv` | 2 | 10 | 0 | 1 |
| `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` | 2 | 0 | 2 | 1 |
| `tools/gates/frozen/round-23/repin-d2/MANIFEST.tsv` | 2 | 10 | 0 | 1 |
| `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` | 2 | 0 | 0 | 6 |
| `tools/gates/frozen/round-26/gate-input/MANIFEST.tsv` | 1 | 4 | 2 | 0 |
| `tools/gates/frozen/round-26/post-register/MANIFEST.tsv` | 1 | 4 | 2 | 0 |
| `tools/gates/frozen/round-3/MANIFEST.tsv` | 2 | 0 | 0 | 7 |
| `tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` | 2 | 0 | 0 | 7 |

## Findings

- `MANIFEST-INPUT-MOVED` — `tools/gates/frozen/round-18/MANIFEST.tsv:2`
- `MANIFEST-INPUT-MOVED` — `tools/gates/frozen/round-18/MANIFEST.tsv:3`
- `MANIFEST-INPUT-MOVED` — `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv:2`
- `MANIFEST-INPUT-MOVED` — `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv:3`
- `MANIFEST-INPUT-MOVED` — `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv:4`
- `MANIFEST-INPUT-MOVED` — `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv:2`
- `MANIFEST-INPUT-MOVED` — `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv:3`
- `MANIFEST-INPUT-MOVED` — `tools/gates/frozen/round-26/gate-input/MANIFEST.tsv:2`
- `MANIFEST-INPUT-MOVED` — `tools/gates/frozen/round-26/gate-input/MANIFEST.tsv:3`
- `MANIFEST-INPUT-MOVED` — `tools/gates/frozen/round-26/post-register/MANIFEST.tsv:2`
- `MANIFEST-INPUT-MOVED` — `tools/gates/frozen/round-26/post-register/MANIFEST.tsv:3`
- `B/C-DIGEST-DRIFT` — `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json` (4 row(s))
- `B/C-DIGEST-DRIFT` — `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/expected.json` (2 row(s))
- `B/C-DIGEST-DRIFT` — `tools/gates/expected/d4-typed-labels-check-gate/r20-post/expected.json` (2 row(s))
- `B/C-DIGEST-DRIFT` — `tools/gates/expected/d4-typed-labels-check-gate/r22-post/expected.json` (1 row(s))
- `D-DIGEST-DRIFT` — `tools/gates/frozen/round-18/freeze-receipt.json` (2 row(s))
- `D-DIGEST-DRIFT` — `tools/gates/frozen/round-22/d4-repin/freeze-receipt.json` (10 row(s))
- `D-DIGEST-DRIFT` — `tools/gates/frozen/round-26/post-register/freeze-receipt.json` (2 row(s))
- `E-DIGEST-DRIFT` — `reports/round-20/handoff/expected.json` (9 row(s))
- `E-DIGEST-DRIFT` — `reports/round-22/handoff/declared-in/expected.json` (9 row(s))
- `E-DIGEST-DRIFT` — `reports/round-22/handoff/declared-in-r2/expected.json` (8 row(s))
- `E-DIGEST-DRIFT` — `reports/round-26/handoff/declared-in-r5/expected.json` (7 row(s))
- `E-DIGEST-DRIFT` — `reports/round-26/register/v3-baseline-r26/expected.json` (7 row(s))
- `E-DIGEST-DRIFT` — `reports/round-26/remainders/v3-baseline-r26/expected.json` (8 row(s))
- `E-DIGEST-DRIFT` — `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/expected.json` (3 row(s))
- `E-DIGEST-DRIFT` — `reports/round-27/pinsweep/baselines/d4-typed-labels-check-gate/r27-post/expected.json` (2 row(s))
- `E-DIGEST-DRIFT` — `reports/round-27/pinsweep/v3-baseline-r27/expected.json` (6 row(s))
- `H-DIGEST-DRIFT` — `reports/round-20/handoff/twin.json` (8 row(s))
- `H-DIGEST-DRIFT` — `reports/round-22/handoff/declared-in/twin.json` (8 row(s))
- `H-DIGEST-DRIFT` — `reports/round-22/handoff/declared-in-r2/twin.json` (8 row(s))
- `H-DIGEST-DRIFT` — `reports/round-26/handoff/declared-in-r5/twin.json` (7 row(s))
- `H-DIGEST-DRIFT` — `reports/round-26/register/v3-baseline-r26/twin.json` (7 row(s))
- `H-DIGEST-DRIFT` — `reports/round-26/remainders/r4-twin/twin.json` (8 row(s))
- `H-DIGEST-DRIFT` — `reports/round-26/remainders/v3-baseline-r26/twin.json` (8 row(s))
- `H-DIGEST-DRIFT` — `reports/round-27/pinsweep/v3-baseline-r27/twin.json` (6 row(s))
- `J-DIGEST-DRIFT` — `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/expected.json` (3 row(s))
- `J-DIGEST-DRIFT` — `reports/round-27/pinsweep/baselines/d4-typed-labels-check-gate/r27-post/expected.json` (2 row(s))
- `J-DIGEST-DRIFT` — `reports/round-27/pinsweep/frozen/r27-post/freeze-receipt.json` (2 row(s))
- `J-DIGEST-DRIFT` — `reports/round-27/pinsweep/v3-baseline-r27/expected.json` (6 row(s))

## Live D4 digests at this stamp

- `examples/culture-d4/packet.d4.yml` `543d68a82640e1b0…`
- `examples/culture-d4/packet.d4.typed.yml` `15c81ec11b42efaa…`
- `examples/culture-d4/typed-labels.d4.yml` `339bfd83bf668324…`
- `examples/culture-d4/expected-holds.json` `65f5a03e092fb4bb…`
- `examples/culture-d4/components/01-brief.yml` `649aa111db2e57a7…`
- `examples/culture-d4/components/03-orthography.yml` `0f2ff45439fd7db3…`
- `examples/culture-d4/components/04-lexicon.yml` `d0d4e17cc3c43a11…`
- `examples/culture-d4/components/09-costumes.yml` `f61cc6845518d44f…`
- `examples/culture-d4/components/13-register-law.yml` `c0d77181ac567c4c…`
- `tools/d2-typed-labels.py` `2819f68769dfc0b5…`
