#!/usr/bin/env python3
"""Mutation harness for reports/round-65/accept-c.py (round 65, seat MutCounterC).

Runs one counter script against one fixture root with the *same* fake git layer
for the original and every mutant, so the only difference between runs is the
mutated bytes of the counter:

  python3 harness.py <counter.py> <root> <base_registry> <base_locator> <entry|empty>

Fake git supplies, without creating any repository:
  git show <BASE>:corpus/SOURCES.md   -> <base_registry> bytes
  git show <BASE>:reports/round-61/reopen-quote.py -> <base_locator> bytes
  git diff --name-only ...            -> entry path, or nothing (red)

All non-git subprocesses (locator / sweep / cited-lines stubs) run for real.
"""
import contextlib
import importlib.util
import io
import sys
import subprocess

REAL_RUN = subprocess.run
ENTRY = "corpus/knowledge/culture-material/games-play-sport-contests.md"


def load(path):
    spec = importlib.util.spec_from_file_location("counter_under_test", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run(script, root, base_registry, base_locator, diff_mode):
    mod = load(script)
    base_reg = open(base_registry, "rb").read()
    base_loc = open(base_locator, "rb").read()
    diff_paths = [ENTRY] if diff_mode == "entry" else []

    def fake_run(args, **kw):
        if args and args[0] == "git":
            argl = list(args)
            if "show" in argl:
                spec = argl[argl.index("show") + 1]
                path = spec.split(":", 1)[1]
                if path == "corpus/SOURCES.md":
                    return subprocess.CompletedProcess(args, 0, base_reg, b"")
                if path == "reports/round-61/reopen-quote.py":
                    return subprocess.CompletedProcess(args, 0, base_loc, b"")
                return subprocess.CompletedProcess(args, 1, b"", b"missing")
            if "diff" in argl:
                out = ("\n".join(diff_paths) + "\n").encode() if diff_paths else b""
                return subprocess.CompletedProcess(args, 0, out, b"")
        return REAL_RUN(args, **kw)

    mod.subprocess.run = fake_run
    old_argv = sys.argv
    sys.argv = [script, "--root", root]
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(io.StringIO()):
            rc = mod.main()
    finally:
        mod.subprocess.run = REAL_RUN
        sys.argv = old_argv
    return rc, buf.getvalue()


if __name__ == "__main__":
    script, root, base_reg, base_loc, diff_mode = sys.argv[1:6]
    rc, out = run(script, root, base_reg, base_loc, diff_mode)
    sys.stdout.write(out)
    print(f"harness_exit={rc}")
