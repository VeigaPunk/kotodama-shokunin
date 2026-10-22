# ReopenS113: re-open of SOURCES rows S113 to S118 (round 51, attempt 3, falsify)

- Seat: KotodamaR51a3.ReopenS113 (leaf seat; read-only on the lane). This file is the only write in the lane.
- Date of every source opening: 2026-10-22.
- Lane state: branch `main` at `9feb69e`. The four lane files I read have sha256 equal to their committed bytes on `main`: `corpus/SOURCES.md` (8000acb2854ef24d), `corpus/knowledge/linguistics/sign-languages-manual-modality.md` (1a71ae2dcf2ecacb), `corpus/lessons/round-51.md` (fa62e591bf4a3c14), `corpus/QUALITY.md` (5fc99f4624283fa4).
- Item attacked: SOURCES rows S113 to S118 (`corpus/SOURCES.md:142-147`), their Gate bullets (`corpus/lessons/round-51.md:70-75`), and every entry line that cites them.

## Verdict

**Item: HOLDS-WITH-FIXES.** Every Gate quote appears verbatim at its stated location, each is 25 words or fewer (7 to 23), all six URLs resolve (HTTP 200), all six rows are `mined`, and all six `used-by` cells name the entry, which cites each S-id. The defects sit in tier, scope and locator, not in the quotes. S117 fails as filed on tier.

| Row | Gate quote | Kind | Tier | Scope and anchor | Used-by (entry lines) | Verdict |
|---|---|---|---|---|---|---|
| S113 | Verbatim at PDF p. 6 (printed p. 5); 7 and 11 words | docs | A, but see F2 | Scope omits the 2007 survey date and sample; the quoted lines are respondents' views | Holds (:155, :156, :203) | HOLDS-WITH-FIXES (medium) |
| S114 | Verbatim in the announcement, first paragraph after the announcement; 23 words | docs | A; factual clause should be B (F5) | Row locates the announcement, not the position paper (F3) | Holds (:156) | HOLDS-WITH-FIXES (medium) |
| S115 | Verbatim in module text, same paragraph as the DRIVE example; 13 words | docs | B holds | Anchor misplaces the quote (F7); ASL scope dropped (F8) | Holds (:158, :190) | HOLDS-WITH-FIXES (low) |
| S116 | Verbatim at ¶3; 15 words | docs | A holds (maintainer statement) | Anchor covers ¶3 only (F9) | Holds (:158, :219) | HOLDS-WITH-FIXES (low) |
| S117 | Verbatim in the abstract; 16 words | paper | A fails: abstract only, and the paper calls itself a review (F1) | Scope says full text; anchor says abstract | Holds (:190) | FAILS as filed (medium) |
| S118 | Verbatim, abstract sentence 1; 20 words | paper | B holds (abstract only) | Holds | Holds (:11, :207) | HOLDS |

Terms used: a *superseding row* is a new row that corrects an old one. The SOURCES preamble (`corpus/SOURCES.md:9-12`) allows only `status`, `recheck` and `used-by` to change in place, and QUALITY criterion 6 (`corpus/QUALITY.md:29`) requires tier corrections by superseding row. The next free IDs are S125 and up (`_grep` for S125 and S126 found nothing).

## Findings

### F1 (medium): S117 is filed tier A, but its only support is the abstract, and the paper calls itself a review
- Pointer: `corpus/SOURCES.md:146` (tier A, anchor "Abstract"); `corpus/lessons/round-51.md:74` (Gate quotes the abstract).
- Evidence: the abstract rule makes abstracts tier B for substantive claims (QUALITY criterion 6, `corpus/QUALITY.md:29`; the assignment's rule). The full text opened today says "In this review, we will provide a brief introduction to fingerspelling" (§1) and the abstract says "We will first review and synthesize research" (https://pmc.ncbi.nlm.nih.gov/articles/PMC10622114/). The tier brief puts expert write-ups and surveys under B (`corpus/SOURCES.md:17-18`), and S118, a review resting on its abstract, is B. The scope cell says "(open-access full text)" while the anchor says "Abstract", so scope and anchor disagree.
- Only entry use: `corpus/knowledge/linguistics/sign-languages-manual-modality.md:190` (NON-CANON micro-example).
- Smallest fix: superseding row S125 ("supersedes S117 —") at tier B, anchor "Abstract; §1 Introduction, 'In this review'". Leave S117's tier unedited and log the change in `round-51.md`.

### F2 (medium): S113 presents respondents' opinions as findings, drops the survey's date and sample, and omits the split in views
- Pointer: `corpus/SOURCES.md:142` (teaches; scope "as surveyed by WFD experts"); entry `:155`, `:156`, `:203`.
- Evidence (printed page = PDF page minus 1; text from pdftotext):
  - Printed 5: "Below are some selected important quotations from the survey responses:". Both Gate quotes are italic respondent lines.
  - Printed 4: the questionnaire went out "during Spring 2007" to WFD experts, sign linguists and WASLI interpreters; "Responses … were received from 24 of 35 respondents in 12 countries"; "Seven (7/24) are Deaf linguists or work with sign language".
  - Printed 5 also has a dissent: "It fulfils all criteria of human language".
  - Printed 11: "This is only a survey of the respondents' opinions but some linguists have also reported various results and opinions about the status of IS." Also: "The main result in this survey shows that International Sign Language is considered not to be a language, but something language-like."
  - Printed 7: "Most of the respondents don't agree International Sign is a pidgin or a Creole." The row says "most surveyed experts".
  - The teaches (`:142`) and the entry (`:155` "a fixed language (S113)"; `:156` "no native users") state respondents' views as facts.
  - Tier A is defensible only for what respondents said. The tier brief lists "survey" under B (`corpus/SOURCES.md:17-18`).
  - The teaches' printed-7 claim has no Gate quote.
- Smallest fix: superseding row S126 with teaches "2007 survey, 24 of 35 respondents: respondents called IS contact signing, said it has no native users, and split on whether it is a language (printed 5, 11)". Tier A for that scope, or B if the team reads "survey" as the tier brief's B example. Cite the report in the form it requests ("Perspectives on the Concept and Definition of International Sign", by Dr. Johanna Mesch for the World Federation of the Deaf, 2010). In the entry, attribute "no native users" to respondents or source it to linguistic work; the report points to Rosenstock 2004 and 2005, which the lane does not hold. Add the printed-7 quote to the round-51 Gate.

### F3 (medium): S114 cites the announcement, but the policy text the row describes is in the position paper
- Pointer: `corpus/SOURCES.md:143` (URL is the announcement).
- Evidence: the announcement's "Read the Position Paper" link goes to https://wfdeaf.org/resources/in-drafting-phase-position-paper-on-the-right-to-choose-sign-language-interpretation/ (HTTP 200). That page links the PDF https://wfdeaf.org/wp-content/uploads/Position-Paper-on-the-right-of-deaf-people-to-choose-and-access-International-Sign-interpretation-services.pdf (HTTP 200; 10 pages; "24 March 2025"). In the PDF, p. 3 says "it cannot replace the primacy of the national sign languages in the lives of deaf people", and p. 6 says "a national sign language interpreting services should take precedence over IS interpreting services". Neither line, nor "substitute", is on the announcement. The announcement's Gate sentence is not in the PDF; the PDF's key points (p. 1) say "Deaf people have the right to choose services and service providers according to their individual requirements and personal preferences".
- Smallest fix: superseding row S127 that anchors the policy clauses to the PDF (pp. 1, 3, 6), keeps the announcement as the dated secondary locator, and keeps the verbatim Gate quote.

### F4 (medium): the entry says S114 supports "a universal sign language"; S114 never says it
- Pointer: `corpus/knowledge/linguistics/sign-languages-manual-modality.md:156` ("What it is not" column).
- Evidence: "universal" is absent from both the announcement and the PDF (checked). Support lies elsewhere: S085 ("There is no universal sign language") and S121 (WFD FAQ).
- Smallest fix: at `:156`, cite "universal" to S085 or S121, and cite the "replacement" clause to the PDF (F3).

### F5 (medium): S114's factual clause sits under an A row scoped to policy, and the lane's WFD tiers disagree
- Pointer: `corpus/SOURCES.md:143` (teaches "IS interpreting is unregulated and undersupplied"). Compare `:107` (S078, WFD positions, B), `:150` (S121, WFD FAQ facts, B), `:105` (S076, NAD, A for term-preference scope only).
- Evidence: the announcement says "remain unregulated, and there are too few qualified interpreters". The PDF (p. 1) says "The regulation of IS interpreting services is in its infancy and currently lacks robust regulation and quality controls, and the pool of skilled and professional-level IS interpreters is scarce globally", and "outstripping the limited supply … of qualified IS interpreters". These are an advocacy body's factual claims about the world. The lane tiers WFD factual claims at B (S121). The row is A for "WFD's own policy".
- Smallest fix: superseding row with the policy clause at tier A (PDF p. 1, "right to choose") and the factual clause at tier B. Write one rule for organisational position statements into `SOURCES.md`.

### F6 (low): S114's publication status is not settled by the material
- Pointer: `corpus/SOURCES.md:143`; PDF metadata.
- Evidence: the PDF's metadata title is "Draft-PositionPaper-SLI-righttochoose.docx" (created 24 March 2025). The resource page slug says "in-drafting-phase". The PDF text does not contain "draft" but says "WFD Position Paper on International Sign: to be developed." (p. 3). The announcement calls it "its latest Position Paper".
- Smallest fix: name the version cited. If the PDF is a draft export, mark status `(to-verify)` and do not present it as adopted policy.

### F7 (low): S115 anchor says "paragraph after the DRIVE (HKSL) example", but the quote sits inside the DRIVE paragraph
- Pointer: `corpus/SOURCES.md:144` (anchor).
- Evidence: the quoted sentence is the last sentence of the paragraph that describes DRIVE in words. The "DRIVE (HKSL)" image caption comes after the quote. Order in the extracted text: DRIVE description, then quote, then caption.
- Smallest fix: anchor "the paragraph describing the DRIVE (HKSL) example, last sentence, before the DRIVE image caption".

### F8 (low): S115 teaches drop the ASL scope and the page's own caveat
- Pointer: `corpus/SOURCES.md:144` (teaches); entry `:158`.
- Evidence: the page says Stokoe's notation captures the possible values "in American Sign Language", and that "This list is not meant to cover the possible handshapes, locations and movements found in all sign languages." (both verified).
- Smallest fix: superseding teaches "…for ASL; the page says the list does not cover all sign languages".

### F9 (low): S116 anchor covers ¶3 only, but the teaches draw on ¶1, ¶2, ¶4 and ¶5
- Pointer: `corpus/SOURCES.md:145` (anchor "¶3 of the HamNoSys page").
- Evidence: ¶1 has "phonetic" and "in the tradition of Stokoe-based systems"; ¶2 has "The current version 4"; ¶4 has "unicode-based character set"; ¶5 has "basis for a series of avatar controls" (all verified). "explicitly independent" glosses "does not refer to national diversified finger spelling" and slightly overstates it.
- Smallest fix: superseding anchor "¶1 to ¶5 (quote at ¶3)"; drop "explicitly".

### F10 (low, note): S118 locator is a search-API query
- Pointer: `corpus/SOURCES.md:147`.
- Evidence: the JSON record matches the row (DOI 10.1093/deafed/enp026; 2010; vol. 15, no. 1; pp. 3-16; pubTypes Review and Journal Article; isOpenAccess N; abstract sentence 1 verbatim). Tier B fits an abstract-only row.
- Smallest fix (optional): give https://doi.org/10.1093/deafed/enp026 as the locator in a superseding row.

### F11 (low, records): the round-51 Gate carries one quote per row, and several teaches clauses have no Gate quote
- Pointer: `corpus/lessons/round-51.md:70-75`.
- Evidence: each teaches clause I checked is in its source (see checker output below), but the Gate lacks: S113 printed-7 claim; S114 "unregulated" and "too few"; S115 ASL; S116 ¶1, ¶2, ¶4, ¶5; S117 abstract sentence 1; S118 "critically reviews".
- Smallest fix: add those located quotes to the Gate bullets.

## Checks that held

- Gate quotes: verbatim in every source (checker, below). Word counts 7, 11, 23, 13, 15, 16, 20, all at most 25.
- Access date 2026-10-22 for every opening. No logins, no paywall bypass, no downloads into the lane.
- Kind: no row has kind `community`, so "community is never A" is not triggered. S113 to S116 are docs; S117 and S118 are paper.
- Abstract rule: S118 keeps it; S117 breaks it (F1).
- Publisher descriptions: none among these six rows.
- used-by: all six name `corpus/knowledge/linguistics/sign-languages-manual-modality.md`, which exists and cites each S-id (S113 at :155, :156, :203; S114 at :156; S115 at :158, :190; S116 at :158, :219; S117 at :190; S118 at :11, :207).
- Queued rows: none in this set. All six are `mined`.
- Committed bytes match the working copy for the four lane files (hashes above).
- Gate URLs: each Gate bullet names the same URL as its source cell for all six rows (S113 PDF; S114 announcement; S115 module; S116 HamNoSys page; S117 PMC page; S118 Europe PMC record). No Gate URL differs, so no second URL is needed.

## Sources opened (every URL, access date 2026-10-22)

| # | URL | HTTP, type, size | What I found | Verdict |
|---|---|---|---|---|
| 1 | https://wfdeaf.org/wp-content/uploads/Perspectives-on-the-Concept-and-Definition-of-IS_Mesch-FINAL.pdf (S113) | 200, pdf, 439,206 B | 15 pages; title as row; "May 2010"; §3 at printed 5 (PDF 6) and §5 at printed 7 (PDF 8); both Gate quotes verbatim on PDF 6 | Quote holds; tier A holds only for respondents' views (F2) |
| 2 | https://wfdeaf.org/position-paper-on-the-right-of-deaf-people-to-choose-and-access-international-sign-interpretation-services/ (S114) | 200, html, 345,863 B | Announcement dated March 24, 2025; Gate quote in the paragraph after the announcement; "unregulated, and there are too few qualified interpreters" in the same paragraph; no "substitute", no "universal" | Quote holds; locator (F3); factual clause (F5) |
| 3 | http://www.cslds.org/apsl-consortium/sign-linguistics/4-sign-phonetics-and-phonolgy-stokoes-notation-symbol/ (S115) | 200, html, no redirect, 93,826 B | "Module 4 – Sign Phonetics and Phonolgy: Stokoe's notation symbol"; Gate quote verbatim; ASL scope and caveat present | Quote holds; B holds; F7, F8 |
| 4 | https://www.sign-lang.uni-hamburg.de/dgs-korpus/hamnosys-97.html (S116) | 200, html, 14,407 B | Page "HamNoSys - EN"; ¶3 quote verbatim; ¶1, ¶2, ¶4, ¶5 support the teaches | Quote holds; A holds; F9 |
| 5 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10622114/ (S117) | 200, html, 257,846 B | Brittany Lee and Kristen Secora; Languages (Basel) 2022 Nov 1; 7(4):278; doi 10.3390/languages7040278; abstract quote verbatim; "In this review" in §1 | Quote and metadata hold; tier A fails (F1) |
| 6 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/deafed/enp026&resultType=core&format=json (S118) | 200, json, 4,401 B | Kusters A., 2010; J Deaf Stud Deaf Educ 15(1) 3-16; doi; pubTypes Review, Journal Article; isOpenAccess N; abstract sentence 1 verbatim | Holds; B holds (F10 note) |
| 7 | https://wfdeaf.org/resources/in-drafting-phase-position-paper-on-the-right-to-choose-sign-language-interpretation/ (linked from S114 page) | 200, html, 381,742 B | Resource page "Position Paper on the Right to Choose Sign Language Interpretation"; links PDF #8 | Locator for F3 |
| 8 | https://wfdeaf.org/wp-content/uploads/Position-Paper-on-the-right-of-deaf-people-to-choose-and-access-International-Sign-interpretation-services.pdf (linked from #7) | 200, pdf, 362,633 B | 10 pages; "24 March 2025"; key points p. 1; "cannot replace the primacy" p. 3; "to be developed" p. 3; "take precedence" p. 6; metadata title "Draft-PositionPaper-SLI-righttochoose.docx" | Policy text (F3); status (F6); factual clause (F5) |

## Commands run (in order, with exit codes)

1. bash: `mkdir -p` scratch directory; `command -v` for curl, pdftotext, pdfinfo, python3, jq; `date -I`. Output: all five found; `2026-10-22`. Exit 0.
2. bash: curl of the six SOURCES URLs to scratch, with `-w` HTTP code. Output: 200 for all six (S113 pdf 439206 B; S114 html 345863; S115 html 93826, final URL http; S116 html 14407; S117 html 257846; S118 json 4401). Exit 0 for each curl.
3. read: the same six URLs (reader). Content as in the table above. No errors.
4. _grep `S11[3-8]` in `corpus/SOURCES.md`: rows at lines 142 to 147 and the Gate and recheck mentions. Exit: matches found.
5. _grep `S11[3-8]` in the entry: lines 10 to 12, 154 to 158, 190, 202 to 210, 219. Exit: matches found.
6. read: `corpus/SOURCES.md:1-40`, `:139-150` (raw); `corpus/lessons/round-51.md:70-76` (raw) and the full lesson; `corpus/QUALITY.md`; `reports/round-51/claims.json`; `skill://godspeed`; `/home/vgpnk/.omp/agent/RULES.md`. No errors.
7. read: entry `:150-160` and `:186-222` (raw); `corpus/knowledge/verification/calibration-registry.md:33-40` (raw). No errors.
8. _grep: WFD and NAD rows and "community" kind rows in `SOURCES.md`; claim terms (unregulated, substitute, native users, conventionalization, pidgin, universal, Stokoe) in the entry. Exit: matches found.
9. bash: `pdfinfo S113.pdf` (exit 0; 15 pages); `pdftotext` whole file and per-page (exit 0). A first footer and heading grep matched nothing and exited 1 ("Command exited with code 1"); the rerun with a page-level pattern exited 0 and showed headings on PDF pp. 6, 8, 12 and the footer "11 | P a g e" on p. 12.
10. bash: python3 HTML-to-text for S114, S115, S116, S117, and JSON parse for S118. Exit 0. Output: S114 5,576 characters; S115 11,788; S116 3,645; S117 107,725; S118 doi, pubYear, volume, issue, pages, pubTypes.
11. bash: python3 quote checker, 39 checks (below; S113 12, S114 6, S115 4 plus one order line, S116 7, S117 7, S118 3). Exit 0; "TOTAL mismatches=0".
12. bash: grep of the announcement's href values and curl of the resource page. Exit 0; resource page HTTP 200, 381,742 B.
13. read: resource page (HTTP 200). It links the PDF.
14. bash: curl of the PDF (HTTP 200, 362,633 B), `pdfinfo` (exit 0; 10 pages; title "Draft-PositionPaper-SLI-righttochoose.docx"), `pdftotext` (exit 0), grep (exit 0), and a python quote check. The python check exited 0: the announcement's Gate sentence, "unregulated", "too few qualified interpreters", "not a substitute", "substitute" and "universal" were all absent from the PDF text (the PDF's wording differs).
15. read: PDF text lines 1 to 300 (of 475), and _grep for regulation and supply terms. Matches at PDF lines 25 to 31, 290, 351 to 356, 388 to 411.
16. bash: per-page locator for the PDF phrases. First attempt exited 1 (TypeError: my format string applied to a list; code error, not a source problem). Rerun exited 0 with page numbers (below).
17. bash: lane realpath; `git -C <lane> rev-parse --short main` (exit 0; `9feb69e`); sha256 of four files on `main` against the working copy (exit 0; all equal); `ls -ld` of the report folder; listing of the round-51 wave folder. Exit 0.
18. _grep `S125|S126` in `corpus/SOURCES.md`. Output: no matches (S125 is free).
19. bash: python3 survey-split checker, 5 checks (below). Exit 0; mismatches 0.

## Checker output (condensed labels; needles unchanged)

```
== S113 Mesch PDF (PDF pages 1, 5, 6, 8, 12 = printed 1, 4, 5, 7, 11)
OK found=True expect=True words= 7 | Gate q1 'It is a form of contact signing.' p6
OK found=True expect=True words=11 | Gate q2 'There are no native users of IS as a first language.' p6
OK found=True expect=True words=14 | teaches: degree of conventionalisation critical to status p6
OK found=True expect=True words= 7 | framing: 'selected important quotations from the survey responses' p6
OK found=True expect=True words=10 | framing: 'various opinions about whether it is a language or not' p6
OK found=True expect=True words=12 | sample: 'received from 24 of 35 respondents' p5
OK found=True expect=True words=10 | sample: 'Seven (7/24) are Deaf linguists or work with sign language' p5
OK found=True expect=True words= 3 | section 5 heading 'Pidgin or Creole?' p8
OK found=True expect=True words=14 | teaches: most respondents reject pidgin/creole p8
OK found=True expect=True words= 9 | own limit: 'This is only a survey of the respondents' opinions' p12
OK found=True expect=True words=19 | own limit: 'There is a difference ... linguistic research on IS' p12
OK found=True expect=True words= 2 | cover 'May 2010' p1
== S114 WFD position paper (announcement)
OK found=True expect=True words=23 | Gate q 'Deaf people have the right to decide ...'
OK found=True expect=True words=13 | teaches: unregulated; too few qualified interpreters
OK found=True expect=True words= 3 | date 'March 24, 2025'
OK found=False expect=False words= 3 | teaches gloss 'not a substitute' (absent, as expected)
OK found=False expect=False words= 1 | entry gloss 'substitute' (absent, as expected)
OK found=False expect=False words= 1 | literal 'undersupplied' (absent; paraphrase of 'too few')
== S115 APSL module 4
OK found=True expect=True words=13 | Gate q 'the handshape, location and movement are the building blocks of a signed word'
OK found=True expect=True words=15 | teaches: simultaneous combination of three phonological elements
OK found=True expect=True words=16 | teaches: 'in American Sign Language' (values)
OK found=True expect=True words=18 | caveat: 'not meant to cover ... all sign languages'
S115 order: quote_at=7649 drive_example_text_at=7462 drive_caption_at=7744 quote_precedes_caption=True quote_after_example_text=True
== S116 HamNoSys page (paragraph lines 3-7 = paragraphs 1-5)
OK found=True expect=True words=15 | Gate q (para 3) 'HamNoSys does not refer to national diversified finger spelling ...'
OK found=True expect=True words= 6 | teaches para 1: 'in the tradition of Stokoe-based systems'
OK found=True expect=True words= 5 | teaches para 1: 'phonetic' transcription system
OK found=True expect=True words= 4 | teaches para 2: 'The current version 4'
OK found=True expect=True words= 3 | teaches para 4: 'unicode-based character set'
OK found=True expect=True words= 7 | teaches para 5: 'basis for a series of avatar controls'
OK found=False expect=False words= 2 | gloss 'explicitly independent' (absent, as expected)
== S117 Lee and Secora abstract
OK found=True expect=True words=16 | Gate q (Abstract) 'This manual representation of orthographic code ... translanguaging'
OK found=True expect=True words= 9 | teaches: 'Fingerspelling is a critical component of many sign languages.'
OK found=True expect=True words=15 | self-description: 'In this review, we will provide a brief introduction ...'
OK found=True expect=True words= 2 | metadata: Brittany Lee
OK found=True expect=True words= 2 | metadata: Kristen Secora
OK found=True expect=True words= 5 | metadata: Languages (Basel). 2022 Nov 1;7(4):278
OK found=True expect=True words= 1 | metadata: doi 10.3390/languages7040278
== S118 Kusters Europe PMC record
OK found=True expect=True words=20 | Gate q (abstract sentence 1 tail)
OK found=True expect=True words=15 | sentence 1 begins with the Martha's Vineyard island clause
OK found=True expect=True words= 7 | teaches: 'This article critically reviews the existing literature'
S118 doi=10.1093/deafed/enp026 pubYear=2010 volume=15 issue=1 pubTypes=['Review', 'Journal Article'] isOpenAccess=N
TOTAL mismatches=0 (exit 0)

== Survey split and conclusion (S113 PDF; run after the checker)
OK pdf-p6 (printed 5) | 7 words | It fulfils all criteria of human language
OK pdf-p6 (printed 5) | 17 words | Fluent users of International Sign regard this as a communication option on par with national sign languages
OK pdf-p12 (printed 11) | 21 words | The main result in this survey shows that International Sign Language is considered not to be a language, but something language-like
OK pdf-p12 (printed 11) | 9 words | IS is used only for formal and internal meetings
OK pdf-p8 (printed 7) | 14 words | Most of the respondents don't agree International Sign is a pidgin or a Creole
mismatches = 0 (exit 0)

== Position paper PDF (10 pages): phrase locations
pages=[3] 'it cannot replace the primacy of the national sign languages in the lives of deaf people'
pages=[6] 'a national sign language interpreting services should take precedence over IS interpreting services'
pages=[1] 'The regulation of IS interpreting services is in its infancy and currently lacks robust regulation'
pages=[1] 'the pool of skilled and professional-level IS interpreters is scarce globally'
pages=[1] 'outstripping the limited supply, capacity, and capability of quali' (ligature broken in extraction)
pages=[3] 'WFD Position Paper on International Sign: to be developed.'
pages=[1] cover title; '24 March 2025'; 'International Sign version'
pages=NONE for 'universal', 'substitute', 'draft' (text)
```

## Tooling

No installs or updates. I used tools already present: `curl`, `pdftotext` and `pdfinfo` (poppler), `python3`, `jq`. Fetched copies sit in `/fast/scratch/hyaku/kotodama-r51a3-falsify/ReopenS113/`, outside the lane, with no symlinks. I wrote nothing else in the lane.

## Not run, not read, residual risk

- Not run (outside this item): the lane counts (`find corpus/knowledge -name '*.md' | wc -l`), `reports/round-28/readme/sweep.py`, `reports/round-51/boundary-count.py`, `tools/gates/provenance-audit.py`, and the separability check.
- Not read in full: S117 §§2 to 12 (abstract, introduction and metadata read); S113 appendix (printed 13 to 14); S114 PDF lines 301 to 475 (searched for the regulation and supply terms).
- Not checked: entry prose beyond the cited lines.
- Residual risk: whether WFD has adopted the 2025 position paper as final is not settled by the material (F6).

## Out of scope, noticed in passing

For the S119 reopen seat: the round-51 Gate bullet for S119 (`corpus/lessons/round-51.md:76`) cites the Europe PMC record for DOI 10.1017/S1366728917000724, while the row (`corpus/SOURCES.md:148`) gives DOI 10.1017/S1366728918000585. I did not check either record.
