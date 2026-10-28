#!/usr/bin/env python3
"""Build a scratch fixture repo for the QUALITY 30 check and print its commits.

The fixture is a *shape* fixture: it plants each pair's stated_text on the line
its stated_at names, rewrites every observe_cmd into the criterion's grammar
(`git -C <repo> <sub> ... <rev> -- <path>`), turns every `rederive` into the
same argv, and moves L76-13's statement into the ANNOTATE allowlist (the r76
statement lives in a knowledge entry, which the r76 set excludes).  It grades
the checker's limbs, not the truth of the r76 corrections.

Usage: make-fixture.py <fixture-dir> <source-ledger.json> <annotate-allow,..>
Environment: TMPDIR must be set; nothing is written outside <fixture-dir>.
"""
import json
import os
import subprocess
import sys


def git(repo, *args, **kw):
    p = subprocess.run(["git", "-C", repo] + list(args), capture_output=True,
                       text=True, **kw)
    if p.returncode != 0:
        raise SystemExit("git %s failed: %s" % (" ".join(args), p.stderr.strip()))
    return p.stdout


def commit(repo, msg):
    ident = ["-c", "user.name=quality30-fixture", "-c",
             "user.email=quality30@fixture.invalid"]
    git(repo, *ident, "add", "-A")
    git(repo, *ident, "commit", "-q", "-m", msg)
    return git(repo, "rev-parse", "HEAD").strip()


def main():
    dest, src, allow = sys.argv[1], sys.argv[2], sys.argv[3]
    annotate = allow.split(",")
    os.makedirs(dest, exist_ok=True)
    git(dest, "init", "-q")
    top = git(dest, "rev-parse", "--show-toplevel").strip()
    assert os.path.realpath(top) == os.path.realpath(dest), (top, dest)

    led = json.load(open(src, encoding="utf-8"))
    pairs = led["pairs"]

    # 1. stated_text sites: path -> {line: text}
    sites = {}
    for p in pairs:
        path, _, line = (p.get("stated_at") or "").rpartition(":")
        if p["id"] == "L76-13":            # moved into the r76 allowlist
            path, line = "corpus/lessons/round-75.md", "8"
        sites.setdefault(path, {}).setdefault(int(line), []).append(p.get("stated_text") or "")

    # 2. operand paths every observe_cmd names (content need not be real text)
    operands = set()
    for p in pairs:
        cmd = p.get("observe_cmd") or []
        for a in cmd:
            if a == "--" or a.startswith("-") or len(a) == 40:
                continue
            if "/" in a or a.endswith((".md", ".txt", ".json", ".py", ".sh")):
                operands.add(a)

    for path in sorted(set(sites) | operands):
        full = os.path.join(dest, path)
        os.makedirs(os.path.dirname(full) or dest, exist_ok=True)
        want = sites.get(path, {})
        if want:
            n = max(want)
            lines = ["line %d" % i for i in range(1, n + 1)]
            for ln, texts in want.items():
                lines[ln - 1] = " ".join(texts)   # two pairs may cite one line
            open(full, "w", encoding="utf-8").write("\n".join(lines) + "\n")
        else:
            open(full, "w", encoding="utf-8").write("fixture operand\n")

    open(os.path.join(dest, "LOG.md"), "w", encoding="utf-8").write(
        "line 1\nline 2\nline 3\n")

    base = commit(dest, "fixture base")

    # 3. rewrite the ledger into the criterion's grammar at the fixture base
    fixed = json.loads(json.dumps(led))
    fixed["base"] = base
    for p in fixed["pairs"]:
        cmd = p["observe_cmd"]
        if os.path.basename(cmd[0]) == "git":
            cmd = ["git", "-C", dest] + cmd[1:]
        cmd = [(base + a[len(led["base"]):]) if a.startswith(led["base"]) else a
               for a in cmd]
        p["observe_cmd"] = cmd
        p["rederive"] = list(cmd)
        if p["id"] == "L76-13":
            p["stated_at"] = "corpus/lessons/round-75.md:8"

    def write(name, ledger):
        full = os.path.join(dest, name)
        os.makedirs(os.path.dirname(full) or dest, exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            json.dump(ledger, fh, ensure_ascii=False, indent=1, sort_keys=True)
            fh.write("\n")

    write("reports/round-76/ledger.json", fixed)

    # 4. single-defect mutants, each a full ledger copy with one edit
    def mutant(name, edit):
        m = json.loads(json.dumps(fixed))
        by = {p["id"]: p for p in m["pairs"]}
        edit(by, m)
        write("mutants/%s.json" % name, m)

    mutant("m1-stated-at-set",
           lambda by, m: by["L76-13"].__setitem__(
               "stated_at",
               "corpus/knowledge/myth-symbol/narrative-structure-frameworks.md:1"))
    mutant("m2-stated-text-absent",
           lambda by, m: by["L76-19"].__setitem__(
               "stated_text", "S892's window (`chars=4097 before=999`)"))
    mutant("m3-rederive-string",
           lambda by, m: by["L76-19"].__setitem__(
               "rederive",
               "git grep -h -E ^window: chars= %s -- "
               "reports/round-75/evidence/S892.txt" % base))
    mutant("m4-no-c",
           lambda by, m: by["L76-01"].__setitem__(
               "observe_cmd", ["git"] + by["L76-01"]["observe_cmd"][3:]))
    mutant("m5-rev-after-dd",
           lambda by, m: by["L76-01"].__setitem__(
               "observe_cmd",
               ["git", "-C", dest, "grep", "-c", "-E", "^", "--",
                "reports/round-75/claims.json", base]))
    mutant("m6-interpreter",
           lambda by, m: by["L76-01"].__setitem__(
               "observe_cmd", ["python3", "-c", "print('present')"]))
    mutant("m7-pattern-split",
           lambda by, m: by["L76-19"].__setitem__(
               "observe_cmd",
               ["git", "-C", dest, "grep", "-h", "-E", "^window:", "chars=",
                base, "--", "reports/round-75/evidence/S892.txt"]))
    mutant("m8-dead-pin",
           lambda by, m: by["L76-01"].__setitem__(
               "observe_cmd",
               [("f" * 40) if a == base else a
                for a in by["L76-01"]["observe_cmd"]]))
    mutant("m9-shell-string",
           lambda by, m: by["L76-01"].__setitem__(
               "observe_cmd", "git grep -c -E ^ %s -- reports/round-75/claims.json"
               % base))

    # 5. a two-pair ledger for the run limb (--execute), plus its mutants

    def exec_pair(pid, stated_at, text, argv, parse, want):
        return {"id": pid, "disposition": "ANNOTATE", "stated_at": stated_at,
                "stated_text": text, "observe_cmd": argv, "rederive": list(argv),
                "parse": parse, "expected_after": want}

    ex = {"round": 76, "claim": "Ca", "axis": "calibration", "base": base,
          "status": "run-limb fixture", "pairs": [
              exec_pair("X01", "LOG.md:3", "line 3",
                        ["git", "-C", dest, "grep", "-h", "-o", "-E",
                         "^line 3$", base, "--", "LOG.md"], "^(line 3)$",
                        "line 3"),
              exec_pair("X02", "LOG.md:1", "line 1",
                        ["git", "-C", dest, "grep", "-c", "-E", "^",
                         base, "--", "LOG.md"], "count-presence", "present")]}
    write("exec/ledger.json", ex)
    m = json.loads(json.dumps(ex))
    m["pairs"][0]["expected_after"] = "line 4"
    write("exec/m1-wrong-token.json", m)
    m = json.loads(json.dumps(ex))
    m["pairs"][0]["observe_cmd"] = ["git", "-C", dest, "grep", "-E",
                                   "^no-such-line$", base, "--", "LOG.md"]
    write("exec/m2-exit-1.json", m)

    head = commit(dest, "fixture ledgers: green plus single-defect mutants")
    print("FIXTURE %s" % dest)
    print("BASE %s" % base)
    print("HEAD %s" % head)


if __name__ == "__main__":
    main()
