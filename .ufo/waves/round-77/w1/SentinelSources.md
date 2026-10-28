# SentinelSources — round 77 / wave 1 — source-integrity attack on the two claim-C documents

Seat: `SentinelSources` (leaf; no subagents, no background jobs, no labrat probe used).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base revision: `211f9526800906e0c585d878d265c37e5e090c15`.
Documents under attack (staged, read-only): `/home/vgpnk/Projects/shokuknow/lanes/kotodama/round4/SOURCES-PROPOSED.md`
rows `S897` and `S903` plus their `## Gate` blocks. Claim under attack: `.ufo/waves/round-77/CLAIMS-DRAFT.md` claim C
(the D1/D2 provenance lines). Every fetch below is dated **2026-10-27**.
Scratch: `/fast/scratch/hyaku/kotodama-r77/SentinelSources` (deleted on exit; receipts copied into
`w1/stage/SentinelSources/receipts/`).

User agents, bound to the response each request got (QUALITY 22):

| label | UA string |
|---|---|
| `curl` | `curl/8.23.0` (also the tool default when `-A` is absent) |
| `browser` | `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` |

Verdict in one line: **neither staged document is fabricated — the S897 quote is verbatim in the 2024 capture and in
the live page, and the S903 quote, §2–§5 headings, the 88-term count and the 17-lexeme list are all in the PDF — but
the DRAFT's D1 live-probe sentence ("HTTP 403 wall both UAs") is false as written, and the S903 `teaches` cell
overclaims one item of the classification.**

---

## Per-document verdicts

### D1 = staged S897 — 魏斌〈單名與雙名：漢晉南方人名的變遷及其意義〉 — **no fabrication-class defect; one claim-level defect (F1)**

| check | result | evidence |
|---|---|---|
| Wayback capture exists at the stated timestamp | **200**, 143,457 B, both UAs | `s897-wayback-cdx.txt` |
| staged Gate quote verbatim in the capture | **1** occurrence | `s897-capture-quote.txt` |
| quote location = 引言 | yes — quote at text line 238, first numbered section `一、單名與雙名` at line 287 | `s897-capture-quote.txt` |
| `teaches` cell phrases present (春秋戰國 / 華夏式姓名習慣 / 文化接觸) | 2 / 1 / 4 | `s897-capture-quote.txt` |
| article identity + date | `<title>魏斌:單名與雙名…</title>`, `2021-03-16` ×2 | `s897-capture-quote.txt` |
| live URL | **browser 200** (full article), **curl 403** | `s897-live-probe.txt` |

The quote, character for character, from the 20240111092427 capture:

```
$ grep -c '在現代社會中，姓、名共同構成一項人群標記符號。但姓與名實際是有區分的。名的使用要早于姓，兩者組合是一種後起的文化習慣。' s897-cap-curl.html
1
$ grep -o '後起的文化習慣' s897-cap-curl.html | wc -l
1
```

Surrounding text (same capture, tags stripped), which is what the `teaches` cell paraphrases:

```
“人之有名，以相紀別”，[5]在現代社會中，姓、名共同構成一項人群標記符號。但姓與名實際是有區分的。名的使用要早于姓，
兩者組合是一種後起的文化習慣。在不同的文化體中，人名的使用大都有其特定規則。[6]具體到古代中國而言，春秋戰國以降
中原地區逐漸形成穩定的華夏式姓名習慣，即“姓（氏）+名”。[7]這種用漢字標記的姓名系統，包含豐富的尊卑、統屬等觀念，[8]
具有華夏文化標籤的作用。在華夏國家向周邊擴展其勢力的過程中，這種文化標籤也會隨之擴散到周邊地帶。
```

Every clause of the staged `teaches` cell is grounded there: 姓/名 distinct ✓; 名 predates 姓 ✓; the combination is a
later cultural habit ✓; a stable 姓（氏）+名 pattern from 春秋戰國 onward ✓; the pattern spreading with cultural
contact ✓ (`文化接觸` ×4 in the body, and the 結語 states the 華夏化 spread by stratum). **No overclaim.**

### D2 = staged S903 — Kałużyńska (2025), *Onomastica* LXIX, DOI 10.17651/ONOMAST.69.7 — **no fabricated quote or anchor; two `teaches`-cell issues (F2, F3) and one counter-fit issue (F4)**

| check | result | evidence |
|---|---|---|
| live PDF | **200**, `application/pdf`, 417,093 B | `s903-pdf-anchor.txt` |
| Wayback captures named in the DRAFT (`20251231111748`, `20260901045105`) | both present in CDX, `application/pdf` 200 | `s903-wayback-cdx.txt` |
| 20260901045105 capture vs live | **byte-identical** (`sha256 5d1bfa5a5f01bee6…`) | hashes below |
| staged Gate quote | **1** (folded-text match; the PDF wraps the line) | `s903-pdf-anchor.txt` |
| anchor §1–§5 | `1. INTRODUCTION` l.30 · `2. …LEXEMES DENOTING PLANTS, FLOWERS, AND TREES` l.97 · `3. THE MOST COMMON LEXEMES…` l.148 · `4. LIST OF THE 17 MOST COMMON LEXEMES/CHARACTERS` l.211 · `5. CONCLUSIONS` l.407 | `s903-pdf-anchor.txt` |
| the 88-term count | `there were altogether 88 terms` l.151 | `s903-pdf-anchor.txt` |
| the 17-lexeme list | §4 heading l.211, last item `(17) Shù 树 [樹]` l.399 | `s903-pdf-anchor.txt` |
| staged recheck token `grep -c 'Kałużyńska'` | **13** — reproduces exactly | `s903-pdf-anchor.txt` |
| publisher | `Publisher: Institute of Polish Language, Polish Academy of Sciences` l.47 | `s903-pdf-anchor.txt` |
| DOI | `302 → onomastica.ijppan.pl/index.php/ONOM/article/view/574` | `s903-pdf-anchor.txt` |

```
$ tr '\n' ' ' < onomastica.txt > ono-fold.txt
$ grep -o 'standard given names with lexemes reflecting feminine softness and female aesthetic values' ono-fold.txt | wc -l
1
$ grep -nE '^[0-9]\. [A-Z]' onomastica.txt
30:1. INTRODUCTION
97:2. CHINESE FEMALE GIVEN NAMES WITH LEXEMES DENOTING
148:3. THE MOST COMMON LEXEMES DENOTING PLANTS,
211:4. LIST OF THE 17 MOST COMMON LEXEMES/CHARACTERS
407:5. CONCLUSIONS
$ pdftotext -enc UTF-8 onomastica.pdf - | grep -c 'Kałużyńska'
13
```

The article does begin at p. 113 (`FLOWERS, PLANTS, AND TREES IN FEMALE NAMING IN CHINA 113`, l.89), matching the
staged `p. 113–`.

---

## F1 — HIGH (claim fidelity) — the DRAFT's D1 live-probe sentence is false, and the staged S897 recheck command no longer returns its recorded token

**What the DRAFT says** (`CLAIMS-DRAFT.md`, D1 line):

```
- D1 = staged S897 → 魏斌〈單名與雙名…〉, cssn.cn 2021-03-16 — http://lishisuo.cssn.cn/…
  (live: HTTP 403 wall both UAs at L1 probe; Wayback capture 20240111092427 status 200 exists — ordinary means via capture).
```

**Measured, repeated:**

```
$ curl -s -o /dev/null -A 'curl/8.23.0' -w '%{http_code}\n' 'http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml'
403                                             (rep 1 and rep 2)
$ curl -s -o /dev/null -A 'Mozilla/5.0 (X11; Linux x86_64) … Chrome/130.0 Safari/537.36' -w '%{http_code}\n' 'http://…/t20210316_5318560.shtml'
200                                             (rep 1 and rep 2)
$ curl -s -A '<browser UA>' -o live-s897-browser.html -w 'status=%{http_code} bytes=%{size_download}\n' 'http://…'
browserUA status=200 type=text/html bytes=143252
$ grep -c '後起的文化習慣' live-s897-browser.html
1
```

The browser-UA body is the **complete article**, not a wall: normalized text is 28,815 characters and **identical** to the
capture's normalized text (same count for `後起的文化習慣`, `春秋戰國以降`, `華夏式姓名習慣`, `結語`), and the page carries the
article title and `2021-03-16`. So the wall is a plain **User-Agent filter**, not a challenge: `curl`/default UA → 403,
browser-shaped UA → 200. The `https://` variant is unreachable altogether (both UAs `000`, connection timeout), so `http://`
is the only live route.

**Second, coupled defect.** The staged row's `recheck` cell is the literal command
`curl -fsSL 'http://…' | grep -c '後起的文化習慣'` → recorded `1`. Run today, that same command returns `0`:

```
$ curl -fsSL 'http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml' | grep -c '後起的文化習慣'; echo pipeline_exit=$?
curl: (22) The requested URL returned error: 403
0
pipeline_exit=1
```

With the browser UA the same grep returns `1`; against the property-free re-fetch it returns `1` as well.

**Impact.** (a) Any r77 record that repeats "403 both UAs" is a statement whose token does not match the artifact it names —
exactly the defect class claim Ca exists to measure, and it would be authored by the lane itself. (b) If the r77 row copies
the staged recheck command verbatim into its `recheck` cell, the recheck is dead on arrival (403 → 0). (c) QUALITY 18's
"live URL + same-page capture" pair is satisfiable — the live URL does work — so the source is *more* open than the claim
says, not less.

**Smallest remediation.** Rewrite the D1 parenthetical to the measured pair, e.g. `live: browser UA 200 (full article,
143,252 B, text-identical to the capture), curl/default UA 403 — a UA filter, no challenge met; https:// times out
(000); Wayback capture 20240111092427 status 200, 143,457 B`. For the row's `recheck`, either pin the UA
(`curl -fsSL -A '<browser UA>' … | grep -c '後起的文化習慣'` → 1) or grep the committed capture
(`grep -c '後起的文化習慣' reports/round-77/evidence/S897.txt` → 1).

---

## F2 — MEDIUM (overclaim) — the S903 `teaches` cell lists "meteorological phenomena" as one of the classification's lexeme subcategories; in the document it is a third party's observation inside a quotation

**Staged `teaches` cell:** "…the subcategories of given name by lexeme (**plants and trees; meteorological phenomena**; the
standard given name with lexemes reflecting feminine softness and feminine aesthetic values)…"

**What the PDF actually says.** The classification in the document's own voice names one category and one subcategory:

```
According to Kałużyńska (2008, pp. 160, 222), such names may be classified as “standard given names with lexemes
reflecting feminine softness and female aesthetic values,” and belong to the subcategory “given names with lexemes
denoting plants and trees.”
```

`meteorological phenomena` occurs **once** in the whole article, and only inside a quotation of Slaměníková (2018, p. 264):

```
As Slaměníková (2018, p. 264) noticed: “…female names make use of a wide range of plant names and meteorological
phenomena that evoke the idea of beauty, softness, tenderness, etc.”
```

The word `subcategory` occurs twice in the document, both in the Kałużyńska sentence above and in the unrelated
`huācăo zì 花草字` passage earlier in §2 — never attached to meteorological phenomena.

**Impact.** Low-to-medium: a reader of the row would take the enumeration as the document's classification scheme when one
of the three items is a cited author's aside. This is the overclaim class the lesson Gate is meant to police, not a
fabrication (the phrase is in the document, in the same region — §2).

**Smallest remediation.** Drop `meteorological phenomena` from the parenthetical, or attribute it in place
("…; meteorological phenomena, as quoted from Slaměníková (2018) in §2").

---

## F3 — LOW (attribution) — the 88-term count is the 2008 book's research material, restated here; the cell says only "in the material"

**Staged cell:** "…the count of plant, flower and tree terms **in the material**…"

**Document:**

```
According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees
(general terms, species or the parts of flowers or trees) among the names of women figuring in the research material
of the work, and the frequency of their occurring varied.
```

The count belongs to the *2008 work's* material (and the frequency base is the 1991 `Xingshi` statistics; the paper's own
new contribution is the comparison with the 2020–2024 ZQS list). Not a fabrication — the sentence is right there — but the
cell should not let a reader believe the 2025 paper counted 88 terms in its own corpus.

**Smallest remediation.** "…the count of plant, flower and tree terms (88, from her 2008 research material)…".

---

## F4 — LOW (counter fit) — the staged S903 Gate quote is 124 characters; the r76 quote cap it inherits is 80 characters

```
$ python3 -c "q=\"such names may be classified as 'standard given names with lexemes reflecting feminine softness and female aesthetic values'\"; print(len(q), len(q.split()))"
124 18
$ grep -n "MAX_QUOTE_TOKENS\s*=\|MAX_QUOTE_CHARS\s*=" reports/round-76/accept-c.py
251:MAX_QUOTE_TOKENS = 25
252:MAX_QUOTE_CHARS = 80
```

`quote_ok()` in `reports/round-76/accept-c.py:510-513` requires `<= 25` whitespace tokens **and** `<= 80` characters
(r76 comment at `:511`: "The frozen Gate cap: <= 25 whitespace tokens AND <= 80 characters"). The staged S903 quote passes
the token cap (18) and fails the character cap (124). The DRAFT's claim-C text says only "≤25-word located quote", so the
r77 counter may or may not inherit the 80-character leg — but if it does, this quote cannot be used as the evidence quote
as-is. The staged S897 quote is 59 characters / 1 whitespace token, inside both caps (note: CJK has no spaces, so for
Chinese quotes the token cap is vacuous and the character cap is the binding one).

**Smallest remediation (if the cap is inherited).** Quote the shorter, still-located span
`standard given names with lexemes reflecting feminine softness` (60 chars) and, if the subcategory clause is needed,
quote `given names with lexemes denoting plants and trees` (53 chars) as a second located span.

---

## F5 — INFO (positive) — capture provenance for both documents is clean

* S897: capture `20240111092427` → 200 / 143,457 B under **both** UAs, identical bytes
  (`sha256 68c6ed377334199f…`); live browser-UA page text-identical (28,815 normalized chars).
* S903: the `20260901045105` capture is **byte-identical** to the live PDF —
  `sha256 5d1bfa5a5f01bee6…` for both `onomastica.pdf` and `ono-cap-2026.pdf` (417,093 B). The 2025 capture appears in CDX
  (`application/pdf`, 200) but was not fetched — stated as unrun rather than implied.
* No `no-capture` ruling is being made anywhere in this report, so the CDX positive control (QUALITY 21/24) is not
  applicable here.

No fabricated quote, no invented section, no phantom DOI, no wrong journal/publisher in either document.

---

## F6 — RECORD ONLY (no judgment) — the docin / sciscanpub carriers in the rejected set

Requested as a record, not a ruling. The rejected `naming-systems.amend-2026-10-24-r10.md` set cites staged `S939`
(sciscanpub issue PDF) and `S940` (docin upload record); the r77 DRAFT rejects that entry as "carrying a tier-C docin
upload record".

| carrier | measured | class |
|---|---|---|
| `docin.com/p-1248229707` | 200, `<title>姓名的人类学研究 - 豆丁网</title>`, `分享于2015-08-06` present, no login met | **user-upload document mirror** — a third-party upload of a copyrighted article; pirated-class by site kind. The staged S940 row is metadata-only and says so itself ("A user-upload mirror is not a citable carrier of the article's content"), so the row is honest about what it is. |
| `sciscanpub.com` | 200, `<title>HOME_SCISCAN Publishing _Open Access Journal…</title>` | **`SCISCAN Publishing` is an open-access journal platform, i.e. the publisher's own host, not an aggregator.** Credentialed-adjacent (it presents as a publisher, hosts a journal with a DOI footer) but the credential is thin: `doi.org/10.35534/wtt.0304009` → **404**, `api.crossref.org/works/10.35534/wtt.0304009` → **404 "Resource not found"**. |

Two factual corrections to the staged S939 cell, recorded here because they sit inside the rejected set and would otherwise
travel into a later round's reasoning:

1. "an aggregator's scan of the published issue, not the publisher's own file" — the host is the publisher platform, and the
   file is **born-digital**, not a scan: `pdftotext -layout` yields clean typeset text with a per-page footer
   `https://doi.org/10.35534/wtt.0304009`, and the string `sciscan` occurs **0** times inside the PDF.
2. The DOI-unregistered half of the cell is correct (both 404s above).

No judgment on whether the r10 entry may later be admitted; only the carrier classification is recorded.

---

## Unrun / not measured

* The r77 counter (`reports/round-77/accept-c.py`) does not exist yet; no r77 leg was run. The 80-character cap in F4 is
  read from the r76 counter at base (`reports/round-76/accept-c.py:251-252`, `:510-513`) as lineage, not as a frozen r77 rule.
* The `20251231111748` onomastica capture was seen in CDX but not fetched.
* No r77 evidence file has been committed yet, so no r77 `EVIDENCE` leg was attempted on either quote.

## Tooling

No tool was installed or upgraded for this seat; no package manager was invoked (pacman is paused host-wide and was not
touched). `curl 8.23.0`, `pdftotext`, `python3`, `sha256sum` were already present.

Receipts (exact command + raw output, in `w1/stage/SentinelSources/receipts/`):

```
s897-wayback-cdx.txt             CDX row set for the S897 page
s897-capture-quote.txt           capture fetch by UA, quote containment, teaches-cell phrase counts, title/date
s897-live-probe.txt              UA×status table (reps), full-body fetch, the staged recheck command run literally
s903-pdf-anchor.txt              live PDF fetch, folded quote, §1–§5 headings, 88/17, recheck count 13, publisher, DOI
s903-wayback-cdx.txt             both captures in CDX, 2026 capture fetched, quote present in it
rejected-set-docin-sciscanpub.txt docin/docsciscanpub observations, DOI/Crossref 404s, WTT front matter
```
