# ReviewSepTool — round 50 attempt 1, FALSIFY wave

**Item attacked:** claim **Ca** — `tools/check-claim-separability.py` at landed commit
`1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`),
together with its two committed artifacts `reports/round-50/separability/r49-fixture.json` +
`reports/round-50/separability/r49-expected-independent.txt` and
`reports/round-50/separability/r50-manifest.json`.

**Verdict: PARTIAL.** The tool is sound where it is exercised and its declared semantics are
implemented as written; but it is **blind to a real C→REC dependency in the round it was built to
police** (the r50 manifest's `0 findings` is obtained by a citation spelling the matcher cannot
see), **its export-novelty guard is vacuous in the common case** (false-positive dependencies),
and **its dynamic leg cannot distinguish a broken unit from a separable one** when the manifest's
acceptance argv is vacuous — which is exactly the r49 mistake class the tool exists to catch. Two
of the six "expected" edges in the frozen fixture are prose mentions, not couplings, and the
"independent prediction" comparator cannot tell the difference.

Author-lane advice, not admission.

---

## 0. Method and hygiene

* All landed bytes were read from a **private clone**, never the lane worktree:
  `git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/sep-review-XXXX` →
  `git -C … checkout -q 1c779e4a…` (clone HEAD verified `1c779e4a…`; `git status --porcelain` clean).
  A second clone `/tmp/sep-base` was checked out at `4ad2683…` for base-tree counterfactuals.
  `GIT_CEILING_DIRECTORIES=/tmp` on every git-touching run.
* **No lane write.** No `git add/commit/stash/checkout/reset`, no `jj`, no write under
  `/home/vgpnk/Projects/shokunin/.ufo`, no edit to any lane file. The lane worktree already showed
  `M reports/round-50/run-validation.py` and two untracked `.ufo/waves/round-50/falsify-*.json`
  files **before** my work (other seats); I did not touch them.
* Counterexample harnesses: `/tmp/sep-exp/{ce.py,ce6.py,comparator.py}` (throwaway git repos under
  `/tmp`, removed). Tooling: python3 3.14.8, git 2.56.0 — **no installs, no updates, no pacman/uv/npm/cargo
  activity**.
* Temp clones deleted after the report was written.

---

## 1. What HOLDS (verified, with output)

| surface | verdict | evidence |
|---|---|---|
| `--selftest` | **HOLDS** | `python3 -B tools/check-claim-separability.py --selftest` → `selftest: 56/56 checks passed …`, rc 0 (2.7 s) |
| exit codes | **HOLDS** | 0 = no findings, 1 = findings, 2 = could not evaluate; input errors print `SEPARABILITY_INPUT_ERROR` on stderr; `SEPARABILITY_UNEVALUATED` on stdout, never 0 |
| added-lines scanning | **HOLDS** | `tools/check-claim-separability.py:479-488` (line-set difference against the base blob); a base line reused verbatim by the claim is not scanned |
| base-absent path rule | **HOLDS (as specified)** | `:483` `unit.base_absent[rel] = base is None`; `:630` `for rel in y.name_paths()` — a path that already resolves at base is not a name target |
| export novelty | **HOLDS as written, vacuous in practice** | `:491-500` — see **F3** |
| overlap | **HOLDS** | `:637-645` → `SEPARABILITY_OVERLAP X/Y PATH`, exit 1 |
| record units | **HOLDS** | `:618` `if x.role == "record": continue`; records carry no acceptance (`:415`) but may still be dependency *targets* |
| `WORKTREE` | **HOLDS** | `:451-467` reads lands from `--root` via `lstat`, never through git; absent land → exit 2 |
| r49 fixture (the declared Ca acceptance) | **HOLDS** | `python3 -B tools/check-claim-separability.py reports/round-50/separability/r49-fixture.json --lane .` → rc **1**, 6 findings including `SEPARABILITY_DEPENDENCY C->S via export …` and `… S->C …` |
| r50 manifest | **HOLDS as run** | `… r50-manifest.json --lane . --root .` → `SEPARABILITY: 0 findings`, rc 0, `acceptance_runs=3` |
| landed receipt runner (Ca slice) | **HOLDS** | `python3 -B reports/round-50/run-validation.py --tree /tmp/sep-review-XXXX --base-tree /tmp/sep-base` → Ca `passed=true`; all 8 Ca `after` checks ok (`r49_fixture_rc=1`, `r49_detects_C_to_S=true`, `r49_matches_independent_prediction=true`, `r50_manifest_rc=0`, `checker_selftest_rc=0`) |

Note (other seats' axes, not mine): the same runner reports `acceptance_passed: False` overall —
claim **C** fails its own before-check `pastoral_topic_owner_lines` (expected 0, actual 1) — and
`reports/round-50/validation.json` does **not exist** at `1c779e4a…` although
`corpus/lessons/round-50.md:3` and `:14` point the reader at it.

---

## 2. Findings

### F1 — HIGH — the r50 "separable" verdict hides a real C→REC dependency, and one token flips it

`reports/round-50/separability/r50-manifest.json` declares `corpus/lessons/round-50.md` as a land of
the **record** unit `REC` (it is absent at base, so it *is* a name path), and `corpus/SOURCES.md`
as a land of **C**. But the registry contract written in C's own landed bytes says the evidence for
C's rows lives in that lesson:

* `corpus/SOURCES.md:8` (landed, added line): *"the round lesson's `## Gate` (`lessons/round-49.md`
  for S001–S047, `lessons/round-50.md` for S048–S069) holds each row's URL, access date and
  **verbatim quote**."*
* `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:9` (the entry's own `- source:`
  field): *"… each with URL, access date 2026-10-21, tier scope and **the round lesson's located
  quote**."*

So C's landed entry quotes evidence that exists only in `corpus/lessons/round-50.md` — REC's land.
The tool does not report it, because both citations spell the lesson **without its repo path**, and
`_name_re` (`:602-604`) matches whole paths only. The build wave knew this:
`.ufo/waves/round-50/build/ExecSepFixture.md` §"Conditions on expected r50 findings: none" item 2
records the choice: *"the r49 precedent (SOURCES line 8) uses the bare form `` `lessons/round-49.md` ``
which stays clean. Bare form, or accept the finding."*

**Mutation proof** (private clone only; reverted; `git status` clean afterwards):

```
# corpus/SOURCES.md : "`lessons/round-50.md`" -> "`corpus/lessons/round-50.md`"
$ python3 -B tools/check-claim-separability.py reports/round-50/separability/r50-manifest.json --lane . --root .
SEPARABILITY_DEPENDENCY C->REC via land path 'corpus/lessons/round-50.md' named at corpus/SOURCES.md:8
SEPARABILITY: 1 findings                      rc=1

# entry line 9: "the round lesson's located quote" -> "the round lesson `corpus/lessons/round-50.md`'s located quote"
SEPARABILITY_DEPENDENCY C->REC via land path 'corpus/lessons/round-50.md' named at corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:9
SEPARABILITY: 1 findings                      rc=1
```

Same manifest, same tree, same claims — **one spelling of one path** turns "separable" into
"inseparable". The shipped bytes use the spelling that hides it. This is the r49 shape the whole
round exists to prevent (`corpus/lessons/round-50.md:68` (R50-M1) and `:70` (R50-M3) name it), and the control
that was built to detect it does not detect it in r50.

**Smallest fix (author lane):** move the Gate-quote dependency out of the record — either land
`corpus/lessons/round-50.md` under **C**'s lands (then C→REC becomes a legitimate co-ownership
question) or give C's acceptance a Gate-resolution leg that reads the lesson
(`grep` the cited row's quote in `corpus/lessons/round-50.md`) so the coupling is detected by the
dynamic leg instead of by spelling. Independently: make the land-path matcher accept a basename
form **when the basename is unique among the manifest's land paths**, so the two spellings cannot
disagree.

### F2 — HIGH — O's acceptance in the r50 manifest is vacuous: it passes on the base tree unchanged

`r50-manifest.json`, unit `O`:

```
"acceptance": ["sh","-c","python3 -B tools/harness/receipt_guard.py --selftest >/dev/null && python3 -B tools/check-readme-revisions.py --selftest >/dev/null"]
```

Run on the **base** tree (pre-fix r49 tool bytes), in `/tmp/sep-base` @ `4ad2683…`:

```
$ sh -c "python3 -B tools/harness/receipt_guard.py --selftest >/dev/null && python3 -B tools/check-readme-revisions.py --selftest >/dev/null"; echo rc=$?
rc=0
```

Contrast, C's acceptance on the same base tree: `rc=1` (FileNotFoundError on the entry) — C's
acceptance **discriminates**; O's does not. The checker never runs a unit's acceptance *without* the
unit's own lands (`_acceptance_findings`, `:647-670`, runs only `base+unit.lands` and
`base+unit.lands+other.lands`), so it cannot see the difference and reports `0 findings` for O as
if it were verified. A claim whose acceptance passes at base is, by construction, not proven by the
tool — that is the exact "vacuous counterfactual leg" defect of r49
(`corpus/lessons/round-50.md:68` (R50-M1)), reproduced inside the manifest that criterion 7 tells the
lane to run.

**Smallest fix:** add a base-only acceptance run per unit and require it to **fail** (report
`SEPARABILITY_ACCEPTANCE_VACUOUS X` when it passes); or, in the manifest, replace O's argv with the
probe that actually discriminates (`reports/round-50/jj-colocation-probe.py --tools-root <tree>`,
which is what `reports/round-50/run-validation.py` really uses for O).

### F3 — HIGH — export novelty is checked against the wrong base, so a broad export fabricates dependencies

`_check_novelty` (`:491-500`) validates each export against the base bytes of **the exporting
unit's own lands**. When those lands are new files, the base side is empty and the check is
vacuous: any regex passes as "novel". The export is then used to accuse other units
(`_static_findings`, `:623-628`), including for identifiers the exporting unit never introduced.

Counterexample (`/tmp/sep-exp/ce.py`, case CE-2; base has `docs/base.md` = "registry row S001 is
defined here"; Y lands a new `docs/y.md` and declares `exports: ["\\bS\\d{3}\\b"]`; X cites
"S001"):

```
SEPARABILITY_DEPENDENCY X->Y via export '\\bS\\d{3}\\b' matched docs/x.md:1
SEPARABILITY: 1 findings          rc=1
```

S001 pre-exists at base and Y introduced no identifier at all — **no dependency exists**. Control
CE-2b (Y's export narrowed to `\bS999\b`) → `0 findings`. The tool's own docstring sells this as
"export novelty: each Y export must match no line of base bytes in Y's lands, else exit 2" — a
guard that cannot fire in the common case (a unit whose lands are all new files, e.g. Ca's checker,
or r50 C's entry).

**Smallest fix:** check export novelty against the **whole base tree** (or require every export
match to occur in the exporting unit's *added* lines), and reject an export that matches identifiers
present in base bytes anywhere in the lane.

### F4 — MEDIUM — the `needs_git` counterfactual overlays are invisible to git-visible acceptance

`_git_counterfactual` (`:582-600`) clones `--root`, checks out the base commit and writes the
unit's lands onto the working tree **without staging or committing them**. An acceptance that reads
git-visible state therefore measures the **base** bytes, not the unit's landed bytes.

Counterexample CE-1 vs CE-1b (identical unit; only the acceptance argv differs):

| case | acceptance | result |
|---|---|---|
| CE-1 | `sh -c "git show HEAD:tools/gate.py \| python3 -"` (unit's landed `tools/gate.py` exits 1) | `SEPARABILITY: 0 findings`, **rc=0** — broken unit reads as separable |
| CE-1b | `sh -c "python3 tools/gate.py"` (same landed bytes) | `SEPARABILITY_DEPENDENCY X-><base> via acceptance … (rc=1)`, rc=1 |

The dynamic leg's own contract ("base with the unit's lands overlaid") is therefore only true for
the filesystem, not for git. It matters here: O's real gates are git-reading tools
(`tools/harness/receipt_guard.py` probes refs; `tools/check-readme-revisions.py` pins a
`BASE_COMMIT`), so an acceptance that inspects git state measures the wrong tree.

**Smallest fix:** in `_git_counterfactual`, `git add -A` the overlays (and optionally commit them
on a scratch branch) before running the acceptance, so `git show/ls-tree/diff --cached` see the
overlaid bytes; add a selftest control that asserts a git-visible acceptance measures the overlay.

### F5 — MEDIUM — the land-path leg is whole-path only: a basename citation is invisible

`_name_re` (`:602-604`) requires the full repo path. CE-3 / CE-3b, same citation, two spellings:

```
CE-3  X: "run thing.py for the check"        -> SEPARABILITY: 0 findings  (rc=0)   # real dependency missed
CE-3b X: "run tools/thing.py for the check"   -> SEPARABILITY_DEPENDENCY X->Y via land path 'tools/thing.py' (rc=1)
```

`tools/thing.py` is absent at base, so the CE-3 dependency is real. This is the same defect
`.ufo/waves/round-50/build/ReviewSepFixtureFacts.md` §F2 flagged for r49 ("Ca→C (rule-dependent):
suffix or basename rule only") and it is what makes **F1** invisible. The r50 landed bytes use the
basename form for the round lesson (F1) and the lane's own `corpus/SOURCES.md:8` uses the basename
form for `lessons/round-49.md`.

**Smallest fix:** match a land path by basename as well, when that basename is unique among the
manifest's land paths; report the matched form in the finding line.

### F6 — MEDIUM — the "independent prediction" comparator throws away the discriminating content

`reports/round-50/separability/r49-expected-independent.txt` is the calibration oracle, but
`reports/round-50/run-validation.py`'s `_norm_finding` / `r49_matches` compare only
`(kind, pair, leg, target)` and discard the id list and the occurrence counts. Probe
(`/tmp/sep-exp/comparator.py`, using the landed runner's own code):

```
original expected file                                     -> matches=True
export leg claims only S031 (1 of 12 ids)                  -> matches=True
land-path occurrence count changed x2 -> x99               -> matches=True
S->C occurrence count changed x12 -> x0                    -> matches=True
export leg's 'matched' clause renamed to 'ignored'         -> matches=False
S->C edge relabelled S->Ca                                 -> matches=False
```

So the receipt's `r49_matches_independent_prediction: true` certifies only the *shape* of the edge
set. It cannot distinguish "matched S031…S042" from "matched S031", and it cannot detect that the
tool reports only the **first** hit per pair (`_first_line_hit`, `:607-614`) while the prediction
file asserts 12 ids and per-site counts. The tool and the "independent" prediction are therefore not
independent witnesses of the export leg's substance.

**Smallest fix:** compare the full normalised finding set including the matched identifiers and
occurrence counts, and have the tool report *all* hits for an export match (or a count), so the
oracle can be checked at that resolution.

### F7 — MEDIUM — two of the six frozen "expected dependency" edges are prose mentions, not couplings

The fixture's expected set (and the shipped prediction file) treat a **mention** of a sibling
claim's path as a dependency edge. At the fixture's trees:

* `corpus/README.md:18` @ `8c78e6b`: *"duplicate, stub and out-of-order revision labels are now
  caught by `python3 tools/check-readme-revisions.py` (exit 1)"* → the fixture's
  `C->Ca via land path 'tools/check-readme-revisions.py'` edge. C's acceptance
  (`assert len(L)==205 …` on the entry) needs nothing from Ca's tool.
* `corpus/lessons/round-49.md:12` @ `d91c632`: *"**Ca** calibration — the dangling `revision: 2.0`
  README stub removed and `tools/check-readme-revisions.py` landed"* → the fixture's `S->Ca` edge.

The other four (`C->S` export, `C->S` via `corpus/SOURCES.md` — absent at base `c42d675`,
`S->C` via the entry path, and the `C/Ca` README overlap) are genuine couplings. So the round's
calibration artifact freezes 6 "dependencies" of which 2 are changelog prose. Under criterion 7's
letter ("may not … name a path another claim newly lands") the tool is correct; the finding is that
the criterion, as written, turns every README changelog entry and every lesson's claim list into a
coupling, and the frozen artifact presents that as measured separability.

**Smallest fix:** distinguish *resolution* from *mention* — require the naming line to be a
reference that the claiming unit's own acceptance must resolve (e.g. only count a path mention when
the citing line is inside a citation-bearing field, or when the acceptance fails without the other
unit's lands), and re-derive the fixture's expected set under that rule.

### F8 — LOW — `claims.json`'s declared Ca acceptance is unsatisfiable and was never corrected

`reports/round-50/claims.json` (Ca.after_required) still says *"run on
`reports/round-50/claims.json` exits 0"*. The landed tool, on that file:

```
$ python3 -B tools/check-claim-separability.py reports/round-50/claims.json --lane .
SEPARABILITY_INPUT_ERROR manifest is missing base, schema
rc=2
```

`claims.json` is a claim ledger, not a manifest (no `schema`/`base`/`tree`/`exports`). The build
seat already flagged the discrepancy (`.ufo/waves/round-50/build/ExecSepTool.md` §"Discrepancy to
flag") and a reviewer called it unsatisfiable
(`.ufo/waves/round-50/build/ReviewR50Separability.md` H2); the landed text is unchanged, and
`reports/round-50/run-validation.py` silently substitutes a *different* acceptance set (fixture +
r50 manifest + selftest). The declaration and the executed evidence are not the same thing.

**Smallest fix:** amend Ca.after_required to name the two manifests it actually runs
(`r49-fixture.json` → exit 1; `r50-manifest.json` → exit 0) and drop the `claims.json` clause, or
land a derived manifest and pin it.

### F9 — LOW — an unevaluable `needs_git` leg silently discards already-computed static findings

`evaluate` (`:672-710`) computes the static findings first, then raises `Unevaluated` from the
`needs_git` leg; `main` (`:1218-1220`) prints only `SEPARABILITY_UNEVALUATED …` and exits 2. Probe
(`/tmp/sep-exp/ce6.py`) — a manifest with a **real** static dependency and an unusable `--root`:

```
usable --root      : SEPARABILITY_DEPENDENCY X->Y via export … ; SEPARABILITY: 1 findings ; rc=1
unusable --root    : SEPARABILITY_UNEVALUATED git clone failed (rc=128) … ; rc=2   (no dependency printed)
```

The exit code fails closed (good), but a caller scanning stdout for `SEPARABILITY_DEPENDENCY` sees
none, and "no findings printed" is indistinguishable from "no dependency".

**Smallest fix:** print the static findings before the `SEPARABILITY_UNEVALUATED` line (or state in
the docstring that an unevaluable dynamic leg suppresses the static verdict).

### F10 — LOW — the r50 manifest pins no commit, so its verdict is not bound to the landed bytes

All four units of `r50-manifest.json` declare `"tree": "WORKTREE"`, i.e. the lands are read from
whatever is on the filesystem at run time (`:451-467`). `ExecSepFixture.md` describes this as a
placeholder — *"all trees `WORKTREE` (= read the lane filesystem at runtime; placeholder until the
integrator fills real trees at landing …)"* — and the landed manifest still carries the placeholder.
Consequences: (i) the round's separability receipt is not reproducible from the committed artifact
alone; (ii) any later edit to a land silently changes the verdict (F1 shows a one-token edit doing
exactly that); (iii) `corpus/QUALITY.md:31` instructs *"Run `tools/check-claim-separability.py` on
the round manifest **before dispatch**"*, which is not satisfiable for r50 — the manifest was created
during the build wave, after dispatch, and pins nothing.

**Smallest fix:** fill the `tree` fields with the landed commit (`1c779e4a…`, or per-unit commits
when the claims are re-cut) and re-run; keep `WORKTREE` only for in-flight work.

### F11 — LOW — exit-code semantics conflate "this unit is broken" with "these units are coupled"

A unit whose acceptance fails on `base+unit.lands` and is repaired by no declared unit yields
`SEPARABILITY_DEPENDENCY X-><base> …` and **exit 1** with `SEPARABILITY: 1 findings` (CE-1b). A
caller reads exit 1 as "coupling found"; the true cause is that the unit fails alone. The message
is honest, the exit code is not.

**Smallest fix:** keep exit 1 for couplings, and give `X-><base>` its own exit code (or a distinct
`SEPARABILITY_UNIT_FAILS_ALONE` line) so a self-broken unit is never reported as inter-claim
coupling.

---

## 3. Per-surface verdicts (the surfaces named in the assignment)

| surface | verdict | where |
|---|---|---|
| added-lines scanning | HOLDS (line-set difference, base reuse invisible) | `:479-488` |
| base-absent path rule | HOLDS as specified; **the rule is what hides F1** | `:483`, `:630` |
| export novelty | **BROKEN as a guard** (vacuous when the exporting unit's lands are new) | `:491-500` → **F3** |
| overlap | HOLDS | `:637-645` |
| record units | HOLDS as specified; records are exempt as dependers, which is what lets F1 pass | `:618`, `:415` |
| `WORKTREE` | HOLDS mechanically; **unpinned trees make the r50 verdict non-reproducible** | `:451-467` → **F10** |
| `needs_git` leg | **PARTIAL** (overlays invisible to git-visible state; unevaluable leg suppresses static findings) | `:582-600`, `:672-710` → **F4**, **F9** |
| exit codes | HOLDS (0/1/2 correct); misleading attribution for a self-broken unit | `:1218-1226` → **F11** |
| r49 fixture + expected file | PARTIAL — detects C→S (the declared 1/1), but 2 of 6 edges are prose mentions and the comparator discards id/count content | **F6**, **F7** |
| r50 manifest | **PARTIAL — `0 findings` is real but incomplete**: a live C→REC dependency exists and is one spelling away from being reported; O's acceptance is vacuous | **F1**, **F2** |

---

## 4. Residual risk and verification gaps

* The falsification of F1 rests on the *substantive* claim that C's entry depends on the lesson's
  verbatim quotes. That is supported by the registry's own contract text
  (`corpus/SOURCES.md:8`) and by the entry's `- source:` field (`…:9`), not by an executed
  resolution test — the lane has no acceptance leg that checks a cited row's quote against the
  lesson. **Not verified here:** whether the round-50 rows' quotes are byte-identical between
  `corpus/SOURCES.md` and `corpus/lessons/round-50.md` (a source-tier/quote seat's question).
* I did not re-open any S048–S069 URL, and I did not audit the tier/scope of any row: those are
  the source re-openers' seats.
* The counterexample manifests (`/tmp/sep-exp/*`) are minimal reproductions of *rule* behaviour;
  they do not assert that the r50 round's claims are factually wrong — only that the control's
  verdict is spelling-sensitive, argv-sensitive and incomplete.
* `reports/round-50/validation.json` does not exist at `1c779e4a…`, so no committed receipt records
  the Ca measurements I re-ran; my numbers come from running the landed runner in a private clone.
* The lane worktree carries `M reports/round-50/run-validation.py` from another seat; my clone is
  pinned to the landed commit, so all "landed bytes" statements above are commit-pinned, but a
  *later* revision of that runner would change the receipt's numbers (F6 concerns its comparator).

## 5. Smallest-fix summary (author lane)

1. **F1** — make the lesson's Gate quotes part of C's lands, or add a Gate-resolution acceptance;
   make the land-path matcher basename-aware for unique basenames. *(without this, the r50
   "separable" verdict does not survive its own mutation test)*
2. **F2** — run each unit's acceptance base-only and fail the unit when it passes there; replace
   O's manifest argv with the probe that discriminates.
3. **F3** — check export novelty against the whole base tree, not the unit's own lands.
4. **F4** — stage/commit the overlays in the `needs_git` clone so git-visible acceptances measure
   the overlay.
5. **F5/F7** — match unique basenames; separate *mention* from *resolution*.
6. **F6** — compare the full finding set (ids and counts) and make the tool report every hit.
7. **F8/F10** — amend `claims.json`'s Ca.after_required to the two manifests actually run; fill the
   manifest's `tree` fields with the landed commit.
8. **F9/F11** — print static findings before `SEPARABILITY_UNEVALUATED`; give `X-><base>` its own
   signal.

## 6. Tooling record

* **No installs, no updates.** Used the pre-existing `python3` 3.14.8 and `git` 2.56.0; coreutils.
* No pacman transaction (host-wide pacman transactions are paused), no `uv`, no `npm`, no `cargo`.
* Scratch: `/tmp/sep-review-XXXX` (clone @ `1c779e4a…`), `/tmp/sep-base` (clone @ `4ad2683…`),
  `/tmp/sep-exp/{ce.py,ce6.py,comparator.py}` — all removed after this report was written.
