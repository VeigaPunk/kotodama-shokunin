# ReopenS077 — falsify of SOURCES rows S077–S082

- Seat: KotodamaR51a3.ReopenS077 (leaf; read-only on the lane).
- Item attacked: Gate rows S077–S082 in `corpus/SOURCES.md` (lines 106–111), the sourcing they carry under claim C, and every entry line that cites them.
- Access date for every URL below: 2026-10-22.
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, branch main.

## Verdict: HOLDS-WITH-FIXES

- All eight Gate quotes for these six rows appear verbatim at the stated place in the source. Checked against the saved page bytes, whitespace normalised. Every quote is 25 words or fewer.
- No row fails on quote, URL, access date, status or used-by path.
- Fixes are needed where a row's teaches cell, anchor, source cell or tier says more than its page carries, and where entry lines cite a row for a claim the row does not carry.
- No finding trips claim C's falsifiers (count, sweep exit, missing S-id, used-by path, forbidden names). The counts were not re-run by this seat.

## Axes checked

1. Quote verbatim at the stated location.
2. Quote 25 words or fewer.
3. Row URL equals the lesson Gate URL, and the URL opens.
4. Kind.
5. Tier under QUALITY criterion 6 (community is never A; abstracts and publisher descriptions are B).
6. Teaches cell and scope against the page.
7. Anchor against the page's sections.
8. Status, used-by, opened and recheck.
9. Entry lines that cite each row, for claims beyond the row's scope.

## Commands and exit codes

| # | Command (abridged) | Exit | Key output |
|---|---|---|---|
| 1 | mkdir of scratch pages dir, realpath, `date -u +%F`, curl of 8 URLs into the scratch dir | 0 (each curl_exit=0) | realpath gave the scratch pages path; date gave 2026-10-22; S077 HTTP 200, 87644 B; S078 200, 387145 B; S079 200, 58024 B; S080 **203**, 5590 B (script shell); S081 200, 86356 B (redirected to books.google.com.br); S082 200, 52293 B; S076 200, 81551 B; S121 200, 344796 B |
| 2 | sha256sum of the eight saved pages | 0 | S076 c13320ac150800bc; S077 54cd39c28b9c4317; S078 4bb534fd52b26dc0; S079 aef8bacffe62ed4a; S080 02c8e42edb0c280d; S081 da57123cd768bdfa; S082 faa08679b6ac803d; S121 e0160c9f4b9376e3 |
| 3 | `curl --version; python3 --version; sha256sum --version` | 0 | curl 8.23.0; Python 3.14.8; sha256sum 0.8.0 |
| 4 | Python: verbatim and word count of the eight Gate quotes against saved pages | completed, no error | S077a True, 13 words; S077b True, 9; S078 True, 16; S079a True, 25; S079b True, 11; S080 False (saved HTML is the PubMed script shell); S081 True, 13; S082 True, 15 |
| 5 | Python: page titles and claim-term probes (S077, S078, S079, S081, S082, S076, S121) | completed | see Findings |
| 6 | curl of NCBI E-utilities efetch, PMID 15375269, saved as S080-eutils.txt | 0 | HTTP 200, 1448 B; sha256 8df9881b…47d0c9; abstract contains the S080 quote verbatim |
| 7 | Python: S080 abstract terms; S079 homesign term; S078 and S077 quote placement; S082 and S081 teaches terms | completed | S078 quote at offset 2221, before the numbered list at 2611; S077 quote order checked; all S082 and S081 teaches terms present |
| 8 | Python: label terms on S077, S078, S076, S121 | completed | S077 hit "hearing-impaired" (photo caption); S078 none; S076 all three; S121 all three plus "not acceptable" |
| 9 | `read` of SOURCES rows (grep for S076/S120/S121; raw lines 105, 150); lesson Gate; QUALITY lines 18–60; entry lines 1–223 and 190 raw; skill and RULES files | n/a (tool reads) | — |
| 10 | `_grep` of the entry for round-51, boundary-count, lessons/round, S123, S124 | no matches | — |
| 11 | realpath of the report path; directory and existence check | 0 | path inside the lane; falsify directory present; report absent before this write |

Installs and updates: none. All tools were already on the host. No pacman use. No subagent dispatch.

Writes: this report only, in the lane. Fetched pages are in `/fast/scratch/hyaku/kotodama-r51a3-falsify/ReopenS077/pages/` (realpath checked; no link into the lane).

Not opened: `reports/round-51/calibration/` and any `/fast/scratch/hyaku/kotodama-r51-*` or `kotodama51-*` material.

## Source URLs opened (access 2026-10-22)

| Row | URL opened | Result | Quote at stated place | Tier and scope |
|---|---|---|---|---|
| S077 | https://www.un.org/en/observances/sign-languages-day | HTTP 200; reader and curl | Both quotes verbatim, under "How many people are deaf worldwide?" and "What are sign languages?", in that order | B holds for the natural-language and statistics scope |
| S078 | https://wfdeaf.org/resources/sign-language-rights/ | HTTP 200; reader and curl | Verbatim in the intro block, before the numbered list | B holds for WFD positions; the grammar claim rests on a position page |
| S079 | https://voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement/ | HTTP 200; reader and curl | Verbatim in "The Resilience of Language" ¶2 and "Hearing Gesture" ¶1 | A is contestable (M1) |
| S080 | https://pubmed.ncbi.nlm.nih.gov/15375269/ | HTTP 203 script shell to curl; reader used NCBI E-utilities | Abstract verified via E-utilities (below) | B holds |
| S080 (same PMID) | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=15375269&rettype=abstract&retmode=text | HTTP 200 | Abstract verbatim; header matches the row citation | — |
| S081 | https://books.google.com/books/about/Sign_Languages_of_Aboriginal_Australia.html?id=Aa34NAEACAAJ | HTTP 200 after redirect to books.google.com.br (pt-BR interface, English description) | Description verbatim | B holds; "paperback" not on page (L7) |
| S082 | https://gupress.gallaudet.edu/Books/M/Manual-Communication | HTTP 200; reader and curl | Description ¶1 verbatim; system names and table of contents present | B holds |
| S076 (extra, for entry line 215) | https://nad.org/knowledge-hub/american-sign-language/community-and-culture-frequently-asked-questions/ | HTTP 200 | Q&A names the three labels | — |
| S121 (extra, for entry lines 210, 213, 215) | https://wfdeaf.org/contact/faqs/ | HTTP 200 | "These terms are not acceptable"; "The WFD estimates more than 70 million deaf people belong to signing deaf communities" | — |

## Row verdicts

| Row | Gate quote | Words | Kind and tier | Scope | Anchor | Status, used-by, opened | Verdict |
|---|---|---|---|---|---|---|---|
| S077 | verbatim (2 quotes) | 13, 9 | docs; B holds | natural-language and statistics scope holds; International Sign wording and "(estimate)" overstate (L1) | names 2 sections; teaches cites 2 more (L2) | mined; entry path; 2026-10-22; recheck on-release (L3) | HOLDS-WITH-FIXES |
| S078 | verbatim | 16 | docs; B holds for WFD position | WFD-position scope holds; "integral to deaf culture" wording (L5); grammar claim thin (L6) | intro and Sign Language Work sections exist | mined; entry path; 2026-10-22; 365d | HOLDS-WITH-FIXES |
| S079 | verbatim (2 quotes) | 25, 11 | docs; A contestable | homesign and co-speech scope holds; "not a conventional system" not on page (M2); term "homesign" not on page (L10) | both sections exist | mined; entry path; 2026-10-22; 365d | HOLDS-WITH-FIXES |
| S080 | verbatim (via E-utilities) | 19 | paper; B holds (abstract) | holds | Abstract holds | mined; entry path; 2026-10-22; 365d | HOLDS (entry overreach at line 131, M3; link note L11) |
| S081 | verbatim | 13 | book; B holds (publisher description) | book programme holds; speech-ban use not on page (M4); "paperback" not on page (L7) | description holds | mined; entry path; 2026-10-22; 365d | HOLDS-WITH-FIXES |
| S082 | verbatim | 15 | book; B holds (publisher description) | holds for education and system names; therapy and mapping not on page (L9) | Description ¶1 and table of contents hold | mined; entry path; 2026-10-22; 365d | HOLDS-WITH-FIXES (L8 "ed." unobserved) |

## Findings

### Medium

**M1 — S079 tier A is contestable.** `corpus/SOURCES.md:108`.
Evidence: the page calls itself a summary: "My book, The Resilience of Language, summarizes these findings and considers what they tell us…" (checked on the saved page). It is the author's own summary of her book and lab, not an original paper. QUALITY criterion 6 makes descriptions of a work tier B for substantive claims about it, even when accurate. Tier A could be argued as the author's own statement, but the row's scope does not say so.
Fix: a superseding row (the lane's correction form; next free id; teaches opens "supersedes S079 —") at tier B, scope "the author's own summary of her lab's findings". Or add the primary book or paper as a tier-A row and cite that for the homesign claims. No in-place tier edit.

**M2 — S079 teaches cell and entry line 64 claim more than the page says.** `corpus/SOURCES.md:108`; `corpus/knowledge/linguistics/sign-languages-manual-modality.md:64`.
Evidence: the teaches cell says co-speech gesture "is not a conventional system". The page does not say that. Checked absent from the saved page: "conventional system", "not a conventional", "universal", "shared convention", "unbounded". The page supports only that gestures "often convey substantive, task-related information" and the "hand-waving" line. Entry line 64 adds "universal among speakers (S079)", "unbounded; no shared convention" and "not a conventional system (S079)". The gloss comes from the S079 Gate bullet in `corpus/lessons/round-51.md`: "Grounds: co-speech gesture is not a system…". That is a gloss, not a quote.
Fix: a superseding row for S079 without the clause. Entry line 64: keep "information-bearing (S079)"; drop the three unsupported cells, or mark them (H) or (to-verify), or cite a row that says them.

**M3 — entry line 131 cites S080 for claims the abstract does not carry.** `corpus/knowledge/linguistics/sign-languages-manual-modality.md:131`.
Evidence: the line says the founder cohort "(a school or village generation) whose peer learning became the grammar (S080)", and that later cohorts show "the Nicaraguan cohorts' regularized grammar (S080)". The abstract (E-utilities text, checked) contains none of: peer, school, village, grammar, regulari. It says children "analyzed complex events into basic elements and sequenced these elements into hierarchically structured expressions", and that "Successive cohorts of learners extended this procedure".
Fix: restate in the abstract's words. For the school point, cite S088; its Gate in the lesson says deaf-community sign languages are "typically organized around the establishment of a school for deaf children" (S088 not opened by this seat). Mark the rest (H).

**M4 — entry line 40 cites S081 alone for speech-ban use.** `corpus/knowledge/linguistics/sign-languages-manual-modality.md:40`.
Evidence: the line says "alternate sign systems used while speech is banned (S081)". The Google Books description has no speech, taboo, disallowed or impractical term (checked on the whole page). S081 supports only that the book treats signed representation of spoken language. Line 40 has no second citation.
Fix: cite S109 for the speech-ban clause. Its Gate in the lesson reads "as an alternative to speech when speech is either impractical or disallowed". Keep S081 for "non-vocal representation" only, as line 135 already does.

### Low

**L1 — S077 teaches cell and entry line 209 drop attribution and change the verb.** `corpus/SOURCES.md:106`; entry line 209.
Evidence: (a) the teaches cell says "International Sign is a pidgin with a limited lexicon". The page says "It is considered a pidgin form of sign language that is not as complex as natural sign languages and has a limited lexicon." (b) The teaches cell says "more than 300 sign languages (estimate)". The page never says "estimate". It says "Collectively, they use more than 300 different sign languages." (c) Entry line 209 says "More than 300 sign languages exist". The page says deaf people "use" them.
Fix: a superseding row restating the attribution and the verb. Entry line 209: "deaf people collectively use more than 300 (UN page)".

**L2 — S077 anchor is incomplete.** `corpus/SOURCES.md:106`.
Evidence: the teaches cell draws "CRPD equal-status framing" from "What does the Convention on the Rights of Persons with Disabilities say about sign languages?" and "preserving sign languages as linguistic-cultural diversity" from "More on the UN Resolution". The anchor names only "What are sign languages?" and "How many people are deaf worldwide?". Both sections exist on the page.
Fix: a superseding row whose anchor names all four sections.

**L3 — S077 recheck does not fit the source.** `corpus/SOURCES.md:106`.
Evidence: recheck is "on-release", but the page is a yearly observance page with no release to watch. Entry lines 11 and 219 tell readers to re-open S077 before quoting any count.
Fix: change recheck in place to 365d, logging old→new in the round-51 lesson (the preamble allows in-place recheck changes).

**L4 — entry line 215 cites S077 and S078 for label rejection, and neither carries it.** `corpus/knowledge/linguistics/sign-languages-manual-modality.md:215`.
Evidence: the S078 page has none of "deaf-mute", "dumb" or "hearing-impaired" (checked). The S077 page has "hearing-impaired" only in a photo caption ("his hearing-impaired brother"), not as a rejection. S076 (the NAD Q&A) and S121 ("These terms are not acceptable") carry the rejection.
Fix: change the citation on line 215 to (S076, S121).

**L5 — S078 teaches cell misstates the page.** `corpus/SOURCES.md:107`.
Evidence: the teaches cell says "sign languages integral to deaf culture and identity". The page says sign languages are "integral to the human rights of deaf people", and that sign language is "a crucial part of deaf culture and identity". The phrase "integral to deaf culture" is not on the page (checked).
Fix: a superseding row using the page's words.

**L6 — S078 is the only citation for grammar claims, and line 205 adds a claim it does not carry.** `corpus/SOURCES.md:107`; entry lines 205–206.
Evidence: the page is WFD's rights position; the row's scope "WFD positions" holds for that. Line 205 cites S078 for "not a transcription of speech", and "transcription" is absent from the page (checked). Tier B is allowed as sole support, but a grammar claim reads better with a linguistic row beside it.
Fix: drop "not a transcription of speech" from line 205 or source it elsewhere. Co-cite a linguistic row for the grammar claim (S072 is a candidate; not opened here).
Cross-row note, outside the six: S076 (`corpus/SOURCES.md:105`) is tier A for a deaf advocacy organisation's FAQ, while S078 and S121 (both WFD) are tier B. Same kind of source, different tier. Left for the integrator; not decided here.

**L7 — S081 source cell says "paperback" and the page does not.** `corpus/SOURCES.md:110`.
Evidence: the page reads "Edição reimpressão" (reprint edition), ISBN 1107414210 and 9781107414211, and "562 páginas". "Paperback" is absent (checked). The URL redirects to books.google.com.br, pt-BR interface, English description intact. The lesson's S081 bullet also says "pb ed." (`corpus/lessons/round-51.md`).
Fix: a superseding row: "CUP 2013 reprint edition, ISBN 9781107414211, as listed on the Google Books page (pt-BR locale)".

**L8 — S082 source cell says "Bornstein ed." and the page does not.** `corpus/SOURCES.md:111`.
Evidence: the page reads "By Harry Bornstein" and lists eight chapter contributors. "ed." and "edited" are absent (checked).
Fix: a superseding row, or write "Harry Bornstein, 2009; multi-contributor volume (page: 'By Harry Bornstein')".

**L9 — entry line 63 cites S082 for things its page does not say.** `corpus/knowledge/linguistics/sign-languages-manual-modality.md:63`.
Evidence: "therapy settings", "contact zones" and "map spoken structure onto signs (S082)". "Therap" and "map" are absent from the page (checked). The page supports education use and the system names: Pidgin Sign (Contact Sign), Signed English, Signing Exact English, Cued Speech.
Fix: keep S082 for "classrooms" and the names. For the English-order mapping, cite S074, which line 157 already cites; its Gate in the lesson says "discussion of the unique features of a manual English system". Drop "therapy settings" unless sourced.

**L10 — the word "homesign" is attributed to S079 but the page does not use it.** `corpus/knowledge/linguistics/sign-languages-manual-modality.md:37`, `:62`; `corpus/SOURCES.md:108`.
Evidence: "homesign" is absent from the S079 page (checked). The page describes the phenomenon: children of hearing parents create gestures without conventional input.
Fix: attribute the term to S087 (its Gate in the lesson: "Homesign is a basic communication system created within a family with one or few deaf members"). Keep S079 for the phenomenon.

**L11 — S080 link is not machine-readable.** `corpus/SOURCES.md:109`.
Evidence: the listed PubMed HTML URL returns HTTP 203 with a 5,590-byte script shell whose title is the host name. The abstract was verified through NCBI E-utilities for the same PMID (HTTP 200).
Fix (optional): add https://doi.org/10.1126/science.1100199 to the anchor cell, or record E-utilities as the access route. Not a verdict-changer.

## Checked and held

- Verbatim and location, all eight quotes (S077 two, S078, S079 two, S080, S081, S082).
- Word counts: 13, 9, 16, 25, 11, 19, 13, 15. None over 25.
- Row URL equals the lesson Gate URL for all six rows.
- Opened and accessed 2026-10-22 for all six.
- Status "mined" for all six; used-by is `corpus/knowledge/linguistics/sign-languages-manual-modality.md`; the entry cites all six.
- S080 citation fields match the PubMed header: Senghas A, Kita S, Ozyürek A; Science 2004 Sep 17;305(5691):1779-82; doi 10.1126/science.1100199.
- S081 teaches cell: "first book-length study", "nine years" and "structure of sign languages and their relationship to spoken languages" are on the page. Page shows 562 páginas.
- S082 teaches cell: system names are on the page.
- Entry line 213 ("WFD estimates more than 70 million deaf people belong to signing deaf communities (S121)") looked like a misattribution to S077. It is not: the S121 page carries that sentence verbatim. Citation correct.
- Entry line 210 (S121: "not acceptable"; preferred term "deaf" or "deaf people") verified.
- Entry lines 155, 203, 204 and 206 use the UN and WFD wording with attribution, as the pages support.
- Entry line 126: S080 "about 25 years"; abstract says "over the past 25 years". Consistent.
- Forbidden names for C (round-51, boundary-count, lessons/round, S123, S124): none in the entry.

## Entry lines that cite these rows

- S077: lines 11, 33, 155, 203, 204, 209, 213, 215, 219.
- S078: lines 33, 205, 206, 211, 213, 215.
- S079: lines 37, 62, 64.
- S080: lines 11, 38, 126, 131, 219.
- S081: lines 40, 135, 139, 190.
- S082: lines 41, 63.

## Residual risk and verification gaps

- Tier and scope are judgments. M1 could be argued the other way. If the lane keeps A for the author's own statement, the scope cell must say so.
- The S080 quote was verified in the E-utilities text, not the PubMed HTML page, which returns a script shell.
- S081 was verified on the pt-BR rendering of the same Google Books page.
- Fix pointers to S072, S074, S087, S088 and S109 are unverified by this seat; those rows were not opened here. Their Gate text is quoted from the lesson.
- This seat checked the entry lines listed above. It did not check the entry's other citations (S071–S076, S083–S124).

## Unrun checks (for the main agent)

- `find corpus/knowledge -name '*.md' | wc -l` (expected 227).
- `python3 -B reports/round-28/readme/sweep.py` (expected exit 0; footer total 227, linguistics 26).
- `python3 -B reports/round-51/boundary-count.py` (expected rows=15 resolved=15 distinct=15).
- `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json` (expected exit 0).
- `python3 -B tools/gates/provenance-audit.py corpus/knowledge/linguistics/sign-languages-manual-modality.md`.

## Tooling record

No installs or updates. Host tools used as found: curl 8.23.0 (libcurl 8.23.0), Python 3.14.8, sha256sum 0.8.0.
