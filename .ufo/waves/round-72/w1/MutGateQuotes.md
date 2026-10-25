# MutGateQuotes — round-72 w1 mutation test: gate-shape blind spot

Seat: `L1Kotodama72.MutGateQuotes` (mutation-tester, leaf — no subagents).
Date: 2026-10-25. Lane: kotodama-shokunin.

## Assignment

`tools/check-gate-quotes.py` is routed for repair (round-71 lesson, gate-shape
blind spot: pipe-table Gate rows parse as 0 rows). Tool is frozen this round —
not edited by this seat. Required: (1) run it against
`corpus/lessons/round-71.md` and a fixture of the planned round-72 pipe-table
Gate shape carrying a >25-word quote in a pipe row; record that it reports
0 findings regardless; (2) measure the round-72 Gate quotes directly
(`wc -w` per quote cell) and record real lengths.

## 1. Tool run on round-71 lesson (frozen, unmodified)

```
$ python3 -B tools/check-gate-quotes.py corpus/lessons/round-71.md
GATE_QUOTES: 0 findings
exit=0
```

`corpus/lessons/round-71.md:17-31` carries a 13-row pipe-table `## Gate`
(S861–S873, all admit). The tool reports 0 findings: its row regex
`^(?:-\s+(?:\*\s+)?|\*\s+)(S\d+)\b` matches only `- S###`/`* S###` bullets,
so every `| S###` pipe row is skipped (`gate_rows` → 0 rows → 0 findings).
Exit 0. Known blind spot reproduced on the real round-71 lesson.

## 2. Fixture: planned round-72 pipe-table Gate shape with a >25-word quote

Round-72's `## Gate` is planned as the same pipe-table shape (per claim C leg
GATE and ScribeEntries draft brief: per-row source | access date | quote |
grounds | verdict). Fixture built at `/tmp/L1Kotodama72.MutGateQuotes/r72-pipe-gate.md`
(seat scratch; nothing written to lane/fleet):

```
# Round 72 — lesson (kotodama)

## Gate

All claim-C rows opened 2026-10-25 (URL + access date + ≤25-word located
quote, verbatim from the fetched page):

| source | access date | quote (≤25 words) | grounds | verdict |
|---|---|---|---|---|
| S874 — 中国非物质文化遗产网 · 中国非物质文化遗产数字博物馆,「国家级非物质文化遗产代表性项目名录」清单页 | 2026-10-25 | "国务院先后于2006年、2008年、2011年和2014年公布了四批国家级项目名录" | 清单页正文 ¶1; Wayback capture 20200216023423id_ | admitted |
| S875 — 文化遺産データベース（文化庁）文化財検索 | 2026-10-25 | "記録作成等の措置を講ずべき無形文化財" | 詳細検索フォーム 指定区分選択肢; live | admitted |
| S999 — deliberately over-long fixture row | 2026-10-25 | "this quotation is intentionally far longer than twenty-five words so that any working checker must flag it as an obvious over-cap finding inside the gate section" | fixture grounds | admitted |

## Status
```

(`S999` deliberately carries a 26-token quote, far over the 25-word cap in a
pipe row.)

Result:

```
$ python3 -B tools/check-gate-quotes.py /tmp/L1Kotodama72.MutGateQuotes/r72-pipe-gate.md
GATE_QUOTES: 0 findings
exit=0
```

**0 findings despite a 26-word quote.** The pipe-table shape is invisible to
the checker — identical blind spot to round-71, now reproduced on the planned
round-72 shape. Verdict: blind spot confirmed (killed-mutant demonstration:
the defect survives; no source contract was changed).

## 3. Direct measurement of round-72 Gate quotes (`wc -w` per quote cell)

The round-72 lesson draft does not exist yet (ScribeEntries drafted to
`/tmp/r72-lesson.md`, absent at check time), so the quote cells are measured
from the actual evidence the Gate will quote — the verbatim passages fetched
this round (`/tmp/ihchina-2020.html`, `/tmp/ihchina-2026.html`,
`/tmp/bunka.html`), all confirmed present verbatim (presence checks: FOUND 8/8).

| row | quote cell (verbatim evidence) | chars | wc -w tokens |
|---|---|---|---|
| S874 candidate | 国务院先后于2006年、2008年、2011年和2014年公布了四批国家级项目名录 (2020 capture ¶1) | 41 | 1 |
| S874 candidate (2026 page) | 国务院先后于2006年、2008年、2011年、2014年和2021公布了五批国家级项目名录 (2026 capture ¶1) | 43 | 1 |
| S874 candidate | 国家级名录将非物质文化遗产分为十大门类 | 17 | 1 |
| S874 candidate | 编号中的罗马数字代表所属门类 | 14 | 1 |
| S875 candidate | 記録作成等の措置を講ずべき無形文化財 (指定区分 option 8) | 18 | 1 |
| S875 candidate | 安土・桃山 [日本] (時代 ladder option 11) | 12 | 1 |
| S875 candidate | 重要無形民俗文化財 (指定区分 option 7) | 10 | 1 |
| fixture control (over-cap) | this quotation is intentionally far longer than twenty-five words so that any working checker must flag it as an obvious over-cap finding inside the gate section | 161 | 26 |

Cross-checks agree: `printf '%s' '<cell> ' | wc -w` → 1 / 1 / 26; python
`len(split())` on the inner span → same; awk `split()` counts 3/3/28 only
because this awk's `split()` includes empty edge fields (a[1]/a[3]="") — the
non-empty whitespace-token counts are 1/1/26, i.e. identical.

### Measurement finding

All real round-72 Gate quotes measure **≤25** by the checker's own rule
(whitespace tokens). But the rule is effectively vacuous for them: CJK quote
cells contain no whitespace, so any length of Chinese/Japanese quoted text
counts as **1 token** under `split()`/`wc -w`. The over-cap finding is
unreachable for these quotes even after the routed `^\|\s*S\d+` fix lands; the
cap can only trip on whitespace-delimited (typically English) quote cells.
The gate-shape blind spot (0 rows parsed) is therefore doubly harmful for
round 72: quotes are not checked at all today, and a naive fix would still not
constrain CJK quote length (worth a note to the routed repair: decide whether
the cap should count CJK characters/`和`-delimited units rather than
whitespace tokens).

## 4. Selftest (corroboration)

`python3 -B tools/check-gate-quotes.py --selftest` → `SELFTEST: 52/52 pass`,
exit 0. All 52 cases exercise bullet-row shapes only; **no pipe-table case
exists**, matching the round-71 Mistakes row note ("MutGateQuotes ran only
bullet-row selftest fixtures").

## 5. Tool integrity / writes

- Tool frozen: `git status --porcelain -- tools/check-gate-quotes.py` → empty
  (unmodified); `sha256sum` → `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.
  No part of the tool was edited (no mutation applied — probe is the pipe-table
  shape, outputs above).
- No files written to the fleet root or lane except this report; fixture lives
  in `/tmp/L1Kotodama72.MutGateQuotes/` (seat scratch).
- Tool installs: none (python3/awk already present; nothing installed).

## 6. Verdict

| probe | expected detector | actual output | verdict |
|---|---|---|---|
| round-71 pipe-table Gate (13 rows, S861–S873) | ≥0 findings if rows parsed | `GATE_QUOTES: 0 findings`, exit 0 | blind spot reproduced (rows silently skipped) |
| round-72-shaped fixture with 26-word pipe-row quote | ≥1 `over-cap` if parsed | `GATE_QUOTES: 0 findings`, exit 0 | blind spot reproduced (over-cap invisible) |
| selftest | 52/52 | 52/52 | passes, but only bullet-row coverage |

Measured round-72 Gate quote lengths (real): 1, 1, 1, 1, 1, 1, 1 tokens
(all ≤25; CJK cells collapse to 1 token); over-cap control: 26 tokens.
