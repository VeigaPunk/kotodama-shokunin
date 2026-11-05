import re,unicodedata
EV='/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-95/w1/stage/ExecRegistry95/evidence'
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in [('\u2019',"'"),('\u2018',"'"),('\u201c','"'),('\u201d','"'),('\u2013','-'),('\u2014','-')]: s=s.replace(a,b)
    return re.sub(r'\s+',' ',s)
def show(sid,pat,w=260,n=3):
    t=norm(open(f'{EV}/{sid}.txt',encoding='utf-8',errors='replace').read())
    ms=[m.start() for m in re.finditer(pat,t,flags=re.I)]
    print(f'== {sid} /{pat}/ n={len(ms)}')
    for s in ms[:n]: print('   ...'+t[max(0,s-w):s+w]+'...')
show('S973','priest',220,6)
show('S973','represent',200,3)
show('S971','jural',300,2)
show('S971','truth-claim|truth claim|claims? to truth',200,2)
show('S970','requirement',160,2)
