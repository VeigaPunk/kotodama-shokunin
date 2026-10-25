# RevengerOrigins — round 73, wave 2 (falsify, hyaku run 7)

Target: landed bytes at `0316b8883b4f8d44b8efd720140e7f52f734a102` (base
`8841ad3b896a0227674fa0725b818c999118046f`). Every landed byte below is read with
`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 0316b88:<path>`; the
working tree is not the target. Experiments ran in a throwaway clone
(`/tmp/tmp.KiihWafBc1/lane`, `git -C /tmp/tmp.KiihWafBc1 rev-parse --show-toplevel`
= `/tmp/tmp.KiihWafBc1`); fetches in `/tmp/revenger/`. No installs (pacman not run).
No lane write except this file.

At read time the lane working tree already carried an **uncommitted** wave-2
corrections section (`git status`: `M .ufo/waves/round-73/w2/...`,
`corpus/lessons/round-73.md` 170 lines in the tree vs 142 at lands) written by
sibling seats. F1/F2/F3 below are therefore corroborations, not first finds; F5/F6
are not in that section.

---

## 0. What I read

- `reports/round-73/claims.json` (frozen), `reports/round-73/ledger.json`,
  `reports/round-73/accept-ca.py` (counter r3).
- Item-10 contract: `/home/vgpnk/Projects/shokunin/.ufo/prompts/kotodama-round-73.md:440`
  ("Assimilation contract (operator directive of 2026-10-24 …)").
- Read-only campaign package: `/home/vgpnk/Projects/shokuknow/merge/kotodama/MERGE-REPORT.md`,
  `SOURCES.append.md` (132 staged rows), `knowledge/corpus/knowledge/linguistics/conlang-scholarship{,.amend-2026-10-23}.md`.
  Nothing under `shokuknow` was written or executed.
- Landed: `corpus/SOURCES.md` S876–S880, both entries, `corpus/lessons/round-73.md`,
  `reports/round-73/evidence/S876..S880.txt`, `SCORECARD.md` corrections, `SKILL.md`,
  `SHONEN.md`, `LOG.md`, `corpus/README.md`.
- Fleet `AXES.md:15` (calibration observable).

---

## 1. Part 1 — CORPUS item 10: does the landing honor the rule it bent?

### 1.1 The rule and its reconstructed intent

The contract text (`.ufo/prompts/kotodama-round-73.md`, item 10, "Scratch
transformation and validation, before any append — **no staged row is appended
as-is**") and its sibling clause:

> "Re-ground each entry in-round under CORPUS.md rule 1: re-open every cited source
> yourself; your Gate block carries YOUR access date and ≤25-word located quote —
> the campaign's `opened` date and quote prove nothing about this lane."

Why the rule exists, from the package itself: the staged rows are campaign-schema —
naive `|`-splitting of `SOURCES.append.md` yields **12** cells per staged row (132
rows, escaped `\|` inside recheck cells), against the lane's 11-column registry — and
the staged anchors carry **locations without quotes** ("article page as served
2026-10-23"). `MERGE-REPORT.md`'s adopt checklist (steps 1–5) adds "Read every `##
Gate` evidence block … spot-reopen a sample of rows". The intent is not cosmetic
renaming: the lane must open the artefact itself, quote it with its own access date,
and let the row text follow the artefact rather than the campaign's summary of it.

**Test used:** substantive re-grounding = the row's source/scope/anchor/teaches cells
carry content the staged cell did not (a quote the campaign did not have, a claim
corrected against the artefact); cosmetic = staged text with id/date/pipe rewriting.

### 1.2 The measured answer: substantive, not cosmetic

Cell-by-cell diff (11 columns × 5 mapped rows):

```
$ python3 - <<'PY'
import re, subprocess
LANE="/home/vgpnk/Projects/shokunin/kotodama-shokunin"
LANDS="0316b8883b4f8d44b8efd720140e7f52f734a102"
S=open("/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md").read()
L=subprocess.run(["git","-C",LANE,"show",LANDS+":corpus/SOURCES.md"],capture_output=True,text=True).stdout
def rows(t):
    o={}
    for ln in t.splitlines():
        m=re.match(r'^ {0,3}\|\s*(S\d{3,})\s*\|',ln)
        if m: o[m.group(1)]=[c.strip() for c in re.split(r'(?<!\\)\|',ln.strip()[1:-1])]
    return o
Lr,Sr=rows(L),rows(S); m={"S876":"S881","S877":"S882","S878":"S892","S879":"S893","S880":"S901"}
cols=["id","source","kind","tier","scope","anchor","teaches","status","opened","recheck","used-by"]
eq=[0]*11; tot=0
for new,old in m.items():
    lc,sc=Lr[new],Sr[old]; r=[i for i in range(11) if lc[i]==sc[i]]; tot+=11
    for i in r: eq[i]+=1
    print(new,"<-",old,"cells",len(lc),"equal",len(r),[cols[i] for i in r])
print("TOTAL equal cells",sum(eq),"of",tot)
for i,c in enumerate(cols): print(f"  {c:9s} equal {eq[i]}/5")
print("substantive cols (source,scope,anchor,teaches,opened,recheck) equal:",sum(eq[i] for i in [1,4,5,6,8,9]),"of 30")
PY
S876 <- S881 cells 11 equal 4 ['kind', 'tier', 'status', 'used-by']
S877 <- S882 cells 11 equal 3 ['kind', 'tier', 'status']
S878 <- S892 cells 11 equal 4 ['kind', 'tier', 'status', 'used-by']
S879 <- S893 cells 11 equal 4 ['kind', 'tier', 'status', 'used-by']
S880 <- S901 cells 11 equal 4 ['kind', 'tier', 'status', 'used-by']
TOTAL equal cells 19 of 55
  id        equal 0/5
  source    equal 0/5
  kind      equal 5/5
  tier      equal 5/5
  scope     equal 0/5
  anchor    equal 0/5
  teaches   equal 0/5
  status    equal 5/5
  opened    equal 0/5
  recheck   equal 0/5
  used-by   equal 4/5
substantive cols (source,scope,anchor,teaches,opened,recheck) equal: 0 of 30
```

19/55 cells are equal, but every equal cell is an enum or status cell (`kind`,
`tier`, `status`) or `used-by`; **0 of 30** substantive cells (source, scope, anchor,
teaches, opened, recheck) are equal. The staged anchors held no quote at all — e.g.
staged S881 anchor = `Abstract + Keywords (Constructed Languages, …) — article page
as served 2026-10-23` — while every landed anchor carries a quote, a locator and the
fetch metadata. That is the opposite of "staged text appended as-is".

The quotes are not merely new, they are true. Live fetch of all five sources, with
sha256 compared to the committed captures (`reports/round-73/evidence/*.txt`):

```
$ sha256sum unito.html conlangs.pdf 20955 anderson-etal-cjl-sotl.pdf
e7260b49370e9a1e715d92b2102eabf8c2c8846f00a94caf3d80138dd019369c  unito.html
e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9  conlangs.pdf
9f745ddaccdbccbf254c5d890cd5b621ab241ea6d6de0219287c2e0c075ed07c  20955
26dbcf2c0fab6d75214df6285e5c7dab92544f598d81a063df91fb4995a0d535  anderson-etal-cjl-sotl.pdf
```

All four match the evidence files byte-for-byte. Verbatim checks (whitespace
collapsed, because `pdftotext` breaks lines):

```
$ grep -c "the construction of languages by students allows them to better grasp the reality of linguistic analysis" unito.html
2
$ pdftotext -enc UTF-8 conlangs.pdf - | tr -s '[:space:]' ' ' | grep -o "Языки, используемые в художественных произведениях, называют вымышленными или фикциональными"
Языки, используемые в художественных произведениях, называют вымышленными или фикциональными
$ pdftotext -enc UTF-8 20955 - | tr -s '[:space:]' ' ' | grep -o "this division should be seen as a scale rather than a binary system"
this division should be seen as a scale rather than a binary system
$ pdftotext -enc UTF-8 20955 - | tr -s '[:space:]' ' ' | grep -o "challenge the integrity of the seemingly well-established dichotomies of a priori and a posteriori, auxiliary and artistic languages"
challenge the integrity of the seemingly well-established dichotomies of a priori and a posteriori, auxiliary and artistic languages
$ pdftotext -enc UTF-8 anderson-etal-cjl-sotl.pdf - | tr -s '[:space:]' ' ' | grep -o "One innovation of this work is that it suggests that a multi-part, creative project can be part of a course even at the introductory level."
One innovation of this work is that it suggests that a multi-part, creative project can be part of a course even at the introductory level.
$ pdftotext -enc UTF-8 anderson-etal-cjl-sotl.pdf - | grep -ci semester
0
$ python3 -c "import re,html;b=open('cyber.html',encoding='utf-8').read();t=re.sub(r'<[^>]+>',' ',b);t=html.unescape(t);print(t.count('2.2. Personal languages'), t.count('Это личные, или персональные, языки'), t.count('Наиболее детализированной классификацией'))"
1 1 1
```

And the staged errors are corrected against the artefact, not re-worded:

- S882 staged scope called the PDF "series announcement booklet"; the landed row says
  the full text was opened and the PDF is **185 pages** (`pdfinfo conlangs.pdf` →
  `Pages: 185`; printed 184 pp.), tier stays B.
- S901 staged claimed "a semester-long language-construction project"; the companion
  PDF has **0** occurrences of `semester` (command above) and the landed row says so.
- S893 staged claimed the review proposes «автоконланги»; the review text has
  `автоконланги` = 0 and `авторскими` = 1 (command above), and the landed row drops
  the term.

Entries: the staged entry bodies were **replaced, not copied** —
`conlang-scholarship.md` 24 → 105 lines, `conlang-scholarship.amend-2026-10-23.md`
50 → 90 lines, `diff | grep -c '^[<>]'` = 117 and 108 changed lines. Eight additional
verbatim quotes I re-checked live (S877 ×2, S878 ×3, S880 ×1, S876 ×2 in-window) are
genuine.

Both counters pass at lands in my clone (with the fleet census script copied into the
clone's parent, because the counter resolves `<root>/../scripts/sources-census.sh`):

```
LEG PASS CENSUS
ACCEPT-C-73: PASS legs=11/11
...
ACCEPT-CA-73: PASS legs=9/9
```

### 1.3 Verdict on part 1

**The landing honors item 10's row rule and its entry rule: this is a substantive
re-grounding, not a cosmetic re-write of staged text.** Two residuals:

1. **Evidence coverage is one quote per row, not one per quote.** The two entries
   carry 30 quoted spans ≥12 chars (`grep -o '"[^"]\{12,\}"'` 9 + 15,
   `grep -o '«[^»]\{12,\}»'` 2 + 4) and the five evidence files carry exactly **1**
   `quote:` line each. The literal Gate requirement is met; "re-open every cited
   source yourself" is only *spot-verifiable* from committed bytes. I verified 9
   quotes beyond the Gate quotes live (S876 ×1, S877 ×6, S878 ×2) and found no
   fabrication; the remaining ~16 quoted spans are unexercised here.
2. **Two of the landed durability/access statements are false** (F1, F2) — exactly
   the class the item-10 Gate exists to prevent.

---

## 2. Part 2 — AXES "calibration": does the eight-pair ledger count mismatches the lane did not choose?

### 2.1 The axis intent

`/home/vgpnk/Projects/shokunin/AXES.md:15`:

> "| **calibration** | Self-assessment quality: gaps named honestly, confidence
> graded, overreach caught | SHONEN.md/SCORECARD entries match observed repo state |"

The observable is a *match predicate over the lane's own self-assessment files*, not
"eight pairs the author picked". `SCORECARD.md:13-15` (cited in `claims.json`) says
the lane holds no numeric rubric, so a records claim is the only way to work the
axis — which makes the denominator the whole question.

### 2.2 The counter cannot discover a mismatch the lane did not write

`reports/round-73/accept-ca.py`, `leg_basemismatch`:

```
def leg_basemismatch(out, pairs, ev, min_pairs):
    mismatched, unobservable, misses = [], [], []
    for idx, pair in enumerate(pairs):
        ...
    passed = (not unobservable) and len(mismatched) >= min_pairs
```

It iterates the ledger's `pairs` only; `--min-pairs 8` is a floor, not a sample.
`BASEMISMATCH` therefore proves "the eight pairs I wrote are red", never "the repo's
self-assessment matches state". The `SEPARABLE`/`LEDGER` legs are green by
construction for the same reason.

### 2.3 One self-assessment mismatch at base that is NOT in the ledger

`SKILL.md` is inside the ledger's declared scope — L08 is a `SKILL.md:697` pair — so
this is a selection, not a scope rule.

```
$ git show 8841ad3b896a0227674fa0725b818c999118046f:SKILL.md | grep -n "94 entries"
594:- `corpus/knowledge/civilizations/` — 94 entries: 92 earlier-civilization
$ git ls-tree -r --name-only 8841ad3b896a0227674fa0725b818c999118046f corpus/knowledge/civilizations | grep -c '\.md$'
95
$ git ls-tree -r --name-only 8841ad3b896a0227674fa0725b818c999118046f corpus/knowledge/civilizations | grep -c 'primary-sources\.md$'
2
$ git show 8841ad3b896a0227674fa0725b818c999118046f:corpus/README.md | grep -n "^## civilizations/"
503:## civilizations/ (95)
$ grep -c civilizations reports/round-73/ledger.json
0
$ git show 0316b8883b4f8d44b8efd720140e7f52f734a102:SKILL.md | grep -n "94 entries"
594:- `corpus/knowledge/civilizations/` — 94 entries: 92 earlier-civilization
$ git show 0316b8883b4f8d44b8efd720140e7f52f734a102:SCORECARD.md | grep -c "94 entries"
0
```

The statement is wrong at base by both of its numbers: 95 files = **93** bases + two
source maps, not 94 = 92 + 2. The lane's own index at the same revision says `(95)`.
It is not in the ledger, not annotated by a round-73 correction row, and still wrong
at lands. The drift is dated and the lane's own commit caused it:

```
$ git log -1 --format='%h %s' 767040e | cut -c1-160
767040e round-56: claim C — civilizations/kongo-kingdom.md (Kingdom of Kongo reference base), README rev 2.13 (civilizations 94 -> 95, total 232), SOURCES S359-S412 (54 rows opened this round, all cited)
$ git show 767040e:corpus/README.md | grep -n "^## civilizations/"
429:## civilizations/ (95)
$ git show 767040e:SKILL.md | grep -n "94 entries"
552:- `corpus/knowledge/civilizations/` — 94 entries: 92 earlier-civilization
```

Round 56 moved the README count and the file count together and left the SKILL corpus
map behind. Ten rounds later the round-73 ledger counts three README count drifts of
exactly this class (L01–L03) and this one not at all.

Secondary, same root as L08 (so not offered as independent evidence): `LOG.md:4255`
says the gates table "now carries one registry row per reports/round-*/accept-*.py
counter: 36 rows … equal to the enumerated file count 36"; at base the table has 36
rows (SKILL.md:662–697) and `git ls-tree … reports/round-*/accept-*.py | wc -l` = 41.

### 2.4 Verdict on part 2

**No — the eight-pair ledger does not count mismatches the lane did not choose.** The
claim is *true as declared* (8/8 red at base, `ACCEPT-CA-73: PASS legs=9/9` at lands,
both reproduced in my clone), but the calibration reading is an author-chosen
denominator: the counter's universe is `ledger.json`, and a same-class mismatch in the
same file set (SKILL.md) is outside it. Under `AXES.md:15`'s observable this is
overreach-not-caught, i.e. the axis's own failure mode. MAJOR (F5), not BLOCKER: no
declared leg is false.

---

## 3. Findings

### F1 — BLOCKER — the S894 refusal's "no Wayback capture" ground is false

At lands, `corpus/lessons/round-73.md:47` (S894 reject row) says: "no Wayback capture
of the same page (CDX 0 for the DOI, the cambridge identifier URL and the slug
prefix)", and `claims.json` pre_data_correction F1 repeats "has no Wayback capture of
the same page". Three probes, all with the browser UA:

```
$ curl -sS -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' \
  'http://web.archive.org/cdx/search/cdx?url=cambridge.org/core/journals/canadian-journal-of-linguistics-revue-canadienne-de-linguistique/article/phonology-from-the-inside-out-constructed-language-as-a-pedagogical-tool*&output=text&limit=10'
org,cambridge)/core/journals/canadian-journal-of-linguistics-revue-canadienne-de-linguistique/article/phonology-from-the-inside-out-constructed-language-as-a-pedagogical-tool/649f8bedbf579512088f614eb2794b59 20241106195515 https://www.cambridge.org/core/journals/canadian-journal-of-linguistics-revue-canadienne-de-linguistique/article/phonology-from-the-inside-out-constructed-language-as-a-pedagogical-tool/649F8BEDBF579512088F614EB2794B59 text/html 200 PHYINBAF4UFJYGIVRKM4FAW772BN5X47 139256
org,cambridge)/core/journals/canadian-journal-of-linguistics-revue-canadienne-de-linguistique/article/phonology-from-the-inside-out-constructed-language-as-a-pedagogical-tool/649f8bedbf579512088f614eb2794b59 20241107004043 https://www.cambridge.org/core/journals/canadian-journal-of-linguistics-revue-canadienne-de-linguistique/article/phonology-from-the-inside-out-constructed-language-as-a-pedagogical-tool/649F8BEDBF579512088F614EB2794B59 text/html 200 QE7UHKBANTDZ55WDAIZUDZ5O5MYXESKH 139614
http_status=200 bytes=1511
```

Two **status-200 text/html** captures exist, and the decoded body carries the article
text (fetched with both required UAs, identical size):

```
$ curl -sS -A '<browser UA>' -o cap_browser.html 'http://web.archive.org/web/20241106195515id_/https://www.cambridge.org/core/journals/canadian-journal-of-linguistics-revue-canadienne-de-linguistique/article/phonology-from-the-inside-out-constructed-language-as-a-pedagogical-tool/649F8BEDBF579512088F614EB2794B59'
browser-UA http_status=200 bytes=1030239
$ curl -sS -A 'curl/8.7.1' -o cap_curl.html '<same URL>'
curl-UA http_status=200 bytes=1030239
$ grep -o "a semester-long language construction project" cap_browser.html | head -2
a semester-long language construction project
a semester-long language construction project
$ grep -o "<title>[^<]*" cap_browser.html
<title>Phonology from the Inside Out: Constructed Language as a Pedagogical Tool | Canadian Journal of Linguistics/Revue canadienne de linguistique | Cambridge Core
```

The same probe refutes the "CDX 0" for the other two URLs:

```
$ curl -sS -A '<browser UA>' 'http://web.archive.org/cdx/search/cdx?url=doi.org/10.1017/cnj.2024.21&output=text&limit=20'
org,doi)/10.1017/cnj.2024.21 20241101042851 https://doi.org/10.1017/cnj.2024.21 text/html 302 WDY6Z7EIDSWCQCFQCVYBGEZIADE7LTON 522
org,doi)/10.1017/cnj.2024.21 20241101082618 https://doi.org/10.1017/cnj.2024.21 text/html 302 WDY6Z7EIDSWCQCFQCVYBGEZIADE7LTON 523
$ curl -sS -A '<browser UA>' 'http://web.archive.org/cdx/search/cdx?url=cambridge.org/core/product/identifier/S0008413124000215/type/journal_article&output=text&limit=10'
org,cambridge)/core/product/identifier/s0008413124000215/type/journal_article 20241101042852 https://www.cambridge.org/core/product/identifier/S0008413124000215/type/journal_article text/plain 301 NODIB77KGF6OM3TXG6JYTNDSYRLJGDCQ 1155
org,cambridge)/core/product/identifier/s0008413124000215/type/journal_article 20241101082618 https://www.cambridge.org/core/product/identifier/S0008413124000215/type/journal_article text/plain 301 NODIB77KGF6OM3TXG6JYTNDSYRLJGDCQ 1161
```

The 429 on the live publisher page is real; the *durability* ground is not. A frozen
claim record (F1) and a Gate reject row state something false. It does not move the
five-row set — S894 is outside it — but the refusal was recorded on a ground that a
single positive-control probe refutes. (Sibling ScoutRejectProbes reached the same
conclusion; the working tree already carries a correction row for it.)

### F2 — BLOCKER — the S879 row's "23443-byte shell that does not carry the span" is false

At lands, `corpus/SOURCES.md:834` scope cell: "Durability: live page only — the one
Wayback capture (20261025222414, made this round) is a 23443-byte shell that does not
carry the span and is not an anchor"; the lesson Gate paragraph repeats it.

```
$ curl -sS --compressed -A '<browser UA>' -o cycap2.html -w 'http_status=%{http_code} bytes=%{size_download}\n' \
  'http://web.archive.org/web/20261025222414id_/https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike'
http_status=200 bytes=23443
$ wc -c cycap2.html
97656 cycap2.html
$ grep -c "Personal languages" cycap2.html
1
$ grep -c "Костюхин" cycap2.html
16
```

23443 B is the gzip wire size; the decoded capture is 97656 B and carries the quoted
span. So S879 has a same-page capture carrying the span — its anchor *is* durable
(QUALITY 18 met), and the row's caveat is the opposite of the truth. The statement is
in an admitted row and in the Gate; it does not change the row's admission (the live
leg is also good) but it is false. (Sibling ScoutReopenS879 has this; I reproduce it.)

### F3 — MAJOR — the S879 entry's "location limit" is false and contradicts its own row

Lands, `conlang-scholarship.amend-2026-10-23.md:56`: "the cyberleninka text is served
as extracted HTML with no page markers, so the page for items 1–2.2 within the
article's pp. 28–34 is (to-verify)". The row at `corpus/SOURCES.md:834` says
"item 2.2 (PDF p. 5 = printed p. 32)". The row is right; the entry is wrong:

```
$ curl -sS -A '<browser UA>' -o kost.pdf -w 'http_status=%{http_code} bytes=%{size_download}\n' \
  'https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike/pdf'
http_status=200 bytes=630227
$ pdfinfo kost.pdf | grep -i '^Pages'
Pages:           7
$ pdftotext -f 5 -l 5 -layout kost.pdf - | grep -n '2.2. Personal languages'
30:2.2. Personal languages                                           классификация Шуваловой и Сидоровой более
$ pdftotext -f 5 -l 5 -layout kost.pdf - | tail -3
32                                                                            Vestnik of MSLU. Humanities. Issue 2 (870) / 2023
```

A 7-page PDF is served at the `/pdf` slug, page 5 is printed page 32, and the
comparison-section heading sits on PDF p. 4 (printed 31). One of two landed statements
had to be false; it is the entry's. (Already in the working-tree wave-2 corrections.)

### F4 — MINOR — S878 quote page is off by one

Lands, `conlang-scholarship.amend-2026-10-23.md:28`: the conclusion quote is cited "18
words, Conclusion, p. 464"; line 3 gives "Conclusion, pp. 464–465". Both are early:

```
$ pdftotext -f 10 -l 10 -layout 20955 - | tail -2
464                                                                               COGNITIVE STUDIES
$ pdftotext -f 11 -l 11 -layout 20955 - | grep -n 'Conclusion'
28:                                         Conclusion
$ pdftotext -f 11 -l 11 -layout 20955 - | tail -2
КОГНИТИВНЫЕ ИССЛЕДОВАНИЯ                                                                         465
```

The Conclusion heading and the quoted sentence are both on printed p. 465 (PDF p. 11);
the Conclusion continues to p. 466. The quote is genuine; the page is wrong. (Already
in the working-tree wave-2 corrections; corroborated.)

### F5 — MAJOR — the calibration ledger's denominator is author-chosen

See §2.3. `SKILL.md:594` states "94 entries: 92 earlier-civilization bases plus two
source maps"; at base the directory holds 95 `.md` files, of which 2 are source maps
(93 bases), and the lane's own README at the same revision says `## civilizations/
(95)`. Not in `ledger.json` (0 mentions), not in the round-73 corrections, unchanged
at lands. The counter's `BASEMISMATCH` leg iterates only the ledger's pairs, so the
claim cannot see it. This is the evidence that the eight pairs are the lane's choice,
not the repo's mismatch set.

### F6 — MINOR — an admitted row carries an unswept negative claim

Lands, `corpus/SOURCES.md:831` teaches cell: "the author states the teaching/research
asymmetry the lane's craft manuals never mention". `CORPUS.md` requires "A negative
claim carries its sweep"; neither the row, the entry, nor the Gate carries one.

```
$ git show 8841ad3b896a0227674fa0725b818c999118046f:corpus/knowledge/linguistics/conlang-methodology.md | grep -c -i 'teach\|marginal\|classroom\|pedagog'
0
$ git show 8841ad3b896a0227674fa0725b818c999118046f:corpus/knowledge/synthesis/conlang-blueprint-template.md | grep -n -i 'teach\|marginal\|classroom\|pedagog'
126:| People/kinship | 091:guest=[ ]; 092:host=[ ]; 093:teacher=[ ]; 094:learner=[ ]; 095:worker=[ ] |
```

The claim happens to be true — `conlang-methodology.md` has 0 hits and the only hit in
`conlang-blueprint-template.md` is the role label `teacher=` (line 126), not the
asymmetry — but as filed it is unverifiable, and the entry's own header shows the lane
knows how to write the sweep (`grep -c 'ojs.unito.it\|philol.msu.ru' corpus/SOURCES.md`
= 0, run 2026-10-25).

---

## 4. What I could NOT check

- **S880's named capture** (`20240801224643`, claimed "same bytes"): `web.archive.org`
  returned HTTP 429, 620 B for the capture fetch. The live PDF matches the committed
  sha (`26dbcf2c…`), so the claim is plausible but unexercised.
- **S877's named capture** (`20260208005339`, claimed "same bytes"): not fetched.
- **S879's evidence capture bytes** (`97622 B`, sha `709e186b…`): the live page now
  serves 97588 B / sha `6ba38146…` (34 B drift); the round's own Wayback capture
  decodes to 97656 B. I could not re-derive the committed capture's exact sha.
- **Every quote in the entries beyond the 5 Gate quotes** (30 quoted spans, 5 bound):
  I spot-verified 8 live and found no fabrication; ~17 are unexercised. Whether the
  seats re-opened those pages in-round is not determinable from committed bytes.
- **The lesson's sibling sweep** ("20 sibling lanes … 0 files in every lane"): not
  re-run (would read 20 sibling repos; out of scope for this item).
- **The SCRATCHMIRROR byte-identity claim**: passed mechanically in my counter run; I
  did not re-derive the mirror sha independently.
- **The 185- vs 184-page wording** (S877): not a defect — printed 184 pp., PDF 185
  pages including the cover.

## 5. Tools and downloads

No installs; pacman not run. Downloads in `/tmp/revenger/`: `unito.html` (30289 B),
`conlangs.pdf` (1055723 B), `20955` (RUDN PDF, 959171 B), `anderson-etal-cjl-sotl.pdf`
(193610 B), `cyber.html` (97588 B), `kost.pdf` (630227 B), `cap_browser.html` /
`cap_curl.html` (1030239 B each), `rudn_cap.pdf` (959171 B), `unito_cap.html`
(30289 B), `cycap2.html` (97656 B decoded / 23443 B wire). UA used on every fetch:
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0
Safari/537.36` (plus `curl/8.7.1` on the Cambridge capture, same bytes).
