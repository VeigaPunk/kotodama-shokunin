# ScribeLessonFinal — round 75, wave 2 (kotodama-shokunin)

Seat: scribe. Deliverable: the round-75 lesson, **staged** at
`.ufo/waves/round-75/w2/stage/corpus/lessons/round-75.md` (365 lines, 40396 B, sha256
`29bf7715d758abbba3b440e7bdd4b63f0e38d3fb1bfd7ae9171b949b99e573d1`). Nothing was committed: only the
L1 commits and applies.

## Behaviour

- Read the shape sources (`corpus/lessons/round-74.md`, `round-73.md`), the w1 draft
  (`.ufo/waves/round-75/drafts/lesson.md`), `CORPUS.md` §SOURCES contract, `LEARNING.md`, and the prompt
  §2b and §6 item 10. Wrote the lesson against the two claims as staged in `reports/round-75/claims.json`
  and the ledger as staged in `reports/round-75/ledger.json`; **edited neither**.
- Re-derived every count the lesson asserts, from bytes, rather than copying the draft:
  40 staged files (`find … | wc -l`, split culture-material 9 / linguistics 17 / myth-symbol 5 /
  verification 9) and the triage line **40 staged .md files in merge/kotodama/knowledge: 3 adopted /
  6 path-present / 31 refused of the 40 (3 + 6 + 31 = 40)**, per the L1's pre-data direction: path-present
  6 = heritage-taxonomy-models ×2, worldbuilding-setting-practice ×2, conlang-scholarship.md and its
  `.amend-2026-10-23.md`; refused 31 = naming-systems 11 + verification 9 + calendar-festival 3 +
  era-periodization 2 + conlang-scholarship amendments 3 + conlang-methodology 1 + narrative
  amend-2026-10-23c and amend-2026-10-24 (2); the four files under `merge/kotodama/amendments` are outside
  the 40; the six path-present sha256 pairs (staged vs `git show <base>:<path>`); the 21-row
  quarantine slice with the prompt's own `awk`; the three guard artifacts (`wc -l`, ranges, sha256,
  `grep -c` for S885–S893 in `reg-ids` and `collisions`); registry and knowledge-file counts at base
  (808 / 249) and the zero `narrative` match; the round-74 S899/S900 correction (four `git grep -c`
  probes, all four reproduced).
- Quote discipline: each Gate quote is copied from the row's `anchor` cell in
  `.ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md`, then tested against the receipt that
  exists for that row (NFKC + whitespace fold, window and full text). Two rows have no receipt and say so.
- Read-only git only (`git show`, `git grep`, `git ls-tree`, `git cat-file -e`, `git status`); no git or
  jj mutation, no fixture, no clone, no scratch left behind
  (`/fast/scratch/hyaku/kotodama-r75/ScribeLessonFinal` was created and removed inside one call).
- No tools installed; no `pacman`; nothing written outside the two paths named below.

## Gates

| gate | status |
|---|---|
| lesson sections (`## Gate`, `## Quarantine`, `## Collision guard`, `## Normalization`, `## Census`, `## Mistakes`, `## Routed to round 76`, `## Sources & frontier`, `## Corrections`) | all nine present (`grep -c '^## '` → 9) |
| `## Gate` per row: URL, access date 2026-10-27, quote ≤25 tokens and ≤80 chars, locator, ≥1 admit, ≥1 reject | 9 rows, longest quote 77 chars / 12 tokens; 9 admits, 4 rejects each with probed URL + reason + flip |
| quotes equal the row's `anchor` cell | 9/9 by copy; locatable in the receipt for 5/7 probed rows, **not** for S888 and S892 (finding F2) |
| `## Quarantine` standing 21-row slice, re-derived | 21 lines, PRESENT 10 / REFUSED 7 / UNVERIFIABLE 4, re-counted from `reports/round-71/telemetry/quarantine-verdicts.md` |
| `## Collision guard` | reg-ids 808, staged-ids 132, collisions 26 (S859..S884), adopted S885–S893 absent from both reg-ids and collisions, guard proof pasted (1/2/3-space found, 4-space/tab not, column-zero control 0 of 3) |
| `## Census` before | exit 0, 808 rows (`census-start.txt`) |
| `## Census` after | the literal line `CENSUS-END: <filled by the L1 at landing>`; no other placeholder token in the file (`grep -oE` scan: one `<filled`, that line) |
| `## Sources & frontier` | 808 → 817 rows, tiers A×3 / B×5 / C×1 verified against the nine row cells; `considerthese` absent (`ls considerthese` → no such directory) |
| `## Corrections` | round-74 S899/S900 reclassified adopt-with-renumber, append-only, round-74.md untouched |

## Touched surfaces

Wrote exactly two files:

1. `.ufo/waves/round-75/w2/stage/corpus/lessons/round-75.md` — the staged lesson.
2. `.ufo/waves/round-75/w2/ScribeLessonFinal.md` — this report.

Read-only: `kotodama-shokunin` lane tree (base `f556d1049fe651d3d63975600b13acd9fb686f15` =
HEAD, plus untracked wave/report dirs), `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge`
(the 40 staged files, read only) and `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/
absent-defect-register.md` (read only), `/home/vgpnk/Projects/shokunin/CORPUS.md`, `LEARNING.md`,
`.ufo/prompts/kotodama-round-75.md`, `.ufo/watchdog.log` (line 1778).

## Findings

1. **The scratch mirror carries two of the three entries (highest impact, pre-freeze).**
   `assimilation/validate/corpus/knowledge` holds 251 files and **no** `…amend-2026-10-23b.md`
   (`find .ufo/waves/round-75/assimilation/validate -name '*23b*'` → 0; only
   `narrative-structure-frameworks.md` and `…amend-2026-10-23.md` are present). Claim C's `entries` lists
   three paths and its `after` says "knowledge files 249 → 252", while `validate-receipt-draft.txt` says
   "mirror knowledge files 251 / lane 249" and its README check prints total 251 with
   `myth-symbol 31`. Consequence: the SCRATCHMIRROR leg ("a mirrored corpus carrying the frozen rows
   **and entries**") and the INDEX leg's `myth-symbol (32)` are not satisfied by the mirror as it stands.
   The mirror must be rebuilt with the third entry before its receipt is citable. Observed, not repaired
   (not my path).
2. **The probe receipts bind a `quote:` that is not the row's anchor span.** All seven probed rows carry
   a title or a 1–2 character token (`S885` "Introduction à l'analyse structurale des récits", `S888`
   `叙事学`, `S889` `narrative`, `S890` `物語`, `S892` the dossier section title), so a receipt cannot
   verify the Gate quote. The anchor quotes are findable in the stored windows for S885/S886/S887/S889/
   S890 (folded, one hit) and are **absent** from the windows for S888 (window `chars=4097 before=10`)
   and S892 (`chars=4097 before=284`); the full bodies do carry each once
   (`validate-receipt-draft.txt`, `EVIDENCE-LOCATE PASS`, hits=1 for all nine). Recorded as lesson row
   R75-M2; the evidence files at `reports/round-75/evidence/` must window p. 3 and p. 7 respectively.
3. **The Persée notices are not byte-stable, and the drift includes length.** Three stored observations of
   the S885 URL disagree: w1 seat fetch 111487 B `9be2c68d…`, probe receipt 111486 B `2bcdd019…`, mirror
   rehearsal 109589 B `25cfd7f6…`. The mirror receipt's note ("same length, different sha256") is false
   of these three. Same class for S886 (109335 / 111234) and S887 (118776 / 118777). The lesson cites the
   probe receipts and names no byte count as canonical.
4. **One `source:` line's URL is hard-wrapped mid-percent-escape.** `…amend-2026-10-23.md:11` ends
   `…2014%20marrone%20age%` and line 12 continues `  dor---2.pdf — …`, so the mirror's own REPOINTED
   cross-check prints `match: False` for S892 against `True` for the other eight. Line-scoped readers
   (census, REPOINTED, any `source:` parser) see a URL that names no document.
5. **The w1 draft's claims line is stale against the staged ledger.** Draft: "eleven ledger pairs
   (4 REPAIR, 7 ANNOTATE)". `reports/round-75/ledger.json`: **10 pairs, 6 REPAIR / 4 ANNOTATE**
   (L75-01…L75-10). Ca's LEDGER leg requires ">= 10 unique pairs", so 10 passes. The lesson's claims line
   uses the ledger's own counts; recorded as R75-M3.
6. **The quarantine `awk` emits three ids with a trailing backtick.** The three unreachable-class register
   rows print `S807\``, `S812\``, `S835\`` (their class cell has no leading space). The slice count is
   still 21 and every line carries an id, but a consumer that trims whitespace only keeps the backtick.
   Noted in `## Quarantine`.
7. **S891 and S893 have no probe receipt** (`counters/probe-receipts/` holds S885–S890 and S892 only).
   Both are admitted on their row anchors with the capture recorded in `validate-fetch/W891.meta` /
   `S893.meta` and `validate-receipt-draft.txt`; `ScoutUnigeSZ.md` recommends a *different* clause of the
   same paragraph as its Gate span, and `ScoutChinawriter2023.md` carries only the first 27 characters of
   S893's 39-character span. The lesson says both are "not yet captured" as receipts.
8. **Register S787 and lane S893 are the same document.** Register S787 =
   `https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html`, verdict REFUSED (span absent);
   lane S893 registers that document with a fresh quote. The register stays REFUSED; the separation is
   recorded and routed (the register is read-only, so no pointer was written there).
9. **Working-tree state, not graded.** `git status --porcelain` shows ` M SHONEN.md`, ` M SKILL.md`,
   ` M reports/round-28/readme/sweep.py`, `?? .ufo/waves/round-75/`, `?? reports/round-75/`. These are
   uncommitted edits and the round's untracked files; the lesson grades none of them, and HEAD equals the
   base revision (`git cat-file -e HEAD:reports/round-75/claims.json` → absent).

## Out of scope / not done

- No source re-fetched: the four reject rows' numbers are attributed to the seats that recorded them
  (`w1/SentinelScope.md` S-75-9, `w1/ScoutPersee1120.md`, `w1/ScoutUnigeSZ.md`,
  `w1/ScoutChinawriter2023.md`) and are not upgraded to this seat's execution evidence.
- No counter run (`accept-c.py`, `accept-ca.py`), no selftest, no census-at-round-end: those are the L1's
  landing steps; the `CENSUS-END` line is the literal placeholder the L1 replaces.
- No edit to `reports/round-75/claims.json`, `ledger.json`, `corpus/SOURCES.md`, `corpus/lessons/
  round-74.md`, the mirror, or any wave-1 file.
- No git/jj mutation anywhere, no fixture, no delegation, no background job.
- The six path-present byte decisions, R74-M5's register adjacency guard, the S877 scope-cell supersede
  row and the R74-M3/M4/M6/M7/M8 + closure R1/R3/R4 items are routed, not closed.
