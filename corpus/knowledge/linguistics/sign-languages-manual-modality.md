# Sign languages and manual modality — the visual-manual channel as a full linguistic system: deaf-community, village and emerging sign languages, homesign, signing by hearing people, manual codes, fingerspelling and notation

- topic: sign languages and other manual communication systems as a conlang and worldbuilding method — deaf-community, shared or village and emerging sign languages, homesign, alternate sign languages used by hearing people, manual codes and contact signing, fingerspelling and notation; the register test that separates a sign language from a body code, a manual code and a writing system; sublexical parameters, grammar in space, iconicity, emergence and families; and the calibration traps (one universal sign language, sign as pantomime, the village idyll, bare counts of sign languages)
- gap filled: no file in the corpus owns sign languages or manual communication systems as a method. Filename sweep `find corpus/knowledge -iname '*sign-lang*' -o -iname '*gestur*' -o -iname '*kinesic*' -o -iname '*nonverbal*' | wc -l` → **0**; topic sweep `grep -rliP '^- topic:.*\b(gestur|sign language|kinesic|nonverbal|non-verbal|body language|proxemic)' corpus/knowledge | wc -l` → **0** (both run 2026-10-22 on corpus bytes equal to base `bff83ba`). The topic sweep reads topic lines only: `../culture-material/adornment-body-codes.md:77,:79` owns gesture and posture as body code in its title and section 7, and keeps it — this entry claims signed languages and manual codes, not gesture. Other partial owners keep their pieces and are cited one-way in §2: `phonetics-phonology.md:201` (the one modality note on sign-language phonology), `syntax-typology.md:99` (the SOV-default caveat drawn from emerging sign languages and homesign), `numerals-and-measures.md:107` (finger counting), `sound-symbolism.md:124` (iconicity in signed channels), `writing-systems.md:21` (semasiography is not writing proper).
- sources:
  - In-corpus anchors (`corpus/knowledge/`-relative `path:line`, each re-read on 2026-10-22 at corpus bytes equal to base `bff83ba`): `culture-material/adornment-body-codes.md:77,:79`; `linguistics/phonetics-phonology.md:201`; `linguistics/syntax-typology.md:99`; `linguistics/numerals-and-measures.md:107`; `linguistics/writing-systems.md:11,:20-21`; `linguistics/sound-symbolism.md:32,:124`; `linguistics/politeness-taboo-euphemism.md:75,:77,:101,:118`; `linguistics/conlang-methodology.md:36,:43`; `linguistics/language-contact.md:105`; `linguistics/language-shift-obsolescence-revival.md:48`; `linguistics/sacred-registers-liturgical-language.md:28`; `linguistics/morphological-typology.md:13`; `linguistics/sociolinguistics-registers.md:50`; `synthesis/worldbible-integration-contract.md:17`; `verification/calibration-registry.md:35-39`.
  - External shelf — **opened this round (2026-10-22)**, registered in `corpus/SOURCES.md` rows **S071–S122**, each row carrying its URL, access date, tier scope and anchor; the round lesson's Gate holds a located quote for every row.
- couples: linguistics — `phonetics-phonology.md` (owns phonological theory; its `:201` note is the manual analogue developed in §5); linguistics — `syntax-typology.md` (owns word-order typology; its `:99` caveat rests on the emergence evidence of §6 and §8); linguistics — `numerals-and-measures.md` (owns counting; finger counting `:107` stays there); linguistics — `writing-systems.md` (owns scripts; fingerspelling and sign notation in §10 are not a script type); linguistics — `politeness-taboo-euphemism.md` (owns the speech ban that triggers alternate signing in §9); linguistics — `language-contact.md` (owns pidgin and creole machinery; International Sign and contact signing in §10 apply it); linguistics — `conlang-methodology.md` (owns the artlang pipeline; this entry extends it to the visual-manual channel); linguistics — `translation-protocol-fidelity.md` (owns mediation; interpreting between signed and spoken languages is one live case); culture-material — `../culture-material/adornment-body-codes.md` (owns emblems, posture and proxemics as body code, `:79`); lore-shokunin (canon: whether a signed language exists in-world, who signs it, and what its Deaf community looks like).
- source: lane-side authority is the in-corpus anchor list above plus the external rows opened this round, **S071–S122** in `corpus/SOURCES.md`, each with URL, access date 2026-10-22, tier scope and the round lesson's located quote. Design method: fix the community first, then the manual parameters, then the grammar in space — never a spoken language transliterated onto the hands.
- verified-at: 2026-10-22 — written against corpus bytes equal to base `bff83ba65bf9559af4d7567e81703059667a0005`; pre-entry `find corpus/knowledge -name '*.md' | wc -l` → **226**, `ls corpus/knowledge/linguistics/*.md | wc -l` → **25**; post-entry **227** and **26**, re-measured with `python3 -B reports/round-28/readme/sweep.py`.
- recheck: before a signed language becomes load-bearing in a world — re-run the two gap sweeps; re-open S080 and S100 before citing an emergence date or a word order; re-open S077, S120 and S121 before quoting any count of sign languages; re-open S118 before writing a shared-signing village; re-read `../culture-material/adornment-body-codes.md:79` before assigning a form to emblem or to sign.
- scope: reference method and lane policy for the linguistics partition. This entry owns sign languages and other manual communication systems — deaf-community, village and emerging sign languages, homesign, alternate signing by hearing people, manual codes, fingerspelling and notation — as conlang and worldbuilding method; it hands gesture and body-code etiquette to `../culture-material/adornment-body-codes.md`, finger counting to `numerals-and-measures.md`, word-order typology to `syntax-typology.md` and scripts to `writing-systems.md` (§2, §15). It decides nothing about any world, gives no clinical, education-policy or legal ruling, and admits no culture into canon.

## 1. The register property: a sign language is a full language in the visual-manual modality

**Master claim.** A sign language is a full language in the visual-manual modality: it has its own lexicon and grammar, is acquired natively by deaf children of signing communities, and does not derive from any spoken language (S071; S072). Stokoe's 1960 analysis first brought "within the purview of linguistics a virtually unknown language" and showed signs compose from a finite inventory of form aspects — tabula (location), designator (handshape), signification (movement) — as phonemes compose words (S071). Four load-bearing choices, in order:

1. **Modality** — manual and non-manual articulators (hands, face, gaze, body) carry the linguistic load; the channel sets the craft constraints, not the grammar's depth.
2. **Sublexical structure** — meaningless form units combine into meaningful signs; without this duality there is only a repertoire (S071; S072).
3. **Community transmission** — the language lives in deaf and mixed communities that transmit it to children, including emergent village/shared sign systems (S071; S073).
4. **Independence from speech** — grammar is invented in the modality, never translated from a spoken language's morphology; codes that graft onto a spoken language fail the test (S071).

| Test | Pass when | Fails as (owner) |
|---|---|---|
| **Productive grammar** | morphemes combine by regular rules; new complex signs form freely | an emblem repertoire: fixed gestural glosses with dictionary meanings (`adornment-body-codes.md:79`) |
| **Natively acquired** | deaf children acquire the system as a first language from signing adults | a manual code of a spoken language: a designed code that keeps the spoken word order (S074) |
| **Primary medium** | carries the full communicative load face-to-face, unsupported | a writing system: a secondary notation of a language (`writing-systems.md:11`) |

Iconicity, simultaneity and spatial grammar are resources of the modality, not signs of deficiency (S075); a worldbuilder writes the register's grammar first and lets gesture borrow from it, never the reverse (design heuristic, **H**). Terminology: signers, deaf or Deaf community, sign language — never "deaf-mute" or "hearing-impaired" as labels (S076).

## 2. One-owner boundary

Sign languages are full natural languages in the visual-manual modality — with their own grammar and lexicon (S077) and their own community identity (S078) — not improvised gesture codes; this entry owns them as a conlang and worldbuilding method, and every neighbour below keeps its own register.

| Neighbour (anchor) | What it owns | This entry's boundary |
|---|---|---|
| `adornment-body-codes.md:79` | gesture and posture as body codes: emblems with dictionary meanings, illustrators, proxemic bands (§7) | emblems and etiquette stay there; homesign (S079) and signed sentences are language, not an emblem inventory |
| `syntax-typology.md:99` | word-order typology, including the SOV-default claim drawn from emerging sign languages and homesign | the typological frame stays there; the emerging-languages evidence (S080) is developed here, not re-claimed there |
| `numerals-and-measures.md:107` | finger counting as culturally patterned counting technology; counting-gesture systems | manual numeral gestures stay there; numeral morphology inside signed systems is designed here |
| `politeness-taboo-euphemism.md:75` | taboo domains, including names of the dead and occupational bans (hunters rename the quarry) | the ban mechanics stay there; alternate sign systems used while speech is banned (S081) are structured here |
| `writing-systems.md:21` | script typology; semasiography (meaning direct, not speech) is "not writing proper" | orthography stays there; fingerspelling and manual codes render a spoken language's written forms on the hands (S082, S083), and signed notation (S084) is transcription of the manual modality, not a script type |
| `phonetics-phonology.md:201` | phonological theory: sign-language phonology works without acoustics — handshape, location, movement carry contrast | the phonological framework stays there; the manual channel's design space for conlangs is built here, with deaf-community languages such as ASL (S085) as anchors |
| `conlang-methodology.md:43` | the artlang pipeline; Damin shows a register can carry its own phonology | the spoken-first pipeline stays there; this entry extends it to the visual-manual modality |
| `language-contact.md:105` | contact machinery — pidgins, creoles, mixed languages; "a creole is a language like any other" | the machinery stays there; deaf-contact varieties and the same anti-"broken" rule are applied here |
| `language-shift-obsolescence-revival.md:48` | the shift/obsolescence/revival ladder; signed languages are cited among the badly documented | the ladder stays there; village/shared sign systems (S086) and their loss and revival are applied here, never re-derived |
| `sacred-registers-liturgical-language.md:28` | the sacred-register competence/event system | that system stays there; restricted manual registers in silence-bound communities `(to-verify)` are one species of alternate code here |
| `sound-symbolism.md:124` | iconicity biases; flags "iconicity is a general property, stronger in signed languages" (Perniss et al. 2010, `(to-verify)`) | the bias toolkit stays there; productive iconicity inside signed lexicons is designed here |
| `morphological-typology.md:13` | the synthesis/fusion axes and the morphological-process catalog | the sequential word-building framework stays there; simultaneous morphology (layering) is treated here as the manual modality's difference |
| `sociolinguistics-registers.md:50` | register machinery: a register is chosen per setting | the machinery stays there; signed registers and deaf-hearing diglossic arrangements are applied cases here |
| `worldbible-integration-contract.md:17` | canon ownership: lore records world-bible entities, chronology, canon decisions, bible-wide consistency | this entry supplies method and reference only; which manual system exists in-world is lore's canon call |

## 3. Typology of manual systems: who signs, and why

Read the rows as dials, not a ladder: a system's community sets how it passes on, how deep it runs, and what grammar it can grow (S087); cells without a citation are lane heuristics (**H**) or `(to-verify)`.

| system | community | transmission | typical size and time depth | design consequence |
|---|---|---|---|---|
| deaf-community sign language | national Deaf community formed at schools, clubs and associations (S087) | generational plus peer-to-peer among unrelated signers (S088) | thousands to about 250,000 primary signers; centuries (ASL since 1817) (S088) | explicit, conventionalized grammar; grammatical use of space grows across generations (S087) |
| shared (village) sign language | small endogamous village with high hereditary deafness; deaf and hearing members both sign (S086) | everyone acquires from birth, within and between families (S087) | dozens to about 130 deaf signers plus many hearing signers; 3–6 generations (S087) | shared context allows less explicit structure; unusual typology; endangered by urban contact (S086) |
| emerging sign language | a new cohort meeting for the first time (a school, a club) (S087) | mostly peer-to-peer, seeded by homesign (S088) | tens to thousands; decades (NSL since 1977) (S087) | simple early grammar — compounding, little inflection; word order and space conventionalize slowly (S087); keep order claims calibrated (`syntax-typology.md:99`) |
| alternate sign language | hearing people where speech is taboo or impractical — mourning, hunting (S086) | learned alongside speech, later in life `(to-verify)` | local; bounded inventory `(to-verify)` | a complement register to speech, not a rival grammar (design frame, **H**) |
| homesign | one deaf child in a hearing family (S079) | invented by the child, with family (S079) | one signer; a lifetime (S087) | language-like structure without a model — the resilient seed (S079, S089) |
| manual codes and contact signing | classrooms, therapy settings and contact zones between signed and spoken users (S082) | taught or improvised; rarely native `(to-verify)` | artificial or mixed; recent `(to-verify)` | map spoken structure onto signs (S082); some programmes pair signs with symbols and speech (S090); contact forms blend source languages (sign-supported speech, International Sign) (S087, S086) |
| gesture boundary | all speakers, co-speech (S079) | universal among speakers (S079) | unbounded; no shared convention | information-bearing but not a conventional system (S079); the raw material sign systems build on (S087) |

No row is a deficit: gesture, homesign and sign languages form a gradient, not a hierarchy (S087); the body-code register stays with `adornment-body-codes.md:79`, finger counting with `numerals-and-measures.md:107`.

## 4. Community ecology and transmission

A signing community forms where deafness is concentrated and interaction is daily: a village with hereditary deafness, a residential school, or a Deaf family. Design these six conditions as dials:

| Condition | Attested case | Worldbuilding lever |
|---|---|---|
| High incidence, hereditary deafness | Adamorobe >10% in 1961, ~2% by 2001 (S091); Bengkala's recessive gene, ≥7 generations (S092); Martha's Vineyard (S093) | village signing emerges at high rates; mobility dilutes them |
| Shared village signing | Martha's Vineyard hearing and Deaf grew up signing together (S093); Adamorobe hearing villagers sign, fluency tracks contact (S091); Bengkala ~1,200 hearing signers (S092) | a bilingual village, not a separate Deaf world |
| Schools as transmission sites | most Deaf children learn their sign language only after entering school; ~5% are born to Deaf parents (S091) | a school generation can shift the language (AdaSL → GSL) |
| Deaf-of-deaf families | family transmission is the minority route (S091); Adamorobe's former chief barred deaf-deaf marriage (S091) | a founder-family effect powers the founding myth, not the main channel |
| Attitudes | oralism spread after the 1880 Milan congress `(to-verify)` — history, not law | the hearing majority's ideology sets status and schooling choices |
| Endangerment of small sign languages | AdaSL potentially endangered (S091); Kata Kolok threatened by Indonesian Sign Language shift and marriage-pattern change (S092) | pressure points: school generation, prestige sign, demographics |

## 5. Sublexical structure: the parameters a conlang must choose

Sign phonology is not gesture choreography: signs are built from a small closed set of simultaneous, contrastive parameters — Stokoe's tab/dez/sig, location, handshape, movement (S071, S094; `phonetics-phonology.md:201-203`), plus palm orientation (S094) and nonmanual features (S095). Contrast is proven by minimal pairs — pairs differing in exactly one parameter (S096, S094); iconicity never excuses skipping contrast (S095).

| Parameter | What the designer decides | Typical failure |
|---|---|---|
| Handshape | one phonemic inventory of contrastive shapes (Stokoe's dez, S071), not the whole natural hand space — Battison counts ~45 handshape primes in ASL (S094) | letting every possible hand posture into the lexicon: contrasts blur and signers cannot discriminate reliable forms (design rule) |
| Location | which body areas and planes are contrastive — four major regions, eight distinctions each in the Prosodic Model (S095) | importing one signed language's location grid wholesale instead of fixing your own; conflating contact with proximity (design rule) |
| Movement | path vs internal aperture change, direction, repetition; movement is the syllable nucleus comparable to vowels (S095) | giving every sign a unique choreography — movement classes must be finite and constrained (design rule) |
| Palm orientation | whether orientation contrasts alone — fewer minimal pairs exist on orientation alone (S095); Battison added it as a fourth parameter (S094) | ignoring orientation so two signs collapse into homophony, or treating it as pure free variation (design rule) |
| Nonmanual features | which face and body articulators are grammatical — eyebrows, gaze, mouth, head tilt — and what they mark (S095) | importing spoken intonation grammar onto the face, or reducing nonmanuals to decoration and affect (design rule) |
| Two-handed constraints | symmetry condition: when both hands move their specs match; dominance condition: a passive hand is limited to a small unmarked set (A, B, 5, G, C, O) (S097, S094) | designing two-handed signs whose hands freely differ — cross-linguistically rare and articulatorily awkward (S097) |
| Minimal pairs | calibrate each parameter: change exactly one feature and see whether meaning changes (APPLE/ONION, CAR/WHICH, OFFER/MAYBE, SHORT/TRAIN, S094) | never testing contrast, or assuming iconicity replaces the phonological system (S095) |

Build order: handshape inventory → locations → movement classes → orientation rule → grammatical nonmanuals → two-handed constraints; then verify every parameter by minimal-pair probes (S096). Each parameter must earn its place by contrast (S071, S095).

## 6. Grammar in space

Signed sentences run several grammatical channels at once: loci and verbs carry argument structure while face and body carry clause type — a surface with no spoken analogue.

| Channel | Attested pattern | Design rule |
|---|---|---|
| Referential loci and pointing | INDEX localizes a referent in signing space; pronouns may be placed anywhere in it (S098) | fix one locus per participant; point back to it |
| Indicating / agreement verbs | verb movement and orientation can be modulated to agree with subject and object (S098) | let verb trajectory point at loci: morphology becomes geometry |
| Depicting constructions | handshape "identifies the class of the referent"; entity vs handling types (S099) | design productive handshape classes, not frozen lexicon |
| Simultaneity | nonmanuals layer over manual signs; headshake is "the most common marker" of negation (S098) | write each channel separately; let them co-occur |
| Question, negation, topic markers | brows mark yes/no questions; topics sit at clause-left with their own marking (S098) | scope of the marker tracks the constituent, not the sentence |
| Emerging word order | ABSL shows regular S-O-V within one generation; subject precedes object in all 32 two-noun clauses (S100) | ordered arguments are the simplest disambiguator; do not assert a universal default (`syntax-typology.md:99`) |

## 7. Iconicity and arbitrariness

Iconicity in sign is **patterned**, not pantomime: signers organize iconic form into lexical strategies whose distribution differs even between unrelated sign languages (S101). Design rule: pick a strategy — handling, instrument, or shape — by what the culture treats as salient, then expect conventionalization: historically, ASL signs tend to drift toward arbitrariness (S102), and every iconic form is motivated but not determined (S103) — a young sign language reads more iconic than an old one.

| Strategy | What the form depicts | Design use |
|---|---|---|
| Handling | the hand holding or manipulating the tool (S101) | action/verb scenes; agent focus |
| Instrument | the handshape stands for the tool's own shape (S101) | noun lexicon; tool categories |
| Shape | the hands trace the referent's outline — ASL, Danish and Chinese TREE are equally iconic yet trace differently (S103) | depicting constructions; spatial layout |

Refuse the myths: sign is not mime — iconic forms are conventional, standard lexicon (S103) — and there is no universal sign: strategy distributions differ across three unrelated sign languages (S101). Build the manual modality like any conlang; the spoken-side three-way map (arbitrary/iconic/systematic) stays in `sound-symbolism.md:32`, its signed-channel note at `sound-symbolism.md:124`.

## 8. Emergence, families and diachrony

| Question | Evidence | Source |
|---|---|---|
| How do sign languages arise? | Nicaraguan Sign Language arose among deaf Nicaraguans over about 25 years; successive child cohorts turned early gestural signing into a linguistic system — through cohorts, not from nothing | S080 |
| What are they related to? | Genealogically to other signed languages, not spoken neighbours: ASL classifies inside LSFic, the French Sign Language pseudo-family | S104, S105 |
| The British strand | BSL, Auslan and NZSL form the BANZSL subgroup within BSLic, argued on lexical and historical evidence | S106, S107 |
| Deep attestation | Plato's *Cratylus* 422e has Socrates propose signalling with hands, head and body when there is no voice — a thought experiment, not evidence of a Greek signing community | S108 |

A conlang's sign history must record: the founder cohort (a school or village generation) whose peer learning became the grammar (S080); its signed lineage — which manual family it descends from, never the ambient spoken language (S104, S106); when and how it was first attested (records, documents, signatures; design heuristic, **H**); and any later cohort's re-analysis, like the Nicaraguan cohorts' regularized grammar (S080).

## 9. Alternate sign languages: signing by hearing people

Signing by hearing people is a design slot wherever speech is banned, blocked or impractical: a manual register beside the spoken one (S081, S109), never a deficient substitute.

| System | Trigger | Who signs | Relation to the spoken language | Design consequence |
|---|---|---|---|---|
| Aboriginal Australian sign (Warlpiri) | mourning speech restrictions — names of the dead (`politeness-taboo-euphemism.md:75`) | hearing signers, including bereaved women `(to-verify)` | alternate system used instead of speech where speech is disallowed (S081, S109) | build a lexicon-swap register; the speech ban stays owned at `politeness-taboo-euphemism.md:75,:77` |
| Plains Indian Sign Talk | intertribal contact: trade and alliances across many spoken languages (S110) | signers across nations — hearing and Deaf (S110) | lingua franca crossing spoken-language barriers (S110); a 1930 council was filmed to record it (S111) | a shared manual convention for contact zones; the film record archives it (S111) |
| Monastic signs (Cluny, c. 900–1200) | vows of silence under a religious rule (S112) | monks bound by the rule (S112) | replaces speech in the cloister for necessary communication; deliberately restricted (S112) | a small, taught, policed inventory — the template for fictional silent orders |
| Occupational signing in noise | working environments where speech fails, such as sawmills (S075) | workers in the trade | supplements or overrides speech in the noisy channel | a domain-limited work shorthand (design frame, **H**) |

Design rule: set the trigger first — ritual ban, contact, rule, or channel — it fixes who signs, what the register covers, and its relation to speech.
Calibration: rows rest on opened sources (**B**) or are marked `(to-verify)`; the design-consequence column is the lane's heuristic (**H**, `calibration-registry.md:35-39`).
The speech-ban trigger is the taboo machinery of `politeness-taboo-euphemism.md:75` (names of the dead; occupational bans) and `:101` (fossil substitutes): a manual register is what a culture signs when speech is charged.
Terminology: sign languages, signers, Deaf communities — never "deaf-mute", "dumb", or "hearing-impaired".

## 10. Contact, codes and writing

| System | What it is | What it is not | Design consequence |
|---|---|---|---|
| Manual alphabet / fingerspelling | conventionalized handshapes represent letters of a spoken alphabet; produced sequentially (S083) | a language; letter-families differ — one-handed (ASL, LIS, ISL) vs two-handed BANZSL (BSL/Auslan/NZSL) (S083) | pick one family per deaf-community language; reserve fingerspelling for names, new terms, borrowings |
| Initialized signs, mouthing | letter-based signs — a sign's first letter with a circular movement — and co-occurring mouthing, as contact traces (S083) | evidence that signed grammar mirrors spoken word order (S083) | assign them to name, school and newest registers; keep core grammar free of them |
| Contact signing | improvised signing between signers of different national sign languages (S113) | a fixed language (S113); the pidgin label is contested — the UN page uses it (S077), most experts surveyed for WFD reject it (S113) | fits fairs, federations, pilgrimages; expect local, unstable varieties |
| International Sign | WFD's meeting/interpreting register; deaf people choose it alongside national sign languages (S114); contact signing whose conventionalization is partial and that has no native users (S113) | a universal sign language or a substitute for a national sign language (S114) | shared-stage occasions only; never a home language (S113) |
| Signed versions of spoken languages | deliberately designed visual codes for a spoken language — e.g. Signed English (14 sign markers) arranges a borrowed sign vocabulary in English word order (S074) | naturally acquired sign languages; not ASL-English bilingual education (S074) | only if your world has a deaf-education policy story; keep codes distinct from languages |
| Notation and writing | Stokoe's notation records handshape, location and movement as parameter values (S071, S115); HamNoSys, a phonetic-style transcription, international, not tied to any national fingerspelling (S116); SignWriting writes sign languages directly (S084) | scripts of a spoken language — they record manual-visual form, not sound (`writing-systems.md:21`) | a literate deaf community writes SignWriting; analysts transcribe with HamNoSys; never conflate notation with a language |

Sign is not gesture-code: emblems and proxemics stay at `adornment-body-codes.md:79`; homesign and emerging signs feed syntax-typology debates (`syntax-typology.md:99`) — this section owns their contact and notation layers.

## 11. Decision table and build order

Unanchored rows are the lane's design heuristics (**H**, `calibration-registry.md:38`); each check names the entry section that owns the detail.

| If your culture… | then the sign system needs… | and check |
|---|---|---|
| has a Deaf community whose members meet daily — schools, clubs, households | a conventionalized deaf-community sign language, transmitted across generations, with its own history and registers | §3; `phonetics-phonology.md:201` — manual parameters carry contrast |
| has only isolated deaf members, no signing community around them | homesign — a private, improvised gestural system, not a community language | §3; `syntax-typology.md:99` — don't assert a default word order for homesign |
| is a small community with high hereditary deafness | a village/shared sign language that hearing neighbours also learn; expect expansion beyond the deaf cohort | §3; S100 |
| uses visible signing only for a restricted purpose — ritual silence, market, military, hunting | an alternate or manual code with a limited lexicon, not a full sign language | §9; `conlang-methodology.md:36` — start from the society's need |
| wants sign used alongside a spoken language by bilingual signers | contact signing: mouthing, loan signs, code-switching, with clear boundaries from the full language | §10 |
| wants to record its sign language — literature, law, dictionaries | a notation that segments handshape, location and movement; never a pictographic transcript | §10; `writing-systems.md:20-21` — featural scripts encode features; semasiography is not writing proper |

1. **Community census** — map who signs: a Deaf-only circle, a mixed hearing-and-Deaf city, or one village with hereditary deafness (decides the §3 type). *Artifact: signer-population map.*
2. **Iconicity budget** — fix how much of the vocabulary is transparent form-meaning mapping versus arbitrary (§7). *Artifact: iconicity dial setting.*
3. **Manual phonology** — choose handshape, location and movement inventories and their constraints; contrast lives in these parameters (`phonetics-phonology.md:201`). *Artifact: manual-parameter chart.*
4. **Grammar in space** — decide spatial verb agreement, layout of discourse, and classifier use (§6). *Artifact: spatial-grammar sketch.*
5. **Contact and notation** — set loan-sign direction, mouthing, and whether the culture writes the language down (§10; `writing-systems.md`). *Artifact: notation sample and contact rules.*

| ID | Decision | Trigger | Failure if skipped |
|---|---|---|---|
| DR-SGN-01 | Fix the community type before any grammar | any sign-language brief | a full language built for an isolated signer, or a homesign imposed on a village |
| DR-SGN-02 | Set the iconicity budget before coining signs | lexicon work begins | an all-transparent "pantomime" stock — the disallowed frame — or an all-arbitrary stock that reads as a spoken conlang in disguise |
| DR-SGN-03 | Choose the manual parameter set (handshape × location × movement) before the lexicon | coining names | a lexicon that cannot be produced fluently or kept distinct in space |
| DR-SGN-04 | Decide notation and contact before any record or loan | literature, archives, bilingual settings | treating a notation as the language itself (`writing-systems.md:21`), or inventing loan signs with no source direction |

## 12. NON-CANON worked micro-example

**NON-CANON.** The Varn valley culture, its places, the signs below and every number are invented; nothing here is a claim about a real people, and canon belongs to lore-shokunin. Walking the §11 decision table: §3 typology — a shared village sign language used by deaf and hearing residents alike (S086, S087), plus a separate mourning alternate sign used by hearing women (S081); §4 ecology — congenital deafness concentrated in two kindreds (S086); §5 sublexical — the parameters below; §6 grammar in space — role markers placed at spatial loci (H, `calibration-registry.md:38`); §9 alternate — the mourning sign answers a speech ban whose substitutes follow `politeness-taboo-euphemism.md:118`; §10 contact/writing — a fingerspelled alphabet from the valley's script (S117), recorded in Stokoe-style parameter rows (S115).

| Sign(s) | Parameters (handshape · location · movement) | Walked through §11 |
|---|---|---|
| GRAIN; RIVER-DROP | flat-B palm · chin · outward tap; bent-1 · chest · downward arc | village shared sign language — §3, §5, §6 |
| MOURN | open-5 · shoulder · slow lowering, held | mourning alternate — §9, §10 |

## 13. Calibration bank

Codes per `calibration-registry.md:35-39` (R rejected, C contested, B bounded, H heuristic, T to-verify).

| Claim | Status | What to say instead |
|---|---|---|
| "There is one universal sign language" | R — no single signed code is universal (S085); International Sign is a contact register with a limited lexicon — the UN page calls it a pidgin (S077), most experts surveyed for WFD reject that label (S113) | name a specific signed language or a contact register |
| "Sign is pantomime or gesture" | R — sign languages are fully fledged natural languages, structurally distinct from spoken ones (S077); the pantomime view is the discredited first stage of sign research (S075) | write sign as language; keep gesture a separate channel |
| "A sign language is the spoken language on the hands" | R — each sign language has its own structure, grammar and lexicon, not a transcription of speech (S078) | give the signed language its own grammar |
| "Sign languages lack grammar" | R — WFD: "Each sign language has its own structure, grammar, and lexicon, equaling spoken languages in every respect" (S078) | describe the signed code's morphology and syntax |
| Shared-signing villages are idylls free of stigma | C — the "utopia" reading of Martha's Vineyard-type communities is itself under critical review (S118); attitudes, access and stigma vary by village | model the village's social field; stigma is a variable |
| First-language acquisition has a critical period | B for timing — late first-language exposure lowers ultimate attainment, even after decades of signing (S119); C for fixed cutoffs — researchers debate the slope and age windows | delay matters for a world's signing characters; no single "closure" birthday |
| More than 300 sign languages exist | B — "more than 300" is the UN page's figure (S077); Ethnologue lists 161 under its own rule (S120); WFD counts 200+ national sign languages, 40% legally recognised (S121) | quote the count and the counter; never a bare number |
| "deaf-mute", "dumb", "hearing-impaired" are neutral labels | R — WFD: these terms "are not acceptable"; preferred "deaf" or "deaf people" (S121); the US national association reports them rejected by the community (S076) | use deaf / Deaf (community), signers, sign languages |
| "Deaf culture" (capital D) is a community identity | B — WFD ties it to shared experience, language and cultural values (S078); capital D is the scholarly convention for communities whose major language is a sign language (S122) | capitalise for the community-cultural sense; lowercase deaf for audiological description |

**Living-practice flag.** Sign languages and Deaf communities are living practice: the UN calls early access to sign language vital to deaf people's development and stresses preserving sign languages as part of linguistic and cultural diversity (S077); WFD estimates more than 70 million deaf people belong to signing deaf communities (S121) and holds language and culture inseparable (S078). State rights as those bodies state them; write fictional communities *like* theirs, never *as* them.

**Precision traps.** "Sign language" is plural and local — hundreds of independent ones, none universal; sign is not gesture, not pantomime, not iconically transparent, not "spoken language on the hands"; "deaf-mute", "dumb" and "hearing-impaired" are rejected labels — say deaf or Deaf (community) and signers (S077, S078, S121).

## 14. Recheck

Before any signed language in a world becomes load-bearing — re-run the head's two sweeps before claiming the gap is still fresh; re-open S080 and S100 before citing an emergence date or word-order claim; re-open S085 before quoting ASL's status; re-read `adornment-body-codes.md:79` before separating an emblem from a sign; re-open S084 and S116 before prescribing a notation; re-open S077, S120 and S121 before quoting any count of sign languages; and re-read `syntax-typology.md:99` before asserting a word-order default.

## 15. Scope

Reference method and lane policy for the linguistics partition. This entry owns sign languages and other manual communication systems — deaf-community, village and emerging sign languages, homesign, alternate and manual codes, fingerspelling and notation — as conlang and worldbuilding method, and hands body-code etiquette, finger counting, word order and writing to their owners (§2). Handoff: lore-shokunin owns whether a signed language exists in-world, who uses it, and what Deaf culture and hearing-signer density look like there. Reference and method only.
