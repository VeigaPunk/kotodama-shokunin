# ScoutRow06 — row-opening findings

Opened the requested drafts:
- `.ufo/waves/round-65/rows/ScoutRow06/row-S760.txt`
- `.ufo/waves/round-65/rows/ScoutRow06/row-S761.txt`

**S760 — ancient Olympic amateurism calibration (B, docs).** KU Leuven’s *Ancient Olympics* page, “Amateurism” (©2012), states: “Today historians no longer think that the Greek athletes were amateurs.” I fetched the live HTTP URL with `curl -L` on 2026-10-24 (200; final URL unchanged) and saw the quote in the response body. Wayback CDX listed `20170213085029` as a 200 capture for the same original URL; opening that capture showed the quote. This is a university secondary overview, not a primary source.

**S761 — Maya ballgame court, equipment, and civic roles (B, docs).** The Hudson Museum, University of Maine, “Ballgame” page (modified 2025-06-27), states: “The ancient Maya ballgame called pitz was part of Maya political, religious, and social life.” The live HTTPS URL returned curl 200 on 2026-10-24 (final URL unchanged); the quote appears in the fetched body. The body also discusses courts, protective gear, and ritual context. Wayback CDX listed `20250814211934` as a 200 capture for the same original URL; the opened capture contains the quoted sentence.

**Uniqueness grep.** S760’s live URL: no match in `corpus/SOURCES.md`; round-65 row-fragment search found only `row-S760.txt` (live URL plus its required capture original). S761’s live URL: no match in `corpus/SOURCES.md`; round-65 row-fragment search found only `row-S761.txt` (live URL plus its required capture original). No other row fragment matched either URL.

**Rejected candidates.** Smithsonian NMAI (403), Met essay (429), and Library of Congress exhibit page (403) could not be independently verified from ordinary curl requests. Reasons and reopen conditions are recorded in `rows/ScoutRow06/rejects.txt`.

**Remaining limits.** KU Leuven’s page does not identify an individual author or cite its historical assertion on-page; keep the row scoped to the page’s amateurism calibration. Hudson Museum is a secondary overview; the row’s bullet stays with its broad political/religious/social characterization rather than asserting a universal Mesoamerican rule.