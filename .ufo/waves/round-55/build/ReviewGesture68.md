# ReviewGesture68 — gesture entry line 68, S201 printed-page locators (round 55 carried item)

Seat: KotodamaR55.ReviewGesture68 (leaf; no dispatches, no background jobs). Date: 2026-10-22.
Axes (godspeed): calibration (the judged axis — the printed page each line-68 locator must name), verification coverage (all three line-68 locators plus the neighbouring rows and the S201 registry row), evidence quality (verbatim proof text, byte-exact corrected line).

Lanes bounds kept: only this report file written in the lane; the PDF landed in /tmp; no git/jj writes; no tool installs (system curl and poppler `pdftotext`/`pdfinfo` were already present).

## Route (source opened this session)

S201 row: `corpus/SOURCES.md:230`. URL opened by plain request (curl, ordinary means; no access control met):

- `https://www.uva.nl/binaries/content/documents/personalpages/p/f/r.pfau/profile-en/profile-en/uva:foldout%5B2%5D/cpitem%5B21%5D/asset` — HTTP 200, `application/pdf;charset=UTF-8`, 474,531 bytes, 20 pages.
- sha256 `89dde92d5f57774e1728ea21435f03f28108b399675ccdf72d141c19b9efb05a` (recorded so future rounds can detect a replaced file).
- Page furniture: "OUP UNCORRECTED PROOF", "MATHUR-Chapter 4 Response-Pageproof", "June 30, 2010 2:31 AM"; internal title `acprof-9780199732548-c04r.indd`.
- Folio mapping pinned from the pages' own footers: pdf p1 carries bare folio 144 (chapter start), pdf p2 → 145, pdf p3 → 146, pdf p4 → 147, pdf p5 → 148; i.e. printed folio = pdf page + 143.
- Byte size 474,531 matches the round-54 fetch record exactly, so this is the same proof file round-54 checked.

Method: `pdftotext` per page, whitespace-normalized substring search for every quoted fragment. No LSP server exists for markdown in this lane, so no definition/references/diagnostics checks were possible; all corpus sweeps are text-level (`grep` fallback) and the semantic ground truth is the direct PDF re-open above, which is the evidence of record.

## Ground truth in the opened proof (printed page of each quoted fragment)

| fragment (normalized text of the proof) | printed page |
|---|---|
| "Analyzing data from England (Northamptonshire) and Italy (Campania), Kendon (2004) and Kendon and Versante (2003)" | 146 (pdf p3) |
| "a speaker singles out an object which is to be attended to as a particular individual object" (Kendon 2004, 205) | 146 (pdf p3) |
| "the object being indicated is not itself the primary focus or topic of the discourse but is something that is linked to the topic" (Kendon 2004, 208) | **146** (pdf p3) |
| "a hierarchical system of pointing ("orienting behaviors") that distinguishes six different handshapes that are used for different purposes" + "the pointing handshapes distinguished by Wilkins include the "middle finger point" and the "wide hand point."" + allomorph note | **147** (pdf p4) |
| "the speaker then shifts the eye "noticeably within the socket toward a particular referent. There is typically no accompanying head movement" (Wilkins 2003, 187) | 147 (pdf p4) |
| "The use of eye pointing reflects a conspiratorial mood; it is used to exclude third parties from being privy to what or who is being talked about" | 147 (pdf p4) |
| lip-pointing spread ("attested in Southeast Asia (Enfield 2001), Australia (Wilkins 2003), Latin America (Sherzer 1973), and Africa") and its relation to manual pointing | 147 (pdf p4) |

## Verdict on line 68 (`corpus/knowledge/linguistics/gesture-co-speech-pointing.md:68`)

| locator on line 68 | proof | verdict |
|---|---|---|
| Northamptonshire/Campania Kendon data "(S201, p. 146 in the proof pagination)" | printed 146 | correct |
| Arrernte "wide hand point" among six handshapes "(S201, p. 147)" | printed 147 | correct |
| Kendon 2004, 208 quote "(as reported in S201, p. 147)" | printed **146** | **WRONG — revert to p. 146** |

Neighbours confirmed: line 67's Kendon 205 quote at "S201, p. 146" is correct (printed 146); line 72's two S201 quotes at "p. 147" are both correct (printed 147). A corpus-wide sweep for `S201, p. NNN` locators finds S201 page citations only in this entry (lines 67, 68, 72), so the corrected text below is the only landing site for the defective locator.

## Exact corrected line 68

Derived from the file's own bytes; the only difference from the current line is the single character `7` → `6` in the final locator. The curly quotes and apostrophes are the file's own:

```
| Whole hand (flat hand, fingers together) | Northamptonshire (England) and Campania (Italy), in Kendon’s index-hand and flat-hand data (S201, p. 146 in the proof pagination); Arrernte (central Australia) keep a “wide hand point” among six handshapes (S201, p. 147) | a referent linked to the topic rather than the topic itself: “the object being indicated is not itself the primary focus or topic of the discourse but is something that is linked to the topic” (Kendon 2004, 208, as reported in S201, p. 146) | give the flat hand a job the index finger does not do; a variant with no contrast of its own is a redundancy (**H**) |
```

Minimal edit for the L1: `(Kendon 2004, 208, as reported in S201, p. 147)` → `(Kendon 2004, 208, as reported in S201, p. 146)`. I did not apply it: reviewers do not edit; this is the carried routed item for the L1/executor to land. The entry's "as reported in S201" framing remains accurate — the proof prints the quote with its own citation "(Kendon 2004, 208)".

## Findings by severity

1. **MEDIUM — line 68's third locator mis-cited.** The Kendon 2004, 208 quote sits on printed p. 146 (pdf p3) of the opened proof, but line 68 says "as reported in S201, p. 147". This confirms the round-54 finding (.ufo/waves/round-54/build-a2/ReviewRoutedFixes.md, item 1). The corrected line above closes it with a one-character change. Note the round-53 lesson row `corpus/lessons/round-53.md:89` already had this quote at p. 146 — the p. 146 locator is both directly observed today and historically attested in the lane.
2. **LOW (carried from round 54, re-evidenced this session) — S201 row anchor cell still bounds the Wilkins inventory under the wrong pages.** `corpus/SOURCES.md:230` anchor cell reads "pp. 145–146 (…; Wilkins's six handshapes including the middle-finger point and the wide hand point) and p. 147 (…)", but the opened proof carries the six-handshape system, the "middle finger point"/"wide hand point" inventory and the allomorph note on printed p. 147 (pdf p4). The row's p. 147 group (lip-pointing spread, Arrernte eye-pointing) is correct. Registry rows below S285 are records, so the L1/row owner decides the landing; the ground cell (c) is otherwise carried.
3. **LOW (new this session) — two stale locators in `corpus/lessons/round-53.md`.** Line 88 cites the Northamptonshire/Campania sentence at "p. 145"; the proof carries it on printed p. 146. Line 90 cites the Wilkins "middle finger point"/"wide hand point" inventory at "p. 146"; the proof carries it on printed p. 147. Lines 89 and 91 of the same block are correct and corroborate today's folio mapping. These lesson rows mirror the pre-fix pagination; they are records, not claims, and no entry cites them.

## Residual risk and verification gaps

- All page assignments rest on one fetch of the uva.nl proof this session. Byte size (474,531) and stamps match the round-54 record, and the sha256 above pins the file; if it is ever replaced by a re-paginated version, all S201 locators (entry lines 67, 68, 72; SOURCES row 230; lessons round-53 block) need re-checking together.
- The underlying Kendon 2004 book (printed pp. 205, 208) was not opened; the entry cites the proof as the reporting locus ("as reported in S201"), which is the scope the row claims (tier B). Nothing on line 68 depends on Kendon's own pagination being verified.
- Unrun checks: none remaining in scope. The only executable follow-ups are the L1's landings of findings 1–3 and, at the next S201 re-check, a sha256 comparison against this report.
