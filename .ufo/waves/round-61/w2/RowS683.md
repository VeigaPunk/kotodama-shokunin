# RowS683 — one-row one-clause review

- URL: https://polotsk-local.museum.by/en/node/45054 ("Bast shoes", Drupal 7, Museum of Local Studies, Polotsk)
- Method: plain `curl -L` (ordinary means), HTTP 200, 27,705 bytes; copy kept at /fast/scratch/hyaku/kotodama-r61/w2/RowS683/live.html
- Wayback availability API returned HTTP 429 (rate-limited); not needed — live page reachable.

## (1) QUOTE
The passage appears verbatim in the node body (`div.field-name-body`, first `<p align="justify">`):

> "Traditional type of peasant shoes were bast shoes. They are woven from vine or linden bast (soft bark). The material was harvested in May-June but the weavers began to weave in the fall or winter when all the work in the field was completed."

This is main article body text — not navigation, breadcrumb, or caption. (The same string also appears in the `<meta name="description">` tag, which is normal Drupal behavior and does not disqualify the body occurrence.)

Verdict: LOCATED (live page, HTTP 200).

## (2) CLAUSE
Clause: "Peasant bast shoes were woven from vine or linden bast."

- "Peasant bast shoes" ← page: "Traditional type of peasant shoes were bast shoes."
- "were woven from vine or linden bast" ← page: "They are woven from vine or linden bast (soft bark)." Present→past tense paraphrase only; no date, place, cause, comparison, or universal added, no hedge removed (the parenthetical "soft bark" is dropped but it only glosses "bast", not a hedge).

Carrying text (≥10 consecutive words from body): "Traditional type of peasant shoes were bast shoes. They are woven from vine or linden bast (soft bark)."

Verdict: SUPPORTED.

QUOTE S683 LOCATED
CLAUSE S683 SUPPORTED
