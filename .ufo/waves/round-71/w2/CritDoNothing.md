# CritDoNothing — re-run of the three round-71 do-nothing control receipts at base

Seat: L1Kotodama71.CritDoNothing (critic, round 71 wave 2). Lane read-only; no lane writes except this report. No spawns.

Task: re-run the three do-nothing control receipts at base (`git archive b94a543c`) and confirm each fails to reach its declared target; report exact outputs.

## Method

```
rm -rf /tmp/r71-base && mkdir -p /tmp/r71-base
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin archive --format=tar b94a543c | tar -C /tmp/r71-base -xf -
```

Base identity:

- commit `b94a543c70f40dba7e49fff96d05bfb8bbd8c678` (2026-10-25 07:24:56 -0300, "round-70 verifier spot-check (integrator, hyaku): non-author admit/reject")
- tree `73ba643b7b5b63415a022bb42079249bd842d7bf`
- archive entries: 8602; `git archive b94a543c | tar -t | grep -c '^reports/round-71'` → **0** (no round-71 path exists at base, confirmed)
- `git merge-base --is-ancestor b94a543c HEAD` → ok (base is an ancestor of HEAD `14c88d9`)

Every command below ran with cwd `/tmp/r71-base`. Receipts compared against, by sha256:

- `reports/round-71/telemetry/controls-c.txt` = `ab2092f3edf578555314df415c1b7f313f47e6bf45f53af9542a25c37518e9a3`
- `reports/round-71/telemetry/controls-ca.txt` = `841ea793fc3bb826aa6ca78fb34fef9e8fcef91046d03a517306c54bd33740ba`
- `reports/round-71/telemetry/controls-d.txt` = `efc0c05694b19bd34122dd4a36bc3055f5c20cf13bffc4fbbcb4db9aa97abbe9`

## Verdict

| control | does it fail to reach its declared target at base? | verdict |
|---|---|---|
| C (`controls-c.txt`) | yes — 35/242/784, entry absent, `check-cited-lines` rc=2 | **PASS** (control discriminates) |
| Ca (`controls-ca.txt`) | yes — 6×0 headers, 0 `acc2d614`, 27 words, 0 trend rows, lesson absent, verdict table absent | **PASS** (control discriminates) |
| D (`controls-d.txt`) | **no** — the declared counting command's no-git leg reaches the target at base (`SELFTEST: COULD-NOT-EVALUATE (no git)`, `EXIT=2`), and the frozen-data leg passes at base by design (`8/8`, exit 0) | **FAIL** (do-nothing control cannot be run as declared; committed receipt is prose, not a capture) |

---

## Control C — PASS (fails to reach target)

Declared counting command (`reports/round-71/claims.json`, claim C), run at base, exact stdout/stderr and per-leg rc:

```
$ find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l
35                                              rc=0
$ find corpus/knowledge -type f -name '*.md' | wc -l
242                                             rc=0
$ grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md
784                                             rc=0
$ python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/dance-performance-movement-codes.md
CITED_LINES_ERROR no such file or directory: corpus/knowledge/culture-material/dance-performance-movement-codes.md   [stderr]  rc=2
$ test -f corpus/knowledge/culture-material/dance-performance-movement-codes.md
                                                rc=1
```

Whole command rc=1. Target is `culture-material=36, corpus=243; registry >= 784+12=796; entry exists; check-cited-lines exit 0` — **every leg misses** (35≠36, 242≠243, 784<796, entry absent, rc 2≠0).

Declared `before` sweeps, re-derived:

```
$ find corpus/knowledge/culture-material -maxdepth 1 -type f -name '*danc*'
                                                (no output)
$ grep -rniE '^- topic:.*\b(danc|choreograph|movement culture|performance)\b' corpus/knowledge/culture-material/*.md
                                                (no output, rc=1)
$ grep -rniE '^- topic:.*(danc|choreograph|movement culture|performance)' corpus/knowledge/culture-material/*.md | head
corpus/knowledge/culture-material/funerary-material-culture.md:4:- topic: … avoidance terms, rite terms …   (only the unbound 'avoidance' false-match)
```

The word-bounded gap is real at base; the unbound variant false-matches only `avoidance`.

Against the committed receipt: `controls-c.txt` states `culture-material: 35`, `corpus: 242`, `registry: 784`, `entry-absent: absent`, `filename-owners: 0`, `topic-owners-wordbounded: 0` — **values faithful**, but it is a normalized summary: it omits the `check-cited-lines` **rc=2 / CITED_LINES_ERROR** leg, which is the leg the target names explicitly. LOW finding, not a control failure.

## Control Ca — PASS (fails to reach target)

Declared counting command (claim Ca), run at base:

```
$ for f in reports/round-70/telemetry/measures-{o,ca,d}.txt reports/round-70/telemetry/controls-{o,ca,d}.txt; do
    grep -cE '^# (counter sha256|stamped revision|evaluated revision|measured revision|tree|worktree dirty)' "$f" || echo MISSING:$f
  done | sort | uniq -c
      6 0
      1 MISSING:reports/round-70/telemetry/controls-ca.txt
      1 MISSING:reports/round-70/telemetry/controls-d.txt
      1 MISSING:reports/round-70/telemetry/controls-o.txt
      1 MISSING:reports/round-70/telemetry/measures-ca.txt
      1 MISSING:reports/round-70/telemetry/measures-d.txt
      1 MISSING:reports/round-70/telemetry/measures-o.txt
$ grep -c 'acc2d614' corpus/SOURCES.md
0                                               rc=1
$ awk -F'|' 'NR==13 {print $4}' corpus/lessons/round-70.md | wc -w
27                                              rc=0
$ grep -c 'round-70 trend-correction' SCORECARD.md
0                                               rc=1
$ grep -c 'rejected this round:' corpus/lessons/round-71.md
grep: corpus/lessons/round-71.md: No such file or directory          [stderr] rc=2
$ awk -F'|' '$1 ~ /S[0-9]+/ && $2 ~ /^(PRESENT|REFUSED|UNVERIFIABLE)$/ {n++} END{print n+0}' reports/round-71/telemetry/quarantine-verdicts.md
awk: fatal: cannot open file `reports/round-71/telemetry/quarantine-verdicts.md' for reading: No such file or directory   [stderr] rc=2
```

Whole command rc=2. Target is `six receipts × 6 header lines = 36 matches; acc2d614 ≥1; ≤25 words; trend-correction row ≥1; reject-sweep statement ≥1; 21 verdict rows` — **all six legs miss** (0 matches, 0, 27>25, 0, absent, absent). Base S860 cell names `6cb51a4` (verified: `grep -c '6cb51a4' corpus/SOURCES.md` → 1; `acc2d614` → 0).

Against the committed receipt: `controls-ca.txt` records `per-file-header-matches: … 0` for each of the six files, `S860-acc2d614: 0`, `round70-gate-quote-words: 27`, `trend-correction-rows: 0`, `lesson71-reject-sweep:` empty, `verdict-labels:` empty. Values faithful, but the receipt is not the command's output, and it hides two facts a grader needs:

1. **`|| echo MISSING:$f` fires on `grep` rc=1 (no matches), not only on rc=2 (missing file).** All six files exist at base, yet the command prints six `MISSING:` lines. Any reader taking the raw output at face value would conclude the round-70 receipts were absent. The committed receipt normalizes this away instead of fixing it.
2. The last two legs **errored (rc=2)**, they did not print `0`/empty: the receipt's empty `lesson71-reject-sweep:` / `verdict-labels:` read as "file present, nothing found", when in fact both files do not exist at base.

Neither point lets the control reach the target — it fails either way — so Ca's control verdict is PASS; both are calibration/provenance defects, not target failures.

## Control D — FAIL (declared control is not executable at base, and one leg reaches the target)

Leg 1, run at base:

```
$ python3 -B reports/round-71/accept-d.py --selftest
python3: can't open file '/tmp/r71-base/reports/round-71/accept-d.py': [Errno 2] No such file or directory   [stderr]
                                                rc=2, no SELFTEST line
```
Target: `SELFTEST: 2/2`, exit 0 → misses. (This leg is satisfied by any new file's absence; it is a file-existence check, not a behavioural one.)

Leg 2 — **the declared counting command, verbatim, at base**:

```
$ bash -c 'T=$(mktemp -d); tar --exclude=.git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin -cf - . | tar -C $T -xf -; cd $T; python3 -B reports/round-71/accept-d.py --selftest; echo EXIT=$?'
SELFTEST: COULD-NOT-EVALUATE (no git)
EXIT=2
```

That is **the declared target line for leg 2**, reached at base. The reason is structural: the leg is not tree-parameterized — it hard-codes `-C /home/vgpnk/Projects/shokunin/kotodama-shokunin`, so it copies the **live worktree**, not the tree under test. Instrumented run from `/tmp/r71-base`:

```
COPY_HAS_ROUND71=yes
COUNTER_SHA=459cfa9da53fe3c4b44cfa5be4f82a2794298cc3b79c7f4e0f330f0977945930
COPY_HAS_S861=1
SELFTEST: COULD-NOT-EVALUATE (no git)
EXIT=2
```

The copied counter's sha256 equals the live counter's sha256 (`459cfa9d…5930`), and the copy carries round-71 data (`S861`). So at base and at the measured revision this leg runs the *same* bytes: it cannot discriminate, and it is evidence about the worktree rather than about `b94a543c`.

Leg 3, run at base:

```
$ python3 -B reports/round-69/accept-d.py --root .
LEG PASS STAMP self=c41ffbc8244f committed=c41ffbc8244f
LEG PASS SECTION heading=### Registry correction chains
LEG PASS TABLE header=5 rows=5
LEG PASS STATES states=['pending', 'settled-active', 'settled-retired', 'settled-closed', 'settled-split']
LEG PASS FIELDS empty=none short=none
LEG PASS SIGNATURES missing=none
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', 'S859', 'S859', 'S859', 'S859']
ACCEPT-D-69: PASS legs=8/8
                                                rc=0
```
Target: `ACCEPT-D-69: PASS legs=8/8 exit 0` → **reached at base**. This leg is a preservation leg (the frozen counter must be untouched), so passing at base is intended — but it means it adds no discrimination to the control.

Base no-git reproduction that the claim's `do_nothing_control` text promises but the committed receipt omits:

```
$ T=$(mktemp -d); tar --exclude=.git -C /tmp/r71-base -cf - . | tar -C $T -xf -; cd $T; python3 -B reports/round-69/accept-d.py --selftest; echo EXIT=$?
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)
SELFTEST: 1/2
EXIT=1
```
This is the V70-6 before-state, reproduced.

Against the committed receipt — `controls-d.txt` in full:

```
# do-nothing control D (rev 2) — base b94a543c, exact declared command on the base tree
new-counter-exists-at-base: no (git archive of b94a543c has no reports/round-71/)
declared no-git leg on base tree: python3 -B reports/round-71/accept-d.py --selftest → file-not-found, exit 2, NO COULD-NOT-EVALUATE line → control FAILS to reach target (good)
```

Three defects, each independently fatal to the control's claim:

1. **It is not a receipt.** No command output, no exit codes captured, unlike the lane's own round-69 bar (`reports/round-69/telemetry/controls.txt` is verbatim output with `exit=N` per command). It is prose asserting an outcome.
2. **It substitutes a different command for the no-git leg.** `python3 -B reports/round-71/accept-d.py --selftest` is the *in-tree* invocation; the declared no-git leg is the `tar --exclude=.git` copy. The receipt's "NO COULD-NOT-EVALUATE line" is trivially true of a missing file and says nothing about the no-git leg.
3. **It omits the frozen-counter `SELFTEST 1/2 exit 1` reproduction** that `claims.json` `do_nothing_control` explicitly promises ("the no-git reproduction shows the frozen counter reporting SELFTEST 1/2 exit 1"). I reproduced it above; it is not in the receipt.

`claims.json` correction (3) states "controls-d was regenerated with the exact declared command". Both the file's content and the base run of that exact command (which prints the target line) contradict that sentence.

### Strongest counterexample

A grader applying the frozen control rule — "the counting command is run at the declaration on the unmodified base tree … the control must FAIL to reach the declared target" — runs claim D's counting command at `b94a543c` and gets `SELFTEST: COULD-NOT-EVALUATE (no git)` / `EXIT=2`: the declared target, on the base tree, with no work done. The control therefore does **not** prove that a do-nothing control cannot reach claim D's target; only the counter's *existence* is falsified, and that by a file-not-found that is true of every not-yet-written file.

## Impacted axes

- **depth (D) — harmed.** Leg 2 of the declared counting command measures the live worktree, so it is identical at base and after: the after-state evidence for leg 2 has false provenance (it is not a property of the measured revision tree), and the do-nothing control for that leg is unimplementable as declared. Leg 3 passes at base by design; leg 1 is a file-existence check. No leg of the control is both base-sensitive and behavioural.
- **calibration (Ca) — touched, not harmed.** Control fails on all six legs; two legs fail by hard error (rc=2) while the receipt renders them as empty labels, and `|| echo MISSING:$f` prints `MISSING` for files that exist.
- **coverage (C) — touched, not harmed.** Control fails on all legs; receipt is a normalized summary that drops the `check-cited-lines` rc=2 leg named in the target.

## Smallest safe correction

1. `reports/round-71/claims.json` claim D `counting_command`, leg 2: copy the tree under test, not the lane — `tar --exclude=.git -C . -cf - .` (cwd = tree under test) or `-C "$ROOT"`. Then base gives file-not-found rc=2 and the measured revision gives `COULD-NOT-EVALUATE` rc=2, and the leg discriminates.
2. Regenerate `reports/round-71/telemetry/controls-d.txt` as a verbatim capture in the round-69 convention (`=== cmd`, output, `exit=N`) of three base-tree commands: (a) `python3 -B reports/round-71/accept-d.py --selftest` → rc=2 `can't open file`; (b) no-git copy of the base tree + `python3 -B reports/round-69/accept-d.py --selftest` → `DO-NOTHING FIXTURE: PASS (unexpected)` / `SELFTEST: 1/2` / `EXIT=1`; (c) `python3 -B reports/round-69/accept-d.py --root .` → `ACCEPT-D-69: PASS legs=8/8`, exit 0. Delete the sentence claiming the declared command was run at base unless the command is fixed per (1) first.
3. `claims.json` claim Ca `counting_command`: replace `grep -c … "$f" || echo MISSING:$f` with `[ -f "$f" ] || echo MISSING:$f` (or gate the echo on rc≥2), so a 0-match file is not reported as missing; record legs 5 and 6 as the rc=2 errors they are.
4. Optional, same bar: append the raw per-leg captures to `controls-c.txt` and `controls-ca.txt` so a grader can re-run byte-for-byte.

## Reproducibility

```
rm -rf /tmp/r71-base && mkdir -p /tmp/r71-base
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin archive --format=tar b94a543c | tar -C /tmp/r71-base -xf -
cd /tmp/r71-base
# C
find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l      # 35
find corpus/knowledge -type f -name '*.md' | wc -l                      # 242
grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md            # 784
python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/dance-performance-movement-codes.md  # rc=2
test -f corpus/knowledge/culture-material/dance-performance-movement-codes.md                                 # rc=1
# Ca  (single command from claims.json)
for f in reports/round-70/telemetry/measures-{o,ca,d}.txt reports/round-70/telemetry/controls-{o,ca,d}.txt; do grep -cE '^# (counter sha256|stamped revision|evaluated revision|measured revision|tree|worktree dirty)' "$f" || echo MISSING:$f; done | sort | uniq -c
grep -c 'acc2d614' corpus/SOURCES.md                                    # 0
awk -F'|' 'NR==13 {print $4}' corpus/lessons/round-70.md | wc -w        # 27
grep -c 'round-70 trend-correction' SCORECARD.md                        # 0
# D  (declared counting command, verbatim)
python3 -B reports/round-71/accept-d.py --selftest                       # rc=2, file-not-found
bash -c 'T=$(mktemp -d); tar --exclude=.git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin -cf - . | tar -C $T -xf -; cd $T; python3 -B reports/round-71/accept-d.py --selftest; echo EXIT=$?'
                                                                        # SELFTEST: COULD-NOT-EVALUATE (no git) / EXIT=2  ← target reached at base
python3 -B reports/round-69/accept-d.py --root .                         # ACCEPT-D-69: PASS legs=8/8, exit 0
```

## Tooling

No installs or updates. Scratch tree `/tmp/r71-base` is disposable; the lane was not written by this seat.

Provenance note: all base measurements above come from the immutable `git archive b94a543c` tree, not from the live worktree. During this run other seats left the live worktree dirty (`M corpus/README.md`, `M corpus/knowledge/culture-material/dance-performance-movement-codes.md`, `M reports/round-71/telemetry/census-end.txt`); this does not affect any figure reported here, but it does affect claim D's declared no-git leg, which copies that dirty worktree by construction (see Control D).
