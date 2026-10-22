# Round 51, attempt 3: routed-defect review

- Seat: KotodamaR51a3.ReviewRoutedDefects (leaf reviewer; no subagents, no background jobs)
- Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin (branch main)
- Claim base: bff83ba65bf9559af4d7567e81703059667a0005
- Lane HEAD at review: 1f97472 (round-51 attempt-3 declaration, on top of 5ab3634)
- Writes: this report only. Nothing else in the lane or fleet was written.
- Installs or updates: none.
- External sources: none opened by this seat.
- Not opened, by rule: reports/round-51/calibration/, /fast/scratch paths, fleet-root .ufo/.

## Result

No high-severity defect in the round-51 declaration. The declared inputs have the keys the checker requires, the agreement check passes, and no round-50 frozen file changed.

Three things stay open and must be carried as stated limits, not as passes:

1. The separability self-application does not exit 0 yet. It cannot until claim C's entry and the record file `corpus/lessons/round-51.md` exist.
2. The separability name check sees only full repo-relative spellings. Short spellings of the must-not-cite paths pass unseen. I measured this.
3. Three properties in the claim text have no acceptance leg (the existing 11 rows keep their neighbours; the four new rows are developed; C's sources were opened this round).

Routed debts: debt 1 is partly done (inputs declared; ownership check pending integration). Debt 2 is declared for the target but not yet met in the worktree. Debts 3, 4 and 5 are carried to a later round.

## Checks run by this seat

| Check | Command or source | Result |
|---|---|---|
| Claims and manifest agree | `python3 -B reports/round-51/claims-agree.py` | `AGREE claims=['C', 'D']`, exit 0 |
| Worktree state | `git -C <lane> status --porcelain` | only `?? .ufo/waves/round-51/`; no tracked entry |
| Tracked diff | `git -C <lane> diff --stat` | empty |
| Base to HEAD | `git diff --stat bff83ba HEAD` | 7 paths, all under reports/round-51/ (five outside calibration/; two under calibration/, names only, not opened) |
| Round-50 frozen paths | base-to-HEAD diff of corpus/, reports/round-50/, tools/ | no change |
| D before-state | `python3 -B reports/round-51/boundary-count.py` | `rows=11 resolved=11 distinct=11`, exit 0 |
| C before-state | `find corpus/knowledge -name '*.md' \| wc -l` | 226 |
| Round-50 spot-check index row | measured bytes, lines and sha256 prefix of `corpus/lessons/round-50-verifier-spotcheck.md`; compared with `corpus/lessons/README.md:107` | 7670 bytes, 102 lines, `db6d4725`; matches the row |
| C premise: sign or gesture file names | `find corpus/knowledge` with four name patterns | none |
| C premise: topic owner | topic grep for gesture, sign language, kinesic, nonverbal, body language, proxemic | 0 matches |
| C premise: named partial owners | `linguistics/syntax-typology.md:99`, `linguistics/numerals-and-measures.md:107`, `culture-material/adornment-body-codes.md:77` | sign-language remark at :99; finger counting at :107; section 7 heading at :77 |
| C export novelty | the S071-and-up export pattern (manifest :28) over base SOURCES.md, README.md and the D entry | 0 matches |
| C acceptance column | parsed corpus/SOURCES.md | 70 rows, 11 cells each, no escaped pipes; used-by is column index 11, as the acceptance assumes |
| Name-leg behaviour (run) | `_name_re` from tools/check-claim-separability.py, called on sample strings | see F2 |
| Separability receipts | telemetry/declaration-dry-run.txt:16-18 and :38-40 | exit 2 twice, because C's entry is absent; not re-run by this seat |
| lsp device | `xd://lsp` | not mounted (mounted: ast_edit, debug). Caller checks were literal text search only, not semantic proof |

## Routed debts (round-50 lesson, lines 92-98)

| # | Routed debt (lesson line) | What round 51 does | Pointer | Status |
|---|---|---|---|---|
| 1 | Declare compatible own-round manifest inputs; verify counterfactual ownership; never rewrite r50's failure; keep the relative-path blind spot and the unowned-path findings (93-94) | Declares `schema` and `base`, units with lands, exports and acceptance, and a record unit REC. The key names match the checker's required keys (`tools/check-claim-separability.py:85-86`). Round 50's failure ("missing base, schema") is not rewritten. Exit 0 is not shown yet: both receipts exit 2 because unit C's entry is absent. The checker reads every unit's lands from the worktree (`:471-474`) and fails on an absent file (`:451-458`). REC's land `corpus/lessons/round-51.md` is also absent today, so it fails the same way after C lands. Blind spot: retained and measured (F2). Unowned-path findings: no such finding code exists in the checker, so this term's referent is not identified; retained by reference only. | claims.json:11, :18-27, :35-44, :47; separability-manifest.json:2-3, :13-17, :27-35, :39-51; telemetry/declaration-dry-run.txt:16-18, :38-40; round-50.md:102 (R50-M6) | Inputs declared. Ownership check pending integration. Blind spot retained |
| 2 | Address the commissioned neighbour target and residual source/content markers, without lowering the target (95) | Claim D lands the pastoral entry and its counter. Target 11 to 15. The counter exits 0 for any consistent count (`boundary-count.py:92`), so exactly 15 is pinned only by the string test in the manifest (:13-17) and by claims.json:25. The lesson says "at least 15" (lesson :47). D's exact pin is stricter, not lower. Residual markers: the entry has 32 literal `(to-verify)` markers, plus one legend mention at entry :188. D claims none of them. | claims.json:18-27; boundary-count.py:25, :63, :92; entry :27 (section 2), :188 | Target declared, not met in the worktree (rows=11). Markers: not this round |
| 3 | Preserve survivor and fake-label limits; use consumer behaviour, not source-text or wiring assertions (96) | No mutation or guard claim lands. The attempt-1 calibration files are not used by C or D (claims.json:8 and records_not_claims). D's counter resolves anchors against real files and line bounds, which is behaviour. C's acceptance runs sweep.py, which is behaviour (the ok flag includes footer totals: `sweep.py:191-194`, `:210`; exit at `:427`). C's acceptance also runs a regex over SOURCES rows, which is a text check (manifest :34). | claims.json:8; separability-manifest.json:13-17, :30-35 | Partly met: two legs execute code, one is a text check. Survivor and fake labels: not this round |
| 4 | Complete touched-checker Gate-standard registry records; improve search-log screened and excluded data (97) | No tools/ file lands (base-to-HEAD diff). The lane's registry home for gate rows is SKILL.md section Gates (`corpus/knowledge/verification/gate-frozen-run-standard.md:5`). `tools/check-claim-separability.py`, touched in round 50, has no Gates row; the other checker rows sit at SKILL.md:617-619 and :675-676. The two round-51 scripts (boundary-count.py, claims-agree.py) have no row either. I found no rule text that requires rows for reports/ scripts; the L1 should confirm. Search log: the round-50 pastoral entry (SOURCES.md:143) names included rows (22), exclusions and failures by name, but gives no identified or screened counts. The earlier entries (:137, :139, :141) give them. | SKILL.md:577, :617-619, :675-676; SOURCES.md:137-143 | Not this round. No claim declares either item. Carry |
| 5 | Preserve the original retry and load-order defects and the unresolved freshness and L0 questions (98) | No dispatch or runner file lands; claims.json lists only entries, scripts and records. Retry defect R50-M7 (round-50.md:103) and the conformance-debt sentence (spot-check :87-88) stay as they are. The freshness pause stays in force (lessons README:216, Q-22-2; :237, Q-30-1, operator-owned). L0 question Q-02-4 is open and parent-owned (README:176). Its L0 record sits at the fleet root (README:72); this seat did not open it. | claims.json:47 (records_not_claims); corpus/lessons/README.md:72, :176, :216, :237; round-50.md:103 | Not this round. Carry |

## Outside disagreements (round-50 lesson, outside table at lines 62-66, and lines 68-69 and 81-82)

The outside table has no row marked as a disagreement. All three rows say "Agree." The rest of the list is corroboration or a reference to an earlier decision.

| Outside item (lesson line) | Recorded result | What round 51 does | Status |
|---|---|---|---|
| Admit S048 for scoped pastoral conditions (:64) | Agree (FAO quote, low-density context) | Nothing to change. The D entry keeps the scoped quotation (entry :16). S048 predates this round and sits outside the S071-and-up rule | No action |
| S048 stage-ladder refutation (:65) | Agree | Nothing to change. The entry still treats the ladder as R (entry :175, :192) | No action |
| Reject the own-round substitute zero (:66) | Agree | Round 51 declares exit 0 and records the real exit 2 (receipts :16-18, :38-40). No substitute is declared (claims.json:11) | Consistent. Pending integration |
| Historical S028 rejection re-opened (:68-69) | Corroboration of an older decision, not a new row | No S028 land in any claim | No action |
| Round-49 disagreement (:81-82; QUALITY.md:29 and :31) | Already QUALITY criteria 6 (claim-scoped source tiers) and 7 (separable claims) | Criterion 7 is applied by the manifest: C lands SOURCES, and D forbids S071-and-up ids. Criterion 6 has no leg; the tier scope of C's new rows is review-only | Partly applied. Tier scope open for review |

## Findings, by severity

**F1, Medium: the separability self-application is pending, not passed.** Evidence: receipts :16-18 and :38-40; checker `_read_worktree` at :451-458 and `_load_units` at :471-474; the manifest's REC land at :42 is absent today. Risk: a reader could take the declared exit 0 as shown. Action for the L1: write `corpus/lessons/round-51.md` before the final separability run, and run the checker after the last edit, because each unit's tree is WORKTREE and the verdict binds to the bytes present at run time.

**F2, Medium: the name leg misses short spellings and never checks lands that already exist at base.** Evidence:
- `_name_re` (checker:602-604) requires the full repo-relative path.
- `name_paths()` (checker:366-368) returns only lands absent at base.
- Executed test of `_name_re`: the full path `corpus/knowledge/linguistics/sign-languages-manual-modality.md` is flagged; the `./`-prefixed form is flagged; the knowledge-relative form `linguistics/sign-languages-manual-modality.md` is not flagged; the basename `sign-languages-manual-modality.md` is not flagged. For C's must-not path `corpus/lessons/round-51.md`, the full path is flagged and the basename `round-51.md` is not.
- The lane writes short spellings as its normal style: the pastoral entry uses knowledge-relative anchors (entry :6) and basenames in couples (entry :8).
- The lesson records the same blind spot as R50-M6 (round-50.md:102).

Consequence: the must-not-cite rules (claims.json:27 and :44) are machine-checked only for full-path spellings. Body prose with a short spelling passes every leg. The pastoral entry already names `corpus/SOURCES.md` at base (entry :7, :9, :208). Not flagging that is correct, but it means no leg would catch a short-form cross-claim mention in existing files. Action: none this round (retained). Manual text check at integration (see below).

**F3, Medium: three claim properties have no acceptance leg.**
- (a) "The existing 11 rows keep their neighbours" (claims.json:18). `boundary-count.py` (main, :63-92) counts the current table and never compares it with base.
- (b) "The four new rows are developed or explicitly narrowed in the entry body" (claims.json:18), and the falsifier about the anchored line (:26). Review only.
- (c) C's "each opened this round" (claims.json:33). The falsifier at claims.json:43 does not test it. The manifest checks only that each cited id exists in SOURCES.md and carries the entry path in its used-by cell (manifest :30-35). It does not check when the row was opened.

Action: reviewer checks at integration (below).

**F4, Low: the agreement check is narrower than its name.** `claims-agree.py` (38 lines, read in full) compares ids, lands and base only. It does not compare acceptance or after_required wording. By hand: D's acceptance string equals claims.json:25. C's acceptance tests 227 and sweep exit 0; it does not name "linguistics 26" literally. The sweep's ok flag includes footer directory totals (`sweep.py:191-194`, `:210`), so 26 follows once the README footer is updated. Action: none; record this as a limited agreement check.

**F5, Low: the exact-15 pin is in the manifest, not the counter.** `boundary-count.py:92` exits 0 for any consistent count. A correct 16-row table would print `rows=16 resolved=16 distinct=16` and fail only the manifest string test (:13-17). Action: none; note for the author.

**F6, Low: registry debt for the round-50 checker.** `tools/check-claim-separability.py` has no SKILL.md Gates row (see routed debt 4). Carry.

**F7, Low: search-log counts missing for the round-50 entry.** SOURCES.md:143 names included rows, exclusions and failures, with no identified or screened counts; :137, :139 and :141 have them. Carry.

**F8, Info: the "unowned-path findings" referent is not identified.** The separability checker has no code that emits an unowned finding (grep found none). The word "unowned" appears in round-50 claims as the before-check id `pastoral-unowned` (reports/round-50/claims.json:20) and in prose. Carry by reference.

**F9, Info: C's main overlap risk.** `culture-material/adornment-body-codes.md` section 7 (:77-93) already covers gesture and posture. The falsifier "restates an existing owner's register" is review-only. Note for the C author.

**F10, Info: residual markers.** 32 literal `(to-verify)` markers remain in the pastoral entry. D does not target them.

**F11, Info: frozen-file check passes.** No tracked file differs from HEAD. The base-to-HEAD diff touches only reports/round-51/. No round-50 path changed.

**F12, Info: no high-severity defect.** The declaration's format, counts and pins match the receipts, and the counterfactual legs are declared correctly. The open items are state (F1), coverage limits (F2, F3) and carried debts.

## Operator teachings not yet reflected in QUALITY.md or SKILL.md

None. No file matching `corpus/lessons/operator-*.md` exists. The glob over corpus/lessons returned no files, and `find` over the lane returned no `operator*` names.

The word "operator" appears only as the owner of open questions in corpus/lessons/README.md (Q-02-3 at :175, Q-05-1 at :182, Q-22-2 at :216, Q-30-1 at :237). Those are open questions, not teachings. QUALITY.md contains no "operator" reference.

## Integration checks for the L1

These are text checks and advice. They are not proof.

1. Write `corpus/lessons/round-51.md` before the final separability run (manifest :42). Give it one row in `corpus/lessons/README.md` (rule C31: every lessons file has exactly one row).
2. D entry: search the body for `sign-languages`, `manual-modality` and `linguistics/sign`. Short spellings pass the name leg. Also compare the section-2 first cells with base to confirm the 11 existing anchors are unchanged. Nothing automated checks that.
3. C entry: search for `boundary-count`, `round-51.md`, `claims.json`, and `pastoralism-animal-husbandry`. The last is a D land. Full-path forms are already flagged; short forms are not.
4. C entry: cite only S071-and-up ids. The acceptance checks every `S` plus three digits in the entry (the regex is at manifest :34), and each must exist in SOURCES.md with the entry path in its used-by cell.
5. README footer: must total 227, with linguistics at 26 (sweep ok, `sweep.py:191-194`). Run the sweep after the edit.
6. Re-run the counter, the agreement check and the separability checker after the final edit.

## Residual risk and verification gaps

- Not re-run by this seat: the separability checker (receipts used; `git status` shows no tracked change since the receipts), and sweep.py (receipt used; code read).
- Not opened: reports/round-51/calibration/, /fast/scratch paths, the fleet-root `.ufo/` (including the L0 record), and sibling lanes. The claim C premise about "21 sibling lanes" is therefore unverified by this seat.
- External sources: none opened. The FAO quotations in the outside table (lesson :64-65) are unverified by this seat.
- lsp: not mounted. Caller checks were literal text search only, not semantic proof.
- The "unowned-path findings" referent is not identified in code.
- The F2 name-leg test ran `_name_re` on sample strings. It did not run the full checker on the manifest.
