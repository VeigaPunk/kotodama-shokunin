# ConnectorOverlap99 — round 99 report (adjacency scan: praise poetry / panegyric)

- Seat: ConnectorOverlap99, leaf, read-only. Lane base `527df3fee305b3454446946e6779ece45456307e`; claims frozen at `b1b80562edfc8f6082aec74bbbf0f25e152708a8`.
- Main output: `.ufo/waves/round-99/w1/stage/ConnectorOverlap99/overlap.md`, 14431 B, sha256 `db67b15276bacf51b585964cd11258bb67f4bfeb0a33da2c16c40435f3308bde` (`sha256sum`, rc 0; `wc -c`, rc 0).
- Nothing written outside my stage; no git/jj command run; no model chosen; no package installed (tooling: none).

## Verdict in one line

No sibling lane claims the praise/panegyric surface; all nine named in-lane neighbours are boundary-to-respect; three items are routed to the L1 as contested scope (two general claims already written inside other entries, one case-pair holding the prior art for "patronage and reward"). The frozen counter's own C8 sweep returns owners 0 over 270 knowledge files, so none of this is a leg risk — it is reviewer-level duplication risk.

## Commands and numbers (all rc 0 unless stated)

| # | command | result |
|---|---|---|
| 1 | `ls -d /home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md \| wc -l` | 21 |
| 2 | per-term `grep -icE` over all 21 sibling `PROVINCE.md` + 19 `SKILL.md` (audio and game-dev-2d have no SKILL.md): praise / panegyric / bard / epithet / poetry | 0 / 0 / 0 / 0 / 0 |
| 3 | same, `genealog` | 2 lines, both `kotodama-shokunin/SKILL.md:792,821` (Akkadogram; name derivation) — sibling-only 0 |
| 4 | same, `\boral\b` | 17 lines / 8 sibling files, all the "no-oral-context" evidence idiom (e.g. `kengaku-shokunin/SKILL.md:21` "No oral tradition.") |
| 5 | same, `performance` | 15 lines / 6 sibling files, all CWV / eval / rendered-output sense (`kake PROVINCE:24-25`, `tabi SKILL:2922`, `kengaku PROVINCE:260`, `game-dev-2d PROVINCE:23`, `mori SKILL:1348`) |
| 6 | `grep -rliE 'praise\|panegyric\|\bbardic\b\|\bgriot\b\|\bskald\|encomium\|oral poetry\|oral literature' <lane>/corpus/knowledge` for every lane | kotodama 54 files; revenger 1 false positive (`round-73-re-resource-atlas.md:381`, RE4B textbook); all other lanes 0 |
| 7 | six frozen phrases over fleet `research/ templates/ tools/ counters/ history-recheck/ exp-full/ st2/ wt2/` | 0 files each |
| 8 | import `reports/round-99/predispatch.py`, call `tree_knowledge`/`sweep_owners`/`PHRASES`/`ENTRY_REL` | files 270, owners 0 |
| 9 | `test -e corpus/knowledge/linguistics/praise-poetry-panegyric.md` | absent, rc 1 |
| 10 | `grep -c 'S1007\|S1008\|S1009\|S1010' corpus/SOURCES.md` | 0, rc 1 |

## Sibling lanes — 21/21 no overlap

- Canon: lore-shokunin (`PROVINCE:3-9`) — owns world-bible records and consistency; the new entry is reference craft and hands off.
- Research method: chousa-shokunin (`PROVINCE:3-10`) — owns source hierarchy and claim-vs-source; the entry cites evidence, owns no method.
- Prompt/skill craft: kotoba-shokunin (`PROVINCE:3-6`) — owns SKILL.md/AGENTS.md quality.
- The remaining 18 (audio, game-dev-2d/3d, kagi, kaidoku, kake, kama, kasegi, kengaku, kumitate, mado, mori, revenger, souji, tabi, tameshi, tsukuroi) have zero praise/panegyric/bard/epithet/poetry hits; their `oral` and `performance` hits are the evidence idiom and the CWV/eval sense, checked line by line.
- Three corpus-level non-owners named so they are not mistaken for claims: `chousa-shokunin/corpus/captures/c9d1e74c3ac8d9eb332c9770.txt:719` (captured MEDLINE page), `kumitate-shokunin/corpus/knowledge/cost-and-profile.md:332` (Google Bard model needle), `revenger-shokunin/corpus/knowledge/round-73-re-resource-atlas.md:381` (book atlas).
- Could not read: `art-east-asian-design/` — named as a lane in `lore-shokunin/PROVINCE.md:9` and `game-dev-2d-shokunin/PROVINCE.md:10` but no directory exists (`ls -d`, rc 2). `kumitate-shokinin/kumitate-shokunin/` is empty, no PROVINCE/SKILL.

## In-lane boundaries (one sentence each; anchors verified by `grep -n`)

1. `linguistics/orality-formulaic-language.md:56` §3 + bullet `:60` — owns the epithet as metrical slot-filler and praise-name as compressed formula (and already states the oríkì/izibongo institution thesis); the new entry owns the institution around the recitation and must cite `:60`, not re-describe it.
2. `linguistics/naming-systems.md:73` §4 — owns divine cult epithets (theonym+epithet); the new entry's praise epithet is person/lineage/office-directed.
3. `linguistics/verbal-duelling-ritual-insult.md:18` §1, `:110` §6 — owns the contest frame and boast/taunt/riposte grammar; the new entry's rivalry/satire is praise-side, not a word-contest.
4. `linguistics/funerary-lament-dirge-formulae.md:15` §1, `:133` §6 — owns praise of the dead inside the mourning register; the new entry takes praise of the living.
5. `linguistics/toast-drinking-speech-formulae.md:21` §1, `:122` §5 — owns the toastmaster's office and toast order; the praise-performance order is a distinct occasion.
6. `linguistics/linguistic-anthropology.md:9` §1, `:91` §5 — owns the SPEAKING grid as method; the new entry applies it and re-derives nothing.
7. `myth-symbol/sacred-kingship-mythic-charter.md:150` §8.5, `:158` §9 — owns praise-recitation as royal legitimation, the reciter as an office, the titulary and pedigree curation; the new entry owns no charter.
8. `myth-symbol/heraldry-emblems-identity-marks.md:18` §2 — owns the carried/inherited mark; a praise epithet is spoken, not borne.
9. `myth-symbol/hero-journey-variants.md:59` §3 — owns the hero pattern and the fossilized founding formula; a royal epithet is only a bearer-tied case for the new entry.

Further owners found by the scan (all case-scoped, boundary to respect): `civilizations/yoruba.md:78,84,86-90` (oríkì economy), `civilizations/mali-songhai.md:50,53,59-64` (jeli archives), `civilizations/parthia.md:165` (gōsān), `civilizations/germanic-norse.md:72,77` (skaldic economy), `civilizations/zimbabwe-shona.md:87,90` (mutupo/chidawo), `civilizations/polynesia-navigation.md:142` (oral genealogy/whakapapa), `civilizations/hawaii.md:51`, `civilizations/maori.md:85`, `culture-material/dance-performance-movement-codes.md:20`, `linguistics/sacred-registers-liturgical-language.md:3`.

Lane convention worth keeping: each genre entry owns its own performer office (keener `funerary:56`, toastmaster `toast:122`, spokesman `sacred-kingship:148`), so a praise-singer office is consistent, not a second owner.

## Contested scope — routed to the L1 (at most three)

1. `orality-formulaic-language.md:60` already states the institution thesis ("Praise poetry as social formula … the epithet system promoted to a social institution"). The claim's boundary sentence assigns orality only the formula lexicon. L1 decision: cite `:60` as prior art and add only the office/patronage/reward/order/audience/rivalry layer, or restate the boundary sentence. C8 cannot catch a body-level restatement.
2. `sacred-kingship-mythic-charter.md:150` already claims "the reciter as an office" and praise-recitation as performed pedigree; `:158` names "the priests, the bards, and the archivists" as curators. L1 decision: patron scope (ruler vs any patron) as the dividing line, royal case cited not re-derived.
3. The praise economy is already written at case level in `yoruba.md:84-90` and `mali-songhai.md:59-64` (public praise invites reward; praise does not exclude criticism). L1 decision: cite both and add only the comparative layer, or narrow the "patronage and reward" / "rivalry, satire" headings so the entry is not a third telling of the same two cases.

## Second-order note

Claim C's C8 leg sweeps topic lines and markdown headings only (`predispatch.py:56,581-587`). Every risk above lives in body text, so the leg passes while duplication remains possible; the entry's own h2 headings carrying the six frozen phrases are what the sweep will see, and they will be excluded by `ENTRY_REL`. No leg change is proposed here — this is a report, not an edit.
