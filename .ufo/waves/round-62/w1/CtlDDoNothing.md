# CtlDDoNothing — claim D pre-data controls

Seat: `KotodamaR62.CtlDDoNothing`. Axis: **depth**. Probe-quality axes: rejection specificity, frozen-counter integrity, exact-byte restoration. No claim O work, integration, admission judgment, or counter edits.

## Scope and detector

Read `reports/round-62/claims.json`, the depth counter docstring, and `corpus/lessons/round-61-verifier-spotcheck.md` §7 before probing. All controls ran in `/fast/scratch/hyaku/kotodama-r62/CtlDDoNothing/clone`, cloned from the lane and checked out at `f0173481047a93c46798f90b68d71d4f169d2642` with `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` unset for clone/checkout.

The identical bounded detector on pristine, mutated, and restored states was:

```sh
timeout 900 python3 -B reports/round-62/accept-d.py; echo exit=$?
```

Every detector run used frozen counter SHA-256 `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4`. No PROBE counter or alternate runtime was used. All shell processes were bounded with `timeout` (at most 900 seconds); no background jobs or services were started, and every command returned before this report. Installs/updates: **none**.

Expected detector: the unchanged/records-only cases should fail SET and the unrepaired semantic/new-row legs. Whitespace-only and swapped lines can satisfy SET, but must still fail the semantic/new-row requirements. Observed results match those expectations.

## Controls and verdicts

Fixture directory: `/fast/scratch/hyaku/kotodama-r62/CtlDDoNothing/fixtures/`. Patches are relative to the pristine clone and retain the tested mutations after restoration.

| Case | Smallest mutation | SET | Legs stopping acceptance |
|---|---|---|---|
| a: unchanged | No changes | FAIL | SET OPEN HEDGE CAPTION SOLE ROWS LOCATE |
| b: records-only | Append one SCORECARD row, one LOG entry, and a lesson file; entry/SOURCES unchanged | FAIL | SET OPEN HEDGE CAPTION SOLE ROWS LOCATE |
| c1: trailing-space | Append one U+0020 to each of lines 63/74/75/93 | PASS | OPEN HEDGE CAPTION SOLE ROWS LOCATE |
| c2: double-space | Double the first internal word separator on each of the four lines; preserve bullet prefix | PASS | OPEN HEDGE CAPTION SOLE ROWS LOCATE |
| c3: NBSP | Replace that internal separator with U+00A0 on each of the four lines | PASS | OPEN HEDGE CAPTION SOLE ROWS LOCATE |
| d: swapped | Swap 63↔93 and 74↔75, including their citations | PASS | OPEN HEDGE CAPTION SOLE ROWS LOCATE |

ONEID, NOMARK, APPEND, LINK, COPY, ACCESS, and LINT passed in all cases. LINK/COPY do not reject the permutation because each original clause travels with its original citation; the line-specific semantic legs still reject it. LOCATE reports zero cited new rows, not a live-source fetch failure.

NONE-MET CtlDDoNothing/unchanged fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDoNothing/fixtures/unchanged.json smallest-counter-change=none-needed; frozen predicate rejects it.

NONE-MET CtlDDoNothing/records-only fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDoNothing/fixtures/records-only.patch smallest-counter-change=none-needed; frozen predicate rejects it.

NONE-MET CtlDDoNothing/trailing-space fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDoNothing/fixtures/trailing-space.patch smallest-counter-change=none-needed; frozen predicate rejects it.

NONE-MET CtlDDoNothing/double-space fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDoNothing/fixtures/double-space.patch smallest-counter-change=none-needed; frozen predicate rejects it.

NONE-MET CtlDDoNothing/nbsp fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDoNothing/fixtures/nbsp.patch smallest-counter-change=none-needed; frozen predicate rejects it.

NONE-MET CtlDDoNothing/swapped fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDoNothing/fixtures/swapped.patch smallest-counter-change=none-needed; frozen predicate rejects it.

Mutation-test verdict: **INCONCLUSIVE, not killed**, because the pristine baseline already fails. As pre-data negative controls, none of these fixtures obtains PASS. No contract change is proposed.

## Before / mutant / restored hashes

SHA-256, exact complete files:

| File/state | SHA-256 |
|---|---|
| Entry, pristine and every restored state | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` |
| Entry, records-only | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` |
| Entry, trailing-space | `ea7b9f053d7dee70ad4d0b3013bdeb4f5744bed47b3362aeb0f72aa4ed9f7aa0` |
| Entry, double-space | `64d8056976092511b729952501b14a7b380a37d55c3511a9d9c69f50aff6b4f8` |
| Entry, NBSP | `f6d35ec17622edcbb0d301cb1a8ceb80a596642d57e4032f1a5c577ced3e6c6a` |
| Entry, swapped | `98552fefdf6874d7e16e1a28f9a5e7b79b3a31420a3bdb71c20a65a221d173f2` |
| SOURCES, pristine / records-only / final | `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2` |
| SCORECARD, pristine / restored | `a3643cd7a3875c84298cb6e894b5cc9d1bbfaca60d975b21b252422f3d2e0da6` |
| SCORECARD, records-only | `492bb18dd23b8e151080114cd687c3bee525c2c703b2274a6b0ac842aa7bdbb6` |
| LOG, pristine / restored | `d37fd8954fafecb5bd6f9e7268d254c47edecebea0aef5481abff234f8df0056` |
| LOG, records-only | `05970e14c6c9593150b10884a366f55c12e6c2a74009e6fa3e1149f74669849b` |
| Added lesson, records-only | `a65c7e1f1358a241debb47951b077e53aa4d72cf942db560a2d6954223e8bdce` |

The added lesson was absent before the control and removed during restoration; `timeout 10 test ! -e corpus/lessons/round-62-control-do-nothing.md` succeeded before both the records-restored and final-restored detector runs. The report below includes every detector run, including each intervening restoration. A restored run is also the pristine state for the next mutation.

Tool anomaly: trailing-space-only edits changed the SHA-256 but retained the read/edit snapshot tag `C2BA`. A fresh read was taken and this was reported through `xd://report_issue`; restoration evidence uses SHA-256, not that tag.

## Full detector stdout and receipts

### a — untouched clone / pristine baseline

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:56Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDDoNothing/unchanged counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### b — records-only

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:57Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDDoNothing/records-only counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### Restored after b

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
exit=1
```

RECEIPT CtlDDoNothing/restored-records counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### c1 — trailing-space

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
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
exit=1
```

RECEIPT CtlDDoNothing/trailing-space counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### Restored after c1

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
exit=1
```

RECEIPT CtlDDoNothing/restored-trailing-space counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### c2 — double-space

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
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
exit=1
```

RECEIPT CtlDDoNothing/double-space counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### Restored after c2

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDDoNothing/restored-double-space counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### c3 — NBSP

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDDoNothing/nbsp counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### Restored after c3

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDDoNothing/restored-nbsp counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### d — swapped lines

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S687'] 74:['S666'] 75:['S665'] 93:['S692']
NOMARK PASS marked=[]
OPEN FAIL ids=['S687']
HEDGE FAIL ids=['S665']
CAPTION FAIL ids=['S666']
SOLE FAIL id=S692 tier=B
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDDoNothing/swapped counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### Restored after d / final state

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDDoNothing/restored-swapped counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

Final restoration hash-command stdout:

```text
3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4  reports/round-62/accept-d.py
eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72  corpus/knowledge/culture-material/footwear-codes-terminology.md
eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2  corpus/SOURCES.md
a3643cd7a3875c84298cb6e894b5cc9d1bbfaca60d975b21b252422f3d2e0da6  SCORECARD.md
d37fd8954fafecb5bd6f9e7268d254c47edecebea0aef5481abff234f8df0056  LOG.md
```

All changed clone files were restored byte-for-byte to their original hashes; the sole newly added clone file was removed. No lane source or counter was modified. This report is the only file written in the lane.
