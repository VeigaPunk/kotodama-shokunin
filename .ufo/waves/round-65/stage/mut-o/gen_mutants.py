#!/usr/bin/env python3
"""Generate the five FULL/MUTEX/FRAG mutants of accept-o.py (each one literal,
single-occurrence replacement) and verify the replacement count."""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PRISTINE = os.path.join(HERE, "accept-o.pristine.py")

MUTANTS = {
    "m1_full_only_gains_frag": (
        'run_legs_all = sorted(set(CORE) | set(EDGE) | {"TOOL", "DRIP", "MUT"})',
        'run_legs_all = sorted(set(CORE) | set(EDGE) | {"TOOL", "DRIP", "MUT", "FRAG"})',
    ),
    "m2_suffix_marker_removed": (
        'suffix = f" [filtered: {len(legs)}/{len(ALL_LEGS)} legs]" if only else ""',
        'suffix = ""',
    ),
    "m3_mutex_m1_extras_emptied": (
        '"m1": {"EDGE_SCHEMEREL", "EDGE_USERINFO", "EDGE_HTTPS"},',
        '"m1": {"EDGE_SCHEMEREL"},',
    ),
    "m4_frag_selftest_requirement_dropped": (
        'frag_ok = (st.returncode == 0 and sc.returncode == 0\n'
        '                           and "0 finding" in sc.stdout.decode("utf-8", "replace")\n'
        '                           and files == 26)',
        'frag_ok = (sc.returncode == 0\n'
        '                           and "0 finding" in sc.stdout.decode("utf-8", "replace")\n'
        '                           and files == 26)',
    ),
    "m5_frag_scan_check_weakened": (
        'and "0 finding" in sc.stdout.decode("utf-8", "replace")\n'
        '                           and files == 26)',
        'and "finding" in sc.stdout.decode("utf-8", "replace")\n'
        '                           and files == 26)',
    ),
}


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main():
    text = open(PRISTINE, encoding="utf-8").read()
    print(f"pristine sha256={sha(PRISTINE)} bytes={len(text.encode())}")
    bad = []
    for name, (needle, repl) in MUTANTS.items():
        n = text.count(needle)
        if n != 1:
            bad.append(f"{name}:needle_count={n}")
            print(f"{name}: NEEDLE COUNT {n} (expected 1)")
            continue
        out = os.path.join(HERE, "accept-o." + name + ".py")
        open(out, "w", encoding="utf-8").write(text.replace(needle, repl, 1))
        print(f"{name}: wrote {os.path.basename(out)} sha256={sha(out)} "
              f"needle_count=1")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
