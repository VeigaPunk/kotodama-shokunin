# ReviewRoutedFixes — prerequisite d761ee8 vs round-53 routed items (2026-10-22)

Seat: KotodamaR54a2.ReviewRoutedFixes (leaf; no dispatches). Axes: verification coverage, calibration, evidence quality. No tool installs (system curl; poppler pdftotext/pdfinfo already present). No LSP server exists for markdown in this lane — all checks are text-level plus direct re-opens of the cited pages this session; grep output is used only as fallback, never as semantic proof. All sources below were opened this session by plain request; none met an access control.

Method: `git show d761ee825f94f7ae45e098ad551d7f735645ad22` (4 files, +14/−9); working copy is byte-identical to the commit for all audited paths (`git diff --stat d761ee8 -- <paths>` empty); routed prescriptions read at `corpus/lessons/round-53-verifier-spotcheck.md:114-121` (partly-supported sentences) and `:169-183` (routed defects 2–6).

## Verdicts

| item | verdict |
|---|---|
| gesture line 68 (S201 page locators) | **PARTLY** — two of three locators correct; the Kendon 208 quote locator is now wrong (147, should be 146) |
| gesture line 133 (S221 softening) | **FIXED** |
| gesture line 150 (S223 "one culture (Barai)") | **FIXED** |
| gesture line 199 (S234 quote + §2.3) | **FIXED** |
| speech-surrogates line 75 (S145 → S185) | **FIXED** |
| SOURCES.md: S145 rejected as superseded | **FIXED** |
| SOURCES.md: S185 queued → mined | **FIXED** |
| SOURCES.md: S225 access note | **FIXED** |
| lessons README row + count + Revision 10 | **FIXED** |

## Item evidence

### 1. Line 68, `gesture-co-speech-pointing.md` — PARTLY

Route: S201 row URL `https://www.uva.nl/binaries/content/documents/personalpages/p/f/r.pfau/profile-en/profile-en/uva:foldout%5B2%5D/cpitem%5B21%5D/asset` — HTTP 200, `application/pdf`, 474,531 bytes, 20 pages; page furniture reads "OUP UNCORRECTED PROOF", "MATHUR-Chapter 4 Response-Pageproof", "June 30, 2010 2:31 AM"; printed folios run 144–163 (pdf p1=144, p2=145, p3=146, p4=147; chapter start p. 144 verified in the page-1 footer). Text extracted with pdftotext and matched per page on whitespace-normalized text.

Ground truth in the proof:

- Printed p. 146 (pdf page 3) carries, in one continuous passage: England "(Northamptonshire) and Italy (Campania), Kendon (2004) and Kendon and Versante (2003)"; the 1-handshape quote "a speaker singles out an object which is to be attended to as a particular individual object" (Kendon 2004, 205); and the B-handshape quote "the object being indicated is not itself the primary focus or topic of the discourse but is something that is linked to the topic" (Kendon 2004, 208).
- Printed p. 147 (pdf page 4) carries: Wilkins's inventory "the pointing handshapes distinguished by Wilkins include the “middle ﬁnger point” and the “wide hand point.”", the six-handshape/allomorph discussion, and Arrernte eye-pointing ("the socket toward a particular referent", "it is used to exclude third parties").

Scored against the fixed line (line 68):

- "Northamptonshire (England) and Campania (Italy) … (S201, p. 146 in the proof pagination)" — correct (was p. 145). FIXED.
- "Arrernte … ‘wide hand point' among six handshapes (S201, p. 147)" — correct (was p. 146). FIXED.
- Kendon 2004, 208 quote "(as reported in S201, p. 147)" — **wrong**: the quote is on printed p. 146, not 147. The blanket +1 over-corrected this third locator; the pre-fix line had it right at p. 146. The round-53 routed prescription ("locators should read pp. 146/147") addressed the two data locators 145/146; the quote's locator did not move.
- Neighbour unchanged and still correct: line 67 cites the Kendon 205 quote at "S201, p. 146" — on printed p. 146. ✓

One-word-class fix closes it: revert the quote's locator to "as reported in S201, p. 146".

### 2. Line 133 — FIXED

Changed text: "the archive holds an Ewe route-description deposit from Ghana, non-elicited, with speech and gesture together (S221; the archive record does not itself tie the deposit to this study)". The dropped phrase "the corpus behind the study" was the routed defect ("the page does not itself call it 'the corpus behind the study'"); the new parenthetical states exactly the limitation the closure recorded. No residual claim is made on S221's behalf.

### 3. Line 150 — FIXED

Route: S223 row URL `https://pure.mpg.de/rest/items/item_762562_18/component/file_1466200/content` — HTTP 200, `application/pdf`, 254,913 bytes, 16 pages. The paper's Discussion reads: "Only one culture to date has been reported to lack index-finger pointing altogether among adult interactors (Barai speakers of Papua New Guinea; see Wilkins, 2003)" and, separately, "but this report provides no empirical evidence and is based on personal communication with a missionary, who we were not able to trace". The fixed line now reads "the report that one culture (Barai) lacks index-finger pointing altogether is `(to-verify)`, since the source reports it rests on untraceable hearsay (S223, p. 708)" — exactly the routed prescription, and `(to-verify)` is kept.

### 4. Line 199 — FIXED

Route: `https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2024.1314120/full` — HTTP 200, text/html, 836,812 bytes, open access. The full text reads: "the “thumbs-up” gesture is an offensive gesture in Sardinia (Italy) and some parts of Greece", and the nearest preceding section heading is "2.3 Variation in gesture forms and functions". The entry's quote "an offensive gesture in Sardinia (Italy) and some parts of Greece" is a verbatim substring, and "(S234, §2.3)" matches the section. The sentence's citation there is Morris et al. 1979, so the entry's hedge "is reported as" is accurate to the page.

### 5. Speech-surrogates line 75 — FIXED

Changed cells now cite "(S144; S185)" (keeps) and "(S185; S146)" (distance); `grep -rn 'S145' corpus/knowledge` → 0 hits, and no "S201, p. 145" locator survives anywhere. Route: S185 row URL `https://www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2003/papers/p15_2131.pdf` — HTTP 200, `application/pdf`, 232,976 bytes, 4 pages, printed 2131–2134.

- Distance passage: printed p. 2132, left column (folio 2132 is the footer of the second page; the passage sits above it), reading "Recall also that Silbo Gomero is a whistled language designed for long-distance communication. It was" / "commonly used in the past to convey messages over distances of 2 or 3 kms and could be heard as far as 8 kms away." This confirms S185's corrected anchor ("left-hand column of printed p. 2132, in the paragraph opening 'Recall also…'") and that S145's old p. 2131 locator was wrong. The line's "2 to 3 km, heard as far as 8 km" is carried. ✓
- Keeps-cell co-cite carried by the same page's abstract (printed p. 2131): "vowel qualities and consonantal place of articulation distinctions are transmitted primarily by F2-to-H0 transposition", "and has been introduced into the primary school curriculum, where it has been a required subject since 1999". ✓ (Notation nit below.)

### 6. SOURCES.md rows — FIXED (all three)

- **S145 (line 174):** status cell now `rejected`, used-by `—`, and the quotes cell ends: "Superseded 2026-10-22 (round 54): retired in favour of S185, which carries the corrected locator and quote for the same paper; the entry now cites S185." Matches the routed base_note ("S145 mined → rejected as superseded") and the zero remaining citations in `corpus/knowledge`.
- **S185 (line 214):** status cell now `mined`, used-by `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`; anchor and quote verified verbatim against the opened PDF (above), including the note that S145's Gate quote had replaced the paper's "It was" with "Silbo Gomero was".
- **S225 (line 254):** anchor cell now carries "Access note (round 54, 2026-10-22): the live catalogue page returned HTTP 403 to a plain request at the round-53 closure; Wayback capture 20260106191949 carries the abstract." — the routed item 3 ("add an access note at its next re-check") executed at this commit.

### 7. `corpus/lessons/README.md` — FIXED

New row: `| corpus/lessons/round-53-verifier-spotcheck.md | plain | 0/4 | none (routed defects carry no Q ids) | non-author closure record; fleet MANIFEST kotodama r53 | bytes=19687 lines=185 sha8=397f2203 |`. Pin re-measured live: `wc -c` = 19687 ✓, `wc -l` = 185 ✓, `sha256sum` = `397f22037197…` → first-8 `397f2203` ✓. Count line updated "**Rows: 43. Files: 43.**" and `ls corpus/lessons/*.md | wc -l` = 43 ✓. Revision 10 block added: "Adds one §2 row … pinned from the live bytes in the round-54 prerequisite commit; rows and files 42 → 43." This executes routed item 6.

## Findings by severity

1. **MEDIUM — line 68's third locator mis-corrected.** The Kendon 2004, 208 quote is on printed p. 146 of the opened OUP proof (pdf page 3), but line 68 now cites "(Kendon 2004, 208, as reported in S201, p. 147)". Pre-commit the locator was p. 146, which was correct. Recommend reverting that one locator to p. 146.
2. **LOW — S201 row anchor cell left stale.** `corpus/SOURCES.md:230` bounds "Wilkins's six handshapes including the middle-finger point and the wide hand point" under "pp. 145–146"; the proof carries them on printed p. 147 (with the allomorph discussion and eye-pointing). The row was outside the routed scope, but after this commit it disagrees with both the corrected line 68 and the PDF. Recommend moving that clause to the p. 147 group at the row's next touch.
3. **INFO — H0 vs H1 notation.** The opened S185 page says "F2-to-H0 transposition"; the entry and the S144/S145 rows say "F2 to H1". Same physical quantity (first harmonic), different notation, and S144 is the lead cite; noting so the next re-check does not read it as a mismatch.

## Residual risk and verification gaps

- S221 archive object page (`https://archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0005_6BE1_E`) was not re-opened this session; the line 133 verdict rests on the wording fix matching the routed requirement, plus the round-53 closure's own re-open which the new parenthetical mirrors.
- S225's live 403 was not re-requested this session; the added note's Wayback id `20260106191949` matches the closure's recorded capture, but I did not fetch it to re-verify the abstract text.
- The three S201 ground-truth page assignments (146/146/147) come from one fetch of the uva.nl proof this session; if the file is ever replaced by a re-paginated version, all three locators need re-checking together.
- `resume_continuity_v1` (role boilerplate): no such mechanism or artifact exists anywhere in this diff or lane; nothing to verify, recorded as not applicable rather than passed.
