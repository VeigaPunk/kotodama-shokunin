# MutationTester94 — round 94 wave 1, claim O mutation probe

Scope: read-only mutation probe. No production edits, no commits, no lane writes outside the stage dir and this report.

## Base (v4, e7fa8eaf) — five routed mutants

Tool sha256 9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7 (checked by `sha256sum`).
Command: `python3 -B ExecMutants94/mutants94.py --tool <scratch>/base-tool.py --work <scratch>/base-run --only script-strip-off,comment-strip-off,unescape-off,dispo-any-casei,baserows-drop-cell8` → rc 1.

- script-strip-off SURVIVED (selftest rc 0)
- comment-strip-off SURVIVED (selftest rc 0)
- unescape-off SURVIVED (selftest rc 0)
- dispo-any-casei SURVIVED (selftest rc 0)
- baserows-drop-cell8 SURVIVED (selftest rc 0)
- `MUTATION-SCORE: 0/5 killed, 5 survived, 0 broken-pattern`

Matches ExecMutants94 red-before-v4.txt exactly.

## Candidate (v5) — full set

Tool: ExecGraderV5/check-advance-evidence.py, sha256 7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff. Clean selftest: `SELFTEST PASS 126/126`, rc 0.
Command: `python3 -B ExecMutants94/mutants94.py --tool <scratch>/v5-tool.py --work <scratch>/mut` → rc 1 (88 mutants: 83 round-93 + 5 routed).

**MUTATION-SCORE: 86/88 killed, 1 survived, 1 broken-pattern**

Non-killed rows:
- `MUTANT head-qualify-off SURVIVED selftest_rc=0` — survivor
- `MUTANT dispo-fallback-off BROKEN-PATTERN selftest_rc=n/a` — counter stale (pattern at 12-space indent; v5 has it at 8 spaces inside `_dispo_match`)

All five routed mutants are KILLED on v5 (script-strip-off, comment-strip-off, unescape-off, dispo-any-casei, baserows-drop-cell8, selftest_rc=1 each).

## Frozen predicate verdict (claims.json O.MUTATION)

Requires killed == total, survived == 0, broken-pattern == 0. **Not met**: survived 1, broken-pattern 1. The five routed classes are all killed (their part of the predicate holds).

## Survivor and recipe (detail in stage/MutationTester94/survivors.md)

- `head-qualify-off`: replace `            return len(h.lstrip('#').split()) >= 2` (v5 line 633, `head_anchors`) with `            return True`. Survives on v5 (126/126 PASS). **Killable**: a pin with a one-token-heading fixture (`## address` … with `min_topic_phrases=4`, `min_anchor_span=0`, expecting `FAIL TOPIC` / `phrase anchors 0/4`) passes on clean v5 (127/127) and kills the mutant (126/127 FAIL). The pin is **not in the candidate**; it must be added to the candidate selftest.
- `dispo-fallback-off`: not a survivor. Re-targeted to v5's line (`        m = DISPO_ANY_RE.search(plain)` → `        m = None`) it is killed (124/126 FAIL). The frozen pattern needs updating for v5.

## Files

- stage/MutationTester94/mutation-score.txt (full driver stdout + receipt; sha256 786c9eb1431213160237cf7a912bfc7a08b35f92c1ecf518d7361a9408e3a211)
- stage/MutationTester94/base-v4-five.txt (base five-run receipt; sha256 5c17a8b477d50fe1ffe24b607daf699374a93c315b1e70addd6cfe395d8e7609)
- stage/MutationTester94/survivors.md
- stage/MutationTester94/probes/probe.py, hq.py, v5-with-singletoken-pin.py (scratch probe sources, kept as evidence)
- stage/MutationTester94/DONE

## Tooling record

No installs or upgrades. No pacman, sysctl, git mutation, or writes outside the stage dir and this report. Scratch /fast/scratch/hyaku/kotodama-r94/MutationTester94 deleted before yield.
