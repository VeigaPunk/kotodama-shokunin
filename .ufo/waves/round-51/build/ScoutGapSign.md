# ScoutGapSign — Claim C premise: sign-language gap sweep, corpus enumeration, ownership verdict

**Assigned item.** Re-run the three gap sweeps recorded in `reports/round-51/claims.json` under `gap_evidence_at_base`; enumerate every `corpus/knowledge` line mentioning sign language(s), signing, signer, deaf, fingerspell, manual alphabet, gesture, emblem, kinesic or homesign; decide whether any current file owns sign languages as a register; name the partial owners the C entry must cite one-way.

**Lane.** All readings taken at `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (corpus bytes equal base `bff83ba65bf9559af4d7567e81703059667a0005`; branch tip `5ab3634` adds only `reports/round-51/calibration/`, not read). No file written except this report. No tool installed.

**Method note — no language server.** `xd://lsp` is not mounted in this session (mounted devices: `ast_edit`, `debug`), and no server answers corpus Markdown prose. Every finding below is a literal-text grep match, recorded as the fallback it is — not semantic proof, and no cold-server empty result is used as evidence.

## 1. Gap sweeps re-run at base — all three legs reproduce

| leg | command (from the lane root) | result |
|---|---|---|
| 1 filenames | `find corpus/knowledge \( -iname '*sign-lang*' -o -iname '*gestur*' -o -iname '*kinesic*' -o -iname '*nonverbal*' \) \| wc -l` | **0** |
| 2 topic lines | `grep -rliP '^- topic:.*\b(gestur\|sign language\|kinesic\|nonverbal\|non-verbal\|body language\|proxemic)' corpus/knowledge \| wc -l` | **0** |
| 3 sibling lanes (read-only) | the same two sweeps over `/home/vgpnk/Projects/shokunin/*-shokunin/corpus/knowledge` (21 lane directories) | **0 files, 0 filenames** |

**Leg-2 caveat (a finding, not a failure).** Leg 2 reads only `- topic:` lines, so it is blind to files that own the material elsewhere. `corpus/knowledge/culture-material/adornment-body-codes.md` carries "Gesture and Posture" in its H1 (`:1`) and owns `## 7. Gesture and posture` (`:77`), yet its `- topic:` line (`:2`) never uses the word. The file escapes leg 2, and any future sweep of the same shape will keep missing it. So `0` on legs 1–3 is **not** evidence that no partial owner exists; section 2 is the evidence.

## 2. Enumeration over `corpus/knowledge/**/*.md`

Assigned pattern: `grep -rniP '\b(sign language|sign languages|signing|signer|deaf|fingerspell\w*|manual alphabet|gesture\w*|emblem\w*|kinesic\w*|homesign\w*|sign-language)\b'` → **277 lines, 110 files**.

Term tallies: gesture **59 lines / 37 files**; emblem **217 lines / 86 files**; sign language 2; deaf 2; homesign 1; signing 1; **signer 0, fingerspell\* 0, manual alphabet 0, kinesic\* 0**.

Two variants the assigned pattern misses, added and recorded as an addition: `\bsigned\b` adds `linguistics/sound-symbolism.md:14,124` ("signed languages") and `linguistics/language-shift-obsolescence-revival.md:48` ("many signed and minority languages"); the semiotic noun `\bsign systems?\b|\bsign-value\b` adds 9 lines in 8 files (2c), all of them the Barthes-style *sign* sense.

### 2a. Modality-core lines — every line bearing on signed languages or gesture-as-communication

| file | lines | what that file owns / sense of the hit |
|---|---|---|
| `linguistics/phonetics-phonology.md` | 201,202 | **§7 owns the modality bullet**: whistled speech (:197), drum language (:199) and sign-language phonology (:201-203: handshape/location/movement carry contrast, Sandler & Lillo-Martin 2006; "deaf cultures need this layer") |
| `linguistics/syntax-typology.md` | 99 | §5 calibration owns the contested SOV-default remark that leans on emerging sign languages and homesign (Nicaraguan Sign Language) |
| `linguistics/linguistic-anthropology.md` | 7,147 | owns speech-event/costume coupling; gesture appears at :7 (couples) and :147 (registers license dress and gesture) |
| `linguistics/numerals-and-measures.md` | 107 | §5 owns counting technologies: finger counting as a culturally patterned body code (:107), body tallies, tally marks, knotted-cord records |
| `linguistics/sound-symbolism.md` | 14,29,124 | §7 hook table owns the **signed channels** row (:124, iconicity stronger in signed languages, Perniss et al. 2010 to-verify); :14 is the Perniss bibliography line; :29 'mouth gesture' is articulation, not manual |
| `linguistics/language-shift-obsolescence-revival.md` | 48 | owns the vitality/documentation machinery (GIDS/UNESCO/EGIDS); :48 counts "many signed and minority languages" as badly documented, with no modality content |
| `myth-symbol/flood-traditions.md` | 97 | Comparative anatomy of flood myths as *charters, not hydrology* |
| `myth-symbol/direction-symbolism.md` | 6,36 | the direction/spatial register named in symbolism-synthesis-method.md §1 as one of the five canonical symbol registers ( |
| `culture-material/dress-through-eras.md` | 105 | how real costume systems organize the three things a scene can show |
| `culture-material/architecture-settlement-lexicon.md` | 38,40,50,54,141 | built-environment vocabulary across real cultures |
| `culture-material/material-culture-inference-method.md` | 3,7,53,96 | the inference method for this category |
| `culture-material/adornment-body-codes.md` | 1,4,77,79,92,93 | **§7 owns gesture and posture as body code** (:77-93: Ekman & Friesen emblems/illustrators/regulators, Morris et al. emblem geography, Hall proxemics, honorific posture gradients, failure modes, calibration); :4 is the Morris/Ekman source line |
| `culture-material/furniture-interior-lexicon.md` | 53,113 | furniture and the interior as a cultural system for fictional cultures |
| `synthesis/multi-culture-creole-workshop.md` | 24,143 | designing a possible trade-port trajectory from intermittent contact through stabilized contact speech to an expanded co |
| `synthesis/deity-name-derivation-pipeline.md` | 167 | Derive era-specific divine naming systems by coupling linguistic history, cult address, myth, symbols, and material disp |
| `synthesis/religion-language-co-evolution.md` | 114,159,171 | How ritual authority preserves, translates, restricts, and reforms language; coupling liturgical fossilization, prayer l |
| `synthesis/taboo-euphemism-lifecycle.md` | 90,93,186 | In-world taboo drift across eras: competing euphemisms, minced forms, fossilized replacements, and the limits of using t |
| `synthesis/symbol-lexicon-colexification.md` | 35,41,91,141,143 | designing shared symbol-to-word mappings and colexification networks; reading polysemy as situated worldview evidence ra |
| `civilizations/java-majapahit.md` | 112 | Javanese linguistic-cultural coupling, anchored in Majapahit-era East Java but explicitly separating medieval evidence f — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/persia-achaemenid.md` | 134 | Achaemenid Persia, approximately 550–330 BCE: Old Persian cuneiform; Elamite/Babylonian monumental trilingualism; contes — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/greece-classical.md` | 120 | A Classical Greek reference base for coupling language, myth, symbol, era, naming, and costume; distinguish literary con — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/aegean-minoan-mycenaean.md` | 114,117 | Bronze Age Crete and mainland Greece as a coupled reference for language, administrative writing, cult, visual motifs, p — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/byzantium.md` | 75,95,178 | Byzantine coupling of Medieval Greek registers, Orthodox sacred narrative and icon theology, imperial signs and regalia, — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/australia-aboriginal.md` | 58 | Ethics-calibrated reference for coupling language, ancestral law, geography, symbol, historical change and dress; locall — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/finnic-sami.md` | 85 | Finnic/Sámi reference base; Uralic inheritance versus substrate, joik as a situated register, noaidi drum interpretation — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/germanic-norse.md` | 154 | Germanic/Norse reference base for coupling language, myth, symbol, era, and costume; methods and historical comparisons, — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/anatolia-hittite.md` | 79,81,124,126,162,163 | Hittite and Luwian cultural-linguistic coupling in Bronze Age Anatolia, with separately staged Iron Age continuities; re — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/israel-ancient-hebrew.md` | 109,117,148,153,154 | Ancient Israel and Judah as a reference base for coupling Hebrew language and writing, divine-name restrictions, covenan — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/rome.md` | 43,112 | Roman reference base for coupling Latin registers and latinitas, interpretatio romana, imperial cult, civic dress, aureu — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/egypt-ancient.md` | 94,103,147,184 | Egyptian reference base for coupling an Afro-Asiatic language and changing scripts with local creation theologies, ma'at — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/india-vedic.md` | 74,135,175 | Vedic reference base for coupling Sanskrit phonetic science (śikṣā), efficacious speech, Ṛgvedic divine relations, conse — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/maori.md` | 123 | Māori linguistic-cultural coupling in Aotearoa: te reo registers and tangata whenua protocols; whakapapa as a relational — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/thrace-dacia.md` | 111,126,127,149,158,171 | Evidence-calibrated Thracian/Getic/Dacian reference base; coupling language, religious authority, funerary feasting, ani — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/siam-thai.md` | 93,114,129,135 | Central Thai/Siamese language–myth–symbol–era–costume coupling; Ramakien indigenization, khon masked performance, rachas — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/igbo.md` | 81 | Igbo linguistic-cultural coupling: tonality and dialect continua; chi and situated cosmologies; Odinani ritual registers — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/india-mughal.md` | 160,181 | A Mughal reference base for coupling language contact, mythic legitimacy, symbols, dated ateliers, and dress hierarchy;  — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/hawaii.md` | 59,130,154 | Hawaiian coupling of ʻōlelo Hawaiʻi, kapu/noa, chiefly featherwork, hula/ mele transmission, and inoa; historical refere — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/khmer-angkor.md` | 34 | Khmer/Angkor reference base coupling Old Khmer inscriptions, Sanskrit–Khmer bilingualism and actual digraphia, devarāja  — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/japan-edo.md` | 122 | Edo/Tokugawa Japan as a coupled reference system: status and dress regulation, chōnin vocabulary, sharebon dialogue and  — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |
| `civilizations/amazonia-tupi-guarani.md` | 81,102,173 | Coupling coastal Tupinambá registers, Guarani Jesuit redução bilingualism, pajé/ritual speech, manioc technology, forest — culture file; its gesture mention is scene-level evidence (ritual, performance, dress or etiquette), never a sign-language claim |

Outside this table, every remaining gesture hit is a culture file's scene-level evidence (ritual, performance, dress, etiquette), and every remaining emblem hit is the political/heraldic/motif sense.

### 2b. `emblem` lines — 217 lines, 86 files, all in the political / heraldic / motif sense

Ownership notes below are each file's own first clause of its `- topic:` head, truncated.

| file | lines | what that file owns (from its head) |
|---|---|---|
| `linguistics/semantics-pragmatics.md` | 7 | how languages package meaning (semantic fields, polysemy, classifiers) and act through it (evidentials, implicature, speech acts, deixis) |
| `linguistics/color-terminology.md` | 116 | how basic color term systems arise and evolve (Berlin & Kay stages and their critiques), how cultures weight color categories (Japanese ao/midori, Chi |
| `linguistics/language-contact.md` | 117 | how languages converge |
| `linguistics/orality-formulaic-language.md` | 28 | Oral tradition linguistics |
| `linguistics/language-shift-obsolescence-revival.md` | 143 | The life-cycle side of language contact |
| `linguistics/sacred-registers-liturgical-language.md` | 18,128,151 | The linguistics of a register system whose high variety is reserved for the sacred: the sacred specialization of diglossia (H allocated to ritual even |
| `myth-symbol/symbolism-synthesis-method.md` | 71,108,113 | the core generation method for this category |
| `myth-symbol/celestial-symbolism-calendars.md` | 94 | The naked-eye sky as the worldbuilder's highest-yield symbolic system |
| `myth-symbol/myth-ritual-theories.md` | 19,46,49,87,98,104 | The classical theories of where myths come from and what they do |
| `myth-symbol/color-symbolism.md` | 75,111,148 | what colors MEAN across real cultures and eras (valence, carrier, institution) |
| `myth-symbol/mineral-stone-symbolism.md` | 27 | the lithic register of a fictional culture's symbolic grammar |
| `myth-symbol/animal-symbolism.md` | 41,55,86 | fauna as the densest symbolic substrate for a fictional culture |
| `myth-symbol/plant-symbolism.md` | 42,99,147,189 | the flora register of a fictional culture's symbolic grammar |
| `culture-material/architecture-settlement-lexicon.md` | 38,54 | built-environment vocabulary across real cultures |
| `culture-material/material-culture-inference-method.md` | 3,53,96 | the inference method for this category |
| `culture-material/adornment-body-codes.md` | 79,92 | the inscribed body as a legible system for fictional cultures |
| `culture-material/fire-fuel-light.md` | 16 | fire as the material system a culture is organized around |
| `synthesis/coupling-model.md` | 24,67,105 | the lane's master method for deriving mutually constrained cultural systems, tracking their different rates of change, and handing non-canonical desig |
| `synthesis/worldbible-integration-contract.md` | 80 | The shared adjacency interface by which kotodama-shokunin hands linguistic-cultural systems to lore-shokunin without claiming, recording, or silently  |
| `synthesis/dialect-faction-map-workflow.md` | 133,185 | Map dialect features and situational registers onto travel networks, factions, hereditary strata, and eras without making political borders into lingu |
| `synthesis/symbolism-consistency-rules.md` | 42,74,76,142,184,193 | assigning one primary domain per scoped symbol; licensing secondary readings, regional variants, era drift, and compounds; auditing the resulting meth |
| `synthesis/era-myth-language-costume-matrix.md` | 92 | A reusable era-by-system worksheet: separate political periodization from changes in cult, speech, writing, naming, dress, signs, and timekeeping; rec |
| `synthesis/consistency-verification-checklist.md` | 114,136,157 | a reference-only preflight for the coupling of language, myth, symbol, era, costume, and material practice; every audit item names the corpus decision |
| `synthesis/costume-language-coupling-table.md` | 104 | A decision table for deriving compatible dress, vocabulary, status, ritual, and period choices; historical reference rows, a deliberately non-canon wo |
| `synthesis/naming-canon-workflow.md` | 50,63,70,75 | An auditable pipeline for proposing names for persons, places, gods, individual items, and ships; couples linguistic derivation to cultural use withou |
| `synthesis/worked-example-mini-culture.md` | 52,197 | A single synthetic teaching fixture coupling a language sketch, pantheon, symbolic grammar, periodization, costume system, twenty-word etymological le |
| `synthesis/multi-culture-creole-workshop.md` | 143 | designing a possible trade-port trajectory from intermittent contact through stabilized contact speech to an expanded community vernacular, coupled to |
| `synthesis/source-discipline-calibration.md` | 117,146,169,172 | Corpus-specific controls for coupling language, myth, symbol, era, costume, and names without laundering a design framework into historical evidence o |
| `synthesis/era-language-staging.md` | 103,137 | Staging one constructed language across fictional eras through ordered sound changes, stratified registers, diglossic domain shifts, regnal naming, pe |
| `synthesis/loanword-material-dating.md` | 34,103,152,174,210 | Infer relative sequences and bounded dates for fictional contact, borrowing, adoption, and deposition by coupling linguistic, material, and naming evi |
| `synthesis/migration-founder-effects.md` | 106,135,147,174 | founder populations and language |
| `synthesis/myth-to-language-derivation.md` | 62 | Operationalizing the kotodama coupling: derive locally motivated phonestheme sets, sacred vocabulary, divine appellations, and name-taboo effects thro |
| `synthesis/religion-language-co-evolution.md` | 171 | How ritual authority preserves, translates, restricts, and reforms language; coupling liturgical fossilization, prayer languages, schism linguistics,  |
| `synthesis/taboo-euphemism-lifecycle.md` | 90,93,186 | In-world taboo drift across eras: competing euphemisms, minced forms, fossilized replacements, and the limits of using their distribution to date fict |
| `synthesis/symbol-lexicon-colexification.md` | 41,91,143 | designing shared symbol-to-word mappings and colexification networks; reading polysemy as situated worldview evidence rather than proof of a culture's |
| `synthesis/conlang-blueprint-template.md` | 24,165 | reusable fill-in specification: phoneme inventory → phonotactics → morphology → syntax → 300-word core lexicon → pragmatics; acceptance gates couple l |
| `verification/citation-format-and-source-registry.md` | 177 | A lane-local citation profile connecting each linguistic-cultural claim to its exact source version, supported scope, mediations, and design transform |
| `verification/lexicon-coverage-audit.md` | 49,151 | a reproducible manual gate for semantic-field coverage against the seven field briefs, derivational consistency, frequency discipline, and coherent lo |
| `verification/phonology-sanity-gate.md` | 239 | An executable, bounded verification specification for fictional spoken-language profiles; distinguish contradictions from typological rarity and keep  |
| `verification/naming-collision-gate.md` | 52,135 | A pre-handoff gate for name uniqueness across a supplied canon snapshot, phonotactic pronounceability, derivational validity, and bounded cross-cultur |
| `verification/internal-consistency-audit.md` | 67,73 | audit the cross-file coherence of linguistic-cultural design methods and candidate handoff packets; expose missing couplings, misaligned terms, incomp |
| `verification/real-world-inspiration-boundaries.md` | 52,56,76,84,89,156 | Screening linguistic-cultural worldbuilding references for extractive copying, restricted or sacred material, misleading authenticity claims, and cons |
| `verification/myth-consistency-gate.md` | 103,108,130,131,148,164 | A source-calibrated review gate for coupling a fictional culture's divine roles, narrative motifs, historical layers, linguistic forms, and worn symbo |
| `verification/calibration-registry.md` | 116,162,165 | Master claim-level calibration registry for the linguistic-cultural corpus: Campbell universalism, fixed-rate glottochronology, strong Whorfian determ |
| `civilizations/mesopotamia-sumer-akkad.md` | 66,132 | Southern Mesopotamian language, writing, myth, kingship, symbols, historical eras, names, and dress as coupled reference systems; methods for fictiona |
| `civilizations/aegean-minoan-mycenaean.md` | 114 | Bronze Age Crete and mainland Greece as a coupled reference for language, administrative writing, cult, visual motifs, periodization, dress, and archi |
| `civilizations/olmec.md` | 123,140 | Gulf Coast Olmec reference base; were-jaguar interpretation, later Epi-Olmec writing, ruler portraiture, and criticism of the mother-culture model; me |
| `civilizations/china-han.md` | 94,162 | Han China as a coupled linguistic-cultural reference: Qin standardization's afterlife, Dong Zhongshu and correlative cosmology, hemp/silk registers, a |
| `civilizations/byzantium.md` | 95 | Byzantine coupling of Medieval Greek registers, Orthodox sacred narrative and icon theology, imperial signs and regalia, changing Theme administration |
| `civilizations/rapa-nui.md` | 136,184,186 | Rapa Nui linguistic-cultural reference: undeciphered rongorongo, moai symbolism, tangata manu/Birdman rites, and language change under relative isolat |
| `civilizations/levant-canaan-phoenician.md` | 88,96,100,165 | Canaanite/Phoenician reference base for coupling Northwest Semitic language and alphabetic transmission with local pantheons, Melqart's maritime cult  |
| `civilizations/china-tang.md` | 129,171 | Tang China (618–907): coupling language and writing, Buddhist translation, examination register, regulated verse, plural sacred authority, symbolic di |
| `civilizations/islamic-caliphate-arabic.md` | 133 | Arabic's preserved scriptural norm and changing vernaculars coupled to waqf vocabulary, sacred calligraphy, contextual aniconism, madrasa learning, dy |
| `civilizations/anatolia-hittite.md` | 79,81,124,162,163 | Hittite and Luwian cultural-linguistic coupling in Bronze Age Anatolia, with separately staged Iron Age continuities; reference and generative method, |
| `civilizations/israel-ancient-hebrew.md` | 148,153,154 | Ancient Israel and Judah as a reference base for coupling Hebrew language and writing, divine-name restrictions, covenantal memory, symbolic objects,  |
| `civilizations/carthage.md` | 119 | Carthaginian reference base for coupling a Phoenician daughter language, votive religion, public symbols, maritime commerce, material display, and pos |
| `civilizations/dine-navajo.md` | 75,175 | Diné linguistic-cultural coupling: Southern Athabaskan tone and register; hózhǫ́; sandpainting as situated ritual technology; weaving, dress, and kins |
| `civilizations/egypt-ancient.md` | 94,103,147,184 | Egyptian reference base for coupling an Afro-Asiatic language and changing scripts with local creation theologies, ma'at, regnal time, material displa |
| `civilizations/mamluk.md` | 8,9,15,125,126,188 | coupling military enslavement and emancipation, Kipchak–Circassian–Turkic–Arabic language strata, furūsiyya literature, office/household blazons, nami |
| `civilizations/thrace-dacia.md` | 126,127,149,171 | Evidence-calibrated Thracian/Getic/Dacian reference base; coupling language, religious authority, funerary feasting, animal standards, period, and dre |
| `civilizations/japan-medieval-sengoku.md` | 115 | A historical reference base for coupling Japanese language, kami–Buddhist traditions, warrior display, settlement naming, and the sixteenth-century Ki |
| `civilizations/siam-thai.md` | 93 | Central Thai/Siamese language–myth–symbol–era–costume coupling; Ramakien indigenization, khon masked performance, rachasap, and sakdina; reference and |
| `civilizations/mongol.md` | 118,119 | Mongol linguistic-cultural coupling: Uyghur-derived writing, the Secret History's registers, Heaven/earth and shamanic vocabulary, deel dress codes, n |
| `civilizations/moche.md` | 86,122 | coupling language, mythic imagery, regional eras, elite costume, and ritual landscape in the Moche societies of Peru's north coast; reference knowledg |
| `civilizations/korea-joseon.md` | 113,116,117 | Joseon linguistic-cultural reference base: han'gŭl/hangul and hanja–hanmun differentiation, Confucian ritual registers, gat/yangban dress, and gwageo  |
| `civilizations/benin.md` | 40,78 | The Edo-speaking Kingdom of Benin as a reference for coupling linguistic registers, royal cosmology, authorized craft, coral regalia, and historical c |
| `civilizations/hawaii.md` | 59 | Hawaiian coupling of ʻōlelo Hawaiʻi, kapu/noa, chiefly featherwork, hula/ mele transmission, and inoa; historical reference and fictional-system metho |
| `civilizations/chimu.md` | 103 | Chimú reference base—Muchik language loss, Chan Chan ciudadela vocabulary, Spondylus exchange symbolism, and the Chimú–Inca conquest layer; generative |
| `civilizations/parthia.md` | 59 | Parthian reference methods for coupling language, myth, symbol, era, and costume; mixed-script coinage, Ecbatana's exchange network, mounted warfare,  |
| `civilizations/ottoman.md` | 91 | Ottoman reference base: Turkic–Arabic–Persian linguistic layering, script plurality, kanun/şeriat registers, Tulip-era costume codes, divan poetry, an |
| `civilizations/maya-classic.md` | 63 | Classic Maya linguistic-cultural coupling: logosyllabic decipherment and the Knorozov/Ventris comparison; Long Count mathematics; the later K’iche’ Po |
| `civilizations/haudenosaunee.md` | 53 | Coupling Iroquoian language, wampum documentation, matrilineal naming, public cosmology, historical dress, and the boundaries around False Face medici |
| `civilizations/lakota-plains.md` | 159 | Lakota-centered language–myth–symbol–era–costume coupling; Siouan comparison, wakȟáŋ discourse, Sun Dance structure, ledger drawings, and winter-count |
| `civilizations/turkic-steppe.md` | 94,99,102,188 | Turkic steppe reference base coupling Old Turkic language and inscriptions, heavenly favor, Ashina ancestry narratives, imperial titles, portable dwel |
| `civilizations/mexica-aztec.md` | 158,174 | A central-Mexican reference base coupling Nahuatl reverentials, Huitzilopochtli migration traditions, calpulli organization, eagle/jaguar warrior iden |
| `civilizations/yoruba.md` | 39,90,93 | Yoruba reference base for coupling language, òrìṣà, praise, divination, historical change, and costume; methods and comparative knowledge only, never  |
| `civilizations/amazonia-tupi-guarani.md` | 102 | Coupling coastal Tupinambá registers, Guarani Jesuit redução bilingualism, pajé/ritual speech, manioc technology, forest nomenclature, periodization,  |
| `civilizations/mississippian.md` | 54,158 | Cahokia-centered Mississippian reference base: political vocabulary and the limits of a “Big Other” cosmology lens; Southeastern Ceremonial Complex ic |
| `civilizations/persia-sasanian.md` | 129 | Sasanian linguistic-cultural coupling, principally 224–651 CE: Middle Persian registers and scripts, the Zurvanism debate, fire-sanctuary cosmology, t |
| `civilizations/burma.md` | 91,115,170 | Burmese/Bamar reference base: script roundness, nat–Buddhist relations, Pali–Burmese prestige, longyi dress codes, and palace nomenclature; method and |
| `civilizations/newar-nepal.md` | 82,90 | Newar linguistic-cultural coupling in the Kathmandu Valley: Nepal Bhasa, respect registers, scripts, Hindu and Buddhist ritual worlds, guthi associati |
| `civilizations/austronesia-philippines-taiwan.md` | 57 | Formosan diversity and homeland inference; Philippine writing and ritual specialists; Ifugao landscape vocabulary; hibiscus, buri, and ramie material  |
| `civilizations/tibet.md` | 95 | Tibetan linguistic-cultural coupling: script-creation traditions and historical evidence; Bön/Buddhist vocabulary strata; prayer-wheel mantra economie |
| `civilizations/akan.md` | 87,88 | Akan linguistic-cultural coupling, especially Asante Twi tone, adinkra, kente, stool regalia, and kra/day naming; reference and generative method, not |
| `civilizations/fon-dahomey.md` | 1,28,118,121,132,134,136,142,148,165,180,187 | Fon/Dahomey as a reference base for coupling tonal language, vodun, ancestral obligation, migration traditions, royal registers, historical eras, and  |
| `civilizations/zimbabwe-shona.md` | 7,78,84,85,87,89,93,105,106,137,147,164,177 | Coupling Shona tonal language, dzimbahwe stone symbolism, ancestral music, mutupo relationships, historical eras, and material display without manufac |

Two of these 217 use "emblem" in the **gesture** sense and belong to 2a: `culture-material/adornment-body-codes.md:79` (Ekman & Friesen's *emblems* = culture-specific gestures with dictionary meanings, called "the conlang-adjacent category") and `:4` (the Morris et al. *Gestures* source line).

### 2c. The semiotic-`sign` family — a naming-collision hazard

9 lines / 8 files: `culture-material/costume-semiotics.md:1,2` (an entire entry titled "Dress as Sign System"), `civilizations/java-majapahit.md:112`, `civilizations/anatolia-hittite.md:75` (hieroglyph sign systems), `civilizations/slavs-early.md:148`, `civilizations/egypt-ancient.md:94` (sign-value), `civilizations/siam-thai.md:131`, `civilizations/igbo.md:145`, `verification/real-world-inspiration-boundaries.md:100`. None owns manual communication, but `costume-semiotics.md` owns the phrase "sign system" for dress — C should not reuse that phrase for a signed language without naming the collision (cf. `verification/naming-collision-gate.md`).

### 2d. Adjacent alternate-channel lines (no assigned term matched; owned elsewhere, on the record so C's "alternate" scope has its neighbours)

| file | lines | what that file owns |
|---|---|---|
| `linguistics/phonetics-phonology.md` | 197,198,199,200,309,310 | whistled speech (Silbo Gomero, Kuşköy, Chinantec; Meyer 2008) and drum language as environment→inventory couplings; :309-310 carry the live source receipts |
| `linguistics/orality-formulaic-language.md` | 24,114 | media extensions: talking drums and whistled registers as a "broadcast layer" for oral formulas |
| `culture-material/music-instrument-lexicon.md` | 98,100 | the talking drum as a language phenomenon on a musical instrument ("this lane's centerpiece coupling") |
| `linguistics/writing-systems.md` | 21,36 | semasiography (Blissymbolics, traffic signs) and quipu as recording technology with no demonstrated phonetic encoding |
| `linguistics/numerals-and-measures.md` | 110 | knotted-cord and rod records as counting technologies |
| `civilizations/inca.md` | 43,45,48,61,64 | khipu as a record system, with the in-corpus calibration of narrative readings |
| `civilizations/fon-dahomey.md` | 35,181,182 | drum-language literature bounds (Finnegan; Durojaye et al. on the dùndún) |
| `civilizations/yoruba.md` | 21 | dùndún talking-drum speech-surrogacy study, directly consulted |

## 3. Verdict

**No current owner of sign languages as a register.** No filename (leg 1), no `- topic:` line (leg 2), no H1 and no `- couples:` head in the corpus claims sign languages or manual communication as a register. Two closing receipts: `grep -rniP '^#{1,3} .*\\b(sign language|sign languages|signed language|deaf|fingerspell|manual alphabet|manual modality|kinesic|homesign)\\b' corpus/knowledge --include='*.md' | wc -l` → **0**; the same sweep restricted to `^- (owns|couples|scope|gap filled):` head lines → **0** (note: this corpus uses `- topic:`, not `- owns:` — `grep -rl '^- owns:'` finds 0 files, so the head-ownership check is the topic sweep plus these two). The entire in-corpus trace is five scattered lines in four files (2a). The corpus contains **zero** lines for signer, fingerspelling, manual alphabet, kinesic, sign notation, village or shared sign, Plains Indian Sign Language, Martha's Vineyard, tactile sign, or deaf education. The C register is genuinely unowned at base, so the coverage claim's premise holds. Confidence: **high** — the enumeration is exhaustive over the assigned term set plus the two added variants, and the negative is a head-field and filename check, not a server absence.

**Partial owners C must cite one-way** (cite the anchor, then do not re-cover its material):

1. `linguistics/phonetics-phonology.md:201-203` — §7 owns the corpus's one modality bullet (sign-language phonology works without acoustics; handshape/location/movement carry contrast, Sandler & Lillo-Martin 2006; "deaf cultures need this layer"). **Missing from claims.json's partial-owner list**; it is the strongest existing claim on sign material in the corpus.
2. `culture-material/adornment-body-codes.md:77-93` — §7 owns gesture and posture as body code (Ekman & Friesen emblems/illustrators/regulators, Morris et al. emblem geography, Hall proxemics, honorific posture gradients, failure modes, calibration). Named in claims.json.
3. `linguistics/syntax-typology.md:99` — §5 owns the contested SOV-default remark leaning on emerging sign languages and homesign (Nicaraguan Sign Language). Named in claims.json.
4. `linguistics/numerals-and-measures.md:107` — §5 owns finger counting as a culturally patterned body code. Named in claims.json.
5. `linguistics/sound-symbolism.md:14,124` — §7's hook table owns the "signed channels" row (iconicity stronger in signed languages; Perniss et al. 2010 `(to-verify)`). **Missing from claims.json's list**.
6. `linguistics/writing-systems.md:21,36` — owns semasiography (Blissymbolics, traffic signs) and quipu as recording technology without demonstrated phonetic encoding. **Missing from claims.json's list**; C's notation section must cite it.
7. `linguistics/linguistic-anthropology.md:7,147` — owns gesture as a speech-event and costume coupling; cite if C develops the event/register ecology.
8. Alternate-channel neighbours, if C covers "alternate" systems beyond the manual channel: `linguistics/phonetics-phonology.md:197-200` (whistled speech, drum language), `linguistics/orality-formulaic-language.md:114`, `culture-material/music-instrument-lexicon.md:98,100` (talking drum), `linguistics/numerals-and-measures.md:110` (knotted-cord records).

## 4. Drafted boundary rows for C (ready to paste; anchors re-read at base)


| neighbour (owner) | one-way citation for C | boundary C keeps |
|---|---|---|
| `linguistics/phonetics-phonology.md:201-203` | "the sound-system file already carries one modality bullet (sign-language phonology; deaf cultures need this layer)" | C owns the system side (community, grammar-in-modality, emergence, codes, notation); the segmental/prosodic inventory stays with phonetics-phonology |
| `culture-material/adornment-body-codes.md:77-93` | "gesture and posture as non-linguistic body code live there (emblems, illustrators, regulators, proxemics, honorific gradients)" | C owns full signed languages (phonology, morphology, community); C does not re-cover etiquette/posture gradients |
| `linguistics/syntax-typology.md:99` | "that file already flags the SOV-default claim as leaning on emerging sign languages and homesign" | C may use emergence evidence for modality questions; word-order universals stay there |
| `linguistics/numerals-and-measures.md:107` | "finger counting is owned there as a counting register and body code" | C owns fingerspelling and manual codes (letter/digit systems inside a signed language); counting gestures stay there |
| `linguistics/sound-symbolism.md:14,124` | "the iconicity-in-signed-languages hook is already a row in that file's cross-file table (Perniss et al. 2010, to-verify)" | C states the modality consequence and cites; it does not restate the iconicity programme |
| `linguistics/writing-systems.md:21,36` | "semasiography and quipu are owned there as script-typology and recording-technology boundaries" | C's notation section covers sign notation (Stokoe-style description systems) and cites this boundary instead of re-arguing 'is it writing' |
| `linguistics/linguistic-anthropology.md:7,147` | "gesture as a speech-event and costume coupling is owned there" | C owns the signed event as a linguistic event; the speech-event/costume coupling stays there |
| `culture-material/costume-semiotics.md:1-2` | "the phrase 'sign system' is that entry's title for dress" | C names its object 'manual modality' / 'signed language', never reusing 'sign system' for a signed language without flagging the collision |


## 5. Unrun checks and residual unknowns

- Did not run D's counter `python3 -B reports/round-51/boundary-count.py`, the README sweep `python3 -B reports/round-28/readme/sweep.py`, or `find corpus/knowledge -name '*.md' | wc -l` as a claim measurement. Pre-state seen incidentally while reading the index: 226 files, `## linguistics/ (25)` at `corpus/README.md:220`, totals line "Total knowledge entries: 226." at `:590`, footer `(total 226 files; directory totals 25/26/28/29/24/94)` at `:594`. `reports/round-28/readme/sweep.py` parses exactly those three lines plus the per-section header, so C's after-state must move all four (226→227, 25→26, totals line, footer).
- C's SOURCES leg is unverifiable here: `corpus/SOURCES.md` currently ends at S070 (70 rows, header `:28`); S071 upward are not yet assigned or opened, so no citation leg can be checked from this seat.
- No LSP device is mounted (see Method note): the "no owner" verdict rests on exhaustive filename, topic-line and head-field sweeps plus the full literal enumeration, not on a server or compiler.
- One reading not closed: whether another seat is drafting the C entry concurrently (the roster shows `KotodamaR51a3.ScribeSec10ContactWriting` reading sign-language material). If so, that draft is the integration target for the boundary rows above, and I did not read it.
