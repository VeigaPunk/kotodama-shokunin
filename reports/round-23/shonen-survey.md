# X11 — SHONEN-box evidence survey (round 23)

Date: 2026-10-18. Role: SCRIBE X11 (round 23, operator loop 2, GLM round 1 of 2).
Purpose: prepare round 24's promotion review by collecting the four `SHONEN.md`
boxes' **current evidence pointers**. This survey records where evidence lives;
it judges nothing, awards no mark, and changes no filed artifact of rounds 8–22.
The canonical `SHONEN.md` remains the sole authority for marks; everything below
is author-side (`[~]`-class) context for the reviewer.

## 0. Canonical state of SHONEN.md (commands, 2026-10-18)

- `git log --oneline --all -- SHONEN.md` → one commit only: `a527120 mint:
  kotodama-shokunin seed kit (operator directive 2026-10-17)`. Unchanged since
  mint.
- `grep -c "^- \[ \]" SHONEN.md` → `4` (all four boxes unmarked `[ ]`).
- `grep -rn "^- \[x\]" LOG.md SCORECARD.md SHONEN.md SKILL.md reports/round-2*/`
  → no matches (no non-author `[x]` exists anywhere in the lane).
- `wc -l SHONEN.md` → 11 lines. Mark legend (`SHONEN.md:5-11`): `[~]` asserted
  by the lane itself with an evidence pointer; `[x]` only with a named
  non-author verifier per Promotion gates.

The four boxes (verbatim, `SHONEN.md:6-9`):

1. SKILL.md contains real decision tables, error patterns, checklists, cited sources
2. At least one end-to-end domain task executed and logged in LOG.md
3. Instructions executable by an agent without oral context
4. No cross-domain bleed (PROVINCE.md still accurate)

## 1. Where the assertions live

- **Full pointer set (supplement era, baseline `fe34faa`, 2026-10-17):**
  `reports/supplement-opencode-1/31-promotion-readiness.md` §"SHONEN — four
  author-side assertions" carries the original four `[~]` paragraphs with
  per-box pointers and the then-open non-author requirements (its §"Unresolved
  non-author verification requirements", items 1–7). It measured an immutable
  baseline; SKILL.md line numbers it cites have since shifted (current anchors
  in §2 below).
- **Last per-box `[~]` skeleton:** `reports/round-9/report-draft.md:192-209`
  (`## SHONEN skeleton`, four `[~]` lines, "every box stays `[~]` for lack of a
  named non-author verifier"). Confirmed descriptive by
  `reports/round-12/defects/sweep-r9.md:45`.
- Rounds 10–22 report drafts carry no new SHONEN section; round-15's draft
  restates only the no-`[x]`-without-non-author rule
  (`reports/round-15/report-draft.md:235-237`). LOG.md has no SHONEN-box entry
  after round 9 beyond box-2 references (`LOG.md:1978`).

## 2. Box-by-box current pointers

### Box 1 — SKILL.md real decision tables, error patterns, checklists, cited sources

Current SKILL.md anchors (`wc -l SKILL.md` → 488; grep `^## `, 2026-10-18):

| surface | current anchor |
|---|---|
| Decision table | `SKILL.md:20` (`## Decision table`) |
| Error patterns | `SKILL.md:244` (`## Error patterns`) |
| Hard boundaries | `SKILL.md:285` (`## Boundaries (hard)`) |
| Executable checklist | `SKILL.md:298` (`## Checklist (executable where a tool exists)`) |
| Corpus map (cited sources) | `SKILL.md:312` (`## Corpus map`) |
| Using the evidence | `SKILL.md:334` |
| Gates and probes (registry) | `SKILL.md:351` |
| Source-to-system constraints r5/r6 | `SKILL.md:411`, `SKILL.md:421` |
| Source-bounded culture drill D3 | `SKILL.md:436` |

- Cited corpus surfaces resolve under `corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}/` (179 knowledge entries; count command of record: `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`, round-5/6 SCORECARD rows).
- Gate registry pinned fixtures: `tools/gates/fixtures/` (7 gates, `git ls-files 'tools/gates/*.py' | wc -l` = 7 at the supplement baseline).
- Supplement-era pointers (`31-promotion-readiness.md`, Box 1 paragraph) and
  residual ("are the tables *real* enough" = non-author judgment) still stand
  as the reviewer's starting list.

### Box 2 — at least one end-to-end domain task executed and logged

Pointer chain, oldest to newest:

- **D2 (round 3):** `LOG.md:1967` entry "round 3: D2 end-to-end build + direct
  triage (ADMITTED)"; box-2 evidence sentence at `LOG.md:1978` ("Task executed
  and logged end-to-end (SHONEN box 2 evidence)"); lesson
  `corpus/lessons/round-3-d2-build.md`; artifacts `examples/culture-d2/`
  (`ASSEMBLY.md`, `packet.d2.yml`), frozen manifest
  `tools/gates/frozen/round-3/MANIFEST.tsv` (7 rows).
- **D3 (rounds 7–9):** declaration `LOG.md:2706` ("round 7 declaration:
  source-bounded culture assembly"; round 7 closed REJECTED, ledger closure
  `LOG.md:2899`); D3 acceptance completed as round-9 work (`LOG.md:2954` ff.,
  capability `culture-d3-acceptance`: `--check` byte-identical,
  evidence-coupling selftest green, frozen replay exit 0); artifacts
  `examples/culture-d3/` and `reports/round-9/d3/`.
- **D4 + handoff e2e v3 (rounds 20–21):** round 20 admitted — "handoff e2e v3 —
  D4 claims (27 total; census 16/7/4); 102/102 links; frozen baseline"
  (`LOG.md:3273-3284`, evidence `reports/round-20/validation.json` acceptance
  true); artifacts `examples/culture-d4/`, `tools/exercise-handoff-e2e.py`,
  `reports/round-20/handoff/`; round-21 adjacency verification
  `reports/round-21/validation.json` acceptance true (`LOG.md:3286-3296`).
- Residuals recorded, not resolved here: round-3 TSV-vs-`expected.json` form
  gap and unmanifested round-4 outputs (`31-promotion-readiness.md` Box 2
  residual; `LOG.md:1961-1962` context) — non-author acceptance items.

### Box 3 — instructions executable by an agent without oral context

- Executability surfaces: SKILL.md sections above; lane-root acceptance runner
  `python3 reports/round-22/run-validation.py` (round-22 counting command) and
  its receipt `reports/round-22/rerun.json`; prior receipts
  `reports/round-21/validation.json` and per-round `run-validation.py` scripts.
- Round-9 `[~]` basis: "gate baselines + battery extension + `run-validation.py`
  run from the lane root" (`reports/round-9/report-draft.md:200-202`).
- **Open (unchanged since the supplement):** no non-author agent cold-run of
  SKILL.md exists; the only valid test is a cold execution with recorded
  transcript pointer (`31-promotion-readiness.md` requirement 4). Wave workers
  and dispatched subagents count as the lane, not as verifiers.

### Box 4 — no cross-domain bleed; PROVINCE.md still accurate

- `PROVINCE.md` current state (31 lines, 2026-10-18): "Owns" now names all six
  knowledge partitions including `verification` and `civilizations` — the
  supplement-era "Owns lists only 4 dirs" accuracy gap observation
  (`31-promotion-readiness.md` Box 4) is factually superseded in the live file;
  whether PROVINCE is "still accurate" remains a non-author ruling.
- Round-21 adjacency audit (admitted, `LOG.md:3286-3296`):
  `reports/round-21/adjacency/{entries.md,province.md,ledger.json,A11-A12-handoff.md}`
  — verdict recorded there: PROVINCE accurate, refusals unviolated, one filed
  D2→D4 fixture bleed routed to r22.
- Round-22 bleed tail (round closed REJECTED on D, `LOG.md:3298-3310`): census
  and design in `reports/round-22/bleed/{analysis.md,design.md,impl.md,skill-rule-draft.md,verification.json}`
  — the family-clean projection rule was designed but never implemented; routed
  to round 25 with the full recipe. Round-23 claim D drafts the rule for
  SKILL.md (`reports/round-23/claims.json`), landing by the orchestrator.
- Historical sweep basis: bounded bleed regex over `corpus/knowledge/` → 0
  matches at the supplement baseline (`31-promotion-readiness.md` Box 4);
  reviewer may re-run a full sweep (then-bounded and pattern-only).

## 3. Standing non-author requirements (input to the round-24 review)

From `31-promotion-readiness.md` §"Unresolved non-author verification
requirements", all still open as of this survey: named non-author verifier per
box (1); Box 1 realness judgment (2); Box 2 TSV-form acceptance + ancestry
re-verification at closure (3); Box 3 cold execution (4); Box 4 PROVINCE
accuracy ruling + full sweep (5); promotion mechanics on pass (6); evidence
freshness re-measurement at the review baseline (7). No box may be marked
`[x]` from lane-authored work, including this survey.

## 4. Survey method

Read-only: `git log --oneline --all -- SHONEN.md`; `grep` counts above; `wc -l`
(SKILL.md 488, LOG.md 3310, SCORECARD.md 456, SHONEN.md 11, PROVINCE.md 31);
section-anchor greps of SKILL.md/LOG.md; reading of the cited files. All
commands run 2026-10-18 in the live worktree at HEAD `7b181a5` (round-23
declaration). No file outside `reports/round-23/shonen-survey.md` was written;
no round validator was run; no promotion claim is made.
