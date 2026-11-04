import contextlib, hashlib, importlib.util, io, json, shutil, subprocess, sys
from pathlib import Path
R=Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin')
W=Path('/fast/scratch/hyaku/kotodama-r86/MutParagraph')
ST=R/'.ufo/waves/round-86/w1/stage/MutParagraph'
C=R/'reports/round-86/measure86.py'
def digest(b):return hashlib.sha256(b).hexdigest()
def run(args):
 p=subprocess.run([sys.executable,'-B',str(W/'locator.py'),*args],capture_output=True,text=True,timeout=30)
 return {'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
def direct():
 cases=[
 ('nav','<div class="mw-parser-output"><nav><p>needle</p></nav><p>opening</p><p>needle</p></div>','needle',2,0),
 ('caption','<div class="mw-parser-output"><p>opening</p><figure><figcaption><p>needle</p></figcaption></figure><p>needle</p></div>','needle',2,0),
 ('generic-caption','<div class="mw-parser-output"><div class="image-caption"><p>needle</p></div><p>opening</p><p>needle</p></div>','needle',2,0),
 ('extraneous','<p>needle</p><div class="mw-parser-output"><p>opening</p><p>needle</p></div><p>needle</p>','needle',2,0),
 ('multiple-roots','<div class="mw-parser-output"><p>opening</p></div><div class="mw-parser-output"><p>needle</p></div>','needle',2,2),
 ('nested-entities-unicode','<div class="mw-parser-output"><p>opening</p><p>café <b>naïve &amp; <i>wise</i></b>\u00a0tail</p></div>','café naïve & wise tail',2,0),
 ('absent','<div class="mw-parser-output"><p>opening</p><p>needle</p></div>','missing',1,1),
 ('duplicate-paragraphs','<div class="mw-parser-output"><p>needle</p><p>needle</p></div>','needle',1,1),
 ('duplicate-same-paragraph','<div class="mw-parser-output"><p>needle then needle</p></div>','needle',1,0),
 ('nested-roots','<div class="mw-parser-output"><p>opening</p><div class="mw-parser-output"><p>needle</p></div><p>tail</p></div>','needle',2,2),
 ]
 out=[]
 for name,html,q,e,expected in cases:
  h=W/(name+'.html');h.write_text(html)
  v=run(['--html',str(h),'--quote',q,'--expect',str(e)])
  v.update(name=name,expected_exit=expected,matches=v['exit']==expected,html=html,quote=q,expect=e)
  out.append(v)
 return out

def counter():
 spec=importlib.util.spec_from_file_location('counter_overlay',C);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 cfg=(R/'reports/round-86/claims.json').read_bytes();config=json.loads(cfg);freeze='16c267832746e1cb98fb42a56180f8d1d12dc18b';lands='f'*40
 def git(root,*a):
  data= ((lands+'\n'+freeze+'\n') if a[0]=='rev-list' else ('0'*40+'\n') if a[0]=='rev-parse' else '').encode()
  return subprocess.CompletedProcess(a,0,data,b'')
 def blob(root,rev,path):
  if path==m.CONFIG:return cfg
  if path==config['claims']['O']['tool']:return None if rev==config['base'] else (W/'locator.py').read_bytes()
  if path==config['claims']['O']['html']:return (R/path).read_bytes()
  if path=='SKILL.md':return b'tools/check-paragraph-locator.py paragraph-locator'
  return None
 m.git=git;m.blob=blob
 a=type('Args',(),dict(root=R,freeze=freeze,lands=lands,claim='O',work=W))()
 o=io.StringIO()
 with contextlib.redirect_stdout(o):rc=m.evaluate(a)
 return {'exit':rc,'stdout':o.getvalue(),'note':'In-memory blob/commit transport only; no commits created. Real frozen evaluate and subprocess detector.'}
if __name__=='__main__':
 result={'direct':direct(),'counter_overlay':counter()}
 print(json.dumps(result,ensure_ascii=False,indent=2))
