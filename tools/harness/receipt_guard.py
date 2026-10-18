#!/usr/bin/env python3
"""Preflight receipt writes against HEAD, not the mutable Git index.

``guard_receipt(path, repo_root=ROOT)`` returns normally or emits a diagnostic
and raises SystemExit(3). Relative paths use repo_root or the current directory;
without a root, the repository is discovered from the destination's ancestors.
Only the exact environment value REFRESH_RECEIPTS=1 permits a committed receipt
write. Path safety and Git errors still fail closed.

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


def _head_commit(root):
    result = _git(root, "rev-parse", "--verify", "--quiet", "HEAD^{commit}")
    if result.returncode == 0 and OID_RE.fullmatch(result.stdout.strip()):
        return result.stdout.strip().decode("ascii")
    if result.returncode == 1:
        symbolic = _git(root, "symbolic-ref", "--quiet", "HEAD")
        if symbolic.returncode == 0:
            branch = os.fsdecode(symbolic.stdout).strip()
            exists = _git(root, "show-ref", "--verify", "--quiet", branch)
            if exists.returncode == 1:
                return None
    raise _git_error(result, "reading HEAD")


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
    head = _head_commit(root)
    if head is None:
        return
    result = _git(root, "ls-tree", "-z", "--full-tree", head, "--", relative.as_posix())
    if result.returncode:
        raise _git_error(result, "checking the committed receipt")
    if not result.stdout:
        return
    entries = result.stdout.rstrip(b"\0").split(b"\0")
    metadata, separator, name = entries[0].partition(b"\t")
    fields = metadata.split()
    if (len(entries) != 1 or not separator or len(fields) != 3
            or fields[1] != b"blob" or not OID_RE.fullmatch(fields[2])
            or name != os.fsencode(relative.as_posix())):
        raise ReceiptGuardError("RECEIPT-GUARD-GIT",
                                "cannot determine committed status: unexpected tree entry")
    identity = (f"path={relative.as_posix()} committed_sha={head} "
                f"committed_blob={fields[2].decode('ascii')}")
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
        raw = kind.encode("ascii") + b" " + str(len(content)).encode("ascii") + b"\0" + content
        oid = hashlib.sha1(raw).hexdigest()
        target = gitdir / "objects" / oid[:2] / oid[2:]
        target.parent.mkdir(exist_ok=True)
        target.write_bytes(zlib.compress(raw))
        return oid

    blob = store("blob", receipt.read_bytes())
    tree = store("tree", b"100644 validation.json\0" + bytes.fromhex(blob))
    commit = store("commit", (
        f"tree {tree}\nauthor Receipt Guard <guard@example.invalid> 0 +0000\n"
        "committer Receipt Guard <guard@example.invalid> 0 +0000\n\ncontrol fixture\n"
    ).encode("ascii"))
    (gitdir / "refs/heads/control").write_text(commit + "\n", encoding="ascii")
    return receipt


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
        head = _head_commit(root)
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
        (root / ".git/HEAD").write_text("ref: refs/heads/not-filed\n", encoding="ascii")
        second_check_source = callback_source.replace(
            "    print('RUNNER-CALLED')",
            f"    Path({str(root / '.git/HEAD')!r}).write_text('ref: refs/heads/control\\n', encoding='ascii')")
        result = subprocess.run([sys.executable, "-c", second_check_source],
                                capture_output=True, text=True,
                                cwd=work, env=env, timeout=30)
        controls.append({"control": "runner-rechecks-before-publisher", "exit": result.returncode,
                         "passed": result.returncode == 3 and receipt.read_bytes() == original
                         and "RECEIPT-GUARD-COMMITTED" in result.stderr})
        (root / ".git/refs/heads/control").write_text("invalid\n", encoding="ascii")
        cli("corrupt-head-fails-closed", receipt, 3, "RECEIPT-GUARD-GIT")
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
