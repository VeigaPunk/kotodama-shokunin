# ScribeSrc05 — Round 61 source research

## Behavior and coverage

Coverage axis: four located source anchors, two on Persian riding heels/high-heel history and two on Japanese geta/zori. All retained URLs were opened by ordinary static reading and their exact anchor quotes were located live. Draft IDs remain `S6??` in every row, entry line, and Gate line; L1 assigns final IDs at integration. These are source drafts, not rows committed to `corpus/SOURCES.md` or an integrated entry.

Retained sources are tiered to the stated scope: Bata Shoe Museum and Japan Search are institutional/authoritative records for the scopes listed; BBC is strong secondary reporting; SFO Museum is a strong institutional interpretation. No Wayback captures were needed. No retained source presented an access challenge. A separate Web Japan candidate fetch failed with HTTP 403; it was not used and no bypass was attempted.

## Drafts

### Persian riding heels and high-heel origins

**SOURCES row (draft):**

```text
| S6?? | Standing Tall: The Curious History of Men in Heels — Bata Shoe Museum, 2019-03-11 — https://batashoemuseum.ca/standing-tall/ | docs | A | Western Asian riding heels and European adoption | Persian, 17th century image caption: "The heel was not a European invention, instead it originated in Western Asia centuries ago for horseback riding" | The museum caption says heels originated in Western Asia for horseback riding centuries before Europeans adopted them. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

**Entry line (draft):**

```text
- A heel originated in Western Asia for horseback riding before Europeans adopted it. (S6??)
```

**Gate line (draft):**

```text
- S6?? | https://batashoemuseum.ca/standing-tall/ | 2026-10-23 | "The heel was not a European invention, instead it originated in Western Asia centuries ago for horseback riding"
```

Locator command and full output:

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://batashoemuseum.ca/standing-tall/' 'The heel was not a European invention, instead it originated in Western Asia centuries ago for horseback riding'
LOCATED https://batashoemuseum.ca/standing-tall/
```

Registry grep: `corpus/SOURCES.md`, pattern `batashoemuseum\.ca/standing-tall` → `No matches found`.

**SOURCES row (draft):**

```text
| S6?? | Six surprising facts about the history of high heeled shoes — BBC Radio 4, You're Dead to Me — https://www.bbc.co.uk/programmes/articles/qsXBljJrnRm60Gdt2PR362/six-surprising-facts-about-the-history-of-high-heeled-shoes | docs | B | Persian evidence for early heel-wearing | section 2, “Heeled shoes were originally designed for Medieval soldiers”: "The earliest evidence we have of someone wearing heels is from a 10th-century Persian bowl." | The article names a 10th-century Persian bowl as its earliest evidence of someone wearing heels. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

**Entry line (draft):**

```text
- The earliest evidence of someone wearing heels comes from a 10th-century Persian bowl. (S6??)
```

**Gate line (draft):**

```text
- S6?? | https://www.bbc.co.uk/programmes/articles/qsXBljJrnRm60Gdt2PR362/six-surprising-facts-about-the-history-of-high-heeled-shoes | 2026-10-23 | "The earliest evidence we have of someone wearing heels is from a 10th-century Persian bowl."
```

Locator command and full output:

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.bbc.co.uk/programmes/articles/qsXBljJrnRm60Gdt2PR362/six-surprising-facts-about-the-history-of-high-heeled-shoes' 'The earliest evidence we have of someone wearing heels is from a 10th-century Persian bowl.'
LOCATED https://www.bbc.co.uk/programmes/articles/qsXBljJrnRm60Gdt2PR362/six-surprising-facts-about-the-history-of-high-heeled-shoes
```

Registry grep: `corpus/SOURCES.md`, pattern `bbc\.co\.uk/programmes/articles/qsXBljJrnRm60Gdt2PR362/six-surprising-facts-about-the-history-of-high-heeled-shoes` → `No matches found`.

### Japanese geta and zori

**SOURCES row (draft):**

```text
| S6?? | Japanese Wooden Clogs — Japan Search, last updated 2024-03-01 — https://jpsearch.go.jp/en/gallery/ndl-GZqzDNvVK0a | docs | A | Japanese footwear categories, geta construction and history | body, “Traditional Japanese footwear” paragraph: "Traditional Japanese footwear can be roughly divided into two groups: zori sandals and geta wooden clogs." | Japan Search divides traditional footwear into zori and geta and describes geta design, craft, changing styles, and period uses. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

**Entry line (draft):**

```text
- Traditional Japanese footwear is roughly divided into zori sandals and geta wooden clogs. (S6??)
```

**Gate line (draft):**

```text
- S6?? | https://jpsearch.go.jp/en/gallery/ndl-GZqzDNvVK0a | 2026-10-23 | "Traditional Japanese footwear can be roughly divided into two groups: zori sandals and geta wooden clogs."
```

Locator command and full output:

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://jpsearch.go.jp/en/gallery/ndl-GZqzDNvVK0a' 'Traditional Japanese footwear can be roughly divided into two groups: zori sandals and geta wooden clogs.'
LOCATED https://jpsearch.go.jp/en/gallery/ndl-GZqzDNvVK0a
```

Registry grep: `corpus/SOURCES.md`, pattern `jpsearch\.go\.jp/en/gallery/ndl-GZqzDNvVK0a` → `No matches found`.

**SOURCES row (draft):**

```text
| S6?? | Stepping Out: Shoes in World Cultures — SFO Museum (2017) — https://www.sfomuseum.org/exhibitions/stepping-out-shoes-world-cultures/gallery | docs | B | zori/geta comparison and Edo-period urban use | “Stilted sandals (geta)” gallery text: "Similar to the zori but elevated in height, geta became fashionable in urban areas during the Edo period (1615–1868)." | SFO Museum describes geta as elevated relative to zori and says they became fashionable in urban areas during the Edo period. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

**Entry line (draft):**

```text
- Geta, elevated relative to zori, became fashionable in urban areas during the Edo period. (S6??)
```

**Gate line (draft):**

```text
- S6?? | https://www.sfomuseum.org/exhibitions/stepping-out-shoes-world-cultures/gallery | 2026-10-23 | "Similar to the zori but elevated in height, geta became fashionable in urban areas during the Edo period (1615–1868)."
```

Locator command and full output:

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.sfomuseum.org/exhibitions/stepping-out-shoes-world-cultures/gallery' 'Similar to the zori but elevated in height, geta became fashionable in urban areas during the Edo period (1615–1868).'
LOCATED https://www.sfomuseum.org/exhibitions/stepping-out-shoes-world-cultures/gallery
```

Registry grep: `corpus/SOURCES.md`, pattern `sfomuseum\.org/exhibitions/stepping-out-shoes-world-cultures/gallery` → `No matches found`.

## Gates, touched surfaces, and limits

- **LOCATE:** PASS for all four retained live URLs; the four exact `LOCATED` lines above are the receipts.
- **Registry freshness screen:** all four host/path patterns returned `No matches found` in the current `corpus/SOURCES.md`.
- **Entry-line shape:** each draft is one bullet with one placeholder S-id, has at least three exact 4+-letter words shared with its quote, and copies no more than 12 consecutive quote words.
- **Access:** `https://web-japan.org/nipponia/nipponia21/en/topic/index.html` failed to fetch with HTTP 403; not retained, no archive fallback tried. DITSONG's curator article and BBC Learning English were opened as additional candidates but not retained. No retained page required a Wayback capture.
- **Touched surface:** this report only, `.ufo/waves/round-61/w1/ScribeSrc05.md`. No product files, registry rows, entry, README, lesson, or counters changed or ran. No tools were installed.
- **Out of scope / limits:** these are four sourced drafts only; no claim is made that claim C, the 20-row floor, or any counter gate passes. IDs are deliberately unresolved as directed by L1. No build/test/lint/counter run was performed.
- **Artifact:** `.ufo/waves/round-61/w1/ScribeSrc05.md`.
