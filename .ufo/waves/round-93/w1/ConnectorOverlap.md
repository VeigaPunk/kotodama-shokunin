# Report — ConnectorOverlap (r93-w1, lane kotodama-shokunin, milestone r93-v1)

Read-only adjacency scan for claim C's new entry `corpus/knowledge/linguistics/greeting-leave-taking-formulae.md`. Full detail: `.ufo/waves/round-93/w1/stage/ConnectorOverlap/overlap-scan.md` (21 listed grep/find commands with match counts, owner table, quotes). All paths below relative to the lane repo. Read-only git; no production writes; no installs, pacman, or sysctls; scratch `/fast/scratch/hyaku/kotodama-r93/ConnectorOverlap` created and removed unused.

## Headline finding

The entry lands into a slot **pre-named by cross-reference but empty at base**: `culture-material/adornment-body-codes.md:5` routes "(greeting formulae, touch taboos…)" and `culture-material/costume-semiotics.md:143` routes "greeting formulae and address systems" into `linguistics/politeness-taboo-euphemism.md` and `linguistics/linguistic-anthropology.md` — but a term grep over `politeness-taboo-euphemism.md` returns **0** greeting/farewell/phatic lines, and `phatic` occurs exactly once corpus-wide (`linguistic-anthropology.md:100`, Malinowski 1923). This independently corroborates claims.json C.surface ("0 filename owners; 35+ topic-word hits are incidental"). The literal "access ritual" family has **zero** corpus hits; "contact-driven shift" machinery is owned by `language-contact.md:3` / `language-shift-obsolescence-revival.md:3`.

## Owner list (all kotodama-owned; no owner sits in another lane's province)

| Owner (file:line) | Overlapping claim | Status |
|---|---|---|
| linguistics/politeness-taboo-euphemism.md:3 | politeness theory + honorific grammar; advertised (by others) as greeting-formulae owner but holds 0 greeting lines | owned; dangling target |
| linguistics/linguistic-anthropology.md:100 | phatic communion, "talk that binds rather than informs" — sole corpus mention | owned |
| linguistics/gesture-co-speech-pointing.md:114,121 | greeting as emblem repertoire content (S215); :113 already bounds body-code to adornment-body-codes.md | owned |
| linguistics/language-socialization-and-acquisition.md:42 | greetings as acquired classroom routine (S742) | owned |
| linguistics/petitionary-and-votive-formulae.md:3 | formulae design-procedure template (S942–S948), divine addressees | owned; structural sibling |
| linguistics/sacred-registers-liturgical-language.md:3 | sacred high-variety register system | owned |
| linguistics/orality-formulaic-language.md:3 | oral-formulaic register design checklist (performance, not conversation) | owned |
| linguistics/sociolinguistics-registers.md:3 | diglossia/strata survey | owned |
| linguistics/language-contact.md:3; language-shift-obsolescence-revival.md:3 | contact strata; shift/revival life-cycle (the entry's "contact-driven shift" axis) | owned |
| linguistics/register-lexicon-ceilings.md:3 | mechanical-derivation ceiling constrains any mechanical greeting register | owned; latent constraint |
| myth-symbol/binding-speech-complex.md:4,93 | executor-bound speech; blessing row binds "the departing" | owned |
| myth-symbol/guest-right-hospitality-law.md:3,33,62 | sacral-legal hospitality bond; parting-gift end marker; address asymmetry rule | owned; nearest "access" ground |
| culture-material/adornment-body-codes.md:3,5 | bow gradients; dangling couples pointer "greeting formulae" | owned; contested |
| culture-material/costume-semiotics.md:142-143 | dangling pointer "greeting formulae and address systems" | owned; contested |
| culture-material/cuisine-food-lexicon.md:38,102 | "have you eaten yet?" greeting; kain tayo greeting/invitation | owned |
| culture-material/furniture-interior-lexicon.md:53,111 | seating regime determines "greeting geometry" | owned |
| synthesis/conlang-blueprint-template.md:178; urban-rural-register-ecology.md:42 | scene-checklist "greeting" row; "Reusable greetings" at the fair | owned |
| civilizations: amazonia-tupi-guarani.md:54; maori.md:60; japan-edo.md:115; pacific-northwest.md:98; india-classical-sanskrit.md:160; india-mughal.md:160; rapa-nui.md:63 | case-specific welcome/salutation/greeting-shift attestations (Léry; tikanga; Manu 2.122–28; Mughal prescribed salutation; ꞌiorana Tahitian contact layer) | owned per-case |
| myth-symbol/ritual-liminality.md:88; culture-material/funerary-material-culture.md:96 | welcome/send-off (mukaebi/okuribi) two-ended rite pair | owned |

Adjacent lanes: PROVINCE.md routes canon to lore-shokunin; the entry stays NON-CANON and hands off via `synthesis/worldbible-integration-contract.md`. Sibling lanes hold **nothing absorbable**: fleet-wide `grep -ril` (20 md hits outside kotodama) resolves to 19 false positives ("emp**hatic**ally" in game-dev-3d round-102/103/104 gate docs; "server **greeting**" in audio-shokunin round-90 PipeWire notes) and 1 config-key string (`mado-shokunin/corpus/knowledge/bind-table-r25.md:21`, Hyprlang `greeting = Hello, $NAME$SUFFIX.`).

## Contested items (report to integrator; production files read-only for seats)

1. **Two dangling couples pointers** (adornment-body-codes.md:5, costume-semiotics.md:143) promise a greeting-formulae owner that does not exist at base. After the entry lands, integrator should retarget both to the new file and add one reciprocal couples line from the entry — restoring couples-target resolution, changing no base row and no S-row.
2. **"Access rituals" topic clause** is corpus-ungrounded under that name; anchor to guest-right-hospitality-law.md (institution) + india-mughal.md:160 / india-classical-sanskrit.md:160 (prescribed salutation), each cited, or label "(design, not sourced)".
3. **"Contact-driven shift" clause** must cite language-contact.md / language-shift-obsolescence-revival.md for mechanism and spend S961–S964 on greeting-specific shift evidence only.

## Boundary sentences (paste-ready for the entry's limits section)

- "This entry owns greeting and leave-taking formulae as speech acts, their sequencing and their contact history; politeness logics, honorific grammar, taboo and euphemism remain politeness-taboo-euphemism.md."
- "The phatic function is invoked here as one unsourced line in linguistic-anthropology.md; this entry operationalizes it for opening/closing encounters with its own sourced rows and leaves the Hymes SPEAKING frame there."
- "Gestural and postural greeting stays adornment-body-codes.md and gesture-co-speech-pointing.md; this entry owns spoken, sung and written formulae and only cross-cites the body-side choreography."
- "How greeting routines are acquired stays language-socialization-and-acquisition.md; this entry treats formula systems, not developmental sequence."
- "Address to divine recipients stays petitionary-and-votive-formulae.md; this entry covers human-directed greeting/farewell and inherits only the house design-procedure shape."
- "Sacred high-variety competence stays sacred-registers-liturgical-language.md; greeting at a sacred threshold cites it for register allocation only."
- "Extended verbal art stays orality-formulaic-language.md; this entry's formulae are conversational phatic units, not composed performance."
- "Diglossia and stratification stay sociolinguistics-registers.md; the greeting register here is one ritual system, not a stratum survey."
- "Contact machinery and shift diagnostics stay language-contact.md and language-shift-obsolescence-revival.md; this entry owns only greeting-specific contact evidence and cites the machinery for mechanism."
- "Binding speech owns words with executors and sanctions; a greeting formula is non-binding phatic form and must not be granted contractual force — leave-taking blessings route through binding-speech-complex.md."
- "Guest-right owns the sacral-legal bond and its markers (threshold, parting gift); this entry owns only the spoken formulae accompanying opening and closing and inherits the address asymmetry as a boundary condition."
- "Civilization entries keep their case-specific attestation rows; this entry generalizes only on its own S961–S964 rows and cites, never restates, civilization evidence."
- "Commensality formulas stay cuisine-food-lexicon.md; seating-regime greeting geometry stays furniture-interior-lexicon.md; the welcome/send-off rite pair for the dead stays ritual-liminality.md and funerary-material-culture.md, cited as a two-ended design parallel only."
- "A mechanically derived fictional greeting register inherits register-lexicon-ceilings.md's ceiling measurement."

## Connector move (bounded)

Pair the landing with the integrator couples-repair above. Improves coverage (fills the advertised vacancy; repairs two dead pointers) with zero operability impact (no frozen tool/battery/mutant/control touched). Verify post-integration: re-run `tools/check-corpus-index.py` with claims C `index_args`, the v4 entry-mode regression leg on the round-92 landed entry, and the couples-targets sweep for the two edited files.

## Checks for the main agent

No builds or tests were run (read-only seat; nothing built). Verification commands named above belong to the integrator post-landing.
