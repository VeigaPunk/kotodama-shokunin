# ReviewerO100 — non-author review of claim O landing (kotodama round 100, attempt 1)

Reviewed bytes: `tools/check-table-support.py` sha256 `972cefea2b429a9d9ca3d9efc1acf3a63391e7c6ba2da576a1225fda6258b73a` (634 lines, the bytes present at both DONE markers). Counter run at 2026-11-06 ~09:0x over the landed lane with `--base-rev 60010a55fb5f04ee728070c463b1a57ae1cc17fc`. Dependencies awaited: `stage/ExecTableSupport100/DONE` and `stage/MutationTester100/DONE` (bounded loop, both present).

## 1. Verdict

**Legs O0–O4: PASS. O5: FAIL at review time — L1-owned registration not yet landed (scorecard-capability-rows=0, skill-mentions=0).**

Per my seat scope (judge O0–O4; report O5 state): the executor-owned surface of claim O is sound. Every conformance probe I built agrees with the L1's frozen feasibility reference. The claim as a whole (predicate O0–O5) is **not yet held as measured**; the first failing leg is **O5**, which is the L1's landing step (SCORECARD capability row + SKILL.md mention), outside executor scope and expected to complete with the L1's commit. No defect is attributable to `tools/check-table-support.py` or `mutants100.py`.

## 2. Counter output (my run; stage file `counter.txt`)

```
LEG O0 PASS tool-sha256 972cefea2b429a9d9ca3d9efc1acf3a63391e7c6ba2da576a1225fda6258b73a
LEG O1 PASS 40/40 floor=24 rc=0
LEG O2 PASS cases=28 pass=28 fail=0 traceback=0 rc=0 failing=[]
LEG O3 PASS actual rc=0 findings=0; forged rc=1 findings=1;
        forged-minus-actual=[('UNSUPPORTED-CELL', 'Yoruba', 'limit on the praise')] actual-minus-forged=[] evidence-dirs=22
LEG O4 PASS 36/36 killed, 0 survived, 0 broken-pattern (floor total 20) rc=0
LEG O5 FAIL scorecard-capability-rows=0 skill-mentions=0
PREDISPATCH-100: FAIL legs=10/15   (counter_rc=1; the 5 failures are O5 + C1/C4/C6/C9, claim-C scope, out of my seat)
```

O3 is exactly the frozen R99-M2 expectation: mutating the Yoruba limit cell to the round-99 outrun sentence yields precisely one new finding `(UNSUPPORTED-CELL, Yoruba, <last header cell>)`, forged rc 1, and the unmutated entry stays clean — the historical capture-outrun is now caught.

## 3. Pin binding and order

| artifact | value | matches |
|---|---|---|
| battery100.py (disk sha256) | `b78176e31c9bfc8f22c8269d7f4217c44a9a9e45a28db8a1c33ed5d43b47a02d` | — |
| reports/round-100/controls/battery100.sha256 | `b78176e3…` | = disk |
| battery100-control-base.txt `BATTERY-SHA256` | `b78176e3…` | = disk = pin |
| battery100-feasibility.txt `BATTERY-SHA256` | `b78176e3…` | = disk = pin |
| mutants100.py (disk sha256) | `18dbcf3b02ef57625b8593a7a514e35b3055e6ad2838fb2d81ec5e9175903424` | — |
| reports/round-100/controls/mutants100.sha256 | `18dbcf3b…` | = disk |
| mutation100-first.txt line 1 `DRIVER-SHA256` | `18dbcf3b…` | = disk = pin |

- Freeze commit membership (`git ls-tree 255d84776c12c918b7bfb2a7173d7b495e3f966e`): battery100.py, battery100.sha256, battery100-control-base.txt, battery100-feasibility.txt all present as blobs (and byte-identical to disk — 7/7 frozen files MATCH, `git show <rev>:<f> | sha256sum` vs disk). The two mutation control files are correctly absent from the freeze commit (produced this round by MutationTester100, the named exception) and are untracked at review time — the L1 is the sole committer.
- Order: `mutants100.sha256` mtime 2026-11-06 08:47:39 predates `mutation100-first.txt` mtime 08:48:26, and the receipt's first line pins the same driver sha — the pin was fixed before the first measurement was recorded.
- First receipt records `MUTATION-SCORE: 36/36 killed, 0 survived, 0 broken-pattern` against an intermediate TOOL-SHA256 `271c42fa…`; the counter's O4 re-runs the pinned driver live against the landed tool and reproduced 36/36, so the score is current-bytes, not stale.

## 4. Contract conformance (claims.O.contract → tool lines → probes)

| clause | tool line(s) | battery covers | my extra probe |
|---|---|---|---|
| cli (flags, `--selftest --work`) | 596–601, 605 | E4, T1/T2, selftest path | FX14 (text mode multi-finding) |
| scope: caption regex `\brecorded cases?\b/i` on contiguous non-blank/non-heading/non-table paragraph above header | 165 (+ walk 119–126 in `tables()` 107–137) | B3, B7, F7, F9 | FX1 (two-line caption paragraph, phrase on 2nd line), FX2 (heading blocks caption), FX3 (prior table blocks caption) |
| binding: label tokens `*_\`` stripped, NFKD-folded, len ≥ 3, not STOP, not 'and'; token equality | 103–105, 199–204 | F2, F5, F8, F10, F12 | FX9 (accented label `Òrìṣà` binds via fold), FX10 (len<3 `Ox`, STOP `Each` cannot bind) |
| binding: contiguous paragraph below last data row | 128–136 | F8 | FX2/FX3 (block boundaries) |
| support: capture `<evidence>/<S-id>.txt` first dir holding it; backticked `path.md:a[-b]` from `<root>/corpus/knowledge` | 171–196 (first-dir 174–177) | B4, F3, F4 | FX5 (path range 1–2), FX6 (out-of-range slice), FX7 (two evidence dirs, first-dir precedence), FX4 (path with no `--root` → NO-PATH) |
| support_rule: fold/content (NFKD, ≥4, STOP, dedup) | 72–97, 56–61 | B2, B5, B6 | FX16 (non-UTF-8 capture read lossily, never rc 2) |
| support_rule: stem() ies→y; es after s/x/z/ch/sh; trailing s not ss | 81–89 | B2 | FX12 (`drums classes lullabies` vs capture; `strangers villains` absent) |
| support_rule: best = max distinct stems in any 80 consecutive tokens of a single support text | 139–158 (WINDOW=80 line 54) | B8, F11 | FX13 (exact boundary: distance 79 co-occurs, distance 80 never does) |
| support_rule: supported iff best*4 ≥ total*3 | 214 (SUPPORT_NUM/DEN line 55) | B9, F13 | FX13 (`(1,2)` → unsupported) |
| findings: UNSUPPORTED-CELL {row, col, words, best, total} | 217–218 (col fallback 216) | F1, F7, F11, F13 (words+best) | FX11 (ragged row → numeric col `3`), FX12, FX13, FX6 |
| findings: UNBOUND-ROW when no line binds or no line carries S-id/path | 204 | F2, F5, F8, F10, F12 | FX10 |
| findings: NO-CAPTURE once per table | 170, 178–179 | F3 | FX8 (same bad id in two tables → two findings) |
| findings: NO-PATH | 189 | F4 | FX4, FX6 |
| output: --json object, text FINDING lines + `TABLE-SUPPORT:` summary, rc 1/0 | 619, 623–624 | T1, T2, all json cases | FX14 (3-line text payload byte-equal to ref) |
| errors: rc 2 TABLE_SUPPORT_ERROR, no traceback, on missing/non-UTF-8 entry, missing evidence dir, no --evidence | 607, 610, 614, 625–628 | E1–E4 | FX16 (capture encoding is NOT an error channel) |

**Fixture suite:** 16 fixtures (none duplicating a battery case) — `FIXTURE-SUMMARY cases=16 pass=16 fail=0` (rc 0), tool and frozen ref byte-equal on every fixture (JSON dict equality + rc equality; text mode line equality).

**Ref-vs-tool disagreements over the corpus:** ran both over every `corpus/knowledge/**/*.md` with `--root <lane>` and all `reports/round-*/evidence` dirs (21 dirs at run time): `CORPUS-COMPARE files=271 disagreements=0` (rc 0). No finding anywhere.

**Documented delta (observation, not a defect):** a capture file that exists but is unreadable (chmod 000) yields rc 2 `TABLE_SUPPORT_ERROR` (tool lines 180–185, 191–195, selftest pins E7/E7dir at 544–570) where the frozen ref would raise an uncaught PermissionError (traceback). The frozen contract's rc-2 list does not name this input; the tool's docstring does. A directory named `<S-id>.txt` is NO-CAPTURE at rc 1, matching ref semantics exactly. No battery case, corpus file, or counter leg exercises the chmod-000 path. Strictly more graceful than the ref on an input class the contract does not enumerate — flagging for the record only.

## 5. Harm check

`git diff --stat 60010a55fb5f04ee728070c463b1a57ae1cc17fc -- tools/` → empty (no tracked file changed); `git status --porcelain -- tools/` → only `?? tools/check-table-support.py`. No existing tool, gate or selftest touched. Frozen controls byte-match the freeze commit (7/7 MATCH, §3). Scratch-only fixtures; nothing written outside my stage/scratch.

## 6. Selftest strength (branch-revert proof, scratch copies only)

| patch (reverted branch) | expected pin to fail | result |
|---|---|---|
| window eviction off (`if idx >= WINDOW:` → `if False:`) | F11-window-80-colocation | rc 1, `SELFTEST PASS 32/33` (interim bytes) / failing=[F11] |
| threshold weakened (`best * 4 < total * 3` → `best == 0`) | F13-threshold-three-quarters | rc 1, failing=[F1, F11, F13] |
| binding by substring instead of token equality | F10-token-not-substring-binding | rc 1, failing=[F10] |
| caption scope widened to any `recorded` | B7-unrecorded-out-of-scope | rc 1, failing=[B7, B7b] |

`REVERT-SUMMARY patches=4 proved=4` (rc 0) — each targeted pin fails when its branch is reverted; the 40-pin selftest is load-bearing, not decorative. (Patches re-applied cleanly to the final bytes; pin counts in the interim rows are from the pre-DONE revision.)

## 7. Residual risk and verification gaps

- **O5 outstanding:** SCORECARD/SKILL registration is the L1's landing step; until it lands, claim O's predicate is unmet. First failing leg: O5. Everything under executor scope passes.
- **Live-tree measurement:** the counter reads the working tree; any post-review byte change to the tool or drivers re-opens O-legs (kill_rule). Tool sha pinned in §0/§2.
- **Mutation control files untracked** (pin + first receipt) — committed landing is the L1's; disk bytes verified against pin and receipt here.
- **Claim C interference:** none observed — O3 needs only round-99 evidence (22 evidence dirs at run time, round-100's included, no effect), and C-leg failures (entry absent, census rc 1, reopen missing) are claim-C seats' scope, not mine.
- Corpus compare covers the 271 pre-entry knowledge files; if the claim-C entry lands later, tool-vs-ref equality on that one file is unverified by this review (out of my claim).
- Fixture expectations are mine, derived from the frozen contract text and validated against the frozen ref (ref passes all 16) — a misunderstanding shared by me and the ref would be invisible; the ref is the contract's named canonical implementation, so this is the intended baseline.
- I did not audit `mutants100.py` internals (mutation-driver quality is MutationTester100's seat; my O4 judges the live pinned score only).

## 8. Tooling authorization record

No tools installed or upgraded. No pacman, no sysctls, no model routing, no git/jj mutations. Scratch `/fast/scratch/hyaku/kotodama-r100/ReviewerO100/` deleted before yield.
