#!/usr/bin/env python3
"""CriticO99 fresh-counterfeit attack driver (round 99, w1).

Attack seat. Nothing here repairs the grader, edits a driver or changes a pin. The driver
imports the frozen round-99 battery (reports/round-99/controls/battery99.py) READ-ONLY via
importlib and uses its own configure/grade/standard/_reps/_heads97/_dispo97/mc, so every
fixture is byte-for-byte the battery's shape: the standard mini-lane whose entry is
mc.body(None) with the five anchoring h2 headings, graded with battery99's exact argv.

Two populations, one run per class, once per tool:

  benign   (control-clean) valid script orthography and bare numbering headings a
           linguistics lane writes; a correct v11 keeps them CLEAN (rc 0).
  attack   (attack) mark-bearing headings and mixed-script numbering tokens that v10
           refuses wholesale; a v11 that narrows the mark check must keep refusing them
           or it reopens a forged anchor. Plus the 25 CriticO98b attack classes re-run
           unchanged (24 are v10 survivors and stay open; none may become newly refused
           or newly surviving relative to v10), and the six CriticO98b benign controls.

Env: CRIT_WORK (scratch, not /tmp), CRIT_BATTERY, CRIT_TOOL, CRIT_OUT_JSON.
Prints CRITIC-O99 survivors=<s> unnamed=<u> refused=<r> traceback=<t> overrefusal=<o>.
Exit 0 once the driver completes (counts are data); exit 2 on a usage error.
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

B = load(battery_path, 'critic99battery')
for attr in ('configure', 'grade', 'standard', '_reps', '_heads97', '_dispo97', 'mc',
             'GAINED_TAIL'):
    assert hasattr(B, attr), f'battery lacks {attr}'

B.configure(tool, work)

NAME = ['']

# ---- byte constants ---------------------------------------------------------------
MC_DEVA_AA = chr(0x093E)   # Devanagari vowel sign AA (Mc, spacing)
MC_DEVA_VIS = chr(0x0903)  # Devanagari visarga (Mc, spacing)
MN_DEVA_NUK = chr(0x093C)  # Devanagari nukta (Mn, non-spacing)
MN_DEVA_ANU = chr(0x0902)  # Devanagari anusvara (Mn)
MN_DEVA_CHA = chr(0x0901)  # Devanagari candrabindu (Mn)
MN_DEVA_VIR = chr(0x094D)  # Devanagari virama (Mn)
MN_LAT_ACU = chr(0x0301)   # combining acute accent (Mn, Latin)
MN_LAT_RING = chr(0x0325)  # combining ring below (Mn)
MN_LAT_TILD = chr(0x0303)  # combining tilde (Mn)
LO_DEVA_RA = chr(0x0930)   # Devanagari letter RA (Lo)
ROMAN = [chr(c) for c in range(0x2160, 0x2165)]   # U+2160.. U+2164 (Nl)
SMALL_ROMAN_12 = chr(0x217B)                       # ⅻ (Nl)
CIRCLED_1 = chr(0x2460)                            # ① (No)
FW_4 = chr(0xFF14)                                 # ４ (Nd, fullwidth)
FW_DOT = chr(0xFF0E)                               # ．(Po, fullwidth full stop)


def body():
    return B.mc.body(None)


def reps(pairs):
    return B._reps(body(), pairs)


def add_head(tok):
    """An extra bare h2 heading after the standard body (NUMOK1/NUMOK2 pattern)."""
    return body().rstrip('\n') + '\n\n## ' + tok + '\n\nA closing remark on the rite and its record.\n'


def script_head(word, base='## 4. Efficacy'):
    """A legitimate script word appended to a normal heading whose English words stay."""
    return reps([(base, base + ' \u2014 ' + word)])


DASH = chr(0x2014)


def dash_heads(mark):
    """Five phrase-only h2 heads whose only second token is a dash glued to `mark`."""
    return B.standard('critic99/' + NAME[0], entry=reps([
        ('## 1. The address', '## 1. address ' + DASH + mark),
        ('## 2. The petition', '## 2. petition ' + DASH + mark),
        ('## 3. Fixed and extempore', '## 3. efficacy ' + DASH + mark),
        ('## 4. Efficacy', '## 4. table ' + DASH + mark),
        ('## 5. Table', '## 5. Notes ' + DASH + mark)]))


def suffix_heads(mark):
    """Five heads: a phrase word with `mark` appended, plus a junk second token."""
    return B.standard('critic99/' + NAME[0], entry=reps([
        ('## 1. The address', '## 1. address' + mark + ' Notes'),
        ('## 2. The petition', '## 2. petition' + mark + ' Notes'),
        ('## 3. Fixed and extempore', '## 3. efficacy' + mark + ' Notes'),
        ('## 4. Efficacy', '## 4. table' + mark + ' Notes'),
        ('## 5. Table', '## 5. Notes' + mark + ' Notes')]))


def heads(prefixes):
    """Five phrase-bearing h2 heads with `prefixes` before the phrase word (_heads97)."""
    return B._heads97('critic99/' + NAME[0], prefixes)


def gain(token):
    """Gained S001 disposition line, `token` where LOCATED stands (_dispo97)."""
    return B._dispo97(token, 'critic99/' + NAME[0])


def variant(entry_text):
    """Wrap a prepared entry text in a battery standard() builder."""
    def f():
        return B.standard('critic99/' + NAME[0], entry=entry_text)
    return f


def ok_heads(prefixes):
    """Benign twin: exotic list mark, heading words KEPT (ROMANOK pattern)."""
    return reps([
        ('## 1. The address', '## ' + prefixes[0] + ' The address'),
        ('## 2. The petition', '## ' + prefixes[1] + ' The petition'),
        ('## 3. Fixed and extempore', '## ' + prefixes[2] + ' Fixed and extempore'),
        ('## 4. Efficacy', '## ' + prefixes[3] + ' Efficacy'),
        ('## 5. Table', '## ' + prefixes[4] + ' Table'),
    ])


def word_reps(infix):
    """Exotic mark inside a heading word + clean twin on each h2 (ZWSH1 pattern)."""
    return reps([('## 1. The address', '## addre' + infix + 'ss address'),
                 ('## 2. The petition', '## petition' + infix + ' petition'),
                 ('## 3. Fixed and extempore', '## efficac' + infix + 'y efficacy'),
                 ('## 4. Efficacy', '## tabl' + infix + 'e table'),
                 ('## 5. Table', '## No' + infix + 'tes Notes')])


# ---- class table ------------------------------------------------------------------
# (id, population, description, builder)
# population: 'benign'  -> must be CLEAN (rc 0, no traceback) on a correct v11
#             'attack'  -> must be REFUSED (rc != 0, no traceback) on a correct v11
CASES = [
    # ---- sanity + CriticO98b benign controls (claim O4 must keep these CLEAN) ----
    ('G0C', 'benign', 'Clean control: unmodified mini-lane re-graded (fixture sanity).',
     lambda: B.standard('critic99/G0C')),
    ('OK-CIRC', 'benign',
     'Benign: circled-digit numbering with heading words kept (`## \u2460. The address` x5).',
     variant(ok_heads([chr(c) + '.' for c in range(0x2460, 0x2465)]))),
    ('OK-LETTER', 'benign',
     'Benign: ASCII letter list marks with heading words kept (`## A. The address` x5).',
     variant(ok_heads(['A.', 'B.', 'E.', 'F.', 'G.']))),
    ('OK-NUMERO', 'benign',
     'Benign: numero-sign numbering with heading words kept (`## \u21161 The address` x5).',
     variant(ok_heads([chr(0x2116) + str(i) for i in range(1, 6)]))),
    ('OK-MCWORD', 'benign',
     'Benign sentinel: Mc mark U+0903 inside a heading word + clean twin on each h2.',
     variant(word_reps(MC_DEVA_VIS))),
    ('OK-DEVAHEAD', 'benign',
     'Benign: a legitimate Devanagari term (svaha, Mc U+093E/U+094D) appended to a '
     'normal h2 heading whose English phrase words are kept.',
     variant(reps([('## 1. The address',
                   '## 1. The address \u2014 \u0938\u094d\u0935\u093e\u0939\u093e')]))),

    # ---- benign: valid script orthography in h2 headings (beyond battery99) ----
    ('OK-BENG', 'benign', 'Benign: Bengali word \u09ac\u09be\u0982\u09b2\u09be (Mc U+09BE, Mn U+0982) appended to a normal heading.',
     variant(script_head('\u09ac\u09be\u0982\u09b2\u09be'))),
    ('OK-BENG-HASANTA', 'benign', 'Benign: Bengali conjunct \u0995\u09cd\u09b7 (Mn U+09CD hasanta) appended to a normal heading.',
     variant(script_head('\u0995\u09cd\u09b7'))),
    ('OK-TAMIL', 'benign', 'Benign: Tamil word \u0ba4\u0bae\u0bbf\u0bb4\u0bcd (Mn U+0BCD virama) appended to a normal heading.',
     variant(script_head('\u0ba4\u0bae\u0bbf\u0bb4\u0bcd'))),
    ('OK-THAI', 'benign', 'Benign: Thai word \u0e19\u0e49\u0e33 (Mn U+0E49 tone mark) appended to a normal heading.',
     variant(script_head('\u0e19\u0e49\u0e33'))),
    ('OK-KHMER', 'benign', 'Benign: Khmer word \u1781\u17d2\u1798\u17c2\u179a (Mn U+17D2 coeng, Mc U+17C2) appended to a normal heading.',
     variant(script_head('\u1781\u17d2\u1798\u17c2\u179a'))),
    ('OK-MYANMAR', 'benign', 'Benign: Myanmar word \u1019\u103c\u1014\u103a\u1019\u102c (Mn U+103A asat, Mc U+102C) appended to a normal heading.',
     variant(script_head('\u1019\u103c\u1014\u103a\u1019\u102c'))),
    ('OK-TIBETAN', 'benign', 'Benign: Tibetan word \u0f56\u0f7c\u0f51 (Mn U+0F7C vowel) appended to a normal heading.',
     variant(script_head('\u0f56\u0f7c\u0f51'))),
    ('OK-JAPAN-NFD', 'benign', 'Benign: decomposed Japanese \u304b\u3099 (U+3099, name COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK) appended to a normal heading.',
     variant(script_head('\u304b' + chr(0x3099)))),
    ('OK-CYR-NFD', 'probe', 'Extra probe: decomposed Cyrillic \u0435\u0301 (U+0435 + combining acute U+0301) appended to a normal heading.',
     variant(script_head('\u0435' + MN_LAT_ACU))),
    ('OK-FR-PETITION', 'probe', 'Extra probe: French pe\u0301titionnaire in NFD (a word that contains the phrase "petition" as a proper substring) appended to a normal heading.',
     variant(script_head('pe' + MN_LAT_ACU + 'titionnaire'))),
    ('OK-ARABIC', 'benign', 'Benign: Arabic word \u0643\u0650\u062a\u064e\u0627\u0628 with harakat (Mn U+0650/U+064E) appended to a normal heading.',
     variant(script_head('\u0643\u0650\u062a\u064e\u0627\u0628'))),
    ('OK-HEBREW', 'benign', 'Benign: Hebrew word \u05e1\u05b5\u05e4\u05b6\u05e8 with niqqud (Mn U+05B5/U+05B6) appended to a normal heading.',
     variant(script_head('\u05e1\u05b5\u05e4\u05b6\u05e8'))),
    ('OK-VIETNFC', 'benign', 'Benign: Vietnamese NFC \u1ebf\u1ec7 (precomposed, no combining marks) appended to a normal heading.',
     variant(script_head('ti\u1ebfng Vi\u1ec7t'))),
    ('OK-VIETNFD', 'benign', 'Benign: Vietnamese NFD tie\u0302\u0301ng Vie\u0302\u0323t (combining marks on Latin bases) appended to a normal heading.',
     variant(script_head('tie' + chr(0x0302) + chr(0x0301) + 'ng Vie' + chr(0x0302) + chr(0x0323) + 't'))),
    ('OK-IPA', 'benign', 'Benign: IPA with combining diacritics n\u0325 a\u0303 in a non-phrase word appended to a normal heading.',
     variant(script_head('n' + MN_LAT_RING + ' a' + MN_LAT_TILD))),
    ('OK-DEVANUKTA', 'benign', 'Benign: Devanagari \u0915\u093c\u0932\u092e with nukta U+093C (Mn) appended to a normal heading.',
     variant(script_head('\u0915' + MN_DEVA_NUK + '\u0932\u092e'))),
    ('OK-DEVANUSVARA', 'benign', 'Benign: Devanagari \u0938\u0902\u0938\u094d\u0915\u0943\u0924 with anusvara U+0902 and virama U+094D appended to a normal heading.',
     variant(script_head('\u0938' + MN_DEVA_ANU + '\u0938' + MN_DEVA_VIR + '\u0915\u0943\u0924'))),
    ('OK-DEVACHANDRA', 'benign', 'Benign: Devanagari \u0939\u0901\u0938\u0940 with chandrabindu U+0901 appended to a normal heading.',
     variant(script_head('\u0939' + MN_DEVA_CHA + '\u0938\u0940'))),
    ('OK-BAREROMAN', 'benign', 'Benign: bare small-roman-numeral section heading `## \u217b.` after the body (NUMOK1 pattern).',
     lambda: B.standard('critic99/OK-BAREROMAN', entry=add_head(SMALL_ROMAN_12 + '.'))),
    ('OK-BARECIRC', 'benign', 'Benign: bare circled-digit section heading `## \u2460` after the body.',
     lambda: B.standard('critic99/OK-BARECIRC', entry=add_head(CIRCLED_1))),
    ('OK-BARENODOT', 'benign', 'Benign: bare roman-numeral heading with no dot `## \u2163` after the body.',
     lambda: B.standard('critic99/OK-BARENODOT', entry=add_head(ROMAN[3]))),
    ('OK-BAREFW-NODOT', 'benign', 'Benign: bare fullwidth-digit heading with no dot `## \uff14` after the body.',
     lambda: B.standard('critic99/OK-BAREFW-NODOT', entry=add_head(FW_4))),
    ('OK-BAREFW', 'benign', 'Benign: bare fullwidth-digit section heading `## \uff14\uff0e` after the body.',
     lambda: B.standard('critic99/OK-BAREFW', entry=add_head(FW_4 + FW_DOT))),

    # ---- attack: mark-bearing numbering tokens (v10 refuses all by HEADING-COMBINING) ----
    ('A-MCONDIGIT', 'attack',
     'Mc U+093E grafted on the ASCII digit numbering token: `## 1<U+093E>. address` x5.',
     lambda: heads(['1' + MC_DEVA_AA + '.', '2' + MC_DEVA_AA + '.', '3' + MC_DEVA_AA + '.',
                    '4' + MC_DEVA_AA + '.', '5' + MC_DEVA_AA + '.'])),
    ('A-VISARGADIGIT', 'attack',
     'Mc visarga U+0903 grafted on the digit numbering token: `## 1<U+0903>. address` x5.',
     lambda: heads(['1' + MC_DEVA_VIS + '.', '2' + MC_DEVA_VIS + '.', '3' + MC_DEVA_VIS + '.',
                    '4' + MC_DEVA_VIS + '.', '5' + MC_DEVA_VIS + '.'])),
    ('A-NUKTADIGIT', 'attack',
     'Mn nukta U+093C grafted on the digit numbering token: `## 1<U+093C>. address` x5.',
     lambda: heads(['1' + MN_DEVA_NUK + '.', '2' + MN_DEVA_NUK + '.', '3' + MN_DEVA_NUK + '.',
                    '4' + MN_DEVA_NUK + '.', '5' + MN_DEVA_NUK + '.'])),
    ('A-MARKTOK', 'attack',
     'Mark-only token as the second heading token: `## address <U+093E>` x5 (phrase-only head '
     'padded to two tokens by a lone Mc).',
     lambda: heads([MC_DEVA_AA, MC_DEVA_AA, MC_DEVA_AA, MC_DEVA_AA, MC_DEVA_AA])),
    ('A-MARKTOK-LAT', 'attack',
     'Latin combining acute U+0301 as a lone second heading token: `## address <U+0301>` x5.',
     lambda: heads([MN_LAT_ACU, MN_LAT_ACU, MN_LAT_ACU, MN_LAT_ACU, MN_LAT_ACU])),
    ('A-DEVLETTERDIGIT', 'attack',
     'Digit + Devanagari letter as the numbering token: `## 1<U+0930>. address` x5.',
     lambda: heads(['1' + LO_DEVA_RA + '.', '2' + LO_DEVA_RA + '.', '3' + LO_DEVA_RA + '.',
                    '4' + LO_DEVA_RA + '.', '5' + LO_DEVA_RA + '.'])),
    ('A-LATMARKINDIC', 'attack',
     'Latin combining acute U+0301 on a Devanagari base as the second heading token: '
     '`## address <U+0930><U+0301>` x5 (script-aware mark stripping would miss it).',
     lambda: heads([LO_DEVA_RA + MN_LAT_ACU, LO_DEVA_RA + MN_LAT_ACU, LO_DEVA_RA + MN_LAT_ACU,
                    LO_DEVA_RA + MN_LAT_ACU, LO_DEVA_RA + MN_LAT_ACU])),
    ('A-DEVLETTERMARK', 'attack',
     'Digit + Devanagari base + Latin mark as the numbering token: `## 1<U+0930><U+0301>. address` x5.',
     lambda: heads(['1' + LO_DEVA_RA + MN_LAT_ACU + '.', '2' + LO_DEVA_RA + MN_LAT_ACU + '.',
                    '3' + LO_DEVA_RA + MN_LAT_ACU + '.', '4' + LO_DEVA_RA + MN_LAT_ACU + '.',
                    '5' + LO_DEVA_RA + MN_LAT_ACU + '.'])),
    ('A-MIXROMANDIGIT', 'attack',
     'Mixed-script numbering token roman numeral + ASCII digit: `## <U+2163>1. address` x5.',
     lambda: heads([ROMAN[i] + str(i + 1) + '.' for i in range(5)])),
    ('A-MIXCIRCDIGIT', 'attack',
     'Mixed-script numbering token ASCII digit + circled digit U+2460: `## 1<U+2460>. address` x5.',
     lambda: heads([str(i + 1) + CIRCLED_1 + '.' for i in range(5)])),
    ('A-FWPERMARK', 'attack',
     'Digit + Mc + fullwidth full stop as the numbering token: `## 1<U+093E><U+FF0E> address` x5.',
     lambda: heads(['1' + MC_DEVA_AA + FW_DOT, '2' + MC_DEVA_AA + FW_DOT, '3' + MC_DEVA_AA + FW_DOT,
                    '4' + MC_DEVA_AA + FW_DOT, '5' + MC_DEVA_AA + FW_DOT])),
    ('A-MARKTOK-NUM', 'attack',
     'Number, phrase word, then a mark-only third token: `## 1. address <U+093E>` x5 '
     '(tests whether only the first token is inspected).',
     lambda: heads(['1. address ' + MC_DEVA_AA, '2. petition ' + MC_DEVA_AA,
                    '3. efficacy ' + MC_DEVA_AA, '4. table ' + MC_DEVA_AA,
                    '5. Notes ' + MC_DEVA_AA])),
    ('A-MARKTOK-FIRST', 'attack',
     'Mark-only FIRST token before the phrase word: `## <U+093E>. address` x5.',
     lambda: heads([MC_DEVA_AA + '.', MC_DEVA_AA + '.', MC_DEVA_AA + '.',
                    MC_DEVA_AA + '.', MC_DEVA_AA + '.'])),
    ('A-ZWJDIGIT', 'attack',
     'ZWJ U+200D (Cf, not a mark) on the digit numbering token: `## 1<U+200D>. address` x5 '
     '(pre-existing probe: v10 has no Cf heading check, so a survivor here is not a regression).',
     lambda: heads(['1' + chr(0x200D) + '.', '2' + chr(0x200D) + '.', '3' + chr(0x200D) + '.',
                    '4' + chr(0x200D) + '.', '5' + chr(0x200D) + '.'])),
    ('OK-MCWORD-DEVAA', 'benign',
     'Benign: Mc U+093E inside a heading word + clean twin on each h2 (OK-MCWORD shape, '
     'Devanagari mark instead of visarga).',
     lambda: heads(['addre' + MC_DEVA_AA + 'ss', 'petitio' + MC_DEVA_AA + 'n',
                    'efficac' + MC_DEVA_AA + 'y', 'tabl' + MC_DEVA_AA + 'e',
                    'No' + MC_DEVA_AA + 'tes'])),

    ('A-DASH-MC', 'attack',
     'Non-Latin Mc U+093E glued to a separator dash U+2014 as the second token: '
     '`## 1. address \u2014<U+093E>` x5 (the mark turns a list mark into a content token).',
     lambda: dash_heads(MC_DEVA_AA)),
    ('A-DASH-VIS', 'attack',
     'Visarga U+0903 glued to a separator dash U+2014: `## 1. address \u2014<U+0903>` x5.',
     lambda: dash_heads(MC_DEVA_VIS)),
    ('A-DASH-LAT', 'attack',
     'Latin combining acute U+0301 glued to a separator dash U+2014: `## 1. address \u2014<U+0301>` x5 '
     '(control: v11 refuses this one by name).',
     lambda: dash_heads(MN_LAT_ACU)),
    ('A-DASH-NOMARK', 'attack',
     'Control for A-DASH-MC: the same five heads with a bare dash and no mark '
     '(`## 1. address \u2014`), span 1 < 3 on any correct grader.',
     lambda: dash_heads('')),
    ('A-SUFFIX-MC', 'attack',
     'Mc U+093E appended to a phrase word, junk second token: `## 1. address<U+093E> Notes` x5 '
     '(norm() still contains the phrase as a substring).',
     lambda: suffix_heads(MC_DEVA_AA)),
    ('A-SUFFIX-VIS', 'attack',
     'Visarga U+0903 appended to a phrase word: `## 1. address<U+0903> Notes` x5.',
     lambda: suffix_heads(MC_DEVA_VIS)),
    ('A-SUFFIX-LAT', 'attack',
     'Latin combining acute U+0301 appended to a phrase word: `## 1. address<U+0301> Notes` x5 '
     '(control: v11 refuses this one by name).',
     lambda: suffix_heads(MN_LAT_ACU)),

    # ---- CriticO98b attack classes re-run unchanged (24 v10 survivors stay open) ----
    ('PLAINMOVE', 'attack', 'Control-refuse: plain forged verdict `- S001 LOCATED recheck moved`.',
     lambda: gain('LOCATED')),
    ('V-PO-MIDDOT', 'attack', 'Middle dot U+00B7 (Po) inside LOCATED.', lambda: gain('LOCA' + chr(0x00B7) + 'TED')),
    ('V-PO-BULLET', 'attack', 'Bullet U+2022 (Po) inside LOCATED.', lambda: gain('LOCA' + chr(0x2022) + 'TED')),
    ('V-PO-DOTLEAD', 'attack', 'One dot leader U+2024 (Po) inside LOCATED.', lambda: gain('LOCA' + chr(0x2024) + 'TED')),
    ('V-SO-COPY', 'attack', 'Copyright sign U+00A9 (So) inside LOCATED.', lambda: gain('LOCA' + chr(0x00A9) + 'TED')),
    ('V-SO-REG', 'attack', 'Registered sign U+00AE (So) inside LOCATED.', lambda: gain('LOCA' + chr(0x00AE) + 'TED')),
    ('V-SK-CIRC', 'attack', 'Modifier circumflex U+02C6 (Sk) inside LOCATED.', lambda: gain('LOCA' + chr(0x02C6) + 'TED')),
    ('V-LM-SUPH', 'attack', 'Modifier letter small h U+02B0 (Lm) inside LOCATED.', lambda: gain('LOCA' + chr(0x02B0) + 'TED')),
    ('V-CO-PUA', 'attack', 'Private-use U+E000 (Co) inside LOCATED.', lambda: gain('LOCA' + chr(0xE000) + 'TED')),
    ('V-CN-UNASSIGNED', 'attack', 'Unassigned U+0378 (Cn) inside LOCATED.', lambda: gain('LOCA' + chr(0x0378) + 'TED')),
    ('V-LU-OSTROKE', 'attack', 'O with stroke U+00D8 (Lu) as the O: L<U+00D8>CATED.', lambda: gain('L' + chr(0x00D8) + 'CATED')),
    ('V-LU-LSTROKE', 'attack', 'L with stroke U+0141 (Lu) as the L: <U+0141>OCATED.', lambda: gain(chr(0x0141) + 'OCATED')),
    ('V-LU-ETH', 'attack', 'Eth U+00D0 (Lu) inside LOCATED.', lambda: gain('LOCA' + chr(0x00D0) + 'TED')),
    ('V-TAB-MID', 'attack', 'Tab U+0009 inside the token: LOC<TAB>ATED.', lambda: gain('LOC' + chr(0x09) + 'ATED')),
    ('V-SPACE-MID', 'attack', 'Plain space U+0020 inside the token: LOCA TED.', lambda: gain('LOCA' + chr(0x20) + 'TED')),
    ('V-MATHL', 'attack', 'Mathematical bold capital L U+1D40B (NFKC/NFKD fold to L).', lambda: gain(chr(0x1D40B) + 'OCATED')),
    ('H-LETTER', 'attack', 'ASCII letter list marks A. B. E. F. G. as the numbering token.',
     lambda: heads(['A.', 'B.', 'E.', 'F.', 'G.'])),
    ('H-COLON', 'attack', 'ASCII digit + colon as the numbering token: 1: 2: 3: 4: 5:.',
     lambda: heads([str(i) + ':' for i in range(1, 6)])),
    ('H-BULLET', 'attack', 'Bullet U+2022 (Po) as the list mark of five phrase-only heads.',
     lambda: heads([chr(0x2022)] * 5)),
    ('H-SECTION', 'attack', 'Section sign U+00A7 (Po) as the list mark of five phrase-only heads.',
     lambda: heads([chr(0x00A7)] * 5)),
    ('H-NUMERO', 'attack', 'Numero sign U+2116 + ASCII digit as the numbering token.',
     lambda: heads([chr(0x2116) + str(i) for i in range(1, 6)])),
    ('H-DEGNUM', 'attack', 'N + degree sign U+00B0 + ASCII digit as the numbering token.',
     lambda: heads(['N' + chr(0x00B0) + str(i) for i in range(1, 6)])),
    ('H-PARENLETTER', 'attack', 'Parenthesised ASCII letters (a)..(e) as the numbering token.',
     lambda: heads(['(a)', '(b)', '(c)', '(d)', '(e)'])),
    ('H-TRIPLENUM', 'attack', 'Three-level numbering 1.1.1..5.1.1.',
     lambda: heads([f'{i}.1.1' for i in range(1, 6)])),
    ('H-CIRCLEDLETTER', 'attack', 'Circled letters U+24B6-24BA (So) as the list mark.',
     lambda: heads([chr(c) for c in range(0x24B6, 0x24BB)])),
    ('H-HASH', 'attack', 'Hash + digit #1..#5 as the numbering token.',
     lambda: heads(['#' + str(i) for i in range(1, 6)])),
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
    print(f'BATTERY sha256={hashlib.sha256(open(battery_path, "rb").read()).hexdigest()} '
          f'path={os.path.abspath(battery_path)}')
    results = []
    transcript = []
    for cid, pop, desc, build in CASES:
        NAME[0] = cid
        fx = build()
        rc, out, cmd = B.grade(fx)
        r = classify(rc, out)
        if pop in ('benign', 'probe'):
            r['outcome'] = 'CLEAN' if (rc == 0 and not r['traceback']) else 'OVERREFUSAL'
        else:
            if r['outcome'] == 'SURVIVOR':
                pass
            elif r['traceback']:
                r['outcome'] = 'TRACEBACK'
            elif cid == 'PLAINMOVE':
                r['outcome'] = 'REFUSED-CONTROL'
            else:
                r['outcome'] = 'REFUSED-NAMED' if r['named'] else 'REFUSED-UNNAMED'
        last = (out.strip().splitlines() or [''])[-1][:200]
        fails_detail = [l[:240] for l in out.splitlines() if 'FAIL' in l]
        results.append(dict(id=cid, population=pop, desc=desc, rc=rc,
                            traceback=r['traceback'], outcome=r['outcome'], named=r['named'],
                            last_line=last, fails=fails_detail, cmd=cmd))
        transcript.append(f'CLASS {cid} pop={pop} rc={rc} outcome={r["outcome"]} '
                          f'named={",".join(r["named"]) if r["named"] else "none"}')
        transcript.append(f'  recipe: {desc}')
        for f in fails_detail:
            transcript.append(f'  FAIL {f}')
        print(f'CLASS {cid} pop={pop} rc={rc} traceback={"yes" if r["traceback"] else "no"} '
              f'named={",".join(r["named"]) if r["named"] else "none"} outcome={r["outcome"]}')
        print(f'  detail {cid}: last-line={last!r}')

    attacks = [r for r in results if r['population'] == 'attack']
    counts = {k: sum(1 for r in attacks if r['outcome'] == k)
              for k in ('SURVIVOR', 'REFUSED-NAMED', 'REFUSED-UNNAMED', 'TRACEBACK')}
    refused = counts['REFUSED-NAMED'] + counts['REFUSED-UNNAMED']
    tally = (f'CRITIC-O99 survivors={counts["SURVIVOR"]} unnamed={counts["REFUSED-UNNAMED"]} '
             f'refused={refused} traceback={counts["TRACEBACK"]} '
             f'overrefusal={sum(1 for r in results if r["outcome"] == "OVERREFUSAL" and r["population"] == "benign")}')
    print(tally)
    # population subtallies so a v10/v11 delta is readable class by class
    for pop, label in (('benign', 'BENIGN'), ('attack', 'ATTACK'), ('probe', 'PROBE')):
        sub = [r for r in results if r['population'] == pop]
        print(f'CRITIC-O99-{label} n={len(sub)} '
              f'survivors={sum(1 for r in sub if r["outcome"] == "SURVIVOR")} '
              f'refused={sum(1 for r in sub if r["outcome"].startswith("REFUSED"))} '
              f'clean={sum(1 for r in sub if r["outcome"] == "CLEAN")} '
              f'overrefusal={sum(1 for r in sub if r["outcome"] == "OVERREFUSAL")} '
              f'traceback={sum(1 for r in sub if r["outcome"] == "TRACEBACK")}')
    overref = [r['id'] for r in results if r['outcome'] == 'OVERREFUSAL' and r['population'] == 'benign']
    overref_probe = [r['id'] for r in results if r['outcome'] == 'OVERREFUSAL' and r['population'] == 'probe']
    print(f'OVERREFUSAL n={len(overref)} ids={",".join(overref) or "none"}')
    print(f'OVERREFUSAL-PROBE n={len(overref_probe)} ids={",".join(overref_probe) or "none"}')
    survivors = [r['id'] for r in attacks if r['outcome'] == 'SURVIVOR']
    print(f'SURVIVOR-IDS {",".join(survivors) or "none"}')
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(dict(tool=os.path.abspath(tool), tool_sha256=tool_sha, battery=battery_path,
                       results=results, counts=counts, tally=tally, overrefusal=overref,
                       overrefusal_probe=overref_probe,
                       survivors=survivors), f, indent=1, ensure_ascii=False)
        f.write('\n')
    with open(os.path.join(work, 'transcript-critic99.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(transcript) + '\n')
    with open(os.path.join(work, 'tally.txt'), 'w', encoding='utf-8') as f:
        f.write(tally + '\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
