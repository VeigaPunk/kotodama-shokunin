- Seat: O01 | executor | O | date 2026-10-19 | baseline 4a7aede

# O01 — R34-N1 hardening patch draft (claim O, operability)

Draft only: nothing under `tools/**` was written by this seat. The integrator applies the fenced
diffs below. All reproduction and verification ran in `git archive 4a7aede` copies under
`.scratch/o01-verify/`, never in-tree and never through a filed round runner.

## 1. What the patch is — four decisions, each with its evidence

**1. Site (confirmed, not assumed).** `tools/exercise-handoff-e2e.py:3822` inside `v3_exercise`
(`:3807`): the drift *reporting* loop indexes `assembly.digests[rel]` directly, while the detection
comprehension at `:3820` uses the tolerant `.get(rel)`. `V3Assembly.__init__` builds `self.digests`
over the live `V3_READ_SET` only (`:3479-3483`, `V3_READ_SET` at `:1935`), so any member named by a
frozen baseline that the live read set no longer carries raises `KeyError` before the designed
`raise Failed("E2E-DIGEST", …)` at `:3823` can fire. Reproduced in the pristine copy
(`--profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json`): exit 1,
**stdout empty**, traceback on stderr ending `KeyError: 'reports/round-20/handoff/claims-map.md'` at
line 3822 — byte-for-byte the traceback K03 captured independently
(`reports/round-35/scout/K03-keyerror-path.md:22-31`).

**2. Truthful wording, not a `.get()` swap.** The condition is membership, not content drift: the
r20 claims-map still hashes to its frozen `4b1b9a35a18f…` (K03 §3, `K03:62-79`), so the `:3823` text
("read-set file(s) changed since the baseline was frozen") and m12b's "naming the changed file"
label are both false for this row. Patch A therefore adds a roster guard *before* the digest
comparison and refuses the row by name; the digest leg keeps its bytes and its semantics.

**3. `E2E-READSET` at exit 1 (`Failed` family).** Matches K03 §4's primary recommendation and its
evidence (`K03:105-120`): the filed r6 control records `"exit": 1`
(`reports/round-34/handoff/repin.json:19-21`, never editable), the sibling drift leg is also exit 1,
and exit 2 is documented for *missing/unreadable* artifacts or *absent/edited* baselines — neither
holds here (file present, baseline integrity-valid, `v3_load_baseline` passes it). Claim O's counting
command declares `(expect: exit 1, named diagnostic)`. The code is new — `E2E-READSET` occurs 0 times
at HEAD (`K03:99-103`) — so the docstring exit map at `:89-93` is extended in the same patch.

**4. Quiet visibility (hunk A4) — adopted from O02's contract, item 5** (`reports/round-35/op/O02-controls.md:52-56`).
The claim's declared counting command is `--quiet`, and `main` printed the
`handoff-v3: {code}: {detail}` line only when `not args.quiet` (`:4603`). Hunk A4 drops the
`not args.quiet` guard on that one print (v3 branch only; the v1 branch returns earlier at `:4556`
and keeps its filed failure shape, quoted at `reports/round-20/handoff/v3.md:76`).

Safety of A4, checked rather than assumed:
- The **summary line is untouched** in every case, so the filed verbatim quotations stay
  reproducible (`reports/round-30/regression.json:698`, `reports/round-30/regression-initial.json:634`,
  `reports/round-22/bleed/evidence/attempt-01-verification.json:241`, `reports/round-27/law/impl-4.md:36`).
- No consumer reads a *failing* quiet stdout: the filed validators run the renderer only in its green
  configuration and parse `packet_sha256=([0-9a-f]{64})` from the **successful** run
  (`reports/round-34/run-validation.py:180-183`; `reports/round-30/run-validation.py:71-73`;
  `reports/round-31/run-validation.py:88-89`), and neither `tools/gates/**` nor `tools/harness/**`
  references the renderer at all (`grep -rln exercise-handoff-e2e tools/gates/ tools/harness/` → no
  matches).
- The success path is byte-identical (`if err:` is only reached when `err` is set).

**This supersedes my first draft's "leave `--quiet` alone" position**: O02's form satisfies the
claim's "named diagnostic" on the declared counting command *and* preserves the filed summary-line
quotations, which the summary-line reformatting I had rejected would not have.

## 2. REQUIRED patch A — apply this

Applies to `tools/exercise-handoff-e2e.py` at baseline `4a7aede` (4 hunks, one file, +21/−3).
`git apply -p1` clean on a fresh `git archive 4a7aede`; compiles; selftest-green (§4).

Patch sha256 `ae15e6c1c1f0badbe0664410482909680f190aff22bdc0440714f40764e1e29b` (54 lines,
`.scratch/o01-verify/O01-A.patch`); patched file sha256
`1663c86ab214e93365edc28874a45d272dde3c207c2a9031dbbdc3e73939428a`.

```diff
--- a/tools/exercise-handoff-e2e.py
+++ b/tools/exercise-handoff-e2e.py
@@ -60,7 +60,9 @@
 
 Assertions the v3 run makes
 
-  1. read-set digests match the frozen v3 baseline (drift names the file);
+  1. read-set digests match the frozen v3 baseline (drift names the file; a
+     baseline naming a read-set member the live read set no longer carries is
+     refused as `E2E-READSET` by name — the row is superseded);
   2. preflight: 16 fields, non-canon marker, licensed glossary vocabulary, no
      floating version, and the uncertainty/link grammar below;
   3. v2-subset equality: the 15 v2 claims parsed out of the v3 ledger are
@@ -88,7 +90,9 @@
 
 Exit codes (stable messages, no traceback): 0 clean; 1 mismatch —
 `E2E-DIGEST`, `E2E-COUNT`, `E2E-GATE`, `E2E-SCAN`, `E2E-UNC` (uncertainty
-findings), `E2E-LINK` (link findings); 2 could-not-evaluate — `E2E-ARTIFACT`
+findings), `E2E-LINK` (link findings), `E2E-READSET` (a frozen baseline names a
+read-set member the live read set no longer carries — the row is superseded and
+cannot be replayed); 2 could-not-evaluate — `E2E-ARTIFACT`
 (missing/unreadable read-set file), `E2E-BASELINE` (absent or edited baseline),
 `E2E-DATA` (malformed input). Writes go only to a fresh directory under
 `TMPDIR` (plus `--freeze DIR`); the read set is never modified, there is no
@@ -3816,6 +3820,20 @@
         snapshot_before = {rel: measure(root, rel)[0] for rel in V3_READ_SET}
         assembly = V3Assembly(root)
 
+        dropped = sorted(rel for rel in baseline["inputs"] if rel not in assembly.digests)
+        if dropped:
+            for rel in dropped:
+                record(
+                    "read-set-roster",
+                    False,
+                    f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… not in the live read set "
+                    f"({len(V3_READ_SET)} members)",
+                )
+            raise Failed(
+                "E2E-READSET",
+                f"{len(dropped)} read-set member(s) named by the frozen baseline are not in the live read set: "
+                f"{', '.join(dropped[:3])} — the baseline row is superseded (re-point or re-freeze it)",
+            )
         drifted = [rel for rel, digest in baseline["inputs"].items() if assembly.digests.get(rel) != digest]
         if drifted:
             for rel in drifted:
@@ -4600,7 +4618,7 @@
         f"v2_subset={subset} alias_leg={alias} "
         f"packet_sha256={matches.group(1) if matches else '(not assembled)'}"
     )
-    if err and not args.quiet:
+    if err:
         print(f"handoff-v3: {err}: {records[-1]['detail'] if records else ''}")
     if args.json:
         print(json.dumps({"profile": "v3", "root": str(root), "baseline": args.baseline or baseline_default,
```

Hunk notes:
- **A3 is the catch site.** The guard makes the `:3822` index safe *by construction* (after it,
  every baseline-named member is a key of `assembly.digests`), so the digest leg's bytes are
  untouched. `assembly.digests` is exactly the live `V3_READ_SET` roster (`:3479-3483`) and
  `measure` raises `MissingArtifact` for an unreadable member (`:293-300`), so the guard cannot mask
  a missing file — that stays exit 2 `E2E-ARTIFACT`. Ordering is load-bearing (O02 §3,
  `O02-controls.md:100-105`): the roster check must precede the `drifted` computation.
- One new record name `read-set-roster`; `main()` looks up only `gate-scan`, `frozen-packet`,
  `semantic-links`, `uncertainty-census`, `v2-subset`, `alias-leg`, none of which collide.
- **Patch A satisfies all five of O02's interface-contract items** (`O02-controls.md:46-56`),
  checked one by one in §4.

## 3. Control block — choose ONE superseded-row control (count arithmetic is binding)

Patch A adds no control (the selftest count is unchanged). Claim O also requires the superseded-row
refusal control. Two ready forms exist; **exactly one** superseded-row control should land, because
they assert the same refusal:

- **B2 (recommended): O02's four controls** — m13a (superseded row), m13b (filed r6 row replay),
  m14a (flipped-sha → exit 2 `E2E-BASELINE`), m14b (content-tampered live member → exit 1
  `E2E-DIGEST`), drafted at `reports/round-35/op/O02-controls.md:107-235`. Measured by me on
  patch A: selftest exit 0, **header 43 / bullets 44**, all four lines green, 0 tracebacks — the
  same 43 O02 reported, so the two measurements agree.
- **B1 (fallback, this seat): one control m12c** — sha256
  `d2a8fdaa499ac1b40199d6446f7eb3a99e50b99db026ba67f23d902b021caf87` (24 lines,
  `.scratch/o01-verify/O01-B1.patch`, applies on top of A). Measured: selftest exit 0,
  **header 40 / bullets 41**.

**Count table (all measured, not inferred):**

| tree | selftest header | bullets |
|---|---|---|
| pristine `4a7aede` | 39 | 40 |
| A (required patch only) | 39 | 40 |
| A + B1 (m12c) | 40 | 41 |
| **A + B2 (O02's four)** | **43** | **44** |
| A + B1 + B2 (both, double-covered) | 44 | 45 |

**O08's leg asserts header `N ≥ 41`** (`reports/round-35/op/O08-validation-legs.md:74-85`), so
**B1 alone does not clear it** — land B2 (43), or B1 + three of B2's four (43), or both (44). If the
integrator lands A alone, that leg fails by construction; record the deviation rather than relaxing
the claim silently.

```diff
--- a/tools/exercise-handoff-e2e.py
+++ b/tools/exercise-handoff-e2e.py
@@ -4448,6 +4448,21 @@
         results.append("m12b tamper read-set (D4 projection): exit 1 E2E-DIGEST naming the changed file")
 
         with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
+            superseded_root, _ = v3_freezed_copy(fixture, control_dir, "superseded-row")
+            victim = superseded_root / baseline_rel
+            edited = json.loads(victim.read_text(encoding="utf-8"))
+            edited["inputs"]["reports/round-20/handoff/claims-map.md"] = edited["inputs"].pop(CLAIMS_MAP)
+            edited["baseline_digest"] = v3_baseline_digest(edited)
+            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
+            code, err, records = v3_exercise(root=superseded_root, baseline_rel=baseline_rel)
+        assert (code, err) == (EXIT_FAIL, "E2E-READSET"), (code, err, records)
+        assert any("reports/round-20/handoff/claims-map.md" in item["detail"] for item in records), records
+        results.append(
+            "m12c superseded row (the frozen baseline names a read-set member the live read set no longer "
+            "carries): exit 1 E2E-READSET naming the unresolvable path, never an unhandled KeyError"
+        )
+
+        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
             v2_root, _ = v3_freezed_copy(fixture, control_dir, "retouched-v2")
             victim = v2_root / V2_PACKET_YML
             victim.write_text(victim.read_text(encoding="utf-8").replace("status: \"supported\"", "status: \"partial\"", 1), encoding="utf-8")
```

m12c re-signs `baseline_digest` after moving the member, so it exercises the roster guard and not
the integrity check; m12b already covers the preserved `E2E-DIGEST` path for a member that *is* in
the live read set, which is why B1 adds only one control (agreeing with `K03:137-142`).

## 4. Verification (isolated copies; `TMPDIR=.scratch`; no in-tree runner)

| # | Command (cwd = isolated copy) | Pristine | Patch A | A + B1 |
|---|---|---|---|---|
| 1 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` | exit 0, header `plus 39 controls`, 40 bullets, 0 `Traceback` | exit 0, header 39, 40 bullets, 0 `Traceback` | exit 0, header 40, 41 bullets, 0 `Traceback` |
| 2 | `… --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | exit 1, stdout empty, stderr = `KeyError` traceback at `:3822` | **exit 1; stdout = summary line (byte-identical to the filed quote) + `handoff-v3: E2E-READSET: 1 read-set member(s) named by the frozen baseline are not in the live read set: reports/round-20/handoff/claims-map.md — the baseline row is superseded (re-point or re-freeze it)`; stderr 0 bytes** | same |
| 3 | same, without `--quiet` | exit 1, stdout empty | exit 1, stderr 0 bytes, same named line (plus the `FAIL read-set-roster: …` record line) | same |
| 4 | `… --profile v3 --quiet` (r7 default chain) | exit 0, `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` | identical line, exit 0 | identical line, exit 0 |
| 5 | selftest controls m12a / m12b / missing-artifact | exit 2 `E2E-BASELINE` / exit 1 `E2E-DIGEST` / exit 2 `E2E-ARTIFACT` | unchanged (same three bullets) | unchanged |
| 6 | `sha256sum` of `reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json,freeze.txt,claims-map.md}`, measured **after** running the tool on the patched tree | — | all five byte-identical to pristine (`45f57132…`, `0e229138…`, `bbe15887…`, `3969954b…`, `d181de28…`); the filed r6 row also unchanged at `ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0` (= repin's recorded `surface_sha256`); no `--freeze` run by this seat | same |
| 7 | `git apply -p1 --check` on fresh archives (A, then B1, then the optional v1 patch in sequence) | — | clean | clean |
| 8 | `python3 -B tools/exercise-handoff-e2e.py --profile v1 --selftest` / `--profile v1 --quiet` | exit 0, 18 bullets / exit 1 pre-existing | exit 0, 18 bullets / exit 1 pre-existing (measured, unchanged — A's hunks are v3-only) | same |

O02's five contract items against patch A, each checked: (1) `(EXIT_FAIL, "E2E-READSET")` on a
baseline naming a member outside the live read set — row 2 ✓; (2) the unresolvable path verbatim in
a failed record row — `FAIL read-set-roster: reports/round-20/handoff/claims-map.md: …` ✓; (3) the
message names the member(s), first three — ✓; (4) `E2E-READSET` added to the docstring exit census —
hunk A2 ✓; (5) named diagnostic visible on `--quiet` — hunk A4, row 2 ✓.

**Deliverable-form check.** Both fenced blocks were re-extracted from this fragment and replayed:
block 1 sha256 `ae15e6c1…`, block 2 sha256 `d2a8fdaa…`; applied in sequence with `git apply -p1` to
a fresh `git archive 4a7aede`, the result compiles, exits 1 on the r6 replay and 0 on the r7 default
chain — the same behavior verified in the table above.

## 5. Acceptance-leg guidance for O05 / O08 / O11

1. **Exit 1 alone does not discriminate** (K03 §1, `K03:36-40`): CPython's uncaught-exception exit
   status is also 1, so an `exit == 1`-only assertion passes on the unpatched tree. Assert all
   three: exit 1, **no `Traceback` on stderr**, and the `handoff-v3: E2E-READSET:` line carrying
   `reports/round-20/handoff/claims-map.md`. With hunk A4 all three hold on the **declared counting
   command itself** (`--quiet`), so no second invocation is needed.
2. **Assert the bullet count, not the header** (K03 §5, `K03:131-136`): the header prints
   `len(results) - 1` (`:4464`) while every element of `results` is printed as a bullet
   (`:4466-4467`), so the invariant is `bullets = header + 1` (39/40, 43/44, 44/45 per §3). O08's
   `N ≥ 41` header assertion is cleared only by the B2 or both-control trees.
3. **Regression controls that must stay green:** r7 default chain exit 0 with packet `45f57132…`
   (equals repin's `R34-D-default-pointer` control, `reports/round-34/handoff/repin.json:16-19`);
   m12a `E2E-BASELINE`, m12b `E2E-DIGEST`, missing-artifact `E2E-ARTIFACT`.
4. **Quiet-failure stdout now has two lines** (summary + diagnostic). Any leg that recorded the
   pre-patch one-line failure shape must be updated; the summary line itself is unchanged, so the
   filed quotations remain accurate.
5. No freeze bytes move: patch A touches one file and no `--freeze` of declared-in-r7 is permitted
   or needed.

## 6. Optional companion — v1 mirror (offered, verified behavior-preserving)

`v1_exercise` carries the identical shape at `:1436-1441` (multi-line `drifted`, crash line `:1440`,
designed raise `:1441`). K03 shows the exposure is latent only — the v1 default baseline
`reports/round-11/handoff/expected.json` (21 members) is a subset of `V1_READ_SET`, baseline-only set
∅ (`K03:53-56`).

Fenced diff, applies **on top of** A (and after B1/B2 if applied; `git apply -p1` clean in sequence;
23 lines, sha256 `e784186e0f787ad5fe94eebfd9652caf1c5e30bca3471483909892adb31a98b3`):

```diff
--- a/tools/exercise-handoff-e2e.py
+++ b/tools/exercise-handoff-e2e.py
@@ -1436,6 +1436,20 @@
         snapshot_before = {rel: measure(root, rel)[0] for rel in V1_READ_SET}
         assembly = V1Assembly(root)
 
+        dropped = sorted(rel for rel in baseline["inputs"] if rel not in assembly.digests)
+        if dropped:
+            for rel in dropped:
+                record(
+                    "read-set-roster",
+                    False,
+                    f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… not in the live read set "
+                    f"({len(V1_READ_SET)} members)",
+                )
+            raise Failed(
+                "E2E-READSET",
+                f"{len(dropped)} read-set member(s) named by the frozen baseline are not in the live read set: "
+                f"{', '.join(dropped[:3])} — the baseline row is superseded (re-point or re-freeze it)",
+            )
         drifted = [
             rel for rel, digest in baseline["inputs"].items() if assembly.digests.get(rel) != digest
         ]
```

Verified (`.scratch/o01-verify/patched-v1`, `.scratch/o01-verify/vAv1`): `--profile v1 --selftest`
exit 0 with 18 bullets, identical to pristine's 18 bullets, 0 tracebacks both sides;
`--profile v1 --quiet` exit 1 with `handoff-e2e: exit=1 fields=? glossary=?/20 findings=? packet_sha256=(not assembled)`
**before and after** — the mirror changes no v1 behavior. That red is pre-existing and unrelated to
this patch: `FAIL verdict: 1 read-set file(s) changed since the baseline was frozen: tools/d2-typed-labels.py`
(the round-20-noted claim-O projector pin drift, `reports/round-20/handoff/capability-draft.md:101`).

**Recommendation:** patch A does not depend on this hunk and claim O scopes to the v3 path. Since the
v1 exposure is latent and no control exercises it, applying it is optional; routing it as a named
finding (owner: future round) is equally acceptable. The integrator's call, to be recorded either
way — do not apply it silently.

## Owed

- `reports/round-35/plan/P02-oa-plan.md` — absent at write time (checked repeatedly; `ls
  reports/round-35/plan/` → no such directory). This draft made the convention choice itself and
  recorded its evidence (§1 decision 3, cross-checked against K03 §4). If P02 lands a different
  choice, exactly four sites change and nothing else: hunk A1, hunk A2, the `Failed("E2E-READSET", …)`
  code string in A3, and the control assertions' expected code (B1's or B2's). If P02 picks the exit-2
  family instead, the guard must raise a `BaselineError` subclass rather than `Failed` — which
  contradicts claim O's declared counting command (`(expect: exit 1, named diagnostic)`) and the
  filed `"exit": 1` at `reports/round-34/handoff/repin.json:19-21`, so the claim text would have to be
  reconciled first. Note also O02's contract fixes exit 1 (`O02-controls.md:46-49`), so exit 2 is
  now doubly ruled out by the fragments that bind this patch.
- Control-block decision (§3) is the integrator's: B2 recommended (header 43), B1 as fallback
  (header 40 — clears no `N ≥ 41` leg), both = 44. Exactly one superseded-row control should land.
- `reports/round-35/scout/K03-keyerror-path.md` — landed and read; traceback, exit-class trade,
  m12b-coverage finding and control-count warning all cited above. One correction recorded: K03
  estimated two new controls (header 41/42); the recommended B2 tree measures header 43 / bullets 44.

## Citations

- `tools/exercise-handoff-e2e.py:184` (`CLAIMS_MAP` → `reports/round-34/handoff/declared-in-r7/claims-map.md`)
- `tools/exercise-handoff-e2e.py:89-93`, `:60-61` (docstring exit map, assertion list — edited by A1/A2)
- `tools/exercise-handoff-e2e.py:112-114`, `:244-268` (`EXIT_*`; `Unevaluatable`/`Failed` taxonomy)
- `tools/exercise-handoff-e2e.py:293-300` (`measure`/`read_text` raise `MissingArtifact`)
- `tools/exercise-handoff-e2e.py:1436-1441` (v1 mirror block, optional §6)
- `tools/exercise-handoff-e2e.py:1933-1935` (`V3_BASELINE_DEFAULT`, `V3_FROZEN_DIR_DEFAULT`, `V3_READ_SET`)
- `tools/exercise-handoff-e2e.py:3479-3483` (`V3Assembly` digests over the live read set only)
- `tools/exercise-handoff-e2e.py:3807`, `:3816-3824` (`v3_exercise`; detection `:3820`, crash `:3822`, designed raise `:3823`)
- `tools/exercise-handoff-e2e.py:4154`, `:4179-4185`, `:4192`, `:4422`, `:4430`, `:4448-4463`, `:4464-4467` (v3 selftest; m12a/m12b, insertion point, header-vs-bullet count)
- `tools/exercise-handoff-e2e.py:4556`, `:4603-4604` (v1 branch returns before the edited print; the v3 `handoff-v3: {err}: {detail}` surface)
- `reports/round-34/handoff/repin.json:16-21` (r6 control: exit 1 + KeyError mechanism), `:39` (r34 successor map `d181de28…`)
- `reports/round-30/regression.json:698`, `reports/round-30/regression-initial.json:634`, `reports/round-22/bleed/evidence/attempt-01-verification.json:241`, `reports/round-27/law/impl-4.md:36` (filed verbatim quotations of the unchanged summary line)
- `reports/round-34/run-validation.py:180-183`; `reports/round-30/run-validation.py:71-73`; `reports/round-31/run-validation.py:88-89` (validators read only the green quiet run)
- `reports/round-20/handoff/capability-draft.md:101`, `reports/round-20/handoff/v3.md:76` (pre-existing v1 red; v1 failure line)
- `reports/round-35/claims.json:38-52` (claim O text, counting commands, thresholds)
- `reports/round-35/scout/K03-keyerror-path.md:22-31, 36-40, 53-56, 62-79, 99-120, 131-136, 137-142`
- `reports/round-35/op/O02-controls.md:40-56, 100-105, 107-235, 251-252, 277` (contract items, ordering rule, four controls, measured count, reconciliation request)
- `reports/round-35/op/O08-validation-legs.md:32, 68-85, 182-183` (B3 pre-patch count, `N ≥ 41` leg, count table)
- Commands (all cwd = a `git archive 4a7aede` copy, `TMPDIR=.scratch`; no in-tree runner, no `--freeze`):
  - `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` → pristine: `KeyError` traceback at `:3822`; A and A+B1: exit 1 with the two stdout lines quoted in §4 row 2, stderr 0 bytes
  - `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` → pristine 39/40; A 39/40; A+B1 40/41; A+B2 43/44; A+B1+B2 44/45; all exit 0, 0 tracebacks
  - `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0, `packet_sha256=45f57132…` on every tree
  - `python3 -B tools/exercise-handoff-e2e.py --profile v1 --selftest` / `--profile v1 --quiet` → 18 bullets both sides, exit 1 both sides (pre-existing)
  - `git apply -p1 --check` of A, B1 and the v1 patch in sequence on fresh archives → clean
  - `sha256sum` of the five `reports/round-34/handoff/declared-in-r7/*` files → identical pristine vs patched
  - `grep -rln exercise-handoff-e2e tools/gates/ tools/harness/` → no matches
