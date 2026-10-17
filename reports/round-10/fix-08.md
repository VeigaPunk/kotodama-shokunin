# R10-O08 — findings fixer: tracker idx 6 (R9-D09 S2) and idx 14 (R8-D17 F-D17-2)

- shard: R10-O08 (findings fixer, operability claim O), round 10 (loop 1 of 3, build round 3 of 4), 2026-10-17
- assignment (verbatim): "FINDINGS R10-O08 (fixer): tracker indices 6 and 14. reports/round-10/fix-08.md."
- tracker read: `reports/round-10/findings-tracker.json` (compiled 21:27Z by R10-O01, 24 rows, baseline `e3a1ec9`). The tracker was **absent at my start**; I polled it (60 s cadence, background task `bash-e6v0qf0b`, 20-min cap) and it landed 21:28:50Z — indices taken from the tracker itself, not from the fallback rule. **idx 6 = R9-D09 S2** (medium, green-by-construction surfaces); **idx 14 = R8-D17 F-D17-2** (low, vocabulary divergence).
- writes: **this file + tracker rows idx 6 and idx 14 only**. No tool, artifact, gate, packet, corpus, SCORECARD or filed-report byte was edited by this shard. Nothing committed.
- scratch: `export TMPDIR=$PWD/.scratch`; my files under `.scratch/r10o08/` (shared `/tmp` remains inode-exhausted per round-9 receipts).
- baseline: worktree HEAD `e3a1ec9` + round-10 wave in flight; all measurements 21:29–21:34Z UTC (local = UTC-3).
- canon: NON-CANON engineering evidence; no admission, promotion or canon claim.

---

## 1. idx 6 — R9-D09 S2 — disposition: `wont-fix` (documented reason) + control demonstrated

**Finding (tracker text).** Green-by-construction surfaces: (a) the guard's own selftest builds `frozen-good`/`frozen-tampered` from live bytes, so `selftest_passed` green can coexist with a red committed freeze — no acceptance summary may cite "frozen 5/5"/`selftest_passed` as evidence for the frozen-replay leg; (b) D04's proposed projection manifest is self-captured — if committed, carry the README-hold correspondence + old-vs-new gate differential into the commit record.

**Disposition: `wont-fix`.** Both items are disclosed by-construction properties, not defects; no code change is warranted, and the condition they impose is verified honored on the current evidence chain. Reason in §1.1, condition-honoring sweep in §1.3, control in §1.2.

### 1.1 Why no fix (reason)

**(a) The selftest's blindness is by design.** `tools/check-evidence-coupling.py:1866-1900` — the selftest's own comment reads "frozen snapshot verification over live digests (copies stay in tmp)": `good_manifest` is built from the packet digest plus live component digests at run time, written to `expected-good.json` in tmp (`frozen-good` row, `:1884`), then one digest is flipped for `frozen-tampered-digest` (`:1897`). The committed freeze is never in the selftest's read-set, so `selftest_passed: true` says nothing about `examples/culture-d3/expected.json`. The frozen-replay leg's evidence in the acceptance chain is the `--frozen` run itself: `reports/round-9/validation.json` `claims.D.measurement.frozen_replay` = argv `[tools/check-evidence-coupling.py, examples/culture-d3/packet.json, --frozen, examples/culture-d3/expected.json]`, `exit: 0`, `drift_paths: []`, `stdout_sha256: c8d1a7b9…b3b2cc`; `SCORECARD.md:142` carries `python3 reports/round-9/run-validation.py` as the evidence command (that runner routes through the `--frozen` run). The round-9 red this finding measured (selftest green + committed freeze red) no longer exists: the freeze was re-pinned in `9dc18ec` after the per-input re-acknowledgement, and the current committed freeze replays clean (§1.2 run 3).

Nuance, not a violation: `reports/round-9/d3/capability-draft.md:64` lists "guard selftest green (… frozen 5/5)" and, separately in the same row, "input freeze re-pinned after round-8 input changes and replay clean"; `:108` describes "frozen 5/5" as the selftest's own frozen *cases*. The replay evidence is the run, not the selftest counters; D08 F3 and `reports/round-9/d3/scribe.md` state "selftest-green ≠ freeze-clear" explicitly. The finding's condition is therefore kept in the tracker record as a standing constraint (a careless reader could still conflate the two mentions in one row).

**(b) The proposal was never committed.** Sweep: `tools/gates/frozen/` holds only round-3/round-4-era frozen artifacts and per-gate `r9-pre/` baselines — no D3 replay manifest; `grep -rn '70affb9d'` over `reports/` and `tools/` (non-scratch) finds no committed hit; `reports/round-9/d3/scribe.md` records D04's manifest as scratch-only ("not committed"). The conditional ("if the orchestrator commits…") therefore does not fire. The corroboration it would require already exists in filed bytes should it ever be committed: `examples/culture-d3/README.md:88-93` (naming CROSS-HOLD ×2 + NAME-NEAR; costume R-01) and the old-vs-new gate differential in `reports/round-9/d3/findings.md` §3 item 5 / `reports/round-9/d3/replay.md`.

### 1.2 Control (re-runnable verbatim by verifiers O10–O13)

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
# run 1 — selftest green (the surface that cannot see the committed freeze)
python3 tools/check-evidence-coupling.py --selftest
#   observed: exit 0; selftest_passed true; positives 5/5, domain 16/16, malformed 4/4,
#             frozen_checks 5/5; 32/32 result rows passed
# run 2 — the pre-re-pin freeze (the exact round-9 red) stays red under a green selftest
git show 9dc18ec^:examples/culture-d3/expected.json > .scratch/r10o08/expected-pre-repin.json
sha256sum .scratch/r10o08/expected-pre-repin.json
#   observed: 74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080  (= S1's pre-refresh token)
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
        --frozen .scratch/r10o08/expected-pre-repin.json
#   observed: exit 2; counts {"D3-SNAPSHOT": 3, "total": 3}
# run 3 — the current committed freeze is green, through its own evidence channel
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
        --frozen examples/culture-d3/expected.json
#   observed: exit 0; counts {"total": 0}; findings []
```

Interpretation: runs 1+2 together prove the independence claim — selftest green (5/5 frozen cases) coexists with a red frozen surface — which is exactly the condition the finding imposes; run 3 shows the committed leg is green through the `--frozen` run itself, never through the selftest.

### 1.3 Condition-honoring sweep (acceptance evidence, read-only)

| surface | what it carries for the frozen leg |
|---|---|
| `reports/round-9/validation.json` `claims.D.measurement.frozen_replay` | the `--frozen` command; exit 0; `drift_paths: []`; stdout sha256 `c8d1a7b9…b3b2cc` |
| `SCORECARD.md:142` (depth row) | evidence command `python3 reports/round-9/run-validation.py` |
| `reports/round-9/d3/capability-draft.md:64,108` | "frozen 5/5" cited inside the selftest breakdown; replay cited separately (see §1.1 nuance) |
| `tools/gates/frozen/` sweep | no committed D3 projection manifest → (b) has no live surface |

---

## 2. idx 14 — R8-D17 F-D17-2 — disposition: `fixed-with-control`

**Finding (tracker text).** The tool's status vocabulary and hold ids diverge from the spec: at `623b5b1f` the tool emitted `declared`/`unresolved` and hold id `TL-01`, while `design-spec.md` §1.2 L1 says `supplied | to-verify | absent` and §1.5 expects `D2L-FORM-UNRESOLVED` for the GAR-01..10 case; a consumer written against the spec's `D2L-*` codes finds none.

**Disposition: `fixed-with-control`.** The divergence was closed by the round-8 rewrite — `reports/round-8/depth/findings.md` resolved-table row S4 records `D2L-*` ×69 at revision `e9209f28`, and the emitted report carries `D2L-FORM-UNRESOLVED`. The finding's own three checks are re-run at the delivered revision below.

### 2.1 Control (the finding's checks, re-run at the delivered revision)

```sh
python3 tools/d2-typed-labels.py --selftest
#   observed: exit 0 — "selftest: 39/39 checks passed — the three shard control matrices, …"
python3 tools/d2-typed-labels.py --emit .scratch/r10o08/emit.yml
#   observed: exit 1 (holds present — the resolved exit map); the projection is written
python3 - <<'PY'   # vocabulary + hold-id counts, fresh emit vs committed artifact
import collections, re
for name, path in [("fresh", ".scratch/r10o08/emit.yml"),
                   ("committed", "examples/culture-d2/typed-labels.d2.yml")]:
    s = open(path).read()
    print(name, dict(collections.Counter(re.findall(r'"status": "([a-z-]+)"', s))),
          "| declared/unresolved:", s.count('"declared"') + s.count('"unresolved"'),
          "| TL-01:", s.count("TL-01"),
          "| D2L-FORM-UNRESOLVED:", s.count("D2L-FORM-UNRESOLVED"),
          "| D2L- total:", len(re.findall(r"D2L-[A-Z-]+", s)))
PY
```

Observed (21:30Z; both surfaces 84,614 bytes):

| surface | sha256 | status vocab | `declared`/`unresolved` | `TL-01` | `D2L-FORM-UNRESOLVED` | `D2L-` total |
|---|---|---|---|---|---|---|
| fresh emit | `a3aa452c…64a43` | supplied 48, to-verify 18, confirmed 4 | 0 / 0 | 0 | 20 | 37 |
| committed artifact | `e70ba147…380b2f` | supplied 48, to-verify 18, confirmed 4 | 0 / 0 | 0 | 20 | 37 |

- The finding's own case is emitted with the spec's code: findings block — `{code: D2L-FORM-UNRESOLVED, id: D2L-FORM-UNRESOLVED, severity: hold, where: GAR-01, detail: "label_id LEX-GAR-01 has no supplied native/borrowed form"}`; all ten `LEX-GAR-01..10` hold ids present. `design-spec.md:236` expects exactly `D2L-FORM-UNRESOLVED` HOLD ×10 for GAR-01..10 → met.
- Vocabulary: spec §1.2 L1 (`design-spec.md:116`): `status: supplied # supplied | to-verify | absent` — the emit uses `supplied`/`to-verify`; the `confirmed` ×4 are the `era_reconciliation.alias_rows` / `two_to_one` mapping rows, for which spec §1.2 E4 (`design-spec.md:264-268`) declares `(confirmed | to-verify)` — era-row vocabulary, not label statuses, so not a divergence.
- The fix is in the **admitted** bytes, not only in the worktree: tool sha256 `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` equals the round-8 admitted value and artifact `e70ba147…` equals the round-8 test-determinism seal (`reports/round-9/d3/interop.md` §2 table, both cross-checked).

### 2.2 Adjacent known red (not this finding; recorded so a verifier does not trip)

`python3 tools/d2-typed-labels.py --check` exits 1 — a single stale provenance line: the artifact records `packet_sha256: 8da90b07…` while the live packet hashes `e0f21509…` (my `diff` of the fresh emit vs the committed artifact: exactly that one line). The identical red exists at round-8's admission commit `e1694ba`; it is filed in `reports/round-9/d3/interop.md` §4 (lines 112-135) and `reports/round-9/d3/scribe.md:90` ("stale one-line packet pin dated to `e1694ba`"). It is **not** a vocabulary issue — §2.1's counts are identical across the artifact and the fresh emit. Repair is the artifact owner's call; this shard made no change.

---

## 3. Tracker updates (rows idx 6 and idx 14 only)

Updated in place with an atomic read-modify-write (load → set my two rows → `os.replace`) behind a lost-update guard (replace only if the file still matched the bytes loaded). The other 22 rows are semantically untouched (verified row-wise after the write); two caveats: my re-serialization changed the file's indentation style (O01 wrote one-space indent, my dump two-space — cosmetic, JSON-identical), and other fixers write the same JSON concurrently (eight rows were dispositioned by 21:36Z; my rows were verified present after those writes).

| row | disposition set | fields added |
|---|---|---|
| idx 6 (R9-D09 S2) | `wont-fix` | `reason` (≥12 chars; §1.1 compressed), `control` (§1.2 battery + observed exits), `fixer_report`, `disposition_at_utc` |
| idx 14 (R8-D17 F-D17-2) | `fixed-with-control` | `control` + `control_evidence` (§2.1 commands and observed counts), `fixer_report`, `disposition_at_utc` |

Contract check with the runner's own O-measure, imported read-only at 21:36Z (`measure_o()` — no writes; the shared `reports/round-10/validation.json` is X03's and was not re-run): my rows 6 and 14 appear in none of `pending_rows`, `unrecognized_labels`, `fixed_without_control`, `documented_without_reason`. The runner's remaining O failures at that stamp — 16 still-pending rows (other fixers in flight) plus the absent verifier verdict files and scribe file (O10–O14) — are not this shard's surfaces.

Concurrency note: eight fixers write the same JSON. If a later writer clobbers rows 6/14 back to `pending`, the scribe (R10-O14) or X04 should reconcile from this file — the dispositions above are the fixer's record.

---

## 4. Limits / to-verify

- idx 6's disposition rests on filed receipts (validation.json, SCORECARD, scribe) plus the three-run control; I did not re-adjudicate the round-9 re-pin's legitimacy beyond matching S1's pre-refresh token (`74496aa8…`) in run 2.
- idx 14's "fixed" refers to the delivered revision (`0da0015f` tool / `e70ba147` artifact = round-8 admitted values); the intermediate revision history (`623b5b1f → e9209f28`) is cited from filed round-8 receipts, not re-derived.
- The `confirmed` ×4 reading as era-row vocabulary follows spec §1.2 E4; a verifier should confirm that reading — if `absent` were instead required somewhere, that is a new finding, not this one.
- Out of scope here: D04's manifest design, the re-pin record's adequacy (verifiers O10–O13), any canon question.

Receipts (all from the lane root, 2026-10-17, 21:29–21:34Z):

```sh
python3 tools/check-evidence-coupling.py --selftest                     # exit 0; frozen_checks 5/5
git show 9dc18ec^:examples/culture-d3/expected.json > .scratch/r10o08/expected-pre-repin.json
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen .scratch/r10o08/expected-pre-repin.json   # exit 2; 3×D3-SNAPSHOT
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json         # exit 0; []
python3 tools/d2-typed-labels.py --selftest                              # exit 0; 39/39
python3 tools/d2-typed-labels.py --emit .scratch/r10o08/emit.yml        # exit 1 (holds)
python3 tools/d2-typed-labels.py --check                                # exit 1 — adjacent known red (§2.2)
sha256sum tools/d2-typed-labels.py examples/culture-d2/typed-labels.d2.yml .scratch/r10o08/emit.yml
```

FILES: reports/round-10/fix-08.md; reports/round-10/findings-tracker.json (rows idx 6, idx 14) | SUMMARY: R10-O08 fixer dispositions tracker idx 6 (R9-D09 S2, green-by-construction surfaces) as wont-fix with reason + a three-run control (selftest green 5/5 coexists with the pre-re-pin freeze red 3×D3-SNAPSHOT; current freeze green through the --frozen run) and idx 14 (R8-D17 F-D17-2, vocabulary) as fixed-with-control (emit and committed artifact both carry supplied 48/to-verify 18, zero declared/unresolved, zero TL-01, D2L-FORM-UNRESOLVED ×20 with holds on LEX-GAR-01..10, selftest 39/39); tracker rows updated atomically, no other files touched.
