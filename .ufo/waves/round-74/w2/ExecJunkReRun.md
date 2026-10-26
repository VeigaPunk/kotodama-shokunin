# ExecJunkReRun — round-74 WAVE 2 attack on the junk-landing controls

Seat: `ExecJunkReRun` (leaf; no delegation). Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
(read-only). Revisions: base `f7104cbce186`, freeze F `00c408a0af2f`, claim Ca `5e4796c0cb6a`,
claim C `c4bf61a8d722`. Everything below was run against those revs.

Environment: git 2.56.0, Python 3.14.8, 32 cores, `/tmp` on XFS. No tool installs or upgrades
(pacman not touched, nothing needed).

## Method and clone discipline

```
D=$(mktemp -d /tmp/ExecJunkReRun.XXXXXX)          # -> /tmp/ExecJunkReRun.oBjdtm
git -C "$D" init -q && git -C "$D" rev-parse --show-toplevel   # prints $D
git clone -q <lane> "$D/lane"
git -C "$D/lane" checkout -q --detach 00c408a0af2fa5ddf65af2224152ce258b26d896
```

All branch moves (`git branch -f main ...`) were inside `$D/lane`. The lane, fleet repo, sibling
lanes, scripts, templates and `.ufo/state` were not written. The generator clones the lane read-only
and commits only inside its own `mktemp` fixture repos.

Two independent counters were also run at the claims' own landings inside the clone:

```
reports/round-74/accept-ca.py  --root . --lands 5e4796c0cb6a --freeze 00c408a0af2f  -> ACCEPT-CA-74: PASS legs=11/11
reports/round-74/accept-c.py   --root . --lands c4bf61a8d722 --freeze 00c408a0af2f  -> ACCEPT-C-74:  PASS legs=13/13
```

## Verdict of the attack: FAILED — the claim survived

Every round-74 junk fixture is rejected; **no** fixture was accepted; every fixture carries its
junk-specific failure on the leg the fixture names. The round-73 survivors reproduce exactly.
Two evidence-integrity defects and one control-design defect were found (F1–F7); none lets a junk
landing through the round-74 counters.

### Round-73 red-before (my re-run, identical to the committed table)

`python3 -B $D/junk-fixtures-main.py --run-r73` is the head of the same sweep (the CLI runs both
tables when both flags are given); the table below is my re-run, byte-identical to the committed one
after normalising fixture repo paths/hashes.

| fixture | claim | my re-run | accepted? |
|---|---|---|---|
| P0 baseline (no junk) | C / Ca | PASS 11/11; PASS 9/9 | — |
| P0b do-nothing (`--lands=base`) | C | FAIL 1/11 (10 legs red) | — |
| J1 header-only stubs | C | FAIL 10/11 red=ENTRIES | no |
| J2 Gate quotes absent | C | FAIL 10/11 red=EVIDENCE | no |
| J3 claims.json shrink (in tree) | C | **PASS 11/11** | **YES (survivor)** |
| J4 literal constant printers | Ca | FAIL 4/9 red=LEDGER,BASEMISMATCH,REPAIR,ANNOTATE,NOSTUB | no |
| J4b evasive constant printer | Ca | **PASS 9/9** | **YES (survivor)** |
| J5 stub correction row | Ca | **PASS 9/9** | **YES (survivor)** |
| J6 frozen r72 receipt edited | Ca | **PASS 9/9** | **YES (survivor)** |
| J7 incidental claim-C citation | Ca | **PASS 9/9** | **YES (survivor)** |

`SURVIVORS ... J3 J4b J5 J6 J7` — reproduced verbatim. These are the round-73 holes; each round-74
counter closes its counterpart: J3 → `ROWS`+`FROZENCFG` (defence in depth: ROWS, REPOINTED, GATE and
EVIDENCE all fire too), J4b → `FROZENCFG` plus the semantic guard (see F2), J5 → `ANNOTATE`+`NOSTUB`,
J6 → `APPENDONLY`, J7 → `SEPARABLE`.

### Round-74 junk landings (my re-run, freeze `00c408a0af2f`)

| fixture | claim | committed | my run | junk-specific delta on the named leg | accepted? |
|---|---|---|---|---|---|
| T0 (no defect) | C | PASS 13/13 | PASS 13/13 | — | — |
| T0 (no defect) | Ca | FAIL 9/11 APPENDONLY,SEPARABLE | FAIL 9/11 same | none (expected PASS — see F1) | — |
| J1 stubs+staged rows | C | FAIL 9/13 ENTRIES,ROWS,CENSUS,INDEX | FAIL 9/13 identical | ENTRIES+ROWS | no |
| J2 fabricated windows | C | FAIL 12/13 EVIDENCE | FAIL 12/13 identical | EVIDENCE | no |
| J3 graded-tree claims shrink | C | FAIL 8/13 | FAIL 8/13 identical | ROWS/REPOINTED/GATE/EVIDENCE/FROZENCFG | no |
| J9 leg deleted | C | FAIL 12/13 FROZENCFG | FAIL 12/13 identical | FROZENCFG | no |
| J4 literal printers | Ca | FAIL 8/11 APPENDONLY,SEPARABLE,FROZENCFG | identical | FROZENCFG only (F2) | no |
| J4b evasive printer | Ca | FAIL 8/11 APPENDONLY,SEPARABLE,FROZENCFG | identical | FROZENCFG only (F2) | no |
| J5 stub correction row | Ca | FAIL 7/11 ANNOTATE,NOSTUB,APPENDONLY,SEPARABLE | identical | ANNOTATE+NOSTUB | no |
| J6 r73 rerun receipt edited | Ca | FAIL 9/11 APPENDONLY,SEPARABLE | identical | APPENDONLY names `.../measures-ca72-rerun.txt` | no |
| J7 claim-C citation | Ca | FAIL 9/11 APPENDONLY,SEPARABLE | identical | SEPARABLE names `corrections-rows` | no |
| J8 typed r73 Ca receipt | Ca | FAIL 8/11 APPENDONLY,SEPARABLE,RECEIPTS | identical | RECEIPTS | no |
| J9 leg deleted | Ca | FAIL 8/11 APPENDONLY,SEPARABLE,FROZENCFG | identical | FROZENCFG | no |

`# ACCEPTED JUNK LANDINGS: none` — reproduced.

My first full sweep differed on four entries (J1, J7, J8 `exit: 2 / verdict:` empty; T0 an extra
`RECEIPTS` red) because `/tmp` filled (`No space left on device`). Each was re-run alone from the
generator library and then matched the committed receipt exactly:

```
probe J1  -> LEG FAIL ENTRIES / ROWS / CENSUS / INDEX ; ACCEPT-C-74: FAIL legs=9/13   (15.6 s)
probe J7  -> LEG FAIL APPENDONLY / SEPARABLE         ; ACCEPT-CA-74: FAIL legs=9/11  (17.8 s)
probe J8  -> LEG FAIL APPENDONLY / SEPARABLE / RECEIPTS ; ACCEPT-CA-74: FAIL legs=8/11 (58 s)
probe T0  -> LEG FAIL APPENDONLY / SEPARABLE         ; ACCEPT-CA-74: FAIL legs=9/11  (13.7 s)
```

So the committed verdicts are reproducible; the receipt is not robust to disk pressure (F6, F7).

## Findings

### F1 — HIGH — the reference landing T0 is red on the Ca counter, and the sweep has no green-baseline gate

`T0` is defined as the intended landing with no defect and expected to PASS
(`R74_FIXTURES["T0"] = ("C+Ca", None, "PASS: the intended round-74 landing with no defect (reference)")`),
but it is red:

```
T0 C: PASS legs=13/13 exit=0
T0 Ca: FAIL legs=9/11 exit=1 red=APPENDONLY,SEPARABLE
T0 LEG FAIL APPENDONLY
     ... problems=['corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]']
T0 LEG FAIL SEPARABLE
     ... problems=['cites <redacted lane id> in reports/round-74/telemetry/controls-ca.txt', ...]
```

Reproduced in the sweep and in a clean single run. Unlike `_run_r73` (which prints
`HARNESS ERROR: the unjunked replay is not green on both counters` and returns `None`), `_run_r74`
prints T0 and continues. Consequence: all 7 Ca fixtures carry both legs red, so a fixture's verdict
does **not** attribute its failure; only the problem-list delta does. I verified the deltas are
present (J6 adds `reports/round-73/telemetry/measures-ca72-rerun.txt: changed lines ...`;
J7 adds the three-problem list starting `cites <redacted lane id> in corrections-rows`), so the
counter *does* discriminate. But the sweep's headline "every junk FAILs" would also be produced by a
counter that simply rejected the intended tree.

The two causes are known and disclosed in `reports/round-74/telemetry/junk-ca.txt:65` but not in the
run receipt: (1) claim C's in-place used-by change is not a REPAIR `stated_at` line of claim Ca;
(2) the freeze still carries the pre-redaction `controls-ca.txt`. I independently confirmed the
claim made there: `accept-ca.py --lands 5e4796c0cb6a --freeze 00c408a0af2f` is `PASS legs=11/11`.

Proposed fix: make the kit's baseline the *measured* shape — build T0 from the Ca landing's
regenerated controls receipt and add the C-side used-by edit to Ca's REPAIR `stated_at` set (or scope
APPENDONLY to the graded claim's own landing) — and restore the round-73 hard gate: abort the table
if T0 is not green on both counters. If T0 stays red by frozen-claims construction, change the T0
expected text to the measured `FAIL legs=9/11` and mark the table as delta-attributed.

### F2 — MEDIUM — J4/J4b never exercise the LEDGER leg; FROZENCFG is class-blind

`leg_ledger` reads the ledger only from the freeze (`ledger_raw`; detail string
`a worktree copy is never read`), so a graded-tree ledger edit can never reach it. The only red leg
J4/J4b add is FROZENCFG, which compares blob ids — it fires for *any* ledger byte change, including a
benign one. So the round-73 M1b evasive-printer class is not red-before-tested at round 74, even
though the expected text names it.

The counter's semantics are sound; I probed the guard directly:

```
observe_problem(["python3","-c","import os;assert os.sep;print(str('804'))"], "/tmp")
  -> shell construct ';' in argv element "import os;assert os.sep;print(str('804'))"
```

and `selftest-ca.txt` records `selftest: constant-printer -> exit=1 LEDGER=FAIL`. So the class is
covered by the counter's own selftest, not by this fixture.

Proposed fix: add a fixture whose *freeze* carries the evasive printer (rewrite the ledger in the
freeze commit and leave the landing's ledger untouched on that path) so LEDGER is the firing leg; or
rename the expectation to "FROZENCFG pin (any ledger byte change, class-blind)".

### F3 — HIGH — the Ca telemetry split hand-rewrites a counter line

`reports/round-74/telemetry/junk-ca.txt` is presented as `split from counters/junk-r74-run.txt by the
L1`, but the J7 expectation differs from the source receipt. Both are committed at `main`:

```
junk-r74-run.txt:205  expected: FAIL: a Ca-read corrections row cites claim-C rows S881..S884 (SEPARABLE)
junk-ca.txt:146       expected: FAIL: a Ca-read corrections row cites claim-C rows the claim-C lane ids (SEPARABLE)
```

A mechanical diff of the two committed blobs shows exactly this rewrite plus an added
`# NOTE (L1, 2026-10-25) ...` block at `junk-ca.txt:65`; the C split is otherwise faithful. This is
the typed-receipt class the round itself attacks (J8). Verdicts are unaffected, but a committed
evidence file does not reproduce from its generator.

Proposed fix: regenerate the split with `git show main:.ufo/waves/round-74/counters/junk-r74-run.txt`
and a script (no hand edits); if redaction is the goal, apply it in the generator so source and split
agree, and record the transformation.

### F4 — MEDIUM — the documented reproduction at the freeze is impossible

The freeze's generator has no round-74 mode:

```
$ git -C "$D/lane" --no-pager show 00c408a0af2f:.ufo/waves/round-74/counters/junk-fixtures.py | wc -l
774
$ ... | grep -c run_r74
0
$ python3 -B .ufo/waves/round-74/counters/junk-fixtures.py --run-r73 --run-r74 --freeze 00c408... 
junk-fixtures.py: error: unrecognized arguments: --run-r74 --freeze 00c408...
```

The sweep was added after both lands: `1d7add3 round-74: junk-landing receipts ...` adds 735 lines to
the generator (`1481` lines, sha256 `ce6505fc…`, which is what the receipt header pins). Reproduction
is therefore only possible from `main`, not from the freeze — the seat brief's recipe fails at the
freeze.

Proposed fix: record the generator commit id in the receipt header (sha256 alone does not say where
to get it) and state "generator at main"; better, land the fixture generator in the freeze next round.

### F5 — LOW — `--only` is silently ignored by `--run-r74`

```
ap.add_argument("--only", ... "comma-separated fixture names (default: all)")
...
run_r74(freeze, workroot=args.workroot, keep=args.keep, out=fh)   # no only=
```

My `--only T0` invocation produced the full 11-fixture table (226 lines, 15m48s). A seat cannot
target a single round-74 fixture; the selector is accepted and discarded.

Proposed fix: `run_r74(freeze, only=only, ...)`.

### F6 — MEDIUM — the receipt discards stderr, so NO-VERDICT lines are unauditable

`run_counter` builds `out = stdout + stderr`, but `_print_block` prints only `exit`, `LEG FAIL` lines
and the verdict. Under disk pressure my sweep produced:

```
fixture: J1
exit: 2
verdict: 
```

with the actual reason only on stderr (`ERROR: clone of ... failed: fatal: failed to copy file ...
No space left on device`). A reader of the committed receipt cannot tell an environmental failure
from a counter refusal or a harness crash, and `_signature` renders both as `NO-VERDICT`.

Proposed fix: for NO-VERDICT (or any exit not producing a verdict) print the last stderr lines in the
fixture block.

### F7 — LOW — RECEIPTS clones into `/tmp` every run; verdicts flip when `/tmp` is full

At 750 MB free on a 128 GB XFS `/tmp`:

```
fixture J7 ... ACCEPT-CA-74: FAIL legs=8/11        # committed: 9/11
stderr: ERROR: clone of ... failed: fatal: failed to copy file to
        '/tmp/r74-ca-rq2ttfnt/r73lands/.git/objects/27/29cd6480...': No such file or directory
```

At 1.7 GB free the same fixture is `FAIL legs=9/11` exactly as committed; a third attempt at full
`/tmp` exited 2 with `No space left on device` on `.../lands/.git/objects/87/...`. The RECEIPTS leg
materialises a clone of the graded tree (and the round-73 lands), so the Ca counter's verdict is
resource-sensitive. This is operational, not logical, but the receipt states no disk requirement.

Proposed fix: fail fast with a clear pre-flight message when the temp filesystem is short, and record
the requirement (each Ca run materialises at least one full clone) in the receipt header.

## Observations (not defects I attribute to the round)

- O1: during my run, the worktree copy of `.ufo/waves/round-74/counters/junk-r74-run.txt` was
  transiently truncated to 0 bytes (`git status` showed ` M`) and later restored to the committed
  bytes (29 399 bytes, sha256 `081e11f2…`). I did not write it and did not restore it. The committed
  blob (git `d89426a0…`) was intact throughout, and all my comparisons use the committed blob.
- O2: the J7 SEPARABLE problem list carries two pre-existing problems (both citing
  `reports/round-74/telemetry/controls-ca.txt`) plus the junk-specific `corrections-rows` problem —
  further evidence for F1's attribution caveat.

## Risks / blockers

- No blocker for the claim. The round-74 counters reject all 11 junk landings and close all five
  round-73 survivors; the counters pass at both real landings (13/13, 11/11).
- Residual risk: because T0 Ca is red, the Ca column's evidence is delta-based; if a future fixture's
  junk lands on a leg that is already red at T0, the receipt would show a FAIL that is not
  attributable. That is a control-design risk (F1), not a live acceptance hole.
- Residual risk: F3 means at least one committed evidence file was edited after generation; any
  future split must be regenerated mechanically.

## Evidence

Reproduction is from the committed generator
(`git show main:.ufo/waves/round-74/counters/junk-fixtures.py`, sha256 `ce6505fc…`) and the freeze
commit. My scratch under `/tmp/ExecJunkReRun.oBjdtm/` (`junk-fixtures-main.py`, `t0.txt` full sweep,
`committed.txt` = committed receipt blob, `probe.py`, `j7-full.txt` ENOSPC capture) is ephemeral and
may be removed; every finding above is reproducible from the lane's committed blobs with the commands
shown.
