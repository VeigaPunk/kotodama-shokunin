# Round 89 — non-author verifier spot-check

author: hyaku closure (non-author integrator, @m_zfl)
lane: kotodama · lane_round: 89 · campaign: hyaku · verified: 2026-11-04 (UTC)
report: `.ufo/reports/round-89/kotodama.md` at `dfea45fb6dbb8bcf29114d9436dc2770960e3fc1` (fleet)
lane: base `42816d2533c44f1d19f38a12fc5f5040d01a2fd3` → after `bd4153ff1f67650487edcdcd98af74cd30280899`
dispatch digest (`.ufo/watchdog.log`, mutable — copied here): `2026-11-04T18:53:44-03:00 launch kotodama round=89 pgid=1458626 driver=hyaku-inline attempt=1`; `2026-11-04T19:26:44-03:00 complete kotodama round=89; hyaku-inline attempt=1`.

I did not author this round. I re-measured what committed bytes can show, re-opened
sampled sources live, and did not execute the lane's counter (PROTOCOL §Gate
standard, Closure consequence). Nothing in this file edits lane-authored bytes.

## 1. Step-1 conformance

| check | command | observed | verdict |
|---|---|---|---|
| report committed by lane identity | `git log --format='%an <%ae> %H' -- .ufo/reports/round-89/kotodama.md` | `kotodama-shokunin <kotodama@shokunin.local> dfea45fb…` | pass |
| `SHONEN` heading, one line per box | `grep -c '^## SHONEN'`; lines under it | `1`; four `[~]` lines, `[x]` count `0` | pass |
| cited lane commits exist and are ancestral | `git cat-file -e` + `git merge-base --is-ancestor <h> main` for `1cbd0efc 9ad00be1 590c2067 aac9cca8 bd4153ff` | all `exists=yes ancestor=yes`, each `author=kotodama-shokunin`; `git rev-list --count base..after` = 5 | pass |
| lane clean and pushed | `scripts/hyaku/jj-lane.sh state …/kotodama-shokunin`; `git status --porcelain` | `branch=main local=bd4153ff remote=bd4153ff ahead=0 behind=0 tracked=0 untracked=0`; porcelain empty; `ls-remote origin refs/heads/main` prints `bd4153ff…` | pass |
| prompt carries the template contract | `diff <(sed -n '1,140p' templates/round-prompt.md) <(sed -n '1,140p' .ufo/prompts/kotodama-round-89.md)` | only placeholder substitutions (`{{LANE}}`, `{{ROUND}}`, `{{FLEET_ROOT}}`, axes) differ; round-level items (i)–(v) and the five child-lane items all present | pass |
| L2 route map vs `MISSION.md` | `grep -n 'L2 concurrency' MISSION.md` | MISSION gives ≥8 in one batched call and only advisory role-class buckets, no alias map; prompt §3 matches the floor and §6 routing is host-mechanics text | pass (no conflict to grade) |
| fleet leftovers | `git -C /home/vgpnk/Projects/shokunin status --porcelain` | only other lanes' closure scratch, `.scratch/run15-state.json`, `kama.md`, and `after` (2026-11-03 20:05, predates the round) — the round's own misroot sweep is committed (`reports/round-89/final/misroot-sweep.txt`) | pass |
| L0 durability | `git show 7b398ea8 -- .ufo/l0-questions.md` | one added line, `kotodama \| round-89 \| Does live source re-verification …`; commit pushed (`origin/main` contains it) | pass |

Conformance defects: none found. Status-neutral observations: `w1-results.json` carries no
per-seat status/id (the lane names it as the inherited R88-M6 gap; delivery is evidenced by
11 committed seat reports); the entry header uses the lane's standing `topic:` /
`sources:` convention rather than CORPUS.md's literal `source:` (pre-existing in every
entry, not a round-89 change — for the aggregator, not this closure).

## 2. Claim re-checks

Re-measured by me over committed bytes: the population, the cell deltas, the registry
counts, the entry's size/shape/citations, the index and partition counts, and the
shingle overlap. Evidence-verified (not executed by me): the lane's frozen counter
receipts, its selftest tally, its red-before, its controls and its separability receipts.

### F / freshness — measured, re-derived

| quantity | command | observed |
|---|---|---|
| registry rows base→after | `git show <rev>:corpus/SOURCES.md \| grep -cE '^\| *S[0-9]{3,} *\|'` | `859` → `865` |
| tiers | `awk -F'\|' … $5` histogram | `A=507 B=328 C=24` → `A=511 B=329 C=25` |
| status | same, `$9` | `mined=757 queued=58 rejected=44` → `mined=762 queued=58 rejected=45` |
| changed base rows | cell-wise compare of all 11 columns, base vs after | exactly 16 rows changed, each `('recheck',)` only; no `status`/`used-by` cell moved |
| recheck cell values | `awk -F'\|' … $11` for the 16 ids | all 16 `90d` → `2027-02-03` |
| the 16 ids | diff of the registry | S009 S012 S020 S021 S031 S032 S033 S084 S104 S105 S106 S107 S142 S157 S163 S875 — matches the report |
| new rows | diff | S936 S937 S938 S939 S940 S941 added, nothing else |
| independent re-open (sampled) | `curl https://cals.info/statistics/` | page text still reads `1323` conlangs, `127` natlangs, `145 features`, `97 .9% of all features are from WALS`; the committed capture `rechecks/S009.txt` carries the same numbers across line breaks, so the lesson quote is a whitespace-normalized concatenation of visible text — agree |

Frozen counter receipts, read but not executed: `final/lands-F.txt` `ACCEPT-F-89: PASS
legs=5/5` (ADVANCED 16, BACKED 16/16, DISPOSED, OTHERCELLS), stamped and evaluated at
`aac9cca80d12077eb3026b202c835c0d6135bc08`, freeze `1cbd0efc…`; `at-freeze-F.txt` FAIL
3/5 (ADVANCED 0, DISPOSED 9…); `counter-selftest.txt` `SELFTEST: PASS 21/21`;
`selftest-redbefore.txt` mutant sha256 `80a8aa56…` → `SELFTEST: FAIL 18/21`, exit 1;
`controls/controls.txt` 9/9 match expectation with two declared known survivors;
`rechecks/refetch-agreement.json` 16/16; `final/recheck-queue-lands.txt` `0 due / 4
upcoming / 16 on-release / 865 rows`. Before→after and the report agree.

Two of the 16 advances carry less freshness than the rest, and the lane states both:
S142's only URL is a fixed 2025-03-31 Wayback memento (an immutable archive cannot drift),
and S032's quote is the paper title, which is exactly that row's declared scope
(`bibliographic identity and title-level position … arguments are unread`). Discounting
both still leaves 14 ≥ the frozen ADVANCED target of 10.

### C / coverage — measured, re-derived

| quantity | command | observed |
|---|---|---|
| entry size | `wc -c corpus/knowledge/linguistics/evidentiality-epistemic-marking.md` | `19901` (report: 19901 B) |
| headings | `grep -c '^##'` | `10` (report: 10 headings) |
| table shape | `awk -F'\|' '/^\|/{print NF-2}'` | 8 table lines × 5 columns = header + separator + 6 data rows (report: 5×6) |
| knowledge files base→after | `git ls-tree -r --name-only <rev> corpus/knowledge \| wc -l` | `260` → `261`; linguistics `33` → `34` (README: `## linguistics/ (34)`, total 261) |
| entry citations | `grep -oE 'S[0-9]{3,}' <entry> \| sort \| uniq -c` | S936 14, S937 16, S938 6, S939 21, S940 3 — no population id cited |
| new rows mined | `awk` over S936–S941 | S936–S939 `A/mined`, S940 `B/mined`, S941 `C/rejected`, all `opened 2026-11-04`, `used-by` = the entry (S941 = the lesson) |
| 8-word shingle overlap | my own shingle count, entry vs five neighbours | 0 shared shingles / 2936 for each of semantics-pragmatics, syntax-typology, conlang-methodology, morphological-typology, semantic-fields-lexicon-building |
| census | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` | `rc=0`, final line `kotodama ok` (warnings only: 29 pre-existing W04 duplicate-URL rows and 6 pre-existing W01 tier-C mined rows, none of them S936–S941) |

Frozen counter receipts, read but not executed: `final/lands-C.txt` `ACCEPT-C-89: PASS
legs=8/8` (ENTRY 19901 B / 10 headings, TABLE `[[5,6]]`, NEWIDS S936–S940, GATE, CAPTURE,
INDEX tool rc0, APPENDONLY) at the same lands revision; `at-freeze-C.txt` FAIL 2/8;
`final/separability.json` `lands_descends_from_freeze: true`, overlay F `PASS legs=5/5`,
overlay C `PASS legs=8/8`, each on its own one-claim overlay.

Base-state honesty: `42816d25:corpus/knowledge/linguistics/semantics-pragmatics.md:66`
already carries `## 4. Evidentiality and mirativity: grammar of where you know from`
(source/mirative split, evidential ≠ epistemic, Willett hierarchy, five canonical systems,
a 3×5 inventory table) and `syntax-typology.md` §4 a sizing table. The frozen
`claims.json` surface text called this "only scattered sub-bullets"; the lane's R89-M4
records the correction and rates C's surface *contested*. The delta is real (77A/78A
counts with sample bounds, the coding axis, access/egophoric, areal spread, a NON-CANON
design), so C is a genuine net-new admitted entry on ground the coverage map did not hold,
with the surface caveat stated rather than hidden.

## 3. Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| freshness | **improved** | 16/16 queue rows re-located live, quotes agree 16/16, recheck `90d` → `2027-02-03`, auditor `20 upcoming` → `4`; re-derived cell-wise, one row re-opened live by me. Admission is withheld, not because the measurement failed, but because the claim class sits under the operator's open round-11 pause (see §6). |
| coverage | **improved** | new 19901 B entry, 10 sections, 5×6 coding table, S936–S940 mined and cited 60 times, partition 33→34, overlap 0; surface contested (R89-M4) and disclosed. |
| calibration | **improved** | the wave falsified the lane's own frozen surface sentence and the lane recorded it as R89-M4 rather than defending it; it declared the counter's mutation score 10/41 (R89-M5) and the undeclared survivor classes (R89-M6); it wrote no `[x]` and did not claim admission. |
| depth | unchanged | no existing entry deepened; `git diff --numstat base after -- corpus/knowledge PROVINCE.md` names only the new entry; PROVINCE.md untouched. |
| operability | unchanged | no new lane tool enters the repertoire; `measure89.py` and `separability89.py` are round receipts, and no capabilities row was added. |
| adjacency | unchanged | `ConnectorSiblings` grep over every sibling (39 hits, all the English adjective) finds no sibling holding evidentiality or WALS 77/78; lore CM-d reliability grading is handed off, not absorbed. |

No axis is harmed. The 16 registry edits are append-only-legal (only `recheck` moved), the
entry cites none of the population ids, and PROVINCE.md is unchanged.

## 4. Discernment spot-check (non-author)

| item | decision | re-opened source | agree / disagree | reason |
|---|---|---|---|---|
| S936 WALS ch. 77 (admit, A/mined) | admit | `https://wals.info/chapter/77` fetched 2026-11-04 | **agree** | live page contains the quoted sentence verbatim: "There are no languages in the sample that have grammaticalized direct evidentials, but no grammaticalized indirect evidentials." — chapter-author text, and the sample-bounded scope is the right tier scope |
| S937 WALS ch. 78 (admit, A/mined) | admit | `https://wals.info/chapter/78` fetched 2026-11-04 | **agree** | live page contains "When a language uses separate particles for evidentiality, this is very strongly correlated with coding indirect evidentiality only." and the Dumi example (6); the coding typology is the author's own |
| S940 SIL Glossary (admit, B/mined) | admit | `https://glossary.sil.org/term/evidentiality` fetched 2026-11-04 | **agree** | live Definition reads "Evidentiality is distinct from (epistemic) modality which concerns the speaker's evaluation of his or her statement, for example, with regard to its certainty."; B at glossary depth is the honest tier |
| S941 Glottopedia (reject, C/rejected) | reject | `http://www.glottopedia.org/index.php/Evidentiality` fetched 2026-11-04 | **agree** | page is marked `STUB`, defines evidentiality as "a way of marking epistemic modality" (the conflation the entry must not inherit), and gives an unreferenced four-way Turkmen paradigm; the stated flip condition (a referenced revision) is the right one |
| S009 registry row (claim F) | admit as LOCATED | `https://cals.info/statistics/` fetched 2026-11-04 | **agree** | live quick-numbers block still carries 1323/127/145/97.9%-from-WALS, the figures the `teaches` cell claims; the lesson quote is that block, whitespace-normalized |
| S032 row quote | accept at row scope | row `scope` cell + `reports/round-89/rechecks/S032.txt` | **agree** | the quote is the paper title, which is exactly the row's declared scope ("arguments are unread"); it is not a substitute for reading the paywalled body, and the lesson says so |
| S142 row quote | accept with caveat | row `source` cell (fixed 2025-03-31 Wayback memento) | **agree** | the row's source is the archive capture by declaration, so re-opening it is legal; it proves immutability, not drift, and the lesson labels it so |

Gate decisions sampled: 3 admits, 1 reject, 2 recheck rows, 1 archive caveat. The gate and
the outside check agree on every sampled item; the two disagreements the wave itself found
(title/chrome quotes and copied-section landings, R89-M5/M6) are recorded and were turned
into `QUALITY.md` criterion 36, which is the `LEARNING.md` condition for
`discernment: improved`.

## 5. Trend verdicts

- **expansion: improved.** One admitted `knowledge/` entry on ground the coverage map did
  not hold, citing `mined` rows S936–S940 and its own new `corpus/README.md` row;
  8-word shingle overlap 0 against all five neighbours. The ground was partly held as
  sub-sections (R89-M4), which is why the surface is reported contested, not clean.
- **quality: improved.** Sixteen stale-dated registry rows re-verified live against their
  own declared sources with 16/16 independent agreement; no `teaches` cell was found false;
  the auditor's upcoming queue fell 20→4; four stale findings (S142 anchor wording, S012
  v1→v4, S021 v1→v2, S157 biomes, S104 script-only children) were flagged, not hidden, and
  `QUALITY36` plus the SKILL re-verification method were added. `harmed` is excluded: no
  admitted entry was found false and left unmarked.
- **discernment: improved.** The non-author spot-check agrees on all sampled admits and the
  reject, and the wave's disagreements became lesson rows with a grounded `QUALITY.md`
  criterion — the criterion cites the executed fixtures, not a vibe.

## 6. Routed defects for round 90

1. **Freshness pause (governance, admission bar).** L0 `kotodama | round-11` ends
   "Freshness axis-move claims are paused until ruled" and carries no answer; the lane's
   own SCORECARD says F's admission is contingent on that ruling. Admitting F here would
   answer an open L0, so this closure records F as measured and withholds admission
   (round verdict `rejected-honest-stop`, improvements preserved — the r49 precedent).
   No further freshness axis-move until the operator rules L0 `kotodama | round-89`.
2. **F predicate counts archive re-locates as advances.** S142's only surface is a fixed
   2025-03-31 memento; the counter's `url_ok` accepts any Wayback timestamp. Round 90
   should either exclude immutable-archive rows from a freshness population or require a
   memento year ≥ the round's year (ConnectorSiblings F-1, unchanged since it is frozen).
3. **Stale findings carried, not repaired.** S142 anchor "by" vs source "for"; S012/S021
   arXiv versions; S104's children only in the page script; S157's biome list. `OTHERCELLS`
   forbids repairing them in the claiming round — repair them in round 90 or record why not.
4. **Counter strength.** Mutation score 10/41, and five undeclared survivor classes (shadow
   duplicate rows, site-chrome/title quotes, capture = graded file, NOT-LOCATED spelling
   variants, copied-section filler). QUALITY36 binds round 90: one selftest negative per
   sub-check and a committed mutation-score receipt before dispatch.
5. **Frozen surface statements must be base-measured.** C's `surface` text was false at the
   freeze. Round 90's before-state for any topic claim must quote
   `grep -rn -i '^## .*<topic>' corpus/knowledge` at the base commit (QUALITY36), so a
   wave cannot have to catch it after the fact.
6. **Minor precision.** The new `recheck` cell is `2027-02-03` = as_of + 91 days (the
   frozen ADVANCED leg needs `> 2027-02-02`), while the lesson prose says it "keeps the
   rows' 90-day cadence"; the value is right for the predicate, the prose is loose by one
   day.

## 7. What this closure does not do

No lane-authored file was edited. No `[x]` was written into `SHONEN.md`; all four boxes
remain `[~]` and promotion stays operator-owned. The lane's counter was not executed. The
open L0 questions were not answered.
