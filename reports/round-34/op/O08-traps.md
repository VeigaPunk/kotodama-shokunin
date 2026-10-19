- Seat: O08 | verifier | claim O | date 2026-10-19 | baseline da68a6d

# O08 — adversarial trap review of the receipt-guard adoption instrument

**Mission.** Craft three trap runners in `.scratch` (guard imported but not called;
guard called only under a flag; write via `os.replace`) and check that
`tools/harness/receipt_guard_adoption.py` classifies each honestly or files
`could-not-evaluate` — never a wrong green.

**Dependency status.** The tool does not exist at this baseline
(`ls tools/harness/` → `packet_links.py packet_uncertainty.py r8_checks.py
receipt_guard.py`; no `receipt_guard_adoption.py`) and O01/O02/O04 fragments are
not landed (`find reports/round-34 -name '*.md'` → empty). Everything that does
not depend on the tool is done below: durable trap fixtures, per-trap expected
classifications, two runnable instruments (reference probe + shortcut battery)
that prove the traps have teeth, an independent census of all 28 filed runners
that **corrects the declared hazard list**, and a digest-guarded replay protocol
for the landed tool. The tool-vs-traps verdict row is recorded under `## Owed`.

## 1. Fixture tree, digests, replay surface

Staged (ephemeral, gitignored): `.scratch/o08-traps/`. Durable record: this
fragment (full bytes inline, §4) + `.scratch/o08-traps/EXPECTATIONS.json`.

Isolated replay copy: `.scratch/o08-traps/iso` — `git archive HEAD | tar -x -C
.scratch/o08-traps/iso` (63M; HEAD = `da68a6d`), traps staged at
`reports/round-901..904/` and `tools/cache-export.py`. No filed round byte is
read-write in this copy; the lane tree is never scanned-in-place by my instruments.

```
ded148a3…  tree/reports/round-901/run-validation.py   (T1)
88049181…  tree/reports/round-902/run-validation.py   (T2)
ca215132…  tree/reports/round-903/run-validation.py   (T3)
0f18ac3e…  tree/reports/round-904/run-validation.py   (C+ control)
8498e854…  tree/tools/cache-export.py                 (C- control)
ee5a17b6…  honest_probe.py        d2d60967…  shortcut_battery.py
8d76557a…  EXPECTATIONS.json      2b1bacde…  replay.sh
596e8f90…  results/probe-real.json    b99f82ee…  results/battery-real.json
1df0cb89…  results/probe-traps.json   d6fbbd1d…  results/battery-traps.json
```

Replay (when the tool lands, either in-tree or in the iso copy):

```
bash .scratch/o08-traps/replay.sh /abs/path/to/receipt_guard_adoption.py [args…]
```

`replay.sh` digests every `reports/*/validation.json` in the iso copy before and
after the tool run and fails closed (exit 91) if any changed — i.e. it detects a
tool that executes scanned runners (F-C13-1 class). Dry-run with a missing tool:
`PRESERVATION-OK: all isolated-copy receipts byte-identical (tool exit 2)`.

## 2. Expected verdicts (binding facts; label vocabulary is the tool's choice)

| id | fixture | writes own receipt | adoption on default path | forbidden (wrong green) |
|---|---|---|---|---|
| T1 | round-901 | yes, `write_text` :59 | **no** (guard loadable, never called) | adopted / clean / no-write |
| T2 | round-902 | yes, `write_text` :63 | **only under `--guarded`** (:61) | adopted / clean |
| T3 | round-903 | yes, `os.replace(staging, output)` :57 (staging :56) | **no** (guard only as CHECKS string :19) | adopted / clean / no-write |
| C+ | round-904 | yes, :56 | yes (runpy wrapper, calls :49,:55) | hazard / unguarded / conditional |
| C- | tools/cache-export.py | writes JSON, **not a round runner** | n/a | any runner row |
| R5 | reports/round-5 | yes, :194 | no | adopted / clean |
| R26 | reports/round-26 | yes, :1909 | **yes (call :1906)** | unguarded / hazard |
| R19 | reports/round-19 | yes — **inside an embedded `subprocess -c` string, :5** | no | clean / no-write / adopted |

Acceptable honest fallbacks: `could-not-evaluate` with a named reason for T2/T3/R19
if the tool's detector genuinely cannot see the pattern; never a green.
The claim-O text ("classifies whether it writes its own validation.json in place
and whether it adopts …") fixes the two axes; the class labels are mine.

## 3. What the two instruments are

- `honest_probe.py` (reference, **not** the landed tool): stdlib AST two-axis
  classifier. Documented approximations: `ROOT / NAME` resolves to NAME's string;
  paths match on the substring `validation.json`; any `if` test that is not a
  `--check`/`--selftest` mode branch or an opt-in `args.*` flag is treated as
  conditional (conservative — never upgrades to adopted); calls lexically inside a
  `def guard_receipt`/`def guard_preflight` wrapper do not count as adoption;
  embedded code strings are scanned for receipt-write tokens and classified
  `unguarded-write (embedded program)` or `could-not-evaluate` under an adopted
  guard. Read-only: parses, never imports or executes a scanned runner.
- `shortcut_battery.py`: six naive heuristics an implementer might be tempted by —
  H1 any `receipt_guard` mention ⇒ adopted; H2 import/runpy/spec ⇒ adopted; H3 any
  guard call anywhere ⇒ adopted; H4 single-line `write_text`+OUTPUT regex;
  H5 guard file-path string ⇒ adopted; H6 `def guard_*` present ⇒ adopted.

## 4. Trap bytes (durable; identical to the staged files)

### T1 — `reports/round-901/run-validation.py` (guard imported, never called)

```python
#!/usr/bin/env python3
"""Round-901 acceptance runner (trap T1: receipt guard imported but never called).

Run:  python3 reports/round-901/run-validation.py
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-901"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
GUARD = "tools/harness/receipt_guard.py"


def load_guard():
    spec = importlib.util.spec_from_file_location("round901_receipt_guard", ROOT / GUARD)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import receipt guard")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def safe_path(relative):
    candidate = (ROOT / relative).resolve()
    if ROOT not in candidate.parents:
        raise ValueError(f"path escapes the lane root: {relative}")
    return candidate


def measure():
    return {
        "round": 901,
        "command": f"python3 {RUNNER}",
        "claims": {"T1": {"passed": True}},
        "acceptance_checks_passed": True,
        "limits": ["Trap fixture for guard-adoption classification; not a filed round."],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="print measured JSON without writing validation.json")
    args = parser.parse_args(argv)
    receipt = measure()
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.check:
        print(rendered, end="")
    else:
        output = ROOT / OUTPUT
        output.write_text(rendered, encoding="utf-8")
        print("acceptance_checks_passed: " + str(receipt["acceptance_checks_passed"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

### T2 — `reports/round-902/run-validation.py` (guard called only under a flag)

```python
#!/usr/bin/env python3
"""Round-902 acceptance runner (trap T2: guard called only under an opt-in flag).

Run:  python3 reports/round-902/run-validation.py
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-902"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
GUARD = "tools/harness/receipt_guard.py"


def guard_receipt():
    spec = importlib.util.spec_from_file_location("round902_receipt_guard", ROOT / GUARD)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import receipt guard")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.guard_receipt(OUTPUT, repo_root=ROOT)


def safe_path(relative):
    candidate = (ROOT / relative).resolve()
    if ROOT not in candidate.parents:
        raise ValueError(f"path escapes the lane root: {relative}")
    return candidate


def measure():
    return {
        "round": 902,
        "command": f"python3 {RUNNER}",
        "claims": {"T2": {"passed": True}},
        "acceptance_checks_passed": True,
        "limits": ["Trap fixture for guard-adoption classification; not a filed round."],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="print measured JSON without writing validation.json")
    parser.add_argument("--guarded", action="store_true",
                        help="opt in to the receipt guard; the default path skips it")
    args = parser.parse_args(argv)
    receipt = measure()
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.check:
        print(rendered, end="")
    else:
        if args.guarded:
            guard_receipt()
        output = ROOT / OUTPUT
        output.write_text(rendered, encoding="utf-8")
        print("acceptance_checks_passed: " + str(receipt["acceptance_checks_passed"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

### T3 — `reports/round-903/run-validation.py` (receipt replaced via `os.replace`)

```python
#!/usr/bin/env python3
"""Round-903 acceptance runner (trap T3: receipt replaced via os.replace, no guard).

Run:  python3 reports/round-903/run-validation.py
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-903"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"

CHECKS = (
    ("recount", ("tools/recount.py", "--json")),
    ("receipt-guard-selftest", ("tools/harness/receipt_guard.py", "--selftest")),
    ("handoff-gate-selftest", ("tools/gates/handoff-packet-check.py", "--selftest")),
)


def safe_path(relative):
    candidate = (ROOT / relative).resolve()
    if ROOT not in candidate.parents:
        raise ValueError(f"path escapes the lane root: {relative}")
    return candidate


def measure():
    return {
        "round": 903,
        "command": f"python3 {RUNNER}",
        "claims": {"T3": {"passed": True}},
        "acceptance_checks_passed": True,
        "limits": ["Trap fixture for guard-adoption classification; not a filed round."],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="print measured JSON without writing validation.json")
    args = parser.parse_args(argv)
    receipt = measure()
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.check:
        print(rendered, end="")
    else:
        output = safe_path(OUTPUT)
        staging = safe_path(OUTPUT + ".tmp")
        staging.write_text(rendered, encoding="utf-8")
        os.replace(staging, output)
        print("acceptance_checks_passed: " + str(receipt["acceptance_checks_passed"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

### C+ — `reports/round-904/run-validation.py` (canonical adopted pattern; control)

```python
#!/usr/bin/env python3
"""Round-904 acceptance runner (control C+: canonical adopted guard pattern).

Run:  python3 reports/round-904/run-validation.py
"""
from __future__ import annotations

import argparse
import json
import runpy
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-904"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"


def safe_path(relative):
    candidate = (ROOT / relative).resolve()
    if ROOT not in candidate.parents:
        raise ValueError(f"path escapes the lane root: {relative}")
    return candidate


def guard_receipt():
    namespace = runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def measure():
    return {
        "round": 904,
        "command": f"python3 {RUNNER}",
        "claims": {"C+": {"passed": True}},
        "acceptance_checks_passed": True,
        "limits": ["Control fixture for guard-adoption classification; not a filed round."],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="print measured JSON without writing validation.json")
    args = parser.parse_args(argv)
    if not args.check:
        guard_receipt()
    receipt = measure()
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.check:
        print(rendered, end="")
    else:
        guard_receipt()
        safe_path(OUTPUT).write_text(rendered, encoding="utf-8")
        print("acceptance_checks_passed: " + str(receipt["acceptance_checks_passed"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

### C− — `tools/cache-export.py` (non-runner writing JSON; control)

```python
#!/usr/bin/env python3
"""Cache exporter (control C-): a non-runner that writes JSON; must not be flagged."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "tools/.cache/notes.json"


def main():
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps({"rows": 3}, indent=2) + "\n", encoding="utf-8")
    print("wrote " + str(CACHE))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## 5. Reference-probe results

```
T1 round-901  class=unguarded-write            adoption=referenced-not-called  writes=[write_text@59:in-place-write]
T2 round-902  class=conditional-guard (default path unguarded)  adoption=conditional-guard  calls=[guard_receipt@61]  writes=[write_text@63]
T3 round-903  class=unguarded-write            adoption=referenced-not-called  writes=[write_text@56:staging-write, replace@57:rename-into-place]
C+ round-904  class=adopted                    adoption=adopted   variant=runpy  calls=[guard_receipt@49, guard_receipt@55]  writes=[write_text@56]
C- cache-export.py  class=no-receipt-write     adoption=absent
```

Shortcut battery on the traps: **T1 0/6, T2 0/6, T3 0/6 correct** (every shortcut
emits a wrong green on T1/T2 as "adopted"; H1/H5 emit "adopted" on T3 and H4
emits "clean" on T3); **C+ 6/6 correct** (control: a guarded runner is not a
false positive).

## 6. Independent census of the 28 filed runners (correction of the declared hazard list)

`python3 .scratch/o08-traps/honest_probe.py 'reports/round-*/run-validation.py'`

- **17 adopted** — r14 r15 r16 r17 r18 r20 (variant `guard_preflight` via
  `importlib.util.spec_from_file_location`) and r22 r23 r24 r25 r26 r27 r28 r30
  r31 r32 r33 (variant runpy wrapper `def guard_receipt()`).
- **11 unguarded writers** — r5 (`:194`), r6 (`:336`), r7 (`:1171`), r8 (`:1486`),
  r9 (`:1910`), r10 (`:1054`), r11 (`:1740`), r12 (`:1071`), r19 (embedded program
  `:5`), r21 (`:1115`), r29 (`:922`).
- 28 runners, 27 receipts filed; `reports/round-22/run-validation.py` has no
  `validation.json` beside it (`to-verify`, out of my scope — recorded for the
  inventory denominator).

Shortcut battery on those real bytes: each of H1/H2/H3/H5/H6 is wrong on
**11/28** rows and every wrong verdict is a wrong green (the unguarded runner is
labelled "adopted"); H4 is wrong on **6/28** (r8, r9, r10, r11, r12, r21 labelled
"clean"). 11/28 real runners receive a wrong green from at least one shortcut.

## 7. Adversarial findings (each actionable for the integrator / O-tool authors)

- **F1 — the declared four-hazard list is wrong twice (blocker for the claim-O
  threshold).** `reports/round-34/claims.json:41` and `LOG.md:3560` name
  r5/r6/r7/r26. Measured: **r26 is adopted** — `git show
  HEAD:reports/round-26/run-validation.py | grep -n guard_receipt` → wrapper def
  `:1855`, call `:1906`; the guarded write is `:1909` (call immediately precedes
  it). And the real unguarded set is **11** runners (r8–r12, r19, r21, r29 in
  addition to r5/r6/r7). Required: the inventory must classify all 28 runners and
  the r26 row must be reclassified as adopted in a **new** supersession row
  (filed LOG/claims bytes untouched).
- **F2 — embedded-program write is a live false-clean.** r19 performs its receipt
  write inside a `subprocess -c` string (`reports/round-19/run-validation.py:5`,
  preview captured in `results/probe-real.json`). A static classifier that does not
  read embedded code strings reports "no write" — a wrong green on real bytes.
  Required: parse embedded code or emit `could-not-evaluate` with the reason.
- **F3 — adoption must be path-sensitive, not call-presence.** A call inside the
  `def guard_receipt()` wrapper itself is not adoption (T2's first draft, and the
  real wrappers at `reports/round-32/run-validation.py:1104`,
  `reports/round-26/run-validation.py:1857` contain such an inner call). My first
  probe version produced exactly this wrong green on T2 before the fix — recorded
  as a real defect class, not a hypothetical.
- **F4 — write detection must resolve aliases and rename-into-place.** The
  `output = ROOT / OUTPUT_REL` + `output.write_text(...)` shape (r8–r12, r21) and
  `os.replace(staging, output)` (T3, where the receipt path is the *second*
  argument) are invisible to a single-line `write_text(...OUTPUT...)` regex — H4
  scores 6/28 wrong, all wrong-green.
- **F5 — registration strings are not adoption.** `reports/round-26/run-validation.py:199`
  registers `("receipt-guard-selftest", ("tools/harness/receipt_guard.py",
  "--selftest"))` in a CHECKS tuple that guards nothing; T3 mirrors this shape at
  `:19`. Any string-mention heuristic (H1/H5) gives wrong greens on T1/T3 and, on
  r26, "adopted for the wrong reason".
- **F6 — two adopted spellings must both be recognized.** The `guard_preflight`
  (r14–r20) and `guard_receipt` (r22–r33) wrappers are both adoption; a detector
  keyed to one name false-positives 7+ adopted runners.
- **F7 — `protection_guard` is not receipt-guard adoption.** r29 guards the
  *tree* (`:779`, git-status regression protection of PROTECTED paths) while its
  receipt write at `:922` is unguarded. The inventory must not count it as
  adoption (my probe: adoption=absent; matches F1's r29 hazard row).

## 8. Self-conformance and preservation evidence

- I executed **no** filed `run-validation.py` anywhere: both instruments are
  AST/text parsers; the traps were never run (they would write their own
  `reports/round-9xx/validation.json` only if executed).
- `git status --porcelain` → only `?? reports/round-34/` (pre-existing untracked
  round dir); no tracked byte modified.
- All 27 filed `reports/round-*/validation.json` re-hashed against
  `git show HEAD:<path>`: **0 differ**. `reports/round-34/run-validation.py` does
  not exist yet, so no round runner was run or written.
- Trap bytes live in `.scratch` (gitignored) and inline above, so scratch cleanup
  loses nothing.

## 9. to-verify

- Whether the landed tool's output vocabulary matches my labels — only the
  **facts** in §2 are binding; `could-not-evaluate` with a reason is an
  acceptable honest verdict for T2/T3/R19, "adopted"/"clean" is not.
- r19's runtime semantics (does the embedded program really rewrite the receipt
  in place?) — answerable only by an isolated `git archive` run, which no
  counting command in this round does. Classified from the embedded text.
- Whether the landed tool scans embedded code strings at all (F2) — replay step
  after the tool lands.
- `reports/round-22` has a runner but no filed `validation.json` — reason unknown.

## Owed

- `op/O07-verify-tool.md` and its input `tools/harness/receipt_guard_adoption.py`
  (O01/O02 fragments not landed at my run time) — when the tool exists, run
  `bash .scratch/o08-traps/replay.sh <tool>` and check the tool's per-file verdicts
  against §2/§3 of `EXPECTATIONS.json`; a verdict of "adopted"/"clean" on T1, T2 or
  T3, or "unguarded" on r26 (F1), is a filed defect against claim O, not an
  acceptable result. My instrument bytes (probe, battery, traps, expectations,
  replay) are inline in §4 and digest-listed in §1.
- `reports/round-34/run-validation.py` does not exist (claim O counting command
  leg cannot be run by me).

## Citations

- `REGIMEN.md:25-50` (per-round contract), `reports/round-34/claims.json:41-51`
  (claim O text, hazards list, thresholds), `reports/round-34/targets.json:51`
  (seat O08 mission), `:5-11` (shared rules).
- `LOG.md:3548` F-C13-1 record; `LOG.md:3560` "carries the same hazard (`:90`,
  `:1909`)" — the sentence F1 corrects.
- `tools/harness/receipt_guard.py:152-168` (`guard_receipt`,
  `round_runner_main`), `:34-35` (REFUSAL_EXIT_CODE=3, REFRESH_ENV).
- `git show HEAD:reports/round-26/run-validation.py | grep -n guard_receipt` →
  `1855:def guard_receipt():`, `1857:` inner call, `1906: guard_receipt()`;
  `sed -n '1904,1910p'` → guarded write at `1909`. Same method for
  `reports/round-32/run-validation.py` → `1102,1104,1123,1142,1143`.
- Census/writes: `results/probe-real.txt` (all 28 rows with `path:line`),
  `results/probe-real.json`, `results/battery-real.json`,
  `results/battery-summary.txt`, `results/probe-traps.txt`, `results/battery-traps.json`.
- Commands: `python3 .scratch/o08-traps/honest_probe.py
  '.scratch/o08-traps/tree/reports/round-9*/run-validation.py'
  '.scratch/o08-traps/tree/tools/*.py'`; `python3
  .scratch/o08-traps/honest_probe.py 'reports/round-*/run-validation.py' --json`;
  `python3 .scratch/o08-traps/shortcut_battery.py
  .scratch/o08-traps/results/probe-{traps,real}.json --json`;
  `git archive HEAD | tar -x -C .scratch/o08-traps/iso`;
  `bash .scratch/o08-traps/replay.sh /nonexistent/receipt_guard_adoption.py --json`
  (dry-run → `PRESERVATION-OK … tool exit 2`);
  `git status --porcelain`; per-file SHA-256 comparison of
  `reports/round-*/validation.json` against `git show HEAD:<path>` (27 checked,
  0 differ); `sha256sum` over `.scratch/o08-traps/**` (§1 prefixes).
