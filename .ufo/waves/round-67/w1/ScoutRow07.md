# ScoutRow07 - row-opening report (claim C)

## Deliverables
- `.ufo/waves/round-67/rows/ScoutRow07/row-S817.txt` - Milwaukee Public Museum, "Medicine and Healing" (Great Lakes Traditional Culture / Wisconsin Indian Resource Project). kind=docs, tier B. Live 200 curl-verified 2026-10-24; anchor quote verbatim in body; Wayback 20260312143012 (id_ byte-verified, quote present; fresh /save returned 429). URL unique against corpus/SOURCES.md + all corpus files (grep zero hits; normalized mpm.edu/... not in base or fragments).
- `.ufo/waves/round-67/rows/ScoutRow07/row-S818.txt` - Lopez Terrada 2009, "Medical Pluralism in the Iberian Kingdoms" (Medical History Supplement 29, pp. 7-25), PMC2836216. kind=paper, tier A (peer-reviewed, open full text). Live 200; quote verbatim; Wayback 20261016194944 (id_ byte-verified). URL unique.
- `.ufo/waves/round-67/rows/ScoutRow07/rejects.txt` - 3 rejected candidates with flip conditions (Met essay Vercel-429; Whittet PMC1033390 title-only + PDF proof-of-work gate; PMC10280199 displaced by museum source for the sweat-lodge row).

## Validation (counter's own functions from reports/round-67/accept-c.py)
Both rows: 11 cells, kind in enum, tier A/B, status mined, opened 2026-10-24, recheck 180d, used-by names the entry. Scope <=60 chars; teaches <=240; quote 8-25 words. Bullets: S817 3 in-order quote words / 8 novel / run 1 / 12 words; S818 3 in-order / 4 novel / run 3 / 10 words; teaches coverage 0.10 / 0.09. CAPTURE leg: capture-original query-aware-normalizes equal to live for both.

## Host diversity note
S817 host = mpm.edu; S818 host = pmc.ncbi.nlm.nih.gov (PMC is already used by base rows and likely siblings; HOSTS leg needs >=10 distinct hosts across all 24 - flag for the integrator).

## Environment / access notes
- Wayback /save/ rate-limited (429) both attempts; existing snapshots used instead, each fetched via id_ and byte-checked.
- PMC PDF endpoints sit behind a JS proof-of-work gate; HTML full text is unaffected.
- metmuseum.org hard-blocks curl entirely (Vercel checkpoint 429) - avoid for other rows.

## L1 sequencing note (post-resolution)
The C-APPEND vs Ca-D4 conflict is resolved by per-claim lands separation (A_r -> A_c -> A_ca): my S817/S818 rows are claim-C appends at A_c and need no change. My `rejects.txt` holds URL-level scout rejects only (the standard format) - it does NOT mint S829+ first-class rejected registry rows; those belong to ScoutReject1/ScoutReject2 (S829-S832) landing at A_ca. No action needed from this seat.

## Tooling installs
None needed (curl, python3, pdftotext already present). No pacman transactions.

Report: .ufo/waves/round-67/w1/ScoutRow07.md
