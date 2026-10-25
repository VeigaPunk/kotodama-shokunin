# ScoutMergeScan — round-72 w1 report (leaf seat L1Kotodama72.ScoutMergeScan)

Date: 2026-10-25. Assignment: assimilation-set scan of
`/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/` (READ-ONLY).
Leaf role; no delegation, no subagents, no background jobs. No tools installed (built-ins only;
pacman untouched per the host-wide pause).

## Verdict summary

| # | Question | Answer | Confidence |
|---|---|---|---|
| 1 | Every file of the heritage-taxonomy theme in the merge corpus | **Exactly 2** — `culture-material/heritage-taxonomy-models.md`, `culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md` | high |
| 2 | Every file citing staged rows S863/S867/S967 | **The same 2** — no third file anywhere in the merge tree cites them | high |
| 3 | Do the two adoptions cite ONLY S863/S867/S967 between them? | **Yes for `source:` citations** (S863+S867 in the canonical, S967 in the amendment) — **but the amendment also carries a foreign id `S837` twice** (prose, not `source:`), which in the lane registry names an unrelated row | high |
| 4 | Would any other staged entry need those rows (used-by exclusivity)? | **No.** Only these two entries have S863/S867/S967 as used-by targets; no other staged row or entry references the ihchina/bunka documents | high |
| 5 | Any existing lane file at `corpus/knowledge/culture-material/heritage-taxonomy-models*.md`? | **No at base `b60c7b1`** (`git ls-tree` → empty). During my scan a sibling executor landed the two files at `770100f` — the pre-adoption absence held at the frozen base | high |

---

## 1. Theme inventory (merge corpus, read-only)

`find … -name '*heritage*'` → 2 files. Confirmed by independent keyword sweep
(`grep -rilE 'ihchina|非物质|非物質|文化遺産|heritage|bunka\.go\.jp'`): 5 files match, of which
2 are the theme proper and 3 are adjacent (era/festival amendments that reference the *ladder
concept*, not these rows):

| file | role | cites S863/S867/S967? |
|---|---|---|
| `culture-material/heritage-taxonomy-models.md` | theme, canonical entry | **yes** (S863, S867) |
| `culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md` | theme, amendment | **yes** (S967) |
| `culture-material/era-periodization-models.amend-2026-10-23.md` | adjacent — couples the "filing ladder" | no (S726/S732/S746/S887/S898) |
| `culture-material/era-periodization-models.amend-2026-10-23b.md` | adjacent — mentions "heritage filing ladder" in prose only | no (S757/S908) |
| `myth-symbol/narrative-structure-frameworks.md` | adjacent — couples `culture-material/heritage-taxonomy-models.md` | no (S864/S865/S866/S870/S876) |

`grep -rnE '\bS(863|867|967)\b'` over the **whole** merge tree
(`merge/kotodama/`, all subdirs) returns hits in exactly 3 files: the two theme entries plus
`SOURCES.append.md` (the row definitions themselves, lines 11 / 15 / 115). No other staged entry,
no `amendments/` file, and no `MERGE-REPORT.*` file cites them.

## 2. S-id census inside the two theme files (staged versions)

```
heritage-taxonomy-models.md :4   source: S863 — https://www.ihchina.cn/project.html?tid=4 …
heritage-taxonomy-models.md :5   source: S867 — https://online.bunka.go.jp/db/heritages/search …
heritage-taxonomy-models.md :7   recheck: … (S863 → 1 with `--retry`, S867 → 3) …
heritage-taxonomy-models.amend-2026-10-24-r13.md :4   source: S967 — https://web.archive.org/web/20200216023423id_/…
heritage-taxonomy-models.amend-2026-10-24-r13.md :12  …a single reading of the live page (S837)…
heritage-taxonomy-models.amend-2026-10-24-r13.md :34  …the lane's row S837 had no substitute carrier…
```

**Finding 2a — `S837` is a foreign id, and it points at the wrong document.**
`S837` is not one of the three staged rows and is not a staged id at all (the staged range is
S859–S990). In the *lane* registry (`corpus/SOURCES.md:792`) `S837` = "BBC Religions, *Sikhism:
The Five Ks*" — an unrelated document. In the shokuknow lane, `S837` was the pre-remap id of the
ihchina register row (`ID-REMAP.md:17`: round1 `S837` → `S863`). So the staged amendment cites a
campaign-mirror id that, once landed in the kotodama lane, resolves to BBC Sikhism. This is
exactly the trap the round-71 `id-renumber-map.json` was built to prevent (`ID-REMAP.md`: "the
same id in two rounds names two different rows, so a round-blind substitution would move one
round's citations onto another's rows"). The landed amendment fixes this correctly — its text
now names the ihchina live page instead of an id (see §5).

**Finding 2b — the `recheck:` line of the canonical is a two-id line.**
`check-cited-lines.py` over the two *staged* files prints:
`MULTI-ID …/heritage-taxonomy-models.md:7 S863,S867` → `CITED-LINES: 1 finding(s) in 2 file(s)`,
exit 1. Under claim C leg CITEDLINES ("prints 0 findings") the staged text as-is would fail.
The landed pair prints **0 findings, exit 0** (verified) because the recheck line was rewritten
to name the normalized rows' commands rather than the two staged ids.

## 3. Used-by exclusivity for the new registry rows

`SOURCES.append.md` staged rows (parsed by unescaped-pipe split; every row has exactly 11 cells):

| staged row | source cell | used-by cell |
|---|---|---|
| S863 | ihchina `清单页` (live) | `corpus/knowledge/culture-material/heritage-taxonomy-models.md` |
| S867 | bunka 文化財検索 | `corpus/knowledge/culture-material/heritage-taxonomy-models.md` |
| S967 | ihchina via Archive capture 2020-02-16 | `corpus/knowledge/culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md` |

Cross-checks (all negative, i.e. exclusivity holds):

- **URL sweep of the whole staged table** (132 rows): only S863/S967 carry an `ihchina.cn` URL;
  only S867 carries a `bunka.go.jp` URL; only S967 carries the `20200216023423` capture URL.
  No other staged row names any of the three documents.
- **Citation sweep of the whole merge knowledge tree** (§1): no third entry cites them.
- **Textual sweep**: `grep -rn 'ihchina\|bunka.go.jp' merge/kotodama/knowledge/` returns hits only
  inside the two theme files. The era/festival amendments that talk about a "heritage filing
  ladder" cite **different** rows (S726/S732/S746/S887/S898/S757/S908 — all present in the lane
  registry as *different* documents, e.g. lane `S726` = Ochs & Schieffelin "Bambi"; lane `S732` =
  Hoff "Bilingual Development"; lane `S757` = Huizinga *Homo Ludens*). The staged
  `era-periodization-models.amend-2026-10-23.md` prose ("round 1's S726") is therefore also a
  round-scoped campaign id, not a lane id — but that entry is **not** part of this adoption, so
  it creates no collision here. Flagged only so the next adopter of the era amendments knows.
- **Lane-side gap sweep at base** `b60c7b1`: `grep -icE 'ihchina|非物质|非物質|文化遺産|heritage
  online|bunka' corpus/SOURCES.md` → **0**, registry 797 rows. So neither of the two new documents
  had a pre-existing lane owner; the "used-by" of the new rows is genuinely exclusive to the two
  admitted entries. Matches claim C's GROUND leg.

**Finding 3a — namespace collision on the *staged* ids S874/S875.**
The merge package's own staged table already contains `S874` and `S875` — the *onomastics*
psychology rows (S791/S792 in the register), used-by `corpus/knowledge/linguistics/naming-systems.md`.
The round-71 renumber map (`id-renumber-map.json`) assigns `S859→S874`, `S860→S875`, `S863→S878`,
`S867→S882`, `S967→S982` — i.e. the whole staged set is meant to land from S874 upward, and the
map's *own* targets for staged S863/S867/S967 are **S878/S882/S982**, not S874/S875. The round-72
adoption instead used S874/S875 for the *heritage* documents (re-pointed by document, per the
claim's "no arithmetic" rule), which means:

- the round-71 map is now **stale for the heritage rows** — it would map staged S863/S867/S967 to
  S878/S882/S982, and staged S859/S860 to S874/S875, i.e. onto the two ids the heritage rows now
  occupy. Its `stale_warning` ("previous targets S861-S873 are now live registry rows; apply only
  from S874+") is now insufficient: S874/S875 are live too, and the map was **not** regenerated
  for round 72 (no renumber artifact under `.ufo/waves/round-72/`; `git status` on the round-71
  map is clean).
- the landed `corpus/lessons/round-72.md` does record the collision ("The staged set's own
  S874/S875 (onomastics rows, register S791 unverifiable / S792 refused) are NOT adopted; the
  collision receipt records them as not-adopted"), and the collision artifacts exist:
  `.ufo/waves/round-72/assimilation/collcheck-{reg-ids,staged-ids}.txt` + a 0-byte
  `collcheck-collisions.txt`. But note the artifacts' `collcheck-staged-ids.txt` **includes
  S874/S875** (24 ids) while `comm -12` against the 797-id `collcheck-reg-ids.txt` still yields
  **S859 S861 S862 S869 S870** as the true id overlap — the empty collisions file is therefore
  consistent with the *adopted* subset only, not with the staged-ids list as written. Any future
  round that lands the rest of the staged set must regenerate the map from S876 upward.

## 4. Header/format conformance of the staged pair (context for the adopter)

Both staged entries carry the full header set claimed by leg ENTRIES
(`source`/`verified-at`/`recheck`/`ground`/`topic`/`gap filled`/`sources`/`couples`/`scope`).
Two defects in the staged text, both fixed in the landed pair:

- the canonical's `recheck:` line references `SOURCES-PROPOSED.md`, a file that exists only in the
  shokuknow lane (`/home/vgpnk/Projects/shokuknow/lanes/kotodama/SOURCES-PROPOSED.md`) and
  **not** in the kotodama lane — a dangling path in a landed entry. The landed version names the
  two normalized row commands instead.
- the canonical's `gap filled` says "over the 643-row registry" (a round-1-era count) and its
  `couples` name `myth-symbol/calendar-festival-systems.md`, a path that does not exist in the
  lane (the file is `culture-material/calendar-festival-systems.md`). The amendment's `couples`
  name `culture-material/calendar-festival-systems.amend-2026-10-24-r10.md`, also absent from the
  lane. All corrected in the landed text.
- staged row recheck cells use an **escaped pipe** (`\|`) inside the `curl … \| grep -c` command
  (S863/S867/S967 all carry one). The kotodama lane registry has **zero** rows with an escaped
  pipe (all 797 rows split into exactly 11 unescaped cells). A row copied verbatim with `\|`
  breaks the census: verified in a /tmp probe (`/tmp/r72-probe`, `sources-census.sh validate`)
  an escaped pipe yields `E01 S900 fields=12` **and** a spurious `E11 missing used-by grep -c 'x'`
  — because the awk field split shifts the used-by cell. The landed S874/S875 rows use a plain
  `180d`/`90d` cadence cell and split cleanly into 11 cells, so this trap is not present in the
  landed rows.

## 5. State of the lane during the scan (base vs concurrent landing)

- At the frozen base `b60c7b1`: `git ls-tree -r --name-only b60c7b1 | grep -i heritage-taxonomy`
  → **empty**. No lane file at `corpus/knowledge/culture-material/heritage-taxonomy-models*.md`
  existed; claim C's "before" statement holds.
- Mid-scan, a sibling executor landed them:
  `770100f round-72 C: heritage-taxonomy assimilation — two entries admitted, registry S874/S875
  appended (797->799), lesson round-72` (2026-10-25 11:38), touching `corpus/SOURCES.md` (+2),
  the two entries, and `corpus/lessons/round-72.md`. Later commits (`2b8d674`, `21ad308`,
  `ac0d18e`, `11a41fb`) add receipts and seat reports.
- Landed pair verified: both cite only S874/S875 (no S863/S867/S967/S837 remain);
  `check-cited-lines.py` → `CITED-LINES: 0 finding(s) in 2 file(s)`, exit 0.
  Registry rows S874/S875: 11 unescaped cells each, `status=mined`,
  `used-by` = {canonical, amendment} for S874 and {canonical} for S875 — union = both entries,
  exactly as leg ROWS requires; no registry row removed (797 → 799).

## 6. Residual unknowns

1. The round-71 `id-renumber-map.json` is not regenerated for round 72 and now conflicts with the
   live S874/S875 (§3a). Whether a later round lands the remaining ~130 staged rows is out of
   scope here, but the map should be regenerated from S876 before that happens.
2. The staged `era-periodization-models.amend-2026-10-23.md` and `-amend-2026-10-23b.md` cite
   campaign-round ids (S726/S732/S746/S757) that in the kotodama lane name unrelated documents.
   Not part of this adoption; a hazard for whoever assimilates them next.
3. The staged `SOURCES-PROPOSED.md` gate sections in the shokuknow lane are labelled
   off-by-one against the rows they document (`## Gate — S864` carries S863's URL/quote,
   `## Gate — S868` carries S867's, `## Gate — S866` appears twice). Anyone re-deriving the
   gate quotes from that file by heading id rather than by row will attach the ihchina quote to
   the wrong row. The landed lesson instead re-derived its quotes from the round-72 re-open
   evidence, so it is unaffected.

## Method / evidence trail

Read-only throughout; shokuknow never written. Commands used: `find`, `grep`, `bash` (fact
pipelines only), `read`, `git ls-tree/log/status/show` (read-only). One /tmp probe
(`/tmp/r72-probe`) to test the census against an escaped-pipe registry row — scratch only, no
fleet or lane file created. No installs; no pacman.
