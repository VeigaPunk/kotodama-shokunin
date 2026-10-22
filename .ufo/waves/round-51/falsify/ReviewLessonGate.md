# ReviewLessonGate: attack on the round-51 lesson

- Seat: KotodamaR51a3.ReviewLessonGate. Leaf, read-only on the lane. No subagents, no background jobs, no swarms.
- Item attacked: `corpus/lessons/round-51.md`. Covers the Gate for S071–S124, the spot-check intake, the status and used-by log, Mistakes rows R51-M1 to M3 (and the working-tree rows R51-M4 and R51-M5), and the Frontier measures.
- Bases. The lesson file as committed at 9feb69e (sha8 fa62e591). Lane HEAD moved during this review to 364eeff, which lands claim D fixes (e6b6629) and claim C fixes (364eeff). That commit adds registry rows S125–S131 and leaves the lesson file byte-identical. The integrator also edited the working tree while I worked (uncommitted: `corpus/lessons/round-51.md` sha8 f4ab1c9d, `corpus/lessons/README.md`, `corpus/QUALITY.md`, `LOG.md`, `SCORECARD.md`, `SHONEN.md`, and `reports/round-51/telemetry/final-measures.txt`). Items tagged **[WT]** concern the uncommitted text. Untagged items hold at both 9feb69e and HEAD 364eeff.
- Access date for every URL I opened: 2026-10-22.
- Installs: none. I used the existing `/usr/bin/pdftotext`, and python3 with `requests` and `bs4`.
- Lane writes: none except this report. No `jj` command was run.

## Verdict: HOLDS-WITH-FIXES

Confidence: high for the mechanical checks (counts, hashes, checker runs, status fields). Medium-high for quotes: 43 rows match verbatim at the cited URL, one of them through a decoded PDF layer. Low for two rows I could not open, S072 and S094 (calibration code T, `calibration-registry.md:39`).

| Part of the lesson | Verdict | Basis |
|---|---|---|
| Gate S071–S124: URL, access date, quote of at most 25 words, location | HOLDS-WITH-FIXES | 54/54 bullets have a URL, a date, a seat and a quote; every quote is at most 25 words. 43 rows verified verbatim at the cited URL; 9 have locator or quote-form defects (F2–F4, F9); 2 unverified (F7). |
| Gate for S125–S131 **[WT]** | HOLDS-WITH-FIXES | Bullets now exist (lines 119–125). S128 has no quote of its own (F1). S125's date is not on its page (F1). |
| Rejected list | HOLDS-WITH-FIXES | 10 + 1 + 2 = 13 Wikipedia rows confirmed. S118 is Kusters 2010, confirmed. S071 breaks the third-party-copy rule (F3). Line 85 is contradicted by R51-M4 and by the entry (F5). |
| Status change log | HOLDS-WITH-FIXES | S001–S070 have no changed row lines. The preamble change is exact, but the quote is incomplete (F12). S071–S122 are mined, opened 2026-10-22 and used-by exactly the entry path. S081 is mined but never cited (F5). S125–S131 are not logged at HEAD (F1). |
| Spot-check intake against round-50 lines 92–98 | HOLDS-WITH-FIXES | The five debts map one-to-one. Dispositions for debts 1, 3 and 4 are incomplete (F11, F13, F14). Search-log arithmetic reconciles: 88 − 15 − 13 − 6 = 54, and tiers are 33 A + 21 B. |
| R51-M1 | HOLDS-WITH-FIXES | The red state is present (answer 1). Its coverage sentence is overstated (F6). |
| R51-M2 | HOLDS | Honest label. Hash and git status re-verified (answer 2). |
| R51-M3 | HOLDS-WITH-FIXES | Counts verified. The evidence id shorthand is wrong (F15). |
| R51-M4, R51-M5 **[WT]** | HOLDS | Evidence files exist. R51-M5's claim matches the manifest (F6). |
| Frontier measures | HOLDS-WITH-FIXES | The to-verify count is 11 on 9 at 9feb69e but 14 on 13 at HEAD (F8). The D counter claim "15/15/15 (controls 10–13)" is overstated (F10). |

**Must fix before admission:** F1 (commit the S125–S131 bullets and give S128 its own quote), F2 (S090 quote), F3 (S071 locator), F4 (S089 URL), F5 (S081 citation and the line-85 claim), F7 (disclose S072 as unverified), and F8 (re-measure the to-verify count at the final commit). Everything else is wording or bookkeeping.

## Direct answers

1. **Does R51-M1's fix really show a red state in `reports/round-51/telemetry/declaration-dry-run.txt`?** Yes.
   - Lines 17–18: the round-51 separability command exits 2 with `SEPARABILITY_INPUT_ERROR unit C lands … absent from the worktree`. That is a not-yet-landed path, which QUALITY criterion 8 allows.
   - Lines 19–21: the historical control on `reports/round-50/claims.json` exits 2 with `manifest is missing base, schema`. That reproduces the round-50 failure exactly.
   - Lines 38–40: the attempt-3 re-run shows the same red line.
   - The lesson quotes the control accurately (line 100).
   - After landing, the same declared separability command exits 0 with `SEPARABILITY: 0 findings`, both at 9feb69e and at HEAD 364eeff.
   - Caveat: line 100 says every round-51 counting and acceptance command was run on its declared input. That is overstated. The two per-claim `acceptance` arrays in `reports/round-51/separability-manifest.json` (`claims[0]`, `claims[1]`) are not in the receipt, which runs their parts separately. The working-tree R51-M5 records this, and I confirmed it (F6).
2. **Is R51-M2 honestly marked as not shown able to fail?** Yes. Line 101 says "Not yet shown able to fail: no red state was captured, so this is a candidate check, not a counted fix." I re-verified the facts it relies on. `sha256sum corpus/lessons/README.md` and `git show main:corpus/lessons/README.md | sha256sum` both give 62f91a93…. `git status` showed only `?? .ufo/waves/round-51/`. The seat's own disclosure (`ScoutReadmeLessonsIndex.md:342–354`) matches: symlink overwrite, four edits reverted, sha back to base. No symlink exists under `corpus/` or `.ufo/waves/round-51/`.
3. **Verdict:** HOLDS-WITH-FIXES, as above.

## Findings

Severity, then pointer, then evidence, then the smallest fix. **[HEAD]** means present at 364eeff. **[WT]** means present only in the working tree.

### High

**F1: rows S125–S131 lack a Gate in the committed lesson [HEAD]; fix in progress [WT].**
- Evidence: the SOURCES preamble (`corpus/SOURCES.md:8`) says the round lesson's Gate holds each row's URL, access date and verbatim quote from S071 on. Commit 364eeff adds seven rows after S124. The committed lesson has no bullet for them and no status-log line (lines 24–26 and 92–94).
- Working tree: seven bullets now exist at lines 119–125. Checked against their pages: S126 verbatim; S127 verbatim, except the page's HTML inserts a space before a comma ("Language , summarizes"); S129 verbatim; S130 ("We thank the commentators for their thoughtful critiques") verbatim; S131 ("Commentary", publisher metadata) verbatim.
- Defects left in the working tree: S128 (line 122) has no quote of its own, only "quote as in S086". Its URL is the S086 URL, but a Gate bullet needs its own verbatim quote with location. S125 (line 119) gives date "2018-07", but the record page shows only "(2018)".
- Smallest fix: commit the bullets, give S128 its own quote, correct S125's date, and log S125–S131 in the status-change line.


### Medium

**F2: S090 quote is not verbatim [HEAD, WT].** Lesson line 47.
- Source (`makaton.org/TMC/TMC/About_Makaton/What_is_Makaton.aspx`, opened 2026-10-22): "Makaton is a **unique** communication programme that uses symbols (pictures), signs (gestures) and speech to enable people to communicate."
- The Gate drops "unique". Working tree: still missing (0 matches).
- Smallest fix: restore the word.

**F3: S071 locator does not show the quote, and a third-party copy is cited [HEAD, WT].** Lesson line 28. Registry `corpus/SOURCES.md:100`.
- The registered archive.org details page does not contain either quote. I checked the full page text (27,515 characters).
- Both quotes are in `https://archive.org/stream/micro_IA41153455_0834/micro_IA41153455_0834_djvu.txt` (HTTP 200, full text, "1 INTRODUCTION Purposes. The primary purpose of this monograph is to bring within the purview of linguistics a virtually unknown language…").
- The same bullet also cites `https://www.joshiesworld.com/wp-content/uploads/2025/10/stokoe_1960.pdf`, a third-party upload not in the registry. Lesson line 87 rejects third-party PDF copies as duplicates, and `corpus/SOURCES.md:200` excludes "a third-party PDF copy". The rule is applied inconsistently.
- Working tree: the djvu stream URL is still absent (0 matches).
- Smallest fix: cite the djvu stream as the locator and drop the third-party copy from the Gate. Register the stream URL with a superseding row, because the contract allows only status, recheck and used-by to change in place.

**F4: S089 Gate URL is not a link [HEAD, WT].** Lesson line 46 contains `https://www.routledge.com/The-Resilience-of-Language-…/9781841694368` with an ellipsis. The registry URL (`corpus/SOURCES.md:118`) is complete, and the quote is present there (checked).
- Smallest fix: paste the full registry URL.

**F5: S081 is "mined" without any citation, and a rejected-list claim is contradicted [HEAD, WT].**
- Lesson line 94 says new mined rows are used by the entry. `corpus/SOURCES.md:110` (S081, Kendon 1988 description) is mined with used-by the entry. The entry never cites S081 (count 0 at 9feb69e and at HEAD). 52 rows are mined and 51 are cited.
- Lesson line 85 says every Wikipedia-carried claim was re-cited to a primary row, including "alternate signing → S081". The working-tree R51-M4 row (line 133) says the S081 re-cite was not carried. Line 85 is therefore false as written.
- Smallest fix: cite S081 where the entry carries the alternate-signing claim, or set S081 to queued and log the change old→new. Correct line 85.

**F6: R51-M1's coverage sentence is overstated [WT wording; present at 9feb69e too].**
- Line 100 says every round-51 counting and acceptance command was run on its declared input. In `reports/round-51/separability-manifest.json`, the `acceptance` arrays of `claims[0]` and `claims[1]` do not appear verbatim in the receipt. The receipt runs their components separately (`boundary-count`, `find … wc -l`, `sweep`, `claims-agree`, separability).
- Smallest fix: qualify line 100 and point to R51-M5, which records this gap.
- I did not replay R51-M5's claim that criterion 9 gives exit 1 at 1f97472 and exit 0 at 9feb69e.

**F7: two Gate rows could not be re-verified in this lane [HEAD for S072; WT notes S094].**
- S072 (line 29): the De Gruyter DOI page returned a human-verification challenge (HTTP 202). `degruyter.com/view/title/36224` (HTTP 200) lacks the quote. Crossref (`api.crossref.org/works/10.1515/9783110261325`) has no abstract. The lesson does not disclose S072 as unverified.
- S094 (line 51): the Gallaudet IDA PDF returned HTTP 403 with a bot challenge to Python and to the reader. The working-tree lesson discloses this in its carried list.
- Smallest fix: mark S072 as seat-opened and not re-verified in this round, or re-open it by another route and record the result.

**F8: the Frontier count is stale at HEAD [HEAD, WT].**
- Line 109 says the C entry carries "11 `(to-verify)` marks on 9 lines".
- At 9feb69e, `python3 -B tools/gates/provenance-audit.py corpus/knowledge/linguistics/sign-languages-manual-modality.md` gives 11 marks on 9 lines (exit 0). I reproduced that.
- At HEAD 364eeff, the same command gives 14 marks on 13 lines (exit 0).
- The header (lines 3–4) lists the D and C landings but not e6b6629 or 364eeff.
- Smallest fix: re-run at the final commit, date the figure, and update the header.

### Low

- **F9: Gate form details (each a one-line fix).**
  - S076 (line 33) and S122 (line 79): the inner quote marks are changed. The source uses double quotes; the Gate uses single quotes. The words hold. Copy the source's marks.
  - S124 (line 81): the location "Abstract and Introduction ¶1" is wrong about the abstract. The quote is not in the Europe PMC abstract; it is in the Introduction. Use "Introduction ¶1".
  - S080 (line 37): the PubMed URL returned HTTP 203 with a cookie page. The quote is verified in the Europe PMC record for PMID 15375269. Cite that record as the locator.
  - S093 (line 50): the annotation "(Wayback capture 20241210011800)" does not match the cited live URL, and the quote is on the live page. Cite the Wayback URL or drop the annotation.
  - S100 (line 57) and S084 (line 41): the same quote appears twice in the bullet. Delete one.
  - S075 (line 32): the Gate's wording matches the PMC page abstract. Europe PMC's abstract for the same DOI reads "Sign was once viewed as nothing more than a system of pictorial gestures without linguistic structure." Name the version used.
  - S119 (line 76): the cited PMC6818964 text is the authors' reply to commentaries ("We thank the commentators…"), not the keynote. The second URL uses DOI 10.1017/S1366728917000724 (Europe PMC PMC6329394, same title, authors and year), which the registry does not list. Say "reply to commentaries" and explain or drop the second DOI.
  - S125 **[WT]**: the date "2018-07" is not on its record page (see F1).
- **F10: "pass at 15/15/15 (controls 10–13)" (line 107) is overstated.** In `.ufo/waves/round-51/build/ExecBoundaryCounterControls.md`, controls 10 and 11 print `rows=11 resolved=11 distinct=11` (rows 49–50). Only controls 12 and 13 print 15/15/15 (rows 51–52). Restate.
- **F11: debt 4 disposition (line 19) says "no checker changed".** Commit 1f97472 added two checker scripts, `reports/round-51/boundary-count.py` and `reports/round-51/claims-agree.py`, plus the separability manifest. No file under `tools/` changed. Say so.
- **F12: the status log's quote of the SOURCES preamble (line 94) drops "and search-log note".** Quote `corpus/SOURCES.md:8` exactly.
- **F13: debt 3 disposition (line 18) omits the round-50 clause** "use consumer behavior, not source-text/wiring assertions" (`corpus/lessons/round-50-verifier-spotcheck.md:96`). Carry it and mark it unmet.
- **F14: debt 1 disposition (line 16) says "(receipt above)".** No receipt appears above. The receipt is `reports/round-51/telemetry/declaration-dry-run.txt`. Its sweep line reads "(tail 3)" (receipt lines 8 and 30), which is not the declared command text, and criterion 8 asks for verbatim. Point to the file and note the annotation.
- **F15: R51-M3 evidence "rows NEW-1…10" (line 102).** The seat's ids are `NEW-ScribeSec02BoundaryC-1` to `-10` (`.ufo/waves/round-51/build/ScribeSec02BoundaryC.md`). Use the real ids.
- **F16: Frontier "Warlpiri widows' signing" (line 109).** At 9feb69e, the entry's Warlpiri to-verify mark sits on "bereaved women" (entry line 139). At HEAD that row was re-scoped (entry line 141). Re-derive the list from the HEAD entry and quote its words.
- **F17: "Admitted: 54 rows" (line 26).** Two of the rows are queued, and the search log says "included". Use "included".
- **F18: rejected-list claim (line 87) that the World Federation of the Deaf "Deafness" page duplicates S078.** Not re-checked here. Say so.
- **F19: falsify paragraph [WT] says "41 attack seats (33 reviewers, 5 critics, 2 mutation testers, 1 scout)".** The folder `.ufo/waves/round-51/falsify/` holds 39 report files: Review 20, Reopen 9, Rerun 2, Critic 5, Mutate 2, Scout 1. Count the files, or say which seats left no file.
- **F20: R50-M6 cross-reference (line 100) checked, no defect.** `corpus/lessons/round-50.md:102` exists and says what R51-M1 says.

## Adjacent observations (for other seats; not scored against the lesson)

- Entry at HEAD line 61 cites "(S086, S109)" for alternate signing. `ReopenS083.md` records S086's problem as its teaches and tier, not its quotes. The C seats should check the citation.
- Entry line 141 cites S075 for Warlpiri signing by women. I checked S075's full text: it mentions Warlpiri twice and "middle-aged" once. No finding.
- Tiers under QUALITY criterion 6: S084 (a masthead slogan, tier A), S090 (a programme's own description, tier A) and S076 (an advocacy FAQ, tier A) read as over-tiered as written. The HEAD superseding rows re-tier S079, S086, S117 and S122 (to S127, S128, S129 and S131).

## What holds (checked)

- Gate: 54/54 bullets have a URL, an access date, a seat and a quote. The longest quotes are 25 words (S079 second quote, S083 first quote, S086 first quote). Seat evidence: 62 of 63 seat–bullet pairs show the URL or its last path segment in the seat's report. The 63rd, S080 with CriticGapPremise, carries the same sentence without the PMID, so it is no defect.
- Status: S071–S122 mined and opened 2026-10-22, used-by exactly `corpus/knowledge/linguistics/sign-languages-manual-modality.md`. S123 and S124 queued. No S001–S070 row line changed between bff83ba and HEAD (only preamble line 8 differs).
- Counts and checkers, at HEAD 364eeff in a private clone: separability exit 0 with 0 findings; claims-agree AGREE; D counter `rows=15 resolved=15 distinct=15`, exit 0; `find corpus/knowledge -name '*.md' | wc -l` = 227; sweep exit 0 with footer total 227 and linguistics 26; provenance audit 14 marks on 13 lines, exit 0.
- Must-not-cite at HEAD: the entry names neither the round lesson nor `boundary-count.py`; the D file names no entry, no S071 or later row, and no lesson.
- Mistakes evidence pointers exist: round-50 Decision and Pins; `reports/round-50/telemetry/final-conformance.json`; `ScribeMistake.md`; `ScoutReadmeLessonsIndex.md` section 5; `corpus/lessons/round-50.md:102`. R51-M4 and R51-M5 evidence files exist in `.ufo/waves/round-51/falsify/`.
- R51-M3 counts: 10 + 1 + 2 Wikipedia rows, confirmed from the distinct URLs in the three seat reports.
- No symlinks under `corpus/` or `.ufo/waves/round-51/`. No `corpus/lessons/operator-*.md` file exists.
- The working-tree lessons index adds a `round-51.md` row (C31, lessons README). This fixes the index gap at HEAD, but it is uncommitted.

## Gate: every URL opened (all accessed 2026-10-22)

"Holds" means the quote is verbatim at the cited URL. Locations were checked only where the page structure was visible. Tier and scope were checked only where a concern is noted.

| Row | URL(s) opened | Result | Verdict |
|---|---|---|---|
| S071 | archive.org/details/micro_IA41153455_0834 (200, metadata only); archive.org/stream/micro_IA41153455_0834/micro_IA41153455_0834_djvu.txt (200, full text); joshiesworld.com/wp-content/uploads/2025/10/stokoe_1960.pdf (200, third-party) | Both quotes in the djvu text and in the third-party PDF; not on the details page | Defect F3 |
| S072 | doi.org/10.1515/9783110261325 (202, human-verification page); degruyterbrill.com same DOI (challenge); degruyter.com/view/title/36224 (200, no quote); api.crossref.org/works/10.1515/9783110261325 (200, no abstract) | Not verified | Unverified (T) |
| S073 | glottolog.org/resource/languoid/id/sign1238 (200) | Heading present | Holds |
| S074 | gupress.gallaudet.edu/Books/T/The-Signed-English-Starter (200) | Present | Holds |
| S075 | pmc.ncbi.nlm.nih.gov/articles/PMC4821822/ (first fetch 331-byte challenge; second 200); Europe PMC record, same DOI | Present in the PMC page abstract; Europe PMC wording differs | Holds; version note F9 |
| S076 | nad.org/knowledge-hub/american-sign-language/community-and-culture-frequently-asked-questions/ (200) | Words present; inner quote marks changed | Defect F9 |
| S077 | un.org/en/observances/sign-languages-day (200 via Python; curl got 403) | 4/4 present | Holds |
| S078 | wfdeaf.org/resources/sign-language-rights/ (200) | Present | Holds |
| S079 | voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement/ (200) | 4/4 present | Holds; tier note (re-tiered by S127 at HEAD) |
| S080 | pubmed.ncbi.nlm.nih.gov/15375269/ (203, cookie page); Europe PMC record for PMID 15375269 (200) | Present in Europe PMC abstract | Defect F9 (locator) |
| S081 | books.google.com/books/about/Sign_Languages_of_Aboriginal_Australia.html?id=Aa34NAEACAAJ (200) | Present | Holds; not cited by entry (F5) |
| S082 | gupress.gallaudet.edu/Books/M/Manual-Communication (200) | Present | Holds |
| S083 | pure.hw.ac.uk/ws/portalfiles/portal/15283839/AT.pdf (200, PDF) | 2/2 present | Holds |
| S084 | www.signwriting.org/ (200) | Masthead quote present (listed twice) | Holds; duplicate F9; tier note |
| S085 | www.nidcd.nih.gov/health/american-sign-language (200) | 2/2 present | Holds |
| S086 | pure.uvt.nl/ws/portalfiles/portal/100130712/Zeshan_deVos_Eds._2012.pdf (200, PDF, 913 KB) | Both quotes present in the Introduction, printed p. 2, after decoding a shifted glyph layer. The text layer drops some letters (y, initial A, ligatures). | Holds with visual-check caveat. ReopenS083 independently found both exact. |
| S087 | linguistics.stonybrook.edu/faculty/mark.aronoff/files/Emerging%20sign%20languages.pdf (Python TLS error; reader 200) | 2/2 present, p. 3 | Holds |
| S088 | pages.ucsd.edu/~cpadden/files/Padden%20SL%20Geography.pdf (Python TLS error; reader 200) | 2/2 present, pp. 8 and 10 | Holds |
| S089 | Gate URL elided with "…" (unusable); registry URL www.routledge.com/…/9781841694368 (200) | Quote present at registry URL | Defect F4 |
| S090 | makaton.org/TMC/TMC/About_Makaton/What_is_Makaton.aspx (200) | Source says "Makaton is a unique communication programme…"; Gate omits "unique" | Defect F2 |
| S091 | www.lotpublications.nl/Documents/151_fulltext.pdf (200, PDF) | Present (section label not checked) | Holds |
| S092 | www.elararchive.org/dk0124 (200) | Present | Holds |
| S093 | www.hup.harvard.edu/books/9780674270411 (200, live page) | Present on the live page | Defect F9 (annotation) |
| S094 | ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls (403, bot challenge; reader 403) | Not verified | Unverified (T) |
| S095 | discovery.ucl.ac.uk/id/eprint/10054130/1/Brentari_Sign%20Language%20Phonology.book.chapter.pdf (200, PDF) | Present | Holds |
| S096 | cslds.org/apsl-consortium/sign-linguistics/6-phonetics-and-phonology-minimal-pairs/ (200) | 2/2 present | Holds |
| S097 | cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition/ (200) | 2/2 present | Holds |
| S098 | cnlse.es/antiguos/Nonmanuals.their%20grammatical%20and%20prosodic%20roles.pdf (200, PDF) | 3/3 present | Holds |
| S099 | pmc.ncbi.nlm.nih.gov/articles/PMC3688355/ (first fetch challenge); Europe PMC full text (200) | Present in §2 full text | Holds |
| S100 | pmc.ncbi.nlm.nih.gov/articles/PMC548320/ (challenge); www.ncbi.nlm.nih.gov/pmc/articles/PMC548320/ (200); Europe PMC abstract (200) | First quote in abstract; second quote complete, including "(in all 32 cases)", on the mirror | Holds; duplicate F9 |
| S101 | www.benjamins.com/catalog/gest.13.3.03pad (200) | Present | Holds |
| S102 | eric.ed.gov/?id=EJ124326 (Python connection reset; reader 200) | Present in the ERIC abstract field | Holds |
| S103 | assets.cambridge.org/97805217/70620/excerpt/9780521770620_excerpt.pdf (200, PDF) | Present (the text layer has the ﬁ ligature) | Holds |
| S104 | glottolog.org/resource/languoid/id/lsfi1234 (200) | Heading present | Holds |
| S105 | glottolog.org/resource/languoid/id/amer1248.json (200) | JSON pair present | Holds |
| S106 | glottolog.org/resource/languoid/id/bsli1234 (200) | Comment present | Holds |
| S107 | glottolog.org/resource/languoid/id/banz1243.json (200) | Newick present | Holds |
| S108 | raw.githubusercontent.com/PerseusDL/canonical-greekLit/master/data/tlg0059/tlg005/tlg0059.tlg005.perseus-grc2.xml (200); www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Crat.:page=422 (200) | Both present | Holds |
| S109 | konferens.ht.lu.se/kendonsymposium2023/abstracts/ (200) | Present | Holds |
| S110 | assets.cambridge.org/97805216/90300/excerpt/9780521690300_excerpt.pdf (200, PDF) | Present | Holds |
| S111 | www.archives.gov/research/guide-fed-records/groups/106.html (200) | Present | Holds |
| S112 | assets.cambridge.org/97805211/23938/excerpt/9780521123938_excerpt.pdf (200, PDF) | 2/2 present (heading matched without case) | Holds |
| S113 | wfdeaf.org/wp-content/uploads/Perspectives-on-the-Concept-and-Definition-of-IS_Mesch-FINAL.pdf (200, PDF) | 2/2 present | Holds |
| S114 | wfdeaf.org/position-paper-on-the-right-of-deaf-people-to-choose-and-access-international-sign-interpretation-services/ (200) | Present | Holds |
| S115 | cslds.org/apsl-consortium/sign-linguistics/4-sign-phonetics-and-phonolgy-stokoes-notation-symbol/ (200) | Present | Holds |
| S116 | www.sign-lang.uni-hamburg.de/dgs-korpus/hamnosys-97.html (200) | Present | Holds |
| S117 | pmc.ncbi.nlm.nih.gov/articles/PMC10622114/ (challenge); Europe PMC record and full text (200) | Present in abstract and full text | Holds |
| S118 | ebi.ac.uk Europe PMC REST, DOI:10.1093/deafed/enp026 (200) | Present in abstract; record author Kusters A., 2010 | Holds |
| S119 | pmc.ncbi.nlm.nih.gov/articles/PMC6818964/ (challenge first); www.ncbi.nlm.nih.gov/pmc/articles/PMC6818964/ (200); Europe PMC DOI:10.1017/S1366728917000724 (200; PMC6329394) | Both quotes present; the text is the authors' reply to commentaries; second DOI not in registry | Defect F9 |
| S120 | www.ethnologue.com/subgroup/2/ (200) | "Subgroup of 161 languages" present | Holds |
| S121 | wfdeaf.org/contact/faqs/ (200) | 2/2 present | Holds |
| S122 | link.springer.com/article/10.1186/1477-7517-9-16 (200 via reader) | Sentence present; Gate writes 'D' where source has "D"; publisher metadata article type "Commentary" | Defect F9; tier note (re-tiered by S131 at HEAD) |
| S123 | web.archive.org/web/20221222142436/https://mitpress.mit.edu/9780262024457/a-prosodic-model-of-sign-language-phonology/ (200) | Present | Holds |
| S124 | pmc.ncbi.nlm.nih.gov/articles/PMC13215104/ (challenge); Europe PMC full text (200) | Present in Introduction, not in abstract | Defect F9 |
| S125 **[WT]** | discovery.ucl.ac.uk/id/eprint/10054130/ (200) | Record fields present; "2018-07" not on page (shows "(2018)") | Defect F1 |
| S126 **[WT]** | glottolog.org/glottolog/glottologinformation (200) | Quote present | Holds |
| S127 **[WT]** | voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement/ (200) | Quote present except a stray space before a comma in the page's HTML | Holds |
| S128 **[WT]** | pure.uvt.nl … (same URL as S086) | Bullet has no quote of its own ("quote as in S086") | Defect F1 |
| S129 **[WT]** | Europe PMC full text of PMC10622114 (200) | Quote present ("In this review, we will provide a brief introduction to fingerspelling…") | Holds |
| S130 **[WT]** | www.ncbi.nlm.nih.gov/pmc/articles/PMC6818964/ (200) | Quote present | Holds |
| S131 **[WT]** | link.springer.com/article/10.1186/1477-7517-9-16 (200) | "Commentary" present in publisher metadata | Holds |

## Commands run (abridged, with exit codes)

| Step | Command or call | Exit or result |
|---|---|---|
| 1 | read `skill://godspeed`; `corpus/lessons/round-51.md`; `reports/round-51/claims.json`; `corpus/lessons/round-50-verifier-spotcheck.md` (1–70, 80–110); the dry-run receipt; `corpus/QUALITY.md`; `calibration-registry.md` 30–45; glob of build seat reports | ok |
| 2 | bash `wc -l`; `git log -n 8`; `ls -la` of lane folders | 0 |
| 3 | read `round-51.md:100-101:raw`; `SOURCES.md` 188–251, 1–25, and `:200:raw` | ok |
| 4 | bash probes: `pdftotext`, `pdfinfo`, `curl` on three URLs (UN 403; PMC 200; Glottolog 200); `sha256sum corpus/lessons/README.md` against `main`; `git status --porcelain` | 0 (both hashes 62f91a93…; status `?? .ufo/waves/round-51/`) |
| 5 | bash `git show --stat` for 1f97472, 35f0d49, da31d3c, 9feb69e; `git diff --stat bff83ba HEAD` | 0 |
| 6 | eval (Python): parse 54 Gate bullets against 54 registry rows; word counts; URL pairing | completed |
| 7 | eval (Python): re-open every Gate URL in memory (PDFs written to `/tmp`); match each quote | completed. Fetch errors: ERIC connection reset; ucsd and stonybrook TLS errors; ida 403 |
| 8 | read: De Gruyter DOI (challenge); Aronoff PDF (ok); Padden PDF (ok); ida.gallaudet (403); ERIC (ok); Springer (ok) | as listed |
| 9 | eval (Python): Europe PMC and PMC mirror triage; Makaton; NAD | completed |
| 10 | eval (Python): S071 pairing; S075 abstract; PDF checks; DOI records; seat-report evidence (63 pairs) | completed |
| 11 | bash: SOURCES base-vs-HEAD diff; row counts | diff rc 1 (only preamble line 8 differs); 0 S001–S070 rows changed |
| 12 | bash: `git clone --shared` at 9feb69e into `/fast/scratch/hyaku/kotodama-r51a3-falsify/`; separability; claims-agree; D counter; C count; sweep; provenance audit | 0 each (separability 0 findings; AGREE; 15/15/15; 227; sweep 227, linguistics 26; provenance 11 marks on 9 lines) |
| 13 | eval (Python): S086 intro; S119 Europe PMC; S072 Crossref; S075 PMC html; S090 | completed |
| 14 | read `PMC6818964` (authors' reply) | ok |
| 15 | bash: seat-report and entry greps (ConnectSiblingSign; controls 10–13; Wikipedia counts 10/1/2; Senghas tier A; operator files) | 0; `ls corpus/lessons/operator-*.md` rc 2 (none exist) |
| 16 | eval (Python): S086 decode (three layers); S100 full sentence; used-by exactness; entry keywords; Kusters author | completed |
| 17 | read `ScoutReadmeLessonsIndex.md:338-352` | ok |
| 18 | eval (Python): S086 letter-only checks; lessons README coverage | completed (no round-51 row at 9feb69e) |
| 19 | bash: lessons README C31 rule; symlink search under `corpus/` and the wave folder | 0; no symlinks |
| 20 | eval (Python): entry S-id citations; hidden line-break characters | completed (S081 not cited; none found) |
| 21 | grep on the entry, tool numbering | ok |
| 22 | bash: HEAD moved to 364eeff; hashes; `git log 9feb69e..HEAD`; SOURCES additions S125–S131; re-clone at HEAD; declared checks; provenance (14 on 13); S081 count 0; must-not-cite greps | 0 each (must-not-cite: no matches) |
| 23 | eval (Python): Warlpiri check on S075 PMC page (Warlpiri 2, widow 0); `/tmp` copies removed | completed |
| 24 | eval (Python): S125–S127 and S129 bullet checks; S127 re-check; S125 date check | completed |
| 25 | bash: working-tree diff of `round-51.md`, `README`, `QUALITY` | 0 |
| 26 | eval (Python): R51-M5 manifest acceptance arrays against the receipt; evidence files for R51-M4 and M5 | completed (all evidence present) |
| 27 | bash: falsify folder counts; ReopenS083 S086 verdict lines | 0 |
| 28 | bash: working-tree status; removed my older clone | 0 |

## Unrun or blocked

- S072 and S094 (see F7).
- Locations for most bullets were not checked beyond the quote. Page or section labels were checked only where visible: S086 p. 2; S087 p. 3; S088 pp. 8 and 10; S100 Results; S119 "Points of agreement" ¶2; S124 Introduction; S122 Background ¶1.
- Seat reports' claims beyond URL presence, and the tier labels inside them.
- Wikipedia tier-B labels in the seat reports.
- The World Federation of the Deaf "Deafness" duplicate claim (F18).
- Tiers and scope of S125–S131 (outside the lesson's Gate scope; quotes checked as listed).
- Falsify verdicts filed by other seats (FAIL or HOLDS). I did not re-adjudicate them. ReopenS083's S086 result agrees with mine on the quotes.
- R51-M5's replay exit codes (1 at 1f97472, 0 at 9feb69e); not replayed.

## Scratch and hygiene

- Temporary PDFs and text copies were written to `/tmp/r51a3-falsify-gate` and removed.
- Private clone kept for reproduction: `/fast/scratch/hyaku/kotodama-r51a3-falsify/ReviewLessonGate-HEAD` (at 364eeff). The earlier clone at 9feb69e was removed after its checks were reproduced at HEAD.
- The integrator's working-tree edits were read, not changed.
