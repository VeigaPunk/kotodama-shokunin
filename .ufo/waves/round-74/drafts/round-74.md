# Round 74 — kotodama: assimilation of the worldbuilding-setting-practice theme (CJK practitioner craft)

**Claims line.** Lane `kotodama-shokunin`, base `f7104cbce186bc2e1522abf0cfd619cc834628bb`, hyaku run 7, two v1 waves
(40 staged knowledge files triaged). **C (coverage, sourced):** at base 804 registry rows, 0 `*worldbuilding-setting*`
files, 247 knowledge files, 0 registry hits for litmemo/tuduku/chinawriter → four rows S881–S884 opened and mined this
round plus S877's in-place `used-by`, two entries admitted (the base entry and its dated amendment), and
`reports/round-74/accept-c.py` printing `ACCEPT-C-74: PASS legs=13/13` at lands. **Ca (calibration):** 13 ledger
pairs (1 REPAIR, 12 ANNOTATE) plus 6 must_track pins → `reports/round-74/accept-ca.py` printing
`ACCEPT-CA-74: PASS legs=11/11`. Operative freeze commit: `00c408a0af2fa5ddf65af2224152ce258b26d896` (see R74-M9 for the two earlier freezes); no seat scored landed data before it.

## Gate

Access date for all five rows: 2026-10-25. Evidence captures are the round-74 files named in the last column
(fetch line, browser UA, HTTP 200, bytes, body sha256, stored window).

| source | access date | quote (≤25 words) | locator | evidence capture | verdict |
|---|---|---|---|---|---|
| S877 — М.Ю. Сидорова, О.Н. Шувалова, «Интернет-лингвистика: вымышленные языки», 2006, author-hosted at МГУ — http://www.philol.msu.ru/~sidorova/files/conlangs.pdf | 2026-10-25 | «Язык – главный инструмент построения вымышленных миров» | p.7 (PDF page 7), first clause of the 108-character sentence | reports/round-74/evidence/S877.txt — 1055723 B, sha256 e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9, window 4098 chars, quote-found-verbatim no (PDF line breaks; found after whitespace folding) | admitted |
| S881 — LitMemo ブログ「世界観の作り方」 — https://litmemo.com/ja/blog/novel-worldbuilding-guide | 2026-10-25 | 「自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観を作る。」 | h3 「3. 外側の層へ因果をつなぐ」, 2nd sentence of the paragraph | reports/round-74/evidence/S881.txt — 101615 B, sha256 441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64, window 4098 chars | admitted |
| S882 — つづく編集室 コラム「Web小説の世界観・設定の作り方」 — https://tuduku.space/column/novel-worldbuilding | 2026-10-25 | 「勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか」 | h2 「世界観設定に必要な5つの要素」 info box 「世界観設定の5要素」, item 5 | reports/round-74/evidence/S882.txt — 17068 B, sha256 754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7, window 2953 chars = the whole visible document (the page text is shorter than the 4096-character floor, so the window is the document, not a padded excerpt) | admitted |
| S883 — 爱潜水的乌贼「我先设定世界观，再考虑怎么升级」, 中国作家网 2025-06-10 — https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html | 2026-10-25 | 「整个过程里，我先做的是世界观，再考虑怎么升级，再考虑升级的表现。」 | P68 (ordinal of `p` in `div.end_article`, image = 1) under subheading 确定风格、设定世界、推导故事 | re-quote: the staged span was absent from its own page (register URL-quote mispairing, R68 refusal) — reports/round-74/evidence/S883.txt, 48536 B, sha256 a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d, window 4104 chars | admitted |
| S884 — 爱潜水的乌贼 interviewed by 李玮, 中国作家网 2022-12-07 — https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html | 2026-10-25 | 「把它放在前面大概20章之内慢慢来，我觉得是问题不大的。」 | para 35 (the 14th 乌贼 answer), final sentence tail | re-quote: the staged span was absent (register Sowers-Wills span mispaired to this URL, R71 refusal) — reports/round-74/evidence/S884.txt, 62604 B, sha256 344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659, window 4103 chars | admitted |

Gate notes, each one a decision a reader can re-check:

- **S877 cell quote trimmed.** The located sentence is 108 characters and 15 whitespace tokens; claim C's GATE leg caps a cell quote at 25 tokens *and* 80 characters, so the cell carries the 54-character first clause (7 tokens) and the full sentence stays on the evidence file's `quote:` line. The long form passes the token limb and fails the 80-character limb — recorded as R74-M7.
- **S882 window geometry.** The capture records `window: chars=2953 min=4096`, and 631 before + 33 quote + 2289 after = 2953 = the entire extracted page. Claim C's EVIDENCE leg asks for a stored window of at least 4096 characters; on this page that floor is unreachable, and `accept-c.py`'s `leg_evidence` does not read the floor, so the limb is vacuous here (R74-M6). The whole-document window is the honest maximum.
- **S877's round-73 evidence file is not reusable.** `reports/round-73/evidence/S877.txt` uses the round-73 grammar (`--- context window (whitespace-collapsed, +-400 chars) ---`, one collapsed paragraph, 1564 B) and carries the p.10 Chapter-1 quote; the round-74 file is a fresh capture in the round-74 grammar at the p.7 locator.
- **Re-quote discipline.** S883 and S884 are *new rows for re-opened documents*, not reversals: the register rows S816 and S817 stay REFUSED (see Quarantine), and each admit row names the earlier refusal.

Rejections — the four probed rows this round, each with its reason and its flip:

| reason | flip | probed URL | verdict |
|---|---|---|---|
| staged S882 (Сидорова/Шувалова PDF) is not appended: the same document already holds lane row S877, so appending would register one document twice | a distinct document under that URL, or S877 retired first; until then the in-place `used-by` change is the only permitted move | http://www.philol.msu.ru/~sidorova/files/conlangs.pdf | refused |
| staged S895's folded passage (王昕玥, 论《龙族》的叙事失控与世界观危机) is dropped: the amend file's superseded section cites a row that is not in the row set | register the document as its own row with a captured, exactly-once quote and a lane frontier ground | https://www.chinawriter.com.cn/n1/2025/1030/c404027-40592897.html | refused |
| staged S899's quoted span was absent from the page it was bound to (register S816 mispairing; the span belongs to the 2022 interview) — the row stays refused and the document is re-opened as the new S883 | a fresh quote located on the 2025 page, which is what S883 carries now | https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html | refused |
| staged S900's quoted span was the Sowers-Wills clause, absent from this page (register S817 mispairing) — the row stays refused and the document is re-opened as the new S884 | a fresh quote located on the 2022 page, which is what S884 carries now | https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html | refused |

Triage of the 40 staged knowledge files: **2 adopted / 4 path-present with differing staged bytes / 34 refused**.
The four path-present files exist in the lane with different bytes and were left untouched:
`heritage-taxonomy-models.md`, `heritage-taxonomy-models.amend-2026-10-24-r13.md`, `conlang-scholarship.md`,
`conlang-scholarship.amend-2026-10-23.md` (staged vs lane sha256 differ in all four; measured this round).

| family | files | why not adopted | clearing condition |
|---|---|---|---|
| narrative-structure-frameworks (base plus 4 amendments) | 5 | staged S870 was refused in round 72; the base document is not a lane row and its quotes were not re-located | register the document with a captured, exactly-once quote and a lane frontier ground |
| naming-systems (base plus 10 amendments) | 11 | no lane row holds the document; the amendment chain re-states one topic without a located quote per claim | one row per document, each with a round-N capture and a located quote |
| calendar-festival-systems amendments | 3 | parent entry and its sources are not lane rows; dates asserted from memory of the text, not from a located span | register the parent and the calendar sources, then re-quote |
| era-periodization-models amendments | 2 | same class as calendar: no parent row, no located span | register the parent and its sources first |
| verification amendments (citation-format r10–r16, journal-serial r16, reopen-gate) | 9 | these are lane-internal process texts, not source-backed domain knowledge; no registry row can support them | either an own-work `source:` path with a lane-relative locator, or leave them as lessons |
| conlang-scholarship.amend-2026-10-23b/-23c/-2026-10-24 plus conlang-methodology.amend-2026-10-24 | 3 + 1 | amendments to entries the lane already holds; their quoted spans were not re-opened this round, and the staged bytes differ from the lane's | re-open each amend's quotes against the parent entry's rows and land as appended amendments, one round per parent |

## Collision guard and scratch mirror (item 10)

**The guard, run as CORPUS specifies.** Item-10 pattern `^ {0,3}\|[[:space:]]*S[0-9]{3,}` over the lane registry
and the staged package, ids normalised then intersected (`ExecRenumber.md` §1):

| artifact | lines | sha256 |
|---|---|---|
| `assimilation/reg-ids` | 804 (S001…S880) | `94a495c7d634123c0d40e6895b7916892e204f450a536ce00cf4af9aef26ca86` |
| `assimilation/staged-ids` | 132 (S859…S990) | `bab11d7d0ee0d84795b1ff80274fe371670fff73a477c747b2fd3cad4c25ddad` |
| `assimilation/collisions` | 22 (S859…S880) | `130ec2d15f923b005a9a91f03e8a9a949a9233d8b70f432663d93031ee041721` |

Re-derived twice and `cmp`-ed against the stored files: all three reproduced. **None of the 22 collision pairs names
the same document** (URL join, 0/22), so the intersections are namespace drift, not duplicate registrations, and the
guard's acceptance is *by document*, not "collisions is empty" — which is unattainable while the package keeps its
S859–S880 rows. The dispatch premise that the lane already holds S883/S884/S899/S900 as different documents is
**false at base and at worktree HEAD**: `grep -c` over `reg-ids` for those four ids is 0 and no lane row carries
litmemo, tuduku or chinawriter. The two-id overlap that matters (`S883`, `S884`) is created *by* this adoption.

**Old → new map, by document, never by arithmetic** (`assimilation/id-renumber-map.json`, sha256
`d3573f7d3cf23afa7296c281d201225eed643aef2b406b3a403c2a67aeb24afa`; join key = normalised URL):

| staged | document | lane id | action |
|---|---|---|---|
| S883 | litmemo.com/ja/blog/novel-worldbuilding-guide | **S881** | append |
| S884 | tuduku.space/column/novel-worldbuilding | **S882** | append |
| S899 | chinawriter.com.cn/n1/2025/0605/c404024-40494534.html | **S883** | append, re-quoted from the page |
| S900 | chinawriter.com.cn/n1/2022/1207/c404024-32582252.html | **S884** | append, re-quoted from the page |
| S882 | philol.msu.ru/~sidorova/files/conlangs.pdf | **S877 (reused)** | not appended; in-place `used-by` only |

The substitution must be a **simultaneous single pass** over one lookup table: staged `S883→S881` and
`S899→S883` share a target namespace, so any sequential per-id replacement re-maps an already-mapped id. A single
pass over both staged entries yields `S877`×4 and `S881`×4/`S882`×4 in the base entry and `S883`×3/`S884`×3 in the
amend; the round-local prose ids (`S729`, `S730`, `S742`, `S743`, `S754`) are not keys and stay untouched, which is
why they are rewritten or removed rather than mapped — `S742→S881` and `S743→S882` are safe same-document rewrites,
while `S729`/`S730` (staged S870/S871, refused) and `S754`/`S895` are not in the row set and appear in neither entry.

**S877 in-place change, exact cell values.** The lane's append-only rule permits `status`, `recheck` and `used-by`
in place, logged old→new:

- `used-by` old: `corpus/knowledge/linguistics/conlang-scholarship.md`
- `used-by` new: `corpus/knowledge/linguistics/conlang-scholarship.md, corpus/knowledge/culture-material/worldbuilding-setting-practice.md`

Every other S877 cell is byte-identical (`corpus/SOURCES.md:832` at base: book, tier B, mined, opened 2026-10-25,
recheck `180d`), and the multi-path separator is the registry's own `, ` convention.

**Recheck prose stripped from the four new rows.** Every staged row for this theme carries a backticked curl
pipeline plus an escaped pipe in the recheck cell, which splits it into 12 cells instead of 11; all four land
cadence-only:

| row | staged recheck cell | stripped cell |
|---|---|---|
| S881 (staged S883) | `180d` + backticked curl of the litmemo URL + `grep -c '自然環境'` → 4 (ran 2026-10-23), one escaped pipe | `180d` |
| S882 (staged S884) | `180d` + backticked curl of the tuduku URL + `grep -c '設定ノートの構成例'` → 1 (ran 2026-10-23), one escaped pipe | `180d` |
| S883 (staged S899) | `180d` + backticked curl of the 2025 URL + `grep -c '先做的是世界观'` → 1 (ran 2026-10-23), one escaped pipe | `180d` |
| S884 (staged S900) | `180d` + backticked curl of the 2022 URL + `grep -c '20章之内慢慢来'` → 1 (ran 2026-10-23), one escaped pipe | `180d` |

The re-fetch and span checks now live here (Gate) and in the seat reports, not in a registry cell; the capture
files are the re-verification instrument.

**Scratch mirror, not a rehearsal in the lane** (`ExecScratchMirror.md`). `assimilation/validate/` holds a copy of
`corpus/` plus `SKILL.md` (so pre-existing `used-by: SKILL.md` cells resolve), the two draft entries
(`sha256 658a8fa4…9986b00b` and `bb5504e2…d80d8673e`), and a mirrored registry with the four normalized rows and
the S877 edit: 804 → **808 rows**, `sha256 81fcebe1…f2f326`, row-level diff exactly `801c801` (S877) and
`804a805,808` (S881–S884), nothing else. `sources-census.sh validate --file` on the mirror → **exit 0, zero
E-codes** (`assimilation/validate-receipt-draft.txt`). The claim's "commit strictly before the registry-append
commit" sequencing clause is not exercised by a leaf seat and stays owed.

**Guard mutations** (`MutRegistryCollision.md`, fixture in `/tmp`): m1 (2-space) and m2 (3-space) and m4
(no-space column zero) all fire the canonical pair (804 → 805 ids, collisions 23, new id `S883`) while the
**raw-pair variant** — `comm` on un-normalised `grep -oE` output — misses all three, so the second normalisation
step is load-bearing. m3 (4-space) and m5 (tab) drop out of both the guard and the census row count silently
(under-count, no error). m6 (lowercase) is invisible to the guard but blocked by census `E02`; m7b (a well-formed
twin) is the battery's only `E03` and proves the census duplicate check works. Two structural limits are recorded,
not gamed: the guard is an intersection, blind to intra-registry duplicates; and `E01` precedence swallows `E03`,
so "E03 fired" can never be evidence that an *as-is* staged row exercised the duplicate check (8 of 132 staged
rows have 11 cells).

## Quarantine

**Register S816 and S817 stay REFUSED as staged — re-confirmed this round** (`ScoutQuarantine816817.md` §2–§4).
Both pages were re-fetched with the browser UA at 2026-10-25 21:14 local: HTTP 200, and **byte-identical to the
committed round-71 captures** (`s816.html` 48536 B sha256 `a3b6640c…bee94d`; `s817.html` 62604 B sha256
`344de345…d3d659`), so the pages did not move and the verdicts cannot be explained by drift. Register S816's quoted
span (这个我肯定考虑过。我自己就是资深读者…) is absent from the 2025 page it is bound to (0 hits) and present once on
the 2022 page; register S817's span (the Sowers-Wills clause) is absent from both chinawriter pages and belongs to
the lane's S880 document. This is a **URL↔quote mispairing**, not a dead payload: `census-adjudication.json` records
campaign ids S758 and S759 with `binding: id` where each id's `url` is paired with the *next* row's quote line — an
off-by-one in the census's row binding (R74-M5).

Bridging for the reader, by document only: register S816 ↔ staged S899 ↔ new lane S883; register S817 ↔ staged S900
↔ new lane S884.

**The four clearing conditions**, all four required before any of these bytes is adopted:

1. The refused rows stay refused — S816 and S817 are not edited, superseded in place, or re-openable by this round.
2. The *documents* are re-opened as new rows (S883, S884), not as a reversal of the register verdicts.
3. The quote must be located on the page this round, from the round-74 capture.
4. The admitted bytes must be a round-74 entry (here the amend file's re-quoted sections), not the staged text.

**All 21 slice rows** (18 `payload-absent` + 3 unreachable-class) carry the standing verdicts recorded in
`reports/round-71/telemetry/quarantine-verdicts.md`, reproduced in `ScoutQuarantine816817.md` §5 and not re-fetched
this round except S816/S817: PRESENT 10 (S776, S778, S795, S796, S804, S820, S823, S824, S825, S827), REFUSED 7
(S779, S786, S787, S792, S814, S816, S817), UNVERIFIABLE 4 (S791, S807, S812, S835) = 21. Two notes travel with the
table: S792's stated reason was wrong (the four headings *are* present; only the reason was) and S824's span came
from a search result rather than the PDF's own text. The round-71 wave-1 file that filed S816 PRESENT was overturned;
the committed table is the record.

## Mistakes

Rules: `CORPUS.md` §"Rules added from the kaika campaign" — one row per mistake, class · evidence pointer ·
captured-by · fix; classes from `.ufo/waves/kaika-w1/mistakes.md` §5. A fix counts only once shown able to fail.

| id | class | evidence | captured-by | fix | state |
|---|---|---|---|---|---|
| R74-M1 | landing | Six round-73 wave-2 seat files were still uncommitted at base `f7104cb`: `CritEntryAmendFinal.md`, `ExecSelftestAll.md`, `ScribeLogScorecard.md`, `SimplifierEntries.md`, `drafts/log-entry.md` (worktree sha256 differs from `git show f7104cb:<path>`) and `RevengerOrigins.md` (untracked, absent from every tree). `corpus/lessons/round-73-verifier-spotcheck.md:13`; `ExecLeftovers.md` verdict table. | none — the verifier spot-check, then `ExecLeftovers` | all six are COMMIT-AS-IS recommendations (`ExecLeftovers.md` §Verdict table: each is the sole carrier of content the landed lesson lacks) and claim Ca's TRACKED leg pins all six blob ids; the six files are committed unchanged in the freeze commit `de93d91c…` (sha256 pinned in the ledger) | fixed at freeze |
| R74-M2 | landing | No PASS-at-lands receipt exists for round 73: `git grep 'ACCEPT-C-73: PASS' f7104cb -- reports/round-73/telemetry` and the corresponding CA form each return 0 lines; the committed telemetry holds only FAIL controls (`controls-c.txt` 1/11, `controls-ca*.txt` 4/9–5/9). The PASS text lives only in wave-2 seat reports. `round-73-verifier-spotcheck.md:15`. | none | claim Ca's RECEIPTS leg materializes a clone of the round-73 lands `2d1cd91…` and re-executes both counters inside it, requiring the exact PASS lines — a typed receipt can no longer substitute; the two receipts `reports/round-74/telemetry/accept-c-73-at-lands.txt` / `accept-ca-73-at-lands.txt` are the stdout of those re-runs | fixed at freeze |
| R74-M3 | survivor | Four counter channels survived round 73 (`MutPredicateC.md` F1–F7): junk landings pass 8 of 12 probes (stub filler, renumbered staged bytes, forged evidence window, invented quotes, lowercase campaign id, fabricated reject row, uncited rows, `claims.json` rewritten at lands); `load_config()` read the graded tree, so a landing shrank its own test; ledger observe commands accepted constant printers; SEPARABLE was wider than frozen. | none before the round | `accept-c.py`/`accept-ca.py` read constants from the frozen commit (`git show <freeze>:reports/round-74/claims.json`, sha256 printed), the ledger allowlist excludes interpreters and constant printers, SEPARABLE is a closed read list, and each junk landing is a committed control expected to FAIL its named leg | pending landing |
| R74-M4 | number-drift | `LOG.md:4297` and the fleet report `.../round-73/kotodama.md:10` say "Ca 9 scenarios", while `reports/round-73/telemetry/selftest-r3.txt:6` prints `SELFTEST OK: 10 scenarios`; `grep -c scenarios SCORECARD.md` = 0, so a SCORECARD third attribution would be red for the wrong reason. `round-73-verifier-spotcheck.md:14`. | none (QUALITY 17/19/23 pin a receipt, not a prose restatement) | the Ca ANNOTATE pair names `LOG.md:4297` and the fleet report only, and its correction row re-derives 10 from the receipt | pending landing |
| R74-M5 | attribution | Register rows S816/S817 bind each URL to the *next* row's quote: `census-adjudication.json` entries S758 (`url` = the 2025 page, `quote` = 这个我肯定考虑过…) and S759 (`url` = the 2022 page, `quote` = the Sowers-Wills clause), both `binding: id`. The fabrication class is the register pair as filed, not the pages and not the staged row text. | `ScoutQuarantine816817.md` §4 (after the round-71 reversal of a false PRESENT) | a row's `url` and `quote` must be read from one row; the checker that pairs them needs an adjacency guard, and the register pair stays refused under the four clearing conditions | open — routed |
| R74-M6 | vacuous | Claim C's EVIDENCE leg asks for a stored window of at least 4096 characters; `reports/round-74/evidence/S882.txt` records `window: chars=2953 min=4096`, and 631 + 33 + 2289 = 2953 is the **whole** extracted page, so no pad can reach the floor. `leg_evidence` does not read the floor, so the limb is unenforced exactly where it is unsatisfiable. Measured this seat (window parse + arithmetic over the landed file). | this seat (`ScribeMistakes`) | either append a claims correction (post-freeze, appended file) lowering the floor to "whole document when shorter", or admit the row with the floor stated in the Gate evidence cell as an exception with its arithmetic | open — routed |
| R74-M7 | scope | The GATE leg's cell cap is 25 whitespace tokens **and** 80 characters; the located S877 sentence is 15 tokens but 108 characters, so the two limbs disagree on which span a cell may carry, and the dispatch quote exceeded the cap it was issued under. | this seat (`ScribeMistakes`), confirmed by the L1 amendment | the cell carries the 54-character, 7-token first clause; the full sentence stays on the evidence file; the conflict is stated in the Gate notes so no later round trims silently | resolved by L1 amendment |
| R74-M8 | reference-drift | Both frozen counters name a path where no counter exists: `claims.json` C.counter is `python3 -B reports/round-74/accept-c.py …` and Ca.counter is `… reports/round-74/accept-ca.py …`, while the only implementations are `.ufo/waves/round-74/counters/accept-c.py` and `…/accept-ca.py` (`find . -name 'accept-c*.py' -path '*round-74*'` returns exactly those two, both untracked; `reports/round-74/` holds `claims.json`, `evidence/`, `telemetry/` only). Additionally, `accept-c.py` does not compile at any of the four revisions measured — `python3 -m py_compile` exits 1, `SyntaxError: line 2159 … ENTRY_TWO_TEXT = _pad_to("""\` — at sha256 `5652c034…`, `ee718a57…`, `fd7bbd2173e561e519e1c93ccc6a354ec07d136fd147bed438b58d1b181ef940` and `0b63cdc613791f20082b50d0ffc064d04b33f916e63d0d0facb397cab5659e18` (22:0x–22:16 local, four successive revisions, same line); `accept-ca.py` (sha256 `b052e9ec…`) compiles. | this seat (`ScribeMistakes`) | the freeze commit must place both counters at the declared paths and `accept-c.py` must compile and print its PASS line from those bytes; otherwise an appended claims correction re-points the command, and no PASS is asserted from a counter that cannot run | open at measurement |

## Frontier-step

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin
kotodama`. **Before:** exit 0, **804 rows** (`reports/round-74/telemetry/census-start.txt`). **After:**
`AFTER-FILLED-BY-L1`. Sourced claim: **C**. `considerthese`: **absent for this lane** (`ls considerthese` → no such
directory), so no proposal is mined this round and no ledger row is added.

## Routed to round 75

1. **Remaining staged families (34 of 40 files).** `narrative-structure-frameworks` (5, staged S870 refused in round
   72), `naming-systems` (11), `calendar-festival-systems` (3), `era-periodization-models` (2), the verification
   amendments (9: citation-format r10–r16, journal-serial r16, reopen-gate), and the conlang amendments
   (`conlang-scholarship.amend-2026-10-23b/-23c/-2026-10-24`, `conlang-methodology.amend-2026-10-24`). Each needs a
   registered parent row with a captured, exactly-once quote before any amendment can cite it.
2. **The four path-present files** (`heritage-taxonomy-models.md` and its r13 amend, `conlang-scholarship.md` and
   its 2026-10-23 amend) need a byte-level decision: the staged copies differ from the lane's in all four, so the
   next round must either diff them for new claims or record them as superseded.
3. **ScoutLedgerSweep leftovers** — live mismatches, not historical: M1 two heritage entries are unindexed
   (`corpus/README.md` 245 index rows vs 247 files) so `sweep.py` is red; M2 the linguistics heading says 30 while
   32 files exist (README-only, no SCORECARD row); M3 `sweep.py` reads the *first* `Counts checked` footer and
   exits 1 although the last footer is right; M4 `SHONEN.md:6` still says "412 rows after round 56" against 804 rows
   (a REPAIR, since SHONEN is not append-only). Also from sweep B: `SKILL.md:594` civilizations "94" vs 95 files,
   `SKILL.md:703`'s "measured 10/11" has no committed receipt, `selftest-r3.txt:6` is truncated mid-word, and the
   fleet report's `c1b5b476…` HEAD sentence is present-tense stale.
4. **R73-M4 decision (from `ExecSelftest72.md`).** No corrected successor to `reports/round-72/accept-c.py` is
   warranted: its real-mode GROUND leg passes on real bytes (lands `21ad3088`, base `b60c7b14`, receipt naming
   797/ihchina 0/bunka 0), and the red `SELFTEST: 10/11` is a fixture artefact — commit `5897ddf` re-pointed
   `leg_ground` to `GROUND_RECEIPT` and left `build_fixture` writing only the old path, so the clean fixture reads a
   file it never writes and the `ground_zeros` mutant passes vacuously. What round 75 owes is the lesson row (already
   in this file's Mistakes table as the R73-M4 successor) and the **QUALITY 23 addendum**: a re-pointed read path
   lands with its fixture in the same commit, and a mutant's redness must be shown against a fixture that is green
   first.
5. **R74-M6 needs an appended claims correction** (floor 4096 vs a 2953-character document) and **R74-M5** needs the
   census binding guard; neither is fixable inside a frozen `claims.json`.
6. **R74-M8 before the freeze:** place the counters at the paths `claims.json` declares
   (`reports/round-74/accept-c.py`, `reports/round-74/accept-ca.py`) and make `accept-c.py` compile; a claim whose
   declared command cannot run cannot emit the PASS its after-state asserts.

## Notes on this draft (what this seat measured, and what it did not)

Measured here, read-only: the five evidence files' headers and windows (bytes, sha256, `window: chars=`, quote
containment after NFKC + whitespace folding); the four staged path-present files' sha256 vs the lane's (all differ);
the 40-file package inventory and its family counts (2 adopted + 4 path-present + 5 + 11 + 3 + 2 + 9 + 4 = 40);
the claim-C GATE/EVIDENCE/REJECTS leg code paths, read as code and then applied to this draft two ways — importing the
counter's own functions from the revision that compiled (before the 22:0x fixture-text edits) and re-implementing the
same rules (`gate_section`, table-row joining, `quoted_spans`, the 25-token recomputation, the reject-row
URL/reason/flip rules, `_window` plus NFKC-fold containment, the refused-family name tests) against the draft — every
check reported below is from those runs: 5 admit rows (6 cells, access date `2026-10-25`, non-dash locator, exactly
one quoted span each at 7/1/1/1/1 tokens and 54/43/33/32/27 characters, one row URL each, verdict `admitted`), 4
reject rows (4 cells each, one URL each, non-dash reason and flip), the family table's last cell never matching
`refused`/`rejected` so it is not read as a reject row, all seven refused-family names present, S882 tied to lane
S877, S899/S900 carrying a re-quote marker, and all five Gate quotes present in their landed windows (4098, 4098,
2953, 4104, 4103 characters). The round-71 verdict table's existence and tally and the adjudication rows S758/S759
were read. Cited but not re-run by this seat: every seat report named above, the census, both counters' PASS verdicts
(the lands state does not exist yet, and `accept-c.py` at sha256 `fd7bbd21…` does not compile), and the live fetches
themselves. No tool was installed; no lane byte outside this draft's directory was written; nothing under the fleet
root, `shokuknow`, or another lane was touched.
