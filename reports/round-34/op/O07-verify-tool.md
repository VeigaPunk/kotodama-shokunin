- Seat: O07 | verifier | claim O | date 2026-10-19 | baseline da68a6d

# O07 — independent verification of the claim-O instrument and adoption inventory

Mission (`reports/round-34/targets.json:50`): extract O02's tool source to
`.scratch` and run its `--selftest` + `--json`; compare `--json` to O04's
predicted inventory row-for-row; file defects. Out: `op/O07-verify-tool.md`.

**Result: the inventory logic is CONFIRMED row-for-row on the real tree (28/28)
and REJECTED on four of its own control fixtures.** The tool that can be run
today is not O02's (`op/O02-tool-source.md` never landed; no `--selftest`/`--json`
exists anywhere — §3.5) but **O01's landed detection core**, which does run:
I extracted it to `.scratch`, ran it against the repo root, and it reproduces my
independent oracle exactly — 28 runners, 11 `unguarded` / 17 `adopted`, every
write anchor and every per-file sha256 matching what O04 predicted. That is the
strongest available evidence for the claim's central number. Against O03's own
12-fixture control list the same core returns **7 correct, 4 wrong**, and three
of the four wrong answers are **false greens on a real hazard** (§3.4). On the
current filed tree that failure is latent (no filed runner has the trap shape);
it becomes live the moment a runner defines the guard helper without calling it.
Details in defects O07-D5…O07-D7.

No filed round runner was executed anywhere in this seat's work (F-C13-1); no
filed byte was written (§6 proves it by digest).

## 1. Method — three independent extraction paths

| path | mechanism | why it is independent |
|---|---|---|
| **A** | my `ast` census (`.scratch/round-34-O07/census3.py`): resolve the receipt sink (`OUTPUT`/`OUTPUT_REL`/literal), follow one-step local aliases (`output = ROOT / OUTPUT_REL`, `out = ROOT / OUTPUT`), collect `write_text`/`write_bytes`/`open(...,'w')` calls mentioning the sink, classify by guard loader + guard call lines | structural |
| **B** | `sed -n '<line>p'` quote of every claimed write line, read by me | raw filed text, independent of my parser |
| **C** | O01's landed core run as an outside program over the real tree and over synthetic trees I built (§3.3–§3.4) | a different implementation, written by another seat, whose disagreements with A/B are findings either way |

Where A and B disagree, B is authoritative. An earlier version of A (census v1/v2)
produced three wrong rows and is recorded so the method's failure modes are
auditable: v1 counted **all** `write_text` calls (r18 showed 11 sites); v2
resolved only direct sink symbols and reported r8–r12, r19, r21 as
`no-receipt-write`. Those false negatives **are** the detection hazards a
classifier must survive (O07-D3), and the landed core survives them (§3.3).

## 2. Oracle — 28-row adoption census at da68a6d

Population: **28** filed runners (`reports/round-5..33`; no round-13).
Command: `python3 -B .scratch/round-34-O07/census3.py` → `census3.json`
(sha256 `24a2067f9590aa14f5482f7dbe0a6c387e0d1856291d98bda51d369a562a5812`).
Canonical TSV: `.scratch/round-34-O07/oracle.tsv` (sha256
`9252d04363c5c87f49b0a937184da484a217212b0a13520f6eddc81e529d00d3`) — the file
the §5.3 comparator consumes. **17 `guarded-adopted` / 11 `unguarded-in-place` /
0 other.**

One correction against my own parser, recorded because it is the same error class
the tool must avoid: census v3 anchored r19's embedded hit on line `:19` (the
`json.load(open(...))` read inside the same string) rather than the write at
`:21`; §2.1 and `oracle.tsv` carry the corrected `:21` from `sed -n '21p'`.

### 2.1 Unguarded — the 11 runners with no refusal path

| round | own-receipt write | filed line, quoted verbatim |
|---|---|---|
| r5 | `reports/round-5/run-validation.py:194` | `(HERE / "validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")` |
| r6 | `reports/round-6/run-validation.py:336` | `(HERE / "validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")` |
| r7 | `reports/round-7/run-validation.py:1171` | `(HERE / "validation.json").write_text(` |
| r8 | `reports/round-8/run-validation.py:1486` | `output.write_text(json.dumps(receipt, indent=2, sort_keys=True,` (`OUTPUT_REL` `:99`, `output = ROOT / OUTPUT_REL` `:1485`) |
| r9 | `reports/round-9/run-validation.py:1910` | `output.write_text(json.dumps(receipt, indent=2, sort_keys=True,` (`OUTPUT_REL` `:127`) |
| r10 | `reports/round-10/run-validation.py:1054` | `output.write_text(json.dumps(receipt, indent=2, sort_keys=True,` (`OUTPUT_REL` `:60`) |
| r11 | `reports/round-11/run-validation.py:1740` | `output.write_text(json.dumps(receipt, indent=2, sort_keys=True,` (`OUTPUT_REL` `:125`) |
| r12 | `reports/round-12/run-validation.py:1071` | `out.write_text(json.dumps(receipt, indent=2, sort_keys=True,` (`OUTPUT` `:18`, `out = ROOT / OUTPUT` `:1069`) |
| r19 | `reports/round-19/run-validation.py:21` | `pathlib.Path('reports/round-19/validation.json').write_text(json.dumps(v,indent=1,ensure_ascii=False))` — inside an embedded `python -c` string; whole file 24 lines |
| r21 | `reports/round-21/run-validation.py:1115` | `output.write_text(json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n",` (`OUTPUT` `:20`, `output = ROOT / OUTPUT` `:1113`) |
| r29 | `reports/round-29/run-validation.py:922` | `safe_path(OUTPUT).write_text(rendered, encoding="utf-8")` |

`grep -c receipt_guard` over these eleven files → `0` for each. The only
`REFRESH_RECEIPTS` mention in the set is `reports/round-21/run-validation.py:474`
(its `.scratch` clone driver, documented `:1106`) — it does not guard r21's own
write. r29's `safe_path` is path confinement only (`:89-92`).

### 2.2 Adopted — the 17 runners that guard their own write

| round | loader | guard-call lines | sink write | Δ (write − last pre-write call) |
|---|---|---|---|---|
| r14 | importlib | 420, 708, 716 | `:717` | 1 |
| r15 | importlib | 1044, 1337, 1345 | `:1346` | 1 |
| r16 | importlib | 1005, 1256, 1264 | `:1265` | 1 |
| r17 | importlib | 1124, 1422, 1430 | `:1431` | 1 |
| r18 | importlib | 1518, 1842, 1850 | `:1851` | 1 |
| r20 | importlib | 1285, 1484 | `:1485` | 1 |
| r22 | runpy | 911, 921 | `:922` | 1 |
| r23 | runpy | 1094 | `:1097` | 3 |
| r24 | runpy | 1181 | `:1184` | 3 |
| r25 | runpy | 1142 | `:1145` | 3 |
| r26 | runpy | **1906** | `:1909` | 3 |
| r27 | runpy | 1904 | `:1907` | 3 |
| r28 | runpy | 2095 | `:2098` | 3 |
| r30 | runpy | 903, 922 | `:923` | 1 |
| r31 | runpy | 1139, 1158 | `:1159` | 1 |
| r32 | runpy | 1123, 1142 | `:1143` | 1 |
| r33 | runpy | 1459, 1470 | `:1471` | 1 |

Measured: every adopted runner has a guard call strictly before its sink write,
gap 1 or 3 lines (`max Δ = 3`). Two idioms —
`importlib.util.spec_from_file_location("round<N>_receipt_guard", ROOT / GUARD)`
(r14–r18, r20; note the **renamed module**, e.g. `reports/round-17/run-validation.py:1118`)
and `runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))`
(r22–r28, r30–r33). Neither is `import receipt_guard`.

## 3. Verification legs — results

### 3.1 O04's predicted inventory vs the oracle — **GREEN on substance**

`reports/round-34/op/O04-predicted-inventory.md` (sha256
`7f0b99982715ea22cfcacb1bf6cd3c6b086f9390db04ac6150c85f49a096d20d`), JSON block
at `:36-80`. Programmatic diff of its 28 rows against `oracle.tsv`:

- row set: **identical** (0 missing, 0 extra);
- `class`: identical under label normalization (`guarded-in-place-write` ≡ my
  `guarded-adopted`; `unguarded-in-place-write` ≡ `unguarded-in-place`). The label
  difference is a taxonomy naming choice, **not** a defect, and I did not file it;
- per-runner `sha256`: **28/28 identical** to my census (the digests are the same
  file-identity check, so both seats hashed the same bytes);
- write line: 27/28 identical; r19 is recorded as the descriptive string
  `"embedded:17 (file line 21)"` where my oracle holds `21`. Semantically
  identical (it names both the payload line and the file line) — my comparator's
  single reported "mismatch" is my own string-comparison artifact, not an O04
  error;
- `counts` field: `{runners: 28, guarded_in_place: 17, unguarded_in_place: 11,
  no_receipt_write: 0}` — matches the oracle;
- `known_hazards`: rows for r5/r6/r7 marked `agrees: true` and **r26 marked
  `agrees: false` with `measured_class: guarded-in-place-write`** — O04
  independently reached the O07-D1 reclassification from the bytes.

### 3.2 The claim's counting commands — status

| command (`claims.json:46-50`) | status |
|---|---|
| `python3 tools/harness/receipt_guard_adoption.py --selftest` | **could-not-evaluate** — the tool is not on disk (`ls tools/harness/` → `packet_links.py packet_uncertainty.py r8_checks.py receipt_guard.py`); no fragment ships a `--selftest` implementation (§3.5) |
| `python3 tools/harness/receipt_guard_adoption.py --json` | **could-not-evaluate** — same; the runnable core (§3.3) has no `--json` flag, it prints its inventory on stdout |
| `python3 reports/round-34/run-validation.py` | does not exist (round in flight) |

Owner of the two unlanded legs: **O02** (`op/O02-tool-source.md` absent at every
poll). The detector logic itself is verified here through O01's core, so the
outstanding item is the CLI surface, not the analysis.

### 3.3 O01's landed core on the real tree — **GREEN, 28/28 rows**

`op/O01-impl.md` (sha256 `3b038b3ce662bcabb940d2015d92acc3ebb15285bf924e97902bc1b1fa940927`)
carries a complete runnable detection module in its single fenced python block
(`:76-446`, fences at `:75`/`:447`, 371 lines); its entry point is
`if __name__ == "__main__": print(json.dumps(scan_repository(sys.argv[1] …)))`.
I extracted it **before** running it and checked it is inert — the only
`write_text`/`subprocess` strings in it are the names of the patterns it *searches
for* (`:26 WRITE_METHODS`, `:263`), no write or exec primitive of its own:

```
python3 -B .scratch/round-34-O07/landed-o01/receipt_guard_adoption_core.py $PWD
→ exit 0, runner_count 28, class_counts {'unguarded-writer': 11, 'guard-adopted': 17}
```

Row-for-row against `oracle.tsv`: **28/28 class agreement and 28/28 write-site
agreement**, including the two rows my own v1/v2 got wrong —
r19 (site `21`, `embedded_receipt_writes: true`) and the alias receivers
r8/r9/r10/r11/r12/r21 (sites 1486/1910/1054/1740/1071/1115) and r29 (`922`).
This is the claim's central number independently reproduced by a different
implementation: **11 unguarded, 17 adopted**.

### 3.4 O01's landed core against O03's 12 control fixtures — **7 correct, 4 wrong**

I materialized O03's own `FIXTURES` dict
(`reports/round-34/op/O03-selftest.md`, single python block, 12 fixtures with
their source strings) into `.scratch/round-34-O07/o03fixtures/` and ran the
extracted core over it (exit 0, `runner_count 11` — correct, F10 is deliberately
not a round runner):

| fixture | O03 expects (`O03-selftest.md:39-50`) | core says | verdict |
|---|---|---|---|
| F01 guarded-runpy-shim | `guarded` | `guard-adopted` | OK |
| F02 guarded-module-call | `guarded` | `guard-adopted` | OK |
| **F03 guard-defined-not-called** | `guard-defined-not-called` | **`guard-adopted`** | **FAIL — false green** |
| **F04 guard-called-after-write** | `guard-after-write` | **`guard-adopted`** | **FAIL — false green** |
| F05 unguarded-here-relative | `unguarded` | `unguarded-writer` | OK |
| F06 unguarded-output-const | `unguarded` | `unguarded-writer` | OK |
| F07 unguarded-variable-receiver | `unguarded` | `unguarded-writer` | OK |
| F08 clean-no-receipt-write | `clean-no-receipt-write` | `no-receipt-write` | OK |
| **F09 embedded-code-writer** | `embedded-write-suspect` | `unguarded-writer` | **FAIL — vocabulary** |
| F10 non-runner-json-writer | absent from inventory | absent | OK |
| F11 unguarded-os-replace | `unguarded` | `unguarded-writer` | OK |
| **F12 writes-other-round-receipt** | `writes-other-round-receipt` | `unguarded-writer` | **FAIL — vocabulary** |

My own four traps (written independently, `.scratch/round-34-O07/trap/`) confirm
F03/F04 are not fixture artifacts:

| trap | honest answer | core says |
|---|---|---|
| helper defined at `:10-12`, **never invoked**, write `:17` | unguarded hazard | `guard-adopted`, `hazard: False`, `pre_write: True` |
| helper invoked `:17` **after** the write `:16` | unguarded (first write unprotected) | `guard-adopted`, `hazard: False`, `pre_write: True` |
| helper invoked only under `if "--check" in sys.argv:` `:17`, write `:18` | unguarded | `guard-adopted`, `hazard: False`, `pre_write: True`, `guard_call_conditional: False` |
| write via `os.replace(tmp, target)` | unguarded | `unguarded-writer`, `hazard: True` (correct) |

So: the core is right on the filed tree and wrong on the trap shapes O03 names.
Root cause is O07-D5.

### 3.4b Cross-check against O08's independent traps (different shapes, same verdicts where it matters)

`op/O08-traps.md` (landed after §3.4) staged its own trap tree at
`.scratch/o08-traps/tree/reports/round-90{1,2,3,4}/run-validation.py` with a
machine-readable expectation file (`.scratch/o08-traps/EXPECTATIONS.json`,
`forbidden_wrong_green` lists per trap). I ran the extracted core over that tree
(exit 0):

| fixture | O08 expectation | core says | verdict |
|---|---|---|---|
| T1 round-901 (importlib helper loaded, guard never invoked; write `:59`) | `referenced-not-called`; forbidden: adopted/guarded/clean/no-write | `guard-loaded-uncalled`, `hazard: True` | **correct** (the helper only *returns* the module, `:22-29`; no in-def guard call exists to be miscounted) |
| T2 round-902 (guard invoked only under `if args.guarded:` `:61`; write `:63`) | `conditional-guard`; forbidden: adopted/guarded/clean | **`guard-adopted`, `hazard: False`** | **FORBIDDEN wrong green** |
| T3 round-903 (write via `os.replace(staging, output)` `:56-57`; guard path only in a CHECKS string `:19`) | `referenced-not-called`; forbidden: adopted/guarded/clean/no-write | `guard-loaded-uncalled`, `hazard: True` | **correct** |
| C+ round-904 (genuine adoption) | `adopted` | `guard-adopted`, `hazard: False` | **correct** (no false positive) |
| C− `tools/cache-export.py` | out of scope | absent from inventory | **correct** |

This sharpens O07-D5 and removes one of its false alarms: a helper that merely
*loads* the guard and is never called is classified honestly (T1). The failure is
specific — it needs an actual guard-call expression **inside** a `def` body (the
`namespace["guard_receipt"](...)` runpy idiom of the filed adopters) or an
invocation that is conditional or post-write. O08's T1/T3 shapes are the ones the
core survives; O08's T2 and O03's F03/F04 are the three it fails.

### 3.5 Tool-source availability (why the CLI legs are owed)

`reports/round-34/op/O02-tool-source.md` did not exist at any poll (file censuses
at 04:00, 04:06, 04:09, 04:12; the `op/` directory eventually held
`O01-impl.md O03-selftest.md O04-predicted-inventory.md O05-routing.md
O06-scribe.md O07-verify-tool.md O09-verify-routing.md O10-final-receipt.md`).
The bytes do not live elsewhere either: a tree-wide scan of
`reports/round-34/*/*.md` fenced python blocks found exactly two large blocks —
O01's 371-line core and O03's 162-line fixture table — and **neither contains
`argparse`, `--selftest` or `--json`** (occurrence counts `0, 0, 0`). Ten
fragments mention the tool's name in prose only.

### 3.6 Guard behavioural controls at HEAD — GREEN (the `adopted` class is real)

1. `python3 -B tools/harness/receipt_guard.py --selftest` → exit **0**,
   `controls_passed 45 / 45`, `selftest_passed True`, `date 2026-10-19`
   (`.scratch/round-34-O07/guard-selftest.json`).
2. `python3 -B tools/harness/receipt_guard.py reports/round-<N>/validation.json`
   for N ∈ {5,6,7,8,9,10,11,12,19,21,29,26,32} → **exit 3** for all thirteen,
   stderr `receipt_guard: refusing overwrite … committed_sha=da68a6d705e41f3…
   [RECEIPT-GUARD-COMMITTED]`; no write in either mode.
3. Consequence: the 17 adopted runners contain this refusal path; the 11
   unguarded ones contain nothing that can refuse — their write is reached on
   every non-`--check` run.
4. Guard identity `sha256 tools/harness/receipt_guard.py` →
   `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1` (373 lines),
   matching the SKILL box-1 row (`reports/round-34/calib/C07-verify-survey.md:109`).

## 4. Defects filed

### O07-D1 — r26's class in the claim and the LOG is contradicted by bytes; **now three-way corroborated**

`claims.json:43` and `LOG.md:3559-3560` call r26 a hazard at `:90`/`:1909`. Bytes:
`reports/round-26/run-validation.py:1855-1857` defines the wrapper and `:1906`
calls it inside the `else:` branch (`:1905`), converting `SystemExit` to a return
code (`:1907-1908`), so the `:1909` write is unreachable on refusal.
**r26 is `guarded-adopted`.** Corroborated independently by O06
(`op/O06-scribe.md:122-134`) and O04 (`known_hazards` row, `agrees: false`), and
by O01's core classifying r26 `guard-adopted` with `pre_write: true`. Fix belongs
in a NEW `LOG.md` row (integrator owns the append, `AGENTS.md`).

### O07-D2 — the hazard class is 11, not 4

r5/r6/r7 are confirmed hazards; the claim's fourth (r26) is not one, and eight
real ones are unnamed: **r8, r9, r10, r11, r12, r19, r21, r29**. A routing
artifact built on the claim's list leaves eight filed receipts rewritable in
tree. The inventory's coverage contract is 28/28 rows with a positive class; the
routing row must be derived from the inventory, not from the claim's prose. The
round-33 incident (`LOG.md:3551-3553` rewrote r5/r6/r7) is the sampled subset of
an 11-runner class — the standing-debt row should be sized accordingly.

### O07-D3 — detection requirements a classifier must survive (now SATISFIED by O01's core)

Measured against my own v1/v2 failures and against the landed core:

- **(a) alias receivers** (r8/r9/r10/r11/r12/r21/r29 write through a local alias):
  my v2 missed 7 of 11; O01's core gets all seven right (`op/O01-impl.md:8-11`).
- **(b) embedded-script write (r19)**: my v3 anchored `:19` instead of `:21`;
  O01's core reports site `:21` with `embedded_receipt_writes: true` — better than
  my parser, and the flag is the honest "lower-confidence" marker.
- **(c) `importlib` adoption with a renamed module** (r14–r18, r20): a classifier
  keyed on `import receipt_guard` would call six adopted runners unguarded; the
  core gets them right.
- **(d) a guard mention must not launder a write** (r21's `REFRESH_RECEIPTS:474`):
  the core keeps r21 `unguarded-writer`. **Half-satisfied**: it fails the
  conditional-*call* variant (O07-D5).

### O07-D4 — minor errata in O06 §2.1 (no class changes)

`op/O06-scribe.md:73` gives r14's call site as `:715` (actual `:716`;
`sed -n '713,718p'` → `:716 guard_preflight()`, `:717` write); `:74` gives r15 one
call site `:1044` where the file has three (`:1044`, `:1337` pre-measure, `:1345`
pre-write). Classes and anchors unaffected.

### O07-D5 — **the adoption test counts definition-site calls: three false-green shapes** (highest-severity finding)

In the extracted core (`op/O01-impl.md`, block lines 322-332; fragment lines
397-407) the classification is
`if not effective: no-receipt-write / elif call_lines: guard-adopted / elif
load_lines: guard-loaded-uncalled / else: unguarded-writer`, and
`guard_call_before_write` is `call_lines[0] <= write_lines[0]` (block `:345-346`).
`call_lines` includes entries of form `def:guard_receipt` (the `def` line itself)
and `subscript:guard_receipt` (the call inside the helper body). Therefore a
runner whose guard call exists **only inside the helper body** — or whose helper
is invoked only *after* the write, or only under a flag — reports
`guard-adopted`, `hazard: false`, `guard_call_before_write: true`. Evidence: the
first three rows of §3.4's trap table (the fourth, `os.replace`, is answered
correctly), O03's F03/F04 (§3.4), and O08's T2
(§3.4b — a verdict O08 lists under `forbidden_wrong_green`). O03 names exactly
these as controls (`op/O03-selftest.md:41-42,254`: "call-not-definition check
(F03)", "guard-order check (F04)"). Scope correction from §3.4b: a helper that
only *loads* the guard and is never called is classified honestly
(`guard-loaded-uncalled`), so the trigger is the in-`def` guard-call idiom or a
conditional/post-write invocation, not "defines any helper". Second facet: the
recorded signals cannot be read back to recover the truth — for O08's T2 the
core emits `guard_call_conditional: false` although the call sits inside
`if args.guarded:` (`:61`), and for F04 `pre_write: true` although the
invocation `:11` follows the write `:10`. Why it matters operationally: the class
field drives routing — `guard-adopted` sends a runner to the in-tree
`REFRESH_RECEIPTS=1` refresh protocol, and a runner of this shape has *no*
refusal path on its writing path, so running it in-tree is exactly the
F-C13-1 recurrence. On the filed tree the defect is latent (every one of the 17
real adoptions also holds a genuine pre-write invocation at Δ ∈ {1,3}, §2.2), so
the 28-row result in §3.3 stands. Required fix: exclude definition-site entries
from `call_lines` (or tag them), require an invocation with `line < write_line`,
grade a flag-conditional invocation as at most `guard-loaded-uncalled` unless the
branch provably dominates the write, and make the conditional/order fields
report the truth.

### O07-D6 — `target_resolved` is mangled in 15 of 28 rows

In the real-tree run, 15 rows report
`target_resolved: "ROOT/reports/round-N/run-validation.py/reports/round-<N>/validation.json"`
— the placeholder `env["__file__"]` string (`op/O01-impl.md:188`) is
concatenated with the resolved relative path instead of being substituted
(build at fragment `:275`; the same mangled values are visible in O01's own
sample output, e.g. `op/O01-impl.md:505,525,545,565,593`). Affected rounds: 5,
6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 21; the other 13 rows are
correct (r19, r22–r33 mostly). Classification is unaffected (class comes from
site presence), but the inventory's promise is to name *which file* each runner
writes; a consumer that opens `target_resolved` gets a path that does not exist.
Required fix: emit the repo-relative receipt path, or emit the placeholder-free
`target_expr` only.

### O07-D7 — class vocabulary diverges from O03's control contract (F09, F12)

O03 requires `embedded-write-suspect` (F09) and `writes-other-round-receipt`
(F12); the core's `CLASSES` tuple (`op/O01-impl.md:110-117`) contains neither, so it
answers `unguarded-writer` for both. These are **not** false greens — the core's
answers are safe in direction and it correctly keeps `hazard: true` — but they
break O03's stated control list, and for F12 they lose the distinction that the
write targets *another round's* receipt (the runner's own receipt is untouched,
so attributing the row to the writer without naming the target is misleading;
`target_expr` was empty in my run of that fixture). Either O03's expectation list
or the tool's vocabulary must move; the reconciliation is the integrator's call,
not mine.

## 5. Acceptance contract for the landed tool

### 5.1 Requirements

1. Coverage 28/28 filed runners, each row carrying its path and a positive class;
   unknown rows are `could-not-evaluate`, never omitted.
2. Class partition **17 adopted / 11 unguarded** (§2.1/§2.2). A different total is
   a defect, not a taxonomy preference.
3. Write anchors equal the oracle's `sink_write_line` (r19 `:21`, not `:19`).
4. Adoption requires an **invocation that dominates the write** — the §3.4 traps
   must classify as hazards, not as adopted (O07-D5).
5. `--selftest` green over O03's 12 controls, with F03/F04/F09/F12 answered as
   O03 names them (or with the contract amended and the amendment recorded).
6. `--json` machine-readable with a stable row key (`round` or `path`);
   `target_resolved` must be a real path (O07-D6).

### 5.2 The claim's threshold text needs correcting before it can count green

`claims.json:51` reads "selftest N/N green; inventory covers 100% of filed
runners; **the four named hazards classified**; zero false positives on
guarded/non-runner fixtures". The four-hazard clause is falsified by the oracle:
the class is 11 (O07-D2) and one of the four is not a hazard (O07-D1). As
written, a tool that reproduces the claim's four-row list would satisfy the
threshold while leaving eight receipts unprotected.

### 5.3 The comparator (re-runnable; needs only O02's bytes)

Full script `.scratch/round-34-O07/verify_o07.py` extracts the tool block from
`op/O02-tool-source.md`, runs `--selftest` and `--json` on the extracted copy
outside the tree's tool path, parses `op/O04-predicted-inventory.md`, and diffs
all three against `oracle.tsv`:

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B .scratch/round-34-O07/verify_o07.py
```

If `.scratch` is cleaned, the oracle is rebuildable from §2 (28 rows, with the
digest anchor `9252d043…` to check the rebuild against), and the two synthetic
trees are rebuildable from §3.4's fixture names — the fixtures live in
`op/O03-selftest.md`'s python block and my traps are transcribed in the §3.4
trap table. Both trees are self-contained (they need no repo files).

### 5.4 Verdict map — symptom in a tool's output → defect id

| symptom | defect |
|---|---|
| r26 classified unguarded | O07-D1 |
| unguarded set ≠ the 11 in §2.1 (e.g. missing the alias receivers) | O07-D2 / O07-D3a |
| r19 reported `no-receipt-write`, or anchored at `:19` | O07-D3b |
| r14–r18 / r20 reported unguarded | O07-D3c |
| r21 reported adopted | O07-D3d |
| a defined-but-uncalled, after-write, or flag-conditional guard reported adopted | **O07-D5** (O08 T2 + O03 F03/F04) |
| `guard_call_conditional: false` on a call inside a flag branch | O07-D5 (second facet) |
| `target_resolved` containing `round-N/run-validation.py/` | O07-D6 |
| F09/F12 answered outside O03's vocabulary | O07-D7 |
| coverage < 28 rows | O07-D2 |

## 6. F-C13-1 compliance and byte preservation (this seat)

- **No filed round runner was executed.** The only programs I ran over round
  bytes were my own `.scratch` readers, `grep`/`sed`, `git`, the guard's
  `--selftest`/CLI (no writes outside a disposable `.scratch` fixture,
  `tools/harness/receipt_guard.py:201-351`), and **O01's extracted core**, which
  I read in full before running and whose only match for `write_text`/`subprocess`
  is as pattern *strings* it searches for. The four synthetic runners of §3.4
  were executed **by nothing**: the core only reads and parses them.
  `reports/round-34/run-validation.py` does not exist, so the ABSOLUTE rule is
  vacuous here.
- **Nothing filed was written.**
  `git hash-object reports/round-<N>/validation.json` ==
  `git rev-parse HEAD:reports/round-<N>/validation.json` for
  N ∈ {5,6,7,8,9,10,11,12,19,21,26,29,32} — all thirteen identical;
  `git status --short` → only `?? reports/round-34/`.
- Only this fragment plus `.scratch/round-34-O07/**` were created.

## 7. For the integrator

1. The claim's "before" block (`claims.json:43`) and the threshold text
   (`:51`) carry the stale four-hazard list; read them with O07-D1/D2 applied.
2. O-claim status today: inventory **verified on the real tree**, tool CLI
   **not landed**, control contract **failing on 4 of 12 fixtures** (O07-D5/D7).
   Landing O02's bytes without fixing O07-D5 ships a detector that cannot fail
   its own O03 controls.
3. `review/R04-o-review.md` and `review/R05-o-review.md` are the O-block
   reviewers; if either asserts a hazard total different from §2.1, §2.1 is the
   re-measure to run — and if either claims the traps pass, §3.4 is the
   counter-evidence.

## Owed

| owed path / item | owner | why |
|---|---|---|
| `reports/round-34/op/O02-tool-source.md` | O02 | never landed; without it `--selftest` and `--json` cannot be run and the two counting commands stay `could-not-evaluate` (§3.2, §3.5) |
| `tools/harness/receipt_guard_adoption.py` (landed tool, with the O07-D5/O07-D6 fixes) | integrator | the claim's deliverable; §5.1 is its acceptance contract |
| re-run of `.scratch/round-34-O07/verify_o07.py` once O02 lands | integrator / follow-up verifier | produces the O07 verdict on the actual tool and the O04 diff; verdict map in §5.4 |
| `LOG.md` errata row (O07-D1/D2) + corrected `claims.json:51` threshold wording | integrator | shared bookkeeping and filed `claims.json` bytes are never written by seats |
| SCORECARD standing-debt sizing (11, not 3) | integrator | the round-33 incident sampled a 11-runner class |

## Citations

- `reports/round-34/targets.json:50` (O07 mission/out), `:44-53` (O-seat block), `:5-12` (`shared_rules`).
- `reports/round-34/claims.json:41` (claim O), `:43` (before-block), `:45` (after_required), `:46-50` (counting commands), `:51` (thresholds), `:68-74` (non-goals).
- `LOG.md:3548` (F-C13-1 heading), `:3551-3553` (window/restore), `:3557-3560` (mechanism + r26 claim), `:3565-3566` (standing debt).
- `tools/harness/receipt_guard.py` (373 lines, sha256 `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`): `:34-36`, `:144-149`, `:152-168`, `:201-351`.
- Unguarded rows (§2.1): r5`:194`, r6`:336`, r7`:1171`, r8`:1486` (`:99`,`:1485`), r9`:1910` (`:127`), r10`:1054` (`:60`), r11`:1740` (`:125`), r12`:1071` (`:18`,`:1069`), r19`:21` (`:2`,`:19`), r21`:1115` (`:20`,`:1113`,`:474`,`:1106`), r29`:922` (`:23`,`:89-92`).
- Adopted rows (§2.2): r14`:25,:414,:420,:716,:717`; r15`:44,:1038,:1044,:1337,:1345,:1346`; r16`:57,:999,:1005,:1264,:1265`; r17`:68,:1118,:1124,:1430,:1431`; r18`:67,:1512,:1518,:1850,:1851`; r20`:57,:1279,:1285,:1484,:1485`; r22`:827-829,:911,:921,:922`; r23`:1064-1066,:1094,:1097`; r24`:1151-1153,:1181,:1184`; r25`:1108-1110,:1142,:1145`; r26`:1855-1857,:1905-1909`; r27`:1853-1855,:1904,:1907`; r28`:1996-1998,:2095,:2098`; r30`:883-885,:903,:922,:923`; r31`:1118-1120,:1139,:1158,:1159`; r32`:1102-1104,:1123,:1142,:1143`; r33`:1441-1443,:1459,:1470,:1471`.
- `reports/round-34/op/O04-predicted-inventory.md` (sha256 `7f0b9998…`), JSON `:36-80` (28 rows, `counts` `:41-42`, `known_hazards` `:73-78`).
- `reports/round-34/op/O01-impl.md` (sha256 `3b038b3c…`), fenced python block at fragment `:76-446` (fences `:75`/`:447`) = 371 lines: `:188` (`env["__file__"]` placeholder), `:275` (`target_resolved` build), `:26`/`:263` (pattern strings only), `:110-117` (`CLASSES`), fragment `:397-407` = block `:322-332` (classification), fragment `:420-421` = block `:345-346` (pre-write test), fragment `:444-446` (`__main__`), json sample block `:494-1168` with mangled paths `:505,:525,:545,:565,:593`.
- `reports/round-34/op/O03-selftest.md`: expectation table `:39-50`, `FIXTURES` block `:57-162`, control-count prose `:227-229`, "call-not-definition check (F03)" / "guard-order check (F04)" `:254`.
- `reports/round-34/op/O08-traps.md` (independent traps; expectation table `:44-56`, census correction `:408-461`), `.scratch/o08-traps/EXPECTATIONS.json` (`traps[]` with `forbidden_wrong_green`), `.scratch/o08-traps/tree/reports/round-90{1,2,3,4}/run-validation.py` (T1 `:22-29` loader-only helper, write `:59`; T2 `:55-64` flag-conditional call `:61`, write `:63`; T3 `os.replace` `:56-57`), `.scratch/o08-traps/tree/tools/cache-export.py` (C−).
- `reports/round-34/op/O06-scribe.md:69-110` (census compared in my earlier pass), `:118-142` (its r26 reclassification), `:73-74` (O07-D4 errata).
- `reports/round-34/op/O05-routing.md` (373 lines; 11 unguarded routing rows agree with §2.1's anchors on text check).
- `reports/round-34/calib/C07-verify-survey.md:109` (SKILL box-1 pin of the guard digest).
- Commands run (all at HEAD `da68a6d`, `TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1`): `ls -1 reports/round-*/run-validation.py` (28); `python3 -B .scratch/round-34-O07/{census.py,census2.py,census3.py}`; `sed -n '<line>p'` for every §2.1 row; `grep -n/-c "receipt_guard|REFRESH_RECEIPTS|guard_receipt|round_runner_main"` across all 28; `python3 -B .scratch/round-34-O07/verify_o07.py` (O06 28 rows 0 defects; O04 diff; O02 absent); `python3 -B .scratch/round-34-O07/landed-o01/receipt_guard_adoption_core.py $PWD` → exit 0, `runner_count 28`, `{'unguarded-writer': 11, 'guard-adopted': 17}` (output sha256 `027983b1…`); same core on `.scratch/round-34-O07/trap` → `runner_count 4`, output sha256 `6994672a…`; same core on `.scratch/round-34-O07/o03fixtures` → `runner_count 11`, output sha256 `cdd01fc2…`; same core on `.scratch/o08-traps/tree` → `class_counts {'guard-loaded-uncalled': 2, 'guard-adopted': 2}`, output sha256 `43c48cb7…`(see `.scratch/round-34-O07/o01-o08traps.json`); `python3 -B tools/harness/receipt_guard.py --selftest` → exit 0, 45/45; `python3 -B tools/harness/receipt_guard.py reports/round-<N>/validation.json` ×13 → exit 3; `sha256sum` of the guard, both fragment inputs and my outputs; `git hash-object` vs `git rev-parse HEAD:` for the 13 receipts; `git status --short`; `git rev-parse --short HEAD` → `da68a6d`; tree-wide fenced-block scan of `reports/round-34/*/*.md` (two large blocks, no `argparse`/`--selftest`/`--json` in either); `find reports/round-34 -type f` polls.
- Seat-produced scratch artifacts (not deliverables): `.scratch/round-34-O07/{census.py,census2.py,census3.py,census.json,census2.json,census3.json,oracle.tsv,verify_o07.py,guard-selftest.json,landed-o01/receipt_guard_adoption_core.py,o01-run.json,o01-trap.json,o01-o03fixtures.json,trap/**,o03fixtures/**}`.
