# Row S670 — one-row, one-clause review

- Seat: KotodamaR61.RowS670 (leaf; no subagents, no background jobs)
- Page: https://vmm.mcb.org.uk/visiting-a-mosque-guide (single page; Wayback capture of same)
- Quoted passage: "You'll be asked to remove your shoes before entering the prayer hall"
- Clause: "Mosque visitors are asked to remove their shoes before entering the prayer hall."
- Method: ordinary means only — plain `curl` HTTP GET (live) and plain GET of the Wayback capture. No headless browser; no challenge was met. Scratch copies: /fast/scratch/hyaku/kotodama-r61/w2/RowS670/page.html, wayback.html.

## 1) QUOTE — LOCATED

- Live fetch: HTTP 200, final URL https://vmm.mcb.org.uk/visiting-a-mosque-guide, 7,721 bytes, `<title>Visitor's Guide — Visit My Mosque 2026</title>`.
- Archive capture works: Wayback CDX shows a 200 capture, timestamp 20260831102835 (http://web.archive.org/web/20260831102835/https://vmm.mcb.org.uk/visiting-a-mosque-guide); fetched HTTP 200, and the same sentence appears in it.
- Verbatim match, body text: the sentence appears exactly as quoted, inside a main-content `<p>` (line 59 of the saved HTML), in the dress/what-to-expect FAQ section following `<h1>Visiting a mosque</h1>`. It is not navigation (nav block is separate, line 30) and not a caption/figure fragment (no `<figure>`/`<figcaption>` on the page). Full sentence on the page: "You'll be asked to remove your shoes before entering the prayer hall — easy-to-slip-off shoes help." The quote is a prefix of that sentence; every quoted character matches.

## 2) CLAUSE — SUPPORTED

Nothing added, nothing removed:

- "Mosque visitors" — faithful conversion of the page's direct address to its audience; the page is a visitor guide (`<h1>Visiting a mosque</h1>`; "this guide explains what one is and what to expect"). No date, place, cause, comparison, or universal quantifier is introduced ("are asked" mirrors the page's generic guidance; the page itself notes "Every mosque is a little different").
- "are asked to remove" — preserves the page's hedge exactly ("You'll be asked", not "must").
- "before entering the prayer hall" — verbatim from the page.
- ≥10 consecutive words of page text carrying the clause: "we'd suggest both men and women dress modestly. You'll be asked to remove your shoes before entering the prayer hall — easy-to-slip-off shoes help."

## Findings by severity

- Critical/High/Medium: none. Both verdicts hold; no defect found in the row as recorded.
- Low (note only): the clause generalizes second-person "you" to "Mosque visitors". This is a supported audience conversion, not an addition — the page's own framing is guidance for prospective visitors.

## Residual risk

- Only one Wayback capture (2026-08-31) was examined; the live page fetched today (2026-10-23) already matches, so drift risk is minimal.
- Live fetch done once; content is behind no bot challenge and the fetch used plain curl, so results are reproducible by ordinary means.

## Verification gaps

- None material. HTTP status (200 live, 200 archive), capture timestamp, and verbatim body-text match are all directly evidenced above.

QUOTE S670 LOCATED
CLAUSE S670 SUPPORTED
