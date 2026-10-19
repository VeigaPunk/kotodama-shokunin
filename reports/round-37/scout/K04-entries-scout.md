- Seat: K04 | scout | A | date 2026-10-19 | baseline 57c8409

# New corpus entries: couples and cross-domain scout

## Scope and method

The eleven-entry set is the ten round-35 entries named at `corpus/README.md:14-20` plus `culture-material/timekeeping-instruments.md`, recorded as the round-36 landing at `corpus/README.md:5-10`. This is a read-only couples-resolution and boundary scout; no entry or runner was edited or executed, and no canon or admission verdict is made.

A read-only inline Python audit from the repository root parsed the single `- couples:` line in each listed file, extracted `.md` references using the `MDREF_RE` and brace-expansion method in `reports/round-19/audit/entry-audit.py:31-42`, then tested entry-directory, repository-root and `corpus/knowledge/` bases in the order at `reports/round-19/audit/entry-audit.py:74-96`. The required environment was set (`TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1`).

Command output (stdout; references deduplicated within each entry's couples line):

```text
agrarian-field-system-lexicon.md: couples_lines=1 refs=22 resolved=22 unresolved=0
bathing-and-body-hygiene.md: couples_lines=1 refs=25 resolved=25 unresolved=0
fire-fuel-light.md: couples_lines=1 refs=44 resolved=44 unresolved=0
funerary-material-culture.md: couples_lines=1 refs=48 resolved=48 unresolved=0
furniture-interior-lexicon.md: couples_lines=1 refs=19 resolved=19 unresolved=0
writing-media-surface-economy.md: couples_lines=1 refs=20 resolved=20 unresolved=0
binding-speech-complex.md: couples_lines=1 refs=40 resolved=40 unresolved=0
death-afterlife-eschatology.md: couples_lines=1 refs=25 resolved=25 unresolved=0
eschatology-world-end-systems.md: couples_lines=1 refs=30 resolved=30 unresolved=0
sacred-kingship-mythic-charter.md: couples_lines=1 refs=36 resolved=21 unresolved=15
timekeeping-instruments.md: couples_lines=1 refs=25 resolved=25 unresolved=0
TOTAL entries=11 refs=334 resolved=319 unresolved=15
UNRESOLVED sacred-kingship-mythic-charter.md: architecture-settlement-lexicon.md
UNRESOLVED sacred-kingship-mythic-charter.md: calendar-festival-systems.md
UNRESOLVED sacred-kingship-mythic-charter.md: calibration-registry.md
UNRESOLVED sacred-kingship-mythic-charter.md: consistency-verification-checklist.md
UNRESOLVED sacred-kingship-mythic-charter.md: costume-semiotics.md
UNRESOLVED sacred-kingship-mythic-charter.md: historical-linguistics.md
UNRESOLVED sacred-kingship-mythic-charter.md: kinship-terminology.md
UNRESOLVED sacred-kingship-mythic-charter.md: naming-systems.md
UNRESOLVED sacred-kingship-mythic-charter.md: orality-formulaic-language.md
UNRESOLVED sacred-kingship-mythic-charter.md: register-strata-attestation.md
UNRESOLVED sacred-kingship-mythic-charter.md: ritual-garments.md
UNRESOLVED sacred-kingship-mythic-charter.md: semantics-pragmatics.md
UNRESOLVED sacred-kingship-mythic-charter.md: sociolinguistics-registers.md
UNRESOLVED sacred-kingship-mythic-charter.md: sumptuary-law-rank-display.md
UNRESOLVED sacred-kingship-mythic-charter.md: trade-economy-lexicon.md
```

These 15 are basename-only cross-partition references grouped under domain labels in `sacred-kingship-mythic-charter.md:37`; the documented resolver does not infer a partition from those labels. This is a resolution finding, not evidence that the referenced files or intended relationship do not exist. The other ten entries' extracted targets all resolved under the same bases.

## Per-entry surface verdicts

- **Agrarian field system — bounded.** The entry assigns food-as-meal, bulk containers, fiber processing and haulage to their respective owners while retaining the field, water, harvest and tenure system; the couples line names these interfaces (`agrarian-field-system-lexicon.md:8,32-34`).
- **Bathing and hygiene — boundary clear; fire/fuel cross-link owed.** It distinguishes everyday material bathing from ritual meaning and separately requires purity and hygiene not be merged (`bathing-and-body-hygiene.md:7,14,50-53`). Hot baths explicitly consume fuel (`:31,57-60`), but the couples line at `:7` does not name `fire-fuel-light.md`, which owns fuel and light (`fire-fuel-light.md:17,25-27`).
- **Fire, fuel and light — boundary clear; timekeeping cross-link owed.** It reserves ritual meaning, cookware/kilns, building heat, forge products and incendiary weapons to their named owners (`fire-fuel-light.md:17,24-26`). It does not name the later timekeeping entry in its couples line (`:17`), although timekeeping treats calibrated candles, lamps and incense as FIRE instruments (`timekeeping-instruments.md:3,7,26`).
- **Funerary material culture — material scope stated; afterlife interface contested/unreconciled.** Its four-machine frame separates disposal, assemblage, monument and word (`funerary-material-culture.md:47-72`), while `death-afterlife-eschatology.md` includes corpse doctrine, burial and offerings among the living's obligations (`:4,99-102`). Neither couples line names the other (`funerary-material-culture.md:39`; `death-afterlife-eschatology.md:12`). Route a boundary reconciliation; do not assign canon ownership here.
- **Furniture and interior — bounded.** The entry separates objects from building/room vocabulary, costume, containers, table etiquette and the measure-to-money chain; it explicitly leaves hearth/fuel and bathing/water to adjacent domains (`furniture-interior-lexicon.md:14,37-39`).
- **Writing media and surface economy — bounded.** It owns material/economic properties of inscription and expressly excludes script typology, counting lexicon, maker's marks, containers-as-documents and printing as an industry (`writing-media-surface-economy.md:29,33,37-39`).
- **Binding speech — boundary stated; royal-register cross-link owed.** It distinguishes the binding effect of an utterance from register law, name systems, omen-reading and rite grammar (`binding-speech-complex.md:37,49-56,79-81`). Sacred kingship also names the royal register, name taboos and oath formula (`sacred-kingship-mythic-charter.md:3,142-154`), but neither entry's couples list explicitly connects the pair (`binding-speech-complex.md:34`; `sacred-kingship-mythic-charter.md:37`). The division appears workable; request an explicit interface, not an ownership ruling.
- **Death and afterlife — boundary stated; two scope collisions remain open.** It distinguishes the fate of persons from world-shape, world-ages, rite grammar, mourning dress/food and grave-goods inference (`death-afterlife-eschatology.md:19-21`). It nevertheless includes corpse/burial obligations (`:99-102`) and end-event grammar for persons (`:4,106-116`), which meet the funerary and world-end subjects below; neither corresponding entry appears in its couples list (`:12`).
- **World-end systems — intended scopes explicit; person-scope overlap with afterlife needs adjudication.** It names person, age, dispensation and world scopes (`eschatology-world-end-systems.md:27-34`) and requires a person-scope verdict apparatus (`:174`). The afterlife entry also owns the end event as it concerns persons (`death-afterlife-eschatology.md:4,108-116`). Their couples lines do not cross-reference (`eschatology-world-end-systems.md:16`; `death-afterlife-eschatology.md:12`). Route this as contested scope, not a defect verdict.
- **Sacred kingship — royal-register subject clear; 15 resolver failures and binding-speech interface owed.** The topic explicitly includes royal speech levels, name taboos and oath formulas (`sacred-kingship-mythic-charter.md:3,142-154`); the grouped couples line cites register-law and language owners but has 15 basename-only references that fail the documented resolver (`:37`; audit output above). Binding speech shares the oath/name-power area (`binding-speech-complex.md:37,53-56,79-81`); add or confirm the cross-reference without absorbing either subject.
- **Timekeeping instruments — bounded; fire/fuel cross-link owed.** It distinguishes the physical instrument from calendar cycles, sky-calendar apparatus, era names and counting bases (`timekeeping-instruments.md:7,14`). Its instrument family includes calibrated candle, lamp and incense measures (`:3,26`), but its couples line names textile consumables rather than `fire-fuel-light.md` (`:7`); the fire entry owns fuel/light and fire apparatus (`fire-fuel-light.md:17,25-27`).

## Owed

- Integrator: route the 15 basename-only references in `sacred-kingship-mythic-charter.md:37` for path normalization or an explicit resolver decision, then rerun the documented path check.
- Integrator: reconcile and explicitly link funerary material culture with death/afterlife doctrine, preserving the distinction between material disposal/assemblage and doctrine/corpse obligations.
- Integrator: adjudicate the person-scope boundary between death/afterlife and world-end systems; both entries claim a person-facing end apparatus, and neither couples to the other.
- Integrator: route explicit coupling follow-up for bathing ↔ fire/fuel/light and timekeeping ↔ fire/fuel/light; the direct fuel and FIRE-instrument interfaces are evidenced above.
- Integrator: add or confirm the binding-speech ↔ sacred-kingship interface for royal oaths/register/name-power, without silently assigning ownership.
- External historical-source verification and canon review were not part of this scout; source-specific `(to-verify)` items remain as filed.

## Citations

- Entry-set basis: `corpus/README.md:5-10,14-20`; mission and output scope: `reports/round-37/targets.json:4-8,13-14`.
- Resolver extraction and path order: `reports/round-19/audit/entry-audit.py:31-42,74-96`; the path-audit command output is transcribed in this fragment above.
- All entry boundary and cross-domain claims cite their current corpus file and line inline in the per-entry verdicts. No `reports/round-*/run-validation.py` was executed.
