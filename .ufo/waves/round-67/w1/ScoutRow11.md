# ScoutRow11 — row-opening report (claim C, medicine/healing register)

## Delivered
- `rows/ScoutRow11/row-S825.txt` — asklepieia & incubation: Gaia Gregis, "Guarigioni di Asclepio a Epidauro / Healings by Asclepius in Epidaurus," *Axon* 1(2) 2017 (Edizioni Ca' Foscari, peer-reviewed OA journal) — tier A, paper.
- `rows/ScoutRow11/row-S826.txt` — Japanese moxibustion & acupuncture transmission: Kobayashi, Uefuji & Yasumo, "History and Progress of Japanese Acupuncture," *eCAM* 7(3) 2010, doi 10.1093/ecam/nem155, PMC OA — tier A, paper.
- `rows/ScoutRow11/rejects.txt` — 2 rejects with flip conditions (academia.edu Kernos login wall; J-STAGE Japanese-only body).

## Verified facts
- Live: both URLs curl HTTP 200, single-hop (no redirects), Date headers Sat 24 Oct 2026 12:37:10–11 GMT; no login/paywall/rate-limit. PMC response is gzip — `--compressed` needed.
- Quote-in-body: S825 quote confirmed in the page's English abstract (article body is Italian — noted in VERIFY); S826 quote confirmed in the abstract, string found verbatim.
- Wayback: `20260513075324` (Axon page) and `20261004041226` (PMC) — both `id_` raw captures fetched, HTTP 200, quote grep hits (2 and 3 respectively). URLs query-free → normalization equal.
- Uniqueness: grepped `PMC2887322`, `guarigioni-di-asclepio`, `Kobayashi`, `Gregis`, `edizionicafoscari` across `corpus/` and `.ufo/waves/` — zero hits; neither URL nor source is in `SOURCES.md` (which currently tops out at S800; S801–S824 slots reserved by peers).
- Format: matched prior-wave `row-*.txt` template (round-65 ScoutRow02 exemplar); scope ≤60 chars, teaches ≤240 chars, quote 8–25 words.


## Post-report note (L1 ruling supersedes)
I confirmed to CriticFrontier that the C-APPEND bound and Ca-D4 ≥2-new-rejects requirement were jointly unsatisfiable at a single lands commit (24+4+2=30 appended ids > 28 allowed). L1 ruled: no counter/claims revision — per-claim lands separation (A_r → A_c → A_ca) makes the joint predicate satisfiable as sequenced. The arithmetic finding stands; "unsatisfiable" does not. My rows are unaffected either way.

## Inference / caveats
- S825 quote is from the abstract, which is the only English body text on the page (main article in Italian). If the reviewer wants an Italian-body quote instead, the same line structure holds — flag for L1.
- Both tiered A (peer-reviewed journals). If the wave prefers a museum source for the asklepieia row, the fallback is the Epidaurus Archaeological Museum page (`archaeologicalmuseums.gr`) — not used since paper > museum under the A/B preference and the topic demanded scholarly treatment of incubation.
- Rejects chosen for logged evidence of source curation; neither rejected URL overlaps registry.

## Tooling
No installs needed (curl, grep, python3 already present). No pacman transactions (host-wide pause honored).

Report: .ufo/waves/round-67/w1/ScoutRow11.md
