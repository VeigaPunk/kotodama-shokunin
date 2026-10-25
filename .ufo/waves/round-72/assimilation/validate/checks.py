#!/usr/bin/env python3
"""Round-72 scratch-mirror checks: malformed rows, duplicate ids, duplicate URLs,
and the id-collision check for the two adopted rows S874/S875.

Read-only. Operates on the mirrored corpus at /tmp/r72-mirror and on the lane
registry (pre-append) as the reg-ids baseline. Census-equivalent URL
normalisation (scripts/sources-census.sh url_of): first http(s) URL in the
source cell, fragment stripped, trailing slash stripped, host lowercased.

Usage: python3 -B checks.py [--mirror DIR] [--lane DIR] [--assim DIR]
"""
import argparse
import pathlib
import re
import sys

ROW_RE = re.compile(r'^\| *S[0-9]{3,} *\|')
ID_RE = re.compile(r'^\| *(S[0-9]{3,}) *\|')
URL_RE = re.compile(r'https?://[^\s|]+')


def url_of(source: str) -> str:
    m = URL_RE.search(source)
    if not m:
        return ""
    u = m.group(0)
    u = re.sub(r'#[^ ]*$', '', u)
    if u.endswith('/'):
        u = u[:-1]
    u = re.sub(r'^[A-Za-z]+://', '', u)
    slash = u.find('/')
    if slash >= 0:
        return u[:slash].lower() + u[slash:]
    return u.lower()


def registry_rows(path: pathlib.Path):
    """Yield (lineno, id, source, status, scope, usedby) for ## Registry rows."""
    in_registry = False
    for n, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if line.startswith('## '):
            in_registry = line[3:].strip() == 'Registry'
            continue
        if line.startswith('# '):
            in_registry = False
            continue
        if not in_registry or not line.startswith('|'):
            continue
        cells = line.split('|')
        if len(cells) < 12:
            continue
        cid = cells[1].strip()
        if not re.fullmatch(r'S[0-9]{3,}', cid):
            continue
        yield n, cid, cells[2].strip(), cells[8].strip(), cells[5].strip(), cells[11].strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--mirror', default='/tmp/r72-mirror')
    ap.add_argument('--lane', default='/home/vgpnk/Projects/shokunin/kotodama-shokunin')
    ap.add_argument('--assim', default=None)
    a = ap.parse_args()
    mirror = pathlib.Path(a.mirror)
    lane = pathlib.Path(a.lane)
    assim = pathlib.Path(a.assim) if a.assim else lane / '.ufo/waves/round-72/assimilation'
    mir_file = mirror / 'corpus/SOURCES.md'
    lane_file = lane / 'corpus/SOURCES.md'
    new_ids = ('S874', 'S875')
    failures = []

    # 1. malformed rows: NF != 13 among S-rows
    bad = []
    total = 0
    for n, line in enumerate(mir_file.read_text(encoding='utf-8').splitlines(), 1):
        if not ROW_RE.match(line):
            continue
        total += 1
        nf = len(line.split('|'))
        if nf != 13:
            bad.append((n, nf))
    print(f'[1] malformed rows (NF!=13): {len(bad)}  over {total} S-rows')
    for n, nf in bad:
        print(f'    line {n}: NF={nf}')
    if bad:
        failures.append('malformed rows present')

    # 2. duplicate ids
    ids = {}
    for n, cid, *_ in registry_rows(mir_file):
        ids.setdefault(cid, []).append(n)
    dup_ids = {k: v for k, v in ids.items() if len(v) > 1}
    print(f'[2] duplicate ids: {len(dup_ids)}  (distinct ids={len(ids)})')
    for k, v in sorted(dup_ids.items()):
        print(f'    {k} at lines {v}')
    if dup_ids:
        failures.append('duplicate ids present')

    # 3. duplicate URLs (census url_of normalisation, whole registry)
    urls = {}
    for n, cid, source, status, scope, _u in registry_rows(mir_file):
        u = url_of(source)
        if u:
            urls.setdefault(u, []).append((cid, scope, status))
    dup_urls = {k: v for k, v in urls.items() if len(v) > 1}
    print(f'[3] duplicate normalised URLs: {len(dup_urls)}  (distinct urls={len(urls)})')
    touched = False
    for k, v in sorted(dup_urls.items()):
        hit = any(cid in new_ids for cid, _s, _st in v)
        touched = touched or hit
        print(f'    {k} <- {[c for c, _s, _st in v]}' + ('   *** NEW ROW COLLIDES ***' if hit else ''))
    if touched:
        failures.append('new-row URL collides with an existing row')

    # 3b. every URL of the two new rows must be unique against the rest of the registry
    print('[3b] per-URL uniqueness of the two new rows')
    all_urls = []
    for n, cid, source, *_ in registry_rows(mir_file):
        for m in URL_RE.finditer(source):
            all_urls.append((cid, m.group(0)))
    for nid in new_ids:
        for cid, raw in all_urls:
            if cid != nid:
                continue
            same = [c for c, r in all_urls if r == raw]
            print(f'    {nid}: {raw}  occurrences={len(same)}  owners={sorted(set(same))}')
            if len(same) != 1:
                failures.append(f'{nid} URL not unique: {raw}')
    for host in ('ihchina.cn', 'bunka.go.jp'):
        hits = sum(1 for _c, r in all_urls if host in r)
        print(f'    host {host}: {hits} URL occurrences in registry (expect 3 for ihchina.cn incl. archive captures, 1 for bunka.go.jp)')

    # 4. id-collision check: adopted new ids vs reg-ids (lane pre-append) and staged ids
    reg_ids = sorted({cid for _n, cid, *_ in registry_rows(lane_file)})
    staged_ids = set()
    rts = assim / 'reg-to-staged.txt'
    if rts.exists():
        for line in rts.read_text(encoding='utf-8').splitlines():
            m = re.search(r'-> \[(.*)\]', line)
            if m:
                for tok in re.findall(r"S[0-9]{3,}`?", m.group(1)):
                    staged_ids.add(tok.rstrip('`'))
    (assim / 'collcheck-reg-ids.txt').write_text('\n'.join(reg_ids) + '\n', encoding='utf-8')
    (assim / 'collcheck-staged-ids.txt').write_text('\n'.join(sorted(staged_ids)) + '\n', encoding='utf-8')
    collisions = sorted(set(new_ids) & set(reg_ids))
    (assim / 'collcheck-collisions.txt').write_text(''.join(c + '\n' for c in collisions), encoding='utf-8')
    print(f'[4] reg-ids={len(reg_ids)} (max {reg_ids[-1]})  staged-ids={len(staged_ids)}')
    print(f'    new ids {list(new_ids)} vs reg-ids -> collisions: {collisions or "none"}')
    if collisions:
        failures.append('new id collides with a registry id')
    staged_hits = sorted(set(new_ids) & staged_ids)
    print(f'    NOTE new ids also present in the staged namespace: {staged_hits or "none"}'
          f' (staged rows are not admitted this round; no registry collision)')

    print()
    print('RESULT:', 'PASS' if not failures else 'FAIL ' + '; '.join(failures))
    return 0 if not failures else 1


if __name__ == '__main__':
    sys.exit(main())
