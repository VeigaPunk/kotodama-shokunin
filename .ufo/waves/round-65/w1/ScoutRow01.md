# ScoutRow01 — row-opening evidence

Opened exactly S750 and S751 in the two row files under `rows/ScoutRow01/`.

- **S750 — high confidence for Culin's historical classification and framing.** The 1907 Bureau of American Ethnology text explicitly divides games into chance and dexterity, excludes chess-like pure skill/calculation, and claims the classes occur among all North American tribes; its introduction also excludes some unimplemented child amusements. The Smithsonian bitstream URL returned HTTP 403 to live curl on 2026-10-24. Its `20260403190714` Wayback capture returned HTTP 200 as plain-text OCR, and the same passage was confirmed in Internet Archive's downloadable OCR text (HTTP 200). Reopen via the archived text or IA OCR; do not treat Culin's broad historical framing as a statement about present-day Native games.
- **S751 — high confidence for the Penn Museum article's claims.** William B. Hafford's Spring 2018 *Expedition* article says Woolley found boards in royal tombs at Ur, a much later cuneiform tablet informs at least one version of play, and the game is a strategy race. The live PDF returned HTTP 200 on 2026-10-24; its `20241003150437` Wayback capture also returned HTTP 200. The article supports a version-specific reconstruction, not a uniquely settled rulebook for the earliest boards.

**URL uniqueness checks (before adding these rows):** exact Smithsonian bitstream URL — `grep` over `corpus/SOURCES.md` and existing `.ufo/waves/round-65/rows/` fragments: `No matches found`; exact Penn Museum PDF URL — same search scope: `No matches found`. No reject was needed. No tools were installed.

**Remaining limitation:** the Smithsonian live content route was not retrievable by curl; its archived OCR and an open IA OCR mirror provided the verified quotation. L1 should recheck that route/access note when integrating.
