# E2 fragment — linguistics / typology / conlang / motif rows (half A, R49SourcesA)

ART dossier leads S001–S015 re-opened 2026-10-19. Temp ids S201–S215 in dossier
order; renumber on merge. All `opened` = 2026-10-19. Draft `watch` statuses
normalized to `queued` (contract enum: queued/mined/rejected). used-by lists are
verified against `corpus/knowledge` in this worktree (each listed path exists and
the citation context was inspected — a bare string match is not a citation).
Post-review fixes: S213 tier A→B (digital surrogate, not the authoritative
edition); S210 anchor pinned to commit; S201/S202/S207/S213 used-by trimmed to
true citations (bibliographic-record mentions don't count); S204 returned to
queued; S203 Gate quote is one contiguous 21-word span.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S201 | Glottolog 5.3, About — https://glottolog.org/about.html | docs | A | language identification, genealogy and endangerment status | About → Credits and Contributing sections, site version 5.3 | languoid catalogue merging Hammarström's top-level classification with dialect-level multitree data; AES derived from ELCat, UNESCO Atlas and Ethnologue; data curated in a public GitHub repo with numbered releases, so always cite the version used | mined | 2026-10-19 | on-release | corpus/knowledge/linguistics/naming-systems.md, corpus/knowledge/civilizations/zapotec-mixtec.md, corpus/knowledge/civilizations/moche.md |
| S202 | WALS Online, CLDF dataset — https://github.com/cldf-datasets/wals | dataset | A | structural feature counts for a conlang's typological passport | README "How to cite" (repo master); wals.info landing citation names release v2020.6, Zenodo 10.5281/zenodo.23010827 | cite both Dryer and Haspelmath eds 2013 and the DOI of the release used; CC-BY-4.0 StructureDataset; proportions shift with the sample so quote feature counts with chapter and release | mined | 2026-10-19 | on-release | corpus/knowledge/linguistics/phonetics-phonology.md, corpus/knowledge/linguistics/syntax-typology.md, corpus/knowledge/linguistics/morphological-typology.md, corpus/knowledge/linguistics/conlang-methodology.md, corpus/knowledge/linguistics/numerals-and-measures.md, corpus/knowledge/myth-symbol/number-symbolism.md, corpus/knowledge/synthesis/worked-example-mini-culture.md, corpus/knowledge/synthesis/conlang-blueprint-template.md, corpus/knowledge/verification/phonology-sanity-gate.md, corpus/knowledge/verification/naming-collision-gate.md, corpus/knowledge/civilizations/newar-nepal.md |
| S203 | PHOIBLE 2.0, dev repository — https://github.com/phoible/dev | dataset | A | phoneme inventory plausibility for a conlang | README "How to use this repository" and "Citing PHOIBLE" sections; DOI 10.5281/zenodo.2626687 | more than 3000 inventories over more than 2100 ISO 639-3 codes, one row per languoid-phoneme pair; use the latest release rather than master; cite the original donor source (e.g. UPSID) inside PHOIBLE | mined | 2026-10-19 | on-release | corpus/knowledge/linguistics/conlang-methodology.md, corpus/knowledge/verification/phonology-sanity-gate.md |
| S204 | Grambank v1.0 — https://github.com/grambank/grambank | dataset | A | grammatical feature design and family-level constraint | README "Grambank v1.0" heading and How to cite section | global structural-feature dataset in Glottobank, CC-BY-4.0 CLDF; cite Skirgård et al. (Science Advances) plus the release DOI; usable both as design space and as a bibliographic record for grammars | queued | 2026-10-19 | on-release | — |
| S205 | Passmore et al. 2023, Kinbank, PLOS ONE 18(5) e0283218 — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283218 | paper | A | kinship terminology data and coevolution claims | Abstract and article metadata, published 24 May 2023 | 210,903 kinterms from 1,229 languages in CLDF; worked null result — no evidence for coevolution of cross-cousin marriage and bifurcate-merging terminology in Bantu | queued | 2026-10-19 | 180d | — |
| S206 | DatSemShift 3.0, Database of Semantic Shifts — https://datsemshift.ru/ | dataset | A | plausible meaning-change paths for a conlang's lexical history | Home page definition and project-phases block, version 3.0 | a shift is a meaning pair linked by derivation, attested as polysemy or as change over time, plus lexical-motivation patterns; 10,642 shifts, 52,241 realisations, 2,439 languages at open | queued | 2026-10-19 | 180d | — |
| S207 | D-PLACE (2026 edition) — https://d-place.org/ | dataset | A | cultural, linguistic, environmental codings cross-referenced to societies | Root landing citation block (Chira, Hrnčíř, Forkel, Greenhill, Gray eds. 2026, dplace2.clld.org) plus About → Overview and How to cite (Kirby et al. 2016) | over 1400 societies coded from ethnographies mostly pre-1950, each description tagged with date and source; quote frequencies with edition and sample; cite Kirby et al. 2016 PLOS ONE e0158391 plus original data sources | mined | 2026-10-19 | on-release | corpus/knowledge/linguistics/kinship-terminology.md |
| S208 | Rosenfelder, The Language Construction Kit — https://zompist.com/kit.html | docs | B | conlang craft method (not linguistic evidence) | Landing page, order-of-steps paragraph; page footer "© 1996, 2012 by Mark Rosenfelder" | naturalistic conlang order — sounds, lexicon, grammar, script, translation; working backwards from a text breeds incoherence; sequels ALC, Lexipedia, Syntax Construction Kit; practitioner method, not typological evidence | mined | 2026-10-19 | 365d | corpus/knowledge/linguistics/conlang-methodology.md, corpus/knowledge/linguistics/semantic-fields-lexicon-building.md |
| S209 | CALS, Conlang Atlas of Language Structures, statistics — https://cals.info/statistics/ | community | C | census of conlanger feature choices | Statistics → Quick numbers table, accessed 2026-10-19 | 1323 conlangs and 127 natlangs on 145 features, 97.9% taken from WALS; a census of what conlangers build, never evidence of natural-language typology | queued | 2026-10-19 | 90d | — |
| S210 | Lexurgy sound change applier — https://github.com/def-gthill/lexurgy | tool | A | deterministic replay of a conlang's sound-change laws | README "Welcome to Lexurgy", master at commit fa5027711cba3cd6a3f4b6defd0d38181fa98cd4 (2026-06-18, v1.7.6), GPL-3.0 | Kotlin sound-change applier (CLI and web app) applying regular ordered rules to a word list; a deterministic replay engine for a conlang's staged sound history | queued | 2026-10-19 | on-release | — |
| S211 | Searchable Index Diachronica v10.2 — https://chridd.nfshost.com/diachronica/ | community | C | attested sound-change lookup and leads | Page sections "Search for a sound (10.2)" and "Some notes about sources and data files" | crowd-compiled attested sound changes searchable by segment; the maintainer did not write the Index and holds no source copies, so trace every change to the cited source before use | queued | 2026-10-19 | 365d | — |
| S212 | Alper, Yanuka, Giryes, Beguš 2025, ConlangCrafter (arXiv 2508.06094) — https://arxiv.org/abs/2508.06094 | paper | A | LLM conlang generation method and its evaluation | Abstract, arXiv v1, published 2025-08-08 | multi-hop LLM pipeline staging phonology, morphology, syntax, lexicon, translation; randomness injected for diversity and self-refinement for consistency, evaluated on consistency and typological diversity | queued | 2026-10-19 | 90d | — |
| S213 | Thompson, Motif-Index of Folk-Literature (rev. 1955–58), digital edition — https://www.ruthenia.ru/folklore/thompson/indexleft.htm | spec | B | motif identity and naming (check against print) | indexleft.htm title block plus 23-chapter link list; edition line states revised and enlarged ed., Indiana UP 1955–1958 | the 23 lettered chapters (A–Z without I, O, Y) online; individually maintained digitization that asks readers to report errors, so check load-bearing IDs against print — the authoritative object is the 1955–58 print TMI, this is its convenient surrogate | mined | 2026-10-19 | 365d | corpus/knowledge/myth-symbol/comparative-frameworks.md, corpus/knowledge/myth-symbol/hero-journey-variants.md, corpus/knowledge/myth-symbol/flood-traditions.md, corpus/knowledge/myth-symbol/creation-myths-taxonomy.md, corpus/knowledge/myth-symbol/pantheon-archetypes.md, corpus/knowledge/myth-symbol/myth-folktale-genres.md, corpus/knowledge/myth-symbol/motif-index-usage.md, corpus/knowledge/synthesis/source-discipline-calibration.md, corpus/knowledge/verification/myth-consistency-gate.md |
| S214 | Karsdorp, van der Meulen, Meder, van den Bosch 2015, MOMFER, Folklore 126(1) 37–52 — https://www.theomeder.nl/momfer.pdf | paper | A | measured defects of the TMI and semantic search over it | "Accessibility of the Motif-Index" section, pp. 38–40; DOI 10.1080/0015587X.2015.1006954 | the TMI's measured defects — 45,000+ motifs, chapters A–K holding 78%, 72 motifs indexed twice, male/female skew 4178 vs 3318, India over-represented and the Arab world thin — plus WordNet-expanded semantic search as remedy | queued | 2026-10-19 | 365d | — |
| S215 | Mellmann 2020, Thompson's Motif-Index as CSV (OSF 10.17605/OSF.IO/XEB67) — https://github.com/KatjaMellmann/TMI_as_CSV | dataset | B | machine-checkable motif-ID existence | README citation and purpose paragraphs, repo main, CC-BY-4.0 | CC-BY-4.0 CSV of the 1955–58 TMI built as a relational reference table, explicitly not a search tool; the basis for an executable motif-ID existence check | queued | 2026-10-19 | 365d | — |

## Gate

Per-row open evidence, all accessed 2026-10-19; quotes verbatim, ≤25 words.

- S201 — https://glottolog.org/about.html, About → Contributing: "Glottolog data is curated in a public repository at https://github.com/glottolog/glottolog." Grounds: versioned, citable catalogue.
- S202 — https://github.com/cldf-datasets/wals, README How to cite: "the derived dataset using the DOI of the particular released version you were using". Grounds: dual citation norm.
- S203 — https://github.com/phoible/dev, README Citing PHOIBLE: "make use of the most recent release in your own analyses, rather than working from the tip of the master branch." Grounds: pin releases.
- S204 — https://github.com/grambank/grambank, README Description: "Global dataset of structural linguistic features, part of Glottobank. This dataset is licensed under a CC-BY-4.0 license". Grounds: scope and licence.
- S205 — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283218, Abstract: "a new database of 210,903 kinterms from a global sample of 1,229 spoken languages". Grounds: dataset identity.
- S206 — https://datsemshift.ru/, home page: "A semantic shift is defined as a pair of meanings, A and B, that are connected to each other through a process of semantic derivation." Grounds: what a row is.
- S207 — https://d-place.org/about, Overview: "All cultural descriptions are tagged with the date to which they refer and with the ethnographic sources that provided the descriptions." Grounds: provenance tagging.
- S208 — https://zompist.com/kit.html, order-of-steps paragraph: "Working backwards (e.g. creating a text and then devising a grammar to match) will lead to an inconsistent if not incoherent work." Grounds: pipeline order.
- S209 — https://cals.info/statistics/, Quick numbers: "97.9% of all features are from WALS". Grounds: census, not evidence.
- S210 — https://github.com/def-gthill/lexurgy, README Welcome: "It allows the user to simulate historical changes in spoken languages by applying regular rules to a list of words." Grounds: what it does.
- S211 — https://chridd.nfshost.com/diachronica/, Some notes about sources and data files: "I (chridd) did not write the Index Diachronica itself." Grounds: trace to the cited source.
- S212 — https://arxiv.org/abs/2508.06094, Abstract: "a multi-hop pipeline that decomposes language design into modular stages -- phonology, morphology, syntax, lexicon generation, and translation." Grounds: staged pipeline.
- S213 — https://www.ruthenia.ru/folklore/thompson/indexleft.htm, title block: "Please write me about errors etc" (digitization solicits corrections). Grounds: check load-bearing IDs against print.
- S214 — https://www.theomeder.nl/momfer.pdf, pp. 39–40: "the index lists seventy-two motifs twice under different headwords" (accessibility section). Grounds: measured index defects.
- S215 — https://github.com/KatjaMellmann/TMI_as_CSV, README: "The main purpose of the csv file is to generate a reference table within a relational database". Grounds: ID-existence check, not search.

## Search log

Question: which open typology, conlang-craft and motif-index sources can ground this
lane's language and narrative work, and at what trust tier? Where searched: the
fifteen lead URLs in the wave-1 ART dossier (rows S001–S015), each fetched and read
directly on 2026-10-19 — no search engine involved; this is a dossier sweep, not a
query sweep. Identified 15, screened 15, included 15 rows (13 carrying content, plus
2 community-tier census rows kept deliberately at C), excluded 0, rejected 0.
Dossier claim corrections on reopening: (a) D-PLACE used-by shrank from the
dossier's listed set — ancestral-puebloan.md and persia-sasanian.md match the
substring 'd-place' only inside unrelated words, not as citations; (b) three draft
`watch` statuses normalized to `queued` per the contract enum; (c) LCK gained a
verified citing entry beyond the draft list (semantic-fields), while initial
hits for Glottolog (hopi, ottoman, costume-language-coupling-table) and Grambank
(siam-thai) proved to be bibliographic records only; (d) two critic passes then
trimmed used-by to true citations — china-qing.md and malagasy-madagascar.md cite
only wals.info refdb records, hopi.md and ottoman.md only Glottolog reference
records (Grambank→queued: siam-thai likewise cites a grambank.clld.org source
record, not the dataset), and mesoamerica-primary-sources.md links a D-PLACE
bibliographic record plus a corpus-internal mention, so it is off S207 and S213.
Stop rationale: every dossier lead in the assigned band was opened; the remaining linguistics leads (AUTOTYP, LAPSyD,
Lexibank/CLICS, SegBo, Kümmel, Blevins, Schreyer 2021) are already recorded as
unopened leads in the dossier and stay there rather than inflating this fragment.

## Paths

- Typology evidence chain — S201 → S202 → S203 → S204: name the languoid in
  Glottolog first (it fixes identity, family and the glottocode every other
  dataset keys on), then take feature proportions from WALS, then check segment
  plausibility against PHOIBLE inventories, then Grambank for grammatical design
  space beyond what WALS covers.
- Kinship and society grounding — S207 → S205: read D-PLACE codings for the
  society's stated regime first (tagged by date and source), then Kinbank for the
  actual term inventories and its worked null-result caution before asserting
  any marriage–terminology coupling.
- Lexical history design — S206 → S211 → S210: mine DatSemShift for attested
  meaning-change directions, sanity-check sound-change steps against the Index
  Diachronica's cited sources (never the index alone), then replay the whole
  staged history deterministically in Lexurgy.
- Conlang method — S208 → S209 → S212: learn the craft order from the LCK, then
  consult CALS only as a census of what other conlangers choose (community tier),
  then ConlangCrafter to see what staged LLM pipelines now automate and where
  their evaluation is still thin.
- Motif-grid grounding — S213 → S214 → S215: anchor motif identities in the
  digital TMI (tier B surrogate — verify load-bearing IDs against print), read
  MOMFER for the index's measured skews and double-entries before drawing
  distribution conclusions, and use the CSV for executable motif-ID existence
  checks.

## Leads (unopened)

None within this half — all fifteen assigned leads opened. Adjacent linguistics
leads left unopened this round (carried in the ART dossier, not mine to promote):
Schreyer 2021 Annual Review (403), ConlangCrafter ACL 2026 acceptance (snippet
only), Grambank paper counts (Skirgård et al. 2023 not opened), Kinbank v1.2
portal note, CALS GitHub/Codeberg move, Kümmel 2007, Blevins 2004, SegBo, LAPSyD,
AUTOTYP, Lexibank/CLICS current release.
