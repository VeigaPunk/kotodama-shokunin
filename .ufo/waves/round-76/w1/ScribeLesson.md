# ScribeLesson-7 — round 76, wave 1 (kotodama): the lesson draft, FILED-AT-DRAFT

**Seat.** role `scribe`, leaf: no subagents, no background jobs, no `task` spawns. Scratch
`/fast/scratch/hyaku/kotodama-r76/ScribeLesson-7` created for the fetches and deleted on exit; every durable
artifact was copied out first. **Installs: none** (no package, tool or binary was installed or upgraded).

## Deliverable

`.ufo/waves/round-76/w1/drafts/corpus/lessons/round-76.md` — 308 lines, 29692 B, sha256
`057763a678e75f62bc7093e1011f2f9f7210628f69ffa00a2868162ea24f8c32` (`sha256sum`). It carries the eight sections
the seat brief names — `## Gate`, `## Quarantine`, `## Collision guard`, `## Normalization`, `## Census`,
`## Mistakes`, `## Routed to round 77`, `## Sources & frontier` — plus `## What the base holds, measured`, and
**13** `<<FILL:…>>` slots (`grep -c '<<FILL:'`), every one a post-landing value: the Ca pair count and counter
verdict, the final lane ids, the landed evidence fetch lines, the landed row/knowledge counts and tier column,
the 11-cell check, the after-census run, the landed tier column, and the L1's mined mistake. Every other number in
the file is the output of a command pasted beside it, and each command's raw output is in
`stage/ScribeLesson-7/measurements.txt`.

## Behavior (what this seat actually did)

1. Read `.ufo/waves/round-76/CLAIMS-DRAFT.md`, `corpus/lessons/round-75.md`, the four staged candidate entries
   (read-only under `/home/vgpnk/Projects/shokuknow/merge/kotodama/…`), and the round-76 assimilation artifacts.
2. Measured the base facts the lesson states (base commit, registry rows, knowledge files, id lists and their
   digests, census-start, id gaps) — `measurements.txt`, blocks 1-8.
3. Fetched the six planned URLs — five planned rows over four documents — with `curl` under the browser-shaped UA, `--compressed`, one
   plain request each, and recorded status chain, wire bytes, stored bytes, sha256 and server date per request
   (`fetch-receipts.md`). Nothing was bypassed: no challenge was met, because none was served.
4. Built one stored window per carrier (4096-char excerpt, or whole-document when the page is shorter), each with
   its own fetch line and `anchor-hits-in-window:` count (`windows/`), and copied the raw bodies into `fetch/` so
   every row is re-openable offline.
5. Re-derived the register slice and opened the two register rows that name this round's documents; re-ran both
   guard-proof extractors over the round-76 fixtures (no run receipt shipped with them).
6. Wrote the draft and this report. Did **not** run the counters, grade any landed byte, or touch a tracked lane
   file.

## Gates

| gate | result | evidence (command → output) |
|---|---|---|
| base revision resolves | pass | `git -C … cat-file -e 98c486bdb4650ba5b8e651d332910e8ee60ad121` → exit 0 |
| census at round start | pass | `tail -2 reports/round-76/telemetry/census-start.txt` → `kotodama ok …/corpus/SOURCES.md` + `exit=0`; 34 lines, 28 `W04`, 4 `W01` |
| four anchors inside the Gate caps | pass | `anchors.txt`: 62 chars / 16 tokens, 24 / 1, 28 / 1, 33 / 1 |
| each anchor inside its stored window | pass | `anchors.txt` and the independent re-check in `measurements.txt`: `hits=1` four times, `carrier-only` for the two capture windows |
| QUALITY 22 binding (UA → the response that request got) | pass | `fetch-receipts.md`: UA string once, then per-request status chain / bytes / sha256 / server date |
| no access control met | pass | sweep: the 6 document requests plus the 3 route tests are all in `fetch-receipts.md`; the only non-200 first responses are a 302 (`showGb`, twice) and a 301 (`/bzgk/gb/newGbInfo`), all redirects; no 403/429/503, no captcha, no login, no paywall anywhere |
| collision guard re-derived | pass | `wc -l` → `817 / 132 / 35`; `sha256sum` → `97eef07a… / bab11d7d… / be203dd8…`; planned ids: `0` in reg-ids, `5` in staged-ids, `0` in collisions |
| guard-proof fixtures re-run | pass | 1-space plant found by the 0-3-space extractor (2 ids) and missed by the column-zero control (1 id); 4-space plant not found; `planted-1space.collisions` = `S859`, `planted-4space.collisions` empty |
| draft's own table shape | pass | `python3 stage/ScribeLesson-7/scripts/checktables.py .ufo/waves/round-76/w1/drafts/corpus/lessons/round-76.md` → 6 tables, `splits=[8] / [6] / [6] / [5] / [6] / [5]`, `mismatched: 0` |
| `accept-c.py` / `accept-ca.py` | **unrun** | `reports/round-76/` holds only `telemetry/census-start.txt`; the counters are freeze artifacts and no landing exists |
| after-census, landed evidence, 11-cell row check | **unrun** | nothing has landed; each is a `<<FILL:…>>` slot in the draft with its command |

## Findings

**F1 — the claims draft's Before leg is false at the base it names.** The draft says both greps "print nothing
(exit 1)". Measured:
`git -C … grep -l -E 'GB/T 33661' 98c486b… -- corpus` → `corpus/lessons/round-68.md`, `corpus/lessons/round-69.md`
(exit 0); `… -E 'digital\.archives\.go\.jp' … -- corpus` → `corpus/lessons/round-68.md` (exit 0). With the scope
the claim needs — `corpus/knowledge` — both return nothing, exit 1 (`2` commands, outputs in `measurements.txt`).
The draft's Gate and this lesson use the `corpus/knowledge` scope; the claim text should be corrected at the
freeze.

**F2 — the planned lane ids S894–S898 are five *other* documents in the staged package.** One command:
`grep -E '^\| *S(894|895|896|897|898) ' …/merge/kotodama/SOURCES.append.md` →
`S894` Sowers-Wills 2024 (doi 10.1017/cnj.2024.21), `S895` 王昕玥《论〈龙族〉…》 (chinawriter 2025-10-30), `S896`
a Korean paper on Chinese surnames (KCI ART001409716), `S897` 魏斌〈單名與雙名〉 (lishisuo.cssn.cn), `S898`
国立国会図書館 NDC10 (ndl.go.jp PDF). `grep -cE '^S89[4-8]$' reg-ids` → `0`; the same over `staged-ids` → `5`.
So the 35-collision figure is the pre-adoption intersection and the adoption *creates* five numeric collisions
that no guard output will show. Package maximum is `S990` (`… | sort -u | tail -1` → `S990`), so `S991+` is free
in both namespaces; alternatively carry the by-document map. The draft's Gate note 2 and `## Collision guard`
state both options and leave the choice to the freeze.

**F3 — S932 and S938 are one document, and the staged entry's byte claim does not reproduce.**
`curl -L -D … '…/showGb?type=online&hcno=…'` → `HTTP/1.1 302` with
`Location: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter`
then `200`; `/bzgk/gb/newGbInfo?hcno=…` → `301` to the same place; `type=download` → the same `302` → `200`.
`md5sum` of the three stored bodies → `e866bfd61a16f4c4fcdc1fc3a16bdf89` three times, sha256 `80b4c781…`, 24144
stored bytes; the Wayback capture of that same URL (`S932`) renders the identical visible text (757 chars;
`diff` prints nothing). The staged entry
`calendar-festival-systems.amend-2026-10-24-r10.md` prints "byte-identical … 24148 bytes each, md5
`9791d9dc0f17384eeab4ff4791eed437`" — no receipt in this round carries that number. Conclusion unaffected: the
"download" route serves the record page and no file (no `Content-Disposition`).

**F4 — the register's two kotodama rows for these documents are `payload-absent` because of how their quotes were
built.** `sed -n '118p;134p' …/absent-defect-register.md` gives
`round1 S776` (openstd newGbInfo, quote `标准号：GB/T 33661-2017 … 标准状态：现行 … 发布日期 2017-05-12 … 实施日期
2017-09-01 … 主管部门 中国科学院`) and `round5 S825` (digital.archives `/search`, quote `元号名称 開始西暦年 令和
2019 平成 1989 昭和 1926 大正 1912 明治 1868` plus `<br>元号名称／開始西暦年`). Measured over the folded pages:
**0** hits for each span; but `标准号：GB/T 33661-2017`, `2017-05-12`, `2017-09-01`, `主管部门` each occur once
(`中国科学院` twice), and the archives table's cells read `令和 2019 選択 平成 1989 選択 …`, i.e. the span omits the
`選択` cells. The table region from the first `元号名称` is 1684 folded chars and character-identical between live
and capture. Class size: **7 of 21** kotodama register quotes contain `…` and **5 of 21** contain `<br>` — for
those the substring absence test cannot fail. The verdicts stand as filed; the documents are re-opened as new
rows. The register's ids are not lane ids (base `S776` is a Pearson mancala paper, base `S825` a Gregis Axon
paper).

**F5 — dangling and mis-resolving citations in two staged entries.** Entry
`calendar-festival-systems.amend-2026-10-24.md` cites "S777" as already held: base has **0** rows for it
(`git show …:corpus/SOURCES.md | grep -E '^\| *S777 '`), **0** commits ever introduced that row
(`git log --oneline -S '| S777 ' -- corpus/SOURCES.md | wc -l`), and `S777` is one of the 76 ids absent from
`S001..S893`. Entry `era-periodization-models.amend-2026-10-23b.md` cites "S718" and "S719": base `S718` is
Farran et al. on infant-directed speech (`PLOS ONE` 11(3):e0151518) and base `S719` is Cristia 2013. Both
entries must re-point or drop before the freeze.

**F6 — the archive host is flaky, not closed.** Two of three `web.archive.org` attempts aborted before any HTTP
response (`curl: (7) Failed to connect to web.archive.org:443`, exit 7); the third returned `HTTP/1.1 200` with
307700 B. Both remaining captures (`S935`, `S932`) are on that host, so a capture step must retry and record its
own exit code.

**F7 — the registry's ids are not contiguous.** `817` rows span `S001..S893` with **76** ids absent:
`S455–S480`, `S492–S499`, `S544–S559`, `S563`, `S577–S599`, `S777`, `S778` (one python one-liner over
`assimilation/reg-ids`, output in `measurements.txt`). Any "row N ⇒ id S(N)" arithmetic is unsafe, and `S777` is
in the gap.

**F8 — the round-76 guard-proof fixtures shipped without a run receipt.** `find
.ufo/waves/round-76/assimilation/guard-proof -type f` returns five files (three registries, two `.collisions`)
and no `proof.txt` or script. This seat re-ran both extractors: the 1-space plant is found by the 0–3-space
extractor and *missed* by the column-zero control (the false green the extractor exists to avoid), the 4-space
plant is correctly not found, and both `.collisions` files match. Recorded in the draft's `## Collision guard`.

**F9 — entry a carries a whole superseded entry with live citation lines.** `grep -n 'recheck:'
…/calendar-festival-systems.amend-2026-10-24.md` → line 8 (round-9 ids) and line 62 (the folded round-7 passage,
`S919 -> 1, S921 -> 1`), and that block keeps its own `source: S919` / `source: S921`, `verified-at:` and
`recheck:` lines. Landing the file whole would append two campaign ids; the draft's `## Normalization` requires
the block be stripped or re-pointed (`S919 → S892`, `S921 → S885`, both by document, both verified against the
staged rows).

## Out of scope (and what was deliberately not run)

- Not written: `CLAIMS-DRAFT.md`, `corpus/**` (I wrote only under `.ufo/waves/round-76/w1/`), `LOG.md`,
  `SKILL.md`, `SCORECARD.md`, `SHONEN.md`, `reports/round-75/**`, `reports/round-76/**`, anything in the fleet
  root, anything under `/home/vgpnk/Projects/shokuknow`.
- No git/jj mutation anywhere: the lane was read only with `cat-file`, `show`, `grep`, `log`, `ls-tree`; no fixture
  repo was created, so no throwaway identity was used.
- **Unrun:** `accept-c.py`, `accept-ca.py` (absent until the freeze), the after-census run, the landed evidence
  files, the 11-cell row check — each is a `<<FILL:…>>` in the draft with its command.
- The four staged candidate entries were not byte-diffed against the lane because the lane holds none of the four
  paths (`git -C … cat-file -e 98c486b…:corpus/knowledge/<path>` → `absent` four times, while
  `calendar-festival-systems.md` and `era-periodization-models.md` exist).
- No pacman, no partial upgrade, nothing installed.

## Artifact paths (all lane-relative to `/home/vgpnk/Projects/shokunin/kotodama-shokunin`)

| path | what |
|---|---|
| `.ufo/waves/round-76/w1/drafts/corpus/lessons/round-76.md` | the FILED-AT-DRAFT lesson (308 lines, 29692 B, sha256 `057763a6…`) |
| `.ufo/waves/round-76/w1/stage/ScribeLesson-7/measurements.txt` | every base/register/package/guard command with its raw output and exit code (sha256 `e5b425a8…`) |
| `.ufo/waves/round-76/w1/stage/ScribeLesson-7/fetch-receipts.md` | UA, per-request status chain, wire/stored bytes, sha256, server date, route tests, failed attempts (sha256 `bea297cf…`) |
| `.ufo/waves/round-76/w1/stage/ScribeLesson-7/anchors.txt` | anchor metrics: chars, tokens, window scope, hits (sha256 `b1b02ab4…`) |
| `.ufo/waves/round-76/w1/stage/ScribeLesson-7/windows/` | six stored windows (`S894-live`, `S894-capture`, `S895-live`, `S896-live`, `S896-capture`, `S898-live`) |
| `.ufo/waves/round-76/w1/stage/ScribeLesson-7/fetch/` | seven raw bodies, incl. the `type=download` route test |
| `.ufo/waves/round-76/w1/stage/ScribeLesson-7/scripts/` | the six generators/checkers, so every artifact above can be rebuilt or re-checked from the durable copies (`gen.py`, `meas.sh`-`meas4.sh`, `checktables.py`) |
| `.ufo/waves/round-76/w1/ScribeLesson.md` | this report |

**Blockers:** none.
