# B2ReviewRowS720 — wave-2 falsification review of draft row S720

Draft: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS720/row.txt`
Review file: `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ReviewRowS720/review.md`

## HTTP results (2026-10-23, verbatim)

- Live GET `https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/` → `HTTP 200 https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/`
- Capture GET `https://web.archive.org/web/20250202023425id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/` → `HTTP 200 https://web.archive.org/web/20250202023425id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/`
- Lane locator first line: `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/`

## Checks

- Anchor quote (24 normalised words) is verbatim, contiguous, single occurrence, in the
  Abstract paragraph (`<p id="P1">`, heading `Abstract`) — body text, not
  caption/alt/title/nav. Found identically in live page and capture.
- Citation verified against page metadata: authors Lee (first of five → "Lee et al."),
  title verbatim, journal Language Learning and Development, `13(1):100–126`,
  `Issue date 2017` → year 2017 correct.
- Tier A justified: the row's scope names exactly this study, so the primary source is A.
- Row shape: 11 cells, mined, 2026-10-23, 180d, used-by = entry path; capture original
  matches live URL.
- BULLET vs RESTATE + semantics: 13 content words, 5 in-order quote hits, 8 novel
  content words, max copied run 2; clause preserves the quote's hedged "may", no
  overreach or invented numbers.

## Required fixes

None.

VERDICT: CLEAN every field verified against live page (HTTP 200) and capture (HTTP 200); locator LOCATED; citation, tier, quote and bullet all honest.
