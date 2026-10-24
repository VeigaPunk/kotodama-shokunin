# RevSeparability — attack on the round-66 separability design (claims.json + manifest_units)

Scope: the frozen unit allocation in `reports/round-66/claims.json` `separability.manifest_units`
(`reports/round-66/separability-manifest.json` does not exist at the tip), the instrument
`tools/check-claim-separability.py`, and the Ca acceptance legs that the allocation must isolate.
Base `94209e8f80969dbac48d56c5d0e2e623635b8616`. Lane tip: no manifest, no
`telemetry/separability-real.txt`; `main` is still at base.

Direct answers to the two assigned questions:

1. **Does the allocation hide a cross-claim path-name? Yes, at least four.**
   `Ca->C` and `Ca->O` are real land-path dependencies that the checker prints and the
   frozen `expected_findings` does not declare — and the claim's own note classes any such
   finding as a real defect. `C->Ca` exists but as a hardcoded whitelist of Ca's base-present
   entry, which the static leg is structurally incapable of seeing.
2. **Does Ca's D2 git leg isolate? No.** The `needs_git` counterfactual is a *byte* overlay on a
   `git clone --shared` of the real lane, so `main` inside it is the lane's real branch and
   `git log -1 main -- <receipt>` returns the real carrier commit (demonstrated, §HIGH-2).
   The leg's verdict is a function of lane history, not of the counterfactual.

---

## HIGH-1 — Undeclared `Ca->C` and `Ca->O` land-path dependencies (release-blocking per the claim's own note)

Evidence (reproduced by running the frozen instrument against a file-level manifest built from
the frozen `manifest_units`, `--static-only`):

```
SEPARABILITY_DEPENDENCY Ca->C via land path 'reports/round-66/accept-c.py' named at reports/round-66/accept-ca.py:45
SEPARABILITY_DEPENDENCY Ca->O via land path 'reports/round-66/accept-o.py' named at reports/round-66/accept-ca.py:46
SEPARABILITY_DEPENDENCY Ca->REC via land path '.ufo/waves/round-66/spec-v2.json' named at reports/round-66/telemetry/seat-evidence.txt:2
SEPARABILITY: 3 findings
EXIT=2 (static-only partial)
```

- `reports/round-66/accept-ca.py:44-48` defines `COUNTERS = {<receipt>: <counter path>}` with the
  literals `reports/round-66/accept-c.py` and `reports/round-66/accept-o.py`. Both are lands of C
  and O and both are absent at base (`reports/round-66` has no entry in `git ls-tree -r <base>`),
  so `name_paths()` counts them.
- This is not a cosmetic mention: D2 opens each counter (`cblob = read(root, counter_path)`) and
  compares its sha256 to the receipt's `counter sha256 (self):` line
  (`accept-ca.py:122-130`). Ca's predicate therefore cannot pass unless C's and O's counter
  *bytes* are exactly the stamped bytes. That is a substantive cross-claim coupling.
- `claims.json separability.note` declares only Ca->REC and states verbatim: "No C->O, C->Ca,
  O->C, O->Ca, Ca->C or Ca->O dependency is declared; any such finding is a real defect."
  The frozen `expected_findings` (one Ca->REC path + one Ca->REC acceptance line) is therefore
  wrong on its face: the actual run prints **at least six** findings, not two
  (adds Ca->C, Ca->O, Ca->REC via `final-measures-o.txt`, `final-measures-ca.txt`, and
  Ca->REC via `spec-v2.json` inside Ca's own D3 receipt).
- The `spec-v2.json` route is worth naming separately: `seat-evidence.txt:2` is a Ca land that
  names REC's wave spec, so even Ca's *dispatch receipt* reaches into a REC land.

Fix direction: either drop the counter sha binding from D2 (it is what forces Ca->C/Ca->O) and
verify receipt sequencing without reading other claims' counters, or declare Ca->C and Ca->O as
known instrument classes *with* an argument for why the coupling is acceptable — the current
text makes them blocking by construction.

## HIGH-2 — D2's git leg reads lane refs; the `needs_git` counterfactual is not a history counterfactual

- `tools/check-claim-separability.py:608-627` (`_git_counterfactual`) runs
  `git clone --shared --no-checkout <lane> <work>` then `checkout --detach <base>`. A clone
  carries the source's branches, so `<work>` has the lane's real `main`; the checkout only moves
  HEAD to base. Overlays are written as *untracked files*.
- `accept-ca.py:106-112` then runs `git -C <counterfactual> log -1 --format=%H main -- <receipt>`.
- Demonstration (throwaway lane, same code path): base commit `1c59561`, a second commit
  `0e5a5f3` adding the receipt; clone as the tool does, `checkout --detach base`, receipt
  overlaid uncommitted:

```
counterfactual HEAD=1c59561  counterfactual main=0e5a5f3
git log -1 main -- receipt => 0e5a5f3 parent=1c59561
receipt tracked in counterfactual? 0
```

  The counterfactual tree does not contain the commit, yet the ancestry leg resolves it.

Consequences, in order of severity:

1. **Pre-integration the leg always fails and is unrepairable.** With lane `main` at base, the
   carrier lookup returns empty (`no_carrier`), D2 fails, and no unit's *bytes* can repair it —
   ancestry is history, not content. `_acceptance_findings` (tool:723-745) then prints
   `SEPARABILITY_DEPENDENCY Ca-><base> ... and no declared unit's lands repairs it`. That
   finding is undeclared and structurally unrepairable: the counterfactual's own base cannot
   supply a commit. (The tool's own mutant `mut2_unresolved_to_base.py` treats `C-><base>` as a
   legitimate outcome, so this would not be recognized as an artifact.)
2. **Post-integration the leg passes on real history.** The verdict flips with lane `main` while
   Ca's land bytes are identical — a same-identity reroute, i.e. the failure mode this round's
   review is supposed to reject via one canonical runtime. Any rebase, squash, or commit
   reordering changes Ca's verdict with no change to any Ca land.
3. **When it passes, its evidence is derived from other claims' lands.** D2 also compares
   `git rev-parse <stamped>^{tree}` to the receipt's `tree: ...` line (`accept-ca.py:118-121`).
   The stamped revision is a real integration commit; its tree is the one that contains C's
   entry and O's tool. So the receipt certifies a tree that necessarily holds the other claims'
   bytes.
4. The declared note calls this "history-derived, consistent with counterfactual overlays".
   That is inaccurate: history is not overlaid, so it is *outside* the counterfactual, not
   consistent with it. Declaring a leak does not make it isolation.

Fix direction (any one works): (a) have the checker create a synthetic commit inside the clone
(`git -C work commit -m sep <overlays>` on `refs/claim-sep/counterfactual`) and forbid the
acceptance from reading any other ref — then "base" means base-of-history too; or (b) rewrite D2
as a static receipt check (stamped revision + expected carrier supplied by the caller), and keep
the dynamic leg for the content legs only; or (c) at minimum run D2's acceptance against a
counterfactual ref (`refs/claim-sep/*`) so a real-ref read exits non-zero instead of silently
succeeding. The same leak applies to C: `accept-c.py:281` runs
`git diff --name-only BASE main -- corpus/knowledge` in its own needs_git clone — C's NOHARM
verdict depends on which other claims are committed between base and `main`.

## HIGH-3 — The frozen allocation is not a runnable manifest; the D4 receipt cannot have been produced by it

- `reports/round-66/separability-manifest.json` is absent. The frozen check command exits 2:
  `SEPARABILITY_INPUT_ERROR cannot read manifest 'reports/round-66/separability-manifest.json': No such file or directory`.
  The manifest is also a REC land in the same block, so the REC unit is itself incomplete.
- Translating `manifest_units` verbatim is impossible. Reproduced against the real parser:
  `claims[1].lands[1] is not canonical (empty, '.' or '..' component): '.ufo/waves/round-66/stage/mut-o/'`
  (exit 2). `_repo_path` (tool:338-348) rejects trailing-slash lands; O's mutant dir and REC's
  `.ufo/waves/round-66/w1/` are exactly that. Directory lands are unsupported in both load
  modes anyway: `_read_worktree` (tool:477-495) requires a regular file or symlink, `_lookup`
  (tool:272-299) requires `FILE_MODES`; a directory has no "landed bytes".
- **O's unit is therefore not self-contained.** `accept-o.py:217-242` requires
  `.ufo/waves/round-66/stage/mut-o/` to exist and to hold four named mutants; if the dir is
  absent it records `leg("MUT", False, "mutant dir absent")`. With the frozen lands (which cannot
  overlay a directory), O's acceptance fails at base+own lands, no repair helps, and the dynamic
  leg prints `SEPARABILITY_DEPENDENCY O-><base>` — again undeclared. The alternative is that the
  real manifest silently expands the directory to the four mutant files, i.e. the checked
  allocation is not the frozen allocation.
- **REC's `w1/` is unowned.** Until it is expanded to individual files, any claim may name files
  under `.ufo/waves/round-66/w1/` without a finding.
- **The D4 receipt is a precondition of the run that must produce it.** REC lands include
  `reports/round-66/telemetry/separability-real.txt`, and `_load_units` (tool:498-513) raises
  `InputError` for any land absent at its unit's tree. So the manifest cannot be evaluated until
  the receipt already exists (as a worktree file or as a committed blob) — yet
  `separability-real.txt` is supposed to be that run's output. The receipt therefore always
  predates the run that justifies it, which is precisely the stale/fabricated-stamp shape.
  Either drop the receipt from REC's lands, or generate it to a path outside the manifest's
  lands and commit it afterwards with the run's provenance.

So the D4 chain is: a receipt that must be produced by a command whose manifest does not exist,
over lands the tool rejects. Whatever lands in `separability-real.txt` is not evidence that this
allocation was evaluated.

## MED-4 — Base-present lands are exempt, and every unit declares `exports: []`; the two real couplings that go through existing files are invisible

- `name_paths()` (tool:392-394) only returns lands absent at base. `_static_findings`
  (tool:657-673) only runs the export leg over `y.exports`; all four units declare `[]`. The
  detector surface is therefore exactly "a base-absent land path named inside a claim's bytes" —
  nothing else.
- **C->Ca (invisible, real):** `accept-c.py:285` hardcodes
  `allowed = sorted([ENTRY, GAMES_ENTRY])` where `GAMES_ENTRY` is Ca's land
  `corpus/knowledge/culture-material/games-play-sport-contests.md`. C's NOHARM passes only
  because it whitelists Ca's entry, and it evaluates that whitelist against real `main`
  (`accept-c.py:281-284`). Base-present ⇒ never a `name_path`, and no export regex exists ⇒ not
  detectable. This is a deliberate cross-claim allowance baked into C's counter, undeclared.
- **Ca->O at the evidence level (invisible, real):** `separability-real.txt` is O's tool's
  output; O's tool land exists at base (old version), so naming it never counts, and
  `accept-ca.py` does not invoke it (D4 only greps the receipt). The Ca->O dependence is
  semantic, not textual, and the instrument cannot see it.
- Minimum fix: give each unit a non-empty `exports` list naming what it introduces
  (`scent-perfume-aromatics-codes`, `SEPARABILITY_PARTIAL`, `acceptance_runs=`,
  `s753-recapture`, criterion-18 wording, ...), and require every hardcoded cross-unit allowance
  (C's `GAMES_ENTRY`, Ca's receipt paths) to appear in `expected_findings` explicitly.

## MED-5 — D4 is an unbound text check (false-stamp surface)

`accept-ca.py:150-155` accepts any text containing `^SEPARABILITY: \d+ findings$`, an
`acceptance_runs=\d+`, and no `PARTIAL`. It does not bind the receipt to the manifest bytes, base
rev, tool sha256, argv, or a time; it accepts `SEPARABILITY: 0 findings` (so the declared
Ca->REC findings are not required to be present) and does not reject `SEPARABILITY_UNRESOLVED`.
Note `acceptance_runs=` is emitted on **stderr** as `SEPARABILITY_NOTE ...` (tool:833-835) while
the verdict line is stdout, so a legitimate receipt must be a `2>&1` capture; a hand-written
two-line file passes identically. Given HIGH-3, the only receipt obtainable today is the
hand-written one. Fix: require a header (tool sha256, manifest sha256, base rev, argv) and
re-derive `acceptance_runs` from the manifest (acceptance units × (1 + repairs)) instead of
trusting text; reject `UNRESOLVED`.

## MED-6 — `--jobs` verdict invariance is only established for unbounded runs; the frozen command uses a budget, where scheduling decides which repairs are skipped

`accept-o.py:202-212` compares `--jobs 1` vs `--jobs 4` with no `--budget`. Under a binding
budget, `_Budget.take()` (tool:696-711) is consulted before each repair; a unit whose repair
would have run under jobs=1 can be skipped under jobs=4 (and vice versa), and a skipped repair
becomes `SEPARABILITY_UNRESOLVED` with **no** `<base>` conclusion (tool:723-745). The result is
still honest (PARTIAL, exit 2, never a fabricated finding), but the claim's "--jobs ... verdict
unchanged" holds only unbounded. Consequence for Ca: D4 rejects any PARTIAL, so the receipt can
only come from a run where `--budget 300` never bound; the frozen command does not guarantee
that (accept-o's own FIXTURES leg reports 6.3 s wall, accept-c runs a corpus sweep, accept-ca
runs three `git log` pairs plus a quotes check, and any failed initial run adds up to three
repair runs). Fix: make the budget deterministic (decide skips in manifest order before any run
starts, or use per-unit slices), or drop `--budget` from the receipt-producing invocation and
keep it for exploratory runs.

## LOW-7 — D3 can be satisfied by eight self-selected files (adjacent, but it is a Ca land in the dependency graph)

`accept-ca.py:129-140` requires `reported >= 8`, every named `.md` to exist, and one line
matching `(?i)(seat|report|status)`. It never checks a last-error line for a dead seat and never
binds the receipt to the dispatch call (`taskcall-v2.json`). Current seed: `D3 FAIL named=65
existing=8` — it flips to PASS purely by files landing. `seat-evidence.txt` is also the Ca land
that names REC's `spec-v2.json` (HIGH-1).

## LOW-8 — stamp provenance

`accept-c.py:137`, `accept-ca.py:75-77`, `accept-o.py:109` all run `git rev-parse main` without
`-C root`, i.e. in the process cwd. In a git-free counterfactual (temp copy, not a repo) that
line yields `unresolvable` or reads an enclosing repo; C's `needs_git: true` happens to mask it.
Cosmetic for the verdict, but the printed "measured revision" is not guaranteed to describe
`--root`.

---

## What I verified vs inferred

Verified by execution (all read-only; no lane writes, no git/jj writes):
- The frozen check command exits 2 with `SEPARABILITY_INPUT_ERROR` (manifest absent).
- The verbatim `manifest_units` allocation is rejected by the parser on the trailing-slash
  directory land; a file-level reconstruction parses and prints the Ca->C, Ca->O, Ca->REC
  land-path findings above.
- The clone refs leak, using the exact `_git_counterfactual` sequence (base HEAD, real `main`,
  receipt untracked yet ancestry resolved).
- `accept-ca.py` current output: D1 FAIL, D2 FAIL (receipts absent), D3 FAIL (named=65
  existing=8), D4 FAIL, CRITERION FAIL, QUOTES FAIL.

Inferred from code reading (labelled): that the dynamic leg would print `Ca-><base>` /
`O-><base>` pre-integration (from `_acceptance_findings` + the unrepairable-by-construction
argument), and the exact full finding list once the real manifest exists.

## Verification gaps / residual risk

- No `separability-manifest.json` to audit; I audited the inline `manifest_units` block as the
  assignment specifies. If the L1 writes a different manifest, HIGH-1's exact line numbers may
  shift but the `COUNTERS` literals and the D2 git leg remain.
- I did not run the full dynamic leg (requires a working manifest plus three acceptances, and
  the lane is at base with drafts only). The dynamic conclusions are code-derived plus the
  reconstructed-clone experiment.
- No LSP server applies to this lane's data files (JSON manifest, Python without project
  config); `lsp status` was not consulted. All semantic claims here come from executing the
  frozen instrument and unit counters, which is stronger than grep for this artifact class.
- My broader static-enumeration sweep (every unit's expanded lands × every other unit's
  base-absent lands, including the wave directories) was aborted after 60 s — expanding REC's
  `w1/` and O's mutant directory makes the scan quadratic, and the directories are invalid as
  lands anyway. The findings above are the confirmed subset from the direct tool run; a sweep
  can only add routes, not remove the ones cited.
- No tool installs were needed (python3 stdlib + git only); nothing was installed or upgraded.
