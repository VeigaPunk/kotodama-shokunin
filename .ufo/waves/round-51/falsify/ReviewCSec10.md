# ReviewCSec10 — falsify attack on claim C, entry section 10

- Seat: KotodamaR51a3.ReviewCSec10 (leaf, read-only on the lane). I wrote only this file.
- Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin (branch main, tip 9feb69e).
- Item attacked: `corpus/knowledge/linguistics/sign-languages-manual-modality.md` section 10, "Contact, codes and writing" (lines 149–160). Also checked: the SOURCES rows it cites (S083, S113, S114, S074, S071, S115, S116, S084, S077), the two in-corpus anchors in its closing paragraph (line 160), and `writing-systems.md:21` (cited at line 158).
- Access date for every URL below: 2026-10-22.
- Judged on: coverage. Every cell in the six section-10 rows was checked against its cited source (table in part 3).

## Verdict: FAILS (section 10, as landed)

Two S083 cells and two S074 cells state things the cited source does not say (QUALITY criterion 1). One S114 cell is supported only by a document the row does not cite. One International Sign restriction is contradicted by the same source and by S077. The S071, S083 and S084 rows carry a wrong term, a tier that is too high, and anchors that miss the cited claim.

Each defect has a text fix or a superseding SOURCES row. The register is append-only, so corrections go in new rows (corpus/SOURCES.md:9–12). With those fixes applied, section 10 should HOLD.

Not attacked: the counts (227 and 26), the D rows, and §§1–9 and 11–15, except the §1 cell at line 26 that repeats the S074 defect.

This is a recommendation for the L1. I made no edits.

## 1. Findings (severity, pointer, smallest fix)

### HIGH

**F1. "initialized signs … as contact traces (S083)"** — entry:154, cell "What it is".
- S083 body (PDF pp. 6–7, https://pure.hw.ac.uk/ws/portalfiles/portal/15283839/AT.pdf) describes initialization as an interpreter's process: a first letter with "usually circular" movement, plus mouthing, "linked to time constraints, especially in TV news settings". The body never says "contact traces". "Contact" appears only in the publisher notice and in reference titles.
- SOURCES row S083 (corpus/SOURCES.md:112) repeats the claim in its "what the source says" column. The row's quote does not carry it.
- Smallest fix: replace the cell with "initialization: first letter with usually circular movement plus mouthing; an interpreter's time-pressure strategy (S083 p.6)". If "contact" is kept, mark it "(to-verify)" and name a source that says it. Correct the S083 row by a superseding row.

**F2. "evidence that signed grammar mirrors spoken word order (S083)"** — entry:154, cell "What it is not".
- S083 has no word-order statement. A text search for "word order", "syntax", "SOV" and "mirror" finds nothing relevant. "Order" appears only in table titles ("Ordered by Frequency") and in "higher-order concepts" (p.24). "Mirror" is used in a frequency sentence about lexicalized fingerspelling.
- Smallest fix: delete the S083 attribution. Word order belongs to syntax-typology.md:99, the entry's own owner, or the claim needs "(to-verify)".

**F3. Signed English word-order and bilingual-education claims cited to S074** — entry:157, cell "arranges a borrowed sign vocabulary in English word order (S074)" and cell "not ASL-English bilingual education (S074)". Also "naturally acquired sign languages" in the same "What it is not" cell. Repeated at entry:26 (§1 table, "a designed code that keeps the spoken word order (S074)").
- The S074 publisher description (https://gupress.gallaudet.edu/Books/T/The-Signed-English-Starter, Description ¶1–¶2, read 2026-10-22) contains none of these. ¶1 has "940 basic signs presented topically". ¶2 has "14 sign markers", "a manual English system", a glossary and exercises. The row's anchor "Description, second paragraph" misses the 940 figure, which is in ¶1.
- SOURCES row S074 (corpus/SOURCES.md:103) also says "a code for English, not ASL". The description does not say that.
- Smallest fix: cut entry:157 to what ¶1–¶2 says. Remove the word-order half of entry:26. Mark any word-order or bilingual-education claim "(to-verify)" until a new S-row with a grammar source supports it. Correct the S074 row with a superseding row.

### MEDIUM

**F4. "a universal sign language or a substitute for a national sign language (S114)"** — entry:156.
- The cited announcement (https://wfdeaf.org/position-paper-on-the-right-of-deaf-people-to-choose-and-access-international-sign-interpretation-services/, read 2026-10-22) has neither "universal" nor "substitute". Its first paragraph says people may choose "between International Sign and national sign languages".
- The support is in the WFD position paper PDF, p.3: IS "cannot replace the primacy of the national sign languages in the lives of deaf people". Body text on p.3 also says WFD "does not support the unification of countries national sign languages". That PDF is linked from the S114 resource page (https://wfdeaf.org/resources/in-drafting-phase-position-paper-on-the-right-to-choose-sign-language-interpretation/, read 2026-10-22). Neither says "universal".
- SOURCES row S114 (corpus/SOURCES.md:143) quotes "IS is an option, not a substitute", which the cited page does not contain.
- Smallest fix: supersede the S114 row, anchored to the PDF p.3, and rewrite the cell to "not a substitute for national sign languages (S114 PDF p.3)". For "not universal", cite S085 (corpus/SOURCES.md:114). I have not re-opened S085; its quote ("There is no universal sign language") comes from the round lesson Gate.

**F5. "shared-stage occasions only (S113)"** — entry:156.
- S113 (https://wfdeaf.org/wp-content/uploads/Perspectives-on-the-Concept-and-Definition-of-IS_Mesch-FINAL.pdf) says "IS is used only for formal and internal meetings" (printed p.11). That is a WFD conclusion, and the cell states it as a design rule.
- The same source reports informal use: "especially in lectures but also informally" (p.10) and "informal communication between the users of national sign languages" (p.11).
- S077 (https://www.un.org/en/observances/sign-languages-day, "What are sign languages?") says IS is used "by deaf people in international meetings and informally when travelling and socializing".
- Smallest fix: attribute and qualify. Write "WFD survey conclusion: formal and internal meetings (S113 p.11); informal and lecture use also reported (S113 p.10–11; S077)".

**F6. "never a home language (S113)"** — entry:156. Canon-adjacent.
- S113 supports only "no native users as a first language" (a respondent's statement, p.5). It does not support a ban on home-language use in any world.
- Entry §2 (entry:50) and §15 (entry:223) hand in-world status to lore. QUALITY criterion 5 bars entries from deciding what is true in any world.
- Smallest fix: "the surveyed respondents report no native users of International Sign (S113 p.5); whether a world's contact register is a home language is lore's call (§2)."

**F7. "fits fairs, federations, pilgrimages"** — entry:155. Unsourced.
- S113 names WFD General Assembly and ICSD meetings and "international meetings and events" (p.4). It does not mention fairs or pilgrimages. A search for "fair" and "pilgrim" in S113 returns nothing.
- Smallest fix: "fits international meetings and events (S113 p.4)". Drop "fairs" and "pilgrimages", or mark them "(H)".

**F8. Unsourced design cells carry no H code; section 10 has no "(to-verify)" mark.**
- Entry:54 says "cells without a citation are lane heuristics (H) or (to-verify)". Entry:153 "pick one family per deaf-community language; reserve fingerspelling for names, new terms, borrowings". Entry:154 "assign them to name, school and newest registers; keep core grammar free of them". Entry:158 "a literate deaf community writes SignWriting; analysts transcribe with HamNoSys". None is cited and none is coded.
- Grep of entry lines 149–160 for "to-verify" returns no hits. The unsupported cells in F1–F3 and F7 are stated as fact, not marked.
- Smallest fix: mark each design-only cell "(H)" (definition at calibration-registry.md:38). Mark any cell that needs a source "(to-verify)" at the cell.

**F9. SignWriting is "writing" in §10 but "not a script type" in §2 and the couples line.**
- Entry:158 says "SignWriting writes sign languages directly (S084)" and "a literate deaf community writes SignWriting".
- Entry:41 (§2) says "signed notation (S084) is transcription of the manual modality, not a script type". Entry:8 (couples) says "fingerspelling and sign notation in §10 are not a script type".
- Smallest fix: pick one term for SignWriting, for example "signed writing system; script-type status open (H)". Align entry:8, :41 and :158.

**F10. S084 tier A on a commercial home page; "directly" is not on the page.**
- SOURCES row S084 (corpus/SOURCES.md:113) is tier A, "maintainer statement, narrow scope". The page (https://www.signwriting.org/, read 2026-10-22) is a sales-and-sites home page. Its meta-description ends "Shop online for books and software". The use claims ("Wikipedias in written sign languages", ASL, Libras and Tunisian Wikipedia links) are substantive claims about the work. QUALITY criterion 6 makes those tier B.
- The page says "Read, write, type all Sign Languages of the Deaf" and "Sign Languages are written languages!". The word "directly" is the lane's addition.
- Smallest fix: supersede the S084 row. Keep tier A only for "SignWriting exists and describes itself as a writing system for sign languages". Mark use claims tier B. In entry:158, drop "directly".

**F11. The writing-systems.md:21 anchor does not support the cell it is cited for.**
- Entry:158, "What it is not": "scripts of a spoken language — they record manual-visual form, not sound (`writing-systems.md:21`)". Line 21 of writing-systems.md is the semasiography row: "meaning direct, not speech … not writing proper". It says nothing about manual form or about sound.
- Smallest fix: drop the cite from this cell, or re-anchor to the typology rows that classify a script by the unit it encodes (writing-systems.md:9–22), and drop "not sound".

**F12. S071 row: wrong term ("signification" for "signation") and an anchor that misses the notation claim.**
- Book text (archive.org full-text OCR, https://archive.org/stream/micro_IA41153455_0834/micro_IA41153455_0834_djvu.txt, read 2026-10-22): "dez, and sig are shortened forms of the terms tabula, designator, and signation" (OCR line 2639); "Signation stands for 'the action of making a sign'" (line 2644). The ERIC abstract says "signation, or sig" (lines 217–221).
- SOURCES row S071 (corpus/SOURCES.md:100) says "signification/action". Entry:16 (§1) says "signification (movement)".
- The row's anchor is the Purposes sentence. That sentence is quoted verbatim and holds (OCR lines 667–670). The notation claim that §10 cites (entry:158) is supported by "Convention of Sign Notation" (book p.40, OCR line 2663), the "tab – dez – sig" notation (lines 2701–2703), and the table of symbols (p.vi and p.68, lines 520, 1949). The row does not carry any of these.
- Smallest fix: supersede the S071 row with the anchor "Convention of Sign Notation, p.40; table of symbols, p.vi/68" and the term "signation". In entry:16, write "signation (movement)".

### LOW

**F13. S083 anchors miss two cited cells; tier and scope overstate a secondhand summary.**
- Entry:153 cites S083 for "produced sequentially" (PDF p.4) and for "ISL" as one-handed (PDF p.16, which cites Cormier et al. 2008). SOURCES row S083 (corpus/SOURCES.md:112) anchors only pp.3 and 6.
- The row's scope, "structure and cross-linguistic variation of manual alphabets", overreaches. The paper studies one speech rendered by 16 interpreters. Its typology is background that cites Battison 1978, Wilcox 1992 and Johnston 2003. Tier A fits the interpreter findings, not the typology.
- Smallest fix: supersede the S083 row. List pp.3–4, 6 and 16. Narrow the scope. Tier B for the typology.

**F14. S113 caveats missing.**
- Entry:155 "most experts surveyed for WFD reject it (S113)". The survey had 24 of 35 respondents from 12 countries (printed p.4). The report says "This is only a survey of the respondents' opinions", and that linguists (Rosenstock 2004, 2005) report different results (p.11). None of that is in the cell.
- Entry:156 "has no native users (S113)". That is a respondent's statement quoted in §3 (p.5), not the report's finding.
- Smallest fix: add the denominator and the caveat. Attribute the no-native-users point to respondents. Keep code C.

**F15. "ISL" and "LIS" are undefined in §10 and "ISL" collides with a WFD term.**
- Entry:153 uses ISL and LIS without expansion. S083 p.3 defines LIS as Italian Sign Language and uses ISL for Irish Sign Language.
- S113 p.4 uses "International Sign Language (ISL)" for the WFD term the report is about.
- Smallest fix: write "Irish Sign Language (ISL)" and "Italian Sign Language (LIS)" at first use in §10.

**F16. "deaf community" in the community-cultural sense.**
- Entry:153 ("deaf-community language") and entry:158 ("a literate deaf community") use lowercase. Entry:147 and entry:168 use "Deaf community" for the same sense. The §13 rule at entry:211 says "capitalise for the community-cultural sense".
- Smallest fix: "Deaf-community" and "a literate Deaf community" in §10.

**F17. "usually circular" dropped; initialization described as a sign class.**
- S083 p.6 says the first letter comes "with a particular movement (usually circular)". Entry:154 drops "usually".
- S083 describes initialization as a process during interpreting. Entry:154 presents "initialized signs" as a class of signs.
- Smallest fix: restore "usually". Describe initialization as an interpreter process (S083 p.6).

**F18. S115: ASL scope missing; anchor drifts.**
- Entry:158 cites S115 for Stokoe's notation without scope. S115 (http://www.cslds.org/apsl-consortium/sign-linguistics/4-sign-phonetics-and-phonolgy-stokoes-notation-symbol/, read 2026-10-22) says Stokoe's notation covers ASL, and that the symbol list "is not meant to cover the possible handshapes, locations and movements found in all sign languages".
- SOURCES row S115 (corpus/SOURCES.md:144) anchors the "building blocks" quote to "the paragraph after the DRIVE (HKSL) example". That sentence is in the paragraph before the DRIVE image. The notation paragraph is after it.
- Smallest fix: add "(for ASL)" in entry:158. Correct the S115 anchor by a superseding row.

**F19. Verification gap: WFD documents and the "community is never A" rule.**
- SOURCES preamble says "`community` is never A" (corpus/SOURCES.md:19). S113 and S114 are WFD documents, typed "docs" and tier A (corpus/SOURCES.md:142–143). WFD is a federation of deaf organizations (S114 PDF, p.10) and represents the international Deaf community's interests (S114 PDF, p.6).
- I did not decide whether WFD documents count as "community" sources. If they do, S113 and S114 cannot be tier A.
- Smallest fix: the L1 decides this and records the decision in a superseding row if needed.

## 2. Held cells and checked anchors (no finding)

- S077 (corpus/SOURCES.md:106). "A pidgin form … limited lexicon" holds. The UN page says "considered a pidgin form" (hedge). The row drops "considered", which does not change §10's use.
- S116 (corpus/SOURCES.md:145). "phonetic", "Stokoe tradition", "version 4", "does not refer to national diversified finger spelling and therefore can be applied internationally" all hold on the page. Tier A holds for the developer's own documentation.
- entry:160 anchors. `adornment-body-codes.md:79` holds: the toolkit bullet names emblems, illustrators and proxemic bands. `syntax-typology.md:99` holds: it contains the SOV-default caveat.
- entry:157 "Only if your world has a deaf-education policy story". This is a conditional design note, not a ruling. No clinical, rights or education-policy ruling was found in §10 beyond F3 and F6.
- Terminology check. "signers" and "sign languages" are used correctly. "deaf-mute", "dumb" and "hearing-impaired" do not appear in §10. "International Sign" is used consistently.

## 3. Cell-by-cell result for section 10 (coverage)

| Line | Cell | Source checked | Result |
|---|---|---|---|
| 153 | conventionalized handshapes represent letters; produced sequentially | S083 p.3 and p.4 | holds (sequential is p.4, outside row anchors; F13) |
| 153 | one-handed (ASL, LIS, ISL) | S083 p.3 (ASL, LIS); p.16 (ISL) | holds; ISL outside anchors (F13, F15) |
| 153 | two-handed BANZSL (BSL, Auslan, NZSL) | S083 p.4 | holds |
| 153 | design: one family per language; reserve fingerspelling for names, new terms, borrowings | none | unsourced, not coded H (F8) |
| 154 | letter-based signs, first letter with circular movement, mouthing | S083 p.6 | holds if "usually" restored (F17) |
| 154 | "as contact traces" | S083 | FAILS (F1) |
| 154 | "evidence that signed grammar mirrors spoken word order" | S083 | FAILS (F2) |
| 154 | design: name, school and newest registers | none | unsourced, not coded H (F8) |
| 155 | improvised signing between signers of different national sign languages | S113 p.5 | holds |
| 155 | "a fixed language" | S113 p.5 | holds (paraphrase) |
| 155 | pidgin label contested; UN page uses it | S077 | holds |
| 155 | most experts surveyed reject it | S113 p.7 | holds; caveats missing (F14) |
| 155 | fits fairs, federations, pilgrimages | none | FAILS (F7) |
| 155 | local, unstable varieties | S113 p.6 | holds |
| 156 | WFD meeting and interpreting register | S113 p.4; S114 | holds |
| 156 | deaf people choose it alongside national sign languages | S114 announcement; PDF p.1 | holds |
| 156 | contact signing, partial conventionalization, no native users | S113 p.5 | holds (respondent statement; F14) |
| 156 | "a universal sign language" | S114 has no "universal"; S085 not re-opened | anchor gap (F4) |
| 156 | "a substitute for a national sign language" | S114 PDF p.3 only | holds in PDF; cited announcement lacks it (F4) |
| 156 | shared-stage occasions only | S113 p.11 conclusion | contradicted in part by S113 p.10–11 and S077 (F5) |
| 156 | never a home language | S113 p.5 | overreach; canon-adjacent (F6) |
| 157 | deliberately designed visual codes | S074 ¶2 ("manual English system") | holds in substance; "deliberately" is a paraphrase |
| 157 | Signed English (14 sign markers) | S074 ¶2 | holds (940 is ¶1; F3) |
| 157 | arranges a borrowed sign vocabulary in English word order | S074 | FAILS (F3) |
| 157 | not ASL-English bilingual education | S074 | FAILS (F3) |
| 157 | naturally acquired sign languages (What it is not) | S074 | FAILS (F3) |
| 157 | only if your world has a deaf-education policy story | none | conditional note; no ruling |
| 158 | Stokoe's notation records handshape, location, movement as parameter values | S115; S071 book p.40, p.vi/68 | holds; S071 row does not carry it (F12, F18) |
| 158 | HamNoSys: phonetic-style, international, not tied to national fingerspelling | S116 ¶1, ¶3 | holds |
| 158 | SignWriting writes sign languages directly | S084 | partial; "directly" not on page; tier (F10) |
| 158 | scripts of a spoken language, record manual-visual form, not sound | writing-systems.md:21 | anchor FAILS (F11) |
| 158 | a literate deaf community writes SignWriting; analysts transcribe with HamNoSys | none | unsourced, not coded H (F8); contradicts entry:41 and :8 (F9) |
| 160 | emblems and proxemics stay at adornment-body-codes.md:79 | in-corpus line 79 | holds |
| 160 | homesign and emerging signs feed syntax-typology.md:99 | in-corpus line 99 | holds |

## 4. Source rows and URLs opened (all 2026-10-22)

| URL | What I found at the stated location | Quote holds | Tier holds | Scope holds |
|---|---|---|---|---|
| https://archive.org/details/micro_IA41153455_0834 (S071 item page) | Stokoe, Sign Language Structure, 1978 revised reprint (ERIC ED 189 878). Links to full text. | yes (see the full text row) | yes (primary) | partly: 1978 revised edition, not the 1960 text |
| https://archive.org/stream/micro_IA41153455_0834/micro_IA41153455_0834_djvu.txt (S071 full text linked from the item page; 5,594 lines, read in part and searched) | Purposes sentence verbatim (lines 667–670). Notation in "Convention of Sign Notation" (p.40), "tab – dez – sig", table of symbols (p.vi, p.68). "Signation", not "signification" (lines 2639, 2644). ERIC abstract (lines 217–229). | yes | yes | partly (term wrong; notation not anchored; F12) |
| https://gupress.gallaudet.edu/Books/T/The-Signed-English-Starter (S074) | Description ¶1: 940 basic signs, topical. ¶2: 14 sign markers, "a manual English system", glossary, exercises. Bios: Gallaudet Signed English Project. | ¶2 quote holds | tier B holds | no: word order, "not ASL", bilingual education absent (F3) |
| https://www.un.org/en/observances/sign-languages-day (S077) | "What are sign languages?": "considered a pidgin form … limited lexicon"; "informally when travelling and socializing" | yes | tier B holds | yes (F5 uses the informal-use line) |
| https://pure.hw.ac.uk/ws/portalfiles/portal/15283839/AT.pdf (S083, PDF, 28 body pages plus refs; read in full, grepped) | p.3 two families, ASL and LIS one-handed; p.4 BANZSL two-handed, fingerspelling sequential; p.6 initialization ("usually circular", mouthing, time constraints); p.16 ISL one-handed (cites Cormier et al. 2008). No word-order statement. "Contact" only in references. | p.3 and p.6 quotes hold | tier A too high for the typology (F13) | partly (F13) |
| https://wfdeaf.org/wp-content/uploads/Perspectives-on-the-Concept-and-Definition-of-IS_Mesch-FINAL.pdf (S113, 337 lines; read in full in part, grepped for the rest) | §2 p.4 (GA and ICSD use; "ISL" term); §3 p.5 ("form of contact signing"; "no native users" as respondent quote); §5 p.7 (most respondents reject pidgin or creole); §8 p.10 ("lectures but also informally"); §9 p.11 ("formal and internal meetings"; informal communication; linguists differ). No "fair" or "pilgrim". | yes | tier A too high for status claims (F14, F19) | partly (F5, F7, F14) |
| https://wfdeaf.org/position-paper-on-the-right-of-deaf-people-to-choose-and-access-international-sign-interpretation-services/ (S114 announcement) | First paragraph: choose "between International Sign and national sign languages"; IS interpreting "unregulated"; "too few qualified interpreters". No "substitute", no "universal". | yes | tier A holds (WFD policy) | yes for policy; no for "substitute" (F4) |
| https://wfdeaf.org/resources/in-drafting-phase-position-paper-on-the-right-to-choose-sign-language-interpretation/ (S114 resource page, linked from the announcement) | Resource page; links the PDF "International Sign version", 24 March 2025. | n/a | n/a | n/a |
| https://wfdeaf.org/wp-content/uploads/Position-Paper-on-the-right-of-deaf-people-to-choose-and-access-International-Sign-interpretation-services.pdf (S114 PDF) | p.1 key points; p.3 IS "cannot replace the primacy of the national sign languages"; p.3 WFD "does not support the unification of countries national sign languages". Says it does not address language rights. | supports the cell's "substitute" claim | tier A holds | yes |
| http://www.cslds.org/apsl-consortium/sign-linguistics/4-sign-phonetics-and-phonolgy-stokoes-notation-symbol/ (S115) | "building blocks" sentence is in the paragraph before the DRIVE image; "Stokoe developed a detailed notation system…" after it; symbol list "not meant to cover … all sign languages" | yes (quote); anchor drift (F18) | tier B holds | partly (ASL scope; F18) |
| https://www.sign-lang.uni-hamburg.de/dgs-korpus/hamnosys-97.html (S116) | ¶1 "phonetic", Stokoe tradition; ¶2 version 4; ¶3 "does not refer to national diversified finger spelling and therefore can be applied internationally" | yes | tier A holds | yes |
| https://www.signwriting.org/ (S084; meta-description and nav read; body grepped, not read in full) | "Read, write, type all Sign Languages of the Deaf. Sign Languages are written languages!"; "Wikipedias in written sign languages"; "Shop online for books and software"; ASL, Libras, Tunisian Wikipedia links | slogan holds | tier A too high for use claims (F10) | partly (F9, F10) |

Not opened: S085, S086 and the rest of the S071–S124 shelf. Named only where the lesson Gate quotes them, flagged as not re-opened.

## 5. Commands and exit codes

1. `_bash` (no cwd set, so the default cwd was the fleet root): `mkdir -p /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-51/falsify && ls -la <that dir> && jj --version 2>/dev/null; git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin log --oneline -5; echo exit=$?`. Exit 0. The directory already existed, so mkdir changed nothing. It holds `swarm-registry.json` (not mine; untouched) and no earlier files of mine. `jj 0.45.1` printed as a version query only; it opens no workspace. The git log tip is 9feb69e, then da31d3c, 35f0d49, 1f97472, 5ab3634.
   - Disclosure: the `jj --version` call ran from the fleet-root cwd. It is a version query and opens no repository, so no snapshot was taken. Recorded here in case the rule is read strictly.
2. `_bash` (cwd set to the lane): `realpath` on `.ufo`, `.ufo/waves`, `.ufo/waves/round-51`, `.ufo/waves/round-51/falsify`, then `ls -la`. Exit 0. All four resolve inside the lane. No symbolic link leads out.
3. Read-only tool calls (all succeeded): `skill://godspeed`; `reports/round-51/claims.json`; the entry in full; `corpus/QUALITY.md`; `corpus/SOURCES.md` lines 1–30 (preamble), 100, 103, 106, 112, 113, 142–145 (raw); `calibration-registry.md:33–40`; `writing-systems.md:9–22` (raw); `adornment-body-codes.md:77–80` (raw); `syntax-typology.md:98–100` (raw); `corpus/lessons/round-51.md` lines 96–112 and Gate grep for S071–S116; grep of the entry for section-10 lines, ISL, LIS, BANZSL, deaf community, signation, to-verify, capitalise, shared-stage, home language, pilgrim, federations, script type, contact trace, word order, mirror; grep of S083 OCR for contact, trace, word order, syntax, SOV, mirror; grep of S071 OCR for purview, primary purpose, signation, notation, table of symbols; grep of S113 for informal, pilgrim, fair, lecture, sports, conference; grep of S084 page for written, countr, Wikipedia, script.

## 6. Checks not run

- `python3 -B reports/round-28/readme/sweep.py`, `find corpus/knowledge -name '*.md' | wc -l`, `python3 -B reports/round-51/boundary-count.py`, `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json`. Not run: they belong to the counts and D items, outside my item.
- `python3 -B tools/gates/provenance-audit.py corpus/knowledge/linguistics/sign-languages-manual-modality.md`. Not run: it is a lane tool that may write, and seats are read-only on the lane. The L1 may run it.
- Not read or used: `reports/round-51/calibration/`, `/fast/scratch/hyaku/kotodama-r51-*`, `/fast/scratch/hyaku/kotodama51-*`. No sandbox clone was needed.

## 7. Installs and updates

None. No package, binary or tool was installed or updated. No pacman transaction was run.

## 8. Residual risk and verification gaps

- S084 body: I read the meta-description and the navigation, and grepped the rest. The homepage body was not read in full.
- S071: I read the first 300 of 5,594 OCR lines, and searched the full text by pattern. The notation chapter text was matched by pattern, not read end to end.
- S113: the appendix (questionnaire) was grepped, not read in full.
- S085 was not re-opened (F4 relies on the lesson Gate quote).
- WFD classification under the "community is never A" rule (F19) is a judgment I did not make.
- Superseding SOURCES rows are needed for F1 (S083 row), F3 (S074 row), F4 (S114 row), F10 (S084 row), F12 (S071 row) and F13 (S083 row). Those rows have not been written. The other fixes are text edits. The fixes are recommendations, and I have not checked whether the rewritten cells hold.
- Re-run the attack after edits, on the changed cells only.
