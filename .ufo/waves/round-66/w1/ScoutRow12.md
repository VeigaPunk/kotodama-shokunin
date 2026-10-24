# ScoutRow12 — ROW-OPENING (claim C): S799 + S800

Deliverables written:
- `.ufo/waves/round-66/rows/ScoutRow12/row-S799.txt`
- `.ufo/waves/round-66/rows/ScoutRow12/row-S800.txt`
- `.ufo/waves/round-66/rows/ScoutRow12/rejects.txt` (8 rejected candidates with flip conditions)

## S799 — Edo-period incense games (kodo/kumiko)
**Landed:** Kyoto National Museum KNM Collection Database, "Incense Game Set with Cranes and Pines" (HK239), `https://knmdb.kyohaku.go.jp/eng/30115.html` — kind `docs`, tier **B** (official national-museum object record, not peer-reviewed).
- Live: curl -L HTTP 200, 2026-10-24; quote "In these games, over several rounds, a host selects varieties of incense for their guests to savor and identify." (19 words) verified verbatim in body text; record dated Japan-Edo-Mid / 18th c.
- Capture: fresh `/save` trigger 2026-10-24 → `20261024113446`; `id_` capture fetched (HTTP 200) and quote re-verified inside capture. Original URL normalizes equal to live.
- Host unique in corpus (knmdb.kyohaku.go.jp absent from SOURCES.md and all round-66 fragments on disk at time of writing).
- Note: the page does not use the words "kumiko"/"jushuko" in English; it documents the host-selects/guest-identifies incense-game mechanic on a mid-Edo set. The rejected TNM exhibition page explicitly defines "kumiko, a game of guessing combinations of incense wood" if the entry needs the term itself (see rejects; kept off the row only because the Kyoto object record is the tighter single-artifact citation).

## S800 — perfume workshop at Herculaneum
**Landed:** Bryn Mawr Classical Review 2013.04.46 (review of Monteix, *Les lieux de métier: boutiques et ateliers d'Herculanum*), `https://bmcr.brynmawr.edu/2013/2013.04.46/` — kind `paper`, tier **A** (peer-reviewed scholarly review journal).
- Live: curl -L HTTP 200, 2026-10-24; quote "it was an oil press for the production of perfume and not a textile press" (15 words) verified verbatim — Monteix reexamined the press in Herculaneum workshop III.10.
- Capture: `20250729161944id_` (pre-existing, fetched HTTP 200, verified). Fresh `/save` attempted twice 2026-10-24; web.archive.org timed out both times — the older capture was retained and its content verified. Re-opener should retry a fresh save for durability.
- Host unique in corpus.
- Caveat for the writer: the perfume identification is Monteix's **reinterpretation** (reported via the review), not the room's original label ("Bottega del Lanarius"); teaches cell and bullet are phrased accordingly — do not overstate as a signed perfumery.

## Uniqueness / format checks performed
- Both live URLs greped against `corpus/SOURCES.md` (exact-path match: absent) and against all fragments present under `.ufo/waves/round-66/rows/` (none existed at write time — sibling scouts may add rows later; L1 should re-run the LINK check).
- Rows: 11 cells each; tier A/B only; status `mined`; opened `2026-10-24`; used-by names the entry. Scopes ≤60 chars; quotes 8–25 body words; bullets carry ≥3 in-order quote words, <80% teaches coverage, ≥1 novel word.
- Two distinct hosts (knmdb.kyohaku.go.jp, bmcr.brynmawr.edu) contributing to the ≥10-host leg.

## Rejects summary
Met Heilbrunn "Japanese Incense" essay and Met jisshuko-bako object page (HTTP 429 all UAs), Cambridge Core JRAS Horiguchi & Jung article (HTTP 429), JSTOR stable 43307645 (JS client challenge), British Museum object A_1912-1012-21 (403), CORE PDF 196730672 (403), wordpress mirror of Brun AJA 2000 (unofficial host), herculaneum.uk III.10 record (non-tier host). Full flip conditions in `rejects.txt`.

## Environment / tools
No installs performed. curl (system) + python3 stdlib for text extraction; web.archive.org `/save` and `/available` endpoints used for captures.
