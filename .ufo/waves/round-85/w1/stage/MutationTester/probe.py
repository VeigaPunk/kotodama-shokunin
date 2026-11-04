#!/usr/bin/env python3
"""Commit-free mutation sensitivity probes. Never an acceptance-revision receipt.
Imports byte-exact frozen counter; overlays only blob transport and ls-tree path
enumeration for uncommitted fixture bytes. Predicates/constants stay unchanged.
"""
import argparse, contextlib, difflib, hashlib, importlib.util, io, json
from pathlib import Path
import shutil, subprocess, sys

HERE=Path(__file__).resolve().parent
LANE=Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin')
FREEZE='ed816e71a97dde9b65f9265276b77c7583274671'
SCRATCH=Path('/fast/scratch/hyaku/kotodama-r85/MutationTester')
ENTRY='corpus/knowledge/culture-material/metallurgy-metal-register.md'
TOOL='tools/check-corpus-index.py'
sha=lambda b: hashlib.sha256(b).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--candidate',type=Path);ap.add_argument('--readme',type=Path);a=ap.parse_args()
    SCRATCH.mkdir(parents=True,exist_ok=True)
    work=SCRATCH/'work';work.mkdir(exist_ok=True)
    spec=importlib.util.spec_from_file_location('frozen',HERE/'measure85.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    original_blob,original_git=m.blob,m.git
    source=original_blob(LANE,FREEZE,'reports/round-85/measure85.py')
    assert source==(HERE/'measure85.py').read_bytes()
    overlay={}
    m.blob=lambda root,rev,path: overlay[path] if rev==FREEZE and path in overlay else original_blob(root,rev,path)
    def git(root,*args):
        result=original_git(root,*args)
        if args[:3]==('ls-tree','-r','--name-only'):
            paths=set(result.decode().splitlines())|set(overlay)
            return ('\n'.join(sorted(paths))+'\n').encode()
        return result
    m.git=git
    results=[]
    def counter(claim):
        old=sys.argv;sys.argv=[str(HERE/'measure85.py'),'--root',str(LANE),'--lands',FREEZE,'--freeze',FREEZE,'--work',str(work),'--claim',claim]
        out=io.StringIO()
        try:
            with contextlib.redirect_stdout(out):rc=m.main()
        finally:sys.argv=old
        return rc,out.getvalue()
    def record(name,claim,clean,mutant):
        overlay.clear();overlay.update(clean)
        rc0,out0=counter(claim)
        overlay.clear();overlay.update(mutant)
        rc1,out1=counter(claim)
        overlay.clear();overlay.update(clean)
        rc2,out2=counter(claim)
        restored=all(overlay[p]==b for p,b in clean.items())
        verdict='inconclusive' if rc0!=0 or rc2!=0 else ('killed' if rc1==1 else 'survived' if rc1==0 else 'inconclusive')
        diff=''.join(''.join(difflib.unified_diff(clean.get(p,b'').decode().splitlines(True),mutant.get(p,b'').decode().splitlines(True),fromfile=p+'.clean',tofile=p+'.mutant')) for p in sorted(set(clean)|set(mutant)))
        (HERE/(name+'.diff')).write_text(diff)
        receipt=f'NON-ACCEPTANCE BYTE-OVERLAY PROBE; frozen predicates unchanged\nBASELINE rc={rc0}\n{out0}\nMUTANT rc={rc1}\n{out1}\nRESTORED rc={rc2}\n{out2}\n'
        (HERE/(name+'.txt')).write_text(receipt)
        results.append({'name':name,'claim':claim,'baseline_rc':rc0,'mutant_rc':rc1,'restored_rc':rc2,'verdict':verdict,'restored_exact':restored,'hashes':{p:{'before':sha(clean.get(p,b'')),'mutant':sha(mutant.get(p,b'')),'after':sha(overlay.get(p,b''))} for p in set(clean)|set(mutant)},'failed_legs':[l for l in out1.splitlines() if l.startswith('LEG ') and ' FAIL' in l]})
    text='# SYNTHETIC COUNTER SUBSTRATE; NOT SCHOLARSHIP\n'+''.join('- '+key+': synthetic fixture only\n' for key in ['source','verified-at','recheck','topic','gap filled','couples','scope'])
    text+='\n## 1. Scope\nSynthetic structural probe only.\n## 2. Six design decisions\n| Choice | Scope |\n|---|---|\n'+''.join(f'| decision {i} | synthetic |\n' for i in range(6))
    text+='## 3. Attested anchors\n'+''.join(f'- Synthetic anchor {i}: S{919+i%4}.\n' for i in range(24))
    text+=''.join(f'## {i}. Probe section\n'+('Synthetic substrate for testing structural predicates; no historical assertion or source authenticity is claimed.\n'*45) for i in range(4,8))
    rows=original_blob(LANE,FREEZE,'corpus/SOURCES.md').decode()
    added=[]
    for i,title in enumerate(['Metallurgy','Iron','Bronze','Alloys'],919):
        added.append(f'| S{i} | https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/{title} | book | B | dated terminology only; SYNTHETIC | fixture locator: 「synthetic quote」 | probe only | mined | 2026-11-04 | 180d | {ENTRY} |\n')
    pristine={ENTRY:text.encode(),'corpus/SOURCES.md':(rows+'\n'+''.join(added)).encode()}
    adulterated=dict(pristine);adulterated['corpus/SOURCES.md']=pristine['corpus/SOURCES.md'].replace(b'Britannica/Metallurgy',b'Britannica/Bronze_Age')
    record('D-source-adulterated', 'D',pristine,adulterated)
    unknown=dict(pristine);unknown[ENTRY]=pristine[ENTRY].replace(b'Synthetic anchor 0: S919',b'Synthetic anchor 0: S99999')
    record('D-unknown-anchor','D',pristine,unknown)
    omitted=dict(pristine);omitted['corpus/SOURCES.md']=pristine['corpus/SOURCES.md'].replace(added[2].encode(),b'')
    record('D-omitted-row','D',pristine,omitted)
    malformed=dict(pristine);malformed['corpus/SOURCES.md']=pristine['corpus/SOURCES.md'].replace(added[0].encode(),added[0].replace('https://','http://').encode())
    record('D-source-shape','D',pristine,malformed)
    if a.candidate:
        candidate=a.candidate.read_bytes()
        (HERE/'candidate-tool.py').write_bytes(candidate)
        toolroot=SCRATCH/'candidate-tree'
        localtool=toolroot/TOOL;localtool.parent.mkdir(parents=True,exist_ok=True);localtool.write_bytes(candidate)
        lineage=toolroot/'reports/round-28/readme/sweep.py'
        lineage.parent.mkdir(parents=True,exist_ok=True)
        lineage.write_bytes(original_blob(LANE,FREEZE,'reports/round-28/readme/sweep.py'))
        for path in original_git(LANE,'ls-tree','-r','--name-only','0d181583b18ae94e80a251ca5ab5f3055b16c74c','--','corpus').decode().splitlines():
            target=toolroot/path;target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes(original_blob(LANE,'0d181583b18ae94e80a251ca5ab5f3055b16c74c',path))
        for name,args in [('candidate-selftest',['--selftest','--work',str(work)]),('candidate-base-index',['--root',str(toolroot)])]:
            cmd=[sys.executable,'-B',str(localtool),*args]
            p=subprocess.run(cmd,cwd=SCRATCH,capture_output=True,text=True,timeout=120)
            (HERE/(name+'.txt')).write_text('command: '+repr(cmd)+'\nrc='+str(p.returncode)+'\n'+p.stdout+p.stderr)
        clean={TOOL:candidate,'SKILL.md':b'## Gates and probes\n'+TOOL.encode()+b' reports/round-85/measure85.py\n'}
        # Repaired real index supplied next to candidate when available; otherwise
        # a nonce-only whole corpus overlay would retain base files. Direct probes
        # below are independent of REALINDEX acceptance.
        fix=SCRATCH/'index-fixture'
        parts=['linguistics','myth-symbol','culture-material','synthesis','verification','civilizations']
        for part in parts:(fix/'corpus/knowledge'/part).mkdir(parents=True,exist_ok=True)
        (fix/'corpus/knowledge/linguistics/nonce.md').write_text('- topic: unseen topic\n- source: own-work\n')
        row='- `nonce.md` — unseen topic\n'
        base='# fixture\n\n'+''.join(f'## {p}/ ({int(p=="linguistics")})\n'+(row if p=='linguistics' else '') for p in parts)+'\nTotal knowledge entries: 1.\n\nCounts checked 2000-01-01 from the repo root:\n`count`\n(total 999 files; directory totals 999/0/0/0/0/0).\n\nCounts checked 2026-11-04 from the repo root:\n`count`\n(total 1 files; directory totals 1/0/0/0/0/0).\n'
        readme=fix/'corpus/README.md'
        for name,body in [('O-omitted-row',base.replace(row,'')),('O-duplicate-row',base.replace(row,row+row)),('O-last-footer',base.replace('(total 1 files;','(total 2 files;'))]:
            runs=[]
            try:
                for label,content in [('baseline',base),('mutant',body),('restored',base)]:
                    readme.write_text(content)
                    cmd=[sys.executable,'-B',str(localtool),'--root',str(fix)]
                    p=subprocess.run(cmd,cwd=SCRATCH,capture_output=True,text=True,timeout=120)
                    runs.append({'phase':label,'rc':p.returncode,'output':p.stdout+p.stderr,'sha256':sha(readme.read_bytes()),'command':cmd})
            finally:readme.write_text(base)
            verdict='inconclusive' if runs[0]['rc']!=0 or runs[2]['rc']!=0 else ('killed' if runs[1]['rc']==1 else 'survived' if runs[1]['rc']==0 else 'inconclusive')
            (HERE/(name+'.json')).write_text(json.dumps(runs,indent=2)+'\n')
            (HERE/(name+'.diff')).write_text(''.join(difflib.unified_diff(base.splitlines(True),body.splitlines(True),fromfile='README.clean',tofile='README.mutant')))
            results.append({'name':name,'verdict':verdict,'candidate_sha256':sha(candidate),'runs':runs,'restored_exact':readme.read_bytes()==base.encode()})
        # Supply full real candidate corpus repair if staged beside tool.
        readme_candidate=a.readme
        if readme_candidate is not None:clean['corpus/README.md']=readme_candidate.read_bytes()
        canned=dict(clean);canned[TOOL]=b'import sys\nprint("SELFTEST: PASS (99 checks)" if "--selftest" in sys.argv else "CORPUS-INDEX: clean")\nsys.exit(0)\n'
        record('O-canned-all-clean','O',clean,canned)
    (HERE/'results.json').write_text(json.dumps({'frozen_sha256':sha(source),'mode':'transport-overlay; not committed-revision acceptance','results':results},indent=2)+'\n')
    print(json.dumps([{'name':r['name'],'verdict':r['verdict']} for r in results],indent=2))
    shutil.rmtree(SCRATCH)

if __name__=='__main__':main()
