# Round 62 W1 — ScribeHeelCaption (line 74)

## Finding and behavior

S665 supports the heel claim only as a gallery-image caption, not as the article’s prose. The fetched HTML places the text in both `data-img-description` fields and a `<p class="thumbnail-description">` nested under the media gallery’s `.mask`; `data-img-caption` is empty. The quote therefore is caption-scoped. The frozen locator still prints `LOCATED`: its HTML parser collects text nodes without distinguishing gallery captions from article body text, so that result is not a body-text verdict.

Observed HTML context (the same sentence occurs in both description locations):

```html
<a class="view view-first" data-fancybox="gallery" href="https://batashoemuseum.ca/wp-content/uploads/Iamge-1.jpg" data-img-title="Persian, 17th century" data-img-caption="" data-img-description="The heel was not a European invention, instead it originated in Western Asia centuries ago for horseback riding before Europeans adopted it at end of the 16th century. This pair of Persian men’s riding were associated with military prowess and equestrianism.
">
  <div class="mask">
    <p class="thumbnail-description">
      The heel was not a European invention, instead it originated in Western Asia centuries ago for horseback riding before Europeans adopted it at end of the 16th century. This pair of Persian men’s riding were associated with military prowess and equestrianism.
    </p>
  </div>
</a>
```

## Option A — retain S665, explicitly scope as caption

Draft line 74:

```text
- The image caption says the heel originated in Western Asia centuries ago for horseback riding. (S665)
```

It names the caption and restates only the supported claim. `[INFERENCE]` Manual LINK/COPY audit against the frozen rules: 10 content words; 7 exact content-word matches in quote order (threshold 4); longest consecutive copied run is 9 words (limit 12). This is a draft, not an `accept-d.py` result.

Locator command:

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py https://batashoemuseum.ca/standing-tall/ "The heel was not a European invention, instead it originated in Western Asia centuries ago for horseback riding"
```

Captured stdout: `LOCATED https://batashoemuseum.ca/standing-tall/`. The locator implementation returns 0 on `LOCATED`; no explicit `exit=` line was captured. The match is the caption text node described above, not article prose.

## Option B — new body-text row S695 and alternate line

BBC News has a body-text statement, attributed in the article to Bata Shoe Museum curator Elizabeth Semmelhack: “The high heel was worn for centuries throughout the near east as a form of riding footwear,”. The article’s next paragraph discusses horsemanship in Persia. This supports Near Eastern riding use; the quoted sentence itself does not say “originated,” so the alternative line avoids that stronger wording.

Draft SOURCES row (11 columns; not added to `SOURCES.md`):

```text
| S695 | William Kremer, “Why did men stop wearing high heels?”, BBC News, 2013-01-25 — https://www.bbc.com/news/magazine-21151350 ; capture https://web.archive.org/web/20260328053821id_/https://www.bbc.com/news/magazine-21151350 | docs | B | Near Eastern use of heels as riding footwear in BBC News’s historical account | Body text, historical section after “Originally, they weren’t.”, Elizabeth Semmelhack quotation: "The high heel was worn for centuries throughout the near east as a form of riding footwear," | BBC News reports the high heel as Near Eastern riding footwear worn for centuries. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

Draft alternate line 74:

```text
- The BBC reports that the high heel was worn for centuries across the Near East as riding footwear. (S695)
```

`[INFERENCE]` Manual LINK/COPY audit against the frozen rules: 10 content words; 8 exact content-word matches in quote order (threshold 4); longest consecutive copied run is 7 words (limit 12). The draft line makes no origin claim.

Locator commands and captured stdout:

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py https://www.bbc.com/news/magazine-21151350 "The high heel was worn for centuries throughout the near east as a form of riding footwear"
LOCATED https://www.bbc.com/news/magazine-21151350

timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py https://web.archive.org/web/20260328053821id_/https://www.bbc.com/news/magazine-21151350 "The high heel was worn for centuries throughout the near east as a form of riding footwear"
LOCATED https://web.archive.org/web/20260328053821id_/https://www.bbc.com/news/magazine-21151350
```

The locator returns 0 for each `LOCATED` result; explicit exit-code lines were not captured. CDX for the exact BBC URL returned a 200 HTML capture at `20260328053821`; the captured page was also read directly. A registry search for `magazine-21151350` and the article title returned no matches in `corpus/SOURCES.md`, so this live URL is not an observed reuse.

## Gates, touched surfaces, limits

- Read-only local sources consulted: `reports/round-62/claims.json`; round-61 verifier spot-check §7; `corpus/SOURCES.md` S665–S669; footwear entry lines 71–79; `reports/round-62/accept-d.py` frozen LINK/COPY/CAPTION rules; and `reports/round-61/reopen-quote.py` locator/parser.
- Public sources were fetched with ordinary reads (not a browser): Bata page and its raw HTML; BBC live article and the exact Wayback `id_` capture. The BBC capture index was checked via the ordinary CDX endpoint.
- Only the three locator invocations above were run. `accept-d.py`, ACCESS/LINT, the bounded multi-pass row locator, builds, and tests were not run. No installation was needed.
- No product file or SOURCES row was changed. This report is the only file written. The manual LINK/COPY counts are explicitly inference; the frozen acceptance counter has not judged either draft.
- Scope stops at line 74. Lines 63, 75, and 93, S693–S699 integration, and claim O are out of scope.

Artifact: `.ufo/waves/round-62/w1/ScribeHeelCaption.md`
