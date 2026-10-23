# CtlDDeadEcho — claim D LOCATE pre-data controls

## Scope and axes

Axes: rejection specificity (only LOCATE fails), measured retry wall time, and exact restoration. Four independent scratch clones were checked out at `f0173481047a93c46798f90b68d71d4f169d2642`; no lane source or counter was changed. Read claims.json, round-61 spot-check §7, godspeed skill and operator rules first. No subagents, background jobs, browser, alternate runtime, or installs were used.

## Result

All four controls are NOT_LOCATED. Each mutated fixture passes the other 13 frozen legs and prints `ACCEPT-D-62: FAIL`, exit 1. The full counter runs completed concurrently in 120.484–131.750 s each (whole batch 131.755 s), under the 900 s outer bound; no timeout fired. This establishes the measured bound for these fixtures, not a universal bound on arbitrary network responses.

The raw pristine repository also fails D, as expected before repairs. Therefore a formal killed/survived mutation classification is **INCONCLUSIVE** (baseline failure), not “killed.” The narrower control finding is conclusive: none of these four cheap sources earned PASS, and LOCATE alone stopped their otherwise passing fixtures.

## Detector and fixtures

- Frozen counter: `reports/round-62/accept-d.py`, sha256 `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4` (identical before, during and after every run).
- Frozen base locator: `reports/round-61/reopen-quote.py`, sha256 `39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390` (unchanged).
- Counter command in each clone: `timeout --kill-after=5 900 python3 -B reports/round-62/accept-d.py`.
- Locator command in each clone: `timeout --kill-after=5 900 python3 -B reports/round-61/reopen-quote.py --row S693`.
- Reproducible fixture bytes, exact unified diffs, clone paths and hashes: `/fast/scratch/hyaku/kotodama-r62/CtlDDeadEcho/fixtures.json` (case keys `dead`, `echo`, `private`, `search`). Clones have been restored; the JSON retains the mutated fixtures.
- Every raw output and timing: `/fast/scratch/hyaku/kotodama-r62/CtlDDeadEcho/runs.json`.

The shared fixture repairs exactly entry lines 63, 74, 75 and 93 and appends a syntactically valid tier-B S693 row. Its only false provenance is the source-cell location. S693 carries this 11-word synthetic quote (not admitted evidence):

> Hermes wore winged short leather boots called talaria by the Romans.

The archive URL is a deliberately fake 2099 `id_` capture of the same live target. No registry URL was reused. Baseline registry URLs and the four chosen live targets were compared before reporting.

| case | live target | direct locator result | full counter seconds |
|---|---|---|---|
| dead | `https://nonexistent-777f706c1db0.example/talaria` | NOT_LOCATED | 131.435 |
| echo | `https://httpbin.org/anything?quote=Hermes%20wore%20winged%20short%20leather%20boots%20called%20talaria%20by%20the%20Romans.` | NOT_LOCATED | 120.484 |
| private | `http://127.0.0.1:9/talaria` | NOT_LOCATED | 131.75 |
| search | `https://www.google.com/search?q=talaria` | NOT_LOCATED | 120.498 |

Expected detector: base locator refuses/unresolves the live target and cannot locate the fake capture; accept-d exhausts its three passes with two 60 s gaps, then fails LOCATE without changing the frozen predicate.

## Control receipts

```text
RECEIPT CtlDDeadEcho/dead counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=LOCATE
RECEIPT CtlDDeadEcho/echo counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=LOCATE
RECEIPT CtlDDeadEcho/private counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=LOCATE
RECEIPT CtlDDeadEcho/search counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=LOCATE
```

NONE-MET dead: fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDeadEcho/fixtures.json#cases.dead; frozen rejected only at LOCATE; smallest counter change needed=none.
NONE-MET echo: fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDeadEcho/fixtures.json#cases.echo; frozen rejected only at LOCATE; smallest counter change needed=none.
NONE-MET private: fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDeadEcho/fixtures.json#cases.private; frozen rejected only at LOCATE; smallest counter change needed=none.
NONE-MET search: fixture=/fast/scratch/hyaku/kotodama-r62/CtlDDeadEcho/fixtures.json#cases.search; frozen rejected only at LOCATE; smallest counter change needed=none.

## Full observed outputs

All stdout is pasted below without truncation. Stderr was empty for every invocation; each exit and monotonic elapsed time is recorded. Pristine and restored counters intentionally retain the pre-repair FAIL; they are not positive calibrations.

### dead

#### pristine

`timeout --kill-after=5 900 python3 -B reports/round-62/accept-d.py`

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
elapsed_s=0.518
stderr=''
```

```text
RECEIPT CtlDDeadEcho/dead-pristine counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```

#### mutated

`timeout --kill-after=5 900 python3 -B reports/round-62/accept-d.py`

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=1 at=2026-10-23T11:00Z not_located=['S693: https://nonexistent-777f706c1db0.example/talaria unresolvable-host; https://web.archive.org/web/20990101000000id_/https://nonexistent-777f706c1db0.example/talaria HTTPError (passes=3)']
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
elapsed_s=131.435
stderr=''
```

#### locator

`timeout --kill-after=5 900 python3 -B reports/round-61/reopen-quote.py --row S693`

```text
NOT_LOCATED https://nonexistent-777f706c1db0.example/talaria unresolvable-host; https://web.archive.org/web/20990101000000id_/https://nonexistent-777f706c1db0.example/talaria HTTPError
exit=1
elapsed_s=2.267
stderr=''
```

#### restored

`timeout --kill-after=5 900 python3 -B reports/round-62/accept-d.py`

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:01Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
elapsed_s=0.407
stderr=''
```

```text
RECEIPT CtlDDeadEcho/dead-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```

### echo

#### pristine

`timeout --kill-after=5 900 python3 -B reports/round-62/accept-d.py`

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
elapsed_s=0.495
stderr=''
```

```text
RECEIPT CtlDDeadEcho/echo-pristine counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```

#### mutated

`timeout --kill-after=5 900 python3 -B reports/round-62/accept-d.py`

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=1 at=2026-10-23T11:00Z not_located=['S693: https://httpbin.org/anything?quote=Hermes%20wore%20winged%20short%20leather%20boots%20called%20talaria%20by%20the%20Romans denied-host; https://web.archive.org/web/20990101000000id_/https://httpbin.org/anything?quote=Hermes%20wore%20winged%20short%20leather%20boots%20called%20talaria%20by%20the%20Romans url-reflects-quote (passes=3)']
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
elapsed_s=120.484
stderr=''
```

#### locator

`timeout --kill-after=5 900 python3 -B reports/round-61/reopen-quote.py --row S693`

```text
NOT_LOCATED https://httpbin.org/anything?quote=Hermes%20wore%20winged%20short%20leather%20boots%20called%20talaria%20by%20the%20Romans denied-host; https://web.archive.org/web/20990101000000id_/https://httpbin.org/anything?quote=Hermes%20wore%20winged%20short%20leather%20boots%20called%20talaria%20by%20the%20Romans url-reflects-quote
exit=1
elapsed_s=0.064
stderr=''
```

#### restored

`timeout --kill-after=5 900 python3 -B reports/round-62/accept-d.py`

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:01Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
elapsed_s=0.431
stderr=''
```

```text
RECEIPT CtlDDeadEcho/echo-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```

### private

#### pristine

`timeout --kill-after=5 900 python3 -B reports/round-62/accept-d.py`

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
elapsed_s=0.521
stderr=''
```

```text
RECEIPT CtlDDeadEcho/private-pristine counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```

#### mutated

`timeout --kill-after=5 900 python3 -B reports/round-62/accept-d.py`

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=1 at=2026-10-23T11:00Z not_located=['S693: http://127.0.0.1:9/talaria private-host; https://web.archive.org/web/20990101000000id_/http://127.0.0.1:9/talaria HTTPError (passes=3)']
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
elapsed_s=131.75
stderr=''
```

#### locator

`timeout --kill-after=5 900 python3 -B reports/round-61/reopen-quote.py --row S693`

```text
NOT_LOCATED http://127.0.0.1:9/talaria private-host; https://web.archive.org/web/20990101000000id_/http://127.0.0.1:9/talaria HTTPError
exit=1
elapsed_s=2.096
stderr=''
```

#### restored

`timeout --kill-after=5 900 python3 -B reports/round-62/accept-d.py`

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:01Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
elapsed_s=0.408
stderr=''
```

```text
RECEIPT CtlDDeadEcho/private-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```

### search

#### pristine

`timeout --kill-after=5 900 python3 -B reports/round-62/accept-d.py`

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
elapsed_s=0.519
stderr=''
```

```text
RECEIPT CtlDDeadEcho/search-pristine counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```

#### mutated

`timeout --kill-after=5 900 python3 -B reports/round-62/accept-d.py`

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=1 at=2026-10-23T11:00Z not_located=['S693: https://www.google.com/search?q=talaria denied-host; https://web.archive.org/web/20990101000000id_/https://www.google.com/search?q=talaria search-url (passes=3)']
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
elapsed_s=120.498
stderr=''
```

#### locator

`timeout --kill-after=5 900 python3 -B reports/round-61/reopen-quote.py --row S693`

```text
NOT_LOCATED https://www.google.com/search?q=talaria denied-host; https://web.archive.org/web/20990101000000id_/https://www.google.com/search?q=talaria search-url
exit=1
elapsed_s=0.06
stderr=''
```

#### restored

`timeout --kill-after=5 900 python3 -B reports/round-62/accept-d.py`

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:01Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
elapsed_s=0.429
stderr=''
```

```text
RECEIPT CtlDDeadEcho/search-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE
```

## Before / mutated / restored hashes

Hashes below are SHA-256. Exact byte equality (not just hash equality) was also checked against the in-memory pristine bytes after surgical restoration for both changed files, the counter and the locator in all four clones.

```text
ENTRY before=after=eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72
ENTRY mutated=1fc1560d1a95fa0bae03eef23adc42b0454f14411e4cc282a7389dab58396788
SOURCES before=after=eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2
SOURCES dead mutated=f7c7a7aef7acce27d281d7d6c7d22417da81ece500aa6c9970964f968f0005dd
SOURCES echo mutated=040372a8072ab54015cc2326a901297e0df541eb55fddb8042c2cacc588783ec
SOURCES private mutated=28a9bdecedccf6b66071c0cb26edce72973e20ace7725fe53d93dcc48b808f02
SOURCES search mutated=c18c8e07d0c69acb1dbccc754777f7cf97cd47c65408b1e5434a4862da678863
RESTORED dead {"corpus/SOURCES.md": true, "corpus/knowledge/culture-material/footwear-codes-terminology.md": true, "reports/round-61/reopen-quote.py": true, "reports/round-62/accept-d.py": true}
RESTORED echo {"corpus/SOURCES.md": true, "corpus/knowledge/culture-material/footwear-codes-terminology.md": true, "reports/round-61/reopen-quote.py": true, "reports/round-62/accept-d.py": true}
RESTORED private {"corpus/SOURCES.md": true, "corpus/knowledge/culture-material/footwear-codes-terminology.md": true, "reports/round-61/reopen-quote.py": true, "reports/round-62/accept-d.py": true}
RESTORED search {"corpus/SOURCES.md": true, "corpus/knowledge/culture-material/footwear-codes-terminology.md": true, "reports/round-61/reopen-quote.py": true, "reports/round-62/accept-d.py": true}
```

## Verdict and cleanup

**NONE-MET for all four controls. Formal mutation verdict: INCONCLUSIVE because pristine D fails; no killed-mutant claim.** No counter modification is indicated by these controls. The measured LOCATE refusal and bounded three-pass behavior are preserved.

All edited clone bytes were restored exactly even though the detectors exited 1. The four control and four locator processes, plus the four restored runs, were launched in dedicated process groups and their groups were cleaned on return; pristine and clone setup commands also completed. No process or service was left running. Only this one scoped report was written in the lane; all fixture/evidence files remain under the assigned scratch root. Tool installations/updates: none.
