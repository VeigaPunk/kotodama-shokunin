# S744 — rejected ushanka candidate

## Finding and provenance
- **Claim/axis:** C, coverage. Rejection row for routed defect 7 from `corpus/lessons/round-63-verifier-spotcheck.md:100`.
- **Candidate reconstruction:** `corpus/lessons/round-63.md:44-47` explicitly records `dictionary.com/browse/ushanka` as redirecting to Khanka with no entry; spot-check line 81 gives the full redirect target and says it was a predecessor candidate for S714. This is the most likely opened candidate, and the tested URL was `https://www.dictionary.com/browse/ushanka`.
- **Search provenance:** `web_search` query `"ushanka hat"` returned a Glosbe snippet defining ushanka as “a traditional Russian fur cap with earflaps that can be tied up on top or fastened under the chin to protect the ears, jaw, and neck from cold”; its results also said Dictionary.com did not appear to have a separate ushanka entry and linked to `/browse/shapka`. The 14-word opening of that snippet was tested as headgear wording against the disputed Dictionary.com URL; it is not attributed to Dictionary.com.

## Re-test and outcome
- Exact curl command: `curl -sS -o /dev/null -w '%{http_code} %{url_effective}' -L --max-time 60 'https://www.dictionary.com/browse/ushanka'`
- Verbatim curl output: `200 https://www.dictionary.com/browse/khanka?q=ushanka&noredirect=true&mismatchType=misspelling`
- Exact candidate-wording locator command: `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.dictionary.com/browse/ushanka' 'a traditional Russian fur cap with earflaps that can be tied up on top'`
- Verbatim locator first line: `NOT_LOCATED https://www.dictionary.com/browse/ushanka quote-absent` (exit 1).
- Corroborating destination-quote locator command: `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.dictionary.com/browse/ushanka' 'Lake, a lake in far SE Russia and NE China, N of Vladivostok.'`
- Verbatim locator output: `LOCATED https://www.dictionary.com/browse/ushanka` (exit 0). The located quote is the lake definition, not headgear wording.
- A native read of the final URL showed the `Khanka` headword and definition “Lake, a lake in far SE Russia and NE China, N of Vladivostok,” with “Showing results for Khanka” and “Search instead for ushanka.” No challenge or paywall was encountered or bypassed.
- **Ground:** still holds. The locator did not find the tested headgear wording; it located the Khanka lake definition on the redirect destination. Thus the quote-found exception for a candidate headgear quote does not apply.

## Row
`row.txt` contains the exact three required labelled lines and the proposed S744 row. Kind/tier follow the existing Dictionary.com `docs`/`B` convention; the scope is the dictionary evidence that would support ushanka as headgear.

## Gates, touched surfaces, and limits
- **Gate:** the requested live-fetch and locator re-tests were run. No `ACCEPT-C-64` script or broader acceptance gate was run.
- **Touched surfaces:** wrote only this scoped report (the item explicitly requested it) and scratch artifact `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRejS744/row.txt`. No registry row or product/corpus entry was edited.
- **Out of scope / limits:** no archive capture was sought; the evidence here is the ordinary live request and the locator outputs above. The tested candidate wording came from the separate Glosbe search result, not from Dictionary.com.

Artifacts: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRejS744/row.txt`; `kotodama-shokunin/.ufo/waves/round-64/w1/ScribeRejS744.md`.