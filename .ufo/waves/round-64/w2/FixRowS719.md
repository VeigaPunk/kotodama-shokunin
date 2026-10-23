# FixRowS719 — claim C

Axes: **coverage**, **operability**, **calibration**.

## Change

Edited only `.ufo/waves/round-64/rows/ScribeRowS719/row.txt` (plus this report). The anchor, scope, tier B, and remaining row cells are unchanged. Updated the teaching summary to retain the review's qualifications; the flat-vs-caveated BULLET is:

- Old: `BULLET: - Infants attend preferentially to IDS-like prosody, helping caregivers attract a baby's attention. (S719)`
- New: `BULLET: - In reviewed studies, infants often attend preferentially to IDS-like prosody, but age, speaker, and stimulus conditions qualify this tendency. (S719)`

The B-tier survey supports the reported tendency but explicitly documents exceptions; retaining age/speaker/stimulus qualifications repairs calibration without narrowing the row's topic scope or weakening coverage.

## Evidence

- Re-fetched the live S719 URL to `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/FixRowS719/S719.pdf`; `file` reported PDF 1.3, 14 pages.
- Read the full relevant section in the reopened PDF. §3 reports newborn preference for maternal ADS over IDS, weaker IDS preference for male voices, age-related differences, and different drivers at 6 and 7–9 months. It says four simplified/synthetic pitch studies found one preference for pitch modulation, one opposite preference, and two null results. §4 restates the general IDS preference and explicitly appends “(with the aforementioned caveats).”
- Ran `python3 -B reports/round-61/reopen-quote.py 'https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content' 'The evidence summarized in Section 3 revealed that infants attend preferentially to IDS, and in particular to IDS-like prosody (with the aforementioned caveats).'`; result: `LOCATED https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content`.
- Ran `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows`; final result: `CHECK-ROWS: 32/32 clean`. The first run caught a missing `BULLET:` label in my edit; I corrected it before this passing run.

No tools installed. No blockers. Remaining risk is the source's own heterogeneous evidence, now expressly bounded in the bullet and teaching summary.
