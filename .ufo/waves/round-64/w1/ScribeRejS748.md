# ScribeRejS748 — S748 candidate retest

## Axis and verdict

- **Axis:** coverage.
- **Ground:** “the path with the asterisk did not resolve to a page” does **not** still hold. The exact HTTPS candidate path returns HTTP 200 at itself, its content is the Corona article, and the round-61 quote locator returns `LOCATED` for the candidate quote. The prior spotcheck states: “live asterisk path → 302 to the site home page.”
- Per the assignment's contradiction rule, this is a **QUEUED-CANDIDATE**, not a rejected row. The existing no-page reason is not filed as a current rejection. The prior S696 scribe record still marks the same-page archive capture unresolved; this retest did not resolve capture eligibility.

## Candidate identification and provenance

Read `corpus/lessons/round-63.md` first, then `corpus/lessons/round-63-verifier-spotcheck.md`. The latter identifies the S696 first source as LacusCurtius's Corona page and describes the asterisk-path failure. The original `.ufo/waves/round-63/w1/ScribeRowS696.md` supplies the exact source citation, URL, and quote: Anthony Rich, “Corona,” in William Smith's *A Dictionary of Greek and Roman Antiquities* (John Murray, 1875), pp. 359–363; `https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html`; “Among the honorary crowns bestowed by the Romans for military achievements.” This is a `book`, tier `B` candidate for Roman military crown forms and their assigned rewards.

`web_search` was run with the requested query `LacusCurtius asterisk path`. Additional searches for the Corona path identified the same Smith/Anthony Rich article. The native static read of the HTTPS page returned title `LacusCurtius • Roman Wreaths and Crowns (Smith's Dictionary, 1875)`, the `p359 Corona` heading, the author and page-range description, and the article body. No challenge, login, or paywall was encountered or bypassed.

## Exact retests

1. Command:

   `curl -sS -o /dev/null -w '%{http_code} %{url_effective}' -L --max-time 60 'https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html'`

   Verbatim output: `200 https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html`

2. Command:

   `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html' 'Among the honorary crowns bestowed by the Romans for military achievements'`

   Verbatim first line: `LOCATED https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html`

The quote is 11 normalized words. These outputs are preserved verbatim in `row.txt` as `TEST` and `TEST2`.

## Gates, touched surfaces, and limits

- **Exercised:** candidate discovery, ordinary live GET via the requested curl command, and the requested quote locator.
- **Not run:** acceptance counters, build, tests, census, or archive/CDX capture check. No tool was installed or updated.
- **Touched:** the requested scratch artifact `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRejS748/row.txt` and this requested wave report only; no product code, registry, corpus entry, or lane index was changed.
- **Limit:** this establishes that the page and quote resolve now. It does not establish an archived capture or meet the mined-row evidence gate. The row is queued rather than rejected to avoid asserting a contradicted failure.

## Artifact paths

- Row and verbatim test outputs: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRejS748/row.txt`
- Report: `.ufo/waves/round-64/w1/ScribeRejS748.md`
