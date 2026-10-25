# ScoutItem10 — round-69 w2 residual verification — item-10 quarantine evidence, independent re-derivation

Seat: ScoutItem10 (residual verification). Date: 2026-10-25. Lane read-only; the only lane
write is this file. Nothing was written, committed or executed inside
`/home/vgpnk/Projects/shokuknow` (git reads only); all scratch lives under
`/tmp/ScoutItem10-r69/`. No installs, no network fetches.

Inputs actually used:
- register `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`
  — 375 lines, sha256 `5afe1810a6c3d62f37987b575a954f5b1197daa23005d4bb2f1d982f64bad833`
  (matches the hash quoted in `.ufo/waves/round-69/w1/ScoutItem10.md:11-12`).
- canonical slice recipe: `corpus/lessons/round-68.md:102`.
- canonical id-collision recipe: fleet prompt `.ufo/prompts/kotodama-round-69.md:413-419`
  (the addendum `RECOVERY-RULES.md` owns budgets, not the recipe; it contains no awk/grep recipe).
- committed evidence: `.ufo/waves/round-69/assimilation/{quarantine-slice,reg-ids,staged-ids,collisions}`
  (687 B / 3910 B / 615 B / 0 B; `git show 6a98d7d --stat` = 21 / 782 / 123 / 0 lines).

---

## 1. Quarantine slice — the addendum's awk recipe — **PASS**

Recipe (verbatim from `corpus/lessons/round-68.md:102`, cwd `/tmp`):

```
cd /tmp && awk -F'|' -v l=kotodama '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print NR": "$2" "$3" "$4}' \
  /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
```

Output: 21 lines, register lines 118–135 (`payload-absent`) + 333–335 (never-checked, ids with a
trailing backtick, still matched by `$4 ~ /S[0-9]+/`):

```
118:  `kotodama`   round1   S776
…
135:  `kotodama`   round5   S827
333:  `kotodama`   round3   S807`
334:  `kotodama`   round3   S812`
335:  `kotodama`   round6   S835`
```

The committed artifact uses a different print (`$4" "$5`), so I reproduced that form byte-for-byte:

```
$ awk -F'|' -v l=kotodama '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4" "$5}' \
    /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md \
  > /tmp/ScoutItem10-r69/quarantine-slice
$ diff /tmp/ScoutItem10-r69/quarantine-slice .ufo/waves/round-69/assimilation/quarantine-slice
(empty)
TMP_SLICE_MATCHES_COMMITTED
```

ID-set comparison: `grep -oE 'S[0-9]+'` on both sides, `sort`, `diff` → empty (`IDS_IDENTICAL`,
21/21). The committed artefact is also byte-identical to `.ufo/waves/round-68/assimilation/quarantine-slice`.

**VERDICT: PASS** — 21 rows, ids `S776 S778 S779 S786 S787 S791 S792 S795 S796 S804 S807 S812
S814 S816 S817 S820 S823 S824 S825 S827 S835`, byte-identical to the committed slice.

## 2. Id-collision check (0–3 leading spaces) — **reg-ids PASS / staged-ids FAIL-to-reproduce / collisions PASS-at-base**

Recipe (verbatim from `.ufo/prompts/kotodama-round-69.md:415-419`), run into `/tmp`:

```
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' <registry>        | grep -oE 'S[0-9]+' | sort > reg-ids
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' $S/merge/kotodama/SOURCES.append.md | grep -oE 'S[0-9]+' | sort > staged-ids
comm -12 reg-ids staged-ids > collisions
```

**reg-ids — PASS.** Against the declaration base blob (`git show 793f797:corpus/SOURCES.md`, the
tree the check was declared against):

```
$ git -C <lane> show 793f797:corpus/SOURCES.md > /tmp/ScoutItem10-r69/base-SOURCES.md
$ grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' base-SOURCES.md | grep -oE 'S[0-9]+' | sort > reg-ids-base.txt
$ wc -l reg-ids-base.txt
782 reg-ids-base.txt
$ diff reg-ids-base.txt .ufo/waves/round-69/assimilation/reg-ids
(empty)  → REG_IDS_BASE_IDENTICAL
```

At the current working tree the same recipe gives **783** (`reg-ids-head.txt`); the single extra id
is `S859`, added by the data land `e86ed3e` — so the committed 782 is the pre-land snapshot and is
exactly reconstructed at the base, not at HEAD. This is expected, not drift.

**staged-ids — FAIL (not reproducible today).** The committed file is 123 ids, `S859 … S981`
(contiguous). The package it was taken from is an unversioned, regenerated input and has moved:

```
$ grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' $S/merge/kotodama/SOURCES.append.md | grep -oE 'S[0-9]+' | sort > staged-ids.txt
$ wc -l staged-ids.txt
132 staged-ids.txt                       # S859 … S990
$ diff staged-ids.txt <committed staged-ids>
124,132d123
< S982 … < S990                            # 9 ids added after the snapshot
$ head -123 staged-ids.txt | diff - <committed staged-ids>
(empty)  → COMMITTED_IS_PREFIX_OF_TODAY
```

The package working tree (`$S/merge/kotodama/SOURCES.append.md`, mtime 2026-10-24 23:33) is
modified relative to shokuknow `HEAD` (`git status --porcelain`: ` M merge/kotodama/SOURCES.append.md`;
`git diff --stat`: 132 insertions, 104 deletions). shokuknow `HEAD` itself yields **104** ids
(`S833 … S936`, `staged-ids-pkgHEAD.txt`) — i.e. the pre-renumbering package, which overlaps the
lane registry. So neither the current tree (132) nor shokuknow HEAD (104) reproduces the committed
123: the 123-row state existed only in the working tree between the declaration (20:57) and the
23:33 regeneration, and was overwritten. The committed value is consistent with the drift
(123 ⊂ 132), but it is a snapshot, not a re-derivable measurement.

**collisions — PASS at the base, but structurally tautological.** Against the base registry (782)
both the committed staged set and today's staged set give 0:

```
$ comm -12 reg-ids-base.txt <committed staged-ids> | wc -l   → 0
$ comm -12 reg-ids-base.txt staged-ids.txt          | wc -l   → 0
```

`reg-ids` at the base ends at `S858` and `staged-ids` begins at `S859`: the sets are disjoint by
construction, so `collisions = 0` is forced regardless of content. It is a true statement and the
committed file is genuinely 0 bytes, but it carries no guard signal; the guard signal lives in §3.

Observation (not a verdict on the base run): at the current HEAD the same recipe returns a
**nonempty** collision, `S859` — the lane's own new row (`corpus/SOURCES.md:814`, own-work
settlement classifier) has the same id as the first staged package row (`GB/T 33661-2017`, the
register's S776 source). This is the namespace collision the lesson warns about, and it is the
direct counter-example to the sentence tested in §4.

**VERDICT: reg-ids PASS; staged-ids FAIL (123 not re-derivable — unversioned package drift, 132
today); collisions 0 PASS-as-stated but content-independent.**

## 3. Guard proof — indented row must produce a nonempty `collisions` — **PASS**

The fleet prompt (`.ufo/prompts/kotodama-round-69.md:421-423`) requires this proof before any
append and it is grounded in `CORPUS.md:152-153` ("accepts 0–3 leading ASCII spaces … 4 or more
spaces are indented code and are ignored").

Fixture A — minimal, isolates indentation. Scratch registry contains only the indented row; scratch
staged set contains `S002`:

```
$ printf '# SOURCES\n\n## Registry\n\n| id | source |\n|---|---|\n  | S002 | fixture indented row |\n' > guard/registry-indented.md
$ printf 'S002\n' > guard/staged-s002.txt
old pattern '^\|[[:space:]]*S[0-9]{3,}'          → reg=0, comm collisions = 0 lines
0–3 pattern '^ {0,3}\|[[:space:]]*S[0-9]{3,}'    → reg=1, comm collisions = 1 line: S002
```

Fixture B — full copy of the base registry with the existing `S002` row moved to 2 leading spaces
(line 31), staged set = today's package ids + `S002`:

```
$ cp base-SOURCES.md guard/registry-full.md && sed -i 's/^| S002 |/  | S002 |/' guard/registry-full.md
old: reg=781 coll=0
new: reg=782 coll=1  → S002
```

**VERDICT: PASS** — the column-zero pattern false-greens exactly as the prompt says; the 0–3-space
pattern catches the indented collision on both a minimal and a full-size registry. Caveat:
the lane committed **no** guard-proof artefact of its own (no round-69/68 report or telemetry file
contains this fixture; `grep -rln 'indented\|false-green'` over `.ufo/waves/round-6{8,9}` and
`corpus/lessons/round-6{8,9}.md` hits only the unrelated W04 census-blinding critique in
`.ufo/waves/round-68/w1/CriticAmendD2.md`). The proof is supplied here, post hoc; the committed
item-10 evidence set does not contain it.

## 4. `corpus/lessons/round-69.md ## Quarantine` vs re-derived numbers — **numbers PASS / one interpretive claim FAIL / considerthese PASS**

| lesson claim (`corpus/lessons/round-69.md:51-64`) | re-derived | verdict |
|---|---|---|
| "**21 data rows**, matching the round-68 count" | 21, byte-identical to both committed slices | PASS |
| "(9 present, 8 refused, 4 unverifiable)" | lines 111/112/113/114 → 9 + 8 + 1 + 3 = 21; `comm -3` against the slice ids = empty | PASS |
| "`reg-ids` 782 ids" | 782 at base `793f797`, byte-identical | PASS |
| "`staged-ids` 123 ids" | committed artefact has 123, but today's package yields 132 and shokuknow HEAD 104 — not re-derivable | PASS as a restatement of the artefact, **FAIL as a reproducible number** |
| "`collisions` **0**" | 0 at the base (tautological: S001–S858 vs S859–S981); 0-byte file confirmed | PASS at the base; nonempty at HEAD (S859) |
| "The lane's own new row is S859, which is **outside** the staged id set" | `staged-ids:1` **is** `S859`; today's package also starts at S859 | **FAIL** |
| "`considerthese/` is **absent** for this lane" | `ls -d /…/kotodama-shokunin/considerthese` → No such file; `corpus/considerthese` also absent; shokuknow has no `considerthese` either | PASS |

The failing sentence matters twice: (a) it contradicts the artefact it cites in the same paragraph
(`S859` is line 1 of the committed `staged-ids`); (b) the correct reading is the opposite — the
lane's own settlement row was allocated the same id as the first staged package row, which is why
the recipe run on today's tree returns `S859` as a collision. Nothing was adopted this round, so
the practical consequence is nil (no renumbering was due), but the recorded reassurance is false
and a future adoption round must treat `S859` as contested rather than as free.

**VERDICT: 21 / 9-8-4 / 782 / 0 / considerthese PASS; 123 not reproducible; the `S859 outside the
staged id set` sentence FAIL.**

## Residual unknowns / for the L1

- The 123-row package state is unrecoverable from disk (overwritten at 23:33; shokuknow HEAD is the
  older 104-row S833–S936 numbering). Whether the 123 ids were exactly `S859…S981` at 20:57 can be
  inferred (today's set is a strict superset with the same head) but not proven.
- The committed item-10 evidence has no guard-proof receipt; the prompt requires one "before this
  lane's first append under this item". None happened (nothing appended), and the proof is now on
  record here.
- No other seat in this wave (w1 or w2) re-ran the id-collision recipe: `RevC1.md` lists the three
  files as added, and `ScoutItem10.md` covers the slice only.
- Commands run: `awk`, `grep`, `sort`, `comm`, `diff`, `wc`, `sed`, `printf`, `git show/status/diff/
  log/rev-parse` (read-only). Nothing installed, nothing fetched.
