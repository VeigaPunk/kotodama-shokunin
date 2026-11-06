#!/usr/bin/env python3
"""CriticO97 fresh-counterfeit attack driver (round 97).

Modeled on .ufo/waves/round-96/w1/stage/CriticO96/attacks_critic96.py (read-only source,
not modified). Environment contract is identical:
  CRIT_WORK      scratch dir (must not be under /tmp); all fixtures live here
  CRIT_BATTERY   battery97.py, imported read-only for configure/standard/grade/_reps/mc/GAINED_TAIL
  CRIT_TOOL      the grader under attack (v9 lane tool, or the v8 baseline export)
  CRIT_OUT_JSON  results JSON path (scratch)

Fresh classes (none carried by battery97 A1..F1/CD1..NUM2/NB1..ANSI1/CYR1/BR1/DASH1/ZWNJ1
or CR1/US1/OGH1/IS1/NUL1/CM1/CMW2, none carried by CriticO96's 19):
  verdict-token channel (gained S001 line, token stands where LOCATED stands):
    BEL1 U+0007, DEL1 U+007F, SUB1 U+001A  (Cc outside every v8/v9 blocklist)
    ENQ1 U+2000, ENSP1 U+2002, FIGSP1 U+2007, THINSP1 U+2009, HAIRSP1 U+200A,
    NNBP1 U+202F, MMSP1 U+205F             (Zs beyond U+1680/U+3000)
    ENC1 U+20DD (Me enclosing mark), VS16VT U+FE0F (Mn variation selector)
    FEFFVT1 U+FEFF inside the token (ZW-set benign control), BOM1 U+FEFF at line start,
    CMID1 combining acute inside the ID token
  heading channel (five h2 lines, CM1/CMW2 siblings with non-Mn bytes):
    ENCH1 U+20DD on the number, VSH1 U+FE0F on the number, ROMAN1 U+2160-2164 numerals,
    SUP1 superscript digits, FWNUMH1 fullwidth digits, FWPER1 fullwidth full stop,
    CYRH1 Cyrillic homoglyph word + clean twin, ZWSH1 ZWSP inside word + clean twin,
    BELH1 BEL inside word + clean twin, NELH1 NEL inside word (severing)
  controls: G0 clean lane; H-CRLF CRLF heading endings; H-CR lone-CR heading joins.
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

B = load(battery_path, 'critic97battery')
for attr in ('configure', 'grade', 'standard', '_reps', 'mc', 'GAINED_TAIL'):
    assert hasattr(B, attr), f'battery lacks {attr}'

B.configure(tool, work)
TAIL = B.GAINED_TAIL

# Real codepoints, built explicitly so the recipe bytes are unambiguous:
BEL = chr(0x0007)     # bell (Cc, not a splitlines boundary, on no v8 blocklist)
DEL = chr(0x007F)     # delete (Cc)
SUB = chr(0x001A)     # substitute (Cc, U+001B ESC is blocked but U+001A is not)
ENQ = chr(0x2000)     # en quad (Zs)
ENSP = chr(0x2002)    # en space (Zs)
FIGSP = chr(0x2007)   # figure space (Zs)
THINSP = chr(0x2009)  # thin space (Zs)
HAIRSP = chr(0x200A)  # hair space (Zs)
NNBP = chr(0x202F)    # narrow no-break space (Zs)
MMSP = chr(0x205F)    # medium mathematical space (Zs)
ENC = chr(0x20DD)     # combining enclosing circle (Me)
VS16 = chr(0xFE0F)    # variation selector-16 (Mn)
FEFF = chr(0xFEFF)    # BOM / zero-width no-break space (Cf, ZW strip-set member)
CM = chr(0x0301)      # combining acute accent (Mn)
ROMANS = ['\u2160', '\u2161', '\u2162', '\u2163', '\u2164']      # Ⅰ Ⅱ Ⅲ Ⅳ Ⅴ
SUPS = ['\u00b9', '\u00b2', '\u00b3', '\u2074', '\u2075']        # ¹ ² ³ ⁴ ⁵
FWDS = ['\uff11', '\uff12', '\uff13', '\uff14', '\uff15']        # １ ２ ３ ４ ５
FWPER = '\uff0e'                                                  # ．fullwidth full stop
CYRA = '\u0430'       # Cyrillic small a
CYRE = '\u0435'       # Cyrillic small e
CYRO = '\u043e'       # Cyrillic small o
ZWS = chr(0x200B)     # zero-width space (Cf, ZW strip-set member)
NEL = chr(0x0085)     # next line (Cc, splitlines severs)


def lesson_gain(token):
    """Gained S001 disposition line with `token` standing where LOCATED stands."""
    return lambda: B.standard('critic97/' + NAME[0], lesson_extra='- S001 ' + token + ' recheck moved' + TAIL)


def lesson_line(line):
    return lambda: B.standard('critic97/' + NAME[0], lesson_extra=line + TAIL)


def entry_variant(reps):
    def f():
        return B.standard('critic97/' + NAME[0], entry=B._reps(B.mc.body(None), reps))
    return f


def heads_with(prefixes):
    return entry_variant([
        ('## 1. The address', '## ' + prefixes[0] + ' address'),
        ('## 2. The petition', '## ' + prefixes[1] + ' petition'),
        ('## 3. Fixed and extempore', '## ' + prefixes[2] + ' efficacy'),
        ('## 4. Efficacy', '## ' + prefixes[3] + ' table'),
        ('## 5. Table', '## ' + prefixes[4] + ' Notes'),
    ])


def cyr_heads():
    """Mixed-script junk word + its clean twin on each of the five h2 lines."""
    return entry_variant([
        ('## 1. The address', '## ' + CYRA + 'ddress address'),
        ('## 2. The petition', '## p' + CYRE + 'tition petition'),
        ('## 3. Fixed and extempore', '## ' + CYRE + 'fficacy efficacy'),
        ('## 4. Efficacy', '## tabl' + CYRE + ' table'),
        ('## 5. Table', '## N' + CYRO + 'tes Notes'),
    ])


CASES = [
    # ---- controls ----
    ('G0', 'Clean control: unmodified mini-lane.', lambda: B.standard('critic97/G0')),
    # ---- verdict-token channel ----
    ('BEL1', 'Bell U+0007 inside the verdict token (Cc, no sever, on no v8 blocklist).',
     lesson_gain('LOCA' + BEL + 'TED')),
    ('DEL1', 'Delete U+007F inside the verdict token (Cc).',
     lesson_gain('LOCA' + DEL + 'TED')),
    ('SUB1', 'Substitute U+001A inside the verdict token (Cc; neighbour U+001B is blocked, U+001A is not).',
     lesson_gain('LOCA' + SUB + 'TED')),
    ('ENQ1', 'En quad U+2000 inside the verdict token (Zs, NFKC folds to plain space).',
     lesson_gain('LOCA' + ENQ + 'TED')),
    ('ENSP1', 'En space U+2002 inside the verdict token (Zs).',
     lesson_gain('LOCA' + ENSP + 'TED')),
    ('FIGSP1', 'Figure space U+2007 inside the verdict token (Zs).',
     lesson_gain('LOCA' + FIGSP + 'TED')),
    ('THINSP1', 'Thin space U+2009 inside the verdict token (Zs).',
     lesson_gain('LOCA' + THINSP + 'TED')),
    ('HAIRSP1', 'Hair space U+200A inside the verdict token (Zs).',
     lesson_gain('LOCA' + HAIRSP + 'TED')),
    ('NNBP1', 'Narrow no-break space U+202F inside the verdict token (Zs).',
     lesson_gain('LOCA' + NNBP + 'TED')),
    ('MMSP1', 'Medium mathematical space U+205F inside the verdict token (Zs).',
     lesson_gain('LOCA' + MMSP + 'TED')),
    ('ENC1', 'Combining enclosing circle U+20DD (Me, NOT Mn) inside the verdict token.',
     lesson_gain('LOCA' + ENC + 'TED')),
    ('VS16VT', 'Variation selector-16 U+FE0F (Mn) inside the verdict token.',
     lesson_gain('LOCA' + VS16 + 'TED')),
    ('FEFFVT1', 'BOM U+FEFF inside the verdict token (ZW strip-set member; benign-control expectation).',
     lesson_gain('LOCA' + FEFF + 'TED')),
    ('BOM1', 'BOM U+FEFF at line start of a gained S001 LOCATED line.',
     lesson_line(FEFF + '- S001 LOCATED recheck moved')),
    ('CMID1', 'Combining acute U+0301 inside the id token: `- S00' + CM + '1 LOCATED ...`.',
     lesson_line('- S00' + CM + '1 LOCATED recheck moved')),
    # ---- heading channel (CM1/CMW2 siblings with non-Mn bytes) ----
    ('ENCH1', 'Enclosing circle U+20DD (Me) on the numbering token: `## 1' + ENC + '. address` x5.',
     heads_with(['1' + ENC + '.', '2' + ENC + '.', '3' + ENC + '.', '4' + ENC + '.', '5' + ENC + '.'])),
    ('VSH1', 'Variation selector U+FE0F (Mn) on the numbering token: `## 1' + VS16 + '. address` x5.',
     heads_with(['1' + VS16 + '.', '2' + VS16 + '.', '3' + VS16 + '.', '4' + VS16 + '.', '5' + VS16 + '.'])),
    ('ROMAN1', 'Unicode roman numeral U+2160-2164 as the heading number: `## ' + ROMANS[0] + '. address` x5.',
     heads_with([r + '.' for r in ROMANS])),
    ('SUP1', 'Superscript digits U+00B9/U+00B2/U+00B3/U+2074/U+2075 as the heading number x5.',
     heads_with([s + '.' for s in SUPS])),
    ('FWNUMH1', 'Fullwidth digits U+FF11-FF15 as the heading number: `## ' + FWDS[0] + '. address` x5.',
     heads_with([f + '.' for f in FWDS])),
    ('FWPER1', 'Fullwidth full stop U+FF0E after the number: `## 1' + FWPER + ' address` x5.',
     heads_with(['1' + FWPER, '2' + FWPER, '3' + FWPER, '4' + FWPER, '5' + FWPER])),
    ('CYRH1', 'Mixed-script junk word + clean twin on each h2: `## ' + CYRA + 'ddress address` x5.',
     cyr_heads()),
    ('ZWSH1', 'Zero-width space U+200B inside the heading word + clean twin: `## add' + ZWS + 'ress address` x5.',
     heads_with(['add' + ZWS + 'ress', 'petition' + ZWS, 'efficac' + ZWS + 'y', 'tabl' + ZWS + 'e', 'No' + ZWS + 'tes'])),
    ('BELH1', 'Bell U+0007 inside the heading word + clean twin: `## 1. add' + BEL + 'ress address` x5.',
     heads_with(['1. add' + BEL + 'ress', '2. petition' + BEL, '3. efficac' + BEL + 'y', '4. tabl' + BEL + 'e', '5. No' + BEL + 'tes'])),
    ('NELH1', 'NEL U+0085 inside the heading word + clean twin (splitlines severs): `## 1. add' + NEL + 'ress address` x5.',
     heads_with(['1. add' + NEL + 'ress', '2. petition' + NEL, '3. efficac' + NEL + 'y', '4. tabl' + NEL + 'e', '5. No' + NEL + 'tes'])),
    # ---- line-ending controls ----
    ('H-CRLF', 'Control: the five original h2 lines terminated CRLF instead of LF.',
     entry_variant([
        ('## 1. The address', '## 1. The address\r'),
        ('## 2. The petition', '## 2. The petition\r'),
        ('## 3. Fixed and extempore', '## 3. Fixed and extempore\r'),
        ('## 4. Efficacy', '## 4. Efficacy\r'),
        ('## 5. Table', '## 5. Table\r')])),
    ('H-CR', 'Control: the five original h2 lines joined by lone CR instead of LF.',
     entry_variant([
        ('\n## 2. The petition', '\r## 2. The petition'),
        ('\n## 3. Fixed and extempore', '\r## 3. Fixed and extempore'),
        ('\n## 4. Efficacy', '\r## 4. Efficacy'),
        ('\n## 5. Table', '\r## 5. Table')])),
]

CONTROLS = {'G0', 'H-CRLF', 'H-CR'}

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
        if cid in CONTROLS and rc == 0:
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
    tally = (f'CRITIC-O97 survivors={counts["SURVIVOR"]} unnamed={counts["REFUSED-UNNAMED"]} '
             f'refused={counts["REFUSED-NAMED"] + counts["REFUSED-UNNAMED"]} traceback={counts["TRACEBACK"]}')
    print(tally)
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(dict(tool=os.path.abspath(tool), tool_sha256=tool_sha, battery=battery_path,
                       results=results, counts=counts, traceback_classes=tb_total, tally=tally),
                  f, indent=1, ensure_ascii=False)
        f.write('\n')
    tpath = os.path.join(work, 'transcript-critic97.txt')
    with open(tpath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(transcript) + '\n')
    with open(os.path.join(work, 'tally.txt'), 'w', encoding='utf-8') as f:
        f.write(tally + '\n')
    return 0


NAME = ['']
if __name__ == '__main__':
    sys.exit(main())
