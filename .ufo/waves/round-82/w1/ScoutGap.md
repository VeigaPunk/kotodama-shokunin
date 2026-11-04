# ScoutGap — claim-D absence census + duplicate-document check (r82 w1)

Base `c285b2afb19d4b64320e18df1f55e426bf2d0b0c`, lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, all reads via `git -C <lane> show|grep|ls-tree <base>` (no worktree/index/jj touch). Full transcript: `.ufo/waves/round-82/w1/stage/ScoutGap/gap-census.md` (narrative + every command and raw output) and `…/stage/ScoutGap/raw-transcript.txt`.

## Verdict

**Claim D's absence clause holds at base: no knowledge file owns guest-right / hospitality as a sacral-legal institution.** 0/255 filenames match `guest|hospital|xenia|hospitium|stranger`; the vocabulary occurs on 27 lines in 15 files, all passing attributes except two narrow partial owners (`cuisine-food-lexicon.md` salt/bread table grammar; `creation-myths-taxonomy.md` one craft hook). The institutional core is absent at string level: `xenia|hospitium|guest-friend|theoxeny` → **0 files / 0 lines**; `Zeus Xenios` 0; `asylum` 0; `Philemon|Baucis` 0. No registry row carries hospitality vocabulary (0 rows).

**One source-level catch the L1 must rule on:** S905 (Wikisource Bellows Hávámál) is the *same Bellows 1923 translation already registered as S320* (Gutenberg #73533, full text opened 2026-10-22, grade A; row reads Völuspá + Grimnismol ranges). URL is free; the work is not. Either register S905 with an explicit "same translation as S320, new poem (Hávámál)" note or fold into S320.

## 1. Absence census (command → output)

- `git -C <lane> ls-tree -r --name-only <base> corpus/knowledge | grep -icE 'guest|hospital|xenia|hospitium|stranger'` → **0**
- `… | grep -c '\.md$'` → **255** (and `| wc -l` → 255: every knowledge file is .md)
- `git -C <lane> grep -icE 'xenia|hospitium|guest-friend|guest-right|guest right|theoxeny|hospitality' <base> -- corpus/knowledge` → **15 files, 27 matching lines** (aggregate: `| wc -l` = 15, `awk -F: '{s+=$NF}'` = 27)
- exact subset `guest-right|guest right|guest-friend|hospitium|xenia|theoxeny` → **2 files, 5 lines** (cuisine :3,:95,:138,:170; creation-myths :49)
- `xenia|hospitium|guest-friend|theoxeny` → **0 files, 0 lines**
- `\bguest` → 18 files / 36 lines; `\bguest-` → 2 files / 5 lines; `\bstranger` → 29 / 44; `\bforeigner` → 13 / 13; `\bhospit` → 18 / 31 (includes bīmāristān "hospital" and hospital wards); `\bsupplia` → 1 / 1
- `sacral legal|sacral-legal|sacred law` → 2 files, both unrelated (`civilizations/china-qing.md:154` witness method; `culture-material/hunting-foraging-subsistence.md:12` coupling note)
- `\bxen(o|i)` → 4 files, all Sino-Xenic / Xenophon (false positives; lines listed in transcript)

Method controls (prove the sweeps are live): filename list `grep -cE 'ritual'` → 4 and finds both owner files; `van Gennep` → 10 files; registry positive controls hit (below).

## 2. Every partial owner (path:line, count, holds / does not hold)

| anchor | n | holds | does NOT hold |
|---|---|---|---|
| `culture-material/cuisine-food-lexicon.md:3,:95,:138,:170` | 4 | salt/bread token (khleb-sol, namak-halāl/harām), pre/post-meal formulas, table grammar | institution: no xenia, theoxeny, supplication/asylum, obligation or breach grammar |
| `civilizations/ainu.md:70,:79,:156,:158,:164` | 5 | iomante reciprocal spirit-visiting | guest law |
| `civilizations/amazonia-tupi-guarani.md:54,:119,:145` | 3 | arrival/reception in encounter records | guest law |
| `civilizations/arabia-pre-islamic.md:69,:71` | 2 | hospitality as honor-virtue (fakhr/hijāʾ) | procedure/obligation |
| `civilizations/balts.md:94,:180` | 2 | calendrical coupling hook | owner claim |
| `civilizations/celts.md:70,:74` | 2 | Bres's provisioning failures → satire | guest-right law |
| `myth-symbol/creation-myths-taxonomy.md:49` | 1 | one earth-diver craft hook ("guest-right owed to the muskrat's kin") | institution |
| `linguistics/orality-formulaic-language.md:66` | 1 | arrival type-scene beat-order (host sees guest → questioning → hospitality) | law; narrative device |
| `civilizations/greece-classical.md:75` | 1 | Hestia/hearth as continuity token | Zeus Xenios, xenia |
| `civilizations/igbo.md:82` | 1 | kola reception procedure | comparative guest-law |
| `civilizations/india-tamil-sangam.md:134` | 1 | hospitality/patronage display | institution |
| `civilizations/thrace-dacia.md:105` | 1 | comparison caution (keep textual hospitality distinct) | explicitly not an owner |
| `civilizations/germanic-norse.md:148` | 1 | séance inventory | guest institution |
| `culture-material/bathing-and-body-hygiene.md:7` | 1 | couples line (bath) | hospitality |
| `myth-symbol/myth-folktale-genres.md:55` | 1 | ATU 750–849 "hospitality tests" genre label | institution |

Adjacent (couple, do not restate): `myth-symbol/purity-pollution-boundary-systems.md:33,:73` (stranger as own/other boundary, *pharmakos*); `myth-symbol/sacred-kingship-mythic-charter.md:111,:156,:159` (Sahlins stranger-king); `linguistics/register-strata-attestation.md:88,:136,:194,:206,:265` (the "guest's charge" / guest-broker — guest as bindable-but-unrecorded legal speaker); `culture-material/medicine-healing-codes.md:32` (suppliants at the abaton).

## 3. The two nearest owners — boundary in one sentence each

- `myth-symbol/ritual-liminality.md` — owns rite-of-passage/gift/sacrifice/calendar **grammar** (van Gennep, Turner, Mauss, potlatch) and hands off hospitality **content**: 0 hits for `hospital|xenia|hospitium|guest-right`; the guest appears only at :21 ("safe-conduct (the guest's token)" in van Gennep's territorial passage) and :110 ("strangers" in communitas); its `- topic:` (:3) and `- couples:` (:14) lines name neither hospitality nor guest-law. New entry may couple for threshold framing, must not restate the phases/gift obligations.
- `culture-material/cuisine-food-lexicon.md` — owns the **table grammar and salt/bread token** ("guest-right of bread and salt" is scoped inside etiquette at :3; :95 gives the lexemes; :170 asks for one guest-right token) and hands off everything institutional: obligor/obligee, sacral guarantor, theoxeny, supplication/asylum, guest-gift exchange, breach consequences. Cite :95/:138/:170; do not re-derive the salt vocabulary.

## 4. Anchors the entry may cite for partial ownership

`corpus/knowledge/culture-material/cuisine-food-lexicon.md:3,95,138,170`; `corpus/knowledge/myth-symbol/creation-myths-taxonomy.md:49`; `corpus/knowledge/linguistics/orality-formulaic-language.md:66`; `corpus/knowledge/civilizations/greece-classical.md:75`; `corpus/knowledge/myth-symbol/myth-folktale-genres.md:55`; `corpus/knowledge/civilizations/ainu.md:70`; `…/amazonia-tupi-guarani.md:54`; `…/arabia-pre-islamic.md:69`; `…/balts.md:94`; `…/celts.md:74`; `…/germanic-norse.md:148`; `…/igbo.md:82`; `…/india-tamil-sangam.md:134`; `…/thrace-dacia.md:105`; `corpus/knowledge/culture-material/bathing-and-body-hygiene.md:7`. Adjacent: `myth-symbol/purity-pollution-boundary-systems.md:33,73`; `myth-symbol/sacred-kingship-mythic-charter.md:111,156,159`; `linguistics/register-strata-attestation.md:88,136,194,206,265`; `culture-material/medicine-healing-codes.md:32`.

Prior use of the planned works (couple, not ownership): Odyssey — `myth-symbol/direction-symbolism.md:11,121`, `divination-omen-systems.md:90,141`, `linguistics/naming-systems.md:106`, `pantheon-archetypes.md:24,52`, `plant-symbolism.md:96`, `death-afterlife-eschatology.md:41`, `orality-formulaic-language.md:42,66`; Ovid *Met.* — `cosmology-cosmography.md:7,82`, `era-periodization-models.md:12,87`, `flood-traditions.md:13,56`, `music-instrument-lexicon.md:88,89` (no file cites Met. 8 / Philemon and Baucis); Hávámál — `pantheon-archetypes.md:24` (138–139) only.

## 5. Duplicate-document check (S904–S907)

- **S904** `gutenberg.org/cache/epub/1727`, boundary `1727`, `\bOdyssey\b`, `\bHomer\b`, `\bButler\b` → **0 hits** each. (A loose `1727` earlier matched S770's eBook **41727**; the boundary probe clears it.) No duplicate.
- **S906** `gutenberg.org/cache/epub/26073`, boundary `26073` → **0**; `\bOvid\b`/`\bMetamorphoses\b` → only `corpus/SOURCES.md:386` **S357** (monsters article quoting "Ovid's *Metamorphoses*"). No row for the work.
- **S907** `1911_Encyclop%C3%A6dia_Britannica/Guest` / `Britannica/Guest` → **0**. Slug free; 1911-EB Wikisource is an established row type (S702 Veil, S765 Chess, S900 Ship, S903 Ordeal).
- **S905** URL `The_Poetic_Edda_(tr._Bellows)/Hovamol`, `Hovamol`, `Hav[aá]m[aá]l` → **0**; `Poetic Edda|Bellows` → **S320 (line 349)** = *The Poetic Edda* trans. Bellows 1923, Gutenberg #73533, full text opened 2026-10-22 (977,828 B, 24,314 lines, grade A; ranges read: Völuspá, Grimnismol 39, General Introduction, Völuspá note); and **S318 (line 347)** quotes Bellows's General Introduction in its provenance chain. **Same translation already registered; Hávámál is inside S320's file.** → L1 decision required.
- Positive controls (same commands, must hit): `grep -inF 'gutenberg.org/cache/epub/73533'` → S320 line 349; `grep -inF '1911_Encyclop%C3%A6dia_Britannica/Chess'` → S765 line 721. Both hit.
- Registry shape: max id **S903**; `^\| S90[4-7] ` → 0 rows (ids free); **827** rows match the 11-cell shape (`awk -F'|' 'NF-2==11 && $2 ~ /^ S[0-9]+ $/'`); `xenia|hospitium|guest-right|guest right|hospitality|theoxeny` over SOURCES.md → **0 rows**.

## 6. Unresolved / not run by this seat

- S905 duplicate-document ruling (above) — L1.
- S907's fetch behaviour (Wikisource Wikibase scaffold) not tested here: recon only, no network call made; the fetch/UA receipt belongs to the fetch seat.
- No tool installs; no pacman; no network fetches. Scratch `/fast/scratch/hyaku/kotodama-r82/ScoutGap` removed at yield.

## 7. Files written

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScoutGap/gap-census.md`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScoutGap/raw-transcript.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScoutGap/census.sh`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/ScoutGap.md` (this report)
