# ReopenS083: attack on SOURCES rows S083 to S088

Seat: KotodamaR51a3.ReopenS083 (leaf; read-only on the lane). Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin, branch main. Access date for every URL below: 2026-10-22.

## 1. Item attacked

- Rows S083 to S088 in corpus/SOURCES.md (lines 112 to 117).
- Their Gate bullets in corpus/lessons/round-51.md (lines 40 to 45). The Gate URL equals the source-cell URL for all six rows.
- Their used-by target, corpus/knowledge/linguistics/sign-languages-manual-modality.md (the entry).
- Checks: Gate quote verbatim at the stated location; quote at most 25 words; kind; tier under QUALITY criterion 6 and the SOURCES tier definitions; scope; anchor; used-by. No row in this set is queued.
- Downloads went only to /fast/scratch/hyaku/kotodama-r51a3-falsify/ReopenS083 (not a clone; no lane writes; no symbolic links). Installs: none.

## 2. Verdict

**FAILS** as filed, on one row: **S086** (tier and teaches; corpus/SOURCES.md:115).

- All six Gate quotes are verbatim and within 25 words, so the quote check passes everywhere.
- All six used-by cells name the entry, which exists and cites every id.
- S086 fails because its teaches and its Gate grounds drop or contradict the hedges in its own quote, and because its tier A is wrong for an editors' survey. The teaches fault does not depend on the tier judgment.
- S083, S084, S085, S087 and S088 HOLD-WITH-FIXES. Smallest fixes are in section 5.

## 3. Per-row results

| Row | Gate quote(s) found in the opened source | Words | Kind | Tier | Scope and teaches | Anchor | used-by | Row verdict |
|---|---|---|---|---|---|---|---|---|
| S083 | G1 PDF p. 3 (exact); G2 PDF p. 6 (exact) | 25; 24 | paper (accepted manuscript) | A holds for the paper's own interpreter data. Its alphabet-family typology is background that cites Battison 1978 and Wilcox 1992. | Scope overstated (M2). "Contact traces" not in the source (M1). | "p. 3; p. 6" resolves, but the teaches also rely on PDF p. 4 and p. 16 (L1). | Yes: entry lines 41, 153, 154 | HOLDS-WITH-FIXES |
| S084 | Banner "Sign Languages are written languages!" (exact, in the page body, not only the meta block) | 5 | docs (maintainer home page) | A holds for the maintainer's narrow scope | "Used across countries" rests on an unanchored passage (L2) | Banner resolves | Yes: entry lines 41, 158 | HOLDS-WITH-FIXES |
| S085 | G1 "ASL is expressed by movements of the hands and face." (exact, §What is ASL); G2 "There is no universal sign language." (exact, §Is sign language the same) | 10; 6 | docs (NIDCD fact sheet) | A holds for NIDCD's own statement; the linguistic claims are secondary (M3) | The headline "complete, natural language" (24 words, same first paragraph) is not in the Gate (M3) | Three sections resolve | Yes: entry lines 42, 203, 219 | HOLDS-WITH-FIXES |
| S086 | G1 printed p. 2 = PDF p. 11 (exact); G2 printed p. 2 (exact) | 25; 22 | book (editors' Introduction, printed pp. 2 to 26) | **Wrong.** An editors' survey of 17 chapters is B under the register's own definitions ("survey"). H1. | **Teaches overstate the hedged quote** (H2). "By hearing people" unsupported (M8). | "Introduction pp. 2 to 10" resolves (printed pages) | Yes: entry lines 45, 59, 61, 63, 190 | **FAILS** |
| S087 | G1 PDF p. 3 (exact); G2 PDF p. 3 (exact) | 23; 16 | paper (in-press author manuscript) | A holds | Teaches hold; "unrelated signers ... clubs" is on PDF p. 6 (not anchored) | "pp. 3, 8-9, 15" omits p. 6 (L3) | Yes: entry lines 54, 58, 59, 60, 63, 66 | HOLDS-WITH-FIXES |
| S088 | G1 PDF p. 8 (exact); G2 PDF p. 10 (exact) | 21; 22 | paper (author manuscript, Word-generated) | A holds (the author's own claims) | Teaches hold; "since 1817" is the school's 1817 opening (p. 10), not a dated ASL claim | "pp. 8, 10, 12" resolve as PDF pages (L5). Gate pointer "pp. 7, 12" for 1817 is wrong (L4). | Yes: entry lines 58, 60 | HOLDS-WITH-FIXES |

Every quote was checked against the page text. S086 was checked twice: in the reader text, and on a decoded glyph layer (see section 7, commands 24 and 28).

## 4. Findings

Severity: High = a claim is wrong or a rule breaks, and an entry relies on it. Medium = a scope or attribution error that must be fixed before the claim stands. Low = anchor, pointer or labelling defect.

### High

**H1. S086 is filed as tier A for an editors' survey.** corpus/SOURCES.md:115.
- The SOURCES tier definitions put "survey" and "textbook" under B, and reserve A for primary or authoritative sources (original paper, official docs, maintainer statement). QUALITY criterion 6 says the same.
- The Introduction is written by the two editors. It summarises the chapters and states class-level generalisations ("All known village sign languages are endangered..."; PDF p. 11). Being expert does not make it a primary source.
- Smallest fix: add a superseding row (teaches opens "supersedes S086 —", next free id), tier B, scope limited to the editors' class-level statements. Keep S086 at A only for facts about its own chapters.

**H2. S086 teaches and Gate grounds overstate the hedged source; the teaches contradicts the Gate's own quote.** corpus/SOURCES.md:115; corpus/lessons/round-51.md:43.
- Teaches: "all documented village sign languages are endangered by urban-sign pressure." The Gate quote says "All known village sign languages are endangered, **usually** because of pressure from larger urban sign languages" (printed p. 2, PDF p. 11). Also on PDF p. 16 (printed p. 7): "Apart from changing marital patterns, language contact ... appears to be **a major risk factor**."
- Teaches: "village sign languages arise from high (often hereditary) deafness and are shared between deaf and hearing members." The source says "In **most cases**, these signing communities have emerged ..." and "these indigenous sign languages are **typically** shared ..." (printed p. 2, PDF p. 11).
- Gate grounds (round-51.md:43): "endangerment-by-contact is universal across the documented cases." Not in the source. The source says "usually".
- Downstream: entry line 59 says "endangered by urban contact (S086)", with no "usually".
- Smallest fix: write the hedges into the teaches ("usually because of...", "in most cases", "typically"). Replace "universal" in the grounds with the source's own words. Entry line 59 becomes "usually endangered by urban contact (S086 p. 2)".

**H3. The entry cites S083 for a claim S083 does not make.** corpus/knowledge/linguistics/sign-languages-manual-modality.md:154: "evidence that signed grammar mirrors spoken word order (S083)".
- The S083 text has no word-order discussion. "word order" has no hits in the 37-page extraction. "mirror" appears once, on PDF p. 18, about how often lexicalized fingerspelling occurs.
- This is a provenance defect under QUALITY criterion 1.
- Smallest fix: delete "(S083)" from that cell. If the claim stays, cite a source that states it (word-order typology is owned by syntax-typology.md:99).

### Medium

**M1. S083 teaches gloss "contact traces" is not in the source.** corpus/SOURCES.md:112.
- PDF p. 6 gives the source's own account: initialization is an interpreter strategy "linked to time constraints, especially in TV news settings (Kellett Bidoli and Sala 2011)."
- "Contact" appears in the body text of S083 nowhere except reference titles (PDF pp. 29, 31, 32; also the cover page, p. 1).
- Entry line 154 repeats "as contact traces (S083)".
- Smallest fix: row teaches becomes "interpreters' initialization (first letter with a circular movement) plus simultaneous mouthing, linked in the source to time pressure (p. 6)." Entry line 154 becomes "as interpreter strategies under time pressure (S083 p. 6)".

**M2. S083 scope is wider than the paper's own work.** corpus/SOURCES.md:112 ("structure and cross-linguistic variation of manual alphabets").
- The paper's own work is counts of interpreter fingerspelling for one speech, 16 interpreters, described by the authors as a "small-scale, exploratory study" (PDF p. 2, abstract).
- The two-family statement (PDF p. 3) is background. The next sentence cites Battison 1978 and Wilcox 1992.
- Smallest fix: scope becomes "fingerspelling production by interpreters in one speech (own data); alphabet families as background (p. 3)."

**M3. S085 headline claim is not in the Gate; tier scope is not stated.** corpus/SOURCES.md:114; corpus/lessons/round-51.md:42.
- The row teaches "ASL as a complete natural language." The Gate quotes do not carry that claim.
- The page does say it: "American Sign Language (ASL) is a complete, natural language that has the same linguistic properties as spoken languages, with grammar that differs from English." (24 words; §What is ASL, first paragraph.)
- Tier A is defensible only as NIDCD's own statement ("official docs"). The linguistic status is secondary.
- Smallest fix: add that sentence to the Gate; scope the row to "NIDCD's public statement (NIH Pub. 11-4756, March 2019; page last updated 2021-10-29)."

**M4. Entry overstates S087.** entry line 59: "everyone acquires from birth, within and between families (S087)."
- S087 PDF p. 4: "many children, both hearing and deaf, acquire the language from birth, or very early in life."
- Smallest fix: "many children, hearing and deaf, acquire it from birth or very early (S087 p. 4)."

**M5. Entry cites S086 for a sentence that is in S087.** entry line 59: "shared context allows less explicit structure ... (S086)."
- The "less explicit" sentence is S087 PDF p. 3 ("This degree of familiarity may allow them to be less explicit verbally..."). S086 contains no such sentence.
- Smallest fix: cite S087 p. 3.

**M6. Entry cites S088 for a claim S088 does not make.** entry line 60: "mostly peer-to-peer, seeded by homesign (S088)."
- S088 PDF p. 11 mentions home signs only for one pupil who entered in 1817 (John Brewster). It then asks a question about how home-sign systems later merged into ASL. It does not say emerging languages are seeded by homesign.
- The seeding claim is in S087 PDF pp. 6 to 7: "Others may have grown up using sign communication only within the family, that is, homesign."
- Smallest fix: cite S087 pp. 6 to 7.

**M7. Entry cites S084 for a typology claim S084 does not make.** entry line 41: "signed notation (S084) is transcription of the manual modality, not a script type."
- S084 supports "read, write, and type all Sign Languages" and "now used to write over 40 sign languages around the world" (page body). It says nothing about script typology.
- Smallest fix: delete "(S084)" from that clause. Entry line 158 ("SignWriting writes sign languages directly (S084)") is supported and stays.

**M8. S086 teaches restricts alternate signing to hearing people.** corpus/SOURCES.md:115 ("alternate sign languages are used by hearing people under speech taboos").
- The source (printed p. 3, PDF p. 12) says: "alternate sign languages are used in situations of speech taboos, for instance during mourning, or during hunting (Kendon 1988)." No hearing-only restriction.
- Printed p. 6 (PDF p. 15) says the Yolngu alternate sign "has also been adopted by a small group of deaf individuals."
- Smallest fix: drop "by hearing people." Cite Kendon 1988 as the source's own citation.

### Low

**L1. S083 anchor and pagination base.** corpus/SOURCES.md:112.
- Teaches use PDF p. 4 (two-handed BSL, Auslan, NZSL; "fingerspelling occurs sequentially") and PDF p. 16 ("ISL is a one-handed system"). Neither is anchored.
- Pages are PDF pages of the Heriot-Watt accepted manuscript ("Peer reviewed version"), not journal pages 143 to 171.
- Smallest fix: anchor "pp. 3, 4, 6, 16"; write "accepted manuscript, PDF pp."

**L2. S084 teaches passage is not anchored.** corpus/SOURCES.md:113. "Used across countries and sign languages" rests on the page-body sentence "now used to write over 40 sign languages around the world." The banner does not say it. Smallest fix: add that passage to the anchor and the Gate.

**L3. S087 anchor misses p. 6.** corpus/SOURCES.md:116. "Unrelated signers of different backgrounds come together" and "deaf associations and clubs" are on PDF p. 6; the anchor "pp. 3, 8 to 9, 15" omits it. Pages are PDF pages of the in-press manuscript. Printed Handbook pages are pp. 267 to 280 (search summary only; not opened). Smallest fix: anchor "pp. 3, 6, 8 to 9, 15" and name the pagination base.

**L4. S088 Gate page pointer is wrong.** corpus/lessons/round-51.md:45 ("ASL ... since 1817 (same PDF, pp. 7, 12)"). "1817" is on PDF pp. 10 to 12 and not on p. 7 (text search). The 250,000 figure is on p. 12, which is correct. Smallest fix: "pp. 10, 12"; teaches "since 1817" becomes "school opened 1817 (p. 10)."

**L5. S088 pagination base.** corpus/SOURCES.md:117. The anchors "pp. 8, 10, 12" are PDF pages of the author manuscript. The extracted text has no printed page numbers. The published chapter is in *Deaf around the World* at pp. 19 to 37 (publisher preview contents: "1 Sign Language Geography, 19"). Smallest fix: "author manuscript, PDF pp. 8, 10, 12 (book pp. 19 to 37)."

**L6. S088 year.** corpus/SOURCES.md:117. "OUP 2011" matches the book's copyright page ("Copyright © 2011 by Oxford University Press, Inc."). The publisher's chapter page returned HTTP 403 to the reader. A search summary reports a November 2010 date. S086 cites "(Padden 2010)" (PDF p. 12). Smallest fix: write "OUP 2011 (copyright); some references give 2010" so entry citations match one edition.

**L7. Entry range "3 to 6 generations" is cited to S087.** entry line 59. S087 gives no range: "third generation" (PDF p. 10) and "five generations" for Al-Sayyid (PDF p. 5). The range matches S086 Table 1 (PDF pp. 13 to 14: Chican three, Mardin four, Kata Kolok five, Alipur at least six). Smallest fix: cite S086 Table 1.

**L8. Entry "impractical" is cited to S086.** entry line 61 ("where speech is taboo or impractical ... (S086)"). "Impractical" is in the S109 abstract, not S086. Smallest fix: cite S109 for that word, or drop it.

**L9. Entry "thousands" has no source.** entry line 58 ("thousands to about 250,000 primary signers ... (S088)"). S088 gives "around 250,000" and no lower bound. Smallest fix: drop the lower bound or source it.

**L10. Emerging-sign definition is Padden's.** corpus/SOURCES.md:115. S086 (PDF p. 12) attributes "emerging sign language" to "(Padden 2010)". The primary is S088 (PDF p. 8). Smallest fix: cite S088 for the definition.

## 5. Smallest fix set that would move the item to HOLDS

1. Superseding row for S086 at tier B, with hedged teaches; remove "universal" from its grounds (H1, H2, M8, L10).
2. Entry line 154: delete "(S083)" from the word-order cell; rewrite the "contact traces" gloss (H3, M1).
3. S083: narrow the scope; anchor PDF p. 4 and p. 16 (M2, L1).
4. S085: add the complete-natural-language sentence to the Gate; state the tier scope (M3).
5. Entry line 59: "everyone" becomes "many" (M4); "less explicit" cites S087 p. 3 (M5); "3 to 6 generations" cites S086 Table 1 (L7); "usually" added to the urban-contact claim (H2).
6. Entry line 60: homesign seeding cites S087 pp. 6 to 7 (M6).
7. Entry line 41: delete "(S084)" from the script-type clause (M7).
8. S084: anchor the body passage (L2). S087: anchor p. 6 (L3). S088: fix the Gate page for 1817 and the pagination base (L4, L5, L6).
9. Entry line 61: "impractical" cites S109 or is dropped (L8). Entry line 58: drop "thousands" (L9).

## 6. Coverage of the entry cells checked

I checked every entry cell that cites S083 to S088 (lines 41, 42, 45, 54, 58 to 61, 63, 66, 153, 154, 158, 190, 203, 219), against the source text. Entry lines 155 and 156 cite only S077, S113 and S114, which are outside this item, and were not checked.

## 7. Commands run

Exit codes are from the shell where a shell ran. Tool results (read, grep, web_search, eval cells) report "ok" when they returned without an error or traceback.

| # | Command or tool call | Result, exit |
|---|---|---|
| 1 | read ~/.omp/agent/RULES.md | ok; tooling directive only; no install done |
| 2 | grep S08[3-8] corpus/SOURCES.md | ok; rows at lines 112 to 117 (also 111, 118, 188 context) |
| 3 | read reports/round-51/claims.json | ok; claims D and C; must_not_cite lists read |
| 4 | read corpus/lessons/round-51.md | ok; Gate bullets for S083 to S088 at lines 40 to 45 |
| 5 | read corpus/QUALITY.md | ok; criteria 1 to 8 (criterion 6 at line 29) |
| 6 | read corpus/SOURCES.md:1-40:raw | ok; tier definitions (A, B, C; community never A) |
| 7 | read corpus/SOURCES.md:112-117:raw | ok; six rows |
| 8 | read corpus/lessons/round-51.md:40-45:raw | ok |
| 9 | read corpus/knowledge/verification/calibration-registry.md:35-39 | ok; codes R, C, B, H, T |
| 10 | read S083 PDF URL | ok; accepted manuscript; 37 pages |
| 11 | read https://www.signwriting.org/ | ok; metadata block only (body checked in command 21) |
| 12 | read NIDCD ASL page | ok |
| 13 | read S086 PDF URL | ok; 423 PDF pages |
| 14 | read S087 PDF URL | ok; 22 pages |
| 15 | read S088 PDF URL | ok; 31 pages |
| 16 | bash: mkdir -p scratch; command -v curl pdftotext pdfinfo python3 qpdf mutool; python3 import checks | exit 0 (last command was echo). curl, pdftotext, pdfinfo, python3, qpdf present. mutool, pypdf and fitz absent (not installed; not needed) |
| 17 | eval py: curl -sS -L --max-time 90 for the six URLs | exit 0 for each; HTTP 200 (sizes and sha256 in section 8) |
| 18 | grep S08[3-8] in the entry | ok; lines 41, 42, 45, 54, 58 to 61, 63, 66, 153, 154, 158, 190, 203, 219 |
| 19 | web_search: Padden chapter year | ok; snippets only; not opened |
| 20 | eval py: pdftotext quote checks (PDF) | no traceback. S083 p. 3 and p. 6 exact; S087 p. 3 twice exact; S088 pp. 8, 10, 12 exact; S086 no hit (glyph-shifted text layer; see 24 and 28) |
| 21 | eval py: HTML checks, S084 and S085 | no traceback. S084 banner in body; S085 both quotes found once; S085 headings found |
| 22 | read entry lines 1 to 30 | ok; header and couples line |
| 23 | read entry lines 148 to 158 | ok; §10 table (columns: what it is, what it is not, design consequence) |
| 24 | eval py: pdftotext -f 11 -l 11 on S086 | no traceback. Output is glyph-shifted: "7KLV\x03ERRN" decodes to "This book" |
| 25 | eval py: S083 word-order and contact search | no traceback. "word order": none. "contact": PDF pp. 1, 29, 31, 32 only. "mirror": p. 18 only |
| 26 | eval py: S085 headline sentence | no traceback. Count 1 |
| 27 | eval py: S087 and S088 entry-claim checks | no traceback. "many children ..." S087 p. 4; homesign S087 pp. 3, 7, 9; "1817" S088 pp. 10 to 12, not p. 7; "home signs" S088 p. 11; "250,000" S088 p. 12 |
| 28 | eval py: S086 decoded glyph layer (two runs; code +29 for codes 0x03 to 0x5F, spaces kept) | no traceback. G1, G2 and "In most cases" on PDF p. 11; "major risk factor" p. 16; "alternate ... speech taboos" and "emerging ... two or three generations" p. 12; "(Padden 2010)" p. 12; "Kendon 1988" p. 12; "adopted by a small group" p. 15; Table 1 p. 13; IS contact pidgin p. 19 |
| 29 | eval py: S084 body check | no traceback. "now used to write over 40 sign languages around the world" in the body |
| 30 | read https://academic.oup.com/book/34430/chapter/292168189 | **reader error: HTTP 403** ("Failed to fetch URL"); not read |
| 31 | read https://global.oup.com/academic/product/deaf-around-the-world-9780199732548?type=510 | ok; navigation text only in lines 1 to 423 of 1411; no publication-date block reached |
| 32 | read pageplace preview PDF | ok; copyright 2011; ISBN 978-0-19-973254-8; contents place chapter 1 at p. 19 |
| 33 | read artifact of the OUP product page, lines 299 to 423 | ok; navigation only |
| 34 | web_search: Meir et al. 2010 publication details | ok; snippet gives 2010, pp. 267 to 280; not opened |
| 35 | eval py: "less explicit" search | no traceback. S087 p. 3 only; S086 none |
| 36 | bash: ls, sha256sum, pdfinfo in the scratch directory | exit 0 |
| 37 | bash: test -d, realpath -m, git status --porcelain (read-only) on .ufo/waves/round-51/falsify | exit 0. Real directory, not a link. Untracked files are other seats'. I changed nothing in the lane |

## 8. URLs opened (access date 2026-10-22)

Gate URL and source-cell URL are identical for all six rows.

1. https://pure.hw.ac.uk/ws/portalfiles/portal/15283839/AT.pdf. HTTP 200; 524,796 bytes; sha256 9758ab48544d6622c5876a11d27b8e9d1d14f41df95fce61dd2dd0c5f2dc9ff2. Accepted manuscript of Sign Language Studies 17(2):143 to 171 (DOI 10.1353/sls.2017.0000). Quotes on PDF pp. 3 and 6 confirmed.
2. https://www.signwriting.org/. HTTP 200; 425,114 bytes; sha256 71141c047b7aafd6415878b25a2e2f629361ff63194d5d6bba3bd784afebf576. Banner and masthead confirmed in the body.
3. https://www.nidcd.nih.gov/health/american-sign-language. HTTP 200; 48,668 bytes; sha256 a62507e0a356db47248909f70bc2ae6fc342722b2360a3631940cefa1168444c. Three sections and both quotes confirmed.
4. https://pure.uvt.nl/ws/portalfiles/portal/100130712/Zeshan_deVos_Eds._2012.pdf. HTTP 200; 18,159,342 bytes; sha256 6afe508a1889dc760d748ad79f8e7fe3d4c9f0ecf895fc07e4a68befa966b9b8. Publisher's PDF (version of record). Introduction printed pp. 2 to 26; quotes confirmed on PDF pp. 11, 12, 16, 19.
5. https://linguistics.stonybrook.edu/faculty/mark.aronoff/files/Emerging%20sign%20languages.pdf. HTTP 200; 343,100 bytes; sha256 de14d0eb625d66105789354f648a268cd5667a1eca341197de1d028aca7511cd. In-press author manuscript; 22 pages; quotes confirmed on p. 3.
6. https://pages.ucsd.edu/~cpadden/files/Padden%20SL%20Geography.pdf. HTTP 200; 216,232 bytes; sha256 df19fa687569d1f0ef5161ad43963272a09cf07d1069cabb2a8e805c80876daa. Word-generated manuscript ("Padden SL Geography 22409.doc", created 2009-09-28); 31 pages; quotes confirmed on pp. 8, 10, 12.
7. https://academic.oup.com/book/34430/chapter/292168189. **Failed: HTTP 403** through the reader. Not read.
8. https://global.oup.com/academic/product/deaf-around-the-world-9780199732548?type=510. Opened; navigation text in the part read; no publication date reached.
9. https://api.pageplace.de/preview/DT0400.9780199780884_A24395425/preview-9780199780884_A24395425.pdf. Publisher preview on a distributor host. Copyright 2011; contents place chapter 1 at p. 19.

Search results only, not opened: Oxford Academic chapter summary (Nov 2010 date); Meir et al. 2010 record (pp. 267 to 280).

## 9. Unrun checks and residual risk

- **Unrun (outside this item):** `python3 -B reports/round-28/readme/sweep.py`; `find corpus/knowledge -name '*.md' | wc -l`; `python3 -B reports/round-51/boundary-count.py`; `tools/gates/provenance-audit.py` on the entry; the separability checker and claims-agree check. These belong to the C and D seats. I ran none of them.
- **Access gap:** the OUP chapter page returned HTTP 403, so the S088 year discrepancy rests on the copyright page alone. The Meir et al. 2010 page range rests on a search summary.
- **Paragraph numbers:** Gate labels such as "p. 3 ¶3" and "p. 8 ¶2" cannot be checked on the extracted layout. I checked each quote by page.
- **S086 text layer:** the PDF uses a shifted glyph encoding. I checked its quotes in the reader text and on a decoded layer (code +29 for codes 0x03 to 0x5F, checked on samples), and both agree.
- **Live page:** S084 is a live page. Its wording may change; the 90-day recheck applies.
- **Tier judgement:** H1 is a tier judgement (an expert survey is B under the register's own definitions). H2 does not depend on it: the teaches contradicts the Gate's own quote.
- **Author-lane attack.** This is an attack report from a leaf seat. It is not an admission on the lane's merge.
