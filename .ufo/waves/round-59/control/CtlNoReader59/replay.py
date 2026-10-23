#!/usr/bin/env python3
"""Replay only the supplied control fixture, using the unchanged round-59 counter."""
import pathlib
import subprocess
import sys

FIXTURES = pathlib.Path(__file__).resolve().parent
ROOT = pathlib.Path(sys.argv[1]).resolve()
NAME = sys.argv[2]
REV = '1b80ee41f544d17c0410733a47a3eecac01bf25e'
ENTRY = 'corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'
TOPIC = 'Sandbox no-reader protective-object control; not admitted knowledge.'
ALLOWED = pathlib.Path('/fast/scratch/hyaku/kotodama-r59/CtlNoReader59')
if not ROOT.is_relative_to(ALLOWED) or NAME not in {
    'metadata', 'snippets', 'structural', 'fetch-abuse', 'fetch-v2', 'fetch-padded'
}:
    raise SystemExit('Requires this seat sandbox and one supplied fixture name')

def base(path):
    return subprocess.run(
        ['timeout', '30', 'git', '-C', str(ROOT), 'show', f'{REV}:{path}'],
        capture_output=True, text=True, check=True, timeout=35,
    ).stdout

(ROOT/'corpus/SOURCES.md').write_text(
    base('corpus/SOURCES.md')+'\n'+(FIXTURES/(NAME+'.rows.md')).read_text()
)
(ROOT/ENTRY).write_text((FIXTURES/(NAME+'.entry.md')).read_text())
index = base('corpus/README.md')
index = index.replace(
    '## myth-symbol/ (28)',
    '## myth-symbol/ (29)\n- `amulets-talismans-apotropaic-marks.md` — '+TOPIC,
)
index = index.replace('Total knowledge entries: 234.', 'Total knowledge entries: 235.')
index = index.replace(
    '(total 234 files; directory totals 29/28/29/29/24/95).',
    '(total 235 files; directory totals 29/29/29/29/24/95).',
)
(ROOT/'corpus/README.md').write_text(index)
result = subprocess.run(
    ['timeout', '900', 'python3', '-B', 'reports/round-59/accept-c.py'],
    cwd=ROOT, timeout=910,
)
raise SystemExit(result.returncode)
