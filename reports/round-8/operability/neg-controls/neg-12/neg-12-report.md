# neg-12 — negative control + repair receipt (shard R8-O12)

- **Round:** 8 · **shard:** R8-O12 (operability) · **claim:** O
- **Date:** 2026-10-17 (all commands below; consolidated evidence run at
  `checked_at_utc = 2026-10-17T20:26:40Z`)
- **Baseline:** declared `e7ca0fa…`; worktree HEAD `cf338a7` — the pre-fix gate
  bytes are byte-identical at both revisions
  (`8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526`, the
  same hash review 26 §0 pins), so the defect and its control bind to the
  declared baseline.
- **Role:** repair shard. Writes only the repaired gate, this directory, and
  this report. No commit.
- **Defect:** review 26 §3 **D8** — packet-controlled regex can hang the naming
  gate (`tools/gates/naming-collision-gate.py`, pre-fix `:1280-1281`).

## 0. Defect selection (dependency status and index identity)

`reports/round-8/operability/defect-inventory.json` (R8-O03's artifact) did
**not exist** when this shard started (17:12–17:16 local `ls` showed only
`neg-04/`); it landed at `20:23:49Z` (file mtime) and was read before any edit
was made. Its entry for this defect:

```
idx 12 | defect_id R26-D8 | severity medium
file: tools/gates/naming-collision-gate.py
status_at_head: present_at_head
verification: {head_revision: cf338a713060f274269cdacb18cdc0085bb06aeb,
               command: "python3 /tmp/r8o03_repro.py",
               result: "redos-naming rc=TIMEOUT at the 8 s bound (no output)."}
```

**Index identity.** The dispatch phrase "defect index N" numbers review 26 §3's
register, not the inventory list position. Sibling shards' own artifacts fix
the convention: `neg-04` = D1, `neg-07` = D3, `neg-08` = D4, `neg-09` = D5,
`neg-11` = "defect index 7 = review 26 §3 D7" (its docstring states both
numbers), `neg-13` = review 29 F1. Every one matches "index N = defect D N",
so **index 8 = D8 = inventory `idx` 12**. The inventory's own `idx` 8 is D4,
which is shard R8-O08's defect and already repaired by it — recorded here
because the two numbering systems coincide for neither of us. Corroboration
that D8 was unclaimed: no other `neg-*` directory or diff hunk addressed
`re.fullmatch` before this shard's edit.

## 1. Defect and pre-fix reproduction

Review claim (26 §3 D8): `formation.pattern` is compiled with `re.fullmatch`
and only `re.error` is caught, so a pattern that compiles but backtracks
catastrophically runs unbounded — "unbounded CPU from a packet a collaborator
or another lane can author".

Reproduced at HEAD before the edit (payload in a scratch file, no repo write):

```
$ cat redos.yml            # rule pattern "^(?P<stem>(a+)+)$", stem 40*'a'+'b'
$ timeout 12 python3 tools/gates/naming-collision-gate.py redos.yml
rc=124 (124=killed by timeout => hang)          # killed at the bound, no output
```

A second, screen-invisible shape was also confirmed to hang pre-fix:
`^a*a*a*a*a*a*a*a*a*a*b$` against a 40-character *failing* subject
(`a`×40 + `c`) — killed at a 10 s bound (`rc=124`, `real 10.001s`).

Pre-fix bytes used throughout:
`git show cf338a7:tools/gates/naming-collision-gate.py` →
`sha256 8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526`
(equals the review 26 §0 pin).

## 2. Repair

`tools/gates/naming-collision-gate.py`, two layers plus a calibration note:

1. **Wall-clock match budget** (`MATCH_BUDGET_SECONDS = 0.5`,
   `_match_with_budget`): `re.fullmatch` runs under a `SIGALRM` deadline that
   raises `_MatchBudgetExceeded`; the previous handler and any pending timer
   are restored in `finally`. Where signals are unavailable (`signal.signal`
   refuses outside the main thread, or no `SIGALRM`), the call degrades to a
   plain `re.fullmatch` — a documented limit, not a silent change.
   Interruption was verified to work in this interpreter before relying on it:
   a 1 s alarm aborts the catastrophic match at `1.00s` (CPython 3.14.7).
2. **Static screen** (`_catastrophic_pattern`, `_quantifier_at`): refuses the
   two canonical catastrophic shapes — a quantified group whose body carries a
   quantifier (`(a+)+`) or an alternation (`(a|aa)+`). The scan is narrow by
   construction: it walks groups with an escape/character-class aware scanner
   and treats only `*`, `+` and open-ended `{m,}` as unbounded quantifiers, so
   bounded `{m,n}`, lookarounds and every committed fixture pattern pass.
3. Both paths emit `DERIV-HOLD` (HOLD, exit 1) naming the reason, replacing
   the pre-fix hang; `re.error` handling is unchanged.

```diff
         try:
-            match = re.fullmatch(pattern, stem)
+            if _catastrophic_pattern(pattern):
+                raise _MatchBudgetExceeded(
+                    "pattern nests a quantifier or alternation inside a quantified group "
+                    "(catastrophic backtracking shape)"
+                )
+            match = _match_with_budget(pattern, stem)
+        except _MatchBudgetExceeded as exc:
+            findings.append(
+                _finding(
+                    "DERIV-HOLD",
+                    "HOLD",
+                    f"name {record['eid']} {record['form']!r}: rule {rule_name!r} pattern is not usable: {exc}",
+                )
+            )
+            continue
         except re.error as exc:
```

plus `import signal` and the docstring bullet "Gate C matching budget" in the
Calibration section (the gate's own contract record).

**File sharing caveat.** `tools/gates/naming-collision-gate.py` is edited
concurrently by sibling O-shards (D2/D3/D4/D5/D9 repairs were landing during
this shard's run). The hunks above are this shard's; the whole-file digest
moved while receipts were taken (`e4acaf56…` at the first control run,
`bb174489…` at the re-run, `d9e4e8f4…` when this report was written). Each
receipt below names the digest observed at its run time.

## 3. Post-fix verification (command evidence)

```
$ python3 tools/gates/naming-collision-gate.py --selftest
selftest: OK — fixture findings 12 across 11 ids (CROSS-HOLD, DERIV-AFFIX,
DERIV-HOLD, DERIV-REPLAY, NAME-LEXEME, NAME-NEAR, NAME-REUSE, NAME-VISUAL,
PHON-CODA, PHON-INVENTORY, PHON-ONSET); positive control clean; malformed
inputs exit 2; missing profile held; case policy routed
selftest rc=0

$ time (timeout 20 python3 tools/gates/naming-collision-gate.py redos.yml)
FINDING DERIV-HOLD: HOLD — name N1 'x': rule 'R1' pattern is not usable:
  pattern nests a quantifier or alternation inside a quantified group
  (catastrophic backtracking shape)
rc=1                                        real 0m0.020s   # pre-fix: rc=124 at 12s

$ time (timeout 25 python3 tools/gates/naming-collision-gate.py poly.yml)
FINDING DERIV-HOLD: HOLD — name N1 'pak': rule 'R1' pattern is not usable:
  matching budget 0.5s exceeded
rc=1                                        real 0m0.520s   # pre-fix: rc=124 at 10s
```

Screen precision (in-process table, 15 cases): 5 catastrophic shapes refused,
10 legitimate patterns — including all four shapes used by the committed
fixture and both example packets — left alone; `15/15 ok`
(`screen-and-timings.txt`).

**No-harm differential** (`no-harm-differential.txt`): the pre-fix baseline
copy and the repaired gate produce **byte-identical stdout and equal exit
codes** on every real packet available:

```
### legit-pattern-twin probe      pre-fix rc=1  post-fix rc=1  stdout IDENTICAL
### tools/gates/fixtures/naming-collision-gate.yml  rc=1  rc=1  stdout IDENTICAL
### examples/culture-d2/packet.d2.yml               rc=1  rc=1  stdout IDENTICAL
### examples/culture-d3/packet.gates.yml            rc=1  rc=1  stdout IDENTICAL
```

**Battery** (round-8 O-claim requirement):

```
$ python3 tools/check-gate-battery.py --selftest
SELFTEST OK 10/10 controls behaved as expected                     rc=0
$ python3 tools/check-craft-exercise.py --selftest
SELFTEST OK 10/10 tamper cases detected; CLI-SELFTEST OK 18/18 cases passed  rc=0
$ python3 tools/check-gate-battery.py            # full seven-gate run
{"summary": {"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}}
battery rc=0        # tools/gates/fixtures tree byte-unchanged by the run
```

## 4. Negative control

`reports/round-8/operability/neg-controls/neg-12/neg-12-control.py` — stdlib
only; payloads written to `$TMPDIR`, else the system temp dir, else a
self-cleaning `.scratch` beside the control (the round-8 wave hit `/tmp` inode
exhaustion, so the fallback is exercised in practice — the pre-fix receipt
below ran from `/var/tmp`); gates run as subprocesses; no live repository path
is written. Five checks: the two canonical shapes and the screen-invisible
budget-only shape must terminate inside a 10 s wall bound with `DERIV-HOLD`
(C1–C3); a legitimate fixture-shaped derivation must still replay with no
`DERIV-*` finding (C4); a legal non-matching pattern must still be
`DERIV-REPLAY` FAIL, not HOLD (C5).

**Post-fix run (live gate, `sha256 d9e4e8f4…`, final `20:27:56Z`; the same
5/5 result was recorded at `e4acaf56…`/`bb174489…` as sibling edits landed)**
— `postfix-receipt.txt`:

```
NEG-12 nested-quantifier        rc=1  t= 0.02s ids=DERIV-HOLD,CROSS-HOLD PASS
NEG-12 quantified-alternation   rc=1  t= 0.02s ids=DERIV-HOLD,CROSS-HOLD PASS
NEG-12 budget-only-shape        rc=1  t= 0.52s ids=DERIV-HOLD,CROSS-HOLD PASS
NEG-12 legit-pattern-twin       rc=1  t= 0.02s ids=CROSS-HOLD PASS
NEG-12 legal-mismatch           rc=1  t= 0.02s ids=DERIV-REPLAY,CROSS-HOLD PASS
NEG-12 RESULT: PASS (5/5 checks)                control rc=0
```

**Pre-fix run (same control, `--pre-fix-from-git cf338a7`)** — `prefix-receipt.txt`:

```
NEG-12 note: this is the review-26 pinned PRE-FIX byte copy (8c5afb0a...)
NEG-12 nested-quantifier        rc=TIMEOUT  t=10.01s ids=- FAIL
NEG-12 quantified-alternation   rc=TIMEOUT  t=10.01s ids=- FAIL
NEG-12 budget-only-shape        rc=TIMEOUT  t=10.01s ids=- FAIL
NEG-12 legit-pattern-twin       rc=1  t= 0.02s ids=CROSS-HOLD PASS
NEG-12 legal-mismatch           rc=1  t= 0.02s ids=DERIV-REPLAY,CROSS-HOLD PASS
NEG-12 RESULT: FAIL (3/5 checks)                prefix-control rc=1
NEG-12 FAILURE: nested-quantifier: PRE-FIX PATTERN OBSERVED: the gate did not
  terminate inside the 10s wall bound (unbounded match); expected rc=1 with
  DERIV-HOLD naming the catastrophic shape within it.
```

So the control **fails on the pre-fix pattern** (exit 1, naming it) and
**passes post-fix** (exit 0, 5/5). The two positive twins pass in *both* modes,
showing the control isolates the defect rather than the gate's general
behavior.

## 5. Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
python3 reports/round-8/operability/neg-controls/neg-12/neg-12-control.py            # → exit 0
python3 reports/round-8/operability/neg-controls/neg-12/neg-12-control.py \
        --pre-fix-from-git cf338a7                                                   # → exit 1
python3 tools/gates/naming-collision-gate.py --selftest                              # → exit 0
python3 tools/check-gate-battery.py --selftest && python3 tools/check-craft-exercise.py --selftest
python3 tools/check-gate-battery.py                                                  # → exit 0, 7/7
```

## 6. Limits (untested, stated)

- **Signals unavailable** (non-POSIX, or a caller embedding `_gate_c` outside
  the main thread): only the static screen guards, so a screen-invisible
  catastrophic pattern would still run unbounded. Stated in the gate's
  docstring; not tested here because every round-8 execution path is a POSIX
  main-thread CLI.
- **Alarm clobbering**: `_match_with_budget` replaces any pre-existing
  `SIGALRM` handler/timer for the duration of one match and restores it; a
  caller with its own timer is not coordinated with. Not exercised.
- **The screen is deliberately narrow** (two shapes). The budget is the
  general guard, so shapes the screen misses are bounded on POSIX only; the
  screen's table is 15 hand-chosen cases, not a complexity proof.
- Only the file-argument CLI path was exercised; the `-` stdin path shares
  `_gate_c` and the same code by construction but was not run separately.
- **Concurrency**: the gate file carries sibling shards' edits (D2–D9
  register entries); this shard's receipts pin the digest at run time, and
  this shard did not re-verify sibling repairs.
- Review 26 D8's own recommendation "screen **or** time-bound" is satisfied
  by both layers; the ReDoS result remains a wall-bound observation, not a
  complexity proof (review 26 §5 makes the same caveat).

## 7. Acceptance-harness snapshot (observed, not authored here)

`reports/round-8/run-validation.py`'s output `reports/round-8/validation.json`
is O15/O16's artifact and moves as shards land. The snapshot read at
`20:29Z` lists for claim O exactly one remaining defect failure — `D9` (not
this shard's; its repair is visibly in flight in the same file) — so **D8 is
counted repaired with a passing control** by the harness's own
`measure_neg_controls` reading. That snapshot also carried stale
`unreadable … neg-12/.scratch/…` lines from this shard's working scratch,
which was deleted at `20:28Z`; a re-run after deletion should not reproduce
them.
