# S725 — Claim C row sourcing report

## Behavior
Prepared one `mined` registry row for the Section 4 topic: maternal corrective recasts and immediate grammatical-morpheme imitation. The associated worldbuilder bullet describes a child imitating a maternal grammatical form after a corrective recast.

## Evidence and provenance
- `web_search` query: `recast corrective feedback child grammar acquisition study recasts grammatical development children open access`. It surfaced the peer-reviewed, open-access systematic review by Cleave et al. (2015), “The Efficacy of Recasts in Language Intervention: A Systematic Review and Meta-Analysis,” *American Journal of Speech-Language Pathology* 24(2):237–255.
- Opened the live PMC page with `curl -sL --max-time 60 -w '\nHTTP_STATUS:%{http_code}\n' https://pmc.ncbi.nlm.nih.gov/articles/PMC4450887/`; outcome: HTTP 200. Page metadata and body identify the paper and the quoted Introduction passage. No challenge or paywall encountered.
- Checked the same page with `curl -s --max-time 60 'https://archive.org/wayback/available?url=https://pmc.ncbi.nlm.nih.gov/articles/PMC4450887/'`; outcome: capture available, status 200, timestamp `20251207214256`, original page URL `https://pmc.ncbi.nlm.nih.gov/articles/PMC4450887/`. Row capture URL: `https://web.archive.org/web/20251207214256id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC4450887/`.
- Ran `python3 -B reports/round-61/reopen-quote.py 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4450887/' 'typically developing children were more likely to imitate a maternal use of a grammatical morpheme following a corrective recast'` from the lane root twice (initial and self-check); both printed `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC4450887/`.
- Format self-check: `awk -F'|'` reported 13 fields (11 cells); the quoted anchor contains 19 words.

## Tier and limits
Tier B applies to the scoped report of the immediate imitation result in typically developing two-year-olds: this peer-reviewed systematic review summarizes the Farrar (1992) study rather than being that original study. The quoted evidence supports immediate imitation after corrective recasts, not durable acquisition or a causal account of the learning mechanism.

## Gates, touched surfaces, and out of scope
Local row checks passed (live page HTTP 200, archived capture available, locator twice located, cell and quote counts in range). No `ACCEPT-C-64` acceptance script was run; this seat's row is not integrated and cannot establish the full claim predicate. No product or registry files were changed; no tests, builds, or lint checks were run. No tools were installed.

Artifacts touched:
- `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS725/row.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-64/w1/ScribeRowS725.md`
