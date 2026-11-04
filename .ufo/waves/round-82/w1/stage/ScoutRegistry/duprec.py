import re, collections
rows=[]
for ln,line in enumerate(open('SOURCES.base.md',encoding='utf-8'),1):
    s=line.rstrip('\n')
    if re.match(r'^ {0,3}\|\s*S\d{3,}\s*\|', s):
        rows.append([c.strip() for c in s.strip().strip('|').split('|')])
ids=collections.Counter(c[0] for c in rows)
print("rows:", len(rows))
print("distinct ids:", len(set(ids)), "duplicate ids:", {k:v for k,v in ids.items() if v>1})
def norm(u):
    u=re.sub(r'^https?://','',u); u=re.sub(r'^www\.','',u); return u.rstrip('/')
g=collections.defaultdict(list)
for c in rows:
    m=re.search(r'(https?://[^\s|]+)', c[1])
    if m: g[norm(m.group(1))].append((c[0], c[4]))
d={u:v for u,v in g.items() if len(v)>1}
same=[u for u,v in d.items() if len(set(s for _,s in v))==1]
diff=[u for u,v in d.items() if len(set(s for _,s in v))>1]
print("normalized duplicate-URL groups:", len(d))
print("  same-scope (supersede/correction pairs, NOT W04):", len(same))
for u in same: print("   same-scope:", u, [i for i,_ in d[u]])
print("  cross-scope (== W04 lines):", len(diff))
