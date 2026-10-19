- Seat: A02 | executor | claim A | date 2026-10-19 | baseline 57c8409

# A02 — new-entry bleed and couples scan

## Result

The round-35 and round-36 corpus deltas contain ten and one new entries respectively. All eleven `couples:` fields resolve: **334 distinct file references checked; 0 unresolved and 0 ambiguous**. The bounded language scan found **0 hits** under the filed round-34 adjudicative language predicate; contextual review found no cross-domain bleed. No dangling couples were found in the scanned set. This is a scope/structure scan, not a scholarship, canon, or admission verdict (`reports/round-37/claims.json:25-30`; `reports/round-37/targets.json:50`; `PROVINCE.md:16-25`; `corpus/QUALITY.md:13-20`).

| Entry | `couples:` line / distinct refs | unresolved / ambiguous | SHA-256 prefix |
|---|---:|---:|---|
| `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md` | 8 / 22 | 0 / 0 | `23564220aa3befa4` |
| `corpus/knowledge/culture-material/bathing-and-body-hygiene.md` | 7 / 25 | 0 / 0 | `15f2ea5de5bb9406` |
| `corpus/knowledge/culture-material/fire-fuel-light.md` | 17 / 44 | 0 / 0 | `481cf1c24734c125` |
| `corpus/knowledge/culture-material/funerary-material-culture.md` | 39 / 48 | 0 / 0 | `182e568cc84fed92` |
| `corpus/knowledge/culture-material/furniture-interior-lexicon.md` | 14 / 19 | 0 / 0 | `eaa48a8988d27466` |
| `corpus/knowledge/culture-material/writing-media-surface-economy.md` | 29 / 20 | 0 / 0 | `f039e6e120ed050f` |
| `corpus/knowledge/myth-symbol/binding-speech-complex.md` | 34 / 40 | 0 / 0 | `458f614fb03ba92d` |
| `corpus/knowledge/myth-symbol/death-afterlife-eschatology.md` | 12 / 25 | 0 / 0 | `47e665c6c8b2f120` |
| `corpus/knowledge/myth-symbol/eschatology-world-end-systems.md` | 16 / 30 | 0 / 0 | `e6bc159d23e2d977` |
| `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md` | 37 / 36 | 0 / 0 | `120302e6a132b460` |
| `corpus/knowledge/culture-material/timekeeping-instruments.md` | 7 / 25 | 0 / 0 | `9805c0b854334ed3` |

Resolution tested relative to each entry, from the repo root, and by unique corpus-basename fallback. The result for each path above is from the same read-only scan; its `couples:` line is cited so the population can be rechecked. Explicit handoff mentions in those fields do not create external file targets.

## Cross-domain language

The strict language predicate was copied from the filed round-34 runner’s `LANG_TOKENS`, `LANG_ALLOW`, and `LANG_FRAME` definitions and `leg_language()` use (`reports/round-34/run-validation.py:283-308`). It produced **no affirmative frame hits** on the eleven entries. The separate PROVINCE-derived screen found no `game-dev`/game-mechanics, chousa/source-research-method, kake/web-publishing, kotoba/prompt-skill, or sibling-repository/out-of-province language. Each entry’s recipient and boundary clauses preserve lore’s ownership of world truth and canon: `agrarian-field-system-lexicon.md:164,176-179`; `bathing-and-body-hygiene.md:10,138-141`; `fire-fuel-light.md:168-173`; `funerary-material-culture.md:216-221`; `furniture-interior-lexicon.md:139-143`; `writing-media-surface-economy.md:197-201`; `binding-speech-complex.md:37,301-305`; `death-afterlife-eschatology.md:187-191`; `eschatology-world-end-systems.md:196-200`; `sacred-kingship-mythic-charter.md:198-203`; `timekeeping-instruments.md:10,136-140`.

The broader lexical candidates were contextual, not bleed:

- `canon` in `writing-media-surface-economy.md:144,175` means the copy-selection canon of a textual tradition; `timekeeping-instruments.md:87,117` uses the partition’s material-inference ladder tags. Handoff/boundary uses state that fictional-world decisions remain lore-owned (`binding-speech-complex.md:301-305`; `timekeeping-instruments.md:10,136-140`).
- Rights/property vocabulary is part of these entries’ material and funerary subject matter, not rights/attribution rulings over reference works: agrarian land/water rights (`agrarian-field-system-lexicon.md:42-44,88-90,117`); fire-property law and attributed inventions marked `to-verify` (`fire-fuel-light.md:8,20,34,82-84,147,163`); funerary rights as a historical burial-duty conflict (`funerary-material-culture.md:88-99`); paper’s traditional attribution explicitly qualified (`writing-media-surface-economy.md:150`).
- Incidental `mechanic*` candidates describe ordinary process or historical institutions, not game mechanics: household census / register mechanism (`fire-fuel-light.md:86,115`), Byzantine throne (`furniture-interior-lexicon.md:28`), audit procedure (`writing-media-surface-economy.md:31`; `death-afterlife-eschatology.md:21`), a non-mechanical causal rule (`eschatology-world-end-systems.md:13,65`), and historical *imperium* (`sacred-kingship-mythic-charter.md:192`).

## Owed

None. All eleven named entries and their `couples:` fields were available in the current tree.

## Citations

- Assignment and acceptance scope: `reports/round-37/targets.json:3-8,50`; `reports/round-37/claims.json:25-30`.
- Ownership/refusal boundary: `PROVINCE.md:9-25`; entry admission/canon-hygiene boundary: `corpus/QUALITY.md:13-20`.
- Census commands and outputs (lane root, HEAD `57c8409ba16d9f9e692297198d95e8f2ce5a1937`):
  - `git diff --name-status 4a7aede ce103bf -- corpus/knowledge` → ten added files: the six culture-material entries except timekeeping listed above, plus `binding-speech-complex.md`, `death-afterlife-eschatology.md`, `eschatology-world-end-systems.md`, and `sacred-kingship-mythic-charter.md`.
  - `git diff --name-status ce103bf 57c8409 -- corpus/knowledge` → added `corpus/knowledge/culture-material/timekeeping-instruments.md`.
  - Read-only `python3 -B` scan with `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` over those eleven paths → the per-entry line/ref counts, digests, zero unresolved/ambiguous refs, and zero round-34 language-predicate hits in the table and findings above; lexical scope-family counts: game-dev/mechanics 0, general research method 0, web publishing 0, prompt/skill craft 0, sibling/out-of-province 0. The broad rights/attribution pattern’s matches were adjudicated in context as the cited in-domain uses above.
- Individual `couples:` source lines: agrarian `:8`; bathing `:7`; fire `:17`; funerary `:39`; furniture `:14`; writing/media `:29`; binding speech `:34`; death/afterlife `:12`; world-end `:16`; sacred kingship `:37`; timekeeping `:7`.
