# R18-D14 — interop 1/3: the D2 typed-gate path vs round-11's recorded verdict

- round 18 (operator: loop 2 of 3, build round 2 of 4; `reports/round-18/claims.json`,
  claim **D**, shard **D14**). Lane: `kotodama-shokunin`.
- assignment (verbatim): "D R18-D14..D16 (interop x3): D2 path (typed gate on D2
  packet) verdict identical to round-11's recorded verdict; d2/d3 assemblers
  --check green; battery green; reports/round-18/d4/interop-{1..3}.md."
- date: 2026-10-18. Evidence window 10:19:20Z–10:26:00Z UTC. Reference revision
  HEAD `c66ac3c951b346a2a56f9386e3324b4f5fe33902`
  ("round-18: declare claims O/D/C", 2026-10-18 07:17:35 -0300). Baseline
  `3dd3754207032cb81f5fb3e202fe85cf79211339` (round-17, D rejected).
- canon: NON-CANON engineering evidence. Nothing here is a canon record, a lore
  handoff, a clearance, or a rights/attribution ruling.
- writes: **this file only** plus gitignored scratch under
  `.scratch/r18interop*` (`export TMPDIR=$PWD/.scratch/…` preceded every
  scratch-writing command; the one exception is the frozen replay in
  `interop-3.md`, which the tool itself refuses to run from an in-repo TMPDIR —
  recorded there). No tool, packet, projection, baseline, receipt or
  earlier-round byte is edited by this seat. No commit, no push.

## 0. Verdict

**MATCH — the D2 typed-gate path reproduces round-11's recorded verdict exactly,
byte-for-byte on both recorded byte artifacts and field-for-field on the
verdict.** The gate file observed is the round-11-frozen one, sha256
`d102fd1d…68e27d` (`tools/gates/frozen/round-11/MANIFEST.tsv` row 1
`gate_sha256`, re-hashed live at 10:19Z and identically at every 60 s poll
through 10:29Z; the round-18 generalization had not landed in this window —
boundary in §5).

| leg | round-11 record | round-11 source | round-18 observation | reading |
|---|---|---|---|---|
| default path `python3 tools/gates/typed-pipeline-gate.py` | exit 0, 15 findings + 1 note, 16/16 legs | `reports/round-17/validation.json` claims.D.measurement.greens.typed_pipeline_gate (exit 0, 2026-10-18); `reports/round-11/validation.json` claims.D | exit **0**, 15 `FINDING` + 1 `NOTE`, **16/16 legs**, stdout sha256 `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b` | match |
| `python3 tools/gates/typed-pipeline-gate.py --json` | exit 0, 16 findings, stdout sha256 `19765ddf2c36a7db5d71bd262079d6164b24f6222d9df83d0cefdeaeb8f47e62` | `reports/round-11/validation.json` claims.D.measurement.e2e.rerun (stdout_sha256); `reports/round-12/recount/ledger.json` (recorded exit 0 / expected_findings 16 / same sha; observed ×2, verdict `match`); `reports/round-14/rerun.json`, `reports/round-15/rerun.json` (regression row 13) | exit **0**, stdout sha256 **`19765ddf…8f47e62` — byte-identical to the record** | **byte match** |
| frozen row 1 `python3 tools/gates/typed-pipeline-gate.py tools/gates/frozen/round-11/typed-pipeline/packet.d2.typed.yml` | exit 0, finding_count 15, output_sha256 `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606` | `tools/gates/frozen/round-11/MANIFEST.tsv` row 1 + `typed-pipeline/run-receipt.json` + `run.log` | exit **0**, stdout sha256 `9a69985a…ada4606`, `cmp` vs `run.log` → **byte-identical** | **byte match** |

Commands (all 2026-10-18, run from the repo root; outputs kept in
`.scratch/r18interop/`):

```sh
python3 tools/gates/typed-pipeline-gate.py                                 # exit 0
python3 tools/gates/typed-pipeline-gate.py --json                          # exit 0
python3 tools/gates/typed-pipeline-gate.py \
    tools/gates/frozen/round-11/typed-pipeline/packet.d2.typed.yml         # exit 0
```

## 1. The verdict, independently re-derived

The gate's own L3 legs self-check the hold set, but this seat also re-parsed the
plain stdout against the committed expected set — an independent reading, not a
re-run of the gate's assertion:

- emitted `FINDING` lines: **15**; emitted `NOTE` lines: **1**; `fail` lines: 0.
- set equality on `(id, severity, where, detail)` vs
  `examples/culture-d2/expected-holds.json` (`counts {hold 15, note 1, fail 0}`):
  **holds exact (0 only-emitted, 0 only-expected), notes exact**.
- the `--json` document's finding set equals the stdout finding set (16 = 15 + 1).
- `--json` fields: `ok true`, `exit_code 0`, `counts {"fail":0,"hold":15,"note":1}`,
  `sound_channel {"routed":10,"removed":10,"added":0,"translated_on_sound_channel":0}`,
  `pins {packet e0f21509…, projection a3aa452c…, adapter c7e5a749…}`,
  16 checks all `ok`, first `L1-assembler_identity`.

Determinism (two consecutive runs each): plain stdout `15cdfbda…` twice,
`cmp` identical; `--json` stdout `19765ddf…` twice, `cmp` identical.

## 2. Inputs at observation time

| path | sha256 | note |
|---|---|---|
| `tools/gates/typed-pipeline-gate.py` | `d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d` | equals round-11 `run-receipt.json` `gate_sha256`; unchanged all window |
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` | equals round-11 frozen pin |
| `examples/culture-d2/packet.d2.typed.yml` | `1b5010b7f449ec78755e9a8b0efea62c705af7ec5c592ceda6cf2c072dfac8a3` | equals round-11 frozen manifest input |
| `examples/culture-d2/typed-labels.d2.yml` | `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` | equals `--json` `pins.projection_sha256` |
| `examples/culture-d2/expected-holds.json` | `a5dc26d5b495a90e05ce42d4d8b6d08f047359c377e458f9190b1d310d6dde3a` | the L3 baseline |

`tools/assemble-d2-typed.py` `c7e5a749…`, `tools/d2-typed-labels.py`
`0da0015f…`, `tools/assemble-d2.py` `8ea6bdde…` — equal to the round-11
`run-receipt.json` tool pins. Repo hygiene after all runs: `git status
--short` shows no tracked modification; the three D2 artifact digests above
re-hashed identically after the runs.

## 3. Negative controls (identity is discriminating, not vacuous)

| control (scratch copies only) | observed |
|---|---|
| A — one byte of the **frozen typed packet** patched (`GAR-05`→`GAR-11`) | exit **1**, 12/13 legs (`L3` fires; the hold set no longer matches) |
| B — one byte of a **D2 packet copy** patched (`GAR-01`→`GAR-91`) | exit **2**, `FAIL L1-assembler_identity: packet bytes are not assemble-d2.py's deterministic assembly (40b8c1ea00c1 vs e0f21509e14a)` — the identity leg is live on the D2 path |
| C — the D4 packet under the current D2-bound gate | exit **2**, `FAIL L1-assembler_identity … (e7ecd2045ef0 vs e0f21509e14a)` — the round-17 rejection, kept here as the pre-generalization baseline for the O/D4 seats |

## 4. Interop checks handed to the sibling arms

- `interop-2.md`: `assemble-d2.py --check` sha `2fa0c8c1…` and
  `assemble-culture-d3.py --check` sha `e20620fa…` both exit 0 and equal
  round-11's recorded shas; the 13-command standing regression set is 13/13
  green.
- `interop-3.md`: battery exit 0 (7/7 selftests, 8/8 baselines pinned);
  round-11 frozen replay 11/11; window boundary.

## 5. Boundary — what this does NOT prove

- The generalization named by claim O (packet-declared/flag assembler pin) had
  **not landed** in this window: the gate stayed at the round-11-frozen sha
  through 10:29Z (60 s poll log, `.scratch/r18interop/watch.log`). This report
  therefore proves the D2 baseline is green and byte-recorded *before* the
  change; the claim-O change must be re-verified against the same three
  commands afterwards, and this seat's file will carry a dated appended section
  if the change lands inside the round-18 window.
- Proven: reproduction of the recorded verdict and bytes, determinism, and
  discriminating controls. Not proven: anything about D4 (claim D's other arm),
  the civ map (claim C), or verdicts of rows outside the D2 path.

---

## 6. Post-generalization re-verification — appended 2026-10-18 (10:35Z–10:42Z)

Claim O's generalization landed inside this seat's window: the gate file changed
under `tools/gates/typed-pipeline-gate.py` (full sha trajectory in `interop-3.md`
§5). The three recordings above were re-run against two generalized revisions,
each verified stable before *and* after the run:

| gate revision | when | plain path | `--json` | frozen row 1 |
|---|---|---|---|---|
| `d102fd1d…68e27d` (round-11 freeze) | 10:20Z–10:22Z | exit 0, 16/16 legs, sha `15cdfbda73cd56cb…5f2e695b` | sha `19765ddf…8f47e62` | byte-identical to `run.log` (`9a69985a…`) |
| `ea95e2a1452ef51d…65d282d` (first settle, ≥120 s stable) | 10:35Z | exit 0, 16/16 legs, sha `15cdfbda…` | sha `19765ddf…` | sha `9a69985a…`, `cmp` identical |
| `286d6e82711427ea…3b8c12af9` | 10:42:09Z | exit 0, 16/16 legs, sha `15cdfbda…` | sha `19765ddf…` | sha `9a69985a…` |

`--selftest` under `ea95e2a1`: **12/12 checks passed**. So the generalized gate
keeps the default D2 path **byte-identical on all three recorded artifacts**
while adding its declared-identity legs for packets that declare one (the D4
packet reaches `ok L1-assembler` + `ok L1-expected-holds`).

Same window, adjacent observation (claim D's other arm, other seats): the D4
packet under the generalized gate still exits **2** on
`FAIL L1-build: adapter missing: tools/assemble-d4-typed.py` — the file was
absent at 10:42Z. That is a could-not-evaluate reading, not a hold set.

**Caveat for the parent:** the gate kept changing after 10:42Z (10:39 `84dc177e`,
10:40 `a201afee`, 10:41 `286d6e82`, and on). The three commands in §0/§5 must be
re-run once the O wave settles — expected (and previously observed at every
generalized revision): `15cdfbda…`, `19765ddf…`, `9a69985a…` unchanged.
