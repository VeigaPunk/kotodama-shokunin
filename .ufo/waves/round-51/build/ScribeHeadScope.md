# ScribeHeadScope — Claim C: opening block and closing sections (head, §14 Recheck, §15 Scope)

- Seat: KotodamaR51a3.ScribeHeadScope (leaf; no delegation, no background jobs, no installs).
- Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin, branch main, base `bff83ba65bf9559af4d7567e81703059667a0005`; branch tip 5ab3634 adds only unused reports/round-51/calibration/ files.
- Date: 2026-10-22. Nothing in the lane was edited except this report (the C entry, README and SOURCES rows are not landed by this seat).

## 1. Assigned item

Draft for the C entry `corpus/knowledge/linguistics/sign-languages-manual-modality.md`: line 1 title + the eight head fields (`topic, gap filled, sources, couples, source, verified-at, recheck, scope`), then `## 14. Recheck` (3 lines) and `## 15. Scope` (3 lines with Handoff). Rerun the two gap sweeps at the lane worktree and report outputs. Name the partial owners cited one-way in §2 with live anchors. Open sources, return registry rows (NEW-ScribeHeadScope-N) and Gate lines. Pipe tables live in the body sections (other seats), per the two model entries (pastoralism/hunting) whose head/recheck/scope blocks contain none; this seat's blocks follow those models exactly.

## 2. Sweeps rerun at the lane worktree (2026-10-22)

```
$ find corpus/knowledge -iname '*sign-lang*' -o -iname '*gestur*' -o -iname '*kinesic*' -o -iname '*nonverbal*' | wc -l
0
$ grep -rliP '^- topic:.*\b(gestur|sign language|kinesic|nonverbal|non-verbal|body language|proxemic)' corpus/knowledge | wc -l
0
```

Both gap probes return 0, as declared in claims.json. Pre-entry census at the same tree: `find corpus/knowledge -name '*.md' | wc -l` → **226**; `ls corpus/knowledge/linguistics/*.md | wc -l` → **25** (required after landing: 227 and 26, sweep exit 0).

## 3. Partial owners verified with live anchors (each line re-read 2026-10-22)

| Partial owner | Anchor | Quoted support |
|---|---|---|
| `culture-material/adornment-body-codes.md` §7 | `:77` (`## 7. Gesture and posture — engineered gradients and their failure modes`), `:79` | "Ekman & Friesen (1969) classify nonverbal behavior into *emblems* (culture-specific gestures with dictionary meanings — the conlang-adjacent category)… Hall (1966) named proxemic distance bands (intimate/personal/social/public)." |
| `syntax-typology.md` | `:99` | "Claims that SOV is 'the human default' draw on emerging sign languages and homesign (e.g., Nicaraguan Sign Language research); suggestive, interpretively contested — don't assert it flat." |
| `numerals-and-measures.md` | `:107` | "**Finger counting** is culturally patterned, not universal… A fictional counting gesture system should be specified like any other body code." |
| `myth-symbol/direction-symbolism.md` | `:36` | "gestures are anchored to the world, not the body (Haviland 1993, 1998; Levinson 1997)." |
| `synthesis/multi-culture-creole-workshop.md` | `:24` | "Ad hoc contact jargon | recurring tasks but unstable conventions; repair by gesture, translation, repetition | …" |
| `linguistics/sound-symbolism.md` | `:29` | "embodied/articulatory: the mouth gesture or vocal effort mimics the referent" |

All anchors resolve at the lane worktree and support the gap-filled sentence.

## 4. Drafted head block (ready to paste; 12 lines)

```
# Sign languages and manual modality — a manual-visual channel as a full linguistic system: deaf-community sign languages, village and emerging sign languages, homesign, alternate and manual codes, fingerspelling, notation, and building a signed conlang

- topic: sign languages and other manual communication systems as a conlang and worldbuilding method — deaf-community sign languages, shared and village sign languages, emerging sign languages, alternate and manual codes, homesign, fingerspelling and notation; a sign language is a complete natural language, not gesture or pantomime; how the visual-manual channel shapes phonology (handshape, location, movement), morphology (simultaneity), syntax, iconicity and literacy; designing a signed conlang and its Deaf culture, hearing-signer communities and contact with spoken languages
- gap filled: no file in the corpus owns sign languages or manual communication systems as a method. Filename sweep `find corpus/knowledge -iname '*sign-lang*' -o -iname '*gestur*' -o -iname '*kinesic*' -o -iname '*nonverbal*' | wc -l` → **0**; topic sweep `grep -rliP '^- topic:.*\b(gestur|sign language|kinesic|nonverbal|non-verbal|body language|proxemic)' corpus/knowledge | wc -l` → **0** (both rerun 2026-10-22 at the round-51 declaration worktree, whose corpus bytes equal base `bff83ba…`). Partial owners keep their pieces and are cited one-way in §2: `culture-material/adornment-body-codes.md:77,:79,:93` (emblems and proxemics as body code), `syntax-typology.md:99` (the SOV-default caveat draws on emerging sign languages and homesign), `numerals-and-measures.md:107` (finger-count gesture systems), `myth-symbol/direction-symbolism.md:36` (pointing anchored to the world, not the body), `synthesis/multi-culture-creole-workshop.md:24` (repair by gesture in contact jargon).
- sources:
  - In-corpus anchors (`corpus/knowledge/`-relative `path:line`, each re-read at the round-51 declaration worktree on 2026-10-22): `culture-material/adornment-body-codes.md:77,:79,:93`; `syntax-typology.md:99`; `numerals-and-measures.md:107`; `myth-symbol/direction-symbolism.md:36`; `synthesis/multi-culture-creole-workshop.md:24`; `linguistics/sound-symbolism.md:29` (the mouth-gesture articulatory class).
  - External shelf — opened this round (2026-10-22), registered in `corpus/SOURCES.md` rows **S071–S0nn** (L1 renumbers the NEW-ids in §6); full locators and quotes in the round lesson's `## Gate`: NIDCD 2021 ASL fact sheet; Senghas et al. 2004 *Science*; Sandler et al. 2005 *PNAS*; Goldin-Meadow 2003 (*Psychology Press*, publisher description); SignWriting.org; The Makaton Charity.
- couples: linguistics — `syntax-typology.md` (owns word-order typology; its `:99` caveat rests on emerging sign languages — the evidence base is developed here); linguistics — `numerals-and-measures.md` (owns counting; finger-count gesture systems `:107` stay there, signed numeral morphology is designed here); linguistics — `semantic-fields-lexicon-building.md` (owns lexicon fields; a signed lexicon still fills fields, with manual word-formation rules supplied here); linguistics — `phonetics-phonology.md` (owns phonological theory; handshape/location/movement contrast per `:201` is the manual analogue); linguistics — `writing-systems.md` (owns scripts; fingerspelling and signed notation transcribe the manual modality, not a script type); linguistics — `translation-protocol-fidelity.md` (owns mediation; interpreters of signed languages are a live mediation case); linguistics — `conlang-methodology.md` (owns the artlang pipeline; this entry extends it to the visual-manual channel); culture-material — `../culture-material/adornment-body-codes.md` (owns emblems and proxemics as body codes, `:77,:79`; this entry owns language-grade manual systems); myth-symbol — `../myth-symbol/direction-symbolism.md` (owns pointing anchored to the world, `:36`); synthesis — `../synthesis/multi-culture-creole-workshop.md` (owns contact/jargon; repair-by-gesture `:24` is the interface).
- source: lane-side authority is the in-corpus anchor list above plus the external rows opened this round: **S071–S0nn** in `corpus/SOURCES.md`, each with URL, access date 2026-10-22, tier and the round lesson's located quote (NIDCD 2021; Senghas et al. 2004; Sandler et al. 2005; Goldin-Meadow 2003; SignWriting; Makaton). Design method: build the channel, then the grammar, then the lexicon — never a transliterated spoken language.
- verified-at: 2026-10-22 — written against the round-51 declaration worktree (corpus bytes equal base `bff83ba65bf9559af4d7567e81703059667a0005` per `reports/round-51/claims.json`). Measured at the lane worktree: filename sweep → **0**; topic sweep → **0**; `find corpus/knowledge -name '*.md' | wc -l` → **226**; `ls corpus/knowledge/linguistics/*.md | wc -l` → **25**; required after landing: 227 total, 26 linguistics, `python3 -B reports/round-28/readme/sweep.py` exit 0.
- recheck: before a signed language becomes load-bearing in a world — re-run the head's sweeps; re-open Senghas et al. 2004 (S0nn) and Sandler et al. 2005 (S0nn) before citing an emergence date or word-order claim; re-open the NIDCD sheet (S0nn) before quoting ASL's status; re-open SignWriting (S0nn) before prescribing a notation; re-read `adornment-body-codes.md:79` before assigning an emblem vs a sign; re-read `syntax-typology.md:99` before asserting a word-order default.
- scope: reference method and lane policy for the linguistics partition. This entry owns sign languages and other manual communication systems — deaf-community, village and emerging sign languages, homesign, alternate and manual codes, fingerspelling and notation — as conlang and worldbuilding method; it hands body-code etiquette to `../culture-material/adornment-body-codes.md`, counting to `numerals-and-measures.md`, word order to `syntax-typology.md` and writing to `writing-systems.md` (§2, §15). It decides nothing about any world and admits no culture into canon.
```

## 5. Drafted closing sections (ready to paste; 7 lines)

```
## 14. Recheck

Before any signed language in a world becomes load-bearing — re-run the head's two sweeps before claiming the gap is still fresh; re-open Senghas et al. 2004 (S0nn) and Sandler et al. 2005 (S0nn) before citing an emergence date or word-order claim; re-open the NIDCD sheet (S0nn) before quoting ASL's status; re-read `adornment-body-codes.md:79` before separating an emblem from a sign; re-open SignWriting (S0nn) before prescribing a notation; and re-read `syntax-typology.md:99` before asserting a word-order default.

## 15. Scope

Reference method and lane policy for the linguistics partition. This entry owns sign languages and other manual communication systems — deaf-community, village and emerging sign languages, homesign, alternate and manual codes, fingerspelling and notation — as conlang and worldbuilding method, and hands body-code etiquette, finger counting, word order and writing to their owners (§2). Handoff: lore-shokunin owns whether a signed language exists in-world, who uses it, and what Deaf culture and hearing-signer density look like there. Reference and method only.
```

Line budget: head 12 lines + closing 7 lines = 19 lines drafted; the entry's remaining budget (≤250) is held by sections 1–13 (other seats). Terminology is respectful throughout (deaf/Deaf community, signers, sign languages; no 'deaf-mute', no deficiency or pantomime framing). The draft names neither `corpus/lessons/round-51.md` nor `reports/round-51/boundary-count.py`.

## 6. Sources opened this round (2026-10-22) — registry rows ready after L1 renumbering (ids → S071 upward)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| NEW-ScribeHeadScope-01 | NIDCD, American Sign Language fact sheet — https://www.nidcd.nih.gov/health/american-sign-language | docs | A | ASL as a complete natural language; no universal sign language; fingerspelling | §What is American Sign Language? first paragraph; §Is sign language the same in other countries?; §How does ASL compare with spoken language? | ASL is a complete natural language with grammar that differs from English, expressed by movements of the hands and face; there is no universal sign language; fingerspelling spells out English words, each letter a distinct handshape | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeHeadScope-02 | Senghas, Kita & Özyürek 2004, Children creating core properties of language, Science 305(5691):1779–1782, doi 10.1126/science.1100199 — https://pubmed.ncbi.nlm.nih.gov/15375269/ | paper | A | emergence of Nicaraguan Sign Language across successive cohorts; not gesture | Abstract | successive cohorts extended the emerging signing and transformed it from an early gestural form into a linguistic system | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeHeadScope-03 | Sandler, Meir, Padden & Aronoff 2005, The emergence of grammar, PNAS 102(7):2661–2665, doi 10.1073/pnas.0405448102 — https://pmc.ncbi.nlm.nih.gov/articles/PMC548320/ | paper | A | Al-Sayyid Bedouin Sign Language: village/emerging sign language, systematic grammar within one generation, independent of ambient languages | Abstract; Discussion | a sign language arose in an isolated endogamous community with high incidence of recessive deafness; systematic grammatical structure emerged within one generation; word order differs from surrounding spoken and signed languages; many signers are hearing | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeHeadScope-04 | Goldin-Meadow 2003, The Resilience of Language, Psychology Press — https://www.routledge.com/The-Resilience-of-Language-What-Gesture-Creation-in-Deaf-Children-Can-Tell-Us-About-How-All-Children-Learn-Language/Goldin-Meadow/p/book/9781841694368 | book | B | the book's claims about homesign (publisher description; QUALITY criterion 6) | Description paragraph | deaf children without sign-language input gesture, and those gestures take on many of the forms and functions of language — the resilient properties | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeHeadScope-05 | SignWriting for Sign Languages (Valerie Sutton) — https://www.signwriting.org/ | docs | A | SignWriting as an existing notation/writing system for signed languages (maintainer statement, narrow scope) | home page banner/header | "Sign Languages are written languages!" — a written form for signed languages exists and is used across countries and sign languages | mined | 2026-10-22 | 90d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeHeadScope-06 | The Makaton Charity, What is Makaton? — https://makaton.org/TMC/TMC/About_Makaton/What_is_Makaton.aspx | docs | A | what Makaton is: an alternate/manual code supplementing speech (the organisation's own statement, narrow scope) | What is Makaton? page description (page body renders via script; the quote is the page's own description text) | Makaton is a communication programme using symbols (pictures), signs (gestures) and speech to enable people to communicate — a manual/alternate code, not a sign language proper | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |

Gate lines (for the round lesson's `## Gate`):

- NEW-ScribeHeadScope-01 — https://www.nidcd.nih.gov/health/american-sign-language — accessed 2026-10-22 — §What is American Sign Language? first paragraph: "ASL is expressed by movements of the hands and face."
- NEW-ScribeHeadScope-01 — https://www.nidcd.nih.gov/health/american-sign-language — accessed 2026-10-22 — §Is sign language the same in other countries?: "There is no universal sign language."
- NEW-ScribeHeadScope-02 — https://pubmed.ncbi.nlm.nih.gov/15375269/ — accessed 2026-10-22 — Abstract: "Successive cohorts of learners extended this procedure, transforming Nicaraguan signing from its early gestural form into a linguistic system."
- NEW-ScribeHeadScope-03 — https://pmc.ncbi.nlm.nih.gov/articles/PMC548320/ — accessed 2026-10-22 — Abstract: "In the space of one generation from its inception, systematic grammatical structure has emerged in the language."
- NEW-ScribeHeadScope-04 — https://www.routledge.com/The-Resilience-of-Language-…/9781841694368 — accessed 2026-10-22 — Description: "the children use their hands to communicate - they gesture - and those gestures take on many of the forms and functions of language."
- NEW-ScribeHeadScope-05 — https://www.signwriting.org/ — accessed 2026-10-22 — home page banner: "Sign Languages are written languages!"
- NEW-ScribeHeadScope-06 — https://makaton.org/TMC/TMC/About_Makaton/What_is_Makaton.aspx — accessed 2026-10-22 — What is Makaton? page description: "Makaton is a communication programme that uses symbols (pictures), signs (gestures) and speech to enable people to communicate."

## 7. URLs tried and failed

- De Gruyter Mouton, Zeshan & de Vos 2012 Village Sign Languages (10.1515/9781614511496): blocked by an anti-bot puzzle — not opened, not registered; Sandler et al. 2005 (NEW-ScribeHeadScope-03) and NIDCD cover the village/emerging ground instead.
- Cambridge Core, Brentari (ed.) 2010 Sign Languages: HTTP 429; MIT Press Bookstore page: HTTP 403 — not opened, not registered.
- Makaton deep link `/about-makaton` returned 404; corrected to the official `What is Makaton?` page (NEW-ScribeHeadScope-06).
- First PubMed guess for Senghas 2004 (PMID 15375271) resolved to an unrelated tomato-yield paper; corrected to PMID 15375269.

## 8. Result and unrun checks

Result: head block (12 lines) + §14 Recheck and §15 Scope (7 lines) drafted and ready to paste; sweeps rerun (0/0); six sources opened with registry rows and Gate lines; partial owners verified with live anchors. No tools installed (pacman paused host-wide; no install needed). Read-only lane commands only.

Unrun checks (L1's, after integration): full-entry `sweep.py` (rows 227, linguistics 26), provenance audit, couples resolver, S-id resolution, and the claims separability/freshness gates — none run here because this seat does not land the entry.
