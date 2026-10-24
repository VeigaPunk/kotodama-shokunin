#!/usr/bin/env python3
"""Run the REAL accept-c.py (lane bytes, unmodified) against each entry mutant
in a throwaway clone of the lane at BASE. Never touches lane files."""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE = "99fae3085ec858446df00c2b294748f635cb6c45"
COUNTER = os.path.join(LANE, "reports/round-68/accept-c.py")
HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
ENTRY = "corpus/knowledge/culture-material/hair-grooming-codes.md"
LEDGER = "reports/round-68/dispositions/dedup-ledger.tsv"
VARIANTS = ["entry-base.md", "entry-m1-no-topic.md", "entry-m2-h3.md",
            "entry-m3-251lines.md", "entry-m4-foreign-cite.md",
            "entry-m5-uncited-bullet.md", "entry-m6-topic-in-fence.md",
            "entry-m7-bare-foreign-id.md",
            "entry-m8-citations-in-comment.md"]

ENV = dict(os.environ)
ENV.update({"GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_AUTHOR_NAME": "mut", "GIT_AUTHOR_EMAIL": "m@i",
            "GIT_COMMITTER_NAME": "mut", "GIT_COMMITTER_EMAIL": "m@i"})


def sh(args, cwd=None):
    return subprocess.run(args, cwd=cwd, env=ENV, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def main():
    fx = "/tmp/r68-mut-entry/fx"
    shutil.rmtree("/tmp/r68-mut-entry", ignore_errors=True)
    os.makedirs(RESULTS, exist_ok=True)
    r = sh(["git", "clone", "--no-local", "-q", LANE, fx])
    if r.returncode:
        print("CLONE FAILED:", r.stdout)
        return 2
    r = sh(["git", "-C", fx, "checkout", "-q", "-B", "main", BASE])
    if r.returncode:
        print("CHECKOUT FAILED:", r.stdout)
        return 2
    reg_rows = open(os.path.join(HERE, "registry-rows-S833-S856.md"),
                    encoding="utf-8").read()
    counter_sha = hashlib.sha256(open(COUNTER, "rb").read()).hexdigest()
    summary = {"counter_sha256": counter_sha, "base": BASE, "runs": {}}
    for variant in VARIANTS:
        sh(["git", "-C", fx, "reset", "-q", "--hard", BASE])
        sh(["git", "-C", fx, "clean", "-qfdx"])
        entry_text = open(os.path.join(HERE, variant), encoding="utf-8").read()
        with open(os.path.join(fx, ENTRY), "w", encoding="utf-8") as fh:
            fh.write(entry_text)
        with open(os.path.join(fx, "corpus/SOURCES.md"), "a",
                  encoding="utf-8") as fh:
            fh.write(reg_rows)
        os.makedirs(os.path.dirname(os.path.join(fx, LEDGER)), exist_ok=True)
        with open(os.path.join(fx, LEDGER), "w", encoding="utf-8") as fh:
            fh.write("# fixture ledger - no rulings\n")
        sh(["git", "-C", fx, "add", "-A"])
        c = sh(["git", "-C", fx, "commit", "-qm", f"fixture {variant}"])
        if c.returncode:
            print(f"{variant}: COMMIT FAILED {c.stdout}")
            continue
        lands = sh(["git", "-C", fx, "rev-parse", "main"]).stdout.strip()
        run = sh([sys.executable, COUNTER, "--root", fx, "--lands", lands])
        out = run.stdout
        with open(os.path.join(RESULTS, variant.replace(".md", ".log")), "w",
                  encoding="utf-8") as fh:
            fh.write(out)
        legs = {m[0]: (m[1], m[2]) for m in
                re.findall(r"^(\w+) (PASS|FAIL) (.*)$", out, re.M)}
        verdict = re.search(r"^ACCEPT-C-68: (PASS|FAIL)$", out, re.M)
        print(f"=== {variant} lands={lands[:8]} rc={run.returncode} "
              f"verdict={verdict.group(1) if verdict else '?'} "
              f"fails={[k for k, v in legs.items() if v[0] == 'FAIL']}")
        for name in ("FILE", "SET", "ROWS", "ONEID", "RESTATE"):
            print(f"    {name}: {legs.get(name, ('?', '?'))}")
        summary["runs"][variant] = {
            "lands": lands, "rc": run.returncode,
            "verdict": verdict.group(1) if verdict else None,
            "fails": [k for k, v in legs.items() if v[0] == "FAIL"],
            "legs": {k: v[0] for k, v in legs.items()},
            "entry_sha256": hashlib.sha256(entry_text.encode()).hexdigest(),
            "entry_lines": len(entry_text.splitlines()),
        }
    with open(os.path.join(RESULTS, "summary.json"), "w",
              encoding="utf-8") as fh:
        json.dump(summary, fh, indent=1, sort_keys=True)
    print("summary:", os.path.join(RESULTS, "summary.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
