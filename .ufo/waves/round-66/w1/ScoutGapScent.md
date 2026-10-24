# ScoutGapScent — r66 w1 report

Seat: verify claim-C gap at base; draft build order. Lane HEAD == base `94209e8f80969dbac48d56c5d0e2e623635b8616` (jj-colocated). Deliverable: `.ufo/waves/round-66/rows/ScoutGapScent/gap.md` (written; full commands+outputs inline there).

## Findings

- **Gap confirmed, total.** Filename census at base prints **0** — no entry owns scent/perfume/aromatics/incense/fragrance/cosmetic/unguent by name in any of the six partitions (239 corpus files, 32 culture-material).
- **Topic-line sweep: 4 true partial owners, 3 false positives.** The briefed naive grep hits 7 files; `vietnam.md`, `kinship-terminology.md`, `sacred-kingship-mythic-charter.md` match only because "scent" is a substring of "**descent**" — word-boundary re-scan clears all three. Real partial owners: `adornment-body-codes.md` (cosmetics as body-code, 21 tokens), `timekeeping-instruments.md` (incense as FIRE clock fuel), `vessel-container-lexicon.md` (cosmetic/perfume *containers*), `craft-artisan-lexicon.md` (nioi sensory metaphor). None claims the register.
- **Body-text census:** 63 of 239 entries carry ≥1 real token (celts 15, fire-fuel-light 8, carthage 8, islamic-caliphate 7, funerary 6 …) — all incidental/adjacent, no owner.
- **Sibling lanes: zero ownership.** Every lore-shokunin/chousa-shokunin match (5 + 2 files) is the same 'descent' substring artifact — no true scent/incense/perfume/aromatic token in either lane. Lore handoff is unclaimed.
- **Registry ready:** `corpus/SOURCES.md` = 701 `| S` rows, max **S775**; S776 is the declared games re-point; S777–S800 are free — exactly the claim's 24-row allocation. 11-cell row format confirmed from tail rows.
- **Consistency check:** claim's stated counts (239→240 corpus, 32→33 culture-material, 701→725 registry, ids S777–S800) all match observed base state.

## Inference (labeled)

- The naive topic-line command in the claim text over-counts via the descent substring; the claim's *conclusion* ("only partial-scope mentions") still holds after disambiguation — actually strengthens it (4 partial owners, not 7).
- `fire-fuel-light.md` and `bathing-and-body-hygiene.md` are the strongest adjacency risks for scope bleed (incense-as-fuel, scented bathing) — the entry's `- couples:` block should name them alongside the four partial owners.

## Build order (drafted in gap.md, 5 lines)

Register map (5 classes) → source-grounded bullets by class from S777–S800 → cross-cultural patterns → design protocol + calibration + one-way pointing to partial owners → lore handoff + README index row.

## Remaining unknowns / dependencies

- None blocking. `reports/round-66/accept-c.py` legs read (FILE/SET/ROWS/ONEID/RESTATE/HOSTS/LINK/APPEND/NOHARM/SWEEP/CAPTURE/TOPIC) — build-seat can proceed from gap.md.

No tools installed (none needed).
