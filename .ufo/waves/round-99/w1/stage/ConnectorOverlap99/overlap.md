# ConnectorOverlap99 — round 99 adjacency scan: praise poetry / panegyric

- Seat: ConnectorOverlap99 (leaf, read-only). Lane base `527df3fee305b3454446946e6779ece45456307e`; claims frozen at `b1b80562edfc8f6082aec74bbbf0f25e152708a8`.
- Question: does any sibling lane, or any other kotodama entry, already own the surface claim C opens at `corpus/knowledge/linguistics/praise-poetry-panegyric.md`?
- Answer: **no sibling lane claims it** (21/21 no overlap); **9/9 named in-lane neighbours are boundary-to-respect**; **3 items routed as contested scope** (two general claims already written inside other entries, one case-pair that holds the prior art for "patronage and reward"). The entry path does not exist at base (`test -e` rc 1).
- C8-equivalent sweep run with the frozen counter's own functions (`tree_knowledge`, `sweep_owners`, `PHRASES`, `ENTRY_REL` imported from `reports/round-99/predispatch.py`): **files 270, owners 0, rc 0**. So the counter's guard passes at base; nothing below is a C8 risk. Everything below is reviewer-level duplication risk, which C8 (topic line + headings only, `predispatch.py:56,581-587`) does not measure.

## 0. Commands and numbers

| # | command (cwd = lane root unless noted) | result | rc |
|---|---|---|---|
| 1 | `ls -d /home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md \| wc -l` | 21 | 0 |
| 2 | per-term `grep -icE` over all 21 sibling `PROVINCE.md` + 19 `SKILL.md` (audio and game-dev-2d have no SKILL.md): praise / panegyric / bard / epithet / poetry | 0 / 0 / 0 / 0 / 0 | 0 |
| 3 | same, `genealog` | 2, both in `kotodama-shokunin/SKILL.md:792,821` (Akkadogram; name-derivation) — sibling-only 0 | 0 |
| 4 | same, `\boral\b` | 17 lines / 8 sibling files, all the "no-oral-context" evidence idiom | 0 |
| 5 | same, `performance` | 15 lines / 6 sibling files, all Core-Web-Vitals / eval / rendered-output sense | 0 |
| 6 | `for lane in */; do grep -rliE 'praise\|panegyric\|\bbardic\b\|\bgriot\b\|\bskald\|encomium\|oral poetry\|oral literature' $lane/corpus/knowledge; done` | kotodama 54 files; revenger 1 (false positive, RE4B textbook row `round-73-re-resource-atlas.md:381`); all other lanes 0 | 0 |
| 7 | six frozen phrases over fleet `research/ templates/ tools/ counters/ history-recheck/ exp-full/ st2/ wt2/` | 0 files each | 0 |
| 8 | frozen-counter sweep (see header) | files 270, owners 0 | 0 |
| 9 | `test -e corpus/knowledge/linguistics/praise-poetry-panegyric.md` | absent | 1 |
| 10 | `grep -c 'S1007\|S1008\|S1009\|S1010' corpus/SOURCES.md` | 0 | 1 |

## 1. Sibling lanes — verdict per owner

No sibling lane claims the praise/panegyric surface. The only corpus-level hits are three non-owners, listed after the table.

| Lane | What its PROVINCE owns (line) | Verdict |
|---|---|---|
| lore | fictional-world records, canon, consistency (PROVINCE:3-9) | no overlap — canon is lore's; this entry is reference craft and hands off |
| chousa | deep-research method, source hierarchy, claim-vs-source (PROVINCE:3-10) | no overlap — research method; the entry cites chousa-grade evidence, owns no method |
| kotoba | prompt & skill craft, SKILL.md/AGENTS.md quality (PROVINCE:3-6) | no overlap — prompt craft, not worldbuilding content |
| audio | game audio production, SFX/ambience (PROVINCE:3-13) | no overlap — sound assets, not verbal art |
| game-dev-2d | 2D game production, headless fixtures (PROVINCE:3-10) | no overlap — mechanics; "performance" hit is rendered-output (PROVINCE:23) |
| game-dev-3d | 3D game production (PROVINCE:3-33) | no overlap — "oral" hit is the no-oral-context idiom (SKILL:17) |
| kagi | secrets & vault ops (PROVINCE:3-6) | no overlap |
| kaidoku | reverse engineering of shipped artifacts (PROVINCE:3) | no overlap |
| kake | web properties & publishing (PROVINCE:3-5) | no overlap — "performance" = field CWV (PROVINCE:24-25) |
| kama | local model serving & endpoint health (PROVINCE:3-6) | no overlap |
| kasegi | bounty & security research (PROVINCE:3) | no overlap |
| kengaku | LLM/model research & evaluation (PROVINCE:3-5) | no overlap — "performance" = model/eval (PROVINCE:260); "No oral tradition." (SKILL:21) is an evidence-discipline line |
| kumitate | orchestration & tooling (PROVINCE:3-5) | no overlap — the only "bard" in any lane corpus is Google Bard, `corpus/knowledge/cost-and-profile.md:332` |
| mado | desktop & compositor craft (PROVINCE:3-6) | no overlap |
| mori | fleet & host observability (PROVINCE:3-6) | no overlap — "performance" = clock/measurement (SKILL:1348) |
| revenger | reverse engineering of shipped artifacts (PROVINCE:3) | no overlap — hit is a book-atlas row |
| souji | fleet repo & workspace hygiene (PROVINCE:3-6) | no overlap |
| tabi | browser & web-interaction craft (PROVINCE:3-6) | no overlap — "performance" = Lighthouse/CWV (SKILL:2922) |
| tameshi | (PROVINCE:1-3) | no overlap |
| tsukuroi | host OS/package/boot diagnosis | no overlap — 8 "oral" hits are the no-oral-context idiom |
| kotodama (self) | linguistic-cultural worldbuilding craft (PROVINCE:3-17) | owns the surface by design; refuses canon (lore), research method (chousa), prompt craft (kotoba) |

Non-owner corpus hits, named so they are not mistaken for claims:
- `chousa-shokunin/corpus/captures/c9d1e74c3ac8d9eb332c9770.txt:719` — a captured MEDLINE retrieval page; a source capture, not lane knowledge.
- `kumitate-shokunin/corpus/knowledge/cost-and-profile.md:332` — `bard` as the Google Bard model needle.
- `revenger-shokunin/corpus/knowledge/round-73-re-resource-atlas.md:381` — "Reverse Engineering for Beginners" atlas row.

Could not read: `art-east-asian-design` is named as a lane in `lore-shokunin/PROVINCE.md:9` and `game-dev-2d-shokunin/PROVINCE.md:10` but has **no directory** under the fleet root (`ls -d art-east-asian-design` rc 2). `kumitate-shokinin/` (typo dir) contains an **empty** `kumitate-shokunin/` and no PROVINCE.md/SKILL.md.

## 2. The nine named in-lane neighbours — one boundary sentence each

| Entry (anchor) | What it already owns | Boundary the new entry must respect |
|---|---|---|
| `linguistics/orality-formulaic-language.md:56` §3 "Epithets and praise-names: the formula lexicon"; bullet at `:60` | the epithet as metrical slot-filler; praise-name as compressed formula; one bullet already states "Praise poetry as social formula: Yoruba oríkì (Barber 1991) and Nguni izibongo (Opland 1983) … the epithet system promoted to a social institution" | orality owns the **formula lexicon** (slot, meter, aptness-independence, traditional referentiality); the new entry owns the **institution around the recitation** and must cite `:60` rather than re-describe oríkì/izibongo. |
| `linguistics/naming-systems.md:73` §4 Theonymy | cult epithets as theonym+epithet (Athena Polias/Nike; Burkert 1985) | divine cult epithets stay there; the new entry's praise epithet is person/lineage/office-directed, not a god's cult title. |
| `linguistics/verbal-duelling-ritual-insult.md:18` §1 scope, `:110` §6 boast formula | the contest frame, boast/taunt/riposte grammar, adjudicating audience; §1 already defers the formulaic machinery to orality | boasts, flyting and the contest frame stay there; the new entry's "rivalry, satire" is praise-side (patron competition, counter-praise, the flattery limit), not a word-contest. |
| `linguistics/funerary-lament-dirge-formulae.md:15` §1 scope, `:133` §6 | the mourning register and "praise of the dead" as one of its formulaic contents | praise of the **dead** inside the dirge stays there; the new entry takes praise of the living (person, lineage, office, place). |
| `linguistics/toast-drinking-speech-formulae.md:21` §1 scope, `:122` §5 | the toastmaster's office and the order of a toast sequence | the cup-borne office/order stays there; the new entry's "order of a praise performance" is a distinct occasion and must not borrow the toast sequence. |
| `linguistics/linguistic-anthropology.md:9` §1 SPEAKING grid, `:91` §5 | the ethnography-of-communication method and special registers | the SPEAKING grid is the **method** the new entry applies — cite it, do not re-derive participants/setting/act-sequence. |
| `myth-symbol/sacred-kingship-mythic-charter.md:150` §8.5 "Praise-recitation as performed pedigree", `:158` §9 | praise recitation as royal legitimation, the reciter as an office, the titulary, pedigree curation by "the priests, the bards, and the archivists" | the **royal-register use** (charter auditable through recitation, titulary, genealogy rewriting) stays there; the new entry may cite the royal case but owns no charter and no legitimation channel. |
| `myth-symbol/heraldry-emblems-identity-marks.md:18` §2 one-owner boundary (routes name slots to `naming-systems.md:46`) | the carried, granted, inherited mark and its bearer unit | the **carried** mark stays there; a praise epithet is spoken, not borne on a shield, seal or garment. |
| `myth-symbol/hero-journey-variants.md:59` §3 | the hero pattern and the fossilized founding formula ("a royal epithet, a name-compound, a fixed line in the founding recitation") | the hero pattern stays there; the new entry may use a royal epithet only as a bearer-tied epithet case, never as a pattern claim. |

## 3. Further in-lane owners found by the scan (not in the nine)

| Entry (anchor) | What it owns | Boundary |
|---|---|---|
| `civilizations/yoruba.md:78` "Oríkì: praise, memory, and an economy of recognition"; `:84` oríkì economy; `:86-90` relation table | the Yoruba case, incl. patronage, gifts, reciprocal expectation, and praise that is not bland flattery (`:83`) | the Yoruba case and its economy table stay there; the new entry cites it for Barber's evidence and adds only the comparative layer. |
| `civilizations/mali-songhai.md:50` "Jeli oral archives: registers, rights, and interested memory"; `:53`; `:59-64` table | the Mande jeli case: genealogy, praise, mediation, patronage, public praise with reward, admonitory court performance, "Praise is assumed to exclude criticism" (`:64`) | the Mande case stays there; do not restate jeliw/jelimusow detail as general theory. |
| `civilizations/parthia.md:165` "Gōsān: calibrate the evidence before designing a bardic institution" | the Parthian minstrel reconstruction and its evidence grading | the gōsān case and its calibration stay there; cite as one bardic-institution case. |
| `civilizations/germanic-norse.md:72` "Eddic/skaldic verse economy"; `:77` dróttkvætt "dense praise … named poets and patrons often matter" | the skaldic case and its meter/economy table | the skaldic case stays there. |
| `civilizations/zimbabwe-shona.md:87` "Mutupo…"; `:90` chidawo | praise/address designation as a clan/branch identity form | praise address as a **clan designation** stays there; the new entry's praise epithet is not a clan name. |
| `civilizations/polynesia-navigation.md:142` "Oral genealogy: whakapapa-style precision without false chronometry" | genealogical recitation's precision axes, performance context, authority of transmission | the Polynesian case and its precision rules stay there; the new entry's "genealogical recitation" is the praise-performance component that recites a patron's line. |
| `civilizations/hawaii.md:51`, `civilizations/maori.md:85` | cosmogonic/chiefly genealogy as a knowledge frame | those charts stay there. |
| `culture-material/dance-performance-movement-codes.md:20` | performance as embodied code (movement vocabulary, role codes) | the moving body stays there; the new entry owns the **verbal event order** of a praise performance. |
| `linguistics/sacred-registers-liturgical-language.md:3` | recitation competence and authorization in a sacred register | liturgical recitation stays there; praise recitation at a court is not a sacred register. |

Pattern note (useful for the new entry): this lane's convention is that **each genre entry owns its own performer office** — keener `funerary-lament-dirge-formulae.md:56` §3, toastmaster `toast-drinking-speech-formulae.md:122` §5, spokesman `sacred-kingship-mythic-charter.md:148` §8.3. A praise-singer office in the new entry follows that convention; it is not a second owner of those offices.

## 4. Contested scope — routed to the L1, not absorbed

1. **`linguistics/orality-formulaic-language.md:60` already states the institution thesis.** The bullet says praise poetry is "the epithet system promoted to a social institution" and names oríkì/izibongo. The claim's boundary sentence assigns orality only "praise-names as formula lexicon", but the written line goes past the lexicon. Decision needed: the new entry must cite `:60` as prior art and add only the office/patronage/reward/order/audience/rivalry layer — or the boundary sentence needs restating. C8 will not catch a restatement (topic lines and headings only).
2. **`myth-symbol/sacred-kingship-mythic-charter.md:150` already claims "the reciter as an office" and praise-recitation as performed pedigree**, and `:158` names "the priests, the bards, and the archivists" as genealogy curators. The new entry's "praise singer's office" and "genealogical recitation" therefore have a general-claim owner. Decision needed: patron scope (ruler vs any patron) as the dividing line, with the royal case cited and not re-derived.
3. **The praise economy is already written at case level in two entries** — `civilizations/yoruba.md:84-90` (patronage, gifts, reciprocal expectations) and `civilizations/mali-songhai.md:59-64` (public praise invites recognition or reward; admonitory performance; praise does not exclude criticism). The new entry's frozen topic carries "patronage and reward" and "rivalry, satire and the limits of flattery". Decision needed: whether the entry may cite both cases and add only the comparative layer, or whether those two clauses need narrower headings so the entry does not read as a third telling of the same two cases.

## 5. Files I could not read

- `art-east-asian-design/` — no such directory (rc 2), though two sibling PROVINCE files name it as a lane.
- `kumitate-shokinin/kumitate-shokunin/` — empty; no PROVINCE.md or SKILL.md.
- Nothing else: all 21 sibling PROVINCE.md files and all 19 sibling SKILL.md files opened (audio and game-dev-2d have no SKILL.md; `ls *-shokunin/SKILL.md | wc -l` = 19, rc 0); all nine named entries plus the nine additional in-lane owners opened at the cited ranges.
