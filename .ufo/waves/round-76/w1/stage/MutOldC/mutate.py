#!/usr/bin/env python3
import hashlib, os, subprocess, sys
D='/fast/scratch/hyaku/kotodama-r76/MutOldC/clone'; S='/fast/scratch/hyaku/kotodama-r76/MutOldC'
LANDS='4f5e3b2535c2c06c51627dc2736c40183847cae1'; FREEZE='5d0167464309d8133991b30f7d7a7011a6a0fd14'

def run(*a, capture=False):
    return subprocess.run(a, cwd=D, check=True, text=True, stdout=subprocess.PIPE if capture else None, stderr=subprocess.STDOUT if capture else None)
def mutate(name):
    if name.startswith('entry_'):
        p='corpus/knowledge/myth-symbol/narrative-structure-frameworks.md'
    elif name.startswith('row_'): p='corpus/SOURCES.md'
    elif name.startswith('gate_'): p='corpus/lessons/round-75.md'
    elif name.startswith('evidence_'): p='reports/round-75/evidence/S885.txt'
    else: p='corpus/README.md'
    f=os.path.join(D,p); b=open(f,'rb').read()
    if name=='entry_blank': old=b'- verified-at: 2026-10-27'; new=b'- verified-at: '
    elif name=='entry_short': old=b'## 1 Calibration key'; new=b'## 1 Calibration key'; b=b.replace(old,new,1); i=b.index(new)+len(new); b=b[:i]+b'\nshort\n'; open(f,'wb').write(b); return p
    elif name=='entry_angle': old=b'- topic: how narrative structure'; new=b'- topic: <draft> how narrative structure'
    elif name=='row_usedby':
        lines=b.splitlines(keepends=True); idx=next(i for i,x in enumerate(lines) if x.startswith(b'| S885 |')); cells=lines[idx].rstrip(b'\n').split(b'|'); cells[-2]=b' '; lines[idx]=b'|'.join(cells)+b'\n'; b=b''.join(lines); old=None
    elif name=='row_extra': b += b'| S999 | Extra test row | book | B | test | - | test | mined | 2026-10-27 | 90d | - |\n'; old=None
    elif name=='row_recheck':
        lines=b.splitlines(keepends=True); idx=next(i for i,x in enumerate(lines) if x.startswith(b'| S885 |')); lines[idx]=lines[idx].replace(b'| 180d |',b'| 180d and reviewed |',1); b=b''.join(lines); old=None
    elif name=='gate_quote': old='Innombrables sont les récits du monde.'.encode(); new=b'This quote is not in the evidence window.'
    elif name=='gate_long': old='Innombrables sont les récits du monde.'.encode(); new=b'one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twenty-one twenty-two twenty-three twenty-four twenty-five twenty-six.'
    elif name=='gate_reject': old=b'| S893 |'; new=b'| S893X |'
    elif name=='evidence_window': old=b'window-sha256: 94acd2bac0cc946a9ec295633f40eaa7d1951ad5e945d6a0c5595dfc53958dc7'; new=b'window-sha256: 04acd2bac0cc946a9ec295633f40eaa7d1951ad5e945d6a0c5595dfc53958dc7'
    elif name=='evidence_quote': old='quote: Innombrables sont les récits du monde.'.encode(); new='quote: Une phrase absente du texte source.'.encode()
    elif name=='evidence_window_short': old=b'window: chars=3720'; new=b'window: chars=3000'
    elif name=='index_topic': old='- `narrative-structure-frameworks.md` —'.encode(); new='- `narrative-structure-frameworks.md` — WRONG TOPIC'.encode()
    elif name=='index_footer': old=b'(total 252 files; directory totals 32/32/40/29/24/95).'; new=b'(total 251 files; directory totals 32/32/40/29/24/95).'
    elif name=='index_remove': old='- `narrative-structure-frameworks.md` —'.encode(); new=old; i=b.index(old); j=b.index(b'\n',i); b=b[:i]+b[j+1:]; old=None
    if old is not None:
        if b.count(old)!=1 and not name.startswith('gate_'): raise ValueError(f'{name}: expected one occurrence, got {b.count(old)}')
        b=b.replace(old,new,1)
    open(f,'wb').write(b); return p

names=['entry_blank','entry_short','entry_angle','row_usedby','row_extra','row_recheck','gate_quote','gate_long','gate_reject','evidence_window','evidence_quote','evidence_window_short','index_topic','index_footer','index_remove']
for name in names:
    run('git','reset','--hard','-q',LANDS)
    p=mutate(name)
    pristine=subprocess.check_output(['git','show',f'{LANDS}:{p}'],cwd=D)
    before=hashlib.sha256(pristine).hexdigest(); changed=hashlib.sha256(open(os.path.join(D,p),'rb').read()).hexdigest()
    run('git','add','--',p); run('git','-c','user.name=MutOldC fixture','-c','user.email=mutoldc@invalid','commit','-qm',f'mutant {name}')
    rev=run('git','rev-parse','HEAD',capture=True).stdout.strip()
    diff=run('git','show','--format=','--binary',rev,capture=True).stdout
    os.makedirs(os.path.join(S,'diffs'),exist_ok=True); open(os.path.join(S,'diffs',name+'.diff'),'w').write(diff)
    cmd=['python3','-B','reports/round-75/accept-c.py','--root','.', '--lands',rev,'--freeze',FREEZE,'--fleet-root','/home/vgpnk/Projects/shokunin','--work',os.path.join(S,'counter-work')]
    env=os.environ.copy(); env['HYAKU_SCRATCH']=S
    r=subprocess.run(cmd,cwd=D,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    out=r.stdout; open(os.path.join(S,'diffs',name+'.output.txt'),'w').write(out)
    legs=[x for x in out.splitlines() if x.startswith('LEG FAIL')]
    verdict=next((x for x in out.splitlines() if x.startswith('ACCEPT-C-75:')),f'EXIT={r.returncode}')
    run('git','reset','--hard','-q',LANDS)
    restored=hashlib.sha256(open(os.path.join(D,p),'rb').read()).hexdigest()
    status=run('git','status','--porcelain',capture=True).stdout.strip()
    print(f'{name}\t{rev}\t{p}\t{before}\t{changed}\t{restored}\t{verdict}\t{",".join(legs)}\tRESTORED={restored==before and not status}')
