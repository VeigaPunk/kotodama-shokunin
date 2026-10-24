# CriticMedicineScope — domain attack on the medicine register (claim C)

Seat: `L1-kotodama-r67.CriticMedicineScope` · 2026-10-24 · base `ad5b52b`
Scope: which neighbors the entry must point to one-way; which of the 24 planned row topics
(spec-v2.json, frozen prompts) duplicate owned registers; which should have been rejects.
Evidence basis: live lane tip (entry + S805+ not yet committed — row *topics* attacked from the
frozen spec; actual row fragments under `.ufo/waves/round-67/rows/` still landing).

## 1. One-way boundary map — every partial-scope neighbor the Boundaries section must name

The entry's Boundaries section must point **out, one-way**, to all of these (entry cites the
neighbor's mechanism/institution; never restates it). Verified owners with line anchors:

**Culture-material partition**
- `bathing-and-body-hygiene.md` — owns bathing-as-*therapy* emic doctrine and the hygiene-evidence
  spine: §8 (temazcalli sweat-bath, onsen/"taking the waters", Semmelweis 1847, Snow 1854, the
  wash-house as disease control, spa-town business — ":92 let the medicine be argued"); §9 owns the
  restricted sweat-lodge permission rule AND "the 40-day quarantine" as an institutional number.
- `scent-perfume-aromatics-codes.md` — owns aromatics-as-prophylaxis: `:31` pomander "believed to
  'disinfect the air and to ward off plague and other diseases'" (S791). The plague-doctor beak's
  *fill logic* is scent's ground.
- `masks-masquerade.md` — owns the mask institution incl. healing masks (S252 "Disease mask for
  healing rituals", S265 Haudenosaunee False Face policy). The beak as mask is masks' ground.
- `costume-semiotics.md` / `dress-through-eras.md` — own costume-as-sign; the plague suit as dress text.
- `adornment-body-codes.md` — owns cosmetics §6 and wearable body objects (medicine-as-adornment,
  physic-for-beauty boundary).
- `funerary-material-culture.md` — owns the death assemblage; medicine's register *ends* at the
  deathbed (physician graves, medical instruments in assemblages read by their ladder).
- `warrior-material-culture.md` — owns war gear only; it does **not** own wounds (no wound-care
  section exists). Entry must mark battlefield surgery as *its own* claim with warrior cited for
  context — a gap-adjacent boundary, not an owned overlap.
- `cuisine-food-lexicon.md` — owns food-as-culture incl. dietary law; the regimen/dietetics boundary
  (six non-naturals vs cuisine's staple theory) needs a named split.
- `craft-artisan-lexicon.md` — owns the **guild grammar** (Epstein/Ogilvie/Rosser at `:5`,
  master-journeyman ladder, fraud machinery). Barber-surgeon and apothecary guilds are craft's
  institution instantiated on medical trades — cite, never re-derive ladders.
- `vessel-container-lexicon.md` — owns container grammar (albarello/drug jar naming; "cosmetic
  extension" already anticipated `:3`).
- `trade-economy-lexicon.md` — owns the drug/spice trade economics behind apothecary stock.
- `architecture-settlement-lexicon.md` — owns building typology; the valetudinarium/bimaristan/
  lazaretto *as buildings* are theirs — medicine owns the ward institution.
- `writing-media-surface-economy.md` — owns the recipe/papyrus/codex-as-medium side of medical texts.
- `ritual-garments.md` + `sumptuary-law-rank-display.md` — mourning/rite dress and dress regulation;
  physician's robe licensing adjacent.
- `transport-mobility-lexicon.md` / `calendar-festival-systems.md` / `fire-fuel-light.md` —
  quarantine-ship logistics, medical calendars (critical days), moxa-as-combustion. Minor but real
  one-way pointers.

**Myth-symbol partition (the dangerous half)**
- `amulets-talismans-apotropaic-marks.md` — owns the amulet register outright (S600–S651 block,
  incl. explicitly medical objects: S611 childbirth amulet, S618 birthing girdle, S622
  "Witch-bottles and **healing charms**", S636 Chnoubis). Entry owns zero amulet typology.
- `sacred-topography-pilgrimage.md` — owns **healing/incubation shrine** as site kind 6 (`:52`,
  "Asclepieia and the *iamata*"), the shrine-archive rule (`:77` "a healing shrine produces a
  medical archive"), and the Dodds incubation flag (`:114`).
- `divination-omen-systems.md` — owns incubation/omen mechanics (`:126` iamata, `:135` "medicine
  from incubation cases", `:186` Dodds contested).
- `purity-pollution-boundary-systems.md` — owns the pollution boundary map; miasma/contagion as
  purity doctrine is theirs to cite.
- `binding-speech-complex.md` — owns the curse/incantation channel; healing charms as speech-acts.
- `plant-symbolism.md` — owns plant *meaning*; materia medica vs plant symbolism needs a named split.
- `ritual-liminality.md` — owns the rite grammar healing rites borrow (votive row `:58`, life-crisis).

**Civilizations layer (in-corpus anchors the entry must cite, not re-mine)**
- `civilizations/kongo-kingdom.md` — owns nganga/nkisi: S361 Bentley gloss *nkixi* "charm,
  enchantment, fetish and medicine" (`:83`), S403 "neutralised without their medicines" (`:89`).
- `civilizations/mamluk.md:170` — *bīmāristān/māristān* already glossed in a lexicon table.
- `civilizations/mesoamerica-primary-sources.md:76` — Chilam Balam glossed "Prophecy, medicine,
  history miscellanies".
- `civilizations/haudenosaunee.md` + `masks-masquerade.md` (S265) — False Face medicine society is a
  **restricted living tradition**; bathing §9's permission rule applies verbatim.
- `civilizations/tibet.md:111` — "do not import medical assertions" caution rides on S816 (Gyushi).
- `civilizations/egypt-ancient.md`, `greece-classical.md`, `islamic-caliphate-arabic.md`,
  `china-*.md`, `india-*.md`, `japan-*.md` — civ-context pointers for the doctrine rows, one-way.

## 2. Row-topic duplicate audit (24 topics, spec order)

| id | topic | verdict |
|----|-------|---------|
| S805 Hippocratic humoral canon | clean — doctrine core, unowned |
| S806 Charaka/Ayurveda | clean |
| S807 Huangdi Neijing/qi/meridians | clean — but see S826 internal overlap |
| S808 Ibn Sina Canon | clean (cite islamic-caliphate one-way) |
| S809 monastic infirmaries/herbals | clean |
| S810 valetudinarium | clean (cite architecture for the building) |
| S811 Ebers/Edwin Smith | clean |
| S812 Galen | clean |
| **S813 plague-doctor costume** | **triple-adjacent, keep only reframed** — see §3 |
| S814 Paracelsus/iatrochemistry | clean |
| S815 Aztec herbal/Badianus | keepable — cite mesoamerica-primary-sources `:76`; the codex-as-materia-medica is medicine's |
| S816 Gyushi/Tibetan medicine | keepable — cite tibet.md `:111` caution |
| **S817 sweat-lodge therapy** | **should have been a reject or narrowed** — see §3 |
| S818 apothecary guild | keepable — cite craft-artisan's guild grammar one-way |
| S819 Vesalius | clean |
| S820 lazaretto/quarantine | keepable — bathing §9 already owns "the 40-day quarantine" as a number; institution is free |
| S821 Kampo | keepable — but East-Asia pile-up with S807/S826 |
| S822 bimaristan | keepable — mamluk.md `:170` already glosses the term; cite it, don't restate |
| S823 barber-surgeons | clean (guild pointer as S818) |
| **S824 sangoma/nganga** | **borderline — composite-topic defect** — see §3 |
| **S825 asklepieia/incubation** | **should have been a reject or recast** — see §3 |
| **S826 moxibustion/acupuncture** | **internal duplicate of S807/S821** — see §3 |
| S827 plague consilia | clean |
| **S828 medical amulets** | **should have been a reject** — see §3 |

## 3. The five flagged topics, strongest-counterexample first

**S828 medical amulets — REJECT-class.** `myth-symbol/amulets-talismans-apotropaic-marks.md` owns
the register with a ~50-row block including objects whose function is explicitly medical
(S622 "healing charms", S611 childbirth amulet, S618 birthing girdle, S636 Chnoubis). A mined row
titled "medical amulets, charms and the materia of protection" re-mines owned ground: its teaches
cell will either restate apotropaic doctrine (myth-symbol's) or thin it into medicine-via-magic
that the amulet file already frames. The honest medicine bullet is in-corpus: *"protective materia
is owned by amulets-talismans; medicine's cut is the prescription — who issues the object, for what
diagnosis, at what price"* — which needs no new row. **Should have been S829-class rejected with
reason `register-owned` and flip `row proves the amulet functions as a prescribed medical artifact
in a way the myth-symbol file does not model`.**

**S825 asklepieia/incubation — REJECT or recast.** `sacred-topography-pilgrimage.md` owns the
healing/incubation shrine as site kind 6 (`:52`) and pre-empted the exact medicine angle at `:77`:
"a healing shrine produces a medical archive". `divination-omen-systems.md` owns incubation
mechanics (`:126,:135`) and carries the Dodds caution (`:186` echoed at `:114`). The stated topic
("Greek healing sanctuaries and incubation") is owned vocabulary end-to-end. Only a recast —
*the iamata as clinical case literature, the temple as medical institution* — is medicine's; as
frozen it duplicates two myth-symbol files. Reject candidate #2.

**S817 sweat-lodge — reject or narrow.** Two owners meet here: bathing §8 owns sweat-bath-as-therapy
(temazcalli named), and bathing §9 owns the restricted-practice rule for real sweat-lodge
traditions ("describe the institution type, do not invent a ritual"). A row whose anchor is the
sweat lodge either restates bathing's doctrine or mines a restricted living ceremony — both
flagged in-corpus already. If the seat wanted an indigenous-medicine row, the unowned slice is the
*healer's office and materia custody* (medicine-bundle as office object — itself adjacent to
kongo-kingdom's nkisi complex), not the bath.

**S826 moxibustion/acupuncture — internal duplicate.** The Neijing *is* the needling canon (S807's
topic); moxa/acupuncture Japanese transmission overlaps S821 Kampo. Three rows sharing the
qi-points doctrinal core risks (a) LINK collisions on the same institutional pages (NCCIH,
museum collections, ukiyo-e), (b) RESTATE failures — three entry bullets all reconstructing
"points/moxa/qi", (c) wasted seats while midwifery, dentistry, nursing and veterinary medicine sit
unclaimed. Merge candidate; the batch padded East Asia to 4/24.

**S813 plague costume — keepable only reframed; reject-class if landed as written.** The stated
topic ("the beaked costume and its prophylaxis logic") is split three ways: the *prophylaxis logic*
is scent's S791 (pomander, same "disinfect the air… ward off plague" quote shape — a row quoting
that will RESTATE scent's teaching), the *beak-as-mask* is masks' ground, the *suit-as-text* is
costume's. The unowned slice is the **office**: the municipally hired plague doctor, the contract,
the civic sanitary payroll. If the row lands as "beak held aromatics against miasma" it is a scent
restatement and should have been rejected; if it lands as the office, it is legitimately medicine's.

**S824 sangoma/nganga — borderline composite.** Not a duplicate of an owned register (the healer's
office is unowned), but defective as scoped: (a) *nganga* is already in-corpus at kongo-kingdom
(S400/S402/S403 — ritual specialist compounding nkisi "medicines"); (b) *sangoma* (Nguni) and
*nganga* (Kongo) are different traditions — one row covering "African healing systems" invites a
shallow composite teaches cell; (c) the divinatory half of the sangoma's work belongs to
divination-omen-systems. Keepable only as the healer's *office/apprenticeship/licensure*; as
written, likely to echo Kongo civ content or produce a survey-grade teaches cell.

## 4. Secondary structural findings

- **Batch asymmetry (mild):** 4/24 rows are East Asian (S807, S816, S821, S826); no midwifery,
  nursing, dentistry, or veterinary row. A scope choice, not a defect — but S826's overlap is where
  the padding cost lands.
- **Instrument cross-impact (verified, then resolved by L1):** the reject pathway looked
  unsatisfiable at the frozen counters — `accept-c.py` bounds APPEND additions to `NEW_IDS`
  (S805-S828) + `EXTRA_IDS` (S801-S804) while `accept-ca.py` D4 requires >=2 rejected rows opened
  2026-10-24 *beyond* S801-S804 (`rej_opened_today >= len(R66_REJECTS)+2`; the `new_rejects` var is
  computed but dead). Any single-commit landing cannot satisfy both. L1 resolution (no counter
  revision): per-claim lands separation — C's receipt stamps A_c carrying only S805-S828 over base;
  Ca's lands A_ca lands later and carries S829+ rejects + the lesson; A_r (S801-S804 dispositions)
  lands before A_c. Joint predicate satisfiable *as sequenced*, recorded here as a design finding.
  Consequence for my reject-class flags: S825/S828/S817/S826 cannot become rejects inside C's lands
  window — they either land as mined rows at A_c or are dropped entirely before row-closing;
  rejected rows may only exist at A_ca. See `.ufo/waves/round-67/w1/CriticFrontier.md`.
- **Boundary count:** ~30 one-way pointers across three partitions + the civ layer. If the
  Boundaries section lists fewer than the owned ones above — specifically amulets-talismans,
  sacred-topography, divination, masks, scent, bathing, craft-artisan, kongo-kingdom, mamluk,
  mesoamerica-primary-sources — it is incomplete.
- **Entry-bullet hazard:** bullets for S825/S828/S817 are the most likely RESTATE/ONEID failures
  (neighbor-echo or thin-quote), independent of whether the rows themselves are well-formed.
- **Unverified downstream:** row fragments under `.ufo/waves/round-67/rows/<seat>/` were still
  landing at write time (only ScoutGapMed present); the verdicts above target the frozen *topics* —
  a well-chosen anchor inside a flagged topic can still survive (e.g., S813 framed on the office,
  S825 on the iamata archive as clinical literature). Flag, don't auto-fail.

Report: .ufo/waves/round-67/w1/CriticMedicineScope.md
