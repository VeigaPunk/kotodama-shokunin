# Reopen S058 — Schareika 2003, *Know to Move, Move to Know* (FAO)

Seat: `KotodamaR50-2.ReopenS058-21` (leaf, read-only). Round 50 falsify wave.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes below read with `git show <sha>:<path>`; the working tree was not trusted.
No clone, no lane edit, no git/jj mutation, no installs. Author-lane advice, not admission.

## Verdict: **PARTIAL**

The row and its Gate bullet hold: the URL opens, the Gate quote is verbatim at the stated location,
tier A is honest for the row's narrow scope under `corpus/QUALITY.md:29`, and lines 7, 21 and 153 of
the entry are supported by the opened text.

**One of the four S058 citations fails on scope.** `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:189`
uses S058 for a present-tense "living practice" claim about the WoDaaBe, while the row's own scope says
`not current practice` and the source-opening report explicitly says "never present as current" and
"present-tense sentences need a second, current source or a dated hedge". S058 documents 1996–97
practice, not 2026 practice; the entry offers no current WoDaaBe source anywhere. Smallest fix in §6.

## 1. Row and Gate as landed

Row — `corpus/SOURCES.md:87` (11 cells, `NF==13` on `|`, one S058 row in the file):

```
| S058 | Schareika 2003, Know to Move, Move to Know: Ecological Knowledge and Herd Movement Strategies among the Wodaabe of Southeastern Niger, FAO — https://www.fao.org/4/y5115e/y5115e00.htm | book | A | the WoDaaBe seasonal movement system in southeastern Niger as observed 1996–97, cattle only; not Fulani at large, not current practice | chapter y5115e08 item 2 (baartol); chapter y5115e0d | seasonal moves follow the rains; mobility as a tool for timing an ecological process; named move types | mined | 2026-10-21 | 365d | corpus/knowledge/culture-material/pastoralism-animal-husbandry.md |
```

Gate bullet — `corpus/lessons/round-50.md:43`:

> - S058 — https://www.fao.org/4/y5115e/y5115e00.htm — accessed 2026-10-21 — chapter y5115e08, item 2 (baartol): "Typically, seasonal migration starts with the beginning of the rains in May or June and leads towards the west." Seat: SrcFulani.

Shape check:

```
$ git show 1c779e4:corpus/SOURCES.md | awk -F'|' '/^\| S058 /{print "NF="NF}'
NF=13
$ git show 1c779e4:corpus/SOURCES.md | grep -c '^| S058 '
1
```

`used-by` names the entry path, which exists in the same commit. The Gate cohort has 22 bullets for
S048–S069; S058 is the eighth.

## 2. URL re-opened this session

```
$ curl -sS -m 60 -o /tmp/s058-toc.html -w 'HTTP %{http_code} size %{size_download} url %{url_effective}\n' -L 'https://www.fao.org/4/y5115e/y5115e00.htm'
HTTP 200 size 7108 url https://www.fao.org/4/y5115e/y5115e00.htm
$ curl -sS -m 90 -o /tmp/s058-ch08.html -w 'HTTP %{http_code} size %{size_download} url %{url_effective}\n' -L 'https://www.fao.org/4/y5115e/y5115e08.htm'
HTTP 200 size 17028 url https://www.fao.org/4/y5115e/y5115e08.htm
```

Both routes are direct (`url_effective` identical; no redirect), `Content-Type: text/html`, no bot wall,
no login. Digests of the served bytes:

```
2a18cbd9d46c71b470a90d9f33ef059a0bfa2d1a72db3b2a0ce3c259b29e1abc  s058-toc.html
fbb4b00a94ed5a266d5965ad71711cb618016690dce4b384da0a1729063990ee  s058-ch08.html
```

The row URL is the work root: it carries the title, author, `© FAO 2003`, `ISBN 92-5-105061-9`, and a
TOC whose link `href="y5115e08.htm#bm08"` opens the chapter page that holds the Gate quote. The row's
`source` URL and `anchor` chapter are therefore consistent.

## 3. Quote verbatim and located

Normalising the served HTML (strip tags, unescape entities, collapse whitespace) and substring-testing
the Gate quote:

```
quote_present_normalized: True
list_anchor_at: 2024
quote_index: 3117
```

The quote is the last sentence of item **2. Seasonal migration (*baartol*)** in the list "There are four
types of pastoral movement", in the chapter page `y5115e08.htm` (H1 "THE CULTURE OF MOVING AND THE
PATTERNS OF MOVEMENT"). Raw HTML lines 50–61; the item ends immediately after "…at the beginning of
October." The Gate bullet reproduces the sentence exactly, including "May or June" and "towards the
west", and its location string ("chapter y5115e08, item 2 (baartol)") is correct.

Identity check against the row: title `Know to Move, Move to Know`, subtitle `ECOLOGICAL KNOWLEDGE AND
HERD MOVEMENT STRATEGIES AMONG THE WODAABE OF SOUTHEASTERN NIGER`, author `NIKOLAUS SCHAREIKA`, `© FAO
2003`, `ISBN 92-5-105061-9`. Matches the row's author, year, publisher and kind (`book`).

## 4. Tier and scope under QUALITY criterion 6

`corpus/QUALITY.md:29`: "publisher descriptions and abstracts are tier B for substantive claims about a
work, even when accurate; reserve tier A for sources primary or authoritative for the exact scope."

- **Tier A is honest.** The quoted pages are the monograph's own chapters, and the methods chapter
  (`y5115e05.htm`) states the basis: "ethnological fieldwork which was carried out from February to
  October 1996, from January to April 1997, and from July to December 1997." This is the author's
  first-hand account, not a publisher blurb or a synthesis of others' reports. For the row's exact
  scope — "the WoDaaBe seasonal movement system in southeastern Niger as observed 1996–97" — it is
  primary.
- **The scope is honest.** "Southeastern Niger" is the title's scope; the 1996–97 dates are the methods
  chapter's dates; "not Fulani at large" is honest (the book contrasts the specialised WoDaaBe with
  "Most Fulani in West Africa [who] diversify production", `y5115e07.htm`); "not current practice" is
  honest for a 1996–97 fieldwork account published in 2003.
- **"Cattle only" is a species limiter, not a herd-composition claim.** The book says the WoDaaBe "only
  raise cattle and a few sheep" (`y5115e07.htm`), so the phrase is a compression of "this row backs
  cattle claims only; it has no sheep/goat or camel analysis." No entry sentence uses S058 for sheep or
  camels, so the row's scope is not contradicted by its own entry. A stricter wording is noted at N2;
  it is not a break.

No tier inflation found.

## 5. Citation-by-citation audit of the entry

`git show 1c779e4:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md | grep -n 'S058'`
returns four lines:

| line | landed sentence (excerpt) | supported by what was read? |
|---|---|---|
| 7 | shelf list: "S058 Schareika 2003 (WoDaaBe movement)" | **Yes.** Title/author/scope match the opened work root. |
| 21 | test row: "movement is the production logic, timed to vegetation and season (S058)" | **Yes.** `y5115e0d.htm`: "the nomads use spatial mobility as a tool for timing an ecological process"; `y5115e08.htm` items 1–4 give the named, seasonal move types; `y5115e0c.htm` classifies the year by vegetation state (`seedu`/`ndunngu`). |
| 153 | build step 3: "§3; S058 for a named-move system" | **Yes.** `y5115e08.htm`, list "There are four types of pastoral movement": *perol*, *baartol*, *goonsol*, *sottol*, each with a stated trigger. |
| 189 | "**Living-practice flag.** Mongolian, Sámi, Maasai, Bedu, WoDaaBe and Tibetan herding are living practice (S058, S059, S063). …" | **No, not as scoped.** The present-tense claim "are living practice" is a claim about current practice. S058 is a 1996–97 fieldwork account and the row itself says "not current practice". No current WoDaaBe source is opened or cited anywhere in the entry (`git grep -i wodaabe` over `corpus/` finds no other mention). |

The failure is internal and checkable against the round's own build bytes:

- `.ufo/waves/round-50/build/SrcFulani.md:121`: "1996–97 fieldwork / 2003 publication: **never present as current**."
- `.ufo/waves/round-50/build/SrcFulani.md:154-156`: "**Time.** Fieldwork 1996–97, book 2003. This is a
  historical ethnography of a system, not a report on 2026 conditions. The entry's present-tense
  sentences need a second, current source or a dated hedge."
- The entry's own model for the flag, `culture-material/hunting-foraging-subsistence.md:195`, defines
  the category as a "live subsistence and identity system for real peoples **today**".
- The entry knows how to date a source: its calibration bank already marks S052 as "one 1940
  ethnography" (`:186`) and S057 as "a description only" (`:187`); S058 gets no date hedge.

The sentence's other citation ids do not cover the gap: S059 (Sametinget, page updated 13 December
2024) is the Sámi support and S063 (UNESCO Bedu) the Bedu support; the Mongolian, Maasai and Tibetan
names in the same sentence carry no citation there at all. S058 is the sole support offered for
WoDaaBe, so the unsupported clause is specifically the S058 citation.

## 6. Smallest fix

One line, `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:189`: date-hedge the
WoDaaBe clause (or replace it with a current source), e.g.

```
**Living-practice flag.** Mongolian, Sámi, Maasai, Bedu, WoDaaBe and Tibetan herding are living practice
(S059, S063; WoDaaBe herding documented 1996–97 in S058 — treat as a living people, not as current
conditions). Write fictional herds *like* these mechanics, never *as* these peoples
(`hunting-foraging-subsistence.md:195`).
```

That keeps S058's real support (a documented living people and practice) while removing the
present-tense currency claim the row disclaims. The row itself needs no change; do not "fix" this by
removing `not current practice` from the scope.

## 7. Non-blocking notes

- **N1 — Gate line names the work-root URL, not the quote page.** `corpus/lessons/round-50.md:43` uses
  `y5115e00.htm` and puts "chapter y5115e08" in the location. The quote is on `y5115e08.htm`, which the
  TOC links; the stated location is correct, and the SOURCES header asks for "each row's URL"
  (`corpus/SOURCES.md:9`). The round's source report preferred the Gate line to "name the URL actually
  opened for the quote" (`SrcFulani.md:183-187`). Smallest traceability fix if the lane wants it: swap
  the Gate URL to `https://www.fao.org/4/y5115e/y5115e08.htm`, or add it parenthetically; no claim
  changes.
- **N2 — "cattle only" compresses "cattle and a few sheep".** `y5115e07.htm`: "They only raise cattle
  and a few sheep". The row's scope is a limiter on what it backs (cattle movement), and no entry claim
  depends on sheep, so this is not a falsification. If the lane wants the scope to survive a literal
  reading, the smallest edit is "cattle (a few sheep are mentioned but not analysed)".
- **N3 — the entry never states the 1996–97 date anywhere.** The §6 fix restores it at the one line
  that needs it; the row and Gate already carry it.

## 8. Command log

```
git -C <lane> show 1c779e4:corpus/SOURCES.md | nl -ba | sed -n '87p'
git -C <lane> show 1c779e4:corpus/lessons/round-50.md | nl -ba | sed -n '43p'
git -C <lane> show 1c779e4:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md | nl -ba | sed -n '7p;21p;153p;189p'
git -C <lane> show 1c779e4:corpus/SOURCES.md | awk -F'|' '/^\| S058 /{print "NF="NF}'   # NF=13
git -C <lane> show 1c779e4:corpus/SOURCES.md | grep -c '^| S058 '                        # 1
curl -sS -m 60 -L -w 'HTTP %{http_code} size %{size_download} url %{url_effective}' https://www.fao.org/4/y5115e/y5115e00.htm
curl -sS -m 90 -L -w 'HTTP %{http_code} size %{size_download} url %{url_effective}' https://www.fao.org/4/y5115e/y5115e08.htm
python3 (strip tags, collapse whitespace, substring-test the Gate quote)  # True
sha256sum s058-toc.html s058-ch08.html
```

## 9. Bounds honoured

Read-only: no lane file edited, no `git add/commit/stash/checkout/reset`, no mutating `jj`, no clone,
no background jobs, no delegation, no live-process probing. No installs or updates (pacman paused;
nothing needed). Temp artifacts under `/tmp` were small HTML fetches and were deleted after the checks.
