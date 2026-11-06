# ConnectorOverlap98 — sibling and adjacent-owner overlap scan, toasts and drinking-speech formulae (round 98, w1)

Seat: ConnectorOverlap98 (leaf member, read-only; writes only this stage). Surface: claim C's new entry
`corpus/knowledge/linguistics/toast-drinking-speech-formulae.md` (frozen topic line, six frozen phrases:
"toast formula", "health-drinking", "toastmaster", "libation", "toast sequence", "drinking oath").

Axes named (godspeed): A1 adjacency precision (boundaries stated per owner), A2 evidence traceability
(every count has its command and rc), A3 zero-harm (no byte written outside this stage; no frozen file touched).

## 1. Method

1. `ls -d /home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md` → 21 lanes, exit=0 (supervised proc `ListProvinces`, pid 201484, `exit=0`).
2. Glob `*-shokunin/SKILL.md` → 19 files. `audio-shokunin/` and `game-dev-2d-shokunin/` publish no SKILL.md (their README.md Domain lines were read instead: game audio; 2D game production).
3. Term scan, pattern `(?i)\b(toast|drink|feast|banquet|libation|hospitality|ritual|ceremony|oath)s?\b`:
   - over all 21 PROVINCE.md → **0 matches** (grep tool verdict "No matches found"; rc-equivalent 1);
   - over all 19 SKILL.md → matches only in **kotodama's own** SKILL.md (:394, :427, :534, :604, :794–796, :806, :820 — register/law and myth tables of this lane) and in mado SKILL.md (:139, :154, :571, :581 — "change rituals" = desktop-config procedure) and mori SKILL.md (:497, :515 — "re-pin ritual" = fleet procedure). No sibling claims any toast/drink/feast/hospitality/oath surface.
4. Domain/Owns/Refuses extraction over the 21 PROVINCE.md (pattern `(?i)^(\*{0,2})(Domain|Owns|Refuses)\b.*`) → 20 files; tsukuroi-shokunin/PROVINCE.md uses the same fields and was read directly (:1–33 of 573).
5. Tooling note for reproducibility: sibling lane repos are filtered out of whole-root directory traversals when gitignore=true (control scan with `(?i)^\*\*(Owns|Refuses|Domain)\b` over the fleet root returned only fleet-root files, 281 hits, none in `*-shokunin/PROVINCE.md`). Every sibling scan in this report ran with gitignore=false; single-file paths are unaffected.
6. In-lane phrase sweep, grep tool over `kotodama-shokunin/corpus/knowledge`, pattern `(?i)\b(toast|wassail|bragafull|toastmaster|health-drinking|libation)\w*` → **4 files, 7 lines**: `civilizations/ainu.md:109`; `culture-material/funerary-material-culture.md:8`; `culture-material/vessel-container-lexicon.md:5, :36, :38`; `myth-symbol/death-afterlife-eschatology.md:41, :100`. Zero matches for toast/wassail/bragafull/toastmaster/health-drinking anywhere — consistent with the frozen claim C "before" census (`reports/round-98/claims.json`, C.before: `grep -rliE 'toast|wassail|bragaf|toastmaster|health-drink' corpus/knowledge` → 0 files; libation in 4 files, prose/table cells only). All 7 libation hits are the object/offering sense (libation stick, libation dish, libations to the dead); no file owns the speech act.
7. Grep tool reports matches, not integer exit codes; "0 matches" above is its "No matches found" verdict. All reads are `read`-tool calls (rc 0).

## 2. Sibling owner table (21 lanes; verdicts)

| Lane | Domain (PROVINCE.md line) | Term hits in PROVINCE/SKILL | Verdict |
|---|---|---|---|
| audio-shokunin | game audio production — SFX, soundtrack (Owns:3) | 0 | no overlap |
| chousa-shokunin | deep-research method 調査 (Domain:3, Owns:5) | 0 | boundary to respect — research **method** (question framing, source hierarchy, citation chaining) stays chousa's; the toast entry's sourcing follows the method but owns none of it (kotodama PROVINCE.md:19 refuses it explicitly) |
| game-dev-2d-shokunin | 2D game production, headless fixtures (Owns:3; no SKILL.md) | 0 | no overlap |
| game-dev-3d-shokunin | 3D game production (Owns:3-6) | 0 | no overlap |
| kagi-shokunin | secrets & vault ops (Domain:3) | 0 | no overlap |
| kaidoku-shokunin | RE of shipped artifacts, Ghidra (Domain:3-6) | 0 | no overlap |
| kake-shokunin | web properties & publishing (Domain:3) | 0 | no overlap |
| kama-shokunin | local model serving & endpoint health (Domain:3-4) | 0 | no overlap |
| kasegi-shokunin | bounty & security research (Domain:3) | 0 | no overlap |
| kengaku-shokunin | LLM/model research & evaluation (Domain:3) | 0 | no overlap |
| kotoba-shokunin | prompt & skill craft (Domain:3) | 0 | no overlap |
| kotodama-shokunin | linguistic-cultural worldbuilding (Domain:3-7, Owns:9-14) | own lane — internal tables only | this seat's lane |
| kumitate-shokunin | orchestration & tooling (Domain:3) | 0 | no overlap |
| lore-shokunin | fictional-world records, entities/relations/timeline (Owns:3) | 0 | boundary to respect — **canon**: whether a fictional people toasts, who presides, what a refusal costs is recorded by lore; kotodama hands off the system (`PROVINCE.md:16-17`; lore PROVINCE.md Adjacent: kotodama owns name generation and calendar/era design, lore records landed names/dates) |
| mado-shokunin | desktop & compositor craft (Domain:3-4) | SKILL "ritual" = config procedure only | no overlap |
| mori-shokunin | fleet & host observability (Domain:3-4) | SKILL "ritual" = re-pin procedure only | no overlap |
| revenger-shokunin | RE of shipped artifacts, evidence ledger (Owns:3-6) | 0 | no overlap |
| souji-shokunin | fleet repo & workspace hygiene (Domain:3-4) | 0 | no overlap |
| tabi-shokunin | browser & web-interaction craft (Domain:3-4) | 0 | no overlap |
| tameshi-shokunin | verification-fixture craft (Domain:3-5) | 0 | no overlap |
| tsukuroi-shokunin | host operability & system repair 繕 (Domain:3-4, Owns:7-12) | 0 | no overlap |

**No sibling claims the toasts / drinking-speech surface.** The two non-trivial verdicts are the standing
lane contracts, both already written in kotodama's own PROVINCE.md Refuses list: lore (canon) and chousa
(research method). Neither is affected by a new lane-internal knowledge entry.

**Contested scope: 0 items routed to the L1** (limit 3). No sibling line, canon or method, reaches the surface.

## 3. In-lane adjacent owners — one-sentence boundaries (9 assigned files)

| File (topic line read) | Boundary in one sentence |
|---|---|
| `culture-material/vessel-container-lexicon.md` | Owns the cup itself — SERVING job, ritual/funerary extensions, vessel-naming grammar, and the attested libation vessels (*phiale*, *patera*, *zun*) at :36–:38; the toast entry borrows the drinking vessel as a prop and owns only the words spoken over it. |
| `culture-material/cuisine-food-lexicon.md` | Owns food as cultural system — staple theory, the feast/famine cycle, meal grammar and table etiquette; the toast entry owns the speech act over the shared cup, not the meal, the menu or the feast order of courses. |
| `myth-symbol/guest-right-hospitality-law.md` | Owns hospitality as sacral-legal institution — guest degrees, host's owed package, the **shared cup as opening marker and seal family**, breach ladder and guest obligations; the toast entry owns the formula spoken at that cup and returns obligation, breach and penalty machinery to this owner. |
| `linguistics/oath-blessing-curse-formulae.md` | Owns the grammar of the binding utterance — invoked witness, conditional sanction, self-imprecation, performative verb (:18); the drinking oath's *words* are built with that grammar, so the toast entry owns the drinking-oath occasion and slots and defers formula construction to it. |
| `linguistics/verbal-duelling-ritual-insult.md` | Owns word-contests — flyting, senna, boasting matches, boast/taunt/riposte grammar and the adjudicating audience; boast-vow contests at the boast-cup stay there, and the toast entry owns only the pledge slot where a toast borders a boast. |
| `linguistics/petitionary-and-votive-formulae.md` | Owns address to powers and the conditional vow ("a vow obliges the speaker to act if the god acts first"); a libation-pledge edge toward a deity uses that vow grammar, while the convivial health-drinking core of the toast entry stays outside it. |
| `linguistics/greeting-leave-taking-formulae.md` | Owns the two ends of an encounter — greeting/farewell speech acts, politeness and access rituals; the toast is mid-encounter ritual speech and only a raised-cup-at-arrival/parting boundary case points there. |
| `culture-material/calendar-festival-systems.md` | Owns civil time machinery and festival-cycle engineering — when recurring occasions fall; the toast entry owns what is said at the occasion, never which day it falls on. |
| `myth-symbol/ritual-liminality.md` | Owns rite-of-passage grammar, liminality/communitas, gift/potlatch and sacrifice typology; a commensal rite may be *classified* by that grammar, but the toast's verbal formula and sequence are the new entry's contribution. |

Additional neighbor found by the phrase sweep, beyond the nine assigned: `myth-symbol/death-afterlife-eschatology.md:41,:100` — owns libation **to the dead** inside the ancestor-offering economy (kispu, Parentalia, Ghost Festival). The toast entry should point the funerary-libation facet there one-way; the living-table libation stays with the new entry.

## 4. Connector move (one bounded proposal, axes A1+A2, harms none)

Open `toast-drinking-speech-formulae.md` with a one-way partial-owner table modeled on
`guest-right-hospitality-law.md` §1, splitting on the line the oath entry already established
("that file owns **who executes and what happens**; this entry owns **how the words are built and parsed**"):
the toast entry owns the **words and sequence** of the drinking rite; it returns the cup to the vessel
lexicon, the feast frame to cuisine, bond/breach/penalty to guest-right, formula grammar to the oath
entry, boast contests to verbal duelling, votive-pledge edges to petitionary/votive, libation-to-the-dead
to death-afterlife-eschatology.

- Affected axes: coverage — pre-wires leg C8 (content sweep owners=0) by making the entry the single topic/heading owner and neighbors pointers; depth — avoids the round-97 defect of copied boundary prose (CriticC97: 294 shared 8-grams with the oath entry, cut to 35) by writing boundaries as pointers, never restated prose.
- Harms: none — neighbors are not edited; C1–C7/C9 bytes and predicates untouched; a partial-owner table only adds legitimate bytes toward C1's ≥12000 B floor and keeps frozen phrases where they must be (h2 headings or table data rows).
- Risks: pointer sentences must not embed the six frozen phrases in neighboring files (would break C8 owners=0); table prose must stay original (8-gram distance from guest-right §1 and oath §1 verified by the CriticC-style check after landing).
- Verification: after the entry lands, rerun the C8 sweep; run the 8-gram overlap count against `guest-right-hospitality-law.md` and `oath-blessing-curse-formulae.md`; both are already named counter/report surfaces this round.

## 5. Files not read

None. All 21 sibling PROVINCE.md were scanned (20 via the field extraction, tsukuroi directly); all 19
existing SKILL.md were scanned; `audio-shokunin/` and `game-dev-2d-shokunin/` have no SKILL.md (glob
evidence), and their PROVINCE/README Domain lines were read instead. All nine assigned lane entries were read.

## 6. Tooling installed

None (no package or tool installed or upgraded; pacman untouched, host-wide pause respected).
