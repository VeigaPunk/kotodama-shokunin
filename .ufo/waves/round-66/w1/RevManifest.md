# RevManifest — attack on the round-66 separability declaration

Seat: L1-kotodama-r66.RevManifest (reviewer, leaf). Base `94209e8f80969dbac48d56c5d0e2e623635b8616`.
Time-boxed; no tool installed or upgraded (none needed), no pacman transaction.
Target of attack: `reports/round-66/separability-manifest.json` — **absent on disk** — so the
declaration under attack is `reports/round-66/claims.json` -> `separability` (note, check,
expected_findings, manifest_units).

Canonical method: the tool's own legs, not a re-implementation. I imported
`tools/check-claim-separability.py` as a module, built `Unit` objects from `manifest_units`,
filled `base_absent` / `base_text` from `git cat-file`/`git show` at base (the tool's own
`_base_object` semantics), and called its `_overlap_findings` + `_static_findings` on the
result. Land contents come from the worktree (the tool's `WORKTREE` tree mode).

## Land map (base fact, verified with `git cat-file -e BASE:<path>`)

ABSENT at base — C: `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md`,
`reports/round-66/accept-c.py`. O: `.ufo/waves/round-66/stage/mut-o/`,
`reports/round-66/accept-o.py`. Ca: `corpus/lessons/round-66.md`,
`reports/round-66/telemetry/{s753-recapture,seat-evidence,separability-real}.txt`,
`reports/round-66/accept-ca.py`. REC: `reports/round-66/{claims.json,separability-manifest.json}`,
`reports/round-66/telemetry/{final-measures-c,final-measures-o,final-measures-ca,census-end}.txt`,
`.ufo/waves/round-66/{registry.json,spec-v2.json}`, `.ufo/waves/round-66/w1/`.

PRESENT at base (so their names do **not** count as dependencies): `corpus/SOURCES.md`,
`corpus/README.md`, `tools/check-claim-separability.py`, `corpus/QUALITY.md`,
`corpus/knowledge/culture-material/games-play-sport-contests.md`, `LOG.md`, `SCORECARD.md`.

Consistency check (non-finding): `manifest_units.{C,O,Ca}.lands` are byte-identical to
`claims[].lands` — no stale/diverged land list. REC has no counterpart in `claims[]` (by design).

## Findings

### HIGH-1 — the declared unit lands cannot be loaded by the declared checker: directory lands with trailing slashes (operability + calibration)

`manifest_units` lists two lands as directories: O `".ufo/waves/round-66/stage/mut-o/"` and REC
`".ufo/waves/round-66/w1/"`. Both are refused before any leg runs.

```
$ python3 -B tools/check-claim-separability.py /tmp/o-only.json --root . --static-only
SEPARABILITY_INPUT_ERROR claims[0].lands[1] is not canonical (empty, '.' or '..' component): '.ufo/waves/round-66/stage/mut-o/'
EXIT=2

$ sed -i 's|stage/mut-o/|stage/mut-o|' /tmp/o-only.json && <same command>
SEPARABILITY_INPUT_ERROR unit O lands '.ufo/waves/round-66/stage/mut-o', which is not a regular file or symlink in the worktree
EXIT=2
```

Repro manifest `/tmp/o-only.json` = `{"schema":"kotodama-separability-manifest-v1","base":<base>,"claims":[{"id":"O","tree":"WORKTREE","lands":[...],"exports":[],"acceptance":[...],"needs_git":false}]}`,
i.e. the O unit exactly as `manifest_units` declares it. Nothing was written inside the lane.

Code evidence: `_repo_path` canonicality (trailing-slash/`.` refusal, `tools/check-claim-separability.py:285`
region), `_read_worktree` -> "which is not a regular file or symlink in the worktree" (:483),
`_lookup` -> "which is not a regular file or symlink (mode 40000)" (:290). The manifest schema has
no directory-land concept: `Unit.landed` is `rel -> (mode, bytes)` and overlays are single-blob
placements (`_place`, :531; `overlays()`, :124). Round 65, which did produce a verdict, expanded
every seat artefact to individual **file** lands — `.ufo/waves/round-65/stage/separability-manifest.json`
lands `.ufo/waves/round-65/rows/ScoutRow01/row-S750.txt` … one file per row, and no trailing slashes
anywhere.

Consequence: the declaration, serialized as written, never yields a verdict (`exit 2`,
SEPARABILITY_INPUT_ERROR), exactly the R65-D4 class this round claims to close. ACCEPT-CA-66's D4
leg ("`telemetry/separability-real.txt` contains a SEPARABILITY: line and an acceptance_runs count,
produced inside the bounded run") cannot be satisfied from this declaration until the lands are
rewritten as files.

### HIGH-2 — undeclared claim-to-claim dependencies Ca->C and Ca->O (calibration)

Canonical static leg on the declared units, verbatim output:

```
SEPARABILITY_DEPENDENCY Ca->C via land path 'reports/round-66/accept-c.py' named at reports/round-66/accept-ca.py:45
SEPARABILITY_DEPENDENCY Ca->O via land path 'reports/round-66/accept-o.py' named at reports/round-66/accept-ca.py:46
SEPARABILITY_DEPENDENCY Ca->REC via land path 'reports/round-66/telemetry/final-measures-c.txt' named at reports/round-66/accept-ca.py:40
SEPARABILITY_DEPENDENCY Ca->REC via land path 'reports/round-66/telemetry/final-measures-o.txt' named at reports/round-66/accept-ca.py:41
SEPARABILITY_DEPENDENCY Ca->REC via land path 'reports/round-66/telemetry/final-measures-ca.txt' named at reports/round-66/accept-ca.py:42
SEPARABILITY_DEPENDENCY Ca->REC via land path '.ufo/waves/round-66/w1' named at reports/round-66/telemetry/seat-evidence.txt:3
SEPARABILITY_DEPENDENCY Ca->REC via land path '.ufo/waves/round-66/spec-v2.json' named at reports/round-66/telemetry/seat-evidence.txt:2
SEPARABILITY_OVERLAP: none
```

`accept-ca.py` (absent at base -> every line is landed) carries
`COUNTERS = {"...final-measures-c.txt": "reports/round-66/accept-c.py", ...}` and D2 hashes that
blob (`reports/round-66/accept-ca.py:140`, `csha = sha256(counter blob)`), so this is not a string
coincidence: **Ca's D2 verification consumes C's and O's landed bytes**. That contradicts the
declaration's own note verbatim — "No C->O, C->Ca, O->C, O->Ca, Ca->C or Ca->O dependency is
declared; any such finding is a real defect." Two such findings exist.

The dynamic leg cannot repair this path either: at `base+Ca.lands` D2 reports
`counter_absent` for all three receipts, and the repair probe tries **one** other unit at a time
(`_acceptance_findings`, `run(unit.overlays() + other.overlays())`, :727). No single unit supplies
both `accept-c.py` and `accept-o.py` plus the receipts, so the expected shape
(`... and passes on base+Ca.lands+REC.lands`) is unattainable and the tool would emit
`SEPARABILITY_DEPENDENCY Ca-><base> ... no declared unit's lands repairs it` — a third forbidden
shape, and the one the round's O claim calls "never fabricated <base>".

Remedy with evidence: every counter already prints `# counter sha256 (self): <sha>`
(`accept-c.py:139`, `accept-ca.py:80`; see `telemetry/dry-run-c.txt:1`). Move the counter-hash
self-check into each claim's own acceptance (C's counter checks its own hash against the receipt it
produced) and leave Ca's D2 to commit ancestry + tree equality only. That removes both claim-to-claim
dependencies without weakening R65-D2.

### MED-3 — expected-finding set is not the observed set (under-declared by 5 of 7 lines)

Declared `expected_findings` has 2 entries; the canonical static leg emits 7. Under-declaration is
concentrated inside the declared class: 5 separate `Ca->REC` land-path findings (the three
`final-measures-*` receipts, `spec-v2.json`, and `w1` from `seat-evidence.txt:3` header), where the
declaration names only `final-measures-c.txt` and a generic acceptance line. Anything else is a
defect per the item; anything inside the class but not listed is still a mis-declared expectation,
because the check's stated purpose is that the verdict be predictable pre-wave.

Note the multiplier: `w1` is a *directory* land, and `_name_re` accepts a descendant path as naming
it, so expanding `w1` to its ~64 file lands (HIGH-1's required fix) converts this one line into one
`Ca->REC via land path` finding per seat report named in `seat-evidence.txt`. Either the header is
trimmed (it currently names `spec-v2.json`, `w1/swarm-registry.json`, `w1/<SEAT>.md` paths) or the
expected set grows by ~64 lines. `swarm-registry.json` is not even a REC land — REC lands
`.ufo/waves/round-66/registry.json`, a different path.

### MED-4 — the declared check cannot be executed, so the expected set has never been observed

```
$ python3 -B tools/check-claim-separability.py reports/round-66/separability-manifest.json --jobs 4 --timeout 120 --budget 300
SEPARABILITY_INPUT_ERROR cannot read manifest 'reports/round-66/separability-manifest.json': No such file or directory
EXIT=2
```

Dependency (not a build defect by itself): the manifest is a REC land, written at integration. But
the round's own controls require the *prediction* to be pre-data (`claims.json` is the frozen
pre-wave instrument). A pre-wave expected set that has never been produced by the tool, and that
diverges from the tool's canonical output on the units as declared, is a calibration failure, not a
timing artefact. Also, a `WORKTREE`-tree manifest is not buildable at any point in this wave until
C's entry and REC's receipts exist on disk; only `tree: <commit>` manifests are buildable, and the
lands commit is the one the manifest is inside.

### LOW-5 — the note's land map is wrong about which receipts are REC lands

`separability.note` says "Ca's D2/D3/D4 legs read committed receipt/evidence files that are lands of
the REC record unit". Only D2's `final-measures-*` are REC lands; `s753-recapture.txt` (D1),
`seat-evidence.txt` (D3) and `separability-real.txt` (D4) are **Ca's own** lands. The stated class
("receipt files absent at base, supplied by REC lands") therefore covers D2 only, which is why the
D3 dependency arrives by a different route (`w1` seat reports) than the note describes.

## Answer to the assigned census

- Every land path absent at base: 18 of the 25 declared lands (C 2/4, O 2/3, Ca 5/7, REC 9/11),
  enumerated in "Land map" above; the other 7 exist at base and are modifications.
- Units whose lands a sibling unit's lands name: **Ca**, and only Ca. Its lands name REC's
  `final-measures-c/-o/-ca`, `spec-v2.json`, `w1` (5 paths), plus C's `accept-c.py` and O's
  `accept-o.py`. C and O name no sibling land: C's `GAMES_ENTRY` re-point target exists at base
  (excluded by `name_paths()`), and O's added bytes name no round-66 path.
- Expected set == declared Ca->REC class? **No.** 2 of 7 lines are outside the class (Ca->C,
  Ca->O, both explicitly declared impossible), 3 of 5 in-class paths are undeclared, and the
  declared acceptance-finding shape (`Ca->REC`) is unattainable by the single-unit repair probe.

## Residual risk / verification gaps

- The dynamic leg was not executed end-to-end: it is unreachable at wave time (missing entry,
  missing receipts, directory lands) and every probe would read a pre-data failure as a
  dependency. HIGH-2's `Ca-><base>` shape is derived from the tool's repair semantics
  (`_acceptance_findings:718-740`), not observed.
- I did not attack O's bounds (`--budget/--max-runs/--jobs/--static-only` behaviour) or its
  selftest; separate seats own those.
- If the L1 expands directory lands to files, re-run the static leg (it will not be the set
  computed here): expected `Ca->REC` grows per seat report named in `seat-evidence.txt`.
- Exactly one temptation to note for the integrator: `--static-only` exits 2 with UNRESOLVED by
  design, and D4 rejects `PARTIAL`; a `--static-only` receipt therefore cannot satisfy D4 — the
  receipt must come from a full bounded dynamic run, which first needs HIGH-1 fixed.
