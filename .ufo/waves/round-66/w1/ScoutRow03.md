# ScoutRow03 — r66-v2 row-opening (claim C)

Scoped rows: **S781**, **S782** for `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md`.

## Observed facts

**S781 — perfume in ancient Greece/Rome (olive-oil base + unguentaria-class vessels).**
Source: Lucie Mackintosh, "The Scent of Status: Perfume and Scented Oils in Ancient Greece," in *Dress and Adornment in Ancient Greece* (Brock University / eCampusOntario Pressbooks, 2025). Tier B (university OER, named student author, scholarly apparatus — same tier precedent as Cleveland State pressbooks entries already cited in `corpus/knowledge/civilizations/igbo.md`).
- Live: `https://ecampusontario.pressbooks.pub/dressandadornmentancientgreece/chapter/perfume-and-scented-oils/` — curl 200, 2026-10-24, 93.5 KB, no redirect/login.
- Anchor verbatim in body: "Beyond its culinary uses, olive oil served as the base for perfumes, cosmetics, and medicines".
- Chapter also names and contextualizes alabastron, aryballos (athlete + strigil scene), lekythos, plemochoe, amphoriskos; gendered scent choices (men: rose/lily, women: myrrh/spikenard, Theophr. *Sens.* 10.42); status framing.
- Wayback capture 200 + anchor-verbatim: `20260511112644id_/`.
- Uniqueness grep: URL/domain absent from `corpus/SOURCES.md` and all corpus fragments (only an unrelated kstatelibraries pressbook exists).

**S782 — medieval Islamic rosewater/attar distillation (Ibn Sina calibration).**
Source: Encyclopaedia Iranica, "ʿAṬR" (perfume), Vol. III, Fasc. 8, pp. 821–24. Tier A (reference encyclopedia; Iranica already cited repeatedly in the corpus).
- Live: `https://www.iranicaonline.org/articles/atr-perfume/` — curl 200, 2026-10-24, 377 KB, no redirect.
- Anchor verbatim: "large quantities of rose-water were regularly distilled in Persia and Iraq at least from the ninth century" — i.e., documented rosewater distillation *predates* Ibn Sina (d. 1037).
- Same article: distillation apparatus described by Jāber b. Ḥayyān (8th c.), al-Kendī (~873), al-Zahrāwī (~1013); attar proper (separated rose essential oil, `gol-ʿaṭr`/otto) dated to Jahāngīr's Mughal court 1611–12 — two independent calibrations of the popular "Avicenna invented attar/rosewater" claim.
- Wayback capture 200 + anchor-verbatim: `20251125160314id_/`. Note: `id_` body is served gzip-compressed; decode before grepping.
- Uniqueness grep: `/articles/atr-perfume/` absent everywhere in registry; only other iranicaonline.org articles exist.

## Files written
- `.ufo/waves/round-66/rows/ScoutRow03/row-S781.txt`
- `.ufo/waves/round-66/rows/ScoutRow03/row-S782.txt`
- `.ufo/waves/round-66/rows/ScoutRow03/rejects.txt` (2 rejects: metmuseum.org/essays/roman-glass — 429 + wrong scope; wikipedia.org/wiki/Golabgiri — below tier bar)

## Inference / residual gaps
- The Brock chapter covers Greece primarily; Roman content enters via its vessel typology. I put unguentaria in the teaches cell rather than the anchor; a Rome-first overview (Met "Roman Glass") exists but was 429 at fetch time — recorded in rejects.txt for a re-opener.
- "mined | 2026-10-24 | 180d" fields filled per the frozen row template; the entry file `scent-perfume-aromatics-codes.md` does not yet exist on the tip (owned by another seat) — dependency noted, not a blocker.
- Confidence: high on both rows (quotes, live status, and captures all verified byte-level, not from search snippets).

## Tools
No installs needed; stock curl/python3 sufficient (pacman guard respected).
