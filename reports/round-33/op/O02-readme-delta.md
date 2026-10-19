- Seat: O02 | executor | claim O | date 2026-10-19 | baseline 139e3b6

# O02 — `corpus/lessons/README.md` delta draft (claim O, lessons leg)

Mission: *"README delta draft: every prose-arithmetic correction the reconciled
README needs (26->33 counts, table row counts, stamp line) plus the new
open-question queue rows for r26-r32 lessons, written as exact before/after text
blocks for integrator application."*

This file is a **draft**. It edits nothing. The integrator applies the blocks
below to `corpus/lessons/README.md`; the seven lesson files of rounds 26–32 are
filed bytes and stay untouched. Dependency fragments `op/K02-lessons-census.md`
and `op/O01-row-drafts.md` were absent at this seat's run (see `## Owed`), so
every cell below was measured by this seat with the round-25 audit tool's own
functions rather than inherited.

## 1. Before state (measured 2026-10-19T03:52Z–03:59Z, baseline `139e3b6`)

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-25/audit/c31-lessons-index-audit.py
```

```
index present: True
lesson files:  33
index rows:    26
queue rows:    49
formats:       {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}
  FAIL C31_index_rows_eq_files
  PASS C32_owners_resolve
  PASS C33_formats_documented
  PASS C34_pins_rederived
  PASS C34c_shape_cells_rederived
  FAIL C34b_prose_arithmetic
findings:      2
  C31-1 unindexed-file: ['round-26.md', 'round-27.md', 'round-28.md', 'round-29.md', 'round-30.md', 'round-31.md', 'round-32.md']
  C34-2 prose-arithmetic-drift: {'table_rows_vs_files': {'stated': [26, 26], 'measured': [26, 33]}}
exit=1
```

`python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` →
`SELFTEST OK: 28/28 checks passed`, exit 0 (same stamp). The filed README's
sha256 at this stamp is
`ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c`, whose prefix
`ec7469dadf87df3e…` is the same digest the round-28 lesson recorded at its own
20:17Z stamp (`corpus/lessons/round-28.md:86`) — the index has not moved since
round 25, so this delta is measured against the revision-2 bytes the round-32
lesson routed as Q-30-2 / Q-31-3 / Q-32-5.

Per-file cells re-measured at the stamp (bytes / lines / sha8 / contract-lines):

| file | bytes | lines | sha8 | contract |
|---|---|---|---|---|
| `round-26.md` | 60054 | 222 | cae06660 | 4/4 |
| `round-27.md` | 54972 | 203 | f15e285b | 4/4 |
| `round-28.md` | 50419 | 145 | dd832ff7 | 4/4 |
| `round-29.md` | 17847 | 118 | b6765d33 | 3/4 (`source:`, `verified-at:`, `scope:`; no `recheck:`) |
| `round-30.md` | 30665 | 181 | 56e77835 | 3/4 (`source:`, `verified-at:`, `scope:`; no `recheck:`) |
| `round-31.md` | 16637 | 73 | 8870bbdd | 4/4 |
| `round-32.md` | 12879 | 66 | 8aacfc2b | 4/4 |

All seven classify `gate-keeper` under the tool's own classifier (each carries a
literal `## Gate` heading line; each carries `### Rule`). The round-32 lesson
measured six of these seven pins independently at 00:36Z
(`corpus/lessons/round-32.md:45`: round-26 `60054/222/cae06660`, round-27
`54972/203/f15e285b`, round-28 `50419/145/dd832ff7`, round-29 `17847/118/b6765d33`,
round-30 `30665/181/56e77835`, round-31 `16637/73/8870bbdd`) — same values,
different seat, different round: a cross-check, not an inheritance. This seat
adds round-32 `12879/66/8aacfc2b`.

## 2. The delta, as exact before → after blocks

Application order matters only for D5/D6 (both inside §4) and D2 (which must not
be preceded by any other table-count line). Each `before` block below was
asserted to occur **exactly once** in the live README before replacement
(8/8 assertions passed in this seat's scratch reconstruction; see §3).

### D1 — §2: seven new index rows (insert after the supplement row)

**Before**

```
| `corpus/lessons/supplement-opencode-1.md` | gate-keeper | 3/4 | Q-S1-1 | `reports/supplement-opencode-1` | bytes=5445 lines=89 sha8=f235fc0a |
```

**After**

```
| `corpus/lessons/supplement-opencode-1.md` | gate-keeper | 3/4 | Q-S1-1 | `reports/supplement-opencode-1` | bytes=5445 lines=89 sha8=f235fc0a |
| `corpus/lessons/round-26.md` | gate-keeper | 4/4 | Q-26-1, Q-26-2 | `reports/round-26/validation.json` (`acceptance_checks_passed: true`, 2026-10-18T19:09:32Z; the lesson's own closing read was `false` at 18:28:22Z, `corpus/lessons/round-26.md:178-186`) | bytes=60054 lines=222 sha8=cae06660 |
| `corpus/lessons/round-27.md` | gate-keeper | 4/4 | Q-27-1..4 | `reports/round-27/validation.json` (`acceptance_checks_passed: true`, 2026-10-18T20:08:49Z; the lesson read two earlier receipts `false` at 19:27:19Z / 19:28:22Z, `corpus/lessons/round-27.md:165-193`) | bytes=54972 lines=203 sha8=f15e285b |
| `corpus/lessons/round-28.md` | gate-keeper | 4/4 | Q-28-1..5 | `reports/round-28/validation.json` (`acceptance_checks_passed: true`, 2026-10-18T20:50:17Z) | bytes=50419 lines=145 sha8=dd832ff7 |
| `corpus/lessons/round-29.md` | gate-keeper | 3/4 | Q-29-1..3 | `reports/round-29/validation.json` (`acceptance_checks_passed: true`, 2026-10-18T21:50:07Z; the lesson's closing read had no receipt at 21:13:09Z, `corpus/lessons/round-29.md:110`) | bytes=17847 lines=118 sha8=b6765d33 |
| `corpus/lessons/round-30.md` | gate-keeper | 3/4 | Q-30-1..5 | `reports/round-30/validation.json` (`acceptance_checks_passed: true`, 2026-10-18T22:32:36Z) | bytes=30665 lines=181 sha8=56e77835 |
| `corpus/lessons/round-31.md` | gate-keeper | 4/4 | Q-31-1..4 | `reports/round-31/validation.json` (`acceptance_checks_passed: true`, 2026-10-19T00:28:05Z) | bytes=16637 lines=73 sha8=8870bbdd |
| `corpus/lessons/round-32.md` | gate-keeper | 4/4 | Q-32-1..6 | `reports/round-32/validation.json` (`acceptance_checks_passed: true`, 2026-10-19T00:59:27Z) | bytes=12879 lines=66 sha8=8aacfc2b |
```

Row-format parity with the filed rows: six pipe-separated cells, first column the
backticked repo-relative path, `format` in column 2 and `contract` in column 3
(the two cells C34c re-derives), and the pin cells in the last column in the
filed `bytes=… lines=… sha8=…` order. `Q-27-1..4` / `Q-28-1..5` / `Q-29-1..3` /
`Q-30-1..5` / `Q-31-1..4` / `Q-32-1..6` use the same range shorthand the filed
rows use (`Q-11-1..3`, `Q-18-1..3`).

Disposition-pointer note for the reviewer: the `acceptance_checks_passed: true`
values above are **filed receipt field values**, read at this stamp from
`reports/round-25..32/validation.json` with
`python3 -c "import json;d=json.load(open(<path>));print(d['acceptance_checks_passed'],d['measured_at_utc'],d['runner_sha256'][:8])"`,
not verdicts granted here. Where the lesson's own closing read differed, the cell
records both rather than only the later value — round 26 `true` at
`2026-10-18T19:09:32Z` / runner `73297683` against the lesson's `false` at
18:28:22Z; round 27 `true` at `20:08:49Z` / runner `36b59706` against the two
`false` receipts the lesson read; round 28 `true` at `20:50:17Z` / runner
`20e09ea8`; round 29 `true` at `21:50:07Z` / runner `59df391b`; round 30 `true`
at `22:32:36Z` / runner `2f447223`; round 31 `true` at `2026-10-19T00:28:05Z` /
runner `9e01c427`; round 32 `true` at `00:59:27Z` / runner `6fd1b96e`.

### D2 — §2: table arithmetic line and its explanatory paragraph

**Before**

```
**Rows: 26. Files: 26.** The count is the runner's own partition glob
(`corpus/lessons/*.md`), which includes **this README** and the round-25
lesson that landed while this index was being written.
```

**After**

```
**Rows: 33. Files: 33.** The count is the runner's own partition glob
(`corpus/lessons/*.md`), which includes **this README** and the round-25
lesson that landed while this index was being written. Seven rows were added
by the round-33 revision-3 reconciliation for the lessons of rounds 26–32
(measured 2026-10-19T03:58Z; see the revision-3 block at the foot of this
file).
```

The rest of that paragraph ("Round 5 contributes two rows on purpose … if a
lesson lands it adds a row") stands unchanged and is still true.

### D3 — §1: the three counting-command annotations (three single-line replacements)

**Before** — pair 1

```
audit.py --selftest  # 26/26, exit 0
```

**After** — pair 1

```
audit.py --selftest  # 28/28, exit 0
```

**Before** — pair 2

```
ls corpus/lessons/*.md | wc -l                                          # 26 (2026-10-18)
```

**After** — pair 2

```
ls corpus/lessons/*.md | wc -l                                          # 33 (2026-10-19)
```

**Before** — pair 3

```
find corpus/lessons -maxdepth 1 -name '*.md' | wc -l                    # 26 (same set)
```

**After** — pair 3

```
find corpus/lessons -maxdepth 1 -name '*.md' | wc -l                    # 33 (same set)
```

The `# 26/26, exit 0` annotation was already wrong before this round: the tool's
`--selftest` prints `SELFTEST OK: 28/28 checks passed` (measured at this stamp,
exit 0), and §1's own prose four lines below says "`--selftest` is 28 in-memory
controls". D3a removes that contradiction; D3b/D3c move the partition count.

### D4 — §3: histogram, sub-shapes, contract coverage

**Before**

```
   `spot-check` sentence, plus the four contract lines. **14 files.**
   Sub-shape: rounds 19–20 carry the older three-candidate marker vocabulary;
   rounds 21–23 carry the newer `### Rule` + per-axis-section shape with no
   marker vocabulary. Both are counted as gate-keeper; a round-21/22/23 lesson
   is the current norm, not a contract regression.
```

**After**

```
   `spot-check` sentence, plus the four contract lines. **21 files.**
   Sub-shape: rounds 19–20 carry the older three-candidate marker vocabulary;
   rounds 21–23 carry the newer `### Rule` + per-axis-section shape with no
   marker vocabulary; rounds 26–28 carry that newer shape too, and rounds
   29–32 carry `### Rule` plus per-axis sections at `## <axis> —` level. All
   are counted as gate-keeper; a round-21/22/23 lesson is the current norm,
   not a contract regression.
```

**Before**

```
Contract-line coverage tracks the round, not the format: rounds 1–4 carry
**0/4** (pre-contract seeds). Of the loop-era files, **rounds 17–23 carry 4/4**
and the rest — rounds 5 (both), 6, 7, 8, 9, 10, 11, 12, 14, 15 and the
supplement — carry **3/4**: each has `source:`, `verified-at:` and `recheck:`
but no `scope:` line. Histogram arithmetic: gate-keeper **14** = the 13 filed
plus the round-25 lesson; fragment-index **5** = rounds 8–12; plain **7** =
rounds 1–4, 7, 16 and this README. Total 26 = the runner's file set. Round 16 is the outlier: `source:`, `verified-at:` and
`scope:` but **no `recheck:`** (3/4, and no `## Gate`). This is the state the
round-20 X24 and round-23 X09 audits recorded, unchanged.
```

**After**

```
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
```

Both histogram counts and the 4/4-vs-3/4 split are the tool's own
`census()`/`contract_lines()` output at this stamp (§1 table), not a reading of
the prose.

### D5 — §4: twenty-nine new open-question queue rows (insert immediately before `### Queue arithmetic`)

**Before**

```
### Queue arithmetic
```

**After** — the same heading, preceded by these rows (the block is inserted, the
heading is not modified):

```
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
```

Provenance of the ids, stated because it differs by round: **rounds 30, 31 and 32
name their own ids** (`Q-30-1..5`, `Q-31-1..4`, `Q-32-1..6`) and those rows quote
the lesson's own id, question and owner label — `Q-30-4` and `Q-30-5` carry the
status the same file's later dated sections give them
(`corpus/lessons/round-30.md:173`). **Rounds 26, 27, 28 and 29 name their open
items in prose without ids**; their rows are first-assigned ids with the lesson's
own wording condensed and the source line cited in the status cell. Every row is
traceable to a lesson line; no row's owner is invented — each owner cell was
checked by the audit tool's own `resolves()` (see §3), and where the lesson's
label is not a resolvable token (`Q-30-3`'s "gate owner") the label is preserved
in the question and the mapped owner is named as this seat's mapping.

Two rows deliberately carry **closed** statuses rather than "open", because the
lesson that filed them also closed them: `Q-30-4` and `Q-30-5`
(`corpus/lessons/round-30.md:138,146,173`) and `Q-31-1`
(`corpus/lessons/round-32.md:31`). The README's §4 rule is that anything a
lesson names as *open* must appear with an owner; a closed item is indexed with
its closure pointer so the queue's arithmetic and the lesson's prose agree. The
round-26 and round-27 lessons' own "closeout" sections are not queue rows here:
they are admission conditions addressed to the parent, not open questions.

### D6 — §4: queue arithmetic

**Before**

```
- Rows: **49**. Of the 26 index rows, **23 carry at least one question**;
  the three that carry none are `round-1-gates-and-triage.md` (its lessons
  were closed within round 1), `round-25.md` (this round's own claims are
  pending, not carried) and this README's self-row.
- Owner classes: **path** (an in-repo surface that can close the item) — **37**;
  **role token** — **12** (`parent` 9, `operator` 3). No row has an empty or
  unresolvable owner; that is the C32 check.
```

**After**

```
- Rows: **78**. Of the 33 index rows, **30 carry at least one question**;
  the three that carry none are `round-1-gates-and-triage.md` (its lessons
  were closed within round 1), `round-25.md` (this round's own claims are
  pending, not carried) and this README's self-row.
- Owner classes: **path** (an in-repo surface that can close the item) — **59**;
  **role token** — **19** (`parent` 15, `operator` 4). No row has an empty or
  unresolvable owner; that is the C32 check. (Recounted 2026-10-19 by the §1
  tool's own `resolves()` over the 78 rows: 22 of the 29 round-33 additions
  resolve as paths, 7 as role tokens — `parent` 6, `operator` 1.)
```

Arithmetic: 49 + 29 = 78 rows; 37 + 22 = 59 paths; 12 + 7 = 19 role tokens
(`parent` 9 + 6 = 15, `operator` 3 + 1 = 4); index rows carrying at least one
question 23 + 7 = 30 (all seven new lessons carry at least one row).

### D7 — §5: the subdirectory paragraph's file count

**Before**

```
`corpus/lessons/` carries 146 files under nine directories
  beside the 26 `*.md` lesson files
```

**After**

```
`corpus/lessons/` carries 146 files under nine directories
  beside the 33 `*.md` lesson files
```

Re-measured at this stamp: `find corpus/lessons -mindepth 2 -type f | wc -l` →
146; `find corpus/lessons -mindepth 1 -maxdepth 1 -type d | wc -l` → 9;
per-directory counts unchanged from the filed table (42/43/1/16/2/10/12/5/15).
The nine-directory table itself needs no edit.

### D8 — new revision-3 block appended at EOF

Append exactly this block at the end of the file (after the revision-2 block):

```

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
```

Note the wording of the two quoted `C31-1` / `C34-2` findings: the phrase
`stated: [26, 26]` inside the block is **not** the literal `**Rows: 26. Files:
26.**` pattern, deliberately — see §3's trap (d).

### D9 (recommended, verified green) — the stamp line

**Before**

```
Index revision 1 (2026-10-18, round 25). Superseding edits land as a new
revision block here, never as an in-place rewrite of the per-round rows'
provenance claims.
```

**After**

```
Index revision 1 (2026-10-18, round 25); revision 2 appended below (round 25,
C35); revision 3 appended below (round 33, seat O02). Superseding edits land
as a new revision block here, never as an in-place rewrite of the per-round
rows' provenance claims.
```

### D10 — §6 boundary record: the selftest count (required; R02's F-R02-9)

**Before**

```
- **Controls:** the tool's `--selftest` is 26/26 in-memory checks, including
```

**After**

```
- **Controls:** the tool's `--selftest` is 28/28 in-memory checks, including
```

The same pre-existing defect as D3a, one screen further down: the live tool's
`--selftest` prints `SELFTEST OK: 28/28 checks passed` (measured this stamp, exit
0), while §1 (`:55`) and the revision-2 block (`:338`) both say 28 — so `:285` is
the third leg of a self-contradiction the round-25 tool cannot see (its C34b
reads only two surfaces). R02's §F-R02-9 lists it; this delta fixes it rather
than declining it.

### D0 — the header parenthetical (required)

The header's "(26 at the final stamp …)" is a revision-1 statement, and the
revision-3 block supersedes it; a reader who stops at line 6 can still misread
it as current. R02's checker lists `:6` among the tool-blind stale-count lines,
so this block is part of the required set (measured green as part of the full set
in §3):

**Before**

```
that index: one row per file the runner's partition glob returns (26 at the
final stamp — the 24 filed lessons, the round-25 lesson that landed mid-audit,
and this file itself), the open-question queue with an owner per item, and the
three formats documented.
```

**After**

```
that index: one row per file the runner's partition glob returns (26 at the
revision-1 stamp — the 24 filed lessons, the round-25 lesson that landed
mid-audit, and this file itself; **33 at the revision-3 stamp of 2026-10-19**,
see the revision-3 block at the foot of this file), the open-question queue
with an owner per item, and the three formats documented.
```

## 3. Verification performed on the proposed bytes (scratch, read-only w.r.t. the repo)

**Self-sufficiency check (this is the check that matters).** The blocks in §2
were parsed back out of *this file* — **13 before/after pairs** (D0, D1, D2,
D3×3, D4×2, D5, D6, D7, D9, D10) **plus the D8 append block** — applied to the
live README in that order with every `before` asserted to occur exactly once,
and the result run through **two independent instruments**: the round-25 audit
module's own `run_checks()` (module `INDEX` patched to the reconstructed bytes)
and R02's §4 parity checker, extracted verbatim from
`reports/round-33/review/R02-op-review.md` into `.scratch/r02-parity.py`. So the
digests below are digests of bytes an integrator reproduces **from this
fragment**, not from a private scratch file:

```
index present: True
lesson files:  33
index rows:    33
queue rows:    78
formats:       {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}
  PASS C31_index_rows_eq_files
  PASS C32_owners_resolve
  PASS C33_formats_documented
  PASS C34_pins_rederived
  PASS C34c_shape_cells_rederived
  PASS C34b_prose_arithmetic
findings:      0
exit=0
```

R02's checker on the same bytes (`python3 -B .scratch/r02-parity.py
<reconstructed>`): `index rows=33 files=33 queue=78 / FAILS=0 / WARNS=0` — its
`P4` (all three pin tokens present per row), `P8` (exactly 4 cells per queue row)
and `P10` (`[33, 33]`) legs included, none of which the filed tool checks. On the
live README the same checker reads `FAILS=2` (`P1 unindexed-file` = the seven,
`P10 table prose [26, 26] != measured [26, 33]`) — the same two defects the filed
tool reports, so the checker is calibrated in both directions.

Digests, all measured 2026-10-19:

| variant | bytes | lines | sha256 | instruments |
|---|---|---|---|---|
| live README (before, revision 1/2) | 29 059 | 346 | `ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c` | filed tool exit 1, `C31-1` + `C34-2`; R02 checker `FAILS=2` |
| **FULL = D0–D10** (the required set) | 43 454 | 448 | `f752e1d79ae627a0d9728fe16fd1532e7cb9e587f6ac7025a880d8af46233868` | filed tool exit 0, findings 0; R02 checker `FAILS=0 WARNS=0` |

The reconstruction also ran the pair-application as a control in its own right:
the first pass **failed** on D2 because the fragment's D2 `before` block ends at
`…was being written.` while the live line continues ` Round 5 contributes two` —
a reminder that these blocks are substrings, not whole lines, and that the
`before`/`after` blocks must be applied as given rather than re-wrapped.

Control battery — each mutation applied to the proposed bytes and re-run through
the tool's own `run_checks()`; the expected check must go red:

| control | mutation | measured |
|---|---|---|
| c1 | delete the round-27 row | `C31_index_rows_eq_files` FAIL, `C31-1 unindexed-file: ['round-27.md']`; `C34b` also FAILs (stated 33 rows vs measured 32) |
| c2 | add a row for `round-99.md` (nonexistent) | `C31` FAIL, `C31-2 ghost-row: ['round-99.md']` |
| c3 | table line says `Files: 32` | `C34b` FAIL, `C34-2 table_rows_vs_files {stated: [33, 32], measured: [33, 33]}` |
| c3b | queue arithmetic says 77 | `C34b` FAIL, `C34-2 queue_rows {stated: 77, measured: 78}` |
| c4 | round-27 pin reverted to the stale `46745/190/cf7461fe` | `C34` FAIL, `C34-1 pin-drift` |
| c5 | `Q-28-1` owner changed to `no-such-owner.md` | `C32` FAIL, `C32-1 unresolvable-owner` |
| c6 | round-29 contract cell changed 3/4 → 4/4 | `C34c` FAIL, `C34-3 shape-cell-drift` |
| d9 | D9 applied alone | all six PASS, findings 0, exit 0 |
| d0+d9 | D0 and D9 applied together | all six PASS, findings 0, exit 0 |

Three traps this battery and the reconstruction caught, filed because the
integrator will meet them:

**(a) The tool reads the *first* queue count and the *last* table count.**
`run_checks()` compares `stated["queue"][0]` (first `Rows: **N**` match) and
`stated["table"]` (last `**Rows: N. Files: N.**` match). A corrected restatement
appended in a revision block therefore cannot fix §4's line, and a revision block
that *quotes* the old table line re-breaks C34b. D6 must be applied in place.

**(b) An added queue row changes the §4 arithmetic, and a row's removal changes
both C31 and C34b** (c1 above) — the two checks are coupled through the stated
counts, so a partial application (rows without D2/D6) leaves the tool red. Apply
D1+D2 and D5+D6 as pairs.

**(c) A quoted `**Rows: 26. Files: 26.**` anywhere in the file — including inside
this round's own new revision block — re-trips C34b.** This seat's first draft
failed exactly this way (last-match semantics), which is why D8's prose says "it
read 26 and 26" instead of quoting the pattern.

## 4. Application recipe (for the integrator)

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
# 1. apply D0..D10 (all required) to corpus/lessons/README.md, by content match
#    (never by line number — see §6f). Expected result: 43 454 bytes, 448 lines,
#    sha256 f752e1d79ae627a0d9728fe16fd1532e7cb9e587f6ac7025a880d8af46233868
#    for the 29-row queue set; a different queue set changes only D5/D6.
# 2. count the pinned state:
python3 -B reports/round-25/audit/c31-lessons-index-audit.py            # expect: 33/33/78, findings 0, exit 0
python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest # expect: SELFTEST OK: 28/28, exit 0
python3 -B reports/round-25/audit/c31-lessons-index-audit.py --json     # the receipt to file with the round
# 3. second instrument (extract §4's python block from review/R02-op-review.md):
python3 -B .scratch/r02-parity.py corpus/lessons/README.md              # expect: FAILS=0 WARNS=0
```

Claim O's counting command also requires
`test -s reports/round-33/op/O05-falsifier-disposition.md`, which is seat O05's
artifact, not this seat's.

## 5. Limits and honest caveats

- **Row cells bind to the stamp.** `bytes`/`lines`/`sha8` for the seven files are
  live measurements at 2026-10-19T03:58Z and are stable only while no further
  `corpus/lessons/*.md` write lands. A lesson landing after that stamp adds a row
  (and moves the partition to 34) rather than changing these.
- **The `round-26.md` file is itself a live-wave surface.** The round-26 lesson's
  own §"Writing this file moved the C-claim auditors" records that its write
  moved `X63` and `C31` readings (`corpus/lessons/round-26.md:196`); the pin
  above is a measurement of the settled bytes, not a claim that earlier readings
  were wrong.
- **The queue rows for rounds 26–29 are an extraction, not a machine
  enumeration** — the same limit §4 of the README names. This seat read each new
  lesson's open-item prose (rounds 26–29: `## Closeout` / `## Status at the
  closing stamp` sections; rounds 30–32: `## Open routes` blocks) and cites a
  line for each row. A reviewer who finds an open item this extraction missed
  should file it as a new row — never as an edit of a filed lesson.
- **`Q-30-3`'s owner mapping is this seat's.** The lesson's label is "gate owner"
  (`corpus/lessons/round-30.md:105`), which is not a token the C32 check
  resolves; the row preserves the label in the question and maps the owner to the
  live `tools/gates/` directory. If the intended owner is a specific gate, the
  integrator should repoint the cell (a cell edit in a new revision, not a
  rewrite of the row's question).
- **No filed byte was edited by this seat.** Writes: this file, and the scratch
  reconstruction under `.scratch/o02/` (gitignored) plus R02's checker extracted
  verbatim from its fragment into `.scratch/r02-parity.py`. No
  `corpus/lessons/**` byte, no round-1..32 artifact, no tool, gate, receipt or pin
  was touched; no commit, no push. The scratch directory is transient, so §2–§4
  carry everything the integrator needs to reproduce the verified bytes.

## 6. Cross-fragment reconciliation (K02, O01, O03, O04, O06, O07 and R02 landed after this seat's run)

This seat's `op/` read was empty; the sibling fragments and
`review/R02-op-review.md` landed later in the same wave. Reconciliations, and
the collision the integrator must decide:

**(a) The seven rows: D1 and `op/O01-row-drafts.md` §2 are alternatives, not
complements.** Both sets are parity-correct and both are machine-green — O01's
rows re-graded by R02 with the filed tool (R02 §2, preview V1: 33/33, all six
checks PASS), D1's rows re-graded here (§3). Applying both would duplicate seven
rows and trip `C31-3 duplicate-row`, so the integrator applies exactly one. They
differ in two places: the **insertion point** (O01 anchors after the `round-25.md`
row at `:94`; D1 anchors after the supplement row, the last table row — both keep
the table contiguous) and the **open-questions cells** (O01's r26–r29 cells say
"— (no new ids …)"; D1's name Q-26-1..Q-29-3, the ids this file's D5 defines).
The §2 column and §4 rows must describe the same set: applying O01's rows with
this file's D5 leaves the column and the queue disagreeing, which no check
catches. R02's F-R02-1 remedy ("the delta must carry `:207`, with the number
equal to the queue-row count actually applied") is satisfied by D6 only for the
29-row set.

**(b) The queue set: three proposals, three arithmetics.** K02 §5/§7 computes
**13** live ids (Q-30-1..3, Q-31-1..4, Q-32-1..6) → `49 + 13 = 62`; O01 §5
computes **15** (`Q-30-1..5` carried) → 64; this file's D5 computes **29** (adding
first-assigned ids for the items rounds 26–29 name in prose) → 78. Each is
internally consistent; the deciding criterion is §4's own rule ("anything a
lesson names as *open* must appear above with an owner, and anything above must
be traceable to a lesson file"), and it is the parent's call. R02's F-R02-2
measured that rounds 26–29 declare no ids (`grep -o 'Q-2[6-9]-[0-9]*'` → zero
hits) and left the id-set choice open. **Whichever set is applied, D6's number
must equal the applied row count** — R02's §2 previews measured exactly this
failure mode (V2: 15 rows with `:207` left at 49 → `C34b` red; V3: `:207` → 64 →
green).

**(c) Closed-at-source ids carry their closure pointer.** R02's F-R02-2 asks that
a cell citing a closed id say so; D5 does it for `Q-30-4` (`round-30.md:138,173`),
`Q-30-5` (`:146,173`) and `Q-31-1` (`round-32.md:31`).

**(d) Disposition-pointer form follows O01** — the modal filed form, 11 of the 26
existing rows name a `reports/round-N/validation.json` (R02 §3 F-R02-8). D1 names
that path plus the receipt's own `acceptance_checks_passed` / `measured_at_utc` /
`runner_sha256` fields; K02's alternative pointers (`routed-resolution.json`,
`closure-ledger.json`, `completion-ledger.json`) all exist and can be appended in
the same cell without disturbing any check.

**(e) R02 §F-R02-9's tool-blind line inventory — disposition per line.**

| line (pre-edit) | disposition |
|---|---|
| `:6` | fixed by D0 |
| `:35` | fixed by D3a |
| `:39`, `:40` | fixed by D3b / D3c |
| `:97` | fixed by D2 |
| `:140` | fixed by D4b |
| `:207` | fixed by D6 |
| `:256-257` | fixed by D7 |
| `:285` | fixed by D10 |
| `:325` | declined — re-measured this stamp: 146 files under nine directories, the sentence is correct |
| `:55`, `:338` | declined — already say 28, correct |
| `:22-29` (the `2026-10-18T17:35Z` re-derivation stamp sentence) | declined in place — it is a revision-1 provenance claim the file's own rule protects; D8's revision-3 block supplies the new stamp, which is the file's stated mechanism |

**(f) Application mechanics (R02's F-R02-6).** Apply every block by content
match, never by line number. Inserting the seven rows shifts later anchors by
+7 and D0 adds one line, so the post-edit anchors in the FULL reconstruction are:
`**Rows: 33. Files: 33.**` at `:105`, §3 heading at `:122`, §4 heading at `:161`,
the queue-arithmetic line at `:254`, the §6 controls line at `:334`, and the
revision-3 block from `:398` (file 448 lines).

**(g) Two supersessions the integrator should record, not discover.**
`reports/round-26/run-validation.py:97` pins `README_BASELINE_BLOB =
"a31870556c733498…"` and asserts the README's blob equals it (R02 §3 F-R02-5);
after this edit that filed runner would go red **if re-run**, which no round-33
counting command does — the honest handling is a declared supersession in the
round's LOG entry. And `op/O07-baseline-receipt.md` lists the README digest
`ec7469da…` under its digest pins: that list is an *expected-move* anchor, not an
invariance claim (claim O's whole point is that these bytes move); the invariance
surface is the four selftests O07 ran. The authority for the edit itself is
`reports/round-33/targets.json`'s `shared_rules` carve-out ("the lessons README
and SKILL.md changes are drafted by seats and applied by the integrator"), which
is what makes this a draft rather than a seat-side write.

**(h) What the machine legs do not certify (R02's F-R02-3).** `C32` inspects only
rows that exist, so a green `c31-lessons-index-audit.py` run certifies the
row/file set, the pins, the shape cells and the two prose counts — it does **not**
certify §4 coverage. This delta takes the **rows-added** option (not prose
pointers); the receipt (`O08`/`S01`) should say so and should not present
"findings: 0" as covering §4 traceability.

## Owed

- **Parent decision 1 — which row set lands** (§6a): this file's D1 or
  `op/O01-row-drafts.md` §2. Not both.
- **Parent decision 2 — which queue set lands** (§6b): K02's 13 → 62, O01's
  15 → 64, or this file's 29 → 78, with D6's number set to the applied count.
- **Integrator — post-apply re-run**: the filed tool (expect 33/33/78, findings
  0, exit 0 for the 29-row set) and R02's checker (expect `FAILS=0 WARNS=0`),
  both recorded in the round's receipt. R02's §4 checker is reproduced verbatim
  in its fragment; the copy this seat used is `.scratch/r02-parity.py`
  (transient).
- **`op/O06-controls.md` reconciliation** (R02 §6): if its expected C34b codes
  disagree with the measured first-match/last-match asymmetry in §3 trap (a),
  the defect is in O06, not in the tool.
- **The six dependency fragments are no longer absent** — K02, O01, O03, O04,
  O06 and O07 all landed after this seat's run. Cross-checked here: K02's §2
  table agrees with §1 on all 21 pin values, all 7 format cells and all 7
  contract cells; O01's row cells agree with §1 on the same 35 values (R02 §1
  reports the same four-way agreement for K02/O01/O04). Not read by this seat:
  `op/O03-owner-checks.md`, `op/O04-format-checks.md`, `op/O06-controls.md`,
  `op/O07-baseline-receipt.md` — their per-item verdicts are theirs to carry, and
  §3's own controls (c5 for owners, the classifier for formats, the battery for
  C34b) are this seat's independent cover for the rows this file adds.

## Citations

- `corpus/lessons/README.md:1-9, 31-60, 61-110, 111-142, 144-233, 255-277,
  303-305, 307-346` — the filed revision-1/2 bytes this delta edits (sha256
  `ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c`).
- `reports/round-25/audit/c31-lessons-index-audit.py:42-56, 72-116, 119-168,
  170-329` — the checks (C31/C32/C33/C34/C34b/C34c), the classifier, the
  contract-line scan, `resolves()` and the two arithmetic regexes this delta must
  satisfy.
- Command: `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` →
  `lesson files: 33 / index rows: 26 / queue rows: 49 / formats {'gate-keeper':
  21, 'fragment-index': 5, 'plain': 7}` + `C31-1` + `C34-2`, exit 1 (2026-10-19,
  this seat).
- Command: `python3 -B reports/round-25/audit/c31-lessons-index-audit.py
  --selftest` → `SELFTEST OK: 28/28 checks passed`, exit 0 (this seat).
- Command: `sha256sum corpus/lessons/README.md` → `ec7469dadf87df3e…` (this seat).
- Command: per-file `bytes/lines/sha8/contract` measurement over
  `corpus/lessons/round-26.md … round-32.md` (this seat; values in §1).
- Command: `find corpus/lessons -mindepth 2 -type f | wc -l` → 146;
  `find corpus/lessons -mindepth 1 -maxdepth 1 -type d | wc -l` → 9 (this seat).
- Command: per-round receipt read
  `python3 -c "import json;d=json.load(open('reports/round-<N>/validation.json'));print(d['acceptance_checks_passed'], d['measured_at_utc'], d['runner_sha256'][:8])"`
  for N in 26..32 (this seat; values in §D1).
- Command: scratch reconstruction + control battery via
  `importlib`-loaded `c31-lessons-index-audit.py` with `INDEX` patched to the
  proposed/mutated bytes (this seat; outputs in §3).
- `corpus/lessons/round-26.md:196, 206, 216-218` — the auditor re-run item and
  the unlanded SKILL rule.
- `corpus/lessons/round-27.md:17, 37, 88, 123, 141, 165, 194` — `L6b-HOLD`, the
  syllabify acceptance surface, the missing `declared-in-r5` dependency, the
  runner control defects.
- `corpus/lessons/round-28.md:50, 86, 88, 94, 96, 126, 132, 139` — the dropped
  ledger acceptance surface, the stale round-26 revision pin (`X57-B2`/`G2`),
  `L9-HOLD`/`L10-HOLD`, the meaning-leg residue, the `handoff-v3` divergence.
- `corpus/lessons/round-29.md:99, 102, 107, 110` — the source-sweep evidence
  defect, the six-versus-four calibration, the unobservable provider launches.
- `corpus/lessons/round-30.md:103, 104, 105, 115, 138, 142, 146, 173` —
  `Q-30-1..5` and their dated rechecks.
- `corpus/lessons/round-31.md:30, 47, 53, 57, 58, 59, 60, 68` — `Q-31-1..4` and
  `Q-31-2`'s narrowing.
- `corpus/lessons/round-32.md:25, 31, 45, 55, 56, 57, 58, 59, 60` — `Q-32-1..6`,
  the six pins re-measured by that seat, and the AGENTS anchor confirmation.
- `reports/round-33/claims.json` (claim O `after_required.a_lessons`) and
  `reports/round-33/targets.json` (seat O02's mission, `out`, `shared_rules`).
