# RevSeparable — round-79 W1: O/Ca shared-path dependencies and counterfactual base+only-claim evaluation

Seat: RevSeparable (leaf, wave-1 pre-data build/recon). Scope per assignment:
"every O/Ca shared path dependency and counterfactual base+only-claim
evaluation." No shared files edited; all work under
`.ufo/waves/round-79/w1/stage/RevSeparable/` and scratch
`/fast/scratch/hyaku/kotodama-r79/RevSeparable/` (removed after receipt
copy). Lane read-only throughout; the only git mutations are inside the
explicitly initialized, root-verified scratch fixture repository
(`git rev-parse --show-toplevel` asserted before every commit there).

Tool installs: none (pacman paused; only `python3 -B`, `git`, and the lane's
existing `tools/check-claim-separability.py` / `scripts/sources-census.sh`).

## 1. The record both claims touch (verified committed bytes)

All facts below are re-derived from committed bytes at base
`44f76d456c1b326a71ffdb381590af825cbf11be` (raw output:
`receipts/p1-base-counterfactual.txt`, `receipts/p2-receipt-and-registry.txt`):

| fact | value |
|---|---|
| receipt | `reports/round-78/telemetry/census-end.txt` line 33: `kotodama W01 S884 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md` |
| receipt digest | `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867` — identical at `4b255745…` (the commit that landed it) and at base; blob `62eb55b…` unchanged |
| recorded revision | `4b255745dea45a45d88b17e3c3fea4cdb6700cf7` (receipt carries no stamp header — only `Command:`/`Exit: 0`; the "recorded revision" is the landing commit, as the round-78 verifier spot-check already asserts) |
| registry actual token | `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` at `4b255745`, at base, and since the row's introduction at `d7a38405`; the `r13` token **never** appears in any committed `corpus/SOURCES.md` (pickaxe over all refs, empty) |
| r13 file existence | `git ls-tree -r` at base: zero paths matching `worldbuilding-setting-practice.amend-2026-10-24-r13` (the `amend-2026-10-24-r13` suffix exists only on `heritage-taxonomy-models`, S874 — the likely naming-convention source of the capture-time rename) |
| green control | `reports/round-78/telemetry/census-start.txt` line 33 (same commit) matches the registry (`…10-23.md`) |
| uniqueness | full W01 sweep of both round-78 receipts against the registry: **S884 in census-end is the only mismatch** (4 W01 lines per receipt; all others MATCH) — exactly the draft's "one recorded mismatch" |
| base absence | S897 absent from the registry at base (`git grep` exit 1); `reports/round-79/` absent at base. O's S897 is a new export; note round-77's *draft* also planned an S897 (naming-systems source) but honest-stopped before landing — the id is free in **committed** bytes; seats must check committed bytes, not drafts |
| observation re-run | `sources-census.sh validate` against a clone at `4b255745` prints the `10-23` token (receipts/p3-observation-rerun.txt; clone root asserted, `status --porcelain` empty). The receipt's `r13` stated token is **not re-derivable from committed bytes at any revision**; the capture answered `Exit: 0`, so the renamed file must have existed on disk at capture — the receipt reflects an uncommitted working-tree state (QUALITY 17/29 class, as routed defect 2 of the round-78 verifier spot-check already filed) |

Self-assessment sizing check (draft's pre-freeze disposition): SHONEN.md:6's
census counts re-derive exactly — `808/713/58/37` at round-75 Ca landing
`012e8d3c`, `817/722/58/37` at C landing `4f5e3b25` (census mode re-run in the
clone; receipts/p4-shonen-counts.txt). SCORECARD self-assessment rows are
count-level or ledger-closed (L01–L03 etc.); no SCORECARD/SHONEN row states
the S884 `used-by` token. **Finding: no corresponding self-assessment
mismatch exists.** Per the draft's own sizing rule this supports rejecting Ca
before freeze and landing the correction as unclaimed conformance repair; the
counterfactual machinery below serves either disposition unchanged (the
correction record and its counter are the same artifact either way).

## 2. Shared path dependencies (the deliverable)

### 2.1 Base-existing read-shared paths (not separability findings — the checker's base-existing-path rule — but shared calibration-record dependencies)

| path | O reads it for | Ca reads it for | coupling risk |
|---|---|---|---|
| `corpus/SOURCES.md` | S897ROW leg (O **lands** an append: S897 row) | MISMATCH/CORRECTION legs re-derive the actual token at the measured revision via `git show` | If O's append diff-hygiene touches the S884 row (or any re-wrap), Ca's lands-time re-read of the S884 row changes. Ca pins the measured revision, so grading is safe; but O's static diff must be exactly one appended row. Also: Ca must **not** land this file (overlap) and must **not** cite S897 (O's export → static finding, demonstrated as M3) |
| `reports/round-78/telemetry/census-end.txt` | the guard's S884 observation fixture (stated token) | RECEIPT leg digest pin; stated-token re-derivation | Both grade the same immutable bytes; neither may write it (changed-receipt control, demonstrated row 8). Single writer history: only `4b255745` |
| `reports/round-78/telemetry/census-start.txt` | green control for the same predicate | same | read-only both |
| `scripts/sources-census.sh` | re-runs the approved observation | same | QUALITY 28: both counters must pin the tool's bytes at freeze (sha256 compare) — a tool upgrade mid-round changes both legs' meaning |
| `reports/round-79/claims.json` (+ `ledger.json` if Ca keeps ledger shape) | frozen constants + legs | same | one freeze file, two claims; each counter must LEGCOUNT only its own claim's `legs[]` and read only its own constants |
| `.ufo/waves/round-77/w2/{MutCaLedger,ScoutLogPairs,ExecCaPass}.md` | S897's cited evidence (R77 mismatch classes) | — | base-existing, so citation by Ca would not be a *checker* finding, but the draft bars it: "This claim owns records only, not O tool or S897." Keep Ca's bytes free of S897 and of the guard path |
| `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-79.md` | records append | records append | neither's added lines may cite the other's export ids (`S897` vs the correction id, e.g. `C79-1`) — M3 shows the checker catches O citing `C79-1` in an added registry line |

### 2.2 Write-overlap risks (must stay empty for the real claims)

- `corpus/SOURCES.md`: O lands it (S897 append). Ca lands nothing in it — the registry already carries the actual token; the draft's correction is a new record binding digest/revision/old/actual, not a registry edit.
- `reports/round-79/telemetry/*`: per-claim filenames (O: `guard-*`, `selftest-o.txt`; Ca: `controls-ca.txt`, `junk-ca.txt`, …). M4 shows the checker reports `SEPARABILITY_OVERLAP` on any shared new path.
- Distinct export ids before dispatch, per QUALITY 7: O exports `S897`; Ca exports its correction id (name it in claims.json, e.g. `C79-1`, and nowhere else).

### 2.3 The one structural shared dependency to design for

The dynamic separability leg overlays a claim's lands as **uncommitted files**
in a clone checked out at base (`tools/check-claim-separability.py
_git_counterfactual`: clone → `checkout --detach base` → `_place` overlays →
run argv). A counter whose legs read only `git show <lands>:<path>` **cannot
see its own lands** in that overlay. Round-65's manifest shows the accepted
idiom: acceptance argv = the counter itself in a default/overlay grading mode
(`python3 -B reports/round-65/accept-c.py`, `needs_git: true`). **The real r79
counters need an explicit overlay/worktree grading mode** (or a manifest
acceptance probe that reads worktree bytes), or every dynamic leg will print a
false `X-><base>` finding. My fixture counters implement `--overlay` as the
toy model; receipts/p8-separability-runs.txt shows the false positive this
section warns about (first m1 run, rc=2 from argparse, before the mode
existed) and the clean 0-findings result after it.

## 3. Counterfactual base + only-claim evaluation

### 3.1 Against the real lane (no fixture)

- **Base (no claim data):** O cannot pass — `reports/round-79/` is absent at
  base (p1 §P9); any O acceptance argv errors. Ca's ground fact is derivable
  at base: stated `r13` ≠ actual `10-23`, count=1 (p1 §P2b/§P3 vs §P7; p3
  re-run). This is the draft's "re-derives mismatch=1 at base".
- **SHONEN/SCORECARD base checks:** re-derived clean (§1) — no second mismatch
  to size a Ca claim with.

### 3.2 Fixture model (toy scale, real evidence bytes)

Fixture repo (isolated, root verified before every commit; bundle and
extracted files in `fixtures/`; raw outputs in `receipts/p5–p8`):

| ref | commit | content |
|---|---|---|
| B0 | `b96a9830…` | real lane bytes at base: registry + both round-78 receipts (digest verified equal to lane) |
| F0 (freeze) | `b054f567…` | counters + frozen `claims.json` (constants read from freeze; refusals: non-40-hex, unreadable frozen claims, LEGCOUNT, lands==frozen base, freeze-not-ancestor; do-nothing lands==freeze graded-never-passed) |
| O1 | `57006fa0…` | `tools/ledger-token-guard.py`, S897 registry append, red/green + selftest receipts |
| C1 | `134bab63…` | `reports/round-79/correction-s884.md` binding the four fields, append-only |
| mutants | see `receipts/fixrepo-commits.txt` | lie / wrong-revision / changed-receipt / M2 / M3 / M4 trees |

Counterfactual matrix (`receipts/p7-final-matrix.txt`, full transcripts
`p5`/`p6`):

| row | grade | O verdict | Ca verdict |
|---|---|---|---|
| 1 do-nothing (lands==freeze) | F0/F0 | FAIL 0/4 (exit 1) | FAIL 2/4, `MISMATCH count=1`, `UNRESOLVED: 1` (exit 1) |
| 2 only-O | O1/F0 | **PASS 4/4** | FAIL 2/4 — Ca does not pass on O's legs |
| 3 only-Ca | C1/F0 | FAIL 0/4 — O does not pass on Ca's legs | **PASS 4/4, `UNRESOLVED: 0`** |
| 4 refusal | B0/F0 | — | exit 2 `refused: lands equals frozen base` |
| 5 refusal | F0/O1 | exit 2 `refused: freeze not ancestor of lands` | — |
| 6 lying correction | C1+lie/F0 | — | FAIL: CORRECTION+RESOLVED red (exit 1) |
| 7 wrong revision | C1+wrongrev/F0 | — | FAIL: CORRECTION+RESOLVED red (exit 1) |
| 8 changed receipt | C1+receipt/F0 | — | FAIL: RECEIPT red (exit 1) — even a "harmless" rewrite of the historical receipt fails the claim |

Separability runs with the lane's own checker (`receipts/p8-separability-runs.txt`):

| manifest | result |
|---|---|
| m1-clean (O1+C1) | `SEPARABILITY: 0 findings` (dynamic legs: each acceptance passes on base+own.lands; runs=2 skipped=0) |
| m2 Ca names `tools/ledger-token-guard.py` | `SEPARABILITY_DEPENDENCY Ca->O via land path` |
| m3 O's S897 row cites `C79-1` | `SEPARABILITY_DEPENDENCY O->Ca via export 'C79-1'` |
| m4 both land `s884-probe.txt` | `SEPARABILITY_OVERLAP O/Ca` |

The checker's `--selftest` was run first: 63/63 pass (`tools/check-claim-separability.py` at base), so the m1–m4 verdicts rest on a healthy detector.

## 4. Defects found in my own fixture while building it (class warnings for the real counters)

1. **Cell index off-by-one**: the registry row splits into 13 `|`-parts with a trailing empty; used-by is index **11**, not 12. My first counter graded `actual=None` and still printed `count=1` (None ≠ stated) — a silent half-failure. The real Ca counter must pin the cell index with a fixture or assert the row's 11-cell shape (E11-style) before trusting it.
2. **Substring prefix match on correction fields**: `f"actual-token: {actual}" in corr` passed with `actual=''` because `"actual-token: "` prefixes the real line. Fixed to whole-value regex parse + equality. The real counter must parse the correction's fields exactly (whole value), never substring.
3. **Overlay-mode argparse**: acceptance argv in the checker's overlay must not require `--root/--lands/--freeze`. Drove the `--overlay` mode design in §2.3.

## 5. Recommendations for L1 / freeze checklist (O/Ca items only)

1. Ca: reject before freeze per the draft's sizing rule (no self-assessment mismatch found; §1) and land the correction as unclaimed conformance repair — the same record/counter below serves both.
2. Freeze constants for Ca: receipt path, expected digest `05b5011a…`, measured revision `4b255745dea45a45d88b17e3c3fea4cdb6700cf7`, correction path — read from `git show <freeze>:reports/round-79/claims.json`; re-derive old/actual tokens at grade time; pin `sources-census.sh` sha256 (QUALITY 28).
3. Keep the real separability manifest free of: Ca landing `corpus/SOURCES.md`; Ca (or its counter) naming `tools/ledger-token-guard.py`; O citing Ca's correction id; either claim landing a shared `reports/round-79/telemetry/*` path. Declare exports `S897` (O) and the correction id (Ca) in claims.json before dispatch.
4. Real counters: ship an overlay/worktree grading mode for `check-claim-separability.py` (§2.3) and selftest receipts per QUALITY 23/25 at the freeze commit.
5. The correction record should live at a new Ca-owned path (fixture models `reports/round-79/correction-s884.md`); the historical receipt stays byte-pinned by the RECEIPT leg.

## 6. Verification status

Everything above is observed output preserved under
`stage/RevSeparable/receipts/` (p1–p8, `fixrepo-commits.txt`) and the fixture
bundle under `stage/RevSeparable/fixtures/`. Not exercised (out of leaf
scope): the real r79 counters (not yet written), the real freeze manifest,
live fetches (none needed). No lane or fleet files were modified; the fixture
repo is scratch-only and its bundle is the durable copy; scratch was removed
after the copy.
