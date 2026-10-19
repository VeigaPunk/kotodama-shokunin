- Seat: K03 | scout | claim O | date 2026-10-19 | baseline da68a6d

# K03 — guard-adoption scout (F-C13-1 routing evidence for claim O)

Scope: how `tools/harness/receipt_guard.py` is adopted by `reports/round-32/run-validation.py`;
how `reports/round-{5,6,7,26}/run-validation.py` write their receipts (`path:line`); the
classification taxonomy the inventory instrument (`reports/round-34/op/O01-impl.md`) should use.
Every line number below was read from the working tree at baseline `da68a6d`
(`git status --short` → only `?? reports/round-34/`, so filed bytes are at baseline).

## 1. The adopted pattern, exactly as r32 does it

| Element | r32 evidence |
| --- | --- |
| receipt destination | `reports/round-32/run-validation.py:25` `OUTPUT = f"{ROUND}/validation.json"` (relative string, not a `Path`) |
| loader | `:1102-1104` — `def guard_receipt():` → `namespace = runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))` → `namespace["guard_receipt"](OUTPUT, repo_root=ROOT)` |
| guard call #1 (pre-measure) | `:1123` `if not args.check:` / `:1124` `guard_receipt()` — before `measure()` |
| guard call #2 (pre-publish) | `:1142` `guard_receipt()` immediately before `:1143` `safe_path(OUTPUT).write_text(rendered, encoding="utf-8")` |
| path safety wrapper | `:85-93` `safe_path()` rejects absolute paths and `..`/`.git` parts before the guard is reached |
| `--check` mode | never guards and never writes (`:1136-1139` prints `rendered`) |
| `REFRESH_RECEIPTS` | **not referenced anywhere in r32** (`grep -n "REFRESH_RECEIPTS" reports/round-32/run-validation.py` → no hits). Refresh is a property of the guard tool, not of the runner: `tools/harness/receipt_guard.py:35` `REFRESH_ENV = "REFRESH_RECEIPTS"`, consumed at `:147-150` — the exact value `1` is the only thing that permits a committed-receipt overwrite. |

Correction to the mission's shorthand: the adopted pattern in r32 is **load (runpy) + two guard
calls**; it does not itself use the `round_runner_main(measure, path, ...)` helper
(`tools/harness/receipt_guard.py:161`). No filed runner uses that helper — its only live callers
are the guard's own selftest fixture (`tools/harness/receipt_guard.py:306,:314`) and
`reports/round-14/guard/retro-tests.py:105,:244-245` (a harness that wraps a runner copy).

Guard tool health at this tree (gap is adoption, not tooling):
`sha256sum tools/harness/receipt_guard.py` → `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`;
`python3 tools/harness/receipt_guard.py --selftest` → exit 0, `"controls_passed": 45`,
`"controls_total": 45`, `"selftest_passed": true`.

Guard semantics the instrument must encode (from the tool and its output above):
- committed destination + env ≠ exactly `1` → `SystemExit(3)`, stderr `[RECEIPT-GUARD-COMMITTED]`;
- committed destination + `REFRESH_RECEIPTS=1` → allowed, stderr `[RECEIPT-GUARD-REFRESH]`;
- **new/untracked destination → allowed with no override** (controls
  `new-receipt-missing-parents-allowed`, `untracked-receipt-allowed`, both exit 0). This is why
  round 34's own new runner may legitimately be run in-tree while filed runners may not.

## 2. How each named hazard runner writes its receipt

| round | own-receipt write | guard reference in file | class |
| --- | --- | --- | --- |
| r5 | `reports/round-5/run-validation.py:194` `(HERE / "validation.json").write_text(json.dumps(report, …))` | **none** (`grep -c -i "receipt_guard\|REFRESH_RECEIPTS\|committed_blob\|refusing overwrite"` → `0`) | unguarded |
| r6 | `reports/round-6/run-validation.py:336` same shape (`HERE` at `:19`) | **none** (count `0`) | unguarded |
| r7 | `reports/round-7/run-validation.py:1171` `(HERE / "validation.json").write_text(…, encoding="utf-8")` (`HERE` at `:55`) | **none** (count `0`) | unguarded |
| r26 | `reports/round-26/run-validation.py:1909` `safe_path(OUTPUT).write_text(rendered, encoding="utf-8")` (`OUTPUT` at `:90`) | `:1855-1857` `def guard_receipt(): … runpy.run_path("tools/harness/receipt_guard.py")`; called `:1906` inside `try/except SystemExit` (`:1905-1908`) immediately before the write | **guarded (write-only)** |

### 2a. Correction to the F-C13-1 record as quoted in `claims.json` / `LOG.md`

`LOG.md:3556-3561` (F-C13-1 entry) says "The r26 runner carries the same hazard (`:90`, `:1909`)".
`:90` is the `OUTPUT` constant and `:1909` the write line; the citation misses `:1855` (definition)
and `:1906` (the guard call). **r26's own-receipt write is guarded**: an in-tree re-run without
`REFRESH_RECEIPTS=1` exits 3 from `guard_receipt()` and never reaches `:1909`
(the `try/except SystemExit` returns the code), so r26 is *not* a same-class hazard as r5/r6/r7.

Two residual caveats the routing (O05) must carry rather than repair:
1. r26's guard is **pre-publish only** — `measure()` runs unguarded (`:1904`); only the write is
   protected. The same is true of r20, r23, r24, r25, r27, r28.
2. The guard does not defend against an environment that already carries `REFRESH_RECEIPTS=1`.
   `reports/round-21/run-validation.py:474` sets exactly that inside its isolated clones
   (`env["REFRESH_RECEIPTS"] = "1"` before `subprocess.run([sys.executable, f"reports/round-{number}/run-validation.py"], cwd=clone, …)` at `:482-483`). Exported into an in-tree run, the
   same value would let any *guarded* runner overwrite a filed receipt. Hazard class
   "guard-bypass-by-exported-override" is real and distinct from "no guard at all".

## 3. Census — all 28 filed runners (`ls reports/round-*/run-validation.py | wc -l` → 28)

Rounds with a filed runner: 5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33.
Directory census (`ls -d reports/round-*` → 30 dirs, rounds 5-34): rounds 1-4 have no directory in
this repo; `reports/round-13/` exists but holds only `claims.json` and `targets.json` — no runner.
So the runner inventory's denominator is 28 files, and the instrument should not treat round 13's
directory (or rounds 5-12's other scripts) as runners.

**Class GUARDED (17)** — a guard call sits between `measure()` and the own-receipt write:

| sub-class | rounds | evidence |
| --- | --- | --- |
| `importlib_preflight`, dual (pre-measure + pre-publish) | 14, 15, 16, 17, 18 | def `:413/:1037/:998/:1117/:1511`; `module.guard_receipt(ROOT / OUTPUT, repo_root=ROOT)` at `:420/:1044/:1005/:1124/:1518`; second call + write at `:716/:717`, `:1345/:1346`, `:1264/:1265`, `:1430/:1431`, `:1850/:1851` |
| `importlib_preflight`, write-only | 20 | def `:1278`, `guard_preflight()` `:1484`, write `:1485` (after `validate()` at `:1480`) |
| `runpy_wrapper`, dual | 22, 30, 31, 32, 33 | def/calls/write: `:827/:911,:921/:922`, `:883/:903,:922/:923`, `:1118/:1139,:1158/:1159`, `:1102/:1123,:1142/:1143`, `:1441/:1459,:1470/:1471` |
| `runpy_wrapper`, write-only | 23, 24, 25, 26, 27, 28 | def/call/write: `:1064/:1094/:1097`, `:1151/:1181/:1184`, `:1108/:1142/:1145`, `:1855/:1906/:1909`, `:1853/:1904/:1907`, `:1996/:2095/:2098` |

**Class UNGUARDED (11)** — own-receipt write, zero guard reference in the file:

| round | write line | destination expression |
| --- | --- | --- |
| 5 | `:194` | `HERE / "validation.json"` (`HERE` `:17`) |
| 6 | `:336` | `HERE / "validation.json"` (`HERE` `:19`) |
| 7 | `:1171` | `HERE / "validation.json"` (`HERE` `:55`) |
| 8 | `:1486` | `output = ROOT / OUTPUT_REL` (`:1485`), `OUTPUT_REL` `:99` |
| 9 | `:1910` | `output = ROOT / OUTPUT_REL` (`:1909`), `OUTPUT_REL` `:127` |
| 10 | `:1054` | `output = ROOT / OUTPUT_REL` (`:1053`), `OUTPUT_REL` `:60` |
| 11 | `:1740` | `output = ROOT / OUTPUT_REL` (`:1738`), `OUTPUT_REL` `:125` |
| 12 | `:1071` | `out = ROOT / OUTPUT` (`:1069`), `OUTPUT` `:18` |
| 19 | `:21` | `pathlib.Path('reports/round-19/validation.json').write_text(...)` inside the inline `python3 -c` payload (`:14-21`) |
| 21 | `:1115` | `output = ROOT / OUTPUT` (`:1113`), `OUTPUT` `:20` |
| 29 | `:922` | `safe_path(OUTPUT).write_text(rendered, ...)`, `OUTPUT` `:23` |

17 + 11 = 28 → census is complete. No runner is in a third state (no file writes through
`open(...,"w")`, `json.dump(f)`, or `os.replace`; the write sites above are the only ones that
target the runner's own round directory — verified by `grep -n "validation\.json" … | grep -i "write\|dump\|open("` per runner).

## 4. Taxonomy the instrument should use

The trap is that "mentions `receipt_guard`" ≠ "adopts the guard". Four reference kinds exist in
this tree, with different meanings:

1. **self-guard** — imports/loads the guard and calls `guard_receipt` on the runner's *own*
   receipt path (`reports/harness` loader style: importlib preflight r14-20, runpy wrapper
   r22-28/r30-33, or `round_runner_main` — none filed).
2. **subject reference** — runs `tools/harness/receipt_guard.py --selftest` as one regression
   command among many: `reports/round-25/run-validation.py:173`,
   `reports/round-26/run-validation.py:199`, `reports/round-27/run-validation.py:222`,
   `reports/round-28/run-validation.py:231` (all four are
   `("receipt-guard-selftest", ("tools/harness/receipt_guard.py", "--selftest"))` in a REGRESSIONS
   tuple; verified by `grep -n "receipt-guard-selftest"`). Also `reports/round-14/run-validation.py:439,:445`, which regex-scans ledger
   prose for the words `receipt.guard|REFRESH_RECEIPTS`. These must **not** count as adoption.
3. **consumer of refresh mode** — sets `REFRESH_RECEIPTS=1` for subprocesses (clone harness):
   `reports/round-21/run-validation.py:474` (+ prose `:1106`). Not adoption.
4. **non-runner JSON writer** — scripts that write *other* receipts, e.g.
   `reports/round-6/check-checkpoint.py:117` writes `checkpoint-validation.json`; ~13 further
   scripts under `reports/round-*/` merely *read* `validation.json`. Must not be classified.

Proposed record fields per inventory row (one per `reports/round-*/run-validation.py`):

- `round`, `path`, `sha256`
- `own_receipt_write`: `{line, expression}` — resolve the constant (`OUTPUT`/`OUTPUT_REL`) or the
  local (`output = ROOT / OUTPUT_REL`, `out = ROOT / OUTPUT`) or the inline literal;
- `write_marked_in_place`: true for all 28 (each rewrites its own round's `validation.json`);
- `adoption`: one of `guarded_dual`, `guarded_write_only`, `unguarded`;
- `loader`: one of `importlib_preflight`, `runpy_wrapper`, `dd_import`, `none`;
- `guard_def_line`, `guard_call_lines` (ordered), `guards_before_measure` (bool),
  `guards_before_publish` (bool);
- `references`: list of `{kind: self_guard|subject_selftest|refresh_env|prose, line}` so the
  subject/consumer cases stay visible without inflating `adoption`;
- `hazard_class`: `none` (guarded) | `receipt-overwrite` (unguarded) | `guard-bypass-exported-override`
  (guarded, but reachable with `REFRESH_RECEIPTS=1` exported — annotate, do not double-classify).

Detection notes (stdlib only; mirrors §2/§3 shapes):
- `ast` walk: collect module-level `OUTPUT*` string constants; collect `Name = ROOT / <const>` and
  `Name = ROOT / f"…"` aliases; then flag `Attribute(value=Name|Call(safe_path,…), attr="write_text")`
  whose resolved target basename is `validation.json` and whose parent round == the file's round.
- guard detection: `runpy.run_path(<str containing "receipt_guard.py">)` OR
  `importlib.util.spec_from_file_location(..., <receipt_guard>)` OR a call named
  `guard_receipt(...)`/`guard_preflight()` OR `round_runner_main(...)`.
- near-miss names that must NOT trigger guard detection (name-only matching is unsafe):
  `reports/round-7/run-validation.py:577` `guard_positive_and_selftest()` and `:791`
  `guard_foreign_cwd_no_writes(scratch)` (both are about the handoff **packet** gate, used at
  `:1111`/`:1120`), and `reports/round-29/run-validation.py:629` `protection_guard(before, after)`
  (a before/after regression comparison). Require the guard *module path* or a call passing the
  runner's own receipt path.
- call-to-write ordering: guard call line < write line, and the guard call not nested inside a
  `--selftest`/`--check`-only branch and not inside a subprocess harness for another round.
- `--check`/`--selftest` early returns (`:args.selftest` guard in r14-20/r22-28/r30-33) do not
  perform the write; treat them as non-path.

Negative/positive fixtures for `--selftest` (each cheap and synthetic):
- positive-adopted: a copy of the r32 shape (runpy + dual call) → `guarded_dual`;
- positive-written-only: the r26 shape (def + single call in `try/except`) → `guarded_write_only`
  — this is the fixture that fails an instrument that only looks for two call sites;
- negative-guarded-not-flagged: any of the 17 guarded runners must not appear in the unguarded list;
- negative-subject-not-adopted: a file whose only guard hit is
  `("receipt-guard-selftest", (GUARD, "--selftest"))` → `adoption: unguarded`, `references[0].kind=subject_selftest`;
- negative-non-runner: a script writing `checkpoint-validation.json` → not inventoried.

Two independent-falsifiable thresholds from `claims.json` claim O map onto this: "inventory covers
100% of filed runners" = 28 rows (command `ls reports/round-*/run-validation.py | wc -l` → 28) and
"the four named hazards classified" — with the classification being **r5, r6, r7 =
`receipt-overwrite`; r26 = `guarded_write_only` with the `:90/:1909` citation corrected to
`:1855/:1906/:1909`**. If the instrument instead reports r26 as unguarded, it is wrong and the
fixture above will catch it.

## 5. Routing implications for O05 (draft, not a decision)

- Unguarded (r5, r6, r7, r8, r9, r10, r11, r12, r19, r21, r29): isolated `git archive` copies only —
  `run-validation.py` is never executed in-tree. This matches the F-C13-1 prevention rule now in
  force and the round-33 practice (`.scratch/c05-iso/`, `LOG.md:3553-3561`).
- Guarded (17): in-tree re-runs are refused by construction (exit 3) *unless* `REFRESH_RECEIPTS=1`
  is present in the environment; the refresh protocol must therefore name the environment state
  (`REFRESH_RECEIPTS=1` exported explicitly, never inherited from a clone harness) and record the
  pre/post `git hash-object` of the target receipt.
- Round 34's own runner does not exist yet (`reports/round-34/run-validation.py`), so its receipt
  destination is uncommitted and the guard would allow it — no guard is needed for the round's own
  counting command; the tool's purpose is protecting *filed* receipts.

## Owed: none

## Citations

Paths (all read at baseline `da68a6d`; working tree clean apart from `?? reports/round-34/`):
- `tools/harness/receipt_guard.py:1-14,34-35,41,70-150,152-165,306,314,354`
- `reports/round-32/run-validation.py:25,85-93,1102-1104,1123-1124,1136-1139,1142-1143`
- `reports/round-5/run-validation.py:17,170,194` · `reports/round-6/run-validation.py:19,280-285,336` · `reports/round-7/run-validation.py:55,1011-1021,1171`
- `reports/round-8/run-validation.py:99,1485-1486` · `reports/round-9/run-validation.py:127,1909-1910` ·
  `reports/round-10/run-validation.py:60,1053-1054` · `reports/round-11/run-validation.py:125,1738-1740` ·
  `reports/round-12/run-validation.py:18,1069-1071`
- `reports/round-19/run-validation.py:14-21` · `reports/round-21/run-validation.py:20,474,482-483,1106,1113,1115` · `reports/round-29/run-validation.py:23,922`
- `reports/round-14/run-validation.py:23,413-420,439,445,708-717` · `reports/round-15/run-validation.py:42,1037-1044,1337-1346` · `reports/round-16/run-validation.py:55,998-1005,1256-1265` · `reports/round-17/run-validation.py:66,1117-1124,1422-1431` · `reports/round-18/run-validation.py:65,1511-1518,1842-1851` · `reports/round-20/run-validation.py:55,1278-1285,1480-1485`
- `reports/round-22/run-validation.py:23,827-828,911,921-922` · `reports/round-23/run-validation.py:49,1064-1065,1094-1097` · `reports/round-24/run-validation.py:63,1151-1152,1181-1184` · `reports/round-25/run-validation.py:83,173,1108-1109,1142-1145` · `reports/round-26/run-validation.py:90,199,1855-1856,1905-1909` · `reports/round-27/run-validation.py:85,222,1853-1854,1904-1907` · `reports/round-28/run-validation.py:87,231,1996-1997,2095-2098`
- `reports/round-30/run-validation.py:26,883-884,903,922-923` · `reports/round-31/run-validation.py:26,1118-1119,1139,1158-1159` · `reports/round-33/run-validation.py:27,1441-1442,1459,1470-1471`
- `reports/round-7/run-validation.py:577,791,1111,1120` · `reports/round-29/run-validation.py:629,779`
- `reports/round-14/guard/retro-tests.py:102,105,107,244-245`
- `reports/round-6/check-checkpoint.py:117`
- `LOG.md:3548-3561` (F-C13-1 incident record) · `reports/round-34/claims.json` (claim O before/thresholds) · `reports/round-34/targets.json:16,44,48`

Commands run (all read-only or tool-selftest; no `reports/round-*/run-validation.py` was executed):
- `git status --short` → `?? reports/round-34/`
- `ls reports/round-*/run-validation.py | wc -l` → `28`
- `grep -rln "receipt_guard" reports/round-*/run-validation.py | sort` → 17 files (r14-18, r20, r22-28, r30-33)
- `sha256sum tools/harness/receipt_guard.py` → `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`
- `python3 tools/harness/receipt_guard.py --selftest` → exit 0, parallel-block output `"controls_passed": 45, "controls_total": 45, "selftest_passed": true`
- per-runner `grep -n -i "committed_blob|REFRESH_RECEIPTS|receipt_guard|refusing overwrite" reports/round-{5,6,7,8,9,10,11,12,19,21,29}/run-validation.py` → counts 0,0,0,0,0,0,0,0,0,2,0
- AST-free structural walk in `.scratch` python one-liners over all 28 runners (write sites, guard def/call sites, subject references) — script text in this seat's transcript, output reproduced in §2-§3/§4

to-verify (not established here):
- whether any round-34 counting command other than the instrument's selftest needs the taxonomy;
- a differently-named *inlined* receipt guard is not excluded: the unguarded class rests on the
  four-token grep plus a `def .*guard|guard(` name scan of r8-12/19/21/29, which returned only
  `reports/round-29/run-validation.py:629` `protection_guard(before, after)` (a before/after
  regression comparison, unrelated to receipts). No file-by-file semantic read of r8-12/19/21/29's
  write paths was performed beyond the write sites cited in §3.
