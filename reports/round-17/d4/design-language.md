# R17-D02 — D4 language design: inventory, syllable profile, lexicon, naming morphology

- round: 17 (operator loop 2 of 3, build round 1 of 4; 64 declared workers,
  `opencode-go/deepseek-v4.1-flash`) · shard: **D02** (D-design seat 2, language
  designer) · claim **D `culture-d4-assembly`**.
- assignment (verbatim): "D4 R17-D02 (language designer): phonology inventory +
  syllable profile + 40+ lexemes by semantic field + naming morphology per the
  brief (poll for D01, max 15 min; else independent);
  reports/round-17/d4/design-language.md."
- date: 2026-10-18. Reference revision `9b49a4a0fca6ceeab917d401945358fdedeb7e11`
  (round-17 declare); baseline `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`.
- **revision 2 — reconciled.** Revision 1 was the assignment's *else* branch: a
  poll for D01's brief ran 2026-10-18 06:15–06:23 (every 60 s, 15-minute window)
  and found no brief, so a self-contained draft was written. D01's
  `design-brief.md` then landed at 06:28 and `components/02-phonology.yml` at
  06:30. Revision 2 **supersedes** that draft: the culture, the spine and the
  phonology now follow the delivered brief and the delivered phonology component,
  and the draft's own material (the archipelago concept, its 19-consonant
  inventory and its 65 lexemes) is withdrawn as superseded, kept only in scratch.
  Nothing in revision 1 was written to any shared artifact, so no repair is owed
  anywhere outside this file.
- canon: **NON-CANON design record.** No real people, language, institution,
  script or argot is described, cited or approximated; no real-world rights,
  clearance, community-consultation or authenticity claim is made, performed or
  implied; nothing here decides anything for any world bible (canon is
  lore-shokunin's — `PROVINCE.md`).
- writes: **this file only**, plus in-lane scratch under `.scratch/`
  (`TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No component,
  tool, gate, packet or earlier-round byte is edited by this seat; no commit, no
  push.

## 0. What this file fixes

For the seats that write `examples/culture-d4/`:

1. the **phonology contract** the lexicon and the names must satisfy — adopted
   from `reports/round-17/d4/components/02-phonology.yml` (seat R17-D06), with
   the divergences between that component and its own rules reported in §2.3;
2. the **syllable profile** and the machine check over every delivered form — §3;
3. the **lexicon**: 74 plain-register lexemes across 13 fields, the derivational
   kit, the **two argot derivations** the brief requires (`head2`, `reverse`)
   with 11 worked derivations, the **6 argot loans AL-01..AL-06**, the **6
   gloss-routed slots GD-01..GD-06**, the register-history record RG-02, and the
   declared lexicon gaps — §6;
4. the **naming morphology** (name lexicon, slots, the register law on names,
   toponyms, the naming-gate red line) — §7;
5. the **typed-pipeline obligations** the language side owns — §8;
6. the **named hold set**, pre-implementation, mapped to the brief's own §7.1
   rows — §9;
7. the machine receipts — §10.

Does not fix: era names and dates, rank rules, garment routes, myth text, the
packet schema, the assembler, or the expected-holds file.

## 1. Authority, in order

| rank | source | status |
|---|---|---|
| 1 | `reports/round-17/d4/design-brief.md` (seat D01, 06:28) | the culture brief, spine COUNT × QUOTE, registry, Δ1–Δ8, candidate hold set §7.1 |
| 2 | `reports/round-17/d4/components/02-phonology.yml` (seat R17-D06, 06:30) | the delivered phonology: inventory, template, stress, allophony, sound changes, loan filters, witnesses, gate run |
| 3 | this file | the lexicon, the derivations, the names, and the language-side hold rows that sit on 1 and 2 |

Where 1 and 2 disagree, or where 2 disagrees with itself, this design follows the
brief's declared requirement, adopts 02's **rules** (which are self-consistent),
supplies forms that satisfy those rules, and **reports** the divergence (§2.3)
instead of repairing another seat's file.

**Spine.** D4's axes are `count` and `quote` (brief §3 SP-01/SP-02, with the
tagging rule SP-03). Every record in §6 carries `axis:` with one of
`count | quote | both | neutral`.

## 2. Phonology

### 2.1 Adopted profile (02-phonology.yml, quoted, not re-decided)

| item | value |
|---|---|
| consonants (14) | `p t k b d g m n s r l w j h` |
| vowels (5) | `a e i o u` |
| template | `(C)V(V)(C)` — no onset clusters, no coda clusters, empty onset only word-initially inside a root |
| codas | `n m s k` (one consonant; same four word-finally) |
| vowel sequences | long vowels `aa ee ii oo uu` and the falling diphthongs `ai au`; length is contrastive only on the stressed syllable; an unstressed vowel is always short |
| stress | fixed on the first syllable of the root; suffixes and compounds never move it |
| tone | none (`tones: 0`); intonation is phrase-level |
| gaps declared by 02 | no `/f/`, `/ʃ/`, `/v/`, `/z/`, `/θ/`; `[z ŋ ts c ç]` are allophones, never phonemes |

**Register law inherited from the brief (02's own words, adopted):** *no register
owns a private segment*. The quote register changes **vocabulary, slot
admissibility and derivation**, never the inventory. A form is a form: the quote
forms in §6 and the argot loans in §6.4 are inventory-clean and stay on the sound
channel exactly as plain forms do (brief Δ1, Δ8).

### 2.2 Allophony, sound changes and loan filters (02's, adopted)

Six allophony rules, each with a witness and no phoneme merger: `n → ŋ / _k`,
`n → ŋ / _g`, `s → z / V_V`, `t → ts / _i`, `k → c / _i`, `h → ç / _i`.
Two ordered sound changes: **SC-1** `*p → b / V_V` (E0 → E1) and **SC-2**
`*h → ∅ / V_V` with lengthening of the first vowel (E1 → E2). Two recipient-side
loan filters: **LA-1** (deaspiration `sh → s`, `kh → k`, `gh → g`; salt-road
trade layer) and **LA-2** (final-vowel truncation; north-road kin layer).

**How this design uses them.** Every E0 form in §6 is an E0-era form; a form
that shows `b` between vowels is E1/E2 by SC-1, and a long vowel that descends
from a lost `h` is E2 by SC-2. The two changes are applied mechanically, never
hand-mutated. **SC-1 is instantiated in the delivered lexicon** by `kapan →
kaban` (X69, the scale-beam: E0 intervocalic `*p`, E1/E2 `b`). **SC-2 is
declared and witnessed but not instantiated**: no delivered lexeme carries an E1
intervocalic `h`, so the change has no live form to derive from — a declared
limit (H-8), not a silent gap.

**The loan filter needs one more step than 02 declares.** LA-1 and LA-2 both
produce donor shapes that end in an unlicensed coda (`resh → res` is legal, but
`ghul → gul`, `mara → mar` are not: `/l/` and `/r/` are not codas). This design
therefore adds the **coda filter** as part of the same recipient-side filter: a
donor coda outside `{n m s k}` is repaired to the nearest licensed coda
(`l → n`, `r → n`). Witnesses: `ghul → gun` (AL-03), `mara → man` (AL-05). The
coda filter is reported as finding **F-LANG-2** (§2.3) because it changes 02's
stated witnesses, not just this file's forms.

### 2.3 Divergences found — reported, never repaired here

| id | what | evidence | owner |
|---|---|---|---|
| **F-LANG-1** | 02's records tag `axis: fire` / `axis: mark`; the brief's SP-03 fixes the tag space as `count \| quote \| both \| neutral-with-rationale` | `design-brief.md:142-145` vs `components/02-phonology.yml:108,121,132,144,155,164,174,184,194` | 02's writer / the hold-set seat |
| **F-LANG-2** | 16 of 02's own declared witnesses and lexemes violate 02's own PHON-01 coda set `{n m s k}` — 14 of them not intended as negative controls | command §10 R-4; list below | 02's writer + 05-lexicon |
| **F-LANG-3** | 02 declares the loan strata as "Salt-road trade layer" and "North-road kin layer"; the brief declares the partner stages as the western grain towns (measures, script donor) and the southern broker network (credit, numeral terms, carrier) | `02-phonology.yml:99, 220-233` vs `design-brief.md:106` | 05-lexicon / 06-register-contract |
| **F-LANG-4** | 02's cross-refs name `04-lexicon` and `05-naming`; the brief's registry names `04-ledger-script` and `12-ranks-names` (lexicon = 05, naming merged into 12) | `02-phonology.yml:263-267` vs `design-brief.md:225-238` | the integrator |

F-LANG-2, in full (forms quoted from `02-phonology.yml`, checked against its own
PHON-01; `nesk` and `kaltun` are 02's intended-illegal controls and are excluded):

`sal` (W-06 and the AL-3 blocked witness), `saal` (W-06), `ar` (AL-3 suffix),
`tat` (AL-4 blocked), `ir` (AL-4 suffix), `kal` (AL-5 blocked and the SC-2
"delivered lexeme kal 'hearth'"), `ker` (AL-5 blocked), `kalcir` (AL-5 witness),
`hacir` (AL-6 witness), `gul` (LA-1 witness), `mar` (LA-2 witness).

A form with a coda `/l/`, `/r/` or `/t/` cannot be a D4 word. This design's
lexicon therefore **respells** the affected bases with licensed codas — `sal →
san` (X01), `kal → kan` (X30), `ker → ken` (X28), `tat → tam` (X03), `-ir →
-in`, `-ar → -an` — and every respelling is listed in the record it touches.
Two exact D2 fixture forms were rejected for the same reason NB-06 exists: `tas`
(D2's "dried meat") and `kas` (D2's script word), which is why the tally notch is
`tam` (X03) and the numeral five is `sam` (X17).

**Measured consequence for the D4 gate.** `python3
tools/gates/phonology-sanity-gate.py` over a probe packet carrying 02's declared
facts (14 C, 5 V, `(C)V(V)(C)`, codas, the six rules) exits 1 with **one
`A-CLASS` REVIEW** — `s → z / V _ V` conditions on a natural class with no
expansion listed — and **no FAIL** (§10 R-3). That REVIEW is a culture-gate
finding, not a typed-pipeline hold: the brief's §7.1 hold set does not name it,
and 02's own `gate_run` note says REVIEW findings are retained and reported. It
is named here as **H-9** so that no leg of the round can claim a clean phonology
gate.

## 3. Syllable profile and the machine check

Template `(C)V(V)(C)`; a syllable is an optional single onset, a nucleus (short
vowel, long vowel, or `ai`/`au`), and an optional single coda from `{n m s k}`.
No clusters anywhere, including compound seams: `haitun` is legal, `kaltun` is
not (02's own example pair). No word of identical CV syllables (`tata` is not a
D4 word). Length and diphthongs appear only in the stressed first syllable.

**Machine check (2026-10-18).** `python3 .scratch/check-d4-language2.py` →
verdict **PASS**, **0 findings**, **333/333 forms parsed** (74 lexeme forms ×
their stage variants, 11 quote derivations, 6 argot loans, 16 name forms, 4
toponyms), seven-field floor met, all 11 derivations reproduce, **0 exact
collisions** with the D2/D3 form ledgers (37 edit-distance-1 pairs, all
cross-example). Receipt `.scratch/d4-language-receipt2.json`
(`1348bc677762ee49f51e516f4fbe89902cf110d5737d201236ae99cfee24153d`), source
`.scratch/d4-forms2.json`
(`26dfc60970f0c2c43ee8689c709549e1adf0326df37e7564cdae054f8cffc453`), checker
`.scratch/check-d4-language2.py`
(`25a239c3887f5226c729575a2083a1289833666973129327e8b781de33d2c6e4`).

## 4. Prosody

Fixed root-initial stress (adopted): the stressed syllable is the word's first,
suffixes never attract stress, and in compounds the first root keeps it. Length
is contrastive **only** under stress, which is why every long vowel in §6 sits in
a first syllable. No tone. The quote register does not add a pitch movement, a
stress shift, or a lengthening rule of its own: a quote form is an ordinary D4
form that is admissible only in a quote slot. The one prosodic fact the register
carries is lexical — the **length mark** on the QN-01 form (§6.3) — and that is
held, not licensed.

## 5. Derivation: the two argot operations (the brief's Δ3)

The brief fixes the operations; this design fixes their **exact algorithms** and
proves them on delivered forms:

- **`head2` — the first two syllables of the base.** Syllabification is
  **maximal-onset**: a consonant is taken as the onset of the following syllable
  whenever that yields a legal syllable. Under that reading `saalumi` is
  `saa.lu.mi` and its `head2` is `saalu` — not `saalum`, which a
  maximal-coda reading would give. The algorithm is stated because the two
  readings disagree, and a derivation that is not deterministic cannot be
  checked.
- **`reverse` — character-level string reversal** of the base.

Eleven worked derivations (all recomputed by the checker, all agreeing):

| base | op | quote form | slot | note |
|---|---|---|---|---|
| saalumi (X02) | head2 | saalu | quote | the QN-01 form: carries the length mark |
| min (X13) | reverse | nim | quote | numeral one |
| kus (X14) | reverse | suk | quote | numeral two |
| nam (X15) | reverse | man | quote | numeral three |
| nes (X16) | reverse | sen | quote | numeral four |
| sam (X17) | reverse | mas | quote | numeral five |
| mus (X18) | reverse | sum | quote | numeral six |
| kin (X19) | reverse | nik | quote | numeral seven |
| sun (X20) | reverse | nus | quote | numeral eight |
| samun (X21) | reverse | numas | quote | numeral nine |
| makun (X22) | reverse | nukam | quote | numeral ten |

Every numeral was chosen so that **its own reversal is a legal D4 form**: `rak`
was dropped because `kar` carries an unlicensed coda `/r/`, and `kas` was dropped
because it is an exact D2 fixture form. A derivation the language cannot spell is
not a derivation, it is a defect.

## 6. Lexicon — 74 plain-register lexemes, 6 argot loans, 6 owed slots

Counts from the receipt (§10 R-2): 74 lexemes — measures 11, numerals 10,
subsistence 8, social_order 7, trade 5, body 5, kinship 5, religion 5, landscape
5, weather 4, war 4, costume 4, quote_register 1. The coverage audit's seven-field
floor
(`corpus/knowledge/verification/lexicon-coverage-audit.md` §1: body, kinship,
weather, landscape, subsistence, war, religion) is met in every field: body 5,
kinship 5, weather 4, landscape 5, subsistence 8, war 4, religion 5. Measures,
numerals, trade, costume, social_order and quote_register are the audit's
cross-field extensions, which is where this brief's COUNT × QUOTE weight sits.
Register split: 74 plain / 0 quote in the base lexicon (quote forms are derived
slots, §5, and the argot loans, §6.4) — the split is a *slot* fact, not a second
word list. Six lexemes were added late for segment coverage (§6.8).

**Derivational kit** (morphology's to own, used consistently here): `-in` AGENT
(`tam → tamin`, `nun → nunin`, `hai → hain`, `sun → sunin`, `hum → husin`),
`-an` LOCATIVE/COLLECTIVE (`mes → mesan`, `kem- → keman`), `-un` INSTITUTION
(`san → sanun`), `-tun` HALL (`hai → haitun`), `-san` SHARE (`hai → haisan`),
`-ak` SEALED PRODUCT (`tum → tumak`), and compounding by concatenation with a
seam that creates no cluster. The 02-declared suffixes `-ir` and `-ar` are **not
used**: their final `/r/` violates PHON-01 (F-LANG-2).

**Etymology discipline.** Every lexeme carries a route (`root` / `derived` +
construction); no route is asserted without its construction, and no coinage is
hand-mutated through a sound change (corpus
`semantic-fields-lexicon-building.md` §3, §7).

### 6.1 Field tables

**measures (9)**

| id | plain form | gloss | route | E0 → E1/E2 | quote slot |
|---|---|---|---|---|---|
| D4-X01 | san | standard weight-stone (the court's public standard) | root | san | - |
| D4-X02 | saalumi | sealed grain measure (the court's sealed vessel) | root | saalumi | saalu (head2) |
| D4-X03 | tam | tally notch (one cut on the court's rod) | root | tam | - |
| D4-X04 | nun | notched rod (the ledger rod; no knot, no cord) | root | nun | - |
| D4-X05 | mes | sealed measure vessel | root | mes | - |
| D4-X06 | keman | weighing floor (where the court's scales stand) | derived | keman | - |
| D4-X07 | hum | toll (the court's charge on a stored lot) | root | hum | - |
| D4-X09 | mesan | measure yard (the court ground where lots are measured) | derived | mesan | - |
| D4-X12 | kinam | ledger frame (the frame that holds the rods of one court) | root | kinam | - |

**numerals (10)**

| id | plain form | gloss | route | E0 → E1/E2 | quote slot |
|---|---|---|---|---|---|
| D4-X13 | min | one | root | min | nim (reverse) |
| D4-X14 | kus | two | root | kus | suk (reverse) |
| D4-X15 | nam | three | root | nam | man (reverse) |
| D4-X16 | nes | four | root | nes | sen (reverse) |
| D4-X17 | sam | five | root | sam | mas (reverse) |
| D4-X18 | mus | six | root | mus | sum (reverse) |
| D4-X19 | kin | seven | root | kin | nik (reverse) |
| D4-X20 | sun | eight | root | sun | nus (reverse) |
| D4-X21 | samun | nine | root | samun | numas (reverse) |
| D4-X22 | makun | ten | root | makun | nukam (reverse) |

**trade (5)**

| id | plain form | gloss | route | E0 → E1/E2 | quote slot |
|---|---|---|---|---|---|
| D4-X53 | kunam | credit-by-tally (the lot given against a notch) | root | kunam | - |
| D4-X54 | rasam | open account (the running tally a household owes) | root | rasam | - |
| D4-X55 | husin | storage charge (the fee for a lot held in the store-house) | derived | husin | - |
| D4-X56 | musin | court seal (the mark that closes a lot) | derived | musin | - |
| D4-X57 | haisan | broker's share (the fee taken for speaking a quote) | derived | haisan | - |

**social_order (7)**

| id | plain form | gloss | route | E0 → E1/E2 | quote slot |
|---|---|---|---|---|---|
| D4-X08 | tamin | notcher (the one who cuts the tally) | derived | tamin | - |
| D4-X10 | sanun | weigh-court (the institution that keeps the standards and the rods) | derived | sanun | - |
| D4-X11 | haitun | quote-hall (the room where quotes are spoken and marked) | derived | haitun | - |
| D4-X63 | kirun | apprentice (the one who carries the rods) | root | kirun | - |
| D4-X64 | nunin | rod-holder (the rank that may cut a notch) | derived | nunin | - |
| D4-X65 | hain | broker (the rank that may speak a quote) | derived | hain | - |
| D4-X66 | sanunin | court-master (the rank that answers for the court's standards) | derived | sanunin | - |

**subsistence (5)**

| id | plain form | gloss | route | E0 → E1/E2 | quote slot |
|---|---|---|---|---|---|
| D4-X23 | kamun | grain (the standing crop of the plain) | root | kamun | - |
| D4-X24 | makan | store-house (the court's granary) | root | makan | - |
| D4-X25 | tum | grain store (the household's sealed store) | root | tum | - |
| D4-X26 | tumak | sealed store-lot (a lot closed under the court seal) | derived | tumak | - |
| D4-X27 | kuras | orchard fruit (the dried crop of the orchard belt) | root | kuras | - |

**landscape (4)**

| id | plain form | gloss | route | E0 → E1/E2 | quote slot |
|---|---|---|---|---|---|
| D4-X28 | ken | orchard tree-line (the rows that bound a court's ground) | root | ken | - |
| D4-X29 | namas | orchard belt (the strip of orchard land) | root | namas | - |
| D4-X67 | kaman | fallow field (the field resting a season) | root | kaman | - |
| D4-X68 | sunak | threshing ground (the court's hard ground where lots are spread) | root | sunak | - |

**weather (4)** — the brief's plain is season-neutral, so this field stays at the
floor: four words, each named by what it does to work.

| id | plain form | gloss | route | E0 → E1/E2 | quote slot |
|---|---|---|---|---|---|
| D4-X31 | husam | dry wind (the plain's dry air) | root | husam | - |
| D4-X32 | namin | rain-front (the rain that crosses the plain) | root | namin | - |
| D4-X33 | kasam | dust haze (the haze that hides the far court) | root | kasam | - |
| D4-X34 | suman | night cold (the plain's cold after dark) | root | suman | - |

**body (5)** — the corpus recipe: one anomalous partition plus one soul-organ
doctrine. Partition: `manuk` (hand-and-grip as one working segment, the segment
that holds a rod). Doctrine: `sunam` (the counting-breath, held while a tally is
read, is the seat of intent — which is why a rod-mark outlives a spoken word).

| id | plain form | gloss | route | E0 → E1/E2 | quote slot |
|---|---|---|---|---|---|
| D4-X30 | kan | hearth (the household fire; the plain-register oath is sworn at it) | root | kan | - |
| D4-X35 | manuk | hand-and-grip, one term | root | manuk | - |
| D4-X36 | sunam | counting-breath (seat of intent) | root | sunam | - |
| D4-X37 | rasun | standing leg (leg-and-foot, one term) | root | rasun | - |
| D4-X38 | nusan | blood (the life-substance that witnesses a rod-mark) | root | nusan | - |

**kinship (5)** — hearth-households bound by recorded marriage; no lineage
ladder, no descent skew (a deliberate contrast with D2's Omaha skew).

| id | plain form | gloss | route | E0 → E1/E2 | quote slot |
|---|---|---|---|---|---|
| D4-X39 | kamin | hearth-household (the unit that keeps a rod) | root | kamin | - |
| D4-X40 | sanin | alliance (two households bound by a recorded marriage) | root | sanin | - |
| D4-X41 | nasin | child of the alliance | root | nasin | - |
| D4-X42 | makin | household head (the one who answers for the rod) | root | makin | - |
| D4-X43 | sunin | elder (the one who keeps the sayings) | derived | sunin | - |

**religion (5)** — oath law, no pantheon: the binding force is the witnessed
quote and the rod-mark.

| id | plain form | gloss | route | E0 → E1/E2 | quote slot |
|---|---|---|---|---|---|
| D4-X44 | nasam | plain oath (sworn in the plain register; binding) | root | nasam | - |
| D4-X45 | haisam | a quote sworn as an oath (void: the quote register cannot bind) | derived | haisam | - |
| D4-X46 | kunan | witness-mark (the rod-mark of a witnessed quote) | root | kunan | - |
| D4-X47 | nurim | record line (a row of notches read in order) | root | nurim | - |
| D4-X48 | samin | attributed saying (kept with the name of the one who said it) | root | samin | - |

**war (4)**

| id | plain form | gloss | route | E0 → E1/E2 | quote slot |
|---|---|---|---|---|---|
| D4-X49 | kasun | escort (the hired guard of a lot in transit) | root | kasun | - |
| D4-X50 | rakam | seizure (a lot taken for a debt left on the rod) | root | rakam | - |
| D4-X51 | musan | night watch (the court's watch over the stores) | root | musan | - |
| D4-X52 | kinas | boundary stone (the court's limit on the plain) | root | kinas | - |

**costume (4)** — the routes are the costume component's; these are the words.

| id | plain form | gloss | route | E0 → E1/E2 | quote slot |
|---|---|---|---|---|---|
| D4-X58 | hairak | trade-sash (the imported-cloth sash worn at the court) | derived | hairak | - |
| D4-X59 | nurak | court-apron (the local-leather apron of a rod-holder) | derived | nurak | - |
| D4-X60 | kasum | guest-robe (the robe a guest broker is given) | derived | kasum | - |
| D4-X61 | sanik | rod-belt (the belt that carries a broker's rod) | derived | sanik | - |

**quote_register (1)**

| id | plain form | gloss | route | E0 → E1/E2 | quote slot |
|---|---|---|---|---|---|
| D4-X62 | hai | quote (a price spoken in the register and rod-marked) | root | hai | - |

### 6.2 Adopted bases from 02 (the cross-ref XR-01)

02's blocked witnesses imply delivered lexemes; this design adopts the legal ones
and respells the illegal ones: adopted — `nes` (X16, numeral four), `nun` (X04,
rod), `hai` (X62, quote), `hum` (X07, toll), `tum` (X25, grain store), `mes`
(X05, measure vessel); respelled — `sal → san`, `kal → kan`, `ker → ken`,
`tat → tam`. This closes 02's XR-01 for the forms 02 itself named.

### 6.3 The QN-01 form

`saalu` (X02's quote slot) is the **quote form that carries the length mark**:
its base `saalumi` has a long stressed first vowel, `head2` preserves it, and the
length notation is 02's own (W-06 family). The brief's hold row 8 requires
exactly such a form to re-exercise the `D4L-NATIVE` hold class. It is held, not
failed, and it is not a licence for the register to own a prosodic rule (§4).

### 6.4 Argot loans AL-01..AL-06 (supplied in the quote slot, plain owed)

| id | form | gloss | layer | ultimate | immediate | carrier | owed | hold |
|---|---|---|---|---|---|---|---|---|
| AL-01 | res | a west grain term | West grain-towns layer | resh | west-stage-1 | — | AL-01#plain | D4L-REGISTER-UNRESOLVED |
| AL-02 | kan | an old measure-name | West grain-towns layer | khar | west-stage-1 | southern broker network | AL-02#plain | D4L-REGISTER-UNRESOLVED |
| AL-03 | gun | a southern credit term | Southern broker layer | — (held) | south-stage-1 | southern broker network | AL-03#plain | D4L-REGISTER-UNRESOLVED |
| AL-04 | suk | a grain-lot term | West grain-towns layer | shuk | west-stage-1 | — | AL-04#plain | D4L-REGISTER-UNRESOLVED |
| AL-05 | man | a kin term of the north road | North-road kin layer | mara | north-stage-1 | — | AL-05#plain | D4L-REGISTER-UNRESOLVED |
| AL-06 | nis | an orchard term of the north road | North-road kin layer | nisha | north-stage-1 | — | AL-06#plain | D4L-REGISTER-UNRESOLVED |

Every loan form is **inventory-clean and legal under PHON-01**, so it passes the
sound gate exactly as a plain form does (Δ1's signature), while its plain doublet
stays owed. AL-02 is the three-field donor row (ultimate/immediate/carrier all
distinct and non-null); AL-03 carries `ultimate: null` and is **held, not
failed** (Δ4's B2 hold branch). Repairs per row: AL-01/AL-04 deaspiration; AL-02
deaspiration + coda filter; AL-03 deaspiration + coda filter; AL-05 truncation +
coda filter; AL-06 deaspiration + truncation.

### 6.5 Gloss-routed slots GD-01..GD-06 (no form supplied — by design)

| id | label | hold | channel |
|---|---|---|---|
| GD-01 | imported plain cloth (the west weave) | D4L-FORM-UNRESOLVED | off-sound-and-identity |
| GD-02 | salt of the south road | D4L-FORM-UNRESOLVED | off-sound-and-identity |
| GD-03 | orchard sugar (the pressed block) | D4L-FORM-UNRESOLVED | off-sound-and-identity |
| GD-04 | sealed oil jar (west goods) | D4L-FORM-UNRESOLVED | off-sound-and-identity |
| GD-05 | the west-stage ledger board (a donor record surface) | D4L-FORM-UNRESOLVED | off-sound-and-identity |
| GD-06 | guest forfeit (the guest-law pledge object) | D4L-FORM-UNRESOLVED | off-sound-and-identity |

These six are the Δ1 class-1 records: goods and donor objects the design
deliberately leaves **without a D4 form**, so their English descriptions must
never be phonotactically tested as names (the round-4 `PHON-INVENTORY` artifact
class, `examples/culture-d2/ASSEMBLY.md:94`). The gloss belongs in the
description field; the record stays off the sound and identity channels.

### 6.6 Register history

| id | record | declared | hold |
|---|---|---|---|
| RG-02 | quote register emergence | "the years the courts began teaching the argot" — a prose span with no stage tag | D4L-ERA (partial, raw string retained) |

The design's own statement of the fact is precise and would be `available_from:
E3`; the **held** record is the one written as a prose span, kept visible rather
than normalized, per Δ5. Every quote form and every argot loan in §5–§6.4 is
`available_from: E3` in the delivered records.

### 6.7 Declared lexicon gaps

No measure ladder above the sealed measure (numerals and classifiers are the
morphology component's); no varietal ladder under `kamun`/`kuras`; no pantheon
and no deity names (the culture's binding force is the quote and the rod); no
weapons stratum beyond the escort/watch words; no cloth or dye words for the
imported cloth (it stays gloss-routed, GD-01); no speech levels and no
evidentials — the register law is the culture's one grammaticalized pragmatic
system, and the other two mechanisms the corpus offers are declined, not
half-built.

### 6.8 Token-coverage additions (late, declared)

Six lexemes were added after the first full pass, because the census showed six
inventory tokens unused in the sample (`p b d w j o`) — a smell the corpus's
pitfall list names, and a real hole for `/o/` in a five-vowel system. They are
listed here rather than rewritten into §6.1's tables, so the addition is dated
and attributable; the field counts in §6's header include them.

| id | plain form | gloss | field | route | E0 → E1/E2 | why added |
|---|---|---|---|---|---|---|
| D4-X69 | kapan | scale-beam (weighed against the standards) | measures | root | kapan → kaban | uses `/p/` and instantiates SC-1 |
| D4-X70 | kona | corner post of the measure yard | measures | root | kona | uses `/o/` |
| D4-X71 | dum | under-floor pit of the store-house | subsistence | root | dum | uses `/d/` |
| D4-X72 | jai | orchard ladder (the court's picking ladder) | subsistence | root | jai | uses `/j/` |
| D4-X73 | sonak | grain sieve (the court's sieve) | subsistence | root | sonak | uses `/o/` |
| D4-X74 | wai | outer gate of the court ground | landscape | root | wai | uses `/w/` |

After these six, the usage census reports **zero unused tokens** (§10 R-2).

## 7. Naming morphology

### 7.1 Name lexicon (plain base → quote name by `reverse`)

| plain | quote (reverse) |
|---|---|
| kani | inak |
| masu | usam |
| niru | urin |
| saka | akas |
| mika | akim |
| kura | aruk |
| nusi | isun |
| musa | asum |

Eight bases, chosen so that **every reversal is a legal D4 form**: `tani` was
dropped (`inat` has an unlicensed `/t/` coda) and `risu` was dropped (`usir` has
`/r/`). The name lexicon is deliberately *not* a separate sound system — it is
the same inventory and template (02's XR-03), and the name-only status is a
matter of use, not of phonology.

### 7.2 Slots and order

Given name first; the **court word follows as a separate word** (`kani sanun`,
`masu haitun`, `niru mesan`); a broker's **quote-name** (the reverse of the given
name) is used **only inside the quote register** and is never written on the rod.
No gender morphology, no patronymic, no hereditary surname: the court, not the
bloodline, is the affiliation.

### 7.3 The register law on names

- A **plain name** is what the rod carries and what the plain register says.
- A **quote-name** is admissible only in a quote slot: speaking it in a plain
  register act is the misuse the register contract (component 06) must rule on.
- **Guest-law asymmetry**: a guest broker may quote under a quote-name but may
  not keep the court's ledger, so a guest's quote-name never enters a rod.
- **Attributed sayings**: a saying is kept with the name of the one who said it
  (`samin`), never with the court's name — which is why the naming component and
  the sayings component share this rule.

### 7.4 Toponyms

Four candidate descriptive compounds: `haitunsan` (the quote-hall court),
`kemanun` (the weighing floor), `mesankan` (the measure yard), `nunsan` (the
rods' court). **No world entity is named**; these are candidates for the toponym
layer.

### 7.5 The naming-gate red line

The brief's Δ8 requires the naming gate over the typed D4 packet to show exactly
one `CROSS-HOLD` row for the unresolved real-language sweep. This design supplies
the forms that can carry it — `saka` and `kura` are real-world-resembling strings
— and states plainly: **no clearance, permission, consultation or authenticity is
claimed, performed or implied anywhere in this design.** The row must stay
visible; it is never to be resolved by editing the form list to look clean.

## 8. Typed-pipeline obligations owned by the language side

| label kind | what supplies it | routing rule |
|---|---|---|
| `native-form` | the 74 plain lexemes (§6.1, §6.8), the 11 quote derivations (§5), the 16 name forms and 4 toponyms (§7) | the form field carries the D4 form; the English gloss never enters it |
| `borrowed-strata` | AL-01..AL-06 (§6.4) | each row links to its declared layer, its three donor fields, and the repairs that reproduce the recorded form |
| `translated-label` | GD-01..GD-06 (§6.5) | the gloss goes to the description field; the record stays off the sound and identity channels |
| **register rows (the D4 delta)** | AL-01..AL-06 quote slots + the derived quote slots | the form stays **on** the sound and identity channels while the plain doublet is owed: `D4L-REGISTER-UNRESOLVED`, `owed_slot: <id>#plain` |

Slot cardinality (Δ2): each record has at most one supplied checked form **per
(owner, slot)**; `<id>#plain` and `<id>#quote` are separate slots; the pair is
carried by `doublet_of`. Register is never `compare_only` (Δ8).

## 9. Named hold set, pre-implementation

Language-side rows, mapped to the brief's §7.1 candidate hold set (which the
hold-set seat freezes). The rows this design supplies or touches:

| brief row | id | severity | where | what this design supplies |
|---|---|---|---|---|
| 1 | `D4L-FORM-UNRESOLVED` | hold | GD-01..GD-06 | six gloss-routed slots with no D4 form (§6.5) |
| 2 | `D4L-REGISTER-UNRESOLVED` | hold | AL-01#plain..AL-06#plain | six argot loans supplied in the quote slot, plain doublet owed (§6.4) |
| 3 | `D4L-BORROW` | hold | AL-03 | donor separation incomplete: `ultimate: null`, held not failed (§6.4) |
| 4 | `D4L-ERA` | hold | RG-02 | register emergence declared as a prose span, raw retained (§6.6) |
| 8 | `D4L-NATIVE` | hold | QN-01 | `saalu`, the quote form carrying the length mark (§6.3) |

Rows 5–7 of §7.1 (`D4L-RANK` ×2, `D4L-MATERIAL`, the `D4L-RANK` note) belong to
the rank, register-contract and materials components and are not supplied here.

Rows this design adds, because the delivered tree makes them provable and leaving
them unnamed would be a silent pass:

| id | code | where | why it exists |
|---|---|---|---|
| **H-8** | declared limit | lexicon, SC-1/SC-2 | SC-1 is instantiated by one delivered lexeme (`kapan → kaban`, X69) and SC-2 is **uninstantiated**: no delivered E1 form carries intervocalic `h`, so the change has no live form to derive from. One witness per change is this design's declared floor; a reviewer wanting more must name the E0/E1 form that shows it. |
| **H-9** | `A-CLASS` | phonology `s → z / V _ V` | measured: the gate exits 1 with this one REVIEW over 02's declared facts (§2.3, §10 R-3). It is a culture-gate finding, retained and reported; the brief's §7.1 file does not name it. |
| **H-10** | `F-LANG-2` class | 02's witnesses | 14 of 02's declared witnesses/lexemes use codas outside `{n m s k}`. This design respells them in its own lexicon; if the component ships them unchanged, the phonology and naming gates will hold or fail those strings. |

Freeze discipline (the brief's §7.2, adopted): the set is named here, before
implementation; later changes are recorded amendments naming the decision that
forced them; a hold is never laundered into a note; the delivered packet carries
zero fails, and exit 0 from the D4 gate is a structural pass with open holds
printed verbatim — never a clearance.

## 10. Machine receipts (cwd = lane root, 2026-10-18, `TMPDIR=$PWD/.scratch`)

| # | command | result | artifact / digest |
|---|---|---|---|
| R-1 | `python3 .scratch/check-d4-language2.py` | exit 0, **PASS**, 0 findings, 333/333 forms parsed, 74 lexemes, seven-field floor met | `.scratch/d4-language-receipt2.json` `1348bc677762ee49f51e516f4fbe89902cf110d5737d201236ae99cfee24153d` |
| R-2 | same, counts + derivation + sweep legs | 13 fields; 11/11 derivations reproduce; 0 exact collisions against 81 prior D2/D3 forms, 37 edit-distance-1 pairs (all cross-example); **zero unused inventory tokens** after §6.8 | inside R-1's receipt |
| R-3 | `python3 tools/gates/phonology-sanity-gate.py .scratch/d4-probe-02.yml` | exit 1, **0 FAIL**, 1 REVIEW (`A-CLASS`: `s → z / V _ V` needs its finite expansion) — the delivered 02 rule set, measured | probe built from 02's declared facts |
| R-4 | `.scratch/f-lang-2-coda-check.txt` (checker's syllabifier over 02's own witnesses) | **16 violations** of 02's PHON-01 among 02's own forms, 2 of them intended negative controls; 14 real (F-LANG-2) | `.scratch/f-lang-2-coda-check.txt` |
| R-5 | `sha256sum` over the design inputs | source `.scratch/d4-forms2.json` `26dfc60970f0c2c43ee8689c709549e1adf0326df37e7564cdae054f8cffc453`; checker `25a239c3887f5226c729575a2083a1289833666973129327e8b781de33d2c6e4` | — |
| R-6 | `python3 .scratch/check-d4-language.py` (revision 1, superseded) | the withdrawn archipelago draft: PASS over its own profile, kept only as the superseded record | `.scratch/d4-language-receipt.json` |

## 11. Calibration and open items

- Every form is a `design-choice`; no form is an attested datum, and no
  real-language source is named as D4's basis. The corpus's contested claims
  (climate/tone, altitude/ejectives, diet/labiodentals) are not used at all —
  02 declines them and this design does not re-open them.
- Pitfalls checked: no kitchen-sink inventory; no English-orthography thinking;
  phonotactics written before the words and machine-checked; no uniform
  frequencies (the forms use all 14 consonants and 5 vowels); no decorative tone;
  no sound-symbolism dictionary; registers scoped as vocabulary and slots, never
  as a second phonology; allophony derived from stated drift; no absence-of-word
  claim anywhere.
- **(to-verify) items**, named so they cannot quietly become canon:
  1. the `head2` maximal-onset algorithm is this design's reading; if the
     morphology component declares a different syllabification, the derivation
     check must be re-run against its declaration;
  2. the coda filter (F-LANG-2's repair) is this design's addition to 02's stated
     loan filters — it needs the phonology owner's agreement or a respelling of
     02's witnesses;
  3. the two donor strata are declared as strata only; no donor inventory is
     modelled, and the north-road sister variety's phonology remains unmodelled
     (02's own OQ-P1);
  4. real-world resemblance screening is the naming gate's job and no clearance
     is claimed (§7.5).

## 12. Reconciliation notes for the other seats

1. **05-lexicon**: §6 is the base lexicon to realize — 74 plain records with
   `register: plain`, `axis`, `era_ids`, and the quote slots of §5; the adopted
   bases of §6.2 close 02's XR-01 for the forms 02 named.
2. **06-register-contract**: §5's two operations, §6.4's owed plain doublets and
   §7.3's name rules are the language-side facts the register law must rule on.
3. **03/04 (morphology, ledger script)**: the derivational kit of §6 is the
   morphology's to own or correct; the script's length notation rides on 02's
   W-06 family and the QN-01 form (§6.3).
4. **12-ranks-names**: §7 supplies the name ledger and the register law on names;
   the rank rules are that component's.
5. **D18/D19 (typed seats)**: §9 is the pre-implementation language-side hold
   set; H-8, H-9 and H-10 must be visible in whatever file the round uses to
   record the delivered finding set.
6. **No absorption**: contested scope, canon, and real-world rights are reported
   (`PROVINCE.md`), never decided here.
