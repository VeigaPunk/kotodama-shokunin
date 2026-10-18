# R19-A16 — filler audit 2/2: the round-19 synthesis-partition entries + wave-level filler verdict (NON-CANON)

- seat: R19-A16 (filler auditor, synthesis partition + wave roll-up). Lane:
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  Assignment (verbatim): *"AUDIT R19-A15..A18 (filler+interop auditors x4): read all new
  entries (filler rejection candidates) … reports/round-19/audit-{1..4}.md"*.
- date: 2026-10-18 (lane-local UTC-03:00; stamps UTC). Readings taken **11:36–11:39Z** on a
  **live, unsettled** wave; §7 records the settle re-check. HEAD `169c616`; baseline
  `e5718945a1ab0a0c3db955338d2cae77d68fd348`.
- role limits: this seat audits and reports; only writes are `audit-1.md`, this file and
  `.scratch/audit/`. No corpus edit, no claim admitted, no candidate disposed.
- criteria: identical to `audit-1.md` §0 (gap-named / decision-record / sources-resolve, plus
  the `corpus/QUALITY.md` bar as a reported observation).
- instruments: `.scratch/audit/r19-audit.py`; verbatim re-runs of each entry's quoted absence
  sweep; `sha256sum`. Companion: `audit-1.md` (verification partition).

## 1. Snapshot — the five new synthesis entries

Baseline synthesis partition: 24 files. Live at this reading: **29** (24 + 5).

| # | entry (under `corpus/knowledge/synthesis/`) | sha256 (first 12) | bytes | mtime (local) |
|---|---|---|---|---|
| S1 | `typed-label-routing-workflow.md` | `f1798edae0c8` | 12535 | 08:36:06 |
| S2 | `generated-artifact-lifecycle.md` | `d8edb53272c7` | 10684 | 08:36:29 |
| S3 | `hold-set-contract-in-brief.md` | `5fbb2e62f0d4` | 10313 | 08:36:51 |
| S4 | `era-material-scoped-reconciliation.md` | `5c508fed145f` | 11223 | 08:37:18 |
| S5 | `finding-disposition-workflow.md` | `fece029493f4` | 11194 | 08:37:47 |

Each maps to a declared gap in `reports/round-19/gaps.md`
(`typed-label-routing-workflow`, `generated-artifact-lifecycle`, `hold-set-contract-in-brief`,
`era-material-scoped-reconciliation`, `finding-disposition-workflow`), with an author fragment
per entry under `reports/round-19/entries/R19-C16..C20.md`. Synthesis minimum for claim C is
>=3; 5 landed.

## 2. Verdicts

**All five clear criteria 1–3. No filler rejection candidate. Two carry a non-reproducing
absence-sweep line (S5, and the wave roll-up in §4), and three carry the QUALITY-bar
calibration gap (§5).**

| # | entry | gap named | decision record | sources resolve | verdict |
|---|---|---|---|---|---|
| S1 | typed-label-routing-workflow | yes (`- gap filled:`) | yes (`## 6. Decision record`) | yes | pass |
| S2 | generated-artifact-lifecycle | yes (`- gap filled:`) | yes (`## 6. Decision record`) | yes | pass |
| S3 | hold-set-contract-in-brief | yes (`- gap filled:`) | yes (`## 6. Decision record`) | yes | pass |
| S4 | era-material-scoped-reconciliation | yes (`- gap filled:`) | yes (`## 6. Decision record`) | yes | pass |
| S5 | finding-disposition-workflow | yes (`- gap filled:`) | yes (`## 6. Decision record`) | yes | pass-with-defect (§4) |

Census: all five carry `topic`/`sources`/`couples`/`verified-at`/`recheck`; all five name their
gap in the recognized `- gap filled:` field form; all five carry a real `## 6. Decision record`
section; every cited repo path resolves (0 missing paths across the five). `follows:` absent
in all five — not required (see `audit-1.md` §2).

## 3. Synthesis absence-sweep replication

Each entry quotes a sweep for its gap's absence. Verbatim re-run from the lane root, 11:38Z:

| sweep (as quoted) | claimed | live total | pre-existing hits | reproduces? |
|---|---|---|---|---|
| S1 `grep -rln "translated-label\|route.*channel\|typed label" corpus/knowledge/synthesis/` | 0 | 1 | **none** | **yes** |
| S2 `grep -rln "generated artifact\|never hand-edit\|rebuild" corpus/knowledge/synthesis/` | 0 | 2 | `loanword-material-dating.md` | **NO** |
| S3 `grep -rln "hold_set_declaration\|hold set\|expected finding" corpus/knowledge/synthesis/` | 0 | 4 | **none** | **yes** |
| S4 `grep -rln "reconcile_scoped\|mapped-confirmed\|mapped-unconfirmed" corpus/knowledge/synthesis/` | 0 | 2 | **none** | **yes** |
| S5 `grep -rln "disposition\|finding severity\|design debt" corpus/knowledge/synthesis/` | 0 | 5 | `worldbible-integration-contract.md`, `naming-canon-workflow.md` | **NO** |

- **S2 — does not reproduce.** `loanword-material-dating.md:139` uses "mosque rebuilding" (a
  material-culture sense). At authoring time the sweep returned **1 file**, not 0. The hit is
  an unrelated sense — the entry's gap (a generated-artifact lifecycle: never hand-edit,
  rebuild + check) is genuine.
- **S5 — does not reproduce.** Two pre-existing synthesis entries use "disposition" in the
  *lore/canon* sense: `worldbible-integration-contract.md` lines 99, 131, 136 ("lore issues
  disposition"; "per-record disposition/reason") and `naming-canon-workflow.md` lines 91, 112,
  145 ("findings/dispositions"; a `disposition` column). At authoring time the sweep returned
  **2 files**, not 0. The entry's own parenthetical ("the term lives in the verification and
  provenance entries, not as a design workflow") shows the author knew the term was in use —
  but it names the wrong partitions and still prints "→ 0 files". The gap is genuine; the
  evidence line is inaccurate.

## 4. Wave roll-up — filler verdict over all ten entries

| criterion | verification (5) | synthesis (5) | wave |
|---|---|---|---|
| names the gap it fills | 5/5 | 5/5 | **10/10** |
| carries a decision-record section | 5/5 | 5/5 | **10/10** |
| cited repo paths resolve | 4/5 (V1 broken) | 5/5 | **9/10** |
| quoted absence sweep reproduces | 3/5 (V4, V5 fail) | 3/5 (S2, S5 fail) | **6/10** |
| carries `calibrat` vocabulary (QUALITY.md §2) | 2/5 | 1/5 | **3/10** |

- **No entry is a filler rejection candidate.** Every one names a specific, checkable gap and
  backs it with D4-round artifacts and existing corpus — the failure mode the assignment asks
  me to reject (an entry naming no gap) does not occur. `reports/round-19/claims.json` claim C's
  "zero filler" reading therefore **holds on merits**.
- **Systematic sourcing-rigor defect, not filler.** 4 of 10 quoted absence sweeps print
  "→ 0 files" where a verbatim re-run returns >=1 file (S1 of `audit-1.md`, V4, V5, S2, S5 —
  five lines across four entries: `gate-battery-surface-verification`, `two-reader-interop-
  agreement`, `generated-artifact-lifecycle`, `finding-disposition-workflow`). Every hit is an
  unrelated sense, so each gap is genuine; the defect is that the evidence line does not
  reproduce, and none of the four documents the pre-existing hit (the round-10 precedent —
  `audit-filler.md` §3.2; `verification-independence-anti-circularity.md`'s own
  "3 hits, all unrelated senses" treatment — was to name the hits and their senses).
  Routed as a wave-level correction: either the four entries add the hit-and-sense clause, or
  the round records the sweep-vs-merits divergence. It is **not** a claim-C failure: the
  counting command's `gap_named` test (`ENTRY_GAP_RE = \bgap\b` + a `.md` ref,
  `reports/round-19/run-validation.py:452`) does not read the sweeps.

## 5. QUALITY-bar observation — missing calibration vocabulary (7 of 10)

Command (11:38Z): `python3 tools/gates/provenance-audit.py corpus/knowledge` → **exit 1**,
`files=199 marks=733 mark-lines=719 findings=7 blocked=0`. All seven findings are
`missing-calibration` (the literal-`calibrat` test, `tools/gates/provenance-audit.py:84`),
against `corpus/QUALITY.md` criterion 2:

```
synthesis/finding-disposition-workflow.md            synthesis/gate-battery-surface-verification.md (*)
synthesis/generated-artifact-lifecycle.md            verification/generated-artifact-roundtrip-verification.md (*)
synthesis/hold-set-contract-in-brief.md              verification/pre-declared-hold-set-reconciliation.md (*)
synthesis/typed-label-routing-workflow.md
```
(*) also listed in `audit-1.md` §5. Carrying `calibrat`: V1 (2), V5 (3), S4 (2) — 3 of 10.

## 6. corpus/README.md reconciliation (claim C3 — status at this reading)

`reports/round-19/run-validation.py:835-873` requires README to change, bump its `revision:`,
index all ten new filenames, and match the live partition counts. At 11:38Z:

- `sha256sum corpus/README.md` → `9df4b7c579b89d6f…` = **byte-identical to the baseline**
  (`git show e571894:corpus/README.md`); `grep -c "round-19" corpus/README.md` → **0**.
- So C3 is **not yet satisfied**: README was not reconciled at this reading. Section headers
  still read `verification/ (15)` and `synthesis/ (24)` against live 20 and 29.
- This is an **integration-pending** item, not an entry defect: the wave is live and the parent
  integrates README after the authors settle. Re-measured in §7.

## 7. Settle re-check (2026-10-18T11:45:59Z; worktree hash `071b5acf90a2` stable ×3)

The synthesis entries were **revised during the window**; the settled hashes differ from §1.

| # | entry | settled sha256 (first 12) | bytes | gap | decision | missing paths |
|---|---|---|---|---|---|---|
| S1 | typed-label-routing-workflow | `5e37da4aaaf8` | 12811 | yes | yes | none |
| S2 | generated-artifact-lifecycle | `a3393d06a3c2` | 10969 | yes | yes | none |
| S3 | hold-set-contract-in-brief | `e1c6780a9201` | 10596 | yes | yes | none |
| S4 | era-material-scoped-reconciliation | `6c92cf3b13a5` | 11468 | yes | yes | none |
| S5 | finding-disposition-workflow | `9d23492f6396` | 11441 | yes | yes | none |

- **§5 (missing calibration) — RESOLVED, wave-wide.** Settled:
  `python3 tools/gates/provenance-audit.py corpus/knowledge` → **exit 0**,
  `files=199 marks=733 mark-lines=719 findings=0 blocked=0`. All ten entries now carry
  `calibrat` vocabulary. The 7-of-10 QUALITY-bar finding is cleared.
- **§6 (README reconciliation) — RESOLVED.** Settled `corpus/README.md`: `revision: 1.4`
  ("Round-19 index refresh"), section headers `## synthesis/ (29)` and `## verification/ (20)`,
  `Total knowledge entries: 199.`, and 5 occurrences of "round-19". Live partition counts match
  (20 verification / 29 synthesis). Claim C3 is satisfied at settle.
- **§3/§4 (absence sweeps) — NOT resolved.** The quoted sweep lines are unchanged at settle;
  the four non-reproducing sweeps stand:

| sweep | claimed | settled total | pre-existing hits (excluding the round-19 entries) | reproduces? |
|---|---|---|---|---|
| V4 `check-gate-battery\|gate battery\|battery_exit` (knowledge) | 0 | 2 | `verification/verification-independence-anti-circularity.md` | NO |
| V5 `interop\|two readers\|reader agreement` (knowledge) | 0 | 2 | `myth-symbol/divination-omen-systems.md:201` | NO |
| S2 `generated artifact\|never hand-edit\|rebuild` (synthesis) | 0 | 2 | `synthesis/loanword-material-dating.md:139` | NO |
| S5 `disposition\|finding severity\|design debt` (synthesis) | 0 | 5 | `synthesis/worldbible-integration-contract.md` (99,131,136), `synthesis/naming-canon-workflow.md` (91,112,145) | NO |

**Settled wave roll-up (10 entries):** gap named 10/10; decision record 10/10; cited paths
resolve 10/10; quoted absence sweep reproduces **6/10**; calibration vocabulary 10/10.

**Final filler verdict: 10/10 entries pass the three assignment criteria. Zero filler
rejection candidates.** The one routed finding is the sourcing-rigor defect on four quoted
absence sweeps (§3, §4 above) — a correction to the evidence line, not a rejection: every gap
is genuine and every hit is an unrelated sense. The parent may accept the round with that
finding recorded, or route the four one-line corrections.

## 8. Limits

- Structural, resolvability and sweep-reproduction checks only. Verdicts bind the §1 hashes and
  the 11:36–11:39Z window on a live wave; entries revised after this reading are re-bound in
  §7. Passage-level source support is the C-reviewer seats' work, not absorbed here.
- Author-side, NON-CANON. No entry is admitted; the README observation is a status reading, not
  a disposition.
