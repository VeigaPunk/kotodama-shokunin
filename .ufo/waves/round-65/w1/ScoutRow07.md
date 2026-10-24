# ScoutRow07 — S762 and S763

Opened exactly the two assigned row drafts:
- `.ufo/waves/round-65/rows/ScoutRow07/row-S762.txt`
- `.ufo/waves/round-65/rows/ScoutRow07/row-S763.txt`

## Findings

- **S762 — FIFA Museum, “Origins – Meso-American ball games”** (`docs`, tier B). Direct `curl` returned HTTP 200 on 2026-10-24 with the original URL unchanged; the quoted wording is present in the returned article body. The article describes 12 solid rubber balls recovered at the Olmec ceremonial/burial site of El Manatí, dates them to about 1600 BCE, and notes size variation may mean offerings rather than balls for one game. Wayback capture `20260925004118` returned HTTP 200 and contains the quoted passage. Confidence: high that the row accurately restates the museum article; this is secondary museum reporting, not a direct laboratory analysis. The bullet deliberately does not claim match use.
- **S763 — Eddie Duggan, “A game on the edge…”**, *Board Game Studies Journal* 15(1) (`paper`, tier A). Direct `curl` returned HTTP 200 on 2026-10-24 without a redirect; the quoted wording is present in the abstract body. OARS metadata identifies the journal article as refereed, and its abstract lists hnefatafl and related tafl-family games, then discusses terminology, archaeological boards, literary evidence, and Linnaeus’s tablut account. Wayback capture `20260520171602` returned HTTP 200. Confidence: high for the abstract-level family and source-method claims. Remaining limit: OARS explicitly has no full text; this row does not substantiate specific movement/capture rules, and publisher access was not checked.

## Live-URL uniqueness checks (`grep`)

- `https://www.fifamuseum.com/en/explore/fifamuseumplus/blog/origins-meso-america-ball-games` — `corpus/SOURCES.md`: **No matches found**. `.ufo/waves/round-65/rows/`: **one matching line, only `ScoutRow07/row-S762.txt`**; no other row fragment matched.
- `https://oars.uos.ac.uk/1736/` — `corpus/SOURCES.md`: **No matches found**. `.ufo/waves/round-65/rows/`: **one matching line, only `ScoutRow07/row-S763.txt`**; no other row fragment matched.

In each matching row the literal URL also appears as the original-URL suffix of its required Wayback capture; the grep match is confined to that row, with no competing registry or row-fragment source. Both captures are query-free and their originals normalize to their respective live URLs.

No tools were installed or updated.