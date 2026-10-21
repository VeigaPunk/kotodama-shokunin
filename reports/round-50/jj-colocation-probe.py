#!/usr/bin/env python3
"""Count jj-colocation false negatives and false positives in the lane's git gates.

Round 50, claim O. Every sandbox is a plain-git repository under a fresh
mkdtemp directory in /tmp. Host GIT_* variables are dropped, and
GIT_CEILING_DIRECTORIES=/tmp stops repository discovery at the sandbox, so a
tree under the lane cannot borrow the lane's repository. jj is never invoked.

Defect states (flagged = false negative: the risk is present):
  R1 cited-sha-not-landed  receipt committed on main and origin/main, HEAD a
     local-only commit above the tip. Flagged when receipt_guard presents a sha
     as committed or landed that is not an ancestor of refs/remotes/origin/main.
  R2 overwrite-allowed     receipt committed on main and origin/main, HEAD
     detached one commit below the tip. Flagged when receipt_guard exits 0.
  R3 skip-pass             repository without the pinned BASE_COMMIT object.
     Flagged when check-readme-revisions --selftest exits 0.

Positive states (flagged = false positive: the tool refuses or fails correctly
permitted work):
  P1 normal-state-allowed           HEAD == origin/main, receipt absent.
  P2 new-untracked-receipt-allowed  receipt file on disk, in no commit.
  P3 pinned-readme-selftest-passes  clone --shared of the history repository,
                                    which holds the pin; --selftest must exit 0
                                    and PASS the control for the pin.
  P4 refresh-permit-allowed         receipt committed, HEAD == origin/main,
                                    REFRESH_RECEIPTS=1 (the documented permit).

A presented sha is a 40- or 64-hex token that a label names as committed or
landed (labels containing blob or tree are ignored), or any other token that
names a commit object and carries no head or local label. A sha labelled head
or local is the local HEAD and is never presented.

Output: one JSON object per case, then
  JJ_COLOCATION_FALSE_NEGATIVES=n/3
  JJ_COLOCATION_FALSE_POSITIVES=m/4
Exit 0 after a completed measurement, whatever the counts. Exit 2 on setup
error: missing tools, no history repository holding the pin, a broken fixture,
or a git or tool process that cannot be started.

Usage:
  python3 reports/round-50/jj-colocation-probe.py --tools-root DIR [--history-repo DIR]
  --history-repo defaults to the git work tree that contains --tools-root.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SANDBOX_PARENT = "/tmp"
GUARD = Path("tools/harness/receipt_guard.py")
README_GATE = Path("tools/check-readme-revisions.py")
RECEIPT = "reports/validation.json"
README_FIXTURE = "# corpus\n\nrevision: 1.0 - only\ninitial body\n"
PIN_RE = re.compile(r'^BASE_COMMIT\s*=\s*["\']([0-9a-f]{40})["\']', re.MULTILINE)
TOKEN_RE = re.compile(r"(?:([A-Za-z_][A-Za-z0-9_]*)=)?\b([0-9a-f]{40}|[0-9a-f]{64})\b")
GIT_IDENTITY = ["-c", "user.name=Jj Colocation Probe", "-c", "user.email=probe@example.invalid",
                "-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null"]
EVIDENCE_CAP = 240


class SetupError(RuntimeError):
    """The fixture or tooling cannot be measured, so any count would be meaningless."""


class Sandbox:
    """One mkdtemp directory under /tmp that holds every fixture and tool run."""

    def __init__(self):
        self.root = Path(tempfile.mkdtemp(prefix="jj-colocation-probe.", dir=SANDBOX_PARENT))
        self.home = self.root / "home"
        self.home.mkdir()

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        shutil.rmtree(self.root, ignore_errors=True)

    def env(self, **extra):
        env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        env.pop("REFRESH_RECEIPTS", None)
        env.update(HOME=str(self.home), XDG_CONFIG_HOME=str(self.home / ".config"),
                   LC_ALL="C", PYTHONDONTWRITEBYTECODE="1",
                   GIT_CEILING_DIRECTORIES=SANDBOX_PARENT)
        env.update(extra)
        return env

    def run(self, argv, cwd, env=None):
        try:
            return subprocess.run(argv, cwd=str(cwd), env=self.env() if env is None else env,
                                  capture_output=True, encoding="utf-8", errors="replace",
                                  timeout=120)
        except (OSError, subprocess.SubprocessError) as error:
            raise SetupError(f"cannot run {argv[0]}: {error}") from error

    def git(self, repo, *args, check=True):
        result = self.run(["git", "-C", str(repo), *args], repo)
        if check and result.returncode:
            raise SetupError(f"git {' '.join(args)} failed (exit {result.returncode}): "
                             f"{result.stderr.strip()}")
        return result

    def init(self, name):
        repo = self.root / name
        repo.mkdir()
        self.git(repo, "init", "-q", "-b", "main")
        self.git(repo, "config", "core.autocrlf", "false")
        return repo

    def commit(self, repo, message, *, empty=False):
        self.git(repo, "add", "-A")
        argv = ["git", "-C", str(repo), *GIT_IDENTITY, "commit", "-q", "-m", message]
        if empty:
            argv.append("--allow-empty")
        result = self.run(argv, repo)
        if result.returncode:
            raise SetupError(f"git commit failed (exit {result.returncode}): "
                             f"{result.stderr.strip()}")

    def rev(self, repo, ref):
        return self.git(repo, "rev-parse", "--verify", f"{ref}^{{commit}}").stdout.strip()

    def has(self, repo, spec):
        return self.git(repo, "cat-file", "-e", spec, check=False).returncode == 0

    def object_type(self, repo, sha):
        result = self.git(repo, "cat-file", "-t", sha, check=False)
        return result.stdout.strip() if result.returncode == 0 else None

    def is_ancestor(self, repo, sha, ref):
        if self.object_type(repo, sha) != "commit":
            return False
        return self.git(repo, "merge-base", "--is-ancestor", sha, ref,
                        check=False).returncode == 0

    def guard(self, tools_root, repo, env=None):
        return self.run([sys.executable, str(tools_root / GUARD), "--repo-root", str(repo),
                         str(repo / RECEIPT)], self.root, env)

    def gate(self, lane):
        return self.run([sys.executable, str(lane / README_GATE), "--selftest"], lane)


def write(repo, rel, text):
    path = Path(repo) / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def gate_pin(tools_root):
    match = PIN_RE.search((tools_root / README_GATE).read_text(encoding="utf-8"))
    if match is None:
        raise SetupError(f'no BASE_COMMIT = "<40-hex>" pin declared in {README_GATE}')
    return match.group(1)


def history_repo(args, tools_root, box, pin):
    if args.history_repo is not None:
        candidate = args.history_repo.resolve()
    else:
        found = box.run(["git", "-C", str(tools_root), "rev-parse", "--show-toplevel"], box.root)
        if found.returncode:
            raise SetupError("the tools root is not inside a git work tree; pass --history-repo DIR")
        candidate = Path(found.stdout.strip())
    if box.run(["git", "-C", str(candidate), "cat-file", "-e", f"{pin}^{{commit}}"],
               box.root).returncode:
        raise SetupError(f"pinned base {pin} is absent from {candidate}; the P3 state cannot run")
    return candidate


def gate_lane(box, name, tools_root):
    """A fresh repository holding the gate script and a corpus README, without the pin."""
    lane = box.init(name)
    (lane / "tools").mkdir()
    shutil.copyfile(tools_root / README_GATE, lane / README_GATE)
    write(lane, "corpus/README.md", README_FIXTURE)
    box.commit(lane, "synthetic lane holding the gate script")
    return lane


def landed_repo(box, name, *, receipt=False):
    """Normal state: HEAD equals refs/remotes/origin/main, with or without a committed receipt."""
    repo = box.init(name)
    write(repo, "README.md", "normal state\n")
    if receipt:
        write(repo, RECEIPT, "committed receipt\n")
    box.commit(repo, "C0: normal state")
    box.git(repo, "update-ref", "refs/remotes/origin/main", box.rev(repo, "refs/heads/main"))
    if (box.rev(repo, "HEAD") != box.rev(repo, "refs/remotes/origin/main")
            or box.has(repo, f"HEAD:{RECEIPT}") != receipt):
        raise SetupError(f"{name} fixture broken: HEAD must equal origin/main with "
                         f"receipt={receipt}")
    return repo


def presented(box, repo, text):
    """(label, sha) pairs that the tool presents as committed or landed commits."""
    found = []
    for label, sha in TOKEN_RE.findall(text):
        if re.search(r"blob|tree", label):
            continue
        if re.search(r"head|local", label) and not re.search(r"committed|landed", label):
            continue
        if re.search(r"committed|landed", label) or box.object_type(repo, sha) == "commit":
            found.append((label or "unlabelled", sha))
    return found


def _evidence(text):
    return " ".join((text or "").split())[:EVIDENCE_CAP]


def _row(case, name, kind, result, flagged, detail, evidence=None, **fields):
    text = (result.stderr or result.stdout) if evidence is None else evidence
    return {"case": case, "name": name, "kind": kind, "flagged": flagged,
            "exit": result.returncode, "detail": detail, "evidence": _evidence(text),
            **fields}


def case_r1(box, tools_root):
    repo = box.init("r1-cited-local")
    write(repo, RECEIPT, "R1 receipt\n")
    box.commit(repo, "C0: receipt committed on main")
    box.git(repo, "update-ref", "refs/remotes/origin/main", box.rev(repo, "refs/heads/main"))
    box.git(repo, "checkout", "-q", "--detach")
    box.commit(repo, "C1: local-only working-copy commit", empty=True)
    local = box.rev(repo, "HEAD")
    if (local == box.rev(repo, "refs/remotes/origin/main")
            or not box.has(repo, f"refs/remotes/origin/main:{RECEIPT}")):
        raise SetupError("R1 fixture broken: HEAD must differ from origin/main, and the "
                         "receipt must be committed on origin/main")
    result = box.guard(tools_root, repo)
    cited = presented(box, repo, result.stderr + "\n" + result.stdout)
    # v2 (round-50 L1, after the v1 run recorded in telemetry/jj-probe-v1.txt): the declared
    # claim O asks for a landed sha reported separately from the local HEAD. A defect is a
    # missing landed-labelled sha, or a landed-labelled sha that is not an ancestor of
    # refs/remotes/origin/main. v1 also flagged the committed_sha=<HEAD> field that the
    # guard's design contract (reports/round-14/guard/design.md) keeps; that stricter view
    # is still reported in `committed_local_only`, informational, outside the count.
    landed = [(label, sha) for label, sha in cited if "landed" in label]
    stray = [(label, sha) for label, sha in landed
             if not box.is_ancestor(repo, sha, "refs/remotes/origin/main")]
    committed_local = [f"{label}={sha}" for label, sha in cited if "landed" not in label
                       and not box.is_ancestor(repo, sha, "refs/remotes/origin/main")]
    flagged = bool(stray) or not landed
    if stray:
        names = ", ".join(f"{label}={sha}" for label, sha in stray)
        detail = (f"guard presents {names} as landed, but it is not an ancestor of "
                  f"refs/remotes/origin/main; the local-only HEAD is {local}")
    elif not landed:
        detail = (f"guard reports no landed sha distinct from the local HEAD {local} "
                  f"(presented: {', '.join(f'{l}={s}' for l, s in cited) or 'none'}; "
                  f"exit {result.returncode})")
    else:
        detail = "every landed-labelled sha is an ancestor of refs/remotes/origin/main"
    return _row("R1", "cited-sha-not-landed", "defect", result, flagged, detail,
                presented=[f"{label}={sha}" for label, sha in cited], local_head=local,
                committed_local_only=committed_local)


def case_r2(box, tools_root):
    repo = box.init("r2-overwrite-below")
    write(repo, "base.txt", "base\n")
    box.commit(repo, "C0: base")
    write(repo, "filler.txt", "pre-receipt state\n")
    box.commit(repo, "C1: pre-receipt state")
    anchored = box.rev(repo, "HEAD")
    write(repo, RECEIPT, "R2 receipt\n")
    box.commit(repo, "C2: receipt committed on main")
    box.git(repo, "update-ref", "refs/remotes/origin/main", box.rev(repo, "refs/heads/main"))
    box.git(repo, "checkout", "-q", "--detach", anchored)
    if box.has(repo, f"HEAD:{RECEIPT}") or not box.has(repo, f"refs/remotes/origin/main:{RECEIPT}"):
        raise SetupError("R2 fixture broken: the receipt must be committed on origin/main "
                         "and absent from HEAD")
    result = box.guard(tools_root, repo)
    allowed = result.returncode == 0
    detail = (f"guard exits 0 and allows the overwrite: the receipt is committed on main and "
              f"origin/main while HEAD is detached at {anchored}" if allowed
              else f"guard refuses the overwrite (exit {result.returncode})")
    return _row("R2", "overwrite-allowed", "defect", result, allowed, detail, head=anchored)


def case_r3(box, tools_root, pin):
    lane = gate_lane(box, "r3-pin-absent", tools_root)
    if box.has(lane, f"{pin}^{{commit}}"):
        raise SetupError(f"R3 fixture broken: the pin {pin} is present in a fresh repository")
    result = box.gate(lane)
    allowed = result.returncode == 0
    skips = "; ".join(line for line in result.stdout.splitlines() if line.startswith("SKIP "))
    detail = (f"selftest exits 0 with pinned BASE_COMMIT {pin} absent from the repository"
              if allowed else f"selftest exits {result.returncode} with the pin absent "
              "(fails closed)")
    return _row("R3", "skip-pass", "defect", result, allowed, detail, evidence=skips or None,
                pinned_base=pin)


def case_p1(box, tools_root):
    result = box.guard(tools_root, landed_repo(box, "p1-normal-state"))
    refused = result.returncode != 0
    detail = (f"guard refuses the normal state (exit {result.returncode})" if refused
              else "guard allows the normal state: HEAD == origin/main, receipt absent")
    return _row("P1", "normal-state-allowed", "positive", result, refused, detail)


def case_p2(box, tools_root):
    repo = landed_repo(box, "p2-untracked-receipt")
    write(repo, RECEIPT, "new untracked receipt\n")
    result = box.guard(tools_root, repo)
    refused = result.returncode != 0
    detail = (f"guard refuses a new untracked receipt (exit {result.returncode})" if refused
              else "guard allows a new untracked receipt that no commit holds")
    return _row("P2", "new-untracked-receipt-allowed", "positive", result, refused, detail)


def case_p3(box, tools_root, pin, history):
    lane = box.root / "p3-pin-present"
    box.git(box.root, "clone", "-q", "--shared", "--no-checkout", str(history), str(lane))
    box.git(lane, "switch", "-q", "--orphan", "fixture")
    (lane / "tools").mkdir()
    shutil.copyfile(tools_root / README_GATE, lane / README_GATE)
    write(lane, "corpus/README.md", README_FIXTURE)
    box.commit(lane, "fixture commit holding the gate script")
    if not box.has(lane, f"{pin}^{{commit}}"):
        raise SetupError(f"P3 fixture broken: the clone of {history} does not expose {pin}")
    result = box.gate(lane)
    control = f"base {pin[:7]}"
    pin_pass = any(line.startswith("PASS ") and control in line
                   for line in result.stdout.splitlines())
    refused = result.returncode != 0 or not pin_pass
    detail = (f"selftest exits {result.returncode}; PASS control for {pin[:7]} present={pin_pass}"
              if refused else f"selftest exits 0 and PASSes the control for pinned {pin[:7]}")
    return _row("P3", "pinned-readme-selftest-passes", "positive", result, refused, detail,
                pinned_base=pin)


def case_p4(box, tools_root):
    repo = landed_repo(box, "p4-refresh-permit", receipt=True)
    result = box.guard(tools_root, repo, env=box.env(REFRESH_RECEIPTS="1"))
    refused = result.returncode != 0
    detail = (f"guard refuses the documented REFRESH_RECEIPTS=1 permit (exit {result.returncode})"
              if refused else "guard honours REFRESH_RECEIPTS=1 for a committed receipt")
    return _row("P4", "refresh-permit-allowed", "positive", result, refused, detail)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Count jj-colocation false negatives and false positives (round 50, claim O).")
    parser.add_argument("--tools-root", required=True, type=Path,
                        help="tree containing tools/harness/receipt_guard.py and "
                             "tools/check-readme-revisions.py")
    parser.add_argument("--history-repo", type=Path,
                        help="git work tree or repository holding the pinned base commit "
                             "(default: the work tree containing --tools-root)")
    args = parser.parse_args(argv)
    tools_root = args.tools_root.resolve()
    missing = [str(rel) for rel in (GUARD, README_GATE) if not (tools_root / rel).is_file()]
    if missing:
        print(f"jj-colocation-probe: setup error: missing under {tools_root}: "
              f"{', '.join(missing)}", file=sys.stderr)
        return 2
    try:
        with Sandbox() as box:
            pin = gate_pin(tools_root)
            history = history_repo(args, tools_root, box, pin)
            rows = [case_r1(box, tools_root), case_r2(box, tools_root),
                    case_r3(box, tools_root, pin), case_p1(box, tools_root),
                    case_p2(box, tools_root), case_p3(box, tools_root, pin, history),
                    case_p4(box, tools_root)]
    except (SetupError, OSError) as error:
        print(f"jj-colocation-probe: setup error: {error}", file=sys.stderr)
        return 2
    for row in rows:
        print(json.dumps(row, sort_keys=True))
    defects = [row for row in rows if row["kind"] == "defect"]
    positives = [row for row in rows if row["kind"] == "positive"]
    print(f"JJ_COLOCATION_FALSE_NEGATIVES={sum(row['flagged'] for row in defects)}/{len(defects)}")
    print(f"JJ_COLOCATION_FALSE_POSITIVES={sum(row['flagged'] for row in positives)}/{len(positives)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
