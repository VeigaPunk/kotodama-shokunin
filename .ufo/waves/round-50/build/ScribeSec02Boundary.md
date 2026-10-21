# ScribeSec02Boundary — Round 50, Claim C, section §2 (one-owner boundary)

Scope: draft §2 of `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (not landed; entry is C's executor output). Lane HEAD base `4ad26836552462d28a946ca3b067cab0b5ce3532`. Read-only; no product file edited; no installs.

## Section text (draft, ready to paste)

```markdown
## 2. One-owner boundary

A herded animal is never a hunted one: the wild-source test (`hunting-foraging-subsistence.md:36`) excludes herding, so this entry owns the animal as a **standing herd** and cites each neighbour for everything else.

| Neighbour (anchor) | What it owns | This entry's boundary |
|---|---|---|
| `agrarian-field-system-lexicon.md:62` agropastoral row; `:56` communal herding after harvest | parcel, plough, manure-for-stubble contract, fold and stubble rights | herd calendar, transhumance *movement logic*, herd composition; parcel and manure contract stay in agrarian |
| `hunting-foraging-subsistence.md:36,:38` | wild source; located-not-produced; processing up to the haul | the herded counterpart only; wild game and gathering stay there |
| `cuisine-food-lexicon.md:67,:81,:86` | yogurt lineages; milk+meat law (kashrut); the cattle-as-milk economy (Harris, contested) | milking, churning, curd and dried milk to the product; the dairy dish and the milk+meat law stay in cuisine (no dairy-dish owner exists: flag, do not invent) |
| `transport-mobility-lexicon.md:58,:70,:95` | route class; vehicle; load and daily-distance figures; draft capacity chain (camelid, horse) | the herd's seasonal move and the husbandry of riding and pack animals (feed, training, herd size); route, load figure and rider privilege stay in transport |
| `trade-economy-lexicon.md:69,:103,:145` | cattle-root money words (*pecus* → *pecuniary*); caravan lingua franca; caravan-share instrument | herd-as-wealth composition and herd-transfer rules; money words and risk instruments stay in trade |
| `textile-technology.md:22,:27,:101` | fibre-to-cloth chain (shear → spin → dye); worsted/woolen fork; steppe wool contrast drill | flock management, shearing season, fleece selection in breeding (cite `:27` for fleece chronology); cloth stays in textile |
| `linguistics/semantic-fields-lexicon-building.md:70,:105` | pastoral wealth vocabulary field; steppe pastoral field-bundle | the herd facts the field lexicalizes (age, colour, condition, count) |
| `civilizations/mongol.md:40,:131`; `turkic-steppe.md:98,:148`; `scythian-saka.md:70,:173`; `finnic-sami.md:140,:150`; `inca.md:128`; `dine-navajo.md:125` | regional pastoral cases and their textile and monument chains | general method only; each regional herd is cited from its owner, never restated |

- **Calibration (QUALITY criterion 2):** "nomadic pastoralism" as a single type is contested. Pastoralism is not isolation (`turkic-steppe.md:148`) and not the universal condition of any people (`finnic-sami.md:150`).
- **Calibration (QUALITY criterion 6):** the secondary-products horizon (Sherratt 1981, `agrarian-field-system-lexicon.md:80`) is contested as a single horizon `(to-verify)`; the Harris cattle-economy claim is contested (`cuisine-food-lexicon.md:86`).
```

## Sources

No external source was opened in this session for §2. Every claim above is an in-corpus `path:line` anchor, each re-read in this session at lane HEAD `4ad2683` (neighbour sha256 prefixes: agrarian `23564220`, cuisine `36df983d`, transport `86e5f952`, trade `760a9df6`, textile `62ba304a`, semantic-fields `80b5e2c8`). No `[SRC:]` placeholders are needed. Sherratt 1981 is cited only as an inherited, `(to-verify)` reference from the agrarian entry; if the integrator wants it load-bearing, a source row must be opened first (a peer scout, `SrcSherratt-4`, is the owner of that lead).

## Anchor verification (this session)

- Read `:range` or grep-confirmed each cited line: agrarian `:3,:33,:56,:62,:80`; hunting `:36,:38`; cuisine `:3,:67,:81,:86,:135`; transport `:3,:9,:58,:70,:93,:95`; trade `:3,:69,:103,:131,:145`; textile `:3,:22,:27,:101`; semantic-fields `:68,:70,:105`; mongol `:40,:131`; turkic-steppe `:3,:98,:148`; scythian-saka `:70,:173`; finnic-sami `:140,:150`; inca `:128`; dine-navajo `:125`.
- Not verified and not cited: `warrior-material-culture.md:3,:10` (a `hunting-foraging` anchor, not needed for this table); `transport-mobility-lexicon.md:74` (skin-on-frame is a watercraft row, not a pack-animal row).

## Gaps and risks for integration

- Cuisine has no dairy-dish owner: the table flags this rather than assigning dairy dishes to pastoral. Integration must not let §2 claim a dairy-dish register.
- Transhumance overlaps agrarian `:62` (routes) and transport `:95` (draft/clock): the table splits *movement logic* (pastoral) from *road and load* (transport). Lore-owned routes stay with lore.
- The civilizations row is a citation list, not an owner split. It must stay that way when the integrator writes §2 into the entry.

## Tool and install record

- None. No tools installed or updated. `jj` 0.45.1 is on the host; not used (read-only neighbour reads only).

## Unrun checks

- Line-count budget (12–20 lines for §2) not measured against the final placement; the draft is about 18 lines of body text.
- Sweep (`python3 -B reports/round-28/readme/sweep.py`) and README row not touched by this seat (lands belong to the entry executor and L1).
