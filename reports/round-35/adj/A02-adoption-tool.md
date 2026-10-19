- Seat: A02 | executor | claim A | date 2026-10-19 | baseline 4a7aede

# A02 — adjacency audit slice: `receipt_guard_adoption.py` + `adoption-inventory.json`

Claim A, slice 2 of 6 (per `reports/round-35/targets.json` A02 mission: "in-lane
ownership, no sibling-path writes, language scan"). Method: read both artifacts in
full, re-run the tool's own controls at HEAD, and probe its write surface in
isolated `.scratch` stand-ins. No filed byte was written or executed; every probe
that needed a write target used a scratch copy.

Audited bytes (sha256, `git status --porcelain` clean for all three):

| artifact | sha256 | lines |
|---|---|---|
| `tools/harness/receipt_guard_adoption.py` | `5858abcd0261e8176ebb285db6d80a7c36185d9a12895b4b43b75710db036544` | 1309 |
| `reports/round-34/op/adoption-inventory.json` | `ceeb8d0413e2832a8555e5a9467f016208a477fc708c7f3834bcc429a6bebf04` | 1825 |
| `tools/harness/receipt_guard.py` (dependency) | `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1` | — |

## Verdicts

| surface | verdict | finding |
|---|---|---|
| in-lane ownership (tool) | green, one named gap | A02-F2 (registration) |
| sibling-path reads/writes | green by default; claim over-broad | A02-F1 |
| language / cross-domain bleed | green (zero matches) | — |
| PROVINCE owns/refuses accuracy for this surface | green | — |
| record reconciliation (inventory vs SCORECARD/LOG/validator) | both readings correct at their times; citation mismatch | A02-F3 |

## In-lane ownership — green

- The tool is a lane instrument beside its four registered peers
  (`tools/harness/{packet_links,packet_uncertainty,r8_checks,receipt_guard}.py`,
  registered at `SKILL.md:452-454`), and `PROVINCE.md` owns "this lane's own
  gates, source-check records, non-canon examples and reports". In-lane.
- Its population is this lane's own runners only
  (`RUNNER_GLOB = "reports/round-*/run-validation.py"`,
  `receipt_guard_adoption.py:60`), its sweep roots are in-lane
  (`SWEEP_ROOTS = ("reports", "tools")`, `:62`), and its guard dependency is the
  lane's own (`GUARD_TOOL = "tools/harness/receipt_guard.py"`, `:59`).
- Zero references to sibling lanes, the world bible, or domain source trees: a
  repo-wide grep for `receipt_guard_adoption` (excluding `.scratch/` and `.git/`)
  resolves only to this lane's `SCORECARD.md:616`, `LOG.md:3604,3634`, the round-34
  claims/targets/telemetry inputs, the round-34 op/review/calib fragments, and the
  tool itself.
- The tool asserts no canon/clearance/closure verdict: hazards are the census's
  findings, not its failure (exit contract, `:31-34`), and the per-class protocol
  strings (`:79-96`) prescribe this lane's own re-run discipline
  (`isolated-copy-only` = the F-C13-1 prevention rule) — routed, not absorbed.
- No contested item is absorbed; nothing here touches lore-owned canon or
  operator-owned promotion.

## Language / bleed scan — green

Word-boundary, case-insensitive scan of both artifacts for
`canon|canonical|clearance|promotion|promote|closure|closed|lore|chousa|kake|kotoba|ownership|absorb|contest(ed)?`
→ **zero matches in either file** (`grep -nEi … ; exit=1`). The unanchored scan
produced only `ast.Attribute` false positives in the tool
(`:217,218,223,237,…`). The inventory's runner excerpts (`_clip` copies of runner
source, e.g. `adoption-inventory.json:137` (r5) and `:1276` (r26)) inherit no
cross-domain language, because every excerpt is this lane's own runner bytes.
Independent concurrence: `reports/round-35/adj/A06-province.md:223` ran its own
`grep -nEi 'canon|promot|clearance|lore-shokunin|fleet'` over the tool → no
matches.

## A02-F1 — write-scope claim is broader than the mechanism (severity: low)

**Claim under audit.** `receipt_guard_adoption.py:26-28` — "this tool never
executes a runner, **never writes into a filed round**, and pins each row with the
runner's `sha256` at read time"; restated as a limit at `:789` and copied into the
filed artifact at `adoption-inventory.json:99` — "This tool executes no round
runner and writes no filed receipt; `--out` refuses absolute paths, path escapes,
and `validation.json` destinations."

**Mechanism.** `_safe_out` (`:1261-1267`) refuses exactly three things —
absolute paths, `..` in `path.parts`, `.git` in `path.parts` — plus any path named
`validation.json`; otherwise it returns `root / path` (`:1267`), where `root` is
the user-supplied `--root` (`:1276-1277`), and the caller writes there
(`:1296-1299`). Nothing refuses a destination under a filed round
(`reports/round-1..34/**`), under `corpus/lessons/`, or under
`tools/gates/frozen/**`.

**Probes** (all writes landed only in `.scratch` stand-ins):

| probe | command (abridged) | observed |
|---|---|---|
| A | `--json --out /tmp/a02-probe.json` | refused: `--out must be a repo-relative path: /tmp/a02-probe.json` |
| B | `--json --out ../a02-probe.json` | refused: same message |
| C | `--json --out reports/round-35/validation.json` | refused: `refusing to write a receipt path` |
| D | `--root .scratch/a02/iso --out reports/round-34/op/probe.json` | **accepted**, wrote `.scratch/a02/iso/reports/round-34/op/probe.json` (4932 B) — a filed-round-shaped destination |
| E | `--root .scratch/a02/sibling --out notes.json` | **accepted**, wrote `.scratch/a02/sibling/notes.json` (4936 B) — the write lands under whatever root is supplied |

**Assessment.** The refusal set covers the escape classes the docstring names, and
no automatic path writes anything (the only two write sites are `--out` and the
selftest tempdir). But "never writes into a filed round" is not a property the
code enforces: probe D shows a filed-round destination is accepted. This is not a
defect in the round-34 claim — the intended, documented use of `--out` is a round
directory (`reports/round-34/op/O02-tool-source.md:24` proposes exactly that), and
the durable inventory legitimately lives in one. The mismatch is between the
over-broad limits wording and the mechanism.

**Owner:** integrator (this tool is live, not filed bytes; the filed round-34
inventory line 99 is not edited). **Preferred disposition** — wording fix in the
tool docstring and limits so the claim matches the mechanism, e.g.:

```
- The census is static analysis only: this tool never executes a runner and
- writes no round receipt, and pins each row with the runner's ``sha256`` at
- read time.
+ The census is static analysis only: this tool never executes a runner, never
+ writes a round receipt (``--out`` destinations are the operator's
+ responsibility and may be any repo-relative path except ``validation.json``),
+ and pins each row with the runner's ``sha256`` at read time.
```

Optional code hardening (integrator's call, not required for the A-claim): extend
`_safe_out` to also refuse destinations under a *filed* round, which needs a
filed-round boundary input the tool does not have today — the wording fix is the
honest minimal move.

Scope note vs the peer check: `reports/round-35/adj/A07-verify.md:37` (row 15)
scanned for hard-coded absolute-path literals in the tool and returned green —
that check is compatible with this finding, which concerns the `--out`/`--root`
combination, not literals. Both are true; this one is additive.

## A02-F2 — new instrument not registered in SKILL.md's executable-authority table (severity: low-medium)

- `grep -n receipt_guard_adoption SKILL.md` → **0 matches at HEAD 4a7aede**, while
  the three other `tools/harness/` instruments are registered at
  `SKILL.md:452-454`.
- The gap was anticipated in round 34: `reports/round-34/calib/C07-verify-survey.md:194-196`
  — "If claim O lands `tools/harness/receipt_guard_adoption.py` and a later
  `SKILL.md` edit names it, the named set becomes 29 … At HEAD
  `grep -n receipt_guard_adoption SKILL.md` → no match".
- **Consequence to name before anyone registers it:** `SKILL.md` is the population
  source for box-1. `reports/round-30/craft/box1-survey.py:5-6` derives
  `named = re.findall(r"tools/[\w./-]+\.py", SKILL.md)`, and the round-34 durable
  receipt records `named_in_skill: 28`, `resolvable: 28`, pinned to
  `skill_sha256 f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`
  (`reports/round-34/craft/box1-resurvey-durable.json`). I measured `SKILL.md` at
  HEAD: sha256 `f9bd07c2…`, 732 lines — **the pin is still live**, so the box-1
  receipt is current and the 28-executable population is still accurate. A
  `SKILL.md` edit that names the new tool moves the denominator to 29 and
  supersedes that reading: the edit and a box-1 re-survey must land together, and
  the r34 receipt is superseded as a **new row**, never edited.
- **Owner:** the round that next edits `SKILL.md` (this round's integrator, or a
  routed item). Not a claim-C/O/A acceptance blocker; the round-34 claim O's
  stated deliverable (claims.json, `after_required`) did not include registration,
  so this is a discoverability/registration gap, not a missed deliverable.

## A02-F3 — inventory count vs the figures cited from it (severity: informational)

- **Independent concurrence:** `reports/round-35/adj/A07-verify.md:36,54-56` re-ran
  the same comparison and files the identical drift as **A07-F1, severity medium**.
  The evidence agrees exactly (28 filed vs 29 live, the one added r34 row, zero
  per-runner class disagreements); only the severity label differs. A08/the
  integrator owns the label — this fragment's rating is "informational" because the
  drift is declared in three places and no filed row is wrong, A07's "medium"
  because the durable artifact understates HEAD. Either way it is routed, not a
  blocked claim.
- Filed artifact: `adoption-inventory.json:3-6` `{guarded-refresh: 17,
  unguarded-in-place: 11}`, `:110` `"runner_count": 28`.
- Cited figures: `SCORECARD.md:616` "inventory of all 29 filed runners: 18
  guarded-refresh / 11 unguarded-in-place"; `LOG.md:3634-3635` the same 29/18/11;
  and the round-34 acceptance runner asserts `len(runners) != 29` with
  `expected_counts = {"guarded-refresh": 18, "unguarded-in-place": 11}`
  (`reports/round-34/run-validation.py:210-211`).
- Live re-run at HEAD 4a7aede (`--json`, stdout only): `runner_count 29`,
  `{guarded-refresh: 18, unguarded-in-place: 11}`, `census_complete true`,
  `hazard_count 11`, findings `[RGA-1-round-26, RGA-2]`. Diff against the filed
  artifact: **the only row difference is the addition of
  `reports/round-34/run-validation.py`** (classified `guarded-refresh`); no filed
  row changed, no row disappeared.
- Cause and disposition: the JSON was generated at `da68a6d`, before round 34's
  own runner existed — declared at `reports/round-34/op/O02-tool-source.md:36`
  ("28 is the filed census at `da68a6d`; `reports/round-34/run-validation.py`
  does not exist yet") and covered by the tool's own limit ("Row digests pin the
  bytes read during this census, not HEAD at commit time; re-run after any landing
  that touches a runner", `:786-788`, copied at `adoption-inventory.json:98`).
  `LOG.md:3604-3606` records 28 (mid-wave entry) and `LOG.md:3634-3635` records 29
  (admission entry) — both correct at their times. The residue is only that
  `SCORECARD.md:616` cites `op/adoption-inventory.json` as the evidence row for the
  29 figure while that artifact carries 28; the 29 reading is reproducible by
  re-running the tool (my command below) and is what the r34 validator asserts.
  **Owner:** integrator — a new-record note (or a refreshed inventory snapshot in a
  later round); filed bytes are not edited.

## A02-O1 — foreign `--root` produces declared-hazard mismatch noise (informational)

Running the census on a root without this lane's runners (probe E's stand-in)
emits `RGA-1-*` findings with `observed_class: None` for every declared hazard,
because `DECLARED_HAZARDS` (`:73-78`) are absolute lane paths compared against the
supplied root's rows (`:716-728`). Not a defect for the tool's default use; worth
one limit line if `--root` is ever pointed at a foreign tree. Owner: integrator.

## Reproduction commands (all at HEAD 4a7aede, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`)

| command | observed |
|---|---|
| `python3 -B tools/harness/receipt_guard_adoption.py --selftest` | exit 0; `selftest_passed true`, 38/38 controls; `live_runner_count 29`; `live_class_counts {guarded-refresh 18, unguarded-in-place 11}`; `live_findings [RGA-1-round-26, RGA-2]` |
| `python3 -B tools/harness/receipt_guard_adoption.py --json` | exit 0; 29 rows; identical to `adoption-inventory.json` except `date`/`root` and the added round-34 row |
| `python3 -B tools/harness/receipt_guard_adoption.py --sweep-repo --json` | exit 0; `files_scanned 246`, 27 writers (all `kind=runner`), `parse_gaps 0`, `sweep_complete true` |
| `sha256sum tools/harness/receipt_guard.py` | `d2297da4…` == `adoption-inventory.json:92` `guard_tool.sha256` (provenance reproduces) |
| `grep -nEi '\b(canon\|clearance\|promotion\|closure\|lore\|…)\b'` both artifacts | zero matches |
| `git status --porcelain` after every run | clean (no filed byte moved by this seat) |

## Owed

- `reports/round-35/scout/K04-touched-census.md` — absent at write time
  (`reports/round-35/scout/` does not exist); risk classes for this slice were
  therefore derived from `PROVINCE.md` + the claim-A text in
  `reports/round-35/claims.json` directly. If K04's census names a risk class for
  these two artifacts that the four checks above do not cover, A08/A10 completes it.
- `reports/round-35/run-validation.py` — not yet authored (claim A's counting
  command names it); the validator legs for this slice are S04's spec, not this
  fragment's. Suggested legs if useful: `--selftest` exit 0 + `selftest_passed
  true`; `--json` runner_count ≥ 29 with the r34 row classified `guarded-refresh`;
  `--out` refusal of an absolute path and of a `validation.json` destination;
  zero-match language scan on both artifacts.
- A02-F2's registration edit (SKILL.md + paired box-1 re-survey) and A02-F3's
  citation note are routed to the integrator, not performed here.

## Citations

- `tools/harness/receipt_guard_adoption.py:26-28,31-34,56-62,73-78,79-96,97-111,716-728,786-789,1082-1085,1261-1267,1276-1277,1296-1300`
- `reports/round-34/op/adoption-inventory.json:3-6,92,98,99,109,110,1170-1175`
- `reports/round-34/op/O02-tool-source.md:24,36`
- `reports/round-34/calib/C07-verify-survey.md:194-196`
- `reports/round-34/run-validation.py:196-212,210-211`
- `reports/round-34/craft/box1-resurvey-durable.json` (`named_in_skill: 28`, `skill_sha256 f9bd07c2…`)
- `reports/round-30/craft/box1-survey.py:5-6`
- `SCORECARD.md:616`; `LOG.md:3604-3606,3634-3635`
- `SKILL.md:452-454`; `PROVINCE.md` (owns/refuses lists)
- `reports/round-35/claims.json` (claim A); `reports/round-35/targets.json` (A02 seat, shared_rules)
- Commands: `sha256sum` on the three audited files + `SKILL.md`; `python3 -B tools/harness/receipt_guard_adoption.py --selftest|--json|--sweep-repo --json`; `--out` probes A–E; `grep -nEi` language scans; `git status --porcelain`; `wc -l SKILL.md`
