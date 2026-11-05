# ReviewerO95 — Report (round 95, claim O falsifier pass)

Verdict: **REVIEWER-O-95: PASS legs=5/5**

Candidate: `.ufo/waves/round-95/w1/stage/ExecGraderV6/v6-candidate.py`, sha256
`f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec` (= its DONE; re-hashed
before each leg). v5 baseline extracted from base `19aa4dd03dfd37b435d0b8ea5b313635d9d51592`,
sha `7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff` (claim match); freeze
HEAD `d41eb594d27fa71869c0c28d9c2dc051fda40079` confirmed. All measurements are my own reruns
in `/fast/scratch/hyaku/kotodama-r95/ReviewerO95` (deleted before this report's yield), never
the builders' stdout.

Leg 1 — selftest ×4 concurrent (`bash run4.sh <cand>`): rc 0/0/0/0, `SELFTEST PASS 134/134`
four times (floor 134; v5 reference run in the same scratch: 126/126 rc 0, below floor as
declared). Battery95 rerun (`python3 -B battery95.py --tool <cand> --work $S/battery --verbose`,
rc 0): `BATTERY-SUMMARY survivors=0 unnamed=0 refused=14`; all 14 classes REFUSED, named,
`traceback=no`; `grep -c Traceback` = 0; stderr empty. REG: `grep '^REG ' | diff - reg-v5.txt`
empty (34 lines byte-identical).

Leg 2 — mutation rerun (`python3 -B mutants95.py --tool <cand> --work $S/mutation`, rc 0):
`MUTATION-SCORE: 95/95 killed, 0 survived, 0 broken-pattern`; 95 KILLED rows, 0 survived,
0 broken; CLEAN-FIRST selftest_rc=0. Graded score line byte-identical (diff empty) to
ExecMutants95's reported line in `stage/ExecMutants95/mutation-score.txt` (their graded
COMMAND-RC 0, same candidate path). Set carries all 88 round-94 names (set difference empty)
plus the seven new refusal-off pins = 95 total (floor 95). Key rows all `matches=1`, KILLED:
`dispo-fallback-off` (r94 broken-pattern mutant; refresh documented in
`stage/ExecMutants95/fallback-patterns-v5.txt`: old target matches=0, refreshed matches=1),
`head-qualify-off` (exactly-once, killed by the new selftest pin), and the seven new pins.
Receipts verified present and sane: `clean-selftest-v6.txt` (clean-first), `stub-control.txt`
(`MUTATION-SCORE: 0/95 killed, 0 survived, 95 broken-pattern`, rc 1 — stub printer scores 0
killed, harness not vacuously green), `red-before-v5.txt` (`87/95 killed, 1 survived, 7
broken-pattern`, rc 1 — red against v5), `missing-work.txt` (rc 2 usage control).

Leg 3 — new-refusal diagnostics (quoted from my --verbose run; all informative, none
empty-after-colon in the r94-MN1 style):
- CD1 `ADVANCE-EVIDENCE_ERROR: line 4: verdict token carries a combining mark (VERDICT-COMBINE)`
- LR1 `ADVANCE-EVIDENCE_ERROR: line 4: verdict token carries a format character (VERDICT-FORMAT)`
- TAB1 `ADVANCE-EVIDENCE_ERROR: line 4: verdict token carries whitespace (VERDICT-TAB)`
- ID1 `ADVANCE-EVIDENCE_ERROR: line 4: id token carries a non-ASCII lookalike letter (ID-NONASCII)`
- NUM1/RM1/NUM2: `ENTRY-EVIDENCE: FAIL legs=8/9 failed=TOPIC` + `LEG FAIL TOPIC … observed=phrase anchors span 1 heading/table surfaces < 3; phrase anchors 4/4 spanning 1 heading/table surfac[es]`

Leg 4 — `diff -u v5.py candidate`: 4 hunks. (1) `_refuse_disguised` rework adds the four named
channels + NFKD/Cf recovery; (2) `dispositions()` now also checks matched verdicts; the raise
conditions gained `and not _dispo_match(plain)` conjuncts — a conditional narrowing that only
suppresses refusals where a valid anchored disposition exists; no pinned case relies on it
(REG 34 identical, selftest 134/134, battery 14/14 with pinned tokens — all measured); K1
still refuses `VERDICT-LOWERCASE` because its line fails the anchored rule; (3) `_content_toks`
extends number-stripping to nested/roman/second-token headings, legit `## 1. The address`
unchanged (G1 byte-identical in battery); (4) selftest purely additive (+8 checks = seven class
pins + the head-qualify pin expecting rc 1 `['FAIL TOPIC', 'phrase anchors 0/4']`); v5's seven
mutant pins all retained (`grep -c 'mutant pin'` 7→7). No removed check, no weakened pinned
refusal, no REG-relevant change. Hazard flags: none.

Timing note: the 45x60s bounded dependency wait expired (depwait exit 3) seconds before
`ExecMutants95/DONE` (=`ff450980dec9e79b3315db276a985ac97df0f950964d751e4416b44c9f3ecf96`,
their driver's sha) landed at 16:05; no further waiting occurred — leg 2 was executed
immediately against bytes I hashed myself, so it does not rest on the builder's report.

Residual risk: (a) `reports/round-95/controls/reg-v5.txt` does not exist yet; at lands
measurement O4 reads that path — the L1 must land the stage `reg-v5.txt` bytes unmodified or
O4 fails closed. (b) The two `_refuse_disguised` conjuncts are certified only against pinned
surfaces; an unpinned input both carrying an anchored disposition and a disguise channel would
now pass unnamed (no such pinned fixture exists). (c) lsp device unavailable in this seat;
every semantic claim above is a direct command rerun, not text-grep inference.

Tooling installed/upgraded: none. Pacman: none (guard respected). Sysctl: none. Git/jj
mutations: none (one read-only `git show` for the v5 bytes). Writes: stage
`ReviewerO95/{review.md,DONE}` and this report only. Scratch deleted.

Stage files: `.ufo/waves/round-95/w1/stage/ReviewerO95/review.md` (sha256
`4d610d0a80ccefec02f0f3d9a35b2afd468fc03d17381d98d7a007ff99741c36`, mirrored in DONE),
`.ufo/waves/round-95/w1/stage/ReviewerO95/DONE`.
