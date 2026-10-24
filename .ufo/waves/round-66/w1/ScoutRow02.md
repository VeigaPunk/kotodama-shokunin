# ScoutRow02 — S779, S780 (claim C, r66-v2)

Two row drafts written; sources verified by curl + Wayback this session.

## S779 — ancient Egyptian kyphi incense recipe
- **Source:** Lise Manniche, “Perfume”, *UCLA Encyclopedia of Egyptology* (2009), UC eScholarship — tier A (peer-reviewed encyclopedia, named Egyptologist author).
- **Live URL:** `https://escholarship.org/content/qt0pb1r0w3/qt0pb1r0w3.pdf` — curl HTTP 200, `application/pdf`, 588,894 bytes, 9 pages **with a browser user-agent**; bare curl gets HTTP 202 + empty body (CDN throttle, not a challenge).
- **Capture:** `20231015204944id_` — fetched and byte-identical to the live PDF (588,894 bytes). A `/save/` trigger today 302'd without producing a capture; the existing one is verified complete.
- **Anchor quote** (PDF p. 3, verified via pdftotext): “The most famous of all scents was kyphi, known from three versions on temple walls (two at Edfu, one at Philae), from papyri (P. Ebers)”.
- Bonus facts for the L1: kyphi = Greek of Egyptian *kapet* “a substance to be smoked”; ~16 ingredients on a raisin base; quoted by Galen/Dioscorides/Plutarch; Manniche warns “any claim to authenticity would stumble over lexicographical hurdles”; also argues the Edfu “laboratory” was likely a storeroom (light/ventilation argument).

## S780 — frankincense and myrrh production/trade
- **Source:** Dept. of Ancient Near Eastern Art, The Met, “Trade between Arabia and the Empires of Rome and Asia”, *Heilbrunn Timeline of Art History* (Oct. 2000) — tier A (museum curatorial essay; matches registry precedent accepting Met text as A).
- **Live URL:** `https://www.metmuseum.org/essays/trade-between-arabia-and-the-empires-of-rome-and-asia` — live host answers HTTP 429 (Vercel Security Checkpoint) to plain curl AND browser-UA curl: **challenge met, not passed** (known metmuseum.org behavior; ~20 prior registry rows record the same).
- **Capture:** `20260311081454id_` — HTTP 200, 120,339 bytes, full essay read. Fresh `/save/` attempt returned 523 (Met blocks the crawler live).
- **Anchor quote** (verified verbatim in captured body): “The Incense Route ran along the western edge of Arabia’s central desert about 100 miles inland from the Red Sea coast”.
- Bonus facts: Incense Route ran Shabwah (Hadhramaut)→Gaza; Pliny’s 65-stage caravan; Strabo’s army-size traffic comparison; cargo beyond resins (gold, ivory, spices, textiles from Africa/India/Far East).

## URL uniqueness
Both live URLs grep-clean against `corpus/SOURCES.md` (S001–S776) and all `.ufo/waves/round-66/rows/` siblings currently present — no S779/S780 rows existed yet and no sibling used either URL.

## Constraint checks (self-audit vs accept-c.py)
- 11 cells, kind∈{paper,docs}, tier A, mined, opened 2026-10-24, used-by = entry path. Teaches cells ≤240 chars. Quotes 8–25 words.
- Bullets: ≥3 in-order quote words, <80% in-order coverage of teaches, ≥1 novel word, no >12-word copied run — hand-counted.

## Artifacts
- `.ufo/waves/round-66/rows/ScoutRow02/row-S779.txt`
- `.ufo/waves/round-66/rows/ScoutRow02/row-S780.txt`
- No rejects file (both first-choice sources survived); rejects noted inline would be the alternatives I dropped: Lapham’s Quarterly frankincense essay (not clearly scholarly-tier), commercial/Scribd kyphi recipe pages (below tier B).

## Tooling
No installs. Used existing `curl`, `pdftotext`, `file`.
