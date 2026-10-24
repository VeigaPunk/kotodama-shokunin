# ScoutRow02 — r67 w1 row-opening report (claim C)

Seat: open S807 + S808 for `corpus/knowledge/culture-material/medicine-healing-codes.md`.
Outputs: `.ufo/waves/round-67/rows/ScoutRow02/row-S807.txt`, `row-S808.txt`, `rejects.txt`.

## Row S807 — TCM foundations (tier A, paper)

- Source: Li, Yong Ming 2021, "Persistent median artery may explain the transition from
  11 to 12 meridians in ancient Chinese medicine", *Journal of Anatomy* 238(6):1428–1434,
  doi 10.1111/joa.13376. Live: `https://pmc.ncbi.nlm.nih.gov/articles/PMC8128758/` — peer-reviewed
  original study, tier A.
- Verified live: HTTP 200, 103,601 B, curl+UA, 2026-10-24. Anchor verbatim in body:
  "Twelve major meridians were documented in the classic medical book, Huangdi Neijing
  (written ~2000 years ago)".
- Capture: `web.archive.org/web/20250202022615id_/…` replayed at HTTP 200; quote re-verified
  inside the capture body. URL query-free — normalizes equal to live.
- Teaches: the Neijing's 12-meridian canon postdates the 11-meridian Mawangdui moxibustion
  texts; the added Hand Jue Yin channel tracks the persistent median artery.
- Note: the paper does not itself define *qi* — it covers Neijing + meridians, the
  historical spine of the register; qi-specific sources can come from sibling seats.

## Row S808 — Islamic Golden Age medicine (tier B, paper)

- Source: Colgan, Restrepo et al. 2020, "Reflections on Avicenna's impact on medicine",
  *J Community Hosp Intern Med Perspect* 10(4):250–252, doi 10.1080/20009666.2020.1774371.
  Live: `https://pmc.ncbi.nlm.nih.gov/articles/PMC7427450/` — peer-reviewed review, tier B
  per QUALITY criterion 6 convention (review vs primary study).
- Verified live: HTTP 200, 118,676 B, curl+UA, 2026-10-24. Anchor verbatim in body:
  "Most notable is his 14-volume book, al-Qanun fi al-Tibb or The Canon of Medicine".
- Capture: `web.archive.org/web/20260925002204id_/…` replayed at HTTP 200; quote re-verified
  inside the capture body. URL query-free — normalizes equal to live.
- Teaches: 14-volume al-Qanun completed 1025 in five books bridging Islamic and Greco-Roman
  medicine; ~700 years as the field's textbook; Osler's "most famous medical textbook ever
  written".

## Uniqueness (LINK leg)

- `grep PMC8128758 / PMC7427450 / joa.13376 / 20009666` over `corpus/SOURCES.md` → 0 hits;
  `grep -rl` over `.ufo/waves/` → 0 hits (checked before drafting). Both live URLs distinct
  from every base row.

## Rejects (8, in rejects.txt with flips)

NCCIH TCM + acupuncture pages (live 200 but no qi/meridian/Neijing content); NLM
islamic_medical exhibit (now a JS redirect stub); wellcomecollection.org works search (WAF
405); britannica.com/topic/The-Canon-of-Medicine (live 403, all checked captures are
challenge/nav stubs — no body); iranicaonline.org avicenna-x/qanun (intermittent Cloudflare
403); PMC11659438 Dorsher 2024 (on-topic but uncapturable — 0 CDX captures, 3 save attempts
HTTP 523); pubmed.ncbi.nlm.nih.gov/32850086 (HTTP 203 bot challenge).

## Findings / caveats for the L1

1. **Wayback /save flakiness on PMC**: `web.archive.org/save/` returned HTTP 523 for
   PMC11659438 on all three attempts while succeeding for older PMC pages — if other seats
   hit 523, prefer sources with existing verified captures rather than retrying saves.
2. **Museum/encyclopedia tiers mostly walled this session**: Britannica (403), Europe PMC
   (403 Cloudflare), Wellcome (405 WAF), Iranica (intermittent 403). PMC full-text pages
   were the only curl-clean scholarly reads.
3. **Design conflict forwarded**: CriticFrontier's C-APPEND vs Ca-D4 id-bound alert reached
   me mid-flight; L1 resolved it via per-claim lands commits (A_c for C, A_ca for Ca) —
   no action needed from row seats; both my ids stay inside S805–S828.
4. No tool installs needed; curl + python3 stdlib sufficed. Nothing installed this round.
