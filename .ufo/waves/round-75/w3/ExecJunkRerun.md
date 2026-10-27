# ExecJunkRerun — round 75, WAVE 3 (falsify): junk-landing controls

Seat: ExecJunkRerun (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Revisions: base `f556d1049fe651d3d63975600b13acd9fb686f15`, freeze
`5d0167464309d8133991b30f7d7a7011a6a0fd14`, Ca landing `012e8d3c8b92f47c734f735d58d118d574fe6a14`,
C landing `4f5e3b2535c2c06c51627dc2736c40183847cae1`. The C landing commits on top of the Ca
landing (`git merge-base --is-ancestor 012e8d3 4f5e3b2` → true), so `4f5e3b2` is the *combined* tree.
Lane main at dispatch `82ced5c` (telemetry/report commits only).

## 0. Verdict

**PARTIAL — the headline reproduces, the control does not cover what it declares.**

* Reproduced five times, including the exact assignment command: **no fixture is ACCEPTED**
  (`accepted: no` for all 16; `# ACCEPTED JUNK LANDINGS: none`). The claim
  "junk sweep … no junk landing accepted" (lesson r75 l.419) **HOLDS as stated**.
* But the sweep cannot show *why* six of its fixtures are rejected, and three of its declared
  expected legs never go red at all (§4 D1–D4). The committed leg table is also not reproducible
  under concurrent seat load (§4 D5).
* Acceptance is monotone-safe: `accepted` requires `ACCEPT-*: PASS` on the counter's stdout, so the
  instabilities below can only cause **false rejection**, never a false ACCEPT
  (`junk-fixtures.py:1435`, `res["verdict"] == "PASS"`).

Method (no lane writes): scratch clone
`D=/fast/scratch/hyaku/kotodama-r75/ExecJunkRerun/base-b5Hh`;
`git -C …/lane rev-parse --show-toplevel` printed the scratch path; every git call named `-C`;
fixture commits used `-c user.name=fixture -c user.email=f@f.invalid` inside the fixture clones only.
No tool installs were made.

Exact rerun command (only `--workroot`/`--out-dir`/`--out` point at my scratch; the harness clones
the lane at `LANE` read-only, which I verified — the lane's `git status` was not touched):

```
python3 -B <lane>/.ufo/waves/round-75/counters/junk-fixtures.py --run \
  --freeze 5d0167464309d8133991b30f7d7a7011a6a0fd14 \
  --base   f556d1049fe651d3d63975600b13acd9fb686f15 \
  --lands  4f5e3b2535c2c06c51627dc2736c40183847cae1 \
  --workroot <scratch>/work --out-dir <scratch>/receipts --out <scratch>/junk-rerun.txt
```

## 1. The table (primary sweep, isolated counter scratch, baseline graded)

`†` = the REPAIR red on that row is the transient scratch failure of §4 D5, not a fixture property
(the same revision passes REPAIR when re-run alone).

| fixture | mutation (short) | verdict | accepted | red legs | newly-red vs baseline | expected legs |
|---|---|---|---|---|---|---|
| J1 | two header-only stub entries + used-by repointed | ACCEPT-C-75: FAIL 9/13 | no | ENTRIES, INDEX, REPOINTED, ROWS | ENTRIES, INDEX, REPOINTED, ROWS | ENTRIES |
| J2 | Gate quote removed from 9 evidence windows, sha recomputed | ACCEPT-C-75: FAIL 12/13 | no | EVIDENCE | EVIDENCE | EVIDENCE |
| J3 | graded-tree claims.json shrunk to 2 rows / 1 entry | ACCEPT-C-75: FAIL 12/13 | no | FROZENCFG | FROZENCFG | FROZENCFG |
| J4 | every observe_cmd → literal constant printer | ACCEPT-CA-75: FAIL 9/12 | no | APPENDONLY, COMBINED, FROZENCFG | FROZENCFG | LEDGER, FROZENCFG |
| J4b | evasive constant printer (`import os;assert os.sep;print(...)`) | ACCEPT-CA-75: FAIL 9/12 | no | APPENDONLY, COMBINED, FROZENCFG | FROZENCFG | LEDGER, FROZENCFG |
| J4c | observe_cmd as one shell string with metacharacters | ACCEPT-CA-75: FAIL 9/12 | no | APPENDONLY, COMBINED, FROZENCFG | FROZENCFG | LEDGER, FROZENCFG |
| J4m | ledger trimmed to 2 pairs | ACCEPT-CA-75: FAIL 8/12 | no | APPENDONLY, COMBINED, FROZENCFG, REPAIR† | FROZENCFG, REPAIR† | LEDGER, FROZENCFG |
| J4f | FROZEN ledger itself constant-prints (own-freeze fixture) | ACCEPT-CA-75: FAIL 9/12 | no | APPENDONLY, COMBINED, FROZENCFG | FROZENCFG | LEDGER |
| J5 | Corrections row for L75-04 reduced to `\| L75-04 \|` | ACCEPT-CA-75: FAIL 8/12 | no | ANNOTATE, APPENDONLY, COMBINED, NOSTUB | ANNOTATE, NOSTUB | ANNOTATE, NOSTUB |
| J6 | frozen receipt outside the protected set edited in place | ACCEPT-CA-75: FAIL 10/12 | no | APPENDONLY, COMBINED | **(none)** | APPENDONLY |
| J7 | teaches-cell edit smuggled beside a used-by edit, row S001 | ACCEPT-CA-75: FAIL 10/12 | no | APPENDONLY, COMBINED | **(none)** | APPENDONLY |
| J8 | Corrections row citing claim-C lane id S885 | ACCEPT-CA-75: FAIL 9/12 | no | APPENDONLY, COMBINED, SEPARABLE | SEPARABLE | SEPARABLE |
| J9 | hand-typed receipt, zeroed counter sha, three disagreeing stamps | ACCEPT-CA-75: FAIL 8/12 | no | APPENDONLY, COMBINED, RECEIPTS, REPAIR† | RECEIPTS, REPAIR† | RECEIPTS, **STAMP** |
| J10 | one line removed from protected `corpus/lessons/round-73.md` | ACCEPT-CA-75: FAIL 9/12 | no | APPENDONLY, COMBINED, REPAIR† | REPAIR† | APPENDONLY |
| G | only a rule-2 (used-by) cell edit, row S001 | ACCEPT-CA-75: FAIL 7/12 | no | ANNOTATE, COMBINED, NOSTUB, RECEIPTS, REPAIR | (none) | APPENDONLY |
| R | only a non-rule-2 (teaches) cell edit, row S001 | ACCEPT-CA-75: FAIL 6/12 | no | ANNOTATE, APPENDONLY, COMBINED, NOSTUB, RECEIPTS, REPAIR | APPENDONLY | APPENDONLY |

**Fixtures ACCEPTED: none.** Baselines: the C landing baseline is fully green
(`CENSUS…SCRATCHMIRROR = PASS`, 13/13); the Ca landing baseline is **already red**
(`ANNOTATE=PASS, APPENDONLY=FAIL, BASEMISMATCH=PASS, COMBINED=FAIL, FROZENCFG=PASS, LEDGER=PASS,
NOSTUB=PASS, R1EXEMPT=PASS, RECEIPTS=PASS, REPAIR=PASS, SEPARABLE=PASS, STAMP=PASS`);
the freeze-tree baseline (G/R) is red on `ANNOTATE, NOSTUB, RECEIPTS, REPAIR, COMBINED`.

The R1EXEMPT pair is the only part that reproduces the committed receipts field for field
(`appendonly: PASS` / `FAIL`, `other-legs-unchanged: yes`, `sources-delta-is-one-changed-line: yes`,
`legs-differing-from-counterpart: APPENDONLY`, `verdict: AS-EXPECTED`, both halves).

## 2. Defects

### D1 — Ca fixtures are graded at claim C's landing, so APPENDONLY is red before any mutation
`build()` applies the Ca mutations to the reference tree `--lands 4f5e3b2` (= C landing, combined
tree). Claim C's `claims.json` declares `owned_inplace: corpus/README.md, base_line 376`
(`5d01674:reports/round-75/claims.json`), and `leg_appendonly` honours that set **only** under
`cfg["combined_exemptions"]` (`reports/round-75/accept-ca.py:1848`), which is set only inside
`leg_combined`'s private copy (`:2565`). Therefore at `4f5e3b2` the main APPENDONLY leg always fails:

```
$ python3 -B reports/round-75/accept-ca.py --root . --lands 4f5e3b2… --freeze 5d01674… \
      --fleet-root /home/vgpnk/Projects/shokunin
LEG FAIL APPENDONLY
     … rule2-edits=0 problems=['corpus/README.md: changed lines outside REPAIR stated_at lines [376]']
ACCEPT-CA-75: FAIL legs=10/12
```

Consequence: the Ca baseline is red (above), so **J6, J7 and J10 produce `newly-red: (none)`** — the
leg they are built to exercise was already failing on the unmutated tree. Their rejection is real
(the counter FAILs) but the sweep does not demonstrate that APPENDONLY discriminates the junk from
the clean tree at that reference. Only the R half of the R1EXEMPT pair (graded at the *freeze* tree,
where APPENDONLY is green) shows APPENDONLY flipping PASS→FAIL.

### D2 — COMBINED is never exercised: the harness never passes `--combined`
`run_counter` builds `--root/--lands/--freeze/--fleet-root` only
(`junk-fixtures.py:1047-1048`). Every Ca fixture therefore reports
`LEG FAIL COMBINED — the explicit --combined revision is required`, including the baseline. With the
frozen invocation's own value the leg passes:

```
… --lands 4f5e3b2… --combined 4f5e3b2… → LEG PASS COMBINED  (APPENDONLY still FAIL on :376)
```

So the sweep's COMBINED column is constant-red noise and the "combined-tree APPENDONLY" property is
untested by every junk landing.

### D3 — J4f is inert: the grading path discards the fixture's own freeze
`build()` returns `Fixture.freeze = rev` for the own-freeze fixture (`junk-fixtures.py:1184-1191`),
and `_grade_baseline` correctly uses `fx.freeze` (`:1404`). But the fixture grading call uses the
outer parameter instead:

```
1426:                res = run_counter(fx.repo, counter, fx.rev, freeze, claim=claim)
```

so the counter reads the *real* freeze ledger. Proof on the very same fixture tree
(`jf-J4f-…`, commit `ff29f634…`):

```
harness call (--freeze 5d0167…):            LEG PASS LEDGER   verdict ACCEPT-CA-75: FAIL legs=9/12
same tree, --lands=--freeze=ff29f634…:      LEG FAIL LEDGER   verdict ACCEPT-CA-75: FAIL legs=5/12
```

LEDGER is `PASS` in **every** fixture (J4, J4b, J4c, J4m, J4f) — `leg_ledger` reads only
`cfg["ledger_raw"]`, the ledger committed at `--freeze` (`:1337`). The constant-printer / argv
allowlist clause that J4/J4b/J4c/J4m/J4f exist to attack is therefore **never executed by any
fixture**; their only real signal is FROZENCFG (the graded tree differs from the freeze).

### D4 — declared expected legs are printed, never enforced; J9's STAMP cannot fire
`fx.expected_legs` is used only at `junk-fixtures.py:1459` (`print("expected-legs: …")`). No check
compares it to `newly-red`, so a fixture whose declared leg never reddens still counts as
"rejected". Two rows are already in that state: J4f (`LEDGER`, D3) and J9 (`RECEIPTS, STAMP`) —
`leg_stamp` validates the counter's *own* printed header (`accept-ca.py:2634-2663`), not a stored
receipt, so the hand-typed receipt's "three disagreeing stamps" is caught by RECEIPTS only
(`newly-red: RECEIPTS`). D1 makes J6/J7/J10 the same kind of vacuous row.

### D5 — the leg table is not reproducible under concurrent load (scratch dirs vanish mid-run)
Five sweeps of the same command produced disjoint REPAIR failures:

| sweep | counter scratch | REPAIR red on |
|---|---|---|
| A (assignment command) | default `/tmp` | J4, J4f, J5 (+G, R baseline) |
| B (debug copy, baseline) | default `/tmp` | J4b, J4c, J4m, J4f, J6, J7, J8, J9, J10 (+G, R) |
| C (isolated `HYAKU_SCRATCH`) | `/fast/…/ExecJunkRerun/cascratch` | G, R only |
| D (debug, baseline) | `/fast/…/cascratch4` | J4f (+G, R) |
| E (primary table above) | `/fast/…/cascratch2` | J4m, J9, J10 (+G, R) |

Verbatim errors from the dumps (the counter's fresh `mkdtemp` destination is deleted while the clone
runs; REPAIR's rederive then records "got None"):

```
ERROR: clone of …/dbgfull/jf-J4b-7u46cvwh/repo failed: fatal: failed to copy file to
 '/tmp/r75-ca-vakzg817/sweep-base/.git/objects/24/9a8ff8bd…': No such file or directory
ERROR: clone of …/dbgfull/jf-J6-dr1dwq2z/repo failed: fatal: failed to copy file to
 '/tmp/r75-ca-99y9k1x9/sweep-base/.git/objects/b8/bcce89a9…': No such file or directory
ERROR: clone of …/dbgfull2/jf-J4f-yflmpq98/repo failed: fatal: failed to copy file to
 '/fast/scratch/hyaku/kotodama-r75/ExecJunkRerun/cascratch4/kotodama-r75/r75-ca-1rjs4su1/r1-green/.git/objects/f1/bf4df49a…': No such file or directory
ERROR: checkout f726443f… failed: fatal: unable to read tree (33361e97…)
LEG FAIL REPAIR  red=['sweep red-before expected exit=1 first-footer 243/live 249; got None']
```

The destination is a private `tempfile.mkdtemp(prefix="r75-ca-")` (`accept-ca.py:2721`) that no code
in this process removes before `:2800`, and the failure follows the location (`/tmp` and `/fast`), so
the deletion is external to the counter. [INFERENCE] the host's concurrent seats run the same
counter with the same generic `r75-ca-` prefix and a shared/prefix-globbed scratch root; any
concurrent sweep of `r75-ca-*` kills an in-flight run. Isolation is not achieved by
`HYAKU_SCRATCH` alone (sweep D still lost a directory). The same fixture revision re-run alone is
stable: J4 `8/8 PASS` in one kept fixture and `PASS` on the first of three standalone harness runs,
J10 `3/3 PASS`; the flake only appears in multi-fixture sweeps.

### D6 — cosmetic: `reference-lands` is wrong for the own-freeze fixture
For J4f the report prints `reference-lands: ff29f634…` and `lands: ff29f634…` (identical), because
`build()` reassigns `reference = rev` before constructing the `Fixture` (`:1185-1191`). It hides the
fact that the diff base and the lands are the same commit.

## 3. What holds

* **No junk landing is ACCEPTED** — 5 sweeps, 16 fixtures each, plus isolated repeats:
  `# ACCEPTED JUNK LANDINGS: none` every time; every row `accepted: no`.
* The C section is well-formed: its baseline is 13/13 green and J1–J3 turn their declared legs red
  (J1 additionally INDEX and REPOINTED — over-catch, not a hole).
* J5 (ANNOTATE+NOSTUB), J8 (SEPARABLE) and J9 (RECEIPTS) hit exactly their declared legs.
* The R1EXEMPT pair reproduces the committed `r1exempt-green.txt` / `r1exempt-red.txt` verdicts:
  one changed SOURCES line, APPENDONLY PASS vs FAIL, every other leg unchanged.

## 4. Suggested repairs (advisory, for the owners of the control)

1. Pass `--combined 4f5e3b2…` in `run_counter` (D2), and grade the Ca section at a tree where main
   APPENDONLY is green — either Ca's own landing `012e8d3…`, or honour `claim_c_owned_inplace` in the
   main APPENDONLY leg so a combined-tree baseline can be green (D1). Without this, J6/J7/J10 stay
   vacuous.
2. `junk-fixtures.py:1426` → `run_counter(fx.repo, counter, fx.rev, fx.freeze, …)` (D3).
3. Enforce `expected_legs`: fail the sweep when a declared leg is not in `newly-red`; drop `STAMP`
   from J9 or make it reachable (D4).
4. Give each counter run a per-seat scratch root and pass it (`--work`) from the harness; make
   `materialize` retry once on ENOENT and make REPAIR's rederive distinguish "clone failed" from
   "instrument returned the wrong code" (D5).
5. Record the harness→counter argument mapping (`fx.freeze`, `--combined`) in the receipt, so the
   leg table can be re-derived exactly (D5/D6).

## 5. Evidence retained (copied from scratch before its deletion)

* `# ACCEPTED JUNK LANDINGS: none` — 5 full sweeps + 10 isolated fixture runs.
* Both Ca-landing counter runs at `4f5e3b2…` (no `--combined`: `FAIL legs=10/12`, APPENDONLY problem
  on `corpus/README.md:376`; with `--combined`: `LEG PASS COMBINED`, APPENDONLY still FAIL).
* J4f same-tree pair (`LEG PASS LEDGER` vs `LEG FAIL LEDGER`) at commit `ff29f634…`.
* The four `failed to copy file` / `unable to read tree` lines quoted in D5, from sweeps B and D.
* `r1exempt-green.txt` / `r1exempt-red.txt` field comparison against the committed receipts:
  identical on every verdict field.
