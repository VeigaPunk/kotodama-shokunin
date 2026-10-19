- Seat: X04 | critic | cross | date 2026-10-19 | baseline 139e3b6

# X04 — honesty census: to-verify marks, could-not-evaluate flags, integrator-only verification

Axes worked (Godspeed, no clarifying questions): **honesty** (mark census with
provenance), **integrator-dependency visibility** (which claim legs no seat can
close), **honest-stop precision** (exact observables that must halt a pass).
Every item below is a file:line or a command run by this seat at the cut;
nothing is inferred. Unknowns are marked `to-verify`.

## Cut and method

Evidence cut **2026-10-19T03:56:43Z**, lane HEAD `139e3b66` (untracked
`REGIMEN.md`, `reports/round-33/`, modified `LOG.md` — `git status --porcelain`).
Only **3** round-33 files existed at the cut (`find reports/round-33 -type f`
= 3): `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`. All 64
seat fragments are therefore **unlanded at this cut**; this census covers (a) the
declaration artifacts, (b) the round-32 evidence base the claims inherit, and (c)
the claim-referenced round-33 paths. A fragment-level re-census is owed (below).

Commands (all re-runnable):
```
find reports/round-33 -type f | wc -l                              # 3
sha256sum reports/round-33/claims.json reports/round-33/targets.json
grep -rn "to-verify" reports/round-33/                             # 2 hits, both non-marks
grep -rn "could-not-evaluate" reports/round-32/ reports/round-29/  # counts in §2
python3 -B reports/round-25/audit/c31-lessons-index-audit.py       # exit 1 (before state)
```

## §1 — to-verify mark census

| scope | literal `to-verify` occurrences | reading |
|---|---|---|
| `reports/round-33/**` at cut | **2**, both non-marks: `targets.json:9` (the shared rule defining the convention) and `targets.json:77` (this seat's own mission text) | zero seat-authored unknowns filed yet |
| `reports/round-33/claims.json` | 0 | claims declare no unknown at declaration |
| `reports/round-32/**` | **4 lines, all inside `validation.json` captured tool stdout** (`:418` d2-typed-labels selftest phrase "a (to-verify) ERX row is mapped-unconfirmed"; `:628` provenance-audit `INFO to-verify-count:`; `:768`, `:936` battery/inventory stdout) | zero seat-authored honesty marks in round-32 `.md` fragments — the marks the census looks for do not exist in the evidence base as marks |

Convention pointers for the mark vocabulary: `AGENTS.md:11` ("claims you cannot
verify are marked `to-verify`"), `targets.json:9`, and the corpus-wide marker
convention the inventory tool counts (`reports/round-32/validation.json:936`
caveat block: 621 bare marker occurrences, "markers_never_auto_cleared") — the
last is `corpus/knowledge` scope, **not** round-33 claim scope.

**Reading:** at this cut round 33 has filed **no** `to-verify` marks, so the
honesty risk is not stray marks but **unmarked unknowns**: statements whose
verification depends on artifacts that do not exist yet (see §3). The
fragment-level census is the operative one and is owed.

## §2 — could-not-evaluate (CNE) census, inherited into round 33

| flag | source (file:line / count) | status carried into r33 |
|---|---|---|
| devin availability leg CNE | `reports/round-32/dossier-d13-operator-decisions.md:116,137`; `final-dossier.md:110`; `reports/round-32/scribe/fragment-ledger.md:135,201,215` (`full_wave_status: "could-not-evaluate"`) | item in the 12-item debt table (claim C scope) |
| r29 recount CNE rows | `reports/round-29/recount/r27-full-sweep-reproduction.json` — **50** occurrences | durable record; not re-litigated this round |
| frozen-manifest rows CNE at filed bytes | `reports/round-32/final-sweep.md:154,155,156,158,159,161,162` (7 manifest rows: round-3, round-3/attempt-1, round-11, round-18, round-20, round-23, round-25) | r32 sweep verdict; r33 does not re-run these |
| sweep-audit gate-digest CNE | `reports/round-32/sweep-audit-O09.json` 7 hits, `sweep-audit-O10.json` 7 hits (`could-not-evaluate reason=gate_digest_mismatch`) | r32 audit artifact |
| validator CNE semantics | `reports/round-32/run-validation.py:925,1136` (exception → `could-not-evaluate`) | the pattern r33's validator should keep |
| r33 telemetry | `telemetry/dispatch-declared.json`: **0** CNE; but `:6` defers observed launches/completions to a separate record and `:28` files the closing snapshot `open-at-seat-close` | **two integrator-owed records** (see §3, HS-6) |

Honesty note: `dispatch-declared.json` declares digests for `claims.json`
(`ba69090f…`) and `targets.json` (`342c8f80…`); this seat re-ran `sha256sum` at
the cut — **both match the declared values exactly**. The declaration's own
provenance is true as filed.

## §3 — claim legs that only the integrator can close

Verified by `python3 -c` over `targets.json` `out` values (64 seat outs) vs the
paths `claims.json` names:

| claim | claim-referenced path / step | seat `out` covers it? | state at cut |
|---|---|---|---|
| C | `reports/round-33/calib/open-items-ledger.json` (after_required; counting command) | **no** — C15's out is `calib/C15-ledger-draft.json` (a draft) | MISSING |
| C | `python3 reports/round-33/run-validation.py` (counting command `claims.json:48`) | **no** — S04 drafts a leg *spec* only (`targets.json:82`) | MISSING |
| C | fix application from `calib/C14-fix-drafts.md` | seat out exists (draft) | MISSING at cut |
| A | `reports/round-33/adj/audit-assembled.md` (after_required says "(integrator)") | **no** — A15's out is `adj/A15-audit-draft.md` | MISSING |
| A | `python3 reports/round-33/run-validation.py` (counting command `claims.json:61`) | **no** | MISSING |
| A | handoff gate re-run on the current packet pair | A02 seat-owed; not yet run | pending |
| O | lessons README edit (`corpus/lessons/README.md`) — the counting command `c31-lessons-index-audit.py` **exits 1 until the integrator applies O01/O02 drafts** | drafts only (seats never edit) | exit 1, 2 findings |
| O | falsifier fix application ("integrator-applied; no filed-byte rewrites", `claims.json:30`) | O05 disposition is a seat out; application is not | O05 MISSING |
| all | regression comparison vs the O07 baseline receipt (post-edit) | O07 = pre-edit receipt; post-edit re-runs are integrator-only | not started |
| all | SCORECARD/LOG/MANIFEST/fleet-report entries, telemetry observed-dispatch + closing snapshot | integrator-only by rule (`targets.json:6-10`, `AGENTS.md:32-38`) | owed |

So **claims C and A are unverifiable by any seat this round**: their own counting
command does not exist at the cut. That is consistent with the contract
(`REGIMEN.md:43` admit-only-when-verified; `:57-58` admitted rounds require
`run-validation.py` exit 0), but it must be stated plainly in the round report —
not presented as seat-verified.

## §4 — before-value re-verification (independently re-run at HEAD)

Claim O before (`claims.json:25`) — **reproduced exactly**:
`python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 1;
`FAIL C31_index_rows_eq_files`, `FAIL C34b_prose_arithmetic`;
`lesson files: 33 / index rows: 26 / queue rows: 49`;
`C31-1 unindexed-file: ['round-26.md' … 'round-32.md']` (exactly 7);
`C34-2 prose-arithmetic-drift: {'table_rows_vs_files': {'stated': [26, 26], 'measured': [26, 33]}}`.
`--selftest` → **28/28 checks passed, exit 0** (README:35 states "26/26" — stale, see H-4).

Claim A before (`claims.json:57`) — **reproduced**: `git ls-files | wc -l` = 2655
and `git ls-tree -r --name-only 139e3b6 | wc -l` = 2655; `git log --oneline -3 --
PROVINCE.md` → last touch `c53782a`; `ls -d reports/round-2{1,9}/adjacency` exists,
`reports/round-3{0,1,2}/adjacency` absent → "no consolidated audit since r29" true.

Claim O threshold pre-check: the four O07 selftests are green at HEAD today —
`tools/check-gate-battery.py --selftest` 44/44 exit 0; `check-craft-exercise.py
--selftest` 10/10 + CLI 18/18 exit 0; `assemble-culture-d4.py --selftest` 81/81
exit 0; c31 `--selftest` 28/28 exit 0. Precision note: `claims.json:37` says
"battery 10/10" — that is the *coverage* mode figure (`reports/round-32/validation.json`
summary `coverage: "10/10"`), not the selftest count (44/44); the O07 receipt
should state which mode each number came from.

## §5 — named honesty findings

- **H-1 (high) — the "12" has no canonical enumeration on record.** `SCORECARD.md:444`
  says "12 standing open items in the dossier"; `final-dossier.md:107` says
  "Twelve named items tabled with origins and pointers"; the Decision-4 table
  itself carries **9** debt rows (`dossier-d13-operator-decisions.md:128-138`).
  A plausible origin of the numeral is the first row's own count — "12 D4
  garment-form holds" (`d13:130`; `final-dossier.md:110` "design debts (12
  garment holds, head2, RL-3)") — but that is a **reading, not a sourced fact**;
  whether SCORECARD's 12 means 9 rows + 3 D11 standing readings, 9 rows alone,
  or the garment-hold count is **`to-verify` until K03's canonicalization lands**.
  Claim C's threshold ("ledger row count == 12", `claims.json:48-50`) and C15's
  "exactly 12 rows" instruction (`targets.json:45`) both assume K03 returns 12.
- **H-2 (medium) — C/A legs are integrator-only** (§3): `open-items-ledger.json`,
  `audit-assembled.md`, `run-validation.py` have no seat out and are MISSING.
  Risk: a round report that reads as if seats verified C/A.
- **H-3 (medium) — claim O leg (b) is scout-dependent and currently failing its
  own counting command**: `test -s reports/round-33/op/O05-falsifier-disposition.md`
  → exit **1** at cut. The phrase *is* findable (`corpus/lessons/round-32.md:36`
  "## The falsifier legs — substance 5/5, instrument false-fires on day one"),
  so a could-not-locate outcome for K01 is unlikely — but O05 must still resolve
  *the filename mismatch* specifically; the lessons file heading names the
  substance count, not the mismatch. `to-verify` until K01/O05 land.
- **H-4 (medium) — README prose arithmetic is under-checked.** The tool's C34b
  reads exactly two prose forms (`c31-lessons-index-audit.py:296-300`: `Rows: **N**`
  → first match, and `**Rows: N. Files: N.**`) and its only live drift key is
  `table_rows_vs_files`. Unflagged stale cells confirmed at the cut:
  `corpus/lessons/README.md:35` "# 26/26, exit 0" (live selftest is 28/28),
  `:39-40` "# 26", `:6` "26 at the". Claim O's after_required ("prose arithmetic
  states 33") is therefore **broader than its counting command** — the extra
  cells are honesty items, not audit items.
- **H-5 (medium, counting-command trap) — adding queue rows moves a second
  number.** C34b's queue leg compares the **first** `Rows: **N**` match
  (`c31:297-298,303-305`) to `len(queue_rows)`; today that is README:207
  "Rows: **49**". O02's after_required includes "the new open-question queue rows
  for r26-r32" (`targets.json:23`) → if new `| Q-` rows land without updating
  `:207`, C34b fails on the queue leg even after the table is fixed.
- **H-6 (low) — revision-block mechanism is compatible, one constraint.** Rows are
  matched by `ROW_RE` anywhere in the README text (`c31:42,124-129`), so
  appending a Revision-3 block (the README's own convention, `README.md:303-304`)
  satisfies C31 — provided each new row *leads* with the file cell
  (`| \`corpus/lessons/<name>.md\` | … |`). In-place rewriting of revision-1 rows
  would violate the README's stated convention; the integrator must choose one
  and say so.
- **H-7 (low) — the round's own closure records are open.** `telemetry/dispatch-declared.json:6,28`
  owes an observed-dispatch record and a closing snapshot; `AGENTS.md:32-38`
  makes the closing snapshot a precondition for admission. No round-33 telemetry
  CNE exists yet, and none may be invented.

## §6 — recommended honest-stop triggers

- **HS-1.** If K03's canonical count ≠ 12 → restate claim C's threshold in the
  round record; **never pad rows to 12** (H-1). Accept only a count derived from
  the dossier's own enumeration with the reconciliation stated.
- **HS-2.** If `run-validation.py` is absent or exits ≠ 0 at close → claims C and
  A are **unprovable**; report unprovable, do not accept (`REGIMEN.md:43`).
- **HS-3.** If the c31 audit still exits ≠ 0 or `findings > 0` after the
  integrator's README edit → claim O after_required unmet → stop, do not accept.
- **HS-4.** If K01 could-not-locates and O05 files no owner+reason → claim O leg
  (b) has no disposition; stop. A "carried-with-owner+reason" O05 is acceptable
  per `claims.json:30`; a missing O05 is not.
- **HS-5.** Any freshness axis-move proposed in any fragment → REGIMEN violation
  (`claims.json:18` `freshness_pause_in_force: true`) → stop and report.
- **HS-6.** If `validation.json` lands and the telemetry closing snapshot does not
  → the round is not admissible (`AGENTS.md:32-38`); file the snapshot or record
  `could-not-recover` with owner+reason.
- **HS-7.** If any seat edited filed bytes (`corpus/lessons/*.md`,
  `reports/round-1..32/**`, README in-place against its own convention) → append-only
  violation; re-run the audit on the corrected tree before any verdict.
- **HS-8.** Any fragment asserting C/A legs "verified" before `run-validation.py`
  exists → treat as unprovable-but-better at most, and only with a named
  non-author reviewer (`REGIMEN.md:38-40`).
- **HS-9.** If the O07 baseline receipt is not reproduced **before** integration
  edits, the "zero regressions" threshold (`claims.json:37`) has no baseline and
  cannot be judged → stop rather than judge on a post-hoc baseline.

## §7 — fragment-level census (second pass, 2026-10-19T04:00:16Z)

The wave landed mid-flight; §1's cut covered 3 files, this pass covers what was
on disk at cut 2 — **45 files**, so the fragment-level census is *done for the
landed set*, not owed. Measured:
`grep -rn "to-verify" reports/round-33/ --include=*.md | grep -v X04-honesty.md | wc -l`
→ **69 mark lines across 25 fragment files**; CNE-family lines
(`could-not-evaluate|could-not-locate|could-not-recover`) → **55**.
Per-file mark counts (measured at cut 2, they move as fragments land):
A16 6 · C14 5 · R05 4 · X03 4 · O08 3 · P02 3 · C01 3 · A15 3 · A04 3 · A03 3 ·
S02 2 · S01 2 · O07 2 · K03 2 · C03 2 · A01 2 · S05 1 · S04 1 · K02 1 · C16 1 ·
C07 1 · A02 1.

Mark classes, with the pointers that carry them:
- **actor/attribution unknown** — the transient filed-byte mutation (H-8):
  `A04-bleed.md:143,148,173`; `R05-calib-review.md:104,161,217`;
  `X03-protocol.md:64,80,150`; `A15-audit-draft.md:224`; `S01-op-receipt.md:281`.
- **count provenance ("12")** — `K03-open-items.md:46,101`; `C01-item-01.md:33`;
  `C03-item-03.md:38,284`; `C16-receipt.md:79`; `S02-calib-receipt.md:93`;
  `S04-integration-draft.md:522`; `R05-calib-review.md:44`.
- **pending draft/fragment dependency** — `A16-shonen-material.md:86,101,117`;
  `O08-receipt.md:159,232,299`; `C07-item-07.md:142`; `A15-audit-draft.md:131`;
  `S05-telemetry-draft.md:377`; `S02-calib-receipt.md:126`.
- **command-actor / method caveat** — `O07-baseline-receipt.md:142,181`;
  `S01-op-receipt.md:193`; `A01-province.md:165`; `K02-lessons-census.md:223`.

Reading: the marks are *honest unknowns*, not defects — every one names a scope
or an actor the seat could not see. The risk they create is aggregation: a round
record that reports the marks' conclusions as verified while dropping the
`to-verify` qualifier. The integrator's final scan (HS-12) is the control.

## §8 — finding updates after the wave (supersede §5 where they conflict)

- **H-1 → updated, still live.** K03 published a counting rule
  (`K03-open-items.md:36-53`): literal D13 rows **9** → canonical **12** by
  splitting box-1 conditions 2/3/4 (→3) and the lore pair (→2); it names the
  numeral's origin `to-verify` (`:45-49`). Independent derivations disagree:
  C03 reaches 12 by a *different* expansion (cold-run `N1/N4/N5/N7` → 4; 8+4=12;
  box-1 alone → 11; both → 14 — `C03-item-03.md:34-39`), and R05 reads the
  numeral as the garment-hold count propagated into a row-count position
  ("a count conflation, not a count", `R05-calib-review.md:38-44`). So the ledger
  may legitimately carry 12 rows **by K03's stated rule**; the *numeral's*
  provenance stays unverified and the round record must not present "12" as
  source-confirmed.
- **H-3 → RESOLVED.** K01 located the mismatch: F-X16-3, the `SKILL.md:715`
  audit's closure test for `telemetry/closing-snapshot.json`
  (`K01-falsifier-scout.md:1-12`; `corpus/lessons/round-32.md:36,41,55`). O05
  landed a located-and-bounded disposition with a repoint draft + 7 controls
  (`O05-falsifier-disposition.md:1-12,73-120,221-224`; 277 lines, `test -s` now
  exits 0). This seat independently confirmed the filename exists nowhere
  (`find reports -name "*closing*"` → **0 matches**) and that the live convention
  is `reports/round-{19,25,26,27,28}/telemetry/availability-close-<N>.json`
  (`O05:38-51`).
- **H-9 (new, medium) — the r33 closing snapshot is invisible to the very audit
  it is meant to satisfy.** The `SKILL.md:715` audit globs
  `reports/round-*/availability*.json`; the live matches stop at round 28
  (`ls reports/round-*/availability*.json` → rounds 5, 10, 19, 25, 26, 27, 28),
  and round 33's record is `telemetry/dispatch-declared.json` — not matched. So
  the round-33 closing snapshot is owed by `AGENTS.md:32-38` while no instrument
  can see it is missing. After O05's repoint lands, the instrument should test
  substance (its §4 controls: live 5→0 rows), and the integrator must file the
  r33 snapshot regardless of the glob.
- **H-8 (new, medium) — filed bytes were touched inside the wave window.**
  `reports/round-5/validation.json` and `reports/round-7/validation.json` appeared
  modified at 03:54:15/03:54:18Z (claim-O `error` text replaced by a
  `gate_digest_mismatch` CNE dump; `tested_file_sha256` `0a126b70…`→`455b595a…`)
  and were restored by 03:55:27Z (`A10-receipt.md:59`; `X03:64,80`;
  `R05:104`). This seat verified at 04:00:16Z: `git status --porcelain` for both
  paths empty, `git diff --stat` empty → both match HEAD again. Actor
  attribution is `to-verify` (`A04:148,173`). Consequence: any claim of "zero
  filed-byte writes this round" must carry this named, restored, unattributed
  event.
- **H-10 (new, low) — two tracked-path baselines in play.** The declared round-33
  baseline is 2655 (`claims.json:57`; this seat re-verified 2655 = 2655), while
  r32's scope watch counted 1,870 protected paths and A10 measured the protected
  surface at 1,905 (`A10-receipt.md:64`, A10-F12). Unlabeled, the comparison
  reads as a 785-path breach.
- **Corroborations.** A10-F3 retracts a revision-1 claim that the c31 audit exits
  0 and re-measures exit **1** (`A10-receipt.md:55`) — matching this seat's §4
  measurement independently. A10-F10 records that `corpus/lessons/README.md` is
  pinned twice (`A10-receipt.md:62`; see HS-10), which this seat re-verified
  against live bytes. A10-F4 (`:56`) requires A08's language scan to be re-run
  after the wave — the same currency rule as HS-12.

## §9 — additional honest-stop triggers (addenda to §6)

- **HS-4 (revised).** H-3 resolved: K01 located and O05 filed. New trigger: O05's
  D-1 fix is a **draft** — if the integrator does not apply the repoint, the
  mismatch stays live; the round must record it `fixed-with-draft` or
  `carried-with-owner+reason`, never silently closed (`O05:221-224,252,262-263`).
- **HS-10 (new, high).** The README reconciliation breaks two live pins **by
  construction**: `reports/round-26/run-validation.py:97` `README_BASELINE_BLOB =
  a31870556c733498243b56697896504a2fb3679a` and `reports/round-25/validation.json:1020`
  `input_sha256 = ec7469dadf87…`. This seat verified both match live bytes now
  (`git rev-parse HEAD:corpus/lessons/README.md` → `a3187055…`; `sha256sum
  corpus/lessons/README.md` → `ec7469da…`). A silent edit that leaves the r26 leg
  red is the failure mode (A10-F10). Require a recorded re-pin decision
  (declared repin with before/after digests, or a re-scoped leg) before judging
  claim O's "zero regressions" threshold.
- **HS-11 (new).** If the round record claims "no filed bytes touched", it must
  qualify H-8 (transient r5/r7 mutation, restored, actor unattributed).
- **HS-12 (new, procedural).** Any mark/language/bleed census run before the last
  fragment lands is provisional: re-run the §7 commands (and A08's scan, per
  `A10-F4`) over the final file set before `adj/audit-assembled.md` and the round
  report are finalized.

## Owed

- **Re-census at finalization** (HS-12): this pass covers the 45 files present at
  04:00:16Z; re-run
  `grep -rn "to-verify\|could-not-evaluate\|could-not-locate\|could-not-recover" reports/round-33/`
  plus the seat-out completeness check over `targets.json` outs once the wave
  closes. Owner: integrator.
- **Integrator-only artifacts still missing at cut 2**: `run-validation.py`,
  `calib/open-items-ledger.json`, `adj/audit-assembled.md`, `calib/C15-ledger-draft.json`
  (and, per O05's own `## Owed`, `op/P01-plan.md`). Claims C and A remain
  unverifiable by any seat until the first three exist (HS-2).
- **H-1 provenance**: the "12" derivation remains `to-verify` as to the original
  author's intent (`K03:45-49`; `R05:44`); the ledger may land 12 rows by K03's
  stated rule without settling it.

## Citations

- `REGIMEN.md:25-50,43,57-58` · `reports/round-33/claims.json:18,23-26,29-37,44-50,55-63,70`
- `reports/round-33/targets.json:6-10,15,23,26,45,77,82,83` · `reports/round-33/telemetry/dispatch-declared.json:6,13,15,28`
- `AGENTS.md:11,32-38` · `SCORECARD.md:443-445` · `reports/round-32/final-dossier.md:107,110`
- `reports/round-32/dossier-d13-operator-decisions.md:116,128-138` · `reports/round-32/dossier-d11-shonen-boxes.md:203-208`
- `reports/round-32/scribe/fragment-ledger.md:135,201,215` · `reports/round-32/final-sweep.md:154-162`
- `reports/round-32/run-validation.py:925,1136` · `reports/round-32/validation.json:418,628,768,936`
- `reports/round-29/recount/r27-full-sweep-reproduction.json` (50 CNE) · `corpus/lessons/round-32.md:36`
- `reports/round-25/audit/c31-lessons-index-audit.py:42,119-135,280-317` · `corpus/lessons/README.md:6,35,39-40,97,207,303-307`
- §7/§8 sources (cut 2, 2026-10-19T04:00:16Z): `reports/round-33/op/K01-falsifier-scout.md:1-12`; `op/O05-falsifier-disposition.md:1-12,38-51,73-120,221-224,252,262-263`; `calib/K03-open-items.md:36-53`; `calib/C03-item-03.md:34-39`; `review/R05-calib-review.md:38-44,104,161,217`; `adj/A10-receipt.md:12,17,55,56,59,62,64`; `cross/X03-protocol.md:64,80,150`; `adj/A04-bleed.md:143,148,173`; `adj/A15-audit-draft.md:131,224`; `scribe/S01-op-receipt.md:281`; `corpus/lessons/round-32.md:36,41,55`; `SKILL.md:713-715`; `reports/round-26/run-validation.py:97`; `reports/round-25/validation.json:1019-1021`
- Commands re-run at 2026-10-19T03:56:43Z (outputs in §4): `find reports/round-33 -type f | wc -l`; `sha256sum` on the three round-33 files; `grep -rn "to-verify"` / `"could-not-evaluate"`; `python3 -B reports/round-25/audit/c31-lessons-index-audit.py [--selftest]`; `python3 -B tools/check-gate-battery.py --selftest`; `python3 -B tools/check-craft-exercise.py --selftest`; `python3 -B tools/assemble-culture-d4.py --selftest`; `git ls-files | wc -l`; `git ls-tree -r --name-only 139e3b6 | wc -l`; `git log --oneline -3 -- PROVINCE.md`; `git status --porcelain`; `test -s reports/round-33/op/O05-falsifier-disposition.md`; `python3 -c` out-vs-claims path check.
