# ScribeSec11Decision — Claim C, §11 of pastoralism-animal-husbandry.md

Scope: draft §11 (decision table + build order + error patterns) for the not-yet-landed entry `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`. Base 4ad2683. The entry file does not exist yet (verified: `read` returned not-found; no `pastoral|herd|husband` filename under `culture-material/`). §11 numbering assumes entry §§1–10 precede it.

## Section text (for integrator)

```markdown
## 11. Decision table and build order for a fictional pastoral culture

Build top to bottom: each row's decision is an input the next row cannot be written without. Layout model: `corpus/knowledge/culture-material/hunting-foraging-subsistence.md:137-146` (§9 decision table) and `:148-157` (§10 build order). Codes per `corpus/knowledge/verification/calibration-registry.md:35-39`.

| # | Build step | Decide before moving on | Anchor and calibration |
|---|---|---|---|
| 1 | Ecology | rainfall, forage patchiness, livestock share of household income | [SRC: https://www.fao.org/4/y2647e/y2647e02.htm \| "the economic importance of livestock within total household income rises as rainfall declines, and in desert regions dependence is near total."] — B (desert scope); dung-as-fuel trade-off `corpus/knowledge/culture-material/fire-fuel-light.md:37` |
| 2 | Species | 2–4 species and their shares; one herd or a portfolio | [SRC: https://www.fao.org/4/y2647e/y2647e02.htm \| "herders seem to manage between two and four species of roughly equal importance simultaneously."] — B; any named case `(to-verify)` |
| 3 | Mobility | nomadic / transhumant / agropastoral / enclosed; herd-splitting rule | [SRC: https://www.fao.org/4/y2647e/y2647e02.htm \| "Any classification of this type must be treated as a simplification"] — H; herd splitting [SRC: https://www.fao.org/4/y2647e/y2647e02.htm \| "A characteristic feature of transhumance is herd splitting"] — B; agropastoral row `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md:62` |
| 4 | Tenure | who grazes, waters and crosses where; fixed or fluid claims | [SRC: https://www.fao.org/4/y2647e/y2647e08.htm \| "Tenure is thus divided by both ecology and the potential for agriculture."] — B. Universal commons-tragedy premise — R. [SRC: https://vtechworks.lib.vt.edu/items/da4238e1-8a2f-49d5-bcaf-8259e0cc0b3b \| "he sees the recognition of customary land tenure as essential for the continuation of pastoralism"] — B (abstract only) |
| 5 | Wealth | herd ceiling set by labour, disease and inheritance; loan and exchange networks | [SRC: https://www.fao.org/4/y2647e/y2647e08.htm \| "the strong relationship between wealth in livestock and labour"] — B. Herd-maximisation as shock buffer: [SRC: https://www.fao.org/4/y2647e/y2647e05.htm \| "the more the animals, the greater the shock."] — B; fails where pasture limits herd size |
| 6 | Lexicon | herd-age, colour, condition and gift terms generated from rows 2–5 | `corpus/knowledge/linguistics/semantic-fields-lexicon-building.md:70` (pastoral wealth vocabulary indexes property) — H; steppe bundle `:104-105` |
| 7 | Ritual | each taboo written with its rite, as a pair | `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:69` "An animal taboo implies a rite; write both or neither" — H; pastoral-specific rite `(to-verify)` — T |

| Error pattern | Why it fails | Anchor and calibration |
|---|---|---|
| Pastoralism as the stage between foraging and farming | [SRC: https://www.fao.org/4/y2647e/y2647e02.htm \| "In most parts of the world, Africa excepted, agriculture seems to have started earlier than pastoralism."] | C; do not equate pastoralism with absent farming, `corpus/knowledge/civilizations/scythian-saka.md:70` |
| Frozen "traditional" herder | veterinary services changed herd size and routes: [SRC: https://www.fao.org/4/y2647e/y2647e05.htm \| "essentially sabotages the notion of a \"traditional\" pastoralist"] | R as a static type; pastoral is not isolation, `corpus/knowledge/civilizations/turkic-steppe.md:148` |
| Doom framing ("last nomads") | [SRC: https://www.fao.org/4/y2647e/y2647e02.htm \| "nomads – surprisingly – seem to outlast these forebodings."] | R as forecast; mobile pastoralism coexists with other production, `corpus/knowledge/civilizations/mongol.md:40` |
```

## Source list (all opened 2026-10-21)

1. **FAO, International Year of Rangelands and Pastoralists 2026 — About** — https://www.fao.org/rangelands-pastoralists-2026/about/en — section "What are Rangelands and who are Pastoralists?": "Pastoralists are people whose livelihoods mainly rely on domesticated and semi-domesticated animals that graze and browse predominantly on rangelands with varying degrees of mobility." (24 words). Scope: UN-designated lead agency's working definition only. Suggested tier **A** (definition, scope-limited); B for all other text on the page. Recheck: annually; page metadata shows last-modified 2026-07-29.
2. **FAO 2001, *Pastoralism in the new millennium*, FAO Animal Production and Health Paper 150, chapter "Introduction: pastoral systems worldwide"** — https://www.fao.org/4/y2647e/y2647e02.htm. Quotes, each verbatim: (a) Overview, para 4: "pastoral society is, above all, driven by the nature and requirements of different species." (b) "Classifying pastoral systems": "the economic importance of livestock within total household income rises as rainfall declines, and in desert regions dependence is near total." (c) "Pastoral enterprises › Nomadism": "Pastoralists usually only diverge from their existing patterns in the face of drought, pasture failure or the spread of an epizootic." (d) "Pastoral species": "herders seem to manage between two and four species of roughly equal importance simultaneously." (e) "History and origins": "In most parts of the world, Africa excepted, agriculture seems to have started earlier than pastoralism." (f) "The discourse of pastoralism": "Gloomy predictions as to the catastrophic decline of pastoralism are commonplace, although nomads – surprisingly – seem to outlast these forebodings." (g) "Pastoral enterprises › Transhumance": "A characteristic feature of transhumance is herd splitting"; "Any classification of this type must be treated as a simplification" (Pastoral enterprises, lead paragraph). Suggested tier **A** for the 2001 classification/typology scope; **B** for any regional case; (e) carry as **C** (chronology, contested, one synthesis). Recheck: 2001 monograph; re-open against current FAO/IYRP material and primary ethnography before any number is used.
3. **Same FAO 2001 volume, chapter "Social and cultural institutions of pastoralism"** — https://www.fao.org/4/y2647e/y2647e08.htm. (a) "Social structures", para 3: "A key aspect of pastoral systems is the strong relationship between wealth in livestock and labour." (b) "Land tenure and the common property resources debate", para 1: "Tenure is thus divided by both ecology and the potential for agriculture." Tier A (typology scope) / B (generalised claims).
4. **Same FAO 2001 volume, chapter "Animal health"** — https://www.fao.org/4/y2647e/y2647e05.htm. (a) "Pastoralists and the health of their animals", final paragraph of that section: "when resource availability becomes the single most important factor that limits herd size, this argument breaks down: the more the animals, the greater the shock." (b) same section, para 2: "essentially sabotages the notion of a \"traditional\" pastoralist." Tier **B** (FAO argument about herd-size mechanism; not a primary datum).
5. **Fratkin, E. 1997, "Pastoralism: Governance and Development Issues," *Annual Review of Anthropology* 26:235–261** — DOI 10.1146/annurev.anthro.26.1.235 (publisher page returned HTTP 403 to my fetch). Opened the repository record with the abstract: https://vtechworks.lib.vt.edu/items/da4238e1-8a2f-49d5-bcaf-8259e0cc0b3b. Quotes from the abstract: (a) "the problem lies not with the fact that resources are held in common, but with the fact that there are no rules governing their usage." (b) "he sees the recognition of customary land tenure as essential for the continuation of pastoralism." Tier **B** (abstract, QUALITY criterion 6). Recheck: open the full text before quoting anything beyond the abstract.

**Attempted, not counted (`(to-verify)`):**
- Dyson-Hudson & Smith 1978, *American Anthropologist* 80(1) — AnthroSource page HTTP 403; UW PDF copy (`faculty.washington.edu/easmith/Dyson-Hudson&Smith1978.pdf`) returned no extractable text for pages 1–21.
- Evans-Pritchard 1940, *The Nuer* — monoskop PDF: extraction incomplete (pages 1–344). Any cattle-ritual claim is unverified.
- Khazanov 1994, *Nomads and the Outside World* — only a catalogue/library record seen; body not opened.
- Galaty & Johnson 1990, *The World of Pastoralism* — catalogue record seen in search results only; not opened.

## Corpus anchor verification (HEAD 4ad2683, grep/sed this session)

- Confirmed verbatim or in-line at the cited line: `hunting-foraging-subsistence.md:137` (§9 heading) `:146`, `:148` (§10) `:157`; `calibration-registry.md:35` (R) through `:39` (T); `QUALITY.md:9-12` (criterion 2), `:16-17` (criterion 4), `:29` (criterion 6); `semantic-fields-lexicon-building.md:70` and `:104-105`; `symbolism-synthesis-method.md:69` (quote verbatim); `fire-fuel-light.md:37`; `agrarian-field-system-lexicon.md:62`; `civilizations/scythian-saka.md:70`; `civilizations/mongol.md:40`; `civilizations/turkic-steppe.md:148`.
- **Path correction for the lane:** scythian-saka, mongol, turkic-steppe, finnic-sami and inca live under `corpus/knowledge/civilizations/`, not `culture-material/`. The section cites them at the correct paths.
- The hunting entry's `:68-71` pointer resolves to the subsistence field (`semantic-fields-lexicon-building.md:68`, `:70`).

## Findings for the integrator

- The section is 16 non-blank lines (inside the 12–20 budget). It has a 7-row build order (ecology → species → mobility → tenure → wealth → lexicon → ritual) and a 3-row error-pattern table.
- The `[SRC: URL \| quote]` placeholders map to the sources above: FAO About → new S-id; FAO 2001 ch. 02, 05, 08 → one S-id per chapter; Fratkin abstract → new S-id (tier B, abstract). The `SOURCES.md` search for pastoral/herd/transhum/nomad rows returned no matches, so none are duplicated.
- Ritual rows are weak: no opened pastoral-ritual source. All pastoral-specific ritual content is `(to-verify)` and should stay that way until Evans-Pritchard 1940 full text is read.
- Calibration coverage: every row carries a code (B, H, R, C, or T). Living-practice flag is not included in §11 and belongs in the entry's calibration bank.

## Tooling

No installs or updates. Only `read` (web and local), `web_search`, `grep`, `sed`, and `write` were used. Nothing was run in the lane repo beyond read-only inspection.

## Checks not run

No build, lint, test, or `reports/round-28/readme/sweep.py`. The entry file does not exist yet, so the sweep cannot apply to §11 alone. No `SOURCES.md` edit (integrator converts placeholders). No production file was edited.
