# ScribeRowCelestialSymbolismCale — Claim D candidate row

Round 51 attempt 3, hyaku phase 3, 2026-10-22. Seat: leaf scribe (no subagent dispatch). Skill read: `skill://godspeed`. Tooling: `/home/vgpnk/.omp/agent/RULES.md` read; no installs performed (none needed). Report path: lane-relative `.ufo/waves/round-51/build/ScribeRowCelestialSymbolismCale.md`.

## Assigned item
Claim D (depth, repair-first) candidate row for the pastoralism entry `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` §2 one-owner boundary table. Neighbour candidate: `corpus/knowledge/myth-symbol/celestial-symbolism-calendars.md`. Expected seam: sky figures by subsistence (its §1 names pastoralists' milky or river figures) versus the herding calendar.

## Baseline (measured, lane worktree, base `bff83ba` bytes)
- `python3 -B reports/round-51/boundary-count.py` → `rows=11 resolved=11 distinct=11` (exit 0). Matches claims.json "before".
- Pastoralism entry line count: 204 (≤ 250; +1 row keeps 205).
- `celestial-symbolism-calendars.md` basename is unique under `corpus/knowledge/` (glob: single hit, myth-symbol/).

## Verdict: ADD

Distinct neighbour (not among the 11 existing §2 rows; not a directory row, not a split of an existing row). Real seam: the celestial entry owns the sky-figure typology *assigned by subsistence*, including the milky/river figures it names for pastoralists; the pastoralism entry owns only the herd-side subsistence input to that reading. Not filler: the boundary is already developed in the pastoralism body (§10 line 148 cites the same anchor with the same boundary).

### (a) Exact table row (ready to paste into §2)
```
| `celestial-symbolism-calendars.md:28` | the milky/river sky-figure typology assigned by subsistence (§1, §6) and the calendar machinery | the herd's pasture/milk track as the subsistence input that picks a milky/river reading; not a second sky-lore or calendar owner |
```

Anchored line quoted verbatim (`celestial-symbolism-calendars.md:28`):
> "Three constraints do most of the design work for you: (1) **latitude** — which stars are circumpolar, whether there is a usable pole star (bright in the north: Polaris; none bright in the south), which zodiac signs ride highest; (2) **subsistence** — farmers anchor on heliacal risings, sailors on star paths, pastoralists on milky/river figures; (3) **economy of omens** — rare events (eclipses, comets, conjunctions) are only useful to institutions that can afford specialists to watch for them."

The line supports the ownership cell: it assigns milky/river figures to pastoral subsistence (the celestial entry's own t; corroborated by §6 "Milk/path" row, line 112: "pastoral etiology; the body of a humiliated goddess", and line 118: "Assign by subsistence … milk → dairy purity rules"). Anchor resolves: file unique, line 28 within 175.

Counter outcome after adding: `rows=12 resolved=12 distinct=12` (expected; the row's first cell carries exactly the one resolving anchor). Three further candidates still needed for 15.

### (b) Where the body already develops this boundary
Already developed: `pastoralism-animal-husbandry.md` §10 (ritual, myth and symbol), line 148 — "Sky figures" row:
> `| Sky figures | pastoralists read milky/river figures (celestial-symbolism-calendars.md:28) | a subsistence input to sky lore, not a creed |`

No sentence needed; the L1 may reuse this boundary phrasing in the §2 cell. (Alternate explicit narrowing if preferred: keep §2 boundary as "the herd's pasture/milk track only"; no new external source, no S-id, no sign-language mention.)

### (c) Falsifier
If a non-author re-read of `celestial-symbolism-calendars.md:28` finds the line does not assign milky/river figures to pastoralists, or that the pastoralism §2 cell's "what it owns" claims ownership the anchored line does not support, the row fails. Also falsified if a reviewer finds the row duplicates an existing row's neighbour or would push the entry past 250 lines.

## Compliance
- Row cites no claim-C entry path and no S-id (S071 upward); no sign-language mention. Domain: conlang/worldbuilding method, not canon (both files are reference-method entries; no canon ruling touched).
- One-way citation only; celestial entry is not modified.
- No git/jj writes; no reads from held prior-attempt material.

## Evidence
- `reports/round-51/claims.json` (claim D statement, lands, counter, falsifier).
- `corpus/knowledge/myth-symbol/celestial-symbolism-calendars.md:28,:112,:118` (raw re-read).
- `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:148` (raw re-read), `:29` section header, entry total 204 lines.
- Counter run output above.

## Unrun checks
- Full claim-D counter post-edit (requires L1 integration; my seat does not edit the entry).
- Three remaining candidate rows (out of scope for this seat).
