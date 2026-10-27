# ExecAdaptJunk — round-76 junk-landing fixtures (WAVE 1, staged)

Seat: `ExecAdaptJunk` (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base
`98c486bdb4650ba5b8e651d332910e8ee60ad121`. Nothing was written outside
`.ufo/waves/round-76/w1/` and my scratch root; the lane's git/jj state, fleet repo, `reports/round-76/`
and every protected file are untouched. No tool installs.

**Deliverable:** `.ufo/waves/round-76/w1/stage/ExecAdaptJunk/junk-fixtures.py` — the round-75 generator
adapted for round 76, with `--round` / `--c-counter` / `--ca-counter` / `--work` support.
`1986` lines, `sha256 f8f71d0f565959f21b3589283749567b0e04d9f7551044be520c6213013d57ca`
(`sha256sum …/junk-fixtures.py`; `wc -l …/junk-fixtures.py` → `1986 junk-fixtures.py`).

Artifacts (same directory): `round-75-redbefore/junk-run.txt` (full run table, 22,454 bytes),
`round-75-redbefore/r1exempt-green.txt`, `round-75-redbefore/r1exempt-red.txt`.

## 1. What the adaptation does

Source: `.ufo/waves/round-75/counters/junk-fixtures.py`
(`sha256 3fa5c6932dfc780e51182e578c25ad7bef33abe819a6dd66697216140b0a4fd2`). The semantics of every
fixture are unchanged; the mechanical changes are:

1. **Round is configuration, read from the frozen claims.** `ROUND = 76` is only a default;
   `--round N` rebuilds `CFG = round_config(N)`, which yields
   `reports/round-N/{claims,ledger,evidence,telemetry}`, `corpus/lessons/round-N.md`,
   `reports/round-N/accept-{c,ca}.py`, the previous round's
   `accept-ca-(N-1)-at-lands.txt` and the `ACCEPT-C-N` / `ACCEPT-CA-N` prefix. `main()` reads
   `git show <freeze>:reports/round-N/claims.json` and (a) refuses when the file is unreadable and no
   `--base` was given, (b) refuses when its `round` differs from `--round`, (c) takes `base` from it
   when `--base` is omitted. `_round_of()` no longer defaults to 75.
   Measured: `--base` omitted resolved `# base: f556d1049fe651d3d63975600b13acd9fb686f15` from the
   round-75 claims (section 3, E5e).
2. **Verdicts are round- and claim-scoped.** `ACCEPT_RE` captures the round token; `verdict_is_for()`
   turns a verdict from another round or the other claim into `NO-VERDICT` (never a PASS).
3. **`--c-counter` / `--ca-counter`** override the counter path for every fixture and for the
   baselines (`_counter_path(..., override=…)`); otherwise the graded tree's
   `reports/round-N/accept-c.py`, then `.ufo/waves/round-N/counters/accept-c.py` is used.
4. **`git clone --shared`** replaces the mirror-clone-then-clone pair; the
   `git rev-parse --show-toplevel` assertion before every commit is kept.
5. **Scratch:** `resolve_workroot()` = `--work`/`--workroot`, else
   `$HYAKU_SCRATCH/kotodama-r<N>/junk-fixtures`, else `$TMPDIR/kotodama-r<N>-junk-fixtures`, else
   `/fast/scratch/hyaku/kotodama-r<N>/junk-fixtures`; a root inside `tempfile.gettempdir()` is
   refused, and there is no system-temp fallback. `grep -nE '"/tmp|/tmp/' junk-fixtures.py` prints
   nothing (exit 1, section 3). `TMPDIR` is never hardcoded.
6. **Derived file sets:** `protected_set()` (round N-1/N-2 lessons, LOG, SCORECARD, QUALITY, SHONEN,
   the two previous rounds' `claims.json`/`ledger.json`), `j10_candidates()` (previous lesson first),
   and `_j6_receipts()` (static older receipts, then a scan of rounds N-2/N-3 telemetry excluding the
   protected set, `stated_at` and the round's pinned `accept-ca-(N-1)-at-lands.txt`).
7. **J9's typed receipt** is built from `CFG`: `reports/round-N/telemetry/accept-ca-(N-1)-at-lands.txt`
   carrying `ACCEPT-CA-(N-1): PASS legs=12/12` (`PREV_LEGS = 12`, round-75's measured leg count),
   `# counter: reports/round-(N-1)/accept-ca.py`, and three disagreeing revisions.
8. **Own-freeze fixtures (J4f) are pinned correctly** — the one behavioural fix, see F1.
9. Round-75 literals in output headers, receipt headers, `--list`, help text and the docstring were
   parameterized; the file's own docstring documents the round-token model and the scratch rule.

## 2. Red-before against the round-75 counters (measured)

Command (exact):

```
cd .../.ufo/waves/round-76/w1/stage/ExecAdaptJunk
S=/fast/scratch/hyaku/kotodama-r76/ExecAdaptJunk
env HYAKU_SCRATCH="$S/env" TMPDIR="$S/env/tmp" \
python3 -B junk-fixtures.py --run --round 75 \
  --freeze 5d0167464309d8133991b30f7d7a7011a6a0fd14 \
  --lands  4f5e3b2535c2c06c51627dc2736c40183847cae1 \
  --base   f556d1049fe651d3d63975600b13acd9fb686f15 \
  --c-counter  /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-75/accept-c.py \
  --ca-counter /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-75/accept-ca.py \
  --workroot "$S/run" --out-dir round-75-redbefore --out "$S/junk-r75-final.txt"
```

Raw result: `exit=0`, wall `201.03s`, `16` fixture blocks (`grep -c '^fixture:'` → `16`), final line
`# ACCEPTED JUNK LANDINGS: none`.

| fixture | claim | expected leg(s) | measured red legs | named leg red? |
|---|---|---|---|---|
| J1 | C | ENTRIES | ENTRIES, INDEX, REPOINTED, ROWS | yes |
| J2 | C | EVIDENCE | EVIDENCE | yes |
| J3 | C | FROZENCFG | FROZENCFG | yes |
| J4 | Ca | LEDGER, FROZENCFG | APPENDONLY, COMBINED, FROZENCFG | FROZENCFG yes / LEDGER **no** |
| J4b | Ca | LEDGER, FROZENCFG | APPENDONLY, COMBINED, FROZENCFG | FROZENCFG yes / LEDGER **no** |
| J4c | Ca | LEDGER, FROZENCFG | APPENDONLY, COMBINED, FROZENCFG | FROZENCFG yes / LEDGER **no** |
| J4m | Ca | LEDGER, FROZENCFG | APPENDONLY, COMBINED, FROZENCFG | FROZENCFG yes / LEDGER **no** |
| J4f | Ca | LEDGER | ANNOTATE, APPENDONLY, BASEMISMATCH, COMBINED, LEDGER, NOSTUB, REPAIR | **yes (after the F1 fix)** |
| J5 | Ca | ANNOTATE, NOSTUB | ANNOTATE, APPENDONLY, COMBINED, NOSTUB | yes / yes |
| J6 | Ca | APPENDONLY | APPENDONLY, COMBINED | yes (baseline-red, see F4) |
| J7 | Ca | APPENDONLY | APPENDONLY, COMBINED | yes (baseline-red) |
| J8 | Ca | SEPARABLE | APPENDONLY, COMBINED, SEPARABLE | yes |
| J9 | Ca | RECEIPTS, STAMP | APPENDONLY, COMBINED, RECEIPTS | RECEIPTS yes / STAMP **no** |
| J10 | Ca | APPENDONLY | APPENDONLY, COMBINED | yes (baseline-red) |
| G | Ca | APPENDONLY green | ANNOTATE, COMBINED, NOSTUB, RECEIPTS, REPAIR | APPENDONLY **PASS** (as expected) |
| R | Ca | APPENDONLY red | + APPENDONLY | yes |

R1EXEMPT pair receipts (`round-75-redbefore/`):

```
grep -nE '^(appendonly|other-legs-unchanged|verdict|# legs-differing-from-counterpart|# sources-delta-is-one-changed-line):' r1exempt-green.txt r1exempt-red.txt
# green: appendonly: PASS / other-legs-unchanged: yes / verdict: AS-EXPECTED
#        # legs-differing-from-counterpart: APPENDONLY
# red:   appendonly: FAIL / other-legs-unchanged: yes / verdict: AS-EXPECTED
#        # legs-differing-from-counterpart: APPENDONLY
# both:  # sources-delta-is-one-changed-line: yes
```

Both receipts carry `# sources-delta-vs-base: 1	1	corpus/SOURCES.md`, the edited row (`S001`) and
cell (`used-by` index 11, rule-2 yes / `teaches` index 7, rule-2 no), so the pair is reproducible.

## 3. Other retained evidence

**E1 — no `/tmp` root.**
```
$ grep -nE '"/tmp|/tmp/' junk-fixtures.py
$ echo "grep-exit=$?"
grep-exit=1
```

**E2 — selftest.** `python3 -B junk-fixtures.py --selftest` → `SELFTEST: PASS`, `selftest-exit=0`.
New cases over round 75: round paths (`round_config(75)`), previous-round receipt/counter,
`CFG.round == ROUND`, protected-set precedence, `verdict_is_for` for right round / wrong round /
wrong claim / non-verdict, `_forbidden_scratch` refusal of a temp root, explicit root,
`$HYAKU_SCRATCH` precedence.

**E3 — fixture table.** `--list` first line `# round 76 (claims reports/round-76/claims.json)`,
16 fixture rows (J1–J10, G, R) — `--list | grep -cE '^(J|G|R)'` → `16`.

**E4 — default scratch (empty `TMPDIR`/`HYAKU_SCRATCH`).**
```
default workroot: /fast/scratch/hyaku/kotodama-r76/junk-fixtures
r76 claims: reports/round-76/claims.json | r76 lesson: corpus/lessons/round-76.md | r76 prev: accept-ca-75-at-lands.txt
protected: ('LOG.md', 'SCORECARD.md', 'corpus/lessons/round-75.md', 'corpus/lessons/round-74.md', 'corpus/QUALITY.md', 'SHONEN.md', 'reports/round-75/claims.json', 'reports/round-75/ledger.json', 'reports/round-74/claims.json', 'reports/round-74/ledger.json')
j10: ('corpus/lessons/round-75.md', 'corpus/lessons/round-74.md', 'LOG.md', 'SCORECARD.md')
```

**E5 — refusal/derivation paths (round-75 freeze, `--round 76`).**
```
$ … --run --freeze 5d016746… --lands 4f5e3b2…
ERROR: cannot read reports/round-76/claims.json at the freeze 5d016746… and no --base was given
exit=2
$ … --run --round 75 --freeze 5d016746… --c-counter /nope/accept-c.py
ERROR: --c-counter /nope/accept-c.py does not exist
exit=2
$ … --run --round 75 --freeze 5d016746… --lands 4f5e3b2… --only J3   (no --base)
# base: f556d1049fe651d3d63975600b13acd9fb686f15
verdict: ACCEPT-C-75: FAIL legs=12/13 / red-legs: FROZENCFG
# ACCEPTED JUNK LANDINGS: none
```

**E6 — no system-temp litter.** `find /tmp -maxdepth 2 \( -name '*kotodama-r75*' -o -name 'r75-ca-*'
-o -name 'jf-*' -o -name 'junk-r75*' \) -printf '%p\n'` printed nothing after the 16-fixture sweep
(the counters were given `TMPDIR` and `HYAKU_SCRATCH` inside my scratch).

**E7 — the adapted run reproduces the committed round-75 receipts.** `reports/round-75/telemetry/junk-c.txt`
(J1 `9/13`, J2 `12/13`, J3 `12/13`, same red legs) and `junk-ca.txt` agree with the table above for
every fixture except J4f; e.g. J4 there is `LEG PASS LEDGER … LEG FAIL FROZENCFG`, `ACCEPT-CA-75: FAIL legs=9/12`.

## 4. Findings

**F1 (fixed in the staged file; measured).** Round 75's J4f never reached its named leg. Its committed
receipt (`reports/round-75/telemetry/junk-ca.txt`, J4f block) shows `LEG PASS LEDGER`,
`LEG FAIL FROZENCFG`, `lands == reference-lands == 8233ddb…` and `--freeze 5d01674…`. Two causes:
(a) `_run_fixtures` passed the CLI `--freeze`, not the fixture's own freeze, so the counter read the
clean frozen ledger; (b) the own-freeze branch made `lands == freeze`, exactly the shape the Ca
counter's FROZENCFG clause refuses to pass, so the LEDGER clause could not be isolated. My run
reproduced this with the adapted-but-unfixed file (same leg table, `FROZENCFG` red, `LEDGER` pass).
Fix: `run_counter(..., fx.freeze, ...)` and, for own-freeze fixtures, a second **empty child** commit
as the landing. Measured after the fix (J4f section of `junk-run.txt`, round-75 counters):
```
LEG FAIL LEDGER … LEG PASS FROZENCFG … LEG PASS STAMP
lands: af23d8031c64444c26eeff3611b25dfe414f2492   reference-lands (the defective freeze): 9d455b0b4b0e6b1a36d2963381e4e52737f76e79
verdict: ACCEPT-CA-75: FAIL legs=5/12   red-legs: ANNOTATE, APPENDONLY, BASEMISMATCH, COMBINED, LEDGER, NOSTUB, REPAIR
```
The extra red legs (ANNOTATE, BASEMISMATCH, NOSTUB, REPAIR) are the pair-derived legs of a counter
that has refused the frozen ledger — observed, and consistent with a cascade; the mechanism was not
traced line-by-line in the counter. `[INFERENCE]` on the cause, measured on the leg table.

**F2.** `J4, J4b, J4c, J4m` declare `(LEDGER, FROZENCFG)` but the round-75 counter only ever reddens
`FROZENCFG`: a tree-level ledger edit is caught as a freeze-byte difference before the LEDGER allowlist
clause runs. Identical to the committed round-75 receipt, so it is inherited, not a regression. If
round 76 wants the LEDGER clause exercised by those mutations too, the same own-freeze treatment as
F1 applies (they would then also pin their own freeze).

**F3.** `J9` declares `(RECEIPTS, STAMP)`; only `RECEIPTS` fires — `STAMP` stays green because the
typed receipt's stamps are consistent *with each other* in the way the STAMP leg reads them, while the
stdout cannot be re-derived. Committed round-75 receipt is identical.

**F4.** `J6, J7, J10` show `newly-red: (none)` because APPENDONLY is already red on the unmutated
reference lands `4f5e3b2` (`baseline-legs: … APPENDONLY=FAIL, COMBINED=FAIL …`), so the named leg is
red but not attributable to the mutation by the `newly-red` column. The committed round-75 receipt shows
the same. Why the Ca-landing tree fails APPENDONLY at that reference is **not investigated** (unrun) —
it is inherited from round 75's own instrument.

**F5.** The round-75 counters' selftest scratch falls back to `tempfile.gettempdir()` when neither
`HYAKU_SCRATCH` nor `SHOKUNIN_SCRATCH` is set (`reports/round-75/accept-c.py:4443-4450`); the harness
sets both, and nothing landed in the system temp dir (E6). The round-76 counters' own `--work` support
is a sibling seat's file, not this one.

## 5. Risks / what the L1 must re-derive at the freeze

* `reports/round-76/claims.json` and `ledger.json` do not exist yet, so **no round-76 grading has been
  run** (explicitly unrun). All round-76 defaults in the staged file are provisional:
  `PREV_LEGS = 12` (round-75's measured `legs=n/12`), the derived `protected_set()` (J10 hits
  `corpus/lessons/round-75.md`; J6 uses round-74/73 receipts), and J9's assumption that
  `reports/round-76/telemetry/accept-ca-75-at-lands.txt` is the receipt the RECEIPTS leg re-grades.
  If the frozen counter's protected set differs, re-check J6 (must stay *outside* it) and J10 (must hit
  a file *inside* it), or APPENDONLY will not redden as named.
* J5 requires `SCORECARD.md` to carry `## Corrections — round 76` with one row per ANNOTATE pair at the
  landing; J2 requires `reports/round-76/evidence/<row>.txt` files with a `--- window ---` block;
  J8's appended row uses the pair's `stated_text`/`expected_after`/`rederive` keys — the frozen ledger
  must keep those key names.
* The staged file is not installed; only the L1 copies it to `reports/round-76/` at the freeze.
* Scratch `/fast/scratch/hyaku/kotodama-r76/ExecAdaptJunk/` held ~16 shared clones during the sweep and
  is deleted per the seat rule; the run table and receipts were copied into the wave directory first,
  so the receipt paths that name scratch directories are historical (as in round-75's committed receipts).

Report: .ufo/waves/round-76/w1/ExecAdaptJunk.md
