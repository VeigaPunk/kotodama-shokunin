# Round 20 — report draft (SCRIBE X19..X20)

- **Round:** 20, operator loop 2 of 3, build round 4 of 4 (64 declared
  workers, provider `opencode-go/deepseek-v4.1-flash` —
  `reports/round-20/claims.json`). **Date:** 2026-10-18.
- **Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. **Baseline:**
  `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d` (round-19 admit). HEAD at draft
  time `122086bce0aa577bec221bb2d37eedf20f4f3ed2` ("round-20: declare claims
  D/O/C (handoff v3 with D4, alias-wart fix, README reconciliation)").
- **Claims:** D / depth (handoff e2e v3: D4 artifacts + claims with
  uncertainty + resolving links); O / operability (per-family era-alias
  resolution; wart closed; D2 byte-identical; re-pin cascade as new rows);
  C / coverage (`corpus/README.md` reconciled command-carried).
- **Counting command:** `python3 reports/round-20/run-validation.py`.
  **This seat ran it with `--check` only** (exit 1, no write); the primary
  receipt `reports/round-20/validation.json` did not exist at the draft stamp
  and this seat neither wrote nor overwrote it. **The runner was revised
  inside the wave:** sha `afdf1198…` at the 13:07Z measurement, `de879cef…`
  at the 13:09Z re-measurement; both revisions read C pass / D fail / O fail,
  with D and O failure sets changing as their seats wrote (the churn is
  disclosed, not smoothed over).
- **Status of this draft:** NON-CANON engineering evidence written against an
  **in-flight tree** — the wave began landing artifacts at 12:56:53Z and was
  still writing at the final stamp (13:13Z). Three runner readings were taken
  (13:07Z, 13:09Z, 13:13Z; runner sha `afdf1198…` → `de879cef…` →
  `566dd75d…`): **C passed at all three; O failed the first two and passed the
  third; D failed at all three** on legs its seat is still working. It admits nothing, certifies no canon, lore receipt,
  source freshness, or real-world clearance, and it is written by the
  X19..X20 scribe seats, not the integrator. The parent owns the final report
  and the LOG/SCORECARD append.

## 1. Runner verdicts across three in-flight readings (measured, not read from prose)

`python3 reports/round-20/run-validation.py --check` — first reading
2026-10-18T13:07Z (runner `afdf1198…`, stdout `.scratch/x19/check.json`);
re-reading 13:09Z (runner `de879cef…`, stdout `.scratch/x19/check2.json`);
final reading 13:13Z (runner `566dd75d…`, stdout `.scratch/x19/check3.json`).
The table is the **first reading (13:07Z)**; the paragraphs below it record the
two later readings:

| claim | verdict at 13:07Z | measured state |
|---|---|---|
| **C / coverage** | **PASS** | README revision 1.5; 199 rows / 199 files; counts 94/19/19/18/29/20; the declared linguistics 20 vs live 19 delta is **named in the README** (`declared_deltas: [{partition: linguistics, declared: 20, live: 19, documented_in_readme: true}]`) |
| **D / depth** | **FAIL** (4 legs) | v1 path exit 1 — the exercise's own `E2E-DIGEST` leg flags `tools/d2-typed-labels.py` as changed since the frozen baseline; `--profile v2` and `--profile v3` are unrecognized arguments (exit 2) — the profile surface has not landed; v3 selftest exit 2; `missing_dependencies: [reports/round-20/<contract-audit-rerun>.md, reports/round-20/handoff/expected.json]` |
| **O / operability** | **FAIL** (8 legs) | adapter selftest still copies the foreign `examples/culture-d2` tree; stale pins in `examples/culture-d4/expected-holds.json` (projector `0da0015f…` vs live `76536a92…`; projection `a59990bb…` vs live `cbcf997f…`) and in `examples/culture-d4/packet.d4.typed.yml` (3 pins unset/`None`); `packet.d4.typed.yml` is not strict JSON; **no round-20 re-pin rows landed** (`reports/round-20/repin/**`, `tools/gates/frozen/round-20/**` empty) |

`filed_rounds` leg (the runner's own guard): **897 files under reports/round-8..19
compared byte-for-byte against the baseline Git blobs — all byte-identical,
0 failures** at all three readings.

**Re-reading at 13:09Z (runner `de879cef…`):** C still **PASS**; **D fail
(6 legs)**; **O fail (6 legs)** — the adapter selftest still copied the foreign
tree and five pins were stale.

**Final reading at 13:13Z (runner `566dd75d…`):** C **PASS** (0 failures); **O
now PASSES** — measured legs: adapter selftest 12/12, D2 projector
byte-identical (`d2_byte_identical: true`), `foreign_tree_copy_in_adapter:
false` (the round-19 wart is closed), D4 gate 19/19, the wart mirror without
`examples/culture-d2` passes, and re-pin rows landed under
`tools/gates/expected/d4-typed-labels-check-gate/r20-post/`; the D3 projector
probe still exits 2 and is recorded informationally. **D still fails (6
legs)** on its own named legs: the v1 exercise exits 2 with `E2E-BASELINE:
frozen baseline not found: reports/round-20/handoff/expected.json`, and
`--profile v2` / `--profile v3` are still unrecognized — the v3 freeze and the
profile surface have not landed. The wave was writing while all three readings
were taken; none is a settled verdict.

## 2. Claim D — depth: handoff e2e v3 (in flight)

**What landed (measured):** the v3 design
(`reports/round-20/handoff/design.md`, 30,773 bytes: extends the v2 envelope
with the D4 furnace-league drill as a third source, twelve D4 claims carrying
`{status, basis}`, the round-19 wart carried as one owner-routed unresolved
claim), the claims map (`handoff/claims-map.md`), the status plan
(`handoff/uncertainty-plan.md`) and a review (`handoff/review.md`). The
runner's D measurement reads the claims map as a *candidate* packet with
**0 rows / 0 statuses** — the packet bytes and the exercise extension have not
landed.

**At the final reading (13:13Z) D still fails (6 legs)** — the v3 freeze
(`reports/round-20/handoff/expected.json`) and the `--profile v2|v3` surface
had not landed; the runner names both.

**What is failing and why:** the projector change for claim O (sha
`0da0015f…` → `76536a92…`) broke the v1 exercise's frozen-read-set digest leg
— an expected coupling between the two claims that the D seat must absorb
(re-freeze or re-scope the digest set). The v2/v3 profile switch
(`--profile v2|v3`) is not in `tools/exercise-handoff-e2e.py` yet
(sha `a21934ad…` at the draft stamp = the baseline bytes).

**Before state (this seat, 12:57:23Z):** v2 green end to end — exit 0,
`fields=16/16 glossary=20/20 findings=0`, packet sha
`6583b6bdbf5e3fe039d1eee1d9f53d63ef09a04e3eeb5c98ae4943ed1771a64f`; the v2
baselines `reports/round-15/handoff/expected.json` (sha `b927db31…`, claims 15:
8 supported / 5 partial / 2 unresolved) and
`reports/round-16/handoff/expected-v2-07.json` (sha `dc75c5d7…`, packet
`kotodama.handoff.d2d3-e2e.v2.build05`).

## 3. Claim O — operability: per-family era-alias resolution (in flight)

**What landed (measured, `tools/d2-typed-labels.py` sha
`0da0015f…` → `de11f031…` → `76536a92…`):** a per-family alias leg —
`packet_family()` / `family_alias_leg()` at `tools/d2-typed-labels.py:2441–2576`:
the D2 family keeps the round-8 path (`declared_era_aliases` +
`era_alias_rows`, reading the D2 components) **byte for byte**; every other
family resolves the alias rules its own packet declares
(`era_reconciliation`, shaped by the same `shape_reconciliation_rows()` used
for the D2 costume block) and, when the packet declares none, records an open
skip with the reason, never importing another family's tree. The O seat's
re-pin row `reports/round-20/wart/expected-v2-07-r20.json` landed at ~13:08Z.
`tools/gates/typed-pipelines.json` was updated (d4 profile pins).

**Measured green after the change:** D2 `--check` byte-identical (exit 0) and
`--selftest` 39/39; the D4 typed packet `--check` exit 0 and typed-pipeline
`examples/culture-d4/packet.d4.yml` **19/19 legs**; the adapter selftest 12/12;
the wart mirror **without** `examples/culture-d2` present passes
`assemble-d4-typed.py --check` (exit 0).

**Measured red at the 13:07Z/13:09Z readings (superseded at 13:13Z):** the
adapter **selftest** still copied the foreign tree
(`tools/assemble-d4-typed.py:418`); five D4 pins were stale against the new
projector and projection bytes; `packet.d4.typed.yml` was not strict JSON; no
re-pin rows existed. **By 13:13Z all of these legs read green** in the
runner's own measurement (see §1).

**Before state (this seat):** `ALIAS_COMPONENT` pinned to the D2 tree at
`tools/d2-typed-labels.py:2316`; the mirror copy at
`tools/assemble-d4-typed.py:410–419`; **106** repo files name the projector sha
`0da0015f…` (the re-pin cascade surface); the D3 projector probe
(`--packet examples/culture-d3/packet.json`) exits 2 with
`P-UNTERMINATED-FLOW` — recorded informationally (the projector has no D3
label surface; the runner's limits say so explicitly).

## 4. Claim C — coverage: corpus/README.md reconciliation (measured PASS)

**Measured by the runner at 13:07Z: PASS, no failures.** Revision **1.5**
(sha `a20b6b263f089364dbfa236afdca58f160954d03d2ef9822c9540ef8ef584f7b`):
199 index rows, 199 files, 0 missing, 0 ghosts; six command-carried counts;
the ten round-19 rows repaired to the entries' own `- topic:` text after
revision 1.4's "0 topic mismatches" was found to be asserted rather than
measured (`reports/round-19/audit/x27-coverage-readme-vs-files.md` §1 cited in
the revision block); receipts `reports/round-20/readme/{reconcile.md,verify.md,gaps.md}`.

**Independent verification (this seat):** a verbatim row-vs-`- topic:`
comparison (joining wrapped topic lines) returns **199 rows, 0 missing,
0 topic mismatches**. A first pass of this seat's own check reported 2
mismatches; both were its own regex artifact on wrapped topic lines, corrected
and re-run. The declared-vs-live linguistics delta (20 vs 19) is real and is
named in the README; no linguistics entry was authored this wave.

## 5. Independent rerun (this seat)

Full record in `reports/round-20/rerun.json`; receipts under `.scratch/x19/`.

- **Regression inventory:** 25 fixed read-only commands → **25/25 green** at
  12:56:21Z (battery exit 0, pass 7 / fail 0 / unevaluable 0; battery selftest
  35/35; D2 projector selftest 39/39; D2/D4 typed assembler selftests 11/11,
  12/12; culture-d3/d4 assemblers 85/85, 81/81; handoff gate selftest; typed
  pipeline D2 16/16, D4 19/19, selftest 12/12; five structural gate
  selftests). Per-command exit and stdout sha256 in `.scratch/x19/inventory.json`.
- **Preservation control (this seat's own):** 892 files under
  `reports/round-8..19` re-measured at 12:58Z and 13:05Z against the 12:55Z
  manifest. **During the wave this control caught a filed-artifact write:**
  `reports/round-9/validation.json` changed at 13:00:55Z (`036f8427…` →
  `50f892b6…`, +594/−64 lines, `acceptance_checks_passed` flipped true→false),
  together with `reports/round-5/validation.json` (13:00:55Z) and
  `reports/round-7/validation.json` (13:00:58Z) — a seat re-running historical
  round validators whose receipt redirect did not take effect. Diffs preserved
  at `.scratch/x19/filed-r9.diff` (sha `3134443d…`) and
  `.scratch/x19/filed-r5-r7.diff`. **By 13:05Z all three receipts were restored
  to their committed bytes** (`git status` clean for those paths; the runner's
  own `filed_rounds` leg reads 897 files byte-identical at 13:07Z).
- **Runner:** `--selftest` 21 controls exit 0; `--check` exit 1 (C pass, D
  fail, O fail); this seat wrote no receipt.
- **Primary receipt:** `reports/round-20/validation.json` did not exist at the
  draft stamp; the runner was revised inside the wave (`afdf1198…` →
  `de879cef…`) and both readings agree at claim level (C pass; D fail; O
  fail).
- **Fragment index:** `reports/round-20/fragment-index.md`, census refreshed
  13:09:56Z (33 artifacts); its own control passes 33/33 with
  duplicate/dropped/missing-path negatives rejected.

## 6. Limits

- All measured artifacts are NON-CANON. This draft certifies no truth, canon,
  lore acceptance, cultural permission, or real-world rights position.
- The draft is a point-in-time reading of an in-flight wave (first artifact
  12:56:53Z; verdicts 13:07Z; draft stamp 13:09Z). Every D/O failure named
  above is the runner's measurement at that stamp, not a prediction; both
  seats were writing while it was taken.
- The C PASS is a point-in-time measurement at runner sha `afdf1198…` on the
  delivered tree; a later README edit needs a re-measurement, not an inherited
  PASS.
- The filed-artifact incident is reported as measured and as restored; this
  seat did not repair it (not its file) and the parent owns any follow-up.
- No historical round validator was executed by this seat; the runner's own
  filed-rounds guard was read, not re-implemented.

## 7. Commands

- `python3 reports/round-20/run-validation.py --selftest` → 21 controls,
  exit 0 (runner sha `afdf1198…`).
- `python3 reports/round-20/run-validation.py --check` → exit 1 at both
  readings; 13:07Z (runner `afdf1198…`): C pass, D fail (4 legs), O fail
  (8 legs) — `.scratch/x19/check.json`; 13:09Z (runner `de879cef…`): C pass,
  D fail (6 legs), O fail (6 legs) — `.scratch/x19/check2.json`.
- `python3 .scratch/x19/inventory.py` → 25/25 green (12:56:21Z).
- `python3 .scratch/x19/before-after.py` → before bundle (12:57:23Z).
- `python3 .scratch/x19/deadline-snapshot.py` → deadline snapshot
  (`.scratch/x19/snapshot.json`).
- `git diff --stat` → README, `examples/culture-d4/typed-labels.d4.yml`,
  `tools/d2-typed-labels.py`, `tools/gates/typed-pipelines.json`.
- `python3 reports/round-20/run-validation.py --check` (13:13Z, runner
  `566dd75d…`) → C pass, O pass, D fail (6 legs); `.scratch/x19/check3.json`.
- `find reports/round-20 -type f | wc -l` → **42** at the final refresh
  (16 → 24 → 33 → 42 between 13:05Z and 13:14Z; the census drift is recorded
  in `reports/round-20/fragment-index.md`, whose own control passes 42/42 at
  13:14:01Z).
