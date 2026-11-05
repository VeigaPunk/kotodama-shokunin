# CriticO96 — fresh-counterfeit attack on grader v7 (round 96)

Summary: **v7 SURVIVORS 7 of 19 fresh classes; REFUSED-NAMED 12; UNNAMED 0; TRACEBACK 0; controls G0/ZWNJ1 CLEAN rc 0.**
Tally (driver stdout, both runs rc 0):

```
v7: CRITIC-O96 survivors=7 unnamed=0 refused=12 traceback=0
v6: CRITIC-O96 survivors=11 unnamed=0 refused=8 traceback=0
```

This is an attack seat: survivors do NOT fail claim O (the frozen predicate remains battery96's
own BATTERY-SUMMARY — battery96.py is the frozen predicate and was not edited, re-run, or
relaxed by this seat). The 7 survivors feed round 97.

## Tested in place (never copied into the lane tree)

- v7 under attack: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py`,
  sha256 `2e28a289746812b14a07a0645e568f0cee9dfb1789af6cfe6ce88f80c8f053ec` (`sha256sum`, rc 0).
- v6 do-nothing baseline: `.ufo/waves/round-96/w1/stage/ExecGraderV7/v6-base.py`,
  sha256 `f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec` (rc 0) — the v6 pin.
- Fixture machinery: `.ufo/waves/round-96/w1/stage/ExecBattery96/battery96.py`,
  sha256 `9f80f59481861b104f166a838222fcdf300e55a27fc841b5217e1980b5e91c21` (rc 0), imported
  read-only for `configure()/standard()/grade()/_reps/mc/GAINED_TAIL`; `B.b96_zwnj1()` reused
  for the ZWNJ1 control. All fixtures built under scratch only.
- Dependency: waited on `stage/ExecGraderV7/DONE` with the bounded 45x60 s loop —
  `DEP-READY after 31 polls` (depwait96, rc 0). battery96.py was read only after that.
- Driver: `stage/CriticO96/attacks_critic96.py` (this seat's stage; 19 classes + G0 + ZWNJ1).

Commands (both rc 0; counts are data):

```
S=/fast/scratch/hyaku/kotodama-r96/CriticO96
ST=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-96/w1/stage
# v7 run
CRIT_WORK=$S CRIT_BATTERY=$ST/ExecBattery96/battery96.py \
  CRIT_TOOL=/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py \
  CRIT_OUT_JSON=$S/results-critic96-v7.json python3 -B $ST/CriticO96/attacks_critic96.py   # rc 0
# v6 do-nothing baseline over the identical fixtures
CRIT_WORK=$S CRIT_BATTERY=$ST/ExecBattery96/battery96.py \
  CRIT_TOOL=$ST/ExecGraderV7/v6-base.py \
  CRIT_OUT_JSON=$S/results-critic96-v6.json python3 -B $ST/CriticO96/attacks_critic96.py   # rc 0
```

Traceback/unnamed check: `tb_classes=0` in both results JSONs (python extraction rc 0); every
`CLASS` line `traceback=no`; REFUSED-UNNAMED count 0 on both versions. GAINED_TAIL on every
forged lesson line: ` — https://registry-example.org/base-old accessed 2026-11-05: “another old
base row about dye plants”\n` (battery96's own).

## Attack table (19 fresh classes; recipe bytes verified with cat -A, rc 0)

Lesson-channel classes forge a gained S001 verdict on an old id (`- S001 <V> recheck moved` + TAIL);
heading-channel classes forge the five h2 lines (`B._reps(B.mc.body(None), ...)`). None of the 19 is
carried by battery96 (A1,B1,G1,H1,I1,J1,K1,CD1,LR1,TAB1,ID1,NUM1,RM1,NUM2,NB1,VT1,FF1,LS1,NEL1,
ANSI1,CYR1,BR1,DASH1,F1) or CriticO94/95's lists.

| id | bytes recipe (forged element) | v6 rc/outcome | v7 rc/outcome | v7 named diagnostic |
|---|---|---|---|---|
| G0 | clean control, no forgery | 0 CLEAN | 0 CLEAN | — (PASS 9/9) |
| FS1 | verdict `LOCA<U+001C>TED` | 0 SURVIVOR | 2 REFUSED | `verdict token carries a line separator (VERDICT-LINESEP)` |
| GS1 | verdict `LOCA<U+001D>TED` | 0 SURVIVOR | 2 REFUSED | `VERDICT-LINESEP` |
| RS1 | verdict `LOCA<U+001E>TED` | 0 SURVIVOR | 2 REFUSED | `VERDICT-LINESEP` |
| PS1 | verdict `LOCA<U+2029>TED` | 0 SURVIVOR | 2 REFUSED | `VERDICT-LINESEP` |
| CR1 | verdict `LOCA<U+000D>TED` (lone CR) | 0 SURVIVOR | **0 SURVIVOR** | none — PASS 9/9 |
| US1 | verdict `LOCA<U+001F>TED` (splitlines does NOT sever) | 0 SURVIVOR | **0 SURVIVOR** | none — PASS 9/9 |
| OGH1 | verdict `LOCA<U+1680>TED` (Zs, no NFKC fold) | 0 SURVIVOR | **0 SURVIVOR** | none — PASS 9/9 |
| IS1 | verdict `LOCA<U+3000>TED` (NFKC folds to space) | 0 SURVIVOR | **0 SURVIVOR** | none — PASS 9/9 |
| ZWJ1 | verdict `LOCA<U+200D>TED` (strip-set member) | 1 REFUSED | 1 REFUSED | `APPENDONLY ... S001: gained a LOCATED line not present at base` |
| MVS1 | verdict `LOCA<U+180E>TED` (Cf out-of-set) | 2 REFUSED | 2 REFUSED | `VERDICT-FORMAT` |
| ALM1 | verdict `LOCA<U+061C>TED` (Cf out-of-set) | 2 REFUSED | 2 REFUSED | `VERDICT-FORMAT` |
| FWID1 | id `S<U+FF10><U+FF10><U+FF11> LOCATED` | 1 REFUSED | 1 REFUSED | `APPENDONLY ... S００１: gained a LOCATED line ...` (names the lookalike id, not S001) |
| FWS1 | id `<U+FF33>001 LOCATED` | 2 REFUSED | 2 REFUSED | `id token carries a non-ASCII lookalike letter (ID-NONASCII)` (v6 said VERDICT-COMBINE) |
| NUL1 | verdict `LOCA<U+0000>TED` (Cc, non-severing) | 0 SURVIVOR | **0 SURVIVOR** | none — PASS 9/9 |
| CM1 | heads `## 1<U+0301>. address` / `## 2<U+0301>. petition` / `## 3<U+0301>. efficacy` / `## 4<U+0301>. table` / `## 5<U+0301>. Notes` | 0 SURVIVOR | **0 SURVIVOR** | none — PASS 9/9 |
| CMW2 | heads `## addre<U+0301>ss address` / `## petition<U+0301> petition` / `## efficac<U+0301>y efficacy` / `## tabl<U+0301>e table` / `## Notes Notes` | 0 SURVIVOR | **0 SURVIVOR** | none — PASS 9/9 |
| TABH1 | heads `## 1.<TAB>address` ... x5 | 1 REFUSED | 1 REFUSED | `TOPIC ... phrase anchors span 1 heading/table surfaces < 3` |
| VTH1 | heads `## 1.<VT>address` ... x5 (splitlines severs the h2) | 1 REFUSED | 1 REFUSED | `TOPIC ... 2 of 4 sub-topic phrases in headings/table cells` |
| ISPH1 | heads `## 1.<U+3000>address` ... x5 | 1 REFUSED | 1 REFUSED | `TOPIC ... phrase anchors span 1 heading/table surfaces < 3` |
| ZWNJ1 | battery96 ZWNJ1 control builder (cell ZWNJ) | 0 CLEAN | 0 CLEAN | — (PASS 9/9) |

v7 closed exactly four of my eleven v6 survivors (FS1, GS1, RS1, PS1 via the new VERDICT-LINESEP
arm) and improved FWS1's naming (VERDICT-COMBINE -> ID-NONASCII). Seven v6 survivors are
byte-identical survivors on v7.

## The three most dangerous v7 survivors (routed to round 97; NOT implemented)

1. **CM1 — a combining mark on the heading number defeats the enumerated number-strip.**
   `_NUM2` strips `1.`/`I.`/`(1)`/dashes, but `1<U+0301>.` matches no enumerated shape, rides as a
   content token, and all five phrase-only headings anchor: the whole BR1/DASH1/G1 span-game
   family reopens with one mark. Fix (one line): NFKD-fold and drop Mn marks from each heading
   token before testing `_NUM2` in `_content_toks`.
2. **CR1 — a lone CR severs the gained verdict line for APPENDONLY while the v7 blocklist omits
   U+000D.** `_refuse_verdict_channel` reads raw `\n`-lines but blocklists only
   {00A0,000B,000C,2028,2029,001C,001D,001E,0085,001B}; `splitlines()` still severs at `\r`, so the
   forged LOCATED is invisible and PASS 9/9. Fix (one line): add `\u000d` to the verdict-window
   blocklist — or, structurally, refuse when a verdict-flavored window over a plausible id line
   keeps any non-letter byte between letters after NFKC+strip+fold (closes CR1+US1+OGH1+IS1+NUL1
   at once, exactly CriticO95's proposed rule which v7 did not take).
3. **IS1 — U+3000 is NBSP's NFKC twin but only literal U+00A0 is checked.** NFKC folds U+3000 to a
   plain space, so `LO<U+3000>TED` is as invisible as NB1 was, and the NBSP arm never fires.
   US1/OGH1/NUL1 are the same gap with non-folding breakers (U+001F/U+1680/U+0000). Fix (one
   line): run the window blocklist over the NFKC-folded span and refuse any Zs/Cc byte inside it.

(CMW2 is the heading-channel sibling of CM1: any junk first token — here a marked word — counts
as a content token for the span floor, because `_content_toks` excludes only enumerated number
shapes. An alphabetic-junk rule for span surfaces would blunt it.)

## Notes for the router

- ZWJ1 and FWID1 refuse via APPENDONLY but through key-splitting: `S００１` becomes a different
  internal id and the diagnostic names `S００１`, not S001. Refused today (the mis-keyed id is never
  in `base_disp`), but the diagnostic points at a row that does not exist — cheap r97 hardening:
  NFKC-fold the id key before the dispositions map.
- VTH1 shows a heading severed by VT reads as `## 1.` + orphan word, collapsing phrase hits to the
  table rows (`2 of 4`) — refused on TOPIC, so benign, but it is the same severing family CR1 uses.
- Controls: G0 and ZWNJ1 CLEAN rc 0 on both versions — the fixture machinery itself moves nothing.
- Honest-entry false-refusal risk (from CriticO95, still open): the TOPIC anchor path never strips
  zero-width/marks, so a genuine accented heading word loses its anchor (CMW2 head 1). Low priority.

## Tooling and writes

- Installed or upgraded tools: **none** (no pacman, no sysctl, no git/jj mutations; read-only
  `sha256sum`/`grep`/`diff`/`sed -n`/`cat` only; `diff` and `sed -n` ran against the grader and
  battery read-only). Tooling record: none.
- Stage writes: `stage/CriticO96/attacks_critic96.py`, `stage/CriticO96/attacks.md` (this file),
  `stage/CriticO96/DONE` (last), plus the Report trailer `.ufo/waves/round-96/w1/CriticO96.md`.
- Scratch `/fast/scratch/hyaku/kotodama-r96/CriticO96` (fixtures, results-critic96-v{6,7}.json,
  transcript) is deleted before yield; the commands above regenerate everything.
