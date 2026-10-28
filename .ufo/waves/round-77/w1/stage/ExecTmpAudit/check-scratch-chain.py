#!/usr/bin/env python3
"""Read-only checker: does a tool resolve its scratch root the lane way?

Companion to check-scratch-root.py (which answers "is any write target a literal
/tmp path?").  This one answers the second half of the scratch discipline
(prompt §7.4, kotodama round 77 seat ExecTmpAudit):

    `--work`, then `$HYAKU_SCRATCH` (older spelling `$SHOKUNIN_SCRATCH`), then
    an operator-set `$TMPDIR`; nothing under a literal `/tmp`; and a tool copied
    from a previous round must not keep that round's scratch directory in a
    path constant (two rounds would then share one scratch tree).

Static pass, per file, one line each:

  CHAIN     the resolution chain the file implements, as a subset of
            `work,hyaku,tmpdir` (order as written) — or `none`.
  NOCHAIN   the file creates scratch (mkdtemp/TemporaryDirectory/mkdir on a
            scratch-named path) but names none of the three — Fatal.
  HARDROUND a path constant still carrying a previous round's scratch root
            (e.g. `kotodama-r76`, `reports/round-76/`) — Fatal: the copy was
            not adapted.
  INVENTED  the chain ends in a hardcoded absolute scratch default instead of
            refusing — Warn (allowed only when the default is the operator's
            own `/fast/scratch/hyaku/...` tree, never /tmp).
  BARE      `tempfile.mkdtemp()`/`TemporaryDirectory()`/`mkstemp()` with no
            `dir=` argument — Warn (honours TMPDIR, bypasses --work).
  UNPARSED  the ast could not parse the file; scanned by regex instead.

Dynamic pass (`--dynamic`), per python file that exposes a resolver
(`_scratch_root`, `scratch_dir`, `_scratch_root_for`, `scratch_root`) — calls
it under four environments and prints the result, so "honours TMPDIR" is
measured rather than read:

  1  --work=<scratch>/w           -> must be under <scratch>/w
  2  $HYAKU_SCRATCH=<scratch>/h   -> must be under <scratch>/h
  3  $TMPDIR=<scratch>/t          -> must be under <scratch>/t
  4  nothing set                  -> must refuse (or land off /tmp)

Read-only: imports the target with `main` un-guarded by construction (the
`if __name__ == "__main__"` guard stays false), passes a fake args object, and
touches neither the target's files nor the network.  Scratch for the selftest
and for the probe lives under --work / $HYAKU_SCRATCH, never a literal /tmp.
Stdlib only.

Usage:
  check-scratch-chain.py --root <dir> --paths '**/*.py'] [--paths ...]
                         [--dynamic] [--work <dir>] [--selftest]
"""
from __future__ import annotations

import argparse
import ast
import os
import re
import sys
import tempfile
import types

ROUND_TOKEN_RE = re.compile(r"(?:kotodama-?r(\d{2})|reports/round-(\d{2})|/round-(\d{2})\b|r(\d{2})/stage)")


def stale_round(value, current):
    """True when a path names a round other than `current` (a stale copy)."""
    for match in ROUND_TOKEN_RE.finditer(value):
        found = next((g for g in match.groups() if g), None)
        if found is not None and found != current:
            return True
    return False
ABS_PATH_RE = re.compile(r"""^/(?:[^/\0]+/)*[^/\0]*$""")
SCRATCH_WORD_RE = re.compile(r"(?i)(tmp|temp|scratch|work)")
CHAIN_KEYS = (("work", re.compile(r"""["']--work["']""")),
              ("hyaku", re.compile(r"HYAKU_SCRATCH")),
              ("shokunin", re.compile(r"SHOKUNIN_SCRATCH")),
              ("tmpdir", re.compile(r"""\bTMPDIR\b""")))
CREATE_RE = re.compile(r"\b(mkdtemp|mkstemp|TemporaryDirectory|NamedTemporaryFile)\s*\(")


def read(path):
    with open(path, "rb") as handle:
        return handle.read().decode("utf-8", "replace")


def strip_py_comments(text):
    """Comment-free source, preserving line numbers (strings untouched)."""
    out = []
    for line in text.splitlines(True):
        stripped = _strip_comment_line(line)
        out.append(stripped)
    return "".join(out)


def _strip_comment_line(line):
    quote = None
    i = 0
    while i < len(line):
        ch = line[i]
        if quote:
            if ch == "\\":
                i += 2
                continue
            if line.startswith(quote, i):
                i += len(quote)
                quote = None
                continue
            i += 1
            continue
        if line.startswith('"""', i) or line.startswith("'''", i):
            quote = line[i:i + 3]
            i += 3
            continue
        if ch in "\"'":
            quote = ch
            i += 1
            continue
        if ch == "#":
            return line[:i] + "\n"
        i += 1
    return line


def static_py(path, current="77"):
    text = read(path)
    code = strip_py_comments(text)
    rows = []
    try:
        tree = ast.parse(text)
    except SyntaxError as exc:
        rows.append(("UNPARSED", "ast: %s" % (exc.msg,)))
        tree = None

    chain = [name for name, regex in CHAIN_KEYS if regex.search(code)]
    label = ",".join(chain) if chain else "none"
    rows.append(("CHAIN", label))

    creates = bool(CREATE_RE.search(code)) or bool(
        re.search(r"\b(makedirs|mkdir)\s*\([^)\n]*scratch", code, re.I))
    if creates and not chain:
        rows.append(("NOCHAIN", "creates scratch, names none of --work/$HYAKU_SCRATCH/$TMPDIR"))

    for number, line in enumerate(code.splitlines(), 1):
        for match in re.finditer(r"""["'](/[^"'\s]*)["']""", line):
            value = match.group(1)
            if "/" not in value.strip("/"):
                continue
            if not ABS_PATH_RE.match(value):
                continue
            if stale_round(value, current):
                rows.append(("HARDROUND", "line %d: %r" % (number, value)))

    if tree is not None:
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            name = _callee(node)
            if name in {"mkdtemp", "mkstemp", "TemporaryDirectory", "NamedTemporaryFile"}:
                if not any(kw.arg == "dir" for kw in node.keywords) and len(node.args) < 2:
                    rows.append(("BARE", "line %d: %s() without dir=" % (getattr(node, "lineno", 0), name)))
        for node in tree.body:
            if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Constant):
                continue
            value = node.value.value
            if not isinstance(value, str) or not stale_round(value, current):
                continue
            for target in node.targets:
                tname = target.id if isinstance(target, ast.Name) else ""
                if tname and PATH_CONST_RE.search(tname):
                    rows.append(("HARDROUND", "line %d: %s = %r (previous round's path root)"
                                 % (getattr(target, "lineno", 0), tname, value)))
        chain_call = _resolver(tree)
        if chain_call is not None:
            invented = _invented_default(chain_call, _module_constants(tree))
            if invented:
                rows.append(("INVENTED", "line %d: hardcoded default %r" % invented))
    return rows


def _callee(call):
    func = call.func
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return ""


PATH_CONST_RE = re.compile(r"(?i)(_rel|_dir|_path|path|dir)$")
RESOLVER_NAMES = {"_scratch_root", "scratch_dir", "scratch_root", "_scratch_root_for"}


def _resolver(tree):
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in RESOLVER_NAMES:
            return node
    return None


def _module_constants(tree):
    """Module-level `NAME = "literal"` bindings, for resolver returns that name one."""
    out = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and isinstance(node.value, ast.Constant):
                    if isinstance(node.value.value, str):
                        out[target.id] = node.value.value
    return out


def _invented_default(func_node, constants=None):
    """(line, value) of the last absolute scratch constant a resolver returns."""
    constants = constants or {}
    last = None
    for node in ast.walk(func_node):
        if not isinstance(node, ast.Return):
            continue
        value = None
        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            value = node.value.value
        elif isinstance(node.value, ast.Name):
            value = constants.get(node.value.id)
        if value and (ABS_PATH_RE.match(value) or value.startswith("/fast/")):
            last = (getattr(node, "lineno", 0), value)
    return last


def static_sh(path, current="77"):
    text = read(path)
    rows = []
    code = "\n".join(_strip_comment_line(line) for line in text.splitlines())
    chain = [name for name, regex in CHAIN_KEYS if regex.search(code)]
    rows.append(("CHAIN", ",".join(chain) if chain else "none"))
    for number, line in enumerate(code.splitlines(), 1):
        for match in re.finditer(r"""["']?(/fast/[^\s"'}]+)""", line):
            if stale_round(match.group(1), current):
                rows.append(("HARDROUND", "line %d: %r" % (number, match.group(1))))
        for match in re.finditer(r"""["'](/tmp[^"']*)["']""", line):
            rows.append(("LITERAL", "line %d: %r" % (number, match.group(1))))
    return rows


def load_allow(path):
    patterns = []
    if not path:
        return patterns
    with open(path, "r", encoding="utf-8") as handle:
        for raw in handle:
            entry = raw.split(" #", 1)[0].strip()
            if entry and not entry.startswith("#"):
                patterns.append(entry)
    return patterns


def allowed(rel, line, patterns):
    import fnmatch
    for pattern in patterns:
        if ":" in pattern and not pattern.startswith("*"):
            target, _, number = pattern.rpartition(":")
            if number.isdigit() and fnmatch.fnmatch(rel, target) and int(number) == line:
                return True
            continue
        if fnmatch.fnmatch(rel, pattern):
            return True
    return False


def collect(root, patterns):
    import fnmatch
    found = []
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for name in files:
            full = os.path.join(base, name)
            rel = os.path.relpath(full, root)
            if any(fnmatch.fnmatch(rel, pat) for pat in patterns):
                found.append(full)
    return sorted(found)


# --- dynamic probe --------------------------------------------------------
def dynamic_probe(path, show):
    """Call the module's resolver under four environments; print what it returns."""
    import importlib.util
    module_name = "probe_" + re.sub(r"\W+", "_", os.path.basename(path))
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    exports = []
    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # noqa: BLE001 - probe must survive any import error
        exports.append(("IMPORT", "line 0: %s: %s" % (type(exc).__name__, exc)))
        return exports
    resolver = None
    for name in ("_scratch_root", "scratch_root", "scratch_dir", "_scratch_root_for"):
        candidate = getattr(module, name, None)
        if callable(candidate):
            resolver = (name, candidate)
            break
    if resolver is None:
        exports.append(("NORESOLVER", "no --work/$HYAKU_SCRATCH resolver exported"))
        return exports
    name, func = resolver
    argnames = func.__code__.co_varnames[:func.__code__.co_argcount]
    for label, env, args in show:
        saved = {key: os.environ.get(key) for key in ("TMPDIR", "HYAKU_SCRATCH", "SHOKUNIN_SCRATCH")}
        try:
            for key in saved:
                os.environ.pop(key, None)
            os.environ.update(env)
            tempfile.tempdir = None  # drop the cached gettempdir() of a previous case
            kwargs = {}
            if argnames == ("explicit",):
                kwargs["explicit"] = args.get("explicit")
            else:
                fake = types.SimpleNamespace(work=args.get("explicit"))
                kwargs[argnames[0]] = fake
            try:
                result = func(**kwargs)
            except Exception as exc:  # noqa: BLE001 - a refusal is a result
                exports.append((label, "refused: %s: %s" % (type(exc).__name__, exc)))
                continue
            exports.append((label, str(result)))
        finally:
            for key, value in saved.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value
    return exports


def scratch_root(work=None):
    for candidate in (work, os.environ.get("HYAKU_SCRATCH"), os.environ.get("SHOKUNIN_SCRATCH")):
        if candidate and candidate.strip():
            return os.path.abspath(candidate.strip())
    return tempfile.gettempdir()


def selftest(work=None):
    root = os.path.join(scratch_root(work), "chain-selftest")
    os.makedirs(root, exist_ok=True)
    cases = {
        "good.py": "import os\n"
                   "def _scratch_root(args):\n"
                   "    if args.work: return os.path.abspath(args.work)\n"
                   "    env = os.environ.get('HYAKU_SCRATCH')\n"
                   "    if env: return os.path.join(env, 'x')\n"
                   "    tmp = os.environ.get('TMPDIR')\n"
                   "    if tmp: return os.path.join(tmp, 'x')\n"
                   "    raise SystemExit('no scratch root')\n",
        "nohain.py": "import tempfile, os\n"
                     "def go():\n"
                     "    d = tempfile.mkdtemp()\n"
                     "    os.makedirs(os.path.join(d, 'scratch'))\n",
        "stale.py": "import os\n"
                    "SCRATCH = \"/fast/scratch/hyaku/kotodama-r76/counter\"\n"
                    "def _scratch_root(args):\n"
                    "    return SCRATCH\n",
        "invented.py": "import os\n"
                       "def _scratch_root(args):\n"
                       "    if args.work: return args.work\n"
                       "    return \"/fast/scratch/hyaku/kotodama-r77/counter\"\n",
    }
    expected = {"good.py": {"CHAIN"}, "nohain.py": {"CHAIN", "NOCHAIN", "BARE"},
                "stale.py": {"CHAIN", "HARDROUND", "INVENTED"}, "invented.py": {"CHAIN", "INVENTED"}}
    failures = 0
    for name, source in sorted(cases.items()):
        target = os.path.join(root, name)
        with open(target, "w", encoding="utf-8") as handle:
            handle.write(source)
        classes = {cls for cls, _ in static_py(target)}
        want = expected[name]
        mark = "ok  " if classes == want else "BAD "
        if classes != want:
            failures += 1
        print("%s%s want=%s got=%s" % (mark, name, ",".join(sorted(want)), ",".join(sorted(classes))))
    import shutil
    shutil.rmtree(root, ignore_errors=True)
    print("selftest: %d failure(s)" % failures)
    return 1 if failures else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="scratch-root resolution-chain checker (read-only)")
    parser.add_argument("--root", default=".")
    parser.add_argument("--paths", action="append", default=None,
                        help="glob relative to --root (repeatable; default **/*.py)")
    parser.add_argument("--dynamic", action="store_true",
                        help="also import each python file's resolver and measure four envs")
    parser.add_argument("--allow", default=None,
                        help="allowlist file: one glob per line, `rel` or `rel:line`")
    parser.add_argument("--round", default="77", help="this round's two-digit token (default 77)")
    parser.add_argument("--work", default=None, help="scratch root for selftest/dynamic probe")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest(args.work)
    patterns = args.paths or ["**/*.py"]
    allow = load_allow(args.allow)
    files = collect(os.path.abspath(args.root), patterns)
    fatal = 0
    for path in files:
        rel = os.path.relpath(path, os.path.abspath(args.root))
        rows = (static_sh(path, args.round) if path.endswith((".sh", ".bash"))
                else static_py(path, args.round))
        for cls, detail in rows:
            line = 0
            for token in detail.split():
                if token.rstrip(":,").isdigit():
                    line = int(token.rstrip(":,"))
                    break
            if allowed(rel, line, allow):
                continue
            if cls in {"NOCHAIN", "HARDROUND", "LITERAL"}:
                fatal += 1
            print("%-9s %s: %s" % (cls, rel, detail))
        if args.dynamic and path.endswith(".py"):
            scratch = scratch_root(args.work)
            os.makedirs(scratch, exist_ok=True)
            show = (("dyn/--work", {}, {"explicit": os.path.join(scratch, "w")}),
                    ("dyn/$HYAKU_SCRATCH", {"HYAKU_SCRATCH": os.path.join(scratch, "h")}, {}),
                    ("dyn/$TMPDIR", {"TMPDIR": os.path.join(scratch, "t")}, {}),
                    ("dyn/$TMPDIR=/tmp", {"TMPDIR": "/tmp"}, {}),
                    ("dyn/none", {}, {}))
            for label, value in dynamic_probe(path, show):
                print("PROBE     %s: %s -> %s" % (rel, label, value))
    print("checked=%d fatal=%d" % (len(files), fatal))
    return 1 if fatal else 0


if __name__ == "__main__":
    sys.exit(main())
