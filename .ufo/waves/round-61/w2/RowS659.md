# RowS659 — one-row one-clause falsify review (Kotodama R61 wave 2)

- URL: https://collections.vam.ac.uk/item/O74164/ (V&A Explore the Collections, "Leather Shoe | Unknown")
- Quoted passage (row): "This is part of a poulaine, a type of medieval man’s shoe with a long pointed toe"
- Clause under test: "A poulaine is a medieval man’s shoe with a long pointed toe."

## (1) QUOTE — LOCATED

- Live page: HTTP 200 on 2026-10-23 (curl, plain GET, `FINAL_URL:https://collections.vam.ac.uk/item/O74164/`, 47,637 bytes). No challenge or redirect encountered.
- The passage appears verbatim (including the U+2019 apostrophe in "man’s") twice in body content:
  1. `<div class="b-object-details__cell-free-content b-object-details__summary">` — the page's summary/description paragraph.
  2. The "Summary" row of the `b-object-details` table: `<td class="b-object-details__cell ..."><div class=b-object-details__cell-free-content>` — the same sentence.
- It is descriptive body text, not navigation, breadcrumb, menu, or a truncated caption fragment.
- Archive corroboration (not needed since live succeeded): Wayback CDX lists captures 20240110192505, 20240303095014, 20250215235103 (all `text/html 200`); the availability API returned 429 but the CDX index and a fetched capture worked — `web.archive.org/web/20250215235103id_/...` returned HTTP 200 containing the same verbatim sentence (twice).

## (2) CLAUSE — SUPPORTED

Page text carrying the clause (≥10 consecutive words, verbatim):

> "a poulaine, a type of medieval man’s shoe with a long pointed toe"

Full surrounding sentence: "This is part of a poulaine, a type of medieval man’s shoe with a long pointed toe. The poulaine was fashionable from about 1370 to 1400 and again from 1450 to 1500."

Check of each clause element:
- "poulaine" — named item class on the page. ✓
- "medieval" — the page calls it a "medieval man's shoe"; supported verbatim. ✓ (Separately, the page's Physical description says "Shoe, known as a poulaine with a very long pointed toe, fashionable from 1370-1400 and again from about 1450-1500" — consistent.)
- "man's shoe" — verbatim "man's shoe". ✓
- "long pointed toe" — verbatim. ✓
- Nothing added by the clause: no date ("1370-1400"/"1450-1500" omitted), no place ("English" omitted), no cause, no comparison, no universal ("all poulaines"), no removed hedge. The clause is a bare definitional restatement of the page's own "a type of medieval man's shoe with a long pointed toe". ✓

## Caveats

- The passage is a curatorial summary, not a citation of an external definition — but the review only asks whether the page supports the clause, which it does verbatim.
- Wayback availability endpoint rate-limited (429); corroboration relied on CDX + direct capture fetch instead. No installs used; curl only.

QUOTE S659 LOCATED
CLAUSE S659 SUPPORTED
