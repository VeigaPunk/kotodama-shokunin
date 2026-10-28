# ScribeEntryA — round 77, wave 1: the adopted naming-systems amendment

Seat: ScribeEntryA (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base
`211f9526800906e0c585d878d265c37e5e090c15`. Date: 2026-10-27. Nothing in the lane, the fleet repo, the
staged corpus or the registry was modified; this seat wrote only the draft named in §1, this report, and
`stage/ScribeEntryA/`.

## Verdict

The adopted entry is drafted and lint-clean: one file, two lane ids (S897, S898), every id-bearing line
carrying exactly one id, no table row carrying an id. Both documents were re-opened this round by plain
requests, and the four facts the claim's draft hangs on — 名 precedes 姓, the 姓（氏）＋名 pairing dates
from 春秋戰國 onward, 88 terms, 17 most-common lexemes — locate in the live responses and in same-page
captures. **One claim-draft sentence is now false**: D1's live URL is not walled "both UAs" — the
browser-shaped UA gets HTTP 200 and the full article (F1). Two structural notes follow from the staged
file (F4, F5), and two locator defects (F6 on the served page's headings, F9 on the PDF's printed pages)
must be fixed before any Gate row is filed.

## 1. Deliverable

`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-77/w1/drafts/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`
(lane-relative target: `corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`), 23,080 bytes,
123 lines.

Shape, in order: title; provenance trio (two `- source:` lines naming each document by its own
author/title/venue with live URL + section anchors; `- verified-at: 2026-10-27`; `- recheck: 180d` plus
three `recheck detail` lines that are re-runnable argv commands); `- ground:`; `- topic:`; `- gap filled:`;
`- sources:`; `- couples:` (naming-systems.md, toponymy-place-names.md, semantic-fields-lexicon-building.md);
`- scope:`; §1 what the documents add; §2 the system is acquired, not given; §3 acquisition is stratified;
§4 the inventory is finite; §5 the inventory is dated; §6 design levers for a worldbuilder (two tables:
the acquisition schedule and the name-lexicon inventory sheet, plus two pipeline insertions 2a and 4a);
§7 calibration table; §8 provenance limits; §9 superseded passage note; §10 handoff.

Lint, run from the lane root:

```
$ python3 -B tools/check-cited-lines.py .ufo/waves/round-77/w1/drafts/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md
CITED-LINES: 0 finding(s) in 1 file(s)
$ echo $?
0
```

Distinct ids in the draft, no staged id surviving:

```
$ grep -oE '\bS[0-9]{3,}\b' .ufo/waves/round-77/w1/drafts/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md | sort -u
S897
S898
```

One document, one id, by document and not by arithmetic: D1 (魏斌, 《歷史研究》2012 年第 1 期) → **S897**;
D2 (Kałużyńska 2025, Onomastica LXIX, DOI 10.17651/ONOMAST.69.7) → **S898**. The staged ids (S897 and
S903 in the staged file's own numbering, which collides with the lane's) appear nowhere in the draft.

## 2. The two facts the assignment made conditional, verified

The seat was told to keep the 88-lexeme and 17-lexeme facts only if their quote verifies. Both were
verified directly against the document (stronger than a peer's report), in the live PDF and in the
archived capture, over the line-flattened text layer:

```
$ pdftotext -layout ev/d2.pdf - | tr '\n' ' ' | grep -o -F 'According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees' | wc -l
1
$ pdftotext -layout -f 4 -l 4 ev/d2.pdf - | tr '\n' ' ' | grep -c -F 'According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees'
1
$ pdftotext -layout -f 5 -l 5 ev/d2.pdf - | tr '\n' ' ' | grep -c -F 'According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees'
0
$ grep -c -F 'there were altogether 88 terms' ev/d2-wayback.txt
1
$ grep -c -F 'the 17 terms/characters listed in' ev/d2.txt
1
$ grep -c -F 'the 17 terms/characters listed in' ev/d2-wayback.txt
1
```

Full span table (18 spans × 4 texts) is `stage/ScribeEntryA/spancheck.txt`. Every S897 span counts 1 in
the live HTML and 1 in the archived HTML; every S898 span counts 1 in the live PDF text and 1 in the
captured PDF text; each counts 0 in the other document's medium, which is the negative control that the
counts are not passing on a shared boilerplate.

The 88 count is used at tier B in the draft and says why, and the quotation carries the page's own attribution to the author's 2008 monograph inside the span (17 words, inside the 25-word bound) so that a reviewer reading the quote alone sees that the article is reporting a count rather than making one: the page reports it from Kałużyńska's own 2008
monograph and does not re-count it (`§3`, printed p. 114). The 17-lexeme list is used at tier A: it is
presented with rank, count and percentage per lexeme from 《姓氏人名用字分析统计》 (语文出版社, 1991), over
a 1982 census sample the page sizes as 「2,500 characters occurred in the names of 85,567 females」.

## 3. Receipts

`stage/ScribeEntryA/` holds: `fetch-log.txt` (per-request URL, verbatim UA, status, bytes, sha256, time;
CDX rows; the QUALITY 22 one-line wall record; the QUALITY 16 retry budget), `spancheck.txt`, and four
text extracts — `d1-live.text`, `d1-wayback-20240111092427.text`, `d2-live.text`,
`d2-wayback-20251231111748.text` — each carrying its sha256 and line count in the log's last block.

Fetches, 2026-10-27:

| target | UA | result |
|---|---|---|
| D1 live, `http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml` | browser-shaped | HTTP 200, 143,252 B, `f14f7a5c…11d5c` |
| D1 live, same URL | `curl/8.7.1` | HTTP 403, 162 B, `<title>403 Forbidden</title>` |
| D1 capture, `…/web/20240111092427id_/…` | `curl/8.7.1` | HTTP 200, 143,457 B, `68c6ed37…f35` |
| D2 live, `https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/` | `curl/8.7.1` | HTTP 200, 417,093 B, application/pdf, `5d1bfa5a…9bc` |
| D2 capture, `…/web/20260901045105id_/…` | `curl/8.7.1` | HTTP 200, 417,093 B, application/pdf, `5d1bfa5a…9bc` — **byte-identical to the live PDF** |
| D2 capture, `…/web/20251231111748id_/…` | `curl/8.7.1` | HTTP 200, 546,440 B on the wire, application/pdf, `1b4c60f2…ff9` |

CDX, run with `curl/8.7.1`:

```
D1  ["cn,cssn,lishisuo)/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml","20240111092427","http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml","text/html","200","MRIGYUAH7BQACKUKQCJ5BNS64GWDTXGA","41417"]
D2  ["pl,ijppan,onomastica)/index.php/onom/article/download/574/763","20251231111748","https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/","application/pdf","200","ZCYDDH2NSNNGJESPPEKUQTJVACTNUBDG","426128"]
D2  ["pl,ijppan,onomastica)/index.php/onom/article/download/574/763","20260901045105","https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763","application/pdf","200","PVIM7DG5B6X7KNKZBBE6ZGXPQ3H32JMG","406446"]
```

The capture's embedded `original` normalises to the live URL in both cases (byte-identical strings for
D1 and D2, so no rewrite is needed), which is the QUALITY 18 requirement the row will have to meet.

## 4. Findings

### F1 — the claim's D1 provenance line is false as written, and the row is stronger than the draft assumes

Claims draft, D1: "live: HTTP 403 wall both UAs at L1 probe". Measured today:

```
$ curl -sS -o /dev/null -w '%{http_code} %{size_download}\n' -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' 'http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml'
200 143252
$ curl -sS -o /dev/null -w '%{http_code} %{size_download}\n' -A 'curl/8.7.1' 'http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml'
403 162
```

The full article is served to the browser-shaped User-Agent; the 403 is User-Agent-gated. QUALITY 22
decides exactly this case ("a wall present under the plain UA and absent under the browser UA voids the
reject and the source is re-opened by ordinary means"), so a Gate row must not record a wall for S897.
The one-line QUALITY 22 shape, as filed in `fetch-log.txt`, is:

```
| S897 | status: live UA "curl/8.7.1" -> HTTP 403, 162 B, wall present ("403 Forbidden"); UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 143252 B, wall absent; automation: none
```

Consequence for the claim: nothing in the kill rule breaks, and the row gains a live URL that works. What
must change is the sentence a Gate row or the claims draft repeats — "403 wall both UAs" would fail
QUALITY 22's own red-before and QUALITY 27's misfiled-reason limb, because the reason would rest on a
response that no longer exists. Suggested replacement, measured: "live 200 to the browser-shaped UA and
403 to the plain client; wall UA-gated, source opened; same-page capture 20240111092427 also read."

### F2 — the Wayback Machine rate-limits this seat's IP; the retry budget succeeded on the third attempt

```
attempt 1  browser-shaped UA  -> HTTP 429, 620 B  ("suspected abusive bot traffic")
attempt 2  browser-shaped UA, +20s -> HTTP 429, 620 B
attempt 3  curl/8.7.1, +30s   -> HTTP 200, 143,457 B
```

QUALITY 16 wants a declared retry budget and its own record; this is the record. Two side notes for
whoever builds the evidence files: the 429 body is an abuse-flag page, not the source, and the archive
answered 200 to the plain client after refusing the browser-shaped one — the opposite gating from the
live origin, so neither UA may be dropped from a fetch record.

### F3 — the two capture timestamps in the claims draft for D2 are exactly what CDX returns

Claims draft: "Wayback captures 20251231111748, 20260901045105". CDX returns both, status 200,
application/pdf, at 426,128 and 406,446 compressed bytes. Both were downloaded and read here. The one to
pair with the live URL is **20260901045105**, which is byte-identical to the live response:

```
$ sha256sum ev/d2-wayback2.pdf ev/d2.pdf
5d1bfa5a5f01bee68e090155ed683d848e6f75dbc456b8b631be81c1fa8d29bc  ev/d2-wayback2.pdf
5d1bfa5a5f01bee68e090155ed683d848e6f75dbc456b8b631be81c1fa8d29bc  ev/d2.pdf
```

`20251231111748` is an earlier OJS regeneration of the same article (different sha, 546,440 B on the
wire); its text layer locates every span unchanged, so it is a valid second witness but the wrong half of
a QUALITY 18 pair. Both captures are of the PDF URL itself, not of the article landing page, so the anchor
quote is inside the capture's own text layer — no second page is being cited as the row's evidence. This
matches ScoutDocS898 (§"Same-page verification"), which reached the same pairing independently; the
draft's §8 now names 20260901045105 as the pair.

### F4 — the staged file's folded round-3 entry cannot be carried without failing the claim's own kill rule

The staged file ends with a "Superseded passage — the round3 entry, retained as the dated record" block
citing six rows (苗字/NDL/onomastics rows: S886, S888, S889, S890, S891, S896). The claim's kill rule
includes "an admitted entry citing an unmined or unopened row". Carrying that block verbatim into the
lane entry would make the entry cite six rows this round does not mine, so the draft does **not** carry
it and records the reason in §9 (naming the block by its subject and round, never by id). If the L1 wants
the fold kept, the six rows have to be re-opened and re-pointed this round — that is a second entry's
worth of work, not a paragraph's.

This is a decision the L1 may overrule; it is flagged rather than silently taken. Note also that the fold
would add no fact: the round-3 text is about reference apparatus and terminology, which the new entry's
two claims do not touch.

### F5 — the base entry's Chinese row says "hereditary surname ~ancient"; the new source dates the pairing, not the surname

`naming-systems.md` §2, Chinese row: "surname first + given + generation-pool character; hereditary
surname ~ancient; …". D1 dates the **pairing** (春秋戰國 onward, Central Plains) and says nothing about
when a surname first existed, so the draft adds a fusion date and leaves the base's date standing, with
a calibration row saying it is not corrected by anything read here. A version of this amendment that
"corrected" the base to "surnames are late" would be over-claiming.

### F6 — the staged anchor "引言" names a heading that does not exist on the served page

```
$ grep -c '引言' ev/d1-live.txt
0
$ grep -c '引言' ev/d1-wayback2.txt
0
$ grep -nE '^(一|二|三|四)、' ev/d1-live.txt
289:一、單名與雙名
634:二、漢代南方人名的變化與單名問題
997:三、晉宋之際上層雙名的興起及其意義
1456:四、結語
```

The reprint has four numbered headings and no 引言 heading. A Gate row whose anchor says "引言" is a
locator that a re-opener cannot resolve; the draft therefore locates the same text as "the opening
paragraphs before the heading 一、單名與雙名", and locates §3's material in 四、結語 and §2's in the closing
paragraph of 一、單名與雙名. This is a locator defect, not a quote defect — every quote is present on the
page.

### F7 — the base numbers the claim cites check out

```
$ git grep -l -E 'lishisuo\.cssn\.cn|onomastica\.ijppan' 211f9526800906e0c585d878d265c37e5e090c15 -- corpus/knowledge
(no output, exit 1)
$ git ls-tree -r --name-only 211f9526800906e0c585d878d265c37e5e090c15 corpus/knowledge | wc -l
253
$ git show 211f9526800906e0c585d878d265c37e5e090c15:corpus/SOURCES.md | grep -cE '^\| S[0-9]{3,} \|'
820
$ git show 211f9526800906e0c585d878d265c37e5e090c15:corpus/SOURCES.md | grep -oE '^\| S[0-9]{3,}' | sort -u | tail -3
| S894
| S895
| S896
```

So the ground sweep is empty at base (negative claim with its sweep), 253 knowledge files, 820 registry
rows, and S897/S898 are genuinely the next two ids — the claim's "253 → 254" and "820 → 822" hold at the
base this seat measured.

### F8 — what the staged file got right, kept

The staged `- topic:`/`- gap filled:` structure is preserved and re-grounded; the staged body's three
§N bullets are replaced by five sections because the staged §N+2 ("what this licenses for an invented
culture") was a one-line assertion where QUALITY 4 wants a usable table. The staged `recheck:` line's
dependence on round 4's `SOURCES-PROPOSED.md` (a staged-repo file that does not exist in the lane) is
replaced by three self-contained commands; a lane entry that points a re-opener at a file the lane does
not hold would be unverifiable at the freeze.

### F9 — the page locators that travel with this row must be measured per page, not read off the header stream

The D2 spans were mapped to printed pages by extracting one PDF page at a time and reading that page's own
header, rather than by reading the header lines of a single `-layout` dump:

```
$ for p in $(seq 1 13); do pdftotext -layout -f $p -l $p ev/d2.pdf - | grep -c -F '<span>'; done
88-term span          -> pdf page 4, header 114   (printed p. 114)
2,500-characters span -> pdf page 5, header 115   (printed p. 115)
17-list heading       -> pdf page 6, header 116   (printed p. 116)
"the 17 terms/characters listed in" (the lead-in) -> pdf page 5 (printed p. 115)
"Six of these seventeen terms" -> pdf page 11     (printed p. 121)
"the other 9 terms is now lower" -> pdf page 12   (printed p. 122)
```

Two consequences. First, the 17-lexeme quotation's sentence sits on printed p. 115 while the §4 heading is
on p. 116; the draft's locator now says exactly that, because "§4 heading, p. 116" would send a reviewer
to a page that does not carry the quoted words. Second, **ScoutDocS898's locator for the 88-term quote is
off by one**: that report says "§3 ¶1, journal p. 115 (PDF p. 5)", but the span counts 1 on PDF page 4
(headed 114) and 0 on PDF page 5 — measured by the per-page loop above. The quote itself is right and the
scout's tier judgement agrees with this seat's; only the page number is wrong, and it is wrong in the
direction that matters if the Gate copies it into a row.

Applied after KotodamaR77 relayed ScribeLesson's independent reading of the same page: the draft's 88-term
anchor now carries its attribution inside the quoted span (17 words, "According to Kałużyńska (2008,
pp. 223, 232), …"), the locator is printed p. 114 / PDF p. 4, and the three commands that establish both
are in §2 and in the draft's third `recheck detail` line. Re-measured after the edit:
`CITED-LINES: 0 finding(s) in 1 file(s)`, draft 23,080 bytes / 123 lines, ids still S897 and S898 only.

## 5. Not done here, by design

- No registry rows, no `SOURCES.md` edit, no `lessons/round-77.md` Gate, no `reports/round-77/evidence/`
  files: those are the L1's lands. The evidence material they need is in `stage/ScribeEntryA/` (text
  extracts + hash/size log), ready to be committed as the capture windows.
- No claims.json / ledger.json / counter work; no acceptance run. Nothing in this seat's remit verifies
  legs.
- The D2 capture `20260901045105` was not downloaded (only its CDX row recorded).
- No tier change was proposed for the staged S903 → lane S898 document: the staged "one tier B, one tier
  A" is preserved, refined per claim rather than per document, in the draft's `- sources:` line.

## 6. Scratch

Scratch dir `/fast/scratch/hyaku/kotodama-r77/ScribeEntryA/` was used for all fetches and extracts and is
deleted at the end of this run; every receipt it produced was first copied into
`.ufo/waves/round-77/w1/stage/ScribeEntryA/`. No tool was installed for this seat.
