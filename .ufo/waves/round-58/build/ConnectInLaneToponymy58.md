# ConnectInLaneToponymy58 — claim C in-lane partial owners (round 58)

Seat: KotodamaR58A2.ConnectInLaneToponymy58 (connector, leaf). Local repository evidence only; no external source opened, no row offered.
Axes judged: **coverage** (the new entry adds ground the corpus does not already hold) and **adjacency** (one-way pointers to the real partial owners, no repeated claims presented as new).

## Evidence: grep, grouped by file

Command (run from the lane root; `rg -E` is the encoding flag, so the pattern went through `-i -e`):
`rg -n -i --sort path -e 'toponym|place[- ]?name|hydronym|exonym|endonym|odonym|gazetteer' corpus/knowledge` gave 239 hit lines in 96 files. Raw output: `/fast/scratch/hyaku/kotodama-r58/ConnectInLaneToponymy58/grep.txt`.

Hit lines that are only `sources:`/`couples:` headers or incidental mentions (no place-name teaching) are marked `(hdr)` or `(inc)`.

- `civilizations/aegean-minoan-mycenaean.md`: 170 (inc), 174, 179
- `civilizations/africa-primary-sources.md`: 64, 116
- `civilizations/ainu.md`: 95, 96, 99
- `civilizations/amazonia-tupi-guarani.md`: 156, 185, 186
- `civilizations/ancestral-puebloan.md`: 173, 174
- `civilizations/arabia-pre-islamic.md`: 67 (inc)
- `civilizations/australia-aboriginal.md`: 49, 54, 139, 140
- `civilizations/austronesia-philippines-taiwan.md`: 157 (inc), 189, 191
- `civilizations/carthage.md`: 161, 184
- `civilizations/chimu.md`: 17 (hdr), 37, 165, 166, 167, 170, 171
- `civilizations/china-ming.md`: 123
- `civilizations/etruria.md`: 160
- `civilizations/finnic-sami.md`: 28, 50, 148, 164, 169, 170, 198
- `civilizations/fon-dahomey.md`: 72 (inc)
- `civilizations/germanic-norse.md`: 45, 176
- `civilizations/hawaii.md`: 19 (hdr), 131
- `civilizations/inca.md`: 4 (hdr), 164, 165, 192 (hdr)
- `civilizations/islamic-caliphate-arabic.md`: 167
- `civilizations/japan-yayoi-kofun.md`: 71, 81, 82
- `civilizations/khmer-angkor.md`: 167, 173
- `civilizations/korea-three-kingdoms-goryeo.md`: 49, 170
- `civilizations/levant-canaan-phoenician.md`: 109, 151, 167, 177
- `civilizations/maori.md`: 72, 183
- `civilizations/maya-classic.md`: 55 (inc)
- `civilizations/mexica-aztec.md`: 158, 167
- `civilizations/mississippian.md`: 46, 155
- `civilizations/moche.md`: 151
- `civilizations/nazca.md`: 60, 65
- `civilizations/newar-nepal.md`: 181
- `civilizations/nubia-kush.md`: 161 (inc)
- `civilizations/olmec.md`: 162 (inc)
- `civilizations/pacific-northwest.md`: 184
- `civilizations/persia-achaemenid.md`: 152
- `civilizations/polynesia-navigation.md`: 164
- `civilizations/rapa-nui.md`: 57 (inc), 172, 175, 179
- `civilizations/scythian-saka.md`: 158, 160
- `civilizations/sogdian-silk-road.md`: 168 (inc)
- `civilizations/taino.md`: 28, 54, 58, 67, 137, 160, 164
- `civilizations/thrace-dacia.md`: 49, 57, 74
- `civilizations/turkic-steppe.md`: 110
- `civilizations/vietnam.md`: 108, 158
- `civilizations/zapotec-mixtec.md`: 46, 83
- `civilizations/zimbabwe-shona.md`: 172
- `culture-material/agrarian-field-system-lexicon.md`: 8 (hdr), 126
- `culture-material/architecture-settlement-lexicon.md`: 3 (hdr), 4 (hdr), 6 (hdr), 105, 145
- `culture-material/cartography-and-mapmaking.md`: 4 (hdr), 19 (hdr), 23 (hdr), 57, 159
- `culture-material/fire-fuel-light.md`: 17 (hdr)
- `culture-material/funerary-material-culture.md`: 144
- `culture-material/furniture-interior-lexicon.md`: 4 (inc), 33 (inc)
- `culture-material/garment-lexicon-crosslinguistic.md`: 5 (hdr), 41, 54, 88, 91, 108, 127, 128
- `culture-material/music-instrument-lexicon.md`: 48 (inc)
- `culture-material/textile-technology.md`: 5 (hdr), 47, 83, 97
- `culture-material/vessel-container-lexicon.md`: 5 (hdr), 52
- `linguistics/conlang-methodology.md`: 17, 50, 152
- `linguistics/historical-linguistics.md`: 227
- `linguistics/language-contact.md`: 148, 165
- `linguistics/language-shift-obsolescence-revival.md`: 30 (hdr), 177
- `linguistics/linguistic-anthropology.md`: 73
- `linguistics/naming-systems.md`: 1, 3, 12, 13, 14, 15, 16 (hdr/sources), 40, 65, 68, 69, 70, 71, 77, 80, 82, 84, 85, 97, 117, 118, 119, 120, 122, 136
- `linguistics/orality-formulaic-language.md`: 77 (inc)
- `linguistics/semantic-fields-lexicon-building.md`: 65
- `linguistics/translation-protocol-fidelity.md`: 9 (hdr)
- `myth-symbol/cosmology-cosmography.md`: 20 (hdr), 27, 133
- `myth-symbol/creation-myths-taxonomy.md`: 49 (inc)
- `myth-symbol/direction-symbolism.md`: 14 (hdr), 182 (inc)
- `myth-symbol/flood-traditions.md`: 19 (hdr)
- `myth-symbol/mineral-stone-symbolism.md`: 8 (hdr), 94
- `myth-symbol/monsters-hybrid-beings.md`: 80 (inc)
- `myth-symbol/myth-ritual-theories.md`: 48 (inc)
- `myth-symbol/plant-symbolism.md`: 6 (hdr), 59, 132
- `myth-symbol/sacred-topography-pilgrimage.md`: 7 (hdr), 9 (hdr), 98
- `myth-symbol/trickster.md`: 4 (hdr)
- `synthesis/conlang-blueprint-template.md`: 54, 56, 57, 167
- `synthesis/consistency-verification-checklist.md`: 88, 99
- `synthesis/coupling-model.md`: 94 (inc)
- `synthesis/cultural-translation-protocol.md`: 93, 105, 159
- `synthesis/deity-name-derivation-pipeline.md`: 120 (the grep misses :73, the "Local / topographic" epithet row, which says "genitive of place" and "Locative")
- `synthesis/dialect-faction-map-workflow.md`: 137, 138
- `synthesis/era-language-staging.md`: 127
- `synthesis/era-myth-language-costume-matrix.md`: 47
- `synthesis/glossary-registry-format.md`: 45, 93, 187
- `synthesis/loanword-material-dating.md`: 89, 97, 171
- `synthesis/migration-founder-effects.md`: 30, 62, 124, 178, 180, 188 (hdr), 189 (hdr)
- `synthesis/multi-culture-creole-workshop.md`: 76, 160, 164
- `synthesis/naming-canon-workflow.md`: 4 (hdr), 52, 140
- `synthesis/taboo-euphemism-lifecycle.md`: 87, 136
- `synthesis/worked-example-mini-culture.md`: 138, 142, 157
- `synthesis/worldbible-integration-contract.md`: 42, 79, 115, 198
- `verification/citation-format-and-source-registry.md`: 70
- `verification/costume-era-consistency-gate.md`: 157 (inc)
- `verification/internal-consistency-audit.md`: 93
- `verification/lexicon-coverage-audit.md`: 46, 150
- `verification/naming-collision-gate.md`: 20, 39, 116
- `verification/phonology-sanity-gate.md`: 247
- `verification/provenance-audit-ledger-format.md`: 120
- `verification/to-verify-triage-protocol.md`: 95

## (1) Claims naming-systems.md already makes about place names

I read `linguistics/naming-systems.md` in full (136 lines). Section 3 is lines 65–71 and section 5 is lines 80–85. Place-name content outside those sections is listed too, because the new entry must not present it as new either.

**§3 Toponymy: functions, strata, politics (lines 65–71)**
- N1 (:67) Functional typology (Kadmon 2000; Stewart 1945): **descriptive** (Black Forest, Table Mountain), **associative** (a town named for its river), **commemorative/eponymous** (Alexandria; MLK boulevards — Alderman 2000), **commendatory** (Greenland — Erik chose the green name to attract settlers, per Eiríks saga rauða; propaganda names Hope, Prosperity), **transfer/shift** (New York from York; New Amsterdam renamed New York on capture), **folk-etymologized**.
- N2 (:68) Place names stratify. Each conquest or migration overlays the previous language, and old morphemes fossilize as opaque heads. The English layers are Celtic, Old English, Norse and Norman (Gelling 1978; Cameron 1996).
- N3 (:68) Tautologies betray the strata: Bredon (Worcs.), attested 772 as *Breodune*, from *bre* + *dun*, meaning "hill-hill"; Breedon-on-the-Hill (Leics.) is "hill-hill hill" (Duignan 1905).
- N4 (:69) Folk etymology (Hock 1986): an opaque name is regularized to a familiar word. Lever: in-world guides explain place names wrongly and confidently.
- N5 (:70) Critical toponymy (Rose-Redwood, Alderman & Azaryahu 2010): naming inscribes power and the street grid is a city-text. Regime changes rewrite it: the St Petersburg chain, Bombay→Mumbai (1995), Salisbury→Harare, Shanghai's roads renamed wholesale after 1949. "Every renaming is datable; a map is an archive of coups."
- N6 (:71) Standardization: UNGEGN runs an endonym-first principle, meaning maps should show the name locals use (UNGEGN 2002). Pinyin (PRC 1958; endorsed by the UN for Chinese names in 1977) is the textbook case of romanization as a geopolitical act.

**§5 Endonym/exonym: the transit layer (lines 80–85)**
- N7 (:82) Definitions (UNGEGN 2002): an endonym is the insiders' name and an exonym is an established outside name. Aurousseau (1957) coined "exonym"; "endonym" was coined later.
- N8 (:83) One country, four roots: Deutschland, Germany, Allemagne, Niemcy/Saksa ("mutes", from *němъ*; the Finnish form from the Saxons). Each root is a different contact event.
- N9 (:84) Route layering: Cīna → China; Khitan → Cathay → Kitay; 日本國 → Cipangu → Japang → Japan. Marco Polo reported China and Cathay as different countries, so one endonym can arrive twice.
- N10 (:85) Craft rules: (1) exonyms are period evidence; (2) pejorative exonyms are slur fossils that can be reclaimed or shed by renaming; (3) a state renaming itself announces a regime.

**Elsewhere in naming-systems.md**
- N11 (:40) Onomastics splits into anthroponymy, toponymy, theonymy and endonym/exonym.
- N12 (:77) Cult epithets are mostly toponyms; build the toponymy first and the epithets fall out of it.
- N13 (:117–118) Pipeline steps 7–8: derive each neighbour's exonym along a route, with one pejorative root and one double arrival. Stratify the map into substrate names plus each regime's commendatory/commemorative layer, with one tautology and one folk etymology placed on purpose.
- N14 (:122) Worked example: a summit named hill-hill-hill from three dead languages.
- N15 (:129) Calibration: "Torpenhow Hill" is a ghost quadruple tautology (Mills; Francis). Verify viral tautologies.
- N16 (:130) Acronym etymologies are virtually all false: acronymy attracts folk etymology.
- N17 (:136) Canon boundary: the map's official names are lore-shokunin's canon decision.

**Not in naming-systems.md** (checked with `rg -i 'field[- ]name|microtoponym|suffix|generic|hydronym|river name|street|romaniz|translit|dual nam|derogatory|commemorat|gazetteer|land reform'`; the only hits are :15, :67, :70, :71 and :118, all already listed above). This is the entry's uncovered ground:
- generic + specific element anatomy and suffixes;
- why river and mountain names are the oldest layer (the mechanism, not just the fact);
- naming authorities and their working principles: national boards, UNGEGN resolutions, local usage, dual naming, commemorative waiting periods, removal of derogatory names;
- romanization and transliteration beyond the one-line pinyin mention;
- street names (odonyms) as a separate system;
- field names and microtoponyms;
- folk etymology as a source-backed process, beyond the one-line lever at N4.

## (2) One-way pointer lines for the new entry

Put these in the new entry's `couples:` header and at section ends. Keep them free of S-ids: RELEVANCE stem-matches every entry line that cites a row, and RANGE fails on any id outside S500–S559. The anchors are the section headings verified above.

- `see linguistics/naming-systems.md §3` — the functional typology (descriptive, associative, commemorative, commendatory, transfer), the Bredon tautology, critical toponymy and the endonym-first summary. This entry goes deeper and does not restate them.
- `see linguistics/naming-systems.md §5` — endonym/exonym definitions, the Germany four-root case and route-layered exonyms.
- `see linguistics/naming-systems.md §7` — steps 7–8 of the name-derivation pipeline. This entry's build order extends step 8 only.
- `see linguistics/naming-systems.md §8` — the Torpenhow ghost tautology and acronym folk etymology.
- `see linguistics/language-contact.md §10` and `§11` — Celtic substrate surviving mostly in place and river names (:148), and "toponymy survives conquest" (:165).
- `see culture-material/architecture-settlement-lexicon.md §7` — the English suffix-stratum table (-chester / -wich / -by / -ton, :105–110) and build step 8 (:145). Do not reprint the table.
- `see culture-material/agrarian-field-system-lexicon.md §8` — field names as the densest rural toponym layer, rewritten first by land reform (:126).
- `see culture-material/cartography-and-mapmaking.md §8` — the replaced toponym as a map-silence class (:159). Section 2 (:57) already names naming-systems as the owner of the sheet's toponym layer.
- `see myth-symbol/sacred-topography-pilgrimage.md §7` — a site name is a charter (:98). Claims review-only partial owner.
- `see myth-symbol/cosmology-cosmography.md §9` — toponyms as cosmographic claims (:133).
- `see synthesis/deity-name-derivation-pipeline.md §4` — local/topographic epithets (:73) — and `§6`, which covers place names reshaped under name taboo (:120). Claims review-only partial owner.
- `see synthesis/naming-canon-workflow.md §7` (etymology ledger) and `§11` (handoff envelope). Claims review-only "naming entries".
- `see verification/naming-collision-gate.md §2` — alias relations such as endonym/exonym and former name (:39) — and `§1`, which says reused place names need relationships, not renaming (:20).
- `see synthesis/migration-founder-effects.md §2` — the critical-toponymy row, "A gazetteer is evidence of power" (:30).
- `see linguistics/language-shift-obsolescence-revival.md §8` — DR-7: toponyms replaced at shift, fossilized, then reclaimed (:177).
- Canon handoff line: the map's official names, dual-name choices and renaming decisions are lore-shokunin canon, matching `naming-systems.md §9` (:136).

One-way means the round lands only the entry, `corpus/README.md` and `corpus/SOURCES.md` (`claims.json` `lands`). No back-pointer is added to naming-systems.md or to any other file.

## (3) Civilization entries holding place-name material the entry may point to

Each item gives the path:line, the section, and what it holds. These are the strongest pointer targets; all other civilization hits are incidental or are "keep fields separate" one-liners.

- **Substrate and hydronym layer**
  - `civilizations/finnic-sami.md:28` ("Language family, writing, and substrate") and `:164` ("Naming practices"): Aikio's non-Uralic substrate place names survive language shift without staying transparent.
  - `civilizations/japan-yayoi-kofun.md:71` and `:81–82` ("Ainu-substrate debate"): a surviving hydronym stratum, and Ainu place-name proposals with calibration.
  - `civilizations/ainu.md:95–96` ("Ainu-moshiri, landscape, and naming practices"): river elements (`pet`, `nay`) and a seven-step toponymy workflow.
- **Generic elements and suffixes**
  - `civilizations/rapa-nui.md:175` (Naming practices): toponymic elements *hanga* 'bay', *motu* 'islet', *maunga* 'hill'.
  - `civilizations/chimu.md:165–167` ("names as layered witnesses"): Muchik `-an` 'house', `-pon/-pong` 'rock' and the unconfirmed "sun-sun" repetition reading.
  - `civilizations/thrace-dacia.md:57` and `:74`: the -dava/-bria endings, and names retained after conquest.
  - `civilizations/mexica-aztec.md:167`: the locatives -co/-tlan and place-name glyph rebus.
  - `civilizations/khmer-angkor.md:167`: local terms beside Sanskrit *-pura*.
- **Dual names, Indigenous names and renaming**
  - `civilizations/taino.md:54–67` ("Toponyms and naming practices"): Hayti beside Hispaniola, Borinquen beside Puerto Rico, Amona, and the endonym / chart exonym / bureaucratic spelling application.
  - `civilizations/australia-aboriginal.md:54` and `:140`: Kata Tjuṯa and Aṉangu place-name meanings, and the rule against borrowing sacred toponyms.
  - `civilizations/maori.md:72` and `:183`: a place name retrieves a story.
  - `civilizations/hawaii.md:131`: the place name as historical relation, not scenery.
- **Transmission and exonym chains**
  - `civilizations/etruria.md:160`: Tarch(u)na / Tarquinii / Tarquinia.
  - `civilizations/carthage.md:161`: Qart-Hadast "New City" becoming opaque and gathering exonyms.
  - `civilizations/levant-canaan-phoenician.md:151` and `:167`: Gadir 'enclosure', and ordinary words fossilizing as names that recur at new settlements.
  - `civilizations/aegean-minoan-mycenaean.md:179`: ko-no-so / Knossos continuity.
  - `civilizations/scythian-saka.md:160`: Herodotus' gloss of Exampaeus.
  - `civilizations/persia-achaemenid.md:152`: Sparda and Bābiruš as aliases.
- **Official versus vernacular, and evidence limits**
  - `civilizations/vietnam.md:158`: oral and official learned forms.
  - `civilizations/newar-nepal.md:181`: Bhaktapur/Khopa.
  - `civilizations/inca.md:164–165`: etymology as hypothesis, plus the Emlen & Norder 2026 toponymic method.
  - `civilizations/korea-three-kingdoms-goryeo.md:49` and `:170`: place-name spellings as difficult evidence.
  - `civilizations/mississippian.md:46`: Cahokia is a later name.
  - `civilizations/ancestral-puebloan.md:173`: survival of a name does not prove continuous residence.
  - `civilizations/nazca.md:60` and `:65`.

## Contradiction (stated, not smoothed)

`naming-systems.md:70` gives the renaming chain as "Leningrad→Petrograd→Leningrad→St Petersburg". The historical sequence is St Petersburg → Petrograd (1914) → Leningrad (1924) → St Petersburg (1991). [INFERENCE: standard history; I opened no source this session and no lane file states the correct chain.] Nothing else in the knowledge corpus quotes the chain; only :70's closing sentence is quoted, at `cartography-and-mapmaking.md:159`.

Consequences:
- The new entry must not repeat the :70 chain or point to §3 for it.
- If the entry uses this case, it needs its own S5xx row.
- Fixing :70 is outside claim C's `lands`. Route it as a records item.

## Proposed move (one, bounded)

**Make the entry the landing place for inbound couplings that already credit naming-systems.md with content it does not hold.** Two `couples:` headers send readers to naming-systems for material that is not there:
- `architecture-settlement-lexicon.md:4` cites it for "place-name suffix strata, toponymic morphology". Naming-systems has no suffix or morphology content; the real table is in architecture §7 itself.
- `agrarian-field-system-lexicon.md:8` cites it for "field names and microtoponyms are the densest toponym layer". Naming-systems never mentions field names.

The assignment already puts generic/specific anatomy, suffixes and field names in scope, so these are the two subsections where the entry most clearly covers ground no file holds in substance.

The move:
1. Write those two subsections from S5xx rows.
2. Point one way to architecture §7 for the English suffix table and to agrarian §8 for tenure.
3. Have the L1 route a records item (next round, outside `lands`) to retarget the two headers from naming-systems.md to toponymy-place-names.md.

Effect on the axes:
- **Coverage improves.** Two orphaned deferrals get a real owner.
- **Adjacency improves.** Pointers follow where the content actually lives.
- **No mechanical leg is affected.** SET counts files, and the move edits no non-landed file this round.

## Risks

- If the L1 edits the two `couples:` headers in-round, that touches files outside `claims.json` `lands`. SET still passes because it counts files only, but scope review fails. Keep it a records item.
- Pointer lines that carry an S-id get stem-checked by RELEVANCE. Keep them S-id-free.
- Using "see …:line" pins goes stale if those files are edited. Section anchors are more stable; line numbers are given here only as evidence.
- The entry could restate N1–N10 with new citations and present them as new. Reviewers judging "uncovered in substance" will see the overlap. Frame any reuse as "naming-systems §3 gives X; the sources show Y" (deeper), never as a fresh X.

## Verification

- Pointer validity: after landing, every `see <path> §N` in the entry should resolve to an existing `## N.` heading. Check with `rg -n '^## N\.' corpus/knowledge/<path>`. All 16 anchors above were resolved in this seat (heading-for-line mapping run over the lane working tree, 2026-10-23).
- Overlap check: grep the landed entry for the N-list markers (Bredon, Greenland, Deutschland, Cathay, Torpenhow, Leningrad, Mumbai, Harare, pinyin). Each hit should be a "see naming-systems" pointer, not a restated claim.
- Predicate: `python3 -B reports/round-58/accept-c.py`. Its review-only list (claims.json:156) names the partial owners this report maps.

installs: none.
