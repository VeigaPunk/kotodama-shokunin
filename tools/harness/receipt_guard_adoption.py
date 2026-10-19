#!/usr/bin/env python3
"""Receipt-guard adoption inventory over every filed round runner (F-C13-1).

F-C13-1 (``LOG.md:3548-3567``) recorded that ``reports/round-{5,6,7}/``
``validation.json`` were rewritten in the working tree during the round-33 wave
and restored byte-exact; the mechanism was a **guard-adoption gap**: historical
runners write their own receipt in place and never call
``tools/harness/receipt_guard.py`` (round 14 onward defines the guard). This
instrument turns that prose into a re-runnable census. For every
``reports/round-*/run-validation.py`` it records, with ``path:line`` evidence:

- every in-place write whose target statically resolves to that runner's own
  receipt: ``write_text`` / ``write_bytes`` / ``open`` in a write mode /
  ``os.replace`` / ``os.rename`` / ``shutil.move`` / ``Path.replace``, plus
  receipt writes embedded inside subprocess script strings (the round-19 shape);
- whether the runner loads and calls the guard — a direct entry-point call, a
  ``module.guard_receipt(...)`` / ``namespace["guard_receipt"](...)`` call, or a
  local proxy/preflight function that calls it — and whether such a call
  dominates the receipt write in the same statement block. A ``try:`` whose
  handlers all terminate (``return`` / ``raise`` / ``break`` / ``continue``)
  counts as dominating; a flag-gated call does not;
- an adoption class (``guarded-refresh`` / ``unguarded-in-place`` /
  ``guard-referenced-only`` / ``no-receipt-write`` / ``could-not-evaluate``)
  and the F-C13-1 routing protocol that class implies.

The census is static analysis only: this tool never executes a runner, never
writes into a filed round, and pins each row with the runner's ``sha256`` at
read time. Unknowns are ``could-not-evaluate`` rows with a named reason — the
tool has no green path for a mechanism it cannot resolve.

Exit status: 0 when the census is complete (every runner parsed, no
``could-not-evaluate`` row); 1 when a row is a gap (still printed in full);
2 on usage or IO error. A hazard row does not change the exit status: the
hazards are the census's findings, not its failure.

CLI: receipt_guard_adoption.py [--json] [--out PATH] [--root DIR]
    receipt_guard_adoption.py --sweep-repo [--json]
    receipt_guard_adoption.py --selftest
"""

from __future__ import annotations

import argparse
import ast
import datetime as dt
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

TOOL = "tools/harness/receipt_guard_adoption.py"
SCHEMA = "receipt-guard-adoption/1"
ROOT = Path(__file__).resolve().parents[2]
GUARD_TOOL = "tools/harness/receipt_guard.py"
RUNNER_GLOB = "reports/round-*/run-validation.py"
RUNNER_RE = re.compile(r"^reports/round-(?P<round>\d+)/run-validation\.py$")
SWEEP_ROOTS = ("reports", "tools")
SKIP_DIRS = {".git", ".scratch", "__pycache__", ".mypy_cache", ".pytest_cache"}
GUARD_ENTRIES = ("guard_receipt", "round_runner_main")
RECEIPT_NAME = "validation.json"
WRITE_METHODS = ("write_text", "write_bytes")
OPEN_METHODS = ("open",)
MOVE_DOTTED = ("os.replace", "os.rename", "shutil.move")
WRITE_MODES = ("w", "a", "x", "+")
RESOLVE_ATTRS = ("resolve", "absolute", "expanduser")
# F-C13-1's declared hazards, transcribed from LOG.md:3556-3560. The census
# records agreement per row and never edits this baseline.
DECLARED_HAZARDS = (
    ("reports/round-5/run-validation.py", "LOG.md:3556-3558", ":194"),
    ("reports/round-6/run-validation.py", "LOG.md:3556-3558", ":336"),
    ("reports/round-7/run-validation.py", "LOG.md:3556-3558", ":1171"),
    ("reports/round-26/run-validation.py", "LOG.md:3559-3560", ":90, :1909"),
)
CLASS_PROTOCOL = {
    "guarded-refresh": (
        "guard-adopted: in-tree re-run is refused by the guard once the receipt "
        "is committed (REFRESH_RECEIPTS=1 is the only override); refresh runs "
        "belong in an isolated clone under the lane's .scratch"),
    "unguarded-in-place": (
        "isolated-copy-only: never execute in-tree; work from a git archive or "
        "clone under .scratch (F-C13-1 prevention)"),
    "guard-referenced-only": (
        "isolated-copy-only: the guard is referenced but no call guards its own "
        "receipt write; never execute in-tree"),
    "no-receipt-write": (
        "no in-place write to the runner's own receipt was found; other writes "
        "remain possible — read the row's write evidence before running it"),
    "could-not-evaluate": (
        "manual review required: the census could not resolve this runner's "
        "receipt write or guard status; no protocol is inferred"),
}
CONTROL_LIVE = (
    ("reports/round-5/run-validation.py", "unguarded-in-place", 194),
    ("reports/round-6/run-validation.py", "unguarded-in-place", 336),
    ("reports/round-7/run-validation.py", "unguarded-in-place", 1171),
    ("reports/round-8/run-validation.py", "unguarded-in-place", 1486),
    ("reports/round-9/run-validation.py", "unguarded-in-place", 1910),
    ("reports/round-10/run-validation.py", "unguarded-in-place", 1054),
    ("reports/round-11/run-validation.py", "unguarded-in-place", 1740),
    ("reports/round-12/run-validation.py", "unguarded-in-place", 1071),
    ("reports/round-19/run-validation.py", "unguarded-in-place", 21),
    ("reports/round-21/run-validation.py", "unguarded-in-place", 1115),
    ("reports/round-29/run-validation.py", "unguarded-in-place", 922),
    ("reports/round-32/run-validation.py", "guarded-refresh", 1143),
    ("reports/round-33/run-validation.py", "guarded-refresh", 1471),
)
RECEIPT_PATH_RE = re.compile(r"[A-Za-z0-9_./-]*validation\.json")
EMBEDDED_WRITE_RE = re.compile(r"\.write_text\(|\.write_bytes\(|\bopen\(|json\.dump\(")
UNRESOLVED_HINTS = ("validation", "receipt", "output")


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 16), b""):
            digest.update(block)
    return digest.hexdigest()


def _clip(text, limit=160):
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


# --------------------------------------------------------------- resolution


def _strip_slashes(value):
    while "//" in value:
        value = value.replace("//", "/")
    return value.strip("/") if value not in ("", "/") else ""


class Resolver:
    """Static, best-effort resolution of path-ish expressions to repo-relative text.

    ``resolved`` is ``None`` whenever the expression cannot be resolved; callers
    must treat that as unknown, never as a negative match.
    """

    def __init__(self, runner_rel):
        self.runner_rel = runner_rel
        self.runner_dir = str(Path(runner_rel).parent).replace(os.sep, "/")
        self.consts = {}

    def collect(self, tree, depth=6):
        for node in self._assigns(tree):
            if isinstance(node, ast.Assign):
                targets = [t.id for t in node.targets if isinstance(t, ast.Name)]
                value_node = node.value
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                targets = [node.target.id]
                value_node = node.value
            else:
                continue
            if value_node is None:
                continue
            value, _kind = self.resolve(value_node, depth=depth - 1)
            for name in targets:
                self.consts[name] = (ast.unparse(value_node), value)

    @staticmethod
    def _assigns(tree):
        found = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
                found.append(node)
        return sorted(found, key=lambda n: (n.lineno, n.col_offset))

    def resolve(self, node, depth=6):
        if node is None or depth < 0:
            return None, "unresolved"
        if isinstance(node, ast.Constant):
            if isinstance(node.value, str):
                return _strip_slashes(node.value), "literal"
            return None, "unresolved"
        if isinstance(node, ast.JoinedStr):
            parts = []
            for piece in node.values:
                if isinstance(piece, ast.Constant) and isinstance(piece.value, str):
                    parts.append(piece.value)
                    continue
                if isinstance(piece, ast.FormattedValue):
                    value, kind = self.resolve(piece.value, depth=depth - 1)
                    if value is None or kind == "unresolved":
                        return None, "unresolved"
                    parts.append(value)
                    continue
                return None, "unresolved"
            return _strip_slashes("".join(parts)), "fstring"
        if isinstance(node, ast.BinOp):
            left, left_kind = self.resolve(node.left, depth=depth - 1)
            right, right_kind = self.resolve(node.right, depth=depth - 1)
            if isinstance(node.op, ast.Add):
                if left is None or right is None:
                    return None, "unresolved"
                return _strip_slashes(left + right), "concat"
            if isinstance(node.op, ast.Div):
                if left is None or right is None:
                    return None, "unresolved"
                return _strip_slashes(f"{left}/{right}"), "join"
            return None, "unresolved"
        if isinstance(node, ast.Name):
            if node.id == "__file__":
                return self.runner_rel, "runner-file"
            if node.id in ("ROOT", "REPO_ROOT", "ROOT_DIR"):
                return "", "root-name"
            entry = self.consts.get(node.id)
            if entry is None:
                return None, "unresolved"
            return entry[1], "const"
        if isinstance(node, ast.Attribute):
            return self._attribute(node, depth)
        if isinstance(node, ast.Call):
            return self._call(node, depth)
        return None, "unresolved"

    def _attribute(self, node, depth):
        if node.attr == "parent" or node.attr == "parents":
            base, kind = self.resolve(node.value, depth=depth - 1)
            if base is None:
                return None, "unresolved"
            if node.attr == "parent":
                return self._drop(base, 1), f"{kind}.parent"
            return None, "unresolved"
        if node.attr in RESOLVE_ATTRS:
            return self.resolve(node.value, depth)
        return None, "unresolved"

    def _call(self, node, depth):
        func = node.func
        if isinstance(func, ast.Attribute) and func.attr in RESOLVE_ATTRS:
            return self.resolve(func.value, depth)
        if isinstance(func, ast.Attribute) and func.attr == "parents":
            return None, "unresolved"
        if isinstance(func, ast.Attribute) and func.attr == "Path" and node.args:
            return self.resolve(node.args[0], depth=depth - 1)
        if isinstance(func, ast.Attribute) and func.attr == "join":
            parts = [self.resolve(arg, depth=depth - 1)[0] for arg in node.args]
            if any(part is None for part in parts):
                return None, "unresolved"
            return _strip_slashes("/".join(parts)), "os.path.join"
        if isinstance(func, ast.Subscript):
            # Path(...).parents[N]
            base, kind = self.resolve(func.value, depth=depth - 1)
            index = func.slice
            if base is not None and isinstance(index, ast.Constant) and isinstance(index.value, int):
                return self._drop(base, index.value + 1), "parents[index]"
            return None, "unresolved"
        if isinstance(func, ast.Name):
            if func.id == "Path":
                if not node.args:
                    return None, "unresolved"
                return self.resolve(node.args[0], depth=depth - 1)
            if func.id in ("str", "repr"):
                if not node.args:
                    return None, "unresolved"
                return self.resolve(node.args[0], depth=depth - 1)
            if func.id == "getattr" and len(node.args) >= 2:
                return None, "unresolved"
            if node.args:
                inner, kind = self.resolve(node.args[0], depth=depth - 1)
                if inner is not None:
                    return inner, f"wrapper:{func.id}"
            return None, "unresolved"
        return None, "unresolved"

    @staticmethod
    def _drop(value, count):
        parts = [part for part in _strip_slashes(value).split("/") if part]
        if count >= len(parts):
            return ""
        return "/".join(parts[: len(parts) - count])


# ----------------------------------------------------------------- evidence


class NodeMaps:
    """Parent links and statement-list membership for dominance walking."""

    LIST_ATTRS = ("body", "orelse", "finalbody", "handlers")

    def __init__(self, tree):
        self.parent = {}
        self.lists = {}
        for node in ast.walk(tree):
            for child in ast.iter_child_nodes(node):
                self.parent.setdefault(id(child), (node, None))
            for attr in self.LIST_ATTRS:
                value = getattr(node, attr, None)
                if isinstance(value, list):
                    statements = [child for child in value if isinstance(child, ast.stmt)]
                    if statements:
                        self.lists[(id(node), attr)] = statements
                    for child in value:
                        self.parent[id(child)] = (node, attr)
        self.parent[id(tree)] = None

    def chain(self, node):
        """Statement lists from the node's innermost list outward, with index."""
        chain = []
        current = node
        while True:
            entry = self.parent.get(id(current))
            if entry is None:
                break
            owner, attr = entry
            if attr is not None:
                statements = self.lists.get((id(owner), attr), [])
                index = next((i for i, s in enumerate(statements) if s is current), None)
                if index is not None:
                    chain.append((statements, index))
            current = owner
        return chain


def _dotted(node):
    try:
        return ast.unparse(node)
    except Exception:  # pragma: no cover - ast.unparse is total in practice
        return "?"


def _guard_entry(func):
    """Recognize the guard's callable shapes: name, ``module.x``, ``ns["x"]``."""
    if isinstance(func, ast.Name) and func.id in GUARD_ENTRIES:
        return f"call:{func.id}", func.id
    if isinstance(func, ast.Attribute) and func.attr in GUARD_ENTRIES:
        return f"call:{_dotted(func)}", func.attr
    if isinstance(func, ast.Subscript) and isinstance(func.slice, ast.Constant):
        if isinstance(func.slice.value, str) and func.slice.value in GUARD_ENTRIES:
            return f"subscript:{_dotted(func)}", func.slice.value
    return None


def _is_guard_call(node, proxies, consts, depth=2):
    if not isinstance(node, ast.Call):
        return None
    entry = _guard_entry(node.func)
    if entry:
        return entry
    func = node.func
    if isinstance(func, ast.Name):
        definition = proxies.get(func.id)
        if definition is not None and _function_calls_guard(definition, proxies, depth - 1):
            return f"proxy:{func.id}", func.id
    return None


def _function_calls_guard(definition, proxies, depth=2):
    if depth < 0:
        return False
    for node in ast.walk(definition):
        if isinstance(node, ast.Call) and _guard_entry(node.func):
            return True
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            nested = proxies.get(node.func.id)
            if nested is not None and nested is not definition and _function_calls_guard(nested, proxies, depth - 1):
                return True
    return False


def _terminates(statements):
    for statement in reversed(statements):
        if isinstance(statement, (ast.Return, ast.Raise, ast.Break, ast.Continue)):
            return True
        if isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call):
            if isinstance(statement.value.func, ast.Name) and statement.value.func.id == "exit":
                return True
        return False
    return False


def _try_provider(statement, proxies, consts):
    """A ``try:`` whose body is guard calls and whose handlers all terminate."""
    if not isinstance(statement, ast.Try) or not statement.body:
        return None
    providers = [_is_guard_call(s.value, proxies, consts) for s in statement.body
                 if isinstance(s, ast.Expr)]
    if len(providers) != len(statement.body) or not all(providers):
        return None
    for handler in statement.handlers:
        if not handler.body or not _terminates(handler.body):
            return None
    return {"line": statement.lineno, "kind": "try-guard",
            "entries": [entry[1] for entry in providers],
            "call_lines": [s.lineno for s in statement.body]}


def _statement_provider(statement, proxies, consts):
    if isinstance(statement, ast.Expr):
        found = _is_guard_call(statement.value, proxies, consts)
        if found:
            return {"line": statement.lineno, "kind": found[0], "entries": [found[1]]}
        return None
    return _try_provider(statement, proxies, consts)


def _conditional_guard_calls(node, proxies, consts, found, depth=0):
    """Guard calls nested inside non-dominating statement kinds (flag gates)."""
    if depth > 3:
        return
    for attr in ("body", "orelse", "finalbody"):
        for child in getattr(node, attr, None) or []:
            if isinstance(child, ast.Expr):
                entry = _is_guard_call(child.value, proxies, consts)
                if entry:
                    found.append({"line": child.lineno, "kind": entry[0]})
            if isinstance(child, ast.If):
                _conditional_guard_calls(child, proxies, consts, found, depth + 1)


def _dominating_provider(chain, proxies, consts, conditional):
    for body, index in chain:
        for statement in reversed(body[:index]):
            provider = _statement_provider(statement, proxies, consts)
            if provider:
                return provider
            _conditional_guard_calls(statement, proxies, consts, conditional)
    return None


def write_sites(tree, resolver, runner_rel, own_receipt):
    """AST write sites whose destination resolves to the runner's own receipt."""
    sites = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        kind = None
        target = None
        if isinstance(func, ast.Attribute) and func.attr in WRITE_METHODS:
            kind, target = func.attr, func.value
        elif isinstance(func, ast.Attribute) and func.attr in OPEN_METHODS:
            mode = node.args[1] if len(node.args) > 1 else None
            for keyword in node.keywords:
                if keyword.arg == "mode":
                    mode = keyword.value
            if isinstance(mode, ast.Constant) and isinstance(mode.value, str):
                if any(flag in mode.value for flag in WRITE_MODES):
                    kind, target = "open(write)", func.value
        elif isinstance(func, ast.Name) and func.id in OPEN_METHODS:
            mode = node.args[1] if len(node.args) > 1 else None
            for keyword in node.keywords:
                if keyword.arg == "mode":
                    mode = keyword.value
            if isinstance(mode, ast.Constant) and isinstance(mode.value, str) \
                    and any(flag in mode.value for flag in WRITE_MODES):
                kind, target = "open(write)", node.args[0] if node.args else None
        elif isinstance(func, ast.Attribute) and _dotted(func) in MOVE_DOTTED:
            if len(node.args) >= 2:
                kind, target = _dotted(func), node.args[1]
        elif isinstance(func, ast.Attribute) and func.attr == "replace" and node.args:
            receiver, _kind = resolver.resolve(func.value)
            if receiver is not None:
                kind, target = "Path.replace", node.args[0]
        if kind is None or target is None:
            continue
        resolved, how = resolver.resolve(target)
        if resolved != own_receipt:
            continue
        sites.append({"line": node.lineno, "kind": kind,
                      "target": _clip(ast.unparse(target)),
                      "resolved": resolved, "resolution": how,
                      "src": _clip(ast.unparse(node)), "_node": node})
    return sorted(sites, key=lambda row: row["line"])


def embedded_write_sites(tree, own_receipt, runner_rel):
    """Receipt writes hidden inside string literals (subprocess script shape).

    A literal that parses as Python is analyzed with the same write-site rule,
    so a read (``open(PATH)`` / ``read_text``) inside a script is not a site;
    the reported line is the file line of the embedded statement.
    """
    sites, opaque = [], []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Constant) or not isinstance(node.value, str):
            continue
        text = node.value
        if RECEIPT_NAME not in text:
            continue
        try:
            inner = ast.parse(text)
        except SyntaxError:
            if EMBEDDED_WRITE_RE.search(text) and RECEIPT_PATH_RE.search(text):
                opaque.append({"literal_line": node.lineno,
                               "reason": "literal mentions a write verb and "
                                         "validation.json but does not parse as Python"})
            continue
        resolver = Resolver(runner_rel)
        resolver.collect(inner)
        for site in write_sites(inner, resolver, runner_rel, own_receipt):
            site.pop("_node", None)
            site["kind"] = "embedded:" + site["kind"]
            site["literal_line"] = node.lineno
            site["line"] = node.lineno + site["line"] - 1
            site["resolution"] = "embedded-script"
            sites.append(site)
    seen = set()
    unique = []
    for site in sorted(sites, key=lambda row: row["line"]):
        key = (site["line"], site["kind"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(site)
    return unique, opaque


def guard_evidence(tree, resolver):
    loads, calls, refresh = [], [], []
    proxies = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if "receipt_guard" in node.value and RECEIPT_NAME not in node.value:
                loads.append({"line": node.lineno, "form": "guard-path-string",
                              "detail": _clip(node.value)})
            if node.value == "REFRESH_RECEIPTS":
                refresh.append({"line": node.lineno, "form": "refresh-env-string"})
        if isinstance(node, ast.Name) and node.id == "REFRESH_RECEIPTS":
            refresh.append({"line": node.lineno, "form": "refresh-env-name"})
        if isinstance(node, ast.Import):
            for alias in node.names:
                if "receipt_guard" in alias.name:
                    loads.append({"line": node.lineno, "form": "import",
                                  "detail": alias.name})
        if isinstance(node, ast.ImportFrom) and node.module and "receipt_guard" in node.module:
            loads.append({"line": node.lineno, "form": "from-import",
                          "detail": f"{node.module}:{','.join(a.name for a in node.names)}"})
        if isinstance(node, ast.Call):
            entry = _guard_entry(node.func)
            if entry:
                receipt_arg = None
                if node.args:
                    receipt_arg, _how = resolver.resolve(node.args[0])
                calls.append({"line": node.lineno, "form": entry[0],
                              "detail": _clip(ast.unparse(node)),
                              "receipt_arg": receipt_arg})
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            proxies[node.name] = node
    proxy_rows = []
    for name, definition in sorted(proxies.items()):
        guard_lines = [child.lineno for child in ast.walk(definition)
                       if isinstance(child, ast.Call) and _guard_entry(child.func)]
        if guard_lines:
            proxy_rows.append({"name": name, "line": definition.lineno,
                               "guard_call_lines": sorted(guard_lines)})
    loads.sort(key=lambda row: (row["line"], row["form"]))
    calls.sort(key=lambda row: row["line"])
    refresh = sorted({(row["line"], row["form"]): row for row in refresh}.values(),
                     key=lambda row: row["line"])
    return {"loads": loads, "calls": calls, "refresh_references": refresh,
            "proxy_defs": proxy_rows}


def analyze(rel, text):
    row = {"runner": rel, "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
           "lines": text.count("\n") + 1}
    match = RUNNER_RE.match(rel)
    round_number = int(match.group("round")) if match else None
    row["round"] = round_number
    own_receipt = f"reports/round-{round_number}/{RECEIPT_NAME}" if round_number else None
    row["receipt"] = own_receipt
    try:
        tree = ast.parse(text)
    except SyntaxError as error:
        row.update({"parse": "error", "parse_error": f"{error.msg} (line {error.lineno})",
                    "class": "could-not-evaluate", "hazard": None,
                    "route": CLASS_PROTOCOL["could-not-evaluate"],
                    "receipt_writes": [], "embedded_receipt_writes": [],
                    "guard": {"loads": [], "calls": [], "refresh_references": [], "proxy_defs": []},
                    "reasons": [f"could-not-evaluate: unparsable source "
                                f"({error.msg} at line {error.lineno})"]})
        return row
    row["parse"] = "ok"
    resolver = Resolver(rel)
    resolver.collect(tree)
    guard = guard_evidence(tree, resolver)
    sites = write_sites(tree, resolver, rel, own_receipt)
    embedded, embedded_opaque = embedded_write_sites(tree, own_receipt, rel)
    maps = NodeMaps(tree)
    proxies = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            proxies[node.name] = node
    conditional = []
    for site in sites:
        node = site.pop("_node", None)
        provider = None
        if node is not None:
            provider = _dominating_provider(maps.chain(node), proxies, resolver, conditional)
        site["guarded"] = provider is not None
        site["guard_provider"] = provider
    for site in embedded:
        site["guarded"] = False
        site["guard_provider"] = None
        site["note"] = ("receipt write embedded in a subprocess script string; "
                        "no in-file guard call can dominate it")
    # Writes whose destination text smells like the receipt but does not resolve.
    unresolved = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        target = None
        if isinstance(func, ast.Attribute) and func.attr in WRITE_METHODS:
            target = func.value
        elif isinstance(func, ast.Name) and func.id == "open" and node.args:
            target = node.args[0]
        if target is None:
            continue
        resolved, _how = resolver.resolve(target)
        if resolved is not None:
            continue
        text_target = _dotted(target).lower()
        if any(hint in text_target for hint in UNRESOLVED_HINTS):
            unresolved.append({"line": node.lineno, "target": _clip(_dotted(target))})
    row["receipt_writes"] = sites
    row["embedded_receipt_writes"] = embedded
    row["embedded_unparsed_literals"] = embedded_opaque
    row["guard"] = guard
    row["unresolved_write_targets"] = unresolved
    write_count = len(sites) + len(embedded)
    reasons = []
    if not write_count:
        if unresolved:
            row["class"] = "could-not-evaluate"
            row["hazard"] = None
            reasons.append("could-not-evaluate: write targets referencing "
                           "receipt/output-like names do not resolve: "
                           + ", ".join(f":{item['line']}" for item in unresolved))
        else:
            row["class"] = "no-receipt-write"
            row["hazard"] = False
            reasons.append("no in-place write to the runner's own receipt "
                           f"({own_receipt}) was found")
    elif all(site["guarded"] for site in sites) and not embedded:
        row["class"] = "guarded-refresh"
        row["hazard"] = False
        reasons.append("every resolved receipt write is dominated by a guard call "
                       f"({', '.join(':' + str(site['guard_provider']['line']) for site in sites)})")
        if guard["calls"]:
            reasons.append("guard entry calls at "
                           + ", ".join(':' + str(call["line"]) for call in guard["calls"]))
    else:
        if not guard["calls"] and guard["loads"]:
            row["class"] = "guard-referenced-only"
            row["hazard"] = True
            reasons.append("guard loaded/referenced but never called in this file")
        else:
            row["class"] = "unguarded-in-place"
            row["hazard"] = True
        if embedded:
            reasons.append("receipt write embedded in a script string: "
                           + ", ".join(':' + str(site["line"]) for site in embedded))
        if not guard["calls"] and not guard["loads"] and not guard["refresh_references"]:
            reasons.append("no guard reference of any kind in this file")
        elif not guard["calls"] and guard["loads"]:
            reasons.append("guard loaded but no guard entry call found")
        elif not guard["calls"]:
            reasons.append("only REFRESH_RECEIPTS references, which gate other "
                           "runners' refresh runs, not this runner's own write")
        else:
            unguarded = [site for site in sites if not site["guarded"]]
            reasons.append("guard call exists but does not dominate the write: "
                           + ", ".join(':' + str(site["line"]) for site in unguarded or sites))
        if conditional:
            reasons.append("flag-gated guard calls (do not dominate): "
                           + ", ".join(':' + str(item["line"]) for item in conditional))
    if row["hazard"] is True and unresolved:
        reasons.append("unresolved receipt-like write targets are also present: "
                       + ", ".join(f":{item['line']}" for item in unresolved))
    row["route"] = CLASS_PROTOCOL[row["class"]]
    row["reasons"] = reasons
    return row


# ------------------------------------------------------------------- census


def runner_paths(root):
    return sorted(
        (path for path in root.glob(RUNNER_GLOB) if RUNNER_RE.match(
            path.relative_to(root).as_posix())),
        key=lambda path: int(RUNNER_RE.match(path.relative_to(root).as_posix()).group("round")))


def census(root):
    rows = []
    for path in runner_paths(root):
        rel = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            rows.append({"runner": rel, "round": int(RUNNER_RE.match(rel).group("round")),
                         "parse": "error", "parse_error": f"{type(error).__name__}: {error}",
                         "class": "could-not-evaluate", "hazard": None,
                         "route": CLASS_PROTOCOL["could-not-evaluate"],
                         "receipt_writes": [], "embedded_receipt_writes": [],
                         "guard": {"loads": [], "calls": [], "refresh_references": [],
                                   "proxy_defs": []},
                         "reasons": [f"could-not-evaluate: unreadable ({error})"]})
            continue
        rows.append(analyze(rel, text))
    by_path = {row["runner"]: row for row in rows}
    class_counts = {}
    for row in rows:
        class_counts[row["class"]] = class_counts.get(row["class"], 0) + 1
    declared_rows = []
    for path, source, declared_lines in DECLARED_HAZARDS:
        row = by_path.get(path)
        observed = row["class"] if row else None
        declared_rows.append({
            "runner": path, "declared_by": source, "declared_lines": declared_lines,
            "declared_class": "unguarded-in-place",
            "observed_class": observed,
            "agrees": observed == "unguarded-in-place",
            "evidence": [] if row is None else (
                [f"{path}:{site['line']}" for site in row["receipt_writes"]]
                + [f"{path}:{call['line']} (guard call)"
                   for call in row["guard"]["calls"]])})
    findings = []
    for declared in declared_rows:
        if not declared["agrees"]:
            findings.append({
                "id": f"RGA-1-{Path(declared['runner']).parts[1]}",
                "kind": "declared-hazard-mismatch",
                "runner": declared["runner"],
                "detail": (f"F-C13-1 ({declared['declared_by']}) names "
                           f"{declared['declared_lines']} as carrying the same "
                           f"unguarded in-place hazard; the live bytes classify as "
                           f"{declared['observed_class']}"),
                "evidence": declared["evidence"],
                "owner": "integrator (round 34) — filed LOG.md bytes are not edited; "
                         "this row is the new-record correction"})
    undeclared = [row["runner"] for row in rows
                  if row["hazard"] is True
                  and row["runner"] not in {item[0] for item in DECLARED_HAZARDS}]
    if undeclared:
        findings.append({
            "id": "RGA-2",
            "kind": "undeclared-unguarded-writer",
            "runner": None,
            "detail": (f"{len(undeclared)} runner(s) write their own receipt without "
                       "a dominating guard call and are not in the F-C13-1 declared set"),
            "evidence": undeclared,
            "owner": "integrator (round 34) — routing row per runner below"})
    gaps = [row["runner"] for row in rows if row["class"] == "could-not-evaluate"]
    guard_path = root / GUARD_TOOL
    report = {
        "tool": TOOL,
        "schema": SCHEMA,
        "mode": "runner-census",
        "root": str(root),
        "date": dt.date.today().isoformat(),
        "glob": RUNNER_GLOB,
        "runner_count": len(rows),
        "class_counts": dict(sorted(class_counts.items())),
        "hazard_count": sum(1 for row in rows if row["hazard"] is True),
        "census_complete": not gaps,
        "gaps": gaps,
        "guard_tool": {
            "path": GUARD_TOOL,
            "sha256": sha256_file(guard_path) if guard_path.is_file() else None,
            "present": guard_path.is_file()},
        "declared_hazards": declared_rows,
        "findings": findings,
        "protocols": CLASS_PROTOCOL,
        "runners": rows,
        "limits": [
            "Static AST/text analysis at read time, not execution: a runner's "
            "runtime behaviour, aliasing beyond the resolved constant map, or a "
            "write performed by a helper it calls can differ from this census, "
            "which is why could-not-evaluate rows are never greened.",
            "Recognized write idioms are write_text/write_bytes, open() in a "
            "write mode, os.replace/os.rename/shutil.move, Path.replace with a "
            "resolvable receiver, and receipt writes embedded in string "
            "literals; other publication idioms are recorded only when their "
            "destination resolves.",
            "Row digests pin the bytes read during this census, not HEAD at "
            "commit time; re-run after any landing that touches a runner.",
            "This tool executes no round runner and writes no filed receipt; "
            "--out refuses absolute paths, path escapes, and validation.json "
            "destinations.",
        ],
    }
    return report


def sweep_repo(root):
    rows = []
    scanned = 0
    for base in SWEEP_ROOTS:
        for path in sorted((root / base).rglob("*.py")):
            rel = path.relative_to(root).as_posix()
            if any(part in SKIP_DIRS for part in Path(rel).parts):
                continue
            scanned += 1
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError) as error:
                rows.append({"path": rel, "parse": "error",
                             "parse_error": f"{type(error).__name__}: {error}",
                             "kind": "runner" if RUNNER_RE.match(rel) else "non-runner",
                             "receipt_writes": []})
                continue
            resolver = Resolver(rel)
            try:
                tree = ast.parse(text)
            except SyntaxError as error:
                rows.append({"path": rel, "parse": "error",
                             "parse_error": f"{error.msg} (line {error.lineno})",
                             "kind": "runner" if RUNNER_RE.match(rel) else "non-runner",
                             "receipt_writes": []})
                continue
            resolver.collect(tree)
            writes = []
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                func = node.func
                target = None
                kind = None
                if isinstance(func, ast.Attribute) and func.attr in WRITE_METHODS:
                    kind, target = func.attr, func.value
                elif isinstance(func, ast.Attribute) and _dotted(func) in MOVE_DOTTED:
                    if len(node.args) >= 2:
                        kind, target = _dotted(func), node.args[1]
                if target is None:
                    continue
                resolved, _how = resolver.resolve(target)
                if resolved and re.match(r"^reports/round-\d+/validation\.json$", resolved):
                    writes.append({"line": node.lineno, "kind": kind,
                                   "target": _clip(ast.unparse(target)),
                                   "resolved": resolved,
                                   "src": _clip(ast.unparse(node))})
            if writes:
                rows.append({"path": rel, "parse": "ok",
                             "kind": "runner" if RUNNER_RE.match(rel) else "non-runner",
                             "receipt_writes": sorted(writes, key=lambda row: row["line"])})
    complete = not any(row["parse"] == "error" for row in rows)
    return {"tool": TOOL, "schema": SCHEMA, "mode": "repo-sweep",
            "root": str(root), "date": dt.date.today().isoformat(),
            "files_scanned": scanned,
            "writers": [row for row in rows if row["receipt_writes"]],
            "parse_gaps": [row for row in rows if row["parse"] == "error"],
            "sweep_complete": complete,
            "limits": [
                "Same static discipline as the runner census for AST-visible "
                "writes; unlike the census, the sweep does not re-parse embedded "
                "script strings, so a receipt write hidden inside a string "
                "literal in a non-runner file would not appear here.",
                "The writers list includes runners (see the census for adoption "
                "classes) and any non-runner row is listed with kind=non-runner.",
            ]}


# ------------------------------------------------------------------ selftest

FIXTURES = {
    "reports/round-41/run-validation.py": '''\
import runpy
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-41"
OUTPUT = f"{ROUND_DIR}/validation.json"


def guard_receipt():
    namespace = runpy.run_path(str(ROOT / "tools/harness/receipt_guard.py"))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def safe_path(relative):
    return ROOT / relative


def main(check=False):
    rendered = "{}\\n"
    if check:
        print(rendered, end="")
    else:
        guard_receipt()
        safe_path(OUTPUT).write_text(rendered, encoding="utf-8")
    return 0
''',
    "reports/round-42/run-validation.py": '''\
import importlib.util
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
GUARD = "tools/harness/receipt_guard.py"
OUTPUT = "reports/round-42/validation.json"


def guard_preflight():
    spec = importlib.util.spec_from_file_location("fixture_guard", ROOT / GUARD)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.guard_receipt(ROOT / OUTPUT, repo_root=ROOT)


def main(check=False):
    if check:
        print("{}")
    else:
        guard_preflight()
        (ROOT / OUTPUT).write_text("{}\\n", encoding="utf-8")
    return 0
''',
    "reports/round-43/run-validation.py": '''\
import runpy
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "reports/round-43/validation.json"


def guard_receipt():
    namespace = runpy.run_path(str(ROOT / "tools/harness/receipt_guard.py"))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def safe_path(relative):
    return ROOT / relative


def main(check=False):
    if check:
        print("{}")
    else:
        try:
            guard_receipt()
        except SystemExit as error:
            return error.code if isinstance(error.code, int) else 3
        safe_path(OUTPUT).write_text("{}\\n", encoding="utf-8")
    return 0
''',
    "reports/round-44/run-validation.py": '''\
from pathlib import Path
HERE = Path(__file__).resolve().parent


def main():
    (HERE / "validation.json").write_text("{}\\n", encoding="utf-8")
    return 0
''',
    "reports/round-45/run-validation.py": '''\
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.harness.receipt_guard import guard_receipt  # noqa: F401  (imported, never called)
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "reports/round-45/validation.json"


def main():
    (ROOT / OUTPUT).write_text("{}\\n", encoding="utf-8")
    return 0
''',
    "reports/round-46/run-validation.py": '''\
import runpy
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "reports/round-46/validation.json"


def guard_receipt():
    namespace = runpy.run_path(str(ROOT / "tools/harness/receipt_guard.py"))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def main(audit=False):
    if audit:
        guard_receipt()
    (ROOT / OUTPUT).write_text("{}\\n", encoding="utf-8")
    return 0
''',
    "reports/round-47/run-validation.py": '''\
import os
import runpy
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "reports/round-47/validation.json"


def guard_receipt():
    namespace = runpy.run_path(str(ROOT / "tools/harness/receipt_guard.py"))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def main():
    guard_receipt()
    temporary = ROOT / ".scratch/fixture-47.json"
    temporary.write_text("{}\\n", encoding="utf-8")
    os.replace(temporary, ROOT / OUTPUT)
    return 0
''',
    "reports/round-48/run-validation.py": '''\
import os
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "reports/round-48/validation.json"


def main():
    temporary = ROOT / ".scratch/fixture-48.json"
    temporary.write_text("{}\\n", encoding="utf-8")
    os.replace(temporary, ROOT / OUTPUT)
    return 0
''',
    "reports/round-49/run-validation.py": '''\
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]


def main():
    (ROOT / ".scratch/fixture-49.json").write_text("{}\\n", encoding="utf-8")
    (ROOT / "reports/round-41/validation.json").write_text("{}\\n", encoding="utf-8")
    return 0
''',
    "reports/round-50/run-validation.py": "def main(:\n    pass\n",
    "reports/round-51/run-validation.py": '''\
import subprocess
import sys
result = subprocess.run([sys.executable, "-c", """
import json, pathlib
v = json.load(open('reports/round-51/validation.json'))
pathlib.Path('reports/round-51/validation.json').write_text(json.dumps(v, indent=1))
print('acceptance:', True)
"""], capture_output=True, text=True)
print(result.stdout.strip())
''',
    "tools/fixture-helper.py": '''\
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]


def main():
    (ROOT / "reports/round-41/validation.json").write_text("{}\\n", encoding="utf-8")
''',
}

FIXTURE_RUNNERS = tuple(rel for rel in FIXTURES if RUNNER_RE.match(rel))

FIXTURE_EXPECTED = {
    "reports/round-41/run-validation.py": "guarded-refresh",
    "reports/round-42/run-validation.py": "guarded-refresh",
    "reports/round-43/run-validation.py": "guarded-refresh",
    "reports/round-44/run-validation.py": "unguarded-in-place",
    "reports/round-45/run-validation.py": "guard-referenced-only",
    "reports/round-46/run-validation.py": "unguarded-in-place",
    "reports/round-47/run-validation.py": "guarded-refresh",
    "reports/round-48/run-validation.py": "unguarded-in-place",
    "reports/round-49/run-validation.py": "no-receipt-write",
    "reports/round-50/run-validation.py": "could-not-evaluate",
    "reports/round-51/run-validation.py": "unguarded-in-place",
}


def _fixture_control(rows, rel, expected_class, controls, note=""):
    row = rows.get(rel)
    passed = row is not None and row["class"] == expected_class
    if expected_class == "guarded-refresh":
        passed = passed and row.get("hazard") is False
    if expected_class in ("unguarded-in-place", "guard-referenced-only"):
        passed = passed and row.get("hazard") is True
    if expected_class == "no-receipt-write":
        passed = passed and row.get("hazard") is False
    controls.append({"control": f"fixture-{Path(rel).parts[1]}-{expected_class}",
                     "passed": bool(passed), "expected_class": expected_class,
                     "observed_class": row["class"] if row else None, "note": note})


def selftest():
    controls = []
    scratch = ROOT / ".scratch"
    scratch.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="rga-", dir=scratch) as temporary:
        fixture_root = Path(temporary) / "repo"
        for rel, text in FIXTURES.items():
            path = fixture_root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        report = census(fixture_root)
        rows = {row["runner"]: row for row in report["runners"]}
        for rel, expected_class in FIXTURE_EXPECTED.items():
            _fixture_control(rows, rel, expected_class, controls)
        controls.append({
            "control": "fixture-census-covers-every-runner",
            "passed": sorted(rows) == sorted(FIXTURE_RUNNERS),
            "expected": sorted(FIXTURE_RUNNERS), "observed": sorted(rows)})
        controls.append({
            "control": "fixture-non-runner-writer-absent",
            "passed": "tools/fixture-helper.py" not in rows
            and all(row["runner"] != "tools/fixture-helper.py" for row in report["runners"]),
            "note": "a non-runner .py writing reports/round-41/validation.json is not a runner row"})
        controls.append({
            "control": "fixture-guarded-runners-not-flagged",
            "passed": all(rows[rel]["hazard"] is False
                          for rel in ("reports/round-41/run-validation.py",
                                      "reports/round-42/run-validation.py",
                                      "reports/round-43/run-validation.py",
                                      "reports/round-47/run-validation.py")),
            "note": "no false hazard flag on any guarded fixture"})
        controls.append({
            "control": "fixture-foreign-writes-not-flagged",
            "passed": rows["reports/round-49/run-validation.py"]["hazard"] is False
            and not rows["reports/round-49/run-validation.py"]["receipt_writes"],
            "note": "scratch-fixture and other-round writes are not own-receipt writes"})
        controls.append({
            "control": "fixture-flag-gated-guard-not-adopted",
            "passed": rows["reports/round-46/run-validation.py"]["class"] != "guarded-refresh"
            and any("flag-gated" in reason
                    for reason in rows["reports/round-46/run-validation.py"]["reasons"]),
            "note": "a guard call under an unset flag does not dominate the write"})
        controls.append({
            "control": "fixture-syntax-error-is-a-gap",
            "passed": report["census_complete"] is False
            and rows["reports/round-50/run-validation.py"]["class"] == "could-not-evaluate",
            "note": "an unparsable runner is a census gap, never a green"})
        controls.append({
            "control": "fixture-embedded-write-line",
            "passed": bool(
                [site for site in rows["reports/round-51/run-validation.py"]["embedded_receipt_writes"]
                 if site["line"] == 6 and site["kind"] == "embedded:write_text"]
                and not [site for site in rows["reports/round-51/run-validation.py"]
                         ["embedded_receipt_writes"] if site["kind"] == "embedded:open"]),
            "note": "the embedded write is located at its script line (fixture :6) and "
                    "the json.load(open(...)) read is not a site"})
        again = census(fixture_root)
        strip = lambda payload: json.dumps(  # noqa: E731
            {key: value for key, value in payload.items()
             if key not in ("date", "root")}, sort_keys=True)
        controls.append({"control": "fixture-deterministic",
                         "passed": strip(report) == strip(again),
                         "note": "same tree, same census"})

    live = census(ROOT)
    live_rows = {row["runner"]: row for row in live["runners"]}
    for rel, expected_class, line in CONTROL_LIVE:
        row = live_rows.get(rel)
        observed = row["class"] if row else None
        write_lines = [] if row is None else [site["line"] for site in row["receipt_writes"]]
        passed = observed == expected_class and (line in write_lines or line in
                                                 [site["line"] for site in
                                                  row.get("embedded_receipt_writes", [])]) \
            if row else False
        controls.append({"control": f"live-{Path(rel).parts[1]}-{expected_class}",
                         "passed": bool(passed), "expected_class": expected_class,
                         "observed_class": observed, "expected_write_line": line,
                         "observed_write_lines": write_lines})
    r26 = live_rows.get("reports/round-26/run-validation.py")
    provider = r26["receipt_writes"][0]["guard_provider"] if (r26 and r26["receipt_writes"]) else None
    controls.append({
        "control": "live-r26-guard-call-precedes-write",
        "passed": bool(r26 and r26["class"] == "guarded-refresh" and r26["hazard"] is False
                       and r26["receipt_writes"] and r26["receipt_writes"][0]["guarded"] is True
                       and provider and provider.get("kind") == "try-guard"
                       and provider.get("call_lines") == [1906]),
        "note": ("F-C13-1 (LOG.md:3559-3560) names r26 as carrying the unguarded "
                 "hazard; the bytes show the guard call at :1906 dominating the "
                 ":1909 write — recorded as finding RGA-1-r26, filed bytes not edited"),
        "observed": None if r26 is None else {
            "class": r26["class"],
            "write": r26["receipt_writes"][0]["line"] if r26["receipt_writes"] else None,
            "provider": r26["receipt_writes"][0]["guard_provider"]
            if r26["receipt_writes"] else None}})
    r19 = live_rows.get("reports/round-19/run-validation.py")
    controls.append({
        "control": "live-r19-embedded-receipt-write",
        "passed": bool(r19 and r19["class"] == "unguarded-in-place"
                       and [site for site in r19["embedded_receipt_writes"]
                            if site["line"] == 21 and site["kind"] == "embedded:write_text"]
                       and not [site for site in r19["embedded_receipt_writes"]
                                if site["kind"] == "embedded:open"]),
        "note": "the r19 receipt write lives inside a subprocess script string at :21; "
                "the open(...) read at :19 is not a site",
        "observed": None if r19 is None else [site["line"] for site in
                                              r19["embedded_receipt_writes"]]})
    controls.append({
        "control": "live-runner-census-floor",
        "passed": live["runner_count"] >= 28,
        "observed": live["runner_count"],
        "note": "28 runners were filed at baseline da68a6d; later rounds may add more"})
    controls.append({
        "control": "live-declared-hazard-four-classified",
        "passed": all(row["observed_class"] is not None for row in live["declared_hazards"]),
        "observed": [{"runner": row["runner"], "observed": row["observed_class"],
                      "agrees": row["agrees"]} for row in live["declared_hazards"]]})
    controls.append({
        "control": "live-findings-recorded",
        "passed": any(finding["kind"] == "declared-hazard-mismatch"
                      for finding in live["findings"])
        and any(finding["kind"] == "undeclared-unguarded-writer"
                for finding in live["findings"]),
        "observed": [finding["id"] for finding in live["findings"]]})
    controls.append({
        "control": "live-guard-digest",
        "passed": bool(live["guard_tool"]["sha256"]),
        "observed": live["guard_tool"]["sha256"]})
    passed = sum(1 for control in controls if control["passed"])
    receipt = {
        "tool": TOOL,
        "command": f"python3 {TOOL} --selftest",
        "date": dt.date.today().isoformat(),
        "fixture_count": len(FIXTURE_EXPECTED),
        "live_runner_count": live["runner_count"],
        "live_class_counts": live["class_counts"],
        "live_findings": [finding["id"] for finding in live["findings"]],
        "controls": controls,
        "controls_passed": passed,
        "controls_total": len(controls),
        "selftest_passed": passed == len(controls),
        "limits": [
            "Fixtures are synthetic runners under a disposable in-repo .scratch "
            "directory; no filed runner is executed and no filed byte is written.",
            "The live controls read filed bytes only; they assert the census's "
            "deterministic reading, including the r26 byte fact that disagrees "
            "with the F-C13-1 parenthetical (finding RGA-1-r26).",
        ],
    }
    return receipt


# ----------------------------------------------------------------------- cli


def render_text(report):
    lines = [f"{report['tool']}  mode={report['mode']}  date={report['date']}"]
    if report["mode"] == "runner-census":
        lines.append(f"{'class':<22}{'runner':<46}{'write':<10}guard")
        for row in report["runners"]:
            write_lines = ",".join(':' + str(site["line"]) for site in
                                   (row["receipt_writes"] + row.get("embedded_receipt_writes", [])))
            guard_lines = ",".join(':' + str(call["line"]) for call in row["guard"]["calls"])
            lines.append(f"{row['class']:<22}{row['runner']:<46}"
                         f"{write_lines or '-':<10}{guard_lines or '-'}")
        lines.append("class_counts: " + " ".join(
            f"{name}={count}" for name, count in report["class_counts"].items()))
        lines.append(f"hazard_count: {report['hazard_count']}  "
                     f"census_complete: {report['census_complete']}")
        for finding in report["findings"]:
            lines.append(f"finding {finding['id']}: {finding['detail']}")
    else:
        for row in report["writers"]:
            lines.append(f"{row['kind']:<12}{row['path']}")
            for write in row["receipt_writes"]:
                lines.append(f"    :{write['line']} {write['kind']} -> {write['resolved']}")
        lines.append(f"writers: {len(report['writers'])}  "
                     f"parse_gaps: {len(report['parse_gaps'])}  "
                     f"sweep_complete: {report['sweep_complete']}")
    return "\n".join(lines) + "\n"


def _safe_out(root, candidate):
    path = Path(candidate)
    if path.is_absolute() or ".." in path.parts or ".git" in path.parts:
        raise SystemExit(f"{TOOL}: --out must be a repo-relative path: {candidate}")
    if path.name == RECEIPT_NAME:
        raise SystemExit(f"{TOOL}: refusing to write a receipt path: {candidate}")
    return root / path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true",
                        help="print the census JSON on stdout")
    parser.add_argument("--out", metavar="PATH",
                        help="write the census JSON to a repo-relative path")
    parser.add_argument("--root", type=Path, default=ROOT,
                        help="repository root to census (default: this lane)")
    parser.add_argument("--sweep-repo", action="store_true",
                        help="census every .py under reports/ and tools/ for "
                             "filed-receipt writes, runners and non-runners alike")
    parser.add_argument("--selftest", action="store_true",
                        help="run fixture and live-bytes controls; prints a control receipt")
    args = parser.parse_args(argv)
    if args.selftest:
        if args.json or args.out or args.sweep_repo or args.root != ROOT:
            parser.error("--selftest takes no other arguments")
        receipt = selftest()
        sys.stdout.write(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        return 0 if receipt["selftest_passed"] else 1
    root = args.root.resolve()
    if not root.is_dir():
        print(f"{TOOL}: root is not a directory: {root}", file=sys.stderr)
        return 2
    report = sweep_repo(root) if args.sweep_repo else census(root)
    rendered = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.out:
        destination = _safe_out(root, args.out)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(rendered, encoding="utf-8")
    if args.json:
        sys.stdout.write(rendered)
    else:
        sys.stdout.write(render_text(report))
    complete = report["census_complete"] if not args.sweep_repo else report["sweep_complete"]
    return 0 if complete else 1


if __name__ == "__main__":
    sys.exit(main())
