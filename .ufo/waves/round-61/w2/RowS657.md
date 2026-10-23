# RowS657 — one-row one-clause review

- URL: https://www.vindolanda.com/blog/the-curators-favourite-shoes
- Fetched live by ordinary means: `curl -L` → HTTP 200, text/html, 70,590 bytes, no redirect off-origin, no bot challenge encountered. Reader-mode extraction also returned the page (title "The Curator's Favourite Shoes | The Vindolanda Trust", published 2020-09-22, modified 2021-02-06).
- No installs used; no archive capture needed (live page works).

## (1) QUOTE

The passage is verbatim body text. Raw HTML contains, inside a `<p>` paragraph under the heading "5. Lady's shoe sole" (regular article prose, not navigation, not a caption/`figcaption` element):

> "The iron studs on any Roman shoe are there as a way of holding the numerous layers of leather which make up the sole together and these definitely do this."

The row's quoted passage is an exact substring of that sentence (stops before "and these definitely do this"). Character-for-character match including "holding the numerous layers of leather which make up the sole together".

Verdict: **LOCATED**

## (2) CLAUSE

Clause: "Iron studs joined the leather layers making up a Roman shoe's sole."

Page text carrying it (24 consecutive words):

> "The iron studs on any Roman shoe are there as a way of holding the numerous layers of leather which make up the sole together"

Part-by-part:
- "Iron studs" — page: "The iron studs" ✓
- "joined" — page: "holding … together" (same claim: studs hold the layers together) ✓
- "the leather layers making up a Roman shoe's sole" — page: "the numerous layers of leather which make up the sole" of "any Roman shoe" ✓ (clause drops "numerous", which removes nothing the clause asserts)

Nothing added: no date, place, cause, or comparison introduced; the clause's indefinite "a Roman shoe" is *weaker* than the page's universal "any Roman shoe", so the clause asserts strictly less than the source. No hedge removed — the page states the function flatly ("are there as a way of holding … together").

Verdict: **SUPPORTED**

QUOTE S657 LOCATED
CLAUSE S657 SUPPORTED
