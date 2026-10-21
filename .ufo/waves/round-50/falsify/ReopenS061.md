# ReopenS061 — attack on SOURCES row S061 (Wiener, Han & Long 2003, *The Yak*, ch. 8/10/12)

Seat: `KotodamaR50-2.ReopenS061-21` (leaf, read-only; no subagents, no background jobs).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes below were read with `git show <sha>:<path>`; the working tree was not used for any
landed claim. No lane writes; the only file written is this report. No clone, no installs.

## Verdict: **HOLDS**

The row URL opens (HTTP 200, no redirect); the Gate quote is an exact substring at the claimed
location (ch. 8 "Management of Yak", Overview ¶1, fourth sentence); the source sentences for the
row's second and third `teaches` facts (butter, dung fuel) are exact substrings at its stated ch. 10 anchors (Overview
¶2 and ¶4); tier B is honest under `corpus/QUALITY.md` criterion 6 for the row's stated scope; and
all three `S061` citations in the knowledge entry are supported by the source text. No fix is
required. Four non-breaking precision notes and one adjacent, out-of-scope landing observation follow
the evidence.

## 1. Row and Gate as landed

Row — `corpus/SOURCES.md:90` (11 cells, matching the header at `corpus/SOURCES.md:28-29`):

```
| S061 | Wiener, Han and Long 2003, The Yak, 2nd ed., FAO RAP 2003/06 — https://www.fao.org/4/AD347E/ad347e0j.htm | book | B | yak husbandry, products and herders' social context on the Qinghai-Tibetan Plateau (ch. 8, 10, 12); FAO synthesis of cited field reports | ch. 8 Management of Yak, Overview ¶1; ch. 10 Products from Yak and Their Utilization, Overview ¶2 and ¶4 (chapter linked from the book contents page https://www.fao.org/4/AD347E/ad347e00.htm) | warm-season high pastures and campsites; butter as the main milk product; dung as fuel | mined | 2026-10-21 | 365d | corpus/knowledge/culture-material/pastoralism-animal-husbandry.md |
```

Gate bullet — `corpus/lessons/round-50.md:46`:

```
- S061 — https://www.fao.org/4/AD347E/ad347e0j.htm — accessed 2026-10-21 — ch. 8 Management of Yak, Overview ¶1: "During the warm season of summer and autumn, yak are on pastures at high elevations and the herdsmen live in campsites". Seat: SrcYak.
```

Cohort: `S048`–`S069` are contiguous at `corpus/SOURCES.md:77-98`, one row per id, and `S061`
occurs once in the registry. The named seat exists at
`.ufo/waves/round-50/build/SrcYak.md`; it records the same three quotes, the same paragraphs, the
same tier reasoning, and HTTP 200 for ch. 8, ch. 10 and ch. 12. The Gate attribution is not invented.

## 2. URL and route

All routes opened this session, direct (no Wayback, no CAPTCHA, no login):

```
$ for u in https://www.fao.org/4/AD347E/ad347e0j.htm \
           https://www.fao.org/4/AD347E/ad347e0l.htm \
           https://www.fao.org/4/AD347E/ad347e00.htm; do
    printf '%s ' "$u"; curl -sS -o /dev/null -w '%{http_code} %{url_effective}\n' --max-time 30 "$u"; done
https://www.fao.org/4/AD347E/ad347e0j.htm 200 https://www.fao.org/4/AD347E/ad347e0j.htm
https://www.fao.org/4/AD347E/ad347e0l.htm 200 https://www.fao.org/4/AD347E/ad347e0l.htm
https://www.fao.org/4/AD347E/ad347e00.htm 200 https://www.fao.org/4/AD347E/ad347e00.htm
```

`https://www.fao.org/4/AD347E/ad347e0v.htm` (ch. 12) also returned **200** and served the chapter
titled `12 SOCIAL, CULTURAL AND ECONOMIC CONTEXT OF YAK PRODUCTION by Wu Ning`, confirming the row's
ch. 12 scope reference. The contents page at `ad347e00.htm` lists exactly the three chapters the row
names: ch. 8 `ad347e0j.htm`, ch. 10 `ad347e0l.htm`, ch. 12 `ad347e0v.htm`.

Identity checks against the contents/title pages: `THE YAK SECOND EDITION`; `RAP Publication
2003/06`; `© FAO 2003`; revised and enlarged by `GERALD WIENER`, `HAN JIANLIN`, `LONG RUIJUN`;
ISBN `92-5-104965-3`. The row's author-year, edition, publisher series and chapter titles are
correct.

## 3. Quote and location — exact

The FAO pages hard-wrap prose in the HTML source. Collapsing all whitespace (the way a browser
renders it) and checking exact substrings gives:

```
ch8 Overview ¶1: HTTP 200 | substring=True | words=21
   before: 'advanced. In general, a transhumance form of management predominates. '
ch10 Overview ¶2: HTTP 200 | substring=True | words=15
   before: 'd principally as a component of "milk tea", which is drunk liberally. '
ch10 Overview ¶4: HTTP 200 | substring=True | words=9
   before: ' Yak heads and tails are also made into ornaments and given as gifts. '
```

The three checked strings were:

1. Gate quote (21 words): `During the warm season of summer and autumn, yak are on pastures at high elevations and the herdsmen live in campsites`
2. ch. 10 butter fact (15 words): `Butter, made in traditional fashion, is the main product from the milk in most places`
3. ch. 10 dung fact (9 words): `Yak faeces is used principally as fuel, after drying`

Location of (1): ch. 8 "Management of Yak" → "Overview" → paragraph 1, fourth sentence, immediately
after "In general, a transhumance form of management predominates." The source sentence continues
", which they move quite frequently"; the Gate quote stops before that comma. The seat report
(`.ufo/waves/round-50/build/SrcYak.md`, "Verbatim quote (21 words)") records the continuation
explicitly, and the quote is a verbatim substring, not a paraphrase. The lane's Gate format uses
short fragments (≤25 words, `corpus/SOURCES.md:7-9`), so the truncation is not a quotation defect.

Location of (2): ch. 10 "Products from Yak and Their Utilization" → "Overview" → paragraph 2, second
sentence. Location of (3): same chapter, "Overview" → paragraph 4 (the hides/hair paragraph), final
sentence. Both match the row's anchor cell exactly.

## 4. Tier and scope under QUALITY criterion 6

`corpus/QUALITY.md:29` (criterion 6) reserves tier A for sources "primary or authoritative for the
exact scope"; `corpus/SOURCES.md:14-19` defines **B** as a "strong secondary (expert write-up with
reproducible detail, survey, textbook)" and **C** as a lead only.

The row claims B for "yak husbandry, products and herders' social context on the Qinghai-Tibetan
Plateau (ch. 8, 10, 12); FAO synthesis of cited field reports". That is honest and not inflated:

- The book is a synthesis, not the authors' primary measurement. Ch. 8 cites Miller (1990),
  Dong *et al.* (1999), Wiener (1996) and Long and Ma (1996); ch. 10 cites Thapa (1996), Joshi
  *et al.* (1999), Schulthess (1986) and others. The row says so in its own scope cell.
- Ch. 8 is management of yak in China, explicitly "the areas of China where the majority of the yak
  live", with plateau and alpine grazing systems; ch. 10's introduction says its account "applies to
  yak-producing parts of China" and is probably similar elsewhere; ch. 12's Overview ¶1 says yak
  keeping is "closely bound up with the social and cultural life of the people, most particularly in
  the vast rangeland grazing areas of the Qinghai-Tibetan Plateau and other parts around the
  Himalayan mountain range." The QTP limitation in the scope cell is conservative, not overbroad.
- B can be sole support for an admitted claim; only tier C is barred from sole support
  (`corpus/QUALITY.md:25-27`). No tier-A claim is made, so there is no criterion-6 inflation to
  correct.

Each row `teaches` item is attested: "warm-season high pastures and campsites" (ch. 8 Overview ¶1);
"butter as the main milk product" (ch. 10 Overview ¶2: "Butter ... is the main product from the milk
in most places"); "dung as fuel" (ch. 10 Overview ¶4: "Yak faeces is used principally as fuel").

## 5. Every `S061` citation in the entry

`git -C <lane> grep -n 'S061' 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0 --` returns exactly five
hits: the registry row (`corpus/SOURCES.md:90`), the Gate bullet (`corpus/lessons/round-50.md:46`),
and three lines in `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (`:7`, `:63`,
`:88`). No other file cites the row, so `used-by` is complete.

- `:7` — shelf bibliography: "S061 Wiener et al. 2003 *The Yak* ch. 8". Bibliographic and accurate
  as far as it goes; see N2 for the chapter-label precision note. No factual claim about yak depends
  on this line alone.
- `:63` — species decision table, Yak row:
  `| Yak | high plateau; summer herds "on pastures at high elevations" (S061) | milk, butter, dung fuel, fibre, pack | vertical seasonal camps | cultural claims bounded to the FAO synthesis (S061) |`
  - `"on pastures at high elevations"` is an exact substring of the Gate quote.
  - "high plateau" matches ch. 8's plateau/alpine systems and ch. 12's QTP framing.
  - "milk, butter, dung fuel, fibre, pack": milk/butter (ch. 10 ¶2 and the Milk and milk products
    section), dung fuel (ch. 10 ¶4 and the Faeces section), fibre (ch. 8 "Harvesting fibre"; ch. 10
    "Hair and down fibre"), pack (ch. 8 Overview ¶2 "steers (pack yak)" and ¶9 "carrying loads").
  - "vertical seasonal camps": ch. 8's warm-season pastures at higher altitudes and cold-season
    pastures "at lower elevations", with campsites moved frequently; the source describes the
    vertical transhumance pattern even though it does not use the word "vertical" in the quoted
    sentence. The compression is faithful.
  - "cultural claims bounded to the FAO synthesis (S061)" is a calibration stance, not an empirical
    claim; the entry makes no yak ritual claim from this row.
- `:88` — products table, Milk and dairy row:
  `| Milk and dairy | living females, repeatable | dairy needs pails, a curd/butter chain and storage; yak butter is the main milk product in most places (S061) |`
  - "pails": ch. 8's milking section describes the milker with "the pail hung from a hook on a
    girdle"; ch. 10's milk-processing sections pour milk into pails.
  - "a curd/butter chain and storage": ch. 10 describes churning butter in a wooden bucket or hide
    bag, storing it in calf-hide/rumen bags for one to two years, soft cheese, and Swiss-type cheese
    with curing/storage.
  - "yak butter is the main milk product in most places" is a faithful paraphrase of ch. 10
    Overview ¶2, and the entry keeps the source's hedge "in most places".

No overreach found in any of the three citations.

## 6. Registry grammar and cohort consistency

Read-only audit of the landed blob (`git show <sha>:corpus/SOURCES.md`), splitting rows on `|` and
checking the header's 11 cells, tier/status enums, the round's opened date, recheck format, and the
existence of every `used-by` path at the commit:

```
S048-S069 rows: 22
issues: []
S061 cells=11: True tier: B status: mined opened: 2026-10-21 recheck: 365d
```

`S061` has no duplicate id, no `supersedes S061` row, and its `status: mined` is consistent with
`used-by` naming an entry that actually cites it. The Gate section has 22 bullets, `S048`–`S069`,
one per row; `S061` is the fourteenth.

## 7. Non-breaking precision notes (no fix required)

- **N1 — the Gate bullet carries one of the row's three attested facts.** The row's `teaches` also
  asserts butter (ch. 10 ¶2) and dung fuel (ch. 10 ¶4), but the Gate bullet quotes only ch. 8 ¶1.
  `corpus/SOURCES.md:7-9` requires each row's URL, access date and a verbatim quote — singular — so
  this is not a contract breach. The seat report already records all three quotes with locations,
  and I re-verified them against the live pages. If a later round wants the Gate self-contained,
  appending the ch. 10 ¶2 quote to a *new* lesson entry (not editing the filed one) is the smallest
  move; no registry change is owed.
- **N2 — entry `:7` labels S061 "ch. 8" while the entry also uses ch. 10 facts.** The row's anchor
  cell supplies ch. 10 ¶2 and ¶4, so the citation is checkable through the registry. If the lane
  wants the shelf list to match the row's scope, "*The Yak* ch. 8, 10, 12" is the smallest wording
  change; this is entry text, not a row defect, and the row remains authoritative.
- **N3 — the row's `scope` names ch. 12 but the `anchor` cell names no ch. 12 section.** Ch. 12 is
  not used by any entry citation; the scope statement itself is supported by the chapter title and
  Overview ¶1, which I opened. If a future claim wants the ritual/social content, the anchor would
  need "ch. 12, Cultural role of yak in Tibetan tradition"; because anchor changes require a
  superseding row (not an in-place edit), that is disproportionate unless such a claim is actually
  filed. No current citation depends on it.
- **N4 — the row's `teaches` drops "in most places" from the butter fact.** The entry restores the
  hedge (`:88`), and the row's scope is already QTP-limited, so the summary does not overgeneralize
  at the level a reader would use it. No change needed.

## 8. Adjacent observation (not an S061 finding)

While locating the receipt named in the round lesson's `source:` line, I observed that
`reports/round-50/validation.json` is **not** in `1c779e4` and is untracked in the worktree
(`git status --porcelain` → `?? reports/round-50/validation.json`; `git ls-tree -r <sha> -- reports`
shows 44 prior `validation.json` receipts, but not round 50's; `git log --all -- '*validation.json'`
shows round-49's receipt landed in a separate ledger commit `3596e2b`). `reports/round-50/run-validation.py`
is also worktree-modified (`M`). This looks like a pending ledger commit rather than an S061 defect,
and it is outside this seat's row; flagging it only so the integrator can confirm the receipt lands
with the round-50 ledger.

## 9. Verification status

- External reads: ch. 8, ch. 10, ch. 12 and the contents page, all HTTP 200, direct.
- Exact-substring checks were run on whitespace-normalized tag-stripped text; the raw HTML's line
  wraps are the only reason a naive non-normalized substring test fails. No fuzzy matching was used.
- Not checked: the print/PDF pagination of *The Yak* 2nd ed. (the row cites chapters/sections, not
  pages); any edition other than the FAO web text; the "in most places" quantifier beyond the
  source's own statement.
- No lane command was run that mutates state; no clone; no `/tmp` files left; no tools installed.
- This report is author-lane advice, not admission.
