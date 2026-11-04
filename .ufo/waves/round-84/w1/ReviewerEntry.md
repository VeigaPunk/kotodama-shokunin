# ReviewerEntry — claim-D draft findings (round 84, w1)

Seat: ReviewerEntry · milestone r84-v1 · axes: depth, calibration. Lane base
`81499ee4`; operative freeze `7e6ee2f8` (r2; claim-D constants identical to r1 `e160a72e`).

Object: `.ufo/waves/round-84/w1/stage/ScribeEntryWitch/witchcraft-sorcery-accusation-institution.md`,
56,778 B / 281 lines, sha256 `675ad0767ddc9dce86aaa78cf3ec19fa26b861c8ec58690590a5f6d637beeb7e`.
Rows: `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/rows.md` (S914–S917 `mined`, S918 `rejected`), `gate.md`,
`S916.txt`, `recheck.md`.

Full review: `.ufo/waves/round-84/w1/stage/ReviewerEntry/review.md`.

## Frozen shape — PASS/FAIL (operative freeze r2)

| check | measured | floor | verdict |
|---|---|---|---|
| bytes | 56,778 | >= 16,000 | **PASS** |
| `## ` sections | 15 | >= 7 | **PASS** |
| `## 2. Six design decisions` + data rows | exact heading, 6 rows | exact + >= 6 | **PASS** |
| `## 3. Attested anchors` + bullets | exact heading, 43 bullets | exact + >= 20 | **PASS** |
| single-id rule | 0 malformed (one S-id per bullet) | every bullet exactly one | **PASS** |
| distinct ids | 25 | >= 4 | **PASS** |
| cited-lines lint | `CITED-LINES: 0 finding(s) in 1 file(s)` | 0 | **PASS** |
| table rows carrying an S-id | 0 | 0 | **PASS** |
| eight header markers | all present | all 8 | **PASS** |
| S914–S917 rows | 11 cells, `mined`, `opened 2026-11-04`, `used-by` names entry | all four | **PASS** |
| SOURCED | all four new ids cited | >= 3 | **PASS** |
| SEPARABLE | not gradable at the stage; draft is one entry file, rows are in the wave stage | own paths only | not graded |

**Stale-freeze caveat.** This seat's prompt names freeze `3ca2cf2` and the r0 headings (`## 2. The decision
table` / `## 4. Attested anchors`). The operative dispatch, scribe brief, lesson header and gate rows name r2,
and the draft is correct for r2. A counter run with `--freeze 3ca2cf2` would fail DECISIONS and ANCHORS on a
correct draft. The L1 must run every round-84 counter with `--freeze 7e6ee2f8` and record the stale r0 hash in
the calibration notes; do not renegotiate the entry to r0.

## Defects, ordered by severity

1. **HIGH — S915 is cited only outside its filed scope; its own anchor is never used.** Entry lines 50, 51, 62.
   The S915 row's scope is the *Malleus* criminal code (arrest on rumour, witnesses, no defence, torture,
   weeping test) plus the black/gray/white taxonomy; the entry cites three other Williams passages (children
   of tender years; Agnes/Odo earliest English case; Cupidity/malice informer). Required: broaden the S915
   row's `scope`/`teaches` to cover those passages and re-run the census validator, **or** add a bullet using
   the row's actual anchor and drop/narrow the three out-of-scope bullets. Dropping S915 still leaves
   S914/S916/S917 = 3 of 4, so SOURCED still passes.
2. **HIGH — the `- recheck:` cell contradicts the row cells.** Line 9 says "180 days per row — both Britannica
   articles…", but the rows are 365d/365d/180d/365d and only S914 is Britannica (S915 is Williams 1865).
   Required: "365 days for S914, S915, S917; 180 days for S916 — per the row cells."
3. **HIGH — the `- gap filled:` count is not derived from the quoted command.** Line 4 quotes the topic sweep
   `\b(witchcraft|sorcery|witch|sorcerer|malefic)\b` (17 lines / 10 files at base) but reports "19 matching
   lines across 11 files" (the `witches`-inclusive pattern). The frozen claim's own "19 times across 10 files"
   is also not reproducible with its frozen `surface_re` (22 occurrences / 12 files). Required: name the exact
   pattern that produced 19/11, or change the number to 17 lines / 10 files for the pattern quoted.
4. **HIGH — the §4 etymology claim has no registered row; its only source is the rejected S918.** Entry line
   118: "the translation 'sorcerer' is a later legal borrowing, and the word's root is divination, not harm."
   No §3 row teaches it; the 1911 Britannica "Sorcery" stub carrying it was filed as **S918 `rejected`**
   (rows.md line 5). Required: remove the etymology assertion or mark it `(to-verify)`; never base a claim on
   a rejected row.
5. **HIGH/MEDIUM — the 21 already-registered rows the entry cites are not added to their `used-by` cells.**
   S280, S295, S297, S349, S350, S381, S382, S403, S605, S610, S621, S622, S644, S645, S854, S901, S902, S903,
   S905, S909, S912. The lane's S904 row lists both citing entries, so the convention is to list every citing
   entry. Required (L1/rows seat): append `corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md`
   to each cited old row's `used-by`.
6. **MEDIUM — two S917 bullets are Scotland passages outside the row's scope, and their volume is wrong.**
   Entry lines 89, 94: the Sinclair retraction and the Mackenzie "she knew she would starve" passages are
   general-witchcraft/Scotland, not Essex/Salem; the page markers are `[i.350]`, so the loci should be
   **vol. i, p. 350**, not "vol. ii, p. 350/351". Required: broaden the S917 row's `scope`/`teaches` to cover
   them and correct the loci, or drop the two bullets.
7. **MEDIUM — the §2 prose names a column the table does not have.** Line 27: "The anchor column names the §3
   group…", but the table is `decision | options | default and threshold | failure if unset`. Required: add an
   `attested anchor` column or rewrite the sentence.
8. **MEDIUM — §1 and `- couples:` understate the amulets borrowing.** Lines 18 and 6 say the entry takes "only
   the word-set" from the amulets entry, but §3 cites S605, S610, S621, S622, S644, S645 for object
   definitions and counter-witchcraft practice. Required: say the entry takes the word-set **and** the
   counter-witchcraft practice as one counter-accusation example, one-way; or drop the object-practice
   bullets.
9. **MEDIUM — the S349 quote verifies but the row's scope cell does not name it.** Entry line 107; the quote is
   in Hunchman p. 109, but the S349 row's `scope`/`teaches` names only windigo commodification and the
   psychiatric misreading. Required: add the access-rights sentence to the row, or rephrase the bullet to the
   row's declared claim.
10. **LOW/MEDIUM — the S915 "first English judicial case" drops Williams's hedge.** Line 51; Williams says
    "The earliest judicial trial for the crime on record in England is said to have occurred…". Required:
    "the earliest recorded English case (Williams hedges: 'is said to have occurred')".
11. **LOW — the S914 "composite" gloss is stronger than the quoted sentence.** Line 49; the article says "a
    learned product", not "composite". Required: use the article's word or quote the fusion sentence.
12. **LOW — the §7 "weary of life" detail is sourced but not visibly anchored.** Line 175 paraphrases Upham's
    Sinclair declaration ("being weary of it, and choosing rather to die than live"), while the §3 S917 quote
    stops at "but, being delated by a malicious woman" with no ellipsis. Required: extend the S917 quote to
    include the "weary of it" clause (marking the cut), or add a pointer.
13. **LOW — the `- sources:` receipt pointer is not a resolvable repo-relative path.** Line 5 says "the
    round's wave evidence directory"; name `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/` instead.
14. **LOW — "four rows" hides the fifth (rejected) row the round opens.** Lines 4, 5, 8; the rows seat opened
    S914–S918 (four mined + one rejected), and the registry grows to 842. Required: "four mined rows
    (S914–S917) and one rejected candidate (S918)" once; the `>= 841` floor is still met.
15. **LOW / round-level — the seat prompt carries the superseded r0 freeze.** The draft is correct for r2; the
    prompt is not. Required (L1): run counters with `--freeze 7e6ee2f8` and record the stale r0 hash in the
    calibration notes.
16. **MEDIUM (row record) — the S916 "no capture" probe has no QUALITY 24 positive control.** `S916.txt` and
    `gate.md` record the CDX exact query returning `[]` (I reproduced it) but no same-query-shape probe over a
    URL known to have captures (the S914 Witchcraft page does). The URL is a direct subpage, not a front-door
    DOI, so the redirect-target limb need not apply — but that should be recorded. Required (rows seat/L1):
    add the positive-control probe and its non-empty output beside S916's `[]`.

## Boundary and PROVINCE

- **Canon handoff — PASS.** §15 hands off through `corpus/knowledge/synthesis/worldbible-integration-contract.md`
  ("Kotodama proposes; lore records"); the worked example is NON-CANON; `- scope:` repeats that canon belongs
  to lore.
- **Boundary file — PASS.** Named in `- couples:` and `- scope:`; §11 marks the 1911 three-period scheme,
  functionalism, the learned/popular split, victim totals and retro-diagnosis as contested/period; §12/§15
  carry the negative list (no living-community names, no restricted motifs, no charges against persons).
- **Living-community claims — PASS with defect 9.** The Kongo/Antonian material is historical and §1 says "makes
  no claim about Kongo"; S349/S350 are boundary anchors.
- **Chousa/kagi ground — PASS.** Design synthesis, not research method or rights ruling; no permission decision.
- **No accusation instructions — PASS.** Every lever is framed as a design choice; the `- topic:` and
  `- scope:` lines say it is not a procedure for use on any person.

## Verified positives

- All **19 quotes from the four mined rows verify exactly once** in the served bytes (S914 7, S915 3, S916 3,
  S917 6).
- Row digests match independent fetches: S914 `68511af9…` (98,968 B), S915 `88407510…` (450,230 B), S916
  `cc7b7d31…` (73,365 B), S917 `925e3634…` (1,801,648 B), S918 `2c4092db…` (60,730 B).
- Captures: S914 86,021 B / `945d377f…`; S915 450,230 / `88407510…`; S917 1,801,648 / `925e3634…`; S916 CDX
  returns `[]`.
- Five rows pass a faithful `sources-census.sh validate` mirror at rc 0 (only pre-existing W04/W01 warnings
  outside claim D; no E01–E12 for S914–S918).
- §3 single-id discipline and the no-table-id rule hold (`CITED-LINES: 0 finding(s) in 1 file(s)`).

## Residual risk

- The Williams (1865) print page numbers cannot be checked against the Gutenberg text (footnote numbers, not
  pages); the chapter attributions are correct.
- The 21 old rows were checked against their `scope`/`teaches` cells, not every underlying source page.
- The entry's "every §3 quote was re-checked" is a process claim; I independently verified the new-row quotes.
- The r0/r2 freeze mismatch is a round-level bookkeeping risk, not a draft defect.
