# ExecBattery96 — round-96 battery driver battery96.py and control receipt (operability)

Leaf seat. No subagent dispatch. Read claims.json and predispatch.py first; frozen
files untouched (claims.json, predispatch.py, predispatch-base.txt, round-95/).
battery95.py read fully (649 lines, sha256
342237cdcc980d6e9eea7e281671e9a7eb168e7731d799ecd4b32ddd7d00fd38, matches spec).

## Driver

`stage/ExecBattery96/battery96.py` (787 lines, sha256 below) copied from battery95.py
and extended in place. CLI shape kept: `python3 -B battery96.py --tool <tool> --work <dir>`
plus battery95's existing `--verbose`/`--emit`. `--work` under /tmp refused as before.
Class manifest: 24 expected-REFUSE classes (battery95's fourteen: A1, B1, G1, H1, I1,
J1, K1, CD1, LR1, TAB1, ID1, NUM1, RM1, NUM2; nine fresh CriticO95 classes NB1, VT1,
FF1, LS1, NEL1, ANSI1, CYR1, BR1, DASH1; plus F1) and 2 CLEAN controls (G0 as in
battery95, ZWNJ1 new: ZWNJ U+200C inside a table-cell phrase, expected CLEAN rc 0).
Control-aware outcome handling added (`class_outcome` CLEAN/NOT-CLEAN branch;
`summarize()` counts survivors/unnamed/refused over expected-REFUSE classes only and
prints extras `traceback=<t> clean=<c> not-clean=<n>` after the battery95
`BATTERY-SUMMARY survivors=... unnamed=... refused=...` prefix, so the frozen
predispatch regex still matches). `--emit` manifest bumped to
`kotodama-round-96-battery-manifest-v1`, driver field `battery96.py`.

Recipes match CriticO95 `attacks_critic95.py`/`attacks.md` lines 40-54: NB1
`LOCA+U+00A0+Ted` lesson gain, VT1/FF1/LS1/NEL1 same shape with U+000B/U+000C/
U+2028/U+0085, ANSI1 `LOCA+ESC+[31mTED`, CYR1 `- <U+0430>001 LOCATED recheck moved`,
BR1 `## (1) address...`, DASH1 `## - address...`, all via `standard()`/`_reps()`/
`GAINED_TAIL` exactly as CriticO95 built them.

F1 (round-95 lesson 'The F1 non-numbered variant', lesson line 78) as routed:
non-numbered content-free h2 heads `## alpha beta`, `## gamma delta`,
`## epsilon zeta`, `## eta theta`, `## iota kappa`. The first draft kept phrase
words in the heads (`## alpha address` etc.) and survived v6 (rc 0, PASS 9/9);
fixed to the lesson's literal content-free shape and re-measured rc 1 TOPIC.
See "Deviation" below.

## Control receipt over frozen v6 bytes

```
S=/fast/scratch/hyaku/kotodama-r96/ExecBattery96
mkdir -p $S/v6                          # rc 0
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 0539276c0e329743200b60e98bf289c540f78864:tools/check-advance-evidence.py > $S/v6/check-advance-evidence.py  # rc 0
sha256sum $S/v6/check-advance-evidence.py  # f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec, matches spec
python3 -B battery96.py --tool v6/check-advance-evidence.py --work work3 --verbose > out  # rc 0
```

Saved complete output as `stage/ExecBattery96/control-v6.txt` (95 lines) from the
stage copy of battery96.py. Per-class v6 outcome (control-v6.txt):

| class | counterfeit | expected | v6 outcome | named |
|---|---|---|---|---|
| A1 | U+041E in verdict | REFUSE | REFUSED | VERDICT-NONASCII |
| B1 | U+00AD in verdict | REFUSE | REFUSED | VERDICT-SOFTHYPHEN |
| G1 | `## 1.` heads | REFUSE | REFUSED | TOPIC |
| H1 | manifest row list | REFUSE | REFUSED | MANIFEST-ROW-TYPE |
| I1 | 4-cell lands row | REFUSE | REFUSED | NEWIDS |
| J1 | U+2013 in NOT-LOCATED | REFUSE | REFUSED | gained a NOT-LOCATED line |
| K1 | lowercase unanchored verdict | REFUSE | REFUSED | VERDICT-LOWERCASE |
| CD1 | U+0301 in verdict | REFUSE | REFUSED | VERDICT-COMBINE |
| LR1 | U+200E in verdict | REFUSE | REFUSED | VERDICT-FORMAT |
| TAB1 | tab in verdict | REFUSE | REFUSED | VERDICT-TAB |
| ID1 | U+A731 id letter | REFUSE | REFUSED | ID-NONASCII |
| NUM1 | `## 1.1` heads | REFUSE | REFUSED | TOPIC |
| RM1 | `## I.` roman heads | REFUSE | REFUSED | TOPIC |
| NUM2 | `## Notes 1)` heads | REFUSE | REFUSED | TOPIC |
| NB1 | NBSP U+00A0 in verdict | REFUSE (v7) | SURVIVOR rc 0 | none |
| VT1 | U+000B in verdict | REFUSE (v7) | SURVIVOR rc 0 | none |
| FF1 | U+000C in verdict | REFUSE (v7) | SURVIVOR rc 0 | none |
| LS1 | U+2028 in verdict | REFUSE (v7) | SURVIVOR rc 0 | none |
| NEL1 | U+0085 in verdict | REFUSE (v7) | SURVIVOR rc 0 | none |
| ANSI1 | ESC[31m in verdict | REFUSE (v7) | SURVIVOR rc 0 | none |
| CYR1 | U+0430 as id letter | REFUSE (v7) | SURVIVOR rc 0 | none |
| BR1 | `## (1)` heads | REFUSE (v7) | SURVIVOR rc 0 | none |
| DASH1 | `## -` heads | REFUSE (v7) | SURVIVOR rc 0 | none |
| F1 | `## alpha beta` heads | REFUSE | REFUSED rc 1 | TOPIC |
| G0 | clean control | CLEAN | CLEAN rc 0 | none |
| ZWNJ1 | U+200C in table cell | CLEAN | CLEAN rc 0 | none |

Summary line over v6: `BATTERY-SUMMARY survivors=9 unnamed=0 refused=15 traceback=0 clean=2 not-clean=0`
— exactly the frozen prediction (refused = battery95's 14 + F1; survivors = the nine
fresh classes). REG-line count 34 (`grep -c '^REG ' control-v6.txt` → 34, rc 0);
`grep -c Traceback control-v6.txt` → 0. Battery exit rc 0.

Sanity: all 34 REG lines byte-identical to
`reports/round-95/controls/reg-v5.txt` in order (diff empty, rc 0); every class
v6 refuses (the battery95 fourteen + F1) is REFUSED on a named diagnostic in the
new table; no traceback anywhere.

## Pin

`stage/ExecBattery96/battery96.sha256` contains
`9f80f59481861b104f166a838222fcdf300e55a27fc841b5217e1980b5e91c21  battery96.py`.
`sha256sum -c battery96.sha256` → `battery96.py: OK`, rc 0; re-measured after
freeze, same sha. battery96.py was not edited after the control run; the control
run used the identical bytes (scratch copy → stage copy, sha re-verified).

## Commands with rc (all rc 0 unless noted)

- `cp .../round-95/.../battery95.py → scratch battery96.py` rc 0; sha256
  342237cd... verified against spec.
- `git -C <lane> show 0539276...:tools/check-advance-evidence.py > $S/v6/...` rc 0;
  sha f7981ba2... matches spec.
- Probe runs of battery95 shape (`--work work1` 14/14 refused; `work2` after edits
  9 survivors/15 refused with the F1 draft excluded) rc 0.
- Final control: `python3 -B battery96.py --tool v6/check-advance-evidence.py
  --work work3 --verbose` rc 0.
- `sha256sum -c battery96.sha256` rc 0; `diff <(grep '^REG ' control-v6.txt)
  <(grep '^REG ' reg-v5.txt)` empty rc 0; `grep -c Traceback control-v6.txt` → 0.
- `py_compile` rc 0; `--help` rc 0.
- `git status --short` rc 0: only untracked round-96 wave dirs (incl. this seat's
  stage and Report); no tracked file modified, nothing committed by this seat.

## Deviation

One edit after the first control probe: the F1 builder's first draft put phrase
words in the heads (`## alpha address` ...), which v6 anchors on (rc 0, PASS 9/9,
not the routed TOPIC refusal). Replaced with the lesson's literal content-free
shape (`## alpha beta` etc.), re-ran the control (9/0/15 as predicted), then
froze. No edit after that freeze.

## Tooling, risks, blockers

- Installed/upgraded tools: none. pacman untouched (paused host-wide; no install
  attempted). No sysctl changes. Disk guard read-only (`disk-guard.sh status` rc 0).
- Scratch `/fast/scratch/hyaku/kotodama-r96/ExecBattery96/` deleted before yield
  (work dirs, v6 export, probe transcripts). Re-runnable via the commands above.
- Risk: the v6 control pins behaviour, not v7; if ExecGraderV7's v7 changes the
  diagnostic strings the battery lexes (e.g. a new token for these channels), the
  manifest tokens here may need the v7's strings — the battery's token lists are
  deliberately broad (`LEG FAIL ...` plus message variants) and the summary counts
  are the frozen target, so a mismatch would show as UNNAMED, not silent PASS.
- Blocker: none.
