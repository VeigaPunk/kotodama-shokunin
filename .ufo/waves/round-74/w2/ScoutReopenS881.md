# ScoutReopenS881 — independent re-open of lane row S881 (LitMemo 世界観の作り方) and its Gate record

Seat: scout, leaf, read-only. Wrote only this file and `/tmp/ScoutReopenS881/` (page.html, b2.html, b3.html, text.txt, ext.py). Repo state: `main` = 1d7add3 (report-side commits after F3 00c408a; landed C = c4bf61a, Ca = 5e4796c). No counters were run (not assigned). No tools installed.

## Verdict in one paragraph

The attack on the Gate record FAILED: the page still hashes to the recorded sha256, the Gate quote is on the page verbatim at the named locator, the evidence window is a true contiguous slice of the page's visible text, the row's anchors and locators exist, and the no-capture ruling reproduces with a working positive control. Every quoted string in the landed entry that cites S881 is present on the page. The attack found only LOW and one MEDIUM-LOW findings: a handful of entry paraphrases that go slightly beyond the page, an unreconciled fetch timestamp between row and evidence, a durability gap (the evidence stores 4098 of 9855 visible characters, and the page was rewritten two days before the capture), and a "paired with tier-B S877" safeguard that is nominal for §3–§9.

## 1. Re-fetch lines (QUALITY 21/22/24)

UA on every fetch below: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` unless marked "no UA".

| # | time (UTC) | command (essentials) | result |
|---|---|---|---|
| 1 | 2026-10-26T02:00:06Z | `curl -sS -L -A "$UA" -D hdr.txt -o page.html -w 'status=%{http_code} size=%{size_download} url=%{url_effective}\n' https://litmemo.com/ja/blog/novel-worldbuilding-guide` | `status=200 size=101615 url=https://litmemo.com/ja/blog/novel-worldbuilding-guide`; `HTTP/2 200`, `content-type: text/html;charset=UTF-8`, `content-length: 101615`, `date: Mon, 26 Oct 2026 02:00:07 GMT`, `cache-control: no-cache, no-store…` |
| 2 | 2026-10-26T02:07:12Z | same with `--compressed --connect-timeout 20 --max-time 90` (the evidence file's own command shape) | `status=200 size=31737` (transfer bytes = the evidence file's `transferred-bytes: 31737`); `cmp b2.html page.html` → identical bytes |
| 3 | 2026-10-26 ~02:07Z | plain `curl -sS -L` (no UA flag; UA `curl/*`) | `status=200 size=101615`, same sha256 — no UA wall |

- sha256 of the body (all three): `441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64`; bytes 101615.
- Recorded in `reports/round-74/evidence/S881.txt:4-5`: `bytes: 101615`, `sha256: 441fc921…ca64` → **hash equality: YES, byte-for-byte, nothing moved.** Same hash also at the wave-1 scout fetch (00:09:12 GMT, `ScoutLitmemo.md:29`) and the evidence fetch (01:09:15Z): four fetches over ~2 h, one hash. The page is `no-cache` but stable in this window.

## 2. Quote found

Gate quote: «自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観を作る。» — 43 characters, 1 whitespace token (CJK; ≤25 tokens satisfied; characters given).

- **Found: Y**, verbatim, exactly once (NFKC+whitespace-folded count = 1; raw-HTML `grep -c` of the exact string = 1 line).
- Location: h3 「3. 外側の層へ因果をつなぐ」 (under h2 「世界観の作り方：5つのステップ」), extracted-text line 54; the paragraph is three sentences: (1) 「生活圏が決まったら、「なぜこの町はこうなっているのか」を外側へたどります。」 (2) the quote, (3) 「この4つの層は次の章で詳しく説明します。」 → the Gate locator "2nd sentence of the paragraph" is exact.
- Evidence file checks (`python3` over `S881.txt`): stored window line (line 33) = 4098 chars, 11709 UTF-8 bytes, sha256 `83e313a9…8809` (= recorded `window-sha256`); quote at index 1270 → `before=1270`, `after=2785`, 1270+43+2785 = 4098 (= recorded geometry); `quote:` line equals the Gate cell string; the window is a contiguous slice (offset 0 → 4098) of my independently extracted, whitespace-folded visible text (`w in tf` → True; my visible length 9856 folded vs recorded `visible-chars: 9855`, i.e. the same text up to one trailing space). Attack on the window: FAILED.

## 3. Row line (corpus/SOURCES.md:836) vs the page

| row element | page evidence | verdict |
|---|---|---|
| title 「世界観の作り方｜小説の世界観設定5ステップと架空の国・魔法の例」 | `<h1>` / breadcrumb, text line 25-26 | carried |
| published 2026-07-16 | visible 「2026年07月16日」; `article:published_time` 2026-07-16T20:50:36Z; JSON-LD Article | carried |
| last updated 2026-10-23 | visible 「最終更新 2026年10月23日」; JSON-LD `"dateModified": "2026-10-23T11:50:12.82078Z"` | carried |
| author LitMemo organisation | JSON-LD Article `author` is an `Organization` named LitMemo (`ScoutLitmemo.md:41`; my grep: 2 Organization nodes, no Person); no byline | carried |
| kind `community`, tier C, "writing-app vendor blog" | footer 「LitMemo is a product of Grogtec LLC」; product CTAs at text lines 121-122, 232-233, 253-263, 284, 301-304 | agree |
| locator h2「世界観の作り方：5つのステップ」(lead sentence and h3 1-5) | text lines 48-58 | carried |
| h2「世界観の4つの層」and h3 第1層..第4層 | lines 70, 79, 85, 91, 97 | carried |
| h3「5. 一か所にまとめ、書きながら更新する」 | line 57 (exact string) | carried |
| FAQ「合作やTRPGなど、複数人で世界観を作るときはどう管理しますか？」 | line 295 (exact string; also in FAQPage JSON-LD) | carried |
| "(43 chars)" | counted 43 | carried |
| teaches: five-step order; four-layer chain; "all collaborators use one settings document as 正本 and change it whenever the text changes" | lines 31, 58, 296 (正本 ×2) | carried |
| wayback carrier | none in the row; the "no capture" statement is in the entry's source line (`worldbuilding-setting-practice.md:4`), not in the row (contrast S882's row, which says "no Wayback capture"). Consistent with live-only; see F2 | n/a |
| "page as served 2026-10-26 00:09 UTC" | page served identically at 00:09:12 (wave-1 scout), but the **Gate evidence is the 01:09:15Z fetch** (`S881.txt:6`) — see F3 | carried, mismatch in provenance |
| status mined / opened 2026-10-25 / recheck 180d / used-by the one entry | entry exists at the path | ok |

**Tier verdict: AGREE with C** (`SOURCES.md` header: "C — lead only, never sole support"; "`community` is never A"). Reasons observed on the page: organisation-authored vendor blog with no named practitioner; product calls to action beside the advice; no cohort, no measurement; the only outside references are second-hand name-drops (Tolkien 1939 lecture, line 154; Sanderson's "law", line 203, no edition; Hemingway's iceberg, line 235). It should not be raised. See F5 on the "paired with tier-B S877" safeguard.

## 4. Every entry sentence citing S881 (`worldbuilding-setting-practice.md`)

Method: `grep S881` gave entry lines 4, 30, 58, 60, 62, 74, 76, 90, 97, 101, 103, 112, 116, 118, 120, 150, 163, 176, 178, 190, 192, 194, 200, 222, 231, 235, 237, 239, 241, 243, 253, plus the uncited-by-id table at 64-68, 82-88, 92-95, 105-110, 152-157, 165-174, 180-188, 202-206, 224-229, 245-251 and the §1 calibration rows (lines 20, 22, 24). All 14 quoted Japanese strings were machine-checked against the page (NFKC+whitespace fold): 世界観の作り方は…5ステップです。 / 物語が起きる世界の決まりごとの総体です / 決めておくのは、展開に直接かかわる核の設定だけで十分です。 / 外側の層が内側の層を決める / 約束を破る者 / 読者は登場人物の目を通して世界を見ます。 / 決めた設定は一つの場所に集め…書き換えます。 / 全員が同じ設定資料を一つだけ使い、それを正本にします。 / 同じ世界でシリーズや複数の作品を書くなら、世界観設定を作品をまたいで共有できます。 / 第3話…第20話で「金竜貨」 → **all found, each exactly once.** (Line 103's 「外側の層が内側の層を決める」 is a verbatim prefix of the page's 「…を決めることです」.) Paraphrase sentences were read against the page text; all are carried except the following, which the page does NOT carry as stated:

| entry line | entry says | page says | severity |
|---|---|---|---|
| 20 (§1 table) | LitMemo page has "no cohort and no citation" | the page does cite: Tolkien's 1939 lecture "On Fairy-Stories" (text line 154), Sanderson, Hemingway; the wave-1 scout wrote "no citations except one named academic reference" (`ScoutLitmemo.md:97`). "no citation" is overbroad (the five-step order and layer chain are indeed uncited) | LOW |
| 60 | a contemporary novel needs the town, workplace/school, invented company or district, "decided once" | FAQ (line 292) is about a *contemporary romance* and lists these items to prevent inconsistency; "once" is not stated anywhere; the table row 現代もの (lines 44-47) gives the general case without "once" | LOW |
| 184 (cost row, under 190's S881 context) | cost options include "standing" | page (line 221): 「周りからの差別」 = discrimination from others, not "standing" | LOW |
| 194 | the keepers are honoured and "their children avoided in marriage" | page (line 231): 「灯台守は町で敬われているが、ほかの家からは縁談を避けられる」 — the keepers (the lighthouse-keeper line) are avoided in marriage matches; "their children" is the entry's reading | LOW |
| 229 (§8 failure table, uncited by id, header "in the sources' own advice") | unused setting → "cut it, or let it resonate somewhere" | LitMemo (line 275) says only to make each setting resonate somewhere in the story; no "cut" advice on this page (the S882 page was not re-opened by this seat, so the "cut" half may be S882's) | LOW |
| 248 (§9 table, uncited by id) | "write the change back the same day" | page: 「その場で設定資料も書き換えます」 (on the spot) | LOW (wording) |

No sentence citing S881 was found to be wholly absent from the page; no invented figure, name or example. The entry's own interpretive sentences (lines 70, 114, 122, 159, 196, the §5 and §6 "question the layer must answer"/"what it prevents" columns) are labelled Design consequence / entry-authored and are not attributed to the page.

## 5. No-capture claim (CDX, canonical slug, positive control)

UA as above; endpoint `https://web.archive.org/cdx/search/cdx`, `output=json`, run 2026-10-26 ~02:00-02:15Z.

| probe | HTTP | body |
|---|---|---|
| `url=litmemo.com/ja/blog/novel-worldbuilding-guide&output=json&limit=20` (canonical slug, exact) | 200 | `[]` (3 bytes) |
| same + `matchType=prefix&limit=50` | 200 | `[]` |
| `url=litmemo.com/ja/blog/novel-worldbuilding-guide*` and `…/` (trailing slash) | 200 | `[]` each |
| `url=www.litmemo.com/ja/blog/novel-worldbuilding-guide` | 200 | `[]` |
| **positive control, same exact-form shape on a sibling slug:** `url=litmemo.com/ja/blog/novel-character-relationship-map&output=json&limit=5` | 200 | `["com,litmemo)/ja/blog/novel-character-relationship-map","20260911102425",…,"200","LN5SCSPMMLK5O3P5453YVM6JTWGOQARJ","18924"]` |
| **positive control, prefix over the same directory:** `url=litmemo.com/ja/blog/&matchType=prefix&output=json&limit=100` (and `litmemo.com/ja/` collapse=urlkey) | 200 | exactly one row — the sibling `novel-character-relationship-map` @ 20260911102425 |
| host-wide: `url=litmemo.com&matchType=domain&output=json&filter=original:.*worldbuilding.*&limit=50` | 200 | one row, a JS asset only: `com,litmemo)/assets/worldbuilding-cr8k19h0.js` @ 20260911102621 — no article capture |
| host liveness in the index: `url=litmemo.com&matchType=domain&output=json&limit=50` | 200 | multiple captures (`litmemo.com/` 20260911102443, 20261010230039; `/.well-known/*` 20261010230340…) |

Disclosed noise: two of my CDX calls returned **503 "Internet Archive: Temporarily Offline"** HTML (11832 bytes) mid-run, and `archive.org/wayback/available` returned HTTP 429 (not used as evidence). The 503s were on the broad `/ja/blog/*` and domain-filter queries and succeeded on retry; every `[]` above came with HTTP 200 and was bracketed by successful positive controls in the same session, so none is an outage artefact. **The no-capture / live-only claim for the canonical slug REPRODUCES** (a capture of the sibling /ja/blog/ page from 2026-09-11 proves the index covers this directory; the article slug, first published 2026-07-16, has none). The probe record itself lives only in seat reports (`w1/ScoutLitmemo.md:105-114`, `w1/ScoutWayback.md:11,22-32,65`), not in `reports/round-74/evidence/S881.txt` (see F2).

## FINDINGS

**F1 (LOW) — six entry paraphrases exceed the page.** Table in §4 above (entry lines 20, 60, 184, 194, 229, 248). Command: `grep`/NFKC-fold of the page text `/tmp/ScoutReopenS881/text.txt` (lines 154, 292, 221, 231, 275, 96) against the entry sentences. Fix: line 20 → "no named practitioner, no cohort, and no source for the order or the chain beyond one 1939 lecture reference"; line 60 → drop "decided once" and scope to "a contemporary romance (the FAQ's case)"; line 184 → "discrimination by others" for 「周りからの差別」; line 194 → "the keepers are honoured but other families avoid marriage matches with them"; line 229 → drop "cut it" or tag the cell S882 if that page carries it; line 248 → "on the spot". Appendable only as a dated amendment (append-only entry lane); none changes a verdict.

**F2 (LOW) — the no-capture ruling is recorded where the gate cannot see it.** Row S881 (SOURCES.md:836) carries no live-only statement (S882's row does: "no Wayback capture"); the entry source line says "CDX holds no capture of this slug, probed 2026-10-25" but gives neither the probe URL nor a positive control; `evidence/S881.txt` has no CDX fields. The probe and control exist only in `.ufo/waves/round-74/w1/ScoutLitmemo.md`/`ScoutWayback.md`. QUALITY 24 asks for a canonical-slug probe *with a positive control*. Fix: add one row-level clause "(live-only; CDX exact/prefix probes of the slug empty, control `/ja/blog/novel-character-relationship-map` @20260911102425 present, probed 2026-10-25)" via the lane's append-only correction route, or record the probe lines in the evidence file in round 75.

**F3 (LOW) — row's fetch time contradicts the Gate evidence's.** Row: "page as served 2026-10-26 00:09 UTC" (SOURCES.md:836, from the wave-1 scout fetch, `ScoutLitmemo.md:3,29`: `date: Mon, 26 Oct 2026 00:09:12 GMT`). Gate evidence: `fetched: 2026-10-26T01:09:15Z` (`S881.txt:6`), `access-date: 2026-10-25` (local, UTC-3). Both fetches hash-identical to mine (441fc921…), so no claim is wrong, but a reader cannot tell which capture the row's sha256 vouches for, and the "UTC date" and the "access date" are on different clocks (2026-10-26 vs 2026-10-25) without a stated basis. Fix: state "access date 2026-10-25 local (UTC-3) = 2026-10-26 UTC" once in the Gate, and name the 01:09:15Z capture as the evidence one.

**F4 (MEDIUM-LOW) — the evidence cannot re-verify most of what the entry cites from this page.** `S881.txt` stores only a 4098-char excerpt (`window-scope: excerpt`, chars 0-4098 of 9855) plus the whole-body sha256; the body itself is not committed anywhere (searched `reports/round-74/evidence/`: `.txt` files only), and the page has no archive copy (§5). The entry's S881 sentences at §3 (partially), §5 layer table, §6 record unit, §7 (country sheet, magic questions), §8, §9 (FAQ 正本, TRPG split, 金竜貨) all lie outside the stored window. The page is `cache-control: no-cache` and its JSON-LD `dateModified` is 2026-10-23, i.e. it was rewritten two days before the capture; if it is edited again the sha256 fails and nothing on disk can say which sentences were once there. Also the stored window is one flattened line without heading markers, so the locator "h3 『3. …』" cannot be checked from the evidence, only from the live page. Command: `python3` read of `S881.txt` line 33 → 4098 chars, `index(quote)=1270`; `ls reports/round-74/evidence/`. Fix: commit the extracted visible text (≈10 KB, 9855 chars) as `evidence/S881.body.txt` (or a second window for the later sections) so the page state is preserved without a Wayback copy; a lane-side substitute for the missing archive carrier.

**F5 (LOW-MEDIUM, tier) — "paired with tier-B S877" is nominal for §3–§9.** Row 836 scope cell: "never the sole support (paired with tier-B S877)". In the entry, S877 carries only §2 (a premise precedes the world; language names a world's realities); the five-step order, four-layer chain, field sets, country/magic sheets, depth scale, failure list and single-source discipline (§3–§9, ~75 % of the lines) are supported by tier-C pages alone (S881, S882). The entry mitigates this honestly — §1 labels every framework "not mainstream — unmeasured", line 32 confines claims about worlds to the monograph, line 26 says "nothing here is contested" — and the header rule is "never sole support for an admitted entry" (the entry as a whole has a B source), so the contract is met technically. Tier C itself: AGREE. Fix (optional): reword the row clause to "paired with tier-B S877 for the premise-first framing only; the method rules are tier-C reports", so the row does not imply wider B support than exists.

**Attacks that FAILED (claim survived), with evidence:** (a) hash drift — four fetches, one sha256, byte-identical (`cmp`); (b) quote absent/altered — found verbatim, once, at the stated h3 and sentence position; (c) window forgery — recomputed window sha256, geometry arithmetic and contiguity all match; (d) row anchors/locators/dates/author — all carried (§3 table); (e) fabricated entry quotations — 14/14 quoted Japanese spans present; (f) no-capture claim — reproduces with a same-host positive control; (g) UA wall — none (browser UA and bare curl both 200, identical bytes).

Not exercised: the Ca/C counters (`accept-c.py`, `accept-ca.py`) were not part of this assignment and were not run; S882's page was not re-opened.
