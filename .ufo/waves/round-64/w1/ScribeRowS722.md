# S722 — Fast mapping and vocabulary spurt

## Behavior and provenance
- Selected Samuelson and McMurray, “What does it take to learn a word?” (2016), *Wiley Interdisciplinary Reviews: Cognitive Science* 8(1–2), as a peer-reviewed review spanning referential ambiguity, fast mapping, and the vocabulary spurt. The quoted passage is in “A Continuous Vocabulary Spurt,” paragraph 35, and identifies domain-general processes in early word learning.
- **Tier B:** this is a substantive peer-reviewed secondary review/synthesis, not the original study for a specific empirical finding. The tier applies only to the scoped topic in the row.
- Opened the live PMC page by plain GET; received HTTP 200. The Wayback availability endpoint reported an available 200 capture at timestamp `20250410073702`. Its response did not contain a separate `original` field; the returned archived URL embeds the requested original page URL. Used the requested `id_` capture form in the row.
- Quote is verbatim body text, 16 words. The final locator invocation returned `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/`. `awk -F'|'` counted 13 fields in the row (11 cells); quote word count was 16.

## Row and learner-facing bullet
ROW: | S722 | Samuelson and McMurray, 2016, "What does it take to learn a word?", Wiley Interdisciplinary Reviews: Cognitive Science 8(1–2) - https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/ ; capture https://web.archive.org/web/20250410073702id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/ | paper | B | early word learning: fast mapping and vocabulary-spurt development | Section A Continuous Vocabulary Spurt, paragraph 35: "emphasizes the importance of domain-general processes like novelty, attention, statistical learning, association, competition, and parallel learning" | Helps worldbuilders portray early word learning as involving interacting general processes rather than a language-specific mechanism. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |
BULLET: - Novelty, attention, statistical learning, and competition shape how toddlers build vocabulary (S722)
VERIFY: LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/
CAPTURE: timestamp=20250410073702; original=https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/
ACCESS: plain curl -sL --max-time 60, HTTP 200, 2026-10-23

## Exact commands and outcomes
- Search: `web_search` query `fast mapping vocabulary spurt children review open access paper`; result identified the PMC review and the specific relevant sections.
- Source GET: `curl -sL --max-time 60 -o /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS722/source.html -w 'HTTP_STATUS:%{http_code}\n' 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/'` — `HTTP_STATUS:200`.
- Capture lookup: `curl -s --max-time 60 'https://archive.org/wayback/available?url=https%3A%2F%2Fpmc.ncbi.nlm.nih.gov%2Farticles%2FPMC5182137%2F'` — returned `{"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/", "archived_snapshots": {"closest": {"status": "200", "available": true, "url": "http://web.archive.org/web/20250410073702/https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/", "timestamp": "20250410073702"}}}`.
- Locator, run twice from working directory `/home/vgpnk/Projects/shokunin/kotodama-shokunin`: `python3 -B reports/round-61/reopen-quote.py 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/' 'emphasizes the importance of domain-general processes like novelty, attention, statistical learning, association, competition, and parallel learning'` — both runs returned `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/`.
- Self-check: `awk -F'|' '/^ROW:/ {printf "ROW_FIELDS:%d\n", NF}' /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS722/row.txt && printf '%s\n' 'emphasizes the importance of domain-general processes like novelty, attention, statistical learning, association, competition, and parallel learning' | wc -w` — `ROW_FIELDS:13`, `16`.
- Prepared scratch/report directories with `mkdir -p`; no tools installed or updated.

## Touched surfaces, gates, and limits
- Artifacts: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS722/row.txt` and retrieved source copy `source.html`; report: `.ufo/waves/round-64/w1/ScribeRowS722.md`.
- Coverage gate for this item: source locator passed twice; row field and quote counts passed. No acceptance script for claim C was run.
- No corpus entry, registry, product code, or other lane files were edited; the scoped row remains an artifact for integration. No build, test, or lint run. No installs.
- Limit: as a review, the source supports a synthesis of the relevant account, not an original empirical result or universal causal law.
