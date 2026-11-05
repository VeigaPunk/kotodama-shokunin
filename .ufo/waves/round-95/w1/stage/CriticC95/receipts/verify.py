import re, unicodedata, collections, os
ST='/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-95/w1/stage'
ENTRY=f'{ST}/ScribeEntry95/funerary-lament-dirge-formulae.md'
EV=f'{ST}/ExecRegistry95/evidence'
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in [('\u2019',"'"),('\u2018',"'"),('\u201c','"'),('\u201d','"'),('\u2013','-'),('\u2014','-'),('\u00ad',''),('\u00a0',' ')]:
        s=s.replace(a,b)
    s=re.sub(r'-\s*\n\s*','',s)  # dehyphenate
    s=re.sub(r'\s+',' ',s)
    return s.lower()
caps={}
for sid in ['S970','S971','S972','S973','S974']:
    caps[sid]=norm(open(f'{EV}/{sid}.txt',encoding='utf-8',errors='replace').read())
text=open(ENTRY,encoding='utf-8').read()
lines=text.split('\n')
print('ENTRY bytes',len(text.encode()),'lines',len(lines))
# A. quotes
quotes=[]
for i,l in enumerate(lines,1):
    for m in re.finditer(r'[\u201c"]([^\u201c\u201d"]{12,})[\u201d"]',l):
        quotes.append((i,m.group(1)))
print('QUOTES total',len(quotes))
miss=[]
for ln,q in quotes:
    # cited id: any S9xx in the same line
    ids=set(re.findall(r'S97[0-4]',lines[ln-1]))
    qn=norm(q).strip(' .,;:')
    hits=[sid for sid,c in caps.items() if qn in c]
    cnt={sid:caps[sid].count(qn) for sid in hits}
    if ids:
        bad=[sid for sid in ids if sid not in hits]
        if bad or not hits:
            miss.append((ln,sorted(ids),q[:140],hits,cnt))
    else:
        miss.append((ln,'NO-ID',q[:140],hits,cnt))
for m in miss: print('QMISS line',m[0],'ids',m[1],'hits',m[3],'count',m[4],'|',m[2])
print('QMISS total',len(miss))

print('---- per-quote detail')
for ln,q in quotes:
    ids=sorted(set(re.findall(r'S97[0-4]',lines[ln-1])))
    qn=norm(q).strip(' .,;:')
    print(ln, ids, 'words=',len(q.split()), {sid:caps[sid].count(qn) for sid in caps if qn in caps[sid]}, '|', q[:90])
print('---- uncited paraphrase probes')
probes={
 'eighteenth-century':['eighteenth','18th'],
 'vocative name S974':['vocative','name of the'],
 'Sima':['sima'],
 'dead village doctor':['doctor'],
 'Greek male-dominated':['male-dominated','male dominated','greek'],
 'Catholic scarce priests':['scarce','priest shortage','shortage of priest','priests'],
 'bean chaointe':['bean chaointe','chaointe'],
 'pipes or harp':['pipe','harp'],
 'jural historicizing':['jural','historicizing'],
 'polyphonic lamenting song':['polyphonic'],
 'maiden':['maiden'],
 'beseeching afterlife':['afterlife','beseech'],
 'vocables such as':['vocables such as'],
 'purely musical terms':['purely musical'],
 'wake sequence visitors':['visitor'],
 'strikes/ hired mourner paid':['paid','payment','fee'],
}
for k,ws in probes.items():
    res={sid:[w for w in ws if w in caps[sid]] for sid in caps}
    print(k, {s:v for s,v in res.items() if v})
