# S702 — veil as garment (round 63)

## Behavior / proposed artifacts
Official Victoria and Albert Museum (V&A) Blog article “A Romantic Frame of Mind” by Susanna Cordner (published 2015-02-11; the page identifies Furniture, Textiles and Fashion) directly discusses the wedding veil’s face-framing and symbolic roles. The evidence is in the article’s opening body paragraph, not an image caption, alt text, title, or search snippet. Scope should remain V&A’s Western bridal-fashion account, not all religious or everyday veiling.

### Registry row (11 cells)
| S702 | “A Romantic Frame of Mind,” Susanna Cordner, Victoria and Albert Museum (V&A Blog), 2015-02-11 - http://www.vam.ac.uk/blog/here-come-brides/a-romantic-frame-of-mind ; capture http://web.archive.org/web/20170729170856id_/http://www.vam.ac.uk/blog/here-come-brides/a-romantic-frame-of-mind | docs | A | V&A account of Western bridal-veil style, face framing and symbolism in wedding wear; not a global account of religious or everyday veiling | Opening entry-content paragraph, first two sentences | "a wedding veil flatters and frames the woman’s face. As in all aspects of wedding wear tradition, a veil must balance style with symbolism" | Bridal veils frame the face and balance fashion with symbolism in the V&A’s wedding-wear account | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |

The chosen live URL is the HTTP spelling because CDX’s selected capture embeds that exact original URL. The body locator located the quote at that exact live URL. The HTTP spelling is accepted by the frozen URL rule; no redirect behavior is asserted here.

### Entry bullet
- A wedding veil flatters and frames the woman’s face, balancing style with symbolism (S702)

The clause has 9 content words after normalization; 8 occur in quote order; longest copied run is 10 normalized words (≤12); `balancing` adds a content word outside the quote. It carries one S-id.

### Gate line
- S702 | http://www.vam.ac.uk/blog/here-come-brides/a-romantic-frame-of-mind | 2026-10-23 | "a wedding veil flatters and frames the woman’s face. As in all aspects of wedding wear tradition, a veil must balance style with symbolism"

The anchor quote is 24 normalized words.

## Gates and evidence

### Locator runs
Live source, complete 24-word quote:
```text
timeout 300 python3 -B reports/round-61/reopen-quote.py 'http://www.vam.ac.uk/blog/here-come-brides/a-romantic-frame-of-mind' 'a wedding veil flatters and frames the woman’s face. As in all aspects of wedding wear tradition, a veil must balance style with symbolism'
LOCATED http://www.vam.ac.uk/blog/here-come-brides/a-romantic-frame-of-mind
exit=0
```

Selected CDX capture, same quote (first run):
```text
timeout 300 python3 -B reports/round-61/reopen-quote.py 'http://web.archive.org/web/20170729170856id_/http://www.vam.ac.uk/blog/here-come-brides/a-romantic-frame-of-mind' 'a wedding veil flatters and frames the woman’s face. As in all aspects of wedding wear tradition, a veil must balance style with symbolism'
LOCATED http://web.archive.org/web/20170729170856id_/http://www.vam.ac.uk/blog/here-come-brides/a-romantic-frame-of-mind
exit=0
```

Conflicting repeat on the same capture and quote (do not collapse this with the prior pass):
```text
timeout 300 python3 -B reports/round-61/reopen-quote.py 'http://web.archive.org/web/20170729170856id_/http://www.vam.ac.uk/blog/here-come-brides/a-romantic-frame-of-mind' 'a wedding veil flatters and frames the woman’s face. As in all aspects of wedding wear tradition, a veil must balance style with symbolism'
NOT_LOCATED http://web.archive.org/web/20170729170856id_/http://www.vam.ac.uk/blog/here-come-brides/a-romantic-frame-of-mind HTTPError
exit=1
```

The same 2017 capture was also opened through `read` in raw mode; its `<p>` body contains the entire quote. A separate locator attempt on another CDX capture (2015-09-06) returned `NOT_LOCATED http://web.archive.org/web/20150906153524id_/http://www.vam.ac.uk/blog/here-come-brides/a-romantic-frame-of-mind HTTPError`, exit 1. A later 2026-07-30 capture’s raw HTML also showed the quote in its body, but its locator returned `NOT_LOCATED http://web.archive.org/web/20260730003624id_/https://www.vam.ac.uk/blog/here-come-brides/a-romantic-frame-of-mind quote-absent`, exit 1. The selected 2017 capture therefore has mixed locator results; the positive and negative evidence is reported verbatim for the canonical judge.

### CDX evidence and URL uniqueness
First HTTPS CDX request returned HTTP 429. Subsequent ordinary CDX reads succeeded. The exact `limit=5` query used for the chosen HTTP URL was:
```text
https://web.archive.org/cdx/search/cdx?url=http%3A%2F%2Fwww.vam.ac.uk%2Fblog%2Fhere-come-brides%2Fa-romantic-frame-of-mind&output=json&limit=5&filter=statuscode%3A200
```
It returned five 200 text/html records: 20150217173700 (`http://www.vam.ac.uk:80/blog/here-come-brides/a-romantic-frame-of-mind`), 20150316023659 (same :80 URL), 20150503135205 (the same path without :80), 20150906153524 (same path), and 20170729170856 (same path). The selected last record has digest `2CKRRAQTHLDLUUI3JMWXBPWNMIJSNAMW`, length 11000, and its embedded original equals the chosen live URL.

The `limit=-5` HTTPS query also returned five 200 text/html captures for the same article path: 20250604212324, 20250911030037, 20251216175525, 20260422081035, and 20260730003624. The capture inventory is multi-snapshot, although the locator outcomes above remain mixed.

URL reuse checks: searching `corpus/SOURCES.md` for the exact HTTP and HTTPS article URL returned no matches. Searching `.ufo/waves/round-63/w1/` for this article path returned no matches. The independent RevRowS702 peer confirmed their 1911 Britannica/Wikisource URL is different.

## Rejections / known limits
- `https://www.britannica.com/topic/veil-dress` returned HTTP 404.
- `https://www.britannica.com/topic/veil` exposed a curated AI quick summary and related coverage, not a full original veil article; no generated-summary quote was used.
- Britannica’s wimple body contained a relevant passage, but the exact ordinary locator run returned `NOT_LOCATED https://www.britannica.com/topic/wimple HTTPError` (exit 1); rejected.
- V&A’s default `read` selection returned its comments feed. Its `:raw` read fetched the actual article HTML and body paragraph; the base locator independently located the live quote.
- No counter was run, so this is not an `ACCEPT-C-63` judgment. No source row or entry was integrated into the lane by this seat.

## Touched surfaces / out of scope
Only this scratch artifact and the assigned report file are to be written. No product source, registry, knowledge entry, counter, claim, or judge was edited; no test or counter was run; no tool was installed. Claim O and whole-entry integration are out of scope.

## Artifact paths
- Scratch: `/fast/scratch/hyaku/kotodama-r63/ScribeRowS702/S702.md`
- Assigned report: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-63/w1/ScribeRowS702.md`
