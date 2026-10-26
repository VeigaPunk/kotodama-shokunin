# ExecScratchMirror — round-75 SCRATCHMIRROR rehearsal

**Seat:** ExecScratchMirror (executor, wave 1) · **lane:** kotodama-shokunin · **base:** `f556d1049fe651d3d63975600b13acd9fb686f15`

**Status: complete.** The mirror builds, the nine normalized rows append cleanly, the census
`validate --file` exits 0 with zero `^E[0-9][0-9]` lines, and the mirror README's index rows and
counts footer are census-clean. Receipt: `.ufo/waves/round-75/assimilation/validate-receipt-draft.txt`.

This is a **rehearsal**: `reports/round-75/claims.json` is still DRAFT and not frozen, so every row
below is a *draft* the L1 can take or reject. I did not edit `claims.json` or `ledger.json`.

---

## 1. What I built

`$A/validate/` with `A = .ufo/waves/round-75/assimilation` — a mirror of the lane `corpus/` that plays
the lane-root role:

```
validate/
  corpus/SOURCES.md   corpus/QUALITY.md   corpus/README.md
  corpus/knowledge/   corpus/lessons/
  SKILL.md            <- needed: rows S859/S860 name SKILL.md in their used-by cell, so without it
                          the census E11 (used-by path missing on disk) would fire on those rows
```

`du -sh` before the copy (as instructed): lane `corpus/` = **13M** (knowledge 7.9M, lessons 3.7M,
SOURCES.md 944K, README.md 172K, QUALITY.md 40K). Mirror knowledge files 249 → **251**.

Two **stand-in** entry files were written (the scribes' drafts landed *after* my first build — see
§7 finding 1 — so I re-derived the used-by from the drafts' actual `source:` lines):
`corpus/knowledge/myth-symbol/narrative-structure-frameworks.md` and
`…narrative-structure-frameworks.amend-2026-10-23.md`. Each carries one S-id per `source:` line, a
`- topic:` head-block, and the header fields the lane's entries carry.

## 2. The nine normalized rows

Drafted from the DRAFT `claims.json` `row_set` (S885–S893), one row per distinct document, ids by
document not by occurrence. Each row: **11 cells (id + 10)**, **no literal or escaped pipe** in any
cell, `status=mined`, `opened=2026-10-27`, **cadence-only** recheck cell (`180d` — no command text, no
`\|`), and `used-by` naming exactly the admitting entry paths.

Each row's **anchor quote is the same string the lesson draft's `## Gate` carries for that row** —
verified 9/9 identical, and each locates in the body this seat fetched. (My first build used deeper
page-level quotes of my own; the reconciliation is §7 finding 1.)

| lane id | staged | document | tier | Gate quote (located) | used-by |
|---|---|---|---|---|---|
| S885 | S876/S885/S917/S921 | persee 1113 — Barthes 1966 | A | «Innombrables sont les récits du monde.» | base + amend |
| S886 | S902 | persee 1120 — Todorov 1966 | A | «Étudier la « littérarité » et non la littérature» | amend |
| S887 | S904 | persee 1114 — Greimas 1966 | A | «Loin de se limiter à l'interprétation des énoncés, la théorie sémantique» | amend |
| S888 | S864 | jw.ucass Chinese narratology syllabus | B | 「故事是一种深层的抽象结构，必须通过话语呈现」 | base |
| S889 | S865 | jstage jcss 25/2 — 小方 孝 2018 | B | «a new research area called “narratology of narrative generation”» | base |
| S890 | S866 | jstage jsik 32/2 — 村井 源 2022 | B | «describe a story as a hierarchical structure consisting of three major layers» | base |
| S891 | S905 | unige.ch — Barthes *S/Z* excerpt | B | «les premières lexies suscitent l'établissement des cinq grands codes» | amend |
| S892 | S919 | iris.unipa.it — Marrone 2015 | B | «Mais combien, et de quelle nature, sont ces codes ?» | amend |
| S893 | S870 | chinawriter 2023 — 三九音域 | C | 「网络小说中的世界观，指的是故事设定中世间万物运转的方式，是故事发生的场景、规则」 | base |

## 3. Receipt — census validate, pasted

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file \
    /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md
file	W04	S127 duplicate url voices.uchicago.edu/goldinmeadowlab/… across scopes
   … 28 further W04 lines …
file	W01	S881 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
file	W01	S882 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
file	W01	S884 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
file	W01	S893 tierC mined used-by=corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
file	ok	…/assimilation/validate/corpus/SOURCES.md
exit=0
```

**exit=0, E-lines=0.** Base comparison (same command on the lane registry, no rows appended):
exit=0, E-lines=0, W-lines=31 → the mirror's 32 W-lines are the same 31 plus exactly one new
`W01` for the tier-C mined row S893 — the warning class the lane already carries on S881/S882/S884.

## 4. README index rows + footer — census-clean

```
OK index row myth-symbol/narrative-structure-frameworks.md — topic text verbatim (458 chars)
OK index row myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md — topic text verbatim (505 chars)
OK last footer: total 251 (live 251) dirs [32, 31, 40, 29, 24, 95] (live [32, 31, 40, 29, 24, 95])
OK last 'Total knowledge entries' line: 251 (live 251)
FINDINGS ['HEADER_DRIFT[INHERITED] linguistics declared=30 files=32',
          'HEADER_DRIFT[INHERITED] culture-material declared=36 files=40']
RESULT PASS
```

The two header drifts are **inherited lane state, not introduced here** — the identical checker on the
lane tree alone reports the same two (`RESULT PASS`, both flagged INHERITED). They are exactly the
ledger's L75-02 (linguistics 30 vs 32) and L75-03 (culture-material 36 vs 40) REPAIR pairs.

**Footer form.** The round-74 landing footer is the *inline* one-line form
(`Counts checked … : \`cmd\` (total N files; …).`); the round-28 `sweep.py` `FOOTER_RE` only matches the
*3-line* form and takes the **first** match — the defect ledger pair L75-04 routes. I wrote the
mirror's new footer in the inline house style, so the repaired sweep (ExecSweepFix) must read the
**last** block of whichever form. Flagging this to L1: whichever form ExecSweepFix settles on, the
mirror footer and the repaired parser have to agree, or the INDEX leg stays red.

## 5. Other legs the rehearsal exercised

| leg | result |
|---|---|
| ROWS — 11 cells, no literal/escaped pipe, mined, opened 2026-10-27, cadence-only recheck | PASS (9/9) |
| ROWS — pre-existing rows byte-identical, none removed | PASS (808 → 817, 0 changed, 0 removed) |
| ROWS — used-by exactly the admitting entries' `source:` ids | PASS (9/9, USEDBY PASS) |
| REPOINTED — every `source:` line one id, id's row URL names the cited document | PASS (10/10 lines match) |
| GATE — the row's anchor quote IS the lesson's Gate quote | PASS (`DIFFERING 0 of 9`) |
| EVIDENCE — every anchor quote locates in its fetched body (NFKC + whitespace fold) | PASS (9/9) |
| RENUMBER — mirror rows agree with the sibling seat's `id-renumber-map.json` (staged→lane by document) | PASS (9/9, `RENUMBER-CROSSCHECK PASS`) |
| CITEDLINES — `check-cited-lines.py` over the two entries | `CITED-LINES: 0 finding(s) in 2 file(s)`, exit 0 |
| INDEX — one index row per adopted entry, topic text verbatim, footer = live counts | PASS |

## 6. Open findings for the L1

1. **The lesson draft and the row set disagreed on the Gate quotes; I reconciled to the lesson.**
   My first build used deeper page-level quotes (e.g. Barthes p. 5 «aucun niveau ne peut à lui seul
   produire du sens»). The scribes' drafts landed afterwards and the lesson draft's `## Gate` carries
   a *different* quote per row — all from the **notice body / page 1** of each document, not the
   transcription pages. Since the GATE leg binds one quote per row and the ROWS leg puts the evidence
   quote in the anchor cell, the two texts must carry the same string or the counter reads them
   against each other. **I re-derived all nine rows' anchor cells from the lesson's Gate quotes and
   re-verified each locates** (`DIFFERING 0 of 9`, all nine located). *This is a rehearsal; the L1
   should confirm the lesson's quotes are the ones that freeze.* Note the consequence: the lesson's
   S885/S886/S887 quotes come from the persee **notice body**, which is the page the row's source cell
   names first — so those rows' evidence windows are the notice body, not a transcription page. The
   transcription-page quotes remain available as the deeper locator text inside the anchor cell.
2. **S893's status is `mined` at tier C, which raises W01.** The claim's ROWS leg says "each row
   status mined"; tier C + mined + non-`—` used-by is a warning by contract. The base entry cites
   S893 in its `source:` line, so `used-by` cannot be `—` without breaking REPOINTED. I kept `mined`
   and accepted the W01 (the lane already carries three). Tier B is the alternative but the evidence
   does not support it — the row is an industry-outlet practitioner statement.
3. **The staged S870 quote stays rejected; the row carries a *new* quote.** The round-72 refusal
   (`作品中的人物名字和地名`, 0 hits) still holds — I re-confirmed 0 hits on the live 2026-10-27 page.
   The S893 anchor cell says so explicitly.
4. **S891 and S892 need an ordinary-means reading, and the live URLs do not give one.**
   `unige.ch/…/barth70.html` served a bot challenge (met, not passed); `iris.unipa.it/…pdf`
   answered **HTTP 403** to a plain request. Both were read through **Internet Archive captures**
   (`web.archive.org/web/20041220223357id_/…` and `…/20251111222249if_/…`), both HTTP 200, both
   with the quote located. The row cells name the direct URL and the capture and say the challenge
   was met and left unsolved — the house pattern of S093/S123/S142/S173. **This is a QUALITY-10
   judgement the L1 should confirm**: an archive capture is an ordinary copy (not a bypass), but the
   row's `tier` rests on it.
5. **The persee document pages are not byte-stable across fetches.** Two fetches of the same URL
   returned the same byte length with different sha256 (the served page carries per-request content).
   Consequence for the EVIDENCE leg: an evidence file must record the sha256 of **its own** fetch, and
   the `window-sha256:` must be recomputed from the stored window — a body sha256 taken from a
   different fetch will not reproduce. Worth telling ExecEvidence.
6. **Staged-id vs lane-id namespace collision — resolved, not a risk.** The staged file already
   uses S885–S893 for *different* documents (kotobank, NDL, onoma, rudn, cyberleninka), so the
   staged→lane map must disambiguate by document, not by number. The sibling seat's
   `id-renumber-map.json` (ExecRenumber) does exactly that, and **my mirror rows agree with it
   9/9** — same lane id per document, same document URL (`RENUMBER-CROSSCHECK PASS`). Cross-check
   this seat's mirror against the map if the map is re-generated.
7. **jstage jsik needed a retry.** The first plain request for the jsik PDF returned **HTTP 502**;
   the retry with a Referer header returned HTTP 200 (697092 bytes). Both requests are recorded with
   their UA.
8. **The third entry file is a live fork.** The scribes drafted
   `narrative-structure-frameworks.amend-2026-10-23b.md` (citing S885/S891/S892), but claim C's
   frozen `entries` list names two paths, so the file gets no row this round (ScribeEntryAmend §6.2,
   ScribeReadmeIndex §2.3a, and the lesson's "Refused (32)" table all treat it as conditional). My
   mirror therefore keeps **two** entries and puts S891/S892's `used-by` on the
   `…amend-2026-10-23.md` entry. **If the L1 adds the b-file to `entries` before the freeze**, the
   b-file must get its own index row, the myth-symbol heading becomes `(32)`, the totals line becomes
   `252`, the footer vector becomes `32/32/40/29/24/95`, and S891/S892's `used-by` must move to the
   b-file path. ScribeReadmeIndex §2.3a has the exact block. Re-run the mirror after any such change.

## 7. Fetch ledger (QUALITY 22 — each UA bound to the response it got)

UA on every request: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/130.0.0.0 Safari/537.36`. Full records (status, bytes, content-type, effective URL, body
sha256) are in `.ufo/waves/round-75/assimilation/validate-fetch/`.

| id | URL | HTTP | bytes | body sha256 (16) |
|---|---|---|---|---|
| S885 | persee doc page 1113 | 200 | 109589 | `25cfd7f699780fcd` |
| S886 | persee doc page 1120 | 200 | 111234 | `9c49c2a23f6a5b99` |
| S887 | persee doc page 1114 | 200 | 118777 | `041cd205b1fc8aa7` |
| S888 | jw.ucass.edu.cn …/xushixue.pdf | 200 | 225123 | `62a13e92e23d764c` |
| S889 | jstage jcss 25/2/25_200/_pdf | 200 | 1085244 | `fdf60d276b3f31cd` |
| S890 | jstage jsik 32/2/32_2022_017/_pdf | 200 (after a 502) | 697092 | `1dccf9d1427defb0` |
| S891 | web.archive.org/web/20041220223357id_/…/barth70.html | 200 | 3898 | `69b5987240ccd728` |
| S892 | web.archive.org/web/20251111222249if_/…/marrone…pdf | 200 | 763802 | `8c0303670ff5db86` |
| S893 | chinawriter 2023/0922/c404024-40083104.html | 200 | 45238 | `51251e22c617617a` |

The per-page transcription pages (T1_0005/0006/0011/0125/0139/0029/0030) were also fetched by plain
request — all HTTP 200, no login, no challenge — and their quotes were used in my first build before
the reconciliation in §6 finding 1.

## 8. Files written

- `.ufo/waves/round-75/assimilation/validate/` — the mirror (new, untracked)
- `.ufo/waves/round-75/assimilation/validate-receipt-draft.txt` — the receipt (new, untracked)
- `.ufo/waves/round-75/assimilation/validate-fetch/` — per-fetch receipts + README (new, untracked)
- `.ufo/waves/round-75/w1/ExecScratchMirror.md` — this report

**No tracked lane file was modified** (`git diff --stat` empty; `git status` shows only the untracked
`.ufo/waves/round-75/` and the pre-existing untracked `reports/round-75/`). `claims.json` and
`ledger.json` were read only. Scratch lived under
`/fast/scratch/hyaku/kotodama-r75/ExecScratchMirror/` and was deleted before yielding.

**No tools installed** — `pdftotext`, `gawk`, `curl` and `python3` were already present; no pacman,
no new package.

## 9. What the main agent should run

1. `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file .ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md` — expect exit 0, zero `^E[0-9][0-9]` lines.
2. Confirm finding 1 (the lesson's Gate quotes are the ones that freeze) before the freeze; if the L1 changes them, the rows' anchor cells must be re-derived from the lesson.
3. Confirm findings 4 and 5 (the archive-capture rows; the unstable persee body sha256) before the freeze, and pass finding 5 to ExecEvidence.
4. Confirm the footer form with ExecSweepFix (finding in §4).
5. Re-run the mirror build after the real entries land, so the used-by cells and index rows come from the *actual* entry `source:` lines rather than my stand-ins.
