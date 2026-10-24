# ScoutRow10 — r66-v2 ROW-OPENING (claim C)

Deliverables written:
- `.ufo/waves/round-66/rows/ScoutRow10/row-S795.txt`
- `.ufo/waves/round-66/rows/ScoutRow10/row-S796.txt`
- `.ufo/waves/round-66/rows/ScoutRow10/rejects.txt` (6 candidates with flip conditions)

## S795 — incense clocks and timekeeping by burning (scholarly source)

**Opened:** Silvio A. Bedini, "The Scent of Time: A Study of the Use of Fire and Incense for Time Measurement in Oriental Countries," *Transactions of the American Philosophical Society* n.s. 53(5) (1963): 1–51, JSTOR stable 1005923 — the canonical scholarly study. Live URL is the archive.org-hosted scan of the JSTOR PDF (curl HTTP 200, 8.75 MB, application/pdf, 2026-10-24 11:38 GMT). Anchor quote: the Fang Kan poem Bedini translates in the incense-seal section — "By burning incense [we] know the passage of the night, With graduated candle [we] confirm the tally of the watches." Tier A. Scope ≤60 chars, teaches ≤240 chars.

**Honest gap:** no Wayback capture exists for the archive.org download URL and a fresh `/save/` attempt returned HTTP 523 (Wayback save service error). The row's CAPTURE field discloses this and instead cites the captured stable-ID leg (jstor.org/stable/1005923, capture 20251011060403, live HTTP 200). If the frozen predicate demands a capture of the cited URL itself, the L1 can either retry `/save/` later, swap the live URL to the JSTOR page (paywalled body — weakens the anchor), or substitute the SMG curator blog (see below).

**Pivot documented:** the intended museum object record, Science Museum Group co729 "Chinese Incense Clock," rate-limited (HTTP 429) on all 5 attempts across ~5 min including its JSON API — S252 shows this host intermittently 429s then serves 200. Seiko Museum pages 503 bot-block. CUP official excerpt PDF of *The Trail of Time* is live but image-only (no text layer). All listed in `rejects.txt` with flip conditions.

## S796 — perfume trade in the medieval Islamic city / souk perfumers (scholarly source)

**Opened:** Fanny Bessard, "The Politics of Sūqs in Early Islam," *JESHO* 61(4) (2018): 491–518, doi 10.1163/15685209-12341460 — University of Bristol repository author manuscript (live HTTP 200, application/pdf, 487,491 bytes, 2026-10-24 11:35 GMT). Anchor quote verified verbatim in the PDF: "designed them to function as a set of defined zones for various commodities and the streets took on the name of the trade plied there" — directly documenting 'aṭṭārīn (perfumer/fragrance-seller) market streets in early Islamic Wāsiṭ. Tier A (peer-reviewed JESHO). Wayback capture 20231119220323, status 200, normalizes equal to live URL (no query). No access restrictions.

## Uniqueness

Both live URLs grepped against `corpus/SOURCES.md`, `corpus/knowledge/culture-material/*.md`, and `.ufo/waves/round-66/rows/` — zero hits for the archive.org Bedini PDF and the Bristol repository URL. `cambridge.org` URLs exist in the registry but none match mine.

## Tooling

No installs needed (curl, pdftotext, python3 present). Nothing installed or updated this run.

## Remaining unknowns for the L1

- Whether the frozen predicate (or L1) requires a Wayback capture of the S795 cited URL itself — the archive.org host has none and `/save/` is erroring today.
- `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` does not yet exist on disk (ScribeEntrySpec's item); these rows point at it per spec.
- SMG co729 remains the superior S795 anchor if its rate-limit clears; retry once at integration time.

Report: .ufo/waves/round-66/w1/ScoutRow10.md
