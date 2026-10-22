# ExecSeparabilityProbe — round 52 separability probe

Seat: `KotodamaR52.ExecSeparabilityProbe` (leaf executor). Date: 2026-10-22.

## Assigned item

Probe `tools/check-claim-separability.py` against the round-52 separability manifest with
synthetic stand-ins, for four cases (clean, D→C by S-id, C→REC by lesson path, D→C by land
path); also run `reports/round-52/claims-agree.py`; report outputs, exit codes and blind
spots. Nothing in the lane was changed except this report.

## Sandbox and stand-ins

Clone: `git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin
/fast/scratch/hyaku/kotodama-r52/ExecSeparabilityProbe`, worktree detached at
`d9f73c80744bb5e483f6d9d39069fe064dc5dffe` (the round-52 declaration commit). The
manifest base stays `147cfde85eb13256438c1ed04d92e8d2ad09b76e`. Stand-ins, sandbox only:

| Path | Content |
|---|---|
| `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` | new minimal C entry; `- topic:` block; cites S134, S135 only |
| `corpus/SOURCES.md:163-164` | S134 and S135 rows (11 columns), `used-by` = `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` |
| `corpus/README.md:231` | `## linguistics/ (26)` → `(27)` |
| `corpus/README.md:254` | index row for the new entry |
| `corpus/README.md:603` | `Total knowledge entries: 227.` → `228.` |
| `corpus/README.md:607` | footer `(total 227 files; directory totals 26/26/28/29/24/94)` → `(total 228 files; directory totals 27/26/28/29/24/94)` |
| `corpus/knowledge/linguistics/sign-languages-manual-modality.md` | D's edit taken verbatim from the L1's landed commit `dea5ece` (S094 lines 5 → 0; cites S095, S096, S097) |
| `corpus/lessons/round-52.md` | stub, so the REC unit's declared land exists in the worktree |

Commands run inside the sandbox:
`python3 -B tools/check-claim-separability.py reports/round-52/separability-manifest.json`
and `python3 -B reports/round-52/claims-agree.py`.

## Runs

### (a) Clean case — expect exit 0

```
SEPARABILITY: 0 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2
EXIT=0
```

Both acceptance legs pass on base + own lands: D's `S094_lines=0` and the no-S134+ grep;
C's `knowledge_files=228`, the README sweep footer and the S-id / used-by audit. Stand-in
state after the run: `S094_lines=0`, `grep -cE '\bS(13[4-9]|1[4-9][0-9]|[2-9][0-9][0-9])\b'
` → 0 (rc 1), `find corpus/knowledge -name '*.md' | wc -l` → 228.

### (b) D's edit also cites S134 — expect a D→C finding

Patched `corpus/knowledge/linguistics/sign-languages-manual-modality.md:87` (the Handshape
row) to read `… (S097, S134)`.

```
SEPARABILITY_DEPENDENCY D-><base> via acceptance ['sh', '-c', 'n=$(awk \'/S094/{n++} END{print n+0}\' corpus/knowledge/linguistics/sign-languages-manual-modality.md); echo S094_lines=$n; test "$n" -eq 0 && ... fails on base+D.lands (rc=1) and no declared unit's lands repairs it
SEPARABILITY_DEPENDENCY D->C via export '\\bS(13[4-9]|1[4-9][0-9]|[2-9][0-9][0-9])\\b' matched corpus/knowledge/linguistics/sign-languages-manual-modality.md:87
SEPARABILITY: 2 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=4
EXIT=1
```

The D→C export finding is present, as expected. Note the second line: because C's lands
cannot repair D's own file, the dynamic leg attributes D's failing acceptance to
`<base>`, not to C. The two legs therefore disagree on the direction of the same defect.

### (c) C's entry names corpus/lessons/round-52.md (REC land created) — report what the checker does

Patched `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:14` to add the
line `Round note pointer: corpus/lessons/round-52.md`.

```
SEPARABILITY_DEPENDENCY C->REC via land path 'corpus/lessons/round-52.md' named at corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:14
SEPARABILITY: 1 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2
EXIT=1
```

The checker does fire: because `corpus/lessons/round-52.md` is absent at base and is a
declared land of the REC unit, a claim naming it is a dependency on the record unit. REC is
never scanned as a depender (records are excluded), so the finding is one-way C→REC.

### (d) D's edit names C's entry path — expect a finding

Patched `corpus/knowledge/linguistics/sign-languages-manual-modality.md:83` to add
`See also corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`.

```
SEPARABILITY_DEPENDENCY D->C via land path 'corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md' named at corpus/knowledge/linguistics/sign-languages-manual-modality.md:83
SEPARABILITY: 1 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2
EXIT=1
```

### Agreement command

```
AGREE claims=['C', 'D']
EXIT=0
```

Same result in the sandbox and when run read-only in the lane
(`/home/vgpnk/Projects/shokunin/kotodama-shokunin`, exit 0).

## Extra probes (blind-spot measurement)

| # | Mutation | Result |
|---|---|---|
| e | C's entry names D's land `corpus/knowledge/linguistics/sign-languages-manual-modality.md` (that path resolves at base) | `SEPARABILITY: 0 findings`, exit 0 — no finding |
| f | README index row topic paraphrased | `python3 -B reports/round-28/readme/sweep.py` → `topic_mismatch 1`, sweep exit 1; separability → `SEPARABILITY: 0 findings`, exit 0 |
| g | README index row for the new entry deleted | sweep → `missing_from_index 1`, sweep exit 1; separability → `SEPARABILITY: 0 findings`, exit 0 |
| h | C's entry cites S071 | `SEPARABILITY_DEPENDENCY C-><base> via acceptance … rc=1 and no declared unit's lands repairs it`, exit 1 — the acceptance does bite |
| i | REC's land `corpus/lessons/round-52.md` absent from the worktree | `SEPARABILITY_INPUT_ERROR unit REC lands 'corpus/lessons/round-52.md', which is absent from the worktree under '/fast/scratch/…'`, exit 2 |

## Blind spots

1. **C's README leg is weaker than it looks.** The acceptance runs
   `python3 -B reports/round-28/readme/sweep.py | grep -q '"total": 228'`. The pipe drops
   the sweep's exit status, and the grep matches the *declared* footer's `"total": 228`
   string, which the sweep prints even when it reports findings. Probes f and g: the sweep
   exits 1 (topic mismatch; missing index row) and the separability control still returns
   0 findings / exit 0. So a wrong index topic or a missing index row for the new entry
   passes C's acceptance. Hardening: `set -o pipefail`, or
   `python3 … > out || exit 1; grep -q '"total": 228' out`, or gate on the sweep's `ok`
   field in `--json` output.
2. **Only land paths absent at base count as dependencies.** Probe e: C naming D's sign
   entry produces no finding, because that path already resolves at base. `claims.json`'s
   `must_not_cite` for C ("the sign-language entry lines changed by D") is therefore not
   enforced by this control; it needs a review leg, not the separability leg.
3. **The static leg reads only added lines** — lines of a land that are not present in the
   base version of that land. A dependency carried by an unchanged line, or by re-using a
   base line verbatim, is invisible. Edits that only reword are still caught (the reworded
   line is new), but a dependency that already existed at base is out of scope by design.
4. **The dynamic leg credits another unit only when that unit's lands repair the failure.**
   In case (b) the export leg says D→C while the acceptance leg says D→`<base>`; a reader
   skimming the acceptance line could conclude C is irrelevant. The export leg is the
   stronger signal there.
5. **The checker only knows declared lands.** A cross-claim reference to a path no unit
   declares (another lane's file, a future lesson file, a path outside the corpus) is
   invisible. Only `must_not_cite` targets that happen to be declared lands are caught.
6. **WORKTREE units read the live working tree.** Good for untracked files, but every
   declared land must exist or the whole control aborts (probe i, exit 2). At the
   declaration commit `corpus/lessons/round-52.md` does not exist, so the control cannot
   run until the round's record files are written. The L1 should create the record lands
   before running this command, or expect exit 2 rather than a verdict.
7. **Export novelty is checked against the unit's own lands at base.** If a base file
   already mentioned an S134+ id, the manifest would be rejected with exit 2 ("export is
   not novel") instead of the claim being failed. At this base neither
   `corpus/SOURCES.md` nor `corpus/README.md` carries an S134+ id (case a ran clean), so
   the fragility did not fire here.
8. **The git-free counterfactual has no `.git`.** Any acceptance that needs git would fail
   with a bare `rc=`; the `needs_git` flag exists but no round-52 unit uses it.

## Result

The control behaves as the manifest intends for (a)–(d): exit 0 with no findings on the
clean case, and one or more findings with exit 1 on each cross-wiring, with the expected
D→C direction in cases (b) and (d) and C→REC in case (c). `claims-agree.py` reports
`AGREE claims=['C', 'D']`, exit 0. The material blind spot for this round is blind spot 1:
C's README acceptance does not enforce the README index, only the declared footer total.

## Unrun checks

- `reports/round-52/dry-run.py` (the round's own receipt) was not run — not in this seat's
  assignment.
- `tools/check-source-access.py`, the QUALITY criterion 10 pass, and the full-corpus
  validation were not run; they are outside this seat's scope.
- No lane file was modified apart from this report; no jj command was run in the lane; no
  git mutation was run in the lane.

## Tools

No installs or upgrades: no `pacman`, no `uv tool`, no `npm`. Everything used the preinstalled
`git`, `python3` (stdlib only), `awk`, `grep`, `find`, `sed`.

## Evidence index

- `tools/check-claim-separability.py:616-670` (static, overlap and acceptance legs),
  `:366-369` (`name_paths()` — only base-absent lands count),
  `:469-498` (WORKTREE loading and export novelty), `:712-722` (`report()` and exit codes),
  `:1191-1230` (`main()` argument handling).
- `reports/round-52/separability-manifest.json` (base `147cfde`, units D, C, REC).
- `reports/round-52/claims-agree.py:12-35` (the AGREE check).
- `reports/round-28/readme/sweep.py:119-213` (`sweep()` — topic mismatch, missing rows,
  footer findings), `:215-232` (`render()`), `:411-429` (`main()` returns 1 when
  `inv["ok"]` is false).
- Sandbox evidence lines: `corpus/knowledge/linguistics/sign-languages-manual-modality.md:87`
  (case b hit), `:83` (case d hit); `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:14`
  (case c hit); `corpus/SOURCES.md:163-164` (S134, S135 rows).
