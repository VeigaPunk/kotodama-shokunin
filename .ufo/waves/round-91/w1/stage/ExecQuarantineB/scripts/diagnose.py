#!/usr/bin/env python3
"""Sharpen notes in verdicts-B.json/md from the already-captured bytes (no re-fetch)."""
import os, re, json, html, subprocess, unicodedata, shutil

STAGE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB'
CAPS = os.path.join(STAGE, 'caps')
SCRATCH = '/fast/scratch/hyaku/kotodama-r91/ExecQuarantineB'
os.environ['TMPDIR'] = SCRATCH


def fold(s):
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = s.replace('\u00a0', ' ').replace('\u2003', ' ')
    s = unicodedata.normalize('NFKC', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s.casefold()


def body(rid):
    with open(os.path.join(CAPS, f'{rid}.bin'), 'rb') as f:
        return f.read()


def pdf_text(rid):
    out = os.path.join(SCRATCH, f'{rid}.txt')
    env = dict(os.environ)
    r = subprocess.run(['pdftotext', '-q', os.path.join(CAPS, f'{rid}.bin'), out],
                       capture_output=True, text=True, env=env)
    if r.returncode != 0:
        return None
    with open(out, encoding='utf-8', errors='replace') as f:
        return f.read()


def hits(text, needles):
    out = {}
    for n in needles:
        nf = fold(n)
        i = fold(text).find(nf)
        out[n] = i
    return out


def ctx(text, needle, width=80):
    ft = fold(text)
    i = ft.find(fold(needle))
    if i < 0:
        return None
    return ft[max(0, i - width): i + width]


def head(s, n=300):
    return re.sub(r'\s+', ' ', s)[:n]


patch = {}

# S807: prose row, PDF served — give extracted-text head (title evidence)
t = pdf_text('S807')
if t:
    patch['S807'] = ('served application/pdf (598 KB) via DOI -> onomajournal.org '
                     '(Onoma 51, Kaluzynska); extracted-text head: ' + repr(head(fold(t), 220)))

# S812 / S835: prose rows whose fetch still fails — state prose + what the wall served
patch['S812'] = ('prose row ("could not be fetched"); re-fetch attempt: http=429 (Cambridge rate-limit page), '
                 '1478 B text/html; DOI -I -L final: https://www.cambridge.org/core/product/identifier/'
                 'S0008413124000215/type/journal_article 429; page head: '
                 + repr(head(body('S812').decode('utf-8', 'replace'), 200)))
patch['S835'] = ('prose row ("could not be fetched"); re-fetch attempt: http=503, 690 B text/html; page head: '
                 + repr(head(body('S835').decode('utf-8', 'replace'), 250)))

# S814: 403 — name the wall body
patch['S814'] = ('http=403, 162 B text/html; body: '
                 + repr(head(body('S814').decode('utf-8', 'replace'), 160)))

# S823: 468 — name the wall body
patch['S823'] = ('http=468 (nonstandard block code, WAF/gateway), 14863 B text/html; body head: '
                 + repr(head(body('S823').decode('utf-8', 'replace'), 250)))

# S816: which parts of the quote exist in the page?
b = body('S816').decode('utf-8', 'replace')
h16 = hits(b, ['肯定考虑过', '资深读者', '这个我肯定考虑过', '我就是资深读者'])
c16 = ctx(b, '肯定考虑过') or ctx(b, '资深读者')
patch['S816'] = ('2xx body 48536 B text/html (UTF-8, article title 爱潜水的乌贼:"我先设定世界观,再考虑怎么升级"); '
                 f'needle hits in raw: {json.dumps(h16, ensure_ascii=False)}; '
                 f'nearest context: {c16!r}')

# S817
b = body('S817').decode('utf-8', 'replace')
h17 = hits(b, ['Phonology', 'Sowers', 'inside out', 'Sowers-Wills'])
patch['S817'] = ('2xx body 62604 B text/html (UTF-8, article title 爱潜水的乌贼:网络文学不断"升级"的"奥术"); '
                 f'needle hits in raw: {json.dumps(h17, ensure_ascii=False)}')

# S820: PDF — check pieces of the quote in the text layer
t = pdf_text('S820')
h20 = hits(t or '', ['standard given names', 'aesthetic', 'softness', 'classified as',
                     'feminine softness', 'female aesthetic val'])
c20 = ctx(t or '', 'standard given names') or ctx(t or '', 'aesthetic')
patch['S820'] = ('2xx body 417093 B application/pdf (Onoma 51 download); byte-level pipeline: no fragment; '
                 f'text-layer diagnostics: needle hits {json.dumps(h20, ensure_ascii=False)}; '
                 f'nearest context: {c20!r}')

# S824: PDF Japanese
t = pdf_text('S824')
h24 = hits(t or '', ['輩行', '輩行字', '命名', '習俗'])
c24 = ctx(t or '', '輩行') or ctx(t or '', '命名')
patch['S824'] = ('2xx body 504441 B application/pdf (Osaka U repository gbg_018_197); byte-level pipeline: '
                 f'no fragment; text-layer diagnostics: needle hits {json.dumps(h24, ensure_ascii=False)}; '
                 f'nearest context: {c24!r}; extracted-text head: {head(fold(t or ""), 120)!r}')

# S825: is it a JS shell? strip script/style then measure visible text; needle hits
b = body('S825').decode('utf-8', 'replace')
nost = re.sub(r'(?is)<(script|style|noscript)\b.*?</\1>', ' ', b)
vis = fold(re.sub(r'(?s)<[^>]+>', ' ', nost))
h25 = hits(b, ['元号', '令和', '開始西暦年', '1989', 'reki', '元号名称'])
patch['S825'] = ('2xx body 311308 B text/html;charset=UTF-8; needle hits in raw: '
                 f'{json.dumps(h25, ensure_ascii=False)}; visible text after stripping script/style/tags: '
                 f'{len(vis)} chars, head: {vis[:200]!r}')

with open(os.path.join(STAGE, 'verdicts-B.json'), encoding='utf-8') as f:
    results = json.load(f)

for r in results:
    if r['id'] in patch:
        r['note'] = patch[r['id']]
    r.pop('_meta', None)

with open(os.path.join(STAGE, 'verdicts-B.json'), 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=1)

# regenerate the md with sharper reasons
cmds = []
for rid in ['S807', 'S812', 'S814', 'S816', 'S817', 'S820', 'S823', 'S824', 'S825', 'S827', 'S835']:
    cmds.append(f"curl -sS -L --max-time 40 -o {STAGE}/caps/{rid}.bin "
                f"-w '%{{http_code}} %{{size_download}} %{{content_type}}' '<url of {rid}>'")
urls = {r['id']: r['url'] for r in results}
doi = {'S807', 'S812', 'S827'}

lines = ['# verdicts-B — ExecQuarantineB (kotodama round-91 quarantine hand-check)', '',
         'Fetched 2026-11-05 (instants per row in verdicts-B.json, TZ offset -03:00); one '
         '`curl -sS -L --max-time 40 -o <stage>/caps/<id>.bin -w \'%{http_code} %{size_download} %{content_type}\'` '
         'per URL; captures retained in `caps/`. Fragments split on U+2026, three dots and `<br>` (register\'s '
         'snippet separator); folded copy = UTF-8(replace) -> tags to single space -> entities decoded -> '
         'U+00A0/U+2003 to space -> NFKC -> whitespace collapsed -> casefold.', '',
         '| id | class-as-registered | verdict | http | bytes | fragments found/total | reason |',
         '|---|---|---|---|---|---|---|']
for r in results:
    found = sum(1 for t in r['fragments'] if t['in_folded'])
    total = len(r['fragments'])
    rid = r['id']
    if rid in ('S807', 'S812', 'S835'):
        reason = r['note'][:220]
    elif r['verdict'] == 'LOCATED':
        reason = 'all fragments found in the folded copy'
    elif r['verdict'] == 'PARTIAL':
        miss = [t['text'] for t in r['fragments'] if not t['in_folded']]
        reason = 'some fragments found; missing: ' + '; '.join(m[:40] for m in miss)
    elif r['verdict'] == 'ABSENT':
        reason = '2xx body served but no fragment found in folded copy; ' + r['note'][:200]
    else:
        reason = r['note'][:220]
    cls = r.get('class') or '`payload-absent`'
    lines.append(f"| {rid} | {cls} | {r['verdict']} | {r['http_status']} | {r['bytes']} | "
                 f"{found}/{total} | {reason.replace('|', '/')} |")

lines += ['', '## Commands run', '']
for rid in urls:
    lines.append('```')
    lines.append(f"curl -sS -L --max-time 40 -o {STAGE}/caps/{rid}.bin "
                 f"-w '%{{http_code}} %{{size_download}} %{{content_type}}' '{urls[rid]}'")
    lines.append('```')
    if rid in doi:
        lines.append('```')
        lines.append(f"curl -sS -I -L --max-time 40 -o /dev/null -w '%{{url_effective}} %{{http_code}}' '{urls[rid]}'")
        lines.append('```')

lines += ['', '## Notes (full, per row)', '']
for r in results:
    lines.append(f"- **{r['id']}** ({r['verdict']}, http {r['http_status']}, {r['bytes']} B, "
                 f"sha256 {r['sha256'][:16]}…, fetched_at {r['fetched_at']}): {r['note']}")
lines.append('')
with open(os.path.join(STAGE, 'verdicts-B.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

for r in results:
    print(r['id'], r['verdict'], '|', r['note'][:150])
