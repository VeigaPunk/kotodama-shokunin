import hashlib,json,subprocess,sys
from pathlib import Path
R=Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin');W=Path('/fast/scratch/hyaku/kotodama-r86/MutParagraph');S=R/'.ufo/waves/round-86/w1/stage/MutParagraph'
source=R/'.ufo/waves/round-86/w1/stage/ExecParagraph/check-paragraph-locator.py'
original=source.read_bytes();target=W/'locator.py'
old=b"c.endswith('caption')";new=b"c == 'caption'"
assert original.count(old)==1
sha=lambda b:hashlib.sha256(b).hexdigest()
record={'candidate_source':str(source),'before_sha256':sha(original),'counter_sha256_before':sha((R/'reports/round-86/measure86.py').read_bytes()),'mutation':{'old':old.decode(),'new':new.decode()},'phases':{}}
def phase(name):
 p=subprocess.run([sys.executable,'-B',str(W/'probe.py')],cwd=W,capture_output=True,text=True,timeout=120)
 v={'driver_exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'locator_sha256':sha(target.read_bytes())}
 if p.returncode==0:v['result']=json.loads(p.stdout)
 record['phases'][name]=v
 (S/(name+'.json')).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
try:
 target.write_bytes(original);phase('pristine')
 if record['phases']['pristine']['driver_exit']!=0:raise RuntimeError('pristine driver failed')
 base=record['phases']['pristine']['result']
 if not all(c['matches'] for c in base['direct']) or base['counter_overlay']['exit']!=0:raise RuntimeError('clean green prerequisite failed; no mutation applied')
 target.write_bytes(original.replace(old,new));phase('mutated')
finally:
 target.write_bytes(original);phase('restored')
 record['after_sha256']=sha(target.read_bytes());record['source_after_sha256']=sha(source.read_bytes());record['counter_sha256_after']=sha((R/'reports/round-86/measure86.py').read_bytes())
 record['exact_restoration']=target.read_bytes()==original
 (S/'receipt.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(record,ensure_ascii=False,indent=2))
