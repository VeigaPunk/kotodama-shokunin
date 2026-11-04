# ConnectorOverlap — sibling-overlap scan for claims D and O (round-84 w1)

Seat: ConnectorOverlap · milestone r84-v1 · axes: **adjacency**, **coverage** · read-only.
Companion scoped findings: `.ufo/waves/round-84/w1/ConnectorOverlap.md`. This file is the raw scan; that file is the verdict, the handoff and the risk register.

## 0. What was scanned, and how

Two claim surfaces were probed against every sibling lane:

- **D-surface term set** (witchcraft/sorcery accusation as an institution):
  `witchcraft | \bwitch(es)?\b | witches | sorcer[a-z]* | malefic[a-z]* | venefic | striga | strix | \blamia\b | evil eye | incantation | exorcis | accusation | slander | defamation | religio* | ritual | folklore`.
- **O-surface term set** (ordered sound-law applier):
  `sound law | sound-law | sound change | sound-change | lautgesetz | phonolog* | proto-lexicon | proto-language | etymon | --rules | rules.json`.

Probes, in order (each cheap, each independent):

| probe | target | result |
|---|---|---|
| P1 | 1 274 `*.md` under `<lane>/corpus/knowledge`, first non-empty line indexed | built and searched by heading |
| P2 | same 1 274 files, full-text, word-bounded, case-insensitive | D: 5 hit files / 13 lines under the strict set (4 lore + kengaku telemetry); the extended set adds 2 lore files (r94 on `myth`, r102 is JSON) | O: 0 |
| P3 | `<lane>/SKILL.md` (18 of 20 lanes carry one) | D: incidental `switches` only; O: 0 |
| P4 | all 21 `PROVINCE.md` (20 siblings + kotodama) | only kotodama declares myth/ritual/folklore |
| P5 | `kagi-shokunin/corpus/adjacency.tsv`, `tabi-shokunin/corpus/adjacency.tsv`, `adjacency-screen*.tsv` | 0 kotodama/lore/myth rows |
| P6 | fleet filename sweep `*sound*`, `*phonolog*`, `*lautgesetz*` (excluding `.ufo`, `.git`) | all hits inside kotodama; 0 outside |
| P7 | in-lane contract reads (kotodama tools, counters, gates, knowledge) | §3–§5 below |

Lane set — 20 sibling lanes with a VCS directory and a `corpus/knowledge` tree. Excluded, with reason: `kumitate-shokinin/` (an empty nested directory, no repo), `research/` (3 dated research notes, no `corpus/knowledge`), fleet `tools/`, `scripts/`, `templates/` (no lane province). `kotodama-shokunin` is the home lane and is not counted as a sibling.

## 1. D surface — lane by lane

`md` = knowledge files scanned in that lane. "Hit" = the D-surface term set matched the heading index or the file text at the cited line.

| lane | md | D hits | classification |
|---|---|---|---|
| audio-shokunin | 18 | 0 | not the province (SFX/soundtrack) |
| chousa-shokunin | 91 | 0 | **another lane's province** — research method; its 91 entries are citation/verification method, no witch or accusation content |
| game-dev-2d-shokunin | 5 | 0 | not the province (2D mechanics) |
| game-dev-3d-shokunin | 28 | 0 | not the province (3D mechanics) |
| kagi-shokunin | 31 | 0 | **another lane's province** — secrets/vault ops; no rights or accusation entries (`PROVINCE.md:3-4`) |
| kaidoku-shokunin | 162 | 0 | not the province (reverse engineering) |
| kake-shokunin | 68 | 0 | not the province (publishing) |
| kama-shokunin | 57 | 0 | not the province (local model serving) |
| kasegi-shokunin | 78 | 0 | not the province (bounty/security research) |
| kengaku-shokunin | 76 | 0 | not the province (model evaluation); the one `accusation` string is "raw accusations" in a telemetry metric (`telemetry-run-design.md:46`), not the surface |
| kotoba-shokunin | 64 | 0 | not the province (prompt/skill craft) |
| kumitate-shokunin | 76 | 0 | not the province (orchestration) |
| lore-shokunin | 25 | **4 strict files + 2 extended files, 3 contract lines** | **handoff target (canon) + neighbour (in-world accusation/record-keeping)** — detail below |
| mado-shokunin | 101 | 0 | **another lane's province** — desktop/compositor; no accusation material (the `witch` strings are `switching`) |
| mori-shokunin | 94 | 0 | not the province (fleet observability) |
| revenger-shokunin | 23 | 0 | not the province (reverse engineering) |
| souji-shokunin | 40 | 0 | not the province (workspace hygiene) |
| tabi-shokunin | 74 | 0 | not the province (browser craft); `switches` only |
| tameshi-shokunin | 69 | 0 | not the province (verification fixtures) |
| tsukuroi-shokunin | 94 | 0 | not the province (host operability) |
| **total** | **1 274** | **1 lane** | |

### 1.1 The lore hits, with lines

All paths are fleet-root-relative (the convention lore states at `PROVINCE.md:28`).

| path:line | what it is | why not an owner of this surface |
|---|---|---|
| `lore-shokunin/corpus/knowledge/r96-response-scope-note.md:11` | defines a class where the record "explicitly asserts no accusation, selects no winner" | in-world fictional record class; the word is a *negation inside testimony*, not the institution |
| `lore-shokunin/corpus/knowledge/r96-response-scope-note.md:13,19,20,33` | the counter-accusation contrast, the note text, its reliability note, and the scope bullet | fiction fixture, not scholarship |
| `lore-shokunin/corpus/knowledge/r97-acknowledgment-scope-note.md:12,20,21,38` | three-beat crossing arc: the class sentence, its two table rows, and "no winner, no accusation" | same; the arc is about *account pairing*, not sorcery |
| `lore-shokunin/corpus/knowledge/r100-crossing-arc-synthesis.md:34,35` | "makes no accusation, selects no winner, states both stand unresolved" (beats 2 and 3) | synthesis of the same fiction arc |
| `lore-shokunin/corpus/knowledge/r101-r10-register-first-entry.md:48` | "I make no accusation against Aru" | in-world register entry |
| `lore-shokunin/corpus/knowledge/r102-debt-ledger.json:1295` | debt row "gate-invisibility of contradiction/accusation/winner classes" (JSON, outside the `.md` scan) | verifier blind-spot ledger, not a topic entry |
| `lore-shokunin/corpus/knowledge/r94-cross-myth-design-comparison.md:1` | myth cluster fixtures, ETCSL/Spence/Kojiki comparisons — matched `myth`, not the strict witch set | cross-myth *editorial method* on lore's own fixtures; consumes myth, does not own myth method |
| `lore-shokunin/PROVINCE.md:19,23` | CM-d/CM-f/CM-g status lines | states what lore has not covered |
| `lore-shokunin/PROVINCE.md:28` | "kotodama — generated-content handoff packets … digest unacknowledged by lore — coverage row CM-g" | the one-way handoff declaration |
| `lore-shokunin/corpus/README.md:73,79,94` | CM-g row: intake **uncovered**; digest `5f4c02bf…` unacknowledged; frontier action | lore's own open row |

`lore-shokunin/SKILL.md:3` settles the classification in one line: lore's anti-trigger is "do not use for real-world source discovery, archive authentication, research-method design, rights or permission conclusions". The D surface is exactly real-world source discovery plus a comparative institution method, so it cannot be lore's entry to write.

### 1.2 Province check (P4)

Grep of all 21 `PROVINCE.md` for `religio|ritual|myth|folklore|belief|supernatural|occult` returns exactly two lines, both in the home lane:

- `kotodama-shokunin/PROVINCE.md:3-4` — "mythic and symbolic systems" in the domain clause;
- `kotodama-shokunin/PROVINCE.md:10` — the `myth-symbol` partition path.

No sibling lane declares religion, ritual, folklore, or the supernatural. There is no "religion/ritual neighbour" lane to hand to.

### 1.3 Base re-measure (independent, for the critic)

At base `81499ee45b5751d388fefc78583810878de01ecd`, over `corpus/knowledge`:

- owning basenames, `git ls-tree -r --name-only … | grep -ciE 'witch|witchcraft|sorcer|malefic'` → **0** (matches the frozen BEFORE);
- owning `- topic:` lines, word-bounded and case-insensitive → **0** (matches; a non-word-bounded probe returns 1 file, `myth-symbol/celestial-symbolism-calendars.md:3`, on the substring `witch` inside "aspect-**switch**ing" — a false positive, recorded so no one re-derives it as an owner);
- the word-boundary term set, `git grep -iocE '\b(witch|witches|witchcraft|sorcer[a-z]*|malefic[a-z]*)\b'` summed → **20 matched lines across 12 files** (22 term instances). The frozen BEFORE sentence says "19 times across 10 files". The difference is 2 files and 1 line; the owning-surface conclusion is unaffected. Flagged for the critic, not asserted as a claim failure.

## 2. O surface — lane by lane

| lane | O hits (knowledge) | O hits (SKILL.md) | note |
|---|---|---|---|
| all 20 sibling lanes | **0** | **0** | no sound-law, sound-change, phonology, proto-lexicon or rules-applier material anywhere in a sibling lane |
| filename sweep | — | — | every `*sound*` / `*phonolog*` / `*lautgesetz*` path in the fleet is inside `kotodama-shokunin` (corpus entry, gate, fixtures, frozen replays, and the supplement example) |
| `.tsv` adjacency tables (kagi, tabi) | 0 | — | no kotodama-related rows at all |
| `--rules`/`rules.json` tooling sweep | — | — | only `mado-shokunin/quality/**` matches, all Hyprland rule/geometry tooling — different sense of "rules" |

So: no sibling applier, no sibling gate, no sibling schema that the new tool could duplicate.

## 3. In-lane adjacency map for claim D (the work the new entry must point one-way)

`corpus/knowledge/myth-symbol/` already holds the neighbours. The new entry is the *accusation* arm; each neighbour keeps its own arm.

| neighbour | owns (cite) | the new entry must not restate |
|---|---|---|
| `myth-symbol/ordeal-judicial-proof-rituals.md` | the proof ladder and the ordeal menu; §1 one-way list at `:12`; its three r81 anchors at `:20-30`; `- couples:` at `:6` | the ordeal as proof technology — the new entry's proof arm cites this entry and must **not** re-cite the r81 ordeal rows |
| `myth-symbol/binding-speech-complex.md` | the curse and the oath as speech acts (§4–§5, `:99,140`) | the curse's mechanics; the new entry owns the *accusation* the curse is alleged to justify |
| `myth-symbol/divination-omen-systems.md` | the reading licence and omen archives (`:115,130`), Azande witchcraft diagnosis as one row (`:112`) | the diagnosis technique; the new entry owns who is accused and by what grammar |
| `myth-symbol/purity-pollution-boundary-systems.md` | the boundary/anomaly engine and who counts as polluted (§3, §5, `:41,65`) | the pollution taxonomy |
| `myth-symbol/amulets-talismans-apotropaic-marks.md` | protection objects, `witch-bottle` practice as a case (`:72,102,104,158`) | the countermeasure objects |
| `myth-symbol/sacred-kingship-mythic-charter.md`, `guest-right-hospitality-law.md`, `marriage-alliance-bridewealth.md` | other law/institution arms | their subject matter |
| `linguistics/politeness-taboo-euphemism.md`, `taboo-strata-lifecycle.md` | taboo naming, euphemism cycles, avoidance strata (`:71,80`; `:27,58`) | the naming-avoidance mechanics the vocabulary set depends on |
| `linguistics/historical-linguistics.md` | semantic drift and the ordered law list (`:182-190`, `:250`) | the etymology method; the new entry cites it for the vocabulary set |
| `verification/citation-format-and-source-registry.md` | the row/citation contract (`:9-32`) | how to cite; the new entry only obeys it |

**Placement.** The lane's partitions are `linguistics`, `myth-symbol`, `culture-material`, `synthesis`, `verification`, `civilizations` (`PROVINCE.md:10`). There is no social-institutions partition, and `civilizations/` is per-culture dossiers ("Mongol base — … historical reference and generative method, never fictional canon", `corpus/knowledge/civilizations/mongol.md:3`), not comparative method. A comparative institution entry therefore belongs to `myth-symbol`, next to `myth-ritual-theories.md` and `comparative-frameworks.md`; creating a new partition would be an unclaimed scope move.

## 4. In-corpus tool contracts for claim O

The closest contracts, and what the new tool must mirror or explicitly differ from.

| tool | its contract (file:line) | overlap | difference the new tool must state |
|---|---|---|---|
| `tools/check-craft-exercise.py` | `:1-33` docstring: "In-memory checker … Rebuilds the toy law engine from the JSON's `law_list.order`"; engine `:45-75` is four hardcoded functions `law_l1`–`law_l4` over characters; exits 0 clean / 1 findings / 2 `CRAFT-CLI-*`; `--selftest` drives subprocess CLI cases in a temp dir | the only existing ordered-sound-law executor in the lane | it **checks a supplied exercise** and cannot derive from arbitrary rules; rules are hardcoded, phonology is a five-vowel string test, there is no trace. The new tool is the generic derivation engine; it must not grow a verdict class |
| `tools/gates/phonology-sanity-gate.py` | `:5-28`: `0 clean / 1 findings / 2 could-not-evaluate` over a culture packet, one `FINDING <id>:` per line | both read segment-tokenised phonology | the new tool **transforms** data and has no findings: exit 0 = applied, exit 2 = input error. It has no exit-1 class, and its registry row must say so or a reader will take exit 2 for could-not-evaluate |
| `tools/assemble-d2.py` | `:1-10`: default writes, `--check` compares bytes without writing, `--selftest` writes only in a `tempfile` dir, runs from any cwd | the applier precedent (a tool that produces committed bytes) | the new tool writes only `--out`/`--trace` (never in place), and must reproduce a committed `expected.tsv` byte-for-byte, like `--check` |
| `tools/check-gate-registry.py` | `:2-10`: audits `## Gates and probes` rows against every `reports/round-*/accept-*.py`; a row covers an instrument when the path appears in the **entry-command cell**; `:30-63` requires 8 cells for `gate`/`probe` rows; `:73-80` counts `tools/*.py` without a row | grades the three rows claim O adds | the row is not prose: path in cell 3, 8 cells, and the tool must be a `tools/*.py` that the unrowed counter sees |
| `tools/check-cited-lines.py` | `:1-35`: `CITED_LINES_ERROR` on stderr, exit 2, "nothing on stdout", never a traceback | the label+exit-2 convention | `SOUNDLAW_ERROR:` mirrors this shape exactly |
| `tools/check-cited-records.py` | `:172`: prints `SELFTEST: %s (%d checks)` | the selftest line format | the frozen `selftest_re` (`^SELFTEST: PASS \((\d+) checks\)$`) is this lane's existing alphabet — do not invent a new one |
| `tools/replay-frozen.py` | `0` = recorded verdict reproduced, `1` = mismatch, `2` = could-not-evaluate (registry row at `SKILL.md:653`) | same 0/1/2 alphabet | its 0 means "a red verdict reproduced"; the new tool's 0 means "the transform ran". Same alphabet, different semantics — the row must name the transform sense |

**The row-count arithmetic.** Live at HEAD, read-only: `python3 tools/check-gate-registry.py --root .` prints
`GATE-REGISTRY: 2 missing / 74 registered / 63 instruments / 0 dead` (missing = `accept-d84.py`, `accept-o84.py`), `GATE-REGISTRY-INFO: 25 tools without a row`, rc 1. The frozen floors are `>= 77 registered`, `>= 63 instruments`, `<= 25 unrowed` (`reports/round-84/claims.json`). 74 + 3 rows = 77 exactly; the new tool adds one `tools/*.py`, so its own row is what keeps the unrowed count at 25. Three rows, not four, not two.

## 5. Contradiction and delta log — frozen bytes, the wave spec, and this seat's text

Both counters read their constants from `reports/round-84/claims.json` **at `--freeze`**, never from the graded tree. The lane's freeze has three commits, all pre-dispatch:

| commit | time | subject |
|---|---|---|
| `3ca2cf28` | 2026-11-04 10:14:29 | "round-84: freeze claims, counters and counter library before any claim artifact" |
| `e160a72e` | 10:28:17 | "freeze revision r1 — entry section headings aligned to the house shape (pre-dispatch, no claim artifact)" |
| `7e6ee2f8` | 10:31:06 | "freeze revision r2 — SOUNDLAW_ERROR shape marker accepts the label constant (fixture-proven, pre-dispatch)" — **HEAD** |

Topology verified: `81499ee` (base) → `3ca2cf28` → `e160a72e` → `7e6ee2f8`; base and all freeze revisions are ancestors of HEAD, and the freeze is not an ancestor of base.

Three texts now have to be kept apart:

| text | written | which constants it carries |
|---|---|---|
| `spec-v1.json` (context + seat prompts) and `w1-dispatch.json` | 10:31:18, twelve seconds after r2 | **r2** — `## 2. Six design decisions`, `## 3. Attested anchors`; the old heading strings are absent; `ScribeEntryWitch`'s prompt repeats the r2 headings |
| this seat's assignment text | captured before r1 (it quotes the 10:14 freeze) | **`3ca2cf28`** — `## 2. The decision table`, `## 4. Attested anchors`, `SOUNDLAW_ERROR: <label>` |
| `reports/round-84/accept-d84.py:15-16` (docstring) | written at the 10:14 freeze | **`3ca2cf28`** — same old headings; the code at `:147`/`:155` reads the block, so the docstring is documentation-only drift |

The constants that moved:

| constant | at `3ca2cf28` | at `7e6ee2f8` (HEAD, and in the wave spec) |
|---|---|---|
| `entry84.decision_heading` | `## 2. The decision table` | `## 2. Six design decisions` |
| `entry84.anchors_heading` | `## 4. Attested anchors` | `## 3. Attested anchors` |
| `tool84.shape_markers` | `SOUNDLAW_ERROR:` | `SOUNDLAW_ERROR` (bare substring) |
| `tool84.semantics`, `tool84.min_trace_columns` | absent | added: 5-column trace; `#` only as first `pre` / last `post` |

The heading matcher is exact string equality on the stripped line (`reports/round-84/accept-d84.py:66-77`, `l.strip() == heading`), and the two headings are read at `:147` and `:155`. So a freeze mistake is loud: the counter prints `no '## 2. The decision table' section`.

Consequences:

1. **Grade at r2.** All counters run with `--freeze 7e6ee2f8`. Grading at `3ca2cf28` — the freeze this seat's assignment names — fails a correct entry on `DECISIONS`/`ANCHORS` while `ENTRY`, `SECTIONS`, `LINT`, `ROWS` and `SOURCED` pass; that signature identifies the freeze error, not a content defect.
2. **No writer action.** The scribe, reviewer and critic were dispatched from the r2 spec; their prompts already carry the house-shape headings.
3. **The hedge is rejected.** Both `## ` sections present would satisfy either freeze, but duplicates the decision table and requires a second ≥20-bullet anchor block — roughly 40 anchors against a four-row id budget.
4. **The label is unchanged either way.** r2 widened the tool *shape marker*, not the printed label; `accept-o84.py`'s negative leg still requires the literal `SOUNDLAW_ERROR:` in stderr.

Other frozen detail the dispatch prose compresses, and that the executors must not miss:

1. `accept-o84.py:117` runs the tool as `["--selftest"]` — the **flag**, not the `selftest` positional the prose CLI shows. The tool must accept `--selftest`.
2. `accept-o84.py:158-178` plants three specific malformed inputs: a missing rules file, a rules file that is not JSON, and a rule whose `from` is `""` (`{"name":"x","from":"","to":"a","pre":[],"post":[]}`). All three must exit 2, stderr must contain the literal `SOUNDLAW_ERROR:` **with the colon**, and stderr must not contain `Traceback`.
3. `accept-o84.py:124-156` grades the demo strictly: `C.one_line` returns `None` when two or more stdout lines match the summary regex (`reports/round-84/counterlib.py:106-109`), so the summary must be the unique matching line; the trace line count must equal the summary's `c` exactly (`len(tl) == c`); every rule name must appear in the trace; and `--out` must equal `examples/sound-laws/expected.tsv` byte-for-byte against the lands blob.
4. `accept-o84.py:180-196` requires the tool's row to be found by `cells[2]` (the entry-command cell) and requires `check-gate-registry.py` to exit 0.
5. `corpus/SOURCES.md` currently ends at `S913` (the last landed registry row), so the four ids this round opens are free; no id collision with the r81 ordeal rows.
6. The two claims' write sets are disjoint by construction and each names the other's paths as foreign: D owns `corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md` + `corpus/SOURCES.md`; O owns `tools/apply-sound-laws.py`, `examples/sound-laws/`, `SKILL.md`. The `SEPARABLE` legs fail on any cross-write, so the SKILL.md rows and the SOURCES rows cannot be written by the same hand without violating one of them.

## 6. Leftovers

Scratch was used only for the heading index and term lists; it is removed before this seat exits. No lane byte outside the two paths named by this seat was written.
