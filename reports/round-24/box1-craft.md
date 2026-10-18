# Box 1b — coverage of craft (promotion-review box 1, substance leg)

- Round: 24 (operator regimen: loop 2, GLM round 2 of 2)
- Reviewer: round-24 swarm seat, **non-author** (authored none of this lane's artifacts; fresh-context verification seat)
- Subject: SHONEN.md box 1 — "SKILL.md contains real decision tables, error patterns, checklists, cited sources" — restricted here to the **coverage-of-craft** question: do the tables cover the lane's actual craft surface (typed pipeline, handoff, gates, corpus rules) without generic filler?
- Method: enumerated the repo's executable + corpus surface, mapped it against SKILL.md's sections, then deep-sampled 15 table rows/probes and resolved every citation against the cited bytes (file:line read, or re-run for the one gate claimed read-only).
- Baseline revision: 8fbcee9 (round-24 claim declaration); claims.json `baseline_revision` b5d9844 (pre-declaration); no lane artifacts were modified by this review.

## Verdict: **verified-with-conditions**

Box 1's substance claim holds: the tables are real, domain-specific, and citation-anchored — 10 of 15 deep samples matched their cited ground truth exactly, one gate row was re-run live and passed, and zero fabricated citations were found (every sampled pointer resolved to genuine content in the named file). Conditions are named below (coverage gaps + drift); they are fixable row-level edits, not structural failures.

## 1. Craft-surface coverage matrix

Actual surface inventoried from `tools/` (13 scripts + `harness/` 4 + `gates/` 10 py), `examples/culture-d2|d3|d4/`, and `corpus/knowledge/` (6 subtrees).

| Craft surface | SKILL.md coverage | Evidence |
|---|---|---|
| Typed pipeline | **Covered deeply** — four dedicated sections with named executable authorities | label typing (`SKILL.md:31-74`, authority `tools/d2-typed-labels.py`), slot-label routing (`SKILL.md:131-187`, `tools/gates/typed-pipeline-gate.py` legs), derivation replay (`SKILL.md:189-242`), family-clean projection (`SKILL.md:244-350`) |
| Handoff semantics | **Covered** — claim uncertainty typing, contract cites, envelope gate, checklist item | `SKILL.md:77-128` (uncertainty table; `tools/harness/packet_uncertainty.py --selftest`), `worldbible-integration-contract.md` cites at :82, :88, :101, :183-region; `handoff-packet-check` gate row `SKILL.md:496`; checklist item `SKILL.md:419-420` |
| Gates | **Mostly covered** — 12-row inventory with entry commands, verdict maps, write scopes (`SKILL.md:488-501`) | all 7 legacy gates, frozen-replay, uncertainty-inventory, D2 drift, craft-exercise, battery present; handoff-packet-check re-run live (sample 13) |
| Corpus rules | **Covered** — corpus map, errata protocol, source-to-system constraint tables, calibration statuses | `SKILL.md:422-442` (map), :444-459 (using-the-evidence), :521-544 (round-5/6 constraint tables), checklist :408-420 |
| D3 bounded drill | Covered | `SKILL.md:546-598` (two gate rows, condition table, replay checklist) |

**Gap — 7 real executables never named in SKILL.md** (verified by exact-string grep, 0 hits each):

| Missing executable | Size | Materiality | Evidence it is live craft |
|---|---|---|---|
| `tools/exercise-handoff-e2e.py` | 4,612 lines | **High** — the v1/v2/v3 end-to-end handoff exerciser (assemble → links → uncertainty → gate, foreign-cwd validation); the craft's principal handoff executable | docstring `tools/exercise-handoff-e2e.py:1-55`; used in LOG.md |
| `tools/assemble-d2-typed.py` | 472 lines | Medium — the D2 typed-packet adapter that originated the routing-row craft; SKILL.md's routing section describes its exact semantics but cites only the D4 twin | docstring `tools/assemble-d2-typed.py:1-40` |
| `tools/gates/d4-assembly-check-gate.py` | 62 lines | Medium — **live frozen-pinned gate**, absent from the gates inventory table | pinned in `tools/gates/frozen/round-18/README.md:18` and `tools/gates/frozen/round-22/d4-repin/freeze-receipt.json:37` |
| `tools/gates/d4-typed-labels-check-gate.py` | 60 lines | Medium — **live frozen-pinned gate**, absent from the gates inventory table | `tools/gates/frozen/round-18/README.md:17`; `freeze-receipt.json:38` |
| `tools/harness/packet_links.py` | — | Medium — the claim-to-record link resolver (the round-12 rejection remedy); the uncertainty section requires links that resolve (`SKILL.md:79-80,389`) but never names its executable | docstring `tools/harness/packet_links.py:1-8` |
| `tools/harness/receipt_guard.py` | — | Low — internal preflight helper | docstring `tools/harness/receipt_guard.py:1-5` |
| `tools/harness/r8_checks.py` | — | Low — internal round-8 fix module | docstring `tools/harness/r8_checks.py:1-5` |

A cold-run reader building the lane's gate/tool inventory from SKILL.md alone would miss all seven; two are gates the frozen replay actually launches.

## 2. Deep sample — 15 rows/probes resolved against ground truth

| # | SKILL.md row (line) | Ground truth checked | Result |
|---|---|---|---|
| 1 | Slot-routing row 1, `SKILL.md:148` — gate leg `L3-routing-consistency` `:736-753`, failure names "holds … vs routed …" | `tools/gates/typed-pipeline-gate.py:736-753` | **EXACT** — check at :750-753, message `"holds %s vs routed %s; owed slots %s vs routing %s"` verbatim |
| 2 | Routing T1, `SKILL.md:158-163` — `ROUTED_KINDS = ("translated-label",)` at `:65` | `tools/assemble-d4-typed.py:65` | **EXACT** |
| 3 | Routing T2 / round-trip class, `SKILL.md:164-167,210` — rename `garment:`→`garment_gloss:` in place, never re-serialize, `:296-310` | `tools/assemble-d4-typed.py:296-313` | **VERIFIED** — `text_payload` docstring :297-312 states rename-not-delete and the regex-corruption class; transform loop begins :313 |
| 4 | Uncertainty `partial` row, `SKILL.md:100` — BR05 "Behistun cross-version leg … remain[s] unverified" at `reports/round-11/handoff/packet.md:108` | same file :108 | **EXACT** — BR05 row carries the quote with `partial-support` wording |
| 5 | Label-typing T3, `SKILL.md:56-58` — five borrowed-strata discriminators from `loanword-material-dating.md:43-57` | same file :43-60 | **VERIFIED** — §3 heading at :43; the five map 1:1: dated witness + usage status (:46), etymon/donor/carrier separation (:47), recurring correspondences (:48), donor-side chronology (:49), register clustering (:51); diagnostics table :53-60 |
| 6 | Error pattern, `SKILL.md:374` — imported prestige terminology cite `loanword-material-dating.md:57` | same file | **DRIFT** — content ("Dictionary selection bias; imported prestige terminology for local goods") is at **:59**; :57 is the donor-innovation row |
| 7 | Error pattern, `SKILL.md:372` — clock conflation cite `:26,60` | same file | **HALF** — :26 exact (Lexical clock ≠ referent arrival); :60 off (TPQ/TAQ bounds at :36-39, sense–referent pairing at :63; :60 is the purism row) |
| 8 | Error pattern, `SKILL.md:375` — curatorial label cite `costume-language-coupling-table.md:43` | same file :43 | **EXACT** — "A modern curatorial label becomes an attested historical native word" |
| 9 | Error pattern, `SKILL.md:376` — sound laws vs translations cite `era-language-staging.md:124` | same file | **DRIFT** — content ("Apply sound laws to an inherited spoken label; separately track … translation, exonym, or official replacement") is at **:127**; :124 is the costume/style-period row |
| 10 | Label-typing grounding, `SKILL.md:38` — `era-language-staging.md:108-124` | same file | **VERIFIED** — §7 "…type every label" heading at :111, label-type table through :124 |
| 11 | Family-clean T4, `SKILL.md:316-324` — 12 holds; supersedes pre-fix projection `cbcf997f…`, projector `76536a92…` | `examples/culture-d4/expected-holds.json` | **EXACT** — counts 12/0/0 (:11-15), six GAR + six LEX-GAR holds, `supersedes_pins` digests match verbatim (:7-10) |
| 12 | Passenger-rows measured instance, `SKILL.md:215` — "expected file **carries** 3 `D2L-RANK` holds + 1 note … each 0 hits" (2026-10-18T11:32Z) | same JSON | **STALE-BUT-DISCLOSED** — current file has 0 such rows (round-22 repair, `revision_note` :6); the removal is disclosed in SKILL.md itself (T4 :316-324; round-25 commitment :333-350). Present-tense "carries" now describes only the pre-fix state |
| 13 | Gates row `handoff-packet-check`, `SKILL.md:496` — `--selftest`, read-only | re-run: `python3 tools/gates/handoff-packet-check.py --selftest` (TMPDIR=$PWD/.scratch) | **LIVE PASS** — exit 0: "fixture findings 11 across 9 ids … clean control exit 0 … malformed inputs exit 2; CLI verified from another cwd" |
| 14 | Decision-table rows, `SKILL.md:22-29` — corpus anchors | `corpus/knowledge/…` | **VERIFIED** — all six row anchors exist: `conlang-methodology.md`, `naming-systems.md`, `era-language-staging.md`, `dress-through-eras.md` + `costume-semiotics.md`, `consistency-verification-checklist.md` |
| 15 | Checklist item 2 + crosswalk, `SKILL.md:414-416,109` — S/C/H/R/U/V at `source-discipline-calibration.md:67` | same file :67 | **EXACT** — the S/C/H/R/U/V status line is verbatim at :67; note the file lives in `corpus/knowledge/synthesis/` (correctly prefixed at :414; the :109 bare cite sits under a `corpus/knowledge/verification/` crosswalk header — path ambiguity only) |

Citation integrity summary: 15/15 sampled pointers resolve to real content in the named file; 0 fabricated sources; 3 pointers off by 2–3 lines (#6, #7 second pin, #9); 1 present-tense row superseded by a disclosed repair (#12).

## 3. Generic-filler test

No sampled row is generic filler. The decision table's six rows name domain pipelines and forbidden moves tied to named corpus files (#14), not generic advice. The error-pattern tables (~35 rows, `SKILL.md:354-393`) are defect-class-specific with file/line cites; the typed-pipeline sections carry executable authorities with leg names, line pins, and measured instances. The only stylistically generic block, "Boundaries (hard)" (`SKILL.md:395-406`), is a refusal-scope statement where generality is the point. Cosmetic defect noted: stray unbalanced code fences at `SKILL.md:129` (four backticks), `:154`, `:217` — formatting debris, no content impact.

## 4. Conditions (named; fixes belong to the lane, not this verifier)

1. **Inventory condition (coverage):** add the seven unnamed executables to SKILL.md — at minimum `exercise-handoff-e2e.py`, `assemble-d2-typed.py`, and the two D4 adapter gates — or record an explicit scoping note that SKILL.md indexes craft rules, not the full executable inventory. Control: `comm -13 <(grep -o 'tools/[A-Za-z0-9./_-]*\.py' SKILL.md | sort -u) <(ls tools/*.py tools/gates/*.py tools/harness/*.py | sort -u)` yields exactly the seven listed in §1, with the two frozen-pinned gates called out.
2. **Citation-drift condition:** re-pin `loanword-material-dating.md:57→:59`, `:60→:36-39/:63`, `era-language-staging.md:124→:127` (or add dated errata). Control: `sed -n '<cited line>p' <file>` reproduces the claimed content.
3. **Stale present-tense condition:** mark the passenger-rows measured instance past-tense / "(pre-repin)" — it is already disclosed via T4 and the round-25 commitment, so this is wording, not silence.
4. **Formatting:** remove the stray fences at `SKILL.md:129,154,217`.

None of these conditions breaks box 1's substance claim: the tables cover the typed pipeline, handoff semantics, gates, and corpus rules with real, verifiable, non-generic content.
