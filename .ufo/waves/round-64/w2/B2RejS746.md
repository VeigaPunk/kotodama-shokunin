# B2RejS746 — S746 rejection-row repair

- **Axis:** coverage.
- **Behavior / disposition:** queued candidate, not rejected. The round-63 lesson preserves only “Wikisource Smith's Corona (no captures)” and does not give the original URL or quotation. The reconstructed Wikisource page serves the typewriter catalogue entry and the reconstructed wording is locatable. That contradicts rejecting this reconstructed wording; the original rejection ground cannot be confirmed without the original exact quote.
- **Candidate URL:** https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447
- **What it supports:** the catalogue's A888375 entry identifies a 38-page Smith-Corona owner's handbook for manual typewriters. It does not support a headgear claim.

## Gates and evidence

Commands were run against the reconstructed page using ordinary HTTP and the lane locator:

```text
curl -sS -o /dev/null -w '%{http_code} %{url_effective}' -L --max-time 60 'https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447'
200 https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447

cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447' "Smith-Corona owner's handbook, manual typewriters. 38 p. Add. ti: Owner's handbook for manual typewriters"
LOCATED https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447
```

**Ground still holds?** Not established for the unknown round-63 quote. For the reconstructed quote, no: the locator finds it on the live page (HTTP 200). Accordingly the row is `queued`, not a false `rejected` disposition.

## Touched surfaces and limits

- Wrote the required row artifact only in `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/RejS746/row.txt`.
- Wrote this scoped report at `.ufo/waves/round-64/w2/B2RejS746.md` as explicitly requested.
- No other lane files, registry rows, or product code were changed. No archive-capture test or acceptance script was run; exact historic wording is absent from the round-63 lesson.

## Artifact paths

- `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/RejS746/row.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-64/w2/B2RejS746.md`
