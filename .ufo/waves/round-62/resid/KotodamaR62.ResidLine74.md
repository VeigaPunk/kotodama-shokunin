VERDICT KotodamaR62.ResidLine74: SUPPORTED

# Tid 62 residual falsify — line 74 (S665) + reopen-row reproduction

Seat: KotodamaR62.ResidLine74 (read-only leaf). Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin, measured revision a2c5caa59b2d67ce35e53d6ce0217030a66cdd48. Claims/frozen predicates: reports/round-62/claims.json (freeze 9143fc44). No installs were made (no tool installed; python3 stdlib + curl only). Scratch: /fast/scratch/hyaku/kotodama-r62/resid/KotodamaR62.ResidLine74/standing-tall.html (113677 bytes, saved from the live fetch).

## 1. Measured-revision line 74 vs base

Command (read-only `git show`):

```
git show a2c5caa59b2d67ce35e53d6ce0217030a66cdd48:corpus/knowledge/culture-material/footwear-codes-terminology.md | sed -n '61,100p'
```

Line 74 at measured revision:

```
- A Bata Shoe Museum image caption says the heel originated in Western Asia centuries ago for horseback riding. (S665)
```

Line numbering verified by sed window: 63 = S692 open-list line, 74 = S665 line, 75 = S666 hedged line, 93 = S693 talaria line (matches accept-d.py LINES = {63:"S692", 74:"S665", 75:"S666", 93:"S687"} mapped to new S693). Base d42ffb89 line 74 was:

```
- A heel originated in Western Asia for horseback riding before Europeans adopted it. (S665)
```

## 2. Live page: where the quote actually sits

Fetch (ordinary means, curl, HTTP/2 200, saved to scratch):

```
timeout 120 curl -sSL --max-time 90 -A "Mozilla/5.0 ... Firefox/132.0" \
  "https://batashoemuseum.ca/standing-tall/" -o standing-tall.html
# HTTP/2 200, content-type: text/html; charset=UTF-8, date Fri 23 Oct 2026
# <title>Standing Tall: The Curious History of Men in Heels &#8211; Bata Shoe Museum</title>
```

The quoted sentence occurs exactly 3 times in the HTML, all inside the first gallery thumbnail ("Persian, 17th century") of the `.media-gallery` block — never in body prose:

1. `data-img-description` attribute of the wrapper `<a class="view view-first" data-fancybox="gallery" href="https://batashoemuseum.ca/wp-content/uploads/Iamge-1.jpg" data-img-title="Persian, 17th century" data-img-caption="" data-img-description="The heel was not a European invention, instead it originated in Western Asia centuries ago for horseback riding before Europeans adopted it at end of the 16th century. This pair of Persian men’s riding were associated with military prowess and equestrianism.">`
2. Same `data-img-description` on the nested `<img class="img-fluid" src="..." alt="" data-img-title="..." data-img-caption="" data-img-description="...">`
3. Visible thumbnail caption block inside `<div class="mask">`: `<h3 class="thumbnail-title">Persian, 17th century</h3>`, `<p class="thumbnail-caption"></p>`, `<p class="thumbnail-description"> …same sentence… </p>`

The gallery overlay uses these as the image caption: the page's fancybox config renders the caption from the data attributes:

```
caption : function(instance, item) {
    var imgTitle = $(this).data('img-title');
    var imgCaption = $(this).data('img-caption');
    var imgDescription = $(this).data('img-description');
    return '<h3 class="gallery-img-title">' + imgTitle + '</h3><p class="gallery-img-date">' + imgCaption + '</p><p class="gallery-img-description">' + imgDescription + '</p>';
}
```

So the quote is per-image gallery caption material (thumbnail caption + lightbox overlay caption), not page body prose. The museum's own markup labels the field `data-img-description` / `thumbnail-description`, but it functions as the gallery image caption, and row S665's anchor cell itself calls it "Persian, 17th century image caption".

Exact source sentence: "The heel was not a European invention, instead it originated in Western Asia centuries ago for horseback riding before Europeans adopted it at end of the 16th century. This pair of Persian men’s riding were associated with military prowess and equestrianism."

Row S665's anchor quote ("The heel was not a European invention, instead it originated in Western Asia centuries ago for horseback riding") is a verbatim prefix substring of that sentence.

## 3. Line 74 vs the caption

Line 74: "A Bata Shoe Museum image caption says the heel originated in Western Asia centuries ago for horseback riding."

- It names the source as an image caption ("image caption") and attributes it to the Bata Shoe Museum — accurate: the quote lives in the gallery image caption of the museum's Standing Tall exhibition page.
- It restates ONLY what that caption says: "the heel originated in Western Asia centuries ago for horseback riding" appears verbatim inside the caption sentence. Nothing in the clause goes beyond the caption.
- Omissions ("was not a European invention", "before Europeans adopted it") are within the predicate: LINK requires ≥3 shared ordered content words (satisfied; 10-word run "heel originated in western asia centuries ago for horseback riding" = LCS), COPY ≤12 consecutive words (10 ≤ 12), KEEP ≥60% base content words (base words [heel originated western asia horseback riding before europeans adopted] = 9; overlap = 6 = 66.7%). The L1 receipt records CAPTION PASS, LINK PASS, COPY PASS, KEEP PASS.

## 4. reopen-row.py reproduction (review-only evidence)

Exact commanded run:

```
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/reopen-row.py \
  --registry /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md \
  --passes 2 --gap 20 S665
```

Output:

```
ROW S665 CAPTION_ONLY attempts=1 url=https://batashoemuseum.ca/standing-tall/
REOPEN: 0/1 located
exit=1
```

CAPTION_ONLY is the tool's verdict for "quote found only in caption material (figcaption, caption/thumbnail/gallery classed element, or alt/title/aria-label/content/data-* attributes)" — exactly matching my manual finding (the quote sits in `data-img-description` + `.thumbnail-description` caption material, not body prose). Exit 1 is by design when not every row is LOCATED (docstring: 0 only when every row LOCATED); the frozen O counter's own fixture run in reports/round-62/telemetry/final-measures.txt records GEN rows=53 wrong=0, EXIT gen_exit=1 body_exit=0 default_registry_exit=0, so non-zero exit on non-LOCATED rows is expected behavior, not a tool defect. (I did not re-run accept-d.py; the L1 first run remains the authoritative receipt: ACCEPT-D-62: PASS at a2c5caa, 2026-10-23T12:05:14Z.)

## Findings

- P0/P1 defects: none. Line 74 at the measured revision restates only what the S665 caption says and names it as an image caption accurately; the live page still carries the quote verbatim (prefix substring) in its gallery image caption.
- P2 (informational, no fix required): the museum's own markup names the field "description" (`data-img-description`, `.thumbnail-description`) rather than "caption"; the entry's "image caption" wording is a fair functional name and matches the row's anchor label, so I do not count it as a defect. Also the row's anchor quote truncates the source sentence mid-way ("...for horseback riding" vs page's "...for horseback riding before Europeans adopted it at end of the 16th century."); truncation is verbatim and consistent with LINK; the remainder adds nothing that line 74 claims.

## Residual risk / verification gaps

- I checked the live page only; no Wayback capture was fetched (S665 is a base row — QUALITY 13's capture requirement applies to new rows S693–S699, not to S665).
- The page's sentence tail ("This pair of Persian men’s riding were associated...") reads truncated on the museum page itself; unrelated to line 74's restatement.
- Google Arts & Culture version of the exhibition exists (linked from the page) but was not checked; not needed for line 74.
