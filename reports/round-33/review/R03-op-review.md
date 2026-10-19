- Seat: R03 | reviewer | claim O | date 2026-10-19 | baseline 139e3b6

# R03 — third adversarial pass over `op/`: controls sufficiency (O06) and baseline-receipt completeness (O07)

Method: every verdict below is from commands I ran myself at the round-33 tree,
not from the fragments under review. All three dependencies landed before my
seat finished writing (`O07-baseline-receipt.md`; `O01-row-drafts.md` as the
artifact the controls must protect; `O06-controls.md`, which landed mid-review).
§1 grades O07 completeness, §2 gives the control requirement set I derived by
execution, §2b grades the control table in `op/P01-plan.md:203-225`, and §2c is
the verdict on `op/O06-controls.md` — the two controls fragments are graded
separately because they specify different sets.

## 1. O07 completeness verdict

I re-ran every command O07 cites and re-measured every digest it pins. All
substantive claims reproduce exactly:

| O07 claim | my independent result | verdict |
|---|---|---|
| 4 commands exit 0 (`:31-34`) | gate-battery `exit=0` `SELFTEST OK 44/44`; craft `exit=0` `10/10` + `CLI-SELFTEST OK 18/18`; d4 `exit=0` `81/81`; c31 `exit=0` `28/28` | verified |
| battery mode (`:38-45`) | `summary {"pass":7,"fail":0,"unevaluable":0}`, `coverage "10/10"`, `baselines_found 20`, `pinned 20`, `gates_uncovered []`, `findings []`, `originals {"preserved":true,"files_hashed_before":33,"files_hashed_after":33,"modified":0,"added":0,"deleted":0}`, `mirror.removed true` | verified verbatim |
| d4 `--check` (`:46-48`) | `exit=0`, `packet.d4.yml: byte-identical deterministic assembly` | verified |
| evidence-coupling selftest (`:49-51`) | `exit=0`, `"selftest_passed": true` | verified |
| c31 before-state (`:52-63`) | `exit=1`, 33 files / 26 rows / 49 queue rows, `FAIL C31_index_rows_eq_files`, `FAIL C34b_prose_arithmetic`, findings `C31-1` (7 files) + `C34-2` `{stated:[26,26], measured:[26,33]}` | verified verbatim |
| 8 digest pins (`:71-79`) | `sha256sum` agrees on all 8 (`check-gate-battery 455b595a…`, `check-craft-exercise b5b890b4…`, `assemble-culture-d4 943f487b…`, `c31-…-audit dc3ee4cc…`, `README.md ec7469da…`, `claims.json ba69090f…`, `targets.json 342c8f80…`, `dispatch-declared.json 139b964e…`) | verified, all 8 |
| digests agree with telemetry (`:81`) | `dispatch-declared.json` `durable_sources[]` carries `ba69090f…` and `342c8f80…` — same values | verified |
| HEAD / status / ls-files (`:19-25`) | `139e3b66…`; 3 status rows ` M LOG.md`, `?? REGIMEN.md`, `?? reports/round-33/`; `2655` | verified |
| LOG.md `+18` (`:23`) | `git diff --stat LOG.md` → `1 file changed, 18 insertions(+)` | verified |
| 1,830 + 825 split (`:126-127`) | `git ls-files \| grep -c '^reports/round-'` = `1830`; `grep -vc` = `825` | verified |
| index byte-frozen since r28 (`:128-133`) | `corpus/lessons/round-28.md:86` carries `ec7469dadf87df3e…`; live README digest is the same `ec7469da…` | verified |
| no gate-side pin on the index (`:136-142`) | same four frozen-gate paths return, all `packet.md`/ledger-format path strings, no digest on `corpus/lessons/README.md` | verified |
| "no integration edit had landed yet" (`:14-15`) | corroborated by mtimes: `claims.json 00:49:35`, `targets.json 00:50:55`, `dispatch-declared.json 00:51:23`, first `op/` fragment `00:54:39` — the tree O07 graded is the tree I graded | verified |

**Completeness defects** (the receipt binds its regression anchors correctly;
these are pointer/provenance gaps, none of which falsifies a measurement):

- **R03-F1 (medium) — dead pointer, cited twice.** `O07:121` and `O07:198` cite
  `reports/round-32/scope.md:13` for "**1,870 tracked paths**". Line 13 of that
  file is **blank** (`awk 'NR==13'` → `[]`); the 1,870 statement is at
  `reports/round-32/scope.md:10`. This is the same defect class claim O exists
  to repair, inside the receipt that is supposed to anchor the claim.
- **R03-F2 (low) — imprecise pointer.** `O07:123` cites `:21-24` for the
  "1,735 + 135" arithmetic. `:23` does carry the protected-surface prose, but
  the arithmetic itself is at `:29` (`Total **1,870** = 1,735 + 135`). The
  citation supports the premise, not the number.
- **R03-F7 (low) — interpreter version unrecorded.** The receipt is meant to be
  re-run by the integrator (`:103-116`), and its anchor values are selftest
  counts, which are interpreter-sensitive. `python3 -V` → `Python 3.14.7` is
  not in the receipt. A re-runner on a different minor version has no baseline
  to compare against.
- **R03-F8 (low) — one exercised tool lacks an anchor.** `tools/check-evidence-coupling.py`
  is run and reported (`:49-51`) but is absent from the digest block
  (`:71-79`), so the one supplemental tool it exercised cannot be
  regression-compared byte-wise.
- **R03-F6 (low, advisory) — a trap the receipt does not name.** The audit
  tool's `--json` path returns `0` unconditionally
  (`reports/round-25/audit/c31-lessons-index-audit.py:445-447`), so a
  post-integration leg that gates on `--json`'s exit code is vacuous even with
  findings present (measured: `--json` with 2 live findings → `JSON_EXIT=0`,
  while plain mode → `exit=1`). O07's own re-run block is correct — it uses
  plain mode at `:115` — but the integrator writing `run-validation.py` is
  exactly the reader who needs the warning.

Related measurement caution, recorded because it is the failure mode a receipt
dies of: capturing exit codes through a pipe reports the **pipe's** status, not
the tool's (`cmd | tail` → `$?` is `tail`'s). My first pass did this and read
`EXIT=0` for every leg; the re-run without a pipe returned the same zeros here,
so O07 is unaffected — but the pattern is one edit away from a false green.

## 2. O06 controls: sufficiency requirements, with the evidence for each

O06 is absent, so I built and ran the control set myself
(`.scratch/r03-controls/rigorous-controls.py`, output below). Nine controls are
needed, not three. The five design constraints below are not stylistic — each
one was a real failure I hit before the controls went green.

**Constraint 1 — the controls cannot run against the live tree.** The tool has
no corpus-redirect flag: `ROOT` is derived from `__file__` three levels up
(`c31-lessons-index-audit.py:34`) and `LESSONS` is fixed from it (`:35`). A
control that injects a fake file therefore has to write into
`corpus/lessons/` — outside the round's write boundary. The working method is a
relocated copy of the tool at `<fixture>/x/y/z/audit.py` (three levels, so
`ROOT` resolves to the fixture), proven here; `corpus/lessons` status rows after
all runs: `0`.

**Constraint 2 — every fixture needs the README self-row.** The census glob
includes the README (`:101`, and the selftest asserts it at `:410`), so a
fixture without a self-row emits `C31-1 unindexed-file: ['README.md']`. My
first harness run fired `C31-1` in **8 of 8** cases — the "fake unindexed file"
control passed for the wrong reason. A control must assert the finding's
**detail payload**, not merely its id or the exit code.

**Constraint 3 — the fixture's prose must count the self-row.** `index rows`
includes the self-row, so `Rows` = 1 + drafted rows and `Files` = lessons + 1.
A fixture with correct rows but naive prose is red on `C34b` and looks like a
row defect.

**Constraint 4 — the fixture must mirror the repo's path universe.** The owner
check resolves tokens against `ROOT` (`:151-167`), so a lessons-only fixture
made **37** live owners unresolvable and reported `C32-1` with 37 entries. That
is a false-positive storm an integrator would read as a regression. Symlinking
every repo entry except `corpus/` (and every `corpus/` child except `lessons/`)
removed all 37; the lessons subdirectories must be copied too, because owner
tokens like `corpus/lessons/round-4-audit` resolve to them.

**Constraint 5 — use plain mode, and assert exit 1 plus the id.** See R03-F6.

The eight negative controls and one positive control, all green with payload
equality asserted (run 2026-10-19, repo root):

```
PASS c1-unindexed    want=['C31-1'] got=['C31-1']        # fake file, detail == ['b.md']
PASS c2-ghost        want=['C31-2'] got=['C31-2']        # row for a nonexistent file
PASS c3-prose-lie    want=['C34-2'] got=['C34-2']        # stated [7,7] vs measured [3,3]
PASS c4-stale-pin    want=['C34-1'] got=['C34-1']        # stale sha8 -> detail [a.md,sha8,deadbeef,<live8>]
PASS c5-shape-drift  want=['C34-3'] got=['C34-3']        # format + contract cells stale
PASS c6-bad-owner    want=['C32-1'] got=['C32-1']        # owner path does not resolve
PASS c7-dupe-row     want=['C31-3'] got=['C31-3']        # duplicate row
PASS c8-clean        want=[]        got=[]               # positive: findings 0
RIGOROUS CONTROLS: 8/8 behaved as expected
```

Against O06's three named controls, the gap is concrete: a fake unindexed file
(c1), a ghost row (c2) and a prose lie (c3) leave **`C34-1` and `C34-3`
untested** — and those are precisely the two classes a hand-drafted row trips,
since O01's cells are hand-copied `bytes/lines/sha8/format/contract` values.
`C32-1` (O03's leg) and `C31-3` are likewise uncovered. The positive control is
not optional: without c8 the set proves only that the tool *can* fail, never
that a reconciled tree *passes*.

### 2b. Verdict on the one landed control design (`P01-plan.md:203-225`)

`O06-controls.md` is absent, but P01's plan carries the control table O06 was to
expand (C-pos, C-1..C-6), so I graded that design against my executed evidence.
Two of its choices are right and two have gaps.

Right, and now verified independently:

- **C-5's expectation is correct.** `P01:217` expects a queue row owned
  `orchestrator` to yield `C32-1 unresolvable-owner`. `resolves()` treats only
  `("operator", "parent", "lore-shokunin", "integrator")` as role tokens
  (`c31-lessons-index-audit.py:158`); I loaded the module and measured
  `orchestrator -> (False, 'unresolved')`, `operator/integrator/parent/lore-shokunin
  -> (True, 'role-token')`, and `lead -> (False, 'unresolved')`. So the
  expectation holds — and it also means any new §4 queue row owned `lead` or
  `orchestrator` will fail C32, which O02/O03 need before drafting rows.
- **The partial-mirror C32 noise is already anticipated** (`P01:220-225`, "a
  **partial** mirror also false-fires C32 … Do not present a partial-mirror C32
  red as a defect"). That is my R03-F5, measured independently on a different
  harness — two routes to the same finding.

Gaps:

- **R03-F11 (medium) — the prescribed `git clone` cannot carry the tree under
  test.** `P01:206-208` prescribes `git clone -q . .scratch/<name>/repo`, with
  `C-pos` = "clone of the reconciled tree" (`P01:212`). But `git clone` copies
  committed bytes only, and the reconciled README exists at control time as an
  **uncommitted** working-tree edit (seats do not commit; the integrator commits
  at round close, `claims.json:70`). Measured: `git ls-files reports/round-33`
  → `0`, `git ls-files REGIMEN.md` → `0` — both untracked, so the clone carries
  neither the round-33 tree nor REGIMEN.md. Two consequences: (a) the harness
  must apply the drafted rows **inside** the clone before `C-pos` can be green,
  or the clone must be taken after the integrator's commit — the plan does not
  say which; (b) any owner token naming a `reports/round-33/...` path — which
  O02's new queue rows for the r30–r32 ids may well use, since those ids are
  filed in round-33 fragments — is unresolvable in a clone and produces exactly
  the false `C32-1` storm the plan warns about. My symlink-mirror fixture
  (§3) avoids both, because it mirrors the live tree including untracked files.
- **R03-F12 (medium) — no duplicate-row control.** The table has C-1..C-6 but
  no control for `C31-3 duplicate-row`, even though the edit under test *adds*
  seven rows to an existing table — the merge error this claim is most likely
  to make. `C31-3` is reachable and distinct (my c7: want `['C31-3']`, got
  `['C31-3']`).
- **R03-F13 (low) — payload assertions are uneven.** `C-1` names its payload
  (`['round-99.md']`, `P01:213`) but `C-4` ("change one row's `sha8=`") and
  `C-6` ("change one row's format cell") name only the id. An id-only assertion
  cannot distinguish "the tool caught my mutation" from "the tool caught
  something else in the fixture" — the exact failure my first harness had
  (R03-F4, `C31-1` firing 8/8 for the wrong reason). `C-3`'s expectation is
  also worth pinning as a payload: the tool reports the **measured** pair too
  (`{stated:[32,33], measured:[33,33]}`), so the assertion should carry both.

Adding R03-F12/F13 to the requirement set makes the sufficient design: P01's
C-pos + C-1..C-6, plus a duplicate-row control, each asserting id **and** detail
payload, run on a fixture that mirrors the live tree (untracked paths included).

### 2c. Verdict on `O06-controls.md` — sufficient, with one control that proves nothing

O06 landed mid-review and delivers **11 controls (C0–C9)**, well past the
mission's minimum of three. I verified it independently rather than reading its
receipt:

- **The embedded harness is real and extractable.** O06's §6 recipe
  (`O06:606-613`) extracts exactly one `python` fence; my extraction's digest is
  `1263f15686ce2662669e8a2b9d21222b2424d117a7e057fa72085bc8262a0d2d` — byte-equal
  to the pin at `O06:617`. So the controls can be re-run by the integrator
  byte-identically, and the §5 bytes are not merely illustrative.
- **It reproduces.** My run of the extracted harness prints
  `CONTROLS OK: 11/11 controls behaved as specified`, exit 0, matching `O06:94-110`
  line for line (baseline `exit=1 checks_failing=['C31_index_rows_eq_files',
  'C34b_prose_arithmetic'] findings=['C31-1','C34-2']`).
- **Its citations are accurate.** Every tool line range in its §1 table
  (`O06:24-31`, `:35-39`) checks out against the tool I read: C31-1 `:201-203`,
  C31-2 `:204-206`, C31-3 `:208-210`, C32-1 `:213-227`, C33-1 `:229-243`,
  C34-1 `:245-266`, C34-3 `:268-291`, C34-2 `:293-317`, `--json` `:445-447`,
  plain exit `:460`.

**Sufficiency: met.** O06 closes every gap I had derived independently —
R03-F3 (its §2 sandbox copies `corpus/lessons` and symlinks the rest, so no live
byte is written and owner paths still resolve), R03-F4 (the delta model plus C0
makes the "fired for the wrong reason" failure impossible by construction, a
stronger answer than payload assertions alone), R03-F5 (`O06:214-222` mirrors the
owner-path universe explicitly), R03-F6 (C8 pins the `--json` trap),
R03-F12 (C3 duplicate-row), R03-F13 (`classes` + `detail_has`). It also carries
**three** positive controls where I had one: C0 identity, C5 mechanical
reachability, C9 end-to-end on O01's real draft. C9 reproduced my §3 result
(findings `[]`, exit 0 on O01's seven rows) through a different harness — two
independent routes to the same verdict.

**R03-F14 (low–medium) — C4a is non-discriminating pre-integration, and its
filed `[PASS]` overstates it.** I probed the extracted harness by disabling one
mutation at a time while leaving every assertion intact:

```
C1  fully disabled (no probe file created)  -> [FAIL]  (discriminating)
C4b disabled (no queue-prose rewrite)       -> [FAIL]  (discriminating)
C4a disabled (no table-prose rewrite)       -> [PASS]  (proves nothing)
```

Cause, both halves of C4a's expectation are already true at the red baseline: its
expected id `C34-2` is in `BASELINE["ids"]`, and its `detail_has` substring
`table_rows_vs_files` is already present in the baseline detail
`{"table_rows_vs_files": {"stated": [26, 26], "measured": [26, 33]}}`. So C4a
passes whether or not its mutation fires. O06 discloses the general limitation at
`O06:645-647` ("C4a/C4b are discriminating only when the baseline is green … the
control cannot isolate its own mutation"), but §4's receipt — the filed evidence —
prints a plain `[PASS]`, so a reader of §4 alone cannot tell that C4a proved
nothing at the pre-integration stamp. **R03-F15 (informational)** records the fix
model: C4b discriminates precisely because its `detail_has` key `queue_rows` is
*absent* from the baseline detail — pinning a value the baseline cannot carry is
what makes a control discriminating. C4a should either pin the lie's own stated
pair (derived from the measurement, as C4a already computes it) or have its
receipt line annotated "non-discriminating pre-integration". Post-integration the
baseline is green and C4a becomes discriminating on its own, so the defect is
confined to the pre-integration receipt being filed as evidence.

This does not change any control's post-integration verdict, and no other control
is affected: C1, C2, C3, C4b, C6, C7, C8 all flip red when their mutation is
disabled, and C0/C5/C9 are positive controls by construction.

## 3. The target state is reachable — the control that matters most

The claim-O after-requirement is "33/33 rows, audit exits 0, zero findings". I
tested that directly rather than trusting the drafts: a fixture copy of the live
33 lesson files plus the live README, with O01's seven drafted rows inserted at
the declared point (`O01:49-62`, after the round-25 row) and the single prose
cell corrected per `O01:120-121`, run through the relocated tool of record:

```
lesson files:  33      index rows: 33      queue rows: 49
  PASS C31_index_rows_eq_files      PASS C32_owners_resolve
  PASS C33_formats_documented       PASS C34_pins_rederived
  PASS C34c_shape_cells_rederived   PASS C34b_prose_arithmetic
findings:      0       exit=0
```

An independent second route (`sha256sum` + `wc` over the seven files) agrees
with O01's pins on **7/7** rows, and K02's independent census agrees with O01 on
the same 7/7 pins and on all seven format/contract cells (`K02:50-56`,
`K02:62-68`) — so the pin control has two independent corroborations. Live
`corpus/lessons/README.md` was never written: digest still `ec7469da…`, status
rows `0`.

## 4. Cross-fragment findings

- **R03-F9 (low) — O01/K02 disagree on the disposition-pointer cell** for two
  of the seven rows, and both paths exist so neither is a broken pointer:
  r30 — `O01:59` names `reports/round-30/validation.json` **and**
  `reports/round-30/routed-resolution.json`, `K02:54` names only the latter;
  r32 — `O01:61` names `reports/round-32/validation.json`, `K02:56` names
  `reports/round-32/completion-ledger.json`. The tool does not machine-check
  that column (its checks cover column 1, `bytes/lines/sha8` and the
  format/contract cells), so nothing will catch the divergence automatically.
  The integrator needs one named rule (recommendation: the cell should name the
  round's `validation.json` as the acceptance artifact, with any additional
  ledger appended after it, matching the existing rows' shape).
- **R03-F10 (informational) — R03-F1 is confined to O07.** `grep -n "scope\.md"
  reports/round-33/op/*.md` returns three hits, all in
  `O07-baseline-receipt.md` (`:121`, `:123`, `:198`); O08 does not inherit the
  dead pointer. Fixing O07's two lines before S01 folds it forward is
  sufficient.

## 5. Findings by severity

| id | sev | target | finding |
|---|---|---|---|
| R03-F1 | medium | `O07:121,198` | `reports/round-32/scope.md:13` is blank; the 1,870 claim is at `:10` |
| R03-F3 | medium | `O06:41-50` | controls cannot run on the live tree — no corpus-redirect flag; sandbox/relocated copy required (**met** by O06 §2) |
| R03-F4 | medium | `O06:52-63` | missing README self-row makes `C31-1` fire in 8/8 of my fixtures — assert payload, not id (**met** by O06's delta model + C0) |
| R03-F5 | medium | `O06:214-222` | lessons-only fixture yields 37 false `C32-1` findings; fixture must mirror the repo path universe (**met**) |
| R03-F11 | medium | `P01:206-212` | `git clone` cannot carry the reconciled README (uncommitted) nor any untracked round-33 path — `git ls-files reports/round-33` → 0 |
| R03-F12 | medium | `P01:210-218` | no duplicate-row control for `C31-3`, though the edit adds seven rows to an existing table (**met** by O06's C3) |
| R03-F14 | low–medium | `O06:73`, `:422-428` | C4a reports `[PASS]` with its mutation disabled — non-discriminating pre-integration; pin a value the baseline cannot carry, or annotate the receipt |
| R03-F2 | low | `O07:123` | `:21-24` supports the premise; the 1,735 + 135 arithmetic is at `:29` |
| R03-F6 | low | `O07` / validator | `--json` exits 0 unconditionally (`c31-…-audit.py:447`); pipe-masked exit codes (**pinned** by O06's C8) |
| R03-F7 | low | `O07:71-79` | no `python3 -V` (3.14.7) pinned for a receipt meant to be re-run |
| R03-F8 | low | `O07:71-79` | `check-evidence-coupling.py` exercised but not digest-pinned |
| R03-F9 | low | O01/K02 | disposition-pointer cells diverge on r30/r32; both paths exist; needs a named rule |
| R03-F13 | low | `P01:216,218` | C-4/C-6 expectations name only the id; assert the detail payload (and C-3's measured pair) (**met** by O06's `classes`/`detail_has`) |
| R03-F15 | info | `O06:74`, `:442-448` | C4b's discriminating power comes from a detail key absent from the baseline — the model C4a should copy |

No finding falsifies a measurement in O07: all 8 digests, all 4 exit codes, the
battery summary, the c31 before-state and the scope counts reproduce exactly as
filed. R03-F1/F2 are pointer repairs, R03-F7/F8 are two added provenance lines,
and R03-F3/F4/F5/F12/F13 are design constraints O06 has since met — none requires
a filed byte to be rewritten. R03-F14 is the one finding that survives O06's
landing, and it is confined to that fragment's pre-integration receipt.

Two P01 choices are independently confirmed rather than faulted: `C-5`'s
`orchestrator`-is-unresolvable expectation (`P01:217`), measured against
`resolves()`; and the partial-mirror `C32` warning (`P01:220-225`), which is
R03-F5 reached by a second route. O06 supersedes P01's control table for
execution purposes (11 controls vs P01's 7), so R03-F11/F12 are recorded against
P01 as written, not as a gap in the round's delivered controls.

## Owed: none

`op/O06-controls.md` landed mid-review and its verdict is delivered in §2c, so
the item this review was prepared to owe is discharged. Nothing else in my focus
is owed: O07 is graded in §1, the controls in §2/§2b/§2c, and the target-state
proof in §3. O02's `readme-delta` content (the queue rows and Revision-3 prose)
is outside this seat's focus and belongs to R01/R02.

## Citations

- `reports/round-33/op/O07-baseline-receipt.md:14-15,19-25,31-34,38-45,46-48,49-51,52-63,71-79,81,96-101,103-116,121,123,126-127,128-133,136-142,198`
- `reports/round-33/op/O01-row-drafts.md:49-62` (drafted rows), `:91-103` (six-file filed pin agreement), `:120-121` (prose cell), `:175-186` (owed cross-checks)
- `reports/round-33/op/K02-lessons-census.md:50-56` (per-file cells), `:62-68` (sha256 re-measurement)
- `reports/round-33/op/P01-plan.md:203-225` (control table C-pos/C-1..C-6), `:212` (C-pos = clone of the reconciled tree), `:217` (C-5 `orchestrator` expectation), `:220-225` (partial-mirror C32 warning), `:229` (baseline before any edit)
- `reports/round-33/op/O06-controls.md:10-13` (11 controls), `:17-18` (read-only tool), `:24-31` (finding/class/line table), `:33-39` (exit contract), `:41-50` (sandbox + `__file__` root), `:52-63` (C0 identity + delta model), `:67-79` (control table), `:91-111` (verified run), `:113-128` (observed details + digests), `:606-622` (integrator run recipe + digest pin), `:624-657` (expected post-edit shape + interpretation rules), `:674-688` (limits, incl. §6 rule 1 at `:645-647`)
- `reports/round-33/claims.json:23-31` (claim O), `:25` (declared before-state), `:37` (threshold naming the O07 receipt)
- `reports/round-33/targets.json:27` (O06 mission/out), `:28` (O07 mission/out), `:67` (this seat), `:5-11` (shared rules)
- `reports/round-33/telemetry/dispatch-declared.json:17-26` (`durable_sources[]` digests)
- `reports/round-25/audit/c31-lessons-index-audit.py:34-35` (ROOT/LESSONS from `__file__`), `:42,45` (ROW_RE/CELL_RE), `:101` (census glob), `:151-167` (`resolves`), `:213-227` (C32), `:250-266` (C34), `:271-291` (C34c), `:296-317` (C34b), `:410` (README-in-census selftest), `:445-447` (`--json` returns 0), `:460` (plain-mode exit)
- `reports/round-32/scope.md:10` (1,870 statement), `:23` (protected-surface prose), `:29` (1,870 = 1,735 + 135), `:13` (blank — the dead pointer)
- `corpus/lessons/round-28.md:86` (filed index digest `ec7469dadf87df3e…`)
- commands (2026-10-19, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `python3 tools/check-gate-battery.py --selftest`; `python3 tools/check-gate-battery.py`;
  `python3 tools/check-craft-exercise.py --selftest`; `python3 tools/assemble-culture-d4.py --selftest`;
  `python3 tools/assemble-culture-d4.py --check`; `python3 tools/check-evidence-coupling.py --selftest`;
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py [--selftest|--json]`;
  `python3 -B .scratch/r03-controls/rigorous-controls.py` (8/8, output in §2);
  `python3 -B .scratch/r03-controls/target-state-check.py` (findings 0, output in §3);
  `bash .scratch/r03-controls/run-controls.sh` (first, confounded pass — evidence for R03-F4);
  `python3 -V`; `date -u +%Y-%m-%dT%H:%M:%SZ`; `git rev-parse HEAD`; `git status --porcelain [corpus/lessons]`;
  `git diff --stat LOG.md`; `git ls-files | wc -l`; `git ls-files | grep -c '^reports/round-'`;
  `sha256sum` over the four tools, `corpus/lessons/README.md`, `reports/round-33/claims.json`,
  `reports/round-33/targets.json`, `reports/round-33/telemetry/dispatch-declared.json`;
  `awk 'NR==13' reports/round-32/scope.md`; `grep -n "1,870\|1870" reports/round-32/scope.md`;
  `grep -rln "lessons/README\|corpus/lessons" tools/gates/expected tools/gates/frozen tools/gates/*.py`;
  `grep -n "scope\.md" reports/round-33/op/*.md`; `ls -la --time-style=+%H:%M:%S reports/round-33/{,op/,telemetry/}`;
  `git ls-files reports/round-33 | wc -l` and `git ls-files REGIMEN.md | wc -l` (both `0` — untracked, evidence for R03-F11);
  `python3 -B -c` loading `reports/round-25/audit/c31-lessons-index-audit.py` via `importlib` and printing
  `resolves()` for `orchestrator/operator/integrator/parent/lore-shokunin/lead` (evidence for §2b);
  `grep -n -i "control\|negative" reports/round-33/op/P01-plan.md`;
  O06 harness extraction + digest check (`python3` regex over the single ```python fence; `sha256sum .scratch/o06-controls.py` → `1263f156…`);
  `python3 -B .scratch/o06-controls.py --receipt .scratch/r03-o06-receipt.json` → `CONTROLS OK: 11/11`, exit 0;
  `python3 -B .scratch/r03-controls/o06-noop-probe.py` (C4a/C4b mutations disabled → C4b `[FAIL]`, C4a `[PASS]`);
  `python3 -B .scratch/r03-controls/o06-c1-probe.py` (C1 mutation disabled → `[FAIL]`)
- scratch (this seat's own, gitignored): `.scratch/r03-controls/{rigorous-controls.py,target-state-check.py,run-controls.sh,o06-noop-probe.py,o06-c1-probe.py,rig/,cases/,target-state/}`; plus O06's harness re-extracted per its §6 recipe to `.scratch/o06-controls.py` and its receipt `.scratch/r03-o06-receipt.json`
