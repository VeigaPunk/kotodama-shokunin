#!/usr/bin/env python3
"""ACCEPT-C-67 mutation probe: 6 single-leg mutants vs 6 planted defects.

For each (mutant, defect) pair the harness plants a defect that the pristine
frozen counter must reject, commits it in a private fixture clone, then runs
the pristine counter and the mutant counter over the same bytes.

  killed   -> mutant still rejects the defect (leg did its job)
  SURVIVED -> mutant prints PASS on bytes carrying the planted defect
  inconclusive -> pristine did not reject the defect (fixture problem)

Nothing here writes outside stage/mut-c/ or the lane repo; the fixture clone
is a private copy of .scratch/eval-base.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(HERE, "repoc")
ORIG = os.path.join(HERE, "accept-c.orig.py")
BASE = "ad5b52b0ab5691358cd38718ab75649dc9916f9a"
ENTRY = "corpus/knowledge/culture-material/medicine-healing-codes.md"
REG = "corpus/SOURCES.md"

MUTANTS = [
    ("m1_oneid_ge1.py", "ONEID", "count != 1", "count < 1",
     "one citation required -> at least one"),
    ("m2_restate_inq_lt2.py", "RESTATE", "if inq < 3 or cov >= 0.8",
     "if inq < 2 or cov >= 0.8", "quote must be restated in >=3 words -> >=2"),
    ("m3_append_unbounded.py", "APPEND", "not missing_old and not extra_ids and not mutable_bad",
     "not missing_old and not mutable_bad", "appended ids bounded -> unbounded"),
    ("m4_capture_skipped.py", "CAPTURE", 'leg("CAPTURE", not cap_bad',
     'leg("CAPTURE", True', "capture/target equality enforced -> skipped"),
    ("m5_stamp_equal_dropped.py", "STAMP", "and mv_rev == lands and bool(",
     "and bool(", "evaluated == stamped enforced -> equality dropped"),
    ("m6_rows_tier_c.py", "ROWS", 'if c[3] not in ("A", "B"):',
     'if c[3] not in ("A", "B", "C"):', "tier A/B -> A/B/C (tier inflation)"),
]

DEFECTS = {
    # name: (mutant, setup callable/description, lands override or None)
    "d1_oneid_double_cite": ("m1_oneid_ge1.py", "dup_cite", None),
    "d2_restate_two_words": ("m2_restate_inq_lt2.py", "restate_two", None),
    "d3_append_extra_row": ("m3_append_unbounded.py", "extra_row", None),
    "d4_capture_missing": ("m4_capture_skipped.py", "no_capture", None),
    "d5_moved_worktree": ("m5_stamp_equal_dropped.py", "none", BASE),
    "d6_tier_inflated": ("m6_rows_tier_c.py", "tier_c", None),
}


def sh(*args, **kw):
    return subprocess.run(args, cwd=kw.pop("cwd", HERE), capture_output=True,
                          text=True, **kw)


def git(*args):
    return sh("git", "-C", REPO, *args)


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def fixture_head():
    return git("rev-parse", "main").stdout.strip()


def amend():
    return sh("git", "-C", REPO, "-c", "user.name=mut-harness",
              "-c", "user.email=mut@local", "commit", "--no-verify",
              "--amend", "--no-edit")


def read(p):
    return open(os.path.join(REPO, p), encoding="utf-8").read()


def writep(p, text):
    with open(os.path.join(REPO, p), "w", encoding="utf-8") as fh:
        fh.write(text)


def d_dup_cite():
    text = read(ENTRY)
    extra = ("- Balm, resin, salve: duplicate harness citation for (S805) kept "
             "for the ONEID probe.\n")
    text = text.replace("## Notes", extra + "\n## Notes", 1)
    writep(ENTRY, text)


def d_restate_two():
    text = read(ENTRY)
    old = ("- Balm, resin, salve: harness teaching line 1 for (S805); "
           "valued by healers beside tincture and decoction.")
    new = ("- Balm, resin, valued by healers beside tincture and decoction "
           "(S805).")
    assert old in text
    writep(ENTRY, text.replace(old, new, 1))


def d_extra_row():
    text = read(REG)
    row = ("| S900 | Harness smuggled row — https://medharness99.example.org/item/99 "
           "| docs | A | smuggled scope | \"balm resin salve myrrh\" | tincture "
           f"decoction poultice fumigation plaster cautery | mined | 2026-10-24 | 180d | {ENTRY} |")
    writep(REG, text.rstrip("\n") + "\n" + row + "\n")


def d_no_capture():
    text = read(REG)
    line = next(l for l in text.splitlines() if l.startswith("| S805 |"))
    new = re.sub(r" ; https://web\.archive\.org/web/\d{14}id_/\S+", "", line)
    assert new != line
    writep(REG, text.replace(line, new, 1))


def d_tier_c():
    text = read(REG)
    line = next(l for l in text.splitlines() if l.startswith("| S805 |"))
    new = line.replace("| docs | A |", "| docs | C |", 1)
    assert new != line
    writep(REG, text.replace(line, new, 1))


SETUPS = {"dup_cite": d_dup_cite, "restate_two": d_restate_two,
          "extra_row": d_extra_row, "no_capture": d_no_capture,
          "tier_c": d_tier_c, "none": lambda: None}


def run(counter, lands):
    return subprocess.run([sys.executable, "-B", counter, "--root", REPO,
                           "--lands", lands], cwd=HERE, capture_output=True,
                          text=True)


def legs(out):
    found = {}
    for line in out.splitlines():
        m = re.match(r"^([A-Z]+) (PASS|FAIL) (.*)$", line)
        if m:
            found[m.group(1)] = m.group(2)
    return found


def main():
    good = fixture_head()
    print(f"# fixture commit F={good}")
    # 1. specificity: pristine PASS on defect-free bytes
    base_run = run(ORIG, good)
    print(f"# pristine baseline exit={base_run.returncode} "
          f"verdict={base_run.stdout.strip().splitlines()[-1]}")
    # 2. build mutants
    orig_text = open(ORIG, encoding="utf-8").read()
    built = []
    for fname, leg, old, new, desc in MUTANTS:
        assert orig_text.count(old) == 1, (fname, orig_text.count(old))
        mpath = os.path.join(HERE, fname)
        with open(mpath, "w", encoding="utf-8") as fh:
            fh.write(orig_text.replace(old, new, 1))
        built.append((fname, leg, old, new, desc, sha(mpath)))
    results = []
    for defect, (mf, setup, lands_override) in DEFECTS.items():
        git("reset", "--hard", good)
        SETUPS[setup]()
        add = git("add", "-A")
        am = amend()
        assert am.returncode == 0, am.stderr
        lands = fixture_head() if lands_override is None else lands_override
        pristine = run(ORIG, lands)
        mutant = run(os.path.join(HERE, mf), lands)
        plegs, mlegs = legs(pristine.stdout), legs(mutant.stdout)
        target = next(l for f, l, *_ in built if f == mf)
        pverdict = pristine.stdout.strip().splitlines()[-1]
        mverdict = mutant.stdout.strip().splitlines()[-1]
        if plegs.get(target) != "FAIL":
            verdict = "INCONCLUSIVE"
        elif mlegs.get(target) == "PASS" or mverdict.endswith("PASS"):
            verdict = "SURVIVED"
        else:
            verdict = "killed"
        changed = sorted(k for k in set(plegs) | set(mlegs)
                         if plegs.get(k) != mlegs.get(k))
        results.append({
            "defect": defect, "mutant": mf, "leg": target,
            "pristine_leg": plegs.get(target), "mutant_leg": mlegs.get(target),
            "pristine_verdict": pverdict, "mutant_verdict": mverdict,
            "legs_changed": changed, "lands": lands, "verdict": verdict,
            "pristine_stdout": pristine.stdout, "mutant_stdout": mutant.stdout,
        })
    # restore
    git("reset", "--hard", good)
    out = {"fixture": good, "pristine_sha": sha(ORIG),
           "mutants": [{"file": f, "leg": l, "from": o, "to": n, "desc": d,
                        "sha": s} for f, l, o, n, d, s in built],
           "results": results}
    with open(os.path.join(HERE, "results.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)

    lines = [f"# mut-c results — ACCEPT-C-67 counter mutants",
             f"# fixture clone: private copy of .scratch/eval-base at {BASE}",
             f"# fixture commit F={good} (synthetic data; every leg PASS)",
             f"# pristine counter accept-c.orig.py sha256={sha(ORIG)} "
             f"(== lane reports/round-67/accept-c.py 3e5f1a58...)",
             f"# baseline pristine run: {base_run.stdout.strip().splitlines()[-1]} "
             f"exit={base_run.returncode}", ""]
    for r in results:
        lines.append(f"## {r['defect']} vs {r['mutant']} (leg {r['leg']})")
        lines.append(f"lands={r['lands']}")
        lines.append(f"pristine {r['leg']} {r['pristine_leg']} -> "
                     f"{r['pristine_verdict']}")
        lines.append(f"mutant   {r['leg']} {r['mutant_leg']} -> "
                     f"{r['mutant_verdict']}")
        lines.append(f"legs_changed={r['legs_changed']}")
        lines.append(f"VERDICT {r['verdict']}")
        lines.append("--- pristine stdout ---")
        lines.append(r["pristine_stdout"].rstrip())
        lines.append("--- mutant stdout ---")
        lines.append(r["mutant_stdout"].rstrip())
        lines.append("")
    with open(os.path.join(HERE, "results.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\n".join(f"{r['defect']:24s} {r['leg']:8s} pristine={r['pristine_leg']} "
                    f"mutant={r['mutant_leg']} {r['verdict']}" for r in results))
    print(f"# pristine counter restored sha256={sha(ORIG)}")


if __name__ == "__main__":
    main()
