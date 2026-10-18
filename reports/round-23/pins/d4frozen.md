# R23-O10 — D4 frozen rows: replay green against the combined sources

Date: 2026-10-18. Seat: O10 of the round-23 combined successor pins. Status: green, rows only (no new manifest needed).

The round-22 D4 frozen generation
`tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` (3 rows: projection check,
assembly check, full typed-pipeline) is the current D4 frozen successor and
already binds the final combined projector via its input snapshots and the
`freeze.txt`/receipt source pins. This seat lands the round-23 frozen rows as
dated replay evidence that the generation still reproduces against the live
combined sources, including the peer-bound replay that checks all 33 live
peers — the strongest available witness that the round-22 D4 pins and the
round-23 combined D2 landing coexist green.

## Replays (command + date, all 2026-10-18)

- Generic: `python3 tools/replay-frozen.py tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv --json`
  — exit 0, `{"rows": 3, "reproduced": 3, "mismatch": 0, "could_not_evaluate": 0, "exit": 0}`.
- Peer-bound: `python3 reports/round-22/bleed/replay.py --require-live` at
  **2026-10-18T15:19:16Z** — exit 0; receipt:
  `peer_snapshot_pairs_checked: 33`, `live_peers_checked: True`,
  execution context "isolated Git clone with all pinned D4 peers restored from
  the new snapshot", replay summary 3/3 reproduced, 0 mismatch, 0
  could-not-evaluate. This run also proves the peer set — including
  `tools/gates/typed-pipelines.json` `396f4678…` and
  `examples/culture-d4/expected-holds.json` `3826ba68…` — is unchanged after
  the round-23 D2 landing, and that the round-23 edit to
  `examples/culture-d2/expected-holds.json` (not a pinned peer) breaks nothing.

## Supporting gate legs (2026-10-18T15:17:49Z)

- `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`
  — exit 0, 19/19 legs.
- `python3 tools/gates/d4-typed-labels-check-gate.py` — exit 0, projection
  byte-identical (`examples/culture-d4/typed-labels.d4.yml` = `60b526b0…`).
- `python3 tools/assemble-d4-typed.py --check` — exit 0, typed packet
  byte-identical.
- `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml`
  — exit 0, assembly byte-identical.
- `python3 tools/assemble-d4-typed.py --selftest` — exit 0, **12/12**;
  `python3 tools/gates/d4-typed-labels-check-gate.py --selftest` — exit 0,
  **163/163** (delegates to the projector suite).

## Why no new D4 manifest

A second D4 snapshot of identical bytes would add a duplicate generation
without binding anything new: the r22 manifest's gate, inputs and outputs are
byte-identical to what a fresh snapshot would pin (verified by the two replays
above plus the byte-identity legs). The round-23 D2 generation
(`tools/gates/frozen/round-23/repin-d2/`, pins/frozen.md) is the genuinely new
frozen work; the D4 rows here are its peer-side witness. If any D4 byte moves
later, the successor is a NEW snapshot directory plus a re-pinned profile row,
per the round-22 recipe.

## Limits

- Reproduction is not design cleanliness: the twelve legitimate garment/slot
  form holds stay open inside the recorded 12-finding typed-pipeline verdict.
- No frozen artifact, receipt or profile file was edited by this seat.
