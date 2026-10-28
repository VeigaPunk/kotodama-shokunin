# CritTriage — round 77 WAVE 2 (falsifier)

Attacked item: the 11-file assimilation triage in `CLAIMS-DRAFT.md` line 19 and the W1
`ScoutHeldEntries.md` triage table. Scope: enumerate every staged `naming-systems*.md`,
verify "exactly one adopted + remaining ten each dispositioned with reason and flip",
identify omitted files/ids or false reasons.

Verdict: **the 11-file enumeration is correct for the theme directory but the triage has
four real defects** — one omitted package artifact (a 12th `naming-systems*` file whose
rows are nowhere dispositioned), one unverifiable/mislabeled hold reason ("S899/S900
quarantine"), missing flips for 7 of 10 dispositions, and a REFUSE-vs-HOLD contradiction
between the draft and the scout table with internally wrong scout arithmetic.

---

## What was checked (commands + raw output)

### E1. Theme-dir enumeration — 11 files, claim's count reproduced

```sh
DIR=/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics
ls "$DIR" | grep -ic 'naming'   # → 11
ls "$DIR" | grep -iE '^naming-systems' | wc -l   # → 11
```
Raw list (verbatim): `naming-systems.amend-2026-10-23.md`, `…-23b.md`, `…-23c.md`,
`…-24.md`, `…-24-r10.md`, `…-24-r11.md`, `…-24-r12.md`, `…-24-r13.md`, `…-24-r14.md`,
`…-24-r15.md`, `…-24-r16.md`. Exactly the 11 the draft/scout name. One adopted
(`…-10-23.md`), 10 siblings. The draft names all 10 (23b, 23c, 24, r10, r11–r16) —
the scout's old note "DRAFT doesn't name 23c/r11–r16" is stale; current draft line 19
names every one.

### E2. Per-file row inventory — scout's table reproduced exactly

```sh
for f in naming-systems*.md; do grep -oE 'source: S[0-9]+' "$f" | sort -u; done
```
Adopted 23.md: S897, S903 + superseded block S886, S888, S889, S890, S891, S896 — matches
scout. 23b: S906/S907/S911. 23c: S912/S913/S914/S918. 24: S924–S927, S931, S933, S934,
S936 (S933/S934/S936 are the three active rows in its header). r10: S939–S941, S943, S944.
r11: S947–S954. r12: S957–S960. r13: S963–S966. r14: S969, S972–S974. r15: S978.
r16: S988. `grep -hoE 'source: S[0-9]+ — [^ ]+' naming-systems*.md | sort -u` → **50
unique rows** — scout's "50" reproduced.

### E3. Intra-staged duplicates — all scout claims verified by URL

- S934 (10-24) `web.archive.org/…/https://onomastica.ijppan.pl/…/download/574/763/` —
  inner URL identical to adopted S903. Same document. **Duplicate confirmed.**
- S936 (10-24) `…/https://omu.repo.nii.ac.jp/record/4358/files/2014000035.pdf` — inner URL
  identical to 23c's S918. **Confirmed.**
- S963 (r13) `http://www.sciscanpub.com/uploads/2024/01/22/8fc3f…pdf` vs r10's S939
  `https://` same path — scheme-only difference. **Confirmed.**
- S947 (r11) = S957 (r12): identical Wayback URL
  `…/20251007125613id_/http://iwr.cass.cn/…/t20240928_5787915.shtml`. **Confirmed.**
- S925 = S931 inside 10-24's superseded block: identical `jshou.edu.vn/houjs/article/view/313`. **Confirmed.**
- S966 (r13) `…/xlkxjz/CN/10.3724/SP.J.1042.2021.01067` vs S933 (10-24) EN-page capture of
  the same DOI — same article, two carriers. **Confirmed.**

### E4. S934 "misdescribed" — draft's reason verified TRUE

`merge/kotodama/SOURCES.append.md:82` titles S934 *"Słon, M., «Names and the named:
gender, femininity and given names in Poland», Onomastica 68"* while its URL is the
onomastica download `574/763`. ScoutDocS898's pdfinfo on that exact URL: Title
`Onomastica 69_07`, Author `Irena Kałużyńska`, DOI `10.17651/ONOMAST.69.7`. The staged
row describes a different paper than the URL carries → draft's "misdescribed duplicate
D2" is accurate. (Byte-level fetch left to sibling seat CritS934.)

### E5. Adopted-ground uniqueness — holds

`grep -cE '88|名.?姓|predate|contact-era|lexeme|terms'` across the 10 siblings: only
10-24 hits (3, its §N+2 gender-lexeme class — neighboring claim, and via a row already
refused as a D2 duplicate). No sibling restates 名≺姓 / contact-era acquisition / the
finite 88-term inventory. Adopted file lines 26–27 carry both grounds. **Claim's
"exactly one" survives.**

### E6. Base registry — reproduced

`git show 211f95…:corpus/SOURCES.md | grep -cE '^\| S[0-9]+'` → **820**; last id S896.
`grep -l 'S899\|S900' merge/kotodama/…/linguistics/naming-systems*.md` → exit 1 (no
S899/S900 row exists anywhere in the naming set).

---

## FINDINGS

### F1 — Omitted file: a 12th `naming-systems*` artifact is in the package and gets no disposition [COUNTEREXAMPLE — material]

```sh
find /home/vgpnk/Projects/shokuknow/merge/kotodama -iname '*naming*' -type f
```
prints **12 paths in 2 dirs**. The triage counts only
`knowledge/corpus/knowledge/linguistics/` (11 files). Missed:
`merge/kotodama/amendments/corpus/knowledge/linguistics/naming-systems.md` — a staged
amendment artifact (header: `<!-- AMENDMENT — append this to the lane's existing
corpus/knowledge/linguistics/naming-systems.md … -->`) carrying staged rows
**S874, S875, S877, S878, S879, S880** (verified `head -20`). None of its six URLs is in
base `corpus/SOURCES.md` (`git show 211f95…:corpus/SOURCES.md | grep -cE
'ir\.psych\.ac\.cn|jstage.*jinbunxshakai|obirin|kankyo-u'` → 0), so it is un-assimilated
staged material, not already-landed content.

It is not a bookkeeping nit: its **S875 is the same document as refused file 10-24's
S933** — `journal.psych.ac.cn/xlkxjz/EN/10.3724/SP.J.1042.2021.01067` (amendments file
line 5 vs 10-24's Wayback inner URL; ScoutQuarantine.md line 23 records the same
document identity). Its round-2 original S792 is `payload-absent` in
`absent-defect-register.md` line 124. So the omitted file intersects both the
duplicate-document leg and the defect register — and its six rows land in
`SOURCES.append.md` (S874–S880 present, verified) with zero triage coverage.

Draft line 19 says "**the package** has 11 `naming-systems*` files" — false for the
package (12 naming artifacts); true only for the theme subdirectory. ScoutHeldEntries
line 5 "no plain `naming-systems.md` in the staged dir" is true of `knowledge/` but
false of `amendments/`. ScoutPathsSearch scoped itself the same way ("eleven … theme
files"), so all three artifacts share the same scope blindness.

*Impacted axes/legs:* coverage C; REJECTS/GATE (a staged naming artifact escapes the
Gate entirely); ENTRIES (if Gate applies the amendment overlay per MERGE-REPORT rule 5
without triage, its S875 re-imports the refused S933 document).

*Smallest safe correction:* rename the set ("the package's staged **theme** files: 11
`naming-systems*` under `knowledge/corpus/knowledge/linguistics/`") and add one
disposition line for
`amendments/corpus/knowledge/linguistics/naming-systems.md` — natural fit is HOLD
(distinct ground: Chinese+Japanese name *taxonomy/measurement* layers; flip: a round
claiming that ground, after its S875 is reconciled with the refused S933 document).

### F2 — False/unverifiable reason: "pending S899/S900 quarantine resolution" names no existing defect [COUNTEREXAMPLE — reason as written is wrong]

The draft's r10 hold reason. What the record actually shows:

- No `S899`/`S900` row exists in any `naming-systems*` file (E6 grep, exit 1).
- The defect register
  `shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` lists kotodama rows
  S776, S778, S779, S786, S787, S791, S792, S795, S796, S804, S807`, S812`, S814, S816,
  S817, S820, S823, S824, S825, S827, S835` — **no S899/S900 row is quarantined**.
- In merged-ID space S899/S900 are the round-4 chinawriter *worldbuilding* pair
  (`ID-REMAP.md: round4 S873→S899, S874→S900`), staged in
  `culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` — a different
  theme entirely.
- The plausibly-intended referent is the register's `payload-absent` pair for those same
  chinawriter documents: register lines 129–130, round4 **S816/S817**. In round-7
  original-ID space `S899/S900` instead map to merged S925/S926 (`ID-REMAP.md:
  round7 S899→S925, S900→S926`) — the superseded jshou/ncpssd rows inside file 10-24
  itself. The reason as written doesn't say which ID space it means, and neither
  candidate is a "quarantine" record.
- ScoutHeldEntries line 88 admits it never verified the family exists.

Sharpening the defect: the `payload-absent` family is **round-4**, and the same round-4
block contains register S814 (the lishisuo URL — **D1's own document**) and S820 (the
onomastica URL — **D2's own document**). If a round-4 defect-family quarantine blocks
r10, it nominally touches the adopted pair too; the draft quietly resolves D1/D2 by
re-opening them this round while citing the same family as r10's blocker without
naming the distinction (re-grounded vs unresolved quote).

*Impacted:* Gate/REJECTS leg — a Gate entry copying this reason cites a non-existent
quarantine; provenance axis (the dependency is false provenance — it serializes r10
behind an unrelated theme's repair and mislabels payload-absence as quarantine).

*Smallest safe correction:* hold r10 on its own merits — "original/venue chase is
distinct ground; additionally carries C-tier docin upload row" (the scout's substance)
— or cite the defect precisely: "hold pending resolution of the `payload-absent`
register rows for round-4 chinawriter documents (merged S899/S900; register S816/S817)".
If the round-4 family is meant to block adoption, the Gate must also note D1's document
is register-S814 payload-absent and only admissible via this round's re-opened copy.

### F3 — Missing flips for 7 of 10 dispositions; counter only enforces ≥1 reject [DEFECT — fixable]

Draft line 19 ends: "reason each refusal by scope, duplicate document or unverified
payload **with reason and flip**". Counted against that standard:

| File | Draft disposition | Flip stated? |
|---|---|---|
| 23b | held for a later round | implicit (a later round on that ground) |
| 23c | field-history ground, not this claim | **no** |
| 24 | refuse S936/S934; S933 route-not-refusal | partial (fix rows) |
| r10 | hold pending "S899/S900" | yes — but see F2 |
| r11–r16 | "monograph-chase chain, distinct ground, held" — **one grouped clause for six files** | **no** |

Seven files (23c, r11–r16) get no flip, and r11–r16 share a single grouped reason — the
very shape the draft's own sentence forbids. Additionally the draft promises the 10 are
"explicitly dispositioned in the Gate/search log", but the counter (line 21) only
requires Gate "≥1 admit + ≥1 reject" — a Gate recording just the S934/S936 refuses
passes that bar while eight holds go unrecorded. The "explicitly dispositioned" promise
is currently unenforceable.

*Smallest safe correction:* one flip clause per held file ("reopen when a round claims
the naming-literature-as-field ground" for 23c; "reopen when the monograph-chase chain
resolves" for r11–r16); require the Gate table to enumerate all 10 filenames verbatim
(list in E1) so INDEX/GATE can check disposition-per-file, not just ≥1 reject.

### F4 — ScoutHeldEntries internal contradiction + stale provenance [DEFECT — false provenance]

- Scout table row for r10 = **REFUSE**; the draft it says it applies reads **HOLD**
  ("hold pending …, not adopted"). REFUSE closes the file; HOLD defers it — different
  Gate records. The scout's own w1-results verdict line says "HOLD 7 … REFUSE 10-24
  *and r10*" — that tallies 1+7+2 = 10 files total, i.e. it counts only 7 holds while
  its own table marks 8 HOLD (23b, 23c, r11, r12, r13, r14, r15, r16). Under either
  scheme the arithmetic is wrong (draft scheme: 9 HOLD + 1 REFUSE).
- Scout line 12 cites "CLAIMS-DRAFT.md §Claim C, lines 22–33" for the adopted name —
  in the current 37-line draft that range is §Claim Ca's ledger text. Lines 34/37 cite
  "DRAFT line 48–51 / 44–47" — the draft has no such lines. Stale provenance; the scout
  verified against an older draft revision.
- Scout line 36 flip text reads "Flip per DRAFT: S934 is a different document than D2"
  — stated backwards (verified fact: same document; presumably "flip *if* different").
  Copying it verbatim into the Gate would record a false condition.

*Smallest safe correction:* Gate records r10 as HOLD (per draft); correct scout summary
to 8 HOLD + 2 REFUSE (or 9+1 under the draft scheme); drop the stale line citations
(point at draft line 19); fix the S934 flip wording to "admit only if S934's document
differs from D2's".

---

## Parts of the claim that survived attack

- Exactly one adopted file: confirmed (E5).
- All 11 theme files enumerated and all 50 staged `source:` rows accounted for (E1/E2).
- Every intra-staged duplicate the draft/scout relies on verified true (E3/E4).
- Base registry 820 rows ending S896; lane S897/S898 = next-unused — consistent (E6).
- Draft's refusal rule "archive-admissible ≠ refuse" is correctly applied to S933
  (refusal rests on S936/S934, not on the archive route).

## Net assessment for the canonical judge

The triage's *substance* (which file to adopt, which documents duplicate) is sound and
independently reproduced. The defects are at the enumeration boundary and in reason
quality: (F1) one staged `naming-systems*` artifact outside the counted set with zero
disposition and a document overlap with a refused row; (F2) a hold reason citing a
quarantine that does not exist under the IDs named; (F3) seven dispositions without the
flip the draft itself mandates, under a counter that cannot check per-file disposition;
(F4) a scout table whose r10 verdict contradicts the draft and whose own tally is
internally inconsistent. All four are fixable pre-freeze with the single-line
corrections above; none requires redesigning the claim.

Tooling: none installed. Scratch: `/fast/scratch/hyaku/kotodama-r77/CritTriage/`
(base file copy for diffing; removed on exit).
