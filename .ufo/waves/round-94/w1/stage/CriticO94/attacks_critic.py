"""CriticO94 attack driver: NEW counterfeit classes (outside the frozen round-94
battery set A1,B1,G1,H1,I1,J1,K1) against the round-94 grader candidate.

Imports the wave battery driver read-only (battery94.py, falling back to
battery93.py) for the exact grading argument shape, builds forged mini-lanes in
scratch only, grades each with the tool under test, and writes a per-class
record. Lane files are never written.

Env:
  CRIT_REPO     lane root (read-only use)
  CRIT_WORK     scratch work dir (fixtures live here)
  CRIT_BATTERY  path to the battery driver whose grade() argument shape is used
  CRIT_TOOL     path to the tool under test
  CRIT_OUT      attacks markdown output path
"""
import hashlib
import importlib.util
import json
import os
import re
import sys
import unicodedata

sys.dont_write_bytecode = True

REPO = os.environ['CRIT_REPO']
WORK = os.environ['CRIT_WORK']
BATTERY = os.environ['CRIT_BATTERY']
TOOL = os.environ['CRIT_TOOL']
OUT = os.environ['CRIT_OUT']

spec = importlib.util.spec_from_file_location('bat', BATTERY)
bat = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bat)
bat.configure(TOOL, WORK)  # sets bat.TOOL, bat.WORK, bat.ENV; grade() reads them

mc = bat.mc
IDS = bat.IDS
AS_OF = bat.AS_OF
TEACH = bat.TEACH
DEFAULT_URLS = bat.DEFAULT_URLS
DEFAULT_MAN_QUOTE = bat.DEFAULT_MAN_QUOTE

# base rows of the fixture registry: the first (S776 role) carries the base
# disposition line; the second (S001 role) has no base disposition, so a lesson
# line for it is a forged GAIN.
def base_ids():
    txt = None
    for attr in ('base_registry_text',):
        fn = getattr(bat, attr, None)
        if fn:
            txt = fn()
    if txt:
        ids = re.findall(r'\| (S\d{3,}) \|', txt)
        if len(ids) >= 2:
            return ids[0], ids[1]
    return 'S776', 'S001'

OLD_BASE, OLD_FREE = base_ids()

FW = ''.join(chr(c) for c in (0xFF2C, 0xFF2F, 0xFF23, 0xFF21, 0xFF34, 0xFF25, 0xFF24))
MB = ''.join(chr(c) for c in (0x1D40B, 0x1D40E, 0x1D402, 0x1D400, 0x1D413, 0x1D404, 0x1D403))
assert unicodedata.normalize('NFKC', FW) == 'LOCATED'
assert unicodedata.normalize('NFKC', MB) == 'LOCATED'


def _reps(text, reps):
    for a, b in reps:
        assert a in text, a
        text = text.replace(a, b)
    return text


def dispo_extra(token):
    return f'{OLD_FREE} {token} recheck 90d accessed {AS_OF}\n'


# ---- counterfeit builders (each = G0 plus exactly one forgery) --------------

def b_g0():
    return bat.standard('G0')


def b_fw1():
    return bat.standard('FW1_fullwidth_verdict', lesson_extra=dispo_extra(FW))


def b_ma1():
    return bat.standard('MA1_mathbold_verdict', lesson_extra=dispo_extra(MB))


def b_cd1():
    return bat.standard('CD1_combining_acute_verdict', lesson_extra=dispo_extra('LOCA\u0301TED'))


def b_lr1():
    return bat.standard('LR1_lrm_split_verdict', lesson_extra=dispo_extra('LO\u200eCATED'))


def b_tab1():
    return bat.standard('TAB1_tab_in_verdict', lesson_extra=dispo_extra('LO\tCATED'))


def b_id1():
    return bat.standard('ID1_smallcap_id', lesson_extra=f'\ua731{OLD_FREE[1:]} LOCATED recheck 90d accessed {AS_OF}\n')


def b_zwj1():
    return bat.standard('ZWJ1_zwj_split_verdict', lesson_extra=dispo_extra('LO\u200dCATED'))


def b_crlf1():
    urls = {**DEFAULT_URLS}
    quotes = bat.default_quotes()
    text = bat.lesson_text(urls, quotes) + dispo_extra('LOCATED')
    return bat.standard('CRLF1_crlf_lesson', lesson_override=text.replace('\n', '\r\n'))


def b_num1():
    e = _reps(mc.body(None), [
        ('## 1. The address', '## 1.1 address'),
        ('## 2. The petition', '## 2.1 petition'),
        ('## 3. Fixed and extempore', '## 3.1 efficacy'),
        ('## 4. Efficacy', '## 4.1 table'),
        ('## 5. Table', '## 5. Notes')])
    return bat.standard('NUM1_nested_number_heads', entry=e)


def b_rm1():
    e = _reps(mc.body(None), [
        ('## 1. The address', '## I. address'),
        ('## 2. The petition', '## II. petition'),
        ('## 3. Fixed and extempore', '## III. efficacy'),
        ('## 4. Efficacy', '## IV. table'),
        ('## 5. Table', '## V. Notes')])
    return bat.standard('RM1_roman_number_heads', entry=e)


def b_num2():
    e = _reps(mc.body(None), [
        ('## 1. The address', '## Notes 1) address'),
        ('## 2. The petition', '## Notes 2) petition'),
        ('## 3. Fixed and extempore', '## Notes 3) efficacy'),
        ('## 4. Efficacy', '## Notes 4) table'),
        ('## 5. Table', '## Notes 5) Table')])
    return bat.standard('NUM2_numbered_second_token', entry=e)


def b_sp1():
    fx = bat.standard('SP1_indented_row')
    rid = 'S958'
    url = 'https://registry-example.org/verlan-case-3'
    quote = f'prayer address petition votive promise fixed extempore efficacy register case 3'
    # lands registry: the extra row, cells exactly eleven, indented past the
    # 3-space block-quote threshold at line start and inside the id cell
    row = '    |    ' + f'{rid} | {url} | docs | A | scope | anchor | {TEACH} | mined | {AS_OF} | 90d | {mc.ENTRY_NAME} |'
    lands = open(fx.lands, encoding='utf-8').read().rstrip('\n')
    put(fx.lands, lands + '\n' + row + '\n')
    # entry cites it
    entry = open(fx.entry, encoding='utf-8').read()
    put(fx.entry, entry.replace('S955 S956 S957 supply', 'S955 S956 S957 S958 supply'))
    # lesson gate line
    lesson = open(fx.lesson, encoding='utf-8').read().rstrip('\n')
    put(fx.lesson, lesson + '\n'
        + f'- {rid} admit A/mined. {url} \u2014 accessed {AS_OF} \u2014 body: \u201c{quote}\u201d\n')
    # capture + manifest row
    cap_rel = f'{bat.EV}/{rid}.txt'
    cap_path = fx.p(cap_rel)
    put(cap_path, f'Page text. prayer address petition votive promise fixed extempore efficacy register case 3. '
                  'Also site boilerplate and navigation. Freemium for Journals platform.')
    man = json.loads(open(fx.manifest, encoding='utf-8').read())
    man['rows'][rid] = dict(capture=cap_rel, url=url, http_status=200,
                            fetched_at=f'{AS_OF}T09:00:00-03:00',
                            sha256=hashlib.sha256(open(cap_path, 'rb').read()).hexdigest(),
                            quote=DEFAULT_MAN_QUOTE)
    put(fx.manifest, json.dumps(man, indent=1))
    return fx


def b_mn1():
    fx = bat.standard('MN1_manifest_dict_no_url')
    man = json.loads(open(fx.manifest, encoding='utf-8').read())
    del man['rows'][IDS[0]]['url']  # dict value missing the url key
    put(fx.manifest, json.dumps(man, indent=1))
    return fx


def put(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.lexists(path):
        os.remove(path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)


ATTACKS = [
    ('G0', 'battery green control (must pass rc 0)', 'unmodified mini-lane', b_g0),
    ('FW1', 'gained-disposition forgery', f'lesson line "{OLD_FREE} {FW} recheck 90d accessed {AS_OF}" - verdict token in fullwidth Latin (NFKC-folds to LOCATED)', b_fw1),
    ('MA1', 'gained-disposition forgery', f'lesson line "{OLD_FREE} {MB} recheck 90d accessed {AS_OF}" - verdict token in mathematical bold (NFKC-folds to LOCATED)', b_ma1),
    ('CD1', 'gained-disposition forgery', f'lesson line "{OLD_FREE} LOCA\\u0301TED ..." - combining acute U+0301 inside the verdict token (Mn, invisible to a letters-only scan)', b_cd1),
    ('LR1', 'gained-disposition forgery', f'lesson line "{OLD_FREE} LO\\u200eCATED ..." - LTR mark U+200E splits the verdict; zero-width but Cf, NOT in the tool\'s zero-width strip set', b_lr1),
    ('TAB1', 'gained-disposition forgery', f'lesson line "{OLD_FREE} LO\\tCATED ..." - horizontal tab splits the verdict token', b_tab1),
    ('ID1', 'gained-disposition forgery', f'lesson line "\\ua731{OLD_FREE[1:]} LOCATED ..." - small-capital S (U+A731, category Ll) in the id token; verdict token is clean ASCII', b_id1),
    ('ZWJ1', 'strip-control (expected refusal)', f'lesson line "{OLD_FREE} LO\\u200dCATED ..." - ZWJ U+200D is in the strip set, so the tool must SEE the gain and refuse on APPENDONLY', b_zwj1),
    ('CRLF1', 'gained-disposition forgery', f'whole lesson with CRLF endings; gained line "{OLD_FREE} LOCATED recheck 90d accessed {AS_OF}"', b_crlf1),
    ('NUM1', 'G1-family heading forgery', 'all five h2 re-headed to nested-numbered phrase-only ("## 1.1 address" ...); stripping ^\\d+[.)] leaves ".1" so the token floor still passes', b_num1),
    ('RM1', 'G1-family heading forgery', 'all five h2 re-headed to roman-numbered phrase-only ("## I. address" ...); ^\\d+[.)] never matches roman numerals', b_rm1),
    ('NUM2', 'G1-family heading forgery', 'second-token numbered headings with bare anchors ("## Notes 1) address" ... "## Notes 4) table"); the leading-number strip sees "Notes" first, so the anchor span passes', b_num2),
    ('SP1', 'registry-visability forgery', 'eleven-cell lands row for S958 indented four spaces at line start and inside the id cell; entry cites S958 with gate line, capture and manifest row', b_sp1),
    ('MN1', 'manifest-shape forgery', f'manifest row value for {IDS[0]} is a dict MISSING the url key (capture/quote/sha intact)', b_mn1),
]

UPPERTOK = re.compile(r'\b[A-Z][A-Z_]{2,}\b')


def classify(rc, out):
    fails = sorted(set(re.findall(r'FAIL\s+([A-Z]+)', out)))
    if rc == 0:
        return 'SURVIVOR'
    if 'Traceback' in out:
        return 'UNNAMED-traceback'
    if fails:
        return 'REFUSED-NAMED:' + ','.join(fails)
    err = [l for l in out.splitlines() if l.startswith('ADVANCE-EVIDENCE_ERROR')]
    toks = sorted(set(t for l in err for t in UPPERTOK.findall(l.split(':', 1)[-1])))
    if toks:
        return 'REFUSED-NAMED-TOK:' + ','.join(toks)
    return f'UNNAMED rc={rc}'


def named_line(out):
    for l in out.splitlines():
        if 'FAIL' in l or l.startswith('ADVANCE-EVIDENCE_ERROR'):
            return l[:220]
    return (out.splitlines() or ['no output'])[-1][:220]


def main():
    os.makedirs(WORK, exist_ok=True)
    os.makedirs(WORK + '/tmp', exist_ok=True)
    sha_tool = hashlib.sha256(open(TOOL, 'rb').read()).hexdigest()
    sha_bat = hashlib.sha256(open(BATTERY, 'rb').read()).hexdigest()
    results = []
    for aid, family, recipe, builder in ATTACKS:
        fx = builder()
        rc, out, cmd = bat.grade(fx)
        outcome = ('CONTROL-CLEAN' if rc == 0 else 'CONTROL-FAIL') if aid == 'G0' else classify(rc, out)
        results.append(dict(id=aid, family=family, recipe=recipe, rc=rc, cmd=cmd,
                            outcome=outcome, named=named_line(out), out=out))
    lines = []
    lines.append(f'# CriticO94 attacks — NEW counterfeit classes vs tool sha256 {sha_tool}')
    lines.append('')
    lines.append(f'Battery driver imported read-only for the argument shape: `{BATTERY}` sha256 {sha_bat}.')
    lines.append(f'Fixture base rows: {OLD_BASE} (base disposition), {OLD_FREE} (forged gain). '
                 'All fixtures under ' + WORK + '/work; no lane file touched.')
    lines.append('')
    n_surv = sum(1 for r in results if r['outcome'] == 'SURVIVOR')
    n_ref = sum(1 for r in results if r['outcome'].startswith('REFUSED-NAMED'))
    n_unn = sum(1 for r in results if r['outcome'].startswith('UNNAMED'))
    lines.append(f'SURVIVORS {n_surv}; UNNAMED {n_unn}; REFUSED-NAMED {n_ref}')
    lines.append('')
    lines.append('| id | family | rc | outcome | named line |')
    lines.append('|---|---|---|---|---|')
    for r in results:
        lines.append(f'| {r["id"]} | {r["family"]} | {r["rc"]} | {r["outcome"]} | `{r["named"]}` |')
    lines.append('')
    for r in results:
        lines.append(f'## {r["id"]} — {r["outcome"]}')
        lines.append('')
        lines.append(f'- Family: {r["family"]}')
        lines.append(f'- Recipe: {r["recipe"]}')
        lines.append(f'- Command: `{r["cmd"]}`')
        lines.append(f'- rc: {r["rc"]}')
        lines.append('- Tool output:')
        lines.append('```')
        lines.append(r['out'])
        lines.append('```')
        lines.append('')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f'SURVIVORS {n_surv}; UNNAMED {n_unn}; REFUSED-NAMED {n_ref}')
    for r in results:
        print(f'{r["id"]:6} rc={r["rc"]} -> {r["outcome"]}')


if __name__ == '__main__':
    main()
