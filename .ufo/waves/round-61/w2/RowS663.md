# Row S663 — one-row one-clause review (wave 2 FALSIFY)

- Row: S663
- Page: https://hue.fitnyc.edu/fit-museum/ (HUE article "A campus museum unlike any other.", `<h1 class="main-title">`, line 267)
- Quoted passage: "The red heels and soles of these latchet shoes are associated with Louis XIV and his court."
- Clause: "The red heels and soles of latchet shoes were associated with Louis XIV and his court."

## QUOTE

LOCATED. Live page fetched by curl: HTTP 200, 78,889 bytes, no redirects (effective URL identical). The sentence appears verbatim at line 289 of the HTML:

```
<div class="description"><p><span style="font-weight: 400;">Oldest item in the collection: Men's shoes, 1640–70, leather with cord ties</span></p>
<p><span style="font-weight: 400;">The red heels and soles of these latchet shoes are associated with Louis XIV and his court.</span></p>
```

It is body text, not navigation or a caption fragment: it sits in `div.description` inside `div.text-container`, the article's running descriptive prose for each museum item. The preceding `figure` is explicitly classed `image-container no-caption`, and the image's alt/`aria-label` text is a different string ("Pair of antique black leather shoes with red heels and green tassels"). The same image+description block pattern repeats for other items (e.g., the Poiret "Sorbet" gown), confirming this is the article body format, not captions.

Archive: Wayback availability API reports closest snapshot http://web.archive.org/web/20260611133831/https://hue.fitnyc.edu/fit-museum/ (status 200, available). Not needed for the verdict since the live page located the passage.

## CLAUSE

SUPPORTED. Evidence (18 consecutive words of page text carrying the clause):

> "The red heels and soles of these latchet shoes are associated with Louis XIV and his court."

Clause deltas vs. page and why none break support:
- "these latchet shoes" → "latchet shoes": drops the demonstrative, giving the clause a generic scope. The page's own claim is that the red heels and soles — the design feature — are associated with Louis XIV and his court; the association attaches to the feature, so the generic reading is what the page asserts. No new universal quantity beyond that is claimed.
- "are" → "were": tense shift to past fits the historical subject (Louis XIV's court); the page dates the shoes 1640–70.
- Nothing added: no date, place, cause, or comparison introduced; the page has no hedge that the clause removes.

Residual note for falsification honesty: the only arguable weak point is the demonstrative→generic move. If a reviewer rules the clause's bare plural an added universal the page doesn't literally state, the clause verdict could be contested — but the page sentence is itself a general association claim about the feature, so SUPPORTED is the honest reading.

No tools installed (curl + grep only; pacman untouched per pause directive).

QUOTE S663 LOCATED
CLAUSE S663 SUPPORTED
