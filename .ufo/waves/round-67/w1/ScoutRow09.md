# ScoutRow09 — row-opening report (claim C)

## Opened rows

### S821 — Kampo / Japanese traditional medicine
- **Source:** Ito, Watanabe, Fukuzawa et al. 2021, *Development of Kampo (traditional Japanese medicine) e-learning program*, Medical Education Online 26(1):1938504 — peer-reviewed, tier A.
- **Live URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC8676632/ — curl -L HTTP 200, 2026-10-24, 175KB; quote verified verbatim in abstract.
- **Anchor (17 body words):** "traditional medicine (known as Kampo) is regulated by the government and prescribed by over 90% of physicians"
- **Wayback:** `20250214131132` id_ capture, HTTP 200 verified. Fresh /save attempts today all returned Cloudflare 523 — archive.org's fetcher cannot reach ANY ncbi.nlm.nih.gov origin right now (tested pmc + pubmed; unrelated hosts save fine). Retained the existing 2025-02-14 same-page capture per the S800 precedent; flagged in CAPTURE/ACCESS.
- **Uniqueness:** `grep PMC8676632` over corpus/SOURCES.md, README, lessons, .ufo → no hits. Host `pmc.ncbi.nlm.nih.gov` already used by base rows (e.g. PMC2575338) but URL is distinct — HOSTS leg needs ≥10 distinct hosts across all 24 rows, not my concern alone.

### S822 — medieval Islamic hospital (bimaristan)
- **Source:** Sadeq Sajjadi, "BĪMĀRESTĀN", Encyclopaedia Iranica Vol. IV Fasc. 3 pp. 257-261 (1989; updated 2013-04-26) — scholarly encyclopedia, tier A.
- **Live URL:** https://www.iranicaonline.org/articles/bimarestan-hospital/ — HTTP 200 via 301 from /articles/bimarestan, 398KB, Mozilla UA. NOTE: prior rounds logged bare-curl 403 on iranicaonline.org; a browser UA works today (change noted in ACCESS).
- **Anchor (14 body words):** "hospitals were also the principal centers of medical education and granted diplomas to their graduates" — verbatim in body.
- **Wayback:** fresh same-day capture `20261024123927`, id_ fetch HTTP 200, 78KB; captured original equals live URL.
- **Uniqueness:** `grep bimarestan` → no hits anywhere in repo/.ufo.

## Rejects (rows/ScoutRow09/rejects.txt)
1. PMC3114169 — wrong article entirely (Turner-syndrome vascular-ring case report; ID was a search guess).
2. nlm.nih.gov/exhibition/islamic_medical/islamic_07.html — retired redirect stub, no hospital text; flip is the resource.nlm.nih.gov/9439902 record.
3. jsom.or.jp/english/background.html — JSOM bylaws boilerplate, nothing about Kampo itself. (Note: jsom.or.jp/english/ exists but the /en/ slug 404s.)

## Environmental findings (attack surface for critics)
- **NCBI wayback save outage (potential validator landmine):** savepagenow → 523 for every *.ncbi.nlm.nih.gov URL today, and repeated saves briefly rate-limited me to 429. Any sibling whose fresh-capture leg targets NCBI hosts will hit the same wall; the S800-style "earlier verified capture + documented failed re-capture" pattern is the established fallback.
- **iranicaonline.org now curlable** with a Mozilla UA (200/301), contradicting the standing "403 to automated fetch" note repeated in several lessons — the ACCESS line records both observations.
- No tool installs needed; curl + python3 stdlib only.

## Confidence
High on both rows: live fetch, verbatim quote containment, capture fetch, and uniqueness all verified by hand. Residual risk: the S821 capture is 2025-02-14 not same-day (env constraint, documented); CAPTURE leg explicitly permits same-page captures.
