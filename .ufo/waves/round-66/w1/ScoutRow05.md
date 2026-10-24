# ScoutRow05 — ROW-OPENING (claim C): S785 + S786

Both rows opened, verified, and written to `.ufo/waves/round-66/rows/ScoutRow05/row-S785.txt` and `row-S786.txt`. Rejects in `rows/ScoutRow05/rejects.txt`.

## S785 — Mesoamerican copal incense (ritual use)
- **Source:** Aurora Montúfar López (INAH), "Copal de *Bursera bipinnata*. Una resina mesoamericana de uso ritual," *Trace* 70 (2016), SciELO México — peer-reviewed, tier A.
- **Live:** `https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0185-62862016000200045` — curl HTTP 200, Sat 24 Oct 2026 11:32 GMT, no redirects/login/paywall.
- **Anchor quote (verbatim in English abstract):** "its aromatic smoke, that was also considered divine food, allowed the link between deities and humans" — covers copal smoke as divine food + human–deity link in agricultural/calendar rites; Templo Mayor offerings context noted in abstract.
- **Capture:** wayback `20250604073907id_` replays HTTP 200; captured original == live URL (query identical).

## S786 — Chinese incense / xiang (香) tradition
- **Source:** Olivia Milburn, "Aromas, Scents, and Spices: Olfactory Culture in China before the Arrival of Buddhism," *Journal of the American Oriental Society* 136(3), 2016, pp. 441–464 — peer-reviewed (AOS flagship), tier A.
- **Live:** `https://lockwoodonlinejournals.com/index.php/jaos/article/view/1362` — curl HTTP 200, Date Sat 24 Oct 2026 11:36:13 GMT, no redirects; landing page exposes the abstract where the quote lives.
- **Anchor quote (verbatim in abstract):** "elite scent culture had already begun to be transformed by the importation of foreign aromatics" — the xiang-tradition thesis that imported aromatics predated Buddhist influence, against a baseline of local scents used individually in religious contexts.
- **Capture:** wayback `20260811211617id_` replays HTTP 200 (verified after transient connect failures); CDX lists 9 snapshots 2022–2026 on bare/www domain variants.

## Uniqueness
Both live URLs grepped against `corpus/SOURCES.md` and all `corpus/` fragments: zero prior use (scielo.org.mx hits are a different pid/article; no lockwood hits). Distinct normalized hosts (scielo.org.mx vs lockwoodonlinejournals.com) — contributes to HOSTS leg diversity.

## Rejects / alternates
- `metmuseum.org/art/collection/search/314557` (Met copal censer) — HTTP 429, logged as reject with flip.
- `cambridge.org` JRAS Feng 2024 article — HTTP 429, logged as reject with flip.
- `dash.harvard.edu` copal PDF (`.../content`, 200 application/pdf, 868KB) — verified live but not needed; kept as alternate for S785-class seats.

## Notes for the integrator
- S785 full text is Spanish; the quoted passage sits in the bilingual English abstract — the entry bullet restates it (burned smoke / divine food / deity link).
- S786 landing page = abstract only; deeper body text needs the JAOS PDF (accessible; not required for the anchor).
- web.archive.org was briefly unreachable twice mid-check (connect refused); the working capture ts was confirmed on retry. No tool installs needed; curl + python stdlib only.
