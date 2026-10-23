# Row S655 — one-row one-clause review (round 61 wave 2, FALSIFY)

Seat: KotodamaR61.RowS655 · Date: 2026-10-23 · Ordinary means only (curl, reader-mode fetch). No tool installs (none needed).

## Target
- Page: https://www.iceman.it/en/news/new-reconstruction-of-the-iceman-s-shoes-and-coat_440 ("New reconstruction of the Iceman's shoes and coat", South Tyrol Museum of Archaeology)
- Recorded passage: "To keep his feet warm in the snow the Iceman also stuffed his shoes with hay."
- Clause under test: "To keep his feet warm in the snow, the Iceman stuffed hay into his shoes."

## Reachability (observed)
- Live: HTTP 200, 604,352 bytes (raw HTML saved to /fast/scratch/hyaku/kotodama-r61/w2/RowS655/live.html).
- Archive capture id_ 20250915132459: HTTP 200, 542,886 bytes (saved as arch.html).
- Reader-mode fetch of both URLs succeeded identically.

## (1) QUOTE — LOCATED
The sentence appears byte-verbatim, exactly once, in each raw copy, in the same article-body paragraph:
- live.html line 933; arch.html line 810: `<p>Eva made the shoes and coat exactly like the originals: … the anti-slip cross straps beneath the sole made of cowhide. The inner netting and the shoelaces are braided from linden bast. To keep his feet warm in the snow the Iceman also stuffed his shoes with hay. Eva Ijsveld did the same thing.</p>`
- Container check: it sits in a plain `<p>` of the article body, between the bold "brand-new replica" announcement paragraph and the workshops paragraph. It is not navigation, not a `<figcaption>`, and not part of the "Photos:" credit lines (which only carry copyright credits). No HTML entities or inline tags break the sentence.
- Body identical between live page and the 2025-09-15 capture; only the dynamic "News" sidebar items differ (irrelevant to the passage).

## (2) CLAUSE — SUPPORTED
Carrier text (16 consecutive words, verbatim from the page): "To keep his feet warm in the snow the Iceman also stuffed his shoes with hay"
Decomposition against the clause:
- purpose "to keep his feet warm" — present; condition "in the snow" — present; agent "the Iceman" — present; action/material/target "stuffed hay into his shoes" ≡ page's "stuffed his shoes with hay" (dative alternation, same proposition).
- Nothing added: no date, place, additional cause, comparison, or universal. The comma after "snow" is punctuation normalization only, meaning-neutral.
- Nothing load-bearing removed: the dropped word "also" is an additive connective tying the practice to the preceding replica-material list; dropping it neither asserts exclusivity (no universal introduced) nor removes any hedge. The page itself attributes the hay-stuffing to the historical Iceman (background fact about the original), and the following sentence "Eva Ijsveld did the same thing." concerns the replica-maker — the clause, about the Iceman, matches the page's own attribution.

## Residual risk / gaps
- Only the one given capture was checked; other capture dates not sampled (out of scope for one row).
- The page is a museum news item about a replica project; it supports the practice claim as stated, with no hedge — noted, not a defect of the row.
- Editorially the page contains a duplicated aside "(after decades of workshops and events)"; does not touch the recorded sentence.

QUOTE S655 LOCATED
CLAUSE S655 SUPPORTED
