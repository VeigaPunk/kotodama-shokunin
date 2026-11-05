#!/usr/bin/env python3
"""ReviewerO94 re-attack driver (read-only on the lane).

Rebuilds the round-93 counterfeit classes A1/B1/G1/H1/I1/J1 (+K1 lowercase
channel) exactly as battery93.py (frozen) builds them, and grades each with the
candidate tool at CAND (env), using battery93's frozen argument shape.
Usage: CAND=<tool.py> python3 reattack.py <scratch-work-dir>
Prints one line per class: id rc outcome first-FAIL-or-PASS-diagnostic.
"""
import hashlib, importlib.util, json, os, re, shlex, shutil, subprocess, sys

sys.dont_write_write = True
REPO = '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
TOOL = os.environ['CAND']
BUILDER = REPO + '/reports/round-92/controls/make-counterfeits.py'
B93 = REPO + '/reports/round-93/battery93.py'
SCRATCH = sys.argv[1]

# import battery93 for its ATTACKS/standard/grade machinery, re-pointed
os.environ['R93_ROOT'] = REPO
os.environ['R93_WORK'] = SCRATCH
spec = importlib.util.spec_from_file_location('b93', B93)
b93 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b93)
b93.TOOL = TOOL  # re-point the tool under test

WANT = {'G0', 'A1_chrome_forged_manifest', 'A5f_zwsp_verdict'}
results = []


def run_case(bid, builder):
    fx = builder()
    rc, out, cmd = b93.grade(fx)
    fails = re.findall(r'FAIL\s+([A-Z]+)', out)
    diag = re.findall(r'^ADVANCE-EVIDENCE_ERROR: (.*)$', out, re.M)
    tr = 'Traceback' in out
    results.append((bid, rc, 'TRACEBACK' if tr else ('LEGFAIL:' + ','.join(sorted(set(fails))) if fails else
                    ('NAMED:' + diag[0][:90] if diag else 'CLEAN-PASS')), out))
    shutil.rmtree(fx.root, ignore_errors=True)


# A1/B1: Cyrillic lookalike / soft hyphen inside a gained verdict token
CYR = {ord('O'): '\u041e'}  # in token: L + U+041E + CATED
def mk_a1(name, token):
    def f():
        extra = ('- S001 L\u041eCATED recheck moved \u2014 https://registry-example.org/base-old '
                 'accessed 2026-11-05: \u201canother old base row about dye plants\u201d\n') if token == 'a1' else \
                ('- S001 LOCA\u00adTED recheck moved \u2014 https://registry-example.org/base-old '
                 'accessed 2026-11-05: \u201canother old base row about dye plants\u201d\n')
        return b93.standard(name, lesson_extra=extra)
    return f

# G1: numbered phrase-only headings
def mk_g1():
    def f():
        e = b93._reps(b93.mc.body(None), [
            ('## 1. The address', '## 1. address'),
            ('## 2. The petition', '## 2. petition'),
            ('## 3. Fixed and extempore', '## 3. efficacy'),
            ('## 4. Efficacy', '## 4. table'),
            ('## 5. Table', '## 5. Rites')])
        return b93.standard('G1_numbered_phrase_headings', entry=e)
    return f

# H1: manifest row value is a list
def mk_h1():
    def f():
        rows = json.dumps({'rows': [{'S955': ['capture', 'url', 'quote']}]})
        return b93.standard('H1_manifest_row_value_list', manifest_override=rows)
    return f

# I1: lands registry new row shorter than eleven cells
def mk_i1():
    def f():
        fx = b93.standard('I1_short_new_row')
        rows = [b93.mc._row('S776', b93.BASE_URL, 'an old base row about prayer notes and rubrics'),
                b93.mc._row('S001', 'https://registry-example.org/base-old',
                            'another old base row about unrelated dye plants')]
        rows += [b93.mc._row(rid, b93.DEFAULT_URLS[rid], b93.TEACH) for rid in b93.IDS]
        short = b93.mc._row('S955', b93.DEFAULT_URLS['S955'], b93.TEACH)
        cells = [c.strip() for c in short.split('|')[1:-1]]
        rows[-3] = '| ' + ' | '.join(cells[:4]) + ' |'
        b93.put(fx.lands, b93.mc.HEADER + '\n' + '\n'.join(rows) + '\n')
        return fx
    return f

# J1: en-dash in NOT-LOCATED (wrong-direction parse)
def mk_j1():
    def f():
        extra = ('- S001 NOT\u2013LOCATED recheck unchanged \u2014 https://registry-example.org/base-old '
                 'accessed 2026-11-05: \u201canother old base row about dye plants\u201d\n')
        return b93.standard('J1_endash_not_located', lesson_extra=extra)
    return f

# K1: lowercase unanchored verdict token (narrow evasion channel from Mut pins)
def mk_k1():
    def f():
        extra = ('blah S001 located recheck 90d accessed 2026-11-05 — '
                 'https://registry-example.org/base-old\n')
        return b93.standard('K1_lowercase_unanchored', lesson_extra=extra)
    return f

CASES = [('A1', mk_a1('A1_cyrillic_token', 'a1')),
         ('B1', mk_a1('B1_softhyphen_token', 'b1')),
         ('G1', mk_g1()),
         ('H1', mk_h1()),
         ('I1', mk_i1()),
         ('J1', mk_j1()),
         ('K1', mk_k1()),
         ('G0', b93.b_g0)]
for bid, b in CASES:
    run_case(bid, b)

for bid, rc, outcome, out in results:
    verdict = out.splitlines()[-1] if out else 'no output'
    print(f'{bid:4} rc={rc} {outcome:48} verdict: {verdict[:110]}')
