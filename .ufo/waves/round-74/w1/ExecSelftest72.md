# ExecSelftest72 — routed defect R73-M4: `reports/round-72/accept-c.py --selftest` red at the round-73 base

Seat: ExecSelftest72 (leaf). Date: 2026-10-25. Lane base `f7104cbce186bc2e1522abf0cfd619cc834628bb`.
Counter under diagnosis: `reports/round-72/accept-c.py`, sha256 `355e67f1bdb15d52…a3c1`
(`355e67f1bdb15d52368ad454d68d8391fd72d1de596225689c4822d21da3c1`), unmodified — all runs in copies.
Nothing was written outside this report.

## Verdict

**Cause = (b) fixture defect. Not (a) stale hard-coded revisions, not (c) a real regression.**

The clean selftest fixture never writes the file the GROUND leg reads. Commit `5897ddf`
("… counter hardening (GROUND receipt path …)") re-pointed `leg_ground` from `RECEIPT`
(`.ufo/waves/round-72/assimilation/validate-receipt.txt`, which `build_fixture` writes) to
`GROUND_RECEIPT` (`reports/round-72/telemetry/gap-sweep.txt`, which only the real lane has) and
did not re-point the fixture with it. Production mode is green: the real receipt carries exactly
the tokens the leg demands, and the leg passes on real bytes at the real round-72 lands.

**A corrected successor is NOT warranted.** The round-72 counter is frozen history for round 72;
its real-mode predicate holds and its red selftest is a fixture artefact, recorded not repaired.
The class is already superseded in substance by `reports/round-73/accept-c.py`, which (i) writes
its own `GROUND_RECEIPT_TEXT` to `GROUND_RECEIPT` in the fixture (`accept-c.py:1593-1596`),
(ii) cross-checks the receipt's N-row count against the fixture's actual base registry instead of
a constant (`leg_ground`, `n != len(base_rows)`), and (iii) prints a real `legs=%d/%d`
(`accept-c.py:1204`). Measured this seat: `python3 -B reports/round-73/accept-c.py --selftest`
→ `SELFTEST: 29/29`, exit 0. What IS warranted is the lesson row below and QUALITY 23 hardening:
a fixture follows the leg's read path, and a mutant's redness must be shown against a GREEN
baseline (pre-fix, the `ground_zeros` mutant passed vacuously — see §5).

## 1. Exact red text (reproduced in an isolated copy, twice)

`/tmp/ExecSelftest72/scratch` (a scratch git repo holding only `reports/round-72/accept-c.py` +
`tools/check-cited-lines.py`; **no** registry, **no** README, **no** lane):

```
$ python3 -B reports/round-72/accept-c.py --selftest
SELFTEST: 10/11
--- clean fixture: expected PASS 10/10, got exit=1
LEG PASS ENTRIES
LEG PASS ROWS
LEG PASS REPOINTED
LEG PASS GATE
LEG PASS REJECTS
LEG FAIL GROUND
     receipt missing: reports/round-72/telemetry/gap-sweep.txt
LEG PASS CITEDLINES
LEG PASS CENSUS
     exit=0 head=<fixture> last-line=kotodama	ok	stub
LEG PASS SCRATCHMIRROR
LEG PASS COLLCHECK
ACCEPT-C-72: FAIL legs=10/10
exit=1
```

Identical output in the lane itself (`python3 -B reports/round-72/accept-c.py --selftest` from
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`, read-only run, exit 1). The single failing leg
is GROUND with one diagnostic: `receipt missing: reports/round-72/telemetry/gap-sweep.txt`.
Nine of ten legs pass; the tenth mutant misses only because the baseline it is compared against is
already red.

## 2. Root cause — the committing edit

`git show 5897ddf -- reports/round-72/accept-c.py` (the whole change):

```diff
@@ -68,6 +68,7 @@
 RECEIPT = ASSIM + "/validate-receipt.txt"
+GROUND_RECEIPT = "reports/round-72/telemetry/gap-sweep.txt"
@@ -376,11 +377,11 @@ def leg_ground(root, lands, base):
-        receipt = show(root, lands, RECEIPT)
+        receipt = show(root, lands, GROUND_RECEIPT)
     except Missing:
         receipt = ""
     if not receipt:
-        bad.append("receipt missing: %s" % RECEIPT)
+        bad.append("receipt missing: %s" % GROUND_RECEIPT)
```

`build_fixture` was not touched: it still calls `git_write(lane, RECEIPT, receipt)` and still
derives the `ground_zeros` mutant by deleting the gap-sweep line **from `RECEIPT_TEXT`** — a string
the GROUND leg no longer reads. Two consequences, both measured:

1. clean fixture: GROUND reads a path that does not exist in the fixture → `receipt missing`;
2. `ground_zeros` mutant: its mutation is dead text, so it fails GROUND for the *baseline's* reason.
   Pre-fix mutant output: `LEG FAIL GROUND` / `receipt missing: reports/round-72/telemetry/gap-sweep.txt`
   (identical to the clean baseline) — i.e. the mutant tests nothing and hides the defect.

## 3. Exclusions (the three hypotheses in the item, each measured)

| hypothesis | test | result |
|---|---|---|
| changed registry | selftest run in `/tmp/ExecSelftest72/scratch`, where `corpus/SOURCES.md` does not exist at all | same `10/11`, same GROUND receipt-missing text → registry content is not an input |
| stale base constant | `git cat-file -t b60c7b140c5350caa7d1073711f14092541533f0` → `commit`; `git show b60c7b14:corpus/SOURCES.md \| grep -cE '^\s{0,3}\|\s*S[0-9]{3,}'` → `797` | `BASE` resolves and holds the 797-row registry the leg's docstring names → constant still holds |
| README footer / lane file | same scratch copy has no `corpus/`, no README, no `.ufo/` | red persists → no lane file is an input |

Pre-hardening control: `git show a7ab3bd:reports/round-72/accept-c.py` (sha256
`27bf86ea28e85a05…ad074`) run in `/tmp/ExecSelftest72/scratch-r1` →
`SELFTEST: 11/11`, exit 0. The fixture was coherent when written; `5897ddf` broke it.

## 4. Real mode is green (rules out (c))

Two measurements:

- **Full counter on real bytes at the round-72 lands**, in a clone
  (`git clone --shared --no-checkout` + `checkout 21ad3088…`, `HEAD == lands`):
  `--lands 21ad3088cb64f7275e5541804e168f15d21d26d0 --base b60c7b14…` →
  `LEG PASS` on ENTRIES, ROWS, REPOINTED, GATE, REJECTS, **GROUND**, CITEDLINES, SCRATCHMIRROR,
  COLLCHECK; `LEG FAIL CENSUS exit=2`. The CENSUS failure is a relocation artefact, not a leg
  result: in the temp fleet the script prints
  `ERROR: config not found: /tmp/ExecSelftest72/fleet/shokunin.conf` /
  `ERROR: unknown lane (not a dir, not in conf or root): kotodama`. The real fleet's census on the
  real lane is green (read-only): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate
  --root /home/vgpnk/Projects/shokunin kotodama` → exit 0, last line
  `kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`.
- **GROUND leg alone on the real lane** (imported module, `leg_ground(real_lane, 21ad3088…, b60c7b14…)`)
  → `LEG PASS GROUND`.

Real receipt bytes at HEAD (`git show HEAD:reports/round-72/telemetry/gap-sweep.txt`, committed at
the round-72 freeze `a7ab3bd`, absent at `b60c7b14`):

```
# registry rows at base b60c7b1: 797
# ihchina matches at base: 0
# bunka.go.jp matches at base: 0
```

which satisfies all three predicates (`\b797\b`, `ihchina…0`, `bunka…0`). Consistent with the filed
`reports/round-72/telemetry/measures-c.txt` (`LEG PASS GROUND`, `ACCEPT-C-72: PASS legs=10/10` at
`21ad3088`), which I did not take on trust — see the clone run above.

## 5. Minimal diff that turns the copy green — evidence only (NOT applied to the lane)

`diff -u reports/round-72/accept-c.py <copy>` in `/tmp/ExecSelftest72/scratch`
(saved: `/tmp/ExecSelftest72/minimal-fix.diff`, fixed bytes
`/tmp/ExecSelftest72/accept-c.fixed.py`, sha256 `032c722fcb497aff…ed9999`):

```diff
@@ -668,6 +668,13 @@
 rows present in mirror: S874 S875
 """
 
+GROUND_TEXT = """\
+# gap sweep re-run at the fixture base (selftest fixture)
+# registry rows at the fixture base: 797
+ihchina matches at base: 0
+bunka matches at base: 0
+"""
+
@@ -709,11 +716,9 @@ def build_fixture(prefix, mut=None):
     receipt = RECEIPT_TEXT
     if mut.get("receipt_no_exit"):
         receipt = receipt.replace("exit 0", "exit 1")
-    if mut.get("ground_zeros"):
-        receipt = receipt.replace(
-            "gap-sweep re-run at the 797-row registry: ihchina-rows: 0 ; bunka-rows: 0\n",
-            "")
     git_write(lane, RECEIPT, receipt)
+    git_write(lane, GROUND_RECEIPT,
+              "" if mut.get("ground_zeros") else GROUND_TEXT)
```

Result: `SELFTEST: 11/11`, exit 0. The mutant is non-vacuous after the fix (its failing reason
becomes its own: an empty committed receipt reads as `receipt missing`; with the file carrying the
text minus one predicate the leg prints the predicate diagnostic — measured below).

Predicate sensitivity of the GROUND leg, probed on the patched fixture (each a distinct
`GROUND_TEXT`):

| probe receipt | leg output |
|---|---|
| `: 799` instead of `: 797` | `LEG FAIL GROUND` — `receipt does not name the 797-row registry` |
| `ihchina matches at base: 2` | `LEG FAIL GROUND` — `receipt does not show ihchina sweep 0` |
| ihchina 2 **and** bunka 3 | `LEG FAIL GROUND` — `… does not show ihchina sweep 0; … does not show bunka sweep 0` |
| `ihchina matches at base: 2 of 0` | **`LEG PASS GROUND`** (survivor — any `\b0\b` on the same line satisfies the token) |
| `: 2` (the fixture base's *true* row count) | `LEG FAIL GROUND` — `receipt does not name the 797-row registry` |

## 6. Residual weaknesses (reported, not repaired — frozen history)

1. **Fixture must lie about its own size.** The minimal fix is green only because the fixture's
   receipt names 797 while the fixture base registry holds 2 rows (last probe row above). The
   round-72 GROUND predicate is bound to the constant 797, not to the tree it grades. Round-73's
   GROUND leg binds to `len(base_rows)` and to `LEDGER_ROWS_BASE` instead.
2. **Mutant vacuity passes silently.** `EXPECTED_FAIL` is judged by `LEG FAIL <leg>` presence only,
   so a mutant that fails for the baseline's reason is indistinguishable from one that fires.
   Nothing in `run_selftest` asserts the clean fixture is green before the mutants are judged — the
   count `10/11` was the only signal, and the round-72 report/SCORECARD never filed it (R73-M4's
   capture-by-none).
3. **Static leg-count label.** `print("ACCEPT-C-72: %s legs=10/10")` is a constant: a failing run
   printed `FAIL legs=10/10` with 9 legs passing. Round-73 prints `legs=%d/%d` of actual results.

## 7. Lesson row text (for round-74 `## Mistakes`; one paragraph after the row)

```markdown
| R73-M4 successor | `reports/round-72/accept-c.py --selftest` → `SELFTEST: 10/11`, exit 1; failing diagnostic `LEG FAIL GROUND` / `receipt missing: reports/round-72/telemetry/gap-sweep.txt`. Cause is a fixture defect, not stale constants or a real regression: `5897ddf` moved `leg_ground` from `RECEIPT` to `GROUND_RECEIPT` and left `build_fixture` writing only the old path, so the clean fixture reads a file it never writes; the `ground_zeros` mutant mutates the now-unread `RECEIPT_TEXT` and passes vacuously. Real mode measured green (GROUND PASS on real bytes at lands `21ad3088`, base `b60c7b14`; real receipt names 797/ihchina 0/bunka 0; base registry 797 rows). Pre-hardening `a7ab3bd` bytes: `SELFTEST: 11/11`. Fix in a copy only (+`GROUND_TEXT` written to `GROUND_RECEIPT`, `ground_zeros` mutates it) → `11/11`; the frozen counter is not amended. Successor: none for round 72 — `reports/round-73/accept-c.py` already writes the receipt it reads, binds the row count to the fixture, and prints real leg counts (`29/29`, exercised) | none (QUALITY 19 asks for `--lands`, not a selftest receipt; no seat ran the selftest before filing `measures-c.txt`) | QUALITY 23 addendum: when a leg's read path is re-pointed, the fixture is re-pointed in the same commit, and every mutant must be shown red against a GREEN baseline. Red-before is per-mutant, not per-suite | recorded, not repaired |
```

Paragraph: A counter leg and its fixture are one object. R73-M4 is neither a stale base constant
nor a behaviour regression — the round-72 GROUND leg grades the right file in real mode (measured
PASS at lands `21ad3088`, base `b60c7b14`, real receipt naming 797/ihchina 0/bunka 0) and the
`BASE` constant still resolves to the 797-row registry; what broke is the selftest fixture, which
`5897ddf`'s re-point of `leg_ground` from the scratch-mirror receipt to the telemetry receipt left
writing only the old path, so the clean fixture reads a file it never creates and the
`ground_zeros` mutant deletes a line the leg no longer reads — passing for the baseline's failure
reason and hiding the defect behind a `10/11`. The durable rule is therefore narrower than
"counters must have selftest receipts": a re-pointed read path must land with its fixture in the
same commit, and each mutant's redness must be demonstrated against a fixture that is green first,
otherwise the mutant grades the baseline instead of the predicate. The round-72 counter stays frozen
and red as recorded; the class is already absent from `reports/round-73/accept-c.py`, whose fixture
writes the receipt its leg reads, whose row count is cross-checked against the graded tree rather
than a constant, and whose selftest prints an honest `legs=%d/%d` (`29/29`, exit 0 this seat), so no
corrected successor for the round-72 counter is warranted — only the lesson and the QUALITY 23
addendum.

## 8. Evidence inventory, scope, tooling

- Lane bytes read only: `git show`, `git log`, `git ls-tree`, `git cat-file`; the working tree was
  never modified; no lane/git-index write; the six inherited round-73 wave-2 files untouched.
- Copies (all under `/tmp/ExecSelftest72/`): `scratch/` (fixed copy + `minimal-fix.diff`,
  `accept-c.fixed.py`), `scratch-r1/` (pre-hardening `a7ab3bd` bytes), `fleet/kotodama-shokunin`
  (shared clone checked out at `21ad3088`, 167 MB) and `fleet/scripts/` (copy of the census script
  for the relocation test). No downloads, no live fetches → no User-Agent to record.
- Tool installs/upgrades: none (python3 and git only); `pacman` not run.
- Checks I did NOT run: the real lane's full counter at `--lands 21ad3088` cannot pass its CENSUS
  leg without checking the real lane out (HEAD is `f7104cb`), so CENSUS was measured via the
  relocation clone (exit 2, config-not-found) plus the real fleet census run read-only (exit 0);
  the 9 remaining legs of the real run were exercised on the clone's real bytes. No other claim in
  this report is unexercised.
