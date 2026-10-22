# ReviewCSec06: falsify attack on claim C, entry section 6 "Grammar in space"

- Seat: KotodamaR51a3.ReviewCSec06 (leaf reviewer). Read-only on the lane; this file is the only lane write.
- Date: 2026-10-22. Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin, branch main, HEAD 9feb69e.
- Item attacked: claim C, entry `corpus/knowledge/linguistics/sign-languages-manual-modality.md` section 6 (lines 97-108). Also the three rows it cites (S098, S099, S100; `corpus/SOURCES.md` lines 127-129), every word-order claim in the entry, and the section 3 word-order cell (line 60), which cites S087 (SOURCES line 116).
- Coverage: all six section 6 rows and the lead sentence; every quoted fragment checked against its source; the anchors of S098, S099, S100 and S087; a scan of the whole entry for universal or word-order claims; calibration status; must-not-cite names for claim C.
- Axes: (1) each cited claim matches its source at the anchor; (2) qualifiers and scope survive paraphrase; (3) calibration status is named (QUALITY criterion 2; registry lines 36-38); (4) provenance and tier (QUALITY criteria 1 and 6); (5) terminology and cross-references.

## Verdict

**HOLDS-WITH-FIXES** for section 6, as a recommendation for the L1 (not an admission).

Every quoted fragment exists in its source. The three S-ids resolve, and each row's `used-by` cell names the entry path. The tiers fit. But one lead sentence is an unsourced absolute that the cited sources contradict (H1). The section 3 word-order cell is contradicted by the source it cites (H2). Five section 6 cells drop qualifiers or invert scope (M1-M5). The three contested framework points carry no status (M6).

None of the falsifiers listed for claim C in `reports/round-51/claims.json` is triggered by this item. Those falsifiers are the count (227), the README sweep, S-id resolution across the entry, the must-not-cite names, and a register finding. This seat did not run the counters (see Unrun checks).

## Findings

Severity: H = high, M = medium, L = low. Pointers are entry lines unless a file is named.

### H1. Unsourced absolute in the section 6 lead (line 99)

- Text: "...a surface with no spoken analogue."
- No cited row says this. Two cited sources draw spoken-language parallels:
  - S099 section 2 (PMC3688355): "DCs in signed languages (particularly depicting handshapes used within these constructions) do appear to share some characteristics with classifier morphemes in these verbal classifiers (Sandler and Lillo-Martin, 2006; Zwitserlood, 2003), though the extent of similarity is the subject of some debate." The worked example is Imonda verbal classifiers.
  - S098 section 3 (copy): "In sign languages, just as in spoken languages, utterances are organized in chunks that are characterized by intricate patterns of stress, rhythm, and intonation." S098 section 2.3.3: "Sign languages are sometimes claimed to be topic-prominent languages – just like e.g. Chinese."
- Smallest fix: delete "— a surface with no spoken analogue" from line 99.

### H2. Section 3 word-order clause contradicted by the cited source (line 60)

- Text (emerging sign language row): "word order and space conventionalize slowly (S087)".
- S087 (Meir, Sandler, Padden & Aronoff, author manuscript; PDF pages 12-13):
  - p. 12: "ABSL developed an SOV order by its second generation (Sandler et al., 2005)." This is a village language, and the order arrives fast.
  - p. 13: "NSL shows a rapid change in word order." NSL is the row's own example ("NSL since 1977", line 60).
  - p. 13: "Signers of the first two generations of ISL do not show preference for any specific word order. Third generation signers use SOV order more than other orders..."
  - p. 13: "It took ISL three generations to develop a full verb agreement system"; the use of space "was gradual". The space half holds.
- The S087 row's anchor is "pp. 3, 8–9, 15" (SOURCES line 116). That excludes pp. 12-13, and the row's teaches cell does not mention word order. SOURCES is append-only (only status, recheck and used-by change in place), so the anchor cannot be corrected in place.
- Smallest fix: drop "word order and" from line 60 and keep "space conventionalizes gradually (S087 p. 13)". If word order stays, state it per language (ABSL fast, S087 p. 12 with S100; ISL variable across three generations; NSL rapid change, S087 p. 13). Then add a superseding S087 row, whose teaches cell opens "supersedes S087 —", and whose anchor covers pp. 12-13.

### M1. Question scope rule contradicts S098 (line 107, design cell)

- Text: "scope of the marker tracks the constituent, not the sentence".
- S098 section 2.3.2: "In yes/no-questions, it is usually the entire clause that is accompanied by the nonmanual marker." For wh-questions, LIS "the nonmanual accompanies the entire clause", and in ASL "the nonmanual may optionally spread over the entire clause".
- Smallest fix: "question marks usually span the whole clause (S098 section 2.3.2); a headshake spreads from the particle over the VP or predicate (section 2.3.1); a topic mark spans its topic constituent (section 2.3.3)".

### M2. Topic marking shown as separate from brows (line 107)

- Text: "brows mark yes/no questions; topics sit at clause-left with their own marking (S098)".
- S098 section 2.3.3: "The basic marking of topics is raised eyebrows, but since the information structure status of topics can vary, other nonmanuals can be layered with the raised eyebrows." Yes/no questions use the same raised brows (section 2.3.2).
- Smallest fix: "topics sit at clause-left; their basic marker is raised eyebrows, with other nonmanuals layered on (S098 section 2.3.3)".

### M3. "Anywhere" applied to all pronouns (line 103)

- Text: "pronouns may be placed anywhere in it (S098)".
- S098 section 2.3.7: "While the first person pronoun INDEX1 has a fixed location (the signer's chest), the same does not hold for second and third person pronouns, which can be articulated anywhere in the signing space." The person-system claim is contested in the same section: Meier (1990) against the Berenz (2002) and Alibašić Ciciliani & Wilbur (2006) challenge.
- Smallest fix: "second- and third-person pronouns may be placed anywhere in it; INDEX1 has a fixed chest location (S098 section 2.3.7; contested)".

### M4. Headshake claim drops its qualifier and its counterexample (line 106)

- Text: 'headshake is "the most common marker" of negation (S098)'.
- S098 section 2.3.1: "As far as the latter is concerned, the most common marker is a side-to-side headshake (hs)." "The latter" is the nonmanual means. The same section says: "there are still some sign languages where a sentence cannot be negated by a negative headshake alone" (HKSL, example 5; Italian and Jordanian Sign Language, which Zeshan 2006 calls "manual dominant").
- Registry line 37 (B) requires exceptions to be carried.
- Smallest fix: "among nonmanual negators the headshake is most common (S098 section 2.3.1); HKSL, Italian and Jordanian Sign Language need a manual negator".

### M5. ABSL scope and sample dropped (line 108)

- Text: "ABSL shows regular S-O-V within one generation; subject precedes object in all 32 two-noun clauses (S100)".
- The numbers hold. S100 Results: "Where two nouns are mentioned in a clause, subject precedes object (in all 32 cases)"; "the prevalent word order for ABSL sentences is S–O–V".
- The scope does not. SOURCES line 129 scopes S100 to "second generation; not the third-generation studies". The paper's Methods: "In this study, we report only on the language of the second generation. Preliminary results from the third generation, however, reveal interesting differences between the systems of the two generations." The sample is eight second-generation signers (seven deaf, one hearing). Of 158 clauses, 136 are predicate-final. Signer 6 gave 8 of 15 non-predicate-final sentences (Fig. 2 text).
- Registry line 37 (B) requires population, period and exceptions. Section 13 line 209 requires "the count and the counter".
- Smallest fix: "second-generation ABSL (eight signers; S100 Methods) shows a prevalent S-O-V order: subject precedes object in all 32 two-noun clauses (S100 Results); third-generation signers differ (S100 Methods); one signer departs (Fig. 2)".

### M6. Three contested points reported without status (lines 103-108; QUALITY criterion 2; registry line 36)

- Depicting constructions and the "classifier" label. S099 section 1: "Terminology and taxonomy are major factors in the debate." The abstract says "so-called 'classifier' constructions". The SOURCES row S099 teaches: "“classifier” terminology is contested".
- Nonmanual agreement. S098 section 2.3.6 reports Thompson et al. (2006), who "conclude that there is no nonmanual object agreement in plain verbs". The section 6 agreement row (line 104) does not mention nonmanual agreement.
- Pronoun person system. S098 section 2.3.7 (see M3).
- Smallest fix: add one status word to each cell (for example "contested: S099 section 1"), or add three rows to the section 13 calibration bank (lines 197-211).

### M7. S098 row cannot be checked by year, and the copy is a manuscript (SOURCES line 127)

- The row gives author and title but no year, editor, publisher or DOI. It does not say that the URL is an author manuscript. The PDF thanks Diane Brentari "for insightful comments on an earlier version of this chapter", and its PDF creation date is 2008.
- CrossRef record (doi.org, opened 2026-10-22): Roland Pfau and Josep Quer, "Nonmanuals: their grammatical and prosodic roles", Cambridge University Press, published 2012-06-28, DOI 10.1017/cbo9780511712203.018, book chapter. The Cambridge listing gave a print year of 2010 in a search snippet, but the page itself returned HTTP 429, so the print year is unverified.
- QUALITY criterion 1 asks for author plus year, or a stable ID that can be checked. The published chapter was not checked, so its section numbers may differ from the copy's.
- Smallest fix: a superseding S098 row (append-only) with the DOI and year, and a note that the cited copy is an author manuscript. Until then, cite as "(S098, author manuscript; published version not checked)".

### L1. Depicting definition stated as settled (line 105)

- S099 section 2: "The core component of the DC has usually been described as the handshape which identifies the class of the referent." This summarizes prior work. The entry drops "usually been described as".
- Smallest fix: 'usually described as the handshape which identifies the class of the referent (S099 section 2)'.

### L2. Agreement row drops "certain verbs" and uses a label the source does not use (line 104)

- S098 section 2.3.6: "It has long been realized that in most sign languages, the movement and/or orientation parameter of certain verbs can be modulated to express agreement with the subject and the object of the verb." The chapter's terms are "agreement verbs" and "plain verbs". "Indicating verbs" does not appear in S098.
- Smallest fix: "certain verbs ('agreement verbs', S098 section 2.3.6) can be modulated to agree with subject and object".

### L3. "Simplest" is the entry's word, not S100's (line 108, design column)

- S100 Discussion: "In the absence of such mechanisms, word order is the only way to disambiguate a message linguistically." The mechanisms are verb agreement, marking of subject or object, and case.
- Smallest fix: "absent verb agreement or case marking, word order is the only linguistic disambiguator (S100 Discussion)".

### L4. Cross-reference to a section with no classifier content (line 178, section 11 step 4)

- Text: "classifier use (§6)". Section 6 never mentions classifiers. S099 puts "classifier" in quotation marks and calls the term contested.
- Smallest fix: "depicting constructions (§6)".

### L5. ABSL not expanded (line 108)

- The only use of "ABSL" in the entry is line 108. No expansion appears anywhere in the entry (grep).
- Smallest fix: "Al-Sayyid Bedouin Sign Language (ABSL)" at first use.

### L6. Tier A claim carried by the abstract in the anchor (SOURCES line 129)

- "systematic grammar emerges within one generation" is anchored to "Abstract; Results (Fig. 3 discussion)". QUALITY criterion 6 treats abstracts as tier B for substantive claims. The same sentence appears in the Introduction of the PMC text.
- Smallest fix: a superseding S100 row that adds "Introduction", or cite the Introduction for this sentence.

### L7. Design cells lack the H label (lines 103-108, design column)

- Registry line 38 (H): label the designer's choices. Section 11 line 164 says unanchored rows are H. Section 5 marks its design cells "(design rule)". Section 6 does not, so cells such as the scope rule at line 107 (see M1) read as facts.
- Smallest fix: append "(design rule, H)" to each section 6 design cell, following section 5.

### L8. Coverage note (line 104, optional)

- S087 p. 13: ISL needed three generations for a full verb agreement system. Section 3 gives this developmental lag for space, but the agreement row does not give it.
- Smallest fix (optional): add "emerging languages take generations to reach it (S087 p. 13)".

## Checks that passed (tried to break, could not)

- Quotes located in source: S098 "the most common marker is a side-to-side headshake (hs)"; S098 "the first person pronoun INDEX1 has a fixed location"; S099 "identifies the class of the referent"; S100 "subject precedes object (in all 32 cases)"; S100 "In the space of one generation from its inception, systematic grammatical structure has emerged in the language." The entry's paraphrases fail in the qualifiers noted above (M1-M5, L1-L2).
- Counts in S100 (32 two-noun clauses, 158 clauses, 136 predicate-final, eight signers) all appear in the source.
- Registry resolution: S098, S099 and S100 exist in SOURCES (lines 127-129), status "mined", and `used-by` includes the entry path.
- URLs: the S098 PDF, S099 PMC, S100 PMC and S087 PDF all returned HTTP 200 on 2026-10-22. Titles, authors, journals and DOIs match the rows (S099 Lang Commun 32(4):329-348; S100 PNAS 102(7):2661-2665).
- Tier and scope: S099 (tier A, original paper; CC BY 3.0 confirmed) and S100 (tier A, original paper) fit their scope, with the S100 scope caveat in M5. S098 (tier B, survey chapter) fits a survey claim.
- Universal word-order claims: none asserted. Line 108 "do not assert a universal default" and line 120 "there is no universal sign" are cautions. They match `syntax-typology.md:95-101`, which says: "Claims that SOV is 'the human default' draw on emerging sign languages and homesign ... don't assert it flat." S100's own cross-linguistic remark (S–O–V as the most common order, citing Dryer) is not repeated in the entry, which is correct.
- Rulings: no clinical, education-policy or rights ruling in section 6. "rights" (line 213) attributes to WFD and the UN. "policy story" (line 157) is a scope condition, not a ruling.
- Canon: none in section 6. Section 12 is marked NON-CANON.
- Must-not-cite names for claim C: no "corpus/lessons/round-51.md" and no "boundary-count.py" in the entry in any spelling (grep `round-51|lessons/|boundary-count`).
- Terminology: no "deaf-mute" or "hearing-impaired" in section 6.

## Residual risk and gaps

- The published S098 chapter was not checked (Cambridge page returned HTTP 429). Its pagination and section numbers may differ from the copy. I cite the copy's section numbers.
- S087 page numbers come from the author manuscript, not the printed Oxford Handbook.
- Not attacked: sections 1-5 and 7-15, except the section 3 word-order cell (line 60) and the section 11 cross-reference (line 178). Sections 5, 7 and 8 cite other rows (S071-S122) that belong to other seats.
- No `lsp` device is exposed to this seat. The target is Markdown. Grep was used to locate strings; grep output is not semantic proof.

## Unrun checks (outside this seat's assignment; not run)

- `find corpus/knowledge -name '*.md' | wc -l` (expected 227)
- `python3 -B reports/round-28/readme/sweep.py` (expected exit 0, footer total 227, linguistics 26)
- `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json`
- `python3 -B reports/round-51/boundary-count.py` (claim D)

## Commands, outputs and exit codes

| # | Command (summary) | Output (summary) | Exit |
|---|---|---|---|
| 1 | `date -u +%F`; `git -C <lane> rev-parse --short HEAD`; `git -C <lane> status --short \| head -20` | 2026-10-22; 9feb69e; only `?? .ufo/waves/round-51/` (untracked) | 0 |
| 2 | `command -v` for pdftotext, curl, python3, uv, w3m, lynx, jq | present: pdftotext, curl, python3, uv, jq; missing: w3m, lynx (no installs) | 0 |
| 3 | `ls -la` of the falsify directory (listing only; peer files not read) | peer files present; target absent before write | 0 |
| 4 | `curl` S098 PDF into /tmp/r51a3-s06/ | HTTP 200, 351,275 bytes, application/pdf | 0 |
| 5 | `curl` S099 PMC into /tmp | HTTP 200, 221,042 bytes, text/html | 0 |
| 6 | `curl` S100 PMC into /tmp | HTTP 200, 136,684 bytes, text/html | 0 |
| 7 | `file`; `pdftotext -layout` S098; `wc -l`; `pdfinfo` | 1041 text lines; 21 pages; pdfinfo printed a non-fatal "Syntax Error: Expected the default config" on stderr | 0 |
| 8 | `curl` S087 PDF; `pdftotext -layout`; `wc -l`; `pdfinfo` | HTTP 200, 343,100 bytes; 1134 text lines; 22 pages | 0 |
| 9 | py (eval): strip HTML from S099 and S100; phrase search | phrases located as cited above; wrote /tmp/r51a3-s06/S099.txt and S100.txt | completed |
| 10 | py (eval): page map of S087 | word-order passage on pp. 12-13; "Use of space" on p. 13 | completed |
| 11 | grep of the S098 text for quoted phrases | located at sections 2.3.1, 2.3.2, 2.3.3, 2.3.6, 2.3.7 | ok |
| 12 | grep of the S087 text (first try) | "Path not found" because the search raced the download; rerun succeeded | n/a |
| 13 | read DOI 10.1017/CBO9780511712203.018 (CrossRef) | Pfau and Quer; Cambridge University Press; published 2012-06-28 | ok |
| 14 | read Cambridge chapter listing | FAILED: HTTP 429 (rate limited); not retried | error |
| 15 | web search for the Pfau and Quer citation | snippets only (Cambridge "Sign Languages - May 2010"); not opened | ok |
| 16 | grep of the entry and S098 text for `round-51\|lessons/\|boundary-count\|Indicating` | no must-not-cite names; "Indicating" only at line 104 | ok |
| 17 | awk print of entry lines 99-108, 38, 60, 178 | line map confirmed | 0 |
| 18 | `realpath`; `test -e` on target; `realpath -m`; `git status --short -- corpus` | target absent before write; corpus clean (no output) | 0 |
| 19 | grep of the entry for the section 11 lead | line 164 | ok |

## Sources opened (access date 2026-10-22)

| URL | Row | Result | Quote, tier and scope |
|---|---|---|---|
| https://cnlse.es/antiguos/Nonmanuals.their%20grammatical%20and%20prosodic%20roles.pdf | S098 | HTTP 200; application/pdf; 21 pages. Pfau and Quer chapter, author manuscript | Quotes located (sections 2.3.1, 2.3.2, 2.3.3, 2.3.6, 2.3.7). Tier B survey fits "survey". Row lacks year and publisher (M7) |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC3688355/ | S099 | HTTP 200; text/html. Cormier et al. 2012, Lang Commun 32(4):329-348; DOI matches; CC BY 3.0 | Quote in section 2 located, with the "usually described" hedge dropped (L1). Terminology contested (section 1). Tier A fits |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC548320/ | S100 | HTTP 200; text/html. Sandler et al. 2005, PNAS 102(7):2661-2665; DOI matches | "32 cases" and "prevalent word order ... S–O–V" located (Results). "One generation" in Abstract and Introduction. Scope: second generation (Methods). Tier A fits the Results (M5, L6) |
| https://linguistics.stonybrook.edu/faculty/mark.aronoff/files/Emerging%20sign%20languages.pdf | S087 (cross-check for line 60) | HTTP 200; 22 pages; Meir, Sandler, Padden and Aronoff, author manuscript | Word-order passage at pp. 12-13 (H2). Row anchor pp. 3, 8-9, 15 excludes it |
| https://doi.org/10.1017/CBO9780511712203.018 | S098 published record | CrossRef metadata; Pfau and Quer; Cambridge University Press; published 2012-06-28; book chapter; no abstract | Confirms the row lacks year and publisher (M7) |
| https://www.cambridge.org/core/books/sign-languages/nonmanuals-their-grammatical-and-prosodic-roles/74716D24A4601967DC2D057DBF1F8290 | S098 published listing | FAILED: HTTP 429 (rate limited); not retried | Print year 2010 unverified (search snippet only) |

In-corpus anchor read (lane file, not a URL): `corpus/knowledge/linguistics/syntax-typology.md:95-101`.

## Tooling

- Installs or updates: none. Used existing curl (/usr/bin/curl), pdftotext and pdfinfo (poppler, /usr/bin), python3 (/usr/bin/python3), and the read and grep tools. `uv` is present (/home/vgpnk/.local/bin/uv) and was not used.
- Git: read-only only (`rev-parse`, `status`). No add, commit, stash, checkout, reset, pull or push. `git status` may refresh the index stat cache, which is the only side effect. No jj commands were run.
- Scratch: source copies and extracted text are in /tmp/r51a3-s06/, outside the lane. Delete them when no longer needed.
