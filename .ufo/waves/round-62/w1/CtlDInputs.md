# CtlDInputs — round 62 wave 1 pre-data input controls

## Scope and result

Claim axis: **depth (D)**. Probe axes: clean input rejection, dependence on the actual repairs, and exact restoration/reproducible evidence. This is a scoped control report, not claim admission or a round judgment.

All five assigned input controls returned **exit 2**, printed `ACCEPT_D_INPUT_ERROR` on stderr, printed nothing on stdout, and emitted **no traceback**. None obtained `ACCEPT-D-62: PASS`. No counter change is required for these five cases.

The pristine frozen tree and all four restored runs returned **exit 1 / ACCEPT-D-62: FAIL**. Therefore these are **not killed-mutant claims**: repair-invariant mutation verdict is **INCONCLUSIVE because the baseline fails**. The separately specified input-robustness expectations were satisfied in all five cases.

Read first: `reports/round-62/claims.json` and `corpus/lessons/round-61-verifier-spotcheck.md` section 7. Counter was never edited; no PROBE counter was needed.

## Fixtures, commands, and bounds

All scratch files are under `/fast/scratch/hyaku/kotodama-r62/CtlDInputs/`:

- `clone/`: full clone checked out at `f0173481047a93c46798f90b68d71d4f169d2642`.
- `shallow/`: true depth-one clone of that frozen full clone; `--no-local` prevents Git from ignoring `--depth 1` for a local source. `.git/shallow` contains exactly `f0173481047a93c46798f90b68d71d4f169d2642`.
- `probe.py`: bounded, reversible fixture driver.
- `primary-results.json`: every primary run's full stdout/stderr/exit and before/mutated/after hashes.
- `shallow-results.json`: shallow run's full stdout/stderr/exit and unchanged-fixture hashes.

Clone setup, with `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` unset:

```text
timeout 900 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r62/CtlDInputs/clone
timeout 60 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotodama-r62/CtlDInputs/clone checkout -q f0173481047a93c46798f90b68d71d4f169d2642
timeout 120 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q --depth 1 --no-local /fast/scratch/hyaku/kotodama-r62/CtlDInputs/clone /fast/scratch/hyaku/kotodama-r62/CtlDInputs/shallow
```

Every detector used the same frozen counter from `clone/`, with the same 60-second process-tree bound:

```text
timeout 60 python3 -B /fast/scratch/hyaku/kotodama-r62/CtlDInputs/clone/reports/round-62/accept-d.py --root ROOT
```

`ROOT` was `/fast/scratch/hyaku/kotodama-r62/CtlDInputs/clone` for every primary run and `/fast/scratch/hyaku/kotodama-r62/CtlDInputs/shallow` for the shallow control. Driver commands were bounded by 300 and 120 seconds, respectively, and ran concurrently; primary mutations were sequential because each required restoration before the next. Child Git environment variables were also unset. No new-row citations existed, so the baseline/restored LOCATE loops made no source requests.

Mutants and expected detector:

| Case | Smallest input defect | Expected |
|---|---|---|
| shallow | Missing base history in a genuine depth-one clone | exit 2 with input-error marker, or FAIL; never PASS/traceback |
| no-git | Temporarily rename only `clone/.git` outside the root | same |
| entry-missing | Temporarily rename only the footwear entry outside the root | same |
| entry-invalid-utf8 | Replace only the entry's first byte with `0xff` | same |
| locator-missing | Temporarily rename only `reports/round-61/reopen-quote.py` outside the root | same |

The driver uses `finally` to restore moved files/directories or original bytes, even when a detector raises. The shallow fixture is separately created, retained unchanged, and does not alter the full clone.

## Full detector outputs and receipts

The following are all ten detector runs. Empty streams are stated explicitly. `frozen=FAIL` on exit 2 means the frozen predicate was not satisfied; no leg or final ACCEPT label was printed on these input-error paths. Receipt `stopped-by` lists only failed legs, not the overall FAIL label.

### 1. pristine

Full stdout:

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
```

Full stderr: empty. `exit=1`.

```text
RECEIPT CtlDInputs/pristine counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```

### 2. shallow

Full stdout: empty.

Full stderr:

```text
ACCEPT_D_INPUT_ERROR Command '['git', '-C', '/fast/scratch/hyaku/kotodama-r62/CtlDInputs/shallow', 'show', 'd42ffb890a54c8431fa891380b6c38bb608b8362:corpus/knowledge/culture-material/footwear-codes-terminology.md']' returned non-zero exit status 128.
```

`exit=2`.

```text
RECEIPT CtlDInputs/shallow counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=2 stopped-by=ACCEPT_D_INPUT_ERROR(no-legs-run)
```

### 3. no-git

Full stdout: empty.

Full stderr:

```text
ACCEPT_D_INPUT_ERROR Command '['git', '-C', '/fast/scratch/hyaku/kotodama-r62/CtlDInputs/clone', 'show', 'd42ffb890a54c8431fa891380b6c38bb608b8362:corpus/knowledge/culture-material/footwear-codes-terminology.md']' returned non-zero exit status 128.
```

`exit=2`.

```text
RECEIPT CtlDInputs/no-git counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=2 stopped-by=ACCEPT_D_INPUT_ERROR(no-legs-run)
```

### 4. no-git-restored

Full stdout:

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
```

Full stderr: empty. `exit=1`.

```text
RECEIPT CtlDInputs/no-git-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```

### 5. entry-missing

Full stdout: empty.

Full stderr:

```text
ACCEPT_D_INPUT_ERROR [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotodama-r62/CtlDInputs/clone/corpus/knowledge/culture-material/footwear-codes-terminology.md'
```

`exit=2`.

```text
RECEIPT CtlDInputs/entry-missing counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=2 stopped-by=ACCEPT_D_INPUT_ERROR(no-legs-run)
```

### 6. entry-missing-restored

Full stdout:

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
```

Full stderr: empty. `exit=1`.

```text
RECEIPT CtlDInputs/entry-missing-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```

### 7. entry-invalid-utf8

Full stdout: empty.

Full stderr:

```text
ACCEPT_D_INPUT_ERROR 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
```

`exit=2`.

```text
RECEIPT CtlDInputs/entry-invalid-utf8 counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=2 stopped-by=ACCEPT_D_INPUT_ERROR(no-legs-run)
```

### 8. entry-invalid-utf8-restored

Full stdout:

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
```

Full stderr: empty. `exit=1`.

```text
RECEIPT CtlDInputs/entry-invalid-utf8-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```

### 9. locator-missing

Full stdout: empty.

Full stderr:

```text
ACCEPT_D_INPUT_ERROR [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotodama-r62/CtlDInputs/clone/reports/round-61/reopen-quote.py'
```

`exit=2`.

```text
RECEIPT CtlDInputs/locator-missing counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=2 stopped-by=ACCEPT_D_INPUT_ERROR(no-legs-run)
```

### 10. locator-missing-restored

Full stdout:

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
```

Full stderr: empty. `exit=1`.

```text
RECEIPT CtlDInputs/locator-missing-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```

## Per-item control verdicts

```text
NONE-MET CtlDInputs/shallow fixture=/fast/scratch/hyaku/kotodama-r62/CtlDInputs/shallow; clean exit-2 rejection, no bypass; smallest counter change needed: none.
NONE-MET CtlDInputs/no-git fixture=/fast/scratch/hyaku/kotodama-r62/CtlDInputs/clone (probe.py temporarily removes .git); clean exit-2 rejection, no bypass; smallest counter change needed: none.
NONE-MET CtlDInputs/entry-missing fixture=/fast/scratch/hyaku/kotodama-r62/CtlDInputs/clone (probe.py temporarily removes ENTRY); clean exit-2 rejection, no bypass; smallest counter change needed: none.
NONE-MET CtlDInputs/entry-invalid-utf8 fixture=/fast/scratch/hyaku/kotodama-r62/CtlDInputs/clone (probe.py replaces ENTRY byte 0 with ff); clean exit-2 rejection, no bypass; smallest counter change needed: none.
NONE-MET CtlDInputs/locator-missing fixture=/fast/scratch/hyaku/kotodama-r62/CtlDInputs/clone (probe.py temporarily removes LOCATOR); clean exit-2 rejection, no bypass; smallest counter change needed: none.
```

## Code dependency findings

At frozen `accept-d.py:143-155`, missing Git/base history raises `CalledProcessError`, missing entry/locator raises `OSError`, and invalid UTF-8 raises `UnicodeDecodeError`; all are caught, produce the input-error marker, and return 2 before any leg. These actual runs exercised those paths.

**Legs not requiring the claimed wording repairs to pass:**

| Leg | Code dependency | Observed baseline result / limitation |
|---|---|---|
| APPEND | `accept-d.py:228-245` reads the base/current registry only; it never examines the four repaired lines. | PASS. A strictly registry-preservation guard, independent of repaired-entry bytes. |
| ACCESS | `accept-d.py:287-288` accepts the external checker's exit status. `tools/check-source-access.py:61-91` checks registry bypass markers, rejected status, and citations to flagged rows. | PASS. No repair-wording/hedge/caption/tier check. It may scan the entry when flagged row ids exist, so it is not unconditionally independent of all entry bytes. |
| LINT | `accept-d.py:289-291` accepts the external checker's exit status. `tools/check-cited-lines.py:53-80` reads entry bytes but checks only multiple distinct ids and table-row citations. | PASS. Does not require any of the four wording repairs; strictly speaking it depends on entry shape/ids, not its truth conditions. |

Additional legs **already PASS on the unrepaired baseline**, but do directly depend on the claimed lines and should not be mislabeled byte-independent:

- ONEID (`accept-d.py:171-173`): bullet and distinct-id shape only.
- NOMARK (`175-176`): absence of defect-marker substrings only.
- LINK (`247-262`): minimum content/shared words and quote-order LCS, not the semantic scope lost by a closed list or removed hedge.
- COPY (`247-263`): maximum contiguous quote overlap only.

Thus all baseline PASS legs were `ONEID,NOMARK,APPEND,LINK,COPY,ACCESS,LINT`. None by itself establishes that a repair happened. The full predicate nevertheless rejected the base via `SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE`. No unsupported inference that ACCESS/LINT prove the four repairs is warranted.

## Restoration and hash evidence

SHA-256 before and after **every** primary mutation matched for all four tracked input/counter files and the complete Git regular-file-content manifest. The driver recorded `exact_restoration=true` for all four cases and `exact_final_restoration=true`. Here are the actual hashes:

| Object | Before | Mutated | Restored |
|---|---|---|---|
| `.git` content manifest, no-git | `0f115a23fa287f9b337be3d60980c104af942d1c31814b34dbcb4674a240a475` | ABSENT | `0f115a23fa287f9b337be3d60980c104af942d1c31814b34dbcb4674a240a475` |
| ENTRY, missing | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` | ABSENT | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` |
| ENTRY, invalid UTF-8 | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` | `f9dfc55406932f8b21f5f7d953bcfb29cd0c8b8a386465a54e2d4e2c4b851310` | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` |
| LOCATOR, missing | `39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390` | ABSENT | `39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390` |

Unchanged before/after throughout: registry SHA-256 `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`; counter SHA-256 `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4`.

The Git content manifest is SHA-256 over sorted regular files, each contributing its relative path, a NUL, its file SHA-256, and a newline. Moving `.git` preserved its bytes; writing/restoring the one-byte UTF-8 mutant preserved the original file's other bytes.

The separate shallow fixture's files matched the same four tracked file hashes. Its Git content-manifest hash stayed `5195e2df7e6007a130c70b5936f68e452a2a7f83bb8d5f1a6ef0c41c298b0460` before/after. `.git/shallow` SHA-256 was `796f08f60cce43d5ea3f246cbeb2513bee9cdd9f1b65b7b2fb288a238b3270b6`. `shallow-results.json` records `unchanged=true`.

All started processes completed in the foreground; no background jobs or services were started. No tool installations/updates. No lane source, counter, registry, or entry writes: this report is the sole lane write.
