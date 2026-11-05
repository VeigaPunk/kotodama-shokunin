import re,unicodedata,collections,os
K='/home/vgpnk/Projects/shokunin/kotodama-shokunin'
ST=f'{K}/.ufo/waves/round-95/w1/stage'
text=open(f'{ST}/ScribeEntry95/funerary-lament-dirge-formulae.md',encoding='utf-8').read()
lines=text.split('\n')
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in [('\u2019',"'"),('\u2018',"'"),('\u201c','"'),('\u201d','"')]: s=s.replace(a,b)
    return re.sub(r'\s+',' ',s).lower()
# 1 unsourced body sentences
print('== 1 unsourced sentences (no S-id, no design marker, not heading/table/NON-CANON)')
sec=None; n=0
for i,l in enumerate(lines,1):
    if l.startswith('## '): sec=l[:60]
    if not l.strip() or l.startswith('#') or l.startswith('|') or l.startswith('- sources') or l.startswith('  - S9') or l.startswith('- '): 
        if not l.startswith('- ') or True: pass
    if not l.strip() or l.startswith('#') or l.startswith('|'): continue
    sents=re.split(r'(?<=[.!?])\s+(?=[A-Z*"(\u201c])',l)
    for s in sents:
        if re.search(r'S97[0-4]',s) or 'design, not sourced' in s or 'NON-CANON' in s or re.match(r'^\s*(\d+\.|-)\s',s) and 'design' in s: continue
        if len(s)<40: continue
        if re.search(r'\d{3,4}|Irish|Corsic|Svan|Seto|Greek|Roman|Chinese|Victorian|Japanese|Malagasy|Hindu|Catholic|Hertz|Herodot|Ó |Ireland|Georgia|Svaneti',s):
            n+=1; print(f'  L{i} [{sec}]: {s[:230]}')
print('  count',n)
# 2 table padding
print('== 2 table cells')
rows=[l for l in lines if l.startswith('|')]
tbl=[ [c.strip() for c in r.strip('|').split('|')] for r in rows if not re.match(r'^\|[-| ]+\|$',r)]
hdr=tbl[0]; body=tbl[1:]
print('  cols',len(hdr),'data rows',len(body))
for r in body:
    empties=sum(1 for c in r if not c)
    print('  row',r[0][:40],'cells',len(r),'empty',empties,'minlen',min(len(c) for c in r),'maxlen',max(len(c) for c in r))
dup=collections.Counter(c for r in body for c in r)
print('  repeated cells', [c[:50] for c,v in dup.items() if v>1])
# 3 repeated boilerplate: largest repeated sentence and repeated 12-word shingle counts
print('== 3 repetition')
sents=[s.strip() for s in re.split(r'(?<=[.!?])\s+',text) if len(s.strip())>30]
c=collections.Counter(norm(s) for s in sents)
top=c.most_common(5)
for s,v in top: print('  x',v, s[:120])
print('  total bytes',len(text.encode()),'design,not-sourced count',text.count('design, not sourced'),'bytes in marker',len('design, not sourced')*text.count('design, not sourced'))
rep=[(s,v) for s,v in c.items() if v>1 and len(s)>80]
print('  sentences of len>80 repeated:',len(rep))
# 4 n-gram overlap vs neighbour entries
print('== 4 overlap (8-gram shingle share of each new paragraph found in neighbour)')
neigh=['linguistics/orality-formulaic-language.md','linguistics/lullaby-child-song-formulae.md','culture-material/funerary-material-culture.md','myth-symbol/death-afterlife-eschatology.md','linguistics/sacred-registers-liturgical-language.md']
def shingles(s,k=8):
    w=re.findall(r'[a-z0-9]+',norm(s))
    return set(tuple(w[i:i+k]) for i in range(max(0,len(w)-k+1)))
NS={}
for nb in neigh:
    NS[nb]=shingles(open(f'{K}/corpus/knowledge/{nb}',encoding='utf-8').read(),8)
paras=[(i,l) for i,l in enumerate(lines,1) if len(l)>200 and not l.startswith('|')]
flag=[]
for i,p in paras:
    sh=shingles(p,8)
    if not sh: continue
    for nb,ns in NS.items():
        f=len(sh&ns)/len(sh)
        if f>=0.10: flag.append((round(f,2),i,nb,p[:110]))
for f in sorted(flag,reverse=True)[:20]: print('  ',f)
print('  flagged paragraphs',len(flag))
