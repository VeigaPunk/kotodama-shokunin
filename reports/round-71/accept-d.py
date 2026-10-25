#!/usr/bin/env python3
r"""Round-71 depth acceptance counter — claim D (NEW counter, V70-6).

The frozen round-69 counter `reports/round-69/accept-d.py` (claim D2) proves
its do-nothing fixture by `git show 793f797:SKILL.md` and silently falls back
to the live SKILL.md when `.git` is absent. On an exported tree (`git
archive`) that fallback reports a FALSE RED: `DO-NOTHING FIXTURE: PASS
(unexpected)`, `SELFTEST: 1/2`, exit 1 — indistinguishable from a genuine
failure. This counter adds the declared no-git path:

  * with `.git` present — the frozen selftest runs unchanged (SELFTEST: 2/2,
    exit 0);
  * without `.git` — prints `SELFTEST: COULD-NOT-EVALUATE (no git)` and exits
    2, so a missing object store is never graded as a craft failure;
  * the frozen data predicate `reports/round-69/accept-d.py --root .` stays
    untouched and must still print `ACCEPT-D-69: PASS legs=8/8` exit 0.

The frozen counter's bytes are NOT modified (no rewrite of any filed round).
"""

import argparse
import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(HERE))
FROZEN = os.path.join(LANE, "reports", "round-69", "accept-d.py")

SPEC = "SELFTEST: COULD-NOT-EVALUATE (no git)"


def _load_frozen():
    """Import the frozen round-69 counter module without executing main()."""
    spec = importlib.util.spec_from_file_location("accept_d_69_frozen", FROZEN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _git_available():
    """A working repo: repo-relative git commands succeed.

    Only a genuine absence of the object store (no `.git` entry in the lane,
    and git failing) is graded as `no git`; a git failure that is NOT a
    missing-store absence (e.g. a GIT_DIR override pointing nowhere) is an
    environment error, and is still graded COULD-NOT-EVALUATE — never a
    craft red.
    """
    try:
        rc = subprocess.call(
            ["git", "-C", LANE, "rev-parse", "--is-inside-work-tree"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return rc == 0
    except Exception:
        return False


def _git_error_text():
    try:
        out = subprocess.check_output(
            ["git", "-C", LANE, "rev-parse", "--git-dir"],
            stderr=subprocess.STDOUT, text=True)
        return (out or "").strip()
    except subprocess.CalledProcessError as exc:
        return (exc.output or "").strip() or "git unavailable"
    except Exception as exc:
        return str(exc)


def selftest():
    mod = _load_frozen()
    if not _git_available():
        if os.path.exists(os.path.join(LANE, ".git")):
            print("SELFTEST: COULD-NOT-EVALUATE (git unavailable: %s)"
                  % _git_error_text())
        else:
            print(SPEC)
        return 2
    return mod.selftest()


def main():
    ap = argparse.ArgumentParser(description="round-71 depth counter (V70-6)")
    ap.add_argument("--root", default=".",
                    help="lane root (graded only by the frozen counter)")
    ap.add_argument("--lands", default=None,
                    help="reserved: lands revision for receipt protocol parity; "
                         "the frozen round-69 counter grades the tree itself "
                         "and does not consume this flag")
    ap.add_argument("--selftest", action="store_true",
                    help="run the selftest (no-git guard)")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    # Data predicate: delegate to the frozen counter unchanged. Forward only
    # the flags the frozen argparse understands (--root), never our reserved
    # extras (--lands), so its exit 0/1 and output semantics are byte-identical.
    mod = _load_frozen()
    sys.argv = [sys.argv[0], "--root", args.root]
    return mod.main()


if __name__ == "__main__":
    sys.exit(main())
