# ReviewSourcesRegistry: falsify attack on the SOURCES registry edit (round 51, attempt 3)

- Seat: KotodamaR51a3.ReviewSourcesRegistry (leaf reviewer, read-only on the lane, no delegation).
- Lane: kotodama-shokunin, branch main. Base bff83ba. Declaration 1f97472. Claim D 35f0d49. Claim C da31d3c. Records 9feb69e.
- Item attacked: `corpus/SOURCES.md` as committed in da31d3c. The worktree matches da31d3c (blob fff4c27a, file sha256 8000acb2...).
- Access and check date: 2026-10-22.
- **Verdict: HOLDS-WITH-FIXES.**

## 1. Verdict in brief

The registry edit meets the registry falsifiers in claim C. The frozen census passes. Rows S001-S070 are byte-identical to 1f97472. Only the four allowed regions changed. Every mined row is cited by the entry and every id the entry cites has the entry path in its used-by cell. Of 85 quote strings checked against re-opened sources, 83 were located. Three of those differ from the Gate only in quote marks or letter case (S076 twice, S122 once).

Three groups of issues block a clean HOLDS:

1. **F5 (high, needs an L1 ruling).** The open route for S094 passed a Cloudflare challenge with a headless browser. I could not re-open S094 without bypassing that gate, so its two quotes are unverified here.
2. **F1 and F2 (medium).** The search-log counts reproduce as row arithmetic, but in drafted-row units. "13 encyclopedia pages" is 13 rows over 11 pages. The note's exclusion count and its "not counted" rule do not follow the seat's own reconciliation.
3. **F3 and F4 (medium).** S117 is tier A on an abstract-only anchor. S122 is tier A for a policy-argument article that the front matter labels "Commentary". Both conflict with QUALITY criterion 6 as written. The census cannot catch either.

Nothing here is a count or identity failure in the registry itself.

## 2. Scope and bounds

Changes in the attacked range (`git diff --stat 1f97472 da31d3c -- corpus/SOURCES.md`: 1 file, 58 insertions, 1 deletion):

| Hunk (old,new) | Content | Lines in da31d3c |
|---|---|---|
| -5,7 +5,7 | Preamble line 8 rewritten (the only deletion) | 8 |
| -97,6 +97,60 | 54 new rows S071-S124 | 100-153 |
| -131,6 +185,7 | One path line, "signed-language design" | 188 |
| -142,6 +197,8 | One search-log note and a blank line | 200-201 |

No other line changed. The Leads section is unchanged.

Writes made by this seat: this report; cached downloads and PNG renders under `/fast/scratch/hyaku/kotodama-r51a3-falsify/downloads-ReviewSourcesRegistry/`; a private clone at `/fast/scratch/hyaku/kotodama-r51a3-falsify/ReviewSourcesRegistry` used only for the mutation control in section 3. The lane was not written to.

## 3. Commands run (cwd, output, exit code)

1. `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` (cwd fleet root; the script is read-only). Output: `kotodama	ok	.../kotodama-shokunin/corpus/SOURCES.md`. Exit 0.
2. Frozen census commands 1-7 (CORPUS.md:133-148), cwd lane root:
   - #1 rows: 124. Exit 0.
   - #2 malformed (NF != 13): 0. Exit 0.
   - #3 tier histogram: A=84 B=33 C=7. Exit 0.
   - #4 status histogram: mined=94 queued=25 rejected=5. Exit 0.
   - #5 duplicate ids: no output. Exit 0.
   - #6 enum and tier-inflation: no output. Exit 0.
   - #7 mined rows with missing used-by paths: no output. Exit 0.
3. `sources-census.sh census --root /home/vgpnk/Projects/shokunin kotodama`: rows 124; tier A 84, B 33, C 7; mined 94, queued 25, rejected 5; missing 0. Exit 0.
4. `sources-census.sh overdue --root ... --today 2026-10-22 kotodama`: 124 cadence lines (symbolic or NNd), zero overdue. Exit 0.
5. `sources-census.sh selftest --root ...`: `selftest ok`; every mutant killed. Exit 0.
6. `git diff --stat 1f97472 da31d3c -- corpus/SOURCES.md`: 58 insertions, 1 deletion. Exit 0.
7. `git diff 1f97472 da31d3c -- corpus/SOURCES.md`: four hunks as in section 2. Exit 0.
8. Row byte identity. `git show 1f97472:corpus/SOURCES.md` and `git show da31d3c:corpus/SOURCES.md`, rows with ids 1-70, piped to sha256sum. Both give `cd39538d97a7f5e196b3c91765bd90a3029266960b9446c300b0aa20c4c3fc61`. Exit 0.
9. Whole-file hashes: 1f97472 `7689f80f...66ff`; da31d3c `8000acb2...fa28c`; worktree `8000acb2...`; `git rev-parse da31d3c:corpus/SOURCES.md` and `git hash-object corpus/SOURCES.md` both give `fff4c27a...`. Exit 0.
10. Used-by against entry. The entry `corpus/knowledge/linguistics/sign-languages-manual-modality.md` cites 52 ids, S071-S122, and none outside that range. All 52 mined rows carry the entry path in used-by. S123 and S124 are uncited, queued, with used-by `-`. Result: 54 of 54 consistent. Exit 0.
11. Naming constraints (claim C must-not-cite). SOURCES.md and the entry contain 0 mentions of `round-51`, `lessons/round-51.md` or `boundary-count`. Exit 0.
12. Credential scan (`op://`, token, session, password, login, cookie, key=) over the 54 new rows. No matches. Exit 1 from grep (no matches).
13. Build-report reproduction (grep, awk and sort over `.ufo/waves/round-51/build/*.md`): row-lines beginning `| NEW-` = 88; distinct NEW ids = 88 (dot-aware regex; the 12 `KotodamaR51a3.`-prefixed ids are included); distinct Wikipedia URLs = 11; Wikipedia row-lines = 13. Exit 0.
14. Failed-route grep over the build reports (lines cited in F1). Exit 0.
15. Mutation control in the private clone. Three rows were inserted after line 153: S125 with tier X; S126 with a missing used-by path; a second S071 (duplicate id). Results:
    - `validate --file <clone>/corpus/SOURCES.md`: `E06 S125 tier=X`, `E03 S071 duplicate id`, `E11 S126 missing used-by .../no-such-file.md`. Exit 1.
    - Frozen #5: S071. Frozen #6: `tier S125 X`. Frozen #7: `missing: .../no-such-file.md`. Frozen #1: 127.
    - The real registry passes validate although S117 and S122 are tier A on the anchors in F3 and F4. The census does not check tier inflation.
16. Wayback probe for the S094 PDF: `curl -L https://web.archive.org/web/2024/https://ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls`. HTTP 404. curl exit 0.
17. Source re-open: 63 route entries covering all 54 S071-S124 ids, fetched with curl at 2026-10-22. Per-route HTTP status is in section 4. PDF text: `pdftotext` (poppler). Page render: `pdftoppm -f 11 -l 12 -r 85 -png` on the S086 PDF, plus page 7 as a table-of-contents check, read visually. Exit 0 on all.
18. Read-only reads of the lane files, the build reports and the claims manifest. No exit codes.

## 4. Search-log counts against the build seat reports

The note at SOURCES.md:200 says: identified 88 drafted source rows; screened 88; included 54; merged 15 duplicate openings; replaced 13 encyclopedia pages; excluded 6.

| Note count | What the build reports give | Reproduces? |
|---|---|---|
| Identified 88 drafted source rows | 88 row-lines beginning `\| NEW-`, each with a distinct NEW id (an earlier 76 figure missed the 12 ids that carry a `KotodamaR51a3.` prefix) | Yes, as a drafted-row count. Not distinct candidates. |
| Screened 88 | The same 88 rows | Only in drafted-row units |
| Included 54 (S071-S122 mined, S123-S124 queued; tier A 33, B 21) | 54 registry rows. Status: mined 52, queued 2. Tier A 33, B 21. | Yes |
| Merged 15 duplicate openings | 69 row-lines map to 54 registry works, leaving 15 extra openings (Sandler 2005 x3 extra; Senghas 2004 x2; Mesch 2010 x2; Stokoe, Glottolog sign1238, Plato, SignWriting, Nicodemus, Meir, UN, Mayberry x1 each) | Yes |
| Replaced 13 encyclopedia pages | 13 Wikipedia row-lines (ScribeSec02BoundaryC-1 to -10; ScribeSec09Alternate-08; ScribeSec12Example-1 and -2) covering 11 distinct pages. Village sign language and Australian Aboriginal sign languages are each drafted twice. | Rows yes; pages no (11) |
| Excluded 6 | Commons film (ScribeSec09Alternate-05); UW finding aid (-07); Internet Archive record (-09); third-party Kusters PDF copy (ReviewTerminologyDeaf-5); WFD "Deafness" page (ReviewTerminologyDeaf-2); WFD Deaf Human Rights page (CriticGapPremise-7) | Yes |
| 54 + 15 + 13 + 6 = 88 | | Yes |

Under the seat's own identity (ScribeSearchLog.md:57: S = A + R + Eo; I = S + Eu; E = Eo + Eu), the same reports give:

- Duplicate openings merged: 18 (15 registry duplicates, 2 duplicate Wikipedia openings, 1 third-party PDF copy of S118).
- Distinct opened works: 70 = 54 registry works + 11 Wikipedia pages + 5 other excluded works.
- A = 54, R = 0, Eo = 16 (11 Wikipedia + 5 other), S = 70. The identity S = A + R + Eo holds at 70 = 54 + 0 + 16.
- Eu (unopened or inaccessible), at least 8, all named in the seat reports and omitted from the note:
  1. ScribeHeadScope.md:90. Cambridge Core "Sign Languages" (Brentari ed. 2010), HTTP 429; MIT Press bookstore, HTTP 403.
  2. ScribeSec09Alternate.md:73. Smithsonian SIRIS object siris_arc_28816, HTTP 403.
  3. ScribeSec09Alternate.md:72. Library of Congress item s2945l01617, HTTP 403; identity checked by search and found to be a different film.
  4. ScribeSec12Example.md:59. OECS MIT entry, HTTP 403.
  5. ScribeSec12Example.md:59. OAPEN library page, HTTP 403.
  6. ScribeSec12Example.md:59. WALS chapter s9, citation block only (metadata-only).
  7. ScribeSec07Iconicity.md:58. Wiley tops.12121, HTTP 403.
  8. ScribeSec12Example.md:59. Wikipedia "Alternate sign language", HTTP 404.
- So I is at least 78 and E is at least 24 in distinct units. The note reports E as 6, counts the 13 Wikipedia rows outside E, and says failed routes are "not counted" (SOURCES.md:200). The seat's reconciliation does not allow that.

## 5. Source re-open, 2026-10-22 (all 54 ids, 63 route entries)

Key: H = quote located at the cited URL. HX = located at a documented alternate route. NR = not re-opened. Tier and scope notes follow the verdict.

| Id | Route(s) opened (accessed 2026-10-22) | What was found | Verdict and tier/scope note |
|---|---|---|---|
| S071 | archive.org details page (200); archive.org djvu text `micro_IA41153455_0834_djvu.txt` (200); joshiesworld.com Stokoe PDF, third-party (200) | Details page lacks the quote. djvu text has "1 INTRODUCTION Purposes. the primary purpose ... bring within the purview of linguistics a virtually unknown language". Joshiesworld PDF has the §1.2 quote. | HX. Locator, F7. A ok. |
| S072 | doi.org (202, empty body); web.archive.org/web/20250309160011 (200) | Publisher description sentence present. | HX, F8. B ok. |
| S073 | glottolog sign1238 (200) | Heading "Pseudo Family: Sign Language". | H. Dataset, A ok. |
| S074 | gupress Signed English Starter (200) | Quote; 940 signs; 14 markers; glossary; exercises. | H. B ok. |
| S075 | pmc PMC4821822 (200) | Abstract quote; sawmill, monastic, mourning, homesign, emblem, fingerspelling present. | H. A ok. |
| S076 | nad.org FAQ (200) | Both quotes present; page uses double quotes, Gate uses single. | H (quote marks only). Docs kind on a membership body, F15. |
| S077 | un.org observance page (200) | Both quotes; "300", "70 million", "80%" present. | H. B ok. |
| S078 | wfdeaf sign-language-rights (200) | Quote; "hundreds"; "unique". | H. B ok. |
| S079 | voices.uchicago.edu research statement (200) | 4 of 4 quotes. | H. A (author's own statement; judgment). |
| S080 | pubmed 15375269 (203, cookie page, no abstract); Europe PMC REST DOI 10.1126/science.1100199 (200) | Abstract quote present; pubType Journal Article. | HX. B (abstract) ok. |
| S081 | books.google about page (200) | Quote; "nine years"; "first book". | H. B ok. |
| S082 | gupress Manual Communication (200) | Quote; Signed English; Signing Exact English; Pidgin Sign; Cued Speech. | H. B ok. |
| S083 | pure.hw.ac.uk PDF (200) | Quote. | H. A ok. |
| S084 | signwriting.org (200) | Banner quote present. | H. A ok. Anchor is a bare homepage, F10. |
| S085 | nidcd.nih.gov (200) | "no universal"; "complete, natural language"; fingerspelling. | H. A ok. |
| S086 | pure.uvt.nl PDF, 18 MB (200) | Text layer garbled in the Introduction. PDF page 11 rendered: both quotes verbatim ("these indigenous sign languages are typically shared between deaf and hearing community members"; "All known village sign languages are endangered"). Printed page 2. | H (visual check). A ok. |
| S087 | stonybrook PDF (200) | 2 of 2 quotes. | H. A ok. |
| S088 | pages.ucsd.edu PDF (200) | 2 of 2; "250,000"; "1817". | H. A ok. |
| S089 | routledge.com (Gate URL abbreviated with "…", HTTP 400); full row URL (200) | Description quote present. | HX, F9. B ok. |
| S090 | makaton.org (200) | Quote present in the page meta description (body is script-rendered). "alternate/manual code ... not a sign language proper" is not on the page. | H (quote). Teaches overstated, F6. |
| S091 | lotpublications PDF, 6.3 MB (200) | Quote; 2%, 10%, 1961, 2001. | H. A ok. |
| S092 | elararchive.org dk0124 (200) | Quote; 48; 1,200; "seven generations". | H. A ok (depositor's summary). |
| S093 | hup.harvard.edu live (504); web.archive.org/web/20241210011800 (200) | Description quote present. | HX. B ok. |
| S094 | ida.gallaudet.edu PDF (403, "Just a moment..." Cloudflare challenge); Wayback 2024 (404) | Not re-opened. Quotes and the "~45 handshape primes / ~25 location primes" figures unverified. | NR. F5. |
| S095 | discovery.ucl.ac.uk chapter PDF (200) | Quote. | H. A ok. |
| S096 | cslds.org Module 6 (200) | 2 of 2. | H. B ok. |
| S097 | cslds.org Module 7 (200) | 2 of 2; "95.9"; "87". | H. B ok. |
| S098 | cnlse.es PDF (200) | 3 of 3. | H. B ok. |
| S099 | pmc PMC3688355 (200) | Quote. | H. A ok. |
| S100 | pmc PMC548320 (200) | 2 of 2 (Abstract); "in all 32 cases"; s-o-v. | H. A ok. |
| S101 | benjamins.com catalog (200) | Abstract quote. | H. B ok. |
| S102 | eric.ed.gov EJ124326 (first attempt: connection reset; retry 200) | Abstract quote. | H. B ok. |
| S103 | cambridge.org excerpt PDF (200) | Quote (PDF ligature ﬁ). | H. A ok. |
| S104 | glottolog lsfi1234 (200) | Heading. | H. Dataset, A ok. |
| S105 | glottolog amer1248.json (200) | Classification array contains {"name": "LSFic", "id": "lsfi1234"}. | H. Dataset, A ok. |
| S106 | glottolog bsli1234 (200) | Quote. | H. A ok. |
| S107 | glottolog banz1243.json (200) | Newick quote. | H. A ok. |
| S108 | raw.githubusercontent Perseus XML (200); perseus.tufts.edu hopper (200) | Greek 422e present; translation quote present. | H. A ok for the Greek wording. |
| S109 | konferens.ht.lu.se (200) | Quote; 1978; 1986. | H. B ok. |
| S110 | cambridge.org excerpt (200) | Quote; contents pages 72, 84, 197, 201. | H. B ok. |
| S111 | archives.gov RG 106 (200) | Quote; "13 reels". | H. A ok. |
| S112 | cambridge.org excerpt (200) | 2 of 2. | H. B ok. |
| S113 | wfdeaf.org Mesch PDF (200) | Both quotes; body: "most of the respondents don't agree international sign is a pidgin or a creole". | H. A tier judgment, F14. |
| S114 | wfdeaf.org position paper (200) | Quote; "unregulated"; "too few qualified interpreters". | H. A ok (WFD policy). |
| S115 | cslds.org Module 4 (200) | Quote. | H. B ok. |
| S116 | sign-lang.uni-hamburg.de (200) | Quote; "version 4". | H. A ok. |
| S117 | pmc PMC10622114 (200) | Quote located only in the Abstract. | H (wording). Tier A on an abstract-only anchor, F3. |
| S118 | Europe PMC REST DOI 10.1093/deafed/enp026 (200) | Abstract quote. | H. B ok. |
| S119 | pmc PMC6818964 (200); Europe PMC REST DOI 10.1017/S1366728917000724 (200) | Quote; "debated"; title. | H. A ok. |
| S120 | ethnologue.com/subgroup/2 (200) | "Subgroup of 161 languages"; 131; 29; Plains Indian and Australian Aboriginal entries sit under the Shared heading. | H. A ok. |
| S121 | wfdeaf.org FAQ (200) | Both quotes; "70 million"; "is sign language universal? no." | H. B ok. |
| S122 | link.springer.com (200, "client challenge" page, not the article); Europe PMC DOI record (200, PMC3384464); Europe PMC full-text XML (200) | Sentence present in the full text as `capital "d"`; the Gate has `capital 'D'`. Front matter heading "Commentary"; JATS article-type "research-article"; Europe PMC pubTypes research-article and Editorial. | HX with letter-case change. Tier A not supported, F4. |
| S123 | web.archive.org/web/20221222142436 (200) | Publisher description quote. | H. B ok. |
| S124 | pmc PMC13215104 (200) | Quote. | H. A ok. |

Totals: 85 quote strings checked (nested quotes split). Located in re-opened text: 83. Not re-opened: 2 (S094). Differing from the Gate only in punctuation or letter case: 3 (S076 x2, S122 x1).

## 6. Findings (severity order; path:line is the exact pointer)

**F5. HIGH (needs an L1 ruling). S094 route passed an access challenge.**
- Evidence: ScribeSec05Phonology.md:70 says the headless browser "passed the challenge and fetched the PDF (553,422 bytes), saved to /tmp/battison1974.pdf". Registry row SOURCES.md:123 cites the same URL as "open issue scan; Cloudflare-gated, opened via headless browser". Gate round-51.md:51. My plain fetch returned HTTP 403, title "Just a moment...". A Wayback probe returned 404.
- Other seats treated the same kind of page as blocked, not passed: ScribeHeadScope.md:89 ("blocked by an anti-bot puzzle - not opened"); ScribeSec01Register.md:13 (live page bot-puzzle blocked; Wayback used instead).
- The context allows no paywall bypass. A bot challenge is an access gate, and this seat's own rule for the same gate was "blocked". The entry cites S094 for Battison's primes and symmetry and dominance wording.
- Minimal fix: L1 rules on the route. If it is not admissible, supersede S094 with a route that does not pass a gate, or remove S094 from the entry and mark its Battison claims `(to-verify)`. If it is admissible, record in the Gate that a bot challenge was passed and why that is not a bypass.

**F1. MEDIUM. Search-log counts are in drafted-row units and do not follow the seat's reconciliation.**
- Evidence: SOURCES.md:200 ("Identified 88 drafted source rows ... Excluded 6 ... failed opens ... not counted"). Seat identity at ScribeSearchLog.md:57 (S = A + R + Eo; I = S + Eu; E = Eo + Eu). Section 4 above gives the distinct-unit figures: 70 distinct opened works; Eo 16; Eu at least 8; E at least 24.
- Minimal fix: restate the note in distinct units with the categories in section 4, or state "drafted rows" and give the distinct identity beside it. Name the Eu candidates in the note. Drop "not counted".

**F2. MEDIUM. "13 encyclopedia pages" is 13 rows over 11 pages. Its basis is misattributed.**
- Evidence: SOURCES.md:200 ("Replaced 13 encyclopedia pages"); the lesson repeats "13 Wikipedia pages" at round-51.md:85. The 13 rows are ScribeSec02BoundaryC-1 to -10, ScribeSec09Alternate-08, ScribeSec12Example-1 and -2. The duplicates are Village sign language and Australian Aboriginal sign languages.
- The note cites "QUALITY criterion 6" for "a tertiary page is never sole support". QUALITY.md:29 (criterion 6) says nothing about encyclopedias. The applicable rule is the tier-C definition at CORPUS.md:96.
- Minimal fix: "11 encyclopedia pages (13 drafted rows)". Cite CORPUS.md:96 instead of criterion 6.

**F3. MEDIUM. S117 is tier A on an abstract-only anchor.**
- Evidence: SOURCES.md:146 (tier A; anchor cell "Abstract"; source cell says "(open-access full text)"). Gate round-51.md:74 quotes the Abstract only. QUALITY.md:29 (criterion 6): "publisher descriptions and abstracts are tier B for substantive claims about a work". The same round tiers S080 B "abstract only" (round-51.md:88).
- The census passes it (validate exit 0). Pre-existing rows show the same pattern (S005, S012, S018, S020, S021, S040, S041, S056, S067). Those predate this round and are noted only.
- Minimal fix: a superseding row with tier B, or a superseding row with a body anchor if the body supports the claim. Do not edit the tier in place (QUALITY.md:29).

**F4. MEDIUM. S122 is tier A for a policy-argument article.**
- Evidence: SOURCES.md:151 (tier A, kind paper, anchor includes "section 'Second, misinforming and coercing behavior counter to the child's welfare'"). Europe PMC full text: title "Reducing the harms of zero tolerance to the use of alternative approaches"; front-matter heading "Commentary"; JATS article-type "research-article" (the two labels conflict); pubTypes research-article and Editorial. The anchored section is education-policy argument, which the claim excludes.
- The Gate at round-51.md:79 renders the source's `capital "d"` as `capital 'D'`. The Springer page returned a client challenge to plain fetch, so the article was read through Europe PMC.
- Minimal fix: a superseding row at tier B without the policy-section anchor, or a written basis for A. Correct the Gate quote to the source's wording.

**F6. LOW-MEDIUM. S090 teaches classify Makaton in a way the page does not.**
- Evidence: SOURCES.md:119 teaches "what Makaton is: an alternate/manual code supplementing speech ... not a sign language proper", attributed to the organisation's own statement. The page (meta description) says "communication programme that uses symbols (pictures), signs (gestures) and speech". Words "alternate", "manual code", "supplement" and "sign language" do not appear in the page's visible text or in its description meta tag.
- Minimal fix: superseding row whose teaches carries only the quoted content. Mark the classification as lane inference.

**F7. LOW. S071 cited URL does not hold its Gate quote; second route not recorded.**
- Evidence: SOURCES.md:100 cites archive.org/details/micro_IA41153455_0834. The Gate quote (round-51.md:28) is not on that page. The djvu text at archive.org/stream/micro_IA41153455_0834/micro_IA41153455_0834_djvu.txt has it. The second Gate route (joshiesworld.com third-party PDF) is not in the row.
- Minimal fix: superseding row citing the full-text URL. Record or drop the third-party copy.

**F8. LOW. S072 route not recorded in the row or Gate.**
- Evidence: SOURCES.md:101 cites doi.org/10.1515/9783110261325. Plain fetch returns HTTP 202 with an empty body. The seat read Wayback capture 20250309160011 (ScribeSec01Register.md:13), which I re-opened (200) and which holds the quote.
- Minimal fix: record the Wayback route in the Gate (or supersede the row).

**F9. LOW. Gate records have a truncated URL and two routes missing from rows.**
- Evidence: round-51.md:46 (S089) gives `routledge.com/The-Resilience-of-Language-…/9781841694368`, which returns HTTP 400. The full URL in the row works. Round-51.md:65 (S108 translation) and round-51.md:76 (S119 Europe PMC search) cite routes not in their rows.
- Minimal fix: correct the Gate lines. These are records, not registry cells.

**F10. LOW. Anchor rules are not met on several rows.**
- Evidence: SOURCES.md:113 (S084 anchor "home page banner/header") is a bare homepage. CORPUS.md:99-100 requires section or page plus revision (version, commit or publication date) and forbids a bare homepage. 21 S071-S124 rows carry no year, version or date marker in source or anchor: S073, S076, S077, S078, S079, S084, S085, S090, S096, S097, S098, S104, S105, S106, S107, S108, S111, S115, S116, S120, S121.
- Minimal fix: add a revision marker through superseding rows, or have the L1 record the reading that web pages without a dated revision are allowed.

**F11. LOW. "Queued as leads" conflicts with the contract.**
- Evidence: SOURCES.md:200 and round-51.md:26 say "S123 and S124 queued as leads". CORPUS.md:83 says a lead is unopened and never a row. CORPUS.md:103-104 defines queued as opened and worth mining. S123 and S124 are opened rows.
- Minimal fix: "queued (opened, not yet cited)".

**F12. LOW. The preamble mapping works by date only.**
- Evidence: SOURCES.md:8 says the S071+ Gate is "the lesson of the round dated in the row's opened cell and search-log note". The note at SOURCES.md:200 names no round. The lesson's verified-at date is 2026-10-22 (round-51.md:4).
- Minimal fix: add "Round 51" to the note heading at SOURCES.md:200. Do not name the lesson file, because claim C's must-not-cite rule forbids it.

**F13. LOW. No rejected rows retained for round 51.**
- Evidence: round-51.md:83-88 keeps the Wikipedia pages and other exclusions as prose ("reasons kept as evidence of taste"). CORPUS.md:104 says a rejected row is "kept". ScribeSearchLog.md:52 requires a retained rejection to read REJECTED with a flip condition. Round 51 adds zero rejected rows; the registry has 5, all earlier.
- Minimal fix: register the substantive rejections as REJECTED rows with flip conditions, or state the exclusion rule for each.

**F14. LOW. S113 tier A for a questionnaire-survey report.**
- Evidence: SOURCES.md:142 (tier A, "docs"). The report says "preliminary survey results", "questionnaire" and "respondents" (Mesch PDF). CORPUS.md:95 lists "survey" under tier B.
- Minimal fix: the L1 states the basis for A (WFD's own report of its survey), or supersede at tier B.

**F15. LOW (judgment). S076 kind and paraphrase.**
- Evidence: SOURCES.md:105 is kind docs, tier A, for a national association's FAQ. "community is never A" (census E10) does not fire because the kind is docs. Teaches "accepted self-identification set" paraphrases "have the right to choose how they wish to be identified".
- Minimal fix: state why the NAD and WFD statements are docs (maintainer statements). Narrow the paraphrase.

**F16. INFO. The census cannot detect tier inflation.**
- Evidence: validate exits 0 with S117 and S122 at tier A (section 3, command 15). E10 covers only kind community at A.
- Action: none required for this edit. Consider a check for abstract-only anchors at tier A.

**F17. INFO. Unverified discrepancy in a merged duplicate.**
- Evidence: ScribeSec12Example.md (row 3) dates the Meir, Sandler, Padden and Aronoff Oxford Handbook chapter 2012. Registry row S087 (SOURCES.md:116) dates it 2010. The merge kept 2010. I did not check the PDF date (my grep for the year returned nothing).

## 7. Checked and holding (no defect found)

- Rows S001-S070: byte-identical to 1f97472 (section 3, commands 8-9).
- The four changed regions are the only changes (section 2).
- Census validate and the seven frozen commands pass (commands 1-2). Census and overdue confirm the counts (commands 3-4).
- S071-S124 ids are contiguous, with no gaps and no duplicates. All opened dates are 2026-10-22. Recheck values are valid. Kinds are within the enum.
- Used-by and entry agree for 54 of 54 rows (command 10). S123 and S124 are not cited.
- Claim C's must-not-cite names do not appear in SOURCES.md or the entry (command 11). The pastoralism entry cites no S071+ id and no round-51 lesson or C entry (D's constraint, checked here only because it is cheap).
- Path line 188: all ids exist and are mined.
- No credential material (command 12).
- Gate: 54 of 54 ids have a seat attribution. Every Gate entry has access date 2026-10-22. Every quote is 25 words or fewer.
- Build-report counts 88, 54, 15, 6 reproduce exactly (section 4). Only "13 pages" fails (F2).

## 8. Residual risk and verification gaps

- S094: not re-opened. Its two quotes and its figures are unverified here (F5).
- S122: Springer page not re-opened (challenge page). Article content taken from Europe PMC full text.
- S080: PubMed page not re-opened (cookie page). Abstract taken from Europe PMC.
- S086: text layer garbled. Verified by visual reading of two quotes. Other S086 claims rest on the same pages but were not checked word by word.
- Teaches numbers were checked for about 20 rows. Non-numeric teaches claims were checked only where listed in section 5.
- Wayback captures are read as archived. They are not current publisher pages.
- The S087 year discrepancy (F17) is not checked.
- Non-author sampling by the L1 is still owed; this seat is an attacking author-lane seat, not admission.

## 9. Unrun checks (other seats or the L1 own these)

- `find corpus/knowledge -name '*.md' | wc -l` (claim C count, expected 227).
- `python3 -B reports/round-28/readme/sweep.py` (claim C sweep).
- `python3 -B reports/round-51/boundary-count.py` (claim D counter).
- `tools/check-claim-separability.py` and `reports/round-51/claims-agree.py`.


## 10. Tooling record

- No installs or updates. Used what was present: curl, pdftotext, pdfinfo and pdftoppm (poppler), python3 standard library, and git (read-only commands on the lane; `git clone --shared` into scratch).
- No pacman, uv, npm or cargo action.
- Scratch paths: `/fast/scratch/hyaku/kotodama-r51a3-falsify/downloads-ReviewSourcesRegistry/` (cached fetches and PNG renders) and `/fast/scratch/hyaku/kotodama-r51a3-falsify/ReviewSourcesRegistry` (private clone; control rows only).
- Lane untouched except this report.
