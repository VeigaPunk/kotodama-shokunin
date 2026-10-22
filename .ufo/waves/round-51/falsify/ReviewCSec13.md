# ReviewCSec13: falsify attack on claim C, entry section 13 (calibration bank)

Author-lane attack. This is a reviewer recommendation, not an admission.

## Item attacked

- Entry: `corpus/knowledge/linguistics/sign-languages-manual-modality.md`, section 13 "Calibration bank", lines 197–215. The table rows sit at lines 203–211; the living-practice flag is at line 213; the precision traps are at line 215.
- Checked against: `corpus/knowledge/verification/calibration-registry.md` lines 30–42; the cited rows of `corpus/SOURCES.md` (S075, S076, S077, S078, S085, S113, S118, S119, S120, S121, S122); `corpus/QUALITY.md` line 29 (criterion 6); `PROVINCE.md` lines 16–20.
- Pinned bytes: entry 223 lines, sha256 `1a71ae2d…b1f7`, identical at HEAD (`9feb69e`) and in the blob at `da31d3c`. `corpus/SOURCES.md` sha256 `8000acb2…1cfa28`, identical at HEAD and at `da31d3c`. Registry sha256 `cf7cceee…0454c`.
- "S-row" below means a numbered row in `corpus/SOURCES.md`.

## Verdict

**HOLDS-WITH-FIXES.** Every quoted phrase and every figure I checked matches its source word for word. Three things do not hold as written: the count row's status and heading (H1), the pantomime row's status (M1), and the critical-period row's anchor and status (M2). Two cells are unsupported by the rows they cite (M3, M4), and one term inverts the entry's own vocabulary (M5). None of the fixes changes the bank's core calls on the universal-language, grammar, and labels rows.

## Findings

### High

**H1. Count row presents a contested count as a bounded fact.** Pointer: entry line 209; SOURCES lines 106, 149, 150.
- The heading "More than 300 sign languages exist" is a bare count filed under status B. Registry line 37 (B) requires population, period and counter. Registry line 36 (C) says not to report one reading as settled.
- The three cited counts measure different things and disagree: "more than 300" (S077, UN page); "200+ national sign languages" (S121, WFD FAQ); "161" (S120, Ethnologue).
- The UN page places the 300 figure in a paragraph that opens "According to the World Federation of the Deaf". The WFD pages I opened give no 300 figure: S078 says "hundreds", S121 says "200+".
- The row's own rule, "never a bare number" (line 209, last cell), contradicts its heading.
- SOURCES line 106 says "(estimate)". The UN page does not say that.
- **Smallest fix:** file the row as C. Retitle it "The count depends on what is counted." Give three cells, each with its counter and access date (2026-10-22), and say the UN figure sits in a WFD-attributed paragraph. Correct the S077 teaching cell with a superseding row, because SOURCES lines 9–12 make the teaching cell append-only.

### Medium

**M1. Pantomime row treats a live position as rejected.** Pointer: entry line 204; SOURCES line 104.
- R (rejected, registry line 35) is applied to "Sign is pantomime or gesture". The S075 abstract, opened 2026-10-22, says the field is "swinging back toward the view that sign is gestural, or at least has gestural components". It also says it is "difficult to tell where sign stops and where gesture begins".
- R fits pure pantomime. The S075 Introduction ¶2 says "Initially, sign was considered nothing more than pantomime or a language of gestures". The gestural-components point is contested, so it needs C.
- The word "discredited" appears in the S075 teaching cell (SOURCES line 104), not in the paper. Registry line 30 says "contested" and "discredited inference" are not synonyms. Registry line 41 allows several codes for parts of one theory.
- **Smallest fix:** split the row. "Sign is only pantomime": R, citing S075 Introduction ¶2. "Sign has gestural components": C, citing the S075 abstract. Correct the S075 teaching cell with a superseding row.

**M2. Critical-period row: wrong anchor for the decades claim, and an unflagged existence dispute.** Pointer: entry line 208; SOURCES line 148.
- (a) "even after decades of signing" is cited to "Points of agreement, paragraph 2". That paragraph does not contain the phrase. The phrase rests on two reported case studies. One is M (25 years of British Sign Language). The other is Martin (30 years of ASL). Both appear in the "Language measurement and cognitive factors" section. Registry line 37 forbids extrapolation by resemblance, and two cases do not support a population clause.
- (b) S119 reports a dispute over whether a critical period exists at all: "Opinions range all the way from the conclusion that there is no critical period at all (Bialystok & Kroll, 2018)". The authors also say Bialystok and Kroll read the late-learner cases as evidence against a critical period. The row gives the heading B and only "fixed cutoffs" C.
- (c) The "roughly age 12–20" range in SOURCES line 148 comes from L2 studies, not first-language studies.
- (d) The row gives no year (2018).
- **Smallest fix:** rewrite as "In two reported case studies, late first-language learners with decades of signing showed limited morphological and syntactic ability (S119)." Split the heading into "later first-language exposure lowers ultimate attainment" (B, S119 paragraphs 1–2) and "a discrete critical period closes at a fixed age" (C, S119 "Opinions range").

**M3. Village row: unsupported stigma cell; anchor and status do not match the abstract.** Pointer: entry line 207; SOURCES line 147.
- (a) "attitudes, access and stigma vary by village" is not in the S118 abstract. The abstract says nothing about stigma, attitudes or access.
- (b) The row's anchor, "abstract, sentence 1", supports only the perception that Martha's Vineyard was "a utopia in the eyes of many Deaf people". The critique is in the later sentences. The literature "critically reviews" the field, and its typologies are "based on 'traditional' Western urban Deaf communities".
- (c) C rests on a single abstract. Registry line 36 asks that alternatives and discriminating evidence be preserved. The row names neither.
- (d) "stigma is a variable" is a designer heuristic (H, registry line 38). It sits in the same cell as reference evidence. Registry line 31 asks that the three record types be kept apart.
- **Smallest fix:** rewrite the C cell to what the abstract supports. The utopia reading is held by many Deaf people. The literature on such communities uses typologies built on urban Deaf communities and is under critical review. Move "stigma varies" to an H line, or mark it "(to-verify)".

**M4. Precision traps: two phrases cited to rows that do not contain them.** Pointer: entry line 215.
- "sign is not gesture" and "not iconically transparent" are cited to S077, S078 and S121. None of the three opened pages contains "gesture", "pantomime" or "iconic". The S075 abstract says the boundary is hard to draw, so a flat "not gesture" overstates it. The same flat wording appears outside section 13 at line 160 ("Sign is not gesture-code"); that line is not my item and is flagged for its owner.
- **Smallest fix:** replace "not gesture" with "distinct in kind; the boundary is contested (S075 abstract)". For iconicity, cite the section 7 rows S101–S103 (not re-opened by me) or drop the phrase.

**M5. Terminology: "signed code" used for a sign language.** Pointer: entry line 203 ("no single signed code is universal") and line 206 ("describe the signed code's morphology and syntax").
- In this entry, "code" means a designed code of a spoken language. See line 26 ("a manual code of a spoken language: a designed code"), line 157 ("deliberately designed visual codes for a spoken language"), and line 21 (codes that graft onto speech fail the test). Lines 203 and 206 use "signed code" for a sign language, which inverts the entry's own vocabulary.
- **Smallest fix:** replace "signed code" with "sign language" in both cells.

### Low

**L1. S113: survey tier and period.** Pointer: entry line 203; SOURCES lines 142 and 17. The WFD survey ran in spring 2007 with 24 of 35 respondents, interpreters included. It was published in May 2010. The row is tier A, but the header lists "survey" under B (SOURCES line 17). Section 13 gives no period. **Fix:** add "2007 survey, 24 respondents"; settle the tier with a superseding row or a scope note.

**L2. S122: tier for a commentary.** Pointer: entry line 211; SOURCES line 151. Springer metadata give the article type as "Commentary" and dc.type as "Letter". The paper is advocacy on cochlear implants and language policy. The capital-D sentence holds, but a commentary is not an "original paper" under the tier A wording (SOURCES lines 15–16). **Fix:** superseding row at tier B. The status B in section 13 stays.

**L3. S076: community source at tier A; missing instruction.** Pointer: entry line 210; SOURCES lines 105 and 19. SOURCES line 19 says "community is never A". The row is tier A for a community organisation's guidance. The cell omits the NAD's last instruction, "When in doubt, ask the individual how they identify themselves", and the accepted self-identifiers (Hard of Hearing, Late-Deafened, DeafBlind, DeafDisabled). **Fix:** add the instruction and the list; decide the tier with a superseding row.

**L4. Living-practice flag: attribution.** Pointer: entry line 213. "The UN calls early access … vital" should name the resolution. The UN page says resolution A/RES/72/161 "acknowledges" that early access is "vital". The UN page also gives "more than 70 million deaf people worldwide", which is a different population statement from the WFD FAQ's "belong to signing deaf communities". Section 13 uses the WFD wording correctly, so keep it. **Fix:** "The UN resolution A/RES/72/161, as the UN page summarises it, acknowledges…"

**L5. Pidgin attribution.** Pointer: entry line 203. The UN page says International Sign "is considered a pidgin form". The entry says "the UN page calls it a pidgin". **Fix:** quote "considered a pidgin form".

**L6. S121 teaching cell overreads.** Pointer: SOURCES line 150. The FAQ says there is "no official count of the number of deaf people in the world". The S-row says "no official global count", which reads as a sign-language count. **Fix:** superseding row.

**L7. Ethnologue: unsupported gloss.** Pointer: entry line 209; SOURCES line 149. The page states no counting rule, so "under its own rule" is an unsupported gloss. The 161 is 131 plus 29 plus 1 (International Sign, listed at top level). **Fix:** drop "under its own rule"; write "161, including International Sign".

**L8. Missing periods.** Pointer: entry lines 203–211. Section 13 gives no years for Kusters 2010 (S118), Mayberry and Kluender 2018 (S119), Humphries et al. 2012 (S122), or the 2007 survey (S113). The counts carry no access date. Registry line 37 lists period as required. **Fix:** add the years and access dates.

**L9. Letter overload.** Pointer: entry line 145 ("rows rest on opened sources (**B**)") and line 207 ("C … (S118)", where S118 is tier B). Calibration codes and source tiers share the letters B and C. **Fix:** write "tier B" where the source tier is meant.

**L10. S119 teaching cell.** Pointer: SOURCES line 148. "Shape and cutoffs debated (roughly age 12–20)": the ages come from L2 studies. **Fix:** superseding row note.

## Verified to hold

- Line 206 quote, "Each sign language has its own structure, grammar, and lexicon, equaling spoken languages in every respect": verbatim at S078 (wfdeaf.org/resources/sign-language-rights/).
- Line 210: "These terms are not acceptable", preferred "deaf" or "deaf people", and "hearing-impaired should not be used": verbatim at S121 (wfdeaf.org/contact/faqs/). S076 calls deaf-mute and "deaf and dumb" offensive, and says "hearing-impaired" is "no longer accepted by most in the community".
- Line 203: "There is no universal sign language." Verbatim at S085 (nidcd.nih.gov).
- Line 203: "most of the respondents don't agree International Sign is a pidgin or a Creole." Verified at S113 section 5 (p. 7).
- Line 209 figures: "Subgroup of 161 languages" (S120); "200+ national sign languages" and "only 40%" legally recognised (S121); "more than 70 million deaf people belong to signing deaf communities" (S121).
- Line 211: S122 Background ¶1, "it is common convention to use a capital 'D' when talking about communities that use a sign language as their major language". S078: "Deaf cultural behaviours and values".
- Line 213: "inseparable" (S078); "preserving sign languages as part of linguistic and cultural diversity" (S077).
- Line 199: the code list (R, C, B, H, T) matches registry lines 35–39.
- All 11 S-ids cited in section 13 exist in SOURCES (lines 104–151) and list the entry path in `used-by`. The C falsifier about used-by cells passes for section 13.
- No cell in section 13 names `corpus/lessons/round-51.md` or `reports/round-51/boundary-count.py` (grep: no match).
- No canon decision, clinical ruling, education-policy ruling or rights ruling appears in section 13. Rights positions are attributed to the UN and WFD. PROVINCE lines 16–20 are respected.
- The registry has no sign-language or critical-period row that conflicts with section 13 (grep: no match). A narrow grep for "critical period", "more than 300 sign", "161 sign" and "Ethnologue lists" over all of `corpus/knowledge` matched only section 13 rows 208–209. The broad pass also reached `language-shift-obsolescence-revival.md:10` and `:92`, which mention Ethnologue as EGIDS wording and are marked "(to-verify)"; neither is a count or critical-period claim.

## Sources opened (all accessed 2026-10-22)

| S-row | URL | What the anchor says | Quote | Tier | Scope |
|---|---|---|---|---|---|
| S076 | https://nad.org/knowledge-hub/american-sign-language/community-and-culture-frequently-asked-questions/ | Q&A on deaf-mute, "deaf and dumb", hearing-impaired; accepted self-identifiers; "ask the individual" | Holds | A stated; see L3 | Holds for term preference |
| S077 | https://www.un.org/en/observances/sign-languages-day | "According to the World Federation of the Deaf… Collectively, they use more than 300 different sign languages." No "(estimate)". "Considered a pidgin form". Resolution A/RES/72/161 "acknowledges" early access is "vital". | 300 holds as WFD-attributed. "(estimate)" does not hold. | B | Holds |
| S078 | https://wfdeaf.org/resources/sign-language-rights/ | Introduction: "Each sign language has its own structure, grammar, and lexicon, equaling spoken languages in every respect"; "hundreds of unique and independent sign languages"; "Language and culture are inseparable" | Holds, verbatim | B | Holds |
| S085 | https://www.nidcd.nih.gov/health/american-sign-language | "There is no universal sign language." | Holds, verbatim | A (official) | Holds |
| S113 | https://wfdeaf.org/wp-content/uploads/Perspectives-on-the-Concept-and-Definition-of-IS_Mesch-FINAL.pdf | Spring 2007 survey, 24 of 35 respondents, published May 2010; section 5: "Most of the respondents don't agree…" | Holds | A stated; see L1 | Holds with period |
| S118 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/deafed/enp026&resultType=core&format=json | Abstract: "a utopia in the eyes of many Deaf people"; typologies from urban Deaf communities; "critically reviews the existing literature". No stigma, attitudes or access. | Partial; see M3 | B (abstract) | Partial |
| S119 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6818964/ | Paragraph 1: "steady decline in ultimate attainment". Paragraph 2: "declines sharply the longer the child matures without language". Case studies M and Martin. "Opinions range… no critical period at all." | Partial; see M2 | A | Partial |
| S120 | https://www.ethnologue.com/subgroup/2/ | "Subgroup of 161 languages"; "Deaf community sign language 131"; "Shared sign language 29"; International Sign at top level | 161 holds; "under its own rule" does not | A (own count) | Holds |
| S121 | https://wfdeaf.org/contact/faqs/ | "200+ national sign languages… only 40%"; "These terms are not acceptable"; "more than 70 million deaf people belong to signing deaf communities"; "no official count of the number of deaf people" | Holds, verbatim | B | Holds |
| S122 | https://link.springer.com/article/10.1186/1477-7517-9-16 (redirected to a `?error=cookies_not_supported&code=…` URL; page content returned) | Background ¶1, capital-D convention; "Over forty years of research…". Article type "Commentary". | Capital-D holds | A stated; see L2 | Capitalisation only |
| S075 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4821822/ | Abstract: "pendulum is currently swinging back… sign is gestural, or at least has gestural components"; "difficult to tell where sign stops and where gesture begins". Introduction ¶2: "Initially, sign was considered nothing more than pantomime". | Pantomime-stage claim holds. "Discredited" does not appear. | A | Partial; see M1 |

## Commands run

| # | Command or call | Output | Exit |
|---|---|---|---|
| 1 | `git rev-parse --short HEAD`, then `git show da31d3c:<entry> \| sha256sum`, `sha256sum <entry>`, `wc -l <entry>`, `git show da31d3c:corpus/SOURCES.md \| sha256sum`, `sha256sum corpus/SOURCES.md` | `9feb69e`; `1a71ae2d…b1f7` (blob and working tree); `223`; `8000acb2…1cfa28` (blob and working tree) | Output returned with no error text. Exit status not shown by the tool; rerun below. |
| 2 | `git show HEAD:<entry> \| sha256sum`; `git show HEAD:corpus/SOURCES.md \| sha256sum`; `realpath -m .ufo/waves/round-51/falsify`; `ls -la` on that directory | `1a71ae2d…b1f7`; `8000acb2…1cfa28`; path inside the lane; directory listing (other seats' files present) | `exit=0` on each step |
| 3 | `sha256sum` on entry, SOURCES and registry; `realpath -m` on this report | `1a71ae2d…b1f7`, `8000acb2…1cfa28`, `cf7cceee…0454c`; report path inside the lane | `exit=0` on both |
| 4 | Grep: registry for sign-language, critical-period, Deaf, Ethnologue | No matches | Tool call, no exit code |
| 5 | Grep: `corpus/knowledge` for critical period, sign-language counts, Ethnologue, "more than 300" | Broad pass (output cut by the tool): `language-shift-obsolescence-revival.md:10` and `:92` (Ethnologue as EGIDS wording, "to-verify") and section 13. Narrow pass for "critical period", "more than 300 sign", "161 sign", "Ethnologue lists": section 13 rows 208–209 only. | Tool call, no exit code |
| 6 | Grep: entry for "signed code", "stigma", "iconically transparent", "not gesture", "decades", "discredited", "pantomime", "round-51", "lesson", "boundary-count", "reports/round", "estimate" | Matched lines: 3, 4, 7, 9, 10, 26, 60, 83, 112, 160, 184, 203, 204, 206, 207, 208, 209, 215. No `round-51` path and no `boundary-count` hit; "reports/round" matched only `reports/round-28` (sweep path). | Tool call, no exit code |
| 7 | Grep: SOURCES for the count and critical-period terms | Matched lines include the cited S-rows (104–107, 142–153) and unrelated rows that contain "161", "200+" or "pantomime". | Tool call, no exit code |
| 8 | Reads: entry lines 1–223; registry lines 29–42; SOURCES lines 1–21 and rows 104–153 and 200; QUALITY; PROVINCE; RULES | As quoted above | Tool calls |

No install or update was run. No `jj` command was run.

## Unrun checks

- `find corpus/knowledge -name '*.md' | wc -l` (must print 227): not my item; unrun by me.
- `python3 -B reports/round-28/readme/sweep.py` (must exit 0 with footer total 227 and linguistics 26): unrun by me.
- `python3 -B reports/round-51/boundary-count.py` (D's counter): unrun by me.
- `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json`: unrun by me.

## Residual risk and verification gaps

- S075: I read the abstract, Introduction ¶1–2 and sections 1–3 in part. Sections 4.3, 5 and 7.2, which the row's anchor list cites, were not read by me.
- S101–S103 (section 7 sources, relied on in M4's fix) were not re-opened.
- S119 was read from the PMC author manuscript (NIHMS1055346), not the publisher PDF. Paragraph numbers may differ in the publisher version.
- S113 was read from a PDF-to-text conversion. Page numbers come from that text.
- S122: I read Background only. The "Second, misinforming…" section, which the row's anchor list also cites, was not read. It is out of section 13's scope.
- The UN, WFD and Ethnologue pages are live. Counts are as of 2026-10-22.
- The round lesson's Gate quotes were not checked. That is outside this item.
- Registry codes were checked against the registry text only.

## Tooling

No tool was installed or updated. Git was used read-only (`rev-parse`, `show`). Hashes and line counts were computed with `sha256sum` and `wc`. This report is the only file written in the lane.
