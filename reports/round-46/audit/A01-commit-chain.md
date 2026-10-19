# A01 — loop-1 commit-chain census (claim A, adjacency)

Read-only audit. HEAD `1dfb87f`; lane identity `kotodama-shokunin <kotodama@shokunin.local>`.

## Per-round lane commits (all authored by the lane identity)

| round | lane commit | author |
|---|---|---|
| 33 | da68a6d | kotodama-shokunin <kotodama@shokunin.local> |
| 34 | 4a7aede | kotodama-shokunin <kotodama@shokunin.local> |
| 35 | ce103bf | kotodama-shokunin <kotodama@shokunin.local> |
| 36 | 57c8409 | kotodama-shokunin <kotodama@shokunin.local> |
| 37 | fa90c77 (+9bccc9b SCORECARD axes) | kotodama-shokunin <kotodama@shokunin.local> |
| 38 | dfb0719 | kotodama-shokunin <kotodama@shokunin.local> |
| 39 | fd55e1f | kotodama-shokunin <kotodama@shokunin.local> |
| 40 | 13a1657 (+456674d receipt refresh) | kotodama-shokunin <kotodama@shokunin.local> |
| 41 | ac47c78 | kotodama-shokunin <kotodama@shokunin.local> |
| 42 | 7ceff59 | kotodama-shokunin <kotodama@shokunin.local> |
| 43 | c9f4eaa | kotodama-shokunin <kotodama@shokunin.local> |
| 44 | 1dfb87f | kotodama-shokunin <kotodama@shokunin.local> |

## Author census

`git log --format='%an <%ae>'` filtered to round commits → **14/14
`kotodama-shokunin <kotodama@shokunin.local>`**, zero foreign-author commits.

## Cross-repo boundary

- Lane commits touching the fleet-root `MANIFEST.json` / `.ufo/`: **zero**.
  The grep hits for "manifest|.ufo" resolve to in-province files:
  `.ufo/reports/round-32/kotodama.md` (inside the lane) and
  `reports/round-2[78]/pinsweep/frozen/*/MANIFEST.tsv`, `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` (inside lane round dirs). Not fleet paths.
- Fleet commits touching lane `corpus/`/`tools/`/`reports/`: **zero**
  (`git -C /home/vgpnk/Projects/shokunin log --name-only -- kotodama-shokunin/corpus kotodama-shokunin/tools kotodama-shokunin/reports` → empty).
- Pushes/merges: **zero** in the window. The lane is ahead of origin by its
  loop-1 commits (`@{u}..HEAD` lists them); local-first holds — push is
  operator-owned and was not performed.

## Two-commit pattern

Each loop-1 round = one lane round-commit + one fleet-side ledger/report commit
(`/home/vgpnk/Projects/shokunin` `git log`: `round-NN ledger + fleet report` /
`fleet: kotodama round-NN`). Holds across 33-44.

Verdict: claim A verified — boundary intact, identity uniform, no cross-repo
write, no push/merge.
