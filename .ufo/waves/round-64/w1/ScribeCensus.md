# ScribeCensus — round-64 wave-1 census item (frontier step)

## Behavior and deliverables

Ran the fleet census over the kotodama lane and captured the full stdout and exit
code into the lane at `reports/round-64/telemetry/census-wave1.txt`. The file's body
is byte-identical to the captured stdout (verified with `diff`); two leading `#`
comment lines carry the command and the exit code so the receipt is self-describing.

Computed and pasted the six manual census counts from `CORPUS.md` §"Census" over
`corpus/SOURCES.md` (rows, malformed, tier histogram, status histogram, duplicate
ids, enum violations) — verbatim, unedited command forms from `CORPUS.md`.

Ran a non-destructive pre-flight against the **staged** wave-1 rows in
`.ufo/waves/round-64/rows/` (a scratch copy only; `corpus/SOURCES.md` was not
edited) to forecast what the post-integration registry will do to the census, and
cross-checked the round-63/64 calibration numbers that `accept-ca.py` pins.

`corpus/SOURCES.md` was **not modified**: `git diff --quiet ff30a205c8d23b35f1ac533740121a955a9fda96 -- corpus/SOURCES.md` → exit 0 (unchanged against the round base).

## Gates and exact outcome

### Gate 1 — the required census (verbatim)

Command, run from the fleet root `/home/vgpnk/Projects/shokunin`:

```
scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
```

Exit code: **0**. Stderr: empty. Full stdout (30 lines) is in the lane receipt
`reports/round-64/telemetry/census-wave1.txt`:

```
kotodama	W04	S127 duplicate url voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement across scopes
kotodama	W04	S128 duplicate url pure.uvt.nl/ws/portalfiles/portal/100130712/Zeshan_deVos_Eds._2012.pdf across scopes
kotodama	W04	S129 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC10622114 across scopes
kotodama	W04	S130 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC6818964 across scopes
kotodama	W04	S131 duplicate url link.springer.com/article/10.1186/1477-7517-9-16 across scopes
kotodama	W04	S132 duplicate url ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls across scopes
kotodama	W04	S133 duplicate url www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition across scopes
kotodama	W04	S185 duplicate url www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2003/papers/p15_2131.pdf across scopes
kotodama	W04	S186 duplicate url ich.unesco.org/en/RL/whistled-language-of-the-island-of-la-gomera-canary-islands-the-silbo-gomero-00172 across scopes
kotodama	W04	S358 duplicate url ich.unesco.org/en/RL/mask-dance-of-the-drums-from-drametse-00161 across scopes
kotodama	W04	S482 duplicate url periodicos.ufpb.br/index.php/srh/article/view/13999/7921 across scopes
kotodama	W04	S483 duplicate url web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693 across scopes
kotodama	W04	S485 duplicate url revistas.usp.br/sankofa/article/view/187402 across scopes
kotodama	W04	S490 duplicate url glottolog.org/resource/languoid/id/kiko1235.json across scopes
kotodama	W04	S561 duplicate url archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt across scopes
kotodama	W04	S564 duplicate url en.maiask.ru/data/documents/13_YatsenkoRogozhinskiiENG.htm across scopes
kotodama	W04	S565 duplicate url ag.colorado.gov/brands/about-brands across scopes
kotodama	W04	S566 duplicate url collections.vam.ac.uk/item/O1053476 across scopes
kotodama	W04	S569 duplicate url www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec1.htm across scopes
kotodama	W04	S570 duplicate url www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf across scopes
kotodama	W04	S571 duplicate url www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf across scopes
kotodama	W04	S572 duplicate url www.icphs2007.de/conference/Papers/1286/1286.pdf across scopes
kotodama	W04	S573 duplicate url archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0016_B509_0 across scopes
kotodama	W04	S648 duplicate url www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf across scopes
kotodama	W04	S649 duplicate url www.metmuseum.org/art/collection/search/464456 across scopes
kotodama	W04	S650 duplicate url footwearresearchnetwork.org/articles/concealed-shoes-revealed across scopes
kotodama	W04	S651 duplicate url collections.vam.ac.uk/item/O87367 across scopes
kotodama	W03	S687 mined but unused
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
```

Warning counts read off that stdout, verbatim: **W04 = 27** rows
(S127, S128, S129, S130, S131, S132, S133, S185, S186, S358, S482, S483, S485, S490,
S561, S564, S565, S566, S569, S570, S571, S572, S573, S648, S649, S650, S651),
**W03 = 1** row (S687 `mined but unused`), **W01 = 0**, **W02 = 0**,
**E-codes = 0**. The lane's own line is `kotodama ok <path>` and the run exits 0
because W-codes do not fail a clean lane.

### Gate 2 — the six manual census counts (CORPUS.md §"Census", verbatim)

Run from the lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Commands
and outputs, unedited:

```
# rows
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
643

# malformed rows (11 columns means NF=13)
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
0

# tier histogram
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
A=406 B=228 C=9

# status histogram
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
mined=567 queued=57 rejected=19

# duplicate ids — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d
(nothing printed)

# enum violations and tier inflation — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,"",i); gsub(/[[:space:]]/,"",k); gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); if (t !~ /^[ABC]$/) print "tier", i, t; if (s !~ /^(queued|mined|rejected)$/) print "status", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print "kind", i, k; if (t=="A" && k=="community") print "tier-inflation", i}' corpus/SOURCES.md
(nothing printed)
```

Summary of the six:

| count | value |
|---|---|
| rows | **643** |
| malformed rows | **0** |
| tier histogram | **A=406 B=228 C=9** |
| status histogram | **mined=567 queued=57 rejected=19** |
| duplicate ids | **none** (empty output) |
| enum violations / tier inflation | **none** (empty output) |

The manual six and the maintained parser agree exactly: the parser's `census` mode
over the same file prints `kotodama rows 643`, `tier.A 406`, `tier.B 228`,
`tier.C 9`, `status.mined 567`, `status.queued 57`, `status.rejected 19`,
`status.invalid 0`, `tier.invalid 0` — 643 + 0 + 0 = 643, no gaps.

### Gate 3 — fleet context (informational, not required)

`scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin` → exit 0,
`FLEET rows 2571`, `FLEET tier.A 2176`, `tier.B 290`, `tier.C 105`, `tier.invalid 0`,
`status.queued 290`, `status.mined 2106`, `status.rejected 175`, `status.invalid 0`,
`missing 0`. The fleet-wide `validate` over every lane exits **0** with **zero
E-codes** fleet-wide.

## Touched surfaces

Written (lane, one file):

- `reports/round-64/telemetry/census-wave1.txt` — the required census receipt
  (31 lines: 2 `#` header lines + the 30 verbatim stdout lines).

Written (scratch only, outside the lane):

- `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeCensus/preflight.txt` — per-row
  shape/enum/URL pre-flight over the 30 staged rows.
- `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeCensus/scratch-validate.txt` —
  census output for a scratch copy of the registry with the staged rows appended
  and S687 flipped.
- `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeCensus/scratch-lane/` — the
  scratch registry copy.

Written (this report):

- `.ufo/waves/round-64/w1/ScribeCensus.md`.

Not touched: `corpus/SOURCES.md` (verified byte-identical to base `ff30a20`),
`corpus/knowledge/**`, `corpus/README.md`, `LOG.md`, `SCORECARD.md`,
`corpus/LOG.md`, any `accept-*.py` counter, the jj/git index, the fleet repo.
No commit, no push.

## Findings

### F1 — coverage axis: the "unowned" premise holds, with one wording caveat

Claim C's premise ("0 filename owners, 0 topic-line owners at the base") was
checked against the live corpus:

- filename owners: `ls corpus/knowledge/linguistics/ | grep -iE 'socializ|acquisit'`
  → no match. `corpus/knowledge/linguistics/` holds 29 entries; none is a
  socialization/acquisition entry.
- topic-line owners: `grep -rhE '^- topic:.*socializ' corpus/knowledge/*/*.md | wc -l`
  → **0**. No `- topic:` line in the corpus mentions socialization.
- Caveat, reported rather than smoothed: three `- topic:` lines do contain the
  word *acquisition* — the co-speech/gesture entry, the language-contact life-cycle
  entry ("adult acquisition"), and the sacred-register entry ("learned without
  native acquisition"). None of the three owns language socialization and
  acquisition as a topic; all three use the word in a narrower sense. The claim's
  "0 topic-line owners" is therefore true of the *topic*, but is not literally true
  of the *word*. Flagged for the judge; no correction is needed to any counter.
- The registry has no owner either: `grep -ciE 'socializ' corpus/SOURCES.md` → 0.
- Base corpus size confirmed: `find corpus/knowledge -type f -name '*.md' | wc -l`
  → **237**; linguistics → **29**. `python3 -B reports/round-28/readme/sweep.py`
  exits 0 with `rows 237 files 237`, `topic_mismatch 0`, `orphan_rows 0`,
  `missing_from_index 0`, `totals_line 237 totals_ok True`. So claim C's
  "237 → 238 entries, linguistics 29 → 30" starts from the stated base.

### F2 — coverage axis (blocking for the APPEND leg): two of the 32 new rows are still missing

`python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows`
prints `CHECK-ROWS: 30/32 clean` and exits 1, with **S723 PROBLEMS MISSING** and
**S740 PROBLEMS MISSING**. The staged directories are `ScribeRowS718…S743` minus
S723 and S740, plus `ScribeRejS744…S749` — 30 rows, not 32.

Consequence for the census and for `accept-c.py`:

- the registry would reach **643 + 30 = 673**, not the **675** that
  `accept-c.py`'s APPEND leg pins (`count_ok = len(reg_lines) == len(base_lines) + 32`;
  `reports/round-64/telemetry/dry-run-c.txt` at base prints `base=643 measured=643
  +32=False`);
- `accept-c.py`'s ROWS leg iterates `NEW_IDS = S718…S743` (26 ids) and would report
  `S723:rows=0` and `S740:rows=0`; LIVE's frozen subset is
  `S718, S723, S728, S733, S738, S743` and includes S723, so LIVE would fail on it
  too.

The two missing ids are exactly the two ids whose row seats are `ScribeRowS723`
and `ScribeRowS740` in `.ufo/waves/round-64/w1-spec.json` (topics: "overextension
and underextension in early word meaning" and "honorifics and keigo acquisition").
Their subject matter is squarely inside the entry's declared sections 3 and 8
(`gen-w1.py`'s bullet mapping puts S723 in section 3 and S740 in section 8), so
these are not optional rows for the entry's own structure.

This seat does not own those rows and did not author them. Flagged to the
main agent: the row seats for S723 and S740 must land, or the entry/registry
cannot satisfy APPEND/ROWS/LIVE.

### F3 — coverage axis: the 30 staged rows are census-clean and cannot introduce a new W-code

Preflight over every staged `ROW:` line (30 rows) found, for each: exactly 11
cells (NF=13), a legal `kind` (spec|docs|paper|code|tool|dataset|talk|book|community|own-work),
a legal `tier` (A/B/C), a legal `status` (queued|mined|rejected), `opened =
2026-10-23`, `recheck = 180d`, no community-at-tier-A (E10), no thin reject (W02),
no tier-C-mined-with-used-by (W01). Tiers: A 17, B 12, C 1. Statuses: mined 24,
queued 3, rejected 3. The single tier-C row is `ScribeRejS749` (`community`, tier C,
queued) — legal, since E10 only fires community at tier **A**.

URL checks against the live registry:

- **no staged live URL string already occurs in `corpus/SOURCES.md`** (exact-string
  check over every registry line), so the LINK leg's "each new row's live URL
  appears in exactly one registry line" holds for the staged set;
- **no duplicate live URL among the staged rows themselves**, and **no same-URL
  across-scope pair among them**, so appending them adds **0 new W04** rows;
- every staged mined row's `used-by` is exactly
  `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`
  (one distinct value across all 24 mined rows);
- every staged mined row's anchor quote normalises to 8–25 words (the ROWS leg's
  `quote_words` window) — no out-of-range quote.

Scratch confirmation (copy of the registry with the 30 staged rows appended and
S687 flipped `mined → queued`, entry placeholder present):
`scripts/sources-census.sh validate --file <scratch SOURCES.md>` → exit 0,
**0 E-codes**, **27 W04** (unchanged from base), **0 W03** (S687's flip retires
the base's only W03), lane line `file ok <path>`. Scratch census of the same file:
`rows 673`, `tier.A 423`, `tier.B 240`, `tier.C 10`, `status.mined 590`,
`status.queued 61`, `status.rejected 22`, `tier.invalid 0`, `status.invalid 0`.
(The 673 figure reflects the two missing rows; with S723 and S740 present the
count would be 675.)

Also verified: with the entry file absent from the scratch copy, the census emits
**24 E11** rows (`missing used-by corpus/knowledge/linguistics/language-socialization-and-acquisition.md`,
one per staged mined row). E11 is expected and correct until the entry lands —
it is a statement about the entry's absence, not a defect in the rows.

### F4 — calibration axis: the W03 warning and its disposition

The base's single W03 (`S687 mined but unused`) is the round-62 item 7 / round-63
defect that claim C's APPEND leg names explicitly: the leg tolerates exactly one
changed base line, `| S687 …`, whose status flips `mined → queued`, and requires
`cells(r)[7] == "queued"`. The scratch run above shows that flip removes the W03
entirely (W03 goes 1 → 0) and raises `status.queued` 57 → 61 while `status.mined`
goes 567 → 590. The round-62 lesson (`corpus/lessons/round-62.md:50,68`) already
documents the S687 `used-by` → `—` change and asks for exactly this status
decision; the flip is the disposition that lesson asked for.

### F5 — calibration axis: the three `accept-ca.py` numeric nits re-measured and confirmed

`accept-ca.py`'s NITS leg pins `"45"` and `"47"` and `"W04"` and `"27"`. Measured
at base `ff30a20`:

- **45 vs 47 seat reports**: `ls .ufo/waves/round-63/w1/*.md | wc -l` → **47**
  (round 63 landed 47 seat reports, not the 45 its own report says).
- **W04 rows named as S650/S651 vs 27 duplicate-URL rows**: the census prints
  **27** W04 rows (Gate 1 above). The lane's SCORECARD row naming only S650/S651
  understates the class.
- **6 vs 9 dry-run FAIL legs**: `grep -oE '^[A-Z_0-9]+ FAIL' reports/round-63/telemetry/declaration-dry-run-o.txt | wc -l`
  → **9** (GEN, ORDER, BOUND, REDIRECT, MALFORMED, GZIP, TRUNC, TIMEOUT, REVIEW),
  not 6.

The HISTOGRAM leg's target is confirmed too: the frozen census over S694–S717 at
the base prints **A=13 B=11** (24 rows), not the "A 14 / B 10" that the round-63
SCORECARD coverage row records — the discrepancy `accept-ca.py` names as defect 3
(S702 is tier B). Measured from the working tree and from
`git show ff30a205…:corpus/SOURCES.md`, both give `A=13 B=11`.

(These are corroborations of numbers other seats repair; this seat did not edit
`SCORECARD.md` or `LOG.md`.)

### F6 — drift check: the registry is unchanged since round 63

`reports/round-63/telemetry/census-end.txt` and this wave's `census-wave1.txt`
are byte-identical (modulo the two `#` header lines) — 27 W04 + 1 W03 + `ok` in
both. The round-63 closure census and the round-64 wave-1 census agree exactly;
no registry drift happened between the rounds. `git diff --quiet ff30a205… -- corpus/SOURCES.md`
→ exit 0.

## Out of scope for this seat

- Authoring or repairing rows S718–S749, the entry, the README index row, the
  lesson, or the `## Gate` section — other seats own these.
- The `S723` / `S740` row contributions (F2): they are missing, this seat does not
  own them, and inventing a source row for them would defeat the row's own
  rule-1 "open the source" discipline.
- Editing `corpus/SOURCES.md` in any way — explicitly forbidden by the
  assignment and honoured here (verified byte-identical to base).
- Editing any frozen counter leg. No counter was modified; the pre-flight and
  scratch work used scratch copies under `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeCensus/`.
- The live re-open of the new rows' URLs (LIVE leg) and the per-row semantic
  review of topic fit / sentence support — those are the review-only clauses and
  the locator's seats.
- Committing, pushing, publishing, deploying, or invoking another runtime.

## Provenance and limits

Every number above comes from a command run in this session and pasted verbatim.
The census script is `scripts/sources-census.sh` at the fleet root (read-only
parser; it writes only stdout or `--out`). The six manual commands are the frozen
examples in `/home/vgpnk/Projects/shokunin/CORPUS.md` §"Census", copied character
for character. The scratch pre-flight and scratch census are stated as
*predictions* about the post-integration registry, not as observations of the
integrated tree: the real registry is still 643 rows and the integration has not
run.

Not verified here: the correctness of each new row's source or quote (semantic
review), whether the entry's assembled bullets restate the rows faithfully, the
live URL re-open, and the acceptance counters' own PASS/FAIL outcomes. Those
remain unobserved by this seat.

## Tooling

No tool was installed or upgraded. The census script, `gawk`, `awk`, `git`/`jj`
(read-only), and the lane's own `python3` checkers were already present and were
used as-is. No `pacman`, `uv`, `npm`, or binary install was run.

## Artifacts

- `reports/round-64/telemetry/census-wave1.txt` (lane — required census receipt:
  full stdout + exit code 0)
- `.ufo/waves/round-64/w1/ScribeCensus.md` (lane — this report)
- `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeCensus/preflight.txt` (scratch)
- `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeCensus/scratch-validate.txt` (scratch)
- `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeCensus/scratch-lane/` (scratch registry copy)
