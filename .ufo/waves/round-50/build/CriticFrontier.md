# CriticFrontier — round 50 frontier step (mined mistake + fix-able-to-fail)

Seat: ChousaR27R2.CriticFrontier-4 (critic, leaf). Author-lane advice, not admission.
Assigned item: the frontier plan "mined mistake = r49 separability rejection; fix = Ca's
checker shown to fail on the r49 fixture". Attack (a) whether that meets "a fix counts only
once shown able to fail", (b) whether another mistake (r42–r49 lessons, rejected r36/42/43/44/47)
is more pressing. Measured 2026-10-21 against base `4ad2683` (read-only `git show`, no lane writes).
Installs: none.

## Verdict

Mining the r49 separability rejection is the right choice: it is the only open outside-review
disagreement. But the fix as declared is **not yet shown able to fail**, and round 50 **repeats
the r49 coupling**. In round 50, C cites registry rows that a different work unit writes. The
only change from r49 is that this unit is labelled "frontier step (not a claim)", and the
manifest cannot see it. Both problems are fixable before landing. The smallest corrections are
listed below.

## Standard being applied

- `CORPUS.md:179-184` (fleet): "A claimed repair ships one red-before state in which the same
  command exits non-clean for the named reason, with the fix as the only delta; the observed
  failure text is committed." Rejected exemplars: M027 (trees split identically), M029 (a
  probe that mutates nothing), M030 (a comparison that accepts an empty prior).
- `.ufo/waves/kaika-w1/mistakes.md:412-417` (L1): "Gate: mutation or negative-control arm,
  with the observed failure text committed."
- `templates/round-prompt.md:68-71`: the row is class · evidence pointer · captured-by · fix.

## Findings

### F1 — Ca's acceptance can be passed by a checker that cannot discriminate (calibration)

Evidence: `reports/round-50/claims.json:50` requires (i) "exits 1 naming the C->S dependency
(1/1 detected)", (ii) "run on reports/round-50/claims.json exits 0".
- (i) No exact finding set is pinned. A checker that prints every ordered pair and exits 1
  satisfies "exits 1 naming C->S".
- (ii) `reports/round-50/claims.json:12-58` has no `schema`, `base`, `tree` or `exports` fields.
  Under the shared contract that input should exit 2. A checker that exits 0 on it either has
  no export leg or accepts an empty prior (M030).
- Combined: a checker that always exits 1 on the r49 fixture and 0 on an input with no exports
  passes every acceptance clause.
- The dynamic leg is never shown to fail unless the fixture's C `acceptance` is the
  registry-resolution check. The r49 runner's leg tested inline URLs instead
  (`reports/round-49/run-validation.py:264-273`, `c_without_s.passed: true` in
  `reports/round-49/validation.json` `claims.separability`). That leg is the vacuous control
  being fixed.
- Nothing in `Ca.lands` (`claims.json:51`) holds the committed failure text.

Smallest correction:
1. Add `"expect_findings": [...]` (exact set) to `r49-fixture.json`. The selftest compares the
   set for equality, not containment.
2. Add a one-delta green twin, for example `r49-fixture-merged.json`, where S's lands are folded
   into C (one claim) and nothing else changes. The same command must exit 0. This is the red
   and green pair with the fix as the only delta.
3. Set the fixture C `acceptance` to "every `\bS\d{3}\b` in the entry resolves to a row in
   `corpus/SOURCES.md`". The dynamic leg then goes red in `c42d675` plus C.lands, because
   `c42d675:corpus/SOURCES.md` is absent (verified: `git cat-file -e` fails).
4. Run the negative control on a real r50 manifest with derived exports, for example
   `reports/round-50/separability/r50-manifest.json`. Do not run it on `claims.json`.
   `claims.json` input must exit 2.
5. Commit the observed red stdout and exit code, either as an added `Ca.lands` file or verbatim
   in the `round-50.md` Mistakes row.

### F2 — the r49 fixture is retrofitted, so its exports must be derived, not chosen (calibration)

Evidence:
- r49 `claims.json` and `claims-addendum-kaika.json` declare no `lands` for C, Ca or S
  (all `None`, measured).
- All three claims landed in one commit: `git show --stat c6a174d` shows 17 files, including
  entry, README, SOURCES, QUALITY, SKILL and `tools/check-readme-revisions.py`.
- The contract's example export `\bS0(3[1-9]|4[0-3])\b` covers exactly S031–S043, the ids C
  cites (`c6a174d` entry: S031–S043). S actually defined S001–S043 at `c6a174d`, plus S044–S047
  at `8cee755`.
- Narrowing the export to the cited subset fits the regex to the known answer.

Smallest correction: derive S's exports mechanically from S's landed bytes, using the row-id
regex `^\|\s*(S\d{3})\s*\|` over `c6a174d:corpus/SOURCES.md`. Record the derivation command and
its output in the fixture.

### F3 — "1/1 detected" will not be the honest count on the r49 fixture (calibration)

Under the contract's path-naming semantics, the r49 fixture also yields:
- **S→C**: `c6a174d:corpus/SOURCES.md` names `hunting-foraging-subsistence.md` 12 times
  (`used-by` cells; `grep -c` = 12).
- **Ca→C, and a lands overlap**: r49 C and Ca both landed `corpus/README.md` (`c6a174d` stat;
  `LOG.md:3966-3970`). Ca's tool names `corpus/README.md` at
  `tools/check-readme-revisions.py:2,50,306`.
- `claims.json:10` asserts "disjoint paths", but the contract's tool semantics never check
  disjointness.

Smallest correction:
- Add a lands-overlap check that exits 1 as `SEPARABILITY_OVERLAP X,Y path`.
- Classify every extra finding in `expect_findings` as either true coupling or false positive.
- Report precision alongside recall. Do not silently drop the extras.

### F4 — the r50 negative control false-positives at base bytes (operability, calibration)

Evidence: I simulated the contract's whole-file path leg over r50 `lands` at `4ad2683`:
- `PATH-LEG C->O`: `corpus/README.md` names `tools/check-readme-revisions.py`.
- `PATH-LEG O->C`: `tools/check-readme-revisions.py` (`:50` `DEFAULT_README`) names
  `corpus/README.md`.

With real lands, a contract-faithful checker exits 1 on r50. The likely failure is that an
implementer weakens the path leg to reach exit 0 without recording why.

Smallest correction: scan only X's added bytes (`git diff base..X.tree -- <land>` added lines
and new files). Then pin r50 `expect_findings: []`, triaging any real hit rather than adding an
unrecorded allowlist.

### F5 — strongest counterexample: r50 repeats the r49 coupling under a new label (coverage, calibration)

Evidence:
- `claims.json:10`: "C's entry cites SOURCES rows opened by the frontier step (not a claim)".
- `C.lands` (`claims.json:18`) excludes `corpus/SOURCES.md`.
- Yet `C.after_required` (`claims.json:17`) requires "every cited S-id resolves to a SOURCES
  row whose used-by names the entry". That cannot hold in `4ad2683` plus C.lands, because
  S048 and later are absent at base.
- So the declared contract sentence "each claim … verifies against base 4ad2683 plus only its
  own paths" is false for C. The checker cannot see this because the frontier unit is absent
  from the manifest.
- This is the exact r49 rejection shape (`corpus/lessons/round-49-verifier-spotcheck.md:17`:
  "C cites the registry S creates"). The mined mistake's own fix would miss its own round's
  recurrence, so the row's "captured-by" would be hollow.

Smallest correction:
1. Move `corpus/SOURCES.md` (the S048+ rows) into `C.lands`. C owns the rows it rests on;
   `templates/round-prompt.md:72-73` permits this ("the knowledge entry or evidence it lands
   cites that S###").
2. Put the S-resolution leg in C's `acceptance` in the r50 manifest, so the dynamic leg proves
   C verifies alone.
3. Keep Ca separable. QUALITY criterion 7 should cite only
   `corpus/lessons/round-49-verifier-spotcheck.md`, which exists at base. It should not cite
   S048+ or a `round-50.md` anchor (frontier bytes).
4. The alternative is a pseudo-unit F in the manifest with a declared C→F finding. That is
   inseparable by construction, and the judge would have to reject it as in r49.
   Prefer the move into `C.lands`.

### F6 — is another mistake more pressing? No; one routed residual must still be dispositioned

- **Separability ranks first.** It is the only outside disagreement left unlearned.
  `LEARNING.md:35` counts discernment harm as "a disagreement is left unlearned". It is not yet
  mined: `grep -ci separab corpus/lessons/round-49.md` returns 0.
- **Recommended row fields:**
  - class: `vacuous` (`mistakes.md:447`; C04).
  - captured-by: `reports/round-49/run-validation.py:264-273`. That leg existed and passed while
    testing inline URLs instead of registry rows. Do not record captured-by as `none`.
  - fix: Ca's checker with the F1 red and green pair.
- **r49 REVISION-ORPHAN residual (open, owed this round).** It was routed with
  `next_touch: r49 close / r50 Ca` (`corpus/lessons/round-49.md:160`, `:205-207`). It is still
  live at `4ad2683`: `python3 -B tools/check-readme-revisions.py` gives findings 0, warnings 1,
  `REVISION-ORPHAN lines=[90, 101]`, exit 0 (run today). r50 Ca does not take it, and
  `claims.json:60` `non_goals` does not disposition it. It does not need to be the mined
  mistake, but `round-50.md` must carry it with a new next_touch. Otherwise it becomes C11
  (ledger abandonment).
  - O's ExecReadmeRev edits the same tool and must keep the advisory ORPHAN leg.
- **r47 size criterion.** Still absent: `grep -nE '250|lines|size' corpus/QUALITY.md` returns 0
  hits. r50 C self-limits to ≤~250 in `claims.json:15` only. Adding it under Ca would widen
  `Ca.lands` scope, so leave it queued.
- **r44 carried-candidate.** No recurrence: pastoralism/husbandry appear in no prior scout
  file. `rg -i 'pastoral|husbandr|transhuman' reports/` excluding r50 hits only the D2 drill
  packets (r9/r11/r15) and an r8 receipt quote. The D2 "highland pastoralists" drill is a
  `- couples:` target for C, not a premise defect.
- **r36/r43 stale premise.** Captured by `claims-freshness`; r50
  `telemetry/declaration-freshness.json` clause 0 reads HOLDS.
- **r42 overwrite gate and r35 placeholder token.** Both are uncaptured and C touches the
  README this round, but there is no incident. They rank below an unlearned outside
  disagreement.

## Impacted axes

- calibration: F1–F4.
- coverage: F5, because C is not separately verifiable as declared.
- operability: F4, the O↔C false positive; F6, keeping the ORPHAN leg.

## Unrun checks

- The Ca checker, fixture and selftest have not landed. `patches/` is empty, and `work/` holds
  only ExecGuard, ExecProbe-4 and ExecReadmeRev, all clean at `4ad2683`. F1–F4 are predictions
  from the contract text plus base-byte simulation, not runs of the real tool.
- I did not run the dynamic leg on `c42d675` plus C.lands. That SOURCES.md is absent there is
  measured; the leg's outcome is `[INFERENCE]`.
