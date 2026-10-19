- Seat: O02 | executor | O | date 2026-10-19 | baseline 456674d

```python
#!/usr/bin/env python3
"""Static conformance audit for acceptance runners; never executes a runner."""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

TOOL = "tools/harness/round_runner_conformance.py"
ROOT = Path(__file__).resolve().parents[2]
ROUNDS = tuple(range(34, 41))
ROOT_EXPR = re.compile(r"(?:[A-Za-z_]\w*\.)*Path\(__file__\)\.resolve\(\)\.parents\[2\]")
ROUND_PART = re.compile(r"^round-(\d+)$")
WRITE_FLAGS = frozenset("wax+")
GUARD_NAMES = {"guard_receipt", "round_runner_main"}


def _targets(node):
    if isinstance(node, ast.Name):
        return [node.id]
    if isinstance(node, (ast.Tuple, ast.List)):
        return [name for item in node.elts for name in _targets(item)]
    return []


def _resolve(node, constants, runner_path, depth=8):
    if node is None or depth < 0:
        return None
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        if node.id == "__file__":
            return str(runner_path)
        return constants.get(node.id)
    if isinstance(node, ast.JoinedStr):
        parts = []
        for item in node.values:
            if isinstance(item, ast.Constant) and isinstance(item.value, str):
                parts.append(item.value)
            elif isinstance(item, ast.FormattedValue):
                value = _resolve(item.value, constants, runner_path, depth - 1)
                if value is None:
                    return None
                parts.append(str(value))
            else:
                return None
        return "".join(parts)
    if isinstance(node, ast.BinOp):
        left = _resolve(node.left, constants, runner_path, depth - 1)
        right = _resolve(node.right, constants, runner_path, depth - 1)
        if isinstance(node.op, ast.Add) and left is not None and right is not None:
            return str(left) + str(right)
        if isinstance(node.op, ast.Div):
            if left is None:
                return right
            if right is None:
                return left
            return str(Path(str(left)) / str(right))
    if isinstance(node, ast.Attribute):
        value = _resolve(node.value, constants, runner_path, depth - 1)
        if node.attr == "resolve":
            return value
        if node.attr == "parent" and value is not None:
            return str(Path(str(value)).parent)
    if isinstance(node, ast.Subscript):
        value = _resolve(node.value, constants, runner_path, depth - 1)
        index = node.slice.value if isinstance(node.slice, ast.Constant) else None
        if isinstance(index, int) and value is not None:
            if isinstance(node.value, ast.Attribute) and node.value.attr == "parents":
                return str(Path(str(value)).parents[index])
            if isinstance(value, (list, tuple)) and -len(value) <= index < len(value):
                return value[index]
    if isinstance(node, ast.Call):
        func = node.func
        name = ast.unparse(func)
        if name in ("str", "Path", "pathlib.Path") and node.args:
            return _resolve(node.args[0], constants, runner_path, depth - 1)
        if isinstance(func, ast.Attribute) and func.attr == "with_name" and node.args:
            base = _resolve(func.value, constants, runner_path, depth - 1)
            name_part = _resolve(node.args[0], constants, runner_path, depth - 1)
            if base is not None and name_part is not None:
                return str(Path(str(base)).with_name(str(name_part)))
        if isinstance(func, ast.Attribute) and func.attr == "joinpath":
            base = _resolve(func.value, constants, runner_path, depth - 1)
            parts = [_resolve(arg, constants, runner_path, depth - 1) for arg in node.args]
            if base is not None and all(part is not None for part in parts):
                return str(Path(str(base)).joinpath(*(str(part) for part in parts)))
        if name in ("os.path.join", "posixpath.join"):
            parts = [_resolve(arg, constants, runner_path, depth - 1) for arg in node.args]
            if all(part is not None for part in parts):
                return os.path.join(*(str(part) for part in parts))
    return None


def _constants(tree, runner_path):
    constants = {}
    assignments = sorted(
        (node for node in ast.walk(tree) if isinstance(node, (ast.Assign, ast.AnnAssign))),
        key=lambda node: (node.lineno, node.col_offset),
    )
    for _ in range(5):
        for node in assignments:
            value_node = node.value
            if value_node is None:
                continue
            value = _resolve(value_node, constants, runner_path)
            if value is None:
                continue
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                for name in _targets(target):
                    constants[name] = value
    return constants


def _root_assignments(tree):
    found = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if any("ROOT" in _targets(target) for target in node.targets):
                found.append((node.value, node.lineno))
        elif isinstance(node, ast.AnnAssign) and "ROOT" in _targets(node.target):
            found.append((node.value, node.lineno))
    return found


def _root_checks(tree, constants, runner_path):
    assignments = _root_assignments(tree)
    relative = any(ROOT_EXPR.search(ast.unparse(value)) for value, _ in assignments if value is not None)
    absolute = False
    if not relative:
        for value, _ in assignments:
            resolved = _resolve(value, constants, runner_path)
            if isinstance(resolved, str) and Path(resolved).is_absolute():
                absolute = True
            if any(isinstance(item, ast.Constant) and isinstance(item.value, str)
                   and Path(item.value).is_absolute() for item in ast.walk(value)):
                absolute = True
    lines = [line for node in ast.walk(tree) if isinstance(node, ast.Call)
             and ((isinstance(node.func, ast.Attribute) and node.func.attr == "chdir")
                  or (isinstance(node.func, ast.Name) and node.func.id == "chdir"))
             for line in [node.lineno]]
    return relative, absolute, sorted(set(lines)), assignments


def _dict_fields(tree):
    candidates = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        fields = {}
        for key, value in zip(node.keys, node.values):
            if isinstance(key, ast.Constant) and isinstance(key.value, str):
                fields[key.value] = value
        score = sum(key in fields for key in ("runner_sha256", "limits", "named_findings", "round"))
        if score:
            candidates.append((score, fields, node.lineno))
    return max(candidates, key=lambda item: (item[0], item[2]))[1] if candidates else {}


def _static_value(node, constants, runner_path):
    if isinstance(node, (ast.List, ast.Tuple)):
        return [_static_value(item, constants, runner_path) for item in node.elts]
    if isinstance(node, ast.Dict):
        return {_static_value(key, constants, runner_path): _static_value(value, constants, runner_path)
                for key, value in zip(node.keys, node.values)}
    return _resolve(node, constants, runner_path)


def _sha_expression_ok(node, functions, constants, runner_path):
    if node is None or isinstance(node, ast.Constant) and node.value is None:
        return False
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Attribute) and node.func.attr == "hexdigest":
            return True
        if isinstance(node.func, ast.Name) and node.func.id in functions:
            returns = [item.value for item in ast.walk(functions[node.func.id])
                       if isinstance(item, ast.Return)]
            return any(value is not None and not (isinstance(value, ast.Constant) and value.value is None)
                       for value in returns)
        return "hexdigest" in ast.unparse(node) or "sha256" in ast.unparse(node)
    value = _resolve(node, constants, runner_path)
    return isinstance(value, str) and bool(re.fullmatch(r"[0-9a-f]{64}", value))


class _NodeMaps:
    SUITES = ("body", "orelse", "finalbody")

    def __init__(self, tree):
        self.parent = {}
        self.lists = {}
        for node in ast.walk(tree):
            for child in ast.iter_child_nodes(node):
                self.parent.setdefault(id(child), (node, None))
            for attr in self.SUITES:
                value = getattr(node, attr, None)
                if isinstance(value, list):
                    statements = [item for item in value if isinstance(item, ast.stmt)]
                    if statements:
                        self.lists[(id(node), attr)] = statements
                    for child in value:
                        self.parent[id(child)] = (node, attr)
        self.parent[id(tree)] = None

    def chain(self, node):
        result = []
        current = node
        while True:
            entry = self.parent.get(id(current))
            if entry is None:
                return result
            owner, attr = entry
            if attr is not None:
                statements = self.lists.get((id(owner), attr), [])
                index = next((i for i, statement in enumerate(statements) if statement is current), None)
                if index is not None:
                    result.append((statements, index))
            current = owner


def _guard_entry(call):
    if not isinstance(call, ast.Call):
        return False
    func = call.func
    if isinstance(func, ast.Name):
        return func.id in GUARD_NAMES
    if isinstance(func, ast.Attribute):
        return func.attr in GUARD_NAMES
    if isinstance(func, ast.Subscript) and isinstance(func.slice, ast.Constant):
        return func.slice.value in GUARD_NAMES
    return False


def _guard_proxies(tree):
    proxies = set()
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if any(_guard_entry(item) for item in ast.walk(node) if isinstance(item, ast.Call)):
            proxies.add(node.name)
    return proxies


def _is_guard_statement(statement, proxies):
    return (isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call)
            and (_guard_entry(statement.value)
                 or isinstance(statement.value.func, ast.Name)
                 and statement.value.func.id in proxies))


def _write_mode(call, path_method=False):
    mode = call.args[0] if path_method and call.args else call.args[1] if len(call.args) > 1 else None
    for keyword in call.keywords:
        if keyword.arg == "mode":
            mode = keyword.value
    return (isinstance(mode, ast.Constant) and isinstance(mode.value, str)
            and any(flag in mode.value for flag in WRITE_FLAGS))


def _write_sites(tree, constants, runner_path, round_number):
    expected = f"reports/round-{round_number}/validation.json"
    sites = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        target = None
        kind = None
        if isinstance(func, ast.Name) and func.id == "open" and node.args and _write_mode(node):
            target, kind = node.args[0], "open(write)"
        elif isinstance(func, ast.Attribute) and func.attr == "open" and _write_mode(node, path_method=True):
            target, kind = func.value, "Path.open(write)"
        elif isinstance(func, ast.Attribute) and func.attr in ("write_text", "write_bytes"):
            target, kind = func.value, func.attr
        elif isinstance(func, ast.Attribute) and ast.unparse(func) in ("os.replace", "os.rename", "shutil.move"):
            if len(node.args) >= 2:
                target, kind = node.args[1], ast.unparse(func)
        if target is None:
            continue
        resolved = _resolve(target, constants, runner_path)
        text = str(resolved).replace("\\", "/") if resolved is not None else ""
        literal_match = any(isinstance(item, ast.Constant) and isinstance(item.value, str)
                            and expected in item.value.replace("\\", "/") for item in ast.walk(target))
        if text.endswith(expected) or text == expected or literal_match:
            sites.append({"line": node.lineno, "kind": kind, "target": ast.unparse(target),
                          "guarded": False, "guard_line": None, "node": node})
    return sorted(sites, key=lambda row: row["line"])


def _guard_dominates(site, maps, proxies):
    for statements, index in maps.chain(site["node"]):
        for previous in reversed(statements[:index]):
            if _is_guard_statement(previous, proxies):
                return previous.lineno
    return None


def _round_from_path(path):
    for part in reversed(path.parts):
        match = ROUND_PART.match(part)
        if match:
            return int(match.group(1))
    return None


def _read_receipt(root, round_number):
    if round_number is None:
        return None, None
    path = root / "reports" / f"round-{round_number}" / "validation.json"
    try:
        return path, json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return path, None


def _signature(findings, limits):
    if not isinstance(limits, list) or not limits:
        return None
    if findings is not None and (not isinstance(findings, list) or not findings):
        return None
    return json.dumps({"findings": findings, "limits": limits}, ensure_ascii=False, sort_keys=True)


def _analyze(root, path):
    root = root.resolve()
    path = path.resolve()
    try:
        relative_path = path.relative_to(root).as_posix()
    except ValueError:
        relative_path = str(path)
    number = _round_from_path(path)
    try:
        raw = path.read_bytes()
        source = raw.decode("utf-8")
    except (OSError, UnicodeDecodeError) as error:
        return {"path": relative_path, "round": number, "parse": "error",
                "error": f"{type(error).__name__}: {error}", "sha256": None,
                "defects": ["could-not-evaluate"], "checks": {}, "evidence": {},
                "_signature": None}
    digest = hashlib.sha256(raw).hexdigest()
    try:
        tree = ast.parse(source, filename=relative_path)
    except SyntaxError as error:
        return {"path": relative_path, "round": number, "parse": "error",
                "error": f"{error.msg} (line {error.lineno})", "sha256": digest,
                "defects": ["could-not-evaluate"], "checks": {}, "evidence": {},
                "_signature": None}

    constants = _constants(tree, path)
    relative_root, absolute_root, chdir_lines, root_assignments = _root_checks(tree, constants, path)
    defects = []
    if not relative_root:
        defects.append("absolute-root" if absolute_root else "root-not-relative")
    if chdir_lines:
        defects.append("chdir")

    sites = _write_sites(tree, constants, path, number)
    maps = _NodeMaps(tree)
    proxies = _guard_proxies(tree)
    for site in sites:
        site["guard_line"] = _guard_dominates(site, maps, proxies)
        site["guarded"] = site["guard_line"] is not None
    guard_ok = bool(sites) and all(site["guarded"] for site in sites)
    if not guard_ok:
        defects.append("guard-not-dominating")

    functions = {node.name: node for node in ast.walk(tree)
                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
    fields = _dict_fields(tree)
    sha_expr_ok = _sha_expression_ok(fields.get("runner_sha256"), functions, constants, path)
    receipt_path, receipt = _read_receipt(root, number)
    reported_sha = receipt.get("runner_sha256") if isinstance(receipt, dict) else None
    sha_matches = reported_sha == digest if isinstance(reported_sha, str) else None
    if isinstance(receipt, dict):
        sha_ok = sha_expr_ok and sha_matches is True
        if reported_sha is None:
            defects.append("runner-sha256-null")
        elif sha_matches is not True or not sha_expr_ok:
            defects.append("runner-sha256-mismatch")
    else:
        sha_ok = sha_expr_ok
        if not sha_expr_ok:
            defects.append("runner-sha256-null")

    if isinstance(receipt, dict):
        receipt_round = receipt.get("round")
        findings = receipt.get("named_findings")
        limits = receipt.get("limits")
    else:
        receipt_round = _static_value(fields.get("round"), constants, path)
        findings = _static_value(fields.get("named_findings"), constants, path)
        limits = _static_value(fields.get("limits"), constants, path)
    if number is not None and receipt_round is not None and receipt_round != number:
        defects.append("receipt-round-mismatch")
    signature = _signature(findings, limits)
    findings_limits_ok = signature is not None
    if not findings_limits_ok:
        defects.append("round-specific-findings-limits")

    checks = {
        "relative_root": relative_root,
        "no_chdir": not chdir_lines,
        "guard_receipt_dominates_writes": guard_ok,
        "runner_sha256_nonnull_and_current": sha_ok,
        "round_specific_findings_limits": findings_limits_ok,
        "receipt_round_matches_path": receipt_round == number if receipt_round is not None else None,
    }
    evidence = {
        "root_assignments": [{"line": line, "source": ast.unparse(value)}
                             for value, line in root_assignments],
        "chdir_lines": chdir_lines,
        "receipt_writes": [{key: value for key, value in site.items() if key != "node"}
                           for site in sites],
        "runner_sha256": {"source_expression": ast.unparse(fields["runner_sha256"])
                          if fields.get("runner_sha256") is not None else None,
                          "receipt_path": str(receipt_path) if receipt_path else None,
                          "receipt_value": reported_sha,
                          "matches_source_sha256": sha_matches},
        "findings_count": len(findings) if isinstance(findings, list) else None,
        "limits_count": len(limits) if isinstance(limits, list) else None,
    }
    return {"path": relative_path, "round": number, "parse": "ok", "sha256": digest,
            "defects": sorted(set(defects)), "checks": checks, "evidence": evidence,
            "_signature": signature}


def census(root, paths=None):
    root = root.resolve()
    if paths is None:
        paths = [root / "reports" / f"round-{number}" / "run-validation.py" for number in ROUNDS]
    rows = [_analyze(root, path) for path in paths]
    seen = {}
    for row in rows:
        signature = row.pop("_signature", None)
        if signature is None:
            continue
        if signature in seen:
            row["defects"] = sorted(set(row["defects"] + ["round-specific-findings-limits"]))
            row["checks"]["round_specific_findings_limits"] = False
            row["evidence"]["duplicate_findings_limits_of"] = seen[signature]
        else:
            seen[signature] = row["path"]
    counts = {}
    for row in rows:
        for defect in row["defects"]:
            counts[defect] = counts.get(defect, 0) + 1
    return {"tool": TOOL, "schema": "round-runner-conformance/1", "mode": "runner-census",
            "root": str(root), "runner_count": len(rows),
            "census_complete": all(row["parse"] == "ok" for row in rows),
            "conformant_count": sum(not row["defects"] and row["parse"] == "ok" for row in rows),
            "defect_counts": dict(sorted(counts.items())), "runners": rows,
            "limits": ["Static AST and adjacent validation.json inspection only; no runner is executed.",
                       "The SHA check compares the filed runner_sha256 with the runner bytes read now.",
                       "Guard dominance recognizes an unconditional earlier guard call in the enclosing suite;"
                       " unrecognized call-flow and dynamic publication mechanisms remain outside this checker.",
                       "The findings/limits check detects absent lists and exact cross-round duplicate pairs;"
                       " semantic adequacy of prose is not inferred."]}


def _fixture_source(number, *, bad=False):
    round_path = f"reports/round-{number}"
    if not bad:
        return f'''import hashlib
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
ROUND = "{round_path}"
RUNNER = f"{{ROUND}}/run-validation.py"

def guard_receipt():
    namespace = {{"guard_receipt": lambda *args, **kwargs: None}}
    namespace["guard_receipt"](f"{{ROUND}}/validation.json")

def main():
    guard_receipt()
    with open(f"{{ROUND}}/validation.json", "w", encoding="utf-8") as handle:
        handle.write("{{}}\\n")

receipt = {{"round": {number}, "runner_sha256": hashlib.sha256(open(RUNNER, "rb").read()).hexdigest(), "named_findings": ["same finding"],
           "limits": ["same limit"]}}
'''
    return f'''import os
ROOT = "/opt/old-checkout"
ROUND = "{round_path}"
os.chdir(ROOT)

def guard_receipt():
    pass

def main(enabled=False):
    if enabled:
        guard_receipt()
    with open(f"{{ROUND}}/validation.json", "w", encoding="utf-8") as handle:
        handle.write("{{}}\\n")

receipt = {{"round": {number}, "runner_sha256": None, "named_findings": ["same finding"],
           "limits": ["same limit"]}}
'''


def _write_fixture(root, number, bad=False):
    path = root / "reports" / f"round-{number}" / "run-validation.py"
    path.parent.mkdir(parents=True, exist_ok=True)
    source = _fixture_source(number, bad=bad)
    path.write_text(source, encoding="utf-8")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    receipt = {"round": number, "runner_sha256": None if bad else digest,
               "named_findings": ["same finding"], "limits": ["same limit"]}
    (path.parent / "validation.json").write_text(json.dumps(receipt), encoding="utf-8")
    return path


def selftest():
    scratch = Path(os.environ.get("TMPDIR", ROOT / ".scratch"))
    scratch.mkdir(parents=True, exist_ok=True)
    controls = []
    with tempfile.TemporaryDirectory(prefix="round-runner-conformance-", dir=scratch) as temporary:
        fixture_root = Path(temporary)
        good = _write_fixture(fixture_root, 901)
        bad = _write_fixture(fixture_root, 902, bad=True)
        report = census(fixture_root, [good, bad])
        by_path = {row["path"]: row for row in report["runners"]}
        good_row = by_path["reports/round-901/run-validation.py"]
        bad_row = by_path["reports/round-902/run-validation.py"]
        required = {"absolute-root", "chdir", "guard-not-dominating", "runner-sha256-null",
                    "round-specific-findings-limits"}
        controls.extend([
            {"control": "fixture-conformant-runner-passes", "passed": not good_row["defects"]},
            {"control": "fixture-nonconformant-defects-classified",
             "passed": required.issubset(set(bad_row["defects"]))},
            {"control": "fixture-census-complete", "passed": report["census_complete"]
             and report["runner_count"] == 2},
        ])
    passed = sum(control["passed"] for control in controls)
    return {"tool": TOOL, "mode": "selftest", "controls": controls,
            "controls_passed": passed, "controls_total": len(controls),
            "selftest_passed": passed == len(controls),
            "limits": ["Synthetic runners and receipts live only in a disposable .scratch directory.",
                       "The fixture source is parsed, never imported or executed."]}


def render_text(report):
    lines = [f"{report['tool']}  mode={report['mode']}  runners={report['runner_count']}"]
    for row in report["runners"]:
        defects = ",".join(row["defects"]) or "none"
        lines.append(f"{row['path']}: {defects}")
    lines.append("defect_counts: " + json.dumps(report["defect_counts"], sort_keys=True))
    lines.append(f"census_complete: {report['census_complete']}")
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print the census as JSON")
    parser.add_argument("--selftest", action="store_true", help="run disposable fixture controls")
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root")
    parser.add_argument("runners", nargs="*", help="runner paths to audit; default is rounds 34-40")
    args = parser.parse_args(argv)
    if args.selftest:
        if args.runners or args.root.resolve() != ROOT.resolve() or args.json:
            parser.error("--selftest takes no other options")
        result = selftest()
        sys.stdout.write(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        return 0 if result["selftest_passed"] else 1
    root = args.root.resolve()
    if not root.is_dir():
        print(f"{TOOL}: root is not a directory: {root}", file=sys.stderr)
        return 2
    paths = []
    for item in args.runners:
        path = Path(item)
        paths.append(path if path.is_absolute() else root / path)
    report = census(root, paths if paths else None)
    rendered = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    sys.stdout.write(rendered if args.json else render_text(report))
    return 0 if report["census_complete"] else 1


if __name__ == "__main__":
    sys.exit(main())
```

## Owed
- None.

## Citations
- Contract and census scope: `reports/round-41/claims.json:14-18`; assigned checker path: `reports/round-41/targets.json:48-52`.
- Baseline runner shapes: r34 absolute ROOT/chdir and guarded publication at `reports/round-34/run-validation.py:10,26,514-535`; r35 at `reports/round-35/run-validation.py:9,36,379-383,492-505`; r36 at `reports/round-36/run-validation.py:8,13,250-267`; r37 at `reports/round-37/run-validation.py:5,10,216-233`; r38 at `reports/round-38/run-validation.py:5,13,218-235`; r39 at `reports/round-39/run-validation.py:5,13,218-235`; r40 relative ROOT and guarded publication at `reports/round-40/run-validation.py:5,227-244`.
- Receipt evidence: r34 non-null `runner_sha256` `reports/round-34/validation.json:194-196`; r35 `reports/round-35/validation.json:220-222`; r36 null `reports/round-36/validation.json:164-168`; r37 null `reports/round-37/validation.json:146-149`; r38 null and findings `reports/round-38/validation.json:122-130`; r39 null and copied findings `reports/round-39/validation.json:118-126`; r40 distinct finding and non-null SHA `reports/round-40/validation.json:135-143`.
- Command output: extracted-source `--selftest` exited 0 with 3/3 controls; extracted-source `--json` exited 0 with census_complete=true, 7 runners and conformant_count=1; defect_counts were absolute-root=6, chdir=6, runner-sha256-null=4, round-specific-findings-limits=1, with r40 defect-free.
