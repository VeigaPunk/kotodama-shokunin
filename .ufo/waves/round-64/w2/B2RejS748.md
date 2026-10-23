# B2RejS748 — S748 candidate retest

## Axis and finding

- **Axis:** coverage.
- **Disposition:** queued candidate, not rejected. The prior no-page ground does not still hold: the exact candidate URL returned HTTP 200 and the locator found the tested quote. The prior same-page archive-capture issue remains unresolved; this retest does not qualify the source as a mined row.
- **Candidate:** Anthony Rich, “Corona,” in William Smith’s *A Dictionary of Greek and Roman Antiquities* (John Murray, 1875), pp. 359–363; https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html. Kind `book`, tier B; scope is Roman military crowns and their assigned rewards.

## Exact retests

Command:

`curl -sS -o /dev/null -w '%{http_code} %{url_effective}' -L --max-time 60 'https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html'`

Verbatim output: `200 https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html`

Command:

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html' 'Among the honorary crowns bestowed by the Romans for military achievements'`

Verbatim first line: `LOCATED https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html`

The tested wording is 11 normalized words. The rejection ground that the path did not resolve to the entry no longer holds. The original absence of a verified same-page archive capture remains unresolved; no archive check was run here.

## Gates, touched surfaces, and limits

- **Exercised:** requested ordinary GET/status check and round-61 quote locator.
- **Not run:** ACCEPT-C-64 or other acceptance counters, build/tests, archive/CDX check.
- **Touched:** `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/RejS748/row.txt` and this requested report. No product code, corpus entry, registry, lane index, or jj state was changed. No tools were installed or updated.
- **Out of scope:** converting this candidate to a mined registry row; the same-page capture remains unresolved.

## Artifact paths

- Row and verbatim outputs: `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/RejS748/row.txt`
- Report: `.ufo/waves/round-64/w2/B2RejS748.md`
