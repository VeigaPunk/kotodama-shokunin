# ScoutReject01 — S801 "cosmetics in the ancient world" (lead: museum survey)

**Decision: ADMIT.** Row written: `.ufo/waves/round-66/rows/ScoutReject01/row-S801.txt`.

## Source
Kenneth D. Matthews, Jr., "Saffron and Swan's Grease," *Expedition* 5(4), Penn Museum, 1963 — a museum survey article on ancient beauty preparations (Roman perfumer Cosmus, Subura shops, Plinian recipes). Live `https://www.penn.museum/sites/expedition/saffron-and-swans-grease/` returned HTTP 200 text/html, 45,869 bytes, direct GET, no redirect, no challenge, to plain curl on 2026-10-24. Wayback capture `20250826123925id_` fetched at HTTP 200 and contains the anchor quote verbatim; the captured original query-normalizes equal to the live URL. Full text also on the HTML page (not teaser-only).

## Why admit despite RevLoreHandoff MED-5
MED-5 is factually correct: `adornment-body-codes.md:68-75` (§6) already owns the cosmetics-vocabulary field (kosmein/kuḥl etymologies, cerussa/fucus pair, moral-register slurs). But this source's usable content sits in the **scent register**, not §6's lexicon territory: the anchor is Pliny's incense/nitre/myrrh/frankincense facial-cream recipe, and the row's teaches cell is scoped to perfumer's craft and aroma-fixative practice (resin making a hair unguent's scent "more permanent"). Scope and bullet deliberately avoid the etymology/moral-slur material §6 covers. Ranked risk for the L1: the entry bullet must stay on the recipe/economy side, never on "kohl/lead/cosmetic palette" facts — those are §6's.

## Tier/kind precedent
`paper | B` matches registry precedent for Penn *Expedition* magazine articles (S753, S751). Host `penn.museum` already in registry (S259, S751, S753); URL itself is unique — grepped against `corpus/SOURCES.md` and all round-65/66 row fragments: zero collisions. ID S801 not present anywhere in the repo.

## Alternates surveyed and passed over
- Met object 543963 (Bes kohl tube): tier A but live 429 to curl; content duplicates adornment §6 Egypt bullet (galena+malachite palettes) more directly — weaker on the MED-5 axis.
- IDB "Timeless Beauty" catalogue (IDB Cultural Center museum survey): live 403 to curl; capture PDF is image-only (no text layer to verify quotes).
- Met Journal v53 PDF: live 200 but serves an Incapsula HTML challenge, not the PDF.
- worldhistory.org article/1441: live 200, but encyclopedia (not museum) and mostly general-cosmetics scope → §6 duplication risk without tier-A payoff.
- MDPI *Cosmetics* 10(3):71: 403 to curl even with browser UA.

## Constraints honored
Anchor 21 body words; teaches cell ~230 chars; bullet 6–25 content words, ≥3 in-order quote words ("Pliny", "incense", "cream", "myrrh"), novel words ("pounded", "pricey", "Empire's"), teaches coverage <80%. No captures fabricated — both the Penn capture and the PDF sibling capture were fetched and read.

No tool installs needed. Time-box kept.


## UPDATE — RevLoreHandoff cross-check (incorporated)
- Peer measured the drafted bullet against accept-c.py helpers: in-order-quote-words=4, teaches_cov≈0.00, novel=10 — RESTATE passes with margin. Row shape: 11 cells, `paper`∈KINDS, tier B, mined, 2026-10-24, used-by=scent entry, 14-digit capture — all clean.
- KEY MECHANICAL FACT: `NEW_IDS = range(777,801)` (accept-c.py:50) → SET/ROWS/ONEID/RESTATE/HOSTS/LINK never read S801; APPEND only checks old-row preservation. **S801 lands undetected — wrong tier/date or zero citations would be invisible to the counter.** The admit decision is real only if the L1 executes the registration + citation by hand.
- Bullet revised per peer: attribution now "Matthews (1963) quotes Pliny's..." (later compiler citing primary, not Pliny-as-source); "pricey" hedged to "luxury" since trade-economy-lexicon.md owns exchange vocabulary.
- L1 registration conditions (peer's four, all REQUIRED, else reject this row at integration): (1) lesson declares S801 an extra row OUTSIDE the claimed 24; (2) entry cites S801 exactly once — if registered uncited, its used-by cell is false and no leg catches it; (3) bullet stays on aromatic materials/recipe/preparation (incense, nitre, myrrh, frankincense, resin seal) — no kohl/lead/cerussa/fucus body-code content, no Subura institution, no price vocabulary; (4) stage/entry-spec.md §12 (:214-231) boundary bullets — the `adornment-body-codes.md` §6 one is MANDATORY (currently missing) since the accepted bullet now contains the word "cosmetics"; the `trade-economy-lexicon.md` bullet only needs to survive the L1's edit; vessel-container-lexicon.md (:38 already owns "cosmetic/perfume (alabastron, aryballos)") likewise.
- Final measured numbers (peer, against the row cell): in-order quote words=4 (pliny/cream/incense/nitre), teaches coverage=0.037, novel=10 — RESTATE margin unchanged. Accepted bullet text is mirrored in RevLoreHandoff.md's S801 delta subsection for the audit trail.
- Peer close-out context (RevLoreHandoff HIGH-A): §12 is missing boundary bullets beyond S801's needs — `timekeeping-instruments.md:26` (S795 incense clocks), `vessel-container-lexicon.md:38` (S798), `games-play-sport-contests.md` (S799 kōdō), `fire-fuel-light.md:62` — and HIGH-2 formalizes the NEW_IDS blind spot as structural. The spec file `stage/entry-spec.md` (137 lines, 13 H2) carries §12 at :210 and §13 at :232; the entry itself was still ABSENT at their final check — S801's registration depends on the L1 landing it by hand.

