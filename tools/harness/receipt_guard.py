#!/usr/bin/env python3
"""Preflight receipt writes against HEAD and every branch and remote-tracking ref, not the mutable Git index.

``guard_receipt(path, repo_root=ROOT)`` returns normally or emits a diagnostic
and raises SystemExit(3). Relative paths use repo_root or the current directory;
without a root, the repository is discovered from the destination's ancestors.
Only the exact environment value REFRESH_RECEIPTS=1 permits a committed receipt
write. Path safety and Git errors still fail closed.

The committed probe covers HEAD and every direct refs/heads/* and refs/remotes/*
ref. A ref that does not resolve to a commit, or any for-each-ref warning, fails
closed; symbolic refs are skipped because they duplicate their targets.
committed_sha is HEAD's commit (none when HEAD is unborn). landed_ref and
landed_sha name only a refs/remotes/* holder, never a local branch or HEAD, and
hit_refs lists every holder. REFRESH_RECEIPTS=1 waives only the committed refusal
and is consulted after every probe has completed.

``round_runner_main(measure, path, repo_root=ROOT, write_receipt=publish)``
checks before measure() and again before publish(result), returning publish's
exit status. With no publisher it returns measure's exit status; such a callback
must call guard_receipt itself immediately before writing. Neither form is a
sandbox for arbitrary callback side effects or a race-proof publication lock.

CLI: receipt_guard.py [--repo-root ROOT] RECEIPT | --selftest
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
import zlib

REFUSAL_EXIT_CODE = 3
REFRESH_ENV = "REFRESH_RECEIPTS"
TOOL = "tools/harness/receipt_guard.py"
OID_RE = re.compile(rb"(?:[0-9a-f]{40}|[0-9a-f]{64})")


class ReceiptGuardError(RuntimeError):
    exit_code = REFUSAL_EXIT_CODE

    def __init__(self, diagnostic, message):
        self.diagnostic = diagnostic
        super().__init__(f"receipt_guard: {message} [{diagnostic}]")


def _git(root, *args):
    env = {key: value for key, value in os.environ.items()
           if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1", LC_ALL="C")
    try:
        return subprocess.run(
            ["git", "--literal-pathspecs", "-C", str(root), *args],
            capture_output=True, env=env, timeout=15)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        raise ReceiptGuardError("RECEIPT-GUARD-GIT",
                                f"cannot determine committed status: {error}") from error


def _git_error(result, operation):
    detail = result.stderr.decode("utf-8", "replace").strip()
    return ReceiptGuardError(
        "RECEIPT-GUARD-GIT", "cannot determine committed status: "
        f"{operation} failed (exit {result.returncode}): {detail}")


def _head_state(root):
    """Return (HEAD commit or None when unborn, attached branch ref or None when detached)."""
    symbolic = _git(root, "symbolic-ref", "--quiet", "HEAD")
    if symbolic.returncode == 0:
        branch = os.fsdecode(symbolic.stdout).strip()
        if not branch.startswith("refs/heads/") or branch == "refs/heads/":
            raise ReceiptGuardError("RECEIPT-GUARD-GIT", "cannot determine committed status: "
                                    f"HEAD names {branch!r}, not a local branch")
    elif symbolic.returncode == 1 and not symbolic.stderr:
        branch = None
    else:
        raise _git_error(symbolic, "reading the symbolic HEAD")
    result = _git(root, "rev-parse", "--verify", "--quiet", "HEAD^{commit}")
    if result.returncode == 0 and OID_RE.fullmatch(result.stdout.strip()):
        return result.stdout.strip().decode("ascii"), branch
    if result.returncode == 1 and not result.stderr and branch is not None:
        return None, branch
    raise _git_error(result, "reading HEAD")


def _enumerate_refs(root):
    """Return sorted (name, commit) pairs for direct refs/heads/* and refs/remotes/*, and every listed name.

    Symbolic refs are skipped because they duplicate their targets. Anything git
    cannot resolve to a commit fails closed: a warning, a non-zero exit, a
    non-commit type, or a name that is not UTF-8.
    """
    result = _git(root, "for-each-ref",
                  "--format=%(refname)%00%(objectname)%00%(objecttype)%00%(symref)",
                  "refs/heads", "refs/remotes")
    if result.returncode or result.stderr:
        raise _git_error(result, "enumerating refs/heads and refs/remotes")
    refs, listed = [], set()
    for line in result.stdout.split(b"\n"):
        if not line:
            continue
        fields = line.split(b"\0")
        if len(fields) != 4:
            raise ReceiptGuardError("RECEIPT-GUARD-GIT",
                                    "cannot determine committed status: unexpected ref record")
        name, commit, kind, symref = fields
        try:
            text = name.decode("utf-8")
        except UnicodeDecodeError:
            raise ReceiptGuardError("RECEIPT-GUARD-GIT", "cannot determine committed status: "
                                    f"ref name is not UTF-8: {name!r}") from None
        listed.add(text)
        if symref:
            continue
        if not OID_RE.fullmatch(commit) or kind != b"commit":
            kind_text = kind.decode("ascii", "replace") or "missing"
            raise ReceiptGuardError("RECEIPT-GUARD-GIT", "cannot determine committed status: "
                                    f"{text} does not resolve to a commit ({kind_text})")
        refs.append((text, commit.decode("ascii")))
    return sorted(refs), listed


def _committed_entry(root, commit, relative):
    result = _git(root, "ls-tree", "-z", "--full-tree", commit, "--", relative.as_posix())
    if result.returncode:
        raise _git_error(result, "checking the committed receipt")
    if not result.stdout:
        return None
    entries = result.stdout.rstrip(b"\0").split(b"\0")
    metadata, separator, name = entries[0].partition(b"\t")
    fields = metadata.split()
    if (len(entries) != 1 or not separator or len(fields) != 3
            or fields[1] != b"blob" or not OID_RE.fullmatch(fields[2])
            or name != os.fsencode(relative.as_posix())):
        raise ReceiptGuardError("RECEIPT-GUARD-GIT",
                                "cannot determine committed status: unexpected tree entry")
    return fields[2].decode("ascii")


def _check_receipt(receipt_path, repo_root):
    try:
        if not os.fspath(receipt_path):
            raise ValueError("empty receipt path")
        anchor = Path(repo_root if repo_root is not None else Path.cwd()).resolve(strict=True)
        proposed = anchor / Path(receipt_path)
        candidate = Path(os.path.abspath(proposed))
        probe = anchor if repo_root is not None else candidate.parent
        while not probe.exists() and probe != probe.parent:
            probe = probe.parent
        result = _git(probe, "rev-parse", "--show-toplevel")
        if result.returncode:
            raise _git_error(result, "locating the working tree")
        root = Path(os.fsdecode(result.stdout).rstrip("\n")).resolve(strict=True)
        if repo_root is not None and root != anchor:
            raise ReceiptGuardError(
                "RECEIPT-GUARD-GIT", "cannot determine committed status: "
                f"bound root {anchor} differs from Git working tree {root}")
        try:
            relative = candidate.relative_to(root)
        except ValueError as error:
            raise ReceiptGuardError("RECEIPT-GUARD-PATH",
                                    f"receipt is outside the working tree: {candidate}") from error
        if not relative.parts or ".git" in relative.parts:
            raise ReceiptGuardError("RECEIPT-GUARD-PATH",
                                    f"not a receipt destination: {candidate}")
        for current in (proposed, *proposed.parents):
            try:
                info = current.lstat()
            except FileNotFoundError:
                continue
            if stat.S_ISLNK(info.st_mode):
                raise ReceiptGuardError("RECEIPT-GUARD-PATH",
                                        f"symlink receipt destination: {current}")
            if current != proposed and not stat.S_ISDIR(info.st_mode):
                raise ReceiptGuardError("RECEIPT-GUARD-PATH",
                                        f"non-directory receipt ancestor: {current}")
            if current == proposed and (not stat.S_ISREG(info.st_mode) or info.st_nlink != 1):
                raise ReceiptGuardError("RECEIPT-GUARD-PATH",
                                        f"receipt is not a singly-linked regular file: {candidate}")
    except (OSError, TypeError, ValueError, RuntimeError) as error:
        if isinstance(error, ReceiptGuardError):
            raise
        raise ReceiptGuardError("RECEIPT-GUARD-PATH", str(error)) from error
    head, branch = _head_state(root)
    refs, listed = _enumerate_refs(root)
    if head is None and branch is not None and branch in listed:
        raise ReceiptGuardError("RECEIPT-GUARD-GIT", "cannot determine committed status: "
                                f"{branch} is listed but HEAD does not resolve to a commit")
    tips = ([("HEAD", head)] if head is not None else []) + refs
    blobs = {}
    for _, commit in tips:
        if commit not in blobs:
            blobs[commit] = _committed_entry(root, commit, relative)
    hits = [(name, commit, blobs[commit]) for name, commit in tips if blobs[commit] is not None]
    if not hits:
        return
    landed = next((hit for hit in hits if hit[0].startswith("refs/remotes/")), None)
    committed_blob = blobs[head] if head is not None else None
    identity = (f"path={relative.as_posix()} committed_sha={head or 'none'} "
                f"committed_blob={committed_blob or 'none'} "
                f"landed_ref={landed[0] if landed else 'none'} "
                f"landed_sha={landed[1] if landed else 'none'} "
                f"landed_blob={landed[2] if landed else 'none'} "
                f"hit_refs={','.join(name for name, _, _ in hits)}")
    if os.environ.get(REFRESH_ENV) != "1":
        raise ReceiptGuardError(
            "RECEIPT-GUARD-COMMITTED",
            f"refusing overwrite {identity}; explicit {REFRESH_ENV}=1 required")
    print(f"receipt_guard: {REFRESH_ENV}=1 permits overwrite {identity} "
          "[RECEIPT-GUARD-REFRESH]", file=sys.stderr)


def guard_receipt(receipt_path, *, repo_root=None):
    """Refuse unsafe writes with a named stderr diagnostic and SystemExit(3)."""
    try:
        _check_receipt(receipt_path, repo_root)
    except ReceiptGuardError as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(error.exit_code) from None


def round_runner_main(runner, receipt_path, *, repo_root=None, write_receipt=None):
    """Guard before work and, when supplied, immediately before publication."""
    guard_receipt(receipt_path, repo_root=repo_root)
    result = runner()
    if write_receipt is None:
        return result
    guard_receipt(receipt_path, repo_root=repo_root)
    return write_receipt(result)


def _fixture_repo(root, *, committed):
    gitdir = root / ".git"
    (gitdir / "objects").mkdir(parents=True)
    (gitdir / "refs/heads").mkdir(parents=True)
    (gitdir / "HEAD").write_text("ref: refs/heads/control\n", encoding="ascii")
    (gitdir / "config").write_text(
        "[core]\n\trepositoryformatversion = 0\n\tbare = false\n", encoding="ascii")
    receipt = root / "validation.json"
    receipt.write_text('{"filed": true}\n', encoding="utf-8")
    if not committed:
        return receipt

    def store(kind, content):
        return _store_object(gitdir, kind, content)

    blob = store("blob", receipt.read_bytes())
    tree = store("tree", b"100644 validation.json\0" + bytes.fromhex(blob))
    commit = store("commit", (
        f"tree {tree}\nauthor Receipt Guard <guard@example.invalid> 0 +0000\n"
        "committer Receipt Guard <guard@example.invalid> 0 +0000\n\ncontrol fixture\n"
    ).encode("ascii"))
    (gitdir / "refs/heads/control").write_text(commit + "\n", encoding="ascii")
    return receipt


def _store_object(gitdir, kind, content):
    raw = kind.encode("ascii") + b" " + str(len(content)).encode("ascii") + b"\0" + content
    oid = hashlib.sha1(raw).hexdigest()
    target = gitdir / "objects" / oid[:2] / oid[2:]
    target.parent.mkdir(exist_ok=True)
    target.write_bytes(zlib.compress(raw))
    return oid


def _store_tree(gitdir, files):
    """Store the tree holding {posix path: blob oid} and return its oid."""
    entries, nested = {}, {}
    for path, blob in files.items():
        first, slash, rest = path.partition("/")
        if slash:
            nested.setdefault(first, {})[rest] = blob
        else:
            entries[first] = (b"100644", bytes.fromhex(blob))
    for name, sub in nested.items():
        entries[name] = (b"40000", bytes.fromhex(_store_tree(gitdir, sub)))
    body = b"".join(
        mode + b" " + name.encode("utf-8") + b"\0" + oid
        for name, (mode, oid) in sorted(
            entries.items(),
            key=lambda item: item[0] + ("/" if item[1][0] == b"40000" else "")))
    return _store_object(gitdir, "tree", body)


def _digest_tree(path):
    digest = hashlib.sha256()
    for item in sorted(path.rglob("*")):
        digest.update(os.fsencode(item.relative_to(path).as_posix()))
        if item.is_file():
            digest.update(item.read_bytes())
    return digest.hexdigest()


def _set_head(root, text):
    (root / ".git" / "HEAD").write_text(text + "\n", encoding="ascii")


def _write_ref(root, name, text):
    path = root / ".git" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text + "\n", encoding="ascii")


def _receipt_at(root, relative):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('{"filed": true}\n', encoding="utf-8")
    return path


def _landing_fixture(work, name):
    """Return a repository with C1 (no receipt), C2 (receipt), L (local child of C2),
    C4 (receipt under reports/round-50), and U1 and U2 (receipt under reports/up)."""
    root = work / name
    gitdir = root / ".git"
    (gitdir / "objects").mkdir(parents=True)
    (gitdir / "refs" / "heads").mkdir(parents=True)
    (gitdir / "refs" / "remotes").mkdir(parents=True)
    (gitdir / "HEAD").write_text("ref: refs/heads/main\n", encoding="ascii")
    (gitdir / "config").write_text(
        "[core]\n\trepositoryformatversion = 0\n\tbare = false\n", encoding="ascii")
    receipt = root / "validation.json"
    receipt.write_text('{"filed": true}\n', encoding="utf-8")
    blob = _store_object(gitdir, "blob", receipt.read_bytes())
    empty_tree = _store_tree(gitdir, {})
    receipt_tree = _store_tree(gitdir, {"validation.json": blob})

    def commit(tree, parent, message):
        body = f"tree {tree}\n"
        if parent is not None:
            body += f"parent {parent}\n"
        body += ("author Receipt Guard <guard@example.invalid> 0 +0000\n"
                 "committer Receipt Guard <guard@example.invalid> 0 +0000\n\n"
                 f"{message}\n")
        return _store_object(gitdir, "commit", body.encode("ascii"))

    oids = {"blob": blob, "tree": receipt_tree}
    oids["c1"] = commit(empty_tree, None, "no receipt")
    oids["c2"] = commit(receipt_tree, oids["c1"], "receipt")
    oids["l"] = commit(receipt_tree, oids["c2"], "local only")
    oids["c4"] = commit(_store_tree(gitdir, {"reports/round-50/validation.json": blob}),
                        oids["c1"], "other branch")
    oids["u1"] = commit(empty_tree, None, "upstream base")
    oids["u2"] = commit(_store_tree(gitdir, {"reports/up/validation.json": blob}),
                        oids["u1"], "upstream receipt")
    return root, receipt, oids


def _landing_controls(work, controls, env, script):
    def control(name, repo, target, expected_exit, must=(), must_not=(),
                refresh=None, extra_env=None):
        run_env = dict(env)
        if refresh is not None:
            run_env[REFRESH_ENV] = refresh
        run_env.update(extra_env or {})

        def snapshot():
            return (target.read_bytes() if target.exists() else None,
                    _digest_tree(repo / ".git"))

        before = snapshot()
        result = subprocess.run(
            [sys.executable, str(script), "--repo-root", str(repo), str(target)],
            capture_output=True, text=True, cwd=work, env=run_env, timeout=30)
        controls.append({
            "control": name,
            "passed": (result.returncode == expected_exit and snapshot() == before
                       and all(token in result.stderr for token in must)
                       and not any(token in result.stderr for token in must_not)),
            "expected_exit": expected_exit, "exit": result.returncode,
            "stderr": result.stderr.strip()})

    root, receipt, o = _landing_fixture(work, "r50-detached-below-remote")
    _set_head(root, o["c1"])
    _write_ref(root, "refs/remotes/origin/main", o["c2"])
    control("r50-detached-below-remote", root, receipt, 3, must=(
        "RECEIPT-GUARD-COMMITTED", f"committed_sha={o['c1']}", "committed_blob=none",
        "landed_ref=refs/remotes/origin/main", f"landed_sha={o['c2']}"))

    root, receipt, o = _landing_fixture(work, "r50-local-over-remote")
    _set_head(root, o["l"])
    _write_ref(root, "refs/remotes/origin/main", o["c2"])
    control("r50-local-over-remote", root, receipt, 3, must=(
        "RECEIPT-GUARD-COMMITTED", f"committed_sha={o['l']}",
        "landed_ref=refs/remotes/origin/main", f"landed_sha={o['c2']}"),
        must_not=(f"landed_sha={o['l']}",))

    root, receipt, o = _landing_fixture(work, "r50-unborn-remote")
    _write_ref(root, "refs/remotes/origin/main", o["c2"])
    control("r50-unborn-remote", root, receipt, 3, must=(
        "RECEIPT-GUARD-COMMITTED", "committed_sha=none",
        "landed_ref=refs/remotes/origin/main", f"landed_sha={o['c2']}"))

    root, receipt, o = _landing_fixture(work, "r50-unborn-empty")
    control("r50-unborn-empty", root, receipt, 0, must_not=("RECEIPT-GUARD",))

    root, receipt, o = _landing_fixture(work, "r50-missing-origin-ref")
    with (root / ".git" / "config").open("a", encoding="ascii") as handle:
        handle.write('[remote "origin"]\n\turl = /nonexistent/origin.git\n'
                     '\tfetch = +refs/heads/*:refs/remotes/origin/*\n')
    control("r50-missing-origin-ref", root, receipt, 0,
            must_not=("RECEIPT-GUARD-GIT", "RECEIPT-GUARD-COMMITTED"))

    root, _, o = _landing_fixture(work, "r50-other-branch-remote")
    _set_head(root, "ref: refs/heads/scratch")
    _write_ref(root, "refs/heads/scratch", o["c1"])
    _write_ref(root, "refs/remotes/origin/kotodama", o["c4"])
    control("r50-other-branch-remote", root,
            _receipt_at(root, "reports/round-50/validation.json"), 3, must=(
                "RECEIPT-GUARD-COMMITTED", "landed_ref=refs/remotes/origin/kotodama"))

    root, _, o = _landing_fixture(work, "r50-other-remote")
    _set_head(root, o["u1"])
    _write_ref(root, "refs/remotes/upstream/main", o["u2"])
    control("r50-other-remote", root, _receipt_at(root, "reports/up/validation.json"), 3, must=(
        "RECEIPT-GUARD-COMMITTED", "landed_ref=refs/remotes/upstream/main"))

    root, receipt, o = _landing_fixture(work, "r50-local-branch-not-landed")
    _write_ref(root, "refs/heads/main", o["l"])
    _write_ref(root, "refs/remotes/origin/main", o["c1"])
    control("r50-local-branch-not-landed", root, receipt, 3, must=(
        "RECEIPT-GUARD-COMMITTED", f"committed_sha={o['l']}", "landed_ref=none",
        "landed_sha=none", "hit_refs=HEAD,refs/heads/main"),
        must_not=(f"landed_sha={o['l']}",))

    root, receipt, o = _landing_fixture(work, "r50-head-is-remote-tip")
    _write_ref(root, "refs/heads/main", o["c2"])
    _write_ref(root, "refs/remotes/origin/main", o["c2"])
    control("r50-head-is-remote-tip", root, receipt, 3, must=(
        "RECEIPT-GUARD-COMMITTED", f"committed_sha={o['c2']}",
        "landed_ref=refs/remotes/origin/main", f"landed_sha={o['c2']}"))

    root, receipt, o = _landing_fixture(work, "r50-corrupt-remote")
    _set_head(root, o["c1"])
    _write_ref(root, "refs/remotes/origin/main", "garbage")
    control("r50-corrupt-remote", root, receipt, 3,
            must=("RECEIPT-GUARD-GIT", "refs/remotes/origin/main"),
            must_not=("RECEIPT-GUARD-COMMITTED",))

    root, receipt, o = _landing_fixture(work, "r50-missing-object-ref")
    _set_head(root, o["c1"])
    _write_ref(root, "refs/remotes/origin/ghost", "0123456789012345678901234567890123456789")
    control("r50-missing-object-ref", root, receipt, 3, must=("RECEIPT-GUARD-GIT",))

    root, receipt, o = _landing_fixture(work, "r50-tree-typed-ref")
    _set_head(root, o["c1"])
    _write_ref(root, "refs/remotes/origin/main", o["tree"])
    control("r50-tree-typed-ref", root, receipt, 3, must=("RECEIPT-GUARD-GIT",))

    root, receipt, o = _landing_fixture(work, "r50-corrupt-branch")
    _set_head(root, "ref: refs/heads/scratch")
    _write_ref(root, "refs/heads/scratch", "garbage")
    control("r50-corrupt-branch", root, receipt, 3, must=("RECEIPT-GUARD-GIT",))

    root, receipt, o = _landing_fixture(work, "r50-dangling-origin-head")
    _set_head(root, o["c1"])
    _write_ref(root, "refs/remotes/origin/HEAD", "ref: refs/remotes/origin/nope")
    _write_ref(root, "refs/remotes/origin/main", o["c1"])
    control("r50-dangling-origin-head", root, receipt, 0, must_not=("RECEIPT-GUARD",))

    root, receipt, o = _landing_fixture(work, "r50-refresh-landed")
    _set_head(root, o["c1"])
    _write_ref(root, "refs/remotes/origin/main", o["c2"])
    control("r50-refresh-landed", root, receipt, 0, refresh="1", must=(
        "RECEIPT-GUARD-REFRESH", f"committed_sha={o['c1']}", f"landed_sha={o['c2']}"))

    root, receipt, o = _landing_fixture(work, "r50-refresh-local")
    _write_ref(root, "refs/heads/main", o["l"])
    _write_ref(root, "refs/remotes/origin/main", o["c1"])
    control("r50-refresh-local", root, receipt, 0, refresh="1", must=(
        "RECEIPT-GUARD-REFRESH", "landed_ref=none"))

    root, receipt, o = _landing_fixture(work, "r50-refresh-corrupt-remote")
    _set_head(root, o["c1"])
    _write_ref(root, "refs/remotes/origin/main", "garbage")
    control("r50-refresh-corrupt-remote", root, receipt, 3, refresh="1",
            must=("RECEIPT-GUARD-GIT",), must_not=("RECEIPT-GUARD-REFRESH",))

    root, receipt, o = _landing_fixture(work, "r50-refresh-nonexact-landed")
    _set_head(root, o["c1"])
    _write_ref(root, "refs/remotes/origin/main", o["c2"])
    control("r50-refresh-nonexact-landed", root, receipt, 3, refresh="yes",
            must=("RECEIPT-GUARD-COMMITTED",))

    root, receipt, o = _landing_fixture(work, "r50-refresh-path-refused")
    _set_head(root, o["c1"])
    _write_ref(root, "refs/remotes/origin/main", o["c2"])
    alias = root / "alias.json"
    alias.symlink_to(receipt)
    control("r50-refresh-path-refused", root, alias, 3, refresh="1",
            must=("RECEIPT-GUARD-PATH",))

    root, receipt, o = _landing_fixture(work, "r50-env-scrub")
    _set_head(root, o["c1"])
    _write_ref(root, "refs/remotes/origin/main", o["c2"])
    control("r50-env-scrub", root, receipt, 3,
            extra_env={"GIT_DIR": str(work / "nonexistent-git")},
            must=("RECEIPT-GUARD-COMMITTED",))

    root, receipt, o = _landing_fixture(work, "r50-nonutf8-refname")
    _set_head(root, o["c1"])
    with open(os.fsencode(str(root / ".git")) + b"/refs/heads/x\xff", "wb") as handle:
        handle.write((o["c2"] + "\n").encode("ascii"))
    control("r50-nonutf8-refname", root, receipt, 3,
            must=("RECEIPT-GUARD-GIT",), must_not=("Traceback",))

    root, receipt, o = _landing_fixture(work, "attached-head-holds-refused")
    _write_ref(root, "refs/heads/main", o["c2"])
    control("attached-head-holds-refused", root, receipt, 3, must=(
        "RECEIPT-GUARD-COMMITTED", f"committed_sha={o['c2']}",
        f"committed_blob={o['blob']}", "landed_ref=none"))

    root, receipt, o = _landing_fixture(work, "unborn-local-branch-refused")
    _write_ref(root, "refs/heads/side", o["c2"])
    control("unborn-local-branch-refused", root, receipt, 3, must=(
        "RECEIPT-GUARD-COMMITTED", "committed_sha=none", "landed_ref=none",
        "hit_refs=refs/heads/side"))

    root, receipt, o = _landing_fixture(work, "other-local-branch-refused")
    _write_ref(root, "refs/heads/main", o["c1"])
    _write_ref(root, "refs/heads/side", o["c2"])
    control("other-local-branch-refused", root, receipt, 3, must=(
        "RECEIPT-GUARD-COMMITTED", f"committed_sha={o['c1']}", "committed_blob=none",
        "landed_ref=none", "hit_refs=refs/heads/side"))



def selftest_receipt():
    controls = []
    scratch = Path(__file__).resolve().parents[2] / ".scratch"
    scratch.mkdir(parents=True, exist_ok=True)
    script = Path(__file__).resolve()
    with tempfile.TemporaryDirectory(prefix="receipt-guard-", dir=scratch) as temporary:
        work = Path(temporary)
        root = work / "repo"
        receipt = _fixture_repo(root, committed=True)
        original = receipt.read_bytes()
        env = dict(os.environ)
        env.pop(REFRESH_ENV, None)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        env["TMPDIR"] = str(scratch)
        head = _head_state(root)[0]
        blob = _git(root, "rev-parse", "HEAD:validation.json").stdout.decode("ascii").strip()

        def cli(name, target, expected_exit, diagnostic=None, *, refresh=None,
                repo=root, extra_env=None):
            run_env = dict(env)
            if refresh is not None:
                run_env[REFRESH_ENV] = refresh
            run_env.update(extra_env or {})
            argv = [sys.executable, str(script)]
            if repo is not None:
                argv += ["--repo-root", str(repo)]
            argv.append(str(target))
            before = receipt.read_bytes() if receipt.exists() else None
            result = subprocess.run(argv, capture_output=True, text=True,
                                    cwd=work, env=run_env, timeout=30)
            after = receipt.read_bytes() if receipt.exists() else None
            passed = (result.returncode == expected_exit and before == after
                      and (diagnostic is None or diagnostic in result.stderr))
            if "RECEIPT-GUARD-COMMITTED" in result.stderr or "RECEIPT-GUARD-REFRESH" in result.stderr:
                passed = passed and f"committed_sha={head}" in result.stderr and f"committed_blob={blob}" in result.stderr
            controls.append({"control": name, "passed": passed,
                             "expected_exit": expected_exit, "exit": result.returncode,
                             "stderr": result.stderr.strip()})

        cli("committed-refused", receipt, 3, "RECEIPT-GUARD-COMMITTED")
        cli("committed-refresh-allowed", receipt, 0, "RECEIPT-GUARD-REFRESH", refresh="1")
        for value in ("", "0", "true", "yes", "01", " 1", "1 "):
            cli(f"nonexact-refresh-{value!r}-refused", receipt, 3,
                "RECEIPT-GUARD-COMMITTED", refresh=value)
        receipt.write_bytes(b"dirty receipt\n")
        cli("dirty-committed-refused", receipt, 3, "RECEIPT-GUARD-COMMITTED")
        staged = _git(root, "add", "--", "validation.json")
        controls.append({"control": "fixture-stage-dirty", "passed": staged.returncode == 0})
        cli("staged-dirty-committed-refused", receipt, 3, "RECEIPT-GUARD-COMMITTED")
        receipt.unlink()
        cli("deleted-committed-refused", receipt, 3, "RECEIPT-GUARD-COMMITTED")
        staged = _git(root, "add", "--", "validation.json")
        controls.append({"control": "fixture-stage-deletion", "passed": staged.returncode == 0})
        cli("staged-deletion-refused", receipt, 3, "RECEIPT-GUARD-COMMITTED")
        receipt.write_bytes(original)
        cli("new-receipt-missing-parents-allowed", root / "reports/new/validation.json", 0)
        fresh = root / "new.json"
        fresh.write_text("new\n", encoding="utf-8")
        cli("untracked-receipt-allowed", fresh, 0)
        staged = _git(root, "add", "--", "new.json")
        controls.append({"control": "fixture-stage-new", "passed": staged.returncode == 0})
        cli("staged-new-receipt-allowed", fresh, 0)
        cli("relative-receipt-refused", "validation.json", 3, "RECEIPT-GUARD-COMMITTED")
        cli("destination-root-discovery", receipt, 3, "RECEIPT-GUARD-COMMITTED", repo=None)
        cli("literal-pathspec-no-wildcard-match", root / "validation[.]json", 0)
        cli("literal-pathspec-no-magic", root / ":(glob)*", 0)
        cli("git-environment-cannot-rebind-root", receipt, 3, "RECEIPT-GUARD-COMMITTED",
            extra_env={"GIT_DIR": str(work / "nonexistent-git")})
        for refresh in (None, "1"):
            cli(f"outside-repo-refused-{refresh}", work / "outside.json", 3,
                "RECEIPT-GUARD-PATH", refresh=refresh)
            cli(f"directory-refused-{refresh}", root, 3,
                "RECEIPT-GUARD-PATH", refresh=refresh)
            alias = root / "alias.json"
            alias.symlink_to(receipt)
            cli(f"symlink-alias-refused-{refresh}", alias, 3,
                "RECEIPT-GUARD-PATH", refresh=refresh)
            alias.unlink()
            alias.symlink_to(root, target_is_directory=True)
            cli(f"symlink-ancestor-refused-{refresh}", alias / "validation.json", 3,
                "RECEIPT-GUARD-PATH", refresh=refresh)
            cli(f"symlink-dotdot-refused-{refresh}", alias / ".." / "repo" / "new.json", 3,
                "RECEIPT-GUARD-PATH", refresh=refresh)
            alias.unlink()
            os.link(receipt, alias)
            cli(f"hardlink-alias-refused-{refresh}", alias, 3,
                "RECEIPT-GUARD-PATH", refresh=refresh)
            alias.unlink()
        unborn = work / "unborn"
        unborn_receipt = _fixture_repo(unborn, committed=False)
        cli("unborn-receipt-allowed", unborn_receipt, 0, repo=unborn)
        not_repo = work / "not-repo"
        not_repo.mkdir()
        cli("explicit-root-cannot-discover-parent-repo", not_repo / "validation.json", 3,
            "RECEIPT-GUARD-GIT", repo=not_repo)
        cli("missing-git-fails-closed", receipt, 3, "RECEIPT-GUARD-GIT",
            extra_env={"PATH": str(work / "no-git")})
        linked = work / "linked"
        result = _git(root, "worktree", "add", "--detach", "--no-checkout", str(linked))
        controls.append({"control": "fixture-linked-worktree", "passed": result.returncode == 0})
        cli("linked-worktree-refused", linked / "validation.json", 3,
            "RECEIPT-GUARD-COMMITTED", repo=linked)
        callback_source = (
            "import sys\n"
            f"sys.path.insert(0, {str(script.parents[2])!r})\n"
            "from tools.harness.receipt_guard import round_runner_main\n"
            "from pathlib import Path\n"
            "def measure():\n"
            "    print('RUNNER-CALLED')\n"
            "    return 'refreshed\\n'\n"
            "def publish(result):\n"
            f"    Path({str(receipt)!r}).write_text(result, encoding='utf-8')\n"
            "    return 7\n"
            f"sys.exit(round_runner_main(measure, {str(receipt)!r}, repo_root={str(root)!r}, write_receipt=publish))\n"
        )
        for name, refresh, expected_exit, expected_bytes, called in (
                ("runner-refusal-before-callback", None, 3, original, False),
                ("runner-refresh-preserves-exit", "1", 7, b"refreshed\n", True)):
            run_env = dict(env)
            if refresh is not None:
                run_env[REFRESH_ENV] = refresh
            result = subprocess.run([sys.executable, "-c", callback_source],
                                    capture_output=True, text=True,
                                    cwd=work, env=run_env, timeout=30)
            controls.append({"control": name, "exit": result.returncode,
                             "passed": result.returncode == expected_exit
                             and receipt.read_bytes() == expected_bytes
                             and ("RUNNER-CALLED" in result.stdout) == called
                             and (called or "RECEIPT-GUARD-COMMITTED" in result.stderr)})
        receipt.write_bytes(original)
        (root / ".git/refs/heads/control").unlink()
        (root / ".git/HEAD").write_text("ref: refs/heads/not-filed\n", encoding="ascii")
        second_check_source = callback_source.replace(
            "    print('RUNNER-CALLED')",
            "    print('RUNNER-CALLED')\n"
            f"    Path({str(root / '.git/HEAD')!r}).write_text('ref: refs/heads/control\\n', encoding='ascii')\n"
            f"    Path({str(root / '.git/refs/heads/control')!r}).write_text({head + chr(10)!r}, encoding='ascii')")
        result = subprocess.run([sys.executable, "-c", second_check_source],
                                capture_output=True, text=True,
                                cwd=work, env=env, timeout=30)
        controls.append({"control": "runner-rechecks-before-publisher", "exit": result.returncode,
                         "passed": result.returncode == 3 and receipt.read_bytes() == original
                         and "RUNNER-CALLED" in result.stdout
                         and "RECEIPT-GUARD-COMMITTED" in result.stderr})
        (root / ".git/refs/heads/control").write_text("invalid\n", encoding="ascii")
        cli("corrupt-head-fails-closed", receipt, 3, "RECEIPT-GUARD-GIT")

        _landing_controls(work, controls, env, script)
    passed = sum(control["passed"] for control in controls)
    return {"tool": TOOL, "command": f"python3 {TOOL} --selftest",
            "date": dt.date.today().isoformat(), "controls": controls,
            "controls_passed": passed, "controls_total": len(controls),
            "selftest_passed": passed == len(controls),
            "limits": ["Synthetic Git objects and Git index/worktree controls exist only in "
                       "a disposable in-repo fixture; no live Git metadata or filed receipt is written.",
                       "The two-phase helper rechecks before its publisher; callbacks remain "
                       "responsible for their own unrelated writes, and publication is not race-proof."]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", nargs="?")
    parser.add_argument("--repo-root", "--root", type=Path)
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        if args.receipt is not None or args.repo_root is not None:
            parser.error("--selftest takes no other arguments")
        receipt = selftest_receipt()
        print(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True))
        return 0 if receipt["selftest_passed"] else 1
    if args.receipt is None:
        parser.error("give a receipt path or --selftest")
    guard_receipt(args.receipt, repo_root=args.repo_root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
