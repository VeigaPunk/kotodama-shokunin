#!/usr/bin/env python3
"""Build a minimal fixture repo with a PERFECT claim-C landing and run the
frozen counter against it. Purpose: measure90.py grade_c parses the grader's
LEG lines as dict(re.findall(r'^LEG (PASS|FAIL) (\S+)')) -- keys become the
verdicts, not the leg names -- so the ENTRY leg must fail even when the
freeze-pinned grader prints PASS legs=6/6 (observed=clean)."""
import hashlib, json, os, re, subprocess, sys

S = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(S, 'fix')
LANE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
AS_OF = '2026-11-04'
TOPIC = ("petitionary address and votive formulae: vocative address to deities, petition mood "
         "(imperative, optative, precative), the conditional vow, votive inscription grammar, "
         "prayer-register archaism and parallelism, design procedure and failure modes")

def sh(cmd, cwd, env=None):
    e = dict(os.environ)
    e.update({'GIT_AUTHOR_NAME': 'fixture', 'GIT_AUTHOR_EMAIL': 'f@f',
              'GIT_COMMITTER_NAME': 'fixture', 'GIT_COMMITTER_EMAIL': 'f@f',
              'GIT_AUTHOR_DATE': '2026-11-04T12:00:00+00:00',
              'GIT_COMMITTER_DATE': '2026-11-04T12:00:00+00:00'})
    if env: e.update(env)
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=e)
    if r.returncode != 0:
        raise SystemExit(f'FAILED {cmd}: {r.stderr}')
    return r.stdout.strip()

subprocess.run(['rm', '-rf', FIX], check=True)
os.makedirs(FIX)
sh(['git', 'init', '-q', '-b', 'main'], FIX)

def commit(msg):
    sh(['git', 'add', '-A'], FIX)
    sh(['git', 'commit', '-q', '-m', msg], FIX)
    return sh(['git', 'rev-parse', 'HEAD'], FIX)

# ---- BASE: registry with one pre-existing row -----------------------------
os.makedirs(os.path.join(FIX, 'corpus'), exist_ok=True)
with open(os.path.join(FIX, 'corpus/SOURCES.md'), 'w') as f:
    f.write('| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n'
            '|---|---|---|---|---|---|---|---|---|---|---|\n'
            '| S001 | https://example.org/old-grammar | docs | A | scope | anchor | older summary | mined '
            '| 2026-10-01 | 180d | corpus/knowledge/old.md |\n')
HBASE = commit('base')

# ---- FREEZE: frozen claims.json (base re-pointed at the fixture) + tools ---
os.makedirs(os.path.join(FIX, 'reports/round-90'), exist_ok=True)
os.makedirs(os.path.join(FIX, 'tools'), exist_ok=True)
claims = json.load(open(os.path.join(LANE, 'reports/round-90/claims.json')))
claims['base'] = HBASE
json.dump(claims, open(os.path.join(FIX, 'reports/round-90/claims.json'), 'w'), indent=1)
for t in ('check-advance-evidence.py', 'check-corpus-index.py'):
    subprocess.run(['cp', os.path.join(LANE, 'tools', t), os.path.join(FIX, 'tools', t)], check=True)
HFREEZE = commit('freeze')

# ---- LANDS: a perfect C landing per the grader's own rules -----------------
entry = []
entry.append('# Petitionary and votive formulae — fixture entry\n\n')
entry.append('- topic: ' + TOPIC + '\n')
entry.append('- sources: S942, S943, S944 (fixture pages), all opened ' + AS_OF + '\n')
entry.append('- verified-at: ' + AS_OF + ' — fixture\n')
entry.append('- recheck: 180 days (2027-05-03)\n\n')
for n in range(1, 7):
    entry.append(f'## {n}. Section {n} on vocative address and petition mood\n\n')
    for j in range(1, 11):
        entry.append(f'[{n}.{j}] Vocative address to deities with marker {n}{j} takes the petition mood slot {j} '
                     f'and the conditional vow clause {n}x{j} in votive inscription grammar, prayer-register '
                     f'archaism, and parallelism across design procedure and failure modes. ')
    entry.append(f'\n\nSection {n} fixture text also cites S001, an existing base row.\n')
table = ['| form | mood | design note |', '|---|---|---|']
for n in range(1, 7):
    table.append(f'| form {n} | optative | note {n} |')
entry.append('\n'.join(table) + '\n')
for n, (rid, url, quote) in enumerate([
        ('S942', 'https://example.org/votive-a', 'The conditional vow binds the donor to the deity through an if-and-then exchange of offerings.'),
        ('S943', 'https://example.org/votive-b', 'Votive inscriptions open with the deity name in the dative and close with the dedicator.'),
        ('S944', 'https://example.org/votive-c', 'Precative petitions soften the imperative with particles of entreaty and humility.')]):
    entry.append(f'\nMined fixture row {rid} carries: “{quote}”\n')
entry_path = os.path.join(FIX, 'corpus/knowledge/linguistics/petitionary-and-votive-formulae.md')
os.makedirs(os.path.dirname(entry_path), exist_ok=True)
with open(entry_path, 'w') as f:
    f.write(''.join(entry))
    f.write('\n' + TOPIC + '\n')  # pad over the 12000-byte floor with topic words

with open(os.path.join(FIX, 'corpus/SOURCES.md'), 'a') as f:
    for rid, url, teaches in [
            ('S942', 'https://example.org/votive-a', 'the conditional vow binds donor to deity'),
            ('S943', 'https://example.org/votive-b', 'dative deity name, dedicator closure'),
            ('S944', 'https://example.org/votive-c', 'precatives soften the imperative')]:
        f.write(f'| {rid} | {url} | docs | A | scope | anchor | {teaches} | mined | {AS_OF} | 180d '
                f'| corpus/knowledge/linguistics/petitionary-and-votive-formulae.md |\n')

os.makedirs(os.path.join(FIX, 'corpus/lessons'), exist_ok=True)
os.makedirs(os.path.join(FIX, 'reports/round-90/evidence'), exist_ok=True)
man = {'rows': {}}
for rid, url, quote in [
        ('S942', 'https://example.org/votive-a', 'The conditional vow binds the donor to the deity through an if-and-then exchange of offerings.'),
        ('S943', 'https://example.org/votive-b', 'Votive inscriptions open with the deity name in the dative and close with the dedicator.'),
        ('S944', 'https://example.org/votive-c', 'Precative petitions soften the imperative with particles of entreaty and humility.')]:
    with open(os.path.join(FIX, f'reports/round-90/evidence/{rid}.txt'), 'w') as f:
        f.write('PAGE CHROME HEADER\n\n' + quote + '\n\nMORE PROSE AROUND IT so the page is a real page.\n')
    raw = open(os.path.join(FIX, f'reports/round-90/evidence/{rid}.txt'), 'rb').read()
    man['rows'][rid] = {'url': url, 'http_status': 200,
                        'fetched_at': f'{AS_OF}T12:00:00+00:00',
                        'capture': f'reports/round-90/evidence/{rid}.txt',
                        'sha256': hashlib.sha256(raw).hexdigest()}
    with open(os.path.join(FIX, 'corpus/lessons/round-90.md'), 'a') as g:
        g.write(f'- **{rid} admit A/mined.** {url} — accessed {AS_OF} — §2: “{quote}” '
                f'Grounds: fixture. Capture reports/round-90/evidence/{rid}.txt.\n')
json.dump(man, open(os.path.join(FIX, 'reports/round-90/evidence/manifest.json'), 'w'), indent=1)
with open(os.path.join(FIX, 'corpus/README.md'), 'w') as f:
    f.write('# fixture readme\n')
HLANDS = commit('lands')

# sanity: the grader alone must PASS 6/6 on this landing
mat = os.path.join(S, 'mat')
subprocess.run(['rm', '-rf', mat], check=True)
os.makedirs(mat, exist_ok=True)
subprocess.run(['git', '-C', FIX, 'archive', '--format=tar', HLANDS], stdout=open(mat + '.tar', 'wb'), check=True)
subprocess.run(['tar', '-xf', mat + '.tar', '-C', mat], check=True)
r = subprocess.run([sys.executable, '-B', os.path.join(FIX, 'tools/check-advance-evidence.py'),
                    'entry', '--root', mat,
                    '--entry', os.path.join(mat, 'corpus/knowledge/linguistics/petitionary-and-votive-formulae.md'),
                    '--base-registry', os.path.join(mat, 'corpus/SOURCES.md'),  # fixture lands has no separate base here; grader used only for leg demo
                    '--lands-registry', os.path.join(mat, 'corpus/SOURCES.md'),
                    '--lesson', os.path.join(mat, 'corpus/lessons/round-90.md'),
                    '--manifest', os.path.join(mat, 'reports/round-90/evidence/manifest.json'),
                    '--capture-dir', 'reports/round-90/evidence',
                    '--as-of', AS_OF, '--topic', TOPIC,
                    '--min-bytes', '12000', '--min-headings', '6', '--min-new-ids', '3',
                    '--min-topic-overlap', '10', '--table-min-rows', '5', '--table-min-cols', '3',
                    '--graded', 'corpus/SOURCES.md', '--graded', 'corpus/lessons/round-90.md'],
                   capture_output=True, text=True)
print('=== grader alone (lands registry as both) ===')
print(r.stdout, r.stderr)
base_reg = os.path.join(S, 'base-SOURCES.md')
open(base_reg, 'w').write(
    '| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n'
    '|---|---|---|---|---|---|---|---|---|---|---|\n'
    '| S001 | https://example.org/old-grammar | docs | A | scope | anchor | older summary | mined '
    '| 2026-10-01 | 180d | corpus/knowledge/old.md |\n')
r2 = subprocess.run([sys.executable, '-B', os.path.join(FIX, 'tools/check-advance-evidence.py'),
                     'entry', '--root', mat,
                     '--entry', os.path.join(mat, 'corpus/knowledge/linguistics/petitionary-and-votive-formulae.md'),
                     '--base-registry', base_reg,
                     '--lands-registry', os.path.join(mat, 'corpus/SOURCES.md'),
                     '--lesson', os.path.join(mat, 'corpus/lessons/round-90.md'),
                     '--manifest', os.path.join(mat, 'reports/round-90/evidence/manifest.json'),
                     '--capture-dir', 'reports/round-90/evidence',
                     '--as-of', AS_OF, '--topic', TOPIC,
                     '--min-bytes', '12000', '--min-headings', '6', '--min-new-ids', '3',
                     '--min-topic-overlap', '10', '--table-min-rows', '5', '--table-min-cols', '3',
                     '--graded', 'corpus/SOURCES.md', '--graded', 'corpus/lessons/round-90.md'],
                    capture_output=True, text=True)
print('=== grader alone (true base registry) ===')
print(r2.stdout, r2.stderr)

# ---- the frozen counter over the same perfect landing ----------------------
work = os.path.join(S, 'work'); os.makedirs(work, exist_ok=True)
r3 = subprocess.run([sys.executable, '-B', os.path.join(LANE, 'reports/round-90/measure90.py'),
                     '--root', FIX, '--lands', HLANDS, '--freeze', HFREEZE,
                     '--claim', 'C', '--work', work],
                    capture_output=True, text=True)
print('=== measure90 --claim C over the perfect landing ===')
print('rc =', r3.returncode)
print(r3.stdout, r3.stderr)

# ---- parse-only demonstration ---------------------------------------------
out = r2.stdout
want = ['ENTRY', 'SHAPE', 'TOPIC', 'NEWIDS', 'GATE', 'CAPTURE']
seen = dict(re.findall(r'^LEG (PASS|FAIL) (\S+)', out, re.M)[::-1])
missing = [l for l in want if l not in seen]
failed = [l for l in want if seen.get(l) == 'FAIL']
print('=== parse simulation on a PASS legs=6/6 output ===')
print('seen dict =', seen)
print('missing =', missing, '-> counter ok flag =', r2.returncode == 0 and not missing and not failed)
print('HBASE', HBASE); print('HFREEZE', HFREEZE); print('HLANDS', HLANDS)
