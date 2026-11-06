import re,os,collections,subprocess,hashlib,json
ROOT='/home/vgpnk/Projects/shokunin/kotodama-shokunin'
ENTRY=os.path.join(ROOT,'corpus/knowledge/linguistics/toast-drinking-speech-formulae.md')
FROZEN=('toasts and drinking-speech formulae: the toast as a speech act over a shared cup — '
 'health-drinking, libation and the pledge; the toastmaster\'s office and the order of a '
 'toast sequence; the drinking oath and the boast-cup; refusal, reciprocity and the '
 'penalty cup; and the design procedure for a fictional drinking rite whose words stay '
 'tied to its hosts, guests, cups and occasions')
PHR=['toast formula','health-drinking','toastmaster','libation','toast sequence','drinking oath']
NB=['linguistics/verbal-duelling-ritual-insult.md','linguistics/oath-blessing-curse-formulae.md','myth-symbol/guest-right-hospitality-law.md']
def norm(s): return re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()
def ws(s): return re.sub(r'\s+',' ',s).strip()
raw=open(ENTRY,encoding='utf-8').read()
size=len(raw.encode('utf-8'))
heads=[l for l in raw.splitlines() if l.startswith('## ')]
rows,cols,sep,best=0,0,False,(0,0); trows=[]
for l in raw.splitlines():
    s=l.strip()
    if not s.startswith('|'): sep=False; rows=0; continue
    if re.match(r'^\|[\s:\-|]+\|$',s): sep=True; rows=0; continue
    c=len(s.strip('|').split('|'))
    if sep: rows+=1; cols=c; best=max(best,(rows,cols)); trows.append(norm(l))
anchor=' '.join(norm(h) for h in heads)
hits=[p for p in PHR if norm(p) in anchor or any(norm(p) in t for t in trows)]
tl=next((l for l in raw.splitlines() if l.strip().startswith('- topic:')),'')
print('SELF-CHECK ScribeEntry98 — round 98 claim C entry (self-check of the landed bytes)')
print('entry: corpus/knowledge/linguistics/toast-drinking-speech-formulae.md')
print('entry sha256:', hashlib.sha256(open(ENTRY,'rb').read()).hexdigest())
print('readme sha256:', hashlib.sha256(open(os.path.join(ROOT,'corpus/README.md'),'rb').read()).hexdigest())
print('registry sha256:', hashlib.sha256(open(os.path.join(ROOT,'corpus/SOURCES.md'),'rb').read()).hexdigest())
print('manifest sha256:', hashlib.sha256(open(os.path.join(ROOT,'reports/round-98/evidence/manifest.json'),'rb').read()).hexdigest())
print()
print('[C1 entry shape]')
print(f'bytes={size} (floor 12000) -> {"PASS" if size>=12000 else "FAIL"}')
print(f'h2={len(heads)} (floor 6) -> {"PASS" if len(heads)>=6 else "FAIL"}')
print(f'table={best[0]} data rows x {best[1]} cols (floor 5x3) -> {"PASS" if best[0]>=5 and best[1]>=3 else "FAIL"}')
print(f'frozen phrases in h2 headings or table data rows={len(hits)}/6 (floor 4) -> {"PASS" if len(hits)>=4 else "FAIL"}')
print(f'  hits={hits}')
print(f'topic line byte-equal to frozen topic -> {"PASS" if tl=="- topic: "+FROZEN else "FAIL"}')
print('  h2 headings:')
for h in heads: print('   ', h)
print()
print('[C6 cited ids / C7 evidence binding]')
reg=os.path.join(ROOT,'corpus/SOURCES.md')
rows_by_id={}
for line in open(reg,encoding='utf-8'):
    if re.match(r'^ {0,3}\|\s*S[0-9]{3,}\s*\|',line):
        c=[x.strip() for x in line.strip().strip('|').split('|')]
        if len(c)==11: rows_by_id[c[0]]=c
ids=sorted(rows_by_id,key=lambda x:int(x[1:]))
new=[i for i in ids if int(i[1:])>993]
qual=[i for i in new if rows_by_id[i][3] in ('A','B') and rows_by_id[i][7]=='mined'
      and rows_by_id[i][8] in ('2026-11-05','2026-11-06')
      and rows_by_id[i][10]=='corpus/knowledge/linguistics/toast-drinking-speech-formulae.md']
print(f'registry rows={len(ids)} highest={ids[-1]} new(>S993)={len(new)} qualifying(used-by=this entry)={len(qual)}')
print('qualifying ids:', qual)
cited=sorted(set(re.findall(r'\bS\d{3,}\b',raw)),key=lambda x:int(x[1:]))
print('ids cited in entry text:', cited)
print('qualifying uncited:', [i for i in qual if not re.search(r'\b'+i+r'\b',raw)])
print('entry cites ids absent from the registry:', [i for i in cited if i not in rows_by_id])
man=os.path.join(ROOT,'reports/round-98/evidence/manifest.json')
m=json.load(open(man,encoding='utf-8'))
byid={e['id']:e for e in m if isinstance(e,dict) and 'id' in e}
print(f'manifest objects={len(m)}')
allok=True
for i in qual:
    e=byid.get(i)
    if not e: print(f'  {i}: NO MANIFEST ENTRY'); allok=False; continue
    q=e.get('quote'); qc=e.get('quote_capture'); caps=e.get('captures') or []
    d=os.path.dirname(man)
    capok=all(os.path.isfile(os.path.join(d,c['file'])) and
               hashlib.sha256(open(os.path.join(d,c['file']),'rb').read()).hexdigest()==c['sha256'] for c in caps)
    qtxt=ws(open(os.path.join(d,qc),encoding='utf-8',errors='replace').read())
    cnt=qtxt.count(ws(q)); inanchor=ws(q) in ws(rows_by_id[i][5])
    ok=(1<=len(q.split())<=25) and cnt==1 and inanchor and capok
    allok=allok and ok
    print(f'  {i}: words={len(q.split())} count_in_capture={cnt} quote_in_anchor_cell={inanchor} captures_sha_ok={capok} quote_capture={qc} -> {"PASS" if ok else "FAIL"}')
print(f'C7-shaped binding over the {len(qual)} qualifying ids -> {"PASS" if allok else "FAIL"}')
print()
print('[body quotes: every double-quoted fragment in the entry body, counted in its capture]')
capt={f'S{n}':ws(open(f'{ROOT}/reports/round-98/evidence/S{n}.txt',encoding='utf-8',errors='replace').read()) for n in range(994,1005)}
nq=0; unmatched=[]
for i,l in enumerate(raw.splitlines(),1):
    if l.startswith('- S99') or l.startswith('- S100'): continue
    for m2 in re.finditer(r'"([^"]{6,})"', l):
        nq+=1; q=m2.group(1)
        c={k:capt[k].count(ws(q)) for k in capt if ws(q) in capt[k]}
        if not any(v==1 for v in c.values()): unmatched.append((i,q,c))
print(f'body quoted fragments={nq} unmatched in any capture={len(unmatched)} {unmatched}')
print()
print('[C8 content sweep: other knowledge files owning a frozen phrase on a topic line or heading]')
owners=[]; nf=0
for d,_,fs in os.walk(os.path.join(ROOT,'corpus/knowledge')):
    for f in fs:
        if not f.endswith('.md'): continue
        nf+=1
        rel=os.path.relpath(os.path.join(d,f),ROOT)
        if rel=='corpus/knowledge/linguistics/toast-drinking-speech-formulae.md': continue
        txt=open(os.path.join(d,f),encoding='utf-8',errors='replace').read()
        surf=[norm(l.strip()) for l in txt.splitlines() if l.strip().startswith('- topic:') or re.match(r'^#{1,6}\s',l.strip())]
        if any(norm(p) in t for p in PHR for t in surf): owners.append(rel)
print(f'files scanned={nf} other owners={len(owners)} {owners[:5]} -> {"PASS" if not owners else "FAIL"}')
print()
print('[8-gram overlap with neighbour entries]')
def words(t): return norm(t).split()
def ngs(ws_,n=8): return set(tuple(ws_[i:i+n]) for i in range(len(ws_)-n+1))
mine=ngs(words(raw))
print(f'entry 8-grams total={len(mine)} (round-97 entry: 6181)')
for nb in NB:
    t=ngs(words(open(os.path.join(ROOT,'corpus/knowledge',nb),encoding='utf-8').read()))
    print(f'  {nb}: shared 8-grams={len(mine&t)}')
print()
print('[cited-line lint shapes (QUALITY criterion 15)]')
SID=re.compile(r"\bS\d{3,}\b")
multi=[]; tab=[]
for i,l in enumerate(raw.splitlines(),1):
    s=sorted(set(SID.findall(l)),key=lambda x:int(x[1:]))
    if len(s)>=2: multi.append((i,s))
    if s and l.lstrip().startswith('|'): tab.append((i,s))
print(f'MULTI-ID lines={len(multi)} TABLE-ID lines={len(tab)}')
print()
print('[commands run from the repo root /home/vgpnk/Projects/shokunin/kotodama-shokunin]')
for cmd in (['python3','-B','tools/check-corpus-index.py','--root','.'],
            ['bash','/home/vgpnk/Projects/shokunin/scripts/sources-census.sh','validate','--file','corpus/SOURCES.md'],
            ['python3','-B','tools/check-cited-lines.py','corpus/knowledge/linguistics/toast-drinking-speech-formulae.md']):
    r=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
    print('$ '+' '.join(cmd))
    print('  rc=',r.returncode,'| stdout:',(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ''),'| stderr:',r.stderr.strip()[:120])
