- Seat: R05 | reviewer | claim C | date 2026-10-19 | baseline 139e3b6

# R05 — second adversarial pass over `calib/`: K03's twelve-item canonicalization

Mission (targets.json R05): second pass over `calib/` with focus on K03's
twelve-item canonicalization — does it match the dossier's own enumeration,
and what is the count's provenance?

**Dependency state at this seat's cut (2026-10-19T03:49–03:57Z):**
`reports/round-33/calib/` is **empty** — K03's fragment and every C01–C16
fragment are absent. Per the missing-dependency rule this review does the part
that does not depend on them: it re-derives the count from the two source
dossiers directly, re-verifies all nine pointers at HEAD, and states the
falsifiable checks K03/C15 must satisfy when they land. The K03-dependent
verdicts are owed, not guessed.

## 1. Headline finding — the dossier's own enumeration is 9 rows; "12" is inherited, never derived

The claim title reads "the twelve standing open items" (claims.json:42). Four
independent places enumerate the same set, and **all four enumerate nine
items**:

| where | enumerates | count |
|---|---|---|
| `reports/round-32/dossier-d13-operator-decisions.md:130-138` (Decision 4 table, 9 data rows) | 12 GAR holds · `head2` · RL-3 · box-1 conds 2-4 · cold-run N1/N4/N5/N7 · lore-owned · rubric · devin · r18 supersession | **9** |
| `reports/round-33/claims.json:44` (claim C's own `before.items` parenthetical) | identical list, same order | **9** |
| `reports/round-32/scribe/fragment-ledger.md:213-216` (the parenthetical inside the sentence calling it "twelve-item") | identical list | **9** |
| `reports/round-32/dossier-d11-shonen-boxes.md:205-208` (summary "open at HEAD" cells, atomic reading) | 3 + 3 + 4 + 3 | **13** |

The assertions of twelve are three, and none carries a derivation:

- `reports/round-33/claims.json:42` — "Disposition the twelve standing open items".
- `SCORECARD.md:444-445` — "12 standing open items in the dossier" (the filed
  round-32 record; this is the phrase claim C's `before` quotes).
- `reports/round-32/scribe/fragment-ledger.md:212` — "D13's twelve-item
  open-debt table", whose **own enumeration three lines later lists nine**
  (`:213-216`). The label and its enumeration disagree inside one paragraph.

**The only literal "12" in D13 is the garment-hold count**, not an item count:
`dossier-d13:130` `| 12 D4 garment-form holds + owed slots |`. That number is
independently measured and confirmed at HEAD (see §3, row 1). The
"twelve" in the claim and in SCORECARD is therefore best explained as the
garment-hold numeral propagated into a position where it reads as a table-row
count — **a count conflation, not a count**. This is `to-verify` as intent (no
source states the derivation); it is measured as text.

### 1.1 Which counting rules actually reach 12

Every candidate rule, tested against the sources:

| # | counting rule | yields | sourced? |
|---|---|---|---|
| a | D13 Decision 4 data rows, as written | 9 | yes — `dossier-d13:130-138` |
| b | (a) + D11 box-4 standing readings 3a/3b/3c | **12** | no — and D11 says those readings are "not defects" (`dossier-d11:176-181`), so including them contradicts the dossier's own class boundary |
| c | (a) with the cold-run row expanded into N1/N4/N5/N7 | **12** | no — the row is written as one row (`dossier-d13:134`) |
| d | (a) with box-1 conditions expanded into 2/3/4 | 11 | no |
| e | (a) with lore-owned expanded into its two halves | 10 | no |
| f | (c) + (e) together | 13 | no |
| g | D11 summary cells counted atomically | 13 | no — and counts box-4 readings as open items |
| h | the numeral read literally | 12 **garment holds** | yes — but it is not an item count |

Exactly two rules reach 12, they are unstated anywhere in the corpus, and they
select **different item sets**: (b) keeps N1/N4/N5/N7 as one item and adds the
three standing readings; (c) drops the readings and carries four cold-run
items. So "the 12" does not identify a set — a ledger built to 12 under (b)
and one built under (c) are both "the 12" and share only 8 rows.

### 1.2 Consequence for claim C as declared

Claim C's after_required: "open-items-ledger.json rows == K03's canonicalized
12 (cross-checked against SCORECARD's '12')", and its counting command is
`run-validation.py` with "ledger row count == 12". As written that leg is
**satisfiable by back-filling**: any self-consistent 12 passes, and the leg
cannot distinguish a sourced count from a label-matched one. K03 cannot
canonicalize 12 *from the dossier* without inventing the rule; the honest
options are (i) declare the rule and show it sourced, or (ii) file the
mismatch as a named finding and reconcile to 9 + a named expansion.

## 2. Pointer re-verification for all nine D13 rows at HEAD

Claim C requires "status-quo pointer re-verified at HEAD" per row. Pre-computed
here so C01–C12 and C13 can cross-check rather than re-derive. HEAD =
`139e3b662900557afe54f632b468619593dc9fcb` (2026-10-19).

| # | row (D13:line) | pointer as filed | verdict at HEAD | measured detail |
|---|---|---|---|---|
| 1 | 12 D4 garment-form holds (`:130`) | `reports/round-24/box2-d4.md:104-108` | **resolves, exact** | F3 note is exactly at `:104-108`; live count confirmed: `examples/culture-d4/expected-holds.json` holds = **12**, all 12 distinct GAR labels (`GAR-01..06`, `LEX-GAR-01..06`) |
| 2 | `head2` empty proper domain (`:131`) | `reports/round-26/register/` named gaps | **resolves, directory-level** | exact finding is `reports/round-26/register/review.md:99` §4 "Finding RD-3"; corroborated `design.md:228` (RL-2 row), `rules.md:89` §3.2 |
| 3 | RL-3 ceiling (`:132`) | "ceilings knowledge entry" (a description, not a path) | **resolves only by search** | `corpus/knowledge/linguistics/register-lexicon-ceilings.md`; its `KTD-RLC-S-0001` cites `reports/round-27/law/design.md` §3.2 + `review.md` §4 for RL-3. Row 3 needs a path in the ledger |
| 4 | box-1 citation conditions 2-4 (`:133`) | `promotion-review.md:71-88` | **resolves, exact** | conditions 2, 3, 4 at `:71-84`; condition 5 also inside the range |
| 5 | cold-run N1/N4/N5/N7 (`:134`) | `promotion-review.md:176-196` | **resolves, exact** | N1 `:178`, N2 `:180`, N3 `:183`, N4 `:186`, N5 `:189`, N6 `:191`, N7 `:193` |
| 6 | lore-owned (`:135`) | "L0 queue; handoff contract" (descriptions) | **resolves, paths implicit** | fleet `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44-47` (four kotodama rows; the contract-digest item is `:45`); `corpus/knowledge/synthesis/worldbible-integration-contract.md:15-16` (bilateral acknowledgement pending; digest change requires both-lane re-read). Needs explicit paths in the ledger |
| 7 | rubric gap (`:136`) | `SCORECARD.md` header | **resolves, exact** | `SCORECARD.md:13-14` "defining a calibrated numeric rubric remains an explicit protocol-conformance gap" |
| 8 | devin could-not-evaluate (`:137`) | `reports/round-29/recount/` | **resolves, but not the canonical artifact** | canonical disposition is `reports/round-29/devin-availability-disposition.md`; the census is `reports/round-29/recount/dispositions.md:22` and `audit.md:18`. **Label overstates**: the filed state is `launched_workers`/`completed_workers` = `null` with clean populations recorded (R25 113/113, R26 171/171, R27 147/147, R28 151/151) — `recount/audit.md:18` explicitly says the census "does not establish that 64 worker processes were launched" |
| 9 | r18 supersession semantics (`:138`) | `final-sweep.md` §5 | **resolves, exact** | `reports/round-31/final-sweep.md:183-190`: "The D4 adapter baselines were not re-pinned … whether their *content* still matches the live packet is the pins' supersession semantics" |

No pointer is dangling. Three rows (2, 3, 6) name a directory or a description
rather than a `path:line`; two rows (3, 6) cannot be resolved without a search.
That is a fixable ledger-quality defect, not a count defect.

## 3. Named finding — condition N2 is firing live, and D11 understates it

Severity: **high** (conformance / append-only discipline). Owner: integrator
(attribution `to-verify`). Not repaired by this seat: restoring filed bytes and
any `git restore` are the integrator's surface.

**Observed.** During this review, inside round 33's window:

- round-33 declaration: `claims.json:6` `2026-10-19T03:49:01Z`.
- receipt mtimes (UTC): `reports/round-5/validation.json` **03:54:15Z** then
  **03:55:27Z**; `reports/round-6/validation.json` **03:54:32Z**;
  `reports/round-7/validation.json` **03:54:18Z** then **03:55:27Z**.
- at 03:55:05Z `git status --porcelain` read ` M reports/round-5/validation.json`
  and ` M reports/round-7/validation.json`; `git hash-object` gave worktree
  `5227945d4548ad12d54527a12ce5d96de767281f` (r5) and
  `d583aad5e32f575cf0f5f6b0d88eddc37f8103de` (r7) against HEAD
  `778c3f5e172405d73eab790b8d6fee4c3282caa0` and
  `e7a8d449a9c154219931601264b4fa54ff408bc7`.
- the changed content (captured from `git diff`; the mutated blobs were never
  written to the object store, so this transcription is the surviving record):
  - r5: `tested_file_sha256["tools/check-gate-battery.py"]`
    `0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1` →
    `455b595ad6d5b1be7844fc9b53a259a5b8a0efbd788b129dbfd2cc0d0ad173ce`
    (the live tool hashes to `455b595a…`, measured — so the rewrite recorded
    the live bytes over a filed stale reading); and the `O` leg's `error`
    string changed from `tools/check-gate-battery.py … got 2` to
    `tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv … got 2`
    (`REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch, 0 reproduced`).
  - r7: one failure row, `inventory: historical knowledge totals changed`,
    `{files: 189, raw_lines: 688, raw_occurrences: 700, ci_occurrences: 702,
    marker_occurrences: 633}` → `{files: 201, raw_lines: 717,
    raw_occurrences: 731, ci_occurrences: 733, marker_occurrences: 655}`.
  - `acceptance_checks_passed` unchanged in both (`false`); r6's rewrite was
    byte-identical (worktree blob `9f6a0f45f96e…` == HEAD).
- by 03:56:13Z all three receipts were byte-identical to HEAD again; a
  four-sample window 03:56:13–03:56:49Z read stable sha256
  `73a66f7464ead0d9…` (r5), `32c621efaccca71d…` (r6), `2f4c1e159b60d782…` (r7),
  each equal to the HEAD blob's sha256. Current `git status --porcelain` shows
  only ` M LOG.md` plus untracked `REGIMEN.md` and `reports/round-33/`.

**Mechanism (measured).** The three acceptance scripts write their own filed
receipt in place: `reports/round-5/run-validation.py:194`,
`reports/round-6/run-validation.py:336`, `reports/round-7/run-validation.py:1171`
(`(HERE / "validation.json").write_text(...)`). **None of them imports
`receipt_guard`** (`grep -c receipt_guard` → 0, 0, 0), the guard that
`SKILL.md:453` documents as "rejects committed-receipt writes by default".
So D11's box-3 line "**N2 — machinery documented**"
(`dossier-d11:141-144`) **understates the state**: the guard covers the
harness receipt path, not these three scripts, and the scripts demonstrably
fired.

**Why it matters to claim C.** (a) It is condition **N2** — a row of the very
ledger this claim must disposition — appearing in fact, not merely on record;
"N2 documented" must not be dispositioned `fixed-with-evidence`. (b) Claim C's
threshold says "no filed bytes edited by seats": at close, a bytes-only check
passes (end state is byte-clean) while an **mtime** check fails — and the
round-32 scope-watch convention measures exactly that
(`reports/round-32/scope.md:10` "0 tracked mtimes newer than the declaration").
(c) Attribution is unresolved: **no round-33 seat is assigned to run the
round-5/6/7 acceptance** (targets.json contains no such mission; A07's re-runs
are the r21/r29 adjacency commands). The actor is `to-verify`.

**Recommended disposition (integrator):** file the incident as a named finding
with this evidence, record the mtime residue, and decide explicitly between
"transient, restored, bytes clean" and "append-only violation" — the honest
reading of the round's own rule is the latter for the interval 03:54:1xZ →
~03:56Z, since byte-identity on restore does not unmake the write. No restore
command is issued here because the tree is already byte-clean; if the
integrator wants a belt-and-braces byte check, the targets are the HEAD blob
SHAs above.

## 4. Falsifiable checks for K03/C15 when they land

Mechanical, so a verifier (A14-style) or the integrator can run them without
re-reading this review:

1. **Counting rule declared.** `calib/K03-open-items.md` contains an explicit
   rule sentence of the form "N items = X table rows + Y named expansions",
   and X, Y and the expansion names are each traceable to a source line.
   Fails if the rule is absent or if it is "12 (as filed)".
2. **Reconciliation line present.** K03 states the D13 table row count (9) and
   the delta to its own count, with the delta's items named. A K03 that
   reports 12 without mentioning 9 has not reconciled.
3. **Label-match independence.** The item set must be derivable from the
   dossiers without consulting SCORECARD.md:444. Check: K03's rule applied to
   `dossier-d13:130-138` alone reproduces its list.
4. **Ledger row count == K03's count**, and every row's `origin` names a
   round that appears in D13's "on record since" column (`r5`, `r8/r15`,
   `r18`, `r24`, `r26`, `r27/r28`, `r29`, `r31`).
5. **Pointer quality**: rows 3 and 6 of §2 above must carry a `path` (not a
   description); rows 2 and 8 should carry the canonical artifact
   (`round-26/register/review.md:99`; `round-29/devin-availability-disposition.md`).
6. **Row 8's label corrected**: "devin availability could-not-evaluate" should
   read as launch/completion counters null, clean populations recorded
   (`recount/audit.md:18`), or be carried with that qualifier.
7. **Row 1's arithmetic**: state 12 holds / 6 owed garment forms
   (`box2-d4.md:104-106`), or the row is a partial restatement.
8. **The count-conflation finding is either fixed or carried**: if the
   integrator corrects `SCORECARD.md:444` (shared file, integrator-applied) the
   correction must be an append-style errata, not a silent rewrite of the
   filed round-32 record.

**Proposed validation leg for `run-validation.py` (for S04/the integrator):**
besides "ledger rows == 12", require `open-items-ledger.json` to carry a
`counting_rule` field and a `reconciliation` object naming the source row
count and the expansions, and require the leg to fail when `counting_rule` is
absent. Without it, the current leg cannot fail for the reason this review
found.

## 5. What this seat did not do

- Did not run `reports/round-{5,6,7}/run-validation.py` (that would reproduce
  the §3 write), did not restore any byte, ran no git-mutating command.
- Did not re-execute the pointer targets' internal commands; §2 verifies
  pointer **resolution and line accuracy**, not the verdicts behind them.
- Attribution of the §3 writes is `to-verify`; this seat names the mechanism
  and the window, not the actor.
- §1–§4 were written before K03 landed (calib/ empty at 03:49–03:57Z); §6 is
  the conformance pass over it, run after it appeared at 03:55Z.

## 6. K03 conformance pass (K03 landed at 03:55Z, read in full, 131 lines)

**Mission question — does K03's canonicalization match the dossier's own
enumeration? No, and K03 says so.** K03 independently measured the same fact
this seat did: `K03:26-30` runs the same command
(`sed -n '130,138p' … | grep -c '^|'` → `9`) and concludes "So '12' is not a
literal row count of the table; it is a count over the items the table names,
under some expansion convention that the dossier never states." Its `to-verify`
flag on the numeral's origin (`K03:45-53`) is correct, and its diagnosis of the
likely contamination path (the first row's own "**12** D4 garment-form holds")
matches §1 above, reached independently. **Two seats, two methods, one
finding.**

K03 also surfaced two provenance assertions this seat had not found:
`LOG.md:3513` ("12 standing open items in the dossier") and
`reports/round-32/final-dossier.md:107-110` ("**Twelve named items** tabled
with origins and pointers — … design debts (12 garment holds, head2, RL-3),
the r24 citation/cold-run conditions, lore-owned items, the rubric gap,
devin-telemetry could-not-evaluate, adapter-baseline supersession semantics").
The tally is now **five assertions of twelve** (claims.json:42, SCORECARD:444,
fragment-ledger:212, LOG.md:3513, final-dossier.md:107) against **five
enumerations of nine** (dossier-d13:130-138, claims.json:44,
fragment-ledger:213-216, final-dossier.md:108-110, K03:36) — including the
final dossier, which prints "Twelve" and then lists nine groups in the same
sentence, exactly as the scribe ledger does.

**Pointer quality: passes.** Every one of K03's twelve pointers was re-verified
here at HEAD and every line range is accurate — `box2-d4.md:104-108`,
`register/design.md:228`, `register/rules.md:89-95`,
`register-lexicon-ceilings.md:6`, `promotion-review.md:71-76/:77-80/:81-84`,
`dossier-d11:53-58/:59-63/:64-68`, `promotion-review.md:178/:186/:189/:193`,
`dossier-d11:145-153`, `worldbible-integration-contract.md:7,15,16`,
`reports/round-15/handoff/contract-v2-audit.md:31,48` (digest `5f…`; "the
outstanding bilateral same-revision read is stated, not asserted complete"),
`.ufo/l0-questions.md:44,45`, `SCORECARD.md:13-14`,
`recount/dispositions.md:22`, `recount/audit.md:18`, `final-sweep.md:187-192`.
K03 also **improves on D13** in two places: OI-11 restates the devin item
honestly ("launched/completed counters null; seat-marker totals are not launch
receipts"), repairing D13's overstatement; OI-01 carries "12 holds + the six
owed form slots", repairing D13's flat "12 holds". All three convention
arithmetics (9 / 15 / 12) are arithmetically correct, and the re-merge
instruction at `K03:51-53` (12 − 3 = 9) is correct.

**Defects, severity-ranked:**

- **R05-C-1 (medium-high — the rule does not select the set).** K03's adopted
  convention (`K03:38`) says "expand only where the dossier itself enumerates
  distinct conditions **with distinct fixes** (box-1 conditions 2/3/4 → 3 rows;
  lore-owned → 2 rows); keep the cold-run set as the one filed row it is". The
  rule is applied asymmetrically: `promotion-review.md:178-193` enumerates
  N1/N4/N5/N7 as **four numbered conditions each with its own remedy** (N1 dated
  expected-verdict errata, N4 a real artifact set / handoff path, N5 the
  history-retaining wording, N7 the executable-surface pinning), and
  `dossier-d11:145-153` lists them individually — the same evidence pattern K03
  uses to justify splitting box-1. The discriminator K03 cites for not
  splitting (`dossier-d11:207` groups the cold-run set in one cell) is
  **symmetric**: `dossier-d11:205` groups box-1 in one cell ("conditions 2, 3,
  4") too. **Applying K03's own rule uniformly yields 15 — K03's own "maximal"
  convention — not 12.** The number 12 is therefore selected backwards from the
  filed label; the `to-verify` disclosure at `K03:45-53` does not name this
  specific inconsistency. Fix is cheap and textual: either restate the rule as
  "expand the two rows D11 splits and keep the cold-run cluster merged, for
  filed-count parity" (an honest parity convention) or adopt 15.
- **R05-C-2 (medium — falsified uniqueness claim).** `K03:42-43`: "This is the
  only convention that both includes all 9 D13 rows and lands on the filed
  '12'." **Counterexample:** expand *only* the cold-run row into N1/N4/N5/N7 and
  leave box-1 and lore-owned merged → 6 single rows + 1 box-1 + 4 cold-run +
  1 lore-owned = **12**, all 9 rows included. A second counterexample exists
  (§1.1 rule b, 9 rows + D11's box-4 readings) if K03's sourced box-4 exclusion
  (`K03:88`) is relaxed. The honest phrasing is "one of at least two
  conventions reaching 12, and the one adopted here".
- **R05-C-3 (high — cross-finding, reason falsified).** `K03:86` excludes
  cold-run N2 because "`dossier-d11:140-144` records the receipt guard as
  documented machinery". **§3 above falsifies that reason by measurement**: the
  three acceptance scripts import no guard (`grep -c receipt_guard` → 0, 0, 0)
  and rewrote filed receipts inside round 33's window. The exclusion still
  stands on the narrow ground that D13's row names only N1/N4/N5/N7
  (`dossier-d13:134`), but the stated reason must be replaced and N2 filed as a
  **new** open item outside the twelve — not silently excluded. This is the
  point where claim C's ledger and §3 must meet.
- **R05-C-4 (low — pointer completeness).** OI-02 cites
  `register/design.md:228` and `rules.md:89-95`; the finding's own location is
  `reports/round-26/register/review.md:99` (§4 "Finding RD-3"), where the
  "59 of 62" measurement is worked. Both cited lines do carry the count, so this
  is completeness, not error.

**Operative verdict for claim C.** The ledger may land 12 rows **only** if the
round declares the expansion rule as its own convention (K03's rule text
repaired per R05-C-1) and the validation leg carries `counting_rule` +
reconciliation per §4; otherwise the honest landing is 9 rows plus a named
finding, with `SCORECARD.md:444` corrected by append-style errata naming all
five "twelve" assertions. A 12-row ledger assembled to K03's table without
that repair would pass the declared counting command while resting on a rule
its own source contradicts — which is precisely the failure mode §1.2
predicted.

## Owed

- `reports/round-33/calib/C01..C12-item-*.md` — present for C01/C03/C07/C11/C12
  at this cut (03:58Z), absent for C02/C04/C05/C06/C08/C09/C10; §2's pointer
  table and §4's checks are pre-computed for them. Per-item verdicts are not
  this seat's mission (R04 covers C01–C12).
- `reports/round-33/calib/C13-consistency.md`, `C14-fix-drafts.md`,
  `C15-ledger-draft.json` — absent at cut. §6's R05-C-1..C-3 are the checks C13
  and C15 must carry; the ledger's `counting_rule`/`reconciliation` fields
  (§4) are the concrete ask.
- `reports/round-33/calib/open-items-ledger.json` — the artifact claim C's
  counting command names; not present at this cut, so the "rows == 12" leg is
  unprovable as of 03:58Z.

## Citations

Commands (all run from the lane root, `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`, 2026-10-19 unless stated):

- `awk 'NR>=130 && NR<=138' reports/round-32/dossier-d13-operator-decisions.md`
  → 9 data rows.
- `python3 -` over `examples/culture-d4/expected-holds.json` → total holds 12,
  12 distinct GAR labels (`GAR-01..06`, `LEX-GAR-01..06`).
- `grep -n "standing open items\|standing open\|12 " SCORECARD.md` → `:444-445`.
- `grep -rn "12 standing\|twelve" reports/round-32/` → `scribe/fragment-ledger.md:212`.
- `awk 'NR>=203 && NR<=208' reports/round-32/dossier-d11-shonen-boxes.md` → summary cells.
- `awk 'NR>=98 && NR<=115' reports/round-24/box2-d4.md` → F3 note `:104-108`.
- `awk 'NR>=71 && NR<=88'` / `NR>=176 && NR<=196` `reports/round-24/promotion-review.md`.
- `grep -n "head2" reports/round-26/register/` → `review.md:99`, `design.md:228`, `rules.md:89`.
- `grep -n "RL-3\|ceiling" corpus/knowledge/linguistics/register-lexicon-ceilings.md` → `:6`.
- `grep -n "rubric" SCORECARD.md` → `:13-14`.
- `grep -rn "devin" reports/round-29/` → `recount/dispositions.md:22`, `recount/audit.md:18`, `devin-availability-disposition.md`.
- `awk 'NR>=183 && NR<=190' reports/round-31/final-sweep.md` → §5.
- `grep -n "kotodama" /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` → `:44-47`.
- `grep -n "bilateral\|digest" corpus/knowledge/synthesis/worldbible-integration-contract.md` → `:15-16`.
- `git log --oneline -1; git rev-parse HEAD` → `139e3b6…`; `git ls-files | wc -l` → 2655.
- `git status --porcelain` (03:55:05Z and 03:56:56Z), `git hash-object`, `git diff`
  on the round-5/6/7 receipts; `git cat-file blob HEAD:<path> | sha256sum`;
  `stat -c '%y'`; four-sample sha256/mtime window 03:56:13–03:56:49Z.
- `grep -n 'validation.json").write_text' reports/round-{5,6,7}/run-validation.py`
  → `:194`, `:336`, `:1171`; `grep -c receipt_guard` on the same three → 0, 0, 0.
- `awk 'NR>=450 && NR<=456' SKILL.md` → `:453` receipt-guard row.
- `grep -n "round-5\|round-6\|round-7\|run-validation" reports/round-33/targets.json`
  → no seat assigned to the r5/6/7 acceptance.
- `awk 'NR>=3510 && NR<=3516' LOG.md` → `:3513` "12 standing open items".
- `awk 'NR>=105 && NR<=112' reports/round-32/final-dossier.md` → `:107-110`
  "Twelve named items" followed by nine enumerated groups.
- `awk 'NR==178 || NR==186 || NR==189 || NR==193' reports/round-24/promotion-review.md`
  → N1/N4/N5/N7 as four numbered conditions with four distinct remedies
  (evidence for R05-C-1).
- `awk 'NR==31 || NR==48' reports/round-15/handoff/contract-v2-audit.md`
  → contract digest `5f…`; bilateral read "stated, not asserted complete".
- `awk 'NR==53 || NR==59 || NR==64'` and `NR==145..153`
  `reports/round-32/dossier-d11-shonen-boxes.md` → box-1 conditions 2/3/4 and
  the N1/N4/N5/N7 status block.
- `ls -la reports/round-33/calib/` (03:58Z) → K03, C01/C03/C07/C11/C12, C16,
  P02 present.

Files relied on: `REGIMEN.md`; `reports/round-33/{claims.json,targets.json}`;
`reports/round-33/calib/{K03-open-items.md,C01-item-01.md,C03-item-03.md,C07-item-07.md,C11-item-11.md,C12-item-12.md,C16-receipt.md,P02-plan.md}`;
`SCORECARD.md`; `LOG.md`; `reports/round-32/{dossier-d13-operator-decisions.md,dossier-d11-shonen-boxes.md,final-dossier.md,scribe/fragment-ledger.md,scope.md}`;
`reports/round-24/{box2-d4.md,promotion-review.md}`;
`reports/round-26/register/{review.md,design.md,rules.md}`;
`reports/round-27/law/`; `reports/round-15/handoff/contract-v2-audit.md`;
`reports/round-29/{devin-availability-disposition.md,recount/{audit.md,dispositions.md}}`;
`reports/round-31/final-sweep.md`; `reports/round-{5,6,7}/run-validation.py`;
`reports/round-{5,6,7}/validation.json`; `examples/culture-d4/expected-holds.json`;
`corpus/knowledge/linguistics/register-lexicon-ceilings.md`;
`corpus/knowledge/synthesis/worldbible-integration-contract.md`;
`SKILL.md`; `tools/harness/receipt_guard.py`; `tools/check-gate-battery.py`;
fleet `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` (read-only).
