# ScoutCalibrationRegistry — round 50, claim C (pastoralism calibration bank)

Assigned item: read `corpus/knowledge/verification/calibration-registry.md` and the hunting entry's §13, then state the exact code/format contract the pastoralism entry must use and the candidate mainstream/contested/discredited items, with opened-source evidence. Author-lane advice only; no production file was edited, no admission is claimed.

Baseline measured this seat: `find corpus/knowledge -name '*.md' | wc -l` → **225**; `ls corpus/knowledge/culture-material/*.md | wc -l` → **27** (matches `reports/round-50/claims.json` before-state).

---

## 1. The code system (observed, not inferred)

`corpus/knowledge/verification/calibration-registry.md:33-39` defines the only five codes an entry may use; `:35-39` are the data rows, which is the span both model entries cite.

| Code | Registry wording (`:35-39`) | Stop rule in practice |
|---|---|---|
| R | "Rejected/discredited as the specified general inference" | never evidence; may appear only as a dated ideology inside fiction, and then labelled |
| C | "Contested empirical or historical interpretation" | carry alternatives, scope and discriminating evidence |
| B | "Bounded, usable within a named domain" | carry population, genre, period, task and exceptions |
| H | "Heuristic or interpretive framework, not an established causal law" | generate with it; label the designer's choice |
| T | "Unresolved provenance or claim check" | inline `(to-verify)` at the exact dependency; not load-bearing |

A code attaches to a **proposition**, not to an author, people or religion (`:31`). Multiple codes may split one theory (`:41`: "Multiple codes may apply to different parts of one theory").

## 2. The format contract (both models agree; use hunting's shape)

Observed in `corpus/knowledge/culture-material/hunting-foraging-subsistence.md:176-197` (§13, round 49 — the newer model) and `corpus/knowledge/culture-material/cartography-and-mapmaking.md:214-231` (§12).

1. **Placement:** `## <N>. Calibration bank` immediately after the NON-CANON micro-example, followed by `## <N+1>. Recheck` and `## <N+2>. Scope`. Numbering is per entry (hunting 13/14/15, cartography 12/13/14); it is not a fixed global number.
2. **Lead line, verbatim pattern:**
   ```
   Codes per `calibration-registry.md:35-39` (R rejected, C contested, B bounded, H heuristic, T to-verify).
   ```
3. **Table header, exactly:** the hunting form is
   ```
   | Claim | Status | What to say instead |
   ```
   or the cartography variant, which puts the citation in the header cell:
   ```
   | Claim | Status (`calibration-registry.md:35-39`) | What to say instead |
   ```
   Pick one; do not do both.
4. **Three columns, no fourth:**
   - `Claim` — the overclaim in quotation marks, as a worldbuilder would repeat it. Not a topic label.
   - `Status` — the code **plus qualifier plus evidence**: `R (as universal) — S0NN ...`; `C — S0NN's number ...`; `B — S0NN presents ... as a tool`; `T — <what is unopened>`. A bare code with no evidence is a defect in both models.
   - `What to say instead` — one imperative clause naming the replacement practice or the phrasing to use. No essays.
5. **Rows are propositions, not verdicts on people.** Expected density: 10–12 rows for this entry size (hunting has 12, cartography 11).
6. **After the table, two bolded paragraphs** (hunting `:195,197`; cartography `:230-231`):
   - `**Living-practice flag** …` — the register is a live livelihood/identity for real people; state the borrowing limit.
   - `**Precision traps.** …` — etic umbrellas and collapsed terms, named.
7. **No row without a replacement.** Registry `:36` forbids leaving C as "one reading is settled"; the third column is where that is discharged.
8. **Cross-reference the registry's CAL rows where the same brake already exists** — for pastoralism the load-bearing ones are `calibration-registry.md:51` (CAL-04, the evolutionary ladder), `:53` (CAL-06, the disaggregate-the-package template), `:142` (§9: "subsistence predicts a total social stage — R"). Citing them keeps the entry from inventing a second calibration vocabulary.

## 3. Candidate calibration bank for the pastoralism entry

Statuses below are mine, derived from the opened evidence in §4 plus the in-corpus anchors; the C author should adopt or downgrade them explicitly, never silently.

| Claim | Status | What to say instead |
|---|---|---|
| "Pastoral nomadism is the stage between hunting and farming" | **R** — FAO 2001 calls it an older, Marxist-influenced reading and notes agriculture generally predates pastoralism outside Africa (`S?` = FAO y2647e02 §History and origins); registry `:51,:142` | Write a specialization, not a rung: herds outgrow the settlement's grazing, movement follows patches; the culture can farm and herd at once |
| "Pastoralists are pure herders who do not cultivate" | **R** as a type — FAO: "Any classification of this type must be treated as a simplification"; agropastoral communities predominate south of the equator, exclusive pastoralists are a pole (`S?` = FAO y2647e02 §Pastoral enterprises); in-corpus `agrarian-field-system-lexicon.md:56` (communal herding after harvest) | Give every herding culture a cultivation share and a switching rule; movement is a dial (nomadic ↔ transhumant ↔ agropastoral ↔ enclosed), not an identity |
| "Nomads wander without logic" | **R** — FAO quotes the Ammianus/Hun stereotype, then: "In reality, pastoralists' landscape is flecked with an invisible constellation of resources" (`S?` = FAO y2647e02 §Nomadism) | Movement is route knowledge — pasture, rainfall, disease, borders, markets; write the route map and its triggers (drought, epizootic, war) |
| "Herskovits's cattle complex explains why herders refuse to destock" | **R** as a unitary explanation — FAO: "The traditional view derives from the cattle complex concept first mooted by Herskovitz (1926)"; the market-keyed risk-aversion alternative "gained considerable ground from the 1960s onwards" (`S?` = FAO y2647e10 §Pastoralists and the environment) | Cattle's social value is real in documented cases, but disaggregate it: `animal-symbolism.md:73` (Nuer "cattle of money"), `:110` (five-livestock wealth-language); add insurance against drought/epizootic as a second reason |
| "Cattle are money; herders are pre-market" | **C** — same FAO passage (ritual/prestige nexus vs market enterprise is the contested pair); `animal-symbolism.md:73` treats cattle as idiom, "not primarily food" | Name the function: bridewealth, fine, sacrifice, savings, sale; a unit of account is not a medium of exchange, and conversion rules are the design |
| "The tragedy of the commons explains rangeland degradation" | **R** as a model of pastoral tenure — Hardin's pasture is "open to all" (no rules, no sanctions); Hardin himself retitled the problem "the tragedy of the unmanaged commons" (1994); Ostrom 1990: commons are "sometimes … solved by voluntary organizations rather than by a coercive state" (`S?` = Hardin 1968, Hardin 1994, Ostrom 1990) | Common property ≠ open access: write the tenure bundle (who may graze where, when, how many), the sanctioning body and the boundary; run Ostrom's questions, not Hardin's parable |
| "Grazing always degrades; herds cause desertification" | **C** — FAO reports "serious doubts about the long-term impact of overgrazing, and more emphasis laid on the resilience of rangelands", but also documents collapse on high-altitude grassland (Box 4, Mambila Plateau) (`S?` = FAO y2647e10) | Specify the rangeland: non-equilibrium semi-arid vs high-altitude/subhumid; give stocking history, rainfall and the baseline "degraded" is measured against; do not universalize either direction |
| "Pastoralists are egalitarian and free" | **R** — FAO documents slave and vassal castes (Tuareg Imajer.en/Iklan/Izeggar.en/Ineden), Fulɓe cattle herds managed by slave labour in the nineteenth century, and a patrilineal, male-dominated majority (`S?` = FAO y2647e08 §Social structures, §Role of women) | Stratify by herd wealth, labour access, caste/slave descent, gender and age-set; write the dependants and the poor, not only the horseman |
| "Pastoralists are warlike predators by nature" | **R** as ethnic character; **B** for the historical association of mobility with raiding and state relations — FAO: "Pastoralism and raiding have been associated since ancient times"; centre-periphery warfare "largely ceased, probably mainly as a result of the introduction of the aeroplane" (`S?` = FAO y2647e02 §Pastoralism and warfare; y2647e09) | Raiding is an institution with a political economy: who sanctions it, what it captures, how the state answers; keep raid, warfare and state formation as separate clocks |
| "Herders and farmers are eternal enemies" | **C** — FAO: conflict is real and everyday, but "tenure regimes that are more supportive of agriculture than livestock" and political power decide it; transhumant herders build patronage and crop-residue exchange with farmers (`S?` = FAO y2647e02 §Transhumance; y2647e10) | Write the contract before the clash: passage rights, manure-for-residue, cattle tracks; escalation follows tenure change and state favour, not ethnicity |
| "The Secondary Products Revolution is one horizon spreading from the Near East" | **C** — Marciniak 2011: "stresses the idiosyncratic nature of the introduction of secondary products in particular areas"; also challenges a meat-based livestock system for early farmers (`S?` = Marciniak) | Treat milk, wool, traction and riding as separate innovations with regional dates; a multi-product herd needs no revolution |
| "Modern horses descend from Botai, and riding spread Yamnaya and Indo-European" | **R** — Librado 2021: "modern domesticated breeds do not descend from the earliest domestic horse lineage associated with archaeological evidence of bridling, milking and corralling"; modern horses spread from the lower Volga-Don from about 2000 BC, and the results reject the riding/Yamnaya association around 3000 BC (`S?` = Librado) | Keep four clocks apart: horse domestication, riding, chariotry, language dispersal; a bit or a wagon does not date a language |
| "Dairying selected lactase persistence in every herding population" | **C** — Segurel 2020: "Central Asian herders are mostly lactase nonpersistent, despite their significant dietary reliance on dairy products"; the T allele spreads 4000–3500 BP and rises in Europe after 3000 BP, not in Asia (`S?` = Segurel) | Dairying works without LP — fermentation, heating, small servings; genes, diet and herd species are separate evidence lines |
| "Domestication is an event: someone tamed an animal" | **C** — FAO: earliest pastoralism involved management of wild animals, "as reindeer pastoralism still does today"; early cattle dates are disputed (`S?` = FAO y2647e02 §History and origins); deep dates `(to-verify)` | Write a process: tolerated wild populations → herd management → morphological change → specialized pastoralism; dates regional and checked |
| "Pastoralism is one worldwide institution" | **R** — FAO classifies by species, management, geography and ecology, and calls every such classification a simplification (`S?` = FAO y2647e02 §Classifying pastoral systems) | Specify species, movement mode, ecology and household; a Mongolian five-livestock herd is not a Nuer cattle camp |

Optional (only if the entry's word budget allows; both are design-precision rows rather than myth rows): "the horse is a weapon of conquest" (**B/C** — separate transport, traction, riding and cavalry, `transport-mobility-lexicon.md:20`); "pastoral vocabulary dates the pastoral expansion" (**T/C** — reconstructed PIE pastoral vocabulary is a model case, not a clock, `semantic-fields-lexicon-building.md:70,105`).

Budget note: the table above is a candidate pool of 15, not a target. For a 10–12-row bank (the model density) fold three into their host sections: "nomads wander without logic" → the mobility/route section; "pastoralism is one worldwide institution" → §1's register property; "domestication is an event" → the coupling move. Keep the rest; retain both the Hardin row and the overgrazing row only if the entry carries a tenure section that distinguishes open access from common property and an environment section that names the rangeland type.

**Living-practice flag (draft, to adapt):** pastoralism is a live livelihood and identity — FAO estimates about 20 million pastoral households, and many are subject to state sedentarization policy (FAO y2647e01 Summary; y2647e02 Overview). Name region and community when borrowing a practice; never use "nomad" as a synonym for "primitive", "lawless" or "vanished".

**Precision traps (draft, to adapt):** "pastoralism" ≠ "nomadic pastoralism" ≠ "transhumance" ≠ "agropastoralism" ≠ "ranching" (FAO y2647e02 §Pastoral enterprises); "nomad" is an etic label with a pejorative transmission (Ammianus quoted in FAO); "cattle complex" is a dated analytical term, not a local category; herd "ownership" is usually a bundle of rights (access, milk, offspring, slaughter), not exclusive title; "overstocking" is a judgment against a stated carrying-capacity model.

## 4. Candidate SOURCES rows (opened this session; L1 assigns S048+)

All opened 2026-10-21. Quotes are verbatim and ≤25 words; locations are section-level. Registering these is the frontier step's call — I did not write `corpus/SOURCES.md`. On registration, every row the entry cites must carry `used-by: corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` and move `queued`→`mined` in the same edit, or the C after-check ("every cited S-id resolves to a SOURCES row whose used-by names the entry") fails.

| Candidate | Source | Kind | Tier | Scope | Anchor | Teaches | Recheck |
|---|---|---|---|---|---|---|---|
| S048? | FAO (2001), *Pastoralism in the new millennium*, Animal Production and Health Paper 150 — https://www.fao.org/4/y2647e/y2647e02.htm | docs | B | definitions, classification and history-of-the-idea of pastoralism; institutional synthesis, not primary ethnography | §Classifying pastoral systems; §Pastoral enterprises; §Nomadism; §History and origins of pastoralism; §Pastoralism and warfare | movement-mode typology is a simplification; the stage reading is an older, ideologically loaded one; agriculture generally predates pastoralism outside Africa; raiding is historically associated with mobility | 365d (static report; check for newer FAO pastoral guidance) |
| S049? | FAO (2001), same report — https://www.fao.org/4/y2647e/y2647e10.htm | docs | B | the cattle-complex and overgrazing debates as summarized for policy | §Pastoralists and the environment; Box 4 (Mambila Plateau) | the cattle-complex reading is the "traditional view", with a market/risk-aversion alternative since the 1960s; overgrazing impact is doubted for semi-arid rangelands but documented on high-altitude grassland | 365d |
| S050? | FAO (2001), same report — https://www.fao.org/4/y2647e/y2647e08.htm | docs | B | social structure, gender and pastoral tenure | §Social structures; §Role of women; §Land tenure and the common property resources debate | pastoral societies include slave/vassal castes and are mostly patrilineal and male-dominated; pastoral tenure is a common-property debate, not open access | 365d |
| S051? | Hardin (1968), "The Tragedy of the Commons", *Science* 162:1243–1248 — https://faculty.washington.edu/stevehar/HardinTragedy.pdf | paper | B | Hardin's argument as printed; university-hosted facsimile, publisher page 403 | §The Tragedy of Freedom in a Commons (PDF p. 2 of 6; article pp. 1243–1248) | the model's pasture is "open to all", i.e. it assumes no institutions; the driver is an unmanaged commons, not common property as such | 365d; flip: open science.org/library copy before load-bearing quotation |
| S052? | Hardin (1994), "The tragedy of the unmanaged commons", *Trends in Ecology & Evolution* 9(5):199 — https://pubmed.ncbi.nlm.nih.gov/21236819/ | paper | A for bibliographic identity only | the existence and title of Hardin's retitling note; argument not read | PubMed record, title and citation fields | Hardin renamed the problem "unmanaged" — governance absence is the model's premise | 365d |
| S053? | Ostrom (1990), *Governing the Commons*, Cambridge University Press — https://assets.cambridge.org/97811075/69782/frontmatter/9781107569782_frontmatter.pdf | book | B | the book's stated thesis (publisher frontmatter, not the argument's evidence chapters) | Frontmatter blurb, p. i | common-pool problems are "sometimes … solved by voluntary organizations rather than by a coercive state"; neither state nor market is uniformly successful | 365d; flip: read ch. 3 for the design principles before quoting them |
| S054? | Marciniak (2011), "The Secondary Products Revolution: Empirical Evidence and its Current Zooarchaeological Critique", *Journal of World Prehistory* 24:117–130 — https://link.springer.com/article/10.1007/s10963-011-9045-7 | paper | A | zooarchaeological critique of Sherratt's Secondary Products Revolution | Abstract; §Current Zooarchaeological Critique | milk, wool and traction are real but introduced idiosyncratically by region; early farmers were not a meat-only system; no single horizon | 365d |
| S055? | Librado et al. (2021), "The origins and spread of domestic horses from the Western Eurasian steppes", *Nature* 598:634–640 — https://www.nature.com/articles/s41586-021-04018-9 | paper | A | origins of modern domestic horses (DOM2) and the riding/Yamnaya question | Abstract | modern horses do not descend from the Botai lineage; DOM2 spreads from the lower Volga-Don from about 2000 BC with Sintashta chariotry; the riding-driven Yamnaya expansion around 3000 BC is rejected | 365d (a 2024 *Nature* paper on horse-based mobility is cited on the page; re-open it before extending) |
| S056? | Segurel et al. (2020), "Why and when was lactase persistence selected for? Insights from Central Asian herders and ancient DNA", *PLOS Biology* 18(6):e3000742 — https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000742 | paper | A | lactase persistence, dairying and Central Asian herders | Abstract; §Central Asia, the exception that proves the rule? | Central Asian herders are mostly LP-nonpersistent despite heavy dairy reliance; fermentation is a cultural adaptation; LP spread 4000–3500 BP with steppe populations, then rose in Europe but not Asia | 365d |

Ready-to-paste Gate lines for `corpus/lessons/round-50.md` (same shape as `corpus/lessons/round-49.md:27-60`):

- `S048 — https://www.fao.org/4/y2647e/y2647e02.htm — accessed 2026-10-21 — §History and origins of pastoralism: "Pastoralism was seen as an evolutionary stage in human history, a phase following hunting-gathering and leading to sedentarization and agriculture." Grounds the stage reading as an older, rejected frame.`
- `S049 — https://www.fao.org/4/y2647e/y2647e10.htm — accessed 2026-10-21 — §Pastoralists and the environment: "The traditional view derives from the cattle complex concept first mooted by Herskovitz (1926)". Grounds the cattle-complex status and its alternative.`
- `S050 — https://www.fao.org/4/y2647e/y2647e08.htm — accessed 2026-10-21 — §Land tenure and the common property resources debate: "Pastoral systems have been at the heart of many debates on the nature of common property resources." Grounds the tenure framing.`
- `S051 — https://faculty.washington.edu/stevehar/HardinTragedy.pdf — accessed 2026-10-21 — §The Tragedy of Freedom in a Commons, PDF p. 2: "Freedom in a commons brings ruin to all." Grounds the open-access premise.`
- `S052 — https://pubmed.ncbi.nlm.nih.gov/21236819/ — accessed 2026-10-21 — record title: "The tragedy of the unmanaged commons". Grounds Hardin's own retitling; argument not read.`
- `S053 — https://assets.cambridge.org/97811075/69782/frontmatter/9781107569782_frontmatter.pdf — accessed 2026-10-21 — frontmatter blurb, p. i: "common-pool problems sometimes are solved by voluntary organizations rather than by a coercive state". Grounds Ostrom's thesis at blurb tier.`
- `S054 — https://link.springer.com/article/10.1007/s10963-011-9045-7 — accessed 2026-10-21 — abstract: "stresses the idiosyncratic nature of the introduction of secondary products in particular areas". Grounds the regional-timing critique.`
- `S055 — https://www.nature.com/articles/s41586-021-04018-9 — accessed 2026-10-21 — abstract: "modern domesticated breeds do not descend from the earliest domestic horse lineage associated with archaeological evidence of bridling, milking and corralling". Grounds the Botai rejection.`
- `S056 — https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000742 — accessed 2026-10-21 — abstract: "Central Asian herders are mostly lactase nonpersistent, despite their significant dietary reliance on dairy products". Grounds the LP counter-case.`

## 5. Sources that failed and must NOT be registered as opened

- Herskovits (1926), "The Cattle Complex in East Africa", *American Anthropologist* 28 — AnthroSource returned **HTTP 403**, AfricaBib **timed out**. The cattle-complex row therefore rests on FAO's summary (S049) and the in-corpus Nuer anchor; the primary is a genuine `(to-verify)` if the entry wants Herskovits's own wording.
- Khazanov (1984), *Nomads and the Outside World* — Cambridge chapter page returned **HTTP 429**; only search snippets seen. Do not register; cite Khazanov only through FAO's citations, marked `(to-verify)`.
- Dyson-Hudson & Dyson-Hudson (1980), "Nomadic Pastoralism", *Annual Review of Anthropology* 9 — **HTTP 403**. Same handling.
- "The Archaeology of Pastoral Nomadism", *Annual Review of Anthropology* 45 (2016) — **HTTP 403**.
- Zeder (2015), PNAS domestication review — **HTTP 403**; the domestication-process row therefore rests on FAO's history section only.
- Ostrom's Cambridge core book page returned **HTTP 429**; the CUP frontmatter PDF (S053) is the opened substitute.

## 6. Unrun checks and remaining unknowns

- Not run: the lane's entry linter/sweep (out of scope for this seat); no selftest or gate was executed, and no production file was edited.
- Not verified: the entry's line budget and final row count; whether L1 wants three FAO rows or one row with a multi-section anchor (I recommend three, because each carries a different teaching and Gate quote).
- Open question for the C author: whether to run the "cattle are money" row separately from the cattle-complex row. I recommend keeping both only if the entry also carries the bridewealth/currency design rule; otherwise merge into the cattle-complex row.
- Installations: none needed; no tool was installed or updated.
