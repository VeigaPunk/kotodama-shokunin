# MutationTester94 — survivors on the v5 candidate

Tool under test: ExecGraderV5/check-advance-evidence.py, sha256 7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff.
Driver: ExecMutants94/mutants94.py (sha256 cdaf7f24…), run as `--tool <scratch>/v5-tool.py --work <scratch>/mut`.
Clean v5 selftest: `SELFTEST PASS 126/126`, rc 0.
Result: `MUTATION-SCORE: 86/88 killed, 1 survived, 1 broken-pattern` (driver rc 1).

Frozen MUTATION predicate (claims.json O.MUTATION: survived == 0 and broken-pattern == 0): **FAILS**.

## S1 — `head-qualify-off` — SURVIVED (rc 0, PASS 126/126)

- Target (v5 line 633, in `head_anchors`, the phrase-hit surface):
  `            return len(h.lstrip('#').split()) >= 2`
- Smallest surviving recipe: replace that one return with `            return True`.
- Why it survives: `head_anchors` only feeds `hit_heads` → `anchor_text` → the phrase-floor count. The span count uses `head_span_anchors`, which is unchanged. No v5 selftest fixture has a one-token heading whose sole word is a single-word phrase while the phrase floor is the only failing leg. The existing phrase pins (`sub-topic phrases absent from headings`, `phrase floor unmet on a real entry`) fail under the mutant too, so they do not distinguish.
- Pin that kills it: **none exists in the v5 candidate.** A proposed pin, verified in scratch:
  `chk('single-token headings anchor no phrase', ['entry'] + E(entry=single_tok, min_topic_phrases='4', min_anchor_span='0', min_topic_overlap='1'), 1, ['FAIL TOPIC', 'phrase anchors 0/4'])`
  with `single_tok` = a file whose only headings are `## address`, `## petition`, `## efficacy`, `## table` (one token each), plus filler body and no table rows containing the phrases.
  - Clean v5 + pin: `SELFTEST PASS 127/127` (rc 0). Pin file: `probes/v5-with-singletoken-pin.py`, generator `probes/probe.py`.
  - v5 + pin + `head-qualify-off`: `SELFTEST FAIL 126/127`, line `BAD single-token headings anchor no phrase: rc=1`. Killed.
  - v5 without pin + `head-qualify-off`: `SELFTEST PASS 126/126` (rc 0). Survives (confirms the gap).
- Not applied by this seat: the candidate and its selftest are read-only here. The executor/L1 must add the pin for O.MUTATION to pass.

## S2 — `dispo-fallback-off` — BROKEN-PATTERN (not a survivor; counter is stale)

- The frozen pattern `            m = DISPO_ANY_RE.search(plain)` (12-space indent, v4 layout) matches **0 times** in v5. The v5 refactor moved the unanchored fallback into `_dispo_match` (v5 line 253) at 8-space indent: `        m = DISPO_ANY_RE.search(plain)`. The driver refuses a 0-match pattern as BROKEN-PATTERN, so the mutant never ran.
- Re-targeted diagnostic (scratch only, not counted in the score): replace the v5 line with `        m = None`. Result: `SELFTEST FAIL 124/126`, rc 1 → **killed**. The unanchored fallback is pinned; the mutant is killable.
- Verdict: the counter is stale, not the candidate. For O.MUTATION the broken-pattern count must be 0, so the mutants94.py pattern must be updated to the v5 target (in-wave counter; L1 integrates).

## Routed five on v5 (all KILLED, rc 1 each)

| mutant | v5 verdict | driver line |
|---|---|---|
| script-strip-off | KILLED | `MUTANT script-strip-off KILLED selftest_rc=1` |
| comment-strip-off | KILLED | `MUTANT comment-strip-off KILLED selftest_rc=1` |
| unescape-off | KILLED | `MUTANT unescape-off KILLED selftest_rc=1` |
| dispo-any-casei | KILLED | `MUTANT dispo-any-casei KILLED selftest_rc=1` |
| baserows-drop-cell8 | KILLED | `MUTANT baserows-drop-cell8 KILLED selftest_rc=1` |

## Base v4 five (control)

`base-v4-five.txt`: 0/5 killed, 5 survived, 0 broken-pattern on the v4 base (sha 9799a96c). Matches ExecMutants94 `red-before-v4.txt` line for line (selftest rc 0 on every mutant).

## Counts and commands

- `python3 -B ExecMutants94/mutants94.py --tool <scratch>/v5-tool.py --work <scratch>/mut` → rc 1; 88 `MUTANT` lines (grep -c "^MUTANT" = 88); `MUTATION-SCORE: 86/88 killed, 1 survived, 1 broken-pattern`.
- Clean v5 green first: `# clean selftest rc=0 ['SELFTEST PASS 126/126']`.
- Not measured: none of the 83 round-93 mutants were re-classified by hand; only the driver verdicts are reported.
