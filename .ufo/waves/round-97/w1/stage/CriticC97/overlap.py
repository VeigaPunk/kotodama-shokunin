#!/usr/bin/env python3
"""CriticC97: word-level 8-gram overlap between the entry and each adjacent owner.
Usage: overlap.py <entry> <owner1> [owner2 ...]
Word tokens: re.findall(r'\\w+', text.casefold()). 8-grams as tuples; shared =
multiset intersection of entry 8-grams and owner 8-grams (counts min). Also
reports maximal shared contiguous spans (runs) with length >= 8."""
import re, sys
from collections import Counter

N = 8

def toks(path):
    text = open(path, encoding='utf-8', errors='replace').read()
    return re.findall(r'\w+', text.casefold())

def grams(t):
    return Counter(tuple(t[i:i+N]) for i in range(len(t) - N + 1))

def spans(a, b):
    """maximal contiguous token runs shared by a and b, length >= N, as (i,j,len)."""
    bs = set(tuple(b[i:i+N]) for i in range(len(b) - N + 1))
    out = []
    i = 0
    while i <= len(a) - N:
        if tuple(a[i:i+N]) in bs:
            j = i + N
            while j < len(a) and tuple(a[j-N+1:j+1]) in bs:
                j += 1
            out.append((i, j - i))
            i = j
        else:
            i += 1
    return out

def main():
    entry, *owners = sys.argv[1:]
    et = toks(entry)
    eg = grams(et)
    print(f'entry tokens={len(et)} 8-grams={sum(eg.values())} distinct={len(eg)}')
    for o in owners:
        ot = toks(o)
        og = grams(ot)
        shared = eg & og
        total = sum(shared.values())
        print(f'--- {o}')
        print(f'    owner tokens={len(ot)} 8-grams={sum(og.values())} distinct={len(og)}')
        print(f'    shared distinct 8-grams={len(shared)} shared multiset count={total}')
        ss = sorted(spans(et, ot), key=lambda x: (-x[1], x[0]))
        for i, ln in ss[:3]:
            print(f'    SPAN len={ln} at entry tok {i}: {" ".join(et[i:i+ln])[:300]}')
        if not ss:
            print('    SPAN none')

if __name__ == '__main__':
    main()
