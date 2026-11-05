import re,sys,unicodedata
EV='/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-95/w1/stage/ExecRegistry95/evidence'
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in [('\u2019',"'"),('\u2018',"'"),('\u201c','"'),('\u201d','"'),('\u2013','-'),('\u2014','-')]: s=s.replace(a,b)
    return re.sub(r'\s+',' ',s)
checks=[
 ('S974',['refrain exclamation','vocative','name of','sobbing','village doctor','elderly','Sima']),
 ('S973',['name of the deceased','non-lexical','scarce','Catholicism']),
 ('S972',['intrinsic','over the corpse','sacred improvised']),
 ('S970',['two reasons','lead singer','improvis','maiden','polyphonic']),
 ('S971',['truth','conflict','male-dominated','Greek','record-keeping']),
]
for sid,terms in checks:
    t=norm(open(f'{EV}/{sid}.txt',encoding='utf-8',errors='replace').read())
    for term in terms:
        ms=[m.start() for m in re.finditer(re.escape(term),t,flags=re.I)]
        print(f'== {sid} [{term}] n={len(ms)}')
        for s in ms[:2]:
            print('   ...'+t[max(0,s-160):s+200].replace('\n',' ')+'...')
