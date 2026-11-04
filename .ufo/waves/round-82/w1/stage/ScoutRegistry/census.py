import re, collections, sys, json
P='/fast/scratch/hyaku/kotodama-r82/ScoutRegistry/SOURCES.base.md'
rows=[]
with open(P, encoding='utf-8') as f:
    for ln, line in enumerate(f, 1):
        s=line.rstrip('\n')
        if re.match(r'^ {0,3}\|\s*S\d{3,}\s*\|', s):
            cells=[c.strip() for c in s.strip().strip('|').split('|')]
            rows.append((ln, cells, s))
print("rows:", len(rows))
print("first line:", rows[0][0], "last line:", rows[-1][0])
# cell count distribution
dist=collections.Counter(len(c) for _,c,_ in rows)
print("cell-count distribution:", dict(sorted(dist.items())))
bad=[(ln,len(c)) for ln,c,_ in rows if len(c)!=11]
print("rows with cell count != 11:", bad[:20], "count", len(bad))
# for 11-cell rows, check the id/opened/recheck columns
ids=collections.Counter(c[0] for _,c,_ in rows)
dups={k:v for k,v in ids.items() if v>1}
print("duplicate ids:", dups)
openvals=collections.Counter(c[8] for _,c,_ in rows if len(c)==11)
print("opened histogram:", dict(sorted(openvals.items())))
rc=collections.Counter(c[9] for _,c,_ in rows if len(c)==11)
print("recheck histogram:", dict(sorted(rc.items())))
ISO=re.compile(r'^\d{4}-\d{2}-\d{2}$')
NNd=re.compile(r'^(\d+)d$')
bad_open=[(ln,c[0],c[8]) for ln,c,_ in rows if len(c)==11 and not ISO.match(c[8])]
print("opened not ISO:", bad_open)
bad_rc=[(ln,c[0],c[9]) for ln,c,_ in rows if len(c)==11 and not (NNd.match(c[9]) or ISO.match(c[9]) or c[9]=='on-release')]
print("recheck not NNd/ISO/on-release:", bad_rc)
# status histogram
print("status histogram:", dict(sorted(collections.Counter(c[7] for _,c,_ in rows if len(c)==11).items())))
# ids numeric range
nums=sorted(int(c[0][1:]) for _,c,_ in rows if len(c)==11)
print("id min/max:", nums[0], nums[-1], "distinct:", len(set(nums)), "expected span:", nums[-1]-nums[0]+1)
missing=[n for n in range(nums[0], nums[-1]+1) if n not in set(nums)]
print("missing ids in span:", missing[:20], len(missing))
