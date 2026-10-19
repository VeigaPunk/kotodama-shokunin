- Seat: O03 | executor | claim O | date 2026-10-19 | baseline da68a6d

# O03 — selftest controls spec + fixtures for `tools/harness/receipt_guard_adoption.py`

Deliverable: the fixture set, the class taxonomy, the expected-class table, the driver
contract for `--selftest`, and the measured evidence that the controls discriminate.
Everything below was produced read-only at da68a6d (worktree clean except untracked
`reports/round-34/`; `git status --short` = `?? reports/round-34/`, 1 row). No filed
runner was executed; no shared file was edited.

## 1. Taxonomy (class precedence is part of the contract)

| class | definition | on the 28 filed runners |
|---|---|---|
| `guarded` | own-receipt write exists AND a guard call (`guard_receipt` / `round_runner_main`) exists at a line **before** the write | 17 |
| `guard-after-write` | guard call exists, but only after the own-receipt write | 0 |
| `guard-defined-not-called` | receipt_guard loaded (`runpy.run_path` / import / local `def`) but no guard call on any path | 0 |
| `unguarded` | own-receipt write, no guard adoption at all | 10 |
| `writes-other-round-receipt` | writes a `reports/round-MM/validation.json` with MM ≠ own round, and no own write | 0 |
| `embedded-write-suspect` | no AST-visible own write, but a string literal contains `validation.json` **and** a write token | 1 |
| `mentions-receipt-no-write` | `validation.json` appears only in prose/limits | 0 |
| `clean-no-receipt-write` | no receipt write and no write token tied to `validation.json` | 0 |
| `could-not-evaluate` | unparseable or ambiguous — must be reported, never silently green | 0 |

Precedence (binding): own write > other-round write > embedded-literal suspect >
prose mention > clean. `embedded-write-suspect` is a **review flag, not a verdict**: it
must be listed with its literal's line, never counted as `guarded` and never as clean.

## 2. Fixtures (integrator lands these; they are the `--selftest` corpus)

11 fixtures + 1 out-of-scope control, staged into a throwaway tree
`$TMPDIR/receipt-guard-adoption-fixtures/<pid>/tree/` (never inside the repo tree — the
fixture rounds are numbered 91–101 so they can never collide with filed rounds 5–33).
Each fixture body is a faithful reduction of a real filed idiom; the `real precedent`
column is the evidence that the control shape is not invented.

| id | fixture path in tree | expected class | real precedent |
|---|---|---|---|
| F01 | `reports/round-91/run-validation.py` | `guarded` | `reports/round-32/run-validation.py:1102-1103,1123,1142` (runpy shim idiom B) |
| F02 | `reports/round-92/run-validation.py` | `guarded` | `reports/round-14/run-validation.py:25,420` (module-call idiom A) |
| F03 | `reports/round-93/run-validation.py` | `guard-defined-not-called` | trap: r32 shape with the call removed |
| F04 | `reports/round-94/run-validation.py` | `guard-after-write` | trap: guard call below the write |
| F05 | `reports/round-95/run-validation.py` | `unguarded` | `reports/round-5/run-validation.py:194`, `reports/round-6/run-validation.py:336`, `reports/round-7/run-validation.py:1171` (`(HERE / "validation.json").write_text`) |
| F06 | `reports/round-96/run-validation.py` | `unguarded` | `reports/round-29/run-validation.py:922`, `reports/round-32/…:1143` shape without the guard |
| F07 | `reports/round-97/run-validation.py` | `unguarded` | `reports/round-8/run-validation.py:1485-1486`, `:9:1909-1910`, `:10:1053-1054`, `:11:1738-1740`, `:12:1069-1071`, `:21:1113-1115` (receiver variable) |
| F08 | `reports/round-98/run-validation.py` | `clean-no-receipt-write` | no filed precedent (all 28 runners write) — synthetic clean |
| F09 | `reports/round-99/run-validation.py` | `embedded-write-suspect` | `reports/round-19/run-validation.py:5-22` (receipt written from inside a `python3 -c` string) |
| F10 | `tools/notes-writer.py` | **absent from inventory** (out of scope) | every `tools/*.py` that writes JSON, e.g. `tools/harness/r8_checks.py` |
| F11 | `reports/round-100/run-validation.py` | `unguarded` | trap: write via `os.replace(temp, target)` |
| F12 | `reports/round-101/run-validation.py` | `writes-other-round-receipt` | `reports/round-21/run-validation.py:472` (writes into an isolated clone) |

`FIXTURES` block for O02's tool — graft as the selftest corpus (stdlib only, no I/O
outside `TMPDIR`):

```python
FIXTURES = {
 "F01-guarded-runpy-shim": ("reports/round-91", '''\
import runpy, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-91"
OUTPUT = f"{ROUND_DIR}/validation.json"
def safe_path(rel): return ROOT / rel
def guard_receipt():
    namespace = runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)
def main(argv=None):
    rendered = json.dumps({"round": 91}, indent=2) + "\\n"
    guard_receipt()
    safe_path(OUTPUT).write_text(rendered, encoding="utf-8")
if __name__ == "__main__":
    sys.exit(main())
'''),
 "F02-guarded-module-call": ("reports/round-92", '''\
import runpy, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "reports/round-92/validation.json"
GUARD = "tools/harness/receipt_guard.py"
def main():
    module = runpy.run_path(str(ROOT / GUARD))
    module.guard_receipt(ROOT / OUTPUT, repo_root=ROOT)
    (ROOT / OUTPUT).write_text(json.dumps({"round": 92}, indent=2) + "\\n", encoding="utf-8")
    return 0
if __name__ == "__main__":
    sys.exit(main())
'''),
 "F03-guard-defined-not-called": ("reports/round-93", '''\
import runpy, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "reports/round-93/validation.json"
def guard_receipt():
    namespace = runpy.run_path(str(ROOT / "tools/harness/receipt_guard.py"))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)
def main():
    (ROOT / OUTPUT).write_text(json.dumps({"round": 93}, indent=2) + "\\n", encoding="utf-8")
    return 0
if __name__ == "__main__":
    sys.exit(main())
'''),
 "F04-guard-called-after-write": ("reports/round-94", '''\
import runpy, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "reports/round-94/validation.json"
def guard_receipt():
    namespace = runpy.run_path(str(ROOT / "tools/harness/receipt_guard.py"))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)
def main():
    safe = ROOT / OUTPUT
    safe.write_text(json.dumps({"round": 94}, indent=2) + "\\n", encoding="utf-8")
    guard_receipt()
    return 0
if __name__ == "__main__":
    sys.exit(main())
'''),
 "F05-unguarded-here-relative": ("reports/round-95", '''\
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "reports/round-95"
def main():
    report = {"round": 95, "acceptance_checks_passed": True}
    (HERE / "validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
    return 0
if __name__ == "__main__":
    sys.exit(main())
'''),
 "F06-unguarded-output-const": ("reports/round-96", '''\
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-96"
OUTPUT = f"{ROUND_DIR}/validation.json"
def safe_path(rel): return ROOT / rel
def main(argv=None):
    rendered = json.dumps({"round": 96}, indent=2) + "\\n"
    if "--check" in (argv or sys.argv):
        print(rendered, end="")
    else:
        safe_path(OUTPUT).write_text(rendered, encoding="utf-8")
    return 0
if __name__ == "__main__":
    sys.exit(main())
'''),
 "F07-unguarded-variable-receiver": ("reports/round-97", '''\
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUTPUT_REL = "reports/round-97/validation.json"
def main():
    receipt = {"round": 97}
    output = ROOT / OUTPUT_REL
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\\n", encoding="utf-8")
    return 0
if __name__ == "__main__":
    sys.exit(main())
'''),
 "F08-clean-no-receipt-write": ("reports/round-98", '''\
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
def main():
    totals = {"checked": 3}
    print(json.dumps(totals, sort_keys=True))
    return 0
if __name__ == "__main__":
    sys.exit(main())
'''),
 "F09-embedded-code-writer": ("reports/round-99", '''\
import subprocess, sys
result = subprocess.run([sys.executable, "-c", """
import json, pathlib
v = json.load(open('reports/round-99/validation.json'))
v['acceptance_checks_passed'] = True
pathlib.Path('reports/round-99/validation.json').write_text(json.dumps(v, indent=1))
print('acceptance: True')
"""], capture_output=True, text=True)
print(result.stdout.strip() or result.stderr[-300:])
'''),
 "F10-non-runner-json-writer": ("tools", '''\
import json, pathlib
# Not a round runner: writes a helper JSON elsewhere in the tree.
def main():
    pathlib.Path("tools/notes.json").write_text(json.dumps({"note": "helper"}), encoding="utf-8")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
'''),
 "F11-unguarded-os-replace": ("reports/round-100", '''\
import json, os, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "reports/round-100/validation.json"
def main():
    target = ROOT / OUTPUT
    with tempfile.NamedTemporaryFile("w", dir=target.parent, delete=False, encoding="utf-8") as handle:
        json.dump({"round": 100}, handle)
        temp = handle.name
    os.replace(temp, target)
    return 0
if __name__ == "__main__":
    sys.exit(main())
'''),
 "F12-writes-other-round-receipt": ("reports/round-101", '''\
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
def main():
    (ROOT / "reports/round-5/validation.json").write_text(json.dumps({"probe": True}), encoding="utf-8")
    return 0
if __name__ == "__main__":
    sys.exit(main())
'''),
}
```

## 3. Selftest driver contract

- `python3 tools/harness/receipt_guard_adoption.py --selftest` → stages the fixtures
  above into `tempfile.mkdtemp(dir=$TMPDIR/"receipt-guard-adoption-fixtures")`, scans
  `<tmp>/tree`, prints the JSON receipt (shape mirroring
  `tools/harness/receipt_guard.py:343-351`: `tool`, `command`, `date`, `controls[]`,
  `controls_passed`, `controls_total`, `selftest_passed`, `limits`), exits 0 iff all pass.
- Controls total = **12**: F01–F12, where F10 asserts *absence* from the inventory
  (the scan walks `reports/round-*/run-validation.py` only; `tools/notes-writer.py`
  must not appear in any row) and each of F01–F09, F11, F12 asserts its expected class.
- `--json` (O04's parity leg) emits, per runner: `path`, `sha256`, `class`,
  `own_write_lines[]`, `guard_lines[]`, `guard_idiom` (`module-call` | `runpy-shim` |
  `import` | `null`), `evidence` (the unparsed receiver expression + literal line for
  `embedded-write-suspect`), and `could_not_evaluate` (reason or `null`).
- The selftest must be dependency-free: it may not read `reports/round-*`, `tools/`, or
  any filed byte; `--json` is the only mode that touches the live tree.

### Interface requirements measured out of the fixture set (binding on O01/O02)

1. **Receiver-variable alias resolution.** `x = ROOT / OUTPUT_REL; x.write_text(...)`
   (F07; six real runners) and `safe = ROOT / OUTPUT; safe.write_text(...)` (F03/F04)
   are invisible to `Call.args[0]` inspection — the write target is `Call.func.value`.
   Observed: with receiver-alias resolution disabled, 7/11 fixtures misclassify
   (rounds 91,92,93,94,96,97,100), including turning F04 into a false clean.
2. **Alias tables must not be last-wins.** The first reference run (last-wins table)
   misclassified `reports/round-22/run-validation.py` and
   `reports/round-30/run-validation.py` as `embedded-write-suspect` because `OUTPUT`
   is reassigned; the corrected first-binding resolver reaches `guarded` on both.
   Ambiguity that survives resolution is `could-not-evaluate`, never a guess.
3. **`os.replace` / `shutil.move` second-argument detection** (F11): disabling it
   misclassifies round-100 (observed).
4. **Embedded-literal scan** (F09 / `reports/round-19/run-validation.py:5-22`):
   AST-only detection calls r19 clean — a **false green** on a runner that does rewrite
   its filed receipt. Disabling the literal scan misclassifies round-99 (observed).
5. **Guard-order check** (F04) and **call-not-definition check** (F03): `def
   guard_receipt():` + `runpy.run_path(...)` without a call is not adoption.

## 4. Measured evidence (scratch reference classifier, `.scratch/o03-classify2.py`)

- Fixtures: **11/11 expected-class PASS**, `fixtures all-green under spec: True`.
- Real tree, 28 runners: **28/28 PASS** against the expected table; class counts
  `{'unguarded': 10, 'guarded': 17, 'embedded-write-suspect': 1}`.
- Per-file evidence (command: `python3 -B .scratch/o03-classify2.py`):
  - `unguarded` (10): `reports/round-5/run-validation.py:194`,
    `reports/round-6/run-validation.py:336`, `reports/round-7/run-validation.py:1171`,
    `reports/round-8/run-validation.py:1485-1486`, `reports/round-9/run-validation.py:1909-1910`,
    `reports/round-10/run-validation.py:1053-1054`, `reports/round-11/run-validation.py:1738-1740`,
    `reports/round-12/run-validation.py:1069-1071`, `reports/round-21/run-validation.py:1113-1115`,
    `reports/round-29/run-validation.py:922`.
  - `guarded` (17): idiom A `module.guard_receipt(...)` —
    `reports/round-14/run-validation.py:420`, `reports/round-15/run-validation.py:1044`,
    `reports/round-16/run-validation.py:1005`, `reports/round-17/run-validation.py:1124`,
    `reports/round-18/run-validation.py:1518`, `reports/round-20/run-validation.py:1285`
    (with `GUARD = "tools/harness/receipt_guard.py"` at
    `reports/round-14/run-validation.py:25`, `reports/round-15/run-validation.py:44`,
    `reports/round-16/run-validation.py:57`, `reports/round-17/run-validation.py:68`,
    `reports/round-18/run-validation.py:67`, `reports/round-20/run-validation.py:57`);
    idiom B runpy shim — `reports/round-22/run-validation.py:827-828,911,921`,
    `reports/round-23/run-validation.py:1064-1065,1094`,
    `reports/round-24/run-validation.py:1151-1152,1181`,
    `reports/round-25/run-validation.py:1108-1109,1142`,
    `reports/round-26/run-validation.py:1855-1857,1906`,
    `reports/round-27/run-validation.py:1853-1854,1904`,
    `reports/round-28/run-validation.py:1996-1997,2095`,
    `reports/round-30/run-validation.py:883-884,903,922`,
    `reports/round-31/run-validation.py:1118-1119,1139,1158`,
    `reports/round-32/run-validation.py:1102-1103,1123,1142`,
    `reports/round-33/run-validation.py:1441-1442,1459,1470`.
  - `embedded-write-suspect` (1): `reports/round-19/run-validation.py:21` inside the `-c`
    literal at `reports/round-19/run-validation.py:5-22`.
- Runner census is 28 files, not 32: rounds 1–4 and 13 have no `run-validation.py`
  (`reports/round-*/run-validation.py | wc -l` = 28).

### Claim-vs-bytes divergence the tool must resolve, not paper over

- `claims.json` names four "known hazards": r5/r6/r7/r26. Bytes at HEAD say: r5/r6/r7
  are `unguarded` (LOG.md:3556-3558 cites their exact write lines — matches), but
  **r26 is `guarded`** — shim `reports/round-26/run-validation.py:1855-1857`, call
  `:1906`, receipt write `:1909`; worktree blob `cfdd58ee…` == `git rev-parse
  HEAD:reports/round-26/run-validation.py`. `LOG.md:3559-3560` and
  `reports/round-33/adj/A15-audit-draft.md:176` both assert r26 "carries the same
  hazard (`:90`,`:1909`)"; that assertion is not supported by the bytes at da68a6d
  and is recorded here as the divergence (owner for resolution: integrator + O04/O05).
- The unguarded set is **ten**, not four: the six unnamed members are r8, r9, r10,
  r11, r12, r21, r29 (seven lines above minus r5/r6/r7 — see §4 list). Threshold
  "the four named hazards classified" is therefore satisfiable while the inventory
  still understates the debt by 6 + r19's embedded writer; the honest routing (O05)
  should cover all 11 non-guarded files or record why not.
- `guard-defined-not-called` is 0 on the filed tree, so F03/F04 are pure traps: they
  cannot be validated against filed bytes and are the controls that must keep the
  selftest honest.

## 5. Limits

- The scratch classifier is evidence for the fixture set's discriminating power, **not
  the deliverable**: O02 ships the tool bytes; my class expectations transfer only if
  the interface requirements in §3 are met.
- `embedded-write-suspect` can in principle flag a runner whose *prose* literal quotes a
  write call; it is defined as a review flag (never `guarded`, never clean), and its
  evidence line must be emitted so a human can adjudicate.
- Fixture rounds 91–101 exist only inside the staged temp tree; nothing is written to
  `reports/` by the selftest.
- No filed byte was read past the runners and their receipts; no filed runner was
  executed (`grep`/`ast`/`sed` reads only). All 28 runner checks are static.

## Owed

- `reports/round-34/op/O01-impl.md` — tool core spec (mine assumes §3 requirements; reconcile).
- `reports/round-34/op/O02-tool-source.md` — tool bytes; must graft §2 `FIXTURES` + §3 contract.
- `reports/round-34/op/O04-predicted-inventory.md` — expected inventory; my §4 census is an independent second reading — row-for-row reconciliation and the r26 divergence disposition are owed there.
- `reports/round-34/op/O05-routing.md` — routing table; owes the 11-file (not 4-file) non-guarded set per §4.
- `reports/round-34/scout/K03-guard-pattern.md` — guard-pattern scout (absent at my run; idiom A/B classification above stands in for it, to-verify against K03 when it lands).
- `reports/round-34/plan/P02-oc-plan.md` — plan of record for O; reconcile the selftest count (12 controls).
- Integration: if O02's tool names a different class vocabulary, the expected-class table in §2 is the source of truth to adapt, not vice versa.

## Citations

- `REGIMEN.md:25-50` (per-round contract), `reports/round-34/claims.json:38-52` (claim O + thresholds), `reports/round-34/targets.json:11,46-48` (shared rules, seat O03).
- `tools/harness/receipt_guard.py` (sha256 `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`), `:7-8,144-149,152-168,201-351`.
- `reports/round-32/run-validation.py:1102-1103,1123,1142-1143`; `reports/round-33/run-validation.py:1441-1442,1459,1470-1471`.
- `reports/round-14/run-validation.py:25,420`; `:15:44,1044`; `:16:57,1005`; `:17:68,1124`; `:18:67,1518`; `:20:57,1285`.
- `reports/round-22/run-validation.py:827-828,911,921-922`; `:23:1064-1065,1094`; `:24:1151-1152,1181`; `:25:1108-1109,1142`; `:26:1855-1857,1906,1909`; `:27:1853-1854,1904`; `:28:1996-1997,2095`; `:30:883-884,903,922`; `:31:1118-1119,1139,1158`; `:33:1441-1442,1459`.
- `reports/round-5/run-validation.py:194`; `:6:336`; `:7:1171`; `:8:1485-1486`; `:9:1909-1910`; `:10:1053-1054`; `:11:1738-1740`; `:12:1069-1071`; `:19:5-22`; `:21:1113-1115,472`; `:29:922`.
- `LOG.md:3548-3567` (F-C13-1 record), `reports/round-33/adj/A15-audit-draft.md:176,320`.
- Commands: `ls reports/round-*/run-validation.py | wc -l` → `28`; `git status --short` → `?? reports/round-34/` (1 row); `git hash-object reports/round-26/run-validation.py` = `git rev-parse HEAD:reports/round-26/run-validation.py` = `cfdd58eece8586d939409349d05688926a7a6d69`; `python3 -B .scratch/o03-fixtures.py` (first run: 8/11 fixtures, 21/28 real — the failures are the §4 discriminating-power evidence); `python3 -B .scratch/o03-classify2.py` (final: fixtures all-green, 28/28, counts `{'unguarded': 10, 'guarded': 17, 'embedded-write-suspect': 1}`); `sha256sum SKILL.md` = `f9bd07c2…` (732 lines, context only).
