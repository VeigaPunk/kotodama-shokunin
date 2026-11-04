# ReviewerEntry — claim-D draft review (round 84, w1)

Seat: ReviewerEntry · milestone r84-v1 · axes: depth, calibration.
Object reviewed: `.ufo/waves/round-84/w1/stage/ScribeEntryWitch/witchcraft-sorcery-accusation-institution.md`,
56,778 bytes, 281 lines, sha256 `675ad0767ddc9dce86aaa78cf3ec19fa26b861c8ec58690590a5f6d637beeb7e`
(mtime 2026-11-04 10:43:39 -0300; stable across a 40 s re-read before this file was written).
Rows reviewed: `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/rows.md` (five rows: S914–S917 mined, S918 rejected)
and its `gate.md` / `S916.txt` / `recheck.md`.

Verdict: the draft clears the **operative** frozen shape (freeze r2 `7e6ee2f8`, whose claim-D constants are
identical to r1 `e160a72e`). It does **not** clear the lane's own bar on provenance and scope: one new row
(S915) is cited only for passages outside its filed scope, two more (S914, S917) are partly over-broadened,
one claim uses a rejected row's source, and three header cells contradict the rows they summarise.

## 1. Frozen shape — explicit PASS/FAIL

Operative freeze: `7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2` (HEAD; the round lesson header names r2 and the
`SKILL.md` gate rows pin r2). Claim D's constants are `## 2. Six design decisions` / `## 3. Attested anchors`
and are identical at r1 and r2.

| check | measured | floor | verdict |
|---|---|---|---|
| bytes | 56,778 | >= 16,000 | **PASS** |
| `## ` sections | 15 | >= 7 | **PASS** |
| decision heading exact + data rows | `## 2. Six design decisions`, 6 rows | heading exact, >= 6 | **PASS** |
| anchor heading exact + bullets | `## 3. Attested anchors`, 43 bullets | heading exact, >= 20 | **PASS** |
| anchor single-id rule | 0 malformed; each `- ` bullet carries exactly one S-id | every bullet exactly one | **PASS** |
| distinct anchor ids | 25 (S280…S917) | >= 4 | **PASS** |
| cited-lines lint | `CITED-LINES: 0 finding(s) in 1 file(s)`, rc 0 | 0 findings | **PASS** |
| no table row carries an S-id | lint TABLE-ID = 0 | 0 | **PASS** |
| eight header markers | all present in house order | all 8 | **PASS** |
| rows S914–S917 | 11 cells each, `mined`, `opened 2026-11-04`, `used-by` names the entry | all four | **PASS** |
| SOURCED | cites S914, S915, S916, S917 | >= 3 of 4 | **PASS** |
| SEPARABLE | not gradable from the stage (needs a lands revision); the draft is one entry file and the rows are in the wave stage, so no O-claim path is touched | own paths only | **not graded** |

**Stale-freeze caveat (binding).** The seat prompt and the wave prose copied into this seat name freeze
`3ca2cf288fb593618e0559ea86a36e2dd3110eb8` (r0) and the headings `## 2. The decision table` /
`## 4. Attested anchors`. A counter run with `--freeze 3ca2cf2` would **FAIL** DECISIONS and ANCHORS on this
draft even though the draft is correct for the operative r2 freeze. The dispatch (`w1-dispatch.json`), the
scribe brief, the lesson header and the gate rows all name r2; r0 is superseded. The L1 must run every
round-84 counter with `--freeze 7e6ee2f8` and record the stale r0 hash in the calibration notes. Do not
renegotiate the entry back to r0 headings.

## 2. Defects, ordered by severity

### D1 — HIGH — S915 is cited only outside its filed scope, and its own anchor is never used

**Locations:** `.ufo/waves/round-84/w1/stage/ScribeEntryWitch/witchcraft-sorcery-accusation-institution.md`
lines 50, 51, 62; row S915 in `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/rows.md` line 2.

**Evidence.** The S915 row's `scope` is "the Malleus Maleficarum's criminal code as the accusation grammar
(arrest on rumour, infamous witnesses, no defence, torture and the weeping test) and the black, gray and white
witch taxonomy"; its `anchor` is the arrest-on-rumour sentence. The entry cites S915 three times, and every
citation is a different Williams passage: the "children of tender years" passage (Part II, ch. I), the
"Agnes / Odo" earliest-English-case passage (Part II, ch. II), and the "Cupidity or malice" informer passage
(Part II, ch. II). None is the Malleus criminal code or the witch taxonomy, and the row's own anchor quote is
never cited. This is the exact failure the seat brief asks to check: the new rows are not cited for material
they actually teach.

**Required edit.** Either (a) broaden the S915 row's `scope` and `teaches` to name these three passages and
re-run `sources-census.sh validate` on the mirror, or (b) add a bullet using the row's actual anchor (the
arrest-on-rumour rule) and drop or narrow the three out-of-scope bullets. If S915 is dropped entirely, the
entry still cites S914, S916 and S917 — 3 of 4 — so the SOURCED leg still passes.

### D2 — HIGH — the `- recheck:` cell contradicts the row cells

**Location:** entry line 9.

**Evidence.** The line reads "180 days per row — both Britannica articles are 1911 surveys…". The row cells
are `365d` (S914), `365d` (S915), `180d` (S916), `365d` (S917). There is only one Britannica row (S914);
S915 is Howard Williams, 1865, not a Britannica article.

**Required edit.** Replace with: "365 days for S914, S915 and S917; 180 days for S916 — per the row cells.
S914 is a 1911 Britannica survey, S915 is Williams 1865, S916 is a 1484 bull in a 1928 translation, S917 is
Upham 1867."

### D3 — HIGH — the `- gap filled:` count is not derived from the command it quotes

**Location:** entry line 4.

**Evidence.** The bullet quotes the topic-line sweep
`grep -rlE '^- topic: .{0,160}\b(witchcraft|sorcery|witch|sorcerer|malefic)' corpus/knowledge`. At base
`81499ee4` that pattern matches **17 lines in 10 files** (19 term occurrences). The bullet reports "19
matching lines across 11 files", which is the count of the `witches`-inclusive pattern
`\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b`. The frozen claim's own "19 times across 10 files"
is also not reproducible with its frozen `surface_re` (22 occurrences in 12 files), so it cannot be copied
either.

**Required edit.** Name the exact pattern that produced 19/11 (add `witches` to the quoted alternation), or
change the sentence to "17 matching lines across 10 files (19 term occurrences)" for the pattern actually
quoted. Whichever is chosen, the owning-surface conclusion (0 owning basenames, 0 owning topic lines) is
unaffected.

### D4 — HIGH — the §4 etymology claim has no registered row, and the only source carrying it is the rejected S918

**Location:** entry line 118 (the "sorcerer" row of the §4 vocabulary table).

**Evidence.** "the translation 'sorcerer' is a later legal borrowing, and the word's root is divination, not
harm" is a factual claim about English etymology. No §3 row teaches it. The only page in the round's candidate
set that carries the etymology is the 1911 Britannica "Sorcery" stub, which the rows seat filed as **S918 with
status `rejected`** (`rows.md` line 5: "printed 71-word dictionary stub, definition only"). The entry does not
cite S918, and the entry's `- sources:` line limits authority to the §3 rows.

**Required edit.** Remove the etymology assertion, or mark it `(to-verify)` and rephrase it as a design
caution ("a world should decide what its charge-word descends from; do not inherit English's"). Never base an
entry claim on a rejected row's source.

### D5 — HIGH/MEDIUM — the 21 already-registered rows the entry cites are not added to those rows' `used-by` cells

**Locations:** `corpus/SOURCES.md` rows S280, S295, S297, S349, S350, S381, S382, S403, S605, S610, S621, S622,
S644, S645, S854, S901, S902, S903, S905, S909, S912.

**Evidence.** Every one of those rows' `used-by` cell names only its owner entry (e.g. S621/S622 name
`amulets-talismans-apotropaic-marks.md`; S901–S903 name `ordeal-judicial-proof-rituals.md`). The lane's own
S904 row lists **both** entries that cite it (`guest-right-hospitality-law.md`,
`marriage-alliance-bridewealth.md`), so the convention is to list every citing entry. As landed, the registry
will read as if these 21 rows are unused by the new entry, and the entry's `- sources:`/`- couples:` claims
will not be traceable through the registry.

**Required edit (L1 / rows seat, not the entry scribe).** Append
`corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md` to the `used-by` cell of each cited
old row. If the lane deliberately keeps `used-by` to the owner entry, record that convention in the round
report/lesson; the current S904 precedent says otherwise.

### D6 — MEDIUM — two S917 bullets are Scotland passages outside the row's scope, and their volume is wrong

**Locations:** entry lines 89, 94; row S917 in `rows.md` line 4.

**Evidence.** The S917 row's `scope` is "the slander law around the word witch in the Essex County Court, and
the social functions of the Salem accusation". The retraction bullet (Sinclair) and the "being defamed for a
witch, she knew she would starve" bullet (Mackenzie) are Scotland / general-witchcraft passages in Upham's
Part Second, not Essex/Salem. The page markers confirm the passages sit at `[i.350]`: line 89 says "vol. ii,
p. 350" (volume wrong, page right) and line 94 says "vol. ii, p. 351" (volume wrong; the quoted sentence is at
vol. i, p. 350).

**Required edit.** Broaden the S917 row's `scope`/`teaches` to include the Sinclair/Mackenzie retraction and
social-death passages and correct the loci to vol. i, p. 350; or drop the two bullets.

### D7 — MEDIUM — the §2 prose names a column the table does not have

**Location:** entry line 27.

**Evidence.** "The anchor column names the §3 group that supplies the material, never a row id." The §2 table's
columns are `decision | options | default and threshold | failure if unset`; there is no anchor column.

**Required edit.** Add an `attested anchor` column pointing to the §3 sub-groups, or rewrite the sentence to
"The §3 groups supply the material; this table carries no row ids."

### D8 — MEDIUM — §1 and `- couples:` understate the amulets borrowing

**Locations:** entry line 18 (§1) and line 6 (`- couples:`, the amulets clause).

**Evidence.** Both say the entry "borrows only the word-set" / "takes only the word-set" from the amulets
entry. §3 in fact cites S605, S610, S621, S622, S644 and S645 for object definitions and counter-witchcraft
practice (witches' marks, the witch bottle, the mezuzah, the frontal-face amulet), not only for words. The
one-way statement is therefore false, and the neighbouring owner is not credited for the practice it owns.

**Required edit.** Say the entry takes the word-set **and** the counter-witchcraft practice as one
counter-accusation example, one-way, and returns the accusation grammar; or drop the object-practice bullets.

### D9 — MEDIUM — the S349 quote is accurate but the row's scope cell does not name it

**Location:** entry line 107; row S349 in `corpus/SOURCES.md`.

**Evidence.** The quote ("Native American communities have the right to limit or deny access to certain
stories, ideas, information") is present in Hunchman at p. 109, so it verifies. But the S349 row's
`scope`/`teaches` names only the windigo commodification and the "Windigo Psychosis" misreading; the
access-rights claim the entry relies on is not in the filed scope.

**Required edit.** Add the access-rights sentence to the S349 row's `anchor`/`scope`/`teaches`, or rephrase the
entry's bullet to the row's declared claim ("the outsider genre misreads the people; the community retains
authority over the tradition").

### D10 — LOW/MEDIUM — the S915 "first English judicial case" drops Williams's hedge

**Location:** entry line 51.

**Evidence.** Williams writes: "The earliest judicial trial for the crime on record in England is said to have
occurred in the reign of John." The entry says "the first English judicial case", which is stronger than the
source.

**Required edit.** "the earliest recorded English case (Williams hedges: 'is said to have occurred')".

### D11 — LOW — the S914 "composite" paraphrase is stronger than the quoted sentence

**Location:** entry line 49.

**Evidence.** The quote is "the modern idea of witchcraft is largely a learned product—the result of
scholastic and inquisitorial ingenuity". The bullet's gloss says the article "calls the modern figure a
composite"; the article's word is "learned product" (its fusion sentence is a different passage).

**Required edit.** Use "a learned product" in the gloss, or quote the article's fusion sentence instead.

### D12 — LOW — the §7 "weary of life" detail is sourced but not visibly anchored; the §3 S917 quote is cut mid-clause

**Locations:** entry line 175 (§7) and line 89 (§3).

**Evidence.** "a confessor can say, on the way to the stake, that she made the confession to end a life she
could no longer live" paraphrases Upham's Sinclair declaration: "I made up that confession on purpose to
destroy my own life, being weary of it, and choosing rather to die than live." The §3 S917 retraction quote
stops at "but, being delated by a malicious woman" with no ellipsis, so the §7 detail has no visible anchor.

**Required edit.** Extend the S917 quote to include "being weary of it, and choosing rather to die than live"
(marking the cut with an ellipsis), or add a pointer to the passage.

### D13 — LOW — the `- sources:` receipt pointer is not a resolvable repo-relative path

**Location:** entry line 5.

**Evidence.** "the seat's fetch receipts sit in the round's wave evidence directory" names no path. The
receipts are at `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/S914.txt` … `S918.txt`.

**Required edit.** Name `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/` (repo-relative) in the line.

### D14 — LOW — "four rows" hides the fifth (rejected) row the round opens

**Locations:** entry lines 4, 5, 8.

**Evidence.** The rows seat opened S914–S918: four `mined` rows plus one `rejected` candidate. The entry says
"four rows opened this round", "the four rows opened with it", and "The four anchors were opened afresh".
The registry actually grows by five rows (837 → 842); the claim's `>= 841` floor is still met.

**Required edit.** Say "four mined rows (S914–S917) and one rejected candidate (S918) opened this round" once,
and keep the four-row wording only where it means the mined set.

### D15 — LOW / round-level — the seat prompt carries the superseded r0 freeze

**Location:** the round's dispatch/bookkeeping, not the draft.

**Evidence.** The seat prompt in this wave names `3ca2cf2` and the r0 headings; the operative freeze is r2
`7e6ee2f8` with the house headings. The draft is correct for r2. A reviewer or counter grading the draft
against the prompt rather than the freeze would fail a correct object.

**Required edit (L1).** Run every round-84 counter with `--freeze 7e6ee2f8`, and record in the round's
calibration notes that the r0 hash and headings in the seat prompts are superseded (the lesson header already
names r2). Do not renegotiate the entry.

### D16 — MEDIUM (row record) — the S916 "no capture" probe has no QUALITY 24 positive control

**Locations:** `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/S916.txt` (capture probe) and `gate.md` (S916
bullet).

**Evidence.** The receipt records the CDX exact query
(`...&filter=statuscode:200`) returning `[]` for the Bull subpage — correct as far as it goes, and I reproduced
the empty result. But QUALITY 24 requires the probe to be run once in the same query shape over a URL known to
have captures, and the row/gate record shows no positive control (the S914 Witchcraft page does have a
capture). The URL is a direct Wikisource subpage, not a front-door DOI, so the redirect-target limb need not
apply — but that should be said.

**Required edit (rows seat / L1).** Add one same-query-shape positive-control probe (e.g. the S914 URL) with
its non-empty output beside S916's `[]`, and state that the redirect-target limb does not apply to a direct
subpage.

## 3. Boundary and PROVINCE

- **Canon handoff — PASS.** §15 hands off through
  `corpus/knowledge/synthesis/worldbible-integration-contract.md`, says "Kotodama proposes; lore records", and
  keeps the worked example labelled NON-CANON. The `- scope:` line repeats that canon belongs to lore.
- **Real-world-inspiration boundary — PASS.** The boundary file is named in `- couples:` and `- scope:`; §11
  marks the 1911 three-period scheme, functionalism, the learned/popular split, the victim totals and
  retro-diagnosis as contested/period; §12 and §15 carry the negative list (no living-community names, no
  restricted motifs, no charges against persons).
- **Living-community claims — PASS with D9.** The Kongo/Antonian material is historical and §1 says "makes no
  claim about Kongo"; the S349/S350 bullets are boundary anchors, not claims about a community. The only gap is
  the S349 scope-cell omission (D9).
- **Chousa/kagi ground — PASS.** The entry is a design synthesis, not a research-method or rights ruling; it
  cites the boundary file and the worldbible contract and makes no permission decision.
- **No accusation instructions — PASS.** The entry frames every lever as a design choice for a fictional
  culture and says twice (the `- topic:` and `- scope:` lines) that it is not a procedure for use on any
  person.

## 4. Verified positives (so the fixes do not disturb them)

- **All 19 quotes from the four mined rows verify exactly once** in the served bytes: S914 (7 quotes), S915
  (3), S916 (3), S917 (6). No quote is absent or duplicated.
- **The row digests match independent fetches:** S914 `68511af9…` (98,968 B), S915 `88407510…` (450,230 B),
  S916 `cc7b7d31…` (73,365 B), S917 `925e3634…` (1,801,648 B), S918 `2c4092db…` (60,730 B).
- **The captures verify:** S914 86,021 decoded bytes / `945d377f…`; S915 450,230 / `88407510…`; S917 1,801,648
  / `925e3634…`; S916's CDX exact query returns `[]`.
- **The five rows pass a faithful `sources-census.sh validate` mirror at rc 0** (only pre-existing W04/W01
  warnings outside claim D; no E01–E12 for S914–S918).
- **The §3 single-id discipline and the no-table-id rule hold** (`CITED-LINES: 0 finding(s) in 1 file(s)`).

## 5. Residual risk / not graded

- I could not verify the **print** page numbers of the Williams (1865) passages against the print edition: the
  Gutenberg text carries footnote numbers, not page numbers. The chapter attributions (Part II, ch. I and
  II) are correct.
- I checked the 21 already-registered rows against their own `scope`/`teaches` cells, not against every
  underlying source page; the entry's quotes match the row `anchor` cells where the two overlap.
- The entry's claim that "every §3 quote was re-checked against the served text by this seat" is a process
  claim; I independently verified the new-row quotes only.
- The r0/r2 freeze discrepancy is a round-level bookkeeping risk (D15), not a draft defect.
