# S730 row falsification review — B2ReviewRowS730

Draft reviewed: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS730/row.txt` (wave-1 inheritance, unverified).
Counter rules read: `reports/round-64/accept-c.py` legs ROWS (ll. 180–222) and RESTATE (ll. 268–314).

## HTTP results (verbatim)
- LIVE: `curl -sL --max-time 90` → `200 https://www.psych.mcgill.ca/perpg/fac/genesee/HDBK%20BFLA%20FINAL.pdf application/pdf 89735`
- CAPTURE (draft URL `…/web/20260406020611id_/…`): `200` after redirect → final `https://web.archive.org/web/20251104145417id_/https://www.psych.mcgill.ca/perpg/fac/genesee/HDBK%20BFLA%20FINAL.pdf` `application/pdf 89735`
- REAL timestamp probe `…/web/20251104145417id_/…`: `200`, serves itself; md5 identical to live body (`5a7725e9607ffd7fe2b6c3185b5e0c8b` all three).
- Wayback availability API: `429 Too Many Requests` (rate-limited; capture checked by direct fetch instead).

## Anchor quote location
Normalised (NFKC, casefold, non-word→space) search of pypdf-extracted text — quote found at norm index 133, contiguous, body text (chapter opening paragraph):
`…hdbk bfla sept 2005 1 bilingual first langauge acquisition1 fred genesee mcgill university and elena nicoladis university of alberta this chapter focuses on the simultaneous acquisition of two languages from birth or what is generally referred to as bilingual first language acquisition bfla a major question in studies of bfla…`
Not a heading/caption/alt/nav: it is the first sentence of the chapter body (PDF page 1, lines after author block).

## Lane locator (re-run)
`python3 -B reports/round-61/reopen-quote.py '<URL>' '<quote>'` → `LOCATED https://www.psych.mcgill.ca/perpg/fac/genesee/HDBK%20BFLA%20FINAL.pdf`

## Citation verification
Published record (Wiley Online Books, DOI 10.1002/9780470757833.ch16): Genesee, F., & Nicoladis, E. (2007). "Bilingual first language acquisition". In E. Hoff & M. Shatz (Eds.), *Blackwell Handbook of Language Development*, pp. 324–342. Draft says "2007", "Chapter 16, pp. 324–342" — all match the published record. Note: the hosted PDF is the Sept-2005 preprint manuscript; its own footnote cites the work in-press as "(2006). Bilingual acquisition" — expected for a preprint, not a citation defect.

## RESTATE arithmetic on BULLET
Clause: "Worldbuilders can model simultaneous acquisition of two languages from birth as an early dual-language path"
content words=10 (≥5 ✓), in-order quote hits=5 (≥3 ✓), novel content words={worldbuilders, model, dual, path, early} (≥1 ✓), longest verbatim run=7 (≤12 ✓). Clause asserts only what the quote establishes (simultaneous acquisition of two languages from birth = BFLA); no invented number.

## Verdict table

| field | draft value | verified? | evidence (verbatim) | required fix |
|---|---|---|---|---|
| cell count / shape | 11 cells, kind=book, status=mined, opened=2026-10-23, recheck=180d, used-by=entry path | YES | row line parses to exactly 11 cells; all ROWS-leg shape fields conform | none |
| live URL | `https://www.psych.mcgill.ca/perpg/fac/genesee/HDBK%20BFLA%20FINAL.pdf` | YES | `LIVE 200 … application/pdf 89735` | none |
| capture URL | `https://web.archive.org/web/20260406020611id_/…` | **NO** | timestamp 20260406020611 does not exist; Wayback redirects to nearest real capture `20251104145417` (`CAPTURE 200 … -> /web/20251104145417id_/…`). Bytes identical (md5 5a7725e9…), but the recorded timestamp is wrong/fabricated | replace timestamp with `20251104145417`: `https://web.archive.org/web/20251104145417id_/https://www.psych.mcgill.ca/perpg/fac/genesee/HDBK%20BFLA%20FINAL.pdf` |
| anchor locator+quote | `Chapter opening paragraph: "This chapter focuses on … (BFLA)."` | YES | verbatim contiguous in body text at norm idx 133; 24 normalised words (8–25 ✓); LOCATED by lane locator | none |
| citation (authors/year/title/venue/pages) | Fred Genesee & Elena Nicoladis, 2007, "Bilingual First Language Acquisition", Blackwell Handbook of Language Development, ch16 pp. 324–342 | YES | matches published record (Wiley ch16, DOI 10.1002/9780470757833.ch16); manuscript head: "BILINGUAL FIRST LANGAUGE ACQUISITION … Fred Genesee, McGill University and Elena Nicoladis, University of Alberta" | none |
| kind | book | YES | handbook chapter — book kind fits | none |
| tier | B for scope "simultaneous bilingual first-language acquisition from birth" | YES | review chapter surveying Ronjat 1913, Leopold 1949, Smith 1935 etc. — strong secondary by the field's leading experts; B correct (A would mean the scope's own primary/official record) | none |
| teaches cell | "Helps learners distinguish children's simultaneous acquisition of two languages from birth from later sequential second-language learning." | YES | consistent with quote and chapter content; ≤ cell, no `|` inside | none |
| BULLET vs quote | "Worldbuilders can model simultaneous acquisition of two languages from birth as an early dual-language path (S730)" | YES | RESTATE metrics pass (10 content words, 5 in-order, 5 novel, max run 7); no overreach — "from birth" ⇒ "early", dual-language path = BFLA | none |

VERDICT: FIX-REQUIRED capture timestamp 20260406020611 does not exist in Wayback (redirects to real capture 20251104145417); every other field verified clean.
