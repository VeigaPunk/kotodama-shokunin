# Review D — sign-language entry re-citation off S094 (round 52, attempt 1)

Seat: KotodamaR52.ReviewDLines, 2026-10-22. Assigned item: attack the landed text of claim D
(`dea5ece`) — diff `147cfde..dea5ece` on
`corpus/knowledge/linguistics/sign-languages-manual-modality.md`, re-open by ordinary means the
page of every S-id each changed line now cites for the changed detail, quote the carrying passage
or record it as absent. Godspeed axes: (a) evidence depth — every changed line × every cited id ×
the changed detail; (b) verdict accuracy — honest "not there" calls; (c) contract fidelity —
canonical counter and D's negative constraints. All moves below improved an axis and harmed none;
no installs performed (none needed).

## Method and access (QUALITY criterion 10)

Four sources, all opened this session by plain fetch (read tool; no headless browser, no challenge
bypass):

- S096 — CSLDS Module 6, http://www.cslds.org/apsl-consortium/sign-linguistics/6-phonetics-and-phonology-minimal-pairs/ — plain HTML, no gate. Access 2026-10-22.
- S097/S133 — CSLDS Module 7, http://www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition/ — plain HTML, no gate. Access 2026-10-22.
- S071 — Stokoe, *Sign Language Structure* (1978 Linstok reprint / ERIC ED189878 scan), full text at https://archive.org/stream/micro_IA41153455_0834/micro_IA41153455_0834_djvu.txt (archive.org ERIC-microfiche item). Access 2026-10-22. OCR errors present ("siqnation", "exclusivitty"); quotes below transcribe them as printed or normalize a single letter with [sic] awareness.
- S095 — Brentari, Fenlon & Cormier, "Sign Language Phonology" (Brentari 2019 chapter), https://discovery.ucl.ac.uk/id/eprint/10054130/1/Brentari_Sign%20Language%20Phonology.book.chapter.pdf (UCL Discovery, open repository). Access 2026-10-22.

No `lsp` device exists in this session's inventory and no language server covers corpus Markdown;
all checks are textual plus the canonical counters. Record: text-level, not semantic-proof.

## Landed-state checks (all pass)

- Canonical counter `awk '/S094/{n++} END{print n+0}'` → **0**. HEAD is `dea5ece`; worktree byte-identical to it for this file (`git diff dea5ece -- <file>` → 0 lines; `status --porcelain` empty), so the counter measures the landed text.
- No S-id S134+ anywhere in the entry (grep `S1[3-9][0-9]` → no matches).
- No reference to `round-52` lessons or `speech-surrogates` (C entry) in the entry (case-insensitive grep → no matches).
- Diff is exactly 5 insertions / 5 deletions; hunk `@@ -80,17 +80,17 @@` keeps numbering identical, so the changed lines are 83, 87, 90, 92, 93 as declared.

## Per-line verdicts (changed detail → cited page)

### Line 83 — "…location, handshape, movement (S071, S096…) — plus palm orientation, which Battison (1978) proposed as a fourth parameter (S096)… nonmanual features, which are part of the phonology (S095). Contrast is tested with minimal pairs… (S096)." — **PASS**

- S096 (Module 6), paragraph beginning "Sign language phonologists can make use of minimal pairs…": "Stokoe argued that the handshapes, locations and movements in his model are all phonemes (he called them 'cheremes' in his early works…" — carries the parameter set and its minimal-pair grounding.
- S096 (Module 6), unheaded paragraph after the movement pairs (before the SEWING-MACHINE/PUSH HKSL pair): "Battison (1978) proposed that palm orientation should be added as the fourth phonological parameter in ASL" — carries the fourth-parameter attribution exactly as the entry words it.
- S096 (Module 6), first pedagogy paragraph: "In a minimal pair, the two words are basically identical, except for one difference." — carries "pairs that differ in one parameter".
- S071 (1978 reprint, p. 49, "Three aspects of any sign"): "Tab, dez, and sig are shortened forms of the terms tabula, designator, and signation." and the boxed revision gloss "TAB is where sign activity occurs… DEZ is what acts… SIG is the action" — carries the tab/dez/sig terminology the line attributes to S071 (S096 uses only the English glosses, so the S071+S096 joint citation is the right split).
- S095 (PDF p. 6, §2.1): "Non-manual behaviors of the face and body are also part of the phonology (see e.g., Pfau & Quer, 2010)" — carries the nonmanuals clause (this S095 detail is unchanged text but the line is a changed line).

### Line 87 — Handshape row: "the CSLDS module, reporting Battison 1978, counts 45 possible handshapes in ASL, of which only 7 can serve as the passive hand (S097)" — **PASS**

- S097 (Module 7), paragraph opening "In effect, the Symmetry and Dominance Conditions exclude a large number of complex gestures…": "Out of the 45 possible handshapes in ASL, only 7 can appear as the passive hand of a Type-3 two-handed sign." — carries both numbers verbatim.
- Minor note, non-falsifying: the module cites Battison 1978 (pp. 204, 206, 207) for the typology and the Dominance Condition; the 45/7 sentence itself is the module's exposition without its own inline page cite. "The CSLDS module, reporting Battison 1978, counts…" is a fair description of that relationship.

### Line 90 — Palm orientation row: "Battison (1978) adds it as a fourth parameter, with the ASL pair CHAIR/NAME (S096), while the 1978 Stokoe reprint argues against isolating it (S071)" — **PASS**

- S096 (Module 6), same unheaded paragraph: "Battison (1978) argued that signs in ASL may only differ in terms of the palm orientation, and the examples given by him were CHAIR and NAME." — carries both the fourth-parameter claim and the CHAIR/NAME pair.
- S071 (1978 reprint, p. 92): "To suppose as some linguists do that there are four parameters of a sign is to abandon a logical position without having another to move to or even without realizing that the three aspects are postulated not observed."
- S071 (p. 93, section headed "Handshape & Attitude in the DEZ"): "Handshape and attitude (miscalled orientation)… are not variable independently of one another, except in a few special circumstances."
- S071 (p. 95): "Attempts at isolating orientation as a basic or phonemic contrast in ASL which ignore the tri-aspectual analysis confuse the dez as the forearm part of what acts with the sig as the rotational or linear action" — carries "argues against isolating it" strongly.
- S095 (PDF p. 9, §2.1.1): "Orientation is traditionally regarded as a minor parameter, since there are fewer minimal pairs based on orientation alone (Brentari, 2012)." — carries the unchanged "fewer minimal pairs rest on orientation alone (S095)" clause.

### Line 92 — Two-handed constraints row: "seven shapes (A, S, B, 5, G, C, O) in the 1978 formulation the CSLDS module reports (S097); an earlier, smaller 1974 set is not checked here (to-verify)" — **PASS**

- S097 (Module 7), paragraph opening "With regards to Type 3 signs, Battison made another interesting observation": "the passive hand can only be one of the following handshapes: A, S, B, 5, G (i.e., 1), C and O, with very few exceptions" — carries the seven shapes in order.
- S097, Dominance Condition statement in the same paragraph: "The specification of the passive handshape is restricted to one of a small set: A, S, B, 5, G (i.e., 1), C and O." — carries the condition wording.
- S097, following paragraph: "These handshapes are unmarked handshapes – they are easier to articulate, more frequent…" — carries "small unmarked set".
- The entry's symmetry-condition gloss ("when both hands move, their specifications match") matches Module 7's Symmetry Condition quotation (1978, pp. 33–35: same location, handshape, movement; orientation symmetrical or identical).
- The 1974 six-shape claim (S094/S132 territory) is now explicitly not asserted and carries an inline `(to-verify)` mark — the honest handling required by the claim's method; S132 is the rejected row, S133 the superseding locator, both consistent with this wording. Note the page has no heading named "Dominance Condition" (S133's anchor note is correct: only title, Type 1–3, References), but line 92 cites S097 for content, and the body text names "the Dominance Condition (Battison, 1978, p.206)" — no defect.

### Line 93 — Minimal pairs row: "APPLE/ONION (location), CAR/WHICH (handshape), NAME/SHORT (movement), CHAIR/NAME (orientation) — the ASL pairs the CSLDS module lists, after Battison 1978 (S096)" — **PASS, one minor note**

- S096 (Module 6) section "2. Minimal Pairs of signs in ASL and HKSL that differ in location": lists "ONION – ASL" and "APPLE – ASL" (with HKSL fillers HOSPITAL, GREY) — carries APPLE/ONION as the ASL location pair.
- S096 section "1. …differ in handshape": "CAR – ASL (Battison, 1978)" and "WHICH – ASL (Battison 1978)" — carries CAR/WHICH.
- S096 section "3. …differ in movement": "NAME – ASL (Battison, 1978)" and "SHORT – ASL (Battison 1978)" — carries NAME/SHORT as a movement pair.
- S096 orientation paragraph: "the examples given by him were CHAIR and NAME" — carries CHAIR/NAME as an orientation pair.
- Minor note, non-falsifying: on the page the Battison-1978 tags are explicit for CAR, WHICH, NAME, SHORT (video labels) and CHAIR/NAME (prose), but the location pair APPLE/ONION carries no Battison tag. "…the ASL pairs the CSLDS module lists, after Battison 1978" therefore states provenance precisely for three of four pairs. The operative citation is to the module (S096), which does list the pair, so the detail stands. If the L1 wants a zero-nit text: "as listed by the CSLDS module (S096)" would drop the gloss — author-lane advice, not a requirement.

## Findings by severity

- Blocker / major: none. No falsifier fires: counter 0, no S134+, no lessons/C-entry citations, and every changed detail rests on a row whose page I re-opened this session by ordinary means and which carries it.
- Minor (2): the "after Battison 1978" gloss on line 93 overreaches for APPLE/ONION (untagged on the page); the "reporting Battison 1978" gloss on line 87 rests on module context rather than an inline page cite for the 45/7 sentence itself. Both are wording observations; the citations themselves (S096, S097) carry the details.

## Residual risk and verification gaps

- The Module 6/7 pair demonstrations are Panopto video embeds; I verified the pages' textual labels, headings and prose only. A gloss error inside a video would not be caught by this check.
- S071 quotes come from archive.org's OCR of the ERIC microfiche scan; OCR defects exist. Recheck cadence per SOURCES row: 365d.
- I did not re-run `tools/check-source-access.py`, the separability/dry-run receipts, or anything for claim C — outside this seat's scope.
- Line-number identity between base and landed text is established by the diff hunk header, not re-derived per line.

## Result

Claim D's landed text withstands attack on all five changed lines. Verdict per line: 83 PASS, 87 PASS, 90 PASS, 92 PASS, 93 PASS (one minor wording note each on 87 and 93, neither falsifying). Recommendation: accept D as measured.
