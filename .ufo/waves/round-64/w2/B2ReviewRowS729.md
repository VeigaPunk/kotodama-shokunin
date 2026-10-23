# B2ReviewRowS729 — falsification review of inherited draft S729

Draft under review: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS729/row.txt` (wave-1 inheritance, unverified).
Counter: `reports/round-64/accept-c.py` legs ROWS (shape) and RESTATE (entry-line support). S729 is not in the LIVE leg subset.
Full review: `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ReviewRowS729/review.md`.

## HTTP results (verbatim, 2026-10-23)

- Live: `HTTP=200 EFFECTIVE=https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518` — 214386 bytes HTML, plain GET.
- Capture: `HTTP=200 EFFECTIVE=https://web.archive.org/web/20261002073140id_/https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518` — served gzip on the wire; gunzips to 214386 bytes **byte-identical to live** → same-page capture. Wayback API: `status 200, timestamp 20261002073140`.
- Lane locator re-run: `python3 -B reports/round-61/reopen-quote.py '<URL>' '<quote>'` → `LOCATED https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518` (exit 0).

## Anchor quote

Normalised (NFKC/casefold/non-word→space, counter-identical): 17 words (8–25 ✓). FOUND verbatim at body-text offset 24980, Results statistics paragraph:
`…statistically significant effect of language f 3 32 8 43 p 006 partial eta squared 19 with the lebanese mothers using more ids utterances per minute across both registers than the american mothers figs 1 and 2…`
Body text, not heading/caption/alt/nav. Locator prefix `Results, paragraph on utterance rates:` accurate.

## Verdict table

| field | draft value | verified? | evidence (verbatim) | required fix |
|---|---|---|---|---|
| Row shape | 11 cells | yes | 11 cells, no `\|` inside, used-by names the entry path | none |
| Citation | Farran, Lee, Yoo & Oller, 2016, PLOS ONE 11(3) e0151518 | yes | meta: `citation_title` exact; authors in doc order Farran/Lee/Yoo/Oller; `citation_date = Mar 16, 2016`; volume 11, issue 3, firstpage e0151518, DOI 10.1371/journal.pone.0151518 | none |
| kind | `paper` | yes | `citation_article_type = Research Article` | none |
| tier | `A` for its scope | yes | original primary article — authoritative for exactly the scoped comparison | none |
| anchor quote | as drafted | yes | verbatim, contiguous, 17 words, Results body paragraph | none |
| live URL / capture | as drafted | yes | both HTTP 200; capture content = live bytes; capture-original = live URL | none |
| scope | "…infants aged 0–24 months" | yes (minor nit) | Lebanese cohort `0–24 months`, American cohort `1–24 months`; study frame "first two years" | none required |
| teaches | "Helps worldbuilders portray Lebanese mothers using more infant-directed speech per minute than the study's American comparison mothers." | yes | faithful paraphrase of quoted result | none |
| status/date/recheck | `mined` \| 2026-10-23 \| 180d | yes | matches ROWS leg | none |
| BULLET | `- Lebanese mothers use more infant-directed speech across both registers in this caregiving setting (S729)` | yes | RESTATE sim: 11 content ≥5; 6 in-order hits ≥3 (lebanese→mothers→more→across→both→registers); copy run 3 ≤12; novel {infant,directed,speech,caregiving,setting}. Clause asserts only what the quote establishes, hedged; no invented number | none |
| Trailer lines | LOCATED / timestamp=20261002073140 / plain curl HTTP 200 | yes | all reproduced by this seat | none |

## Residual risk

- Scope's "0–24 months" fits the Lebanese cohort exactly; the American cohort was recruited 1–24 months — cosmetic, claim does not hinge on it.
- Bullet elides "per minute" rate and the explicit American comparison; legal restatement (in_order 6/3, novel 5). Any L1 rewrite must keep ≥3 in-order quote content words.
- Capture endpoint serves gzip unless `--compressed`; harmless to the counter, noted for other reviewers.

## Tooling

No installs. curl, python3 stdlib, file, cmp — all present.

VERDICT: CLEAN — quote verbatim in Results body text (LOCATED), citation/tier/scope accurate, bullet passes RESTATE, live+capture HTTP 200 same-page.
