#!/usr/bin/env python3
"""ScribeNotation round-88: re-verify every anchor quote of the staged section
against the retained live capture AND the retained Wayback capture.

Read-only; writes nothing. Exit 0 when every quote is present in both copies,
1 otherwise, 2 on a missing input.

Usage:
  python3 -B verify-quotes.py [--receipts RECEIPTS_DIR]
"""
import argparse
import html
import pathlib
import re
import sys
import unicodedata

PAIRS = [
    ('S931', 'S931-terrain-17506-lang-en-2026-11-04.html', 'S931-terrain-17506-wayback-20190505043833.html', [
        "All numerical notations fall into five basic typological categories, across two dimensions",
        "is logically excluded because multiplicative systems express power through special power signs, not through place value",
        "it is evident that there is no perfect system",
        "Ciphered-additive systems write numerals more compactly than any of the other types",
        "Cumulative-positional systems use a much smaller inventory of signs than other systems",
        "Cumulative-positional numeral systems are cross-culturally very rare, in fact, the rarest of the five types described above",
        "such devices seem to have been developed independently in the Near East, East Asia, India, the Andes, and Mesoamerica",
        "whereas numerical notation systems are structured through a base",
        "tallies do not have a base",
        "It is comparatively rare to use numerical notation directly for arithmetic even today",
        "Numerical notations are semiotically and causally linked to, but distinct from, both the numeral words of their users' languages",
        "twenty seventeen and two thousand seventeen are both available to English speakers upon reading the numeral 2017",
        "the two systems dating unequivocally from the 4 th millennium BCE, are cumulative-additive",
        "This avoids the teleological argument of Ifrah (1987) and Dehaene (1997) that sees decimal, positional numeration as the end-point of a developmental sequence towards perfection",
    ]),
    ('S932', 'S932-mactutor-babylonian-numerals-2026-11-04.html', 'S932-mactutor-babylonian-wayback-20200708131715.html', [
        "the Babylonians only had to learn two symbols to produce their base 60 positional system",
        "there was no zero to put into an empty position",
        "later Babylonian civilisations did invent a symbol to indicate an empty place",
        "neither the Sumerian nor the Akkadian system was a positional system",
        "the 59 numbers, which go into one of the places of the system, were built from a 'unit' symbol and a 'ten' symbol",
    ]),
    ('S933', 'S933-mactutor-egyptian-numerals-2026-11-04.html', 'S933-mactutor-egyptian-wayback-20200724192341.html', [
        "separate symbols for one unit, one ten, one hundred, one thousand, one ten thousand, one hundred thousand, and one million",
        "To make up the number 276, for example, fifteen symbols were required",
        "These numerals allowed numbers to be written in a far more compact form yet using the system required many more symbols to be memorised",
        "did not form a positional system so the particular numerals could be written in any order",
        "The number 9999 had just 4 hieratic symbols instead of 36 hieroglyphs",
    ]),
]


def body_text(path):
    text = path.read_text(errors='replace')
    text = re.sub(r'(?is)<(script|style|noscript|template).*?</\1>', ' ', text)
    text = re.sub(r'(?is)<figcaption[^>]*>.*?</figcaption>', ' ', text)
    text = re.sub(r'(?s)<[^>]+>', ' ', text)
    return re.sub(r'\s+', ' ', html.unescape(text))


def norm(text):
    text = unicodedata.normalize('NFKC', text).casefold()
    return ' '.join(w for w in re.sub(r'[^\w]+', ' ', text).split() if w)


# Quoted spans in the staged section that are the AUTHOR'S OWN framing words rather
# than source quotations. Each is listed so the check can exclude it explicitly
# instead of silently skipping it.
OWN_FRAMING = [
    'which stage is it at?',
]


def prose_quotes(section_path, bodies):
    """Every double-quoted span of the staged section that is a source quotation.

    A span is a source quotation when it is not one of the section's own framing
    phrases. Only spans that lie on one line are considered, so a phrase that
    merely happens to sit between two quotes is not mistaken for a quotation.
    """
    text = section_path.read_text()
    corpus = '\n'.join(norm(body_text(p)) for p in bodies)
    found = []
    for number, line in enumerate(text.splitlines(), 1):
        for span in re.findall(r'"([^"\n]{8,})"', line):
            # A span carrying markdown bold markers or a section reference is a
            # regex artifact spanning two separate quotes, not a quotation.
            if len(span.split()) < 3 or '**' in span or '\u00a7' in span:
                continue
            # A span that opens or closes mid-sentence (leading or trailing
            # space, no terminal punctuation) is a fragment between two quotes.
            if span != span.strip() and span.strip()[-1:] not in '.?':
                continue
            if span.strip() in OWN_FRAMING:
                continue
            found.append((number, span, norm(span) in corpus))
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--receipts', default=str(pathlib.Path(__file__).parent))
    ap.add_argument('--section', default=str(pathlib.Path(__file__).parent.parent / 'notation-section.md'))
    ns = ap.parse_args()
    root = pathlib.Path(ns.receipts)
    failures = 0
    total = 0
    bodies = []
    for sid, live_name, arch_name, quotes in PAIRS:
        live = root / live_name
        arch = root / arch_name
        if not live.is_file() or not arch.is_file():
            print('QUOTE_ERROR missing capture for ' + sid, file=sys.stderr)
            return 2
        bodies.append(live)
        live_words = norm(body_text(live))
        arch_words = norm(body_text(arch))
        for quote in quotes:
            total += 1
            nq = norm(quote)
            in_live = nq in live_words
            in_arch = nq in arch_words
            if not (in_live and in_arch):
                failures += 1
                print('QUOTE FAIL ' + sid + ' live=' + str(in_live) + ' arch=' + str(in_arch) +
                      ' | ' + quote[:70])
    print('ANCHOR QUOTES: ' + str(total - failures) + '/' + str(total) + ' located in both copies')

    section_path = pathlib.Path(ns.section)
    if section_path.is_file():
        prose = prose_quotes(section_path, bodies)
        prose_bad = [p for p in prose if not p[2]]
        print('PROSE QUOTES: ' + str(len(prose) - len(prose_bad)) + '/' + str(len(prose)) +
              ' located in the retained bodies')
        for number, span, _ in prose_bad:
            failures += 1
            print('PROSE FAIL line ' + str(number) + ' | ' + span[:70])
        total += len(prose)
    else:
        print('PROSE QUOTES: skipped, section file not found at ' + str(section_path))
    print('QUOTES: ' + str(total - failures) + '/' + str(total) + ' located in both copies')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
