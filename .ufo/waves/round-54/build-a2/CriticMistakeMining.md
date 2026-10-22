# CriticMistakeMining — round 54, attempt 2

Seat: `KotodamaR54a2.CriticMistakeMining` (critic, leaf). Everything below was re-opened or run in this session. Nothing from attempt 1's scratch is used. Scratch: `/fast/scratch/hyaku/kotodama-r54-a2/CriticMistakeMining/`. Tool installs: none.

## Pick

I picked candidate (a), joined Gate quotes past 25 words. It is the only one of the three whose fix can be a short stdlib check shown able to fail.

- (b), S201 locators off by one and "some communities": no mechanical check can fail on these without re-opening the page. The fix is procedural, and the round-53 closure already routed it (fixed in prerequisite `d761ee8`, per `reports/round-54/claims.json:5`).
- (c), S237 cites a landing page but quotes the offprint: the nearest mechanical proxy is "a printed-page locator on a URL that is not a `.pdf`". On round-53 `## Gate` that proxy flags **49 lines, and only 1 is the real defect** (`round-53.md:182`, S237). The other 48 are PDF endpoints without a `.pdf` suffix: `pure.mpg.de/.../content`, the `uva.nl/binaries/...` asset, WRAP, the Tilburg bitstream and OJS. A check that fails 48 times on good lines teaches nothing.

## Counterexamples to the assigned framing

1. **"Expect the five lines" does not reproduce under any one rule.** The closure wrote "seven lines … (S200, S205 ×3, S214, S224, S236)" (`round-53-verifier-spotcheck.md:149`) and routed five rows (`:175`). Applying its own metric (all quoted words on the line) consistently over S187–S238 gives **12 lines, not 7**. It missed five lines:
   - S187 `round-53.md:42` (28 words);
   - S188 `:44` (26);
   - S189 `:49` (28);
   - S192 `:58` (40);
   - S194 `:62` (28).

   Outside its S187–S238 scope, the same metric also flags S184 `:32` (33) and S186 `:34` (26). The closure's mechanical claim had no published unit and cannot be re-derived.
2. **The routed fix for S200, S214, S224 and S236 has nothing to change.** Each of those lines carries one quote plus a quoted heading or paragraph anchor inside the locator:
   - `:84` Table 2 "Counts of pointing forms used" + a 21-word quote;
   - `:128` §1.2 "Motion + Path" + 24;
   - `:160` paragraph beginning "That probably explains many cultures' fear" + 22;
   - `:181` the anchor "Total Liking = …" + 15.

   The rule is "a ≤25-word quote with its location" (fleet `CORPUS.md:113-114`; `templates/round-prompt.md:51`), and the anchor *is* the location. "Split joined fragments" in those four lines is a no-op. Only **S205** (`round-53.md:109-111`) joins two source fragments under one locator ("abstract, sentences 1–2"), at 14+22=36, 16+14=30 and 13+13=26 words.
3. **The class is older than round 53, and two closures missed it.** `round-52.md:87`, S155, quotes one contiguous 31-word span from the Crossref abstract ("a reduction in the types of repair initiations; … to favor open formats"). The round-52 closure ran no quote-length scan (`round-52-verifier-spotcheck.md` has no cap check). The round-53 closure scanned only S187–S238.
4. **Neither naive rule from the brief is right on its own.**
   - "Every quoted span ≤25" passes S205: each of its fragments is ≤25.
   - "No two spans joined by '; '" flags four short, harmless joins: S184 `:32` (6+9), S186 `:34` (15+8), S201 `:88` (8+9) and S221 `:142` (2+3+2).

   The unit that matches the rule's text is **the located quote**: every quoted span under one locator, ≤25 words in total, with locator anchors excluded.
5. **Residual tradeoff (for the L1, not fixable by this check).** S205's three lines together quote six consecutive sentences of one publisher abstract, 92 words. Splitting them into six separately located quotes would pass any per-locator check and still reproduce nearly the whole abstract. Neither the cap nor this check bounds the total per row.

## Proposed `## Mistakes` row (the L1 assigns the id)

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R54-M? | provenance (quote cap). A Gate line's located quote exceeds the 25-word cap. In round 52 it was one 31-word span (S155). In round 53 it was two abstract fragments joined under one locator (S205, three lines, 26–36 words). The cap's unit was never defined, so the round-53 closure's scan listed 7 lines where its own metric gives 12, and it routed four lines that hold one quote plus a locator anchor | `corpus/lessons/round-52.md:87`; `corpus/lessons/round-53.md:109-111`; `corpus/lessons/round-53-verifier-spotcheck.md:149`, `:175` | none. The cap lives only in fleet `CORPUS.md:113-114`, its source `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:47` (same wording, no unit defined) and `templates/round-prompt.md:51`; no QUALITY criterion or lane tool reads Gate lines. The round-53 L1 trimmed one 32-word quote by hand (`round-53.md:38`), a span-level check only. The round-52 closure did not scan, and the round-53 closure scanned S187–S238 with no stated unit | a record tool (proposed `tools/check-gate-quotes.py`, below) run on the round lesson before the records commit. It fixes the unit: a located quote is every quoted span under one locator, at most 25 words in total, and a quoted span followed by `:` is the locator's anchor, not the quote. Shown able to fail: `round-53.md` gives 3 findings (S205 ×3), exit 1; `round-52.md` gives 1 (S155), exit 1; the repaired copies of both give 0, exit 0; controls pass 14/14. Rounds 49–51 give 0 findings. Not covered: cumulative quotation per row (item 5 above) |

Routing correction for the round-53 Gate errata: S205 → split into separately located quotes (one per abstract sentence, or cut). S155 (round 52) → cut to ≤25 words. S200, S214, S224 and S236 → no change, record them as "anchor, not quote".

**Duplicate authority:** sibling seat `ExecGateQuoteCheck` was assigned a checker for the same routed defect. The L1 should land exactly one tool and diff the two seats' outputs on `round-52.md` and `round-53.md` before choosing.

## The check (scratch only, not landed)

`/fast/scratch/hyaku/kotodama-r54-a2/CriticMistakeMining/check_gate_quotes.py`, sha256 `5b7e3fdb529a23ff05d84082ad50fa10d1861eb887e6bef1b3e02a6eba697577`:

```python
#!/usr/bin/env python3
"""Check the quoted words in a lesson's `## Gate` lines against the 25-word cap.

Unit: a located quote is every quoted span that sits under one locator. Spans joined
only by punctuation (`;`, `/`, `,`, `…`, dashes) or a bare `and`/`or` share a locator. A quoted
span followed by `:` (or `):`) is part of the locator (a heading or paragraph anchor),
not the quote.

Findings (exit 1):
  SPAN  one quoted span over 25 words
  JOIN  two or more spans joined under one locator, over 25 words together
Info (no exit effect):
  LINE  every quoted word on the line, anchors included, over 25 (the round-53 closure's metric)
  JOINED_SHORT  spans joined under one locator, 25 words or fewer together
"""
import re
import sys

CAP = 25
OPEN_CLOSE = {'"': '"', '“': '”', '‘': '’'}
WORD = re.compile(r"[^\W_]", re.UNICODE)
JOINER = re.compile(r"[\s;,/….–—-]*(?:\b(?:and|or)\b)?[\s;,/….–—-]*")


def words(text):
    return sum(1 for tok in text.split() if WORD.search(tok))


def spans(text):
    out, i = [], 0
    while i < len(text):
        ch = text[i]
        if ch in OPEN_CLOSE:
            close = OPEN_CLOSE[ch]
            j = i + 1
            while j < len(text):
                if text[j] == close and not (close == '’' and j + 1 < len(text) and text[j + 1].isalpha()):
                    break
                j += 1
            if j < len(text):
                out.append((i, j + 1, text[i + 1:j]))
                i = j + 1
                continue
        i += 1
    return out


def gate_lines(path):
    in_gate = False
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            if line.startswith("## "):
                in_gate = line.strip() == "## Gate"
                continue
            if in_gate and re.match(r"- S\d{3}\b", line):
                yield n, line.rstrip("\n")


def evidence(line):
    m = re.search(r"\b(accessed|re-opened|attempted)\b", line)
    start = m.start() if m else 0
    end = line.find(" Grounds:", start)
    return line[start:] if end < 0 else line[start:end]


def check(path):
    findings, info = [], []
    for n, line in gate_lines(path):
        ev = evidence(line)
        sp = spans(ev)
        sid = line[2:6]
        total = sum(words(t) for _, _, t in sp)
        if total > CAP:
            info.append(f"LINE {path}:{n} {sid} quoted_words={total}")
        quotes = []
        for k, (a, b, t) in enumerate(sp):
            after = ev[b:sp[k + 1][0]] if k + 1 < len(sp) else ev[b:]
            w = words(t)
            if w > CAP:
                findings.append(f"SPAN {path}:{n} {sid} words={w}")
            if not re.match(r"\)?\s*:", after):
                quotes.append((a, b, w))
        groups, cur = [], []
        for q in quotes:
            if cur and JOINER.fullmatch(ev[cur[-1][1]:q[0]]):
                cur.append(q)
            else:
                if cur:
                    groups.append(cur)
                cur = [q]
        if cur:
            groups.append(cur)
        for g in groups:
            if len(g) < 2:
                continue
            w = sum(x[2] for x in g)
            parts = "+".join(str(x[2]) for x in g)
            if w > CAP:
                findings.append(f"JOIN {path}:{n} {sid} words={w} ({parts})")
            else:
                info.append(f"JOINED_SHORT {path}:{n} {sid} words={w} ({parts})")
    return findings, info


def main(argv):
    if len(argv) < 2:
        print("usage: check_gate_quotes.py LESSON.md [...]", file=sys.stderr)
        return 2
    bad = 0
    for path in argv[1:]:
        findings, info = check(path)
        for f in findings:
            print(f)
        for i in info:
            print("info " + i)
        print(f"GATE_QUOTES {path}: {len(findings)} findings")
        bad += len(findings)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

Controls: `controls.py`, sha256 `d2d9a12f251bb5940ed8269f271581e3b77e29f67739c2f18fa056021d9f0fe3`. Each control is a one-line synthetic `## Gate` lesson, run through the checker as a subprocess:

| control | line shape | want exit |
|---|---|---|
| G-span-25 | one 25-word span | 0 |
| R-span-26 | one 26-word span | 1 (SPAN) |
| R-ellipsis-inside | 14 + `…` + 12 inside one span | 1 (SPAN) |
| R-join-semicolon / -ellipsis / -comma / -and / -curly-single / -slash / -endash | 14 + 12 joined by `; `, ` … `, `, `, ` and `, `‘…’; ‘…’`, ` / `, ` – ` | 1 (JOIN) |
| G-join-short | 12 + 13 joined by `; ` | 0 |
| G-anchor-plus-25 | §2 "6-word anchor": 25-word quote | 0 |
| G-two-locators | p. 1: 20 words. p. 2: 20 words | 0 |
| G-grounds-quote-ignored | 20-word quote, then a 20-word quote inside `Grounds:` | 0 |

The first controls run gave 13/14. A ` – ` (en dash) join escaped, so I added en and em dashes to `JOINER`; the run after the change gives 14/14.

## Runs (lane at `5757c45`, cwd the lane root; `info` lines kept for round 53, trimmed for round 52)

```
$ python3 -B $S/controls.py
ok   G-span-25: exit=0 want=0
ok   R-span-26: exit=1 want=1 SPAN
ok   R-ellipsis-inside: exit=1 want=1 SPAN
ok   R-join-semicolon: exit=1 want=1 JOIN
ok   R-join-ellipsis: exit=1 want=1 JOIN
ok   R-join-comma: exit=1 want=1 JOIN
ok   R-join-and: exit=1 want=1 JOIN
ok   R-join-curly-single: exit=1 want=1 JOIN
ok   R-join-slash: exit=1 want=1 JOIN
ok   R-join-endash: exit=1 want=1 JOIN
ok   G-join-short: exit=0 want=0
ok   G-anchor-plus-25: exit=0 want=0
ok   G-two-locators: exit=0 want=0
ok   G-grounds-quote-ignored: exit=0 want=0
CONTROLS 14/14                                   (exit 0)

$ python3 -B $S/check_gate_quotes.py corpus/lessons/round-53.md
JOIN corpus/lessons/round-53.md:109 S205 words=36 (14+22)
JOIN corpus/lessons/round-53.md:110 S205 words=30 (16+14)
JOIN corpus/lessons/round-53.md:111 S205 words=26 (13+13)
info LINE corpus/lessons/round-53.md:32 S184 quoted_words=33
info JOINED_SHORT corpus/lessons/round-53.md:32 S184 words=15 (6+9)
info LINE corpus/lessons/round-53.md:34 S186 quoted_words=26
info JOINED_SHORT corpus/lessons/round-53.md:34 S186 words=23 (15+8)
info LINE corpus/lessons/round-53.md:42 S187 quoted_words=28
info LINE corpus/lessons/round-53.md:44 S188 quoted_words=26
info LINE corpus/lessons/round-53.md:49 S189 quoted_words=28
info LINE corpus/lessons/round-53.md:58 S192 quoted_words=40
info LINE corpus/lessons/round-53.md:62 S194 quoted_words=28
info LINE corpus/lessons/round-53.md:84 S200 quoted_words=26
info JOINED_SHORT corpus/lessons/round-53.md:88 S201 words=17 (8+9)
info LINE corpus/lessons/round-53.md:109 S205 quoted_words=36
info LINE corpus/lessons/round-53.md:110 S205 quoted_words=30
info LINE corpus/lessons/round-53.md:111 S205 quoted_words=26
info LINE corpus/lessons/round-53.md:128 S214 quoted_words=26
info JOINED_SHORT corpus/lessons/round-53.md:142 S221 words=7 (2+3+2)
info LINE corpus/lessons/round-53.md:160 S224 quoted_words=28
info LINE corpus/lessons/round-53.md:181 S236 quoted_words=26
GATE_QUOTES corpus/lessons/round-53.md: 3 findings          (exit 1)

$ python3 -B $S/check_gate_quotes.py corpus/lessons/round-52.md
SPAN corpus/lessons/round-52.md:87 S155 words=31
info LINE … (S096:34 41, S139:59 26, S140:66 27, S142:68 34, S155:87 31, S159:94 30, S164:99 29, S168:103 26)
info JOINED_SHORT corpus/lessons/round-52.md:34 S096 words=21 (9+12)
GATE_QUOTES corpus/lessons/round-52.md: 1 findings          (exit 1)

$ python3 -B $S/check_gate_quotes.py $S/round-53-fixed.md   # S205 lines split, one located quote per sentence
GATE_QUOTES …/round-53-fixed.md: 0 findings                 (exit 0)
$ python3 -B $S/check_gate_quotes.py $S/round-52-fixed.md   # S155 cut to its third clause
GATE_QUOTES …/round-52-fixed.md: 0 findings                 (exit 0)
$ for r in 49 50 51: python3 -B $S/check_gate_quotes.py corpus/lessons/round-$r.md
GATE_QUOTES corpus/lessons/round-49.md: 0 findings          (exit 0)
GATE_QUOTES corpus/lessons/round-50.md: 0 findings          (exit 0)
GATE_QUOTES corpus/lessons/round-51.md: 0 findings          (exit 0)
```

Parse coverage: Gate lines and quoted spans read per lesson: round 49, 47 and 52; round 50, 23 and 25; round 51, 54 and 81; round 52, 84 and 114; round 53, 147 and 198.

Hand checks: I counted S155 (31), S187 `:42` (23-word quote plus a 5-word anchor), S200 `:84` (21 tokens, with `/` not counted) and the S205 fragments word by word, and they agree with the tool.

## Known limits of the check (for the L1's landing decision)

- Joins worded in prose ("then", "and later") are not treated as joined, so two such fragments escape JOIN. Each span still faces SPAN.
- Straight single quotes are not delimiters, because the lesson text uses them as apostrophes. A quote written only in `'…'` is not read.
- The anchor exemption counts a span followed by `:` as locator text. A 25-word anchor plus a 25-word quote passes. Anchors still face SPAN.
- It reads only `- S###` bullets under `## Gate`. Errata or teaches cells elsewhere are not checked. The round-52 S185 teaches cell (27 words, noted at `round-53.md:33`) lives in `SOURCES.md` and is out of reach.
- It does not bound the total quoted per row (counterexample 5).

## Incidental (not in scope; for the L1's errata pass)

- `round-53.md:158`, S223: the URL reads `item_762562_16` while the row's other twelve Gate lines read `item_762562_18`.

## Impacted axes

- **Calibration:** the closure's 7-line count is not reproducible (12 under its own metric, 3 under the rule's unit), and the routed list over-routes four rows.
- **Coverage:** none directly. The tool is a record, not a claim.

## Unrun checks

- I did not run sibling `ExecGateQuoteCheck`'s tool or compare our outputs.
- I did not re-open S205's or S155's sources. Word counts are taken from the lesson bytes, not from the publisher pages.
- No lane gate was run, and nothing was written outside my scratch directory and this report.
