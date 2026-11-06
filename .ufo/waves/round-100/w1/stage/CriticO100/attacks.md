# CriticO100 — adversarial attack on `tools/check-table-support.py` (claim O, round 100)

- Tool tested: `tools/check-table-support.py` sha256 `3ad56147dcf95ef02a3f5e0109a870065b80351c2dd4db4218abd78d5b8023a4`
  (31835 B, mtime 2026-11-06 08:48:25; unchanged across every run below). An earlier build
  `271c42fa…` (08:45:23) carried the A10 defect; it was fixed after `EARLY.md` and re-tested here.
- Second opinion / oracle: `reports/round-100/controls/feasibility/table_support_ref.py` sha256
  `24fd73f4b89af8450ae3f2ce56b39b53f20574bec99b3c7d0e436d12782889c1` (the L1's implementation,
  pinned by battery100 28/28). Never edited.
- Contract: `reports/round-100/claims.json` claims.O.contract (frozen). Never edited.
- Driver: `stage/CriticO100/attacks_critic100.py`; fixtures under
  `/fast/scratch/hyaku/kotodama-r100/CriticO100/classes/`. Attack seat: no repair, no driver/pin edit.

Method: the contract-expected verdict for each class was fixed from the contract text before the run;
the tool and the pinned ref were then run on identical bytes. A tool/ref disagreement is reported
separately from a contract mismatch. `scoped_tables` is asserted wherever a table must be seen, so a
silently skipped table cannot masquerade as "clean".

## Tally

```
CRITIC-O100 classes=25 ok=22 overrefusal=0 falsegreen=0 gap=3 traceback=0
SWEEP files=271 evidence=22 rc0=270 rc1=1 rc2=0 rcother=0 traceback=0 jsonbad=0 diverge=0 scoped_total=1
```

Driver rc 0; sweep sub-run rc 0. No tool/ref divergence in any class or in any of the 271 real
entries.

## Attack table

Benign set — contract expects CLEAN (rc 0, no findings, table scoped):

| id | recipe (bytes) | expected | observed | verdict |
|---|---|---|---|---|
| B1 | separator `\|---\|:---\|:--:\|` | rc0, scoped 1 | rc0, scoped 1 | OK |
| B2 | cell `**singer** receives [gifts](x) &amp; `rewards`` | rc0 | rc0 | OK |
| B3 | every line CRLF | rc0, scoped 1 | rc0, scoped 1 | OK |
| B4 | `   ` appended to every line | rc0, scoped 1 | rc0, scoped 1 | OK |
| B5 | two leading spaces on every table pipe | rc0, scoped 1 | rc0, scoped 1 | OK |
| B6 | one binding line carrying S9001 and S9002 | rc0 | rc0 | OK |
| B7 | label `Oríkì`, binding line says `oriki` | rc0 | rc0 | OK |
| B8 | caption `Each row is a recorded case.` (singular) | rc0, scoped 1 | rc0, scoped 1 | OK |
| B9 | scoped table + second unscoped table in the file | rc0, scoped 1 | rc0, scoped 1 | OK |
| B10 | entry with no tables | rc0, scoped 0 | rc0, scoped 0 | OK |

Attack set — contract expects FLAGGED:

| id | recipe (bytes) | expected | observed | verdict |
|---|---|---|---|---|
| A1 | capture `court` +200 filler +`singer` +200 +`receives` +200 +`gifts`; cell `singer receives gifts` | UNSUPPORTED-CELL Court/singer, best 1/3 | rc1, same, best/total 1/3 | OK |
| A2 | Court row cites S9001; cell `leader calls each line` exists only in the River row's S9002 | UNSUPPORTED-CELL Court/practice only | rc1, exactly that | OK |
| A3 | binding line `The Court row reports the court.` (no S-id, no path) | UNBOUND-ROW Court | rc1, same | OK |
| A4 | row, blank, `Notes without ids.`, blank, then the S9001 binding line | UNBOUND-ROW Court | rc1, same | OK |
| A5 | binding lines cite S9001 and S9999 (no capture) | NO-CAPTURE S9999 only | rc1, same | OK |
| A6 | `x/ref.md:99-120` in a 2-line support file | UNSUPPORTED-CELL Loom/practice, best 0/3 | rc1, same, best/total 0/3 | OK |
| A7 | trailing spaces + `singer receives zebra quantum` | UNSUPPORTED-CELL Court/reward, words [quantum,zebra] | rc1, same | OK |
| A8 | leading spaces + same unsupported cell | same | rc1, same | OK |
| A9 | CRLF + same unsupported cell | same | rc1, same | OK |
| A10 | evidence dir contains a **directory** named `S9001.txt`; binding cites S9001 and S9002 | NO-CAPTURE S9001, rc 1 | rc1, `[('NO-CAPTURE','S9001')]` (build `271c42fa` returned rc 2; fixed) | OK |
| A11 | supported cell `[singer](https://example.org/wiki/Singer) receives gifts` | flagged (URL tokens are content) | rc1, UNSUPPORTED-CELL Court/singer | OK (contract measures badly — residual 2) |
| A12 | label `Court drums`, binding line `The drums row ...` (S9004) | clean | rc0 | OK (contract measures badly — residual 3) |

Contract probes (contract silent or ambiguous):

| id | recipe | contract | observed | verdict |
|---|---|---|---|---|
| G1 | table inside a ` ``` ` fence whose caption line sits inside the fence | silent on fences | rc1, UNBOUND-ROW Court (ref identical) | CONTRACT-GAP |
| G2 | caption is the heading `### Recorded cases` | caption defined as non-heading paragraph → scoped 0 | rc0, scoped 0 | CONTRACT-GAP |
| G3 | GFM table without outer pipes (`tradition \| singer` / `--- \| ---`) | "a markdown table" undefined for this form | rc0, scoped 0 | CONTRACT-GAP |

A10 was a confirmed violation on build `271c42fa…` (rc 2 `TABLE_SUPPORT_ERROR capture unreadable:
S9001` where the contract requires NO-CAPTURE at rc 1; recipe in `stage/CriticO100/EARLY.md`). The
`blocked = os.path.exists(p)` branch was removed in `3ad56147…` and A10 now returns rc 1 with
NO-CAPTURE S9001, matching the ref. The remaining `check()` divergence from the ref is only OSError
wrapping for unreadable capture/support files (contract silent -> gap, not violation); `main` wraps
all exceptions into rc 2. AST diff: `fold toks stem content cells label_words tables window_best`
are byte-identical to the ref. battery100 never creates a non-file capture, so O2/O3/O4 are
unaffected.

## Robustness sweep (real corpus)

Command (driver `--sweep`, same bytes as the assigned form):

```
python3 -B tools/check-table-support.py --entry <each of 271 corpus/knowledge/**/*.md> --json \
  --root <lane> $(for d in reports/round-*/evidence; do printf -- '--evidence %s ' "$d"; done)
```

Result: `files=271 evidence=22 rc0=270 rc1=1 rc2=0 rcother=0 traceback=0 jsonbad=0 diverge=0
scoped_total=1`. No traceback, no rc outside 0/1/2, every stdout parsed as JSON, and the tool's
findings/scoped set equals the ref on every file. The single rc 1 file is
`corpus/knowledge/linguistics/praise-poetry-panegyric.md`.

## Real-entry evidence (the only live table)

`praise-poetry-panegyric.md`: scoped 1, **21 findings over 36 non-label cells (58%)**. The table has
9 data rows x 5 columns; every row is bound and every finding is UNSUPPORTED-CELL. Several are
near-misses: `Southern Bantu court / singer and office` best 4 of 6, `patron and reward` best 4 of 6
— 4*4 = 16 < 18, so a two-thirds-supported cell is refused. This is the contract's lexical threshold
working as frozen, not a tool defect; it is the live operability cost of residual 1.

R99-M2 replay (independent of the executor's O3): copy the real entry to scratch, replace the Yoruba
limit cell with `titles are public property, so any drummer who knows them can assemble the praise`,
run both with the same 22 evidence dirs and `--root`:

```
actual rc=1 findings=21; forged rc=1 findings=22
FORGED-MINUS-ACTUAL [('UNSUPPORTED-CELL', 'Yoruba', 'limit on the praise')]
ACTUAL-MINUS-FORGED []
```

The historical defect is caught exactly; no false green on the R99-M2 case.

## Three most dangerous residuals of the contract (routed to a later round; not implemented)

1. **Paraphrase over-refusal at the 3/4 threshold.** Live: the only real scoped table yields 21/36
   findings, including cells at 4/6 support. Fix: window over the concatenation of the row's *own*
   bound support texts (cross-row isolation, which F6 tests, is preserved) or use `best*2 >= total`.
2. **Markup and URL tokens counted as content.** `[singer](https://example.org/wiki/Singer)` adds
   `https example wiki` to `total`, so a correctly supported cell is refused; 102 corpus table rows
   already contain `](`. Fix: strip link targets, decode HTML entities and drop inline-code markers
   before tokenizing.
3. **Any-token label binding.** A multi-token label (`Court drums`) binds a source mentioning only
   one token (`drums`), so a cell can borrow support from a source about a different aspect of the
   row and pass clean (A12). Fix: require every non-generic label token (or the longest token) to
   appear in the binding line.

Secondary detection gaps (not in the top three): G1 fenced example tables are scoped and refused;
G2 a heading caption hides a table; G3 a GFM table without outer pipes is invisible (0 occurrences
in the current corpus: 1618 leading-pipe tables, 0 no-outer-pipe separator rows). Any of these
becomes dangerous the moment an entry uses the form; all three are silent except G1.

## Reproduction

```
python3 -B stage/CriticO100/attacks_critic100.py --work /fast/scratch/hyaku/kotodama-r100/CriticO100/classes
  -> 25 CLASS lines + CRITIC-O100 tally, rc 0
python3 -B stage/CriticO100/attacks_critic100.py --only B10 --sweep
  -> SWEEP line above, rc 0
```

Corpus exposure counts (rc 0): 271 files, 262 with `^|` lines, 1618 leading-pipe tables, 0
no-outer-pipe separator rows, 102 table rows containing `](`, 12 files with fences, 3 `recorded case`
mentions.
