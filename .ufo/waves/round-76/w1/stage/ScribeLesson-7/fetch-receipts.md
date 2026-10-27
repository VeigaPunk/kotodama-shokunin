# Wave-1 fetch receipts — ScribeLesson-7 (round 76, kotodama)

ua on every request below: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

access date: **2026-10-27**. One plain request per URL; no header spoofing beyond the UA, no cookie, no login, no challenge solved.
`wire bytes` is curl's `%{size_download}` (compressed bytes as sent); `stored bytes`/`sha256` are the body this directory keeps (`fetch/`), decompressed by curl `--compressed`.

| row | carrier | url requested | status chain | content-type | wire bytes | stored bytes | sha256 (stored) | visible chars (non-space) | server date |
|---|---|---|---|---|---|---|---|---|---|
| S894 | live | https://www.digital.archives.go.jp/search | HTTP/2 200 | text/html;charset=UTF-8 | 311308 | 311308 | `204b7188493573f85b0a7d394983ce90e1a1b1280786643de6c60fc50b763ea8` | 5402 | 2026-10-27 fetch clock (no Date header on HTTP/2 response) |
| S894 | capture | https://web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search | HTTP/1.1 200 (1st of 3 attempts; attempts 2 and 3 died at TCP, curl exit 7) | text/html | 307700 | 307700 | `c015e1dce915d4c9f3d3fa6d04e25605cc59547526284372de55112f268a13e0` | 5323 | 2026-10-27 fetch clock |
| S895 | live | https://www.xingzuobaike.com/huangli/wannianli/d165803.html | HTTP/2 200 | text/html; charset=utf-8 | 9093 | 33179 | `830495598c1f769095438473b8cfb7819d9906f730713a1ba95ac016d077735e` | 3954 | 2026-10-27 fetch clock |
| S896 | live | https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296 | HTTP/1.1 302 -> Location .../newGbInfo?hcno=...&refer=outter -> HTTP/1.1 200 | text/html;charset=utf-8 | 7334 | 24144 | `80b4c781f4b772107427218dc0a3596842a66388a5c05635679787fe41530aa9` | 689 | Tue, 27 Oct 2026 21:35:30 GMT |
| S896 | capture | https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 | HTTP/1.1 200 (gzip on the wire; stored body decompressed) | text/html | 8075 | 24174 | `f04feb475163287e85238628d5425846fde0118ce277daca7081c76058101e0e` | 689 | 2026-10-27 fetch clock |
| S898 | live | https://news.gmw.cn/2017-05/23/content_24559485.htm | HTTP/1.1 200 OK (gzip on the wire) | text/html | 8076 | 25250 | `670850ea26dd6de7d480a80d95381d21107b9fbc3cd32414bd4a80123a2366f1` | 1519 | Tue, 27 Oct 2026 21:35:30 GMT |

**Failed attempts in the same window.** `web.archive.org` (the S935 and S932 carriers): two of three attempts aborted before any HTTP response — `curl: (7) Failed to connect to web.archive.org:443`, exit 7; the attempt that connected returned HTTP/1.1 200 with 307700 B (S935). The capture kept here is the one that connected.

**No access control was met.** No response above was a 403/429/503, a captcha (altcha, hCaptcha, reCAPTCHA), a `Just a moment...` interstitial, a login wall or a paywall; every recorded response is the document itself.

**Route tests (same UA, same window)** — the registry's own alternate routes, all resolving to one URL:

| route | status chain | wire bytes | stored bytes | sha256 (stored) |
|---|---|---|---|---|
| `showGb?type=online&hcno=…` | 302 -> newGbInfo?hcno=…&refer=outter -> 200 | 7334 | 24144 | `80b4c781f4b772107427218dc0a3596842a66388a5c05635679787fe41530aa9` |
| `showGb?type=download&hcno=…` | 302 -> newGbInfo?hcno=…&refer=outter -> 200 | 7334 | 24144 | `80b4c781f4b772107427218dc0a3596842a66388a5c05635679787fe41530aa9` |
| `/bzgk/gb/newGbInfo?hcno=…` | 301 -> `/bzgk/std/newGbInfo` -> 200 | 7334 | 24144 | (same bytes as the two rows above; the seat compared with `md5sum`, which printed `e866bfd61a16f4c4fcdc1fc3a16bdf89` three times) |

The download route carries no `Content-Disposition` header and returns the record page, not a file.
