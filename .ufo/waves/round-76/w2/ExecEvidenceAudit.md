# ExecEvidenceAudit — round 76 wave 2, claim C evidence falsification

Seat: `ExecEvidenceAudit` (WAVE 2 falsification). Lane: `kotodama-shokunin`.
Scope: compare the S894–S896 committed evidence headers and stored windows against the
Gate quotes and the SOURCES anchors. Read-only; nothing outside this report was written.

**Verdict: the three Gate quotes and their stored windows are CORRECT — every quote is
inside its window, every window re-derives from the committed body bytes, and every
SOURCES anchor carries its row's quote. But the three evidence files are NOT round-76
evidence files: they are round-75 files with hand-edited quote/locator/round-banner lines.
Three header-level defects follow, one of them (B) fatal to the round-76 capture grammar
and (C) fatal to any reader that recomputes the geometry from the landed quote.**

Revisions used (committed blobs only, `git show <rev>:<path>`; the mutable worktree was
never read as evidence):

| role | revision |
|---|---|
| base | `98c486bdb4650ba5b8e651d332910e8ee60ad121` |
| frozen C/Ca configuration | `df0f0309d61e5485bb17035d3f8791b1e6a11d40` |
| Ca landing | `a43ed807ea38b5fc5a7875a839d576cea73aba7c` |
| C landing (audit target) | `722e69ff6361aadf148cb46acbf6ac8fd147f59a` |

`reports/round-76/claims.json` is byte-identical at `b4965d5` (the freeze commit) and at
`df0f030` (`git rev-parse` → `c0bb053fdfdeb6f698e6cf5c332e33fb32a8646b` for both), so the
frozen configuration was not moved between the two.

---

## 1. Per-id quote/window correctness — the question asked

**All three PASS on quote/window correctness.** Measured independently (my own
re-implementation of the EVIDENCE leg's rules, plus the committed round-76 producer's own
`locate()` / `verify_file()` / `html_to_text()` functions run against the committed
blobs).

### S894 — National Archives of Japan era table

- Evidence: `reports/round-76/evidence/S894.txt` (37 lines, at C landing).
- Gate row: `corpus/lessons/round-76.md:11`; quote cell 「元号名称 開始西暦年 令和 2019」.
- SOURCES row: `corpus/SOURCES.md:849`; ANCHOR cell carries the same 「元号名称 開始西暦年 令和 2019」.

| check | measured | result |
|---|---|---|
| Gate span == evidence `quote:` header | byte-exact | PASS |
| Gate span == SOURCES ANCHOR span | byte-exact | PASS |
| quote in stored window (verbatim / folded) | True / True | PASS |
| quote tokens / chars vs cap (≤25 / ≤80) | 4 / 18 | PASS |
| `window-sha256` recomputed from stored window | `86428e0a…` | PASS |
| `window-bytes` recomputed | 9059 | PASS |
| scope rule (`excerpt`, 4103 ≥ 4096, ≤ visible 6815) | holds | PASS |
| stored window ⊂ extracted text of committed body | True | PASS |
| body sha256 == evidence `sha256:` | `204b7188…` | PASS |
| `fetch:` line names the row's document | yes | PASS |
| `challenge: none`, `access-date: 2026-10-27`, `http-status: 200` | yes | PASS |

Committed body: `.ufo/waves/round-76/w1/stage/ExecCensusRows/window/S894-digital.archives.go.jp-live-2026-10-27.html`
(311308 B, sha256 `204b7188493573f85b0a7d394983ce90e1a1b1280786643de6c60fc50b763ea8` — equals the
evidence `sha256:`). My re-extraction with the producer's `html_to_text()` + `collapse()`
gives 6815 visible chars, equal to the evidence `visible-chars: 6815`, and the stored
4103-char window is a substring of it (offset 634).

### S895 — openstd GB/T 33661-2017 registry record

- Evidence: `reports/round-76/evidence/S895.txt`.
- Gate row: `corpus/lessons/round-76.md:12`; quote 「标准号：GB/T 33661-2017」.
- SOURCES row: `corpus/SOURCES.md:850`; ANCHOR cell carries the same 「标准号：GB/T 33661-2017」.

| check | measured | result |
|---|---|---|
| Gate span == evidence `quote:` header | byte-exact | PASS |
| Gate span == SOURCES ANCHOR span | byte-exact (fullwidth `：`, U+FF1A) | PASS |
| quote in stored window (verbatim / folded) | True / True | PASS |
| quote tokens / chars vs cap | 2 / 19 | PASS |
| `window-sha256` recomputed | `882d1f9a…` | PASS |
| `window-bytes` recomputed | 1445 | PASS |
| scope rule (`whole-document`, 664 == visible-chars 664 < 4096) | holds | PASS |
| stored window ⊂ extracted text of committed body | True | PASS |
| body sha256 == evidence `sha256:` | `f04feb47…` | PASS |

Committed body: `.ufo/waves/round-76/w1/stage/ExecCensusRows/window/S896-openstd.newGbInfo-capture-20260424031027.html`
(24174 B, sha256 `f04feb475163287e85238628d5425846fde0118ce277daca7081c76058101e0e` — equals the
evidence `sha256:`). The evidence `url:` is the Wayback carrier
`https://web.archive.org/web/20260424031027id_/…/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296`,
which is the same document the SOURCES SOURCE cell names as the captured record.

### S896 — Guangming Daily report

- Evidence: `reports/round-76/evidence/S896.txt`.
- Gate row: `corpus/lessons/round-76.md:13`; quote 「首次明确了农历的编排规则、计算模型和精度等」.
- SOURCES row: `corpus/SOURCES.md:851`; ANCHOR cell carries the same 「首次明确了农历的编排规则、计算模型和精度等」.

| check | measured | result |
|---|---|---|
| Gate span == evidence `quote:` header | byte-exact | PASS |
| Gate span == SOURCES ANCHOR span | byte-exact | PASS |
| quote in stored window (verbatim / folded) | True / True | PASS |
| quote tokens / chars vs cap | 1 / 21 | PASS |
| `window-sha256` recomputed | `3b0fc54b…` | PASS |
| `window-bytes` recomputed | 4005 | PASS |
| scope rule (`whole-document`, 1487 == visible-chars 1487 < 4096) | holds | PASS |
| stored window ⊂ extracted text of committed body | True | PASS |
| body sha256 == evidence `sha256:` | `670850ea…` | PASS |

Committed body: `.ufo/waves/round-76/w1/stage/ExecCensusRows/window/S897-news.gmw.cn-2017-05-23.html`
(25250 B, sha256 `670850ea26dd6de7d480a80d95381d21107b9fbc3cd32414bd4a80123a2366f1` — equals the
evidence `sha256:`).

### Any missing header — the answer to the second half of the question

**Yes: every one of the three files is missing 17 headers.** Not three, not one — the
complete set of 17 keys that the round-76 producer adds over round 75:

```
anchor-quote  anchor-quote-chars  anchor-quote-words  anchor-found  anchor-in-window
anchor-char   quote-in-anchor      quote-anchor-distance
find  find-char  find-page  find-hits  page-count  window-pages
bytes-rule  claims-source  claims-frozen
```

Each file is 37 lines: 32 header lines carrying 32 distinct header keys, with an identical
key set across all three. The round-75 producer's `render()` emits 30 named keys plus the
`window:` geometry line and the `normalise:` line it builds separately — exactly the 32
the landed files carry, so the landed files are byte-for-byte round-75 shapes with the
round-75 key set. The round-76 producer's `render()` emits 47 named keys plus those same
two separately-built lines (49 in total), so 17 keys are absent. The round-76 producer's own
`verify_file()` (`.ufo/waves/round-76/counters/capture-evidence.py`, committed at
`.ufo/waves/round-76/counters/capture-evidence.py`) rejects all three with 8 problems each:

```
missing header key 'anchor-quote'          missing header key 'anchor-found'
missing header key 'anchor-quote-chars'    missing header key 'anchor-in-window'
missing header key 'bytes-rule'            missing header key 'claims-source'
missing header key 'claims-frozen'
no anchor-quote to check (R75-M2: the receipt must carry the row's anchor span)
```

The frozen claim's own EVIDENCE leg text does not require those keys — it requires "fetch
line, the UA used, HTTP status, bytes, the sha256 of the fetched body, the stored
`--- window ---` text and its own `window-sha256:` which the counter recomputes, with a
`window-scope:` header … the Gate quote occurs in the stored window after NFKC and
whitespace folding" (`reports/round-76/claims.json`, claim C, leg 5). So the counter
`accept-c.py` (`leg_evidence`, lines 2697–2750; `_evidence_core`, lines 2606–2695) passes
all three files, and my independent re-implementation of that leg also passes all three.
**The missing headers do not by themselves turn the counter red.** They are nevertheless
load-bearing, because the round-76 producer exists to make the *anchor* binding
machine-checkable (its docstring, lines 18–22 and 137–145: round 75 "stored a `quote:`
that was not the row's anchor span … so two receipts stored a window that did not contain
the anchor at all"), and these three files carry no anchor binding at all.

---

## 2. Defect A — the files are hand-edited round-75 files, not round-76 captures

The three landed files are the w1-stage round-75 captures with lines hand-edited. The
evidence is exact and mechanical.

`reports/round-76/evidence/S894.txt` vs `.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/evidence/S894.txt`
— identical `url:`, identical `sha256:`, identical `window-sha256:`, identical stored window
text; 14 changed lines, all of them hand edits:

```
-# evidence S894 — claim C GATE (round 75)        +# evidence S894 — claim C GATE (round 76)
-quote-words: 7                                   +quote-words: 4
-quote-chars: 29                                  +quote-chars: 18
-quote-found-verbatim: no                         +quote-found-verbatim: yes
-locator: …table rows: 元号名称 header and the 令和/2019, 平成/1989 rows
                                                +locator: …table, headings and first data row
-quote: 元号名称 開始西暦年 令和 2019 選択 平成 1989
                                                +quote: 元号名称 開始西暦年 令和 2019
```

`S895` is the same edit applied to stage `S896.txt` (the Wayback capture of the openstd
record; identical `url:`, identical `sha256:`). `S896` is the same edit applied to stage
`S898.txt` (identical `url:`, identical `sha256:`). The landing files additionally
renumbered the ids (`S896→S895`, `S898→S896`) while the round-75 banner was rewritten to
"round 76" — the file claims to be a round-76 capture whose producer would have written
17 more headers it does not contain.

The capture seat itself declared this in its own report, `.ufo/waves/round-76/w1/ExecCaptureEvidence.md:214`:

> Tool used: `kotodama-shokunin/.ufo/waves/round-75/counters/capture-evidence.py` (read-only use; not …)

and lines 222–224:

> `# evidence <id> — claim C GATE (round 75)`. That is the grammar the ticket asked for; if the
> round-76 counter greps for `round 76` in that comment it must tolerate this (see Risk R5).

So the round-76 banner on the landed files is a **hand edit over a round-75 capture**, not a
round-76 capture. The round-76 producer was committed (`.ufo/waves/round-76/counters/capture-evidence.py`)
but was never used for these three rows.

---

## 3. Defect B — the `window:` geometry line describes the OLD quote, not the landed one

This is the sharpest defect and it is measurable per id. The `window:` header line records
`before=`/`after=` — the quote's character offsets inside the stored window. In all three
landed files those numbers are **the offsets of the pre-edit (round-75) quote**, left behind
when the quote line was shortened by hand.

The producer's own `locate()` (the committed `capture-evidence.py`) recomputed on the landed
window + landed quote gives the correct values; the landed header disagrees:

| id | header `before`/`after` | header brackets a span of | that span is | producer would emit for the landed quote | `before+after+len(quote)` vs `chars` |
|---|---|---|---|---|---|
| S894 | `2037` / `2037` | 29 chars | the **stage** quote `元号名称 開始西暦年 令和 2019 選択 平成 1989` | `2037` / `2048` | 4092 vs 4103 (Δ 11) |
| S895 | `119` / `510` | 35 chars | the **stage** quote `标准号：GB/T 33661-2017 中文标准名称：农历的编算和颁行` | `119` / `526` | 648 vs 664 (Δ 16) |
| S896 | `561` / `871` | 55 chars | the **stage** quote `此次发布的《农历的编算和颁行》首次明确了农历的编排规则、计算模型和精度等，为农历日历编算提供了科学的规范依据。` | `576` / `890` | 1453 vs 1487 (Δ 34) |

In every case the landed `window:` line is arithmetically impossible for its own file:
`before + after + len(quote)` does not equal the recorded `chars`. The line was carried
over verbatim from the stage capture (S894's landed line is byte-identical to stage
S894's: `window: chars=4103 min=4096 pad=400 before=2037 after=2037`).

Note that the frozen counter does **not** read this line — `accept-c.py` reads
`window-sha256`, `window-bytes`, `window-scope`, `visible-chars` and the stored window, and
never parses `before=`/`after=` (grep for `before=` in `reports/round-76/accept-c.py` returns
only the selftest fixture writer at line 5194). So the counter stays green on a line that is
demonstrably stale. The round-76 producer's `render()` computes `before`/`after` from the
quote it is about to store, so a genuine round-76 capture cannot carry this mismatch.

## 4. Defect C — `normalise:` contradicts `quote-found-verbatim:` in two of three files

The producer emits `normalise: … matched=<tier>` from the same `locate()` that sets
`quote-found-verbatim:` (round-76 `render()`, lines 1114–1117 and 1106–1108). Two of the
three landed files contradict themselves:

| id | `normalise:` | `quote-found-verbatim:` | measured tier against the full extracted text | verdict |
|---|---|---|---|---|
| S894 | `… matched=folded` | `yes` | `verbatim` | **contradictory** |
| S895 | `… matched=folded` | `yes` | `verbatim` | **contradictory** |
| S896 | `… matched=verbatim` | `yes` | `verbatim` | consistent |

The landed S894/S895 quotes are byte-verbatim substrings of the extracted text (my
`locate()` on the full extraction returns `tier='verbatim'`), so `matched=folded` is
false — it is the stage capture's tier for the longer stage quote, left in place.
(S894 and S895 both came from stage files whose `quote-found-verbatim: no` / `matched=folded`
was flipped to `yes` by hand while `normalise:` was not updated.)

Both counter and producer treat `quote-found` / `quote-found-verbatim` as human-facing
flags that are never read (`accept-c.py:2515-2518`), so this contradiction does not
fail the EVIDENCE leg — but it is exactly the kind of self-attested inconsistency the
round-76 capture tool was written to eliminate, and a human reader of the file is misled
about how the quote was matched.

---

## 5. Defect D — the S894 and S896 same-page capture carriers are not evidenced

Both SOURCES rows and the Gate table name a second carrier for S894 and S896:

- `corpus/SOURCES.md:849` (S894): "same page in Internet Archive capture of 2026-04-22
  (https://web.archive.org/web/20260422145052id_/…) — live HTTP 200, 311308 bytes; capture
  HTTP 200, 307700 bytes". The admitted entry
  (`corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md:5`)
  additionally states the capture's sha256 `c015e1dce915d4c9f3d3fa6d04e25605cc59547526284372de55112f268a13e0`.
- `corpus/SOURCES.md:851` (S896): "the same article in Internet Archive capture
  https://web.archive.org/web/20170523024955id_/…"; the entry states "a same-page Wayback
  capture exists at timestamp 20170523024955 (status 200)".

Checked against committed bytes:

- **S894 capture: backed.** `.ufo/waves/round-76/w1/stage/ExecCensusRows/window/S894-digital.archives.go.jp-capture-20260422145052.html`
  is 307700 bytes with sha256 `c015e1dce915d4c9f3d3fa6d04e25605cc59547526284372de55112f268a13e0`
  — exactly the digest and byte count the entry and SOURCES row assert. I also confirmed the
  anchor quote `元号名称 開始西暦年 令和 2019` occurs in that capture's extracted visible text
  (6724 chars). So the S894 row's capture claim is truthful; it simply has **no evidence
  file of its own** — `reports/round-76/evidence/S894.txt` covers the live fetch only.
- **S896 capture: NOT backed.** No committed body carries the `20170523024955` capture. The
  only committed gmw bodies are the live page
  (`.ufo/waves/round-76/w1/stage/ExecCensusRows/window/S897-news.gmw.cn-2017-05-23.html`, sha256 `670850ea…`)
  and `.ufo/waves/round-76/w1/stage/ScribeLesson-7/fetch/S937-live-gmw-2017-05-23.html` (same
  digest). The capture's digest `1a187ee4…` appears only in prose in
  `.ufo/waves/round-76/w1/ScoutDocS898.md` — never as a committed body.

This matters because the SOURCES row for S896 asserts the capture as a source of the row
while the row's tier-B scope rests on the article body; and the Gate admit row for S896
(`corpus/lessons/round-76.md:13`) names the capture in its source cell. The capture
existence claim is currently carried by prose only. Note this is *not* a counter failure —
the frozen EVIDENCE leg requires one evidence file per row and `S896.txt` supplies it — it
is an unbacked assertion inside the row text.

---

## 6. What is NOT wrong

- The Gate table is complete and correctly shaped: header row
  `| source | access date | quote (≤25 tokens, ≤80 characters) | locator | evidence | verdict |`
  (`corpus/lessons/round-76.md:5`), three admit rows (lines 7–9) each carrying URL, access
  date `2026-10-27`, a delimited ≤25-token/≤80-char quote, a locator and an evidence path,
  plus a reject table (lines 11–15) whose three rows each carry a probed URL, a reason and a
  flip, and a refused-family table (lines 21–31). The GATE leg's requirements are met.
- Every Gate quote is byte-identical to its evidence `quote:` header and to its SOURCES
  ANCHOR span, for all three ids.
- Every stored window is a genuine substring of the extracted visible text of the committed
  body whose sha256 the evidence file records — the windows were not fabricated.
- `window-sha256` and `window-bytes` recompute exactly for all three; the scope rule
  (`excerpt` ≥4096 and ≤ visible-chars; `whole-document` == visible-chars and <4096) holds
  for all three.
- Every `fetch:` line names the row's own document; every `challenge:` is `none`;
  every `access-date:` is `2026-10-27`; every `http-status:` is `200`.
- The three evidence files are committed at C landing and are identical in the worktree
  (sha256 of `S894.txt` from `git show` == sha256 of the worktree file).

## 7. Risks

1. **The landed files assert a round they were not produced in.** A reader (or a future
   round) that trusts `claim C GATE (round 76)` will expect the r76 grammar, and will find
   none of the 17 r76 keys — including the anchor binding that is the whole point of the
   round-76 capture tool.
2. **`window:` geometry is stale in all three files** and is arithmetically impossible
   against their own quote. Any downstream tool that recomputes the window from
   `before`/`after` (as the r76 producer's `render()` does, and as its own selftest regex
   at `capture-evidence.py:2092` expects) will mis-locate the quote.
3. **`normalise:` contradicts `quote-found-verbatim:` in S894 and S895**, so the recorded
   match tier is false in two of three files.
4. **The S896 capture carrier is prose-only.** If the capture is the row's re-open path,
   the row currently has no committed body for it.
5. The Gate reject row for the showGb alias
   (`corpus/lessons/round-76.md:13`) cites `w1/stage/ExecCensusRows/window/S896-openstd.showGb-followed-2026-10-27.html`
   — that path exists in the committed tree
   (`.ufo/waves/round-76/w1/stage/ExecCensusRows/window/S896-openstd.showGb-followed-2026-10-27.html`),
   so that citation resolves; the stage-file id `S896-openstd.showGb-*` uses the pre-renumber
   id, which is only a naming mismatch, not a missing artifact.

## 8. Blockers / notes

- **No tool install was needed and none was performed.** This was a read-only falsification
  wave over committed bytes; no new tool, version, or channel is recorded. Nothing was
  installed, upgraded, or removed. `pacman` was not touched (it stays paused).
- Scratch used: `/fast/scratch/hyaku/kotodama-r76/ExecEvidenceAudit/` (my own verifier
  script, the two producer copies extracted with `git show`, and its output JSON). It was
  **deleted before this report was written**, per the ticket.
- I did not run any build, test, linter or formatter. The lane's own counter
  (`reports/round-76/accept-c.py`) was **not executed** — I read its EVIDENCE/GATE leg
  source and re-implemented its rules independently in my scratch script. Every claim of
  "PASS" above is my own re-derivation from committed bytes, plus the committed round-76
  producer's own pure functions (`locate`, `verify_file`, `html_to_text`, `collapse`)
  imported and called read-only.
- Nothing was written outside this report. `git status` in the lane is unchanged by me: the
  only pre-existing modifications (`.ufo/waves/round-76/w1/stage/ExecAdaptC/claim-C.json`,
  untracked `reports/round-76/counters/`, `.ufo/waves/round-76/selftest.sh`, `w2.ready*`)
  were present before I started and are not mine.
