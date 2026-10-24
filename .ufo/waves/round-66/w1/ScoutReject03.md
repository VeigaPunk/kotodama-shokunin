# ScoutReject03 — REJECT-CANDIDATE verdict: ADMIT S803

## Decision
ADMITTED. Candidate topic "scent in medieval Christian liturgy" → row `S803` drafted at `.ufo/waves/round-66/rows/ScoutReject03/row-S803.txt`.

## Source admitted
Brazinski, Paul and Fryxell, Allegra R. P. — “The Smell of Relics: Authenticating Saintly Bones and the Role of Scent in the Sensory Experience of Medieval Christian Veneration,” *Papers from the Institute of Archaeology* (UCL) 23(1) art. 11 (2013), DOI 10.5334/pia.430.
- Live URL: https://student-journals.ucl.ac.uk/pia/article/id/489/ → HTTP 200, abstract page; PDF galley `/article/489/galley/656/view/` → 200, `application/pdf`, 3,455,729 bytes, 15 pp.
- Wayback capture: `20261016181022` (freshest) replays 200; `id_` replay serves gzip-compressed bytes (decompress to verify); quote text verified inside decompressed page.
- Topic fit: source covers smell inside medieval Christian worship — relic veneration, translatio, perfumed oils/ampullae, liturgy-adjacent devotional practice in Western Europe and Byzantium. Strictly "liturgy" is adjacent rather than central (paper is relic-cult focused), but it is in-scope for the scent register's Christian-ritual wing. Tier B (peer-reviewed university journal, single paper, claim-scoped).
- Anchor quote (17 words, verbatim, appears in abstract and PDF body): “smell was used in the medieval world as a means to challenge or confirm a relic’s authenticity”
- Uniqueness: URL absent from `corpus/SOURCES.md` registry and all lessons except round-65 rows on the same host (S773 is `/article/id/1286/` — different article, no collision).

## Rejected alternatives (checked this session)
- `https://onlinelibrary.wiley.com/doi/full/10.1111/emed.12394` (Charles West, *Early Medieval Europe* — incense in Carolingian medicine/liturgy) — HTTP 403 bot-wall, body unreachable via curl; flip: open-access deposit.
- `https://books.openedition.org/pur/45742?lang=en` (Caseau, “Encens et sacralisation de l’espace dans le christianisme byzantin”) — 200 but Anubis JS bot-challenge; body unreachable; flip: plain-text mirror.
- `https://shs.hal.science/halshs-03862055v1/document` (Caseau, olfactory landscape chapter, PDF) — Anubis challenge page, not the PDF; flip: ungated HAL file.
- Susan Ashbrook Harvey, *Scenting Salvation* (UC Press 2006) — Fulcrum/JSTOR/OUP all access-gated; only reviews open (BMCR review is tier-B at best for a book-description claim).

## Row-format conformance checked
11 registry cells (id, source+live+`id_` capture, kind=paper, tier B, scope 56 chars, 17-word quote, teaches 224 chars, mined, 2026-10-24, 180d, used-by = scent entry). BULLET: 11 content words, ≥3 in-order from quote ("authenticity" + scent/veneration field), no run >12 from quote, novel words (certify, expose, olfactorily), token coverage vs teaches <80%.

## Dependencies/notes for the integrator
- The used-by entry `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` does not yet exist at lane tip — normal at draft stage; L1 owns integration.
- If the entry's bullets require literal "liturgy" (Mass rite) rather than cult/devotion scope, prefer re-scoping to relic/worship practice, which this source supports directly.
- No tools installed; only system `pdftotext` (poppler, already present) used for PDF verification.

Report: .ufo/waves/round-66/w1/ScoutReject03.md
