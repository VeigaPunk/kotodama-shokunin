# CtlDDeleteMove — round 62 wave 1 pre-data controls
## Scope and axes
Axes: **depth** (claim D); detector discrimination; exact-byte reproducibility. Leaf mutation/control probe only: no integration, claim admission, source build, counter modification, new runtime, package install, or background job.
Read the frozen claims, round-61 verifier spot-check §7, counter docstring, and operator rules before editing. All mutations were confined to the isolated clone below; the lane receives only this report.
- Scratch: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove`
- Clone: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/clone`
- Revision: `f0173481047a93c46798f90b68d71d4f169d2642`
- Counter SHA-256: `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4` (matches the assignment).
- Detector, unchanged for pristine, each mutant, and each exact restoration: `timeout 900 python3 -B reports/round-62/accept-d.py`, run from that clone with GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE unset. Every run returned exit 1; stderr was empty.
## Result and calibration limit
**NONE-MET:** none of the six fixtures received `ACCEPT-D-62: PASS`. All six mutation verdicts are **INCONCLUSIVE**, not killed: the pristine frozen revision already fails SET, OPEN, HEDGE, CAPTION, SOLE, ROWS and LOCATE. Each restored run reproduces that failing baseline. These are observed rejection receipts, not proof of sensitivity against a passing repaired object.
Observed leg behavior: deletion/relocation/number shift fail SET; blank lines pass SET but fail ONEID; id-only bullets pass both SET and ONEID but fail LINK with zero content; reusing S688 fails SOLE. No predicate or contract change is recommended from these results.
**Assignment correction:** S688 is actually tier **B**, not tier A, in the frozen registry (corpus/SOURCES.md line 643). It is still an existing A/B row and cannot satisfy the new-row requirement. Its anchor quote names neither talaria nor Hermes, and the unchanged talaria prose also fails LINK. This probe therefore does not isolate only the reused-id branch of SOLE.
**Relocation limitation:** the appended drafts repair wording and demonstrate out-of-place text; no S693–S699 support row was invented or built. Thus this fixture is not a fully sourced positive repair relocated wholesale. Its exact appended text is shown below. SET independently rejects it based on the changed line count and unchanged target slots.
## Mutants, expected detectors and hashes
Before and restored entry hash (all six): `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`. Each restoration was compared byte-for-byte with the saved pristine bytes before running the same detector.
| Case | Mutated entry SHA-256 | Verdict |
|---|---|---|
| delete-four | `8184a4a27d7b4a624efbf4c0da98bea0cf510ec5fb375b04d85d4e079f69f428` | INCONCLUSIVE (baseline FAIL) |
| blank-four | `f8b3638b44c7add229ad5dd75c2339e9f4baee377bd2ac15b54c04a1a9a2ff14` | INCONCLUSIVE (baseline FAIL) |
| id-only-four | `38ce5155e10bacbb31664a1de72cbccd5dafc2a216fe1d8c48f68dbb02d84f3c` | INCONCLUSIVE (baseline FAIL) |
| move-repairs-to-end | `344dbbfddca55b0b5e613bb574ae077a30b354defd890d780794d57d405dba0d` | INCONCLUSIVE (baseline FAIL) |
| insert-before-63 | `54f4d6d364cd68185cda73af20821424ba170c483cd284c2a79b9ab9f8147518` | INCONCLUSIVE (baseline FAIL) |
| reuse-s688 | `7f70b9c6227b11ef3dc13760c0f0f6f25844b8f06f4c18e3e566394d35ac3bbb` | INCONCLUSIVE (baseline FAIL) |

### delete-four
- Mutant: Delete original physical lines 63, 74, 75 and 93.
- Expected detector: SET must reject the lost four lines; shifted slots may also fail ONEID.
- Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/delete-four.entry.md`
- Output: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/delete-four.stdout.txt`
NONE-MET delete-four fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/delete-four.entry.md frozen=FAIL; smallest-counter-change=none (already rejected).

### blank-four
- Mutant: Replace the four original lines with empty lines, preserving line count.
- Expected detector: ONEID must reject empty slots. SET is expected to pass because exactly the four lines changed.
- Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/blank-four.entry.md`
- Output: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/blank-four.stdout.txt`
NONE-MET blank-four fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/blank-four.entry.md frozen=FAIL; smallest-counter-change=none (already rejected).

### id-only-four
- Mutant: Replace the four original lines with - (S692), - (S665), - (S666), - (S687).
- Expected detector: The whole predicate must fail. ONEID and SET can pass by design; LINK must reject zero-content bullets.
- Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/id-only-four.entry.md`
- Output: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/id-only-four.stdout.txt`
NONE-MET id-only-four fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/id-only-four.entry.md frozen=FAIL; smallest-counter-change=none (already rejected).

### move-repairs-to-end
- Mutant: Leave every original line untouched; append four wording-repair drafts at lines 108–111. The last draft re-scopes the talaria statement to the existing S688 sandals quotation; it does not create the required new row.
- Expected detector: SET must reject append-only relocation rather than in-place repair. The original defect slots remain unrepaired.
- Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/move-repairs-to-end.entry.md`
- Output: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/move-repairs-to-end.stdout.txt`
NONE-MET move-repairs-to-end fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/move-repairs-to-end.entry.md frozen=FAIL; smallest-counter-change=none (already rejected).

### insert-before-63
- Mutant: Insert one empty line immediately before original line 63; leave all original bytes in their relative order.
- Expected detector: SET must reject changed line count and shifted physical positions.
- Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/insert-before-63.entry.md`
- Output: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/insert-before-63.stdout.txt`
NONE-MET insert-before-63 fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/insert-before-63.entry.md frozen=FAIL; smallest-counter-change=none (already rejected).

### reuse-s688
- Mutant: Change only line 93 citation from S687 to existing S688; preserve its original prose.
- Expected detector: SOLE must reject an old row outside S693–S699. LINK also rejects this quotation/prose mismatch.
- Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/reuse-s688.entry.md`
- Output: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/reuse-s688.stdout.txt`
NONE-MET reuse-s688 fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/reuse-s688.entry.md frozen=FAIL; smallest-counter-change=none (already rejected).

Appended relocation drafts (not a new-row source build):
```markdown
- A sabot is hollowed from a wooden block; traditional wearers include farmers and workers in the Netherlands, France, Belgium, etc. (S692)
- Bata's caption says the heel originated in Western Asia centuries ago for riding on horseback. (S665)
- The BBC article cites a 10th-century Persian bowl as the earliest evidence we have of someone wearing heels. (S666)
- Mercury's artistic sandals carry wings fastened on each side over the ankles. (S688)
```

## Complete frozen receipts
Full stdout and exit code for every run follow, in execution order. No counter was edited and no PROBE counter exists. The initial pristine stdout was copied verbatim from its tool result; the other twelve outputs were captured directly. Machine-readable copy: `/fast/scratch/hyaku/kotodama-r62/CtlDDeleteMove/receipts.json`.

### pristine
RECEIPT CtlDDeleteMove/pristine counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
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

### delete-four
RECEIPT CtlDDeleteMove/delete-four counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,ONEID,OPEN,HEDGE,CAPTION,SOLE,ROWS,LINK,COPY,LOCATE
```text
SET FAIL lines=104 base=108 differ=[63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83]
ONEID FAIL 63:['S678'] 74:['S676'] 75:['S677'] 93:[]
NOMARK PASS marked=[]
OPEN FAIL ids=['S678']
HEDGE FAIL ids=['S677']
CAPTION FAIL ids=['S676']
SOLE FAIL id=- tier=-
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK FAIL bad=['93:ids']
COPY FAIL bad=['93:ids']
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:57Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

### restored-delete-four
RECEIPT CtlDDeleteMove/restored-delete-four counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
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

### blank-four
RECEIPT CtlDDeleteMove/blank-four counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=ONEID,OPEN,HEDGE,CAPTION,SOLE,ROWS,LINK,COPY,LOCATE
```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID FAIL 63:[] 74:[] 75:[] 93:[]
NOMARK PASS marked=[]
OPEN FAIL ids=[]
HEDGE FAIL ids=[]
CAPTION FAIL ids=[]
SOLE FAIL id=- tier=-
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK FAIL bad=['63:ids', '74:ids', '75:ids', '93:ids']
COPY FAIL bad=['63:ids', '74:ids', '75:ids', '93:ids']
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:57Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

### restored-blank-four
RECEIPT CtlDDeleteMove/restored-blank-four counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
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

### id-only-four
RECEIPT CtlDDeleteMove/id-only-four counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LINK,LOCATE
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
LINK FAIL bad=['63:content=0 shared=0 order=0/4', '74:content=0 shared=0 order=0/4', '75:content=0 shared=0 order=0/4', '93:content=0 shared=0 order=0/4']
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:57Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

### restored-id-only-four
RECEIPT CtlDDeleteMove/restored-id-only-four counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
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

### move-repairs-to-end
RECEIPT CtlDDeleteMove/move-repairs-to-end counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```text
SET FAIL lines=112 base=108 differ=[108]
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

### restored-move-repairs-to-end
RECEIPT CtlDDeleteMove/restored-move-repairs-to-end counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
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

### insert-before-63
RECEIPT CtlDDeleteMove/insert-before-63 counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,ONEID,OPEN,HEDGE,CAPTION,SOLE,ROWS,LINK,COPY,LOCATE
```text
SET FAIL lines=109 base=108 differ=[63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82]
ONEID FAIL 63:[] 74:['S664'] 75:['S665'] 93:[]
NOMARK PASS marked=[]
OPEN FAIL ids=[]
HEDGE FAIL ids=['S665']
CAPTION FAIL ids=['S664']
SOLE FAIL id=- tier=-
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK FAIL bad=['63:ids', '93:ids']
COPY FAIL bad=['63:ids', '93:ids']
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

### restored-insert-before-63
RECEIPT CtlDDeleteMove/restored-insert-before-63 counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
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

### reuse-s688
RECEIPT CtlDDeleteMove/reuse-s688 counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LINK,LOCATE
```text
SET FAIL lines=108 base=108 differ=[93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S688']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S688 tier=B
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK FAIL bad=['93:content=5 shared=0 order=0/4']
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

### restored-reuse-s688
RECEIPT CtlDDeleteMove/restored-reuse-s688 counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
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

## Restoration and bounds
- The entry was restored after every mutation, before the next fixture. All six byte comparisons succeeded; the final restored detector exited 1 with the same baseline legs failing.
| File | Before SHA-256 | Final SHA-256 | Exact bytes |
|---|---|---|---|
| Entry | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` | yes |
| Frozen counter | `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4` | `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4` | yes |
| Registry | `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2` | `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2` | yes |
- Registry and counter were checked against their saved original bytes on every detector run; neither was edited. No new source rows and no live quote fetches were requested by these fixtures (cited_new was empty throughout). ACCESS and LINT ran only because the frozen counter invokes them.
- All started clone/checkout/hash/detector processes were synchronous, bounded at 900 seconds or less, and completed. No service, background job, or child process tree was left running.
- Every retained artifact is under the scratch root above and below 5 MB. No tools were installed or updated. No git/jj write command ran in the lane or fleet repo.
- No main-agent checks are requested for this closed probe. A passing-object mutation calibration was not performed and is not claimed.
