# ExecJunkAudit — junk-landing control set vs both claims' legs (round 75, wave 2)

Seat: `ExecJunkAudit` (executor, leaf). Lane `kotodama-shokunin`, base
`f556d1049fe651d3d63975600b13acd9fb686f15`. Audit of
`.ufo/waves/round-75/counters/junk-fixtures.py` (71 134 bytes, 1668 lines,
sha256 `3fa5c6932dfc780e51182e578c25ad7bef33abe819a6dd66697216140b0a4fd2`)
against the 13 claim-C legs and 12 claim-Ca legs in
`reports/round-75/claims.json` (DRAFT, not frozen, not edited by me).

Nothing in the lane's git/jj state was touched: read-only `git show` /
`git ls-tree` / `git diff` only, no `add`/`commit`/`checkout`/`stash`/`reset`,
no `jj`. No fetch, no network, no source opened, no tool installed. The two
files I wrote are this report and the fixture patch named in my seat item.

## 1. Files written

| path | sha256 | what it is |
|---|---|---|
| `.ufo/waves/round-75/w2/junk-additions.py` | `1bc55ff33f35271db537077e99af9c930b1ac4347d393531606ec150d369072e` | additive patch: 14 red fixtures + 2 documented survivors, in the generator's own style, plus registry tables and a self-test |
| `.ufo/waves/round-75/w2/ExecJunkAudit.md` | (this file) | the matrix, the ranking, the findings |

The generator itself, both counters, `claims.json`, `ledger.json`, the
assimilation scratch and every telemetry path are untouched.

## 2. What I actually ran (read-only)

```
$ python3 -B .ufo/waves/round-75/counters/junk-fixtures.py --selftest
SELFTEST: PASS                                   # exit 0
$ python3 -B .ufo/waves/round-75/counters/junk-fixtures.py --list
J1 … J10, G, R                                   # 16 rows, exit 0
```

Both as shipped: the helper self-test passes and the registry lists 14 `J*`
fixtures plus the `G`/`R` R1EXEMPT pair. A `--run` attempt at the current
tree, with scratch under `/fast/scratch/hyaku/kotodama-r75/ExecJunkAudit`:

```
$ … --run --freeze f556d104… --lands f556d104… --only J5 --no-baseline
fixture: J5
error: FixtureError: SCORECARD carries no `## Corrections — round 75` section
accepted: no (no verdict was produced)
# ACCEPTED JUNK LANDINGS: none                    # exit 0  <-- see F1

$ … --only J6,J10,G,R --no-baseline
fixture: J6 / J10 / G / R
error: FixtureError: no counter found in the tree at reports/round-75/accept-ca.py
       or .ufo/waves/round-75/counters/accept-ca.py
# ACCEPTED JUNK LANDINGS: none                    # exit 0, 4 fixtures ungraded
```

**No verdict is obtainable before the freeze**, for two independent reasons I
verified in the tree:

1. `.ufo/waves/round-75/counters/accept-c.py` is **PART A only** — 511 lines,
   ending at `# --- PART B ---`; it defines helpers and `leg()` but has no
   `def main`, no `leg_*` function and no `__main__` guard, so running it
   prints nothing and exits 0. The claim-C legs do not exist in code yet
   (w2 seats `ExecLeg*`/`ExecCtrCfgMain` own them, `w2/parts/` was still empty
   when I read it). Every C-side claim in this report is therefore derived from
   the **frozen leg wording**, and each C fixture is written to that wording,
   not to an implementation.
2. Both counters, `claims.json` and `ledger.json` are uncommitted
   (`git status --porcelain`: `M SHONEN.md`, `M SKILL.md`,
   `M reports/round-28/readme/sweep.py`, `?? .ufo/waves/round-75/`,
   `?? reports/round-75/`), so a fixture cloned at `--freeze <base>` cannot
   resolve a counter file at all.

`accept-ca.py` was complete and runnable-in-shape when I read it (all 12
frozen names in `REQUIRED_LEGS`, a `leg(...)` return per leg; the file is
under active edit by a sibling seat this wave, so I cite leg behaviour, not a
line count). I read the three uncovered legs (`leg_basemismatch`,
`leg_repair`, `leg_combined`) plus `leg_ledger`, `leg_r1exempt` and
`observe_problem` to write fixtures that match what those legs actually read.

## 3. The matrix

Rows = the frozen legs (names from `claims.json`, in claim order). Columns =
the fixtures that target that leg. "shipped" is the generator as it stands;
"with patch" adds `.ufo/waves/round-75/w2/junk-additions.py`.

### claim C — 13 legs

| # | leg | shipped | with patch |
|---|---|---|---|
| 1 | ENTRIES | J1 (header-only stub only) | J1, **JC11** (survivor: filler body) |
| 2 | ROWS | — | **JC1** (opened 2026-10-28), **JC7** (escaped pipe) |
| 3 | REPOINTED | — | **JC2** (source ids swapped), JC6b |
| 4 | GATE | — | **JC3** (access date off 2026-10-27) |
| 5 | EVIDENCE | J2 (quote absent) | J2 |
| 6 | REJECTS | — | **JC4** (`## Quarantine` renamed) |
| 7 | GROUND | — | **JC5** (gap-sweep 808 → 809) |
| 8 | CITEDLINES | — | **JC6** (survivor: stub tool), **JC6b** (dangling S999) |
| 9 | CENSUS | — | **JC7** (row NF 13 → 14) |
| 10 | SCRATCHMIRROR | — | **JC8** (receipt declares non-zero exit) |
| 11 | COLLCHECK | — | **JC9** (map points one staged id at the wrong document) |
| 12 | FROZENCFG | J3 | J3 |
| 13 | INDEX | — | **JC10** (heading count +1) |

Coverage: **3/13 shipped → 13/13 with the patch** (two of the thirteen,
ENTRIES and CITEDLINES, are covered by *survivors* that record a hole the
wording cannot close — see §5; they are not catches).

### claim Ca — 12 legs

| # | leg | shipped | with patch |
|---|---|---|---|
| 1 | LEDGER | J4, J4b, J4c, J4m, J4f | same |
| 2 | BASEMISMATCH | — | **JCA1** (11th pair, stated == observed at base) |
| 3 | REPAIR | — | **JCA2** (base stated_text back at the statement path) |
| 4 | ANNOTATE | J5 | same |
| 5 | APPENDONLY | J6, J7, J10 (+ G/R two-way proof) | same |
| 6 | R1EXEMPT | G/R pair (fixtures executed by the leg itself) | + **JCA4** (green receipt carries the red shape) |
| 7 | NOSTUB | J5 | same |
| 8 | SEPARABLE | J8 | same |
| 9 | RECEIPTS | J9 | same |
| 10 | COMBINED | — | **JCA3** (in-place edit; needs `--combined`, see F3) |
| 11 | FROZENCFG | J4, J4b, J4c, J4m | same |
| 12 | STAMP | J9 | same |

Coverage: **9/12 shipped → 12/12 with the patch**. (Counting R1EXEMPT as
covered-by-G/R shipped, it was 10/12; G/R *prove* the exemption but never
attack the receipts that are supposed to carry the proof — JCA4 does.)

### Fixture → leg, declared vs necessarily-also-reddened

Declared is what the registry tuple promises (the generator's
`expected-legs` and the `newly-red` column). "Also reddens" is my reading of
the wording: a mutation that satisfies one leg's kill clause almost always
satisfies a neighbour's, and a receipt that hides that is too generous.

| fixture | declared | also reddens (wording-derived) |
|---|---|---|
| J1 | ENTRIES | INDEX (stub `- topic:` text is not the README row's verbatim topic) |
| J2 | EVIDENCE | — (window length and digests are preserved on purpose) |
| J3 | FROZENCFG | — |
| J4/J4b/J4c/J4m | LEDGER, FROZENCFG | — (the counter never reads the graded ledger as config; measured in r74 as FROZENCFG-only) |
| J4f | LEDGER | — |
| J5 | ANNOTATE, NOSTUB | — |
| J6 / J7 / J10 | APPENDONLY | — |
| J8 | SEPARABLE | — |
| J9 | RECEIPTS, STAMP | — |
| G / R | APPENDONLY (G green, R red) | — by construction |
| JC1 | ROWS | — |
| JC2 | REPOINTED | GATE? no — the Gate rows are untouched; only the entries' source lines move |
| JC3 | GATE | — |
| JC4 | REJECTS | — |
| JC5 | GROUND | — |
| JC6b | CITEDLINES, REPOINTED | — (no C-owned inline-id defect can move CITEDLINES alone; see F5) |
| JC7 | CENSUS, ROWS | REPOINTED? no |
| JC8 | SCRATCHMIRROR | — |
| JC9 | COLLCHECK | REPOINTED if the entry's `source:` line is re-pointed to follow the bogus map entry — the fixture does not touch entries, so COLLCHECK alone |
| JC10 | INDEX | — |
| JCA1 | BASEMISMATCH | — (LEDGER stays green: the added pair is allowlisted and structurally valid; verified, §6) |
| JCA2 | REPAIR | — |
| JCA3 | COMBINED | — (only with `--combined`; APPENDONLY at Ca-lands is not asked to see it) |
| JCA4 | R1EXEMPT | — |
| JC6 / JC11 | (survivors: no leg may redden) | — |

## 4. Ranked exposure — the cheapest junk landing each wording passes

This is the do-nothing-control design the L1 needs before freeze. Rank = risk
that a landing which does not do the work still grades the leg green. Where a
shipped/patch fixture already attacks the leg, the attack is named; where the
attack is a *survivor*, the hole is declared and stays open.

| rank | leg | attack now | cheapest landing the wording passes |
|---|---|---|---|
| 1 | C **CITEDLINES** | JC6 (survivor) | Replace `tools/check-cited-lines.py` **in the lands tree** with a 4-line stub that prints `CITED-LINES: 0 finding(s)`. The wording runs the materialized tree's tool, so the landing controls its own instrument. Only freezing the tool blob closes it. |
| 2 | C **SCRATCHMIRROR** | JC8 | Commit a hand-written `validate-receipt.txt` that says `validate --file … exit 0` and names every frozen row id and entry basename, **before** the registry-append commit. No mirror, no run, no `--file` invocation. |
| 3 | C **COLLCHECK** | JC9 | Write `guard-proof` prose that says a 1–3-space indentation collision was found and a 4-space one was not, plus the four id files; no guard ever runs. |
| 4 | C **GATE** + **EVIDENCE** | JC3 (date), J2 (absence) | A 5-token invented quote with a plausible locator, plus a ≥4096-character fabricated window that contains it and a recomputed `window-sha256`. No leg re-opens the page, and the landing writes both files, so both legs pass with the source never containing the sentence. |
| 5 | C **ROWS** | JC1, JC7 | Append the nine mapped rows with correct geometry (opened 2026-10-27, cadence recheck, 11 cells, no pipe, used-by = the citing entries) but an anchor-cell quote that occurs nowhere on the page. Page truth is only reachable by the ordinary re-open. |
| 6 | C **ENTRIES** | J1 + JC11 (survivor) | 478+ words of repeated boilerplate under one `## Body`, with the nine non-placeholder header fields. The leg declares itself "a length-and-shape gate only". J1 catches only the *header-only* stub, so a receipt that cites J1 does not show filler is refused. |
| 7 | C **INDEX** | JC10 | Verbatim topics for the three adopted entries **plus** one extra row for a `narrative-*.md` file that does not exist, or a wrong-topic row for another file. The wording binds only the adopted entries' rows and the heading count. |
| 8 | C **REJECTS** | JC4 | Name every refused staged file, then satisfy "reason and flip" with one generic sentence each, or with `—` cells: the leg as written checks names, counts and the presence of the words. |
| 9 | Ca **SEPARABLE** | J8 | A Ca correction row that cites a **staged** id outside `S885..S893` (e.g. `S876`, mapped by the frozen map). The wording bars "a lane id claim C adds (S885..S893)", not staged ids — the overlap the r75 map calls out. |
| 10 | C **CENSUS** | JC7 | Semantically false but syntactically valid cells (a wrong `tier`, a `teaches` cell copied from another row): the census exits 0. ROWS catches tier drift only because it compares pre-existing rows byte-for-byte and the frozen new rows. |
| 11 | C **REPOINTED** | JC2, JC6b | Correct id + the row's URL on the `source:` line, with prose attributing something the document does not say. The leg couples id↔URL, not assertion↔document. |
| 12 | C **GROUND** | JC5 | A fabricated receipt that agrees with the true base facts (808 rows, 0 matches). Low harm: the counter independently re-derives 0 at base, so only the receipt's honesty suffers. |
| 13 | Ca **LEDGER** | J4f | An allowlisted command whose output is true but unrelated to the statement (e.g. `git diff --shortstat` on a directory that happens to have N files, paired with a line that mentions N for another reason). The allowlist closes `echo`/interpreters, not relevance. |
| 14 | Ca **BASEMISMATCH** | JCA1 | Ten pairs that are red for trivia — stale numbers about surfaces the claim never promises to calibrate — with `observed_at_base` filled in to match. The leg measures the arithmetic, not the choice of surface. |
| 15 | Ca **REPAIR** | JCA2 | `statement_after.parse` is landing-authored: a parse that captures a number which coincidentally equals the re-run observation (a count elsewhere in the same file) passes while the intended statement is wrong. Requires the landing to also delete the base `stated_text`, which the leg checks. |
| 16 | Ca **ANNOTATE** | J5 | A row with id + base token + observed token + a rederivation command that returns the observed token, but a `note` that misdescribes the surface. The leg re-runs the command, so the numbers are honest. |
| 17 | Ca **RECEIPTS**, **STAMP**, **APPENDONLY**, **R1EXEMPT**, **FROZENCFG** | J9, J6/J7/J10, G/R, JCA4, J3/J4* | Measured by execution or byte identity; no cheap survivor found. STAMP's grammar can be hand-typed to agree, but RECEIPTS re-runs the round-74 counter and requires its verbatim stdout at the pinned revision. |
| 18 | Ca **COMBINED** | JCA3 | Fail-closed, not a survivor: without `--combined` the leg is red by construction ("the explicit --combined revision is required"). The risk is the mirror image — a red leg that looks like a catch for a missing flag. See F3. |

Two consequences for the freeze:

- The four C legs whose only protection would be a *receipt* (CITEDLINES,
  SCRATCHMIRROR, COLLCHECK, GROUND) plus GATE/EVIDENCE are exactly the legs
  the claim's `kill_rule` already tries to reach through the ordinary re-open.
  The junk set cannot close them; the freeze should not present
  `junk-c.txt` as if it did. If the L1 wants CITEDLINES, SCRATCHMIRROR and
  COLLCHECK closable, the cheap fix is to pin the instrument blob (freeze-time
  option, not a predicate change): require the tool/guard/receipt named by the
  leg to be byte-identical to `git show <freeze>:<path>`.
- JC6 and JC11 are **survivors**: a correct counter must leave ENTRIES (JC11)
  and CITEDLINES (JC6) green. A receipt that books them as catches is wrong,
  and `--list` must print them from their own table so nobody reads silence as
  coverage.

## 5. The patch

`.ufo/waves/round-75/w2/junk-additions.py` (892 lines) appends to the generator
without editing it. It carries:

- **14 fixtures in `ADDITIONS`** — `JC1 JC2 JC3 JC4 JC5 JC6b JC7 JC8 JC9 JC10
  JCA1 JCA2 JCA3 JCA4` — each one surgical, each raising `FixtureError` with
  the missing artifact named when the reference tree does not carry the landing
  yet (the generator's existing F6 convention: no artifact, no verdict).
- **2 survivors in `SURVIVOR_FIXTURES`** — `JC6` (stub citation checker),
  `JC11` (filler entry body) — with `ORDER_ADDITIONS`/`SURVIVOR_ORDER`,
  `EXTRA_ARGS` for the `--combined` fixture, and `selftest_additions()`, a
  stdlib self-test that builds one synthetic tree per mutator in a `mkdtemp`
  under `$SHOKUNIN_SCRATCH` and asserts each intended defect without a counter.

Apply order (in the patch docstring, corrected after I hit the trap myself):
append the code before the `# ---- CLI ---` marker, then place
`FIXTURES.update(ADDITIONS)`, `ORDER = ORDER + ORDER_ADDITIONS`,
`SURVIVORS = SURVIVOR_FIXTURES` immediately **before** that marker — at end of
file the table update runs after `main()` under the `__main__` guard and
`--list` silently omits the additions — and add `selftest_additions()` to
`_selftest()`.

### Evidence that the patch is sound (measured, scratch-only)

Assembled exactly as above and run:

```
$ python3 -B -W error::DeprecationWarning generator_patched.py --selftest
ADDITIONS SELFTEST: PASS (16 checks, 14 added fixtures)
SELFTEST: PASS                                   # exit 0, no deprecation
$ python3 -B generator_patched.py --list | wc -l
30                                               # 16 shipped + 14 additions
```

Each of the 16 mutators was applied to a fresh copy of one synthetic landing
tree and the intended defect asserted (opened cell 2026-10-28; swapped source
ids; Gate date 2026-10-26; `## Quarantine` gone; gap-sweep 809; stub tool <300
bytes and logic-free; `S999` in the entry body; row NF 13→14 with a literal
`\|`; receipt `exit 1`; map `S876 → S886`; heading `(33)`; ledger pair
`L75-J1` with `expected_after == observed_at_base`; base `stated_text` back in
`SHONEN.md`; in-place line edit; green receipt carrying `LEG FAIL APPENDONLY`
and `exit: 1`; filler body ≥478 words with the header intact).

The two mutators whose target the C counter reads from **frozen config** were
checked against the real code paths:

- **JCA1 (BASEMISMATCH).** `leg_basemismatch` reads its pairs from
  `git show <freeze>:reports/round-75/ledger.json`, so — like `J4f` — the
  fixture sets `ctx["own_freeze"]` and its own commit becomes the freeze.
  I validated the added pair with `accept-ca.py`'s own helpers against a real
  clone at base:

  ```
  observe_problem(pair["observe_cmd"], base_clone) -> None      # allowlisted argv
  run_observe -> " 29 files changed, 5248 insertions(+)"        # exit 0
  parse_observed -> ('29', True, '')  stated_token -> ('29', True)
  norm(observed) == norm(stated) -> True
  base corpus/README.md:447 == "## synthesis/ (29)"
  ```

  So LEDGER stays green (structural clauses all hold, `observed_at_base` "29"
  matches) and BASEMISMATCH must redden on its one non-red pair. Had I edited
  only the graded tree's ledger, the fixture would have reddened FROZENCFG and
  left BASEMISMATCH green — the w1 F1 trap.
- **JC7 (CENSUS).** The escaped pipe takes the row from `awk -F'|'` NF 13 (the
  frozen geometry) to NF 14 on the same line, with the teaches text otherwise
  unchanged.
- **JCA4 (R1EXEMPT).** `leg_r1exempt` requires the green receipt to carry
  `LEG PASS APPENDONLY` and an exit-0 line and the red receipt the `FAIL`
  shape; the fixture flips exactly those three tokens in the green receipt.

## 6. Findings for the L1 (all measured unless marked [INFERENCE])

- **F1 (HIGH — the sweep can report success with zero verdicts).**
  `run()` returns `accepted`, and `main()` maps `not accepted` to exit 0. A
  fixture that errors prints `accepted: no (no verdict was produced)` and is
  counted nowhere, so a run in which *every* fixture failed prints
  `# ACCEPTED JUNK LANDINGS: none` and exits 0 — measured above on J5 alone
  and on J6/J10/G/R. At freeze, `junk-c.txt`/`junk-ca.txt` must not be accepted
  on that line. Ask the generator's owner for two lines: `# GRADED: <k>/<n>`
  and exit 2 when `k < n`. [The claim's control sentence only names the
  receipts; nothing in it forbids a vacuous receipt.]
- **F2 (MED — the patch's own trap, now documented).** Registry updates placed
  at end of file run after `main()` under the `__main__` guard; `--list` then
  omits the additions. Verified: with the lines at EOF, `--list` printed 16
  rows; with them before the CLI marker, 30.
- **F3 (HIGH for the Ca control — COMBINED fails closed without `--combined`).**
  `leg_combined` returns FAIL when no combined revision is supplied, and the
  generator's `run_counter` never passes one. JCA3 therefore **needs** the
  `EXTRA_ARGS` plumbing; without it the fixture "catches" COMBINED for the
  wrong reason (missing flag, not the in-place edit). With the flag, JCA3's
  in-place edit of `corpus/knowledge/myth-symbol/comparative-frameworks.md` is
  outside the frozen C exemptions and outside the rule-2 cells.
- **F4 (MED).** Any Ca fixture whose leg reads the freeze must set
  `ctx["own_freeze"]` (J4f already does). JCA1 does. A graded-tree mutation of
  `ledger.json` can only ever redden FROZENCFG.
- **F5 (MED — CITEDLINES cannot be isolated).** Any inline-id defect in the
  entries reddens REPOINTED too, by REPOINTED's own wording ("every inline
  S-id in the entries resolves to a frozen row"), so JC6b declares both.
  CITEDLINES alone is only moved by substituting the tool (JC6), and that
  substitution cannot be caught. Freezing `tools/check-cited-lines.py`'s blob
  is the only cheap close.
- **F6 (LOW).** ENTRIES cannot reject filler by construction. J1 catches the
  header-only stub; JC11 records that a 480-word boilerplate body passes. Do
  not cite J1 as an anti-filler control.
- **F7 (LOW).** The Ca frozen sentence's fixture list is
  `J4f, J5, J6, J7, J8, J9, J10 + R1EXEMPT counterpart controls`; it does not
  name any fixture for BASEMISMATCH, REPAIR or COMBINED (the three legs that
  had none). Claim C's control defers to "fixtures named at freeze". Naming
  `JCA1, JCA2, JCA3, JCA4` and the six C-leg fixtures at freeze is not a
  predicate change; leaving them unnamed is a coverage claim the receipts
  cannot support.
- **F8 (INFO).** Audit-time build state: `accept-c.py` is PART A only (511
  lines, stops at `# --- PART B ---`), `accept-ca.py` complete. Every C-side
  expected-leg in this report and in the patch is therefore derived from the
  frozen wording, not from an executed leg. The moment PART B is assembled,
  `--lands <landing>` is the real test.

## 7. Risks and blockers

- The C legs are unimplemented at audit time (F8): the C fixtures are
  wording-faithful but unexecuted. If a leg's implementation reads a different
  surface than its wording (e.g. `INDEX` deriving topics from the frozen claim
  instead of the entry header), the fixture may redden a neighbouring leg
  first; the `newly-red` column will show it and the seat that owns the leg
  should read the fixture's declared legs.
- `JCA2`'s mutation is landing-shape dependent: it re-appends the pair's
  `stated_text` to `statement_after.path`, so it works for any landed SHONEN
  summary, but it must run with `--lands <Ca-lands>`; at freeze it raises
  `FixtureError` (no canonical landing statement to contradict yet).
- `JC8` assumes the receipt names its exit status (`exit 0`/`exit: 0`/
  `exit=0`); the fallback appends `exit 1`. If the landed receipt uses another
  spelling the fixture still mutates the file, but the declared leg should be
  re-read against the landed receipt.
- `accept-ca.py` is being edited by a sibling seat while this wave runs (its
  length changed under me between reads). The leg behaviour I targeted
  (`leg_basemismatch` requires every frozen pair red at base and no green;
  `leg_repair` requires the re-run token, difference from base, base text
  gone and `expected_after == token`; `leg_combined` requires `--combined`
  and checks APPENDONLY at that tree; `leg_r1exempt` executes the G/R
  fixtures itself and requires the receipts' `LEG PASS/FAIL APPENDONLY` and
  exit lines) is the frozen wording's behaviour; if the implementation moves
  away from the wording, the fixture should be re-read against the moved
  code, not against this report.
- Scratch note: my first scratch dir under
  `/fast/scratch/hyaku/kotodama-r75/ExecJunkAudit` was deleted at 16:53 by
  peer `ExecTmpSweep`'s mistaken `rm -rf` of the round root (they reported it).
  I recreated it and re-ran every check above from the lane files; nothing in
  this report depends on the deleted directory, which is removed now.
- No blockers on the deliverables; no tool installed, so nothing to record
  under the install ledger.

## 8. Scratch

All clones, synthetic trees and the assembled generator lived under
`/fast/scratch/hyaku/kotodama-r75/ExecJunkAudit/` (mirror clone, base clone,
`generator_patched.py`, `smoke/`), deleted before this report was yielded. The
patch re-derives the mutators' own test from its bundled
`selftest_additions()`, so no scratch path is citable evidence.
