# R19-C24 — reviewer of entry `gate-battery-surface-verification.md`

- round: 19 (loop 2 of 3, build round 3 of 4; `hyper/deepseek-v4.1-flash`),
  lane `kotodama-shokunin`, claim **C**.
- assignment (verbatim): "C R19-C21..C28 (entry reviewers x8): one per entry
  (poll, max 20 min): frontmatter, source resolvability, no filler, no
  duplication; verdicts reports/round-19/entries/review-<id>.md."
- date: 2026-10-18, stamps UTC. Window 11:31–11:42Z. Baseline
  `e5718945a1ab0a0c3db955338d2cae77d68fd348`, HEAD `169c616`.
- canon: **NON-CANON** engineering review; author-side evidence only.
- writes: **this file only** plus `.scratch/r19c/`. No commit, no push.

## 0. Artifact under review and verdict

`corpus/knowledge/verification/gate-battery-surface-verification.md` — new
verification entry, gap `gate-battery-surface-verification`
(`reports/round-19/gaps.md`, seat R19-C14). Anchor: sha256
`48e0ae7590d98761a77115b48626c43025ecb978c7c973d15d015e25b5e8fe26`, 12,265
bytes, 83 lines, mtime 2026-10-18 11:40:11Z (stable at 11:41:52Z).

**Verdict: 2 of 4 mandated checks pass clean; the entry's load-bearing
measurement no longer reproduces, and its quoted absence sweep is false as
written.** Both defects are low-to-medium and are *drift*, not fabrication: the
battery was edited by the round's own O work after this entry was measured.

| mandated check | verdict |
|---|---|
| frontmatter completeness | **pass** |
| source resolvability | **defect — the §2/`verified-at` measurement does not reproduce; the §4 coverage claim is contradicted by the live tool** (§2) |
| no filler | **pass** with one false quoted sweep (§3) |
| no duplication | **pass** |

## 1. Frontmatter completeness — PASS

Head block = L1–18 (first `## ` at L20). `- topic:` L3, `- sources:` L5 (8
sub-bullets), `- couples:` L15, `- source:` L16, `- verified-at:` L17,
`- recheck:` L18; `- gap filled:` L4. Decision record `## 6.` (L75), rows 1–6.
Instrument → `missing_frontmatter=[] gap=True decision_record=True`.

## 2. Source resolvability — DEFECT (measurement superseded mid-round)

The entry's KTD-GB-S-0002 and `verified-at` state, measured 2026-10-18:
`python3 tools/check-gate-battery.py` → **exit 0**, `pass 7`, `unevaluable 0`,
`originals {files_hashed_before: 28, files_hashed_after: 28}`, and §4 asserts the
battery does **not** cover the D4 gates.

This seat's re-run at **11:38Z** on the same tree:

```
battery_exit: 2   pass: 8   fail: 0   unevaluable: 1
originals: {files_hashed_before: 32, files_hashed_after: 32, preserved: true}
summary: {coverage: "9/9", gates_covered: [7 legacy, d4-typed-labels-check-gate.py, d4-assembly-check-gate.py]}
findings: [{gate: d4-assembly-check-gate.py, id: GATE-UNEVALUABLE-EXIT, detail: "selftest exited 2"}]
```

**Cause (measured, not inferred).** `tools/check-gate-battery.py` is modified
against the baseline — `git diff --stat tools/check-gate-battery.py` → **252
insertions, 37 deletions**, mtime 2026-10-18 **11:40:08Z** (baseline copy
`git show e571894:…` = 50,929 B vs live 62,254 B) — and the D4 family has gained
committed baselines: `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json`
and `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/expected.json` now
exist and are read by the battery. This is the round's own claim **O** landing
("battery default run covers the D4 gates (7 structural + 2 D4 = 9/9)").

Consequence: three of the entry's statements are stale against the live tree —
the `pass 7` count, the `exit 0` reading, and §4's "a battery green does **not**
cover `d4-typed-labels-check-gate.py` or `d4-assembly-check-gate.py`". The
entry's own `recheck` trigger ("whenever the D4 family is added to the battery's
surface") fires exactly now.

**What still resolves:** KTD-GB-S-0004's cited sentence is genuine —
`tools/gates/frozen/round-18/README.md` L49–51 reads "It is deliberately **not**
named `expected.json`: `tools/check-gate-battery.py` discovers every
`expected.json` under its baseline roots and fails closed on a gate outside its
seven-name constant". The citation is accurate *as a round-18 record*; the round's
own O change supersedes it. KTD-GB-S-0003's root list (`tools/gates/expected/`,
`tools/gates/frozen/`, `reports/round-9/baselines/`) matches the live run's
`roots` block (4 / 10 / 3 files). URL `https://doi.org/10.1109/TSE.2010.62` →
HTTP 202.

## 3. No filler — PASS, with one false quoted sweep

- The gap is real as an *entry-shaped* gap: before this round no committed entry
  stated what the battery covers. **But the quoted absence sweep does not
  reproduce.** The entry says
  `grep -rln "check-gate-battery\|gate battery\|battery_exit" corpus/knowledge/`
  → **0 files**. Re-run 11:40Z it returns
  `corpus/knowledge/verification/verification-independence-anti-circularity.md`
  (pre-existing, round-18, mtime 2026-10-17), which names
  `tools/check-gate-battery.py` at L15 (`couples`), L18 (`recheck`) and L89
  (a table row). The claim "0 files" is therefore false as written; the gap
  survives as a *scope* gap (no entry owns the battery's surface), not as a
  first-mention gap.
- **Delivers**: a 3-row duty table (§2), a 3-row exit-code table (§3), the
  coverage-boundary section (§4), a reviewer checklist (§5), a 6-row decision
  record (§6).

## 4. No duplication — PASS

Slug unique against the 189-file baseline. Max token-Jaccard vs the pre-existing
corpus **J=0.262** (`verification-independence-anti-circularity.md`); vs
round-19 siblings J=0.358 (`finding-disposition-workflow.md`). No
near-duplicate.

## 5. Findings

| # | finding | severity | status |
|---|---|---|---|
| R19C24-F1 | The entry's measured reading (`pass 7`, exit 0, 28 files) and its §4 coverage boundary are superseded by the round's O change to `tools/check-gate-battery.py` (252 insertions, mtime 11:40:08Z) and by two new `tools/gates/expected/d4-*-check-gate/r19-pre/expected.json` baselines. The live battery reads `pass 8 / unevaluable 1 / exit 2 / coverage 9/9`. | medium | **open — reported to parent**; the entry needs a correction (a NEW entry, never a rewrite) once O settles |
| R19C24-F2 | The quoted absence sweep `grep -rln "check-gate-battery\|gate battery\|battery_exit" corpus/knowledge/` → 0 files is false: `verification-independence-anti-circularity.md` (pre-existing) carries the term at L15/L18/L89. The gap remains real as a scope gap. | low | **open — reported to parent** |
| R19C24-F3 | Churn: the entry was re-touched at 11:40:11Z; no content change found in the sections checked. | informational | — |

## 6. Limits

- This seat re-ran the battery once (11:38Z) and did not re-derive its baseline
  checks; it reports the tool's own output as the entry does.
- The O work is still in flight (12 O-battery workers); the live reading may
  move again before the round closes. F1's numbers are point-in-time
  (11:38Z) and should be re-measured before being quoted.
- Verdicts bind to sha256 `48e0ae75…`; a later edit invalidates them.
- NON-CANON throughout.

FILES: reports/round-19/entries/review-C14.md
