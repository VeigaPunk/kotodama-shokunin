#!/usr/bin/env python3
"""Round-90 stub control, reproducible source (L1, added after CriticClaims attack 4).

The cheapest do-nothing landing for claim O: a tool that prints the verdict line a
frozen selftest would print and exits 0, without implementing any check. The
attempt-1 stub (`reports/round-90/controls/stub-tool.txt`, sha256 52ae4b62…) was
recorded by receipt only; this file is the same class with its bytes committed so
the control can be re-run. It is NOT the receipted stub (different bytes, same
class) and it is never installed as tools/check-advance-evidence.py.
"""

import argparse
import sys

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--work')
    ap.parse_args()
    print('SELFTEST PASS 67/67')
    sys.exit(0)
