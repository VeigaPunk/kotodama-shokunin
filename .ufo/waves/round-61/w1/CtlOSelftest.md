# CtlOSelftest — claim O pre-data controls

## Scope and axes

Axes: selftest authenticity; independent lint defect detection; isolated, exact-byte restoration. This is control evidence, not integration or judgment of the eventual lane tool.

Read `reports/round-61/claims.json` first. All scoring used the isolated clone at `/fast/scratch/hyaku/kotodama-r61/CtlOSelftest/clone`, checked out at `78ad4b176695e9fcd490ab607cb8218e2ce62738`. The frozen counter was never edited:

`reports/round-61/accept-o.py` SHA-256 `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`.

Every run used `timeout 900 python3 -B reports/round-61/accept-o.py` with that clone as cwd, `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` unset, and `TMPDIR=/fast/scratch/hyaku/kotodama-r61/CtlOSelftest/tmp`. No probe counter was used. All stdout below is complete; every counter stderr was empty. The receipt helper is `/fast/scratch/hyaku/kotodama-r61/CtlOSelftest/receipt.py`; per-run JSON receipts are beside it.

## Result

**TOOL does not distinguish a real selftest from a fake.** It observes only existence, exit 0, and the final `selftest N/N` line with N >= 10 (`accept-o.py:150-156`). The correct tool with no selftest fails TOOL, while the same tool with a print-only selftest passes every leg.

Thus a fake selftest **can satisfy the frozen claim-O predicate**. It cannot truthfully satisfy the substantive statement “passes its own selftest of at least 10 cases”: no cases ran. The counter does not establish that statement.

| Item | Mutant and expected detector | Actual output summary | Mutation verdict |
| --- | --- | --- | --- |
| a | Replace the real selftest with only `print("selftest 10/10"); return 0`; lint unchanged. An authenticity-enforcing TOOL would reject it. | TOOL PASS; all six legs PASS; exit 0. | **SURVIVED**, CONTROL-MET. |
| b | Remove the selftest function and its CLI dispatch; lint unchanged. Expected TOOL failure. | TOOL FAIL; all five other legs PASS; exit 1. | **KILLED** by TOOL, NONE-MET. |
| c | Use the same fake selftest and change only the MULTI-ID threshold from `len(ids) >= 2` to `len(ids) >= 3`. Expected GEN/REAL failure. | TOOL PASS; GEN misses 29 findings; REAL misses 186; exit 1. | **KILLED** by GEN and REAL, NONE-MET overall; fake selftest still passes TOOL. |

CONTROL-MET CtlOSelftest/a-fake-selftest fixture=/fast/scratch/hyaku/kotodama-r61/CtlOSelftest/a-fake-selftest.py

NONE-MET CtlOSelftest/b-no-selftest fixture=/fast/scratch/hyaku/kotodama-r61/CtlOSelftest/b-no-selftest.py

NONE-MET CtlOSelftest/c-broken-fake-selftest fixture=/fast/scratch/hyaku/kotodama-r61/CtlOSelftest/c-broken-fake-selftest.py

## Minimal honest change proposed, not applied

Choose a **statement change**, with no additional leg and no new failure mode for a correct tool. Replace “passes its own selftest of at least 10 cases” with:

> its `--selftest` command exits 0 and ends with `selftest N/N` for N >= 10 (a self-reported result; execution of N cases is not established by this predicate)

Mirror that wording in the tool-contract docstring, replacing the unverified assertion that `--selftest` “runs its own cases.” Keep the independent runtime behavior requirements and existing TOOL implementation unchanged. If the substantive case-execution claim is retained instead, its truth needs separate implementation/test review; a completion string alone is not that evidence. No formatting heuristic, tracing scheme, or extra mandatory selftest API is proposed that could reject a correct implementation accidentally.

## Fixtures, mutations, and restoration

The pristine fixture's actual selftest exercises ten input-line cases through the lint runner, plus no arguments, a missing path, invalid UTF-8, and recursive directory traversal that ignores a `.txt` file: 14 executed cases. It reports `selftest 14/14`. Its restored source remains at `/fast/scratch/hyaku/kotodama-r61/CtlOSelftest/clone/tools/check-cited-lines.py`.

Only that scratch tool was mutated. For (a), its real selftest body was replaced by the two statements above. For (b), the selftest function and the two-line `--selftest` dispatch were removed. For (c), the print-only selftest was combined with the single-character threshold mutation `2` -> `3`. Archived mutant files have exactly the hashes recorded when each was scored.

SHA-256 aliases:

- H0, pristine/restored: `6f3b3400966da7474dce983aa3bda8710cc5425ea0e59b7d8ef0cf00bdd94aa4`
- HA, fixture (a): `2bbb6367ca545fd61a5c8f8f9d2e110625e3ffbb23384d638f3e272a8327c9cd`
- HB, fixture (b): `94483fcc173b1c03e0f86ac902ed58049795ab74bb4b9569fdffce6c2e7833a3`
- HC, fixture (c): `0584a53477d2da1fa44e34173fe84576927558909197bc1f11f8288870062aa3`

| Run | Tool hash before detector | Tool hash after detector | Role |
| --- | --- | --- | --- |
| a-pristine | H0 | H0 | Pristine for a |
| a-fake-selftest | HA | HA | Mutated a |
| a-restored-b-pristine | H0 | H0 | Restored a; pristine b |
| b-no-selftest | HB | HB | Mutated b |
| b-restored-c-pristine | H0 | H0 | Restored b; pristine c |
| c-broken-fake-selftest | HC | HC | Mutated c |
| c-restored | H0 | H0 | Restored c |

The counter hash before and after **every** run was the frozen SHA-256 above. Each restoration returned the tool to exactly H0, not merely equivalent behavior. The same bounded detector passed on every pristine/restored state; no baseline failure was counted as a kill. Restored runs double as the next control's pristine run, avoiding duplicate checks.

## Full scoring receipts

### a-pristine

```text
TOOL PASS exists=True exit=0 last='selftest 14/14'
INDEP PASS exists=True
GEN PASS exit=1 want=101 got=101 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 101 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```

RECEIPT CtlOSelftest/a-pristine counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=none

### a-fake-selftest

```text
TOOL PASS exists=True exit=0 last='selftest 10/10'
INDEP PASS exists=True
GEN PASS exit=1 want=96 got=96 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 96 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```

RECEIPT CtlOSelftest/a-fake-selftest counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=none

### a-restored-b-pristine

```text
TOOL PASS exists=True exit=0 last='selftest 14/14'
INDEP PASS exists=True
GEN PASS exit=1 want=91 got=91 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 91 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```

RECEIPT CtlOSelftest/a-restored-b-pristine counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=none

### b-no-selftest

```text
TOOL FAIL exists=True exit=2 last=''
INDEP PASS exists=True
GEN PASS exit=1 want=86 got=86 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 86 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

RECEIPT CtlOSelftest/b-no-selftest counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=TOOL

### b-restored-c-pristine

```text
TOOL PASS exists=True exit=0 last='selftest 14/14'
INDEP PASS exists=True
GEN PASS exit=1 want=95 got=95 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 95 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```

RECEIPT CtlOSelftest/b-restored-c-pristine counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=none

### c-broken-fake-selftest

```text
TOOL PASS exists=True exit=0 last='selftest 10/10'
INDEP PASS exists=True
GEN FAIL exit=1 want=93 got=64 missing=29 extra=0 unparsed=0 files=4 summary=CITED-LINES: 64 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=417 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 16, 'S395,S397'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

RECEIPT CtlOSelftest/c-broken-fake-selftest counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN,REAL

### c-restored

```text
TOOL PASS exists=True exit=0 last='selftest 14/14'
INDEP PASS exists=True
GEN PASS exit=1 want=86 got=86 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 86 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```

RECEIPT CtlOSelftest/c-restored counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=none

## Bounds and evidence notes

- No counter, claimed lane tool, corpus file, or sibling source was modified. This report is the only write outside the assigned scratch directory.
- No delegation, background jobs, browser, external fetch, other agent runtime, or tool installation/update was used. All started commands completed in the foreground under explicit timeouts; no process tree remains outstanding.
- Receipt helper metadata initially included the aggregate `ACCEPT-O-61:` label among failed legs for b. Its parser and only that `stopped_by` metadata were corrected to list real legs; detector stdout, stderr, exit status, hashes, and the original run were preserved. No detector rerun was used to replace the failure.
- All fixture/report/receipt files are below 5 MB. Counter temporary files were confined to the scratch TMPDIR. No outputs were redirected into importable Python source.
