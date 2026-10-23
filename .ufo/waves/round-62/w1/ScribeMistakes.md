# Round 62 W1 — ScribeMistakes

**Axis:** calibration. **Outcome:** proposed three records from the requested round-61 sweep; the pinned round-62 base does not contain `corpus/lessons/round-62.md`, so there is no existing `## Mistakes` text to quote or reconcile. These are report-only proposals, not edits to that lesson.

## Proposed rows

| id | class | evidence pointer (path:line) | captured-by | fix (failing witness below) |
|---|---|---|---|---|
| R62-M1 | Routed review defects remained unmarked in the measured entry | `corpus/lessons/round-61-verifier-spotcheck.md:114`; `corpus/knowledge/culture-material/footwear-codes-terminology.md:63,74,75,93` at `efbee29c` | No R61 acceptance leg or QUALITY 1–15 rule enforces marking a known, unresolved review defect. R61 `accept-c.py` checks cited-line shape; R62 `accept-d.py` `NOMARK` checks the repaired terminal state, not the interim state after review. | When a non-author review routes a concrete defect, mark its line until repaired; add a pre-close check that every routed S-id is marked. F1 checks the four routed lines against the marker vocabulary in R62 `accept-d.py` and fails on the R61 measured bytes. |
| R62-M2 | Round log's mistake range is stale against the closed lesson | `LOG.md:4139`; `corpus/lessons/round-61.md:108-114` | No QUALITY 1–15 criterion or tool found that reconciles a LOG mistake range with the final lesson table. | Derive the range from the final lesson table at filing and compare the two before closure; append a dated correction if later evidence adds a row. F2 reports the R61 snapshot mismatch. The available files establish the mismatch at `f0173481047a93c46798f90b68d71d4f169d2642`, but not when the LOG text was authored, so this is described as stale/mismatched, not as proven premature. |
| R62-M3 | Post-landing in-place `kind` corrections repeated the append-only violation | `corpus/lessons/round-61-verifier-spotcheck.md:70`; `corpus/lessons/round-61.md:114`; `corpus/SOURCES.md:9-12` | `SOURCES.md:9-12` prohibits this except for `status`, `recheck`, and `used-by`, and R61-M7 already records the recurrence; no QUALITY 1–15 criterion or historical mutation checker was found. This is a repeated implementation gap, not a new policy gap. | Run the vocabulary census before landing. For a post-landing correction, preserve the original row and append a superseding row. Add a history check that permits only the three listed in-place fields. F3 compares `efbee29c` with `ae8e393e` and fails on the three changed `kind` cells. |

## Failing witnesses on round-61 bytes

These are ad hoc, read-only evidence checks, not ACCEPT-D/ACCEPT-O runs and not claim receipts. Each printed the shown stdout and exited 1 as intended.

### F1 — routed lines lack a defect marker

Command:
```sh
timeout 300 python3 -B -c 'import subprocess,sys; repo="/fast/scratch/hyaku/kotodama-r62/ScribeMistakes/clone"; p=subprocess.run(["git","-C",repo,"show","efbee29c:corpus/knowledge/culture-material/footwear-codes-terminology.md"],capture_output=True,text=True,check=True,timeout=60); lines=p.stdout.splitlines(); targets=[(63,"S692"),(74,"S665"),(75,"S666"),(93,"S687")]; marks=("to-verify","overstat","unsupported","not supported","defect","[","]"); bad=[(n,sid) for n,sid in targets if not any(mark in lines[n-1].casefold() for mark in marks)]; print("UNMARKED_ROUTED_LINES: "+", ".join(f"{n} {sid}" for n,sid in bad)); sys.exit(1 if bad else 0)'
```

Output:
```text
UNMARKED_ROUTED_LINES: 63 S692, 74 S665, 75 S666, 93 S687
exit=1
```

### F2 — LOG range does not cover the lesson's seven rows

Command:
```sh
timeout 300 python3 -B -c 'import re,subprocess,sys; repo="/fast/scratch/hyaku/kotodama-r62/ScribeMistakes/clone"; rev="f0173481047a93c46798f90b68d71d4f169d2642"; show=lambda path: subprocess.run(["git","-C",repo,"show",rev+":"+path],capture_output=True,text=True,check=True,timeout=60).stdout; log=show("LOG.md"); lesson=show("corpus/lessons/round-61.md"); declared=int(re.search(r"mistakes R61-M1\.\.M(\d+)",log,re.I).group(1)); ids=[int(x) for x in re.findall(r"(?m)^\| R61-M(\d+) \|",lesson)]; actual=max(ids); print(f"MISTAKE_RANGE_MISMATCH: LOG=R61-M1..M{declared}; lesson=R61-M1..M{actual}; rows={len(ids)}"); sys.exit(1 if declared != actual else 0)'
```

Output:
```text
MISTAKE_RANGE_MISMATCH: LOG=R61-M1..M6; lesson=R61-M1..M7; rows=7
exit=1
```

### F3 — existing registry rows changed outside the allowed cells

Command:
```sh
timeout 300 python3 -B -c 'import subprocess,sys
repo="/fast/scratch/hyaku/kotodama-r62/ScribeMistakes/clone"
allowed={7,9,10}
fields=("id","source","kind","tier","scope","anchor","teaches","status","opened","recheck","used-by")
def rows(rev):
    text=subprocess.run(["git","-C",repo,"show",rev+":corpus/SOURCES.md"],capture_output=True,text=True,check=True,timeout=60).stdout
    out={}
    for line in text.splitlines():
        parts=line.split("|")
        if len(parts)>=13 and parts[1].strip().startswith("S"):
            cells=[cell.strip() for cell in parts[1:-1]]
            if len(cells)==11: out[cells[0]]=cells
    return out
old=rows("efbee29c")
new=rows("ae8e393e")
bad=[]
for sid,a in old.items():
    b=new.get(sid)
    if b is None:
        bad.append(f"{sid} row removed")
        continue
    for i,(before,after) in enumerate(zip(a,b)):
        if i not in allowed and before!=after:
            bad.append(f"{sid} {fields[i]} {before!r} -> {after!r}")
print("REGISTRY_APPEND_ONLY: "+("FAIL "+"; ".join(bad) if bad else "PASS"))
sys.exit(1 if bad else 0)'
```

Output:
```text
REGISTRY_APPEND_ONLY: FAIL S655 kind 'news' -> 'docs'; S658 kind 'news' -> 'docs'; S681 kind 'news' -> 'docs'
exit=1
```

A first F3 draft placed `def rows(rev):` after semicolon-separated statements and failed at Python parse time (`SyntaxError: invalid syntax`); it produced no data result. The multiline command above is the corrected evidence run.

## Behavior, gates, surfaces, limits

- **Behavior changed:** none. This is a records-only report; no product code, judge, counter, or lesson was edited.
- **Gates:** no acceptance counters, build, lint, or tests were run. The three negative witnesses above are the only executed checks; no install was made.
- **Touched surfaces:** read-only source inspection in the scratch clone; the only lane-repository write is this report. The clone was created with `timeout 900 mkdir -p /fast/scratch/hyaku/kotodama-r62/ScribeMistakes && timeout 900 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r62/ScribeMistakes/clone && timeout 900 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotodama-r62/ScribeMistakes/clone checkout -q f0173481047a93c46798f90b68d71d4f169d2642`. Historical comparisons use the round-61 revisions named in the spot-check (`efbee29c`, `ae8e393e`).
- **Out of scope:** writing the proposed rows into `corpus/lessons/round-62.md` (absent from the pinned base), changing QUALITY, adding a checker, or adjudicating round-62 claims.
- **Known limits:** the marker command uses R62 `accept-d.py`'s current marker strings as its operational vocabulary; it does not establish that R61 had a pre-existing marker policy. The LOG/lesson mismatch is proven at the pinned snapshot only; its authorship timing is not established. The SOURCES in-place violation is already disclosed as R61-M7 and constrained by the SOURCES append-only rule; the proposed record highlights that the prohibition lacked a historical check.
- **Artifacts:** report `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-62/w1/ScribeMistakes.md`; read-only evidence clone `/fast/scratch/hyaku/kotodama-r62/ScribeMistakes/clone`.