# Scribe row — Claim D candidate: `calendar-festival-systems.md`

**Seat:** KotodamaR51a3.ScribeRowCalendarFestivalSystem · **Assigned item:** one new §2 boundary row for the pastoralism entry, neighbour candidate `culture-material/calendar-festival-systems.md` (seam: festival and calendar reckoning versus the herding year — lambing, moves, shearing).

## Verdict: ADD

Distinct neighbour with a real seam, not filler, not a split of an existing row.

- **Distinct:** no existing §2 row anchors `calendar-festival-systems.md` (the only calendar-adjacent row is `agrarian-field-system-lexicon.md:56,:62`, which owns the *agropastoral* field calendar; `civilizations/` is a directory row). Basename unique: glob over `corpus/knowledge/**` returns exactly one file.
- **Real seam:** the candidate stakes the same ground from the other side. `calendar-festival-systems.md:53` — "Farmers in any case timed work by flood and stars, not by the civil date: the civil and natural calendars are separate institutions." `:79` — French Republican month names "keyed to season and husbandry … ordinary days renamed for plants, animals, farm tools — a rural almanac as civic catechism." `:121` — "1 Elul for cattle tithes … separate legal clocks on separate new years." The pastoralism entry currently owns the herding year *implicitly* (below) with no explicit fence against the civil/festival calendar; this row supplies it.
- **Not a split:** the agrarian row's ownership cell is parcel/plough/manure contract and the agropastoral calendar; this row's is the statutory civil/festival calendar. Different neighbour, different file, different register.

## (a) Exact table row (ready to paste into §2)

```
| `calendar-festival-systems.md:53,:79,:121` | the civil and festival calendar: month/week design, new-year and era statute, festival placement — incl. livestock-dated fiscal dates (the 1 Elul cattle-tithe new year); a year named from husbandry without running the farms | the herding year — lambing, moves, shearing — as the herd's working schedule; the calendar's livestock dates are statutory events, not pastoral timetables |
```

Anchored lines, quoted verbatim (`calendar-festival-systems.md`, line 175 total; all three anchors in range and each supports the ownership cell):

- `:53` — "Farmers in any case timed work by flood and stars, not by the civil date: the civil and natural calendars are separate institutions." → supports "civil and natural calendars are separate institutions; the neighbour owns the civil calendar".
- `:79` — "Decree of 5 October 1793, names by Fabre d'Églantine: 12 months × 3 décades × 10 days; poetic month names keyed to season and husbandry (Vendémiaire vintage, Brumaire mist, Frimaire frost; Nivôse snow, Pluviôse rain, Ventôse wind; Germinal sprouting, Floréal blossom, Prairial meadow; Messidor harvest, Thermidor heat, Fructidor fruit); décade days Primidi–Décadi; ordinary days renamed for plants, animals, farm tools — a rural almanac as civic catechism." → supports "a year named from husbandry without running the farms".
- `:121` — "Four new years at once (Mishnah Rosh Hashanah 1:1): 1 Nisan for kings and festival counts, 1 Elul for cattle tithes, 1 Tishrei for years, sabbatical and jubilee, 15 Shevat for trees — separate legal clocks on separate new years." → supports "livestock-dated fiscal dates (the 1 Elul cattle-tithe new year)".

## (b) Boundary development

The boundary is already developed in the pastoralism body (`pastoralism-animal-husbandry.md`):

- §1, line 16 (Master claim): "It reads rangeland as a moving schedule and holds the herd as living capital" — the herding year as schedule.
- §1 test table, line 21: `| **Mobility tracks forage** | movement is the production logic, timed to vegetation and season (S058) | … |` — moves timed to vegetation/season, not to the civil date.
- §3 typology table, lines 51–54: nomadic "forage cycle"; transhumant "seasonal movement of people with their livestock"; agro-pastoral "herd calendar collides with the ploughing peak" — the moves.
- §6 products table, line 93: `| Wool and hair | living animals, shorn or plucked | flock management lives here; cloth stays in `textile-technology.md:27` |` — shearing.

Optional one sentence the L1 can insert after **line 16** (§1, end of the Master claim paragraph, before the test table), to make the civil-calendar contrast explicit (25 words; no new external sources; no S-ids; no sign languages):

> The herding year — lambing, moves, shearing — is the herd's working schedule; the civil and festival calendar (`calendar-festival-systems.md:53`) places feasts and epochs, never the herd's moves.

## (c) Falsifier

A non-author review finds that `calendar-festival-systems.md:53,:79,:121` does not support the row's ownership cell (e.g., reading `:53`'s farmers-only wording as excluding herders from the "natural calendar" principle), or that the row restates the `agrarian-field-system-lexicon.md:56,:62` calendar row rather than naming a distinct civil/festival neighbour, or that the anchor fails to resolve.

## Constraint checks

- Counter static check: new first cell `calendar-festival-systems.md:53,:79,:121` matches the counter's `FILE_ANCHOR` (basename + line list); basename resolves to exactly one file (glob); lines 53/79/121 within 175. `distinct` target (file path) is new, so rows/resolved/distinct each gain 1 (11 → 12; other scribe rows complete to 15).
- Entry line budget: currently 204 lines; +1 row and +1 optional sentence → 206 ≤ 250.
- D restrictions: row and sentence cite no `sign-languages-manual-modality.md`, no S-id ≥ S071, no `reports/round-51/boundary-count.py`.

## Evidence

- `corpus/knowledge/culture-material/calendar-festival-systems.md:53,:79,:121` (read raw, this session) — quotes above.
- `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:16,:21,:51-54,:93` — body development above; entry is 204 lines.
- `reports/round-51/claims.json` (D statement, falsifier, must-not-cite) and `reports/round-51/boundary-count.py` (row/anchor semantics) — read, not executed.

## Unrun checks

- `python3 -B reports/round-51/boundary-count.py` — for the main agent to run after the L1 lands the row (I did not mutate the entry; current tree still measures 11/11/11).
- No tool installs performed this session (no install was needed).
