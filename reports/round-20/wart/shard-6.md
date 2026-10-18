# R20-O10 — shard 6/6: the wart erratum closed, and the residuals named

- round 20, seat **R20-O05..O10**, claim **O**. Fragment 6 of 6.
- date 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
  baseline revision `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`.
- canon: NON-CANON. Nothing here is a clearance; the residuals below are the
  honest bound of this seat's work.
- writes: this fragment (plus the artifacts shards 1–5 name).

## 1. The erratum, closed

Round 19 routed one wart (`reports/round-19/validation.json` line 40, quoted):
"projector era-alias leg requires the D2 alias component even for D4 packets
(documented wart)". Round 20 closes it, with the closure measured by the round's
own counting command (`python3 reports/round-20/run-validation.py` → `claim O:
PASS`) rather than asserted:

| what the erratum said | the r20 reading | evidence |
|---|---|---|
| the alias component is required for a D4 packet | a D4 run reads **no** `examples/culture-d2` byte; the component is resolved per packet family | shard 3 §2 (before 6 reads → after 4, both reproducible) |
| a faithful D4 mirror must copy the D2 tree | two independent mirrors hold no `examples/culture-d2` and are green: the projector's selftest mirror and the runner's `wart_mirror` | shard 3 §3; `wart_mirror.culture_d2_present false`, both mirror checks exit 0 |
| the adapter's selftest mirror must copy it too | `tools/assemble-d4-typed.py` no longer copies it; its selftest still reads 12/12 | runner field `foreign_tree_copy_in_adapter: false`; shard 5 row 8 |
| the D4 projection carried D2 alias rows | it now carries the four `named_eras` rows the D4 packet declares; the legs it does not declare are `skipped` in the open | shard 1 §4 |
| (the run was green despite the wart) | still green, and the D2 path is byte-identical | shard 5 rows 1, 2, 5, 6, 14; runner field `d2_byte_identical: true` |

The D2 path is the control that the fix did not become a D2 regression: a fresh
build of the D2 projection compares clean against the filed bytes
(`a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`).

## 2. Residuals — named, not hidden

**R1 — the filed v2-05 packet's manifest is now doubly stale, and the v2 links
finding count moved 1 → 2.** `python3 tools/harness/packet_links.py --packet
reports/round-15/handoff/packet-v2-05.yml --repo-root . --json` (2026-10-18)
reports two `M-DIGEST-MISMATCH` rows:

| subject | live | manifest in the filed packet | attribution |
|---|---|---|---|
| `tools/d2-typed-labels.py` | `76536a924280…` | `0da0015f7003…` | **this claim** (the round-20 impl); the new row is `reports/round-20/wart/expected-v2-07-r20.json` |
| `tools/harness/packet_links.py` | `66d854cc710f…` | `f81bc9f77527…` | **pre-existing** (present at round 18: the r18 baseline already recorded `links.findings 1`); out of this seat's scope |

Both rows resolve (50/50 links checked and resolved); the count of *findings*
moved, not the resolution. Consequence for a sibling seat: the round-20 handoff
v3 work must cite the r20 baseline, not `expected-v2-07-r18.json`.

**R2 — closed in this round (was a residual): `examples/culture-d4/expected-holds.json`'s
internal pins.** They named the round-19 projector and projection; the round's
counting command reads them as live pins, so they were re-pinned in place
(`09490a27…` → `18d0cfce…`, a surgical diff: two values, a `revision_note`, a
`supersedes_pins` block). The hold/note set did not move (fail 0 / hold 15 /
note 1). Note the asymmetry this leaves: a *filed* round receipt is never edited,
a *live* artifact's pins are.

**R3 — the rank-rule ledger is still family-independent.** `build_payload()`'s
rule set is the round-8 literal set, so a D4 projection carries those rules
(their authorities are D2's) and no file read is involved. The round-19 wart was
scoped to the *alias* leg and is closed; this one is a different leg, named here
so the next round can route it if it wants it. It is not hidden by this seat's
green readings: shard 3 §4 says the mirror test does not cover it.

**R4 — `d4-assembly-check-gate.py --selftest` remains unevaluable** (exit 2,
`assembly error: [Errno 2] No such file or directory: '--selftest'`): pre-existing,
documented in the r19-pre freeze notes, and untouched here. The gate's own run
mode is green (shard 5 row 11).

**R5 — the D4 family declares no costume-era reconciliation rows.** The r19
projection showed D2 `ERX-1..4` verdicts in a D4 projection; the r20 projection
shows the leg as `skipped` with the measured reason. A reader diffing r19 → r20
sees rows disappear: that is the wart leaving, not data loss — the rows were
D2's and never described D4.

## 3. Cross-claim coupling this seat created (for the integrator)

- `reports/round-20/handoff/design.md` lines 333 and 337 cite the **old** D4
  projection sha `a59990bb…` and the expected-holds sha `09490a27…`. Both moved
  (`cbcf997f…`, `18d0cfce…`). Any v3 packet row that pins them must re-measure;
  the same applies to `tools/assemble-d4-typed.py` (`1ddad6a7…` → `92f5460b…`)
  and `examples/culture-d4/packet.d4.typed.yml` (`f63ed531…` → `e823db67…`).
- `reports/round-20/report-draft.md` line 172 counts `grep -rl 0da0015f … | wc
  -l` → 106. Re-measured at 13:07Z with `--exclude-dir=.git --exclude-dir=.scratch
  --exclude-dir=__pycache__`: **82** files name the old projector sha, 3 name the
  new one. The difference is the exclusion set, not the tree; the number to carry
  forward is the one with its command.
- Nothing else in this lane's live pin set moved: `examples/culture-d2/**` is
  byte-identical (shard 4 row 9).

## 4. Limits

- Green readings are measurements at 13:06–13:12Z on a tree other seats are
  still writing; the pins are the durable part, the counters are not.
- The closure covers the alias leg, the adapter mirror and the D4 pin set, no
  more: R1's pre-existing row, R3 and R4 are open and named above.
- No canon: the era tags are fixture-relative, no date is synthesized, and the
  projector remains a designer audit aid.
