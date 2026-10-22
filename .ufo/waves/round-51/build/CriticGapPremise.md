# CriticGapPremise — round 51 attempt 3, claim C premise attack

- Seat: KotodamaR51a3.CriticGapPremise (critic, leaf). Read-only. The only file written is this report.
- Lane state: HEAD is `1f97472` (the attempt-3 declaration commit on top of `5ab3634`), not `5ab3634` as the wave context says. `git diff --quiet bff83ba… HEAD -- corpus` succeeds, so every corpus `path:line` below is valid at base. `corpus/knowledge` holds 226 files, linguistics holds 25, and the entry path does not exist yet. `DR-SGN` appears only in `.ufo/waves/round-51/*` specs. The last SOURCES row is `S070` (`corpus/SOURCES.md:99`).
- Axes attacked: coverage (is the 227 real?), calibration, province and canon hygiene, separability.

## 0. Verdict

The gap is real, but the claim's gap evidence is mis-scoped. No file owns sign languages. However, gesture, emblems, proxemics and posture **are** owned: by `culture-material/adornment-body-codes.md` (H1 at line 1, section 7 at lines 77–94) and by `furniture-interior-lexicon.md:1` (seating posture). The claim's topic probe includes `gestur|kinesic|nonverbal|proxemic|body language`, and it returns 0 only because it reads `- topic:` lines and not the H1 or the body. C is therefore admissible **only** as an owner of signed languages and manual codes. It must never own gesture or nonverbal behaviour. The count 226 → 227 becomes hollow if the entry restates seven neighbour lines that the claim never listed (section 1), or if it leans on counts, idylls or clinical framing (section 3). None of these is a blocker. Each is fixable in drafting.

## 1. Is adornment-body-codes.md section 7 already an owner? Not of sign languages; yes of the emblem seam.

Read in full (lines 1–113).

| finding | evidence | consequence for C |
|---|---|---|
| Section 7 owns gesture as a body code: Ekman and Friesen's five classes, Morris's emblem geography, Hall's proxemic bands | `adornment-body-codes.md:79` "*emblems* (culture-specific gestures with dictionary meanings — the conlang-adjacent category)" | the emblem-to-sign seam is the contested border. C must cite :79 as the owner of emblems and define the test that separates a sign language from an emblem set |
| It owns posture gradients, embassy posture scenes and their table | `:80`, `:81`, `:83–90`, build step `:111` | C restates none of this |
| It owns gesture failure modes, including finger-number systems (Bede) | `:92` | finger counting is shared with `linguistics/numerals-and-measures.md:107`. C cites, does not own |
| It owns the expression-universality calibration (Barrett et al. 2019) | `:94` | C's calibration bank must not repeat it |
| It never mentions sign languages, deafness, fingerspelling or manual alphabets | bounded grep `\bsign(ed)? languages?\b` returns only `syntax-typology.md` and `sound-symbolism.md`. The 7 hits of `\b(sign\|deaf\|fingerspell)` in adornment are all `signature`, `signet` or plain "sign" | the gap is real for signed languages |
| H1 owns "Gesture and Posture" while the topic line says only "greeting and posture" | `adornment-body-codes.md:1`, `:3`. Also `furniture-interior-lexicon.md:1` "Seating Posture" | the claim's topic-only probe under-reads ownership (see C1 below) |

**Counterexample to the gap evidence (C1).** `gap_evidence_at_base` treats `gestur|kinesic|nonverbal|proxemic|body language` as unowned. `rg -n '^# .*(?i:gesture|posture)' corpus/knowledge` returns `adornment-body-codes.md:1` and `furniture-interior-lexicon.md:1`, and `:79` owns Hall's proxemics in its body. Smallest safe correction: in the entry's `- gap filled:` field, state the gap as **signed languages and manual codes**. Record the gesture probe words as "owned elsewhere (adornment-body-codes.md:1, :79)", not as evidence of a gap. Keep `gesture|kinesics|nonverbal|proxemic|body language` out of C's `- topic:` line. If one appears, it must sit in a "not … (owner …)" clause.

**Partial owners the claim missed (C2).** The claim names three partial owners. There are at least seven more, and each one is a "restates an existing owner" risk under the claim's own falsifier:

| neighbour (anchor) | what it owns now | C's boundary |
|---|---|---|
| `linguistics/phonetics-phonology.md:201` (to :203) | "Sign-language phonology works without acoustics — handshape, location, movement carry contrast (Sandler & Lillo-Martin 2006); deaf cultures need this layer." | the parent seed. C's planned section 5 develops the parameter inventory. It must add design decisions beyond :201, such as symmetry and dominance constraints, nonmanuals and inventory sizing, and say it extends :201 |
| `linguistics/phonetics-phonology.md:197–200` (section 7) | whistled and drum speech channels | speech surrogates stay there. C mentions them only as a contrast, in a boundary row |
| `linguistics/sound-symbolism.md:124` (and the source line :14) | "signed channels — iconicity is a general property, stronger in signed languages — Perniss et al. 2010 (to-verify)" | C's section 7 (iconicity) must cite :124 and not re-derive the general claim |
| `linguistics/linguistic-anthropology.md:22` | SPEAKING "I — Instrumentalities — Channel and codes/registers" | channel as part of the speech event stays there |
| `linguistics/writing-systems.md:21` | semasiography (Blissymbolics) separated from writing proper | the sign notation row (Stokoe notation, HamNoSys, SignWriting) must state whether each is writing or notation and cite :21 |
| `linguistics/language-contact.md:89–90` | the pidgin and creole definitions | International Sign and emergent-cohort grammar cite :89–90 for the frame and do not redefine pidgin or creole |
| `linguistics/taboo-strata-lifecycle.md:89–91` | "Negative strata and channel silence" | the only live anchor for "a speech ban moves meaning into another channel" (see C3) |

**C3 (the planned anchor does not support the row).** ScribeSec09 is told to couple alternate sign to `linguistics/politeness-taboo-euphemism.md` "for the speech ban". That file has no speech-ban, mourning-silence or widow-speech line. Its closest line, `:75`, is a taboo-domain inventory (death and corpses, names of the dead). Correction: anchor the row to `:75` as "death and names-of-the-dead taboo domains" only, or to `taboo-strata-lifecycle.md:89`. Never cite it as the owner of mourning speech bans.

**C4 (false-friend anchor).** `linguistics/sociolinguistics-registers.md:66` mentions Martha's Vineyard for Labov's vowel centralization, not for Martha's Vineyard Sign Language. Any C row that anchors shared signing there fails "anchored line supports the ownership cell".

**C5 (probe instrument hazard, the same class as round 50's `sherd`).** An unbounded `sign language` grep matches "de**sign language**" in 8 files under `corpus/knowledge`. The bounded `\bsign(ed)? languages?\b` matches 2. Every scribe or reviewer probe must use word boundaries.

**Sibling overlap: none.** I grepped every `*-shokunin/corpus/knowledge` and `PROVINCE.md` outside kotodama for `sign(ed) language(s)|deaf|fingerspell*|homesign`: 0 hits, and 0 hits in `lore-shokunin`. The nearest neighbour province is kake's web accessibility (`kake-shokunin/PROVINCE.md:24`, `:70–75`). C must not drift into captioning, interpreting services or media accessibility.

## 2. Province fit

The topic fits as conlang and worldbuilding method. `PROVINCE.md:3–7` covers "conlang design and diachronic staging", and `phonetics-phonology.md:201–203` already declares that "deaf cultures need this layer". The drift risk is in the **build plan itself** (`.ufo/waves/round-51/gen-build-spec.py`), not in the topic:

| planned item | drift | smallest safe correction |
|---|---|---|
| Section 4: "incidence and heredity of deafness" | clinical genetics. The ABSL abstract (NEW-CriticGapPremise-5) uses clinical language ("nonsyndromic, genetically recessive, profound prelingual neurosensory deafness") | say "a high, persistent proportion of deaf members across generations" as a design input. No aetiology, no gene names |
| Section 4: "schools and residential institutions", "oralism after the 1880 Milan congress" | education policy and history | allowed as transmission sites and in-world institutional attitudes. One dated, cited mention of Milan at most. No judgement on any method of teaching deaf children |
| Section 4: "endangerment of small sign languages" | rights and policy | cite `language-shift-obsolescence-revival.md:3` (transmission break) as the owner of shift. C adds only the modality-specific transmission sites |
| Section 13: "language rights stated as the cited bodies state them", sources from the UN day page and the WFD rights page | rights rulings. The UN page also bundles WHO hearing-loss statistics ("430 million people – require rehabilitation") | rights appear only as "<body> states … (S0nn)" inside the Living-practice flag. No legal-recognition counts and no CRPD obligations stated as the entry's own claims. The WHO clinical statistics never enter |
| Section 13: critical period, with Mayberry as the source | clinical or developmental advice | see trap T1. The row stays a calibration row and never becomes guidance |
| Section 12 NON-CANON: an invented valley with "a separate mourning alternate sign" | lifting one real community's practice wholesale | label it as a designer's pattern derived from a cited relation, per `synthesis/symbolism-consistency-rules.md:184` ("complete civilization context, not emblem shopping") |
| Handoff | canon | Scope hands off through `synthesis/worldbible-integration-contract.md:2`. A boundary row for "lore canon" needs that in-corpus anchor, because no lore file exists in the corpus |

## 3. Dangerous over-generalizations (calibration traps)

All web sources below were opened this session on 2026-10-22. Registry drafts are in section 6.

| # | trap | evidence | what the entry must say instead (status) |
|---|---|---|---|
| T1 | a critical period with a sharp age cutoff for first-language acquisition, given as advice | Mayberry and Kluender 2018 exists ("Rethinking the critical period for language…", *Bilingualism* 21(5):886–905, doi 10.1017/S1366728917000724). PubMed shows "No abstract available", and I could not open the full text | C: late first-language exposure in deaf signers is associated with lasting effects. The shape (cutoff or gradient) is debated. No age numbers and no prescriptions. Keep it `(to-verify)` until a wave-2 seat quotes the opened full text. Never cite isolated "feral child" cases as sign-language evidence |
| T2 | one bare number of sign languages | UN page: "more than 300 different sign languages", relaying WFD (NEW-1). Ethnologue: "Subgroup of 161 languages" = 131 deaf-community and 29 shared (NEW-2). Glottolog files them under "Pseudo Family: Sign Language" (NEW-9) | B: every count names its counting authority, its date and the counting rule. Never write "the Sign Language family". Families are lineages (LSF-derived, BANZSL) |
| T3 | the shared-signing village as an idyll | Kusters 2010 abstract: Martha's Vineyard is "a utopia in the eyes of many Deaf people", and the article "critically reviews the existing literature" (NEW-3) | C: shared signing is not equality. Stigma, marriage rules and pressure from schools can coexist with it. Martha's Vineyard Sign Language is historical, not present tense |
| T4 | the categories alternate, shared and deaf-community are settled | Ethnologue lists **Plains Indian Sign Language** and **Australian Aboriginal Sign Language** (both used by hearing people) under "Shared sign language" (NEW-2) | C: say that classification schemes disagree, and state which scheme the entry's typology follows |
| T5 | children invented a language from nothing, and its SOV order is "the human default" | Senghas et al. 2004 abstract: created "over the past 25 years", "from its early gestural form", with successive cohorts (NEW-4). Sandler et al. 2005 abstract: "without any apparent external influence" (NEW-5). `syntax-typology.md:99` already calibrates the SOV claim | C: emergence happens by cohorts, from homesign and contact at a school or within a community. Cite `syntax-typology.md:99` and do not re-assert the default. Read "no external influence" as the authors' claim, not a law |
| T6 | International Sign is a universal sign language | the UN page calls it "considered a pidgin form of sign language … limited lexicon" (NEW-1) | R for "universal sign language". C for the pidgin label (its status is debated, `(to-verify)` with a linguistic source). Cite `language-contact.md:89` |
| T7 | Plato's *Cratylus* 422e as evidence of a Greek deaf signing community | Fowler 1921 translation: "should we not try, as dumb people actually do, to make signs with our hands and head and person generally?" (NEW-6) | B: a hypothetical inside a naming argument. It shows that deaf people's signing was known, not that a sign language or community existed. Paraphrase as "deaf people" and keep the translator's word only inside the Gate quote |
| T8 | a manual alphabet exists everywhere | inference from T3 and T4: shared and alternate systems arise without a literate spoken-language base `[INFERENCE]` | B: fingerspelling presupposes contact with a written spoken language. Give the typology a "has a manual alphabet?" column, not an assumption |
| T9 | monastic sign and Plains sign as full languages, or "all Aboriginal Australians signed" | plan rows rest on publisher pages (Bruce 2007, Davis 2010, Kendon 1988, all tier B) | B: scope each row to its documented community and period. Lexicons used under vows of silence are not full grammars unless the source says so |
| T10 | iconicity always decays into arbitrariness, or sign is pantomime | `sound-symbolism.md:124`. Frishberg 1975 is planned | C for one-way decay. R for pantomime |
| T11 | the Deaf/deaf capital-letter convention as settled doctrine | planned terminology row | C: say which convention the entry uses and that its use is debated. Terminology is not a ruling |

## 4. What would make 227 hollow

1. **The counter is file-only.** `find … | wc -l` reaches 227 for any file, even a stray `.md`. It proves nothing alone.
2. **Restating owners (C2).** If sections 5, 7, 8 or 10 paraphrase `phonetics-phonology.md:201`, `sound-symbolism.md:124`, `syntax-typology.md:99` or `writing-systems.md:21`, the claim's falsifier "restates an existing owner's register" fires. If section 1 re-teaches the Ekman–Friesen classes or Hall's bands, it re-owns `adornment-body-codes.md:79`.
3. **Thin sourcing.** The plan pins sections 4, 7 and 9 on publisher pages (tier B). If a blurb's quote does not contain the asserted fact, the claim rests on an unopened book. It must carry `(to-verify)`, not an S-id.
4. **Fifteen H2s in about 230 lines.** That is roughly 13 lines per section. If the tables lack a design-consequence column, it is reference material, not craft (QUALITY items 3 and 4).
5. **Leftover drafting tokens.** `S071–S0nn` in the head, or `NEW-<Seat>-n` ids left behind. The §2.9-A forbidden-word regex does not catch `S0nn`.
6. **Dangling S-ids**, or a SOURCES row whose `used-by` cell lacks the entry.
7. **A hidden lesson coupling** through a relative path (`../../lessons/round-51.md`), which is the known blind spot of the separability checker.

## 5. Must-not list for claim C

1. Must not own or define gesture, emblems, kinesics, proxemics, posture or "nonverbal communication". Route them to `adornment-body-codes.md:79` and `:80`.
2. Must not put `gesture|kinesic|nonverbal|proxemic|body language` in `- topic:` except inside a "not … (owner …)" clause.
3. Must not re-teach whistled or drum surrogates (`phonetics-phonology.md:197–200`), finger counting (`numerals-and-measures.md:107`, `adornment-body-codes.md:92`), the SOV-default calibration (`syntax-typology.md:99`), or general iconicity (`sound-symbolism.md:124`). Cite them one-way.
4. Must not anchor Martha's Vineyard signing to `sociolinguistics-registers.md:66`, or mourning speech bans to `politeness-taboo-euphemism.md`. No such line exists there.
5. Must not state clinical content: aetiology, genes, degrees of hearing loss, devices, rehabilitation, or WHO hearing-loss figures.
6. Must not prescribe anything about deaf children's education, ages of exposure or teaching methods. It must not rule on the rights or legal status of any real language. Only "<body> states … (S0nn)" is allowed.
7. Must not print a bare count of sign languages or of deaf people. Every count names its authority, date and rule (T2).
8. Must not present any shared-signing community as an idyll or in timeless present tense (T3). Martha's Vineyard Sign Language is historical.
9. Must not call International Sign universal, call "Sign Language" a family, or call sign pantomime or the spoken language on the hands.
10. Must not use "deaf-mute", "deaf and dumb", "dumb", "hearing-impaired" or "suffers from" in the entry's own voice. The UN page caption uses "hearing-impaired", so do not paste captions.
11. Must not name `corpus/lessons/round-51.md` or `reports/round-51/boundary-count.py`, in any spelling or relative form.
12. Must not cite an unopened source as an S-id, or leave `S0nn` or `NEW-` tokens.
13. Must not decide canon. The NON-CANON example says the culture, signs and numbers are invented and does not lift one real community's practice wholesale (`symbolism-consistency-rules.md:184`).

## 6. Falsifiers for wave 2

Run these in the integrator's clone, from the lane root, after integration. Each one fails the claim, or the named section, if its expectation is not met.

| id | check | expected |
|---|---|---|
| F1 | `find corpus/knowledge -name '*.md' \| wc -l` and `git diff --name-status bff83ba65bf9559af4d7567e81703059667a0005 -- corpus/knowledge` | `227`. Exactly one line, `A corpus/knowledge/linguistics/sign-languages-manual-modality.md`, with no `M` lines |
| F2 | `grep -P '^- topic:' E \| grep -oiP '\b(gesture\w*\|kinesic\w*\|nonverbal\|non-verbal\|proxemic\w*\|body language)\b'` (E = entry) | empty, or each hit sits in a "not … owner" clause (reviewer reads it) |
| F3 | the boundary table contains rows anchored at `adornment-body-codes.md:79`, `phonetics-phonology.md:201`, `sound-symbolism.md:124`, `syntax-typology.md:99`, `numerals-and-measures.md:107`, `writing-systems.md:21`, `language-contact.md:89`, plus a handoff row at `worldbible-integration-contract.md:2`. Every `file.md:N` resolves (unique basename under `corpus/knowledge`, N ≤ the line count) and the quoted needle sits on line N | all present and resolving |
| F4 | restatement probes on E: `rg -n -i 'illustrators\|affect displays\|regulators\|adaptors\|intimate distance\|eshaku\|keirei\|Silbo\|Kuşköy\|talking drum\|Bede'` | hits only inside boundary rows that cite the owner |
| F5 | clinical, education and rights probe: `rg -n -i '\b(cochlear\|implant\|audiolog\w*\|hearing loss\|hearing aid\|decibel\|GJB2\|connexin\|syndrom\w*\|rehabilitat\w*\|therapy\|intervention\|should (be taught\|learn)\|must (be taught\|learn)\|ratif\w*\|obligat\w*)' E` | 0 outside the calibration bank's "What to say instead" cells and the Precision traps paragraph |
| F6 | terminology: `rg -n -i "deaf-mute\|deaf and dumb\|\bdumb\b\|hearing-impaired\|suffer" E` | 0 |
| F7 | counts: `rg -n -i '\b[0-9]{2,3}\b[^|]{0,60}sign languages' E`. Each hit line also matches `S0[7-9][0-9]` and one of `Ethnologue\|WFD\|Glottolog\|World Federation` | every hit passes |
| F8 | critical period: `rg -n -i 'critical period\|sensitive period\|late first-language\|deprivation' E`. Hit lines must not match `\bage[sd]? [0-9]\|by (age )?[0-9]\|[0-9]+ years old\|should\|must` | no forbidden co-occurrence. The bank row status is C or B. Load-bearing content is `(to-verify)` unless the full text was opened |
| F9 | idyll: if E matches `Martha's Vineyard\|Adamorobe\|Kata Kolok\|Al-Sayyid\|shared sign`, then E has a bank row with status C on shared signing that cites the Kusters 2010 row, and no sentence puts Martha's Vineyard signing in the present tense | holds |
| F10 | `rg -n -i 'universal sign\|the sign language family\|pantomime' E` | hits only in rows with status R |
| F11 | taxonomy: the typology table or the bank states that classification schemes disagree (Ethnologue's "Shared" bucket holds Plains Indian Sign Language and Australian Aboriginal Sign Language) | present |
| F12 | ReviewEntryContract §2.9-A with the path swapped to E and the README row `sign-languages-manual-modality.md` | `PASS` |
| F13 | §2.9-B with `REL=` set to E | `[]`. Every cited id is S071 or above |
| F14 | `rg -n 'NEW-\|S0nn\|S07x\|lessons/round-51\|round-51\.md\|boundary-count' E` plus the README added lines (also try `\.\./\.\./lessons`) | 0 |
| F15 | `python3 -B reports/round-28/readme/sweep.py` | exit 0, rows 227, files 227, `topic_mismatch 0 []`, `footer_ok True`, linguistics 26 |
| F16 | tier audit: for each S-id that E cites, read the SOURCES tier. Each domain section from 3 to 10 has at least one row that is primary (tier A, or an opened abstract of the original paper), and every publisher-page (B) row's Gate quote contains the fact it supports | holds, or the claim is downgraded to `(to-verify)` |
| F17 | non-author restatement review: diff E's sections 5, 7, 8 and 10 against `phonetics-phonology.md:201–203`, `sound-symbolism.md:124`, `syntax-typology.md:99` and `writing-systems.md:21` | each section adds at least one design decision absent from its parent line, and the boundary row says "extends" |
| F18 | usability: every domain section table has a design-consequence or "and check" column | 8 of 8 domain sections |
| F19 | `wc -l E` | ≤ 250 |

## 7. Sources opened this session (registry drafts; the L1 renumbers)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| NEW-CriticGapPremise-1 | United Nations, "International Day of Sign Languages" observance page | docs | B | count of sign languages and deaf people as relayed from WFD; the UN description of International Sign | section "How many people are deaf worldwide?" | counts are relayed advocacy figures with an authority and must be cited as such; International Sign is "considered a pidgin form" | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-CriticGapPremise-2 | Ethnologue Free, "Sign language" subgroup page | dataset | A | Ethnologue's own count and subgrouping of sign languages | page header and the subgroup headings "Deaf community sign language 131", "Shared sign language 29" | 161 by Ethnologue's rule against 300+ by WFD's. Ethnologue files Plains Indian and Australian Aboriginal Sign Language as "Shared" | mined | 2026-10-22 | on-release | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-CriticGapPremise-3 | Kusters, A. (2010), "Deaf utopias? Reviewing the sociocultural literature on the world's 'Martha's Vineyard Situations'", *Journal of Deaf Studies and Deaf Education* 15(1), doi 10.1093/deafed/enp026; Europe PMC record | paper | B | critique of idyllic readings of shared-signing communities (abstract only) | abstract, sentence 1 | shared-signing villages are read as utopias, and the literature is critically reviewed | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-CriticGapPremise-4 | Senghas, Kita and Özyürek (2004), "Children creating core properties of language: evidence from an emerging sign language in Nicaragua", *Science*, doi 10.1126/science.1100199; Europe PMC record | paper | B | emergence of Nicaraguan Sign Language by cohorts (abstract only) | abstract, sentence 1 | emergence over about 25 years, from gestural form, by successive cohorts | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-CriticGapPremise-5 | Sandler, Meir, Padden and Aronoff (2005), "The emergence of grammar: systematic structure in a new language", *PNAS*, doi 10.1073/pnas.0405448102; Europe PMC record | paper | B | Al-Sayyid Bedouin Sign Language word-order emergence (abstract only) | abstract, sentence 1 | "no external influence" is the authors' claim. The abstract's clinical wording is not design material | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-CriticGapPremise-6 | Plato, *Cratylus* 422e, translated by H. N. Fowler (1921), Perseus Digital Library | book | A | what the *Cratylus* text says at 422e (in this translation) | Crat. 422e | a hypothetical about signing, inside a naming argument | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-CriticGapPremise-7 | World Federation of the Deaf, "Deaf Human Rights" page | docs | A | WFD's own statement of its advocacy topics (not a ruling) | section "WFD Policy and Letters of support" | recognition, interpreting and education are advocacy topics, which is evidence for the must-not on rights rulings | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-CriticGapPremise-8 | Mayberry and Kluender (2018), "Rethinking the critical period for language: New insights into an old question from American Sign Language", *Bilingualism: Language and Cognition* 21(5):886–905, doi 10.1017/S1366728917000724; Europe PMC search record | paper | B | bibliographic existence only. No content claim (full text not opened) | Europe PMC record title field | the critical-period row stays `(to-verify)` until the full text is opened | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-CriticGapPremise-9 | Glottolog 5.3, languoid sign1238 | dataset | A | Glottolog's classification status of sign languages | page heading | sign languages are a pseudo-family, not a genealogical family | mined | 2026-10-22 | on-release | corpus/knowledge/linguistics/sign-languages-manual-modality.md |

Gate lines:

- NEW-CriticGapPremise-1 — https://www.un.org/en/observances/sign-languages-day — accessed 2026-10-22 — section "How many people are deaf worldwide?": "Collectively, they use more than 300 different sign languages."
- NEW-CriticGapPremise-2 — https://www.ethnologue.com/subgroup/2/ — accessed 2026-10-22 — page header under "Sign language": "Subgroup of 161 languages"
- NEW-CriticGapPremise-3 — https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/deafed/enp026&resultType=core&format=json — accessed 2026-10-22 — abstract, sentence 1: "known as a community where "everyone signed" for several hundred years, a utopia in the eyes of many Deaf people."
- NEW-CriticGapPremise-4 — https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Children%20creating%20core%20properties%20of%20language%22&resultType=core&format=json — accessed 2026-10-22 — abstract, sentence 1: "A new sign language has been created by deaf Nicaraguans over the past 25 years"
- NEW-CriticGapPremise-5 — https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Emergence%20of%20grammar%20systematic%20structure%20in%20a%20new%20language%22&resultType=core&format=json — accessed 2026-10-22 — abstract, sentence 1: "a language created spontaneously without any apparent external influence in a stable existing community"
- NEW-CriticGapPremise-6 — https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Crat.:page=422 — accessed 2026-10-22 — Crat. 422e: "should we not try, as dumb people actually do, to make signs with our hands and head and person generally?"
- NEW-CriticGapPremise-7 — https://wfdeaf.org/our-work/human-rights-of-the-deaf/ — accessed 2026-10-22 — section "WFD Policy and Letters of support": "The advocacy work covers topics like national sign language recognition, deaf people’s right to drive, professional sign language interpreter training and funding"
- NEW-CriticGapPremise-8 — https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1017/S1366728917000724&resultType=core&format=json — accessed 2026-10-22 — title field: "Rethinking the critical period for language: New insights into an old question from American Sign Language."
- NEW-CriticGapPremise-9 — https://glottolog.org/resource/languoid/id/sign1238 — accessed 2026-10-22 — page heading: "Pseudo Family: Sign Language"

Failed or partial opens: the OUP article page for Kusters 2010 timed out; PubMed search for Kusters returned 403; the Europe PMC full text of Mayberry and Kluender (PMC6329394) returned no body; the Europe PMC article page timed out. The Glottolog page rendered no member counts.

## 8. Unrun checks and tooling

- Not run: every F-check (no entry exists yet), separability, the sweep in a clone, and §2.9-A and §2.9-B. No sandbox clone was made.
- Read-only commands used: `git log`, `git diff --stat`, `git diff --quiet`, `git rev-parse`, `git status --short`, `rg`, `sed -n`, `ls`, `find`, `test -e`, plus `curl` and `python3` against Europe PMC (output read in memory, nothing written into the lane).
- Installs: none.
