# CriticGapPremise — round 50, claim C premise ("pastoralism/animal husbandry is unowned")

Seat: critic (leaf). Read-only sweep at HEAD `4ad26836552462d28a946ca3b067cab0b5ce3532` (lane HEAD == base, verified `git log -1`). All six partitions swept on topic lines, H1–H3, table rows and body text. No installs. Paths below are relative to `corpus/knowledge/` unless prefixed.

## Verdict

**The premise holds narrowly and fails in its blanket wording.**

- **Holds:** there are 0 filename owners and 0 topic-line owners. The claim's own word-mode probe terms (`pastoralism|pastoral|herding|husbandry|transhumance|livestock`) match no `- topic:` line: `grep -rniwE` gives rc=1. No filename contains `pastor`, `herd`, `husband`, `nomad` or `livestock`.
- **Fails:** "existing mentions are cross-references" (`reports/round-50/claims.json` `lowest_axis_reasoning`) is false. At least six entries partly own a piece of the pastoral register at section or table-row level, with method content of their own. Two of these are files the claim itself names as "cross-references": `agrarian-field-system-lexicon.md` and `semantic-fields-lexicon-building.md`. This is the same defect the r49 critic raised for hunting (`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika-w3/kotodama-critic.md:6`: the filed "0 true topic owners" hid partial owners, one of which was `semantic-fields-lexicon-building.md`).
- **Fixable defect, not a judge-reject tradeoff.** Narrow the claim to a comparative pastoral production-system gap (see the last section) and keep the topic-level probe.

## Counterexample 1: the claim's own evidence command returns a hit

`reports/round-50/claims.json` before-check `pastoral-unowned` sets `expect: true` with `mode: "word"`. Its `evidence_command` is `grep -rniE '^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)'`, a substring match. Run at base, it returns one line: `culture-material/writing-media-surface-economy.md:3`. The match is `herd` inside "**sherd**, wall, pot, body". The probe and the evidence command disagree, so a judge who runs the evidence command literally sees a non-empty result for a check that expects absence.

- Smallest fix: `grep -rniE '^- topic:.*\b(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/`. Tested at base: rc=1, 0 lines.
- Impacted axis: calibration (false-positive evidence on a declared before-state).

## Counterexample 2: partial owners (own a sub-register with method content)

| Anchor | What it already owns | Class |
|---|---|---|
| `culture-material/agrarian-field-system-lexicon.md:62` | **Agropastoral** row in the field-system typology: "fields + pasture + transhumance routes \| ploughing peak plus herd calendar; manure contracts \| … herd rights; manure-for-stubble exchange \| fold, transhumance, stubble-right". This is the only corpus use of "transhumance". | partial owner (mixed farming, herd calendar, stubble rights) |
| `culture-material/agrarian-field-system-lexicon.md:56` | Communal herding after harvest and common pasture rights in the open-field row | partial owner (commons grazing inside the field system) |
| `culture-material/agrarian-field-system-lexicon.md:80` | **Secondary-products revolution (Sherratt 1981: traction, milk, wool, manure)**, marked "contested … (to-verify)" | partial owner, with a direct collision with the `SrcSherratt-4` source seat |
| `linguistics/semantic-fields-lexicon-building.md:70` | "Pastoral wealth vocabulary (herd-age, herd-color, herd-condition terms) indexes property systems; … PIE horse/wheel/pastoral vocabulary … (Anthony 2007)" | partial owner (pastoral lexicon field) |
| `linguistics/semantic-fields-lexicon-building.md:105` | Field-priority table row "steppe pastoral \| subsistence (herd wealth), kin (clan), war (raid), landscape (pasture)" | partial owner (lexicon elaboration brief) |
| `myth-symbol/animal-symbolism.md:110` | "the Mongol five livestock (horse, cattle, camel, sheep, goat) structure wealth-language; … Decide which species is the culture's **idiom of value**" | partial owner (livestock as value idiom), colliding with the `SrcMongolFiveSnouts-4` seat |
| `myth-symbol/animal-symbolism.md:73`, `:68` | Nuer "cattle of money" (Evans-Pritchard 1940: names, songs, bridewealth); sacred cow, Harris traction/milk/dung vs Simoons | partial owner (cattle-complex symbolism and taboo) |
| `culture-material/trade-economy-lexicon.md:69-70` | fee/pecuniary < *pecus* 'cattle'; capital/cattle/chattel "wealth counted by heads"; Nuer idiom of value | partial owner (livestock-as-currency lexicon), colliding with `ScribeSec07Wealth-4` |
| `culture-material/transport-mobility-lexicon.md:4`, `:70`, `:95` | DRAFT layer "ox, horse/mule, camelid, dog", harness and feed vocabulary, llama load figures | partial owner (traction and pack animals), colliding with `ScribeSec06Products-4` if traction appears there |
| `culture-material/textile-technology.md:11`, `:27` | Fiber gate (sheep flocks); worsted vs woollen; Ryder 1983 fleece evolution | partial owner (wool product chain) |
| `culture-material/fire-fuel-light.md:37` | Dried-dung fuel row: "a real trade-off against manure; fuel-poor pastoral cultures pay for it in soil" | narrow partial owner (dung as fuel only) |

## Cross-references (mention only, no ownership)

- **Regional calibration guards in civilizations.** None of these files has a pastoral topic. Each carries an anti-stereotype flag that the new entry's calibration section should cite rather than restate as new (`ScribeSec13Calibration-4`):
  - `civilizations/mongol.md:40`: "not a ladder from 'primitive nomad' … Mobile pastoralism, urban production … can coexist".
  - `civilizations/mongol.md:146`, `:166`, `:185`: the yam's post-horses, provision sheep and milch mares, and winter pasture as a bottleneck. These belong to the yam register, not to husbandry.
  - `civilizations/turkic-steppe.md:18` (H2 "not a timeless nomad kit"), `:26`, `:98`, `:148`, `:183`: "nomadic" and "textual" are not opposites, and pastoral production is not isolation.
  - `civilizations/scythian-saka.md:70`: pastoralism ≠ no farming (Herodotus 4.17–20).
  - `civilizations/finnic-sami.md:140`, `:150`: reindeer herding is not Sámi identity, and large-scale pastoralism has a history (Aikio 2012: 86).
  - `civilizations/dine-navajo.md:116`, `:125`: grazing → sheep → fleece causal chain, and Navajo-Churro sheep introduced from Spain.
  - Smaller mentions: `civilizations/india-tamil-sangam.md:77` (Mullai pastoral landscape), `civilizations/zimbabwe-shona.md:142`, `:164`, `civilizations/arabia-pre-islamic.md:68`, `:113`, `:174` (camel and Safaitic nomads), `civilizations/india-vedic.md:31`, `:137`.
  - The H1s of `scythian-saka.md:1` and `turkic-steppe.md:1` name the "steppe" polity, not the husbandry register.
- **Hunting boundary.** `culture-material/hunting-foraging-subsistence.md:36` excludes "herded" sources from its register (wild-source property). Its neighbour list (`:4`) does not name a pastoral owner. That is consistent with a gap, and the new entry should cite `:36` as the reciprocal boundary.
- **Myth and synthesis.** `myth-symbol/celestial-symbolism-calendars.md:28`, `:112`, `:118` (pastoralist sky constraint; milk → dairy purity rules). `myth-symbol/hero-journey-variants.md:110` ("steppe/pastoral → … cattle-raid quests"), already flagged as a non-law by `synthesis/source-discipline-calibration.md:96`, which the entry must not invert into a causal claim. Also `linguistics/semantics-pragmatics.md:22`, `linguistics/semantic-fields-lexicon-building.md:41`, `verification/costume-era-consistency-gate.md:65` (MAT-02 herding as fiber source), `synthesis/coupling-model.md:150`, `synthesis/worked-example-mini-culture.md:26`, `cuisine-food-lexicon.md:67`, `:81` (yogurt lineages; milk-meat law owned with animal-symbolism), `music-instrument-lexicon.md:87`, `myth-symbol/sacred-kingship-mythic-charter.md:65` (shepherd-king metaphor).

## Counterexample 3: r49 filed bytes contradict r50

`reports/round-49/claims.json:30` asserted that "adjacent registers own agrarian, animal, cuisine, **pastoral**". No pastoral owner existed then or exists now; only the partial owners above do. r50's "0 topic owners" is the correct reading. The new entry and the round lesson MUST NOT cite the r49 sentence as evidence of a prior owner. They also must not silently treat r50 as overturning a real owner. Record it as a stale r49 premise, as the r49 critic did for `claims.json:19`.

## What is genuinely unowned (corpus-wide grep, 0 hits at base)

- Herd demography and risk: offtake, herd growth and loss, restocking, herd splitting and loaning.
- Mobility regimes as a typology: transhumance, nomadism, agropastoral sedentism, ranching. `agrarian:62` only lists "transhumance routes" as one row attribute.
- Pasture tenure and common-pool governance. Hardin and Ostrom are cited nowhere for pastures; the only "Hardin" hit is `linguistics/color-terminology.md:46`, Hardin & Maffi on color.
- Dairy and meat specialization as production choices (kumis, butter, cheese as a pastoral output chain). Only `cuisine-food-lexicon.md:67` names "yogurt lineages" as a ferment.
- Herd-as-capital institutions (bridewealth herds, stock friendship) as production and social organization. `animal-symbolism.md:73` owns the symbolic idiom only.
- A herding decision table that ties species mix to ecology, mobility and tenure.

## Smallest safe correction (exact narrowing)

1. **Reword `claims.json` C `before` and `lowest_axis_reasoning`.** Replace "no filename or topic owner … existing mentions are cross-references" with: "0 filename and 0 topic-line owners; **comparative pastoral production-system gap** (herd management and demography, mobility regime, pasture tenure and commons, product specialization). Partial owners keep their sub-registers: agropastoral field system and secondary products (`agrarian-field-system-lexicon.md:56,62,80`), pastoral lexicon (`semantic-fields-lexicon-building.md:70,105`), livestock value idiom and cattle complex (`animal-symbolism.md:68,73,110`; `trade-economy-lexicon.md:69-70`), traction and pack animals (`transport-mobility-lexicon.md:95`), wool (`textile-technology.md:11,27`), dung fuel (`fire-fuel-light.md:37`)." If the filed bytes are frozen, record this narrowing in the r50 report and lesson instead of editing them.
2. **Fix the evidence command** to use `\b`, as tested above.
3. **Entry contract additions (C lands only):**
   - The one-owner boundary section names every partial owner above with its live anchor and the line the entry does not cross, plus the hunting reciprocal boundary at `hunting-foraging-subsistence.md:36`.
   - Sherratt is cited as a bounded hand-off to `agrarian:80` (to-verify there), not re-owned.
   - The five-livestock material defers the value-idiom reading to `animal-symbolism.md:110`.
   - The calibration flags cite the civilization guards rather than restating them as new.
4. **Landing gate (r49 critic correction, still unimplemented in r50 `after_required`).** Add a post-landing topic recheck: exactly 1 topic owner (the new entry) under the fixed regex. Also add an anchor check that the boundary table names at least `agrarian-field-system-lexicon.md:62`, `semantic-fields-lexicon-building.md:70`, `animal-symbolism.md:110` and `transport-mobility-lexicon.md:95`.
5. **Separability.** The entry cannot edit `agrarian:80` or any partial owner, because C's `lands` are only the entry and `corpus/README.md`. Boundaries are therefore one-way citations. Any reciprocal edits would be a new claim, not part of C.

## Impacted axes

- **Coverage:** the gain is real but narrower than declared. A comparative production-system entry passes; a blanket "pastoralism" register would duplicate six partial owners.
- **Calibration:** the stale premise wording, the evidence-command false positive, and the r49 `claims.json:30` contradiction.
- **Operability:** none.

## Unrun checks

- No entry draft was inspected: none was landed or patched at sweep time, so boundary-table compliance is unverified.
- `reports/round-28/readme/sweep.py` was not run (assignment is premise only).
- External sources were not opened (critic seat).
