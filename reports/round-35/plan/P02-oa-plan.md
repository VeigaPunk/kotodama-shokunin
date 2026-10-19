- Seat: P02 | planner | claim O (+ A-claim audit checklist) | date 2026-10-19 | baseline 4a7aede

# P02 — O hardening design + A audit checklist

Method: reproduced the R34-N1 defect in-tree (renderer non-freeze modes are
permitted in-tree; no `--freeze` was run, no filed runner was executed), read
the catch site and its surroundings, measured the current selftest and the r7
default chain, and derived the touched-surface census from the round-33/34
commits (`git diff --name-status`) because K04's fragment is not yet written.
Every line cite is HEAD 4a7aede (`tools/exercise-handoff-e2e.py` is the
renderer unless stated).

## 1. Defect anatomy (R34-N1) — measured, not inferred

Reproduced, command as filed in the claim:

```
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
  --baseline reports/round-30/handoff/declared-in-r6/expected.json
→ Traceback … KeyError: 'reports/round-20/handoff/claims-map.md'
   at tools/exercise-handoff-e2e.py:3822 in v3_exercise
```

Mechanism, two lines apart:

- `3822: … live {assembly.digests[rel][:12]}…` — unguarded index.
- `3819: drifted = [rel for rel, digest in baseline["inputs"].items() if assembly.digests.get(rel) != digest]`
  — `.get` returns `None` for a baseline member that is not a current
  read-set member, so the member *enters* `drifted`; line 3822 then indexes
  the same dict it just failed to find a key in. `assembly.digests` is keyed
  strictly by `V3_READ_SET` (`3478-3485`), so any baseline member outside the
  current read set is guaranteed absent.

Read-set skew is exactly one key. Comparing the two baselines:

```
only in r6: ['reports/round-20/handoff/claims-map.md']
only in r7: ['reports/round-34/handoff/declared-in-r7/claims-map.md']
common changed digests: []   (58 members each)
```

`CLAIMS_MAP` was re-pointed at `184` by round 34 (`git show 4a7aede -- tools/exercise-handoff-e2e.py`),
and `reports/round-20/handoff/claims-map.md` is still filed (24,888 bytes,
2026-10-18) — so the member is **superseded, not missing**. That distinction
is what the diagnostic must carry.

Exit code alone cannot detect the fix: the unhandled traceback also exits 1.
Any acceptance leg must regex the named code and assert `Traceback` is absent.

## 2. Convention to mirror (choice made, not invented)

The renderer already declares its own contract at `88-93`: *"Exit codes
(stable messages, no traceback): 0 clean; 1 mismatch — `E2E-DIGEST`,
`E2E-COUNT`, `E2E-GATE`, `E2E-SCAN`, `E2E-UNC`, `E2E-LINK`; 2
could-not-evaluate — `E2E-ARTIFACT`, `E2E-BASELINE`, `E2E-DATA`."*

Decision: **`E2E-READSET`, exit 1 (`Failed`)**, naming every unresolvable
member. Rationale: the row is not *unreadable* and the baseline is not
*tampered* — the replay is a positive mismatch of baseline-against-revision,
which is the `Failed` class (`1`), matching the claim's counting command
("expect: exit 1, named diagnostic"). Rejected alternative: `E2E-BASELINE` /
exit 2 (`Unevaluatable`), which would be the better semantic if a superseded
row were a could-not-evaluate of the *live* revision; the claim pins exit 1
and `E2E-READSET` explicitly, so the design follows the claim and records the
alternative here rather than silently deviating. Also rejected: folding the
case into `E2E-DIGEST` (r34's own repin.json notes "the designed E2E-DIGEST
leg is unreachable for this class" — the class needs its own name).

## 3. Where the catch lands — design sketch (O01 owns the exact diff)

Replace `3819-3823` (nothing else in the drift check moves):

```python
        drifted = [rel for rel, digest in baseline["inputs"].items() if assembly.digests.get(rel) != digest]
        if drifted:
            superseded = [rel for rel in drifted if rel not in assembly.digests]
            for rel in drifted:
                if rel in assembly.digests:
                    record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
            if superseded:
                raise Failed(
                    "E2E-READSET",
                    f"{len(superseded)} baseline read-set member(s) are not in this revision's read set: "
                    f"{', '.join(superseded[:3])} — this baseline row is superseded by a read-set move; replay it against the revision it was frozen at",
                )
            raise Failed("E2E-DIGEST", f"{len(drifted)} read-set file(s) changed since the baseline was frozen: {', '.join(drifted[:3])}")
        record("input-digest", True, f"{len(V3_READ_SET)} read-set digests match the frozen baseline")
```

Design properties, each deliberate:

- The pure-drift branch keeps its message **byte-identical** to the current
  `3823` (`"{n} read-set file(s) changed since the baseline was frozen: …"`)
  and its code (`E2E-DIGEST`), so `m12b` (`4424-4430`), `m8` (`4432-4438`)
  and every filed reading of that message stay valid.
- Drift among *resolvable* members is still recorded before the raise, so a
  mixed baseline (one superseded + one drifted member) hides nothing.
- Precedence is deterministic: superseded members decide the code, resolvable
  drift is reported in `records`; no ordering depends on dict iteration.
- The diagnostic names up to three members with the full path (the r6 case
  names `reports/round-20/handoff/claims-map.md` verbatim).
- No internals leak: the message carries baseline/read-set facts only — no
  traceback, no root path, no digest material beyond the existing convention.

## 4. Mandatory companion edit: `--quiet` must still name the diagnostic

`main` prints the failure line only under `if err and not args.quiet:` at
`4603` (v3 branch; the v1/v2 twins are `4554`/`4515`). Under `--quiet` the
run would exit 1 with the summary line only — the claim's own counting
command (`--quiet`, "expect: exit 1, named diagnostic") could not observe
`E2E-READSET`. The v3 branch's guard must become `if err:` (one-line change;
v1/v2 may follow for symmetry but are not required by the claim — flag to
R04 as a scope choice, default: v3 only, minimal blast radius).

Measured, not inferred (tampered-baseline control in `TMPDIR`, same run both
ways — `--quiet` prints the summary line only, the diagnostic line is
suppressed):

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline <tampered>.json
handoff-v3: exit=2 fields=? glossary=?/20 findings=? links=? claims=? statuses=? v2_subset=unequal alias_leg=? packet_sha256=(not assembled)
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline <tampered>.json | tail -1
handoff-v3: E2E-BASELINE: baseline integrity digest mismatch — the baseline file was edited without re-freezing …
```

Note the summary line also degrades to `packet_sha256=(not assembled)` and
`fields=?` on any early failure, so the summary alone can never carry the
diagnostic — the `if err:` change is load-bearing, not cosmetic.

## 5. Docstring / prose sweep — scoped, with one hazard

- `34` and `57` still name `reports/round-20/handoff/claims-map.md` after the
  r34 repoint (the repin edit-set named `2290` and `2566`, not these). They
  are module-docstring prose, **not rendered** — safe to sweep to `CLAIMS_MAP`.
- `2700` is **rendered bytes**: its string is emitted into §1 of the packet,
  and the frozen r7 `packet.md:3` contains it verbatim ("the twelve D4 rows
  are carried from `reports/round-20/handoff/claims-map.md`"). Sweeping it
  changes `packet_sha256` → the r7 baseline would fail `E2E-DIGEST`, and
  re-freezing declared-in-r7 is forbidden this round. **Do not touch `2700`.**

Named finding **F-P02-1** (routed, owner: integrator / next round): the r7
frozen packet is internally inconsistent — `packet.md:3` (prose) names the
pre-move round-20 map while `packet.md:95` and `packet.md:113` (artifact
manifest) name `reports/round-34/handoff/declared-in-r7/claims-map.md`. The
frozen bytes cannot be corrected without a re-freeze, so this is recorded, not
fixed. A01 should confirm and file it as a per-surface finding, not a bleed.

Named finding **F-P02-2** (routed, owner: renderer hardening, same round as
the patch): stale docstring cites `34`, `57` (fixable now, item above).

## 6. Freeze-bytes safety argument

The patch touches: the drift check (`3819-3823`), the v3 failure print
(`4603`), and optionally docstring `34`/`57`. `v3_freeze` builds `inputs`
from `V3_READ_SET` (`4020`) and the packet from `V3Assembly`/`v3_build_packet`
— none of the touched lines feed either. Therefore the frozen r7 bytes and
`packet_sha256` are invariant under the patch. Measured control at baseline:

```
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
→ handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105
  claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed
  packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
```

which matches `reports/round-34/handoff/repin.json` row
`R34-D-default-pointer.control` — so post-patch equality on this line is a
valid regression check.

## 7. Selftest control list (O02 implements; insert after `4424-4430`)

Current state, measured: `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest`
→ exit 0, summary line `selftest: OK — positive run (…) plus 39 controls:`,
40 result lines. Fixture helpers: `v3_build_fixture_root` (`4133-4144`, copies
the read set from the live root) and `v3_freezed_copy` (`4147-4151`, copies
the fixture and re-freezes a fresh baseline into it) — controls are
self-contained and do not read the live r7 frozen dir. Anchor for the insert:
the unique string `v2_root, _ = v3_freezed_copy(fixture, control_dir, "retouched-v2")` (`4433`).

- **N1 — superseded-row refusal (the new leg).**
  `v3_freezed_copy(…, "superseded-row")`; load `expected.json`; move the
  member key (`edited["inputs"]["reports/round-20/handoff/claims-map.md"] = edited["inputs"].pop(CLAIMS_MAP)`);
  re-sign with `v3_baseline_digest`; write back. Assert
  `(code, err) == (EXIT_FAIL, "E2E-READSET")` and that
  `records[-1]["detail"]` contains the member path. This is the same skew
  shape as the r6 row (renamed member key), so it pins the claim's case
  without reading filed r6 bytes.
- **N2 — preserved digest-drift branch (negative control).**
  `v3_freezed_copy(…, "re-signed-drift")`; set
  `edited["inputs"][D4_TYPED_LABELS] = "0" * 64` (an in-read-set, resolvable
  member); re-sign; write back. Assert
  `(code, err) == (EXIT_FAIL, "E2E-DIGEST")` — i.e. the new superseded branch
  did **not** swallow the drift branch — and that the detail names the member.
- **N3 — optional, mixed precedence.** One superseded + one drifted member in
  one re-signed baseline → code is `E2E-READSET` and `records` still carries
  the resolvable drift row. Include only if O01's diff keeps the record-then-raise
  shape from §3; if it does not, the control would encode a weaker design.

After N1+N2: 42 result lines, summary `plus 41 controls`. Thresholds in
`claims.json` ("selftest N/N") should therefore read 41 controls / 42 lines,
not an inherited 39/40 — the integrator should state the measured number, not
a predicted one.

## 8. Acceptance legs for `run-validation.py` (handoff to O08/S04)

1. **r6-row replay:** run the claim's command; require exit 1, require
   `E2E-READSET` in `stdout+stderr`, require the literal member path
   `reports/round-20/handoff/claims-map.md` in the same capture, and require
   `Traceback (most recent call last)` **absent** (this is the leg that
   distinguishes the fix from today's defect, which also exits 1).
2. **r7 default chain:** `--profile v3 --quiet` exits 0 and the summary line
   still carries `packet_sha256=45f5713261762a95…` (freeze bytes unmoved).
3. **Selftest:** exit 0 and the measured control count from §7.
4. **Negative controls:** N2's `E2E-DIGEST` plus the pre-existing `m12a`
   (`4414-4422`, flipped `packet_sha256` without re-signing → exit 2
   `E2E-BASELINE`) and `m12b` (`4424-4430`, tampered read-set member → exit 1
   `E2E-DIGEST`).

Regression census to keep green (handoff to O04): positive run `4175-4182`,
foreign-cwd isolation `4184-4193`, `m11` `4379-4395`, the gate/malformed
matrix `4200-4300`, `m6`/`m2b` `4344-4377`, `m12a`/`m12b` `4414-4430`, `m8`
`4432-4438`, scan-expectation `4440-4449`, missing-artifact `4451-4457`.

## 9. A-claim audit checklist (per surface, with the scan recipe)

Surfaces derived from `git diff --name-status da68a6d~1 da68a6d` (r33) and
`git diff --name-status 4a7aede~1 4a7aede` (r34); K04's census fragment is
absent, so A01–A06 should reconcile against this list and R06 should re-derive
it independently.

| # | Surface | Owner seat | Checks |
|---|---|---|---|
| 1 | `reports/round-34/handoff/declared-in-r7/{packet.md,expected.json,twin.json,freeze.txt,claims-map.md}` | A01 | negation-only canon/clearance language; manifest rows resolve; **F-P02-1** confirmed |
| 2 | `reports/round-34/handoff/repin.json` | A01 | R34-N1/N2 routed-not-absorbed (repin.json `named_findings`); "pins integrity, never truth/clearance" language |
| 3 | `tools/harness/receipt_guard_adoption.py` + `reports/round-34/op/adoption-inventory.json` | A02 | in-lane ownership; inventory `root` is the lane repo only (inventory:109) |
| 4 | `examples/culture-d3/{README.md,handoff.md}`, `examples/handoff-packet.sample.{md,yml}` (r33) | A03 | digest repoints correct; no lore-asset or rights claims |
| 5 | `SKILL.md`, `AGENTS.md` (r33 edits; `AGENTS.md` excised content) | A04 | no cross-domain protocol bleed; PROVINCE conformance |
| 6 | `corpus/knowledge/linguistics/register-lexicon-ceilings.md` + `reports/round-34/calib/*`, `reports/round-34/craft/*` | A05 | box-1/reissue records keep bilateral items routed, not absorbed |
| 7 | `reports/round-33/adj/contract-read-record.md` | A05 | contested items routed with owners |
| 8 | `corpus/lessons/README.md` (r33 revision 3) | R09/A05 | census consistency (R09 owns the counting question) |
| 9 | `tools/exercise-handoff-e2e.py` (r34 edit + this round's patch) | A04/A02 | patch introduces no cross-domain language; **F-P02-2** stale docstring cites `34`,`57`; `2700` left alone |

Per-surface recipe (run each; record observed output, not a summary):

- Language scan: `grep -nEi "canoniz|canon |clearance|rights ruling|promot|accept(ed|ance)|approved" <surface>`
  — classify each hit as negation/routing (pass) or assertion (finding).
  Known negation-context examples that must **not** be false-flagged:
  `reports/round-34/handoff/declared-in-r7/claims-map.md:61` ("not canonized",
  "no real-language clearance … is claimed"), `:141`/`:142` ("no residual is
  promoted").
- Ownership scan: `grep -rnE "world.?bible|chousa|kake|kotoba|game-dev" <surface>`
  plus a write-path check (no `open(...,"w")`/`write_text` target outside the
  lane repo).
- PROVINCE accuracy (A06/A11): `PROVINCE.md:9-14` owns list vs the tree — the
  new tool (`tools/harness/receipt_guard_adoption.py`), the r7 packet under
  `reports/round-34/handoff/`, and the renderer repoint are all in-lane
  artifacts; `PROVINCE.md:16-20` refuses list (canon, rights rulings, game
  mechanics, general source method, web publishing, prompt/skill craft) is
  unchanged and still accurate at HEAD.

Cross-claim note for X00/R08 (not an A verdict): the r7 read set's only
`corpus/**` members are `corpus/knowledge/synthesis/worldbible-integration-contract.md`
and four `corpus/lessons/round-6-sources/*.json` files. The ten C-claim
entries land under `corpus/knowledge/{culture-material,myth-symbol}/`, which
are **not** read-set members — so a hypothetical re-freeze would see no drift
from the C landing. X00/R08 should confirm against `V3_READ_SET` (`1935-1959`).

## Owed

- `reports/round-35/scout/K03-keyerror-path.md` — missing at write time. I
  reproduced the traceback and the resolving site myself (§1); K03's fragment
  remains owed for the independent traceback capture and the diagnostic-
  convention inventory it was scoped for.
- `reports/round-35/scout/K04-touched-census.md` — missing at write time. I
  derived the surface census from the r33/r34 commits (§9) with per-surface
  owners and risk classes; K04's fragment remains owed as the independent
  census R06 reconciles against.
- `reports/round-35/op/O01-patch-draft.md` — not owed by me, but §3 is the
  design O01 must turn into the exact before/after diff; if O01's diff
  departs from §3 (e.g. drops the record-then-raise shape), N3 in §7 must be
  dropped and R04 must see the departure.

## Citations

- `tools/exercise-handoff-e2e.py:3822` — `assembly.digests[rel]` unguarded index (KeyError site).
- `tools/exercise-handoff-e2e.py:3819` — `assembly.digests.get(rel)` predicate that admits the superseded member into `drifted`.
- `tools/exercise-handoff-e2e.py:3478-3485` — `assembly.digests` keyed strictly by `V3_READ_SET`.
- `tools/exercise-handoff-e2e.py:1935-1959` — `V3_READ_SET` (58 members; `CLAIMS_MAP` at `1957`).
- `tools/exercise-handoff-e2e.py:184` — `CLAIMS_MAP = "reports/round-34/handoff/declared-in-r7/claims-map.md"`.
- `tools/exercise-handoff-e2e.py:34`, `:57` — stale docstring cites of `reports/round-20/handoff/claims-map.md`.
- `tools/exercise-handoff-e2e.py:2700` — rendered packet prose naming the same path (must not be swept).
- `tools/exercise-handoff-e2e.py:88-93` — the exit-code/diagnostic contract the new code mirrors.
- `tools/exercise-handoff-e2e.py:4020` — `inputs` built from `V3_READ_SET` at freeze (freeze-invariance argument).
- `tools/exercise-handoff-e2e.py:4603` — `if err and not args.quiet:` (v3 branch) — companion edit.
- `tools/exercise-handoff-e2e.py:4133-4151` — `v3_build_fixture_root` / `v3_freezed_copy`.
- `tools/exercise-handoff-e2e.py:4414-4430`, `:4432-4438`, `:4440-4449`, `:4451-4457` — existing controls (`m12a`, `m12b`, `m8`, scan-expectation, missing-artifact).
- `tools/exercise-handoff-e2e.py:4459-4467` — selftest summary (`plus N controls`).
- Command: `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` → `KeyError: 'reports/round-20/handoff/claims-map.md'`, exit 1.
- Command: `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` → exit 0, `plus 39 controls`, 40 result lines.
- Command: `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → `exit=0 … packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`.
- Command: python diff of the two baselines' `inputs` maps → r6-only member `reports/round-20/handoff/claims-map.md`; r7-only member `reports/round-34/handoff/declared-in-r7/claims-map.md`; no other digest differs.
- Command: `--profile v3 --quiet --baseline <tampered-baseline.json>` vs the same run without `--quiet` → the `handoff-v3: E2E-BASELINE: …` line is suppressed under `--quiet` (measured; §4).
- `reports/round-34/handoff/repin.json` — row `R34-D-stale-row` (the N1 record, "designed E2E-DIGEST leg is unreachable for this class"), row `R34-D-default-pointer.control` (packet_sha256 match), row `R34-D-edit-set` (the r34 edit list, docstring `2290`/`2566`).
- `reports/round-34/handoff/declared-in-r7/packet.md:3` (round-20 path in prose) vs `:95`, `:113` (r7 path in the manifest) — F-P02-1.
- `reports/round-30/handoff/declared-in-r6/expected.json`, `reports/round-34/handoff/declared-in-r7/expected.json` — the two baseline `inputs` maps.
- `reports/round-35/claims.json:38-52` — claim O, its counting commands and thresholds.
- `PROVINCE.md:9-14`, `:16-20` — owns / refuses lists used in §9.
- Commands: `git diff --name-status da68a6d~1 da68a6d` (r33) and `git diff --name-status 4a7aede~1 4a7aede` (r34) — the surface census in §9.
- `git show 4a7aede -- tools/exercise-handoff-e2e.py` — r34 renderer hunks (CLAIMS_MAP re-point at `184`).
- `ls -l reports/round-20/handoff/claims-map.md` → present, 24,888 bytes — superseded, not missing.
