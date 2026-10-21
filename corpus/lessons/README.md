# `corpus/lessons/` — reconciled index (round 25, 2026-10-18)

This directory is the lane's append-only lesson record: one file per round that
ran, written by the round's gate-keeper (SCRIBE) seat. At this seat's opening
it had **24 filed lessons, three census formats and no index**. This README is
that index: one row per file the runner's partition glob returns (26 at the
revision-1 stamp — the 24 filed lessons, the round-25 lesson that landed
mid-audit, and this file itself; **33 at the revision-3 stamp of 2026-10-19**,
see the revision-3 block at the foot of this file), the open-question queue
with an owner per item, and the three formats documented.

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
python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest  # 28/28, exit 0
python3 -B reports/round-25/audit/c31-lessons-index-audit.py             # census + findings
python3 -B reports/round-25/audit/c31-lessons-index-audit.py --json      # receipt

ls corpus/lessons/*.md | wc -l                                          # 37 (verifier integration, 2026-10-21)
find corpus/lessons -maxdepth 1 -name '*.md' | wc -l                    # 37 (same set)
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
| `corpus/lessons/round-26.md` | gate-keeper | 4/4 | Q-26-1, Q-26-2 | `reports/round-26/validation.json` (`acceptance_checks_passed: true`, 2026-10-18T19:09:32Z; the lesson's own closing read was `false` at 18:28:22Z, `corpus/lessons/round-26.md:178-186`) | bytes=60054 lines=222 sha8=cae06660 |
| `corpus/lessons/round-27.md` | gate-keeper | 4/4 | Q-27-1..4 | `reports/round-27/validation.json` (`acceptance_checks_passed: true`, 2026-10-18T20:08:49Z; the lesson read two earlier receipts `false` at 19:27:19Z / 19:28:22Z, `corpus/lessons/round-27.md:165-193`) | bytes=54972 lines=203 sha8=f15e285b |
| `corpus/lessons/round-28.md` | gate-keeper | 4/4 | Q-28-1..5 | `reports/round-28/validation.json` (`acceptance_checks_passed: true`, 2026-10-18T20:50:17Z) | bytes=50419 lines=145 sha8=dd832ff7 |
| `corpus/lessons/round-29.md` | gate-keeper | 3/4 | Q-29-1..3 | `reports/round-29/validation.json` (`acceptance_checks_passed: true`, 2026-10-18T21:50:07Z; the lesson's closing read had no receipt at 21:13:09Z, `corpus/lessons/round-29.md:110`) | bytes=17847 lines=118 sha8=b6765d33 |
| `corpus/lessons/round-30.md` | gate-keeper | 3/4 | Q-30-1..5 | `reports/round-30/validation.json` (`acceptance_checks_passed: true`, 2026-10-18T22:32:36Z) | bytes=30665 lines=181 sha8=56e77835 |
| `corpus/lessons/round-31.md` | gate-keeper | 4/4 | Q-31-1..4 | `reports/round-31/validation.json` (`acceptance_checks_passed: true`, 2026-10-19T00:28:05Z) | bytes=16637 lines=73 sha8=8870bbdd |
| `corpus/lessons/round-32.md` | gate-keeper | 4/4 | Q-32-1..6 | `reports/round-32/validation.json` (`acceptance_checks_passed: true`, 2026-10-19T00:59:27Z) | bytes=12879 lines=66 sha8=8aacfc2b |
| `corpus/lessons/round-49.md` | gate-keeper | 4/4 | none (frontier bullets carry no Q ids) | `reports/round-49/validation.json` | bytes=39223 lines=317 sha8=51ab6a5c |
| `corpus/lessons/round-49-verifier-spotcheck.md` | plain | 0/4 | none (the adjudication names no open item id) | `corpus/lessons/round-49.md` (outside-review record) | bytes=1880 lines=17 sha8=b1169c50 |
| `corpus/lessons/round-50.md` | gate-keeper | 4/4 | none (no Q ids) | `reports/round-50/claims.json` | bytes=24235 lines=151 sha8=c421b84c |
| `corpus/lessons/round-50-verifier-spotcheck.md` | plain | 0/4 | none (no new Q ids) | non-author closure record; fleet MANIFEST kotodama r50 | bytes=7670 lines=102 sha8=db6d4725 |

**Rows: 37. Files: 37.** The count is the runner's own partition glob
(`corpus/lessons/*.md`), which includes **this README** and the round-25
lesson that landed while this index was being written. Seven rows were added
by the round-33 revision-3 reconciliation for the lessons of rounds 26–32
(measured 2026-10-19T03:58Z; see the revision-3 block at the foot of this
file). Round 5 contributes two
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
   `spot-check` sentence, plus the four contract lines. **21 files.**
   Sub-shape: rounds 19–20 carry the older three-candidate marker vocabulary;
   rounds 21–23 carry the newer `### Rule` + per-axis-section shape with no
   marker vocabulary; rounds 26–28 carry that newer shape too, and rounds
   29–32 carry `### Rule` plus per-axis sections at `## <axis> —` level. All
   are counted as gate-keeper; a round-21/22/23 lesson is the current norm,
   not a contract regression.
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
**0/4** (pre-contract seeds). Of the loop-era files, **rounds 17–23 and 26–28
and 31–32 carry 4/4** and the rest — rounds 5 (both), 6, 7, 8, 9, 10, 11, 12,
14, 15, 29, 30 and the supplement — carry **3/4**: each has `source:`,
`verified-at:` and `recheck:` but no `scope:` line, except rounds 16, 29 and
30, which carry `source:`, `verified-at:` and `scope:` but **no `recheck:`**.
Histogram arithmetic: gate-keeper **21** = the 14 rows of revision 1 plus the
lessons of rounds 26–32; fragment-index **5** = rounds 8–12; plain **7** =
rounds 1–4, 7, 16 and this README. Total 33 = the runner's file set
(2026-10-19). Round 16 is the outlier: `source:`, `verified-at:` and
`scope:` but **no `recheck:`** (3/4, and no `## Gate`), and rounds 29–30 join
it in the 3/4-without-`recheck:` class. This is the state the
round-20 X24, round-23 X09 and round-33 revision-3 measurements recorded.

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

| Q-26-1 | the ledger auditors (`X63`, `C31`) must be re-run against the settled round-26 bytes; this lesson's own write moved them | `reports/round-26/audit/x63-lessons-audit.py` | open at filing (`corpus/lessons/round-26.md:196,206`); superseded in part by the round-31/32 readings (`corpus/lessons/round-31.md:53`, `round-32.md:45`) that count r26–r32 unindexed |
| Q-26-2 | the round-25 derivation-relations `SKILL.md` rule never landed, while round-26 D seats drafted a capability row and a rule row on top of it | `SKILL.md` | open at filing (`corpus/lessons/round-26.md:216-218`); the lesson records the D scribe's reading, not its own re-measurement |
| Q-27-1 | the law has no teeth: a tampered law value is not a finding in any delivered gate (`L6b-HOLD`), and five of six `RLAW-*` rules have no executable owner | `tools/gates/register-law-gate.py` | partially closed by round 28 — the vocabulary leg landed and `L6b-HOLD` was closed at that round's final tree (`corpus/lessons/round-28.md:50`); the meaning leg stays open (`round-28.md:94,126`) |
| Q-27-2 | the syllabify acceptance surface: the delivered gate reads 6/8 on the packet's own declared `syllables:` witness and 1 head2 disagreement of 62 remains; the runner's `disagreements 0` is a self-comparison | `examples/culture-d4/packet.d4.yml` | open at filing (`corpus/lessons/round-27.md:17,88,194`) |
| Q-27-3 | the declared v3 baseline path `reports/round-27/handoff/declared-in-r5/expected.json` was declared and never delivered (the runner's `missing_dependencies`) | `reports/round-27` | open at filing; the round-27 v3 baseline landed at `reports/round-27/pinsweep/v3-baseline-r27/expected.json` (`corpus/lessons/round-27.md:123,165`) |
| Q-27-4 | the round-27 runner's control defects (list-vs-string `SYLLABLE_CONTROLS`, null battery parse, shared diphthong bug, expectations moved onto the artifact) must be fixed before its D verdict can be trusted | `reports/round-27/run-validation.py` | open at filing (`corpus/lessons/round-27.md:141,194`) |
| Q-28-1 | the lessons ledger was off the acceptance surface for two rounds (`grep -c "corpus/lessons"` reads 0 in the round-27 and round-28 runners): put it back on an acceptance surface or explicitly retire it | `parent` | open at filing (`corpus/lessons/round-28.md:86,126,139`) |
| Q-28-2 | the register-law leg refuses out-of-vocabulary forces but not meaning-inverting ones (four semantic tampers silent) | `tools/gates/register-law-gate.py` | open at filing (`corpus/lessons/round-28.md:50,94,96,126`) |
| Q-28-3 | `L9-HOLD`/`L10-HOLD`: the assembler declares `register_law` in neither `PACKET_KEYS` nor `RECORD_FIELDS`, and the law's five `force` values have no declared vocabulary to check against | `tools/assemble-culture-d4.py` | open at filing; `x59` explicitly declines to fold `L9` into the closed RL-4 gap (`corpus/lessons/round-28.md:50,96,126`) |
| Q-28-4 | the round-26 revision's `round-26.md` pin is stale (`bytes=46745 lines=190 sha8=cf7461fe` against live `60054/222/cae06660`): re-pin as a new row, never an edit | `reports/round-26/zzz-lessons-index-revision-3.md` | open at filing (`X57-B2`/`G2`, `corpus/lessons/round-28.md:88`) |
| Q-28-5 | the `handoff-v3` exit-code divergence (the runner's regression run reads exit 2, this seat's own run exit 0) is unresolved by the lesson and reported as such | `parent` | open at filing (`corpus/lessons/round-28.md:132`) |
| Q-29-1 | `C` remains incomplete: the six-versus-four clean-law calibration is unresolved | `reports/round-29` | open at filing (`corpus/lessons/round-29.md:102,110`); the filed receipt's later `acceptance_checks_passed: true` does not answer the calibration question |
| Q-29-2 | provider worker launches are unobservable and the visible recount set does not establish every R25–R28 counting command | `parent` | open at filing (`corpus/lessons/round-29.md:110`) |
| Q-29-3 | the source-sweep evidence defect is preserved (4 quoted sweeps did not reproduce: one authoring defect, three later landings) and the older R21 `typed-labels.d4.yml` boundary finding is not closed by the scoped adjacency pass | `reports/round-28/audit/x63-entry-source-resolvability.py` | open at filing (`corpus/lessons/round-29.md:99,107`) |
| Q-30-1 | prospective freshness measurement contract and threshold remain operator-owned; a recommendation is not adoption — retain the historical rejections and the pause | `operator` | open at filing (`corpus/lessons/round-30.md:103,173`) |
| Q-30-2 | lesson-index coverage: a new lesson changes the partition; do not amend filed indices — explicitly disposition the live-ledger coverage if it remains outside acceptance | `parent` | open at filing (`corpus/lessons/round-30.md:104,173`); carried into Q-31-3 and Q-32-5 |
| Q-30-3 | semantic ceiling: named-ID speaker resolution and vocabulary/stem checks leave the controlled residues; a bounded round-30 repair must not be described as complete enforcement | `tools/gates/` (the lesson's own label: gate owner) | open at filing (`corpus/lessons/round-30.md:105,173`) |
| Q-30-4 | telemetry owners: choose or reconcile the canonical contract, re-run its consumers and negative controls, and disposition the incompatible reader rather than letting one green stand for both | `reports/round-30/telemetry` | resolved in the same file's dated recheck (distinct telemetry paths; 11/11 negative controls, `corpus/lessons/round-30.md:138,173`) |
| Q-30-5 | bind the R27 late-sweep number to its actual artifact: the C11 prose reads 41 findings while the receipt reads `exit 1 / findings 31 / surfaces 117` — preserve the discrepancy, do not present 41 as that JSON's reproduced count | `reports/round-29/recount/r27-full-sweep-reproduction.json` | closed as a current-retrospective attribution defect in the same file's dated recheck (`corpus/lessons/round-30.md:142,146,173`); the historical prose/receipt disagreement remains |
| Q-31-1 | D landing anchor: apply the AGENTS.md bullet after line 31 (end of the wrapped final telemetry bullet), not "after :30" | `AGENTS.md` | closed by round 32 — the hunk landed after old line 31, rule at `AGENTS.md:32-39` (`corpus/lessons/round-31.md:57`, `round-32.md:31`) |
| Q-31-2 | the sweep denominator: `final-sweep.md` must name its own capability denominator and relate it to both measured bounds (SCORECARD table 9 rows, newest round 5; live surface 121/40/10) | `reports/round-32/final-sweep.md` | narrowed at filing — the sweep does name its denominator (50 green-surface rows + 13 expected-red controls); what remains is that the manifest derive from the SCORECARD surface (`corpus/lessons/round-31.md:58,68`) |
| Q-31-3 | lesson indexing: six lessons (r26–r30 and r31) sat outside the README index; add rows as new parent-owned rows | `parent` | carried into Q-32-5 and this round's claim O (`corpus/lessons/round-31.md:53,59`) |
| Q-31-4 | the closure ledger's evidence commands are fleet-root-relative by the runner's own design; a lane-root re-execution cannot falsify a ledger row | `reports/round-31` | carried into Q-32-6 (`corpus/lessons/round-31.md:30,60`, `round-32.md:25`) |
| Q-32-1 | falsifier disposition (F-X16-3): the recorded falsification condition (i) has fired instrumentally — re-key the `SKILL.md:715` audit to the landed snapshot convention or reword the clause | `SKILL.md` | open at filing (`corpus/lessons/round-32.md:55`) |
| Q-32-2 | AGENTS residue (F-X16-1): excise `AGENTS.md:40-42` as a logged change; the bytes are `draft.md:35,37` residue, not rules | `AGENTS.md` | open at filing (`corpus/lessons/round-32.md:56`) |
| Q-32-3 | checklist position (F-X16-2): the executable item at `SKILL.md:713-715` sits outside `## Checklist` (`:522-534`); move it or cross-reference it | `SKILL.md` | open at filing (`corpus/lessons/round-32.md:57`) |
| Q-32-4 | draft-vs-landing (F-X16-4): the `patch-draft.md` erratum leg (the `SKILL.md:294`-class cell) never landed; disposition optional, record kept | `SKILL.md` | open at filing (`corpus/lessons/round-32.md:58`) |
| Q-32-5 | lesson indexing: Q-30-2/Q-31-3 carried — 7 unindexed lessons (r26–r32); add parent-owned rows using the §Ledger pins | `parent` | carried into this round's claim O (`corpus/lessons/round-32.md:59`) |
| Q-32-6 | inherited remainders: Q-31-2's narrowed remainder and Q-31-4's boundary transfer to this round's C/O reading; read the ledger's rows, not its verdict prose | `reports/round-32/run-validation.py` | open at filing (`corpus/lessons/round-32.md:60`) |

### Queue arithmetic

Measured 2026-10-18T17:4xZ by the §1 tool over the table above; re-run it
rather than inheriting these numbers.

- Rows: **78**. Of the 37 index rows, **30 carry at least one question**;
  the seven that carry none are `round-1-gates-and-triage.md` (its lessons
  were closed within round 1), `round-25.md` (this round's own claims are
  pending, not carried), `round-49.md`, `round-49-verifier-spotcheck.md`,
  `round-50.md`, `round-50-verifier-spotcheck.md` (no new Q ids), and this
  README's self-row.
- Owner classes: **path** (an in-repo surface that can close the item) — **59**;
  **role token** — **19** (`parent` 15, `operator` 4). No row has an empty or
  unresolvable owner; that is the C32 check. (Recounted 2026-10-19 by the §1
  tool's own `resolves()` over the 78 rows: 22 of the 29 round-33 additions
  resolve as paths, 7 as role tokens — `parent` 6, `operator` 1.)
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
  beside the 33 `*.md` lesson files, and the §2 rows cover only the `*.md`
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
- **Controls:** the tool's `--selftest` is 28/28 in-memory checks, including
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

Index revision 1 (2026-10-18, round 25); revision 2 appended below (round 25,
C35); revision 3 appended below (round 33, seat O02); revisions 4 and 5 below (rounds 49 and 50). Superseding edits land
as a new revision block here, never as an in-place rewrite of the per-round
rows' provenance claims.

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

## Revision 3 — round-33 reconciliation (2026-10-19)

Seat **O02** (round 33, claim O, `reports/round-33/op/O02-readme-delta.md`) read
the settled revision-2 bytes and drafted the reconciliation the round-32 lesson
routed as Q-30-2 / Q-31-3 / Q-32-5. Revision 1 (round 25) and revision 2
(round 25, C35) are filed bytes; their per-round rows' provenance claims and
their two stamps stand unedited. This block records what changed and why.

**What this revision adds.** Seven rows in §2 for the lessons that landed after
the round-25 stamp — rounds 26, 27, 28, 29, 30, 31, 32 — each with its
`format`, `contract`, open-questions, disposition-pointer and `pin` cells
re-measured from the live bytes at **2026-10-19T03:58Z** by
`reports/round-25/audit/c31-lessons-index-audit.py`'s own functions. Twenty-nine
rows in §4 for the open items those seven lessons name, each carrying its
lesson's own id where the lesson declared one (rounds 30–32) and a first-assigned
id where it did not (rounds 26–29, whose prose names the items without ids).

**Counting command, before and after.** Before this revision
`python3 -B reports/round-25/audit/c31-lessons-index-audit.py` exited **1** with
two findings: `C31-1 unindexed-file: ['round-26.md', 'round-27.md', 'round-28.md',
'round-29.md', 'round-30.md', 'round-31.md', 'round-32.md']` and
`C34-2 prose-arithmetic-drift: {'table_rows_vs_files': {'stated': [26, 26],
'measured': [26, 33]}}` (33 lesson files, 26 index rows, 49 queue rows,
`formats {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}`). After it, the
same command must exit **0** with `findings: 0` and the six checks PASS at
`index rows: 33  lesson files: 33  queue rows: 78`. The round-33 integrator runs
that command after applying this revision and files its output as the
operability receipt.

**In-place corrections, and why they are not provenance rewrites.** Four
machine- or reader-visible arithmetic statements were corrected in place because
a revision block cannot supersede them: §2's row/file count line (it read 26 and
26), §4's queue-arithmetic row count (it read 49) — the audit tool reads the
*first* queue-row count in the file and the *last* table count, so neither can be
superseded by an appended restatement — §3's histogram and contract-coverage
paragraph, and §1's three counting-command annotations. Revision 2 corrected the
round-4 row's disposition pointer in the same way and recorded it; the rule this
file states — per-round rows' provenance claims are never rewritten — is
honored: no `bytes`/`lines`/`sha8` cell of revisions 1–2 was touched, and the
seven new rows are new rows.

**Boundary.** This revision writes this file only. No `corpus/lessons/round-*.md`
byte, no filed round 1–32 artifact, no tool, gate, index, receipt or pin was
edited. Applied by the round-33 integrator; drafted, measured and controlled by
seat O02 under `reports/round-33/op/O02-readme-delta.md`, which also carries the
negative controls (a fake unindexed file must fail C31; a row naming a
nonexistent file must fail C31; a stated count that disagrees with the
measurement must fail C34b).

Superseding edits land as a new revision block here, never as an in-place
rewrite of the per-round rows' provenance claims.

## Revision 4 — round-49 lesson row (2026-10-19)

The round-49 integrator (kaika wave 2) landed `corpus/lessons/round-49.md`, the
first lesson file since round 32, because the fleet sources contract asks every
new `corpus/SOURCES.md` row for a round-lesson `## Gate` record. **What this
revision adds:** one §2 row for that lesson, pinned from the live bytes by
`reports/round-25/audit/c31-lessons-index-audit.py --json`
(`bytes=35993 lines=293 sha8=272eab2e`, format `gate-keeper`, contract 4/4).
**In-place correction:** §2's count line 33/33 → 34/34, the same machine-read
line revision 3 corrected. §3's histogram prose stays as the dated record it
is; the live histogram is now gate-keeper **22**, fragment-index **5**, plain
**7** (total 34). **Counting command:** before this revision the audit exited
with `C31-1 unindexed-file: ['round-49.md']` and `C34-2 prose-arithmetic-drift`
(stated 33/33, measured 33/34); after it, `findings: 0`. Rounds 33–48 still
have no lesson file — their scribe records live under
`reports/round-N/scribe/`; that convention gap is recorded in the round-49
lesson's `## Mistakes` and left for an owner decision, not settled here.

## Revision 5 — round-50 index rows and round-49 re-pin (2026-10-21)

Adds rows for the outside `round-49-verifier-spotcheck.md` and `round-50.md`.
The round-49 row's stale pin (`bytes=35993 lines=293 sha8=272eab2e`) is
replaced by its current bytes (`39223/317/51ab6a5c`); no round-49 lesson
bytes are edited. The round-50 pin is measured after its falsify-wave addendum.
The build seat's stored revision-5 diff had fixture pins and was not applied.
Counts and question-row prose above are reconciled to 36 files / 36 rows,
30 with Q ids / six without. Live histogram: gate-keeper 23,
fragment-index 5, plain 8 (total 36); earlier histogram prose is dated history.

The audit at base and at the build landing exits 1 with three findings:
C31-1 unindexed files, C34-1 round-49 pin drift, and C34-2 count drift.
Re-run `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` for
the current index verdict; `--selftest` exercises 28 controls.


## Revision 6 — non-author round-50 verifier index integration (2026-10-21)

Main added `round-50-verifier-spotcheck.md` as the outside closure record, not a
new lane-authored claim or promotion. Its measured pin is in the new §2 row.
Only that row and current machine-read count cells are changed; no filed lesson
bytes or prior per-round pins are rewritten. The question queue still has 78
rows and 30 indexed files carry a question; seven now carry none. Current
formats are gate-keeper 23, fragment-index 5 and plain 9 (37 files total).

This mechanically required index change prevents the integrator's own new
artifact from introducing an unindexed-file defect. The producer's revision-5
36/36 state above remains its dated history. The parent checked the actual
file/row bijection and new file pin independently; no sibling-owned gate or
selftest was executed for this integration.
