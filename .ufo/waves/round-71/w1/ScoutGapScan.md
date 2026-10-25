# ScoutGapScan — round-71 coverage-gap widening (claim C)

Seat: L1Kotodama71.ScoutGapScan (leaf). Date: 2026-10-25. Tree: kotodama-shokunin HEAD as of sweep.
Scope: five candidate registers, word-bounded sweeps of filenames and `- topic:` lines inside
`corpus/knowledge/culture-material` (35 files), plus corpus-wide topic greps for partial owners
outside the partition. Findings only — no corpus file written. No tools installed (none needed).

## Method

- Filename sweep: tokens split on `-`/`_`; full-token match against each register lexicon (pattern of the
  claim's `find -name '*danc*'`, but word-bounded).
- Topic-line sweep: `^- topic:.*\b(<lexicon>)\b` (case-insensitive) over every culture-material `*.md`;
  corpus-wide variant over `corpus/knowledge/**/*.md`.
- Lexicons (stems): R1 dance/performance/movement = danc*, choreograph*, movement, performance, performing,
  performative · R2 maritime/seafaring/riverine = maritim*, seafar*, nautic*, sailor*, boat*, ship*, river*,
  fluvial, watercraft, harbour/harbor, naval, dock* · R3 prosody/verse-meter/poetic form = prosod*, verse*,
  metr*, metre, poetic, poetry, poem*, rhyme*, rhythm*, stanza, alliterat*, assonan*, syllabic, hexameter,
  pentameter, haiku, sonnet, bard* · R4 ritual-calendar/community-festival cycle = ritual*, calendar*,
  festival*, rite(s), ceremon*, seasonal, festive, solstice, equinox, pageant · R5 gift-exchange/reciprocity/
  hospitality = gift*, reciproc*, hospitality, potlatch, kula, moka, patronage, redistribut*, guest*, reciprocal.

## Per-register results (culture-material partition)

| Register | (a) filename owners | (b) topic-line owners | Strict claim terms |
|---|---|---|---|
| R1 dance/performance/movement | 0 | 1 (incidental) | 0 / 0 |
| R2 maritime/seafaring/riverine | 0 | 2 (incidental) | 0 / 0 |
| R3 prosody/verse-meter/poetic form | 0 | 1 (homograph) | 0 / 0 |
| R4 ritual-calendar/community-festival cycle | 2 | 20 | held |
| R5 gift-exchange/reciprocity/hospitality | 0 | 4 (incidental) | 0 / 0 |

### R1 dance/performance/movement
(a) 0 dedicated filenames. (b) 1 topic-line hit, incidental: `ritual-garments.md:3` — "…vesting prayers as
performative speech…" (performative, not dance). Strict claim terms `danc|choreograph|movement culture` = 0/0.
(c) Nearest partial owners:
1. `culture-material/ritual-garments.md:3` — performative speech in vesting; owns garment-as-office/donning-as-rite, not movement.
2. `civilizations/siam-thai.md:2` — "Ramakien indigenization, khon masked performance, rachasap…" (one tradition's performance).
3. `civilizations/taino.md:2` — "batey performance"; also `civilizations/amazigh-berber.md:2` ("asefru performance registers"), `civilizations/java-majapahit.md:3` ("…performance, and heritage traditions").
(d) Openness: HIGH. Verified open venues (probed 2026-10-25): *Recherches en danse* (OpenEdition Journals,
e-ISSN 2275-2293, diamond OA since 2014 — https://journals.openedition.org/danse/, live; issues incl. n°10 "Observer, analyser et dire le geste dansé", n°12 "Parole de danseurs et de danseuses"); *Dancecult: Journal of Electronic Music and Dance Culture* (peer-reviewed OA — https://dj.dancecult.net/); UNESCO ICH list pages (https://ich.unesco.org/en/lists) are open in browsers but served a CAPTCHA to plain HTTP reads (use browser/Wayback captures); museum catalogue pages (Met/V&A/Smithsonian online) as B-tier. 12+ tier A/B rows are readily available.

### R2 maritime/seafaring/riverine
(a) 0 dedicated filenames. (b) 2 topic-line hits, incidental: `transport-mobility-lexicon.md:4` — "VEHICLE (sledge, wheeled cart, litter, watercraft)" (watercraft as one vehicle subclass); `bathing-and-body-hygiene.md:3` — "…baptismal and river bathing" and "aqueduct, well, cistern, river, water-carrier…" (infrastructure list). Strict terms = 0/0.
(c) Nearest partial owners:
1. `culture-material/transport-mobility-lexicon.md:4` — owns the watercraft *vehicle slot*, not boats/ships/ports/navigation/seafaring life.
2. `culture-material/trade-economy-lexicon.md:5` — couples line: "trade-route loanword strata…" (commerce adjacency; maritime trade only as context).
3. Civilizations hold one tradition's maritime facet each: `civilizations/carthage.md:3` ("maritime commerce"), `civilizations/china-ming.md:2` ("maritime loan layers"), `civilizations/swahili-coast.md:2` ("maritime vocabulary"), `civilizations/ryukyu.md:2` ("maritime multilingualism"). None treats seafaring as a material system.
(d) Openness: HIGH–MEDIUM. Verified open venues: *Journal of Marine and Island Cultures* (ISSN 2212-6821, fully OA, Scopus+DOAJ, CC BY-NC-ND — https://jmic.online/, live, v15n2 2026); *Coriolis: The Interdisciplinary Journal of Maritime Studies* (OA — https://ijms.nmdl.org/, includes material culture/nautical archaeology/freshwater); Royal Museums Greenwich collections; UNESCO ICH (seafaring/fishing knowledge) bot-gated as above.

### R3 prosody/verse-meter/poetic form
(a) 0 dedicated filenames. (b) 1 topic-line hit, homograph false-positive: `trade-economy-lexicon.md:3` — "Torah and Qurʾanic balance-verses … the revolutionary metre" (measure words, not verse). Genuine poetic-form topic holders in culture-material: 0.
(c) Nearest partial owners:
1. `culture-material/trade-economy-lexicon.md:3` — the homograph trap itself (metre = unit; balance-verses = weighings).
2. `civilizations/china-tang.md:2` — "…examination register, regulated verse…" (Tang 律詩 as one civilization's poetic form).
3. `civilizations/ottoman.md:2` — "…divan poetry…"; `civilizations/swahili-coast.md:2` — "taarab poetic registers". Sibling partition `linguistics/orality-formulaic-language.md` exists (formulaic/poetic language) — a prosody entry would couple there, raising the question whether this register belongs in culture-material at all.
(d) Openness: MEDIUM–HIGH. Verified: *Cahiers de littérature orale* (OpenEdition, diamond OA — https://journals.openedition.org/clo/, live; recent issue n°95-96 "Poésies performatives : approches croisées" 2024, n°94 Bob Dylan). Classical versification scholarship is largely paywalled (Brill/CUP); public-domain metrical treatises (Wikisource/archive.org) supply A-tier primary text. Fewer dedicated OA venues than dance or maritime.

### R4 ritual-calendar/community-festival cycle
(a) 2 dedicated filenames: `calendar-festival-systems.md`, `ritual-garments.md`. (b) 20 topic-line owners (calendar-festival-systems, era-periodization-models, timekeeping-instruments, masks-masquerade, games-play-sport-contests, music-instrument, ritual-garments, etc.).
(c) Nearest partial owners: `calendar-festival-systems.md:3` (full owner: intercalation, week systems, festival cycles); `ritual-garments.md:3` (ritual work of dress; GIRM color calendar); `myth-symbol/ritual-liminality.md:3` (rites of passage, calendrical rites); `era-periodization-models.md:3` (calendar-as-loyalty).
(d) Openness: HIGH (Journal of Festive Studies, H-Net, OA no APC, DOAJ — https://journals.h-net.org/jfs; ethnographiques.org free) — but the register is already held; the 0-owner premise fails. **Not viable for a gap entry.**

### R5 gift-exchange/reciprocity/hospitality
(a) 0 dedicated filenames. (b) 4 topic-line hits, all incidental: `adornment-body-codes.md:3` ("…kula shells…" as heirloom exemplar), `bathing-and-body-hygiene.md:3` ("the bath as gift and as tax"), `cuisine-food-lexicon.md:3` ("guest-right of bread and salt"), `furniture-interior-lexicon.md:3` ("the vacant seat as a holder for an absent guest"). None owns exchange as a system.
(c) Nearest partial owners:
1. `myth-symbol/ritual-liminality.md:3` — explicitly teaches "Mauss's gift (three obligations, hau, kula, potlatch with full colonial-contact calibration)" — the strongest conceptual neighbor; a new entry must couple, never restate.
2. `culture-material/trade-economy-lexicon.md:5` — couples line: "haggle vs fixed-price vs gift registers" (market-registry adjacency).
3. `civilizations/pacific-northwest.md:2` — "ceremonial exchange … potlatch speech"; `civilizations/ainu.md:2` — "reciprocity between human and spirit worlds".
(d) Openness: MEDIUM. HAU: Journal of Ethnographic Theory archive (2011–2017) is OA; post-2018 issues are subscription (selected articles OA); HAU Books (https://haubooks.org/) full-OA monograph program; Mauss's *Essai sur le don* public-domain full text (Les Classiques des sciences sociales). Workable, but more friction and conceptual overlap than R1/R2.

## Recommendation

**Single best register: R1 dance/performance/movement** (consistent with claim C's declared entry `dance-performance-movement-codes.md`):
- True gap: 0/0 under the strict claim terms; the expanded lexicon adds only one incidental `performative` in ritual-garments, pointable one-way.
- Deepest verified open-source stack of the five: Recherches en danse (OpenEdition diamond, many issues), Dancecult (OA), UNESCO ICH dance inscriptions (bot-gated but reachable via browser/Wayback), museum collection pages — 12+ new tier A/B SOURCES rows are readily openable.
- Nearest partial owners are externals (civilizations) or one non-overlapping sibling (ritual-garments) → clean NOHARM diff (new entry + new rows + README/lesson/scorecard/log appends).

Runner-up: R2 maritime/seafaring/riverine — equally clean gap and strong OA (JMIC, Coriolis), but couples tightly with three existing siblings (transport-mobility holds watercraft; vessel-container; trade-economy), raising write complexity. R3 prosody third (gap real, OA thinner, partition fit questionable). R5 gift-exchange fourth (conceptual overlap with ritual-liminality; HAU partially closed). R4 ritual-calendar excluded — already owned.
