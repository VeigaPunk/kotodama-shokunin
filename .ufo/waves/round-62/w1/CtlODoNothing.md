# Claim O — do-nothing pre-data controls

Seat: `KotodamaR62.CtlODoNothing`

Axes: operability; frozen-detector discrimination; complete receipts; scratch containment and exact restoration.

## Scope and detector

Read `reports/round-62/claims.json`, section 7 of `corpus/lessons/round-61-verifier-spotcheck.md`, the frozen O counter's contract and scoring code, `skill://godspeed`, and the operator's tooling rules before probing. No installs or updates were needed.

All controls ran in the isolated clone `/fast/scratch/hyaku/kotodama-r62/CtlODoNothing/clone`, checked out at `f0173481047a93c46798f90b68d71d4f169d2642`. The counter was never edited or copied into a probe variant. Its SHA-256 before the baseline, before each present-tool run, and after restoration was:

`bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551`

Frozen predicate: **ACCEPT-O-62: every leg above prints PASS.**

Each detector invocation used the clone as cwd and this bounded command, with no `--root` override:

```sh
timeout 900 env TMPDIR=/fast/scratch/hyaku/kotodama-r62/CtlODoNothing/tmp PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-62/accept-o.py
```

The shell recorded its actual status with `rc=$?; printf 'exit=%s\n' "$rc"`. Hash commands were separately bounded at 20 seconds. All invocations completed synchronously; no background jobs were launched. The counter's local HTTP fixture and temporary tool copies remained under this seat's scratch tree; no external fetch was used.

Expected detector: the missing tool fails TOOL and all dependent legs; each present do-nothing file passes only TOOL and INDEP, then fails the behavioral legs. Expected final label `ACCEPT-O-62: FAIL`, exit 1, for every case.

## Findings

| Case | Legs passing | Legs failing | Frozen result |
|---|---|---|---|
| No tool (pristine) | None | TOOL INDEP GEN ORDER BOUND EXIT PRIV DEFAULT ERR | FAIL, exit 1 |
| Empty file | TOOL INDEP | GEN ORDER BOUND EXIT PRIV DEFAULT ERR | FAIL, exit 1 |
| Silent exit 0 | TOOL INDEP | GEN ORDER BOUND EXIT PRIV DEFAULT ERR | FAIL, exit 1 |
| `REOPEN: 0/0 located`, exit 0 | TOOL INDEP | GEN ORDER BOUND EXIT PRIV DEFAULT ERR | FAIL, exit 1 |
| Echo arguments | TOOL INDEP | GEN ORDER BOUND EXIT PRIV DEFAULT ERR | FAIL, exit 1 |
| No tool (restored) | None | TOOL INDEP GEN ORDER BOUND EXIT PRIV DEFAULT ERR | FAIL, exit 1 |

TOOL and INDEP provide no capability evidence for these controls: TOOL is only a file-existence check; INDEP passes vacuously because empty or trivial source text contains none of the forbidden strings. Missing-tool INDEP does **not** pass: the counter explicitly marks it FAIL. The present controls print zero valid ROW lines, make zero fixture requests, and exit 0 even on the five invalid-input cases. Thus the compound EXIT and PRIV legs fail even though some individual subconditions (all-body exit 0; no private-host requests) are satisfied.

**Mutation verdict: INCONCLUSIVE as a mutant-kill experiment**, because the pristine missing-tool baseline already fails. **Negative-control verdict: all five rejected; NONE-MET.** These results are not reported as killed mutants and do not establish positive calibration of an honest tool.

## Retained fixtures and hashes

Only the scratch clone's `tools/reopen-row.py` slot was changed. The four retained fixture files are under `/fast/scratch/hyaku/kotodama-r62/CtlODoNothing/fixtures/`:

| Fixture | Exact behavior / bytes | SHA-256 |
|---|---|---|
| `empty.py` | 0 bytes | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `silent-zero.py` | `raise SystemExit(0)` plus newline; 20 bytes | `0e0e7eaed7cbb486356c6101499ffe3dfbb88d49e884aaa1d604f970fb8c214c` |
| `zero-summary.py` | Prints the fixed zero summary, then `raise SystemExit(0)`; 49 bytes | `125bd4feb28d398ff821165dbccdb806cfc64b29dfdcce537a0b813cb977a086` |
| `echo-args.py` | Imports sys and prints space-joined `sys.argv[1:]`; 42 bytes | `353e4864bb94d29ee96f080ee52f96074c19e430a82b602cc517461eab33ea75` |

Each installed tool hash matched its retained fixture. The no-tool fixture is the absent slot `/fast/scratch/hyaku/kotodama-r62/CtlODoNothing/clone/tools/reopen-row.py`, both pristine and restored. An absent file has no byte hash; it is not conflated with the empty-file SHA-256. The counter's before/after byte hashes match exactly as recorded above.

## Full run outputs and receipts

These are the full stdout outputs of the six run commands, including their hash/state preambles where present and the shell's recorded exit status. No output was trimmed by this report. The frozen counter itself prints only selected mismatch examples, as its code specifies.

### 1. Pristine / no tool

Initial identity command output:

```text
f0173481047a93c46798f90b68d71d4f169d2642
bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  /fast/scratch/hyaku/kotodama-r62/CtlODoNothing/clone/reports/round-62/accept-o.py
tool-state=ABSENT
```

Detector run:

```text
TOOL FAIL path=tools/reopen-row.py exists=False
INDEP FAIL no tool
GEN FAIL no tool
ORDER FAIL no tool
BOUND FAIL no tool
EXIT FAIL no tool
PRIV FAIL no tool
DEFAULT FAIL no tool
ERR FAIL no tool
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlODoNothing/no-tool counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=TOOL,INDEP,GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR

NONE-MET no-tool — the absent clone tool is rejected. No counter change is needed; TOOL already stops it.

### 2. Empty file

```text
bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  reports/round-62/accept-o.py
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  tools/reopen-row.py
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=37 ['ARCHIVE_CAPTION:S7946:want=CAPTION_ONLY/2:got=[]', 'ARCHIVE_CAPTION:S2474:want=CAPTION_ONLY/2:got=[]', 'PLAIN:S9899:want=LOCATED/1:got=[]', 'NOQUOTE:S8409:want=NO_QUOTE/0:got=[]', 'CAP_FIG:S4778:want=CAPTION_ONLY/1:got=[]', 'TRANSIENT_PASS:S4233:want=LOCATED/4:got=[]'] summary_ok=False exit=0
ORDER FAIL printed=0 expected=37
BOUND FAIL bad=['ARCHIVE_CAPTION:live:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'ARCHIVE_CAPTION:live:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'PLAIN:live:want=1:hits=0', 'CAP_FIG:live:want=1:hits=0', 'TRANSIENT_PASS:live:want=4:hits=0', 'CAP_FIG:live:want=1:hits=0']
EXIT FAIL gen_exit=0 body_exit=0
PRIV FAIL exit=0 rows=[]
DEFAULT FAIL rows=[] wall=0s hits=0 exit=0
ERR FAIL bad=['no-id:exit=0', 'missing:exit=0', 'badutf8:exit=0', 'passes0:exit=0', 'gapx:exit=0']
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlODoNothing/empty counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR

NONE-MET empty — fixture `fixtures/empty.py` is rejected. No counter change is needed; GEN already stops it.

### 3. Silent exit 0

```text
bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  reports/round-62/accept-o.py
0e0e7eaed7cbb486356c6101499ffe3dfbb88d49e884aaa1d604f970fb8c214c  tools/reopen-row.py
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=37 ['BODY:S5715:want=LOCATED/1:got=[]', 'CAP_FIG:S7259:want=CAPTION_ONLY/1:got=[]', 'GONE:S1521:want=UNREACHABLE/1:got=[]', 'CAP_ATTR:S8280:want=CAPTION_ONLY/1:got=[]', 'PLAIN:S4973:want=LOCATED/1:got=[]', 'DEAD:S8962:want=UNREACHABLE/9:got=[]'] summary_ok=False exit=0
ORDER FAIL printed=0 expected=37
BOUND FAIL bad=['BODY:live:want=1:hits=0', 'CAP_FIG:live:want=1:hits=0', 'GONE:live:want=1:hits=0', 'CAP_ATTR:live:want=1:hits=0', 'PLAIN:live:want=1:hits=0', 'DEAD:live:want=9:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_THEN_BODY2:arch:want=1:hits=0']
EXIT FAIL gen_exit=0 body_exit=0
PRIV FAIL exit=0 rows=[]
DEFAULT FAIL rows=[] wall=0s hits=0 exit=0
ERR FAIL bad=['no-id:exit=0', 'missing:exit=0', 'badutf8:exit=0', 'passes0:exit=0', 'gapx:exit=0']
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlODoNothing/silent-zero counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR

NONE-MET silent-zero — fixture `fixtures/silent-zero.py` is rejected. No counter change is needed; GEN already stops it.

### 4. Fixed zero summary, exit 0

```text
bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  reports/round-62/accept-o.py
125bd4feb28d398ff821165dbccdb806cfc64b29dfdcce537a0b813cb977a086  tools/reopen-row.py
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=37 ['BODY_SPLIT:S5568:want=LOCATED/1:got=[]', 'DEAD:S6904:want=UNREACHABLE/9:got=[]', 'ABSENT:S5118:want=ABSENT/1:got=[]', 'CAP_FIG:S2003:want=CAPTION_ONLY/1:got=[]', 'DEAD_ARCHIVE:S2163:want=LOCATED/2:got=[]', 'ARCHIVE_CAPTION:S5842:want=CAPTION_ONLY/2:got=[]'] summary_ok=False exit=0
ORDER FAIL printed=0 expected=37
BOUND FAIL bad=['BODY_SPLIT:live:want=1:hits=0', 'DEAD:live:want=9:hits=0', 'ABSENT:live:want=1:hits=0', 'CAP_FIG:live:want=1:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'ARCHIVE_CAPTION:live:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0']
EXIT FAIL gen_exit=0 body_exit=0
PRIV FAIL exit=0 rows=[]
DEFAULT FAIL rows=[] wall=0s hits=0 exit=0
ERR FAIL bad=['no-id:exit=0', 'missing:exit=0', 'badutf8:exit=0', 'passes0:exit=0', 'gapx:exit=0']
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlODoNothing/zero-summary counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR

NONE-MET zero-summary — fixture `fixtures/zero-summary.py` is rejected. No counter change is needed; GEN already stops it, including the incorrect summary.

### 5. Echo arguments

```text
bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  reports/round-62/accept-o.py
353e4864bb94d29ee96f080ee52f96074c19e430a82b602cc517461eab33ea75  tools/reopen-row.py
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=37 ['CAP_CLASS:S8535:want=CAPTION_ONLY/1:got=[]', 'CAP_ATTR:S9100:want=CAPTION_ONLY/1:got=[]', 'DEAD_THEN_BODY2:S4641:want=LOCATED/4:got=[]', 'SHORT:S2119:want=NO_QUOTE/0:got=[]', 'BODY_SPLIT:S7116:want=LOCATED/1:got=[]', 'DEAD:S5645:want=UNREACHABLE/9:got=[]'] summary_ok=False exit=0
ORDER FAIL printed=0 expected=37
BOUND FAIL bad=['CAP_CLASS:live:want=1:hits=0', 'CAP_ATTR:live:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'BODY_SPLIT:live:want=1:hits=0', 'DEAD:live:want=9:hits=0', 'BODY:live:want=1:hits=0', 'SCRIPT:live:want=1:hits=0']
EXIT FAIL gen_exit=0 body_exit=0
PRIV FAIL exit=0 rows=[]
DEFAULT FAIL rows=[] wall=0s hits=0 exit=0
ERR FAIL bad=['no-id:exit=0', 'missing:exit=0', 'badutf8:exit=0', 'passes0:exit=0', 'gapx:exit=0']
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlODoNothing/echo-args counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR

NONE-MET echo-args — fixture `fixtures/echo-args.py` is rejected. No counter change is needed; GEN already stops it.

### 6. Restored / no tool

The scratch tool was removed after the last control, restoring the original absent state before this final run.

```text
bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  reports/round-62/accept-o.py
tool-state=ABSENT
TOOL FAIL path=tools/reopen-row.py exists=False
INDEP FAIL no tool
GEN FAIL no tool
ORDER FAIL no tool
BOUND FAIL no tool
EXIT FAIL no tool
PRIV FAIL no tool
DEFAULT FAIL no tool
ERR FAIL no tool
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlODoNothing/restored-no-tool counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=TOOL,INDEP,GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR

## Restoration and bounds

- Original tool state: absent. Final tool state: absent, shown both by the explicit state check and the restored detector's TOOL failure.
- Counter SHA-256: identical before and after; no counter edits, probe counters, or contract changes.
- Retained fixtures remain only in this seat's scratch tree; only this report was written in the lane.
- No sibling source, fleet files, live lane tool, git/jj state in the lane, or host services were changed.
- No additional checks, live-page runs, integrations, or tool installations were performed.
