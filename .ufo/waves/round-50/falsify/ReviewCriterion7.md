# Round 50 — falsify seat: QUALITY.md criterion 7 (Ca calibration)

**Item attacked:** `corpus/QUALITY.md` line 31 — criterion 7 "**Claims stay separable**" as landed at
`1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`),
together with the tool it names (`tools/check-claim-separability.py`).

**Verdict: PARTIAL.**

- Grounding: **HOLDS.** The cited lesson file exists, the `#adjudication` anchor exists, and the quoted
  content matches the criterion's parenthetical and its middle clause.
- Style vs criteria 1–6: **PARTIAL.** The closing "Grounded in …" sentence matches criterion 6 exactly;
  the line is 1.5× the previous longest criterion, packs a property + three rules + a procedure into one
  line, and is round-scoped inside a document whose frame is entry admission.
- Enforceability: **BROKEN in two named clauses, and the mandated command is not executable as written.**
  The criterion promises that a counterfactual leg which keeps the dependency or rewrites the other
  claim's bytes "does not count as verification"; the tool as written cannot see either, and I reproduced
  both as `SEPARABILITY: 0 findings` / exit 0.

Read-only seat. No lane file was edited; all reproduction ran in a private clone under `/tmp`
(`/tmp/kg7-4180537`, `git clone -q --shared … && git checkout -q 1c779e4`), deleted afterwards.
No packages were installed (python3 stdlib only); no tool installs were needed.

---

## 1. What the criterion says (verbatim, `corpus/QUALITY.md:31`)

> 7. **Claims stay separable** — each round claim verifies on the base commit plus only the paths it
> lands itself. Its added lines may not cite an identifier another claim newly exports, nor name a path
> another claim newly lands; a counterfactual leg that quietly keeps the dependency (inline URLs standing
> in for the registry rows) or rewrites the other claim's bytes before checking does not count as
> verification. Sources a claim cites are that claim's lands. Run
> `tools/check-claim-separability.py` on the round manifest before dispatch. Grounded in the round-49
> REJECTED-HONEST-STOP at `corpus/lessons/round-49-verifier-spotcheck.md#adjudication` (C cited the
> registry S created).

Clause inventory used below: **(a)** base + own lands only; **(b)** no citing another claim's newly
exported identifier; **(c)** no naming another claim's newly landed path; **(d)** a counterfactual leg
that keeps the dependency does not count; **(e)** a leg that rewrites the other claim's bytes does not
count; **(f)** "Sources a claim cites are that claim's lands"; **(g)** "Run … on the round manifest
before dispatch"; **(h)** grounding.

---

## 2. Grounding — HOLDS

| check | command | result |
|---|---|---|
| file exists at landed commit | `git show 1c779e4:corpus/lessons/round-49-verifier-spotcheck.md` | present (17 lines, added by base commit `4ad2683`) |
| anchor exists | `… \| grep -n "^#"` | `15:## Adjudication` → GitHub slug `#adjudication` ✓ |
| parenthetical supported | `…:17` | "REJECTED-HONEST-STOP on claim separability, not on the landed work. Coverage C and sources capability S both have supported outcomes, **but C cites the registry S creates**; the c_without_s runner leg retained inline URLs rather than the required registry rows and therefore did not verify the required counterfactual." |
| clause (d)/(e) supported by the same section | same line | the lesson names **both** failure modes (inline URLs retained; counterfactual not verified) — the criterion's middle clause is grounded, not invented |

Comparison anchor for style (criterion 6) also resolves: `corpus/lessons/round-49.md:302
## Post-review corrections (2026-10-19)` → `#post-review-corrections` ✓.

**Residual (S5, minor):** the grounding file is **not indexed** in the corpus's own lessons index at the
landed commit — `git show 1c779e4:corpus/lessons/README.md | grep -n spotcheck` → 0 hits, and
`git diff 4ad2683 1c779e4 -- corpus/lessons/README.md` is empty. The build wave prepared exactly this row
(`.ufo/waves/round-50/build/ReviewLessonsIndex-revision5.diff:20`) and it did not land. The lane's own
defect id names this file: `.ufo/waves/round-50/build/ReviewLessonsIndex.md:21` — "**C31-1**
unindexed-file `round-49-verifier-spotcheck.md`. Committed at `4ad2683`. The README table has no row for
it". Criterion 7 therefore points the admission bar at a lesson the corpus index does not list.

---

## 3. Style vs criteria 1–6

Measured on the landed file (`awk '{printf "%d\tchars=%d\twords=%d\n", NR, length($0), NF}'`):

| line | criterion | chars | words |
|---|---|---|---|
| 5,9,13,16,18 | 1–5 | 73, 70, 70, 75, 73 | 11–12 |
| 29 | 6 | 445 | 62 |
| **31** | **7** | **683** | **98** |

What matches criterion 6: bold label + em dash opening; a normative sentence; the closing
"Grounded in … \`path#anchor\` (paraphrase)." sentence with the same shape as criterion 6's; the
`corpus/lessons/…` pointer style.

What deviates:

1. **Subject mismatch.** `corpus/QUALITY.md:3` frames the whole file: "An entry is admitted into
   `corpus/knowledge/` only when it clears all of:". Criteria 1–6 are entry-level (provenance,
   calibration, coupling, usability, canon hygiene, source authority). Criterion 7 is **round-level**
   ("each round claim"), so no individual entry can clear it, and entry admission now depends on round
   bookkeeping that no entry controls.
2. **Density.** Criterion 7 packs a property (a), two prohibitions (b, c), two exclusion rules (d, e), a
   registry rule (f), a procedure (g) and the grounding (h) into one 98-word line — 1.5× criterion 6,
   ~9× criteria 1–5. Criterion 6 packs a property + one correction rule + grounding.
3. **Procedure inside the admission bar.** "Run `tools/check-claim-separability.py` on the round manifest
   before dispatch" is an executor instruction, not an admission property; criteria 1–6 contain no
   procedure of this kind (criterion 6 contains one *corrective* rule, not a run order).
4. **List continuity (pre-existing, inherited).** Items 1–5, then the tier paragraph (lines 25–27), then
   6, then 7 — the numbered list is split by prose. Criterion 6 already did this; criterion 7 inherits it.

---

## 4. Enforceability map — clause → tool as written

Tool cited by the criterion: `tools/check-claim-separability.py` at `1c779e4`.

| clause | tool behaviour (file:line) | verdict |
|---|---|---|
| (a) base + own lands only | `_counterfactual` (553–567) / `_git_counterfactual` (582–597) materialize base + X.lands, every other path at base bytes; `_acceptance_findings` (647–670) runs the argv there | enforced **for units that declare an `acceptance`**; `acceptance` is optional in the schema (87, 408–410), so a claim with none is never dynamically verified |
| (b) no citing another claim's newly exported identifier | `_static_findings` (616–635) matches Y's **self-declared** export regexes against X's added lines; novelty enforced at 491 | enforced as written, but only over identifiers the *other* claim chose to declare — in `reports/round-50/separability/r50-manifest.json` both `O` and `Ca` declare `"exports": []`, so for this round the export leg is vacuous |
| (c) no naming another claim's newly landed path | `name_paths` (366–368) counts only land paths **absent at base**; `_name_re` (602) matches whole paths | enforced as written; narrower than a reader may expect (a path that exists at base, or a relative mention such as `lessons/round-50.md` for `corpus/lessons/round-50.md`, is not a finding) |
| (d) leg that keeps the dependency (inline URLs) | only detected when the inline URL text carries the exported identifier (selftest control 935–941) | **NOT enforced** — see §5.2 |
| (e) leg that rewrites the other claim's bytes | no post-run integrity check anywhere: `_counterfactual` returns straight from `_run_acceptance` (562) and `_git_counterfactual` likewise (592); `rc == 0` is read as "verified" at 650–651 | **NOT enforced** — see §5.1 |
| (f) "Sources a claim cites are that claim's lands" | no check of this kind exists; lands are path-granular and the same path in two units is an `SEPARABILITY_OVERLAP` finding (637–645) | not machine-checked, and unsatisfiable for two source-citing claims in one round — see §5.4 |
| (g) "Run … on the round manifest before dispatch" | the tool's input schema is `kotodama-separability-manifest-v1` (4–16, 73); "the round manifest" is a term used **nowhere else in the repo** (`git grep -n "round manifest"` → only `corpus/QUALITY.md:31`) | **not executable as written** — see §5.3 |
| (h) grounding | — | HOLDS (§2) |

---

## 5. Findings by severity

### 5.1 S1 — major — clause (e) is not enforceable: a leg that rewrites the other claim's bytes reads as verified

The criterion states a leg that "rewrites the other claim's bytes before checking does not count as
verification". The tool has no post-run tree-integrity check: `_counterfactual`
(`tools/check-claim-separability.py:553–567`) copies base, places X's overlays, runs the argv and returns
the result; `_git_counterfactual` (582–597) is the same in a clone. `_acceptance_findings` (650–651)
turns `rc == 0` into "no finding".

Reproduction (synthetic lane, base + claim trees C and S; C's acceptance writes S's registry row into
`corpus/SOURCES.md` **before** checking — the exact round-49 shape):

```
$ python3 -B tools/check-claim-separability.py <manifest> --lane <lane> --root <lane>
rc=0
SEPARABILITY: 0 findings
SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=1
```

A manifest whose acceptance forges the other claim's bytes is scored **0 findings, exit 0** — i.e. the
tool reads it as "verified", which is exactly what clause (e) forbids.

### 5.2 S2 — major — clause (d) is not enforceable: an inline-URL stand-in without the identifier is invisible

The static leg matches only Y's declared export regexes (`_static_findings`, 616–635). An inline URL that
stands in for a registry row but does not carry the identifier text is not matched; the dynamic leg then
accepts any `rc == 0`.

```
M-D control (inline URL embedding the identifier) → rc=1
  SEPARABILITY_DEPENDENCY C->S via export '\bS031\b' matched corpus/knowledge/c.md:1
M-C (inline URL stand-in, no identifier)            → rc=0, "SEPARABILITY: 0 findings"
```

This is precisely the failure the lane itself logged at `corpus/lessons/round-50.md:68` (R50-M1):
"inseparable claims passed by a vacuous counterfactual: a claim cited identifiers another claim created,
**and the leg tested bytes that survive the removal**". Criterion 7 forbids exactly that; the tool cannot
observe it, because the tool never learns which bytes the leg asserted.

Note in fairness to the round: the lesson's own fix column is **honest and narrow** — "shown able to
fail: it exits 1 with the C→S and S→C findings on the round-49 bytes, and its selftest's inline-URL
control exits 1". The lesson does not claim the tool detects a rewriting or vacuous leg. The over-claim is
in `corpus/QUALITY.md:31`, not in the lesson.

Also note the static leg is *not* defeated by a fake acceptance when the identifier is present in the
bytes: with `acceptance = ["sh","-c","exit 0"]` the C→S export finding is still reported (rc=1). The
exposure is precisely the case where the identifier is **absent** from the bytes (URL stand-in) or where
the acceptance manufactures the dependency.

### 5.3 S3 — major — clause (g): the mandated command is ambiguous and not executable "before dispatch"

Two independent failures:

1. **"the round manifest" is undefined.** `git grep -n "round manifest" 1c779e4` → exactly one hit,
   `corpus/QUALITY.md:31` itself. The lane's round claims manifest is
   `reports/round-50/claims.json`; the tool rejects it:

   ```
   $ python3 -B tools/check-claim-separability.py reports/round-50/claims.json --lane . --root .
   SEPARABILITY_INPUT_ERROR manifest is missing base, schema
   RC=2
   ```

   (The tool's own docstring, lines 49–51, says exit 2 "could not evaluate" and "never reads as 0".)
   Note this also contradicts `reports/round-50/claims.json:50` (Ca's `after_required`: "run on
   `reports/round-50/claims.json` exits 0"), which is unachievable with the tool as written.

2. **A pre-dispatch run is impossible with the round's own manifest.** Every unit in
   `reports/round-50/separability/r50-manifest.json` declares `"tree": "WORKTREE"` (lines 7, 25, 41, 58),
   so the checker reads the *current filesystem*, and the lands do not exist before the claims land.
   Simulating the pre-dispatch state (root = base tree `4ad2683`):

   ```
   $ python3 -B tools/check-claim-separability.py reports/round-50/separability/r50-manifest.json \
       --lane <clone> --root <base tree>
   SEPARABILITY_INPUT_ERROR unit C lands
     'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md',
     which is absent from the worktree under '<base tree>'
   RC=2
   ```

   A commit-tree manifest cannot help either: the per-claim trees do not exist until after the claims
   land. So the criterion mandates a moment at which the check cannot be performed.

3. **Related fragility (S3b, minor):** because all four units are `WORKTREE`, the gating verdict is a
   statement about the working tree, not about the landed commit. One appended line flips it:

   ```
   $ printf '\nSee corpus/lessons/round-50.md for the gate quotes.\n' \
       >> corpus/knowledge/culture-material/pastoralism-animal-husbandry.md
   $ python3 -B tools/check-claim-separability.py reports/round-50/separability/r50-manifest.json \
       --lane . --root .
   SEPARABILITY_DEPENDENCY C->REC via land path 'corpus/lessons/round-50.md' named at
     corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:201
   SEPARABILITY: 1 findings      RC=1
   ```

   (Run in the `/tmp` clone; the file was restored afterwards. Against the lane's current dirty working
   tree the same manifest still reports 0 findings.)

### 5.4 S4 — medium — clause (f) is not what the tool checks, and as written it bans a normal multi-claim round

"Sources a claim cites are that claim's lands." Under the tool's path-granular model, a claim that cites
S-rows must land the whole registry file `corpus/SOURCES.md`; if two claims in one round both cite
sources, both must land that file, and the same path in two units is an overlap finding
(`_overlap_findings`, 637–645) → `SEPARABILITY_OVERLAP C/D corpus/SOURCES.md` → exit 1. The r49 fixture
already shows this shape (`SEPARABILITY_OVERLAP C/Ca corpus/README.md`). In round 50 the rule is
satisfiable only because exactly one claim (C) cites sources — it is a latent contradiction between the
criterion's sentence and the tool's semantics, not a rule the tool enforces.

For the record, round 50's own manifest does satisfy the rule: `reports/round-50/separability/r50-manifest.json`
lists `corpus/SOURCES.md` among C's lands (lines 8–12), and the landed `corpus/SOURCES.md` diff adds
rows S048–S069 plus one header-line update.

### 5.5 S5 — minor — grounding file is unindexed (see §2)

### 5.6 S6 — nit — the operative mandate is in no executable lane contract

`SKILL.md` is **unchanged** in the landed commit (`git diff 4ad2683 1c779e4 -- SKILL.md` → empty) and
contains no occurrence of "separab" or "QUALITY". The build wave drafted the matching row
(`.ufo/waves/round-50/build/ScribeSkillRow.md:30`) but it did not land. So "Run … before dispatch" is a
rule that lives only in the admission bar, where no executor reads it.

---

## 6. What holds (positive evidence, same session)

| claim | command | result |
|---|---|---|
| the tool's own controls pass | `python3 -B tools/check-claim-separability.py --selftest` | `selftest: 56/56 checks passed`, rc 0 |
| the r49 failure shape is reproduced | `… reports/round-50/separability/r49-fixture.json --lane . --root .` | rc=1, 6 findings incl. `C->S via export`, `S->C via land path`, `SEPARABILITY_OVERLAP C/Ca corpus/README.md` — matches `reports/round-50/separability/r49-expected-independent.txt` (same 6 pairs; the prediction file is written in a normalised notation, not the tool's byte format) |
| this round's manifest is separable | `… reports/round-50/separability/r50-manifest.json --lane . --root .` | `SEPARABILITY: 0 findings`, rc=0, `acceptance_runs=3` (all three claim acceptances passed on base+own lands) |
| the tool fails closed on bad input | claims.json / pre-dispatch root | exit 2 with `SEPARABILITY_INPUT_ERROR`, never 0 (docstring 49–51) |
| the lesson's fix column is honest | `corpus/lessons/round-50.md:68` | claims only "exits 1 with the C→S and S→C findings … inline-URL control exits 1" — no claim that the tool detects rewriting/vacuous legs |

---

## 7. Smallest fixes (author-lane advice)

1. **`corpus/QUALITY.md:31`, clause (d)+(e).** Either narrow the criterion to what the tool checks, or
   make the tool able to check it. Narrowing (one sentence):
   *"a leg whose assertions survive the removal of the other claim's lands is not evidence: the checker
   sees only the leg's exit status, so the round's receipt must show the leg failing when the other
   claim's lands are removed."*
   Implementing (tool, ~20 lines): (a) hash every file of the counterfactual tree before and after the
   acceptance run (`_counterfactual` 553–567, `_git_counterfactual` 582–597); if the acceptance mutated
   anything, report `SEPARABILITY_ACCEPTANCE_MUTATED` instead of reading `rc == 0` as verified (650–651);
   (b) a vacuity leg — for each ordered pair (X, Y) with `X.acceptance`, re-run X's acceptance on
   base+X.lands with X's added lines that match Y's export regexes removed; if it still exits 0, the leg
   is vacuous with respect to Y ⇒ finding. Leg (b) also catches the §5.2 inline-URL survivor.
2. **`corpus/QUALITY.md:31`, clause (g).** Name the file, the schema and the moment:
   *"Run `python3 -B tools/check-claim-separability.py <round>/separability/rNN-manifest.json` (schema
   `kotodama-separability-manifest-v1`) on the round's separability manifest once the claim bytes exist;
   exit 0 is required before the round's claims are counted as verified."* Drop "before dispatch" (it
   cannot be satisfied) or move the run order into SKILL.md, where an executor reads it.
3. **`corpus/QUALITY.md:31`, clause (f).** Say what is meant at identifier granularity: *"the registry rows
   a claim cites are attributed to that claim; the registry file itself is landed by one claim per round,
   and a round with two source-citing claims records the shared registry as an overlap finding."*
4. **Land the lessons-index row** for `corpus/lessons/round-49-verifier-spotcheck.md` (prepared in
   `.ufo/waves/round-50/build/ReviewLessonsIndex-revision5.diff:20`) so the criterion's grounding is
   reachable from the corpus index.
5. **Style.** Split criterion 7's scope explicitly ("7. **Round claims stay separable** — (round-level;
   not an entry admission test)") and move the run instruction to SKILL.md; consider one property sentence
   + the grounding sentence, so the line sits in the same weight class as criterion 6.
6. **`reports/round-50/claims.json:50`** (Ca `after_required`) should read "run on
   `reports/round-50/separability/r50-manifest.json` exits 0", not "run on `reports/round-50/claims.json`
   exits 0" — the latter is exit 2 with the tool as written.

---

## 8. Residual risk and verification gaps

- I did not evaluate the C entry's content, the S048–S069 rows' tiers/quotes, or the O gates — other seats.
- The §5.1/§5.2 mutations were run against synthetic lanes I built in `/tmp`, not against the round's own
  manifest (read-only bounds: the r50 manifest was never modified).
- Criterion 7's grounding was checked for existence, anchor and text; whether a round-49 adjudication is
  the right lesson to hang a *standing* admission criterion on is a judgment call I flag but do not decide.
- The WORKTREE-sensitivity datum (§5.3-3) was produced in the `/tmp` clone; the lane's own dirty working
  tree still yields 0 findings at the time of writing.
- No tool installs were performed (python3 stdlib only); nothing was installed, updated or downgraded.

**Private clone `/tmp/kg7-4180537` and `/tmp/kg7-base` deleted at end of seat.**
