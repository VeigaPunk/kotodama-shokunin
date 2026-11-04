# ScribeRecord — red-before / green checks (round 83, claim C record repairs)

Lane-relative paths only; `<lane>` is the lane root. No scratch root appears in this file or in the files it checks.

## Red-before — base `3088bd7fe2a55a123214abba7008dcddf12b301c`

```
$ git -C <lane> cat-file -s <base>:reports/round-82/counter-revisions.md
0
$ git -C <lane> show <base>:corpus/QUALITY.md | grep -c '^31\. '
0
$ git -C <lane> show <base>:reports/round-83/annotations/errata-r82.md
fatal: path 'reports/round-83/annotations/errata-r82.md' exists on disk, but not in '3088bd7fe2a55a123214abba7008dcddf12b301c'
rc=128
$ grep -n 'RECHECK-ERROR line' .ufo/waves/round-82/w1/stage/ExecEvidence/malformed-row-probe.txt
7:  stdout: 'RECHECK-ERROR line 5: row has 12 cells, expected 11\n'
17:  stdout: 'RECHECK-ERROR line 5: row has 10 cells, expected 11\n'
$ grep -c 'fast/scratch' reports/round-82/telemetry/quality30-probe.txt .ufo/waves/round-82/w1/stage/ExecEvidence/malformed-row-probe.txt
reports/round-82/telemetry/quality30-probe.txt:2
.ufo/waves/round-82/w1/stage/ExecEvidence/malformed-row-probe.txt:3
```

The defect census is the red-before criterion 31 names: an empty cited record (0 B at base) and two receipts carrying scratch roots. No RECHECK-ERROR receipt exists under `reports/round-82/telemetry/` (measured; the committed line-5 probe is the tracked wave-stage file above).

## Green — worktree after the three repairs

```
record_bytes                                        7051
record_hashes  696835ee5a8f8361031262f02d88299ea775ff1a  True
record_hashes  ea667212554f7062650ee6942d559bdd35736c05  True
record_first_line  Restored in round 83 from those committed receipts: `reports/round-82/telemetry/...
erratum_bytes                                       1018
erratum_markers  R82-M2 True / line 5 True / line 7 True
criterion_lines  [221]
criterion_body_bytes                                3416
criterion_markers  nonempty True / resolve True / access date True
earlier_219_lines_identical_to_base                 True (base file 57227 B)
base_criterion_count                                0
record_scratch_roots                                []
erratum_scratch_roots                               []
record_cited_tokens                                 13
```

All 13 backticked repo-relative tokens in the restored record resolve at base; the one self-reference (`reports/round-82/counter-revisions.md`) is 0 B at base by construction and 7051 B at the restored worktree.

## Commands (green)

```
$ wc -c <lane>/reports/round-82/counter-revisions.md
7051 <lane>/reports/round-82/counter-revisions.md
$ grep -c '^31\. ' <lane>/corpus/QUALITY.md
1
$ git -C <lane> diff --stat -- corpus/QUALITY.md
 corpus/QUALITY.md | 20 ++++++++++++++++++++
 1 file changed, 20 insertions(+)
$ git -C <lane> diff --numstat -- corpus/QUALITY.md
20	0	corpus/QUALITY.md
```

`git diff --numstat` reports 0 deletions: no earlier line moved. (The 20 added lines are the blank separator plus criterion 31.)
