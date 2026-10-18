# R23-O09 — D4 profile row: combined-source re-verification (rows only)

Date: 2026-10-18. Seat: O09 of the round-23 combined successor pins. Status: verified green; no file edited.

The d4 profile row in `tools/gates/typed-pipelines.json` already binds the
final combined sources (round-22 re-pin, `repin` block round 22 at
2026-10-18T14:53:59Z; `expected` field `3826ba68…` whose
`projector_sha256` content is the combined projector). No D4 digest moved in
round 23, so per the file's own rule ("editing this file cannot silently
re-point a run — a stale pin refuses until it is re-pinned with a command and a
date") there is nothing to re-pin. This seat lands the round-23 successor row
as dated re-verification evidence instead, and deliberately does NOT edit the
file: the r22 peer-bound D4 replay pins `tools/gates/typed-pipelines.json` =
`396f4678…` as one of its 33 live peers, so any edit would break the filed
`reports/round-22/bleed/replay.py --require-live` replay (which passes — see
pins/d4frozen.md).

## Pin re-measurement (command + date)

`sha256sum` at **2026-10-18T15:21:01Z**, every value equal to its pinned
digest in the d4 profile row:

| profile field | path | live sha256 (= pin) |
|---|---|---|
| packet | `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` |
| assembler | `tools/assemble-culture-d4.py` | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` |
| projection | `examples/culture-d4/typed-labels.d4.yml` | `60b526b0b3d07141875d20c472451cdf6658f61936d39fe18af4f3d981981092` |
| adapter | `tools/assemble-d4-typed.py` | `92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0` |
| expected | `examples/culture-d4/expected-holds.json` | `3826ba68d705b3c379b2a12737c14075d9095a1ba2aa2eb525de1851a9ecd2f7` |
| (combined pair) | `tools/d2-typed-labels.py` | `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` |
| (profile file) | `tools/gates/typed-pipelines.json` | `396f4678133ad3223752c27d7153fdff06945abfa49137a307e10ef6e29b44d0` |

Field read at the same stamp: `examples/culture-d4/expected-holds.json`
`projector_sha256` = `2819f68769df…` — the expected file's embedded source pin
equals the final combined projector.

## Gate legs through the profile (2026-10-18T15:17:49Z)

- `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`
  — exit 0, **19/19 legs** (includes the `L1-profile` leg: every pinned profile
  digest re-verified against live bytes in-run).
- `python3 tools/gates/d4-typed-labels-check-gate.py` — exit 0, projection
  byte-identical.
- `python3 tools/assemble-d4-typed.py --check` — exit 0, typed packet
  byte-identical.
- `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml`
  — exit 0, assembly byte-identical.
- `python3 tools/gates/typed-pipeline-gate.py --selftest-generalized` — exit 0,
  **14/14** (stale-pin and missing-expected controls among them).

## Limits

- Rows only: no shared channel file was edited by this seat; the D4 side of
  the combined-source landing stays exactly as round 22 filed it.
- The twelve legitimate garment/slot form holds remain open; no lore
  acceptance or canon standing is claimed.
