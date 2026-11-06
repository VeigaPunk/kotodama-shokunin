#!/usr/bin/env python3
"""Enumerate every seat of a wave spec and test that its Report file <wave-dir>/<Seat>.md exists and is
non-empty (round-100 fix for round-99 closure defect D1: a report claimed a uniform seat-report path
that one seat did not have). Prints one line per seat and `SEAT-REPORTS: <ok>/<n> present`; rc 0 iff
all present, 1 otherwise, 2 on unreadable input.

Usage: python3 -B seat-report-paths.py --spec <wN-spec.json> --wave-dir <dir>
"""
import argparse
import json
import os
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--spec', required=True)
    ap.add_argument('--wave-dir', required=True)
    a = ap.parse_args()
    try:
        items = json.load(open(a.spec, encoding='utf-8'))['items']
        names = [i['name'] for i in items]
    except (OSError, ValueError, KeyError, TypeError) as e:
        print(f'SEAT-REPORTS-ERROR unreadable spec: {type(e).__name__}')
        return 2
    ok = 0
    for n in names:
        p = os.path.join(a.wave_dir, n + '.md')
        good = os.path.isfile(p) and os.path.getsize(p) > 0
        ok += good
        print(f'{"PRESENT" if good else "MISSING"} {n}.md')
    print(f'SEAT-REPORTS: {ok}/{len(names)} present')
    return 0 if ok == len(names) else 1


if __name__ == '__main__':
    sys.exit(main())
