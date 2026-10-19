- Seat: C04 | verifier (claim C) | round 43 | date 2026-10-19 | baseline `7ceff59`

# C04 — pre-landing contract audit 2: r42 C01 lithic spare

- Mission (verbatim, `reports/round-43/targets.json` seat C04): "Pre-landing audit 2: contract audit — the entry satisfies corpus/QUALITY.md (calibration present, living-practice flags, no canon claim, handoff target named) and the partition's naming/structure convention. Report pass/fail per clause."
- Writes: this fragment only. No corpus byte, no filed-round byte, no tool byte was written. No `run-validation.py` was executed (see §7).
- All measurements are read-only, at lane HEAD `7ceff59` (`git rev-parse --short HEAD` → `7ceff59`), 2026-10-19T16:55Z, from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

## 0. Verdict — BLOCKING: this is a duplicate-topic landing, not an unbuilt-slot landing

**CONTRACT AUDIT: FAIL (1 apply-blocking finding).** The C claim's pre-state is false at baseline. The lithic register is already owned: `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` (61,884 B) is tracked at HEAD and is the r42 C04 landing. The live partition is already at **26 myth-symbol files / 223 total** — the claim's own *before* figures — and those 26 already include the lithic entry. Landing the spare would reach 27/224 by adding a **second entry for the same register**, not by completing an unbuilt slot.

Per-clause summary (details §2-§3):

| clause | verdict |
|---|---|
| Q1 provenance (sources / to-verify) | PASS as authored; **FAIL as delivered** — the gap statement is stale at HEAD |
| Q2 calibration | PASS |
| Q3 coupling | PASS with two named defects (dangling `§Owed`; landed lithic owner not coupled) |
| Q4 usability | PASS |
| Q5 canon hygiene / handoff | PASS |
| N1 filename form | PASS |
| N2 topic uniqueness / one-owner rule | **FAIL (apply-blocking)** |
| N3 header field presence | PASS (9/9) |
| N4 header field order | PASS-with-note (review tier) |
| N5 single-line couples | PASS (3,831 chars, one physical line) |
| N6 fence stageability / digest | PASS (triple-backtick; 55,101 B; sha256 `6999a912…`) |
| N7 README index contract | **PENDING/FAIL by duplication** — the lithic row already exists |

## 1. The collision, proven at three independent layers

### 1.1 Live tree

```
$ git rev-parse --short HEAD
7ceff59
$ git ls-files corpus/knowledge/myth-symbol | wc -l
26
$ ls corpus/knowledge/myth-symbol/*.md | wc -l
26
$ git ls-files 'corpus/knowledge/**/*.md' | wc -l
223
```

`mineral-stone-symbolism.md` is in that listing. `git log --oneline --all -- corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` → `7ceff59 round-42: NOT ADMITTED on C (O verified) — N6 successor extractor, 3 myth-symbol entries, collision ruling + overwrite restore`; the r42 commit's name-status adds the file as `A`.

### 1.2 The filed record names the duplicate explicitly

- `reports/round-42/validation.json` → `claims.C.measurement.legs.C1.measurement.ruling`: "C01 and C04 authored the same lithic register mid-wave; C04 lands, C01 routes as the named spare".
- `reports/round-42/cov/C05-audit.md:262-272` (D1): "C01 and C04 declare the same topic at the same landing path ... would leave the lithic register owned twice — the partition's one-owner rule is violated either way."
- `LOG.md:3804` heads "Round 42 NOT ADMITTED on C"; `LOG.md:3812-3814` reads "three entries landed (26/223) ... C01/C04 authored the same lithic register; integrator ruling lands C04, routes C01 as the named spare."

### 1.3 The index already carries the landed row

`corpus/README.md:5` opens `revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19)` and states that "a fourth draft (C01's lithic register) collided with C04's and is routed as a named spare by integrator ruling." `corpus/README.md:205` says `## myth-symbol/ (26)`; `corpus/README.md:219` is the `mineral-stone-symbolism.md` row, and its topic text is **byte-identical** to the landed entry's `- topic:` line (2,077 chars each; comparison output in §6).

The claim says the before-state is "myth-symbol 26 (lithic slot named but unbuilt ...)". The number 26 is right; the parenthetical is not. The r42 arithmetic shows why: r42 expected four distinct topics, delivered three distinct topics plus one duplicate, so the count stopped at 26/223. The missing 27th was never a distinct unbuilt topic.

### 1.4 Consequence if applied

- Byte-wise, a differently-named target (e.g. `lithic-register.md`) would not overwrite an existing file — but it would put two entries on one topic, double the partition's lithic coverage row, and violate the one-owner rule the r42 audit named.
- `corpus/README.md` would gain a second lithic-register row. The sweep (`reports/round-28/readme/sweep.py`) tests rows-vs-files, missing rows, topic byte-equality and totals; it has **no duplicate-topic test**, so a green `224 == 224` would not detect this. Mechanical green is not a coverage verdict.
- The spare's own gap statement would ship false (see D2).

This is the blocking finding. The remaining clauses are reported so that a re-scoped landing (new topic) or an explicit successor-revision decision has the spare's contract state on record.

## 2. corpus/QUALITY.md — clause by clause

### Q1 — Provenance (`corpus/QUALITY.md:5-8`)

**PASS as authored.**
- External works are declared unread and marked: `reports/round-42/cov/C01-mineral-spare.md:9` (Pliny *NH* 37, "**Not consulted this round** (offline)"), `:10` (Marbod / Philippe de Thaon, "**Not consulted this round**"), `:11` (Taube, registered in-lane with DOI, "cited at that in-lane status; not re-fetched"), `:194` (page-level claims and etymologies marked `(to-verify)`).
- No invented source was found: every external name has an in-corpus registration or a bibliographic record, stated at `:23`.
- In-repo pointers: **54 repo-path tokens (31 distinct), 0 unresolved**; **50 bare `.md` tokens (21 distinct), 0 ambiguous, 0 zero-hit** (§6 commands). This corroborates the r42 C05 audit's "0 unresolved pointers/couples" at `C05-audit.md:32`.
- The `- verified-at:` transcript pointer resolves: it cites "the author fragment's Citations"; `reports/round-42/cov/C01-entry-1.md:528` is a `## Citations` section, and `:274` records "31 tokens, 0 unresolved".

**FAIL as delivered — the gap statement is stale.** At the landing HEAD the entry would assert (`:7`): "the partition's register family is **closed at five plus flora and the lithic slot is named but never built**"; "**no filename** carries `mineral`, `stone`, `gem` or `lithic` ... → **0 hits**"; "`grep -rli 'lapidary' corpus/knowledge/` → **2 files**". Re-run at `7ceff59`:

```
$ ls corpus/knowledge/*/ | grep -icE 'mineral|stone|gem|lithic'
1
$ grep -rli 'lapidary' corpus/knowledge/ | wc -l
4
$ grep -rlEi -- '^- topic:.*(mineral|gem|lapidary|lithic|precious)' corpus/knowledge/
corpus/knowledge/linguistics/sound-symbolism.md                 # substring artefact
corpus/knowledge/myth-symbol/death-afterlife-eschatology.md     # substring artefact
corpus/knowledge/myth-symbol/mineral-stone-symbolism.md         # the owner
```

The sweep in the spare is dated to `ac47c78` (`:24`), so it is honest as a *dated* measurement — but false as a delivered claim. QUALITY #1's bar is a checkable claim; this one checks and fails at landing. If the spare were ever re-scoped and landed, the gap field must be re-measured at the landing HEAD (and the topic would still be owned).

### Q2 — Calibration (`corpus/QUALITY.md:9-12`) — PASS

`C01-mineral-spare.md:21` is a full calibration field, and `## 11. Calibration bank` (`:182-196`) expands it:
- lapidary genre: usable as genre, **discredited as physics** (`:184`);
- sympathetic magic: **discredited as explanation**, retained only as an emic folk model (`:186`);
- "crystal energy" / chakra-mineral / gem therapy: **modern invented tradition** (`:188`);
- Taube, the choshen/zodiac reading, and the Emerald Buddha: attributed, with the in-lane cautions quoted (`:190`);
- living-practice constraint declared binding (`:192`), with DR-MS-15 at `:179` and the named-knowledge-holder rule;
- house method explicitly separated from findings (`:21`, `:194`).

No framework is left unstatused. The "known thin spots" subsection (`:194`) names exactly what was not retrieved. This is the strongest clause of the draft.

### Q3 — Coupling (`corpus/QUALITY.md:13-15`) — PASS with two named defects

`- couples:` at `:22` names myth-symbol, linguistics, culture-material, synthesis and verification targets plus a handoff target. All 54 repo-path tokens resolve; all 21 distinct bare basenames resolve uniquely (no ambiguity).

- **Defect 1:** the line says "the **quarry/mine production side**, which no corpus entry owns at this HEAD (owed — see §Owed)" — **there is no `## Owed` section** (headings enumerated in §6: §1-§13 only). The pointer is dead as written; either add the section or drop "see §Owed".
- **Defect 2:** the line does **not** name `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`, the landed owner of the same register (`grep -c 'mineral-stone-symbolism'` on `:22` → 0). If the spare were ever landed, its nearest neighbour and duplicate would be uncoupled; as filed, the omission is evidence the draft predates the landing.

Both are review-tier, not blockers: the coupling leg is present and resolves.

### Q4 — Usability (`corpus/QUALITY.md:16-17`) — PASS

`## 10. Decision record` (`:161-181`) carries 16 ids (DR-MS-01..16); §2/§3/§4/§5/§6/§7 are typology and decision tables; `## 9. Build order` (`:147-159`) is an 11-step protocol; `## 12` is a NON-CANON worked example with a decision record; `- recheck:` (`:25`) gives five concrete triggers. No essay-only sections.

### Q5 — Canon hygiene (`corpus/QUALITY.md:18-20`) — PASS

Boundary statements: `:6` "Reference knowledge and method only; canon decisions belong to lore-shokunin"; `## 12. NON-CANON worked micro-example (illustrative only — decides nothing)` (`:198`); `## 13. Handoff` (`:212`) → lore-shokunin first. The strict no-bleed scan (`promoted|promotion|promote|cleared|clearance|closure|closed as|signed off|green-lit`) → **0 hits**; every `canon` occurrence is a boundary/negation or the NON-CANON heading. No admission, clearance or promotion claim.

## 3. Partition naming/structure convention

Convention sources: `reports/round-42/plan/P01-plan.md:409-431` (§2.2 entry contract) and `reports/round-35/cov/C12-audit-runbook.md:28-44` (the R35-4F-1 reading).

| # | clause | reading | verdict |
|---|---|---|---|
| N1 | filename form | kebab-case, topic-descriptive, no numeric prefix; all 26 live slugs conform | PASS |
| N2 | topic uniqueness | the topic is already owned by `mineral-stone-symbolism.md` | **FAIL (blocking)** |
| N3 | header field presence | 9 head fields — topic, gap filled, sources, calibration, couples, source, verified-at, recheck, scope; 4/4 required legs, round-10 5/5, optional calibration | PASS |
| N4 | field order | contract states `# Title`, then `- gap:` / `- gap filled:`, then `- topic:`; the spare is topic (`:6`) then gap (`:7`). Neighbours plant/mineral/sacred-topography are gap-first; `color-symbolism.md` is topic-first with no gap field | PASS-with-note (review tier; presence reading passes) |
| N5 | single-line couples | `:22` is one physical line (3,831 chars) — satisfies the H1 no-wrapped-field hazard | PASS |
| N6 | fence / stageability | triple-backtick fence opens `:3`, closes `:219`; apply range `:4-218` = 215 lines / 55,101 B / sha256 `6999a9123578bf8f…` — matches the r42 C05 pin (`C05-audit.md:51`: `6999a912… 55 101 B / 215 wc -l`) | PASS |
| N7 | README row | a row must be the entry's `- topic:` byte-equal and placed in filename order (`P01-plan.md:401`); the landed row at `corpus/README.md:219` already occupies the lithic slot | **PENDING/FAIL by duplication** |
| N8 | no overwrite | the spare itself proposes no path; free slugs exist but none cures the topic duplicate | **FAIL by duplication** |

## 4. Defect register

- **D1 (apply-blocking). Duplicate topic.** The spare and `mineral-stone-symbolism.md` both own "the lithic register"; the latter landed in r42 and is indexed. Landing the spare produces two owners, not a new slot. Evidence: §1.
- **D2 (major, delivered-falsity). Stale gap statement.** `:7`'s absence sweep is dated `ac47c78` and fails at `7ceff59` (filename hits 0 → 1; lapidary 2 → 4; the topic-line owner is now present). Evidence: §2 Q1.
- **D3 (review). Dangling `§Owed`.** `:22` cites a section that does not exist. Evidence: headings are §1-§13 at `:28-212`; `grep -n 'Owed'` returns only `:22`.
- **D4 (review). Field order.** `- topic:` before `- gap filled:` against the r42 contract's stated order; presence checks still pass. Evidence: §3 N4.
- **D5 (contingent, apply-blocking if C proceeds). README second lithic row.** Adding a row for a free slug would make the index carry two lithic-register entries; the sweep cannot detect it (no duplicate-topic test). Evidence: §1.4.
- **D6 (review). Nearest-neighbour coupling omitted.** `:22` does not name `mineral-stone-symbolism.md`, the landed owner of the same register (`grep -c` on the line → 0). Evidence: §2 Q3 defect 2.

No defect was found in calibration, canon hygiene, usability, or pointer resolution. The two Q3 coupling defects (D3, D6) and the field-order note (D4) are review-tier. The draft is a contract-strong entry for a topic that is already owned.

## 5. Disposition options (this seat reports; the parent decides)

- **A — do not land the spare (recommended).** Record C as no-move/carry at 26/223/rev 2.4. This is the only option that does not double-count coverage. The sweep already reads green at baseline (§6), so the tree needs no repair.
- **B — re-scope to a genuinely unbuilt topic.** A fresh absence sweep at `7ceff59` is required. r42's alternates are not clean at this HEAD by a broad probe: monster/monstrous/terato/ogre topic-line hits 2; spirit/demon/jinn 6; marriage/alliance 3 — all by-product or substring hits, but each must be dispositioned, not assumed. This seat did not select a topic.
- **C — successor revision of `mineral-stone-symbolism.md`.** If the spare's material is judged better than the landed entry, that is an explicit replacement/merge with a diff audit, not a coverage landing; it cannot be done under claim C's "no existing entry overwritten" rule without an integrator ruling.
- **Not an option:** landing under a free slug (`lithic-register.md`, `stone-gem-metal-symbolism.md`, `stone-gem-and-metal-symbolism.md`, `mineral-symbolism.md` are all free) merely to satisfy the count. That avoids a byte overwrite but still creates a second owner.

## 6. Measurements (all read-only; lane root; 2026-10-19T16:55Z; HEAD `7ceff59`)

```
$ git rev-parse --short HEAD                         -> 7ceff59
$ git ls-files corpus/knowledge/myth-symbol | wc -l  -> 26
$ find corpus/knowledge -name '*.md' | wc -l         -> 223
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25,
       "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0

$ git log --oneline --all -- corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
7ceff59 round-42: NOT ADMITTED on C (O verified) — N6 successor extractor, 3 myth-symbol entries, collision ruling + overwrite restore

$ sha256sum reports/round-42/cov/C01-mineral-spare.md
2b9326e351de0e324bce3e71d45390c4a03e838138902ffcf23a971704ef6156

$ sed -n '4,218p' reports/round-42/cov/C01-mineral-spare.md | wc -c
55101
$ sed -n '4,218p' reports/round-42/cov/C01-mineral-spare.md | sha256sum
6999a9123578bf8fbae4ecfdcef5e811eb764f3aef7522830029dfc8f74dbd89  -
```

Pointer audit (python regex over the whole spare):
- `(corpus|tools|reports|examples)/….md|json|py|yml|yaml|tsv|txt` tokens: 54 total / 31 distinct / **0 unresolved**.
- bare `*.md` tokens: 50 total / 21 distinct / **0 ambiguous / 0 zero-hit** against `corpus/knowledge/*/*.md`.
- headings: `## 1` … `## 13` only; no `## Owed`.
- head fields in order: `topic` (:6), `gap filled` (:7), `sources` (:8), `calibration` (:21), `couples` (:22), `source` (:23), `verified-at` (:24), `recheck` (:25), `scope` (:26).
- `verified-at` ISO date: 2026-10-19 — present.
- strict no-bleed hits: 0.
- `- couples:` physical-line length: 3,831 chars (single line).
- README row vs landed entry topic: 2,077 chars each, byte-identical `True`.
- candidate target paths: `mineral-stone-symbolism.md` TAKEN; `lithic-register.md`, `stone-gem-metal-symbolism.md`, `stone-gem-and-metal-symbolism.md`, `mineral-symbolism.md` free.
- landed entry title (`mineral-stone-symbolism.md:1`): "Stone, gem and metal symbolism — the lithic register: the lapidary code, material prestige, and the quarry-to-regalia chain"; spare title (`C01-mineral-spare.md:4`): "Stone, gem, and metal — the lithic register: material properties as symbol, the scarcity ladder, and the lapidary as an institution".

## 7. What this seat did not do

- Did not run `reports/round-43/run-validation.py` or any round runner (absolute rule; the file does not yet exist at this writing).
- Did not write, stage or edit any byte under `corpus/`, `tools/`, or `reports/round-1..42/`; the only write is this out file.
- Did not treat the spare's dated probes as current claims; every sweep above was re-run at `7ceff59`.
- Did not fetch any external source (no network); no external source was independently verified beyond in-corpus pointer resolution — the source audit is C03's seat.
- Did not judge scholarship, admit any entry, or decide canon.
