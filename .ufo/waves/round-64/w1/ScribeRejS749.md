# ScribeRejS749 — round 64

## Behavior and finding

The exact `web_search` query was `headgear listing descriptive`. The result included Wikipedia’s “List of headgear” as source [6], so this is the most likely candidate page [INFERENCE]; round-63 lesson prose does not identify this exact URL as the candidate opened. URL tested: https://en.wikipedia.org/wiki/List_of_headgear.

The page is live and its opening body sentence is a substantive, locatable claim about headgear purposes. The original ground — “the page only listed objects without a substantive, locatable claim” — does **not** still hold for this tested wording. Per the assignment’s exception, this is labelled `QUEUED-CANDIDATE`, not filed as a false rejection. The source is community / tier C; further admission would need stronger support and same-page capture evidence, neither tested here.

## Gates and exact evidence

Commands executed:

```text
curl -sS -o /dev/null -w '%{http_code} %{url_effective}' -L --max-time 60 'https://en.wikipedia.org/wiki/List_of_headgear'
200 https://en.wikipedia.org/wiki/List_of_headgear

cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://en.wikipedia.org/wiki/List_of_headgear' 'Headgear is worn for many purposes, including protection against the elements, decoration, or for religious or cultural reasons, including social conventions.'
LOCATED https://en.wikipedia.org/wiki/List_of_headgear
```

The locator quote is 21 words. Static `read` of the same URL returned the Wikipedia API page text, including the sentence and the list sections.

## Surfaces and limits

- Scratch artifact: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRejS749/row.txt`.
- Requested report: `.ufo/waves/round-64/w1/ScribeRejS749.md`.
- No corpus registry, knowledge entry, product code, counters, or tests were changed or run. No archive capture was tested, and the exact candidate URL’s round-63 provenance remains inferred rather than observed.
- No tools installed or updated.
