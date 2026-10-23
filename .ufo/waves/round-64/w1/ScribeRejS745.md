# ScribeRejS745 — S745 candidate retest

## Behavior and verdict

The most likely round-63 headgear candidate is Merriam-Webster.com Dictionary, “tiara”: `https://www.merriam-webster.com/dictionary/tiara`. Round-63's `ScribeRowS710.md` records the Merriam-Webster quote “a decorative jeweled or flowered headband or semicircle for formal wear” and reports HTTP 403; S710 is the tiara seat. The round-63 lesson records Merriam-Webster refusals among the rejected headgear candidates. The seat artifact did not print the Merriam-Webster URL, so the exact URL attribution is a reconstruction; this is the standard Merriam-Webster `tiara` entry URL and is the URL tested here.

The stated ground still holds on the requested ordinary probes: curl returned HTTP 403 and the quote locator returned `NOT_LOCATED ... HTTPError` (exit 1). The response body was discarded as specified by the curl command, so the report asserts the observed refusal status and locator failure, not any unobserved response-body text. No challenge was solved or bypassed.

## Exact retest commands and outcomes

1. `curl -sS -o /dev/null -w '%{http_code} %{url_effective}' -L --max-time 60 'https://www.merriam-webster.com/dictionary/tiara'`

   Verbatim output: `403 https://www.merriam-webster.com/dictionary/tiara`

2. `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://www.merriam-webster.com/dictionary/tiara' 'a decorative jeweled or flowered headband or semicircle for formal wear'`

   Verbatim first-line output: `NOT_LOCATED https://www.merriam-webster.com/dictionary/tiara HTTPError` (exit 1). The tested quote is 11 words.

## Row artifact

`/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRejS745/row.txt` contains the required `ROW`, `TEST`, and `TEST2` lines with the two observed outputs. Its row classifies the source as `docs`, tier `A` for the scoped lexical definition, and keeps the candidate rejected with a stated flip condition. The quote is 11 words, within the locator's 8–25-word range.

## Provenance and findings

- Read `corpus/lessons/round-63.md` first; it describes Merriam-Webster refusals among the headgear rejects but does not identify the exact Merriam-Webster URL.
- Read `corpus/lessons/round-63-verifier-spotcheck.md`; routed defect 7 says rejected candidates were not curated as registry rows.
- Read `.ufo/waves/round-63/w1/ScribeRowS710.md`; it gives the Merriam-Webster definition quote and records direct curl 403 and locator `HTTPError` for the tiara candidate.
- Ran `web_search` for `Merriam-Webster dictionary entry`. The visible results included Merriam-Webster's generic `ENTRY Definition & Meaning` page and help pages; this search did not identify the tiara candidate by itself. The round-63 S710 evidence and headgear context identify tiara as the most likely candidate.

## Gates, touched surfaces, and limits

- **Gate exercised:** ordinary live request and the instructed round-61 quote locator, re-testing the criterion-12 grounds.
- **No claim counter** (`ACCEPT-C-64`) was run; no registry row or product code was edited. This artifact stages the rejection row for integration but does not establish the coverage claim's acceptance.
- **Touched surfaces:** this scoped report and the scratch `row.txt` only. No tool was installed or updated.
- **Out of scope:** no archive/CDX lookup, browser, challenge bypass, or unrelated claim-O/claim-Ca work.

## Artifact paths

- Row and verbatim outputs: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRejS745/row.txt`
- This report: `.ufo/waves/round-64/w1/ScribeRejS745.md`
