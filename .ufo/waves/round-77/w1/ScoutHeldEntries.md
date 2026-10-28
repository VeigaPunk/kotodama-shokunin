# ScoutHeldEntries — round 77 WAVE 1

Scope: triage every staged `naming-systems*` file under
`/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/` (11 files —
`ls | grep -i naming` printed 11 `naming-systems*` entries, no plain `naming-systems.md` in the staged
dir), against the DRAFT's adopted ground. Registry check is document-level against
`corpus/SOURCES.md` at base `211f9526800906e0c585d878d265c37e5e090c15` (820 `| S…` rows, last id S896 —
`git show 211f…:corpus/SOURCES.md | grep -cE '^\| S[0-9]+'` → 820).

## Adopted entry

`naming-systems.amend-2026-10-23.md` — the DRAFT's ONE adoption (CLAIMS-DRAFT.md §Claim C, lines 22–33
name it verbatim). Active rows: **S897** (cssn.cn 魏斌 article, live-403 → Wayback capture per DRAFT)
+ **S903** (onomastica Kałużyńska 2025, live 200). Tier mix **B + A** (self-declared, line 20).
Ground: (a) 名 predates 姓; 姓(氏)+名 is a contact-era acquired system; (b) given-name lexemes are a
finite, classified inventory (88 plant terms; 17 most-common). The file also folds in a superseded
round-3 entry (S886/S888/S889/S890/S891/S896, all tier B — Japanese name-dictionary apparatus +
onomastics rows) which travels inside the same file if adopted; the DRAFT's row_set (S897→D1, S898→D2)
maps only the two active rows.

Ground-overlap verdict: **no other staged naming entry is needed to cover the adopted ground.**
Checked every §-block of all 10 siblings: none restates 名≺姓 / contact-era 姓+名 acquisition or a
counted given-name lexeme inventory. Closest neighbours: 10-24's S934 row is the *same document* as
S903 (duplicate, not additional coverage); r13's §N+1 quotes the monograph's name-system typology
(second-hand) and r14's §N the monograph's own TOC — different claim (edition/bibliographic anchoring),
not the system-structure/lexeme ground. Coupling lines reference the adopted file but state different
claims.

## Per-file triage

| File | Active staged rows | Tier mix (as stated) | Claimed ground | Verdict |
|---|---|---|---|---|
| naming-systems.amend-2026-10-23.md | S897, S903 (+superseded S886,888,889,890,891,896) | 1B+1A (superseded 6B) | 名≺姓; 姓+名 contact-era system; finite classified lexeme inventory | **ADOPT** — the DRAFT's entry; ground unique in the staged set |
| naming-systems.amend-2026-10-23b.md | S906, S907, S911 | 2B+1C | one person's several names (小名/正名/字/号/笔名/艺名/室名); 避祖諒 + 輩行字 customs; ten 名–字 relations | **HOLD** — distinct ground; matches DRAFT line 48–51 (held, flip: later amendment on that ground) |
| naming-systems.amend-2026-10-23c.md | S912, S913, S914, S918 | "three tier B and one tier B" (4B) | the naming literature *as a field*: review lit, own journal (KCI), TW–JP comparative thesis, cross-language bibliography | **HOLD** — distinct ground (discipline apparatus, not structure/inventory); DRAFT silent, consistent with a later round |
| naming-systems.amend-2026-10-24.md | S936, S933, S934 (+superseded S927,S931 and S926,S924,S925) | 3A active | monograph's checkable address (S936); four research orientations (S933); gender-lexeme name class (S934) | **REFUSE** — per DRAFT: S934 is a document-duplicate of D2 (capture of the same onomastica PDF — verified: its staged URL unwraps to S903's URL); S936 is a Wayback copy of 23c's S918 (bibliography-bridge, same document re-staged); S933's document is re-carried live by r13's S966/S969. Flip per DRAFT: S934 is a different document than D2 |
| naming-systems.amend-2026-10-24-r10.md | S939, S940, S943, S944, S941 | 1B,1C,2B,1A | original of 姓名についての人類学的研究 found (《译道》2023 bilingual); docin upload record (S940, tier C); venue ruled out | **REFUSE** — per DRAFT lines 44–47: own ground needs the S899/S900 reject-family resolution first + adds C-tier weight a one-amendment claim does not need. Confirmed S940 is the docin upload record, tier C as stated |
| naming-systems.amend-2026-10-24-r11.md | S947, S948, S949, S950, S951, S952, S953, S954 | 3A+3B+1B(+1B) — "three A … three B … one B" (8 rows: A×3 counted incl. serial pair, B×4, machine-readable second copy B) | study's first venue 《民俗研究》2014(4) p.08; Latin author form Naran Bilik; 2023 issue = translation; editor serial + Cambridge volume closed | **HOLD** — bibliographic-provenance ground, distinct from adopted; continues r10's chase, so it serialises behind r10's resolution |
| naming-systems.amend-2026-10-24-r12.md | S957, S958, S959, S960 | 1A+3B | extent pp.8–23; monograph 《姓名论》 argument (father/child name-order ↔ modifier–head order); serial 6th issue; issue mirror thin | **HOLD** — provenance/monograph ground; S957 is the *same Wayback capture* as r11's S947 (duplicate row across files, same document) |
| naming-systems.amend-2026-10-24-r13.md | S963, S964, S965, S966 | not stated | study's Chinese text open (parallel column in 《译道》 PDF); 《姓名论》1997 first-edition page cite; migration rule 顺外传内; psych review's CN page | **HOLD** — distinct. Note S963 is the *same PDF* as r10's S939 (http vs https scheme); S966 is the live CN page of the S933-captured article |
| naming-systems.amend-2026-10-24-r14.md | S969, S972, S973, S974 | not stated | monograph's own text/TOC both editions (273 vs 366/377pp contested); publisher's two findings; review's full CN PDF (S969 = PDF form of S966's article) | **HOLD** — edition-anchoring ground, distinct |
| naming-systems.amend-2026-10-24-r15.md | S978 | not stated (single row) | per-edition award = edition anchor (1997→2000 prize; 2015→Shanghai prize); two renderings of the book's central claim | **HOLD** — citation-discipline ground, distinct |
| naming-systems.amend-2026-10-24-r16.md | S988 | not stated (single row) | in-literature citation fixing the 2015 printing; Yi 生辰岁位 naming rule with mythic etymology | **HOLD** — edition-anchor + one practice rule; distinct |

## Registry check (document-level, at base)

50 unique staged `source: S… — URL` rows extracted
(`grep -hoE 'source: S[0-9]+ — [^ ]+' naming-systems*.md | sort -u` → 50 lines).
Each raw URL **and** its document identity (Wayback unwrapped to inner URL, scheme-normalised,
percent-decoded) was checked against all URLs in base `corpus/SOURCES.md`:

**Result: 0/50 raw hits, 0/50 document-level hits** — no staged URL (or its underlying document)
already sits in the lane registry at base. Script + output in scratch (deleted per protocol);
the per-row table printed `raw=False doc=False` for all 50.

Intra-staged duplicates found (flag for the IdMap/Gate, not base-registry hits):
- **S934** (10-24) wraps the same onomastica PDF as **S903** (10-23, adopted D2) — the DRAFT's named
  duplicate; verified by unwrapping the Wayback URL.
- **S936** (10-24) wraps the same omu.repo PDF as **S918** (23c).
- **S963** (r13, http) = **S939** (r10, https) — same sciscanpub PDF, scheme differs only.
- **S947** (r11) = **S957** (r12) — identical Wayback capture URL of the 民俗研究 contents page.
- **S925** = **S931** (both inside 10-24's superseded sections) — identical jshou.edu.vn URL.
- **S969** (r14) is the PDF carrier of the same psych.ac.cn article whose CN page is **S966** (r13)
  and whose EN capture is **S933** (10-24) — three carriers, one document.

## Verification of DRAFT statements

1. `git grep -l -E 'lishisuo\.cssn\.cn|onomastica\.ijppan' 211f952… -- corpus/knowledge` → **prints
   nothing, exit 1** — DRAFT's negative sweep reproduces exactly.
2. Base `corpus/knowledge/linguistics/naming-systems.md` covers Chinese bìhuì taboo, exam-case
   homophone taboo, surname-first slot order, name-magic — **no 名≺姓 historical-structure claim, no
   counted lexeme inventory** (skim of §-tables + source list at base). DRAFT's ground statement holds.
3. Base linguistics dir holds `naming-systems.md` only — no `naming-systems.amend-*` file at base;
   the adopted path is a new file (consistent with 253→254 ENTRIES).
4. DRAFT's refused-candidate list names 10-24, r10, 23b — but does **not** name 23c or r11–r16.
   Triage above fills that gap: all HOLD on distinct ground (no silent skip needed; recommend the
   Gate record them as "not this ground" like 23b).
5. Minor wording flag on the DRAFT's S933 reason: it says "its own staged row says so" that the live
   CN page no longer carries the text. The staged row in 10-24 only cites the 2022 EN-page Wayback
   capture and does not literally state that; the substance is still sound — the document is
   re-carried by live CN rows S966/S969 in r13/r14 — so the refuse verdict stands, but the Gate
   should cite r13/r16-era rows rather than "the row says so".

## Unrun / out of scope

- Live re-open of staged URLs: not run (recon is naming-theme only; re-grounding is the L1's C-lands
  step under CORPUS.md rule 1).
- S899/S900 reject-family contents: not in this staged set (referenced by r10's ground chain only);
  existence inside the wider staged package unverified by this seat.
- Tier letters for r13–r16 rows are not declared in the files; reported as "not stated", not inferred.
