- Seat: O01 | executor | claim O | date 2026-10-19 | baseline 9bccc9b

# O01 — roster-guard design: a D4-scoped, record-only manifest-vs-read-set check

**Verdict.** The guard claim O asks for is landable, and its *only* safe shape is
**D4-scoped, record-only (name, never raise), placed before the existing
supersession abort**. Measured in isolated `git archive 9bccc9b` copies
(`TMPDIR=$PWD/.scratch`): the r7 default chain stays **exit 0** with packet
`45f57132…` byte-identical and exactly one named row
(`examples/culture-d4/components/13-register-law.yml`); the full
`--profile v3 --selftest` exits **0** with the two new controls (43 → **45**).
The two rejected shapes are measured too: a **raising** guard reds the r7 chain
(`exit 1 E2E-READSET`), and a **global** (all-tree) guard names **7** rows — 6
of them the legitimate D2 partial read set. **Zero filed bytes moved; no
in-tree round-runner executed; no re-freeze of `declared-in-r7`.**

This seat had **no landed scout dependency**: `reports/round-38/scout/K02-roster-guard.md`
and `reports/round-38/cross/X00-connector.md` are both absent (two of the 10
missing seats). The design below is derived directly from the renderer source and
from the landed O-block fragments O04/O05/R02/X02/A01.

## 1. The compared pair — which two sets, and why the obvious pair is vacuous

Claim O's own wording (`reports/round-38/claims.json`) is "a frozen baseline's read
set and the packet's own component manifest disagree". The pair that *measures* is:

- **manifest side** — the packet's authored component roster, mined by
  `v3_mine_d4` at `tools/exercise-handoff-e2e.py:2045-2056` from the packet's own
  `assembly.source_sha256` block (`examples/culture-d4/packet.d4.yml:2888`):
  **13 members** today.
- **read-set side** — `V3_READ_SET` (`tools/exercise-handoff-e2e.py:1939-1965`):
  **58 members**, carrying 12 of the 13 D4 components.

The packet's **artifact_manifest** (`A-01`…`A-58`) is **read-set-derived**:
`v3_manifest_rows` (`:2585-2590`) builds one row per `V3_READ_SET` member, and
`assert_manifest_equality` (`:3646-3662`) hard-requires
`checked == len(V3_READ_SET)`. A guard comparing the artifact manifest against the
read set is therefore **trivially always in sync** — a vacuous pass. This matches
O04 §1 and O05 §1 independently; it is the reason the pair above, not the obvious
one, is the guard's subject.

Live probe (isolated copy, no patch):

```text
V3_READ_SET len 58 | D4_COMPONENTS len 12 | d4 manifest members 13
outside read set: ['examples/culture-d4/components/13-register-law.yml']
D4_COMPONENTS vs manifest gap: ['examples/culture-d4/components/13-register-law.yml']
D2 manifest 9 outside 6 | D3 manifest 4 outside 0
```

So D4 is the only in-scope tree with a gap; D2's gap is **intentional**
(`tools/exercise-handoff-e2e.py:51-52` documents the four D2 component inputs the
D2 selftest fixture copies, and `D2_COMPONENT_INPUTS` at `:2255-2262` names 4
paths) and D3 is clean. This is the measurement that forces the D4 scope in §3.

## 2. The guard point — and the ordering constraint X02 raises

Insert inside `v3_exercise`, immediately after `assembly = V3Assembly(root)`
(`tools/exercise-handoff-e2e.py:3821`) and **before** the `dropped = …` supersession
block at `:3823`, so the existing check keeps priority.

X02 (`reports/round-38/cross/X02-honesty.md` §4b, constraint 1) warns that an
isolation run against r2/r5/r6 aborts at `E2E-READSET` before any *later-added*
check is reached, which would make O08's replay produce no manifest verdict. Placing
the guard **before** the abort resolves it: `record()` appends to `records` before
the `raise`, and the CLI prints the whole record list even on the failing path
(`:4660-4663`). Measured on all four filed rows with the patch applied:

```text
r2 (declared-in-r2): FAIL manifest-roster 13-register-law.yml … | FAIL read-set-roster claims-map.md | exit 1 E2E-READSET
r5 (declared-in-r5): FAIL manifest-roster 13-register-law.yml … | FAIL read-set-roster claims-map.md | exit 1 E2E-READSET
r6 (declared-in-r6): FAIL manifest-roster 13-register-law.yml … | FAIL read-set-roster claims-map.md | exit 1 E2E-READSET
r7 (declared-in-r7): FAIL manifest-roster 13-register-law.yml … | exit 0, code None
```

The manifest-roster row is emitted in **every** case. Note the row text says the
bytes are still digest-checked: this guard adds **naming/completeness**, not
detection — `v3_verify_component_digests` (`:2208-2222`) already raises
`E2E-DIGEST` on a mutated 13th component with or without the read-set expansion
(O05 §4, A01 §26-31). Claim O must not be reported as closing a detection gap.

The record name is deliberately **`manifest-roster`**, distinct from the existing
`read-set-roster` (`:3827`), so the two classes are not indistinguishable in the
same run (R02 Finding 1 + guard-point note).

## 3. Rejected shapes, measured

| shape | r7 default chain | rows named | selftest | verdict |
|---|---|---|---|---|
| **D4-scoped, record-only (recommended)** | exit **0**, packet `45f57132…` | **1** (the D4 member) | exit **0**, 45 controls | accept |
| D4-scoped, **raising** `E2E-READSET` | exit **1** | 1 | positive run breaks | **reject** — violates claim O's own "r7 default chain still exits 0 unchanged" |
| **global** (D2+D3+D4 manifest vs read set) | exit 0 (record-only) | **7** (6 D2 false reds + 1 D4) | n/a | **reject** — harms operability; reddens the legitimate green path |

The raising shape's rejection is not a judgment call: R02 Finding 3 measured that a
raising guard also **breaks the selftest's own positive run**, because the fixture
freeze pins exactly `V3_READ_SET` (`:4165-4169`) and so reproduces the asymmetry.
The global shape's 6 D2 rows are false reds against a documented partial read set.

## 4. Interaction with the D claim and the successor baseline

- **The guard does not move any digest.** The record-only guard changes no bytes;
  the r7 packet sha stays `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`
  (filed `reports/round-34/handoff/declared-in-r7/packet.md`). So the D pins census
  is untouched by the O guard (R03 cross-claim: no D leg reads a `manifest-roster`
  row).
- **After the fix route lands, the guard goes green — not silent.** Reproducing
  O04 variant C in isolation (read set 59 members + the two default constants
  re-pointed to a successor dir) and running the patched guard:

  ```text
  OK manifest-roster: the packet component manifest (13 members) is carried by the live read set (59 members)
  handoff-v3: exit=0 … packet_sha256=26a7882d313d63101de5f3fb9ff97457df2a670c1e814cc6ffaf340963c14ffa
  ```

  (The digest differs from O04/O05's `b102aa70…`/`9e003970…` because the renderer
  emits `V3_BASELINE_DEFAULT` into the packet prose at `:3189`, so the successor
  digest is a function of the successor *path name* — O05 D-2. The successor dir
  used here is `reports/round-38/handoff/declared-in-r8`.) So the guard names the
  row **until** a successor baseline exists, then reports in-sync; it never
  silently disables itself.

## 5. The check, factored for cheap fixtures

The gap computation is factored into a pure helper so the selftest controls are
unit-level and do not need to freeze two more trees:

```python
def v3_manifest_roster_gap(manifest, read_set):
    """Members of a packet component manifest that the live read set does not carry.

    The packet's own `assembly.source_sha256` block is the authored roster; the
    artifact_manifest is read-set-derived and therefore always agrees with it, so
    this pair is the only non-vacuous one. Direction is manifest -> read set (the
    opposite of the superseded-row check, which reads baseline -> live read set).
    """
    return sorted(set(manifest) - set(read_set))
```

## 6. Patch draft (fenced — the integrator applies; no filed byte written here)

Applies cleanly to the HEAD tool (`sha256
bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9`); verified
with `patch -p1 --dry-run` in a fresh `git archive` copy → `PATCH_OK`. Patched tool
sha256 `e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553`; the
patch draft itself is `c4141c716c5b634051ae8dd2cb6fbc13893b291f9ce6913a8a60e7bc4e0e4d9d`.

```diff
--- a/tools/exercise-handoff-e2e.py
+++ b/tools/exercise-handoff-e2e.py
@@ -168,6 +168,7 @@
     "examples/culture-d4/components/11-contact-history.yml",
     "examples/culture-d4/components/12-provenance.yml",
 )
+D4_ROSTER_MEMBER = "examples/culture-d4/components/13-register-law.yml"
 D4_ASSEMBLER = "tools/assemble-culture-d4.py"
 D4_TYPED_TOOL = "tools/assemble-d4-typed.py"
 D4_TYPED_GATE = "tools/gates/d4-typed-labels-check-gate.py"
@@ -3808,6 +3809,17 @@
     return path, baseline
 
 
+def v3_manifest_roster_gap(manifest, read_set):
+    """Members of a packet component manifest that the live read set does not carry.
+
+    The packet's own `assembly.source_sha256` block is the authored roster; the
+    artifact_manifest is read-set-derived and therefore always agrees with it, so
+    this pair is the only non-vacuous one. Direction is manifest -> read set (the
+    opposite of the superseded-row check, which reads baseline -> live read set).
+    """
+    return sorted(set(manifest) - set(read_set))
+
+
 def v3_exercise(root=ROOT, baseline_rel=V3_BASELINE_DEFAULT):
     """Run the v3 exercise; return (exit code, code-or-None, records)."""
     records = []
@@ -3820,6 +3832,23 @@
         snapshot_before = {rel: measure(root, rel)[0] for rel in V3_READ_SET}
         assembly = V3Assembly(root)
 
+        roster_gap = v3_manifest_roster_gap(assembly.d4["components"], V3_READ_SET)
+        for rel in roster_gap:
+            record(
+                "manifest-roster",
+                False,
+                f"{rel}: in the packet component manifest ({len(assembly.d4['components'])} members, "
+                f"packet.d4.yml assembly.source_sha256) but not in the live read set "
+                f"({len(V3_READ_SET)} members) — the roster is incomplete; the bytes are still digest-checked",
+            )
+        if not roster_gap:
+            record(
+                "manifest-roster",
+                True,
+                f"the packet component manifest ({len(assembly.d4['components'])} members) is carried by the "
+                f"live read set ({len(V3_READ_SET)} members)",
+            )
+
         dropped = sorted(rel for rel in baseline["inputs"] if rel not in assembly.digests)
         if dropped:
             for rel in dropped:
@@ -4511,6 +4540,37 @@
         )
 
         with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
+            sync_root, _ = v3_freezed_copy(fixture, control_dir, "roster-sync")
+            live_gap = v3_manifest_roster_gap(V3Assembly(sync_root).d4["components"], V3_READ_SET)
+            assert live_gap == [D4_ROSTER_MEMBER], live_gap
+            code, err, records = v3_exercise(root=sync_root, baseline_rel=baseline_rel)
+            named = [row for row in records if row["check"] == "manifest-roster" and not row["ok"]]
+        assert code == EXIT_PASS, (code, err)
+        assert [row["detail"].split(":")[0] for row in named] == [D4_ROSTER_MEMBER], named
+        results.append(
+            f"m15a roster gap named, not raised: exit {code} {err} with a manifest-roster row naming "
+            f"{D4_ROSTER_MEMBER} (the r7 class; the read set still carries every frozen member)"
+        )
+
+        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
+            expanded = (*V3_READ_SET, D4_ROSTER_MEMBER)
+            original_read_set = V3_READ_SET
+            globals()["V3_READ_SET"] = expanded
+            try:
+                synced_root, _ = v3_freezed_copy(fixture, control_dir, "roster-in-sync")
+                code, err, records = v3_exercise(root=synced_root, baseline_rel=baseline_rel)
+            finally:
+                globals()["V3_READ_SET"] = original_read_set
+            green = [row for row in records if row["check"] == "manifest-roster"]
+        assert code == EXIT_PASS, (code, err)
+        assert green and all(row["ok"] for row in green), green
+        assert D4_ROSTER_MEMBER in str(green[-1]["detail"]) or "carried by the" in green[-1]["detail"], green
+        results.append(
+            "m15b in-sync roster green: the read set carries every manifest member, exit 0 with the "
+            "manifest-roster row green"
+        )
+
+        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
             v2_root, _ = v3_freezed_copy(fixture, control_dir, "retouched-v2")
             victim = v2_root / V2_PACKET_YML
             victim.write_text(victim.read_text(encoding="utf-8").replace("status: \"supported\"", "status: \"partial\"", 1), encoding="utf-8")
```

### 6.1 Selftest fixtures (the two claim-O controls, named)

| id | control | fixture | expected |
|---|---|---|---|
| `m15a` | manifest member not in the read set is **named**, not raised | fresh `v3_freezed_copy` of the live fixture (D4 manifest 13, read set 58) | `exit 0`, exactly one `manifest-roster` row naming `13-register-law.yml` |
| `m15b` | in-sync roster is **green** | same, with `V3_READ_SET` temporarily expanded to 59 and re-frozen | `exit 0`, one `manifest-roster` row, `ok=True`, "carried by the live read set (59 members)" |

Both are unit-level where possible: `v3_manifest_roster_gap` is exercised directly
(the assertion `live_gap == [D4_ROSTER_MEMBER]` in `m15a`), and the full exercise
run is asserted for the record shape. Measured results:

```text
selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0,
links=105/105, claims=27, statuses=16/7/4, v2_subset=equal, alias_leg=landed) plus 45 controls:
  - m15a roster gap named, not raised: exit 0 None with a manifest-roster row naming
    examples/culture-d4/components/13-register-law.yml (the r7 class; the read set still
    carries every frozen member)
  - m15b in-sync roster green: the read set carries every manifest member, exit 0 with the
    manifest-roster row green
```

`m15b` uses `globals()["V3_READ_SET"] = expanded` because `v3_exercise` reads the
module-global; the `finally` restores it, so no later control sees the expansion.
The existing `v3_freezed_copy`/`v3_build_fixture_root` machinery already builds the
fixture from the live read set (`:4165-4168`), so no new fixture builder is owed.

## 7. What the guard is, in one line

A **named completeness check**: "the packet says it has 13 authored D4 components;
the run's read set carries 12 of them" — emitted before the supersession abort,
never raising, never touching a digest. It is the instrument that makes the
`R36-R7-READSET-13` class visible at run time instead of only in a reviewer's
adjudication file.

## Owed

- **O02 (isolated verify):** re-measure §3's three-shape table and §2's four-row
  ordering independently; this seat's readings are one seat's. The patch draft in
  §6 is the artifact to apply in a fresh `git archive` copy — do **not** apply it
  in-tree.
- **O03 / R02 / R03:** the pair choice (§1) and the ordering placement (§2) are the
  falsifiable gates; re-derive that the artifact manifest is read-set-derived rather
  than trusting §1's citation.
- **O08 (regression sweep):** the expectation must be rewritten — r6 names too
  (X02 §4a), and r2/r5/r6 report the pre-existing `E2E-READSET` **in addition to**
  the new `manifest-roster` row. The sweep's correct reading is: "the new D4 guard
  adds exactly one row (`13-register-law.yml`) to every row that reaches it, and
  changes no existing row's verdict."
- **Integrator:** apply §6 as one step (the helper + guard + two fixtures are a
  single coherent edit); the `D4_ROSTER_MEMBER` constant is optional sugar — the
  guard works without it if the fixture block is rewritten to spell the path.
- **Not owed / out of scope:** no read-set edit, no re-freeze, no `CLAIMS_MAP`
  move, no filed-byte rewrite, no freshness axis-move.

## Citations

- `tools/exercise-handoff-e2e.py:51-59,157-171,188,1937-1965,2045-2056,2208-2222,2255-2262,2585-2590,3189,3646-3662,3811-3838,4165-4169,4660-4663`
- `examples/culture-d4/packet.d4.yml:2888`; `examples/culture-d4/components/13-register-law.yml` (`sha256 c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`)
- `reports/round-38/claims.json` (claim O); `reports/round-38/targets.json` (seats O01-O08)
- `reports/round-38/op/O04-fix-route.md` §1-§2; `reports/round-38/op/O05-verify-route.md` §1-§4; `reports/round-38/review/R02-o-review.md` Findings 1-3,6; `reports/round-38/cross/X02-honesty.md` §4,§4b; `reports/round-38/adj/A01-scope.md:110-143`
- `reports/round-37/adj/A01-freeze-adjudication.md:5,19,26-35`; `reports/round-37/op/defect-queue.json` (`R36-R7-READSET-13`)
- Command evidence (isolated `git archive 9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` copies, `TMPDIR=$PWD/.scratch`; no in-tree runner executed, `git status --short` → `?? reports/round-38/` only):
  - `.scratch/o01/base` (patched, D4-scoped record-only): `--profile v3 --quiet` → exit 0, packet `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`; `--profile v3` → `FAIL manifest-roster: examples/culture-d4/components/13-register-law.yml: in the packet component manifest (13 members, packet.d4.yml assembly.source_sha256) but not in the live read set (58 members) — the roster is incomplete; the bytes are still digest-checked`; `--profile v3 --selftest` → exit 0, "plus 45 controls"
  - `.scratch/o01/base`: `--baseline reports/round-22/handoff/declared-in-r2/expected.json` → exit 1 `E2E-READSET`, records carry `manifest-roster` **and** `read-set-roster`; same for `declared-in-r5`, `declared-in-r6`; `declared-in-r7` → exit 0 with `manifest-roster` only
  - `.scratch/o01/raise` (D4-scoped raising): `--profile v3 --quiet` → exit 1, `E2E-READSET: 1 packet component manifest member(s) are not in the live read set: examples/culture-d4/components/13-register-law.yml`
  - `.scratch/o01/global` (all-tree record-only): `--profile v3` → **7** `FAIL manifest-roster` lines; `--profile v3 --quiet` → exit 0 (the false reds do not raise)
  - `.scratch/o01/vC` (variant C + guard): `--freeze reports/round-38/handoff/declared-in-r8` → exit 0; `--profile v3` → `OK manifest-roster: the packet component manifest (13 members) is carried by the live read set (59 members)`, exit 0, packet `26a7882d313d63101de5f3fb9ff97457df2a670c1e814cc6ffaf340963c14ffa`
  - helper probe (`.scratch/o01/base`): `v3_manifest_roster_gap` → D4 `['…/13-register-law.yml']`, D4 in-sync `[]`, D2 6 members, D3 `[]`
  - `patch -p1 --dry-run < .scratch/o01/o01-guard.patch` in a fresh archive → `PATCH_OK`
  - `sha256sum tools/exercise-handoff-e2e.py` → `bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9`; patched tool → `e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553`; patch draft → `c4141c716c5b634051ae8dd2cb6fbc13893b291f9ce6913a8a60e7bc4e0e4d9d`; r7 `expected.json` → `bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55` (unmoved)
