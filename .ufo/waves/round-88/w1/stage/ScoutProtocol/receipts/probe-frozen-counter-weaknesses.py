#!/usr/bin/env python3
"""ScoutProtocol (kotodama round-88) — read-only probes of the FROZEN counter.

Never amends reports/round-88/measure88.py, claims.json or cases.json. Every probe
copies the frozen bytes into the given --work directory and exercises them there.

Probes:
  P1  materialize() worktree fallback: a control present ONLY in the worktree is
      graded under a lands revision label, contradicting the module docstring
      ("It grades committed bytes at a named revision; it never grades the worktree").
  P2  --selftest false green: the counter's own selftest exits 0 against a
      neutered comparison layer (always-reject / always-accept / membership-only).
  P3  battery-agrees coverage gap: a battery that reports the two checked counts
      (13, 4) and analyses nothing passes every leg of claim O, including while
      it accepts the constant-pass counterfeIt.
  P4  D predicate surface: rows/columns/cited/growth legs are satisfiable by
      prose citation, multi-table row summing, literal-pipe column inflation and
      growth placed outside the section.
  P5  claims.json claim-D counter command omits the REQUIRED --work argument.

Usage: probe-frozen-counter-weaknesses.py --root <lane> --work <existing-dir>
"""
import argparse
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ap = argparse.ArgumentParser()
ap.add_argument('--root', type=pathlib.Path, required=True)
ap.add_argument('--work', type=pathlib.Path, required=True)
ns = ap.parse_args()
ROOT = ns.root.resolve()
WORK = ns.work.resolve()
if not WORK.is_dir():
    print('PROBE_ERROR work must exist', file=sys.stderr)
    raise SystemExit(2)

FROZEN = ROOT / 'reports/round-88/measure88.py'
BASE = '4956282281dac1306cfbe59523e46dde99749d75'
LANDS = '4b76524c51e1c2f76c99eeb3b629cfac08a44a76'
PACKET = '.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json'
CASES = 'reports/round-88/cases.json'
HONEST = 'tools/check-attestation-packet.py'
BATTERY = 'tools/check-finding-sets.py'
CONTROLS = ['constant-pass', 'shotgun-all-labels', 'extra-id', 'filename-only']

spec = importlib.util.spec_from_file_location('frozen_measure88', FROZEN)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
m.ROOT = str(ROOT)

findings = []


def note(pid, title, observed, verdict):
    findings.append(dict(id=pid, title=title, observed=observed, verdict=verdict))
    print(f'{pid}  {title}\n    observed: {observed}\n    verdict:  {verdict}')


# ---------- P1: materialize() worktree fallback ----------
repo = WORK / 'p1-repo'
shutil.rmtree(repo, ignore_errors=True)
repo.mkdir(parents=True)
subprocess.run(['git', 'init', '-q', str(repo)], check=True, capture_output=True)
subprocess.run(['git', '-C', str(repo), '-c', 'user.email=a@b', '-c', 'user.name=t',
                'commit', '--allow-empty', '-qm', 'init'], check=True, capture_output=True)
(repo / 'reports/round-88/controls').mkdir(parents=True, exist_ok=True)
(repo / 'reports/round-88/controls/ghost.py').write_text('print("worktree only")\n')
subprocess.run(['git', '-C', str(repo), 'add', '-A'], check=True, capture_output=True)
subprocess.run(['git', '-C', str(repo), '-c', 'user.email=a@b', '-c', 'user.name=t',
                'commit', '-qm', 'base'], check=True, capture_output=True)
rev = subprocess.run(['git', '-C', str(repo), 'rev-parse', 'HEAD'],
                     capture_output=True, text=True).stdout.strip()
blob = m.blob(str(repo), rev, 'reports/round-88/controls/ghost.py')
# add the file to the WORKTREE only (not to git): blob stays absent at the revision
(repo / 'reports/round-88/controls/ghost2.py').write_text('print("worktree only")\n')
got = m.materialize(str(repo), rev, 'reports/round-88/controls/ghost2.py', WORK)
note('P1', 'materialize() grades WORKTREE bytes under a revision label',
     dict(blob_at_revision=None, materialize_returned=str(got) if got else None,
          content=got.read_text() if got else None),
     'FLAW: docstring says "never grades the worktree"; the fallback reads '
     'pathlib.Path(root)/path when the revision blob is absent.')

# ---------- P2: --selftest false green ----------
src = FROZEN.read_text()
mutants = {
    'always_reject': ("    ok = run.returncode == expected['rc']", '    ok = False'),
    'always_accept': ("    ok = run.returncode == expected['rc']", '    ok = True'),
    'membership_only': ("        ok = ok and ids == set(expected['ids']) and pairs == {(i, r) for i, r in zip(expected['ids'], expected['records'])}",
                        "        ok = ok and set(expected['ids']).issubset(ids)"),
}
p2 = {}
for name, (old, new) in mutants.items():
    assert old in src, name
    path = WORK / f'p2-mutant-{name}.py'
    path.write_text(src.replace(old, new))
    run = subprocess.run([sys.executable, '-B', str(path), '--root', str(ROOT),
                          '--work', str(WORK), '--selftest'], capture_output=True, text=True)
    p2[name] = dict(selftest_rc=run.returncode, survived=(run.returncode == 0))
stock = subprocess.run([sys.executable, '-B', str(FROZEN), '--root', str(ROOT),
                        '--work', str(WORK), '--selftest'], capture_output=True, text=True)
note('P2', "frozen --selftest cannot detect a neutered comparison layer",
     dict(stock_selftest_rc=stock.returncode, mutants=p2),
     'FLAW: every neutered mutant SURVIVES with rc=0, so the selftest exit 0 '
     'proves nothing about the layer it claims to check.')
# and the transport detail behind it
body = json.dumps({'records': 6, 'findings': [{'id': 'RECORD_ID', 'record': 'R1'}]})
tool = m.report_partial_tool(WORK, 'p2-exact-accepted', body)
child = subprocess.run([sys.executable, '-B', str(tool), '--packet', str(WORK / 'p2-packet.json'),
                        '--json'], capture_output=True, text=True)
note('P2b', 'exact-accepted selftest child crashes instead of emitting a report',
     dict(child_rc=child.returncode, child_stdout=child.stdout,
          stderr_tail=child.stderr.strip().splitlines()[-1] if child.stderr.strip() else ''),
     'FLAW: report_partial_tool() writes the JSON body as a PATHNAME; the child '
     'raises FileNotFoundError, so the "positive" leg asserts on a crash.')

# ---------- P3: battery-agrees coverage gap ----------
def gitshow(rev, path):
    p = subprocess.run(['git', '-C', str(ROOT), 'show', rev + ':' + path], capture_output=True)
    return p.stdout if p.returncode == 0 else None


def build_repo(name, battery_source):
    r = WORK / name
    shutil.rmtree(r, ignore_errors=True)
    r.mkdir(parents=True)
    subprocess.run(['git', 'init', '-q', str(r)], check=True, capture_output=True)
    subprocess.run(['git', '-C', str(r), '-c', 'user.email=a@b', '-c', 'user.name=t',
                    'commit', '--allow-empty', '-qm', 'i'], check=True, capture_output=True)

    def put(path, data):
        f = r / path
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(data)

    def commit(msg):
        subprocess.run(['git', '-C', str(r), 'add', '-A'], check=True, capture_output=True)
        subprocess.run(['git', '-C', str(r), '-c', 'user.email=a@b', '-c', 'user.name=t',
                        'commit', '-qm', msg], check=True, capture_output=True)
        return subprocess.run(['git', '-C', str(r), 'rev-parse', 'HEAD'],
                              capture_output=True, text=True).stdout.strip()

    put(PACKET, gitshow(BASE, PACKET))
    base_rev = commit('base')
    put(CASES, gitshow(LANDS, CASES))
    put(HONEST, gitshow(LANDS, HONEST))
    for c in CONTROLS:
        put(f'reports/round-88/controls/{c}.py', gitshow(LANDS, f'reports/round-88/controls/{c}.py'))
    put(BATTERY, battery_source.encode())
    lands_rev = commit('lands')
    return r, base_rev, lands_rev


DEGENERATE_BATTERY = '''#!/usr/bin/env python3
"""Degenerate battery: never analyses a packet. Reports 13/13 for every candidate
EXCEPT shotgun-all-labels (4/13). It therefore ACCEPTS the constant-pass
counterfeIt, extra-id and filename-only."""
import json, sys, pathlib
a = sys.argv[1:]
def opt(n, d=None): return a[a.index(n)+1] if n in a else d
if '--selftest' in a:
    print(json.dumps(dict(selftest='PASS'))); sys.exit(0)
name = pathlib.Path(opt('--candidate', '')).stem
print(json.dumps(dict(passed=4 if name == 'shotgun-all-labels' else 13, records=6, findings=[])))
'''

repo3, base3, lands3 = build_repo('p3-repo', DEGENERATE_BATTERY)
out3 = WORK / 'p3-work'
out3.mkdir(exist_ok=True)
run3 = subprocess.run([sys.executable, '-B', str(FROZEN), '--root', str(repo3),
                        '--base', base3, '--lands', lands3, '--claim', 'O',
                        '--work', str(out3)], capture_output=True, text=True)
try:
    body3 = json.loads(run3.stdout)
    legs3 = [(l['leg'], l['expected'], l['observed'], l['passed']) for l in body3['legs']]
except ValueError:
    legs3 = []
note('P3', 'claim O passes with a battery that accepts the constant-pass counterfeIt',
     dict(counter_rc=run3.returncode, passed=body3.get('passed') if isinstance(body3, dict) else None,
          total=body3.get('total') if isinstance(body3, dict) else None, legs=legs3),
     'FLAW: battery-agrees checks only (honest=13, shotgun=4) via the battery\'s own '
     'self-reported `passed` field; constant-pass/extra-id/filename-only are never '
     'asked of the battery. The kill_rule names per-class counts the counter does '
     'not obtain from the battery.')

# ---------- P4: D predicate surface ----------
HEADING = '## 4b. Numeral notation: two axes, five types, and their trade-offs'
NEW_IDS = ['S931', 'S932', 'S933']


def d_surface(text, base_len):
    section = text.split(HEADING, 1)[1].split('\n## ', 1)[0] if HEADING in text else ''
    rows = [ln for ln in section.splitlines()
            if ln.strip().startswith('|') and not re.match(r'^\s*\|[\s:|-]+\|\s*$', ln)]
    data_rows = max(0, len(rows) - 1)
    columns = max([ln.count('|') - 1 for ln in rows] or [0])
    cited = sorted({i for i in NEW_IDS if re.search(r'\b' + i + r'\b', section)})
    return dict(data_rows=data_rows, columns=columns, cited=cited,
                growth=len(text) - base_len)


base = '# numerals\n\n## 4. existing\n\ntext\n'
p4 = {}
# (a) two tables of two data rows each -> 5 counted data rows, only 4 real rows
t = (base + '\n' + HEADING + '\n\n| a | b |\n|---|---|\n| 1 | 2 |\n| 3 | 4 |\n'
     '\n| c | d |\n|---|---|\n| 5 | 6 |\n| 7 | 8 |\n\nSee S931, S932, S933.\n')
p4['two_tables_row_sum'] = d_surface(t, len(base))
# (b) ids in prose only, never in a table row
t = (base + '\n' + HEADING + '\n\n| a | b | c |\n|---|---|---|\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n'
     '| 7 | 8 | 9 |\n| 10 | 11 | 12 |\n| 13 | 14 | 15 |\n\n'
     'Sources consulted: S931, S932 and S933.\n')
p4['prose_only_citation'] = d_surface(t, len(base))
# (c) two-column table, one cell carries a literal pipe -> columns counted as 3
t = (base + '\n' + HEADING + '\n\n| a | b |\n|---|---|\n| x \\| y | z |\n| 3 | 4 |\n'
     '| 5 | 6 |\n| 7 | 8 |\n| 9 | 10 |\n\nS931 S932 S933\n')
p4['literal_pipe_columns'] = d_surface(t, len(base))
# (d) 2500 bytes of growth placed entirely OUTSIDE the 4b section
pad = '\n\n## Appendix Z\n\n' + ('x' * 2500)
t = (base + '\n' + HEADING + '\n\n| a | b | c |\n|---|---|---|\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n'
     '| 7 | 8 | 9 |\n| 10 | 11 | 12 |\n| 13 | 14 | 15 |\n\nS931 S932 S933\n' + pad)
p4['growth_outside_section'] = d_surface(t, len(base))
# (e) the heading text appearing twice (e.g. a TOC) fails the count==1 leg
t = ('TOC:\n' + HEADING + '\n\n' + HEADING + '\n\n| a | b | c |\n|---|---|---|\n| 1 | 2 | 3 |\n'
     '| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n| 10 | 11 | 12 |\n| 13 | 14 | 15 |\n\nS931 S932 S933\n')
p4['heading_count'] = t.count(HEADING)
note('P4', 'D predicate surface: rows/columns/cited/growth legs are weakly binding',
     p4,
     'WEAKNESS: table-rows sums rows across MULTIPLE tables (and counts a second '
     'table header as data); table-columns counts literal "|" so a 2-column table '
     'can read as 3; new-rows-cited is satisfied by prose, never by a table row; '
     'growth-bytes is measured over the whole file, not the section.')

# ---------- P5: claims.json claim-D counter command omits --work ----------
claims = json.loads((ROOT / 'reports/round-88/claims.json').read_text())
d_cmd = [c['counter'] for c in claims['claims'] if c['id'] == 'D'][0]
run5 = subprocess.run(d_cmd.replace('<lands>', LANDS), shell=True, cwd=str(ROOT),
                       capture_output=True, text=True)
note('P5', 'claims.json claim-D counter command is not runnable as written',
     dict(command=d_cmd, rc=run5.returncode,
          stderr_tail=run5.stderr.strip().splitlines()[-1] if run5.stderr.strip() else ''),
     'FLAW: measure88.py requires --work (argparse required=True); the frozen '
     'claim-D command omits it and exits 2 with a usage error. The claim-O '
     'command does include --work.')

print()
print(json.dumps(dict(label='SCOUTPROTOCOL_FROZEN_COUNTER_PROBES',
                      findings=findings), indent=2, sort_keys=True))
raise SystemExit(0)
