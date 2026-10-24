# CriticSeparabilityDesign — r66 v2 wave 1

Seat: critic (separability design). Scope: attack the declared expected class `Ca->REC`; test the
hypotheticals `C->O`, `O->C`, `Ca->C`. Sources of truth: `reports/round-66/{claims.json,
accept-c.py, accept-o.py, accept-ca.py}`, `tools/check-claim-separability.py` (tip, `M` in
worktree vs base), `.ufo/waves/round-66/stage/mut-o/mut{1..4}*.py`, `tools/check-gate-quotes.py`,
`reports/round-66/telemetry/{dry-run,controls}-*.txt`. No manifests edits made; read-only.

Checker semantics used below (verified in `tools/check-claim-separability.py`):
- Static leg scans each non-record unit's **added lines** for (a) other units' export regexes,
  (b) other units' land paths **absent at base**, matched as whole paths (`_name_re`,
  tool:628; `_static_findings`, tool:640-660).
- Dynamic leg runs `X.acceptance` in base + `X.lands` only; on failure, **pairwise** repair
  attempts `base+X.lands+Y.lands` for each other unit `Y`. Every repairing unit yields
  `X->Y`; if none repairs, `X-><base>` (tool:707-741).
- `needs_git:false` (O) runs in a **git-free** `shutil.copytree` of base (tool:579-592);
  `needs_git:true` runs in `git clone --shared` checked out at base (tool:608-622) — the lane's
  real refs are visible there.
- Lands are read per path and must be regular files or symlinks; a **directory land raises
  InputError** (`_read_worktree`, tool:487-489; `_lookup` per file otherwise).

## Predicted findings on the frozen `manifest_units` (the checker run claims.json advertises)

1. `SEPARABILITY_DEPENDENCY Ca->REC via land path 'reports/round-66/telemetry/final-measures-c.txt'` — DECLARED (expected[0]).
   But the same static leg also emits one finding **per receipt**: `final-measures-o.txt` and
   `final-measures-ca.txt` are named at `accept-ca.py:41-42` and are REC lands absent at base.
   `expected_findings` declares only the `-c.txt` instance; the checker will print three
   land-path findings (plus more if expanded `w1/` seat-file lands are named inside
   `seat-evidence.txt`). Under-counted expectation, same declared class — a completeness defect
   in the frozen block, not a new class.
2. `SEPARABILITY_DEPENDENCY Ca->C via land path 'reports/round-66/accept-c.py'` — **REAL DEFECT, undeclared.**
3. `SEPARABILITY_DEPENDENCY Ca->O via land path 'reports/round-66/accept-o.py'` — **REAL DEFECT, undeclared.**
4. `SEPARABILITY_DEPENDENCY O-><base> via acceptance ...` — **REAL DEFECT, undeclared** (see H4).
5. `SEPARABILITY_DEPENDENCY Ca-><base> via acceptance ...` — **REAL DEFECT**: the declared
   `Ca->REC via acceptance` (expected[1]) will **not** be emitted, because no single unit's
   lands repair Ca's acceptance (see F2).

## Hypotheticals assigned

### H1 — C->O: "accept-c reads the upgraded tool" — DISPROVEN.
`reports/round-66/accept-c.py` contains no reference to `tools/check-claim-separability.py`,
`.ufo/waves/round-66/`, `reports/round-66/`, or any O/REC land path. Its only subprocesses are
`git show BASE:corpus/SOURCES.md`, `git diff --name-only BASE main -- corpus/knowledge`, and
`reports/round-28/readme/sweep.py` (lines 83, 281, 293); `sweep.py` greps clean for
`separability`/`check-claim` (verified). All paths it names (`corpus/SOURCES.md`,
`corpus/README.md`, `GAMES_ENTRY`, `SWEEP`) exist at base or are its own lands, so the static
leg cannot fire either. **No C->O, C->Ca, or C->REC path exists.**

### H2 — O->C: "mut-o fixtures name the entry path" — DISPROVEN.
`mut1..mut4` are byte-mutants of the tool itself; grep across all four shows the only
`corpus/SOURCES.md` mentions are inside copied selftest fixture strings (`mut*:984,1070` — a
synthetic unit file, and `corpus/SOURCES.md` resolves at base so `name_paths()` excludes it
anyway). No mutant, fixture lane, or `accept-o.py` line names
`corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md`, the S7xx id space as an
export, or any C/REC land path absent at base. The fixture claims are named `C`/`S` but build
synthetic files under `tempfile` lanes (`accept-o.py:146-188`). **No O->C or O->Ca path
exists.** (O does name its own land `mut-o` dir and `tools/check-claim-separability.py` —
self, skipped.)

### H3 — Ca->C: "QUOTES gate ids live in the registry Ca does not own" — DISPROVEN as stated;
### the real Ca->C/Ca->O comes from D2's COUNTERS dict.
- The gate-id half fails to bite: `accept-ca.py:174` counts `S(776..800)` matches **inside
  `corpus/lessons/round-66.md`** — a Ca land. The ids' strings live in Ca's own land; the
  registry is never consulted for them. Needs `>=25` distinct ids from the lesson file alone.
- `check-gate-quotes.py` does read `corpus/SOURCES.md` (a C land) via `registry_teaches()`
  (tool lines 193-212, invoked unconditionally by `check()` at line 322) — but only to feed
  `truncated_grounds`, which emits a finding when a Gate Grounds quote is an incomplete prefix
  of the row's teaches cell. For S777-S800 the teaches lookup misses at base → the check is
  vacuous under base bytes and active only with C's lands. A dependency requires the C-less
  run to be *worse*; here the C-ful run can only add findings. **No `Ca->C via acceptance`
  from QUOTES.** Residual smell for reviewers, not a separability finding: `SOURCES.md` is
  silently read beside the lesson, so QUOTES is structurally blind to the 24 new rows'
  grounds-vs-teaches conformance, and if the scribe quotes an *incomplete prefix* of S776's
  teaches, the finding fires only post-integration (a false-pass in the counterfactual, never
  a dependency line).
- The real defect: `accept-ca.py:44-46` `COUNTERS` literally names
  `reports/round-66/accept-c.py` and `reports/round-66/accept-o.py` — C's and O's lands, both
  absent at base (verified `git cat-file -e BASE:` missing). Whole-path match succeeds on the
  added lines → **Ca->C and Ca->O via land path**, both undeclared → real defects.

### H4 (found while tracing) — O-><base> via `needs_git:false`.
`manifest_units.O.needs_git` is `false`, but `accept-o.py`'s DIFF leg runs
`git -C root diff BASE -- tools/check-claim-separability.py` (line 128) and treats rc!=0 as
FAIL. The git-free counterfactual has no `.git`; `git diff` exits non-zero (stderr
"not a git repository"), DIFF fails, `ACCEPT-O-66: FAIL`. No unit's lands install a `.git`, so
`repairs=[]` → `SEPARABILITY_DEPENDENCY O-><base>`. The manifest design forgot that the O
counter is history-derived exactly like C's and Ca's. **Fix: `needs_git: true` for O** — the
clone is checked out at base with O's lands overlaid, `git diff BASE -- tool` sees the
upgrade, `git rev-parse main` resolves.

### F2 — D2 counter-sha read breaks the DECLARED Ca->REC dynamic finding.
`accept-ca.py:135-141` reads each counter file from the **worktree**
(`read(root, counter_path)` → `os.path.isfile`-style) to re-derive the stamped
`counter sha256 (self)`. In `base+Ca+REC`: receipts exist, git legs pass, but
`accept-c.py`/`accept-o.py` are absent → `d2_bad={...counter_absent}` → D2 FAIL. The repair
loop is strictly pairwise; `base+Ca+REC+C` still fails on the o receipt's counter, `+O` on the
c receipt's, `+REC` on both counters. Nothing repairs → the dynamic verdict is
`Ca-><base>`, and the declared `Ca->REC via acceptance` never prints. So the D2 design both
(a) creates the two static defects in H3 and (b) converts the one expected dynamic finding
into a `<base>` defect.

## Smallest safe corrections (for L1; canonical judge decides)

1. **D2 counter read → stamped revision.** Replace the worktree read with
   `git show <stamped>:<counter_path>` (or `<carrier>:<counter_path>`) in `accept-ca.py` —
   the stamped revision is already required to exist (the `rev-parse {stamped}^{tree}` leg).
   The receipt then proves the counter bytes at the measured revision, which is the intended
   ancestry re-derivation; `base+Ca+REC` repairs cleanly → `Ca->REC via acceptance` as
   declared. Also derive the counter path programmatically
   (`"accept-%s.py" % receipt_id`, joined under `reports/round-66/`) so the literal land
   paths no longer appear in added lines — kills both static findings without weakening the
   check (the hash still pins the exact counter bytes).
2. **O needs_git: true** in `separability-manifest.json` (and the claims.json
   `manifest_units` illustration, which is frozen spec for the file L1 must generate).
3. **Directory lands**: `.ufo/waves/round-66/stage/mut-o/` and `.ufo/waves/round-66/w1/` as
   literal lands → InputError (`not a regular file`). The generated manifest must expand them
   to per-file lands (`stage/mut-o/mut1_...py` ×4; `w1/<seat>.md` ×N).
4. **expected_findings completeness**: declare all three `final-measures-*.txt` land-path
   hits (and any `w1/<seat>.md` hits inside `seat-evidence.txt`), or enforce parity; else the
   real run prints undeclared findings that masquerade as defects.

## Other probes run (negative)

- `accept-c.py` on Ca lands: `GAMES_ENTRY` exists at base → `name_paths` excludes it;
  `NOHARM`'s allow-list intentionally includes the games entry → no `C->Ca`.
- `accept-ca` on C lands: names no `corpus/SOURCES.md`, `README.md`, or scent entry path → no
  further `Ca->C`.
- No `SEPARABILITY_OVERLAP` pairs: the three units' land lists are disjoint.
- `dry-run-o.txt` shows `ACCEPT-O-66: PASS` — i.e. the O dry run was taken on the live
  worktree (tip tool already carrying the new flags), not on a base-bytes tree; consistent
  with the tool being ` M` in the worktree, but note the controls receipt only asserts the
  option-refusal control, so O's "counter fails at base" evidence is the base tool refusing
  `--jobs/--budget/--max-runs/--static-only` (controls-o.txt), which does hold.

## Dependencies noted (absent artifacts — recorded, not blocking)

- `reports/round-66/separability-manifest.json` does not exist yet; claims.json
  `manifest_units` is its frozen spec. All predicted findings above assume it is generated
  verbatim from that spec (with directory lands expanded per correction 3).
- `reports/round-66/telemetry/final-measures-*.txt`, `separability-real.txt`,
  `s753-recapture.txt`, `corpus/lessons/round-66.md`, `.ufo/waves/round-66/registry.json` are
  not yet on disk — dynamic-run outcomes are derived from counter source + tool semantics,
  not executed. `[INFERENCE]` only where flagged.

No tools installed (existing python3/git sufficed). Time: within box.
