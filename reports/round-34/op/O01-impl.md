- Seat: O01 | executor | claim O (operability) | date 2026-10-19 | baseline da68a6d

## Scope and deliverable

Claim O's executable **core**: the detection engine for `tools/harness/receipt_guard_adoption.py`
— walk every filed round runner, decide whether it writes its own `validation.json` in place,
decide whether it adopts `tools/harness/receipt_guard.py`, and emit an inventory JSON.

Hard boundary respected: **nothing was written outside `reports/round-34/op/O01-impl.md`.**
The durable tool file is a shared path, so it is *drafted here* and landed by the integrator
(same rule that governs the `tools/exercise-handoff-e2e.py` default change in claim D).
Nothing in this fragment executes a filed runner: the core is a reader/parser, and no
`reports/round-*/run-validation.py` was run in-tree (F-C13-1 prevention).

O02 owns the full tool bytes and the CLI; the core below is the reference implementation its
CLI should wrap (functions, classes and JSON field names are already fixed so O07's
row-for-row comparison against O04's predicted inventory is mechanical).

## Core contract

`scan_repository(root) -> dict` is the entry point. Per runner it returns `runner`, `class`,
`hazard`, `receipt_write_sites[]`, `embedded_receipt_writes`, `guard_loads[]`, `guard_calls[]`,
`refresh_flag_mentions[]`, `guard_call_before_write`, `guard_call_conditional`,
`guard_call_condition`, `lines`, `parse`.

Classification decision table, applied in this order:

| # | condition | class | hazard |
|---|---|---|---|
| 1 | no receipt-write site found | `no-receipt-write` | no |
| 2 | receipt write + a guard **call** site | `guard-adopted` | no |
| 3 | receipt write + guard **load**, no call | `guard-loaded-uncalled` | yes |
| 4 | receipt write, neither load nor call | `unguarded-writer` | yes |
| 5 | source does not parse | `could-not-evaluate` | n/a |

`hazard = (receipt write site exists) and (no guard call site)`. A `REFRESH_RECEIPTS`
mention or a guard-path string is recorded as an **attribute**, never as a class: a flag
reference must not launder an unguarded write into a clean row (this is exactly r21's shape).

### Detection rules (each earned from measured bytes, not guessed)

1. **Literal pass** — static string resolution of the write target: constants, name
   constants, f-strings, `+`, `/` path joins, `Path(...)`, `.resolve()/.parent/.parents`,
   `joinpath`, and single-argument wrapper calls such as `safe_path(OUTPUT)`.
   Earned by: r5:194 `(HERE / "validation.json").write_text(...)` (join),
   r26:1909 `safe_path(OUTPUT).write_text(...)` (wrapper), r14:717 / r8:1486 (local alias).
2. **Symbol pass** — receipt-constant propagation to a fixpoint: `OUTPUT =
   f"{ROUND_DIR}/validation.json"` → `output = ROOT / OUTPUT` → `output.write_text(...)`.
   Sites found only this way carry `resolution: "name-derived"` so a reviewer can audit the
   conservative match instead of trusting it.
3. **Write-site shapes** — `.write_text/.write_bytes`, `open(path, "w"|"a"|"x")`,
   `os.replace`/`os.rename`/`shutil.move`/`copy`/`copy2`/`copyfile` destination.
   The move family is why r12:1071 and the round-8 style `output = ROOT / OUTPUT` cannot
   hide behind a helper.
4. **Guard adoption evidence** — module import/`from-import`, `run_path(...receipt_guard.py)`,
   `spec_from_file_location(...receipt_guard.py)`, the guard-path string constant, calls to
   `guard_receipt`/`round_runner_main` (including the `namespace["guard_receipt"](...)`
   subscript form r26:1857 uses), and a local `def guard_receipt()` wrapper.
5. **Embedded-source pass** — string literals that themselves parse as Python (the
   `python -c` payload idiom), scanned with their own constant environment, with the
   payload-internal line mapped back to the **absolute file line** so citations are exact.

Path text in the table below is a placeholder-rooted path (`ROOT/...`) where the runner
derives the path from `Path(__file__)...`; that is a display convention, not a claim that the
literal string contains the word ROOT.

### Read-only guarantee

The core opens no runner for execution, imports none of them, and writes nothing except the
JSON handed to it by the caller. It uses only `ast`, `re`, `json`, `pathlib`, `hashlib`
(stdlib), and sets no environment variables.

## Core source (byte-exact as tested; sha256 a8d9e201a5afbb2ab0a4e35e992fc2a6cb7004d9c76e6ebd586773f264d34980)

```python
#!/usr/bin/env python3
"""Core detection logic for the receipt-guard adoption inventory (claim O).

Stdlib only. Read-only: never executes a scanned runner, never writes a receipt.
Two passes over each runner:
  1. literal pass  - static string resolution of the write target (incl. `/` joins
                     and wrapper calls such as `safe_path(OUTPUT)`)
  2. symbol pass   - receipt-constant propagation (`OUTPUT = f"{ROUND}/validation.json"`
                     -> `output = ROOT / OUTPUT` -> `output.write_text(...)`)
A site found only by the symbol pass is reported with resolution "name-derived"
so a reviewer can audit the conservative match.
"""
from __future__ import annotations

import ast
import json
from pathlib import Path
import re

RECEIPT_BASENAME = "validation.json"
GUARD_RELATIVE = "tools/harness/receipt_guard.py"
GUARD_MODULE = "receipt_guard"
REFRESH_ENV = "REFRESH_RECEIPTS"
RUNNER_GLOB = "reports/round-*/run-validation.py"

WRITE_METHODS = {"write_text", "write_bytes"}
WRITE_MODES = set("wax")
MOVE_FUNCS = {
    ("os", "replace"), ("os", "rename"), ("shutil", "move"), ("shutil", "copy"),
    ("shutil", "copy2"), ("shutil", "copyfile"),
}
GUARD_API = {"guard_receipt", "round_runner_main"}
GUARD_LOADERS = {"run_path", "spec_from_file_location"}

CLASSES = (
    "guard-adopted",
    "guard-loaded-uncalled",
    "guard-referenced-only",
    "unguarded-writer",
    "no-receipt-write",
    "could-not-evaluate",
)


def _literal(node, env, depth=0):
    """Statically resolve a string expression; None when not statically known."""
    if depth > 6 or node is None:
        return None
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name):
        return env.get(node.id)
    if isinstance(node, ast.Attribute):
        base = _literal(node.value, env, depth + 1)
        # only path-preserving attributes may stand in for their receiver; any
        # other attribute (`.name`, `.stem`, an object's field) is not a path
        return base if node.attr in {"resolve", "absolute", "expanduser", "as_posix",
                                     "parent", "parents"} else None
    if isinstance(node, ast.JoinedStr):
        parts = []
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                parts.append(value.value)
            elif isinstance(value, ast.FormattedValue):
                inner = _literal(value.value, env, depth + 1)
                if inner is None:
                    return None
                parts.append(inner)
            else:
                return None
        return "".join(parts)
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, ast.Add):
            left, right = _literal(node.left, env, depth + 1), _literal(node.right, env, depth + 1)
            return None if left is None or right is None else left + right
        if isinstance(node.op, ast.Div):  # Path("/a") / "b"
            left, right = _literal(node.left, env, depth + 1), _literal(node.right, env, depth + 1)
            return None if left is None or right is None else f"{left.rstrip('/')}/{right.lstrip('/')}"
    if isinstance(node, ast.Call):
        func = node.func
        name = func.attr if isinstance(func, ast.Attribute) else getattr(func, "id", None)
        if name in {"resolve", "absolute", "expanduser", "as_posix"} and not node.args:
            return _literal(func.value, env, depth + 1)
        if name == "parent" and isinstance(func, ast.Attribute):
            base = _literal(func.value, env, depth + 1)
            return None if base is None else str(Path(base).parent)
        if name in {"joinpath", "join"}:
            base = _literal(func.value, env, depth + 1) if isinstance(func, ast.Attribute) else None
            parts = [_literal(arg, env, depth + 1) for arg in node.args]
            if base is None and isinstance(func, ast.Attribute):
                return None
            if any(part is None for part in parts):
                return None
            return "/".join([part for part in [base, *parts] if part])
        if name == "Path" and len(node.args) == 1:
            return _literal(node.args[0], env, depth + 1)
        # wrapper call (safe_path(OUTPUT), str(OUTPUT), ...): single resolvable arg
        resolved_args = [_literal(arg, env, depth + 1) for arg in node.args]
        known = [value for value in resolved_args if value is not None]
        if len(known) == 1 and (len(resolved_args) == 1 or name in {"safe_path", "str", "Path"}):
            return known[0]
    if isinstance(node, ast.Subscript):
        return _literal(node.value, env, depth + 1)
    return None


def names_in(node):
    return {child.id for child in ast.walk(node) if isinstance(child, ast.Name)}


def module_constants(tree):
    """Module-level name -> literal string, iterated to a fixpoint so A = B works."""
    env = {"__file__": "ROOT/reports/round-N/run-validation.py"}
    for _ in range(5):
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign) and len(node.targets) == 1:
                target = node.targets[0]
                if isinstance(target, ast.Name):
                    value = _literal(node.value, env)
                    if value is not None and env.get(target.id) != value:
                        env[target.id] = value
                        changed = True
        if not changed:
            break
    return env


def receipt_symbols(tree, env):
    """Names statically bound (module or local) to a path ending in validation.json."""
    symbols = {name for name, value in env.items() if contains_receipt(value)}
    for _ in range(5):
        added = False
        for node in ast.walk(tree):
            if not isinstance(node, ast.Assign):
                continue
            value_names = names_in(node.value)
            value_literal = _literal(node.value, env)
            hit = (value_literal is not None and contains_receipt(value_literal)) or bool(
                value_names & symbols)
            if not hit:
                continue
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id not in symbols:
                    symbols.add(target.id)
                    added = True
        if not added:
            break
    return symbols


def contains_receipt(text):
    return bool(text) and (text == RECEIPT_BASENAME or text.endswith("/" + RECEIPT_BASENAME)
                           or RECEIPT_BASENAME in text)


def resolution(node, env, symbols):
    """('literal'|'name-derived'|None, resolved_path_or_None)."""
    resolved = _literal(node, env)
    if resolved is not None and contains_receipt(resolved):
        return "literal", resolved
    if names_in(node) & symbols:
        return "name-derived", None
    return None, None


def write_sites(tree, env, symbols):
    """Every candidate receipt-write call site in one syntax tree."""
    sites = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        kind = None
        target_node = None
        if isinstance(func, ast.Attribute) and func.attr in WRITE_METHODS:
            kind, target_node = func.attr, func.value
        elif isinstance(func, (ast.Attribute, ast.Name)) and (
                func.attr if isinstance(func, ast.Attribute) else func.id) == "open":
            mode = _literal(node.args[1], env) if len(node.args) > 1 else None
            for keyword in node.keywords:
                if keyword.arg == "mode":
                    mode = _literal(keyword.value, env)
            if mode and any(char in mode for char in WRITE_MODES):
                kind = "open-w"
                target_node = func.value if isinstance(func, ast.Attribute) else (
                    node.args[0] if node.args else None)
        elif isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
            if (func.value.id, func.attr) in MOVE_FUNCS and len(node.args) >= 2:
                kind, target_node = f"{func.value.id}.{func.attr}", node.args[1]
        if kind is None or target_node is None:
            continue
        how, resolved = resolution(target_node, env, symbols)
        if how is None:
            continue
        sites.append({
            "line": node.lineno,
            "kind": kind,
            "target_expr": ast.unparse(target_node),
            "target_resolved": resolved,
            "resolution": how,
        })
    return sites


def guard_signals(tree, source, env):
    """Load / call / flag evidence for tools/harness/receipt_guard.py adoption."""
    loads, calls, flags = [], [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[-1] == GUARD_MODULE:
                    loads.append({"line": node.lineno, "form": "import",
                                  "detail": f"import {alias.name}"})
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            if module.split(".")[-1] == GUARD_MODULE:
                loads.append({"line": node.lineno, "form": "from-import",
                              "detail": f"from {module} import ..."})
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            text = node.value
            if REFRESH_ENV in text:
                flags.append({"line": node.lineno, "form": "refresh-flag",
                              "detail": REFRESH_ENV})
            if GUARD_RELATIVE in text:
                loads.append({"line": node.lineno, "form": "guard-path-constant",
                              "detail": text.strip().splitlines()[0][:60]})
        elif isinstance(node, ast.Call):
            func = node.func
            name = func.attr if isinstance(func, ast.Attribute) else getattr(func, "id", None)
            if name in GUARD_API and not (isinstance(func, ast.Name) and func.id in
                                          {"guard_receipt"} and node.lineno == 0):
                calls.append({"line": node.lineno, "form": name,
                              "detail": ast.unparse(node)[:80]})
            elif isinstance(func, ast.Subscript):
                key = _literal(func.slice, env)
                if key in GUARD_API:
                    calls.append({"line": node.lineno, "form": f"subscript:{key}",
                                  "detail": ast.unparse(node)[:80]})
            elif name in GUARD_LOADERS or (
                    isinstance(func, ast.Attribute) and func.attr == "run_path"):
                for arg in [*node.args, *[kw.value for kw in node.keywords]]:
                    value = _literal(arg, env)
                    if value and GUARD_RELATIVE in value:
                        loads.append({"line": node.lineno, "form": f"loader:{name}",
                                      "detail": ast.unparse(node)[:80]})
                        break
        elif isinstance(node, ast.FunctionDef) and node.name in GUARD_API:
            calls.append({"line": node.lineno, "form": f"def:{node.name}",
                          "detail": f"local guard wrapper {node.name}()"})
    return loads, calls, flags


def embedded_sources(tree):
    """String literals that themselves parse as Python (e.g. python -c payloads)."""
    payloads = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Constant) or not isinstance(node.value, str):
            continue
        text = node.value
        if RECEIPT_BASENAME not in text and REFRESH_ENV not in text:
            continue
        if "import " not in text and "write_text" not in text:
            continue
        try:
            inner = ast.parse(text)
        except SyntaxError:
            continue
        payloads.append({"line": node.lineno, "tree": inner, "text": text})
    return payloads


def _conditional_call(tree, line):
    """True when the call at `line` sits under an If testing a flag/argv/check."""
    for node in ast.walk(tree):
        if not isinstance(node, ast.If):
            continue
        span = [child.lineno for child in ast.walk(node) if hasattr(child, "lineno")]
        if not span or not (min(span) <= line <= max(span)):
            continue
        test = ast.unparse(node.test)
        if re.search(r"argv|flag|refresh|args\.|check", test):
            return True, test[:60]
    return False, None


def scan_runner(path, root):
    """Classify one filed round runner. Read-only."""
    source = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source)
    except SyntaxError as error:
        return {
            "runner": path.relative_to(root).as_posix(),
            "class": "could-not-evaluate",
            "reason": f"SyntaxError: {error.msg} at line {error.lineno}",
            "parse": "failed",
        }
    env = module_constants(tree)
    symbols = receipt_symbols(tree, env)
    sites = write_sites(tree, env, symbols)
    loads, calls, flags = guard_signals(tree, source, env)
    embedded = []
    for payload in embedded_sources(tree):
        inner_env = module_constants(payload["tree"])
        inner_symbols = receipt_symbols(payload["tree"], inner_env)
        for site in write_sites(payload["tree"], inner_env, inner_symbols):
            # map the payload-internal line onto the file line so the citation is
            # absolute (r19's write lives at file line 21 inside a python -c payload)
            site["payload_line"] = site["line"]
            site["line"] = payload["line"] + site["line"] - 1
            site["embedded_at_line"] = payload["line"]
            embedded.append(site)
        inner_loads, inner_calls, inner_flags = guard_signals(
            payload["tree"], payload["text"], inner_env)
        loads.extend(inner_loads)
        calls.extend(inner_calls)
        flags.extend(inner_flags)
    effective = sites or embedded
    call_lines = sorted({item["line"] for item in calls})
    load_lines = sorted({item["line"] for item in loads})
    if not effective:
        klass = "no-receipt-write"
    elif call_lines:
        klass = "guard-adopted"
    elif load_lines:
        klass = "guard-loaded-uncalled"
    else:
        # A REFRESH_RECEIPTS mention or a guard-path reference does not protect a
        # write: it stays an unguarded in-place writer, with the mention recorded
        # as an attribute so the flag can never launder the hazard class.
        klass = "unguarded-writer"
    write_lines = sorted({site["line"] for site in effective})
    conditional, test = _conditional_call(tree, call_lines[0]) if call_lines else (None, None)
    return {
        "runner": path.relative_to(root).as_posix(),
        "class": klass,
        "hazard": bool(effective) and not call_lines,
        "parse": "ok",
        "receipt_write_sites": effective,
        "embedded_receipt_writes": bool(embedded),
        "guard_loads": loads,
        "guard_calls": calls,
        "refresh_flag_mentions": flags,
        "guard_call_before_write": bool(call_lines and write_lines
                                       and call_lines[0] <= write_lines[0]),
        "guard_call_conditional": conditional,
        "guard_call_condition": test,
        "lines": len(source.splitlines()),
    }


def scan_repository(root):
    root = Path(root).resolve()
    records = [scan_runner(path, root) for path in sorted(root.glob(RUNNER_GLOB))]
    counts = {}
    for record in records:
        counts[record["class"]] = counts.get(record["class"], 0) + 1
    return {
        "tool": "tools/harness/receipt_guard_adoption.py",
        "mode": "inventory",
        "root": str(root),
        "runner_count": len(records),
        "class_counts": counts,
        "runners": records,
    }


if __name__ == "__main__":
    import sys
    print(json.dumps(scan_repository(sys.argv[1] if len(sys.argv) > 1 else "."), indent=1))
```

## Measured inventory — 28/28 filed runners at baseline da68a6d

Produced by the core above; inventory digest sha256 `027983b1b43d752cd1330fe3a8374e883937d0338eb88df5d1da182eb54eef8a`.
Independent cross-check on the same tree: `grep -l receipt_guard reports/round-*/run-validation.py | wc -l`
= **17**, `grep -L receipt_guard reports/round-*/run-validation.py | wc -l` = **11**,
`ls reports/round-*/run-validation.py | wc -l` = **28** — matching the classes below 17/11/28.

Class counts: **guard-adopted 17**, **unguarded-writer 11**, `guard-loaded-uncalled` 0,
`no-receipt-write` 0, `could-not-evaluate` 0.
Hazard set (11): round-10, round-11, round-12, round-19, round-21, round-29, round-5, round-6, round-7, round-8, round-9.
Adopted set (17): round-14, round-15, round-16, round-17, round-18, round-20, round-22, round-23, round-24, round-25, round-26, round-27, round-28, round-30, round-31, round-32, round-33.

| runner | class | write site | guard load | guard call | call before write | flag mention | embedded |
|---|---|---|---|---|---|---|---|
| `reports/round-10/run-validation.py` | unguarded-writer | :1054 (write_text) | — | — | no | — | no |
| `reports/round-11/run-validation.py` | unguarded-writer | :1740 (write_text) | — | — | no | — | no |
| `reports/round-12/run-validation.py` | unguarded-writer | :1071 (write_text) | — | — | no | — | no |
| `reports/round-14/run-validation.py` | guard-adopted | :717 (write_text) | :25, :414 | :420 | yes | :439, :445 | no |
| `reports/round-15/run-validation.py` | guard-adopted | :1346 (write_text) | :1038, :44 | :1044 | yes | — | no |
| `reports/round-16/run-validation.py` | guard-adopted | :1265 (write_text) | :57, :999 | :1005 | yes | — | no |
| `reports/round-17/run-validation.py` | guard-adopted | :1431 (write_text) | :1118, :68 | :1124 | yes | — | no |
| `reports/round-18/run-validation.py` | guard-adopted | :1851 (write_text) | :1512, :67 | :1518 | yes | — | no |
| `reports/round-19/run-validation.py` | unguarded-writer | :21 (write_text) | — | — | no | — | yes |
| `reports/round-20/run-validation.py` | guard-adopted | :1485 (write_text) | :1279, :57 | :1285 | yes | — | no |
| `reports/round-21/run-validation.py` | unguarded-writer | :1115 (write_text) | — | — | no | :1106, :474 | no |
| `reports/round-22/run-validation.py` | guard-adopted | :922 (write_text) | :828 | :827, :829, :911, :921 | yes | — | no |
| `reports/round-23/run-validation.py` | guard-adopted | :1097 (write_text) | :1065 | :1064, :1066, :1094 | yes | — | no |
| `reports/round-24/run-validation.py` | guard-adopted | :1184 (write_text) | :1152 | :1151, :1153, :1181 | yes | — | no |
| `reports/round-25/run-validation.py` | guard-adopted | :1145 (write_text) | :1109, :173 | :1108, :1110, :1142 | yes | — | no |
| `reports/round-26/run-validation.py` | guard-adopted | :1909 (write_text) | :1856, :199 | :1855, :1857, :1906 | yes | — | no |
| `reports/round-27/run-validation.py` | guard-adopted | :1907 (write_text) | :1854, :222 | :1853, :1855, :1904 | yes | — | no |
| `reports/round-28/run-validation.py` | guard-adopted | :2098 (write_text) | :1997, :231 | :1996, :1998, :2095 | yes | — | no |
| `reports/round-29/run-validation.py` | unguarded-writer | :922 (write_text) | — | — | no | — | no |
| `reports/round-30/run-validation.py` | guard-adopted | :923 (write_text) | :884 | :883, :885, :903, :922 | yes | — | no |
| `reports/round-31/run-validation.py` | guard-adopted | :1159 (write_text) | :1119 | :1118, :1120, :1139, :1158 | yes | — | no |
| `reports/round-32/run-validation.py` | guard-adopted | :1143 (write_text) | :1103 | :1102, :1104, :1123, :1142 | yes | — | no |
| `reports/round-33/run-validation.py` | guard-adopted | :1471 (write_text) | :1442 | :1441, :1443, :1459, :1470 | yes | — | no |
| `reports/round-5/run-validation.py` | unguarded-writer | :194 (write_text) | — | — | no | — | no |
| `reports/round-6/run-validation.py` | unguarded-writer | :336 (write_text) | — | — | no | — | no |
| `reports/round-7/run-validation.py` | unguarded-writer | :1171 (write_text) | — | — | no | — | no |
| `reports/round-8/run-validation.py` | unguarded-writer | :1486 (write_text) | — | — | no | — | no |
| `reports/round-9/run-validation.py` | unguarded-writer | :1910 (write_text) | — | — | no | — | no |

Machine-readable rows for row-for-row comparison (same fields as the tool's per-runner records):

```json
[
 {
  "runner": "reports/round-10/run-validation.py",
  "class": "unguarded-writer",
  "hazard": true,
  "receipt_write_sites": [
   {
    "line": 1054,
    "kind": "write_text",
    "target_expr": "output",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-10/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [],
  "guard_call_lines": [],
  "guard_call_before_write": false,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1069
 },
 {
  "runner": "reports/round-11/run-validation.py",
  "class": "unguarded-writer",
  "hazard": true,
  "receipt_write_sites": [
   {
    "line": 1740,
    "kind": "write_text",
    "target_expr": "output",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-11/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [],
  "guard_call_lines": [],
  "guard_call_before_write": false,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1755
 },
 {
  "runner": "reports/round-12/run-validation.py",
  "class": "unguarded-writer",
  "hazard": true,
  "receipt_write_sites": [
   {
    "line": 1071,
    "kind": "write_text",
    "target_expr": "out",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-12/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [],
  "guard_call_lines": [],
  "guard_call_before_write": false,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1082
 },
 {
  "runner": "reports/round-14/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 717,
    "kind": "write_text",
    "target_expr": "ROOT / OUTPUT",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-14/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   25,
   414
  ],
  "guard_call_lines": [
   420
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [
   439,
   445
  ],
  "embedded_receipt_writes": false,
  "lines": 727
 },
 {
  "runner": "reports/round-15/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 1346,
    "kind": "write_text",
    "target_expr": "ROOT / OUTPUT",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-15/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   44,
   1038
  ],
  "guard_call_lines": [
   1044
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1357
 },
 {
  "runner": "reports/round-16/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 1265,
    "kind": "write_text",
    "target_expr": "ROOT / OUTPUT",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-16/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   57,
   999
  ],
  "guard_call_lines": [
   1005
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1276
 },
 {
  "runner": "reports/round-17/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 1431,
    "kind": "write_text",
    "target_expr": "ROOT / OUTPUT",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-17/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   68,
   1118
  ],
  "guard_call_lines": [
   1124
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1442
 },
 {
  "runner": "reports/round-18/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 1851,
    "kind": "write_text",
    "target_expr": "ROOT / OUTPUT",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-18/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   67,
   1512
  ],
  "guard_call_lines": [
   1518
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1862
 },
 {
  "runner": "reports/round-19/run-validation.py",
  "class": "unguarded-writer",
  "hazard": true,
  "receipt_write_sites": [
   {
    "line": 21,
    "kind": "write_text",
    "target_expr": "pathlib.Path('reports/round-19/validation.json')",
    "target_resolved": "reports/round-19/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [],
  "guard_call_lines": [],
  "guard_call_before_write": false,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": true,
  "lines": 24
 },
 {
  "runner": "reports/round-20/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 1485,
    "kind": "write_text",
    "target_expr": "ROOT / OUTPUT",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-20/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   57,
   1279
  ],
  "guard_call_lines": [
   1285
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1498
 },
 {
  "runner": "reports/round-21/run-validation.py",
  "class": "unguarded-writer",
  "hazard": true,
  "receipt_write_sites": [
   {
    "line": 1115,
    "kind": "write_text",
    "target_expr": "output",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-21/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [],
  "guard_call_lines": [],
  "guard_call_before_write": false,
  "refresh_flag_lines": [
   474,
   1106
  ],
  "embedded_receipt_writes": false,
  "lines": 1126
 },
 {
  "runner": "reports/round-22/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 922,
    "kind": "write_text",
    "target_expr": "safe_path(OUTPUT)",
    "target_resolved": "reports/round-22/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   828
  ],
  "guard_call_lines": [
   827,
   829,
   911,
   921
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 932
 },
 {
  "runner": "reports/round-23/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 1097,
    "kind": "write_text",
    "target_expr": "safe_path(OUTPUT)",
    "target_resolved": "reports/round-23/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   1065
  ],
  "guard_call_lines": [
   1064,
   1066,
   1094
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1107
 },
 {
  "runner": "reports/round-24/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 1184,
    "kind": "write_text",
    "target_expr": "safe_path(OUTPUT)",
    "target_resolved": "reports/round-24/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   1152
  ],
  "guard_call_lines": [
   1151,
   1153,
   1181
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1194
 },
 {
  "runner": "reports/round-25/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 1145,
    "kind": "write_text",
    "target_expr": "safe_path(OUTPUT)",
    "target_resolved": "reports/round-25/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   173,
   1109
  ],
  "guard_call_lines": [
   1108,
   1110,
   1142
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1155
 },
 {
  "runner": "reports/round-26/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 1909,
    "kind": "write_text",
    "target_expr": "safe_path(OUTPUT)",
    "target_resolved": "reports/round-26/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   199,
   1856
  ],
  "guard_call_lines": [
   1855,
   1857,
   1906
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1919
 },
 {
  "runner": "reports/round-27/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 1907,
    "kind": "write_text",
    "target_expr": "safe_path(OUTPUT)",
    "target_resolved": "reports/round-27/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   222,
   1854
  ],
  "guard_call_lines": [
   1853,
   1855,
   1904
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1917
 },
 {
  "runner": "reports/round-28/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 2098,
    "kind": "write_text",
    "target_expr": "safe_path(OUTPUT)",
    "target_resolved": "reports/round-28/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   231,
   1997
  ],
  "guard_call_lines": [
   1996,
   1998,
   2095
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 2108
 },
 {
  "runner": "reports/round-29/run-validation.py",
  "class": "unguarded-writer",
  "hazard": true,
  "receipt_write_sites": [
   {
    "line": 922,
    "kind": "write_text",
    "target_expr": "safe_path(OUTPUT)",
    "target_resolved": "reports/round-29/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [],
  "guard_call_lines": [],
  "guard_call_before_write": false,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 931
 },
 {
  "runner": "reports/round-30/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 923,
    "kind": "write_text",
    "target_expr": "safe_path(OUTPUT)",
    "target_resolved": "reports/round-30/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   884
  ],
  "guard_call_lines": [
   883,
   885,
   903,
   922
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 934
 },
 {
  "runner": "reports/round-31/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 1159,
    "kind": "write_text",
    "target_expr": "safe_path(OUTPUT)",
    "target_resolved": "reports/round-31/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   1119
  ],
  "guard_call_lines": [
   1118,
   1120,
   1139,
   1158
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1170
 },
 {
  "runner": "reports/round-32/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 1143,
    "kind": "write_text",
    "target_expr": "safe_path(OUTPUT)",
    "target_resolved": "reports/round-32/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   1103
  ],
  "guard_call_lines": [
   1102,
   1104,
   1123,
   1142
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1154
 },
 {
  "runner": "reports/round-33/run-validation.py",
  "class": "guard-adopted",
  "hazard": false,
  "receipt_write_sites": [
   {
    "line": 1471,
    "kind": "write_text",
    "target_expr": "safe_path(OUTPUT)",
    "target_resolved": "reports/round-33/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [
   1442
  ],
  "guard_call_lines": [
   1441,
   1443,
   1459,
   1470
  ],
  "guard_call_before_write": true,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1478
 },
 {
  "runner": "reports/round-5/run-validation.py",
  "class": "unguarded-writer",
  "hazard": true,
  "receipt_write_sites": [
   {
    "line": 194,
    "kind": "write_text",
    "target_expr": "HERE / 'validation.json'",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-5/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [],
  "guard_call_lines": [],
  "guard_call_before_write": false,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 210
 },
 {
  "runner": "reports/round-6/run-validation.py",
  "class": "unguarded-writer",
  "hazard": true,
  "receipt_write_sites": [
   {
    "line": 336,
    "kind": "write_text",
    "target_expr": "HERE / 'validation.json'",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-6/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [],
  "guard_call_lines": [],
  "guard_call_before_write": false,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 349
 },
 {
  "runner": "reports/round-7/run-validation.py",
  "class": "unguarded-writer",
  "hazard": true,
  "receipt_write_sites": [
   {
    "line": 1171,
    "kind": "write_text",
    "target_expr": "HERE / 'validation.json'",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-7/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [],
  "guard_call_lines": [],
  "guard_call_before_write": false,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1192
 },
 {
  "runner": "reports/round-8/run-validation.py",
  "class": "unguarded-writer",
  "hazard": true,
  "receipt_write_sites": [
   {
    "line": 1486,
    "kind": "write_text",
    "target_expr": "output",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-8/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [],
  "guard_call_lines": [],
  "guard_call_before_write": false,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1498
 },
 {
  "runner": "reports/round-9/run-validation.py",
  "class": "unguarded-writer",
  "hazard": true,
  "receipt_write_sites": [
   {
    "line": 1910,
    "kind": "write_text",
    "target_expr": "output",
    "target_resolved": "ROOT/reports/round-N/run-validation.py/reports/round-9/validation.json",
    "resolution": "literal"
   }
  ],
  "guard_load_lines": [],
  "guard_call_lines": [],
  "guard_call_before_write": false,
  "refresh_flag_lines": [],
  "embedded_receipt_writes": false,
  "lines": 1943
 }
]
```

## Findings

**F1 — the unguarded-writer set is 11 runners, not the 4 named in the claim.** Measured
in-place receipt writes with no guard call: r5:194, r6:336, r7:1171 (the three in
`LOG.md:3548-3566`), r8:1486, r9:1910, r10:1054, r11:1740, r12:1071, r19:21, r21:1115,
r29:922. The routing table (O05) and the adoption-gap debt row are therefore larger than the
claim's "four known hazards" phrasing; the three LOG-named runners are a subset, not the set.

**F2 — r26 measures as guard-adopted, contradicting its hazard framing.** `LOG.md:3559-3561`
lists r26 as carrying "the same hazard (`:90`, `:1909`)". Measured: r26:1856 loads the guard
via `runpy.run_path`, r26:1857 calls `namespace["guard_receipt"](OUTPUT, repo_root=ROOT)`,
and the write at r26:1909 sits on the guarded branch after `guard_receipt()` at r26:1906
(its `:90` reference is the `OUTPUT` constant, not a write). Reported as a **wording
discrepancy resolved in favour of the bytes** — no filed byte is edited, and no claim of
r26 being clean beyond this evidence is made. The same hold for r27:1855/1904/1907 and
r28:1997/1998/2095, which the claim's hazard list does not name.

**F3 — an embedded `python -c` payload can hide a receipt write from a module-body-only AST
pass.** r19 is 24 lines; its receipt write lives at absolute file line 21 inside the payload
string that starts at r19:5 (`sys.executable, "-c", """`), and it rewrites the filed
`reports/round-19/validation.json` in place with no guard. A tool that walks only the module
body classifies r19 `no-receipt-write` — a false green. The core's embedded pass reports the
absolute line (21, `payload_line` 17) so the citation matches `sed -n '21p'`.

**F4 — a flag mention is not protection.** r21 writes its receipt in place at r21:1115 with no
guard at all, while mentioning `REFRESH_RECEIPTS` only where it sets the variable for
isolated clones (r21:474) and describes that policy (r21:1106). Classifying r21 by the flag
would launder a hazard row into a clean one; the core keeps it `unguarded-writer` and records
the flag as an attribute. Routing note for O05: r21 also rewrites another filed runner's
source inside its clone (r21:472, r18's `OUTSIDE_TMP_CANDIDATES`), so its isolated-copy
protocol must preserve the clone-only guarantee.

**F5 — the gap is not merely chronological.** Adopted rounds run r14-r18, r20, r22-r28,
r30-r33; the gaps r19, r21 and r29 sit *inside* that adopted span. A "round ≥ 14 ⇒ guarded"
rule of thumb would be wrong in three places, which is why the inventory is measured per
runner instead of inferred from round number.

**F6 — two adoption idioms exist and both must be recognised.** r14 loads the guard with
`importlib.util.spec_from_file_location` (r14:414) and calls it (r14:420, invoked from
r14:708/r14:716); r15 onward use the `runpy.run_path` wrapper (e.g. r26:1856, r32:1103,
r33:1442). The core accepts both, plus the guard-path string constant that both idioms share.

## Control fixtures already exercised

Built in scratch (`.scratch/o01/traps/`), each run through `scan_runner` on the same core
bytes filed above:

| fixture | shape | measured class | expected |
|---|---|---|---|
| `t1_import_only.py` | `import receipt_guard`, write, never called | `guard-loaded-uncalled` | yes |
| `t2_flag_only.py` | write with no guard reference at all | `unguarded-writer` | yes |
| `t3_os_replace.py` | write to temp then `os.replace` onto the receipt | `unguarded-writer` | yes |
| `t4_clean_guard.py` | `runpy` load + call immediately before the write | `guard-adopted` | yes |
| `t5_nonrunner.py` | non-runner writing `reports/index.json` | `no-receipt-write` | yes |

O03 owns the final selftest control spec and O07/O08 own verification; these five are
existence proof that the core has a positive and four negatives, not the selftest itself.

## What O02's CLI must add (and must not re-derive)

- `--selftest` (controls per O03), `--json` (this inventory), `--root`, optional
  `--runner PATH`; exit 0 = inventory produced, non-zero only on real failure.
- Dedupe repeated `guard_loads` entries that share a line but differ in form (the
  guard-path constant and the loader call legitimately land on one line, e.g. r26:1856).
- Deterministic ordering (sorted by runner path) and a `generated_at` + `runner_count`
  header; never write outside stdout/the caller's out path.
- Must NOT re-implement path resolution: reuse `_literal`/`receipt_symbols`/`write_sites`
  verbatim, otherwise the 17/11 split above stops being reproducible.

## Independent corroboration (fragments filed after my census)

Sibling seats landed after this seat's census and were measured independently of it:

- `reports/round-34/op/O05-routing.md:99` reports "**28 runners, 11 unguarded, 17 guarded**" and
  its §2.1 table lists the same 11 write sites (r5:194, r6:336, r7:1171, r8:1486, r9:1910,
  r10:1054, r11:1740, r12:1071, r19:21, r21:1115, r29:922) with the same guarded/adopted rows
  (e.g. r26 write 1909 / guard 1906).
- `reports/round-34/op/O09-verify-routing.md:12-18` states it built its own AST census
  instrument (`.scratch/o09/census.py`) rather than reusing mine or O02's.

Three instruments (this seat's core, O05's scan, O09's census) independently agree on the
28/11/17 split, which is the strongest available evidence for the hazard set at this baseline.
This is corroboration, not verification: O07/O09 own the row-for-row diff, and the wording in
`LOG.md:3559-3561` about r26 (F2) still stands as filed.

## Owed

- `reports/round-34/scout/K03-guard-pattern.md` and `reports/round-34/plan/P02-oc-plan.md`
  did not exist at scan time (K03/P02 seats still running). No blocking: I ran my own
  read-only census over the 28 runners instead of consuming theirs, and this fragment's
  findings are independent of them. The integrator should reconcile K03's classification
  taxonomy and P02's architecture note against the decision table above; where they differ,
  the measured classes in this fragment are the ones with per-line evidence.
- The landed tool path `tools/harness/receipt_guard_adoption.py` and its selftest are O02's
  bytes plus the integrator's land act — not written by this seat by boundary.

## Citations

- Seat assignment: `reports/round-34/targets.json` (seat `O01`), `reports/round-34/claims.json` claim `O`.
- Hazard record: `LOG.md:3548-3566` (F-C13-1, mechanism lines r5:194 / r6:336 / r7:1171, r26 `:90`/`:1909`).
- Runner census: `ls reports/round-*/run-validation.py` (28 files, rounds 5-12 and 14-33).
- Guard mention counts: `grep -l receipt_guard reports/round-*/run-validation.py | wc -l` = 17;
  `grep -L receipt_guard reports/round-*/run-validation.py | wc -l` = 11;
  `grep -c REFRESH_RECEIPTS reports/round-*/run-validation.py | grep -v ':0'` = r14 (2), r21 (2).
- Measured write/guard sites cited above: r5:194, r6:336, r7:1171, r8:1486, r9:1910, r10:1054,
  r11:1740, r12:1071, r14:414/420/708/717, r19:5/21, r21:472/474/1106/1115, r26:1856/1857/1906/1909,
  r27:1855/1904/1907, r28:1997/1998/2095, r29:922, r32:1103/1143, r33:1442/1471.
- `sed -n '21p' reports/round-19/run-validation.py` → `pathlib.Path('reports/round-19/validation.json').write_text(json.dumps(v,...))`.
- Core source and inventory digests: sha256(core) = `a8d9e201a5afbb2ab0a4e35e992fc2a6cb7004d9c76e6ebd586773f264d34980`, sha256(inventory) = `027983b1b43d752cd1330fe3a8374e883937d0338eb88df5d1da182eb54eef8a`
  (measured in scratch under `TMPDIR=$PWD/.scratch`, `python3 -B`); the durable copy of both is
  the fenced blocks in this fragment.
- Commands run (all read-only): the core's `__main__` over `.` — `python3 -B <core.py> .` — and
  the five trap fixtures through `scan_runner`.
