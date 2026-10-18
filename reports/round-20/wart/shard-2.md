# R20-O06 — shard 2/6: the projector's own control matrix (selftest)

- round 20, seat **R20-O05..O10**, claim **O**. Fragment 2 of 6.
- date 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- canon: NON-CANON. Every count below carries its command and date.
- writes: `tools/d2-typed-labels.py` (selftest sections 3d and 5) and this file.

## 1. Reading

| command (2026-10-18, lane root) | before (r19 revision) | after (r20 revision) |
|---|---|---|
| `python3 tools/d2-typed-labels.py --selftest` | exit 0, **39/39 checks passed** | exit 0, **50/50 checks passed** |

The 11 new legs are one control per claim, not padding: six hold the family
resolution apart (D4 resolved, D2 unchanged, skip reachable, shaping shared),
five hold the mirror-faithfulness property (shard 3).

## 2. The new legs, verbatim from the run

```
ok   family: a d4 packet resolves its own declared alias rows
ok   family: no d4 alias row or basis line resolves from the d2 tree
ok   family: the leg the d4 packet does not declare is skipped, not faked
ok   family: the d4 verdict probes are the packet's own labels
ok   family: the d2 leg is the round-8 leg, unchanged
ok   family: a packet declaring no alias rules is skipped, never aliased
ok   family: a packet-declared reconciliation row is shaped like the d2 leg
ok   mirror: the d4 mirror holds no examples/culture-d2 tree
ok   mirror: the d4 build runs with no foreign tree (exit 0/1)
ok   mirror: the mirror build is byte-identical to the filed d4 projection
ok   mirror: --check exits 0 in the mirror
```

What each one answers, so a later reader can tell a real control from a green
line:

| leg | the question it answers | the negative it rules out |
|---|---|---|
| d4 resolves its own rows | `family_alias_leg(d4 packet)` returns the four `named_eras` rows, all `confirmed` | the D2 rows reappearing in a D4 projection |
| no row or basis line resolves from the d2 tree | no row id names `12-rank-rules`; no basis line **starts with** `examples/culture-d2` | a silent fallback to the foreign source |
| the undeclared leg is skipped | `skipped == ["costume-era reconciliation"]` | a faked reconciliation leg |
| probes are the packet's own labels | `probes[-1] == "E9 no such label"`, `the league` present, `aliases["the league"] == "E2"` | D2 probe labels in a D4 projection |
| the d2 leg is the round-8 leg | row ids `12-rank-rules era_aliases.era-1..3`, probes `== D2_ERA_PROBES`, `skipped == []`, basis[0] the D2 path | a D2 regression hidden behind the new code |
| a packet with no declaration is skipped | aliases `{}`, rows `[]`, both legs in `skipped`, probes `[unmapped]` | `Malformed` where the claim requires a documented skip |
| a declared reconciliation row is shaped like the d2 leg | a synthetic `ERX-9` row comes back `to-verify` / `E1` / source `the old era` | a second, divergent shaping for packet-declared rows |

The two synthetic packets (`examples/culture-d4/probe-bare.yml`,
`probe-rows.yml`) are dicts passed straight to `family_alias_leg`; **no file is
read or written** — the selftest's closing line still says "no file outside the
temporary directory touched".

## 3. Controls that were already there and still hold

The r19 legs are unchanged and still pass: the three shard control matrices, the
loader/parser malformed cases (`P-UNTERMINATED-FLOW`, `P-DUPLICATE-KEY`,
`P-ANCHOR-TAG`, `P-TAB-INDENT`, `P-EMPTY`, `P-DEPTH-CAP`), the live-packet
typing and reconciliation cases, the CLI emit/check/tamper legs. Two of them
carry the D2 byte-identity claim from the other side:

- `cli: --emit writes the projection` + `cli: --check exit 0 on the fresh
  projection` run the D2 packet in an isolated mirror that still copies the D2
  components (the D2 leg needs them, by design);
- `cli: malformed packet exits 2 with a stable code` holds the exit-2 contract
  that the D3 refusal reading in shard 5 depends on.

## 4. Limits

- The selftest is a control matrix, not a clearance: 50/50 asserts the listed
  properties, nothing about the projection's content being sound.
- The mirror legs compare against the filed D4 projection, so they fail if that
  file is stale — deliberate (a stale filed projection is a defect), and named
  here so a later reader reads the failure correctly.
- The D3 family is not exercised by the projector at all (the loader refuses the
  D3 JSON packet before the alias leg is reached); see shard 5 §3.
