- Seat: O02 | executor | claim O | date 2026-10-19 | baseline 4a7aede

# O02 — the two new renderer selftest controls (superseded-row named refusal; preserved E2E-DIGEST path)

Deliverable of claim O's "renderer selftest controls" leg: the two new controls for
`tools/exercise-handoff-e2e.py` with their fixture designs, the interface contract they bind,
and the expected outputs, each measured by prototype against a reference implementation of the
guard in an isolated `git archive` copy (`.scratch/o02-proto{,-patched}`, scratch only, not filed).
The catch-site patch itself is O01's deliverable; the guard below is the prototype that produced
these expected outputs and is offered for reconciliation, not as the binding patch form.

## 1. Defect anchor (before, measured in-tree)

```
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
    --baseline reports/round-30/handoff/declared-in-r6/expected.json
Traceback (most recent call last):
  File ".../tools/exercise-handoff-e2e.py", line 4613, in <module>
    sys.exit(main())
  File ".../tools/exercise-handoff-e2e.py", line 4578, in main
    code, err, records = v3_exercise(root=root, baseline_rel=args.baseline or baseline_default)
  File ".../tools/exercise-handoff-e2e.py", line 3822, in v3_exercise
    record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
KeyError: 'reports/round-20/handoff/claims-map.md'
EXIT=1
```

Mechanism: `tools/exercise-handoff-e2e.py:3819` builds `drifted` with `assembly.digests.get(rel)`
(tolerating an unknown member), then `:3822` indexes `assembly.digests[rel]` — the plain index is
the KeyError. `drifted` is non-empty exactly because the r6 row names a member the live read set
no longer carries (`CLAIMS_MAP` moved to `reports/round-34/handoff/declared-in-r7/claims-map.md`
at `:184`; the v3 default pair is `:1933-1934`). The refusal is correct; the mechanism is not.

Read-set delta of the r6 row (measured at 4a7aede, sha256 `ea1e2927…`):

| class | count | members |
|---|---|---|
| `inputs` keys total | 58 | — |
| unresolvable (not in live `V3_READ_SET`, `:1935`, 58 members) | 1 | `reports/round-20/handoff/claims-map.md` |
| resolvable but drifted | 0 | — |

The zero-drift reading matters twice: the superseded-row class is isolable from the digest leg
(no interference in the fixture), and the r6 replay cannot be "fixed" by a digest-leg rewrite.

## 2. Interface contract the controls bind (for O01's patch)

Any patch form is acceptable that satisfies all five:

1. a baseline whose `inputs` name ≥1 path outside the live read set yields
   `v3_exercise(...) == (EXIT_FAIL, "E2E-READSET", records)` — exit **1** (mismatch class, not
   could-not-evaluate; the claim's counting command records `expect: exit 1`);
2. at least one failed record row's `detail` contains the unresolvable path **verbatim**;
3. the message names the unresolvable member(s) (existing convention: first three, `:3823`);
4. `E2E-READSET` is added to the docstring exit-code census (`:90-92`);
5. the named diagnostic is visible on the **`--quiet`** path, because the claim's counting command
   is `--quiet` and `main` currently prints the `handoff-v3: {code}: {detail}` line only when
   `not args.quiet` (`:4603`). Minimal change: hoist that one print out of the guard:

```diff
--- a/tools/exercise-handoff-e2e.py
+++ b/tools/exercise-handoff-e2e.py
@@ -4600,7 +4600,7 @@
-    if err and not args.quiet:
+    if err:
         print(f"handoff-v3: {err}: {records[-1]['detail'] if records else ''}")
```

Trade, stated not hidden: this changes the stdout of a *failing* `--quiet` v3 run from summary-only
to summary-plus-diagnostic. No consumer of a failing quiet stdout was found — the filed validators
parse `packet_sha256=([0-9a-f]{64})` from the **successful** quiet run
(`reports/round-34/run-validation.py:180-183`, `reports/round-30/run-validation.py:73`,
`reports/round-31/run-validation.py:89`); the non-quiet failure shape is already the filed
precedent (`reports/round-22/bleed/evidence/attempt-01-verification.json:241`). The summary line
itself is unchanged in every case.

## 3. Reference guard (prototype, O01's patch is binding)

Inserted at the catch site, after `v3_load_baseline` and before `snapshot_before`/`V3Assembly`
(so the refusal is cheap and fires before any assembly work):

```python
        baseline_path, baseline = v3_load_baseline(root, baseline_rel)

        # R34-N1 hardening: a superseded row can name a read-set member the live
        # read set no longer carries (the CLAIMS_MAP move is the precedent).
        # Refuse by name; never die on an unhandled KeyError at the digest report.
        unresolved = sorted(rel for rel in baseline["inputs"] if rel not in set(V3_READ_SET))
        if unresolved:
            for rel in unresolved:
                record("input-readset", False, f"{rel}: named by the baseline, absent from the live read set")
            raise Failed(
                "E2E-READSET",
                f"{len(unresolved)} read-set member(s) named by the baseline are not in the live read set: "
                f"{', '.join(unresolved[:3])}"
                + (f" (+{len(unresolved) - 3} more)" if len(unresolved) > 3 else "")
                + " — the row is superseded; replay a current row or freeze a new one",
            )

        snapshot_before = {rel: measure(root, rel)[0] for rel in V3_READ_SET}
```

Ordering is load-bearing: the unresolved check must precede the `drifted` computation, or the
r6 row reports `E2E-DIGEST` on a resolvable member and the superseded member stays unnamed.

## 4. Control m13 — superseded-row named refusal (fixture + expected output)

Insert after the m12b leg (`tools/exercise-handoff-e2e.py:4430`), inside `v3_selftest` (`:4154`);
`json`, `shutil`, `tempfile`, `ROOT`, `CLAIMS_MAP`, `MissingArtifact`, `v3_freezed_copy`,
`v3_baseline_digest` are already in scope there.

Fixtures (all built under `tempfile.TemporaryDirectory`, filed bytes never written):

- **m13a synthetic superseded row** — `v3_freezed_copy` freezes the throwaway fixture root, then
  the *control* edits only that throwaway copy's `expected.json`: the live member key
  (`CLAIMS_MAP`) is moved to the filed r6 stale path (`reports/round-20/handoff/claims-map.md`)
  and `baseline_digest` is re-signed, so the row is integrity-valid and its only defect is the
  moved member. Expected: `(1, "E2E-READSET")`, stale path named in a failed record, and **no**
  failed `input-digest` row (the read-set guard fires alone).
- **m13b filed r6 row replay** — a fresh frozen fixture root receives a read-only copy of the
  actual filed row `reports/round-30/handoff/declared-in-r6/expected.json` (sha256 `ea1e2927…`),
  which is then replayed as the baseline. This is the claim's counting command made executable
  inside the suite. Expected: `(1, "E2E-READSET")` naming
  `reports/round-20/handoff/claims-map.md`; the call returns records — it must not raise.

```python
        r6_row_rel = "reports/round-30/handoff/declared-in-r6/expected.json"
        r6_stale_member = "reports/round-20/handoff/claims-map.md"
        assert r6_stale_member not in V3_READ_SET and CLAIMS_MAP in V3_READ_SET, (r6_stale_member, CLAIMS_MAP)

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            superseded_root, _ = v3_freezed_copy(fixture, control_dir, "superseded-row")
            victim = superseded_root / baseline_rel
            edited = json.loads(victim.read_text(encoding="utf-8"))
            assert sorted(edited["inputs"]) == sorted(V3_READ_SET), "a fresh freeze does not pin the live read set"
            edited["inputs"][r6_stale_member] = edited["inputs"].pop(CLAIMS_MAP)
            edited["baseline_digest"] = v3_baseline_digest(edited)
            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
            code, err, records = v3_exercise(root=superseded_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_FAIL, "E2E-READSET"), (code, err, records)
        assert any(not row["ok"] and r6_stale_member in row["detail"] for row in records), records
        assert not any(row["check"] == "input-digest" and not row["ok"] for row in records), records
        results.append(
            f"m13a superseded row (a member moved out of the live read set): exit {code} {err} "
            f"naming {r6_stale_member}"
        )

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            r6_root, _ = v3_freezed_copy(fixture, control_dir, "r6-row-replay")
            source = ROOT / r6_row_rel
            if not source.is_file():
                raise MissingArtifact(f"selftest fixture source missing: {r6_row_rel}")
            target = r6_root / r6_row_rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            code, err, records = v3_exercise(root=r6_root, baseline_rel=r6_row_rel)
        assert (code, err) == (EXIT_FAIL, "E2E-READSET"), (code, err, records)
        assert any(not row["ok"] and r6_stale_member in row["detail"] for row in records), records
        results.append(
            f"m13b filed r6 row replay against the live tree: exit {code} {err} naming {r6_stale_member} "
            "(the R34-N1 KeyError path is a named refusal, never a traceback)"
        )
```

Observed control lines (patched isolated copy, `--profile v3 --selftest`, exit 0):

```
  - m13a superseded row (a member moved out of the live read set): exit 1 E2E-READSET naming reports/round-20/handoff/claims-map.md
  - m13b filed r6 row replay against the live tree: exit 1 E2E-READSET naming reports/round-20/handoff/claims-map.md (the R34-N1 KeyError path is a named refusal, never a traceback)
```

Discrimination (unpatched copy, same fixtures, driver `.scratch/o02-proto/o02-discriminate.py`):

```
m13a UNPATCHED: unhandled KeyError 'reports/round-20/handoff/claims-map.md'
m13b UNPATCHED: unhandled KeyError 'reports/round-20/handoff/claims-map.md'
```

## 5. Control m14 — preserved E2E-DIGEST path (fixture + expected output)

Two legs, both on the moved member itself (`CLAIMS_MAP`) so the boundary between the two codes is
pinned on one file. This is a **preservation** control: it passes before and after the patch, and
it fails only if the new guard swallows or shadows resolvable drift or the baseline-integrity leg.

- **m14a flipped-sha expectation** — frozen fixture root, then `inputs[CLAIMS_MAP] = "0" * 64`
  written **without** re-signing `baseline_digest`. The member is resolvable, so the read-set
  guard must not fire. Expected: `(2, "E2E-BASELINE")` (integrity digest mismatch), never a pass.
- **m14b content-tampered live member** — frozen fixture root, then a newline appended to the live
  `CLAIMS_MAP` bytes. Expected: `(1, "E2E-DIGEST")` naming the changed file, and the code must
  **not** be `E2E-READSET`.

```python
        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            flipped_root, _ = v3_freezed_copy(fixture, control_dir, "flipped-sha")
            victim = flipped_root / baseline_rel
            edited = json.loads(victim.read_text(encoding="utf-8"))
            edited["inputs"][CLAIMS_MAP] = "0" * 64
            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
            code, err, records = v3_exercise(root=flipped_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_UNEVALUATED, "E2E-BASELINE"), (code, err, records)
        results.append(
            "m14a flipped read-set sha in the baseline without re-signing: exit 2 E2E-BASELINE "
            "(integrity digest mismatch), never a pass"
        )

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            tampered_root, _ = v3_freezed_copy(fixture, control_dir, "tampered-member")
            victim = tampered_root / CLAIMS_MAP
            victim.write_text(victim.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            code, err, records = v3_exercise(root=tampered_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_FAIL, "E2E-DIGEST"), (code, err, records)
        assert err != "E2E-READSET", err
        assert any(not row["ok"] and CLAIMS_MAP in row["detail"] for row in records), records
        results.append(
            f"m14b content-tampered live member {CLAIMS_MAP}: exit {code} {err} naming the changed file "
            "(resolvable drift keeps its own leg; the read-set guard does not swallow it)"
        )
```

Observed control lines (patched isolated copy) and the same codes on the unpatched copy:

```
  - m14a flipped read-set sha in the baseline without re-signing: exit 2 E2E-BASELINE (integrity digest mismatch), never a pass
  - m14b content-tampered live member reports/round-34/handoff/declared-in-r7/claims-map.md: exit 1 E2E-DIGEST naming the changed file (resolvable drift keeps its own leg; the read-set guard does not swallow it)
m14a UNPATCHED: returned 2 E2E-BASELINE
m14b UNPATCHED: returned 1 E2E-DIGEST | naming: ['reports/round-34/handoff/declared-in-r7/claims-map.md: frozen d181de28ccaf… live 04e7e76b8de1…']
```

m14b's observed digest pair is live-file evidence: `d181de28ccaf…` is the filed r7 claims-map
digest (`reports/round-34/handoff/repin.json`, `d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c`).

## 6. Expected outputs for the claim's counting commands (prototype-observed)

Isolated patched copy at 4a7aede + the reference guard:

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
    --baseline reports/round-30/handoff/declared-in-r6/expected.json
handoff-v3: exit=1 fields=? glossary=?/20 findings=? links=? claims=? statuses=? v2_subset=unequal alias_leg=? packet_sha256=(not assembled)
handoff-v3: E2E-READSET: 1 read-set member(s) named by the baseline are not in the live read set: reports/round-20/handoff/claims-map.md — the row is superseded; replay a current row or freeze a new one
EXIT=1

$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline reports/round-30/handoff/declared-in-r6/expected.json
FAIL input-readset: reports/round-20/handoff/claims-map.md: named by the baseline, absent from the live read set
FAIL verdict: 1 read-set member(s) named by the baseline are not in the live read set: reports/round-20/handoff/claims-map.md — the row is superseded; replay a current row or freeze a new one
handoff-v3: exit=1 fields=? glossary=?/20 findings=? links=? claims=? statuses=? v2_subset=unequal alias_leg=? packet_sha256=(not assembled)
handoff-v3: E2E-READSET: 1 read-set member(s) named by the baseline are not in the live read set: reports/round-20/handoff/claims-map.md — the row is superseded; replay a current row or freeze a new one
EXIT=1

$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest
selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0, links=105/105, claims=27, statuses=16/7/4, v2_subset=equal, alias_leg=landed) plus 43 controls:
EXIT=0        # 39 controls before the patch; +4 leg lines (m13a, m13b, m14a, m14b)

$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
EXIT=0        # byte-identical to the filed r7 packet digest (reports/round-34/handoff/repin.json); no freeze ran
```

Regression checks in the same isolated copies: `--profile v2 --quiet` exit 0 with the filed
round-16 drift note, identical before and after; the v1 default chain is red **pre-existing** at
HEAD and byte-identical before and after the patch (`E2E-DIGEST: 1 read-set file(s) changed since
the baseline was frozen: tools/d2-typed-labels.py`) — that is v1's filed round-11 baseline against
later live bytes, not a patch effect. The v1 profile carries the same latent index at
`tools/exercise-handoff-e2e.py:1440` (`assembly.digests[rel]`), but its filed baseline names no
member outside the live v1 read set, so the KeyError class is not reachable there today; out of
this claim's scope, named here for the regression census.

## 7. Acceptance legs for the validator (for O08 / S04)

- r6 replay: exit **1**; stdout matches `handoff-v3: E2E-READSET: .*reports/round-20/handoff/claims-map\.md`; no `Traceback` on stderr.
- r7 default chain: exit 0 and `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`.
- selftest: exit 0 and the four new control lines present (grep `m13a superseded row`, `m13b filed r6 row replay`, `m14a flipped read-set sha`, `m14b content-tampered live member`); control count 39 → 43.
- preservation: `reports/round-30/handoff/declared-in-r6/**` sha256 unchanged (`expected.json` = `ea1e2927…`), and no `--freeze` of `reports/round-34/handoff/declared-in-r7` runs.

## Owed

- `reports/round-35/op/O01-patch-draft.md` — reconcile the catch-site form. The controls bind only
  the five-point observable contract in §2; if O01's patch names the record row differently, the
  assertions still pass (they key on the failed-record `detail` text and the code, not the row
  name). If O01's patch places the guard after `V3Assembly`, m13a/m13b still hold (they assert
  codes and naming only) — but the r6 replay then pays a full assembly before refusing.
- `reports/round-35/scout/K03-keyerror-path.md` — cross-check the traceback reproduction
  (same site, `:3822`) if K03 filed a different reading.
- In-tree execution of the §6 counting commands is owed to the integrator: seats may not apply the
  patch to `tools/exercise-handoff-e2e.py`, and the pre-patch in-tree run is the traceback in §1.

## Citations

- `tools/exercise-handoff-e2e.py:184` (`CLAIMS_MAP`), `:1933-1934` (v3 default pair), `:1935` (`V3_READ_SET`), `:3807` (`v3_exercise`), `:3819` (`drifted`, `.get`), `:3822` (KeyError site), `:3823` (first-three naming convention), `:4154` (`v3_selftest`), `:4430` (m12b anchor), `:4461-4464` (selftest header count), `:4603` (quiet-gated error print), `:90-92` (exit-code census), `:1440` (v1 latent index)
- `reports/round-34/handoff/repin.json` (R34-N1 finding; R34-D-stale-row control; r7 packet digest `45f57132…`; claims-map digest `d181de28…`)
- `reports/round-30/handoff/declared-in-r6/expected.json` sha256 `ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0` (58 `inputs`, 1 unresolvable, 0 drifted)
- `reports/round-34/handoff/declared-in-r7/claims-map.md` sha256 `d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c`
- `reports/round-34/run-validation.py:180-183`, `reports/round-30/run-validation.py:73`, `reports/round-31/run-validation.py:89` (quiet-stdout consumers), `reports/round-22/bleed/evidence/attempt-01-verification.json:241` (filed failing-run stdout shape)
- Commands (all with `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`): in-tree r6 replay (§1 traceback); `git archive HEAD | tar -x` into `.scratch/o02-proto{,-patched}`; `.scratch/o02-proto-patched/apply-o02-proto.py` (4 edits); patched/unpatched `--profile v3 --selftest`, `--profile v3 --quiet [--baseline r6]`, `--profile v2 --quiet`, default `v1`; `.scratch/o02-proto/o02-discriminate.py` (unpatched fixture runs). Scratch copies are not filed; every filed byte read above is unchanged (no writes under `reports/round-30/**`, `reports/round-34/**`, `tools/**`).
