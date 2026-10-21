# ExecSepFixture-4 — claim-Ca fixture (r49 frozen fixture + r50 forward manifest)

Round 50 attempt 1, hyaku phase 2. Leaf executor; no installs performed (none needed).

## Assigned item
Build `reports/round-50/separability/r49-fixture.json` (frozen, per Shared contract Ca as refined
by L1 irc 2026-10-21: added-lines-only scanning, path hits only for paths absent at base, exports
novel at base, shared lands → SEPARABILITY_OVERLAP, role:"record" units never dependers, tree
"WORKTREE" reads the filesystem) and `reports/round-50/separability/r50-manifest.json`.

## Artifacts (private clone → patch)
- Clone: `.ufo/waves/round-50/work/ExecSepFixture-4` at base `4ad26836552462d28a946ca3b067cab0b5ce3532` (clone HEAD verified equal).
- `reports/round-50/separability/r49-fixture.json` — sha256 `6bd7f750efed381748f575612a4e969a7f8393ff64b755751e01cd74b06a10e5`
- `reports/round-50/separability/r50-manifest.json` — sha256 `7a31beaa46ac74d5ad571f6b423296a8dfe9e14f284253409d6c0b31b511a735`
- Patch (both files, `git add -N` + diff): `.ufo/waves/round-50/patches/ExecSepFixture-4.patch` (133 lines). Production lane untouched (read-only git only).

## Sha ledger and verification
| ref | full sha | verified by |
|---|---|---|
| r49 base | `c42d675be96b6b3957e6e5c00ab192080cb70083` | rev-parse; `git diff --name-only 78f77a6 c42d675` touches only reports/round-49 framing files (addendum premise transfer re-confirmed) |
| C+Ca+S landing | `c6a174dd4830929e0f8f0de478bb8be29dfb803b` | `git show --stat` (17 files) |
| C-without-S leg fix | `8c78e6bee93a5b1a257d8b98e3d70b2281b35d71` | stat: entry only; `diff --name-only c6a174d 8c78e6b` = entry only |
| r49 adjudicated state | `d91c632fe71515acc8e133a804ed2fcfbbe31264` | diff vs 8c78e6b: LOG/SCORECARD/SHONEN/QUALITY/SOURCES/lesson/validation.json only |
| ledgers | `3596e2bb326be4aa1f3477efc07e8884939964fc` | log ("validation receipt (measured 8c78e6b)") |
| post-review fixes | `8cee75561cab92c8da7edc501d6221b9f9b5cde8` | rev-parse |
| r50 base | `4ad26836552462d28a946ca3b067cab0b5ce3532` | rev-parse == clone HEAD |

Frozen-tree proof: blob sha256 of all 7 `validation.json input_sha256` files at 8c78e6b match the
receipt byte-for-byte (entry `64cb0d55…`, SOURCES `933013a1…`, README `666fb794…`, lesson
`272eab2e…`, revisions tool `d49fdf1c…`, runner `9f5f7a2e…`, claims.json `501eb760…`). 8c78e6b IS
the measured receipt state.

## r49 fixture design decisions
- Lands derived mechanically from `git show --stat c6a174d 8c78e6b`, partitioned per L1: C = entry +
  corpus/README.md; Ca = tools/check-readme-revisions.py + reports/round-49/integration/Ca-evidence.md
  + corpus/README.md (co-landed); S = corpus/SOURCES.md + corpus/lessons/round-49.md + corpus/QUALITY.md
  + SKILL.md. SKILL.md attributed to S by diff content (adds the `corpus/SOURCES.md` registry pointer);
  QUALITY.md to S (tier pointer, SOURCES-CONTRACT rule 3). Unassigned stat paths (integration helpers,
  run-validation.py, claims-addendum, lessons/README.md) belong to no unit and stay at base bytes in
  every counterfactual.
- Trees: C `8c78e6b` (L1-pinned), S `d91c632` (the adjudicated spot-check state; 47 anchored rows
  S001–S047, matching L1's export range; the receipt measured 8c78e6b but the REJECTED-HONEST-STOP
  adjudicated d91c632, so calibration freezes the adjudicated registry), Ca `8c78e6b` (byte-identical
  to d91c632 for all three Ca lands — none appear in the 8c78e6b→d91c632 diff).
- S export `\bS0(3[1-9]|4[0-7])\b`: novel at base under `\b` (`git grep -E` at c42d675: rc=1, no
  hits; earlier apparent hits were an artifact of my first grep omitting `\b`). r50 C export
  `\bS0(4[89]|[5-9]\d)\b`: novel at 4ad2683 (rc=1). Entry cites S031–S042 (12 ids, uniq -c at 8c78e6b);
  the assignment's guessed "S031–S043" was wrong in both directions — registry defines S001–S043 at
  8c78e6b / S001–S047 at d91c632, entry cites S031–S042.
- Acceptance legs verified against frozen bytes: entry 205 lines / 1 H1 / 1 `- topic:`; 47 unique
  anchored registry rows at d91c632; anchored `revision: 2.0` count 1 in README + tool exists.

## Expected findings on the r49 fixture (exit 1, encoded in `expected_findings`)
1. `SEPARABILITY_DEPENDENCY C->Ca via land path tools/check-readme-revisions.py x1` (README line 18 records the control)
2. `SEPARABILITY_DEPENDENCY C->S via export \bS0(3[1-9]|4[0-7])\b matched S031…S042` — the adjudicated r49 dependency, export leg
3. `SEPARABILITY_DEPENDENCY C->S via land path corpus/SOURCES.md x2` (entry shelf note + sources line) — same dependency, path leg
4. `SEPARABILITY_DEPENDENCY S->C via land path corpus/knowledge/culture-material/hunting-foraging-subsistence.md x12` (SOURCES used-by)
5. `SEPARABILITY_DEPENDENCY S->Ca via land path tools/check-readme-revisions.py x9` (lesson)
6. `SEPARABILITY_OVERLAP C/Ca corpus/README.md`
Ca->C and Ca->S verified ABSENT (Ca-evidence.md: 0 entry-path, 0 SOURCES, 0 S-id, 1 self-tool hit;
README full entry path count 0). All six computed by an independent reference matcher implementing
the L1 semantics, not hand-asserted.

## r50 manifest
Base 4ad2683; all trees `WORKTREE` (= read the lane filesystem at runtime; placeholder until the
integrator fills real trees at landing — until then, unlanded files contribute zero scanned bytes).
C lands entry + corpus/README.md + corpus/SOURCES.md (new rows are C's sources), export
`\bS0(4[89]|[5-9]\d)\b`; O unchanged; Ca lands checker + `reports/round-50/separability/*.json` +
corpus/QUALITY.md; REC unit role "record" (lesson, lessons index, LOG, SCORECARD, r50 runner,
claims.json) never scanned as depender. `expected_findings: []` per L1.

## Conditions on "expected r50 findings: none" (risks for L1)
1. Instrument exemption required: r50-manifest.json self-lists every unit's lands; scanned as a Ca
   byte it yields `Ca->C via pastoralism path` and `Ca->O via reports/round-50/jj-colocation-probe.py`
   (both absent at base). The checker must exempt the separability manifests (calibration instruments)
   from byte-scanning, or these two findings fire at landing. r49-fixture.json is clean either way
   (all paths it quotes exist at 4ad2683 → muted).
2. WIP observation (L1's in-flight lane bytes; production worktree is dirty: M QUALITY/README/SOURCES/
   revisions-tool, untracked entry/lesson/round-50 dir/checker): entry line 7 names the full
   `corpus/lessons/round-50.md` → would fire `C->REC` at landing; the r49 precedent (SOURCES line 8)
   uses the bare form `` `lessons/round-49.md` `` which stays clean. Bare form, or accept the finding.
3. Transient `S048` token was seen in Ca-candidate bytes during matcher runs (in-flight checker/QUALITY
   edits); current QUALITY has 0 S04x tokens. Anything citing "S048–S069" as tokens in Ca/O/REC bytes
   will fire `->C` via C's export.
4. Contract sharp edges for the checker: report export matches via finditer/group(0) (findall with a
   capturing group returns group text: "31" not "S031"); land-path hits are exact full-path substrings
   (bare `lessons/round-50.md` does NOT match land `corpus/lessons/round-50.md`).

## Unrun checks
Did not execute ExecSepTool-4's checker (in flight); fixture validity = independent reference matcher
+ receipt digest cross-check + JSON parse. Patch intentionally not applied to production.
