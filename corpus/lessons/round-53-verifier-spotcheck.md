# Kotodama round 53 — non-author verification

author: hyaku closure (non-author integrator, @m_opus)

Runtime model as exposed to this session: `anthropic/claude-opus-5-5`, reached through the configured `task` route with no model parameter. This closure did not author round 53. It judged only committed bytes: base `6524184e9c55665b84884a25ec240c695cacb64e`, head `2f7331e3661f59323517d17b8abb6d82f5f90355`, plus `9ae5af9` (prerequisite), `a9cf95f` (claim base), `60f1d2a` (declaration), `374ae5a` (D), `47ec825` (C) and `0ef3a4a` (records). Each was exported read-only with `git archive` into `/fast/scratch/hyaku/kotodama-r53-closure/{base,pre,inst,decl,dland,cland,rec,head}`. Five read-only reviewer seats re-opened sources by ordinary means (plain `curl`, Wayback captures, PubMed E-utilities). Every challenge met (Anubis, Cloudflare, Fastly) was left unanswered and routed to an archive copy or ended. No lane gate was executed. The held `kotodama51-prereg-critic` item was not opened, retried or reproduced. Tool installs: none.

## Decision

**Admitted.** Claim D (depth) and claim C (coverage) both re-derive to their declared after-values, and no axis is harmed.

- **D.** All 14 changed lines are supported by the re-opened pages.
- **C.** The 12 falsify section reviews were cancelled unreturned, so this closure sentence-checked the landed text: 105 factual sentences against 47 of the 51 cited rows (all but S188 and S230–S232). 101 were supported, 4 partly supported, 0 not supported, 0 false.
- **Drift sentinel.** It trips on claim sizing, the third round running. C still verifies, because every clause of its statement re-derives with one plain command. The ruling and the routing are below.

## Step-1 conformance

| check | command | observed |
|---|---|---|
| report committed by the lane identity | `git log --format='%an %ae %H' -- .ufo/reports/round-53/kotodama.md` (fleet root) | `kotodama-shokunin kotodama@shokunin.local 4269161aa71860889cebd1ab6e3e8b9c014f0c74` |
| SHONEN heading, one line per box | report `## SHONEN`; `grep -cE '^- \[[ x~]\]'` on the report and on `SHONEN.md` | 4 and 4, all `[~]` |
| cited commits exist and are ancestors of `main` | `git merge-base --is-ancestor <h> main` for `9ae5af9 a9cf95f 60f1d2a 374ae5a 47ec825 e0f9505 e2197ac 0ef3a4a 2f7331e` | all nine are ancestors. `git log 6524184e..2f7331e3` shows exactly these nine, all by `kotodama-shokunin` |
| lane pushed | `scripts/hyaku/jj-lane.sh state <lane>`; `git ls-remote origin refs/heads/main` | `ahead=0 behind=0 tracked=0 untracked=0`; remote `main` = `2f7331e3…` |
| no leftovers | `git status --porcelain` | empty |
| prompt carries the template contract | every non-placeholder line of `templates/round-prompt.md` present in `.ufo/prompts/kotodama-round-53.md` | 105 of 105; directive 3 verbatim and the Claim sizing text present |
| declaration frozen | `git diff --stat 60f1d2a 2f7331e3 -- reports/round-53/claims.json reports/round-53/separability-manifest.json` | empty |
| evidence timestamps | receipt headers against commit times | dry-run `14:00:12Z` = `60f1d2a` at 11:00:12 −03:00 (same second, not after). `final-measures.txt` `15:36:13Z`, before `2f7331e` at 12:36:23 −03:00. `git diff --name-status 0ef3a4a 2f7331e3` → only `A reports/round-53/telemetry/final-measures.txt` |

Driver digest (copied from `.ufo/watchdog.log:704,713`): `2026-10-22T10:52:00-03:00 launch kotodama round=53 pgid=4014948 driver=hyaku-inline attempt=1`; `2026-10-22T12:38:21-03:00 complete kotodama round=53; hyaku-inline attempt=1`.

## Per-claim re-check

Re-measured: the counts, the fragment and phrase greps, both declared commands, and the statement clauses. Evidence-verified only: the separability checker (a lane gate that needs a git checkout). Its receipt in `final-measures.txt` reads `SEPARABILITY: 0 findings`, exit 0, on the export of `0ef3a4a`.

### Claim D — depth, repair-first

Plain measurements on each export of `speech-surrogates-whistled-drummed.md`:

| tree | `grep -oE ', -[0-9]+\b' \| wc -l` | lines matching the six routed phrases | `wc -l` |
|---|---|---|---|
| `6524184` (base) | 11 | 5 (line 54 carries two) | 195 |
| `9ae5af9` (prerequisite; line 104 re-cited to S184) | 10 | 5 | 195 |
| `a9cf95f`, `60f1d2a` | 10 | 5 | 195 |
| `374ae5a`, `2f7331e` | 0 | 0 | 195 |

- The declared counter `python3 -B reports/round-53/d-count.py` gives `OPEN 18` and `SID_BAD 0 [] cited 50`, exit 1, at `a9cf95f`. At head it gives `OPEN 0` and `SID_BAD 0 [] cited 50`, exit 0. Both match the report.
- The cited S-id set is unchanged from `a9cf95f`. Against `6524184` it gains only S184 (the prerequisite). No S-id from S187 up is cited.
- Seat R53CloseDLines re-opened every row behind the 14 changed lines (54, 58, 76, 79, 105, 106, 107, 113, 121, 174, 176, 177, 179, 181). All 14 are supported as newly cited. None rewords the same over-read: each repair narrows the claim, re-scopes it, quotes the source, or marks `(to-verify)`. Examples:
  - line 76 now says "[p] … very similar to [k]" (S147 :240–242);
  - line 113 now reads "about to lose its communication function" (S159);
  - line 121 is scoped to one drummer's biography (S165).
- The fragment replacements checked against the round-52 seat draft-id maps: 8 of 8 match. Line 179's `-12` (S180) was dropped rather than mapped; S180 stays cited on line 181, so no detail lost its support.
- Falsifier: not met.

### Claim C — coverage, the learning claim

- `find corpus/knowledge -name '*.md' | wc -l`: 228 at `6524184`, `a9cf95f` and `60f1d2a`; 229 at `47ec825` and head.
- `python3 -B reports/round-53/accept-c.py`:
  - at `a9cf95f`: all four legs FAIL, exit 1;
  - at head: `COUNT PASS 229`, `ENTRY PASS`, `SWEEP PASS exit=0 rows 229 files 229 missing_from_index 0 []`, `SIDS PASS cited=51 bad=[]`, exit 0.
- Cited S-ids: `grep -oE '\bS[0-9]{3}\b' <entry> | sort -u` gives 51, exactly S187–S238 minus S233. In `SOURCES.md` S187–S238 are 51 `mined` and 1 `rejected` (S233, used-by `—`). Tiers: 30 A and 22 B.
- Registry hygiene:
  - rows 183 → 238 (`grep -cE '^\| S[0-9]{3} '`);
  - no row S001–S183 changed (`diff` of those rows between base and head is empty);
  - S184–S186 unchanged since `9ae5af9`;
  - status totals 194 mined, 35 queued, 9 rejected.

**Ruling on the claim-sizing disclosure (R53-M2), and the drift sentinel.**

1. The defect is real, but narrower than the report says. On scratch copies of head, `accept-c.py` *does* fail the plain mutants, through the README sweep:
   - a second added file plus a removed file → `SWEEP FAIL … missing_from_index 1 ['linguistics/zz-probe.md']`, exit 1;
   - the topic line changed in the entry only → `SWEEP FAIL` (`topic_mismatch 1`), exit 1.
2. It passes only coordinated mutants, which edit the README index row together with the file:
   - a file renamed with its README row renamed → `accept-c` exit 0, `clauses.py` `C1 FAIL`;
   - the topic changed in both the entry and the README row → `accept-c` exit 0, `C2 FAIL`.

   The lane's own controls C-red-4 and C-red-5 ran only `clauses.py`, never `accept-c.py`. So the receipt does not show the gap it describes; this closure's coordinated mutants do.
3. Every clause of C's statement re-derives on head with one plain command:
   - the count (229);
   - `git diff --name-status --no-renames --diff-filter=AD a9cf95f 2f7331e3 -- corpus/knowledge` → one line, `A …/gesture-co-speech-pointing.md`;
   - `grep -c '^- topic: co-speech gesture, pointing and quotable gestures as a conlang and worldbuilding method'` → 1;
   - `accept-c.py` exit 0;
   - the S-id set above.

   The declaration was frozen at `60f1d2a`, not narrowed after landing. So C verifies on what it states.
4. This is the third consecutive round of the class: round-51 D, round-52 C, round-53 C. The round-52 closure set the rule (`round-52-verifier-spotcheck.md:57`), and the drift sentinel trips (`.scratch/goal-20261022-hyaku-12h.md`, Drift sentinels, "same routed defect class in a lane 3 rounds running"). Its prescribed action is routed below. QUALITY criterion 11 (`corpus/QUALITY.md:39`) is the lane's answer. It cites R52-M3 and R53-M2 and has an able-to-fail receipt: `criterion11-controls.txt` shows the round-51 D and round-52 C argv exiting 0 with their clause made false. It binds from round 54.

**Red-before receipt per claim (round-52 note).** Each claim has one:

- **D:** `declaration-dry-run.txt` runs `d-count.py` at `a9cf95f` (`OPEN 18`, exit 1). `final-measures.txt` adds D-red-1 (`FRAG`), D-red-2 (`WROW2`) and D-red-3 (`clauses.py` D1).
- **C:** the same dry-run runs `accept-c.py` at `a9cf95f` (exit 1, all legs FAIL). C-red-1 (`SWEEP FAIL`), C-red-2 (`SIDS FAIL`) and C-red-3 (`ENTRY FAIL`) fail the declared command. C-red-4 and C-red-5 fail only the record script, as noted above.

**Sentence check of C's landed text (substitute for the 12 cancelled section reviews).** Three seats re-opened the cited rows for §§1, 3–9 and 12. This closure re-opened S225 itself.

| span | sentences | supported | partly supported | not supported / false | distinct rows |
|---|---|---|---|---|---|
| §1, §3, §4 (R53CloseSentA) | 25 | 24 | 1 | 0 / 0 | 15 |
| §5, §6, §7 (R53CloseSentB) | 27 | 27 | 0 | 0 / 0 | 15 |
| §8, §9, §12 (R53CloseSentC; S225 re-opened by this closure) | 53 | 50 | 3 | 0 / 0 | 20 |
| **total** | **105** | **101** | **4** | **0 / 0** | 47 (union; S202, S208, S212 checked by two seats) |

Supported at stated strength includes:

- the pointing counts 450 (91%), 104/598 (17%) against 11/496 (2%), and 252/598 (42%) against 0/496 (S200, Table 2);
- the Aymara future-behind result and its sample of thirty speakers aged 38–84 (S208);
- the Yupno uphill future and the doorway-oriented gestures indoors (S209);
- English left vs Hebrew right (S210);
- the Japanese/Turkish two-clause packaging and the straight vs arc gestures (S212);
- the 3.0-month gesture lead (S227);
- the 10–14-month pointing onset across seven sites (S223);
- the Mehrabian scope limit (S235, S236, S237 via a Wayback offprint).

S225's live Benjamins page returned HTTP 403 to a plain request. Wayback `20260106191949` carries "We asked 14 Korean and 14 Catalan participants … curtail gestures when interacting with a socially distant superior", so line 135 is supported.

The four partly supported:

- line 68: S201's page locators (pp. 145/146) are pp. 146/147 in the opened OUP proof;
- line 133: S221 is one deposit (Ewe, Ghana, route description, collector Essegbey, contact Kita). The page does not itself call it "the corpus behind the study";
- line 150: S223 reports *one* culture (Barai) on a missionary's personal communication, not "some communities". The entry already marks the claim `(to-verify)`;
- line 199: the thumbs-up and OK-ring examples are in S234, which that row does not cite. The cited S189 sentence is generic.

C's falsifier asks whether the entry states a claim its cited row's page does not carry. None of the four does in substance: each is a locator, an attribution or a generalisation slip, and every fact is on a page the round opened. They are routed.

## Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| depth | improved | D: OPEN 18 → 0 and SID_BAD 0 → 0, re-measured; 14 of 14 changed lines supported on re-opened pages; S-id set kept |
| coverage | improved | C: 228 → 229; `accept-c` exit 0; the new file is the only `A` line; topic grep 1; 51 of 51 cited rows `mined` with the entry in `used-by`; 105-sentence sample with 0 not supported and 0 false |
| calibration | unchanged | not claimed. SCORECARD's round-53 values match the observed state (rows 238, mined 194, queued 35, rejected 9, tiers A 30 / B 22 for S187–S238, linguistics 28). SHONEN line 6 matches, and line 8 now reads 52 mined / 9 queued, as observed by the round-52 closure |
| operability | unchanged | not claimed; `tools/check-draft-ids.py` is a record tool. Its receipt shows `DRAFT_IDS: 0 findings`; this closure's own sweep finds 0 `NEW-` tokens and 0 citation `, -N` fragments in `corpus/knowledge` |
| freshness | unchanged | not claimed; paused by the open round-11 L0 question |
| adjacency | unchanged | not claimed; the entry defers to adornment-body-codes, sign-languages, numerals, semantics-pragmatics and direction-symbolism by one-way pointers |

`git diff 6524184e 2f7331e3 -- SCORECARD.md`: +16 lines, 0 deleted. It appends the round-53 section and a correction note after the round-51 frontier line, and edits no prior row. It adds no capability row. `corpus/QUALITY.md` gains 2 lines and loses 0.

## Discernment spot-check

| item | gate decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S187 (Haviland 1993, Guugu Yimithirr pointing) — new row, quote checked | admit, tier A, mined | https://pages.ucsd.edu/~jhaviland/Publications/jlin.1993.3.1.3.Anchoring.pdf (curl 200, 43 pp., `pdftotext`) | agree | The Gate and row quote "If one is talking about going to the beach and the beach is east, one points east" (17 words, ≤25) is verbatim. It sits on PDF page 10, which is printed p. 12 of 3–45, as the row's anchor says. The row's teaches cell ("a map drawn in the dust keeps north north") is on the same page. A primary author copy of a peer-reviewed paper fits tier A |
| S184 (UNESCO nomination file 00172, prerequisite) | admit, tier A, mined | https://web.archive.org/web/2018id_/https://ich.unesco.org/doc/src/01610-EN.doc (served 20190622061452id_, 200, `application/msword`) | agree | "an unlimited range of messages over a distance of up to five kilometres", "a network of very deep ravines" and "between the various population clusters posed serious diffi[culties]" are all in the file. Line 104 now cites the source that carries its figure, which fixes round-52 routed defect 1 |
| S204 (Wilkins, Arrernte pointing chapter) | admit, tier B, abstract only | https://www.taylorfrancis.com/chapters/edit/10.4324/9781410607744-12/… (200) | agree | Both Gate quotes are verbatim. The entry's only use (line 72, "(S204, publisher abstract)") stays within the abstract's scope |
| S228 (L2 gesture transfer, AILE 4514) | admit, tier A | live `journals.openedition.org/aile/4514`: Anubis page, not passed; Wayback `20221018012522` (200) | agree | All three Gate quotes are verbatim in the capture. The row records the challenge as met and not passed, and the Wayback route; QUALITY criterion 10 accepts an ordinary copy |
| S233 (Andonova & Taylor 2012 via PubMed) | reject (retired as a duplicate of S219) | https://pubmed.ncbi.nlm.nih.gov/22915258/ (JS shell; abstract via E-utilities efetch, 200) | agree | Same DOI `10.1007/s10339-012-0472-x` as S219. The Gate quote "in Bulgaria, this response pattern is reversed" is verbatim. `grep -rn S233 corpus/knowledge` → 0. Retiring the second row keeps one row per work |
| Bavelas et al. 1992 (drafted, not registered) | reject, tier C lead | https://eric.ed.gov/?id=EJ462208 (200); the publisher DOI page gave 403 | agree | The ERIC record is an abstractor's description (tier C). The entry carries the four interactive roles through S198 "as reported by", so no unregistered source is cited |

The sample agrees with the gate on four admits and two rejects. `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → `kotodama ok`, exit 0. W04 duplicate-URL warnings appear on S127–S133, S185 and S186 only (superseding rows by design).

Gate-quote cap: a mechanical scan of the S187–S238 Gate lines finds no single contiguous quote over 25 words. Seven lines join an anchor or a second fragment to a quote, so the quoted words per line reach 26–36 (S200, S205 ×3, S214, S224, S236; S205 joins two abstract fragments to 36 words).

**Outside-verifier correction (R53-M3).** The round-52 closure wrote that "primitive peoples" is not on S181's page. Seat R53CloseDLines re-opened https://www.dictionary.com/browse/bush-telegraph (200). The Collins block reads "a means of communication between primitive peoples over large areas, as by drum beats". The round-52 closure was wrong, and the lane's R53-M3 is right. The removal of the sub-quote at line 176 is conservative, not harmful.

## Wave shape

- The build wave had 39 seats and the falsify wave 32, 71 in total. `build-sent-payload.json` and `falsify-sent-payload.json` hold 39 and 32 tasks, with no `model` key anywhere.
- `falsify/` holds 6 seat reports. 32 − 6 = 26 = 5 dead at spawn + 21 cancelled, matching the report.
- Dead seats are 5 of 32 (15.6%), under the >20% sentinel. The error text ("No model selected"; the route's primary is deprecated, an operator-owned routing issue) is recorded only in the fleet report, not in the committed wave files.
- The 21 cancellations included all 12 C section reviewers, which is why this closure ran the 105-sentence check above.

## Trend verdicts

- **expansion: improved.** One entry on ground with 0 filename owners and 0 topic-line owners at `a9cf95f`. It cites 51 rows opened this round, all `mined` with the entry in `used-by`, and is indexed at 229. Counter-evidence: four partly supported sentences (routed); one row (S225) now meets a 403 on its live page.
- **quality: improved.** D moved 18 routed defect instances to 0. All 14 changed lines re-open as supported, and none restates an over-read. The landed C text has 0 sentences found false in a 105-sentence outside sample. Counter-evidence: the lane's own frontier list leaves line 75 citing the superseded S145, plus the line-79 "Oaxaca" and single-clause wording.
- **discernment: improved, with the sentinel trip recorded.** The outside sample agrees with the gate on four admits and two rejects. Round 52's claim-sizing disagreement became QUALITY criterion 11, grounded in R52-M3 and R53-M2, with an able-to-fail receipt. The lane caught an outside verifier's error (R53-M3) by re-opening the source. Counter-evidence: the claim-sizing class recurs a third time, and the lane's description of it is wider than its controls show (above).

## Routed defects (lane, next round)

1. **Drift sentinel (claim sizing, 3 rounds running).** Round 54 must work a different frontier area, as the sentinel prescribes. Its declaration must satisfy criterion 11: each statement clause is either checked by a declared command shown able to fail, or listed as review-only. Red controls must run the *declared* acceptance command, not only a record script.
2. **C entry citations.**
   - Line 68: S201 locators should read pp. 146/147, or name the proof pagination.
   - Line 133: soften "the corpus behind the study" for S221, or cite a page that links the deposit to the study.
   - Line 150: "one culture (Barai)", not "some communities".
   - Line 199: cite S234 for the thumbs-up and OK-ring examples.
3. **Gate text.**
   - Split joined fragments into separate quotes, each ≤25 words: S200, S205, S214, S224, S236.
   - S237's Gate URL is the landing page, but its quote is from the offprint (p. 11, readable at Wayback `20261014222628`).
   - S225's live page now returns 403 to a plain request; add an access note at its next re-check.
4. **Speech-surrogates leftovers (the lane's own frontier list).**
   - Line 75 still cites S145, which S185 supersedes.
   - Line 79 "Oaxaca" and "single-clause".
   - Registry cells S135, S141, S147, S151 and S159.
5. **Wave evidence.** Commit the dead-seat error texts with the wave files, not only in the fleet report.
6. **Index.** Add this file to `corpus/lessons/README.md`.

SHONEN: all four boxes are `[~]` with asserted pointers and no named non-author verifier. This closure does not judge them fully checkable. Promotion is operator-owned.
