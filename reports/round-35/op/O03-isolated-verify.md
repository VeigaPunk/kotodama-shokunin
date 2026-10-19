- Seat: O03 | executor | O | date 2026-10-19 | baseline 4a7aede

# O03 — apply-and-verify the R34-N1 hardening in an isolated `git archive` copy

Mission: extract the patch from O01, apply it in `.scratch`, run the r6-row
replay there (named diagnostic expected) + the r7 default chain (exit 0) +
selftest; report observed outputs.

**Dependency status at run time (05:19–05:36Z).** `reports/round-35/op/` held
only `O04-regressions.md`, `O08-validation-legs.md`, `O10-scribe.md`;
`O01-patch-draft.md` and `O02-controls.md` did **not** exist. Per the
missing-dependency rule I did every part I could: I derived the patch myself,
and I adopted `reports/round-35/plan/P02-oa-plan.md:71-88` (§3 sketch)
**verbatim** as the applied patch — same code (`E2E-READSET`, exit 1
`Failed`), same message text, same precedence shape — so the artifact below is
the verified realization of the round's own plan, not a rival design. The
exact bytes are in §3; the integrator applies them to `tools/`.

## 1. Isolation and the defect, reproduced

```
mkdir -p .scratch/o03-iso && git archive 4a7aede | tar -x -C .scratch/o03-iso/tree
sha256sum .scratch/o03-iso/tree/tools/exercise-handoff-e2e.py tools/exercise-handoff-e2e.py
34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9  .scratch/o03-iso/tree/… (pre-patch)
34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9  tools/… (live; == git show HEAD:…)
```

Pre-patch replay in the unpatched copy (`.scratch/o03-iso/tree-orig`,
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
    --baseline reports/round-30/handoff/declared-in-r6/expected.json
Traceback (most recent call last):
  File "…/tools/exercise-handoff-e2e.py", line 4613, in <module>
    sys.exit(main())
  File "…/tools/exercise-handoff-e2e.py", line 4578, in main
    code, err, records = v3_exercise(root=root, baseline_rel=args.baseline or baseline_default)
  File "…/tools/exercise-handoff-e2e.py", line 3822, in v3_exercise
    record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
                                                                                             ~~~~~~~~~~~~~~~~^^^^^
KeyError: 'reports/round-20/handoff/claims-map.md'
exit=1
```

This matches K03's traceback (`reports/round-35/scout/K03-keyerror-path.md:27-30,48-51`)
line for line. The defect line is the *reporting* step `:3822`; the designed
`E2E-DIGEST` raise at `:3823` is unreachable for membership-only drift.

Drift census (`.scratch/o03-iso/logs/probe-drift.txt`, probe against the
isolated tree):

```
r6: baseline_inputs=58 live_read_set=58 unresolvable=['reports/round-20/handoff/claims-map.md'] drifted=['reports/round-20/handoff/claims-map.md']
r6: live read-set members absent from the baseline: ['reports/round-34/handoff/declared-in-r7/claims-map.md']
r7: baseline_inputs=58 live_read_set=58 unresolvable=[] drifted=[]
```

So the r6 row has exactly one unresolvable member and the r7 row has none —
the guard can be precise and the r7 chain must stay green.

## 2. What the patch changes (4 hunks + 2 one-liners)

- **v3 drift check** (`tools/exercise-handoff-e2e.py:3819-3823` pre-patch): the
  `assembly.digests[rel]` index is guarded; members absent from the live read
  set raise `Failed("E2E-READSET", …)` naming up to three moved paths. Drift
  among *resolvable* members is still recorded before any raise, so a mixed
  baseline hides nothing (P02 §3 property).
- **v1 twin site** (`:1439-1441` pre-patch): the identical three-line pattern
  patched the same way (scope choice — see §7).
- **`--quiet` observability** (`main`, v1 `:4578` / v3 `:4627` pre-patch): the
  failure line printed only under `if err and not args.quiet:`, so the claim's
  own counting command (`--quiet`, "expect: exit 1, named diagnostic") could
  not observe the code. Guard is now `if err:`; a green run's output is
  byte-identical (err is None), only failing runs gain the verdict line.
- **Docstring** (`:63`, `:89-93` pre-patch): `E2E-READSET` added to the
  exit-1 table, assertion 1 extended, `--quiet` behaviour stated. All edits are
  above line 100 — no rendered bytes (the rendered §1 prose near `:2700` is
  untouched, P02 §5).

## 3. The patch bytes (apply with `patch -p1` from the repo root)

Verified applicable to a **fresh** `git archive 4a7aede` copy:

```
$ patch -p1 --dry-run < O03-patch-p1.diff      # checking file tools/exercise-handoff-e2e.py
$ patch -p1        < O03-patch-p1.diff         # patching file tools/exercise-handoff-e2e.py
$ sha256sum tools/exercise-handoff-e2e.py
1a003d677f106e975f8b9ef5b2b990b307236340535d18acf700ec5ab9d5308e
$ python3 -B -c "import ast;ast.parse(open('tools/exercise-handoff-e2e.py').read())"   # AST OK
```

`1a003d67…` is the same digest as the tree on which every leg in §5 was run.
Diff digest: `3d680b13d3f3132ea13a91dafbb4824671fadc2c74091f0c30b757c6bc1c3574`
(150 lines, +84/−6 including hunk headers).

The diff block below is byte-identical to that file (`sha256` of the extracted
block = `3d680b13…`, checked programmatically). Self-sufficiency check: the
block was extracted *from this fragment*, applied with `patch -p1` to a fresh
`git archive 4a7aede` copy, and produced `1a003d67…`; in that copy the r6
replay exited 1 with the `E2E-READSET` line and the r7 chain exited 0 with
`packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`.

```diff
--- a/tools/exercise-handoff-e2e.py
+++ b/tools/exercise-handoff-e2e.py
@@ -60,7 +60,9 @@
 
 Assertions the v3 run makes
 
-  1. read-set digests match the frozen v3 baseline (drift names the file);
+  1. read-set digests match the frozen v3 baseline (drift names the file; a
+     frozen member this revision no longer carries is `E2E-READSET`, naming the
+     moved path);
   2. preflight: 16 fields, non-canon marker, licensed glossary vocabulary, no
      floating version, and the uncertainty/link grammar below;
   3. v2-subset equality: the 15 v2 claims parsed out of the v3 ledger are
@@ -88,9 +90,13 @@
 
 Exit codes (stable messages, no traceback): 0 clean; 1 mismatch —
 `E2E-DIGEST`, `E2E-COUNT`, `E2E-GATE`, `E2E-SCAN`, `E2E-UNC` (uncertainty
-findings), `E2E-LINK` (link findings); 2 could-not-evaluate — `E2E-ARTIFACT`
+findings), `E2E-LINK` (link findings), `E2E-READSET` (a frozen baseline row
+whose read-set member this revision no longer carries — the superseded row
+refuses by name, never a traceback); 2 could-not-evaluate — `E2E-ARTIFACT`
 (missing/unreadable read-set file), `E2E-BASELINE` (absent or edited baseline),
-`E2E-DATA` (malformed input). Writes go only to a fresh directory under
+`E2E-DATA` (malformed input); the verdict line naming the code prints even
+under `--quiet` (the flag suppresses the per-check transcript, not the code).
+Writes go only to a fresh directory under
 `TMPDIR` (plus `--freeze DIR`); the read set is never modified, there is no
 network access, and the tool is stdlib-only (the D2/D4 YAML packets are read
 as bytes with id-level regex extraction, never through a third-party YAML
@@ -1436,8 +1442,16 @@
             rel for rel, digest in baseline["inputs"].items() if assembly.digests.get(rel) != digest
         ]
         if drifted:
+            superseded = [rel for rel in drifted if rel not in assembly.digests]
             for rel in drifted:
-                record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
+                if rel in assembly.digests:
+                    record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
+            if superseded:
+                raise Failed(
+                    "E2E-READSET",
+                    f"{len(superseded)} baseline read-set member(s) are not in this revision's read set: "
+                    f"{', '.join(superseded[:3])} — this baseline row is superseded by a read-set move; replay it against the revision it was frozen at",
+                )
             raise Failed("E2E-DIGEST", f"{len(drifted)} read-set file(s) changed since the baseline was frozen: {', '.join(drifted[:3])}")
         record("input-digest", True, f"{len(V1_READ_SET)} read-set digests match the frozen baseline")
 
@@ -1763,6 +1777,19 @@
         results.append("tamper read-set: exit 1 E2E-DIGEST naming the changed file")
 
         with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
+            superseded_root, _ = v1_freezed_copy(fixture, control_dir, "superseded-row")
+            victim = superseded_root / baseline_rel
+            edited = json.loads(victim.read_text(encoding="utf-8"))
+            moved = edited["inputs"].pop(D2_TYPED)
+            edited["inputs"]["reports/round-20/handoff/claims-map.md"] = moved
+            edited["baseline_digest"] = v1_baseline_digest(edited)
+            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
+            code, err, records = v1_exercise(root=superseded_root, baseline_rel=baseline_rel)
+        assert (code, err) == (EXIT_FAIL, "E2E-READSET"), (code, err, records)
+        assert "reports/round-20/handoff/claims-map.md" in records[-1]["detail"], records[-1]
+        results.append("superseded row: exit 1 E2E-READSET naming the frozen member this revision's read set no longer carries")
+
+        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
             scan_root, _ = v1_freezed_copy(fixture, control_dir, "scan-disagreement")
             victim = scan_root / baseline_rel
             edited = json.loads(victim.read_text(encoding="utf-8"))
@@ -3818,8 +3845,16 @@
 
         drifted = [rel for rel, digest in baseline["inputs"].items() if assembly.digests.get(rel) != digest]
         if drifted:
+            superseded = [rel for rel in drifted if rel not in assembly.digests]
             for rel in drifted:
-                record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
+                if rel in assembly.digests:
+                    record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
+            if superseded:
+                raise Failed(
+                    "E2E-READSET",
+                    f"{len(superseded)} baseline read-set member(s) are not in this revision's read set: "
+                    f"{', '.join(superseded[:3])} — this baseline row is superseded by a read-set move; replay it against the revision it was frozen at",
+                )
             raise Failed("E2E-DIGEST", f"{len(drifted)} read-set file(s) changed since the baseline was frozen: {', '.join(drifted[:3])}")
         record("input-digest", True, f"{len(V3_READ_SET)} read-set digests match the frozen baseline")
 
@@ -4449,6 +4484,46 @@
         results.append("tamper scan expectation: exit 2 E2E-BASELINE (a re-signed expectation is refused, not honoured)")
 
         with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
+            superseded_root, _ = v3_freezed_copy(fixture, control_dir, "superseded-row")
+            victim = superseded_root / baseline_rel
+            edited = json.loads(victim.read_text(encoding="utf-8"))
+            moved = edited["inputs"].pop(CLAIMS_MAP)
+            edited["inputs"]["reports/round-20/handoff/claims-map.md"] = moved
+            edited["baseline_digest"] = v3_baseline_digest(edited)
+            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
+            code, err, records = v3_exercise(root=superseded_root, baseline_rel=baseline_rel)
+            assert (code, err) == (EXIT_FAIL, "E2E-READSET"), (code, err, records)
+            assert "reports/round-20/handoff/claims-map.md" in records[-1]["detail"], records[-1]
+            run = subprocess.run(
+                [sys.executable, str(ROOT / "tools/exercise-handoff-e2e.py"), "--profile", "v3", "--root",
+                 str(superseded_root), "--baseline", baseline_rel, "--quiet"],
+                cwd=control_dir,
+                capture_output=True,
+                text=True,
+            )
+        assert run.returncode == EXIT_FAIL, (run.returncode, run.stdout, run.stderr)
+        assert "E2E-READSET" in run.stdout and "reports/round-20/handoff/claims-map.md" in run.stdout, run.stdout
+        assert "Traceback" not in run.stderr, run.stderr
+        results.append("m12c superseded row: exit 1 E2E-READSET naming the moved read-set member, never a traceback")
+        results.append("m12d observability: the superseded row under --quiet exits 1 and prints its E2E-READSET line naming the moved path")
+
+        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
+            mixed_root, _ = v3_freezed_copy(fixture, control_dir, "superseded-and-drifted")
+            victim = mixed_root / baseline_rel
+            edited = json.loads(victim.read_text(encoding="utf-8"))
+            moved = edited["inputs"].pop(CLAIMS_MAP)
+            edited["inputs"]["reports/round-20/handoff/claims-map.md"] = moved
+            edited["baseline_digest"] = v3_baseline_digest(edited)
+            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
+            drifted_victim = mixed_root / "reports/round-18/d4/replay.md"
+            drifted_victim.write_text(drifted_victim.read_text(encoding="utf-8") + "\n", encoding="utf-8")
+            code, err, records = v3_exercise(root=mixed_root, baseline_rel=baseline_rel)
+        assert (code, err) == (EXIT_FAIL, "E2E-READSET"), (code, err, records)
+        assert "reports/round-20/handoff/claims-map.md" in records[-1]["detail"], records[-1]
+        assert any("reports/round-18/d4/replay.md" in row["detail"] and not row["ok"] for row in records), records
+        results.append("m12e precedence: a moved member decides the code (E2E-READSET) while the resolvable drift is still recorded — nothing hidden")
+
+        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
             missing_root = Path(control_dir) / "missing"
             shutil.copytree(frozen_root, missing_root)
             (missing_root / D4_PACKET).unlink()
@@ -4551,7 +4626,7 @@
             f"glossary={glossary.group(1) if glossary else '?'}/20 findings={findings.group(1) if findings else '?'} "
             f"packet_sha256={matches.group(1) if matches else '(not assembled)'}"
         )
-        if err and not args.quiet:
+        if err:
             print(f"handoff-e2e: {err}: {records[-1]['detail'] if records else ''}")
         if args.json:
             print(json.dumps({"profile": "v1", "root": str(root), "baseline": args.baseline or baseline_default,
@@ -4600,7 +4675,7 @@
         f"v2_subset={subset} alias_leg={alias} "
         f"packet_sha256={matches.group(1) if matches else '(not assembled)'}"
     )
-    if err and not args.quiet:
+    if err:
         print(f"handoff-v3: {err}: {records[-1]['detail'] if records else ''}")
     if args.json:
         print(json.dumps({"profile": "v3", "root": str(root), "baseline": args.baseline or baseline_default,
```

## 4. Line-number map (pre-patch → patched, as applied to 4a7aede)

| surface | pre-patch | patched |
|---|---|---|
| v1 drift check | `1435-1441` | `1435-1450` |
| v1 selftest new control | — | `1779-1790` |
| v3 drift check | `3819-3823` | `3846-3860` |
| v3 selftest new controls | — | `4487-4523` |
| `main` v1 failure print | `4578` | `4626` |
| `main` v3 failure print | `4627` | `4675` |
| docstring table | `63`, `89-93` | `63-65`, `91-98` |

## 5. Applied-and-verified legs (all in the isolated copy, patched bytes `1a003d67…`)

Every command ran with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`;
all writes went to `TMPDIR` under `.scratch/o03-iso/`.

**L1 — the claim's core leg (r6 row).**

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
    --baseline reports/round-30/handoff/declared-in-r6/expected.json
handoff-v3: exit=1 fields=? glossary=?/20 findings=? links=? claims=? statuses=? v2_subset=unequal alias_leg=? packet_sha256=(not assembled)
handoff-v3: E2E-READSET: 1 baseline read-set member(s) are not in this revision's read set: reports/round-20/handoff/claims-map.md — this baseline row is superseded by a read-set move; replay it against the revision it was frozen at
exit=1
```

O08 §2 O1 leg checks, run on the combined output: `grep -c Traceback` → `0`;
`grep -c KeyError` → `0`; `grep -nP '^.*\bE2E-READSET\b.*reports/round-20/handoff/claims-map\.md.*$'`
→ matches line 2 (code token + member path on **one** line, under `--quiet`,
no traceback). `--json` receipt: `profile v3 exit 1 code E2E-READSET`,
`checks = [{"check": "verdict", "ok": false, "detail": "1 baseline read-set
member(s) are not in this revision's read set: reports/round-20/handoff/claims-map.md — …"}]`.

**L2 — r7 default chain regression (claim threshold).**

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
exit=0
```

The sha equals the filed row (`reports/round-34/handoff/repin.json` `R34-D-default-pointer.control.packet_sha256`)
and `sha256sum reports/round-34/handoff/declared-in-r7/packet.md`.

**L3 — v3 selftest (O08 §2 O2).** exit 0; header
`selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0, links=105/105, claims=27, statuses=16/7/4, v2_subset=equal, alias_leg=landed) plus 42 controls:`;
`grep -c '^  - '` → **43** (= N+1); pre-patch N was 39 (P02 §7, O08 §2 O2), so
the patch adds three controls (claim floor was N ≥ 41). Preserved lines:
`m12a tamper baseline: exit 2 E2E-BASELINE …`, `m12b tamper read-set (D4 projection): exit 1 E2E-DIGEST naming the changed file`.
New lines (verbatim):

```
  - m12c superseded row: exit 1 E2E-READSET naming the moved read-set member, never a traceback
  - m12d observability: the superseded row under --quiet exits 1 and prints its E2E-READSET line naming the moved path
  - m12e precedence: a moved member decides the code (E2E-READSET) while the resolvable drift is still recorded — nothing hidden
```

m12c satisfies O08 O2's new-control regex (`E2E-READSET` + `superseded` +
`exit 1`). m12d is a real CLI subprocess run of the superseded fixture under
`--quiet` (asserts stdout carries the code + path and stderr carries no
traceback) — the claim's counting command shape, tested. m12e is P02's N3
mixed case: it asserts `E2E-READSET` **and** that the resolvable drift row is
still in `records`. Note the first draft of m12e tampered `D4_TYPED_LABELS`,
which the `V3Assembly` constructor's D4 pin leg catches first (`E2E-DIGEST`,
observed) — the control now tampers `reports/round-18/d4/replay.md`, an
unpinned read-set member that reaches the drift leg (see L7).

**L4 — v1 selftest.** exit 0, 18 controls, including
`  - superseded row: exit 1 E2E-READSET naming the frozen member this revision's read set no longer carries`.

**L5 — v2 chain (untouched path).**

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v2 --quiet
handoff-v2: exit=0 claims=15 links=50/50 drift=named(tools/harness/packet_links.py round-16)
```

**L6 — negative control, flipped-sha expectation → exit 2 `E2E-BASELINE`** (r7
`expected.json` copied with `packet_sha256 = "0"*64`, not re-signed):

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline …/ctl-flipped-sha.json
handoff-v3: E2E-BASELINE: baseline integrity digest mismatch — the baseline file was edited without re-freezing (re-freeze with --profile v3 --freeze DIR and read the diff it prints)
exit=2
```

**L7 — negative control, content-tampered *resolvable* member → exit 1
`E2E-DIGEST`** (a copy of the patched tree with one newline appended to
`reports/round-18/d4/replay.md`):

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: E2E-DIGEST: 1 read-set file(s) changed since the baseline was frozen: reports/round-18/d4/replay.md
exit=1
```

The designed drift leg is therefore preserved *and reachable*, and the new
superseded branch does not swallow it.

**L8 — negative control, tampered pinned member → exit 1 `E2E-DIGEST`** (newline
appended to `examples/culture-d4/typed-labels.d4.yml`):

```
handoff-v3: E2E-DIGEST: examples/culture-d4/expected-holds.json projection_sha256: the tree recorded c23b0ab532cf… for examples/culture-d4/typed-labels.d4.yml but the bytes measure 91da200a5f5f…
exit=1
```

**L9 — pre-existing red, attributed to baseline (not the patch).** The v1
*default* chain is red at 4a7aede, with and without the patch:

```
$ python3 -B tools/exercise-handoff-e2e.py            # patched tree
handoff-e2e: exit=1 … / handoff-e2e: E2E-DIGEST: 1 read-set file(s) changed since the baseline was frozen: tools/d2-typed-labels.py
$ python3 -B tools/exercise-handoff-e2e.py            # unpatched tree-orig (4a7aede bytes)
FAIL input-digest: tools/d2-typed-labels.py: frozen 0da0015f7003… live 2819f68769df…
FAIL verdict: 1 read-set file(s) changed since the baseline was frozen: tools/d2-typed-labels.py
exit=1
```

Same file, same frozen/live digests, same exit code before and after — a
long-standing drift in `reports/round-11/handoff/expected.json` versus the
round-19 `tools/d2-typed-labels.py`. The only difference the patch makes is
that the code line now prints under `--quiet`. No filed validator in
`reports/round-2[2-9]/run-validation.py` or `reports/round-3[0-4]/run-validation.py`
runs the plain v1 default chain (they run `--profile v2`/`v3`), so nothing
filed depends on it; routed as an observation for the next renderer round, not
absorbed here.

## 5b. Landing-candidate check — `O01-patch-draft.md` §2 (landed after my run)

`O01-patch-draft.md` (19.6 KB) and `O02-controls.md` (19.7 KB) appeared at
05:26/05:23Z, after my legs. I extracted O01's §2 REQUIRED diff
(`.scratch/o03-iso/o01-block0.diff`, sha256
`ebc6e1cc77bbfe9d8619bd778c4977f24db3219de1348aaaee08f756a671f6d1`, 67 lines),
applied it with `patch -p1` to a fresh `git archive 4a7aede` copy, and ran the
legs. Findings:

- It applies cleanly and yields `tools/exercise-handoff-e2e.py` sha256
  `84276189359177325c5b806f86a168936199bd3ac222cc80bdd14e725c6ef1c8`; AST OK.
- r6 replay: **exit 1** (`handoff-v3: exit=1 …`), r7 chain: **exit 0** with
  `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`.
  Same catch class/exit code as mine (`Failed("E2E-READSET")`, O01 §1
  "Decision 2"), different wording, plus a `read-set-roster` record line.
- **Defect (blocks O08 leg O1 as written).** O01 §2 deliberately leaves the
  `--quiet` print byte-identical (`O01-patch-draft.md:40-45`) and does not
  include P02 §4's mandatory companion edit: all three `if err and not
  args.quiet:` guards survive (applied file lines `4548`, `4587`, `4636`).
  Measured on O01's patched copy:

  ```
  $ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline …/declared-in-r6/expected.json 2>&1 | grep -c E2E-READSET
  0            # the token is ABSENT under --quiet — O08 O1's own command shape
  $ python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline …/declared-in-r6/expected.json 2>&1 | grep -n E2E-READSET
  4:handoff-v3: E2E-READSET: 1 read-set member(s) named by the frozen baseline are not in the live read set: reports/round-20/handoff/claims-map.md — the baseline row is superseded (re-point or re-freeze it)
  ```

  O08 §2 O1 runs exactly the `--quiet` form and requires the token in the
  combined output, so landing O01 §2 alone fails the round's own validator leg
  (and fails the declared counting command's "expect: exit 1, named
  diagnostic"). The fix is the one-line `if err:` change (P02 §4), present in
  my §3 diff; O01's control-count is also short of O08 O2's floor on its own —
  measured on O01's patched copy: `--profile v3 --selftest` exits 0 with
  `… plus 40 controls:` and 41 result lines, `m12c superseded row (…): exit 1
  E2E-READSET naming the unresolvable path, never an unhandled KeyError`
  (N = 40 < 41), which is why O02's four controls
  (`O02-controls.md:168-169, 251-252`: m13a/m13b/m14a/m14b, 39 → 43) are the
  complement. Log digests: `o01-selftest.txt`
  `23800fa2db865cc572c10484a68c8691255a736f55ec720ca7d19b1f04b2b9cc`,
  `o01-r6-quiet-combined.txt`
  `5b7b5cc08609c571fce070dc669b28654e54d06c168d12c050bae03e3effb366`.

- **Recommended landing recipe:** one catch-site form (O01 §2 **or** my §3
  diff — both verified here; my §3 additionally carries the `if err:` fix and
  the v1 mirror, O01 §5 offers the v1 mirror separately) **plus** the `if err:`
  one-liner **plus** one control set (O02's four, or my three + v1 control).
  Then re-run the L1/L2/L3 legs on the landed bytes; my verified digests
  (`1a003d67…`, `84276189…`) are per-candidate, not interchangeable.

## 6. Freeze bytes and in-tree state (O08 O4/O5)

```
$ git status --porcelain=v1 -uall -- reports/round-30/handoff/declared-in-r6 reports/round-34/handoff/declared-in-r7
(empty)
live == git show HEAD:  reports/round-30/handoff/declared-in-r6/expected.json
live == git show HEAD:  reports/round-34/handoff/declared-in-r7/packet.md
live == git show HEAD:  reports/round-34/handoff/declared-in-r7/expected.json
live tools/exercise-handoff-e2e.py = 34c85f57… == git show HEAD:…   (patch NOT applied in-tree; the integrator applies it)
```

No `--freeze` was run anywhere (not even in an isolated copy); no filed round
runner was executed; no in-tree file was modified by this seat.

## 7. Scope choices and the one contested decision (for R04 / the integrator)

1. **v1 twin site patched too.** P02 §4 defaulted to "v3 only, minimal blast
   radius" and asked that the choice be flagged. I patched v1 as well because
   the defect is the same three lines and the v1 site now has its own control
   (L4). Dropping the v1 hunk is safe if the integrator prefers the smaller
   diff: the v3 hunk alone satisfies claim O, and the v1 control would then
   need to go too. v2's path has no drift check and was left untouched.
2. **`if err:` in both v1 and v3** (v2's print path unchanged) — load-bearing
   for the claim's counting command, per P02 §4.
3. **Exit code — the genuine fork, both variants measured.**
   - Shipped here: `Failed("E2E-READSET", …)` → **exit 1**. It matches
     `claims.json:48` (`expect: exit 1`), the filed r34 row's recorded exit
     (`reports/round-34/handoff/repin.json` `R34-D-stale-row.control.exit = 1`),
     and P02 §2's decision; O08's binding leg accepts `{1, 2}`.
   - Alternative (`Unevaluatable` subclass, **exit 2**) — what O08 §4 and
     S04 §4 call convention-correct. Measured in a second isolated copy
     (`.scratch/o03-iso/tree-alt2`, `class ReadsetError(Unevaluatable): code = "E2E-READSET"`):

     ```
     $ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline …/declared-in-r6/expected.json
     handoff-v3: exit=2 … / handoff-v3: E2E-READSET: 1 baseline read-set member(s) are not in this revision's read set: reports/round-20/handoff/claims-map.md — …
     exit=2
     $ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
     handoff-v3: exit=0 … packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
     exit=0
     ```

     The exit-2 variant is CLI-verified only: its three selftest control
     assertions were not authored, so adopting it means flipping
     `EXIT_FAIL` → `EXIT_UNEVALUATED` in the v1 control, m12c and m12e (and the
     `run.returncode` assertion), then re-running L3/L4. It also needs the
     `claims.json:48` exit-1 string filed as a named deviation (O08 §4).
4. **Not touched, routed:** the stale docstring cites of the pre-move map
   (P02 §5, F-P02-2) and the internally inconsistent frozen r7 packet prose
   (F-P02-1) are outside claim O and stay with their owners.

## 8. Limits

- Verification is entirely in isolated `git archive` copies under
  `.scratch/o03-iso/`; the patch is **drafted**, and per the shared rules the
  integrator applies it to `tools/exercise-handoff-e2e.py`. The verified byte
  target is sha256 `1a003d677f106e975f8b9ef5b2b990b307236340535d18acf700ec5ab9d5308e`.
- Selftest wall time on this host was 54 s (loaded, 64-seat batch) versus O08's
  38.6 s pre-patch measurement; counts, not timings, are the threshold.
- Raw logs live under `.scratch/o03-iso/logs/` (not durable, and not a
  telemetry path). Digests of the ones cited here:
  `v3-selftest-final.txt d732e7b0f7eb536cf788a3d547b78cd5f11cc51fa014dd7bca7a4b4598fa713a`,
  `v1-selftest-final.txt c4376355fa27d202a803c2be58ff6b213c14456b8d833a0c3dc02b069a215710`,
  `r6-replay-final.txt 5a6e6dffc0cb54e1a2cb3473903fb5e67c257fadfaebdf4aaeecf9f70547b848`,
  `r7-default-final.txt 74afae3367284b03733f296fef135da7aab53f59771fdc649a42d8bfecce1320`,
  `ctl-flipped-sha-final.txt 1603d62ab157378455d46c9fc5fb12109b3d5322f4c5a939611f47cd1a383583`,
  `ctl-drifted-member-final.txt c107d96278125e8fffb77b827c1e40b06485ba687c6a3d71621d3ec3514043cc`,
  `r6-replay-after-json-final.txt 094331a1cccf1426d4374a20d86524a46acd4dbae41722c89742fcb7bd50673f`,
  `probe-drift.txt 3102a0cafee5422b5be6950e828c0ab3415cee525e81c125d743cf44b568fcbf`,
  `v1-default-orig-verbose.txt 5547467f29e88f517a81e72f5c154dccfd109cfad5bcac1cebb27e9d178c55bf`,
  `alt2-r6-replay.txt ce88d08efcde0b4e2a022005ba55df9bd016ea904cde9fed4c6c3f785343dcff`,
  `alt2-r7-default.txt 74afae3367284b03733f296fef135da7aab53f59771fdc649a42d8bfecce1320`.
  The verbatim outputs are embedded above so the fragment stands without them.

## Owed

- `reports/round-35/op/O01-patch-draft.md` — **absent during my legs
  (05:19–05:36Z), landed 05:26Z and checked afterwards** (see §5b). It is not a
  blocker: the landing is single-sourced from §5b's recipe. Two patch variants
  must not land at once; the wording is non-binding per O08 §3, but the `if
  err:` one-liner is not optional (O01 §2 omits it; O08 leg O1 then fails).
- `reports/round-35/op/O02-controls.md` — **absent during my legs, landed
  05:23Z**: its four controls (m13a/m13b/m14a/m14b,
  `O02-controls.md:168-169,251-252`) are the complement O01 §2 needs; my three
  v3 controls + one v1 control (N = 42) satisfy the same O08 O2 requirements.
  Keep exactly one control set in the landed patch, and re-measure the landed
  count (O08 O2 floor: N ≥ 41).
- Integrator action: apply `§3`'s diff to `tools/exercise-handoff-e2e.py` with
  `patch -p1` (verified to reproduce `1a003d67…`), then re-run the L1/L2/L3
  legs in-tree; no `--freeze` against `reports/round-34/handoff/declared-in-r7`.
  If the integrator lands O01 §2 instead, the `if err:` one-liner from `§3`
  **must** ride along (see `§5b`), otherwise O08 leg O1 fails on its own
  `--quiet` command.

## Citations

Paths (all relative to the repo root; `file:line` refers to pre-patch bytes at
4a7aede unless noted):

- `tools/exercise-handoff-e2e.py:244-265` (`Unevaluatable`/`ArtifactError`/`BaselineError`/`Failed`),
  `:88-93` (exit-code table), `:462` `V1_READ_SET`, `:1935-1960` `V3_READ_SET` +
  `V3_BASELINE_DEFAULT`/`V3_FROZEN_DIR_DEFAULT`, `:184` `CLAIMS_MAP`,
  `:172-177` `D4_RECEIPTS`, `:293-302` `measure`, `:1435-1441` v1 drift check,
  `:3819-3823` v3 drift check, `:4578`/`:4627` `main` failure prints,
  `:1635` `v1_selftest`, `:4154` `v3_selftest`, `:1614-1633`/`:4131-4171` fixture helpers.
- `reports/round-30/handoff/declared-in-r6/expected.json` (`inputs` names
  `reports/round-20/handoff/claims-map.md`; 58 inputs; `packet_sha256`
  `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb`).
- `reports/round-34/handoff/declared-in-r7/expected.json` (58 inputs, zero
  unresolvable), `.../packet.md` (sha256 `45f57132…`), `.../freeze.txt`.
- `reports/round-34/handoff/repin.json` (R34-D-default-pointer control
  `exit 0`, packet sha; R34-D-stale-row control `exit 1`, KeyError mechanism;
  `named_findings[0]` = R34-N1 routed to renderer hardening).
- `reports/round-35/claims.json:38-52` (claim O text, `after_required`,
  counting commands, thresholds), `:67-73` (non-goals).
- `reports/round-35/targets.json` (seat O03 mission/out; shared_rules).
- `reports/round-35/plan/P02-oa-plan.md:50-128` (§2 decision `E2E-READSET` exit 1,
  §3 sketch applied verbatim, §4 `--quiet` companion edit, §7 control list N1–N3).
- `reports/round-35/scout/K03-keyerror-path.md:27-30,44-51,101-119`.
- `reports/round-35/op/O08-validation-legs.md:53-88` (legs O1/O2/O3), `:99-134`
  (O4/O5/O6), `:136-174` (diagnostic shape, exit-code policy).
- `reports/round-35/scribe/S04-integration-draft.md:547,616-618,786-805`.
- `reports/round-35/op/O01-patch-draft.md:17,31-45,59-127,149-152,192-216,236-239`
  (§2 diff extracted and applied; `:40-45` the deliberate `--quiet` non-change).
- `reports/round-35/op/O02-controls.md:46-55,93,108-160,168-169,182-212,240-252,270-277`
  (control interface contract, m13a/m13b/m14a/m14b, 39 → 43).
- `reports/round-27/run-validation.py:1431`, `reports/round-28/run-validation.py:1398`
  (filed successor-replay legs consume exit codes only),
  `reports/round-34/run-validation.py:176-183` (D5-quiet leg parses
  `packet_sha256` from a green run).

Commands (all run by this seat; `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `git archive 4a7aede | tar -x -C .scratch/o03-iso/tree` (+ `tree-orig`, `tree-apply`, `tree-tamper`, `tree-alt2`)
- `sha256sum .scratch/o03-iso/tree/tools/exercise-handoff-e2e.py tools/exercise-handoff-e2e.py`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` (pre-patch: traceback/exit 1; post-patch: `E2E-READSET`/exit 1; `--json` receipt)
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` (exit 0, packet sha `45f57132…`)
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` (exit 0, 42 controls, 43 result lines)
- `python3 -B tools/exercise-handoff-e2e.py --profile v1 --selftest` (exit 0, 18 controls)
- `python3 -B tools/exercise-handoff-e2e.py --profile v2 --quiet` (exit 0)
- `python3 -B tools/exercise-handoff-e2e.py` (v1 default; exit 1 `E2E-DIGEST tools/d2-typed-labels.py`, identical pre-patch)
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline .scratch/o03-iso/ctl-flipped-sha.json` (exit 2 `E2E-BASELINE`)
- `python3 -B .scratch/o03-iso/probe-drift.py .scratch/o03-iso/tree`
- `diff -u --label a/tools/exercise-handoff-e2e.py --label b/tools/exercise-handoff-e2e.py <orig> <patched>` → `.scratch/o03-iso/O03-patch-p1.diff`
- `patch -p1 --dry-run < ../O03-patch-p1.diff && patch -p1 < ../O03-patch-p1.diff && sha256sum tools/exercise-handoff-e2e.py` in `.scratch/o03-iso/tree-apply`
- `git status --porcelain=v1 -uall -- reports/round-30/handoff/declared-in-r6 reports/round-34/handoff/declared-in-r7`
- `grep -c Traceback / grep -c KeyError / grep -nP '^.*\bE2E-READSET\b.*reports/round-20/handoff/claims-map\.md.*$'` over the r6 replay output
