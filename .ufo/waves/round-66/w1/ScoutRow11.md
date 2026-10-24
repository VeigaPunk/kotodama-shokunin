# ScoutRow11 — round 66, claim C rows S797 + S798

## Outcome
- `rows/ScoutRow11/row-S797.txt` — Pliny, *Natural History* XIII.2, Bostock & Riley trans., Perseus Digital Library (tier A, kind book). Quote verbatim: "In later times Phoenicia eclipsed Egypt in the manufacture of these last two, but left to that country the repute of producing the best unguent of cyprus." Live HTTP 200 (665,664 B); capture 20260127095527 (HTTP 200, quote present). Single page carries both scope legs: Phoenicia/Cyprus/Sidon vs Egypt's Mendes/metopium.
- `rows/ScoutRow11/row-S798.txt` — ANU Classics Museum catalogue object 1963.02 "Corinthian Alabastron" (tier B, kind docs). Quote verbatim: "The alabastron was a shape introduced into Corinthian pottery from the east in the mid-seventh century and was used as a flask for perfume or perfumed oils." Page also states it "was displaced in the sixth by the globular aryballos" — both vessel names on one museum page. Live HTTP 200 (23,114 B); capture 20250421121114 fetched HTTP 200 with quote confirmed.
- `rows/ScoutRow11/rejects.txt` — 8 rejected candidates with reasons + flips (incl. Manniche UEE duplicating sibling S779, Met 429, BM/UCL/Kelsey 403, BMCR and Manchester Egypt-only-vs-scope failures).

## Verification performed
- Live curls (browser UA where needed): Perseus 200, ANU 200 — quotes extracted from raw HTML and matched verbatim (Phoenicia ligature "Phœnicia" preserved in quote text; footnote `<sup>` tags sit inline but do not split the sentence).
- Wayback: availability API → ANU 20250421121114 (200), Perseus ch2 20260127095527 (200); both capture bodies fetched and grep-confirmed for the quote strings.
- Uniqueness: `grep` over `corpus/SOURCES.md` (701 rows) and all `round-66/rows/*/row-*.txt` — neither live URL appears elsewhere. Perseus `?doc=` URL shape matches precedent S242/S311 (Bostock & Riley, tier A).
- Every field in the ROW template populated; BULLETs checked for <80% token overlap vs teaches cell, ≥1 novel word, ≥3 in-order quote words, no >12-word run.

## Noted for the integrator
- Fresh `/save` on ANU hit a transient archive.org 520 (six prior captures exist, latest 20250421, verified); fresh `/save` on Perseus ch2 timed out client-side but capture index still resolves. If the validator demands a fresher capture, one retry of `/save` may be needed.
- `web.archive.org/web/…id_/` returns a 403 block page to this host for `penelope.uchicago.edu` (rejected; not used).
- No tool installs needed. pacman untouched per pause order.
