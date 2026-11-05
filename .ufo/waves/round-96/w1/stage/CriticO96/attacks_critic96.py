#!/usr/bin/env python3
"""CriticO96 fresh-counterfeit attack driver (round 96).

Attacks the v7 grader in place with classes battery96 does not carry:
  lesson channel (forged gained S001 verdict on an old id):
    FS1/GS1/RS1  U+001C/U+001D/U+001E inside the verdict token
    PS1          U+2029 paragraph separator inside the verdict token
    CR1          lone CR U+000D inside the verdict token (CR-only severing)
    US1          U+001F unit separator inside the verdict token (non-severing)
    OGH1         U+1680 OGHAM SPACE MARK inside the verdict token (no NFKC fold)
    IS1          U+3000 ideographic space inside the verdict token (NFKC->space)
    ZWJ1         U+200D zero-width joiner inside the verdict token (strip-set member)
    MVS1         U+180E Mongolian vowel separator (Cf outside the strip set)
    ALM1         U+061C Arabic letter mark (Cf outside the strip set)
    FWID1        fullwidth digits in the id token (S００１)
    FWS1         fullwidth id letter (Ｓ001)
    NUL1         U+0000 inside the verdict token (non-severing Cc)
  heading channel (forged phrase-bearing h2 surfaces):
    CM1          combining acute on the numbering token (## 1<U+0301>. address)
    CMW2         combining acute inside a heading phrase word
    TABH1        tab between number and phrase word
    VTH1         vertical tab between number and phrase word
    ISPH1        ideographic space between number and phrase word
Controls: G0 (clean mini-lane), ZWNJ1 (battery's own benign control builder).

Fixture machinery is battery96's own (B.standard/B.grade/B._reps/B.mc), driven
read-only; all fixtures live under CRIT_WORK. CRIT_TOOL must be the v7 grader.
"""
import json
import hashlib
import os
import re
import sys

sys.dont_write_bytecode = True


def load(path, name):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


work = os.environ['CRIT_WORK']
battery_path = os.environ['CRIT_BATTERY']
tool = os.environ['CRIT_TOOL']
out_json = os.environ['CRIT_OUT_JSON']

assert not (work == '/tmp' or work.startswith('/tmp/')), 'work must not be under /tmp'
assert os.path.isfile(tool), tool
assert os.path.isfile(battery_path), battery_path

B = load(battery_path, 'critic96battery')
for attr in ('configure', 'grade', 'standard', '_reps', 'mc', 'GAINED_TAIL'):
    assert hasattr(B, attr), f'battery lacks {attr}'

B.configure(tool, work)
TAIL = B.GAINED_TAIL

# Real codepoints, built explicitly so the recipe bytes are unambiguous:
FS = chr(0x001C)    # information separator four (file)
GS = chr(0x001D)    # information separator three (group)
RS = chr(0x001E)    # information separator two (record)
US = chr(0x001F)    # information separator one (unit)
PS = chr(0x2029)    # paragraph separator
CR = chr(0x000D)    # carriage return
OGH = chr(0x1680)   # ogham space mark
ISPACE = chr(0x3000)  # ideographic space
ZWJ = chr(0x200D)   # zero-width joiner
MVS = chr(0x180E)   # mongolian vowel separator (Cf)
ALM = chr(0x061C)   # arabic letter mark (Cf)
NUL = chr(0x0000)   # nul
FWD = {c: chr(0xFF10 + int(c)) for c in '0123456789'}  # fullwidth digits
FWS = chr(0xFF33)   # fullwidth capital S
CM = chr(0x0301)    # combining acute accent


def lesson_gain(token):
    """Gained S001 disposition line with `token` standing where LOCATED stands."""
    return lambda: B.standard('critic96/' + NAME[0], lesson_extra='- S001 ' + token + ' recheck moved' + TAIL)


def lesson_line(line):
    return lambda: B.standard('critic96/' + NAME[0], lesson_extra=line + TAIL)


def entry_variant(reps):
    def f():
        return B.standard('critic96/' + NAME[0], entry=B._reps(B.mc.body(None), reps))
    return f


def heads_with(prefixes):
    return entry_variant([
        ('## 1. The address', '## ' + prefixes[0] + ' address'),
        ('## 2. The petition', '## ' + prefixes[1] + ' petition'),
        ('## 3. Fixed and extempore', '## ' + prefixes[2] + ' efficacy'),
        ('## 4. Efficacy', '## ' + prefixes[3] + ' table'),
        ('## 5. Table', '## ' + prefixes[4] + ' Notes'),
    ])


CASES = [
    ('G0', 'Clean control: unmodified mini-lane.', lambda: B.standard('critic96/G0')),
    ('FS1', 'Information separator U+001C inside the verdict token of a gained S001 line.',
     lesson_gain('LOCA' + FS + 'TED')),
    ('GS1', 'Information separator U+001D inside the verdict token.',
     lesson_gain('LOCA' + GS + 'TED')),
    ('RS1', 'Information separator U+001E inside the verdict token.',
     lesson_gain('LOCA' + RS + 'TED')),
    ('PS1', 'Paragraph separator U+2029 inside the verdict token.',
     lesson_gain('LOCA' + PS + 'TED')),
    ('CR1', 'Lone carriage return U+000D inside the verdict token (CR-only severing).',
     lesson_gain('LOCA' + CR + 'TED')),
    ('US1', 'Unit separator U+001F inside the verdict token (splitlines does NOT sever).',
     lesson_gain('LOCA' + US + 'TED')),
    ('OGH1', 'Ogham space mark U+1680 inside the verdict token (Zs, no NFKC fold, no sever).',
     lesson_gain('LOCA' + OGH + 'TED')),
    ('IS1', 'Ideographic space U+3000 inside the verdict token (NFKC folds to plain space).',
     lesson_gain('LOCA' + ISPACE + 'TED')),
    ('ZWJ1', 'Zero-width joiner U+200D inside the verdict token (ZW strip-set member).',
     lesson_gain('LOCA' + ZWJ + 'TED')),
    ('MVS1', 'Mongolian vowel separator U+180E (Cf outside the strip set) inside the verdict token.',
     lesson_gain('LOCA' + MVS + 'TED')),
    ('ALM1', 'Arabic letter mark U+061C (Cf outside the strip set) inside the verdict token.',
     lesson_gain('LOCA' + ALM + 'TED')),
    ('FWID1', 'Fullwidth digits in the id token: `- S' + FWD['0'] + FWD['0'] + FWD['1'] + ' LOCATED ...`.',
     lesson_line('- S' + FWD['0'] + FWD['0'] + FWD['1'] + ' LOCATED recheck moved')),
    ('FWS1', 'Fullwidth id letter: `- ' + FWS + '001 LOCATED ...`.',
     lesson_line('- ' + FWS + '001 LOCATED recheck moved')),
    ('NUL1', 'NUL U+0000 inside the verdict token (Cc, splitlines does NOT sever).',
     lesson_gain('LOCA' + NUL + 'TED')),
    ('CM1', 'Combining acute on the numbering token: `## 1' + CM + '. address` x5 (defeats the number-strip).',
     heads_with(['1' + CM + '.', '2' + CM + '.', '3' + CM + '.', '4' + CM + '.', '5' + CM + '.'])),
    ('CMW2', 'Combining acute inside a heading phrase word: `## addre' + CM + 'ss` style x5.',
     heads_with(['addre' + CM + 'ss', 'petition' + CM, 'efficac' + CM + 'y', 'tabl' + CM + 'e', 'Notes'])),
    ('TABH1', 'Tab between the number and the phrase word: `## 1.\taddress` x5.',
     heads_with(['1.\t', '2.\t', '3.\t', '4.\t', '5.\t'])),
    ('VTH1', 'Vertical tab between the number and the phrase word: `## 1.' + chr(0x0B) + 'address` x5.',
     heads_with(['1.' + chr(0x0B), '2.' + chr(0x0B), '3.' + chr(0x0B), '4.' + chr(0x0B), '5.' + chr(0x0B)])),
    ('ISPH1', 'Ideographic space between the number and the phrase word: `## 1.' + ISPACE + 'address` x5.',
     heads_with(['1.' + ISPACE, '2.' + ISPACE, '3.' + ISPACE, '4.' + ISPACE, '5.' + ISPACE])),
    ('ZWNJ1', 'Control: battery96 ZWNJ1 benign control builder, expected rc 0.',
     lambda: B.b96_zwnj1()),
]

DIAG_RE = re.compile(r'\(([A-Z][A-Z0-9-]{3,})\)')
FAIL_RE = re.compile(r'FAIL\s+([A-Z]+)')


def classify(rc, out):
    tb = out.count('Traceback')
    named = sorted(set(FAIL_RE.findall(out)) | set(DIAG_RE.findall(out)))
    if rc == 0:
        return dict(rc=rc, traceback=tb, outcome='SURVIVOR', named=None)
    if tb:
        return dict(rc=rc, traceback=tb, outcome='TRACEBACK', named=named or None)
    if named:
        return dict(rc=rc, traceback=tb, outcome='REFUSED-NAMED', named=named)
    return dict(rc=rc, traceback=tb, outcome='REFUSED-UNNAMED', named=None)


def main():
    tool_sha = hashlib.sha256(open(tool, 'rb').read()).hexdigest()
    print(f'TOOL sha256={tool_sha} path={os.path.abspath(tool)}')
    print(f'BATTERY sha256={hashlib.sha256(open(battery_path, "rb").read()).hexdigest()} path={os.path.abspath(battery_path)}')
    results = []
    transcript = []
    for cid, desc, builder in CASES:
        NAME[0] = cid
        fx = builder()
        rc, out, cmd = B.grade(fx)
        r = classify(rc, out)
        if cid == 'G0' and rc == 0:
            r['outcome'] = 'CLEAN'
        if cid == 'ZWNJ1' and rc == 0:
            r['outcome'] = 'CLEAN'
        last = (out.strip().splitlines() or [''])[-1][:200]
        fails_detail = [l[:240] for l in out.splitlines() if 'FAIL' in l]
        results.append(dict(id=cid, desc=desc, rc=rc, traceback=r['traceback'],
                            outcome=r['outcome'], named=r['named'], last_line=last,
                            fails=fails_detail, cmd=cmd))
        transcript.append(f'CLASS {cid} rc={rc} outcome={r["outcome"]} named={",".join(r["named"]) if r["named"] else "none"}')
        transcript.append(f'  recipe: {desc}')
        for f in fails_detail:
            transcript.append(f'  FAIL {f}')
        print(f'CLASS {cid} rc={rc} traceback={"yes" if r["traceback"] else "no"} '
              f'named={",".join(r["named"]) if r["named"] else "none"} outcome={r["outcome"]}')
        print(f'  detail {cid}: last-line={last!r}')
    counts = {k: sum(1 for r in results if r['outcome'] == k)
              for k in ('SURVIVOR', 'REFUSED-NAMED', 'REFUSED-UNNAMED', 'TRACEBACK', 'CLEAN')}
    tb_total = sum(r['traceback'] for r in results)
    tally = (f'CRITIC-O96 survivors={counts["SURVIVOR"]} unnamed={counts["REFUSED-UNNAMED"]} '
             f'refused={counts["REFUSED-NAMED"] + counts["REFUSED-UNNAMED"]} traceback={counts["TRACEBACK"]}')
    print(tally)
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(dict(tool=os.path.abspath(tool), tool_sha256=tool_sha, battery=battery_path,
                       results=results, counts=counts, traceback_classes=tb_total, tally=tally),
                  f, indent=1, ensure_ascii=False)
        f.write('\n')
    tpath = os.path.join(work, 'transcript-critic96.txt')
    with open(tpath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(transcript) + '\n')
    with open(os.path.join(work, 'tally.txt'), 'w', encoding='utf-8') as f:
        f.write(tally + '\n')
    return 0


NAME = ['']
if __name__ == '__main__':
    sys.exit(main())
