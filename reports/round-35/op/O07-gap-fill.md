- Seat: O07 | executor (spare, claim O) | claim O | date 2026-10-19 | baseline 4a7aede

# O07 — spare gap-fill for the O block

Mission (targets.json, seat O07): *"Spare: assist O01-O04 with any missing dependency;
record what you completed."* This fragment is that record. It supplies the two O-block
artifacts that did not exist when I looked, as **redundant, independently measured**
material — the integrator may take either my bytes or the owning seat's, but must not
treat this as a substitute verification of O01/O03 themselves.

## 1. Dependency map as observed

| dependency | state at 05:2x | what I supplied |
|---|---|---|
| `op/O01-patch-draft.md` | **absent** (op/ existed with O02/O04/O08/O10 only) | §3: an exact, applyable, byte-verified diff |
| `op/O03-isolated-verify.md` | **absent** | §4: apply-and-verify in a `git archive` copy I built myself |
| `scout/K03-keyerror-path.md` | present (05:20) | §2 cross-check: same site, same traceback |
| `plan/P02-oa-plan.md` | present (05:22) | §3 follows its convention decision (`E2E-READSET`, exit 1) |
| `op/O02-controls.md` | present (05:22) | §3 embeds its reference guard + m13/m14 controls **verbatim**; §4 re-runs them |
| `op/O04-regressions.md` | present (05:21) | §4 supplies the after-state the census pins (its owed item) |

O02 §Owed, O04 §Owed and O08 §Owed all name `op/O01-patch-draft.md`; O04/O08 also name
`op/O03-isolated-verify.md` and the post-patch observed outputs. Those are the gaps closed here.

## 2. The defect, reconstructed independently

Isolated copy (`git archive 4a7aede | tar -x -C .scratch/o07-iso`), never in-tree:

```
$ cd .scratch/o07-iso && python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
    --baseline reports/round-30/handoff/declared-in-r6/expected.json
EXIT=1
  File ".../.scratch/o07-iso/tools/exercise-handoff-e2e.py", line 3822, in v3_exercise
    record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
KeyError: 'reports/round-20/handoff/claims-map.md'
```

Read-set census of the r6 row, measured by importing the renderer and hashing live bytes
(`tools/exercise-handoff-e2e.py:1935` `V3_READ_SET`, `:184` `CLAIMS_MAP`):

| class | count | members |
|---|---|---|
| `inputs` keys in the r6 row | 58 | — |
| live `V3_READ_SET` members | 58 | — |
| unresolvable (named by the row, absent from the live read set) | 1 | `reports/round-20/handoff/claims-map.md` |
| resolvable but drifted | 0 | — |

r6 row sha256 `ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0` (matches
`reports/round-34/handoff/repin.json` R34-D-stale-row); isolated renderer sha256
`34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9` (matches that row's
`surface_sha256_after`). The class is exactly "the baseline names a member the live read set
no longer carries"; the drift branch's `.get` (line 3819) tolerates the unknown member, then the
report line's plain index dies. Zero drift is load-bearing: the superseded class is isolable.

## 3. Verified patch draft (O01's owed artifact)

Four hunks, all inside `tools/exercise-handoff-e2e.py`. Hunk 2 is O02 §3's reference guard
**verbatim**; hunk 3 is O02 §4/§5's four controls **verbatim**; hunk 4 is P02 §4's mandatory
one-line gate change; hunk 1 is O02 contract point 4. Convention follows P02 §3:
`Failed("E2E-READSET", …)` → exit **1**, naming the unresolvable member.

Applied to a fresh `git archive 4a7aede` copy by `.scratch/o07-apply-full.py` (assertion-guarded
string replacement, no in-tree write); patched file sha256
`bfd7e9ecb5bf979d8a6b74fc896c649f04dd7ba70cc8ccc8b3ef66dbec63d5a7`, `ast.parse` clean.

```diff
--- a/tools/exercise-handoff-e2e.py
+++ b/tools/exercise-handoff-e2e.py
@@ -88,7 +88,8 @@
 
 Exit codes (stable messages, no traceback): 0 clean; 1 mismatch —
 `E2E-DIGEST`, `E2E-COUNT`, `E2E-GATE`, `E2E-SCAN`, `E2E-UNC` (uncertainty
-findings), `E2E-LINK` (link findings); 2 could-not-evaluate — `E2E-ARTIFACT`
+findings), `E2E-LINK` (link findings), `E2E-READSET` (a baseline row naming a read-set member the
+live read set no longer carries); 2 could-not-evaluate — `E2E-ARTIFACT`
 (missing/unreadable read-set file), `E2E-BASELINE` (absent or edited baseline),
 `E2E-DATA` (malformed input). Writes go only to a fresh directory under
 `TMPDIR` (plus `--freeze DIR`); the read set is never modified, there is no
@@ -3813,6 +3814,22 @@
 
     try:
         baseline_path, baseline = v3_load_baseline(root, baseline_rel)
+
+        # R34-N1 hardening: a superseded row can name a read-set member the live
+        # read set no longer carries (the CLAIMS_MAP move is the precedent).
+        # Refuse by name; never die on an unhandled KeyError at the digest report.
+        unresolved = sorted(rel for rel in baseline["inputs"] if rel not in set(V3_READ_SET))
+        if unresolved:
+            for rel in unresolved:
+                record("input-readset", False, f"{rel}: named by the baseline, absent from the live read set")
+            raise Failed(
+                "E2E-READSET",
+                f"{len(unresolved)} read-set member(s) named by the baseline are not in the live read set: "
+                f"{', '.join(unresolved[:3])}"
+                + (f" (+{len(unresolved) - 3} more)" if len(unresolved) > 3 else "")
+                + " — the row is superseded; replay a current row or freeze a new one",
+            )
+
         snapshot_before = {rel: measure(root, rel)[0] for rel in V3_READ_SET}
         assembly = V3Assembly(root)
 
@@ -4456,6 +4473,69 @@
         assert (code, err) == (EXIT_UNEVALUATED, "E2E-ARTIFACT"), (code, err, records)
         results.append("missing D4 artifact: exit 2 E2E-ARTIFACT naming the unreadable path")
 
+        r6_row_rel = "reports/round-30/handoff/declared-in-r6/expected.json"
+        r6_stale_member = "reports/round-20/handoff/claims-map.md"
+        assert r6_stale_member not in V3_READ_SET and CLAIMS_MAP in V3_READ_SET, (r6_stale_member, CLAIMS_MAP)
+
+        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
+            superseded_root, _ = v3_freezed_copy(fixture, control_dir, "superseded-row")
+            victim = superseded_root / baseline_rel
+            edited = json.loads(victim.read_text(encoding="utf-8"))
+            assert sorted(edited["inputs"]) == sorted(V3_READ_SET), "a fresh freeze does not pin the live read set"
+            edited["inputs"][r6_stale_member] = edited["inputs"].pop(CLAIMS_MAP)
+            edited["baseline_digest"] = v3_baseline_digest(edited)
+            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
+            code, err, records = v3_exercise(root=superseded_root, baseline_rel=baseline_rel)
+        assert (code, err) == (EXIT_FAIL, "E2E-READSET"), (code, err, records)
+        assert any(not row["ok"] and r6_stale_member in row["detail"] for row in records), records
+        assert not any(row["check"] == "input-digest" and not row["ok"] for row in records), records
+        results.append(
+            f"m13a superseded row (a member moved out of the live read set): exit {code} {err} "
+            f"naming {r6_stale_member}"
+        )
+
+        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
+            r6_root, _ = v3_freezed_copy(fixture, control_dir, "r6-row-replay")
+            source = ROOT / r6_row_rel
+            if not source.is_file():
+                raise MissingArtifact(f"selftest fixture source missing: {r6_row_rel}")
+            target = r6_root / r6_row_rel
+            target.parent.mkdir(parents=True, exist_ok=True)
+            shutil.copy2(source, target)
+            code, err, records = v3_exercise(root=r6_root, baseline_rel=r6_row_rel)
+        assert (code, err) == (EXIT_FAIL, "E2E-READSET"), (code, err, records)
+        assert any(not row["ok"] and r6_stale_member in row["detail"] for row in records), records
+        results.append(
+            f"m13b filed r6 row replay against the live tree: exit {code} {err} naming {r6_stale_member} "
+            "(the R34-N1 KeyError path is a named refusal, never a traceback)"
+        )
+
+        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
+            flipped_root, _ = v3_freezed_copy(fixture, control_dir, "flipped-sha")
+            victim = flipped_root / baseline_rel
+            edited = json.loads(victim.read_text(encoding="utf-8"))
+            edited["inputs"][CLAIMS_MAP] = "0" * 64
+            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
+            code, err, records = v3_exercise(root=flipped_root, baseline_rel=baseline_rel)
+        assert (code, err) == (EXIT_UNEVALUATED, "E2E-BASELINE"), (code, err, records)
+        results.append(
+            "m14a flipped read-set sha in the baseline without re-signing: exit 2 E2E-BASELINE "
+            "(integrity digest mismatch), never a pass"
+        )
+
+        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
+            tampered_root, _ = v3_freezed_copy(fixture, control_dir, "tampered-member")
+            victim = tampered_root / CLAIMS_MAP
+            victim.write_text(victim.read_text(encoding="utf-8") + "\n", encoding="utf-8")
+            code, err, records = v3_exercise(root=tampered_root, baseline_rel=baseline_rel)
+        assert (code, err) == (EXIT_FAIL, "E2E-DIGEST"), (code, err, records)
+        assert err != "E2E-READSET", err
+        assert any(not row["ok"] and CLAIMS_MAP in row["detail"] for row in records), records
+        results.append(
+            f"m14b content-tampered live member {CLAIMS_MAP}: exit {code} {err} naming the changed file "
+            "(resolvable drift keeps its own leg; the read-set guard does not swallow it)"
+        )
+
     census = baseline["uncertainty"]["statuses"]
     print(
         f"selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0, "
@@ -4600,7 +4680,7 @@
         f"v2_subset={subset} alias_leg={alias} "
         f"packet_sha256={matches.group(1) if matches else '(not assembled)'}"
     )
-    if err and not args.quiet:
+    if err:
         print(f"handoff-v3: {err}: {records[-1]['detail'] if records else ''}")
     if args.json:
         print(json.dumps({"profile": "v3", "root": str(root), "baseline": args.baseline or baseline_default,
```

Notes for the integrator:

- **Precedence**: hunk 2 fires before `V3Assembly`, so a superseded row is refused cheaply and the
  drift branch stays byte-identical (`m12b`, `m8` and every filed reading of the
  `"{n} read-set file(s) changed since the baseline was frozen"` message are untouched by
  construction). Stated trade vs P02 §3's sketch: P02's drift-branch form additionally *records*
  resolvable drift for a mixed baseline; the pre-assembly guard refuses on the superseded member
  alone. Both satisfy O02 §2's five-point contract; the pre-assembly form is the one measured here.
- **Hunk 4 is load-bearing**, not cosmetic: `--quiet` is the claim's counting-command mode and the
  `handoff-v3: {code}: {detail}` line was gated on `not args.quiet` (`:4603`). v1 (`:4554`) and v2
  (`:4515`) twins are deliberately left alone (P02 §4 default: v3 only).
- Do **not** re-freeze `declared-in-r7` (claims.json non-goal); the patch changes no freeze path —
  measured identical in §4.

## 4. Isolated apply-and-verify (O03's owed artifact)

Fresh copy `.scratch/o07-full` at `4a7aede` + the §3 diff. All commands with
`TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all from inside the isolated copy.

**r6-row replay (the claim's counting command) — exit 1, named diagnostic, no traceback:**

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
    --baseline reports/round-30/handoff/declared-in-r6/expected.json
EXIT=1   (stderr 0 bytes)
handoff-v3: exit=1 fields=? glossary=?/20 findings=? links=? claims=? statuses=? v2_subset=unequal alias_leg=? packet_sha256=(not assembled)
handoff-v3: E2E-READSET: 1 read-set member(s) named by the baseline are not in the live read set: reports/round-20/handoff/claims-map.md — the row is superseded; replay a current row or freeze a new one
```

`--json` receipt on the same command: `receipt exit 1 code E2E-READSET`, failed records
`input-readset` (detail names `reports/round-20/handoff/claims-map.md`) and `verdict`.

**r7 default chain (regression, must exit 0):**

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
EXIT=0
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
```

Identical to the unpatched reading (same packet sha256, `repin.json` R34-D-default-pointer control).

**Selftest — exit 0, 43 controls (was 39), the four new lines as O02 predicted:**

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest
EXIT=0
selftest: OK — positive run (…) plus 43 controls:      [44 output lines: 1 header + 43 controls]
  - m13a superseded row (a member moved out of the live read set): exit 1 E2E-READSET naming reports/round-20/handoff/claims-map.md
  - m13b filed r6 row replay against the live tree: exit 1 E2E-READSET naming reports/round-20/handoff/claims-map.md (the R34-N1 KeyError path is a named refusal, never a traceback)
  - m14a flipped read-set sha in the baseline without re-signing: exit 2 E2E-BASELINE (integrity digest mismatch), never a pass
  - m14b content-tampered live member reports/round-34/handoff/declared-in-r7/claims-map.md: exit 1 E2E-DIGEST naming the changed file (resolvable drift keeps its own leg; the read-set guard does not swallow it)
```

**Freeze semantics unchanged** — `--profile v3 --quiet --freeze <scratch dir>` (scratch target only;
`declared-in-r7` never touched) run on both copies: exit 0, both print
`packet sha256 45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`, and
`diff -r` over the two produced directories reports **IDENTICAL**.

**Profiles unaffected**: `--profile v1 --quiet` → exit 1, `handoff-e2e: exit=1 fields=? …` and
`--profile v2 --quiet` → exit 0, `handoff-v2: exit=0 claims=15 links=50/50 drift=named(…)` —
byte-identical strings patched vs unpatched.

**Discrimination (unpatched copy, same command)**: unhandled `KeyError` traceback at `:3822`,
exit 1 via traceback — so the patch changes mechanism (named refusal) and diagnostic visibility,
not the verdict class.

## 5. Cross-checks against the block

- **K03** (`scout/K03-keyerror-path.md`): same site `:3822`; agrees the refusal is correct and the
  mechanism is not. My traceback is first-hand from an isolated copy, so the site is confirmed twice.
- **O02** (`op/O02-controls.md`): my §4 re-runs its guard and all four controls unmodified; the four
  emitted control lines match its §4/§5 "observed" lines verbatim, and the 39→43 control count is
  reproduced. Its §3 note "the unresolved check must precede the `drifted` computation" holds.
- **O04** (`op/O04-regressions.md`): its owed after-column is §4 — r7 chain exit 0 + unchanged packet
  sha256, freeze identical, v1/v2 unchanged, selftest green at 43 controls.
- **P02** (`plan/P02-oa-plan.md` §3/§4): convention and gate change followed exactly; the one
  deviation is placement (pre-assembly guard, as in O02's prototype), recorded as a trade above.
- **claims.json** counting command expects "exit 1, named diagnostic" — met only *with* hunk 4;
  without it `--quiet` prints the summary line alone (measured). If the integrator drops hunk 4,
  the validation leg must run the r6 replay without `--quiet`.

## 6. Boundary notes (routed, not absorbed)

- **v1 has the same latent index** at `tools/exercise-handoff-e2e.py:1440` (identical record line,
  reachable only if a v1 baseline names a member outside `V1_READ_SET`). Not touched — claim O names
  the v3 r6 replay; route to a future round if wanted. The earlier scratch variant that hardened it
  was discarded to keep this diff inside claim scope.
- No write of any kind under `reports/round-1..34/**`, `corpus/**`, `tools/**`, `.ufo/**`; the only
  renderer bytes I created live in `.scratch/`. No `--freeze` of `declared-in-r7`; no in-tree
  execution of any `reports/round-*/run-validation.py`.

## Owed

- `reports/round-35/op/O01-patch-draft.md` — still owed by O01 if that seat lands; this fragment's
  §3 is a tested stand-in, not O01's own draft. If O01's wording differs, §4's assertions are
  word-keyed only on the failed-record `detail` text and the code (O02 §2), so either form verifies.
- `reports/round-35/op/O03-isolated-verify.md` — still owed by O03; §4 is an independent
  apply-and-verify from a copy I rebuilt, but O05/O11 remain the independent verifiers of record.
- Integrator-applied in-tree state: the patch bytes must be applied by the integrator (seats may not
  write `tools/**`); §3's sha256 is the pre-application artifact, and post-application the in-tree
  file sha256 will differ (that reading is owed to whoever runs the §4 battery in-tree).
- `.scratch/o07-*` holds the isolated copies, the apply script and the raw outputs; per `AGENTS.md`
  the raw evidence needed to reproduce §2/§4 must be landed under `reports/round-35/telemetry/`
  before scratch cleanup if the parent wants it durable — my out path is this fragment only.

## Citations

- `tools/exercise-handoff-e2e.py:88-94` (exit-code census), `:184` (`CLAIMS_MAP` = r7 map),
  `:1933-1935` (v3 defaults + `V3_READ_SET`), `:3814-3823` (`v3_exercise` load, `.get` drift,
  `:3822` KeyError site), `:4154` (`v3_selftest`), `:4457` (insertion anchor for the controls),
  `:4603` (v3 quiet gate), `:4515`/`:4554` (v1/v2 twins), `:1440` (v1 latent index).
- `reports/round-34/handoff/repin.json` (R34-N1; R34-D-stale-row control; r7 packet digest
  `45f57132…`; renderer `surface_sha256_after` `34c85f57…`).
- `reports/round-30/handoff/declared-in-r6/expected.json` (sha256 `ea1e2927…`; 58 inputs;
  1 unresolvable; 0 drifted).
- `reports/round-35/claims.json:37-52` (claim O, counting commands, thresholds), `:71` (non-goals);
  `reports/round-35/targets.json` (seat O07 mission + `shared_rules`).
- `reports/round-35/op/O02-controls.md` §2-§6 (reference guard, m13/m14 controls, quiet-gate
  argument), `reports/round-35/plan/P02-oa-plan.md` §2-§5 (convention decision, catch sketch),
  `reports/round-35/op/O04-regressions.md` §Owed, `reports/round-35/op/O08-validation-legs.md` §Owed,
  `reports/round-35/scout/K03-keyerror-path.md`.
- Commands (all `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19): `git archive 4a7aede |
  tar -x -C .scratch/o07-iso`; unpatched `--profile v3 --quiet --baseline <r6 row>` (exit 1,
  traceback at `:3822`); `sha256sum` of the isolated renderer (`34c85f57…`) and of the patched file
  (`bfd7e9ec…`); `.scratch/o07-apply-full.py` (4 hunks) + `ast.parse`; patched `--profile v3 --quiet
  --baseline <r6 row>` (exit 1, stderr 0), `--profile v3 --quiet` (exit 0, `45f57132…`),
  `--profile v3 --selftest` (exit 0, 43 controls), `--profile v3 --quiet --json` (code
  `E2E-READSET`), `--profile v3 --quiet --freeze .scratch/o07-freeze-{unpatched,patched}` +
  `diff -r` (identical), `--profile v1 --quiet` / `--profile v2 --quiet` (unchanged both copies).
