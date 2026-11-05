#!/usr/bin/env python3
"""CriticClaims92 attack driver (read-only attack seat).

Imports the frozen round-92 fixture builder (reports/round-92/controls/make-counterfeits.py,
sha256 86d3b816...) for its constants and row helper, builds each counterfeit mini-lane in
SCRATCH/work/<name>, and grades it with the frozen entry mode of
tools/check-advance-evidence.py (sha256 905be2fe...) under set-B arguments
(--min-anchor-span 3 --min-gate-overlap 3). Writes the per-counterfeit record to
STAGE/attacks.md. Nothing in the repo is written; the frozen files are read only.
"""
import hashlib
import importlib.util
import json
import os
import re
import shlex
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True

REPO = '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
TOOL = REPO + '/tools/check-advance-evidence.py'
BUILDER = REPO + '/reports/round-92/controls/make-counterfeits.py'
SCRATCH = '/fast/scratch/hyaku/kotodama-r92/CriticClaims92'
WORK = SCRATCH + '/work'
STAGE = REPO + '/.ufo/waves/round-92/w1/stage/CriticClaims92'
EV = 'reports/round-90/evidence'
IDS = ['S955', 'S956', 'S957']
AS_OF = '2026-11-05'
DEFAULT_URLS = {'S955': 'https://registry-example.org/verlan-case-0',
                'S956': 'https://registry-example.org/verlan-case-1',
                'S957': 'https://registry-example.org/verlan-case-2'}
BASE_URL = 'https://registry-example.org/base-prayer-notes'
TEACH = 'prayer address petition votive promise register case'
DEFAULT_MAN_QUOTE = 'prayer address petition votive promise fixed extempore efficacy register case'
BASE_LESSON = ('- S776 LOCATED recheck unchanged \u2014 ' + BASE_URL
               + ' accessed 2026-10-01: \u201can old base row about prayer notes and rubrics\u201d\n')

spec = importlib.util.spec_from_file_location('mc', BUILDER)
mc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mc)
ENV = dict(os.environ, TMPDIR=SCRATCH + '/tmp')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def put(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.lexists(path):
        os.remove(path)
    if isinstance(data, bytes):
        with open(path, 'wb') as f:
            f.write(data)
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(data)


def default_caps():
    return {rid: (f'Page text. prayer address petition votive promise fixed extempore efficacy register case {i}. '
                  'Also site boilerplate and navigation. Freemium for Journals platform.')
            for i, rid in enumerate(IDS)}


def default_quotes():
    return {rid: f'prayer address petition votive promise fixed extempore efficacy register case {i}'
            for i, rid in enumerate(IDS)}


def lands_text(urls, s776_teach=None, s001=True):
    rows = [mc._row('S776', BASE_URL, s776_teach or 'an old base row about prayer notes and rubrics')]
    if s001:
        rows.append(mc._row('S001', 'https://registry-example.org/base-old',
                            'another old base row about unrelated dye plants'))
    rows += [mc._row(rid, urls[rid], TEACH) for rid in IDS]
    return mc.HEADER + '\n' + '\n'.join(rows) + '\n'


def lesson_text(urls, quotes, extra=''):
    lines = [f'- {rid} admit A/mined. {urls[rid]} \u2014 accessed {AS_OF} \u2014 body: \u201c{quotes[rid]}\u201d'
             for rid in IDS]
    return '\n'.join(lines) + '\n' + extra


def base_registry_text():
    return (mc.HEADER + '\n'
            + mc._row('S776', BASE_URL, 'an old base row about prayer notes and rubrics') + '\n'
            + mc._row('S001', 'https://registry-example.org/base-old',
                      'another old base row about unrelated dye plants') + '\n')


class FX:
    def __init__(self, name):
        self.name = name
        self.root = os.path.join(WORK, name)
        shutil.rmtree(self.root, ignore_errors=True)
        os.makedirs(self.root)
        self.base = self.p('base.md')
        self.lands = self.p('lands.md')
        self.lesson = self.p('lesson.md')
        self.base_lesson = self.p('base-lesson.md')
        self.entry = self.p(mc.ENTRY_NAME)
        self.manifest = self.p('manifest.json')

    def p(self, rel):
        return os.path.join(self.root, rel)

    def fixture(self):
        return dict(root=self.root, base=self.base, lands=self.lands, lesson=self.lesson,
                    entry=self.entry, manifest=self.manifest, base_lesson=self.base_lesson)


def standard(name, urls=None, quotes=None, man_quotes=None, entry=None, caps=None, symlinks=None,
             s776_teach=None, s001=True, lesson_extra='', lesson_override=None, manifest_override=None):
    fx = FX(name)
    urls = {**DEFAULT_URLS, **(urls or {})}
    quotes = {**default_quotes(), **(quotes or {})}
    man_quotes = {**{rid: DEFAULT_MAN_QUOTE for rid in IDS}, **(man_quotes or {})}
    caps = {**default_caps(), **(caps or {})}
    symlinks = symlinks or {}
    put(fx.base, base_registry_text())
    put(fx.lands, lands_text(urls, s776_teach, s001))
    put(fx.base_lesson, BASE_LESSON)
    put(fx.lesson, lesson_override if lesson_override is not None else lesson_text(urls, quotes, lesson_extra))
    put(fx.entry, entry if entry is not None else mc.body(None))
    for rid in IDS:
        rel = f'{EV}/{rid}.txt'
        if rid in symlinks:
            if os.path.lexists(fx.p(rel)):
                os.remove(fx.p(rel))
            os.makedirs(os.path.dirname(fx.p(rel)), exist_ok=True)
            os.symlink(symlinks[rid], fx.p(rel))
        else:
            put(fx.p(rel), caps[rid])
    rows = {}
    for rid in IDS:
        rel = f'{EV}/{rid}.txt'
        data = open(fx.p(rel), 'rb').read()  # follows symlinks, as the grader does
        rows[rid] = dict(capture=rel, url=urls[rid], http_status=200,
                         fetched_at='2026-11-05T09:00:00-03:00', sha256=sha(data),
                         quote=man_quotes[rid])
    put(fx.manifest, manifest_override if manifest_override is not None else json.dumps({'rows': rows}, indent=1))
    return fx


def grade(fx):
    a = ['--root', fx.root, 'entry',
         '--entry', fx.entry,
         '--base-registry', fx.base,
         '--lands-registry', fx.lands,
         '--lesson', fx.lesson,
         '--manifest', fx.manifest,
         '--capture-dir', EV,
         '--as-of', AS_OF,
         '--topic', mc.TOPIC,
         '--topic-phrases', mc.PHRASES,
         '--min-topic-phrases', '4',
         '--min-bytes', '1200',
         '--min-headings', '4',
         '--min-new-ids', '3',
         '--min-topic-overlap', '8',
         '--table-min-rows', '5',
         '--table-min-cols', '3',
         '--base-lesson', fx.base_lesson,
         '--graded', 'corpus/SOURCES.md',
         '--graded', 'lesson.md',
         '--min-anchor-span', '3',
         '--min-gate-overlap', '3']
    cmd = [sys.executable, '-B', TOOL] + a
    r = subprocess.run(cmd, capture_output=True, text=True, env=ENV, cwd=SCRATCH)
    out = ((r.stdout or '') + (r.stderr or '')).strip()
    return r.returncode, out, shlex.join(cmd)


# ---- counterfeit builders -------------------------------------------------

def b_g0():
    return standard('G0')


def b_chrome_noforge():
    return standard('C1c_chrome_noforge',
                    entry=mc.body(own_sentence='Freemium for Journals platform carries this note.'),
                    quotes={'S955': 'Freemium for Journals platform'})


def b_chrome_forged():
    return standard('A1_chrome_forged_manifest',
                    entry=mc.body(own_sentence='Freemium for Journals platform carries this note.'),
                    quotes={'S955': 'Freemium for Journals platform'},
                    man_quotes={'S955': 'Freemium Journals platform prayer address petition'})


def b_url(variant):
    def f():
        return standard('A2_url_' + re.sub(r'\W+', '_', variant)[:24], urls={'S955': variant})
    return f


ENTRY_A3 = mc.body(None)
Q_A3 = 'A prayer opens by naming the deity in the vocative'


def b_a3_exact():
    return standard('A3a_entry_exact_copy', entry=ENTRY_A3, caps={'S955': ENTRY_A3},
                    quotes={'S955': Q_A3}, man_quotes={'S955': 'prayer opens naming deity vocative'})


def b_a3_plus1():
    return standard('A3b_entry_plus_newline', entry=ENTRY_A3, caps={'S955': ENTRY_A3 + '\n'},
                    quotes={'S955': Q_A3}, man_quotes={'S955': 'prayer opens naming deity vocative'})


def _reps(text, reps):
    for a, b in reps:
        assert a in text, a
        text = text.replace(a, b)
    return text


def b_a4_span():
    e = _reps(mc.body(None), [
        ('## 1. The address', '## address'),
        ('## 2. The petition', '## petition'),
        ('## 3. Fixed and extempore', '## efficacy'),
        ('## 4. Efficacy', '## Notes'),
        ('## 5. Table', '## Rites'),
        ('| element | fixed | extempore |', '| table | fixed | extempore |')])
    return standard('A4a_three_minimal_headings', entry=e)


def b_a4_onehead():
    e = _reps(mc.body(None), [
        ('## 1. The address', '## address petition efficacy table'),
        ('## 2. The petition', '## Two'),
        ('## 3. Fixed and extempore', '## Three'),
        ('## 4. Efficacy', '## Four'),
        ('## 5. Table', '## Five')])
    return standard('A4b_all_phrases_one_heading', entry=e)


def b_lesson(extra, name):
    return lambda: standard(name, lesson_extra=extra)


def b_a6d_meta():
    caps = {'S955': ('<!doctype html><html><head><meta name="description" content="'
                     'prayer address petition votive promise fixed extempore efficacy register case 0">'
                     '</head><body><nav>Freemium for Journals platform</nav><script>var x=1;</script>'
                     '</body></html>')}
    return standard('A6e_quote_only_in_meta', caps=caps)


def b_a6f_decoy():
    urls = DEFAULT_URLS
    quotes = default_quotes()
    line1 = (f'- S955 admit A/mined. {urls["S955"]} \u2014 accessed {AS_OF} \u2014 '
             f'\u201c{quotes["S955"]}\u201d \u2014 body: \u201cFreemium for Journals platform\u201d\n')
    rest = ''.join(f'- {rid} admit A/mined. {urls[rid]} \u2014 accessed {AS_OF} \u2014 body: \u201c{quotes[rid]}\u201d\n'
                   for rid in ('S956', 'S957'))
    return standard('A6f_decoy_first_quote', lesson_override=line1 + rest)


def b_a6c_symlink_inroot():
    target = os.path.join(WORK, 'A6c_symlink_inroot_base_lesson', 'base-lesson.md')
    return standard('A6c_symlink_inroot_base_lesson',
                    quotes={'S955': 'an old base row about prayer notes and rubrics'},
                    man_quotes={'S955': 'an old base row about prayer notes and rubrics'},
                    symlinks={'S955': target})


def b_a6d_symlink_outside():
    outdir = os.path.join(SCRATCH, 'outside')
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir, 'S955-page.txt')
    put(outfile, default_caps()['S955'])
    return standard('A6d_symlink_outside_root', symlinks={'S955': outfile})


def b_a6a_base_rewrite():
    return standard('A6a_base_row_teaches_rewritten_in_lands',
                    s776_teach='prayer address petition votive promise fixed extempore efficacy register case')


def b_a6b_base_row_dropped():
    return standard('A6b_base_row_S001_dropped_in_lands', s001=False)


def b_a6g_manifest_list():
    return standard('A6g_manifest_rows_as_list', manifest_override=json.dumps({'rows': [1, 2, 3]}))


ATTACKS = [
    # id, expectation, recipe, builder
    ('G0', 'CLEAN', 'Compliant control: set-B grade of the unmodified mini-lane.', b_g0),
    ('C1c', 'REFUSE:GATE', 'Control for attack 1: chrome quote as an own sentence in the entry, manifest quote NOT forged.', b_chrome_noforge),
    ('A1', 'SURVIVE', 'Chrome quote "Freemium for Journals platform" as the gate quote, the same string as the entry\'s own sentence, and the manifest quote field forged to "Freemium Journals platform prayer address petition" so the content-word bind (3 words) passes.', b_chrome_forged),
    ('A2a', 'REFUSE:UNIQUENESS', 'Combined fragment + trailing slash + uppercase host: S955 url "https://REGISTRY-EXAMPLE.org/base-prayer-notes/#polari" (requested combined shadow).', b_url('https://REGISTRY-EXAMPLE.org/base-prayer-notes/#polari')),
    ('A2b', 'REFUSE:GATE/CAPTURE', 'Uppercase scheme "HTTPS://registry-example.org/base-prayer-notes": URL_RE is case-sensitive, so UNIQUENESS sees no url at all; another leg must refuse.', b_url('HTTPS://registry-example.org/base-prayer-notes')),
    ('A2c', 'SURVIVE', 'Scheme swap: S955 url "http://registry-example.org/base-prayer-notes" (same host and path as base S776 under http).', b_url('http://registry-example.org/base-prayer-notes')),
    ('A2d', 'SURVIVE', 'Host prefix: S955 url "https://www.registry-example.org/base-prayer-notes".', b_url('https://www.registry-example.org/base-prayer-notes')),
    ('A2e', 'SURVIVE', 'Query suffix: S955 url "https://registry-example.org/base-prayer-notes?ref=lane".', b_url('https://registry-example.org/base-prayer-notes?ref=lane')),
    ('A2f', 'SURVIVE', 'Path case: S955 url "https://registry-example.org/Base-Prayer-Notes".', b_url('https://registry-example.org/Base-Prayer-Notes')),
    ('A3a', 'REFUSE:CAPTURE', 'Capture file S955.txt is a byte-exact copy of the ENTRY; gate quote is an entry prose sentence; manifest sha = entry sha.', b_a3_exact),
    ('A3b', 'SURVIVE', 'Capture file S955.txt is the ENTRY plus one trailing newline (sha differs from the graded entry, text identical after norm).', b_a3_plus1),
    ('A4a', 'SURVIVE', 'Span gaming: four h2 headings, three of them a single phrase each ("## address", "## petition", "## efficacy"), "table" in the table header row; topical prose otherwise.', b_a4_span),
    ('A4b', 'REFUSE:TOPIC', 'Control for attack 4: all four phrases in one heading, no other heading or table hit (span 1).', b_a4_onehead),
    ('A5a', 'CLEAN', 'Prose sentence "S776 located in the archive, ..." in the lands lesson; S776 base disposition is LOCATED, so no movement.', b_lesson('S776 located in the archive, rechecked against the registry row.\n', 'A5a_prose_S776_located')),
    ('A5b', 'REFUSE:APPENDONLY', 'Prose sentence "S001 located in the archive, ..." in the lands lesson; S001 has no base disposition line (over-fire test on honest prose).', b_lesson('S001 located in the archive, rechecked against the registry row.\n', 'A5b_prose_S001_located')),
    ('A5c', 'REFUSE:APPENDONLY', 'Control for 5b: "S001 NOT located in the archive, ..." prose line (verdict flip spelled with a space).', b_lesson('S001 NOT located in the archive, rechecked against the registry row.\n', 'A5c_prose_S001_not_located')),
    ('A5d', 'SURVIVE', 'Bold-wrapped disposition "**S001** LOCATED recheck 90d accessed 2026-11-05" (under-fire: DISPO_RE anchor needs the id at line start after an optional whitespace-terminated prefix).', b_lesson('**S001** LOCATED recheck 90d accessed 2026-11-05\n', 'A5d_bold_disposition')),
    ('A5e', 'SURVIVE', 'Table-row disposition "| S001 | LOCATED | accessed 2026-11-05 |" in the lands lesson.', b_lesson('| S001 | LOCATED | accessed 2026-11-05 |\n', 'A5e_table_row_disposition')),
    ('A5f', 'SURVIVE', 'Zero-width space inside the verdict: "S001 LOC\\u200bATED recheck 90d accessed 2026-11-05" (renders as LOCATED, regex sees no token).', b_lesson('S001 LOC\u200bATED recheck 90d accessed 2026-11-05\n', 'A5f_zwsp_verdict')),
    ('A6a', 'SURVIVE', 'Invented class: lands registry base row S776 teaches cell rewritten to a flattering string (entry mode has no OTHERCELLS leg; base registry itself unchanged).', b_a6a_base_rewrite),
    ('A6b', 'SURVIVE', 'Invented class: base row S001 deleted from the lands registry (entry mode does not compare lands base rows to base).', b_a6b_base_row_dropped),
    ('A6c', 'SURVIVE', 'Invented class: S955 capture is an in-root SYMLINK to base-lesson.md (not graded, lexically confined path, sha matches target, quote in target bytes). Residual of routed finding 6 (non-graded blob).', b_a6c_symlink_inroot),
    ('A6d', 'SURVIVE', 'Invented class: S955 capture is a SYMLINK escaping the repository root to a file in the scratch dir (lexical confinement only).', b_a6d_symlink_outside),
    ('A6e', 'SURVIVE', 'Invented class: quote exists only in raw HTML markup (meta content attribute) of the capture, not in rendered text; CAPTURE matches raw bytes.', b_a6d_meta),
    ('A6f', 'SURVIVE', 'Invented class: gate line carries a valid first quote (bound, in capture) and a chrome "body:" quote second; only the first quote is ever checked.', b_a6f_decoy),
    ('A6g', 'REFUSE:unnamed', 'Operability probe: manifest with rows as a list (not a dict). Expected: unnamed traceback, not a named leg.', b_a6g_manifest_list),
]


def legs_of(out):
    fails = re.findall(r'FAIL\s+([A-Z]+)', out)
    passes = re.findall(r'PASS\s+([A-Z]+)', out)
    return sorted(set(fails)), sorted(set(passes))


def classify(expect, rc, out):
    fails, passes = legs_of(out)
    if rc == 0:
        return 'SURVIVOR' if expect == 'SURVIVE' else 'CLEAN'
    if rc == 1 and fails:
        return 'refused on ' + ','.join(fails)
    return f'refused-unnamed (rc={rc})'


def main():
    os.makedirs(WORK, exist_ok=True)
    os.makedirs(SCRATCH + '/tmp', exist_ok=True)
    os.makedirs(STAGE, exist_ok=True)
    sha_tool = sha(open(TOOL, 'rb').read())
    sha_builder = sha(open(BUILDER, 'rb').read())
    assert sha_tool == '905be2fed386c491d52224832ea75ed8c7b02e67c1b021b2c66511658c1c1422', sha_tool
    results = []
    for aid, expect, recipe, builder in ATTACKS:
        fx = builder()
        rc, out, cmd = grade(fx)
        outcome = classify(expect, rc, out)
        verdict = out.splitlines()[-1] if out else 'no output'
        with open(os.path.join(SCRATCH, f'{aid}.out.txt'), 'w', encoding='utf-8') as f:
            f.write(out + '\n')
        results.append(dict(id=aid, expect=expect, recipe=recipe, rc=rc, cmd=cmd,
                            verdict=verdict, outcome=outcome, out=out))
    survivors = [r for r in results if r['outcome'] == 'SURVIVOR']
    refused = [r for r in results if r['outcome'].startswith('refused')]
    mismatch = [r for r in results if (r['expect'] == 'SURVIVE') != (r['outcome'] == 'SURVIVOR')
                and r['expect'] not in ('REFUSE:unnamed',) and not (r['expect'].startswith('REFUSE') and r['outcome'].startswith('refused'))
                and r['expect'] != 'CLEAN']
    # selftest of frozen tool, for the record
    os.makedirs(SCRATCH + '/selftest', exist_ok=True)
    st = subprocess.run([sys.executable, '-B', TOOL, '--selftest', '--work', SCRATCH + '/selftest'],
                        capture_output=True, text=True, env=ENV, cwd=SCRATCH)
    st_out = (st.stdout + st.stderr).strip().splitlines()
    lines = []
    lines.append('# attacks.md — CriticClaims92 counterfeit battery against the frozen v3 entry mode')
    lines.append('')
    lines.append(f'Frozen tool: tools/check-advance-evidence.py sha256 {sha_tool} (matches O.tool_sha256).')
    lines.append(f'Fixture builder imported read-only: reports/round-92/controls/make-counterfeits.py sha256 {sha_builder}.')
    lines.append('Args: entry mode, set B (--min-anchor-span 3 --min-gate-overlap 3), plus the builder floors '
                 '(--min-topic-phrases 4 --min-bytes 1200 --min-headings 4 --min-new-ids 3 --min-topic-overlap 8 '
                 '--table-min-rows 5 --table-min-cols 3, base-lesson corpus/lessons/round-91.md equivalent fixture).')
    lines.append(f'Selftest of the frozen tool (run for the record): rc={st.returncode} last line: '
                 f'`{st_out[-1] if st_out else "none"}`')
    lines.append('Driver: attack_driver.py (this stage dir). Fixtures rebuilt under scratch and deleted at seat end.')
    lines.append('')
    CONTROLS = {'G0', 'C1c', 'A4b', 'A5a', 'A5c'}
    cf = [r for r in results if r['id'] not in CONTROLS]
    cf_ref = [r for r in cf if r['outcome'].startswith('refused')]
    cf_unnamed = [r for r in cf_ref if 'unnamed' in r['outcome']]
    lines.append(f'Totals: counterfeits {len(cf)}; SURVIVORS {len([r for r in cf if r["outcome"] == "SURVIVOR"])}; '
                 f'refused {len(cf_ref)} (unnamed {len(cf_unnamed)}); controls: '
                 + ', '.join(f'{r["id"]}={r["outcome"]}' for r in results if r['id'] in CONTROLS) + '.')
    lines.append('')
    lines.append('| id | expected | rc | outcome | verdict line |')
    lines.append('|---|---|---|---|---|')
    for r in results:
        lines.append(f'| {r["id"]} | {r["expect"]} | {r["rc"]} | {r["outcome"]} | `{r["verdict"]}` |')
    lines.append('')
    for r in results:
        lines.append(f'## {r["id"]} — {r["outcome"]}')
        lines.append('')
        lines.append(f'- Recipe: {r["recipe"]}')
        lines.append(f'- Command: `{r["cmd"]}`')
        lines.append(f'- rc: {r["rc"]}')
        lines.append(f'- Verdict line: `{r["verdict"]}`')
        lines.append(f'- Expected: {r["expect"]}')
        lines.append('- Leg output:')
        lines.append('```')
        lines.append(r['out'])
        lines.append('```')
        lines.append('')
    open(os.path.join(STAGE, 'attacks.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    summary = dict(survivors=[r['id'] for r in survivors], refused=[(r['id'], r['outcome']) for r in refused],
                   mismatch=[r['id'] for r in mismatch], total=len(results))
    print(json.dumps(summary, indent=1))
    for r in results:
        print(f'{r["id"]:6} rc={r["rc"]} exp={r["expect"]:20} -> {r["outcome"]}')


if __name__ == '__main__':
    main()
