# ScoutRow06 — round-67 claim C row-opening (S815, S816)

## Deliverables
- `.ufo/waves/round-67/rows/ScoutRow06/row-S815.txt` — opened
- `.ufo/waves/round-67/rows/ScoutRow06/row-S816.txt` — opened
- `.ufo/waves/round-67/rows/ScoutRow06/rejects.txt` — 4 rejects with flips

## S815 — Aztec/Mesoamerican herbal medicine
- Source: Tufts University Tisch Library Special Collections, "The Badianus Manuscript" (docs, tier B).
- Live `https://tischlibrary.tufts.edu/special-collections-badianus-manuscript` → HTTP 200 (curl, 2026-10-24), no challenge/paywall; body describes the 1552 Cruz-Badiano herbal, earliest Nahua medicine book, 185 plant illustrations, composed in Nahuatl by Martín de la Cruz, Latin translation by Juan Badiano.
- Anchor quote (14 words): "It is the earliest known work on Mexican medicinal practices and treatment of diseases" — verbatim in body and meta description; confirmed present in the wayback capture `20261011022805` (gzip body decompressed and grepped).
- Capture normalized-equal to live (no query). Host `tischlibrary.tufts.edu` absent from corpus/SOURCES.md (Perseus is `perseus.tufts.edu`, distinct host).

## S816 — Tibetan medicine / Four Tantras (Gyushi)
- Source: Himalayan Art Resources (Rubin Museum of Art project), "Charts: Blue Beryl Main Page (Medical Paintings)" set outline (docs, tier B).
- Live `https://www.himalayanart.org/search/set.cfm?setID=253` → HTTP 200 (curl, 2026-10-24); page states the Four Tantras is Tibetan medicine's foundational text, discovered as terma by Draba Ngonshe in the 11th century; Blue Beryl commentary and charts commissioned by Desi Sanggye Gyatso late 17th century.
- Anchor quote (18 words): "The Four Tantras was discovered as a 'Revealed Treasure' text (terma) by Draba Ngonshe in the 11th century" — verbatim live and in capture `20260310213249`.
- Capture query-aware-normalizes equal to live (`setID=253` carried in both). Host `himalayanart.org` absent from SOURCES.md.


## Post-report note (L1 broadcast)
C-APPEND vs Ca-D4 id conflict (rejects needing ids outside NEW_IDS∪EXTRA_IDS) resolved by per-claim lands sequencing: C measures at A_c (only S805-S828 appended), Ca at later A_ca carrying S829+ reject rows; S801-S804 land earlier at A_r inside EXTRA_IDS. No counter revision. My rejects.txt entries stay fragment-format and are promotable to rejected registry rows at A_ca if the integrator wants them.
## Constraint checks (accept-c.py reviewed: legs ROWS/LINK/CAPTURE/RESTATE)
- 11 cells, kind=docs, tier B, status mined, opened 2026-10-24, used-by names the entry. ✔
- Live URLs grep-unique against corpus/SOURCES.md (0 hits for both hosts and paths). Two new distinct hosts contribute to the >=10 HOSTS leg.
- Anchor-quote regex reads first `"..."` in cell 5 — quote cell only; source names contain no stray pipes or double-quote spans. ✔
- RESTATE metrics computed locally with the acceptor's own functions: S815 inq=5, teaches_cov=0.14, 8 novel words; S816 inq=5, teaches_cov=0.16, 7 novel words; q_in_teach 0.00/0.50 (<0.8 echo guard). ✔
- Scope ≤60 chars (56/50); teaches ≤240 chars (193/188); quotes 8–25 body words; bullets 6–25 words, no >12-word run copied. ✔

## Rejects (in rejects.txt)
- rubinmuseum.org Project Himalayan Art Hofer essay — 403 bot block; otherwise the strongest Four Tantras museum-scholarly source.
- si.edu exhibition page — 403; live asia-archive.si.edu twin is 200 but description-thin.
- nlm.nih.gov Badianus exhibition URL — 404 (retired/moved).
- exhibits.tcu.edu item 2444 — 200 but describes the 1940 Emmart print edition, not the codex register; out of assigned scope.

## Notes for the L1/entry author
- Tier B chosen for both: institutional descriptive pages (secondary write-ups), not primary artifacts. If a seat wants tier A here, the flip is a primary/digital-facsimile source (e.g., NLM digital collections scan of the codex, INAH record).
- HAR page requires the `setID=253` query; dropping it normalizes to a different page — keep the full URL.
- Metmuseum ToAH pages returned 429 under curl this run — flag for re-openers (rate limiting, not absence).
- No tooling installed; standard curl/python3 sufficed.

Report: .ufo/waves/round-67/w1/ScoutRow06.md
