# ReopenS089: falsify attack on SOURCES rows S089–S094

Seat: `KotodamaR51a3.ReopenS089` (leaf reviewer, read-only on the lane). Every access date is 2026-10-22. Lane: `kotodama-shokunin`, branch `main`, HEAD `9feb69e` (read-only inspection). This file is the only lane write. Downloads went to scratch, `/fast/scratch/hyaku/kotodama-r51a3-falsify/ReopenS089`.

## Item attacked

SOURCES rows S089–S094 (`corpus/SOURCES.md:118–123`), their Gate bullets (`corpus/lessons/round-51.md:46–51`) and their `used-by` cells. For each row I checked: the Gate quote is verbatim at the stated location and at most 25 words; kind; tier under QUALITY criterion 6; scope; anchor; `used-by`.

## Verdict: HOLDS-WITH-FIXES

- Five rows were re-observed at the stated location, with quotes verbatim: S089, S090, S091, S092, S093.
- S094 was not re-observed. Its URL returns HTTP 403 with a Cloudflare managed challenge, and no archived copy exists. I did not try to pass the challenge. S094 therefore cannot be HOLDS from this seat. Its quote, counts and minimal-pair list are unverified, and its dominance shape list conflicts with S097.
- No high-severity finding. Medium: F1, F2, F3, F4, F11. Low: F5–F10, F12.

## Per-row results

| Row (SOURCES line) | Where the quote was checked | Verbatim | Words | Tier and scope | Row verdict |
|---|---|---|---|---|---|
| S089 (118) | Routledge page, "Description" paragraph (live, HTTP 200) | yes | 22 | B, publisher description: holds | HOLDS (F7: lesson URL elided) |
| S090 (119) | `<meta name="Description">`, makaton.html:19 (also `og:description`, :20) | yes in meta; the body `<p>` at :1018 reads "a unique communication programme" | 18 | A as the maintainer's statement; narrow scope holds; the gloss goes beyond the page | HOLDS-WITH-FIXES (F5) |
| S091 (120) | nyst2007.pdf physical p. 29; §1.4 opens there and matches the TOC's printed p. 29 | yes (line break after "Akan and") | 24 | A for Nyst's own work holds; A for reported studies does not (F3); §1.6 in the anchor is outside the stated scope (F4) | HOLDS-WITH-FIXES (F3, F4, F12) |
| S092 (121) | "Summary of the collection" (live, HTTP 200) | yes | 19 | A for the depositor's own counts holds; judgement note (F8) | HOLDS (F8 note) |
| S093 (122) | Wayback capture 20241210011800, description paragraph 2 | yes | 13 | B, publisher description: holds | HOLDS-WITH-FIXES (F6: ¶ number and edition) |
| S094 (123) | not re-observed (HTTP 403, Cloudflare challenge) | not verified | 22 | A: not checkable here | UNVERIFIED, blocked (F1, F2, F9–F11) |

Structural checks (all pass):
- One registry row per id: six matches, lines 118–123.
- All six rows are `mined`, and each `used-by` cell names `corpus/knowledge/linguistics/sign-languages-manual-modality.md`.
- The entry cites every id: S089 at line 62; S090 at 63; S091 at 74, 75, 76, 77, 79; S092 at 74, 75, 79; S093 at 74, 75; S094 at 83, 87, 90, 92, 93.
- Gate URLs equal the row URLs except S089 (F7). All Gate dates are 2026-10-22.

## URLs opened (access 2026-10-22)

1. Routledge, S089: https://www.routledge.com/The-Resilience-of-Language-What-Gesture-Creation-in-Deaf-Children-Can-Tell-Us-About-How-All-Children-Learn-Language/Goldin-Meadow/p/book/9781841694368. Live, HTTP 200. The "## Description" paragraph holds the quote. Page says "Copyright 2003", "1st Edition", "Psychology Press".
2. Makaton, S090: https://makaton.org/TMC/TMC/About_Makaton/What_is_Makaton.aspx. Live, HTTP 200. The reader showed only the skip link. Raw HTML (scratch copy) has the quote in the meta description and `og:description`. The body `<p>` reads "Makaton is a unique communication programme…".
3. Nyst, S091: https://www.lotpublications.nl/Documents/151_fulltext.pdf. Live, HTTP 200, application/pdf, 245 pages. Text layer extracted with pdftotext. The quote is on physical p. 29.
4. ELAR, S092: https://www.elararchive.org/dk0124. Live, HTTP 200. "Summary of the collection", "Group represented" and "Language information" are present. Quote verbatim.
5. HUP, S093 live: https://www.hup.harvard.edu/books/9780674270411. HTTP 202 with an AWS WAF challenge script and no product text. Not usable; the row already says so.
6. HUP, S093 capture: https://web.archive.org/web/20241210011800/https://www.hup.harvard.edu/books/9780674270411. HTTP 200, 297,892 bytes (scratch). Quote verbatim in description paragraph 2.
7. Battison, S094: https://ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls. HTTP 403. curl shows `cf-mitigated: challenge`. Reader: "Failed to fetch URL (HTTP 403)". Not passed.
8. Wayback for S094: https://web.archive.org/web/2024/https://ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls. HTTP 404 (reader and curl). The archive.org availability API for the same URL returned `archived_snapshots: {}`.
9. IDA issue landing page: https://ida.gallaudet.edu/sls/5/. HTTP 200. Record "Sign Language Studies, Vol. 05, 1974". Contents item 1 is "Phonological Deletion in American Sign Language", and Robbin Battison is listed among the authors. Repository date 1975. Confirms the article exists; no article text.
10. JSTOR: https://www.jstor.org/stable/26203099. HTTP 200, but the body is "Client Challenge" text. No article content.
11. Scilit: https://www.scilit.com/publications/4b7cf335cf61dbd039375d48e774d512. HTTP 403.
12. web_search for Battison 1974: search snippets only, not opened. Snippets gave DOI 10.1353/sls.1974.0005 and JSTOR, Scilit, DeepDyve and academia.edu listings.

## Commands and exit codes

| # | Command | Exit | Key result |
|---|---|---|---|
| 1 | read: RULES.md; claims.json; QUALITY.md; round-51.md; SOURCES.md rows, preamble and lines 118–126 raw; round-51.md 44–52 raw | ok | Rows and Gate bullets read |
| 2 | git log -8; git status --porcelain; ls -la .ufo/waves/round-51; realpath of falsify (read-only, in lane) | 0 | HEAD 9feb69e; only untracked `.ufo/waves/round-51/` |
| 3 | command -v for pdftotext, pdfinfo, curl, wget, python3; import checks for pypdf, pdfminer, fitz; mkdir scratch | 0 (imports failed, expected) | /usr/bin tools present |
| 4 | curl Nyst PDF to scratch; pdfinfo; pdftotext -layout | 0; 0; 0 | 245 pages; poppler font warnings only, text produced |
| 5 | curl Makaton HTML to scratch | 0 | 118,197 bytes |
| 6 | curl -D - Gallaudet viewcontent | 0 (HTTP 403) | `cf-mitigated: challenge` |
| 7 | curl archive.org wayback/available for the Gallaudet URL | 0 | `archived_snapshots: {}` |
| 8 | curl HUP Wayback capture to scratch; pdftotext -v; curl -V; pdfinfo -v | 0 | 297,892 bytes; poppler 26.08.0; curl 8.23.0 |
| 9 | grep of Nyst text for S091 claims | ok | hits on pp. 21, 24, 25, 27, 28, 29, 32 |
| 10 | grep of Makaton HTML | ok | lines 19–21 and 1018 |
| 11 | eval (py): page map, word counts, flexible quote match, §1.6 and family context | ok | quote on p. 29 (1 hit); words 22, 18, 24, 19, 13, 22 |
| 12 | eval (py): HUP markup and paragraph map | ok | description = 11th and 12th of 35 `<p>` blocks |
| 13 | eval (py): curl -sSL status for 11 URLs | 0 each | status codes in the URL list above |
| 14 | grep: S089–S094 row ids at line start in SOURCES.md | ok | six matches, lines 118–123 |
| 15 | grep: C entry for round-51 lesson path or boundary-count | ok | no matches |
| 16 | grep: build folder for the Battison access route | ok | ScribeSec05Phonology.md lines 21, 54, 63, 70 |
| 17 | web_search (Battison 1974) | ok | snippets only |

Unrun (outside this item, listed as unrun): `python3 -B reports/round-51/boundary-count.py`; `find corpus/knowledge -name '*.md' | wc -l`; `python3 -B reports/round-28/readme/sweep.py`; `python3 -B tools/gates/provenance-audit.py corpus/knowledge/linguistics/sign-languages-manual-modality.md`; `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json`. Inside this item, the Battison primary text (quote, counts, minimal pairs, dominance list, anchor pp. 3–5) is unrun because it is blocked.

## Findings

**F1 (medium). S094 not re-observed (access).** `corpus/SOURCES.md:123`; entry `sign-languages-manual-modality.md:83, 87, 90, 92, 93`. Evidence: URLs 7–11. Smallest fix: the integrator re-opens S094 from an accessible copy and records the Gate quote, the ~45 and ~25 counts, the minimal pairs and the dominance list at the anchor. Until then, mark entry lines 87 (~45 primes), 92 (shape list) and 93 (minimal pairs) `(to-verify)` per QUALITY criterion 1.

**F2 (medium). Dominance shape list conflicts with S097.** S097 teaches (`SOURCES.md:126`) and its Gate (`corpus/lessons/round-51.md:54`) give "A, S, B, 5, G/1, C, O": seven shapes, including S. S094 teaches (`SOURCES.md:123`) say "the six unmarked passive shapes A B 5 G C O". Entry line 92 writes "(A, B, 5, G, C, O) (S097, S094)", so the entry contradicts S097, the row it cites. Smallest fix: change entry line 92 to the seven-shape set S097 supports, and mark it `(to-verify against S094)` until F1 closes. Any change to S094's teaches needs a superseding row, because the preamble makes the registry append-only (`SOURCES.md:9–12`).

**F3 (medium). S091 tier A covers reported studies.** `SOURCES.md:120` gives tier A for "the Adamorobe case as documented by Nyst's own 2001 fieldwork and the studies she reports". The 1961 figure (>10%) is Drummond's survey as reported in David et al. (1971) (`nyst2007.pdf` p. 21; Table 1.1 source note). The 1995 count is Amedofu et al. (1999) (Table 1.1). Criterion 6 reserves A for sources primary or authoritative for the exact scope, so a reported figure is B. Entry line 74 uses S091 for "Adamorobe >10% in 1961". Smallest fix: a superseding row narrows S091's scope to Nyst's own work (2001 count, fieldwork, AdaSL description; tier A). Reported figures become B, or David et al. (1971) gets its own queued row.

**F4 (medium). S091 used beyond its stated scope; population drift.** S091's scope says "not other sign-language claims" (`SOURCES.md:120`), yet its anchor includes §1.6, "Structural similarity in signed languages" (`nyst2007.pdf` pp. 31–35), which is cross-linguistic. Entry line 76 cites S091 for "most Deaf children learn their sign language only after entering school; ~5% are born to Deaf parents". The source (p. 32) says: "Only a small proportion of the members of large Deaf communities are native signers, as only an estimated 5% of Deaf children are born to Deaf parents. As a result, most adult members of the large Deaf communities acquired sign language only after entering school." So the entry (a) uses a general claim the row excludes, and (b) changes "adult members" to "children". Smallest fix: rewrite entry line 76 to the source's population ("in large Deaf communities, most adult signers learned their sign language after entering school; about 5% of Deaf children have Deaf parents (S091 §1.6, Nyst reporting the literature)"). Drop §1.6 from S091's anchor by superseding row, or cite the original source for the figure once it is opened.

**F5 (low). S090 anchor and scope.** `SOURCES.md:119` says "page body renders via script". The raw HTML shows the body is server-rendered (`makaton.html:1018`) and reads "a unique communication programme". The Gate quote is verbatim only in the meta description (`makaton.html:19–20`). The scope "an alternate/manual code supplementing speech" and the teaches cell "not a sign language proper" are the row's gloss; the page says "a communication programme that uses symbols (pictures), signs (gestures) and speech". Tier A holds as the maintainer's statement for that narrow scope. Smallest fix: a superseding row whose anchor reads "head meta Description (line 19); body text (line 1018) adds 'unique'" and whose scope is limited to the page's own words. In the lesson, change `round-51.md:47` to say "meta description".

**F6 (low). S093 paragraph number and edition.** `SOURCES.md:122` anchor says "product description ¶1 and ¶3"; `round-51.md:50` says "book description ¶3". In the capture the description has two body paragraphs (the 11th and 12th `<p>` blocks). The quote is in the second, and there is no ¶3. The capture also reads "Publication date: 03/15/1988" for ISBN 9780674270411, while the row cites "Groce 1985". Smallest fix: `round-51.md:50` → "description, second paragraph (¶2) of the 2024-12-10 capture". Name the edition actually read in a superseding row.

**F7 (low). S089 Gate URL elided.** `round-51.md:46` reads "https://www.routledge.com/The-Resilience-of-Language-…/9781841694368" with an ellipsis. The row URL (`SOURCES.md:118`) is the checkable one. The quote and tier hold on the Routledge page. Smallest fix: paste the full URL into `round-51.md:46`.

**F8 (low). S092 tier A rests on an archive summary.** `SOURCES.md:121` gives tier A to the ELAR "Summary of the collection". Criterion 6 treats abstracts as B for substantive claims about a work. The row's own scope limits A to "field counts reported by the depositor", and the depositor is the primary observer, so A holds for those counts. This is a judgement call, not a defect. Smallest fix: keep A for the counts only. For the threat and ecology prose, either a superseding row sets B, or a queued row for the depositor's primary work (de Vos 2012, cited in the deposit's "Collection history") is added.

**F9 (low). Entry line 90 credits S094 with a claim it does not state.** Entry line 90 says "Battison added it as a fourth parameter (S094)". S094's row (`SOURCES.md:123`) says only "four simultaneous aspects". The "fourth parameter" wording is in S096's teaches (`SOURCES.md:125`, tier B). Smallest fix: cite S096 for the history clause, or keep S094 for "four aspects" only.

**F10 (low). S094 section title differs between anchor and Gate.** `SOURCES.md:123` anchor: "Restrictions on Combinations of Primes: Simultaneous Morpheme Structure Conditions" (article pp. 3–5). `round-51.md:51` Gate: "'Restrictions on Combinations of Primes' section". Smallest fix: align the lesson bullet with the anchor.

**F11 (medium). S094 access route needs an integrator decision.** `SOURCES.md:123` says the row was "opened via headless browser" past a Cloudflare gate. The build record (`.ufo/waves/round-51/build/ScribeSec05Phonology.md:70`) says the headless tab "passed the challenge" and saved the PDF to /tmp. A bot challenge is an access control. Lane rules bar logins and paywall bypass, and I did not pass the challenge. Smallest fix: the integrator decides whether that route is within lane bounds, and the row or lesson records it accurately. If it is not, F1 stays open until an accessible copy is used.

**F12 (low). Entry line 77 states an inference as a finding.** Entry line 77 says "family transmission is the minority route (S091)". Source p. 27: "Typically, deaf people in Adamorobe live in hearing families, with one, two or no deaf family members." "Minority route" is an inference. Smallest fix: mark it `[INFERENCE]` or cite the sourced sentence.

## Residual risk and verification gaps

- S094: the quote, the ~45 and ~25 counts, the minimal pairs, the symmetry wording, the dominance list and the anchor pages (pp. 3–5) are all unverified by this seat.
- S093: the live page (2026-10-22) is a WAF challenge, so the verdict rests on a December 2024 capture. The publisher's text may have changed since.
- S090: the body and the meta description differ by one word, "unique". Both are the programme owner's own text.
- S091: the text layer comes from poppler, which printed font-encoding warnings. Quotes were matched as exact strings after whitespace normalization. Nyst is internally inconsistent on one figure: p. 24 says "from 10% in 1971", while pp. 21 and 25 say 1961. The row's 1961 matches two of the three.
- Checks outside this item are listed as unrun above.

## Tooling record

No installs or updates. I used existing tools: /usr/bin/pdftotext and pdfinfo (poppler 26.08.0), curl 8.23.0, and python3 3.14.8 (standard library only). pypdf, pdfminer and PyMuPDF are not installed and were not needed. No pacman, uv, pip or npm action was taken.
