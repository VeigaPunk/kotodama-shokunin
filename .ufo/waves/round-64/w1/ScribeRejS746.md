# ScribeRejS746 — S746 rejection-row re-test

## Behavior and disposition

The likely typewriter-related Wikisource page is the U.S. Copyright Office catalogue scan/transcription, *1977 Books and Pamphlets, July–December*, p. 2333, entry A888375 (“Smith-Corona owner's handbook, manual typewriters”):
`https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447`

`web_search` for `"Wikisource Smith Corona"` first returned the unrelated Smith-edited *A Dictionary of Greek and Roman Antiquities/Corona* entry as the closest Wikisource match. A follow-up `site:en.wikisource.org "Smith Corona" typewriter` identified the 1977 handbook catalogue listing as the direct typewriter-related match. The round-63 lesson records only “Wikisource Smith's Corona (no captures)” and does not preserve a URL or the candidate quotation. I therefore tested a reconstructed 14-word excerpt from the handbook listing itself, not an unrecorded quotation claimed by the round-63 seat.

For that reconstructed wording, the ground does **not** hold: the page returns HTTP 200 and the locator returns `LOCATED`. The original round-63 ground remains indeterminate because its exact candidate quotation is not present in the available lesson record. This is consequently marked `QUEUED-CANDIDATE`, not submitted as a verified rejection. The proposed row keeps the prescribed 11-cell/rejected-row shape, but the queued label is its disposition and it is not ready to integrate.

## Tests and gates

Exact ordinary requests run:

```text
curl -sS -o /dev/null -w '%{http_code} %{url_effective}' -L --max-time 60 'https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447'
=> 200 https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447

cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447' "Smith-Corona owner's handbook, manual typewriters. 38 p. Add. ti: Owner's handbook for manual typewriters"
=> LOCATED https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447
```

Verbatim command outputs: `200 https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447`; `LOCATED https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447`.

The tested string is present in the extracted page text under entry A888375. Criterion 12's output-evidence requirement is met for this re-test. No archive lookup, browser challenge, captcha, paywall, or access-control workaround was attempted.

## Touched surfaces, scope, and limits

- Wrote the proposed queued row to `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRejS746/row.txt`.
- Wrote this scoped report to `.ufo/waves/round-64/w1/ScribeRejS746.md`.
- No registry, lesson, knowledge entry, product code, judge, counter, or other repo file was changed. No acceptance suite/build/lint/test was run; no tool was installed.
- The original round-63 candidate wording and its URL cannot be confirmed from the round-63 lesson. Recover those exact inputs and re-test before filing a confirmed S746 rejection.

## Artifact

`/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRejS746/row.txt` — queued candidate row plus the exact re-test outputs.
