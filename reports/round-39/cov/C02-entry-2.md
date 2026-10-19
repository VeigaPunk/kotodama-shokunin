- Seat: C02 | executor | claim C | date 2026-10-19 | baseline dfb0719

# C02 — verification entry 2 of 4 (draft bytes for the integrator)

Mission (verbatim, `reports/round-39/targets.json` seat C02): *"Author entry 2 with the same contract."* Out path: `reports/round-39/cov/C02-entry-2.md`. Contract applied: the round-35/36 entry contract (head-block fields, sources with locators, gap statement, decision record), instantiated in the verification partition's house style (`corpus/knowledge/verification/two-reader-interop-agreement.md:1-19` is the field-shape exemplar).

Dependency status: `reports/round-39/scout/K01-verification-gaps.md` and `reports/round-39/plan/P01-plan.md` were **absent at seat time** (`ls reports/round-39` → `claims.json targets.json telemetry` only, checked twice before this write). Per the missing-dependency rule this seat selected its own topic from a live census (below), and records the slug claim for X00's collision matrix under `## Owed`.

**Proposed target path (integrator applies):** `corpus/knowledge/verification/index-sweep-verification.md`

---

```markdown
# Index-sweep verification — re-measuring a corpus index against the files it indexes

- topic: The verification procedure for the **corpus-index sweep** — the recurring, selftested instrument that re-measures `corpus/README.md` against the file tree it indexes (index rows vs `.md` files, missing rows, ghost rows, duplicate rows, row-topic byte-equality, section-header counts, the totals line, the counts footer) — and the contract that keeps a sweep honest: every present-tense claim the index makes gets a measured leg, a claim with no leg is a finding rather than a pass, and a green reading is a digest-pinned reading of one tree state, never a state of the world. Covers the leg table, the three filed failures that wrote the contract (r19 paraphrase rows "asserted rather than measured", r20's never-committed `.scratch` sweep, r27's footer-blind green over rev 1.7's stale counts footer), the planted-control battery, green-reading discipline, and the append-only repair rule. Method and lane policy only; canon belongs to lore-shokunin.
- gap filled: the partition carries single-tool verification (`verification-method-overview.md`), entry-header count readings (`header-conformance-readings.md`), interop comparison (`two-reader-interop-agreement.md`) and independence discipline (`verification-independence-anti-circularity.md`), but no entry owns the index-vs-tree sweep that every corpus landing since round 10 has relied on. Absence sweep 2026-10-19 at baseline dfb0719: `grep -rliE "index sweep|counts footer|totals line|header drift|ghost row|orphan row|duplicate row" corpus/knowledge/` → 0 files; the nearest strings are false friends (`ghost` alone hits 13 folklore files; `topic mismatch` appears once, `linguistics/register-strata-attestation.md:31`, quoting a sweep output line — a mention, not a topic owner).
- sources:
  - KTD-IS-S-0001 — `reports/round-28/readme/sweep.py:2-16` — the R28-C47 docstring: round 27's sweep "did **not** check the counts footer, and that is where round 28 found a live defect"; revision 1.7 moved `## linguistics/` 19 → 20 and the totals line 199 → 200 "but left this present-tense footer reading 199/19"; the instrument "adds that leg" (`:15`).
  - KTD-IS-S-0002 — `reports/round-28/readme/sweep.py:18-26` — the leg declaration "Legs (all measured, none asserted)": the inherited index legs, the footer leg (the `Counts checked <date>` block's total and six directory totals vs the live tree), and the separate totals-block leg.
  - KTD-IS-S-0003 — `reports/round-28/readme/sweep.py:64-71` — `FOOTER_RE`: the footer's shape is a dated present-tense claim that carries its own counting command, a file total and the six directory totals in section order; `:345-380` — the three new controls (stale footer TOTAL; stale footer DIRECTORY vector with a matching total; ABSENT footer flagged, not silently passed); `:419` — selftest verdict line "12/12 checks passed".
  - KTD-IS-S-0004 — `reports/round-27/readme/sweep.py:2-28` — the seven-leg predecessor (rows, files, topic byte-equality with continuation lines space-joined, ghosts, missing, header drift, totals line), its conventions "inherited by measurement from rounds 10/19/20" and the history note that round 20's sweep "lived in `.scratch/` and was never committed" (`:19-22`); its ok-gate (`:133`) contains no footer term and its selftest reports "9/9" (`:314`) — the honest shape of a seven-leg instrument, recorded as the boundary of what its greens covered.
  - KTD-IS-S-0005 — `corpus/README.md:43-55` — revision 1.8's defect record: the stale present-tense footer, and the reason statement that round 27's sweep "never reads the counts footer, so it went green over a stale claim" (`:52-55`).
  - KTD-IS-S-0006 — `corpus/README.md:95-101` — revision 1.5's repair: the ten round-19 rows "carried condensed paraphrases instead of the entries' own `- topic:` text, and the round-19 auditor's tool states it never compared a row's description with its file's content … so revision 1.4's '0 topic mismatches' was asserted rather than measured" (`:97-101`).
  - KTD-IS-S-0007 — `reports/round-19/audit/x27-coverage-readme-vs-files.md:47-49` — the audit "answers the *index↔files* question only … does not verify that an indexed description matches its file's content"; `:83-86` — a mid-wave DIRTY reading is "the expected intermediate state" of an append-only wave, not a defect; `:132-136` — the reconciliation is "a multi-write act, not atomic" (rows read clean about two minutes before the `revision:` bump); `:140-142` — "Structural comparison only … does not audit the row descriptions" or the Known-gaps section.
  - KTD-IS-S-0008 — `reports/round-20/readme/verify.md:21-30` — the round-20 sweep re-run from a `.scratch` copy (exit 0, 199/199, selftest 10/10) and `:63-74` — V3/V4, the planted-repair re-run and the controls leg ("the sweep can fail"); the conventions ledger `reports/round-20/readme/reconcile.md` §2, which the round-27 instrument names as inherited (`reports/round-27/readme/sweep.py:19-21`).
  - KTD-IS-S-0009 — the landing receipts the legs read: `corpus/README.md:14-28` (revision 2.0 — ten rows added in filename order byte-equal to each entry's `- topic:` text; "0 missing, 0 ghosts, 0 duplicate rows, 0 header drift, 0 topic mismatches, totals line 211, footer 211 / 21/23/24/29/20/94, exit 0 — measured at close"), `corpus/README.md:11` (revision 2.1 — re-measured with the r28 instrument at landing: "212 rows vs 212 files, exit 0"), and the read objects themselves, `corpus/README.md:505` (totals line) and `:507-510` (counts footer block).
  - KTD-IS-S-0010 — measured this round, 2026-10-19, seat C02, baseline dfb0719 (`dfb0719711204b5943432034bd80c8dc248acddd`), no filed-round script executed as a process: (a) an inline replication of all seven index legs plus both footer legs over the live README/tree → 212 rows vs 212 files, 0 missing, 0 ghosts, 0 duplicate rows, 0 header drift, 0 topic mismatches, totals line 212 ok, footer total 212 with vector 21/23/25/29/20/94 ok (README sha256 `b80274bcd24b8b6e621f499fb20d4a07aa3b7b48dbb3508e0a9ac974f68e1d74`); (b) the filed round-28 instrument exec'd in memory from its filed bytes (sha256 `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`, 17,117 bytes) → selftest 12/12 PASS and its live leg agrees (`ok True`, `footer_ok True`); (c) three in-memory controls over the replication (planted paraphrase row, stale footer total, absent footer) each flagged.
  - KTD-IS-S-0011 — inherited bibliography (no network at seat time; calibration, not evidence): Dijkstra's testing epigram — testing shows the presence of bugs, never their absence — "Notes on Structured Programming" (EWD249) (to-verify: exact report number and edition not re-read this seat); the Reproducible Builds project docs, already cited in-corpus at `two-reader-interop-agreement.md:13` (inherited through that entry; anything beyond what it carries is to-verify).
- calibration: the leg set, the absent-leg rule and the repair rule are this lane's house policy assembled from its own filed defect records — not a published standard, and not a claim about any real corpus beyond this one; Dijkstra's epigram is the general calibration warning behind §5 (a green sweep is not truth), carried inherited and to-verify for its exact source; the Reproducible Builds docs are an engineering reference inherited through an in-corpus entry; no real culture is described, and the index counts markers, not verified facts (`corpus/README.md:510`).
- couples: verification — `header-conformance-readings.md` (the boundary: that entry owns how an entry-header count may be quoted, this one owns the index-vs-tree question; a circulating count carries its reading id under either), `verification-method-overview.md`, `verification-independence-anti-circularity.md` (a re-run sweep must not become a blessing; the re-pin admissibility rules apply to re-readings), `internal-consistency-audit.md`, `gate-battery-surface-verification.md`, `generated-artifact-roundtrip-verification.md`, `two-reader-interop-agreement.md` (the sweep is itself a two-reader check: index rows and disk files are independent readers of the corpus); synthesis — `../synthesis/consistency-verification-checklist.md`, `../synthesis/finding-disposition-workflow.md` (a sweep finding is dispositioned like a gate finding), `../synthesis/generated-artifact-lifecycle.md`; tooling — `reports/round-27/readme/sweep.py`, `reports/round-28/readme/sweep.py`, `reports/round-19/audit/coverage-audit.py`, `reports/round-20/readme/reconcile.md`, `reports/round-20/readme/verify.md`, `tools/source-audit-inventory.py`; siblings — lore-shokunin owns canon; chousa-shokunin owns general research method.
- source: the procedure is house policy assembled from the lane's filed instruments and defect records; every repo locator above was re-read at baseline dfb0719 in this seat (command transcript in the seat fragment). No URL was fetched (no network at seat time), so the two inherited references carry to-verify.
- verified-at: 2026-10-19 — round-39 authoring pass, seat C02, baseline dfb0719: live sweep replication green (212 rows vs 212 files, footer ok), the filed round-28 instrument's selftest 12/12 from its filed bytes, the absence sweep 0 files over six instrument-term patterns, and every `path:line` in `- sources:` re-read; the green reading is pinned to README sha256 `b80274bcd24b8b6e621f499fb20d4a07aa3b7b48dbb3508e0a9ac974f68e1d74`.
- recheck: after every corpus landing, before the README's totals line, counts footer, or any "rows vs files" claim circulates; whenever an index count is quoted without its reading id; and whenever a sweep instrument gains or loses a leg — an instrument-shape change re-reads every claim the old green covered (the round-27→28 transition is the worked case).

## 1. What this entry licenses

- A **re-measurement procedure**, not an index: how to prove that `corpus/README.md` still describes `corpus/knowledge/**`, and what a green reading does and does not license afterwards.
- The rule the filed defects force: **every present-tense claim the index makes gets a leg, and a claim with no leg is a finding, not a pass.** A sweep that reads seven of the index's claims is not mostly green — it is unaudited for the rest.
- Green is a **reading at a digest**: `ok: true` is true of one README text (sha256-pinned, the instrument returns the digest with the verdict) against one tree state, never of "the corpus is fine".
- Boundary: `header-conformance-readings.md` owns the readings of *entry-header* counts; this entry owns the *index-vs-tree* question. The two meet in the house rule that no count circulates without its reading id.

## 2. The legs — one per present-tense claim the index makes

| # | leg | the index claim it reads | where defined |
|---|---|---|---|
| 1 | rows vs files | every `- `name.md` — topic` row names a real file, and every file has a row | inherited from r27 (`reports/round-27/readme/sweep.py:2-28`) |
| 2 | missing rows | a file with no row surfaces as `missing_from_index` | same |
| 3 | ghost rows | a row naming no file surfaces as `orphan_rows` | same |
| 4 | duplicate rows | the same file indexed twice is reported | same |
| 5 | topic equality | each row's topic is byte-equal to the entry's own `- topic:` head-block text, continuation lines space-joined; a paraphrase or truncation is a `REWRITE` mismatch | same |
| 6 | header drift | each `## <part>/ (N)` count equals the live file count | same |
| 7 | totals line | `Total knowledge entries: N.` equals the file total | same |
| 8 | counts footer | the `Counts checked <date>` block's total and six-directory vector equal the live tree, in the README's section order | added by r28 (`reports/round-28/readme/sweep.py:18-26`, `:64-71`) |
| 9 | totals block | the same total read separately so a totals-only drift is visible | added by r28 (same) |

- The r28 ok-gate requires the footer legs too: `ok` is false when `footer_findings` is non-empty (`reports/round-28/readme/sweep.py:191-194`), where the r27 gate (`:133`) was silent about the footer.
- Legs 1–7 are structural; leg 5 is the one that makes the index *descriptive* rather than merely *complete* — the r19 paraphrase rows were complete and wrong.

## 3. The filed failures that wrote the contract

| failure | what went green anyway | the leg/rule it added |
|---|---|---|
| round 19: ten rows carried condensed paraphrases; the auditor's tool "never compared a row's description with its file's content", so "0 topic mismatches" was asserted rather than measured (`corpus/README.md:95-101`; `reports/round-19/audit/x27-coverage-readme-vs-files.md:47-49`) | an index↔files audit reading CLEAN over wrong descriptions | leg 5 (byte-equality, not presence); rule: a check's limits are recorded, not implied |
| round 20: the sweep lived in `.scratch/` and was never committed (`reports/round-27/readme/sweep.py:19-22`) | an unreproducible green | rule: the instrument is a filed, selftested artifact, not a scratch script |
| round 28: revision 1.7 moved the section header and the totals line in one file and left the present-tense counts footer at 199/19; the seven-leg sweep "went green over a stale claim" (`corpus/README.md:43-55`) | a fully green 7-leg reading over a stale index | legs 8–9 plus the FOOTER_ABSENT and FOOTER_DIR_TOTALS controls (`reports/round-28/readme/sweep.py:345-380`) |

- The pattern across all three: the defect was never in the checked legs — it was in the **unchecked claim**. That is why the absent-leg rule (§5) is a finding class and not a style note.

## 4. Controls — proving the sweep can fail

| planted condition | required result | filed at |
|---|---|---|
| a paraphrased row | 1 `REWRITE` topic mismatch | r27 selftest + r28 (`:302-312`) |
| a truncated topic (the r19 defect class) | 1 topic mismatch | r27 selftest |
| a ghost row | `orphan_rows` names it | r27 + r28 |
| a deleted row | `missing_from_index` names the file | r27 + r28 |
| a wrong `## part/ (N)` count | header drift names the partition | r27 + r28 |
| a wrong totals line | `totals_ok` false, `ok` false | r27 + r28 |
| a duplicated row | `duplicate_rows` names it | r27 + r28 |
| a stale footer total | `FOOTER_TOTAL`, `ok` false | r28 (`:345-357`) |
| a stale footer directory vector with a matching total | `FOOTER_DIR_TOTALS` without `FOOTER_TOTAL` | r28 (`:359-371`) |
| an absent footer | `FOOTER_ABSENT` — a missing claim is a finding | r28 (`:373-380`) |
| a correct fixture footer | PASS (the leg is not always-red) | r28 (`:382-392`) |
| continuation lines | space-joined, not newline-joined | r27 + r28 |

- Filed instruments carry 9 controls (r27, selftest line "9/9", `:314`) and 12 (r28, `:419`); the round-20 predecessor's controls are recorded in its receipts (`reports/round-20/readme/verify.md:63-74`). Re-proven this round on the replication and by the exec'd instrument (KTD-IS-S-0010).

## 5. Reading a green sweep — what green is and never proves

- **Quote the reading, not the state**: a green sweep is cited with the README sha256, the instrument identity (filed path + selftest verdict) and the date. A bare "the index is clean" is the asserted-not-measured class.
- **The absent-leg rule**: `FOOTER_ABSENT` is a finding (`reports/round-28/readme/sweep.py:373-380`). A sweep never passes over a claim it does not read, and an instrument that gains a leg retroactively limits its old greens — the r27 greens did not cover the footer, which is exactly where the r28 defect was.
- **Mid-wave readings are snapshots**: an append-only wave shows DIRTY between the file landings and the index reconciliation (`reports/round-19/audit/x27-coverage-readme-vs-files.md:83-86`); only the at-close reading is a verdict, and the reconciliation is multi-write — rows can read clean while the `revision:` bump is still in flight (`:132-136`).
- **Green is not truth**: the sweep proves the index describes the files; it says nothing about whether the files are true. The footer itself says "The inventory counts markers, not verified facts" (`corpus/README.md:510`).
- **Scope limit is part of the reading**: a structural sweep does not audit the `Known gaps (frontier)` prose or the `to-verify` inventory (`reports/round-19/audit/x27-coverage-readme-vs-files.md:140-142`); quoting a green sweep as auditing those is the same asserted-not-measured class.

## 6. Repair discipline — a finding triggers an append-only landing

- **Rows**: added in filename order, byte-equal to the entry's own `- topic:` text (continuations space-joined) — never a paraphrase (revision 1.5's recorded lesson).
- **Counts move together**: the section header count, the totals line, and the counts footer (total and six-vector) are one landing transaction; revision 1.8 is the recorded cost of splitting it.
- **Revision blocks are append-only**: a landing writes a NEW revision block with its own re-measurement line; a filed revision block is never edited in place, and superseded readings stay as dated records ("preserved below as the dated record it was", `corpus/README.md:52`).
- **Disposition, not silence**: a sweep finding is dispositioned like a gate finding (`../synthesis/finding-disposition-workflow.md`) — repaired, deferred with an owner, or recorded as expected (mid-wave) — and the disposition cites the re-run that cleared it.

## 7. Decision record

1. **Adopted (DR-IS-01):** every present-tense claim the index makes gets a measured leg; a claim with no leg is a `FOOTER_ABSENT`-class finding, never a pass (§2, §5; `reports/round-28/readme/sweep.py:373-380`).
2. **Adopted (DR-IS-02):** row topics are byte-equal to the entry's `- topic:` text with continuations space-joined; paraphrase and truncation are `REWRITE` defects (§2 leg 5; `corpus/README.md:95-101`).
3. **Adopted (DR-IS-03):** a green reading is quoted only with the README digest, the instrument identity and its selftest verdict, and the date; a count without its reading is the asserted-not-measured class (§5; `corpus/README.md:101`).
4. **Adopted (DR-IS-04):** the header count, the totals line and the counts footer move in one landing; the footer's directory vector is checked even when the total matches (`FOOTER_DIR_TOTALS`; `reports/round-28/readme/sweep.py:359-371`).
5. **Adopted (DR-IS-05):** the sweep instrument is a filed, selftested artifact with an absent-footer control and at least one always-passing control; `.scratch`-only sweeps are not evidence (§3; `reports/round-27/readme/sweep.py:19-22`).
6. **Adopted (DR-IS-06):** a mid-wave DIRTY reading is reported as a snapshot with its stamp; only the at-close reading is a verdict, and the multi-write window is recorded, not smoothed over (`reports/round-19/audit/x27-coverage-readme-vs-files.md:83-86,:132-136`).
7. **Adopted (DR-IS-07):** repairs are append-only — new rows in filename order, a new revision block per landing, superseded readings preserved as dated records (§6; `corpus/README.md:52`).
8. **Rejected (DR-IS-08):** reading a green sweep as correctness, truth, or canon — the sweep audits description, not veracity, and the inventory counts markers, not verified facts; canon belongs to lore-shokunin (`corpus/README.md:510`).
9. **Open (DR-IS-09, to-verify):** whether a sweep leg should also read the `Known gaps (frontier)` bullets' reproduction commands for staleness — the recorded audits state that section is outside the structural comparison (`reports/round-19/audit/x27-coverage-readme-vs-files.md:140-142`). Owner: this lane's O/D boundary; not disposed here.
```

---

## Self-audit (replicated checks, run at authoring time; no filed-round runner executed)

- Fence shape for the stagers: exactly one ` ```markdown ` outer fence closed by the next ` ``` ` line, **no** three-backtick fence or line inside the entry body (the round-35 CANNOT-EVALUATE hazard, `reports/round-35/cov/C02-entry-2.md` Finding 4). Measured on this fragment: `fenced_blocks_found: 1`, `internal_fence_lines: 0` — the regex `^```(?:markdown|md)\s*$([\s\S]*?)^```\s*$` (the r35 stager shape) stages the full block.
- Replicated round-19 entry-audit regexes (the `entry-audit.py:25-31` pattern, replicated inline, never executed from a filed round path) over the extracted block: `header_fields: ['Boundary', 'calibration', 'couples', 'recheck', 'source', 'sources', 'topic', 'verified-at']` — `Boundary` is a `## 1` bullet the field regex over-matches, not a head-block field; `header_missing_required: []` (required = topic, sources, couples); `header_tail_ok: True`; `gap_named: True` (GAP_RE hits "gap filled"); `decision_record: True` with 9 `DR-IS` rows; `calibration_flagged: True`; `canon_hygiene: True` (lore-shokunin named).
- Source leg: `source_bullets: 11` (KTD-IS-S-0001..0011), every bullet carrying locators; `locator_cites: 24` `path:line` references, all asserted needle-in-line at baseline dfb0719. Two anchors were corrected after first assertion, both check-side or off-by-one, and re-asserted OK: `corpus/README.md` "dated record it was" is at `:52`, not `:51` (the entry's two `:51` cites were amended to `:52` — this moved the staged digest, see below); the `reports/round-28/readme/sweep.py:191-194` ok-gate needle spans `:192-193` and needs a range-join to assert. `(to-verify)` metric, stated per the round-35 Finding-5 discipline: 1 parenthesized detailed form (KTD-IS-S-0011's Dijkstra line), 6 total occurrences (2 in S-0011, 1 each in `- calibration:`, `- source:`, §5 scope-limit bullet, DR-IS-09).
- Couples: 9 `.md` targets extracted from the couples line, `unresolved: []` (resolver candidates: entry dir, `corpus/knowledge/`, lane root); the four non-`.md` tooling paths resolve separately (checked in the same pass: `reports/round-27/readme/sweep.py`, `reports/round-28/readme/sweep.py`, `reports/round-19/audit/coverage-audit.py`, `tools/source-audit-inventory.py`).
- Shape: 103 lines / 19,745 bytes, 7 `##` sections (inside the partition's 7–14 band; the r19 procedure entries run 80–93 lines and registries 159–252 — this sits between), `- topic:` a single line (row-emittable byte-equal).
- **Staged digest for C05**: the entry block's sha256 is `eabb1d63ddc66b7c6c4c2767078aa3072cc44b1a90d290a67946f3f97481c174` (19,745 bytes, 103 lines — byte count unchanged by the `:51`→`:52` amendments), computed on the fenced block exactly as extracted by the stager regex above; audit these bytes, and re-run if the fragment is revised (the digest moves with any in-block edit). Superseded digest of the pre-amendment block: `41ffc5ad5ccb1455f2c994de62dba731f11e3ab8cf33ef9ca8c1b8d25675cc04`.

## Owed

- `reports/round-39/scout/K01-verification-gaps.md` and `reports/round-39/plan/P01-plan.md` — absent at seat time (checked twice). This seat self-selected the topic from the live census above and files the slug claim: `index-sweep-verification` → verification → seat C02. If K01/P01 assign slot 2 differently, renumber or supersede per the round-35 collision rule (`reports/round-35/cov/C02-entry-2.md` `## Owed` precedent): the later author appends `-b` to the slug and says so in the gap line.
- Topic de-collision for X00: the three sibling executors (C01, C03, C04) had **not landed** at this write. This seat's topic occupies the index-sweep/README-reconciliation register. Adjacent registers this entry does NOT claim, so siblings may: the isolation-replay of filed round runners (claim-Ca territory: worktree replay, basename-couples policy), digest-pin/re-pin admissibility as a standalone entry, entry-header count readings (owned by `header-conformance-readings.md`), and telemetry closing snapshots. **Re-checked after C01 and C04 landed**: C01 → `worked-example-verification.md`, C04 → `append-only-record-verification.md` (its fragment discusses "README index-sweep verification" as a candidate it ranked weaker — discussion, not a claim; `reports/round-39/cov/C04-entry-4.md:161`). C03 had not landed at this re-check — the only residual collision risk.
- **README row, for C06/integrator**: the index row must be emitted from this entry's own `- topic:` text, byte-equal, continuation-joined if ever wrapped (round-35 C17 note (i) precedent). The `- topic:` line above is a single line. Partition header moves `## verification/ (20)` → `(24)`; totals 212 → 216; footer vector 21/23/25/29/20/94 → 21/**24**/25/29/20/94 — one landing transaction per DR-IS-04.
- **Independent audit** by C05 at the staged digest (recorded in `## Self-audit` after MEASURED-PENDING is replaced), per the round-35 C17 pattern; re-run on final bytes if this fragment is revised.
- **External-source fetch pass (network)**: the two inherited references (KTD-IS-S-0011) carry `(to-verify)` and need a fetch/read before any figure or attribution in them is quoted beyond what `two-reader-interop-agreement.md:13` already carries. This seat had no network per its dispatch.

## Citations

- `reports/round-39/targets.json` — seat C02 object (`mission`, `out`), `shared_rules`; `reports/round-39/claims.json` — claim C (contract: head-block fields, sources, gap statement, decision record), baseline `dfb0719`.
- `REGIMEN.md:25-50` — per-round contract; `:60-69` scope.
- `corpus/README.md:11,:14-28,:43-55,:52,:95-101,:505,:507-510` — the revision ledger and the read objects (rev 2.1 landing sweep, rev 2.0 receipt, rev 1.8 defect, rev 1.5 repair, the dated-record convention line, totals line, counts footer).
- `reports/round-27/readme/sweep.py:2-28,:133,:314,:19-22` — the seven-leg instrument, its ok-gate, its 9/9 selftest, the never-committed r20 history.
- `reports/round-28/readme/sweep.py:2-16,:18-26,:64-71,:191-194,:239-408,:345-380,:419` — the footer legs, the footer regex, the extended ok-gate, the 12-control selftest, and the three new controls.
- `reports/round-19/audit/x27-coverage-readme-vs-files.md:47-49,:83-86,:132-136,:140-142` — the structural-only limit, the mid-wave snapshot rule, the multi-write timing note; `reports/round-19/audit/coverage-audit.py` — that audit's tool (path-cited, not run).
- `reports/round-20/readme/verify.md:21-30,:63-74`; `reports/round-20/readme/reconcile.md` §2 — the round-20 receipts and conventions ledger.
- `corpus/knowledge/verification/two-reader-interop-agreement.md:1-19,:13` — the partition's field-shape exemplar and the inherited Reproducible Builds citation; `corpus/knowledge/verification/header-conformance-readings.md` — the boundary entry (path-cited).
- `reports/round-35/cov/C02-entry-2.md` — the contract exemplar and the fence-shape/`-b`-collision precedents cited in `## Owed`.
- Commands run this seat (transcripts quoted in `## Self-audit`): the census greps; `git rev-parse --short HEAD` → `dfb0719`; the inline sweep replication + 3 in-memory controls; the exec'd r28 instrument selftest (12/12) + live leg; the absence sweep; the 21 path:line anchor assertions (19 first-pass OK, 2 needle typos corrected and re-asserted OK).
