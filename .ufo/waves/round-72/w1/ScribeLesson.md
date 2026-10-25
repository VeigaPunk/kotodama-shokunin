# ScribeLesson — round-72 w1 (seat `L1Kotodama72.ScribeLesson`)

Leaf seat; no delegation, no background jobs, no `task` spawns. Date of run 2026-10-25.
Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

## What this seat produced

The draft lesson skeleton, written to the assigned scratch path:

- **`/tmp/r72-lesson.md`** — 82 lines, sha256 `3611c635347defc80bade35c8f7f11c98fb2d0f1734e511c17ba5038472eb59d`.
  Sections: `# Round 72` header (claims C/Ca, round shape), `## Gate` (S874/S875 admit table +
  the assimilation reject table with reason + flip), `## Mistakes` (one row), `## Quarantine`
  (adoption OPEN, id-collision guard result, staged REFUSED set not adopted, F-1/F-2 notes).

No lane, fleet, or shokuknow file was written by this seat. The lane already carries a
`corpus/lessons/round-72.md` (committed at `770100f`, amended at `5897ddf`, `334d79d`); the
draft above is the advisory skeleton for that file, and its diff against the landed text is
reproduced under "Divergence from the landed lesson" below.

## Re-open evidence gathered by this seat (all under `/tmp/L1Kotodama72.ScribeLesson/`)

| file | what | how |
|---|---|---|
| `ihchina-live-20261025.html` | live `https://www.ihchina.cn/project.html` | `curl -sS -m 25` → **HTTP 200, 43 255 B**, sha256 `1510bc63462fc620575da92fbea33b0dbbb38df0e487533ad4d982bf7decef33` (byte-identical to ScoutIHChinaCapture's live fetch) |
| `bunka-search-live-20261025.html` | live `https://online.bunka.go.jp/db/heritages/search` | `curl -sS -m 25` → **HTTP 200, 231 736 B**, sha256 `ad56b0c86c1f0c2bac31116f9d6854ba290b33abb6f113cd55f07e84f350ae2b` (differs from the lane's earlier copy only in the CSRF `_token` value — 3 identical `<option>`/label lines otherwise) |
| `register-S792-journal-psych-20261025.html` | live register row S792 URL `https://journal.psych.ac.cn/xlkxjz/EN/10.3724/SP.J.1042.2021.01067` | `curl -sS -m 30` → **HTTP 200, 159 831 B** |

Verbatim located spans re-confirmed this seat (`grep -c`, all count 1 unless stated):

- ihchina live + both Archive captures: `国务院先后于2006年、2008年、2011年、2014年和2021公布了五批国家级项目名录`; `国家级名录将非物质文化遗产分为十大门类`; `编号中的罗马数字代表所属门类`.
- ihchina 2020 capture only: `国务院先后于2006年、2008年、2011年和2014年公布了四批国家级项目名录` (the 四批 wording is **absent** from the 2026 capture and the live page).
- bunka live: `<option value="11">安土・桃山 [日本]</option>` (1), `安土・桃山 [日本]` (3), `旧石器 [中国]` (3), `清 [中国]` (3), `材質・構造・技法` (14), `指定区分` (1), `建造物` (18), `伝統的建造物群` (9).
- register S792 page: the four headings `实际影响取向` / `社会认知取向` / `自我信息加工取向` / `文化产品取向` are **present, 2 hits each**; the slash-joined quoted span is **absent** (0 hits). This independently reproduces the round-72 lesson's F-1 correction: the filed round-71 *reason* for S792 was factually wrong; the REFUSED verdict and the staged S875/S933 refusal still stand because only the slash-joined span is missing.

## Gates run (exact commands, outcomes)

| gate | command | outcome |
|---|---|---|
| Coverage counter, draft lesson substituted | `git clone --no-hardlinks --shared <lane> /tmp/scribelesson72/clone`; `cp /tmp/r72-lesson.md corpus/lessons/round-72.md`; commit; `python3 -B reports/round-72/accept-c.py --root . --lands $(git rev-parse HEAD) --fleet-root /home/vgpnk/Projects/shokunin` | **`ACCEPT-C-72: PASS legs=10/10`** (ENTRIES, ROWS, REPOINTED, **GATE**, **REJECTS**, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK all PASS) |
| Coverage counter, lane HEAD | same command at lane HEAD `11a41fb` | `ACCEPT-C-72: PASS legs=10/10` |
| Calibration counter, lane HEAD + fleet report landed | `python3 -B reports/round-72/accept-ca.py --root . --lands $(git rev-parse HEAD) --fleet-root /home/vgpnk/Projects/shokunin` | **`ACCEPT-CA-72: PASS legs=12/12`** (REPORTCORR `fleet-rev=406c4e9eb611`, REPORTLAST `report-names-lands=True`, NOHARM `census exit=0`) |
| APPENDONLY leg, whole-file set | `git diff -U0 b60c7b1..HEAD -- LOG.md corpus/lessons/round-71.md corpus/QUALITY.md reports/round-71 ':(exclude).ufo/waves/round-71/w2'` | removed content lines = **0**; numstat deletions = **0** |
| Id-collision guard, contract pattern | `grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' <lane corpus/SOURCES.md> \| grep -oE 'S[0-9]+' \| sort` vs the same over `shokuknow/merge/kotodama/SOURCES.append.md`, then `comm -12` | at base `b60c7b1`: lane 797 ids (max S873), staged 132 ids (S859–S990), overlap **15 ids S859–S873**; `S874`/`S875` **absent** from lane reg-ids → next-free, collisions file empty |
| Id-collision guard, post-append re-run | same over the landed HEAD registry (799 ids) | overlap **17 ids** — S859–S873 **plus S874/S875**, because the *staged* package independently uses S874/S875 for its onomastics rows. The lane ids are free; the staged namespace is not. This is the same caveat the landed lesson records (F-2 / the staged set's own S874/S875) and it is the reason the adoption re-pointed by document. |
| APPENDONLY mutation, m2 (in-place LOG heading rewrite) | scratch git fixture; `git diff -U0 base..HEAD -- LOG.md corpus/lessons/round-71.md corpus/QUALITY.md` | removed = **1** → the leg's zero-deletion assertion **rejects** m2 (the landed leg design, not the raw diff command MutCaAppend probed) |
| APPENDONLY mutation, m4 (in-place rewrite **plus** an appended correction) | same fixture | removed = **2** → **rejects** m4; appending does not heal an in-place deletion |
| F-1 factual check | `grep -c` per heading on `register-S792-journal-psych-20261025.html` | 4/4 headings present (2 each), slash-joined span absent → F-1 correction verified |
| Lesson-header claims cross-check | `git show HEAD:corpus/lessons/round-72.md`; `git show HEAD:corpus/lessons/round-71.md \| awk 'NR==83'`; `git show HEAD:LOG.md \| awk 'NR==4274'`; `git show 99e3d63 -- LOG.md corpus/lessons/round-71.md` | lesson-71:83 = `collisions S859 S860; id-renumber-map.json S874→S1005 by document). No`; LOG:4274 = the `**Item 10.**` renumber-map line, both `S861→S992 → S874→S1005`; `git show 99e3d63` shows both files changed by **1 line each** — the in-place edit the Mistakes row names |
| Round-shape cross-check | `python3 -c` role histogram over `.ufo/waves/round-72/w1/spec.json` (32 items: 7 scout, 6 reviewer, 5 critic, 4 executor, 3 scribe, 3 mutation-tester, 1 sentinel, 1 connector, 1 revenger, 1 simplifier); `dispatch.json` `counts.spawn` = 32 | attack roles (reviewer+critic+mutation-tester+sentinel+revenger) = **16/32 = 50%** — matches the landed header |

Note: `claims.json` carries **no** wave-shape field (only `round`, `frozen`, `base`, `claims`); the
shape in the header is read from the frozen wave spec and dispatch file. The draft header says so
explicitly, so the round shape is not attributed to `claims.json`.

## Findings (audit-relevant; none is mine to fix — routed to the L1)

1. **The landed lesson's `## Mistakes` fix cell contradicts my brief, and the landed wording is
   the correct one.** My brief says the fix is "appended corrections + QUALITY 21". The landed
   lesson says: *"QUALITY criterion 21 not needed for this class — it is a Gate-discipline
   criterion; the round-72 corrections are the fix."* Verified against the committed criterion:
   `corpus/QUALITY.md:63` is criterion **21** = *"A 'no capture' ruling probes the canonical slug
   and files the probed URLs"* — a Gate reject-discipline criterion (CDX canonical-slug probe), not
   an append-only criterion. Attributing criterion 21 to the in-place-edit class would mis-file it.
   The draft skeleton keeps the landed wording; the brief's phrase is read as "the round's fixes
   are the appended corrections, and QUALITY 21 exists this round", not "criterion 21 governs this
   class". **Not a defect — a brief-vs-artifact wording gap, flagged for the judge.**

2. **`reports/round-72/telemetry/census-end.txt` was rewritten in place, and the frozen
   `census-end.txt` receipt at `b47033a` recorded two `E12` findings.** Sequence, all committed:
   `b47033a` lands the LOG entry + census-end with `kotodama E12 S874 row outside Registry section`
   and the same for S875 (the two rows had been appended after the `## Leads` section, not inside
   `## Registry`). `868107e` moves them into the Registry table. `2b8d674` then **rewrites**
   `census-end.txt` in place — the diff shows two `-E12` lines removed and one `+ok` line added
   (`git diff b47033a..2b8d674 -- reports/round-72/telemetry/census-end.txt`). Same pattern for the
   two measures receipts at `ac0d18e`: `measures-ca.txt` 4 added / 4 removed, `measures-c.txt` 3
   added / 3 removed (header revision + tree lines replaced in place).
   This is the *same* in-place-receipt class the round's own `## Mistakes` row names, on this
   round's telemetry. It is **not** caught by the `APPENDONLY` leg, whose filed set is
   `LOG.md`, `corpus/lessons/round-71.md`, `corpus/QUALITY.md`, `reports/round-71` — round-72
   telemetry is outside it. `AGENTS.md:34` requires a closing snapshot as *"a new append-only
   file, never an in-place edit of the original record"*, and `REGIMEN.md:44` requires per-round
   telemetry in `reports/round-<N>/telemetry/`. **Recommendation to the L1: either add
   `reports/round-72/telemetry` to the APPENDONLY filed set for round 73, or record the rewrite as
   a named exception with its reason.** No file changed by this seat.

3. **A stale copy of the calibration counter is committed at
   `.ufo/waves/round-72/counters/accept-ca.py` (sha256 `bcc952bb…`, frozen at `a7ab3bd`) and its
   `QUAL20`/`QUAL21` legs can never pass.** The frozen copy writes the pattern as
   `re.search(r"^20\\. ", q, re.M)` — in a raw string `\\.` matches a literal backslash followed by
   any character, so the criterion-20 line never matches. Verified: `python3 -B
   .ufo/waves/round-72/counters/accept-ca.py --root . --lands HEAD` prints `LEG FAIL QUAL20` and
   `LEG FAIL QUAL21` on a tree where both criteria **are** committed (`corpus/QUALITY.md:61` and
   `:63`), then dies with `COUNTER ERROR: path '.ufo/reports/round-72/kotodama.md' does not exist`
   (it also reads the fleet report from the lane root instead of the fleet repo). The live
   `reports/round-72/accept-ca.py` (sha256 `f080c240…`) uses `re.findall(r"^20\. ", …)` and
   correctly counts `n20 == 1`. The claims' `counter` field names `reports/round-72/accept-ca.py`,
   so the executed instrument is right — but two counter copies with the same name and different
   behaviour are committed, and the frozen one is the one a reader is most likely to pick up from
   the freeze commit. **Same class for `.ufo/waves/round-72/counters/accept-c.py` (sha256
   `72e7f846…`): it fails `GROUND` and `COLLCHECK` at HEAD** (it reads the pre-rename receipt path
   `.ufo/waves/round-72/assimilation/validate-receipt.txt` and the pre-rename id-file names
   `reg-ids`/`staged-ids`/`collisions`, while the landed artifacts are `gap-sweep.txt` and
   `collcheck-*.txt`); the live `reports/round-72/accept-c.py` (sha256 `355e67f1…`) accepts both
   spellings and passes 10/10. **Recommendation: retire or clearly mark the frozen duplicates.**

4. **The control receipt `reports/round-72/telemetry/controls-ca.txt` names a counter sha256
   (`dbb2ff63b9ec3fa3`) that exists nowhere in the lane's git history.** Checked every blob at every
   commit on every `accept-ca.py` path: the historical shas are
   `091074c5 103fc42d 1ce25fb9 347d9c7c 3a5a79d1 3f3f63fc 51255593 5382ffed 550c89a4 5e8915ac
   7319ff4b 9d93cbd5 a6d1c1c2 a8088092 bcc952bb cc2a755e d0787979 f080c240 f206095b f222648e
   f706aacd` — `dbb2ff63` is absent, and an exhaustive blob scan (`git rev-list --all --objects`
   → `cat-file` → sha256) finds it at no path. Its sibling `controls-c.txt` names `72e7f846…`,
   which **is** the committed frozen `counters/accept-c.py`. The claim-Ca control therefore cites a
   counter build that cannot be re-derived from the repo, so the do-nothing control's own
   instrument is not reproducible. This is the K71-7 class (a receipt naming a counter sha that
   does not match the counter at the stamped revision) recurring one round later, in a control
   receipt rather than a measures receipt. **Recommendation: re-stamp `controls-ca.txt` from a
   committed counter, or record why the named build is not in the repo.**

5. **`claims.json` names the wrong path for the calibration counter's inputs relative to the
   pre-data corrections.** The frozen `claims.json` `counter` field says
   `reports/round-72/accept-ca.py --root . --lands <lands> --fleet-root /home/vgpnk/Projects/shokunin`
   — correct — but the *committed* `reports/round-72/accept-ca.py` at freeze (`a7ab3bd`, sha256
   `347d9c7c…`) is an earlier build than the one that passes today (`f080c240…`); the frozen copy
   reads `.ufo/reports/round-72/kotodama.md` from the lane root and so cannot complete at all.
   The live copy (used for `measures-ca.txt`) reads the fleet report from the fleet repo, which is
   what the round prompt requires. This is the same stale-duplicate issue as finding 3, seen from
   the claims side.

6. **The `E12` episode is now fully remediated in the tree, and the census is clean.** The landed
   `corpus/SOURCES.md` places S874/S875 at lines 829–830, inside `## Registry` (which runs to line
   830); `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`
   exits 0 and the committed `census-end.txt` now ends `kotodama ok …/corpus/SOURCES.md` with zero
   `E12` lines. `git show HEAD:corpus/SOURCES.md` confirms both rows inside the Registry table
   (the earlier `b47033a`/`5897ddf` state had them at lines 926–927, after `## Leads`).

7. **The lesson's `## Gate` quotes are ≤25 words under the counter's own rule, and the CJK length
   caveat is real.** `tools/check-gate-quotes.py` parses only `- S### ` / `* S### ` bullet rows, so
   pipe-table Gate rows are invisible to it (blind spot recorded by MutGateQuotes, tool not
   re-edited). The counter `accept-c.py` counts quotes itself (`len(s.split()) > 25`); the four
   CJK quotes each measure **1** whitespace token. The `GATE` leg passes at HEAD and on the draft.
   The S875 quote `“安土・桃山 [日本]”` was checked against the served page: the exact
   `<option value="11">安土・桃山 [日本]</option>` occurs once and the bare string three times, so
   the located span is verbatim either way.

8. **`S875`'s `used-by` names only the canonical entry, while `S874`'s names both.** Verified at
   HEAD: S874 `used-by` = both `heritage-taxonomy-models.md` and the r13 amendment; S875 `used-by` =
   `heritage-taxonomy-models.md` only. The claim's `ROWS` leg requires the *union* of used-by to equal
   the two admitted entries, which S874 satisfies alone, so the leg passes. But the amendment's
   `source:` line names **only S874** — so the amendment does not cite S875, and S875's single-entry
   `used-by` is consistent with that. No defect; recorded so the reader does not expect the
   amendment to carry the Japanese row.

## Divergence from the landed lesson (`corpus/lessons/round-72.md` at HEAD `11a41fb`)

The landed lesson already satisfies the brief's structure. The draft skeleton's differences, all
additive or clarifying:

- **Header**: draft names the claims in the brief's order (C/Ca) and states explicitly that the
  wave shape comes from `spec.json`/`dispatch.json`, not from `claims.json` (which has no such
  field). Landed header lists Ca first and attributes the shape without that caveat.
- **S874 Gate row**: draft writes the two Archive capture URLs in full; landed abbreviates to the
  capture ids. Both are the same carriers; the fuller form is directly checkable.
- **S875 Gate quote**: draft `“安土・桃山 [日本]”` (the option text as served, incl. the branch
  tag) vs landed `“安土・桃山”`. Both verbatim; the draft's is the longer located span.
- **`## Quarantine`**: draft adds an explicit id-collision-guard paragraph (lane 797 ids max S873
  vs staged 132 ids; overlap band 15 ids S859–S873; S874/S875 next-free; staged namespace
  independently reuses S874/S875 for the onomastics rows). Landed covers the namespace point in
  `## Gate` and `F-2` rather than in `## Quarantine`.
- **`## Mistakes` fix cell**: draft keeps the landed wording (criterion 21 is a Gate criterion, not
  this class's fix) — see finding 1.
- The landed lesson additionally carries four sections the brief did not enumerate and the draft
  omits: the sibling-overlap note (connector), `## Corrections (pre-data, claims freeze)`,
  `## Frontier-step`, and `## Routed to round 73 (post-landing, ScoutMergeScan)`. **A reader must
  not treat the draft as a replacement for the landed file; it is the brief's skeleton only.**

## Touched surfaces

| path | by this seat | note |
|---|---|---|
| `/tmp/r72-lesson.md` | **created** | the draft skeleton (assigned scratch path) |
| `/tmp/L1Kotodama72.ScribeLesson/{ihchina-live-20261025,bunka-search-live-20261025,register-S792-journal-psych-20261025}.html` | **created** | re-open fetches, named for what they are |
| `/tmp/scribelesson72/` | created | scratch: clone, id lists, diffs, fixture repo (not the report path) |
| lane repo `corpus/`, `LOG.md`, `SCORECARD.md`, `reports/`, `.ufo/waves/` | **not written** | read-only for this seat; the lane's own commits moved under it while this seat ran |
| fleet repo `/home/vgpnk/Projects/shokunin` | **not written** | read-only; the round-72 fleet report (`406c4e9e`) was written by the L1, not this seat |
| `/home/vgpnk/Projects/shokuknow` | **not written** | read-only source tree, per the round prompt |
| git index / jj state | **not touched** | no add, no commit, no jj operation from this seat |

## Out of scope for this seat

- Committing or amending the lesson (`corpus/lessons/round-72.md`) — the L1 integrates; this seat's
  draft is advisory and lands only via the L1.
- The counter defects in findings 3–5 and the receipt rewrite in finding 2: `reports/` and
  `.ufo/waves/round-72/counters/` are the L1's and the executing seats' surfaces; this seat
  reports and routes, and changes nothing.
- The `E12` remediation (already committed at `868107e`) and the fleet report (already committed
  at `406c4e9e`) — observed and verified, not performed here.
- `considerthese/`: absent for this lane (no such directory under the lane repo), so nothing was
  mined from it.
- `tools/check-gate-quotes.py`: frozen and not edited (MutGateQuotes probed the blind spot; the
  repair stays routed).

## Tooling

**No installs, upgrades, or version changes.** Everything ran on the host's pre-existing tools:
`git`, `curl`, `python3` (3.14.1 stdlib), `grep`/`sed`/`awk`, `sha256sum`, `diff`, `comm`, `sort`,
`rsync`-free `cp`, and the lane's own `scripts/sources-census.sh` and `tools/check-cited-lines.py`.
`/home/vgpnk/.omp/agent/RULES.md` was read before any tooling consideration; pacman was not
invoked (paused host-wide by the operator ruling).

## Status

Draft complete and gate-verified: with the draft substituted for the lane lesson, the coverage
counter prints **`ACCEPT-C-72: PASS legs=10/10`**, including the `GATE` and `REJECTS` legs this
seat's brief targets. The lane's own lesson at HEAD also passes both counters
(`ACCEPT-C-72: PASS legs=10/10`, `ACCEPT-CA-72: PASS legs=12/12`). Eight findings are routed above;
none is left unrecorded and none was silently fixed.
