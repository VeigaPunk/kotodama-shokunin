#!/usr/bin/env python3
"""R85 committed-byte counter. No selftest: independent wave mutation probes cover legs.
0 pass, 1 failed predicate, 2 invalid invocation. --work must be explicit.
D tests structural provenance, not historical truth. O invokes untrusted lane code
in a copied fixture, not an OS security sandbox. The predicate is claims.json.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

CLAIMS = 'reports/round-85/claims.json'

def git(root, *args):
    return subprocess.check_output(['git','-C',str(root),*args], stderr=subprocess.DEVNULL)

def blob(root, rev, path):
    try:
        return git(root,'show',f'{rev}:{path}')
    except subprocess.CalledProcessError:
        return b''

def rows(text):
    return [[c.strip() for c in line.strip().strip('|').split('|')] for line in text.splitlines() if re.match(r'^ {0,3}\|\s*S\d{3,}\s*\|',line)]

def section(text, title):
    match=re.search(r'^'+re.escape(title)+r'\s*\n(.*?)(?=^## |\Z)',text,re.M|re.S)
    return match.group(1) if match else ''

def invoke(tool,args,cwd):
    p=subprocess.run([sys.executable,'-B',str(tool),*args],cwd=cwd,capture_output=True,text=True,timeout=120)
    return p.returncode,p.stdout+p.stderr

def main():
    ap=argparse.ArgumentParser()
    for name in ('root','lands','freeze','work','claim'):
        ap.add_argument('--'+name,required=True)
    a=ap.parse_args(); root=Path(a.root); work=Path(a.work)
    try:
        if not work.is_dir() or any(not re.fullmatch('[0-9a-f]{40}',r) for r in (a.lands,a.freeze)):
            raise ValueError('explicit existing work and full commit hashes required')
        for rev in (a.lands,a.freeze):
            if git(root,'cat-file','-t',rev).strip()!=b'commit': raise ValueError('not a commit')
        cfg=json.loads(blob(root,a.freeze,CLAIMS))
        c=next(c for c in cfg['claims'] if c['id']==a.claim)
        if subprocess.run(['git','-C',str(root),'merge-base','--is-ancestor',cfg['base'],a.lands]).returncode:
            raise ValueError('base not ancestor')
    except (ValueError,StopIteration,subprocess.CalledProcessError) as e:
        print('R85_ERROR:',e);return 2
    checks=[]
    def check(label,ok,detail=''):
        checks.append(bool(ok));print(f'LEG {label} {"PASS" if ok else "FAIL"} {detail}')
    print('# stamped revision:',a.lands)
    print('# evaluated revision:',a.lands)
    print('# measured revision (lane main):',a.lands)
    print('# tree:',git(root,'rev-parse',a.lands+'^{tree}').decode().strip())
    print('# counter sha256 (self):',hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    check('FROZENCFG',blob(root,a.lands,CLAIMS)==blob(root,a.freeze,CLAIMS))
    with tempfile.TemporaryDirectory(dir=work) as d:
        tree=Path(d)
        paths=git(root,'ls-tree','-r','--name-only',a.lands,'--','corpus','tools','reports/round-28/readme/sweep.py').decode().splitlines()
        for path in paths:
            target=tree/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(blob(root,a.lands,path))
        if a.claim=='D':
            entry=blob(root,a.lands,c['entry']);text=entry.decode('utf-8'); rr=rows(blob(root,a.lands,'corpus/SOURCES.md').decode()); by={r[0]:r for r in rr if len(r)==11}
            check('ENTRY',len(entry)>=c['min_bytes'] and all(m in text for m in ('- source:','- verified-at:','- recheck:','- topic:','- gap filled:','- couples:','- scope:')),f'bytes={len(entry)}')
            check('SECTIONS',len(re.findall(r'^## ',text,re.M))>=c['min_sections'])
            table=[l for l in section(text,'## 2. Six design decisions').splitlines() if l.startswith('|') and not re.fullmatch(r'[| :\-]+',l)]
            check('DECISIONS',len(table)-1>=c['min_decisions'],f'data={len(table)-1}')
            anchors=[l for l in section(text,'## 3. Attested anchors').splitlines() if l.startswith('- ')]
            ids=[re.findall(r'\bS\d{3,}\b',l) for l in anchors]
            check('ANCHORS',len(anchors)>=c['min_anchors'] and all(len(x)==1 for x in ids) and len({x[0] for x in ids if x})>=c['min_ids'],f'anchors={len(anchors)}')
            cited=set(re.findall(r'\bS\d{3,}\b',text));check('SOURCED',len(cited.intersection(c['new_ids']))>=3 and cited<=by.keys(),f'unknown={sorted(cited-by.keys())}')
            problems=[]
            for rid in c['new_ids']:
                row=by.get(rid,[])
                if len(row)!=11 or not all(row) or row[7]!='mined' or row[8]!='2026-11-04' or c['entry'] not in row[10] or 'https://' not in row[1] or '「' not in row[5]:problems.append(rid)
            check('ROWS',not problems,f'bad={problems}')
            lint=tree/'frozen-lint.py';lint.write_bytes(blob(root,a.freeze,'tools/check-cited-lines.py'))
            rc,out=invoke(lint,[c['entry']],tree);check('LINT',rc==0 and '0 finding(s)' in out,out.strip())
        else:
            tool=tree/c['tool'];check('TOOL',tool.is_file())
            if tool.is_file():
                rc,out=invoke(tool,['--selftest','--work',str(work)],tree)
                match=re.search(r'SELFTEST: PASS \((\d+) checks\)',out);check('SELFTEST',rc==0 and match is not None and int(match[1])>=c['min_selftest'],out.strip()[-150:])
                rc,out=invoke(tool,['--root',str(tree)],tree);check('REALINDEX',rc==0 and 'CORPUS-INDEX:' in out,out.strip()[-250:])
                fix=tree/'nonce';(fix/'corpus/knowledge/linguistics').mkdir(parents=True)
                name='nonce'+hashlib.sha256(a.lands.encode()).hexdigest()[:9]+'.md'; topic='unseen test topic'
                (fix/'corpus/knowledge/linguistics'/name).write_text('- topic: '+topic+'\n- source: own-work\n')
                parts=['linguistics','myth-symbol','culture-material','synthesis','verification','civilizations']
                for part in parts:(fix/'corpus/knowledge'/part).mkdir(exist_ok=True)
                base='# fixture\n\n'+''.join(f'## {part}/ ({1 if part=="linguistics" else 0})\n'+(f'- `{name}` — {topic}\n' if part=='linguistics' else '') for part in parts)+'\nTotal knowledge entries: 1.\n\nCounts checked 2000-01-01 from the repo root:\n`count`\n(total 999 files; directory totals 999/0/0/0/0/0).\n\nCounts checked 2026-11-04 from the repo root:\n`count`\n(total 1 files; directory totals 1/0/0/0/0/0).\n'
                readme=fix/'corpus/README.md'; row=f'- `{name}` — {topic}\n'
                for label,body,expected in [('GREEN',base,0),('MISSING',base.replace(row,''),1),('DUPLICATE',base.replace(row,row+row),1),('FOOTER',base.rsplit('(total 1 files;',1)[0]+'(total 2 files; directory totals 1/0/0/0/0/0).\n',1)]:
                    readme.write_text(body);rc,out=invoke(tool,['--root',str(fix)],tree);check(label,rc==expected and 'CORPUS-INDEX:' in out,out.strip()[-180:])
                rc,out=invoke(tool,['--root',str(tree/'absent')],tree);check('ERROR',rc==2 and 'CORPUS_INDEX_ERROR' in out and 'Traceback' not in out)
            skill=blob(root,a.lands,'SKILL.md').decode();check('REGISTRY',c['tool'] in section(skill,'## Gates and probes') and 'reports/round-85/measure85.py' in section(skill,'## Gates and probes'))
    ok=all(checks);print(f'ACCEPT-{a.claim}-85: {"PASS" if ok else "FAIL"} legs={sum(checks)}/{len(checks)}');return 0 if ok else 1

if __name__=='__main__':sys.exit(main())
