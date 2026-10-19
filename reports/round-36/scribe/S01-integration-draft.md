- Seat: S01 | scribe | cross | date 2026-10-19 | baseline ce103bf

# S01 — round-36 integration dossier: fleet-report material, validation-leg spec, selftest list

Purpose: give the integrating parent (a) the fleet-report draft for
`../.ufo/reports/round-36/kotodama.md`, (b) a machine-checkable leg spec it
implements as `reports/round-36/run-validation.py`, and (c) the selftest control
list. Every value in §8 was measured by this seat at the round-36 tree on
2026-10-19 with the commands in §8; every value keyed to a fragment path is a
placeholder the integrator fills from the landed fragment.

Baseline `ce103bf5885af00023cdc4a174c17602476cdcf8` (= `git rev-parse HEAD` =
`git rev-parse ce103bf`, §8 M4). All python ran with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` from the lane root. This
seat executed **no** filed round runner in-tree (F-C13-1); the two filed runners
it needed were run with `--check` inside a `git archive HEAD` copy (§8 M9, M10),
and `--check` never publishes.

**Non-author declaration:** this seat authored no lane artifact before this
round. No promotion, canon, clearance or closure verdict is claimed anywhere in
this file; each such token appears only as a negation, a routed reference, or a
quoted scanner pattern (§6.7).

---

## §0 — Dependency state at this seat's cut, and one incident the integrator must read first

### 0.1 What exists

`reports/round-36/` held **26 files** at this seat's last read (§8 M1): the two
declarations, two telemetry files, and 22 landed seat fragments. The 32 declared
seat outputs are enumerated at §8 M3; the 10 still absent are listed in §10.

`../.ufo/reports/round-36/` **does not exist** (§8 M12) — the fleet report is
integrator-only, written outside this repo.

### 0.2 INCIDENT — a filed byte was rewritten in the live tree during this round's wave

**Finding (F-S01-1).** During the round-36 wave, `reports/round-34/validation.json`
was rewritten **in the live tree**. Observed by this seat at
2026-10-19T09:30:56Z: `git status --porcelain` → ` M reports/round-34/validation.json`;
live digest `1f115eeaab528d52689876e2ef0282b4bf8fcbdc0181f7468c5be39627fb76f8`
against the filed HEAD digest `ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a`.
The rewrite flipped `acceptance_checks_passed` **true → false** and changed the
claim-O leg's census:

```
-      "guarded-refresh": 18,          →        "guarded-refresh": 19,
-      "status": "green"                →        "status": "failed"
+      "failures": ["O1-O5: O2: inventory counts differ: 30 runners,
+                    {'guarded-refresh': 19, 'unguarded-in-place': 11}"]
```

**Mechanism (measured, not inferred).** `reports/round-34/run-validation.py:10`
hardcodes `ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"` and then
`os.chdir(ROOT)` at `:26`. A sibling seat ran that runner from inside a
`git clone` under `.scratch` believing the clone isolated it; because `ROOT` is
absolute, the receipt write at `:534` (`open(out_path, "w")`) landed in the
**live** tree. `ps` captured the writer in the act (§8 M13):

```
1080853 … export REFRESH_RECEIPTS=1 TMPDIR=…/.scratch … for r in 33 34 35; do
        python3 -B reports/round-$r/run-validation.py … done
```

The r33 runner is **not** affected — it uses `ROOT = Path(__file__).resolve().parents[2]`
(`reports/round-33/run-validation.py:23`), which resolves to the clone. Only the
runners with an absolute `ROOT` literal (r34 `:10`, r35 `:9`) escape their copy.
`REFRESH_RECEIPTS=1` was set in that process, which is what permits the guard to
pass a committed-receipt write (`tools/harness/receipt_guard.py:7-8`).

**Why the r34 assertion fires at all.** The census moved because
`reports/round-35/run-validation.py` now exists: the filed r34 receipt recorded
**29** runners with `{"guarded-refresh": 18, "unguarded-in-place": 11}`, and the
live census is **30** with `{"guarded-refresh": 19, "unguarded-in-place": 11}`
(§8 M14). The r34 runner pins its own census as a constant
(`reports/round-34/run-validation.py:209-211`: `expected_counts = {"guarded-refresh": 18, …}`,
`len(runners) != 29`), so adding a round necessarily reddens a re-run of r34.

**This is the filed F-C13-1 class repeating, not a new class.** `LOG.md:3548-3567`
recorded the same shape for `reports/round-{5,6,7}/validation.json` during the
round-33 wave, "restored byte-exact". The round-34 claim O built
`tools/harness/receipt_guard_adoption.py` precisely to instrument it — and that
tool's own docstring (`:6-8`) states the tool "never executes a runner".

**This is an OPEN, REPEATING incident, not a one-off.** Two distinct writers were
captured, and the dirty byte **moved from r34 to r35** between reads:

| read | dirty filed byte | live digest | HEAD digest |
|---|---|---|---|
| 09:30:56Z | `reports/round-34/validation.json` | `1f115eea…` | `ba2fa4dc…` |
| 09:32:14Z | none (r34 back at HEAD) | — | — |
| 09:34:47Z | `reports/round-35/validation.json` | `8a40245dcecf…` | `328e97b3…` |

The second writer's command line is explicit about its intent — it *tries* to
restore before running and leaves the receipt rewritten after:

```
1115469 … cd .scratch/x01-clone && export REFRESH_RECEIPTS=1 TMPDIR=… && \
  for r in 33 34 35; do git checkout -q -- reports/round-$r/validation.json; done; \
  for r in 33 34 35; do out=$(python3 -B reports/round-$r/run-validation.py 2>/tmp/err$r); …; done
```

It runs from `.scratch/x01-clone` and restores with `git checkout --` **before**
the loop, then runs each runner with `REFRESH_RECEIPTS=1`; because those runners
carry an absolute `ROOT` and `os.chdir(ROOT)`, every write lands in the live tree
**after** the restore. r35's diff is a live re-measure: `measured_at_utc`
`06:19:14` → `06:33:23` and the `X1-X3.measurement.manifest`
`"pending-by-construction: …"` note emptied to `{}` — i.e. the runner observed the
round-36 wave's in-flight state and overwrote the filed r35 close record with it.

**This seat did not write either byte.** This seat's only write in this round is
`reports/round-36/scribe/S01-integration-draft.md`; it ran no filed runner except
in a `git archive` copy with `--check` (§8 M9, M10), and it verified digests
rather than restoring anything.

**F-S01-2 — the filed runners' own "filed bytes modified" check is a DEAD CHECK.**
Both runners guard the protected set with a git pathspec that **git does not
expand**:

```
reports/round-34/run-validation.py:228  git("status","--porcelain","--","reports/round-1..33", …)
reports/round-35/run-validation.py:235  git("status","--porcelain","--","reports/round-1..34", …)
```

`round-1..33` is a literal path, not a range, so it matches nothing and the check
always returns zero rows. Measured in a throwaway repo built from
`git archive HEAD` (§8 M22): after appending one byte to
`reports/round-33/validation.json`, `git status --porcelain -- reports` → **1**
row, `-- 'reports/round-33'` → **1** row, `-- 'reports/round-1..33'` → **0** rows.
So a sibling seat can rewrite any filed receipt **in the live tree** and every
filed runner's self-check will still report the protected set clean — which is
exactly the blindness that let both incidents run undetected by the lane's own
instruments. (The regex-based preservation leg at `:268` walks `git ls-tree` and
**is** sound; it is the `git status` scope line that is inert.)

**What the integrator should do with this.** (i) Re-verify **both** receipts
against HEAD in the close pass (`ba2fa4dc…` r34, `328e97b3…` r35) and record the
outcome; if either is dirty, restore it and file the occurrence as a new
append-only row. (ii) Do **not** "fix" the r34 census constant to 30 — that edits
a filed byte and would launder a genuine revision boundary. (iii) Record in the
receipt's `limits` that the r34 census assertion is a **revision-boundary
constant**, not a live invariant. (iv) The round-36 non-goal "no in-tree
round-runner execution" (`claims.json`) was violated at least twice by sibling
seats during the wave; the integrator owns the disposition, this seat only files
the evidence. (v) **The round-36 runner must not copy the dead pathspec.** Use the
`git ls-tree` + `re.match(r"reports/round-(?:[1-9]|[12][0-9]|3[0-5])/…")` form
(the r34 `:268` shape, widened to `3[0-5]`), and additionally assert the two
receipt digests by constant — a digest assertion cannot be defeated by a pathspec
that matches nothing.

---

## §1 — Fleet-report draft (four required sections)

Heading set required by the filed contract (`reports/round-34/run-validation.py:319`,
the four `SECTIONS` strings; round 35 re-used the same tuple at
`reports/round-35/run-validation.py:319`). Reuse the same regex pair for round 36.

### Draft header

```text
# kotodama — round 36 report (2026-10-19)

Regimen 2 (`REGIMEN.md:13`), loop 1, position 4 — the hyper-provider build. Declared
allocation `hyper / deepseek-v4.1-flash`, 32 requested workers, one batched
AgentSwarm (`claims.json` dispatch; `telemetry/dispatch-declared.json`).
**Observed route (named deviation):** hyper returned `402 You're out of credits`
at launch for **all 32 seats with zero started** — `telemetry/availability-attempt-1.json`
records requested 32 / launched 0 / completed 0 / failed 32 (agent-386..agent-417).
Per the declared REGIMEN.md position-4 fallback the batch re-dispatched on
`devin/deepseek-v4-1-flash-high` as attempt 2. Declared baseline `ce103bf`
(`claims.json:8-9`; expands to `ce103bf5885af00023cdc4a174c17602476cdcf8`, §8 M4);
this round's work lands in the same integrating pass that files this report.
Claims D/C/Ca on depth/coverage/calibration (`claims.json`); freshness axis-move
claims stay paused (`claims.json` `freshness_pause_in_force: true`). Seat
accounting: `seat_count: 32` with 32 declared rows and 32 unique `out` paths
(§8 M3) — a 32-seat round, not the 64-seat shape of rounds 33-35. Dispatch
honesty: allocation is declared at `reports/round-36/telemetry/dispatch-declared.json`
(digest-pinned); observed launches/completions/failures are `{{counts or null}}` —
{{owner}} — with the closing snapshot owed once validation.json lands
(`AGENTS.md:32-39`).
```

### Draft — Work performed

```text
- **Depth (claim D):** the declared target was the r25 empty-domain record —
  build register-form content into the D4 lineage. **The claim's `before` was
  measured stale**: the domain is not empty at `ce103bf`. It was closed by round 26
  (`SCORECARD.md:329`: "8 verified register forms (tuum/kit/lom/nees/huum/mees/reek/saam)
  … derivation replay clean (8 derived pairs, 0 violations over 170 records)") and
  extended by rounds 27/28/30. Measured live: `examples/culture-d4/components/04-lexicon.yml:236-243`
  carries the 8 rows; `packet.d4.yml:1053-1170` carries them assembled;
  `:1329` the `registers:` block (QREG-01..08); `:2788` the `register_law:` block
  (RGL-01..05). The leg agrees: `tools/gates/argot-derivation-gate.py
  examples/culture-d4/packet.d4.yml` → `records=187 register_scoped=14
  derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0`,
  exit 0 (§8 M5). Three seats reached this finding independently (K01, D01, X00;
  §11.1). The work that IS owed is the residue the scouts name — the F-6 coverage
  counters, `head2`'s proper domain, the era leg — not a build. {{D-block pointers}}.
- **Coverage (claim C):** the routed r35 timekeeping spare
  (`reports/round-35/cov/C04-timekeeping-spare.md`) landed as one new
  culture-material entry plus README reconciliation. Before: CM 24 / total 211,
  the spare drafted but unlanded (§8 M6). After: CM 25 / total 212; README rev 2.1
  sweep-green (212 rows == 212 files). The spare's gap statement re-verified
  against the current tree: the absence sweep still returns 0 files for every
  instrument term (§8 M7) — the one near-miss is `curfew`, which now hits 1 file
  (`culture-material/fire-fuel-light.md`, landed in r35), a legitimate new
  neighbour rather than a collision. {{C-block pointers}}.
- **Calibration (claim Ca):** the mid-loop recount ledger — every counting
  command filed in rounds 33-35 re-run and dispositioned. This seat's own
  independent reproduction of the r33-35 filed commands is in §3/§8 and agrees
  with the Ca block's ledger on every command it could re-run. {{Ca-block pointers}}.
```

### Draft — Landed changes

```text
- `corpus/knowledge/culture-material/timekeeping-instruments.md` (or the filename
  the C block lands) — one new entry from the routed r35 spare; drafted as a
  fenced block, landed by the integrator.
- `corpus/README.md` — revision 2.1 reconciliation: the `## culture-material/`
  header 24 → 25, the totals line 211 → 212, the counts footer vector
  21/23/25/29/20/94, one new index row in filename order (drafted by the C block,
  applied by the integrator).
- `examples/culture-d4/components/*.yml` and `examples/culture-d4/packet.d4.yml`
  — the claim-D register residue, **only if** the integrator accepts a re-aimed
  claim D (see §9 item 1); as declared, claim D's premise is already satisfied.
- `reports/round-36/validation.json` — this round's acceptance receipt
  (integrator-run; the runner never publishes under `--check`).
- `reports/round-36/telemetry/` — `availability-attempt-1.json` (the hyper 402)
  and `dispatch-declared.json` (filed) plus the observed-dispatch record and the
  closing snapshot owed once validation.json lands.
- Filed bytes: `{{P1 verdict}}`. **Named exception filed, not smoothed:** during
  the wave `reports/round-34/validation.json` was rewritten in the live tree by a
  sibling seat's in-tree runner execution and restored; the incident, its
  mechanism and the live-clean re-verification are recorded in
  `reports/round-36/scribe/S01-integration-draft.md` §0.2 (F-S01-1).
```

### Draft — Before → after measurements

Fill from §3's table (same numbers, prose form). Rule: every after-value names
the fragment that measured it and the counting command; every before-value below
was measured by this seat and is reproducible from §8.

### Draft — SHONEN

```text
All four boxes: {{untouched this round; the r24 verdicts and the r30/r33/r34
re-surveys stand as filed}}. Conditions carried named, none silently closed:
- box 1 (decision tables/errors/checklists/sources): verified-with-conditions;
  the inventory condition closed at r30 (28/28) and re-pinned durable at r34
  (claim C, digest `f9bd07c2…` — re-measured live this round, §8 M11); the
  citation-level conditions 2-4 remain open
  (`reports/round-32/dossier-d11-shonen-boxes.md:44-52,205`).
- box 2 (end-to-end domain task): verified-with-conditions; standing design debts
  named — the 6 D4 garment-form holds (`form_slots` LEX-GAR-01..06, all
  `status: unfilled`, live at `packet.d4.yml:2491-2527`), the register-lexicon
  ceiling RL-3, the `head2` empty proper domain (d11:206; d13:130-132).
- box 3 (cold-run executability): verified-with-conditions; N1/N4/N5/N7 remain
  open as filed (d11:145-150,207).
- box 4 (no bleed / PROVINCE accurate): verified-with-conditions; standing
  readings 3a/3b/3c by design (d11:208).
No promotion decision is taken or implied here; the decision remains
operator-owned (SHONEN.md:10-11).
```

---

## §2 — Integration order and collision notes

1. **Land claim C first** (the corpus entry + `corpus/README.md`), because the C
   legs measure the landed counts and the close legs read the resulting tree.
   Then the Ca ledger, then `run-validation.py`, then telemetry, then the fleet
   report, then SCORECARD/LOG/MANIFEST.
2. **Claim D needs an operator/integrator decision before any D4 byte moves**
   (§9 item 1). If a D4 component edit does land, it is **not** isolated: the
   `D4_COMPONENTS` tuple at `tools/exercise-handoff-e2e.py:157-170` pins
   `01-brief.yml` … `12-provenance.yml`, and the r7 frozen roster
   (`reports/round-34/handoff/declared-in-r7/expected.json#inputs`) holds all 12
   of them (§8 M16) — so editing `04-lexicon.yml` reddens the r7 default chain
   with `E2E-DIGEST`. Adding a **new** component file (e.g. `14-register-forms.yml`)
   is worse: `tools/assemble-culture-d4.py:214-224` walks `COMPONENTS.iterdir()`
   and only requires `>= MINIMUM_COMPONENTS` (12), so a 14th file is accepted,
   merged, and rewrites `packet.d4.yml` — which reddens the r7 chain too
   (independently measured by R03, §11.5).
3. **Collision surface.** `tools/exercise-handoff-e2e.py` is touched only if a D
   or O draft names it — no round-36 seat owns an O claim, so it should stay
   untouched. `corpus/knowledge/**` and `corpus/README.md` are written only by
   the integrator from the C block's fenced drafts. `LOG.md` is integrator-only.
   **No shared file is written by two seats** — verified against the 32 `out`
   paths, which partition into 8 directories (§8 M3).
4. **`corpus/README.md` is NOT in the protected set.** The r34 preservation leg's
   protected **regex** (`reports/round-34/run-validation.py:264-280`) covers
   `reports/round-1..33/**`, `corpus/lessons/*.md` (excluding `README.md`) and
   `tools/gates/frozen/round-*`. Round 36 must widen the round range to `3[0-5]`
   and must **not** add `corpus/knowledge/**` or `corpus/README.md` — they are
   this round's claim-C deliverables. **But the sibling `git status` scope line
   (`:228`, `:235`) must NOT be copied: it is a dead pathspec (§0.2 F-S01-2).**
   Widening the *regex* range is what makes the r34 and r35 freeze bytes
   immovable; widening a literal pathspec does nothing at all.
5. **Two filed-round facts to carry.** (a) `reports/round-35/validation.json` is
   now inside the protected set, so its digest
   (`328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124`, §8 M17)
   must stay put. (b) `reports/round-34/validation.json` is **also** protected and
   was observed dirty during the wave (§0.2) — re-verify at close.
6. **The r34 census constant is a revision boundary, not an invariant** (§0.2):
   do not re-run a filed runner in-tree, and do not edit the r34 constant.

---

## §3 — Before → after table

| claim | axis | before (measured 2026-10-19 by S01, §8) | after required (claims.json) | counting command |
|---|---|---|---|---|
| D | depth | **premise stale**: the register-form domain is NOT empty. 8 register forms `L-55..L-62` delivered at `04-lexicon.yml:236-243`, assembled at `packet.d4.yml:1053-1170`, `registers:` QREG-01..08 at `:1329`, `register_law:` RGL-01..05 at `:2788`; argot leg `derived_pairs=8 violations=0`, exit 0; law leg `law_rows=5 findings=0`, exit 0 (§8 M5) | register-form domain non-empty with verified forms; replay/law/typed legs green; every pin re-frozen as a new row; filed r25-r35 bytes untouched | `python3 -B reports/round-36/run-validation.py` |
| C | coverage | CM 24 / total 211 (`ls` census 21/23/24/29/20/94 = 211); the r35 spare drafted and routed but unlanded — no `corpus/knowledge/culture-material/timekeeping*.md` exists; README rev 2.0, headers `(21)/(23)/(24)/(29)/(20)/(94)`, totals line 211, footer 211 / 21/23/24/29/20/94, sweep green, `readme_sha256 51b966af…` (§8 M6) | CM 25 / total 212; README rev 2.1 sweep-green (212 rows == 212 files); the spare audited (two auditors) before landing | `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md \| wc -l; done`; `python3 -B reports/round-28/readme/sweep.py` |
| Ca | calibration | rounds 33-35 filed their counting commands but no cross-round recount exists; this seat re-ran the live read-only ones and they agree with the filed values (§8 M17-M20) | recount ledger with one row per filed counting command (33-35), each with observed output and disposition; mismatches named with causes, none smoothed | `python3 -B reports/round-36/run-validation.py` |
| all | — | regressions green at this seat's cut: argot leg 27/27 selftest, law leg 45/45, typed pipeline 20/20 legs + 19/19 selftest, assemble-d4 81/81, gate battery `pass 7 / fail 0`, craft 18/18, D2 typed labels 163/163, box1-survey 28/28, c31 audit exit 0 findings 0 (§8 M8, M11) | unchanged or better; zero regressions | §6 `CO9` |

---

## §4 — Telemetry material (draft)

- `telemetry/dispatch-declared.json` (filed): owner = orchestrator (goal-mode
  parent); declared 2026-10-19T09:20:00Z; allocation = `hyper` /
  `deepseek-v4.1-flash` / **32** requested workers / 1 batched AgentSwarm call;
  `fallback` names `devin/deepseek-v4-1-flash-high`; `baseline_commit ce103bf`.
  Durable digests: `claims.json` = `b8d1af8f…` and `targets.json` = `39ddbc72…`.
  **This seat re-verified both against live bytes (§8 M2) — they match.**
  Its `closing_snapshot` field reads `"open-at-seat-close: owed once
  validation.json lands"`.
- `telemetry/availability-attempt-1.json` (filed): the hyper 402. Records
  requested 32 / launched **0** / completed **0** / failed **32**, error
  `402 You're out of credits (hyper.charm.land)`, seat-id range
  `agent-386..agent-417`, and the disposition naming the REGIMEN.md position-4
  fallback to devin as attempt 2. This is the round's availability evidence.
- **Route accounting the integrator must not net.** 32 seats failed at launch on
  hyper (zero started) and the batch re-dispatched on devin. The 32 hyper failures
  must not be netted against the devin completions, and no report sentence may
  say "32 seats on hyper completed". Declared allocation (hyper) and observed
  route (devin) stay separate fields.
- Composition cross-check (this seat's count, §8 M3): **32 seat rows** by claim
  {D 14, C 6, Ca 6, cross 6} and by role {scout 3, planner 1, connector 1,
  executor 12, verifier 4, scribe 6, reviewer 3, critic 2}; 32 unique `out` paths
  across 8 directories. Report the **measured** census.
- Owed at close (`AGENTS.md:32-39`): an **observed-dispatch record** (launches,
  completions, failures, runtime concurrency, actual route = devin; unknown
  counters `null` with owner + reason, never inferred zeroes) and the **closing
  snapshot** that closes `dispatch-declared.json` by path + its SHA-256 at close
  time.
- **Closing-snapshot filename (binding):**
  `reports/round-36/telemetry/availability-close-36.json`, mirroring the landed
  convention (`reports/round-{19,25,26,27,28,33,34,35}/telemetry/availability-close-N.json`;
  schema `kotodama-availability-closing-snapshot-v1`, keys `closes` +
  `closes_sha256` + `closed_fields` + `could_not_recover` + `sources` +
  `owner` + `reason`, as at `reports/round-33/telemetry/availability-close-33.json`).
  Do **not** name it `closing-snapshot.json` — that name exists nowhere in the
  repo and is the F-X16-3 defect the round-33 lane already reproduced. The live
  instrument globs `telemetry/availability-close-*.json` and keys the audit on
  `closes` + `closes_sha256` (`SKILL.md:730-732`). The snapshot must fill the
  devin route the declaration left open, citing `availability-attempt-1.json`'s
  `disposition` — that is the "close what you open" obligation this round created.

---

## §5 — Validator acceptance shape and the four schema traps

Mirror the round-35 receipt key set (`reports/round-35/validation.json`):
`round`, `runner`, `runner_sha256`, `counting_command`, `date`, `measured_at_utc`,
`baseline_revision`, `baseline_expanded`, `claims_declared`, `acceptance_checks_passed`,
`claims` (per-claim `{passed, date, command, failures[], measurement{}}`),
`failures`, `missing_dependencies`, `target_outputs`, `input_sha256`, `limits`.
Behaviour: `--check` prints and never publishes; `--selftest` is dependency-free
positive/negative controls; the default mode guards `reports/round-36/validation.json`
through `tools/harness/receipt_guard.py` (a new file, so the guard passes) and
exits 0 iff `acceptance_checks_passed`.

### Trap 1 — the baseline is declared twice and both tokens are identical

`claims.json` carries `"baseline_commit": "ce103bf"` **and**
`"baseline_expanded": "ce103bf"`; `dispatch-declared.json` carries
`"baseline_commit": "ce103bf"`. Unlike r34/r35 the declared "expansion" is the
**short** token, not the 40-hex id. `CO1` must (a) run
`git rev-parse --verify ce103bf^{commit}`, (b) assert the result equals
`ce103bf5885af00023cdc4a17602476cdcf8`, and (c) record all three tokens
separately in the measurement — the declared `baseline_expanded` field is a
*claim*, not a measurement, and here it is **not** an expansion. Never rewrite
the declared value; the file's digest is pinned at `dispatch-declared.json`
`durable_sources` and verified live (§8 M2).

### Trap 2 — this is a 32-seat round; do not copy the 64-seat constant

`targets.json` declares `seat_count: 32` and the `seats` array has **32** entries
(§8 M3). Round 35's validator asserts `len(seats) == 64`
(`reports/round-35/run-validation.py` `CO4`). Copying that line into round 36
**fails a well-formed round**. Implement `CO4` as `len(seats) == 32` with no
deviation block. Round 34's separate 63-vs-64 deviation also does **not** repeat.

### Trap 3 — the provider is a declared-vs-observed divergence, and it is a *fallback*, not a live-key switch

`claims.json` dispatch declares `provider_lane: "hyper"` /
`model: "deepseek-v4.1-flash"` / `requested_workers: 32` / `batched_calls: 1`, and
`dispatch-declared.json` agrees; the batch actually ran on
`devin/deepseek-v4-1-flash-high`. This is the **REGIMEN.md-declared** fallback
(REGIMEN.md position 4: "hyper / deepseek-v4.1-flash; fallback
devin/deepseek-v4-1-flash-high"), not an undeclared substitution — unlike
round 35, where the deviation was a live-key switch inside one lane.
`AGENTS.md` still forbids conflating requested allocation with observed route.
Implement `CO5` as two separate assertions plus a named deviation: assert the
*declared* allocation exactly (lane `hyper`, model `deepseek-v4.1-flash`, 32
requested workers, 1 batched call), then record the observed route
(`devin/deepseek-v4-1-flash-high`), the 402 attempt record as its evidence, and
the owner (orchestrator) — as a deviation row, never as a leg failure and never
as a silent pass. Assert that the fallback string appears in
`claims.json.dispatch.fallback` **and** in REGIMEN.md, so an undeclared provider
cannot pass by adding a `fallback` key alone. Do **not** edit `claims.json`.

### Trap 4 — the r34 census constant will redden a re-run; that is a revision boundary

If any leg re-runs `reports/round-34/run-validation.py` (or reads its receipt),
it will observe `acceptance_checks_passed: false` with
`O2: inventory counts differ: 30 runners, {'guarded-refresh': 19, …}` — because
the runner census grew by exactly one when round 35 landed (§0.2, §8 M14). A leg
asserting "the r34 receipt says true" passes only against the **filed HEAD
bytes**, never against a re-run. Assert the digest
(`ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a`), not the
verdict. Do not re-run any filed runner in-tree; if a re-run is needed for the Ca
ledger, use a clone with the `ROOT` line re-pointed inside the copy (the Ca02
precedent, §11.6).

---

## §6 — Validation-leg spec (machine-checkable)

Format: `id | claim | command/check | expected | parser hint`. `{{}}` means
"resolve from the landed fragment and pin the path". Every leg below was
requested by this seat's mission: fleet-report material, the leg spec, and the
selftest list.

### §6.1 Coherence / schema legs (cross)

- **CO1** strict-parse `claims.json` and `targets.json` (duplicate JSON keys
  refused, round-34 `strict_json` pattern at `reports/round-34/run-validation.py:47-56`).
  Expect `round == 36` in both; baseline three-way agreement (Trap 1); record the
  short token, the declared "expansion" and the git-resolved expansion separately.
- **CO2** `{c.id: c.axis for c in claims.claims}` ==
  `{"D": "depth", "C": "coverage", "Ca": "calibration"}` and
  `set(claims.axes_in_play) == {"depth", "coverage", "calibration"}` with three
  pairwise-distinct axes (`REGIMEN.md:26-29`; `claims.json`).
- **CO3** `claims.freshness_pause_in_force is True` and `"freshness"` absent from
  `axes_in_play` and from every claim's axis.
- **CO4** seat census (Trap 2): `len(targets.seats) == 32` == `seat_count`; every
  `out` unique and under `reports/round-36/`; non-empty `id`/`role`/`mission`.
  No deviation block. Report the measured count as the measurement.
- **CO5** dispatch shape + provider deviation (Trap 3): declared allocation
  asserted exactly; the declared fallback asserted present in both `claims.json`
  and `REGIMEN.md`; observed route recorded as a named deviation with the 402
  attempt record as evidence and owner = orchestrator.
- **CO6** composition cross-check: role counts == `{scout 3, planner 1,
  connector 1, executor 12, verifier 4, scribe 6, reviewer 3, critic 2}` and
  claim counts == `{D 14, C 6, Ca 6, cross 6}` (measured 2026-10-19, §8 M3).
  Report the counts as the measurement, not as a threshold alone.
- **CO7** lowest-axis rule: the claim set contains `depth` and
  `claims.json.lowest_axis_reasoning` names depth as the least-claimed
  non-paused axis (three prior regimen-2 rounds claimed coverage/calibration;
  depth has one). Assert the *presence* of the depth axis and that no freshness
  axis-move claim exists; do not re-derive the priority ordering.
- **CO8** godspeed lead: **not machine-checkable from durable artifacts** — the
  prompts are not persisted and `AGENTS.md:30-31` forbids private prompt payloads
  in telemetry. Record `could-not-evaluate` with owner = orchestrator and
  `dispatch-declared.json` as the only evidence. Never score this leg as passed
  from absence of evidence.
- **CO9** regression floor: the ten non-mutating tools in §8 M8/M11 all exit 0
  with the counts recorded there. This is the "no axis harmed" leg; it is
  deliberately independent of the claim legs so a bad change shows up as a
  regression rather than as its own verdict.

### §6.2 Claim-C legs (coverage: CM 25 / total 212 + audit parity + README equality)

- **C1 — partition counts.** Run
  `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done`
  and assert the vector is `21/23/25/29/20/94` (sum 212). Assert **per
  partition**, not just the total. Record the before vector
  (`21/23/24/29/20/94`, §8 M6) in the measurement so the delta is visible.
- **C2 — no partition drift outside the one named.** Assert `linguistics == 21`,
  `myth-symbol == 23`, `synthesis == 29`, `verification == 20`,
  `civilizations == 94` exactly. The claim names only culture-material; a change
  anywhere else is a defect even if the total still reads 212.
- **C3 — inventory total.** `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
  → `totals.files == 212`, and every file appears exactly once in `files[]`.
  Record `lines`/`raw_lines`/`marker_occurrences` as the measurement (before:
  `38353 / 991 / 785`, §8 M6) — they must grow, and a *shrink* is a named finding.
- **C4 — README equality on all four count surfaces.** `corpus/README.md` must
  agree with the live census at:
  (a) the section header `## culture-material/ (25)` (before: `:186` reads `(24)`);
  (b) the totals line (before: `:492` reads `Total knowledge entries: 211.`);
  (c) the counts footer (before: `:496` reads `(total 211 files; directory totals 21/23/24/29/20/94)`);
  (d) index-row parity: the number of `^- \`<name>.md\`` rows equals the live
  file count (before: 211 == 211, §8 M6).
  **This four-surface leg is the direct response to the r28 defect**: a sweep that
  checked rows but never read the footer went green over a stale claim
  (`corpus/README.md:19-33`). A leg that checks only the totals line reproduces
  it. Assert the footer vector in its declared order
  (linguistics/myth-symbol/culture-material/synthesis/verification/civilizations)
  and assert the new revision note (2.1) exists at the top of the file.
- **C5 — entry audit parity (two independent auditors).** The one new entry
  passes: frontmatter 4/4 (`source` / `verified-at` / `recheck` / `scope`) or a
  documented 3/4 class; decision record present; gap named in-file; every source
  pointer resolves **or** is marked `to-verify` in-file. The leg reads the two
  auditors' fragments and asserts: both auditors ran, their per-entry verdicts
  cover the entry, and any disagreement between them is filed as a defect rather
  than resolved by the validator. **A green single-auditor result is a failure of
  this leg**, because the claim's threshold is "audited (two auditors)".
- **C6 — zero fabricated sources.** Assert the union of `to-verify` markers across
  the landed entry equals the count the audit fragments report, and that every
  non-`to-verify` citation resolves by `test -e`/grep at HEAD. The leg must not
  accept an empty `to-verify` set as proof of resolution — it must re-resolve the
  pointers itself. Report both counts. The r35 spare carries an unusually large
  `to-verify` set (§11.3) — expect it to survive landing and be reported, not
  zeroed.
- **C7 — the new entry carries no bleed.** Language scan over the new entry's text
  for canon/clearance/closure grant frames outside negations; contested items
  routed to lore-shokunin, never absorbed. Note the r34 scanner walks `ROUND`
  only, so `corpus/knowledge/**` sits **outside** L1's reach (§9 item 5) — this
  leg must scope the assertion to the landed entry explicitly.
- **C8 — the lessons partition is untouched.** `ls corpus/lessons/*.md | wc -l` ==
  33 (measured, §8 M6). A change to the lessons count means the wrong tree was
  written.

### §6.3 Claim-D legs (the register residue, gated on the re-aim decision)

**Read §9 item 1 before implementing any D leg.** The claim's `before` is stale;
the legs below are written so that they are *true and useful* either way.

- **D1 — the stale-premise leg (binding, passes today).** Assert the register-form
  domain is **non-empty**: `python3 -B tools/gates/argot-derivation-gate.py
  examples/culture-d4/packet.d4.yml` → exit 0 with `derived_pairs >= 8` and
  `violations == 0`. This is the leg the claim's own `after_required` asks for
  ("register-form domain non-empty with verified forms … derivation replay clean").
  It is **already green at baseline** (§8 M5) — record that in the measurement,
  because a leg that is green before any work is the honest signature of a stale
  premise.
- **D2 — the law leg.** `python3 -B tools/gates/register-law-gate.py
  examples/culture-d4/packet.d4.yml` → exit 0, `law_rows=5`, `dangling=0`,
  `findings=0` (§8 M5). Also green at baseline.
- **D3 — the typed pipeline.** `python3 -B tools/gates/typed-pipeline-gate.py
  examples/culture-d4/packet.d4.yml` → exit 0, `summary: 20/20 legs passed`, and
  the printed hold set equals the frozen `expected-holds.json`
  (`sha256 e6ae9828d6c8…`, §8 M5). Also green at baseline.
- **D4 — the residue census (the work that IS owed).** Assert the claim's own
  named gaps are present as *named* holds, not silently absent: the six garment
  `form_slots` LEX-GAR-01..06 all `status: unfilled`
  (`examples/culture-d4/packet.d4.yml:2491-2527`, §8 M5), the register-lexicon
  ceiling RL-3, and the `head2` proper-domain gap. Assert the counts and that each
  names an owner. This leg is the honest content of the re-aimed claim.
- **D5 — the r7 freeze read set (load-bearing; do not skip).** Assert the r7
  frozen roster `reports/round-34/handoff/declared-in-r7/expected.json#inputs`
  has **58** members and contains `examples/culture-d4/components/04-lexicon.yml`
  and the other 11 `D4_COMPONENTS` (`tools/exercise-handoff-e2e.py:157-170`), but
  **not** `13-register-law.yml` (§8 M16). Then assert the r7 default chain is
  still green: `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet`
  → exit 0, `packet_sha256 == 45f57132…` == `freeze.txt`. **If any D4 component
  byte moved, this leg fails with `E2E-DIGEST` — and that is the correct
  outcome**, not a bug to be worked around by re-freezing (the round's non-goals
  forbid it).
- **D6 — filed bytes untouched.** The r25-r35 register evidence
  (`reports/round-25/argot/`, `reports/round-26/register/`, `reports/round-27/law/`,
  `reports/round-28/law/`) is byte-identical to baseline; asserted by P1.

### §6.4 Claim-Ca legs (the recount ledger)

- **Ca1 — ledger shape.** The ledger is strict JSON with one row per distinct
  counting command filed in rounds 33-35, each row carrying `source_round`,
  `command`, `filed_result`, `observed_result`, `disposition` ∈
  {`match`, `dispositioned-mismatch`, `could-not-reproduce`}. Rows with
  `could-not-reproduce` carry `owner` and `reason`. Assert row count and that no
  `dispositioned-mismatch` row is missing its named cause.
- **Ca2 — no in-tree runner execution.** The ledger's own evidence must show any
  `run-validation.py` re-run happened in a clone with the `ROOT` line re-pointed
  (the Ca02 precedent, §11.6) or with `--check`. Assert the ledger contains no
  evidence row naming an in-tree execution — this is the leg that would have
  caught the §0.2 incident.
- **Ca3 — the filed commands re-run.** This seat independently re-ran the live
  read-only filed commands; the expected dispositions are in §8 M17-M20. Assert
  the ledger's `observed_result` matches this seat's measurements where the
  command is live-re-runnable, and that the provider-transport rows
  (`AgentSwarm result: …`) are `could-not-reproduce` with owner = orchestrator —
  never inferred zeroes.
- **Ca4 — the r34 revision-boundary row.** The ledger must carry a row for
  `reports/round-34/validation.json` recording that a re-run now reddens the O
  leg (29→30 runners) while the **filed** receipt is unchanged at
  `ba2fa4dc…`. A ledger that smooths this into `match` is defective.
- **Ca5 — receipt consistency.** `validation.json.counting_command ==
  "python3 reports/round-36/run-validation.py"` and `round == 36`.

### §6.5 Cross / close legs

- **P1 — preservation (global).** Reuse the round-34 `protected_snapshot`
  **regex** approach (`reports/round-34/run-validation.py:264-280`) with the round
  range widened to `3[0-5]`: every blob under `reports/round-1..35/**`,
  `tools/gates/frozen/round-*`, and `corpus/lessons/*.md` (excluding
  `corpus/lessons/README.md`) is byte-identical to the baseline commit's tree,
  walked via `git ls-tree` (never via a literal git pathspec — §0.2 F-S01-2).
  **Deliberately excludes `corpus/knowledge/**` and `corpus/README.md`** — this
  round's claim-C deliverables. Run it before and after measurement.
  **Additionally assert the §0.2 incident did not recur, by digest constant:**
  `sha256(reports/round-34/validation.json) ==
  ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a` and
  `sha256(reports/round-35/validation.json) ==
  328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124`.
- **L1 — language.** Run the embedded scanner over every `reports/round-36/**`
  file; allow a hit only in a negation or routed-reference context; require every
  declared seat `out` path to be present in the scan; zero unallowed hits. Carry
  the round-34 two-pass design (`reports/round-34/run-validation.py:283-310`):
  `LANG_TOKENS` flags token presence, `LANG_ALLOW` clears negations, and only
  `LANG_FRAME` grant/completion frames are UNSUPPORTED. Evidence prose naming
  tokens (audit dossiers, "the verified surface", digests) must **not** fire. Two
  adjudications to pre-clear by path: this file and every fragment quoting audit
  tokens inside a fenced spec block, and `claims.json`/`targets.json`/the runner
  itself.
- **X1** fleet report at `../.ufo/reports/round-36/kotodama.md` with all four
  required headings, an ISO date, and a citation of
  `reports/round-36/run-validation.py`. The report lives **outside** this repo, so
  the integrator writes it — seats cannot.
- **X2** MANIFEST: the fleet-root `MANIFEST.json` round-36 entry present, or
  recorded `pending-by-construction` with the reason naming the integrator.
  (Measured: `grep -c '"round": 36' MANIFEST.json` → **0** today, §8 M21.)
- **X3** telemetry: `dispatch-declared.json` SHA-256 recorded; its
  `durable_sources` digests equal the live `claims.json`/`targets.json` digests
  (verified true at this seat's cut, §8 M2); the observed-dispatch record and the
  closing snapshot `availability-close-36.json` exist **or** are reported as owed
  with owner + reason. Never infer missing counters.
- **X4** self-consistency: `round == 36`, `counting_command == "python3
  reports/round-36/run-validation.py"`, `acceptance_checks_passed` true only if
  every leg passed, `limits` non-empty, `missing_dependencies` ⊇ `target_outputs`
  (every owed seat fragment listed). In-flight evidence changes invalidate
  acceptance (re-read digests before writing).

### §6.6 Leg table (machine-readable)

```json
{
  "round": 36,
  "runner": "reports/round-36/run-validation.py",
  "receipt": "reports/round-36/validation.json",
  "baseline_key": "claims.baseline_commit",
  "baseline_declared_token": "ce103bf",
  "baseline_declared_expanded_field": "ce103bf",
  "baseline_expanded": "ce103bf5885af00023cdc4a174c17602476cdcf8",
  "legs": [
    {"id": "CO1", "claim": "cross", "check": "strict json + round==36 + baseline three-way agreement (the declared 'expanded' field is the short token, not an expansion)", "expect": "pass"},
    {"id": "CO2", "claim": "cross", "check": "claim axes D/C/Ca on distinct axes == axes_in_play", "expect": "pass"},
    {"id": "CO3", "claim": "cross", "check": "freshness_pause_in_force true and freshness absent", "expect": "pass"},
    {"id": "CO4", "claim": "cross", "check": "32 seat rows == seat_count 32; unique outs; NO 64- or 63-style carry-over", "expect": "pass"},
    {"id": "CO5", "claim": "cross", "check": "declared allocation hyper / deepseek-v4.1-flash / 32 / 1 batch asserted; declared fallback present in claims.json AND REGIMEN.md; observed route devin recorded as a named deviation", "expect": "pass-with-deviation", "deviation": "declared hyper returned 402 at launch for all 32 seats with zero started (availability-attempt-1.json); REGIMEN.md position-4 declared fallback devin/deepseek-v4-1-flash-high; owner orchestrator"},
    {"id": "CO6", "claim": "cross", "check": "seat role/claim counts == measured census", "expect": "pass", "measured_2026_10_19": {"claims": {"D": 14, "C": 6, "Ca": 6, "cross": 6}, "roles": {"scout": 3, "planner": 1, "connector": 1, "executor": 12, "verifier": 4, "scribe": 6, "reviewer": 3, "critic": 2}}},
    {"id": "CO7", "claim": "cross", "check": "depth axis present; no freshness axis-move claim", "expect": "pass"},
    {"id": "CO8", "claim": "cross", "check": "godspeed lead", "expect": "could-not-evaluate", "owner": "orchestrator", "reason": "prompts not persisted; AGENTS.md:30-31 forbids private prompt payloads"},
    {"id": "CO9", "claim": "cross", "check": "regression floor: the ten tools of §8 M8/M11 exit 0 with the recorded counts", "expect": "pass"},
    {"id": "D1", "claim": "D", "command": "python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml", "expect": "exit 0; derived_pairs >= 8; violations == 0 — ALREADY GREEN at baseline (stale premise)", "severity": "stale-premise signature"},
    {"id": "D2", "claim": "D", "command": "python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml", "expect": "exit 0; law_rows 5; dangling 0; findings 0 — already green"},
    {"id": "D3", "claim": "D", "command": "python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml", "expect": "exit 0; 20/20 legs; hold set == expected-holds.json sha256 e6ae9828d6c8…"},
    {"id": "D4", "claim": "D", "check": "residue census: 6 LEX-GAR-* form_slots unfilled; RL-3 ceiling; head2 gap — each named with an owner", "expect": "pass"},
    {"id": "D5", "claim": "D", "check": "r7 roster 58 members incl. 04-lexicon.yml and the 12 D4_COMPONENTS, excl. 13-register-law.yml; r7 chain exit 0 packet 45f57132…", "expect": "pass", "severity": "load-bearing"},
    {"id": "D6", "claim": "D", "check": "r25-r35 register evidence byte-identical (delegated to P1)", "expect": "pass"},
    {"id": "C1", "claim": "C", "command": "for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done", "expect": "21/23/25/29/20/94 (sum 212), per partition"},
    {"id": "C2", "claim": "C", "check": "linguistics 21, myth-symbol 23, synthesis 29, verification 20, civilizations 94 unchanged", "expect": "pass"},
    {"id": "C3", "claim": "C", "command": "python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "expect": "totals.files == 212; every file once; line/marker totals grew from 38353/991/785"},
    {"id": "C4", "claim": "C", "check": "README equality on all four count surfaces: culture-material header, totals line, counts footer, index-row parity 212==212; plus revision 2.1", "expect": "pass"},
    {"id": "C5", "claim": "C", "check": "the new entry audited by TWO independent auditors; disagreements filed not smoothed", "expect": "pass"},
    {"id": "C6", "claim": "C", "check": "zero fabricated sources; every non-to-verify pointer re-resolved by the leg itself; to-verify census reported (not zeroed)", "expect": "pass"},
    {"id": "C7", "claim": "C", "check": "new entry carries no grant-frame bleed; contested items routed to lore-shokunin", "expect": "pass"},
    {"id": "C8", "claim": "C", "check": "corpus/lessons/*.md count == 33 unchanged", "expect": "pass"},
    {"id": "Ca1", "claim": "Ca", "check": "ledger strict JSON; one row per distinct 33-35 counting command; required fields; could-not-reproduce rows carry owner+reason", "expect": "pass"},
    {"id": "Ca2", "claim": "Ca", "check": "no evidence row names an in-tree run-validation.py execution", "expect": "pass", "severity": "would have caught F-S01-1"},
    {"id": "Ca3", "claim": "Ca", "check": "live read-only filed commands re-run; provider-transport rows could-not-reproduce with owner orchestrator", "expect": "pass"},
    {"id": "Ca4", "claim": "Ca", "check": "a row records the r34 revision boundary (29->30 runners) while the filed receipt stays ba2fa4dc…", "expect": "pass"},
    {"id": "Ca5", "claim": "Ca", "check": "validation.json round 36 and counting_command match", "expect": "pass"},
    {"id": "P1", "claim": "cross", "check": "reports/round-1..35/**, tools/gates/frozen/round-*, corpus/lessons/*.md byte-identical to baseline; no new protected paths; r34 receipt == ba2fa4dc… and r35 == 328e97b3…", "expect": "pass"},
    {"id": "L1", "claim": "cross", "check": "language scan over reports/round-36/**; every declared seat out present in the scan; zero unadjudicated grant-frame hits", "expect": "pass"},
    {"id": "X1", "claim": "cross", "check": "fleet report with 4 headings + date + runner citation", "expect": "pass"},
    {"id": "X2", "claim": "cross", "check": "MANIFEST round-36 entry present or pending-by-construction with reason", "expect": "pass"},
    {"id": "X3", "claim": "cross", "check": "telemetry digests match live; observed record + availability-close-36.json or owed with owner", "expect": "pass"},
    {"id": "X4", "claim": "cross", "check": "validation.json self-consistency + missing_dependencies covers target_outputs", "expect": "pass"}
  ]
}
```

### §6.7 Language and negation posture (binding on every leg)

No leg, fragment, receipt or report in this round asserts promotion, canon,
clearance or closure. Every occurrence of those tokens must be a negation, a
routed reference, or a quoted pattern. The three legitimate shapes, all present
in this file: `no promotion decision is taken` (§1 SHONEN draft), `canon
decisions belong to lore-shokunin` (`PROVINCE.md:20`), and quoted scanner patterns
(§6.5 L1). The r34 scanner's frame rule is the contract: **token presence alone
never fires; only grant/completion frames do.**

---

## §7 — Selftest control list (`--selftest`, dependency-free, synthetic inputs)

Each control is a positive/negative pair the integrator implements with in-memory
fixtures, mirroring `reports/round-34/run-validation.py:439-464` (12 controls) and
`reports/round-35/run-validation.py` (9 controls). Round 36 needs 28, because this
round adds three new assertion surfaces (the stale-premise leg, the revision-boundary
row, the incident re-verification):

1. `claims.json` with `round: 35` → **CO1 fails**;
2. a duplicate JSON key → **strict parse refused**;
3. `baseline_commit` absent or non-resolving → **CO1 fails**;
4. a declared `baseline_expanded` that disagrees with `git rev-parse` → **CO1
   fails** (the declared field is a claim, not evidence — and here it is not even
   an expansion);
5. `targets.json` with 64 seat rows → **CO4 fails** (32 is the measured value —
   the inverse of round 35's control);
6. `targets.json` with 63 seat rows → **CO4 fails** (round 34's deviation must not
   be inherited);
7. a duplicate `out` path across seats → **CO4 fails**;
8. `axes_in_play` containing `freshness` → **CO3 fails**;
9. a fixture with the declared lane `devin` → **CO5 fails** on the
   declared-allocation assertion;
10. a fixture declaring the devin fallback with no attempt record → **CO5 fails**
    on the deviation's evidence requirement;
11. a fixture declaring an *undeclared* provider fallback (a `fallback` key naming
    a lane absent from REGIMEN.md) → **CO5 fails**;
12. a partition vector `21/23/25/29/20/94` → **C1 passes**;
13. a partition vector `21/23/24/29/20/94` (culture-material short) → **C1 fails**,
    naming culture-material;
14. a vector summing to 212 with the +1 in the wrong partition → **C1/C2 fail**
    (per-partition assertion, not total-only);
15. `totals.files == 212` with one file listed twice → **C3 fails**;
16. a README whose totals line reads 212 but whose footer still reads
    `211` / `21/23/24/29/20/94` → **C4 fails** (the r28 defect, reproduced as a
    control — this is the single most important control in the set);
17. a README whose section header still reads `## culture-material/ (24)` →
    **C4 fails**;
18. a README with 211 index rows against 212 files → **C4 fails**;
19. one new entry with no decision record → **C5 fails**;
20. a register-form domain reported EMPTY → **D1 fails** (the stale-premise
    direction: a leg that reported empty would be reading a summary, not the tree);
21. a `form_slots` fixture with LEX-GAR-01 filled → **D4 fails** (the residue
    count is asserted, so a silent fill must show);
22. an r7 roster fixture lacking `04-lexicon.yml` → **D5 fails**;
23. a protected file with one mutated byte → **P1 fails**, naming the path;
24. an r34 receipt fixture with a digest other than `ba2fa4dc…` → **P1 fails**
    (the F-S01-1 re-verification control);
25. a round-36 fragment introducing a promotion token outside a negation → **L1
    fails**; and `no promotion decision is taken here` → **L1 passes**;
26. a fleet report with 3 of the 4 headings → **X1 fails**;
27. a fixture whose protected-set probe uses a literal range pathspec
    (`reports/round-1..35`) with a mutated filed receipt present → **P1 fails**,
    because P1 must catch it (F-S01-2: a range pathspec matches nothing, so a leg
    built on one would pass a dirty tree);
28. a fixture whose `reports/round-34/validation.json` digest differs from
    `ba2fa4dc…` → **P1 fails** (the digest-constant control that cannot be
    defeated by a pathspec).

### §7b — The revision-boundary control (owned by the leg, not a tool)

This is not a control *inside* a tool; it is a control the integrator must
implement in the runner, because it is the one thing about this round that is
easy to get wrong:

- **the census-boundary control:** a fixture whose runner census is 30 with
  `{"guarded-refresh": 19, "unguarded-in-place": 11}` must be reported as a
  **revision boundary**, not as a failure of the filed r34 receipt. The control's
  assertion is that the leg reads the r34 receipt's **digest**, never its
  re-computed verdict. A leg that re-runs r34 and asserts its verdict passes only
  on the filed bytes and fails on the live tree — which is exactly the
  `KeyError`-vs-`E2E-READSET` trap of round 35 (Trap 4 there) in a new dress.

---

## §8 — Measurements taken by this seat (2026-10-19, round-36 tree)

- **M1** `find reports/round-36 -type f | wc -l` → **26** at this seat's last
  read: `claims.json`, `targets.json`, `telemetry/{availability-attempt-1,dispatch-declared}.json`,
  and 22 landed seat fragments (K01, K02, P01, X00, X02, D01, D02, D03, D05, D06,
  D09, D10, C01, C02, C03, C04, C05, R01, R02, R03, Ca02, Ca05, S02). Ten seat
  outputs were still absent (§10). `reports/round-36/run-validation.py` and
  `validation.json` do not exist.
- **M2** `sha256sum reports/round-36/claims.json reports/round-36/targets.json` →
  `b8d1af8fd1fb3814e707e24965a6bd404e83158ae26d48d852118d7abec470b8`,
  `39ddbc72345d15bc9ec3aa272e161b9e9c7ce652301abca3f55a9c3e28c343d8`. Both equal
  the digests declared in `telemetry/dispatch-declared.json` `durable_sources` —
  **verified live**.
- **M3** seat census from `targets.json` (JSON parse) → `seat_count` field **32**,
  **32 rows**, 32 unique `out` paths, 0 duplicates. Claims {D 14, C 6, Ca 6,
  cross 6}; roles {scout 3, planner 1, connector 1, executor 12, verifier 4,
  scribe 6, reviewer 3, critic 2}. Directories {scout 3, plan 1, cross 3, depth 10,
  cov 5, calib 5, review 3, scribe 2}. Ids: K01-K03, P01, X00, D01-D10, C01-C05,
  Ca01-Ca05, R01-R03, X01-X02, S01-S02.
- **M4** `git rev-parse HEAD` → `ce103bf5885af00023cdc4a174c17602476cdcf8`;
  `git rev-parse --verify ce103bf^{commit}` → the same. `claims.json`
  `baseline_commit` = `"ce103bf"` and `baseline_expanded` = `"ce103bf"` (the
  declared "expansion" is the short token); `dispatch-declared.json`
  `baseline_commit` = `"ce103bf"`. Three tokens, two distinct values, one resolved
  full id.
- **M5** register-domain census at `ce103bf`:
  `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml`
  → `coverage: … records=187 register_scoped=14 derived_pairs=8 claimed_chains=8
  borrow_pairs=6 violations=0 rule_holds=0`, exit 0.
  `python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml`
  → `law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3
  force_failures=0 consequence_failures=0 dangling=0 findings=0`, exit 0.
  `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`
  → `TYPED-PIPELINE: exit 0`, `summary: 20/20 legs passed`, projection
  `c23b0ab532cf`, expected `e6ae9828d6c8`, 12 `D2L-FORM-UNRESOLVED` holds for
  GAR-01..06 / LEX-GAR-01..06. Component rows:
  `examples/culture-d4/components/04-lexicon.yml:236-243` (L-56 kit, L-57 lom,
  L-55 tuum, L-58 nees, L-59 huum, L-60 mees, L-61 reek, L-62 saam; each
  `register: stamp`, `construction: STAMP-REVERSE`/`STAMP-LENGTHEN`,
  `derived_from`, `derivation`, `doublet_of`). Packet: `registers:` at `:1329`
  (QREG-01..08), `register_law:` at `:2788` (RGL-01..05), `form_slots:` at
  `:2491-2527` (LEX-GAR-01..06 all `status: unfilled`). A packet-block census
  counts 20 records carrying `register: "stamp"` (8 lexicon + 7 QREG + 5 RGL) and
  8 with `derived_from`. Digests:
  `packet.d4.yml aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`,
  `packet.d4.typed.yml d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182`,
  `04-lexicon.yml ed7093d6b92111c2300e7c04b9100f9e57f6d5802101b69335f9fe138858755d`,
  `assemble-culture-d4.py 943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2`.
- **M6** partition census
  `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done`
  → `21 / 23 / 24 / 29 / 20 / 94` = **211**; `ls corpus/knowledge/*/*.md | wc -l` →
  211; `ls corpus/lessons/*.md | wc -l` → **33**. Inventory:
  `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
  → schema `kotodama-source-audit-inventory/1`, `read_only true`,
  `deterministic true`, `totals.files 211`, `files_with_marker 145`, `lines 38353`,
  `raw_lines 991`, `raw_occurrences 1074`, `marker_occurrences 785`,
  `class_totals {substantive-flag-candidate 668, policy-use-mention 115,
  needs-review 293}`, `skipped []`. README parity by python over
  `corpus/README.md`: index rows **211**, live files **211**, rows-not-files `[]`,
  files-not-rows `[]`; headers `## linguistics/ (21)` at `:136`,
  `## myth-symbol/ (23)` at `:160`, `## culture-material/ (24)` at `:186`,
  `## synthesis/ (29)` at `:213`, `## verification/ (20)` at `:245`,
  `## civilizations/ (94)` at `:268`; totals line at `:492`
  (`Total knowledge entries: 211.`); counts footer at `:494-496`
  (`(total 211 files; directory totals 21/23/24/29/20/94)`); revision 2.0 at `:3`.
  `python3 -B reports/round-28/readme/sweep.py` → exit 0, `footer_ok True`,
  `header_drift {}`, `totals_ok True`, `total_rows 211`, `total_files 211`,
  `topic_mismatch []`, `readme_sha256 51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`.
  No `corpus/knowledge/culture-material/timekeeping*.md` exists.
- **M7** the r35 spare's absence sweep re-run at `ce103bf` over
  `corpus/knowledge/*/*.md` for the instrument vocabulary →
  `water clock 0, clepsydra 0, gnomon 0, sundial 0, escapement 0, pendulum 0,
  hourglass 0, "incense clock" 0, "bell tower" 0, "canonical hour" 0,
  clockmaker 0, muwaqqit 0, wadokei 0, shichen 0`; **`curfew 1`** (a single hit,
  `corpus/knowledge/culture-material/fire-fuel-light.md`, landed in round 35 —
  a new neighbour, not the timekeeping entry). `clock` hits 10 culture-material
  files, none of them the instrument entry.
- **M8** regression floor (all exit 0): `tools/gates/argot-derivation-gate.py
  --selftest` → `27/27`; `tools/gates/register-law-gate.py --selftest` → `45/45`;
  `tools/gates/typed-pipeline-gate.py --selftest` → `19/19`; `tools/assemble-culture-d4.py
  --selftest` → `81/81`; `tools/check-gate-battery.py` → `battery_exit 0, pass 7,
  fail 0, unevaluable 0`, `preserved true`, 33 files hashed, 0 modified;
  `tools/check-craft-exercise.py --selftest` → `SELFTEST OK 10/10`, `CLI-SELFTEST
  OK 18/18`; `tools/d2-typed-labels.py --selftest` → `163/163`;
  `tools/harness/packet_uncertainty.py --selftest` → `19 checks passed`;
  `tools/assemble-culture-d4.py --check` → `byte-identical deterministic assembly`;
  `tools/assemble-d4-typed.py --check` → `byte-identical deterministic typed packet`.
- **M9** the two filed runners this seat needed, run with `--check` **inside a
  `git archive HEAD` copy** at `.scratch/s01-iso`:
  `reports/round-35/run-validation.py --check` → exit 0,
  `acceptance_checks_passed` true, `failures []`,
  `input_sha256` covering 7 files (including
  `run-validation.py 4ed1ae59386acb8fa17e33dd4d6eba9d7a40581b85f45a33f104529e924bede0`
  and `availability-close-35.json e51ba5e0…`), `missing_dependencies []`,
  `target_outputs []`. `tools/exercise-handoff-e2e.py --profile v3 --quiet
  --baseline reports/round-30/handoff/declared-in-r6/expected.json` → **exit 1**
  with the named diagnostic:
  `handoff-v3: E2E-READSET: 1 read-set member(s) named by the frozen baseline are
  not in the live read set: reports/round-20/handoff/claims-map.md — the baseline
  row is superseded (re-point or re-freeze it)`, and **no** traceback. The r35
  hardening is therefore confirmed live from a clean copy.
- **M10** the r6 replay refusal and the r7 default chain, both in the isolated
  copy: r6 → exit 1 with the `E2E-READSET` line above; r7 default →
  exit 0, `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105
  claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed
  packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`.
- **M11** `python3 -B reports/round-30/craft/box1-survey.py` → `named 28`,
  `resolvable 28`, `unnamed_in_skill []`, `skill_sha256
  f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` — box 1's
  evidence is current at the r34 digest. `python3 -B reports/round-25/audit/c31-lessons-index-audit.py`
  → exit 0, `findings: 0`; `--selftest` → `SELFTEST OK: 28/28`. `python3 -B
  tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md`
  → `INFO scan: fields=16/16 glossary-entries=20 findings=0`, exit 0.
- **M12** `ls ../.ufo/reports/round-36` → **No such file or directory**;
  `../.ufo/reports/round-35/kotodama.md` exists (the r35 precedent). The lane
  repo's own `.ufo/reports/` is empty — the fleet report belongs at the fleet root.
- **M13** the F-S01-1 incident evidence, captured to
  `.scratch/s01-ev/incident-r34-snapshot.txt` at 2026-10-19T09:32:14Z. `ps` rows
  include the writer:
  `1080853 … export REFRESH_RECEIPTS=1 TMPDIR=…/.scratch … for r in 33 34 35; do
  python3 -B reports/round-$r/run-validation.py …` and its child
  `1085369 python3 -B reports/round-35/run-validation.py`. Also observed:
  `1079801 python3 -B reports/round-35/run-validation.py --check`,
  `1082394 python3 -B reports/round-35/run-validation.py --check` (from
  `.scratch/ca01`), and two `unshare -rm --propagation private bash -c "mount --bind
  … .scratch/ca03/$n $LIVE …"` probes (a bind-mount isolation attempt). The
  `.git/index` mtime moved at `06:31:18` (the `git clone` at `1080853`).
- **M14** the census delta that makes the r34 leg red:
  `ls reports/round-*/run-validation.py | wc -l` → **30**;
  `tools/harness/receipt_guard_adoption.py --json` → `runner_count 30`,
  `class_counts {"guarded-refresh": 19, "unguarded-in-place": 11}`,
  `census_complete true`, `findings` unchanged, 30 runner rows (r5-r35).
  The filed r34 receipt records `{"guarded-refresh": 18, "unguarded-in-place": 11}`
  and the r34 runner pins `expected_counts = {"guarded-refresh": 18, …}` with
  `len(runners) != 29` (`reports/round-34/run-validation.py:209-211`).
- **M15** the incident's live state at this seat's finish:
  `sha256sum reports/round-34/validation.json` →
  `ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a` ==
  `git show HEAD:reports/round-34/validation.json | sha256sum`; the mid-incident
  live value `1f115eea…` was saved to
  `.scratch/incident-r34-validation-modified.json`. A sweep of **every** filed
  receipt (`for f in $(git ls-files 'reports/round-*/validation.json'); do live vs
  HEAD; done`) is the sound instrument here: at the r34 read it found **no other
  drift** (r33 `93b28f3635cc…`, r35 `328e97b3…`, both == HEAD); at the second read
  it found **r35 drifted** to `8a40245dcecf…` while r34 had returned to
  `ba2fa4dc…`. **This seat's earlier "protected roots → 0 rows" reading was taken
  with a broken pathspec and is retracted — see M22.** The honest statement is:
  the per-file digest sweep (which does not use a pathspec) is authoritative, and
  it showed the dirty byte moving r34 → r35 during the wave.
- **M22 (RETRACTION + F-S01-2) — `git status -- reports/round-1..N` is a DEAD
  CHECK.** `git status --porcelain -uall -- 'reports/round-1..35'` returns **0
  rows** even when a filed receipt inside that range is modified, because git
  treats `round-1..35` as a **literal path**, not a range (it has no glob
  metacharacter and no `:(glob)` magic). Controlled reproduction in a throwaway
  repo built from `git archive HEAD` (`.scratch/s01-pathspec`):

  ```
  $ printf '\n' >> reports/round-33/validation.json      # mutate one filed byte
  $ git status --porcelain -- reports                   → 1 row
  $ git status --porcelain -- 'reports/round-33'        → 1 row
  $ git status --porcelain -- 'reports/round-1..33'     → 0 rows   ← the dead check
  $ git status --porcelain -- 'reports/round-*'         → 33 rows  (glob works)
  ```

  Both filed runners use the dead form —
  `reports/round-34/run-validation.py:228` `git("status","--porcelain","--","reports/round-1..33", …)`
  and `reports/round-35/run-validation.py:235` `… "reports/round-1..34" …` — so
  their own "filed bytes modified" leg can never fire on a rewritten receipt.
  Their regex-based preservation leg (`:268`) walks `git ls-tree` and **is**
  sound; only the `git status` scope line is inert. The same inert scope line is
  what produced this seat's retracted M15 sentence.
- **M23** the round-36 runner must therefore assert the protected set two ways:
  (a) the `git ls-tree` + `re.match(r"reports/round-(?:[1-9]|[12][0-9]|3[0-5])/|corpus/lessons/(?!README)|tools/gates/frozen/round-", p)`
  walk (the r34 `:268` shape, range widened to `3[0-5]`), and (b) **digest
  constants** for `reports/round-34/validation.json` (`ba2fa4dc…`) and
  `reports/round-35/validation.json` (`328e97b3…`). A digest assertion cannot be
  defeated by a pathspec that matches nothing.
- **M16** the r7 freeze read set:
  `python3 -c "import json; d=json.load(open('reports/round-34/handoff/declared-in-r7/expected.json'))['inputs']; print(len(d), '13-register-law.yml' in d)"`
  → `58 False`. The `D4_COMPONENTS` tuple at `tools/exercise-handoff-e2e.py:157-170`
  names `01-brief.yml` … `12-provenance.yml`. r7 pins: `packet.md
  45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`, `twin.json
  0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599`,
  `claims-map.md d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c`,
  `expected.json bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55`,
  `freeze.txt 3969954bd817f5ab00137c018c82d6642fa15ac8dedc856ff1b761c9716c1223`,
  `run.log ffae4ecdcf2558693e9ace21e918572e84d6be6607a5b8a5284805ab7e11136c`.
  r6 pins: `expected.json ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0`,
  `freeze.txt 6fe70c0c2b3a03ee82181a4906dc9670f73424c54efddec8fc632d213cca5d59`,
  `packet.md 6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb`,
  `run.log b5ee33510af0297e162e24bcdcf4aea563cbf7f3d112faf85720587479e3ed47`,
  `twin.json 6633443d70ce44ed2bb43ab58aa60a1c98e4bbc79b2f577a63181c89dc16fd4e`.
- **M17** the round-35 filed receipt digest:
  `328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124` == HEAD.
  Round-33 receipt `93b28f3635cc11765dd5c4be00e7b8c31ed95dad2f23ce6ec9846684b1b51d9f`
  == HEAD.
- **M18** the r35 runner's own `--selftest` (in-tree, dependency-free, writes
  nothing) → `ok true`, `passed_controls 9`, `total_controls 9`, exit 0.
  r34 `--selftest` → `12/12`, exit 0. r33 `--selftest` → `16/16`, exit 0. These
  are the three filed runners whose **selftest** mode is dependency-free and
  non-writing; their default modes must never run in-tree.
- **M19** the r33 filed counting commands re-run live:
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 0,
  `findings: 0`; `--selftest` → `SELFTEST OK: 28/28`; `test -s
  reports/round-33/op/O05-falsifier-disposition.md` → present and non-empty.
  All three **match** the r33 filing.
- **M20** the r34 filed counting commands re-run live:
  `tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md`
  → exit 0, `fields=16/16 glossary-entries=20 findings=0`; `tools/exercise-handoff-e2e.py
  --profile v3 --quiet` → exit 0, packet `45f57132…`; `tools/harness/receipt_guard_adoption.py
  --selftest` → `selftest_passed true`; `--json` → `census_complete true`. The
  runner row itself is the **revision-boundary mismatch** of M14 (29→30), not a
  filing error. `reports/round-30/craft/box1-survey.py` → 28/28 at `f9bd07c2…`.
  The r35 filed commands are in M6/M8/M9/M10/M11 and all **match** except the
  provider-transport rows, which are `could-not-reproduce` by construction.
- **M21** `grep -c '"round": 36' MANIFEST.json` → **0**; the fleet-root
  `MANIFEST.json` has 250 round rows, the last kotodama rows being rounds 33/34/35
  (`lane_rounds.kotodama` 33/34/35, all `admitted: true`). The round-36 row is
  integrator-owed. `PROVINCE.md` last touched by `c53782a`.

Honest limits: every after-value in §3 is a requirement from `claims.json`, not an
observation — the C entry and README revision 2.1 do not exist at this seat's cut.
§6 is a design the integrator implements and self-tests; this seat executed no
part of `run-validation.py`. §0.2 is an observation about a **sibling seat's**
in-tree execution, captured from `ps` and digests, not a claim about intent. This
seat wrote exactly one byte-path: `reports/round-36/scribe/S01-integration-draft.md`.

---

## §9 — Declaration defects and errata for the integrator

1. **Claim D's `before` is stale — the domain is not empty, and the claim as
   worded is already satisfied in substance.** `claims.json` claim D declares
   `before: "Register-form domain empty (reports/round-25/argot/ + SCORECARD r25
   row); register law/strata exist but the form class has no instances"`. That is
   r25's measurement (`SCORECARD.md:312`, worktree `f74fc940…`) and it was closed
   by round 26 (`SCORECARD.md:329`: "8 verified register forms … derivation replay
   clean (8 derived pairs, 0 violations over 170 records)") and extended by
   rounds 27/28/30. Measured at `ce103bf`: `derived_pairs=8 violations=0` exit 0
   (§8 M5). Three seats independently reached this finding (K01, D01, X00;
   §11.1). **This is not a leg failure and not a claim failure** — it is a
   declaration defect the integrator must adjudicate: either (a) re-aim claim D
   onto the genuine residue the scouts name (the F-6 coverage counters, `head2`'s
   proper domain, the era leg) and record the re-aim in the LOG entry, or (b) rule
   claim D satisfied-by-baseline and record it as such with the evidence. Do
   **not** silently re-run the r25 build. Do **not** edit `claims.json` (its digest
   is pinned in `dispatch-declared.json` `durable_sources` and verified live,
   §8 M2).
2. **Claim D's counting command cannot observe its own threshold.**
   `claims.json` claim D's only `counting_commands` entry is
   `python3 -B reports/round-36/run-validation.py`, and its threshold reads
   "forms verified by two independent seats; replay/law/typed legs green". The
   three legs named are `tools/gates/argot-derivation-gate.py`,
   `tools/gates/register-law-gate.py` and `tools/gates/typed-pipeline-gate.py` —
   none of which the round runner command names. The runner must implement the
   legs (§6.3) and cite the three tool commands in the receipt's measurement, or
   the threshold is unobservable. This is the same shape as round 35's §9 item 6.
3. **The dispatch declares a provider that returned 402 for every seat, and the
   fallback is REGIMEN-declared — say so plainly.** `claims.json` and
   `dispatch-declared.json` both declare `hyper / deepseek-v4.1-flash`;
   `availability-attempt-1.json` records **0 launched, 0 completed, 32 failed**
   with `402 You're out of credits`. The fallback to
   `devin/deepseek-v4-1-flash-high` is declared in REGIMEN.md position 4, so it
   is a permitted deviation — but the report must not present it as the declared
   route. Assert the fallback string in **both** `claims.json` and REGIMEN.md
   (§6.1 CO5), so an undeclared provider cannot pass by adding a `fallback` key.
4. **`claims.json` declares `baseline_expanded` as the short token.** Both
   `baseline_commit` and `baseline_expanded` read `"ce103bf"`. A leg that treats
   the second field as a 40-hex id (as r35's did) will fail a well-formed round.
   Resolve the full id by `git rev-parse --verify` and record all three tokens
   (Trap 1). Do not "correct" the declared field — it is digest-pinned.
5. **The L1 language scanner does not cover `corpus/knowledge/**`.** The r34
   scanner walks `ROUND` (`reports/round-34/run-validation.py:297`). The new
   claim-C entry containing canon-boundary prose therefore sits **outside** L1's
   reach, while the audit fragments that quote it sit inside. The integrator must
   either extend the walk to the landed entry path (preferred — the claim requires
   "no bleed" on the new entry) or add the C7 leg scoped to it, and must state
   which in the receipt's `limits`. A green L1 that never read the new entry is a
   false assurance. (Round 35's §9 item 5 filed the same gap; it is unfixed.)
6. **A filed byte was rewritten in-tree during this wave — twice, and the incident
   is still open (F-S01-1, §0.2).** The round's own non-goals list "no filed byte
   rewrites" and "no in-tree round-runner execution"; both were violated by
   sibling seats running filed runners from inside a clone, because those runners
   carry an absolute `ROOT` literal (r34 `:10`, r35 `:9`) and `os.chdir(ROOT)`
   defeats the copy. `REFRESH_RECEIPTS=1` was set in the writing processes, which
   is what let the guard pass. **The dirty byte moved from r34 (`1f115eea…`) to
   r35 (`8a40245dcecf…`) between reads**, and the second writer restores with
   `git checkout --` *before* its loop, so its writes land after the restore. The
   integrator must (a) re-verify **both** receipts against HEAD at close
   (`ba2fa4dc…` r34, `328e97b3…` r35), (b) file the incident as a new append-only
   row with this evidence, and (c) add the Ca2 leg so the ledger proves no in-tree
   runner execution. **Do not** edit the r34 runner's census constant to 30 —
   that edits a filed byte and launders a revision boundary.
6b. **F-S01-2 — the filed runners' own filed-byte check is dead, and the round-36
   runner must not copy it (§0.2).** `reports/round-34/run-validation.py:228` and
   `reports/round-35/run-validation.py:235` scope their `git status` guard with a
   literal `"reports/round-1..33"` / `"reports/round-1..34"` pathspec, which git
   treats as a **path that matches nothing** — so a rewritten filed receipt never
   trips their own check (reproduced in §8 M22: mutate a filed byte, then
   `-- reports` → 1 row vs `-- 'reports/round-1..33'` → 0 rows). Use the
   `git ls-tree` + regex walk (`:268` shape, range `3[0-5]`) **and** digest
   constants for the r34/r35 receipts. This seat's own first reading of the
   protected set used the same dead pathspec and has been retracted (§8 M15/M22).
7. **The r34 O-leg census is a revision boundary, not an invariant.** Any re-run
   of `reports/round-34/run-validation.py` now reports
   `acceptance_checks_passed: false` because the runner census grew 29 → 30 when
   round 35 landed (§8 M14). Legs must read the filed r34 receipt's **digest**
   (`ba2fa4dc…`), never a re-computed verdict (Trap 4). The same applies to r35's
   `--check` output, which is stable (§8 M9).
8. **`reports/round-36/` may hold fewer than 32 fragments at close.** Four declared
   outputs were still absent at this seat's last read (§10). The receipt's
   `missing_dependencies` must list them exactly, and `target_outputs` must be a
   subset — an empty `missing_dependencies` over an incomplete wave is the
   false-green this leg exists to catch.

---

## §10 — Owed

Declared seat outputs **absent** at this seat's final read
(`find reports/round-36 -type f` → **34** files; **30 of 32** seat outputs
landed):

- `calib/Ca01-recount-33-34.md`
- `cross/X01-trades.md`

(At earlier reads of the same still-dispatching wave the absent set was larger —
`depth/D04-repin.md`, `depth/D07-verify.md`, `depth/D08-verify-repin.md`,
`calib/Ca03-ledger-draft.md`, `calib/Ca04-verify.md` and
`scout/K03-recount-scout.md` were also missing. Recompute with §10.1 rather than
trusting any list, including this one.)

Beyond the seat fragments:

- the one new corpus entry under `corpus/knowledge/culture-material/` (claim C's
  deliverable) and the `corpus/README.md` revision 2.1 reconciliation — drafted by
  the C block, applied by the integrator;
- the claim-D residue content, **only if** the integrator accepts a re-aimed
  claim D (§9 item 1);
- `reports/round-36/run-validation.py` and `reports/round-36/validation.json`
  (integrator-authored; this seat executed no part of either);
- `reports/round-36/telemetry/observed-dispatch.json` and the closing snapshot
  `reports/round-36/telemetry/availability-close-36.json` (§4);
- `../.ufo/reports/round-36/kotodama.md` (the four-section report this draft
  supplies), the fleet-root `MANIFEST.json` round-36 entry, `SCORECARD.md`, and
  the append-only `LOG.md` entry — integrator-only writes;
- the F-S01-1/F-S01-2 incident rows (§0.2, §9 items 6 and 6b).

**Still open at this seat's final read:** `reports/round-35/validation.json` was
**still dirty** — live `8a40245dcecf…` against filed `328e97b3…` — while
`reports/round-34/validation.json` had returned to `ba2fa4dc…`. The integrator
must restore the r35 byte (or rule the rewrite admissible and file it) before the
r35 receipt can be treated as filed evidence, and must re-verify both at close.

### §10.1 — Recompute commands (do not trust the snapshot list)

```bash
python3 -c "import json,os;t=json.load(open('reports/round-36/targets.json'));print([s['out'] for s in t['seats'] if not os.path.isfile('reports/round-36/'+s['out'])])"
find reports/round-36 -type f | wc -l
git status --porcelain=v1 -uall -- reports corpus/lessons corpus/knowledge tools/gates/frozen | wc -l
# AUTHORITATIVE filed-byte check: per-file digest vs HEAD. Never use a literal
# range pathspec like 'reports/round-1..35' — git does not expand it (F-S01-2).
for f in $(git ls-files 'reports/round-*/validation.json'); do L=$(sha256sum "$f" | cut -d' ' -f1); H=$(git show "HEAD:$f" | sha256sum | cut -d' ' -f1); [ "$L" != "$H" ] && echo "DRIFT $f"; done
for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
```

---

## §11 — Landed-fragment cross-check (addendum, same wave)

Read by this seat after §1-§10 were written. The wave was still dispatching, so
every list here is a point-in-time snapshot with its command (§10.1).

**Dependency supersession.** At this seat's first cut `reports/round-36/` held
four files; at this addendum's read it holds **26** (§8 M1). The fragments this
dossier's legs depend on have landed: `scout/K01` (the register scout),
`depth/D01`/`D03` (the design and the isolated verification), `plan/P01`,
`cross/X00` (the connector), `review/R03` (the cross review), and
`calib/Ca02` (the r35 recount). What each changed in this draft:

**§11.1 — Claim D's stale premise is confirmed by three independent seats.** K01
(`scout/K01-register-scout.md:11-16`) states it in one line: the r25 record "was
true at the r25 worktree (`f74fc940…`) and is **false at the round-36 baseline
`ce103bf`**"; D01 (`depth/D01-design.md` §0) reaches the same conclusion with the
landing commits (`git log -S "register: stamp"` → `4f09c99` round-26, `11df1fd`
round-30); X00 (`cross/X00-connector.md` §0) calls it "a **premise collision**"
and tabulates the same six surfaces this seat measured (§8 M5). K01 adds the
decomposition this seat's census needed: `register_scoped=14` = **8**
`derived_pairs` (the stamp forms) + **6** `borrow_pairs` (the loan layer
`L-49..L-54`, whose layer carries a register) — and it warns that r26's own
review (`reports/round-26/argot/D24-forecast-closure.md:88-92`) named
`register_scoped=6` as the **loan layer**, so reading it as the register domain is
the false-closure trap. K01 also names the genuine residue: the F-6 coverage
counters, `head2`'s empty proper domain, and the era leg (E-6/E-7).

**§11.2 — Claim D is not a build; D01 and D03 price the residue.** D01 designs
the surface that is genuinely open and D03 (`depth/D03-isolated-verify.md`)
executes the isolated apply-and-verify in **five** `git archive` copies
(`iso`, `iso-base` as an untouched causality control, `iso-d01`, `iso-p01`,
`iso-d02`) — the correct isolation pattern, and the one the §0.2 writer did not
use. D03 also reproduces a hazard this seat's D5 leg must carry: D02's proposed
component 14 and D01's Draft 1 **double-grade** the same surface when both are
applied (§5b.2 of D03). P01 recommends "Surface A + B-1 only" — the `doublets`
block *is* the forward index, no per-record edit, no contract change — and prices
B-2 (`register_form` on base records) as a contract amendment with a larger pin
cascade, "Recorded, not recommended".

**§11.3 — Claim C: the spare's `to-verify` set is large and must survive.** K02
(`scout/K02-timekeeping-scout.md`) re-verified the spare against the current tree.
This seat's independent sweep (§8 M7) agrees: 14 instrument terms → 0 files, with
`curfew` the single new near-miss (`fire-fuel-light.md`, landed r35). The C6 leg
must therefore report the landed entry's `to-verify` census rather than expect it
to be small — the r35 spare carries an unusually long list of unresolved page-level
checks (it was written with no network access, `cov/C04-timekeeping-spare.md`).

**§11.4 — Claim Ca: the recount is being done the right way, and the ledger row
this seat files is a real one.** `calib/Ca02-recount-35.md` re-ran the r35 runner
in a **local clone with the `ROOT` line re-pointed inside the copy** and with
`--check` — explicitly because "`reports/round-35/run-validation.py` hardcodes the
live tree … so an `git archive` copy of it still writes to the live tree"
(`Ca02:14-18`). That is the correct protocol and the direct answer to §0.2. Its
12-row table dispositions the r35 filed commands, including the two
`could-not-reproduce` provider-transport rows with owner = orchestrator — the
honest treatment. Ca02 also records that the v3 selftest's **machine** count is 44
while the header prose says "43 controls", matching the r35 S04 §11.8 note.

**§11.5 — R03 independently proves the r7 read set is load-bearing.** R03
(`review/R03-cross-review.md` §1) measured the `V3_READ_SET` membership
(`tools/exercise-handoff-e2e.py:1939-1962` against the 58-member r7 roster), found
`13-register-law.yml` is **not** a member, ran a no-mutation control (green,
`45f57132…`), then ran two probes: **Probe A** edited `04-lexicon.yml` by one
comment byte → `exit=1 E2E-DIGEST: D4 component … the assembler recorded
ed7093d6b921… but the bytes measure d4bca30ca2e3…`; **Probe B** added a new
`14-register-forms.yml` → the assembler merged it and rewrote `packet.d4.yml`
(`102837 bytes`), and the default chain then failed. This seat's §8 M16
independently confirms the roster membership and the `13-register-law.yml`
absence. R03's conclusion is this dossier's §2 note 2: **a D4 component edit is
not isolated, and re-freezing is a non-goal.**

**§11.6 — the isolation precedent the Ca legs should cite.** Ca02's clone-with-patched-`ROOT`
is the only in-repo pattern that correctly isolates a filed runner whose `ROOT` is
absolute. The `unshare -rm --propagation private … mount --bind` probes this seat
observed in `ps` (§8 M13) are a **different** isolation attempt — a private mount
namespace binding the scratch dir over the lane root. Both are legitimate; the
leg (Ca2) should accept either and require only that the ledger's evidence show
*one* of them, never an unisolated in-tree run.

**§11.7 — the incident was observed by another seat's window too.** The
`REFRESH_RECEIPTS=1` process in `ps` (§8 M13) re-ran **all three** of r33/r34/r35
in sequence from one clone. r33 escaped (its `ROOT` is
`Path(__file__).resolve().parents[2]`), r34 did not (absolute `ROOT`), and r35's
own `--check` runs are non-writing. So the single observed dirty byte is exactly
the one predicted by reading the three runners' `ROOT` lines — the mechanism is
confirmed by the outcome, not just by the `ps` row.

**§11.8 — F-S01-2 was independently reproduced while this dossier was being
written.** The `x01-clone` process in §8 M13's snapshot ran `git checkout -q --
reports/round-$r/validation.json` for `r` in 33/34/35 and then re-ran all three
runners with `REFRESH_RECEIPTS=1`; the r35 receipt's live digest moved
`328e97b3…` → `8a40245dcecf…` during this seat's own session, and its diff is a
live re-measure (`measured_at_utc 06:19:14` → `06:33:23`, the `X1-X3` manifest
note emptied). This is the second, still-open occurrence of F-S01-1, and it is
also the clean demonstration of F-S01-2: the filed runners' own
`git status -- 'reports/round-1..N'` guard cannot see it. Both findings belong to
the integrator's close pass, not to any claim verdict.

---

## Owed

See §10 for the full owed list and §10.1 for the recompute commands. In brief:
three declared seat outputs were still absent at this seat's final read
(`calib/Ca01-recount-33-34.md`, `calib/Ca03-ledger-draft.md`,
`cross/X01-trades.md`); the claim-C corpus entry and the README revision 2.1 are
integrator-applied drafts; `reports/round-36/run-validation.py`,
`validation.json`, the observed-dispatch record, `availability-close-36.json`,
`../.ufo/reports/round-36/kotodama.md`, the MANIFEST row, `SCORECARD.md` and
`LOG.md` are integrator-only writes; and **`reports/round-35/validation.json` was
still dirty at this seat's finish** (live `8a40245dcecf…` vs filed `328e97b3…`)
and must be restored or adjudicated before the r35 receipt is treated as filed
evidence.

## Citations

- `REGIMEN.md:13,25-29,34-36,52-58` — schedule position 4 (hyper + declared devin
  fallback), the per-round contract, done-when, and the provider-deviation rule.
- `reports/round-36/claims.json` — `round`/`loop`/`position`/`declared_at_utc`/
  `baseline_commit`/`baseline_expanded`/`axes_in_play`/`freshness_pause_in_force`;
  the dispatch block; claims D/C/Ca with their `before`, `after_required`,
  `counting_commands` and `thresholds`; `non_goals`.
- `reports/round-36/targets.json` — `seat_count` 32, the six `shared_rules`, and
  32 seat rows (this seat's mission at the `S01` row).
- `reports/round-36/telemetry/dispatch-declared.json` — allocation, fallback,
  baseline, `durable_sources` digests, `closing_snapshot: open-at-seat-close`.
- `reports/round-36/telemetry/availability-attempt-1.json` — the hyper 402:
  requested 32 / launched 0 / completed 0 / failed 32, seat-id range
  `agent-386..agent-417`, and the position-4 fallback disposition.
- `reports/round-34/run-validation.py:10,26,47-56,209-211,264-280,283-310,319,439-464,514-534`
  — the absolute `ROOT` and `os.chdir`, `strict_json`, the census constant this
  round must not copy, the preservation walk, the language scanner, the four
  `SECTIONS` strings, the selftest style, and the receipt-write site.
- `reports/round-35/run-validation.py:9,36,319` — the same absolute-`ROOT` shape,
  and the re-used `SECTIONS` tuple; `reports/round-33/run-validation.py:23` — the
  relative `ROOT` that made r33 immune.
- `tools/harness/receipt_guard.py:4-8,34-35` — the guard contract and
  `REFRESH_RECEIPTS`; `tools/harness/receipt_guard_adoption.py:6-8,60-61` — the
  census contract and the runner glob.
- `tools/exercise-handoff-e2e.py:157-170` — `D4_COMPONENTS`; `:1939-1962` —
  `V3_READ_SET` (as read by R03); the r7 default chain at `--profile v3 --quiet`.
- `reports/round-34/handoff/declared-in-r7/{expected.json,freeze.txt,packet.md,twin.json,claims-map.md,run.log}`
  — the 58-member roster and the five pinned digests (§8 M16).
- `reports/round-30/handoff/declared-in-r6/{expected.json,freeze.txt,packet.md,twin.json,run.log}`
  — the superseded row whose replay now refuses with `E2E-READSET` (§8 M9).
- `SCORECARD.md:312` — the r25 empty-domain record this claim quotes;
  `SCORECARD.md:329` — the r26 register-stratum landing that closed it;
  `SCORECARD.md:345,363,400` — the r27 law, r28 replay leg, and r30 QREG landing;
  `SCORECARD.md:588-590,615-617,640-642` — the r33/r34/r35 axis rows.
- `reports/round-25/argot/current-state.md:5` — the r25 worktree `f74fc940…`;
  `reports/round-25/argot/delta.md:150-160,206,299,330` — the empty-domain and
  vacuity wording; `reports/round-26/argot/D24-forecast-closure.md:88-92` — the
  false-closure warning K01 cites; `reports/round-26/register/forms.md:16-40` —
  the eight authoritative forms and their arithmetic;
  `reports/round-26/register/execution-3.md:32-51` — the then-`register_scoped=6`
  measurement and the E-1..E-8 delivery table.
- `examples/culture-d4/components/04-lexicon.yml:236-243` — the eight register
  rows; `examples/culture-d4/packet.d4.yml:1329,2491-2527,2788` — the `registers`,
  `form_slots` and `register_law` blocks; `tools/assemble-culture-d4.py:214-224` —
  the `COMPONENTS.iterdir()` walk and `MINIMUM_COMPONENTS`.
- `corpus/README.md:3,31-37,136,160,186,213,245,268,492,494-496` — revision 2.0,
  the r28 footer-defect record, the six section headers, the totals line, the
  counts footer.
- `corpus/knowledge/culture-material/fire-fuel-light.md` — the single `curfew`
  hit in the absence sweep.
- `PROVINCE.md:20` and `:23-26` — the lore-shokunin ownership line and the
  adjacent-contract / contested-scope lines; `SHONEN.md:10-11` — the mark rules;
  `reports/round-32/dossier-d11-shonen-boxes.md:44-52,143-152,200-210` — the box
  conditions quoted in the SHONEN draft.
- `AGENTS.md:15-39` — telemetry rules and close-what-you-open; `LOG.md:3548-3567`
  — the F-C13-1 record of the rounds 5/6/7 in-tree rewrite and its restoration.
- Landed round-36 fragments read in §11: `scout/K01-register-scout.md:11-16,21-22,29,65,136,187,198`;
  `depth/D01-design.md` §0 and the `git log -S` census;
  `depth/D03-isolated-verify.md` §0 and the five-copy table;
  `cross/X00-connector.md` §0 and its surface table;
  `review/R03-cross-review.md` §1 (the two probes);
  `calib/Ca02-recount-35.md:14-18` and its 12-row table;
  `scout/K02-timekeeping-scout.md`; `cov/C04-timekeeping-spare.md`.
- Commands (2026-10-19, repo root, `export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`): §8 M1-M21 as listed there, plus
  `git archive HEAD | tar -x -C .scratch/s01-iso` and the two isolated runner
  invocations (§8 M9, M10), the `ps -eo pid,ppid,etimes,args` capture
  (§8 M13), the whole-receipt digest sweep (§8 M15), and the `ps`/digest
  evidence file `.scratch/s01-ev/incident-r34-snapshot.txt`.
