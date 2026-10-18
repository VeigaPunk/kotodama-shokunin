# R20-O05 — shard 1/6: per-family era-alias resolution (implementation)

- round 20, seat **R20-O05..O10** (impl + tests, one writer owns the projector),
  claim **O** (operability). Fragment 1 of 6.
- date 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
  baseline revision `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`.
- canon: NON-CANON. This fragment records the author's writes and measurements.
- writes: `tools/d2-typed-labels.py` (the projector), the D4 cascade files shard-4
  names, and `reports/round-20/wart/{shard-1..6.md,repin-r20.json}` — plus
  gitignored `.scratch/`. No filed artifact of rounds 8–19 is edited.

## 1. The wart this closes (routed in round 19)

`reports/round-19/validation.json` line 40 (quoted): "Routed: projector
era-alias leg requires the D2 alias component even for D4 packets (documented
wart)." Measured before the fix: the two functions below read
`examples/culture-d2/components/12-rank-rules.yml` (and `11-costumes.yml`)
whatever packet they were given, so a D4 run carried D2 rows in its projection
and a faithful D4 mirror had to copy the foreign tree.

| location (pre-fix) | what it did |
|---|---|
| `tools/d2-typed-labels.py:2319` `declared_era_aliases()` | `Malformed("missing examples/culture-d2/components/12-rank-rules.yml; A1 cannot be recorded")` for **every** family |
| `tools/d2-typed-labels.py:2369` `era_alias_rows()` | built `alias_rows` from the D2 components for every family |
| `tools/d2-typed-labels.py:2456-2467` (call site) | verdict probes hardcoded to D2 labels (`era-1`, `E1 shelter era`, `E4 script era`) and a basis string naming the D2 files |

Control that made the wart visible without reading code (measured 2026-10-18,
before the fix): a mirror holding the projector, the reader gate and
`examples/culture-d4/**` but **no** `examples/culture-d2` failed with exactly
`d2-typed-labels error: missing examples/culture-d2/components/12-rank-rules.yml;
A1 cannot be recorded`.

## 2. The change

One leg, resolved per packet family. The D2 path is untouched code; a non-D2
family resolves from its own packet and never from another family's tree.

| new symbol (post-fix line) | role |
|---|---|
| `packet_family()` :2412 | `examples/culture-<family>/…` → `<family>`; anything else keeps the `d2` default (the same convention `tools/gates/typed-pipeline-gate.py` `family_of` names) |
| `shown_path()` :2424 | the repo-relative path the projection reports |
| `packet_alias_rows()` :2432 | the packet's own declaration, in order: `era_aliases` (label→tag map), then `named_eras` / `era_records` (declared `name`→`tag`); `key` is None when none is declared |
| `family_alias_leg()` :2466 | the leg: aliases, rows, `two_to_one`, basis, probes, `skipped` |
| `shape_reconciliation_rows()` :2402 | the D2 costume-row shaping, factored out so a packet-declared `era_reconciliation` table is shaped by the same function (no second semantics) |

Reading rule, stated because it is the load-bearing decision: a family resolves
**only** what its own packet declares. A leg the packet does not declare is
reported in `era_reconciliation.skipped` with the measured reason and in the
`basis` lines — never satisfied from the D2 tree, never silently aliased (A1).

## 3. D2 is byte-identical (the hard constraint)

| control | command (2026-10-18) | observed |
|---|---|---|
| filed projection, checked | `python3 tools/d2-typed-labels.py --check examples/culture-d2/typed-labels.d2.yml` | exit 0, "byte-identical deterministic projection" |
| filed projection, **rebuilt** | `python3 tools/d2-typed-labels.py --emit .scratch/o05/d2-rebuild.yml && cmp .scratch/o05/d2-rebuild.yml examples/culture-d2/typed-labels.d2.yml` | cmp clean; both `sha256 a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` |
| D2 legs | `python3 tools/gates/typed-pipeline-gate.py` | exit 0, `summary: 16/16 legs passed` |
| D2 adapter | `python3 tools/assemble-d2-typed.py --selftest` | exit 0, 11/11 checks passed |

The new `skipped` key is emitted only when a leg is skipped, so the D2
projection's key set is unchanged; the D2 basis strings, row ids and probe list
are the round-8 literals (control: `--selftest` leg "family: the d2 leg is the
round-8 leg, unchanged").

## 4. What the D4 projection carries now

Field-by-field diff of the old and new D4 projection (script, 2026-10-18): the
alias leg is the **only** thing that moved — `alias_rows` 10 → 4 rows,
`two_to_one` 2 → 0, `verdicts` re-probed from the packet's own labels, the new
`skipped` list, and `rank_rules.era_aliases_applied` /
`era_aliases_basis` re-sourced. Findings and coverage are unchanged
(`fail 0, hold 15, labels 74, note 1`; `coverage` block identical).

| field | before (r19 build) | after (r20 build) |
|---|---|---|
| `era_reconciliation.alias_rows` | 10 rows: `12-rank-rules era_aliases.era-1..3` + D2 `ERX-1..4` | 4 rows: `packet named_eras.ER-01..04`, `the stamp era→E0`, `the mark hand→E1`, `the league→E2`, `the cold fire (reserved)→E3`, all `confirmed` |
| `era_reconciliation.verdicts` | `era-1`, `E1 shelter era`, `E4 script era` probes | `E0`, `E1`, `the cold fire (reserved)`, `the league`, `E9 no such label` (last = the unmapped control) |
| `era_reconciliation.basis` | the two D2 component paths | `examples/culture-d4/packet.d4.yml named_eras (A1)` + the skip line |
| `era_reconciliation.skipped` | absent | one row: `{"leg": "costume-era reconciliation", "source": "examples/culture-d4/packet.d4.yml", "why": "the packet declares no era_reconciliation rows"}` |
| `rank_rules.era_aliases_applied` | `{era-1:E0, era-2:E1, era-3:E2}` | `{the cold fire (reserved):E3, the league:E2, the mark hand:E1, the stamp era:E0}` |

## 5. Limits

- The alias leg is the only leg this seat changed. The rank-rule ledger's rule
  set is still the round-8 literal set (family-independent) — a named residual,
  not hidden: shard-6 §3.
- A D4 packet that declared no era-name records would be skipped in the open
  (aliases `{}`, probes `[unmapped]`); the live D4 packet declares four names,
  so that branch is exercised by the synthetic controls in shard-2, not by the
  live packet.
- Nothing here is a canon ruling: the tags are fixture-relative (`E0`–`E3`) and
  no date is synthesized.
