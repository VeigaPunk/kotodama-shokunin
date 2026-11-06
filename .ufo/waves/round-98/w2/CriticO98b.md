# CriticO98b — Report (round 98, w2, attack seat)

Status: DONE. No grader/driver/pin edited; nothing committed. Full evidence: `stage/CriticO98b/attacks.md`;
driver: `stage/CriticO98b/attacks_critic98.py`. Scratch `/fast/scratch/hyaku/kotodama-r98/CriticO98b/`
deleted before yield.

## Objects (read-only)

- v10 grader sha256 `d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7` (matches spec).
- battery98 sha256 `cdb77c4b5092800899fec2d27b6b69b1afbcc83fd1ec022fd7d5940b3714968b` (matches `battery98.sha256`).
- v9 export from `bcf664aa089ddbd1fac85772ed22a38d1b454d23` sha256 `1021dc9db778042d8049920292d96930f31481e77bce2b36f577ea2d88b5717b` (matches claim O).
- battery97 sha256 `79efb67c40f9a534a051fa4e2b99fca0bb196decadc3a9987e5acc72d13fb94c`.

## Tallies (commands rc=0)

- v10, 25 fresh attack classes: `CRITIC-O98 survivors=24 unnamed=0 refused=1 traceback=0`.
- v9, same 25: `CRITIC-O98 survivors=24 unnamed=0 refused=1 traceback=0` (identical set).
- critic97 replay on v10: `CRITIC-O97 survivors=3 unnamed=0 refused=22 traceback=0`; the 3 are the
  benign controls CYRH1/ZWSH1/BELH1 (rc 0, as the claim requires). The five claim-O forgeries are
  refused by name: DEL1 `VERDICT-CTRL` (rc 2), ENC1 `VERDICT-COMBINE` (rc 2), ROMAN1/SUP1/FWPER1
  `FAIL TOPIC` (rc 1).
- Frozen predicate on v10: `BATTERY-SUMMARY survivors=0 unnamed=0 refused=36 traceback=0 clean=3
  not-clean=0` — every survivor below is outside battery98's coverage, not a battery regression.
- Positive control PLAINMOVE (plain `S001 LOCATED` gained line) rc 1 `FAIL APPENDONLY`; benign
  controls G0B/OK-CIRC/OK-LETTER/OK-NUMERO rc 0.

## Attack table (v10; v9 identical)

Verdict channel (gained S001 line; token where LOCATED stands): 14 SURVIVOR, 1 REFUSED.

| id | recipe | rc | outcome | named |
|---|---|---|---|---|
| V-PO-MIDDOT | `LOCA<U+00B7>TED` | 0 | SURVIVOR | none |
| V-PO-BULLET | `LOCA<U+2022>TED` | 0 | SURVIVOR | none |
| V-PO-DOTLEAD | `LOCA<U+2024>TED` | 0 | SURVIVOR | none |
| V-SO-COPY | `LOCA<U+00A9>TED` | 0 | SURVIVOR | none |
| V-SO-REG | `LOCA<U+00AE>TED` | 0 | SURVIVOR | none |
| V-SK-CIRC | `LOCA<U+02C6>TED` | 0 | SURVIVOR | none |
| V-LM-SUPH | `LOCA<U+02B0>TED` | 0 | SURVIVOR | none |
| V-CO-PUA | `LOCA<U+E000>TED` | 0 | SURVIVOR | none |
| V-CN-UNASSIGNED | `LOCA<U+0378>TED` | 0 | SURVIVOR | none |
| V-LU-OSTROKE | `L<U+00D8>CATED` | 0 | SURVIVOR | none |
| V-LU-LSTROKE | `<U+0141>OCATED` | 0 | SURVIVOR | none |
| V-LU-ETH | `LOCA<U+00D0>TED` | 0 | SURVIVOR | none |
| V-TAB-MID | `LOC<TAB>ATED` | 0 | SURVIVOR | none |
| V-SPACE-MID | `LOCA<SP>TED` | 0 | SURVIVOR | none |
| V-MATHL | `<U+1D40B>OCATED` | 2 | REFUSED-NAMED | `VERDICT-COMBINE` |

Heading channel (five phrase-only h2 heads): 10 SURVIVOR.

| id | mark before the phrase word | rc | outcome | named |
|---|---|---|---|---|
| H-LETTER | `A.` `B.` `E.` `F.` `G.` | 0 | SURVIVOR | none |
| H-COLON | `1:`..`5:` | 0 | SURVIVOR | none |
| H-BULLET | `<U+2022>` | 0 | SURVIVOR | none |
| H-SECTION | `<U+00A7>` | 0 | SURVIVOR | none |
| H-NUMERO | `<U+2116>1`..`<U+2116>5` | 0 | SURVIVOR | none |
| H-DEGNUM | `N<U+00B0>1`..`N<U+00B0>5` | 0 | SURVIVOR | none |
| H-PARENLETTER | `(a)`..`(e)` | 0 | SURVIVOR | none |
| H-TRIPLENUM | `1.1.1`..`5.1.1` | 0 | SURVIVOR | none |
| H-CIRCLEDLETTER | `<U+24B6>`..`<U+24BA>` | 0 | SURVIVOR | none |
| H-HASH | `#1`..`#5` | 0 | SURVIVOR | none |

Requested channels that v10 DOES close (measured): C1 controls U+0081/U+009C/U+009F → `VERDICT-CTRL`;
Mc U+0903/U+0B03 and Me U+20DE/U+0488/U+20E0 → `VERDICT-COMBINE`; U+2060 → `FAIL APPENDONLY`;
U+180E → `VERDICT-FORMAT`; circled digits/small roman/Arabic-Indic/Devanagari/fractions/math bold
digits → `FAIL TOPIC`; stops U+3002/U+FF61/U+FE52 → `FAIL TOPIC`; a lone combining mark after the
number → `HEADING-COMBINING`. The one requested stop that survives is U+2024 (one dot leader).

## Mechanisms

- Verdict: the window regex `\S*(?:LOCATED|LO[\s\S]{0,10}TED|NOT[\s\S]{0,6}LOCATED)\S*` misses any
  token whose "LO" is broken by a letter substitution (`LØCATED`, `ŁOCATED`, `LOCAÐTED`); Ø/Ł/Ð have
  no decomposition and are absent from HOMOGLYPH_MAP, so the NFKD/NFKC recoveries miss too. When the
  window does match, the per-char loop names only Cc/M/Zs, so Po/So/Sk/Lm/Co/Cn pass; tab is skipped
  and the VERDICT-TAB regex only covers `LO\s+CATED|NOT\s+LOCATED`; plain space is skipped. In every
  case `dispositions()` returns `{}`, APPENDONLY sees no gained line, and the entry passes 9/9.
- Heading: `_nonascii_number` keys on category N (plus four stop codepoints); `_NUM2` strips digits,
  two-level numbers, roman numerals, bracketed digits and dashes only. Any other list mark counts as
  a content token, so five phrase-only heads meet the span floor of 3.

## Over-refusal (harm)

1. v10 regression: OK-MCWORD (`## addre<U+0903>ss address` x5, clean twin kept) is CLEAN on v9 and
   `FAIL TOPIC`/`HEADING-COMBINING` on v10. v9 checks `category in ('Mn','Me')`; v10 checks
   `category[0] == 'M'`, adding Mc. Real trigger: any Devanagari/Bengali/Oriya term with a visarga
   (Mc) in an h2 heading refuses the entry. The v10 docstring still says Mn/Me.
2. Pre-existing: OK-DEVAHEAD (`## 1. The address — स्वाहा`, virama U+094D is Mn) is refused on v9 and
   v10; the mark check reads the whole heading string, not the numbering token/phrase word.
3. Frozen controls G0/ZWNJ1/ROMANOK and sentinels OK-CIRC/OK-LETTER/OK-NUMERO stay CLEAN, so no
   refusal above is blanket.

## Three most dangerous survivors (routed to round 99; not implemented)

1. `V-LU-OSTROKE`/`V-LU-LSTROKE`/`V-LU-ETH`: non-decomposable non-ASCII letters make a gained S001
   freshness line invisible (window regex never matches). Fix: widen the window to `L\S{0,3}CATED`
   and refuse any in-window char outside `[A-Za-z -]` by name (whitelist, not category blocklist).
2. `V-PO-*`/`V-SO-*`/`V-SK-*`/`V-LM-*`/`V-CO-*`/`V-CN-*`/`V-TAB-MID`/`V-SPACE-MID`: the window
   matches but the blocklist names no such category. Fix: require the window to equal `LOCATED` or
   `NOT LOCATED` exactly; any other near-miss → `VERDICT-NONASCII` naming the first offending codepoint.
3. `H-LETTER`/`H-NUMERO`/`H-COLON`/`H-BULLET`/`H-SECTION`/`H-PARENLETTER`/`H-TRIPLENUM`/
   `H-CIRCLEDLETTER`/`H-HASH`: non-numeral list marks count as heading tokens. Fix: in
   `_content_toks`, strip a leading list-mark token generally before counting content tokens.

## Correction of the w1 draft

The dead seat's `V-MATHL1D40C` was mislabelled: U+1D40C is MATHEMATICAL BOLD CAPITAL **M**, so its
rc 0 was the token `MOCATED`, not a LOCATED forgery. Replaced with U+1D40B (true math bold L), which
v10 refuses as `VERDICT-COMBINE`. The draft's only genuine survivor was H-DOTLEAD (U+2024).

## Tooling

None installed or upgraded. No pacman run. No sysctl touched. Scratch deleted before yield.
