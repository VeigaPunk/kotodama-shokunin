# ReopenS071: falsify report for SOURCES rows S071–S076

Author-lane attack, not an admission. The verdict below is a recommendation to the L1.

**Item attacked:** SOURCES rows S071–S076 (`corpus/SOURCES.md:100–105`) and their Gate bullets (`corpus/lessons/round-51.md:28–33`). Also every caller of those ids in `corpus/knowledge/linguistics/sign-languages-manual-modality.md` (claim C).

**Access date for every URL:** 2026-10-22.

**Verdict: HOLDS-WITH-FIXES.**

- Every Gate quote for S071–S076 appears verbatim at its stated URL, and every quote is 25 words or fewer.
- S071 has a second Gate quote that is verbatim only in the 1960 text, not in the 1978 edition the row names (F1).
- S072's live publisher page is blocked, so its quote is confirmed only on a 2025 archive snapshot (F2).
- Three sentences in the entry cite sources that do not say what the sentences claim (F4–F6). These do not trip claim C's declared falsifiers, but they are provenance defects under QUALITY criterion 1. I recommend fixing them before C is called HOLDS.

## 1. Row checks

| Row | Gate quote and stated location | Words | Kind / tier | Scope and anchor | used-by | Result |
|---|---|---|---|---|---|---|
| S071 | "bring within the purview of linguistics a virtually unknown language", 1978 text, "1 INTRODUCTION / Purposes." | 11 | book / A | Anchor holds. "signification/action" is the wrong term (F7). "no post-1960 data" needs the edition named (F8). | Entry path, mined ✓ | HOLDS-WITH-FIXES |
| S071, Gate URL 2 | "Like consonant and vowel, the aspects position, configuration, and motion may only be described in terms of contrast with each other." Verbatim in the 1960 copy only. The 1978 text reads "action". | 21 | (same row) | Not the row's own edition (F1). | — | HOLDS at its URL; mismatch F1 |
| S072 | "Sign language linguists show here that all questions relevant to the linguistic investigation of spoken languages can be asked about sign languages." Verbatim on the 2025-03-09 archive snapshot of the publisher page. Live page blocked. | 22 | book / B | Programme description holds. HSK 37 and the editors (Pfau, Steinbach, Woll) hold on the snapshot. | Entry path, mined ✓ | HOLDS-WITH-FIXES (F2) |
| S073 | Heading "Pseudo Family: Sign Language"; title "Glottolog 5.3 - Sign Language" | 4 | dataset / A | Newick children match the teaches column (deaf-community, village/shared, auxiliary/alternate, Australian auxiliary sign languages). | Entry path, mined ✓ | HOLDS |
| S074 | "discussion of the unique features of a manual English system", Description ¶2 | 11 | book / B | 940 basic signs, 14 sign markers, glossary, exercises, Bornstein as former director of the Gallaudet Signed English Project: all verified. Two unquoted glosses (F12). | Entry path, mined ✓ | HOLDS |
| S075 | Abstract: "At one time, sign was viewed as nothing more than a system of pictorial gestures with no linguistic structure." | 19 | paper / A | Body anchors verified: Introduction ¶2 (P3), §3, §4.3 (P44–P45: sawmills, monastic orders, mourning taboo), §5, §7.2 (homesign, P80). The Gate itself quotes only the abstract (F3). | Entry path, mined ✓ | HOLDS-WITH-FIXES |
| S076 | "'Hearing-impaired' was a well-meaning term that is not accepted or used by many deaf and hard of hearing people." Q&A "What is wrong with the use of these terms…" | 19 | docs / A | Q&A anchor, accepted set (Deaf, DeafBlind, DeafDisabled, Hard of Hearing, Late-Deafened), and "ask the individual" all verified. Tier question (F9). | Entry path, mined ✓ | HOLDS-WITH-FIXES |

Other row facts checked:

- All six rows have status `mined`, `opened` 2026-10-22, and used-by naming `corpus/knowledge/linguistics/sign-languages-manual-modality.md`.
- The entry file exists (223 lines) and cites all six ids (entry lines 16, 19–21, 26, 29, 83, 87, 95, 142, 157–158, 204, 210).
- For S072–S076 the Gate URL equals the row's source URL. S071's Gate has a second URL that the row does not list (F1).

## 2. Findings, by severity

### F1 (medium): S071's second Gate quote is not in the row's edition
- Where: `corpus/lessons/round-51.md:28` (Gate URL 2, a third-party copy at joshiesworld.com) against `corpus/SOURCES.md:100` (the row names the 1978 ERIC/archive.org reprint).
- Evidence: The 1960 text layer (pdftotext of the joshiesworld PDF) reads "…configuration, and motion may only be described in terms of contrast with each other." The 1978 archive.org OCR reads "…con- figuration, and action may only be described in terms of contrast with each other." The joshiesworld copy is not in the row's source cell.
- Smallest fix: Re-quote the Gate from the 1978 text ("…and action may only be described…") and name the edition. If the 1960 copy is wanted, register it as its own row rather than editing this one.

### F2 (medium): S072's live publisher page cannot be re-opened, so the Gate's "accessed 2026-10-22" is not reproducible
- Where: `corpus/SOURCES.md:101`; `corpus/lessons/round-51.md:29`.
- Evidence: `https://doi.org/10.1515/9783110261325` redirects to `degruyterbrill.com/…/html`, which returned HTTP 202 with a 0-byte body. The reader view showed "Temporary error. Please try again" and a "Let's confirm you are human … Begin" interstitial. I did not try to solve the check. The archive snapshot of 2025-03-09 contains the quote, "Volume 37 in the series … [HSK]", and the editors.
- Smallest fix: Name the snapshot in the Gate (the same pattern S093 uses at `corpus/SOURCES.md:122`). Retry the live page later, and do not claim a 2026-10-22 live read unless it happens.

### F3 (medium): S075 is tier A, but its only Gate quote is from the abstract
- Where: `corpus/lessons/round-51.md:32`; `corpus/SOURCES.md:104`.
- Evidence: Criterion 6 makes abstract-only support tier B. The lane applied that rule to S080 (`corpus/SOURCES.md:109`, tier B "as stated in the abstract"). The body anchors do check out (see the S075 row above), but the Gate records no body quote.
- Smallest fix: Add a body quote to the Gate, for example P45: "in sawmills where noise prevents the use of speech, workers create silent gestures" (verbatim, 14 words). Any change of tier needs a superseding row, per criterion 6.

### F4 (medium): Two entry sentences cite S074 for content the S074 page does not state
- Where: `corpus/knowledge/linguistics/sign-languages-manual-modality.md:26` ("a designed code that keeps the spoken word order (S074)") and `:157` ("arranges a borrowed sign vocabulary in English word order (S074)"; "not ASL-English bilingual education (S074)").
- Evidence: The S074 Description and reviews say 940 basic signs, 14 sign markers, a glossary, exercises, and a "discussion of the unique features of a manual English system". A search of the saved page for word order, "borrowed", "bilingual", and "English word" found no content hits.
- Smallest fix: Delete the three clauses, or cite a source that states them.

### F5 (medium): Two master-claim sentences cite S072 for content the S072 description does not carry
- Where: entry `:16` ("does not derive from any spoken language (S071; S072)") and `:19` ("without this duality there is only a repertoire (S071; S072)").
- Evidence: The S072 publisher description (archive snapshot) describes the handbook's scope and says questions should be asked both ways. It says nothing about derivation or sublexical duality.
- Smallest fix: Cite S072 only for "the handbook's stated programme", or drop it from those two clauses.

### F6 (medium): The entry's "does not derive from any spoken language" omits S071's own qualifier
- Where: entry `:16`, citing S071.
- Evidence: The 1978 S071 text says ASL "stems both from the natural signing of deaf persons and the methodical sign language of Epée and Sicard", and that French and English influence on syntax "may be suspected". (Scratch copy of the archive OCR, `s071-archive-djvu.txt`, approximately lines 3673–3677 and 3717–3721.)
- Smallest fix: Qualify the clause, for example "not derived from a spoken language's grammar; methodical-sign contact influence is documented in S071".

### F7 (low): The term is "signation", not "signification"
- Where: `corpus/SOURCES.md:100` (teaches: "signification/action"); entry `:16` ("signification (movement)").
- Evidence: The 1978 text gives "tabula, or tab", "designator, or dez", and "siqnation, or sig" (OCR, approximately lines 2702–2704), and defines "Signation stands for 'the action of making a sign'" (approximately lines 5385–5390).
- Smallest fix: Write "signation (sig)" in both places.

### F8 (low): The S071 scope should name the edition
- Where: `corpus/SOURCES.md:100` ("no post-1960 data").
- Evidence: The cited text is the 1978 "Newly Revised" edition, with bracketed 1978 notes (for example Battison 1978, and "in 1978 that since 1960…").
- Smallest fix: Name the edition, and say the bracketed notes are commentary, not data.

### F9 (low): S076's tier A is inconsistent with S121 on the same scope
- Where: `corpus/SOURCES.md:105` (S076, tier A) against `corpus/SOURCES.md:150` (S121, a WFD FAQ on "terminology preferences", tier B).
- Evidence: The NAD page is a national advocacy organisation's FAQ. The SOURCES preamble says "community is never A" but does not say how that applies to organisations. Quote and page content verified.
- Smallest fix: Either make S076 tier B through a superseding row, or write a rule for organisation pages. Reword the teaches column from "are community-rejected" to "NAD states they are rejected".

### F10 (low): Two S075 teaches glosses are not in the cited paragraphs
- Where: `corpus/SOURCES.md:104` ("emblems are conventional forms without grammar"; "discredited stage-1 position"); entry `:204` ("discredited first stage").
- Evidence: P46 says "Emblems are hand movements that have conventional forms and meanings". The word "grammar" does not appear in P46, P61, or P63. P3 says the first stage was "considered nothing more than pantomime"; the paper does not use "discredited".
- Smallest fix: Quote the paper's own words in the teaches column.

### F11 (low): S075's year needs the online date
- Where: `corpus/SOURCES.md:104`.
- Evidence: The PMC record shows "Behav Brain Sci. 2015 Oct 5;40:e46" and "Issue date 2017 Jan".
- Smallest fix: Write "(2015 online; 2017 issue)".

### F12 (low): Two S074 glosses are not in the Description
- Where: `corpus/SOURCES.md:103` ("deliberately designed"; "a code for English, not ASL").
- Evidence: Neither phrase appears on the page. "Not ASL" is an inference from "manual English system".
- Smallest fix: Mark them as glosses, or drop them.

## 3. URLs opened (all accessed 2026-10-22)

| URL | What I found | Holds? |
|---|---|---|
| https://archive.org/details/micro_IA41153455_0834 | Item "Sign Language Structure." by Stokoe; publication date 1978-00-00; collection eric-microfiche. Full OCR (`…/stream/micro_IA41153455_0834/micro_IA41153455_0834_djvu.txt`, HTTP 200, 365,710 B) has "ED 189 878", "Linstok Press, Inc.", "Copyright © 1978", "Newly Revised", and "originally appeared as Occasional Paper 8 … 1960". Gate quote 1 is at "1 INTRODUCTION / Purposes." | Quote, anchor, kind, tier hold; F7, F8 |
| https://www.joshiesworld.com/wp-content/uploads/2025/10/stokoe_1960.pdf | HTTP 200, 22,561,312 B; 41 pages; text layer present. Gate quote 2 verbatim with "motion" (1960 text, §1.2). Third-party re-host. | Holds at its URL; not the row's edition (F1) |
| https://doi.org/10.1515/9783110261325 | Redirects to `https://www.degruyterbrill.com/document/doi/10.1515/9783110261325/html`: HTTP 202, 0 B, bot interstitial. Not solved. | Blocked live (F2) |
| https://api.crossref.org/works/10.1515/9783110261325 | HTTP 200, 2,094 B. Title "Sign Language"; editors Roland Pfau, Markus Steinbach, Bencie Woll; published 2012-08-16; publisher DE GRUYTER. No HSK or series field; no abstract. | Metadata holds (HSK not in this record) |
| https://web.archive.org/web/20250309160011id_/https://www.degruyter.com/document/doi/10.1515/9783110261325/html | Snapshot of 2025-03-09. HTTP 200, 376,561 B. "Volume 37 in the series … [HSK]"; "About this book": "Sign language linguists show here that all questions relevant to the linguistic investigation of spoken languages can be asked about sign languages."; the teaches list (typology, grammar, psycholinguistics, neurolinguistics, sociolinguistics, documentation and transcription) is present. | Quote, HSK 37, editors, anchor hold on the snapshot |
| https://www.degruyter.com/isbn/9783110261325; https://www.degruyter.com/document/doi/10.1515/9783110261325/html; https://doi.org/10.1515/9783110261325.fm | HTTP 202, 0 B each (bot interstitial). | Blocked |
| https://www.degruyter.com/view/product/179434 | A guessed product URL. HTTP 200, but the final URL is the site homepage (117,370 B). No book content used. | Not useful |
| https://glottolog.org/resource/languoid/id/sign1238 | Title "Glottolog 5.3 - Sign Language"; heading "Pseudo Family: Sign Language"; links to JSON and newick. | Holds |
| https://glottolog.org/resource/languoid/id/sign1238.json | `"category": "Pseudo Family"`. Newick includes "L1 Sign Language [deaf1237]", "Auxiliary Sign Systems [auxi1235]" with Australian auxiliary sign languages (Dieri, Gurindji, Jingulu, and others), "Adamorobe Sign Language", "Nebaj Shared Homesign Systems", and "International Sign" under "Pidgin Sign Language". | Holds |
| https://glottolog.org/glottolog/glottologinformation | HTTP 200, 62,524 B. Lists "Sign Language" among "non-genealogical trees"; says the methodology for signed languages "remains to be articulated". | Corroborates the S073 gloss |
| https://gupress.gallaudet.edu/Books/T/The-Signed-English-Starter | HTTP 200, 54,229 B. Description ¶2 quote verbatim. 940 basic signs; 14 sign markers; glossary; exercises for each of 12 chapters; Bornstein "former director of the Gallaudet Signed English Project"; paperback May 1984. No word-order, borrowing, or bilingual-education text. | Quote holds; F4 caller issue |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC4821822/ | HTTP 200, 368,753 B. Abstract quote verbatim (P1). P3 is Introduction ¶2. P44–P45 are §4.3 (sawmills, monastic orders, mourning taboo). Headings §3, §5, §7.2 present. P80 defines homesign. Metadata: BBS 2015 Oct 5 (online); issue 2017 Jan. | Quote holds (abstract); body anchors hold; F3, F10, F11 |
| https://nad.org/knowledge-hub/american-sign-language/community-and-culture-frequently-asked-questions/ | HTTP 200 (reader view). Q&A header verbatim. "'Hearing-impaired' was a well-meaning term…" verbatim. "the most commonly accepted terms have come to be Deaf, DeafBlind, DeafDisabled, Hard of Hearing, and Late-Deafened". "When in doubt, ask the individual how they identify themselves." | Quote holds; tier question F9 |

## 4. Commands run

| # | Command (shortened) | Exit | Result |
|---|---|---|---|
| 1 | `date -u +%F`; `mkdir -p` scratch dir; `realpath`; `curl --version`; `git -C <lane> log --oneline -4` (read-only) | 0 | 2026-10-22; curl 8.23.0; lane head `9feb69e`, `da31d3c`, `35f0d49`, `1f97472` |
| 2 | `curl -L` for five source URLs into scratch; `which pdftotext pdftoppm tesseract mutool qpdf`; Python import probes | 0 | HTTP 200, 200, 202 (0 B), 200, 200. pdftotext, pdftoppm, tesseract, qpdf present. fitz, pypdf, pdfminer not installed (not needed). |
| 3 | `pdfinfo`; `pdftotext -layout` on the joshiesworld PDF; DOI and degruyter probes; `file` on the djvu text | 0 | 41 pages; 272,026 characters; DOI resolves to degruyterbrill, HTTP 202 |
| 4 | `curl` probes: degruyter isbn, guessed product URL, DOI `.fm` | 0 | HTTP 202, 200 (homepage), 202 |
| 5 | `curl -L` of the Wayback capture of the S072 page; `grep -c "Sign language linguists show"` | 0 | HTTP 200, 376,561 B, capture 20250309160011; grep count 3 |
| 6 | `curl` CrossRef API; `grep -o 'HSK…'`; `grep -c series` | 1 (both greps: no match) | CrossRef HTTP 200, 2,094 B; no HSK or series field |
| 7 | `pdftotext -v`; `curl` Glottolog information page | 0 | pdftotext 26.08.0; HTTP 200, 62,524 B |
| 8 | `curl` Gallaudet page | 0 | HTTP 200, 54,229 B |
| 9 | `ls -la` on the entry file and report folder; `date -u` | 0 | Entry 37,549 B; report folder present |

Tool reads, greps, and Python extraction (no shell exit codes): the source pages above; lane greps for S071–S076 callers and for row and Gate line numbers; Python paragraph extraction of the PMC HTML and a search of the OCR. One grep ran before its file existed (a race with a parallel curl). I re-ran it after the curl finished, and the re-run is the result reported here.

## 5. Tools

No installs or updates. I used the pre-installed curl 8.23.0, poppler pdftotext and pdfinfo 26.08.0, and the Python standard library. I did not run pacman, sudo, pip, or uv. I read `/home/vgpnk/.omp/agent/RULES.md` before starting. Downloads went to `/fast/scratch/hyaku/kotodama-r51a3-falsify/ReopenS071/`, outside the lane. The only lane file I wrote is this report.

## 6. Not run and residual risk

- Not run (outside this item): claim C's counters (`find corpus/knowledge -name '*.md' | wc -l`, expected 227; `python3 -B reports/round-28/readme/sweep.py`), claim D's counter, and the separability checker.
- S072's live page was not re-opened. The quote is confirmed only on the 2025-03-09 archive snapshot.
- The S071 "action" reading comes from machine OCR of the archive.org scan. I did not check it against the page image. The 1960 text layer is clean.
- The copyright status of the joshiesworld re-host was not assessed.
- I did not check the seat attribution in the Gate bullets.
