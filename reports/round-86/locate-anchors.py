#!/usr/bin/env python3
"""Read-only quotation probe; prints counts, not an admission or truth verdict."""
import argparse
import html
import json
import re
import subprocess

p=argparse.ArgumentParser()
p.add_argument('--root',required=True)
p.add_argument('--lands',required=True)
a=p.parse_args()
def read(path):
    return subprocess.check_output(['git','-C',a.root,'show',a.lands+':'+path]).decode('utf-8')
s=read('corpus/knowledge/linguistics/proverbs-riddles-attestation-solutions.md')
section=s.split('## 3. Attested anchors',1)[1].split('\n## ',1)[0]
rows=[]
for line in section.splitlines():
    m=re.match(r'- (S\d+) .*Quote: “([^”]+)”',line)
    if m:
        sid,q=m.groups()
        raw=read('reports/round-86/evidence/'+sid+('.html' if sid=='S924' else '.txt'))
        body=html.unescape(re.sub('<[^>]+>',' ',raw)) if sid=='S924' else raw
        rows.append({'id':sid,'quote':q,'words':len(q.split()),'folded_count':' '.join(body.split()).count(q)})
print(json.dumps({'measured_revision':a.lands,'anchors':rows},indent=2))
print('ANCHOR-PROBE: located=%d/%d over25=%d' % (sum(r['folded_count']>0 for r in rows),len(rows),sum(r['words']>25 for r in rows)))
