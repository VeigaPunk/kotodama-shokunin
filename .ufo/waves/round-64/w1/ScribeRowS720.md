# S720 — Babbling and early phonological development

## Behavior and provenance
- Selected Lee et al. (2017), “Subtlety of Ambient-Language Effects in Babbling: A Study of English- and Chinese-Learning Infants at 8, 10, and 12 Months,” *Language Learning and Development* 13(1), 100–126. This original peer-reviewed study evaluates ambient-language detection in infant utterances, including those with canonical syllables.
- **Tier A:** the original research paper is authoritative for its own findings; this tier is scoped to ambient-language effects in the studied English- and Chinese-learning infants’ babbling and canonical-syllable utterances, not to universal language-development claims.
- The PMC page identifies the article’s 2017 issue, authors, journal, and abstract. The abstract reports that ambient-language effects were not detected in most infant utterances and were detectable only in items judged to be words or to contain canonical syllables that might sound like words with language-specific shapes; effects were small compared with adult speech.
- The quote is verbatim body text from the Abstract (23 words). The locator’s final invocation returned `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/`.
- The Wayback availability response reported an available status-200 capture at timestamp `20250202023425`. It did not have a separate `original` JSON field; the original page URL is embedded after the timestamp in its returned archived URL. The requested `id_` replay URL was fetched successfully (HTTP 200).

## Row and learner-facing bullet
ROW: | S720 | Lee et al., 2017 "Subtlety of Ambient-Language Effects in Babbling: A Study of English- and Chinese-Learning Infants at 8, 10, and 12 Months", Language Learning and Development, 13(1), 100–126 - https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/ ; capture https://web.archive.org/web/20250202023425id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/ | paper | A | ambient-language effects on 8-, 10-, and 12-month-old English- and Chinese-learning infants’ babbling and canonical-syllable utterances | Abstract: "only in items deemed to be words or to contain canonical syllables that may have made them sound like words with language-specific shapes" | Helps worldbuilders portray ambient-language influence as subtle and most discernible in infant utterances with canonical or word-like forms. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |
BULLET: - Canonical syllables may make language-specific word shapes audible during early infant vocal development (S720)
VERIFY: LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/
CAPTURE: timestamp=20250202023425; original=https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/
ACCESS: plain curl of live source HTTP 200; archived capture HTTP 200; 2026-10-23

## Exact commands and outcomes
- Search 1: `web_search` query `canonical babbling phonological development infants language-specific drift peer reviewed open access`; result set included open-access infant babbling studies.
- Search 2: `web_search` query `infant babbling language-specific drift consonant repertoire canonical babbling original research open access`; result identified the open PMC study.
- Scratch setup: `mkdir -p /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS720` — completed.
- Live source GET: `curl -sL --max-time 60 -o /dev/null -w 'HTTP %{http_code}\n' 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/'` — `HTTP 200`.
- Wayback lookup: `curl -s --max-time 60 'https://archive.org/wayback/available?url=https%3A%2F%2Fpmc.ncbi.nlm.nih.gov%2Farticles%2FPMC5421641%2F'` — returned `available: true`, `status: 200`, timestamp `20250202023425`, and archived URL `http://web.archive.org/web/20250202023425/https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/`.
- Capture GET: `curl -sL --max-time 60 -o /dev/null -w 'HTTP %{http_code}\n' 'https://web.archive.org/web/20250202023425id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/'` — `HTTP 200`.
- Locator, run twice from `/home/vgpnk/Projects/shokunin/kotodama-shokunin`: `python3 -B reports/round-61/reopen-quote.py 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/' 'only in items deemed to be words or to contain canonical syllables that may have made them sound like words with language-specific shapes'` — both runs returned `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/`.
- Self-check: `awk -F'|' '/^ROW:/ {print "ROW fields=" NF}' /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS720/row.txt && printf '%s\\n' 'only in items deemed to be words or to contain canonical syllables that may have made them sound like words with language-specific shapes' | wc -w` — `ROW fields=13` (11 cells), quote count `23` words.

## Touched surfaces, gates, and limits
- Artifacts: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS720/row.txt` and `.ufo/waves/round-64/w1/ScribeRowS720.md`. An existing `article.html` was present in the scratch directory before writing `row.txt`; it was not changed or used as source evidence.
- Item-level locator and row-shape/quote-count checks passed. No claim-C acceptance script, claim-O/claim-Ca check, build, test, or lint was run. No tools were installed or updated.
- No corpus entry, registry, product code, or other lane source files were edited; the row is a sourced integration artifact.
- Limit: this study concerns English- and Chinese-learning infants at 8, 10, and 12 months and reports small, context-dependent effects. It does not establish that all babbling is reliably language-specific or that every infant’s early vocal repertoire follows a universal drift pattern.