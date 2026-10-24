# ScoutReject02 — S802 admit decision (smell and disease theory)

Verdict: ADMIT. Row fragment written to `.ufo/waves/round-66/rows/ScoutReject02/row-S802.txt`.

## Admitted source
- Science Museum (official national museum, tier B docs), 'Preventing infection: lessons from the past' — https://www.sciencemuseum.org.uk/objects-and-stories/preventing-infection-lessons-past
- Live curl 200 (2026-10-24); quote verified verbatim in served HTML body: "Miasma theory led to positive advancements in medicine, although for the wrong reasons."
- Wayback capture 20251115220917 (`id_` raw, pre-existing) re-fetched and the quote re-verified; original URL query-aware-normalizes equal to the live URL (no query params). No fabricated capture.
- URL uniqueness: `grep` for `preventing-infection-lessons-past` and `sciencemuseum.org.uk/objects-and-stories` against `corpus/SOURCES.md` and `.ufo/waves/round-66/rows/*/*.txt` → no matches.
- Fit: article directly binds scent to disease theory — miasma (bad air) explanation plus the 1832 "cholera preventive costume" packing herbs and perfumed tea because strong-smelling items were believed to stop miasmas; hospitals removed bad smells and incidentally cut infections. Adjacent to but distinct from S791 (pomander prophylaxis): theory+sanitation vs. a single object class, different host.

## Alternatives considered (rejected at admission ranking, still viable)
- Science History Institute, "If You Smell Something, Say Something" — https://www.sciencehistory.org/stories/magazine/if-you-smell-something-say-something/ — live 200, rich quotes ("potent protection from miasma", "foul miasmas were understood to spread disease"). Less direct on aromatics-as-treatment; fallback if S802 is dropped. Flip: promote if the Science Museum page becomes unreachable.
- Royal College of Physicians, "Disease in the air: exploring the relationship between health and smell" — https://history.rcp.ac.uk/blog/disease-air-exploring-relationship-between-health-and-smell — curl 403 (bot block). Flip: an ordinary fetch serving the article with a verifiable quote.
- NIH news page — 403; Met Museum Heilbrunn — 429 rate-limited. PMC2862330 was a dead end (1918 influenza photo essay, no miasma content).

## Format checks performed
- 11 cells; kind=docs; tier=B; scope 51 chars; quote 13 words verbatim (8–25 band); teaches 209 chars (<240); BULLET "Miasma theory spurred advancements in medicine, albeit for the wrong reasons." — inq=6 shared quote content-words (≥3), teaches in-order coverage 0.0 (<0.8), novel words {spurred, albeit}; verified by replaying accept-c.py RESTATE math. Source-name uses single quotes so the anchor-quote regex picks the body quote.
- Access: first live fetch 200; a rapid second refetch hit Varnish 405 — re-openers should space requests or use the capture; third fetch after ~12 s cooldown returned 200.

## Dependencies / notes
- `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` does not exist at lane tip (gap confirmed); rows S777–S800 not yet in `corpus/SOURCES.md`. Entry/scribes own bullet placement; my BULLET is a candidate clause.
- No tools installed (pacman paused per ruling; curl/python3 sufficient).

Report: .ufo/waves/round-66/w1/ScoutReject02.md
