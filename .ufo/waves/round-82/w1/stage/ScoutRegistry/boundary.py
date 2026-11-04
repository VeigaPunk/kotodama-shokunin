import re, datetime
rows=[]
for line in open('SOURCES.base.md',encoding='utf-8'):
    s=line.rstrip('\n')
    if re.match(r'^ {0,3}\|\s*S\d{3,}\s*\|', s):
        rows.append([c.strip() for c in s.strip().strip('|').split('|')])
def due(c):
    o=datetime.date.fromisoformat(c[8]); r=c[9]
    m=re.match(r'^(\d+)d$', r)
    if m: return o+datetime.timedelta(days=int(m.group(1)))
    if r=='on-release': return None
    return datetime.date.fromisoformat(r)
NNd=sum(1 for c in rows if re.match(r'^\d+d$', c[9]))
ISO=sum(1 for c in rows if re.match(r'^\d{4}-\d{2}-\d{2}$', c[9]))
print("NNd rows=%d  ISO-recheck rows=%d  on-release rows=%d  total=%d" % (NNd, ISO, sum(1 for c in rows if c[9]=='on-release'), len(rows)))
print("fleet cadence-line total = NNd + on-release =", NNd + sum(1 for c in rows if c[9]=='on-release'))
print("fleet overdue total at 2027-11-01 = NNd + ISO =", NNd + ISO)
print()
print("as-of / window=90 / due / upcoming / on-release / rows")
for asof in ["2026-10-19","2026-11-04","2027-01-16","2027-01-17","2027-02-02","2027-02-03","2027-10-22","2027-10-24","2027-11-01"]:
    A=datetime.date.fromisoformat(asof); E=A+datetime.timedelta(days=90)
    d=sum(1 for c in rows if due(c) and due(c)<=A)
    u=sum(1 for c in rows if due(c) and A<due(c)<=E)
    o=sum(1 for c in rows if due(c) is None)
    print(f"{asof}  {d}  {u}  {o}  {len(rows)}")
print()
A=datetime.date(2027,1,17); E=A+datetime.timedelta(days=90)
print("strict '<' implementation at as-of 2027-01-17:", 
      "due=%d upcoming=%d" % (sum(1 for c in rows if due(c) and due(c)<A), sum(1 for c in rows if due(c) and A<due(c)<=E)))
print("rows due exactly on 2026-11-04:", sum(1 for c in rows if due(c)==datetime.date(2026,11,4)))
print("rows due exactly on 2027-11-01:", sum(1 for c in rows if due(c)==datetime.date(2027,11,1)))
print("distance of latest in-window due date from the 2026-11-04+90d edge:", (datetime.date(2027,2,2)-datetime.date(2027,1,23)).days, "days")
