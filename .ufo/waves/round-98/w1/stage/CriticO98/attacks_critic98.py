#!/usr/bin/env python3
"""CriticO98 fresh-counterfeit attack driver (round 98).

Adversarial classes battery98 does NOT carry, in the same two channels the
battery covers: (a) forged verdict tokens on a gained S001 disposition line
(`_dispo97` byte-for-byte), (b) phrase-only h2 headings with exotic numbering
tokens (`_heads97` byte-for-byte), plus benign over-refusal sentinels and a
plain forged-verdict positive control proving refusals are real.

Loads battery98 read-only via importlib (fixtures land under CRIT_WORK, in the
seat scratch, never /tmp). Env: CRIT_TOOL, CRIT_BATTERY, CRIT_WORK,
CRIT_OUT_JSON. Prints `CRITIC-O98 survivors=<s> unnamed=<u> refused=<r>
traceback=<t>` over the attack classes; controls and over-refusal sentinels
are reported separately and never inflate the tally.
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

B = load(battery_path, 'critic98battery')
for attr in ('configure', 'grade', 'standard', '_reps', '_dispo97', '_heads97', 'mc', 'GAINED_TAIL'):
    assert hasattr(B, attr), f'battery lacks {attr}'

B.configure(tool, work)
TAIL = B.GAINED_TAIL
CM = chr(0x0301)          # combining acute (Mn), the battery's own probe byte

# ---- verdict-channel bytes (all fresh vs battery98) ------------------------
C81 = chr(0x0081)         # C1 control (Cc, no name, no sever)
C9C = chr(0x009C)         # C1 STRING TERMINATOR (Cc)
C9F = chr(0x009F)         # C1 APPLICATION COMMAND (Cc)
MC1 = chr(0x0903)         # Devanagari sign visarga (Mc, spacing combining mark)
MC2 = chr(0x0B03)         # Oriya sign visarga (Mc)
ME_SQ = chr(0x20DE)       # combining enclosing square (Me)
ME_ML = chr(0x0488)       # combining Cyrillic millions sign (Me)
ME_BS = chr(0x20E0)       # combining enclosing circle backslash (Me)
WJ = chr(0x2060)          # word joiner (Cf)
MVS = chr(0x180E)         # Mongolian vowel separator (Cf)
ZWJ = chr(0x200D)         # zero-width joiner (Cf)
CGJ = chr(0x034F)         # combining grapheme joiner (Mn)
FWL = chr(0xFF2C)         # fullwidth capital L (NFKC folds to L)
MATHL = chr(0x1D40C)      # mathematical bold capital L (NFKC folds to L)

# ---- heading-number tokens (all fresh vs battery98) ------------------------
CIRC = [chr(c) for c in range(0x2460, 0x2465)]              # circled digit one..five
SROM = [chr(c) for c in range(0x2170, 0x2175)]              # small roman i..v
ARAB = [chr(c) for c in range(0x0661, 0x0666)]              # arabic-indic one..five
DEVA = [chr(c) for c in range(0x0967, 0x0972)]              # devanagari one..five
FRAC = [chr(0x00BD), chr(0x2153), chr(0x00BC), chr(0x2155), chr(0x215B)]  # vulgar fractions
MATHD = [chr(c) for c in range(0x1D7CF, 0x1D7D4)]           # mathematical bold digits 1..5
SUPS = [chr(0x00B9), chr(0x00B2), chr(0x00B3), chr(0x2074), chr(0x2075)]
FWDS = [chr(c) for c in range(0xFF11, 0xFF16)]              # fullwidth digits
FWPER = chr(0xFF0E)
STOPS = [('IDEOSTOP', chr(0x3002)), ('HWSTOP', chr(0xFF61)),
         ('DOTLEAD', chr(0x2024)), ('SMALLSTOP', chr(0xFE52))]


def gain(token):
    """Gained S001 disposition line, `token` where LOCATED stands (_dispo97)."""
    return lambda: B._dispo97(token, 'critic98/' + NAME[0])


def heads(prefixes):
    """Five phrase-only h2 heads with `prefixes` before the phrase (_heads97)."""
    return lambda: B._heads97('critic98/' + NAME[0], prefixes)


def entry_variant(reps):
    def f():
        return B.standard('critic98/' + NAME[0], entry=B._reps(B.mc.body(None), reps))
    return f


def ok_heads(prefixes):
    """Benign twin: exotic numbering token, heading words KEPT (ROMANOK pattern)."""
    return entry_variant([
        ('## 1. The address', '## ' + prefixes[0] + ' The address'),
        ('## 2. The petition', '## ' + prefixes[1] + ' The petition'),
        ('## 3. Fixed and extempore', '## ' + prefixes[2] + ' Fixed and extempore'),
        ('## 4. Efficacy', '## ' + prefixes[3] + ' Efficacy'),
        ('## 5. Table', '## ' + prefixes[4] + ' Table'),
    ])


def word_reps(infix):
    """Exotic mark inside a heading word + clean twin on each h2 (ZWSH1 pattern)."""
    return [('## 1. The address', '## addre' + infix + 'ss address'),
            ('## 2. The petition', '## petition' + infix + ' petition'),
            ('## 3. Fixed and extempore', '## efficac' + infix + 'y efficacy'),
            ('## 4. Efficacy', '## tabl' + infix + 'e table'),
            ('## 5. Table', '## No' + infix + 'tes Notes')]


CASES = [
    # ---- positive control: plain forged verdict must be REFUSED ----
    ('PLAINMOVE', 'control-refuse',
     'Plain forged verdict: `- S001 LOCATED recheck moved` gained line, no exotic bytes; '
     'a grader that leaves this standing is dead, not gamed.'),
    # ---- over-refusal sentinels: benign, expected rc 0 CLEAN ----
    ('G0B', 'control-clean',
     'Clean control: unmodified mini-lane re-graded (fixture sanity).'),
    ('OK-CIRC', 'control-clean',
     'Benign: circled-digit numbering with heading words kept (`## \u2460. The address` x5).'),
    ('OK-MCWORD', 'control-clean',
     'Benign: Mc mark U+0903 inside a heading word + clean twin on each h2 (ZWSH1 pattern with Mc).'),
    # ---- verdict-token channel ----
    ('V-C81', 'attack', f'C1 control U+0081 (Cc, unnamed) inside LOCATED: LOCA<U+0081>TED.'),
    ('V-C9C', 'attack', f'C1 control U+009C STRING TERMINATOR inside LOCATED.'),
    ('V-C9F', 'attack', f'C1 control U+009F APPLICATION COMMAND inside LOCATED.'),
    ('V-MC0903', 'attack', f'Spacing combining mark U+0903 (Mc, Devanagari visarga) inside LOCATED.'),
    ('V-MC0B03', 'attack', f'Spacing combining mark U+0B03 (Mc, Oriya visarga) inside LOCATED.'),
    ('V-ME20DE', 'attack', f'Me mark U+20DE (combining enclosing square) inside LOCATED.'),
    ('V-ME0488', 'attack', f'Me mark U+0488 (combining Cyrillic millions sign) inside LOCATED.'),
    ('V-ME20E0', 'attack', f'Me mark U+20E0 (enclosing circle backslash) inside LOCATED.'),
    ('V-WJ2060', 'attack', f'Verdict token split by word joiner U+2060 (Cf): LOCA<U+2060>TED.'),
    ('V-MVS180E', 'attack', f'Verdict token split by Mongolian vowel separator U+180E (Cf).'),
    ('V-ZWJ200D', 'attack', f'Verdict token split by zero-width joiner U+200D (Cf).'),
    ('V-CGF034F', 'attack', f'Combining grapheme joiner U+034F (Mn) inside LOCATED.'),
    ('V-FWLFF2C', 'attack', f'First letter is fullwidth L U+FF2C: <U+FF2C>OCATED (NFKC letter lookalike).'),
    ('V-MATHL1D40C', 'attack', f'First letter is mathematical bold L U+1D40C: <U+1D40C>OCATED.'),
    # ---- heading-number channel (phrase-only heads) ----
    ('H-CIRC', 'attack', f'Circled digits U+2460-2464 + ASCII dot as the numbering token.'),
    ('H-CIRC-NODOT', 'attack', f'Circled digits U+2460-2464 alone, no dot, as the numbering token.'),
    ('H-SROMAN', 'attack', f'Small roman numerals U+2170-2174 + dot as the numbering token.'),
    ('H-ARABIC', 'attack', f'Arabic-Indic digits U+0661-0665 + dot as the numbering token.'),
    ('H-DEVANAGARI', 'attack', f'Devanagari digits U+0967-0971 + dot as the numbering token.'),
    ('H-FRACTION', 'attack', f'Vulgar fractions \u00bd \u2153 \u00bc \u2155 \u215b + dot as the numbering token.'),
    ('H-MATHBOLD', 'attack', f'Mathematical bold digits U+1D7CF-1D7D3 + dot as the numbering token.'),
    ('H-SUP-NODOT', 'attack', f'Superscript digits U+00B9 U+00B2 U+00B3 U+2074 U+2075 alone, no dot.'),
    ('H-FWFW', 'attack', f'Fullwidth digits U+FF11-FF15 + fullwidth stop U+FF0E (both halves exotic).'),
    ('H-IDEOSTOP', 'attack', f'ASCII digit + ideographic full stop U+3002 as the numbering token.'),
    ('H-HWSTOP', 'attack', f'ASCII digit + halfwidth ideographic full stop U+FF61 as the numbering token.'),
    ('H-DOTLEAD', 'attack', f'ASCII digit + one dot leader U+2024 as the numbering token.'),
    ('H-SMALLSTOP', 'attack', f'ASCII digit + small full stop U+FE52 as the numbering token.'),
    ('H-DOTCM', 'attack', f'ASCII digit + dot + lone combining acute U+0301 (mark AFTER the dot).'),
    ('H-MC0903NUM', 'attack', f'ASCII digit + Mc mark U+0903 + dot as the numbering token.'),
    ('H-ME20DENUM', 'attack', f'ASCII digit + Me mark U+20DE + dot as the numbering token.'),
    ('H-ME0488NUM', 'attack', f'ASCII digit + Me mark U+0488 + dot as the numbering token.'),
]


def builders():
    out = {}
    out['PLAINMOVE'] = gain('LOCATED')
    out['G0B'] = lambda: B.standard('critic98/G0B')
    out['OK-CIRC'] = ok_heads([c + '.' for c in CIRC])
    out['OK-MCWORD'] = entry_variant(word_reps(MC1))
    for cid in ('V-C81',): out[cid] = gain('LOCA' + C81 + 'TED')
    out['V-C9C'] = gain('LOCA' + C9C + 'TED')
    out['V-C9F'] = gain('LOCA' + C9F + 'TED')
    out['V-MC0903'] = gain('LOCA' + MC1 + 'TED')
    out['V-MC0B03'] = gain('LOCA' + MC2 + 'TED')
    out['V-ME20DE'] = gain('LOCA' + ME_SQ + 'TED')
    out['V-ME0488'] = gain('LOCA' + ME_ML + 'TED')
    out['V-ME20E0'] = gain('LOCA' + ME_BS + 'TED')
    out['V-WJ2060'] = gain('LOCA' + WJ + 'TED')
    out['V-MVS180E'] = gain('LOCA' + MVS + 'TED')
    out['V-ZWJ200D'] = gain('LOCA' + ZWJ + 'TED')
    out['V-CGF034F'] = gain('LOCA' + CGJ + 'TED')
    out['V-FWLFF2C'] = gain(FWL + 'OCATED')
    out['V-MATHL1D40C'] = gain(MATHL + 'OCATED')
    out['H-CIRC'] = heads([c + '.' for c in CIRC])
    out['H-CIRC-NODOT'] = heads(CIRC)
    out['H-SROMAN'] = heads([c + '.' for c in SROM])
    out['H-ARABIC'] = heads([c + '.' for c in ARAB])
    out['H-DEVANAGARI'] = heads([c + '.' for c in DEVA])
    out['H-FRACTION'] = heads([c + '.' for c in FRAC])
    out['H-MATHBOLD'] = heads([c + '.' for c in MATHD])
    out['H-SUP-NODOT'] = heads(SUPS)
    out['H-FWFW'] = heads([d + FWPER for d in FWDS])
    for tag, stop in STOPS:
        out['H-' + tag] = heads([str(i + 1) + stop for i in range(5)])
    out['H-DOTCM'] = heads([str(i + 1) + '.' + CM for i in range(5)])
    out['H-MC0903NUM'] = heads([str(i + 1) + MC1 + '.' for i in range(5)])
    out['H-ME20DENUM'] = heads([str(i + 1) + ME_SQ + '.' for i in range(5)])
    out['H-ME0488NUM'] = heads([str(i + 1) + ME_ML + '.' for i in range(5)])
    return out


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
    print(f'BATTERY sha256={hashlib.sha256(open(battery_path, "rb").read()).hexdigest()} '
          f'path={os.path.abspath(battery_path)}')
    bld = builders()
    results = []
    transcript = []
    for cid, kind, desc in CASES:
        NAME[0] = cid
        fx = bld[cid]()
        rc, out, cmd = B.grade(fx)
        r = classify(rc, out)
        if kind == 'control-clean':
            r['outcome'] = 'CLEAN' if (rc == 0 and not r['traceback']) else 'OVERREFUSAL'
        elif kind == 'control-refuse':
            if rc == 0 and not r['traceback']:
                r['outcome'] = 'HARNESS-DEAD'
            elif r['traceback']:
                r['outcome'] = 'TRACEBACK'
            else:
                r['outcome'] = 'REFUSED-CONTROL'
        last = (out.strip().splitlines() or [''])[-1][:200]
        fails_detail = [l[:240] for l in out.splitlines() if 'FAIL' in l]
        results.append(dict(id=cid, kind=kind, desc=desc, rc=rc, traceback=r['traceback'],
                            outcome=r['outcome'], named=r['named'], last_line=last,
                            fails=fails_detail, cmd=cmd))
        transcript.append(f'CLASS {cid} kind={kind} rc={rc} outcome={r["outcome"]} '
                          f'named={",".join(r["named"]) if r["named"] else "none"}')
        transcript.append(f'  recipe: {desc}')
        for f in fails_detail:
            transcript.append(f'  FAIL {f}')
        print(f'CLASS {cid} kind={kind} rc={rc} traceback={"yes" if r["traceback"] else "no"} '
              f'named={",".join(r["named"]) if r["named"] else "none"} outcome={r["outcome"]}')
        print(f'  detail {cid}: last-line={last!r}')
    attacks = [r for r in results if r['kind'] == 'attack']
    counts = {k: sum(1 for r in attacks if r['outcome'] == k)
              for k in ('SURVIVOR', 'REFUSED-NAMED', 'REFUSED-UNNAMED', 'TRACEBACK')}
    tally = (f'CRITIC-O98 survivors={counts["SURVIVOR"]} unnamed={counts["REFUSED-UNNAMED"]} '
             f'refused={counts["REFUSED-NAMED"] + counts["REFUSED-UNNAMED"]} '
             f'traceback={counts["TRACEBACK"]}')
    print(tally)
    overref = [r['id'] for r in results if r['outcome'] == 'OVERREFUSAL']
    print(f'OVERREFUSAL n={len(overref)} ids={",".join(overref) or "none"}')
    print(f'OVERREFUSAL-INFO benign-sentinels=3 (G0B, OK-CIRC, OK-MCWORD); '
          f'plainmove-refused={"yes" if any(r["outcome"] == "REFUSED-CONTROL" for r in results) else "NO"}')
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(dict(tool=os.path.abspath(tool), tool_sha256=tool_sha, battery=battery_path,
                       results=results, counts=counts, tally=tally,
                       overrefusal=overref), f, indent=1, ensure_ascii=False)
        f.write('\n')
    with open(os.path.join(work, 'transcript-critic98.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(transcript) + '\n')
    with open(os.path.join(work, 'tally.txt'), 'w', encoding='utf-8') as f:
        f.write(tally + '\n')
    return 0


NAME = ['']
if __name__ == '__main__':
    sys.exit(main())
