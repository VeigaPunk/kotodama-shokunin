#!/usr/bin/env python3
"""ExecQuarantineB — kotodama round-91 quarantine hand-check of 11 register rows.

Pipeline per seat spec:
 (a) one curl -sS -L --max-time 40 fetch per URL, captured to stage caps/<id>.bin
 (b) raw UTF-8 (replacement) decode + folded copy (tags->space, entities, NBSP/EMSP, NFKC, ws collapse, casefold)
 (c) fragment split on U+2026, three dots, and <br> (register's snippet separator); fragments >= 6 chars
 (d) verdict: LOCATED / PARTIAL / ABSENT / UNREACHABLE / UNVERIFIABLE
Diagnostics (note only, never the verdict): declared-encoding re-decode for HTML, PDF text layer.
"""
import os, re, json, html, shutil, hashlib, subprocess, unicodedata, datetime
from concurrent.futures import ThreadPoolExecutor

STAGE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB'
CAPS = os.path.join(STAGE, 'caps')
SCRATCH = '/fast/scratch/hyaku/kotodama-r91/ExecQuarantineB'
os.environ['TMPDIR'] = SCRATCH
os.makedirs(CAPS, exist_ok=True)
os.makedirs(SCRATCH, exist_ok=True)

SLICE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-91/quarantine/slice.tsv'
MINE = ['S807', 'S812', 'S814', 'S816', 'S817', 'S820', 'S823', 'S824', 'S825', 'S827', 'S835']
DOI_IDS = {'S807', 'S812', 'S827'}


def now_iso():
    return datetime.datetime.now().astimezone().isoformat(timespec='seconds')


# ---- parse slice ----
rows = {}
with open(SLICE, encoding='utf-8') as f:
    lines = [l.rstrip('\n') for l in f]
header = lines[0].split('\t')
for l in lines[1:]:
    if not l.strip():
        continue
    parts = l.split('\t')
    d = dict(zip(header, parts))
    if d['id'] in MINE:
        rows[d['id']] = d
missing = [i for i in MINE if i not in rows]
assert not missing, f'slice missing ids: {missing}'


def cell_strip(s):
    s = s.strip()
    if s.startswith('`'):
        s = s[1:]
    if s.endswith('`'):
        s = s[:-1]
    return s


def fragments_of(quote_cell):
    q = cell_strip(quote_cell)
    if not q:
        return []
    pieces = re.split(r'<br\s*/?>|…|\.\.\.', q)
    out = []
    for p in pieces:
        p = p.replace('`', '').strip()
        if len(p) >= 6:
            out.append(p)
    return out


def norm_text(s):
    """fragment-side normalization: entities, NBSP/EMSP, NFKC, ws collapse, casefold (no tag strip)."""
    s = html.unescape(s)
    s = s.replace('\u00a0', ' ').replace('\u2003', ' ')
    s = unicodedata.normalize('NFKC', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s.casefold()


def fold_html(s):
    """body-side folded copy per spec (b): tags->single space, entities, NBSP/EMSP, NFKC, ws collapse, casefold."""
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    return norm_text(s)


# ---- (a) fetch ----
def fetch(row):
    rid = cell_strip(row['id'])
    url = cell_strip(row['url'])
    out = os.path.join(CAPS, f'{rid}.bin')
    t0 = now_iso()
    ts = datetime.datetime.now().astimezone()
    cmd = ['curl', '-sS', '-L', '--max-time', '40', '-o', out,
           '-w', '%{http_code} %{size_download} %{content_type}', url]
    r = subprocess.run(cmd, capture_output=True, text=True)
    dur = (datetime.datetime.now().astimezone() - ts).total_seconds()
    w = (r.stdout or '').strip()
    m = re.match(r'^(\d{3}) (\d+) ?(.*)$', w)
    status = int(m.group(1)) if m else 0
    nbytes = int(m.group(2)) if m else 0
    ctype = (m.group(3).strip() if m else '') or '-'
    return {'id': rid, 'url': url, 'cmd': cmd, 'rc': r.returncode,
            'stderr': (r.stderr or '').strip().replace('\n', '; '),
            'status': status, 'bytes': nbytes, 'ctype': ctype,
            'fetched_at': t0, 'duration_s': round(dur, 1), 'path': out}


with ThreadPoolExecutor(max_workers=11) as ex:
    fetched = list(ex.map(fetch, [rows[i] for i in MINE]))


def head_doi(url):
    cmd = ['curl', '-sS', '-I', '-L', '--max-time', '40', '-o', '/dev/null',
           '-w', '%{url_effective} %{http_code}', url]
    r = subprocess.run(cmd, capture_output=True, text=True, env=dict(os.environ))
    return (r.stdout or '').strip(), r.returncode, cmd


doi_heads = {}
with ThreadPoolExecutor(max_workers=3) as ex:
    for row, res in zip([rows[i] for i in MINE if i in DOI_IDS],
                        ex.map(lambda i: head_doi(cell_strip(rows[i]['url'])),
                               [i for i in MINE if i in DOI_IDS])):
        doi_heads[row['id']] = res

# ---- diagnostics helpers ----
def meta_charset(raw):
    m = re.search(r'charset\s*=\s*["\']?([\w-]+)', raw[:4096], re.I)
    return m.group(1).lower() if m else None


def pdf_extract(path):
    if shutil.which('pdftotext'):
        txtout = os.path.join(SCRATCH, f'{os.path.basename(path)}.txt')
        env = dict(os.environ)
        env['TMPDIR'] = SCRATCH
        r = subprocess.run(['pdftotext', '-q', path, txtout], capture_output=True, text=True, env=env)
        if r.returncode == 0 and os.path.exists(txtout):
            with open(txtout, encoding='utf-8', errors='replace') as f:
                return f.read(), 'pdftotext'
        return None, f'pdftotext rc={r.returncode}'
    if shutil.which('uv'):
        txtout = os.path.join(SCRATCH, f'{os.path.basename(path)}.txt')
        code = (
            "import sys\n"
            "from pypdf import PdfReader\n"
            f"rd = PdfReader({path!r})\n"
            "txt = chr(10).join((p.extract_text() or '') for p in rd.pages)\n"
            f"open({txtout!r}, 'w', encoding='utf-8').write(txt)\n"
        )
        env = dict(os.environ)
        env['TMPDIR'] = SCRATCH
        r = subprocess.run(['uv', 'run', '--with', 'pypdf', 'python', '-c', code],
                           capture_output=True, text=True, env=env, timeout=180)
        if r.returncode == 0 and os.path.exists(txtout):
            with open(txtout, encoding='utf-8', errors='replace') as f:
                return f.read(), 'pypdf-via-uv'
        return None, f'pypdf-via-uv rc={r.returncode} err={(r.stderr or "")[-200:]}'
    return None, 'no pdftotext/uv available'


results = []
for fr in fetched:
    rid = fr['id']
    row = rows[rid]
    class_cell = row['class'].strip()
    url = fr['url']
    quote_cell = row['cited_quote_or_prose']
    frags_raw = fragments_of(quote_cell)
    frags = [(t, norm_text(t)) for t in frags_raw]

    with open(fr['path'], 'rb') as f:
        body = f.read()
    sha = hashlib.sha256(body).hexdigest()
    raw = body.decode('utf-8', errors='replace')
    folded = fold_html(raw)
    rawfold = norm_text(raw)

    notes = []
    ftests = []
    for text, nf in frags:
        ftests.append({'text': text, 'in_raw': nf in rawfold, 'in_folded': nf in folded})

    found = sum(1 for t in ftests if t['in_folded'])
    total = len(ftests)
    is_prose = (frags_raw == [])

    verdict = None
    if fr['rc'] != 0 or not (200 <= fr['status'] < 300) or fr['bytes'] == 0:
        verdict = 'UNREACHABLE'
        notes.append(f"curl rc={fr['rc']} http={fr['status']} bytes={fr['bytes']} type={fr['ctype']}"
                     + (f" err: {fr['stderr']}" if fr['stderr'] else ''))
    elif is_prose:
        # state what the URL served
        head = folded[:200]
        verdict = 'UNVERIFIABLE'
        notes.append(f"prose row (no quote in register cell); served http={fr['status']} "
                     f"bytes={fr['bytes']} type={fr['ctype']}; body text head: {head!r}")
    else:
        if total and found == total:
            verdict = 'LOCATED'
        elif found > 0:
            verdict = 'PARTIAL'
        else:
            # JS shell check: essentially no visible text
            if len(folded) < 120:
                verdict = 'UNREACHABLE'
                notes.append(f'JS shell / empty shell: visible text after tag strip = {len(folded)} chars; '
                             f'body head: {folded[:120]!r}')
            else:
                verdict = 'ABSENT'
                notes.append(f'2xx body ({fr["bytes"]} B, type={fr["ctype"]}); no fragment in folded copy; '
                             f'folded head: {folded[:160]!r}')
                # encoding diagnostic
                cs = meta_charset(raw)
                tried = ([cs] if cs else []) + ['gb18030', 'big5', 'shift_jis', 'euc-jp', 'euc-kr']
                seen = set()
                for enc in tried:
                    if not enc or enc in seen:
                        continue
                    seen.add(enc)
                    try:
                        alt = body.decode(enc, errors='replace')
                    except LookupError:
                        continue
                    altfold = fold_html(alt)
                    hit = sum(1 for _, nf in frags if nf in altfold)
                    if hit:
                        notes.append(f're-decode as {enc}: {hit}/{total} fragments found '
                                     '(diagnostic only; quote present in source under this encoding)')
                        break
                if body[:5] == b'%PDF-':
                    txt, how = pdf_extract(fr['path'])
                    if txt is not None:
                        tf = fold_html(txt)
                        hit = sum(1 for _, nf in frags if nf in tf)
                        notes.append(f'PDF text-layer diagnostic ({how}): {hit}/{total} fragments found '
                                     'in extracted text (diagnostic only; prescribed pipeline is byte-level)')
                    else:
                        notes.append(f'PDF text-layer diagnostic unavailable: {how}')
                elif fr['ctype'].lower().startswith('application/pdf') or 'pdf' in fr['ctype'].lower():
                    notes.append('content-type says PDF but body lacks %PDF magic')

    if rid in DOI_IDS:
        fin, rc, cmd = doi_heads[rid]
        notes.append(f'DOI -I -L final: {fin} (rc={rc})')

    note = ' | '.join(notes) if notes else '-'
    results.append({'id': rid, 'url': url, 'http_status': fr['status'], 'bytes': fr['bytes'],
                    'sha256': sha, 'fetched_at': fr['fetched_at'], 'fragments': ftests,
                    'verdict': verdict, 'note': note, '_meta': {'duration_s': fr['duration_s'],
                    'curl_rc': fr['rc'], 'content_type': fr['ctype'], 'class': class_cell}})

results.sort(key=lambda r: MINE.index(r['id']))
with open(os.path.join(STAGE, 'verdicts-B.json'), 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=1)

# ---- markdown ----
lines = ['# verdicts-B — ExecQuarantineB (kotodama round-91 quarantine hand-check)', '',
         f'Fetched {now_iso()}; one `curl -sS -L --max-time 40` per URL; captures in `caps/<id>.bin`.', '',
         '| id | class-as-registered | verdict | http | bytes | fragments found/total | reason |',
         '|---|---|---|---|---|---|---|']
reasons = {
    'S807': 'Prose row ("could not be fetched"); fetched and reported what the DOI serves.',
    'S812': 'Prose row ("could not be fetched"); fetched and reported what the DOI serves.',
    'S835': 'Prose row ("could not be fetched"); fetched and reported what the record URL serves.',
}
for r in results:
    found = sum(1 for t in r['fragments'] if t['in_folded'])
    total = len(r['fragments'])
    reason = reasons.get(r['id'])
    if not reason:
        if r['verdict'] == 'LOCATED':
            reason = 'every fragment found in the folded copy'
        elif r['verdict'] == 'PARTIAL':
            miss = [t['text'] for t in r['fragments'] if not t['in_folded']]
            reason = f'some fragments found; missing: {"; ".join(m[:40] for m in miss)}'
        elif r['verdict'] == 'ABSENT':
            reason = '2xx body served but no fragment found in folded copy (see note / diagnostics)'
        elif r['verdict'] == 'UNREACHABLE':
            reason = r['note'].split(' | ')[0][:160]
        else:
            reason = r['note'][:160]
    lines.append(f"| {r['id']} | `{r['_meta']['class']}` | {r['verdict']} | {r['http_status']} | "
                 f"{r['bytes']} | {found}/{total} | {reason} |")

lines += ['', '## Commands run', '']
for fr in fetched:
    lines.append('```')
    lines.append(' '.join(fr['cmd']))
    lines.append('```')
    if fr['id'] in DOI_IDS:
        lines.append('```')
        lines.append(' '.join(doi_heads[fr['id']][2]))
        lines.append('```')
lines += ['', '## Notes (full)', '']
for r in results:
    lines.append(f"- **{r['id']}** ({r['verdict']}): {r['note']}")
lines.append('')
with open(os.path.join(STAGE, 'verdicts-B.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

for r in results:
    print(f"{r['id']} {r['verdict']} http={r['http_status']} bytes={r['bytes']} "
          f"frags={sum(1 for t in r['fragments'] if t['in_folded'])}/{len(r['fragments'])}")
