# ExecAdaptCa — claim Ca counter adapted for round 77 (BUILD)

Verdict: **BUILD done, self-tested.** `accept-ca.py` is adapted for round 77 at
`.ufo/waves/round-77/w1/stage/ExecAdaptCa/accept-ca.py` (4040 lines, sha256
`ac2bc93d02932464f9ee43222ffe1d06dd5bf1a0e68fd38bd94e10a991489b2e` — `sha256sum
accept-ca.py`). `--selftest` exits 0 with `SELFTEST: 199/199` (receipt
`selftest-ca.txt`). `--ledger-check` passes on the real lane base with a real
11-pair probe ledger (both `-C .` and `-C <lane>` forms). Nothing is committed
here; no lane file outside this wave dir was written.

## Deliverables (all under `.ufo/waves/round-77/w1/stage/ExecAdaptCa/`)

| file | what it is |
|---|---|
| `accept-ca.py` | the adapted counter (copy to `reports/round-77/accept-ca.py` at the freeze) |
| `selftest-ca.txt` / `selftest-ca.err` | full selftest stdout/stderr; stdout ends `SELFTEST OK: 199 checks across 51 scenarios reported-fail=0` and `SELFTEST: 199/199`; stderr carries only the three CLI-error probes the selftest drives deliberately |
| `emit-legs.json` | `--emit-legs` output: the canonical `legs[]` (12) + `legs_sha256` for `claims.json` |
| `probe-real-ledger.json` | scratch probe ledger (11 pairs over real `LOG.md` lines + the real `corpus/README.md:755` totals line); NOT a lane file |
| `ledger-check-real-base.txt`, `ledger-check-real-base-laneC.txt` | `LEDGER-CHECK-77: PASS pairs=11`, exit 0, for `-C .` and `-C <lane>` |
| `probe-no-readme-overlap.json`, `ledger-check-no-readme-overlap.txt` | 10 real `LOG.md` ANNOTATE pairs + 1 REPAIR on `SHONEN.md:6` (mutable set, no README line) → `LEDGER-CHECK-77: PASS pairs=11`, exit 0 |

## What changed against `reports/round-76/accept-ca.py` (routed defects)

1. **LEDGER leg** now grades the whole pair grammar and executes it:
   - `stated_at` must be a **lane** `path:line` inside the frozen allowlist —
     ANNOTATE: `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-75.md`,
     `corpus/lessons/round-76.md`; REPAIR: `corpus/README.md`, `SKILL.md`,
     `SHONEN.md` (constants `ANNOTATE_ALLOW` / `REPAIR_MUTABLE`; a frozen list
     that names a different set is a FROZENCFG problem).
   - `stated_text` must be found **on that line of the base tree** (`git show
     <base>:<path>` inside the base clone) — closes L76-19 (absent stated_text)
     and L76-13 (out-of-allowlist site).
   - `observe_cmd` and `rederive` must **execute**: argv validated (executable
     allowlist, no interpreters/constant printers, no shell meta outside a
     grep PATTERN operand, no bare `name=value` operand), then run in the base
     clone and parsed; for ANNOTATE the re-derivation must already return the
     observed base token. A `git` argv must open with `-C <dir>`, carry a
     read-only subcommand, the revision in rev position and `-- <path>`; the
     round-76 `git grep … <rev>` form without `-C` is refused. The `-C` operand
     is a **declaration**: every non-fleet operand is retargeted to the
     materialized clone before execution, so observations read clone bytes.
   - an `escaped pipe` or backtick outside a pattern operand is now refused in
     the observe_cmd and the rederive alike (r76 admitted a backtick anywhere in
     a rederive).
2. **RECEIPTS leg** rewritten: every telemetry path named by a ledger pair, by a
   committed fixture spec, or by the frozen R1EXEMPT receipt names must be a
   committed blob at `<freeze>` (`git cat-file -e <freeze>:<path>`); at least one
   path must be named (no vacuous green). The round-75 counter re-run is gone.
3. **COMBINED leg** now requires every claim-C `owned_inplace` record to carry
   the **line number** it edits (`base_line`, or `line`), with exact
   `base_text`/`after_text` at base and at the combined tree; a README record
   without a line number fails the leg, and a whole-file fixed surface on a
   README is refused (closes the r76 COMBINED defect).
4. **REPAIR** no longer uses the r76 heading/totals heuristic: a REPAIR pair may
   not target a line that a claim-C `owned_inplace` record owns (precise
   conflict test), so the README totals line is repairable while an in-place
   claim-C line is not.
5. **Leg table** is one structure (`LEG_SPECS`) + one dispatch order; leg names,
   LEGCOUNT refusal, `--emit-legs` and the printed verdict all derive from it.
   The list is the r75/76 lineage, 12 legs, in table order: LEDGER,
   BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY, R1EXEMPT, NOSTUB, SEPARABLE,
   COMBINED, RECEIPTS, FROZENCFG, STAMP. NOSTUB is restored (folded checks added
   to ANNOTATE as well); no LEDGELIST leg exists.
6. **Refusals kept**: `lands == freeze` is graded and can never PASS (exit 2 if
   every leg is green); `lands == base` refused; missing `--combined` and no
   scratch root refused with `ACCEPT-CA-77: FAIL legs=0/12 (refused: …)` and no
   leg line.
7. **Scratch**: `--work`, else `$HYAKU_SCRATCH`, else `$TMPDIR`; with none set
   the counter refuses. No `/tmp` literal anywhere (`grep -n "/tmp" accept-ca.py`
   → 0 matches).
8. **New modes**: `--emit-legs` (prints `{round, claim, legs, legs_sha256}`) and
   `--ledger-check <ledger.json> --base <40hex>` (the pre-freeze build check; the
   same `pair_problems()` the LEDGER leg uses).

## Frozen-config contract the L1 must satisfy (integration)

- `claims.json` Ca `legs[]` **must be `--emit-legs` output** (12 strings,
  table order) and SHOULD carry `legs_sha256` =
  `0f40d78e029f4104e04c89f688a0987e02ddc8466f7ac7eea3930ce48bfa94bd`
  (`python3 -B accept-ca.py --emit-legs | python3 -c 'import json,sys;
  print(json.load(sys.stdin)["legs_sha256"])'` → that value). A different leg
  list is a LEGCOUNT refusal (exit 2); a matching list with a wrong digest is a
  FROZENCFG failure.
- `claims.json` Ca SHOULD list `fixtures` (defaults:
  `reports/round-77/fixtures/r1exempt-{green,red,mixed}.json`). Each fixture is
  a JSON object with a `cells` list (`green` → rule-2 cells, `red`/`mixed` →
  teaches), optionally `row`, `marker`, and may name a telemetry receipt.
- Claim C needs `row_set` ids (S897, S898 per the draft), `entries`, and
  `owned_inplace` records of the shape
  `{"path": "corpus/README.md", "base_line": <int>, "base_text": "<base line>",
  "after_text": "<combined-tree line>"}`. The round-76 record shape had no
  `base_line`; that is exactly what COMBINED now refuses.
- R1 receipts `reports/round-77/telemetry/r1exempt-green.txt` /
  `r1exempt-red.txt` (named by the emitted R1EXEMPT leg text) must be committed
  at the freeze; any telemetry path a pair or fixture names likewise.
- A REPAIR pair must not share `path:line` with a claim-C `owned_inplace` record
  (pick distinct README lines; the probe uses 755 for the repair).
- Graded run form:
  `python3 -B reports/round-77/accept-ca.py --root . --lands <Ca-lands>
  --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin --combined
  <C-lands> --main <Ca-lands> --work /fast/scratch/hyaku/kotodama-r77/<seat>`;
  PASS line `ACCEPT-CA-77: PASS legs=12/12`.

## Selftest coverage (the r76 failure classes are named scenarios)

`stated-text-absent`, `stated-at-out-of-allowlist`, `annotate-on-mutable`,
`no-c-form`, `bare-assign`, `escaped-pipe`, `dead-pin`, `out-of-clone`,
`constant-printer`, `interpreter`, `shell-string`, `rederive-backtick` (positive
control: a backtick inside a PATTERN executes), `annotate-other-token`,
`absence-pair`, `min-pairs`, `green-pair`, `fabricated-base-observation`,
`stated-line-mismatch`, `repair-no-statement`, `repair-not-mutable`,
`shadow-repair`, `expected-after-mismatch`, `stub-rows`, `no-rederive`,
`prose-row`, `append-only-removal`, `protected-in-place`, `unnamed-in-place`,
`r1-rule2-exempt`, `r1-teaches-red`, `r1-mixed-red`, `separable-lane-row`,
`separable-family`, `config-edit-ledger`, `config-edit-claims`,
`freeze-off-first-parent`, `stamp-measured`, `uncommitted-receipt`,
`fixtures-absent`, `readme-exemption-no-line`, `combined-missing-entry`,
`do-nothing`, `clean`, `lands-eq-base`, `combined-required`, `scratch-noroot`,
`legcount`, `legorder`, plus `ledger-check`/`emit-legs`/CLI assertions. Every
implemented leg has at least one named failing mutant (coverage table inside
`selftest()`).

## Evidence (command → raw output)

- `python3 -m py_compile accept-ca.py` → exit 0 (`COMPILE_OK`).
- `HYAKU_SCRATCH=… python3 -B accept-ca.py --selftest` → exit 0;
  `grep -o "SELFTEST OK: [0-9]* checks across [0-9]* scenarios" selftest-ca.txt`
  → `SELFTEST OK: 199 checks across 51 scenarios`; last line `SELFTEST: 199/199`.
- `python3 -B accept-ca.py --emit-legs` → exit 0; 12 legs; digest
  `0f40d78e029f4104e04c89f688a0987e02ddc8466f7ac7eea3930ce48bfa94bd`.
- `python3 -B accept-ca.py --ledger-check probe-real-ledger.json --root
  /home/vgpnk/Projects/shokunin/kotodama-shokunin --base
  211f9526800906e0c585d878d265c37e5e090c15 --work <scratch>` → exit 0,
  `LEDGER-CHECK-77: PASS pairs=11` (and the same with the `-C <lane>` variant).
- `grep -n "/tmp" accept-ca.py` → 0 matches.
- `sha256sum accept-ca.py` → `ac2bc93d02932464f9ee43222ffe1d06dd5bf1a0e68fd38bd94e10a991489b2e`.
- Allowlist files present at base: `git cat-file -e 211f952…:<path>` for
  LOG.md, SCORECARD.md, SKILL.md, SHONEN.md, corpus/README.md,
  corpus/lessons/round-75.md, corpus/lessons/round-76.md, corpus/QUALITY.md →
  all present.

## Risks / notes

- I did not run the counter end-to-end on round-77 data: `reports/round-77/
  claims.json`, `ledger.json` and the fixtures do not exist yet. The selftest and
  the real-base build check are the exercised evidence; the graded run is the
  L1's. **Unrun: end-to-end `ACCEPT-CA-77` on real round-77 landings.**
- `RECEIPTS` is never vacuous but does require the R1 receipts at the freeze; if
  the L1 commits claims/ledger but forgets the receipt files, RECEIPTS is red by
  design.
- The r1 fixtures are read **from the freeze commit**, not from the worktree; a
  fixture left out of the freeze commit fails R1EXEMPT and RECEIPTS.
- REPAIR/claim-C line collision is refused (see contract); the draft's README
  footer line is claim C's in the real lane, so the Ca REPAIR pair should target
  a different README line or a different mutable file.
- No tool installs this wave (nothing needed; python 3.14.8, git 2.56.0 in
  place). No labrat probe was spawned — the hypotheses were settled by the
  counter's own selftest.
- Scratch `/fast/scratch/hyaku/kotodama-r77/ExecAdaptCa` was deleted after the
  receipts above were copied into the wave dir.
