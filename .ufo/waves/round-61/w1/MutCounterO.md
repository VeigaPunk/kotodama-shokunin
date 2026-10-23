# Round 61 W1 — MutCounterO

**Result: 6/6 requested counter mutants KILLED; 0 survived; 0 inconclusive.** All six fake tools were rejected by pristine and restored frozen bytes, and accepted by their respective single-point mutants. No frozen predicate was revised.

## Axes and scope

- Operability / detector sensitivity: distinguish exact findings, counts, summary, corpus completeness, error diagnostics, and TABLE-ID reference coverage.
- Isolation / restoration: one subject per case in the assigned scratch clone; exact byte restoration, unchanged counterfeit tools, no sibling source edits.
- Cheap bounded execution: independent fixtures and scoring run in concurrent tool batches; no subagents or background jobs.

Read claims.json first and the Godspeed skill and operator rules before execution. Clone: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/clone`; checked out `78ad4b176695e9fcd490ab607cb8218e2ce62738`. Frozen accept-o SHA-256: `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`. The canonical counter was never mutated. Each subject is an initially byte-identical copy under `clone/reports/round-61/mutants/<case>/accept-o.py`; only the stated behavior-bearing point was changed.

Each fixture root contains a standalone `tools/check-cited-lines.py` plus a `.git` pointer to the isolated clone solely for the counter’s read-only base archive. No fixture imports or reads the counter. The scanner’s twelve selftests execute real comparisons, not just an echoed selftest claim. Only the requested output defect differs from the honest baseline. These are deliberately test-leg-aware cheap fakes, not proposed production implementations.

## Detector and interpretation

`/fast/scratch/hyaku/kotodama-r61/MutCounterO/run-probe.py` is the same bounded detector in all three phases. It asserts that an intentionally invalid fake is rejected with `ACCEPT-O-61: FAIL`, exit 1, and no unrelated failing legs. Therefore a raw counter FAIL is an expected negative-control result, **not a failing pristine behavioral detector**. Observed detector sequence for every case: **PASS → FAIL → PASS** (pristine → mutant → restored); observed raw counter sequence: **FAIL/1 → PASS/0 → FAIL/1**. An independent honest-tool run against the canonical frozen counter passed all six legs, exit 0. No baseline detector failed.

A mutant is KILLED because its false acceptance fails this rejection detector. A mutant-only PASS is not CONTROL-MET and is not evidence that the unchanged frozen predicate accepts the fake.

The outer driver was capped at 180 seconds; each counter process used `timeout 150` plus a 160-second subprocess deadline. The counter’s child-tool calls retain their own 300-second cap, enclosed by the counter’s shorter process-group timeout. `TMPDIR` was set inside this scratch directory; GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE were removed. The counter’s os.urandom fixtures were regenerated on every run, as frozen; no deterministic seed or counter constants were changed. All processes completed; no background process/service was started or left to terminate. No installs, updates, external fetches, other runtimes, builds, formatters, or production integration were performed.

## Summary

| Case | Frozen stopped by | Mutant result | Verdict |
|---|---|---|---|
| `gen_drop_set` | GEN | PASS / 0 | KILLED |
| `gen_count_only` | GEN | PASS / 0 | KILLED |
| `gen_skip_summary` | GEN | PASS / 0 | KILLED |
| `real_nonempty` | REAL | PASS / 0 | KILLED |
| `err_exit_only` | ERR | PASS / 0 | KILLED |
| `ignore_table` | GEN,REAL | PASS / 0 | KILLED |

The base reference contains 603 findings; the table-ignoring reference has 297 (306 TABLE-ID findings omitted). The REAL-nonempty fake returns only one finding.

## Honest canonical baseline

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/honest
```
RECEIPT MutCounterO/honest counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=none

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN PASS exit=1 want=78 got=78 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 78 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```
Counter stderr: empty. Detector PASS / exit 0.

## gen_drop_set

**Mutant:** GEN: delete only `got == want`.

**Cheap fake:** Generated-directory summary-only tool: suppresses every finding but retains the correct finding/file counts and exit 1. Other paths are handled normally.

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_drop_set/tools/check-cited-lines.py`

Fixture SHA-256 (unchanged across all phases): `e67447e348d7ffd86e30252eb6c83d5e157ce278d848d4b270ea28c986a683a7`.

Expected detector: reject this fake at the named affected leg(s); accept all unaffected behavior.

Exact single-point mutation (recorded before restoration):
```diff
--- frozen/accept-o.py
+++ gen_drop_set/accept-o.py
@@ -163,7 +163,7 @@
         want, nfiles = reference(fx, tmp)
         out = run_tool(root, [fx], tmp)
         got, bad, summary = parse(out)
-        ok = (exists and out.returncode == 1 and not bad and got == want and summary is not None
+        ok = (exists and out.returncode == 1 and not bad and summary is not None
               and int(summary.group(1)) == len(want) and int(summary.group(2)) == nfiles)
         legs.append(("GEN", ok, f"exit={out.returncode} want={len(want)} got={len(got)} missing={len(want - got)} "
                      f"extra={len(got - want)} unparsed={len(bad)} files={nfiles} summary={summary.group(0) if summary else None}"))
```

### Pristine frozen bytes

Counter SHA-256: `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/gen_drop_set/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_drop_set
```
RECEIPT MutCounterO/gen_drop_set counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN FAIL exit=1 want=78 got=0 missing=78 extra=0 unparsed=0 files=4 summary=CITED-LINES: 78 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```
Counter stderr: empty.
Rejection detector: PASS / exit 0.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/gen_drop_set.frozen.json`.

### Mutated bytes (not a frozen claim run)

Counter SHA-256: `6655407d5b1fc989aacf6dee14b8aefee82040465c4533eb7b4d33b79bcda054`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/gen_drop_set/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_drop_set
```
MUTANT-RECEIPT MutCounterO/gen_drop_set counter-sha256=6655407d5b1fc989aacf6dee14b8aefee82040465c4533eb7b4d33b79bcda054 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 mutated=PASS exit=0 stopped-by=none

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN PASS exit=1 want=87 got=0 missing=87 extra=0 unparsed=0 files=4 summary=CITED-LINES: 87 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```
Counter stderr: empty.
Rejection detector: FAIL / exit 1.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/gen_drop_set.mutant.json`.

### Exact restored bytes

Counter SHA-256: `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/gen_drop_set/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_drop_set
```
RECEIPT MutCounterO/gen_drop_set-restored counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN FAIL exit=1 want=114 got=0 missing=114 extra=0 unparsed=0 files=4 summary=CITED-LINES: 114 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```
Counter stderr: empty.
Rejection detector: PASS / exit 0.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/gen_drop_set.restored.json`.

**Verdict: KILLED.** `NONE-MET MutCounterO/gen_drop_set fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_drop_set/tools/check-cited-lines.py` — no frozen-counter PASS and no allowed FLOOR-only probe applies to O.

## gen_count_only

**Mutant:** GEN: replace `got == want` with `len(got) == len(want)`.

**Cheap fake:** Generated-directory tool shifts every reported line number by +1. Cardinality, ids, paths, summary and exit are unchanged; the finding set is entirely wrong.

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_count_only/tools/check-cited-lines.py`

Fixture SHA-256 (unchanged across all phases): `f9a8f902ae86f7b868c6cf4023b031dbaa6c829b977f6fd1020757bc9f056522`.

Expected detector: reject this fake at the named affected leg(s); accept all unaffected behavior.

Exact single-point mutation (recorded before restoration):
```diff
--- frozen/accept-o.py
+++ gen_count_only/accept-o.py
@@ -163,7 +163,7 @@
         want, nfiles = reference(fx, tmp)
         out = run_tool(root, [fx], tmp)
         got, bad, summary = parse(out)
-        ok = (exists and out.returncode == 1 and not bad and got == want and summary is not None
+        ok = (exists and out.returncode == 1 and not bad and len(got) == len(want) and summary is not None
               and int(summary.group(1)) == len(want) and int(summary.group(2)) == nfiles)
         legs.append(("GEN", ok, f"exit={out.returncode} want={len(want)} got={len(got)} missing={len(want - got)} "
                      f"extra={len(got - want)} unparsed={len(bad)} files={nfiles} summary={summary.group(0) if summary else None}"))
```

### Pristine frozen bytes

Counter SHA-256: `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/gen_count_only/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_count_only
```
RECEIPT MutCounterO/gen_count_only counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN FAIL exit=1 want=75 got=75 missing=75 extra=75 unparsed=0 files=4 summary=CITED-LINES: 75 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```
Counter stderr: empty.
Rejection detector: PASS / exit 0.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/gen_count_only.frozen.json`.

### Mutated bytes (not a frozen claim run)

Counter SHA-256: `4b602ccbd7cc53708466d5adcd849591de8bb4aa2873be9e1583d2d1180451c0`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/gen_count_only/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_count_only
```
MUTANT-RECEIPT MutCounterO/gen_count_only counter-sha256=4b602ccbd7cc53708466d5adcd849591de8bb4aa2873be9e1583d2d1180451c0 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 mutated=PASS exit=0 stopped-by=none

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN PASS exit=1 want=76 got=76 missing=76 extra=76 unparsed=0 files=4 summary=CITED-LINES: 76 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```
Counter stderr: empty.
Rejection detector: FAIL / exit 1.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/gen_count_only.mutant.json`.

### Exact restored bytes

Counter SHA-256: `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/gen_count_only/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_count_only
```
RECEIPT MutCounterO/gen_count_only-restored counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN FAIL exit=1 want=97 got=97 missing=97 extra=97 unparsed=0 files=4 summary=CITED-LINES: 97 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```
Counter stderr: empty.
Rejection detector: PASS / exit 0.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/gen_count_only.restored.json`.

**Verdict: KILLED.** `NONE-MET MutCounterO/gen_count_only fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_count_only/tools/check-cited-lines.py` — no frozen-counter PASS and no allowed FLOOR-only probe applies to O.

## gen_skip_summary

**Mutant:** GEN: remove summary presence and both summary-count checks; retain finding-set equality.

**Cheap fake:** Generated-directory tool emits the correct findings but a constant `CITED-LINES: 0 finding(s) in 0 file(s)` summary.

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_skip_summary/tools/check-cited-lines.py`

Fixture SHA-256 (unchanged across all phases): `c3d837d7908506e8412e1a08ff01e5128a1b8d8264887d35c60d59e06f1edbb4`.

Expected detector: reject this fake at the named affected leg(s); accept all unaffected behavior.

Exact single-point mutation (recorded before restoration):
```diff
--- frozen/accept-o.py
+++ gen_skip_summary/accept-o.py
@@ -163,8 +163,7 @@
         want, nfiles = reference(fx, tmp)
         out = run_tool(root, [fx], tmp)
         got, bad, summary = parse(out)
-        ok = (exists and out.returncode == 1 and not bad and got == want and summary is not None
-              and int(summary.group(1)) == len(want) and int(summary.group(2)) == nfiles)
+        ok = (exists and out.returncode == 1 and not bad and got == want)
         legs.append(("GEN", ok, f"exit={out.returncode} want={len(want)} got={len(got)} missing={len(want - got)} "
                      f"extra={len(got - want)} unparsed={len(bad)} files={nfiles} summary={summary.group(0) if summary else None}"))
         clean = os.path.join(tmp, f"{word(rng)}.md")
```

### Pristine frozen bytes

Counter SHA-256: `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/gen_skip_summary/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_skip_summary
```
RECEIPT MutCounterO/gen_skip_summary counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN FAIL exit=1 want=84 got=84 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 0 finding(s) in 0 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```
Counter stderr: empty.
Rejection detector: PASS / exit 0.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/gen_skip_summary.frozen.json`.

### Mutated bytes (not a frozen claim run)

Counter SHA-256: `35ecfd749f792e6281f2fa5e803962808706cd14640f93fe521918c24f660537`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/gen_skip_summary/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_skip_summary
```
MUTANT-RECEIPT MutCounterO/gen_skip_summary counter-sha256=35ecfd749f792e6281f2fa5e803962808706cd14640f93fe521918c24f660537 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 mutated=PASS exit=0 stopped-by=none

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN PASS exit=1 want=81 got=81 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 0 finding(s) in 0 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```
Counter stderr: empty.
Rejection detector: FAIL / exit 1.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/gen_skip_summary.mutant.json`.

### Exact restored bytes

Counter SHA-256: `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/gen_skip_summary/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_skip_summary
```
RECEIPT MutCounterO/gen_skip_summary-restored counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN FAIL exit=1 want=74 got=74 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 0 finding(s) in 0 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```
Counter stderr: empty.
Rejection detector: PASS / exit 0.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/gen_skip_summary.restored.json`.

**Verdict: KILLED.** `NONE-MET MutCounterO/gen_skip_summary fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/gen_skip_summary/tools/check-cited-lines.py` — no frozen-counter PASS and no allowed FLOOR-only probe applies to O.

## real_nonempty

**Mutant:** REAL: replace `got == want` with `bool(got)`; retain nonempty reference, R60 witness, parsing and exit checks.

**Cheap fake:** On the base corpus only, emit the first finding rather than all 603, with an accurate one-finding summary and exit 1.

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/real_nonempty/tools/check-cited-lines.py`

Fixture SHA-256 (unchanged across all phases): `0fcae29d231465e6a8849a6d8b5f6c7eb8e31349243d7e5ded15e9f9b19097c8`.

Expected detector: reject this fake at the named affected leg(s); accept all unaffected behavior.

Exact single-point mutation (recorded before restoration):
```diff
--- frozen/accept-o.py
+++ real_nonempty/accept-o.py
@@ -195,7 +195,7 @@
         got, bad, summary = parse(out)
         r60 = any(k == "MULTI-ID" and p.endswith("amulets-talismans-apotropaic-marks.md")
                   and "S612" in ids.split(",") and "S613" in ids.split(",") for k, p, _, ids in want)
-        legs.append(("REAL", exists and bool(want) and r60 and got == want and not bad and out.returncode == 1,
+        legs.append(("REAL", exists and bool(want) and r60 and bool(got) and not bad and out.returncode == 1,
                      f"exit={out.returncode} want={len(want)} got={len(got)} missing={sorted(want - got)[:3]} "
                      f"extra={sorted(got - want)[:3]} r60_line_in_reference={r60}"))
     for name, ok, detail in legs:
```

### Pristine frozen bytes

Counter SHA-256: `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/real_nonempty/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/real_nonempty
```
RECEIPT MutCounterO/real_nonempty counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=REAL

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN PASS exit=1 want=92 got=92 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 92 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=1 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 52, 'S378,S379')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```
Counter stderr: empty.
Rejection detector: PASS / exit 0.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/real_nonempty.frozen.json`.

### Mutated bytes (not a frozen claim run)

Counter SHA-256: `43d31f432ac91381e67815e4de29081f0e3f881371e6740da20adf6121b0a5ba`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/real_nonempty/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/real_nonempty
```
MUTANT-RECEIPT MutCounterO/real_nonempty counter-sha256=43d31f432ac91381e67815e4de29081f0e3f881371e6740da20adf6121b0a5ba rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 mutated=PASS exit=0 stopped-by=none

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN PASS exit=1 want=79 got=79 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 79 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=1 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 52, 'S378,S379')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```
Counter stderr: empty.
Rejection detector: FAIL / exit 1.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/real_nonempty.mutant.json`.

### Exact restored bytes

Counter SHA-256: `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/real_nonempty/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/real_nonempty
```
RECEIPT MutCounterO/real_nonempty-restored counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=REAL

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN PASS exit=1 want=103 got=103 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 103 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=1 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 52, 'S378,S379')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```
Counter stderr: empty.
Rejection detector: PASS / exit 0.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/real_nonempty.restored.json`.

**Verdict: KILLED.** `NONE-MET MutCounterO/real_nonempty fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/real_nonempty/tools/check-cited-lines.py` — no frozen-counter PASS and no allowed FLOOR-only probe applies to O.

## err_exit_only

**Mutant:** ERR: remove the stderr `CITED_LINES_ERROR` requirement; retain exit 2 for both inputs.

**Cheap fake:** For missing paths and invalid UTF-8, return 2 silently. Normal findings and real selftests remain correct.

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/err_exit_only/tools/check-cited-lines.py`

Fixture SHA-256 (unchanged across all phases): `267e18dac7a311f1988d73d0663eb6c079e84264ad7e8d53701fbae037170a42`.

Expected detector: reject this fake at the named affected leg(s); accept all unaffected behavior.

Exact single-point mutation (recorded before restoration):
```diff
--- frozen/accept-o.py
+++ err_exit_only/accept-o.py
@@ -181,7 +181,7 @@
             h.write(b"- ok S123\n- \xff\xfe broken S456 S789\n")
         e1 = run_tool(root, [os.path.join(tmp, word(rng) + "-missing.md")], tmp)
         e2 = run_tool(root, [badutf], tmp)
-        legs.append(("ERR", exists and all(e.returncode == 2 and "CITED_LINES_ERROR" in e.stderr for e in (e1, e2)),
+        legs.append(("ERR", exists and all(e.returncode == 2 for e in (e1, e2)),
                      f"missing_exit={e1.returncode} badutf8_exit={e2.returncode}"))
         real = os.path.join(tmp, "base")
         os.makedirs(real)
```

### Pristine frozen bytes

Counter SHA-256: `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/err_exit_only/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/err_exit_only
```
RECEIPT MutCounterO/err_exit_only counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=ERR

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN PASS exit=1 want=90 got=90 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 90 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR FAIL missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```
Counter stderr: empty.
Rejection detector: PASS / exit 0.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/err_exit_only.frozen.json`.

### Mutated bytes (not a frozen claim run)

Counter SHA-256: `a3e6d20d68d8c2ea2374a941f66a77111281475d3a39e46ef978ebed77ef2d50`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/err_exit_only/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/err_exit_only
```
MUTANT-RECEIPT MutCounterO/err_exit_only counter-sha256=a3e6d20d68d8c2ea2374a941f66a77111281475d3a39e46ef978ebed77ef2d50 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 mutated=PASS exit=0 stopped-by=none

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN PASS exit=1 want=104 got=104 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 104 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```
Counter stderr: empty.
Rejection detector: FAIL / exit 1.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/err_exit_only.mutant.json`.

### Exact restored bytes

Counter SHA-256: `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/err_exit_only/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/err_exit_only
```
RECEIPT MutCounterO/err_exit_only-restored counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=ERR

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN PASS exit=1 want=85 got=85 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 85 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR FAIL missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```
Counter stderr: empty.
Rejection detector: PASS / exit 0.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/err_exit_only.restored.json`.

**Verdict: KILLED.** `NONE-MET MutCounterO/err_exit_only fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/err_exit_only/tools/check-cited-lines.py` — no frozen-counter PASS and no allowed FLOOR-only probe applies to O.

## ignore_table

**Mutant:** reference(): delete the TABLE-ID branch, leaving MULTI-ID on table rows intact.

**Cheap fake:** Globally omit TABLE-ID findings, including single-ID table rows; retain MULTI-ID, proper counts for the incomplete output, and correct exits.

Fixture: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/ignore_table/tools/check-cited-lines.py`

Fixture SHA-256 (unchanged across all phases): `b6abc1cd44f0a338ba0ec65fc9f6052e19a71e506223968a6eaab267d90ed7a0`.

Expected detector: reject this fake at the named affected leg(s); accept all unaffected behavior.

Exact single-point mutation (recorded before restoration):
```diff
--- frozen/accept-o.py
+++ ignore_table/accept-o.py
@@ -64,8 +64,6 @@
                     ids = sorted(set(SID.findall(line)), key=lambda s: int(s[1:]))
                     if len(ids) >= 2:
                         found.add(("MULTI-ID", rel, n, ",".join(ids)))
-                    if ids and line.lstrip().startswith("|"):
-                        found.add(("TABLE-ID", rel, n, ",".join(ids)))
     return found, files
 
 
```

### Pristine frozen bytes

Counter SHA-256: `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/ignore_table/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/ignore_table
```
RECEIPT MutCounterO/ignore_table counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN,REAL

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN FAIL exit=1 want=92 got=48 missing=44 extra=0 unparsed=0 files=4 summary=CITED-LINES: 48 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=297 missing=[('TABLE-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 42, 'S359'), ('TABLE-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 43, 'S404'), ('TABLE-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```
Counter stderr: empty.
Rejection detector: PASS / exit 0.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/ignore_table.frozen.json`.

### Mutated bytes (not a frozen claim run)

Counter SHA-256: `1c86a62d548196627a3b5c5fe360f46da7c7fa412a4fd8f226368f02de888156`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/ignore_table/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/ignore_table
```
MUTANT-RECEIPT MutCounterO/ignore_table counter-sha256=1c86a62d548196627a3b5c5fe360f46da7c7fa412a4fd8f226368f02de888156 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 mutated=PASS exit=0 stopped-by=none

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN PASS exit=1 want=34 got=34 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 34 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=297 got=297 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```
Counter stderr: empty.
Rejection detector: FAIL / exit 1.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/ignore_table.mutant.json`.

### Exact restored bytes

Counter SHA-256: `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`.

Command (cwd isolated clone):
```sh
timeout 150 /usr/bin/python3 -B reports/round-61/mutants/ignore_table/accept-o.py --root /fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/ignore_table
```
RECEIPT MutCounterO/ignore_table-restored counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN,REAL

Full stdout and exit:
```text
TOOL PASS exists=True exit=0 last='selftest 12/12'
INDEP PASS exists=True
GEN FAIL exit=1 want=67 got=35 missing=32 extra=0 unparsed=0 files=4 summary=CITED-LINES: 35 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=297 missing=[('TABLE-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 42, 'S359'), ('TABLE-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 43, 'S404'), ('TABLE-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```
Counter stderr: empty.
Rejection detector: PASS / exit 0.
Raw record: `/fast/scratch/hyaku/kotodama-r61/MutCounterO/ignore_table.restored.json`.

**Verdict: KILLED.** `NONE-MET MutCounterO/ignore_table fixture=/fast/scratch/hyaku/kotodama-r61/MutCounterO/fixtures/ignore_table/tools/check-cited-lines.py` — no frozen-counter PASS and no allowed FLOOR-only probe applies to O.

## Restoration evidence and handoff

All six subject files were reversed with surgical edits, then scored again. Every restored subject was compared to the original source string and found byte-equal; every restored SHA-256 equals the before SHA-256 `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`. The canonical clone counter is also byte-equal to that original source and has this hash. Fixture hashes agree across all three phase records. Mutant hashes and full deltas are preserved above and in `/fast/scratch/hyaku/kotodama-r61/MutCounterO/mutation-diffs.json`.

No files in the lane were changed except this one-shot scoped report. No sibling source, shipped tool, claims, frozen counter, corpus, or fleet files were modified. Scratch fixtures and logs are retained at the paths above for reproduction. These probes test the six requested predicate weakenings only; they do not judge or certify the concurrently built production lint tool.
