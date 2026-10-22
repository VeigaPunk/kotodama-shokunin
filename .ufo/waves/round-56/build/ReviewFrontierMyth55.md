# ReviewFrontierMyth55 — round-55 Frontier items: griffin line, chapter F gloss, S254 locators

- seat: KotodamaR56.ReviewFrontierMyth55 (reviewer, judged on calibration)
- date: 2026-10-22; lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; leaf seat, no subagents, no installs, no git/jj writes.
- Scope: the three routed items, each with exact old -> new line text or a reasoned NO CHANGE. No lane file outside this report was written.
- Method/LSP note: no LSP server answers Markdown in this lane (no language server is configured for `.md`; consistent with round-55 seats' method notes), so the checks below are text-level against current file bytes plus re-opened sources. Every load-bearing web quote was byte-checked against a page fetched this session; no finding rests on unverified memory.

## Findings by severity

No high or medium findings. Four low findings and one stale-premise note; all are one-line corrections.

| # | severity | where | defect |
|---|---|---|---|
| 1 | info (stale premise) + low | `myth-symbol/animal-symbolism.md:109` | Frontier premise is stale (bank row recoded R->C in round 55); residual gap: line names no evaluation and carries no stop rule |
| 2 | low | `myth-symbol/motif-index-usage.md:37` | F chapter glossed by non-motif block names; exemplar cell has no real IDs and misattributes blocks |
| 3 | low | `culture-material/masks-masquerade.md:105` | locator `film transcript ¶3` ambiguous (holds only if the credit line is skipped) and the source's hedge "more or less" is dropped — over-read of source strength |
| 4 | low | `culture-material/masks-masquerade.md:59` | locator `Our Masks Come Home page, ¶3` identifies nothing on the page (dangling ordinal) |
| 5 | low (nit, same class, not routed) | `culture-material/masks-masquerade.md:59` | locator `Potlatch page, ¶3` is a bare ordinal across five named sections |

## Item 1 — `corpus/knowledge/myth-symbol/animal-symbolism.md:109` (griffin–Protoceratops)

The routed claim ("the round-55 calibration bank files it R as an origin claim") is **stale**:

- The landed bank row is **C**: `corpus/knowledge/myth-symbol/monsters-hybrid-beings.md:174` reads `- **C — "griffins came from *Protoceratops* fossils."** ... Witton and Hing (2024) find the link uncompelling and call it an "ex post facto geomyth" (S343, Abstract). The published evaluation weighs against the thesis; do not state it as the griffin's origin.`
- The recode is recorded: `corpus/lessons/round-55.md:209` — "CriticCalibrationBank: griffin R->C; monere bounded to Latin word history; ...". The Frontier line `round-55.md:239` predates that recode.
- So "contested" at line 109 already agrees with the bank's C code. NO CHANGE is defensible on the routed ground.

Residual calibration gap: line 109 carries only "attractive, contested, not required by the literary record" — no named evaluation, no stop rule. The bank's evidence sentence and stop rule are the sourced qualification, and `verification/calibration-registry.md` §1 requires the claim-level qualification to travel alongside seeded notes. A reader of this file alone never learns that a detailed 2024 peer-reviewed evaluation weighs against the origin reading.

Recommended change (unique fragment; rest of the line unchanged):

- old: `— attractive, contested, not required by the literary record;`
- new: `— attractive, contested; the published 2024 evaluation (Witton and Hing) finds the link uncompelling, so it is a proposal, not the griffin's origin — the literary record does not require it;`

All three original elements survive; the evaluation and the bank's stop rule are added. Author-year style is kept (the file cites no S-ids). Source strength verified this session against the re-opened S343 PDF (quotes below); quote the p. 7 body text for the imagery date, never the Figure 2 caption (caption says "4th century BCE Mesopotamia" — the round-55 seats' internal-inconsistency caveat confirmed in the same text layer).

## Item 2 — `corpus/knowledge/myth-symbol/motif-index-usage.md:37` (chapter F)

The F row compresses the chapter to "fantastic places, beings, objects" and the exemplar cell names "fairyland / wonder-object block" — no real motif IDs, and both named blocks are sub-blocks only (fairyland is F200–F399, inside the creatures block; wonder objects are F700–F899). The chapter's own four blocks (General Synopsis, printed p. 31; both copies checked this session): F0—F199 Otherworld journeys; F200—F699 Marvelous creatures (F200–F399 fairies and elves, F400–F499 spirits and demons, F500–F599 remarkable persons, F600–F699 persons with extraordinary powers); F700—F899 Extraordinary places and things; F900—F1099 Extraordinary occurrences. The audits cell "liminal geography" misses that the largest block files marvelous beings, not places.

Recommended change (full line; verified byte-exact):

- old: `| F | Marvels: fantastic places, beings, objects | fairyland / wonder-object block | liminal geography |`
- new: `| F | Marvels: otherworld journeys, marvelous creatures, extraordinary places, things and occurrences | F200 Fairies (elves); F420 Water-spirits; F110 Journey to terrestrial otherworlds | marvelous beings; liminal geography |`

Exemplar IDs are real and were spot-checked this session against the ruthenia chapter text (`F200. Fairies (elves).`, `F420. Water-spirits.`; F110's full heading per the same page, quoted by round-55 ScoutMotifIndexMonsters NEW-2). Style matches the B row's "B11 Dragon". If the L1 wants a smaller cut, replacing only the exemplar cell with these three IDs clears the routed imprecision.

## Item 3 — `corpus/knowledge/culture-material/masks-masquerade.md:59` and `:105` (S254)

The corrected S254 anchor cell has **landed** (`corpus/SOURCES.md:283` now carries all six quotes including both Come Home locators), so these entry-side fixes align the entry with the row. Both target fragments are unique in the corpus (checked).

### 3a. Line 59, Come Home locator (finding 4)

The sentence "After repatriation each family decided where its regalia would be held" sits in the section RETURN OF THE COLLECTION, third paragraph (paragraph opens "The Kwakwaka'wakw were able to demonstrate that Indian Agent Halliday..." and carries "Each family decided where their regalia was to be held" — byte-verified this session). Counted at page level, ¶3 falls in an opening caption/video block; counted as film transcript, ¶3 is the "We did not have such a thing" paragraph. Either way the bare ¶3 identifies nothing.

- old: `(S254, Our Masks Come Home page, ¶3)`
- new: `(S254, Our Masks Come Home page, RETURN OF THE COLLECTION, para. 3)`

### 3b. Line 59, Potlatch-page locator (finding 5, nit)

`(S254, Potlatch page, ¶3; Contemporary Potlatch, ¶1)` — the first locator is a bare ordinal on a page with five named sections; the quoted sentence sits in the section the site titles `English Translation of Potlatch Means "To Give"`, third paragraph (paragraph opens "It is a time for pride - a time for showing the masks and dances owned by the Chief or host giving the potlatch." — byte-verified). Suggested:

- old: `(S254, Potlatch page, ¶3; Contemporary Potlatch, ¶1)`
- new: `(S254, Potlatch page, English Translation of Potlatch Means To Give, para. 3; CONTEMPORARY POTLATCH, para. 1)`

(Section name written without its inner straight quotes — the doubled-locator class ScoutAnchorFixes routing note 4 flags for Gate lines.) `(S254, Potlatch page, purposes)` resolves to the section the site titles PURPOSES OF THE POTLATCH; NO CHANGE acceptable, or tighten to `PURPOSES OF THE POTLATCH, second bullet, third sub-item` to match the anchor cell exactly. The entry's quote "the right to wear, use, and display certain regalia" is a contiguous prefix of the anchor's quote (tail dropped, nothing joined) — NO CHANGE.

### 3c. Line 105 (finding 3)

Page bytes: "The objects in the Potlatch Collection have been arranged in this big house space, more or less in the order that they would appear in a potlatch, and they're not in cases." The entry drops "more or less" (asserting an exactness the page does not claim) and cites "film transcript ¶3", which holds only if the credit line "Film: Barbara Cranmer" is not counted (the objects paragraph is the fourth block element, third transcript paragraph).

- old (full line): `- **Display as argument.** The U'mista Cultural Centre arranged its returned objects in potlatch order and not in cases (S254, Our Masks Come Home page, film transcript ¶3).`
- new (full line): `- **Display as argument.** The U'mista Cultural Centre arranged its returned objects more or less in the order they would appear in a potlatch, not in cases (S254, Our Masks Come Home page, film transcript, the paragraph beginning The objects in the Potlatch Collection).`

The new locator matches the landed anchor cell's wording character for character.

## Sources re-opened this session (ordinary means; access date 2026-10-22; all plain curl, no challenge met)

1. Witton, Mark P.; Hing, Richard A. 2024. "Did the horned dinosaur *Protoceratops* inspire the griffin?" *Interdisciplinary Science Reviews*, doi 10.1177/03080188241255543 — lane row S343.
   - url: https://pure.port.ac.uk/ws/portalfiles/portal/93218631/Did_the_horned_dinosaur_Protoceratops_inspire_the_griffin.pdf
   - route: direct plain request, HTTP 200, application/pdf, 5,505,793 bytes (same byte count the S343 row records); text layer read with pdftotext (poppler 26.08.0). The ﬁ ligature in the text layer is normalized to "griffin" in the quotes below.
   - quotes — Abstract: "it uncompelling. Not only does it ignore established histories of griffin art and myth"; Abstract: "Protoceratops fossils occur hundreds of kilometres from the nearest gold deposits, subverting suggestions"; p. 7, body text: "oldest griffin-like imagery of 4th millennium BCE Asia and Egypt"; Figure 2 caption (p. 6, not to be quoted for the date): "from 4th century BCE Mesopotamia".
2. U'mista Cultural Society, "Our Masks Come Home" page — part of lane row S254.
   - url: https://umistapotlatch.ca/nos_masques_come_home-our_masks_come_home-eng.php
   - route: direct plain request, HTTP 200, text/html; charset=UTF-8, 54,814 bytes (matches ScoutAnchorFixes' record byte for byte).
   - quotes — film transcript, objects paragraph: "have been arranged in this big house space, more or less in the order that they would appear in a potlatch"; RETURN OF THE COLLECTION, para. 3: "Each family decided where their regalia was to be held"; film transcript, preceding paragraph (shows the ¶3 ambiguity): "We did not have such a thing among our people. It is like a storage box".
3. U'mista Cultural Society, "Potlatch" page — part of lane row S254.
   - url: https://umistapotlatch.ca/potlatch-eng.php
   - route: direct plain request, HTTP 200, text/html; charset=UTF-8, 74,806 bytes (matches ScoutAnchorFixes' record byte for byte).
   - quotes — section `English Translation of Potlatch Means "To Give"`, para. 3: "It is a time for pride - a time for showing the masks and dances owned by the Chief or host giving the potlatch"; CONTEMPORARY POTLATCH, para. 1: "They are witnesses who are “paid” with gifts for acknowledging a family’s inheritance" (curly quotes are the page's own characters). Section headings PURPOSES OF THE POTLATCH and CONTEMPORARY POTLATCH observed as served.
4. Thompson, Motif-Index, ch. F full text (ruthenia.ru) — supports lane row S013's specimen copy.
   - url: https://www.ruthenia.ru/folklore/thompson/f.htm
   - route: direct plain request, HTTP 200, text/html; charset=windows-1251, 659,007 bytes; converted windows-1251 to UTF-8 with 4 invalid bytes skipped at OCR artifacts (same conversion route as round-55 ScoutMotifIndexMonsters).
   - quotes — chapter F entries: "F200. Fairies (elves)."; "F420. Water-spirits."; chapter F, detailed synopsis: "F200--F699. MARVELOUS" (block title continues "CREATURES"; the hyphenation and capitals are the copy's).
5. Thompson, Motif-Index vol. 1, General Synopsis, printed p. 31 (Wikisource proofread scan transcription) — the tier-A copy for range wording.
   - url: https://en.wikisource.org/wiki/Page:Thompson_Motif-Index_2nd_1.djvu/37
   - route: direct plain request, HTTP 200, 61,163 bytes.
   - quotes — F table: "F200—F699. Marvelous creatures"; "F900—F1099. Extraordinary occurrences"; the F0—F199 and F700—F899 rows observed as "Otherworld journeys" and "Extraordinary places and things" (leading ranges are set with the page's hidden alignment characters, so I quote only the clean rows).

## Residual risk and verification gaps

- Item 1's recommended edit is a strengthening, not a contradiction fix; if the L1 prefers strictly status-consistency, NO CHANGE on line 109 is defensible and the bank row remains the controlling qualification. I did not re-open Mayor 2000 or 2005 (Princeton pages) — the recommended wording attributes only the 2024 evaluation.
- The landed S254 anchor cell contains the section name `English Translation of Potlatch Means "To Give"` with inner straight quotes; harmless inside the table row, but any future copy into a `## Gate` line must de-quote (ScoutAnchorFixes routing note 4).
- I checked only the F row of the motif table; the B and G rows were confirmed by round-55 ScoutMotifIndexMonsters and were not re-audited.
- Unopened: umistapotlatch.ca's other exhibit pages (out of scope), the printed vol. 3 scan of the Motif-Index (archive.org lending flow; challenge met, not passed — same as round 55), HathiTrust full-view candidates for the Motif-Index.
- Unrun checks: no acceptance scripts, no sweep, no git/jj commands (none needed; every check was against current working-tree bytes).
