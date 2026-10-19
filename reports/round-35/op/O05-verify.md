- Seat: O05 | verifier | claim O | date 2026-10-19 | baseline 4a7aede

# O05 — independent isolated-copy verification of the R34-N1 hardening (claim O)

**Mission** (`reports/round-35/targets.json:212`): independent isolated-copy
verification of O03's claims — rebuild the archive yourself; file defects.

**Dependency status at write time (2026-10-19T05:30Z).** `reports/round-35/op/`
holds O02, O04, O06, O08, O10; **`O01-patch-draft.md` and
`O03-isolated-verify.md` never landed during this run** (`ls reports/round-35/op/`).
I therefore could not verify O03's *bytes*; instead I (a) rebuilt the archive
myself, (b) reproduced the defect independently, (c) implemented a candidate
hardening in my own isolated copy, and (d) verified it against claim O's declared
acceptance (`claims.json:38-51`) **and** against O08's binding legs
(`op/O08-validation-legs.md:53-135`) and R04's integration obligations
(`review/R04-o-review.md:136-165`), which landed while I worked. The owed
comparison against O01/O03 is recorded under `## Owed`.

## 1. Independent reproduction (my own archive, nothing run in-tree)

Archive: `git archive 4a7aede | tar -x -C .scratch/o05/repo` (HEAD of the lane
tree is `4a7aede`; `git status --porcelain` → `?? reports/round-35/` only).
The live renderer and the archive copy are byte-identical, so patch context taken
from the archive is valid for the live file:

```
live  sha256 tools/exercise-handoff-e2e.py = 34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9
arch  sha256 tools/exercise-handoff-e2e.py = 34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9
```

**Pre-patch defect (reproduced, exit 1, raw traceback):**

```
$ cd .scratch/o05/repo && python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
    --baseline reports/round-30/handoff/declared-in-r6/expected.json
EXIT=1
Traceback (most recent call last):
  ...
  File ".../tools/exercise-handoff-e2e.py", line 3822, in v3_exercise
    record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
KeyError: 'reports/round-20/handoff/claims-map.md'
```

Root cause (my reading, matching K03 and R04 §3): `tools/exercise-handoff-e2e.py:3819`
builds the drift list from the **baseline's** `inputs` map, but `:3822` formats
the per-row detail with a **direct index** into `assembly.digests`, which is keyed
only by the live `V3_READ_SET`. The r6 baseline names
`reports/round-20/handoff/claims-map.md`; the live read set names its successor
via `CLAIMS_MAP` (`:184` = `reports/round-34/handoff/declared-in-r7/claims-map.md`).
The refusal is the control's intent (`reports/round-34/handoff/repin.json:20-21`
records `"exit": 1` and the KeyError mechanism; `:49-51` routes R34-N1 as
`state: routed`, owner "renderer hardening (future round)"); the *mechanism* is an
unhandled exception.

**Row-set census (measured by importing the tool module and comparing sets):**

| baseline | baseline rows | live read set | unresolvable rows | live-only rows |
|---|---|---|---|---|
| `reports/round-11/handoff/expected.json` (v1) | 21 | 21 | NONE | 0 |
| `reports/round-30/handoff/declared-in-r6/expected.json` | 58 | 58 | `reports/round-20/handoff/claims-map.md` | 1 (`…/declared-in-r7/claims-map.md`) |
| `reports/round-34/handoff/declared-in-r7/expected.json` | 58 | 58 | NONE | 0 |

The comparison must stay one-way (baseline rows → live set): a live-only member
must keep being ignored, or every pre-r34 row would emit a second finding class
(R04 §3, final bullet).

**Pre-patch baseline behaviour I measured for the before→after table:**

| command | pre-patch |
|---|---|
| r6 replay, `--quiet` | exit 1, traceback, `KeyError` (§ above) |
| r6 replay, non-quiet | same crash; no `FAIL`/verdict line survives |
| `--profile v3 --quiet` (r7 default) | exit 0 — `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` |
| `--profile v3 --selftest` | exit 0, header `… plus 39 controls:`, 40 `^  - ` lines |
| default profile (v1) | exit 1 — `tools/d2-typed-labels.py` drift; **pre-existing at 4a7aede** (identical in the pristine archive and after my patch, diff of the `FAIL` lines empty) |
| `--profile v2 --quiet` | exit 0 — `handoff-v2: exit=0 claims=15 links=50/50 drift=named(tools/harness/packet_links.py round-16)` |

## 2. The candidate patch I verified (draft — the integrator applies it)

I wrote no `tools/**` byte in the lane tree. The patch below exists only in my
isolated copy; the integrator applies it (or O01's equivalent) to the live file.

- patched file sha256 `2e126e4f98ebe498b6173474a55bedaa953512dd8d6e56f7fabb6280cd6ea56e`
  (pre-patch `34c85f57…`), diff sha256 `cae4b999963719529f8a7e262a1493af8d414cbc4249e3e39bd5dec296f1f090`,
  105 diff lines, 5 hunks. Scratch copies kept for this round:
  `.scratch/o05/repo/tools/exercise-handoff-e2e.py` and `.scratch/o05/O05-candidate-final.patch`.
  The fenced block below differs from that patch file only in the `+++` header
  path (the block names the live path so it applies with `patch -p0`); extracted
  verbatim it is sha256 `edd438615b54472e743a1c805a7b66a4bfc628749a3d8fcb01d41635b97062d2`.
- **The fenced diff below applies cleanly to the live pre-patch bytes**: extracted
  from this fragment into `.scratch/o05/embedded.patch` and run against a *copy* of
  the live file in `.scratch/o05/apply-test/` — `patch -p0 --dry-run` exit 0, then
  `patch -p0` reproduces sha256 `2e126e4f…`, identical to the verified copy. The
  live file was never written to.

Design, in one sentence: **classify before comparing** (R04's S2 shape,
`review/R04-o-review.md:71`) — refuse a baseline whose read-set row is absent from
the live read set with a new named code `E2E-READSET` raised as `Failed`
(exit 1), keep the drift leg untouched, and make the diagnostic visible in the
`--quiet` mode that claim O's own counting command uses (`claims.json:48`).

```diff
--- tools/exercise-handoff-e2e.py	2026-10-19 04:33:13.997085875 -0300
+++ tools/exercise-handoff-e2e.py	2026-10-19 05:24:58.630198501 -0300
@@ -60,7 +60,9 @@
 
 Assertions the v3 run makes
 
-  1. read-set digests match the frozen v3 baseline (drift names the file);
+  1. read-set digests match the frozen v3 baseline (drift names the file); a
+     frozen row that is absent from the live read set is `E2E-READSET`, naming
+     the unresolvable member — never an unhandled `KeyError`;
   2. preflight: 16 fields, non-canon marker, licensed glossary vocabulary, no
      floating version, and the uncertainty/link grammar below;
   3. v2-subset equality: the 15 v2 claims parsed out of the v3 ledger are
@@ -88,7 +90,9 @@
 
 Exit codes (stable messages, no traceback): 0 clean; 1 mismatch —
 `E2E-DIGEST`, `E2E-COUNT`, `E2E-GATE`, `E2E-SCAN`, `E2E-UNC` (uncertainty
-findings), `E2E-LINK` (link findings); 2 could-not-evaluate — `E2E-ARTIFACT`
+findings), `E2E-LINK` (link findings), `E2E-READSET` (a frozen baseline row is
+absent from the live read set — the baseline is superseded, not silently
+re-drifted); 2 could-not-evaluate — `E2E-ARTIFACT`
 (missing/unreadable read-set file), `E2E-BASELINE` (absent or edited baseline),
 `E2E-DATA` (malformed input). Writes go only to a fresh directory under
 `TMPDIR` (plus `--freeze DIR`); the read set is never modified, there is no
@@ -3816,6 +3820,16 @@
         snapshot_before = {rel: measure(root, rel)[0] for rel in V3_READ_SET}
         assembly = V3Assembly(root)
 
+        missing = [rel for rel in baseline["inputs"] if rel not in assembly.digests]
+        if missing:
+            for rel in missing:
+                record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live: absent from the live read set (superseded baseline row)")
+            raise Failed(
+                "E2E-READSET",
+                f"{len(missing)} frozen read-set row(s) are not in the live read set: {', '.join(missing[:3])} "
+                "(drift not evaluated for these rows)",
+            )
+
         drifted = [rel for rel, digest in baseline["inputs"].items() if assembly.digests.get(rel) != digest]
         if drifted:
             for rel in drifted:
@@ -4430,6 +4444,43 @@
         results.append("m12b tamper read-set (D4 projection): exit 1 E2E-DIGEST naming the changed file")
 
         with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
+            superseded_root, _ = v3_freezed_copy(fixture, control_dir, "superseded-row")
+            superseded_rel = "reports/round-20/handoff/claims-map.md"
+            assert superseded_rel not in V3_READ_SET, "control anchor: the superseded row must not be in the live read set"
+            victim = superseded_root / baseline_rel
+            edited = json.loads(victim.read_text(encoding="utf-8"))
+            edited["inputs"][superseded_rel] = edited["inputs"].pop(CLAIMS_MAP)
+            edited["baseline_digest"] = v3_baseline_digest(edited)
+            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
+            code, err, records = v3_exercise(root=superseded_root, baseline_rel=baseline_rel)
+        assert (code, err) == (EXIT_FAIL, "E2E-READSET"), (code, err, records)
+        assert any(superseded_rel in item["detail"] for item in records if not item["ok"]), records
+        results.append(
+            "superseded baseline row: exit 1 E2E-READSET naming the unresolvable member "
+            "(never an unhandled KeyError, never swallowed by the E2E-DIGEST drift leg)"
+        )
+
+        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
+            mixed_root, _ = v3_freezed_copy(fixture, control_dir, "mixed-unresolvable-drifted")
+            superseded_rel = "reports/round-20/handoff/claims-map.md"
+            victim = mixed_root / baseline_rel
+            edited = json.loads(victim.read_text(encoding="utf-8"))
+            edited["inputs"][superseded_rel] = edited["inputs"].pop(CLAIMS_MAP)
+            edited["baseline_digest"] = v3_baseline_digest(edited)
+            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
+            drifted = mixed_root / D4_BRIEF
+            drifted.write_text(drifted.read_text(encoding="utf-8") + "\n", encoding="utf-8")
+            code, err, records = v3_exercise(root=mixed_root, baseline_rel=baseline_rel)
+        assert (code, err) == (EXIT_FAIL, "E2E-READSET"), (code, err, records)
+        verdict = next(item["detail"] for item in records if item["check"] == "verdict")
+        assert superseded_rel in verdict and "drift not evaluated" in verdict, verdict
+        assert D4_BRIEF not in verdict, verdict
+        results.append(
+            "mixed unresolvable+drifted baseline: E2E-READSET wins and says drift was not evaluated "
+            "(the drift leg is never reached for an unresolvable row)"
+        )
+
+        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
             v2_root, _ = v3_freezed_copy(fixture, control_dir, "retouched-v2")
             victim = v2_root / V2_PACKET_YML
             victim.write_text(victim.read_text(encoding="utf-8").replace("status: \"supported\"", "status: \"partial\"", 1), encoding="utf-8")
@@ -4490,7 +4541,7 @@
     parser.add_argument("--keep", metavar="DIR", help="keep the isolated packet directory at DIR")
     parser.add_argument("--json", action="store_true", help="print a receipt document on stdout")
     parser.add_argument("--freeze", metavar="DIR", help="(re)write the frozen baseline into DIR, printing diffs")
-    parser.add_argument("--quiet", action="store_true", help="print only the summary line")
+    parser.add_argument("--quiet", action="store_true", help="print only the summary line (a failed run still names its diagnostic)")
     args = parser.parse_args(argv)
 
     root = Path(args.root).resolve() if args.root else ROOT
@@ -4599,8 +4650,9 @@
         f"statuses={census_counts.group(2) + '/' + census_counts.group(3) + '/' + census_counts.group(4) if census_counts else '?'} "
         f"v2_subset={subset} alias_leg={alias} "
         f"packet_sha256={matches.group(1) if matches else '(not assembled)'}"
+        + (f" code={err}" if err else "")
     )
-    if err and not args.quiet:
+    if err:
         print(f"handoff-v3: {err}: {records[-1]['detail'] if records else ''}")
     if args.json:
         print(json.dumps({"profile": "v3", "root": str(root), "baseline": args.baseline or baseline_default,
```

The last hunk is the fix for R04's new finding
(`review/R04-o-review.md:161-162`): the code and message were printed only when
`not args.quiet` (`tools/exercise-handoff-e2e.py:4603-4604`), so claim O's own
`--quiet` command could not demonstrate "named diagnostic". A failed run now
always names its diagnostic; the green `exit=0` summary line is byte-identical
(the selftest's own assertion at `:4192` is unaffected). v1/v2 verdict prints
(`:4554` in v1, `:4515` in v2) are deliberately untouched — their baselines are preserved
byte-for-byte in behaviour.

## 3. Acceptance legs — command and observed output

All commands below ran in `.scratch/o05/repo` (isolated archive + patch), with
`export TMPDIR=$PWD/.scratch/o05/tmp PYTHONDONTWRITEBYTECODE=1`.

**L1 — r6 replay, `--quiet` (the claim's own command, `claims.json:48`): exit 1,
named diagnostic carrying the member path.**

```
handoff-v3: exit=1 fields=? glossary=?/20 findings=? links=? claims=? statuses=? v2_subset=unequal alias_leg=? packet_sha256=(not assembled) code=E2E-READSET
handoff-v3: E2E-READSET: 1 frozen read-set row(s) are not in the live read set: reports/round-20/handoff/claims-map.md (drift not evaluated for these rows)
```

O08 leg O1 (`op/O08-validation-legs.md:53-67`) checked mechanically: exit in
{1,2} → 1; `\bE2E-READSET\b` → present; single line matching
`^.*\bE2E-READSET\b.*reports/round-20/handoff/claims-map\.md.*$` → present;
`Traceback (most recent call last)` / `\bKeyError\b` → **absent**.

**L1b — same replay, non-quiet** (per-row record now names the member):

```
FAIL input-digest: reports/round-20/handoff/claims-map.md: frozen 4b1b9a35a18f… live: absent from the live read set (superseded baseline row)
```

**L1c — same replay, `--quiet --json`**: `"exit": 1`, `"code": "E2E-READSET"`,
failing checks `input-digest` (member path in the detail) and `verdict`
(`1 frozen read-set row(s) are not in the live read set: reports/round-20/handoff/claims-map.md`).

**L2 — selftest (`claims.json:47`): exit 0, 41 controls, both new controls
present, m12a/m12b preserved.**

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest
SELFTEST_EXIT=0
selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0, links=105/105, claims=27, statuses=16/7/4, v2_subset=equal, alias_leg=landed) plus 41 controls:
  - m12a tamper baseline: exit 2 E2E-BASELINE (integrity digest mismatch), never a pass
  - m12b tamper read-set (D4 projection): exit 1 E2E-DIGEST naming the changed file
  - superseded baseline row: exit 1 E2E-READSET naming the unresolvable member (never an unhandled KeyError, never swallowed by the E2E-DIGEST drift leg)
  - mixed unresolvable+drifted baseline: E2E-READSET wins and says drift was not evaluated (the drift leg is never reached for an unresolvable row)
```

42 `^  - ` result lines = 1 positive + 41 controls; pre-patch was 39 controls /
40 lines (O08 leg O2 floor is N ≥ 41, `:68-89`). The second new control is R04's
item 5(b) (`review/R04-o-review.md:150-152`), not a re-spelling of m12b; the
preserved `E2E-DIGEST` path stays covered by m12b and by negative control N2 below.

**L3 — r7 default chain regression (`claims.json:51`): exit 0, summary shape and
packet digest unchanged.**

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
```

Byte-identical to the pre-patch line, and the sha equals
`sha256sum reports/round-34/handoff/declared-in-r7/packet.md`
(O08 leg O3, `:90-98`).

**L4 — static legs (O08 O5, `:118-125`)**: patched renderer sha
`2e126e4f…` ≠ pre-patch `34c85f57…`; `E2E-READSET` occurs 7× in the patched
source and is named in the module docstring's exit-code table (the docstring is
the tool's contract, R04 §4.5).

**L5 — O08's legs O1/O2/O3 + the static leg re-implemented as a script and run
against the patched copy** (`.scratch/o05/o08-legs-check.py`, written by me; it
executes only the renderer, never a filed round runner):

```
O1: exit=1 PASS — handoff-v3: E2E-READSET: 1 frozen read-set row(s) are not in the live read set: reports/round-20/handoff/claims-map.md (drift not evaluated for these rows)
O2: exit=0 PASS — controls=41 result_lines=42
O3: exit=0 PASS — packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19 live=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
O5(static): exit=0 PASS — sha256=2e126e4f98ebe498b6173474a55bedaa953512dd8d6e56f7fabb6280cd6ea56e
{"legs_pass": true}   # exit 0
```

## 4. Negative controls (the paths the patch must NOT change)

| # | construction | observed |
|---|---|---|
| N1 | r7 baseline copied to `.scratch/o05/flipped-baseline.json` with `packet_sha256` flipped to `0`*64 and **not** re-signed | exit **2**, `E2E-BASELINE: baseline integrity digest mismatch — the baseline file was edited without re-freezing (re-freeze with --profile v3 --freeze DIR and read the diff it prints)` |
| N2 | live member `examples/culture-d4/brief.md` content-tampered in a copy | exit **1**, `E2E-DIGEST: 1 read-set file(s) changed since the baseline was frozen: examples/culture-d4/brief.md` — the new check does **not** shadow the drift leg |
| N3 | mixed unresolvable + drifted (in-selftest control) | `E2E-READSET` wins; verdict names the unresolvable member and says drift was not evaluated; the drifted member is absent from the verdict |
| N4 | v1 profile (`--quiet`, default) | exit 1 with `tools/d2-typed-labels.py` drift — **pre-existing**: the pristine archive produces the identical `FAIL` lines (`diff` of pre/post `FAIL` output empty). My patch does not touch v1 |
| N5 | v2 profile | exit 0, `handoff-v2: exit=0 claims=15 links=50/50 drift=named(tools/harness/packet_links.py round-16)` — unchanged |

An earlier attempt at N1 used a wrong relative baseline path and therefore
exercised the "baseline not found" branch, not the integrity branch; the result
above is the corrected run against an absolute path, and the distinction is
recorded here rather than dropped.

## 5. Preservation / freeze-byte evidence (`claims.json:67-73`, O08 leg O4)

- `git status --porcelain -- reports/round-30/handoff/declared-in-r6 reports/round-34/handoff/declared-in-r7` → **empty**.
- Per-file `sha256sum` vs `git show HEAD:<path>`: `declared-in-r6/expected.json`,
  `declared-in-r7/{expected.json,packet.md,claims-map.md}` → all **SAME**.
- Committed bytes of `tools/gates/frozen/**`, `reports/round-34/**`,
  `reports/round-30/handoff/declared-in-r6/**` compared between the lane tree and
  my archive: file lists and digests identical except `run.log` files, which are
  gitignored (`.gitignore:3` → `*.log`) and therefore absent from the archive —
  an archive-vs-worktree artifact, not byte drift.
- The renderer is in **neither** baseline's read set (`'tools/exercise-handoff-e2e.py'
  in inputs` → False for r6 and r7), so patching it cannot drift a frozen row.
- No `--freeze` was run against `reports/round-30/handoff/declared-in-r6` or
  `reports/round-34/handoff/declared-in-r7`. The only freeze calls were
  `v3_freezed_copy` inside selftest temp dirs. No filed round runner was executed;
  no in-tree write of any kind (`git status` shows only `?? reports/round-35/`).

## 6. Defects, decisions and findings filed (with owners)

**F1 — exit-code class is a decision the integrator must make once (owner:
integrator).** My patch raises `Failed` → **exit 1**. Evidence for 1:
`claims.json:48` declares it, `reports/round-34/handoff/repin.json:20` files
`"exit": 1` for this exact command, and R04 §5.1 (`review/R04-o-review.md:138-146`)
recommends it. The alternative — an `Unevaluatable` subclass → exit 2
(`scribe/S04-integration-draft.md:877`, `op/O08-validation-legs.md:159-176`'s
"convention-correct" reading) — would falsify the filed `exit: 1` and need an
explicit reading-change row. O08's leg accepts {1, 2}. **Verified value: 1.**

**F2 — `--quiet` diagnostic visibility (fixed in my patch; owner: integrator).**
Matches R04's finding (`review/R04-o-review.md:161-162`); the fix chosen is R04's
second option plus a `code=` field on the failure summary.

**F3 — stale docstring/packet-prose references to the superseded map (owner:
integrator/scribe; NOT fixed, outside claim O).** `tools/exercise-handoff-e2e.py:34`
and `:57` still describe the v3 read set as naming
`reports/round-20/handoff/claims-map.md`, while `CLAIMS_MAP` (`:184`) is the r34
path. Correction of `:34`/`:57` is free. **`:2700` is different**: it is emitted
packet prose — the string `reports/round-20/handoff/claims-map.md` occurs once in
the frozen `reports/round-34/handoff/declared-in-r7/packet.md`, so editing it
would move the frozen packet digest (`45f57132…`) and break the r7 baseline. It
must not be touched without a re-freeze, which is a non-goal (`claims.json:67-73`).

**F4 — v1 latent twin (known-latent, not fixed; owner: integrator).**
`tools/exercise-handoff-e2e.py:1440` carries the identical direct-index pattern in
the v1 leg. I verified the round-11 baseline has 21/21 resolvable rows, so the
crash cannot fire today (R04 §3's "v1 twin" bullet). Claim O is v3-scoped; this is
recorded, not absorbed.

**F5 — the round-34 filed record's mechanism string is now superseded (owner:
integrator).** `reports/round-34/handoff/repin.json:21` records the mechanism as
`KeyError: …`; once the patch lands, the round-35 record needs a supersession row
naming it (R04 §5.1, precedent `repin.json:45-47`). Not mine to write.

## 7. What I did not verify

- O03's and O01's bytes: both fragments are absent (see `## Owed`). My §2 patch is
  an independent candidate that satisfies the same declared acceptance; if the
  integrator applies O01's wording instead, legs L1–L3 must be re-measured on the
  landed bytes (the validator's O1–O3 legs are the check).
- The claim's third counting command (`claims.json:49`,
  `python3 reports/round-35/run-validation.py`) — that file does not exist yet.
- Nothing was executed in-tree; all renderer runs were in `.scratch/o05/**`
  copies. The `--freeze` mode was never exercised against any pinned directory.

## Owed

- `reports/round-35/op/O01-patch-draft.md` — missing dependency; the integrator
  should reconcile my §2 diff with O01's wording (or state which one lands).
- `reports/round-35/op/O03-isolated-verify.md` — missing dependency; O03's claimed
  observations could not be compared with mine. My §3 is an independent
  reproduction of the same legs.
- Post-application re-verification of the landed renderer bytes (owner:
  integrator/validator) — my evidence is measured on `.scratch/o05/repo`, whose
  patched sha is `2e126e4f…`; the live file is still `34c85f57…`.
- `reports/round-35/run-validation.py` — absent at write time; O08's legs are the
  draft it should implement.

## Citations

Files (all in this repo, at 4a7aede):
- `reports/round-35/targets.json:212` — seat O05 object (mission, out).
- `reports/round-35/claims.json:38,45,46-49,51,67-73` — claim O, after_required,
  counting commands (incl. the `--quiet` replay and `expect: exit 1`), thresholds,
  non-goals.
- `reports/round-34/handoff/repin.json:19-21,45-47,49-51` — filed `exit: 1`, the
  KeyError mechanism string, the supersession precedent, R34-N1 routed.
- `tools/exercise-handoff-e2e.py:34,57,89-93,184,1440,2700,3819,3822,4192,4430-4432,4515,4554,4603-4604`
  — read set description; exit-code table; `CLAIMS_MAP`; v1 latent twin; drift
  list; crash site; selftest green assertion; control insertion point; v1/v2
  verdict prints; quiet-gated verdict print; emitted packet prose.
- `reports/round-30/handoff/declared-in-r6/expected.json` — 58 `inputs`, incl.
  `reports/round-20/handoff/claims-map.md` (frozen `4b1b9a35a18f…`).
- `reports/round-34/handoff/declared-in-r7/expected.json`, `packet.md` — 58
  inputs, none unresolvable; packet names the round-20 map once.
- `reports/round-11/handoff/expected.json` — 21 inputs, none unresolvable.
- `.gitignore:3` — `*.log` (why `run.log` has no HEAD reference).
- `reports/round-35/op/O08-validation-legs.md:53,68,90,99,118,126,159,178` — legs
  O1–O6, the diagnostic shape, the exit-code policy, the selftest-count floors.
- `reports/round-35/review/R04-o-review.md:63-112,114-134,136-165` — the four
  executed fix shapes (S2 recommended at `:71`), leak analysis, integration
  obligations (exit-1 recommendation `:138-146`; quiet finding `:161-162`).
- `reports/round-35/scribe/S04-integration-draft.md:877` — the Unevaluatable/exit-2
  alternative.

Commands (run in `.scratch/o05/repo` unless noted; all with
`export TMPDIR=$PWD/.scratch/o05/tmp PYTHONDONTWRITEBYTECODE=1`):
- `git archive 4a7aede | tar -x -C .scratch/o05/repo`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest`
- `python3 -B tools/exercise-handoff-e2e.py --profile v2 --quiet` and the v1 default
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline .scratch/o05/flipped-baseline.json`
- `python3 -B .scratch/o05/o08-legs-check.py` (my re-implementation of O08 legs O1/O2/O3 + static)
- `sha256sum`, `diff -u`, `git status --porcelain`, `git show HEAD:<path> | sha256sum`,
  `find … -exec sha256sum {} +` tree comparisons (lane tree vs archive)
- module import of the renderer to compute the row-set census
  (`importlib.util.spec_from_file_location`) — read-only.
