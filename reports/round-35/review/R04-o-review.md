- Seat: R04 | reviewer | claim O | date 2026-10-19 | baseline 4a7aede

# R04 — adversarial review of the R34-N1 hardening (claim O)

Review performed against the live defect site and four executed candidate patch
shapes in isolated `git archive 4a7aede` copies (`.scratch/r04`, `.scratch/r04v`).
The O-block design fragments (O01/O02/O03/O05/O11) did not exist at review time
(parallel seats); this review therefore states the conditions any applied patch
must satisfy, each backed by an observed run, and is owed a re-read of the final
bytes (see `## Owed`).

## 1. The defect, pinned

- Site: `tools/exercise-handoff-e2e.py:3819-3822` (v3 replay read-set leg).
  `:3819` builds `drifted` with `assembly.digests.get(rel)`; `:3822` then indexes
  `assembly.digests[rel]` directly. `assembly.digests` is keyed by the live
  `V3_READ_SET` only (`:3479-3483`), so any baseline `inputs` member outside the
  live read set is `None`-compared at `:3819` (drift) and raises `KeyError` at `:3822`.
- Reproduced (isolated copy, `git archive 4a7aede`):
  `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json`
  → **exit 1, raw traceback on stderr**, `KeyError: 'reports/round-20/handoff/claims-map.md'`
  at `:3822`; no `E2E-*` code emitted, no records printed.
- Cause: the r6 baseline's `inputs` (58 keys) names
  `reports/round-20/handoff/claims-map.md`; live `V3_READ_SET` (`:1935-1959`)
  names `reports/round-34/handoff/declared-in-r7/claims-map.md` (`CLAIMS_MAP`,
  `:184`, slot `:1957`). One-member set difference, measured:
  baseline-not-live = `['reports/round-20/handoff/claims-map.md']`,
  live-not-baseline = `['reports/round-34/handoff/declared-in-r7/claims-map.md']`.

## 2. Scope of the defect: nine filed v3 baselines, not one

Census command (all `reports/**/expected.json` whose `profile` is a renderer
profile, `inputs` keys vs the module's read-set tuples):

```
reports/round-20/handoff/expected.json                     inputs=58 unresolvable=[round-20 claims-map]
reports/round-22/handoff/declared-in/expected.json         inputs=58 unresolvable=[round-20 claims-map]
reports/round-22/handoff/declared-in-r2/expected.json      inputs=58 unresolvable=[round-20 claims-map]
reports/round-26/handoff/declared-in-r5/expected.json      inputs=58 unresolvable=[round-20 claims-map]
reports/round-26/register/v3-baseline-r26/expected.json    inputs=58 unresolvable=[round-20 claims-map]
reports/round-26/remainders/v3-baseline-r26/expected.json  inputs=58 unresolvable=[round-20 claims-map]
reports/round-27/pinsweep/v3-baseline-r27/expected.json    inputs=58 unresolvable=[round-20 claims-map]
reports/round-28/pinsweep/v3-baseline-r28/expected.json    inputs=58 unresolvable=[round-20 claims-map]
reports/round-30/handoff/declared-in-r6/expected.json      inputs=58 unresolvable=[round-20 claims-map]
reports/round-34/handoff/declared-in-r7/expected.json      inputs=58 unresolvable=[]
reports/round-26/remainders/r4-twin/expected.json          inputs=0  unresolvable=[]
reports/round-11/handoff/expected.json (v1)                inputs=21 unresolvable=[]
```

- Reproduced live for four of the nine (r20, r26-register, r28, r30/r6) — all
  four die with the identical traceback at `:3822`. The other five are
  census-predicted (same code path, same member) and are marked **predicted, not
  executed** here.
- `reports/round-26/remainders/r4-twin/expected.json` has `inputs={}` → no crash
  (observed: exit 2, clean summary, no traceback).
- `reports/round-25/v3-supersession/declared-in-r4/expected.json` is named in
  `repin.json`'s history list but carries no `profile`/`inputs` (keys:
  `binding/census/date/declared_by/delta/kind/live_measurements/packet_sha256/
  packet_version/parent/reason/revision/v2_subset_digest`) — it is not a
  renderer baseline row and is not replayable by this tool at all. The hardening
  must not be validated against it.

## 3. Q1 — does the catch change any other path? Four shapes, executed

All four run in `.scratch/r04v` (isolated archive; in-tree bytes untouched),
against the r6 row unless stated.

| # | Shape | Observed |
|---|---|---|
| S1 | `.get(rel)` only in the record string | exit 1; `FAIL input-digest: reports/round-20/handoff/claims-map.md: frozen 4b1b9a35a18f… live not in the live read set`; then `handoff-v3: E2E-DIGEST: 1 read-set file(s) changed since the baseline was frozen: reports/round-20/handoff/claims-map.md` |
| S2 | classify first, `raise Failed("E2E-READSET", …)` | exit 1; `handoff-v3: E2E-READSET: 1 baseline read-set member(s) are outside the live read set: reports/round-20/handoff/claims-map.md` |
| S3 | measure-on-demand (the `:3648`/`:1340` idiom copied here) | exit 1; **`OK input-digest: 58 read-set digests match the frozen baseline`** then `FAIL frozen-packet: assembled 45f571326176… vs frozen 6ced88ad009f…` and `handoff-v3: E2E-DIGEST: the assembled packet does not match the frozen packet digest` |
| S4 | broad `except KeyError` in the outer handler + injected unrelated fault | on the **green r7 chain**: exit 1, `handoff-v3: E2E-READSET: E2E-READSET: 'unrelated-injected-key'`, summary still printing `fields=16/16 … packet_sha256=45f5713261762a95…`; same fault without the catch crashes with a traceback |

Findings:

- **S3 must not be the chosen shape.** The round-20 map still exists on disk with
  exactly its r6-frozen digest (measured: `4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8`,
  equal to `reports/round-30/handoff/declared-in-r6/expected.json`'s frozen value),
  so measuring it on demand yields "no drift" and the superseded row is evaluated
  **as if live**, refusing later for a different reason and printing a read-set
  parity record that is false for the live read set. That is the exact hazard the
  r6 control exists to prevent.
- **S1 stops the crash but keeps a false statement**: "read-set file(s) changed"
  asserts a comparison that was never made for that member. It also collapses the
  new class back into `E2E-DIGEST`, which the claim explicitly distinguishes from
  the "flipped-sha expectation" negative control (`claims.json:45`).
- **S2 is the recommended shape** — one new named code, relative path named,
  exit code unchanged (see item 1 below).
- **A broad catch is harmful**: S4 shows an unrelated `KeyError` (injected at the
  end of the v3 try body, after the preservation check; probe, not a real-world
  repro) being relabelled `E2E-READSET` while the row's read set is perfectly
  resolvable. The catch must be a *classification*, not an exception handler — or,
  if a handler is used, it must be a single-expression `try` around `:3822` only.
- Paths the patch must leave byte-identical: the freeze path is independent
  (`v3_freeze` builds its own assembly, `:3979-3984`; `inputs` is built from the
  live read set at `:4020`, so a superseded row cannot be produced by freezing);
  the m12a/m12b/scan-expectation/missing-artifact controls (`:4414-4457`) must
  keep their exact codes and exits; the preservation leg (`:3958-3968`) is
  unaffected.
- Direction of the comparison must stay one-way: a live member the baseline does
  not name (the r7 map under the r6 baseline) is correctly ignored today. The fix
  must not start reporting live-only members — every pre-r34 row, and every future
  supersession of the r7 row, would emit a second finding class.
- **v1 twin**: `:1436-1440` carries the identical pattern. No filed v1 baseline
  currently triggers it (round-11 baseline: 21/21 resolvable — census above), so
  it is latent. A v1-only-vs-both choice is the integrator's; if left unfixed, the
  round record should name it as known-latent with the reason, not leave it
  unmentioned.
- **Correct precedent already in the file**: the v2 path does it right —
  `baseline["inputs"].get(rel)` compared against a measured digest with an explicit
  message (`:1844-1849`). Mirror that, do not mirror `:3648`.

## 4. Q2 — does the named diagnostic leak internals it shouldn't?

- The *current* failure mode is the leaky one: an uncaught traceback prints the
  absolute host path (observed:
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch/r04v/tools/exercise-handoff-e2e.py:3822`),
  `main()` internals and the `KeyError` repr. The hardening reduces host-layout
  exposure; it does not add any.
- Message requirements for the new diagnostic (all satisfied by S2 as run):
  1. repo-relative path only, no absolute `root`/`baseline_path`/tempdir echoes.
     Do **not** copy the baseline leg's form: `E2E-BASELINE: frozen baseline not
     found: /home/vgpnk/…/nope.json` (`:3775`, observed) prints an absolute path.
  2. frozen digest truncated as the file already does it (`str(...)[:12]…`,
     `:3822`/`:1440`) — the full 64-char digest is already public in the baseline
     file itself (`repin.json` `stale_pin`), so naming the prefix adds nothing.
  3. no file-content excerpts, no dump of the baseline `inputs` map, no packet or
     claim payload — name the member list bounded, as S2 does
     (`', '.join(unresolvable[:3])`).
  4. no traceback, no exception repr in the message (the docstring's own promise:
     "Exit codes (stable messages, no traceback)", `:89-93`).
  5. add the code to the documented list at `:89-93`; that docstring is the
     tool's contract and the round-35 validator/report cite it.

## 5. Integration obligations the applied patch must meet

1. **Exit code (adjudication item).** Recommend `Failed` → **exit 1**, matching
   the class-1 convention and, decisively, keeping the filed control true:
   `reports/round-34/handoff/repin.json:19-21` records `"exit": 1` for this exact
   command, and `SCORECARD.md:615` / `LOG.md:3630` record "exit 1, KeyError
   mechanism". Choosing `BaselineError` (exit 2) is defensible on the
   "could-not-evaluate" reading (`:89-93`) but falsifies those filed exit values
   and would require an explicit reading-change row. Either way the *mechanism*
   string is superseded — the round-35 record needs a supersession row naming
   `repin.json:21` (precedent: the repin's own `reading_changed_not_verdict` list,
   `repin.json:45-47`), and `SCORECARD.md:615,621` / `LOG.md:3612,3630` carry the
   old mechanism too.
2. **Mixed baselines.** If a baseline is both unresolvable *and* drifted, raise
   `E2E-READSET` first and say drift was not evaluated (an unresolvable row cannot
   be evaluated; a digest verdict about it would be unverifiable). Keep the pure
   drift leg (`:3819-3823`) exactly as is — the m12b control depends on it.
3. **Name the member(s)** so a validator can regex them; for the r6 row the exact
   expected token is `reports/round-20/handoff/claims-map.md`.
4. **Diagnostic visibility under `--quiet` (new finding, likely round-35
   self-inflicted failure).** The claim's counting command uses `--quiet`
   (`claims.json:48`), but the code and message are printed only when not quiet:
   `if err and not args.quiet: print(...)` (`:4603-4604`). Observed with the S2
   patch: `--quiet` on the r6 row prints only
   `handoff-v3: exit=1 fields=? glossary=?/20 findings=? links=? claims=? statuses=? v2_subset=unequal alias_leg=? packet_sha256=(not assembled)`
   — **no `E2E-READSET` string anywhere on stdout**. Fix one of: validator leg
   drops `--quiet`; or the quiet summary carries the code (`exit=1 code=E2E-READSET`).
   As written, claim O's own command cannot demonstrate "named diagnostic".
5. **Selftest controls (O02).** The superseded-row control is constructible by the
   established precedent at `:4440-4449` (hand-edit a frozen baseline field, then
   re-sign with `v3_baseline_digest`). Un-re-signed edits die earlier at `:3793`
   (`E2E-BASELINE`, the m12a control, `:4414-4422`) and would test the wrong leg.
   The "preserved E2E-DIGEST digest-mismatch path" already exists as m12b
   (`:4424-4430`) — the two *new* controls should be (a) the READSET refusal and
   (b) the mixed unresolvable+drifted ordering, not a re-spelling of m12b. Note
   the renderer selftest prints `plus {len(results) - 1} controls` (`:4464`):
   adding controls changes a printed number, so any receipt/validator quoting it
   must be re-derived. The `selftest: N/N checks passed` strings belong to other
   tools (the witness at `:3468-3473` parses the D2/D4 legs), not to this one.
6. **R34-N1 ownership.** `repin.json:49-51` routes it to "renderer hardening
   (future round)" with state `routed`; this round is that round. The round-35
   record should close it with evidence (new code + the r6 replay output) or carry
   it with a named reason — not leave the state stale.
7. **Freeze bytes.** The patch must not touch
   `reports/round-34/handoff/declared-in-r7/**` (pinned; `claims.json:70`). The
   replay path writes nothing in-tree: `diff -r --brief .scratch/r04 .scratch/r04v`
   after all runs showed only the tool file differing, and no `reports/round-35`
   directory was created in the archive copy (the in-run control is the
   preservation leg, `:3958-3968`).

## 6. Not reviewed

- The actual patch bytes (O01) and the isolated verifications (O03/O05/O11) were
  absent at review time; §7 re-reviews the design fragments that landed later
  (P02, O02, O08, K03). Items 1-7 and §7 are the acceptance conditions; if the
  applied patch differs from them, the difference — not this review — decides, and
  the divergence should be recorded.

## 7. Re-review against the O-block design as it landed (P02, O02, O08, K03)

The design fragments arrived after §1-6 were written; read against them:

- **Independent convergence.** K03 reproduces the same traceback at `:3822` and the
  same exit-1-with-empty-stdout reading (`scout/K03-keyerror-path.md:19-38`), and
  flags the same caveat I would have raised — the pre-patch `1` is CPython's
  uncaught-exception exit, not the tool's own code (`:36-38`, `tools/…:112-114`).
  P02 chooses `E2E-READSET` + exit 1 (`Failed`) with the ordering stated as
  load-bearing (`plan/P02-oa-plan.md:57-64`, `:103-104`), which is my S2 shape and
  my item 2. O02 binds the same five-point observable contract and places the guard
  before `V3Assembly` so the refusal is cheap (`op/O02-controls.md:48-58`,
  `:88-101`). The guard as written (`rel not in set(V3_READ_SET)`) is a pure
  classification, so the S4 broad-catch hazard cannot arise by construction.
- **One genuine disagreement, flagged not averaged.** O08 argues exit 2 is the
  convention-correct class (`op/O08-validation-legs.md:159-168`: an unresolvable
  baseline member is a could-not-evaluate, cf. `E2E-BASELINE`), accepts `{1, 2}`
  and would record the `claims.json:48` "(expect: exit 1)" string as a named
  deviation if 2 lands (`:169-174`). P02/O02/K03 pin exit 1. My recommendation
  stands at **exit 1**, and the tie-breaker is not taste: `repin.json:20` files
  `"exit": 1` for this command, and `SCORECARD.md:615` / `LOG.md:3630` file the
  same reading — landing exit 2 would falsify a filed value and needs a
  reading-change row naming `repin.json:20`, not only the `claims.json` deviation
  O08 proposes. The convention argument is worth routing as a question about the
  `:89-93` taxonomy (it should arguably gain a "superseded row" clause either way),
  not absorbing into this round.
- **A trade the guard creates, stated rather than hidden.** Firing before the
  digest leg means a superseded row's *resolvable* members are never digest-checked
  (O02 asserts this deliberately: no failed `input-digest` row, `:118-119`,
  `:142`). That is acceptable — a superseded row cannot be evaluated — but a row
  that is both superseded and drifted reports only `E2E-READSET`; the round record
  should carry that as a stated limit (the message does say "the row is
  superseded").
- **Control design meets the conditions in §5 item 5**: the superseded-row control
  re-signs the edited baseline with `v3_baseline_digest` (`op/O02-controls.md:137`)
  and the un-re-signed variant is covered by m14a (`:185-204`), so both the
  integrity leg and the new leg are pinned; m13b additionally makes the claim's
  counting command executable inside the suite (`:120-124`). O02's §7 acceptance
  legs match my items 3 and 4 (`:270-273`).
- **Count discipline.** O02 predicts 43 controls (39 + 4 leg lines, `:251-252`)
  while O08 sets the floor at ≥ 41 with content anchors (`:183-192`) — O08's shape
  is the right one for the validator; a pinned 43 would make a third corroborating
  control read as a failure. My own run of the pristine 4a7aede copy:
  `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` → exit 0,
  header `… plus 39 controls:`, 40 `^  - ` result lines (confirms O08:183-184's
  pre-patch numbers).
- **Pre-existing redness the patch must not be blamed for.** O02 records the v1
  default chain as red at HEAD (`E2E-DIGEST: 1 read-set file(s) changed …:
  tools/d2-typed-labels.py`, `op/O02-controls.md:259-266`); independently confirmed
  by my run of the pristine copy — `--profile v1 --quiet` → exit 1 with
  `handoff-e2e: exit=1 fields=? glossary=?/20 findings=? packet_sha256=(not assembled)`
  (the v1 quiet branch suppresses its code too, `:4554`, which is the same gap as
  item 4 on the v1 side). No leg may treat "v1 green" as a patch-regression
  baseline, and the
  v1 latent index at `:1440` stays out of this claim's scope (O02 names it for the
  regression census — the same conclusion as my §3 bullet).

## Owed

Still owed — the applied patch bytes and their independent verifications were not
in the tree when this fragment was written:
`reports/round-35/op/O01-patch-draft.md`, `reports/round-35/op/O03-isolated-verify.md`,
`reports/round-35/op/O05-verify.md`, `reports/round-35/op/O11-verify-2.md` (the
integrator completes). Check the applied patch against §5 items 1-7 and §7:
the exit-code choice (1 vs 2, with `repin.json:20` as the tie-breaker), the
docstring code-list update (`:89-93`), whether the `--quiet` diagnostic print is
hoisted (`:4603`), and that the guard is a classification rather than a broad
`except KeyError`. `op/O02-controls.md`, `op/O08-validation-legs.md`,
`plan/P02-oa-plan.md` and `scout/K03-keyerror-path.md` have since been re-read in
§7 and are no longer owed.

## Citations

- `tools/exercise-handoff-e2e.py:184` (`CLAIMS_MAP` = declared-in-r7 map),
  `:1935-1959` (`V3_READ_SET`, `:1957` claims-map slot), `:3479-3483`
  (`V3Assembly.digests` keyed by the live read set), `:3648` and `:1340`
  (the `.get() or measure()` idiom), `:3772-3804` (`v3_load_baseline`;
  `:3775` absolute-path message), `:3816-3824` (`:3819` drift, `:3822` KeyError
  site), `:3861` (tempdir path in a record detail), `:3933-3947` (frozen
  packet/twin), `:3958-3968` (preservation leg), `:3971-3976` (v3 handlers),
  `:3979-3984` (`v3_freeze` independent of the replay leg), `:4020` (`inputs`
  built from the live read set), `:4414-4457` (m12a/m12b/scan/missing controls),
  `:4440-4449` (re-sign precedent), `:4459-4467` (control count printed),
  `:1844-1849` (v2 correct pattern), `:1436-1440` (v1 twin defect),
  `:1352-1382` and `:1365-1372` (`run_gate`, `E2E-DATA` guard), `:3468-3473`
  (`v3_selftest_witness`), `:89-93` (documented exit-code classes),
  `:112-114` (`EXIT_PASS/FAIL/UNEVALUATED`), `:4603-4604` (`--quiet` suppresses
  the code), `:4175-4193` (selftest calls into `v3_exercise`).
- O-block design fragments re-read in §7: `reports/round-35/plan/P02-oa-plan.md:57-64,103-104,105-120`
  (exit 1 + `E2E-READSET`; the `--quiet` companion edit),
  `reports/round-35/op/O02-controls.md:48-58,88-101,118-124,137,185-204,251-266,270-273`
  (five-point contract, guard placement, control fixtures, count prediction, v1
  redness), `reports/round-35/op/O08-validation-legs.md:53-66,159-174,183-192`
  (the O1 leg, the exit-2 argument and its deviation policy, the count floor),
  `reports/round-35/scout/K03-keyerror-path.md:19-38,107-111` (traceback, the
  uncaught-exception exit caveat, the exit-1 anchors).
- My own §7 measurements, pristine `git archive 4a7aede` copy `.scratch/r04`:
  `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` → exit 0,
  header `… plus 39 controls:`, 40 `^  - ` lines;
  `python3 -B tools/exercise-handoff-e2e.py --profile v1 --quiet` → exit 1,
  `handoff-e2e: exit=1 fields=? glossary=?/20 findings=? packet_sha256=(not assembled)`.
- `reports/round-34/handoff/repin.json:19-21` (filed r6 control: exit 1, KeyError
  mechanism), `:45-47` (`reading_changed_not_verdict` precedent), `:49-51`
  (R34-N1 routed).
- `reports/round-30/handoff/declared-in-r6/expected.json` (`inputs` 58 keys incl.
  the round-20 claims-map), `reports/round-34/handoff/declared-in-r7/expected.json`
  (58 keys, none unresolvable).
- `reports/round-25/v3-supersession/declared-in-r4/expected.json` (not a renderer
  baseline: no `profile`/`inputs`).
- `SCORECARD.md:615`, `SCORECARD.md:621`, `LOG.md:3612`, `LOG.md:3630`
  (filed "exit 1, KeyError mechanism" readings).
- `reports/round-35/claims.json:37-52` (claim O), `:48` (the `--quiet` counting
  command), `:67-73` (non-goals).
- Commands run (all in isolated `git archive 4a7aede` copies under `.scratch/`,
  never in-tree; no filed runner executed):
  - `git archive 4a7aede | tar -x -C .scratch/r04` then
    `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json`
    → exit 1, traceback, `KeyError: 'reports/round-20/handoff/claims-map.md'`.
  - Same command for `reports/round-28/pinsweep/v3-baseline-r28/expected.json`,
    `reports/round-26/register/v3-baseline-r26/expected.json`,
    `reports/round-20/handoff/expected.json` → identical exit 1 + KeyError;
    `reports/round-26/remainders/r4-twin/expected.json` → exit 2, no traceback.
  - Census script (module import + `reports/**/expected.json` walk) → the table in
    §2; digest equality check for the round-20 claims-map
    (`4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8`).
  - `.scratch/r04v` variants S1/S2/S3/S4 (+ S4-nowrap control) as tabulated in §3;
    `diff -r --brief .scratch/r04 .scratch/r04v` → only the tool file differs.
