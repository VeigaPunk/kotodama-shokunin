#!/usr/bin/env python3
"""Read-only scanner: does a committed script write scratch under a literal /tmp?

Prompt §7.4 (kotodama round 76, seat ExecTmpAudit).  The lane rule is that every
scratch root is routed: `--work`, then `$HYAKU_SCRATCH`, then the older
`$SHOKUNIN_SCRATCH`, then the system tempdir.  A *literal* `/tmp` root breaks
that chain on hosts where /tmp is small or inode-exhausted, and leaves the files
behind after the run.

Three classes are reported, one per line, `<CLASS> <rel>:<line>: <detail>`:

  HIT       a write target (open() in a write mode, mkdir/makedirs, a temp
            `dir=`/`cwd=` keyword, an shutil copy destination, a redirect or
            mktemp path) that is a literal /tmp path.  Exit 1 — this is the
            routed defect.
  FALLBACK  `os.environ.get("TMPDIR", "/tmp")` — inherits the literal /tmp when
            the variable is unset.  Reported, does not fail unless --strict.
  UNROUTED  `tempfile.mkdtemp()`/`TemporaryDirectory()`/`mkstemp()`/
            `NamedTemporaryFile()` with no `dir=` — honours TMPDIR but bypasses
            --work/$HYAKU_SCRATCH.  Reported, does not fail unless --strict.
  UNPARSED  a .py file the ast would not parse (scanned by the shell rules
            instead).  Reported, never fatal.

Read-only: opens files, writes nothing, creates no directory.  Stdlib only.

Usage:
  check-scratch-root.py --root <dir> --paths 'tools/**/*.py' --paths 'x.sh' \
                        [--allow allow.txt] [--strict] [--selftest]
"""
from __future__ import annotations

import argparse
import ast
import fnmatch
import os
import re
import sys
import tempfile

PY_SUFFIXES = (".py",)
SH_SUFFIXES = (".sh", ".bash")

# callee basenames
WRITE_PATH_FUNCS = {"open", "makedirs", "mkdir", "mkfifo", "mknode",
                    "write_text", "write_bytes", "touch"}
TEMP_FUNCS = {"mkdtemp", "mkstemp", "TemporaryDirectory",
              "NamedTemporaryFile", "SpooledTemporaryFile"}
COPY_FUNCS = {"copy", "copy2", "copyfile", "copytree", "move"}
DESTRUCT_FUNCS = {"rmtree", "remove", "unlink", "rmdir"}
WRITE_MODES = set("wax+")  # any mode string carrying one of these writes
ENV_KEYS = {"TMPDIR", "TMP", "TEMP", "HYAKU_SCRATCH", "SHOKUNIN_SCRATCH"}
SCRATCH_NAME_RE = re.compile(r"(?i)(tmp|temp|scratch|work)")

# shell: only write-shaped uses of a literal /tmp, never a read
SH_RULES = (
    (re.compile(r"(?:^|[^<>&>])>>?\s*/tmp(?:/|\b)"), "redirect target"),
    (re.compile(r"\bmktemp\b[^;|&]*?\s/tmp(?:/|\b)"), "mktemp path"),
    (re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*=(?:\$\{[A-Za-z_][A-Za-z0-9_]*:-)?/tmp(?:/|\s|$)"),
     "variable = literal /tmp root"),
    (re.compile(r"\bmkdir\s+(?:-\w+\s+)*/tmp(?:/|\b)"), "mkdir path"),
    (re.compile(r"\bcd\s+/tmp(?:/|\b)"), "cwd"),
    (re.compile(r"\b(?:cp|mv|install|tar|unzip)\b[^;|&]*?\s/tmp(?:/|\b)"), "copy destination"),
)


def is_tmp_path(value):
    """True for the literal /tmp and anything below it (never /var/tmp)."""
    if not isinstance(value, str):
        return False
    return value == "/tmp" or value.startswith("/tmp/") or value.startswith("/tmp.")


def const_str(node):
    """Best-effort static string of an expression, or None.

    Handles a plain literal, an f-string whose leading part is literal,
    `Path("...")`, and `os.path.join("...", "...")` when every part is static.
    """
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr) and node.values:
        head = node.values[0]
        if isinstance(head, ast.Constant) and isinstance(head.value, str):
            return head.value
        return None
    if isinstance(node, ast.Attribute) and node.attr == "sep":
        # `os.sep` / `os.path.sep` — the disguised spelling of the root
        return os.sep
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left, right = const_str(node.left), const_str(node.right)
        if left is not None and right is not None:
            return left + right
        return None
    if isinstance(node, ast.Call):
        name = callee_name(node)
        if name in {"Path", "PurePath"}:
            if node.args:
                return const_str(node.args[0])
            return None
        if name in {"join", "abspath", "normpath", "expanduser", "realpath"}:
            parts = [const_str(a) for a in node.args]
            if parts and all(p is not None for p in parts):
                return os.path.join(*parts)
            return None
    return None


def uses_sep(node):
    """True when the static value needed `os.sep` folded into it."""
    if node is None:
        return False
    for child in ast.walk(node):
        if isinstance(child, ast.Attribute) and child.attr == "sep":
            return True
    return False


def cls_for(node, base):
    """`DISGUISED` when the /tmp value is spelled through os.sep."""
    return "DISGUISED" if uses_sep(node) else base


def callee_name(call):
    func = call.func
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return ""


def keyword(node, name):
    for kw in node.keywords or ():
        if kw.arg == name:
            return kw.value
    return None


def iter_calls(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            yield node


def at(node, fallback=0):
    """Line of the node that actually carries the path, not of the call head."""
    return getattr(node, "lineno", fallback) or fallback


def scan_python(text):
    """[(line, cls, detail)] for one python source text.

    The reported line is the argument that carries the /tmp constant, so a line
    grep hit and a scanner row name the same line for the same defect.
    """
    out = []
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return None
    for call in iter_calls(tree):
        name = callee_name(call)
        call_line = getattr(call, "lineno", 0)
        # routed keywords: a literal /tmp here *is* the scratch target
        for kw_name in ("dir", "cwd", "default", "tmpdir", "work", "scratch", "root"):
            value = keyword(call, kw_name)
            static = const_str(value) if value is not None else None
            if is_tmp_path(static):
                out.append((at(value, call_line), "HIT",
                            "%s=/tmp under %s()" % (kw_name, name or "?")))
        # tempfile.* with no dir= bypasses --work/$HYAKU_SCRATCH
        if name in TEMP_FUNCS and keyword(call, "dir") is None:
            out.append((call_line, "UNROUTED", "%s() without dir=" % name))
        # os.environ.get("TMPDIR", "/tmp") and friends
        if name == "get" and len(call.args) >= 2:
            key = const_str(call.args[0])
            envish = key in ENV_KEYS or (isinstance(key, str) and "TMPDIR" in key)
            if envish and is_tmp_path(const_str(call.args[1])):
                out.append((at(call.args[1], call_line),
                            cls_for(call.args[1], "FALLBACK"),
                            "os.environ.get(%r, %r)" % (key, const_str(call.args[1]))))
        if name in WRITE_PATH_FUNCS:
            target_node = None
            if call.args:
                target_node = call.args[0]
            elif isinstance(call.func, ast.Attribute):
                target_node = call.func.value  # Path("/tmp/x").mkdir()
            target = const_str(target_node) if target_node is not None else None
            line = at(target_node, call_line)
            if is_tmp_path(target):
                if name == "open":
                    mode_node = (call.args[1] if len(call.args) > 1
                                 else keyword(call, "mode"))
                    mode = const_str(mode_node) if mode_node is not None else "r"
                    if mode is None or not (set(mode) & WRITE_MODES):
                        continue
                    out.append((line, cls_for(target_node, "HIT"),
                                "open(%r, mode=%r)" % (target, mode)))
                else:
                    out.append((line, cls_for(target_node, "HIT"),
                                "%s(%r)" % (name, target)))
        if name in COPY_FUNCS:
            for arg in call.args:
                static = const_str(arg)
                if is_tmp_path(static):
                    out.append((at(arg, call_line), cls_for(arg, "HIT"),
                                "%s destination %r" % (name, static)))
        if name in DESTRUCT_FUNCS:
            static = const_str(call.args[0]) if call.args else None
            if is_tmp_path(static):
                out.append((at(call.args[0], call_line), cls_for(call.args[0], "HIT"),
                            "%s(%r)" % (name, static)))
    for node in ast.walk(tree):
        # X = "/tmp" where X names a scratch root (R74_TMPDIR and cousins)
        if isinstance(node, ast.Assign):
            static = const_str(node.value)
            if not is_tmp_path(static):
                continue
            for target in node.targets:
                tname = target.id if isinstance(target, ast.Name) else (
                    target.attr if isinstance(target, ast.Attribute) else "")
                if tname and SCRATCH_NAME_RE.search(tname):
                    out.append((at(target, node.lineno), cls_for(node.value, "HIT"),
                                "%s = %r" % (tname, static)))
        # {"TMPDIR": "/tmp"} handed to a subprocess
        if isinstance(node, ast.Dict):
            for key, value in zip(node.keys, node.values):
                static_key = const_str(key) if key is not None else None
                static_value = const_str(value)
                if static_key in ENV_KEYS and is_tmp_path(static_value):
                    out.append((at(key, node.lineno), cls_for(value, "HIT"),
                                "env %s=%r" % (static_key, static_value)))
    out.extend(scan_embedded(tree))
    return out


CODE_NAME_RE = re.compile(r"(?i)(bootstrap|script|prog|snippet|runner|^_?code|source)")


def scan_embedded(tree):
    """[(line, cls, detail)] for python code embedded in a named constant.

    A counter that shells out with `python -c "<prog>"` carries a second program
    in a string literal; the outer ast never sees its /tmp paths.  Only a
    module-level `NAME = "..."` whose NAME reads as code (BOOTSTRAP, SCRIPT,
    PROG, ...) is treated as a program — a data fixture that merely quotes an
    example command stays out, which keeps the scanner's own selftest fixtures
    clean.  Rows are reported against the assignment line as
    `embedded (+N): <detail>`.
    """
    out = []
    for node in tree.body:
        if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Constant):
            continue
        text = node.value.value
        if not isinstance(text, str) or "\n" not in text:
            continue
        names = [t.id for t in node.targets if isinstance(t, ast.Name)]
        if not any(CODE_NAME_RE.search(name) for name in names):
            continue
        try:
            ast.parse(text)
        except SyntaxError:
            continue
        base = getattr(node, "lineno", 0)
        for line, cls, detail in scan_python(text):
            out.append((base, cls, "embedded (+%d): %s" % (line, detail)))
    return out


def strip_shell_comment(line):
    out, quote = [], None
    for char in line:
        if quote:
            out.append(char)
            if char == quote:
                quote = None
            continue
        if char in "'\"":
            quote = char
        elif char == "#" and (not out or out[-1].isspace()):
            break
        out.append(char)
    return "".join(out)


def scan_shell(text):
    out = []
    for number, raw in enumerate(text.splitlines(), 1):
        line = strip_shell_comment(raw)
        if "/tmp" not in line:
            continue
        for pattern, why in SH_RULES:
            if pattern.search(line):
                out.append((number, "HIT", "shell %s" % why))
                break
    return out


def scan_file(path, root):
    rel = os.path.relpath(path, root)
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            text = handle.read()
    except OSError as exc:
        return [(0, "UNREAD", str(exc))], rel
    if path.endswith(SH_SUFFIXES):
        return scan_shell(text), rel
    found = scan_python(text)
    if found is None:
        return scan_shell(text) + [(0, "UNPARSED", "ast refused; shell rules only")], rel
    return found, rel


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
    for pattern in patterns:
        if fnmatch.fnmatch(rel, pattern) or fnmatch.fnmatch("%s:%d" % (rel, line), pattern):
            return True
    return False


def pattern_regex(pattern):
    """A glob matcher that also walks hidden segments (`**` must not skip .ufo).

    glob.glob's `*` refuses a leading dot, so `.ufo/**/*.py` would silently scan
    nothing; the lane's wave machinery lives exactly there.
    """
    out, index = [], 0
    while index < len(pattern):
        if pattern.startswith("**/", index):
            out.append(r"(?:[^/]+/)*")
            index += 3
        elif pattern.startswith("**", index):
            out.append(r".*")
            index += 2
        elif pattern[index] == "*":
            out.append(r"[^/]*")
            index += 1
        elif pattern[index] == "?":
            out.append(r"[^/]")
            index += 1
        else:
            out.append(re.escape(pattern[index]))
            index += 1
    return re.compile("^" + "".join(out) + "$")


def collect(root, paths):
    """(files, patterns that matched nothing) — one walk, no symlink following."""
    compiled = [(pattern, pattern_regex(pattern)) for pattern in paths]
    matched = set()
    files = set()
    root = os.path.abspath(root)
    for directory, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for name in filenames:
            path = os.path.join(directory, name)
            rel = os.path.relpath(path, root).replace(os.sep, "/")
            for pattern, regex in compiled:
                if regex.match(rel):
                    matched.add(pattern)
                    files.add(path)
                    break
    missing = [pattern for pattern, _ in compiled if pattern not in matched]
    return sorted(files), missing


def scan(root, patterns, allow_patterns=()):
    """Return (rows, missing, checked) — rows are (cls, rel, line, detail, is_allowed)."""
    files, missing = collect(root, patterns)
    rows = []
    for path in files:
        found, rel = scan_file(path, root)
        for line, cls, detail in found:
            rows.append((cls, rel, line, detail, allowed(rel, line, allow_patterns)))
    return rows, missing, len(files)


def report(rows, missing, checked, strict):
    counts = {}
    for cls, rel, line, detail, is_allowed in rows:
        key = cls + ("(allowlisted)" if is_allowed else "")
        counts[key] = counts.get(key, 0) + 1
        print("%-9s %s:%d: %s" % (cls, rel, line, detail))
    for pattern in missing:
        print("NOMATCH   %s: no file matched" % pattern)
    ordered = " ".join("%s=%d" % (k, counts[k]) for k in sorted(counts))
    print("checked=%d %s" % (checked, ordered or "clean"))
    live_hits = [r for r in rows if r[0] == "HIT" and not r[4]]
    live_strict = [r for r in rows if r[0] in ("HIT", "FALLBACK", "UNROUTED") and not r[4]]
    if live_hits or (strict and live_strict):
        return 1
    return 0


# --- selftest -------------------------------------------------------------
# Every fixture below is written under the resolved scratch root, never under a
# literal /tmp: the scanner is run in-process, the files are temporary, and the
# selftest proves the class of each fixture rather than trusting the reader.
FIXTURES = [
    # (name, suffix, body, expected classes on the payload line)
    ("hit_mkdtemp_dir", ".py",
     'import tempfile\ntmp = tempfile.mkdtemp(dir="/tmp")\n', ["HIT"]),
    ("hit_mkdtemp_prefix_dir", ".py",
     "import tempfile\ntmp = tempfile.mkdtemp(prefix='r76-', dir='/tmp')\n", ["HIT"]),
    ("hit_open_write", ".py",
     "open('/tmp/x.txt', 'w').close()\n", ["HIT"]),
    ("hit_open_write_kw", ".py",
     "with open('/tmp/x.txt', mode='a') as fh:\n    fh.write('x')\n", ["HIT"]),
    ("hit_path_mkdir", ".py",
     "import pathlib\npathlib.Path('/tmp/r76-run').mkdir(parents=True, exist_ok=True)\n",
     ["HIT"]),
    ("hit_env_dict", ".py",
     "env = {'TMPDIR': '/tmp'}\n", ["HIT"]),
    ("hit_scratch_assign", ".py",
     'R74_TMPDIR = "/tmp"\n', ["HIT"]),
    ("hit_popen_cwd", ".py",
     "import subprocess\nsubprocess.run(['ls'], cwd='/tmp/build')\n", ["HIT"]),
    ("hit_sh_mktemp", ".sh",
     "OUT=$(mktemp -d /tmp/r76-XXXXXX)\n", ["HIT"]),
    ("hit_sh_redirect", ".sh",
     "census validate --file x > /tmp/r76-census.out 2>&1\n", ["HIT"]),
    ("miss_comment", ".py",
     "# scratch never goes under /tmp; use $HYAKU_SCRATCH\nx = 1\n", []),
    ("miss_docstring", ".py",
     '"""Scratch lives under --work/$HYAKU_SCRATCH (never a literal /tmp)."""\nx = 1\n',
     []),
    ("miss_read", ".py",
     "open('/tmp/log.txt')\nwith open('/tmp/log.txt', 'r') as fh:\n    fh.read()\n", []),
    ("miss_read_dir", ".py",
     "import os\nprint(os.listdir('/tmp'))\n", []),
    ("miss_sh_read", ".sh",
     "cat /tmp/r73-mirror-census.out\ngrep -c W04 /tmp/r73-mirror-census.out\n# /tmp is forbidden\n",
     []),
    ("unrouted_mkdtemp", ".py",
     "import tempfile\ntmp = tempfile.mkdtemp()\n", ["UNROUTED"]),
    ("fallback_tmpdir", ".py",
     'import os\nenv = {"TMPDIR": os.environ.get("TMPDIR", "/tmp")}\n', ["FALLBACK"]),
    ("allowlisted", ".py",
     "open('/tmp/allowed.txt', 'w').close()\n", ["HIT"]),
]


def scratch_root(work=None):
    """--work, then $HYAKU_SCRATCH, then $SHOKUNIN_SCRATCH, then the tempdir."""
    for candidate in (work, os.environ.get("HYAKU_SCRATCH"),
                      os.environ.get("SHOKUNIN_SCRATCH")):
        if candidate and candidate.strip():
            return os.path.abspath(candidate.strip())
    return tempfile.gettempdir()


def selftest(work=None):
    import shutil

    failures = []

    def check(name, condition, detail=""):
        print(("PASS " if condition else "FAIL ") + name + (" " + detail if detail else ""))
        if not condition:
            failures.append(name)

    root = tempfile.mkdtemp(prefix="scratch-root-selftest-", dir=scratch_root(work))
    os.makedirs(os.path.join(root, "tree"))
    allow_path = os.path.join(root, "allow.txt")
    with open(allow_path, "w", encoding="utf-8") as handle:
        handle.write("# selftest allowlist\nfixtures/allowlisted.py  # deliberate\n")
    try:
        fixtures = os.path.join(root, "tree", "fixtures")
        os.makedirs(fixtures)
        expects = {}
        for name, suffix, body, classes in FIXTURES:
            path = os.path.join(fixtures, name + suffix)
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(body)
            expects["fixtures/%s%s" % (name, suffix)] = classes
        rows, missing, checked = scan(
            os.path.join(root, "tree"), ["fixtures/*.py", "fixtures/*.sh"],
            load_allow(allow_path))
        check("fixtures collected", checked == len(FIXTURES) and not missing,
              "checked=%d missing=%s" % (checked, missing))
        got = {}
        for cls, rel, line, detail, is_allowed in rows:
            got.setdefault(rel, []).append("HIT-allowed" if (cls == "HIT" and is_allowed) else cls)
        for rel, expected in expects.items():
            if rel.endswith("allowlisted.py"):
                expected = ["HIT-allowed"]
            check("class %s" % rel, sorted(got.get(rel, [])) == sorted(expected),
                  "got=%s" % sorted(got.get(rel, [])))
        # exit contract: HIT fails, non-strict passes FALLBACK/UNROUTED
        only_unrouted = os.path.join(root, "tree2")
        os.makedirs(only_unrouted)
        with open(os.path.join(only_unrouted, "u.py"), "w", encoding="utf-8") as handle:
            handle.write("import tempfile\ntempfile.mkdtemp()\n")
        relaxed, _, _ = scan(only_unrouted, ["u.py"], [])
        strict, _, _ = scan(only_unrouted, ["u.py"], [])
        check("unrouted is exit 0 by default", report_silent(relaxed, False) == 0)
        check("unrouted is exit 1 under --strict", report_silent(strict, True) == 1)
        clean_dir = os.path.join(root, "tree3")
        os.makedirs(clean_dir)
        with open(os.path.join(clean_dir, "c.py"), "w", encoding="utf-8") as handle:
            handle.write("import tempfile\ntempfile.mkdtemp(dir='/fast/scratch')\n")
        clean, _, _ = scan(clean_dir, ["c.py"], [])
        check("routed tempdir is clean", report_silent(clean, True) == 0)
        # allowlist actually suppresses the failing row
        hit_rows, _, _ = scan(os.path.join(root, "tree"), ["fixtures/allowlisted.py"], [])
        allowed_rows, _, _ = scan(os.path.join(root, "tree"), ["fixtures/allowlisted.py"],
                                  load_allow(allow_path))
        check("allowlist suppresses",
              report_silent(hit_rows, False) == 1 and report_silent(allowed_rows, True) == 0)
        # hidden directories must be walked: the lane's wave machinery is under .ufo
        hidden = os.path.join(root, "tree4", ".ufo", "waves")
        os.makedirs(hidden)
        with open(os.path.join(hidden, "gen.py"), "w", encoding="utf-8") as handle:
            handle.write("import tempfile\ntempfile.mkdtemp(dir='/tmp')\n")
        hidden_rows, hidden_missing, hidden_checked = scan(
            os.path.join(root, "tree4"), ["**/*.py"], [])
        check("hidden segment walked under **",
              hidden_checked == 1 and not hidden_missing
              and [r[0] for r in hidden_rows] == ["HIT"],
              "checked=%d missing=%s" % (hidden_checked, hidden_missing))
        # the scanner itself must not route through a literal /tmp
        own, _ = scan_file(os.path.abspath(__file__), os.path.dirname(os.path.abspath(__file__)))
        check("scanner writes nothing under a literal /tmp",
              not [r for r in own if r[1] == "HIT" and "redirect" not in r[2]],
              str([r for r in own if r[1] == "HIT"][:3]))
        return 1 if failures else 0
    finally:
        shutil.rmtree(root, ignore_errors=True)


def report_silent(rows, strict):
    import contextlib
    import io

    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        return report(rows, [], len(rows), strict)


def main(argv=None):
    parser = argparse.ArgumentParser(description="literal-/tmp scratch-root scanner (read-only)")
    parser.add_argument("--root", default=os.getcwd())
    parser.add_argument("--paths", action="append", nargs="+", default=[],
                        help="one or more globs, relative to --root (repeatable)")
    parser.add_argument("--allow", default=None, help="allowlist: globs vs rel or rel:line")
    parser.add_argument("--strict", action="store_true",
                        help="also fail on FALLBACK and UNROUTED rows")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--work", default=None,
                        help="selftest scratch (default $HYAKU_SCRATCH)")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest(args.work)
    if not args.paths:
        parser.error("--paths is required (one or more globs)")
    patterns = [p for group in args.paths for p in group]
    root = os.path.abspath(args.root)
    rows, missing, checked = scan(root, patterns, load_allow(args.allow))
    return report(rows, missing, checked, args.strict)


if __name__ == "__main__":
    sys.exit(main())
