# SentinelSources fetch ledger — round 76 w1 — 2026-10-27
# UA used for every recorded fetch: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36
# Bodies are NOT copied into the repo (rights-reserved text); sha256 below lets a re-fetch be compared byte-for-byte.

## status / final URL / host (curl -sS -I -L -A <UA>)
## code, redirects, host, ctype are from the HEAD pass; "GET bytes" is from the body GET (same UA, no cookie jar).

| key | code | redirects | host | ctype | GET bytes | final URL |
|---|---|---|---|---|---|---|
| S894-live | 200 | 0 | www.digital.archives.go.jp | text/html;charset=UTF-8 | 311308 | https://www.digital.archives.go.jp/search |
| S894-cap | 200 | 0 | web.archive.org | text/html;charset=UTF-8 | 307700 | https://web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search |
| S895 | 200 | 0 | www.xingzuobaike.com | text/html; charset=utf-8 | 33179 | https://www.xingzuobaike.com/huangli/wannianli/d165803.html |
| S896-cap | 200 | 0 | web.archive.org | text/html;charset=utf-8 | 8075 (gzip; 24174 decoded) | https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 |
| S896-orig | 200 | 0 | openstd.samr.gov.cn | text/html;charset=utf-8 | 24144 | https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 |
| S897 | 200 | 1 | openstd.samr.gov.cn | text/html;charset=utf-8 | 24144 | https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter  (302 from .../std/showGb?type=online&hcno=...) |
| S898 | 200 | 0 | news.gmw.cn | text/html | 8076 | https://news.gmw.cn/2017-05/23/content_24559485.htm |
| S892-held | 200 | 0 | web.archive.org | application/pdf | 763802 | https://web.archive.org/web/20251111222249if_/https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf |
| S885-held | 200 | 0 | www.persee.fr | text/html;charset=utf-8 | 111487 | https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113 |

## additional route spellings probed (same authority, all 302 -> /bzgk/std/newGbInfo)
/bzgk/std/showGb?type=download&hcno=...   -> 200, 24144, md5 e866bfd6...
/bzgk/gb/newGbInfo?hcno=...               -> 200, 24144, final .../bzgk/std/newGbInfo?hcno=...
/bzgk/gb/showGb?type=online&hcno=...      -> 200, 24144, final .../bzgk/std/newGbInfo?hcno=...&refer=outter


## body sha256
80b4c781f4b772107427218dc0a3596842a66388a5c05635679787fe41530aa9  body-896orig.html
f04feb475163287e85238628d5425846fde0118ce277daca7081c76058101e0e  body-896cap.dec.html
830495598c1f769095438473b8cfb7819d9906f730713a1ba95ac016d077735e  body-895.html
670850ea26dd6de7d480a80d95381d21107b9fbc3cd32414bd4a80123a2366f1  body-898.html
204b7188493573f85b0a7d394983ce90e1a1b1280786643de6c60fc50b763ea8  body-894live.html
c015e1dce915d4c9f3d3fa6d04e25605cc59547526284372de55112f268a13e0  body-894cap.raw
813bdb125fa9f43a3003994ba42dc2549fbd778043de5f460b164f5125f28832  jiedu.pdf

## openstd route identity (showGb/newGbInfo, online/download), 2 runs each
e866bfd61a16f4c4fcdc1fc3a16bdf89  route-download-1.html
e866bfd61a16f4c4fcdc1fc3a16bdf89  route-download-2.html
e866bfd61a16f4c4fcdc1fc3a16bdf89  route-online-1.html
e866bfd61a16f4c4fcdc1fc3a16bdf89  route-online-2.html

## UA binding delta (openstd record page)
browser-UA bytes=24144  curl-UA bytes=24057
diff of the two responses:
340c340
<     		var userAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36';
---
>     		var userAgent = 'curl/8.5.0';
record-field block md5 (browser vs curl):
c609e73c5018dd7cbdb42094f2ac8775  -
c609e73c5018dd7cbdb42094f2ac8775  -

## mirror-vs-official-document containment (xingzuobaike vs pmo.cas.cn 解读材料 PDF)
pdf=813bdb125fa9f43a3003994ba42dc2549fbd778043de5f460b164f5125f28832  pdf_pages=5  pdf_chars=8735
content lines=27 in_pdf=21 not_in_pdf=6 ; normative-clause markers on the mirror page = 0

## NAJ era table: live vs 2026-04-22 capture
button-list md5 identical: cc88460841fee4655e7633b8bb9ea2a8 == cc88460841fee4655e7633b8bb9ea2a8

## direct iris.unipa.it (lane S892's withdrawn original), plain request
code=403 size=5867  (capture used; recorded in lane S892 already)
