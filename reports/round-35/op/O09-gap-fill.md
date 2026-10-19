- Seat: O09 | executor | claim O | date 2026-10-19 | baseline 4a7aede

# O09 — second gap-fill across the O block: the R34-N1 hardening built and verified in two placements

Mission (`reports/round-35/targets.json:240-244`): "Spare: second gap-fill across the O block."
Gap census at write time (`ls reports/round-35/op/` → `O02-controls.md`, `O04-regressions.md`,
`O06-receipt.md`, `O08-validation-legs.md`, `O10-scribe.md`; O01/O03/O05/O07/O11 not landed):

- **O02 §2 item 5 is the live gap.** O02's interface contract requires the named diagnostic to be
  visible on the `--quiet` path (because the claim's own counting command is `--quiet`,
  `reports/round-35/claims.json:48`), and O08's binding leg O1 asserts the token **and** the member
  path on the combined `--quiet` output (`reports/round-35/op/O08-validation-legs.md:53-80`).
  Measured on the pristine bytes: `--quiet` prints the summary line only — the diagnostic line sits
  behind `if err and not args.quiet:` (`tools/exercise-handoff-e2e.py:4603`). So **O08 leg O1 is
  unsatisfiable with the claim's counting command unless the print is hoisted**, and no landed
  fragment supplied the hoist. I built it and verified it.
- **No independently verified patch bytes existed yet** for O01/O03/O05/O11 to work from, so I also
  built the catch site + the two controls and verified the full configuration end to end in
  **two placements** (post-assembly and O02's pre-assembly site) in isolated `git archive` copies.

Everything below is measured in `.scratch/o09` (post-assembly form), `.scratch/o09-o02form`
(early form) and `.scratch/o09-before` (pristine control), all `git archive 4a7aede` extracts
outside the durable tree; **no in-tree byte was written** (in-tree renderer sha256 still
`34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9`, equal to
`reports/round-34/handoff/repin.json:12` `surface_sha256_after`).

## 1. Before-state, pristine bytes (isolated copy)

```
$ cd .scratch/o09-before && python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
    --baseline reports/round-30/handoff/declared-in-r6/expected.json
  File ".../tools/exercise-handoff-e2e.py", line 3822, in v3_exercise
    record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
KeyError: 'reports/round-20/handoff/claims-map.md'
EXIT=1
```

Mechanism (unchanged from `reports/round-34/handoff/repin.json:50`, R34-N1): `:3819` classifies with
`assembly.digests.get(rel)` (tolerating an unknown member), then `:3822` indexes
`assembly.digests[rel]` directly, so the designed `raise Failed("E2E-DIGEST", …)` at `:3823` is
unreachable for a superseded row. `assembly.digests` is keyed by the live `V3_READ_SET` (`:3481-3484`).

**New evidence: the class is five rows wide, not one.** Replaying every filed v3 baseline on pristine
bytes (same copy, full output, no `--quiet`):

| baseline | pristine | patched (both forms) |
|---|---|---|
| `reports/round-20/handoff/expected.json` | exit 1, `KeyError: 'reports/round-20/handoff/claims-map.md'` at `:3822` | exit 1, `E2E-READSET` naming that path |
| `reports/round-22/handoff/declared-in/expected.json` | same KeyError | same named refusal |
| `reports/round-22/handoff/declared-in-r2/expected.json` | same KeyError | same named refusal |
| `reports/round-26/handoff/declared-in-r5/expected.json` | same KeyError | same named refusal |
| `reports/round-30/handoff/declared-in-r6/expected.json` | same KeyError | same named refusal |
| `reports/round-34/handoff/declared-in-r7/expected.json` | exit 0, packet `45f57132…` | exit 0, packet `45f57132…` (unchanged) |
| `reports/round-11/handoff/expected.json` (v1) | exit 1, **named** `E2E-DIGEST: … tools/d2-typed-labels.py` | identical |
| `reports/round-15/handoff/expected.json` (v2) | exit 0, `drift=named(tools/harness/packet_links.py round-16)` | identical |

R34-N1 recorded only the r6-row instance; the same unhandled exception is the current behaviour of
all five filed superseded v3 rows. The v1 site carries the identical latent pattern
(`tools/exercise-handoff-e2e.py:1435-1441`, same `.get()` classify / plain-index report) but is
**not** live: the filed round-11 baseline's only defect is a resolvable member whose digest drifted,
so the designed `E2E-DIGEST` fires correctly. Do not "fix" v1 in this round; file it as a routed
finding if the integrator wants it covered.

## 2. Adjacent hole found while probing (routed, integrator's call)

A baseline whose `inputs` **omit** a live read-set member replays silently: with the r7 baseline
minus one member and a re-signed `baseline_digest`, the pristine renderer returned
`exit=0 … packet_sha256=45f57132…` — the row vouches for 57 of 58 read-set files and nothing notices.
Probe recipe (isolated copy):

```
$ python3 -B -c "import json,runpy;m=runpy.run_path('tools/exercise-handoff-e2e.py');b=json.load(open('reports/round-34/handoff/declared-in-r7/expected.json'));b['inputs'].pop('tools/assemble-d4-typed.py');b['baseline_digest']=m['v3_baseline_digest'](b);json.dump(b,open('.probe/subset-expected.json','w'),indent=1,sort_keys=True)"
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline .probe/subset-expected.json   # pristine → EXIT=0
```

The optional `unpinned` leg in the diff below closes it (patched → exit 1 `E2E-READSET` naming
`tools/assemble-d4-typed.py`). It is a **separate** move from R34-N1: it is not required by claim O's
`after_required` (`claims.json:45`), it changes behaviour for rows that today pass, and the integrator
may drop it without touching the R34-N1 legs. With it applied, every filed baseline's verdict is
unchanged (§1 table, "patched" column).

## 3. The patch — recommended form (early placement, O02's site)

Placement rationale: refusing **before** `V3Assembly` costs nothing, and — unlike the
post-assembly variant I first built — it cannot be masked by an assembly failure that a superseded
row might also trip. Both forms are verified; apply one. Diff against pristine
`tools/exercise-handoff-e2e.py` (sha256 `34c85f57…`); patched sha256 `06a3ae04…` (early form) /
`98139a0d…` (post-assembly form); full bytes at `.scratch/o09-o02form/patch-o02form.diff` and
`.scratch/o09/.probe/patch-final.diff`:

```diff
@@ -3813,6 +3813,32 @@
     try:
         baseline_path, baseline = v3_load_baseline(root, baseline_rel)
+        unresolvable = [rel for rel in baseline["inputs"] if rel not in set(V3_READ_SET)]
+        if unresolvable:
+            record(
+                "input-readset",
+                False,
+                f"{len(unresolvable)} frozen read-set member(s) are not in this renderer revision's read set: "
+                f"{', '.join(unresolvable[:3])}",
+            )
+            raise Failed(
+                "E2E-READSET",
+                f"{len(unresolvable)} frozen read-set member(s) are not in this renderer revision's read set: "
+                f"{', '.join(unresolvable[:3])} — the baseline row predates a read-set move and cannot replay "
+                "against the live read set; the frozen row stays byte-identical",
+            )
+        unpinned = [rel for rel in V3_READ_SET if rel not in baseline["inputs"]]
+        if unpinned:
+            record(
+                "input-readset",
+                False,
+                f"{len(unpinned)} live read-set member(s) are not pinned by the baseline: {', '.join(unpinned[:3])}",
+            )
+            raise Failed(
+                "E2E-READSET",
+                f"{len(unpinned)} live read-set member(s) are not pinned by the baseline: {', '.join(unpinned[:3])} — "
+                "the row predates the member's addition and cannot vouch for it",
+            )
         snapshot_before = {rel: measure(root, rel)[0] for rel in V3_READ_SET}
         assembly = V3Assembly(root)
@@ -4600,7 +4652,7 @@
         f"packet_sha256={matches.group(1) if matches else '(not assembled)'}"
     )
-    if err and not args.quiet:
+    if err:
         print(f"handoff-v3: {err}: {records[-1]['detail'] if records else ''}")
     if args.json:
```

Selftest controls (draft bytes, `v3_selftest`, inserted after the m12b leg at `:4430`); the whole
block is in `.scratch/o09-o02form/patch-o02form.diff` hunk 2:

```python
        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            superseded_root, _ = v3_freezed_copy(fixture, control_dir, "superseded-row")
            victim = superseded_root / baseline_rel
            edited = json.loads(victim.read_text(encoding="utf-8"))
            moved_member = "reports/round-20/handoff/claims-map.md"
            edited["inputs"][moved_member] = "0" * 64
            edited["baseline_digest"] = v3_baseline_digest(edited)
            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
            code, err, records = v3_exercise(root=superseded_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_FAIL, "E2E-READSET"), (code, err, records)
        readset_detail = next(r["detail"] for r in records if r["check"] == "input-readset")
        assert moved_member in readset_detail, readset_detail
        results.append("superseded row (a frozen read-set member left the live read set): exit 1 E2E-READSET naming the unresolvable path")
```

(the second control, `subset-row`, differs only in dropping `V3_READ_SET[-1]` from `inputs` and
asserting the same `(EXIT_FAIL, "E2E-READSET")`; full bytes in the diff.)

Reconciliation with O02 §4 (`op/O02-controls.md:106-113`): O02 drafts the same control as `m13` with the
same record name `input-readset` and the same `(EXIT_FAIL, "E2E-READSET")` expectation. **Apply one
control, not both** — otherwise the suite double-counts the same class. Also note O02's guard is
inserted after `v3_load_baseline` (pre-assembly, the placement I recommend); its message wording
differs from mine but satisfies the same regex, and O02 §2 item 4 additionally asks for `E2E-READSET`
to be added to the docstring exit-code census (`:89-95`) — **that edit is not in my diff and remains
owed by O01/the integrator.**

## 4. Verification matrix (both forms, isolated copies)

| # | command | observed |
|---|---|---|
| V1 | `--profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | exit 1; second line `handoff-v3: E2E-READSET: 1 frozen read-set member(s) are not in this renderer revision's read set: reports/round-20/handoff/claims-map.md — the baseline row predates a read-set move and cannot replay against the live read set; the frozen row stays byte-identical` — token + path on one line, on the `--quiet` path |
| V2 | `--profile v3 --quiet` (r7 default chain) | exit 0; `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` — single line, byte-identical to the pristine run |
| V3 | `--profile v3 --selftest` | exit 0; header `selftest: OK — … plus 41 controls:`; 42 `^  - ` lines; `superseded row …` and `subset row …` both green; `tamper read-set: exit 1 E2E-DIGEST naming the changed file`, `tamper baseline: exit 2 E2E-BASELINE …`, `m8 re-typed v2 row: exit 1 E2E-DIGEST …`, `m11 D4-CL08 … E2E-UNC`, `missing artifact: exit 2 E2E-ARTIFACT …` all preserved |
| V4 | `--selftest` (no profile) | exit 0; `plus 17 controls:` — the **v1** suite, unchanged by the patch |
| V5 | `--profile v1 --quiet --baseline reports/round-11/handoff/expected.json` | exit 1, summary-only stdout — the hoist is v3-scoped, v1's failing-quiet shape is untouched |
| V6 | `--profile v2 --quiet --baseline reports/round-15/handoff/expected.json` | exit 0, `drift=named(tools/harness/packet_links.py round-16)` — unchanged |
| V7 | `--profile v3 --json --baseline …declared-in-r6/expected.json` | receipt carries `"code": "E2E-READSET"`, `"exit": 1`, `checks: [('input-readset', False), ('verdict', False)]` |
| V8 | five superseded baselines (§1 table) | all five → exit 1 `E2E-READSET` naming the moved path; zero tracebacks |
| V9 | `--profile v3 --quiet --baseline .probe/subset-expected.json` | exit 1, `E2E-READSET: 1 live read-set member(s) are not pinned by the baseline: tools/assemble-d4-typed.py — …` (only with the optional `unpinned` leg) |

Control-count arithmetic: pristine v3 suite **39** controls (`grep -c '^  - '` = 40, header `plus 39
controls`) → +superseded-row = **40** → +subset-row = **41**. O02's trade note on the hoist
(`op/O02-controls.md:69-75`; failing quiet stdout gains one line, successful quiet stdout unchanged)
is confirmed by V2/V5/V6.

## 5. Hand-off notes for the validator author (feeds O08 leg O1 / S04)

- Run the v3 suite explicitly: **`--selftest` alone runs the v1 suite (17 controls)**; the new
  controls only exist under `--profile v3 --selftest` (`main`, `:4524` v2 branch vs `:4563` v3 branch).
- The claim's counting command (`claims.json:48`) keeps `--quiet`; with the hoist applied, the
  diagnostic is on stdout, so O08 leg O1's regex can be
  `^handoff-v3: E2E-READSET: .*reports/round-20/handoff/claims-map\.md` on the combined output.
  Without the hoist, the only observable is the exit code — the leg would have to be `--json`.
- `E2E-READSET` is a **new** code: the renderer's documented census is `E2E-DIGEST, E2E-COUNT,
  E2E-GATE, E2E-SCAN, E2E-UNC, E2E-LINK` (exit 1) and `E2E-ARTIFACT, E2E-BASELINE, E2E-DATA`
  (exit 2) at `:89-95`; the docstring edit (O02 §2 item 4) is still owed.

## 6. Preservation (measured after all runs)

- `reports/round-30/handoff/declared-in-r6/expected.json` sha256 `ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0` — unchanged, equals `reports/round-34/handoff/repin.json:17`.
- `reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json,freeze.txt,claims-map.md}` sha256 `45f57132… / 0e229138… / bbe15887… / 3969954b… / d181de28…` — all five equal `repin.json:26-30`; no freeze byte moved (no `--freeze` was run anywhere, per the round's non-goals).
- In-tree `tools/exercise-handoff-e2e.py` sha256 `34c85f57…` — untouched; the patch exists only in `.scratch` copies.
- No `reports/round-*/run-validation.py` was executed in-tree or in any copy (F-C13-1); no filed round byte was written.

## Owed

- `reports/round-35/op/O01-patch-draft.md` was not landed when this fragment was written; the binding patch form is O01's. This fragment supplies two verified candidate forms, not the binding one — the integrator must reconcile O01/O02 with the diff above before applying, and must add `E2E-READSET` to the docstring exit-code census (`tools/exercise-handoff-e2e.py:89-95`) which none of the verified diffs contains.
- The patch is **not applied in-tree** (by this seat's write boundary). O03/O05/O11 must rebuild their own `git archive` copy and re-run §4's V1–V4, V7, V9 legs against whatever form the integrator adopts; my raw logs live only in `.scratch/o09/.probe/` and `.scratch/o09-o02form/selftest-o02form.log` (scratch, not durable) — the reproducible commands and observed lines are inlined above.
- O08 leg O1's exact regex should be re-read against the adopted patch wording; my message text and O02's differ, so the leg must be written to the token + path, not to a fixed sentence.

## Citations

- `reports/round-35/targets.json:240-244` (O09 mission/out), `reports/round-35/claims.json:37-52` (claim O incl. counting commands `:46-49`), `reports/round-35/claims.json:67-73` (non-goals)
- `reports/round-35/op/O02-controls.md:55-75` (§2 items 4-5 + hoist diff + trade note), `:77-105` (reference guard), `:106-113` (m13 control), `reports/round-35/op/O08-validation-legs.md:53-80` (leg O1), `reports/round-35/op/O04-regressions.md:27-45` (site + classification)
- `tools/exercise-handoff-e2e.py:184` (CLAIMS_MAP), `:1933-1935` (v3 default pair + read set), `:3819-3823` (defect site), `:1435-1441` (v1 latent twin), `:3481-3484` (digests keyed by live read set), `:4154` (`v3_selftest`), `:4430` (m12b control), `:4524`/`:4563` (selftest dispatch: v2 / v3 branch), `:4603` (quiet guard), `:89-95` (exit-code census)
- `reports/round-34/handoff/repin.json:12,17,19-21,26-30,50` (surface digest, r6 row, R34-N1, r7 digests)
- Commands (all `cd .scratch/o09{,-before,-o02form}` with `export TMPDIR=… PYTHONDONTWRITEBYTECODE=1`): `git archive 4a7aede | tar -x -C …`; `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` (V1/V8); `--profile v3 --quiet` (V2); `--profile v3 --selftest` (V3); `--selftest` (V4); `--profile v1|v2 --quiet --baseline reports/round-1{1,5}/handoff/expected.json` (V5/V6); `--profile v3 --json --baseline …` (V7); `--profile v3 --quiet --baseline .probe/subset-expected.json` (V9, probe built with `runpy` + `v3_baseline_digest`); `sha256sum` on the renderer and on the five r7 artifacts; `diff -u .scratch/o09-before/tools/exercise-handoff-e2e.py .scratch/o09-o02form/tools/exercise-handoff-e2e.py`
