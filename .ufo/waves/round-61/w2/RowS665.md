# RowS665 — one-row one-clause review

Row: S665
URL: https://batashoemuseum.ca/standing-tall/
Fetched: 2026-10-23 UTC, HTTP 200 (113,677 bytes) via curl; identical content via reader.

## QUOTE

Quoted passage: "The heel was not a European invention, instead it originated in Western Asia centuries ago for horseback riding"

The string occurs verbatim 3 times in the page HTML, but every occurrence is inside an image-caption gallery block, not the article body:

- `data-img-description` attribute on `<a class="view view-first" data-fancybox="gallery" href=".../Iamge-1.jpg" data-img-title="Persian, 17th century" ...>` (offset 63208)
- identical `data-img-description` attribute on the `<img>` (offset 63712)
- `<p class="thumbnail-description">` inside `<div class="mask">` under heading `Persian, 17th century`, in the "Press Materials" gallery (offset 64478)

The rendered page confirms it is the caption/description text of the first press image ("Persian, 17th century …"), followed by the easy-social-share shortcode — a caption fragment, not body paragraph text. Under the criterion "(not navigation or a caption fragment)", the passage is verbatim caption text only.

Verdict: NOT-LOCATED (verbatim on the page, but exclusively as an image-caption fragment, which the criterion excludes; if captions are counted as page text, it is a full verbatim substring match).

## CLAUSE

Clause: "A heel originated in Western Asia for horseback riding before Europeans adopted it."

Supporting page text (≥10 consecutive words, verbatim):

"The heel was not a European invention, instead it originated in Western Asia centuries ago for horseback riding before Europeans adopted it at end of the 16th century."

Part-by-part check:
- "originated in Western Asia" — present verbatim.
- "for horseback riding" — present verbatim.
- "before Europeans adopted it" — present verbatim; the clause drops "at end of the 16th century", which removes a date rather than adding anything.
- "A heel" vs page's "The heel" — no change in meaning; the page also says it "was not a European invention", which the clause's "before Europeans adopted it" does not contradict.
- Nothing added by the clause: no date, no place beyond Western Asia, no cause, no comparison, no universal, no hedge.

Every part of the clause is carried by the page text (in the caption). Note: the same "caption not body" caveat applies — the support lives in the press-materials image caption, and the article body itself never mentions the heel's Western-Asian origin.

Verdict: SUPPORTED (page text carries every part of the clause; caveat: only via caption text, mirroring the QUOTE caveat).

## Notes
- Live page works (HTTP 200); no archive capture needed.
- No installs used.

QUOTE S665 NOT-LOCATED
CLAUSE S665 SUPPORTED
