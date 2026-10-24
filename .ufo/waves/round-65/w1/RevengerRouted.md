# RevengerRouted — claim Ca routed-defect calibration (round 65, wave 1)

seat: kotodama-r65.RevengerRouted
date: 2026-10-24
scope: reconstruct each R1–R7 directive from `corpus/lessons/round-64-verifier-spotcheck.md` §6 ALONE, then verdict the ExecRecordsFix draft (`.ufo/waves/round-65/stage/records-fix/`) per defect: satisfies / over-reaches (edits filed bytes that must stay append-only) / misses.
method: quotes below are verbatim from §6 (lines 84–90); filed-bytes evidence re-verified at this lane tip (base 17c32302c684…) by read-only inspection; git used read-only only (`git log --all`, `git show`, `git ls-files`). No installs this session. No repo/jj/index mutation.

## 0. Dependency finding (blocks final verdicts)

**The ExecRecordsFix draft is ABSENT.** `.ufo/waves/round-65/stage/records-fix/` did not exist at any check: 01:45–01:47 (glob: "Path not found"), 01:50, and 01:54 (`ls .ufo/waves/round-65/stage/` → `assemble-audit.json assemble-entry.py entry-draft.md gate-spec.md lesson-skeleton.md mut-c mut-ca mut-o readme-patch.md` — sibling drafts landing, records-fix never appeared). Per leaf rules I did not wait.

**Hazard named:** `.ufo/waves/round-65/att-r1/` holds six variant copies of `.ufo/waves/round-64/w2/LessonFinal.md` (`A1_truncated_original`, `A2_renamed_marker`, `A2b_no_marker`, `A3_old_above_marker`, `CTL_wrong_tree`, `E_unanchored_repeats`). These are NOT the routed draft and must not be reviewed as if they were; whoever verdicts R1 must read `stage/records-fix/` only. [INFERENCE on intent: likely another seat's attack fixture.]

Per-defect verdicts below are therefore **NOT EVALUABLE (draft dependency)**, each with a pre-registered satisfies/over-reach/miss contract against ground truth I independently verified, so the L1 can stamp verdicts the moment the draft lands.

## 1. Operative quotes + ground truth + verdict contracts

### R1 — HIGH, records-only (lesson line 84)

Operative quote: "re-stamp `reports/round-64/telemetry/final-measures-ca.txt` to `8bab271c` (or record "worktree dirty at run; read-path bytes = 8bab271c") and correct the three repeats: report line "After at `95c9194e`: ACCEPT-CA-64 PASS 7/7", `LOG.md` round-64 final-measures entry, `SCORECARD.md` Ca row measured evidence, `w2/LessonFinal.md`. Receipts must pin a tree hash of read inputs, not only the counter sha."

Ground truth (verified here):
- `reports/round-64/telemetry/final-measures-ca.txt:2` = `measured revision: 95c9194ef938e1338b2af894086a46e8b8677ee2`, `:5` date `2026-10-24T00:28:55-03:00` — the false stamp exists as routed.
- `LOG.md:4162` carries "Round-64 final measures (2026-10-24, L1): at the claim-C land `95c9194e…`: … ACCEPT-CA-64 PASS 7/7" — repeat confirmed.
- `SCORECARD.md:1235` (Ca row) and `:1229` pin measurement to `95c9194e…` — repeat confirmed.
- `.ufo/waves/round-64/w2/LessonFinal.md:858-859` = "each naming measured revision `95c9194ef938e1338b2af894086a46e8b8677ee2`" — repeat confirmed (file present in this tree).
- **Cross-lane gap:** the round-64 REPORT carrying the literal line "After at `95c9194e`: ACCEPT-CA-64 PASS 7/7" is NOT reachable from this lane: `.ufo/reports/round-64/` does not exist in the tree, `find . -name kotodama.md` finds no round-64 copy, `git log --all -- .ufo/reports/round-64/kotodama.md` is empty, and `git show 8bab271c:.ufo/reports/round-64/kotodama.md` fails. Commit `e1fe5c97` (lesson §1) does not resolve here. A draft that claims to have "corrected the report line" from this lane would be fabricating — that leg is unverifiable here.

Verdict contract — draft SATISFIES if: receipt re-stamp is additive-disclosing (old stamp kept + correction/annotation naming `8bab271c` or the "worktree dirty at run; read-path bytes = 8bab271c" formulation; never a silent overwrite of `:2`), repeats corrected or disclaimed with old→new named, and the unreachable report leg is declared uncorrectable-from-this-lane rather than claimed done. OVER-REACHES if: `final-measures-ca.txt` bytes are rewritten in place erasing the false `95c9194e` stamp (receipt bytes are evidence), or LOG/SCORECARD/lesson history is silently edited without old→new disclosure, or a report-line "fix" is asserted for bytes absent from this lane. MISSES if: repeats left untouched or tree-hash-pinning requirement ("receipts must pin a tree hash of read inputs") is not carried into the round-65 instrument.

### R2 — MEDIUM (lesson line 85)

Operative quote: "`reports/round-63/telemetry/revisions.txt:12-13` still asserts `8d2041fa` added `final-measures-c.txt` — false (added by 0c892ce; path absent at 8d2041fa). Named correction entry, append-only."

Ground truth (verified here): `reports/round-63/telemetry/revisions.txt:11` = "added by `0c892ceac42f…`" while `:12-13` = "`8d2041fa` is the round-63 claim-C land commit and the commit that added this receipt." — the internal contradiction exists exactly as routed; the file already carries a round-64 appended "Correction (round 64, CaReceipts)" entry at `:14+`, establishing the append precedent.

Verdict contract — SATISFIES if a new named correction entry is APPENDED (to revisions.txt or a named corrections file) stating old→new. OVER-REACHES if lines 12–13 are edited/deleted in place (routing demands append-only). MISSES if no entry names the specific `8d2041fa`→`0c892ce` fact and the `path absent at 8d2041fa` evidence.

### R3 — MEDIUM (lesson line 86)

Operative quote: "report cites `w2/ReviewerCa.md` — actual path `w1/ReviewerCa.md`. (SCORECARD cites both correctly.)"

Ground truth (verified here): actual file = `.ufo/waves/round-64/w1/ReviewerCa.md` (exists; no w2 copy). **The routing's parenthetical is FALSE at this tip:** `SCORECARD.md:1235` cites "`w2/ReviewerCa.md`, `w2/CaReceipts.md`" — i.e. SCORECARD repeats the wrong w2/ path for ReviewerCa. (CaReceipts is correctly at w2.) The report itself is cross-lane-absent (see R1).

Verdict contract — SATISFIES if the draft corrects/appends an erratum naming BOTH the report citation and `SCORECARD.md:1235`'s wrong `w2/ReviewerCa.md`, with old→new. OVER-REACHES if filed SCORECARD bytes are edited in place without disclosure, or if the draft trusts the parenthetical and skips SCORECARD (that is a MISS of the real surface). MISSES if only "the report" is named — the report is not in this lane, so a report-only fix corrects nothing reachable.

### R4 — MEDIUM, frozen wording (lesson line 87)

Operative quote: "`claims.json` O statement "ten byte-patched mutants each fail exactly their pinned leg" is contradicted by the lane's own `exactness-sweep-o.txt` (m1 also fails EDGE_USERINFO/EDGE_HTTPS; m2 also fails EDGE_MALTARG); frozen-predicate rule routes the wording; SCORECARD already states the honest version."

Ground truth (verified here): `reports/round-64/claims.json:44` carries the exact overstatement "…ten byte-patched mutants each fail exactly their pinned leg."; `reports/round-64/telemetry/exactness-sweep-o.txt:1` = "evidence that 'each mutant fails exactly its pinned leg' is false for m1 and m2" with `:6` declaring the m1/m2 pins; `SCORECARD.md:1234` already hedges ("10 mutants kill their pinned legs; m5 exactly, isolation-verified").

Verdict contract — SATISFIES if the draft keeps `claims.json` untouched (frozen-predicate bytes route the wording, they are not edited mid-flight) and records the disposition/named wording note in round-65 records, optionally pointing at SCORECARD's honest version. OVER-REACHES if `reports/round-64/claims.json` is edited — the statement is a frozen round-64 predicate; rewriting it in round 65 breaks the frozen-predicate rule even though the sentence is false. MISSES if the contradiction is left with no disposition entry anywhere.

### R5 — LOW (lesson line 88)

Operative quote: "`control-o.txt` binds counter rev3 `c27a9fef…` / measured `b7d22703`, not final rev5 — the report does not state the binding; name it next round."

Ground truth (verified here): `reports/round-64/telemetry/control-o.txt:1` binds measured `b7d22703dfb6…` (jj working copy @, parent 097c21d0), `:2` binds counter "(revision 3) sha256 c27a9fefb37c…" — the binding exists exactly as routed.

Verdict contract — SATISFIES if a round-65 record (report/lesson/LOG append) NAMES the rev3/b7d22703 binding and why the control predates final rev5. OVER-REACHES if `control-o.txt` itself is touched (nothing routes editing it). MISSES if no round-65 record names the binding.

### R6 — LOW (lesson line 89)

Operative quote: "lesson R64-M12 wave-2 status sentence ("closed in the worktree, open in the index") is a pre-land snapshot; at HEAD the S687 flip is committed in 95c9194e. Append a status correction."

Ground truth (verified here): `corpus/lessons/round-64.md:327` = "Wave-2 status: **closed in the worktree, open in the index.**" (the exact stale sentence); at this tip `corpus/SOURCES.md:642` S687 status cell = `queued` — the flip is landed, so the sentence is stale as routed.

Verdict contract — SATISFIES if a status correction is APPENDED (to the R64-M12 entry or a named erratum) with old→new and the landing commit. OVER-REACHES if `corpus/lessons/round-64.md:327` is rewritten in place — routing says "Append", and filed lessons are append-only records. MISSES if the correction lands without the "now committed" fact.

### R7 — LOW (lesson line 90)

Operative quote: "new entry's `verified-at: 2026-10-23` line still reads "skeleton structure prepared; cited source claims await L1 insertion" — stale after insertion; correct in round 65's entry touch or a named erratum."

Ground truth (verified here): `corpus/knowledge/linguistics/language-socialization-and-acquisition.md:5` = "- verified-at: 2026-10-23 — skeleton structure prepared; cited source claims await L1 insertion and review." — stale exactly as routed (claims were inserted and reviewed; verified-at predates the round-64 land).

Verdict contract — SATISFIES if the line is corrected WITHIN a sanctioned channel: round 65's entry touch (corpus diffs are routinely landed and NOHARM-scoped) or a named erratum, keeping old→new visible in the round's records. OVER-REACHES only if the edit lands outside the declared touch scope (silent drive-by on an unrelated filed entry with no record). MISSES if the stale line survives with no erratum.

## 2. Divergences between the routing text and observable tip state

1. **R1 report leg unreachable (HIGH for the fixer):** the "report line" repeat and R3's report citation live in `.ufo/reports/round-64/kotodama.md`, which is absent from this lane tree AND all local history (`git log --all` empty; `8bab271c` and `e1fe5c97` not resolvable here — round-64 was a different lane repo). No draft produced in this lane can honestly claim that leg done; it must be declared a cross-lane dependency.
2. **R3 parenthetical false (MEDIUM):** "(SCORECARD cites both correctly.)" does not hold — `SCORECARD.md:1235` cites `w2/ReviewerCa.md` while the file is at `w1/`. The real R3 surface is report (unreachable) + SCORECARD:1235 (reachable). A draft that believes the parenthetical will miss the only reachable instance.
3. **Draft dependency:** `stage/records-fix/` absent through 01:54; verdicts in §1 remain pre-registered contracts, not measured verdicts.

## 3. Confidence

- Quotes: verbatim from §6, high confidence (lines 84–90 re-read raw).
- Filed-bytes evidence: high confidence — every line cited above was read at this tip during this session (01:45–01:54).
- att-r1 fixture intent: [INFERENCE] — presence verified, purpose not.
- Per-defect satisfies/over-reach/miss verdicts: not measurable this session (draft absent); contracts are pre-registered against verified ground truth, so stamping is mechanical once ExecRecordsFix lands.
