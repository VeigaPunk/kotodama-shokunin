# Row S673 — falsify review (wave 2)

Row: S673 | Page: https://www.musee-mccord-stewart.ca/en/collections/indigenous-cultures/
Quoted passage: "Moccasins, Nêhiyawak, 1920. Gift of the Art Association of Montreal, ME928.8.1-2"
Clause: "The caption lists Nêhiyawak moccasins dated 1920 as a gift of the Art Association of Montreal."

## (1) QUOTE

Fetch: live page fetched by ordinary means (curl, Firefox UA), HTTP 200, 73,686 bytes, final URL unchanged. No challenge, captcha, or login encountered.

The quoted string appears verbatim, as one continuous run, at three places in the served HTML:

- Line 322 — LIVE `<div class="credit">Moccasins, Nêhiyawak, 1920. Gift of the Art Association of Montreal, ME928.8.1-2 © McCord Stewart Museum</div>` inside the visible `<div class="headerImg">` block (lines 320–323). This is the complete credit line (the quote is the whole caption minus the trailing "© McCord Stewart Museum"), rendered as body content under the header image — not navigation, and the complete caption rather than a fragment of one.
- Lines 327–330 — an identical `headerImg`/`credit` block inside an HTML comment (`<!-- ... -->`); dead markup, not rendered.
- Line 355 — `alt`/`title` attributes on the thumbnail `<img src="...me928-8-1-2_en-1021x800.jpg">` in the object gallery; same complete credit line.

The live line-322 occurrence alone satisfies verbatim presence as page body text; the complete caption is present, not a fragment. Archive check: Wayback availability API returned HTTP 429 (rate limited) — archive corroboration was not needed because the live page returns 200 and contains the quote. Reported as attempted-not-passed, not met-not-passed (rate limit, not a challenge).

## (2) CLAUSE

Every element of the clause maps onto the page text:

- "The caption lists" — the text is literally the header-image credit/caption (`div.credit`); it is also the gallery image's alt/title caption.
- "Nêhiyawak moccasins" — "Moccasins, Nêhiyawak".
- "dated 1920" — "1920".
- "a gift of the Art Association of Montreal" — "Gift of the Art Association of Montreal".

Nothing is added by the clause: no date, place, cause, comparison, or universal beyond the caption; no hedge removed. The only omission is the accession number ME928.8.1-2 and the © notice, which the clause does not assert.

Page text carrying the clause (consecutive words from line 322):
"Moccasins, Nêhiyawak, 1920. Gift of the Art Association of Montreal, ME928.8.1-2 © McCord Stewart Museum"

## Notes

No tools installed; no installs needed. No writes to the fleet repo or lane repo other than this report. Scratch evidence: /fast/scratch/hyaku/kotodama-r61/w2/RowS673/live.html.

QUOTE S673 LOCATED
CLAUSE S673 SUPPORTED
