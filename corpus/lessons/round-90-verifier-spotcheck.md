# Round 90 — non-author verifier spot-check

author: hyaku closure (non-author integrator, @m_zfl)
checked: 2026-11-05 (America/Sao_Paulo) against lane tip `6394ad434e6995a5e5395652f01e7eeff560860c` (`main`, pushed).
subject: lane round 90, claims O (operability, capability acquisition) and C (coverage, sourced claim).
authorship: the kotodama lane and its dispatched seats authored round 90. This file is written by a fresh integrator that authored no round-90 change.

Method. Plain measurements were run over committed bytes (`git show <tip>:<path>`, `git diff`, `git ls-tree`, `sha256sum`, `wc`, `grep`, and the census script). Lane-owned gates were NOT executed; their committed receipts were verified instead (PROTOCOL §Gate standard, closure consequence). Sources were re-opened live with `curl -sS -L`, and each live body was compared with the committed capture.

Legend. `re-measured` = I ran the measurement myself. `evidence-verified` = I checked a committed receipt and did not re-run it.

## 1. Conformance (PROTOCOL §Round-robin step 1)

| item | observed | ruling |
|---|---|---|
| report filed by lane identity | `git log --format='%an %H' -- .ufo/reports/round-90/kotodama.md` → author `kotodama-shokunin` on `c109f0e8`, `f07d2c3d`, `882866cd` | landed. The last commit `882866cd` is a hyaku sweep commit (subject "L1 returned without committing; attribution defect"). Attribution defect recorded here; status-neutral. |
| `SHONEN` heading, one line per box | `## SHONEN` present; four lines, all `[~]` with pointers; no `[x]` | pass (re-measured) |
| cited lane hashes are ancestors of the branch | 15 hashes cited in the report (`6b0b86e4 945e6a3e d0b6f2a7 9fb2c58f c0c628d8 ebd81b1b 7f3a7aa6 210c0dd0 e0795be6 3f56892f 26e30795 195aff9c 19187112 fe59fc35 6394ad43`); `git merge-base --is-ancestor <h> main` true for all | pass (re-measured). `6e1ea6a5` and `121888f0` in the report are sha256 prefixes, not commits. |
| lane clean and pushed | `jj-lane.sh state …` → `branch=main local=6394ad43 remote=6394ad43 ahead=0 behind=0 tracked=0 untracked=0`; `git status --porcelain` empty; `ls-remote origin refs/heads/main` → `6394ad43…` | pass (re-measured) |
| prompt carries the template contract | `.ufo/prompts/kotodama-round-90.md` (92,487 B) has §1 MISSION/AXES, §2 claims, §2b frontier step, §3 L2 floor, §4 report contract, §5 commit/push/L0; the five child-lane items are present; `grep -c '^## SHONEN'` instruction and the Sources & frontier and trend-verdict requirements are present. `templates/round-prompt.md` carries the same report-contract lines (grep). | pass (re-measured by keyword grep) |
| watchdog digest | the 10 digest lines the orchestrator supplied (launch 20:12:06 → complete 00:50:51) match `.ufo/watchdog.log` byte for byte. The log also holds four earlier kotodama round-90 lines (19:33:36 launch, 19:46:42 dead, 19:46:44 launch, 20:12:04 dead) that the digest omits. | pass; omission noted |
| reported-count defects | report and SCORECARD say the entry has "10 `##` headings"; bytes have 8 `## ` headings | defect, status-neutral; routed |
| lowest-axis clause | AXES.md: at least one claim works the lowest non-retired axis unless the stagnation nudge waives it. The lane's stated lowest axis is freshness, paused by open L0 `round-11`/`round-89`. The stagnation nudge was not invoked (O entered the capabilities table this round). No numeric axis scores exist to confirm "lowest" (numeric-mapping debt R86-C1). | defect, status-neutral; the blocker is an operator ruling, not the lane |
| stale-lane line | report says only "this lane holds no other open mission"; the progressing/silent grade is not stated | defect, status-neutral |
| frozen-predicate defects (disclosed by the lane) | (a) `O.after_target` and `O.predicate` say the stub receipt records the stub failing SELFTEST and MUTATION; the receipt records `SELFTEST PASS 67/67` (rc 0) for the stub, REFUSALS 0/13, MUTATION 0/43. (b) `O.before` cites `reports/round-89/mutation-score.txt`, absent at base; the real receipt is `.ufo/waves/round-89/w1/MutationCounter.md`, present at base, which shows the 10/41 result. | disclosed, not repaired; see §2 O |

## 2. Claims re-check (PROTOCOL §Gate standard; `reports/round-90/claims.json`)

### Claim O — operability, capability acquisition

- before (re-measured): `git cat-file -e 6b0b86e4:tools/check-advance-evidence.py` → `fatal: path … exists on disk, but not in '6b0b86e4…'`. The tool is absent at base. The round-89 receipt `.ufo/waves/round-89/w1/MutationCounter.md` at base carries the 10/41 result the lane cites.
- after, tool identity (re-measured): `git show 6394ad43:tools/check-advance-evidence.py | sha256sum` → `121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed`, equal to `claims.json` `tool_sha256` and the freeze pin.
- counter identity (re-measured): `git show 6394ad43:reports/round-90/measure90.py | sha256sum` → `6e1ea6a5f96c…`, equal to counter revision 6 in `counter-revisions.md`.
- legs (evidence-verified; the counter was not re-run):
  - `reports/round-90/final/lands-O-final.txt` at tip: `LEG PASS TOOL`; `LEG PASS SELFTEST … SELFTEST PASS 67/67`; `LEG PASS REFUSALS … all ok`; `LEG PASS MUTATION … MUTATION-SCORE: 43/43 killed, 0 survived, 0 broken-pattern`; `MEASURE90-O: PASS legs=6/6`.
  - `reports/round-90/mutation-score.txt`: 43 lines beginning `  KILLED` (re-measured by grep); header `43/43 killed, 0 survived, 0 broken-pattern`.
  - `reports/round-90/final/separability.txt`: O overlay `PASS legs=6/6` with the six C paths absent.
- STUB leg (the one defect): `reports/round-90/controls/stub-tool.txt` records the stub's SELFTEST as `rc=0 SELFTEST PASS 67/67` (re-measured by grep: one such line), REFUSALS `0/13`, and MUTATION `0/43 killed, 43 broken-pattern`. The frozen sentence "records the stub failing SELFTEST and MUTATION" is false on its SELFTEST half. The O kill rule enumerates what kills O: tool sha, selftest tally, surviving or broken mutants, and a refusal not printed ok. None of these is a stub-receipt wording. The stub's discrimination is carried by REFUSALS 0/13 and MUTATION 0/43, which the receipt does record. Ruling: over-claimed frozen text, disclosed by the lane; it does not move the O verdict. It is routed (§6 item 1) because the STUB leg as the counter implements it (`observed=recorded`) is a presence check and cannot fail.
- bounds (not disputed): the lane's own falsification table shows 14 of 21 independent entry-mode mutants survive the selftest, and an 11-line stub that prints the tally and the 13 case names passes SELFTEST and REFUSALS (`CriticClaims`). These limit what O proves; they are not frozen-predicate failures.
- O verdict: **improved**. Re-measured: base absence, tool sha, counter sha, and SCORECARD append-only (`git diff --numstat 6b0b86e4 6394ad43 -- SCORECARD.md` → `49 0`). Evidence-verified: selftest tally, refusals, mutation receipt, stub control.

### Claim C — coverage, sourced claim

- entry `corpus/knowledge/linguistics/petitionary-and-votive-formulae.md` (re-measured):
  - `git show 6394ad43:<entry> | wc -c` → `20400` (≥ 12000 ✓)
  - `grep -c '^## '` → `8` (≥ 6 ✓; the report's "10" is wrong)
  - header keys present: `- topic:`, `- sources: S942 S943 S944 S945 S946 S947 S948`, `- verified-at: 2026-11-04`, `- recheck: 180d`
  - tables: one table with 5 data rows and 4 columns (5 pipes per line) → meets `table_min_rows 5`, `table_min_cols 3`
- registry (re-measured with `grep -cE '^\| S[0-9]+ \|'` and tier/status columns):

  | quantity | base `6b0b86e4` | tip `6394ad43` |
  |---|---|---|
  | rows | 865 | 875 |
  | tier A / B / C | 511 / 329 / 25 | 517 / 330 / 28 |
  | status mined / queued / rejected | 762 / 58 / 45 | 769 / 58 / 48 |

  New rows S942–S948 are `mined`, `opened 2026-11-04`, with `used-by` the entry (checked by column). S949–S951 are `rejected`; S949 has the lesson as `used-by`. S950 and S951 are rejected rows at tip.
- APPENDONLY (re-measured): `git diff --numstat 6b0b86e4 6394ad43 -- corpus/SOURCES.md` → `10 0`. Zero deleted lines; no existing row cell changed.
- linguistics partition (re-measured with `git ls-tree -r --name-only`): base 34, tip 35. `corpus/knowledge`: base 261, tip 262. `corpus/README.md` diff: `## linguistics/ (34)` → `(35)`, one index row, one round-90 section, `Total knowledge entries: 262`.
- census (re-measured): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit 0 (`ok` on `corpus/SOURCES.md`). Its warnings are the inherited W01/W04 rows; none names S942–S951.
- captures (re-measured): all ten `reports/round-90/evidence/S9xx.txt` match `manifest.json` by byte count and sha256; `http_status` is 200 for all ten.
- gate lines (re-measured): each of the ten quotes in the lesson's `## Gate` occurs in its own committed capture after entity and whitespace normalisation, with two exceptions noted below. Word counts are 12–22, all ≤ 25; minimum characters ≥ 20 for all.
  - S950 matches only after tags are removed.
  - S951 does not match a raw grep: the capture splits the sentence across `<b>` and `<a>` markup. It matches exactly once tags are removed with no replacement. The lesson should say the locator is tag-stripped text (routed, §6 item 6).
- INDEX: `CORPUS-INDEX: OK files=262 rows=262 findings=0` is evidence-verified from `final/lands-C-final.txt`. I did not run the index tool.
- C verdict: **improved**. Re-measured: counts, dimensions, APPENDONLY, captures, quote binding. Evidence-verified: the freeze-pinned ENTRY and INDEX legs.

### Other axes

- depth: **unchanged**. `git diff --name-status 6b0b86e4 6394ad43 -- corpus/knowledge` lists only the new `A` entry; no existing knowledge file changed.
- freshness: **unchanged**. No existing registry row changed (§2 C APPENDONLY); no `verified-at` or `recheck` moved; freshness is paused by open L0 questions.
- calibration: **unchanged**. No calibration claim declared (SCORECARD: "observation, no scored claim").
- adjacency: **unchanged**. No sibling-owned file changed; the entry hands the register to lore through `synthesis/worldbible-integration-contract.md` and leaves canon and research method alone.

## 3. Discernment spot-check (LEARNING.md)

Sample: the `## Gate` section of `corpus/lessons/round-90.md`. Three admits (S944, S946, S947) and three rejects (S949, S950, S951). Each source was re-opened live (`curl -sS -L`, HTTP 200); the live byte count is compared with the committed capture.

| item | decision | re-opened source (live) | agree/disagree | reason |
|---|---|---|---|---|
| S944 WALS ch. 71 prohibitive | admit (A) | `https://wals.info/chapter/71` → 200, 46,113 B, identical to capture | agree | The quote "The prohibitive uses the verbal construction of the second singular imperative and a sentential negative strategy found in (indicative) declaratives" is verbatim live. Map 71A reads 113 / 182 / 55 / 146, total 496. The entry's mood section ("113 of 496", "largest single class (182)") matches. The row's own word "minority pattern" for the 113 class is loose (113 is 23% of the sample; the 55 class is smaller), but the admit rests on the cited counts and is correct. |
| S946 IGI3 646 Smikros | admit (A) | `https://www.atticinscriptions.com/inscription/IGI3/646` → 200, 13,536 B, identical | agree | "ca. 510-500 BC", translator Edmund Stewart, and Stephen Tracy's objection quote are all present live. The gate line quotes the commentary note, so the admit is grounded. |
| S947 Blidstein PLOS One | admit (A) | `https://pmc.ncbi.nlm.nih.gov/articles/PMC13671548/` → 200, 295,969 B, identical | agree | Abstract quote "The results reveal a significant relative increase in the use of explicit votive terminology" is verbatim. "approximately 11,000 Greek dedicatory inscriptions" and the epigraphic-habit control appear in the same abstract. |
| S949 Wikipedia *Votive offering* | reject (C) | `https://en.wikipedia.org/wiki/Votive_offering` → 200, 182,592 B (committed capture 182,403 B: the page has drifted by 189 B since capture) | agree | Quote is present live. The page names no author and gives no corpus, so it cannot carry a votive claim under the tier rule. The flip condition is correctly stated. The drift does not affect the reject; the committed capture is the bound evidence. |
| S950 Wikipedia *Curse tablet* | reject (C) | `https://en.wikipedia.org/wiki/Curse_tablet` → 200, 318,144 B, identical | agree | Lead-section quote is present live. Tertiary text with no named author; the practice it describes is compulsion, not petition or vow. The reason is right. |
| S951 Wikipedia *Sacred language* | reject (C) | `https://en.wikipedia.org/wiki/Sacred_language` → 200, 425,389 B, identical | agree | Tertiary text with no named author and no corpus. The gate quote is present once markup is removed (§2 C gate lines). The locator method needs to say so (routed). |

Re-opened SOURCES row: `S944` in `corpus/SOURCES.md` (tier A, `mined`, opened 2026-11-04, recheck 90d, used-by the entry). Its gate-line quote is 20 words, within the ≤ 25 bound; the S945 gate-line quote is 14 words.

Sample result: 6 of 6 agree; 0 disagree. The sample is 6 of the 10 registry decisions this round. Discernment is improved on this sample. The grader's known survivors (§6 item 2) are instrument limits, not gate-decision disagreements.

## 4. Trend verdicts (LEARNING.md)

- **expansion: improved.** One admitted `knowledge/` entry on ground the coverage map did not hold: the base surface existed only as sub-sections of six entries and no dedicated file existed (base file count 34 → 35 in the partition, verified by `git ls-tree`; the base-surface grep in the lesson was not re-run). Its `sources:` line cites seven `mined` rows (S942–S948), each opened 2026-11-04 and `used-by` the entry. README gains one index row and the partition count moves 34 → 35.
- **quality: unchanged.** The LEARNING observable for `improved` is a weaker entry superseded by a stronger one, or stale entries re-verified, with no admitted entry failing its re-check. This round did neither: freshness is paused, no existing entry was re-verified or superseded, and no existing row changed. The instrument's gains (the grader, the counter revisions) are gating capability, not corpus quality, and are not counted here. The lane's report claims `improved`; the observable does not support it. The new entry is accurate on the numbers I re-measured (WALS 72 Map 72A 133/20/21/201 of 375; WALS 73 48/271 of 319 with the areal list; WALS 71 113/496), so no `harmed` ruling is warranted.
- **discernment: improved.** The spot-check agrees with the gate on admits and rejects (§3, 6 of 6). Known grader survivors are recorded as limits and routed, not left as unlearned gate-decision disagreements. No criterion was added without a lesson.

## 5. Axis verdicts (must agree with the MANIFEST entry)

| axis | verdict | evidence |
|---|---|---|
| operability (claim O) | improved | §2 O |
| coverage (claim C) | improved | §2 C |
| depth | unchanged | §2 other axes |
| freshness | unchanged | §2 other axes |
| calibration | unchanged | §2 other axes |
| adjacency | unchanged | §2 other axes |

No axis is harmed. Both claims verify on their kill rules. Admission: true.

## 6. Routed defects for the lane (round 91)

1. **STUB leg.** The counter's STUB leg reports `observed=recorded`, a presence check, so it cannot fail. The frozen `O.after_target` and `O.predicate` sentence about the stub failing SELFTEST is false on the bytes (the stub passes SELFTEST 67/67). Route: a new counter revision that checks the stub receipt's REFUSALS and MUTATION failure lines, plus a correction entry that names the frozen sentence it supersedes. Do not edit the frozen predicate in place.
2. **Grader entry-mode survivors.** Your own report routes these (14 of 21 entry-mode mutants survive; title/chrome quotes; co-fabricated captures; duplicate lands ids; self-quote check). I concur with the routing. The round-91 counter revision should carry the critic's three comparisons plus the surviving sub-checks.
3. **Numeric correction.** The entry has 8 `##` headings, not 10 (report and SCORECARD). Correct with an erratum, not a rewrite of filed bytes.
4. **Citation correction.** `O.before` in `claims.json` cites `reports/round-89/mutation-score.txt` (absent at base). Correct the citation in a correction entry; the real receipt is `.ufo/waves/round-89/w1/MutationCounter.md`.
5. **Lowest-axis clause.** Name the stagnation-nudge test or the operator ruling on L0 `kotodama | round-11` and `kotodama | round-89` in the round report. Until then the lowest-axis obligation is neither met nor waived.
6. **Locator method.** For gate lines whose capture splits the quote across markup (S951), state that the locator is tag-stripped text, or cite the text node.
7. **Stale-lane grade.** State progressing or silent for every open mission, including the round's own.
8. **Quality trend.** Do not claim `quality: improved` from instrument gains. Claim it only when an entry is re-verified, deepened or superseded (freshness is still paused).
9. **Attribution.** The final report bytes landed by sweep commit `882866cd`. Lane identity was on the author line, but the lane did not commit the file. Route: the lane commits its own report at the close of its round.

## 7. SHONEN notes for the operator

No `[x]` is supported by this closure. Box 1 needs a SKILL.md decision table and error patterns; SKILL.md is unchanged this round. Box 2 (end-to-end task) rests on the entry's procedure being exercised on paper; the lesson says so. Box 3 (instructions executable without oral context) is partly supported by the counter commands; I did not run them. Box 4 (no cross-domain bleed) is untested by me. Promotion is operator-owned.
