# ExecCaFix — round 75, wave 2 (claim Ca counter)

Seat: `ExecCaFix`, leaf executor. Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base
`f556d1049fe651d3d63975600b13acd9fb686f15`. I own the claim-Ca counter
`.ufo/waves/round-75/counters/accept-ca.py`; I did not edit `reports/round-75/claims.json`,
`reports/round-75/ledger.json`, the drafts, or any lane/fleet tracked byte.

## 1. Result

* Selftest: `SELFTEST: 154/154`, exit 0, no `SELFTEST FAIL` line (full log in
  `.ufo/waves/round-75/w2/parts/ExecCaFix-selftest.txt`).
* Leg table: exactly the twelve frozen names **in the frozen order**, enforced by LEGCOUNT
  (`frozen_names != list(REQUIRED_LEGS)` refuses with exit 2 and prints `FAIL legs=0/12`).
* Rehearsal: **`ACCEPT-CA-75: PASS legs=12/12`** (exit 0) on a tree built from the staged Ca
  landing plus one repair the stage does not yet carry (SHONEN.md:6) plus a stub claim-C landing
  for `--combined`; **10/12** on the staged landing exactly as staged; **7/12** for the do-nothing
  control; refusal for `--lands == base`. Table and per-leg reasons:
  `.ufo/waves/round-75/w2/parts/ExecCaFix-rehearsal.md`.
* R1EXEMPT fixtures: three committed-ready JSON specs under
  `.ufo/waves/round-75/counters/fixtures/`, applied deterministically by the counter (not
  synthesised by the selftest). On the real base registry they grade
  `{green: True, red: False, mixed: False}`.
* Claim-text conflicts: six, listed in §7. Two change what a leg can mean; the rest are landing
  defects the L1 must fix before the freeze/landing.

## 2. Files written (sha256)

| path | sha256 |
|---|---|
| `.ufo/waves/round-75/counters/accept-ca.py` | `3c89412923de5fe5026421a7bf0d025eeefd80da299153842dce4234274ad4fd` |
| `.ufo/waves/round-75/counters/fixtures/r1exempt-green.json` | `e2927b92688edbb6e289926332415b21b7679b25b15f66b3202b51214bafa84c` |
| `.ufo/waves/round-75/counters/fixtures/r1exempt-red.json` | `6ca910760947afdb0a45fdd065b9a7a9a56e7ea97072699fb6267d6084bdf1cb` |
| `.ufo/waves/round-75/counters/fixtures/r1exempt-mixed.json` | `55b471cb2521ce7b8c39cb5e18ed5640ea969ea4ec1fdff1e5e57b4a604b9a14` |
| `.ufo/waves/round-75/w2/stage/reports/round-75/accept-ca.py` (byte copy, for the freeze) | `3c89412923de…` (same) |
| `.ufo/waves/round-75/w2/stage/reports/round-75/fixtures/r1exempt-{green,red,mixed}.json` | same three digests |
| `.ufo/waves/round-75/w2/parts/ExecCaFix-selftest.txt` | `174594e1c1dcbe81322f069f999ef41a0ef2158960d777eb0994a1583dbb6973` |
| `.ufo/waves/round-75/w2/parts/ExecCaFix-rehearsal.md` | `abfcdb33b96e178816246f11b3e99953fb4815c57b595b93220b93b2e13cbe5e` |
| `.ufo/waves/round-75/w2/parts/run-staged-ca.txt` | `152ba2a4ba3acaaa05b7e77877a669447c652f12737eb05364e41fa7dadf548e` |
| `.ufo/waves/round-75/w2/parts/run-staged-full-ca.txt` | `add3f2c89f2b3568f431f012169161c3687bb9dcd572a9262b9a8f8f4283e10a` |
| `.ufo/waves/round-75/w2/parts/run-staged-full-combined.txt` | `8f66bb9c1af4beade849a65c96448162c31e9af42bfc8688f2fbeb7eeaf7221b` |
| `.ufo/waves/round-75/w2/parts/run-do-nothing.txt` | `82be3e7d5a1db9674a8e4d50a20ff0503f9c3e787cfeba44d4002269a8f72f4a` |
| `.ufo/waves/round-75/w2/parts/run-lands-eq-base.txt` | `7db685a077931cde7e5121bb21b965bc1bc7dc557ceebaa66935d091b1b2bac7` |
| `.ufo/waves/round-75/w2/parts/run-sweep-draft-verbatim.txt` | `7a829f6685252aff7e9886783f3325e930201697a5cefdc2f737aae5c401797c` |

The staged counter copy and the staged fixtures are byte-identical to the source files above; the
freeze must carry the counter at `reports/round-75/accept-ca.py` (the path the claim grades) with
`fixtures/` **beside it** (the counter looks beside itself first, then in
`.ufo/waves/round-75/counters/fixtures/`, so either placement works).

No tools were installed. No package manager was run.

## 3. Counter changes (diff summary)

The counter arrived as the round-74 instrument adapted by a wave-1 seat and never run to
completion. Six changes are bug fixes, five are predicate readings the frozen text forces, and the
rest is selftest/scratch work.

**Bug fixes (the leg was wrong, not the case):**

1. `statement_after()` compiled `statement_after.parse` **without `re.M`**. Every `^`-anchored
   repair parse in the ledger (`^## linguistics/ \((\d+)\)`, `^## culture-material/ \((\d+)\)`)
   was therefore a guaranteed `no-match` — L75-02 and L75-03 could never be green. Now
   `re.compile(parse, re.M)`.
2. `leg_ledger()` accepted a REPAIR pair with no `statement_after`, falling back to
   `stated_at`/`stated_parse`. The frozen REPAIR sentence names `statement_after` for every REPAIR
   pair; the fallback is withdrawn and the pair fails LEDGER (the selftest case
   `repair-no-statement` now expects `LEDGER=FAIL` and `REPAIR=FAIL`).
3. `leg_repair()`'s shadow check required the base `stated_text` to be absent from the **whole
   file**. `corpus/README.md:805` quotes the stale `## culture-material/ (36)` heading on purpose
   (an append-only dated record), so the whole-file reading can never hold together with
   APPENDONLY. The check is now: **no line that the `statement_after` parse matches may still
   carry the base `stated_text`** (shadow-append still caught: the selftest `shadow-repair` mutant
   stays red).
4. `_required_ok()` (new) replaces `required not in text` for fixed surfaces. The claim's
   `required` strings are requirement descriptions, not verbatim bytes ("criterion 23 addendum: a
   re-pointed read path lands with its fixture in the same commit; mutant redness is shown against
   a fixture that is green first" is nowhere verbatim in the landing). Each `;`-separated clause
   passes on its normalized text **or** on all of its 4+-character words; a missing addendum still
   fails. Also fixed the word tokenizer (a trailing `:` made `addendum:` unmatchable).
5. `leg_repair()`'s sweep receipt names (`sweep-red-before.txt` / `sweep-green-after.txt`) were
   inherited from round 74 and are not in the frozen text; the staged landing ships
   `sweep-base.txt`, `sweep-fixed-at-base.txt`, `sweep-fixed-after-ca.txt`. The re-run stays
   mandatory (base exit 1 naming 243/249, lands exit 0 with `"ok": true`); the legacy names are
   checked **when present**, and any committed `telemetry/sweep*.txt` pair carrying both an exit-1
   and an exit-0 verdict satisfies the frozen `after`.
6. `leg_repair()` now runs the check the frozen REPAIR sentence names and no leg implemented:
   `corpus/lessons/round-75.md`'s `## Corrections` section must carry a row for staged **S899**
   and **S900** (`_lesson_correction_problems`).

**Predicate readings the frozen text forces (each stated in the module docstring):**

7. **Shell metacharacters.** LEDGER says observe_cmd excludes them; L75-04's pattern contains
   backticks and L75-05/06/07's contain `\|`, so the strict reading makes four of ten pairs
   unobservable and the claim unsatisfiable. The counter now refuses a metacharacter in **every
   element except the grep / git-grep PATTERN operand** (an argv is never shell-parsed), and keeps
   the refusal for paths, revisions, separators and redirections. See §7.3 for the alternative.
8. **Re-derivation commands** are executed as argv (`shlex.split`), so `REDERIVE_META` admits a
   backtick inside a quoted pattern while `;`, `&`, `|`, `<`, `>`, `$(` stay refused.
9. **APPENDONLY fixed-surface exceptions** are now the frozen `fixed_surfaces` list itself: an
   integer `line` exempts that line only (SKILL.md:701 via the REPAIR stated_at rule), a frozen
   `sha256` pins bytes, and an entry with neither (the declared `reports/round-28/readme/sweep.py`
   repair) is the exception the frozen APPENDONLY text names, bound by REPAIR's own base/lands
   re-run. Previously an entry without `sha256` was a hard failure, so the declared sweep repair
   could never land.
10. `sources_diff()` fails closed when a row does not parse to the header's cell count at either
    revision (inserted delimiter, changed indentation).
11. **LEGCOUNT now enforces the frozen ORDER**, not just the set (`frozen_names !=
    list(REQUIRED_LEGS)`), with a new selftest scenario `legorder`.

**Scratch (prompt §7.4):**

12. `--work` (default `$HYAKU_SCRATCH/kotodama-r75`, else the system tempdir) is the one scratch
    root; `scratch_dir()` creates it, the run's `mkdtemp` and the selftest's fixture repo live
    under it, and the observation/sub-run environments carry it as `TMPDIR`. The two hardcoded
    `"TMPDIR": "/tmp"` in `_run_tool()`/`_run_r74_counter()` are gone. **One documented exception**
    remains, `R74_TMPDIR = "/tmp"` for the round-74 counter re-run only — see §7.5.
13. Dead code removed: `REQUIRED_RECEIPTS`, `hunks_with_removals`, `sources_nonrow_lines`.

**Selftest (cases fixed, where the case was wrong):**

14. `_build()` built the clean landing's correction rows from the *unmutated* pairs, so every
    ledger mutant that touched `rederive` failed NOSTUB for the wrong reason
    (`annotate-other-token`); it now builds them from the graded pairs.
15. `_claims_legs()` pinned the fixture's round-74 freeze to a hardcoded real-lane commit that is
    not in the fixture repo, so RECEIPTS failed in every scenario; it now pins the fixture's own
    base.
16. The R1EXEMPT receipts moved into the fixture **freeze** (the claim's do-nothing control reads
    them at `lands == freeze`), and the do-nothing expectation is `R1EXEMPT=PASS` per the claim.
17. New scenarios: `legorder`, `rederive-backtick` (a quoted backtick pattern is admitted and the
    run still passes), `r1-mixed-red` (a simultaneous teaches + used-by edit is red).
18. Final line `SELFTEST: <p>/<n>` added beside the inherited `SELFTEST OK: …` line.

## 4. Selftest output

```
SELFTEST OK: 154 checks across 39 scenarios reported-fail=0: do-nothing, clean, lands-eq-base,
legcount, legorder, stub-rows, no-rederive, annotate-other-token, rederive-backtick,
append-only-removal, protected-in-place, unnamed-in-place, r1-rule2-exempt, r1-teaches-red,
r1-mixed-red, shell-string, interpreter, constant-printer, out-of-clone, dead-pin, absence-pair,
min-pairs, config-edit-ledger, config-edit-claims, freeze-off-first-parent, repair-no-statement,
shadow-repair, separable-lane-row, separable-family, fabricated-base-observation, green-pair,
stated-line-mismatch, prose-row, expected-after-mismatch, worktree-only-ledger, stamp-measured,
receipts-r74-fail, combined-missing-entry, cli-errors
SELFTEST: 154/154
```

Exit 0. Every implemented leg has a named failing mutant (the `covered` table at the end of
`selftest()`); `R1EXEMPT` gained `r1-mixed-red`, `LEDGER` gained `legorder` coverage through the
refusal path.

## 5. Rehearsal (summary)

Scratch repository under `/fast/scratch/hyaku/kotodama-r75/ExecCaFix/rehearse/`, `git clone
--shared` of the lane (toplevel asserted), every commit made with the throwaway identity and
`git -C "$D"`. Freeze (rehearsal-only) `59ff98af64695f6d9ed24b609738e8e0232100ca` carries
`reports/round-75/{claims,ledger}.json` (the current draft bytes), the counter at
`reports/round-75/accept-ca.py`, `reports/round-75/fixtures/` and the two R1EXEMPT receipts.

| run | exit | legs | the reds |
|---|---|---|---|
| staged landing as staged (`121e7ea2…`) | 1 | 10/12 | REPAIR: L75-01/05/06/07 `statement_after no-match in SHONEN.md`; COMBINED: no `--combined` |
| staged + SHONEN.md:6 repair (`a08b9728…`), `--combined 9a878ff0…` | **0** | **12/12** | — |
| same lands, no `--combined` | 1 | 11/12 | COMBINED: `the explicit --combined revision is required` |
| do-nothing (`lands == freeze`) | 1 | 7/12 | REPAIR, ANNOTATE, NOSTUB, RECEIPTS, COMBINED |
| `--lands f556d104…` (base) | 2 | 0/12 | refused: `--lands equals the frozen base` |
| staged + the staged sweep draft verbatim (`e92fce5a…`) | 1 | 10/12 | REPAIR: `sweep green-after expected exit=0 ok=true; got 1` |

Which legs are green/red **because a landing file is not written yet** — named:

* REPAIR's four SHONEN pairs: no `SHONEN.md` edit exists anywhere in
  `.ufo/waves/round-75/w2/stage/`. Exact line that closes it (verified in the rehearsal; base line 6
  with the stale segment replaced, the round-53–56 figures moved to the lesson):

  ```
    asserted: `SKILL.md:20` (Decision table), `:505` (Error patterns), `:564` (Checklist); sources registered in `corpus/SOURCES.md` (Registry counts at round 75 Ca landing — rows: 808, mined: 713, queued: 58, rejected: 37 — census exit 0 in `reports/round-56/telemetry/final-measures.txt`; the round-53–56 historical figures are carried in `corpus/lessons/round-75.md`).
  ```

  The four base `stated_text` fragments (`(412 rows after round 56 — 367 mined, 35 queued, 10
  rejected`, `367 mined`, `35 queued`, `10 rejected`) must not survive on that line.
* REPAIR's sweep sub-check: `reports/round-28/readme/sweep.py` is not staged; the only repaired
  instrument in the tree (`drafts/sweep-fixed.py`) does not compile (§7.1). The rehearsal used a
  scratch-only corrected copy to show the achievable state.
* COMBINED: no claim-C landing exists yet; the rehearsal's combined tree is a stub (nine rows
  S885–S893, the three staged entries, the C-owned README heading). COMBINED's own predicate is
  what the rehearsal exercised, not claim C's counter.
* RECEIPTS: `reports/round-75/telemetry/accept-ca-74-at-lands.txt` is not staged; the rehearsal
  generated it from the real re-run (§7.5 fixes the environment it must be produced in).

## 6. R1EXEMPT fixtures

Three committed-ready specs (not selftest-synthesised): the counter materialises base, applies the
named cell edit to one pre-existing row, commits it in a throwaway clone, and grades
`sources_diff()`.

| fixture | cells edited | row | expected | measured on the real base registry |
|---|---|---|---|---|
| `r1exempt-green.json` | `used-by` | S004 | green | `APPENDONLY PASS` |
| `r1exempt-red.json` | `teaches` | S004 | red | `LEG FAIL APPENDONLY` — `row S004 changed outside the rule-2 cells (teaches)` |
| `r1exempt-mixed.json` | `teaches` + `used-by` | S004 | red | `LEG FAIL APPENDONLY` (the used-by change does not buy the teaches edit) |

The fixtures name a row id; when the graded registry does not carry it (the selftest's synthetic
registry) the counter uses that registry's first row id, so one code path serves both. Receipts
`reports/round-75/telemetry/r1exempt-{green,red}.txt` are committed **with the freeze** and are
what `lands == freeze` reads (the claim's do-nothing control). A prefix of the base tree is not
enough: the fixtures must be in the freeze commit.

## 7. Claim-text conflicts and landing defects

**7.1 `drafts/sweep-fixed.py` does not compile.** `IndentationError: unexpected indent`, line 170:
`ghosts.extend("unassigned/%s" % …)` sits at function indentation in the middle of the
`for part in sorted(sections):` body. The correct repair is to move those two lines above
`for part in sorted(sections):` (inside the loop they would append the same unassigned entries once
per part). With that move the instrument exits 0 with `"ok": true` at the Ca landing (rows ==
files == 249, no header drift, no missing rows/ghosts). The landing has **no** staged
`reports/round-28/readme/sweep.py`; the staged receipts `sweep-fixed-*.txt` claim a green run that
the staged draft cannot produce.

**7.2 No staged SHONEN.md:6 repair** — four of the six REPAIR pairs stay red without it (§5).

**7.3 LEDGER's "shell metacharacters" exclusion vs the ledger's own pairs.** L75-04's
`observe_cmd` pattern contains backticks; L75-05/06/07's contain `\|`. Strictly read, the frozen
LEDGER sentence makes four pairs structurally invalid, so `LEDGER`, `BASEMISMATCH`, `ANNOTATE` and
`NOSTUB` cannot pass. Two ways out, and the L1 must choose before the freeze:
(a) keep the frozen wording and accept the pattern-operand reading implemented here (a pattern is
data; the argv is never shell-parsed); (b) keep the strict wording and re-cut those four
`observe_cmd`/`rederive` strings to metacharacter-free patterns (e.g. `git grep -c -e mined` —
note this changes the measured quantity, so it changes the pair). The counter passes either way;
it fails only on a ledger that keeps `\|`/backtick patterns **and** a strict guard.

**7.4 REPAIR's "no base `stated_text` remains at the statement path" vs APPENDONLY.**
`corpus/README.md:805` quotes `## culture-material/ (36)` in prose and is an append-only dated
record. A whole-file absence check forces editing that line, which APPENDONLY forbids; the claim
would be unsatisfiable. Implemented reading (stated in the docstring): no line the
`statement_after` parse matches may still carry the old text.

**7.5 RECEIPTS' `ACCEPT-CA-74: PASS legs=11/11` holds only under `TMPDIR=/tmp`.** Measured on the
real lane: the round-74 counter at `5e4796c0…` with `--freeze 00c408a0…` prints `PASS legs=11/11`
with `TMPDIR=/tmp` and `FAIL legs=10/11` with any other tempdir — its own RECEIPTS leg compares
the committed round-73 receipts and its normalizer strips `/tmp` paths alone. The frozen RECEIPTS
sentence requires the exact PASS line, so `_run_r74_counter()` pins `R74_TMPDIR = "/tmp"`. That is
the only `/tmp` use in the counter (transient clones owned by the round-74 instrument, deleted by
it); every clone and fixture of this counter stays under `--work`. If the L1 wants no `/tmp` at
all, the frozen RECEIPTS sentence must change (e.g. require the r74 counter's *actual* verdict and
compare the committed receipt verbatim), not the counter.

**7.6 COMBINED's `measures-ca-combined.txt` receipt is named by the frozen text and read by no
leg.** I did not add a check: the frozen text says the receipt carries the **Ca-lands stamp** and
the exact combined revision/tree, but a receipt committed at lands cannot name a combined revision
that only exists after lands unless the commit order is fixed (and then it is not at lands). The
claim does not fix that order, so any implementation I could write would be either vacuous or
unsatisfiable. Recommendation: either drop the receipt clause or state that the receipt lands in a
later commit read by a different leg.

**7.7 Stale drafts.** `drafts/scorecard-corrections.md` describes an eleven-pair ledger and rows
L75-05/06/08/09/10; the current ledger has ten pairs and rows L75-04/08/09/10. The staged
`SCORECARD.md.append` already carries the correct four rows — do not land the draft.
`drafts/lesson.md` has the same stale ids; the staged `corpus/lessons/round-75.md` is correct and
its `## Corrections` section names staged S899 and S900 (REPAIR's new check passes on it).

**7.8 SKILL.md:701 is a line-number-pinned fixed surface.** The staged `NEW-701` payload matches
base line 701 exactly (verified) and lands at line 701 as long as no landing inserts a line above
it. No staged landing does. If claim C ever edits SKILL.md above 701, the check breaks.

## 8. Residual risks

* The pattern-operand reading (§7.3) is the one place where a grader could argue the counter is
  more permissive than the frozen sentence. It is stated in the docstring and pinned by the
  `shell-string` / `interpreter` / `constant-printer` / `out-of-clone` / `dead-pin` mutants, which
  still fail.
* The staged landing is a moving target (other seats were still writing during the rehearsal). The
  applied snapshot's digests are in `parts/ExecCaFix-rehearsal.md`; a later staging change is not
  covered by the rehearsal.
* The rehearsal's combined tree is a stub, not claim C's landing; COMBINED's predicate is
  exercised, claim C's counter is not.
* `--work` defaults to `$HYAKU_SCRATCH/kotodama-r75`; the graded invocation passes nothing, so a
  runner without `HYAKU_SCRATCH` falls back to the system tempdir (still not hardcoded).

## 9. Housekeeping

Scratch `/fast/scratch/hyaku/kotodama-r75/ExecCaFix/` (clone, freeze/lands commits, fixture
clones, run logs) was deleted after the logs were copied into
`.ufo/waves/round-75/w2/parts/`. No file under `/home/vgpnk/Projects/shokunin` outside the wave
directory was written; the fleet repo was read with `git -C` only. No tools installed.
