#!/usr/bin/env python3
"""Gap-hunt driver (MutationTesterV3). Scratch only: mutates copies of the
frozen tool under the scratch dir; never writes to the lane."""
import hashlib
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

SCRATCH = '/fast/scratch/hyaku/kotodama-r92/MutationTesterV3'
FROZEN = os.path.join(SCRATCH, 'frozen-check-advance-evidence.py')
OUT = os.path.join(SCRATCH, 'gap')

GAPS = [
    ('gap-readme-graded-off',
     "args.base_registry, 'corpus/README.md', args.manifest]:",
     "args.base_registry, args.manifest]:"),
    ('gap-manifest-graded-off',
     "args.base_registry, 'corpus/README.md', args.manifest]:",
     "args.base_registry, 'corpus/README.md']:"),
    ('gap-entry-graded-off',
     "[args.lesson, args.lands_registry, args.entry,",
     "[args.lesson, args.lands_registry,"),
    ('gap-lands-graded-off',
     "[args.lesson, args.lands_registry, args.entry,",
     "[args.lesson, args.entry,"),
    ('gap-lesson-graded-off',
     "[args.lesson, args.lands_registry, args.entry,",
     "[args.lands_registry, args.entry,"),
    ('gap-traversal-off',
     "    if rel.startswith('/') or '..' in rel.split('/'):\n        return f'capture path not relative and confined: {rel}'",
     "    if rel.startswith('/'):\n        return f'capture path not relative and confined: {rel}'"),
    ('gap-fetch-offset-optional',
     r"(?:Z|[+-]\d{2}:\d{2})$')",
     r"(?:Z|[+-]\d{2}:\d{2})?$')"),
    ('gap-fetch-date-off',
     "    if fm.group(1) != as_of:",
     "    if False:"),
    ('gap-cap-slash-off',
     "rel.startswith(cap_dir.rstrip('/') + '/')",
     "rel.startswith(cap_dir.rstrip('/'))"),
    ('gap-port-strip-off',
     "if (scheme == 'http' and host.endswith(':80')) or (scheme == 'https' and host.endswith(':443')):",
     "if False:"),
]


def run_selftest(tool, work):
    os.makedirs(work, exist_ok=True)
    r = subprocess.run([sys.executable, '-B', tool, '--selftest', '--work', work],
                       capture_output=True, text=True, env={**os.environ, 'TMPDIR': work})
    out = (r.stdout or '') + (r.stderr or '')
    ok = sum(1 for ln in out.splitlines() if ln.startswith('  ok '))
    tail = [ln for ln in out.splitlines() if 'SELFTEST' in ln or 'FAIL' in ln][:3]
    return r.returncode, ok, tail


def one(name, old, new, src):
    n = src.count(old)
    if n != 1:
        return {'name': name, 'verdict': 'BROKEN-PATTERN', 'count': n}
    mut_src = src.replace(old, new)
    d = os.path.join(OUT, name)
    os.makedirs(d, exist_ok=True)
    mut = os.path.join(d, 'mut.py')
    with open(mut, 'w') as f:
        f.write(mut_src)
    rc, ok, tail = run_selftest(mut, os.path.join(d, 'work'))
    verdict = 'KILLED' if rc != 0 else 'SURVIVED'
    return {'name': name, 'verdict': verdict, 'rc': rc, 'ok_lines': ok,
            'mut_sha256': hashlib.sha256(mut_src.encode()).hexdigest(), 'tail': tail,
            'old': old, 'new': new}


def main():
    with open(FROZEN, 'rb') as f:
        raw = f.read()
    src = raw.decode('utf-8')
    base_sha = hashlib.sha256(raw).hexdigest()
    clean_rc, clean_ok, clean_tail = run_selftest(FROZEN, os.path.join(OUT, 'clean', 'work'))
    print(f'frozen sha256={base_sha} clean selftest rc={clean_rc} ok_lines={clean_ok} tail={clean_tail}')
    with ThreadPoolExecutor(max_workers=4) as ex:
        results = list(ex.map(lambda g: one(g[0], g[1], g[2], src), GAPS))
    for r in results:
        print(json.dumps({k: v for k, v in r.items() if k not in ('old', 'new')}, sort_keys=True))
    with open(os.path.join(OUT, 'gap-results.json'), 'w') as f:
        json.dump({'frozen_sha256': base_sha, 'clean_rc': clean_rc, 'clean_ok_lines': clean_ok,
                   'results': results}, f, indent=1, sort_keys=True)


if __name__ == '__main__':
    main()
