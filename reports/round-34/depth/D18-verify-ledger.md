- Seat: D18 | verifier | claim D | date 2026-10-19 | baseline da68a6d

# D18 — independent verification of the D4 ledger numbers D03 must rewrite

Read-only seat. No filed byte written; every command ran from the repo root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; audit window
`AUDIT_UTC=2026-10-19T07:04:23Z` (`date -u`). I re-read the live D4 artifacts myself
and did **not** copy any number from `claims.json`, `reports/round-33/adj/A02-handoff.md`,
or the r6 packet's own prose. The only write by this seat is this fragment.

## Dependency state (measured, not assumed)

`find reports/round-34 -maxdepth 3 | sort` at 2026-10-19T07:04Z returns exactly:
`reports/round-34/claims.json`, `reports/round-34/targets.json`,
`reports/round-34/telemetry/dispatch-declared.json` — **no fragment directories yet**,
so `depth/D03-ledger-rows.md` does not exist. Per the missing-dependency rule I built the
oracle table first (§1), filed the checking rule D03 can be verified against (§7), and owe
the row-for-row leg (§Owed).

## Method (three independent legs per number)

1. Read the live artifact directly; take the number from its declared counting block.
2. **Recount** the same quantity from the underlying array/object in the same file, so no
   number rests on one field.
3. Anchor the file digests to the pins the r6 packet itself carries, to prove I read the
   same bytes the packet names.

## §1 Live truth table — the oracle for D03

Digests re-measured with `sha256sum` (2026-10-19T07:0xZ), and each equals the digest the
r6 packet pins at `reports/round-30/handoff/declared-in-r6/packet.md:68` (typed-labels) and
`:69` / `:106` (expected-holds): `typed-labels.d4.yml` = `c23b0ab5…ea13f82e`,
`expected-holds.json` = `e6ae9828…9166bfba3`.

| field | live value | declared citation | independent recount in the same file |
|---|---|---|---|
| `typed_labels` | **82** | `typed-labels.d4.yml:46` | `len(typed_labels.labels)` = 82 (`:614-615` header, first label `:616`, last `NM-08` `:2856-2863`) |
| `labels_by_kind.native-form` | **64** | `:37` | recount of `labels[].kind` = 64 |
| `labels_by_kind.translated-label` | **12** | `:38` | recount = 12 |
| `labels_by_kind.borrowed-strata` | **6** | `:36` | recount = 6 (sum 64+12+6 = 82 = `typed_labels`) |
| `findings_total` | **12** | `:32` | `len(findings)` = 12 (`:209-294`), all `severity: hold`, all `id: D2L-FORM-UNRESOLVED` |
| `findings_hold_or_fail` | **12** | `:31` | = 12 holds + 0 fails, matches the findings array |
| `label_findings_hold` / `label_findings_fail` | **12 / 0** | `:34` / `:33` | every one of the 12 findings is a form hold on a label-bearing record |
| `stats` | **fail 0 / hold 12 / labels 82** | `:2865-2868` | agrees with `coverage` and with the array recounts |
| `conflicts` | **0** | `:30` | `era_reconciliation.two_to_one` = `[]` (`:175`) |
| `rank_quarantine_handles` | **0** | `:40` | `rank_rules.quarantine` = `[]` (`:603`) |
| `rank_rules_unresolved_items` | **0** | `:44` | `rank_rules.unresolved` = `[]`; `residuals`/`act_rules`/`assay_gaps`/`calibration_flags`/`jurisdiction_gaps`/`entitlement_edges` all `[]` (`:303-312, 603-612`) |
| `rank_rules_component` / `_gate_projected` / `_normalized` | **4 / 4 / 4** | `:41-43` | `len(normalized_rules)` = 4 (`:462-602`), `len(gate_rank_rules)` = 4 (`:320-460`) |
| `reconciliation_records` | **6** | `:45` | `len(era_material_reconciliation.records)` = 6 (`:50-123`); summary `claims 6, findings 0` (`:129-134`) |
| era alias rows | **4** | `:137-162` | `alias_rows` ER-01..ER-04 |
| expected-holds `counts` | **hold 12 / note 0 / fail 0** | `expected-holds.json:46-49` | `len(holds)` = 12 (`:51-124`), every `id: D2L-FORM-UNRESOLVED`, `where` = GAR-01..GAR-06 + LEX-GAR-01..LEX-GAR-06; `notes` = `[]` (`:125`) |
| expected-holds second witness | **hold 12 / note 0 / fail 0** | `packet.d4.typed.yml:3417-3420` (`pipeline_counts`) | independent file, same numbers (digest `d581e0ad…` pinned at `packet.md:67`) |
| rank-rule mechanism (qualitative) | `act_rules` **empty**; every `normalized_rules[].adapt_status` = **`executable`** | `:303`, `:462-602` | no `cannot-evaluate` and no `partial` row exists anywhere in the live file |

The live `expected-holds.json` also carries `active_pin_generation: round-30-qreg-records`
(`:6`) — the hold set is not an r18-era relic.

## §2 Row-by-row verdicts — the five surfaces D03 must rewrite

Live truth per §1. `MATCH` cells must be left alone; only `MISMATCH` cells are defects.

| r6 surface | token in r6 | live | verdict |
|---|---|---|---|
| `packet.md:148` D4-CL05 | `typed_labels 74` | 82 | **MISMATCH** |
| `:148` | `native-form 56` | 64 | **MISMATCH** |
| `:148` | `translated-label 12` / `borrowed-strata 6` | 12 / 6 | MATCH |
| `:148` | `findings_total 16` | 12 | **MISMATCH** |
| `:148` | `findings_hold_or_fail 15` | 12 | **MISMATCH** |
| `:148` | `label_findings_fail 0`, "(12 label holds, 0 label fails)" | 0, 12 holds | MATCH |
| `:148` | `stats (fail 0, hold 12, labels 74)` | 0 / 12 / 82 | `fail`+`hold` MATCH, `labels 74` **MISMATCH** |
| `:149` D4-CL06 | `hold 15` | 12 | **MISMATCH** |
| `:149` | `note 1` | 0 | **MISMATCH** |
| `:149` | `fail 0` | 0 | MATCH |
| `:149` | composition "twelve `D2L-FORM-UNRESOLVED` … and three `D2L-RANK` holds, plus one `D2L-RANK` note" | 12 form holds, **0** rank holds, **0** notes | **MISMATCH (composition, not arithmetic)** |
| `:150` D4-CL07 | `conflicts (4)` | 0 | **MISMATCH** |
| `:150` | `quarantine handles (3)` | 0 | **MISMATCH** |
| `:150` | `reconciliation records (6)`, "six records … summary claims 6 findings 0" | 6, 6, 0 | MATCH |
| `:152` D4-CL09 | `rank_rules_unresolved_items 13` | 0 | **MISMATCH** |
| `:152` | `rank_quarantine_handles 3` | 0 | **MISMATCH** |
| `:152` | `conflicts 4` | 0 | **MISMATCH** |
| `:152` | mechanism: "act rows carry `adapt_status: cannot-evaluate` because speech is not a gate-modelled channel" | no act rows at all; 4 normalized rules, all `executable` | **MISMATCH (false mechanism, §5a)** |
| `:307` OQ-V3-05 | "twelve form holds" | 12 | MATCH |
| `:307` | "three rank holds" / "one note" | 0 / 0 | **MISMATCH** |
| `:307` | "thirteen unresolved rank items" / "three quarantine handles" / "four conflicts" | 0 / 0 / 0 | **MISMATCH** |

**Counter-control — rows that are already live-correct and must NOT be touched by D03/D05:**
`packet.md:68` (A-30: 82 / 64 / 12 / 6, 12 findings, 0 unresolved rank items, 4 era-alias rows),
`:69` (A-31: 12 holds / 0 note / 0 fail), `:284` (D2 read-only facts — re-measured against
`examples/culture-d2/typed-labels.d2.yml`: 58 / 46 / 10 / 2, findings 16 with 15 hold-or-fail,
13 unresolved, 3 quarantine, 4 conflicts, 10 reconciliation — all MATCH), `:285` (D4 read-only
facts: 82 / 64 / 12 / 6, 12 findings /12 hold-or-fail, 0 unresolved, 0 quarantine, hold set
12 / 0 — all MATCH). The r6 pair therefore **contradicts itself**: `:285` and `:68/:69` already
agree with live bytes while `:148-152` and `:307` do not (this is the A02-H1 self-contradiction,
re-derived here from my own reads, not quoted).

Twin parity: the stale text is duplicated in the machine twin —
`twin.json` contains the phrase `thirteen unresolved rank items` **2×**, `three quarantine handles`
**2×**, `four conflicts` **3×**, `hold 15` **1×**, `note 1` **1×** (my `str.count` over the raw file).
So a Markdown-only rewrite leaves the twin stale in the same places.

## §3 Provenance of the stale figures — they are an old generation, not fabrications

Scan of every `typed-labels.d4.yml` revision outside `.scratch` (`find … | sort`, parsed with
`json.loads`):

| generation | digest8 | typed / native | findings | unres / quar / conf | comp / gate / norm | act rows |
|---|---|---|---|---|---|---|
| `tools/gates/frozen/round-18/inputs/examples/culture-d4/typed-labels.d4.yml` (= `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/…`) | `a59990bb` (= `cbcf997f`) | 74 / 56 | 16 = 15 hold + 1 note | **13 / 3 / 4** | 21 / 5 / 9 | 13, all `cannot-evaluate` |
| `tools/gates/expected/d4-typed-labels-check-gate/r22-post/…` (= `frozen/round-22/d4-repin/…`) | `60b526b0` | 74 / 56 | 12 | 0 / 0 / 0 | 4 / 4 / 4 | 0 |
| `reports/round-27/pinsweep/frozen/r27-post/…` | `88a94422` | 82 / 64 | 12 | 0 / 0 / 0 | 4 / 4 / 4 | 0 |
| `reports/round-28/pinsweep/frozen/r28-post/…` | `339bfd83` | 82 / 64 | 12 | 0 / 0 / 0 | 4 / 4 / 4 | 0 |
| live `examples/culture-d4/typed-labels.d4.yml` (= `reports/round-31/sweep/frozen/r31-post/…`) | `c23b0ab5` | 82 / 64 | 12 | 0 / 0 / 0 | 4 / 4 / 4 | 0 |

Findings: every stale token in `:148-152` and the composition in `:149` are **exactly the
r18/r19-pre generation's values** (`a59990bb`), including the composition
`12 × D2L-FORM-UNRESOLVED + 3 × D2L-RANK holds + 1 × D2L-RANK note` (r18 findings id counter
= `{D2L-FORM-UNRESOLVED: 12, D2L-RANK: 4}` = 3 holds + 1 note by severity `{hold: 15, note: 1}`).
So the r6 literals are a real historical generation, ~11 rounds stale on the label counts (the
74/56 → 82/64 step landed at round 27, `a59990bb`/`60b526b0` → `88a94422`) and pre-r22 stale on the
findings/rank numbers (the 13/3/4 → 0/0/0 and act-row removals landed at round 22, `cbcf997f` →
`60b526b0`). This is the stale-generation class, not fabrication — but it is stale, and the r6
row cites it as if read from today's bytes.

**Disambiguation of the `:149` number.** The r6 row cites `examples/culture-d4/expected-holds.json#counts`
for `hold 15, note 1`. No D4 hold-file generation ever carried those counts: the only two D4
copies on disk are the live file (`e6ae9828`, 12/0/0) and `frozen/round-22/d4-repin/…`
(`3826ba68`, 12/0/0). The **live D2** hold set does say `hold 15, note 1`
(`examples/culture-d2/expected-holds.json#counts`) — but its composition is
`{D2L-FORM-UNRESOLVED: 10, D2L-NATIVE: 2, D2L-RANK: 3}` + 1 `D2L-RANK` note, which does **not**
match the r6 prose. The r18/r19-pre **D4 projection** does match the prose composition exactly.
Verdict: `:149` reproduces the r18-generation projection's counts while the cell's *citation*
points at a hold file whose every D4 generation says 12/0/0; the equality with the live D2 file is
a same-value coincidence, not the source. Either way the row is a defect: the cited file does not
contain the quoted number. (Marked here because "wrong file, right-looking number" is exactly the
class that survives a totals check.)

## §4 What is not stale (so the r7 diff stays minimal)

Within the D4 claim rows the only drifted surfaces are `packet.md:148, :149, :150, :152, :307` and
their twin copies. `:68`, `:69`, `:284`, `:285` and the whole D4-CL01..CL04, CL07-numbers,
CL08, CL10-CL12 legs I spot-checked (`brief.md` canon block, `packet.d4.yml#era_records` ER-01..ER-04,
`RK-01..RK-04`, `form_slots` LEX-GAR-01..06 `unfilled`, `alias_rows` 4, `PR-01..PR-09` presence)
agree with live bytes on my reads. A rewrite that touches `:68/:69/:284/:285` would be introducing
drift, not fixing it.

## §5 Two traps a number-only rewrite will step into

**(a) D4-CL09's mechanism sentence is false live, not merely mis-numbered.** Live `rank_rules`
has `act_rules: []` (`:303`) and all four `normalized_rules[].adapt_status` = `executable`
(`:462-602`); `quarantine`/`unresolved`/`residuals` are all `[]`. The r18 generation did carry
13 act rows, all `cannot-evaluate`, and 9 normalized rows of `partial`/`cannot-evaluate`
(`a59990bb`) — that is where the sentence came from. Rewriting `13/3/4 → 0/0/0` while keeping
"act rows carry `adapt_status: cannot-evaluate`" leaves a false statement in a row whose status is
`unresolved`. D03/D04 must rewrite the clause, not just the integers.

**(b) Two legitimate hold counts live in the D4 tree, and the wrong one is easy to cite.**
The pre-implementation *declaration* is 6 (`examples/culture-d4/packet.d4.typed.yml:165-202`, its
`counts:` at `:199-202` = hold 6 / note 0 / fail 0; `examples/culture-d4/components/01-brief.yml:66`
"six unresolved garment form slots, zero fails"), while the *committed* set is 12
(`expected-holds.json:46-49`, corroborated by `packet.d4.typed.yml:3417-3420 pipeline_counts`). The
r7 rows must quote the committed 12 and may mention the six-row declaration only as the reconciled
delta. Additionally, the r18 generation was **internally inconsistent** (its
`coverage.findings_hold_or_fail` = 15 while its own `stats.hold` = 12 and its findings array held
15 holds + 1 note) — so a fix that copies the old packet's / old generation's tokens wholesale
re-imports that inconsistency and fails my check.

## §6 Negative control — the method is not a blanket "stale" stamp

Ran the five surfaces through the checker with the §1 table as the oracle. It flagged the
mismatches above **and passed** the live-correct cells it must leave alone: `hold 12` and `fail 0`
inside `:148`, `fail 0` inside `:149`, `translated-label 12`, `borrowed-strata 6`,
`label_findings_fail 0`, `reconciliation records (6)`, `:307`'s "twelve form holds", and the
whole of `:68/:69/:284/:285`. Discrimination is therefore demonstrated in both directions on the
same run.

**Why every filed green check coexisted with this (independent of A02's reading):** the stale set is
arithmetically *internally consistent* — 56 + 12 + 6 = 74, 12 label holds + 3 rank holds = 15
hold-or-fail — so no totals check can catch it; catching it requires comparing against live bytes,
which is exactly what the gate does not do (the packet's own gate line `:295` asserts
`fields=16/16, glossary-entries=20, findings=0`, a shape verdict). A stale generation that is
self-consistent is the failure mode my method has to be built against, and is why §7's oracle is
pre-registered rather than recomputed ad hoc.

## §7 Interface filed for D03 (mechanical check, no re-derivation needed)

- For each of `packet.md:148, :149, :150, :152, :307` (and the twin's matching rows), D03's
  replacement row must carry the value from §1 **with a live citation path:line**.
- Checking rule for the integrator (or a later verifier): extract every integer from a D03 row,
  match it to its field label, look the label up in §1. Integer present in §1 and unequal →
  **defect**; label absent from §1 → *not in oracle*, and D03 must cite it independently or mark
  it `to-verify`. Cells listed MATCH in §2 are `leave-alone` cells.
- Verdicts I will file when the fragment lands: a row-for-row MATCH/MISMATCH table plus a defect
  list, in this file or its successor fragment — not by editing this one after D03 lands, so the
  oracle above stays a pre-registration.
- Filed-row discipline: this seat wrote no filed byte; `git status --porcelain reports/round-2[0-9]
  reports/round-3[0-3]` is expected empty from this seat's work (only `reports/round-34/depth/`
  gains a file).

## §8 Limits and to-verify

- `depth/D03-ledger-rows.md` did not exist at 2026-10-19T07:04Z → the row-for-row leg is owed
  (§Owed). Everything above is the oracle plus the r6-side verdicts, which are complete.
- I did **not** re-run `tools/assemble-culture-d4.py`, `tools/assemble-d4-typed.py` or
  `tools/d2-typed-labels.py` (a rebuild would rewrite the live projections). The live numbers are
  verified as *declared value = recount from the same file's arrays*, not as "the projector computes
  them"; the projector-side provenance is the D4 claim rows' own leg and stays with D05/D07.
- I did not run any `reports/round-*/run-validation.py` (F-C13-1) and ran no round runner.
- My §1 table is bound to digests `c23b0ab5…` (typed-labels) and `e6ae9828…` (expected-holds) as
  read at 2026-10-19T07:0xZ. If any D4 artifact is rebuilt later in the round, §1 must be
  re-measured before it is used as an oracle — otherwise this table is `to-verify` against the
  new bytes.
- The `:284` D2 facts I re-measured come from `examples/culture-d2/typed-labels.d2.yml`; I did not
  re-derive the D2 `packet.d2.yml#to-verify` line count (21) or the D2E-01..29 edge count, which
  are outside the D4 ledger scope of my mission.

## Owed

- `reports/round-34/depth/D03-ledger-rows.md` — absent at write time (`find reports/round-34
  -maxdepth 3` = claims.json, targets.json, telemetry/dispatch-declared.json only). The
  row-for-row verification of every D03 replacement row against the §1 oracle is owed to the
  integrator; the oracle (§1) and the checking rule (§7) are filed above so the comparison needs no
  re-derivation. If D03 lands with values differing from §1, the discrepancy is a defect against
  whichever side disagrees with the digest-pinned live bytes at `c23b0ab5…` / `e6ae9828…`.

## Citations

- Live artifacts: `examples/culture-d4/typed-labels.d4.yml:29-47,137-162,175,209-294,303,320-460,462-602,603-612,614-615,2865-2868`;
  `examples/culture-d4/expected-holds.json:6,46-49,51-124,125`;
  `examples/culture-d4/packet.d4.typed.yml:165-202,3417-3420`;
  `examples/culture-d4/components/01-brief.yml:66`; `examples/culture-d2/typed-labels.d2.yml`
  (`coverage` parse); `examples/culture-d2/expected-holds.json` (`counts` parse).
- r6 pair: `reports/round-30/handoff/declared-in-r6/packet.md:67,68,69,106,148,149,150,152,284,285,295,307`;
  `reports/round-30/handoff/declared-in-r6/twin.json` (phrase counts via `str.count`).
- Generation lineage: `tools/gates/frozen/round-18/inputs/examples/culture-d4/typed-labels.d4.yml`
  (`a59990bb`), `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/typed-labels.d4.yml`
  (`cbcf997f`), `…/r22-post/typed-labels.d4.yml` (`60b526b0`), `…/r20-post/…`,
  `tools/gates/frozen/round-22/d4-repin/inputs/examples/culture-d4/{typed-labels.d4.yml,expected-holds.json}`
  (`60b526b0`, `3826ba68`), `reports/round-27/pinsweep/frozen/r27-post/inputs/…` (`88a94422`),
  `reports/round-28/pinsweep/frozen/r28-post/inputs/…` (`339bfd83`),
  `reports/round-31/sweep/frozen/r31-post/inputs/…` (`c23b0ab5`).
- Prior context read but not relied on for any number: `reports/round-33/adj/A02-handoff.md`.
- Commands (all 2026-10-19, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `date -u '+AUDIT_UTC=%Y-%m-%dT%H:%M:%SZ'`;
  `sha256sum examples/culture-d4/{typed-labels.d4.yml,expected-holds.json,packet.d4.yml,packet.d4.typed.yml} tools/d2-typed-labels.py`;
  `wc -l examples/culture-d4/{typed-labels.d4.yml,expected-holds.json}`;
  `find reports/round-34 -maxdepth 3 | sort`; `find . -name 'typed-labels.d4.yml' -not -path './.git/*' -not -path './.scratch/*' | sort`;
  `find . -name 'expected-holds.json' -path '*d4*' …`;
  `python3` heredocs parsing the live files and every generation copy (coverage blocks, findings
  id/severity counters, `rank_rules` sub-block lengths, `adapt_status` counters, hold/note id
  counters) — outputs are quoted inline in §1/§3;
  `grep -n` for exact field line numbers in `typed-labels.d4.yml` / `expected-holds.json`;
  `grep -n -E '<stale tokens>' reports/round-30/handoff/declared-in-r6/packet.md`;
  `python3 -c` `str.count` over `twin.json`.

FILES: reports/round-34/depth/D18-verify-ledger.md | SUMMARY: independent re-derivation of every D4
ledger number; live truth table filed as the oracle (82/64/12/6, findings 12/12, conflicts 0,
quarantine 0, rank items 0, hold 12/0/0, digests c23b0ab5… / e6ae9828…); all five r6 surfaces
(`packet.md:148,149,150,152,307`) verified stale against live bytes with MATCH cells named for
leave-alone; the stale figures traced to the r18/r19-pre generation `a59990bb` (not fabrication);
two non-arithmetic defects filed (`:152` false `cannot-evaluate` mechanism; `:149` cites
`expected-holds.json#counts` for a number no D4 hold-file generation ever carried); D03 absent, its
row-for-row check owed with the oracle and checking rule pre-registered.
