# ExecSeparabilityProbe — round 51, attempt 3

## Assigned item and axes

Test the own-round manifest in an isolated base-pinned sandbox with synthetic D/C landings, then exercise the two literal dependency controls and the known relative-path blind spot. Axes: manifest compatibility, counterfactual ownership, dependency sensitivity, and lane isolation.

**Result:** clean case exited 0; literal D→C and C→REC cases each produced exactly the requested finding and exited 1; relative C→REC spelling produced no finding and exited 0. The blind spot is reproduced, not repaired. This is author-lane setup evidence, not admission of the final entries.

## Isolation and fixtures

Sandbox: `/fast/scratch/hyaku/kotodama-r51a3/ExecSeparabilityProbe`.

Cloned the lane with `git clone -q --shared`, then checked out the requested base in the sandbox. Preparation output:

```text
sandbox HEAD: bff83ba65bf9559af4d7567e81703059667a0005
lane HEAD: 1f97472aefdd40c150cddcfb7d5d7acff12b6a2b
```

Copied these four authorized, uncommitted files into the sandbox's `reports/round-51/`: `separability-manifest.json`, `claims-agree.py`, `claims.json`, `boundary-count.py`. Used the checker already present at the pinned base. Neither checker nor manifest nor acceptance commands were changed.

Sandbox-only synthetic changes:

- `corpus/knowledge/linguistics/sign-languages-manual-modality.md`: a six-line minimal entry, with topic `synthetic manual-modality fixture for separability only` and source citation `S071 (synthetic; not research evidence)`.
- `corpus/SOURCES.md:100`: matching 11-column S071 row, explicitly labelled synthetic and used by the entry. No external source was opened or claimed as research evidence.
- `corpus/README.md`: linguistics heading 25→26; matching topic row at line 240; total 226→227; footer vector `25/26/28/29/24/94`→`26/26/28/29/24/94`.
- `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:42-45`: four additional section-2 rows, preserving the original 11. Synthetic neighbours were `cartography-and-mapmaking.md:3`, `timekeeping-instruments.md:3`, `bathing-and-body-hygiene.md:3`, and `furniture-interior-lexicon.md:3`. Ownership cells were respectively mapmaking, timekeeping instruments, bathing institution, and furniture/seating regime. These are counter fixtures, not proposed production boundary rows.
- `corpus/lessons/round-51.md`: a three-line synthetic record, required because the REC unit lands this new path. The other pre-existing REC lands were left at base bytes.

Lane anchors re-read for those synthetic neighbour labels: `corpus/knowledge/culture-material/cartography-and-mapmaking.md:3`, `corpus/knowledge/culture-material/timekeeping-instruments.md:3`, `corpus/knowledge/culture-material/bathing-and-body-hygiene.md:3`, `corpus/knowledge/culture-material/furniture-interior-lexicon.md:3`.

No commits, installs, checker fixes, global changes, or lane implementation edits. Only this advisory report was written in the lane. No LSP tool is exposed in this seat; no symbol refactor was needed.

## Baseline and declaration agreement

Command, before adding the four D rows:

```sh
python3 -B reports/round-51/boundary-count.py && python3 -B reports/round-51/claims-agree.py
```

Complete output, exit 0:

```text
rows=11 resolved=11 distinct=11
AGREE claims=['C', 'D']
```

The manifest gives D its own boundary counter and C its new entry, README, and SOURCES; REC holds the lesson and administrative records (`reports/round-51/separability-manifest.json:6-17,20-35,38-51`). The agreement check compares claim IDs, lands, and base (`reports/round-51/claims-agree.py:18-29`).

## Four requested executions

Each case ran this exact command from the sandbox root, followed by a shell status print; the `exit=` line is the checker's status, not the wrapper's status:

```sh
python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json; printf 'exit=%s\n' "$?"
```

Output below includes both streams as displayed by the tool. Each case ran once.

### (a) Clean synthetic landing

```text
SEPARABILITY: 0 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2
exit=0
```

This is a compatible own-round manifest, not an input-error result. The two acceptance runs passed on each claim's own overlay: the checker first calls `run(unit.overlays())` and returns immediately on success (`tools/check-claim-separability.py:647-651`), against the materialized manifest base (`tools/check-claim-separability.py:685-695`). Thus D's 15/resolved/distinct acceptance passed without C, and C's 227-entry/index/source-ID acceptance passed without D or REC. Synthetic fixture success does not validate production entry content.

### (b) D new row names C's entry path

Changed only the boundary cell of the first synthetic row, at pastoralism line 42, to append `; names corpus/knowledge/linguistics/sign-languages-manual-modality.md`. Kept its existing-neighbour anchor unchanged, isolating the static path control from the numeric counter.

```text
SEPARABILITY_DEPENDENCY D->C via land path 'corpus/knowledge/linguistics/sign-languages-manual-modality.md' named at corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:42
SEPARABILITY: 1 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2
exit=1
```

### (c) C names round-51 record literally

Restored the clean D row first. Appended a blank line and then this line to the C entry at line 8:

```text
Synthetic dependency: corpus/lessons/round-51.md.
```

Complete output:

```text
SEPARABILITY_DEPENDENCY C->REC via land path 'corpus/lessons/round-51.md' named at corpus/knowledge/linguistics/sign-languages-manual-modality.md:8
SEPARABILITY: 1 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2
exit=1
```

### (d) C names the same record relatively

Replaced only C entry line 8 with:

```text
Synthetic dependency: ../../lessons/round-51.md.
```

Complete output:

```text
SEPARABILITY: 0 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2
exit=0
```

The spelling points from the entry's directory to `corpus/lessons/round-51.md`, but is not detected. The static leg uses a regex of the declared literal repository path, without relative-path resolution (`tools/check-claim-separability.py:602-604,629-633`). The acceptance leg checks counts, index, and source-ID linkage, not consumption of record prose. Final sandbox state retains case (d), with D restored clean. Do not mistake its green result for absence of a relative record reference.

## Retained input hashes

Command: `sha256sum reports/round-51/separability-manifest.json reports/round-51/claims-agree.py reports/round-51/claims.json reports/round-51/boundary-count.py tools/check-claim-separability.py`.

Complete output:

```text
8eabed4173e45638289f401be123000e239bf0119d50299f25433efc19610495  reports/round-51/separability-manifest.json
abad0376323780afdd00c84261ec75b625e7436ce0a7ff707623ade25b8d07fd  reports/round-51/claims-agree.py
d991616c5a218c450f5013f274c47bf9ecb9941fd063edba10115e81d6fb763b  reports/round-51/claims.json
fb1d5c89d2ed3ea32a699692901fa24fed28020f5a930fc7198e2b62f1b14cc2  reports/round-51/boundary-count.py
5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5  tools/check-claim-separability.py
```

## Risks, blockers, and unrun checks

- Known risk reproduced: literal path matching misses an equivalent relative C→REC reference. No checker change was requested or made.
- These deliberately minimal fixtures establish control behavior and overlay ownership, not factual quality, source provenance, final boundary semantics, or entry-contract compliance.
- No blockers. No external source opening, tool installation, build, lint, formatter, broad test battery, or final lane integration gate ran.
- Parent should run declaration agreement, the real final-tree boundary count, index sweep, and separability check after integration; manually inspect C's relative record references rather than relying on a green checker alone.
