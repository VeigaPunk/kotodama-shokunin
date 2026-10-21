# CriticGapPremise2 — round 50 falsify, claim C gap premise and cite-vs-duplicate

Seat: critic (leaf). Item attacked: C's gap premise on the landed bytes. The question has two parts. Does any existing entry already own pastoralism as a production system? Does the new entry duplicate its partial owners instead of citing them?

Bytes read: `git show 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0:<path>` (landed) and `4ad26836552462d28a946ca3b067cab0b5ce3532` (base) only. The lane working tree was not used. No installs. The temp dump `/tmp/cgp2` was removed afterwards. Unless prefixed, paths are under `corpus/knowledge/`, and `PAH` = `culture-material/pastoralism-animal-husbandry.md` at the landed commit.

## Verdict: PARTIAL

- **The gap premise HOLDS.** No entry at base owns pastoralism as a production system. The partial owners named in the assignment own sub-pieces: one typology row, a lexicon field, an idiom, and money words. None owns the system.
- **"Cites rather than duplicates" is PARTIAL.** Agrarian `:62` and semantic-fields `:70`/`:105` are cited at the point of use. Trade-economy `:69` is cited too. But:
  - the entry's own `gap filled` line makes a false claim about where animal-symbolism is cited;
  - three propositions owned by `agrarian-field-system-lexicon.md:80` and `animal-symbolism.md:73,:110` are restated in the body without an inline citation, and one of them is regraded;
  - one boundary anchor is wrong.
- All of these are fixable defects of one-way citation. None is a tradeoff the judge must reject.

## A. Premise: no existing owner (HOLDS)

Commands run (read-only, on commit objects):

| Check | Result |
|---|---|
| `git grep -nP '^- topic:.*\b(?i:pastoral\|herd\|husbandr\|transhuman\|livestock)' 4ad2683 -- corpus/knowledge \| wc -l` | **0** |
| same pattern without `\b`, base | 1 hit: `culture-material/writing-media-surface-economy.md:3` ("sherd"), a non-owner. This matches PAH:4 and lesson R50-M2. |
| same bounded pattern, landed | 1 hit: `PAH:3` only |
| base filenames matching `pastoral\|husband\|herd\|nomad\|livestock\|steppe` | 1: `civilizations/turkic-steppe.md`, a regional polity entry. Its topic is language, inscriptions, titles, dwellings and dress, not husbandry. |
| broad H1/H2/`topic`/`scope`/`gap filled` sweep at base for `pastoral*\|herd*\|husbandr*\|transhuman*\|livestock\|nomad*\|cattle\|flock\|reindeer\|camel*\|sheep\|goat\|yak` | 2 hits. `civilizations/turkic-steppe.md:18` is an H2 anti-stereotype guard ("not a timeless nomad kit"). `culture-material/transport-mobility-lexicon.md:4` is the draught-animal layer of the mobility system. Neither is a production-system owner. |
| base body-hit density (`git grep -ciE 'pastoral\|herd\|transhuman\|livestock\|nomad\|husbandr\|flock\|pasture'`) | Highest non-new file: `turkic-steppe.md` with 8 hits, then `writing-media-surface-economy.md` with 7 (all "sherd"/parchment herd) and `mongol.md` with 5. Every hit is a regional guard or a mention. None is method. |
| sibling lanes: `rg -P '^- topic:.*\b(?i:pastoral\|herd\|husbandr\|transhuman\|livestock\|nomad)'` over the other 20 `*-shokunin` trees | 0 lines. PAH:4's "no sibling lane owns the register" holds. |

I checked each partial-owner anchor in the assignment at the landed bytes:

| Anchor | Content | What it owns | Production-system owner? |
|---|---|---|---|
| `culture-material/agrarian-field-system-lexicon.md:62` | agropastoral row: "fields + pasture + transhumance routes \| ploughing peak plus herd calendar; manure contracts \| … manure-for-stubble exchange" | one row of a *field*-system typology | no |
| `linguistics/semantic-fields-lexicon-building.md:70` | "Pastoral wealth vocabulary (herd-age, herd-color, herd-condition terms) indexes property systems; … (Anthony 2007)" | the lexicon field | no |
| `linguistics/semantic-fields-lexicon-building.md:105` | "steppe pastoral \| subsistence (herd wealth), kin (clan), war (raid), landscape (pasture)" | a field-priority bundle | no |
| `myth-symbol/animal-symbolism.md:73` | Nuer "cattle of money": "cattle as social idiom — names, songs, bridewealth; not primarily food" | the symbolic idiom | no |
| `myth-symbol/animal-symbolism.md:110` | "the Mongol five livestock (horse, cattle, camel, sheep, goat) structure wealth-language … Decide which species is the culture's **idiom of value**" | the value idiom | no |
| `culture-material/trade-economy-lexicon.md:69` | "fee, pecuniary … *pecus* 'cattle' … PIE \*peḳu- 'movable wealth = cattle' (Watkins); cf. Nuer cattle as the idiom of all value" | money-word etymology | no |

None of the six owns mobility regimes, herd demography or offtake, pasture tenure and commons, product chains, transfer institutions, or pastoral–sedentary exchange. Those are PAH §3–§9. The premise as narrowed at `PAH:4` ("no file … owns the pastoral **production system** as a cross-cultural method") is true.

Side finding (calibration, not coverage): the frozen declaration still has the blanket wording that the build-wave critic refuted. `reports/round-50/claims.json` `lowest_axis_reasoning` says "existing mentions are cross-references in agrarian, fire-fuel, semantic-fields, civilizations entries". It also omits animal-symbolism, trade-economy, transport and textile, which `PAH:4` itself lists as partial owners. Lesson R50-M2 records the "sherd" evidence-command defect but not this premise-wording defect. `corpus/lessons/round-50.md` §Mistakes has rows M1–M3 only.

## B. Cite or duplicate (PARTIAL)

### Holds: cited at the point of use

- **agrarian `:62`** is cited at `PAH:21` (test table), `PAH:31` (§2 row, with `:56`), and `PAH:50` (typology agro-pastoral row: "herd calendar collides with the ploughing peak (`agrarian-field-system-lexicon.md:62`)"). It is not restated.
- **semantic-fields `:70`** is cited at `PAH:71` ("A herd vocabulary is a property index … (`semantic-fields-lexicon-building.md:70`)"). §5 then adds sourced lexicon facts (S052, S059, S060) rather than repeating `:70`. **`:105`** is cited at `PAH:37` and `PAH:156`.
- **trade-economy `:69`** is cited at `PAH:35` and `PAH:79`. `PAH:79` adds S065 for \*peku- and cites trade-economy for *pecūnia*, so it supplements instead of re-owning.
- **Regional guards are cited, not restated as new:** `mongol.md:40` (`PAH:43`, `:164`), `turkic-steppe.md:148,:193,:194` (`PAH:131`, `:163`), `scythian-saka.md:70` (`PAH:131`), `finnic-sami.md:140,:150` (`PAH:64`, `:118`, `:165`), `dine-navajo.md:125` (`PAH:118`), `inca.md:128` (`PAH:65`). I re-read every anchor at the landed bytes and each matches its use.
- Other anchors re-read and matching: `hunting-foraging-subsistence.md:27,:36`, `fire-fuel-light.md:37`, `textile-technology.md:27`, `transport-mobility-lexicon.md:95`, `sacred-kingship-mythic-charter.md:65`, `ritual-liminality.md:63`, `symbolism-synthesis-method.md:69`, `celestial-symbolism-calendars.md:28`, `verification/calibration-registry.md:142`.

### Counterexample 1: false self-claim that §2 cites animal-symbolism (BROKEN, one line)

`PAH:4` says: "Partial owners keep their pieces and are cited one-way in §2: … livestock-as-wealth idiom (`animal-symbolism.md:73,:110`)."

The §2 one-owner table (`PAH:29-39`) has nine rows: agrarian, hunting, cuisine, transport, trade-economy, textile, semantic-fields, fire-fuel and `civilizations/`. **None of them is `animal-symbolism.md`.** The only body citation is the single closing sentence of §10, `PAH:145` ("The herd's signs belong to `animal-symbolism.md:73,:110`"). The build-wave critic's anchor contract (`.ufo/waves/round-50/build/CriticGapPremise.md:71-72`: "boundary table names at least … `animal-symbolism.md:110`") is therefore unmet.

- Impacted axes: coverage (the one-owner boundary is incomplete) and calibration (the head misstates its own body).

### Counterexample 2: Sherratt is regraded with no citation of the existing owner (duplicate authority)

- Owner: `culture-material/agrarian-field-system-lexicon.md:80` says "**Secondary-products revolution** (Sherratt 1981: traction, milk, wool, manure arriving after domestication) — … contested as a single horizon (to-verify)."
- PAH restates and grades the same proposition twice without citing `:80`:
  - `PAH:93`: "Sherratt's 'secondary products revolution' — … (S051) — is **C**: the review finds adoption regional and staged, not one horizon (S051)."
  - `PAH:183`: "Sherratt's secondary products arrived as one revolution \| C — S051".
- `:80` appears only in the header anchor list `PAH:6`. The §2 agrarian row (`PAH:31`) cites `:56,:62`, not `:80`.
- Result: two entries now grade Sherratt. Agrarian says "contested (to-verify)" with no source. PAH says C with S051 opened. Neither points to the other at the claim. The build-wave contract (`CriticGapPremise.md:69`: "Sherratt is cited as a bounded hand-off to `agrarian:80` … not re-owned") was not implemented.

### Counterexample 3: the Nuer cattle idiom is restated three times with no inline citation, and its tier differs from the owners'

- Owners:
  - `myth-symbol/animal-symbolism.md:73`: "cattle as social idiom — names, songs, bridewealth".
  - `culture-material/trade-economy-lexicon.md:69`: "Nuer cattle as the idiom of all value (Evans-Pritchard 1940)".
  - Both state it **without** a tier qualifier.
- PAH restates it at three places, none citing `animal-symbolism.md:73`:
  - `PAH:59`: "social idiom in Nilotic ethnography (S052) is regional, not a law".
  - `PAH:106`: "Evans-Pritchard wrote that 'Nuer tend to define all social processes and relationships in terms of cattle' (S052): a 1940 outsider's functionalist claim, **B** to that people and period."
  - `PAH:186`: "'Nuer define everything through cattle' generalises to herders \| B — S052".
- This regrade is the better calibration, because it rests on an opened source with place and date. But it lands as a second authority: a reader of animal-symbolism or trade-economy gets the unbounded form, and a reader of PAH gets B. Neither text is linked to the other at the claim.
- PAH's §5 colour and age×sex rows (`PAH:75-76`) are new sourced facts that refine `semantic-fields:70`. They are not duplication.

### Counterexample 4: "five snouts" restates `animal-symbolism.md:110` with no inline citation

- `PAH:67`: "The Mongolian 'five snouts' — horses, yaks/cattle, camel, goats and sheep — is an emic portfolio term (S060)".
- `PAH:78`: "Species set \| 'five snouts' as one collective term (S060)".
- Owner: `animal-symbolism.md:110` already carries "the Mongol five livestock (horse, cattle, camel, sheep, goat) structure wealth-language".
- PAH frames the set as a production portfolio and a collective noun, which is a defensible distinct use with its own external source. Still, the build-wave contract (`CriticGapPremise.md:70`: "The five-livestock material defers the value-idiom reading to `animal-symbolism.md:110`") is met only by the distant generic sentence at `PAH:145`.
- This one is weak. It is overlap on the same species list, not a contradiction.

### Counterexample 5: wrong boundary anchor for the cuisine owner

- `PAH:33` (§2) assigns "yogurt lineages, milk+meat law, Harris's cattle economy (contested)" to `cuisine-food-lexicon.md:67,:86`. `PAH:8` repeats "owns the dish and milk+meat law, `:67,:86`".
- At the landed bytes:
  - `:67` is yogurt lineages ✓.
  - `:86` is Harris's "cattle are worth more alive (traction, milk, dung)" ✓.
  - **The milk+meat law is at `cuisine-food-lexicon.md:81`** ("Mixing rules \| milk + meat separation (Ex 23:19 …)"), not at `:67` or `:86`.
  - The "contested" status is at `:152` ("Harris's materialist taboos … contested … weakest the cow").
  - `animal-symbolism.md:67-68` co-owns milk-meat separation and Harris's sacred-cow economics, and §2 does not cite it.
- Impacted axis: coverage boundary precision.

## Impacted axes

- **Coverage:** the gain is real, and no existing owner is displaced. But the one-owner boundary misses animal-symbolism in §2 and carries one wrong cuisine anchor (`:81`).
- **Calibration:** there are duplicate grading authorities for Sherratt and the Nuer idiom. The head misstates where it cites animal-symbolism. The `claims.json` `lowest_axis_reasoning` premise wording is stale and not logged in §Mistakes.
- **Operability:** none.

## Smallest safe correction

These are author-lane advice and one-way edits inside C's `lands` (PAH only). No partial-owner file is edited.

1. Add a §2 row after `PAH:37`: `` | `animal-symbolism.md:67,:68,:73,:110` | milk-meat separation, sacred-cow theories, Nuer cattle idiom, five-livestock value idiom | the herd facts behind the idiom; §4, §7 supply inputs | ``. This makes `PAH:4` true.
2. At `PAH:93`, add after "(S051)": "; the generator lives at `agrarian-field-system-lexicon.md:80` (to-verify there), this row supplies the opened grading". Add `:80` to the §2 agrarian row at `PAH:31`.
3. At `PAH:106`, add: "(the idiom itself is owned at `animal-symbolism.md:73` and `trade-economy-lexicon.md:69`; read them under this B bound)".
4. At `PAH:67`, add: "; its value-idiom reading is `animal-symbolism.md:110`".
5. At `PAH:8` and `PAH:33`, change `cuisine-food-lexicon.md:67,:86` to `cuisine-food-lexicon.md:67,:81,:86`.
6. Lesson: add an R50-M row for the stale `claims.json` `lowest_axis_reasoning` "cross-references" wording. The declaration is frozen, so record the narrowing rather than edit it.
7. Optional reciprocal edits (a new claim, not C): repoint `agrarian:80`'s "(to-verify)" to S051, and qualify `animal-symbolism.md:73` / `trade-economy-lexicon.md:69` with the B bound.

## Unrun / out of scope

- External rows (S048–S069) were not opened. That belongs to the source re-opener seats.
- `reports/round-28/readme/sweep.py` and the entry-contract shape checks were not run.
- The sibling-lane sweep read the current working trees of the other 20 `*-shokunin` lanes (read-only `rg`), not pinned commits.
