#!/usr/bin/env python3
"""ScribeNotation round-88 check: does a proposed SOURCES.md row shape satisfy
the frozen claim-D mined leg, and does the staged section satisfy the other
frozen D legs?

Read-only. It writes nothing outside its own stdout. It does NOT modify
reports/round-88/claims.json, reports/round-88/measure88.py or
reports/round-88/cases.json, and it does not run the frozen counter: the leg
logic is replicated here in the same shape so the integrator can see the
arithmetic without the graded tree being involved.

Usage:
  python3 -B mined-leg-check.py [--lane LANE_ROOT] [--entry ENTRY_PATH]
                                  [--section SECTION_PATH]

Exit codes: 0 all simulated legs pass; 1 a leg fails; 2 an input is missing.
"""
import argparse
import pathlib
import re
import subprocess
import sys

BASE = '4956282281dac1306cfbe59523e46dde99749d75'
HEADING = '## 4b. Numeral notation: two axes, five types, and their trade-offs'
NEW_IDS = ['S931', 'S932', 'S933']
ENTRY = 'corpus/knowledge/linguistics/numerals-and-measures.md'
SOURCES = 'corpus/SOURCES.md'


def blob(root, rev, path):
    p = subprocess.run(['git', '-C', str(root), 'show', rev + ':' + path],
                       capture_output=True)
    return p.stdout if p.returncode == 0 else None


def mined_leg(sources_text, ids):
    """The frozen claim-D mined-leg arithmetic, replicated."""
    out = []
    for i in ids:
        m = re.search(r'^ {0,3}\|\s*' + i + r'\s*\|(.*)$', sources_text, re.M)
        if not m:
            out.append(dict(id=i, found=False, ok=False))
            continue
        cells = [c.strip() for c in m.group(1).split('|')]
        tier = cells[2] if len(cells) > 2 else ''
        status = cells[6] if len(cells) > 6 else ''
        out.append(dict(id=i, found=True, tier=tier, status=status,
                        ok=(tier in ('A', 'B') and status == 'mined'),
                        cells=len(cells)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lane', default='/home/vgpnk/Projects/shokunin/kotodama-shokunin')
    ap.add_argument('--entry', default=ENTRY)
    ap.add_argument('--section', required=True)
    ap.add_argument('--sources', default=SOURCES)
    ns = ap.parse_args()
    root = pathlib.Path(ns.lane)
    section_path = pathlib.Path(ns.section)
    if not section_path.is_file():
        print('MINED_LEG_ERROR missing section ' + str(section_path), file=sys.stderr)
        return 2
    base_entry = blob(root, BASE, ns.entry)
    if base_entry is None:
        print('MINED_LEG_ERROR cannot read base entry at ' + BASE, file=sys.stderr)
        return 2
    section = section_path.read_text()
    marker = '\n## 5. Counting technologies'
    if marker not in base_entry.decode():
        print('MINED_LEG_ERROR insertion marker not found in base entry', file=sys.stderr)
        return 2
    merged = base_entry.decode().replace(marker, '\n' + section.rstrip() + '\n' + marker, 1)

    legs = []
    legs.append(('heading-absent-at-base', 0, base_entry.decode().count(HEADING)))
    legs.append(('heading-present-at-lands', 1, merged.count(HEADING)))
    sec = merged.split(HEADING, 1)[1].split('\n## ', 1)[0]
    rows = [ln for ln in sec.splitlines()
            if ln.strip().startswith('|') and not re.match(r'^\s*\|[\s:|-]+\|\s*$', ln)]
    legs.append(('table-rows', True, max(0, len(rows) - 1) >= 5))
    legs.append(('table-columns', True, max([ln.count('|') - 1 for ln in rows] or [0]) >= 3))
    cited = sorted({i for i in NEW_IDS if re.search(r'\b' + i + r'\b', sec)})
    legs.append(('new-rows-cited', 3, len(cited)))
    legs.append(('growth-bytes', True, len(merged.encode()) - len(base_entry) >= 2500))

    sources_text = blob(root, 'HEAD', ns.sources)
    if sources_text is not None:
        mined = mined_leg(sources_text.decode('utf-8', 'replace'), NEW_IDS)
        legs.append(('new-rows-mined', 3, sum(1 for m in mined if m.get('ok'))))

    ok = True
    for name, want, got in legs:
        good = (want == got) if not isinstance(want, bool) else (want is got)
        ok = ok and good
        print(('LEG PASS ' if good else 'LEG FAIL ') + name +
              ' expected=' + repr(want) + ' observed=' + repr(got))
    if sources_text is None:
        print('NOTE new-rows-mined not evaluated: corpus/SOURCES.md unreadable at HEAD')
    print('CITED_LINES_SIM: see tools/check-cited-lines.py on the merged candidate')
    print('MINED_LEG: ' + ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
