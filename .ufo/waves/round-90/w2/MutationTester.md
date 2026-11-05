# MutationTester — round 90 / w2 — independent mutation pass over the landed advance-evidence grader

Seat: MutationTester (leaf, no dispatch). Claim under test: **O / operability** —
`tools/check-advance-evidence.py`, freeze `d0b6f2a7f9cc36272682749a9b047b739406f0c8`,
base `6b0b86e45ae902331aca75863db380f2991458c4`, LANDS `7f3a7aa6615624afadc2cc2d2d4f7ad225f44761`.

Bytes graded here:

```
$ sha256sum /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py
121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed  tools/check-advance-evidence.py
$ git -C <lane> show 3f56892f:tools/check-advance-evidence.py | sha256sum   # lane HEAD when I ran
121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed  -
$ git -C <lane> show 7f3a7aa6:tools/check-advance-evidence.py | sha256sum   # LANDS
121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed  -
```

Worktree, lane HEAD and LANDS are the same bytes and equal `claims.json` `O.tool_sha256`. Nothing here
touches a lane file: the graded tree was extracted with `git archive` into scratch and every mutant is a
fresh file under scratch.

**Result in one line: the frozen 43/43 reproduces byte-identically at LANDS, but it is not
representative of the grader's discrimination surface — 21 new single-point mutants give
`MUTATION-SCORE: 7/21 killed, 14 survived, 0 broken-pattern`, and all 14 survivors are proven
behaviour-changing (they flip a graded leg on a crafted fixture the 67-check selftest never visits).**

---

## 1. Setup (scratch only)

```
$ export TMPDIR=/fast/scratch/hyaku/kotodama-r90/MutationTester/tmp
$ cd /fast/scratch/hyaku/kotodama-r90/MutationTester
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin archive 7f3a7aa6615624afadc2cc2d2d4f7ad225f44761 \
    | tar -x -C lands
$ sha256sum lands/tools/check-advance-evidence.py
121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed  lands/tools/check-advance-evidence.py
```

`git archive` is a read of the lane object store; the only writes are under
`/fast/scratch/hyaku/kotodama-r90/MutationTester/`. No `git`/`jj` mutation, no lane write, no
production write.

## 2. The frozen tally reproduces at LANDS (my own run)

Ran the freeze-pinned driver, unmodified, over the LANDS bytes, with `--root`/`--out` aimed at scratch so
its own receipt write could not land in the lane:

```
$ python3 -B lands/reports/round-90/mutants.py --root lands --work work/repro \
      --out repro/mutation-score
MUTATION-SCORE: 43/43 killed, 0 survived, 0 broken-pattern
tool sha256 121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed
clean selftest green: rc=0 SELFTEST PASS 67/67
  KILLED         overlap-bound-to-zero SELFTEST FAIL 66/67
  KILLED         self-quote-check-off SELFTEST FAIL 66/67
  ...
  KILLED         gate-min-chars-off SELFTEST FAIL 66/67
  KILLED         required-arg-off SELFTEST FAIL 65/67
real 4m29.687s
```

```
$ diff lands/repro/mutation-score.txt \
      /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-90/mutation-score.txt
(no output)
$ python3 -c "import json;d=json.load(open('lands/repro/mutation-score.json'));print(d['total'],d['killed'],d['tool_sha256'])"
43 43 121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed
```

My reproduction is **byte-identical** to the committed receipt — same score line, same 43 rows, same
per-row `SELFTEST FAIL 6x/67` details, same tool sha. The committed `43/43` is therefore honest and
reproducible at LANDS, not an at-freeze-only artifact. (Staged: `repro-mutation-score.txt` /
`.json`.)

## 3. The new mutant set (21 single-point mutants)

Purpose: probe **entry-mode legs** and the two helpers, where the committed 43 are dominated by
`if False:` "delete the check" edits. Composition of my set: **11 mutants edit a span a committed
mutant also edits, but with a different edit** (bound/filter/order change instead of removal) and
**10 edit loci no committed mutant touches** (0 duplicate `(old, new)` pairs — verified by set
comparison over both lists). Sections of the graded object covered: SHAPE repetition threshold and
table floors, TOPIC counter and topic-line scope, NEWIDS qualifier cells (`status`, `opened`,
`tier`, `used-by` index, new-id derivation), GATE url/date/word/char bounds and quote selection,
CAPTURE confinement boundary/traversal/`sha256`/`http_status`/`fetched_at` date, `ROW_RE` indent
window `{0,3}`, and duplicate handling in `ADVANCE`/`SHADOW`.

```
$ python3 -B mut2.py --tool lands/tools/check-advance-evidence.py --work work/m2 \
      --out out/mutation2-score
MUTATION-SCORE: 7/21 killed, 14 survived, 0 broken-pattern
tool sha256 121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed
tool sha256 restored 121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed (unchanged=True)
clean selftest green: rc=0 SELFTEST PASS 67/67
```

| # | mutant | src line | edit (single point) | verdict | observed |
|---|---|---|---|---|---|
| 1 | shape-repeat-threshold-3 | 407 | `if worst > 2` → `> 3` | KILLED | `SELFTEST FAIL 66/67`, `BAD entry repeats a sentence three times` |
| 2 | shape-table-row-off-by-one | 405 | `rows < table_min_rows` → `< table_min_rows - 1` | **SURVIVED** | `SELFTEST PASS 67/67` |
| 3 | topic-floor-off-by-one | 417 | `shared < min_topic_overlap` → `< min_topic_overlap - 1` | **SURVIVED** | `SELFTEST PASS 67/67` |
| 4 | topic-counts-topic-line-only | 413 | `overlap(entry, topic)` → `overlap(topic_line, topic)` | KILLED | `SELFTEST FAIL 65/67`, `BAD positive entry` |
| 5 | newids-status-off | 441 | `if status != 'mined':` → `if False:` | **SURVIVED** | `SELFTEST PASS 67/67` |
| 6 | newids-basesubtract-off | 427 | `new_ids = lands_ids - base_ids` → `lands_ids` | **SURVIVED** | `SELFTEST PASS 67/67` |
| 7 | newids-usedby-index-drift | 437 | `used = cells[10]` → `cells[9]` | KILLED | `SELFTEST FAIL 60/67`, `BAD positive entry` |
| 8 | newids-tier-accepts-c | 438 | `tier not in ('A','B')` → `('A','B','C')` | KILLED | `SELFTEST FAIL 66/67`, `BAD new id at tier C` |
| 9 | gate-word-bound-plus-12 | 476 | `> quote_max_words` → `> quote_max_words + 12` | KILLED | `SELFTEST FAIL 66/67`, `BAD gate quote over the word bound` |
| 10 | gate-char-floor-minus-6 | 476 | `< quote_min_chars` → `< quote_min_chars - 6` | KILLED | `SELFTEST FAIL 66/67`, `BAD gate quote below the char floor` |
| 11 | gate-quote-selection-last | 469 | `line, quote = qs[0]` → `qs[-1]` | **SURVIVED** | `SELFTEST PASS 67/67` |
| 12 | gate-url-slash-relaxed | 472 | `u in line` → `u.rstrip('/') in line` | **SURVIVED** | `SELFTEST PASS 67/67` |
| 13 | capture-prefix-boundary-off | 198 | `cap_dir + '/'` → `cap_dir` | **SURVIVED** | `SELFTEST PASS 67/67` |
| 14 | capture-traversal-guard-off | 196 | absolute/`..` guard → `if False:` | **SURVIVED** | `SELFTEST PASS 67/67` |
| 15 | capture-sha256-skip-absent | 209 | compare only when `sha256` present | **SURVIVED** | `SELFTEST PASS 67/67` |
| 16 | capture-http-status-widen | 211 | `200 <= x < 300` → `100 <= x < 400` | **SURVIVED** | `SELFTEST PASS 67/67` |
| 17 | capture-fetched-date-off | 216 | `if fm.group(1) != as_of:` → `if False:` | **SURVIVED** | `SELFTEST PASS 67/67` |
| 18 | row-indent-unbounded | 49 | `^ {0,3}\|` → `^ *\|` | **SURVIVED** | `SELFTEST PASS 67/67` |
| 19 | row-indent-zero-only | 49 | `^ {0,3}\|` → `^\|` | **SURVIVED** | `SELFTEST PASS 67/67` |
| 20 | advanced-dup-length-lenient | 266 | `len(rows) != 1` → `< 1` | **SURVIVED** | `SELFTEST PASS 67/67` |
| 21 | shadow-url-threshold-3 | 296 | `len(owners) > 1` → `> 2` | KILLED | `SELFTEST FAIL 66/67`, `BAD shadow duplicate url` |

All 21 patterns matched exactly once in the LANDS bytes (0 `BROKEN-PATTERN`), so every row above is a
true single-point mutation of the graded object.

## 4. Every survivor is a real gap, not an equivalent mutant

A survivor only matters if it changes behaviour. Each of the 14 was checked by calling the *same*
grader function on the *same* crafted fixture with the clean bytes and the mutant bytes
(`probe.py`, direct function calls, no subprocess selftest):

```
$ python3 -B probe.py > out/probes-full.txt
14 DIFF lines, 0 EQ lines
```

| survivor | clean bytes | mutant bytes |
|---|---|---|
| shape-table-row-off-by-one | `SHAPE:FAIL table 4x3 < 5x3` | `SHAPE:PASS clean` |
| topic-floor-off-by-one | `TOPIC:FAIL entry shares 11 content words … < 12` | `TOPIC:PASS clean` |
| newids-status-off | `NEWIDS:FAIL S010: status retired not mined; … 0 qualifying new ids < 3` | `NEWIDS:PASS clean` |
| newids-basesubtract-off | `NEWIDS:PASS clean` | `NEWIDS:FAIL S001: opened 2026-10-19 != 2026-11-04` |
| gate-url-slash-relaxed | `GATE:FAIL S010: gate line does not name the row url` | `GATE:PASS clean` |
| gate-quote-selection-last | `GATE:PASS clean` | `GATE:FAIL S010: gate line does not name the row url` |
| capture-traversal-guard-off | `capture path not relative and confined: reports/round-90/evidence/../../secret/leak.txt` | `None` (accepted) |
| capture-sha256-skip-absent | `capture sha256 mismatch: reports/round-90/evidence/S001.txt` | `None` |
| capture-http-status-widen | `capture http_status not 2xx: …` | `None` |
| capture-fetched-date-off | `fetched_at date 2026-11-03 != as_of 2026-11-04` | `None` |
| capture-prefix-boundary-off | `capture outside reports/round-90/evidence: reports/round-90/evidence-extra/S001.txt` | `None` |
| row-indent-unbounded | `ids=[] dup=[]` | `ids=['S777'] dup=[]` |
| row-indent-zero-only | `ids=['S777'] dup=[]` | `ids=[] dup=[]` |
| advanced-dup-length-lenient | `ADVANCED:FAIL 0 advanced; S001: 2 rows at lands \| SHADOW:FAIL duplicate ids: S001` | `ADVANCED:PASS 1 advanced \| SHADOW:FAIL duplicate ids: S001` |

## 5. MUTATION-SCORE for this set

```
MUTATION-SCORE: 7/21 killed, 14 survived, 0 broken-pattern
```

For reference the frozen set's own line at LANDS, from my reproduction: `MUTATION-SCORE: 43/43 killed,
0 survived, 0 broken-pattern`.

## 6. The survivors, one line each

1. **shape-table-row-off-by-one** — the only table fixture is 4 rows below the floor, so the `>=5` boundary is unpinned; a 4-row table lands.
2. **topic-floor-off-by-one** — the TOPIC floor is pinned only by an entry sharing 0 words with the topic and by `--min-topic-overlap 40`; the 7-vs-8 edge is free.
3. **newids-status-off** — no cited new row carries a status other than `mined` (the only `rejected` row is uncited), so the `status` qualifier cell has no negative at all.
4. **newids-basesubtract-off** — no fixture has the entry citing a base-only row, so `lands_ids - base_ids` is unpinned; the mutant *over*-rejects (`S001: opened … != …`) a legitimate entry.
5. **gate-quote-selection-last** — every lesson fixture has exactly one quoted line per id, so *which* gate line is graded (`qs[0]` vs `qs[-1]`) is order-dependent and untested.
6. **gate-url-slash-relaxed** — no fixture url carries a trailing slash, so the url match can be loosened without detection.
7. **capture-prefix-boundary-off** — the only out-of-dir fixture (`reports/round-90/elsewhere/`) fails both with and without the `/` boundary; a sibling `evidence-extra/` is never tried and would be accepted.
8. **capture-traversal-guard-off** — no fixture capture path is absolute or contains `..`; with the guard gone, an existing file reached through `..` under the capture dir is accepted (sha, status, date and quote all pass).
9. **capture-sha256-skip-absent** — `_manifest` always writes a digest, so no fixture omits `sha256`; the mutant accepts a manifest entry with no digest at all.
10. **capture-http-status-widen** — the only status negative is `503`; `1xx`/`3xx` are never tried, so widening to `100..399` passes.
11. **capture-fetched-date-off** — `mjunk` only tests the *format* of `fetched_at`; no fixture shifts the date, so "fetched on another day" is untested.
12. **row-indent-unbounded** — no fixture registry row is indented, so a 4+-space-indented `| S… |` line (a quoted or nested-list table) would be ingested as a registry row.
13. **row-indent-zero-only** — same blind spot in the other direction: 1–3 space indents are legitimate per `ROW_RE` and are dropped by the mutant, with no fixture noticing.
14. **advanced-dup-length-lenient** — the duplicate-id fixtures are still failed by `SHADOW`, so `ADVANCED`'s own `!= 1` guard could be removed without a `BAD`; defence-in-depth here is real, but that leg's guard is unpinned.

## 7. Verdict: is the frozen 43/43 representative?

**It reproduces exactly and it is honest, but it is not representative of the graded object's
discrimination surface.**

- Representative *of what it claims*: the score line, the 43 rows and every `SELFTEST FAIL 6x/67`
  detail are byte-identical to `reports/round-90/mutation-score.txt` when run at LANDS today, so
  `O.predicate`'s "`killed==total>=42`, 0 survived, 0 broken-pattern" is a true statement about those
  43 mutants. The committed set is also structurally sound: every entry is a real single-point edit,
  and 38/43 are killed by exactly one check (`SELFTEST FAIL 66/67`); four fail two (`65/67`) and
  `recheck-iso-off` fails 21 at once (`46/67` — `d = as_of` really does collapse most advance-side
  checks), so its kill is coarse rather than localized.
- Not representative *of the grader's strength*: the committed set is 43 check-removals and constant
  swaps, and the selftest has one negative per sub-check, so a removal is killed almost by
  construction. At **six spans** a committed mutant is KILLED while my boundary mutant at the same
  span SURVIVES — table floor (405), topic floor (417), capture dir boundary (198), `sha256` (209),
  `http_status` (211), gate url (472). That is the definition of a kill set that proves *the check
  exists* but not *where the check stops*. 24 of the 67 checks are entry-mode fixtures; of my 14
  survivors 6 sit in entry-mode legs proper (SHAPE, TOPIC, NEWIDS ×2, GATE ×2), 7 more in helpers the
  entry legs call (`capture_error` ×5, `registry` ×2) and only 1 in `ADVANCED`.
- Consequence for claim O: nothing here falsifies it. The predicate only asserts the pinned 43, and
  `O.bounds` already says discrimination "does not prove that no other counterfeit class exists". What
  must not be read into `43/43` is "the grader refuses every plausible single-point defect": 14
  plausible ones, all with proven behavioural differentials, pass its own selftest at 67/67.
- Recommended (next round, not this one — the claims are frozen and no repair is in scope): add
  fixtures for the boundary rather than the switch — a 4-data-row table, a `shared == floor-1`
  entry, a cited new row with `status: retired`, an entry that cites a base-only row, a lesson with
  two quoted lines for one id, a trailing-slash url, a capture in a prefix-sibling dir, a `..`
  capture path, a manifest entry with no `sha256`, `http_status: 302`, `fetched_at` on the previous
  day, and both a 1-space and a 4-space indented registry row. Those 14 negatives alone would move
  the score from 7/21 to 21/21 without touching the grader.

## 8. Things I did not do, and things found that are not mutants

- I did not re-verify, re-date or repair any registry row, did not run the C counter, did not judge
  the entry's scholarship, and did not touch the lands revision beyond `git archive` extraction.
  Freshness stays paused; no freshness claim is made.
- Non-mutant observation (maintainability, no behaviour): `grade_entry` assigns
  `topic_line = next((l for l in entry.splitlines() if l.strip().startswith('- topic:')), '')` and
  never uses it — the TOPIC leg counts against the whole entry. Mutant 4 exists only because that
  dead value is reachable; the line should be deleted or the leg should use it deliberately.
- The selftest is stronger than its exit codes suggest: mutant 9 keeps `rc=1` on the word-bound
  fixture but is still killed, because `_run` also asserts the failing **leg name** (`FAIL GATE`)
  appears. Do not weaken those `expect=` substrings.
- Deviation from the ticket's "at least ten NEW mutants": 21 were written and 21 run; the count is
  reported as observed, not padded.

## 9. Reproduction, hygiene, tooling

Artifacts staged at
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-90/w2/stage/MutationTester/`:
`mut2.py` (21-mutant harness), `mutation2-score.txt` / `.json`, `probe.py` (differential probes),
`probes-full.txt`, `repro-mutation-score.txt` / `.json` (the 43/43 reproduction).

```
$ python3 -B mut2.py  --tool lands/tools/check-advance-evidence.py --work work/m2 --out out/mutation2-score
$ python3 -B probe.py > out/probes-full.txt
$ python3 -B lands/reports/round-90/mutants.py --root lands --work work/repro --out repro/mutation-score
```

- Restoration: the graded source was never written. Each mutant is a separate `m-<name>.py` in
  `--work` (unlinked after its run); tool sha256 before `121888f0…` and after `121888f0…`
  (`unchanged=True`), and `sha256sum lands/tools/check-advance-evidence.py` re-checked after the
  probe run is still `121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed`.
- Lane status after my work: only other seats' changes (`M corpus/…petitionary-and-votive-formulae.md`,
  `M reports/round-90/census-end.txt`, untracked wave dirs, HEAD `3f56892f`); no file I wrote is in
  the lane outside `stage/MutationTester/` and this report.
- Scratch `/fast/scratch/hyaku/kotodama-r90/MutationTester/` (all clones, fixtures, mutant files,
  `TMPDIR`) was removed with `rm -rf` on exit; nothing cited above lives in `/tmp`.
- Tooling: no installs, no upgrades, no `pacman`. `python3 3.14.8` (system) was sufficient;
  `mutants.py` and `measure90.py` were read, never modified.

Report: .ufo/waves/round-90/w2/MutationTester.md
