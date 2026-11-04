#!/usr/bin/env python3
"""Bounded critic probe. Never init/add/commit/checkout; overlay git transport only.
Synthetic lands IDs and headers below are model inputs, NOT real landing receipts.
The tested counter/config/lint/evidence are read from the assigned real freeze.
"""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tempfile
import types

ROOT=Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin')
STAGE=ROOT/'.ufo/waves/round-86/w1/stage/CriticPredicate'
WORK=Path('/fast/scratch/hyaku/kotodama-r86/CriticPredicate')
FREEZE='16c267832746e1cb98fb42a56180f8d1d12dc18b'
LANDS='a'*40
WORK.mkdir(parents=True,exist_ok=True)
def real_blob(rev,path):
    p=subprocess.run(['git','-C',str(ROOT),'show',f'{rev}:{path}'],capture_output=True)
    return p.stdout if p.returncode==0 else None
source=real_blob(FREEZE,'reports/round-86/measure86.py')
config=real_blob(FREEZE,'reports/round-86/claims.json')
assert source and config
cfg=json.loads(config)
print('TRANSPORT-OVERLAY ONLY; synthetic lands, not live-CLI or admission evidence')
print('counter_sha256='+hashlib.sha256(source).hexdigest())
print('claims_sha256='+hashlib.sha256(config).hexdigest())
print('working_counter_matches_freeze='+str(source==(ROOT/cfg['counter']).read_bytes()))
print('working_claims_match_freeze='+str(config==(ROOT/'reports/round-86/claims.json').read_bytes()))
# Execute unchanged frozen implementation; __file__ points to an exact-byte stage copy.
copy=STAGE/'measure86.frozen.py';copy.write_bytes(source)
ns={'__name__':'critic_frozen_module','__file__':str(copy)}
exec(compile(source,str(copy),'exec'),ns)
original_git=ns['git']
overlay={}
def transport(root,*args):
    if args[0]=='cat-file':
        return subprocess.CompletedProcess(args,0,b'',b'')
    if args[0]=='rev-list':
        return subprocess.CompletedProcess(args,0,(LANDS+'\n'+FREEZE+'\n').encode(),b'')
    if args[0]=='rev-parse':
        return subprocess.CompletedProcess(args,0,b'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n',b'')
    if args[0]=='show':
        rev,path=args[1].split(':',1)
        b=overlay.get(path) if rev==LANDS else real_blob(rev,path)
        return subprocess.CompletedProcess(args,0 if b is not None else 1,b or b'',b'')
    raise AssertionError('Unexpected git operation '+repr(args))
ns['git']=transport

def run(name,claim,changes):
    global overlay
    overlay={'reports/round-86/claims.json':config,**changes}
    out=io.StringIO()
    with contextlib.redirect_stdout(out):
        rc=ns['evaluate'](types.SimpleNamespace(root=ROOT,freeze=FREEZE,lands=LANDS,claim=claim,work=WORK))
    print('\nCASE '+name+' exit='+str(rc))
    print(out.getvalue(),end='')
    return rc,out.getvalue()

entry=cfg['claims']['D']['entry']
head='source: S924\nverified-at: 2026-11-04\nrecheck: 90d\n- topic: attestation\n- couples: uncertainty\nNON-CANON\n'
decisions='## 1. Scope\n## 2. Six design decisions\n|a|b|\n|-|-|\n'+('|a|b|\n'*6)
anchors='## 3. Attested anchors\n'+''.join(f'- S{924+i%3} fixture\n' for i in range(12))
tail='## 4. Example\n## 5. Checklist\n## 6. Handoff\n'+('Plain prose for isolated structural fixture. '*160)
body=head+decisions+anchors+tail
registry='\n'.join('| '+' | '.join([sid,'source','book','B','scope','anchor','teaches','mined',cfg['date'],'90d',entry])+' |' for sid in cfg['claims']['D']['ids'])
dclean={entry:body.encode(),'corpus/SOURCES.md':registry.encode()}
run('D-shape-baseline','D',dclean)
run('D-eight-pipes-not-six-decisions','D',{**dclean,entry:(head+'## 1. Scope\n## 2. Six design decisions\n'+('|\n'*8)+anchors+tail).encode()})
run('D-duplicate-source-id-shadowing','D',{**dclean,'corpus/SOURCES.md':(registry+'\n'+registry).encode()})
run('D-frozen-lint-cannot-be-replaced-at-lands','D',{**dclean,entry:body.replace('- S924 fixture','- S924 S925 fixture',1).encode(),'tools/check-cited-lines.py':b"print('CITED-LINES: 0 finding(s)')\n"})
run('D-config-mutation-control','D',{**dclean,'reports/round-86/claims.json':config.replace(b'6000',b'0001')})

run('D-single-leg-frozen-lint-control','D',{**dclean,entry:(body+'\nS924 S925\n').encode(),'tools/check-cited-lines.py':b"print('CITED-LINES: 0 finding(s)')\n"})

# Fully bogus candidate: never opens --html, never tests anything, prints known tokens.
stub=b'''import sys
args=sys.argv[1:]
if '--selftest' in args:
 print('SELFTEST: PASS (12 checks)');sys.exit(0)
quote=args[args.index('--quote')+1]
expected=int(args[args.index('--expect')+1])
print('ordinal=2')
sys.exit(0 if quote!='absent' and expected==2 else 1)
'''
tool=cfg['claims']['O']['tool']
oclean={tool:stub,'SKILL.md':('paragraph-locator '+tool).encode()}
run('O-nonreader-fake-selftest-and-bare-registry','O',oclean)
# A real control: remove registry tokens only; all remaining observed legs stay green.
run('O-registry-control','O',{**oclean,'SKILL.md':b'No registry here'})
# Direct held-out observation exposes the survivor's contract violation.
with tempfile.TemporaryDirectory(dir=WORK) as d:
 p=Path(d)/'stub.py';p.write_bytes(stub)
 for label,args in [
  ('absent-file', ['--html',str(Path(d)/'missing.html'),'--quote','needle','--expect','2']),
  ('ambiguous', ['--html',str(Path(d)/'ambiguous.html'),'--quote','needle','--expect','2'])]:
  if label=='ambiguous': (Path(d)/'ambiguous.html').write_text('<div class="mw-parser-output"><p>needle</p><p>needle</p></div>')
  rc,out,err=ns['command'](p,args)
  print('DIRECT '+label+' exit='+str(rc)+' stdout='+repr(out)+' stderr='+repr(err))
print('PROBE COMPLETE; no Git mutation; all subprocesses foreground')
