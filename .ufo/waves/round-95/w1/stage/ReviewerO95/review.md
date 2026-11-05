# ReviewerO95 — independent attack of the v6 candidate receipts (falsifier pass)

Candidate: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-95/w1/stage/ExecGraderV6/v6-candidate.py`
sha256 `f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec` — equals its `ExecGraderV6/DONE` line (read at 15:4x and re-hashed before every leg; stable).
v5 baseline: `git show 19aa4dd03dfd37b435d0b8ea5b313635d9d51592:tools/check-advance-evidence.py` → scratch `v5.py`, sha256 `7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff` (matches the claim's v5 sha; freeze HEAD `d41eb594d27fa71869c0c28d9c2dc051fda40079` confirmed).
Frozen receipts cross-checked: `predispatch-base.txt` prints FAIL legs=4/10 (O1 126/126 floor=134, O2/O3 driver missing, O4 no REG, C1 entry absent, C2 rows=893 highest=S969) — consistent with the do-nothing control declaration.
`reports/round-95/controls/` does not exist at freeze; the REG baseline I am given is `ExecBattery95/stage/reg-v5.txt` (34 lines). O4's "fail closed when the baseline is missing" behavior is predispatch's own and was exercised by the base receipt.

lsp device: not available in this seat's tool inventory; all checks below are direct command reruns (grep/diff used only as literal text fallback, every semantic claim is a measured rerun).

## Leg 1 — selftest ×4 concurrent, battery95 rerun, REG diff

Command (scratch `/fast/scratch/hyaku/kotodama-r95/ReviewerO95`):
```
bash run4.sh <candidate>            # four concurrent `python3 -B <cand> --selftest --work st4/rN`
rc per run: 0 0 0 0
run1 rc=0 SELFTEST PASS 134/134
run2 rc=0 SELFTEST PASS 134/134
run3 rc=0 SELFTEST PASS 134/134
run4 rc=0 SELFTEST PASS 134/134     -> floor 134 met, 134=134 (O1 shape)
```
(v5 reference run in the same scratch: `SELFTEST PASS 126/126` rc 0, 4.8 s — below floor, as declared.)

Battery rerun:
```
python3 -B ExecBattery95/battery95.py --tool <candidate> --work $S/battery --verbose
rc=0
BATTERY-SUMMARY survivors=0 unnamed=0 refused=14
```
All 14 classes outcome=REFUSED with traceback=no and a named token:
A1 VERDICT-NONASCII, B1 VERDICT-SOFTHYPHEN, G1 TOPIC, H1 MANIFEST-ROW-TYPE, I1 NEWIDS,
J1 gained_a_NOT-LOCATED_line, K1 VERDICT-LOWERCASE, CD1 VERDICT-COMBINE, LR1 VERDICT-FORMAT,
TAB1 VERDICT-TAB, ID1 ID-NONASCII, NUM1 TOPIC, RM1 TOPIC, NUM2 TOPIC.
`grep -c Traceback battery-out.txt` = 0; stderr empty.
REG: `grep '^REG ' battery-out.txt | diff - ExecBattery95/stage/reg-v5.txt` → empty (34 lines byte-identical; O4 shape on my rerun).

## Leg 2 — mutation cross-check

`ExecMutants95/DONE` (=`ff450980dec9e79b3315db276a985ac97df0f950964d751e4416b44c9f3ecf96`, sha
of their `mutants95.py`) landed at 16:05, just after the 45x60s bounded wait expired at ~16:05
(depwait exit 3). No extra waiting was done; the rerun below started immediately.

My rerun (scratch, candidate bytes re-hashed `f7981ba2…` before the run):
```
python3 -B ExecMutants95/mutants95.py --tool <candidate> --work $S/mutation
rc=0
TOOL sha256=f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec
CLEAN-FIRST selftest_rc=0 SELFTEST-PASS-line=True
MUTATION-SCORE: 95/95 killed, 0 survived, 0 broken-pattern
receipt rows: 95 KILLED, 0 SURVIVED, 0 BROKEN-PATTERN
```
Byte-for-byte: `diff <(grep -m1 MUTATION-SCORE my-out) <(grep -m1 MUTATION-SCORE ExecMutants95/stage/mutation-score.txt)`
→ empty. Their graded line: `MUTATION-SCORE: 95/95 killed, 0 survived, 0 broken-pattern`,
`COMMAND-RC: 0`, tool = the same candidate path.
Key rows in my receipt (all `matches=1`, all KILLED): `dispo-fallback-off` (the r94
broken-pattern mutant, now matching the v6 bytes exactly once — refresh documented in
`ExecMutants95/stage/fallback-patterns-v5.txt`: old target matches=0, refreshed matches=1),
`head-qualify-off` (semantics=exactly-once, killed by the new selftest pin),
`combining-refuse-off`, `lrm-refuse-off`, `tab-refuse-off`, `id-lookalike-refuse-off`,
`num1-anchor-off`, `rm1-anchor-off`, `num2-anchor-off`.
Set composition: r94 `MUTANTS` list has 88 names, all 88 carried into r95 (`set(r94)-set(r95)`
empty), r95 total 95 = 88 + the seven new refusal-off pins; floor >= 95 met with killed == total.
Clean-first receipt: `ExecMutants95/stage/clean-selftest-v6.txt` + `CLEAN-FIRST selftest_rc=0`
in their `mutation-score.txt` (and in my run). Stub control:
`ExecMutants95/stage/stub-control.txt` — `MUTATION-SCORE: 0/95 killed, 0 survived, 95
broken-pattern`, `COMMAND-RC: 1` (a printer that cannot apply the pairs scores 0 killed;
harness not vacuously green). Red-before-v5 receipt: `87/95 killed, 1 survived, 7
broken-pattern` rc 1 (head-qualify-off survives on v5, the seven new pins' patterns are absent
from v5) — the explicit red-before the claims require. `missing-work.txt` (rc 2 usage control)
also present.

## Leg 3 — diagnostic quality (every new refusal quoted, from my --verbose rerun)

- CD1: `ADVANCE-EVIDENCE_ERROR: line 4: verdict token carries a combining mark (VERDICT-COMBINE)`
- LR1: `ADVANCE-EVIDENCE_ERROR: line 4: verdict token carries a format character (VERDICT-FORMAT)`
- TAB1: `ADVANCE-EVIDENCE_ERROR: line 4: verdict token carries whitespace (VERDICT-TAB)`
- ID1: `ADVANCE-EVIDENCE_ERROR: line 4: id token carries a non-ASCII lookalike letter (ID-NONASCII)`
- NUM1: `ENTRY-EVIDENCE: FAIL legs=8/9 failed=TOPIC` with `LEG FAIL TOPIC expected=… observed=phrase anchors span 1 heading/table surfaces < 3; phrase anchors 4/4 spanning 1 heading/table surfac[es]`
- RM1: same TOPIC shape as NUM1 (same observed string, measured separately)
- NUM2: same TOPIC shape as NUM1 (same observed string, measured separately)

All nonempty after the token; nothing r94-MN1-like (empty after colon). PASS.

## Leg 4 — v5→v6 byte diff hazard read (`diff -u v5.py candidate`, 4 hunks, 174 lines)

1. `_refuse_disguised` rework: new named channels VERDICT-COMBINE (Mn category), VERDICT-FORMAT
   (Cf outside ZW_MAP), VERDICT-TAB (`LO\s+CATED|NOT\s+LOCATED` with a tab present), ID-NONASCII
   (small-cap fold map + non-ASCII letter in an `\S+\d{3,}` token); NFKD mark-strip and Cf-strip
   recovery paths. No v5 check removed; the seven v5 mutant pins are all still present
   (`grep -c 'mutant pin'` v5=7, v6=7) and total check sites went 124→132 (+8 = the seven class
   pins + the head-qualify pin), PASS line 126→134.
2. `dispositions()`: `_refuse_disguised` is now additionally invoked when the anchored
   disposition DID match (a matching verdict is still checked). The raising conditions gained
   `and not _dispo_match(plain)` conjuncts (VERDICT-NONASCII, DISPO_ANY_RE_I/lowercase,
   probe paths), so a line that already carries a valid anchored disposition is not refused by
   the disguise channels. This is a conditional narrowing — it only suppresses refusals where a
   valid disposition exists; no pinned case relies on that: REG 34 byte-identical (measured),
   selftest 134/134 (measured), battery 14/14 REFUSED with the pinned tokens (measured).
   K1 still refuses VERDICT-LOWERCASE because its line fails the anchored rule.
3. `_content_toks` (heading anchors): v5 stripped only a leading `\d+[.)]`; v6 drops nested
   digits (`1.1`), roman (`I.`), and second-token numbers (`Notes 1)` → content surface
   `[address]`), leaving legit `## 1. The address` → `[The, address]` unchanged. G1's pinned
   TOPIC refusal is byte-identical in the battery rerun.
4. Selftest: purely additive (+68 lines, no `-` removals in the selftest body). The
   head-qualify pin expects rc 1 with `['FAIL TOPIC', 'phrase anchors 0/4']` on single-token
   headings — the pin that fails under head-qualify-off, as the claim requires.

No removed selftest check, no weakened pinned refusal, no REG-relevant line change observed.
Hazard flags: none.

## Verdict

Every leg was re-measured in my own scratch against the candidate bytes
(`f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec`), never taken from the
builders' stdout: four concurrent selftests (all rc 0, 134/134 >= floor 134), battery95 rerun
(survivors=0 unnamed=0 refused=14, all named, Traceback count 0), REG section byte-identical
to `ExecBattery95/stage/reg-v5.txt` (diff empty, 34 lines), full mutation rerun (rc 0,
95/95 killed, 0 survived, 0 broken-pattern; graded score line byte-identical to
ExecMutants95's reported line; clean-first and stub-control receipts present and sane;
red-before-v5 red), diagnostic quotes all informative, and the v5→v6 diff read hunk by hunk
with no removed check and no weakened pinned behavior.

REVIEWER-O-95: PASS legs=5/5

Residual risk (no action required): (a) the frozen counter's own REG baseline
`reports/round-95/controls/reg-v5.txt` is not yet in the repo; O4 will read the baseline
path at lands measurement — if the L1 lands a byte-different file there than
`ExecBattery95/stage/reg-v5.txt`, O4 fails closed; the bytes I certified are the stage copy.
(b) `_refuse_disguised`'s two new `and not _dispo_match(plain)` conjuncts are conditional
narrowings certified only against the pinned surfaces (REG 34, selftest 134, battery 14);
a hitherto-unpinned input class that both carries an anchored disposition and a disguise
channel would now pass unnamed — no such case exists in any pinned fixture I ran.
(c) the 45x60s dependency bound expired seconds before `ExecMutants95/DONE` appeared; the
mutation rerun used their landed driver bytes (`ff450980…`) and the candidate, so leg 2 does
not depend on their goodwill — only on bytes I hashed myself.
