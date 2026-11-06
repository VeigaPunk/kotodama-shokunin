# CriticO100 — round 100 attack report (claim O, table-cell support checker)

Attack seat only: no repair, no edit of the tool, battery, pins, drivers, claims or controls. The
tool changed twice under me; every number below is pinned to the bytes named.

- Tool: `tools/check-table-support.py` sha256 `3ad56147dcf95ef02a3f5e0109a870065b80351c2dd4db4218abd78d5b8023a4`
  (31835 B, mtime 2026-11-06 08:48:25). Earlier builds tested: `fde6d992…` (08:42), `271c42fa…`
  (08:45:23, carried the A10 defect).
- Ref oracle: `reports/round-100/controls/feasibility/table_support_ref.py` sha256
  `24fd73f4b89af8450ae3f2ce56b39b53f20574bec99b3c7d0e436d12782889c1` (read-only, never edited).
- Contract: `reports/round-100/claims.json` claims.O.contract (frozen, read-only).
- Driver: `stage/CriticO100/attacks_critic100.py`. Full attack table: `stage/CriticO100/attacks.md`.
  EARLY note: `stage/CriticO100/EARLY.md` (resolved).

## Tallies (commands and rc)

```
python3 -B stage/CriticO100/attacks_critic100.py --work /fast/scratch/hyaku/kotodama-r100/CriticO100/classes --sweep
  rc=0  CRITIC-O100 classes=25 ok=22 overrefusal=0 falsegreen=0 gap=3 traceback=0
        SWEEP files=271 evidence=22 rc0=270 rc1=1 rc2=0 rcother=0 traceback=0 jsonbad=0 diverge=0 scoped_total=1

python3 -B stage/CriticO100/attacks_critic100.py --only B10 --sweep
  rc=0  (sweep alone; no traceback, no rc outside 0/1/2, every stdout parsed as JSON)
```

The sweep is the assigned robustness form: every `corpus/knowledge/**/*.md` (271) with `--root` and
all 22 `reports/round-*/evidence` dirs, `--json`. The tool's findings/scoped set equals the pinned
ref on every file (diverge=0). The single rc 1 file is
`corpus/knowledge/linguistics/praise-poetry-panegyric.md`.

## Findings

1. **Contract violation, confirmed then fixed (A10).** On build `271c42fa…`, an evidence dir holding
   a *directory* named `S9001.txt` made `check()` raise `ToolError` -> rc 2
   `TABLE_SUPPORT_ERROR capture unreadable: S9001`, while claims.O.contract requires
   `NO-CAPTURE {sid}` at rc 1 (the rc-2 list is exhaustive: missing/non-UTF-8 entry, missing
   evidence dir, no --evidence). Recipe and 4-line cause in `EARLY.md`; messaged to
   ExecTableSupport100; the `blocked = os.path.exists(p)` branch is gone in `3ad56147…` and A10 now
   returns rc 1 `[('NO-CAPTURE','S9001')]`, matching the ref. Remaining divergence from the ref is
   only OSError wrapping for unreadable capture/support files (contract silent -> gap). battery100
   never creates a non-file capture, so O2/O3/O4 were unaffected either way.

2. **Real-entry over-refusal (contract-level, live).** The only real scoped table
   (`praise-poetry-panegyric.md`, 9 rows x 5 cols) yields **21 findings over 36 non-label cells
   (58%)**; all are UNSUPPORTED-CELL, several at 4/6 support (4*4=16 < 18). The tool matches the
   contract and the ref exactly; this is the frozen 3/4 lexical threshold refusing paraphrase.
   Command: `python3 -B tools/check-table-support.py --entry corpus/knowledge/linguistics/praise-poetry-panegyric.md
   $(for d in reports/round-*/evidence; do printf -- '--evidence %s ' "$d"; done) --root . --json`
   -> rc 1, scoped 1, findings 21.

3. **R99-M2 replay is exact (independent of the executor's O3).** Copy the real entry to scratch,
   replace the Yoruba limit cell with the forged sentence, run both with the same 22 evidence dirs:
   actual rc 1 / 21 findings, forged rc 1 / 22 findings,
   `FORGED-MINUS-ACTUAL [('UNSUPPORTED-CELL','Yoruba','limit on the praise')]`,
   `ACTUAL-MINUS-FORGED []`. No false green on the historical defect.

4. **Benign set all clean, attack set all flagged.** 10/10 benign classes (alignment colons,
   emphasis/code/`[link](x)`/`&amp;`, CRLF, trailing spaces, leading spaces, two ids on one binding
   line, `Oríkì`/`oriki`, singular `recorded case`, second unscoped table, no tables) return rc 0
   with the table scoped; the 6 assigned attack classes plus 3 whitespace negative controls return
   the contract's exact finding set, including `best/total` and `words`. `scoped_tables` is asserted
   on every class, so a silently skipped table cannot read as clean.

5. **Contract gaps observed (not tool defects).** G1: a table inside a ``` fence with a matching
   caption line inside the fence is scoped and refused (UNBOUND-ROW); the contract never mentions
   fences. G2: a heading caption (`### Recorded cases`) is excluded by definition -> scoped 0, rc 0.
   G3: a GFM table without outer pipes is not detected -> scoped 0, rc 0 (0 live occurrences: 1618
   leading-pipe tables, 0 no-outer-pipe separator rows in the corpus).

## Three most dangerous residuals of the contract (routed to a later round; not implemented)

1. **Paraphrase over-refusal at the 3/4 threshold** — live 21/36 on the only real table. Fix: window
   over the concatenation of the row's *own* bound support texts (cross-row isolation, which F6
   tests, is preserved) or use `best*2 >= total`.
2. **Markup/URL tokens counted as content** — `[singer](https://example.org/wiki/Singer)` adds
   `https example wiki` to `total`, so a supported cell is refused; 102 corpus table rows already
   contain `](`. Fix: strip link targets, decode HTML entities and drop inline-code markers before
   tokenizing.
3. **Any-token label binding** — label `Court drums` is bound by a line mentioning only `drums`, so a
   cell can borrow support from a source about a different aspect of the row and pass clean (A12).
   Fix: require every non-generic label token (or the longest token) to appear in the binding line.

## Corpus exposure counts (rc 0)

271 files; 262 with `^|` lines; 1618 leading-pipe tables; 0 no-outer-pipe separator rows; 102 table
rows containing `](`; 12 files with fences; 3 `recorded case` mentions.

## Tooling, blockers, writes

- Tools installed/upgraded: none.
- Blockers: none. ExecTableSupport100's TOOL-READY was present; the tool changed twice and was
  re-tested each time.
- Files written: `stage/CriticO100/attacks_critic100.py`, `attacks.md`, `EARLY.md`, this report,
  `DONE`. Scratch `/fast/scratch/hyaku/kotodama-r100/CriticO100` deleted before yield.
- Nothing committed; no repo file outside my stage touched.
