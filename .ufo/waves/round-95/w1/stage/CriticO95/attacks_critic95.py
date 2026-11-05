#!/usr/bin/env python3
"""CriticO95 routed-findings attack driver (round 95).

Builds fresh counterfeit fixtures the frozen round-94/95 batteries do NOT carry
and grades them with the wave battery's own configure()/grade() invocation shape
(the battery module is imported read-only; battery95.py preferred, battery94.py
accepted as the equivalent). Fixtures live only under the seat scratch dir.

Env:
  CRIT_WORK      scratch dir (refused under /tmp)
  CRIT_BATTERY   battery driver path (battery95.py or battery94.py)
  CRIT_TOOL      grader under test
  CRIT_OUT_JSON  per-class results JSON written here

Output mirrors battery94.py's shape:
  TOOL sha256=... path=...
  CLASS <id> rc=<n> traceback=<yes|no> named=<leg-or-diagnostic|none> outcome=<SURVIVOR|REFUSED-NAMED|REFUSED-UNNAMED|TRACEBACK|CLEAN>
  BATTERY-SUMMARY survivors=<n> refused=<n> unnamed=<n> traceback=<n> clean=<n>
Exit 0 once the run completes (counts are data). Every special byte in the
recipes below is written as an explicit \\u escape; no invisible characters
sit in this source file.
"""
import hashlib
import importlib.util
import json
import os
import re
import sys

sys.dont_write_bytecode = True


def load(path, name):
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

B = load(battery_path, 'critic95battery')
for attr in ('configure', 'grade', 'standard', '_reps', 'mc', 'GAINED_TAIL'):
    assert hasattr(B, attr), f'battery lacks {attr}'

B.configure(tool, work)
TAIL = B.GAINED_TAIL

NBSP = ' '          # U+00A0
VTAB = '\x0b'       # U+000B
FF = '\x0c'         # U+000C
LSEP = '¨'          # U+2028 (written below via chr to stay ASCII-safe)
NEL = ''           # U+0085 (chr(133))
ESC = '\x1b'        # U+001B
RLE = '«'           # placeholder replaced below; real codepoints come from chr()
RLO = '»'           # placeholder replaced below
CYRA = 'α'          # placeholder replaced below
ZWNJ = ''          # placeholder replaced below
FW1 = '１'          # placeholder replaced below

# Real codepoints, built explicitly so the recipe bytes are unambiguous:
NBSP = chr(0x00A0)
VTAB = chr(0x0B)
FF = chr(0x0C)
LSEP = chr(0x2028)
NEL = chr(0x85)
ESC = chr(0x1B)
RLE = chr(0x202B)   # RTL marking (U+202B)
RLO = chr(0x202E)   # right-to-left override (U+202E)
CYRA = chr(0x0430)  # Cyrillic small a
ZWNJ = chr(0x200C)
FW = {c: chr(0xFF10 + int(c)) for c in '1234'}  # fullwidth digits １-４


def lesson_gain(token):
    """Gained S001 disposition line with `token` standing where LOCATED stands."""
    return lambda: B.standard('critic95/' + NAME[0], lesson_extra='- S001 ' + token + ' recheck moved' + TAIL)


def lesson_line(line):
    return lambda: B.standard('critic95/' + NAME[0], lesson_extra=line + TAIL)


def entry_variant(reps):
    def f():
        return B.standard('critic95/' + NAME[0], entry=B._reps(B.mc.body(None), reps))
    return f


# (id, class description, builder) — 15 fresh counterfeit classes plus G0 and the
# ZWNJ1 control. None overlaps the frozen battery classes or CriticO94's thirteen.
CASES = [
    ('G0', 'Clean control: unmodified mini-lane, set-B grade.', lambda: B.standard('critic95/G0')),
    ('NB1', 'NBSP U+00A0 inside the verdict token of a gained S001 line.',
     lesson_gain('LOCA' + NBSP + 'TED')),
    ('VT1', 'Vertical tab U+000B inside the verdict token (splitlines severs the line).',
     lesson_gain('LOCA' + VTAB + 'TED')),
    ('FF1', 'Form feed U+000C inside the verdict token (splitlines severs the line).',
     lesson_gain('LOCA' + FF + 'TED')),
    ('LS1', 'Line separator U+2028 inside the verdict token (splitlines severs the line).',
     lesson_gain('LOCA' + LSEP + 'TED')),
    ('NEL1', 'NEL U+0085 inside the verdict token (splitlines severs the line).',
     lesson_gain('LOCA' + NEL + 'TED')),
    ('ANSI1', 'ANSI CSI escape U+001B [31 m inside the verdict token.',
     lesson_gain('LOCA' + ESC + '[31mTED')),
    ('RTL1', 'RTL marking U+202B immediately before the id token of a gained S001 line.',
     lesson_line(RLE + 'S001 LOCATED recheck moved')),
    ('RTL2', 'RTL marking U+202B inside the id token of a gained line.',
     lesson_line('- S' + RLE + '001 LOCATED recheck moved')),
    ('RTL3', 'RLO U+202E inside the id token of a gained line.',
     lesson_line('- S' + RLO + '001 LOCATED recheck moved')),
    ('CYR1', 'Cyrillic small-a U+0430 in place of the id letter S of a gained line.',
     lesson_line('- ' + CYRA + '001 LOCATED recheck moved')),
    ('FW2', 'Fullwidth digit dot-form phrase heads (## <fw1>. address ...).',
     entry_variant([('## 1. The address', '## ' + FW['1'] + '. address'),
                    ('## 2. The petition', '## ' + FW['2'] + '. petition'),
                    ('## 3. Fixed and extempore', '## ' + FW['3'] + '. efficacy'),
                    ('## 4. Efficacy', '## ' + FW['4'] + '. table')])),
    ('FW3', 'Fullwidth digit dotless phrase heads (## <fw1> address ...).',
     entry_variant([('## 1. The address', '## ' + FW['1'] + ' address'),
                    ('## 2. The petition', '## ' + FW['2'] + ' petition'),
                    ('## 3. Fixed and extempore', '## ' + FW['3'] + ' efficacy'),
                    ('## 4. Efficacy', '## ' + FW['4'] + ' table')])),
    ('LR2', 'Lowercase roman dot-form phrase heads (## ii. address ...).',
     entry_variant([('## 1. The address', '## ii. address'),
                    ('## 2. The petition', '## iii. petition'),
                    ('## 3. Fixed and extempore', '## iv. efficacy'),
                    ('## 4. Efficacy', '## v. table')])),
    ('BR1', 'Bracketed-number phrase heads (## (1) address ...).',
     entry_variant([('## 1. The address', '## (1) address'),
                    ('## 2. The petition', '## (2) petition'),
                    ('## 3. Fixed and extempore', '## (3) efficacy'),
                    ('## 4. Efficacy', '## (4) table')])),
    ('DASH1', 'Separator-dash phrase heads (## - address ...): a bare dash token anchors.',
     entry_variant([('## 1. The address', '## - address'),
                    ('## 2. The petition', '## - petition'),
                    ('## 3. Fixed and extempore', '## - efficacy'),
                    ('## 4. Efficacy', '## - table')])),
    ('ZWNJ1', 'Control: ZWNJ U+200C inside a table-cell phrase (ZW strip set covers U+200C on the disposition path).',
     entry_variant([('| address | rote | improvised |', '| addr' + ZWNJ + 'ess | rote | improvised |')])),
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
    results = []
    for cid, desc, builder in CASES:
        NAME[0] = cid
        fx = builder()
        rc, out, _cmd = B.grade(fx)
        r = classify(rc, out)
        if cid == 'G0' and rc == 0:
            r['outcome'] = 'CLEAN'
        last = (out.strip().splitlines() or [''])[-1][:200]
        fails_detail = [l[:220] for l in out.splitlines() if 'FAIL' in l]
        results.append(dict(id=cid, desc=desc, rc=rc, traceback=r['traceback'],
                            outcome=r['outcome'], named=r['named'], last_line=last,
                            fails=fails_detail))
        print(f'CLASS {cid} rc={rc} traceback={"yes" if r["traceback"] else "no"} '
              f'named={",".join(r["named"]) if r["named"] else "none"} outcome={r["outcome"]}')
        print(f'  detail {cid}: last-line={last!r}')
    counts = {k: sum(1 for r in results if r['outcome'] == k)
              for k in ('SURVIVOR', 'REFUSED-NAMED', 'REFUSED-UNNAMED', 'TRACEBACK', 'CLEAN')}
    tb_total = sum(r['traceback'] for r in results)
    print(f'BATTERY-SUMMARY survivors={counts["SURVIVOR"]} refused={counts["REFUSED-NAMED"] + counts["REFUSED-UNNAMED"]} '
          f'unnamed={counts["REFUSED-UNNAMED"]} traceback={counts["TRACEBACK"]} clean={counts["CLEAN"]} '
          f'traceback-classes={tb_total}')
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(dict(tool=os.path.abspath(tool), tool_sha256=tool_sha, battery=battery_path,
                       results=results, counts=counts, traceback_classes=tb_total),
                  f, indent=1, ensure_ascii=False)
        f.write('\n')
    return 0


NAME = ['']
if __name__ == '__main__':
    sys.exit(main())
