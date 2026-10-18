# R23-O06 — D2 live expected-holds: combined-source successor pin

Date: 2026-10-18. Seat: O06 of the round-23 combined successor pins (O05..O10). Status: landed and green.
This seat moves the D2 live `projector_sha256` pin inside
`examples/culture-d2/expected-holds.json` from the round-20 source `76536a92…`
to the final combined projector `2819f68769df…` as a NEW revision of that
append-only record. No historical pin is overwritten: the superseded value is
retained in the new `supersedes_pins` block, and the round-22 alias-only
intermediate `a10861f0…` (published by
`reports/round-22/fixes/alias-coercion-repin.json` but never landed live) is
preserved as history in the revision note, not landed as a live value.

## Before/after

| field | before (round-20 live pin) | after (round-23 combined pin) |
|---|---|---|
| file sha256 | `7b9439c4d695b50b0898605e9038dd46ba62fc05536a21ca6d806fcad69d2b51` | `9dd1a1050d93045cc8cec0020acbce620b1e3ceb46dc5b1b5b186eecd7cadf06` |
| `projector_sha256` | `76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb` | `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` |
| `packet_sha256` / `projection_sha256` | `e0f21509…` / `a3aa452c…` | unchanged (re-measured 2026-10-18T15:21:30Z) |
| `counts` / holds / notes | hold 15 / note 1 / fail 0; 15 holds + 1 note | identical, byte-for-byte rows |

Binding command (after): `sha256sum examples/culture-d2/expected-holds.json` at
2026-10-18T15:14:49Z; before-state block captured at 2026-10-18T15:13:48Z
(`HEAD=7b181a52eb74319e5e5c40cdb1f0a1a1dc652079`) before any edit.

## Controls

- Structural control (load-bearing pin): `python3 tools/gates/typed-pipeline-gate.py --selftest`
  exit 0, **12/12** — `constant == committed expected-holds.json (both directions)`
  stays true across the edit because only the pin/note fields moved and every
  hold/note row and count is unchanged (2026-10-18, after-state).
- Before control: `python3 tools/d2-typed-labels.py --check` exit 0,
  `typed-labels.d2.yml: byte-identical deterministic projection` (15:13:48Z,
  stale-pin file); after control: same command, exit 0, byte-identical
  (15:14:49Z, re-pinned file).
- Flagless D2 gate before and after: `python3 tools/gates/typed-pipeline-gate.py`
  exit 0, **16/16 legs** (15:13:48Z and 15:14:49Z).
- Combined source suite after: `python3 tools/d2-typed-labels.py --selftest`
  exit 0, **163/163**; `python3 tools/assemble-d2-typed.py --check` exit 0,
  typed packet byte-identical (2026-10-18, regression sweep below).
- Consumer safety: the gate reads only `holds`, `notes`, `counts`, `schema`
  from this file (`tools/gates/typed-pipeline-gate.py:507-527`); the file is in
  no frozen manifest, no battery baseline and no handoff v1/v2/v3 read set; the
  r22 peer-bound D4 replay's 33 live peers do not include it (verified by the
  require-live run passing after this edit, see pins/d4frozen.md).

## Successor wiring

- Frozen successor generation binding this pin:
  `tools/gates/frozen/round-23/repin-d2/MANIFEST.tsv` (pins/frozen.md).
- Before/after table across all five combined channels: pins/table.md.
- The D4 twin of this record
  (`examples/culture-d4/expected-holds.json`, `3826ba68…`) already binds the
  combined projector and is re-verified unchanged in pins/d4profile.md.

## Limits

- This is a pin movement, not a debt change: the 15 D2 holds + 1 note (garment
  forms, native forms, rank items) remain open design debt. No lore acceptance
  or canon standing is claimed.
- The alias-only `a10861f0…` row published in round 22 stays filed as the
  record of that intermediate measurement; it was never a live pin.
- Evidence transcripts: `.scratch/r23-o05/preflight/` and
  `.scratch/r23-o05/after/` (this lane's scratch; the filed record is this
  report plus the re-pinned JSON itself).
