import re, collections, datetime
P='SOURCES.base.md'
rows=[]
for ln, line in enumerate(open(P, encoding='utf-8'), 1):
    s=line.rstrip('\n')
    if re.match(r'^ {0,3}\|\s*S\d{3,}\s*\|', s):
        cells=[c.strip() for c in s.strip().strip('|').split('|')]
        rows.append((ln,cells))
def due(cells):
    opened=datetime.date.fromisoformat(cells[8]); rc=cells[9]
    m=re.match(r'^(\d+)d$', rc)
    if m: return opened+datetime.timedelta(days=int(m.group(1))), 'opened+%sd'%m.group(1)
    if rc=='on-release': return None, 'on-release'
    return datetime.date.fromisoformat(rc), 'iso'
recs=[]
for ln,c in rows:
    d,kind=due(c); recs.append((c[0],c[8],c[9],d,kind))
opened=[r[1] for r in recs]
print("earliest opened:", min(opened), "latest opened:", max(opened))
def score(asof, window):
    A=datetime.date.fromisoformat(asof)
    due_n=up_n=onrel=0
    for sid,op,rc,d,kind in recs:
        if d is None: onrel+=1
        elif d<=A: due_n+=1
        elif d<=A+datetime.timedelta(days=window): up_n+=1
    return due_n,up_n,onrel,len(recs)
for asof,w in [("2026-11-04",90),("2027-11-01",90)]:
    print(f"as-of {asof} window {w}: due={score(asof,w)[0]} upcoming={score(asof,w)[1]} on-release={score(asof,w)[2]} rows={score(asof,w)[3]}")
# rows due exactly on dates
for target in ["2026-11-04","2027-11-01"]:
    T=datetime.date.fromisoformat(target)
    hits=[r[0] for r in recs if r[3]==T]
    print(f"rows with due_date == {target}: {len(hits)} {hits[:10]}")
# distribution of due dates among non-exempt
byday=collections.Counter(r[3].isoformat() for r in recs if r[3] is not None)
print("distinct due dates:", len(byday))
for k in sorted(byday)[:6]: print("  ", k, byday[k])
print("  ...")
for k in sorted(byday)[-6:]: print("  ", k, byday[k])
