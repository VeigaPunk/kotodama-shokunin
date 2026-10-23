# CtlOHonest — claim O pre-data control + honest positive calibration (round 61, wave 1)

Lane revision: `78ad4b176695e9fcd490ab607cb8218e2ce62738` (clone at
`/fast/scratch/hyaku/kotodama-r61/KotodamaR61.CtlOHonest/clone`; lane itself untouched except this report).
Instrument: `reports/round-61/accept-o.py`, sha256
`1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd` (identical in lane and clone; matches the
frozen counter named in the assignment and claims.json). Probe: **n/a** — `accept-o.py` has no `FLOOR`-like
constant and the assignment's probe rule allows changing only `accept-c.py`'s `FLOOR`/`TOTAL`, so every frozen
run below is the unmodified counter.
No tools were installed or updated. No background jobs or process trees were started; every run is bounded by
`timeout 300` (driver bounded at 900).

## What was done

1. Built an **independent, straightforward correct implementation** of the `accept-o.py` docstring contract at
   `/fast/scratch/hyaku/kotodama-r61/KotodamaR61.CtlOHonest/clone/tools/check-cited-lines.py`
   (sha256 `0be03b85c437e632a5f6103eb7a83bc13d30693286a66adc2b5052b9311715d8`, saved at
   `.../KotodamaR61.CtlOHonest/honest-tool.py`). This is the calibration control, **not** the tool to land; it
   exists only in my clone. It does not name `reports/` or `accept-o` anywhere (`grep -c` = 0 for both), reads
   UTF-8 strictly, walks directory arguments for `*.md`, prints `MULTI-ID`/`TABLE-ID` in numeric-id order, prints
   both findings when a table line carries two ids, counts every scanned `.md` file in the summary, and exits
   2 with a `CITED_LINES_ERROR` stderr line for no PATH / missing PATH / unreadable or non-UTF-8 file. Its
   selftest runs **15 real cases** (clean, single, repeated-id, lookalike ids, comma pair, `and` pair, numeric
   sort, table-one, table-multi, line numbers, directory walk skipping `.txt`, empty directory, missing path,
   invalid UTF-8, no path): `python3 -B tools/check-cited-lines.py --selftest` → `selftest 15/15`, exit 0.
2. Ran `accept-o.py` on it **5 times** (batch A, interactive; batch B, canonical driver run). All 10 runs PASS
   every leg; no counter defect found, so no fix is needed before data.
3. Built 12 cheap fixtures against the nine `claims.json` `O` control items, and scored every one with the
   frozen counter. Full stdout and exit code for every run are pasted below, never trimmed.
4. Driver/fixtures: `/fast/scratch/hyaku/kotodama-r61/KotodamaR61.CtlOHonest/run_controls.py` (regenerates each
   fixture deterministically from the honest source), sources under `.../fixtures/`, per-run records under
   `.../runs/`, base corpus export under `.../base/`.

## Base reference census (driver instrumentation, not counter output)

The honest tool (which passed REAL 5/5) run on the exported base `corpus/knowledge`:

```
BASE findings=603 files-summary='CITED-LINES: 603 finding(s) in 235 file(s)' separator-stats:
base multi=297 table=306
base separators between ids: {'comma': 41, 'and': 246, 'slash': 18, 'dash': 81, 'space': 0, 'other': 242}
```

So REAL is non-empty and separator-diverse; the R60-M6 amulets line is present (REAL leg detail below).

## Receipts

Format: `RECEIPT <case> counter-sha256=… rev=… frozen=<counter verdict> exit=<n> probe=n/a stopped-by=<FAIL legs>`.

```
RECEIPT KotodamaR61.CtlOHonest/honest-run-1 counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=-
RECEIPT KotodamaR61.CtlOHonest/honest-run-2 counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=-
RECEIPT KotodamaR61.CtlOHonest/honest-run-3 counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=-
RECEIPT KotodamaR61.CtlOHonest/honest-run-4 counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=-
RECEIPT KotodamaR61.CtlOHonest/honest-run-5 counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=-
RECEIPT KotodamaR61.CtlOHonest/do-nothing counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=TOOL,INDEP,GEN,CLEAN,ERR,REAL
RECEIPT KotodamaR61.CtlOHonest/always-exit-0 counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN,CLEAN,ERR,REAL
RECEIPT KotodamaR61.CtlOHonest/flag-every-line counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN,CLEAN,ERR,REAL
RECEIPT KotodamaR61.CtlOHonest/keyed-base-list counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN,CLEAN
RECEIPT KotodamaR61.CtlOHonest/ignores-separators-1 counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=TOOL,GEN,REAL
RECEIPT KotodamaR61.CtlOHonest/ignores-separators-2 counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=TOOL,GEN,REAL
RECEIPT KotodamaR61.CtlOHonest/ignores-separators-3 counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=TOOL,GEN,REAL
RECEIPT KotodamaR61.CtlOHonest/ignores-table-rows counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=TOOL,GEN,REAL
RECEIPT KotodamaR61.CtlOHonest/fake-selftest counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=-
RECEIPT KotodamaR61.CtlOHonest/imports-reference-literal counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=INDEP
RECEIPT KotodamaR61.CtlOHonest/imports-reference-obfuscated counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=-
RECEIPT KotodamaR61.CtlOHonest/wrong-exit-bad-input counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=TOOL,ERR
```

## Calibration batch A — five runs, before any fixture (all PASS)

Implementation sha `0be03b85…15d8`. Command: `cd …/clone && timeout 300 python3 -B reports/round-61/accept-o.py`.

```
===== honest-run-1 =====
TOOL PASS exists=True exit=0 last='selftest 15/15'
INDEP PASS exists=True
GEN PASS exit=1 want=90 got=90 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 90 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
===== honest-run-2 =====
TOOL PASS exists=True exit=0 last='selftest 15/15'
INDEP PASS exists=True
GEN PASS exit=1 want=89 got=89 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 89 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
===== honest-run-3 =====
TOOL PASS exists=True exit=0 last='selftest 15/15'
INDEP PASS exists=True
GEN PASS exit=1 want=90 got=90 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 90 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
===== honest-run-4 =====
TOOL PASS exists=True exit=0 last='selftest 15/15'
INDEP PASS exists=True
GEN PASS exit=1 want=80 got=80 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 80 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
===== honest-run-5 =====
TOOL PASS exists=True exit=0 last='selftest 15/15'
INDEP PASS exists=True
GEN PASS exit=1 want=86 got=86 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 86 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```

## Calibration batch B — canonical driver run, five more runs (all PASS)

Same implementation sha. Full stdout:

```
===== honest-run-1 =====
TOOL PASS exists=True exit=0 last='selftest 15/15'
INDEP PASS exists=True
GEN PASS exit=1 want=86 got=86 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 86 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
===== honest-run-2 =====
TOOL PASS exists=True exit=0 last='selftest 15/15'
INDEP PASS exists=True
GEN PASS exit=1 want=91 got=91 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 91 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
===== honest-run-3 =====
TOOL PASS exists=True exit=0 last='selftest 15/15'
INDEP PASS exists=True
GEN PASS exit=1 want=78 got=78 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 78 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
===== honest-run-4 =====
TOOL PASS exists=True exit=0 last='selftest 15/15'
INDEP PASS exists=True
GEN PASS exit=1 want=96 got=96 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 96 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
===== honest-run-5 =====
TOOL PASS exists=True exit=0 last='selftest 15/15'
INDEP PASS exists=True
GEN PASS exit=1 want=81 got=81 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 81 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```

**Honest-positive result: 10/10 PASS.** GEN counts move every run (90/89/90/80/86, 86/91/78/96/81), so the
os.urandom fixture is genuinely live; REAL is stable at 603/603 with the R60 line present. No leg ever FAILed on
the honest implementation, therefore there is **no counter defect to fix before data** on this axis. Causes that
were checked and did not occur as defects: path normalisation (relative dir arg `fx` printed as `fx/...`, matching
`reference()`'s `normpath(join(root_arg, relpath))`), file ordering (set comparison, no order dependence), summary
wording (exact `CITED-LINES: k finding(s) in m file(s)`, files = all scanned `.md`), CRLF/BOM (not exercised by the
counter; my tool uses `splitlines()` and strict UTF-8 like the reference), trailing newline (fixture always writes
one; irrelevant to `splitlines()`).

## Fixtures and full counter output

Inventory (source sha256 is the fixture tool actually run):

| case | fixture path | tool sha256 | frozen |
|---|---|---|---|
| do-nothing | (no tool file) | — | FAIL |
| always-exit-0 | `…/fixtures/always-exit-0.py` | `092496bf…864e04` | FAIL |
| flag-every-line | `…/fixtures/flag-every-line.py` | `eaff87e2…8050d8` | FAIL |
| keyed-base-list | `…/fixtures/keyed-base-list.py` | `868a3360…f75a81` | FAIL |
| ignores-separators 1–3 | `…/fixtures/ignores-separators-1.py` | `102a9078…e4ed8dd` | FAIL |
| ignores-table-rows | `…/fixtures/ignores-table-rows.py` | `f550ef56…52efce` | FAIL |
| fake-selftest | `…/fixtures/fake-selftest.py` | `afc77bee…15ecd68` | **PASS** |
| imports-reference-literal | `…/fixtures/imports-reference-literal.py` | `5adb682c…57ba36` | FAIL |
| imports-reference-obfuscated | `…/fixtures/imports-reference-obfuscated.py` | `c77271cc…8db3b96` | **PASS** |
| wrong-exit-bad-input | `…/fixtures/wrong-exit-bad-input.py` | `82fce3c2…29fc9` | FAIL |

All mutating fixtures keep the honest selftest (or a 10-assertion selftest of their own hardcoded list for
`keyed-base-list`) so the TOOL leg is not the target unless the mutation breaks the selftest.

### do-nothing (no tool)

```
TOOL FAIL exists=False exit=None last=''
INDEP FAIL exists=False
GEN FAIL exit=2 want=93 got=0 missing=93 extra=0 unparsed=0 files=4 summary=None
CLEAN FAIL exit=2 findings=0 summary=None
ERR FAIL missing_exit=2 badutf8_exit=2
REAL FAIL exit=2 want=603 got=0 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 16, 'S395,S397'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

Note: with the file absent, the interpreter itself exits 2 on the missing script, so the ERR detail printed
`missing_exit=2 badutf8_exit=2`; the leg still FAILs because that stderr is Python's `can't open file`, not
`CITED_LINES_ERROR`. Verdict is correct; only the detail string is misleading.

### always-exit-0

```
TOOL PASS exists=True exit=0 last='selftest 10/10'
INDEP PASS exists=True
GEN FAIL exit=0 want=81 got=0 missing=81 extra=0 unparsed=0 files=4 summary=CITED-LINES: 0 finding(s) in 0 file(s)
CLEAN FAIL exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 0 file(s)
ERR FAIL missing_exit=0 badutf8_exit=0
REAL FAIL exit=0 want=603 got=0 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 16, 'S395,S397'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

### flag-every-line

```
TOOL PASS exists=True exit=0 last='selftest 10/10'
INDEP PASS exists=True
GEN FAIL exit=1 want=106 got=196 missing=106 extra=196 unparsed=0 files=4 summary=CITED-LINES: 196 finding(s) in 4 file(s)
CLEAN FAIL exit=1 findings=60 summary=CITED-LINES: 60 finding(s) in 1 file(s)
ERR FAIL missing_exit=2 badutf8_exit=1
REAL FAIL exit=1 want=603 got=34958 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 16, 'S395,S397'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382')] extra=[('MULTI-ID', 'corpus/knowledge/civilizations/aegean-minoan-mycenaean.md', 1, 'S100'), ('MULTI-ID', 'corpus/knowledge/civilizations/aegean-minoan-mycenaean.md', 3, 'S100'), ('MULTI-ID', 'corpus/knowledge/civilizations/aegean-minoan-mycenaean.md', 4, 'S100')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

### keyed-base-list (hardcodes the 603 base findings; correct input-error handling)

```
TOOL PASS exists=True exit=0 last='selftest 10/10'
INDEP PASS exists=True
GEN FAIL exit=1 want=93 got=603 missing=93 extra=603 unparsed=0 files=4 summary=CITED-LINES: 603 finding(s) in 1 file(s)
CLEAN FAIL exit=1 findings=603 summary=CITED-LINES: 603 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

REAL alone is fooled (expected: it is keyed to that corpus); GEN's random tree is what stops it. Also note REAL
does not verify the summary (it accepted `603 finding(s) in 1 file(s)`; the true file count is 235).

### ignores-separators 1/2/3 (multi only when a literal `", "` sits on the line)

```
TOOL FAIL exists=True exit=1 last='selftest 10/15'
INDEP PASS exists=True
GEN FAIL exit=1 want=85 got=38 missing=47 extra=0 unparsed=0 files=4 summary=CITED-LINES: 38 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=585 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 109, 'S372,S373,S412'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 111, 'S374,S386,S387'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 115, 'S362,S393,S401')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

```
TOOL FAIL exists=True exit=1 last='selftest 10/15'
INDEP PASS exists=True
GEN FAIL exit=1 want=72 got=44 missing=28 extra=0 unparsed=0 files=4 summary=CITED-LINES: 44 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=585 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 109, 'S372,S373,S412'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 111, 'S374,S386,S387'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 115, 'S362,S393,S401')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

```
TOOL FAIL exists=True exit=1 last='selftest 10/15'
INDEP PASS exists=True
GEN FAIL exit=1 want=88 got=50 missing=38 extra=0 unparsed=0 files=4 summary=CITED-LINES: 50 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=585 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 109, 'S372,S373,S412'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 111, 'S374,S386,S387'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 115, 'S362,S393,S401')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

3/3 runs fail on GEN and on REAL (base separator census above: only 41 of 588 inter-id separators are comma).

### ignores-table-rows (never prints TABLE-ID)

```
TOOL FAIL exists=True exit=1 last='selftest 11/15'
INDEP PASS exists=True
GEN FAIL exit=1 want=88 got=42 missing=46 extra=0 unparsed=0 files=4 summary=CITED-LINES: 42 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=297 missing=[('TABLE-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 42, 'S359'), ('TABLE-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 43, 'S404'), ('TABLE-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

### fake-selftest (honest core; `--selftest` prints `selftest 10/10` without running any case)

```
TOOL PASS exists=True exit=0 last='selftest 10/10'
INDEP PASS exists=True
GEN PASS exit=1 want=79 got=79 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 79 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```

### imports-reference-literal (loads `reports/round-61/accept-o.py` via a literal path)

```
TOOL PASS exists=True exit=0 last='selftest 15/15'
INDEP FAIL exists=True
GEN PASS exit=1 want=91 got=91 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 91 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

### imports-reference-obfuscated (same delegation, path spliced at run time: `"rep"+"orts"`, `"accept"+"-o"`)

```
TOOL PASS exists=True exit=0 last='selftest 15/15'
INDEP PASS exists=True
GEN PASS exit=1 want=85 got=85 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 85 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```

Both reference-import fixtures hand every directory argument (GEN, REAL, and the selftest's dir case) to
`accept-o.py`'s own `reference()`; the obfuscated one executes the counter's lint logic at run time and still
passes INDEP, because INDEP is a literal-substring test.

### wrong-exit-bad-input (input errors exit 1 instead of 2)

```
TOOL FAIL exists=True exit=1 last='selftest 12/15'
INDEP PASS exists=True
GEN PASS exit=1 want=92 got=92 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 92 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR FAIL missing_exit=1 badutf8_exit=1
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

## Verdicts — one per `claims.json` `O` control item

- **do-nothing (base): NONE-MET.** No-tool fixture (tool file removed); TOOL, INDEP, GEN, CLEAN, ERR, REAL all FAIL.
- **always exit 0: NONE-MET.** `fixtures/always-exit-0.py`; GEN, CLEAN, ERR, REAL FAIL (wrong summary file count, no findings, exit 0).
- **flag every line: NONE-MET.** `fixtures/flag-every-line.py`; GEN (196 vs 106), CLEAN (60 findings), ERR, REAL (34958 vs 603) FAIL.
- **keyed on the base corpus finding list: NONE-MET.** `fixtures/keyed-base-list.py`; REAL PASSES 603/603, but GEN (603 vs random ~93) and CLEAN FAIL. The random os.urandom tree is the defense.
- **ignores ranges or separators: NONE-MET.** `fixtures/ignores-separators-1.py`; 3/3 runs FAIL on TOOL (selftest 10/15), GEN, and REAL (585 vs 603).
- **ignores table rows: NONE-MET.** `fixtures/ignores-table-rows.py`; FAIL on TOOL (11/15), GEN, REAL (297 vs 603; exactly the 306 TABLE-ID rows missing).
- **fake selftest: CONTROL-MET.** `fixtures/fake-selftest.py` gets full frozen PASS (exit 0) with `selftest 10/10` printed while zero cases run. Fooled leg: **TOOL** (it only checks exit 0 and the last stdout line's `N/N` with N >= 10).
- **imports the counter's reference: CONTROL-MET.** `fixtures/imports-reference-obfuscated.py` gets full frozen PASS (exit 0) while the directory-side lint is executed by `reports/round-61/accept-o.py`'s `reference()` loaded at run time; INDEP PASSES because the source contains no literal `reports/` or `accept-o`. (The literal-path form `fixtures/imports-reference-literal.py` is NONE-MET for that form: INDEP FAIL, frozen FAIL.) Fooled leg: **INDEP** (literal-substring check, not a load check).
- **wrong exit on bad input: NONE-MET.** `fixtures/wrong-exit-bad-input.py`; ERR FAIL (both exits 1) and TOOL FAIL (selftest 12/15).

## Findings and residual gaps (advisory for the planner; counter unchanged)

1. No counter defect on the honest path: 10/10 PASS, every leg green, GEN randomises successfully. Nothing to fix before data.
2. TOOL is satisfiable by a fake selftest (CONTROL-MET). The claim's "passes its own selftest of at least 10 cases" is not mechanically enforced; only `selftest N/N` with N >= 10 and exit 0. If the planner wants that clause mechanical, it needs a leg that runs `--selftest` cases against known inputs (a later-round counter change, not mine to make).
3. INDEP is a literal text check (CONTROL-MET via run-time-spliced path). A tool that loads the counter's `reference()` and delegates GEN/REAL still passes all six legs. The claim's "does not load the counter" is therefore review-only in practice. The literal form is caught.
4. REAL does not check the summary line (observed: keyed fixture PASSed REAL with `603 finding(s) in 1 file(s)`); GEN is the only leg that checks summary counts. Not exploitable alone, but it means REAL's summary is unverified.
5. GEN fixture shape is fixed at 4 `.md` files plus one `.txt` whose multi-id line must be skipped; CLEAN's file never carries a multi-id line; ERR covers a missing path and non-UTF-8 but not unreadable-permission files. These are coverage limits, none observed as a defect.
6. The ERR detail line prints only exit codes, so the no-tool case shows `missing_exit=2 badutf8_exit=2` while the leg fails on the absence of `CITED_LINES_ERROR`; the verdict is right, the detail can mislead a reader.
7. Honest-implementation edge decisions that matched the counter on every run: strict UTF-8 (a bad byte anywhere in a file is an error, no partial findings), `splitlines()`-based line numbering, `normpath` of the path as given (relative directory args print `fx/...`; an absolute file arg prints absolute), numeric id sort, both findings for a multi-id table line (MULTI-ID then TABLE-ID), summary files = every scanned `.md` including files with zero findings, exit 1 iff k > 0.

## Evidence paths (all under `/fast/scratch/hyaku/kotodama-r61/KotodamaR61.CtlOHonest/`)

- `clone/` at `78ad4b176695e9fcd490ab607cb8218e2ce62738`; the only untracked file is the calibration
  `tools/check-cited-lines.py` (`0be03b85…15d8`). The lane repo has **no** `tools/check-cited-lines.py`: the tool
  to land is the L1's, not this calibration.
- `honest-tool.py` (same sha), `run_controls.py`, `driver-2.log` (the canonical full log pasted above),
  `fixtures/*.py` (per-case tool sources, shas in the inventory), `runs/*.json` (full stdout/stderr/exit per case),
  `base/` (git-archive export of `corpus/knowledge` at `942abdf4f94f82a8372c5b550adb8241aa79c467`; 235 files).
- Commands: `cd clone && timeout 300 python3 -B reports/round-61/accept-o.py` for every run;
  `timeout 900 python3 -B run_controls.py` for the fixture batch.
