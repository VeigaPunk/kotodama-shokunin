# ReviewerFreeze-2 report — round-92 freeze review

Trailer path (relative to lane root): `.ufo/waves/round-92/w1/ReviewerFreeze.md`
Stage dir: `.ufo/waves/round-92/w1/stage/ReviewerFreeze/` (freeze-review.md + evidence/)

## Verdict

No gate-defeating finding. All six assigned checks executed; results:

- (a) Clause→leg map: complete, every O/C clause has a checker leg (map table in stage/freeze-review.md). Two informational notes: claims.json "separability leg" names a leg the instrument does not emit (prose-vs-code cosmetic), and v2_tool_sha256_base is declared-but-unread by the counter.
- (b) LEGCOUNT: PASS — grade_o emits exactly legs.O, grade_c emits exactly legs.C; REFUSED-on-mismatch (exit 2) exists in main() before receipt printing.
- (c) refusal_cases: all 21 declared names appear as `  ok <name>:` in the selftest across 45+ runs (fresh, reused, concurrent, env-varied, cross-cwd). NAME-SETS MATCH.
- (d) Counter provenance: every constant read from `git show <freeze>:…` (claims.json, mutants.py, stub, tool, index tool, base registry/lesson); no graded-tree constant read. PASS.
- (e) MUTRECEIPT: committed receipt header carries tool sha 905be2fe… (= frozen bytes) and `# clean selftest rc=0 ['SELFTEST PASS 89/89']` — the routed D4 fix is real code (`clean_rc, clean_head = run(...)` then the header write, non-hardcoded). Score line 60/60 killed, 0 survived, 0 broken-pattern meets O.mutation_min. Byte-identical (sha 6b2a1b8a…) across: committed file, do-nothing seat lands copy, and two independent live replications of the full harness I ran from frozen mutants.py. All 60 KILLED row names match the frozen mutant tuple list exactly.
- (f) O.bounds chrome-quote partial-defence sentence: present verbatim, naming the manifest-quote-forgery tradeoff with the attacks.md pointer. PASS.

## D-numbered findings

- D3 (the only substantive residual): intermittent tool-selftest state in which the run prints SELFTEST FAIL 88/89 with `BAD capture byte-copies the base registry` (captured outputs in stage/evidence/selftest.out, st2now.out). Effect is strictly fail-closed: in that state SELFTEST rc=1, OKCOUNT 88<89, REFUSALS misses one of the 21 names, and MUTATION's clean-baseline precondition fails (live header showed `rc=1` → 0/60 killed) — every leg that reads the selftest rejects, so the flake can kill a true lands claim but can never pass a bad tool. The committed freeze-time receipt proves the baseline was green at freeze; my post-window replications also came out green. Mechanism unresolved after ~40 controlled variations (env, cwd, dir reuse, PYTHONHASHSEED rig, 12-way same-dir concurrency, sibling-process pressure, exact 10:27 shell-shape replay); confined to the 10:27–10:54 window, not reproduced since. Recommend the L1 record this as a reproducibility gap (counter stability), not a refusal gap.
- D1/D2 informational (claims.json "separability leg" wording; v2_tool_sha256_base unused by the counter) — no gate depends on them.

## Not reached (per L1 halt directive)

Live counter run at lands 1473606b; live STUB-leg exercise; content recomputation of the two counterfeit-control receipts (builder sha 86d3b816… verified only).

## Counts and commands (with rc)

- sha256 checks: tool 905be2fe… (freeze bytes = worktree = declared), claims e07f669b…, measure f170cc8f…, make-counterfeits 86d3b816…, mutants-frozen 31dc3dc3…, committed receipt 6b2a1b8a…; `git diff --stat 066b9728… HEAD` over the three frozen paths → empty.
- Selftest runs executed: 25 fresh-dir burst + 3 reuse pairs + 4 rm-rf-between + 12-way concurrent + 4 rm-rf + misc ≈ 50+; passing runs 89 `  ok ` lines, `SELFTEST PASS 89/89`, rc0.
- Full mutation harness from frozen mutants.py: run 1 (no TMPDIR) 60/60 killed; run 2 (with TMPDIR) 60/60 killed; both receipts byte-equal the committed one. Fail-window runs printed 0/60 with `clean tool not green first: rc=1` — reproduced the exact committed-receipt disagreement signature the counter's MUTRECEIPT leg is built to catch (proving the leg bites).
- No tool installs; no sysctls; no writes outside my stage dir, this trailer, and /fast/scratch/hyaku/kotodama-r92/ReviewerFreeze/.
