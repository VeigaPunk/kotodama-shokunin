import subprocess, json, hashlib, os, sys, shutil, re
W='/fast/scratch/hyaku/kotodama-r89/CriticClaims'
LANE='/home/vgpnk/Projects/shokunin/kotodama-shokunin'
D=os.path.join(W,'clone')
def g(*a, **k):
    p=subprocess.run(['git','-C',D]+list(a),capture_output=True,text=True)
    if p.returncode: print('GIT',a,p.stderr); sys.exit(3)
    return p.stdout.strip()
shutil.rmtree(D,ignore_errors=True)
subprocess.run(['git','clone','-q','--shared','--no-checkout',LANE,D],check=True)
assert g('rev-parse','--show-toplevel')==D
g('config','user.email','critic@fixture'); g('config','user.name','fixture')
START='9ad00be1'
FREEZE=g('rev-parse','1cbd0efc')
pop=["S009","S012","S020","S021","S031","S032","S033","S084","S104","S105","S106","S107","S142","S157","S163","S875"]
quotes={"S009":"Conlang Atlas of Language Structures","S012":"phonology, morphology, syntax, lexicon","S020":"Automated Motif Indexing on the Arabian Nights","S021":"Do Large Language Models Always Tell The Same Stories?","S031":"The Myth of Man the Hunter","S032":"Female foragers sometimes hunt, yet gendered divisions of labor are real","S033":"Correction: The Myth of Man the Hunter","S084":"SignWriting for Sign Languages","S104":"French Sign Language family","S105":"American Sign Language"}
urls=json.load(open(W+'/urls.json'))
NEW='2027-11-05'  # as_of+366: maximal cadence weakening
def put(path,data):
    p=os.path.join(D,path); os.makedirs(os.path.dirname(p),exist_ok=True)
    open(p,'wb').write(data if isinstance(data,bytes) else data.encode())
def set_cell(text,rid,idx,val):
    out=[]
    for line in text.split('\n'):
        if re.match(r'^\s{0,3}\|\s*%s\s*\|'%rid,line):
            c=line.strip().strip('|').split('|'); c[idx]=' %s '%val; line='|'+'|'.join(c)+'|'
        out.append(line)
    return '\n'.join(out)
def f_overlay(src,lesson):
    man={}
    for rid,q in quotes.items():
        src=set_cell(src,rid,9,NEW)
        cap=open(W+'/cap/%s.raw'%rid,'rb').read()
        cp='reports/round-89/rechecks/%s.html'%rid; put(cp,cap)
        man[rid]=dict(capture=cp,sha256=hashlib.sha256(cap).hexdigest(),http_status=200,fetched_at='2026-11-04T19:11:00-03:00',url=urls[rid][0])
        lesson+='- %s LOCATED recheck 90d→%s accessed 2026-11-04 "%s"\n'%(rid,NEW,q)
    for rid in pop:
        if rid not in quotes: lesson+='- %s NOT-LOCATED\n'%rid
    put('reports/round-89/rechecks/manifest.json',json.dumps({'rows':man}))
    return src,lesson
SP=open(LANE+'/corpus/knowledge/linguistics/semantics-pragmatics.md').read()
SEC=SP[SP.find('## 4. Evidentiality'):SP.find('## 5. Implicature')]
CSRC=[('S936','https://wals.info/chapter/77','chapter_77','Semantic Distinctions of Evidentiality'),('S937','https://wals.info/chapter/78','chapter_78','Coding of Evidentiality'),('S938','https://wals.info/feature/77A','feature_77A','Semantic Distinctions of Evidentiality')]
def c_overlay(src,lesson,cite_pop=False):
    body='# Evidentiality and epistemic marking\n\n- topic: evidentiality\n- sources: S936, S937, S938%s\n- verified-at: 2026-11-04\n- recheck: 90d\n\n'%(', S009' if cite_pop else '')
    body+=SEC
    i=0
    while len(body.encode())<8200:
        i+=1; body+='\n## Design note %d\n\nEvidential choice is a social fact and a grammatical habit; a culture that marks source must decide who may infer for whom, and courts, rumours and prophecy inherit that decision. '%i*1
    put('corpus/knowledge/linguistics/evidentiality-epistemic-marking.md',body)
    man={}
    for rid,u,f,q in CSRC:
        src=src.rstrip('\n')+'\n| %s | WALS %s — %s | web | A | typology | title | evidentiality | mined | 2026-11-04 | 90d | knowledge/linguistics/evidentiality-epistemic-marking.md |\n'%(rid,f,u)
        cap=open(W+'/cap/wals_%s.raw'%f,'rb').read(); cp='reports/round-89/evidence/%s.html'%rid; put(cp,cap)
        man[rid]=dict(capture=cp,sha256=hashlib.sha256(cap).hexdigest(),http_status=200,fetched_at='2026-11-04T19:20:00-03:00',url=u)
        lesson+='- %s %s 2026-11-04 "%s"\n'%(rid,u,q)
    if cite_pop:
        src=set_cell(src,'S009',10,'knowledge/linguistics/evidentiality-epistemic-marking.md')
    put('reports/round-89/evidence/manifest.json',json.dumps({'rows':man}))
    rd=open(D+'/corpus/README.md').read().replace('## linguistics/ (33)','## linguistics/ (34)')
    rd+='\n## Fixture evidentiality entry (2026-11-04)\n\n- `evidentiality-epistemic-marking.md` — evidentiality\n\nTotal knowledge entries: 261.\n\nCounts checked 2026-11-04 from the repo root:\n`python3 -B tools/check-corpus-index.py --root .`\n(total 261 files; directory totals 34/36/43/29/24/95).\n'
    put('corpus/README.md',rd)
    return src,lesson
def land(name,doF,doC,cite_pop=False):
    g('checkout','-q','-f','--detach',START); g('clean','-qfdx')
    src=open(D+'/corpus/SOURCES.md').read(); lesson='# round 89 fixture lesson\n\n'
    if doF: src,lesson=f_overlay(src,lesson)
    if doC: src,lesson=c_overlay(src,lesson,cite_pop)
    put('corpus/SOURCES.md',src); put('corpus/lessons/round-89.md',lesson)
    g('add','-A'); g('commit','-qm',name)
    return g('rev-parse','HEAD')
res={}
for name,f,c,cp in [('F-lazy-titlequote',1,0,0),('C-filler-copy-sec4',0,1,0),('FC-cite-pop',1,1,1)]:
    L=land(name,f,c,cp); work=os.path.join(W,'work-'+name); os.makedirs(work,exist_ok=True)
    for claim in (['F'] if f and not c else ['C'] if c and not f else ['F','C']):
        p=subprocess.run([sys.executable,'-B',LANE+'/reports/round-89/measure89.py','--root',D,'--freeze',FREEZE,'--lands',L,'--claim',claim,'--work',work],capture_output=True,text=True)
        open(W+'/receipt-%s-%s.txt'%(name,claim),'w').write('$ measure89.py --root <clone> --freeze %s --lands %s --claim %s\nrc=%d\n%s%s'%(FREEZE,L,claim,p.returncode,p.stdout,p.stderr))
        print(name,claim,'rc=%d'%p.returncode,[l for l in p.stdout.splitlines() if 'FAIL' in l or 'ACCEPT' in l])
