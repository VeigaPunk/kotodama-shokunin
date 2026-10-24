#!/usr/bin/env python3
"""Separability control for round claims (round 50, claim Ca).

Reads a separability manifest and reports where one unit's landed bytes depend
on another unit:

  {"schema": "kotodama-separability-manifest-v1",
   "base": "<commit>",
   "claims": [{"id": "C",
               "role": "claim" | "record",                   (optional, default "claim")
               "tree": "<commit holding C's landed bytes>" | "WORKTREE",
               "lands": ["<repo-relative path>", ...],
               "exports": ["<python regex naming identifiers C introduces>", ...],
               "acceptance": ["<argv, program first>", ...], (optional, claims only)
               "needs_git": true | false}]}                  (optional, needs acceptance)

Landed bytes of a unit are the lines of each land, as read at its tree (or from
the filesystem under --root for "WORKTREE"), that are not present in the base
version of that path. A land absent at base contributes all of its lines.
Records are never scanned as dependers; claims may depend on them.

Static leg, per ordered pair X != Y (X a claim):
  * a Y export regex matches a line of X's landed bytes (export novelty: each
    Y export must match no line of base bytes in Y's lands, else exit 2);
  * X's landed bytes name a Y land path that is absent at base (a path that
    already resolves at base is not a dependency). A path is named as a whole
    path: tools/x.py is not named by old-tools/x.py, tools/x.pyc or tools/x.py.bak.
Overlap: the same path in two units' lands is a finding, not a dependency.

Dynamic leg (only for units with acceptance): the argv runs in base with the
unit's lands overlaid (every other path at base bytes). Without needs_git this is
a git-free temporary copy; with needs_git it is `git clone --shared` of --root,
checked out at base. If the argv fails there, each other unit whose lands repair
it (base + X.lands + Y.lands passes) yields a finding X->Y; if no declared unit
repairs it, the finding is X-><base>.

Bounds (round 66, claim O): the dynamic leg is bounded by four knobs so a verdict
returns inside a round's budget:
  --timeout SECONDS   per acceptance run (unchanged semantic: a timed-out run
                      counts as a failed run, never as a hang)
  --jobs N            acceptance units evaluated in parallel (findings are
                      printed sorted, so the verdict is unchanged by N)
  --budget SECONDS    global wall-clock bound on the dynamic leg: a run not yet
                      started when the budget is exhausted is SKIPPED
  --max-runs N        per-unit cap on dynamic runs (initial plus repairs); runs
                      beyond the cap are SKIPPED
  --static-only       evaluate overlap + static legs only; the dynamic leg is
                      skipped as a whole (counts as a partial verdict)
Any skipped run produces a partial verdict: the report prints
`SEPARABILITY_PARTIAL <k> run(s) skipped` and exits 2 - a partial verdict is
honest, never silent, and never reads as a finding or as 0 findings.

Output: finding lines sorted, then `SEPARABILITY: <n> findings` (plus
`SEPARABILITY_PARTIAL <k> run(s) skipped` when bounded). Finding lines:
  SEPARABILITY_DEPENDENCY X->Y via export 'RE' matched PATH:LINE
  SEPARABILITY_DEPENDENCY X->Y via land path 'PATH' named at PATH:LINE
  SEPARABILITY_DEPENDENCY X->Y via acceptance ... and passes on base+X.lands+Y.lands
  SEPARABILITY_DEPENDENCY X-><base> via acceptance ... and no declared unit's lands repairs it
  SEPARABILITY_OVERLAP X/Y PATH

Usage:
  python3 tools/check-claim-separability.py <manifest.json> [--lane LANE] [--root ROOT]
                                            [--timeout SECONDS] [--jobs N]
                                            [--budget SECONDS] [--max-runs N]
                                            [--static-only]
  python3 tools/check-claim-separability.py --selftest

Exit codes: 0 no findings; 1 findings; 2 could not evaluate or partial verdict.
Input errors print SEPARABILITY_INPUT_ERROR on stderr. A needs_git leg that
cannot be built or run prints SEPARABILITY_UNEVALUATED on stdout and exits 2;
it never reads as 0. A partial verdict prints SEPARABILITY_PARTIAL and exits 2.

Read-only git: the lane is read through `git cat-file --batch` (one process).
The one other git invocation is `git clone --shared` from --root into a temporary
directory, and only for needs_git units. Stdlib only.
"""
import argparse
import contextlib
import dataclasses
import io
import json
import math
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
LANE_DEFAULT = os.path.abspath(os.path.join(HERE, ".."))
SCHEMA = "kotodama-separability-manifest-v1"
BASE_NAME = "<base>"
WORKTREE = "WORKTREE"
ROLES = ("claim", "record")
DEFAULT_TIMEOUT = 600.0
DEFAULT_JOBS = 1
DEFAULT_BUDGET = None     # dynamic-leg wall budget in seconds; None = unbounded
DEFAULT_MAX_RUNS = None   # per-unit dynamic run cap; None = unbounded
EXIT_OK, EXIT_DEPENDENT, EXIT_INPUT = 0, 1, 2

ID_RE = re.compile(r"[A-Za-z][A-Za-z0-9_-]*")
TREE_HEX_RE = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")
DIR_MODE = "40000"
GITLINK_MODE = "160000"
FILE_MODES = ("100644", "100755", "120000")
MANIFEST_KEYS = frozenset(("schema", "base", "claims"))
UNIT_KEYS = frozenset(("id", "tree", "lands", "exports"))
UNIT_OPTIONAL_KEYS = frozenset(("acceptance", "role", "needs_git"))
GIT_LOCATION_VARS = (
    "GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_OBJECT_DIRECTORY",
    "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_COMMON_DIR", "GIT_NAMESPACE",
)


class InputError(Exception):
    """Could not evaluate: the manifest, the lane, a commit or a path is unusable."""


class MissingObject(InputError):
    """A requested name does not resolve in the lane."""


class Unevaluated(Exception):
    """A needs_git leg could not be built or run. Never a separability verdict."""


class CannotStart(Exception):
    """An acceptance argv could not be executed."""


def _clean_env():
    """The process environment without inherited repository pointers."""
    env = dict(os.environ)
    for name in GIT_LOCATION_VARS:
        env.pop(name, None)
    return env


def _short(text, limit=160):
    return text if len(text) <= limit else text[: limit - 3] + "..."


def _lines(content):
    """Lines of CONTENT without terminators; a final newline ends the last line."""
    parts = content.split(b"\n")
    if parts[-1] == b"":
        parts.pop()
    return parts


def _text(line):
    return line.decode("utf-8", "surrogateescape")


# ---------------------------------------------------------------- lane reading


class Objects:
    """Read-only object access through one `git cat-file --batch` process."""

    def __init__(self, lane):
        self.lane = lane
        self._err = tempfile.TemporaryFile()
        try:
            self._proc = subprocess.Popen(
                ["git", "-C", lane, "cat-file", "--batch"],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=self._err,
                env=_clean_env())
        except OSError as exc:
            self._err.close()
            raise InputError("cannot run git for lane %r: %s" % (lane, exc))

    def read(self, name):
        """(oid, type, content) of object NAME. MissingObject if it does not resolve."""
        try:
            self._proc.stdin.write(name.encode("utf-8") + b"\n")
            self._proc.stdin.flush()
            header = self._proc.stdout.readline()
        except OSError:
            header = b""
        if not header:
            raise InputError("git cat-file stopped in lane %r while reading %r%s"
                             % (self.lane, name, self._stderr_suffix()))
        if header.endswith((b" missing\n", b" ambiguous\n")):
            raise MissingObject("%r is not an object in lane %r" % (name, self.lane))
        fields = header.split()
        if len(fields) != 3 or not fields[2].isdigit():
            raise InputError("unexpected cat-file header for %r: %r" % (name, header[:120]))
        size = int(fields[2])
        content = self._proc.stdout.read(size)
        if len(content) != size or self._proc.stdout.read(1) != b"\n":
            raise InputError("truncated cat-file output for %r" % name)
        return fields[0].decode("ascii"), fields[1].decode("ascii"), content

    def _stderr_suffix(self):
        self._proc.wait()
        self._err.seek(0)
        text = self._err.read().decode("utf-8", "replace").strip()
        return ": " + text if text else ""

    def close(self):
        with contextlib.suppress(OSError):
            self._proc.stdin.close()
        self._proc.stdout.read()
        self._proc.wait()
        self._err.close()


def _parse_tree(data, raw_len):
    """[(mode, name, hex_sha)] of a raw tree object; raw_len is the binary id length."""
    entries, pos = [], 0
    while pos < len(data):
        space = data.find(b" ", pos)
        nul = data.find(b"\0", space + 1) if space != -1 else -1
        end = nul + 1 + raw_len if nul != -1 else -1
        if space == -1 or nul == -1 or end > len(data):
            raise InputError("malformed tree object")
        entries.append((data[pos:space].decode("ascii", "replace"),
                        os.fsdecode(data[space + 1:nul]),
                        data[nul + 1:end].hex()))
        pos = end
    return entries


def _commit_pair(objs, rev, what):
    """(commit oid, root tree hex) of the commit that REV names; InputError otherwise."""
    try:
        oid, typ, data = objs.read(rev + "^{commit}")
    except MissingObject:
        raise InputError("%s %r does not name a commit in lane %r" % (what, rev, objs.lane))
    head = data.split(b"\n", 1)[0].decode("ascii", "replace")
    if typ != "commit" or not head.startswith("tree ") or not TREE_HEX_RE.fullmatch(head[5:]):
        raise InputError("%s %r does not name a commit" % (what, rev))
    return oid, head[5:]


def _tree_content(objs, tree_hex, what):
    _, typ, data = objs.read(tree_hex)
    if typ != "tree":
        raise InputError("%s: object %s is a %s, not a tree" % (what, tree_hex, typ))
    return data


def _base_object(objs, base_oid, rel):
    """(type, content) of the object base:REL, or None when REL is absent at base."""
    try:
        _, typ, content = objs.read("%s:%s" % (base_oid, rel))
    except MissingObject:
        return None
    return typ, content


def _walk_files(objs, root_hex, raw_len):
    """[(path, mode, blob_hex)] for every file-like entry; gitlinks are skipped."""
    found, stack = [], [("", root_hex)]
    while stack:
        prefix, tree_hex = stack.pop()
        for mode, name, sha in _parse_tree(_tree_content(objs, tree_hex, "base"), raw_len):
            rel = prefix + name
            if mode == DIR_MODE:
                stack.append((rel + "/", sha))
            elif mode in FILE_MODES:
                found.append((rel, mode, sha))
            elif mode != GITLINK_MODE:
                raise InputError("unsupported tree mode %s at %r" % (mode, rel))
    return sorted(found)


def _lookup(objs, root_hex, raw_len, rel, uid):
    """(mode, content) of the regular file or symlink REL under the tree ROOT_HEX."""
    parts = rel.split("/")
    cur = root_hex
    for depth, part in enumerate(parts):
        hit = None
        for mode, name, sha in _parse_tree(_tree_content(objs, cur, "unit %s" % uid), raw_len):
            if name == part:
                hit = (mode, sha)
                break
        if hit is None:
            raise InputError("unit %s lands %r, which is absent at its tree" % (uid, rel))
        mode, sha = hit
        if depth < len(parts) - 1:
            if mode != DIR_MODE:
                raise InputError("unit %s lands %r, but %r is not a directory at its tree"
                                 % (uid, rel, "/".join(parts[: depth + 1])))
            cur = sha
            continue
        if mode not in FILE_MODES:
            raise InputError("unit %s lands %r, which is not a regular file or symlink (mode %s)"
                             % (uid, rel, mode))
        _, typ, content = objs.read(sha)
        if typ != "blob":
            raise InputError("unit %s lands %r, which is a %s, not a blob" % (uid, rel, typ))
        return mode, content


# ------------------------------------------------------------ manifest parsing


def _object_no_duplicates(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise InputError("manifest repeats JSON key %r" % key)
        obj[key] = value
    return obj


def _reject_constant(token):
    raise InputError("manifest uses non-standard JSON constant %s" % token)


def _check_keys(obj, where, required, optional=frozenset()):
    missing = sorted(required - set(obj))
    if missing:
        raise InputError("%s is missing %s" % (where, ", ".join(missing)))
    unknown = sorted(set(obj) - required - optional)
    if unknown:
        raise InputError("%s has unknown key(s) %s; a misspelled key would be silently ignored"
                         % (where, ", ".join(unknown)))


def _rev(value, where):
    if (not isinstance(value, str) or not value or value.startswith("-")
            or any(ch.isspace() or ord(ch) < 0x20 for ch in value)):
        raise InputError("%s must be a commit name without spaces or control characters, "
                         "not starting with '-': %r" % (where, value))
    return value


def _repo_path(value, where):
    if not isinstance(value, str) or not value:
        raise InputError("%s must be a non-empty repo-relative path" % where)
    if value.startswith("/") or any(ord(ch) < 0x20 for ch in value):
        raise InputError("%s is not a repo-relative path: %r" % (where, value))
    parts = value.split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise InputError("%s is not canonical (empty, '.' or '..' component): %r" % (where, value))
    if ".git" in parts:
        raise InputError("%s names .git metadata: %r" % (where, value))
    return value


def _export(value, where):
    if not isinstance(value, str) or not value:
        raise InputError("%s must be a non-empty regex string" % where)
    try:
        pattern = re.compile(value)
    except re.error as exc:
        raise InputError("%s is not a valid regex (%s): %r" % (where, exc, value))
    if pattern.search("") is not None:
        raise InputError("%s matches the empty string and would name every unit: %r"
                         % (where, value))
    return pattern


def _argv(value, where):
    if (not isinstance(value, list) or not value
            or not all(isinstance(item, str) and "\0" not in item for item in value)
            or value[0] == ""):
        raise InputError("%s must be a non-empty argv list of strings (program first)" % where)
    return list(value)


def _nests(a, b):
    return a == b or a.startswith(b + "/") or b.startswith(a + "/")


@dataclasses.dataclass
class Unit:
    uid: str
    role: str
    tree: str            # a commit name, or WORKTREE
    lands: list
    export_src: list
    exports: list
    acceptance: object   # argv list, or None
    needs_git: bool
    landed: dict = dataclasses.field(default_factory=dict)       # rel -> (mode, bytes)
    added: dict = dataclasses.field(default_factory=dict)        # rel -> [(line, text)]
    base_absent: dict = dataclasses.field(default_factory=dict)  # rel -> bool
    base_text: dict = dataclasses.field(default_factory=dict)    # rel -> [text]

    def overlays(self):
        return [(rel, mode, content) for rel, (mode, content) in self.landed.items()]

    def name_paths(self):
        """Land paths absent at base: the only land paths whose names count."""
        return [rel for rel in self.lands if self.base_absent[rel]]


def _parse_manifest(doc):
    if not isinstance(doc, dict):
        raise InputError("manifest must be a JSON object")
    _check_keys(doc, "manifest", MANIFEST_KEYS)
    if doc["schema"] != SCHEMA:
        raise InputError("manifest schema must be %r, got %r" % (SCHEMA, doc["schema"]))
    base = _rev(doc["base"], "base")
    raw_units = doc["claims"]
    if not isinstance(raw_units, list) or not raw_units:
        raise InputError("claims must be a non-empty list")
    units = []
    for index, raw in enumerate(raw_units):
        where = "claims[%d]" % index
        if not isinstance(raw, dict):
            raise InputError("%s must be a JSON object" % where)
        _check_keys(raw, where, UNIT_KEYS, UNIT_OPTIONAL_KEYS)
        uid = raw["id"]
        if not isinstance(uid, str) or not ID_RE.fullmatch(uid):
            raise InputError("%s.id must match [A-Za-z][A-Za-z0-9_-]*: %r" % (where, uid))
        if any(unit.uid == uid for unit in units):
            raise InputError("claim id %r is declared twice" % uid)
        role = raw.get("role", "claim")
        if role not in ROLES:
            raise InputError("%s.role must be 'claim' or 'record', got %r" % (where, role))
        tree = raw["tree"]
        tree = WORKTREE if tree == WORKTREE else _rev(tree, "%s.tree" % where)
        lands = raw["lands"]
        if not isinstance(lands, list) or not lands:
            raise InputError("%s.lands must be a non-empty list of paths" % where)
        lands = [_repo_path(p, "%s.lands[%d]" % (where, i)) for i, p in enumerate(lands)]
        if len(set(lands)) != len(lands):
            raise InputError("%s.lands repeats a path" % where)
        export_src = raw["exports"]
        if not isinstance(export_src, list):
            raise InputError("%s.exports must be a list of regex strings" % where)
        exports = [_export(src, "%s.exports[%d]" % (where, i))
                   for i, src in enumerate(export_src)]
        acceptance = None
        if "acceptance" in raw:
            acceptance = _argv(raw["acceptance"], "%s.acceptance" % where)
        needs_git = raw.get("needs_git", False)
        if not isinstance(needs_git, bool):
            raise InputError("%s.needs_git must be true or false" % where)
        if role == "record" and acceptance is not None:
            raise InputError("%s is a record: records carry no acceptance and are never dependers"
                             % where)
        if needs_git and acceptance is None:
            raise InputError("%s.needs_git requires an acceptance argv" % where)
        units.append(Unit(uid, role, tree, lands, list(export_src), exports, acceptance,
                          needs_git))
    owned = [(unit.uid, rel) for unit in units for rel in unit.lands]
    for i, (ui, pi) in enumerate(owned):
        for uj, pj in owned[i + 1:]:
            if pi != pj and _nests(pi, pj):
                raise InputError("lands conflict: %s lands %r and %s lands %r; no path may sit "
                                 "under another" % (ui, pi, uj, pj))
    return base, units


def _load_manifest(path):
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except OSError as exc:
        raise InputError("cannot read manifest %r: %s" % (path, exc.strerror or exc))
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise InputError("manifest %r is not UTF-8: %s" % (path, exc))
    try:
        doc = json.loads(text, object_pairs_hook=_object_no_duplicates,
                         parse_constant=_reject_constant)
    except ValueError as exc:
        raise InputError("manifest %r is not valid JSON: %s" % (path, exc))
    return _parse_manifest(doc)


# ------------------------------------------------------------- unit contents


def _read_worktree(root, rel, uid):
    """(mode, content) of REL on the filesystem under ROOT (never followed through git)."""
    path = os.path.join(root, *rel.split("/"))
    try:
        info = os.lstat(path)
    except OSError:
        raise InputError("unit %s lands %r, which is absent from the worktree under %r"
                         % (uid, rel, root))
    if stat.S_ISLNK(info.st_mode):
        return "120000", os.fsencode(os.readlink(path))
    if not stat.S_ISREG(info.st_mode):
        raise InputError("unit %s lands %r, which is not a regular file or symlink in the worktree"
                         % (uid, rel))
    with open(path, "rb") as fh:
        content = fh.read()
    return ("100755" if info.st_mode & 0o111 else "100644"), content


def _load_units(objs, base_oid, raw_len, units, root):
    """Fill each unit's landed bytes, added lines and base facts."""
    for unit in units:
        if unit.tree == WORKTREE:
            for rel in unit.lands:
                unit.landed[rel] = _read_worktree(root, rel, unit.uid)
        else:
            _, root_hex = _commit_pair(objs, unit.tree, "unit %s tree" % unit.uid)
            for rel in unit.lands:
                unit.landed[rel] = _lookup(objs, root_hex, raw_len, rel, unit.uid)
        for rel in unit.lands:
            _, content = unit.landed[rel]
            base = _base_object(objs, base_oid, rel)
            base_lines = _lines(base[1]) if base is not None and base[0] == "blob" else []
            seen = set(base_lines)
            unit.base_absent[rel] = base is None
            unit.base_text[rel] = [_text(line) for line in base_lines]
            unit.added[rel] = [(number, _text(line))
                               for number, line in enumerate(_lines(content), 1)
                               if line not in seen]


def _check_novelty(units):
    """Each export must match no line of base bytes in its own unit's lands."""
    for unit in units:
        for src, pattern in zip(unit.export_src, unit.exports):
            for rel in unit.lands:
                for text in unit.base_text[rel]:
                    if pattern.search(text) is not None:
                        raise InputError("unit %s export %r is not novel: it matches base bytes "
                                         "of %r" % (unit.uid, src, rel))


# ----------------------------------------------------- counterfactual trees


def _place(root, rel, mode, content):
    """Write repo path REL under ROOT. Never writes through a symlink."""
    parts = rel.split("/")
    cur = root
    for part in parts[:-1]:
        cur = os.path.join(cur, part)
        if os.path.islink(cur) or (os.path.lexists(cur) and not os.path.isdir(cur)):
            raise InputError("cannot place %r: an ancestor is not a plain directory in base" % rel)
        os.makedirs(cur, exist_ok=True)
    dest = os.path.join(cur, parts[-1])
    if os.path.isdir(dest) and not os.path.islink(dest):
        raise InputError("cannot place %r: base has a directory at that path" % rel)
    if os.path.lexists(dest):
        os.unlink(dest)
    if mode == "120000":
        os.symlink(os.fsdecode(content), dest)
    else:
        with open(dest, "wb") as fh:
            fh.write(content)
        os.chmod(dest, 0o755 if mode == "100755" else 0o644)


def _materialize(objs, base_tree, raw_len, root):
    for rel, mode, sha in _walk_files(objs, base_tree, raw_len):
        _, typ, content = objs.read(sha)
        if typ != "blob":
            raise InputError("base entry %r is a %s, not a blob" % (rel, typ))
        _place(root, rel, mode, content)


def _run_acceptance(argv, cwd, timeout):
    """(passed, why) for one run of ARGV in CWD. CannotStart if it cannot execute."""
    try:
        proc = subprocess.run(argv, cwd=cwd, env=_clean_env(), stdin=subprocess.DEVNULL,
                              capture_output=True, timeout=timeout, check=False)
    except subprocess.TimeoutExpired:
        return False, "timeout after %gs" % timeout
    except OSError as exc:
        raise CannotStart("acceptance program %r cannot start: %s" % (argv[0], exc))
    if proc.returncode == 0:
        return True, "rc=0"
    why = "rc=%d" % proc.returncode
    tail = proc.stderr.decode("utf-8", "replace").strip().splitlines()
    if tail:
        why += ", stderr %r" % _short(tail[-1], 120)
    return False, why


def _counterfactual(base_root, overlays, argv, timeout):
    """Run ARGV in a fresh git-free copy of base plus OVERLAYS: (passed, why)."""
    scratch = tempfile.mkdtemp(prefix="claim-separability-run-")
    try:
        root = os.path.join(scratch, "tree")
        shutil.copytree(base_root, root, symlinks=True)
        for rel, mode, content in overlays:
            _place(root, rel, mode, content)
        try:
            return _run_acceptance(argv, root, timeout)
        except CannotStart as exc:
            raise InputError(str(exc))
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


def _git_run(args):
    """Run git with ARGS; Unevaluated when git is missing or the command fails."""
    try:
        proc = subprocess.run(["git", *args], env=_clean_env(), stdin=subprocess.DEVNULL,
                              capture_output=True, check=False)
    except OSError as exc:
        raise Unevaluated("cannot run git: %s" % exc)
    if proc.returncode != 0:
        tail = proc.stderr.decode("utf-8", "replace").strip().splitlines()
        detail = ": " + _short(tail[-1], 160) if tail else ""
        raise Unevaluated("git %s failed (rc=%d)%s" % (args[0], proc.returncode, detail))


def _git_counterfactual(root, base_oid, overlays, argv, timeout):
    """Run ARGV in `git clone --shared` of ROOT checked out at base plus OVERLAYS."""
    scratch = tempfile.mkdtemp(prefix="claim-separability-clone-")
    try:
        work = os.path.join(scratch, "work")
        _git_run(["clone", "--shared", "-q", "--no-checkout", os.path.abspath(root), work])
        _git_run(["-C", work, "checkout", "-q", "--detach", base_oid])
        for rel, mode, content in overlays:
            _place(work, rel, mode, content)
        try:
            return _run_acceptance(argv, work, timeout)
        except CannotStart as exc:
            raise Unevaluated(str(exc))
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


# --------------------------------------------------------------- the legs


def _name_re(rel):
    """Matches the repo path REL as a whole path, never inside a longer name."""
    return re.compile(r"(?<![\w.\-])" + re.escape(rel) + r"(?![\w\-]|\.\w)")


def _first_line_hit(unit, search):
    """'path:line' of the first added line of UNIT matching SEARCH, or None."""
    for rel, lines in unit.added.items():
        for number, text in lines:
            if search(text) is not None:
                return "%s:%d" % (rel, number)
    return None


def _static_findings(units):
    findings = []
    for x in units:
        if x.role == "record":
            continue
        for y in units:
            if y is x:
                continue
            for src, pattern in zip(y.export_src, y.exports):
                hit = _first_line_hit(x, pattern.search)
                if hit is not None:
                    findings.append("SEPARABILITY_DEPENDENCY %s->%s via export %r matched %s"
                                    % (x.uid, y.uid, src, hit))
            for rel in y.name_paths():
                hit = _first_line_hit(x, _name_re(rel).search)
                if hit is not None:
                    findings.append("SEPARABILITY_DEPENDENCY %s->%s via land path %r named at %s"
                                    % (x.uid, y.uid, rel, hit))
    return findings


def _overlap_findings(units):
    findings = []
    for i, x in enumerate(units):
        for y in units[i + 1:]:
            for rel in x.lands:
                if rel in y.lands:
                    findings.append("SEPARABILITY_OVERLAP %s/%s %s" % (x.uid, y.uid, rel))
    return findings


class _Budget:
    """Dynamic-leg bounds shared across units. A run is skipped (never
    silently dropped) when the wall budget is exhausted or the unit's own run
    cap is reached; skipped runs make the verdict partial and exit 2.

    Thread-safe for the single-writer pattern used here: `take()` is the only
    mutator and is called from one unit task at a time per `per_unit` key;
    `expired()` is read-only. The run counter is guarded by a lock because
    several unit tasks may finish simultaneously.
    """

    def __init__(self, budget, max_runs):
        self._deadline = None if budget is None else time.monotonic() + budget
        self._max_runs = max_runs
        self._lock = threading.Lock()
        self._per_unit = {}
        self.runs = 0
        self.skipped = 0

    def expired(self):
        return (self._deadline is not None
                and time.monotonic() >= self._deadline)

    def take(self, uid):
        """True when one more dynamic run may start for unit UID."""
        with self._lock:
            if self.expired():
                self.skipped += 1
                return False
            used = self._per_unit.get(uid, 0)
            if self._max_runs is not None and used >= self._max_runs:
                self.skipped += 1
                return False
            self._per_unit[uid] = used + 1
            self.runs += 1
            return True


def _acceptance_findings(unit, units, run, bound):
    """(findings, unresolved) for one unit's acceptance. run(overlays) ->
    (passed, why); bound.take(uid) meters the initial run and each repair
    attempt. A skipped repair attempt is an unresolved question, never a
    `<base>` conclusion."""
    if not bound.take(unit.uid):
        return [], ["SEPARABILITY_UNRESOLVED %s acceptance never ran" % unit.uid]
    passed, why = run(unit.overlays())
    if passed:
        return [], []
    repairs = []
    unevaluated = []
    for other in units:
        if other is unit:
            continue
        if not bound.take(unit.uid):
            unevaluated.append(other.uid)
            continue
        repaired, _ = run(unit.overlays() + other.overlays())
        if repaired:
            repairs.append(other.uid)
    head = "via acceptance %s fails on base+%s.lands (%s)" % (
        _short(repr(unit.acceptance)), unit.uid, why)
    findings = ["SEPARABILITY_DEPENDENCY %s->%s %s and passes on base+%s.lands+%s.lands"
                % (unit.uid, other_id, head, unit.uid, other_id)
                for other_id in repairs]
    if not repairs and not unevaluated:
        findings = ["SEPARABILITY_DEPENDENCY %s-><base> %s and no declared unit's lands repairs it"
                    % (unit.uid, head)]
    unresolved = ["SEPARABILITY_UNRESOLVED %s->%s %s: repair attempt skipped" % (
        unit.uid, other_id, head) for other_id in unevaluated]
    return findings, unresolved


def evaluate(manifest_path, lane, root, timeout, jobs=DEFAULT_JOBS,
             budget=DEFAULT_BUDGET, max_runs=DEFAULT_MAX_RUNS,
             static_only=False):
    """(findings, unresolved, units, runs, skipped) for the manifest; raises
    InputError or Unevaluated. The dynamic leg honours TIMEOUT per run, BUDGET
    as a global wall bound, MAX_RUNS as a per-unit cap, and STATIC_ONLY to
    skip it entirely; every skipped run is counted in `skipped` and named in
    `unresolved` (an unresolved run never reads as a finding)."""
    base, units = _load_manifest(manifest_path)
    objs = Objects(lane)
    try:
        base_oid, base_tree = _commit_pair(objs, base, "base")
        raw_len = len(base_tree) // 2
        _load_units(objs, base_oid, raw_len, units, root)
        _check_novelty(units)
        findings = _overlap_findings(units) + _static_findings(units)
        unresolved = []
        bound = _Budget(budget, max_runs)
        if static_only:
            dyn_units = [u for u in units if u.acceptance is not None]
            unresolved = ["SEPARABILITY_UNRESOLVED %s acceptance skipped (static-only)"
                          % u.uid for u in dyn_units]
            return findings, unresolved, units, 0, len(dyn_units)
        git_free = [u for u in units if u.acceptance is not None and not u.needs_git]
        git_units = [u for u in units if u.acceptance is not None and u.needs_git]
        tasks = []          # (unit, closure) in manifest order
        if git_free:
            scratch = tempfile.mkdtemp(prefix="claim-separability-base-")
            try:
                base_root = os.path.join(scratch, "base")
                os.mkdir(base_root)
                _materialize(objs, base_tree, raw_len, base_root)
                for unit in git_free:
                    tasks.append(
                        (unit, lambda u=unit: _acceptance_findings(
                            u, units,
                            lambda overlays: _counterfactual(
                                base_root, overlays, u.acceptance, timeout),
                            bound)))
                results = _run_unit_tasks(tasks, jobs)
            finally:
                shutil.rmtree(scratch, ignore_errors=True)
        else:
            results = []
        tasks = [
            (unit, lambda u=unit: _acceptance_findings(
                u, units,
                lambda overlays: _git_counterfactual(
                    root, base_oid, overlays, u.acceptance, timeout),
                bound))
            for unit in git_units]
        results += _run_unit_tasks(tasks, jobs)
        for found, unres in results:
            findings += found
            unresolved += unres
    finally:
        objs.close()
    return findings, unresolved, units, bound.runs, bound.skipped


def _run_unit_tasks(tasks, jobs):
    """Return each task's findings in submission order; tasks run in manifest
    order under --jobs 1, and in parallel (order preserved in the result list)
    under --jobs N."""
    if not tasks:
        return []
    if jobs <= 1 or len(tasks) == 1:
        return [task() for _, task in tasks]
    with ThreadPoolExecutor(max_workers=min(jobs, len(tasks))) as pool:
        return list(pool.map(lambda item: item[1](), tasks))


def report(manifest_path, lane, root, timeout, jobs=DEFAULT_JOBS,
           budget=DEFAULT_BUDGET, max_runs=DEFAULT_MAX_RUNS, static_only=False):
    findings, unresolved, units, runs, skipped = evaluate(
        manifest_path, lane, root, timeout,
        jobs=jobs, budget=budget, max_runs=max_runs,
        static_only=static_only)
    lines = sorted(findings)
    for line in lines:
        print(line)
    for line in sorted(unresolved):
        print(line)
    print("SEPARABILITY: %d findings" % len(lines))
    partial = skipped > 0 or bool(unresolved)
    if partial:
        print("SEPARABILITY_PARTIAL %d run(s) skipped%s" % (
            skipped, " (static-only)" if static_only else ""))
    pairs = len(units) * (len(units) - 1)
    print("SEPARABILITY_NOTE units=%d ordered_pairs=%d acceptance_runs=%d skipped=%d"
          % (len(units), pairs, runs, skipped), file=sys.stderr)
    if partial:
        return EXIT_INPUT
    return EXIT_DEPENDENT if lines else EXIT_OK


# --------------------------------------------------------------- selftest


def _git_fixture(cwd, *args):
    """Run git inside a temporary repository the selftest creates."""
    env = _clean_env()
    env.update({
        "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_AUTHOR_NAME": "selftest", "GIT_AUTHOR_EMAIL": "selftest@invalid",
        "GIT_COMMITTER_NAME": "selftest", "GIT_COMMITTER_EMAIL": "selftest@invalid",
    })
    proc = subprocess.run(["git", "-c", "commit.gpgsign=false", *args], cwd=cwd, env=env,
                          capture_output=True, text=True, check=True)
    return proc.stdout.strip()


def _write_files(root, files):
    for rel, content in files.items():
        dest = os.path.join(root, *rel.split("/"))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as fh:
            fh.write(content)


def _make_lane(root, base_files, claim_files):
    """Temporary repo: a base commit, then one commit per unit holding base plus its files."""
    lane = os.path.join(root, "lane")
    os.makedirs(lane)
    _git_fixture(lane, "init", "-q")
    _write_files(lane, base_files)
    _git_fixture(lane, "add", "-A")
    _git_fixture(lane, "commit", "-q", "--allow-empty", "-m", "base")
    base = _git_fixture(lane, "rev-parse", "HEAD")
    trees = {}
    for cid, files in claim_files.items():
        _git_fixture(lane, "checkout", "-q", "--detach", base)
        _git_fixture(lane, "clean", "-fdxq")
        _write_files(lane, files)
        _git_fixture(lane, "add", "-A")
        _git_fixture(lane, "commit", "-q", "--allow-empty", "-m", cid)
        trees[cid] = _git_fixture(lane, "rev-parse", "HEAD")
    return lane, base, trees


def _invoke(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        rc = main(argv)
    return rc, out.getvalue(), err.getvalue()


def selftest():
    py = sys.executable  # acceptance programs run the interpreter that runs this selftest
    c_path, s_path = "corpus/knowledge/c.md", "corpus/SOURCES.md"
    s_range = r"\bS0(3[1-9]|4[0-3])\b"
    base_files = {"README.md": "index\n", "tools/base.txt": "base\n"}
    results = []

    def check(name, ok, detail=""):
        results.append((name, bool(ok), detail))

    def findings_of(out):
        return [line for line in out.splitlines()
                if line.startswith("SEPARABILITY_") and not line.startswith("SEPARABILITY: ")]

    with tempfile.TemporaryDirectory(prefix="claim-separability-selftest-") as tmp:
        counter = [0]

        def fresh():
            counter[0] += 1
            path = os.path.join(tmp, "case-%02d" % counter[0])
            os.makedirs(path)
            return path

        def verdict(name, argv, expect, out_must=(), out_must_not=(), err_must=(),
                    out_check=None):
            rc, out, err = _invoke(argv)
            ok = (rc == expect
                  and all(s in out for s in out_must)
                  and not any(s in out for s in out_must_not)
                  and all(s in err for s in err_must)
                  and "internal fault" not in err
                  and (expect != EXIT_INPUT or "SEPARABILITY_INPUT_ERROR" in err
                       or "SEPARABILITY_UNEVALUATED" in out
                       or "SEPARABILITY_PARTIAL" in out)
                  and (out_check is None or out_check(out)))
            check(name, ok, "rc=%d want %d; stdout=%r stderr=%r" % (rc, expect, out, err))

        def unit_doc(spec, trees):
            doc = dict(spec)
            if doc.get("tree") != WORKTREE:
                doc["tree"] = trees[spec["id"]]
            return doc

        def scenario(name, claim_files, units, expect, base=base_files, worktree=None,
                     root=None, timeout=None, extra=None, **expectations):
            root_dir = fresh()
            lane, base_sha, trees = _make_lane(root_dir, base, claim_files)
            for rel, content in (worktree or {}).items():
                _write_files(lane, {rel: content})
            doc = {"schema": SCHEMA, "base": base_sha,
                   "claims": [unit_doc(spec, trees) for spec in units]}
            manifest = os.path.join(root_dir, "manifest.json")
            with open(manifest, "w", encoding="utf-8") as fh:
                json.dump(doc, fh)
            argv = [manifest, "--lane", lane]
            if root is not None:
                argv += ["--root", root]
            if timeout is not None:
                argv += ["--timeout", str(timeout)]
            if extra:
                argv += list(extra)
            verdict(name, argv, expect, **expectations)

        # ---- positive controls: no finding, exit 0
        scenario("positive: disjoint units are separable",
                 {"C": {c_path: "pastoral entry without registry ids\n"},
                  "S": {s_path: "| S998 | a row outside the exported range |\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCPAST\b"]},
                  {"id": "S", "lands": [s_path], "exports": [s_range]}],
                 EXIT_OK, out_must=["SEPARABILITY: 0 findings"],
                 out_must_not=["SEPARABILITY_DEPENDENCY"])

        scenario("positive: self-citation and empty exports are not dependencies",
                 {"C": {c_path: "defines S031 itself\n"}, "S": {s_path: "no identifiers\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bS031\b"]},
                  {"id": "S", "lands": [s_path], "exports": []}],
                 EXIT_OK, out_must=["SEPARABILITY: 0 findings"])

        scenario("positive: a path that only shares a prefix or suffix is not named",
                 {"C": {c_path: "see old-tools/check.py, subtools/check.py and tools/check.pyc\n"},
                  "S": {"tools/check.py": "print('s')\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCX\b"]},
                  {"id": "S", "lands": ["tools/check.py"], "exports": [r"\bSX\b"]}],
                 EXIT_OK, out_must=["SEPARABILITY: 0 findings"])

        scenario("positive: citations already in base are not claim bytes",
                 {"C": {c_path: "no citation here\n"}, "S": {s_path: "| S031 | row |\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [s_path], "exports": [s_range]}],
                 EXIT_OK, base={**base_files, "README.md": "index cites S031 already\n"},
                 out_must=["SEPARABILITY: 0 findings"])

        scenario("positive: a base-existing path mention is not a dependency",
                 {"S": {s_path: "| S001 | base row |\n| S998 | new row |\n"},
                  "C": {c_path: "see corpus/SOURCES.md for the rows\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [s_path], "exports": [s_range]}],
                 EXIT_OK, base={**base_files, s_path: "| S001 | base row |\n"},
                 out_must=["SEPARABILITY: 0 findings"])

        scenario("positive: only added lines are scanned",
                 {"C": {c_path: "base cites S031 already\nC adds an unrelated line\n"},
                  "S": {s_path: "| S998 | new row |\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [s_path], "exports": [s_range]}],
                 EXIT_OK, base={**base_files, c_path: "base cites S031 already\n"},
                 out_must=["SEPARABILITY: 0 findings"])

        scenario("positive: a record unit is never scanned as a depender",
                 {"R": {"LOG.md": "| C: cites CQ and S031 |\n"},
                  "C": {c_path: "x\n"}, "S": {s_path: "s\n"}},
                 [{"id": "R", "role": "record", "lands": ["LOG.md"],
                   "exports": [r"\bRLOG-\d+\b"]},
                  {"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [s_path], "exports": [s_range]}],
                 EXIT_OK, out_must=["SEPARABILITY: 0 findings"])

        scenario("positive: acceptance passes on base plus the unit's own lands",
                 {"C": {c_path: "c\n"}, "S": {s_path: "s\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCX\b"],
                   "acceptance": [py, "-c", "import os, sys; sys.exit(0 if "
                                  "os.path.isfile('README.md') and os.path.isfile('%s') "
                                  "else 1)" % c_path]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSX\b"]}],
                 EXIT_OK, out_must=["SEPARABILITY: 0 findings"],
                 err_must=["acceptance_runs=1"])

        scenario("positive: the counterfactual leaves other units at base bytes",
                 {"C": {c_path: "c\n"}, "S": {s_path: "s\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCX\b"],
                   "acceptance": [py, "-c", "import os, sys; sys.exit(1 if "
                                  "os.path.exists('%s') else 0)" % s_path]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSX\b"]}],
                 EXIT_OK, out_must=["SEPARABILITY: 0 findings"],
                 err_must=["acceptance_runs=1"])

        scenario("positive: a needs_git acceptance runs in a clone checked out at base",
                 {"C": {c_path: "c\n"}, "S": {s_path: "s\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCX\b"], "needs_git": True,
                   "acceptance": [py, "-c", "import os, sys; sys.exit(0 if "
                                  "os.path.isfile('README.md') and os.path.isfile('%s') "
                                  "and os.path.isdir('.git') else 1)" % c_path]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSX\b"]}],
                 EXIT_OK, out_must=["SEPARABILITY: 0 findings"],
                 err_must=["acceptance_runs=1"])

        scenario("positive: a WORKTREE unit reads its lands from --root",
                 {"S": {s_path: "s\n"}},
                 [{"id": "C", "tree": WORKTREE, "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [s_path], "exports": [s_range]}],
                 EXIT_OK, worktree={c_path: "no citation\n"},
                 out_must=["SEPARABILITY: 0 findings"])

        # ---- negative controls: findings, exit 1
        scenario("negative: C cites an identifier S exports (round-49 shape)",
                 {"C": {c_path: "rows cited: S031 and S040\n"},
                  "S": {s_path: "| S031 | row |\n| S040 | row |\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [s_path], "exports": [s_range]}],
                 EXIT_DEPENDENT, out_must=["SEPARABILITY_DEPENDENCY C->S via export",
                                           "SEPARABILITY: 1 findings"],
                 out_must_not=["SEPARABILITY_DEPENDENCY S->C"])

        scenario("negative: an inline-URL-only citation of another unit's export is a dependency",
                 {"S": {s_path: "| S998 | row |\n"},
                  "C": {c_path: "see https://example.org/sources/S031 for the row\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [s_path], "exports": [s_range]}],
                 EXIT_DEPENDENT, out_must=["SEPARABILITY_DEPENDENCY C->S via export"],
                 out_must_not=["SEPARABILITY_DEPENDENCY S->C"])

        scenario("negative: a back-reference to a unit's new file is a dependency",
                 {"C": {c_path: "x\n"}, "S": {s_path: "used-by: corpus/knowledge/c.md\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [s_path], "exports": [s_range]}],
                 EXIT_DEPENDENT,
                 out_must=["SEPARABILITY_DEPENDENCY S->C via land path 'corpus/knowledge/c.md'"],
                 out_must_not=["SEPARABILITY_DEPENDENCY C->S"])

        scenario("negative: C names a land path that S lands, absent at base",
                 {"C": {c_path: "see corpus/SOURCES.md for the rows\n"},
                  "S": {s_path: "| S998 | row |\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSZ\b"]}],
                 EXIT_DEPENDENT,
                 out_must=["SEPARABILITY_DEPENDENCY C->S via land path 'corpus/SOURCES.md'"])

        scenario("negative: acceptance fails only without S's lands",
                 {"C": {c_path: "no reference\n"}, "S": {s_path: "rows\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"],
                   "acceptance": [py, "-c", "import os, sys; sys.exit(0 if "
                                  "os.path.isfile('%s') else 1)" % s_path]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSZ\b"]}],
                 EXIT_DEPENDENT, out_must=["SEPARABILITY_DEPENDENCY C->S via acceptance"],
                 out_must_not=["SEPARABILITY_DEPENDENCY C-><base>", "SEPARABILITY_DEPENDENCY S->C"],
                 err_must=["acceptance_runs=2"])

        scenario("negative: acceptance that no declared unit repairs names <base>",
                 {"C": {c_path: "x\n"}, "S": {s_path: "y\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"],
                   "acceptance": [py, "-c", "import sys; sys.exit(3)"]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSZ\b"]}],
                 EXIT_DEPENDENT, out_must=["SEPARABILITY_DEPENDENCY C-><base> via acceptance"],
                 out_must_not=["SEPARABILITY_DEPENDENCY C->S"])

        scenario("negative: acceptance is attributed to the one unit that repairs it",
                 {"C": {c_path: "x\n"}, "S": {s_path: "y\n"}, "T": {"tools/t.txt": "t\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"],
                   "acceptance": [py, "-c", "import os, sys; sys.exit(0 if "
                                  "os.path.isfile('tools/t.txt') else 1)"]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSZ\b"]},
                  {"id": "T", "lands": ["tools/t.txt"], "exports": [r"\bTZ\b"]}],
                 EXIT_DEPENDENT, out_must=["SEPARABILITY_DEPENDENCY C->T via acceptance"],
                 out_must_not=["SEPARABILITY_DEPENDENCY C->S", "SEPARABILITY_DEPENDENCY C-><base>"])

        scenario("negative: an acceptance run that times out is a failure",
                 {"C": {c_path: "x\n"}, "S": {s_path: "y\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"],
                   "acceptance": [py, "-c", "import time; time.sleep(30)"]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSZ\b"]}],
                 EXIT_DEPENDENT,
                 out_must=["SEPARABILITY_DEPENDENCY C-><base> via acceptance", "timeout after 1s"],
                 timeout=1)

        scenario("negative: a needs_git acceptance is attributed inside its clone",
                 {"C": {c_path: "c\n"}, "S": {s_path: "s\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"], "needs_git": True,
                   "acceptance": [py, "-c", "import os, sys; sys.exit(0 if "
                                  "os.path.isfile('%s') else 1)" % s_path]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSZ\b"]}],
                 EXIT_DEPENDENT, out_must=["SEPARABILITY_DEPENDENCY C->S via acceptance"],
                 err_must=["acceptance_runs=2"])

        scenario("negative: dependency direction is ordered (S cites C, C cites nothing)",
                 {"C": {c_path: "no citation\n"}, "S": {s_path: "| S998 | cites CQ |\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [s_path], "exports": [s_range]}],
                 EXIT_DEPENDENT, out_must=["SEPARABILITY_DEPENDENCY S->C via export"],
                 out_must_not=["SEPARABILITY_DEPENDENCY C->S"])

        scenario("negative: a claim citing a record's export is a finding",
                 {"R": {"LOG.md": "RLOG-7 entry\n"}, "C": {c_path: "cites RLOG-7\n"}},
                 [{"id": "R", "role": "record", "lands": ["LOG.md"],
                   "exports": [r"\bRLOG-\d+\b"]},
                  {"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]}],
                 EXIT_DEPENDENT, out_must=["SEPARABILITY_DEPENDENCY C->R via export"],
                 out_must_not=["SEPARABILITY_DEPENDENCY R->C"])

        scenario("negative: a claim naming a record's new path is a finding",
                 {"R": {"LOG-round-50.md": "entry\n"},
                  "C": {c_path: "see LOG-round-50.md for the entry\n"}},
                 [{"id": "R", "role": "record", "lands": ["LOG-round-50.md"],
                   "exports": [r"\bRLOG-\d+\b"]},
                  {"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]}],
                 EXIT_DEPENDENT,
                 out_must=["SEPARABILITY_DEPENDENCY C->R via land path 'LOG-round-50.md'"])

        scenario("negative: one path landed by two units is an overlap finding",
                 {"C": {c_path: "x\n"}, "S": {c_path: "y\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [c_path], "exports": [r"\bSZ\b"]}],
                 EXIT_DEPENDENT, out_must=["SEPARABILITY: 1 findings"],
                 out_check=lambda out: findings_of(out) == ["SEPARABILITY_OVERLAP C/S %s" % c_path])

        scenario("negative: findings are printed sorted, then the summary",
                 {"C": {c_path: "rows cited: S031\n"},
                  "S": {s_path: "used-by: corpus/knowledge/c.md\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [s_path], "exports": [s_range]}],
                 EXIT_DEPENDENT, out_must=["SEPARABILITY: 2 findings"],
                 out_check=lambda out: (len(findings_of(out)) == 2
                                        and findings_of(out) == sorted(findings_of(out))))

        scenario("negative: a WORKTREE unit's uncommitted bytes are scanned",
                 {"S": {s_path: "s\n"}},
                 [{"id": "C", "tree": WORKTREE, "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [s_path], "exports": [s_range]}],
                 EXIT_DEPENDENT, worktree={c_path: "cites S031 here\n"},
                 out_must=["SEPARABILITY_DEPENDENCY C->S via export"])

        # ---- bounded verdict controls (round 66, claim O): the dynamic leg is
        # metered by --budget/--max-runs/--jobs/--static-only; skipped runs are
        # partial (exit 2), never silent and never a fabricated <base> finding.
        scenario("bound: --static-only skips the dynamic leg and exits 2",
                 {"C": {c_path: "x\n"}, "S": {s_path: "y\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"],
                   "acceptance": [py, "-c", "import sys; sys.exit(3)"]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSZ\b"]}],
                 EXIT_INPUT, extra=["--static-only"],
                 out_must=["SEPARABILITY: 0 findings", "SEPARABILITY_PARTIAL",
                          "SEPARABILITY_UNRESOLVED C acceptance skipped"],
                 out_must_not=["via acceptance", "SEPARABILITY_DEPENDENCY"],
                 err_must=["acceptance_runs=0"])

        scenario("bound: --jobs leaves the verdict unchanged",
                 {"C": {c_path: "no reference\n"}, "S": {s_path: "rows\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"],
                   "acceptance": [py, "-c", "import os, sys; sys.exit(0 if "
                                  "os.path.isfile('%s') else 1)" % s_path]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSZ\b"]}],
                 EXIT_DEPENDENT, extra=["--jobs", "4"],
                 out_must=["SEPARABILITY_DEPENDENCY C->S via acceptance"],
                 err_must=["acceptance_runs=2"])

        scenario("bound: --max-runs 1 skips the repair attempts",
                 {"C": {c_path: "no reference\n"}, "S": {s_path: "rows\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"],
                   "acceptance": [py, "-c", "import os, sys; sys.exit(0 if "
                                  "os.path.isfile('%s') else 1)" % s_path]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSZ\b"]}],
                 EXIT_INPUT, extra=["--max-runs", "1"],
                 out_must=["SEPARABILITY_PARTIAL 1 run(s) skipped",
                          "SEPARABILITY_UNRESOLVED C->S"],
                 out_must_not=["SEPARABILITY_DEPENDENCY C-><base>",
                              "SEPARABILITY_DEPENDENCY C->S via acceptance"],
                 err_must=["acceptance_runs=1", "skipped=1"])

        scenario("bound: --budget that expires skips runs",
                 {"C": {c_path: "no reference\n"}, "S": {s_path: "rows\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"],
                   "acceptance": [py, "-c", "import os, sys, time; "
                                  "time.sleep(1.5); sys.exit(0 if "
                                  "os.path.isfile('%s') else 1)" % s_path]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSZ\b"]}],
                 EXIT_INPUT, extra=["--budget", "0.5", "--timeout", "10"],
                 out_must=["SEPARABILITY_PARTIAL"],
                 out_must_not=["SEPARABILITY_DEPENDENCY C->S via acceptance"],
                 err_must=["skipped="])

        scenario("bound: a manifest with no acceptance units is complete",
                 {"C": {c_path: "x\n"}, "S": {s_path: "y\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSZ\b"]}],
                 EXIT_OK, out_must=["SEPARABILITY: 0 findings"],
                 err_must=["acceptance_runs=0"])

        scenario("bound: static-only with no acceptance units is complete",
                 {"C": {c_path: "x\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]}],
                 EXIT_OK, extra=["--static-only"],
                 out_must=["SEPARABILITY: 0 findings"],
                 out_must_not=["SEPARABILITY_PARTIAL"])

        scenario("bound: static-only counts one skipped run per dynamic unit",
                 {"C": {c_path: "x\n"}, "S": {s_path: "y\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"],
                   "acceptance": [py, "-c", "import sys; sys.exit(0)"]},
                  {"id": "S", "lands": [s_path], "exports": [r"\bSZ\b"]}],
                 EXIT_INPUT, extra=["--static-only"],
                 out_must=["SEPARABILITY_PARTIAL 1 run(s) skipped (static-only)"],
                 err_must=["skipped=1"])

        # ---- malformed or unevaluable input: exit 2
        shared_root = fresh()
        shared_lane, shared_base, shared_trees = _make_lane(
            shared_root, base_files,
            {"C": {c_path: "cites nothing\n"}, "S": {s_path: "| S998 | row |\n"}})
        readme_blob = _git_fixture(shared_lane, "rev-parse", shared_base + ":README.md")

        def shared_doc():
            return {"schema": SCHEMA, "base": shared_base, "claims": [
                {"id": "C", "tree": shared_trees["C"], "lands": [c_path],
                 "exports": [r"\bCQ\b"]},
                {"id": "S", "tree": shared_trees["S"], "lands": [s_path],
                 "exports": [s_range]},
            ]}

        def malformed(name, mutate, needle):
            doc = shared_doc()
            mutate(doc)
            root_dir = fresh()
            manifest = os.path.join(root_dir, "manifest.json")
            with open(manifest, "w", encoding="utf-8") as fh:
                json.dump(doc, fh)
            verdict(name, [manifest, "--lane", shared_lane], EXIT_INPUT, err_must=[needle])

        def raw(name, text, needle):
            root_dir = fresh()
            manifest = os.path.join(root_dir, "manifest.json")
            with open(manifest, "w", encoding="utf-8") as fh:
                fh.write(text)
            verdict(name, [manifest, "--lane", shared_lane], EXIT_INPUT, err_must=[needle])

        raw("malformed: not JSON", "{not json", "is not valid JSON")
        raw("malformed: duplicate JSON key",
            '{"schema": "%s", "base": "x", "base": "%s", "claims": []}' % (SCHEMA, shared_base),
            "repeats JSON key")
        malformed("malformed: manifest without schema", lambda d: d.pop("schema"),
                  "manifest is missing schema")
        malformed("malformed: wrong schema",
                  lambda d: d.update(schema="kotodama-separability-manifest-v0"),
                  "manifest schema must be")
        malformed("malformed: misspelled unit key is refused, not skipped",
                  lambda d: d["claims"][0].update(acceptence=["true"]),
                  "has unknown key(s) acceptence")
        malformed("malformed: unknown top-level key", lambda d: d.update(notes="x"),
                  "has unknown key(s) notes")
        malformed("malformed: base does not name a commit", lambda d: d.update(base="0" * 40),
                  "does not name a commit")
        malformed("malformed: unit tree is a blob",
                  lambda d: d["claims"][0].update(tree=readme_blob), "does not name a commit")
        malformed("malformed: unit key missing", lambda d: d["claims"][0].pop("exports"),
                  "is missing exports")
        malformed("malformed: empty lands", lambda d: d["claims"][0].update(lands=[]),
                  "must be a non-empty list of paths")
        malformed("malformed: land path absent at its tree",
                  lambda d: d["claims"][0].update(lands=["corpus/knowledge/missing.md"]),
                  "which is absent at its tree")
        malformed("malformed: absolute land path",
                  lambda d: d["claims"][0].update(lands=["/etc/passwd"]),
                  "is not a repo-relative path")
        malformed("malformed: non-canonical land path",
                  lambda d: d["claims"][1].update(lands=["corpus/../README.md"]),
                  "is not canonical")
        malformed("malformed: land path names .git metadata",
                  lambda d: d["claims"][1].update(lands=[".git/config"]), "names .git metadata")
        malformed("malformed: lands nest across units",
                  lambda d: d["claims"][1].update(lands=[c_path + "/row"]), "lands conflict")
        malformed("malformed: unknown role",
                  lambda d: d["claims"][0].update(role="reviewer"),
                  "role must be 'claim' or 'record'")
        malformed("malformed: record carries acceptance",
                  lambda d: d["claims"][1].update(role="record", acceptance=["true"]),
                  "carry no acceptance")
        malformed("malformed: needs_git without acceptance",
                  lambda d: d["claims"][0].update(needs_git=True), "needs_git requires")
        malformed("malformed: export is not a regex",
                  lambda d: d["claims"][0].update(exports=["("]), "is not a valid regex")
        malformed("malformed: export matches the empty string",
                  lambda d: d["claims"][0].update(exports=["0*"]), "matches the empty string")
        malformed("malformed: empty export string",
                  lambda d: d["claims"][0].update(exports=[""]),
                  "must be a non-empty regex string")
        malformed("malformed: empty acceptance argv",
                  lambda d: d["claims"][0].update(acceptance=[]),
                  "must be a non-empty argv list")
        malformed("malformed: acceptance program cannot start",
                  lambda d: d["claims"][0].update(
                      acceptance=["no-such-program-for-the-separability-selftest"]),
                  "cannot start")
        malformed("malformed: unit id declared twice",
                  lambda d: d["claims"][1].update(id="C"), "is declared twice")
        malformed("malformed: no units", lambda d: d.update(claims=[]),
                  "claims must be a non-empty list")

        scenario("malformed: an export matching base bytes of its own lands is not novel",
                 {"C": {c_path: "CQ already in base\nnew line\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"]}],
                 EXIT_INPUT, base={**base_files, c_path: "CQ already in base\n"},
                 err_must=["is not novel"])

        scenario("malformed: a WORKTREE land absent from --root is refused",
                 {"S": {s_path: "s\n"}},
                 [{"id": "C", "tree": WORKTREE, "lands": [c_path], "exports": [r"\bCQ\b"]},
                  {"id": "S", "lands": [s_path], "exports": [s_range]}],
                 EXIT_INPUT, err_must=["absent from the worktree"])

        not_repo = os.path.join(tmp, "not-a-repo")
        os.makedirs(not_repo)
        scenario("malformed: a needs_git leg with an unusable --root is unevaluated",
                 {"C": {c_path: "c\n"}},
                 [{"id": "C", "lands": [c_path], "exports": [r"\bCQ\b"], "needs_git": True,
                   "acceptance": [py, "-c", "import sys; sys.exit(0)"]}],
                 EXIT_INPUT, root=not_repo, out_must=["SEPARABILITY_UNEVALUATED"])

        good = os.path.join(tmp, "good-manifest.json")
        with open(good, "w", encoding="utf-8") as fh:
            json.dump(shared_doc(), fh)
        verdict("malformed: lane is not a git repository", [good, "--lane", not_repo], EXIT_INPUT,
                err_must=["not a git repository"])
        verdict("malformed: manifest file absent",
                [os.path.join(tmp, "absent.json"), "--lane", shared_lane], EXIT_INPUT,
                err_must=["cannot read manifest"])

    failed = [item for item in results if not item[1]]
    for name, ok, detail in results:
        print(("PASS " if ok else "FAIL ") + name + ("" if ok else ": " + detail))
    total = len(results)
    passed = total - len(failed)
    if failed:
        print("selftest: %d/%d checks passed - FAILED" % (passed, total))
        return False
    print("selftest: %d/%d checks passed - negative controls (export, inline URL, back-reference, "
          "land path, acceptance attribution in git-free and needs_git trees, timeout, direction, "
          "record citation, overlap, sorted output, WORKTREE), positive controls (disjoint, "
          "self-citation, name boundary, base-existing path, added-lines only, record unit, "
          "acceptance on base plus own lands, other units at base bytes, needs_git clone, "
          "WORKTREE reads), bounded verdicts (static-only, jobs, max-runs, budget, "
          "no-acceptance manifests, skipped-run accounting) and malformed or "
          "unevaluable input (exit 2)" % (passed, total))
    return True


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Check round claims for cross-claim dependencies (separability manifest).")
    ap.add_argument("manifest", nargs="?",
                    help="separability manifest JSON (schema %s)" % SCHEMA)
    ap.add_argument("--lane", default=LANE_DEFAULT,
                    help="git lane whose objects are read, read-only (default: the repo "
                         "holding this script)")
    ap.add_argument("--root", default=None,
                    help="filesystem root for WORKTREE units and needs_git clones "
                         "(default: --lane)")
    ap.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT,
                    help="seconds allowed per acceptance run (default %g)" % DEFAULT_TIMEOUT)
    ap.add_argument("--jobs", type=int, default=DEFAULT_JOBS,
                    help="acceptance units evaluated in parallel (default %d); "
                         "findings print sorted, so the verdict is unchanged" % DEFAULT_JOBS)
    ap.add_argument("--budget", type=float, default=DEFAULT_BUDGET,
                    help="global wall-clock seconds for the dynamic leg; runs not "
                         "started when it is exhausted are skipped and the verdict "
                         "is partial (exit 2)")
    ap.add_argument("--max-runs", type=int, default=DEFAULT_MAX_RUNS, dest="max_runs",
                    help="per-unit cap on dynamic runs (initial plus repair "
                         "attempts); runs beyond it are skipped (partial, exit 2)")
    ap.add_argument("--static-only", action="store_true", dest="static_only",
                    help="evaluate overlap and static legs only; the dynamic leg is "
                         "skipped and the verdict is partial (exit 2)")
    ap.add_argument("--selftest", "--self-test", action="store_true", dest="selftest",
                    help="run the negative and positive controls in temporary repos")
    args = ap.parse_args(argv)
    if args.selftest:
        if args.manifest is not None:
            ap.error("--selftest takes no manifest")
        return 0 if selftest() else 1
    if args.manifest is None:
        ap.error("a manifest path is required")
    if not (math.isfinite(args.timeout) and args.timeout > 0):
        ap.error("--timeout must be a positive finite number of seconds")
    if not args.jobs >= 1:
        ap.error("--jobs must be a positive integer")
    if args.budget is not None and not (math.isfinite(args.budget) and args.budget > 0):
        ap.error("--budget must be a positive finite number of seconds")
    if args.max_runs is not None and not args.max_runs >= 1:
        ap.error("--max-runs must be a positive integer")
    root = args.root if args.root is not None else args.lane
    try:
        return report(args.manifest, args.lane, root, args.timeout,
                      jobs=args.jobs, budget=args.budget,
                      max_runs=args.max_runs, static_only=args.static_only)
    except Unevaluated as exc:
        print("SEPARABILITY_UNEVALUATED %s" % exc)
        return EXIT_INPUT
    except InputError as exc:
        print("SEPARABILITY_INPUT_ERROR %s" % exc, file=sys.stderr)
        return EXIT_INPUT
    except Exception as exc:  # an internal fault must never read as a finding
        print("SEPARABILITY_INPUT_ERROR internal fault: %r" % (exc,), file=sys.stderr)
        return EXIT_INPUT


if __name__ == "__main__":
    sys.exit(main())
