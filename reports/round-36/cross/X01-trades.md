- Seat: X01 | critic | cross | date 2026-10-19 | baseline ce103bf

# X01 — trade hunter across D / C / Ca

Mission (`reports/round-36/targets.json`, seat `X01`): "Trade hunter."
Out path `reports/round-36/cross/X01-trades.md`. Claim under hunt: `cross`.

This is a **trade register**: every place where a declared axis-move buys one axis at a
cost on another, with the gain, the cost, the evidence and the owner. A trade is
**reported, never averaged into an accept** (`REGIMEN.md`, per-round contract). Nothing
here is an axis verdict, round acceptance, or a promotion/canon/clearance/closure
statement — it is NON-CANON engineering evidence for the integrator's per-axis judging.

Baseline `ce103bf5885af00023cdc4a174c17602476cdcf8` (`git rev-parse HEAD`; equal to
`git rev-parse ce103bf`). Every command from the lane root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. No `reports/round-*/run-validation.py`
was executed **in-tree** (F-C13-1); no `--freeze` was attempted. §6 records one
in-tree filed-byte write **this seat caused and restored**, with its mechanism named.

Dependency state: at this seat's first cut the round directory held the pre-dispatch
files plus three landed fragments (K01, K02, K03); §7 reconciles the fragments that
landed while this seat wrote. The D drafts D01–D03/D05/D06/D09/D10, the C drafts
C01–C05, the Ca drafts Ca01–Ca05, the reviews R01–R03 and the scribe S01/S02 were
**not all on disk**; trades that can only settle on the delivered revision are re-listed
under `## Owed`.

## 0. First-hand measurements (this seat's own runs at `ce103bf`)

| # | command | observed |
|---|---|---|
| M1 | `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md \| wc -l; done` | 21 / 23 / 24 / 29 / 20 / 94 = **211** |
| M2 | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `totals.files 211`, `marker_occurrences 785`, `raw_lines 991` |
| M3 | `python3 -B reports/round-28/readme/sweep.py` | **exit 0**; `rows 211 files 211`, `header_drift {}`, `totals_line 211 totals_ok True`, `footer_ok True`, `readme_sha256 51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0` |
| M4 | `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | **exit 0**, `records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` |
| M5 | `python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | **exit 0**, `law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0` |
| M6 | `python3 -B tools/gates/register-law-gate.py --selftest` | **exit 0**, `selftest: 45/45 checks passed` |
| M7 | `python3 -B tools/gates/typed-pipeline-gate.py` | **exit 0**, `summary: 16/16 legs passed` (flagless) |
| M8 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | **exit 0**, `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` |
| M9 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | **exit 1**, `E2E-READSET: 1 read-set member(s) named by the frozen baseline are not in the live read set: reports/round-20/handoff/claims-map.md — the baseline row is superseded`; **no traceback** |
| M10 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` | **exit 0**, `plus 43 controls` (`grep -c '^  - '` = 44), incl. `m13a`/`m13b` naming `reports/round-20/handoff/claims-map.md` |
| M11 | `python3 -B tools/exercise-handoff-e2e.py --selftest` (bare = **v1** profile, `:4485-4486` equivalent) | **exit 0**, `plus 17 controls` (`grep -c '^  - '` = 18); **zero** `E2E-READSET` mentions |
| M12 | `python3 -B -c` probe: `V3_READ_SET` vs the r7 baseline `inputs` | live 58 / r7 58; **difference empty in both directions**; the only `corpus/knowledge` member is `corpus/knowledge/synthesis/worldbible-integration-contract.md`; `corpus/README.md` **not** a member; no `culture-material` or `myth-symbol` member; `13-register-law.yml` **absent** |
| M13 | the r25 `execution-4.md` greps re-run on the live packet | `derived_from` **9** (r25: 0), `head2` **2** (r25: 0), `#plain\|#quote` 0, `slot_ref\|doublet_of` 0, `^derivation:` 0; packet sha256 now `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` vs r25's filed `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` |
| M14 | the spare's own 28-term absence sweep re-run at `ce103bf` | **27 of 28 terms → 0**; **`curfew` → 1** file (`culture-material/fire-fuel-light.md`) |
| M15 | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` / `--selftest` | exit 0, `findings: 0`, 33 rows == 33 files / exit 0 |
| M16 | `python3 tools/harness/receipt_guard_adoption.py --json` | `class_counts {guarded-refresh: 19, unguarded-in-place: 11}`, `runner_count 30`, `census_complete True` |
| M17 | `git status --porcelain` at this seat's open and close | `?? reports/round-36/` only (§6) |

## 1. Trade register

### T1 — REAL, decidable now, and the round's most consequential. Claim D's axis-move is already in the tree

- **Declared gain (claim D):** "Close the r25 empty-domain record … Author register-form
  component content and the register forms in the packet" (`reports/round-36/claims.json`,
  claim D).
- **Cost: the `before` is a filed reading of 2026-10-18, not of `ce103bf`.** Measured
  first-hand, M4 returns `derived_pairs=8 violations=0` — **not zero**. The domain was
  closed by round 26 (`SCORECARD.md:329`, capability `register-stratum`) and extended by
  r27 (`SCORECARD.md:345`, component 13 + `register_law`), r28 (`SCORECARD.md:363`, the
  law replay leg), r30 (`SCORECARD.md:400`, QREG-05..08). The r25 sentence the claim quotes
  (`SCORECARD.md:312`) is a **superseded filed reading**, correctly left filed under the
  append-only rule, and false of this baseline.
- **Evidence the eight forms are delivered and wired:** M4 `derived_pairs=8`; M5
  `law_rows=5 identity_rows=8 findings=0`; M13 shows the r25 "zero" greps now return 9
  (`derived_from`) and 2 (`head2`); the packet carries 20 `register: "stamp"` lines and
  19 `RGL-0x` row hits; `examples/culture-d4/components/13-register-law.yml` exists as a
  13th component.
- **The trade, stated plainly:** if D lands *new* register-form content, the round buys
  **no depth** (the capability already exists and is green) and pays a ~44-holder pin
  cascade plus a renderer re-point (T2). If D instead lands the genuine residue, the round
  buys real depth and pays the same cascade. Either way the **claim text as declared is not
  the trade the round thinks it is** — the cost is identical, the gain is not.
- **Owner/route:** the integrator/parent (the claim text is not a seat surface). Three
  independent seats reached this same reading before this seat: `scout/K01-register-scout.md`
  §1–§6, `review/R03-cross-review.md` §2, `cross/X00-connector.md` §0 (and D01/D02/D03/D05,
  which landed while this seat wrote — §7). This is not consensus-by-repetition: each
  measured the delivered bytes.
- **Residue that *is* open** (so a re-aimed D has a target): F-6 (`derived_forms`/`derived_ok`
  counters in the coverage block — no producer exists anywhere in `examples/` or `tools/`),
  `head2` declared-but-unused with no domain, and RL-8 (the era leg for RGL-05 is specified,
  unimplemented). Named by K01 §4 and P01 §0; not re-derived here.

### T2 — REAL, structural. Any D4 component edit reddens the pinned r7 chain (depth vs operability)

- **Gain:** whatever content D lands.
- **Cost:** the r7 frozen row `reports/round-34/handoff/declared-in-r7/` is the live default
  (`tools/exercise-handoff-e2e.py:1937-1938`), and it digest-pins the D4 packet and the
  twelve read-set components (M12). Because the assembler rebuilds the packet from the
  **directory** (`tools/assemble-culture-d4.py:214-224`, `>= MINIMUM_COMPONENTS`), *any*
  component-tree change moves the packet.
- **First-hand proof (isolated `git archive HEAD` copy, `.scratch/x01-iso`, this seat):**
  - control: clean copy → r7 chain **exit 0**, `packet_sha256=45f57132…` (matches M8);
  - append a register-form slot to `components/04-lexicon.yml` → r7 default chain **exit 1
    `E2E-DIGEST`**; `assemble-d4-typed.py --check` **exit 2** (`stale projection pin`);
    `d2-typed-labels.py --selftest` **exit 1**.
  - mechanism: `E2E-DIGEST: examples/culture-d4/typed-labels.d4.yml assembly.packet_sha256:
    the tree recorded aac91246cede… for examples/culture-d4/packet.d4.yml but the bytes
    measure 8812df0a2250…` — fail-closed, **not** the `E2E-READSET` superseded-row path.
- **The declared remedy is forbidden and the conformant one is not declared.** Claim D's
  `after_required` says "every pin re-frozen as a new row"; the frozen row in question is
  `declared-in-r7`, which the round boundary and `reports/round-35/claims.json#non_goals`
  both forbid re-freezing. The only conformant move is the r34 precedent
  (`reports/round-34/handoff/repin.json#rows[R34-D-default-pointer]`): land a **successor**
  row and re-point `V3_BASELINE_DEFAULT`/`V3_FROZEN_DIR_DEFAULT`, leaving r7 byte-identical.
- **Owner/route:** D04 (`depth/D04-repin.md`, the re-pin executor) + integrator. Declaring
  the depth improvement without the re-point cascade is a **harm to operability**, not a
  trade (R03 §1 reaches the same verdict from three independent probes).

### T3 — REAL, mitigated in draft. Coverage gain vs the README's present-tense readings

- **Gain:** +1 culture-material entry, 211 → 212 (`cov/C04-timekeeping-spare.md`).
- **Cost:** four present-tense surfaces in `corpus/README.md` move together: the revision
  block (`:3`), `## culture-material/ (24)` (`:186`), `Total knowledge entries: 211.`
  (`:492`), the counts footer `(total 211 files; directory totals 21/23/24/29/20/94)`
  (`:496`). The lane has a documented blind spot for exactly this class: the r27 sweep
  never read the footer and "went green over a stale claim" (`corpus/README.md:27-31`).
- **Mitigation present:** K02 §3 measured the delta and **simulated it end-to-end** on an
  isolated tree (212 rows vs 212 files, `footer_ok True`, `header_drift {}`) with three
  negative controls that all fire exit 1 (header reverted / row deleted / row paraphrased).
  The declared footer vector `21/23/25/29/20/94` is the correct successor of the live
  `21/23/24/29/20/94` (M1, M3). Residual risk is integration-only: applying a *subset* of
  the edits re-opens the r28 defect class.
- **Owner/route:** C02 (delta draft) + S01/S04 (validator legs). The acceptance instrument
  is a filed r28 artifact that must run from the repo root with its reading recorded.

### T4 — REAL, blocking. The spare's own receipt is stale, and it collides with a landed r35 sibling

- **Gain:** the coverage claim's single entry.
- **Costs, both measured:**
  - **Stale gap statement.** The spare's `- gap filled:` line asserts a sweep at HEAD
    `4a7aede` over "201 files" with "**0 for every term**" (`cov/C04-timekeeping-spare.md:13`).
    Re-run at `ce103bf` (M14): the tree is 211 files and **`curfew` → 1**
    (`culture-material/fire-fuel-light.md`). Landing the fenced bytes unedited writes a
    present-tense false measurement into the corpus — the r28 false-green class one level up.
  - **Unamended couples collision.** The spare's `- couples:` line names 24
    `corpus/knowledge/…` paths, **none** of which is any of the ten r35 entries. The
    load-bearing one is `fire-fuel-light.md`, which landed in r35 and owns the
    night-watch / curfew / risk-apparatus surface the spare also claims (K02 §2 measures
    shared-term Jaccard **0.211** vs the 0.118 topic-level pass threshold).
- **The honest reading:** the *domain* claim survives — no entry owns the **instrument**
  (27 of 28 instrument terms still 0, and no file owns a sundial, clepsydra, escapement or
  gnomon). What fails is the **receipt**. The gap line must be **re-measured, not
  arithmetic-adjusted** (`corpus/lessons/round-19.md:115`), and a boundary clause against
  `fire-fuel-light.md` is owed before landing.
- **Owner/route:** C01/C02/C03 + integrator. Also routed: C01's F1 stager defect — the
  spare names no explicit target path, so the r35 runbook's stager resolves it to an
  existing filed entry (`calendar-festival-systems.md`). Any landing must be given the slug
  explicitly.

### T5 — REAL, minor, filed. A filed census row disagrees with its own filed artifact

- **Gain:** none (this is a defect, not a trade).
- **Observation:** `SCORECARD.md:616` (r34 operability row) and `reports/round-34/validation.json`
  record "inventory of all **29** filed runners: **18** guarded-refresh / **11**
  unguarded-in-place". The filed artifact the row cites,
  `reports/round-34/op/adoption-inventory.json`, contains **28** rows and
  `class_counts {guarded-refresh: 17, unguarded-in-place: 11}`. Re-running the tool at
  `ce103bf` (M16) returns **30** rows / **19+11**, the two extra being r34's and r35's own
  runners (which did not exist at r34's close).
- **Why the numbers differ, measured:** the r34 inventory's `glob` is
  `reports/round-*/run-validation.py`; at r34's close that glob matched **28** files
  (r13 has no runner), so 29 is not reproducible from the artifact under any reading tried.
  The `28 → 30` growth is fully explained by two new filed runners and is *not* a defect;
  the `29/18` reading is.
- **Disposition:** `unprovable-as-stated` against `SCORECARD.md:616` /
  `validation.json#claims.O`. Not repaired here (both are filed bytes; the lane rule is a
  new dated row, never an edit). Owner: the Ca ledger (Ca03) or the integrator. This is the
  same class as `reports/round-34/op/adoption-inventory.json#findings[RGA-2]`
  ("8 runner(s) … are not in the F-C13-1 declared set") — a count row that outlives its
  artifact.

### T6 — REAL, drafting requirement. Coverage and calibration collide on the same counting surface

- **Gain:** claim C moves 211 → 212; claim Ca recounts the r33–35 filed commands.
- **Cost:** `for p in …; do ls corpus/knowledge/$p/*.md | wc -l; done` and
  `reports/round-28/readme/sweep.py` are **both** enumerated by Ca and **both** moved by C.
  A ledger that records "observed" without a revision stamp will read as a mismatch: 211
  before C lands, 212 after. Neither number is wrong.
- **Evidence:** M1/M3 are the pre-landing readings; the r35 filed census (211) and the r36
  target (212) are both correct at their own revisions.
- **Owner/route:** Ca03 (ledger draft) — carry a per-row `observed_at_revision` or an
  explicit ordering statement, the discipline the r29 recount already used
  ("revision boundaries documented 175/183", `SCORECARD.md:382`).

### T7 — REAL, bounded. Coverage gain vs the r35 filed runner's hardcoded counts

- **Gain:** the +1 entry.
- **Cost:** `reports/round-35/run-validation.py` hardcodes `EXPECTED_COUNTS` (CM 24) and
  `!= 211`. Those are **filed bytes and must not be edited**; after the C landing the r35
  runner's own legs would go red if re-run against the new tree.
- **Bounded, and provable:** this is exactly what M17's recount shows for r33 — see §3.
  `reports/round-33/run-validation.py:943` hardcodes `tracked_count != 2655`, and at
  `ce103bf` `git ls-files | wc -l` = **2903** (the tree has grown 248 tracked paths since
  r33), so the r33 runner now fails its own A3 leg. **This is not a r36 regression** — it is
  the expected consequence of a filed round-runner pinning its round's tree — but it means
  a recount that runs old runners and reports their exit codes as the round's reading will
  report `False` for a round that was admitted. Round 36 needs its own 212 expectations.
- **Owner/route:** S01 (validator-leg spec) + integrator.

## 2. The recount (claim Ca) — this seat's own readings

The Ca ledger is Ca01–Ca03's deliverable; this is an independent recount from the trade
side, since a mismatch here is itself a trade surface (T5/T7).

| round | claim | command | filed | observed at `ce103bf` | disposition |
|---|---|---|---|---|---|
| 33 | O | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | exit 0, 0 findings | exit 0, `findings: 0`, 33 rows == 33 files | **match** |
| 33 | O | `… --selftest` | green | exit 0 | **match** |
| 33 | O | `test -s reports/round-33/op/O05-falsifier-disposition.md` | landed | exit 0 (20935 B) | **match** |
| 33 | C/A | `python3 reports/round-33/run-validation.py` | exit 0 | **exit 1**, `acceptance=False`, 4 failures (A3 2655 vs 2903; X1 ×3) | **mismatch — expected, T7** |
| 34 | D | `tools/gates/handoff-packet-check.py …/declared-in-r7/packet.md` | exit 0 | exit 0, `fields=16/16 glossary-entries=20 findings=0` | **match** |
| 34 | D | `tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0, `45f57132…` | exit 0, `45f5713261762a95…` | **match** |
| 34 | O | `tools/harness/receipt_guard_adoption.py --selftest` | green | exit 0, `selftest_passed true` | **match** |
| 34 | O | `tools/harness/receipt_guard_adoption.py --json` | inventory | exit 0, **30 rows / 19+11** (filed artifact: 28 / 17+11) | **mismatch — T5** |
| 34 | C | `python3 -B reports/round-30/craft/box1-survey.py` | 28/28 at `f9bd07c2…` | exit 0, `resolvable 28`, `unnamed_in_skill []`, `skill_sha256 f9bd07c2…` | **match** |
| 34 | D/O/C | `python3 reports/round-34/run-validation.py` | exit 0, `acceptance True` | **exit 120 / `acceptance True`, 0 failures** (isolated clone) | **match on substance** — see §3 |
| 35 | C | partition census | 21/23/24/29/20/94 | 21/23/24/29/20/94 | **match** |
| 35 | C | `tools/source-audit-inventory.py --json --summary` | 211 | `totals.files 211` | **match** |
| 35 | O | `tools/exercise-handoff-e2e.py --selftest` | green | exit 0, 18 controls | **match** |
| 35 | O | `… --profile v3 --quiet --baseline …declared-in-r6…` | exit 1, named | exit 1, `E2E-READSET … reports/round-20/handoff/claims-map.md`, no traceback | **match** |
| 35 | C/O/A | `python3 reports/round-35/run-validation.py` | exit 0, `acceptance True` | **exit 0, `acceptance True`, 0 failures** (isolated clone, §3) | **match** |

Summary: **12 match, 2 dispositioned mismatches (T5, T7), 1 substantive match with a
recorded exit-code caveat (§3).** No mismatch smoothed. R03 §5 independently recounts
11 match / 7 `could-not-reproduce-in-tree`; this seat's extra resolution is that the two
runner rows **do** reproduce — see §3.

## 3. The runner recount, done properly (isolated clone), and the trap that cost this seat a filed-byte write

**Method.** `git clone --no-hardlinks . .scratch/x01-clone`, `git checkout ce103bf`,
`export REFRESH_RECEIPTS=1`, then run each filed runner. This is the sanctioned
isolated-copy protocol (`reports/round-34/op/adoption-inventory.json#protocols`).

**Results.**

| runner | exit | `acceptance_checks_passed` | failures |
|---|---|---|---|
| `reports/round-33/run-validation.py` | 1 | **False** | A3 (2655 vs 2903) + X1 ×3 — **filed r33 value was True** |
| `reports/round-34/run-validation.py` | 0 (first) / 120 (later) | **True** | 0 — matches filed |
| `reports/round-35/run-validation.py` | 0 | **True** | 0 — matches filed |

**The r33 reading is not a r36 regression.** `reports/round-33/run-validation.py:943` pins
`tracked_count != 2655`; the r33 baseline `139e3b6` had exactly 2655 tracked paths (verified
`git ls-tree -r --name-only 139e3b6 | wc -l` → 2655) and `ce103bf` has **2903** — the tree
has grown 248 tracked paths across r34/r35/r36. The r33 X1 leg fails for the same reason:
the fleet report `.ufo/reports/round-33/kotodama.md` is **outside this repo** and does not
exist here (`ls .ufo/reports/round-33/` → No such file or directory). Both failures are
**filed-pin-vs-current-tree** effects, exactly T7's class, and the filed r33 receipt stands
as the r33 reading.

**The trap (F-C13-1-adjacent, self-caused, restored).** `reports/round-34/run-validation.py:10`
and `reports/round-35/run-validation.py:9` hardcode `ROOT =
"/home/vgpnk/Projects/shokunin/kotodama-shokunin"` and call `os.chdir(ROOT)` (`:26` and
`:36`). Running either from inside the clone therefore **chdir's into the main tree and
writes `reports/round-35/validation.json` there** — the isolated copy does not protect
against a runner that absolutizes its own root. This seat's clone runs did exactly that:

- observed at 09:31Z: `git status --porcelain` → ` M reports/round-35/validation.json`;
  worktree blob `9b85cd08…` ≠ HEAD `11f241a4…`; `git diff` showed `X1-X3.measurement`
  losing its `pending-by-construction` note and `measured_at_utc` moving
  `06:19:14` → `06:33:23`;
- **restored byte-exact** with `git checkout -- reports/round-35/validation.json`; verified
  worktree blob `11f241a4ba14901c3ef14b348c28f915e772fa7a` == `HEAD:` blob, and
  `X1-X3.measurement` again carries `pending-by-construction`, `measured_at_utc`
  `06:19:14.685566-03:00`;
- at this seat's close: `git status --porcelain` → `?? reports/round-36/` **only** (M17).

**Why this matters beyond this seat.** `reports/round-33/run-validation.py:23` uses the
portable form `ROOT = Path(__file__).resolve().parents[2]`; r34 and r35 switched to an
absolute literal. So r34/r35 are **guard-adopted but not clone-safe** — the guard refuses
an in-tree overwrite until `REFRESH_RECEIPTS=1`, but `REFRESH_RECEIPTS=1` (which the
sanctioned clone protocol requires) combined with an absolute `ROOT` writes the main tree
from anywhere. The r34 census classifies both as `guarded-refresh` and routes
`unguarded-in-place` runners to isolated-copy-only; **it does not name this
absolute-ROOT hazard** (`reports/round-34/op/adoption-inventory.json#findings` carries
RGA-1 and RGA-2 only). Owner: the integrator — either a new census finding, or a note in
the protocol that the clone must also shadow the absolute `ROOT`.

## 4. Negative findings (no trade — checked, not assumed)

- **N1 — claim C's landing cannot drift the r7 freeze.** M12: `corpus/README.md` is not a
  read-set member, and the only `corpus/knowledge` member is the contract file. Neither the
  new `culture-material/timekeeping-instruments.md` nor the README revision block is a
  member. Guard worth a leg: assert `git diff --name-only ce103bf..HEAD` ∩ read-set = ∅.
- **N2 — the r35 operability fix is landed, green, and non-vacuous.** M9 returns the named
  `E2E-READSET` refusal with no traceback (the r34 `KeyError` is gone), M10 shows `m13a`/`m13b`
  covering it, and M8 shows the r7 chain still exit 0 at the same `45f57132…` packet. The
  r35 `after_required` ("named diagnostic … E2E-DIGEST path unchanged") is satisfied.
- **N3 — the r7 chain is not exposed to the C landing.** M8 measured at `ce103bf`; the C
  landing touches no read-set member (N1). Only the D landing is exposed (T2).
- **N4 — no live gate auto-scans the corpus partitions.** `tools/gates/register-law-gate.py`
  and `argot-derivation-gate.py` take a packet path; adding one `.md` entry trips no gate.
  The C gain carries no hidden operability cost there.

## 5. What this puts on the integrator (actionable)

1. **Re-state or re-aim claim D before any landing.** Its `before` is unverifiable at
   `ce103bf` (T1). Either narrow D to the named residue (F-6 counters, `head2` domain,
   RL-8 era leg) or record D as already-satisfied and report the round's depth verdict
   against the residue, not against an empty domain.
2. **Pair any D landing with the successor-row re-point** (T2). Without it, the r7 default
   chain goes red and the round's own standing regression breaks. `declared-in-r7` must
   stay byte-identical.
3. **Re-measure the spare's gap line and add the `fire-fuel-light.md` boundary clause**
   before the C landing (T4). Do not arithmetic-adjust the counts.
4. **Stamp each Ca ledger row with its revision** (T6), so the 211/212 boundary reads as
   two correct readings, not a mismatch.
5. **Disposition `SCORECARD.md:616` / `reports/round-34/validation.json`'s 29/18/11** as a
   new dated row (T5); the artifact says 28/17/11 and the live tool says 30/19/11.
6. **Record the absolute-`ROOT` clone hazard** (§3) as a census finding or protocol note.

## 6. Owed

**All 32 seats have landed.** `find reports/round-36 -type f -name '*.md' | wc -l` → **32**
(the D block D01–D10, the C block C01–C05, the Ca block Ca01–Ca05, K01–K03, P01, R01–R03,
S01–S02, X00/X02 and this file). Every dependency this seat's trades named is therefore
available; §7 reconciles the ones that landed after §0–§5 were drafted.

Still owed at this seat's close:

- **`reports/round-36/run-validation.py` does not exist** (`ls` → absent), so claims D and
  Ca's declared counting command `python3 -B reports/round-36/run-validation.py` is
  `to-verify` until the integrator lands it; per F-C13-1 it must not be run in-tree regardless.
- **The successor-row bytes** (T2) — D04 drafts the row set and the pointer move, but the
  digests must be re-measured on the bytes actually landed (D04 §0: "the *row set* is what
  this seat owes; the digest values must be re-measured by the integrator").
- **The spare's re-measured gap line and the `fire-fuel-light.md` boundary clause** (T4) —
  authored bytes, owed to whoever lands the entry.
- **The Ca ledger's per-row revision stamp** (T6) — Ca03 landed (`calib/Ca03-ledger-draft.md`,
  ledger `"revision": 2`, every row `match`), but its rows record the pre-landing **211**
  census with no `observed_at_revision` field, so the stamp is still owed to the integrator's
  finalization.
- **The adoption-census disposition** (T5) — not reached by any landed fragment.

Post-landing re-measurement this seat cannot do at `ce103bf`, to be closed against the
delivered revision:

1. T1/T2 — the re-aimed D content, the successor-row name (`declared-in-r8` vs
   `pinsweep/v3-baseline-r36`), and whether the r7 default chain is still exit 0 after the
   re-point.
2. T3/T4 — the spare's re-measured gap line and boundary clause, then the r28 sweep reading
   (`footer_ok True`, `totals_line 212`, `header_drift {}`).
3. T5 — the adoption-census row re-derived from the filed artifact and the live tool.
4. T6 — the Ca ledger's revision stamps.

## 7. Post-cut reconciliation (fragments that landed while this seat wrote)

Fragments appeared in two waves after §0–§5 were drafted; re-read for the trades above. All 32
seat files are now on disk. The first wave (seven fragments: K01, K02, R03, X00, P01, D02, D03)
is reconciled first; the second wave (the remainder, incl. D04, Ca02–Ca05, C01–C05) follows.

**T1 — independently corroborated, five more seats, same measurement.** `scout/K01-register-scout.md`
§1–§4 (lineage table r26→r30; `derived_pairs=8`; the three-item residue F-6/`head2`/RL-8),
`review/R03-cross-review.md` §2 (the r25 sentence "was superseded two rounds later"),
`cross/X00-connector.md` §0 (with the landing commit `4f09c99`), `depth/D05-receipt.md` §0
("every clause of `after_required` is already satisfied … clause by clause"),
`depth/D02-packet-draft.md` §0, `depth/D03-isolated-verify.md` §1, `plan/P01-d-plan.md` §0
("the claim's `before` is stale; the plan is re-aimed"). P01 re-aims onto **Surface A + B-1**
(the `doublets` block as the forward index) and prices B-2 as a contract amendment — so the
re-aim has a concrete target, which strengthens T1's route.

**T2 — corroborated and sharpened.** R03 §1 ran three independent probes (edit a read-set
member; add a **new** component file; edit **only** the non-member `13-register-law.yml`)
and all three reddened the r7 chain — the third is the sharpest and confirms my M12 reading
that read-set membership is not the protection. R03 §1 also names the conformant remedy
(successor row + `V3_BASELINE_DEFAULT` re-point) and the r34 precedent, matching §5.2.
D02 §1 adds a *second* cost inside a D landing: `argot-derivation-gate.py` grades **every**
block carrying a form-shaped field, so a `register_forms` block that restates
`form`+`derived_from`+`derivation` double-grades the eight derivations
(`register_scoped` 14 → **22**); pointer-only or off-channel field names avoid it. That is a
real design constraint on the D content, and it is a **harm** if ignored, not a trade.

**T4 — corroborated.** `scout/K02-timekeeping-scout.md` §1 re-ran the spare's own sweep and
found the same `curfew → 1` plus a wider stale set (`chronometer` 2→4, `hour` 8→17,
`bell` 81→87, `clock`-in-CM 6→10, `night watch` 1→2), and §2 measured the
`fire-fuel-light.md` section-level overlap. `cov/C01-audit.md` and `cov/C03-verify.md`
independently agree on `curfew` and the delta; C01 adds the F1 stager defect. **One countable
disagreement filed rather than smoothed:** K02 §6.1 records three seats reading the spare's
`couples:` as 24 (K02), 25 (C01) and 31 (C03). This seat's own count reproduces **24** for
the `- couples:` line (prefixed-unique 24, occurrences 24) and cannot reproduce 25 or 31
under any of six methods tried (whole-entry prefixed-unique 27, +bare 28, occurrences 46).
**Disposition: 24 with the method named; the peers' 25/31 are `unprovable-as-stated` from
the entry text.** 0 unresolved under every method, so no finding changes.

**T5 — not corroborated by any peer, and it is a genuine new reading.** No landed fragment
dispositions `SCORECARD.md:616`'s 29/18/11 against
`reports/round-34/op/adoption-inventory.json`'s 28/17/11. `cross/X02-conformance.md`
audits append-only/F-C13-1 discipline and does not reach the count.

**§3's trap — independently identified by a peer, and it is now the round's clearest tool finding.**
`calib/Ca02-recount-35.md:14-22` names the *identical* mechanism from the same filed lines
(`reports/round-35/run-validation.py:9` absolute `ROOT`, `:36` `os.chdir(ROOT)`) and reaches the
same conclusion: "an `git archive` copy of it still writes to the live tree". Ca02 avoided it by
patching that one line in its clone and running `--check` (which never publishes) — the correct
workaround, and the one this seat did not take. `cross/X02-conformance.md` §0a observed
` M reports/round-35/validation.json` at 09:26–09:31Z with the *same* two-field diff
(`X1-X3.measurement` → `{}`; `measured_at_utc` moving) and read it as an in-flight
F-C13-1-class breach by another seat. **All three observations are the same artifact and the same
cause**: a tool property (absolute `ROOT` + `os.chdir`), not a seat's discipline lapse. Ca02 and
this seat are two independent confirmations of the mechanism, and Ca02's `--check` route is the
remedy to adopt. Worth a named finding: the r34 census's `guarded-refresh` class does **not**
imply clone-safety.

**New corroboration for T7:** the r33 runner's own A3/X1 failures (§3) are the cleanest
available demonstration that a filed runner pins its round's tree, not the current one.

**T2/T6 — the late fragments supply the remedies this seat's trades named.**
`depth/D04-repin.md` §2.3 drafts the successor directory as
`reports/round-36/handoff/declared-in-r8/…` and states the rule this seat's T2 argues
("the r7 bytes must not be edited"), plus the limit that makes the trade irreducible: because
digests are content-dependent, "the *row set* is what this seat owes; the digest values must be
re-measured by the integrator on the bytes actually landed". D04 §3.5/§3.6 also adds two filed
surfaces this seat's T2 list did not name (`twin.json`'s successor row and
`reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` needing its own successor generation).
`calib/Ca03-ledger-draft.md` landed at `"revision": 2` with every row `match`, and `calib/Ca04-verify.md`
§S1–S11 independently reproduces 11 of this seat's §2 readings (including `readme_sha256 51b966af…`
and the `E2E-READSET` refusal) — no mismatch between Ca04's recount and this seat's on any row
both measured. Ca03's rows still carry the pre-landing 211 census without an
`observed_at_revision` field, so T6's stamp remains owed.

## Citations

- `reports/round-36/claims.json` (claims D/C/Ca, `before`/`after_required`/`thresholds`);
  `reports/round-36/targets.json` (seat X01 mission/out; `shared_rules`).
- `reports/round-36/scout/K01-register-scout.md` §1–§6; `scout/K02-timekeeping-scout.md`
  §0–§6.1; `review/R03-cross-review.md` §1–§7; `cross/X00-connector.md` §0;
  `cross/X02-conformance.md` §0a; `plan/P01-d-plan.md` §0, §4.2;
  `depth/D02-packet-draft.md` §0–§1; `depth/D03-isolated-verify.md` §1;
  `depth/D05-receipt.md` §0.
- `reports/round-35/claims.json` (claim O `after_required`, `non_goals`); `reports/round-35/cov/C04-timekeeping-spare.md:13`
  (stale gap line), sha256 `258fb166e35f3b0f92854dcb7c5e08fcfc285c51a42aa828cb79f3f761f5bcd2`.
- `SCORECARD.md:312` (r25 EMPTY), `:329` (r26 register-stratum), `:345,352` (r27 law + RL-3),
  `:363` (r28 replay leg), `:382` (r29 revision boundaries), `:400` (r30 QREG), `:616` (r34
  29/18/11), `:640` (r35 211).
- `corpus/README.md:3`, `:27-31`, `:186`, `:492`, `:496`; `corpus/lessons/round-19.md:115`.
- `tools/exercise-handoff-e2e.py:1937-1938` (`V3_BASELINE_DEFAULT`/`V3_FROZEN_DIR_DEFAULT`),
  `:157-170` (`D4_COMPONENTS`, 12 files), `:1939-1962` (`V3_READ_SET`, 58 members),
  `:3830-3840` (`E2E-READSET`), `:3841` (`E2E-DIGEST`); `tools/assemble-culture-d4.py:64,214-224`.
- `reports/round-34/handoff/repin.json` rows `R34-D-default-pointer`, `R34-D-stale-row`;
  `reports/round-34/handoff/declared-in-r7/{freeze.txt,expected.json}`.
- `reports/round-34/op/adoption-inventory.json` (`class_counts`, `runners` 28,
  `findings[RGA-2]`, `limits`, `protocols`); `reports/round-34/validation.json#claims.O`.
- `reports/round-35/run-validation.py:9,36,203` (absolute `ROOT`, `os.chdir`, the v3 selftest
  leg); `reports/round-34/run-validation.py:10,26,209`;
  `reports/round-33/run-validation.py:23,943,1028-1032`;
  `reports/round-28/readme/sweep.py:21,22,69,74-79`;
  `tools/harness/receipt_guard.py:34,152,161,314`.
- `examples/culture-d4/components/13-register-law.yml`; `examples/culture-d4/packet.d4.yml`
  (20 `register: "stamp"` lines, 19 `RGL-0x` hits, sha256 `aac91246cede…`);
  `corpus/knowledge/culture-material/fire-fuel-light.md`.
- Commands: M1–M17 as tabulated in §0; the isolated probes in T2
  (`.scratch/x01-iso`, `git archive HEAD`); the clone recount in §3
  (`.scratch/x01-clone`, `git clone --no-hardlinks .`, `REFRESH_RECEIPTS=1`).
