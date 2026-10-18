# R27-O25..O32 — D4 pin sweep (machine census)

- revision: `b95fca1e40f32f7346937ab6426f9ccca60e319f`; date 2026-10-18
- surfaces enumerated: 113; findings: 31

| family | what | surfaces | drifted |
|---|---|---:|---:|
| A | MANIFEST.tsv rows under tools/gates/frozen/** | 12 manifests / 86 rows (16 D4) | 11 |
| B/C | committed expected.json (battery roots) | 4 | 4 |
| D | freeze-receipt.json embedded pins | 3 | 3 |
| E | reports/**/expected*.json handoff baselines | 8 | 6 |
| G | expected-holds self-pins | 1 | 0 |
| H | twin.json artifact_manifest pins | 7 | 7 |
| F | tools/gates/typed-pipelines.json | 1 | 0 |
| I | reports/**/evidence/*.json embedded D4 pairs (historical) | 3 | 12 stale pins |

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
- `B/C-DIGEST-DRIFT` — `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json` (2 row(s))
- `B/C-DIGEST-DRIFT` — `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/expected.json` (2 row(s))
- `B/C-DIGEST-DRIFT` — `tools/gates/expected/d4-typed-labels-check-gate/r20-post/expected.json` (2 row(s))
- `B/C-DIGEST-DRIFT` — `tools/gates/expected/d4-typed-labels-check-gate/r22-post/expected.json` (1 row(s))
- `D-DIGEST-DRIFT` — `tools/gates/frozen/round-18/freeze-receipt.json` (2 row(s))
- `D-DIGEST-DRIFT` — `tools/gates/frozen/round-22/d4-repin/freeze-receipt.json` (8 row(s))
- `D-DIGEST-DRIFT` — `tools/gates/frozen/round-26/post-register/freeze-receipt.json` (2 row(s))
- `E-DIGEST-DRIFT` — `reports/round-20/handoff/expected.json` (7 row(s))
- `E-DIGEST-DRIFT` — `reports/round-22/handoff/declared-in/expected.json` (7 row(s))
- `E-DIGEST-DRIFT` — `reports/round-22/handoff/declared-in-r2/expected.json` (6 row(s))
- `E-DIGEST-DRIFT` — `reports/round-26/handoff/declared-in-r5/expected.json` (5 row(s))
- `E-DIGEST-DRIFT` — `reports/round-26/register/v3-baseline-r26/expected.json` (5 row(s))
- `E-DIGEST-DRIFT` — `reports/round-26/remainders/v3-baseline-r26/expected.json` (6 row(s))
- `H-DIGEST-DRIFT` — `reports/round-20/handoff/twin.json` (6 row(s))
- `H-DIGEST-DRIFT` — `reports/round-22/handoff/declared-in/twin.json` (6 row(s))
- `H-DIGEST-DRIFT` — `reports/round-22/handoff/declared-in-r2/twin.json` (6 row(s))
- `H-DIGEST-DRIFT` — `reports/round-26/handoff/declared-in-r5/twin.json` (5 row(s))
- `H-DIGEST-DRIFT` — `reports/round-26/register/v3-baseline-r26/twin.json` (5 row(s))
- `H-DIGEST-DRIFT` — `reports/round-26/remainders/r4-twin/twin.json` (6 row(s))
- `H-DIGEST-DRIFT` — `reports/round-26/remainders/v3-baseline-r26/twin.json` (6 row(s))

## Live D4 digests at this stamp

- `examples/culture-d4/packet.d4.yml` `86079a6708a0d360…`
- `examples/culture-d4/packet.d4.typed.yml` `1c4b88088b696a13…`
- `examples/culture-d4/typed-labels.d4.yml` `88a94422b4123f6b…`
- `examples/culture-d4/expected-holds.json` `857417e949fb5cb9…`
- `examples/culture-d4/components/01-brief.yml` `649aa111db2e57a7…`
- `examples/culture-d4/components/04-lexicon.yml` `d0d4e17cc3c43a11…`
- `examples/culture-d4/components/13-register-law.yml` `c0d77181ac567c4c…`
- `tools/d2-typed-labels.py` `2819f68769dfc0b5…`
