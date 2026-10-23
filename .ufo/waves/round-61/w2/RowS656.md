# Row S656 — one-row one-clause review (wave 2 falsify)

## Page
- URL: https://exarc.net/issue-2023-2/at/reconstructing-otzis-shoes
- Fetch: live page reachable, HTTP 200 (138,114 bytes), fetched 2026-10-23 via plain curl with a browser UA. No challenge encountered.
- Archive capture: https://web.archive.org/web/20230616010106id_/https://exarc.net/issue-2023-2/at/reconstructing-otzis-shoes — HTTP 200 (126,322 bytes), capture serves and contains the same passage.

## (1) QUOTE
Quoted passage: "The shoes consist of a bearskin sole, deerskin upper leather attached to the sole with a thin cow hide strap."

- Verbatim match, character-for-character including the space in "cow hide" and the period.
- Live page: inside `<div class="print-only ... field--name-body ..."><h4>Description of the shoes</h4><p>The shoes consist of a bearskin sole, ...</p>` — the Drupal body field of the article.
- Archive copy (line 441): identical sentence inside the same `field--name-body` div, following the article intro ("...I had the opportunity to reconstruct Ötzi's shoes.").
- It is body text of the article, under the section heading "Description of the shoes" — not navigation, not a figure caption, not a pull-quote field (the separate `field--name-field-quote` pull-quote contains different text).

Verdict: LOCATED.

## (2) CLAUSE
Clause under test: "Ötzi's shoes joined a bearskin sole to deerskin upper leather with a thin cowhide strap."

Page text carrying the clause (>=10 consecutive words, verbatim):
> "The shoes consist of a bearskin sole, deerskin upper leather attached to the sole with a thin cow hide strap."

Component check:
- "Ötzi's shoes": page title is "Reconstructing Ötzi's Shoes"; intro: "...the opportunity to reconstruct Ötzi's shoes."; body: "The right shoe was still on Ötzi's foot when he was found." The "shoes" described in the quoted sentence are these shoes. Supported.
- "bearskin sole": verbatim "a bearskin sole"; elsewhere "The sole is made from bearskin". Supported.
- "deerskin upper leather": verbatim "deerskin upper leather"; elsewhere "upper and back of the shoes are made from roe deer skin" (roe deer is a deer — consistent, not contradicted). Supported.
- "joined ... with a thin cowhide strap": verbatim "attached to the sole with a thin cow hide strap". "Joined" faithfully compresses "attached to the sole with"; "cowhide" is the same word as "cow hide" (the page itself writes "cowhide" elsewhere: "a 0.5 cm wide cowhide strap"). Supported.
- Nothing added: no date, place, cause, comparison, or universal claim in the clause; no hedge present in the source sentence that the clause drops (the source states the construction flatly).
- Note: the page elsewhere distinguishes the thin (0.5 cm) strap sewing the upper from a thick (~1.2-2 cm) strap shaping the sole; the clause's "thin" attaches correctly to the upper-to-sole strap and introduces no confusion.

Verdict: SUPPORTED.

QUOTE S656 LOCATED
CLAUSE S656 SUPPORTED
