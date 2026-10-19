- Seat: R01 | reviewer | claim O | date 2026-10-19 | baseline 139e3b6

# R01 — adversarial review of the claim-O (`op/`) fragments

**Verdict summary.** The op/ batch is honest and reproducible. I re-ran every
command the fragments cite that can be re-run and independently re-measured every
pin, digest, histogram, resolver verdict and control set. The claim-O before-state
reproduces exactly; the regression battery is green; K01's falsifier locate is
correct; **O05's bounded fix draft works verbatim** (I extracted its §3b command
from the fragment bytes and ran it: live tree 0 rows, negative control fires);
**O02's whole control battery reproduces** (proposed bytes all-green, each of its
six controls fires the expected check) and its proposed-README digest reproduces by
re-running its own build script; **O06's embedded harness reproduces 11/11** at the
digest it claims. Twelve findings: one HIGH (a filed-bytes incident already observed
by O07/R05 — I add the current restoration state and digests), five MEDIUM, one
LOW-MEDIUM, five LOW. Nothing found invalidates the claim's before-state or its
regression thresholds. Three items need the integrator's decision before the README
edit lands (F-R01-2, F-R01-10, F-R01-3/4 corrections).

## 1. Scope, stamp, and method

Fragments reviewed — sha256 at review stamp (2026-10-19 ~04:10Z). Fragments were
revised repeatedly during the window; every finding below was **re-applied to the
current bytes** (verified by re-grepping the specific claim), and the digests are a
moving target by design in a 64-seat wave:

| fragment | sha256 (first 16) | reviewed |
|---|---|---|
| `op/K01-falsifier-scout.md` | `9d9dbe83b8b5ca38` | all sections |
| `op/K02-lessons-census.md` | `5d7f96a3f27fdad5` | all sections |
| `op/O01-row-drafts.md` | `f9e86e58bd70be00` | all sections |
| `op/O02-readme-delta.md` | `59ec9589f6f5ed96` | all sections |
| `op/O03-owner-checks.md` | `7db3554ea8096c33` | all sections |
| `op/O04-format-checks.md` | `89ccee0cd934d5a6` | all sections |
| `op/O05-falsifier-disposition.md` | `6499d3b3fa8813e2` | all sections |
| `op/O06-controls.md` | `a4b847752f2deaa6` | all sections |
| `op/O07-baseline-receipt.md` | `d2cb6b554d39a8ac` | all sections |
| `op/O08-receipt.md` | `2ebb25b29f17cf45` | all sections |
| `op/P01-plan.md` | `cfeed62fcfd827f1` | all sections |

All eleven claim-O fragments have landed; none is owed.

Method: (1) every command output quoted in a fragment was re-executed from the lane
root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; (2) every pin,
digest, histogram, count and line pointer was re-derived by a second route (raw
`wc`/`sha256sum`/`grep`/`find` or a stdlib probe) rather than by re-reading the
fragment's own tool; (3) fragment assertions that no command can settle after the
fact (e.g. "P01 did not exist at my read") were checked for internal consistency
and left `to-verify` where unverifiable; (4) severities: HIGH = moves filed bytes or
blocks the claim; MEDIUM = a contested number or an integration hazard; LOW =
citation/completeness defects that do not change a verdict.

Independence: no fragment's number is accepted here because the fragment states it.
I did not read the sibling review fragments (`review/R02`, `R03`) before writing, and
no fragment's text was modified.

## 2. Severity-ranked findings

### F-R01-1 (HIGH) — three filed `validation.json` files were rewritten in place inside the round window; the tree now reads HEAD again, and the round must record the incident *and* the restore

- Observed by O07 (`op/O07-baseline-receipt.md:147-179`, "Post-capture observation")
  and by R05 (`review/R05-calib-review.md:105-118`): between 03:52Z and 03:55Z a seat
  re-ran historical validators, which rewrite their own receipt in place —
  `reports/round-5/run-validation.py:194`, `reports/round-6/run-validation.py:336`,
  `reports/round-7/run-validation.py:1171`. That moves filed round bytes
  (`reports/round-1..32/**`), which the round's own shared rules forbid.
- **My independent measurement, 2026-10-19 ~04:00Z:** all three files are
  byte-identical to HEAD again —
  `reports/round-5/validation.json` `73a66f7464ead0d9…`,
  `reports/round-6/validation.json` `32c621efaccca71d…`,
  `reports/round-7/validation.json` `2f4c1e159b60d782…`; `git hash-object` equals
  `git rev-parse HEAD:<path>` for each and `git diff --numstat` over the three is
  empty. The mtimes (03:55:27Z, matching R05's second stamp) show a restore write;
  the mutated blobs were never committed and O07/R05 recorded their digests while
  they existed.
- Why this is HIGH and not merely "already reported": the restore erases the evidence
  from `git status`, so the round's scope statement (A03/X02) and O07's receipt can
  both read clean while filed bytes were in fact moved and restored. O07
  `:19-25` ("Binding facts at capture", 3 rows) is no longer the tree state; its own
  post-capture section is the only in-fragment correction.
- Integrator action: (a) record the incident and the restore as a new dated LOG/scope
  entry naming the three paths, the pre-restore digests O07 measured
  (`fe926984e8d15728…` r5, `af0cf4ed32d68c2b…` r7) and the post-restore digests
  above; (b) attribute the writer — **`to-verify`**: O07 and R05 both leave it open
  and I could not attribute it either (no round-33 fragment claims those runs;
  `tools/harness/r8_checks.py` only references r7's receipt as a defect record, it
  does not write it); (c) file an errata line on O07's receipt so it is not read as a
  clean pre-edit binding. Do **not** repair filed bytes further — they are at HEAD.

### F-R01-2 (MEDIUM) — the §4 queue-mint count is contested across fragments: 13 / 15 / 29 rows

- `op/O01-row-drafts.md:127` — "§4 must gain queue rows for the ids these lessons
  carry: **Q-30-1..5, Q-31-1..4, Q-32-1..6 (15 ids)**".
- `op/P01-plan.md:171-181` — "The lessons carry **15 explicit ids** that must appear".
- `op/O03-owner-checks.md:84-92` — the same 15 dangling.
- `op/K02-lessons-census.md:149` — option (a) "Q-30-1..3, Q-31-1..4, Q-32-1..6 =
  **13 ids**", excluding Q-30-4/Q-30-5 as closed-at-source.
- `op/O02-readme-delta.md` D5/D6 — **29 rows**: the 15 above plus first-assigned ids
  for the prose-named open items of rounds 26–29 (`Q-26-1..2`, `Q-27-1..4`,
  `Q-28-1..5`, `Q-29-1..3`), reaching `Rows: **78**`.
- The number is not cosmetic: §4's `Rows: **N**` line is re-derived by C34b's queue
  regex, and K02's own `:190` computes `49 + 13 = 62` under its option (a). A stated
  count that disagrees with the applied table turns C34b red *after* the
  reconciliation — the exact failure class claim O exists to close. O02's D6 does
  carry the applied-state control (`ctl-c3b-queue-77-lie` → C34b red, which I
  reproduced), so the 29-row design is self-consistent; the 13/15 designs are not
  yet reconciled with D1's cell choice (see F-R01-10).
- Integrator action: pick one design, state the rule in the Revision-3 block, and
  re-derive `Rows: **N**` from the applied table — never from a fragment's
  arithmetic.

### F-R01-3 (MEDIUM) — P01's contract-cell derivation rule misnames the missing line

- `op/P01-plan.md:123-124` — "contract — count of line-anchored
  `source:`/`verified-at:`/`recheck:`/`scope:` … r29/r30 are 3/4 (**missing
  `scope:`**)".
- Measured (my probe; K02 `:116-117`, O01 `:82-84`, O02 `:58-59`, O04 `:43-45` all
  agree): r29/r30 have `source:`/`verified-at:`/`scope:` and **no `recheck:`**
  (`grep -c '^recheck:'` → 0 for both).
- The applied cell (`3/4`) is unaffected because the tool measures it; the rule text
  is wrong and would mis-derive a cell if followed literally. Fix before the plan is
  executed from.

### F-R01-4 (MEDIUM) — O04's H3 sub-shape count (17 files) contradicts its own enumeration and the measurement (13 files)

- `op/O04-format-checks.md:77-80` — "H3 per-axis sections (`^### [DOCA] — `) occur in
  **17 files**, including … rounds 14 (3), 15 (2), 17–19 (3 each) and 20 (6)".
- My independent count over `corpus/lessons/*.md`: **13 files** — rounds 14 (3),
  15 (2), 17 (3), 18 (3), 19 (3), 20 (6), 21 (3), 22 (3), 23 (2), 25 (3), 26 (3),
  27 (3), 28 (3). O04's own enumeration sums to 6 + 7 = 13, so "17" is a miscount
  inside its §2 F1.
- O04's other counts reproduce exactly: `^## [DOCA] — ` occurs in exactly 4 files
  (r29 3, r30 3, r31 3, r32 1) and `^### Rule$` in exactly 11 (r21–23, r25–32), so
  the "H2 form is new at round 29" conclusion stands; only the H3 total is wrong.

### F-R01-5 (MEDIUM, now RESOLVED by the fragment's own revision — retained for the record) — O08's early "not located" disposition is superseded by K01/O05

- The revision I first read (`0d9f6166…`) concluded "**no antecedent artifact
  located**" and dispositioned the item `carried-with-owner + reason` (owner K01 →
  O05), ranking four candidates. That was honest at its stamp.
- K01 then located the artifact (`corpus/lessons/round-32.md:36,41,55`) and O05
  produced the located branch. **O08's current revision (`2ebb25b2…`, `:263-282`)
  now carries an explicit "Supersession by O05" paragraph** naming O05 as the
  disposition record and its re-key as the second construction — so no integrator
  action is needed beyond confirming that `scribe/S01-op-receipt.md` cites O05 §3-§5
  (the located branch) rather than O08's early summary.

### F-R01-6 (LOW-MEDIUM) — carried-cell definition drift (r31/r32), and a range-expression read rule is missing

- Same lesson bytes, two readings: K02 `:139-140`, O01 `:60-61` and P01 `:114-115`
  give r31 "Q-31-1..4" and r32 "Q-32-1..6" (ids *declared* in each lesson's own queue
  section); O03 `:91-92` gives r31 "Q-30-2, Q-31-1..4" and r32 "Q-30-2, Q-31-1..4,
  Q-32-1..6" (ids *named anywhere*). My literal-id census: r31 names 5 (Q-30-2 at
  `:53`, Q-31-1..4 at `:57-60`), r32 names 11 — O03's set. The index cell needs one
  stated rule.
- Related: O03 `:86` reads r26 as 6 ids, but `corpus/lessons/round-26.md:126` carries
  the range expression "`Q-02-1..4`" — 9 ids, all present in §4
  (`corpus/lessons/README.md:152-155`), so O03's "0 dangling" verdict holds while its
  count understates by 3. A `X-N..M` range-reading rule is needed before any
  fragment's id census sizes the §4 delta (feeds F-R01-2/F-R01-10).

### F-R01-7 (LOW) — O07's two stale pointers to the round-32 scope receipt

- `op/O07-baseline-receipt.md:120-127` and `:162` cite `reports/round-32/scope.md:13`
  for the 1,870 tracked-paths figure and `:21-24` for the "1,870 = 1,735 + 135"
  breakdown. Measured: the figure is at `:10`, the breakdown at `:29`; `:13` is blank
  and `:21-24` is the baseline-binding bullet and the protected-surface paragraph. The
  reconciliation note itself is correct and useful. (O07's `:128-133` citation of
  `corpus/lessons/round-28.md:86` reproduces exactly.)

### F-R01-8 (LOW) — O04's `spot-check` line list is short one line

- `op/O04-format-checks.md:95-96` — "`spot-check` ×4 in round-26 (`round-26.md:29`,
  `:155`, `:168` — prose about spot-checks)": three lines for four occurrences.
  Measured: one occurrence each on `:29`, `:155`, `:168`, **`:172`**. K02 `:97` lists
  all four. The count is right; the citation is incomplete.

### F-R01-9 (LOW) — O01's quoted self-check output no longer matches the filed fragment

- `op/O01-row-drafts.md:147-152` quotes its checker's output as "fence count: 3"; the
  filed fragment carries **4** fenced blocks (8 fence lines at `:22,:40,:54,:62,
  :96,:99,:147,:152`). The check's substance is unaffected — the checker reads the
  *second* block, which is still the §2 row block — but a re-runner reproducing §6
  verbatim will see `fence count: 4`. Re-run and re-quote, or note the revision.

### F-R01-10 (MEDIUM) — O02's D1 and O01's §2 disagree on the r26–r29 "open-questions carried" cells, and the choice drives F-R01-2

- `op/O01-row-drafts.md:55-58` gives r26–r29 rows `— (no queue ids; …)` with prose
  parentheticals; `op/O02-readme-delta.md:91-94` gives the same four rows
  `Q-26-1, Q-26-2` / `Q-27-1..4` / `Q-28-1..5` / `Q-29-1..3` — first-assigned ids that
  exist only if O02's D5 queue block is applied. O02's own §Owed says "if O01 lands a
  differently-formatted draft, its format should win and D1's cells should be
  re-checked"; O01 has landed.
- The two choices are not equivalent: O01's cells imply the 15-row mint (F-R01-2);
  O02's cells imply the 29-row mint and `Rows: **78**`. Applying O01's §2 rows with
  O02's D5/D6 leaves §4 rows naming ids that no index row references and a stated
  count (78) whose arithmetic the §2 cells contradict; applying O02's D1 rows with
  O01's cells leaves four queue rows unowned by any lesson row.
- Integrator action: apply **one** pair (recommended: O02 D1 + D5 + D6, because D6's
  count is control-backed and every owner cell in D5 resolves — I verified all 29
  owner tokens against the filesystem and the tool's `resolves()` semantics), and
  record the choice in the Revision-3 block. If O01's cells win, drop the four
  first-assigned id groups from D5 and restate D6's counts (49 + 15 = 64).

### F-R01-11 (LOW) — O06's quoted receipt details for C4a/C4b do not match its own digest-pinned harness

- `op/O06-controls.md:117-118` quotes C4a's detail as
  `{"table_rows_vs_files": {"stated": [99, 99], "measured": [26, 33]}}` and C4b's as
  `{"queue_rows": {"stated": 99, "measured": 49}}`.
- I extracted the harness from the fragment (digest
  `1263f15686ce2662669e8a2b9d21222b2424d117a7e057fa72085bc8262a0d2d` — **matches the
  claimed value exactly**) and ran it: `CONTROLS OK: 11/11`, exit 0. The receipt it
  produced carries **stated [27, 34]** for C4a and **stated 50** for C4b, because the
  harness derives each lie from the measurement (`n_rows + 1`, `int(...) + 1`) — the
  `99`s are leftovers from an earlier hardcoded version. The controls are correct and
  stronger than the quote implies (a derived lie cannot become true later); only the
  quoted details are stale. Re-quote from the receipt.

### F-R01-12 (LOW) — O02's control table under-reports one control's red set

- `op/O02-readme-delta.md:499` lists c2 (ghost row) as "`C31` FAIL, `C31-2
  ghost-row`". Reproduced against the proposed bytes: **both** `C31` and `C34b` go red
  (`C34-2 table_rows_vs_files {stated: [33, 33], measured: [34, 33]}`), because the
  ghost row raises the measured row count above the stated 33. O02's c1 row already
  documents the same coupling for row *removal*; c2 should name it too. No design
  change needed.

## 3. Verified-green ledger (what I reproduced, per fragment)

| fragment | claim checked | my route | result |
|---|---|---|---|
| K01 | artifact at `round-32.md:36/:41/:55`; sha256 `8aacfc2b…` | `sed` + `sha256sum` | equal |
| K01 | instrument false-fires with 5 rows, exit 0 | verbatim `SKILL.md:715` one-liner | 5 rows, exit 0 |
| K01 | substance 5/5, digest table | `sha256sum` vs `closes_sha256` per round | 5/5 equal, digests equal |
| K01 | 9 `availability*.json`, zero `closing-snapshot.json` | `ls` + `find` | 9 files; 0 matches |
| K01 | SKILL.md sha256 `79fe91d3…`, `wc -l` 715; item inside D3 (no heading 660–715); Checklist 522–534 | `sha256sum`, `awk` heading scan | equal |
| K01 | landed by `17e90b9`, SKILL.md +3 | `git show --stat` | confirmed |
| K02 | before-state, exit 1, findings 2 | full audit run | identical |
| K02 | README sha256 `ec7469da…`, 29059 B / 346 lines | `sha256sum`, `wc` | equal |
| K02 | format histogram 21/5/7; contract histogram 0/3/4 = 5/15/13 | partition-wide probe | equal |
| K02 | per-file pins r26–r32 (7× bytes/lines/sha8) | `wc -c`, `wc -l`, `sha256sum` | 7/7 equal |
| K02 | only r30/r31/r32 declare own-round ids; r26–r29 none | `grep -o 'Q-[0-9][0-9]-[0-9]*'` | equal (r26 cites a range, does not declare) |
| K02 | README line refs `:83,:97,:138-142,:200,:207,:227-232,:247-250,:296-301` | `sed` spot reads | all resolve |
| O01 | 7 row pins + format + contract cells | second route + tool `--json` | 7/7 equal (incl. `3/4` for r29/r30) |
| O01 | insertion point `:94`/`:95`; `:97` literal | `sed` | confirmed |
| O01 | `--json` carries `index_sha256` + `live[]` with bytes/lines/sha8 | `--json` run | confirmed |
| O01 | r32 `:45` pins the same six triples | `sed` | confirmed |
| O01 | validation.json sha8 prefixes ×7 | `sha256sum` | 7/7 equal |
| O02 | proposed-README digest `335bb22a…` (43 261 B, 446 lines) | re-ran `.scratch/o02/build-proposed.py` | byte-identical |
| O02 | proposed bytes pass all six checks, findings 0 | tool's own `run_checks()` over the proposed file | confirmed |
| O02 | six-control battery (c1…c6) | re-ran each control file through `run_checks()` | c1 → C31+C34b; c2 → C31(+C34b, F-R01-12); c3 → C34b; c3b → C34b; c4 → C34; c5 → C32; c6 → C34c — all as designed |
| O02 | D9/D0 variants stay green | `run_checks()` over both | findings 0 |
| O02 | all 29 D5 owner tokens resolve | `test -e` + `resolves()` semantics | all resolve (22 paths, 7 role tokens) |
| O02 | receipt fields for r26–r32 (`acceptance_checks_passed`, `measured_at_utc`, `runner_sha256[:8]`) | re-read each `validation.json` | 7/7 equal |
| O02 | `find` counts 146 files / 9 dirs; README `:35,:39,:40` before-blocks | `find`, `sed` | equal |
| O03 | resolver semantics (role-token set, parenthetical strip, round-pointer `isdir`, path `exists`) | read `:151-167` + 18-token probe via `runpy` | 9/15 resolve, 6 fail — exactly as tabled; rewrites green; `round-99` fails as `round-pointer` |
| O03 | §4 owner classes path 37 / role-token 12 | README `:211-213` read | equal |
| O03 | 21 candidate pointers exist | `test -e` on every named path | all exist |
| O04 | 7/7 gate-keeper; H2 form only in r29–r32 (3/3/3/1); `### Rule` in exactly 11; fragment-index ⊂ gate | partition probe | equal |
| O04 | zero fenced marker false-positives | fence-aware scan | 0 hits |
| O04 | C33 is a substring check; C34b reads the first `Rows: **N**`; C34c compares cells[1]/[2] | code read `:229-243,:296-317,:272-288` | confirmed |
| O05 | before-block digest `541bad77…` | hash of the fragment's §3a block and of live `SKILL.md:713-715` | equal; block bytes == live bytes |
| O05 | §3b draft command works | extracted verbatim from the fragment, run live (twice, incl. current bytes) | **0 rows, exit 0** |
| O05 | negative control fires | same command, one snapshot hidden | 1 row (r28) |
| O05 | `closes_record` exists nowhere; live key is `closes`; r31 `:780` is name-exact | `grep -l` + `:780/:799` read | confirmed |
| O06 | harness digest `1263f156…` | extracted the single python block, hashed | equal |
| O06 | 11/11 controls | ran the extracted harness | `CONTROLS OK: 11/11`, exit 0; C5/C9 reach findings 0 |
| O06 | `--json` exits 0 unconditionally (`:445-447`); plain exit is the verdict (`:460`) | code read + C8 behaviour | confirmed |
| O07 | 4 assigned commands exit 0 (battery 44/44, craft 10/10+18/18, d4 81/81, c31 28/28) | re-runs | 4/4 exit 0 |
| O07 | battery mode: pass 7 / fail 0 / unevaluable 0, coverage 10/10, pinned 20, findings [], originals preserved | full battery run | equal |
| O07 | 4 tool digests + README digest; `ls-files` 2655 = 1830 + 825 | `sha256sum`, `git ls-files` | equal |
| O08 | before-state, exit 1; simulation "after" shape (33 rows, findings 0, exit 0) | audit run + code read `:444-460` | before equal; after-shape consistent with the tool's logic |
| O08 | `Rows: **49**` untouched by a minimal reconciliation | C34b code read | confirmed |
| O08 | supersession of its early §3 by O05 | current `:263-282` read | recorded (F-R01-5 resolved) |
| P01 | row cells, `:45` cross-check 6/6, owner-token trap, controls plan, integration order | probes + code reads | equal (except F-R01-3) |

## 4. Independent ground truth for claim O (what the round runner should compare against)

- **Before-state (reproduced 3×, 2026-10-19):**
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit **1**;
  `lesson files: 33`, `index rows: 26`, `queue rows: 49`, `formats {'gate-keeper':
  21, 'fragment-index': 5, 'plain': 7}`; `FAIL C31_index_rows_eq_files`, `FAIL
  C34b_prose_arithmetic`; findings `C31-1` (exactly `round-26.md … round-32.md`) and
  `C34-2 {stated [26,26], measured [26,33]}`. `--selftest` → `SELFTEST OK: 28/28`,
  exit 0. This matches `claims.json` claim O `before` exactly.
- **Regression baseline (my re-run, same tree):** gate battery `--selftest` 44/44
  exit 0; craft `--selftest` 10/10 + CLI 18/18 exit 0; `assemble-culture-d4.py
  --selftest` 81/81 exit 0 and `--check` byte-identical; c31 `--selftest` 28/28 exit
  0; `check-evidence-coupling.py --selftest` green.
- **The "battery 10/10" reading, clarified so it cannot be misread as a regression:**
  the battery's `pass` counter is **7** (structural gate selftests executed) while
  `coverage` is **10/10** (registered gates carrying a committed baseline) with
  `pinned 20`, `unevaluable 0`, `findings []`, `originals.preserved true`. The claim's
  threshold language is the coverage reading; a reader expecting `pass 10` will read a
  false regression. O07 `:38-45` states this correctly; the final receipt should carry
  both numbers.
- **Falsifier leg:** instrument false-fires (5 rows) on a tree where all five records
  are closed; substance holds 5/5 on two independent routes (digest equality, and the
  `closed_fields` counts against the LOG.md admission lines: r19 12/12, r25 26/26,
  r26 24/24, r27 24/24, r28 24/24). O05's §3b repoint is **functionally verified by
  me**, and its `legacy-name-only` control pair (same fixture, the two instruments
  disagree) is the evidence that the fix is substance-keyed rather than name-keyed.
- **Reconciliation reachability:** two independent routes reach `findings: 0` —
  O06's C5/C9 (mechanically generated rows, then O01's drafted rows) and O02's
  proposed bytes. The after-state is attainable without editing the tool.

## 5. Integration instructions no single fragment owns

1. **Record F-R01-1** (filed-bytes incident + restore + attribution `to-verify`) in
   the round's scope/conformance record and as an O07 receipt errata.
2. **Choose the §4 design once** (F-R01-2 + F-R01-10): O02's D1+D5+D6 (29 rows,
   `Rows: **78**`, control-backed) or O01's cells with a 15-row mint
   (`Rows: **64**`); then re-derive the count from the applied table.
3. **Apply O05 §3b as the located branch** of the falsifier leg (integrator, shared
   file), then re-run O05's control harness and P01 `:328-332`'s round-33
   self-application (the re-keyed audit must not print `reports/round-33` once its own
   closing snapshot lands). Confirm S01 cites O05, not O08's early summary.
4. **Correct before quoting**: P01 `:124` (F-R01-3), O04 `:78` (F-R01-4), O06
   `:117-118` (F-R01-11), O07 `:120-127` (F-R01-7), O02 `:499` (F-R01-12).
5. **State the carried-cell rule** (F-R01-6) and the range-reading rule before any id
   census is used to size §4.
6. **Re-measure at apply time** — every fragment says so and I agree: pins,
   histograms, queue counts and the README digest are all stamp-bound.

## Owed

- **No op/ fragment is owed.** All eleven claim-O fragments (K01, K02, O01, O02, O03,
  O04, O05, O06, O07, O08, P01) had landed and were reviewed at this stamp. O02 and
  O06 landed after my first pass and are folded in above.
- Residual dependencies for *other* seats, not review debts of this one: the round-33
  `availability.json` + its closing snapshot (P01 `:403-404`, the integrator's act),
  and the `SKILL.md` application of O05 §3b (integrator, shared file).
- Because fragments were revised mid-window, a later revision of any fragment above
  can move a finding's *line number*; the measured value each finding rests on was
  re-verified against the current bytes at this stamp and still binds.

## Citations

- `reports/round-33/claims.json:19-37` (claim O: before, after_required,
  counting_commands, thresholds); `reports/round-33/targets.json:5-11` (shared rules),
  seat R01 object
- `reports/round-33/op/K01-falsifier-scout.md:5-12,41-49,74-91`;
  `op/K02-lessons-census.md:32-40,82-90,116-124,138-154,182-195`;
  `op/O01-row-drafts.md:42-45,49-62,70-89,120-136,140-152`;
  `op/O02-readme-delta.md:53-70,79-118,120-139,237-331,463-525,571-593`;
  `op/O03-owner-checks.md:27-47,57-69,84-92,115-137,178-212`;
  `op/O04-format-checks.md:40-45,66-97,124-153`;
  `op/O05-falsifier-disposition.md:30-38,42-71,78-92,123-151,215-243,253-262`;
  `op/O06-controls.md:22-39,65-88,89-128,130-598,600-657,674-689`;
  `op/O07-baseline-receipt.md:19-25,27-34,38-45,52-63,65-83,120-133,147-179`;
  `op/O08-receipt.md:18-63,98-181,197-290,301-316`;
  `op/P01-plan.md:100-140,141-165,167-201,203-225,227-236,240-332,336-378`
- `reports/round-33/review/R05-calib-review.md:105-118` (independent observation of the
  filed-bytes incident)
- `corpus/lessons/round-32.md:31,36,41,45,55-60`; `corpus/lessons/round-26.md:126`;
  `corpus/lessons/round-29.md`/`round-30.md` (contract lines);
  `corpus/lessons/README.md:10,29` (round-32 scope), `:35,39-40`,
  `:69-97,111-142,144-155,200-213,227-232,247-250,296-301`
- `reports/round-32/scope.md:10,23,29`; `reports/round-28.md:86`;
  `reports/round-{19,25,26,27,28}/telemetry/availability-close-<N>.json`
- `SKILL.md:522,534,660,713-715`; `LOG.md:3460-3468,3512-3514`; `SCORECARD.md:443-445`
- `reports/round-25/audit/c31-lessons-index-audit.py:42-56,72-89,138-167,191-211,
  229-243,262-317,440-460`; `reports/round-31/run-validation.py:780,792-812`;
  `reports/round-31/jinii/draft.md:38-45,85-121`;
  `reports/round-5/run-validation.py:194`; `reports/round-6/run-validation.py:336`;
  `reports/round-7/run-validation.py:1171`
- Commands (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`): the c31 audit + `--selftest` + `--json`;
  `python3 tools/check-gate-battery.py [--selftest]`;
  `python3 tools/check-craft-exercise.py --selftest`;
  `python3 tools/assemble-culture-d4.py --selftest|--check`;
  `python3 tools/check-evidence-coupling.py --selftest`; the verbatim and re-keyed
  `SKILL.md:715` one-liners (plus a negative control with one snapshot hidden); the
  O05 §3b command extracted from the fragment bytes and run; the O06 harness
  extracted from the fragment bytes and run with `--receipt`; O02's
  `.scratch/o02/build-proposed.py` re-run and each `ctl-*.md` re-run through the
  tool's `run_checks()`; `runpy` probe of `resolves()` over 18 tokens;
  `sha256sum`/`wc -c`/`wc -l` over the seven lesson files, the five snapshots and the
  proposed README; `git hash-object`/`git rev-parse HEAD:<path>`/`git diff --numstat`
  over `reports/round-{5,6,7}/validation.json`; `git ls-files | wc -l`,
  `git ls-files | grep -c '^reports/round-'`; heading-level, fence-aware and
  marker-vocabulary probes over `corpus/lessons/*.md`; `grep -o 'Q-[0-9][0-9]-[0-9]*'`
  per lesson file; `find corpus/lessons -mindepth 2 -type f | wc -l`; `test -e` over
  the 29 D5 owner tokens; `sed` line reads as cited above
