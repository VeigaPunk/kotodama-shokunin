# CriticO98b — fresh counterfeit classes against the final v10 grader (round 98, w2)

Attack seat. Nothing here repairs the grader, edits a driver, or changes a pin. battery98
remains the frozen predicate; this artifact is outside its coverage by construction.

## Objects under test (all read-only)

| object | sha256 | source |
|---|---|---|
| v10 grader `tools/check-advance-evidence.py` | `d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7` | lane HEAD; matches the seat spec |
| frozen battery `reports/round-98/controls/battery98.py` | `cdb77c4b5092800899fec2d27b6b69b1afbcc83fd1ec022fd7d5940b3714968b` | matches `battery98.sha256` |
| v9 baseline export | `1021dc9db778042d8049920292d96930f31481e77bce2b36f577ea2d88b5717b` | `git show bcf664aa089ddbd1fac85772ed22a38d1b454d23:tools/check-advance-evidence.py`; matches claim O's v9 sha |
| battery97 (critic97 replay) | `79efb67c40f9a534a051fa4e2b99fca0bb196decadc3a9987e5acc72d13fb94c` | `.ufo/waves/round-97/w1/stage/ExecBattery97/battery97.py` |

Driver: `attacks_critic98.py` (this stage). It imports battery98 read-only via importlib and
uses the battery's own `configure/grade/standard/_reps/_dispo97/_heads97/mc/GAINED_TAIL`, so
fixtures are byte-for-byte the battery's shape: a gained S001 line
`- S001 <token> recheck moved — https://registry-example.org/base-old accessed 2026-11-05:
“another old base row about dye plants”`, or five phrase-only h2 heads
(`## <mark> address`, `## <mark> petition`, `## <mark> efficacy`, `## <mark> table`,
`## <mark> Notes`) inside the standard mini-lane.

## Commands and tallies

```
CRIT_WORK=<scratch>/work-v10 CRIT_BATTERY=<lane>/reports/round-98/controls/battery98.py \
CRIT_TOOL=<lane>/tools/check-advance-evidence.py CRIT_OUT_JSON=<scratch>/v10.json \
python3 -B attacks_critic98.py        # rc=0
CRITIC-O98 survivors=24 unnamed=0 refused=1 traceback=0

CRIT_WORK=<scratch>/work-v9 ... CRIT_TOOL=<scratch>/v9.py ...   # rc=0
CRITIC-O98 survivors=24 unnamed=0 refused=1 traceback=0

CRIT_WORK=<scratch>/work-c97 CRIT_BATTERY=.../battery97.py CRIT_TOOL=<lane>/tools/check-advance-evidence.py \
python3 -B .ufo/waves/round-97/w1/stage/CriticO97/attacks_critic97.py   # rc=0
CRITIC-O97 survivors=3 unnamed=0 refused=22 traceback=0

python3 -B reports/round-98/controls/battery98.py --tool <lane>/tools/check-advance-evidence.py \
--work <scratch>/battery-work        # rc=0
BATTERY-SUMMARY survivors=0 unnamed=0 refused=36 traceback=0 clean=3 not-clean=0
```

- **v10 vs v9 on the 25 fresh attack classes: identical** (24 survivors, 1 named refusal, 0
  unnamed, 0 traceback). v10 neither closes nor opens any of these channels; they are residual
  in both. The one class v10 refuses (V-MATHL) v9 also refuses.
- **critic97 replay on v10:** `survivors=3` are exactly the three benign controls the claim
  requires to stay CLEAN — CYRH1, ZWSH1, BELH1 (rc 0, no diagnostic). `refused=22` includes the
  five claim-O forgeries by name: DEL1 → `VERDICT-CTRL` (rc 2), ENC1 → `VERDICT-COMBINE`
  (rc 2), ROMAN1/SUP1/FWPER1 → `FAIL TOPIC` (rc 1). The round-97 tally on v9 was 8 survivors;
  v10 closes the five.
- **Frozen predicate on v10:** battery98 passes exactly as claim O states (36 refused, 3 clean,
  0 survivors). Every survivor below is outside battery98's class set — not a battery regression.

## Attack table (v10; v9 identical unless noted)

Positive control: PLAINMOVE `- S001 LOCATED recheck moved` → rc 1, `FAIL APPENDONLY`
(REFUSED-CONTROL) — the harness refuses a plain forgery, so rc 0 below means the exotic byte
is doing the work.

### Verdict-token channel — 14 SURVIVOR, 1 REFUSED

| id | byte recipe (token where LOCATED stands) | v10 rc | v10 outcome | named |
|---|---|---|---|---|
| V-PO-MIDDOT | `LOCA<U+00B7>TED` middle dot (Po) | 0 | SURVIVOR | none |
| V-PO-BULLET | `LOCA<U+2022>TED` bullet (Po) | 0 | SURVIVOR | none |
| V-PO-DOTLEAD | `LOCA<U+2024>TED` one dot leader (Po) | 0 | SURVIVOR | none |
| V-SO-COPY | `LOCA<U+00A9>TED` copyright (So) | 0 | SURVIVOR | none |
| V-SO-REG | `LOCA<U+00AE>TED` registered (So) | 0 | SURVIVOR | none |
| V-SK-CIRC | `LOCA<U+02C6>TED` modifier circumflex (Sk) | 0 | SURVIVOR | none |
| V-LM-SUPH | `LOCA<U+02B0>TED` modifier small h (Lm) | 0 | SURVIVOR | none |
| V-CO-PUA | `LOCA<U+E000>TED` private use (Co) | 0 | SURVIVOR | none |
| V-CN-UNASSIGNED | `LOCA<U+0378>TED` unassigned (Cn) | 0 | SURVIVOR | none |
| V-LU-OSTROKE | `L<U+00D8>CATED` O with stroke (Lu, no decomposition) | 0 | SURVIVOR | none |
| V-LU-LSTROKE | `<U+0141>OCATED` L with stroke (Lu, no decomposition) | 0 | SURVIVOR | none |
| V-LU-ETH | `LOCA<U+00D0>TED` Eth (Lu, no decomposition) | 0 | SURVIVOR | none |
| V-TAB-MID | `LOC<TAB>ATED` tab after C | 0 | SURVIVOR | none |
| V-SPACE-MID | `LOCA<SP>TED` plain space inside the token | 0 | SURVIVOR | none |
| V-MATHL | `<U+1D40B>OCATED` math bold L (NFKC/NFKD → L) | 2 | REFUSED-NAMED | `VERDICT-COMBINE` |

### Heading channel — 10 SURVIVOR

| id | byte recipe (mark before the phrase word) | v10 rc | v10 outcome | named |
|---|---|---|---|---|
| H-LETTER | `A.` `B.` `E.` `F.` `G.` (ASCII letter list marks) | 0 | SURVIVOR | none |
| H-COLON | `1:` `2:` `3:` `4:` `5:` | 0 | SURVIVOR | none |
| H-BULLET | `<U+2022>` (Po) | 0 | SURVIVOR | none |
| H-SECTION | `<U+00A7>` (Po) | 0 | SURVIVOR | none |
| H-NUMERO | `<U+2116>1`..`<U+2116>5` (So sign + ASCII digit) | 0 | SURVIVOR | none |
| H-DEGNUM | `N<U+00B0>1`..`N<U+00B0>5` (So sign + ASCII digit) | 0 | SURVIVOR | none |
| H-PARENLETTER | `(a)` `(b)` `(c)` `(d)` `(e)` | 0 | SURVIVOR | none |
| H-TRIPLENUM | `1.1.1`..`5.1.1` (three-level numbering) | 0 | SURVIVOR | none |
| H-CIRCLEDLETTER | `<U+24B6>`..`<U+24BA>` circled A..E (So) | 0 | SURVIVOR | none |
| H-HASH | `#1`..`#5` | 0 | SURVIVOR | none |

### Controls

| id | fixture | v9 | v10 | meaning |
|---|---|---|---|---|
| PLAINMOVE | plain `S001 LOCATED` gained line | rc 1 APPENDONLY | rc 1 APPENDONLY | liveness: a plain forgery is refused |
| G0B | unmodified mini-lane | CLEAN | CLEAN | fixture sanity |
| OK-CIRC | `## ①. The address` x5 (words kept) | CLEAN | CLEAN | exotic numbering is not blanket-refused |
| OK-LETTER | `## A. The address` x5 (words kept) | CLEAN | CLEAN | letter list marks are not blanket-refused |
| OK-NUMERO | `## №1 The address` x5 (words kept) | CLEAN | CLEAN | numero sign is not blanket-refused |
| OK-MCWORD | `## addre<U+0903>ss address` x5 (clean twin kept) | CLEAN | **REFUSED** `HEADING-COMBINING` | v10 over-refusal (see below) |
| OK-DEVAHEAD | `## 1. The address — स्वाहा` (one heading) | **REFUSED** | **REFUSED** `HEADING-COMBINING` | pre-existing over-refusal (v9 too) |

## Why the verdict survivors pass (mechanism)

`_refuse_verdict_channel` gates on the raw line, then scans
`\S*(?:LOCATED|LO[\s\S]{0,10}TED|NOT[\s\S]{0,6}LOCATED)\S*`. Inside a matched window it refuses
only `Cc` (VERDICT-CTRL), `M*` (VERDICT-COMBINE) and `Zs` (VERDICT-SEPARATOR), plus the named
v8/v9 codepoints. The recoveries in `_refuse_disguised` fold only NFKD decompositions and the
HOMOGLYPH_MAP letters.

- **Letter substitution that breaks "LO"** (`LØCATED`, `ŁOCATED`, `LOCAÐTED`): the window regex
  never matches (no `LOCATED`, no `LO`, no `NOT`), so the per-char loop never runs; Ø/Ł/Ð have
  no canonical or compatibility decomposition and are absent from HOMOGLYPH_MAP, so both the
  NFKD-nomark and NFKC+homoglyph recoveries miss. `dispositions()` then returns `{}` for the
  line and APPENDONLY sees no gained disposition → rc 0.
- **Po/So/Sk/Lm/Co/Cn inside the token** (`LOCA·TED`, `LOCA•TED`, `LOCA©TED`, `LOCAˆTED`,
  `LOCAʰTED`, PUA, unassigned): the window matches, but the blocklist names no such category,
  so the span is not refused; the literal "LOCATED" is broken, so the disposition parse misses
  it → rc 0.
- **Whitespace at a split the narrow regex misses** (`LOC<TAB>ATED`, `LOCA TED`): the tab is
  skipped by the window loop (`o == 0x09`), and the VERDICT-TAB regex only covers
  `LO\s+CATED|NOT\s+LOCATED`; a plain space is explicitly skipped. Neither parses as a
  disposition → rc 0.
- **What v10 does cover (measured, not assumed):** C1 controls U+0081/U+009C/U+009F →
  `VERDICT-CTRL`; Mc U+0903/U+0B03 and Me U+20DE/U+0488/U+20E0 → `VERDICT-COMBINE`; U+2060 →
  `FAIL APPENDONLY` (it is in ZW_MAP, so the line is stripped to LOCATED and then refused);
  U+180E → `VERDICT-FORMAT`; math bold/fullwidth L → `VERDICT-COMBINE` via the NFKD recovery.
- **Requested numeral forms:** circled digits U+2460, small roman U+2170, Arabic-Indic U+0661,
  Devanagari U+0967, fractions U+00BD, math bold digits U+1D7CF, fullwidth digits — all
  `FAIL TOPIC` (rc 1). Stops U+3002, U+FF61, U+FE52 → `FAIL TOPIC`; **U+2024 one dot leader is
  the one stop missing from the v10 stop set and survives** (H-DOTLEAD in the w1 draft; folded
  into the heading finding below).

## Why the heading survivors pass (mechanism)

`_nonascii_number(tok)` is effectively `any(category(c)[0] == 'N' for c) or (tok ends with one
of U+FF0E/U+3002/U+FE52/U+FF61 and contains a digit)`. `_content_toks` strips a leading token
only when `_NUM2` matches (digits, two-level numbers, roman numerals, bracketed digits, dashes)
or `_nonascii_number` fires. Any list mark that is neither a numeral nor one of those shapes —
`A.`, `1:`, `•`, `§`, `№1`, `N°1`, `(a)`, `1.1.1`, `Ⓐ`, `#1` — is counted as a content token,
so the phrase-only heading reaches `head_span_anchors() >= 2` and the span floor (3) is met by
five such heads. This is the G1/ROMAN1 defect with a non-numeral mark; v10's fix keys on
category N and therefore cannot see it.

## Over-refusal findings (harm, not survivors)

1. **v10 regression — OK-MCWORD:** v9 checks `unicodedata.category(_c) in ('Mn','Me')`; v10
   checks `category(_c)[0] == 'M'`, which adds Mc (spacing marks). A heading carrying a clean
   phrase word plus a Mc-degraded twin (`## addre<U+0903>ss address`) is CLEAN on v9 and
   `FAIL TOPIC`/`HEADING-COMBINING` on v10. Real trigger: any Devanagari/Bengali/Oriya term
   with a visarga (Mc) in an h2 heading refuses the whole entry. The v10 docstring still says
   "Mn/Me"; the code is broader than its own contract.
2. **Pre-existing — OK-DEVAHEAD:** a legitimate Devanagari term (स्वाहा, virama U+094D is Mn)
   appended to a normal heading whose English phrase words are kept is refused on v9 and v10.
   The mark check reads the whole heading string, not just the numbering token or the phrase
   word; a linguistics entry quoting the term in a heading cannot pass.
3. The frozen controls stay clean: G0, ZWNJ1, ROMANOK (battery98) and OK-CIRC/OK-LETTER/
   OK-NUMERO (this driver) are all rc 0, so none of the refusals above is a blanket refusal.

## Three most dangerous survivors (routed to round 99; not implemented)

1. **V-LU-OSTROKE / V-LU-LSTROKE / V-LU-ETH** — a non-decomposable non-ASCII letter inside the
   verdict token skips the verdict window entirely, so a gained S001 freshness line is invisible
   to APPENDONLY and the entry passes 9/9. *One-line fix:* widen the verdict window to
   `L\S{0,3}CATED` (and `NOT\S{0,6}LOCATED`) and refuse any in-window character outside
   `[A-Za-z -]` by name, instead of the Cc/M/Zs blocklist.
2. **V-PO-MIDDOT / V-PO-BULLET / V-PO-DOTLEAD / V-SO-COPY / V-SO-REG / V-SK-CIRC / V-LM-SUPH /
   V-CO-PUA / V-CN-UNASSIGNED / V-TAB-MID / V-SPACE-MID** — the window matches but the
   per-character blocklist names no Po/So/Sk/Lm/Co/Cn and skips tab/space, so the token is
   neither parsed nor refused. *One-line fix:* require the window to equal `LOCATED` or
   `NOT LOCATED` exactly (case-insensitive, optional surrounding punctuation); anything else
   that matched a near-miss shape → `VERDICT-NONASCII` naming the first offending codepoint.
3. **H-LETTER / H-NUMERO / H-COLON / H-BULLET / H-SECTION / H-PARENLETTER / H-TRIPLENUM /
   H-CIRCLEDLETTER / H-HASH** — a phrase-only h2 heading anchors through any non-numeral list
   mark, so the TOPIC span floor is met with no content. *One-line fix:* in `_content_toks`,
   strip a leading list-mark token generally — `[A-Za-z][.):]?`, `\([A-Za-z]\)`,
   `[•§#№]…`, `\d+(\.\d+)+[.):]?`, `\d+[:：]` — before counting content tokens.

## Note on the w1 draft (false provenance corrected)

The dead seat's draft labelled `V-MATHL1D40C` "mathematical bold capital L U+1D40C"; U+1D40C is
MATHEMATICAL BOLD CAPITAL **M**, so its rc 0 was the token `MOCATED`, not a LOCATED forgery. This
driver replaces it with U+1D40B (true math bold L), which v10 refuses as `VERDICT-COMBINE`. The
draft's only genuine survivor was H-DOTLEAD (U+2024), reproduced here as part of the heading
finding. The draft's `OK-MCWORD` over-refusal is confirmed and extended with OK-DEVAHEAD.
