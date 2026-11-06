# ConnectorOverlap97 — sibling/adjacent-owner overlap scan: verbal duelling and ritual insult

Round 97 w1, seat ConnectorOverlap97. Read-only scan; write surface: this file, the wave
report `../../../ConnectorOverlap97.md`, and `DONE` beside it. No file owned by another seat
was touched; frozen files (claims.json, predispatch.py, predispatch-base.txt, sweep-control.*,
controls/*) were read only.

## 1. Surface scanned
The frozen claim-C surface: verbal duelling / ritual insult — flyting, senna, song duels,
boasting matches, invective/taunt contests, rap-battle-like word duels, and their audience
adjudication (six frozen phrases: "verbal duel", "ritual insult", "flyting", "song duel",
"boast formula", "audience adjudication").

## 2. Commands and results (every count with command and rc)

| # | Command (verbatim) | Result | rc |
|---|---|---|---|
| C1 | `ls -d /home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md \| wc -l` | 21 | 0 |
| C2 | grep tool, `(?i)\b(flyting\|insult\|insults\|duel\|duels\|contest\|contests\|satire\|invective\|boast\|boasts\|taunt\|taunts\|rap battle\|debate)\b` over `/home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md` | No matches found (0 files) | 0 |
| C3 | same pattern over `/home/vgpnk/Projects/shokunin/*-shokunin/SKILL.md` | No matches found (0 files) | 0 |
| C4 | `grep -riocE '<pattern of C2>' /home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md /home/vgpnk/Projects/shokunin/*-shokunin/SKILL.md \| grep -v ':0$' \| wc -l` | 0 | 0 |
| C5 | grep tool, substring pass `(?i)flyting\|insult\|duel\|contest\|satire\|invective\|boast\|taunt\|rap battle\|debate` over PROVINCE.md glob | hits only in lines carrying the fleet word "contested" (substring "contest"): game-dev-2d:10, game-dev-3d:36,78, kagi:64, kaidoku:187, kake:45, kotoba:17, kotodama:25, mori:66, souji:189, tsukuroi:570 — arbitration vocabulary, not the duelling surface | 0 |
| C6 | `grep -rilE 'verbal duel\|ritual insult\|flyting\|song duel\|boast formula\|audience adjudication' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge \| wc -l` | 2 (linguistics/orality-formulaic-language.md; myth-symbol/trickster.md) | 0 |
| C7 | grep tool, `(?i)^(?:- topic:\|#{1,6} ).*(verbal duel\|ritual insult\|flyting\|song duel\|boast formula\|audience adjudication)` over `corpus/knowledge` | No matches found → 0 topic-line/heading owners | 0 |
| C8 | glob `corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md` | Path not found (pre-state confirmed; the entry does not exist yet) | — |

## 3. Sibling owner table (21 lanes; every PROVINCE.md read)

| Lane | Ownership line observed (file:lines) | Surface-term hits | Class | Verdict |
|---|---|---|---|---|
| lore-shokunin | PROVINCE.md:3 Owns "fictional-world records — entities…, relations, timeline events…"; :9 refuses "claiming canon without an in-world citation" | 0 | canon | **Boundary to respect** — lore records in-world duels as canon; it owns no reference craft for them. Kotodama hands systems off; lore never sources real-world practice. |
| chousa-shokunin | PROVINCE.md:3 Domain "deep-research method (調査) — the reusable craft of source research"; :5-8 Owns question framing, source hierarchy, claim-vs-source verification | 0 | research method | **Boundary to respect** — chousa owns the sourcing method claim C's rows must be mined under, not the linguistic content. No domain overlap. |
| kotoba-shokunin | PROVINCE.md:3-6 prompt & skill craft | 0 | tooling craft | No overlap |
| kengaku-shokunin | PROVINCE.md:3-6 LLM/model research & evaluation | 0 | tooling craft | No overlap |
| kaidoku-shokunin | PROVINCE.md:1-5 RE of shipped artifacts (Ghidra/REA) | 0 | RE | No overlap |
| revenger-shokunin | PROVINCE.md:3-6 Owns reverse engineering of shipped artifacts; :44-47 Refuses | 0 | RE | No overlap |
| kasegi-shokunin | PROVINCE.md:3,19-20 bounty & security research | 0 | security | No overlap |
| kagi-shokunin | PROVINCE.md:3-6 secrets & vault ops | 0 | secrets | No overlap |
| kama-shokunin | PROVINCE.md:3-5 local model serving & endpoint health | 0 | serving | No overlap |
| kake-shokunin | PROVINCE.md:3-6 web properties & publishing | 0 | publishing | No overlap |
| tabi-shokunin | PROVINCE.md:1-8 browser & web-interaction craft | 0 | browsing | No overlap |
| kumitate-shokunin | PROVINCE.md:3-6 orchestration & tooling (OMP/ufo-fsd) | 0 | orchestration | No overlap |
| tsukuroi-shokunin | PROVINCE.md:2-6 host operability & system repair | 0 | host OS | No overlap |
| tameshi-shokunin | PROVINCE.md:1-5 verification-fixture craft | 0 | verification | No overlap |
| mori-shokunin | PROVINCE.md:1-7 fleet & host observability (read-only probes) | 0 | observability | No overlap |
| souji-shokunin | PROVINCE.md:1-4 fleet repo & workspace hygiene | 0 | hygiene | No overlap |
| mado-shokunin | PROVINCE.md:1-4 desktop & compositor craft | 0 | desktop | No overlap |
| audio-shokunin | PROVINCE.md:3-5 game audio production; :13-15 Refuses | 0 | game audio | No overlap |
| game-dev-2d-shokunin | PROVINCE.md:3 2D game production; :10 Refuses ("narrative canon (lore lane — contested scope is reported, not absorbed)") | 0 (C5 "contested" only) | game dev | No overlap |
| game-dev-3d-shokunin | PROVINCE.md:3-6 3D game production; :33-36 Refuses | 0 (C5 "contested" only) | game dev | No overlap |
| kotodama-shokunin (self) | PROVINCE.md:3-5 linguistic-cultural worldbuilding; Refuses names lore (canon) and chousa (research method) | owner of the new entry | reference craft | Writes `corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md` + S985+ rows |

No sibling PROVINCE.md or SKILL.md contains any of the ten scan terms with word boundaries
(C2-C4: 0). No sibling claims flyting, insult contests, duels, satire, invective, boasting,
taunting, rap battle, or debate as an owned or refused surface. **No sibling claims this
surface; nothing is contested; nothing routes to the L1.**

## 4. In-lane neighbours (corpus/knowledge) — boundary in one sentence each

| File | Topic line / ownership observed | Boundary |
|---|---|---|
| linguistics/orality-formulaic-language.md | topic (:3): oral-formulaic composition, performer licensing — flyting and Lokasenna-style senna appear as :112 list item 10 "competitive forms" | Orality owns the formulaic performance substrate (composition, licensing, festival frames); the new entry owns the adversarial word-contest itself — duel as contest, not as composition technique. |
| linguistics/politeness-taboo-euphemism.md | topic (:3): face-work, honorifics, taboo vocabulary and sanctions; closing handoff: canon is lore's | Politeness owns how cultures forbid saying; the new entry owns the licensed transgression where insult is ritual — the sanctioned inverse of taboo, not taboo itself. |
| myth-symbol/binding-speech-complex.md | topic (:3): oath, curse, blessing, name-power as one binding machinery with executors | Binding owns the word-holds machinery (who executes a spoken word); the new entry owns the adversarial contest frame — satire-as-curse is the coupling point, owned here only as machinery. |
| myth-symbol/trickster.md | topic (:3): the trickster figure class; :25 table cell and :62 "pure flyting clown (Lokasenna)" | Trickster owns the boundary-crossing figure who wins the word-duel; the new entry owns the duel genre and its rules, treating Lokasenna as a flyting instance, not a trickster study. |
| linguistics/oath-blessing-curse-formulae.md | topic (title :1): performative word-acts that bind, bless or harm; sources S975-S984 | Formulae owns the performative anatomy of binding utterances; the new entry owns boast/taunt/riposte formulas whose stakes are adjudicated by an audience, not sealed by an executor. |
| linguistics/greeting-leave-taking-formulae.md | topic (:3): greeting/farewell speech acts, politeness and access rituals (S961-S964) | Greetings owns ritualised encounter openings and closings; a word-duel often opens with such formulae, but the contest proper and its adjudication belong to the new entry. |
| linguistics/secret-and-ludic-languages.md | topic (:3): argot, anti-languages, ludling, word-play registers (S952-S955) | Ludic languages owns playful registers without adjudicated stakes; the new entry owns adversarial word-play whose outcome carries rank, shame or settlement. |
| culture-material/games-play-sport-contests.md | topic (:3): games, play, sport and contests as material and social practice; §5 (:41-44) "Athletic and ritual contests" | Nearest internal neighbour: Games owns contest procedure, staging and competitor status for contests of bodies and boards; the new entry owns contests fought in words and should couple to Games' three-variable decomposition (festival setting / contest procedure / status of competitors) instead of re-owning it. |

C6/C7: the only frozen-phrase mentions in the corpus are prose/list/table mentions
(orality:112, trickster:25, trickster:62) — matches the claims.json before-state; the wider
term surface additionally surfaces `civilizations/arabia-pre-islamic.md:69-73` (Fakhr
"self/group praise", Hijāʾ "invective", "idealized boast", "do not turn every insult into an
ethnographic fact") — a table-cell mention of the same subject matter, not an owner, and
consistent with the claims.json base-mentions pointer at `:71`. Zero topic-line or heading
owners of any frozen phrase (C7) — the frozen zero-owner premise holds by content, not by
filename.

## 5. Contested-scope items

None (0 of at-most-3). Nothing routes to the L1. Every neighbour boundary above is a stated
respect-line between kotodama's own entries or between kotodama and lore/chousa under the
existing adjacent contract (kotodama PROVINCE.md:15-25).

## 6. Files that could not be read

None. All 21 PROVINCE.md heads read; SKILL.md and corpus greps ran clean.

## 7. Second-order note for the round (finding, not action)

The move "write the entry at the frozen path" is ownership-clean: it improves claim-C
coverage and harms no sibling or in-lane owner. One live risk travels with later edits:
any round that adds a heading or topic line containing "verbal duel", "ritual insult",
"flyting", "song duel", "boast formula" or "audience adjudication" to any *other* knowledge
file flips frozen leg C8 to FAIL. Verification before any scoring seat runs: re-run command
C7 (0 owners expected) and C6 (2 mention files expected) against the landed tree.

## 8. Tooling authorization

None used — no tool installed or upgraded for this seat.
