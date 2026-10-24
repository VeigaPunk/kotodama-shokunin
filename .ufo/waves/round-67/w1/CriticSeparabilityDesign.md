# CriticSeparabilityDesign — r67 separability expected-findings table

Seat: CriticSeparabilityDesign (critic). Scope: derive the r67 expectation for
`tools/check-claim-separability.py` from `reports/round-67/claims.json`

> **Addendum — L1 resolution (same-day):** the C-APPEND vs Ca-D4 id conflict
> (CriticFrontier F-class) is resolved by sequencing, not revision: A_r
> (S801-S804 + r66 dispositions) → A_c (C's lands; S805-S828 only) →
> A_o → A_ca (Ca's lands; S829+ rejects + lesson). Joint predicate is
> satisfiable as sequenced. Consequence for this table: `corpus/SOURCES.md`
> lands under C and Ca with **different bytes** (A_c vs A_ca). The OVERLAP
> line still counts once, but in dynamic repair runs the two overlays collide —
> last writer wins — so Ca+C repair would show Ca the A_c registry (D4
> under-counts S829 rejects) and C+Ca would show C the A_ca registry (APPEND
> extra=S829+). Both already fail for stronger reasons; the collision is a
> second-order artifact worth a parenthetical in the run report. Ca's own
> lands must carry the A_ca SOURCES bytes or D4 cannot see its own rejects.
(separability_note) + the r66 baseline `reports/round-66/telemetry/separability-real.txt`
(8 findings), so ExecSeparabilityReal can verify its run line-by-line.

Sources read: checker docstring + `_static_findings`/`_overlap_findings`/`_acceptance_findings`/`_nests`
(tools/check-claim-separability.py); all three r67 counters; r66 manifest+output;
staged draft `.ufo/waves/round-67/stage/separability-manifest.json`; base/tip trees.

## Mechanism recap (what can and cannot fire)

- `name_paths()` = a unit's lands **absent at base** only. Naming a base-present
  land (e.g. `corpus/SOURCES.md`, `LOG.md`) is never a finding.
- Static finding = a *claim's added lines* naming another unit's base-absent land
  (whole path; `tools/x.py` ≠ `x.py`). Records never depend; all r67 exports are
  `[]` → zero export findings possible.
- Overlap finding = the identical path in two units' lands. **Nested-but-unequal
  paths across units are INPUT_ERROR** (`_nests`, line ~450) — so a directory land
  in one unit plus files under it in another is a crash, not a finding.
- Dynamic finding: acceptance argv runs in `git clone --shared` of --root,
  `--detach`ed at base + the unit's land overlays. `git rev-parse main` inside the
  clone resolves the **lane tip at run time**, not base. A fail repaired by one
  other unit → `X->Y`; by none → `X-><base>`. Single-unit repairs only: a leg
  needing *two* units' lands (e.g. Ca's SEQ needs C's **and** O's counters)
  can never be repaired → reads `X-><base>`.
- `_read_worktree`/`_lookup` raise INPUT_ERROR on absent lands and on directory
  lands → a manifest that copies `claims.json` lands verbatim mid-wave cannot run.

## r66 → r67 class map

| r66 finding | class | r67 fate | why |
|---|---|---|---|
| Ca-><base> (rc=1, unrepaired) | dynamic `<base>` | **REPEATS** | new cause: SEQ leg greps `accept-c.py`+`accept-o.py`; no single unit repairs it. If manifest stamps `--lands <base>` (as staged) it fires for the degenerate stamp reason instead. |
| Ca->C via `reports/round-*/accept-c.py` | static land-path | **REPEATS** (`reports/round-67/accept-c.py`, accept-ca.py:63) | SEQ COUNTERS literal; counter is in C.lands, base-absent. |
| Ca->O via `reports/round-*/accept-o.py` | static land-path | **REPEATS** (`reports/round-67/accept-o.py`, accept-ca.py:64) | same. |
| Ca->O via **`tools/check-receipt-seq.py`** | static land-path | **NEW** (accept-ca.py:62 `SEQ_TOOL`) | note under-predicts: it says "counter reads" only; the SEQ leg also runs the O tool's selftest. |
| Ca->R ×3 (lesson + telemetry lands) | static land-path | **DISAPPEARS as staged** | r67 accept-ca names no dry-run/controls/recapture telemetry. The one r67 record-ish path it does name — `reports/round-67/telemetry/post-records.txt` (accept-ca.py:15) — is **not in the staged REC lands**, so Ca->REC = 0 despite the note's prediction (see F-3). |
| O-><base> (rc=1) | dynamic `<base>` | **DISAPPEARS under honest stamp** | O lands (tool + 5 mutants + accept-o) are self-contained and all exist (worktree + tip b78f8b8): STAMP/SELFTEST/DIFF/OPTIONS/LANDS/TOPO/HEADERS/MUT/R66/FIXTURES all evaluable on base+O.lands. **Resurrects as stamp-artifact** if `--lands <base>` is kept. |
| — | overlap | **NEW: `C/Ca corpus/SOURCES.md`** (1 line) | r67 declares the registry in both lands arrays (shared dispositions); identical string → OVERLAP, allowed (only _nests conflicts are fatal). A second overlap `C/Ca corpus/lessons/round-67.md` fires **iff** Exec lands it under both units; assign it to one. |
| — | `<base>` on C | **NEW** | C acceptance can't pass on base+pruned-C.lands this wave regardless (entry/S805-S828 don't exist yet; under the staged `--lands <base>` stamp it fails at STAMP even sooner). |
| export-match findings | static export | none (r66 also had none) | all `exports: []` in r67 claims.json. |

## Expected findings, two manifest branches

Branch A — honest stamp: `--lands` = `git rev-parse main` at manifest-write
(currently `b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21`).

| # | expected line | status vs note |
| 1 | `SEPARABILITY_OVERLAP C/Ca corpus/SOURCES.md` (+ `corpus/lessons/round-67.md` if double-landed) | note is silent on overlaps |
| 2 | `SEPARABILITY_DEPENDENCY Ca->C via land path 'reports/round-67/accept-c.py'` | predicted |
| 3 | `SEPARABILITY_DEPENDENCY Ca->O via land path 'reports/round-67/accept-o.py'` | predicted |
| 4 | `SEPARABILITY_DEPENDENCY Ca->O via land path 'tools/check-receipt-seq.py'` | predicted class, unnamed path |
| 5 | `SEPARABILITY_DEPENDENCY Ca-><base> via acceptance … and no declared unit's lands repairs it` | note-implied blind spot: SEQ asserts C's **and** O's counter bytes, below the checker's single-unit repair horizon; still true at A_ca (SEQ is version-insensitive) |
| 6 | `SEPARABILITY_DEPENDENCY C-><base> via acceptance …` | note silent; mid-wave unavoidable (entry/S805-S828 not yet landed). At closure this should disappear — the A_c lands commit makes C pass on its own lands |
| 7 | `SEPARABILITY_DEPENDENCY Ca->REC via land path 'reports/round-67/telemetry/post-records.txt'` | **only if REC lands add post-records.txt** — predicted, currently unexpressible |

Total ≈ 6–7 findings + N Ca->REC. skipped=0 expected (O's FIXTURES leg is the
slowest run; 240s budget is generous).

Branch B — staged `--lands ad5b52b0…` (base as stamp): STAMP fails on every
claim (`main`==tip in the clone) → `C-><base>`, `O-><base>`, `Ca-><base>` all
fire as **stamp artifacts**; repairs can never pass. Same static+overlap lines.
Verdict reads like r66 but the O-><base> recurrence is manufactured, not real.

## Findings (critic)

- **F-1 (design defect, fixable): staged manifest stamps `--lands <base>`.**
  With needs_git clones, `rev-parse main` = lane tip ⇒ evaluated≠stamped ⇒ every
  acceptance exits 1 ⇒ all dynamic findings read `<base>` regardless of true
  dependencies. The dynamic leg becomes incapable of finding a real X->Y.
  Correction: resolve `git rev-parse main` at manifest-write, embed that sha,
  and re-run promptly (lane-tip move between write and run silently reverts to
  Branch B — the manifest pins a stale stamp). Alternative honest choice: omit
  `acceptance` or run `--static-only` and declare the partial verdict.
- **F-2 (note under-prediction):** separability_note predicts "Ca->C and Ca->O
  via counter reads" + "Ca->REC" only. Actual static leg also yields Ca->O via
  `tools/check-receipt-seq.py` and — under any stamp — Ca-><base> because SEQ's
  dependency is on *two* units (below the checker's single-unit repair horizon).
  The `<base>` line is honest but its text won't say "needs C and O"; read it as
  such, not as a counter defect.
- **F-3 (note prediction currently unexpressible):** Ca->REC requires REC to
  hold a base-absent land that Ca's added bytes name. The only candidate named
  is `post-records.txt` (accept-ca.py:15), absent from staged REC lands. Putting
  `.ufo/waves/round-66/*` under REC while Ca lands `.ufo/waves/round-66/` trips
  the `_nests` INPUT_ERROR; putting them under Ca makes the D1-asserted
  dependency invisible (self-name skipped). Correction: REC should land
  `post-records.txt` (and/or enumerated wave-66 evidence files with the
  Ca-side directory land dropped), else the predicted class simply won't appear.
- **F-4 (disappears, as tasked):** the r66 unevaluable-leg class (Ca's D2
  carrier leg asserting a post-records commit at lands) is gone — r67 counters
  assert lands-time evaluable legs only; carrier-parentage is explicitly
  post-records (`post-records.txt` re-verified by hand at closure, claims.json
  note line 113). The residual risk moved to lands-time deps (F-3) and stamp
  pinning (F-1), not to unevaluability.
- **F-5 (timing):** mid-wave, most C lands and the dispositions manifest don't
  exist; a verbatim claims.json lands manifest is INPUT_ERROR, and every
  directory land (`.ufo/waves/round-66/`, `mut-o/` unexpanded) is INPUT_ERROR
  too. The staged manifest already prunes/expands correctly on this axis; a
  full verdict is only meaningful at lands. Report the mid-wave run as
  provisional.

## Impacted axes / smallest safe correction

- Axis: calibration (Ca claim evidence) primarily; operability secondarily
  (O-><base> would falsely testify the tool is not self-contained).
- Correction for ExecSeparabilityReal: re-stamp `--lands` to the run-time main
  sha (Branch A), keep `corpus/SOURCES.md` in both lands (declared overlap) and
  `corpus/lessons/round-67.md` under exactly one unit, add
  `reports/round-67/telemetry/post-records.txt` to REC lands if available,
  verify the output against the Branch A table above.

No tools installed this run (pacman pause noted; nothing needed).
Report: .ufo/waves/round-67/w1/CriticSeparabilityDesign.md
