#!/usr/bin/env python3
"""Round 86 frozen counter. --selftest exercises the real CLI over isolated Git fixtures.
0 clean, 1 failed, 2 could-not-evaluate/refused. No live-tree writes or network.
All evaluation reads committed blobs. Semantic source support remains review-only.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

CONFIG = 'reports/round-86/claims.json'
LEGS = {'D': ['FROZENCFG','BEFORE','ENTRY','DECISIONS','ANCHORS','ROWS','LINT'],
        'O': ['FROZENCFG','BEFORE','TOOL','SELFTEST','IRON_RED','IRON_GREEN','HELDOUT','REGISTRY']}

def git(root, *args):
    return subprocess.run(['git','-C',str(root),*args],capture_output=True)

def blob(root, rev, path):
    p=git(root,'show',f'{rev}:{path}')
    return p.stdout if p.returncode==0 else None

def text(root,rev,path):
    return (blob(root,rev,path) or b'').decode('utf-8')

def sha(b):
    return hashlib.sha256(b).hexdigest()

def command(path,args):
    p=subprocess.run([sys.executable,'-B',str(path),*args],capture_output=True,text=True,timeout=60)
    return p.returncode,p.stdout,p.stderr

def rows(s):
    out={}
    for line in s.splitlines():
        if re.match(r'^ {0,3}\|\s*S\d{3,}\s*\|',line):
            c=[x.strip() for x in line.strip().strip('|').split('|')]
            if len(c)==11: out[c[0]]=c
    return out

def evaluate(a):
    label=f'ACCEPT-{a.claim}-86'; legs=LEGS[a.claim]
    try:
        for rev in (a.freeze,a.lands):
            if not re.fullmatch('[0-9a-f]{40}',rev) or git(a.root,'cat-file','-e',rev+'^{commit}').returncode:
                raise ValueError('full commit id required')
        chain=git(a.root,'rev-list','--first-parent',a.lands).stdout.decode().split()
        if a.freeze not in chain: raise ValueError('freeze not on lands first-parent chain')
        cfg=json.loads(text(a.root,a.freeze,CONFIG)); c=cfg['claims'][a.claim]
        if c['legs']!=legs: raise ValueError('LEGCOUNT')
        if not Path(a.work).is_dir(): raise ValueError('existing --work required')
        if a.lands==cfg['base']: raise ValueError('unchanged base')
        print(f'# stamped revision: {a.lands}\n# evaluated revision: {a.lands}\n# measured revision (lane main): {a.lands}')
        print('# tree: '+git(a.root,'rev-parse',a.lands+'^{tree}').stdout.decode().strip())
        print('# counter sha256 (self): '+sha(Path(__file__).read_bytes()))
        print('# frozen legs: '+str(len(legs))+' ('+','.join(legs)+')')
        results=[]
        def grade(name,ok,detail=''):
            results.append((name,bool(ok)));print(f'LEG {"PASS" if ok else "FAIL"} {name} {detail}')
        grade('FROZENCFG',blob(a.root,a.lands,CONFIG)==blob(a.root,a.freeze,CONFIG))
        with tempfile.TemporaryDirectory(prefix='measure86-',dir=a.work) as d:
            d=Path(d)
            if a.claim=='D':
                entry=c['entry']; b=blob(a.root,a.lands,entry); s=(b or b'').decode('utf-8')
                grade('BEFORE',blob(a.root,cfg['base'],entry) is None)
                grade('ENTRY',b is not None and len(b)>=c['min_bytes'] and len(re.findall(r'^## ',s,re.M))>=6 and all(x in s for x in ('source:','verified-at:','recheck:','- topic:','- couples:','NON-CANON')),'bytes='+str(len(b or b'')))
                section=s.split('## 2. Six design decisions',1)[-1].split('\n## ',1)[0] if '## 2. Six design decisions' in s else ''
                table=[l for l in section.splitlines() if l.startswith('|')]
                grade('DECISIONS',len(table)>=8,'table-lines='+str(len(table)))
                section=s.split('## 3. Attested anchors',1)[-1].split('\n## ',1)[0] if '## 3. Attested anchors' in s else ''
                bullets=[l for l in section.splitlines() if l.startswith('- ')]
                ids=[re.findall(r'\bS\d{3,}\b',l) for l in bullets]
                grade('ANCHORS',len(bullets)>=12 and all(len(set(x))==1 for x in ids) and set(c['ids'])<=set(sum(ids,[])),'bullets='+str(len(bullets)))
                rr=rows(text(a.root,a.lands,'corpus/SOURCES.md'))
                good=all(i in rr and all(rr[i]) and rr[i][7]=='mined' and rr[i][8]==cfg['date'] and entry in rr[i][10] for i in c['ids'])
                grade('ROWS',good)
                lint=blob(a.root,a.freeze,'tools/check-cited-lines.py')
                if lint is None or sha(lint)!=cfg['lint_sha256']: raise ValueError('frozen lint authority mismatch')
                (d/'lint.py').write_bytes(lint);(d/'entry.md').write_text(s)
                rc,out,err=command(d/'lint.py',[str(d/'entry.md')])
                grade('LINT',rc==0 and re.search(r'CITED-LINES: 0 finding',out) is not None,out.strip())
            else:
                tool=c['tool']; b=blob(a.root,a.lands,tool)
                grade('BEFORE',blob(a.root,cfg['base'],tool) is None)
                grade('TOOL',b is not None)
                if b is not None:
                    p=d/'locator.py';p.write_bytes(b)
                    rc,out,err=command(p,['--selftest','--work',str(d)])
                    n=re.search(r'SELFTEST: PASS \((\d+) checks\)',out)
                    grade('SELFTEST',rc==0 and n is not None and int(n[1])>=12,out.strip())
                    html=blob(a.root,a.freeze,c['html']);(d/'iron.html').write_bytes(html or b'')
                    for expected,leg,code in ((1,'IRON_RED',1),(2,'IRON_GREEN',0)):
                        rc,out,err=command(p,['--html',str(d/'iron.html'),'--quote',c['quote'],'--expect',str(expected)])
                        grade(leg,rc==code and 'ordinal=2' in out,out.strip())
                    held='<div class="mw-parser-output"><p>first anchor</p><p>second <b>needle</b> tail</p><figure><p>caption needle</p></figure></div>'
                    (d/'held.html').write_text(held)
                    tests=[('second needle tail',2,0),('second needle tail',1,1),('absent',1,1),('needle',2,0)]
                    ok=True
                    for quote,expected,code in tests:
                        rc,out,err=command(p,['--html',str(d/'held.html'),'--quote',quote,'--expect',str(expected)])
                        ok &= rc==code and 'Traceback' not in out+err
                    grade('HELDOUT',ok)
                else:
                    for name in ('SELFTEST','IRON_RED','IRON_GREEN','HELDOUT'):grade(name,False,'tool absent')
                skill=text(a.root,a.lands,'SKILL.md')
                grade('REGISTRY',tool in skill and 'paragraph-locator' in skill)
        if [x[0] for x in results]!=legs:raise ValueError('runtime LEGCOUNT')
        n=sum(x[1] for x in results);ok=n==len(legs)
        print(f'{label}: {"PASS" if ok else "FAIL"} legs={n}/{len(legs)}')
        return 0 if ok else 1
    except (ValueError,KeyError,OSError,UnicodeError,subprocess.TimeoutExpired) as e:
        print(f'{label}: FAIL legs=0/{len(legs)} (refused: {e})');return 2

def selftest(work):
    """Run the public D CLI, clean first, then independent entry/config/row mutations."""
    with tempfile.TemporaryDirectory(prefix='counter-selftest-',dir=work) as d:
        root=Path(d);git(root,'init','-q');git(root,'config','user.name','fixture');git(root,'config','user.email','fixture@invalid')
        def put(p,s):
            f=root/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(s)
        def commit():
            git(root,'add','.');p=git(root,'commit','-qm','fixture')
            if p.returncode:raise ValueError(p.stderr.decode())
            return git(root,'rev-parse','HEAD').stdout.decode().strip()
        put('base','base');base=commit()
        lint="print('CITED-LINES: 0 finding(s) in 1 file(s)')\n"
        cfg={'base':base,'date':'2026-11-04','lint_sha256':sha(lint.encode()),'claims':{'D':{'entry':'entry.md','min_bytes':1,'ids':['S924','S925','S926'],'legs':LEGS['D']}}}
        put(CONFIG,json.dumps(cfg));put('tools/check-cited-lines.py',lint);freeze=commit()
        entry='source: S924\nverified-at: today\nrecheck: local\n- topic: fixture\n- couples: fixture\nNON-CANON\n## 1. Scope\n## 2. Six design decisions\n|a|b|\n|-|-|\n'+('|a|b|\n'*6)+'## 3. Attested anchors\n'+''.join(f'- S{924+i%3} fixture\n' for i in range(12))+'## 4. Example\n## 5. Checklist\n## 6. Handoff\n'
        registry='\n'.join('| '+ ' | '.join([i,'source','book','B','scope','anchor','teaches','mined','2026-11-04','90d','entry.md'])+' |' for i in cfg['claims']['D']['ids'])
        put('entry.md',entry);put('corpus/SOURCES.md',registry);clean=commit();checks=0
        def run(rev,code,label):
            nonlocal checks
            rc,out,err=command(Path(__file__),['--root',str(root),'--lands',rev,'--freeze',freeze,'--claim','D','--work',str(root)])
            if rc!=code or label not in out:raise ValueError(f'selftest {label}: rc={rc} {out} {err}')
            print(f'selftest: {label} exit={rc}');checks+=1
        run(clean,0,'ACCEPT-D-86: PASS')
        for path,value,leg in [('entry.md','stub','ENTRY'),('entry.md',entry.replace('|a|b|\n',''),'DECISIONS'),('entry.md',entry.replace('- S924 fixture','- no id'),'ANCHORS'),('corpus/SOURCES.md','','ROWS'),(CONFIG,json.dumps({**cfg,'date':'wrong'}),'FROZENCFG')]:
            git(root,'checkout','-q',clean);put(path,value);rev=commit();run(rev,1,'LEG FAIL '+leg)
        run(freeze,1,'LEG FAIL ENTRY')
        run(base,2,'refused:')
        print(f'COUNTER-SELFTEST: PASS ({checks} checks; clean green first)')
    return 0

def main():
    p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--lands');p.add_argument('--freeze');p.add_argument('--claim',choices=LEGS);p.add_argument('--work',required=True);p.add_argument('--selftest',action='store_true');a=p.parse_args()
    if a.selftest:return selftest(a.work)
    if not a.lands or not a.freeze or not a.claim:p.error('--lands --freeze --claim required')
    return evaluate(a)
if __name__=='__main__':sys.exit(main())
