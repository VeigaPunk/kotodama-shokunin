# CriticMeasurement — round 50, all claims: counting-command validity

Seat: `ChousaR27R2.CriticMeasurement-4` (critic, leaf). Assigned item: attack every counting
command in `reports/round-50/claims.json` for before/after validity, circularity and base-run
safety, and specify the exact base and final commands the round report must paste.
Author-lane advice only; this is not an admission decision.

Inputs: `reports/round-50/claims.json` is **untracked** (`git ls-files --error-unmatch` → no
match) with sha256 `fd3d6346c4f1b0db518fafece5acb96601460683d675114f11c22b7b57af599b` at
2026-10-21 15:2x UTC. Base `B=4ad26836552462d28a946ca3b067cab0b5ce3532`. Lane HEAD is
attached to `main` = `origin/main` = B; jj `@` = `13ae1394` (empty), `snapshot.auto-track =
"none()"`.

Axes: coverage (C), operability (O), calibration (Ca and every counting command).

## Headline findings (strongest counterexamples first)

### M1 (blocker, Ca + C) — "checker on round-50 claims exits 0" is false or vacuous under the declared semantics

The shared contract says that X depends on Y when X's landed bytes **name any Y land path**.
At base, with no round-50 edit at all:

- `tools/check-readme-revisions.py` (an O land) names `corpus/README.md` (a C land) at
  `:2` and `:306` (`"%s:corpus/README.md" % BASE_COMMIT`). This gives **O→C**.
- `corpus/README.md` (a C land) names `tools/check-readme-revisions.py` (an O land) at `:18`,
  in the rev-2.6 body. This gives **C→O**.

So whole-file path matching turns pre-existing references into dependencies. The acceptance
"run on `reports/round-50/claims.json` exits 0" can then only pass in two ways. Either the tool
is weakened (for example, the path leg is dropped), or the input is not a manifest. As of this
review `claims.json` has no `schema`, `tree` or `exports` fields, so the contract requires
exit 2 (input error), not 0.

The frontier step (SOURCES rows S048 and up, plus `corpus/lessons/round-50.md`) is also not a
manifest claim. C's entry will cite S048+, which do not exist at B (the SOURCES row count at B is
47 and the last id is S047). The r49 mistake therefore comes back invisibly: C depends on the
frontier step (call it C→F), and an exit-0 run proves nothing. This is the same
REJECTED-HONEST-STOP pattern recorded in `corpus/lessons/round-49-verifier-spotcheck.md:16`.

**Smallest safe correction.**

1. Define a dependency as a reference to something **Y creates**. That is a path that is absent
   at base and present at `Y.tree`, or an export regex with 0 matches in base bytes and at least 1
   match at `Y.tree`. Match only against **lines X adds** (`git diff B X.tree -- X.lands`, `+`
   lines), not whole files.
2. Land an explicit manifest, `reports/round-50/separability/r50-manifest.json`, and add it to
   Ca's `lands`. It must contain the frontier step as pseudo-claim `F`, with lands
   `corpus/SOURCES.md` and `corpus/lessons/round-50.md` and export `\bS0(4[89]|[5-9]\d)\b`.
3. Declare the honest expected result: either `C→F` (exit 1, a disclosed and ordered
   dependency), or land F first as its own commit and make that commit C's counterfactual base.
   Rewording "frontier step, not a claim" does not make C separable.

### M2 (blocker, Ca) — a "1/1 detected" result on the r49 fixture means the fixture was tuned

r49 C, Ca and S all landed in **one commit**, `c6a174d` (`git show --stat`). Per-claim `tree`
values are therefore identical, and `corpus/README.md` was landed by **both** C and Ca, which
violates the disjoint-lands premise.

I simulated the declared semantics with read-only `git show` (`/tmp/cm50-sim.py`, now
removed). The inputs were r49 lands taken from `git show --stat`, plus these exports:
`\bS0(3[1-9]|4[0-3])\b` for S, `hunting-foraging-subsistence` for C, and
`\bREVISION-(DUP|STUB|ORDER)\b` for Ca. At both `c6a174d` and `d91c632` this gives
**15 findings across 5 ordered pairs**:

- C→S via export S031 in the entry, and via path `corpus/SOURCES.md`.
- S→C via the SOURCES `used-by` column and via `lessons/round-49.md`.
- C→Ca, because README `:18` names `tools/check-readme-revisions.py`.
- Ca→C through the shared README.
- S→Ca, because `lessons/round-49.md` names REVISION-DUP.

A fixture that yields exactly "C→S, 1/1" must have dropped Ca and S's back-references, or
narrowed exports, with the answer already known. That is circular calibration: recall over one
hand-picked pair, with precision never measured.

Note also that S→C is a real byte dependency. The r49 addendum's own S separability note says
that without C, rows "would read queued", so S's bytes change.

**Correction.** Derive the fixture mechanically from `reports/round-49/claims.json`, the addendum,
and `git show --stat c6a174d`. Pin its sha256 in the report before the first checker run. The
expected output must be the **exact finding set**, with each finding adjudicated as true
dependency, accepted back-reference, or shared-land. The shared-lands case must be its own
finding class or an input error, never a silent pass. Report precision and recall, not "1/1".

### M3 (high, O) — the false-negative-only probe metric is gamed by always-refuse or always-fail

"0/3 false negatives on landed tools" is satisfied by a guard that exits 3 on everything and a
checker that exits 1 on everything. The probe must also count **false positives** on paired
controls, and require 0. Base bytes reproduce every one of these with plain git
(GIT_CEILING_DIRECTORIES=/tmp, sandbox under `/tmp`, no jj needed):

| scenario (base tool bytes) | observed | role |
|---|---|---|
| receipt on `C2` = `refs/remotes/origin/main`, HEAD detached at `C1` (below the tip) | guard **rc 0** (allowed) | R2 false negative |
| HEAD = empty local commit `C3` on top of `C2` = origin/main | guard rc 3, `committed_sha=<C3>` ≠ origin/main | R1 false negative |
| `check-readme-revisions --selftest` in a git-free export | **rc 0**, `SKIP … (base object unreachable)`, `selftest skips: 1`, "all checks passed" | R3 false negative |
| new path `reports/other.json`, tip checkout | rc 0 | false-positive control (must stay 0) |
| same, with `refs/remotes/origin/main` deleted | rc 0 | false-positive control: a missing ref means absent, not an error |
| `check-readme-revisions --selftest` in a full clone at B | rc 0, `PASS … base c42d675`, `skips: 0` | false-positive control |

Further required controls: a receipt only in HEAD that was never pushed must still be refused,
and must not be labelled landed. A receipt whose blob differs between HEAD and origin/main must
report both blobs.

### M4 (high, O) — git discovery walks upward and silently masks R3

`check-readme-revisions.py:306` runs `git -C LANE` with LANE = `tools/..` and **does not scrub
`GIT_*`**, unlike `receipt_guard._git`. Any `--tools-root` tree without its own `.git` that sits
under the lane resolves to the lane's `.git` (or a work clone's), and `c42d675` resolves there.
The probe then reports R3 as absent on base (2/3 instead of 3/3), which is a measurement artifact.
Every executor work clone lives under the lane (`.ufo/waves/round-50/work/<NAME>`), so this is
the default path. Required: the probe creates its trees with `mktemp -d /tmp/...`, sets
`GIT_CEILING_DIRECTORIES`, and strips `GIT_DIR` and `GIT_OBJECT_DIRECTORY` from the environment.
[INFERENCE] The O fix should also scrub `GIT_*` in CR's git call, matching RG `:49-51`.

Interaction with Ca's dynamic leg: once O fails closed, any acceptance argv that runs
`check-readme-revisions --selftest` inside Ca's **git-free** counterfactual dir exits nonzero by
design. O's acceptance in a manifest must therefore name a clone (with `.git`), not the git-free
tree. Otherwise O's correct fix shows up as an "acceptance failure".

### M5 (high, O) — a retained control can silently become vacuous

`receipt_guard.py:331-340` (`runner-rechecks-before-publisher`) points HEAD at the unborn
`refs/heads/not-filed`. It then expects exit 3 from the **second** check, but it never asserts
that the callback ran. If the R1/R2 fix adds `refs/heads/main` or `refs/remotes/origin/main`
carrying the receipt to the shared `_fixture_repo`, the **first** guard refuses. The control
still passes (rc 3, COMMITTED) but no longer tests the recheck.

Likewise, `:234-235` asserts `committed_sha={head}`. If the fix redefines `committed_sha` as the
landed sha, that assertion must be edited, which weakens a control.

Required: keep `committed_sha` = HEAD byte-identical and add a separate `landed_sha=` field.
Either keep the branch and remote refs out of the shared fixture or add a marker assertion to the
recheck control. Paste the selftest diff showing **no removed assertion lines**.

### M6 (medium, C) — the topic-owner evidence command is substring-based (cross-ref CriticGapPremise, SrcBarfield)

At base, `grep -rniE '^- topic:.*(pastoral|herd|…)'` returns one line,
`writing-media-surface-economy.md:3`: "herd" inside "s**herd**". The word-bounded form returns 0.
After landing, the entry's own topic line matches, so the "before 0 → after 0 owners" framing is
wrong. The correct pair is base **0**, final **exactly 1 = the new entry**. Piping into
`cut`/`wc` also hides grep's rc. Print `-l` lists, not piped rcs.

### M7 (medium, C) — `find` counts the working copy, not the landed commit

Under jj with `auto-track none()`, files can exist on disk without being in any commit, so
`find … | wc -l` can read 226 when the pushed tree holds 225. Count from the **pushed** sha with
`git ls-tree`. Also assert `git merge-base --is-ancestor $B $F` and `F == refs/remotes/origin/main`
(this is the R1 hazard applied to the report itself).

### M8 (medium, C) — two after-requirements have no command

"Every cited S-id resolves to a SOURCES row whose used-by names the entry" and "8-field head in
order" have no command. They are given below. C's README revision gate must use the **base**
checker bytes (`git show B:tools/check-readme-revisions.py`). If C used O's modified checker, C
would gain an acceptance dependency on O.

### M9 (low, O/Ca) — `grep_absent` before-checks are gameable as after-evidence

`readme-rev-skip-present` (`base object unreachable`) and `guard-head-only` (`refs/remotes/origin`)
flip if a string is reworded or added in a comment. They are valid only as **before** freshness
probes. The after-evidence must be the behavioural probe (M3).

### M10 (low, all) — base runs must not write into the lane

`receipt_guard --selftest` creates `.scratch/` under `parents[2]` of the script. That directory is
gitignored (`.gitignore:6`), but it is a lane write, and the fixture runs `git worktree add`.
`reports/round-49/run-validation.py` writes a filed receipt. **Never** run either in the live lane
for "base" numbers. Read r49's committed `validation.json` instead (base:
`claims.separability.c_without_s.passed = true`, which is the 0/1 detection Ca cites).
`claims.json` itself should be committed, or its sha pinned in the report, before any final run,
so the declared thresholds cannot move post hoc.

## Exact commands the round report MUST paste (base, then final)

The common preamble is pasted once. `F` is the pushed sha.

```bash
L=/home/vgpnk/Projects/shokunin/kotodama-shokunin; B=4ad26836552462d28a946ca3b067cab0b5ce3532
F=$(git -C $L rev-parse refs/remotes/origin/main); git -C $L merge-base --is-ancestor $B $F; echo anc=$?
export GIT_CEILING_DIRECTORIES=/tmp
exp(){ d=$(mktemp -d /tmp/r50-$1.XXXX); git -C $L archive $2 | tar -x -C $d; echo $d; }   # git-free tree
cln(){ d=$(mktemp -d /tmp/r50-c$1.XXXX); git clone -q $L $d && git -C $d checkout -q $2; echo $d; }  # tree with .git
DB=$(exp b $B); DF=$(exp f $F); CB=$(cln b $B); CF=$(cln f $F)
sha256sum $L/reports/round-50/claims.json   # must equal fd3d6346…599b or the drift is disclosed
```

### C (run with X=$B, then X=$F; D=$DB, then $DF)

| # | command | base (observed) | final (required) |
|---|---|---|---|
| C1 | `git -C $L ls-tree -r --name-only $X -- corpus/knowledge \| grep -c '\.md$'` | 225 | 226 |
| C2 | `git -C $L ls-tree --name-only $X -- corpus/knowledge/culture-material/ \| grep -c '\.md$'` | 27 | 28 |
| C3 | `git -C $L grep -lIiE '^- topic:.*\b(pastoral(ism\|ist\|ists)?\|herd(ing\|er\|ers\|s)?\|husbandry\|transhumance\|livestock)\b' $X -- corpus/knowledge` | (empty) | exactly `…/pastoralism-animal-husbandry.md` |
| C4 | `git -C $L ls-tree -r --name-only $X -- corpus/knowledge \| grep -iE 'pastoral\|husband\|herd'` | (empty) | exactly the new entry |
| C5 | `(cd $D && python3 -B reports/round-28/readme/sweep.py; echo rc=$?)` | rows 225 files 225, topic_mismatch 0, totals 225, footer 25/26/27/29/24/94, rc=0 | rows 226 files 226, topic_mismatch 0, totals 226, footer 25/26/28/29/24/94, rc=0 |
| C6 | `git -C $L show $B:tools/check-readme-revisions.py > /tmp/crr-base.py; python3 -B /tmp/crr-base.py --readme $D/corpus/README.md; echo rc=$?` | findings 0, rc=0 | findings 0, rc=0, new top label > 2.6 |
| C7 | `E=$DF/corpus/knowledge/culture-material/pastoralism-animal-husbandry.md; wc -l < $E; grep -c '^# ' $E; grep -c '^### ' $E; grep -c '^- topic:' $E` | n/a | ≤250 · 1 · 0 · 1 |
| C8 | `awk '/^## /{exit} /^- [a-z][a-z -]*:/{sub(/:.*/,"");print}' $E \| paste -sd,` | model: `- topic,- gap filled,- sources,- couples,- source,- verified-at,- recheck,- scope` | identical string |
| C9 | S-id resolution (below) | n/a | `cited≥1 new≥1 bad=[]` |

```bash
python3 - "$DF" <<'EOF'
import re,sys; d=sys.argv[1]; E='corpus/knowledge/culture-material/pastoralism-animal-husbandry.md'
ids=sorted(set(re.findall(r'\bS\d{3}\b',open(f'{d}/{E}').read())))
rows={m.group(1):m.group(0) for m in re.finditer(r'^\|\s*(S\d{3})\s*\|.*$',open(f'{d}/corpus/SOURCES.md').read(),re.M)}
bad=[i for i in ids if i not in rows or E.rsplit('/',1)[1] not in rows[i].rsplit('|',2)[-2]]
print('cited',len(ids),'new',sum(int(i[1:])>=48 for i in ids),'bad',bad)
EOF
```

Frontier census, base vs final: `git -C $L show $X:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`
gives 47 at base and 47+N at final, plus the seven SOURCES-CONTRACT-v1 census commands run on
`$DF`. Every new row's quote must be ≤25 words with access date 2026-10-21 in
`lessons/round-50.md ## Gate`.

### O (base column = base tool bytes; final = landed bytes)

| # | command | base (observed/required) | final (required) |
|---|---|---|---|
| O1 | `python3 -B $DF/reports/round-50/jj-colocation-probe.py --tools-root $DB` (probe trees under `/tmp`, ceiling set) | FN 3/3 (R1, R2, R3), FP 0/k | n/a |
| O2 | `python3 -B $DF/reports/round-50/jj-colocation-probe.py --tools-root $DF` | n/a | FN 0/3 **and** FP 0/k (the M3 controls) |
| O3 | `(cd $CX && python3 -B tools/harness/receipt_guard.py --selftest) \| python3 -c 'import json,sys;d=json.load(sys.stdin);print(d["controls_passed"],d["controls_total"]);print("\n".join(sorted(c["control"] for c in d["controls"])))'` | 45 45 (names listed) | P==T, with the name set ⊇ the base 45 |
| O4 | `(cd $CX && python3 -B tools/check-readme-revisions.py --selftest; echo rc=$?) \| grep -E '^(PASS\|FAIL\|SKIP)\|skips\|rc='` | 11 PASS, skips 0, rc=0 | the same 11 PASS names plus a new fail-closed control; no SKIP path remains; rc=0 |
| O5 | `(cd $DX && python3 -B tools/check-readme-revisions.py --selftest; echo rc=$?)` (git-free) | **rc=0**, `SKIP … unreachable`, skips 1 (R3 live) | rc≠0 with a named fail-closed diagnostic |
| O6 | `git -C $L diff $B $F -- tools/harness/receipt_guard.py tools/check-readme-revisions.py \| grep -E '^-[^-]' \| grep -E 'check\(\|cli\(\|controls.append\|passed'` | n/a | empty, or each removal justified |

Independent cross-check, pasted with O1 so the author-built probe is not the only witness: the
plain-git R1/R2 sandbox above (init `main`; C1 without the receipt; C2 with
`reports/validation.json`; `update-ref refs/remotes/origin/main C2`; `checkout --detach C1` → guard
rc; `checkout --detach C2; commit --allow-empty` → `committed_sha` vs origin).

### Ca

| # | command | base | final |
|---|---|---|---|
| Ca1 | `git -C $L ls-tree -r --name-only $X -- tools \| grep -ci separab` | 0 | 1 |
| Ca2 | `git -C $L show $X:corpus/QUALITY.md \| grep -nE '^7\. ' ; git -C $L show $X:corpus/QUALITY.md \| grep -c 'round-49-verifier-spotcheck'` | (none) · 0 | criterion 7 line · ≥1 |
| Ca3 | `git -C $L show $B:reports/round-49/validation.json \| python3 -c 'import json,sys;print(json.load(sys.stdin)["claims"]["separability"]["c_without_s"]["passed"])'` | `True` (0/1 detected) | unchanged (filed bytes) |
| Ca4 | `sha256sum $DF/reports/round-50/separability/r49-fixture.json` before the first checker run, and again at report time | n/a | equal |
| Ca5 | `(cd $DF && python3 -B tools/check-claim-separability.py reports/round-50/separability/r49-fixture.json; echo rc=$?)` | n/a | rc=1; **exact** finding set equal to the fixture's declared expectation (M2), with precision and recall printed |
| Ca6 | `(cd $DF && python3 -B tools/check-claim-separability.py --selftest; echo rc=$?)` | n/a | rc=0, including: the r49 fixture with C's S0xx citations stripped → C→S gone; a planted cross-reference → flagged; a pre-existing path mention (O→C README case) → **not** flagged |
| Ca7 | `(cd $DF && python3 -B tools/check-claim-separability.py reports/round-50/separability/r50-manifest.json; echo rc=$?)` with F as a pseudo-claim | n/a | the honest result (expected `C→F`, rc=1, disclosed), or rc=0 only if F was landed as C's base. Never run on raw `claims.json` (contract rc=2) |

## Unrun checks

- I ran no checks on executor patches: none existed at review time (`patches/` was empty).
- I did not run `claims-freshness.py` (it has write paths at `:1125` and `:2503`).
  CriticGapPremise covers its probe.
- I did not run `run-validation.py`, because it writes a filed receipt.
- The probe and checker do not exist yet, so O1, O2 and Ca4–Ca7 are specifications, not
  observations.

## Session record

- No tool installs.
- All writes went to `/tmp` (`cm50-base`, `cm50-sbx.*`, `cm50-clone`, `cm50-sim.py`, and the
  selftest outputs) and were removed.
- Lane access was read-only: `git show`, `ls-tree`, `archive`, `grep`, `cat-file`, `clone` from the
  lane into `/tmp`.
- I ran one `jj log` in the lane before switching to `--ignore-working-copy`. The jj op log is
  unchanged afterwards (op head `77950fc537a2`, 12:05:31, no new operation), and `@` was empty
  because of `auto-track none()`.
