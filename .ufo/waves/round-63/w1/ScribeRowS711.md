# ScribeRowS711 — round 63 coverage item

## Behavior / source finding

The live University of Oxford page `https://www.ox.ac.uk/students/academic/dress` opened by ordinary static read as **Academic dress**. Its visible body text under “Additional notes” contains the 19-word quote: “The mortar board may be worn outdoors but must be removed as you enter buildings and carried whilst indoors.” The page date is not shown. Search of `corpus/SOURCES.md` found no existing match for this URL.

Locator command, run from the lane root:

```text
timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.ox.ac.uk/students/academic/dress' 'The mortar board may be worn outdoors but must be removed as you enter buildings and carried whilst indoors.'
```

Full stdout: `LOCATED https://www.ox.ac.uk/students/academic/dress`. The tool output did not separately record a numeric exit code. The locator was not run against a capture because none was obtained.

## Gates

- **Live quote:** LOCATED in the University of Oxford page body; the wording is not from a caption, alt/title attribute, or search snippet.
- **Archive quote / row validity:** BLOCKED. The prescribed Wayback CDX request returned HTTP 429; a plain `curl` request and the Internet Archive availability endpoint also returned HTTP 429. A direct Wayback wildcard request returned the generic Wayback landing page, not a capture of this page. No timestamp or capture URL was inferred. Therefore the same-page capture and archive locator requirement remain unverified.
- **S711 overall:** NOT COMPLETE. Do not append the rejected row draft or treat the entry/Gate candidates as ready. The source row cannot meet the required `live URL ; capture <Wayback id_ URL>` shape without the real capture.

The following alternatives were rejected: Britannica `https://www.britannica.com/topic/mortarboard` returned HTTP 404 and its CDX response was `[]`; Cambridge `https://www.cam.ac.uk/about-the-university/history/academic-dress` returned HTTP 404 and its CDX request returned HTTP 429. These candidate URL searches also found no matches in `corpus/SOURCES.md`.

Exact Oxford archive request URL: `https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fwww.ox.ac.uk%2Fstudents%2Facademic%2Fdress&output=json&limit=-5&filter=statuscode%3A200`.

Exact plain request command and outcome:

```text
curl -sS --max-time 60 -w '\nHTTP_STATUS=%{http_code}\n' 'https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fwww.ox.ac.uk%2Fstudents%2Facademic%2Fdress&output=json&limit=-5&filter=statuscode%3A200'
```

```text
<html><body><h1>429 Too Many Requests</h1>
You have sent too many requests in a given amount of time.
</body></html>

HTTP_STATUS=429
```

## Touched surfaces and out-of-scope

No product entry, registry row, source, counter, or tool was edited. The only lane-repository write is this required report. No control counter, O behavior, review gate, or other S694–S717 row was run or changed. No tools were installed.

## Scratch artifacts

- `/fast/scratch/hyaku/kotodama-r63/ScribeRowS711/row-candidate.txt` — explicitly rejected draft; missing real capture.
- `/fast/scratch/hyaku/kotodama-r63/ScribeRowS711/entry-bullet-candidate.txt` — provisional bullet; not ready to merge.
- `/fast/scratch/hyaku/kotodama-r63/ScribeRowS711/gate-line-candidate.txt` — live-only candidate; not Gate-ready.
- `/fast/scratch/hyaku/kotodama-r63/ScribeRowS711/locator-and-rejections.md` — live locator stdout and exact candidate/capture rejection evidence.
