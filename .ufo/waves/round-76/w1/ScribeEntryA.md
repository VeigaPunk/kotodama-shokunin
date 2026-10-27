# ScribeEntryA — round 76, wave 1: candidate a, `calendar-festival-systems.amend-2026-10-24.md`

**Verdict.** The entry is writable and I staged it: three tier-A rows opened by a plain request, three refusals of staged sentences the pages do not carry, one dropped off-theme coupling, one correction to the staged text's carrier, and one defect found in the DRAFT claims' own before-state. The staged text as delivered would have failed the Gate on two sentences; the draft below refuses them and passes the cited-lines lint with 0 findings.

Role: leaf scribe. No subagent, no background job, no tool install, no pacman. Nothing written outside my report, `w1/drafts/`, `w1/stage/ScribeEntryA/`, and my scratch dir.

## 1. Deliverables

- Draft entry: `.ufo/waves/round-76/w1/drafts/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md` — 109 lines, 18,678 B.
- Gate notes (every source: URL, access date, located quote, status/bytes/UA, verdict + flip): `.ufo/waves/round-76/w1/stage/ScribeEntryA/gate-notes.md`.
- Evidence windows, one per row, with fetch header + sha256 + locator scheme:
  `stage/ScribeEntryA/S898.window.txt`, `S896.window.txt`, `S894.window.txt`.
- Scratch `/fast/scratch/hyaku/kotodama-r76/ScribeEntryA/` deleted at exit; receipts live only in the stage dir above.

## 2. Draft gates, measured

- Cited-line lint: `CITED-LINES: 0 finding(s) in 1 file(s)` / `exit=0` — `python3 -B tools/check-cited-lines.py .ufo/waves/round-76/w1/drafts/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md`.
- Body length: `2575` body tokens and `1834` body Latin words (body = everything from `## §1` on) — `python3 -c "... re.findall(r'[A-Za-z0-9][A-Za-z0-9\-]*|[\u4e00-\u9fff]', body)"`. Declared minimum 478 words: met by the Latin-word count alone.
- Span locatability: `spans 15 misses 0` — every 「…」 span in the draft was searched (spaces stripped) inside its own window file. First run had two misses and both were fixed, not waved through: the page `<title>` (added to the S898 window as a `#` line) and one elided quote containing `…` (replaced with the located prefix 「国家标准委22日发布」).
- Couples resolve at base `98c486bdb4650ba5b8e651d332910e8ee60ad121`:
  `corpus/knowledge/culture-material/calendar-festival-systems.md`, `…/timekeeping-instruments.md`, `…/era-periodization-models.md`, `corpus/knowledge/linguistics/naming-systems.md`, `corpus/knowledge/synthesis/worldbible-integration-contract.md` — five `git cat-file -e` calls, five `OK`, no `FAIL`.
- The staged file's own `- couples:` named `linguistics/naming-systems.amend-2026-10-24.md`, which does **not** exist at base: `git cat-file -e 98c486b:corpus/knowledge/linguistics/naming-systems.amend-2026-10-24.md` → `fatal: path '…' does not exist`. Replaced with the base `naming-systems.md`.

## 3. Admissions

| row | document | fetch | verdict |
|---|---|---|---|
| S898 | 光明日报 2017-05-23 01版 report on the release | live HTTP/1.1 200, 25,250 B decompressed, sha256 `670850ea…2366f1`; same-page Wayback capture `20170523024955` 200 | ADMIT |
| S896 | 全国标准信息公共服务平台 GB/T 33661-2017 record | capture HTTP/2 200, 24,174 B decompressed, sha256 `f04feb47…101e0e`; live 200, 7,334 B, same fields | ADMIT |
| S894 | 国立公文書館デジタルアーカイブ 詳細検索, 元号選択 modal | live 200, 311,308 B, sha256 `204b7188…b763ea8`; capture `20260422145052` 200, 307,700 B, sha256 `c015e1dc…68a13e0` | ADMIT (with carrier correction, §5) |

Nothing was reached through a challenge, login, paywall or automation; the only wall met in the round was the archive's own JS-gated table, and the capture is an ordinary public copy of the same path — the challenge was met and not passed, and the table also renders in the live HTML, so the claim does not depend on the capture.

## 4. Refusals — three, each with its sweep

**(a) The leap-month rule is not on any page read.** `grep -o '闰' s898b.html | wc -l` → `0`; `grep -o '閏' s898.txt | wc -l` → `0`; the article's counters for the neighbouring terms are `冬至 = 2` and `朔 = 2`, both inside the anchor/model sentences. So the staged sentence about a leap-month rule is refused; the draft keeps the month-11 anchor and marks the derived selection rule `(to-verify)`. **If the round requires the leap-month selection rule from these three rows, the entry must be REFUSED — it is not in them.**

**(b) The era table is not a 詔勅・勅令・勅書 database.** `詔勅 = 0`, `勅令 = 0`, `勅書 = 0` in the live page **and** in the capture (`grep -o … | wc -l`, both artifacts). The page's own framing is 詳細検索 with a 元号選択 modal over three tabs. The staged phrase is dropped and the page's own framing is used.

**(c) The Barthes/Marrone codes comparison is dropped as off-theme.** It is narrative theory, it is already held by `myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md` (S885/S892 there), and neither document was opened for this entry. Flagged in the draft's `- scope:` line and here. No campaign id S919/S921 and no bare `S887` appears anywhere in the draft; the only ids in it are S894, S896, S898.

## 5. Corrections carried from the staged text

1. `詔勅・勅令・勅書 database` → the archive's advanced-search era selector (sweep in §4b).
2. `linguistics/naming-systems.amend-2026-10-24.md` (nonexistent at base) → `linguistics/naming-systems.md`.
3. Staged `source:` lines cited campaign ids S937/S935/S932 and `verified-at: 2026-10-24` → re-pointed by document to lane S898/S896/S894, `verified-at: 2026-10-27`, with a fetch note per row.
4. Staged "the report also names the drafter: … the observatory, not a ministry" plus "the promulgation chain runs through the National Astronomical Observatory" → split into the two links the two rows actually carry: the registry places 主管/归口 in 中国科学院, the report places drafting in 中国科学院紫金山天文台. The registry does **not** name the observatory; the chained sentence was wider than either page.
5. Added the located negatives the entry needs (no 闰 on the page; the 备注 cell is empty; the record's own full-text notice gates preview to a browser), and the two-date tension (registry 发布日期 `2017-05-12` vs press 「国家标准委22日发布」), which the staged text did not mention and which a reader copying an "announced" date needs.

## 6. Two findings for the L1 on the round's own text (not mine to edit)

**F1 — the DRAFT claim C before-state command is false as written.** The claims file says `git grep -l -E 'GB/T 33661' 98c486b -- corpus` and `git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus` "each print nothing (exit 1)". Measured:

```
$ git grep -l -E 'GB/T 33661' 98c486b -- corpus
98c486b…:corpus/lessons/round-68.md
98c486b…:corpus/lessons/round-69.md
exit=0
$ git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus
98c486b…:corpus/lessons/round-68.md
exit=0
```

The knowledge-corpus form of the same sweep does hold:

```
$ git grep -l -E 'GB/T 33661' 98c486b -- corpus/knowledge        → (no output) exit=1
$ git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus/knowledge → (no output) exit=1
```

So the before-state leg should be declared on `corpus/knowledge` (or the claim should say the lessons carry the string). As declared, the leg fails before any work lands. My draft's `- ground:` uses the knowledge-scoped sweep, with its exit 1.

**F2 — id hazard in the staged file.** The staged text cites `S750`, `S776`, `S777`, `S807` as if they were this standard's rows. At base those ids are other documents (S750 = Culin 1907, S776 = Pearson 2016, S807 = a 2021 anatomy paper), and `git show 98c486b:corpus/SOURCES.md | grep -c 33661` → `0`: the registry holds no row for the standard at all. No lane-id-looking citation from the staged text is carried into the draft; every row is cited by document. The plannned new ids S894/S896/S898 are free (registry's highest id at base is S893).

## 7. Limits and unrun checks

- The standard's clause text was **not** read (unrun). The record's own notice routes full text to a browser-only preview; no clause statement is made anywhere in the draft, and the leap-month selection rule is explicitly `(to-verify)`.
- Whether 「1秒」 means a second of time or of arc is **not** resolved; the draft keeps the page's word and says so. Unrun: no standard text to test it against.
- The reform's effect was **not** measured; the report gives a 2013 anecdote and no post-2017 count, and the draft claims none.
- The era table's 開始西暦年 values were checked only as archive fields (live vs capture, byte-identical row lists: 248/248, 94/94, 8/8, `IDENTICAL`); no independent chronology check was run, and the draft says the table is a finding aid.
- The archive page's Chinese/Korean tabs are the archive's own labels (`清宣統`, `金天輔`, `民国`); the draft marks that as the label problem rather than asserting any state's era sequence.

## 8. Hygiene

- Scratch created at `/fast/scratch/hyaku/kotodama-r76/ScribeEntryA/`, every fetch wrote there, and it is removed on exit; no `/tmp` path is cited anywhere.
- Installs: none (no tool was needed). `pacman` not run.
- Lane git state untouched; only read-only `git show/cat-file/grep` against `98c486b` was used.
- The DRAFT claims file was read, never edited.

Report: .ufo/waves/round-76/w1/ScribeEntryA.md
