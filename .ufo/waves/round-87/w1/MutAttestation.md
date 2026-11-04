# MutAttestation — round87 v1

Axis: **operability**. Author-side mutation evidence only; no admission, integration, or semantic-truth judgment.

## Result

Three independent single-branch removals were **killed by both assigned detectors**. Each mutation started from pristine bytes, disabled exactly one guard with `False`, and restored exact bytes before repeating the same detectors. No production or sibling source was edited.

For each of all three probes:

- Pristine: clean-first tool selftest **37/37, exit 0**; frozen battery **12/12, exit 0**.
- Mutated: tool selftest **36/37, exit 1**; frozen battery **11/12, exit 1**.
- Restored: tool selftest **37/37, exit 0**; frozen battery **12/12, exit 0**.

| Removed branch | Selftest failed case | Frozen failed case | Missing expected ID | Verdict |
|---|---|---|---|---|
| Translation chronology | translation-backdated | translation-backdated | TRANSLATION_CLOCK | killed |
| Unresolved solution selecting answer | unresolved-selected | unresolved-selected | SOLUTION_CONFLICT | killed |
| Duplicate record ID | duplicate-id | duplicate-record | RECORD_ID | killed |

Actual failed inner CLI results: all returned **exit 0**, empty stderr, and `findings: []`, rather than expected exit 1 and the indicated finding. Selftest record counts were respectively 1, 1, and 2; frozen battery record counts were 6 in all three. Each detector's first positive case remained green. No survivors or inconclusive probes occurred.

## Hashes and restoration

SHA-256 pristine candidate and every restored copy:

`4abcbbd058c33b95cc7c8acc4840493ccaeda0bdf01cb3947d074c3352c497aa`

| Mutant | SHA-256 |
|---|---|
| translation-clock | bfdceb75127db17cbd6787bd7c18337833f14dc09122291442e5905b3a831d31 |
| solution-selected | 23fc4ce0fa6fd75de869c6457f2ea1723008e0eff2260d381fb71cf1710b3ec7 |
| duplicate-id | 03cdcf108f2ee0f898f514113611493deda12a3530f7075fd7b182d2a100f682 |

Frozen inputs were extracted with read-only Git from `2a3b5643899c3520867ae930593cafef6ef19cad`, not edited:

- measure87.py: `131b29e84d39c2cbd22993aaadd469b5a96602651927730c980503cc74738e62`
- claims.json: `bfc2de174261ad410a63abb3949385d8be76fe29ef8aaa528ec8d0f9feb43264`
- Baseline packet hash is recorded in every frozen-battery output in the receipt.

The candidate source matched its initial bytes after the probes. The active scratch candidate was restored and copied into this seat's stage; scratch was removed. Receipt records `exact_restoration`, `source_unchanged`, and `scratch_removed` all true.

## Reproduction and evidence

All files below are relative to `.ufo/waves/round-87/w1/stage/MutAttestation/`:

- `run-mutations.py`: bounded harness; two identical detector commands for pristine, mutated, and restored bytes per probe, with restoration in `finally`.
- `mutations.json`: exact original/replacement guards and expected detectors.
- `mutation-receipt.json`: actual commands, exits, complete stdout/stderr, per-state digests, verdicts, and cleanup evidence.
- `pristine-candidate.py`, `restored-candidate.py`, and three `*-mutant.py` files: retained exact source evidence.
- `frozen-measure87.py`, `frozen-claims.json`: immutable-revision input snapshots.

Invocation used Python `-B run-mutations.py --candidate <ExecAuditor stage>/check-attestation-packet.py --mutations <own stage>/mutations.json`. Each detector used the same scratch candidate path; selftest received an existing isolated `--work` directory; battery additionally received explicit lane `--root`, pinned `--revision`, and scratch `--candidate`. Eighteen assigned detector runs completed (three states × two detectors × three mutants). Harness exit 0; stderr empty.

## Scope and limits

This demonstrates discrimination for three removed integrity guards on a finite CLI battery, not truth, arbitrary-defect coverage, cultural authenticity, or lore canon. Existing r86 stage completeness checking is not newly acquired here. Frozen source IDs, claims, counter, and history were untouched. L1 remains canonical for production planning/integration; the disclosed unresolved L2 planner-policy conflict is not resolved by these probes. No commits, index writes, installs, background jobs, or delegated workers were used. Initial discovery included a read-only HEAD lookup; executable battery calls and frozen extraction were pinned to the named immutable revision.

Runtime: existing Python 3.14.8, GCC 16.2.1 build; no tool installation/update.

## Self-evaluation

Accuracy 4/5: raw command outputs and hashes support all results; the harness does not infer semantic correctness. Completeness 5/5: all three requested mutants have pristine/mutated/restored runs and cleanup evidence. Clarity 4/5: compact result table; full outputs intentionally reside in the receipt. Actionability 4/5: exact sources and replay harness retained, but replay requires an available candidate path. Conciseness 4/5: hashes make the report longer but auditable. Overall 4.2/5. Improvements: preserve finite-scope wording when integrating; use receipt case outputs rather than extrapolating coverage. Self-check: the requested mutation matrix and restoration requirements are met.
