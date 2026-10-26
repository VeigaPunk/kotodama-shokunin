# ScoutWaybackCarriers — round 75 wave 1

## Method and control

The draft claims/ledger were read first; neither was edited. CDX probes used `http://web.archive.org/cdx/search/cdx?url=<URL>&output=json&filter=statuscode:200&limit=10`; where needed, `limit=-10` was also used to obtain the latest captures. A separate positive control used the same `output=json&filter=statuscode:200` shape against `https://en.wikipedia.org/wiki/Narrative`; it returned status-200 captures, including `20261009122432` (10 returned in the last-10 query). Thus the successful empty UCASS response is not a malformed-query/control failure. Some archive requests to `web.archive.org` later failed with connection refused; HTTPS and retries recovered selected probes. These gaps are noted below.

Live requests below were made once per URL for each listed UA using `curl/8.23.0`, following redirects (`-L`). Exact browser UA: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`. “wall marker” records content visibly identifying a block/challenge, not a page's ordinary feature such as Persée's hidden PDF-download CAPTCHA widget. Timestamps are CDX timestamps in UTC.

## Candidate URLs: Wayback and live results

| Candidate / probed URL (verbatim) | CDX status-200 observations; latest | CDX `original` agrees with live URL? | Live curl default UA response | Browser-UA response |
|---|---|---|---|---|
| S885 `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113` | Returned 10 rows in last-10 query; latest `20261005135926`; returned sample begins `20251123103450` | Yes: CDX `original` is exactly the HTTPS URL | HTTP 200, 109582 B, HTML; no blocking wall (page contains ordinary `pdf-download-captcha-widget`, not an interstitial) | HTTP 200, 109589 B, HTML; no blocking wall |
| S886 `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120` | 10 returned; latest `20261002231615`; sample begins `20230605015239` | Yes, exact HTTPS original | HTTP 200, 109329 B, HTML; no blocking wall | HTTP 200, 109336 B, HTML; no blocking wall |
| S887 `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114` | 10 returned; latest `20261006095414`; sample begins `20230117100359` | Yes, exact HTTPS original (one other row's original used HTTP, but latest/other rows include exact HTTPS) | HTTP 200, 118770 B, HTML; no blocking wall | HTTP 200, 116879 B, HTML; no blocking wall |
| Persee page-level URL `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113?pageId=T1_2` | 10 returned; latest `20261004024135`; earliest in returned last-10 `20220624045337` | Yes: CDX `original` preserves URL/query as given | HTTP 200, 111331 B, HTML; no blocking wall | HTTP 200, 111338 B, HTML; no blocking wall |
| S888 `https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf` | Exact CDX response `[]` (0 rows; no status-200 capture under this URL) | N/A: no capture | HTTP 200, 225123 B, PDF; no blocking wall | HTTP 200, 225123 B, PDF; no blocking wall |
| S889 `https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf` | 2 rows; earliest `20201212045824`; latest `20240904135913` | Yes: exact HTTPS original | HTTP 200, 1085244 B, PDF; no blocking wall | HTTP 200, 1085244 B, PDF; no blocking wall |
| S890 `https://www.jstage.jst.go.jp/article/jsik/32/2/32_2022_017/_pdf` | 2 rows; earliest `20220704171942`; latest `20260108033329` | Yes: exact HTTPS original | HTTP 200, 697092 B, PDF; no blocking wall | HTTP 200, 697092 B, PDF; no blocking wall |
| S891 `https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html` | 2 rows; earliest `20030908073936`; latest `20041220223357` | Capture `original` is `http://www.unige.ch:80/lettres/framo/cernet/biblio/barth70.html`; host/path agree, scheme/default port normalize to the HTTPS live URL | HTTP 200, 245 B, HTML containing `Request Rejected` / “requested URL was rejected” (refusal marker) | HTTP 200, 46712 B, HTML, bot-management interstitial (`/TSPD/3000` code; not the source page) |
| S892 front door `https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014 marrone age dor---2.pdf` (request encoded spaces as `%20`) | 1 row; timestamp `20251111222249` | Yes: CDX `original` is `https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf`, same path after space/`%20` normalization | HTTP 403, 5676 B, HTML wall marker `<title>Just a moment...</title>` / Cloudflare challenge | HTTP 403, 5867 B, HTML wall marker `<title>Just a moment...</title>` / Cloudflare challenge |

### Exact CDX URL probes and capture identity

The `url=` values queried (including the encoded iris path) were the exact URLs in the table. The persee page-level URL was discovered from live page HTML: its `pageId=T1_2` link. CDX rows for all captures above named the probed page in their `original` field except Unige's legacy HTTP/default-port spelling, which normalizes to the HTTPS live URL. Iris's CDX row gives original timestamp `20251111222249`; direct capture request `https://web.archive.org/web/20251111222249id_/https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf` returned HTTP 200, 763802 B, `application/pdf`; body identified as PDF. Its response `Link: rel="original"` names the same iris retrieve path (percent-encoded by Wayback), and `x-archive-orig-content-length: 763802`. This is the same-page archive capture, not just a metadata landing page.

The exact first-10 and last-10 raw JSON responses were kept in the scratch during probing. Count terminology above is rows returned by the specified capped query, not asserted total CDX cardinality. CDX requests that failed to connect are not counted as zero.

## Front-door/redirect check and unresolved edge

HEAD requests were made for each live URL. Persée and both J-STAGE PDF URLs returned their document directly (J-STAGE `Content-Disposition` filenames `25_200.pdf` and `32_2022_017.pdf`); UCASS returned the PDF directly. Iris's HEAD request got HTTP 403 with `cf-mitigated: challenge`, and its GETs likewise got challenge walls; no `Location` target was exposed. Therefore no live redirect target could be discovered/probed for Iris without passing the challenge, which I did not do. The Wayback capture itself is the PDF at the same retrieve URL. Unige HEAD reset the connection; live GET differed by UA as reported, so no redirect target was observed there either.

The positive-control probe returned captures as expected. The CDX probe for `https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf` returned an empty JSON array under the exact tested slug; report phrasing: **no capture under `https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf`**. This result does not imply no alternative URL/canonical slug exists; no redirect was observed on live HEAD.

## Evidence limits / disposition relevance

- UCASS is live and serves a 225123-byte PDF to both UAs, but the tested URL has no returned status-200 capture. Under QUALITY 18 this lacks the required same-page capture; if its live body serves the quote to a re-opener, durability is still absent under the stated criterion.
- Unige's capture original normalizes to the live URL, but live responses were non-source/refusal content: curl default got a 245-byte “Request Rejected” body and browser UA got an interstitial. The browser-shaped UA is only a request header sent by curl; no browser automation, challenge solving, or bypass was used. This source could not be verified live in these probes.
- Iris has a positive same-page PDF capture matching the URL, but both live UAs received Cloudflare challenge pages. Do not treat the challenge response as a source opening; no challenge was passed. No redirect target was exposed.
- Persee pages respond 200 to both UAs. Their HTML includes a hidden PDF-download CAPTCHA widget, but the document pages themselves were returned; the probes did not invoke the widget or any protected transcription endpoint. The page-level `?pageId=T1_2` URL also responded 200 for both UAs.

Scratch artifacts were removed before handoff. No tools were installed.