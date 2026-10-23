# B2ReviewRowS718 — falsification review of inherited draft row S718

Draft: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS718/row.txt`
Full review: `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ReviewRowS718/review.md`

## HTTP results (verbatim)

- Live: `HTTP 200 https://pmc.ncbi.nlm.nih.gov/articles/PMC4794163/` (197,724 bytes, plain `curl -sL`, 2026-10-23)
- Capture: `HTTP 200 https://web.archive.org/web/20250212134043id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC4794163/` (193,353 bytes)
- `archive.org/wayback/available`: 429 rate-limited; capture verified by direct fetch instead.

## Lane locator (re-run verbatim, first line)

`LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC4794163/`

## Findings

| field | verified? | evidence |
|---|---|---|
| live URL / capture pair | YES | both 200; `id_` raw capture; capture original == live URL |
| anchor quote | YES | verbatim + contiguous in a `<p>` under `Results` heading: "…Rate in Utterances per Minute also indicate that Lebanese mothers, compared to American mothers, produced more IDS, a fact reflected in Fig 1 as well." — present in live body AND capture; not caption/alt/nav |
| citation | YES | meta tags: title identical; PLoS ONE; 2016 Mar 16; vol 11, issue 3; DOI 10.1371/journal.pone.0151518; authors Farran, Lee, Yoo, Oller |
| tier A | YES | original research paper; authoritative for its own reported result named by scope |
| scope | YES | body confirms "Lebanese Arabic-speaking … American English-speaking mothers" (19 Lebanese dyads, Arabic first language); rate in utterances per minute |
| teaches | YES | asserts only cross-community rate variability; no invented number |
| BULLET vs RESTATE | YES | hedged "in this sample"; ≥5 content words; in-order hits lebanese→mothers→produced / american→mothers; novel content words present; longest verbatim run = 2 (≤12); shape matches `- clause (S718)` |
| row shape (11 cells, mined, 2026-10-23, 180d, used-by) | YES | matches accept-c.py ROWS literals |

Required fixes: none.

VERDICT: CLEAN — quote verbatim in Results body text of live page and capture; citation, tier, scope, and bullet all verified; locator prints LOCATED.
