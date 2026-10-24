# ScoutRow04 — ROW-OPENING (claim C): S811, S812

Two registry rows opened for the medicine/healing register, under
`.ufo/waves/round-67/rows/ScoutRow04/`. Both verified live with curl on
2026-10-24, both carry resolvable `id_` wayback captures, both dedup-checked
against all 768 base live URLs in `corpus/SOURCES.md` and all wave fragments
in `.ufo/`.

## S811 — Egyptian medical papyri (scholarly source)

- **Source**: Hartsock & Halverson, "Lost in translation: the history of the
  Ebers Papyrus and Dr. Carl H. von Klein", *Journal of the Medical Library
  Association* 111(4), 2023, doi 10.5195/jmla.2023.1755 — PMC open access.
  Peer-reviewed (tier A), `paper` kind. Host `pmc.ncbi.nlm.nih.gov` (distinct
- Bullet RESTATE self-check (counter semantics: `ordered_hits(qw, bw)` —
  quote content words found in-order inside the bullet): `oldest, complete,
  ancient, healing` = 4 (>=3 ✓); `in_order_coverage(tw, bw)` = 0.00 (<0.80
  ✓); novel words `egypt, record, survives` ✓; max verbatim run 2 ✓;
  `teaches_echoes_quote` q_cov 0.25 (<0.80 ✓).
- **Live**: HTTP 200, quote verified in body text (abstract). No paywall.
- **Capture**: `20250227171945id_` (CDX status 200). NOTE: anonymous Save Page
  Now on this URL returned HTTP 523 today — the 2025-02-27 snapshot is the
  one recorded; the L1 should confirm the capture leg accepts it (CAPTURE
  only requires a `web.archive.org/web/<14>id_/` URL in the source cell).
- Anchor quote (15 body words): "one of the oldest and most complete
  contemporaneous perspectives on Ancient Egyptian healing practices".
- Bullet RESTATE self-check: in-order quote content words
  `oldest, complete, healing` (>=3 ✓); teaches coverage 0.00 (<0.80 ✓);
  novel word `egypt` ✓; no run >12 ✓.

## S812 — Galen / Alexandrian-Roman medical system (encyclopedia source)

- **Source**: Michael Boylan (Marymount University), "Galen", *Internet
  Encyclopedia of Philosophy* (peer-reviewed, ISSN 2161-0002). Tier A,
  `docs` kind (encyclopedia, matching existing convention). Host
  `iep.utm.edu` — fresh host, unique URL.
- **Live**: HTTP 200, quote verified in body text (§1 "Life"). No paywall,
  no redirects.
- **Capture**: `20261001114120id_` (fresh, 2026-10-01). Normalizes equal to
  live (trailing-slash drop only).
- Anchor quote (19 body words): "Galen traveled to Egypt (Alexandria) where
  he lived for perhaps five years (152-157)".
- Bullet RESTATE self-check: `ordered_hits(qw,bw)` = 4 (`galen, traveled,
  egypt, alexandria`); cov(tw in bw) 0.00; q_cov(teaches echo) 0.11; novel
  `trained, before, competing, crowded, medical, arena`; max verbatim run 4.

## Formatting hazard found (recorded for the L1 integrator)

The counter's `anchor_quote` regex matches the FIRST straight-quote `"…"`
or curly-quote "…" span in cell 5 — but my validation shows titles written
with straight quotes in cell 1 are safe because the regex is applied to
cell 5 only. HOWEVER titles in cell 1 written as `"Title"` still parse fine;
the existing convention (S779 etc.) uses curly quotes for titles and
straight quotes for the anchor in cell 5. **Both drafted rows follow that
convention** (curly titles, straight anchor). Any seat using straight-quote
titles inside the scope cell would break their own anchor extraction —
worth a spot-check across sibling rows before integration.

## RESTATE direction — earlier draft corrected

First-pass bullets were written for the wrong match direction
(bullet-words-in-quote). The counter measures `ordered_hits(qw, bw)` =
quote content words found in-order inside the bullet, plus a second check
`in_order_coverage(qw, tw)` = teaches cell must not echo >=80% of quote
words. Bullets rewritten to carry >=3 of the quote's content words;
re-validated against the counter code verbatim.

## C-APPEND vs Ca-D4 id conflict — resolved (L1 ruling)

CriticFrontier/ScribeGateRows flagged that accept-c APPEND bounds new ids
to S805-S828+S801-S804 while accept-ca D4 needs >=2 extra rejected rows
opened today. L1 resolution (IRC): no counter revision; per-claim lands
separation — C's receipt stamped at lands commit A_c (only S805-S828 over
base), Ca at later A_ca carrying S829+ rejects, S801-S804 land earlier.
Joint predicate is satisfiable as sequenced. My rows sit inside NEW_IDS —
unaffected; recorded here as a design finding for the ledger.

## Rejects (full reasons in rows/ScoutRow04/rejects.txt)

- nyam.org Edwin Smith papyrus page — HTTP 403 (WAF/bot block)
- metmuseum.org Met-publications Art of Medicine in Ancient Egypt — HTTP 429
- britannica.com/biography/Galen — HTTP 403
- ucl.ac.uk Digital Egypt medical tools — HTTP 403
- pmc.ncbi.nlm.nih.gov/articles/PMC3978985/ — wrong guess, off-topic
- nlm.nih.gov pubs/techbull Edwin Smith Turning the Pages — backup only
- ub.uni-leipzig.de papyrus-ebers — HTTP 404 (moved)

## Findings / dependencies for the wave

- Both live URLs verified unique vs base registry (768 live URLs extracted).
- No install needed; curl + python3 only. No pacman transactions attempted.
- Dependency: row files are drafts at `rows/ScoutRow04/row-S811.txt` and
  `row-S812.txt`; the entry scribe + L1 integrate into `corpus/SOURCES.md`
  and cite `(S811)`/`(S812)` in `medicine-healing-codes.md` using the
  BULLET= clauses (or equivalent RESTATE-passing text).

Report: .ufo/waves/round-67/w1/ScoutRow04.md
