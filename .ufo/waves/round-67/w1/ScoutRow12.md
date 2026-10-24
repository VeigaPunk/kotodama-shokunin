# ScoutRow12 — row-opening, claim C (S827, S828)

Two rows opened for `corpus/knowledge/culture-material/medicine-healing-codes.md`. Drafts at `.ufo/waves/round-67/rows/ScoutRow12/row-S827.txt`, `row-S828.txt`; evaluated/rejected URLs in `rejects.txt`.

## S827 — plague consilium / medical-advice literature (tier A, kind book)
- Hecker, *The Black Death in the Fourteenth Century*, trans. Babington, London 1833, Project Gutenberg #52413, chapter "The Physicians". Live `https://www.gutenberg.org/files/52413/52413-h/52413-h.htm` → 200, 303,805 B (2026-10-24); quote verified verbatim in fetched text.
- Capture `web.archive.org/web/20250607152037id_/…` → 200, identical bytes; normalized equal to live. CDX also lists 20251223150659 (revisit) and 20260221184152.
- Anchor: "medical faculty of Paris, the most celebrated of the 14th century, were commissioned to deliver their opinion on the causes of the Black Plague" (24 words; verified substring). The chapter prints the Paris Consilium's celestial-cause preamble and its conduct/diet regimen — directly the medical-advice-literature genre.
- Uniqueness: URL absent from corpus/SOURCES.md (5 gutenberg.org rows exist, all other ebooks).

## S828 — amulet materia of protection (tier A, kind docs)
- Pitt Rivers Museum (Univ. Oxford), "England: The Other Within" — Imogen Crawford-Mowday, "Caul: A Sailor's Charm" (objects 1917.14.33, 1907.1.13). Live `https://england.prm.ox.ac.uk/englishness-sailors-charm.html` → 200, 18,514 B; quote verified verbatim.
- No prior capture existed; minted via SPN → `web.archive.org/web/20261024124257id_/…` → 200, 18,514 B, quote present; normalized equal to live.
- Anchor: "In Iceland the guardian spirit of a child was supposed to reside in the caul, which was carefully preserved after birth and kept" (23 words) — body-derived protective materia; page also records caul prices rising under submarine peril (1/6 → £2+), oracular use, and the rolling-pin carrier object.
- Uniqueness: absent from SOURCES.md; sibling PRM amulet rows (S641, S401) use different URLs/hosts.

## Constraint conformance (simulated vs accept-c.py tokenization)
- S827: in-order quote words in bullet 4 (≥3); teaches coverage 0.38 (<0.8); novel words present; quote→teaches 0.27; bullet 21 words; max verbatim run 2.
- S828: in-order 4; teaches coverage 0.14; novel present; q→t 0.31; bullet 19 words.
- Both rows: 11 cells, kind/tier/mined/2026-10-24/180d/used-by match ROWS leg; live URL + id_ capture pair satisfies CAPTURE.

## Rejects (see rejects.txt)
Singer "Some Plague Tractates" PMC2017705 (chrome-only landing, JS-gated PDF, archive.org OCR 500s); SMG Journal amulets article (dup of S642); SMG collection search (429); two archive.org `_djvu.txt` Hecker URLs (live fine but SPN 523-refuses archive.org/download — no capture obtainable).

## Findings / gaps for L1
- Wayback SPN currently refuses `archive.org/download/*` URLs (523 "valid web address") — other seats mining archive.org scans should check whether their capture chain works or pick Wayback-friendly mirrors (Gutenberg HTML worked).
- `rows/` and `w1/` were empty on arrival; no sibling fragment files existed to grep for URL uniqueness — LINK check was run against corpus/SOURCES.md only.
- Install log: none needed (curl/python3 sufficient).

Report: .ufo/waves/round-67/w1/ScoutRow12.md
