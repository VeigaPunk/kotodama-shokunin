# ScoutRow04 — round-66 w1 — ROW-OPENING (claim C)

Opened exactly two registry rows, S783 and S784, at:
- `.ufo/waves/round-66/rows/ScoutRow04/row-S783.txt`
- `.ufo/waves/round-66/rows/ScoutRow04/row-S784.txt`

No rejects (zero candidates discarded; no rejects.txt written).

## S783 — Hungary Water (docs, tier B)
- Source: Hunt Institute for Botanical Documentation (Carnegie Mellon University), online exhibition "Virtues and Pleasures of Herbs through History," Fragrance → Rosemary essay.
- Live URL `https://www.huntbotanical.org/virtues-pleasures-herbs/page.php?Fragrance-4` — curl 200, quote verbatim in body, no redirect/paywall.
- Anchor (17 words): first-named alcohol-based perfume, "Hungary water", produced around 1370. Teaches cell adds the serpentine-cooler/high-proof-alcohol commercialization mechanism — all verbatim-supported by the same paragraph.
- Wayback capture 20201101061450id_ fetched and quote-verified; it is the freshest snapshot of this URL per the availability API (checked with timestamp=20261024 during the outage).

## S784 — Grasse perfumery UNESCO ICH (docs, tier A)
- Source: official UNESCO element page, element 01207 (note: element number is 01207, not 01307; the 01307 URL in my initial guess silently redirected to the ICH homepage — caught and corrected).
- Live URL returns HTTP 200 to curl but the body is a TSPD/JS anti-bot challenge; real-browser render shows the full element page. Anchor quote "Inscribed in 2018 (13.COM) on the Representative List of the Intangible Cultural Heritage of Humanity" verified in the rendered DOM. This matches corpus precedent S186 (ich.unesco.org CAPTCHA documented as an access note).
- Wayback capture 20260906234122id_ fetched (served as raw gzip; decompressed) — quote and three-aspects description both present verbatim.

## Uniqueness
Both live URLs grepped against `corpus/SOURCES.md`, all of `corpus/`, `.ufo/`, and `reports/` — zero hits outside my own row files. UNESCO hosts exist in the base registry (S062, S063, S069, S157, …) but for different element pages; the HOSTS leg counts distinct hosts, and ich.unesco.org adds one host shared with old rows — host diversity is a fleet-level check, not a per-row violation.

## Environment notes
- Internet Archive had a live "Temporarily Offline" outage mid-check (~2026-10-24): archive.org/wayback/available kept answering, web.archive.org refused connections and served the outage page briefly, then recovered; all needed captures were confirmed.
- Tooling: no installs or upgrades performed; curl, Python 3, and the omp browser device sufficed.

## Residual risks for L1
- S783 anchor quote contains inner ASCII double quotes ("Hungary water") — verbatim from source; if the row parser's quote field is delimiter-sensitive, the L1 may prefer the alternate verbatim span "believed to have been produced around 1370 and derived its base from this herb" (also on the page).
- Hunt capture is from 2020 (freshest available); a fresher capture may be created by the fleet later if desired.
- S784 tier A chosen on official-body authority; if the fleet's tier rubric maps UNESCO element summary pages to B (as S157/S163/S186 did), L1 may flip to B — still within the A/B requirement.
