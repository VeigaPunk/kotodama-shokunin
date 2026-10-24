# ScoutRow03 — rows S809 + S810 (claim C, medicine/healing register)

Delivered two registry row drafts + rejects at `.ufo/waves/round-67/rows/ScoutRow03/`.

## S809 — Medieval European monastic infirmaries and herbals
- **Source**: Winston Black, "Medicine and Miracle in a Medieval Monastery," Circulating Now (US National Library of Medicine historical-collections blog), 2023-01-05. `docs`, tier **B** (official-body blog, guest scholarly post — secondary voice, so B not A).
- Live `https://circulatingnow.nlm.nih.gov/2023/01/05/medicine-and-miracle-in-a-medieval-monastery/` — HTTP 200 (216,990 b) with browser UA; **default curl UA answers 403** (UA filter, recorded in VERIFY/ACCESS; an ordinary browser request reaches it, criterion 10 satisfied — not a captcha/credential bypass).
- Capture `20260801154508` id_ — same page (no query), quote verbatim in capture body (grep-verified).
- Anchor quote (22 words): "infirmary could range from a single room just for the monks to a complex of medical buildings including a hospital, pharmacy, baths" — body text, both live page and capture.
- Covers both halves: infirmary scale (quote) + the Bury St Edmunds manuscript's 185 folios of diagnosis and herbal remedies (teaches).

## S810 — Roman military medicine and the valetudinarium
- **Source**: Museum Aargau, Vindonissa Legionary Trail, "Military hospital (Valetudinarium)" — official canton museum site page for the excavated Roman legionary-camp hospital at Vindonissa. `docs`, tier **A** (holding museum's own site interpretation).
- Live `https://www.museumaargau.ch/en/legionary-trail/roman-sites/military-hospital-valetudinarium` — HTTP 200 (64,673 b), plain request, no redirects, no challenge.
- Capture `20260316002018` id_ — same page, quote verbatim in capture body (grep-verified).
- Anchor quote (18 words): "At the camp hospital (valetudinarium), military doctors and medical orderlies treated battle injuries, everyday illnesses and work accidents." — names the term, staff, caseload.

## Compliance math (replicated against reports/round-67/accept-c.py logic)
- Both rows: 11 cells; kind `docs` (in KINDS); tier A/B; status `mined`; opened `2026-10-24`; used-by `corpus/knowledge/culture-material/medicine-healing-codes.md`; recheck `180d` matching this round's row convention.
- Bullets: in-order quote content words S809=5, S810=8 (need ≥3); teaches in-order coverage of quote S809=0.08, S810=0.14 (need <0.8); novel content words present both; longest verbatim quote↔bullet run = 3 words (<12); teaches ≤240 chars; scope ≤60 chars.
- LINK uniqueness: `grep -rn` of corpus/SOURCES.md + all `.ufo/waves/round-67/` fragments — neither live URL nor host paths appear anywhere (hosts circulatingnow.nlm.nih.gov, museumaargau.ch both add distinct normalized hosts for the HOSTS leg ≥10).

## Rejects (filed, with flips)

english-heritage.org.uk housesteads/rievaulx (403 challenge), stgallplan.org (redirects to metadata-only landing — criterion 18), sourcebooks.fordham.edu St Gall (HTTP 500), vindolanda.com + vindolanda.csad.ox.ac.uk (unreachable), metmuseum.org essay (429 Vercel checkpoint — same class as S400), britishmuseum.org collection term (403).
## Design-conflict note (observed, resolved by L1)
CriticFrontier broadcast that Ca-D4 (>=6 today-dated rejected rows) and C-APPEND (additions bounded to S805-S828+S801-S804) were jointly unsatisfiable on a single commit. Verified true on the counter bytes: `accept-ca.py:235` needs `rej_opened_today >= 6` while `accept-c.py:357-358` bounds `allowed_new`. L1 resolved via per-claim lands sequencing: C's receipt runs at A_c (only S805-S828 appended), Ca's at later A_ca (S829+ rejects present). My rows unaffected; noted for the wave record.

## Notes for L1
- No tool installs needed; curl + python3 + NCBI eutils sufficed.
- S809's teaches cell deliberately covers the herbals half since the anchor quote covers infirmary scale; the entry bullet should lead with infirmaries per topic phrasing.
- If a blind reviewer wants a stronger primary source for S810, the peer-reviewed alternatives found (Novae excavation literature; Scarborough 1970 via PMC) were slower to confirm inside the time-box — Vindonissa is the cleaner museum-source pick per the seat's "museum source" mandate.
