# MutO4 — mutation test of tools/check-settlement-fixture.py (round-69 w1, operability)

Seat: MutO4 (leaf, no dispatch). Scope: mutation-test the round-69 operability
harness, then hand-re-derive its negative case. All mutations were performed on
copies under `/tmp`; the lane tree was never modified (read-only `git
rev-parse/log/diff/status` only).

## Provenance

- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (jj-colocated).
- Declared base revision `793f79746712a79f915bb481215e54bbea8b5e7a` exists
  (`git log --oneline -1` → `793f797 round-68 verifier spot-check (integrator,
  hyaku): non-author admit/reject`). Working-copy HEAD at test time:
  `6a98d7d042b6c58d2165773b1585069798111035`.
  `git diff --stat 793f797… -- tools/check-settlement-fixture.py
  tools/check-supersession-settlement.py` shows the checker byte-identical to
  the declared base and the harness ABSENT from the base (187 insertions —
  added by the round-69 instrument commits on top of it). I tested the
  working-tree bytes.
- SHA-256 (tested bytes):
  - `tools/check-supersession-settlement.py` (the counter, unmutated in lane):
    `05214b3d7618b47c7ff9c8d9127647b7b7832c0ed748b3271b0266c7f343ad74`
  - `tools/check-settlement-fixture.py` (harness, unmutated in lane):
    `f7adb4ba52e0db1a1c20ee33a5b52a0e2288b287866493ed43d800967712f7f8`
  - mutants/scratch (all in `/tmp/muto4*`):
    `mutA-drop-negative.py` `1f427d4527160270d639e02d83eb01b74cd82e3ffcbec85917eb22165c339303` ·
    `mutB-r68m1-negative-creates-file.py` `aeb12c1f2347dad9cca7841e5ccc5ed1e267e3e0eee943ba6f54f1a88b071ee2` ·
    `broken-checker.py` `00ad6c83f017986357d92709b006ea930375a15247714430a4c085380042ac79` ·
    `muto4-hand1/corpus/SOURCES.md` `0d6a43553823042a95646a67549df1398ceda534805bb4db8861d7ee334213cc` ·
    `muto4-hand2/corpus/SOURCES.md` `ef0b9382daf2205663faf2d62ec4269afe8e47b8e7c9c9235c1848c30af83ac2`

## 0. Baseline control (unmutated harness)

```
$ python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-settlement-fixture.py --selftest
PASS fixture-green rc=0 pending=0 missing_paths=0
PASS fixture-negative rc=0 pending=0 missing_paths=1
PASS fixture-pending rc=1 pending=1 missing_paths=0
FIXTURE: 3/3
rc=0
```

VERDICT: PASS (control green — the negative leg asserts `missing_paths=1` on
the absent-used-by fixture, exactly the R68-M1 class).

## 1. MutA — remove the negative case (the assigned mutation)

Copy of the harness at `/tmp/muto4/mutA-drop-negative.py`; the whole `neg`
block of `check_cases` (fixture whose used-by file is absent, plus its
`missing_paths == 1` assertion) deleted. Diff vs lane original:

```diff
-        neg = os.path.join(td, "negative")
-        write_fixture(neg, create_usedby=False, unsettled=False)
-        rc, out = run_checker(checker, neg)
-        s = parse_summary(out)
-        ok = s is not None and s["pending"] == 0 and s["missing_paths"] == 1
-        results.append(("negative", ok,
-                        "rc=%d pending=%s missing_paths=%s" % (
-                            rc, s["pending"] if s else "?",
-                            s["missing_paths"] if s else "?")))
-
```

Run (note: the mutant resolves its default checker relative to its own /tmp
location, so the lane checker is passed explicitly — same behavior either way
once overridden):

```
$ python3 -B /tmp/muto4/mutA-drop-negative.py --selftest \
    --checker /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-supersession-settlement.py
PASS fixture-green rc=0 pending=0 missing_paths=0
PASS fixture-pending rc=1 pending=1 missing_paths=0
FIXTURE: 2/2
rc=0
$ grep -n 'missing_paths..==..1' /tmp/muto4/mutA-drop-negative.py || echo "NO MATCH"
NO MATCH
```

Finding: with the negative case gone, the harness reports "all pass" AND exits
0 while the missing-used-by class is asserted nowhere. The counter could
regress to never reporting `missing_paths` at all and `--selftest` would stay
green. (mutA's `--root` mode still forwards the scanned tree's `missing_paths`
count, but that trusts the counter's own summary — it cannot detect a counter
whose detection is broken.)

VERDICT: FAIL — the mutation survives; minus the negative case the harness no
longer proves the missing-used-by class is caught.

## 2. MutB — reintroduce the R68-M1 defect (negative fixture creates the file)

Copy `/tmp/muto4/mutB-r68m1-negative-creates-file.py`; one line flipped
(`create_usedby=False` → `True` in the negative case). The harness itself
catches this:

```
$ python3 -B /tmp/muto4/mutB-r68m1-negative-creates-file.py --selftest \
    --checker /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-supersession-settlement.py
PASS fixture-green rc=0 pending=0 missing_paths=0
FAIL fixture-negative rc=0 pending=0 missing_paths=0
PASS fixture-pending rc=1 pending=1 missing_paths=0
FIXTURE: 2/3
rc=1
```

VERDICT: PASS — the negative leg is load-bearing: the moment the absent-file
precondition is broken, the harness fails (rc=1) instead of silently
degrading. This is the same defect shape as the round-68 counter fixture
(R68-M1), and the round-69 harness detects it where the round-68 battery
could not.

## 3. Kill demonstration — original harness vs MutA against a broken counter

Counter copy `/tmp/muto4/broken-checker.py` with missing-path detection
deleted (`missing_paths = []` at its line 164). Same scanned root for both
harnesses: `/tmp/muto4-hand1` (single mined row whose used-by names
`corpus/knowledge/a.md`; file absent).

```
$ python3 -B tools/check-settlement-fixture.py --root /tmp/muto4-hand1 --checker /tmp/muto4/broken-checker.py
PASS fixture-green rc=0 pending=0 missing_paths=0
FAIL fixture-negative rc=0 pending=0 missing_paths=0
PASS fixture-pending rc=1 pending=1 missing_paths=0
FIXTURE: 2/3
LANE: pending=0 missing_paths=0
rc=1

$ python3 -B /tmp/muto4/mutA-drop-negative.py --root /tmp/muto4-hand1 --checker /tmp/muto4/broken-checker.py
PASS fixture-green rc=0 pending=0 missing_paths=0
PASS fixture-pending rc=1 pending=1 missing_paths=0
FIXTURE: 2/2
LANE: pending=0 missing_paths=0
rc=0
```

Finding: the original harness kills the broken counter (negative fixture
FAILs, rc=1). MutA blesses the same broken counter with `FIXTURE: 2/2`,
`LANE: missing_paths=0`, rc=0 — on a root that genuinely has a missing
used-by path. The negative case is the only place the harness distinguishes
"counter detects the class" from "counter is blind to it".

## 4. Hand re-derivation of the negative case

Two lane-shaped fixtures built by hand under /tmp, both with the used-by file
deliberately NOT created (`ls` shows only `SOURCES.md` under `corpus/`).

Fixture 1 (`/tmp/muto4-hand1`, single mined row, no chain):

```
| S001 | Hand base source — https://example.invalid/hand-base | docs | B | the base row's scope | §1 | the base claim | mined | 2026-10-24 | 90d | corpus/knowledge/a.md |
```

```
$ python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-supersession-settlement.py --scan --root /tmp/muto4-hand1
SETTLEMENT: pending=0 chains=0 usedby_paths=1 missing_paths=1
rc=0
```

Fixture 2 (`/tmp/muto4-hand2`, exact chain shape of the harness's negative
fixture — S002 `mined` supersedes S001 `queued`, used-by file absent):

```
$ python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-supersession-settlement.py --scan --root /tmp/muto4-hand2
SETTLED-ACTIVE S002>S001 s=mined t=queued same_url=False used_by=1
SETTLEMENT: pending=0 chains=1 usedby_paths=1 missing_paths=1
rc=0
```

Question answered: **YES — `missing_paths=1` in both shapes**, single-row and
chain. The class detection lives in the counter's used-by existence walk and
is independent of chain settlement.

Finding (for accept-o's attention): in both hand runs the checker's exit code
is **0** — `--scan` gates on `pending` alone (its own docstring says so);
`missing_paths` is reported but never gates the exit. The ONLY thing that
turns this class into a hard failure is the harness's negative case
(`missing_paths == 1` assertion). One regression in that assertion, or its
deletion (MutA), and the class is enforced nowhere.

## Verdicts

- VERDICT: PASS — baseline harness selftest 3/3, rc=0 (control).
- VERDICT: FAIL — MutA (negative case removed) survives: `FIXTURE: 2/2`,
  rc=0, `missing_paths == 1` asserted nowhere; harness no longer proves the
  missing-used-by class is caught. This is the finding the round asked for.
- VERDICT: PASS — MutB (R68-M1 defect reintroduced) is caught by the harness:
  `FAIL fixture-negative`, `FIXTURE: 2/3`, rc=1; the negative leg is
  load-bearing.
- VERDICT: PASS — kill demo: original harness rc=1 vs broken counter; MutA
  rc=0 vs the same broken counter on the same root.
- VERDICT: PASS — hand re-derivation: `SETTLEMENT: pending=0 chains=0
  usedby_paths=1 missing_paths=1` (single row) and `SETTLEMENT: pending=0
  chains=1 usedby_paths=1 missing_paths=1` (chain shape); `missing_paths=1`
  reported in both.

## Notes / caveats

- Tested bytes are the working tree at HEAD `6a98d7d042b6…`, not the declared
  base `793f7974…` (the harness does not exist at the declared base; the
  checker is byte-identical to it). No git/jj state was changed by this seat.
- No external network was used; all fixtures are synthetic under `/tmp`.
- Scratch kept for reproduction: `/tmp/muto4/`, `/tmp/muto4-hand1/`,
  `/tmp/muto4-hand2/` (disposable; digests above allow re-derivation).
