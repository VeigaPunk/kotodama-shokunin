# `corpus/lessons/` — reconciled index (round 25, 2026-10-18)

This directory is the lane's append-only lesson record: one file per round that
ran, written by the round's gate-keeper (SCRIBE) seat. At this seat's opening
it had **24 filed lessons, three census formats and no index**. This README is
that index: one row per file the runner's partition glob returns (26 at the
final stamp — the 24 filed lessons, the round-25 lesson that landed mid-audit,
and this file itself), the open-question queue with an owner per item, and the
three formats documented.

- **Owner of this file:** the C seat of round 25 (claims `R25-C31..C34` in
  `reports/round-25/claims.json`). The round's counting command is
  `python3 reports/round-25/run-validation.py`.
- **Canon:** NON-CANON engineering evidence. This index admits nothing,
  certifies no round, and blesses no lesson. It is a pointer file, not a
  verdict. The per-round verdicts stay in the round receipts and in `LOG.md`.
- **Filed lessons are read-only.** Every lesson file listed below is filed
  bytes: this index never edits them, and a correction lands as a new file or
  a new dated record, never as an in-place rewrite. The round-19 lesson-path
  collision (X24-L1 / X28-1) is the standing example and remains the parent's
  disposition.
- **Re-derivation, not inheritance.** Every `bytes=` / `lines=` / `sha8=`
  cell below was re-measured from the live bytes at
  **2026-10-18T17:35Z** by the read-only tool
  `reports/round-25/audit/c31-lessons-index-audit.py` (`--json` prints the
  receipt). A consumer must re-measure rather than inherit: the two loop-era
  lessons that carry a filed auditor pin (round 19 `0c975cf1…`, round 23
  `b567a60a…`) still reproduce those exact prefixes here, which is the
  continuity control for this table.

## 1. Counting command

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest  # 26/26, exit 0
python3 -B reports/round-25/audit/c31-lessons-index-audit.py             # census + findings
python3 -B reports/round-25/audit/c31-lessons-index-audit.py --json      # receipt

ls corpus/lessons/*.md | wc -l                                          # 26 (2026-10-18)
find corpus/lessons -maxdepth 1 -name '*.md' | wc -l                    # 26 (same set)
```

The tool answers one question per claim id, plus two self-consistency checks
this seat added:

| id | question | green means |
|---|---|---|
| C31 | index rows == files | every `*.md` file has exactly one row here, and every row names a file on disk; no duplicates |
| C32 | owners resolve | every open-question row's owner is a live path, `operator`, or a round pointer that resolves |
| C33 | formats documented | the format classes the partition carries are a subset of the three documented in §3 |
| C34 | pins re-derived | each row's `bytes`/`lines`/`sha8` cells equal the live bytes |
| C34b | prose arithmetic | this file's own stated row and lesson counts equal the measurement |
| C34c | shape cells re-derived | each row's `format` and `contract` cells equal the live bytes |

`--selftest` is 28 in-memory controls (exit 0), including the negative
controls: a non-row line, a header row and a `## Gate candidates` prose
heading must not be misread, a missing path and an empty owner must not
resolve, and an unescaped inner pipe must make the row refused rather than
misparsed.

## 2. Per-round index

Columns: **file** · **format** (§3) · **contract** (`source:`/`verified-at:`/
`recheck:`/`scope:` lines present, of 4) · **open-questions carried** (ids from
§4) · **disposition pointer** (where the round's verdict lives) · **pin**.

| file | format | contract | open-questions carried | disposition pointer | pin |
|---|---|---|---|---|---|
| `corpus/lessons/README.md` | index (this file) | — | — | itself: §1 | bytes=0 lines=0 sha8=self-referential |
| `corpus/lessons/round-1-gates-and-triage.md` | plain | 0/4 | — | `reports/round-1` not filed; record is `LOG.md` | bytes=1957 lines=39 sha8=7fc36614 |
| `corpus/lessons/round-2-adjacency.md` | plain | 0/4 | Q-02-1..4 | `reports/round-2` not filed; `.ufo/l0-questions.md` (fleet root) | bytes=5611 lines=98 sha8=2497bf44 |
| `corpus/lessons/round-3-d2-build.md` | plain | 0/4 | Q-03-1 | `reports/round-3` not filed | bytes=2827 lines=47 sha8=f784596e |
| `corpus/lessons/round-4-sol-fixes-and-audits.md` | plain | 0/4 | Q-04-1..4 | `corpus/lessons/round-4-audit/` (16 reports), `corpus/lessons/round-4-triage/`; **no `reports/round-4*` exists** (C35 correction) | bytes=1935 lines=35 sha8=adc87178 |
| `corpus/lessons/round-5-availability.md` | gate-keeper | 3/4 | Q-05-1 | `reports/round-5` | bytes=2666 lines=46 sha8=4e7d7c33 |
| `corpus/lessons/round-5.md` | gate-keeper | 3/4 | Q-05-2, Q-05-3 | `reports/round-5/validation.json` | bytes=8684 lines=117 sha8=83440a1a |
| `corpus/lessons/round-6.md` | gate-keeper | 3/4 | Q-06-1, Q-06-2 | `reports/round-6/checkpoint.json`, `reports/round-6/run-validation.py` | bytes=9180 lines=147 sha8=a9b92585 |
| `corpus/lessons/round-7.md` | plain | 3/4 | Q-07-1 | `reports/round-7` (runner excluded its own historical whitelist) | bytes=7535 lines=120 sha8=4d77c52c |
| `corpus/lessons/round-8.md` | fragment-index | 3/4 | Q-08-1 | `reports/round-8` | bytes=12146 lines=181 sha8=51de56a1 |
| `corpus/lessons/round-9.md` | fragment-index | 3/4 | Q-09-1 | `reports/round-9/validation.json` | bytes=15593 lines=223 sha8=2d9ed20e |
| `corpus/lessons/round-10.md` | fragment-index | 3/4 | Q-10-1 | `reports/round-10/validation.json` | bytes=16615 lines=241 sha8=4152eb02 |
| `corpus/lessons/round-11.md` | fragment-index | 3/4 | Q-11-1..3 | `reports/round-11/validation.json` | bytes=19300 lines=274 sha8=9b61d8bd |
| `corpus/lessons/round-12.md` | fragment-index | 3/4 | Q-12-1..3 | `reports/round-12` (no `validation.json`; provisional, no admission) | bytes=11312 lines=52 sha8=655896d1 |
| `round-13` | — | — | — | operator-skipped; **no lesson file exists** (see §5) | — |
| `corpus/lessons/round-14.md` | gate-keeper | 3/4 | Q-14-1, Q-14-2 | `reports/round-14/validation.json` | bytes=32860 lines=168 sha8=f3f85684 |
| `corpus/lessons/round-15.md` | gate-keeper | 3/4 | Q-15-1, Q-15-2 | `reports/round-15/validation.json` | bytes=27100 lines=122 sha8=13e17f0e |
| `corpus/lessons/round-16.md` | plain | 3/4 | Q-16-1 | `reports/round-16/civ-map.json` (map scribe; claim C owned by runner) | bytes=10937 lines=59 sha8=421bf6a1 |
| `corpus/lessons/round-17.md` | gate-keeper | 4/4 | Q-17-1, Q-17-2 | `reports/round-17` (round REJECTED; see `LOG.md`) | bytes=48841 lines=202 sha8=ce1741dc |
| `corpus/lessons/round-18.md` | gate-keeper | 4/4 | Q-18-1..3 | `reports/round-18/d4/holds.md`, `reports/round-18/validation.json` | bytes=68692 lines=236 sha8=20ababe0 |
| `corpus/lessons/round-19.md` | gate-keeper | 4/4 | Q-19-1, Q-19-2 | `reports/round-19/validation.json` | bytes=64818 lines=250 sha8=0c975cf1 |
| `corpus/lessons/round-20.md` | gate-keeper | 4/4 | Q-20-1..4 | `reports/round-20/validation.json` | bytes=43056 lines=182 sha8=d54eb3f7 |
| `corpus/lessons/round-21.md` | gate-keeper | 4/4 | Q-21-1, Q-21-2 | `reports/round-21` (no `validation.json` at the lesson's stamp) | bytes=10758 lines=45 sha8=2071454b |
| `corpus/lessons/round-22.md` | gate-keeper | 4/4 | Q-22-1..3 | `reports/round-22/routed-resolution.json`; round REJECTED on D | bytes=22477 lines=102 sha8=bfe06e58 |
| `corpus/lessons/round-23.md` | gate-keeper | 4/4 | Q-23-1..3 | `reports/round-23/integration/fragment-ledger.md` | bytes=14179 lines=51 sha8=b567a60a |
| `corpus/lessons/round-25.md` | gate-keeper | 4/4 | — (this round's own O/D/C claims are pending, not carried) | `reports/round-25/claims.json` | bytes=38520 lines=205 sha8=08f0337e |
| `corpus/lessons/supplement-opencode-1.md` | gate-keeper | 3/4 | Q-S1-1 | `reports/supplement-opencode-1` | bytes=5445 lines=89 sha8=f235fc0a |

**Rows: 26. Files: 26.** The count is the runner's own partition glob
(`corpus/lessons/*.md`), which includes **this README** and the round-25
lesson that landed while this index was being written. Round 5 contributes two
rows on purpose (the availability preflight and the round itself); round 13
contributes no row because no lesson file exists; `supplement-opencode-1.md`
is not round-numbered and is indexed as its own row. Round 24 has no lesson
file — its record is the promotion-review dossier under `reports/round-24/`;
if a lesson lands it adds a row (a new row, never an edit of a filed one).

The **self-row** for this README carries no pin (`sha8=self-referential`): a
file cannot contain its own digest. The C34 check exempts exactly this row
from pin equality and says so, rather than writing a placeholder digest that
would read as a measurement.

## 3. The three census formats

The partition grew three shapes. A reader must know which one they are holding
before quoting a lesson's verdict.

1. **gate-keeper survey** — a `## Gate` section with the marker vocabulary
   `Opening <axis> reading:` candidates, `Admitted` / `Rejected` lines and a
   `spot-check` sentence, plus the four contract lines. **14 files.**
   Sub-shape: rounds 19–20 carry the older three-candidate marker vocabulary;
   rounds 21–23 carry the newer `### Rule` + per-axis-section shape with no
   marker vocabulary. Both are counted as gate-keeper; a round-21/22/23 lesson
   is the current norm, not a contract regression.
2. **fragment-index** — the gate-keeper survey **plus** a `## Fragment index`
   section enumerating the round's report fragments. **5 files** (rounds
   8–12).
3. **plain lesson** — no `## Gate`: the pre-contract seed lessons (rounds 1–4)
   and round 16 (a map-scribe record, not a gate-keeper survey). **7 files.**
   Round 7 is also plain by this classifier: its `## Gate candidates` heading
   is prose, not a gate section, and it carries no `## Gate` block. This
   README also falls in this class by the same test — it carries no `## Gate`
   — so the histogram's **plain 7** is rounds 1–4, 7, 16 **and this file**;
   the index's own row labels it `index (this file)`.

Contract-line coverage tracks the round, not the format: rounds 1–4 carry
**0/4** (pre-contract seeds). Of the loop-era files, **rounds 17–23 carry 4/4**
and the rest — rounds 5 (both), 6, 7, 8, 9, 10, 11, 12, 14, 15 and the
supplement — carry **3/4**: each has `source:`, `verified-at:` and `recheck:`
but no `scope:` line. Histogram arithmetic: gate-keeper **14** = the 13 filed
plus the round-25 lesson; fragment-index **5** = rounds 8–12; plain **7** =
rounds 1–4, 7, 16 and this README. Total 26 = the runner's file set. Round 16 is the outlier: `source:`, `verified-at:` and
`scope:` but **no `recheck:`** (3/4, and no `## Gate`). This is the state the
round-20 X24 and round-23 X09 audits recorded, unchanged.

## 4. Open-question queue (one owner per item)

Each row is an open question a lesson carries forward, with the owner that can
close it. **Owner must resolve**: a live path in this repo, the literal
`operator`, or a round pointer. The C32 check re-verifies this column.

| Q-id | question | owner | status |
|---|---|---|---|
| Q-02-1 | handoff sample's intake serialization: contract §4 defaults to Markdown, the packet is YAML with no-agreement note, the checker cannot read its field forms | `corpus/knowledge/synthesis/worldbible-integration-contract.md` | open (lore decides) — round 12 A11-A12-handoff explicitly REJECTED the handoff over this class |
| Q-02-2 | §4 completeness: `validation` absent from the pinned revision while `/validation` is cited three times | `examples/handoff-packet.sample.yml` | open |
| Q-02-3 | §1 read gate: no kotodama-side read record (`lane, contract_id, revision, file_sha256, reader, read_at, evidence_pointer`) exists in this repo | `operator` | open (bilateral ack cannot be closed unilaterally) |
| Q-02-4 | packet digest not stabilizable at close; re-check the L0 record against the frozen submission | `parent` | open |
| Q-03-1 | naming-collision PHON-INVENTORY ×10: real coda/segment violations or an encoding mismatch | `tools/gates/naming-collision-gate.py` | open at filing; the round-4 residual class |
| Q-04-1 | DERIV-REPLAY ×8: component 03's explicit regex rules the naming gate cannot replay — needs a derivation adapter | `tools/gates/naming-collision-gate.py` | **open** — round 25's claim D is the adapter, and at this stamp the leg is **not delivered**: `D4L-ARGOT-DERIV` is absent from `tools/gates/typed-pipeline-gate.py` and `reports/round-25/argot/delta.md` names a four-step recipe with none taken |
| Q-04-2 | CROSS-HOLD ×1: real-language sweep stays a declared pre-publication gap | `corpus/QUALITY.md` | open, declared |
| Q-04-3 | 11 retained gap flags + 5 civ files (39 flags) routed to round 5 on the zai lane | `reports/round-5` | routed; see round-5 lesson for the reconciliation |
| Q-04-4 | target-setting fallacy: a declared target is not a measurement | `corpus/lessons/round-4-audit` | carried as craft rule |
| Q-05-1 | native model route refused at preflight; do not route through an implicit default or Flash alias and call it the non-flash Z.ai round | `operator` | open |
| Q-05-2 | freshness reconciliation: 5 scoped supported / 15 unresolved, not 13 confirmed whole claims | `reports/round-5/parent-reconciliation.json` | reconciled at round 5 |
| Q-05-3 | whole-corpus header conformance and numeric-rubric debts remain explicit | `corpus/QUALITY.md` | open |
| Q-06-1 | eleven partial-support round-6 assertions and four unresolved round-6 questions | `reports/round-6/checkpoint.json` | carried to rounds 7–9 |
| Q-06-2 | worker 09/11 temporary fleet-root writes: "zero outside writes ever" is not independently established | `parent` | open |
| Q-07-1 | fifteen original round-5 residuals, eleven partial and four unresolved round-6 questions, D2's twenty findings, corpus-header debts, legacy parser/fixture limits, cultural permission, name screening and lore receipt | `reports/round-7` | carried; the runner excluded round-7 paths from its historical whitelist |
| Q-08-1 | eleven partial-support / four unresolved reconciliation rows must each carry a named disposition | `reports/round-8` | carried to round 9 (`R9-R8-F01..F04`) |
| Q-09-1 | parent acceptance on a settled tree, independent re-run receipt and parent source re-fetch receipt for the round-9 F receipts | `parent` | open at filing |
| Q-10-1 | C: 4 receipt failures — two "no named gap (filler risk)" rows, one "no retrievable locator", one audit-count shortfall | `reports/round-10/validation.json` | recorded `acceptance_checks_passed: false` |
| Q-11-1 | the freshness ratio denominator is unresolved (192 vs the receipt's 0.788 arithmetic vs `summary.json`'s sum-194 rows) | `parent` | open |
| Q-11-2 | six rewritten prior-round receipts: restore or re-file — a scope incident, not freshness drift | `parent` | open |
| Q-11-3 | the `index-update-22.md` appendix to a filed round-10 artifact: reported, not absorbed | `reports/round-11` | reported |
| Q-12-1 | C23-F1: a differing round-9 normalized hash attributed to `.scratch` path leakage | `reports/round-12/recount/audit.md` | named finding |
| Q-12-2 | the combined target tuple stays inconsistent if read as `0.778 = 147/192` | `parent` | open |
| Q-12-3 | structured `adjacency/ledger.json` entry rows and the A01–A04 receipts are absent | `reports/round-12` | open |
| Q-14-1 | the failed runner-hash A/B and census C2 commands stay retained as failures; the append-only integrity control is scoped to the named erratum | `reports/round-14/retro-consistency.md` | scoped, not retroactive |
| Q-14-2 | the required actual SCORECARD summary append had not landed at close; a passing proposed-row check is not the append | `SCORECARD.md` | open at filing |
| Q-15-1 | handoff v2 design's named remainders OQ-V2-01..03 | `reports/round-15/handoff/v2-design.md` | open at filing |
| Q-15-2 | `tools/harness/packet_uncertainty.py` selftest RED (`ValueError: line 2: not a mapping row`) | `tools/harness/packet_uncertainty.py` | open at filing |
| Q-16-1 | the map-auditor's independent ≥10-entry stratified spot-check is the pending half of claim C | `reports/round-16/civ-map.json` | pending at filing (owner is the map-auditor seat) |
| Q-17-1 | D: 8 named misses on the typed pipeline; the round REJECTED on D | `reports/round-17` | rejected; routed to round 18 |
| Q-17-2 | the C scoring defect: every C07 entry self-cited to "fixed" | `reports/round-17` | superseded by the revised runner (F-X01-1) |
| Q-18-1 | A-07 (`examples/culture-d4/components/01-brief.yml`): the finding set must equal `contract.hold_set_declaration` exactly — contradicted by the delivered 15/1 set | `examples/culture-d4/components/01-brief.yml` | reported, not absorbed; parent's disposition |
| Q-18-2 | the authority question: "emitted-as-truth vs declared-as-truth" for the D4 expected set | `parent` | open; three seats hold it |
| Q-18-3 | the register class has no engine path (`D4L-REGISTER-UNRESOLVED`, six frozen rows) | `tools/d2-typed-labels.py` | open at filing |
| Q-19-1 | the lesson-path collision: `corpus/lessons/round-19.md` was assigned to two seats; R19-D08's entry is unintegrated at `reports/round-19/integration/d4-lessons-entry.md` | `parent` | **still open** (X24-L1 / X28-1); the two dispositions are append-under-authorship or land at a new path |
| Q-19-2 | `examples/culture-d4/expected-holds.json` carries no reconciliation pointer (`declared_expectation`, `fragment_of`, amendment pointer) | `examples/culture-d4/expected-holds.json` | open at filing; the reconciliation lives in `reports/round-18/d4/holds.md` |
| Q-20-1 | the declared `linguistics 20` count is named non-reproducible in `corpus/README.md` rev 1.5 | `corpus/README.md` | open |
| Q-20-2 | one stale live pin with no reader: `examples/culture-d2/expected-holds.json` `projector_sha256` vs the live projector | `examples/culture-d2/expected-holds.json` | open at filing; the D4 counterpart was re-pinned |
| Q-20-3 | the exercise's `--profile v2\|v3` routes and the contract-audit re-run owed at the survey's last stamp | `tools/exercise-handoff-e2e.py` | open at filing |
| Q-20-4 | the filed round-5/7/9 `validation.json` in-tree mutations by live seats (outside the runner's rounds-8–19 window) | `parent` | reported |
| Q-21-1 | the round-17 current-tree mismatch and the round-20 link-count discrepancy remain open in the defect ledger | `reports/round-21/defects/ledger.json` | open at filing |
| Q-21-2 | the regression report routes a still-superseded replay to the next round | `reports/round-21/defects/regression.md` | open at filing |
| Q-22-1 | the D4 fixture bleed: fix required at the producer `tools/d2-typed-labels.py` and its regenerated output | `tools/d2-typed-labels.py` | implemented at `0e81d9d`; confirmed by round-23 X04 (see `LOG.md` correction) |
| Q-22-2 | freshness threshold/recalibration: the recorded pause remains in force until the operator changes it | `operator` | open (pause in force) |
| Q-22-3 | successor pins must bind final bytes; a pin on moving bytes is not a pin | `reports/round-22/routed-resolution.json` | carried as craft rule |
| Q-23-1 | **committed to round 25:** a superseding handoff v3 claim map/baseline — D4-CL05/06/07/09 and OQ-V3-05 still describe the removed rank passengers | `reports/round-25/claims.json` | **in flight round 25** (claim O) |
| Q-23-2 | **committed to round 25:** the `PLACEHOLDER_RE` validator-wording disposition, so the full historical check runs without weakening any placeholder rule | `reports/round-25/claims.json` | **in flight round 25** (claim O) |
| Q-23-3 | **committed to round 25:** any combined-source successor row (D2 live/frozen pins, v2) not landed under round 23's O claim | `reports/round-25/claims.json` | **in flight round 25** (claim O) |
| Q-S1-1 | the 20 unresolved supplemental outcomes must be preserved, not hidden; all promotion boxes remain unverified by a non-author | `reports/supplement-opencode-1` | open at filing; round 24 promotion review addresses the boxes |

### Queue arithmetic

Measured 2026-10-18T17:4xZ by the §1 tool over the table above; re-run it
rather than inheriting these numbers.

- Rows: **49**. Of the 26 index rows, **23 carry at least one question**;
  the three that carry none are `round-1-gates-and-triage.md` (its lessons
  were closed within round 1), `round-25.md` (this round's own claims are
  pending, not carried) and this README's self-row.
- Owner classes: **path** (an in-repo surface that can close the item) — **37**;
  **role token** — **12** (`parent` 9, `operator` 3). No row has an empty or
  unresolvable owner; that is the C32 check.
- The `parent` rows are the integration and protection-discipline items
  `AGENTS.md` assigns to the parent (LOG/SCORECARD integration, filed-surface
  protection, the round-19 path collision, the authority question, the
  freshness pause's counterpart decisions).
- Four rows are **in flight in round 25** and are the cross-link between this
  index and the round's O/D claims: Q-04-1 (the round-17 derivation-adapter
  forecast that claim D targets) and Q-23-1..3 (the round-23 commitments claim
  O carries). Their owners point at `reports/round-25/claims.json`, the
  declaration surface that names them. **In flight is not delivered**: this
  index records the leg as still open at its stamp, because the D seat's own
  `reports/round-25/argot/delta.md` measures it undelivered. A later revision
  of this index may close the row; that is a new row state, not a rewrite of
  the finding.
- This queue is **extracted, not exhaustive of prose**: a lesson's narrative
  "lessons carried forward" section can contain craft rules with no owner. The
  rule here is that anything a lesson names as *open* must appear above with
  an owner, and anything above must be traceable to a lesson file. The C32
  check enforces the owner half; the traceability half was checked by hand
  against each lesson's residual/queue section (see §6, known limit).

## 5. Structural notes a reader must not misread

- **No round-13 file.** Round 13 was operator-skipped; no work landed
  (`LOG.md:3077-3078`). A missing round in the sequence is a record fact, not
  a missing deliverable. The round-19 collision (`corpus/lessons/` has no
  naming convention for a second seat's material) is the same ambiguity seen
  from the other side.
- **Two round-5 rows.** `round-5-availability.md` is the preflight refusal
  record; `round-5.md` is the round. Both are filed and both are indexed.
- **Round 5's lesson table is author-side.** Its Gate explicitly says the
  readings are "author-side readings/reviews, not independent non-author
  promotion verification". Quoting a round-5 green as promotion evidence
  misreads the lesson.
- **A lesson is not a verdict.** Every gate-keeper survey in this directory
  says some variant of "Admitted by X01: none" and routes the verdict to the
  assigned runner and the parent. The index above therefore points each row at
  a *disposition pointer*, not at a verdict.
- **Gate-shape readings bind to a stamp.** The partition is a live-wave
  surface: round 23's lesson landed *inside* the round-23 audit's own window.
  Any later re-read of this index is a new measurement, and a lesson landing
  after this stamp adds a row rather than changing one.
- **Nine evidence subdirectories are part of the partition and are NOT
  indexed above.** `corpus/lessons/` carries 146 files under nine directories
  beside the 26 `*.md` lesson files, and the §2 rows cover only the `*.md`
  files. They are the per-round source/triage/audit material the lessons cite:

  | directory | files | carries |
  |---|---|---|
  | `round-1-triage/` | 42 | round-1 triage fragments (`C1.md`…) |
  | `round-2-triage/` | 43 | round-2 triage fragments |
  | `round-3-triage/` | 1 | `orchestrator-direct.md` |
  | `round-4-audit/` | 16 | 13 `civ-*` audits + 3 partition audits |
  | `round-4-triage/` | 2 | `frozen-run-standard.md`, `mesoamerica.md` |
  | `round-5-sources/` | 10 | source receipts (`04.json`…) |
  | `round-6-sources/` | 12 | source receipts |
  | `round-7-sources/` | 5 | source receipts |
  | `supplement-opencode-1/` | 15 | `sources/` receipts |

  They are **not** round files and carry no `## Gate`, so the three-format
  census does not classify them; a reader who needs a lesson's underlying
  evidence must look in the directory beside it. This is a named coverage
  limit of the index, not a claim that they were checked. Two of the nine are
  the correct targets for pointers the §2 rows previously mis-cited as
  `reports/round-4-audit` / `reports/round-4-triage` (C35 correction).

## 6. Boundary record

- **Writes:** this file and `reports/round-25/audit/c31-lessons-index-audit.py`
  (+ its receipt via stdout redirect). No `corpus/lessons/round-*.md` byte was
  touched, no filed round 8–24 artifact was edited, no tool or gate was
  changed. No commit, no push.
- **Controls:** the tool's `--selftest` is 26/26 in-memory checks, including
  the negative controls (a non-row line and a header row must not parse as
  index rows; a missing path and an empty owner must not resolve; the
  fragment-index classifier must win over gate-keeper). The before-control for
  this file is the same tool with the README absent: `C31-0 missing-index`,
  exit 1.
- **Independence:** this index was re-derived from the live bytes by the tool
  in §1, not transcribed from the round-19 X28, round-20 X24 or round-23 X09
  auditor receipts. Where those receipts and this census agree (round-19
  `0c975cf1…`, round-23 `b567a60a…`, the 24 filed lessons, the contract-line
  pattern), the agreement is an independent cross-check, not inheritance.
- **Known limit:** the queue in §4 is a *reading* of each lesson's open-item
  prose. It is not machine-verifiable end-to-end — a lesson could name an open
  item in a sentence this extraction missed. The C32 check verifies the owner
  column, not the extraction's completeness; completeness was checked by hand
  against the round-2 `## Open questions` block and the residual/queue sections
  of rounds 4–7, 14–23 and the supplement.

Index revision 1 (2026-10-18, round 25). Superseding edits land as a new
revision block here, never as an in-place rewrite of the per-round rows'
provenance claims.

## Revision 2 — C35 final pass (2026-10-18)

Seat **C35** (claim C, `R25-C35..C36`) read the settled revision-1 bytes and
fixed three defects the §1 tool does **not** check — it verifies the row/file
set, the owner column, the format classes and the pin cells, but it resolves no
disposition pointer and counts no evidence subdirectory:

1. **A disposition pointer cited a path that does not exist.** The round-4 row
   pointed at `reports/round-4-audit` and `reports/round-4-triage`; neither
   exists. The round-4 lesson's own wording ("17 audit reports under
   round-4-audit/") names a directory in the **lessons** partition, and the
   live bytes are `corpus/lessons/round-4-audit/` (16 files) and
   `corpus/lessons/round-4-triage/` (2 files). Measured 2026-10-18:
   `ls -d reports/round-4*` → no such file; `find corpus/lessons/round-4-audit
   -type f | wc -l` → 16. Pointer corrected. The lesson's own "17" is a
   round-4-era count against a 16-file directory — a filed-byte discrepancy,
   recorded here and **not** repaired (filed lessons are read-only).
2. **The nine evidence subdirectories were undocumented.** §5 previously
   covered only the `*.md` lesson files; 146 files under nine directories went
   unnamed. Added as a table with a named coverage limit — they are evidence,
   not lesson files, and the three-format census does not classify them.
3. **The round-25 row's pin was stale.** The X38 gate-keeper survey appended to
   `corpus/lessons/round-25.md` after the index pinned it; the cell read
   `bytes=26897 lines=150 sha8=feccf068` against live `38520 / 205 /
   08f0337e`. Pin refreshed to the settled bytes (measured 2026-10-18T17:47Z,
   stable across five 30-second samples). This is a **new measurement of a new
   revision**, not a correction of a filed value: the earlier pin was true of
   the bytes that existed when it was written.

Control for this revision: `python3 -B
reports/round-25/audit/c31-lessons-index-audit.py` over the edited bytes →
**findings: 0**, `--selftest` 28/28 (2026-10-18T17:47Z). The §1 tool's
`C34b_prose_arithmetic` check re-derives this file's own stated counts, so the
row/pin edits above are machine-checked; the pointer and subdirectory fixes are
hand-verified and named here because no tool resolves them.

Boundary: this revision writes only this file. No `corpus/lessons/round-*.md`
byte, no filed round 8–24 artifact, no tool and no gate was touched. The
revision-1 rows' provenance claims stand unedited; this block is appended, per
the file's own closing rule.
