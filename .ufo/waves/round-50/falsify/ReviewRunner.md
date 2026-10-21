# ReviewRunner — attack on `reports/round-50/run-validation.py` + `reports/round-50/validation.json`

Seat: `KotodamaR50-2.ReviewRunner-21` (reviewer). Round 50 attempt 1, FALSIFY wave.
Axes touched: coverage, operability, calibration. Read-only attack seat; no lane file was
edited, no git/jj mutating command was run in the lane.

**Item attacked:** the round-50 before/after measurement runner (`reports/round-50/run-validation.py`,
working-tree sha256 `de5b9c16…`, later than `1c779e4`'s runner `2b7d4cd7…`) and the receipt it
produced (`reports/round-50/validation.json`).

**Verdict: PARTIAL.** The runner is a real instrument with teeth on most of its rows (9 of the
13 EXPECT rows I mutation-tested failed loudly when I broke the thing they measure). But four
defects are load-bearing, one of them breaks the receipt's own provenance, and the receipt is
not a landed artifact at all. Details below, most severe first.

---

## Reproduction setup

```bash
git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/rr21-landed
git -C /tmp/rr21-landed checkout -q 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0   # landed
git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/rr21-base
git -C /tmp/rr21-base   checkout -q 4ad26836552462d28a946ca3b067cab0b5ce3532   # base
export GIT_CEILING_DIRECTORIES=/tmp
```
All clones deleted afterwards (`rm -rf /tmp/rr21-*`). Note: `/tmp` was at 97–100 % during this
seat (other agents' 1–6 GB trees); one mutation batch aborted with `No space left on device`
and was re-run in a smaller form. No installs were needed — no tool, version, channel or
reason to record.

---

## F1 (SEVERE) — The landed runner cannot pass its own receipt; the receipt was produced by bytes that are not in the landed commit

`1c779e4`'s runner (`2b7d4cd7…`) **fails** against the landed/base pair it claims to measure:

```
$ python3 -B /tmp/rr21-landed-runner.py --tree /tmp/rr21-landed --base-tree /tmp/rr21-base \
      --probe /tmp/rr21-landed/reports/round-50/jj-colocation-probe.py
rc=1
acceptance_passed False
== C passed False
  FAIL before pastoral_topic_owner_lines expected 0 actual 1
```

Cause: the landed `TOPIC_OWNER_RE` at `reports/round-50/run-validation.py:69` (landed) is
**unbounded**:

```python
TOPIC_OWNER_RE = re.compile(r"^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)", re.IGNORECASE)
```

The substring `herd` matches `sherd`. The base tree carries one such line —
`corpus/knowledge/culture-material/writing-media-surface-economy.md:3` — so the base count is 1,
not the 0 that `EXPECT["C"]["before"]["pastoral_topic_owner_lines"]` (landed `:92`) demands.
Verified directly:

```
$ grep -rniE '^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)' /tmp/rr21-base/corpus/knowledge/
corpus/knowledge/culture-material/writing-media-surface-economy.md:3   ← "- topic: ... incidental surfaces — sherd, wall, pot, body ..."
$ grep -rniP '^- topic:.*\b(pastoral|herd|husbandr|transhuman|livestock)' /tmp/rr21-base/corpus/knowledge/
rc=1   (no match — word-bounded is correct)
```

The working-tree runner fixes exactly this (`run-validation.py:71`, `\b(...)\b`) and then passes
cleanly on the same clones:

```
$ python3 -B <lane>/reports/round-50/run-validation.py --tree /tmp/rr21-landed --base-tree /tmp/rr21-base
rc=0  acceptance_passed True   (C/O/Ca all passed)
```

**Consequence.** The receipt `reports/round-50/validation.json` records `"acceptance_passed": true`,
and the runner that produced it is the **unlanded** working-tree bytes. The landed commit
`1c779e4` contains a runner that exits 1 on the landed/base pair it ships with. The receipt is
therefore not reproducible from the landed artifact — it certifies bytes that are not in the
commit. Everything downstream that cites the receipt as the round's acceptance evidence
(`corpus/lessons/round-50.md:3` and `:14`, both landed) inherits that.

**Smallest fix:** land the one-line `TOPIC_OWNER_RE` word-bounding change from the working tree
(and regenerate the receipt from the landed bytes). One line, `reports/round-50/run-validation.py:71`.
Do **not** "fix" it by relaxing the expected value to 1 — the base tree genuinely has no
pastoralism topic owner, and the word-bounded predicate is the honest one.

---

## F2 (SEVERE) — The receipt is not in the landed commit, and the landed lesson points at it as if it were

```
$ git cat-file -e 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0:reports/round-50/validation.json
fatal: path 'reports/round-50/validation.json' exists on disk, but not in '1c779e4...'
$ git status --porcelain
?? reports/round-50/validation.json
```

Every prior round tracked its receipt — `git ls-files | grep validation.json` returns 44 entries
(`reports/round-5/…` through `reports/round-49/validation.json`). Round 50 is the only one that
does not. The landed lesson cites it anyway:

- `corpus/lessons/round-50.md:3` — ``source: … `reports/round-50/validation.json` (acceptance receipt)``
- `corpus/lessons/round-50.md:14-15` — ``Verdicts live in `reports/round-50/validation.json`, `SCORECARD.md` and `LOG.md`.``

The other two named verdict carriers are also empty for round 50: `grep -in 'round.50' SCORECARD.md
LOG.md` returns **0 hits** in both the landed commit and the working tree. So the landed lesson
points at three verdict locations and all three are silent about round 50 — the round's own
acceptance evidence is unreachable from the commit that claims it.

**Smallest fix:** `git add reports/round-50/validation.json` in the landing commit, and add the
round-50 row to `SCORECARD.md` and `LOG.md` (or amend the lesson to name only what exists).

---

## F3 (MAJOR) — `Ca`'s `r50_manifest_rc` row does not measure what `claims.json` asks for

`claims.json:50` (Ca `after_required`) says:

> "run on reports/round-50/**claims.json** exits 0"

The runner never runs the checker on `claims.json`. `EXPECT["Ca"]["after"]["r50_manifest_rc"]`
(`run-validation.py:136`, measured at `:422`) points at `MANIFEST_R50 =
"reports/round-50/separability/r50-manifest.json"` (`:62`) — a *different* file. And the command
`claims.json` actually names **fails**:

```
$ cd /tmp/rr21-landed && python3 -B tools/check-claim-separability.py reports/round-50/claims.json
SEPARABILITY_INPUT_ERROR manifest is missing base, schema
rc=2
```

`claims.json` is not a separability manifest (no `schema`, no `base`, no per-unit `tree`/`exports`
keys); it is a claims *declaration*. The manifest schema is `kotodama-separability-manifest-v1`.
So the literal `after_required` clause is unsatisfiable as written, and the runner quietly
substitutes a different artifact that does satisfy it. The runner's `Ca` acceptance therefore
certifies a fact nobody declared.

This matters because the substituted manifest is materially weaker than `claims.json`'s intent.
`r50-manifest.json` declares `corpus/SOURCES.md` as one of C's own lands, which is what makes
the C→S dependency invisible to the checker:

```
# manifest as shipped, C lands include corpus/SOURCES.md  → 0 findings, rc 0
$ python3 -B tools/check-claim-separability.py reports/round-50/separability/r50-manifest.json
SEPARABILITY: 0 findings        rc=0

# same manifest with corpus/SOURCES.md removed from C's lands (matching claims.json C.lands)
$ python3 -B tools/check-claim-separability.py /tmp/rr21-manifest-nosources.json
SEPARABILITY_DEPENDENCY C-><base> via acceptance […] fails on base+C.lands (rc=1) and
  no declared unit's lands repairs it
SEPARABILITY: 1 findings        rc=1
```

That is a design decision (documented in `corpus/lessons/round-50.md:20-22`: "this round's own
manifest declares `corpus/SOURCES.md` as a land of C, because the rows C cites are C's sources").
It is defensible for round 50 — but it is **not** what `claims.json:50` asked to be measured, and
the runner's receipt reports it as if it were.

**Smallest fix:** amend `claims.json:50` to name the artifact actually measured
(`reports/round-50/separability/r50-manifest.json`), or extend the checker to accept the
claims-declaration schema. Either way the declared `after_required` and the measured artifact
must agree; right now they do not.

---

## F4 (MAJOR) — Two EXPECT rows are unfalsifiable as written

### F4a — `quality_cites_spotcheck` / `quality_separab_lines` cannot detect criterion 7's absence

`claims.json:50` requires "QUALITY **criterion 7** cites the spot-check". The runner checks only
that *some* line of `corpus/QUALITY.md` contains `separab` and that *some* line contains
`round-49-verifier-spotcheck` (`run-validation.py:138-139`, measured `:424-425`). It never checks
that a criterion **numbered 7** exists.

Mutation: renumber criterion 7 → 8 in `corpus/QUALITY.md`. The runner reports success:

```
--- V1 QUALITY: renumber criterion 7 -> 8 (criterion 7 no longer exists) -> runner rc=0
   acceptance_passed True   fails: NONE (check did not notice)
```

The real `QUALITY.md:31` is criterion 7 in a `1.`–`7.` list; renumbering it to `8.` breaks the
declared contract and the receipt stays green. (For contrast, deleting the `separab` substring
*does* fail the runner — V2 — so the row has half a grip.)

**Smallest fix:** assert the criterion number explicitly, e.g. count lines matching
`^\s*7\.\s` that also contain the spot-check path, instead of two independent substring counts.

### F4b — `C`'s README row order and the entry's line budget are never checked

`claims.json:17` requires "entry landed per contract" (the contract is "<=~250 lines … README
index row in filename order"). The runner measures `entry_lines` (`:311`) but **no EXPECT row
uses it**, and nothing checks README row order.

Mutations, both green:

```
--- V3 README: move the pastoralism row out of filename order -> runner rc=0
   acceptance_passed True   fails: NONE
--- V4 entry: bloat past 250 lines (contract says <=~250) -> runner rc=0
   acceptance_passed True   fails: NONE
```

The landed README *is* currently in filename order within every section (verified: all six
sections `sorted? True`), and the entry is 199 lines — so the artifacts are fine today. The
**measurement** does not establish it, and the receipt presents a green that a future editor
could break silently.

**Smallest fix:** add two EXPECT rows — `entry_lines` `("max", 250)`, and a README-order check
(per-section filename sort), the latter either in the runner or as a sweep leg.

---

## F5 (MODERATE) — `O`'s "all prior controls retained" clause is measured by exit code only

`claims.json:36` (O `after_required`) requires "receipt_guard --selftest and
check-readme-revisions --selftest pass **with all prior controls retained**". The runner asserts
only `receipt_guard_selftest_rc == 0` and `readme_revisions_selftest_rc == 0`
(`run-validation.py:122-123`, measured `:364-367`). Exit code 0 says the *surviving* controls
pass; it says nothing about whether a prior control was **deleted**.

Mutation: remove/blank one prior control label from the landed readme gate's selftest. The
runner stays green:

```
--- V6 readme gate: neuter a prior selftest control but keep exit 0 -> runner rc=0
   acceptance_passed True   fails: NONE
```

Fact check, for fairness: the controls were in fact retained. Base tree = 11 controls, landed
tree = 15 (11 base labels all present + 4 new fail-closed ones), so the *claim* is true. But the
receipt's own evidence makes it look false in the opposite direction — the receipt's truncated
12-line tail shows PASS-in-tail **10 (before) → 9 (after)**, because `brief()` (`:180-182`) keeps
only the last 12 lines and the after-run's tail is dominated by the 4 new controls' long
`unreachable in /tmp/…` messages. A reviewer reading the receipt would conclude controls were
*dropped*. The receipt is misleading in the safe direction here, but by accident, not by design.

**Smallest fix:** record the control count (not the tail) in the receipt — e.g. count `PASS `
lines across full stdout — and assert `after_count >= before_count`.

---

## Rows I proved DO have teeth

Mutation-tested on a clone of the landed commit; each broke the artifact and the runner failed
loudly, so these rows are not vacuous:

| Mutation | Runner result |
|---|---|
| add a bogus finding to `r49-expected-independent.txt` | `rc=1` — `Ca r49_matches_independent_prediction` False |
| delete `r49-expected-independent.txt` | `rc=1` — `r49_matches_independent_prediction` None, `r50_manifest_rc` 2 |
| add an `### ` section to the entry | `rc=1` — `C entry_h3` 1 |
| break S050's `used-by` cell | `rc=1` — `C sources_unresolved` `['S050:used-by-missing-entry']` |
| delete criterion 7 from QUALITY.md | `rc=1` — `quality_separab_lines` 0, `quality_cites_spotcheck` 0 |
| strip the `separab` substring everywhere | `rc=1` — `quality_separab_lines` 0 |
| delete the entry's `- couples:` field | `rc=1` — `C entry_head_fields_ordered` False |
| make `receipt_guard --selftest` always exit 0 | `rc=1` — `O receipt_guard_selftest_rc` 1, probe values `None` |

The separability checker itself is sound on the r50 manifest: adding a synthetic `S` unit that
lands `corpus/SOURCES.md` and exports the S048+ pattern yields the expected findings and rc 1 —
```
SEPARABILITY_DEPENDENCY C->S via export '\bS0(4[89]|[5-9]\d)\b' matched …pastoralism-animal-husbandry.md:7
SEPARABILITY_OVERLAP C/S corpus/SOURCES.md
SEPARABILITY: 4 findings
```
and its `--selftest` passes 56/56 with both negative and positive controls. The `r49-fixture.json`
frozen fixture still exits 1 naming C→S, and `r49-expected-independent.txt` still matches the
tool's output exactly.

---

## Rerun summary

| Run | Tree | Result |
|---|---|---|
| working-tree runner `de5b9c16…` | landed `1c779e4` + base `4ad2683` | `rc=0`, `acceptance_passed: true` — all three claims pass; receipt reproduced except for two path strings in `readme_revisions_selftest` tails (`/tmp/kr50-base`→`/tmp/rr21-base`, random tmpdir names) |
| landed runner `2b7d4cd7…` | same | `rc=1`, `acceptance_passed: false` — `C before pastoral_topic_owner_lines` expected 0 actual 1 (F1) |
| landed runner, `--probe` pointed at the landed probe | same | same single failure (isolates F1 to the regex, not the probe path) |
| receipt's exact argv replayed now | `/tmp/k50-landed` + `/tmp/k50-baseclone` | `rc=0`, `acceptance_passed: true` — still green, but with the *current* (v3) lane probe, not the v2 probe the receipt names |

---

## Residual risk / verification gaps

- **The lane working tree has drifted since the receipt was written** — `git status` now shows
  modified `reports/round-50/jj-colocation-probe.py` (v3: R1 predicate tightened to require the
  landed sha to be *exactly* the remote tip), `tools/harness/receipt_guard.py`,
  `tools/check-readme-revisions.py`, `corpus/SOURCES.md`, the entry, and `corpus/lessons/round-50.md`,
  plus an untracked `reports/round-50/telemetry/jj-probe-v3.txt`. The receipt's
  `"probe": "/home/vgpnk/…/reports/round-50/jj-colocation-probe.py"` therefore points at bytes that
  no longer match the probe the receipt was produced with (receipt-era sha `d3fff001…` vs current
  `dee0c65b…`). **The receipt is not reproducible from its own recorded inputs**, independent of F1.
  I did not evaluate whether the v3 predicate is right — that is the `CriticProbeV2` seat's scope;
  I only record that the receipt's instrument pointer is stale.
- I did not re-verify the 22 SOURCES rows' URLs (that is the `ReopenS04x`/`ReopenS05x` seats), the
  guard's own R1–R3 semantics (the `MutateGuard`/`ReviewGuardCode` seats), or the checker's
  counterfactual-tree correctness (`ReviewSepTool`/`MutateSepTool` seats). Nothing in this report
  should be read as clearing those.
- The mutation battery was limited by `/tmp` pressure (97–100 % during the run). Each mutation was
  run in a fresh clone of `1c779e4` with the base tree held at `4ad2683`, so results are
  single-tree-isolated; I did not run the mutations against the base tree to confirm the `before`
  rows also fail when the base is perturbed.
- `readme_revisions_selftest`'s control-count comparison in F5 is from a single pair of runs; the
  base/landed label diff was noisy because the new controls' PASS text embeds a random tmpdir
  path, so I compared control *count* and the set of the 11 base labels rather than exact strings.
  The base→landed direction (11 → 15, none dropped) is confirmed; the exact label set is.

---

## Smallest fixes, in one place

1. **Land the `TOPIC_OWNER_RE` word-bounding** (`run-validation.py:71`) — one line — and regenerate
   the receipt from the landed bytes. Until then the landed runner exits 1 on its own trees. (F1)
2. **`git add reports/round-50/validation.json`** in the landing commit, and add the round-50 rows
   to `SCORECARD.md` / `LOG.md`, or amend `corpus/lessons/round-50.md:3,14-15` to name only what
   the commit actually contains. (F2)
3. **Reconcile `claims.json:50` with what is measured**: either rename the artifact to
   `reports/round-50/separability/r50-manifest.json`, or teach the checker the claims-declaration
   schema so the declared command can be run literally. (F3)
4. **Two new EXPECT rows**: criterion number (`^\s*7\.\s` line containing the spot-check) instead
   of two substring counts; and `entry_lines` `("max", 250)` plus a README filename-order row.
   (F4a, F4b)
5. **Record selftest control counts, not the 12-line tail**, and assert `after >= before`. (F5)
6. Re-run the probe and the receipt against the *final* tool bytes once the working-tree drift
   settles, so the receipt's `"probe"` pointer names the bytes it was produced with.

Author-lane advice, not admission. Verdict on the item attacked: **PARTIAL** — the instrument is
real and mostly honest, but the receipt it produced is not a landed artifact, is not reproducible
from the commit it belongs to, and its `Ca` leg measures a substitute for the declared one.
