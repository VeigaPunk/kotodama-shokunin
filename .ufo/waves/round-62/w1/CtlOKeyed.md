# CtlOKeyed — claim O pre-data shortcut controls

## Scope and axes

Axis: **operability**. Probe dimensions: fixture independence, generalisation, observable request counts, and shortcut cost. No claimed-object tool was scored or changed. No counter was changed. No tool was installed. No delegation, background job, live-source fetch, git/jj lane write, integration, or shipping occurred.

Clone: `/fast/scratch/hyaku/kotodama-r62/CtlOKeyed/clone`, checked out at `f0173481047a93c46798f90b68d71d4f169d2642` with the prescribed unset git environment. All scoring used this clone's frozen `reports/round-62/accept-o.py`, SHA-256 `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551` (19,359 bytes). `--root controls/<case>` selected fake tools placed inside this clone; it did not select or alter another counter. All three mutated runs were executed concurrently as bounded synchronous subprocesses, then joined. Every scoring subprocess exited; the counter's fixture servers shut down.

Read first: round-62 claims and round-61 verifier spot-check §7; also the frozen O contract and applicable skills/operator rules.

## Result

**NONE-MET: no shortcut obtained ACCEPT-O-62: PASS.** Each passed seven legs and failed **GEN, BOUND**. **INDEP caught none**, including a tool that successfully read and loaded its parent's counter through `/proc/<ppid>/cmdline` and `/proc/<ppid>/cwd` without including a forbidden literal in its own text.

The cheapest tied result was **surface**: 3,855 source bytes; no requests at all in the mixed GEN run; correct generic argument/error handling and private refusal; real bounded requests only in the specially recognised no-explicit-retry-flags DEFAULT run. Thus “no fetching” describes its GEN shortcut, not the whole counter invocation. Its mixed fixture had 22 wrong rows. **once** did better on individual rows (four wrong) but still failed the same two legs and was larger.

Mutation-test qualification: the frozen revision has no tool, so the pristine detector failed. These are **rejected negative controls, but inconclusive mutation kills**, not killed mutants. Restoration returned the target paths to that same exact absence. No positive calibration is claimed here; the honest-reference seat was still working when inspected.

## Mutants, expected detector, and retained fixtures

All files below are retained outside the restored clone targets, under `/fast/scratch/hyaku/kotodama-r62/CtlOKeyed/fixtures/`:

| Case | Deliberate shortcut | Expected detector | Observed |
|---|---|---|---|
| `class-source/tools/reopen-row.py` | Resolve the parent Python script through procfs, `runpy.run_path` it, import `CLASSES`, then guess BODY / DEAD_ARCHIVE / DEAD using registry surface features instead of fetching. | INDEP might miss the computed dependency; random class mapping should fail GEN and actual server hits should fail BOUND. | INDEP PASS; GEN FAIL (22 wrong); BOUND FAIL (zero mixed-fixture hits). |
| `surface/tools/reopen-row.py` | Guess from quoted-span length, `Closed port page`, `capture`, `/web/2025`, and `Fixture Press`; do not fetch mixed-fixture rows. | GEN and BOUND. | INDEP PASS; GEN FAIL (22 wrong); BOUND FAIL. |
| `once/tools/reopen-row.py` | Fetch at most once per URL in the mixed fixture, parse body/caption, and fabricate retry attempts from status/verdict instead of performing retries. | GEN on transient-success cases; BOUND on skipped retries despite reported attempt counts. | INDEP PASS; GEN FAIL (4 wrong: TRANSIENT2 / TRANSIENT_PASS); BOUND FAIL. |

Each fake tool genuinely performs the default nine-request/150-second dead-row path, so DEFAULT is not the cause of rejection. For the source-reader, complete ROW output and empty stderr show that the procfs/runpy dependency succeeded rather than merely crashing.

NONE-MET class-source: retained fixture `/fast/scratch/hyaku/kotodama-r62/CtlOKeyed/fixtures/class-source/tools/reopen-row.py`; no counter change is needed to stop full acceptance (GEN and BOUND already do). An exact-fixture-only INDEP strengthening would add `runpy` to the forbidden text list; this would not establish robust independence and was not applied.

NONE-MET surface: retained fixture `/fast/scratch/hyaku/kotodama-r62/CtlOKeyed/fixtures/surface/tools/reopen-row.py`; no counter change needed (GEN and BOUND already stop it).

NONE-MET once: retained fixture `/fast/scratch/hyaku/kotodama-r62/CtlOKeyed/fixtures/once/tools/reopen-row.py`; no counter change needed (GEN and BOUND already stop it).

## Hashes and exact restoration

| Case | SHA-256 immediately before detector | SHA-256 after detector / retained fixture | Restored clone target |
|---|---|---|---|
| class-source | `daa36568a182efa364277c86412683d6486b71d84d2e92201afdba0b321b4575` | `daa36568a182efa364277c86412683d6486b71d84d2e92201afdba0b321b4575` | absent |
| surface | `4bf6959ab7e7036341a3b76e0e857b3db13b11c78606e00cd3e9d0985f7004b9` | `4bf6959ab7e7036341a3b76e0e857b3db13b11c78606e00cd3e9d0985f7004b9` | absent |
| once | `786a4fd3f0c72899c5f8ad97dcacad47f01fd9ea020c8c708ffa74aa9f38a7e9` | `786a4fd3f0c72899c5f8ad97dcacad47f01fd9ea020c8c708ffa74aa9f38a7e9` | absent |

Counter before and after all runs: `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551`.

The clone-root `tools/reopen-row.py` was absent at pristine scoring and remained absent throughout. The three `controls/<case>/tools/reopen-row.py` additions were removed after preserving identical fixtures. All three restored detectors printed `exists=False`. Absent files have no byte hash; for an explicitly labelled state marker only, SHA-256 of the bytes `ABSENT\n` is `ede4663fa9a5e8031704705268edde90aae07273f42b7b7274db7b317a40b001`. This is not presented as a file-content digest. No original tracked source bytes were modified.

## Full detector receipts

All commands below ran from the clone root. All stdout is pasted in full, including the frozen counter's own limited wrong-row detail. All mutated/restored runs had empty stderr. Raw run receipts are also retained at `/fast/scratch/hyaku/kotodama-r62/CtlOKeyed/<case>.stdout.txt` and `restored-<case>.stdout.txt`.

### Pristine baseline

Command: `timeout 900 python3 -B reports/round-62/accept-o.py` (followed by printing its exit status).

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

RECEIPT CtlOKeyed/pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=TOOL,INDEP,GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR

### class-source

Command: `timeout 840 python3 -B reports/round-62/accept-o.py --root controls/class-source`

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=22 ["TRANSIENT2:S5973:want=LOCATED/3:got=[('LOCATED', 1)]", "CAP_CLASS:S3523:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "DEAD_THEN_BODY2:S2953:want=LOCATED/4:got=[('LOCATED', 2)]", "TRANSIENT_PASS:S8338:want=LOCATED/4:got=[('LOCATED', 1)]", "ARCHIVE_CAPTION:S1959:want=CAPTION_ONLY/2:got=[('LOCATED', 2)]", "GONE:S4090:want=UNREACHABLE/1:got=[('LOCATED', 1)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['TRANSIENT2:live:want=3:hits=0', 'CAP_CLASS:live:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'TRANSIENT_PASS:live:want=4:hits=0', 'ARCHIVE_CAPTION:live:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'GONE:live:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S3648', 'REFUSED', 0), ('S9539', 'REFUSED', 0), ('S2668', 'REFUSED', 0)]
DEFAULT PASS rows=[('S6481', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlOKeyed/class-source counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND

### surface

Command: `timeout 840 python3 -B reports/round-62/accept-o.py --root controls/surface`

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=22 ["TRANSIENT_PASS:S2362:want=LOCATED/4:got=[('LOCATED', 1)]", "CAP_FIG:S6700:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_ATTR:S2191:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "DEAD:S6344:want=UNREACHABLE/9:got=[('LOCATED', 1)]", "ARCHIVE_CAPTION:S3950:want=CAPTION_ONLY/2:got=[('LOCATED', 2)]", "DEAD_THEN_BODY2:S7739:want=LOCATED/4:got=[('LOCATED', 2)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['TRANSIENT_PASS:live:want=4:hits=0', 'CAP_FIG:live:want=1:hits=0', 'CAP_ATTR:live:want=1:hits=0', 'BODY_SPLIT:live:want=1:hits=0', 'BODY_SPLIT:live:want=1:hits=0', 'DEAD:live:want=9:hits=0', 'ARCHIVE_CAPTION:live:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S7147', 'REFUSED', 0), ('S7972', 'REFUSED', 0), ('S6430', 'REFUSED', 0)]
DEFAULT PASS rows=[('S9214', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlOKeyed/surface counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND

### once

Command: `timeout 840 python3 -B reports/round-62/accept-o.py --root controls/once`

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=4 ["TRANSIENT_PASS:S9185:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "TRANSIENT2:S8950:want=LOCATED/3:got=[('UNREACHABLE', 9)]", "TRANSIENT2:S8081:want=LOCATED/3:got=[('UNREACHABLE', 9)]", "TRANSIENT_PASS:S5064:want=LOCATED/4:got=[('UNREACHABLE', 9)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD:live:want=9:hits=1', 'DEAD:live:want=9:hits=1', 'TRANSIENT_PASS:live:want=4:hits=1', 'TRANSIENT2:live:want=3:hits=1', 'TRANSIENT2:live:want=3:hits=1', 'TRANSIENT_PASS:live:want=4:hits=1', 'DEAD_THEN_BODY2:live:want=3:hits=1', 'DEAD_THEN_BODY2:live:want=3:hits=1']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S4399', 'REFUSED', 0), ('S3098', 'REFUSED', 0), ('S2134', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2739', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlOKeyed/once counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND

### restored-class-source

Command: `timeout 30 python3 -B reports/round-62/accept-o.py --root controls/class-source`

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

RECEIPT CtlOKeyed/restored-class-source counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=TOOL,INDEP,GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR

### restored-surface

Command: `timeout 30 python3 -B reports/round-62/accept-o.py --root controls/surface`

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

RECEIPT CtlOKeyed/restored-surface counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=TOOL,INDEP,GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR

### restored-once

Command: `timeout 30 python3 -B reports/round-62/accept-o.py --root controls/once`

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

RECEIPT CtlOKeyed/restored-once counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=TOOL,INDEP,GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR

## Handoff

The full frozen predicate rejected all three controls. The narrower finding is that INDEP's literal scan permits a computed import of the very counter it purports to exclude; GEN and BOUND supplied the actual rejection. Nothing here demonstrates that class-table access reveals the random per-row class mapping. No further probe or counter change was performed.
