# ConnectorOverlap — findings (round-84 w1)

Seat: ConnectorOverlap · milestone r84-v1 · axes **adjacency**, **coverage** · read-only.
Raw scan (lane tables, hit lists, probe record): `.ufo/waves/round-84/w1/stage/ConnectorOverlap/overlap.md`.
Per the seat contract this file only reports; it does not edit, absorb, or re-scope anything.

## 1. Verdict, per surface

- **D (witchcraft/sorcery as an accusation institution): no sibling owner.** No lane's `corpus/knowledge` owns the surface (1 274 sibling knowledge files scanned; 0 owning headings, 0 owning topic lines), no lane's `PROVINCE.md` declares religion, ritual, folklore or the supernatural, and no lane's `SKILL.md` claims it. The only sibling with adjacent material is **lore-shokunin** (4 files under the strict term set, 2 more on the extended set), and its material is (a) the canon handoff target and (b) in-world fictional accusation records — not the comparative institution entry. One more strict hit is kengaku's telemetry metric ("raw accusations"), unrelated. The correct in-lane owner is `corpus/knowledge/myth-symbol/`, beside `ordeal-judicial-proof-rituals.md` and `myth-ritual-theories.md`.
- **O (ordered sound-law applier): no sibling owner, and no sibling applier to duplicate.** 0 matches for the entire sound-law/phonology/proto-lexicon term set across 1 274 sibling knowledge files and 18 sibling `SKILL.md` files; every `*sound*`/`*phonolog*` path in the tracked fleet trees (`.ufo` state excluded) is inside this lane. The nearest existing contract is **in-corpus**, not cross-lane: `tools/check-craft-exercise.py`, whose `law_l1`–`law_l4` hardcoded toy engine (`:45-75`) is the thing this tool generalises.

## 2. What the D entry must point one-way (and must not restate)

Every neighbour below is already landed; the new entry's `- couples:` line and a short §1 owner list are the only places it should name them. Evidence is from `corpus/knowledge/myth-symbol/ordeal-judicial-proof-rituals.md:6,12,20-30`, which is the house pattern for this exact move.

| neighbour | keeps | the new entry owns instead |
|---|---|---|
| `myth-symbol/ordeal-judicial-proof-rituals.md` | proof ladder, ordeal menu, inspection grammar, its own three r81 source rows | the accusation that precedes proof; **do not re-cite the r81 ordeal rows** |
| `myth-symbol/binding-speech-complex.md` | curse/oath as speech acts | the allegation that a curse was used |
| `myth-symbol/divination-omen-systems.md` | the reading licence, diagnosis technique | who gets accused, by whom, on what grammar |
| `myth-symbol/purity-pollution-boundary-systems.md` | boundary/anomaly engine, pollution carriers | the accusation's social selection |
| `myth-symbol/amulets-talismans-apotropaic-marks.md` | protective objects (witch-bottle at `:72,102`) | the accusation's countermeasure economy, one line at most |
| `linguistics/politeness-taboo-euphemism.md`, `taboo-strata-lifecycle.md` | taboo naming, euphemism cycle, avoidance strata | the vocabulary set only as far as the accusation needs it |
| `linguistics/historical-linguistics.md` | semantic drift, ordered law list (`:182-190`) | the etymological hand-off, one clause |
| `verification/citation-format-and-source-registry.md` | row/citation contract | nothing — it only obeys it |

Placement is not a free choice: the lane's partitions are `linguistics`, `myth-symbol`, `culture-material`, `synthesis`, `verification`, `civilizations` (`PROVINCE.md:10`), and `civilizations/` is per-culture dossiers ("historical reference and generative method, never fictional canon", `corpus/knowledge/civilizations/mongol.md:3`). A comparative institution entry is a `myth-symbol` entry; inventing a social-institutions partition is an unclaimed scope move.

## 3. The one-way handoff: what kotodama supplies, what stays here

The governing text is `corpus/knowledge/synthesis/worldbible-integration-contract.md` — canonical copy here, lore reads it read-only (`:13`), authority split at `:17`, ownership table at `:36-44`.

**For D.** Per the contract's `Myth / pantheon` row (`:43`) kotodama supplies *variant relations, ritual consequences, candidate epithets, attribution rules*; lore records *who holds a belief and whether any supernatural claim is true*; stop condition *sacred doctrine is not automatically world-fact*. Applied to this entry: kotodama may supply the vocabulary set, the accusation grammar, the proof ladder's hand-off, the confession's form, the slander law's shape, and the social functions as **design levers**. It may not supply "this community practised X", may not decide whether a supernatural claim is true, and may not treat a prescription as evidence of practice. The `Symbol / costume` row (`:44`) already states the general rule: *prescriptive dress rules do not prove actual practice* — the same sentence is the boundary for accusation norms. The entry's `- scope:` line should copy the ordeal entry's wording (`:10` in that file): decides nothing about what is true in any world, canon belongs to lore-shokunin, no claim about any living community's practice.

**For O.** Kotodama supplies the derivation engine and its trace as a reproducible design record; lore records which forms and dates are canon. `linguistics/historical-linguistics.md:250-252` already states this handoff for law lists and strata tables ("hand off the family tree, law lists with phase numbers, and the strata table; never record canon from them"). A derived form is a candidate, never an attested word; the trace shows what the rules did, not what any language did. Nothing about the applier belongs to lore.

**Current cross-lane state (do not absorb it).** The contract digest now reads `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`, which is exactly the digest lore records as **unacknowledged** (`lore-shokunin/corpus/README.md:79`); lore's intake row **CM-g is `uncovered`** (`:73`) with the frontier action at `:94`, and `lore-shokunin/PROVINCE.md:28` names the contract path fleet-root-relative and restates that lore holds no acknowledgement. That is a *lore* record to write, on lore's surface, with lore's own read receipt. This round produces no packet, so CM-g correctly stays open. Writing any acknowledgement into `lore-shokunin/` would be absorbing a sibling province and is outside this lane's write bounds.

## 4. The in-corpus contract the O tool must mirror or explicitly differ from

Closest first; the difference column is the text the SKILL.md row and the tool docstring should carry.

| tool | overlap | difference the new tool must state |
|---|---|---|
| `tools/check-craft-exercise.py:45-75` | applies ordered sound laws to forms | it *checks* one hardcoded exercise and cannot derive from a rule file; no trace; character-level, not segments. Do not make the new tool a second checker — that would duplicate a verdict it does not own |
| `tools/gates/phonology-sanity-gate.py:5-28` | same segment vocabulary | gates map `0 clean / 1 findings / 2 could-not-evaluate`. The applier has **no exit-1 class**: `0` applied, `2` input error. The row must say so, or a reader will misread exit 2 |
| `tools/assemble-d2.py:1-10` | produces committed bytes an example can pin | writes only `--out`/`--trace`, never in place; reproduces `examples/sound-laws/expected.tsv` byte-for-byte, like `--check` |
| `tools/check-gate-registry.py:2-10,30-63,73-80` | grades the registry rows | row is structural: path in the **entry-command cell** (cell 3), 8 cells for `gate`/`probe` kinds, and the tool must be a `tools/*.py` the unrowed counter sees |
| `tools/check-cited-lines.py:1-35` | `LABEL:` on stderr + exit 2 + nothing on stdout + no traceback | `SOUNDLAW_ERROR:` is the same shape; keep the colon (the counter's negative leg hardcodes `SOUNDLAW_ERROR:`) |
| `tools/check-cited-records.py:172` | `SELFTEST: PASS (n checks)` | reuse the exact line; the frozen regex is `^SELFTEST: PASS \((\d+) checks\)$` |
| `tools/replay-frozen.py` (row at `SKILL.md:653`) | 0/1/2 alphabet | its 0 means a recorded (possibly red) verdict reproduced; the applier's 0 means the transform ran. Different meaning, same alphabet |

## 5. Freeze revisions vs the seat text (stated, not smoothed)

The freeze has three commits, all pre-dispatch:

| commit | time | subject |
|---|---|---|
| `3ca2cf28` | 10:14:29 | "freeze claims, counters and counter library before any claim artifact" |
| `e160a72e` | 10:28:17 | "freeze revision r1 — entry section headings aligned to the house shape (pre-dispatch, no claim artifact)" |
| `7e6ee2f8` | 10:31:06 | "freeze revision r2 — SOUNDLAW_ERROR shape marker accepts the label constant (fixture-proven, pre-dispatch)" — **HEAD** |

Topology verified: `81499ee` (base) → `3ca2cf28` → `e160a72e` → `7e6ee2f8`; all three are ancestors of HEAD and the freeze is not an ancestor of base.

The wave that dispatched the seats was written at 10:31:18 — twelve seconds after r2 — and carries the **r2** constants in both the shared context and the per-seat prompts. Verified in `spec-v1.json`: `## 2. Six design decisions` and `## 3. Attested anchors` are present, the old strings absent, and the `ScribeEntryWitch` prompt repeats the r2 headings.

This seat's own assignment text is a **pre-r1 snapshot**: it says `## 2. The decision table`, `## 4. Attested anchors`, and prints `SOUNDLAW_ERROR: <label>: <detail>`. Those are the 10:14 (`3ca2cf28`) strings, and the counter's docstring (`reports/round-84/accept-d84.py:15-16`) still reproduces them.

What follows, exactly:

- **The operative target is r2.** Counters must be run with `--freeze 7e6ee2f8`. A run with `--freeze 3ca2cf28` grades a correct entry against obsolete headings.
- **The failure is diagnostic, not silent.** `accept-d84.py:147-149` prints `no '## 2. The decision table' section`, so a freeze mistake is visible as a heading name, not as a content verdict.
- **No scribe or reviewer correction is needed.** The only places the old headings survive as instruction are assignment texts captured before 10:28 (this seat's included) and the counter's docstring.
- **The dual-heading hedge is rejected on cost.** Carrying both `## ` sections satisfies either freeze, but duplicates the decision table and doubles the ≥20-bullet anchor block, which the four-row S-id budget would then have to supply at ~40 anchors.

The shape change is not cosmetic: r1 moved §2 to "Six design decisions" and the anchors section to §3, matching `corpus/knowledge/myth-symbol/ordeal-judicial-proof-rituals.md` — the "house shape" its subject names. r2 relaxed the tool marker from `SOUNDLAW_ERROR:` to the bare substring; the negative leg still hardcodes the colon, so the printed label is unchanged.

Other frozen detail the dispatch prose compresses, and that the executors must not miss:

1. `accept-o84.py:117` runs the tool as `["--selftest"]` — the **flag**, not the `selftest` positional the prose CLI shows. The tool must accept `--selftest`.
2. `accept-o84.py:158-178` plants three specific malformed inputs: a missing rules file, a rules file that is not JSON, and a rule whose `from` is `""` (`{"name":"x","from":"","to":"a","pre":[],"post":[]}`). All three must exit 2, stderr must contain the literal `SOUNDLAW_ERROR:` **with the colon**, and stderr must not contain `Traceback`.
3. `accept-o84.py:124-156` grades the demo strictly: `C.one_line` returns `None` when two or more stdout lines match the summary regex (`reports/round-84/counterlib.py:106-109`), so the summary must be the unique matching line; the trace line count must equal the summary's `c` exactly (`len(tl) == c`); every rule name must appear in the trace; and `--out` must equal `examples/sound-laws/expected.tsv` byte-for-byte against the lands blob.
4. `accept-o84.py:180-196` requires the tool's row to be found by `cells[2]` (the entry-command cell) and requires `check-gate-registry.py` to exit 0.
5. `corpus/SOURCES.md` currently ends at `S913`, so the four ids this round opens are free; no collision with the r81 ordeal rows.
6. The two claims' write sets are disjoint by construction and each names the other's paths as foreign: D owns `corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md` + `corpus/SOURCES.md`; O owns `tools/apply-sound-laws.py`, `examples/sound-laws/`, `SKILL.md`. The `SEPARABLE` legs fail on any cross-write, so the SKILL.md rows and the SOURCES rows cannot be written by the same hand without violating one of them.

## 6. Risks, each with the deciding byte and an owner

| # | risk | deciding evidence | owner |
|---|---|---|---|
| 1 | **Freeze selection** (D): grading with `--freeze 3ca2cf28`, or checking against the pre-r1 assignment text, fails a correct r2-shaped entry with `no '## 2. The decision table' section` — a dispatch error, not an entry defect | `accept-d84.py:66-77,147-155`; `claims.json` `entry84.*_heading`; wave spec written 10:31:18 | L1 (declare `--freeze 7e6ee2f8`) |
| 2 | **`--selftest` vs `selftest`** (O): the counter invokes the tool with the flag; the prose CLI shows a positional | `accept-o84.py:117` | executor |
| 3 | **Empty `from`** (O): the third malformed case is a rule with `from: ""`; without a semantic check it will be accepted and the leg fails | `accept-o84.py:158-178` | executor |
| 4 | **Summary must be unique**: two matching stdout lines make `one_line` return `None` → "no single summary line" | `counterlib.py:106-109`; `accept-o84.py:124-140` | executor |
| 5 | **Trace count**: `len(trace lines) == c` from the summary; printing a header or a per-rule total breaks it | `accept-o84.py:150-156` | executor |
| 6 | **TABLE-ID lint** (D): any `|` row carrying an S-id is a finding, so the decision table must anchor as `§3 a`, exactly as the ordeal entry does | `tools/check-cited-lines.py:1-35`; `ordeal-judicial-proof-rituals.md:22-29` | scribe |
| 7 | **Row-count arithmetic** (O): live `2 missing / 74 registered / 63 instruments / 0 dead`, floors `77 / 63`, unrowed cap 25 → exactly three rows (tool, accept-d84, accept-o84), path in cell 3 | live run cited in `overlap.md` §4; `claims.json` `tool84.*` | registry-row executor |
| 8 | **Cross-write** (D↔O): each claim lists the other's paths as foreign; `SEPARABLE` fails on any cross-write, so SKILL.md and SOURCES.md rows cannot come from the same hand | `claims.json` `entry84.own_paths/foreign_paths`, `tool84.own_paths/foreign_paths` | L1 |
| 9 | **Lore write-scope**: the contract digest is unacknowledged by lore; do not "fix" CM-g from here | `worldbible-integration-contract.md:13,17`; `lore-shokunin/PROVINCE.md:28`; `lore-shokunin/corpus/README.md:73,79,94` | all seats |
| 10 | **Real-persecution surface** (D): the topic is historical persecution and living traditions; the entry's scope line must keep the ordeal entry's no-claims-about-practice boundary | `ordeal-judicial-proof-rituals.md:10`; `PROVINCE.md:16-18` (Refuses: claiming or recording canon) | scribe + reviewer |

## 7. Verification the L1 can run after landing

All from the lane root; read-only except the counters' own scratch.

- `python3 tools/check-gate-registry.py --root .` → expect `GATE-REGISTRY: 0 missing / 77 registered / 63 instruments / 0 dead` and `GATE-REGISTRY-INFO: 25 tools without a row`, rc 0 (today: `2 missing / 74 / 63 / 0`, rc 1).
- `python3 tools/check-cited-lines.py corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md` → `CITED-LINES: 0 finding(s) in 1 file(s)`, rc 0.
- `python3 -B reports/round-84/accept-d84.py --root . --lands <lands> --freeze 7e6ee2f8 --work <dir>` and the same for `accept-o84.py`; on a correct entry a run at the wrong heading freeze fails only `DECISIONS`/`ANCHORS`, which distinguishes risk 1 from a real content defect.
- `git show 7e6ee2f8:reports/round-84/claims.json | python3 -c "import json,sys; b=json.load(sys.stdin)['claims']; print([c['entry84']['decision_heading'] for c in b if c['id']=='D'])"` → confirms the heading constant actually used at grading.
- `git -C <lane> grep -nE 'S91[4-7]' 81499ee -- corpus/SOURCES.md` → empty at base (the four ids this round opens are free); after landing, four rows, all `mined`, all `used-by` the entry.
- `node`/`python3` not needed for the last one: `git ls-tree -r --name-only <lands> corpus/knowledge | grep -c '\.md$'` → 258.

## 8. Coverage note

Every sibling lane was named and probed (`overlap.md` §1–§2): 20 lanes, 1 274 knowledge files, 21 `PROVINCE.md`, 18 `SKILL.md`, 2 adjacency-table sets, one fleet-wide filename sweep. The non-lane directories (`research/`, fleet `tools/`, `scripts/`, `templates/`, the empty `kumitate-shokinin/`) were checked and excluded with reasons. Nothing was left behind; scratch was removed at exit.
