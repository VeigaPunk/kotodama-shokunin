#!/usr/bin/env python3
"""Scratch-discipline probe for accept-c.py (round 77).

Builds one clean fixture lane under $HYAKU_SCRATCH (git init + base/freeze/lands,
toplevel asserted) and runs the counter twice:

  1. --work /tmp/<probe>   -> refused exit 2, FAIL verdict, no LEG line, no dir
  2. --work <scratch>/ok   -> graded PASS 15/15, every clone under that work dir

Also prints _scratch_root's resolution for the documented sources.
"""
import importlib.util
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    spec = importlib.util.spec_from_file_location(
        "accept_c", os.path.join(HERE, "accept-c.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    scratch = os.environ.get("HYAKU_SCRATCH") or ""
    if not scratch:
        print("ERROR: set HYAKU_SCRATCH to a scratch root", file=sys.stderr)
        return 2
    root = tempfile.mkdtemp(dir=scratch)
    case = os.path.join(root, "clean")
    os.makedirs(case)
    paths = m._st_build(case, {})
    probe = os.path.join(os.sep, "tmp", "r77-scratch-probe")
    work_ok = os.path.join(root, "work")
    base_cmd = [sys.executable, "-B", os.path.join(HERE, "accept-c.py"),
                "--root", paths["root"], "--lands", paths["lands"],
                "--freeze", paths["freeze"], "--fleet-root", paths["fleet"]]

    r = subprocess.run(base_cmd + ["--work", probe],
                       capture_output=True, text=True)
    leg_lines = [l for l in r.stdout.splitlines() if l.startswith("LEG ")]
    print("system-tmp probe: exit=%d leg-lines=%d dir-created=%s"
          % (r.returncode, len(leg_lines), os.path.exists(probe)))
    print("  verdict: %s"
          % next((l for l in r.stdout.splitlines()
                  if l.startswith("ACCEPT-C-77:")), "-"))
    print("  stderr: %s" % r.stderr.strip())

    r = subprocess.run(base_cmd + ["--work", work_ok],
                       capture_output=True, text=True)
    leg_lines = [l for l in r.stdout.splitlines() if l.startswith("LEG ")]
    print("operator-work probe: exit=%d leg-lines=%d work-created=%s"
          % (r.returncode, len(leg_lines), os.path.isdir(work_ok)))
    print("  verdict: %s"
          % next((l for l in r.stdout.splitlines()
                  if l.startswith("ACCEPT-C-77:")), "-"))
    print("  materialized line: %s"
          % next((l for l in r.stdout.splitlines()
                  if l.startswith("# materialized:")), "-")[:180])

    class A:
        work = None
    saved = {k: os.environ.get(k) for k in ("HYAKU_SCRATCH", "TMPDIR")}
    for k in saved:
        os.environ.pop(k, None)
    print("no source -> %s" % m._scratch_root(A()))
    os.environ["TMPDIR"] = os.path.join(os.sep, "tmp")
    print("system TMPDIR -> %s (forbidden=%s)"
          % (m._scratch_root(A()), m._forbidden_scratch(os.path.join(os.sep, "tmp"))))
    for k, v in saved.items():
        if v is not None:
            os.environ[k] = v
    return 0


if __name__ == "__main__":
    sys.exit(main())
