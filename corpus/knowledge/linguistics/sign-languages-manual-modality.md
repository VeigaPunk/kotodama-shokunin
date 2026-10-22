# Sign languages and manual modality — the visual-manual channel as a full linguistic system: deaf-community, village and emerging sign languages, homesign, signing by hearing people, manual codes, fingerspelling and notation

- topic: sign languages and other manual communication systems as a conlang and worldbuilding method — deaf-community, shared or village and emerging sign languages, homesign, alternate sign languages used by hearing people, manual codes and contact signing, fingerspelling and notation; the register test that separates a sign language from a body code, a manual code and a writing system; sublexical parameters, grammar in space, iconicity, emergence and families; and the calibration traps (one universal sign language, sign as pantomime, the village idyll, bare counts of sign languages)
- gap filled: no file in the corpus owns sign languages or manual communication systems as a method. Filename sweep `find corpus/knowledge -iname '*sign-lang*' -o -iname '*gestur*' -o -iname '*kinesic*' -o -iname '*nonverbal*' | wc -l` → **0**; topic sweep `grep -rliP '^- topic:.*\b(gestur|sign language|kinesic|nonverbal|non-verbal|body language|proxemic)' corpus/knowledge | wc -l` → **0** (both run 2026-10-22 on corpus bytes equal to base `bff83ba`). The topic sweep reads topic lines only: `../culture-material/adornment-body-codes.md:77,:79` owns gesture and posture as body code in its title and section 7, and keeps it — this entry claims signed languages and manual codes, not gesture. Other partial owners keep their pieces and are cited one-way in §2: `phonetics-phonology.md:201` (the one modality note on sign-language phonology), `syntax-typology.md:99` (the SOV-default caveat drawn from emerging sign languages and homesign), `numerals-and-measures.md:107` (finger counting), `sound-symbolism.md:124` (iconicity in signed channels), `writing-systems.md:21` (semasiography is not writing proper).
- sources:
  - In-corpus anchors (`corpus/knowledge/`-relative `path:line`, each re-read on 2026-10-22 at corpus bytes equal to base `bff83ba`): `culture-material/adornment-body-codes.md:77,:79`; `linguistics/phonetics-phonology.md:201`; `linguistics/syntax-typology.md:99`; `linguistics/numerals-and-measures.md:107`; `linguistics/writing-systems.md:11,:20-21`; `linguistics/sound-symbolism.md:32,:124`; `linguistics/politeness-taboo-euphemism.md:75,:77,:101,:118`; `linguistics/conlang-methodology.md:36,:43`; `linguistics/language-contact.md:105`; `linguistics/language-shift-obsolescence-revival.md:48`; `linguistics/sacred-registers-liturgical-language.md:28`; `linguistics/morphological-typology.md:13`; `linguistics/sociolinguistics-registers.md:50`; `synthesis/worldbible-integration-contract.md:17`; `verification/calibration-registry.md:35-39`.
  - External shelf — **opened this round (2026-10-22)**, registered in `corpus/SOURCES.md` rows **S071–S122** and **S126**, each row carrying its URL, access date, tier scope and anchor; the round lesson's Gate holds a located quote for every row. Tier corrections to cited rows are filed as superseding rows in the same registry.
- couples: linguistics — `phonetics-phonology.md` (owns phonological theory; its `:201` note is the manual analogue developed in §5); linguistics — `syntax-typology.md` (owns word-order typology; its `:99` caveat rests on the emergence evidence of §6 and §8); linguistics — `numerals-and-measures.md` (owns counting; finger counting `:107` stays there); linguistics — `writing-systems.md` (owns scripts; fingerspelling and sign notation in §10 are not a script type); linguistics — `politeness-taboo-euphemism.md` (owns the speech ban that triggers alternate signing in §9); linguistics — `language-contact.md` (owns pidgin and creole machinery; International Sign and contact signing in §10 apply it); linguistics — `conlang-methodology.md` (owns the artlang pipeline; this entry extends it to the visual-manual channel); linguistics — `translation-protocol-fidelity.md` (owns mediation, including interpreting; this entry does not develop interpreting); culture-material — `../culture-material/adornment-body-codes.md` (owns emblems, posture and proxemics as body code, `:79`); lore-shokunin (canon: whether a signed language exists in-world, who signs it, and what its Deaf community looks like).
- source: lane-side authority is the in-corpus anchor list above plus the external rows opened this round, **S071–S122** and **S126** in `corpus/SOURCES.md`, each with URL, access date 2026-10-22, tier scope and the round lesson's located quote. Design method: fix the community first, then the manual parameters, then the grammar in space — never a spoken language transliterated onto the hands.
- verified-at: 2026-10-22 — written against corpus bytes equal to base `bff83ba65bf9559af4d7567e81703059667a0005`; pre-entry `find corpus/knowledge -name '*.md' | wc -l` → **226**, `ls corpus/knowledge/linguistics/*.md | wc -l` → **25**; post-entry **227** and **26**, re-measured with `python3 -B reports/round-28/readme/sweep.py`.
- recheck: before a signed language becomes load-bearing in a world — re-run the two gap sweeps; re-open S080 and S100 before citing an emergence date or a word order; re-open S077, S120 and S121 before quoting any count of sign languages; re-open S118 before writing a shared-signing village; re-read `../culture-material/adornment-body-codes.md:79` before assigning a form to emblem or to sign.
- scope: reference method and lane policy for the linguistics partition. This entry owns sign languages and other manual communication systems — deaf-community, village and emerging sign languages, homesign, alternate signing by hearing people, manual codes, fingerspelling and notation — as conlang and worldbuilding method; it hands gesture and body-code etiquette to `../culture-material/adornment-body-codes.md`, finger counting to `numerals-and-measures.md`, word-order typology to `syntax-typology.md` and scripts to `writing-systems.md` (§2, §15). It decides nothing about any world, gives no clinical, education-policy or legal ruling, and admits no culture into canon.

## 1. The register property: a sign language is a full language in the visual-manual modality

**Master claim.** A sign language is a full natural language in the visual-manual modality, structurally distinct from spoken languages (S077), with its own grammar and lexicon (S078); sign-language linguistics asks the same questions as spoken-language linguistics (S072, publisher description). Stokoe's 1960 monograph brought "within the purview of linguistics a virtually unknown language" and analysed signs as built from a small set of aspects — tab (location), dez (handshape), sig (movement) (S071). Status: **B** for the sign languages the sources describe; the four choices below are the lane's design frame (**H**), in order:

1. **Modality** — hands, face and body carry the linguistic load (S085); the channel sets the craft constraints.
2. **Sublexical structure** — meaningless form units combine into meaningful signs (S071, S095); without them there is only a repertoire.
3. **Community transmission** — the language lives in deaf and mixed communities and passes between generations and peers, village sign languages included (S086, S087).
4. **A grammar of its own** — design the grammar in the modality; a designed code that carries a spoken language on the hands is a manual code, not a sign language (S074, S082). Contact with spoken languages still leaves traces such as initialized signs (§10).

| Test | Pass when | Fails as (owner) |
|---|---|---|
| **Productive grammar** | morphemes combine by regular rules; new complex signs form freely | an emblem repertoire: fixed gestural glosses with dictionary meanings (`adornment-body-codes.md:79`) |
| **Community language** | a community acquires and uses it, children included — in large Deaf communities many learn it at school rather than from signing parents (S091) | a manual code of a spoken language: a designed teaching system (S074, S082) |
| **Primary medium** | carries the full communicative load face to face (**H**) | a writing system: a script encodes a unit of a language (`writing-systems.md:11`) |

Iconicity, simultaneity and the use of space are resources of the modality, not signs of deficiency; how far spatial grammar is gestural is debated (S075, **C**). Terminology: signers, deaf or Deaf community, sign language — never "deaf-mute" or "hearing-impaired" as labels (S076).

## 2. One-owner boundary

Sign languages are full natural languages in the visual-manual modality, structurally distinct from spoken languages (S077), each with its own grammar and lexicon (S078) — not improvised gesture codes; this entry owns them as a conlang and worldbuilding method, and every neighbour below keeps its own register.

| Neighbour (anchor) | What it owns | This entry's boundary |
|---|---|---|
| `adornment-body-codes.md:79` | gesture and posture as body codes: emblems with dictionary meanings, illustrators, proxemic bands (§7) | emblems and etiquette stay there; signed sentences are language and homesign is language-like (S079), not an emblem inventory |
| `syntax-typology.md:99` | word-order typology, including the SOV-default claim drawn from emerging sign languages and homesign | the typological frame stays there; the emerging-languages evidence (S080) is developed here, not re-claimed there |
| `numerals-and-measures.md:107` | finger counting as culturally patterned counting technology; counting-gesture systems | finger counting stays there; this entry treats a signed language's numerals only as lexicon built from the §5 parameters |
| `politeness-taboo-euphemism.md:75` | taboo domains, including names of the dead and occupational bans (hunters rename the quarry) | the ban mechanics stay there; signing used when speech is impractical or disallowed for cultural reasons (S109) is structured here (§9) |
| `writing-systems.md:21` | script typology; semasiography (meaning direct, not speech) is "not writing proper" | orthography stays there; fingerspelling spells a written alphabet's letters on the hands (S083), manual codes are designed for teaching a spoken language (S082), and sign notation (S116) records manual form — none of them is a script for speech |
| `phonetics-phonology.md:201` | phonological theory: sign-language phonology works without acoustics — handshape, location, movement carry contrast | the phonological framework stays there; the manual channel's design space for conlangs is built here, with deaf-community languages such as ASL (S085) as anchors |
| `conlang-methodology.md:43` | the artlang pipeline; Damin shows a register can carry its own phonology | the spoken-first pipeline stays there; this entry extends it to the visual-manual modality |
| `language-contact.md:105` | contact machinery — pidgins, creoles, mixed languages; "a creole is a language like any other" | the machinery stays there; contact signing and International Sign (§10) are contact varieties under that machinery, never "broken" signing |
| `language-shift-obsolescence-revival.md:48` | the shift/obsolescence/revival ladder; signed languages are cited among the badly documented | the ladder stays there; this entry records the endangerment of village sign languages (§4, S086) and leaves revival to that ladder |
| `sacred-registers-liturgical-language.md:28` | the sacred-register competence/event system | that system stays there; restricted manual registers in silence-bound communities `(to-verify)` are one species of alternate code here |
| `sound-symbolism.md:124` | iconicity biases; flags "iconicity is a general property, stronger in signed languages" (Perniss et al. 2010, `(to-verify)`) | the bias toolkit stays there; productive iconicity inside signed lexicons is designed here |
| `morphological-typology.md:13` | the synthesis/fusion axes and the morphological-process catalog | the sequential word-building framework stays there; simultaneous morphology (layering) is treated here as the manual modality's difference |
| `sociolinguistics-registers.md:50` | register machinery: a register is chosen per setting | the machinery stays there; this entry names contact signing and International Sign (§10) as the signed settings it applies |
| `worldbible-integration-contract.md:17` | canon ownership: lore records world-bible entities, chronology, canon decisions, bible-wide consistency | this entry supplies method and reference only; which manual system exists in-world is lore's canon call |

## 3. Typology of manual systems: who signs, and why

Read the rows as dials, not a ladder: a system's community sets how it passes on, how deep it runs, and what grammar it can grow (S087); cells without a citation are lane heuristics (**H**) or `(to-verify)`. The categories are not settled — Ethnologue files Plains Indian and Australian Aboriginal signing, both used by hearing people, as "shared" sign languages (S120).

| system | community | transmission | typical size and time depth | design consequence |
|---|---|---|---|---|
| deaf-community sign language | national Deaf community formed at schools, clubs and associations (S087) | generational plus peer-to-peer among unrelated signers (S088) | up to hundreds of thousands — ASL, one of the largest, is roughly estimated at around 250,000 users; ASL converged after the Hartford school opened in 1817 (S088) | explicit, conventionalized grammar; grammatical use of space grows across generations (S087) |
| shared (village) sign language | small village with high, often hereditary deafness; deaf and hearing members both sign (S086) | many children, deaf and hearing, acquire it in the family (S087) | a handful to about 150 deaf signers plus many hearing signers; three to at least six generations, or 90–200 years (S086); Kata Kolok at least seven generations (S092) | shared context allows less explicit structure; unusual typology; endangered by contact with urban sign languages (S086) |
| emerging sign language | a new cohort meeting for the first time (a school, a club) (S087) | mostly peer-to-peer, seeded by homesign (S088) | tens to thousands; decades (Nicaraguan Sign Language since the 1977 school) (S087) | simple early grammar — compounding, little inflection (S087); word order can fix within a generation (§6, S100); keep order claims calibrated (`syntax-typology.md:99`) |
| alternate sign language | hearing people where speech is impractical or disallowed for cultural reasons — mourning, hunting (S086, S109) | learned alongside speech; monastic signs were taught under a rule of silence (S112) | local; bounded inventory `(to-verify)` | a complement register to speech, not a rival grammar (design frame, **H**) |
| homesign | one deaf child in a hearing family (S089) | invented by the child, with family (S089) | one signer; a lifetime (S087) | structured like early language without a model — the resilient seed (S079, S089) |
| manual codes and contact signing | deaf-education classrooms and contact zones between signed and spoken users (S082) | taught or improvised; rarely native `(to-verify)` | artificial or mixed; recent `(to-verify)` | named sign systems used in deaf education (S082); some programmes pair signs with symbols and speech (S090); International Sign is a form of contact signing (S113) |
| co-speech gesture (boundary) | speakers, alongside speech (S079) | picked up with the spoken language (design frame, **H**) | every speaker; no community boundary (design frame, **H**) | conveys information but is not conventionalized and systematic the way sign is (S087); conventional emblems are body code at `adornment-body-codes.md:79` |

No row is a deficit: gesture, homesign and sign languages differ by conventionalization and systematicity (S087), and the field has moved away from its early view of sign as mere pictorial gesture (S075); the body-code register stays with `adornment-body-codes.md:79`, finger counting with `numerals-and-measures.md:107`.

## 4. Community ecology and transmission

A signing community forms where deafness is concentrated and interaction is daily: a village with hereditary deafness, a residential school, or a Deaf family. Design these six conditions as dials; the lever column is the lane's design heuristic (**H**).

| Condition | Attested case | Worldbuilding lever |
|---|---|---|
| High incidence, hereditary deafness | Adamorobe >10% in 1961, ~2% by 2001 (S091); Bengkala's recessive gene, ≥7 generations (S092); Martha's Vineyard (S093) | village signing emerges at high rates; mobility dilutes them |
| Shared village signing | Martha's Vineyard hearing and Deaf grew up signing together (S093); Adamorobe hearing villagers sign, fluency tracks contact (S091); Bengkala ~1,200 hearing signers (S092) | a bilingual village, not a separate Deaf world |
| Schools as transmission sites | in large Deaf communities most adults acquired sign language only after entering school (S091) | a school generation can shift the language (AdaSL → GSL) |
| Deaf-of-deaf families | family transmission is the minority route (S091); Adamorobe's former chief barred deaf-deaf marriage (S091) | a founder-family effect powers the founding myth, not the main channel |
| Attitudes | oralism spread after the 1880 Milan congress `(to-verify)` — history, not law | the hearing majority's ideology sets status and schooling choices (design frame, **H**) |
| Endangerment of small sign languages | AdaSL potentially endangered (S091); Kata Kolok threatened by Indonesian Sign Language shift and marriage-pattern change (S092) | pressure points: school generation, prestige sign, demographics |

## 5. Sublexical structure: the parameters a conlang must choose

Sign phonology is not gesture choreography: signs are built from a small set of simultaneous, contrastive parameters — Stokoe's tab, dez and sig: location, handshape, movement (S071, S096; `phonetics-phonology.md:201-203`) — plus palm orientation, which Battison (1978) proposed as a fourth parameter (S096), and nonmanual features, which are part of the phonology (S095). Contrast is tested with minimal pairs, pairs that differ in one parameter (S096). Status codes per `../verification/calibration-registry.md:35-39`: the parameter set is **B** (bounded to the cited sign languages); the "typical failure" column is the lane's heuristic (**H**).

| Parameter | What the designer decides | Typical failure |
|---|---|---|
| Handshape | one inventory of contrastive shapes (Stokoe's dez, S071), not the whole natural hand space — the CSLDS module, reporting Battison 1978, counts 45 possible handshapes in ASL, of which only 7 can serve as the passive hand (S097) | letting every possible hand posture into the lexicon: contrasts blur |
| Location | which body areas and planes are contrastive — four major regions with eight places each in the Prosodic Model (S095) | importing one signed language's location grid wholesale instead of fixing your own |
| Movement | path versus internal change, direction, repetition; the Prosodic Model treats movement as the core of the sign, comparable to vowels (S095) | giving every sign a unique choreography — movement classes must be finite |
| Palm orientation | whether orientation contrasts alone — fewer minimal pairs rest on orientation alone (S095); Battison (1978) adds it as a fourth parameter, with the ASL pair CHAIR/NAME (S096), while the 1978 Stokoe reprint argues against isolating it (S071) — status **C** | ignoring orientation so two signs collapse into homophony |
| Nonmanual features | which face and body articulators are grammatical — eyebrows mark yes/no questions, a headshake marks negation (S098) | reducing nonmanuals to decoration and affect |
| Two-handed constraints | symmetry condition: when both hands move, their specifications match; dominance condition: a passive hand is limited to a small unmarked set — seven shapes (A, S, B, 5, G, C, O) in the 1978 formulation the CSLDS module reports (S097); an earlier, smaller 1974 set is not checked here (to-verify) | designing two-handed signs whose hands freely differ (S097) |
| Minimal pairs | change exactly one parameter and see whether meaning changes: APPLE/ONION (location), CAR/WHICH (handshape), NAME/SHORT (movement), CHAIR/NAME (orientation) — the ASL pairs the CSLDS module lists, after Battison 1978 (S096) | never testing contrast, so the inventory cannot be told apart in use |

Build order (design heuristic, **H**): handshape inventory → locations → movement classes → orientation rule → grammatical nonmanuals → two-handed constraints; then verify every parameter by minimal-pair probes (S096).

## 6. Grammar in space

Signed sentences run several grammatical channels at once: loci and verbs carry argument structure while face and body mark clause type. Spoken languages have analogues (verbal classifiers, intonation, topic-prominent word order) (S098, S099); the difference is that the channels are visible and simultaneous. Status: the analyses of "classifier" or depicting constructions and of agreement are contested in the cited sources (**C**); the design-rule column is the lane's heuristic (**H**).

| Channel | Attested pattern | Design rule |
|---|---|---|
| Referential loci and pointing | INDEX localizes a referent in signing space; third-person referents may be placed at loci, while the first person sits at the signer's chest (S098) | fix one locus per participant; point back to it |
| Agreement verbs | the movement and orientation of certain verbs can be modulated to agree with subject and object loci (S098) | let verb trajectory point at loci: morphology becomes geometry |
| Depicting constructions | the handshape "is usually described as" identifying the class of the referent; entity versus handling types (S099) | design productive handshape classes, not frozen lexicon |
| Simultaneity | nonmanuals layer over manual signs; a side-to-side headshake is the most common nonmanual marker of negation, though some sign languages rely on manual negation (S098) | write each channel separately; let them co-occur |
| Question and topic markers | raised brows mark yes/no questions, usually over the whole clause; topics sit at the clause's left edge, typically with raised brows (S098) | decide the scope of each marker and keep it fixed |
| Emerging word order | in Al-Sayyid Bedouin Sign Language's second generation, subject precedes object in all 32 two-noun clauses; the third generation shows differences (S100) | ordered arguments are one way to disambiguate; do not assert a universal default (`syntax-typology.md:99`) |

## 7. Iconicity and arbitrariness

Iconicity in sign is **patterned**, not pantomime: in a tool-picture study, signers of three unrelated sign languages and hearing silent gesturers preferred different iconic strategies, and the preferences differed between the sign languages (S101). Design rule (**H**): pick a strategy by what the culture treats as salient, then expect conventionalization — Frishberg reports that ASL signs historically tended toward arbitrariness (S102), and Taub treats iconic forms as motivated but not determined (S103). Whether younger sign languages are more iconic in general is untested here `(to-verify)`.

| Strategy | What the form depicts | Design use (**H**) |
|---|---|---|
| Handling | the hand holding or manipulating the object (S101) | action scenes; agent focus |
| Instrument | the hand stands for the object itself (S101) | object nouns; tool categories |
| Different aspects of one referent | ASL, Danish and Chinese signs for TREE are each iconic yet pick different features of a tree (S103); finer strategy typologies exist `(to-verify)` | let each sign language of a world choose its own iconic aspect |

Refuse the myths: sign is not mime — iconic forms are conventional parts of the standard lexicon (S103) — and iconicity does not make signs universal, since strategy preferences differ across the sign languages studied (S101). Build the manual modality like any conlang; the spoken-side three-way map (arbitrary/iconic/systematic) stays in `sound-symbolism.md:32`, its signed-channel note at `sound-symbolism.md:124`.

## 8. Emergence, families and diachrony

Status: sign-language groupings are classifications, not established genealogy — Glottolog files them as pseudo-families (S073, S104) in a non-genealogical tree, grouped on lexical and/or historical evidence; for signed languages, its own page says, "such a methodology remains to be articulated" (S126) (**C**).

| Question | Evidence | Source |
|---|---|---|
| How do sign languages arise? | Nicaraguan Sign Language arose among deaf Nicaraguans "over the past 25 years" (written in 2004); successive cohorts of learners transformed early gestural signing into a linguistic system | S080 |
| What are they grouped with? | with other signed languages, not with spoken neighbours: Glottolog places ASL under LSFic, the pseudo-family named for French Sign Language (S104, S105); ASL's origin is contested (S087) | S104, S105, S087 |
| The British strand | Glottolog records a BANZSL subgroup with British and New Zealand Sign Language, inside the BSLic pseudo-family (S106, S107) | S106, S107 |
| Classical mention | Plato's *Cratylus* 422e has Socrates imagine signalling with hands, head and body "as the speechless do now" — a hypothetical in a dialogue, not a description of a signing community | S108 |

A conlang's sign history should record (design heuristic, **H**): the founder cohort (a school or village generation) whose signing later cohorts transformed (S080); its signed grouping, never the ambient spoken language by default; when and how it was first attested (records, documents, signatures); and any later cohort's change.

## 9. Alternate sign languages: signing by hearing people

Signing by hearing people is a design slot wherever speech is impractical or disallowed for cultural reasons: a manual register beside the spoken one (S109), never a deficient substitute.

| System | Trigger | Who signs | Relation to the spoken language | Design consequence |
|---|---|---|---|---|
| Aboriginal Australian sign (Warlpiri) | a taboo on speaking during mourning (S075); the dead's names are taboo in many cultures (`politeness-taboo-euphemism.md:75`) | hearing signers; Warlpiri signing tends to be confined to middle-aged and older women (S075) | alternate system used where speech is impractical or disallowed (S109) | build a lexicon-swap register; the speech ban stays owned at `politeness-taboo-euphemism.md:75,:77` |
| Plains Indian Sign Talk | intertribal contact: trade and political alliances across many spoken languages (S110) | signers across nations, including deaf signers (S110); hearing signers `(to-verify)` | a sign language crossing spoken-language barriers (S110); a 1930 Indian Sign Language Council is among the book's subjects (S110), and the National Archives hold a 1930–31 sign-language film project (S111) | a shared manual convention for contact zones; film records archive it |
| Monastic signs (Cluny, c. 900–1200) | a rule-bound discipline of silence (S112) | monks bound by the rule (S112) | signs used in place of speech in the cloister (S112) | a small, taught, policed inventory — the template for fictional silent orders |
| Occupational signing in noise | working environments where speech fails, such as sawmills (S075) | workers in the trade | supplements or overrides speech in the noisy channel | a domain-limited work shorthand (design frame, **H**) |

Design rule: set the trigger first — ritual ban, contact, rule, or channel — it fixes who signs, what the register covers, and its relation to speech.
Calibration: rows rest on opened sources (**B**) or are marked `(to-verify)`; the design-consequence column is the lane's heuristic (**H**, `../verification/calibration-registry.md:35-39`).
The speech-ban trigger is the taboo machinery of `politeness-taboo-euphemism.md:75` (names of the dead; occupational bans) and `:101` (fossil substitutes): a manual register is what a culture signs when speech is charged (design frame, **H**).

## 10. Contact, codes and writing

| System | What it is | What it is not | Design consequence |
|---|---|---|---|
| Manual alphabet / fingerspelling | conventionalized handshapes represent letters of a written alphabet; produced in sequence (S083) | a language; two families for the Latin alphabet — one-handed (ASL, Italian Sign Language) and two-handed (BSL, Auslan, NZSL) (S083) | pick one family per deaf-community language; reserve fingerspelling for names, new terms and borrowings (**H**) |
| Initialized signs, mouthing | after a first fingerspelling, an interpreter may produce the word's first letter with a movement and mouth the word (S083) | evidence about a sign language's grammar `(to-verify)` | treat them as contact features at the edge of the lexicon (**H**) |
| Contact signing | signing between users of different national sign languages (S113) | a fixed language (S113); the pidgin label is contested — the UN page uses it (S077), most experts surveyed for WFD in 2007 reject it (S113) | expect local, unstable varieties wherever signers of different languages meet (**H**) |
| International Sign | a register WFD offers for international meetings; deaf people choose between it and national sign languages (S114); contact signing with partial conventionalization and no native users (S113) | a universal sign language (S085, S121) | international occasions; any in-world home use is lore's call (**H**) |
| Signed versions of spoken languages | designed manual codes for a spoken language — Signed English is a "manual English system" with 14 sign markers (S074); named systems of this kind are used in deaf education (S082) | a naturally acquired sign language `(to-verify)` | use only if a world needs a designed code; keep codes distinct from languages (**H**) |
| Notation and writing | Stokoe's notation records handshape, location and movement as parameter values (S071, S115); HamNoSys, a phonetic-style transcription not tied to any national fingerspelling (S116); SignWriting presents itself as a way to write sign languages (S084) | a script for speech — these record manual form, not sound (contrast `writing-systems.md:21`) | analysts transcribe with a notation; whether a culture writes its sign language, and how, is a design choice (**H**) |

Sign is not gesture-code: emblems and proxemics stay at `adornment-body-codes.md:79`; homesign and emerging signs feed syntax-typology debates (`syntax-typology.md:99`) — this section owns their contact and notation layers.

## 11. Decision table and build order

Unanchored rows are the lane's design heuristics (**H**, `../verification/calibration-registry.md:38`); each check names the entry section that owns the detail.

| If your culture… | then the sign system needs… | and check |
|---|---|---|
| has a Deaf community whose members meet daily — schools, clubs, households | a conventionalized deaf-community sign language, transmitted across generations, with its own history | §3, §8; `phonetics-phonology.md:201` — manual parameters carry contrast |
| has only isolated deaf members, no signing community around them | homesign — a family-scale system structured like early language, not a community language | §3; `syntax-typology.md:99` — don't assert a default word order for homesign |
| is a small community with high hereditary deafness | a village/shared sign language that hearing members also use | §3, §4; S086, S087 |
| uses visible signing only for a restricted purpose — ritual silence, market, military, hunting | an alternate or manual code with a limited lexicon, not a full sign language | §9; `conlang-methodology.md:36` — start from the society's need |
| wants sign used alongside a spoken language by bilingual signers | contact signing: mouthing, loan signs, code-switching, with clear boundaries from the full language | §10 |
| wants to record its sign language — literature, law, dictionaries | a notation that segments handshape, location and movement; never a pictographic transcript | §10; `writing-systems.md:20-21` — featural scripts encode features; semasiography is not writing proper |

1. **Community census** — map who signs: a Deaf-only circle, a mixed hearing-and-Deaf city, or one village with hereditary deafness (decides the §3 type). *Artifact: signer-population map.*
2. **Iconicity budget** — fix how much of the vocabulary is transparent form-meaning mapping versus arbitrary (§7). *Artifact: iconicity dial setting.*
3. **Manual phonology** — choose handshape, location, movement and orientation inventories, the grammatical nonmanuals and the two-handed constraints; contrast lives in these parameters (§5; `phonetics-phonology.md:201`). *Artifact: manual-parameter chart.*
4. **Grammar in space** — decide spatial verb agreement, layout of discourse, and classifier use (§6). *Artifact: spatial-grammar sketch.*
5. **Contact and notation** — set loan-sign direction, mouthing, and whether the culture writes the language down (§10; `writing-systems.md`). *Artifact: notation sample and contact rules.*

| ID | Decision | Trigger | Failure if skipped |
|---|---|---|---|
| DR-SGN-01 | Fix the community type before any grammar | any sign-language brief | a full language built for an isolated signer, or a homesign imposed on a village |
| DR-SGN-02 | Set the iconicity budget before coining signs | lexicon work begins | an all-transparent "pantomime" stock — the disallowed frame — or an all-arbitrary stock that reads as a spoken conlang in disguise |
| DR-SGN-03 | Choose the manual parameter set (handshape, location, movement, orientation, nonmanuals, two-handed constraints) before the lexicon | coining names | a lexicon that cannot be produced fluently or kept distinct in space |
| DR-SGN-04 | Decide notation and contact before any record or loan | literature, archives, bilingual settings | treating a notation as the language itself (`writing-systems.md:21`), or inventing loan signs with no source direction |

## 12. NON-CANON worked micro-example

**NON-CANON.** The Varn valley culture, its places, the signs below and every number are invented; nothing here is a claim about a real people, and canon belongs to lore-shokunin. Walking the §11 decision table: §3 typology — a shared village sign language used by deaf and hearing residents alike (S086, S087), plus a separate mourning sign used by older women, after the Warlpiri pattern (S075); §4 ecology — hereditary deafness concentrated in two invented families (**H**); DR-SGN-02 — a mid-range iconicity budget, many signs traceable to the thing they name (§7); §5 sublexical — the parameters below; §6 grammar in space — the village signs point to real places rather than abstract loci, the attested village pattern (S087); §9 alternate — the mourning sign answers a speech ban on the dead's names (`politeness-taboo-euphemism.md:75,:77`); §10 contact and writing — a fingerspelled alphabet borrowed from the valley's script (S117), recorded in Stokoe-style parameter rows (S115).

| Sign(s) | Parameters (handshape · location · movement) | Walked through §11 |
|---|---|---|
| GRAIN; RIVER-DROP | flat-B palm · chin · outward tap; bent-1 · chest · downward arc | village shared sign language — §3, §5, §6 |
| MOURN | open-5 · shoulder · slow lowering, held | mourning alternate — §9, §10 |

## 13. Calibration bank

Codes per `../verification/calibration-registry.md:35-39` (R rejected, C contested, B bounded, H heuristic, T to-verify).

| Claim | Status | What to say instead |
|---|---|---|
| "There is one universal sign language" | R — no single signed code is universal (S085); International Sign is a contact register with a limited lexicon — the UN page calls it a pidgin (S077), most experts surveyed for WFD reject that label (S113) | name a specific signed language or a contact register |
| "Sign is pantomime" | R for pure pantomime — sign languages are fully fledged natural languages, structurally distinct from spoken ones (S077); C for "sign has gestural components" — the field once treated sign as pictorial gesture and now debates how far gesture takes part (S075) | write sign as language; decide separately how much gesture your signers use |
| "A sign language is the spoken language on the hands" | R — each sign language has its own structure, grammar and lexicon (S078) | give the signed language its own grammar |
| "Sign languages lack grammar" | R — WFD: "Each sign language has its own structure, grammar, and lexicon, equaling spoken languages in every respect" (S078) | describe the sign language's morphology and syntax |
| Shared-signing villages are idylls free of stigma | C — the "utopia" reading of Martha's Vineyard-type communities is itself under critical review (S118) | model the village's social field; attitudes are a variable (**H**) |
| First-language acquisition has a critical period | C — late first-language exposure is reported to lower ultimate attainment (S119); whether a critical period exists, its slope and any age window are debated in the same exchange | delay can matter for a world's signing characters; no single "closure" birthday |
| A world has a fixed number of sign languages | C — the counts depend on the counter: the UN page gives "more than 300", relaying WFD (S077); Ethnologue lists 161 (S120); WFD's own page counts 200+ national sign languages, 40% legally recognised (S121) | quote the count and the counter; never a bare number |
| "deaf-mute", "dumb", "hearing-impaired" are neutral labels | R — WFD: these terms "are not acceptable"; preferred "deaf" or "deaf people" (S121); the US national association reports them rejected by the community (S076) | use deaf / Deaf (community), signers, sign languages |
| "Deaf culture" (capital D) is a community identity | B — WFD ties it to shared experience, language and cultural values (S078); capital D is the scholarly convention for communities whose major language is a sign language (S122) | capitalise for the community-cultural sense; lowercase deaf for the audiological sense |

**Living-practice flag.** Sign languages and Deaf communities are living practice: the UN calls early access to sign language vital to deaf people's development and stresses preserving sign languages as part of linguistic and cultural diversity (S077); WFD estimates more than 70 million deaf people belong to signing deaf communities (S121) and holds language and culture inseparable (S078). Attribute any rights or status statement to the body that makes it; this lane rules on neither. Write fictional communities *like* theirs, never *as* them.

**Precision traps.** "Sign language" is plural and local — there is no universal sign language (S085, S121); sign is not pantomime and not "spoken language on the hands" (S077, S078); "deaf-mute", "dumb" and "hearing-impaired" are rejected labels — say deaf or Deaf (community) and signers (S076, S121).

## 14. Recheck

Before any signed language in a world becomes load-bearing — re-run the head's two sweeps before claiming the gap is still fresh; re-open S080 and S100 before citing an emergence date or word-order claim; re-open S085 before quoting ASL's status; re-open S086, S091 and S092 before quoting any village figure; re-read `../culture-material/adornment-body-codes.md:79` before separating an emblem from a sign; re-open S084 and S116 before prescribing a notation; re-open S077, S120 and S121 before quoting any count of sign languages; and re-read `syntax-typology.md:99` before asserting a word-order default.

## 15. Scope

Reference method and lane policy for the linguistics partition. This entry owns sign languages and other manual communication systems — deaf-community, village and emerging sign languages, homesign, alternate and manual codes, fingerspelling and notation — as conlang and worldbuilding method, and hands body-code etiquette, finger counting, word order and writing to their owners (§2). Handoff: lore-shokunin owns whether a signed language exists in-world, who uses it, and what Deaf culture and hearing-signer density look like there. Reference and method only.
