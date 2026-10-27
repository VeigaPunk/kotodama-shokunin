# Draft — round 76 `corpus/SOURCES.md`: one `## Paths` row and one `## Search log` note

Stage-only draft against lane base `98c486bdb4650ba5b8e651d332910e8ee60ad121`. **Not applied to the
lane.** Seat: ScribeIndex.

Section boundaries in the base file: `## Registry` line 26, `## Paths` line 849, `## Search log`
line 884, `## Leads (unopened)` line 896. The `## Paths` row goes in as the **last bullet of the Paths
section** (immediately before the `## Search log` heading); the Search log note goes in as the **last
paragraph of the Search log section** (immediately before the `## Leads (unopened)` heading). Nothing in
the Registry table is drafted here — registry rows are another seat's artefact.

Both insertions are **CONDITIONAL** on which of the four round-76 candidate entries the Gate admits, and
on the lane ids the document map settles: the claim plans S894 (National Archives of Japan era-name
table — campaign S908 live form + S935 Wayback capture of the same page, one row), S895 (xingzuobaike
GB/T 33661 reproduction — campaign S916), S896 (openstd newGbInfo Wayback — S932), S897 (openstd showGb
page — S938), S898 (gmw.cn 2017 report — S937). Lane ids are not quoted in the prose below beyond those
planned ids, because one row per document is the rule and the scouts may still merge two URLs into one
document.

---

## 1. `## Paths` row — insert as the last bullet of the section

```markdown
- calendar and era instruments — S898 → S896 → S897 → S895: the state press's promulgation report first
  (what a published 农历 calendar is required to state, and at what precision), then the registry's
  record of the standard at an address a plain client can open, then the authoritative copy's own
  account of why its clause text cannot be reached that way, then the one page that reproduces the
  clause text — read as a declared reproduction and never as the standard itself; the archival leg,
  S894, is read beside the set rather than through it, because an institution's applied dating
  vocabulary is evidence of how an archive dates its holdings, not of what the standard compels.
```

Reading order and its reason: the promulgation report is the cheapest carrier of the standard's
requirements and states them in the state's own words; the registry record establishes identity and the
route before any clause is quoted; the showGb page is what tells a reader the route is closed to a plain
client, so no later statement can pretend the clause text was opened directly; the reproduction page is
last because it is the weakest carrier and every statement taken from it is scoped to it. The era-name
table is a different document class (institutional practice, not a standard) and is deliberately not
chained into the standard's reading order.

If the Gate admits no entry citing the reproduction page, drop `→ S895` and the clause about the
reproduction; if it admits none citing the showGb page, drop `→ S897` and its clause. If it admits no
entry citing the archival table, drop the archival sentence and the row covers the standard only; if it
admits none of the standards documents, the row is not installed at all.

---

## 2. `## Search log` note — insert as the last paragraph of the section

```markdown
**Calendar and era instruments — assimilation package triage (round 76).** Question: which entries of
the read-only assimilation package can this lane admit as the round-76 coverage move — standards-level
calendar compilation (GB/T 33661-2017 and the route to its clause text) and archival era-name tables —
without duplicating an entry or a document the lane already holds, and which of their documents must a
lane reader open before any row is written? Where searched: the package at
`/home/vgpnk/Projects/shokuknow/merge/kotodama/` — `knowledge/corpus/knowledge/` (40 staged `.md` files
across four partitions: culture-material 9, linguistics 17, myth-symbol 5, verification 9),
`SOURCES.append.md`, `MERGE-REPORT.md` — together with the package's own id census (`staged-ids` 132,
`reg-ids` 817, `collisions` 35) and this lane's `corpus/knowledge` and Registry table for duplicate
targets and duplicate documents; no search engine and no web query was used, this is a package sweep and
not a query sweep. Date 2026-10-27. Identified 40 staged knowledge files carrying 132 proposed source
rows. Screened <<FILL:screened>> by opening the candidate document (the other three partitions were
triaged at file-name and `- topic:` level only). Included <<FILL:included>> entries, citing
<<FILL:rows>> distinct documents written as rows S894–S898. Excluded <<FILL:excluded>>, for these
reasons: 4 staged culture-material files are already held by this lane
(`heritage-taxonomy-models.md`, `heritage-taxonomy-models.amend-2026-10-24-r13.md`,
`worldbuilding-setting-practice.md`, `worldbuilding-setting-practice.amend-2026-10-23.md`) and carry no
new coverage; 1 further staged file is not held but is the older amendment of an entry the round
already covers and is flagged a duplicate target by the package's own merge report
(`era-periodization-models.amend-2026-10-23.md`); 31 staged files sit in the linguistics, myth-symbol
and verification partitions and are outside this round's frozen theme, named here as available to a
later round rather than re-screened; and <<FILL:unreachable>> candidate documents could not be opened, so
their entries were not admitted. Stop rationale: the frozen theme covers one partition and four
candidate paths, all four now have a document map and no further in-theme entry remains unexamined;
widening to the other three partitions would change the claim, not serve it.
```

Notes for the installer:

- Every `<<FILL:...>>` slot is a count only the scouts' reports can supply, at the seat-named report
  paths under `.ufo/waves/round-76/w1/` — package triage (`ScoutPackageTriage.md`), per-document scouts
  (`ScoutDocS894.md` … `ScoutDocS897.md`), quarantine (`ScoutQuarantine-2.md`) and the coverage sweep
  (`ScoutCoverageSweep.md`). Those seat names are from the round-76 roster; the exact file each one
  writes is [INFERENCE] and must be confirmed before the note lands. **No count is invented here.** The
  measured parts are the file and id counts, derived in §3.
- `Identified 40` counts the staged `.md` files under the package's `knowledge/` tree. The package also
  carries 4 files under `amendments/` and its merge report states "proposed knowledge entries: 56" — the
  difference between that figure, the 40 staged files and the 4 amendment files is unresolved here and
  should be settled before the note is written as 40; the census the note states must match the number
  the package triage actually screens.
- `Excluded` cannot contradict the included count: 40 staged files = `<<FILL:included>>` (n, the four
  candidates at most) + 4 already held + 1 duplicate-target amendment + 31 out of theme. With all four
  admitted the arithmetic is 4 + 36 = 40; a Gate rejection moves a candidate into excluded.
- The 35 collisions are lane ids S859–S893 already occupied; every adopted citation is therefore
  re-pointed **by document** to a lane id, and no campaign-namespace id may appear in an entry or a row.
- The round's before-state check, scoped as it must be to the knowledge corpus:
  `git grep -l -E 'GB/T 33661' 98c486b -- corpus/knowledge` and
  `git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus/knowledge` each print nothing (exit 1), so
  neither the standard nor the archives' era-name table is held as knowledge at base. **Do not write the
  `-- corpus` form the claim text uses:** at base that matches `corpus/lessons/round-68.md` and
  `corpus/lessons/round-69.md` for `GB/T 33661` (exit 0) and `corpus/lessons/round-68.md` for
  `digital.archives.go.jp` (exit 0), because the lessons discuss the package row by name. The claim's
  before-state leg is true of the knowledge corpus and false as literally written; the installer must
  restate the command, not the expectation.

---

## 3. Measured counts and their commands (all re-runnable, read-only)

```
# staged knowledge files in the package, and per partition
find /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge -type f -name '*.md' | wc -l
# -> 40
for d in $(find /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge -mindepth 1 -maxdepth 1 -type d | sort); do
  printf '%s %s\n' "$(basename $d)" "$(find $d -type f -name '*.md' | wc -l)"; done
# -> culture-material 9, linguistics 17, myth-symbol 5, verification 9

# package id census (lane-supplied copies)
wc -l <kotodama-shokunin/.ufo/waves/round-76/assimilation/staged-ids     # 132
wc -l <kotodama-shokunin/.ufo/waves/round-76/assimilation/reg-ids        # 817
wc -l <kotodama-shokunin/.ufo/waves/round-76/assimilation/collisions     # 35

# which staged culture-material files the lane already holds at base
git -C kotodama-shokunin ls-tree -r --name-only 98c486b corpus/knowledge/culture-material \
  | sed 's|.*/||' | LC_ALL=C sort                                    # 40 names
comm -12 <staged sorted> <held sorted>                               # 4 names (the already-held four)
comm -23 <staged sorted> <held sorted>                               # 5 names (the four candidates + one duplicate target)

# base culture-material count and heading
git -C kotodama-shokunin ls-tree -r --name-only 98c486b corpus/knowledge/culture-material | grep -c '\.md$'   # 40
git -C kotodama-shokunin show 98c486b:corpus/README.md | grep -n '^## culture-material/'                      # (40)

# before-state, knowledge-scoped: nothing held at base
git -C kotodama-shokunin grep -l -E 'GB/T 33661' 98c486b -- corpus/knowledge              # empty, exit 1
git -C kotodama-shokunin grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus/knowledge  # empty, exit 1
# the claim's unscoped form is NOT empty at base:
git -C kotodama-shokunin grep -l -E 'GB/T 33661' 98c486b -- corpus
# -> corpus/lessons/round-68.md, corpus/lessons/round-69.md (exit 0)
git -C kotodama-shokunin grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus
# -> corpus/lessons/round-68.md (exit 0)
```
