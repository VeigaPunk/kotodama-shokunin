# ScribeReadmeIndex — round 74 wave 1 — corpus/README.md draft for claim C

Seat: ScribeReadmeIndex (leaf; no dispatch, no subagents, no background jobs). Date: 2026-10-25.
Item: draft the `corpus/README.md` changes for claim C at
`.ufo/waves/round-74/drafts/readme-rows.md` — index rows for the two new culture-material
entries, an append-only dated footer line for after landing, a `## Known gaps (frontier)` note —
and say whether the lane root `README.md` needs a line.

Lane HEAD at read time: `f7104cbce186bc2e1522abf0cfd619cc834628bb` = the round's base
(`git rev-parse HEAD`). `corpus/README.md` and `README.md` are byte-identical to the base after
this seat: `git diff --stat -- corpus/README.md README.md` prints nothing.

## 1. Deliverable

`.ufo/waves/round-74/drafts/readme-rows.md` — 283 lines, 19,256 bytes, sha256
`b824a0528786c0af1265345d8cc6fe27c54766477382e127cf20a414f6a1fabe`. It contains, in patch
order:

1. **Index rows** — two rows for the `## culture-material/` section, inserted at `:444`/`:445`
   (after `writing-media-surface-economy.md`, before `## synthesis/ (29)`), in filename order
   (`…amend-2026-10-23.md` first: `LC_ALL=C sort` and the default locale both put `a` before `m`
   at the first byte after `practice.`). Each row is `` - `<name>` — <entry's own `- topic:`
   text> ``, byte-for-byte; measured equal to the drafts' `- topic:` strings for both entries
   (row lengths 485 and 338 characters with the prefix; topic strings 283 B/44 tokens and
   445 B/65 tokens). The amendment's topic keeps its terminal full stop; the base row gets none
   added.
2. **Frontier note** — two bullets appended after `:730` (the last existing bullet, `- Round 65
   adds …`) inside `## Known gaps (frontier)`: what landed (the entry and its amendment) with
   the at-base zeros, the partial one-way owners, and the remaining staged families with counts
   (naming-systems 11, calendar 3, era 2, verification 9, narrative-structure 5) plus pointers to
   `corpus/lessons/round-73.md` `## Routed to round 74`.
3. **Footer** — appended at end of file after `:777`: a `## Round 74 landing (appended
   2026-10-25, hyaku run 7)` block, `Total knowledge entries: 249.`, and a three-line
   `Counts checked` block in the shape `FOOTER_RE` (`reports/round-28/readme/sweep.py:66-72`)
   matches — the command `find corpus/knowledge -type f -name '*.md' | wc -l`, vector
   `32/29/40/29/24/95` — then the index-rows remeasurement line. Nothing above `:777` is edited.

Lane root `README.md`: **no line needed** (draft §5). It carries no counts, no entry list and no
pointer to `corpus/README.md`; the landing changes no domain sentence, trigger or owned surface.
Reasoned, not guessed: the file is 14 lines and was read whole.

## 2. Commands run, with outcomes

All read-only except the two writes named in §1/§4.

```
$ git -C <lane> rev-parse HEAD                      -> f7104cbce186bc2e1522abf0cfd619cc834628bb
$ git -C <lane> status --porcelain=v1               -> 5 M + 1 ?? under .ufo/waves/round-73/w2/
                                                       (inherited, untouched), ?? .ufo/waves/round-74/,
                                                       ?? reports/round-74/
$ find corpus/knowledge -type f -name '*.md' | wc -l                        -> 247
$ for d in linguistics myth-symbol culture-material synthesis verification \
      civilizations; do find corpus/knowledge/$d -maxdepth 1 -name '*.md' | wc -l; done
                                                                            -> 32 29 38 29 24 95
$ python3 -B reports/round-28/readme/sweep.py                               -> exit 1
    rows 245 files 247
    missing_from_index 4  (the two culture-material heritage-taxonomy-models files and the two
                          round-73 conlang-scholarship rows — written here in shorthand, the
                          tool prints full paths on four lines)
    orphan_rows 2  (the two round-73 conlang-scholarship rows, attributed to civilizations)
    topic_mismatch 0
    header_drift {"culture-material": {"declared": 36, "files": 38},
                  "linguistics": {"declared": 30, "files": 32}}
    totals_line 243 footer {"total": 243, "dir_totals": [30,29,36,29,24,95]}
    footer_live {"total": 247, "dir_totals": [32,29,38,29,24,95]}
    readme_sha256 52fd7536e1bf41ff019115e7c9e37eb15fb64e44d06c5f299fdcc7443a433d91
$ git ls-tree -r --name-only f7104cb corpus/knowledge | grep -ciE 'worldbuilding|setting'  -> 0
$ git grep -lE '設定ノート|世界観|世界观|設定資料集' f7104cb -- corpus/knowledge | wc -l    -> 0
$ git show f7104cb:corpus/SOURCES.md | grep -c {litmemo.com|tuduku.space|chinawriter.com.cn}
                                                                            -> 0 0 0
$ find <staged>/knowledge/corpus/knowledge -name '<family>*' | wc -l
    naming-systems 11, calendar-festival-systems 3, era-periodization-models 2,
    narrative-structure-frameworks 5 (1 base + 4 amendments)
$ find <staged>/knowledge/corpus/knowledge/verification -name '*.amend-*' | wc -l -> 9
    (7 amend citation-format-and-source-registry.md, 1 journal-serial-catalogue-records,
     1 reopen-gate)
```

Scratch simulation (the only way to measure the drafted footer before a landing commit exists):
the whole lane was copied to `/tmp/ScribeReadmeIndex/lane`, the two draft entries copied into
`corpus/knowledge/culture-material/`, this draft's patch applied to that copy only, and its
`reports/round-28/readme/sweep.py` (copied, unmodified) run:

```
before patch: footer_live {"total": 249, "dir_totals": [32,29,40,29,24,95]}
              header_drift culture-material 36 vs 40, linguistics 30 vs 32
after patch:  rows 247 files 249, topic_mismatch 0,
              missing_from_index 4 (the two heritage files + the two round-73 conlang rows),
              orphan_rows 2 (the conlang pair), totals_line 243, footer_ok False,
              readme_sha256 ee2b68543d8d92f8e40c0caec31219a26c4670e8abf9b4c2cef040eedeff6a61,
              exit 1
```

The scratch lane was deleted afterwards. Nothing was downloaded; no network call was made; no
tool was installed or upgraded (none was needed). Fidelity: after the run, one prose sentence
inside the drafted block was reworded (which older footer reading is which); the lines any leg
parses — `Total knowledge entries: 249.` and the three `FOOTER_RE` lines — are unchanged from
the simulated bytes, and the draft says so in §3. `/tmp` had no room to rebuild the copy.

## 3. Findings

- **F1 — the README sweep reads the FIRST total/footer, not the last.** `TOTALS_RE.search` takes
  the first `Total knowledge entries: N.` (currently `:732`, 243) and `footer_reading` the first
  matching `Counts checked` block (`:734-736`, 243 / 30-29-36-29-24-95). With an append-only
  footer convention, `totals_ok` and `footer_ok` therefore can never go true again by appending;
  they will read 243 vs 249 after this landing. The draft states this in the footer prose instead
  of pretending the append repairs the instrument. This is a calibration/ledger surface for claim
  Ca, not a claim-C defect.
- **F2 — `## Round 73 additions (appended …)` is not a partition to the sweep.** `SECTION_RE`
  needs `^## ([a-z-]+)/ \((\d+)\)$`, so the civilizations section runs to end of file and the two
  round-73 `conlang-scholarship` rows are reported as `orphan_rows` under `civilizations` and as
  `missing_from_index` under `linguistics`. Measured, not inferred (before and after the patch).
  Consequence for this draft: the after-state `missing` count is 4, not 2 — named in the drafted
  footer line so no reader mistakes it for two brand-new holes. Any future appended index rows
  will inherit the same misattribution; the draft puts no rows there.
- **F3 — culture-material heading is stale by two today and four after landing** (declared 36;
  38 files now, 40 after the two entries land). Round 71's revision 2.21 fixed exactly this class
  in place ("the header was stale at 34 against 35 files; the landing fixes it"); round 73's
  addition left its heading as filed ("append-only: an in-place heading edit would be a rewrite").
  The draft assumes "leave as filed", names the stale, and gives the exact replacement line
  (`## culture-material/ (40)`) for a lander who rules the other way. The round-73 Ca ledger
  pairs L01-L03 already record the 36-vs-38 stale, so either choice is auditable.
- **F4 — two culture-material files are unindexed and not this seat's to invent rows for**:
  `heritage-taxonomy-models.md` and its `amend-2026-10-24-r13.md` (landed by an earlier round
  without rows). The draft names them in the gap note instead of claiming 40/40 coverage.
- **F5 — two staged families cannot be adopted by amendment alone.** The nine staged
  `verification` files amend three documents, but the lane holds only
  `citation-format-and-source-registry.md`; `journal-serial-catalogue-records.amend-2026-10-24-r16.md`
  and `reopen-gate.amend-2026-10-24.md` have no base in `corpus/knowledge/verification/`. Likewise
  `narrative-structure-frameworks` is a staged base + 4 amendments and the lane has no
  `myth-symbol/narrative-structure-frameworks.md`. The routed plan ("one family per round with
  by-document re-pointing") therefore needs a base-document decision before those two families
  can land, or the amendments have nothing to amend.
- **F6 — family counts reproduce unevenly, so the bullets state their commands.** `naming-systems`
  11 / `calendar` 3 / `era` 2 / `narrative-structure` 5 are `find -name '<family>*' | wc -l`
  results (all amendments for the first three; base+4 for the last). `verification` is 9 only
  under `find ./verification -name '*.amend-*'`; the naive `-name 'verification*'` matches the
  directory itself and returns 1 — the bullet names the correct command per family.
- **F7 — environment: `/tmp` is 100% full.** `df -h /tmp` → 128G size, 128G used, 280K→8.4M
  available; a 2 KB redirect failed with `No space left on device` mid-run. My scratch copy was
  8.1 MB and has been deleted (freed to 8.4M). Not caused by this seat's work as far as the
  numbers show, but downloads in `/tmp` are at risk for every seat.
- **F8 — filename order differs from the round-73 presentation.** The only base+amend pair
  already indexed (round 73's `conlang-scholarship`) is presented base-then-amend inside an
  appended section, which is not strict filename order. The draft keeps strict order and records
  that the sweep is order-agnostic (`parse_readme` set comparison), so a lander may swap without
  changing any measurement.

## 4. Touched surfaces

- Written: `.ufo/waves/round-74/drafts/readme-rows.md` (this seat's draft; new file).
  Report: `.ufo/waves/round-74/w1/ScribeReadmeIndex.md` (this file).
- Scratch, created and deleted: `/tmp/ScribeReadmeIndex/` (lane copy, two draft entries, copied
  `sweep.py`, patched README copy). No download directory was needed.
- Read only: lane `corpus/README.md`, `README.md`, `corpus/knowledge/**` (listing/counting),
  `reports/round-28/readme/sweep.py`, `reports/round-74/claims.json`,
  `reports/round-74/telemetry/census-start.txt`, `.ufo/waves/round-74/**` (peers' wave-1 files,
  read for provenance only), `corpus/lessons/round-73.md`, and the staged package under
  `/home/vgpnk/Projects/shokuknow/merge/kotodama/` (`find`/`ls` only).
- Not touched, by instruction or by scope: `corpus/README.md`, the lane root `README.md`,
  `corpus/SOURCES.md` and its rows, `SKILL.md`, `LOG.md`, `SCORECARD.md`, `PROVINCE.md`,
  `corpus/QUALITY.md`, `corpus/lessons/**`, `corpus/knowledge/**`, `reports/round-74/claims.json`,
  the six inherited round-73 w2 files, the fleet root `/home/vgpnk/Projects/shokunin/**`, the
  lane git index/JJ state, and `/home/vgpnk/Projects/shokuknow` (read-only; no campaign tool run
  there). No `git add`, no commit, no counter, no gate.

## 5. Out of scope / handed back

- The landing edit itself (rows, frontier bullets, footer) belongs to the seat that lands claim C;
  this seat only drafted it.
- `corpus/SOURCES.md` registry rows S881-S884: another seat's write path. The drafted footer says
  "804 → 808 rows" — that is claim C's `row_set` (four rows) and the base census reading, not a
  measurement this seat made; the after-census receipt is the executor's.
- The `## culture-material/ (36)` heading, a `revision: 2.22` head block, and the sweep's
  first-footer semantics (F1) need a ruling; the draft gives exact text for the first two and
  leaves all three unwritten.
- Nothing here scores landed data; claim C's counter (`accept-c.py`) was not run and its legs are
  not claimed by this seat.
