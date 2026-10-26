# ScoutGapSweep — gap sweep for claim C GROUND

Seat: ScoutGapSweep (leaf). Lane: kotodama-shokunin. Base: f556d1049fe651d3d63975600b13acd9fb686f15.
Question: is the round-75 claim C "before" ground true at base, and does any sibling lane already own the narrative-structure/narratology surface?
Tooling installs: none (read-only git/grep only).

## 1. Claim C ground, re-derived at base (all commands run 2026-10-27, cwd fleet root, lane addressed with `git -C`)

Command: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree -r --name-only f556d1049fe651d3d63975600b13acd9fb686f15 corpus/knowledge | grep -ci narrative`
Output: `0` (grep exit 1 — no narrative-named file at base). Matches claim "before(a)" (= 0).

Command: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show f556d1049fe651d3d63975600b13acd9fb686f15:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`
Output: `808` (exit 0). Tail ids: `| S882`, `| S883`, `| S884` → last id S884. Matches claim (808-row registry, last id S884).

Same registry grep per fragment, all against base corpus/SOURCES.md (each `grep -c "<fragment>"`, all exit 1 → 0):

| fragment | matches |
|---|---|
| persee.fr/doc/comm_0588-8018_1966_num_8_1_1113 | 0 |
| persee.fr/doc/comm_0588-8018_1966_num_8_1_1120 | 0 |
| persee.fr/doc/comm_0588-8018_1966_num_8_1_1114 | 0 |
| jw.ucass.edu.cn | 0 |
| jstage.jst.go.jp/article/jcss | 0 |
| jstage.jst.go.jp/article/jsik | 0 |
| unige.ch/lettres/framo | 0 |
| iris.unipa.it | 0 |

All 8 fragments: 0 rows. Matches claim ground.

Command: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree -r --name-only f556d1049fe651d3d63975600b13acd9fb686f15 corpus/knowledge | grep -c '\.md$'`
Output: `249`. Matches claim ("Knowledge files 249 -> 249 + frozen entries").

Command: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -ilE 'narrative structure|narratolog' f556d1049fe651d3d63975600b13acd9fb686f15 -- corpus/knowledge | wc -l`
Output: `3` — files: corpus/knowledge/civilizations/yoruba.md, corpus/knowledge/myth-symbol/myth-ritual-theories.md, corpus/knowledge/myth-symbol/ritual-liminality.md. These are incidental term mentions, not coverage (line evidence at base):
- yoruba.md:18 — a citation note ("…directly consulted for missionary mediation, signs, narrative structure, and interpretive authority").
- myth-ritual-theories.md:48 — "comparative Indo-European mythology is now done with formulae and narrative structures".
- ritual-liminality.md:3 — topic line tail: "the mapping of ritual grammar onto narrative structure (p…".
None governs narrative structure as a framework surface; none is named narrative-structure*.

Nuance check on the claim's parenthetical: `git grep -inE 'Barthes|Greimas|Todorov|structuralis|narratolog' <base> -- corpus/knowledge/myth-symbol/comparative-frameworks.md corpus/knowledge/myth-symbol/hero-journey-variants.md` → comparative-frameworks.md:1,3,15,69,78,105,112; hero-journey-variants.md: no output. comparative-frameworks.md does cite "Greimas (1966), Sémantique structurale, Larousse (actantial model)" (:15, :78) — a structuralist source, but not a Communications-8 narrative paper; Barthes and Todorov appear nowhere in corpus/knowledge at base. The claim's fragment-level ground (0 registry rows; no narrative-structure file; neither comparative-frameworks.md nor hero-journey-variants.md names a structuralist *narrative* source) holds; the strict sentence "neither names a structuralist narrative source" is accurate for the recits canon (Barthes/Todorov/Greimas-Communications-8) the claim cites.

Lane HEAD note: `git log --oneline -3` → f556d10 (round-74 verifier spot-check) is HEAD; `git diff --shortstat <base> HEAD -- corpus/knowledge` → empty. Lane tree == base for corpus/knowledge; numbers above are also live-tree numbers.

## 2. Sibling lane sweep (read-only)

All 21 `*-shokunin` lanes have PROVINCE.md.

Per-lane corpus/knowledge grep for `narratolog|narrative.structure|Greimas|Todorov|Barthes` at HEAD (`git -C <lane> grep -ilE ... HEAD -- corpus/knowledge`): 20/21 lanes → 0 hits. Only kotodama-shokunin hits (5 files at HEAD, 3 at base as above — HEAD adds costume-semiotics.md and comparative-frameworks.md which already held Greimas at base).

Narrative-named files: `git ls-tree -r --name-only HEAD corpus/knowledge | grep -i narrative` → none in any lane.

PROVINCE narrative mentions: 5 lanes match `narrat|Barthes|Greimas|Todorov` — audio-shokunin, game-dev-2d-shokunin, game-dev-3d-shokunin, kotoba-shokunin, revenger-shokunin — every hit is the routing phrase "narrative canon (lore)" or a refusal of narrative canon (e.g. game-dev-2d PROVINCE.md:10 "narrative canon (lore lane — contested scope is reported, not absorbed)"; audio PROVINCE.md:15,26,29). That is in-world canon ownership, not narrative theory.

Targeted reads:
- lore-shokunin PROVINCE.md:3-6,23,28,34 — owns fictional-world records/entities/timeline and the world bible ("in-world documents under corpus/ (world bible…)", line 6, annotated 2026-10-19 that fixture bibles exist); line 28 explicitly routes to kotodama for name generation, calendar/era design and acknowledges the worldbible-integration-contract. Lore owns canon records; no narratology/structuralist-narrative claim anywhere in its corpus (0 grep hits).
- kengaku-shokunin PROVINCE.md: research-methodology lane (mentions of "narrative" at :393,:405 are about grader/history-pass wording, not the surface). 0 corpus hits.

kotodama-shokunin PROVINCE.md:4,10 — owns `corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}`; mythic and symbolic systems are its domain ("mythic and symbolic systems" line 4). The narrative-structure-frameworks theme lands on kotodama-owned ground (myth-symbol), and the claim's entries are scoped as generative/coupling craft, not lore canon (PROVINCE Refuses: "claiming or recording canon — that is lore-shokunin").

shokuknow spot check (read-only): `grep -rilE 'narrative.structure.framework|Barthes|Greimas' /home/vgpnk/Projects/shokuknow` → hits under shokuknow/.ufo/waves/corpus-expansion-1/wave{3..7}-messages/ScoutKotodama.md — the theme was scouted at the source during corpus-expansion, consistent with the claim's "shokuknow assimilation" framing. (Not exhaustively re-derived; the assimilation source exists.)

## 3. Verdict

- Claim C GROUND legs re-derive exactly at base: 0 narrative-named files; 808 registry rows ending S884; 0/8 fragment rows; 249 knowledge .md files; term-hits incidental (3 files) and no governing entry. The counter's independent re-derivation should print the same.
- Sibling ownership: none. No lane owns the narratology/structuralist-narrative-theory surface; lore owns in-world narrative canon only; kengaku owns research method only. No collision with the planned corpus/knowledge/myth-symbol/narrative-structure-frameworks*.md entries.
- Confidence: high on ground numbers (direct git re-derivation); high on sibling sweep (full 21-lane grep + PROVINCE reads); medium on shokuknow theme provenance (grep-l evidence only, wave messages not opened line-by-line — not required for the gap question).
- Remaining unknowns: none for the assigned question. (The GROUND telemetry file reports/round-75/telemetry/gap-sweep.txt is the builder/counter's artifact, not this seat's.)

## 4. Evidence hygiene

All commands above were read-only git/grep against the lane repo and sibling repos; no fleet file, lane jj/git state, scripts/templates, or shokuknow content was mutated. No tools installed. Scratch dir /fast/scratch/hyaku/kotodama-r75/ScoutGapSweep (created, unused beyond mkdir) removed before yield; no /tmp evidence used.
