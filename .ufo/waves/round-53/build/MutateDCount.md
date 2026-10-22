# MutateDCount — mutation test of `reports/round-53/d-count.py` (round 53, claim D)

Seat: `KotodamaR53.MutateDCount` (leaf; no delegation). Date: 2026-10-22.
Sandbox: `/fast/scratch/hyaku/kotodama-r53/MutateDCount` (private copy; the lane was never edited by this seat).

## 1. What was tested, and how

The claim instrument under test is `reports/round-53/d-count.py` in the lane
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`. The claim D statement says that
running that script over `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`
prints `OPEN 18` and `SID_BAD 0` at base (exit 1) and `OPEN 0` and `SID_BAD 0` after the repair
(exit 0). A counter that cannot distinguish those two states cannot support the claim, so the
question here is: which single-point changes to the counter would still print the same numbers?

Method:

1. The lane's `corpus/` tree and the lane's `reports/round-53/d-count.py` were copied into the
   sandbox. The lane was read only.
2. A **repaired copy** was made in the sandbox (`repaired/corpus/`) by cutting back the routed
   wording exactly as the round-52 routing describes. It is this seat's own reconstruction, not
   the lane's landing.
3. Twenty-five mutants were generated from the pristine script bytes, each changing exactly one
   source site. The generator asserts every replacement site is present and occurs once, so a
   mutant that does not apply to the pristine bytes is a hard error, not a silent no-op.
4. Each mutant was run on the base copy and on the repaired copy. A mutant is **killed** when
   either run no longer reproduces the pristine result (`OPEN 18`, exit 1 on base; `OPEN 0`,
   exit 0 on repaired) — by count, by exit code, or by any byte of output.
5. A survivor is not a licence to change the contract. It is a coverage finding: the detector
   has a leg that no corpus input exercises. For every survivor a **control input** was built —
   a corpus copy perturbed in one way — that separates the mutant from the pristine script, and
   the mutant was re-run on it.

Baseline, re-run at the end of the session on the pristine bytes (restoration evidence):

```
PRISTINE base      : OPEN 18  SID_BAD 0  exit 1
PRISTINE repaired  : OPEN 0   SID_BAD 0  exit 0
```

The base run lists the 18 instances the claim names: 6 over-read phrases (lines 54 twice, 76, 79,
121, 176), 10 draft-id fragments (lines 106, 107, 113, 174, 177 ×3, 179, 181 ×2) and the 2
wrong-row citations (lines 106 and 113).

## 2. The repaired copy used as the "after" state

`repaired/corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` changes exactly the
routed wording, and nothing else:

| line | before | after |
|---|---|---|
| 54 | `two tones (Suruí) force fixed formulas (S135)` | `two tones (Suruí) leave only a narrow set of tonal contrasts to carry (S135)` |
| 54 | `Hmong (Laos, Thailand, United States) (S135)` | `Hmong, in Laos, Thailand and the United States (S135; S140)` |
| 76 | `lip-locked /p/, /b/ merging with /k/ in the whistle (S147)` | `lip-locked /p/ merging with /k/ in the whistle (S147)` |
| 79 | `so the register is learned young (S151)` | `so the register is acquired in childhood (S151)` |
| 106 | `"a few words spoken by shepherds"; … "working their farms" (S159, -6)` | `"a few words spoken by shepherds" (S159); … "working their farms" (S162)` |
| 107 | `"someone gets lost in the bush" (S160, -6)` | `"someone gets lost in the bush" (S160)` |
| 113 | `mobile phones arrived (S163, -4)` | `mobile phones arrived (S159)` |
| 121 | `in Akan (Ghana) practice a master drummer is` | `an Akan court drummer is` |
| 174 | `named communities and instruments (S179, -5)` | `named communities and instruments (S179)` |
| 176 | `"natives of a jungle"/"primitive peoples", S181` | `"natives of a jungle", S181` |
| 177 | `formulaic redundancy (S179, -5, -6, -7)` | `formulaic redundancy (S179)` |
| 179 | `Urgent Safeguarding List, S183, -12)` | `Urgent Safeguarding List, S183)` |
| 181 | `(S173, -2)` and `(S173, -12)` | `(S173)` and `(S173)` |

The repaired copy reads `OPEN 0`, `SID_BAD 0`, exit 0. Its cited-id count drops from 50 to 49
because line 113 no longer cites S163.

## 3. Results — 25 mutants

`base` = run over the base copy (expect `OPEN 18`, exit 1); `repaired` = run over the repaired copy
(expect `OPEN 0`, exit 0). "killed by control" names the control input that kills a survivor.

| mutant | change (one site) | base OPEN | base exit | repaired OPEN | repaired exit | verdict | killed by control |
|---|---|---|---|---|---|---|---|
| M01 | `FRAG` regex loses its trailing word boundary (`, -[0-9]+\b` → `, -[0-9]+`) | 18 | 1 | 0 | 0 | survived | ctrl_frag |
| M02 | `FRAG` regex changes `, -` to `-` | 73 | 1 | 55 | 1 | killed | — |
| M03 | drop the OVER1 leg (`force fixed formulas`) | 17 | 1 | 0 | 0 | killed | — |
| M04 | drop the OVER2 leg (`(Laos, Thailand, United States) (S135)`) | 17 | 1 | 0 | 0 | killed | — |
| M05 | drop the OVER3 leg (`/b/` merging with `/k/`) | 17 | 1 | 0 | 0 | killed | — |
| M06 | drop the OVER4 leg (`learned young`) | 17 | 1 | 0 | 0 | killed | — |
| M07 | drop the OVER5 leg (`in Akan (Ghana) practice`) | 17 | 1 | 0 | 0 | killed | — |
| M08 | drop the OVER6 leg (`primitive peoples`) | 17 | 1 | 0 | 0 | killed | — |
| M09 | flip the S162 test (`not in` → `in`) | 17 | 1 | 1 | 1 | killed | — |
| M10 | drop the S163 exclusion from the WROW2 test | 18 | 1 | 0 | 0 | survived | ctrl_s163 |
| M11 | an absent `working their farms` line counts as closed | 18 | 1 | 0 | 0 | survived | ctrl_absent_farms |
| M12 | an absent `mobile phone` line counts as closed | 18 | 1 | 0 | 0 | survived | ctrl_s163, ctrl_absent_phones |
| M13 | skip the used-by check in SID_BAD | 18 | 1 | 0 | 0 | survived | ctrl_usedby, ctrl_column, ctrl_sidbad_only |
| M14 | drop the `S-id not in rows` guard in SID_BAD | 18 | 1 | 0 | 0 | survived | ctrl_missing_row |
| M15 | return 0 even when open items remain | 18 | **0** | 0 | 0 | killed | — |
| M16 | exit code ignores SID_BAD | 18 | 1 | 0 | 0 | survived | ctrl_sidbad_only |
| M17 | read the wrong column of SOURCES.md (`cells[11]` → `cells[10]`) | 18 (SID_BAD 50) | 1 | 0 (SID_BAD 49) | 1 | killed | — |
| M18 | ignore lines after the first FRAG match on a line | 15 | 1 | 0 | 0 | killed | — |
| M19 | remove the FRAG leg entirely | 8 | 1 | 0 | 0 | killed | — |
| M20 | drop the WROW1 check | 17 | 1 | 0 | 0 | killed | — |
| M21 | drop the WROW2 check | 17 | 1 | 0 | 0 | killed | — |
| M22 | SID regex takes two digits instead of three | 18 (cited 0) | 1 | 0 (cited 0) | 0 | killed | — |
| M23 | ignore phrase matches after the first on a line | 17 | 1 | 0 | 0 | killed | — |
| M24 | FRAG regex requires two or more digits | 10 | 1 | 0 | 0 | killed | — |
| M25 | phrase match anchored at line start (`match`, not `search`) | 12 | 1 | 0 | 0 | killed | — |

Killed: 18 of 25. Survived: 7 (M01, M10, M11, M12, M13, M14, M16).

Every mutation is a one-site diff; the full diffs are in `mutants/` in the sandbox and each mutant's
sha256 is in `results.tsv`.

## 4. Survivors and the controls that kill them

Each survivor is inert on both corpus states: the base entry cites only rows that already name it,
and both quoted lines are present in the entry. The controls below are corpus copies perturbed in
one way; pristine and mutant outputs are given as actually observed.

**M01 — the FRAG word boundary is not exercised.** No draft-id fragment in the corpus is followed by
a letter, so `\b` never changes the result.
Control `ctrl_frag`: one extra line appended to the entry, `Seat draft note: source ref , -6x stays open.`
```
pristine : OPEN 18  SID_BAD 0  exit 1     (", -6x" is not a fragment: \b fails between 6 and x)
M01      : OPEN 19  SID_BAD 0  exit 1     (", -6" matches without \b)
```

**M10 — the S163 exclusion is not exercised.** At base the mobile-phone line cites S163 *and* omits
S159, so the "S159 missing" half of the test already fires; the exclusion never decides anything.
Control `ctrl_s163`: the repaired entry with line 113 changed to `mobile phones arrived (S159; S163)`.
```
pristine : OPEN 1  (WROW2)  exit 1
M10      : OPEN 0  exit 0
```

**M11 — an absent farms line counts as closed.** Both corpus states quote the line, so the
"absent" branch is never taken.
Control `ctrl_absent_farms`: the base entry with `working their farms` changed to `working their fields`.
```
pristine : OPEN 18  (WROW1 'absent')  exit 1
M11      : OPEN 17  exit 1
```

**M12 — an absent mobile-phone line counts as closed.** Same shape as M11.
Control `ctrl_absent_phones`: the base entry with `mobile phones arrived` changed to `telephones arrived`.
```
pristine : OPEN 18  (WROW2 'absent')  exit 1
M12      : OPEN 17  exit 1
```

**M13 — the used-by check in SID_BAD is inert.** Every S-id the entry cites already names the entry
in its SOURCES.md used-by cell, so SID_BAD is 0 on both corpus states and the check contributes
nothing to the reported numbers.
Control `ctrl_usedby`: S140's used-by cell replaced by ` — `.
```
pristine : OPEN 18  SID_BAD 1 ['S140']  exit 1
M13      : OPEN 18  SID_BAD 0           exit 1
```
Control `ctrl_column`: S140's used-by cell replaced by ` — ` and the entry path moved into its
recheck cell.
```
pristine : OPEN 18  SID_BAD 1 ['S140']  exit 1
M13      : OPEN 18  SID_BAD 0           exit 1
```
Control `ctrl_sidbad_only`: the repaired tree with S140's used-by cell replaced by ` — `.
```
pristine : OPEN 0   SID_BAD 1 ['S140']  exit 1
M13      : OPEN 0   SID_BAD 0           exit 0
```

**M14 — the `S-id not in rows` guard is inert.** Every S-id the entry cites has a SOURCES.md row.
Control `ctrl_missing_row`: the base entry with line 104 citing `(S184; S199)`, S199 having no row.
```
pristine : OPEN 18  SID_BAD 1 ['S199']  exit 1
M14      : KeyError: 'S199'  (traceback, exit 1)
```

**M16 — the exit code's SID_BAD term is inert.** SID_BAD is 0 on both corpus states, so dropping it
from the exit expression changes nothing until a row fails the used-by test.
Control `ctrl_sidbad_only` (as above):
```
pristine : OPEN 0   SID_BAD 1 ['S140']  exit 1
M16      : OPEN 0   SID_BAD 1 ['S140']  exit 0
```

## 5. What this means for the claim (advice, not a ruling)

- The counter's 18 base instances are real content, not decoration: 18 of the 25 single-point
  changes break the base count, and the six over-read legs are each pinned by exactly one instance
  (M03–M08 each drop the count to 17). The FRAG leg is pinned by ten instances and the two
  wrong-row legs by one each (M18–M21).
- The repaired state is also pinned: 18 of 25 mutants break `OPEN 0` on the repaired copy.
- Four legs of the counter are not exercised by any corpus input today and can only be shown to
  work with a purpose-built control input: the FRAG word boundary, the S163 exclusion, the two
  "absent line" branches, and the whole `SID_BAD` machinery including its share of the exit code.
  A reviewer who wants to see those legs exercised should build the controls above (or their
  equivalents) rather than trust the corpus run.
- The `SID_BAD` finding is worth one sentence in the closure: at base the entry cites 50 S-ids and
  every one of them already names the entry in its used-by cell, so the SID_BAD leg reports 0 for
  the wrong reason as well as the right one. It is not evidence that the used-by cells are right.

## 6. Restoration evidence

- The pristine script was never edited: `sha256 618bb09e5f8142de6a973f1cd398e7727cb2ce56654dc819ba422afffcd03efd`
  for `reports/round-53/d-count.py`, identical in the sandbox copy and in the lane
  (`/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-53/d-count.py`), re-read after the
  mutation run.
- The sandbox base corpus snapshot is unchanged: entry
  `sha256 60b56b4f6d397e68ef799dbd6df3586a985ab72247dbd38199e4ca3f364098fe`, SOURCES.md
  `sha256 29c68ad0de9bda9fd20b533382cc595ed97edf69739e39504c451b9d774fac02` (both identical to the lane's
  SOURCES.md at the time of the copy).
- Only the repaired copy differs, as intended:
  `sha256 be46733b4cfabaa75478e9c4196fabd942538e43c28307454d426da0ba3bf1b9`.
- No file outside the sandbox and this seat's report was created or changed. No commit, no index
  write, no `jj` write; the only lane commands run were read-only (`git status`, `sha256sum`) and one
  read-only run of the counter over the lane.
- The lane's entry file has been edited by another seat while this session ran (its hash moved from
  the snapshot `60b56b4f…` to `39ef89ab…` and then to `8e53fde2…`; `git status` shows it modified
  with `corpus/lessons/round-53.md` and `reports/round-53/` untracked). A read-only run of the
  pristine counter over the lane at the time of writing printed `OPEN 6` (the six over-read phrases
  at lines 54 ×2, 76, 79, 121, 176) and `SID_BAD 0`, exit 1 — the draft-id fragments and the two
  wrong-row citations had already been repaired there. Those changes are that seat's work, not this
  seat's.

## 7. Unrun checks and limits

- The mutants were not run against the lane's live entry; a sibling seat was editing that file
  concurrently, so only the sandbox snapshots (taken at session start) are used as the base and the
  repaired state.
- The repaired copy is this seat's reconstruction of the routed repair. The falsify wave still has
  to judge whether each replacement is supported by the row it cites; the counter only shows that
  the routed wording is gone.
- No equivalent mutation run was done for `reports/round-53/accept-c.py` (claim C's instrument);
  that instrument was out of this seat's scope.
- Tooling: nothing was installed. Python 3.14.8 (system, Arch) with the standard library only;
  `diff`, `sha256sum` and `git status` from the system toolchain.

## 8. Files in the sandbox

```
/fast/scratch/hyaku/kotodama-r53/MutateDCount/
  corpus/                        base copy of the lane corpus (unmodified)
  repaired/corpus/               the OPEN-0 copy described in §2
  controls/                      eight control corpus trees (ctrl_frag, ctrl_usedby, ctrl_column,
                                 ctrl_s163, ctrl_absent_farms, ctrl_absent_phones,
                                 ctrl_sidbad_only, ctrl_missing_row)
  mutants/M01.py … M25.py        the 25 single-point mutants
  gen_mutants.py                 the generator (asserts each site applies exactly once)
  run_mutants.py                 the harness (base, repaired and control runs)
  results.tsv                    mutant sha256 and description
  mutant-descriptions.txt        mutant id and description
```
