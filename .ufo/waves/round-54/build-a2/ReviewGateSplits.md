# ReviewGateSplits — routed defect 3 (Gate text): split the joined quotes in `corpus/lessons/round-53.md`

Round 54, attempt 2, leaf seat. Scope: the seven Gate lines named by round-53 routed defect 3 and `corpus/lessons/round-53-verifier-spotcheck.md:175` — `round-53.md:84` (S200), `:109`, `:110`, `:111` (S205), `:128` (S214), `:160` (S224), `:181` (S236). All five sources re-opened this session, 2026-10-22, by ordinary means (plain curl; one Wayback capture after a challenge). No tools installed; pacman untouched.

## Routes used (per source)

- **S200** — `http://kensycooperrider.com/s/Cooperrider-Slotta-Nunez-2018-The-Preference-for-Pointing-With-the-Hand-Is-Not-Universal.pdf` → HTTP 302 → author-hosted copy at `https://static1.squarespace.com/static/56bb3f762b8dde105680b465/t/5a8362e471c10bfae93dcd39/1518559973507/...pdf`, HTTP 200, application/pdf. Text layer clean. Table 2 sits on printed p. 8 (page header `8   un~ez / Cognitive Science (2018)`); §3 Results opens on printed p. 7. Cross-checks: each table row sums to its total (234+8+252+104 = 598; 450+35+0+11 = 496), row percentages match the totals, and the body text agrees ("Manual pointing made up 40% of all Yupno pointing gestures", "Yupno = .88; United States = 1.00").
- **S205** — live `https://benjamins.com/catalog/gest.1.1.06kit` → HTTP 403, Cloudflare "Attention Required!" interstitial. **Challenge met, not passed.** Abstract read from the Wayback capture `20260106010024` (raw `id_` route, HTTP 200). The capture carries the full abstract verbatim, including the printed typo "peolple". It also shows the filed locators mis-numbered the abstract's sentences: the fragments filed as "sentences 1–2", "2–4" and "5–6" are actually sentences 1+3, 4+5 and 7+8 of the nine-sentence abstract.
- **S214** — `https://dingo.sbs.arizona.edu/~hharley/courses/PDF/TalmyLexicalizationPatterns.pdf`, HTTP 200, application/pdf, 47-page scan imaging two book pages per PDF page. OCR text layer garbled at the passage ("pattem", "&e verb"), so the passage was verified from a pdftoppm raster of the PDF page carrying the printed pp. 68–69 spread: the heading "1.2 *Motion + Path*" and the sentence are verbatim on printed p. 68, as the filed locator says.
- **S224** — `https://www.psu.edu/news/research/story/rainbow-bridge`, HTTP 200. Direct read.
- **S236** — `http://www.kaaj.com/psych/smorder.html`, HTTP 200. Direct read. The equation ends the "Inconsistent communications" bullet; the bolded note after the bullet list carries the scope sentence.

## Finding 1 (the routed defect, confirmed): seven lines join fragments/anchors so the quoted words per line reach 26–36

Per-line totals, each fragment counted with `printf '%s' … | wc -w` (whitespace tokenization):

| round-53.md line | joined fragments (old words) | line total |
|---|---|---|
| :84 S200 | Yupno row + United States row joined by " / " in one quote (22), plus the caption quoted in the locator (5) | 27 |
| :109 S205 | "In Ghana, many peolple …" (14) + "there is a politeness convention …" (22) | 36 |
| :110 S205 | "right-handed pointing may involve …" (16) + "pointing is sometimes performed …" (14) | 30 |
| :111 S205 | "Left-handed pointing gestures …" (13) + "Ghanaians do not consider …" (13) | 26 |
| :128 S214 | §-title "Motion + Path" quoted in the locator (3) + the sentence (24) | 27 |
| :160 S224 | anchor "That probably explains many cultures' fear" (6) + the quote (22) | 28 |
| :181 S236 | formula "Total Liking = 7% …" quoted in the locator (14) + the quote (15) | 29 |

## Finding 2 (new, same line): the S224 anchor is not a verbatim span

`round-53.md:160` anchors the paragraph with `"That probably explains many cultures' fear"`. The page reads: `That the rainbow does so "probably explains many cultures' fear" of it.` The filed anchor splices the story's "That" onto the Lee-and-Fraser quotation and drops "the rainbow does so", so it reproduces no contiguous span of the page. The replacement below quotes the whole first sentence instead.

## Finding 3 (adjacent, outside the routed set, no line proposed)

The non-offender line `round-53.md:86` locates Table 1 at "§1, p. 4"; in this copy the caption "Table 1 / Non-manual pointing conventions across cultures" and its rows (including Enga) sit on text page 3 (printed p. 3 by the same header rule that puts Table 2 on p. 8). Verified at text-layer level only — no raster check — so I record it as a question for the row's owner, not an erratum.

## Replacement Gate lines

Each quote below is a separate verbatim span of at most 25 words with its own locator. Counts are `wc -w`.

**R1 — replaces `round-53.md:84` (quotes: 10; 11)**

`- S200 — http://kensycooperrider.com/s/Cooperrider-Slotta-Nunez-2018-The-Preference-for-Pointing-With-the-Hand-Is-Not-Universal.pdf — accessed 2026-10-22 — §3 Results, p. 8, Table 2 (captioned Counts of pointing forms used), the Yupno row: "Yupno 234 (39%) 8 (1%) 252 (42%) 104 (17%) 598"; the same table's United States row: "United States 450 (91%) 35 (7%) 0 (0%) 11 (2%) 496". Grounds: the index-finger, chin/head and nose-pointing rows' community and count cells. Seat: ScribeSec04Pointing.`

**R2 — replaces `round-53.md:109` (quotes: 14; 23)**

`- S205 — https://benjamins.com/catalog/gest.1.1.06kit — accessed 2026-10-22 — abstract, sentence 1: "In Ghana, many peolple consider pointing by the left hand to be a taboo"; abstract, sentence 3: "First, there is a politeness convention to place the left hand on the lower back, as if to hide it from the interlocutor". Grounds: the Ghana left-hand restriction paragraph — tier B, publisher abstract only, article body not opened. (The publisher's abstract prints "peolple"; the quote is copied as printed. The live page now serves a Cloudflare challenge, met and not passed; this text was read from the Wayback capture 20260106010024.) Seat: ScribeSec04Pointing.`

**R3 — replaces `round-53.md:110` (quotes: 23; 15)**

`- S205 — https://benjamins.com/catalog/gest.1.1.06kit — accessed 2026-10-22 — abstract, sentence 4: "Second, as a consequence of left-hand suppression, right-handed pointing may involve an anatomically staining position when indicating a leftward direction across the body"; abstract, sentence 5: "Third, pointing is sometimes performed with both hands together, which does not violate the taboo". Grounds: the substitute and the escape hatch the Ghana taboo forces. (Same Cloudflare-challenge route and Wayback capture 20260106010024 as the line above.) Seat: ScribeSec04Pointing.`

**R4 — replaces `round-53.md:111` (quotes: 20; 13)**

`- S205 — https://benjamins.com/catalog/gest.1.1.06kit — accessed 2026-10-22 — abstract, sentence 7: "Left-handed pointing gestures occur in association with the verbalization of the concept LEFT, suggesting the embodied nature of the concept"; abstract, sentence 8, final clause: "Ghanaians do not consider them as pointing for the purpose of the taboo". Grounds: the claim that the taboo is a constraint on the system, not a prohibition. (Same Cloudflare-challenge route and Wayback capture 20260106010024.) Seat: ScribeSec04Pointing.`

**R5 — replaces `round-53.md:128` (quotes: 3; 24)**

`- S214 — https://dingo.sbs.arizona.edu/~hharley/courses/PDF/TalmyLexicalizationPatterns.pdf — accessed 2026-10-22 — printed p. 68, §1.2 heading: "Motion + Path"; printed p. 68, §1.2, first sentence: "In the second typological pattern for the expression of Motion, the verb root at once expresses both the fact of Motion and the Path". Grounds: the verb-framed pattern in the primary source; the satellite pattern is carried by S213, p. 220. Note: the copy's OCR text layer is unreliable, so both quotations were read from the rasterised printed page (the scan images two book pages per PDF page; this passage is on printed p. 68 of the pp. 68–69 spread). Seat: ScribeSec06Packaging.`

**R6 — replaces `round-53.md:160` (quotes: 12; 22)**

`- S224 — (S224) — https://www.psu.edu/news/research/story/rainbow-bridge — accessed 2026-10-22 — the paragraph quoting Lee and Fraser on the rainbow as personal, its first sentence: "That the rainbow does so "probably explains many cultures' fear" of it"; the same paragraph, the Lee and Fraser quotation: "In places as widely separated as Hungary, China, Mexico, and Gabon, pointing (or even looking) at a rainbow is a foolhardy act". Grounds: the university story's own quotation of Lee and Fraser's text. Seat: ScribeSec08Social.`

**R7 — replaces `round-53.md:181` (quotes: 14; 15)**

`- S236 — http://www.kaaj.com/psych/smorder.html — accessed 2026-10-22 — the equation ending the Inconsistent communications bullet: "Total Liking = 7% Verbal Liking + 38% Vocal Liking + 55% Facial Liking"; the bolded note after the bullet list: "Unless a communicator is talking about their feelings or attitudes, these equations are not applicable". Grounds: the 93% row — the author's own scope limit. Seat: ScribeSec12Calibration.`

Every replacement line's largest single quote is 24 words; the old per-line totals of 26–37 quoted words become separately-located quotes of 3–24 words each. (R2–R4 line sums stay above 25 because each line carries two quotes — the routed criterion is per-quote, with each fragment independently located and counted.)

## Erratum lines for the round-54 lesson (paste-ready)

```
- S200 (`round-53.md:84`): the Gate line joins the Yupno and United States rows of Table 2 into one 22-word quote (27 with the caption quoted in the locator). Re-opened 2026-10-22, direct route (HTTP 302 to the author's squarespace copy, then 200); rows cross-checked against the row totals. Replacement Gate line: - S200 — http://kensycooperrider.com/s/Cooperrider-Slotta-Nunez-2018-The-Preference-for-Pointing-With-the-Hand-Is-Not-Universal.pdf — accessed 2026-10-22 — §3 Results, p. 8, Table 2 (captioned Counts of pointing forms used), the Yupno row: "Yupno 234 (39%) 8 (1%) 252 (42%) 104 (17%) 598"; the same table's United States row: "United States 450 (91%) 35 (7%) 0 (0%) 11 (2%) 496". Grounds: the index-finger, chin/head and nose-pointing rows' community and count cells. Seat: ScribeSec04Pointing.
- S205 (`round-53.md:109`): the Gate line joins two abstract fragments into one 36-word quotation (14 + 22), and its "sentences 1–2" locator is wrong — the fragments are abstract sentences 1 and 3. The live page now serves a Cloudflare challenge, met and not passed; the abstract was read from the Wayback capture 20260106010024. Replacement Gate line: - S205 — https://benjamins.com/catalog/gest.1.1.06kit — accessed 2026-10-22 — abstract, sentence 1: "In Ghana, many peolple consider pointing by the left hand to be a taboo"; abstract, sentence 3: "First, there is a politeness convention to place the left hand on the lower back, as if to hide it from the interlocutor". Grounds: the Ghana left-hand restriction paragraph — tier B, publisher abstract only, article body not opened. (The publisher's abstract prints "peolple"; the quote is copied as printed.) Seat: ScribeSec04Pointing.
- S205 (`round-53.md:110`): the same joined-fragments defect (16 + 14 = 30 quoted words), and its "sentences 2–4" locator is wrong — the fragments are abstract sentences 4 and 5. Same Wayback route. Replacement Gate line: - S205 — https://benjamins.com/catalog/gest.1.1.06kit — accessed 2026-10-22 — abstract, sentence 4: "Second, as a consequence of left-hand suppression, right-handed pointing may involve an anatomically staining position when indicating a leftward direction across the body"; abstract, sentence 5: "Third, pointing is sometimes performed with both hands together, which does not violate the taboo". Grounds: the substitute and the escape hatch the Ghana taboo forces. (Live page: Cloudflare challenge, met and not passed; read from the Wayback capture 20260106010024.) Seat: ScribeSec04Pointing.
- S205 (`round-53.md:111`): the same joined-fragments defect (13 + 13 = 26 quoted words), and its "sentences 5–6" locator is wrong — the fragments are abstract sentence 7 and the final clause of sentence 8. Same Wayback route. Replacement Gate line: - S205 — https://benjamins.com/catalog/gest.1.1.06kit — accessed 2026-10-22 — abstract, sentence 7: "Left-handed pointing gestures occur in association with the verbalization of the concept LEFT, suggesting the embodied nature of the concept"; abstract, sentence 8, final clause: "Ghanaians do not consider them as pointing for the purpose of the taboo". Grounds: the claim that the taboo is a constraint on the system, not a prohibition. (Live page: Cloudflare challenge, met and not passed; read from the Wayback capture 20260106010024.) Seat: ScribeSec04Pointing.
- S214 (`round-53.md:128`): the Gate line quotes the §1.2 heading inside the locator and joins it to a 24-word quote (27 quoted words). Re-opened 2026-10-22, direct (HTTP 200); the passage verified on the rasterised printed page because the OCR layer is garbled. Replacement Gate line: - S214 — https://dingo.sbs.arizona.edu/~hharley/courses/PDF/TalmyLexicalizationPatterns.pdf — accessed 2026-10-22 — printed p. 68, §1.2 heading: "Motion + Path"; printed p. 68, §1.2, first sentence: "In the second typological pattern for the expression of Motion, the verb root at once expresses both the fact of Motion and the Path". Grounds: the verb-framed pattern in the primary source; the satellite pattern is carried by S213, p. 220. Note: the copy's OCR text layer is unreliable, so both quotations were read from the rasterised printed page (this passage is on printed p. 68 of the pp. 68–69 spread). Seat: ScribeSec06Packaging.
- S224 (`round-53.md:160`): two defects — the line joins a 6-word anchor to a 22-word quote (28), and the anchor "That probably explains many cultures' fear" is not a verbatim span: the page reads 'That the rainbow does so "probably explains many cultures' fear" of it'. Re-opened 2026-10-22, direct (HTTP 200). Replacement Gate line: - S224 — (S224) — https://www.psu.edu/news/research/story/rainbow-bridge — accessed 2026-10-22 — the paragraph quoting Lee and Fraser on the rainbow as personal, its first sentence: "That the rainbow does so "probably explains many cultures' fear" of it"; the same paragraph, the Lee and Fraser quotation: "In places as widely separated as Hungary, China, Mexico, and Gabon, pointing (or even looking) at a rainbow is a foolhardy act". Grounds: the university story's own quotation of Lee and Fraser's text. Seat: ScribeSec08Social.
- S236 (`round-53.md:181`): the Gate line quotes the Total Liking equation inside the locator and joins it to a 15-word quote (29 quoted words). Re-opened 2026-10-22, direct (HTTP 200); the equation ends the "Inconsistent communications" bullet and the scope sentence is the bolded note after the bullet list. Replacement Gate line: - S236 — http://www.kaaj.com/psych/smorder.html — accessed 2026-10-22 — the equation ending the Inconsistent communications bullet: "Total Liking = 7% Verbal Liking + 38% Vocal Liking + 55% Facial Liking"; the bolded note after the bullet list: "Unless a communicator is talking about their feelings or attitudes, these equations are not applicable". Grounds: the 93% row — the author's own scope limit. Seat: ScribeSec12Calibration.
```

## Word-count receipt (command output, `printf '%s' <quote> | wc -w` tokenization)

Old joined lines: 22 (S200 quote alone), 36 / 30 / 26 (S205 ×3), 28 (S214), 29 (S236) — the 26–36 band the spotcheck reports; adding S200's 5-word locator caption reaches 27.
New quotes, per replacement line — R1: 10, 11. R2: 14, 23. R3: 23, 15. R4: 20, 13. R5: 3, 24. R6: 12, 22. R7: 14, 15. `wc -w` was run directly on the four longest (23, 23, 24, 12) and the tokenizer equivalence checked on all fourteen.

## Verification gaps and checks not run

- S200 Table 2 verified from the text layer plus arithmetic and body-text cross-checks, not from a raster.
- S205's article body was not opened (paywalled); the rows stay tier B on the abstract. The Cloudflare challenge was met and not passed; no route around it except the public archival copy.
- S224's Lee and Fraser book itself was not opened — the story's quotations remain the evidence, as filed.
- The adjacent `round-53.md:86` "p. 4" locator question (Table 1 on printed p. 3 in this copy) is text-layer evidence only and is left to that line's owner.
- Evidence trail in scratch: `/fast/scratch/hyaku/kotodama-r54-a2/ReviewGateSplits/` (`s200.pdf`, `s200.txt`, `s205.html` (403 page), `s205-wb.html`, `s214.pdf`, `s214.txt`, `s214-p7.txt`, `s214-p7-07.png`, `s224.html`, `s236.html`).
