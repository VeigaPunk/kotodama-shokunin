# ScoutCensusAfter — round-50 falsify attack

**Item attacked.** The C coverage contract's *after-landing census*: commit
`1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad2683`) lands 22 new registry rows
S048–S069 (opened 2026-10-21), the pastoralism entry, and the README index row; the fleet
validator and the contract's seven manual census commands are clean on both the lane working
tree and a clone of the landed commit; totals 226/28; sweep green. Secondary: the measurement
instrument that reports those numbers (`reports/round-50/run-validation.py` +
`reports/round-50/validation.json`).

**Verdict.**
- Census after landing, on landed bytes: **HOLDS** — every count, exit code and cross-link
  matches; the 22 rows are exactly the delta, all `mined`, all `used-by` the new entry, and the
  entry cites all 22.
- The landed measurement instrument that is supposed to regenerate the receipt: **BROKEN**
  (reproducibility) — see §6. Landed `run-validation.py` exits 1 where the receipt says
  `acceptance_passed: true`.

Method: lane HEAD read-only (`git -C … rev-parse HEAD` = `1c779e4a…`; `git status --porcelain`
shows only `M reports/round-50/run-validation.py` plus untracked wave/receipt files — `corpus/SOURCES.md`,
`corpus/README.md` and the entry are clean, so lane reads equal landed bytes for every path in
this item). Reproduction ran in a private `git clone -q --shared` under `/tmp` checked out at
`1c779e4a…` with `GIT_CEILING_DIRECTORIES=/tmp`; the clone and all fetched bodies were deleted.
No lane file was edited; no tool installed.

## 1. Fleet validator

From `/home/vgpnk/Projects/shokunin` (lane by conf name):

```
$ bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
EXIT=0
$ bash scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kotodama
kotodama	rows	69
kotodama	tier.A	50
kotodama	tier.B	12
kotodama	tier.C	7
kotodama	status.mined	42
kotodama	status.queued	22
kotodama	status.rejected	5
FLEET	rows	69
FLEET	tier.A	50
FLEET	tier.B	12
FLEET	tier.C	7
FLEET	tier.invalid	0
FLEET	status.queued	22
FLEET	status.mined	42
FLEET	status.rejected	5
FLEET	status.invalid	0
FLEET	missing	0
EXIT=0
```

On the landed clone (explicit lane dir; `--today 2026-10-21`):

```
$ bash scripts/sources-census.sh validate --today 2026-10-21 /tmp/scoutcensus-4Mot
scoutcensus-4Mot	ok	/tmp/scoutcensus-4Mot/corpus/SOURCES.md
EXIT=0
$ bash scripts/sources-census.sh census --today 2026-10-21 /tmp/scoutcensus-4Mot
scoutcensus-4Mot	rows	69   tier.A 50  tier.B 12  tier.C 7
scoutcensus-4Mot	status.mined 42  status.queued 22  status.rejected 5
FLEET rows 69, tier.invalid 0, status.invalid 0, missing 0
EXIT=0
$ bash scripts/sources-census.sh overdue --today 2026-10-21 /tmp/scoutcensus-4Mot
… 69 `cadence` lines, S048–S069 `recheck=365d opened=2026-10-21`; no `overdue` line
EXIT=0
```

## 2. The contract's seven manual census commands

Run from each tree root (`/home/vgpnk/Projects/shokunin/kotodama-shokunin` and the clone);
outputs were byte-identical, so one column is shown. Source of the seven:
`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:64-81`.

| # | command (contract) | output (lane = clone) | exit |
|---|---|---|---|
| 1 | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | `69` | 0 |
| 2 | malformed rows `NF!=13` | `0` | 0 |
| 3 | tier histogram | `A=50 B=12 C=7 ` | 0 |
| 4 | status histogram | `mined=42 queued=22 rejected=5 ` | 0 |
| 5 | duplicate ids (`sort \| uniq -d`) | *(empty)* | 0 |
| 6 | enum violations + tier inflation | *(empty)* | 0 |
| 7 | mined rows whose used-by paths do not exist | *(empty)* | 0 |

## 3. Rows by tier/status, before vs after

| metric | base `4ad2683` | landed `1c779e4` | delta |
|---|---|---|---|
| rows | 47 | 69 | +22 |
| tier A / B / C | 34 / 6 / 7 | 50 / 12 / 7 | +16 / +6 / 0 |
| status queued / mined / rejected | 22 / 20 / 5 | 22 / 42 / 5 | 0 / +22 / 0 |

The 22 added rows occupy `corpus/SOURCES.md:77-98` (S048 at :77, S069 at :98), all
`opened = 2026-10-21`, all `mined`, all `used-by =
corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`. Tier/kind of the additions:
A = S050 S052 S053 S054 S055 S056 S058 S059 S060 S062 S063 S064 S066 S067 S068 S069 (16);
B = S048 S049 S051 S057 S061 S065 (6); no C, no `community`. The `git diff` for SOURCES is
25 insertions / 1 deletion: the deletion is only the preamble pointer line
(`lessons/round-49.md for S001–S043` → `… S001–S047, … S048–S069`), so no pre-existing row's
`status`/`recheck`/`used-by` changed (matches `corpus/lessons/round-50.md` "Status and
used-by change log").

## 4. Cross-links and totals

- Entry cites exactly S048–S069: 22 distinct ids, occurrence counts 2–11; no other S-id.
  The manifest's C acceptance run verbatim on the clone prints `C_SID_UNRESOLVED 0 []`, exit 0.
- `find corpus/knowledge -name '*.md' | wc -l` = **226**; culture-material = **28** (base: 225/27).
- `python3 -B reports/round-28/readme/sweep.py` on the clone:
  `rows 226 files 226`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`,
  `header_drift {}`, `totals_ok True`, `footer_ok True`, exit 0
  (parts `culture-material: 28`, footer `[25,26,28,29,24,94]`).
- README at landed bytes: row at `corpus/README.md:297`, between
  `music-instrument-lexicon.md` (:296) and `ritual-garments.md` (:298) — filename order;
  header `## culture-material/ (28)` at :277; `Total knowledge entries: 226` at :590;
  date line 2026-10-21 at :592. Entry is 199 lines.

## 5. Source re-open (22 rows, opened this session)

Each row URL was fetched read-only (curl, browser UA, 30–60 s), then the Gate quote in
`corpus/lessons/round-50.md:27` was searched in the returned bytes. `verbatim` allows HTML
markup/line-wrapping between words but no rewording.

| row | HTTP route | quote | note |
|---|---|---|---|
| S048 | 200 fao.org/4/y2647e/y2647e02.htm | yes | |
| S049 | 200 fao.org/4/y2647e/y2647e08.htm | yes | |
| S050 | 200 pmc.ncbi.nlm.nih.gov/articles/PMC2575338/ | yes | markup `<em>ca.</em>` inside the quote |
| S051 | 200 link.springer.com/… but bot-challenge body (3 KB, no abstract) | unverifiable at row URL | abstract fetched from Semantic Scholar for DOI 10.1007/s10963-011-9045-7 matches the Gate sentence verbatim |
| S052 | 200 people.duke.edu/…Nuer…pdf (17 MB, OCR layer) | yes | quote split by line; p. 19 idiom, §VIII colour passage both present |
| S053 | 200 but Anubis JS challenge (5 KB) on every openedition route incl. `/pdf/14002` | unverifiable live | Wayback capture of the page carries the French quote verbatim in body and meta |
| S054 | 200 web.mit.edu/…HardinCommons.pdf | yes | line-wrapped; p. 1244 |
| S055 | 200 nobelprize.org/…ostrom_lecture.pdf | yes | §4E, PDF p. 15 |
| S056 | 200 scielo.cl/…chungara-00302.pdf | yes | line-wrapped, p. 85 |
| S057 | 200 routledge.com book page | yes | publisher description only — row says so, tier B (QUALITY 6 correct) |
| S058 | 200 fao.org/4/y5115e/y5115e08.htm | yes | quote is item 2 (`baartol`) split by a newline; row URL is the book contents page `y5115e00` which links this chapter — Gate names the chapter, so coordinate is honest, just not the landing URL |
| S059 | 200 sametinget.se/renmarken | yes | |
| S060 | 200 d-nb.info/1152169939/34 (PDF) | yes | line-wrapped |
| S061 | 200 fao.org/4/AD347E/ad347e0j.htm | yes | |
| S062 | 200 live ich.unesco.org element page | yes | Gate says "live page CAPTCHA"; live page actually serves the description text (3 hits, 0 captcha markers) — stale disclosure, not a source defect; Wayback capture also carries it |
| S063 | 200 live ich.unesco.org element page | yes | |
| S064 | **000 / connection timeout** at etcsl.orinst.ox.ac.uk (40 s) | yes | matches row's and Gate's disclosure; Wayback capture 20260605210113 carries lines 130–142, quote split by newline |
| S065 | 200 ahdictionary.com/word/indoeurop.html | yes | anchor `#IR084700`; tier B is right for a dictionary gloss |
| S066 | 200 d-place.org/parameters/EA004 | yes | |
| S067 | 200 nature.com/articles/s41586-021-04018-9 | yes | |
| S068 | doi.org → academic.oup.com **403** (Cloudflare "Just a moment") | yes via disclosed PMC8214430 | row discloses "(full text PMC8214430)" |
| S069 | 200 ich.unesco.org/en/decisions/14.COM/10.B.2 | yes | |

Tier/scope honesty under QUALITY criterion 6 (`corpus/QUALITY.md:29`): every scope column is
limited to what was read (S052 "1940 assertions … not contemporary", S053 "not Herskovits'
text", S056 "B for the historical episodes it reports", S057 "publisher description …
QUALITY criterion 6", S062/S064 disclose mirror routes), A is reserved for primary/authoritative
sources in scope, and no `community` row is A. No tier inflation found. Spot-checked entry
sentences against the fetched text: S048 conditions, S050 "harvesting of young males and
prolonged survivorship of females" and four species c. 11,000–10,000 BP, S052 colour ×
distribution naming (ten principal colour terms), S058 baartol seasonal move, S059 earmark
definition, S060 five snouts, S061 warm-season high pastures, S062 ger portability, S063 Bedu
pastoral culture, S067 Botai/DOM2, S068 camelids-only, S069 horizontal/vertical transhumance —
all supported.

## 6. FINDING (measurement): landed runner cannot reproduce the receipt

`reports/round-50/validation.json` (untracked; not present in `1c779e4`) declares
`"acceptance_passed": true` and records C before `pastoral_topic_owner_lines = 0`. The landed
runner uses the substring regex at `reports/round-50/run-validation.py:69`:

```
TOPIC_OWNER_RE = re.compile(r"^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)", re.IGNORECASE)
```

At base, `corpus/knowledge/culture-material/writing-media-surface-economy.md:3` contains
"… incidental surfaces — sherd, wall, pot, body …", so the landed regex counts 1 owner and
`EXPECT["C"]["before"]["pastoral_topic_owner_lines"] = 0` (`run-validation.py:92`) fails.
The lane working tree holds an **uncommitted** fix (comment "Word-bounded (R50-M2)" + `\b`); the
landed blob has neither (`git show 1c779e4:reports/round-50/run-validation.py` has no R50-M2
line). The receipt was therefore produced with bytes that are not in the landed commit.

Reproduction, exact receipt argv, run from the already-present clean landed tree
(`/tmp/kr50-landed` is a git checkout at `1c779e4`, status clean, `run-validation.py:69` is the
landed substring regex; `/tmp/kr50-base` is clean at `4ad2683`; neither tree was modified):

```
$ cd /tmp/kr50-landed && GIT_CEILING_DIRECTORIES=/tmp \
  python3 -B reports/round-50/run-validation.py \
    --tree /tmp/kr50-landed --base-tree /tmp/kr50-base
RC=1
receipt passed: True | exact-argv repro passed: False
DIFF C before pastoral_topic_owner_lines receipt={'actual':0,'expected':0,'ok':True}
                                        repro  ={'actual':1,'expected':0,'ok':False}
```

Identical result from a fresh clone at `1c779e4` with a detached `4ad2683` worktree as base
(only that one acceptance cell differs; every other before/after cell, including the whole O
and Ca blocks, reproduces).

Raw after-value also drifts (receipt `pastoral_topic_owner_lines` 1 vs repro 2) but is not
asserted in `EXPECT["C"]["after"]`, so the acceptance diff is exactly the one before-check.
O and Ca reproduce exactly (`probe_false_negatives` 0, `probe_false_positives` 0,
`r49_fixture_rc` 1, `r49_detects_C_to_S` true, `r49_matches_independent_prediction` true,
`r50_manifest_rc` 0, `checker_selftest_rc` 0). The probe itself was also run directly:
landed tools `JJ_COLOCATION_FALSE_NEGATIVES=0/3`, `JJ_COLOCATION_FALSE_POSITIVES=0/4`; base
tools (git worktree) satisfy the receipt's 3/3 expectation.

Smallest fix (author lane): land the two-hunk word-boundary change already sitting in the lane
working tree into `reports/round-50/run-validation.py:69` and regenerate
`reports/round-50/validation.json` from the landed tree (its `--tree`/`--base-tree`
paths still exist and are clean, but the receipt records nothing about which runner bytes
produced it, which is why the mismatch is invisible from the receipt alone). Until then the
receipt's `acceptance_passed: true` is not valid for landed bytes.
Census readers should not treat this as a census error: the census values themselves (tier/status
counts, used-by resolution, totals, sweep) are identical under the fixed and landed regexes.

## Verdict

- Census after landing (S048–S069 rows, entry, README, totals, validator + seven commands on
  lane and landed clone): **HOLDS**.
- Measurement instrument/receipt reproducibility in the same landed work: **BROKEN** (one
  before-check, uncommitted fix; §6). No fix applied by this read-only seat.
