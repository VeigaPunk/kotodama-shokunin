# B2ReviewRowS734 — per-row falsification review (claim C, wave 2)

Subject: inherited wave-1 draft `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS734/row.txt`
Full verdict table: `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ReviewRowS734/review.md`

## HTTP results (verbatim)

- Live: `HTTP 200 https://pmc.ncbi.nlm.nih.gov/articles/PMC2614655/` (body 213871 bytes)
- Capture: `HTTP 200 https://web.archive.org/web/20250319021450id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC2614655/` (body 209519 bytes; capture citation_title + PMID 18062986 identical to live)
- Locator: `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC2614655/`
- No challenge met; plain GET on both fetches.

## Findings

- ROW shape: 11 cells, tier A, mined, 2026-10-23, 180d, used-by names the entry; capture original == live URL. All ROWS checks pass.
- Anchor quote verbatim and contiguous in the abstract body text (single occurrence), 16 normalized words; not a heading/caption/nav string.
- Citation verified against page metadata: authors Wenner, Burch, Lynch, Bauer (all four correct); title identical to `citation_title`; JECP 101(1), 1-19 matches `citation_volume/issue/firstpage`; year 2008 is the correct issue year (page meta: "issue date 2008 sep"; the page's "2007 Dec 11" string is the online-first date only — non-blocking observation, not a wrong-year defect).
- Tier A justified: original research paper's own record for exactly the scoped topic.
- BULLET satisfies RESTATE mechanically (shape, 13 content words, 6 in-order, copy run 5, 7 novel words) and asserts only what the quote establishes ("may learn", "plausible route" — no overreach, no invented numbers).
- Teaches cell and scope accurately describe the paper's design (reminiscence vs. independent fictional narratives).

## Required fixes

None.

VERDICT: CLEAN all cells, quote, citation, tier, scope and bullet verified against HTTP-200 live page and matching archive capture; no fix required.
