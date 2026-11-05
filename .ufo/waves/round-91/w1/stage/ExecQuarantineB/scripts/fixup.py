#!/usr/bin/env python3
"""Restore class-as-registered column; append explicit conclusion sentences to notes; rewrite MD."""
import os, re, json

STAGE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB'
SLICE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-91/quarantine/slice.tsv'
MINE = ['S807', 'S812', 'S814', 'S816', 'S817', 'S820', 'S823', 'S824', 'S825', 'S827', 'S835']

classes = {}
with open(SLICE, encoding='utf-8') as f:
    lines = [l.rstrip('\n') for l in f]
header = lines[0].split('\t')
for l in lines[1:]:
    if not l.strip():
        continue
    d = dict(zip(header, l.split('\t')))
    if d['id'] in MINE:
        classes[d['id']] = d['class'].strip()

CONCL = {
 'S807': 'Conclusion: fetch now succeeds (prose "could not be fetched" is stale); row stays UNVERIFIABLE '
         'because the register cell carries no quote to check; served object is the Onoma 51 article PDF '
         '"Linguistic composition and characteristics of Chinese given names" (Kalu\u017cy\u0144ska).',
 'S812': 'Conclusion: still unfetchable by ordinary request (Cambridge "Too many automated requests from '
         'this network" wall); row has no quote cell, so no span was checkable.',
 'S814': 'Conclusion: nginx 403 Forbidden wall; no content served; quote uncheckable.',
 'S816': 'Conclusion: served body is the correct interview article (\u7231\u6f5c\u6c34\u7684\u4e4c\u8d3c:'
         '\u201c\u6211\u5148\u8bbe\u5b9a\u4e16\u754c\u89c2,\u518d\u8003\u8651\u600e\u4e48\u5347\u7ea7\u201d) '
         'in UTF-8, but the cited sentence\u2019s words (\u80af\u5b9a\u8003\u8651\u8fc7 / \u8d44\u6df1\u8bfb\u8005) '
         'appear nowhere in it; quote as registered is absent from this page.',
 'S817': 'Conclusion: served body is a Chinese web-literature article; the registered English fragment '
         '(Sowers-Wills / Phonology from the inside out) appears nowhere in it; citation points at a page '
         'that does not contain the quote.',
 'S820': 'Conclusion: quote IS present in the PDF text layer, verbatim in wording, at folded offsets '
         '\u224810065\u201310154 \u2014 the registered fragment fails only on quote glyphs (registered '
         "ASCII '\\'' vs source U+201C \u201c\u201d) and the register cell is truncated mid-word "
         "('female aesthetic val'); mechanically ABSENT by the prescribed byte-level pipeline, "
         'locatable in substance.',
 'S823': 'Conclusion: SafeLine WAF block page (body references /.safeline/ static assets and an empty '
         '<title id="slg-title">); article content not served; quote uncheckable.',
 'S824': 'Conclusion: ABSENT under the byte-level pipeline, verified by fragment-level test: the two halves '
         'of the registered fragment (習俗、輩行字を使って名づける and 輩行字命名の習俗) each occur in the '
         'pdftotext text layer (plain and -layout), but the full fragment as one contiguous span does not '
         '(fold test False in both modes): the passage is in the source, scattered across reading order.',
 'S825': 'Conclusion: not a JS shell (6838 chars of server-rendered text, 国立公文書館デジタルアーカイブ 詳細検索). '
         'Verified fragment-level: each component of the cited table line occurs (元号名称 開始西暦年; 令和 2019; '
         '平成 1989; 昭和 1926; 大正 1912; 明治 1868) but the full line is not contiguous after fold, and the '
         'second fragment 元号名称/開始西暦年 (fullwidth slash folded to /) is not present; ABSENT as served today.',
 'S827': 'Conclusion: all three cited snippets on the Springer chapter landing page (Conlangs in '
         'Theoretical Linguistics / The Palgrave Handbook of Constructed Languages / Springer Nature '
         'Switzerland); LOCATED.',
 'S835': 'Conclusion: repository under maintenance since 2026-10-28 15:00 (\u505c\u6b62\u671f\u9593 notice '
         'on the 503 page); still unfetchable, consistent with the registered prose.',
}

with open(os.path.join(STAGE, 'verdicts-B.json'), encoding='utf-8') as f:
    results = json.load(f)

for r in results:
    r['note'] = r['note'].split(' | Conclusion:')[0] + ' | ' + CONCL[r['id']]
    r['class'] = classes[r['id']]

# keep spec schema order: id, url, http_status, bytes, sha256, fetched_at, fragments, verdict, note
order = ['id', 'url', 'http_status', 'bytes', 'sha256', 'fetched_at', 'fragments', 'verdict', 'note']
out = []
for r in results:
    o = {k: r[k] for k in order}
    out.append(o)
with open(os.path.join(STAGE, 'verdicts-B.json'), 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

lines = ['# verdicts-B \u2014 ExecQuarantineB (kotodama round-91 quarantine hand-check)', '',
         'Fetched 2026-11-05 (per-row instants in verdicts-B.json, TZ offset -03:00); one '
         '`curl -sS -L --max-time 40 -o <stage>/caps/<id>.bin -w \'%{http_code} %{size_download} '
         '%{content_type}\'` per URL; captures retained in `caps/`. Fragments split on U+2026, three '
         'dots and `<br>` (the register\u2019s snippet separator); folded copy = UTF-8(replace) \u2192 tags '
         '\u2192 single space \u2192 entities decoded \u2192 U+00A0/U+2003 to space \u2192 NFKC \u2192 whitespace '
         'collapsed \u2192 casefold. Verdicts follow the frozen taxonomy: LOCATED / PARTIAL / ABSENT '
         '(2xx, no fragment) / UNREACHABLE (non-2xx, empty, wall, JS shell) / UNVERIFIABLE (prose cell, '
         'no checkable span). Rule used for the three prose rows: fetch fails \u2192 UNREACHABLE; fetch '
         'succeeds \u2192 UNVERIFIABLE; the note states what the URL served. PDF text-layer and '
         're-encoding checks are diagnostics in notes, never the verdict.', '',
         '| id | class-as-registered | verdict | http | bytes | fragments found/total | reason |',
         '|---|---|---|---|---|---|---|']
for r in out:
    found = sum(1 for t in r['fragments'] if t['in_folded'])
    total = len(r['fragments'])
    rid = r['id']
    concl = CONCL[rid]
    if rid in ('S807', 'S812', 'S835'):
        reason = concl
    elif r['verdict'] == 'LOCATED':
        reason = concl
    elif r['verdict'] == 'PARTIAL':
        miss = [t['text'] for t in r['fragments'] if not t['in_folded']]
        reason = 'some fragments found; missing: ' + '; '.join(m[:40] for m in miss) + ' | ' + concl
    elif r['verdict'] == 'ABSENT':
        reason = '2xx body served, no fragment in folded copy | ' + concl
    else:
        reason = concl
    reason = reason.replace('|', '/').replace('\n', ' ')
    cls = classes[rid]
    lines.append(f"| {rid} | {cls} | {r['verdict']} | {r['http_status']} | {r['bytes']} | "
                 f"{found}/{total} | {reason} |")

lines += ['', '## Commands run', '']
urls = {r['id']: r['url'] for r in out}
for rid in MINE:
    lines.append('```')
    lines.append(f"curl -sS -L --max-time 40 -o {STAGE}/caps/{rid}.bin "
                 f"-w '%{{http_code}} %{{size_download}} %{{content_type}}' '{urls[rid]}'")
    lines.append('```')
    if rid in ('S807', 'S812', 'S827'):
        lines.append('```')
        lines.append(f"curl -sS -I -L --max-time 40 -o /dev/null -w '%{{url_effective}} %{{http_code}}' '{urls[rid]}'")
        lines.append('```')

lines += ['', '## Notes (full, per row)', '']
for r in out:
    lines.append(f"- **{r['id']}** ({r['verdict']}, http {r['http_status']}, {r['bytes']} B, "
                 f"sha256 {r['sha256']}, fetched_at {r['fetched_at']}): {r['note']}")
lines.append('')
with open(os.path.join(STAGE, 'verdicts-B.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('rewrote verdicts-B.json (11 rows, spec schema) and verdicts-B.md')
for r in out:
    print(r['id'], r['verdict'], r['class'][:40])
