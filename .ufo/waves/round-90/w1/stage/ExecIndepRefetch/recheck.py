#!/usr/bin/env python3
"""Re-check the scribe's landed evidence against this seat's independent captures.

Run from anywhere:
    python3 -B .ufo/waves/round-90/w1/stage/ExecIndepRefetch/recheck.py

Reads the scribe's manifest (reports/round-90/evidence/manifest.json in the lane, or the
stage copy under ScribeEntry/evidence/) plus any lesson gate lines, compares every quote
with this seat's own curl captures in caps/, and rewrites agreement.json. Exit 0 when every
quote is present, 1 when any is absent (naming the id and the missing span), 2 when there is
no manifest yet (nothing to compare - not a pass).

No network access: it compares against the captures this seat already fetched. A URL the
scribe used that this seat has not fetched is reported as `unfetched`, never guessed.
"""
import hashlib
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
CAPS = os.path.join(HERE, 'caps')
SCRIBE = os.path.join(LANE, '.ufo/waves/round-90/w1/stage/ScribeEntry')
AGREEMENT = os.path.join(HERE, 'agreement.json')


def norm(s):
    s = unicodedata.normalize('NFKC', str(s)).replace('\u2019', "'")
    s = ' '.join(s.split()).casefold()
    return re.sub(r'\s+([.,;:!?%\)\]])', r'\1', s)


def load_fetch():
    with open(os.path.join(HERE, 'fetch.json'), encoding='utf-8') as f:
        return json.load(f)


def find_manifest():
    for p in (os.path.join(LANE, 'reports/round-90/evidence/manifest.json'),
              os.path.join(SCRIBE, 'evidence/manifest.json'),
              os.path.join(SCRIBE, 'manifest.json')):
        if os.path.isfile(p):
            return p
    return ''


def find_lesson():
    for p in (os.path.join(LANE, 'corpus/lessons/round-90.md'),
              os.path.join(SCRIBE, 'lesson.md')):
        if os.path.isfile(p):
            return p
    return ''


def quote_from_lesson(lesson, rid):
    m = re.search(r'^[-*] ?' + rid + r'\b.*?[\u201c"]([^\u201d"]+)[\u201d"]', lesson, re.M)
    return m.group(1).strip() if m else ''


def main():
    fetch = load_fetch()
    by_url = {v['url']: k for k, v in fetch['captures'].items()}
    man_path = find_manifest()
    if not man_path:
        doc = json.load(open(AGREEMENT, encoding='utf-8')) if os.path.isfile(AGREEMENT) else {}
        doc.update(status='pending-absent', scribe_manifest=None, quote_agreement=[])
        json.dump(doc, open(AGREEMENT, 'w'), indent=1, sort_keys=True)
        print('PENDING: no scribe manifest; nothing to compare. Capture-level agreement stands.')
        return 2

    man = json.load(open(man_path, encoding='utf-8'))
    rows_in = man.get('rows', man)
    lesson_path = find_lesson()
    lesson = open(lesson_path, encoding='utf-8', errors='replace').read() if lesson_path else ''
    out = []
    for rid, rec in sorted(rows_in.items()):
        if not isinstance(rec, dict):
            continue
        url = str(rec.get('url', '')).strip()
        quote = str(rec.get('quote', '')).strip() or quote_from_lesson(lesson, rid)
        slug = by_url.get(url)
        if not slug:
            out.append(dict(id=rid, url=url, scribe_quote=quote, scribe_quote_present='unfetched',
                            note='this seat has no capture of this url; fetch it before trusting the quote'))
            continue
        p = os.path.join(CAPS, slug + '.txt')
        text = norm(open(p, encoding='utf-8', errors='replace').read())
        present = bool(quote) and norm(quote) in text
        idx = text.find(norm(quote)) if present else -1
        out.append(dict(id=rid, url=url, capture=f'caps/{slug}.txt', scribe_quote=quote,
                        scribe_quote_present='yes' if present else 'no',
                        my_sha256=hashlib.sha256(open(p, 'rb').read()).hexdigest(),
                        my_http_status=fetch['captures'][slug]['http_status'],
                        my_fetched_at=fetch['captures'][slug]['fetched_at'],
                        context=text[max(0, idx - 100):idx + 200] if present else ''))

    doc = json.load(open(AGREEMENT, encoding='utf-8')) if os.path.isfile(AGREEMENT) else {}
    doc.update(status='compared', scribe_manifest=man_path, quote_agreement=out)
    json.dump(doc, open(AGREEMENT, 'w'), indent=1, sort_keys=True)

    absent = [r for r in out if r['scribe_quote_present'] != 'yes']
    for r in absent:
        print(f'FINDING {r["id"]}: quote {r["scribe_quote_present"]}'
              + ('' if r['scribe_quote_present'] == 'unfetched' else f' - missing span: {r["scribe_quote"]!r}'))
    print(f'AGREEMENT: {len(out) - len(absent)}/{len(out)} scribe quotes located in this seat\'s captures')
    return 0 if not absent else 1


if __name__ == '__main__':
    sys.exit(main())
