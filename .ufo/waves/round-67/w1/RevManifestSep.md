# RevManifestSep — r67 v2 review of the separability draft + partial-mode honesty

Seat: reviewer (calibration). Lane `kotodama-shokunin`, base `ad5b52b0ab5691358cd38718ab75649dc9916f9a`.
Instrument: `tools/check-claim-separability.py` (byte-identical to base — `git diff ad5b52b0 -- tools/check-claim-separability.py` is empty; no r67 change to this tool).
Artifact under test: `.ufo/waves/round-67/stage/separability-manifest.json` (landed after I started; `w1/ExecSeparabilityReal.md` is **absent** at review time — see V1).
Everything below was re-run by me; no lane write other than this file (`/tmp/r67sep/**` is scratch).

## Verdict

**Not acceptable as filed for lands-time evidence.** The draft manifest is a *partial land set*: it silently drops 4 of the 13 declared `lands` paths in `reports/round-67/claims.json`, including claim C's primary artifact, and its acceptance argv pins `--lands` to the **base** revision. The full run therefore reports `7 findings / 12 acceptance_runs / skipped=0` in which **all 12 dynamic runs are STAMP failures** and the three `X-><base>` findings are forced by the pinned stamp, not measured. Partial modes (`--static-only`, `--max-runs 1`, `--budget`) *do* degrade honestly — exit 2, `SEPARABILITY_PARTIAL`, exact skip counts, no fabricated `<base>` — so the dishonesty is in the draft's land/stamp inputs, not in the bounded-verdict machinery. The finding-class set also differs from r66: 3 land-path + 3 `<base>` + **1 `SEPARABILITY_OVERLAP`** (a class r66 never produced, and one the frozen `separability_note` does not predict).

## High

### H1. Draft manifest drops 4 declared land paths, including claim C's entry — and nothing in r67 checks it
`reports/round-67/claims.json` vs the draft:

| unit | dropped | added |
|---|---|---|
| C | `corpus/knowledge/culture-material/medicine-healing-codes.md`, `corpus/lessons/round-67.md` | — |
| O | — | `.ufo/waves/round-67/stage/mut-o/` expanded to its 5 mutant files |
| Ca | `reports/round-67/dispositions/r66-wave-evidence-manifest.txt`, `.ufo/waves/round-66/`, `corpus/lessons/round-67.md` | — |
| REC | (no REC unit exists in claims.json) | `reports/round-67/claims.json` + 6 telemetry receipts |

Consequences that I measured:
- Under-report: my faithful reconstruction (same base, same stubs for the 3 not-yet-written paths, `.git` metadata excluded) yields **6 static findings**, the draft yields **4**. The two missing are `Ca->C via land path 'corpus/lessons/round-67.md' named at reports/round-67/accept-ca.py:42` and `SEPARABILITY_OVERLAP C/Ca corpus/lessons/round-67.md` (`.git`-free expansion of `claims.json` lands, `/tmp/r67sep/m4.json`).
- The entry is the one land whose bytes are the claim: a handoff section citing `corpus/SOURCES.md` / `corpus/lessons/round-67.md` would itself create `C->Ca` land-path findings (`corpus/SOURCES.md` is also a Ca land). Excluding the entry excludes exactly that leg. The draft as it stands cannot report on the artifact claim C is about.
- O's land `.ufo/waves/round-67/stage/mut-o/` is *unrepresentable* faithfully (see H2); the 5-file expansion is a curation, not the declared land.
- No r67 leg reads the manifest or the separability receipt: `grep -n "separability\|acceptance_runs\|PARTIAL" reports/round-67/accept-c.py reports/round-67/accept-o.py reports/round-67/accept-ca.py` is empty. So the draft↔claims divergence is uncontested by every frozen predicate.

### H2. Claim Ca's declared lands are not representable in a separability manifest at all
Faithful reproductions of `claims.json` Ca lands all fail structurally (reproduced, exit 2 each):

1. Literal `".ufo/waves/round-67/stage/mut-o/"` → `SEPARABILITY_INPUT_ERROR claims[1].lands[1] is not canonical (empty, '.' or '..' component)`.
2. Trailing slash stripped → `SEPARABILITY_INPUT_ERROR unit C lands 'corpus/knowledge/culture-material/medicine-healing-codes.md', which is absent from the worktree` (pre-data state: the entry, `corpus/lessons/round-67.md` and the dispositions manifest do not exist yet).
3. `.ufo/waves/round-66/` expanded (18,589 files, 283 MB) → `SEPARABILITY_INPUT_ERROR claims[2].lands[56] names .git metadata: '.ufo/waves/round-66/stage/mut-c/fx/.git/COMMIT_EDITMSG'`; the tree contains **7,245** `.git`-metadata paths, every one of which `_repo_path` rejects.
4. Filtering `.git` paths and expanding fully gives Ca 11,351 lands; `_load_units` reads them all as landed bytes and the **static leg alone takes 21.4 s** (`time` on `/tmp/r67sep/m4.json --static-only`).

So *some* curation of Ca's lands is forced. The draft's choice (drop the whole round-66 tree and the dispositions manifest, keep SOURCES/QUALITY/LOG/SCORECARD) is a reasonable engineering call, but it is undocumented in the manifest (no excluded-lands note) and it removes the very records the frozen note says Ca must show a dependency on.

### H3. `--lands` is pinned to the base revision; the full verdict's dynamic leg is 12 STAMP failures and its `<base>` findings are forced
The draft's acceptance argv is `... --lands ad5b52b0ab5691358cd38718ab75649dc9916f9a` for all three claims. Reproducing the tool's own counterfactual (`git clone --shared . /tmp/r67sep/cf; git checkout --detach ad5b52b0; python3 -B reports/round-67/accept-c.py --root /tmp/r67sep/cf --lands ad5b52b0...`):

```
# evaluated revision: b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21
# measured revision (lane main): b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21
# tree: de353b046be5e119c5203f0c5c82e92790c3e546
STAMP FAIL stamped=ad5b52b0 evaluated=b78f8b8e equal=False tree=de353b04 dirty_tracked=False
ACCEPT-C-67: FAIL
```

`accept-c.py` exits 1 at STAMP (lines 175-204) before any data leg. The full run on the draft:

```
SEPARABILITY_DEPENDENCY C-><base> ... (rc=1) and no declared unit's lands repairs it
SEPARABILITY_DEPENDENCY Ca-><base> ... (rc=1) ...
SEPARABILITY_DEPENDENCY O-><base> ... (rc=1) ...
SEPARABILITY: 7 findings
SEPARABILITY_NOTE units=4 ordered_pairs=12 acceptance_runs=12 skipped=0   (exit 1, 2.1 s)
```

`acceptance_runs=12` counts 12 *invocations*, none of which evaluated a claim leg. Two readings are both wrong and both were demonstrated:
- pinned base stamp: STAMP can only pass when main == base, i.e. before lands; post-lands it always fails → `<base>` for every claim (observed).
- unpinned/r66-shape argv (`--root .`, no `--lands`) → argparse `rc=2 ... the following arguments are required: --lands` and the tool still prints a *complete* verdict `SEPARABILITY: 9 findings ... skipped=0, exit 1`, turning a harness usage error into three `X-><base>` dependency assertions (`/tmp/r67sep/full_nolands.txt`).

Per the L1 sequencing ruling (per-claim lands commits A_r → A_c → A_ca), the stamp for C must be A_c and for Ca A_ca; a single manifest with one pinned `--lands` cannot express that. **Minimal fix:** make the stamp a manifest-input the runner substitutes at receipt time (e.g. `--lands` value read from an env var or per-unit `lands_rev` field), file the base-pinned run only as a *pre-data* receipt, and never file a `skipped=0` verdict whose dynamic runs all died at STAMP. That `STAMP` binds `git rev-parse main` of a clone that is *detached at base* (`check-claim-separability.py:608-627`) is the deeper defect: the guard compares a ref, never the measured bytes; the receipt's `# tree:` is `<stamp>^{tree}`, so it cannot distinguish measured base bytes either. This is the R66-D3 class relocated, and it belongs to RevCounterC / RevIntegrity — I attacked it through the manifest's dynamic leg and am reporting it, not judging the counters' disposition.

## Medium

### M1. `SEPARABILITY_OVERLAP C/Ca corpus/SOURCES.md` is a real declared write conflict, a class r66 never had, and it is unpredicted
Both claims land `corpus/SOURCES.md` (C appends S805-S828, Ca appends S801-S804 + the S753 repair). The tool reports it as a finding (`SEPARABILITY_OVERLAP`), counted in `SEPARABILITY: N findings` and exit 1. Two of the three frozen assertions are affected: `separability_note` predicts only "Ca->C and Ca->O via counter reads … record-dependency class only", with no overlap; and the "8 expected findings" hypothesis carries r66's class mix (6 land-path + 2 `<base>`, 0 overlap). A faithful run cannot reproduce it: the draft's class set is 3 land-path + 3 `<base>` + 1 overlap; my faithful reconstruction is 4 land-path + 3 `<base>` + 2 overlaps. Either the claims' land declaration accepts a shared write path (and the note must say so), or the round must give `corpus/SOURCES.md` to one unit and the other must not land it.

### M2. `Ca->REC` cannot exist in this manifest
`separability_note` predicts "Ca->REC via lands-time disposition legs over records committed in the lands commit". But `claims.json` has no REC unit, and the draft's REC unit lands only `reports/round-67/claims.json` + the six pre-data telemetry receipts — **not** the dispositions manifest, not the round-66 lesson. `accept-ca.py` names `reports/round-67/dispositions/r66-wave-evidence-manifest.txt`, which is no unit's land, so no finding is produced (observed: zero REC lines in the full run). The predicted leg is unmeasurable as constructed. If the disposition records are meant to be a record unit, they must be in REC's lands — and then `.ufo/waves/round-66/` (H2) and/or the manifest's overlap budget have to be settled.

### M3. The draft disables the export leg for every unit (`"exports": []` ×4)
r66's manifest declared exports (`scent-perfume-aromatics-codes\.md`, `SEPARABILITY_PARTIAL`); r67's declares none, so `_check_novelty` is vacuous and the static leg is reduced to whole-path mention detection. The coupling this round is actually about — Ca's counter asserting the *structure* of the C/O counters (the note's own "record-dependency class") — is a vocabulary dependency (`--lands`, `STAMP`, `stamped/evaluated`) that a path mention catches only where the file path is literally written (`accept-ca.py:63,:64`). Declaring e.g. `--lands|STAMP` as a Ca export (if novel against base) would make that dependency class explicit rather than incidental.

## Low

### L1. Partial-mode accounting is honest; the residual risk is the reader, not the tool
All three partial shapes measured on the **landed draft manifest**:

| mode | exit | findings | skipped | `SEPARABILITY_PARTIAL` | fabricated `<base>` |
|---|---|---|---|---|---|
| `--static-only` | 2 | 4 (static only) | 3 (= dyn units) | yes, `(static-only)` | none |
| `--max-runs 1` | 2 | 4 (static only) | 9 (= 3 units × 3 repairs) | yes | none |
| `--budget 1` | 2 | 5 (1 `<base>` completed, 4 pairs skipped) | 4 | yes | none |
| full `--jobs 4 --budget 240` | 1 | 7 | 0 | — | 3 (forced, H3) |

`--jobs 1` output is byte-identical to `--jobs 4` (verified with `diff`). `skipped` is exactly the number of dynamic units / skipped repair attempts, each skip is named `SEPARABILITY_UNRESOLVED` per (unit, other), and a skipped repair never becomes `<base>` (`_acceptance_findings`, `check-claim-separability.py:711-742`). Two residual traps: (a) `SEPARABILITY: N findings` is printed *before* the `PARTIAL`/`UNRESOLVED` lines, so a consumer that greps only the count reads a partial verdict as complete — in this round no leg greps it at all (H1); (b) `--budget` makes the *finding set* schedule-dependent (5 vs 7 findings between two runs at the same inputs), honest only because exit is 2.

## Residual risk / verification gaps

- **V1 (dependency):** `w1/ExecSeparabilityReal.md` and `reports/round-67/telemetry/separability-real.txt` were absent at review time; the draft exists only as `stage/separability-manifest.json`. My re-runs are therefore of the draft manifest, not of a filed receipt. If the filed receipt is `--static-only` or `--max-runs 1`, nothing in the round rejects it (H1) — it must be checked at integration.
- **V2:** `corpus/knowledge/culture-material/medicine-healing-codes.md`, `corpus/lessons/round-67.md` and `reports/round-67/dispositions/r66-wave-evidence-manifest.txt` do not exist yet, so my faithful reconstruction used minimal stubs for them. Findings that the *real* entry would add (handoff citations → `C->Ca`) are therefore **[INFERENCE]**, not measured; the draft's omission of the entry is measured.
- **V3:** my reconstruction excluded the 7,245 `.git`-metadata paths inside `.ufo/waves/round-66/` (the tool rejects them) and used the draft's `.git`-free curation for nothing else. Runtime numbers are from this host; the static leg's 21.4 s is dominated by the 11,351-file Ca land set that the draft drops.
- **V4:** I did not judge the r67 counters' STAMP semantics (H3) as a disposition — RevCounterC/RevCounterCa/RevIntegrity own that. I only established that it makes the manifest's dynamic leg non-evaluative.
- Tooling: no installs/upgrades (nothing needed; `python3`, `git` sufficient).

Report: .ufo/waves/round-67/w1/RevManifestSep.md
