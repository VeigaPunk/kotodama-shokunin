# ReviewCells135to159 — round-53 carried registry cells S135, S141, S147, S151, S159

Seat: `KotodamaR55.ReviewCells135to159` (reviewer, leaf, no delegation). Every source re-opened this session, 2026-10-22, by ordinary means only (plain `curl`; `pdftotext`/`pdfinfo`/`qpdf` for PDFs; `soffice --headless` for the .doc). No challenge, captcha or paywall met. Downloads at `/fast/scratch/hyaku/kotodama-r55/ReviewCells135to159/`. Recommendation only — I edited no file but this report.

## What the closure said was wrong

`corpus/lessons/round-53-verifier-spotcheck.md:178-181` routes the cells under "Speech-surrogates leftovers (the lane's own frontier list)". The in-lane lesson `corpus/lessons/round-53.md:213` itemizes the defects:

- **S135** — anchor cell: wrong page count and the locator does not reach the pages the entry cites (`ScribeDOverreads` F3, `ReviewDS135` R1).
- **S141** — anchor cell: wrong page ("p. 4 paragraph [13]"; `ReviewDS135` R2).
- **S147** — teaches cell carries the round-52 over-read "lip-locked /p/, /b/ approach /k/" (`ScribeDOverreads` F3; the paper makes the [k]-similarity claim for [p] only).
- **S151** — teaches cell carries the over-read "made with children of the village — the register is transmitted young" (`ScribeDOverreads` F3, `ReviewDS147S151` §4/§6).
- **S159** — anchor names a heading the file lacks (`ScribeDFragments`).

## Repair convention (resolves the ticket's "old -> new cell text" vs. the contract)

`corpus/SOURCES.md:9-12` is append-only: "only `status`, `recheck` and `used-by` change in place … a correction is a new row whose `teaches` opens `supersedes S0NN —`". Precedent: S185 supersedes S145 for an anchor+quote slip (`SOURCES.md:174,214`), S186 supersedes S157 for an access note (`SOURCES.md:215`). The round-53 lesson also says these five cells "need superseding rows". So for all five I give: (1) the appended retirement text for the old row's teaches cell (the "old -> new"), and (2) a complete drafted superseding row. No tier change is warranted for any of the five — no in-place tier edit is requested, and each filed tier matches QUALITY criterion 6 for its scope — so no special tier-superseding row is needed beyond the five drafts. All five rows' `used-by` names only `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`, whose citations the L1 re-points to the new ids (S135 appears 16 times in that entry, S141 2, S147 3, S151 2, S159 4). Draft ids below: final ids assigned by the L1 at integration.

---

## S135 → NEW-ReviewCells135to159-1 (anchor correction)

**Old (anchor cell, `SOURCES.md:164`):** `Abstract and "Body Text", PDF pp. 1–2 of 17`

**Re-open evidence.** `curl http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf` → HTTP 200, 1,439,365 bytes, application/pdf (same copy as round 53: byte count identical). `pdfinfo` Pages: 10; `qpdf --show-npages` → 10; `file(1)` reports "17 page(s)" — a heuristic miscount, the reverse-confusion ReviewDS135 recorded (file also says 10 for the 17-page S141). The anchor's "of 17" is wrong on either count, and "pp. 1–2" does not reach the cited material. Page map of the entry's S135 clauses (pdftotext, normalized): abstract "secondary speech codes based on whistles anchored to, and derived from, a spoken language" p. 1; the sign-language contrast "substantially different from sign languages, which are self-standing lexically, grammatically, and phonologically" p. 2; "to speak in secret from foreigners" and "herding" p. 2; "commonly remain intelligible up to 2km" (the line-53 distance cell) p. 2; "Mazatec or Chinantec" (Mexico) p. 3; "basic segmental information is rendered by the amplitude envelope" p. 5; the whole informational-load paragraph — "seven to eight contour tones" vs "two level tones", "more formulaic and therefore more predictable", "high levels of intelligibility … such as Chinantec", and "single-clause utterances and equally simple conversational repairs" — p. 7.

**Retirement text appended to S135's teaches cell:** ` Superseded 2026-10-22 (round 55): retired in favour of NEW-ReviewCells135to159-1, which carries the corrected page count and the locators of the cited passages; the entry now cites NEW-ReviewCells135to159-1.` — and old row status `mined` → `rejected`, used-by → `—`.

**Draft row:**

```
| NEW-ReviewCells135to159-1 | Julien Meyer, David Díaz Reyes, Andre Batchelder-Schwab and Bernard Gautheron 2025, "Whistled Languages and Whistled Speech", *Encyclopedia of Language and Linguistics* (Elsevier), author-hosted copy — http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf | book | B | as S135: the mechanism and social setting of whistled speech as a secondary speech code | Abstract and "Body Text": abstract pp. 1–2, sign-language contrast and secrecy/herding p. 2, Mexico mention p. 3, tone and segmental rendering pp. 5–6, tone-load and intelligibility paragraph p. 7, of a 10-page copy (`file(1)` misreports 17; `pdfinfo` and `qpdf` agree on 10) | supersedes S135 — anchor only: S135's "pp. 1–2 of 17" miscounts the copy (10 pages) and does not reach the cited passages, which sit on pp. 1–7; teaching as S135 | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
```

## S141 → NEW-ReviewCells135to159-2 (anchor correction)

**Old (anchor cell, `SOURCES.md:170`):** `p. 6 paragraph [15]; p. 4 paragraph [13]; p. 8 paragraph [20]`

**Re-open evidence.** `curl https://www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf` → HTTP 200, 233,242 bytes (same copy as ScribeDOverreads fetched). `pdfinfo`/`qpdf`: 17 pages; the printed headers "Hmong Studies Journal Page N of 17" align 1:1 with PDF pages. Paragraph [13] sits on page 5 (page 5 carries markers [12]–[14]); [15] is on page 6 and [20] on page 8, so only the [13] page is wrong. Paragraph [13] itself carries the two sentences the row is cited for: p. 5, [13]: 'the single "voice" of the qeej is made from a blending of the multiple pipe tones' (13 words) and 'except for the Hmong in China, the instrument is played now exclusively by men when it was invented by women' (18 words). Teaches cell verified: p. 6, [15] has "one of seven tones", "all of the Hmong vowel sounds" and "cannot be pronounced by the qeej"; p. 8, [20] "note by note, word by word". Only the one page number changes.

**Retirement text appended to S141's teaches cell:** ` Superseded 2026-10-22 (round 55): retired in favour of NEW-ReviewCells135to159-2, which carries the corrected page for paragraph [13]; the entry now cites NEW-ReviewCells135to159-2.` — status → `rejected`, used-by → `—`.

**Draft row:**

```
| NEW-ReviewCells135to159-2 | Morrison, Gayle 1998, "The Hmong Qeej: Speaking to the Spirit World", Hmong Studies Journal v2n2 — https://www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf (open copy) | paper | B | as S141: the Hmong qeej as a ritual speech instrument, from interviews with players including a master player; one community's own account, not a comparative study | p. 6 paragraph [15]; p. 5 paragraph [13]; p. 8 paragraph [20] (printed "Page N of 17" headers; PDF pages align) | supersedes S141 — anchor only: S141 places paragraph [13] on p. 4; it is on p. 5, holding the "blending of the multiple pipe tones" and "exclusively by men" sentences the row is cited for; teaching as S141 | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
```

## S147 → NEW-ReviewCells135to159-3 (teaches correction)

**Old (teaches cell, `SOURCES.md:176`):** `in most tone languages the whistle selects primarily F0 cues carrying tone registers and contours, in most non-tonal languages primarily segmental formant cues, and in an intermediate category both; eight Turkish vowels fall into four whistle-frequency groups resolved by vowel harmony; consonants appear as frequency and amplitude modulations with silent gaps, and lip-locked /p/, /b/ approach /k/; the practice lives in the village of Kuşköy and with the shepherds on the summer high plateaus`

**Re-open evidence.** `curl http://www.icphs2007.de/conference/Papers/1286/1286.pdf` → HTTP 200, 337,860 bytes, 4-page PDF (printed pp. 837–840). "lip-locked" appears nowhere in the paper (0 hits, both spellings). Printed p. 839, §3: the [k]-similarity is asserted for [p] only — "The occlusive [p] is expressed mainly with this process and is therefore very similar to [k] in whistles." The [b] facts the paper does state: p. 839, §3.1.1 "Some consonants are more difficult to classify because they bear intermediate positions between two of these categories, like [n], [b], [v] and [f]", and p. 839, §3: "the fixed lips modify the labial articulation of [m], [p] and [b] which all use in compensation a glottal occlusion". All other teaches clauses verified on the pages (§1 typology "primarily Fo cues" / "segmental cues of the formants" / "intermediate category"; p. 838 four groups and harmony; "silent gaps" §3; "village of Kusköy and by the shepherds going in summer in the high plateaus" p. 837). Only the defective tail changes.

**Retirement text appended to S147's teaches cell:** ` Superseded 2026-10-22 (round 55): retired in favour of NEW-ReviewCells135to159-3, which drops the "lip-locked /b/ approaches /k/" over-read; the entry now cites NEW-ReviewCells135to159-3.` — status → `rejected`, used-by → `—`.

**Draft row:**

```
| NEW-ReviewCells135to159-3 | Meyer, Julien 2007, "Whistled Turkish: Statistical analysis of vowel distribution and consonant modulations", ICPhS XVI (Saarbrücken), paper 1286 — http://www.icphs2007.de/conference/Papers/1286/1286.pdf | paper | A | as S147: the Kuşköy whistled Turkish system as measured — the eight vowel bands and the four statistical groups, harmony rules, and the consonant modulations; the tone/non-tonal/intermediate assignment of languages including Mazatec, Chinantec, Akha, Hmong, Surui, Siberian Yupik, Chepang | §1 Introduction (p. 837, strategy typology and the Kusköy practice); §2 and §2.2.1 (vowel groups, harmony); §3 (consonants) | supersedes S147 — teaches cell only: S147's "lip-locked /p/, /b/ approach /k/" over-reads printed p. 839, which states the [k]-similarity for [p] alone and classifies [b] as an intermediate case; in most tone languages the whistle selects primarily F0 cues carrying tone registers and contours, in most non-tonal languages primarily segmental formant cues, and in an intermediate category both; eight Turkish vowels fall into four whistle-frequency groups resolved by vowel harmony; consonants appear as frequency and amplitude modulations with silent gaps, and the occlusive [p] whistles "very similar to [k]" while [b] counts among the intermediate [n], [b], [v], [f]; the practice lives in the village of Kuşköy and with the shepherds on the summer high plateaus | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
```

## S151 → NEW-ReviewCells135to159-4 (scope + teaches correction)

**Old (teaches cell, `SOURCES.md:180`):** `a Sochiapam Chinantec whistled-speech corpus exists, made with children of the village — the register is transmitted young`

**Re-open evidence.** `curl 'https://archive.mpi.nl/tla/islandora/object/lat%3A1839_00_0000_0000_0016_B509_0'` → HTTP 200, 29,619 bytes HTML, deposit CAM20459. The page's only content sentence, Details → Description: "David Yetman and Mark Sicoli elicit spoken and whistled Chinantec from children in San Pedro Sochiápam." (14 words; the page also carries the persistent identifier `https://hdl.handle.net/1839/00-0000-0000-0016-B509-0` and Country "Mexico"). Zero hits on the page for "of the village", "transmit"/"transmitted", "learn"/"learned"/"young", "Oaxaca". The old teaches carries two additions the page does not: "of the village" (the page names the place of the elicitation, not the children's provenance — sibling sessions on the parent collection support "children of Sochiápam" but are outside the row's anchor) and "the register is transmitted young" (no acquisition-age claim anywhere). The scope cell's "children of the village produced the material" carries the same "of the village" slip, so the new row corrects the scope cell too (secondary, flagged; the routed defect named the teaches cell).

**Retirement text appended to S151's teaches cell:** ` Superseded 2026-10-22 (round 55): retired in favour of NEW-ReviewCells135to159-4, which drops the unsupported "of the village" and "transmitted young"; the entry now cites NEW-ReviewCells135to159-4.` — status → `rejected`, used-by → `—`.

**Draft row:**

```
| NEW-ReviewCells135to159-4 | The Language Archive, Max Planck Institute for Psycholinguistics — deposit CAM20459, "David Yetman and Mark Sicoli elicit spoken and whistled Chinantec from children in San Pedro Sochiápam" — https://archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0016_B509_0 | dataset | A | the existence and content of a Chinantec whistled-speech deposit from San Pedro Sochiápam, recorded in spoken and whistled Chinantec elicited from children there; not a linguistic analysis, and no acquisition-age statement | deposit title and Description block; persistent identifier `https://hdl.handle.net/1839/00-0000-0000-0016-B509-0` | supersedes S151 — scope and teaches only: S151's "children of the village" and "the register is transmitted young" are not on the page, which says "from children in San Pedro Sochiápam" and carries no acquisition or transmission-age claim; a Sochiapam Chinantec whistled-speech corpus exists, recorded in spoken and whistled Chinantec elicited from children in San Pedro Sochiápam | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
```

## S159 → NEW-ReviewCells135to159-5 (anchor correction; route now names the capture)

**Old (anchor cell, `SOURCES.md:188`):** `§D "Brief textual description of the nominated element": paragraphs on the mountainous terrain and remote houses, on whistled warning/SOS/calling for help, on the remaining use by shepherds, and on decline`

**Re-open evidence.** Live `https://ich.unesco.org/doc/src/36234-EN.doc` → HTTP 200 but serves an unrelated HTML page (44,649 bytes, no title, not the form) — the row's route note is accurate. Wayback availability offered capture `20241003132739`, which redirected at fetch to `20221007161757` — served capture: `https://web.archive.org/web/20221007161757/https://ich.unesco.org/doc/src/36234-EN.doc` → HTTP 200, 236,544 bytes, application/msword (real Word file, "Nomination file no. 00658", 2017 session, Türkiye). Converted with `soffice --headless`. The file has **no heading "Brief textual description of the nominated element"** anywhere: its lettered fields are A–F, and its §D heading is "Geographical location and range of the element". Actual placement of the cited material: §1 "Identification and definition of the element" — "houses being built that are remote and inaccessible from one another" (steep mountains/rugged topography) and the warning/SOS examples "'There is a forest fire!'"; §C — "currently nearly 10.000 people in Turkey's Eastern Black Sea Region are able to speak and/or understand whistled language"; §D — "either disappeared or is limited to a few words spoken by shepherds" (named districts Trabzon, Rize, Ordu, Artvin and Bayburt); §2 "Need for urgent safeguarding" — "One of the most important threats to this element is the increase in the use of mobile phones" and "about to lose its communication function" (the latter is the entry's line-113 quote). The teaches cell's content is all supported — only the anchor is defective. Secondary: the citation cell says "opened via Wayback capture" without a capture id (repeatability); the new row names the served capture.

**Retirement text appended to S159's teaches cell:** ` Superseded 2026-10-22 (round 55): retired in favour of NEW-ReviewCells135to159-5, which names the file's real sections and the served Wayback capture; the entry now cites NEW-ReviewCells135to159-5.` — status → `rejected`, used-by → `—`.

**Draft row:**

```
| NEW-ReviewCells135to159-5 | UNESCO nomination form 00658, "Whistled language" (Türkiye) (English), https://ich.unesco.org/doc/src/36234-EN.doc (live URL serves an unrelated page; read via Wayback capture 20221007161757 — the availability API's closer 20241003132739 redirects to it) | docs | A | Primary State Party nomination document for element 00658: terrain and settlement pattern, use cases, bearers, decline factors | §1 "Identification and definition of the element" (terrain, remote houses, warning and SOS calls); §C community box (nearly 10.000 speakers); §D "Geographical location and range of the element" (shepherd remainder); §2 "Need for urgent safeguarding" (mobile phones, loss of function) | supersedes S159 — anchor and route note only: S159's anchor names a "§D Brief textual description of the nominated element" heading the file does not have (its §D is "Geographical location and range"); Houses "remote and inaccessible from one another" in the Eastern Black Sea Region; whistled warning, SOS and calls for help including "There is a forest fire!"; nearly 10.000 people able to speak and/or understand it; use reduced to "a few words spoken by shepherds"; mobile phones named one of the most important threats | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
```

(Note: the teaches restatement above says "one of the most important threats" where S159's cell wrote "the main threat" — the file's words, adopted verbatim.)

## Residual risk and verification gaps

- Landing the five rows needs the companion edits above (retirement line + `rejected`/`—` on each old row) and re-pointing the entry's citations S135→-1 (16 sites), S141→-2 (2), S147→-3 (3), S151→-4 (2), S159→-5 (4) — outside my scope; stated for the L1.
- `tools/check-source-access.py` was not run; the S159 row's wording "read via Wayback capture" matches the pattern other rows use (cf. S142, S186) and the live-URL note is accurate as of today.
- ScribeDOverreads' round-53 finding F4 left two entry-level residuals on these same rows' lines: line 79's leading "Oaxaca" cites no row (S155 carries it) and "whistles stay short" is not S135's wording — the round-53 lesson routes these to the entry, not the registry; noted, not re-adjudicated.
- S135's scope/teaches cells verified non-defective: every teaches clause traces to pp. 1–2. Not re-audited: S140/S155/S166 (adjacent round-53 findings outside this assignment's five rows).
- Round-53 seats disagreed on the S135 page count (ReviewDS135: 10 via qpdf/pdfinfo; ScribeDOverreads: 17). Settled here: `pdfinfo` 10, `qpdf --show-npages` 10 on the byte-identical copy; the 17 is `file(1)`'s heuristic.
- No installs this run (tooling directive: prefer none). Used: curl, pdftotext/pdfinfo (poppler), qpdf, soffice, python3 — all already present.
- No LSP server applies (corpus markdown and external binaries; no code symbols). Caller checks were text greps: `grep -c` per S-id on the entry file; the registry header (`SOURCES.md:9-12,28`) and precedent rows (S145→S185, S157→S186) set the superseding-row form.
- Unrun by me: the round-55 acceptance scripts (accept-c.py, accept-o.py) and any landing edits — L1's gates.
