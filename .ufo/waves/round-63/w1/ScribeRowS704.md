# ScribeRowS704 report

## Behavior
Prepared one S704 candidate about the Arizona State Museum's kabuto record. The quoted sentence is in the record's descriptive prose paragraph, not an image caption; it says the helmet has 120 individual riveted steel plates rather than the standard 62 or fewer. The same sentence was visible in the live page and in two Wayback `read` renderings. The live locator returned `LOCATED`; the required capture locator could not fetch either tested Wayback URL, so the candidate is **not fully validated for integration**. This is a fetch failure, not evidence that the quote is absent. No acceptance verdict is assigned.

## Gates and evidence
- Read `reports/round-63/claims.json`, both counter docstrings, and section 5 of `corpus/lessons/round-62-verifier-spotcheck.md` as assigned. No accept counter or held `tools/reopen-row.py` was run.
- Source: Davison Packard Koenig, former Senior Exhibit Coordinator, text dated August 2011, “Japanese Samurai Helmet and Half Mask,” Arizona State Museum: <https://statemuseum.arizona.edu/online-exhibit/curators-choice/samurai-helmet-half-mask>. The exact live URL search in `corpus/SOURCES.md` returned `No matches found.`
- `read` on the live URL displayed the selected body-text quote. CDX query `https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fstatemuseum.arizona.edu%2Fonline-exhibit%2Fcurators-choice%2Fsamurai-helmet-half-mask&output=json&limit=-5&filter=statuscode%3A200` returned captures for the same original URL, status 200, at timestamps `20241010065900`, `20241213235120`, `20250219205419`, `20250712060510`, and `20260316015949`. `read` on the latest (`20260316015949id_`) and the `20250712060510id_` replay showed the same quote in the prose paragraph.
- Live locator command:
  `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://statemuseum.arizona.edu/online-exhibit/curators-choice/samurai-helmet-half-mask' 'This kabuto is made of 120 individual riveted steel plates, rather than the standard 62 or fewer.'`
  Output: `LOCATED https://statemuseum.arizona.edu/online-exhibit/curators-choice/samurai-helmet-half-mask` (the locator returns 0 on `LOCATED`).
- Latest capture locator command:
  `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260316015949id_/https://statemuseum.arizona.edu/online-exhibit/curators-choice/samurai-helmet-half-mask' 'This kabuto is made of 120 individual riveted steel plates, rather than the standard 62 or fewer.'`
  Output: `NOT_LOCATED https://web.archive.org/web/20260316015949id_/https://statemuseum.arizona.edu/online-exhibit/curators-choice/samurai-helmet-half-mask URLError`; exit 1.
- Alternate capture locator command:
  `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20250712060510id_/https://statemuseum.arizona.edu/online-exhibit/curators-choice/samurai-helmet-half-mask' 'This kabuto is made of 120 individual riveted steel plates, rather than the standard 62 or fewer.'`
  Output: `NOT_LOCATED https://web.archive.org/web/20250712060510id_/https://statemuseum.arizona.edu/online-exhibit/curators-choice/samurai-helmet-half-mask URLError`; exit 1.
- Retried the latest capture command once; it again printed the same `NOT_LOCATED ... URLError` and exited 1. Testing `http://web.archive.org/web/20260316015949id_/https://statemuseum.arizona.edu/online-exhibit/curators-choice/samurai-helmet-half-mask` printed `NOT_LOCATED http://web.archive.org/web/20260316015949id_/https://statemuseum.arizona.edu/online-exhibit/curators-choice/samurai-helmet-half-mask HTTPError`; exit 1. The locator source maps fetch/parse errors to non-location results; the output does not establish quote absence. Because the required capture locator did not locate, treat this row as provisional and do not count it as a verified S704 contribution.

## Draft artifacts
Registry row (11 columns):

`| S704 | Koenig, Davison Packard (text), “Japanese Samurai Helmet and Half Mask,” Arizona State Museum, August 2011 — https://statemuseum.arizona.edu/online-exhibit/curators-choice/samurai-helmet-half-mask ; capture https://web.archive.org/web/20260316015949id_/https://statemuseum.arizona.edu/online-exhibit/curators-choice/samurai-helmet-half-mask | docs | A | Arizona State Museum's curatorial account of this kabuto's construction, unusual plate count, maker's signature, and family crest | Construction paragraph, "This kabuto is made of 120 individual riveted steel plates, rather than the standard 62 or fewer." | The museum describes this kabuto's 120 riveted plates as exceeding the standard count and says its crest identified the wearer on the battlefield. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |`

Entry bullet:

`- The 120 riveted steel plates distinguish this kabuto from the standard count described by the museum (S704)`

Gate-ready line:

`- S704 | https://statemuseum.arizona.edu/online-exhibit/curators-choice/samurai-helmet-half-mask | 2026-10-23 | "This kabuto is made of 120 individual riveted steel plates, rather than the standard 62 or fewer."`

## Touched surfaces and out of scope
Wrote only the four S704 evidence/artifact files below under the assigned scratch directory and this report at its designated path. No lane source, entry, registry, product code, counter, or Git/JJ state was changed. No tool was installed. No C or O counter was run; no row-level blind review or full-wave judgment was performed. This row is not in the frozen C LIVE subset (S694, S698, S702, S706, S710, S714).

## Artifact paths
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS704/S704-registry-row.txt`
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS704/S704-entry-bullet.txt`
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS704/S704-Gate-line.txt`
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS704/S704-locator-results.md`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-63/w1/ScribeRowS704.md`
