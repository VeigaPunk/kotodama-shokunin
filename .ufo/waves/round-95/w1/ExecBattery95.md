- topic: funerary laments and dirges: the sung speech of mourning — professional keeners and lament genres, antiphonal and refrain structures, formulaic grief content (praise of the dead, address to the dead, blame and consolation), gendered mourning rules, the lament between speech and song, and the design procedure for a fictional mourning register
- seat: ExecBattery95 (operability, milestone r95-v1)

# ExecBattery95 report

Battery95 built from the round-94 driver + seven new classes from CriticO94 "Survivor recipes".

Files written (stage `ExecBattery95/`):
- battery95.py (sha256 342237cdcc980d6e9eea7e281671e9a7eb168e7731d799ecd4b32ddd7d00fd38)
- manifest95.json (schema kotodama-round-95-battery-manifest-v1, 14 classes A1..NUM2)
- red-before-v5.txt (v5 TOOL line + full per-class + BATTERY-SUMMARY + REG)
- reg-v5.txt (34 REG lines, reproducible, byte-diffed equal on two runs)
- stub.txt (G0 rc 0 CONTROL-CLEAN; stub tool survivors=14 refused=0)
- DONE (sha256 of battery95.py)

Red-before against v5 bytes (sha256 7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff, extracted from base 19aa4dd via `git show`):

`BATTERY-SUMMARY survivors=7 unnamed=0 refused=7`

Refused 7: A1 (VERDICT-NONASCII, rc 2), B1 (VERDICT-SOFTHYPHEN, rc 2), G1 (TOPIC, rc 1),
H1 (MANIFEST-ROW-TYPE, rc 2), I1 (NEWIDS, rc 1), J1 (gained a NOT-LOCATED line, rc 1),
K1 (VERDICT-LOWERCASE, rc 2). Survivors 7: CD1, LR1, TAB1, ID1, NUM1, RM1, NUM2
(all rc 0, ENTRY-EVIDENCE: PASS legs=9/9, traceback=no). Unnamed 0. Matches the
frozen claim O "before" exactly — no fixture tuning was needed or performed.

Fixtures byte-verified against CriticO94.md recipes: CD1 `LOCA\u0301TED`, LR1 `LO\u200eCATED`,
TAB1 `LO\tCATED`, ID1 `\ua731001 LOCATED`, NUM1 `## 1.1 address`..., RM1 `## I. address`...,
NUM2 `## Notes 1) address`... — all built on the G0 mini-lane, grade() identical to G0
(entry mode, set B). One deviation note: lesson line shape uses battery94's convention
(`S001 <token> recheck 90d accessed 2026-11-05`, no `- ` prefix, no GAINED_TAIL) exactly
as CriticO94's own dispo_extra does (`S001 {token} ...`), not battery94's b94_a1
`- S001 ...` + tail form; the forgery is the same lesson disposition for the no-base-
disposition row S001. Token lists for the new classes are nonempty seat-chosen guesses
(`LEG FAIL APPENDONLY`, `VERDICT-NONASCII`, `VERDICT-COMBINE/FORMAT/WS/TAB/LRM`,
`ID-NONASCII`, `LEG FAIL TOPIC`); per the round-94 precedent the L1 may amend them
before the v6 graded run if v6's actual diagnostic names differ.

REG: 34 lines (`REG R93` x22, `REG R92` x12... 22 R93 + 12 R92 = 34 total lines) identical
to reports/round-94/controls/reg-v5.txt (diff empty), reproducible on a second w-v5b run.

Controls: G0 clean (rc 0, ENTRY-EVIDENCE: PASS legs=9/9); stub always-rc-0 tool gives
survivors=14 unnamed=0 refused=0. Fail-closed: --work under /tmp refused rc 2;
nonexistent --tool refused rc 2.

Tooling: none installed or upgraded. Tooling record: none.
Scratch /fast/scratch/hyaku/kotodama-r95/ExecBattery95 deleted before yield.
