- Seat: S01 | scribe | claim O | date 2026-10-19 | baseline 139e3b6

# S01 — final operability receipt (claim O), cut 2026-10-19T04:05Z (rev 5; earlier cuts 03:54Z, 03:58Z, 04:00Z, 04:02Z)

## 0. Status at this cut — read this first

**Claim O is not yet verified, but every fragment it depends on has landed and
been folded.** The falsifier leg's counting command passes (O05 landed with a
bounded fix draft + controls, re-executed by both R01 and R02); the lessons leg
is still red on live bytes because the README reconciliation is
integrator-applied. All three reviews (R01-R03) are folded in §5.

**Honesty declaration (R02-F3, `review/R02-op-review.md:136-147`).** The machine
legs certify the row/file set, the pins, the shape cells and the two prose
counts only — they cannot see whether §4's queue traceability rule
(`corpus/lessons/README.md:227-232`) is met for the new ids, and `C32` does not
fire on absent rows. "findings: 0" in this receipt is therefore **not**
presented as §4 coverage; the round must declare which option the integrator
took (queue rows added vs prose pointers) when the delta lands. Routed to
`cross/X04-honesty.md` as R02 directs.

| leg | state at this cut | evidence |
|---|---|---|
| lessons index reconciliation (O-a) | **not landed** — audit still red; three independent reachability proofs exist (O08 simulation, R03 fixture, R02 previews V1/V3) | §2.1 |
| falsifier mismatch (O-b) — location | **located**: F-X16-3, `corpus/lessons/round-32.md:41` (K01; confirmed by this seat, O05, R01 and R02) | §2.2 |
| falsifier mismatch (O-b) — disposition artifact | **landed 03:59Z** — `op/O05-falsifier-disposition.md`, `test -s` exit 0; bounded repoint draft + 7-scenario control set, re-executed by both R01 and R02 | §2.2 |
| regression baseline | **green**; O07 is the baseline of record, verified verbatim by R03 and re-run row-for-row by this seat | §3 |
| filed-byte integrity during the wave | **three** filed `validation.json` (r5/r6/r7) moved, then restored; all CLEAN vs HEAD at 04:02Z (R01-F1, HIGH) | §2.4 |
| R01 findings folded in | **folded 04:02Z** — nine findings accepted/errata, one HIGH | §5 |
| R02 findings folded in | **folded 04:05Z** — eleven findings accepted/errata; its tool-graded previews and the C34b parser asymmetry folded into §2.1 | §5 |
| R03 findings folded in | **folded** — O07 errata + control/validator constraints | §5 |

Revision history: the first cut (03:54Z) was written while every sibling
fragment directory was empty; rev 2 (03:58Z) folded K01, O07 and O08; rev 3
(04:00Z) folded O05 and R03; rev 4 (04:02Z) folded R01; rev 5 (this one, 04:05Z)
folds R02 — the last of the three review inputs.

Scope statement: this seat wrote exactly one file, this one. No filed round
1–32 byte, no `corpus/lessons/*.md`, no `tools/gates/frozen/**`, no `.ufo/**`
path was written by this seat; no git command mutated state; no network call
was made. `git status --porcelain` at 03:56:23Z read `M LOG.md`,
`?? REGIMEN.md`, `?? reports/round-33/` (3 rows). Interpreter for every command
below: `python3 -V` → **Python 3.14.7** (recorded because the anchors are
selftest counts, which are interpreter-sensitive — R03-F7).

## 1. Method and dependency state

Mission (`reports/round-33/targets.json:79`): "Final operability receipt
(post-review): fold R01-R03 findings into O08's draft as accepted/errata;
final command-carried receipt."

At the first cut, `reports/round-33/op/`, `review/`, `calib/`, `adj/`,
`cross/` and `scribe/` were all empty directories (`ls -la` per directory,
2026-10-19T03:50Z). Per the shared missing-dependency rule
(`reports/round-33/targets.json:10`) this seat ran every claim-O command
first-hand rather than inheriting numbers, then folded each fragment as it
landed. Exit codes here were captured unpiped or via `PIPESTATUS`, never as a
pipe's status (R03's own caution, `review/R03-op-review.md:64-68`).

## 2. Claim O — receipt

### 2.1 Lessons leg (O-a): declaration-time state reproduced, after-state not landed

Counting command (`reports/round-33/claims.json:33`):
`python3 -B reports/round-25/audit/c31-lessons-index-audit.py`

Measured at 2026-10-19T03:53Z, exit **1**:

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
```

This reproduces the declaration-time before-state (`reports/round-33/claims.json:25`)
exactly, and it matches three independent same-window captures line for line:
O07's (`op/O07-baseline-receipt.md:52-63`), O08's (`op/O08-receipt.md:23-40`)
and R03's re-run (`review/R03-op-review.md:24`). The tool's checks are at
`reports/round-25/audit/c31-lessons-index-audit.py:197` (`C31_index_rows_eq_files`),
`:202` (finding `C31-1`), `:315` (`C34b_prose_arithmetic`), `:317` (finding `C34-2`).

Selftest leg (`reports/round-33/claims.json:34`):
`python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest`
→ **exit 0, `SELFTEST OK: 28/28 checks passed`** (03:53Z).

File-count cross-checks at 03:53Z: `ls corpus/lessons/*.md | wc -l` = **33**;
`git ls-files | wc -l` = **2655**; `git ls-files corpus/lessons | wc -l` = 179
(the partition glob counts only top-level `*.md`).

**After-state not landed:** `corpus/lessons/README.md` is unedited at
sha256 `ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c`
(03:53Z; O07 `:76` and R03 `:151-152` agree), and the audit is still red. The
required after-state (`reports/round-33/claims.json:29`) is owed to integrator
application of O01's rows and O02's delta.

**The target state is reachable — two independent proofs, neither a delivery.**

- O08's simulation (`op/O08-receipt.md:65-96`): reconciled README built in
  scratch, tool's `INDEX` patched to those bytes, `run_checks()` unchanged →
  `index rows: 33`, six PASS, `findings: 0`, exit 0
  (`reports/round-25/audit/c31-lessons-index-audit.py:460`:
  `main()` returns `0 if not res["findings"]`). Labelled a simulation
  throughout (`op/O08-receipt.md:12-16,284-288`).
- R03's fixture route (`review/R03-op-review.md:131-152`): live 33 lesson files
  + live README with O01's seven drafted rows inserted, run through a relocated
  copy of the tool → same green. R03 also confirms the seven row pins by an
  independent `sha256sum`/`wc` route (7/7, `:147-150`).

**Row cells the seven new rows must carry** (O08's re-measurement,
`op/O08-receipt.md:105-113`, agreeing with K01 `op/K01-falsifier-scout.md:45`,
K02 and O01 per R03 `:147-150`): round-26 `60054/222/cae06660`, round-27
`54972/203/f15e285b`, round-28 `50419/145/dd832ff7`, round-29 `17847/118/b6765d33`,
round-30 `30665/181/56e77835`, round-31 `16637/73/8870bbdd`, round-32
`12879/66/8aacfc2b` (this seat's own pin for `round-32.md`: sha256
`8aacfc2bd9f55ec9dae3a721dc793a83bf071e90b98955ffa2cb45a33437ab64`). All seven
classify `gate-keeper`; O04 owns the format verdicts.

**Open row-shape divergence (R03-F9, `review/R03-op-review.md:156-166`):** O01
and K02 name different disposition-pointer cells for rounds 30 and 32 (both
paths exist; the tool does not machine-check that column). R03 recommends the
cell name the round's `validation.json` as the acceptance artifact, with any
additional ledger appended. The integrator needs one named rule before applying
the rows; this receipt records the divergence rather than choosing for them.

**Two more rules the integrator must state before the README edit lands
(R01-F2/F6, `review/R01-op-review.md:85-115,147-162`):**

- **The §4 queue-mint count is contested across fragments — 15 ids (O01 `:127`,
  P01 `:171-181`, O03 `:84-92`) vs 13 ids (K02 `:149`, excluding Q-30-4/Q-30-5
  as closed-at-source).** This is not cosmetic: `Rows: **49**` is re-derived by
  the tool's queue regex, and K02's own after-value is `49 + 13 = 62`. Drafting
  15 rows while the prose states 62 turns C34b red for an arithmetic reason
  after the reconciliation — the exact failure class claim O exists to close.
  R01 recommends K02's stricter "carried, not closed-at-source" reading, with
  Q-30-4/Q-30-5 named in the carried cell as closed, and re-deriving
  `Rows: **N**` from the applied table rather than from any fragment's
  arithmetic.
- **The carried-cell definition needs one rule (F-R01-6).** K02/O01/P01 read
  r31/r32 cells as the ids *declared* in each lesson's own queue section
  (r31 "Q-31-1..4", r32 "Q-32-1..6"); O03 reads ids *named anywhere* (r31
  "Q-30-2, Q-31-1..4", r32 "Q-30-2, Q-31-1..4, Q-32-1..6"). Both reproduce
  their own stated rule; the literal id count favours O03's set (r31 names 5,
  r32 names 11). A `X-N..M` range-read rule is also missing — O03 reads r26 as
  6 ids while `corpus/lessons/round-26.md:126` carries the range expression
  "`Q-02-1..4`" (9 ids, all present in §4), so its "0 dangling" verdict stands
  while its count understates by 3. Any fragment's id census used to size the
  §4 delta must follow the stated rule.

**R02's tool-graded previews of O01's rows (folded, `review/R02-op-review.md:60-98`).**
R02 ran the filed tool itself against previews built from the live README bytes
with O01's seven rows inserted:

| preview | rows/files | queue | verdict |
|---|---|---|---|
| V1 — O01's 7 rows + `:97` → `**Rows: 33. Files: 33.**`, §4 untouched | 33/33 | 49 | all six PASS, findings 0 — O01's rows are machine-sufficient |
| V2 — V1 + 15 new §4 queue rows, `:207` left at 49 | 33/33 | 64 | FAIL C34b `{queue_rows: {stated: 49, measured: 64}}` |
| V3 — V2 + `:207` → `Rows: **64**` | 33/33 | 64 | all six PASS, findings 0 |
| NEG — O01's rows, `:97` stale | 33/33 | 49 | FAIL C34b `{table_rows_vs_files: {stated: [26,26], measured: [33,33]}}` |

Three consequences the integrator must handle:

- **F-R02-1 (HIGH): the delta must carry `:207`.** O01's §5 byte list omits
  `:207` — the **first** `Rows: **N**` match and therefore the C34b queue leg;
  K02 §7 names it. Adding the queue rows O01 requires while leaving `:207` reds
  the claim's own counting command (V2). The second sentence of `:207` ("Of the
  26 index rows, **23 carry at least one question**") must also be restated
  against the applied rows, with the "carries" convention stated — R02 counts 4
  of the 7 new rows naming ids, giving `23 → 27` on the "names any id" reading
  or `23 → 26` if citing is not carrying.
- **The C34b parser asymmetry (R02 §2a, `review/R02-op-review.md:88-98`):** the
  queue count is governed by the **first** `Rows: **N**` match and the table
  pair by the **last** `**Rows: n. Files: n.**` match. Any new `Rows: **N**`
  line above §4 shadows the queue count, and any later table-shaped line —
  including one written inside §3 to describe class counts — shadows the table
  pair. Both shapes must stay unique and correct.
- **F-R02-4 (MEDIUM): a dated Revision 3 block is required.** Seven rows
  measured on 2026-10-19 make `README.md:22-29`'s "re-measured … at
  2026-10-18T17:35Z" sentence false; `README.md:303-305` is the file's own rule
  (superseding edits land as a new revision block). **F-R02-6 (MEDIUM):**
  inserting 7 rows after `:94` shifts every later anchor by +7 (`:97`→`:104`,
  `:111`→`:118`, `:144`→`:151`, `:207`→`:214`, `:234`→`:241`, `:279`→`:286`,
  `:307`→`:314`) — apply by content match, never by pre-edit line number.

**Stale-26 inventory the reconciliation must address.** The tool machine-checks
exactly two prose sites (`reports/round-25/audit/c31-lessons-index-audit.py:296-314`).
O08's fuller sweep (`op/O08-receipt.md:128-159`) finds ten further stale sites
the regexes do not reach; this seat spot-checked each README line against live
text and confirms them:

| README site | current text | measured reality |
|---|---|---|
| `corpus/lessons/README.md:5` | "**24 filed lessons**" | 31 filed lessons (33 files − README − round-25 row) |
| `corpus/lessons/README.md:6` | "26 at the final stamp" | 33 files |
| `corpus/lessons/README.md:35` | `--selftest  # 26/26, exit 0` | 28/28 |
| `corpus/lessons/README.md:39-40` | `ls … \| wc -l  # 26 (2026-10-18)` | 33 |
| `corpus/lessons/README.md:97` | "**Rows: 26. Files: 26.**" | **the machine-checked table site — must become 33/33** |
| `corpus/lessons/README.md:118` | "**14 files.**" (gate-keeper class) | 21 files |
| `corpus/lessons/README.md:124-125` | "**5 files**" (fragment-index) | 5 — still correct |
| `corpus/lessons/README.md:127-128` | "**7 files.**" (plain) | 7 — still correct |
| `corpus/lessons/README.md:138-141` | histogram "gate-keeper **14** … Total 26" | gate-keeper **21**, fragment-index 5, plain 7, total **33** |
| `corpus/lessons/README.md:207` | "Rows: **49**. Of the 26 index rows, **23 carry…**" | machine-checked cell: 49 stays green if no queue rows are added (`op/O08-receipt.md:136-144`); the surrounding prose ("Of the 26 index rows", "the three that carry none" at `:208-210`) is stale once 33 rows land |
| `corpus/lessons/README.md:257` | "beside the 26 `*.md` lesson files" | 33 |
| `corpus/lessons/README.md:285` | "`--selftest` is 26/26 in-memory checks" | 28/28 |
| `corpus/lessons/README.md:294` | "the 24 filed lessons" | 31 filed lessons |

The README also contradicts itself independent of the seven new files: it
states 26/26 at `:35` and `:285` but 28/28 at `:338` (its own Revision-2
control line, written 2026-10-18T17:47Z); the live tool says 28/28.
`corpus/lessons/round-32.md:45` records the same gap from the lesson side: the
index "carries **27 data rows**: 26 naming `corpus/lessons/*.md` paths … plus
the round-13 absence row", with rounds 26–31 filed outside it and round 32
making 7. The path-row count is what C31 compares, so the round-13 absence row
must not be counted as a file row when the rows land.

**Validator trap for whoever writes `run-validation.py` (R03-F6,
`review/R03-op-review.md:55-62`).** The audit tool's `--json` path returns 0
unconditionally (`reports/round-25/audit/c31-lessons-index-audit.py:444-447`,
confirmed here by reading the bytes), so a leg gating on `--json`'s exit code
is vacuous even with findings present; use plain mode, which exits 1
(`:460`). R03 measured `--json` with 2 live findings → exit 0 while plain mode
→ exit 1.

**README §5's nine-subdirectory / 146-file count is measured, not owed (R02).**
R02 re-measured `find corpus/lessons/*/ -type f | wc -l` → **146 files over 9
directories**, so `:256-257` and `:325` remain correct and only the "26 `*.md`
lesson files" phrase moves (`review/R02-op-review.md:229-231,475-476`). This
closes the `to-verify` item O08 left (`op/O08-receipt.md:157-159,298-299`).

### 2.2 Falsifier leg (O-b): located, dispositioned, counting command green

Counting command (`reports/round-33/claims.json:35`):
`test -s reports/round-33/op/O05-falsifier-disposition.md` → **exit 0** at
04:00Z (it read exit 1 at 03:53Z and 03:57Z; the artifact landed at 03:59Z).

**Location (K01, `op/K01-falsifier-scout.md:5-27`; independently reproduced by
O05, `op/O05-falsifier-disposition.md:18-38`).** The debt is finding **F-X16-3**,
stated at `corpus/lessons/round-32.md:36` (heading "The falsifier legs —
substance 5/5, instrument false-fires on day one") and `:41`, with its open
route **Q-32-1** at `:55`. The instrument is the checklist one-liner at
`SKILL.md:713-715`, landed by commit `17e90b9`: its closure predicate tests for
a file literally named `telemetry/closing-snapshot.json`, while the landed
snapshots are named `telemetry/availability-close-N.json` — so the audit
false-fires with 5 rows for rounds that are in fact closed.

This seat independently confirmed the load-bearing facts at HEAD `139e3b6`:

- `find reports corpus tools -name 'closing-snapshot.json' | wc -l` → **0**; the
  literal filename the audit requires exists nowhere (O05's `grep` agrees,
  `op/O05-falsifier-disposition.md:50-53`).
- `ls reports/round-*/telemetry/availability-close-*.json | wc -l` → **5**
  (rounds 19, 25, 26, 27, 28) — the landed convention.
- Live schema keys in `reports/round-19/telemetry/availability-close-19.json`
  are `"closes"` and `"closes_sha256"`; `grep -rn "closes_record"` over the repo
  returns only `corpus/lessons/round-32.md:41,55` and the fragments quoting it.
  The lesson and Q-32-1 paraphrase the key; a re-keyed audit testing
  `closes_record` would false-fire a second time (K01 `:82-91`, O05 `:58-67`).
- `corpus/lessons/round-32.md` sha256 `8aacfc2bd9f55ec9dae3a721dc793a83bf071e90b98955ffa2cb45a33437ab64`,
  matching K01's `:135` and O05's `:269` pins.

**Disposition folded from O05** (`op/O05-falsifier-disposition.md:73-93,123-152,217-226`).
R01 extracted the §3b command from the fragment's own bytes and ran it live:
**0 rows, exit 0**; with one snapshot hidden the negative control fires 1 row
(r28) — the repoint is functionally verified by a non-author, not merely
asserted (`review/R01-op-review.md:220-222,254-257`):

| # | element | class | next touch |
|---|---|---|---|
| D-1 | the closure predicate at `SKILL.md:715` | **fixed-with-evidence (draft ready; integrator applies)** — §3b carries the exact after-bytes, content-keyed on `closes` + `closes_sha256`, and a 7-scenario control set shows live rows 5 → 0 with the old/new instruments disagreeing exactly where the fixture's content decides | the round-33 SKILL.md landing, then re-run `.scratch/o05/build-controls.py`; and per R02 §5 item 6, re-run `python3 -B reports/round-30/craft/box1-survey.py` and record the new SKILL sha so the round-32 dossier's box-1 inventory condition is re-bound rather than left stamp-stale (`review/R02-op-review.md:393-403`) |
| D-2 | the recorded falsification clause (i) (`LOG.md:3460-3463`) | **carried — no change needed once D-1 lands** (the clause is satisfied as written; its day-one fire was instrumental) | parent/operator re-read at the D-1 landing; the reword variant would be a new dated LOG entry |
| D-3 | the lesson prose key name `closes_record` (`corpus/lessons/round-32.md:41,55`) | **carried-with-owner+reason+next-touch** — the lesson is filed bytes, append-only | the next lessons write records that the key is `closes` |
| D-4 | `reports/round-31/run-validation.py:780` closure test keyed to the exact filename | **carried, routed — not absorbed** (same defect class in another instrument; demonstrated, `op/O05-falsifier-disposition.md:228-245`) | parent/operator, at the first correction-named snapshot |

**O08's disposition is superseded by K01/O05.** `op/O08-receipt.md:257-266`
carried the item `carried-with-owner + reason` (owner K01 → O05) on the finding
that no in-lane antecedent existed at its read, listing four ranked candidates
as `to-verify` (`:231-255`). The antecedent is the round-32 lesson, which
O08's and this seat's first-cut search surfaces both omitted. With O05's
bounded fix draft landed, the claim's binary resolves to
**fixed-with-evidence, pending integrator application**.

**Still owed for full claim-O verification:** the integrator's application of
O05 §3b to `SKILL.md:715` and a post-landing re-run of the control harness.
The filed lesson bytes are never rewritten (`corpus/lessons/round-32.md:41`
closes with "this lesson does not edit the rule it audits").

### 2.3 Cross-check against the other landed claim-O fragments

- `op/O07-baseline-receipt.md` (baseline of record) — verified verbatim by R03
  (`review/R03-op-review.md:18-32`) and re-run row-for-row by this seat (§3).
- `op/O08-receipt.md` — before-state, cells, stale-26 inventory and simulated
  after-state folded into §2.1.
- `op/O01-row-drafts.md`, `op/O04-format-checks.md`, `op/K02-lessons-census.md`,
  `op/O03-owner-checks.md`, `op/P01-plan.md` — landed; R03 cross-checked O01/K02
  pins (7/7 agreement) and found the F9 pointer divergence. This seat did not
  re-verify their cells — R01/R02 own that surface
  (`reports/round-33/targets.json:65-66`).
- `op/O06-controls.md` — **landed 04:01Z**, just after this seat's 04:00Z check
  (`ls reports/round-33/op/O06*` → no such file at that stamp): **11 controls
  (C0–C9) executed green** against the round-33 tree before any integration
  edit, covering `C31-1`/`C31-2`/`C31-3`, `C32-1`, `C33-1`, `C34-1`, `C34-3`,
  `C34-2`, plus an identity control and a mechanically-reconciled positive
  control, and pinning the `--json` exit-0 trap as control C8
  (`op/O06-controls.md:10-12,22-31,38-39,65-76`). R03 §2 supplies the
  nine-control requirement set to grade it against; the sufficiency verdict is
  still owed by a reviewer (`review/R03-op-review.md:70-129,193-200`).

### 2.4 Filed-byte integrity incident: three filed `validation.json` moved, then restored (R01-F1, HIGH)

`op/O07-baseline-receipt.md:147-181` records that between its 03:52Z capture and
03:54:59Z, `reports/round-5/validation.json` and `reports/round-7/validation.json`
were rewritten in place by some seat re-running historical validators — filed
round bytes, which this round's rules forbid moving. O08's own read at ~03:52Z
shows the same two rows in its `git status --porcelain`
(`op/O08-receipt.md:58-63`), and R05 observed the same state independently
(`review/R05-calib-review.md:105-118`).

R01 raises this to its only HIGH finding and adds a third file plus the
restoration evidence (`review/R01-op-review.md:51-83`):
`reports/round-6/validation.json` was rewritten too, and the writers are the
historical validators themselves — each rewrites its own receipt in place
(`reports/round-5/run-validation.py:194`, `reports/round-6/run-validation.py:336`,
`reports/round-7/run-validation.py:1171`). R01's point is that the **restore
erases the evidence from `git status`**: the scope watch (A03/X02) and this
receipt's threshold binding can both read clean while filed bytes were in fact
moved and restored.

This seat re-verified all three at 2026-10-19T04:02Z:

- `git status --porcelain -- <the three paths>` → **no rows**; `git diff
  --numstat` over them → **empty**.
- live sha256 == `git show HEAD:` sha256 for each: r5 `73a66f7464ead0d9…`,
  r6 `32c621efaccca71d…`, r7 `2f4c1e159b60d782…` — matching R01's post-restore
  digests (`review/R01-op-review.md:60-66`).

So the drift was transient and the tree reads HEAD again — but the incident is
real and the round still owes R01's three integrator actions
(`review/R01-op-review.md:75-83`): a dated LOG/scope entry recording the
incident and the restore with the three paths and both digest sets (pre-restore
r5 `fe926984e8d15728…`, r7 `af0cf4ed32d68c2b…` per
`op/O07-baseline-receipt.md:169-174`); an errata line on O07's receipt so it is
not read as a clean pre-edit binding; and the writer's attribution, which stays
**to-verify** (O07, R05 and R01 all leave it open). Claim O's "zero regressions"
leg binds on tool digests and command results (§3), not on these files, but the
episode is the round's only observed filed-byte motion.

## 3. Regression baseline receipt — green, and verified

Baseline of record: `reports/round-33/op/O07-baseline-receipt.md` (capture window
2026-10-19T03:52:07Z–03:52:30Z, digest pins at `:67-83`). R03 re-ran every
command and re-measured every digest: **verified verbatim**, all 8 digests, all
4 exit codes, the battery summary, the c31 before-state and the scope counts
(`review/R03-op-review.md:18-32`). This seat ran the same four commands
independently at 03:53-03:54Z; results match row for row:

| command | exit | measured result | O07 |
|---|---|---|---|
| `python3 tools/check-gate-battery.py --selftest` | 0 | `SELFTEST OK 44/44 controls behaved as expected` | `:31` |
| `python3 tools/check-craft-exercise.py --selftest` | 0 | `SELFTEST OK 10/10 tamper cases detected` + `CLI-SELFTEST OK 18/18 cases passed` | `:32` |
| `python3 tools/assemble-culture-d4.py --selftest` | 0 | `selftest: 81/81 checks passed` | `:33` |
| `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` | 0 | `SELFTEST OK: 28/28 checks passed` | `:34` |

The battery's own control lines carry expected codes (e.g.
`CTRL-BASELINE-TAMPERED: exit=2 outcome=snapshot_tampered`), so 44/44 is a
behavioural count, not an "all green" count. O07 additionally captured battery
mode (`pass 7, fail 0, unevaluable 0`, coverage `10/10`, `pinned 20`,
`originals.preserved true`) — the "battery 10/10" of the claim-O threshold
(`reports/round-33/claims.json:37`) — plus `assemble-culture-d4.py --check`
byte-identical and `check-evidence-coupling.py --selftest` exit 0. O08 ran only
the c31 selftest and names the rest owed to O07 (`op/O08-receipt.md:295-297`).

**Errata R03 filed against O07** (none falsifies a measurement; all are
pointer/provenance repairs for the integrator, `review/R03-op-review.md:34-62,173-191`):

- R03-F1 (medium): `O07:121` and `:198` cite `reports/round-32/scope.md:13` for
  the 1,870-path figure; line 13 is **blank** and the statement is at `:10`.
  Confirmed here (`awk 'NR==13'` → empty; `sed -n '10p'` carries "**1,870
  tracked paths**").
- R03-F2 (low): `O07:123` cites `:21-24` for the 1,735 + 135 arithmetic, which
  is at `:29`.
- R03-F7 (low): no `python3 -V` in O07's pins — this receipt records
  **Python 3.14.7** for its own runs (§0).
- R03-F8 (low): `tools/check-evidence-coupling.py` is exercised by O07 but
  absent from its digest block.
- R03-F10 (informational): F1 is confined to O07 (`grep -n "scope\.md"
  reports/round-33/op/*.md` → three hits, all in O07); fixing those two lines
  before folding forward is sufficient. This receipt cites no `scope.md` line.

## 4. Cross-claim touchpoints (outside this receipt's surface)

- Claim C's ledger (`calib/open-items-ledger.json`, `reports/round-33/claims.json:46`)
  and claim A's audit (`adj/audit-assembled.md`, `:59`) are S02's and S03's
  receipts. This seat did not evaluate them.
- Shared-file collision surface for claim O's after-state: the lessons README
  (integrator-applied, `reports/round-33/targets.json:7`) and `SKILL.md:713-715`
  for the O05 repoint (also shared-file). X00's collision matrix owns that
  overlap; O05 keeps the repoint position-agnostic and routes the item's
  *location* question (F-X16-2 / Q-32-3) to the parent
  (`op/O05-falsifier-disposition.md:113-121`).

## 5. Fold-in register for R01-R03

| slot | expected source | state | fold-in result |
|---|---|---|---|
| R01 findings (adversarial pass over `op/`) | `reports/round-33/review/R01-op-review.md` | **landed 04:02Z — folded** | nine findings, one HIGH; fold-in table below. R01's §4 independent ground truth (`:231-257`) reproduces this receipt's before-state, baseline and falsifier verdicts; its clarification that the claim's "battery 10/10" is the **coverage** reading while the battery's `pass` counter is **7** is carried in §3 — the round receipt should keep both numbers so a reader expecting `pass 10` does not read a false regression |
| R02 findings (README row-format parity + O05 disposition logic) | `reports/round-33/review/R02-op-review.md` | **landed 04:04Z — folded** | eleven findings, three HIGH; fold-in table below. Its tool-graded previews V1/V2/V3/NEG and the C34b first/last-match asymmetry are folded into §2.1; its §5 re-execution of O05's §3b command (0 rows live vs OLD's 5) and the new box-1 pin cascade into §2.2; its honesty requirement (F-R02-3) into §0. **Owed from its own list**: O02 (absent) — grade it with R02 §4's checker when it lands |
| R03 findings (controls sufficiency + baseline completeness) | `reports/round-33/review/R03-op-review.md` | **landed 03:59Z — folded** | **accepted**: F1/F2/F7/F8/F10 as O07 errata (§3, F1 confirmed first-hand); F6 as the `--json` validator trap (§2.1); F9 as the row-shape rule the integrator must name (§2.1); the O07 completeness verdict (verified verbatim, `:18-32`) and the fixture target-state proof (`:131-152`) folded into §3 and §2.1. **Owed, not folded**: R03-F3/F4/F5's sufficiency verdict on O06 — R03 wrote before O06 landed (O06 filed 04:01Z with 11 controls, `op/O06-controls.md:10-12`), so the diff of O06's named controls against R03 §2's requirement set is still a reviewer task (`:193-200`) |
| O08 draft (the receipt body this file finalizes) | `reports/round-33/op/O08-receipt.md` | **landed 03:57Z — folded** | before-state, simulated after-state, seven-file cells, stale-26 inventory, command inventory and honest limits folded (§2.1, §3); its falsifier disposition is superseded by K01/O05 (§2.2) |

### R01 findings — accepted / errata

| R01 finding | sev | fold-in result |
|---|---|---|
| F-R01-1 — three filed `validation.json` (r5, r6, r7) rewritten in place, then restored | HIGH | **accepted** — §2.4 rewritten to add r6, the restoration digests and R01's three integrator actions; this seat re-verified all three CLEAN vs HEAD at 04:02Z |
| F-R01-2 — §4 queue-mint count contested: 15 ids (O01/P01/O03) vs 13 ids (K02) | MEDIUM | **accepted** — recorded in §2.1's integration rules; the integrator must state the rule (R01 recommends K02's stricter "carried, not closed-at-source" reading) and re-derive `Rows: **N**` from the applied table, never from a fragment's arithmetic, or C34b goes red for an arithmetic reason |
| F-R01-3 — P01 misnames the missing contract line (r29/r30 lack `recheck:`, not `scope:`) | MEDIUM | **accepted as errata** — the applied cell `3/4` is unaffected (the tool measures it); the rule text would mis-derive a cell if followed literally for another file |
| F-R01-4 — O04's H3 sub-shape count 17 contradicts its own enumeration and the measurement (13 files) | MEDIUM | **accepted as errata** — the H2-is-new conclusion stands; only the H3 total is wrong; fix before the §3 prose draft is applied |
| F-R01-5 — O08 §3 superseded; the integrator must consume O05, not O08 §3 | MEDIUM | **accepted — already satisfied**: §2.2 names O08 §3 superseded by K01/O05 and cites O05 as the disposition of record, so the "located" branch is the one on record |
| F-R01-6 — carried-cell definition drift (r31/r32) and no `X-N..M` range-read rule | LOW-MEDIUM | **accepted** — recorded in §2.1's integration rules; feeds F-R01-2's mint count |
| F-R01-7 — O07's two stale pointers to `reports/round-32/scope.md:13` | LOW | **accepted as errata** — converges with R03-F1/F2 (§3); two independent reviewers found the same dead pointer |
| F-R01-8 — O04's `spot-check` line list is short one line (`round-26.md:172`) | LOW | **accepted as errata** — the count is right, the citation incomplete |
| F-R01-9 — O01's quoted self-check output is stale (fence count 3 vs the filed 4) | LOW | **accepted as errata** — re-run and re-quote, or note the revision; the checker's substance is unaffected |

### R02 findings — accepted / errata

| R02 finding | sev | fold-in result |
|---|---|---|
| F-R02-1 — O01's delta list omits `README.md:207`, the C34b queue anchor | HIGH | **accepted** — folded into §2.1's preview table and rules; the delta must carry `:207` and restate its second sentence |
| F-R02-2 — §4 id set 13 (K02) vs 15 (O01); the C34b number 62 vs 64 follows the choice | HIGH | **accepted** — folded into §2.1 (converges with R01-F2): one owner decides, and the Revision 3 block states set, count and arithmetic |
| F-R02-3 — the machine legs cannot distinguish V1 from V3; "findings: 0" is not §4 coverage | HIGH | **accepted** — §0 now carries the honesty declaration and routes it to `cross/X04-honesty.md`; this receipt does not present findings: 0 as §4 coverage |
| F-R02-4 — adding rows contradicts `:22-29`'s stamp unless a Revision 3 block lands | MEDIUM | **accepted** — folded into §2.1's rules (dated Revision 3 block per `README.md:303-305`) |
| F-R02-5 — the README edit reds a filed runner and makes two digest pins stamp-stale | MEDIUM | **accepted** — `reports/round-26/run-validation.py:97,1494-1500` pins the README blob `a3187055…` and asserts it: the honest handling is a declared supersession in the round's LOG entry, not silence. And O07's digest list must not be read as "these bytes are invariant" — the four named selftests are the invariance surface, the README digest is an expected-move surface |
| F-R02-6 — every later README anchor shifts by +7 after the insertion | MEDIUM | **accepted** — folded into §2.1's rules (apply by content match) |
| F-R02-7 — O01 §4's "round-32.md is pinned only by the live read" is false | LOW | **accepted as errata** — `reports/round-32/scribe/fragment-ledger.md:273` pins it (12879 bytes, sha8 `8aacfc2bd9f5`); the value agrees, the provenance sentence does not |
| F-R02-8 — three disposition-pointer cells differ between K02 §6 and O01 §2 (r30/r31/r32) | LOW | **accepted** — same class as R03-F9 but three cells, not two; parity favours O01 (11 of the 26 existing §2 rows name a `validation.json`); the delta must state which fragment it followed |
| F-R02-9 — tool-blind stale prose the delta must fix or explicitly decline | LOW | **accepted** — already covered by §2.1's inventory; R02 adds that `:35` and `:285` are wrong at baseline (28/28) and that `:325` stays correct |
| F-R02-10 — O04's H2 sub-shape finding confirmed independently (H2 in exactly rounds 29–32) | LOW | **accepted as confirmation** — a §3 documentation gap the delta should close, per O04 §5 item 2 |
| F-R02-11 — `AGENTS.md:42` is a bodyless, instruction-shaped heading | LOW | **accepted, report-only** — routed to `cross/X02-conformance.md` / A08; no round-33 seat edits `AGENTS.md`. R02 also confirms the "Checklist ends at `:534`" citation is correct — do not "fix" it |

R02's §5 additionally reviews O05's disposition logic as sound across six
checks (the counting-command trap acknowledged; located-not-asserted reproduced;
the §3b one-liner extracted verbatim — 515 chars, no embedded newline — and run
live: **0 rows vs OLD's 5**; the `legacy-name-only` pair proving the old green
was name-based; no filed-byte rewrite; honest limits filed) and adds one cascade
O05 does not name: applying §3b changes `SKILL.md`'s bytes, so the round-32
dossier's box-1 inventory condition — pinned to `79fe91d3…` at
`reports/round-32/dossier-d11-shonen-boxes.md:205`, `dossier-d12-capability-inventory.md:97`,
`dossier-d13-operator-decisions.md:48`, `final-dossier.md:46,133` — becomes
stamp-stale. Recommended: re-run `python3 -B reports/round-30/craft/box1-survey.py`
after applying §3b and record the new SKILL sha with the result
(`review/R02-op-review.md:393-403`). Folded into D-1's next touch in §2.2.

## 6. What would make claim O verify

1. Integrator applies the O01/O02 drafts to `corpus/lessons/README.md`
   (33 path rows — disposition-pointer cells per one named rule, R03-F9 —
   the machine-checked table site at `:97` plus the stale prose listed in
   §2.1, cells re-measured) — then
   `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` must exit 0
   in **plain mode** with `findings: 0` and 33 rows == 33 files, and
   `--selftest` must stay 28/28. Do not gate on `--json`'s exit code (§2.1).
2. Integrator applies O05 §3b to `SKILL.md:713-715` as a logged change and
   re-runs `.scratch/o05/build-controls.py` (expect: live rows 5 → 0, 7/7
   scenarios as designed, `op/O05-falsifier-disposition.md:123-152`).
3. All three review rows in §5 are folded (done at this revision: R01, R02,
   R03), and O06's sufficiency verdict is filed against R03 §2's nine-control
   requirement set.
4. §3's four commands still exit 0 with the same counts and the O07 digest pins
   hold (`op/O07-baseline-receipt.md:67-83`, with R03's and R01's errata applied).
5. No filed round 1–32 byte differs from the baseline commit at close
   (`git status --porcelain` free of `reports/round-*` rows) — the §2.4 episode
   must not recur, and the incident plus its restore are recorded in a dated
   LOG/scope entry.
6. The §4 traceability question is dispositioned explicitly (queue rows added vs
   prose pointers) and the receipt does not lean on "findings: 0" for it
   (R02-F3, §0).

At this cut: item 2's artifact exists, its control set is green and two
reviewers re-executed the draft command, but the `SKILL.md` application is still
integrator work; item 1 is untouched on live bytes; item 3 is satisfied for the
reviews and still owed for O06's verdict; items 5-6 are outstanding. The honest
claim-O verdict is therefore **not verified yet — both legs dispositioned,
neither delivered**.

## Owed

- `reports/round-33/op/O02-readme-delta.md` — the one claim-O artifact still absent; R01 `:274-282` and R02 §4 name the checks to grade it against, including R02's parity checker (P1–P10)
- O06 sufficiency verdict — `op/O06-controls.md` landed 04:01Z with 11 controls (C0–C9, `CONTROLS OK: 11/11`, `op/O06-controls.md:10-12`); a reviewer must diff its named controls against R03 §2's requirement set, re-run them with payload assertions (`review/R03-op-review.md:193-200`), and reconcile its C34b expectations with R02 §2a's measured first/last-match asymmetry
- Integrator application of O05 §3b to `SKILL.md:713-715` + control re-run + the box-1 re-bind (`python3 -B reports/round-30/craft/box1-survey.py`) — the disposition draft is landed and reviewer-verified; the landing is not
- Integrator application of O01/O02 to `corpus/lessons/README.md` with the rules now on record: the F9/F-R02-8 pointer-cell rule, the F-R01-2/F-R02-2 queue-mint count, the F-R01-6 carried-cell/range rule, the F-R02-1 `:207` anchor, the F-R02-4 Revision 3 block, and F-R02-6 content-match application (§2.1)
- A declared supersession in the round's LOG entry for `reports/round-26/run-validation.py:97,1494-1500`'s README blob assertion (F-R02-5)
- R01's three filed-byte actions (§2.4): a dated LOG/scope entry recording the incident and restore, an errata line on O07's receipt, and the writer's attribution (to-verify)
- Errata re-quotes before any number is quoted onward: P01 `:123-124` (F-R01-3), O04 `:77-80` (F-R01-4), O04 `:95-96` (F-R01-8), O01 `:147-152` (F-R01-9), O01 §4's provenance sentence (F-R02-7)
- README §5's nine-subdirectory / 146-file count — **closed at this revision** by R02's re-measurement (146 files over 9 directories; §2.1), no longer owed
- attribution of the §2.4 filed-byte rewrite (owner to-verify) — for A03/X02, not for this seat

Landed and folded (no longer owed): `op/K01-falsifier-scout.md`,
`op/K02-lessons-census.md`, `op/O01-row-drafts.md`, `op/O03-owner-checks.md`,
`op/O04-format-checks.md`, `op/O05-falsifier-disposition.md`,
`op/O06-controls.md`, `op/O07-baseline-receipt.md`, `op/O08-receipt.md`,
`op/P01-plan.md`, `review/R01-op-review.md`, `review/R02-op-review.md`,
`review/R03-op-review.md`.

## Citations

Paths:lines
- `reports/round-33/claims.json:19-37` (claim O); `:25`, `:29`, `:33-35`, `:37`; `:46`, `:59` (claims C and A artifacts)
- `reports/round-33/targets.json:6-10` (shared rules), `:7` (shared files integrator-applied), `:13` (K01), `:26` (O05), `:28` (O07), `:65-67` (R01-R03), `:79` (S01 mission)
- `reports/round-25/audit/c31-lessons-index-audit.py:197,202,296-317,315,317,444-447,460` (checks/findings, the two machine-checked prose sites, `--json` exit, plain-mode exit)
- `corpus/lessons/README.md:5,6,35,39-40,97,118,124-125,127-128,138-141,207-210,257,285,294,338` (stale-26 inventory and the 26/26-vs-28/28 inconsistency)
- `corpus/lessons/round-32.md:36,41,45,55` (F-X16-3 heading/finding, row census, Q-32-1); sha256 `8aacfc2bd9f55ec9dae3a721dc793a83bf071e90b98955ffa2cb45a33437ab64`
- `SKILL.md:522,534,660,713-715` (Checklist section bounds, D3 heading, the item and its false-firing one-liner)
- `SCORECARD.md:443-445`; `LOG.md:3460-3468` (falsification clause i-iii), `:3512-3514` (standing inputs)
- `reports/round-32/scope.md:10` (the 1,870 statement), `:13` (blank — R03-F1)
- `reports/round-33/op/K01-falsifier-scout.md:5-27,45,82-91,119-129,135`
- `reports/round-33/op/O05-falsifier-disposition.md:18-38,50-53,58-67,73-93,113-121,123-152,217-226,228-245,269`
- `reports/round-33/op/O07-baseline-receipt.md:14-15,27-34,52-63,67-83,103-116,121,123,147-181,198`
- `reports/round-33/op/O08-receipt.md:12-16,23-40,42-44,58-63,65-96,105-113,128-159,231-266,284-299`
- `reports/round-33/review/R03-op-review.md:18-32,34-62,64-68,70-129,131-152,156-166,173-191,193-200`
- `reports/round-33/review/R01-op-review.md:5-14,51-83,85-115,147-162,189-229,231-257,259-291`
- `reports/round-33/review/R02-op-review.md:22-58,60-98,100-147,149-184,186-192,194-215,216-236,238-245,247-256,258-361,363-408,409-425`
- `reports/round-26/run-validation.py:97,1494-1500` (the README blob assertion the edit supersedes — F-R02-5); `reports/round-32/scribe/fragment-ledger.md:273` (round-32.md's filed pin — F-R02-7); `reports/round-32/dossier-d11-shonen-boxes.md:205`, `dossier-d12-capability-inventory.md:97`, `dossier-d13-operator-decisions.md:48`, `final-dossier.md:46,133` (the box-1 `79fe91d3…` pins — R02 §5.6); `reports/round-30/craft/box1-survey.py` (the re-bind command)
- `AGENTS.md:42` (bodyless instruction-shaped heading — F-R02-11, routed)
- `reports/round-5/run-validation.py:194`, `reports/round-6/run-validation.py:336`, `reports/round-7/run-validation.py:1171` (the validators that rewrite their own receipts in place — §2.4)
- `reports/round-31/run-validation.py:780,792-812` (name-exact closure test and the landed integrity leg a fix should mirror)
- `reports/round-19/telemetry/availability-close-19.json` (`closes`, `closes_sha256` keys)

Commands (run 2026-10-19T03:53-04:02Z, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; exits unpiped or via `PIPESTATUS`)
- `python3 -V` → `Python 3.14.7`
- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 1 (output quoted in §2.1)
- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` → exit 0, 28/28
- `python3 tools/check-gate-battery.py --selftest` → exit 0, 44/44 controls
- `python3 tools/check-craft-exercise.py --selftest` → exit 0, 10/10 + 18/18
- `python3 tools/assemble-culture-d4.py --selftest` → exit 0, 81/81
- `test -s reports/round-33/op/O05-falsifier-disposition.md` → exit 1 at 03:53/03:57Z, **exit 0 at 04:00Z**
- `ls reports/round-33/op/O06*` → no such file (04:00Z)
- `find reports corpus tools -name 'closing-snapshot.json' | wc -l` → 0
- `ls reports/round-*/telemetry/availability-close-*.json | wc -l` → 5
- `grep -o '"closes[a-z_0-9]*"' reports/round-19/telemetry/availability-close-19.json | sort -u` → `"closes"`, `"closes_sha256"`
- `grep -rn "closes_record"` (repo, excluding `.git`) → `corpus/lessons/round-32.md:41,55` + fragments quoting it only
- `sed -n '444,447p' reports/round-25/audit/c31-lessons-index-audit.py` → `--json` returns 0 unconditionally (R03-F6 confirmed)
- `awk 'NR==13' reports/round-32/scope.md` → empty; `sed -n '10p'` → carries the 1,870 figure (R03-F1 confirmed)
- `sed -n '5,6p;118p;124,128p;138,141p;294p' corpus/lessons/README.md` → confirms each stale-26 site quoted in §2.1
- `ls corpus/lessons/*.md | wc -l` → 33; `git ls-files | wc -l` → 2655; `git ls-files corpus/lessons | wc -l` → 179
- `sha256sum corpus/lessons/README.md` → `ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c`; `sha256sum corpus/lessons/round-32.md` → `8aacfc2b…37ab64`
- `sha256sum reports/round-33/claims.json reports/round-33/targets.json` → `ba69090f…b3fb12`, `342c8f80…7df13f`
- `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`
- `git status --porcelain` → 3 rows at 03:54Z and 03:56:23Z; `git diff --stat reports/round-5/validation.json reports/round-7/validation.json` → empty
- live-vs-HEAD sha256 compare for `reports/round-5/validation.json` (`73a66f7464ea…`) and `reports/round-7/validation.json` (`2f4c1e159b60…`) → CLEAN at 03:56:23Z
- 04:02Z re-verification of all three filed-byte paths (R01-F1): `git status --porcelain -- <paths>` → no rows; `git diff --numstat` → empty; live vs `git show HEAD:` → r5 `73a66f7464ead0d9…`, r6 `32c621efaccca71d…`, r7 `2f4c1e159b60d782…`, all CLEAN (§2.4)
- first-cut searches retained as history: `grep -rn "filename mismatch\|filename-mismatch\|file name mismatch"` (repo, excluding `.git`) → 5 hits, all naming the debt; `grep -rln "filename" reports/round-31/ reports/round-32/` → no hits; `grep -rn "mismatch" reports/round-30/ reports/round-31/ reports/round-32/` (excluding `validation.json`) → 12 hits, none the named mismatch; `grep -n "falsifier\|filename" /home/vgpnk/Projects/shokunin/.ufo/reports/round-3{0,1,2}/kotodama.md` → 1 hit (round-32:32); in-session filename-resolution probe over `reports/round-32/*.md` → 113 tokens, 109 resolve, 4 line-wrap artifacts
- R02's own runs, folded (`review/R02-op-review.md:462-484`): the audit + `--selftest` + `--json`; per-file `wc -c`/`wc -l`/`sha256sum`/`grep -c '^## Gate$'` over the seven files (its §1 table, 21 pin values agreeing with O01/K02/O04); `git log --oneline -- corpus/lessons/README.md` → one commit `fc13cd2`; `git hash-object corpus/lessons/README.md` → `a31870556c733498…`; the c31-copy harness with `m.ROOT`/`m.LESSONS` overridden and previews V1/V2/V3/NEG (§2); `.scratch/r02-parity.py` positive/negative controls (§4); verbatim extraction of O05 §3b's one-liner (515 chars, no newline) run live → 0 rows vs OLD 5 (§5.3); `grep -c closes_record corpus/lessons/round-32.md` → 2; `grep -l closes_record reports/round-*/telemetry/*.json` → 0; `find corpus/lessons/*/ -type f | wc -l` → 146 over 9 directories; `grep -c '^## [DOCA] — '`/`'^### [DOCA] — '` per file (H2: 29×3, 30×3, 31×3, 32×1)
