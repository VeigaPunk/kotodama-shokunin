#!/usr/bin/env python3
"""CriticO98b fresh-counterfeit attack driver (round 98, w2).

Extends the w1 draft (.ufo/waves/round-98/w1/stage/CriticO98/attacks_critic98.py,
read-only source) with classes battery98 does NOT carry, in the two channels the
battery covers: (a) forged verdict tokens on a gained S001 disposition line
(`_dispo97` byte-for-byte), (b) phrase-only h2 headings with exotic numbering
tokens (`_heads97` byte-for-byte), plus benign over-refusal sentinels and a
plain forged-verdict positive control proving refusals are real.

Fresh vs battery98 (and vs the w1 draft, which is superseded here):
  verdict channel, bytes the v10 window loop does not name and the NFKD/NFKC
  recoveries cannot fold:
    V-PO-MIDDOT U+00B7, V-PO-BULLET U+2022, V-PO-DOTLEAD U+2024 (Po)
    V-SO-COPY U+00A9, V-SO-REG U+00AE (So)
    V-SK-CIRC U+02C6 (Sk), V-LM-SUPH U+02B0 (Lm)
    V-CO-PUA U+E000 (Co), V-CN-UNASSIGNED U+0378 (Cn)
    V-LU-OSTROKE U+00D8, V-LU-LSTROKE U+0141, V-LU-ETH U+00D0 (Lu, no
      canonical/compatibility decomposition, absent from HOMOGLYPH_MAP)
    V-TAB-MID `LOC<TAB>ATED` (tab at a split position the VERDICT-TAB regex
      `LO\\s+CATED|NOT\\s+LOCATED` does not cover)
    V-SPACE-MID `LOCA TED` (plain space inside the token)
    V-MATHL U+1D40B (mathematical bold capital L, NFKC/NFKD fold to L)
  heading channel, list marks that are not non-ASCII numerals (so the v10
  HEADING-NUMBER predicate cannot fire) and are not stripped by `_NUM2`:
    H-LETTER A. B. E. F. G. (ASCII letter list marks; C./D./M. are roman and
      stripped, so the five keep non-roman letters)
    H-COLON 1: 2: 3: 4: 5:
    H-BULLET U+2022 (Po), H-SECTION U+00A7 (Po)
    H-NUMERO U+2116+digit, H-DEGNUM N+U+00B0+digit (So sign, ASCII digit)
    H-PARENLETTER (a)..(e), H-TRIPLENUM 1.1.1..5.1.1 (`_NUM2` handles only
      two-level nesting), H-CIRCLEDLETTER U+24B6-24BA (So), H-HASH #1..#5
  controls:
    PLAINMOVE plain forged verdict, must be REFUSED (harness liveness)
    G0B clean lane, must be CLEAN
    OK-CIRC circled-digit numbering with the heading words kept, must be CLEAN
    OK-LETTER letter list marks with the heading words kept, must be CLEAN
    OK-NUMERO numero-sign numbering with the heading words kept, must be CLEAN
    OK-MCWORD Mc mark inside a heading word plus the clean twin word, benign
      sentinel: v10 refuses it (over-refusal finding, not a survivor)
    OK-DEVAHEAD a legitimate Devanagari term (Mc marks) appended to a normal h2
      heading whose English phrase words are kept; benign, v10 refuses it

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

# ---- fresh verdict-channel bytes (none carried by battery98) --------------
PO_MIDDOT = chr(0x00B7)   # middle dot (Po)
PO_BULLET = chr(0x2022)   # bullet (Po)
PO_DOTLEAD = chr(0x2024)  # one dot leader (Po)
SO_COPY = chr(0x00A9)     # copyright sign (So)
SO_REG = chr(0x00AE)      # registered sign (So)
SK_CIRC = chr(0x02C6)     # modifier letter circumflex accent (Sk)
LM_SUPH = chr(0x02B0)     # modifier letter small h (Lm)
CO_PUA = chr(0xE000)      # private use (Co)
CN_UNASSIGNED = chr(0x0378)  # unassigned (Cn)
LU_OSTROKE = chr(0x00D8)  # O with stroke (Lu, no decomposition)
LU_LSTROKE = chr(0x0141)  # L with stroke (Lu, no decomposition)
LU_ETH = chr(0x00D0)      # Eth (Lu, no decomposition)
MATH_L = chr(0x1D40B)     # mathematical bold capital L (NFKC/NFKD -> L)
TAB = chr(0x0009)
SP = chr(0x0020)

# ---- fresh heading list marks (not non-ASCII numerals) --------------------
BULLET = chr(0x2022)
SECTION = chr(0x00A7)
NUMERO = chr(0x2116)
DEGREE = chr(0x00B0)
CIRCLED_LETTERS = [chr(c) for c in range(0x24B6, 0x24BB)]  # circled A..E (So)


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
    """Benign twin: exotic list mark, heading words KEPT (ROMANOK pattern)."""
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
    ('OK-LETTER', 'control-clean',
     'Benign: ASCII letter list marks with heading words kept (`## A. The address` x5).'),
    ('OK-NUMERO', 'control-clean',
     'Benign: numero-sign numbering with heading words kept (`## \u21161 The address` x5).'),
    ('OK-MCWORD', 'control-clean',
     'Benign sentinel: Mc mark U+0903 inside a heading word + clean twin on each h2 '
     '(ZWSH1 pattern with Mc).'),
    ('OK-DEVAHEAD', 'control-clean',
     'Benign: a legitimate Devanagari term (svaha, Mc marks U+093E/U+094D) appended to a '
     'normal h2 heading whose English phrase words are kept.'),
    # ---- verdict-token channel: bytes v10 does not name ----
    ('V-PO-MIDDOT', 'attack', 'Middle dot U+00B7 (Po) inside LOCATED: LOCA<U+00B7>TED.'),
    ('V-PO-BULLET', 'attack', 'Bullet U+2022 (Po) inside LOCATED: LOCA<U+2022>TED.'),
    ('V-PO-DOTLEAD', 'attack', 'One dot leader U+2024 (Po) inside LOCATED: LOCA<U+2024>TED.'),
    ('V-SO-COPY', 'attack', 'Copyright sign U+00A9 (So) inside LOCATED: LOCA<U+00A9>TED.'),
    ('V-SO-REG', 'attack', 'Registered sign U+00AE (So) inside LOCATED: LOCA<U+00AE>TED.'),
    ('V-SK-CIRC', 'attack', 'Modifier circumflex U+02C6 (Sk) inside LOCATED: LOCA<U+02C6>TED.'),
    ('V-LM-SUPH', 'attack', 'Modifier letter small h U+02B0 (Lm) inside LOCATED: LOCA<U+02B0>TED.'),
    ('V-CO-PUA', 'attack', 'Private-use U+E000 (Co) inside LOCATED: LOCA<U+E000>TED.'),
    ('V-CN-UNASSIGNED', 'attack', 'Unassigned U+0378 (Cn) inside LOCATED: LOCA<U+0378>TED.'),
    ('V-LU-OSTROKE', 'attack', 'O with stroke U+00D8 (Lu, no decomposition) as the O: L<U+00D8>CATED.'),
    ('V-LU-LSTROKE', 'attack', 'L with stroke U+0141 (Lu, no decomposition) as the L: <U+0141>OCATED.'),
    ('V-LU-ETH', 'attack', 'Eth U+00D0 (Lu, no decomposition) inside LOCATED: LOCA<U+00D0>TED.'),
    ('V-TAB-MID', 'attack', 'Tab U+0009 at a split the VERDICT-TAB regex misses: LOC<TAB>ATED.'),
    ('V-SPACE-MID', 'attack', 'Plain space U+0020 inside the token: LOCA TED.'),
    ('V-MATHL', 'attack', 'Mathematical bold capital L U+1D40B (NFKC/NFKD fold to L): <U+1D40B>OCATED.'),
    # ---- heading channel: phrase-only heads with non-numeral list marks ----
    ('H-LETTER', 'attack', 'ASCII letter list marks A. B. E. F. G. as the numbering token.'),
    ('H-COLON', 'attack', 'ASCII digit + colon as the numbering token: 1: 2: 3: 4: 5:.'),
    ('H-BULLET', 'attack', 'Bullet U+2022 (Po) as the list mark of five phrase-only heads.'),
    ('H-SECTION', 'attack', 'Section sign U+00A7 (Po) as the list mark of five phrase-only heads.'),
    ('H-NUMERO', 'attack', 'Numero sign U+2116 + ASCII digit (So + Nd) as the numbering token.'),
    ('H-DEGNUM', 'attack', 'N + degree sign U+00B0 + ASCII digit as the numbering token.'),
    ('H-PARENLETTER', 'attack', 'Parenthesised ASCII letters (a)..(e) as the numbering token.'),
    ('H-TRIPLENUM', 'attack', 'Three-level numbering 1.1.1..5.1.1 (beyond the two-level _NUM2 shape).'),
    ('H-CIRCLEDLETTER', 'attack', 'Circled letters U+24B6-24BA (So) as the list mark.'),
    ('H-HASH', 'attack', 'Hash + digit #1..#5 as the numbering token.'),
]


def builders():
    out = {}
    out['PLAINMOVE'] = gain('LOCATED')
    out['G0B'] = lambda: B.standard('critic98/G0B')
    out['OK-CIRC'] = ok_heads([chr(c) + '.' for c in range(0x2460, 0x2465)])
    out['OK-LETTER'] = ok_heads(['A.', 'B.', 'E.', 'F.', 'G.'])
    out['OK-NUMERO'] = ok_heads([NUMERO + str(i) for i in range(1, 6)])
    out['OK-MCWORD'] = entry_variant(word_reps(chr(0x0903)))
    out['OK-DEVAHEAD'] = entry_variant([
        ('## 1. The address',
         '## 1. The address \u2014 \u0938\u094d\u0935\u093e\u0939\u093e')])
    out['V-PO-MIDDOT'] = gain('LOCA' + PO_MIDDOT + 'TED')
    out['V-PO-BULLET'] = gain('LOCA' + PO_BULLET + 'TED')
    out['V-PO-DOTLEAD'] = gain('LOCA' + PO_DOTLEAD + 'TED')
    out['V-SO-COPY'] = gain('LOCA' + SO_COPY + 'TED')
    out['V-SO-REG'] = gain('LOCA' + SO_REG + 'TED')
    out['V-SK-CIRC'] = gain('LOCA' + SK_CIRC + 'TED')
    out['V-LM-SUPH'] = gain('LOCA' + LM_SUPH + 'TED')
    out['V-CO-PUA'] = gain('LOCA' + CO_PUA + 'TED')
    out['V-CN-UNASSIGNED'] = gain('LOCA' + CN_UNASSIGNED + 'TED')
    out['V-LU-OSTROKE'] = gain('L' + LU_OSTROKE + 'CATED')
    out['V-LU-LSTROKE'] = gain(LU_LSTROKE + 'OCATED')
    out['V-LU-ETH'] = gain('LOCA' + LU_ETH + 'TED')
    out['V-TAB-MID'] = gain('LOC' + TAB + 'ATED')
    out['V-SPACE-MID'] = gain('LOCA' + SP + 'TED')
    out['V-MATHL'] = gain(MATH_L + 'OCATED')
    out['H-LETTER'] = heads(['A.', 'B.', 'E.', 'F.', 'G.'])
    out['H-COLON'] = heads([str(i) + ':' for i in range(1, 6)])
    out['H-BULLET'] = heads([BULLET] * 5)
    out['H-SECTION'] = heads([SECTION] * 5)
    out['H-NUMERO'] = heads([NUMERO + str(i) for i in range(1, 6)])
    out['H-DEGNUM'] = heads(['N' + DEGREE + str(i) for i in range(1, 6)])
    out['H-PARENLETTER'] = heads(['(a)', '(b)', '(c)', '(d)', '(e)'])
    out['H-TRIPLENUM'] = heads([f'{i}.1.1' for i in range(1, 6)])
    out['H-CIRCLEDLETTER'] = heads(CIRCLED_LETTERS)
    out['H-HASH'] = heads(['#' + str(i) for i in range(1, 6)])
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
    print(f'OVERREFUSAL-INFO benign-sentinels=5 (G0B, OK-CIRC, OK-LETTER, OK-NUMERO, OK-MCWORD); '
          f'plainmove-refused={"yes" if any(r["outcome"] == "REFUSED-CONTROL" for r in results) else "NO"}')
    survivors = [r['id'] for r in attacks if r['outcome'] == 'SURVIVOR']
    print(f'SURVIVOR-IDS {",".join(survivors) or "none"}')
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(dict(tool=os.path.abspath(tool), tool_sha256=tool_sha, battery=battery_path,
                       results=results, counts=counts, tally=tally,
                       overrefusal=overref, survivors=survivors), f, indent=1, ensure_ascii=False)
        f.write('\n')
    with open(os.path.join(work, 'transcript-critic98.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(transcript) + '\n')
    with open(os.path.join(work, 'tally.txt'), 'w', encoding='utf-8') as f:
        f.write(tally + '\n')
    return 0


NAME = ['']
if __name__ == '__main__':
    sys.exit(main())
