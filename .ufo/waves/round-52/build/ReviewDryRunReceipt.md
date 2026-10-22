# Review: criterion 9 dry-run receipt (round 52, KotodamaR52.ReviewDryRunReceipt)

Assigned item: QUALITY criterion 9 (`corpus/QUALITY.md:35`) against `reports/round-52/dry-run.py` and the committed receipt `reports/round-52/telemetry/declaration-dry-run.txt`. Author-lane advice; findings are recommendations, not admissions.

## Required command output

`python3 -B reports/round-52/dry-run.py check reports/round-52/telemetry/declaration-dry-run.txt` at the lane worktree:

```
MISSING_FROM_RECEIPT []
UNDECLARED_IN_RECEIPT []
EXIT=0
```

## What the checker does right (verified, not assumed)

- **Two-way comparison is real.** `dry-run.py:71-72` computes both `want - seen` and `seen - want`. Mutation tests on a `/tmp` copy: a receipt missing three commands fails with those three in `MISSING_FROM_RECEIPT` (exit 1); a receipt containing one invented `$ echo invented-command` line fails with it in `UNDECLARED_IN_RECEIPT` (exit 1). Input-shape damage fails safe: removing D's acceptance from the manifest gives `CHECK_INPUT_ERROR 'D'`, exit 2.
- **No declared command is missed for the current declaration.** Six declared commands (2 counting, 2 manifest acceptance, separability, agreement) all appear in the receipt; the six `$ ` lines match verbatim.
- **Expected pre-landing results are named for every command** (receipt lines 5, 9, 13, 19, 25, 29): before values with base line numbers (D: `5 (lines 83, 87, 90, 92, 93 at base)`; C: `227`), acceptance expectations with the before value actually printed in the output (`S094_lines=5`, `knowledge_files=227`) and the after targets (`0`, `228`), the separability absent land named in the error text (`speech-surrogates-whistled-drummed.md`), and the first-absent-land stop disclosed on the separability role line — criterion 9's letter is met by this receipt's content.
- **Receipt is internally consistent with a pre-landing tree**: outputs show S094 count 5, knowledge files 227, separability exit 2 naming the C land — exactly the before-state.
- **Base is identified and real.** Header names full 40-hex `147cfde85eb1...`, equal to `claims.json` `base` and `separability-manifest.json` `base`; `git cat-file -t` says commit; it is `d9f73c8`'s parent. Criterion 8's "receipt committed with the declaration" holds: `git show --stat d9f73c8` = exactly the 4 declaration files + the receipt (5 files, 277 insertions), and `git diff --stat d9f73c8` over those files is empty (worktree identical to the committed declaration).
- **Historical control reproduces.** Running the same check against `reports/round-51/telemetry/declaration-dry-run.txt` exits 1 with both round-51 manifest acceptance `sh -c` commands in `MISSING_FROM_RECEIPT` — the R51-M5 ground of criterion 9 is genuinely caught by this checker.

## Findings

### F1 — Major: `check` never validates the expected-result lines (criterion 9 half-enforced)
`check` parses only `$ ` lines (`dry-run.py:66-67`); the `# role: ...; expected pre-landing: ...` lines are ignored. Experiment: deleting every `# role:` line from the receipt → `MISSING_FROM_RECEIPT []`, `UNDECLARED_IN_RECEIPT []`, **exit 0**. A future receipt could omit or falsify all expectations and still pass the mandated two-way check, defeating criterion 9's "expected pre-landing results are named in the receipt".
Fix: for each declared command, require the next `#` line to equal `# role: <role>; expected pre-landing: <expected>` (whitespace-normalized) and emit a third list, e.g. `WRONG_EXPECTATION`, failing the run otherwise. `declared()` already returns `(role, command, shell, expected)` — the data is in hand.

### F2 — Medium: a manifest acceptance keyed by an id absent from `claims.json` is silently unchecked
`declared()` builds `acceptance` from all manifest claims (`dry-run.py:31`) but iterates only `claims.json` claims (`dry-run.py:33-36`). Experiment: adding an `acceptance` to the manifest's `REC` record unit (id not in `claims.json.claims`) and re-checking the unchanged receipt → **exit 0**; the declared acceptance appears in neither `run` output nor `want`. Since criterion 9's ground (R51-M5) is precisely "manifest acceptance commands omitted from the receipt", the manifest is a declaration source and a silent drop is a hole. Latent today (REC declares no acceptance), live the first time someone attaches one.
Fix: symmetric id check — every `claims.json` claim id must have a manifest acceptance and every manifest acceptance id must be a `claims.json` claim id, else `CHECK_INPUT_ERROR` exit 2 (the input-shape rule of criterion 8).

### F3 — Low: `run` crashes with a raw traceback on the same input-shape errors `check` handles
The try/except in `check` (`dry-run.py:63-69`) covers `declared()`; `run` (`dry-run.py:49-54`) calls `declared()` uncaught. Experiment: manifest acceptance for D deleted → `check` prints `CHECK_INPUT_ERROR 'D'` exit 2, but `run` would raise `KeyError: 'D'`. Fix: same except-branch in `run`, print `CHECK_INPUT_ERROR`, exit 2.

### F4 — Low: the receipt's embedded control output is truncated, not verbatim
Receipt lines 32-33 are exactly 200 chars each and cut mid-token (`'python3 -B tools/check-claim-se`). The reproduced control output (lane root, against the round-51 receipt) is far longer. The embedded `$$ control` block therefore under-states its own evidence; its `exit 1` line survives, but a closure re-running it byte-for-byte would not match. Fix: commit the full control output as e.g. `telemetry/declaration-dry-run-control.txt` and reference the path, or paste untruncated.

### F5 — Low: clock metadata disagrees inside one commit
Receipt stamp `10:39:47Z` (line 1) < `d9f73c8` author=committer `2026-10-22T07:39:52-03:00` (= 10:39:52Z) < `claims.json` `declared_at` `2026-10-22T10:47Z`. A field inside the commit postdates the commit by ~7 minutes, so one of the clocks is stale or pre-filled. Fix: anchor receipts and declarations to the commit hash (drop wall-clock fields or restate them as "committed as d9f73c8"); a wall clock proves nothing a hash doesn't.

### F6 — Residual: `$ `-line misparse (false UNDECLARED)
`seen` accepts any line starting `"$ "` (`dry-run.py:66`). Experiment: injecting `$ simulated-prompt-line-from-command-output` into a command's output region → flagged `UNDECLARED_IN_RECEIPT ['simulated-prompt-line-from-command-output']`, exit 1. No current declared command prints such lines, so this is a known limitation, not a live defect. Mitigation if wanted: `run` emits commands with a distinctive marker (e.g. `$! `) or `check` requires an `exit <n>` line between consecutive command lines.

### F7 — Residual: set semantics collapse duplicates
`seen`/`want` are sets (`dry-run.py:66-67,71-72`): if two declared commands were identical strings, one receipt line would satisfy both, and duplicate receipt lines vanish. All six current commands are distinct, so no live effect. Optional: `collections.Counter` on both sides.

## Answers to the assigned attack questions

- **Does `check` really compare both ways?** Yes — verified by mutation (missing commands flagged, invented command flagged), code at `dry-run.py:71-72`, and the round-51 control failing as designed.
- **Does it miss a declared command?** Not for the current declaration (all 6 found). One structural hole: manifest acceptance entries not keyed by `claims.json` ids are silently ignored (F2). Also note the manifest's `REC` record unit correctly carries no acceptance and is out of criterion 9's scope — not a miss.
- **Are expected pre-landing results named for each command?** Yes, in this receipt, in criterion 9's required forms (absent land with exit 2 and the land named; after-value comparison failing with before value printed). But the checker cannot enforce that — see F1, the main defect.
- **Does the tree line identify the base?** Yes: full hash `147cfde85eb1...`, matching both JSON `base` fields and an existing commit that is `d9f73c8`'s parent; and criterion 8's commit-together rule holds via `d9f73c8`. The `+ uncommitted round-52 declaration files` suffix is the honest description of a state a hash alone cannot reconstruct; the digest fix below closes it. Recommendation: have `run` stamp `# declarations <sha256 of claims.json + manifest + dry-run.py>` in the header and have `check` recompute — this binds the receipt to the exact declared bytes and would also have exposed the F5 staleness window (receipt 10:39:47Z vs `declared_at` 10:47Z).

## Not run / gaps

- The 10:39:47Z worktree state itself is unreproducible post-landing (D landed at `dea5ece` on top); consistency was inferred from the receipt's own before-values plus the empty `git diff` vs `d9f73c8` — no independent re-measurement of the pre-landing tree was possible.
- `tools/check-claim-separability.py` and `claims-agree.py` internals are out of scope here (other seats); only their receipt legs were inspected.
- Checker mutation experiments ran on a `/tmp` copy; the lane repo was not modified (only this report file written).
