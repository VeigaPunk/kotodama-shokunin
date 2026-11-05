# ExecMutants95 — scoped findings

Axis: operability; secondary axes: faithful mutation semantics and reproducible evidence.

## Deliverable

`stage/ExecMutants95/mutants95.py`: 95 entries, the 88 round-94 removals carried and seven new refusal-channel removals. Each entry has a semantics field. All original replacement strings are retained except the refreshed fallback indentation. Clean-first gate precedes mutation execution; pattern counts are collected at run start. Missing or wrong-count exactly-once targets are BROKEN-PATTERN, never skipped. Receipt is `<work>/mutation95-score.txt`. No production files changed.

Semantics clarification: the request names 83 lineage entries plus five routed entries (=88), but also explicitly requires head-qualify-off to be exactly-once even though it belongs to the 83. Accordingly 82 carried entries retain replace-all, head-qualify-off and the five routed entries are exactly-once; all seven additions are exactly-once. Refreshed dispo-fallback-off retains replace-all semantics and matches exactly once on both candidate and base. Multi-match lineage targets remain replace-all.

## Measurements and commands

All commands were run from the assigned scratch directory with explicit --work. In these commands, R is `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, S is `/fast/scratch/hyaku/kotodama-r95/ExecMutants95`, D is `$R/.ufo/waves/round-95/w1/stage/ExecMutants95/mutants95.py`, and V6 is `$R/.ufo/waves/round-95/w1/stage/ExecGraderV6/v6-candidate.py`. Fully expanded commands are retained in the respective receipts.

- Base bytes: `git -C "$R" show 19aa4dd03dfd37b435d0b8ea5b313635d9d51592:tools/check-advance-evidence.py`, rc 0, sha256 `7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff`.
- RED: `python3 -B "$D" --tool "$S/v5.py" --work "$S/red"`, rc 1: **MUTATION-SCORE: 87/95 killed, 1 survived, 7 broken-pattern**. head-qualify-off survives. All seven new targets are absent/broken. Refreshed dispo-fallback-off matches once and is killed on v5; the expected additional stale fallback break does NOT occur with the refreshed driver. `fallback-patterns-v5.txt` records `str.count` evidence: historical 12-space target=0, refreshed 8-space target=1. This is an honest discrepancy from the expected red-before description, not a claim of eight broken targets.
- GRADED: `python3 -B "$D" --tool "$V6" --work "$S/graded"`, rc 0: **MUTATION-SCORE: 95/95 killed, 0 survived, 0 broken-pattern**. Clean-first rc 0; `clean-selftest-v6.txt` retains SELFTEST PASS 134/134. Candidate sha256 `f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec`.
- Stub: `$S/stub.py` contains only `print('SELFTEST PASS 134/134')`. `python3 -B "$D" --tool "$S/stub.py" --work "$S/stub"`, rc 1: **MUTATION-SCORE: 0/95 killed, 0 survived, 95 broken-pattern**. It passes clean-first but cannot apply any pair. Stub receipt is also appended after the graded score in mutation-score.txt.
- Missing work: `python3 -B "$D" --tool "$S/v5.py"`, rc 2, argparse names missing --work; retained in missing-work.txt.
- Entry count is the full driver loop count, 95, shown in every score denominator; no --only subset was used.
- Disk guard: `/home/vgpnk/Projects/shokunin/scripts/hyaku/disk-guard.sh status`, rc 0: scratch free 409.5G before full passes.

## Refreshed targets

- dispo-fallback-off: old `            m = DISPO_ANY_RE.search(plain)` (12 spaces) → new `        m = DISPO_ANY_RE.search(plain)` (8 spaces). Replacement updated to matching 8-space `m = None`. Candidate line 253; the old string was stale already on v5.
- head-qualify-off: no byte refresh needed: `            return len(h.lstrip('#').split()) >= 2` → `            return True`, candidate line 689, occurs once. Its semantics is now explicitly exactly-once; new v6 pin kills it.
- No other carried target or replacement refreshed. Seven added removals disable CD1 recovery, LR1 recovery, TAB1 condition, ID1 folded-id condition, nested-number regex alternative, roman-number regex alternatives, and second-token stripping condition respectively. They are one textual replacement each, not edits to selftest expectations.

## Evidence and risks

Live stage receipts: red-before-v5.txt, mutation-score.txt, stub-control.txt, missing-work.txt, clean-selftest-v6.txt, fallback-patterns-v5.txt. DONE hashes mutants95.py. Dependencies both completed before grading. All requested runs completed; no builds/linters/formatters or wider checks run. No tools installed or upgraded. No supported LSP interface was mounted; this was an independent standalone driver, not a symbol refactor. Scratch deleted before DONE.

Risks: exact textual mutations deliberately couple to candidate bytes; later changes may report BROKEN-PATTERN. Red-before fallback expectation and lineage-count wording are inconsistent as detailed above; measurements are not rewritten to match expectations. No implementation blocker remains.

Self-evaluation: accuracy 4 (red-before expectation mismatch disclosed), completeness 4 (all runs/receipts retained; contradictory semantics resolved explicitly), clarity 4 (expanded command receipts plus alias definitions), actionability 5 (integratable driver and independent rerun commands), conciseness 4 (report detail retained only here). Improvement: parent should retain the explicit semantic arithmetic and red-before discrepancy when citing results.
