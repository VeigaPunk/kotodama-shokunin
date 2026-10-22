# MutateSeparability — round 51, attempt 3, falsify wave

Seat: `KotodamaR51a3.MutateSeparability` (mutation tester). Date: 2026-10-22.

## Item attacked

The round's own separability evidence: the manifest `reports/round-51/separability-manifest.json`,
the checker `tools/check-claim-separability.py`, and the run recorded as the declaration's
`separability_command` (`python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json`).
The claim under attack is the one the evidence is cited for:

- `reports/round-51/claims.json:27` — claim D must not cite `corpus/knowledge/linguistics/sign-languages-manual-modality.md` or any S-id from S071 upward.
- `reports/round-51/claims.json:44` — claim C must not cite `corpus/lessons/round-51.md` or `reports/round-51/boundary-count.py`; the round's falsify context adds "in any spelling".
- `corpus/lessons/round-51.md:16` and `:108` — the lane records that "the relative-path blind spot is retained, not repaired".

My question is narrow: **does the landed detector actually fail when a forbidden citation appears?**
I planted one forbidden citation at a time in a private clone and ran the same detector on pristine,
mutated and restored bytes.

## Bounds and isolation

- Sandbox: `/fast/scratch/hyaku/kotodama-r51a3-falsify/MutateSeparability`, created with
  `git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin`, checked out at tip `9feb69e`.
- `realpath` of the sandbox: `/fast/scratch/hyaku/kotodama-r51a3-falsify/MutateSeparability` (a real
  directory, no symbolic link into the lane). Every write went there; `realpath` was printed before each run.
- The lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin` was read only: `git log`, `git status`,
  `git cat-file`, `git show`. No git write command, no jj command, was run in the lane. The only file
  I wrote in the lane is this report.
- Harness and results (kept for reproduction, outside the lane):
  `.mutate-harness.py`, `.mutate-results.json`,
  `.mutate-results-reports_round_51_separability_manifest_fixed_json.json`,
  and the proposed fixed manifest `reports/round-51/separability-manifest.fixed.json` inside the sandbox only.
- No tool was installed. No pacman, uv, cargo or npm transaction was run. The detector needs only
  `python3` and `git`, both already present (`python3` reports `Python 3.14.8`, `git --version` reports
  `git version 2.56.0`); no version change was made.

## Baseline (pristine bytes at tip)

```sh
cd /fast/scratch/hyaku/kotodama-r51a3-falsify/MutateSeparability
python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json
```

```text
SEPARABILITY: 0 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2
exit=0
```

The other declared legs of the round are also green on these bytes, so no mutant below is masked by a
broken tree:

```sh
python3 -B reports/round-51/boundary-count.py      # rows=15 resolved=15 distinct=15   exit=0
find corpus/knowledge -name '*.md' | wc -l           # 227
python3 -B reports/round-28/readme/sweep.py >/dev/null; echo $?   # exit=0
```

The sweep prints `rows 227 files 227`, `linguistics 26`, `totals_line 227 totals_ok True`,
`footer {"total": 227, "dir_totals": [26, 26, 28, 29, 24, 94]}`, `footer_ok True`.

## Mutation matrix

One mutation at a time. Every run is the same detector command. `killed` = the detector exits 1 with a
`SEPARABILITY_DEPENDENCY` finding; `survived` = the detector exits 0 with no finding.

| id | mutation (file and exact text) | exit | finding | verdict |
|---|---|---|---|---|
| M1 | D boundary row (line 47) names the C entry by full path | 1 | `SEPARABILITY_DEPENDENCY D->C via land path 'corpus/knowledge/linguistics/sign-languages-manual-modality.md' named at corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:47` | killed |
| M2 | D boundary row (line 45) cites `S071` | 1 | `SEPARABILITY_DEPENDENCY D->C via export '\bS(07[1-9]|0[89]\d|[1-9]\d\d)\b' matched corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:45` | killed |
| M3 | C entry names `corpus/lessons/round-51.md` | 1 | `SEPARABILITY_DEPENDENCY C->REC via land path 'corpus/lessons/round-51.md' named at corpus/knowledge/linguistics/sign-languages-manual-modality.md:219` | killed |
| M4 | C entry names `lessons/round-51.md` (relative) | 0 | none | **survived** |
| M5 | C entry names `reports/round-51/boundary-count.py` | 1 | `SEPARABILITY_DEPENDENCY C->D via land path 'reports/round-51/boundary-count.py' named at corpus/knowledge/linguistics/sign-languages-manual-modality.md:219` | killed |
| M6 | README (C's land) gains a line naming the D entry path and its new fact | 0 | none | **survived** |
| M7 | README (C's land) gains a line naming `reports/round-51/boundary-count.py` | 1 | `SEPARABILITY_DEPENDENCY C->D via land path 'reports/round-51/boundary-count.py' named at corpus/README.md:14` | killed |
| M8 | D boundary row (line 47) names the C entry by basename only | 0 | none | **survived** |
| M9 | C entry names the D entry path (mirror of M1, other direction) | 0 | none | **survived** |
| M10 | D boundary row (line 45) cites the two-digit spelling `S71` | 0 | none | **survived** |
| M11 | D boundary row (line 45) cites the hyphenated spelling `S-071` | 0 | none | **survived** |
| M12 | C entry names `../lessons/round-51.md` | 0 | none | **survived** |

M1, M2, M3, M5, M7 are the assigned six (M1 = C entry path in a D row, M2 = `S071` in a D row,
M3 = `corpus/lessons/round-51.md` in the C entry, M4 = `lessons/round-51.md` in the C entry,
M5 = `reports/round-51/boundary-count.py` in the C entry, M6 = README line naming the D entry).
M7 to M12 are extra probes I added to locate the edges of the blind spot.

### Exact mutant text (the six assigned)

- M1, D entry line 47, third cell:
  `... not the counting system |` → `... not the counting system; counting by hand is owned by \`corpus/knowledge/linguistics/sign-languages-manual-modality.md\` |`
- M2, D entry line 45, third cell:
  `... no second symbol grammar |` → `... no second symbol grammar; manual counting signs are catalogued at S071 |`
- M3, C entry, new line after `## 14. Recheck`:
  ``Round-51 gate record and located quotes: `corpus/lessons/round-51.md`.``
- M4, same place: ``Round-51 gate record and located quotes: `lessons/round-51.md`.``
- M5, same place: ``Round-51 boundary counter for the neighbour table: `reports/round-51/boundary-count.py`.``
- M6, `corpus/README.md`, new line after the revision 2.8 block:
  ``This round's other landing, `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`, grew its section-2 one-owner boundary table from 11 to 15 rows.``

Every mutated run kept `acceptance_runs=2` in the stderr note, so the acceptance legs never fired: each
mutant was killed or spared by the static naming rule alone, not by an acceptance failure.

## Why each mutant lived or died

The checker has three legs. The one that matters here is the static leg
(`tools/check-claim-separability.py:616-635`), which scans the **added lines** of each claim's landed
files for two things:

1. the other unit's `exports` regexes (`reports/round-51/separability-manifest.json:12, 28, 51`);
2. the other unit's **land paths that are absent at base** (`tools/check-claim-separability.py:366-368`,
   `name_paths`, computed at `:484`).

The path match itself is exact-string: `_name_re` (`:602-604`) builds
`(?<![\w.\-])<repo-relative path>(?![\w\-]|\.\w)`. Direct probe of that function:

```text
'corpus/knowledge/linguistics/sign-languages-manual-modality.md' vs 'sign-languages-manual-modality.md' -> False
'corpus/knowledge/linguistics/sign-languages-manual-modality.md' vs 'corpus/knowledge/linguistics/sign-languages-manual-modality.md' -> True
'corpus/lessons/round-51.md' vs 'lessons/round-51.md' -> False
'corpus/lessons/round-51.md' vs 'corpus/lessons/round-51.md' -> True
'corpus/lessons/round-51.md' vs 'round-51.md' -> False
'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md' vs 'pastoralism-animal-husbandry.md' -> False
```

So the detector sees a citation only when the line spells the path exactly as the manifest spells it,
and only when the target path did not exist at base `bff83ba`. Both conditions hold for M1, M2, M3, M5
and M7, and both fail for M4, M6, M8, M9, M10, M11 and M12.

## Findings

### F1 — The forbidden-citation rule is spelling-bound (severity: high)

`tools/check-claim-separability.py:602-604` and `:366-368`. A claim that names a forbidden file in any
spelling other than the manifest's exact repo-relative path exits 0 with no finding.

- Evidence: M4 (`lessons/round-51.md`), M8 (`sign-languages-manual-modality.md`), M12 (`../lessons/round-51.md`) all survived with exit 0.
- Contract at risk: `reports/round-51/claims.json:44` plus the round context "in any spelling"; and claim D's falsifier "a new row names the round's new claim-C entry" (`reports/round-51/claims.json:24`).
- Why it matters in practice: the corpus's own anchor style is basename plus line, for example `numerals-and-measures.md:101` at `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:47`. M8 is therefore the spelling a real author is most likely to write, and it is the one the detector cannot see.
- Smallest fix, manifest only, no tool change: add alias regexes to the manifest `exports` lists, which the checker already supports. For the REC unit:
  `"exports": ["(?:^|[^\\w./-])(?:\\.\\./)?(?:corpus/)?lessons/round-51\\.md"]`;
  for the C unit:
  `"exports": ["\\bS(07[1-9]|0[89]\\d|[1-9]\\d\\d)\\b", "\\bS-?(?:0?7[1-9]|0[89]\\d|[1-9]\\d\\d)\\b", "(?:^|[^\\w./-])(?:corpus/knowledge/linguistics/)?sign-languages-manual-modality\\.md"]`.
  I built exactly this manifest in the sandbox as `reports/round-51/separability-manifest.fixed.json` and re-ran the whole matrix against it: the pristine tree still gives `SEPARABILITY: 0 findings`, exit 0, and all twelve mutants are then killed. No false positive appears (the C entry never mentions the D entry; the D entry's base bytes never contain its own basename, so the export stays novel per the checker's own rule at `:491-502`).

### F2 — The S-id export only matches the canonical three-digit spelling (severity: medium)

`reports/round-51/separability-manifest.json:28` uses `\bS(07[1-9]|0[89]\d|[1-9]\d\d)\b`. `S71` (M10)
and `S-071` (M11) both survive with exit 0, while `reports/round-51/claims.json:27` forbids "any S-id
from S071 upward". Smallest fix: add `"\\bS-?(?:0?7[1-9]|0[89]\\d|[1-9]\\d\\d)\\b"` to the C unit's
`exports`. Verified in the sandbox as part of F1: M10 and M11 are killed and the pristine tree stays at 0 findings.

### F3 — A citation of another claim's *modified* file is invisible in both directions (severity: medium)

`tools/check-claim-separability.py:366-368` counts only land paths **absent at base**. D's entry,
`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`, was already present at base
`bff83ba`, so it is excluded from the check; the same holds for C's `corpus/README.md`.

- M6: `corpus/README.md` is C's land. A line there asserting D's new fact ("grew its section-2 one-owner boundary table from 11 to 15 rows") produced no finding. If claim D were dropped, that README sentence would be false and the round would still read clean.
- M9: the C entry naming D's entry path produced no finding.
- The asymmetry is the point: D naming C is caught (M1) only because C's entry is a **new** path. The same citation in the other direction, or any citation of a file the other claim merely edited, is invisible.
- Smallest fix, manifest only: give the D unit an export that names its own entry, for example
  `"exports": ["(?:^|[^\\w./-])(?:corpus/knowledge/culture-material/)?pastoralism-animal-husbandry\\.md"]`.
  Verified in the sandbox: M6 and M9 are then killed and the pristine tree stays at 0 findings.

### F4 — The bare spelling `round-51.md` cannot be caught safely (severity: low, residual)

`.ufo/waves/round-51/build/CriticClaimD.md:124` lists `round-51.md` and `lessons/round-51.md` as the
spellings to watch. The F1 alias catches the directory-bearing spellings. A bare `round-51.md` would
need a pattern that also matches `reports/round-51/...` paths, so it needs a human eye or a dedicated
check, not a regex. Flagged, not repaired.

### No live violation in the landed bytes

The corpus itself is clean, so none of the findings above needs a corpus edit. Measured on the tip
bytes with the sandbox clone:

```text
grep -n "sign-languages-manual-modality" corpus/knowledge/culture-material/pastoralism-animal-husbandry.md   -> no match
grep -oE '\bS(07[1-9]|0[89][0-9]|[1-9][0-9][0-9])\b' corpus/knowledge/culture-material/pastoralism-animal-husbandry.md -> no match
grep -n "round-51" corpus/knowledge/linguistics/sign-languages-manual-modality.md                            -> no match
grep -n "boundary-count" corpus/knowledge/linguistics/sign-languages-manual-modality.md                      -> no match
```

This agrees with `corpus/lessons/round-51.md:108` ("the C entry names no lesson path in any spelling")
and with the build-wave probe `.ufo/waves/round-51/build/ExecSeparabilityProbe.md`, which reproduced the
relative-path blind spot with synthetic fixtures. My contribution is that the blind spot is now measured
on the **real landed entries** rather than on fixtures, and that three further routes (basename citation,
base-present-file citation, non-canonical S-id spelling) were never measured at all.

## Survivors

Seven of twelve mutants exited 0 with no finding: **M4, M6, M8, M9, M10, M11, M12**.
The five canonical spellings (M1, M2, M3, M5, M7) were all killed, so the detector is not inert.

## Restoration evidence

Every mutant was restored byte-exactly and the detector was re-run on the restored bytes. For all twelve
mutants: `bytes_restored=True`, the post-restore sha256 equals the pre-mutation sha256, and the
re-run printed `SEPARABILITY: 0 findings` with exit 0, identical to the baseline.

| file | sha256 before | sha256 mutated | sha256 after restore |
|---|---|---|---|
| `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` | `5c2e09d04652920ae5c8d2f64c175b871b5b98b3cf7a0327ccfe063390c019d0` | `50a5e9fb36c76c277d9eaf683326ca34a482bc68797a89ec9f8cc74e076b63f5` (M1), `2d974d3dfde40a79e26db371b538d2ac5fecfbd141a31a4a7c0b06b11abfaf2b` (M2), `8f3a2af17fb50d0473878f768005f8b2e0c6337b40817c0543a30288b072661d` (M8) | `5c2e09d04652920ae5c8d2f64c175b871b5b98b3cf7a0327ccfe063390c019d0` |
| `corpus/knowledge/linguistics/sign-languages-manual-modality.md` | `1a71ae2dcf2ecacbbd23884b5b4894aaf18879dbde23e9ed32067f018c52b1f7` | `88f6e29e92f654d499b1d1f12aa9e9401d635315dd484d643cb84d8753bb9570` (M3), `15711412b50c3cca5e20d1df86558e3439c9e9e9f9988640916e176a0b118d12` (M4), `e5647d7e3566f3a3a9376f1f9bca4fa43300f2565ef6a99008674af61d2c2212` (M5), `5b641cb6a9e72475ca00dcf834ac4e2b8ff5b6c9a5a2806287969d58e03c922b` (M9) | `1a71ae2dcf2ecacbbd23884b5b4894aaf18879dbde23e9ed32067f018c52b1f7` |
| `corpus/README.md` | `f425c6ffd378af55a4a35fe851a2ceb5dd3a3d17fd9bca0c4b45864be9436ac0` | `b793e45b53e60e2bef464d8053ac7d1f8a9b4d6195d2962c0f715d3a3d776e92` (M6), `fdccf5bbb4c14e11d0026a35475b3cfde60899f06ce201e7be32bd47bc5697a1` (M7) | `f425c6ffd378af55a4a35fe851a2ceb5dd3a3d17fd9bca0c4b45864be9436ac0` |

Final state of the sandbox: `git diff --stat` is empty and `git status --porcelain` shows only the four
untracked helper files I created (harness, two results files, proposed fixed manifest). The lane's own
tip is still `9feb69e` and the lane's `git status` shows only the untracked `.ufo/waves/round-51/` wave
folder.

## Sources opened

None. This seat opened no external URL and asserted no source row. The round's source rows
(`corpus/SOURCES.md` S071 to S124) were read as files only, to locate the export patterns; no URL was
fetched, so no access date, quote or tier was re-verified here. That work belongs to the source-review
seats.

## Unrun checks

- `python3 -B tools/check-claim-separability.py --selftest` was not run (out of scope for this seat; the
  checker is unmodified by me).
- `reports/round-51/claims-agree.py` was not run by this seat (another seat owns the manifest and
  claims agreement); the manifest and `claims.json` were read and compared by hand only.
- The round-50 spot-check instruments and `reports/round-50/**` were not exercised.
- No source URL was opened, so no tier or scope re-verification was done.

## Verdict

**HOLDS-WITH-FIXES** for the round's separability evidence.

What holds: the landed tree complies with every stated forbidden-citation constraint (no C-entry mention
and no S-id from S071 in D's entry; no lesson path and no counter path in C's entry), the manifest's
declared acceptance legs are green (D counter `rows=15 resolved=15 distinct=15`; C count 227; sweep exit 0
with footer total 227 and linguistics 26), and the detector kills all five canonical forms of the four
forbidden citations (M1, M2, M3, M5, M7).

What does not hold: the detector cannot see a forbidden citation in any other spelling (M4, M8, M12), in a
non-canonical S-id spelling (M10, M11), or when the cited file is one the other claim merely **edited**
rather than created (M6, M9). The round's own contract asks for "any spelling"
(`reports/round-51/claims.json:44`), and the lesson records the relative-path part of this as retained
rather than repaired (`corpus/lessons/round-51.md:16`, `:108`). The fix is manifest-only, needs no tool
change, and I have shown it works in the sandbox: with the alias exports added, the pristine tree still
reports `SEPARABILITY: 0 findings` and all twelve mutants are killed.

No corpus byte needs repair. The gap is in the instrument, not in the round's landed content.
