# ScoutRow02 — claim C rows S752–S753

## Opened
- `rows/ScoutRow02/row-S752.txt`: Peter A. Piccione, “In Search of the Meaning of Senet,” *Archaeology* 33 (July/August 1980), tier B. Its specialist account supports New Kingdom funerary interpretation while distinguishing tomb-made boards from continuing secular play.
- `rows/ScoutRow02/row-S753.txt`: Kristen Pearson, “Sowing the Seeds of Competitive Play: The Enduring Legacy of Mancala,” *Expedition* 58(1) (Spring 2016), tier B. The Penn Museum article covers the Africa/Asia distribution, variable boards, and sowing mechanic.
- Both anchor quotes appear in the live PDFs' extracted body text. No rejects; no tool installed.

## Verification evidence
- S752 live `curl -L`: HTTP 200, `Date: Sat, 24 Oct 2026 04:52:12 GMT`, zero redirects. CDX returned capture `20240613084025`, original `https://piccionep.people.charleston.edu/piccione_senet.pdf`, HTTP 200/application-pdf; the `id_` replay returned HTTP 200. Original URL has no query, so query-aware normalization equals the live URL.
- S753 live `curl -L`: HTTP 200, same Date header, zero redirects. CDX returned capture `20250926172224`, original `https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf`, HTTP 200/application-pdf; Wayback availability API reports it available. Repeated HTTPS `id_` and HTTP `id_` replay checks returned HTTP 404; the standard HTTPS replay failed with connection refusal. The capture is listed, but its direct replay remains unresolved. Original URL has no query, so query-aware normalization equals the live URL.
- No live redirect, login, paywall, or rate limit was observed on either PDF. S753's Wayback replay caveat is recorded in its `ACCESS` field.

## URL uniqueness scans
Before writing these two row fragments, exact-URL scans with `functions.grep` against `corpus/SOURCES.md` and every then-present fragment under `.ufo/waves/round-65/rows/` returned `No matches found` for each URL. The directory listing at scan time contained `rows/ScoutGapGames/gap.md`; neither URL occurred there. These scans establish no pre-existing exact-string duplicate in the scanned registry/fragments.
