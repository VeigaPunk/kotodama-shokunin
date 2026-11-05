# ReviewerFreeze — round-92 predicate freeze review (seat: ReviewerFreeze-2)

Date: 2026-11-05. Scope: read-only attack of the frozen round-92 predicate at
freeze `066b9728fc64e78735769c4740d05c1000d31a3b`, base `21350361500aa000b90f91082bf9d7295a9c24cd`,
lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

Freeze identity verified first: `git show 066b9728…:tools/check-advance-evidence.py`
sha256 = `905be2fed386c491d52224832ea75ed8c7b02e67c1b021b2c66511658c1c1422` = worktree bytes
= declared O.tool_sha256. Also byte-identical freeze↔worktree: claims.json (`e07f669b…`),
measure92.py (`f170cc8f…`), make-counterfeits.py (`86d3b816…` = declared). `git diff --stat
066b9728… HEAD` over the three frozen paths is empty. Lane HEAD is `66b3ae93…` (locally ahead of the freeze; frozen files unmoved).

## (a) Clause → leg map (QUALITY 11)

O (claims.json `legs.O`, 8 legs, emitted by measure92.py `grade_o` in exactly this order):
| claims.json clause | checker leg | verified by |
|---|---|---|
| lands materialized | MATERIALIZE (archive + tools/ dir check) | measure92.py grade_o |
| tool sha == O.tool_sha256 | TOOL (`got == want`) | measure92.py grade_o |
| selftest rc0 "869→89/89" | SELFTEST (rc + `SELFTEST PASS n/n` regex + total==`O.selftest_checks`) | measure92.py grade_o |
| exactly N `  ok ` lines | OKCOUNT (`count_ok`) | measure92.py grade_o |
| all 21 refusal names ok | REFUSALS (regex `^  ok +<esc(name)>:` over selftest output) | measure92.py grade_o |
| killed==total>=60, 0 survived, 0 broken-pattern | MUTATION (`MUT_RE`) | measure92.py grade_o + mutants.py run |
| committed receipt exists, same tool sha, same numbers | MUTRECEIPT | measure92.py grade_o |
| stub refused by OKCOUNT and kills 0 | STUB | measure92.py grade_o |

C: claims.json `legs.C` = 4 counter legs; `C.legs` = 8 tool-level legs folded inside the
ENTRY leg (measure92.py `grade_c` collects `seen = {name: verdict}` from `LEG (PASS|FAIL) (\S+)`
lines and fails ENTRY on any of `c['legs']` missing or FAIL). Verified code path; all 8
names were actually emitted in my v3-tool entry runs (`LEG PASS ENTRY/SHAPE/TOPIC/NEWIDS/
UNIQUENESS/GATE/CAPTURE/APPENDONLY` seen in xprobe runs).
| claims.json C clause | checker | verified |
|---|---|---|
| lands materialized | MATERIALIZE | code read |
| entry eight legs pass at law-floors of claims.json | ENTRY (subprocess of freeze-pinned tool) | code read + live tool runs |
| index tool exit 0 | INDEX (freeze's tools/check-corpus-index.py) | code read |
| no base row removed/cell-changed; >=3 new mined A/B rows opened 2026-11-05, cited, used-by naming entry, README row; malformed rows are leg FAIL (W3) | APPENDONLY (counter-level registry leg; `registry_rows` keeps malformed rows and len<11 → problems) | code read |

Every graded gate clause has a leg. No clause was found without a checker.

Findings (informational, not gate defects):

- **D1 (informational, prose≈instrument).** claims.json `separability` reads "The counter's
  **separability leg** builds both overlays from committed revisions" — no leg list (legs.O,
  legs.C, C.legs) contains a leg named SEPARABILITY. The materialization-of-overlays
  behaviour is real (measure92 materializes committed revisions), but the prose names a leg
  the instrument does not have. Frozen-data cosmetic; recommend rewording only if claims.json
  is ever amended upstream (it is frozen; do not amend now).
- **D2 (informational).** `O.v2_tool_sha256_base` (88597a66…) is declared but the counter
  never reads it; the base-side control lives in `controls/before-v2-counterfeits.txt` and
  the O.before prose instead. Provenance-only; no gate depends on it being verified live.

## (b) LEGCOUNT

measure92.py main(): after grading, `names = [n for n,_ok,_e,_o in legs]`; if
`names != cfg['legs'][claim]` → `raise Refused(f'LEGCOUNT: counter leg table {names} disagrees
with the frozen list {frozen_legs}')` → exit 2 (measure92.py, main(), the check sits before
receipt emission; the REFUSED path exists and precedes any PASS output). Emitted O legs read
from code: MATERIALIZE TOOL SELFTEST OKCOUNT REFUSALS MUTATION MUTRECEIPT STUB — equals
claims.json legs.O exactly. C emitted: MATERIALIZE ENTRY INDEX APPENDONLY — equals legs.C exactly.
Also `# frozen legs:` header line is emitted with the frozen list. PASS.

## (c) refusal_cases vs selftest

All 21 declared names (jq extraction, 21 rows) appear as `  ok <name>:` in the selftest
output in every passing run; name strings match the selftest case labels byte-for-byte
(grep'd each). Verified across: 25 fresh-dir burst runs (all PASS), 3 fresh+reuse pairs,
4 rm-rf-between runs, 12-concurrent pressure triad (concurrent-same-dir collisions produce
rc=2 refusals, not false PASS), env-i (empty env minus PATH/HOME) run, `env -u TMPDIR` run,
fleet-cwd and round-92-cwd runs, plus worktree-path copies.

**D3 (residual risk, unresolved, fail-closed).** One intermittent selftest outcome exists:
SELFTEST FAIL 88/89 with `BAD capture byte-copies the base registry: rc=1 tail=['ENTRY-EVIDENCE:
FAIL legs=7/8 failed=CAPTURE']` (outputs selftest.out 10:27:51, selftest2/3.out 10:36,
st2now.out/bn999.out 10:54, all in my scratch). The failing check itself is an *extra*
tool selftest: the tool's own kill-switch works in the immediate runs I inspected — the BAD
case is: my own fixture keeps its capture of `reports/round-90/evidence/S011.txt` sha-copy of
`basereg.txt` in the graded set; `capture is a graded file: {rel}` short-circuits correctly
(tool.py L239 vs L249 branches). When the skip-fires instead (vals hit the (w,d)-skips),
the entry verdict becomes `FAIL legs=7/8 failed=CAPTURE`, which the selftest's own `chk`
cannot accept; the run's `ok` count drops to 88, SELFTEST rc 1.
Effect on the counter under this state: SELFTEST rc 1 → SELFTEST leg FAIL; OKCOUNT=88<89 FAIL;
REFUSALS misses one of the 21 names FAIL; MUTATION clean-baseline `rc=1` → `MUTATION-SCORE:
0/60 … (clean tool not green first)` FAIL. All four legs reject — **the flake can only ever
kill a true lands claim, never pass a bad tool**; fail-closed. The committed receipt proves
the clean baseline was green at freeze time (header `# clean selftest rc=0 ['SELFTEST PASS
89/89']`, bytes sha `6b2a1b8a…` independently confirmed identical from the do-nothing seat's
scratch copy `st-donothing/mutation-score-lands.txt`), and I fully re-replicated the 60/60
receipt twice post-window (harness via python subprocess twice, bg_5462 and bg_5479; both
receipts sha `6b2a1b8a…` = committed = do-nothing copy). Trigger mechanism unresolved after
~40 controlled variations (env, cwd, dir reuse, hash seed rig, concurrency, cp-shape replay);
it confined itself to a single 10:27–10:54 window and has not reproduced since. Recommend
the L1 notice this as a reproducibility (not refusal-bypass) gap: gate stability of the
live-run legs depends on an environment state I could not pin down.

## (d) Counter constant provenance

Read of measure92.py in full: `claims()` = `git_show(root, freeze, 'reports/round-92/claims.json')`
— the ONE constants source. `run_mutation` writes `git_show(freeze_root, freeze, 'reports/round-92/mutants.py')`
to work. STUB writes `git_show(root, freeze, cfg['O']['stub_control'])`. grade_c materializes
lands with `git archive`; the tool for ENTRY is `git_show(root, freeze, 'tools/check-advance-evidence.py')`;
INDEX reads `cfg['C']['index_tool']` from the freeze; base registry/lesson come from
`git_show(root, cfg['base'], …)` — cfg['base'] itself read from the freeze's claims.json.
No constant is read from the graded tree. The counter stamps its own sha in the receipt
(transparent, not a trust anchor). PASS.

## (e) MUTRECEIPT

Committed reports/round-92/mutation-score.txt: header line 1 `# tool sha256 905be2fe…`
matches O.tool_sha256 (regex `^# tool sha256 ([0-9a-f]{64})$` in measure92 catches this);
line 2 `# clean selftest rc=0 ['SELFTEST PASS 89/89']`; score line
`MUTATION-SCORE: 60/60 killed, 0 survived, 0 broken-pattern` → MUT_RE groups (60,60,0,0):
killed==total, total 60 ≥ O.mutation_min 60, survived 0, broken 0. Byte-identical to my two
independent live harness replications (sha 6b2a1b8a… all three) and to the do-nothing seat's
lands copy. The D4 fix is present in mutants.py code: the clean run's own rc and first stdout
line are captured (`clean_rc, clean_head = run(clean_tool, …)`) and written into the header
(`# clean selftest rc={clean_rc} {clean_head}`), not hardcoded. Receipt carries all 60 KILLED
rows whose names match the frozen mutant tuple list exactly (diff of name sets = empty).
PASS.

## (f) Mounting of the chrome-quote partial-defence tradeoff in O.bounds

Present verbatim in claims.json O.bounds: "…and the gate-quote topic binding is a partial
defence: a forger who also forges the manifest quote field still passes it (attacks.md
finding 4's stated tradeoff)." PASS.

## Not reached (L1-directed: no further reruns)

- Live measure92 counter run at lands `1473606b` (O 8/8, C 4/4 reported by L1; not re-run by me).
- STUB leg live exercise (stub-tool.py OKCOUNT refusal + 0-killed mutation run) — code path read only.
- Byte-level recomputation of before-v2-counterfeits.txt / after-v3-refusals.txt content —
  builder sha 86d3b816… verified only.
- Root-cause of the D3 intermittent (see D3).

## Evidence files (copied into stage/evidence/)

Passing selftest: f1.out, cwd.out, burst1..25 (in scratch, not copied individually).
Failing-window: selftest.out, st2now.out. Harness receipts: notmp-out.txt, pyharness-out.txt
(both sha 6b2a1b8a… = committed), live-new.txt (fail-window harness header showing rc=1 baseline).
Committed receipt copy: receipt-committed.txt. All shas in stage/MANIFEST.txt.

No tool installs, no sysctls, no writes outside this stage dir, the trailer file, and my scratch.
