#!/usr/bin/env python3
"""ReviewerCounter r89 probe B: (1) lands-tree .gitattributes export-ignore steers what the
freeze-pinned index tool sees; (2) FROZENCFG does not bind the *executing* counter file."""
import os, subprocess, sys, shutil
R = sys.argv[1]
sys.argv = [sys.argv[0], R]
src = open(os.path.join(R, 'probe89.py')).read().replace('\nmain()\n', '\n')
exec(compile(src, 'probe89.py', 'exec'))

reset()
c_land(offtopic_entry())
put('corpus/knowledge/linguistics/hidden-unindexed.md', '# hidden\n\n- topic: nothing\n')
put('corpus/.gitattributes', 'knowledge/linguistics/hidden-unindexed.md export-ignore\n')
lands = commit('C-export-ignore-hides-unindexed-file')
rc, so, se = run(lands, 'C')
print('C-export-ignore-hides-unindexed-file rc=%d %s' % (rc, so.strip().splitlines()[-1]))
p = subprocess.run([sys.executable, '-B', os.path.join(D, 'tools/check-corpus-index.py'), '--root', D], capture_output=True)
print('  same lands, index tool over the real checkout: rc=%d %s' % (p.returncode, p.stdout.decode().strip().splitlines()[-1][:200]))

# (2) an edited counter outside the repo, graded against an untouched lands, still reports FROZENCFG PASS
reset()
mod = os.path.join(R, 'measure89-edited.py')
body = open(os.path.join(D, 'reports/round-89/measure89.py')).read()
body = body.replace("out.append(leg('ADVANCED', len(advanced) >= c['advance_min'],", "out.append(leg('ADVANCED', True,")
body = body.replace("out.append(leg('DISPOSED', not undisposed,", "out.append(leg('DISPOSED', True,")
open(mod, 'w').write(body)
p = subprocess.run([sys.executable, '-B', mod, '--root', D, '--freeze', FREEZE, '--lands', FREEZE, '--claim', 'F', '--work', R], capture_output=True)
so = p.stdout.decode()
print('edited-counter-on-do-nothing rc=%d %s | %s' % (p.returncode, [l for l in so.splitlines() if 'FROZENCFG' in l][0][:60], so.strip().splitlines()[-1]))
print('  self sha line:', [l for l in so.splitlines() if 'sha256 (self)' in l][0])
os.remove(mod)
reset()
