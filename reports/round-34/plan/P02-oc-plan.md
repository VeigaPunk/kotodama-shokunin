- Seat: P02 | planner | O | date 2026-10-19 | baseline da68a6d

# P02 — execution plans for claims O and C

Mission (`reports/round-34/targets.json`, seat P02): "Execution plans for claims O and
C: the instrument's architecture (stdlib-only, mirrors the round-25 audit-tool style),
selftest control list, and the durable-receipt shapes."

**Method.** Read the round-34 contract (`REGIMEN.md`, `claims.json`, `targets.json`),
then measured every surface the two plans bind: the filed runner census, the guard's
own behaviour at HEAD (read-only), the box-1 tool at live bytes, the round-33→HEAD
byte deltas for `SKILL.md` / `README.md` / `AGENTS.md`. No file was written outside
this fragment; every command is read-only. K03/K04 did not exist at my reads (see
`## Owed`), so the two censuses in §1.4 and §2.2 are measured here, not imported.

## 1. Claim O — `tools/harness/receipt_guard_adoption.py`

### 1.0 Two binding constraints that shape every step

1. **The tool file is a shared-file change.** Claim O's `after_required` says "the tool
   is durable" (`reports/round-34/claims.json`, claim O), but the round's shared rules
   say seats write only their assigned `out` paths and shared files are drafted as
   before/after text for the integrator (`reports/round-34/targets.json` → `shared_rules`
   bullet 2). So O02's fragment carries the **full tool source as a fenced block**
   (`op/O02-tool-source.md`); the integrator applies it to
   `tools/harness/receipt_guard_adoption.py`. Every "run the tool" command below is
   executed against a scratch materialization under `$TMPDIR` (the regimen's own
   `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`), and the inventory receipt
   records **both** the fragment path and the applied tool's sha256, so a drift between
   the draft and the applied bytes is detectable.
2. **The guard exists but its protection is not adoption.** `python3 -B
   tools/harness/receipt_guard.py reports/round-26/validation.json` → exit 3,
   `receipt_guard: refusing overwrite path=reports/round-26/validation.json
   committed_sha=da68a6d705e41f369f21e8607bfaab5b54077f84 [RECEIPT-GUARD-COMMITTED]`
   (measured for r5, r6, r7, r12, r19, r21, r26, r29, r32 — all exit 3). That refusal is
   a property of the *guard*, not evidence that a runner consults it: r5 writes at
   `reports/round-5/run-validation.py:194` and never calls the guard. The instrument
   must therefore classify **call sites on the write path**, never the mere existence of
   the guard.

### 1.1 Architecture (stdlib-only, round-25 audit-tool style)

Style reference: `reports/round-25/audit/x45-lessons-pointer-audit.py` — module docstring
that names its numbered questions (X45-P1..P3, `:11-17`), "Stdlib only. Opens no file for
writing; `--json` is a stdout receipt" (`:18`), `ROOT` resolved from `__file__`
(`:33`), `--selftest` / `--json` flags, exit 0/1/2. The adoption instrument takes the
same shape plus `receipt_guard.py`'s receipt convention (`controls` / `controls_passed`
/ `controls_total` / `selftest_passed` / `limits`, `tools/harness/receipt_guard.py:345-348`,
exit `0 if receipt["selftest_passed"] else 1` at `:365`) and its `.scratch`-rooted
fixture idiom (`receipt_guard.py:212-213`).

```
tools/harness/receipt_guard_adoption.py
  docstring      purpose, the classification lattice, the enumerated non-claims, usage, exit codes
  ROOT           Path(__file__).resolve().parents[2]           # repo root, same idiom as receipt_guard
  imports        argparse, ast, hashlib, json, os, pathlib, re, sys, tempfile  (no third-party, no clock, no env)
  --- enumeration
  runner_paths(root)          -> sorted numeric reports/round-*/run-validation.py (glob, never a list)
  round_gaps(paths)           -> rounds 1..max without a runner (honest coverage row)
  --- parsing (ast, one pass per file; no import, no exec of the target)
  module_string_map(tree)     -> name -> literal string (OUTPUT, OUTPUT_REL, RECEIPT, …) + one alias hop
  receipt_targets(...)        -> str constants matching reports/round-\d+/validation\.json
  write_sites(tree, map)      -> Call nodes: Path.write_text / open(...,'w'|'a') / json.dump to a resolved target
  guard_load_site(tree)       -> runpy.run_path("…receipt_guard.py"), importlib.util.spec_from_file_location,
                                 sys.path insert + import receipt_guard, from … import receipt_guard
  guard_call_sites(tree)      -> guard_receipt(…) / round_runner_main(…) / guard_preflight() / ns["guard_receipt"](…)
  guard_placement(…, write)   -> same_function | preflight_function | mention_only | none   (rule in §1.2)
  classification(...)         -> one class per runner (§1.2 lattice) + attributes
  --- output
  inventory(root)             -> deterministic dict (sorted keys, relative posix paths, file:line strings)
  render_json(inv) / render_text(inv)
  selftest()                  -> fixture tree under tempfile.TemporaryDirectory(dir=<scratch>) → controls receipt
  main(argv)                  -> exit 0 inventory/all controls pass; 1 one or more selftest controls failed;
                                 2 could-not-evaluate (root absent/not a directory, unreadable/unparsable runner,
                                 census count mismatch), 2 argparse usage error
CLI: receipt_guard_adoption.py [--json] [--root DIR] [--selftest]
```

Read-only invariant, stated in the docstring and asserted by a control: the tool opens
no path under `reports/` for writing, never imports or executes a runner, and its only
side effect outside the fixture is stdout (receipt) — the durable file is the caller's
redirect, as in `x48-v3-supersession-audit.py:21` ("the receipt is the caller's stdout
redirect").

Named checks (round-25 style, cited by id in the receipt):

- **RGA-P1 census completeness** — the classified count equals the glob count equals
  `ls -d reports/round-*/run-validation.py | wc -l` (28 at HEAD, measured).
- **RGA-P2 target resolution** — every runner's receipt target resolves in-tree; an
  unresolved target is a `could-not-evaluate` row, never silently "safe".
- **RGA-P3 adoption on the write path** — adopted iff a guard call site is on the
  publish path (§1.2); a string mention is not adoption.
- **RGA-P4 declared-hazard reconciliation** — the four hazards named by
  `reports/round-33/claims.json`/`LOG.md:3556-3560` (r5, r6, r7, r26) each get a
  declared-vs-measured row; disagreement is a finding, not a silent re-classification.
- **RGA-P5 hazard legend** — every unguarded self-writer is listed with `file:line` of
  its write site so the routing draft can name its protocol per runner.

### 1.2 Classification contract

Lattice, in precedence order (first match wins; each runner gets exactly one class):

| class | rule | hazard |
|---|---|---|
| `unresolved` | census found the file but the AST parse or target resolution failed | could-not-evaluate — never "safe" |
| `no-receipt-write` | no write site resolves to a `reports/round-*/validation.json` target | none (does not publish a receipt) |
| `adopted-guarded-write` | a write site exists **and** `guard_placement ∈ {same_function, preflight_function}` | mitigated — the guard refuses at HEAD unless `REFRESH_RECEIPTS=1` |
| `unguarded-self-write` | a write site exists, no guard on the publish path, target is the runner's own round receipt | **the F-C13-1 class** |
| `delegating-runner` | attribute on any class: the runner's argv names another `reports/round-*/run-validation.py` | routing input (isolated-copy protocol) |

`guard_placement` rule (deterministic, approximate, declared as such in `limits`):

- `same_function` — guard call and write site inside one function, guard line < write line
  (covers r22 `:921` → `:922`, r25 `:1142` → `:1145`, r26 `:1906` → `:1909`, r30 `:922` → `:923`,
  r32 `:1142` → `:1143`, r33 `:1470` → `:1471`).
- `preflight_function` — the guard call is inside a function whose name is called from
  `main()` (or the write's function) before the write (covers r14 `:413` → `:717`, r15
  `:1037` → `:1346`, r16 `:998` → `:1265`, r17 `:1117` → `:1431`, r18 `:1511` → `:1851`,
  r20 `:1278` → `:1485`, and the r23/r24/r27/r28/r31 variants).
- `mention_only` — the only hits are: a subprocess entry running
  `tools/harness/receipt_guard.py --selftest` (e.g. r26's command list `:199`), a docstring
  or comment, or an import without a call → **not** adopted.
- `none` — no mention at all.

Non-claims the tool must print verbatim in `limits` (each is a control in §1.3):
adoption classification is static — it does not prove the guard call is reached at
runtime on every path; a runner's own `--check` branch is not evidence of adoption;
the census covers `reports/round-*/run-validation.py` only, so a filed helper that
writes a receipt (e.g. `reports/round-26/lessons/c51-revision-audit.py`) is out of
scope by construction and must be listed as `out_of_scope` rather than omitted;
the tool decides no admission, promotion or repair — the runners are filed bytes and
are not edited (PREVENTION, `LOG.md:3563-3567`).

### 1.3 Selftest control list (13 controls, fixture root, no repo write)

Fixtures are tiny synthetic trees under `tempfile.TemporaryDirectory(dir=<repo>/.scratch)`
mirroring `reports/round-99/run-validation.py` shapes; the tool is pointed at them with
`--root`. Every control asserts class **and** the reported `file:line`.

| # | control | fixture | assertion |
|---|---|---|---|
| C1 | `adopted-runpy-positive` | copies r32's shape: `runpy.run_path("…receipt_guard.py")` + `guard_receipt()` before `safe_path(OUTPUT).write_text(rendered)` | `adopted-guarded-write`; **not** in the hazard list (claim O's positive control) |
| C2 | `adopted-preflight-positive` | copies r20's `guard_preflight()` def + call before `(ROOT/OUTPUT).write_text` | `adopted-guarded-write` |
| C3 | `unguarded-inline-hazard` | `(HERE / "validation.json").write_text(json.dumps(receipt))` | `unguarded-self-write` + exact write line |
| C4 | `unguarded-output-rel-alias` | `OUTPUT_REL = "reports/round-99/validation.json"` … `output = ROOT / OUTPUT_REL; output.write_text(…)` (the r8–r11 idiom, `reports/round-8/run-validation.py:99,1485-1486`) | `unguarded-self-write` — **false-negative control**; a regex-first classifier misses this |
| C5 | `mention-only-selftest-entry` | writes its receipt but only lists `("tools/harness/receipt_guard.py", "--selftest")` in a command table (the r26 `:199` idiom) | `unguarded-self-write`, **not** adopted — false-positive control for string mentions |
| C6 | `import-without-call` | loads the guard module, never calls a guard function | not adopted |
| C7 | `non-runner-json-writer` | `reports/round-99/audit/helper.py` writing JSON | **not enumerated at all** (claim O's second negative control) |
| C8 | `check-only-no-write` | argparse `--check` print, no write site | `no-receipt-write` |
| C9 | `delegating-clone-runner` | subprocess argv naming `reports/round-98/run-validation.py` | class per write rule **and** `delegating-runner` attribute set |
| C10 | `docstring-mention-only` | prose mention of `receipt_guard` in a docstring | not adopted |
| C11 | `deterministic-twice` | C1 fixture, two invocations | byte-identical JSON (no clock, no env, no absolute paths) |
| C12 | `missing-root-could-not-evaluate` | `--root /nonexistent` | exit 2, not 0 |
| C13 | `live-census-self-consistency` | the real repo root | `classified == glob count == shell count`; gap rounds reported |

Selftest receipt shape mirrors the guard's (`controls`, `controls_passed`,
`controls_total`, `selftest_passed`, `limits`) and is quoted inside O03's fragment; the
exit code is 0 iff all 13 pass.

### 1.4 Predicted inventory (O04's reconciliation target) — measured here, read-only

Measured by an ad-hoc AST/regex scan of the filed bytes (command in §Citations):
**28** `reports/round-*/run-validation.py` on disk; rounds **1, 2, 3, 4, 13** have no
runner.

| class | count | runners (write site / guard site) |
|---|---|---|
| `adopted-guarded-write` | 17 | r14 `:413→:717`; r15 `:1037→:1346`; r16 `:998→:1265`; r17 `:1117→:1431`; r18 `:1511→:1851`; r20 `:1278→:1485`; r22 `:921→:922`; r23 `:1094→:1097`; r24 `:1181→:1184`; r25 `:1142→:1145`; r26 `:1906→:1909`; r27 `:1904→:1907`; r28 `:2095→:2098`; r30 `:922→:923`; r31 `:1158→:1159`; r32 `:1142→:1143`; r33 `:1470→:1471` |
| `unguarded-self-write` | 11 | r5 `:194`; r6 `:336`; r7 `:1171`; r8 `:1485-1486` (`OUTPUT_REL :99`); r9 `:1909-1910`; r10 `:1053-1054`; r11 `:1738-1740`; r12 `:1069-1072`; r19 `:19-21`; r21 `:1113-1116`; r29 `:922` |
| `no-receipt-write` | 0 | — |
| `unresolved` | 0 | — |

Declared-hazard reconciliation (RGA-P4), with the divergence already visible:

| hazard | declared (source) | measured | verdict |
|---|---|---|---|
| r5 | unguarded in-place write (`LOG.md:3556-3558`; `reports/round-5/run-validation.py:194`) | `unguarded-self-write` | agrees |
| r6 | same (`LOG.md:3558`; `:336`) | `unguarded-self-write` | agrees |
| r7 | same (`LOG.md:3557`; `:1171`) | `unguarded-self-write` | agrees |
| r26 | "the r26 runner carries the same hazard (`:90`, `:1909`)" (`LOG.md:3559-3560`) | `adopted-guarded-write`: `guard_receipt()` at `reports/round-26/run-validation.py:1906` wraps the write at `:1909`; `--check` at `:1871` | **diverges** — the LOG cites r26's *write location*, but r26 **is** guarded; its residual exposure is the README blob pin (A09-F1/E1), not an unguarded write. Resolution owner: O07/O09; `to-verify` in this plan which reading the round files as authoritative |

Consequence for O04/O07: the inventory must report the measured class and carry the
divergence as a finding with the two citations above, **not** re-label r26 as a hazard
to match the claim's prose, and not quietly drop it either. Both readings stay visible;
the receipt states which bytes each was read from.

Two further measured facts the routing draft needs:

- r12's own `limits` text already states the rule the routing will generalize:
  "does not invoke historical round runners, which would rewrite their validation.json
  files" (`reports/round-12/run-validation.py:1062`); r5 states the isolated-copy
  convention (`reports/round-5/run-validation.py:193`); r21 documents the clone protocol
  with `REFRESH_RECEIPTS=1` scoped to clones (`.scratch/round-21`,
  `reports/round-21/run-validation.py:1106`) → `delegating-runner` attribute true for r21.
- The incident's recovery route is already precedented: `.scratch/c05-iso/` isolated
  `git archive` run (`LOG.md:3554-3555`) — exactly the protocol the routing drafts for
  the 11 unguarded runners.

### 1.5 Durable-receipt shapes

**(a) Tool source (O02, drafted):** `reports/round-34/op/O02-tool-source.md` — fenced
before/after block for the new file, plus the tool's own `--selftest` receipt quoted, and
`tool_sha256` of the draft bytes so the integrator's applied bytes can be compared.

**(b) Inventory (O04):** `reports/round-34/op/receipt-guard-adoption.json` — the
redirected stdout of `receipt_guard_adoption.py --json`, deterministic and
digest-pinable:

```
{"tool","tool_path","tool_sha256","tool_draft","date","baseline_commit",
 "census":{"runners_on_disk":28,"classified":28,"unresolved":0,
           "glob_command":"ls -d reports/round-*/run-validation.py | wc -l",
           "rounds_without_runner":[1,2,3,4,13]},
 "classes":{"adopted-guarded-write":17,"unguarded-self-write":11,
            "no-receipt-write":0,"unresolved":0},
 "runners":[{"round","path","class","runner_sha256","output_target",
             "write_sites":["path:line"],"guard_load_site","guard_call_sites",
             "guard_placement","mode_flags","delegating_runner"}],
 "declared_hazards":[{"round","declared_class","declared_source","measured_class","agrees","note"}],
 "out_of_scope":[{"path","why"}],
 "checks":{"RGA-P1":…,"RGA-P2":…,"RGA-P3":…,"RGA-P4":…,"RGA-P5":…},
 "findings":[{"id","class","detail","evidence"}],
 "limits":[…]}
```
Every digest in it is a sha256 of bytes on disk at the run; no `mtime`, no wall clock
beyond the declared `date`, sorted keys, relative posix paths (so re-running on a copy
reproduces it byte-for-byte — C11).

**(c) Prose receipt (O04):** `reports/round-34/op/O04-inventory-receipt.md` — the five
RGA-P rows, the predicted-vs-measured reconciliation table of §1.4 (including the r26
divergence), the selftest transcript, and the sha256 of the JSON receipt.

**(d) Routing draft (O05):** `reports/round-34/op/O05-routing.md` — two protocols:
*guarded re-run* for the 17 adopted runners (in-tree re-run is safe by refusal; the only
sanctioned overwrite is `REFRESH_RECEIPTS=1` inside an isolated clone, recorded as a new
snapshot, never an in-place filed-byte edit) and *isolated-copy-only* for the 11
unguarded ones (`git archive <baseline>` → run under `.scratch/…`, per `LOG.md:3554-3555`
and `:3563-3567`), each row naming the runner, its write site and its owner.

## 2. Claim C — box-1 durable re-survey + A09 R1–R8 anchor reissue

### 2.1 Box-1 re-survey (C01/C02/C05)

Live measurement at HEAD (`python3 -B reports/round-30/craft/box1-survey.py`, exit 0):

```
{"date":"2026-10-18","named":28,"resolvable":28,"unnamed_in_skill":[],
 "skill_sha256":"f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b"}
```
— exactly claim C's target digest (`reports/round-34/claims.json`, claim C), 28/28
resolvable, `SKILL.md` 732 lines, `sha256sum SKILL.md` → `f9bd07c2…`.

Traps the durable receipt must handle honestly:

- The tool self-reports a **hard-coded** `date: "2026-10-18"` (`reports/round-30/craft/box1-survey.py:8`)
  and names its fields `named` / `resolvable`, while the last filed receipt uses
  `named_in_skill` / `resolvable` (`reports/round-30/craft/box1-landed-survey.json:5`).
  The new receipt keeps the tool's own key names **and** records the mapping, rather than
  silently renaming (a renamed field is how a count drifts unnoticed).
- The 28 named paths are not in the r30 receipt; the new receipt adds the sorted list
  (measured: the 28 `tools/**.py` paths, the `tools/harness/receipt_guard.py` /
  `tools/source-audit-inventory.py` members included), so a future `named_in_skill`
  move is diffable rather than opaque.
- Supersede relation, recorded not edited: `83b0a78a…` (r30 receipt,
  `reports/round-30/craft/box1-landed-survey.json:4`) and the r32 closure at `79fe91d3…`
  (`reports/round-32/final-dossier.md:46`) read as **superseded readings**; no filed byte
  is touched.

Shapes:

- `reports/round-34/craft/box1-resurvey-durable.json` — `date`, `mode:"post-round-33"`,
  `skill_sha256`, `skill_lines`, `named`, `resolvable`, `unresolvable`, `named_paths[]`,
  `command`, `exit_code`, `tool`, `tool_sha256` (digest of
  `reports/round-30/craft/box1-survey.py`), `supersedes` (the two digests above with
  their paths), `limits`.
- `reports/round-34/craft/C02-receipt.md` — transcript, re-run command, and the control
  that the filed r30 receipt bytes are unchanged (`git hash-object` vs
  `git rev-parse HEAD:<path>`).

### 2.2 A09 R1–R8 anchor reissue (C03): method, then the measured map

The old anchors were recorded against the pre-admission bytes (SKILL.md 715 lines /
`79fe91d3…`, README 346 lines / `ec7469da…` — `reports/round-33/adj/A09-pins.md:19-20`);
the round-33 admission commit `da68a6d` moved them (`git diff --numstat 139e3b6 da68a6d`
→ `35 18 SKILL.md`, `130 28 corpus/lessons/README.md`, `0 2 AGENTS.md`). Method for
C03 (re-runnable, no guessing):

1. `git diff --unified=0 139e3b6 da68a6d -- SKILL.md` → hunk offsets; an anchor's new
   address is old + cumulative offset of the hunks strictly above it.
   Measured hunks (old line → new lines, offset after): `:128→:128` (0), `:479/:481/:483/:486/:488/:491/:501`
   (all in place, 0), `:584→:584-586` (**+2**), `:694-697→:696-700` (+3),
   `:699-700→:702-705` (+5), `:704→:709-720` (**+16**), `:714-715→:730-732` (**+17 = 732-715**).
2. Verify every new address with grep on the live file (not by trusting the arithmetic);
3. same procedure for `corpus/lessons/README.md` (new digest `f752e1d7…`, blob
   `73f3e1bd…`, 448 lines, 33 rows = 33 files);
4. record each old anchor as a **superseded reading**, never an edit of
   `reports/round-33/adj/A09-pins.md`.

The measured map, ready for C03's table (`old → new → owning row`, each row to be
re-verified by grep when the fragment is written):

| owning row | old anchor (r33 bytes) | new anchor (HEAD) | live check |
|---|---|---|---|
| R5 (self-cites) | `SKILL.md:47` cited at `:149`, `:183` | unchanged: `SKILL.md:47`, cites at `:149`, `:183` | `grep -n "SKILL\.md:47" SKILL.md` → `149`, `183` — identical at `139e3b6` |
| R5 (fix targets) | `:128`, `:486`, `:488`, `:501` (FD-N4/N5 + C14 Fixes) | same addresses, content replaced in place | hunk list §2.2 step 1 |
| R5 (checklist anchor) | heading `:522`, last item `:534`, `## Corpus map` `:536` | unchanged `:522`, `:534`, `:536` (all above the first shift at `:584`) | `sed -n '522p;534p;536p' SKILL.md` |
| R5 (AGENTS.md anchor) | `AGENTS.md:42` "after :534" | **excised** — `AGENTS.md` is 40 lines and carries no such instruction | `wc -l AGENTS.md` → 40; `grep -n "SKILL.md" AGENTS.md` → no match; excision recorded `LOG.md:3584-3586` |
| R5 (D3 heading) | `:660` | `:662` | `sed -n '662p' SKILL.md` → `## Source-bounded culture drill — D3 (round 7)` |
| R5 (r31 checklist item) | `:713-715` | `:729-732` | `sed -n '729,732p' SKILL.md` |
| R5 (round-7 pointer) | `:710` | `:726` | `sed -n '726p' SKILL.md` |
| R6 (README arithmetic) | `:97` rows/files, `:207` queue arithmetic | `:105` ("**Rows: 33. Files: 33.**"), `:254` ("Rows: **78**. Of the 33 index rows, **30 carry at least one question**") | `c31` → exit 0, `findings: 0`, `C34b_prose_arithmetic PASS` |
| R3 (SKILL digests) | `79fe91d3…` at 8 sites | `f9bd07c2…`; every old site a superseded reading | `grep -rln 79fe91d3 reports/round-3[012]/` → 7 files (`round-31/validation.json`, `round-32/{validation.json,dossier-d11-shonen-boxes.md,dossier-d12-capability-inventory.md,dossier-d13-operator-decisions.md,final-dossier.md,scribe/fragment-ledger.md}`) |
| R4 (box-1) | `83b0a78a…` (r30 receipt) | `f9bd07c2…` (28/28) — §2.1 | `python3 -B reports/round-30/craft/box1-survey.py` exit 0 |
| R7 (peer instruments) | `x45` exit 1; `x57 --selftest` 34/37 | `x45` exit **0** (fixed by the round-33 delta); `x57 --selftest` **28/37** at HEAD | `python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py --json` exit 0; `python3 -B reports/round-27/audit/x57-lessons-audit.py --selftest` → `"passed": 28, "total": 37` |
| R8 (landing order) | README rows vs `round-33.md` | **open**: `corpus/lessons/round-33.md` does not exist at HEAD; the revision-3 stamp covers rounds 26–32 (32 lesson files + README = 33 glob hits), so the round-33 lesson landing re-opens `C31-1` with exactly one orphan | `ls corpus/lessons/round-33.md` → No such file; `ls corpus/lessons/*.md | wc -l` → 33; README `:105` claims 33 rows/33 files (`to-verify`: which round files the round-33 lesson, and whether it lands before round 34's admission) |
| R1/R2 (README blob + digest) | blob `a3187055…` / `ec7469da…` | blob `73f3e1bd…` / sha256 `f752e1d7…`; the r26 runner's `README_BASELINE_BLOB` (`reports/round-26/run-validation.py:97`) is superseded, never re-run in-tree | `git hash-object corpus/lessons/README.md`; `sha256sum corpus/lessons/README.md`; supersession already filed `LOG.md:3570-3576` |

Two honesty constraints for C03: (a) `x45`'s flip to exit 0 and `x57`'s further drift to
28/37 are **new readings**, so the table shows both states with their dates and neither
is called "green" without its command; (b) R8 stays **open** in the table — filing it as
closed would be a false claim, since no `round-33.md` byte exists.

### 2.3 Byte-preservation controls (C04)

- No filed byte edited: `git status --short -- reports/round-1 reports/round-2 … reports/round-33`
  must show nothing; the only untracked path is `reports/round-34/` (measured at my
  reads: `git status --short` → `?? reports/round-34/` only).
- The two old digests stay quotable: `83b0a78a…` from
  `reports/round-30/craft/box1-landed-survey.json:4` and `79fe91d3…` from the 7 files
  above — re-read and recorded, never rewritten.
- `reports/round-33/adj/A09-pins.md` keeps its old anchors: C03 quotes `:19-20,:55-101,103-116`
  and appends new rows elsewhere under `reports/round-34/`.

## 3. Interfaces, owners, order

| step | owner | artifact | depends on |
|---|---|---|---|
| tool source draft | O02 | `op/O02-tool-source.md` | this plan |
| selftest transcript (13 controls) | O03 | `op/O03-selftest.md` | O02 draft (scratch materialization) |
| inventory run + receipt | O04 | `op/receipt-guard-adoption.json`, `op/O04-predicted-inventory.md` | O02/O03 |
| routing draft | O05 | `op/O05-routing.md` | O04 (classes per runner) |
| O verification (incl. the r26 divergence) | O07/O08/O09 | `op/O07-verify-tool.md`, `op/O08-traps.md`, `op/O09-verify-routing.md` | O02–O05 |
| box-1 survey + durable receipt | C01/C02 | `calib/box1-resurvey-durable.json`, `calib/C02-receipt-json.md` | none (filed tool + live SKILL bytes) |
| anchor reissue table | C03 | `calib/C03-anchor-reissue.md` | §2.2 method |
| byte controls | C04 | `calib/C04-byte-check.md` | C02/C03 |
| C verification | C07/C08 | `calib/C07-verify-survey.md`, `calib/C08-verify-reissue.md` | C01–C04 |

Order rule: O03's selftest is what makes O04's inventory trustworthy (a classifier that
misses the `OUTPUT_REL` idiom — control C4 — under-reports the hazard count), and C03's
table must be built **after** C02 pins the SKILL digest, so the reissue is bound to the
same bytes the survey measured.

## Owed

- `reports/round-34/scout/K03-guard-pattern.md` — absent at every read (`ls
  reports/round-34/scout/` → No such file or directory). §1.4's census is my own
  measurement and should be reconciled with K03 when it lands; if K03's class names
  differ, the receipt should carry both vocabularies rather than silently renaming.
- `reports/round-34/scout/K04-anchor-census.md` — same absence; §2.2's anchor map is
  re-derivable from `git diff --unified=0 139e3b6 da68a6d -- SKILL.md
  corpus/lessons/README.md AGENTS.md` and must be cross-checked against K04 before C03
  files.
- `reports/round-34/plan/P01-d-plan.md` — not read (D-side, not this mission's
  dependency); if P01's plan fixes a shared artifact-name convention for round 34, the
  integrative seat should align O/C names to it.

## Citations

- `REGIMEN.md` (round contract; per-round claim/verdict rules); `reports/round-34/claims.json`
  (claims O and C: before/after_required/counting_commands/thresholds);
  `reports/round-34/targets.json` (seat P02 `mission`/`out`; `shared_rules`).
- `reports/round-33/claims.json` (the four named hazards for claim O); `LOG.md:3548-3567`
  (F-C13-1 incident: write sites `:3556-3558`, r26 `:3559-3560`, PREVENTION `:3563-3567`,
  isolated `git archive` route `:3554-3555`); `LOG.md:3570-3576` (README/SKILL supersession
  records); `LOG.md:3584-3586` (AGENTS.md 42→40 excision).
- `tools/harness/receipt_guard.py` (guard semantics `:1-16`, `_check_receipt` `:82-150`,
  `guard_receipt` `:152`, `round_runner_main` `:161`, fixture idiom `:212-213`, selftest
  controls `:240-342`, receipt tail `controls*`/`limits`).
- Round-25 audit-tool style: `reports/round-25/audit/x45-lessons-pointer-audit.py:11-24,33,47-57,138-140`;
  `reports/round-25/audit/c31-lessons-index-audit.py:18-26,432-464`;
  `reports/round-25/audit/x48-v3-supersession-audit.py` (head: numbered checks, read-only,
  stdout receipt).
- Runner census and class evidence (filed bytes, read-only): `reports/round-5/run-validation.py:193-194`;
  `reports/round-6/run-validation.py:336`; `reports/round-7/run-validation.py:1171`;
  `reports/round-8/run-validation.py:99,1485-1486`; `reports/round-9/run-validation.py:127,1909-1910`;
  `reports/round-10/run-validation.py:60,1053-1054`; `reports/round-11/run-validation.py:125,1738-1740`;
  `reports/round-12/run-validation.py:1062,1069-1072`; `reports/round-19/run-validation.py:2,19-21`;
  `reports/round-21/run-validation.py:1106,1113-1116`; `reports/round-29/run-validation.py:891-897,918-922`;
  `reports/round-14/run-validation.py:413,716-717`; `reports/round-15/run-validation.py:1037,1345-1346`;
  `reports/round-16/run-validation.py:998,1264-1265`; `reports/round-17/run-validation.py:1117,1430-1431`;
  `reports/round-18/run-validation.py:1511,1850-1851`; `reports/round-20/run-validation.py:1278,1484-1485`;
  `reports/round-22/run-validation.py:827-829,921-922`; `reports/round-23/run-validation.py:1064-1066,1094-1097`;
  `reports/round-24/run-validation.py:1151-1153,1181-1184`; `reports/round-25/run-validation.py:1108-1110,1142-1145`;
  `reports/round-26/run-validation.py:90,199,1855-1857,1871,1906-1909`;
  `reports/round-27/run-validation.py:1853-1855,1904-1907`; `reports/round-28/run-validation.py:1996-1998,2095-2098`;
  `reports/round-30/run-validation.py:883-885,903,922-923`; `reports/round-31/run-validation.py:1118-1120,1158-1159`;
  `reports/round-32/run-validation.py:1102-1104,1123,1142-1143`; `reports/round-33/run-validation.py:1441-1443,1470-1471`.
- Box-1: `reports/round-30/craft/box1-survey.py:5-12`; `reports/round-30/craft/box1-landed-survey.json:2-6`;
  `reports/round-30/run-validation.py:697-700`; `reports/round-32/final-dossier.md:46`.
- Anchors and deltas: `reports/round-33/adj/A09-pins.md:19-20,31-41,55-101,103-116,118-131`;
  `reports/round-33/op/O07-baseline-receipt.md:147-181`.
- README state: `corpus/lessons/README.md:105,254,398-448`; `git diff --numstat 139e3b6 da68a6d`
  → `35 18 SKILL.md`, `130 28 corpus/lessons/README.md`, `0 2 AGENTS.md`.
- Commands run (all 2026-10-19, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`,
  read-only): `python3 -B reports/round-30/craft/box1-survey.py` → exit 0, `named 28`,
  `skill_sha256 f9bd07c2…`; `sha256sum SKILL.md` → `f9bd07c2…`, `wc -l` → 732;
  `python3 -B tools/harness/receipt_guard.py reports/round-{5,6,7,12,19,21,26,29,32}/validation.json`
  → all exit 3 with `RECEIPT-GUARD-COMMITTED`; ad-hoc read-only `ast`/regex census over
  `reports/round-*/run-validation.py` (28 files; class table §1.4);
  `ls -d reports/round-*/run-validation.py | wc -l` → 28;
  `git diff --unified=0 139e3b6 da68a6d -- SKILL.md` (hunk offsets §2.2);
  `git show 139e3b6:SKILL.md | wc -l` → 715 and its `sha256sum` → `79fe91d3…`;
  `grep -n "SKILL\.md:47" SKILL.md` → `149,183` (identical at `139e3b6`);
  `sed -n '522p;534p;536p;662p;726p;729,732p' SKILL.md`;
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 0, six PASS,
  `findings: 0`; `python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py --json`
  → exit 0; `python3 -B reports/round-27/audit/x57-lessons-audit.py --selftest` →
  `"passed": 28, "total": 37`; `sha256sum corpus/lessons/README.md` → `f752e1d7…`,
  `git hash-object` → `73f3e1bd…`, `wc -l` → 448; `ls corpus/lessons/*.md | wc -l` → 33
  (README included, `round-33.md` absent); `wc -l AGENTS.md` → 40,
  `grep -n "SKILL.md" AGENTS.md` → no match; `grep -rln 79fe91d3 reports/round-3[012]/` → 7 files;
  `git status --short` → `?? reports/round-34/`; `git rev-parse HEAD` →
  `da68a6d705e41f369f21e8607bfaab5b54077f84`.
