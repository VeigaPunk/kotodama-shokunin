# Falsify report: claim C, section 12 (NON-CANON worked micro-example)

- Seat: KotodamaR51a3.ReviewCSec12 (leaf; read-only on the lane; no subagents, no background jobs; this file is the only write).
- Date: 2026-10-22. Axis: coverage. Round 51, attempt 3, falsify wave.
- Item attacked: `corpus/knowledge/linguistics/sign-languages-manual-modality.md`, section 12, lines 188–195, as landed at commit `da31d3c`. The commit blob and the working-tree file have the same sha256 (`1a71ae2dcf2ecacbbd23884b5b4894aaf18879dbde23e9ed32067f018c52b1f7`). Lane HEAD is `9feb69e`.
- **Verdict: FAILS as landed.** Every defect is a local edit to section 12 or to one SOURCES row. None touches claim C's declared counters, which this seat did not run.
- Attack report: a recommendation, not an admission.

## Summary

1. **High.** "Hearing women" is keyed to S081, which does not carry it. The entry's own section 9 marks the same detail `(to-verify)`.
2. **Medium.** "Walking the §11 decision table" overstates the walk. DR-SGN-02 is not walked, several §11 build steps and row checks are missing, the table shows no §6 or §10 content, and no control is on record.
3. **Medium.** S117 is tier A on an abstract-only anchor. QUALITY criterion 6 says abstracts are tier B. The lane gave S080 tier B for the same kind of anchor.
4. **Medium.** The `politeness-taboo-euphemism.md:118` anchor is an invented sea-folk example with no NON-CANON mark. It describes no mourning ban.
5. **Medium.** The village "loci" walk leaves out the counter-evidence that the entry's own sources give.
6. **Medium.** "Two kindreds" is keyed to S086, which does not say it. The support is S087 p.10, which is outside the row's pinned pages.
7. **Medium (records).** The round lesson says the Wikipedia-carried claims were re-cited to primary rows, with "alternate signing → S081" as the example. That is not true of this claim.
8. **Low.** S115 locator error; S086 tier for a secondary sentence; calibration-registry path; terminology; social-field dial; S081 metadata.

Held: the NON-CANON label; the shared and hereditary village definitions (S086 p.2); the mourning and speech-taboo sentence (S086 p.3, a secondary report of Kendon 1988); the village-typology claim (S087 p.3–4); the S087 year 2010 (CrossRef); the Stokoe parameters (S115); and the fingerspelling concept (S117, full text).

## Findings

### R12-1 · HIGH · "Hearing women" is keyed to S081, which does not carry it
- Where: `E:190` "a separate mourning alternate sign used by hearing women (S081)". `E:139` flags the same detail as "bereaved women `(to-verify)`". The same S081 key also sits at `E:40` and `E:135`, for speech-ban claims.
- Opened source: S081 is the Google Books description (`SRC:110` anchor). It says this was the first book-length study of sign language as "a means of communication among Australian Aborigines", based on nine years of fieldwork, and that it analyses sign-language structure. It does not mention mourning, speech taboo, alternate signing, or women.
- Origin: the "widows and women" wording came from the tier-C Wikipedia Warlpiri page (`.ufo/waves/round-51/build/ScribeSec12Example.md:32`). That seat wrote that the mourning-ban half needed a peer-reviewed primary before it could carry weight (`…ScribeSec12Example.md:60`).
- What does carry the mourning sentence: S086 p.3 (PDF p.12): "alternate sign languages are used in situations of speech taboos, for instance during mourning, or during hunting (Kendon 1988)." The entry already keys this to S086 at `E:61`. `E:40`, `E:135`, `E:139` and `E:190` key it to S081 instead. No source opened here says "women".
- Either reading fails. If "hearing women" is a real-world attribution, S081 cannot carry it. If it is a design choice, it should carry an H label and no source key.
- Mitigation: the paragraph carries the NON-CANON label (see Held).
- Smallest fix: delete "used by hearing women", or mark it `(to-verify)` as `E:139` does. Key the mourning and speech-taboo clause to S086 p.3. Re-key `E:40` and `E:135` the same way (outside section 12, same defect).

### R12-2 · MEDIUM · "Walking the §11 decision table" overstates what is walked
- Where: `E:190`; §11 is at `E:162–186`.
- Walked: row 3 (village type, `E:170`) and row 4 (mourning alternate, `E:171`), at type level only. DR-SGN-01 (community type first).
- Not walked:
  - DR-SGN-02 (set the iconicity budget before coining signs, `E:184`). No iconicity setting appears.
  - §11 build steps 1–5 (`E:175–179`) each name an artifact: signer map, iconicity dial, manual-parameter chart, spatial-grammar sketch, notation sample and contact rules. None is produced. Step 4 is an H assertion only.
  - Row checks: S100 (row 3, `E:170`), `conlang-methodology.md:36` (row 4, `E:171`), `writing-systems.md:20-21` (row 6, `E:173`). None appears.
  - §3: only the community column is set. Transmission, size and time depth, and design consequence are not (`E:59`).
  - §4: one of six conditions (`E:74–79`), keyed to S086 rather than §4's own rows.
  - §5: no minimal-pair check (`E:95` requires one). No palm orientation, nonmanual or two-handed status (`E:90–92`).
  - DR-SGN-03 and DR-SGN-04: partly walked.
- Lane standard: `corpus/knowledge/verification/worked-example-verification.md` (WEV). This paragraph is a class (b) invented micro-example (`WEV:25`; obligations at `WEV:51`).
  - Derive fails. No DR id is cited. "Two kindreds", "hearing women" and "role markers at loci" hang on no rule id (`WEV:74`, F1). The table cells are asserted values, not outputs of any named rule (`WEV:78`, F5).
  - Reject fails. No forbidden input appears in the prose. No §12 receipt turned up in the entry, the build seat report (`ScribeSec12Example.md:57–61`: "no counter or sweep was re-run"), or the lesson. For class (b), "none on record = finding" (`WEV:51`; DR-WE-04 at `WEV:101`).
- Smallest fix: either narrow `E:190` to what is walked (rows 3 and 4, DR-SGN-01), or add the DR-SGN ids to each walked item, add one iconicity sentence (DR-SGN-02), add one rejected counterexample (for example, "a homesign imposed on a village" as a DR-SGN-01 failure), and add a one-line receipt.

### R12-3 · MEDIUM · S117 is tier A on an abstract-only anchor
- Where: `SRC:146` (tier A; anchor "Abstract"; scope "(open-access full text)"); `E:190` "(S117)".
- Rule: `corpus/QUALITY.md:29` (criterion 6): abstracts are tier B for substantive claims. The lane applied this to S080 (`SRC:109`, tier B on an abstract; `LES:88`). S117 is the same kind of row and was kept at A.
- Opened: the PMC full text. The claim is in §1 Introduction, paragraph 1: "Fingerspelling is a manual representation of orthographic code and is one of the main ways in which Deaf and Hard of Hearing people engage in translanguaging." The SRC quote column merges two abstract sentences without quotation marks. It is not a verbatim quote.
- Smallest fix: a superseding S117 row (criterion 6 forbids an in-place tier edit) anchored to the full text, §1 ¶1, with the verbatim sentence. Tier A is defensible on that anchor. Otherwise tier B.

### R12-4 · MEDIUM · The `politeness-taboo-euphemism.md:118` anchor is an invented example and does not carry mourning substitutes
- Where: `E:190` "substitutes follow `politeness-taboo-euphemism.md:118`".
- Opened: `PTE:118` begins "Worked micro-example: a sea-folk culture." It describes a divine-name taboo, an occupational ban on land-animal words aboard ships ("hay-biter" for the mule), a court's verb grading, and a ministry's renaming of conscription. Its only death-related line is a dating remark ("death-ladder rung its funeral rolls use"). It does not describe a mourning speech ban.
- The file contains no "NON-CANON" string. "Canon" appears only at `PTE:37` and `PTE:135` (grep). `WEV:25` lists `PTE:118` as a class (b) exemplar, and class (b) needs the NON-CANON mark in the paragraph itself (`WEV:51`; F4 at `WEV:77`). So the anchor cannot evidence a real-world pattern.
- The entry's own section 9 keys the same ban mechanics to `PTE:75` (names of the dead) and `PTE:77` ("replaced and preserved as a citation-form") at `E:139`. Section 12 should do the same.
- Smallest fix: key the speech-ban and substitute clause to `PTE:75` and `PTE:77`, and drop `:118`. Tell the politeness file's owner that `:118` lacks the NON-CANON mark (outside this seat).

### R12-5 · MEDIUM · The village "loci" walk leaves out the counter-evidence the entry's sources give
- Where: `E:190` "§6 grammar in space — role markers placed at spatial loci (H …)"; `E:194` "village shared sign language — §3, §5, §6"; `E:103` (loci row; no village caveat).
- Opened, S086 pp.10–11 (PDF pp.19–20; Table 2 on p.11): Adamorobe Sign Language has directional verbs (YES) and no whole-entity classifiers. Kata Kolok has no directional verbs (NO), and "KK signers do not establish conceptual referent locations (known as 'loci') in signing space" (p.11).
- Opened, S087 p.15: "Village sign languages do not seem to have these spatially based grammatical systems."
- The attested village pattern is topographic pointing: S087 p.13 (ABSL signers point to the real-world location of houses); S086 p.11 (KK signers point to the actual location of a person's home).
- The GRAIN and RIVER-DROP cells list chin and chest. They show no loci, agreement or classifiers, so the table does not show a §6 walk.
- Smallest fix: either use topographic pointing (S087 p.13) for this village, or label the loci choice as a departure from the documented village pattern and cite S086 p.11 and S087 p.15. Drop "§6" from the GRAIN row unless a locus or agreement form appears.

### R12-6 · MEDIUM · "Congenital deafness concentrated in two kindreds (S086)" is keyed to a source that does not say it
- Where: `E:190`; `SRC:116` (S087 pinned pages are 3, 8–9 and 15).
- Opened: S086 p.2 says "a high incidence of (often hereditary) deafness". It does not mention kindreds or "congenital". "Congenital" traces to the tier-C Wikipedia lead (`ScribeSec12Example.md:31`).
- The support is S087 p.10: "Deafness may be restricted to one or two families within the community, as in the case of Amami Sign Language." That page is not pinned. S087 p.4, which supports "both deaf and hearing members" in the same sentence, is not pinned either.
- The term "congenital" is not wrong in general: S087 p.4's footnote uses it for US incidence. It is wrong as a key to S086.
- Smallest fix: if the two kindreds are a design choice, label them H with no source key. If they are a real-world pattern, key them to S087 p.10 and add p.4 and p.10 to the S087 locator (or supersede the row). Use "hereditary", the keyed source's own word.

### R12-7 · LOW · S115 locator error; ASL-only caveat missing
- Where: `SRC:144` ("paragraph after the DRIVE (HKSL) example"); `LES:72` and `ScribeSec12Example.md:45` repeat it.
- Opened (CUHK Module 4): "In other words, the handshape, location and movement are the building blocks of a signed word" comes before the DRIVE image. "Stokoe developed a detailed notation system to capture the possible values of each of these three phonological parameters" comes after it. The module also says its symbol list "is not meant to cover the possible handshapes, locations and movements found in all sign languages."
- `E:190` says "recorded in Stokoe-style parameter rows". The table holds English labels, not Stokoe symbols.
- Smallest fix: change the locator to "paragraphs before and after the DRIVE (HKSL) example". Change `E:190` to "parameter rows in Stokoe's three-parameter frame (S115)".

### R12-8 · LOW · Script caveat missing; §10 has no payload in the table
- `E:190` says "a fingerspelled alphabet from the valley's script (S117)". S117 §2.1 says that where the community uses a nonalphabetic written language, fingerspelling "is somewhat different" (Japanese Sign Language spells surnames with kanji-based signs; Chinese Sign Language uses pinyin handshapes). The example does not say the valley's script is alphabetic.
- The §10 payload (a fingerspelled alphabet) does not appear in the table. MOURN (`E:195`) carries no §10 content either.
- Smallest fix: state that the script is alphabetic, or cite the S117 caveat. Add a fingerspelling row, or drop "§10" from the MOURN row.

### R12-9 · LOW · S086 tier applies to a secondary sentence; locator omits p.11
- `SRC:115` is tier A, and its scope includes "alternate sign languages." The mourning sentence (p.3) reports Kendon (1988), so for that sentence the tier is B. Kendon is not open to this seat (see Verification gaps). The row's pages 2–10 also exclude p.11, which carries the Table 2 used in R12-5.
- Smallest fix: scope the tier A to the village-definition claims. Add p.11 to the locator.

### R12-10 · LOW · Calibration-registry anchor does not resolve from this folder
- `E:190` "`calibration-registry.md:38`". The file is `corpus/knowledge/verification/calibration-registry.md` (glob). From `linguistics/` the bare name resolves to nothing. Line 38 is the H row (checked). The bare form also appears at `E:145` and `E:164`.
- Smallest fix: `../verification/calibration-registry.md:38`.

### R12-11 · LOW · Terminology and parameter precision
- "flat-B palm" folds palm orientation into the handshape cell. §5 lists orientation as its own parameter (`E:90`). Fix: a separate column, or "palm facing X".
- "A separate mourning alternate sign" is singular and names one lexical item (MOURN). §9 says "alternate system", and §11 says "alternate or manual code with a limited lexicon" (`E:171`). Fix: "a one-sign mourning alternate (MOURN)".
- "Role markers" is not a §6 term. §6 uses referential loci and indicating verbs (`E:103–104`).

### R12-12 · LOW · Social field not modelled
- `E:190` "used by deaf and hearing residents alike." §13 says the village's social field must be modelled and stigma is a variable (`E:207`). §4's Attitudes dial (`E:78`) is unset. Fix: set the dial and mark it H or C, or drop "alike".

### R12-13 · MEDIUM (records) · The round lesson records a re-citation that did not happen
- `LES:85`: "every claim they carried was re-cited to a primary row (for example homesign → S079 and S089, village sign → S086, alternate signing → S081, …)". For R12-1, S081 carries neither alternate signing nor mourning. `LES:72` repeats the S115 locator error (R12-7).
- Fix: the lesson's owner corrects the record. This seat did not edit it.

### R12-14 · LOW · S081 row wording
- `SRC:110` says "2013 pb ed." The page says "reimpressão" (reprint), Cambridge University Press, 2013, 562 pp. It never says paperback. The row's "alternate sign languages" is the row's own gloss, not the page's wording.
- Fix: copy the page's words.

## Held (checked; no finding)
- NON-CANON label, verbatim, at `E:190` (WEV class (b) label leg).
- Section references §3, §4, §5, §6, §9 and §10 exist, and their titles match the walk.
- S086 p.2 (PDF p.11): "these indigenous sign languages are typically shared between deaf and hearing community members", and "a high incidence of (often hereditary) deafness." Holds.
- S086 p.3 (PDF p.12): the mourning and speech-taboo sentence. Holds, as a secondary report of Kendon 1988 (R12-9).
- S087 p.3 (village and deaf-community types) and p.4 ("characteristically used by both deaf and hearing members of the community"). Both hold. p.4 is outside the pinned pages (R12-6).
- S087 year 2010. CrossRef DOI `10.1093/oxfordhb/9780195390032.013.0018` gives "Published: 2010-06-28". The build draft said 2012; the landed row is right.
- S115 three parameters (tab, dez, sig). Holds.
- S117 concept (fingerspelling as a manual representation of orthographic code). Holds on the full text. R12-3 concerns tier and anchor only.
- The entry text names neither `corpus/lessons/round-51.md` nor `reports/round-51/boundary-count.py` (grep). The must-not-cite list holds for the whole entry.
- No clinical, education-policy or rights ruling in section 12. The one clinical-register word ("congenital") is R12-6.
- "Varn" appears only in the entry and in the build seat's draft. "Varner" (`naming-systems.md:28, :100`) is a different real author. No corpus collision. Not checked against the world bible, which belongs to lore and is outside the lane.

## Smallest fix set (for a re-attack)
1. `E:190`: delete "used by hearing women", or mark it `(to-verify)`. Key the mourning and speech-taboo clause to S086 p.3. Re-key `E:40`, `E:135` and `E:139` the same way.
2. `E:190`: narrow "Walking the §11 decision table", or add DR-SGN ids, an iconicity sentence, one rejected counterexample, and a receipt line.
3. `SRC`: superseding S117 row anchored to full text, §1 ¶1, with tier per criterion 6.
4. `E:190`: replace `:118` with `:75` and `:77`.
5. `E:190`: "two kindreds" either H with no key, or S087 p.10 with p.4 and p.10 added to the locator. "Congenital" becomes "hereditary".
6. `E:190` and `E:194`: village loci either shown as topographic pointing, or labelled as a departure with S086 p.11 and S087 p.15 cited. Drop "§6" from GRAIN unless shown.
7. `SRC:144`: S115 locator "before and after the DRIVE example".
8. `E:190`: `../verification/calibration-registry.md:38`.
9. Terminology: palm-orientation column, one-sign MOURN, §6 terms, script caveat, §10 payload, social-field dial.
10. Records owner: correct `LES:85` and `LES:72`.

## Verification gaps and unrun checks
- Not run: claim C's counters (`find corpus/knowledge -name '*.md' | wc -l`, expected 227) and `python3 -B reports/round-28/readme/sweep.py`. These are outside section 12 and belong to other seats.
- No `lsp` device is in this seat's tool set. Grep was the literal fallback, used only to locate lines. Each finding rests on text I opened, listed below.
- Kendon 1988 was not opened. Google Books search-inside was refused twice (HTTP 429, a Google "sorry" page). I did not retry and did not bypass it. The archive copy is lending-restricted (`.ufo/waves/round-51/build/ScribeSec09Alternate.md:28`). So whether Kendon says anything about women is unknown here. R12-1 rests on what the S081 row carries.
- Wikipedia pages (tier C) were not reopened. They are not landed rows.
- Reading method: the S086 PDF was converted by the reader. Intro pages 2–12 were read directly, and the full text was searched by term. S087 was read through p.15. S117 was read in lines 1–265 of 553 (abstract, §1, §2.1–2.5). S115 and S081 were read in full.
- No §12 receipt was found in the entry, the build seat reports, or the lesson. I did not open `reports/round-51/` beyond `claims.json`, and I did not open `reports/round-51/calibration/`.
- No installs. Nothing was added or updated (RULES.md tooling directive: none needed).

## URLs opened (access date 2026-10-22)

| URL | What it shows | Result for the row |
|---|---|---|
| books.google.com/books/about/Sign_Languages_of_Aboriginal_Australia.html?id=Aa34NAEACAAJ (served via books.google.com.br) | Publisher description; Kendon 1988; CUP 2013 reprint; 562 pp.; "sign language as a means of communication among Australian Aborigines"; nine years of fieldwork | S081: quote holds for the description. "Mourning", "women", "alternate" and "speech taboo" are absent (R12-1). Tier B fits. |
| pure.uvt.nl/ws/portalfiles/portal/100130712/Zeshan_deVos_Eds._2012.pdf | Zeshan & de Vos 2012 introduction: printed pp. 2, 3, 10–11 (PDF 11, 12, 19–20) | S086: shared (p.2) and hereditary (p.2) hold; mourning (p.3) holds as secondary; "two kindreds" absent; loci and Table 2 on p.11 (R12-5, R12-9). |
| linguistics.stonybrook.edu/faculty/mark.aronoff/files/Emerging%20sign%20languages.pdf | Meir, Sandler, Padden & Aronoff manuscript: pp. 3, 4, 10, 13, 15 | S087: typology (p.3) holds; "both deaf and hearing members" (p.4) holds, unpinned; "one or two families" (p.10) holds, unpinned; houses pointing (p.13); no village loci (p.15). |
| cslds.org Module 4 (http) | Stokoe's three parameters; DRIVE (HKSL) example | S115: parameters hold. Locator is wrong (R12-7); ASL-only caveat omitted. |
| pmc.ncbi.nlm.nih.gov/articles/PMC10622114/ | Lee & Secora 2022 (author manuscript, PMC copy): abstract, §1, §2.1 | S117: concept holds on full text. Tier A on an abstract breaks criterion 6 (R12-3). §2.1 caveat (R12-8). |
| doi.org/10.1093/oxfordhb/9780195390032.013.0018 (via CrossRef) | Meir et al., "Emerging Sign Languages"; published 2010-06-28 | S087 year 2010 holds. |
| books.google.com/books?id=Aa34NAEACAAJ&q=mourning, and the same with &q=women | HTTP 429, Google "sorry" page, both times | Not verified; not retried. |

## Commands run (all read-only)

| # | Command or call | Result | Exit |
|---|---|---|---|
| 1 | read reports/round-51/claims.json | C statement, falsifiers, must-not-cite list | ok |
| 2 | read sign-languages-manual-modality.md (full) | §12 at 188–195 | ok |
| 3 | read corpus/QUALITY.md | criteria 1–8; criterion 6 at line 29 | ok |
| 4 | read ~/.omp/agent/RULES.md | tooling directive; no installs made | ok |
| 5 | read calibration-registry.md:30–45 | H is at line 38 | ok |
| 6 | read politeness-taboo-euphemism.md:105–130 | line 118 is the sea-folk micro-example | ok |
| 7 | grep corpus/SOURCES.md for S081, S086, S087, S115, S117 | rows at lines 110, 115, 116, 144, 146 | ok |
| 8 | read SOURCES.md rows 110, 115–116, 144, 146 (raw) | full rows | ok |
| 9 | read entry lines 188–195 (raw) | §12 text | ok |
| 10 | read politeness lines 75–77 and 118 (raw) | lines 75, 77 and 118 | ok |
| 11 | grep entry for cited S-ids | uses at 40, 59, 61, 135, 139, 190 | ok |
| 12 | grep corpus, PROVINCE.md and build reports for Varn and NON-CANON | Varn: entry, build draft, Varner only | ok |
| 13 | glob corpus/knowledge/**/calibration-registry.md | verification/ | ok |
| 14 | bash: git show da31d3c:entry \| sha256sum; sha256sum working file; git log; git show --stat da31d3c | hashes match; commit list; three files changed | not captured on this call (re-run in 15) |
| 15 | bash: re-run hash compare, SOURCES row count, git log -1 | hashes match; HEAD 9feb69e | EXIT=0 for each |
| 16 | read the five source URLs and the DOI (table above) | as tabled | ok |
| 17 | glob corpus/**/worked-example-verification.md | verification/ | ok |
| 18 | read verification/worked-example-verification.md | class rules; F1–F7; DR-WE rows | ok |
| 19 | read PROVINCE.md | refuses canon and rights rulings | ok |
| 20 | grep S086 text for mourn, women, taboo, congenital, kindred, hereditary | mourning at p.3; hereditary at p.2 | ok |
| 21 | grep lesson for S-ids; read lesson lines 37–44, 72–74, 85–88 | gate lines; re-cite claim; S080 tier rule | ok |
| 22 | grep entry for round-51, boundary-count, lessons/, DR-SGN | DR-SGN appears only in §11; no must-not-cite hit | ok |
| 23 | read build ScribeSec12Example.md | Wikipedia NEW-1 and NEW-2; tier note | ok |
| 24 | grep politeness file for NON-CANON and canon | no NON-CANON; "canon" at lines 37 and 135 | ok |
| 25 | grep entry, SOURCES and build reports for women and bereaved | E:139 `(to-verify)`; build NEW-2 | ok |
| 26 | glob .ufo/waves/round-51/** (names only) | peer report names; none opened | ok |
| 27 | two Google Books search-inside reads | HTTP 429 | failed |
