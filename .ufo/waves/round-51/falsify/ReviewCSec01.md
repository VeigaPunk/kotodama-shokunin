# ReviewCSec01: falsify pass on claim C, entry section 1, and rows S071-S076

- **Seat:** KotodamaR51a3.ReviewCSec01 (leaf reviewer; read-only on the lane; no subagents, no background jobs).
- **Lane:** /home/vgpnk/Projects/shokunin/kotodama-shokunin (branch main). Claim base bff83ba. C landed at da31d3c; records at 9feb69e.
- **Access date for every URL below:** 2026-10-22.
- **Item attacked:** `corpus/knowledge/linguistics/sign-languages-manual-modality.md`, section 1 "The register property" (lines 14-29). That is the master claim (line 16), the four choices (lines 18-21), the test table (lines 23-27), and the iconicity and terminology sentence (line 29). I also checked whether registry rows S071-S076 (`corpus/SOURCES.md` lines 100-105) support what section 1 cites.

## Verdict: HOLDS-WITH-FIXES

- The registry leg holds. All six rows exist, each names the entry path in its `used-by` cell, and each was opened on 2026-10-22.
- The sourcing does not hold as written. Four load-bearing cells cite a row that does not say the cited thing: the two halves of the master claim (F1), the word-order cell in test row 2 (F2), and the transmission cell in choice 3 (F3). Three cells are contradicted or overstated by their own source (F6, F7, F8). One publisher-description row carries substantive claims and could not be checked (F11). None of this needs new research. Each cell needs re-citation, narrowing, calibration, or a "(to-verify)" mark.
- As landed, section 1 does not meet QUALITY criterion 1 (provenance) or criterion 6 (claim-scoped source authority). The claim's declared falsifiers in `reports/round-51/claims.json` test counts, the sweep, registry presence, and owner restatement. None of them tests whether a cited row supports its cell. So this defect passes the declared falsifiers. The L1 should add a cell-level support check to the declaration.
- Must-not-cite check for C: a grep of the entry for `round-51`, `lessons/`, `boundary-count` and `reports/round-51` returned no matches.

## 1. Commands run

Bash commands. Each one read files or wrote only to scratch. Nothing was written to the lane.

| # | Command (abridged) | Output | Exit |
|---|---|---|---|
| 1 | `git log --oneline -5`; `wc -l` on SOURCES.md, the entry, and round-51.md; `ls` of `.ufo/waves/round-51/` and its `falsify/` folder | Commits 9feb69e, da31d3c, 35f0d49, 1f97472, 5ab3634. Line counts 251, 223, 111. The `falsify/` folder exists. | 0 |
| 2 | `command -v` for pdftotext, pdftoppm, mutool, qpdf; Python imports of pypdf, fitz, pdfminer; `mkdir -p /fast/scratch/hyaku/kotodama-r51a3-falsify/ReviewCSec01` | pdftotext, pdftoppm and qpdf are in /usr/bin. pypdf, fitz and pdfminer are not installed and were not needed. Scratch folder created. | 0 |
| 3 | `curl -sSfL` of the 1960 Stokoe PDF into scratch; `pdftotext -layout` into scratch | curl exit 0, 22,561,312 bytes. pdftotext exit 0, 2,269 text lines, 41-page PDF. | 0, 0 |
| 4 | `pdftotext -v`; `curl -V`; `realpath` and `ls -la` of the `falsify/` folder | pdftotext 26.08.0. curl 8.23.0. The folder resolves inside the lane, with no symlink. My report file did not exist before this write. | 0, 0, 0, 0 |
| 5 | Grep of the entry for `round-51\|lessons/\|boundary-count\|reports/round-51` | No matches. | no match |

Read, grep and eval calls. These were read-only. They covered the entry, SOURCES.md rows S071-S076, round-51.md (Gate lines 28-33), QUALITY.md, claims.json, writing-systems.md:11, adornment-body-codes.md:79, calibration-registry.md:35-39, RULES.md, the saved full texts of the 1978 Stokoe reprint, the PMC article, the Glottolog pages and the 1960 PDF text. One eval call located PDF pages in the 1960 text. Line numbers in section 4 refer to the reader text of the saved sources, so they can be re-checked.

Installs: none. I read RULES.md first. The tools I used (curl and poppler's pdftotext) were already installed, and their versions are recorded above.

## 2. Sources opened (accessed 2026-10-22)

| Row | URL | What is at the anchor | Quote holds? | Tier and scope hold? |
|---|---|---|---|---|
| S071 | https://archive.org/details/micro_IA41153455_0834 | Catalogue page for the ERIC microfiche of the 1978 Linstok reprint. | n/a | n/a |
| S071 | https://archive.org/stream/micro_IA41153455_0834/micro_IA41153455_0834_djvu.txt | Full text of the 1978 reprint. Page numbers come from footers. Purposes quote at lines 667-669. Abstract at lines 219-221. OCR is imperfect in places. | Yes. The purview quote holds. | Tier A holds. "No post-1960 data" does not (F16). |
| S071 | https://www.joshiesworld.com/wp-content/uploads/2025/10/stokoe_1960.pdf (the Gate's second URL; not registered in SOURCES) | The 1960 Occasional Paper 8 copy, 41 PDF pages. Checked: PDF p.5 purview; p.16 "ultimately deriving from the French"; p.18 "tertiary symbol system"; p.21 "Like consonant and vowel ... motion" and "Tabula, designator, and signation"; p.30 "does not argue a simple subordination". | The Gate's "motion" quote holds for this copy. The registered reprint says "action" (F14). | This is an unregistered third-party copy (F14). |
| S072 | https://doi.org/10.1515/9783110261325 | Crossref record: title "Sign Language", publisher De Gruyter, published 2012-08-16, type edited book. Abstract field: "No abstract available." | The quoted publisher sentence was not found. | n/a |
| S072 | https://www.degruyterbrill.com/document/doi/10.1515/9783110261325/html (and https://www.degruyter.com/document/doi/10.1515/9783110261325/html, which redirected to the same page) | Bot-check page: "Let's confirm you are human ... Complete the security check before continuing." | Not checkable. | n/a |
| S072 | https://books.google.com/books?vid=ISBN9783110261325 (redirected to books.google.com.br) | Volume metadata: Pfau, Steinbach and Woll; Walter de Gruyter, 2012; ISBN 9783110261325. The description shown is the German series preface. | Not found. | n/a |
| S073 | https://glottolog.org/resource/languoid/id/sign1238 | Heading "Pseudo Family: Sign Language". The classification tree is collapsed in the text. | The heading holds. | The tier-A "genealogical classification" scope does not hold (F3). |
| S073 | https://glottolog.org/resource/languoid/id/sign1238.json | `"category": "Pseudo Family"`. The newick tree includes Auxiliary Sign Systems, with Australian Aborigines Sign Language and its child languoids; also L1 Sign Language, International Sign and Pidgin Sign Language. Nothing about children, mother tongues or transmission. | The auxiliary-children claim holds. | n/a |
| S073 | https://glottolog.org/glottolog/glottologinformation | Classification principles. "Non-genealogical trees" include Sign Language. "Sign languages are classified on a weaker theoretical basis." L1 sign languages "are or were someone's mother tongue." Homesign systems are "not full-fledged languages." | This page supports a different, correct claim (F3). | The row's scope should say non-genealogical catalogue (F3). |
| S074 | https://gupress.gallaudet.edu/Books/T/The-Signed-English-Starter | Publisher description. "940 basic signs presented topically"; "14 sign markers"; "discussion of the unique features of a manual English system"; glossary; exercises. Bornstein is a former director of the Gallaudet Signed English Project. | The Gate quote holds (Description, paragraph 2). | Tier B for contents holds. Tier B does not carry the word-order claim (F2). |
| S075 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4821822/ | Goldin-Meadow and Brentari, Behavioral and Brain Sciences 40:e46. This is the NIHPA author manuscript: online 2015 Oct 5, issue 2017 Jan. I read the full text: abstract, introduction, sections 1-8. | The abstract quote holds. | Tier A holds for research history. "Discredited" and "without grammar" are not in the text (F12, F19). |
| S076 | https://nad.org/knowledge-hub/american-sign-language/community-and-culture-frequently-asked-questions/ | Q&A text. "'Hearing-impaired' was a well-meaning term that is not accepted or used by many deaf and hard of hearing people." "This term is no longer accepted by most in the community." "Deaf-mute" and "deaf and dumb" are called offensive. "When in doubt, ask the individual how they identify themselves." | The quote holds. | Tier A holds for US term preference. A universal "never" does not (F15). |

## 3. Cell-by-cell check of section 1

| Cell (entry line) | Cited row(s) | Supported? | Finding |
|---|---|---|---|
| Master claim: "is acquired natively by deaf children of signing communities" (16) | S071; S072 | No. S071 says most deaf signers did not have deaf signing parents (p.88). S072 has no acquisition statement. S075 §3 supports it, but the entry does not cite S075 here. | F1 |
| Master claim: "does not derive from any spoken language" (16) | S071; S072 | Not as worded. S071 describes borrowing and initialized signs, so the claim needs a scope. | F1 |
| "Stokoe's 1960 analysis first brought ..." (16) | S071 | The quote holds. "First" rests on the author's own preface. "Showed" is "argued" in S075 §2. | F13 |
| "signification (movement)" (16) | S071 | No. Stokoe's term is "signation (sig)". | F4 |
| "as phonemes compose words" (16) | S071 | Supported. Stokoe draws the analogy with segmental phonemes (PDF p.21). The categorical status of motion and location is contested (S075 §4.2, §7.3). | F9 |
| Choice 1, articulators carry the load (18) | none | Uncited. The source the entry leans on says modality does influence structure. | F6 |
| Choice 1, "not the grammar's depth" (18) | none | Contradicted by S075 intro paragraph 3. | F6 |
| Choice 2, duality (19) | S071; S072 | S071 supports the aspect analogy. S072 is unverified. | F11 |
| Choice 3, transmission to children (20) | S071; S073 | Not in S073. S071 does not discuss village or mixed communities. | F3 |
| Choice 4, "fail the test" for codes (21) | S071 | Supported: methodical signs are a separate system. | none |
| Choice 4, "never translated" (21) | S071 | Not in S071. S071 suspects spoken syntax influenced sign syntax. | F7 |
| Test row 1: emblem repertoire (25) | adornment-body-codes.md:79 | Owner correct. Line 79 says emblems have dictionary meanings. The pass column is uncited. | F17 |
| Test row 2: "keeps the spoken word order" (26) | S074 | Not in S074. The pass criterion conflicts with §3 and §4. | F2, F10 |
| Test row 3: "a secondary notation" (27) | writing-systems.md:11 | Line 11 does not say it. S071 p.30 does. | F5 |
| Line 29: iconicity | S075 | Supported (§1). | none |
| Line 29: simultaneity and spatial grammar | S075 | Simultaneity appears only as a difference from speech. Spatial grammar is contested in S075. | F8 |
| Line 29: "never 'deaf-mute' or 'hearing-impaired'" | S076 | Supported for US usage. A universal "never" overreaches. | F15 |
| Line 29: "never the reverse" (H) | none | Labelled H, which is the right label. S075 §7.2 describes the reverse pathway. | F18 |

## 4. Findings

Severity scale. HIGH: a cited claim is not in its cited source, or the source says the opposite. MEDIUM: a calibration, scope or anchor error where the substance survives. LOW: wording, provenance hygiene or citation detail.

### HIGH

**F1. The master claim cites S071 and S072 for two claims that neither row carries** (entry line 16; SOURCES.md:100-101).
- *Acquisition.* S071 (1978 reprint, p.88, reader lines 4603-4608) says that deaf signers "are not automatically competent native signers if only because most of them did not have deaf signing parents." That is a caveat, not support. S072 gives no acquisition statement in any text I could open (F11). The entry's own §4 (line 76) says most Deaf children learn sign only after entering school. The support that does exist is S075 §3, in the introduction paragraphs to the section: Supalla's "acquisition data on deaf children acquiring ASL from their deaf parents."
- *Derivation.* Neither row says "does not derive from any spoken language." S071 records borrowing. Toward the latter two kinds (conventional and methodical signs), the language of signs "seems to have behaved as other languages behave toward borrowings" (p.19). Initialized signs "may have a French origin" (reader lines 3930-3933). The 1960 copy says "does not argue a simple subordination of the one language to the other" (PDF p.30). The defensible claim is in S071 at reader lines 1276-1278: a natural sign language "differs in phonology, morphology, syntax, and semantics from a natural spoken language."
- **Smallest fix.** (a) Split line 16. Say that grammar and phonology are not derived from a spoken language (S071 lines 1276-1278; S075 §3). Say that the lexicon borrows through initialization and fingerspelling (S071 p.19 and lines 3930-3933; S075 §3, Battison paragraph). (b) For acquisition, cite S075 §3 and add the S071 p.88 caveat. Use "from signing adults or peers" (see F10). (c) Remove S072 from line 16 until its description is opened (F11).

**F2. Test row 2 and line 157 cite S074 for word order that S074 does not state** (entry lines 26 and 157; SOURCES.md:103).
- Line 26 reads "a designed code that keeps the spoken word order (S074)." The publisher description I opened lists 940 basic signs, 14 sign markers, "discussion of the unique features of a manual English system", a glossary and exercises. It says nothing about word order. The row's teaches cell adds "deliberately designed" and "a code for English, not ASL." Neither phrase is on the page.
- Line 157 repeats the claim: Signed English "arranges a borrowed sign vocabulary in English word order (S074)."
- S071's English-word-order passages describe signing in English word order during simultaneous communication (p.83, reader lines 4330-4340), and a "greater or less similarity to English syntax" across signing levels (reader lines 4535-4539). Neither describes a designed code. S075 §4.3 says the order of monastic silent signs "follows the word order in the monks' spoken language." That is a point about alternate silent systems. It cannot move to line 26 without changing the category.
- **Smallest fix.** Delete "that keeps the spoken word order" from line 26 and the word-order clause from line 157, or mark it "(to-verify)". If the monastic point stays, cite S075 §4.3 and say it concerns alternate systems. Correct the S074 teaches cell by a superseding row.

**F3. Choice 3 cites S073 for transmission to children. S073 does not say that, and its scope is wrong** (entry line 20; SOURCES.md:102).
- The Glottolog node lists child languoids under "Pseudo Family." It does not mention children, mother tongues or transmission.
- The row's scope says "genealogical classification" at tier A. Glottolog's information page lists "Sign Language" among the "non-genealogical trees" and says sign languages "are classified on a weaker theoretical basis." The same page gives the principle the entry needs: L1 sign languages "are or were someone's mother tongue."
- **Smallest fix.** For choice 3, cite the Glottolog information page in a new row. Re-scope S073 by a superseding row to "Glottolog's non-genealogical catalogue of sign languages." Tier A then covers what Glottolog catalogues, not genealogy or transmission. For the village and mixed-community part, cite S086 and S087, which are already in SOURCES and are not cited in section 1.

### MEDIUM

**F4. Terminology: "signification (movement)" misnames Stokoe's third aspect. The designator gloss drops "attitude"** (entry line 16; S071 teaches cell, SOURCES.md:100).
- Stokoe's term is "signation (sig)." PDF p.21: "Tabula, designator, and signation may be easily shortened to tab, dez, and sig." The reprint abstract (reader lines 219-221) gives "handshape and attitude (designator, or dez)" and "the action of the sign (siqnation, or sig)", where "siqnation" is an OCR error for "signation." The entry's own line 83 uses "tab/dez/sig." The S071 teaches cell repeats "signification/action."
- **Smallest fix.** Use "tabula (location), designator (handshape and attitude), signation (sig; movement or action)." Correct the S071 teaches cell by a new row whose teaches opens "supersedes S071 —", as the SOURCES header requires. Do not edit the row in place.

**F5. Test row 3 cites writing-systems.md:11 for "a secondary notation." That line does not say it** (entry line 27).
- writing-systems.md:11 is Daniels' framing: "classify a script by which linguistic unit one basic sign encodes." The word "secondary" does not appear in that file. S071 does say it: "writing is a secondary symbol system, and fingerspelling one step further, a tertiary system for English transmission, not itself a sign language" (reprint p.30, reader lines 2070-2072; PDF p.18 has the 1960 "tertiary symbol system").
- **Smallest fix.** Cite S071 p.30 for the secondary-notation point. Keep writing-systems.md:11 only for "a script encodes a linguistic unit."

**F6. Choice 1 states as settled that the channel does not change "the grammar's depth." It is uncited, and the paper the entry leans on says otherwise** (entry line 18).
- S075 introduction paragraph 3: "Researchers are discovering that modality does influence the structure of language." The articulator clause has no citation. S071 supports it (reader lines 2568-2570: "One of the other features is clearly facial expression"). S098 §2.3 also supports it.
- **Smallest fix.** Cite S071 and S098 for the articulator clause. Either delete "not the grammar's depth" or mark it contested (C, calibration-registry.md:36), citing S075 introduction paragraph 3 and §7.3.

**F7. Choice 4 says grammar is "never translated." S071 does not say "never," and it suspects the reverse for syntax** (entry line 21).
- S071 p.20 (reader lines 1129-1133): the influence of French and English "through the medium of methodical signing ... affected the syntax of the sign language actually in use by the deaf may be suspected." That is Stokoe's hypothesis, not a finding.
- S071 does support "the meta-language of the methodical signs was a different system" (reader lines 1107-1111 and 1123-1128) and the difference in phonology, morphology, syntax and semantics (lines 1276-1278).
- **Smallest fix.** "A sign language's own grammar is not a transcription of a spoken language. Manual codes that map spoken grammar are a separate meta-language (S071 p.20). Spoken-language influence on sign syntax through methodical signing is suspected, not shown (S071 p.20; C)." Drop "never."

**F8. Line 29 presents spatial grammar as a settled resource. The cited paper treats it as contested** (entry line 29; S075).
- S075 §1 supports iconicity: "We therefore do not take the presence of iconicity in a system as an indicator that the system is not a language."
- Simultaneity appears in S075 §2 only as a difference from speech, citing Stokoe. It is not presented as a resource.
- Spatial grammar: S075 §4.2 says Liddell's analysis "makes them more gestural than linguistic." §7.3 says the categorical status of motion and location is open, and finds no evidence that place of articulation is categorical.
- **Smallest fix.** Keep the iconicity claim, citing S075 §1-2. Mark spatial agreement C, citing S075 §4.2 and §7.3. Drop "simultaneity" from the list, or cite S071 reader lines 2552-2553 (simultaneous, not sequential, production) as a difference.

**F9. No calibration status on the master claim or on the aspect inventory** (entry line 16; QUALITY criterion 2; calibration-registry.md:35-39).
- S075 §7.3: "It is generally accepted that handshape, motion, and location constitute the three parameters." The same section says the categorical status of motion and location is open. The master claim states all three as phonemic-like, with no status.
- **Smallest fix.** Add "(B for the inventory; C for whether motion and location are categorical; S075 §4.2 and §7.3)."

**F10. Test row 2's pass criterion "from signing adults" contradicts the entry's own §3 and §4** (entry line 26).
- §3 line 60: emerging sign languages are "mostly peer-to-peer, seeded by homesign (S088)." §4 line 76: "most Deaf children learn their sign language only after entering school." Under line 26 both fail "natively acquired." Line 16 still calls them native.
- **Smallest fix.** Redefine the pass criterion as "acquired in early childhood in a signing community, from adults or peers." Cite S075 §3 and S071 p.88 for the minority route.

**F11. S072 is a tier-B publisher description. Its quoted sentence could not be checked, and the master claim uses it for substantive claims** (entry lines 16 and 19; SOURCES.md:101; QUALITY criterion 6).
- De Gruyter returned a bot-check page. Crossref says "No abstract available." Google Books shows a German series preface, not the sentence. The teaches cell lists a toolkit ("typology, grammar, psycholinguistics, neurolinguistics, sociolinguistics, documentation and transcription") that the quoted sentence does not contain. A programme statement cannot carry acquisition or derivation (F1).
- **Smallest fix.** Mark S072 unverified (status queued). Remove it from lines 16 and 19, or open an unblocked copy and quote the exact sentence.

**F12. The S075 teaches cell says "discredited." The paper does not say it, and the misconceptions table uses it for an R code** (SOURCES.md:104; entry line 204; outside section 1).
- A full-text search of the paper finds no "discredited." Introduction paragraph 2 presents pantomime as stage (1) of a pendulum. The abstract says the pendulum "is currently swinging back toward the view that sign is gestural, or at least has gestural components."
- Line 204 reads "Sign is pantomime or gesture: R." R means "rejected/discredited as the specified general inference" (calibration-registry.md:35). That is too strong for the gestural-components half, which the paper calls open.
- **Smallest fix.** Teaches cell: "stage (1) of the research history: pantomime or a language of gestures." Line 204: "superseded first stage (R for pure pantomime); whether sign has gestural components is C (S075 abstract)." Pass this to the owner of the misconceptions table.

### LOW

**F13. "First brought" and "showed"** (entry line 16).
- The priority claim rests on the author's own preface in the 1978 reprint: "the first linguistic treatment of the language" (reader line 331). The cover says "The First Linguistic Analysis." The Gate quote does not show it. S075 §2 says Stokoe "argued," not "showed."
- **Smallest fix.** "Stokoe's 1960 monograph (its 1978 reprint calls itself the first linguistic analysis) argued that ..."

**F14. The S071 Gate quote and the registered URL do not match** (SOURCES.md:100; round-51.md Gate line 28).
- The Gate's "...position, configuration, and motion..." is accurate to the 1960 copy (PDF p.21). The registered reprint says "action" in the same sentence (reader lines 2594-2595). The Gate cites a second URL that the row does not register.
- **Smallest fix.** Register the edition used in a superseding row, with its page numbers.

**F15. S076 scope drift at line 29.** NAD is a US association.
- NAD's own rule is "When in doubt, ask the individual how they identify themselves." The entry omits that rule and omits "deaf and dumb," which NAD calls offensive. It turns a US position into a universal "never." This is a usage norm, not a clinical, education-policy or rights ruling.
- **Smallest fix.** "NAD (US) advises against 'deaf-mute', 'deaf and dumb' and 'hearing-impaired'; ask the individual (S076)."

**F16. The S071 scope "no post-1960 data" is wrong for the 1978 reprint** (SOURCES.md:100).
- The reprint contains bracketed later additions, for example "research reported since 1976 by Bellugi, Pedersen, Newport, and Supalla" (about reader lines 2073-2077).
- **Smallest fix.** Scope cell: "1960 monograph; 1978 reprint with bracketed editorial additions," in the superseding row.

**F17. Pass columns for test rows 1 to 3 are uncited** (entry lines 25-27).
- "Productive grammar" and "primary medium" are factual claims. S075 §3.2 (reduplication as a derivational rule) supports the first.
- **Smallest fix.** Cite S075 §3.2 for row 1. Mark row 3's pass criterion "(to-verify)" or cite it.

**F18. "Never the reverse" (line 29, H) has the right label, but it should note S075 §7.2.** S075 §7.2 says "It is likely that all conventional sign languages ... have their roots in homesign ... and perhaps also in the co-speech gestures." That is the reverse pathway, offered as a hypothesis. **Smallest fix.** "Design rule (H). S075 §7.2 documents the reverse pathway as a hypothesis."

**F19. S075 citation details** (SOURCES.md:104).
- The PMC record gives online 2015 Oct 5 and issue 2017 Jan. The row's "(2017)" is the issue year. The PMC copy is the NIHPA author manuscript. The "without grammar" gloss on emblems is not in the paper, which says emblems "have standards of form" (§6). **Smallest fix.** "(2015 online; 2017 issue)." Delete "without grammar."

## 5. Test table and owners

- **Row 1 (emblems).** The owner is correct. adornment-body-codes.md:79 covers emblems "with dictionary meanings" (checked).
- **Row 2 (manual codes).** The owner column names a source (S074), not an owner. The owner for manual codes is this entry's §10, at line 157. The word-order claim fails (F2). The pass criterion conflicts with §3 and §4 (F10).
- **Row 3 (writing).** The owner anchor, writing-systems.md:11, does not carry the claim (F5).

## 6. Canon, clinical, education-policy and rights rulings

- **Canon decisions.** None in section 1. Lines 16-29 are method. The canon handoff is in §2 and the closing paragraph.
- **Clinical rulings.** None in section 1.
- **Education-policy rulings.** None in section 1. Line 157 is outside section 1, and it fails on word order (F2).
- **Rights rulings.** None in section 1. The terminology rule on line 29 is a usage norm (F15).
- **Abstract-only and publisher-description rows carrying substantive claims (criterion 6).** S072 (F11) and S074 (F2). S075's Gate quote is the abstract, but its row anchors full sections, and I checked those sections.

## 7. Residual risk and verification gaps

- **Not run in this seat** (outside section 1, or not needed for it): `find corpus/knowledge -name '*.md' | wc -l` (expected 227); `python3 -B reports/round-28/readme/sweep.py` (expected exit 0, footer 227 and linguistics 26); the separability checker; the provenance-audit tool; and the README row check.
- **S072 publisher description: not verified** (blocked). F11 stands whatever its text says, because the master claim uses a programme statement for substantive claims.
- **Page numbers.** The reprint's page numbers come from footers. One running head is OCR-garbled ("10 Sign Language Theory" on what I count as p.20). The 1960 page numbers are PDF page numbers from the scanned copy.
- **OCR.** Quotes from the reprint were checked against the 1960 copy where OCR was poor.
- **Not reviewed:** S077-S124, and sections 2-12 of the entry, except where section 1 relies on S073-S076.
