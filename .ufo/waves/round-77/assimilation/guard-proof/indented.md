# SOURCES — where kotodama learns

The lane's curated reading list and the standing record of its taste:
what each source teaches, how far to trust it for which scope, and when to
look again. Shape and rules: fleet contract `SOURCES-CONTRACT-v1`
(kaika, 2026-10-19). Claim admission stays in `QUALITY.md`; the research
method stays chousa's. Every row was opened in the round that wrote it —
the round lesson's `## Gate` (`lessons/round-49.md` for S001–S047, `lessons/round-50.md` for S048–S070, and from S071 onward the lesson of the round dated in the row's `opened` cell and search-log note) holds
each row's URL, access date and verbatim quote. Append-only: only
`status`, `recheck` and `used-by` change in place, each change logged
old→new in a round lesson; a correction is a new row whose `teaches`
opens `supersedes S0NN —`.

Tiers are scoped to the row's `scope`, never global. **A** — primary or
authoritative for that scope (spec, official docs, source code, original
paper, maintainer statement, the lane's own re-runnable gate output).
**B** — strong secondary (expert write-up with reproducible detail, survey,
textbook). **C** — lead only, never sole support for an admitted entry.
`community` is never A. Tier is curation, not truth. Status: `queued`
(opened, worth mining) · `mined` (cited by the paths in `used-by`) ·
`rejected` (kept with reason and flip — a rejection is evidence of taste).

Census (from the lane root): the seven commands in the contract's
`## Census` block; `python3 reports/round-49/run-validation.py` runs them.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | Glottolog 5.3, About — https://glottolog.org/about.html | docs | A | language identification, genealogy and endangerment status | About → Credits and Contributing sections, site version 5.3 | languoid catalogue merging Hammarström's top-level classification with dialect-level multitree data; AES derived from ELCat, UNESCO Atlas and Ethnologue; data curated in a public GitHub repo with numbered releases, so always cite the version used | mined | 2026-10-19 | on-release | corpus/knowledge/linguistics/naming-systems.md, corpus/knowledge/civilizations/zapotec-mixtec.md, corpus/knowledge/civilizations/moche.md |
| S002 | WALS Online, CLDF dataset — https://github.com/cldf-datasets/wals | dataset | A | structural feature counts for a conlang's typological passport | README "How to cite" (repo master); wals.info landing citation names release v2020.6, Zenodo 10.5281/zenodo.23010827 | cite both Dryer and Haspelmath eds 2013 and the DOI of the release used; CC-BY-4.0 StructureDataset; proportions shift with the sample so quote feature counts with chapter and release | mined | 2026-10-19 | on-release | corpus/knowledge/linguistics/phonetics-phonology.md, corpus/knowledge/linguistics/syntax-typology.md, corpus/knowledge/linguistics/morphological-typology.md, corpus/knowledge/linguistics/conlang-methodology.md, corpus/knowledge/linguistics/numerals-and-measures.md, corpus/knowledge/myth-symbol/number-symbolism.md, corpus/knowledge/synthesis/worked-example-mini-culture.md, corpus/knowledge/synthesis/conlang-blueprint-template.md, corpus/knowledge/verification/phonology-sanity-gate.md, corpus/knowledge/verification/naming-collision-gate.md, corpus/knowledge/civilizations/newar-nepal.md |
| S003 | PHOIBLE 2.0, dev repository — https://github.com/phoible/dev | dataset | A | phoneme inventory plausibility for a conlang | README "How to use this repository" and "Citing PHOIBLE" sections; DOI 10.5281/zenodo.2626687 | more than 3000 inventories over more than 2100 ISO 639-3 codes, one row per languoid-phoneme pair; use the latest release rather than master; cite the original donor source (e.g. UPSID) inside PHOIBLE | mined | 2026-10-19 | on-release | corpus/knowledge/linguistics/conlang-methodology.md, corpus/knowledge/verification/phonology-sanity-gate.md |
| S004 | Grambank v1.0 — https://github.com/grambank/grambank | dataset | A | grammatical feature design and family-level constraint | README "Grambank v1.0" heading and How to cite section | global structural-feature dataset in Glottobank, CC-BY-4.0 CLDF; cite Skirgård et al. (Science Advances) plus the release DOI; usable both as design space and as a bibliographic record for grammars | queued | 2026-10-19 | on-release | — |
| S005 | Passmore et al. 2023, Kinbank, PLOS ONE 18(5) e0283218 — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283218 | paper | A | kinship terminology data and coevolution claims | Abstract and article metadata, published 24 May 2023 | 210,903 kinterms from 1,229 languages in CLDF; worked null result — no evidence for coevolution of cross-cousin marriage and bifurcate-merging terminology in Bantu | queued | 2026-10-19 | 180d | — |
| S006 | DatSemShift 3.0, Database of Semantic Shifts — https://datsemshift.ru/ | dataset | A | plausible meaning-change paths for a conlang's lexical history | Home page definition and project-phases block, version 3.0 | a shift is a meaning pair linked by derivation, attested as polysemy or as change over time, plus lexical-motivation patterns; 10,642 shifts, 52,241 realisations, 2,439 languages at open | queued | 2026-10-19 | 180d | — |
| S007 | D-PLACE (2026 edition) — https://d-place.org/ | dataset | A | cultural, linguistic, environmental codings cross-referenced to societies | Root landing citation block (Chira, Hrnčíř, Forkel, Greenhill, Gray eds. 2026, dplace2.clld.org) plus About → Overview and How to cite (Kirby et al. 2016) | over 1400 societies coded from ethnographies mostly pre-1950, each description tagged with date and source; quote frequencies with edition and sample; cite Kirby et al. 2016 PLOS ONE e0158391 plus original data sources | mined | 2026-10-19 | on-release | corpus/knowledge/linguistics/kinship-terminology.md |
| S008 | Rosenfelder, The Language Construction Kit — https://zompist.com/kit.html | docs | B | conlang craft method (not linguistic evidence) | Landing page, order-of-steps paragraph; page footer "© 1996, 2012 by Mark Rosenfelder" | naturalistic conlang order — sounds, lexicon, grammar, script, translation; working backwards from a text breeds incoherence; sequels ALC, Lexipedia, Syntax Construction Kit; practitioner method, not typological evidence | mined | 2026-10-19 | 365d | corpus/knowledge/linguistics/conlang-methodology.md, corpus/knowledge/linguistics/semantic-fields-lexicon-building.md |
| S009 | CALS, Conlang Atlas of Language Structures, statistics — https://cals.info/statistics/ | community | C | census of conlanger feature choices | Statistics → Quick numbers table, accessed 2026-10-19 | 1323 conlangs and 127 natlangs on 145 features, 97.9% taken from WALS; a census of what conlangers build, never evidence of natural-language typology | queued | 2026-10-19 | 90d | — |
| S010 | Lexurgy sound change applier — https://github.com/def-gthill/lexurgy | tool | A | deterministic replay of a conlang's sound-change laws | README "Welcome to Lexurgy", master at fa50277 (2026-06-18; latest release v1.7.6), GPL-3.0 | Kotlin sound-change applier (CLI and web app) applying regular ordered rules to a word list; a deterministic replay engine for a conlang's staged sound history | queued | 2026-10-19 | on-release | — |
| S011 | Searchable Index Diachronica v10.2 — https://chridd.nfshost.com/diachronica/ | community | C | attested sound-change lookup and leads | Page sections "Search for a sound (10.2)" and "Some notes about sources and data files" | crowd-compiled attested sound changes searchable by segment; the maintainer did not write the Index and holds no source copies, so trace every change to the cited source before use | queued | 2026-10-19 | 365d | — |
  | S897 | planted indented row | paper | A | x | y | z | queued | 2026-10-27 | 90d | — |
