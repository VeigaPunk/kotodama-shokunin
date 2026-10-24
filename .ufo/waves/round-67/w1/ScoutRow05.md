# ScoutRow05 — round-67 w1 — row openings S813, S814 (claim C, medicine-healing register)

## Delivered
- `.ufo/waves/round-67/rows/ScoutRow05/row-S813.txt` — Ruisinger, "Die Pestarztmaske im Deutschen Medizinhistorischen Museum Ingolstadt" (NTM 28, 2020, DOI 10.1007/s00048-020-00255-7), PMC full text. Peer-reviewed paper authored by the Ingolstadt museum's curator; covers the beaked costume's protective-clothing logic and the authenticity/practicability of the two surviving museum specimens (Ingolstadt, Berlin). kind=paper, tier A.
- `.ufo/waves/round-67/rows/ScoutRow05/row-S814.txt` — Elisabeth Berry Drago, "Paracelsus, the Alchemist Who Wed Medicine to Magic," Distillations, Science History Institute (2020-03-03); a museum-institute scholarly article on Moran's *Paracelsus: An Alchemical Life* covering chemical cures vs Galenic humoralism — iatrochemistry. kind=docs, tier A.
- `.ufo/waves/round-67/rows/ScoutRow05/rejects.txt` — 6 rejects with flip conditions.

## Verification performed (all curl, 2026-10-24)
- S813 live: `https://pmc.ncbi.nlm.nih.gov/articles/PMC8156585/` → HTTP 200, 139,363 bytes, no redirect; anchor quote verified verbatim in the English abstract text.
- S813 capture: `https://web.archive.org/web/20260728172941id_/...` → 200 via plain HTTP fallback (HTTPS replay timed out twice from this host — flagged in row file); quote verified in captured body.
- S814 live: `https://www.sciencehistory.org/stories/magazine/paracelsus-the-alchemist-who-wed-medicine-to-magic/` → HTTP 200, 188,150 bytes, no redirect; quote verbatim in static HTML.
- S814 capture: `https://web.archive.org/web/20261011051916id_/...` → 200; quote verified in captured body.
- Uniqueness: grep of `PMC8156585`, `sciencehistory.org/...paracelsus-the-alchemist`, `32451562` against `corpus/SOURCES.md`, `corpus/`, `.ufo/` → no live-URL collisions (a different sciencehistory.org URL exists in a verification doc — URL unique, host distinctness not required).
- Row shape checked against `accept-c.py`: 11 cells, kind in KINDS enum, tier A|B, status=mined, opened=2026-10-24, used-by=`corpus/knowledge/culture-material/medicine-healing-codes.md`, CAPTURE `id_`-form capture present.
- Bullets: >=3 in-order content words from quote under the counter's `content_words` definition (len>=4, alpha, non-stopword), novel content word(s) present, <80% teaches-cell overlap, no >12-word run copied.

## Notes / caveats
- S813 anchor quote comes from the article's English abstract (14 content words); body is bilingual German/English — the English abstract is served in the same page, and the "role of the beak-like part of the mask" clause names the prophylaxis function, though aromatic-filler specifics live in the German body.
- `.ufo/waves/round-67/rows/` was empty when this seat ran; no sibling-row URL collisions possible at write time — L1 should re-run the LINK/host uniqueness check at integration.
- Rejected-but-close candidates (flip conditions in rejects.txt): pubmed.ncbi.nlm.nih.gov abstract page 203 bot-wall; wellcomecollection.org works page 405 to curl (its API JSON has the best aromatic-beak quote, fetchable if a row ever cites the catalogue API endpoint); SMG collection 429 rate-limited; IMSS article JS-rendered; PMC7920879 search-citation error; NLM exhibition index page nav-only.

## Tooling
No installs needed; curl + python3 stdlib only.



## Fleet note (post-write, L1-resolved)
CriticFrontier flagged joint unsatisfiability of accept-c.py APPEND (new ids bounded to S805-S828+S801-S804) vs accept-ca.py D4 (needs >=2 additional rejected rows opened 2026-10-24 => new ids outside APPEND's bound). I verified it from source, including the closed loophole: the APPEND mutable-cell carve-out freezes c[8]=opened, so flipping a base row's status to `rejected` can never feed D4's opened-today count — new ids were genuinely forced. **L1 resolution (final):** no counter revision; per-claim lands separation — A_r (S801-S804 dispositions) -> A_c (claim C receipt; only S805-S828 append) -> A_ca (carries S829+ reject rows). My rows are unaffected.

Report: .ufo/waves/round-67/w1/ScoutRow05.md
