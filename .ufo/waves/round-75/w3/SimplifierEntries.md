# W3 simplifier — claim C's three landed entries: what can be deleted, measured

Seat: `SimplifierEntries` (leaf — no dispatch, no background jobs).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (read-only; the only lane write is this report).
Base `f556d1049fe651d3d63975600b13acd9fb686f15` · freeze `5d0167464309d8133991b30f7d7a7011a6a0fd14` ·
claim Ca landed `012e8d3c8b92f47c734f735d58d118d574fe6a14` · claim C landed `4f5e3b2535c2c06c51627dc2736c40183847cae1`
(the lane `main` carries only later telemetry/report-side commits; `git -C <lane> diff --stat 4f5e3b2 -- corpus/knowledge/myth-symbol corpus/SOURCES.md corpus/README.md` is empty, so every line number below is the landed byte offset).
Scratch: `/fast/scratch/hyaku/kotodama-r75/SimplifierEntries` — clone of the lane, five fixture branches on top of `4f5e3b2` (A, Bv1, B2, C, D), deleted at yield. The receipts below are transcribed from the runs: the summary line and the INDEX detail line are verbatim, and runs whose every leg passed are collapsed as noted; §9 gives the exact recipe to rebuild any of them.

## 0 Result in one line

The three entries are **not load-bearing prose**. Every sentence a registry row, a Gate record or a counter leg needs survives every cut I ran:

* **877 words (6.9 %) of pure duplication are deletable** with `ACCEPT-C-75: PASS legs=13/13` (set B2, §4). This is the set I recommend.
* The mechanical ceiling is **9,010 of 12,744 words (70.7 %) deletable**, all 13 legs still green (tier D, §6).

Verdict: the **entries HOLD** on the cut axis (no claim a row/Gate/leg needs is lost by any cut I proposed, and no section restates another entry's section). The landing's **record about** the entries is **PARTIAL**: D1 and D2 (§8) are false statements in the landed lesson about these exact files, and no leg reads either.

## 1 The landing, measured

| entry | bytes | words | pre-section block words (H1 + the nine fields, lines 1–16 / 1–14 / 1–14) | body words as the counter counts them | `## ` sections |
|---|---|---|---|---|---|
| `myth-symbol/narrative-structure-frameworks.md` | 30,920 | 5,014 | 767 | 4,139 | 12 |
| `…narrative-structure-frameworks.amend-2026-10-23.md` | 24,166 | 3,951 | 550 | 3,329 | 8 |
| `…narrative-structure-frameworks.amend-2026-10-23b.md` | 23,049 | 3,779 | 644 | 3,048 | 7 |
| **total** | **78,135** | **12,744** | **1,961** | **10,516** | **27** |

The floor is `_ENTRIES_WORD_FLOOR = 478` (`reports/round-75/accept-c.py:1140`), derived as the smallest **whole-file** word count of any `corpus/knowledge/**/*.md` at base — `corpus/knowledge/culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md`, 478 words (re-derived by this seat, `git show <base>:<path> | wc -w`). The leg applies it to **body** words (everything after the first `## `, heading lines removed, `accept-c.py:1158-1162`). See D3.

Baseline, run by this seat in a clone checked out at the landing (not quoted from the landing's own receipt):

```
$ python3 -B reports/round-75/accept-c.py --root . --lands 4f5e3b2535c2 --freeze 5d0167464309 --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS ENTRIES … LEG PASS INDEX
ACCEPT-C-75: PASS legs=13/13
```

This reproduces the summary line of `reports/round-75/telemetry/measures-c.txt`. One operational note: the CENSUS leg runs `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`, so a run **without** `--fleet-root` prints `LEG FAIL CENSUS … census script not found` and `legs=12/13`. That is a missing argument, not a landing defect; every run quoted below passes `--fleet-root`.

## 2 The preserved contract — what no cut may touch

| binding artifact | what reads it | consequence for cut design |
|---|---|---|
| nine header fields (`source, verified-at, recheck, ground, topic, gap-filled, sources, couples, scope`) before the first `## `; no placeholder, no `<…>` | `leg_entries` (`accept-c.py:1176-1243`), `HEADER_FIELDS` at `:198` | the whole header block (1,961 words) is untouchable as a block; only prose *inside* values could shrink, and that prose carries provenance claims (see §7) |
| each `- source:` line: **exactly one** S-id **and** a URL whose document key equals the row's | `leg_repointed` (`:1730-1810`), `_repointed_source_lines` (`:1494`), `_repointed_problem` (`:1710`) | no `source:` line was cut. Cutting one would also force a registry `used-by` edit (`leg_rows` derives it from these lines), which is a rewrite, not a deletion |
| `- topic:` value | `leg_index`: the README row is "each entry's own `- topic:` text verbatim" | untouched; each of the three `- topic:` values is byte-identical to the text after `— ` in `corpus/README.md:406-408` |
| ≥ 1 `## ` and ≥ 478 **body** words per entry | `leg_entries` | the only numeric floor; binds §6 only |
| no line with ≥ 2 distinct S-ids; no `|`-leading line with any S-id | `leg_citedlines` → `tools/check-cited-lines.py` | cuts may only **remove** ids, never merge two cited lines |
| inline S-ids ⊆ {S885…S893}; no base-row id, no campaign-namespace id except map identity | `_repointed_problem` (`:1710-1727`) | cuts may not introduce an id; removing inline ids is free |
| `S893` must appear in the entries' cited set | `leg_repointed` (`:1809-1810`) | satisfied by the base entry's `source:` line, not by any body sentence |
| QUALITY-10 "challenge met and **not passed**", verbatim: `amend-2026-10-23.md:126`, `…-23b.md:116` and `:118` | **no leg** — carried by claim C's `kill_rule` ("any other source is accessed by passing an access control (QUALITY 10) → the claim fails") | hand-carried; §7 keeps them in every tier |
| the one-window statements (`amend-2026-10-23.md:136`, `…-23b.md:114`) | **no leg** — they scope which page each row's committed evidence window covers | hand-carried; kept in every tier |
| the entry **bytes**: `assimilation/validate-receipt.txt` lines 8–10 carry one `entry sha256` per entry | `leg_scratch_mirror` checks ids/basenames/exit 0 only, **not** the digests | the digests equal the landed files today (measured); any cut desynchronises the receipt (§7) |

Nothing else in the entries is read by anything: the Gate table (`corpus/lessons/round-75.md:17-125`) quotes **documents**, never entry sentences, and the evidence windows hold document text.

## 3 Is any entry restating another entry's section?

**No.** Measured on section bodies (header block excluded), 6-word shingle containment:

| pair | shared 6-grams | as % of the smaller file's body |
|---|---|---|
| base ↔ `amend-2026-10-23` | 1 | 0.03 % |
| base ↔ `amend-2026-10-23b` | 0 | 0.00 % |
| `amend-2026-10-23` ↔ `amend-2026-10-23b` | 20 | 0.64 % |

The only section-level overlap in the corpus is `## 7. Provenance limits` (amend-23:124-140) with `## 7. Provenance limits, the one-window rule, …` (23b:110-122): **19 of the 20** shared 6-grams, i.e. the two files state the same provenance rule for their own rows. The amendments also defer explicitly rather than repeat (amend-23:37 "the levels … are carried by `…amend-2026-10-23b.md`"; 23b header `couples:` "whose two-reading section this file does not repeat").

What does duplicate is at **claim level, as paraphrase** (no 6-gram hit, so no text search will ever catch it). Seven pairs:

| # | duplicated claim | side A | side B | disposition |
|---|---|---|---|---|
| 1 | credits at p. 5: Benveniste for the levels, Lévi-Strauss for the mythème, Todorov for two levels | amend-23:107 (30 w) | 23b:25 (116 w, window-backed p. 5) | **cut** (§4 row 7) — B is the stronger record |
| 2 | Barthes p. 5 OCR damage (`V analyse`, `Vhistoire`) | amend-23:128 (29 w) | 23b:27 (86 w) | not cut in A/B2: A's own "no claim rests on a damaged character" sentence (amend-23:134) is the claim this paragraph demonstrates; cut only if a pointer replaces it, which is a rewrite |
| 3 | "this file decides no culture's story / canon belongs to lore-shokunin" | `scope:` + closing para (amend-23:13, :140; 23b:13, :122; base:15, :190) | — | **cut the closing paragraph in each file**; the `scope:` field is the same claim with more detail |
| 4 | the three levels (fonctions/actions/narration) and the four classes (noyaux/catalyses/indices/informants) | base §2:27, 29, 31 (446 w) | 23b §1:17-21 + §3:53 (787 w) | **keep both** — base needs the enumeration for §9's steps 2-3, 23b needs it as the object of its correction; a bare cut orphans base's two §2 tables. A future pass can collapse base:27+29 into one deferring sentence (246 w) |
| 5 | "the five codes are not in the 1966 article" | base:45 (89 w, with its own no-occurrence check) | 23b §2:39 (35 w) | keep both: base states a check over its four served texts, 23b states what its own row does not carry |
| 6 | universality quote «Innombrables sont les récits du monde.» | base:25 | amend-23:19 | keep: the quote is the premise in base and the opening move in the amendment |
| 7 | calibration of the same page (hierarchy "mainstream as method, contested as a claim") | base §10:162-175 | 23b §6:102 | keep: each file calibrates its own rows |

Boilerplate repeated verbatim across files is only the two clauses in pair 3 plus the shared S885 document URL — that is per-file provenance, not restatement.

## 4 The cuts I recommend (set B2): 877 words, 6.9 %

All ranges are inclusive line numbers on the landed bytes; every range is **below** the header block (the block ends at base:16, amend-23:14, 23b:14), so no header field, `topic:` value or `source:` line is touched. Delete the range; the file keeps all its other sections.

| # | file | lines | words | what is deleted | the claim survives at |
|---|---|---|---|---|---|
| 1 | base | 158 | 45 | step→status map ("Steps 1 to 6 rest on the taught method …") | §10 rows + §3/§4/§6/§7 inline statuses |
| 2 | base | 190 | 38 | "Nothing here decides a culture's story …" | `scope:` field (base:15) — same claim, more detail |
| 3 | base | 194 | 24 | §12 bullet: five codes not attributed to the 1966 article | base:45 (with the no-occurrence check) |
| 4 | base | 196 | 17 | §12 bullet: Chatman's six participants not enumerated | base:86 ("… names the six participants without enumerating them") |
| 5 | base | 197 | 45 | §12 bullet: three-layer format / generation programme not findings | base:117 (§6) + base:121, :125 (§7) + §10 rows |
| 6 | base | 198 | 20 | §12 bullet: 世界观 not a warrant, tier C | base:137 ("The status is **tier-C vocabulary** … borrows no warrant from it") |
| 7 | amend-23 | 107 | 30 | credits paragraph (Benveniste / Lévi-Strauss / Todorov at p. 5) | 23b:25, on the page the window holds |
| 8 | amend-23 | 140 | 40 | closing "This amendment appends to …; canon … belongs to lore-shokunin" | `scope:` (amend-23:13) + `couples:` (amend-23:11 names the base) |
| 9 | amend-23 | 144-152 | 213 | §8 "Checklist, runnable without the three articles" — every item restates §2's three orders or §3's axis table (item 4 = §3 table row 1; item 5 = amend-23:56; items 6-8 = §4's plane table; item 9 = `scope:`) | the sections it indexes |
| 10 | 23b | 73-78 | 213 | §5 "Checklist, in order" — items restate §1 (level map/integration), §3 (count, deletion test), §2 (codes as registers) | those sections; the two decision tables at 82-96 stay |
| 11 | 23b | 98 | 159 | §5 "Worked example, no canon decided" (river-port town) — illustration only; contains no claim not stated in §1-§3 | §1-§3 |
| 12 | 23b | 122 | 33 | closing "This amendment appends to …; canon …" | `scope:` (23b:13) + `couples:` |
| | **total** | | **877** | | |

After B2: base 4,825 w / body 3,950; amend-23 3,668 w / body 3,046; 23b 3,374 w / body 2,643 — all far above 478. Sections: 12 / 8 / 7 unchanged.

Set **A** (only the pure restatements, 247 w) = rows 2-8 **and row 12** above; it leaves every checklist and example in place. Rows 1, 9, 10, 11 are the ones that cost a *form* (a consolidated index, a runnable checklist, a worked example) while losing no claim; that is why B2 and not A is my recommendation, and why an owner who values the checklists can stop at A.

**Not cut, deliberately:** the calibration tables at `base:162-175` (§10, 304 w) and `amend-23:113-120` (§6, 194 w). An earlier draft of set B deleted both and the counter still passed, but three rows are the *only* place a status is assigned — "the cultural-skew argument | contested" (base §10), "narrative is a human universal | mainstream as an observation, contested as a law" (amend-23 §6), "noyaux against expansions | mainstream as a distinction, contested as a closed taxonomy" (base §10) — and a status is a claim about a source. Deleting those tables is a claim loss, not a simplification. Measured as tier **Bv1** below (1,415 w cut, 13/13 green) so a later round knows the number, not as a recommendation.

## 5 Measured runs

Every run is a fixture commit **on top of the landing** in my clone (branch per tier, `-c user.name=fixture -c user.email=f@f.invalid`), graded by the frozen counter against the frozen config; only the three entry paths differ from the landing in each commit.

| tier | words removed | entry totals (base / 23 / 23b) | bodies | `check-cited-lines.py` | counter |
|---|---|---|---|---|---|
| landing | 0 | 5,014 / 3,951 / 3,779 | 4,139 / 3,329 / 3,048 | `0 finding(s) in 3 file(s)` | `PASS legs=13/13` |
| **A** (247 w) | 247 | 4,870 / 3,881 / 3,746 | 3,995 / 3,259 / 3,015 | 0 | `PASS legs=13/13` |
| **Bv1** (tables incl., 1,415 w) | 1,415 | 4,521 / 3,434 / 3,374 | 3,646 / 2,812 / 2,643 | 0 | `PASS legs=13/13` |
| **B2** (recommended, 877 w) | 877 | 4,825 / 3,668 / 3,374 | 3,950 / 3,046 / 2,643 | 0 | `PASS legs=13/13` |
| **C** (whole sections, 7,915 w) | 7,915 | 1,643 / 1,577 / 1,609 | 867 / 1,012 / 938 | 0 | `PASS legs=13/13` |
| **D** (floor probe, 9,010 w) | 9,010 | 1,339 / 1,174 / 1,221 | 563 / 609 / 550 | 0 | `PASS legs=13/13` |

Receipts, transcribed (one per tier; the INDEX detail line is quoted in full because it is the only line that varies, and the runs collapsed to a summary are the ones whose every leg printed PASS):

```
######## tier A  (db093b2abe962b2ee97e2ececca9d6e93c490d94)
LEG PASS ENTRIES / ROWS / REPOINTED / GATE / EVIDENCE / REJECTS / GROUND / CITEDLINES
     files=3 last-line=CITED-LINES: 0 finding(s) in 3 file(s)
LEG PASS CENSUS   exit=0 last-line=file ok <clone>/corpus/SOURCES.md
LEG PASS SCRATCHMIRROR   receipt@0 append@2 rows=9 entries=3
LEG PASS COLLCHECK   ids=808 staged=132 collisions=26 guard=ok/ok map=12
LEG PASS FROZENCFG   freeze 5d0167464309 … map=(sha256-match) ledger=frozen-bytes counter=self-pinned
LEG PASS INDEX
     corpus/README.md: 6 section(s), myth-symbol=32, last footer total=252 vector=32/32/40/29/24/95, 3 adopted row(s), 822 base / 831 lands line(s), 12 exempt line(s)
ACCEPT-C-75: PASS legs=13/13

######## tier Bv1 (dc4df30747e2a81eafeb73f08e8dc439dd13f399)
ACCEPT-C-75: PASS legs=13/13        (every leg PASS, INDEX line identical to the above)

######## tier B2  (3623c3798f28203d719ccfc2ace78a775f84d3a5)
LEG PASS ENTRIES … LEG PASS INDEX
     corpus/README.md: 6 section(s), myth-symbol=32, last footer total=252 vector=32/32/40/29/24/95, 3 adopted row(s), 822 base / 831 lands line(s), 12 exempt line(s)
ACCEPT-C-75: PASS legs=13/13

######## tier C  (80d3483ff6a0936a5497738a21f23a8a752eeb79)
ACCEPT-C-75: PASS legs=13/13        (every leg PASS, INDEX line identical)

######## tier D  (93e6d566b21dbcbe47e9bdfc9eb4a48d5dd2691b)
LEG PASS ENTRIES / ROWS / REPOINTED / GATE / EVIDENCE / REJECTS / GROUND / CITEDLINES / CENSUS / SCRATCHMIRROR / COLLCHECK / FROZENCFG / INDEX
ACCEPT-C-75: PASS legs=13/13
```

Reproduce one line of it: the counter's ENTRIES detail prints a note only when the derived floor differs from 478, and no run printed one — the floor is the frozen number, unchanged by cuts.

## 6 The ceiling: 70.7 % is deletable, all legs green

Tier D keeps, per entry, the header block plus the smallest set of paragraphs that (a) stays above 478 body words, (b) keeps at least one `## ` section, and (c) keeps the hand-carried QUALITY-10 / one-window sentences:

* base: §2 lines 25, 27, 29, 31 → **563** body words. Deleted: §1 and §3-§12 (the entire Chinese and Japanese half, the actant table, the time dimensions, the three-layer format, the generation side, 世界观, the ten-step sequence, the calibration table, the handoff, and §12).
* amend-23: §3 lines 58, 60 + §7 (124-140, the closing paragraph at 140 included) → **609** body words. Deleted: §1, §2, §4, §5, §6, §8 (Barthes, Greimas, the side-by-side table, calibration, checklist).
* 23b: §3 lines 43, 51 + §7 (110-122, the closing paragraph at 122 included) → **550** body words. Deleted: §1, §2, §4, §5, §6 (the levels, the five codes, the attribution table, the design orders, calibration).

`ACCEPT-C-75: PASS legs=13/13`. That is the honest size of the enforcement gap: the ENTRIES leg is declared *"a length-and-shape gate only"* (`claims.json`, claim C, legs[0]) and behaves exactly so — it cannot tell 12,744 words from 3,734. No leg reads a single entry sentence. Not a defect in the leg (the claim declares the limitation); it is the reason the entries' *content* is defended only by review, and the reason D1/D2 below can sit in the landed lesson with every leg green.

## 7 Costs and tradeoffs of actually cutting

1. **The receipt binds the landed bytes.** `assimilation/validate-receipt.txt:8-10` carries one `entry sha256` per entry, and all three equal the landed files (measured: `25992609…` / `63a4d5bf…` / `3ea4d6f8…`, matching `sha256sum` of the tree). `leg_scratch_mirror` does **not** recompute them, so any cut passes the leg while leaving the receipt describing bytes that no longer exist. A cut must either refresh the receipt in the same commit or state in the cut's commit message that the receipt is the record of the pre-cut validation run (historical, not current). Three artifacts also carry the digests (`w2/ScribeEntryBaseFinal.md`, `w2/ScribeEntryAmend23Final.md`, `w2/w2-results.json`); those are historical and must not be rewritten.
2. **The lesson's byte counts do not bind.** `corpus/lessons/round-75.md:92-94` prints 6862 / 5933 / 2514 B — the **staged** sizes (`/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/myth-symbol/*.md`, measured), not the landed 30,920 / 24,166 / 23,049 B. A cutter therefore does not falsify the lesson by shrinking the landed files. See D4.
3. **The header block is 1,961 words (15.4 %) and mostly unread.** Only the nine field *names*, the `topic:` value, and the `source:` id+URLs are read; the rest of each `verified-at` / `recheck` / `ground` / `sources` / `couples` / `scope` value and the bibliographic tail of each `source:` line is not. Trimming it is possible but it is **not a deletion of duplicated content** — those sentences are the per-file provenance record (HTTP status, byte counts, UA, page scope, "no login or no challenge"), and `…-23b`'s source lines must keep their archive-carrier URLs for QUALITY 22 to remain true. I did not cut any header line and do not recommend it without a separate provenance decision.
4. **Coverage value is not free.** B2 removes only duplication, so the coverage axis loses nothing. C and D remove substance (C removes the base entry's whole CJK half); they are measurements of the floor, not proposals.

## 8 Defects found while measuring (outside my cut scope; none is caught by any leg)

**D1 — the landing lesson points refused material at the wrong file.** `corpus/lessons/round-75.md:107` says 23c's four classes "in `…amend-2026-10-23.md` §N+2" and 24's Marrone/S892 statement "in §N+3". Measured on the landed bytes: `…amend-2026-10-23.md` has **0** occurrences of `noyaux|indices|informants` and **0** of `S892|Marrone`; the four classes are in the base entry §2:31 (and §9:148-149) and in `…-23b.md`:51-53, restated as its attribution-table row at `:62`, and the Marrone statement is in `…-23b.md` §§2-3 (7 × `S892`). The frozen claim's own reject note says the material is "folded into the admitted amend-2026-10-23b entry" — so the lesson contradicts `claims.json`. `§N+2` / `§N+3` are literal placeholder tokens, not section numbers. The refusal's substance stands (the material is carried by the three admitted entries); the pointer does not.

**D2 — the landing lesson records an unrepaired defect that the entries do not have, at a path:line that does not hold the line.** `corpus/lessons/round-75.md:250-255`: "In `…amend-2026-10-23.md:11` the S892 `source:` line's URL is hard-wrapped mid-percent-escape … the mirror's own REPOINTED cross-check prints `match: False` for S892". Measured: amend-23:11 is `- couples:`; amend-23's only `source:` lines are 3-5 (S885, S886, S887); the S892 line is `…-23b.md:5` and carries its complete URL on one line; **no** line in any of the three entries ends in a percent-escape (`grep -n 'age%$\|%$'` → 0); `leg_repointed` PASSES at the landing, i.e. the counter's own by-document join matches S892; and the committed receipt contains no `match:` line at all (it is a census `validate --file` run). The paragraph is stale — it should read "found and repaired", or be removed. It is a present-tense false claim in a landing artifact, and the ENTRIES/REPOINTED legs cannot see it.

**D3 — the 478 floor's stated derivation is a different measure.** `claims.json` calls 478 "the smallest `corpus/knowledge` entry at base", and the counter derives it from whole-file words (`_min_entry_words`, `accept-c.py:980-1000`) but applies it to body words with the header and all heading lines removed (`_entries_body_words`, `:1158`). The two measures differ by each file's header and heading mass (base entry: 875 words between them). Nothing in the landing is near the floor (smallest body after my cuts is 550), so nothing fails; the wording is imprecise, not the leg.

**D4 — the lesson's adopted-entry sizes are the staged sizes.** `corpus/lessons/round-75.md:92-94` lists the three adopted paths with 6862 / 5933 / 2514 B. Those are exactly the staged files' sizes in the read-only source tree; the landed files are 30,920 / 24,166 / 23,049 B (4.5×). A reader checking the lesson's figures against the corpus finds a mismatch that no leg reports.

None of D1-D4 requires a byte change to the three entries.

## 9 Reproduction (scratch was deleted; these are the exact steps)

```
seat=/fast/scratch/hyaku/kotodama-r75/SimplifierEntries
mkdir -p "$seat"; D=$(mktemp -d -p "$seat")
git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"
git -C "$D/lane" rev-parse --show-toplevel        # must print "$D/lane"
git -C "$D/lane" checkout -q -B main 4f5e3b2535c2c06c51627dc2736c40183847cae1
# apply the §4 ranges to corpus/knowledge/myth-symbol/<entry>, then:
git -C "$D/lane" add corpus/knowledge/myth-symbol
git -C "$D/lane" -c user.name=fixture -c user.email=f@f.invalid commit -qm "fixture: B2 cuts"
R=$(git -C "$D/lane" rev-parse HEAD)
python3 -B "$D/lane/reports/round-75/accept-c.py" --root "$D/lane" --lands "$R" \
  --freeze 5d0167464309d8133991b30f7d7a7011a6a0fd14 --fleet-root /home/vgpnk/Projects/shokunin
python3 -B "$D/lane/tools/check-cited-lines.py" "$D/lane/corpus/knowledge/myth-symbol"/narrative-structure-frameworks*.md
```

My clone held five fixture branches plus the analysis copies; the whole seat directory was removed before this report was published, so no cited path is a `/tmp` path and nothing in the lane was mutated (working tree unchanged apart from this file).

## 10 Verdict

**Entries: HOLDS.** No cut I could construct — 247 w, 877 w, 1,415 w, 7,915 w, or 9,010 w — removes a claim that a registry row, a Gate record or a counter leg needs; every cut I would make has a surviving pointer for the claim it removes, and no entry restates another entry's section (0.00-0.64 % 6-gram containment). The duplication that does exist is claim-level paraphrase, and 877 words of it (6.9 %) are safely removable with all 13 legs green.

**Landing record: PARTIAL.** D1 (lesson:107 points the refused 23c/24 material at the wrong file and contradicts the frozen claim) and D2 (lesson:250-255 records an unrepaired hard-wrapped S892 URL that does not exist in any landed entry) are false statements about these entries' bytes, and no leg reads them. D3 (floor derivation is whole-file, application is body-only) and D4 (adopted-entry sizes are the staged sizes) are measured wording imprecisions.
