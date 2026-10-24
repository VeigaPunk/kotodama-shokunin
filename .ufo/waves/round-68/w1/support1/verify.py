#!/usr/bin/env python3
"""Parse a row fragment, fetch live URL, check anchor quote + emit JSON."""
import json, re, subprocess, sys, html, urllib.parse

UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/128.0 Safari/537.36')

def fetch(url, timeout=30):
    p = subprocess.run(
        ['curl', '-sS', '-L', '-m', str(timeout), '-A', UA,
         '-w', '\n__CURL__%{http_code} %{url_effective}', url],
        capture_output=True, text=True)
    body = p.stdout
    code, eff = '000', url
    m = re.search(r'\n__CURL__(\d{3}) (\S+)\s*$', body)
    if m:
        code, eff = m.group(1), m.group(2)
        body = body[:m.start()]
    return code, eff, body, p.stderr.strip()

def strip_text(body):
    t = re.sub(r'(?is)<script.*?</script>|<style.*?</style>|<!--.*?-->', ' ', body)
    t = re.sub(r'(?s)<[^>]+>', ' ', t)
    t = html.unescape(t)
    return re.sub(r'\s+', ' ', t)

def norm_words(s):
    s = html.unescape(s).lower()
    s = re.sub(r"[’‘]", "'", s)
    return re.sub(r'\s+', ' ', re.sub(r"[^a-z0-9' ]+", ' ', s)).strip()

def main(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    out = {'file': path}
    for tag in ('ROW', 'BULLET', 'VERIFY', 'CAPTURE', 'ACCESS'):
        m = re.search(rf'^{tag}=(.*)$', raw, re.M)
        out[tag.lower()] = m.group(1).strip() if m else None
    row = out.get('row') or ''
    cells = [c.strip() for c in row.split('|')]
    out['cells'] = len(cells)
    sid = next((c for c in cells if re.fullmatch(r'S\d{3,}', c)), None)
    out['sid'] = sid
    urls = re.findall(r'https?://[^\s|"]+', row)
    live = [u for u in urls if 'web.archive.org' not in u]
    wb = [u for u in urls if 'web.archive.org' in u]
    out['live_url'] = live[0] if live else None
    out['wayback'] = wb[0] if wb else None
    mq = re.search(r'"([^"]{8,300})"|“([^“”]{8,300})”', row)
    out['quote'] = (mq.group(1) or mq.group(2)) if mq else None
    # teaches = second-to-last 4 cells are date/180d/entry/; find teaches as
    # cell after the quoted one
    if out['quote'] and out['quote'] in row:
        after = row.split(out['quote'], 1)[1]
        rest = [c.strip() for c in after.split('|') if c.strip()]
        out['teaches'] = rest[0] if rest else None
    if out['live_url']:
        code, eff, body, err = fetch(out['live_url'])
        out['http'] = code
        out['effective'] = eff
        out['fetch_err'] = err[:200] if err else None
        text = strip_text(body)
        out['body_len'] = len(text)
        ntext = norm_words(text)
        if out['quote']:
            nq = norm_words(out['quote'])
            out['quote_norm_hit'] = nq in ntext
            if not out['quote_norm_hit']:
                qw = nq.split()
                for k in range(len(qw), max(3, len(qw)-8), -1):
                    found = False
                    for i in range(0, len(qw)-k+1):
                        frag = ' '.join(qw[i:i+k])
                        if frag in ntext:
                            idx = ntext.find(frag)
                            out['partial'] = {'k': k, 'frag': frag,
                                'ctx': ntext[max(0,idx-120):idx+len(frag)+120]}
                            found = True
                            break
                    if found:
                        break
            else:
                idx = ntext.find(nq)
                out['qctx'] = ntext[max(0,idx-150):idx+len(nq)+150]
        open(path + '.body.txt', 'w', encoding='utf-8').write(text[:400000])
    print(json.dumps(out, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main(sys.argv[1])
