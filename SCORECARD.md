# kotodama-shokunin — SCORECARD

Axes: depth, coverage, operability, freshness, calibration, adjacency
(fleet `AXES.md`). The supplemental OpenCode Go wave is additional work,
not one of the three reserved non-flash Z.ai rounds. Four numbered rounds
are recorded so far; their historical admission decisions are not rewritten.

The old 0–10 estimates had no reproducible mapping from evidence to score.
They remain historical in Git, not new numeric claims. This table records
per-axis verdicts and independently checkable observations instead; defining
a calibrated numeric rubric remains an explicit protocol-conformance gap.
A raw file or marker count is not a quality score.

## Axes — supplement-opencode-1

Measured baseline: `fe34faaafbe0add59ff68827a0df6c5782a72404`. Delivered-tree
commands and results are persisted in
`reports/supplement-opencode-1/validation.json`; the filed lane report names
the carrying work commit. Source verdicts are worker observations except
for the five parent re-fetches recorded in `parent-source-spotchecks.json`.

| axis | verdict | observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | improved (unclaimed observation) | D2 PAN-03 now derives as `huma + weha`; one genuine coda violation removed; nine-derivation non-canon contrast exercise runs | `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json --counts` | `reports/supplement-opencode-1/04-name-correction.md`, `validation.json` |
| coverage | unchanged | 179 knowledge entries, six partitions, 94 civilization-partition entries including two primary-source maps; index omission corrected, not a new civilization | `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | inventory reports 179 files; `corpus/README.md` |
| operability | improved | Assembler selftest and deterministic check pass; all seven round-3 frozen verdicts replay; seven original gate selftests pass in isolation | `python3 tools/assemble-d2.py --selftest`; `python3 tools/assemble-d2.py --check`; `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` | `reports/supplement-opencode-1/validation.json`; immutable round-3 manifest |
| freshness | improved | 148 assigned claim rechecks across 13 entries: 118 supported, 10 contradicted, 20 unresolved; five parent passage checks; old corpus bytes preserved under dated errata | `python3 -c 'import json,pathlib,collections; ns="ottoman slavs sogdian tibet turkic africa mesoamerica color kinship orality phonetics registers lexicon".split(); c=collections.Counter(a["verdict"] for n in ns for a in json.loads((pathlib.Path("corpus/lessons/supplement-opencode-1/sources")/(n+".json")).read_text())["audits"]); print(dict(c),sum(c.values()))'` | assigned JSON ledgers; `reports/supplement-opencode-1/parent-source-spotchecks.json` |
| calibration | improved | Historical round-4 findings 21, not 24; audit reports 16, not 17; line/occurrence units and unresolved scholarship separated | `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`; `python3 -c 'from pathlib import Path; print(sum(l.startswith("FINDING ") for p in Path("tools/gates/frozen/round-4").glob("*.out") for l in p.read_text().splitlines()),len(list(Path("corpus/lessons/round-4-audit").glob("*.md"))))'` | baseline 590 marker-bearing lines; delivered counts in validation; appended LOG correction |
| adjacency | unchanged | Handoff envelope checker still sees 16 fields and 20 glossary entries, exit 0; no lore receipt or cultural clearance claimed | `python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md` | `reports/supplement-opencode-1/25-handoff-boundary.md`, validation |

## Capabilities

| name | demonstrated behavior | command / evidence | first working |
|---|---|---|---|
| structural domain checks | Phonology, lexicon, myth, costume, naming and provenance verdicts on their supplied inputs; coverage limitations retained | `tools/gates/*.py --selftest`, seven isolated legacy selftests | round 1 (handoff round 2) |
| reproducible culture assembly | Source-hash-pinned D2 packet and positive/negative assembly controls | `python3 tools/assemble-d2.py --selftest`; `--check` | round 3; selftest supplement-opencode-1 |
| frozen verdict replay | Validate snapshot/gate/output digests before re-executing pinned inputs; expected red remains red | `python3 tools/replay-frozen.py --selftest`; actual round-3 replay | supplement-opencode-1 |
| uncertainty inventory | Deterministic lines/occurrences/marker inventory with heuristic labels, never scholarship certification | `python3 tools/source-audit-inventory.py --selftest`; `--json --summary` | supplement-opencode-1 |
| historical source rechecks | Per-claim retrieved passages, access limits, contradictions and unresolved outcomes | 13 assigned JSON ledgers, 148 audits; five parent re-fetches | supplement-opencode-1 |
| contrastive craft exercise | Distinguish sound law, register-limited name avoidance and borrowed garment strata across two eras | `python3 tools/check-craft-exercise.py --selftest`; `examples/supplement-opencode-1/sound-change-vs-taboo.json` | supplement-opencode-1 |
| corpus apparatus audit | Inspect declared metadata and ledger scope without equating it to factual truth | `corpus/lessons/round-4-audit/` (16 reports), supplemental reviews | round 4 |

## Planned

- Latest operator ordering (2026-10-17; appended in LOG.md): pending rounds
  5–7 are the three non-flash `zai-coding-plan/glm-5.3` rounds, 16 workers
  each. The OpenCode Go supplement does not substitute for them.
- Pending rounds 8–9 return to Alibaba token-plan DeepSeek v4.1 Flash,
  32–64 workers per round, with keys rotated by availability.
- Round 10 is the requested Grok 4.7 xhigh fast 128-worker wave, AFTER the
  DeepSeek rounds. This supersedes the older goal draft's round-8 ordering,
  not its exact-model requirement. Use the native route or the host's Grok
  CLI if necessary and available; no silent model or provider substitution.
- D2 needs typed translated-label/native-form handling, scoped era/material
  reconciliation and an executable rank-rule adapter. A green partial
  schema check is not whole-culture verification.
- Fix legacy parser/regex and fixture-rewriting defects documented in
  supplemental reviews 26 and 29; add isolated negative controls.
- Corpus metadata (`source`, `verified-at`, `recheck`), per-gate
  `expected.json` baseline layout, and a reproducible numeric axis rubric
  remain conformance debts. Do not claim promotion or fleet closure.

## Saturation and retired axes

No retirement. Legacy saturation line 8 and stagnation window 3 remain
historical policy; the nudge is not invoked without calibrated scores.
