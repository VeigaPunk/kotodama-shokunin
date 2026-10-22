# ConnectSiblingSign — claim C sibling-overlap scan (round 51, attempt 3)

Seat: `KotodamaR51a3.ConnectSiblingSign` (connector, leaf, read-only). Judged on: coverage.
Author-lane advice, never admission. No installs. No files written except this report.

## Assigned item

Read-only scan of every sibling lane `/home/vgpnk/Projects/shokunin/*-shokunin` (kotodama
excluded): `corpus/knowledge/`, `PROVINCE.md`, `SKILL.md`, plus lore-shokunin's whole tree
(world-bible fixtures included). The question is whether any sibling owns or partly owns sign
languages, gesture, deaf communities, manual communication or sign notation, and whether a
kotodama entry `corpus/knowledge/linguistics/sign-languages-manual-modality.md` would overlap
a sibling's province.

## Result (lead)

**No sibling lane owns or partly owns any part of claim C's scope.** No sibling is a
contested owner of sign languages, deaf communities, homesign, manual codes, fingerspelling or
sign notation. Every lexical hit is either a non-linguistic sense of the word (code signing,
pointer gestures, browser user-gesture flags) or noise. Two sibling **boundaries** still
touch C and must be named in its Scope section: lore-shokunin (canon) and kake/tabi
(real-world web accessibility). Kotodama's own `PROVINCE.md:9-14` already claims the
linguistics partition, so C stays inside province.

## Method (reproducible)

All 20 sibling lanes have `PROVINCE.md` and `corpus/knowledge/`. All except audio, game-dev-2d
and revenger have `SKILL.md`. Four case-insensitive ripgrep passes were run:

1. Over each sibling's `corpus/knowledge`, `PROVINCE.md` and `SKILL.md`:
   `sign[- ]languages?|\bdeaf|fingerspell|manual (communication|code|modality|alphabet|sign)|homesign|signwriting|hamnosys|stokoe|gestur|\b(ASL|BSL|LSF|NSL|ABSL)\b|\bsigners?\b|\bsigning\b|sign notation|notation of signs|hand ?shapes?|sign systems?`
2. Over lore-shokunin's entire tree: the same core terms plus `mute|hand ?talk|silent speech`.
3. Over every sibling's entire tree, excluding `.git`, `.jj` and `node_modules`: the core sign-language terms.
4. Over the scope of pass 1 plus `lore-shokunin/corpus/fixtures`, for adjacent manual channels:
   `semaphore|hand[- ]signals?|pantomim|\bmime\b|nonverbal|kinesic|body language|signal flags|tactile|braille`.

## Hits, classified

| # | path:line | what it says | class | overlaps C? |
|---|---|---|---|---|
| 1 | `kake-shokunin/corpus/knowledge/accessibility-review-cards.json:412-419` | WCAG 2.5.1 "Pointer Gestures" review card (multipoint or path touch gestures) | mention, unrelated sense (UI input gesture) | no |
| 2 | `kake-shokunin/corpus/knowledge/accessibility-review-cards.json:27-59` | WCAG 1.2.2 and 1.2.4 caption cards; card ids run 1.1.1, 1.2.1-1.2.5, 1.3.x, 1.4.x — **no 1.2.6 "Sign Language (Prerecorded)" card** | adjacent boundary (media accessibility), not an owner | no, if C makes no conformance or accessibility claim |
| 3 | `kake-shokunin/corpus/knowledge/accessibility-review-packet.md:15,19-20` | "The fixed population is the Level A and AA success criteria"; "AAA criteria are outside this packet" (1.2.6 Sign Language is AAA) | explicit non-owner: kake refuses the AAA sign-language criterion | no; see the contested-scope item below |
| 4 | `kake-shokunin/PROVINCE.md:23-25,70-77` | WCAG 2.2 accessibility conformance is kake's frontier; preparation only; tabi owns browser and assistive-technology execution | adjacent boundary | no, while C stays conlang and worldbuilding method |
| 5 | `tabi-shokunin/corpus/knowledge/network-evidence-rung.md:155` | `hasUserGesture=true` (Chrome DevTools field) | mention, unrelated sense | no |
| 6 | `tabi-shokunin/corpus/knowledge/webmcp-nonautosubmit-round-21-corrected.md:34` | "submit event isTrusted" row (matched "signing" or "gesture" noise) | mention, unrelated | no |
| 7 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-apk-inventory.md:55,59,171,178` and five more kaidoku entries | APK Signing Block, signing keys | noise (code signing) | no |
| 8 | `tsukuroi-shokunin/corpus/knowledge/foreign-provenance-r6.md:87,215` | pacman signer key | noise (package signing) | no |
| 9 | `kasegi-shokunin/corpus/knowledge/intake-surface.md:123`; `kotoba-shokunin/corpus/knowledge/harness-independent-round37.md:250` | "gesture at", "an empty gesture" (idiom) | noise | no |
| 10 | `game-dev-2d-shokunin/corpus/live/r94-critic/manifest.sha256:2195` | the hash contains `deaffe…` | noise | no |
| 11 | `lore-shokunin/reports/r34-axis-adjudicator.md:7`; `lore-shokunin/reports/r10-source-scout.md:24,34` | "heard that"; a fictional registry signer | noise | no |
| 12 | `souji-shokunin/census/round-6/seat-*.json` (many lines) | census of kotodama's own `.scratch` paths (`design-language.md`) | noise (kotodama bytes catalogued by souji) | no |
| 13 | pass 4: `kotoba…/harness-verifier-round10.md:197`, `kumitate…/omp-task-contract.md:80`, `mado…/walker-deep-r9.md:173,319`, plus audio and kaidoku lines | concurrency semaphores, MIME types | noise | no |

lore-shokunin's whole tree, including `corpus/fixtures` (the world-bible fixtures; 174 fixture
directories per `lore-shokunin/PROVINCE.md:35`), has **zero** sign, deaf, gesture, homesign or
manual-communication hits. No fixture world bible records a signed language that C's guidance
could contradict.

## Province lines that bound C (sibling side)

- `lore-shokunin/PROVINCE.md:3` owns fictional-world records. `:8` refuses "claiming canon without an in-world citation". `:28` names kotodama as the supplier of "generated-content handoff packets" via `kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md` (the file exists) and says kotodama owns name generation and calendar design. Read together, these mean lore owns which signed languages exist in a world, and C owns the method only.
- `lore-shokunin/PROVINCE.md:19,23`: "CM-g kotodama packet intake stay `uncovered`". Lore has no gate that ingests kotodama packets yet, so C's handoff section is a one-way offer, not a verified integration.
- `kotoba-shokunin/PROVINCE.md:34`: "kotodama (worldbuilding/naming) … — no overlap observed." This is an explicit sibling non-claim.
- `audio-shokunin/PROVINCE.md:3-5,13-15` owns game audio and refuses narrative canon. It has no speech or modality ownership; whistled and drum channels sit on kotodama's side (`kotodama-shokunin/corpus/knowledge/linguistics/phonetics-phonology.md:75,197-200`).
- `kotodama-shokunin/PROVINCE.md:16-20` refuses canon (lore), game mechanics (game-dev-2d/3d), research method (chousa), web publishing (kake) and prompt craft (kotoba). None of these refusals covers sign-language method.

## Contested scope for the integrator (name, never absorb)

1. **Real-world accessibility of signed content (WCAG 1.2.6, AAA) has no owner in the fleet.** Kake excludes AAA criteria (`kake-shokunin/corpus/knowledge/accessibility-review-packet.md:19-20`) and its cards stop at 1.2.5. Tabi only executes authorized browser runs (`kake-shokunin/PROVINCE.md:30-31,75-76`). A kotodama sign-language entry is the natural place for this to leak: an "interpreter inset" or "sign-language track" design note would read as accessibility guidance. This is unowned and must stay unowned by C. C's Scope MUST refuse conformance, captioning and interpretation-provision advice and route it to kake (preparation) and tabi (execution) without claiming either one owns AAA. The routing complements the brief's existing refusals of clinical, education-policy and rights rulings.
2. **Canon of signed languages in any world belongs to lore.** Lore's intake is uncovered (CM-g), so C's lore-shokunin handoff must say it supplies systems and decision tables only. It must not say lore "records" or "verified" anything.

## Intra-lane coupling C must narrow against (kotodama side, not sibling)

These are the existing kotodama lines that already touch C's scope. C should cite each one and
state who owns what, so the coverage gain is a new owner rather than a duplicate:

| path:line | existing content | C's relation |
|---|---|---|
| `corpus/knowledge/linguistics/phonetics-phonology.md:201-203` | "Sign-language phonology works without acoustics — handshape, location, movement carry contrast (Sandler & Lillo-Martin 2006); deaf cultures need this layer." | a seed; C becomes the full owner, and phonetics-phonology keeps the acoustic channel |
| `corpus/knowledge/linguistics/syntax-typology.md:99` | emerging sign languages and homesign as contested evidence for an "SOV default" | C must keep the contested flag and must not upgrade it to a fact |
| `corpus/knowledge/linguistics/numerals-and-measures.md:107` | finger counting is culturally patterned; gesture as digit or as word | numerals keeps counting gestures; C owns lexical signs and manual codes |
| `corpus/knowledge/linguistics/linguistic-anthropology.md:147` | registers license dress and gesture | co-speech gesture and register stay there; C owns full manual languages |
| `corpus/knowledge/linguistics/writing-systems.md:9,21` | script typology classified by the sign-to-speech mapping; semasiography row | writing-systems owns scripts for speech; C owns notation of signed languages (Stokoe, HamNoSys, SignWriting) as a distinct row, citing `:21` as the boundary |

## Proposed move (one, bounded)

Give C's Scope section a **three-column refusal table** (`scope item | owner | anchor`), with
rows for:

- canon: lore-shokunin, `lore-shokunin/PROVINCE.md:3,28`;
- web accessibility conformance, including the unowned AAA 1.2.6 criterion: kake and tabi for preparation and execution, `kake-shokunin/corpus/knowledge/accessibility-review-packet.md:19-20`;
- clinical, education-policy and rights rulings: refused, per the brief and `PROVINCE.md`.

Add the five intra-lane rows above as C's own one-owner boundary table.

- **Axes improved:** coverage, because C enters as a sole owner with zero sibling overlap and the unowned AAA gap is made visible instead of silently filled. Canon hygiene and coupling (QUALITY) also improve.
- **Axes harmed:** none. The rows cite existing entries and sibling province files only. They do not cite `corpus/lessons/round-51.md` or `reports/round-51/boundary-count.py`, which avoids round 50's hidden entry-to-lesson coupling. They add no dependency from claim D to C.
- **Risks:**
  - Sibling path anchors are fleet-root-relative and live outside the lane. If C's link checker resolves only lane-relative paths, write the sibling anchors as plain text, not backticked `file.md:N`.
  - C's 250-line cap: the two tables cost about 14 lines.
  - Lore's CM-g gap means the handoff stays unverified. State that; do not paper over it.
- **Verification (unrun here):**
  - `find corpus/knowledge -name '*.md' | wc -l` gives 227 after C lands.
  - Re-run the pass-1 grep after integration. It should still show no sibling owner.
  - Check that each cited kotodama line still reads as quoted at the base `bff83ba`.
  - `rg -n 'lessons/round-51|boundary-count' corpus/knowledge/linguistics/sign-languages-manual-modality.md` should return nothing.

## Unrun checks

- No web sources were opened (none were needed for a sibling-overlap scan). No `NEW-` registry rows are drafted.
- The sibling scan is lexical. A sibling entry that discusses manual communication with none of the searched terms would be missed. Pass 4's adjacent-channel sweep reduces that risk but does not prove absence.
- The `game-dev-3d`, `kengaku`, `chousa` and `mori` provinces were covered by the greps, not read in full.
