# CriticCCalibration — round 51 attempt 3, falsify wave

- Item attacked: claim C, the calibration of `corpus/knowledge/linguistics/sign-languages-manual-modality.md` (landed in `da31d3c`). Author-lane attack, not admission.
- Axis judged: calibration (QUALITY criteria 1, 2 and 6; registry codes `calibration-registry.md:35-39`).
- Seat: leaf, read-only on the lane. The only lane write is this report. Downloads went to the private scratch directory `/fast/scratch/hyaku/kotodama-r51a3-falsify/CriticCCalibration/src` (realpath checked). No clone was needed because no experiment wrote anything.
- Installs: none.

## Verdict

**HOLDS-WITH-FIXES.** Six of the eight headline figures I was asked to test hold at their cited source, two of them only with a scope fix. One fails as cited: the village-sign-language cell "dozens to about 130 deaf signers … 3–6 generations (S087)". S087 contains no generation range. The source that does have a time-depth table (S086, Table 1) contradicts the range at both ends, and also contradicts the 130 ceiling. Separately, §4 carries six unmarked lever cells and §6, §7 each carry one unmarked general claim. None of these findings hits claim C's declared falsifier (count, sweep, missing S-id or used-by, restating another owner's register), so every finding can be fixed in place.

## Headline figures: re-opened and checked

| Figure (entry line) | Cited | What the source says | Holds? |
|---|---|---|---|
| ASL about 250,000 primary signers (`:58`) | S088 | Padden PDF p. 12: "The number of primary users of ASL, those who use it as a first and dominant language, is roughly estimated at around 250,000 signers." S087 p. 9 agrees ("about a quarter of a million people"). | **Holds for ASL.** But the cell uses it as the *ceiling* of the deaf-community type ("thousands to about 250,000"). Padden calls ASL "one of the largest sign languages in the world", not the largest, so the ceiling has no source (finding F4). |
| ASL "since 1817" (`:58`) | S088 | Padden p. 11 says the Hartford school opened in 1817 and asks "How did the different village sign languages in existence in 1817 coalesce together with home sign systems … to create a common sign language? How did LSF enter into this mix?" S087 p. 6 says sign languages "dating from before the arrival of LSF in Hartford must have played a role in the emergence of ASL". | **Holds with a fix.** 1817 is when the school was founded, which is where ASL's convergence starts. It is not a date when ASL already existed (F5). |
| NSL since 1977 (`:60`) | S087 | Meir et al. p. 7: "The first deaf school in Nicaragua was opened in Managua in 1977"; p. 9: NSL is "dating from the founding of the Managua deaf school in 1977". | **Holds.** |
| "about 25 years" (`:126`) | S080 | PubMed abstract (via E-utilities): "A new sign language has been created by deaf Nicaraguans over the past 25 years". The paper was published 2004-09-17. | **Holds with a fix.** The figure is relative to 2004, and the entry drops that anchor, so a reader takes 25 years as a closed formation span (F6). |
| "3–6 generations" (`:59`) | S087 | Not in S087. S087 gives ABSL as "about 75 years old … currently in its third generation", Ban Khor and Providence Island as "at least three generations", Adamorobe as "about two hundred years old", and Kata Kolok as 63–134 years versus 500 (contested). S086 (Introduction, Table 1, p. 4) gives Chican "Three generations", Mardin "Four", Kata Kolok "Five generations of deaf native signers", Alipur "At least 6 generations", ABSL "90 years" and Adamorobe "200 years". S092 (ELAR) says the recessive gene "emerged in the village at least seven generations ago". | **Fails as cited** (F1). |
| "~45 handshape primes" (`:87`) | S094 | **S094 could not be opened.** curl got HTTP 403, and headless Chromium got the Cloudflare page titled "Just a moment...". The round lesson's Gate quote for S094 (`corpus/lessons/round-51.md:51`) is the Dominance Condition sentence and does not contain the number. S097 (CSLDS Module 7) does: "Out of the 45 possible handshapes in ASL, only 7 can appear as the passive hand of a Type-3 two-handed sign", attributed to Battison 1978 p. 207. | **Holds through S097** (Battison 1978). I could not verify it in S094 (Battison 1974) (F9). |
| "14 sign markers" (`:156`) | S074 | Gallaudet University Press Description: "a systematic progression in the use of the 14 sign markers; discussion of the unique features of a manual English system". | **The number holds word for word.** The same cell's other claims are not on the page (F2). |
| WFD "more than 70 million" (`:213`) | S121 | WFD FAQ: "The WFD estimates more than 70 million deaf people belong to signing deaf communities." | **Holds word for word.** Note that the UN page (S077) restates WFD's figure as "more than 70 million deaf people worldwide", which is a different denominator. The entry correctly follows WFD's own wording. |

## Findings

| # | Severity | Pointer | Finding | Smallest fix |
|---|---|---|---|---|
| F1 | **high** | `sign-languages-manual-modality.md:59` | **False provenance and a miscalibrated range.** "dozens to about 130 deaf signers … 3–6 generations (S087)": S087 has no generation range. The build seat grounded it on a p. 15 sentence about complexity accruing over time (`.ufo/waves/round-51/build/ScribeSec03Typology.md:20,55`). The S086 Table 1 values (three, four, five and at least six generations; 90 and 200 years) and S092's "at least seven generations" put the upper end above 6, and two of those are lower bounds. The same table lists Alipur with **150** deaf signers, which breaks the "about 130" ceiling (130 is S087's 2010 "largest … so far"). Yolngu with 5, Chican with 17 and Ban Khor with 24 (S086 Table 1), and Urubu-Kaapor with 5 (S087 p. 9), break the "dozens" floor. The entry's own §4 (`:74`, Bengkala ≥7 generations, S092) contradicts §3. | `a handful to about 150 deaf signers plus many hearing signers; three to at least six generations, or 90–200 years (S086 Table 1); Kata Kolok's gene at least seven generations (S092)` |
| F2 | medium | `:156`; `:26` | **The S074 page does not carry the word-order claims.** "arranges a borrowed sign vocabulary in English word order" and "not ASL-English bilingual education (S074)" are not on the page. Its Description says only "940 basic signs", "14 sign markers" and "a manual English system", and the Gate quote (`round-51.md:31`) is only "unique features of a manual English system". `:26` "a designed code that keeps the spoken word order (S074)" has the same gap. S082's page does not say it either. | Keep `(14 sign markers) (S074)`. Rewrite the rest as `a manual English system (S074)`, and either mark "English word order" `(to-verify)` or source it from an opened row that states it. |
| F3 | medium | `:76`, `:77` | **S091 is used outside its declared scope.** The row's scope is "the Adamorobe case … not other sign-language claims". "most Deaf children learn their sign language only after entering school; ~5% are born to Deaf parents (S091)" is Nyst's general remark about "large Deaf communities" (PDF p. 1141 region: "only an estimated 5% of Deaf children are born to Deaf parents"), and she gives no source for it there. The same paragraph is a counterexample to the lever: Nyst notes that Deaf communities "arose outside of an educational context" in Mali and among Hausa signers. | Mark the 5% figure `(to-verify)` or move it to a row whose scope is general Deaf demography; add "some Deaf communities form outside schools (Mali, Hausa)". |
| F4 | medium | `:58` | **ASL used as the type's ceiling.** "thousands to about 250,000 primary signers": the source calls ASL "one of the largest", so 250,000 is not a sourced maximum for deaf-community sign languages. | `thousands (LSQ 5–6,000) to ASL's roughly 250,000 primary users, one of the largest (S088)` |
| F5 | low | `:58` | "ASL since 1817" reads as a birth date. Both cited sources describe convergence starting at the 1817 Hartford school from earlier village sign languages, home sign and LSF. | `(ASL traced to the 1817 Hartford school, S088)` |
| F6 | low | `:126` | "over about 25 years" drops the abstract's "over the past 25 years" (2004) time anchor. | `over the 25 years before 2004 (S080)` |
| F7 | medium | `:112` | **Extrapolation with no marker.** "a young sign language reads more iconic than an old one" generalizes Frishberg's ASL-only historical tendency (S102, a tier-B abstract) to every sign language. Registry code B says "no extrapolation by resemblance" (`calibration-registry.md:37`). | Append `(design heuristic, **H**)` or limit it to `ASL's history suggests` |
| F8 | medium | `:99` | **Unanchored overclaim.** "a surface with no spoken analogue": spoken languages also mark clause type in parallel with the words, through intonation. The entry's own S098 frames nonmanuals as "grammatical and prosodic". | Cut the clause, or say `wider simultaneous layering than spoken intonation (S098)` |
| F9 | low | `:87`, `:92` | "~45 handshape primes (S094)" could not be re-opened at S094 (Cloudflare). The Gate quote does not carry the number, and S097 does (from Battison 1978). In `:92`, "(A, B, 5, G, C, O) (S097, S094)" lists six shapes, but the co-cited S097 lists seven: "A, S, B, 5, G (i.e., 1), C and O". | Cite `(S097; S094)` for 45; give the list as S097's seven, or attribute the six to S094 alone. |
| F10 | low | `:152` | "one-handed (ASL, LIS, ISL)": S083 p. 3 names only ASL and LIS as one-handed. ISL appears only as a studied language. | Drop ISL or mark it `(to-verify)` |
| F11 | low | `:140` | "a 1930 council was filmed to record it (S111)": the NARA RG 106 entry is "Development of an intertribal sign language dictionary … ca. 1930-31 (13 reels)" and names no council. The council is in S110's contents ("The Indian Sign Language Council, 1930"; Appendix 3 "films of the 1930 Indian Sign Language Council"). | `(S110; film holding S111)` |
| F12 | low | `:64` | "universal among speakers (S079)": the Goldin-Meadow research statement speaks of "the spontaneous gestures that hearing adults and children produce as they speak". It makes no universality claim. | `common among speakers (S079)` |
| F13 | low | `:13`, `:14`, `:20` | Support is weaker than the wording. "does not derive from any spoken language (S071; S072)": S071's quote is the monograph's purpose, and S072 is a tier-B publisher description of method; neither states non-derivation. "Stokoe's 1960 analysis first brought": "first" is a priority claim beyond S071's quote. "emergent village/shared sign systems (S071; S073)": S071 (1960) does not treat village sign languages. | Cite S078 or S085 for independence; drop "first"; cite S086 or S087 for village systems. |

### Unanchored factual claims (no S-id, no in-corpus anchor, no `(to-verify)`, no **H**)

§3, §9 and §11 carry a blanket "uncited = **H** or `(to-verify)`" statement (`:55`, `:145`, `:164`). §4, §5, §6 and §10 do not, so their uncited cells are unmarked.

| Line | Claim |
|---|---|
| `:17` | "manual and non-manual articulators (hands, face, gaze, body) carry the linguistic load; the channel sets the craft constraints, not the grammar's depth" |
| `:70` | "A signing community forms where deafness is concentrated and interaction is daily: a village with hereditary deafness, a residential school, or a Deaf family" (counterexample: F3) |
| `:74` | "village signing emerges at high rates; mobility dilutes them" |
| `:75` | "a bilingual village, not a separate Deaf world" |
| `:76` | "a school generation can shift the language (AdaSL → GSL)" (support exists in S091's row but is not cited in the cell) |
| `:77` | "a founder-family effect powers the founding myth, not the main channel" |
| `:78` | "the hearing majority's ideology sets status and schooling choices" |
| `:79` | "pressure points: school generation, prestige sign, demographics" |
| `:87`–`:90` | the "(design rule)" failure cells include factual statements ("contrasts blur and signers cannot discriminate reliable forms"; "movement classes must be finite and constrained"). "(design rule)" is not a registry code. |
| `:99` | "a surface with no spoken analogue" (F8) |
| `:112` | "a young sign language reads more iconic than an old one" (F7) |
| `:142` | the Occupational row's "workers in the trade" and "supplements or overrides speech in the noisy channel". Only the trigger cell cites S075, despite `:145` saying rows rest on opened sources or are `(to-verify)`. |
| `:157` | "a literate deaf community writes SignWriting; analysts transcribe with HamNoSys" (design consequence in §10, which has no blanket **H**) |
| `:206` | "attitudes, access and stigma vary by village" (S086's introduction supports "deaf villages are far from homogeneous", but the cell does not cite it) |
| `:215` | "not iconically transparent", closed by (S077, S078, S121), none of which covers iconicity (S103 does) |

Smallest fix for the table: add the sentence `Lever cells are design heuristics (**H**, calibration-registry.md:38).` under the §4 and §10 tables, and use **H** instead of "(design rule)" in §5. Cite or mark the individual factual cells listed above.

## Other figures re-checked in passing (hold)

- Adamorobe ">10% in 1961, ~2% by 2001" (`:74`, S091): Nyst says "estimated to occur in more than 10% of the population at that time" and "from 10% in 1961 to 2% in 2001". Holds.
- Adamorobe's former chief barred deaf-deaf marriage (`:77`, S091): Nyst says "Former chief Nana Kwaakwa Asiampong II prohibited marriage between two deaf persons". Holds.
- Bengkala "~1,200 hearing signers" and "≥7 generations" (`:74`–`:75`, S092): ELAR says "approximately 1,200 hearing signers" and "at least seven generations ago". Holds.
- "four major regions, eight distinctions each" (`:88`, S095): Brentari et al. say "four major body regions … each region has eight place distinctions". Holds.
- ABSL "all 32 two-noun clauses" (`:108`, S100): PMC548320 says "subject precedes object (in all 32 cases)". Holds.
- Alternate signing during "mourning, hunting" (`:61`, S086): Introduction p. 3, decoded: "alternate sign languages are used in situations of speech taboos for instance during mourning or during hunting". Holds.
- "even after decades of signing" (`:207`, S119): Mayberry and Kluender cite cases with 25 and 30 years of experience. Holds.
- "more than 300" (`:208`, S077): UN page says "Collectively, they use more than 300 different sign languages". Holds. "161" (S120): Ethnologue says "Subgroup of 161 languages … Deaf community sign language 131 … Shared sign language 29". Holds. "200+ … 40%" (S121): holds word for word.
- BANZSL "argued on lexical and historical evidence" (`:128`, S106): Glottolog cites "Lexicostatistical evidence … (as also supported by historical evidence …)". Holds.

## Sources opened (all accessed 2026-10-22)

| Row | URL | Result | Quote / tier / scope |
|---|---|---|---|
| S088 | https://pages.ucsd.edu/~cpadden/files/Padden%20SL%20Geography.pdf | 200, PDF | Quote holds (pp. 11–12). Tier A for the author's own claims is fine. Scope holds for ASL, not as a type ceiling. |
| S087 | https://linguistics.stonybrook.edu/faculty/mark.aronoff/files/Emerging%20sign%20languages.pdf | 200, PDF | Holds for 1977 and 130 (as of 2010). No generation range anywhere in the text. |
| S086 | https://pure.uvt.nl/ws/portalfiles/portal/100130712/Zeshan_deVos_Eds._2012.pdf | 200, PDF; the Introduction is font-shifted (+29) and I decoded it locally | Table 1 p. 4 and p. 3 alternate-signing sentence read as given above. Tier A for the introduction's scope holds. |
| S080 | https://pubmed.ncbi.nlm.nih.gov/15375269/ | HTTP 203, page text "Cookies must be enabled". I read the same abstract via https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=15375269&rettype=abstract&retmode=text (200) | Quote holds; tier B (abstract) is correct. |
| S094 | https://ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls | **Failed**: curl got HTTP 403; headless Chromium got the Cloudflare page with title "Just a moment..."; Wayback availability returned `"archived_snapshots": {}` | Not verified. |
| S097 | http://www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition/ | 200 | "Out of the 45 possible handshapes in ASL"; seven passive shapes; 95.9% / 87%. Tier B (secondary) is correct. |
| S096 | http://www.cslds.org/apsl-consortium/sign-linguistics/6-phonetics-and-phonology-minimal-pairs/ | 200 | No 45 figure. |
| S074 | https://gupress.gallaudet.edu/Books/T/The-Signed-English-Starter | 200 | "14 sign markers" holds; no word-order or ASL statement. Tier B (publisher description) is correct. |
| S082 | https://gupress.gallaudet.edu/Books/M/Manual-Communication | 200 | Lists systems including ASL; no word-order statement. |
| S121 | https://wfdeaf.org/contact/faqs/ | 200 | 70 million, 200+ and 40% hold word for word. |
| S077 | https://www.un.org/en/observances/sign-languages-day | First try 502; retry 200 | "more than 300", "pidgin" and the 70-million wording (for "deaf people worldwide") hold. |
| S091 | https://www.lotpublications.nl/Documents/151_fulltext.pdf | 200, PDF | Adamorobe figures hold; the 5% figure is outside the row's scope (F3). |
| S092 | https://www.elararchive.org/dk0124 | 200 | 48 deaf signers, about 1,200 hearing signers, ≥7 generations. |
| S100 | https://pmc.ncbi.nlm.nih.gov/articles/PMC548320/ | 200 | 32 cases; hearing members sign. |
| S095 | https://discovery.ucl.ac.uk/id/eprint/10054130/1/Brentari_Sign%20Language%20Phonology.book.chapter.pdf | 200, PDF | Regions × places holds. |
| S083 | https://pure.hw.ac.uk/ws/portalfiles/portal/15283839/AT.pdf | 200, PDF | One-handed: ASL and LIS only; initialization "(usually circular)". |
| S119 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6818964/ | 200 | 25 and 30 years of experience cases. |
| S079 | https://voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement/ | 200 | No universality claim. |
| S111 | https://www.archives.gov/research/guide-fed-records/groups/106.html | 200 | The film-project entry names no council. |
| S110 | https://assets.cambridge.org/97805216/90300/excerpt/9780521690300_excerpt.pdf | 200, PDF | Contents list "The Indian Sign Language Council, 1930". |
| S112 | https://assets.cambridge.org/97805211/23938/excerpt/9780521123938_excerpt.pdf | 200, PDF | Checked only in passing. |
| S106 | https://glottolog.org/resource/languoid/id/bsli1234 | 200 | Lexicostatistical and historical evidence. |
| S120 | https://www.ethnologue.com/subgroup/2/ | 200 | 161 / 131 / 29. |
| S102 | https://eric.ed.gov/?id=EJ124326 | 200 | ASL-only tendency toward arbitrariness. |
| S071 | https://archive.org/details/micro_IA41153455_0834 | 200 (landing page only, full text not read) | Not re-verified beyond the landing page. |
| S075, S076 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4821822/ ; https://nad.org/knowledge-hub/american-sign-language/community-and-culture-frequently-asked-questions/ | 200 each | Fetched; not used for any finding. |

## Commands (all run with the working directory in scratch unless stated; every one exited 0)

1. `mkdir -p …/CriticCCalibration/src && realpath … && which pdftotext curl python3 chromium` returned `/fast/scratch/hyaku/kotodama-r51a3-falsify/CriticCCalibration/src`, `/usr/bin/pdftotext`, `/usr/bin/curl`, `/usr/bin/python3` and `/usr/bin/chromium` (exit 0).
2. Parallel `curl -sSL -A <Chrome UA>` of 16 source URLs: battison 403, un 502, senghas 203 (cookie wall), all others 200 (exit 0).
3. `pdftotext -layout` on padden, meir, nyst, brentari, nicodemus and zeshan: line counts 1451, 1134, 9422, 1539, 1700 and 15716 (exit 0; nyst printed font warnings).
4. `grep` passes over the extracted texts for 250,000, 1817, generation, 1977, 130, 45, %, region, one-handed, decades and council; the outputs are quoted in the tables above (exit 0).
5. `curl 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=15375269&rettype=abstract&retmode=text'` returned 200 with the abstract text quoted above (exit 0). The cookie-jar retry of PubMed returned 203 again.
6. `curl 'https://archive.org/wayback/available?url=ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004%26context=sls'` returned `"archived_snapshots": {}`; `web.archive.org/web/2024id_/…` returned 404 (exit 0).
7. `chromium --headless=new --dump-dom <S094 URL>` returned `<title>Just a moment...</title>` (Cloudflare challenge) (exit 0).
8. A Python decode (character + 29) of S086 Introduction lines 234–375 recovered Table 1, quoted above (exit 0).
9. In the lane, read-only: `realpath …/.ufo/waves/round-51/falsify` then `ls`; `CriticCCalibration.md` was absent before this write (exit 0).

## Checks not run

- S094 at its stated location (blocked by Cloudflare). I did not try to get around the challenge.
- S071 full text (ERIC/archive.org), and S089, S090, S093, S098, S099, S101, S103–S105, S107–S109, S113–S118, S122 at their stated locations. These were not among this seat's targets.
- The claim C counters (`find … | wc -l`, `sweep.py`). Those belong to RerunCCount.
