# RowS666 — one-row one-clause review (round 61 wave 2 FALSIFY)

URL: https://www.bbc.co.uk/programmes/articles/qsXBljJrnRm60Gdt2PR362/six-surprising-facts-about-the-history-of-high-heeled-shoes
Quoted passage: "The earliest evidence we have of someone wearing heels is from a 10th-century Persian bowl."
Clause: "The earliest evidence of someone wearing heels comes from a 10th-century Persian bowl."
Method: ordinary means only — curl + python stdlib html.parser / urllib. No headless browser. Revision context efbee29 (lane repo untouched; only this report written).

## (1) QUOTE — LOCATED

- Live fetch: HTTP 200, 234,982 bytes (curl, desktop UA). No redirect away from the article; `<title>` = "BBC Radio 4 - You're Dead to Me - Six surprising facts about the history of high heeled shoes".
- The exact string "The earliest evidence we have of someone wearing heels is from a 10th-century Persian bowl." occurs verbatim exactly once in the served HTML (byte-exact `str.count == 1`, charrefs resolved — page uses `&rsquo;` only later in the same paragraph, after the quoted sentence's period).
- Placement: it is the complete first sentence of an article-body `<p>` directly under `<h2>2. Heeled shoes were originally designed for Medieval soldiers</h2>` — body prose, not navigation, not a breadcrumb. The adjacent image caption is a separate element ("Persian riding shoes (Image © Bata Shoe Museum, Toronto.)") and is not the source of the quote.
- Archive capture works: CDX lists repeated 200 text/html captures (20220119… through 20241007130238+); snapshot https://web.archive.org/web/20241007130238/… fetched HTTP 200 (233,705 bytes) and contains the same sentence verbatim in the same paragraph position. Note: the `archive.org/wayback/available` JSON endpoint answered 429 Too Many Requests (rate limit) — capture verification done via CDX + direct snapshot instead.

## (2) CLAUSE — NOT-SUPPORTED (one part: removed hedge "we have")

Page text (≥10 consecutive words carrying the clause, verbatim):

> "The earliest evidence we have of someone wearing heels is from a 10th-century Persian bowl."

- "is from" → "comes from": meaning-preserving paraphrase, supported.
- 10th-century / Persian / bowl / someone wearing heels / earliest: all present, nothing added.
- Unsupported part named exactly: the hedge "we have" is dropped. The page bounds the claim to currently held evidence ("the earliest evidence **we have** … is from…"); the clause asserts "The earliest evidence of someone wearing heels comes from…" unqualified — i.e. earliest evidence simpliciter, which the page does not claim (unknown/unheld earlier evidence would falsify the clause but not the page sentence). Under the rubric "nothing added … or a hedge removed", this is a hedge removal, so the page does not support EVERY part of the clause. Narrow defect: no date/place/cause/comparison was invented; the fix is "The earliest evidence we have of someone wearing heels comes from…".

## Housekeeping

- No tools installed or updated (none needed). No processes left running (curl/urllib calls completed and exited). Scratch files only under /fast/scratch/hyaku/kotodama-r61/w2/RowS666/ (live.html, live.headers).
- Never ran reports/round-61/accept-c.py; no git/jj commands in the lane or fleet repos.

QUOTE S666 LOCATED
CLAUSE S666 NOT-SUPPORTED
