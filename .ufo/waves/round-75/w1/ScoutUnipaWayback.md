# ScoutUnipaWayback — S919 / proposed S892

## Observed fetches (2026-10-27)

Commands run from `/fast/scratch/hyaku/kotodama-r75/ScoutUnipaWayback`:

```sh
curl -sS -o live-browser.body -D live-browser.headers -w 'HTTP_STATUS:%{http_code}\nBYTES:%{size_download}\nCONTENT_TYPE:%{content_type}\nURL_EFFECTIVE:%{url_effective}\n' -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' 'https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf'
```
Raw output: `HTTP_STATUS:403`, `BYTES:5867`, `CONTENT_TYPE:text/html; charset=UTF-8`, effective URL unchanged; `cf-mitigated: challenge`, title `Just a moment...`; wall time `real 0m0.454s`; sha256 `73139543b39fbe77a1c1211d727b388b25ead6727dc7fbdd9ca977e5dc4ed4c7`. UA exactly as shown above.

Additional comparison request (not a challenge bypass): same URL, `-A 'curl/8.23.0'`; raw output `HTTP_STATUS:403`, `BYTES:5697`, `CONTENT_TYPE:text/html; charset=UTF-8`, URL unchanged; `cf-mitigated: challenge`, title `Just a moment...`; wall time `real 0m0.411s`; sha256 `34227f5491b340a0280bab86eeba6b3b50cd587486a5b0063413d5ca154e81bb`. Thus the live URL is challenged under both UAs; challenge was met and not passed.

```sh
curl -sS -o wayback.pdf -D wayback.headers -w 'HTTP_STATUS:%{http_code}\nBYTES:%{size_download}\nCONTENT_TYPE:%{content_type}\nURL_EFFECTIVE:%{url_effective}\n' -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' 'https://web.archive.org/web/20251111222249if_/https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf'
```
Raw output: `HTTP_STATUS:200`, `BYTES:763802`, `CONTENT_TYPE:application/pdf`, effective URL unchanged; wall time `real 0m1.809s`; sha256 `8c0303670ff5db8625d034be958ad5729a2c79fa77f3642efc5f6341fb25a19a`. Response has `memento-datetime: Tue, 11 Nov 2025 22:22:49 GMT`, `x-archive-orig-content-type: application/pdf;charset=UTF-8`, and `x-archive-orig-content-length: 763802`. UA exactly as shown above. `pdfinfo`: 25 pages; producer Adobe PDF Library 10.0.1.

Extraction command: `pdftotext -enc UTF-8 wayback.pdf wayback-text.txt`; extracted 73,505 bytes. The passage is on PDF page 7, printed page 58 (page header reads `58`). Located text:

> “Mais combien, et de quelle nature, sont ces codes ?”

Quote length: 10 whitespace-separated words, 51 characters including punctuation. It is followed by the five-code list: proaïretique, sémantique, culturel, herméneutique, symbolique. The relation claim is explicitly present: “ces cinq codes sont en partie une reformulation des quatre niveaux du récit individués dans l’« Introduction à L’analyse structurale des récits » (1966) : fonctions, actions, indices et informants.” The next discussion states “Le code proaïretique est en quelque sorte une synthèse des fonctions et actions”. These confirm the staged five-codes-origin claims, including the partial (not total) relationship and the proairetic synthesis. (Text extracted with `pdftotext`; source page image itself was not independently inspected in this run.)

## CDX canonical-slug probe / positive control

Exact query command shape:

```sh
curl -sS 'https://web.archive.org/cdx/search/cdx?url=iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf&output=text&matchType=exact' -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -w '\nHTTP_STATUS:%{http_code}\nBYTES:%{size_download}\n'
```
Probed URL is the direct live PDF URL (the direct request's effective URL was unchanged, so no redirect target was returned). Raw CDX row: `it,unipa,iris)/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf 20251111222249 https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf application/pdf 200 WUQOTMBFQNXZDSOQTVPOY6B7DHMX2YVF 759396`; HTTP 200, 274 bytes. A doubled-escape `%2520` exact probe also returned that same normalized CDX row (HTTP 200, 274 bytes). An exploratory `matchType=prefix` query on the path with `*` returned HTTP 200 and 0 bytes; treated as an invalid/empty probe, not evidence of absence.

Positive control, same CDX endpoint and exact-query shape, probed URL `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113`: HTTP 200, 8,184 bytes; output contains numerous archived captures, including 200 status rows. This establishes the query is operational; no no-capture ruling is made here.

The preliminary `http://web.archive.org/cdx/...` attempt failed to connect to port 80 (curl exit 7, HTTP 000, 0 bytes); successful probes used HTTPS.

## Proposed lane registry row (11 columns)

`| S892 | Gianfranco Marrone, « L’âge d’or de la sémiotique littéraire, et quelques conséquences théoriques », Signata 5 (2014), pp. 57–72 — Internet Archive capture of the University of Palermo publisher deposit — https://web.archive.org/web/20251111222249if_/https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf | paper | B | The scholarly literature’s account of the relation between Barthes’s five codes and the four levels in the 1966 Introduction, including its explicit limitation to a partial reformulation; not a primary source for Barthes’s 1966 text. | Printed p. 58, passage beginning « Mais combien, et de quelle nature, sont ces codes ? »; “ces cinq codes sont en partie une reformulation des quatre niveaux” (11 words, 66 characters); following discussion: “une synthèse des fonctions et actions”. | Establishes that Marrone describes the five codes as a partial reformulation of the 1966 four levels, and describes the proairetic code as a synthesis of functions and actions. | mined | 2026-10-27 | 180d | corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-24.md |`

Tier B: the scope is a peer-reviewed scholar’s interpretation, not an authoritative primary account of Barthes’s 1966 article; community is not A. The live host’s Cloudflare challenge was not passed; the ordinary Wayback capture supplied the readable copy.

## Verdict

**ADMIT.** The archived PDF is a valid PDF capture, its timestamp matches the staged capture, and both central origin claims locate in extracted text on printed p. 58. This supports the scoped scholarly-literature claim, not an independent claim that Marrone’s interpretation is definitive. Flip to REFUSE/UNVERIFIABLE if the capture ceases to return the document or if a page-level/visual check contradicts the extracted passage; do not treat the live 403 alone as a reason to refuse the reachable ordinary archive copy.