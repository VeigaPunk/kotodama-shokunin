# ScribeSec12Example — Round 50, claim C: §12 NON-CANON micro-example

Lane: kotodama-shokunin, base 4ad26836552462d28a946ca3b067cab0b5ce3532. Read-only seat; no production file touched.

## Status

- Target `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` does **not exist** at base (checked 2026-10-21). The §12 text below is drafted for insertion after §11 (decision record) and before §13 (calibration bank), matching the model's §12 position (`hunting-foraging-subsistence.md:170`).
- The micro-example applies a decision table. The pastoralism entry's §9 table is not yet written; the rows applied below are the ones the example needs. The integrator must land a §9 table with matching rows, or re-point the table column headers.
- Budget: 15 lines of body text (plus the table). Shape follows `hunting-foraging-subsistence.md:170-172` and the H2 `## 12.` form. No H3.
- Anchor paths are relative to `corpus/knowledge/`, per `verification/calibration-registry.md:29`.

## Section text (draft)

```markdown
## 12. NON-CANON worked micro-example

**NON-CANON.** The people, valley, flocks and numbers below are invented to demonstrate the method; nothing here is a claim about a real people (shape: `hunting-foraging-subsistence.md:170-172`).

The **Ketrun** keep sheep, goats and a few yaks on a vertical round: valley-floor pens in winter, a western pass in spring, high meadows in summer, the same pass back in autumn. Applied to the §9 decision-table rows:

| If your culture… | the Ketrun answer (invented) | and check |
|---|---|---|
| Keeps stock as its dominant mode, with hay only as a supplement | sheep and goats supply most food and wool; hay is a winter addition | dominant-mode test (§1); the register is pastoral, not cultivation with stock |
| Moves stock up and down one mountain, twice a year | vertical round, about 60 km, valley pen → high meadow → valley pen (invented figure) | B, element-level typology: [SRC: https://unesco.cultura.gov.it/en/projects/transumanza/ \| §1.1 "vertical transhumance, typically in mountain regions"] |
| Runs more than one species | sheep, goats, yaks (yaks only above the tree line) | A for Turgen/Rinchinlkumbe 1999–2000 data only; B for any wider claim: [SRC: https://www.fao.org/4/y4856e/y4856e08.htm \| Ch. III, Summary ¶2 "Multispecies herding using hardy local landraces is the basis of the system."] |
| Stores a surplus | cheese in cave lofts; hay cut at the valley edge | storage is the hinge of rank: the pen-owning lineage holds the lofts (`hunting-foraging-subsistence.md:117`) |
| Is "behind" the valley farmers on a ladder | the Ketrun are a different economy, not an earlier stage | R, stage ladders discredited (`verification/calibration-registry.md:142`) |
| Gives its herding labour a gender rule | women milk and make cheese at camp; men take the flock over the pass: a deliberate choice | T `(to-verify)`: no pastoral gender source opened this round; stated as design, not evidence (`hunting-foraging-subsistence.md:119`) |
```

## Source list (opened this session, 2026-10-21)

1. **UNESCO element record, Italian ministry mirror.** URL: https://unesco.cultura.gov.it/en/projects/transumanza/ — access 2026-10-21. Located: §1.1 "Description of the element". Quote (22 words): "Two broad types of transhumance can be distinguished: horizontal transhumance, in plain or plateau regions; and vertical transhumance, typically in mountain regions." Scope: the inscribed Mediterranean/Alps element (Inscribed 2019, 14.COM); a typology from the nomination summary, not an ethnographic study. Suggested tier: **B** (official description of a work/element; QUALITY criterion 6). Recheck: when the canonical record changes. Note: the canonical page `ich.unesco.org/en/RL/…-01964` returned a bot-challenge page instead of content on 2026-10-21 and was **not** used; the mirror was read instead. Recheck the canonical page before any Representative List claim.
2. **FAO, *Transhumant grazing systems in temperate Asia*, Chapter III (Mongolia case study 1).** URL: https://www.fao.org/4/y4856e/y4856e08.htm — access 2026-10-21. Located: Chapter III, "## Summary", paragraph 2. Quote (12 words): "Multispecies herding using hardy local landraces is the basis of the system." Scope: Uvs and Khuvsgul aimags, Mongolia, 1999–2000 field data only. Suggested tier: **A** for that case-study scope (primary report of the field data); **B** for the book-level meta-description (publisher blurb, `meta-description` on the same page); **no** tier-A reading for any wider "pastoralism" claim. Recheck: the field years are fixed; recheck the 2000 snow and drought context before comparing across years.

Not opened or not used: Wikipedia "Transhumance" and LibreTexts "Pastoralism" appeared as search snippets only; Khazanov *Nomads and the Outside World* appeared as catalogue/search records only. None is cited.

## Anchor verification (path relative to `corpus/knowledge/`)

| Anchor | Re-read this session | Result |
|---|---|---|
| `culture-material/hunting-foraging-subsistence.md:170-172` | §12 header and NON-CANON line | exists |
| `culture-material/hunting-foraging-subsistence.md:117` | "Storage as the hinge of rank" bullet | exists |
| `culture-material/hunting-foraging-subsistence.md:119` | §7 header, gendered division of labour | exists |
| `culture-material/hunting-foraging-subsistence.md:137-146` | §9 decision table (model shape) | exists |
| `verification/calibration-registry.md:29` | "Paths below are relative to `corpus/knowledge/`" | exists |
| `verification/calibration-registry.md:35-39` | R/C/B/H/T code table | exists |
| `verification/calibration-registry.md:142` | "Stone–Bronze–Iron … subsistence predicts a total social stage — R" | exists |
| `corpus/QUALITY.md:9-12` criterion 2 calibration; `:16-17` criterion 4 usability; `:29` criterion 6 source authority | re-read | exist |

## Unrun checks and blockers

- No sweep, build, or SOURCES.md edit was run; this seat is a leaf and writes only this report.
- The `[SRC: … | …]` placeholders must be converted by the integrator to S-ids (S048 upward). Each new row needs the URL, access date 2026-10-21, the quote above, and the tier stated here.
- The pastoralism file, its §9 table, and `corpus/README.md` row are the integrator's to land; `sweep.py` expectations (225 → 226) are unaffected by this section alone.

## Tooling

No installs. No pacman transactions. Web reads were via the `read` tool only.
