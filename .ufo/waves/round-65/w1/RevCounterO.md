# RevCounterO — attack report: accept-o.py FULL / MUTEX

Seat: `kotodama-r65.RevCounterO` (attack/verify leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
(base `17c32302c6845c8f164b985a8cb312d3181c8788`). Scope: `reports/round-65/accept-o.py` FULL and MUTEX,
suffix/`--only` logic, and the mutant-exactness receipt. No mutations performed.

## Snapshot (instrument moved during this review)

| fact | value |
|---|---|
| file reviewed | `reports/round-65/accept-o.py`, sha256 `2a03a2feeec98a88adef99e08cf2230bfeeea81e5f636489b4dd9dab544a54c2`, mtime `2026-10-24 01:52:59 -0300`, 1267 lines |
| prior state at review start | 1246 lines (sha not captured); suffix at line 1240, FULL at 1116 |
| base dry-run receipt | `reports/round-65/telemetry/dry-run-o.txt`, mtime `01:41:29` — **predates the counter revision that cites it** |
| pre-data control | `reports/round-65/telemetry/controls-o.txt`, mtime `01:53:10` |
| VCS state | `git status --porcelain` → `?? reports/round-65/` (counter is untracked; no content pin anywhere) |
| tool under test | `tools/reopen-row.py` sha256 `c0f10a84…9568a0` = base blob (`git show 17c32302:tools/reopen-row.py`) — unchanged |
| installs | none performed (no tool needed) |

The counter gained +21 lines between my first read and this write (revision-2 header at lines 109-113, FULL skip
tolerance at 1134-1139, FRAG `files=0/26` at 1232-1238). All findings below are against the snapshot above.

## Verdicts (as asked)

1. **Can `ACCEPT-O-65: PASS` print from a `--only` run without the filtered marker? — HOLDS: no.**
   `only = {x for x in args.only.split(",") if x}` (line 432 area); `suffix = f" [filtered: {len(legs)}/{len(ALL_LEGS)} legs]" if only else ""` (line 1261). The suffix is unconditional on any non-empty set, and the two other ACCEPT prints are `FAIL` (missing-tool early return) and stderr `ACCEPT_O_INPUT_ERROR` (exit 2). Live check: `python3 -B reports/round-65/accept-o.py --root . --only TOOL` → `ACCEPT-O-65: PASS [filtered: 1/26 legs]`, exit 0. Corner: `--only ,`/`--only=` normalizes to the empty set, i.e. the *unfiltered full battery* (all 26 legs run, no marker) — not a filtered green. Residual (below): filtered runs still exit 0, so exit-code-only automation can record a filtered green without the marker; the claim's own command is unfiltered, so the predicate text is safe on paper.

2. **MUTEX `SWEEP_EXPECT` m1/m2 extras under tool drift — BROKEN (unpassable), with an honesty defect in the diagnostic.**
   Drift direction: the expectation is compared by exact set equality (line 1193), so any drift — m1 losing `EDGE_USERINFO`/`EDGE_HTTPS`, or gaining a failure — is caught loudly as `measured=…!=expect=…`. That part is fail-closed/honest. But the sweep's *measurement* is digit-blind: `failed` is built with `re.match(r"^[A-Z_]+ FAIL", …)` (line 1188), which cannot match `EDGE_308 FAIL` or `EDGE_5TH200 FAIL`. Result: m6/m7 can never equal their expectations (`{"EDGE_308"}`, `{"EDGE_5TH200"}`) regardless of tool behavior. The base receipt proves it is the counter, not the tool: `dry-run-o.txt` MUT (startswith-based, line 1092) reports `m6->EDGE_308 FAIL …` and `m7->EDGE_5TH200 FAIL …`, while MUTEX in the same run reports `m6:measured=[]!=expect=['EDGE_308']`, `m7:measured=[]!=expect=['EDGE_5TH200']`. So MUTEX prints `pinned_not_failed` for mutants that **were** killed — a false diagnostic. Which leg fails first: in a full run, FULL is printed before MUTEX (and is itself unconditionally failing, finding F1), so the transcript's first failing leg is always FULL and never localizes drift; inside MUTEX the first deviation reported is the earliest mutant in `MUTANTS` order (m1, m10, m2, …, per the base table), and `bad[:6]` truncates the printed detail after six entries (the `table=` field still carries all rows).

3. **FULL `len(pass_lines) == len(run_legs_all)` — BROKEN, and no leg can print two PASS lines.**
   AST scan of every `leg(...)` call (26 names): zero call sites inside a `for`/`while`; the seven EDGE/DRIP/FULL/MUT/MUTEX/FRAG names each have two call sites forming an exclusive if/else. Details are single-line reprs — no leg embeds raw multiline stdout/stderr (checked ERR, MALFORMED, GZIP, TRUNC, TIMEOUT, DRIP), so no detail can fabricate a line matching `^[A-Z_]+ PASS`. The count is wrong in the opposite direction: `pass_lines`/`fail_lines` use `^[A-Z_]+ (PASS|FAIL)` (lines 1131/1133), which excludes the two digit-bearing leg names, so a 100% green inner battery yields `pass=21/23`. Base receipt confirms: `FULL FAIL exit=0 pass=21/23 skip=3 fail=0 wall=426.3s` — exit 0 means the inner 23-leg verdict was PASS (all executed legs green), yet FULL still failed. Constraint unsatisfiable.

## Findings by severity

### F1 — CRITICAL: FULL is unpassable; claim O's predicate cannot be satisfied
`reports/round-65/accept-o.py:1126-1146`.
Revision 2 fixed only one of the three causes visible in its own forcing receipt:
- fixed: SKIP tolerance now allows exactly `{FULL SKIP, MUTEX SKIP, FRAG SKIP}` (lines 1138-1139, 1143);
- **still broken:** `len(pass_lines) == len(run_legs_all)` counts 21 against 23 because `EDGE_308`/`EDGE_5TH200` are regex-invisible (F3);
- **still broken:** `verdict_line == ["ACCEPT-O-65: PASS"]` (line 1144) can never hold, because the FULL subprocess is invoked with `--only` (line 1128) and therefore always appends ` [filtered: 23/26 legs]` (line 1261). The inner ACCEPT line is deterministic: `ACCEPT-O-65: PASS [filtered: 23/26 legs]` whenever green.

Consequence: on **any** tool state, a full run appends `False` for FULL, so `verdict = all(legs)` is always False: `ACCEPT-O-65: PASS` can never print, exit is permanently 1. `claims.json` predicate "every leg … prints PASS" is unsatisfiable at this snapshot. `controls-o.txt` control 1 quotes the very receipt line that proves the other two causes (`pass=21/23` and `exit=0` ⇒ filtered ACCEPT) and repairs only the skip clause: the repair is incomplete, not merely in-progress.
Remediation (reviewer, not applied): make the regexes `^[A-Z0-9_]+ (PASS|FAIL)`; compare the inner verdict to the exact expected filtered string `ACCEPT-O-65: PASS [filtered: 23/26 legs]` (prefix matching alone would accept an inconsistent count), or suppress the marker in the self-re-execution via a dedicated flag/env and assert no user filter.

### F2 — HIGH: MUTEX m6/m7 are permanently unmeasurable (digit-blind FAIL extraction)
`reports/round-65/accept-o.py:1187-1195`.
Same root cause as F3, on the MUTEX side: `failed` never contains `EDGE_308`/`EDGE_5TH200`, so `set(failed) != expect` fires for m6/m7 always, and `pinned_not_failed` reports a kill failure that did not happen. Base receipt: MUTEX `bad=[m6:pinned_not_failed=['EDGE_308'], m6:measured=[]!=expect=['EDGE_308'], m7:pinned_not_failed=['EDGE_5TH200'], …]` vs MUT `kill_evidence` containing `m6->EDGE_308 FAIL` and `m7->EDGE_5TH200 FAIL`. The other eight mutants' measured rows already equal `SWEEP_EXPECT` at base, so a digit-aware regex is sufficient to make the sweep satisfiable. `controls-o.txt` control 3 says "under debug … will be repaired or dispositioned before integration" — the root cause is exactly line 1188, and the disposition must not be "accept the mismatch."

### F3 — HIGH (latent, same predicate): FULL's fail-side extraction is digit-blind
`reports/round-65/accept-o.py:1133`. If `EDGE_308`/`EDGE_5TH200` fail in the inner run, `fail_lines` stays 0 and the detail prints `fail=0` while `exit=1`. Today the count check masks this by always failing; a future repair that relaxes the count (e.g. to 21) would let the two legs' failures ride on `fc==0` alone and silently report `fail=0`. Fix both regexes together.

### F4 — MEDIUM: the exactness receipt's tool identity is decorative
`reports/round-65/accept-o.py:1198-1213`. `sweep_text` embeds a hardcoded `tool sha256 c0f10a84…9568a0`, but the comparison is only `committed.splitlines()[-len(sweep_rows):] != sweep_rows` — header and sha line are never regenerated-and-compared, and the tool's sha256 is never recomputed. A committed `exactness-sweep-o65.txt` generated against a *different* tool revision with the same ten rows passes. (The constant happens to equal the current/base tool sha — verified — so it is accurate today, but unenforced.) Remediation: compare the whole regenerated `sweep_text` (header + rows) to the committed file, or recompute `sha256(src)` and compare it to the committed header. Note also the receipt path is still absent (`not_committed` at base; no `exactness-sweep-o65.txt` in telemetry as of this write), so the receipt leg has never been exercised green.

### F5 — MEDIUM: MUTEX ignores the mutant subprocess exit code and stderr
`reports/round-65/accept-o.py:1184-1195`. `xc` is captured and unused; `xe` is unused. A mutant run that crashes (Traceback) *after* emitting the expected FAIL lines still matches the expectation and contributes a clean row. Fail-closed for crashes that suppress lines, but a crash is itself a counter defect and should be recorded: require `xc == 1` and `"Traceback" not in xe` per mutant.

### F6 — MEDIUM: SWEEP_EXPECT's m1/m2 "extras" pin incidental blast radius, not required semantics
`reports/round-65/accept-o.py:1154-1165`. `m1` additionally expects `EDGE_USERINFO+EDGE_HTTPS`; `m2` additionally expects `EDGE_MALTARG`. These are a snapshot of the round-64 tool's collateral kills, not mutations of the surface each mutant targets. Monotone in the safe direction (a benign extra guard that kills one more leg blocks PASS → no false green), so this is a brittleness/honesty-of-label issue (a benign tool change reports as `measured != expect`, indistinguishable from a mutant not being killed) rather than a bypass. Since claim O is counter-only and `tools/reopen-row.py` is unchanged, this does not bite this round — but it will on the next tool edit; consider pinning only `pinned` (superset semantics) plus a separately disclosed `TABLE` census, or keying expectations to mutation semantics.

### F7 — MEDIUM: the instrument moved after its base receipt, and nothing pins its content
Facts: counter mtime `01:52:59` > `dry-run-o.txt` mtime `01:41:29`; revision-2 header explicitly cites the base receipt as forcing evidence; `controls-o.txt` (01:53:10) records the repair; `claims.json` mtime `01:53:44`. `reports/round-65/` is untracked (`??`), `claims.json` carries no instrument sha256, and `controls-o.txt` names no counter sha. Therefore (a) the recorded base FAIL lines were produced by an instrument that no longer exists on disk, and (b) any further pre-data edit silently invalidates every quoted control without any tripwire. The header also still says "revision 1 (pre-data)" at line 84 while two revision blocks exist at 108-113. Remediation: record `accept-o.py` sha256 in `controls-o.txt` (and replay the base controls against that exact sha), and re-capture `dry-run-o.txt` after the last pre-data revision, or mark which receipt lines are rev1 vs rev2.

### F8 — LOW: `dry-run-o.txt` header contradicts its own body
Line 1 asserts "FULL/MUTEX/FRAG must FAIL"; the body is `FRAG PASS … 0 file(s)` (the vacuous-empty-dir pass that `controls-o.txt` control 2 then repairs). Not a FULL/MUTEX defect, but the receipt is being cited as authority for instrument revisions, so its header should match its content per revision.

## Residual risk

- The filtered-run exit code is still 0 (line 1262 returns `0 if verdict else 1` with `verdict` over executed legs only). The marker prevents a *transcript* from being mistaken for the full verdict, but a receipt that quotes only exit status can still record a filtered green. Suggest a distinct non-zero exit (or a required `--full` evidence file) for `--only` runs.
- `MUTEX` writes nothing: the sweep receipt must be hand-assembled from the `table=` detail (or re-run). That is an easy place to paste rows from a different run; F4 is the only defense and it does not cover the header.
- Both affected legs depend on `MUTANTS` needle uniqueness (`tool_text.count(needle) != 1`): any tool drift that duplicates a needle aborts the mutant with a `needle_count` entry rather than a skipped mutant — fail-closed, noted only because it changes the failure mode.

## Verification performed / gaps

Performed (no lane writes; temp fixtures only):
- `python3 -B reports/round-65/accept-o.py --root . --only TOOL` → `TOOL PASS …`, `… SKIP` ×12 including `FULL SKIP/MUTEX SKIP/FRAG SKIP`, `ACCEPT-O-65: PASS [filtered: 1/26 legs]`, exit 0.
- Regex probe: `re.match(r'^[A-Z_]+ (PASS|FAIL)', …)` on `EDGE_308 FAIL`, `EDGE_5TH200 PASS`, `EDGE_USERINFO FAIL`, `MUTEX PASS` → False, False, True, True.
- AST scan of all `leg(` call sites (0 inside loops; 26 names; if/else exclusivity).
- Read-only git: base blob sha of `tools/reopen-row.py`, `??` status of `reports/round-65/`, absence of `accept-o.py` in base.
- Re-read of `dry-run-o.txt` (FULL/MUTEX/MUT/FRAG lines) and `controls-o.txt`.

Gaps: I did **not** execute FULL (426 s at base) or a full MUTEX sweep (ten mutant subprocesses) inside the 15-minute box; the FULL conclusion rests on the frozen receipt's `exit=0 … pass=21/23 skip=3` plus the code/regex trace, which is sufficient because all three causes are static. No green-state MUTEX run exists on disk to inspect (receipt absent). The counter changed mid-review; if revision 3 lands, re-check the two FULL predicates (digit-aware counts, exact filtered verdict) and the two MUTEX regexes before treating this report as current.
