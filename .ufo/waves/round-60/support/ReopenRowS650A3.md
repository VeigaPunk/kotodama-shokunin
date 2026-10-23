HOLDS

# Reopen S650 (falsify)

Frozen tree `47f27bd0cb0bea219f21cd731c2eb0fe71f7f626` (`HEAD` is that commit). Working-tree `corpus/SOURCES.md` rows S650 and S623 are byte-equal to that blob. No tools installed. Sandbox: `/fast/scratch/hyaku/kotodama-r60a3/ReopenRowS650A3/`. Confidence: high. The linked site `https://theconcealedrevealed.wordpress.com` was not opened; the carrying sentence is in the Footwear Research Network article itself.

## Row at the freeze

`corpus/SOURCES.md:605` (13 cells). Source cell has one URL and no Wayback URL.

| cell | value |
|---|---|
| id | S650 |
| source | `https://footwearresearchnetwork.org/articles/concealed-shoes-revealed` (direct, HTTP 200, 248354 bytes; accessed 2026-10-23) — Rebecca Shawcross, 2022, "Concealed Shoes Revealed", Footwear Research Network, 4 February 2022 |
| kind | docs |
| tier | B |
| scope | Shawcross's account of concealed shoes found in buildings, including the uncertainty and interpretations of their purpose |
| anchor | University of Hertfordshire research paragraph (`locate_in=True`): "currently suggests less and less that they were specifically apotropaic items, ones that have the power to avert evil influences or bad luck" |
| teaches | supersedes S623 — Shawcross reports that University of Hertfordshire research currently suggests less and less that concealed shoes were specifically apotropaic items, and that they were connected to notions of good luck and hope. |
| status | mined |
| opened | 2026-10-23 |
| recheck | 2027-10-23 |
| used-by | `corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md` |

S623 (`corpus/SOURCES.md:578`) first URL is the same string: `https://footwearresearchnetwork.org/articles/concealed-shoes-revealed`. Same page.

## Live fetch vs pin

Ordinary GET (curl, Firefox UA, redirects allowed). No redirect, no challenge page.

- HTTP 200, `content-type: text/html;charset=utf-8`, `size_download=248354`, `url_effective` is the row URL, `num_redirects=0`.
- sha256 `5e353d2f81f4c6ee4dca42362a36ec56981c6e4247dadc95a108f5e1bb432ef5` on both the live body and `reports/round-60/captures/S650.bin`.
- `captures/manifest.json` `S650`: bytes 248354, same sha256, same URL, `fetched_at` 2026-10-23T05:37:02Z, http 200. `cmp` of pin and live body: identical.
- Squarespace answered with a `set-cookie: crumb=…` and `age: 16761`. The body is the article, not an interstitial.

Access note `(direct, HTTP 200, 248354 bytes; accessed 2026-10-23)` matches this fetch and the pin.

No Wayback capture is listed on the row (source cell, manifest URL, or page bytes). `archive.org` count in `S650.bin` is 0; `wayback` count is 0. None fetched.

## Quote

Anchor quote (23 words) locates.

`python3 -B reports/round-60/reopen-quote.py --row S650` → `LOCATED https://footwearresearchnetwork.org/articles/concealed-shoes-revealed` exit 0.

Same result with the URL and the frozen quote as two arguments, exit 0.

Pinned HTML text node 1890 is that quote verbatim, then an en dash and the good-luck clause. Preceding nodes name the researchers inside the same sentence (link text, not a second claim).

## Tier, scope, byline, date

`corpus/SOURCES.md:14-18`: **B** is a strong secondary (expert write-up with reproducible detail). This page is Senior Shoe Curator Rebecca Shawcross's essay on the Northampton Museum concealed-shoe collection. B is not inflated (not filed as A) and not a lead (not C). S623 for the same page is also B.

Scope matches the page: concealed shoes in buildings, plus an explicit uncertainty and rival interpretations. It does not repeat S623's narrower "English buildings" (the page also records finds outside England). Scope is narrower than the whole page (object descriptions, index statistics) and not wider.

Byline and date on the page:

- `<meta itemprop="author" content="Rebecca Shawcross"/>`
- JSON-LD `author` Rebecca Shawcross, `datePublished` `2022-02-04T08:17:33+1100`, headline Concealed Shoes revealed
- visible `<time … datetime="4 Feb">` / `<span>4 Feb</span>`
- og:description: "Senior Shoe Curator Rebecca Shawcross explores…"

"4 February 2022" is the publisher's calendar date (the `+1100` instant is 3 February UTC). The word "February" is not in the body; the year is in `datePublished`, the day-month in the time element.

## Entry line

`corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:103` at the freeze, the only `S650` cite in that file:

`- Concealed shoes: Shawcross says the reason why people concealed shoes remains a mystery; University of Hertfordshire research currently suggests less and less that they were specifically apotropaic items, and that they were connected to notions of good luck and hope (S650). **C**`

Calibration key at line 16: **C** means hedged by the row itself. The page hedges ("remains a mystery", "suggests"); **C** is not a separate factual clause.

| clause | page sentence | verdict |
|---|---|---|
| Concealed shoes (topic) | Title node: "Concealed Shoes Revealed — Footwear Research Network" | carried |
| Shawcross says the reason why people concealed shoes remains a mystery | "As common as this practice appears to have been, the reason why people concealed shoes remains a mystery." (text node 1663; author metadata Rebecca Shawcross) | carried |
| University of Hertfordshire research currently suggests less and less that they were specifically apotropaic items | "The research undertaken by The University of Hertfordshire in particularly Professor Owen Davies and Dr Ceri Houlbrook, currently suggests less and less that they were specifically apotropaic items, ones that have the power to avert evil influences or bad luck – and that they were connected to notions of good luck and hope." (nodes 1888–1890) | carried (page also names Davies and Houlbrook and keeps the appositive "ones that have the power…") |
| and that they were connected to notions of good luck and hope | same sentence, after the en dash: "and that they were connected to notions of good luck and hope." | carried |

Not the same sentence: node 1887, "a practice that builders might do this during renovations to bring good luck in their work." That line has neither "hope" nor "notions of good luck". The entry's "good luck and hope" is the Hertfordshire sentence, not the builders sentence.

`**C**` is the calibration mark, not a page clause. The page's own hedge carries it.

## Commands and full output

```
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD
47f27bd0cb0bea219f21cd731c2eb0fe71f7f626
```

Cell split of `git show 47f27bd0…:corpus/SOURCES.md` (both rows): S650 line 605, 13 cells, lengths 0/6/223/6/3/123/211/232/7/12/12/68/0. S623 line 578, lengths 0/6/203/6/3/92/215/122/10/12/12/3/0. Cell text is the table above. Working tree vs that blob: `S650 equal True`, `S623 equal True`.

```
sha256sum …/reports/round-60/captures/S650.bin
5e353d2f81f4c6ee4dca42362a36ec56981c6e4247dadc95a108f5e1bb432ef5  …/S650.bin
wc -c → 248354

curl -sS -L --max-redirs 5 -A 'Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0' \
  -D live.headers -o live.bin -w '…' \
  'https://footwearresearchnetwork.org/articles/concealed-shoes-revealed'
http_code=200
size_download=248354
content_type=text/html;charset=utf-8
url_effective=https://footwearresearchnetwork.org/articles/concealed-shoes-revealed
redirect_url=
num_redirects=0

sha256sum live.bin
5e353d2f81f4c6ee4dca42362a36ec56981c6e4247dadc95a108f5e1bb432ef5  …/live.bin
wc -c → 248354

HTTP/2 200
accept-ranges: bytes
age: 16761
content-type: text/html;charset=utf-8
date: Fri, 23 Oct 2026 03:10:36 GMT
etag: W/"632a8d3b8a7d5de39bb2bde33353b989"
expires: Thu, 01 Jan 1970 00:00:00 GMT
server: Squarespace
set-cookie: crumb=BRh0y5lJWtsDNWVmNTBiYjI1ZjlmNWZjNGE0YmFhOWZiMDgxMDFh;Secure;Path=/
strict-transport-security: max-age=15552000
vary: Accept-Encoding
x-content-type-options: nosniff
x-contextid: Vzeb34c7/ayVRuZ9a
x-frame-options: SAMEORIGIN
x-frame-options: SAMEORIGIN

cmp -s pin live && echo CMP_PIN_LIVE_IDENTICAL
CMP_PIN_LIVE_IDENTICAL
```

```
python3 -B reports/round-60/reopen-quote.py --row S650
LOCATED https://footwearresearchnetwork.org/articles/concealed-shoes-revealed
EXIT:0
python3 -B reports/round-60/reopen-quote.py 'https://footwearresearchnetwork.org/articles/concealed-shoes-revealed' \
  'currently suggests less and less that they were specifically apotropaic items, ones that have the power to avert evil influences or bad luck'
LOCATED https://footwearresearchnetwork.org/articles/concealed-shoes-revealed
EXIT2:0
```

Page counts in `S650.bin`: Shawcross 10, Rebecca 10, February 0, 2022 5, archive.org 0, wayback 0. ISO dates in the file: `2022-02-04`, `2022-02-07`.
