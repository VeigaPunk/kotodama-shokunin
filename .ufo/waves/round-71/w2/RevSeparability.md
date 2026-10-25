# RevSeparability — claim-separation review (round 71, wave 2)

Seat: `L1Kotodama71.RevSeparability` (leaf, read-only; no spawns, no lane writes except this file).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Stamped revision: **27db4ce** (`27db4ce round-71: id map regenerated post-landing (S874+) + R71-M14 anchor-base note`).

The lane moved while this seat ran (`14c88d9` → `e7e7e26` → `1721fbd` → `f5c845b` → `e1d0d44` → `27db4ce`).
Every verdict below was re-derived at `27db4ce`; earlier readings were discarded, and where a finding was
already repaired by a later commit (F1) both states are recorded. The tree is still moving, so each finding
cites the exact command and output so it can be re-checked at any later revision.

## Verdict

**CONFIRMED (PASS): the three claims are file-segment disjoint.** The only shared file is
`corpus/SOURCES.md`, and within it claim C adds lines 816–828 (S861–S873) while claim Ca replaces line 815
(S860) in place. No line, no cell, and no row is written by two claims. D writes only its own counter and its
own receipt.

**Isolation holds at runtime, not just on paper.** A base tree carrying *only* C's bytes passes `ACCEPT-C-71`
and fails `ACCEPT-CA-71`; a base tree carrying *only* Ca's bytes passes `ACCEPT-CA-71` and fails
`ACCEPT-C-71`. Neither claim's predicate is satisfiable by the other claim's landings.

**One cross-claim defect found (F1)**: C's 13 new rows occupied the exact id span (`S861–S873`) that Ca's
landed item-10 map certified as free (`next_free: S861`). The claims are file-disjoint but were not
state-disjoint at the registry tail. The lane regenerated the map at `27db4ce` (`next_free: S874`, span
`S874→S1005`, no target id occupied), which removes the double-assignment hazard; the map's `collisions` field
and the lesson/LOG/quarantine citations were not updated and still name the old set (F1).

## Landings verified

### Claim C — coverage (entry, rows, README)

| leg | command | result |
|---|---|---|
| entry exists | `test -f corpus/knowledge/culture-material/dance-performance-movement-codes.md` | PASS (10149 B) |
| partition/corpus | `find corpus/knowledge/culture-material -maxdepth 1 -type f \| wc -l`; `find corpus/knowledge -type f -name '*.md' \| wc -l` | PASS 36 / 243 |
| rows | `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` | PASS 797 (784 + 13, not 12) |
| rows are new | `git show b94a543:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S86[1-9]\|^ {0,3}\|[[:space:]]*S87[0-9]'` | PASS 0 at base (base max id S860) |
| row shape | `awk -F'\|' '/^\| S861 /{print NF}' corpus/SOURCES.md` | PASS 13 fields, same as S860 |
| entry citations | `grep -oE 'S[0-9]{3,}' <entry> \| sort -u` | PASS exactly S861–S873 (13) |
| README | entry row verbatim vs entry `- topic:` line 20; header `## culture-material/ (34)` → `(36)`; footer 242→243 | PASS |
| README sweep | `python3 reports/round-28/readme/sweep.py` | PASS exit 0, totals 243, `footer_findings []` |
| counter | `python3 -B reports/round-71/accept-c.py` | PASS `ACCEPT-C-71: PASS`, exit 0 |

Base control re-derived (`/tmp/sep71/base` = `git archive b94a543`): filename sweep prints nothing, word-bounded
topic sweep prints nothing, unbound sweep matches `funerary-material-culture.md:4` ("avoidance") — the
word-bounded correction in `claims.json` is the true one.

### Claim Ca — records (receipts, S860, corrections, scorecard, lesson, quarantine)

| leg | command | result |
|---|---|---|
| six round-70 receipts, six header lines each | `for f in reports/round-70/telemetry/{measures,controls}-{o,ca,d}.txt; do grep -cE '^# (counter sha256\|stamped revision\|evaluated revision\|measured revision\|tree\|worktree dirty)' $f; done` | PASS 6 6 6 6 6 6 |
| original bytes preserved | `grep -c 'original bytes preserved below' reports/round-70/telemetry/measures-o.txt` + first line below marker is `# after-state receipt` / `# pre-data control` | PASS |
| S860 repoint | `grep -n 'acc2d614' corpus/SOURCES.md` | PASS 1 (line 815) |
| S860 blob is real | `git rev-parse acc2d614:tools/check-supersession-settlement.py` | PASS `6a314e9c7c5635a15a9b2f8b57bc34db8039a301` |
| corrections | `grep -cE '^\| V70-[1-5] ' reports/round-71/corrections-r70.md`; rows containing `→` | PASS 5 / 5 |
| scorecard row | `grep -c 'round-70 trend-correction' SCORECARD.md` | PASS 1 |
| lesson reject sweep | `grep -c 'rejected this round:' corpus/lessons/round-71.md` | PASS 1 |
| lesson Gate quotes | 13 pipe-table rows S861–S873 | PASS 13 |
| quarantine table | `awk -F'\|' '/^\| S[0-9]+ \| (PRESENT\|REFUSED\|UNVERIFIABLE) \|/' reports/round-71/telemetry/quarantine-verdicts.md \| wc -l` | PASS 21 rows, 21 unique ids, tally PRESENT 10 / REFUSED 7 / UNVERIFIABLE 4 |
| quarantine class leg | `accept-ca.py` `class_ok`: unreachable-class rows S807/S812/S835 must be `UNVERIFIABLE` | PASS |
| counter | `python3 -B reports/round-71/accept-ca.py` | PASS `ACCEPT-CA-71: PASS`, exit 0 |

Quarantine ids cross-checked against the registry: 20 of 21 have a live row; S778 has none (`grep -c` = 0) and
is verdicted PRESENT (EUC-JP decode of the fetched page). No verdict row id falls in C's S861–S873 block. The
table's tally and two verdicts (S778 PRESENT, S816 REFUSED) were re-derived in `57e0a72` after this seat's first
pass; the row count and id set are unchanged, and the `class-admissibility` leg landed in the same commit.
The committed receipt for this leg is stale — see **F8**.

### Claim D — depth (accept-d.py + measures-d)

| leg | command | result |
|---|---|---|
| in-repo selftest | `python3 -B reports/round-71/accept-d.py --selftest` | PASS `SELFTEST: 2/2`, exit 0 |
| no-git path | `T=$(mktemp -d); tar --exclude=.git -C . -cf - . \| tar -C $T -xf -; cd $T; python3 -B reports/round-71/accept-d.py --selftest` | PASS `SELFTEST: COULD-NOT-EVALUATE (no git)`, exit 2 |
| frozen predicate | `python3 -B reports/round-69/accept-d.py --root .` | PASS `ACCEPT-D-69: PASS legs=8/8`, exit 0 |
| receipt | `reports/round-71/telemetry/measures-d.txt` committed; `# counter sha256 (self)` = `459cfa9d…` = `sha256sum reports/round-71/accept-d.py` | PASS |
| file exclusivity | D writes `accept-d.py` + `measures-d.txt` only; no C or Ca file appears in D's surface | PASS |

## Same-file-segment analysis (`corpus/SOURCES.md`)

Base→HEAD net diff is exactly two disjoint segments:

```
$ git diff b94a543..HEAD -- corpus/SOURCES.md | grep -E '^[-+]' | grep -vE '^(\+\+\+|---)' \
    | sed -E 's/^([-+])[[:space:]]*\|[[:space:]]*(S[0-9]+).*/\1 \2/' | sort | uniq -c
      1 + S860      <- Ca: in-place cell repoint (V70-2)
      1 - S860      <- Ca
      1 + S861 … 1 + S873   <- C: 13 appended rows (S861..S873, one each, no deletions)
```

Line map at HEAD: `S860` = line 815 (unchanged from base — base line 815 too), `S861–S873` = lines 816–828,
`## Paths` = 829. Ca's write is line 815 only; C's writes are 816–828 only. **No overlap.**

Row-integrity: `grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' | sort | uniq -d` → 0 duplicate ids.
`awk -F'|' '/^\| S860 /{print NF}'` = 13 and `S861` = 13: Ca's cell replacement preserves the table's column
arity, so C's rows are not shifted into a malformed table.

### Isolation experiment (the load-bearing evidence)

Two snapshot trees, both `git archive b94a543` plus one claim's bytes only; SOURCES reconstructed by
reverting the other claim's segment:

```
conly  = base + HEAD entry/README/accept-c.py + HEAD SOURCES with S860 reverted to base
caonly = base + HEAD receipts/lesson/scorecard/LOG/accept-ca/corrections/quarantine + HEAD SOURCES minus S861–S873

conly  rows=797 acc2d614=0   -> accept-c  PASS ; accept-ca FAIL (all six legs FAIL)
caonly rows=784 acc2d614=1   -> accept-ca PASS ; accept-c  FAIL (ENTRY, COUNTS, then FileNotFoundError)
```

Read both ways: each claim is provable from its own bytes alone, and neither claim's target is reachable from
the other claim's bytes. This is the strongest available proof of claim separation.

### Residual patch-level coupling (not a segment violation)

The two SOURCES edits are line-disjoint but share diff context, and the order is fixed:

- C's append hunk (`8c203bd`) carries the **S860 line as context** (`git show 8c203bd -- corpus/SOURCES.md | grep -n S860` → 1 context line).
- Ca's repoint hunk (`1d1b432`) carries **S861–S863 as trailing context** (`@@ -812,7 +812,7 @@`, context rows S861–S863 visible).

So C's patch depends on pre-Ca S860 bytes and Ca's patch depends on post-C rows; applied in the opposite
order either patch would conflict. This is a sequencing constraint on the two landings, not a shared segment.
It is satisfied by the landed order (C at 08:34/08:35, Ca at 08:38).

## Findings

### F1 — MEDIUM at e1d0d44, now LOW — C's row block falsified Ca's item-10 map; the map was regenerated but its collision list and the citing records were not

**State at e1d0d44 (as found).** Ca's landed records certified the registry tail as it stood at 784 rows while
C's 13 rows already occupied it:

```
784 S861 ['S859', 'S860']                       <- map at e1d0d44
actual staged∩lane = S859 … S873 (15 ids)
map target ids occupied = S861 … S873 (13 ids)
```

`map["S859"] == "S861"` and lane row `S861` was UNESCO Tango: the first 13 renumber targets were taken.

**State at 27db4ce (repair).** Commit `27db4ce` regenerates the map:

```
$ python3 - <<'PY'
import json,re
m=json.load(open('.ufo/waves/round-71/assimilation/id-renumber-map.json'))
lane=set(re.findall(r'^\s{0,3}\|\s*(S\d{3,})\s*\|',open('corpus/SOURCES.md',encoding='utf-8').read(),re.M))
staged=set(open('.ufo/waves/round-71/assimilation/staged-ids',encoding='utf-8').read().split())
print(m['registry_count'], m['next_free'], m['span'], m['collisions'])
print(sorted(staged&lane,key=lambda s:int(s[1:])))
print(sorted(set(m['map'].values())&lane,key=lambda s:int(s[1:])))
PY
797 S874 S874→S1005 ['S859', 'S860']
['S859','S860','S861','S862','S863','S864','S865','S866','S867','S868','S869','S870','S871','S872','S873']
[]
```

The double-assignment hazard is gone: `next_free: S874`, span `S874→S1005`, no target id occupied.

**What remains at 27db4ce.**

- The map's own `collisions` field still lists **2** ids where staged∩lane is **15** (S859–S873). A consumer
  that reads `collisions` without re-deriving will believe 13 colliding ids do not collide.
- The records that cite the map still quote the **pre-regeneration** span and collision set:
  `corpus/lessons/round-71.md:81` "Id collisions S859/S860 …" and `:83`
  "collisions S859 S860; id-renumber-map.json S861→S992 by document";
  `reports/round-71/telemetry/quarantine-verdicts.md:37` "(id collisions S859/S860 recorded at …)";
  `LOG.md:4274` "id collisions S859/S860 recorded with renumber map (S861→S992 by document)".
  The lesson now contradicts both the regenerated map (S874→S1005) and its own line 89 ("Registry 784 → 797
  rows (S861–S873 …)"). `LOG.md:4260` still says the guard is "re-proven at the 783-row registry".
- No live harm: item-10 adoption is CLOSED and nothing is renumbered this round.

Fix: set `collisions` to the 15 staged ids, and replace the `S861→S992` citations in lesson/LOG/quarantine
footer with the regenerated span (or a "map regenerated at 27db4ce; see file" pointer).

Wave-2 seat `RevCounterC` filed the same staleness as its **F8** (`.ufo/waves/round-71/w2/RevCounterC.md:90-93`)
against the pre-repair map; this seat re-derived the numbers independently and records the post-repair residue.

### F2 — LOW — receipt stamps lag the landed revision

```
$ grep -H 'stamped revision' reports/round-71/telemetry/measures-{c,ca,d}.txt
measures-c.txt  : 64da9e1…
measures-ca.txt : 64da9e1…
measures-d.txt  : 1d1b432…
$ git rev-parse HEAD   -> 27db4ce…
```

HEAD carries entry edits after the C/Ca stamp (`2eb0183` wording, `e1d0d44` S861 ¶2 wording) and receipt-header
edits at `f5c845b`/`57e0a72`, and D's receipt was never re-stamped past the records commit although `7179d6d`
is titled "re-stamp C/Ca receipts at final HEAD". No graded leg is affected — the post-stamp entry edits change
prose and an anchor, not the cited S-id set, and all three counters PASS at 27db4ce — but "evaluated revision"
in the receipts is not the landed revision.

### F3 — LOW — commit-level claim mixing (files stay single-claim)

Files are exclusive, but two landed commits bundle claims, so the claims are not independently revertible:

- `1d1b432` ("records — Ca repairs …") also adds **D's** `reports/round-71/accept-d.py` and **C's**
  `reports/round-71/telemetry/census-end.txt`.
- `3764c2d` adds **Ca's** `measures-ca.txt` and **D's** `measures-d.txt` in one commit.
- `57e0a72` (Ca-side: quarantine re-derivation + `accept-ca.py` class leg) also re-stamps **C's**
  `reports/round-71/telemetry/measures-c.txt`.
- Post-filing hardening commits `75d1675` (C entry + README, Ca `accept-ca.py` + lesson, C `census-end.txt`)
  and `64da9e1` (C `SOURCES.md` S861, Ca lesson + `controls-d.txt`) write both claims' files in one commit.
  (`edd7895` touches `accept-c.py` only; `2eb0183` and `e1d0d44` touch the entry only — C-only.)

Reverting "the Ca commit" would delete D's counter and C's census receipt. No same-file write; provenance only.

### F4 — LOW — C's README landing is not append-only

`git diff b94a543..HEAD -- corpus/README.md | grep -cE '^-$'` → **3**: three blank lines unrelated to the
landing are deleted (before `## myth-symbol/`, `## culture-material/`, `## civilizations/`). `claims.json`
claim C's NOHARM sweep describes the README change as "appends". Content is correct (entry row verbatim,
header 34→36, totals 242→243, footer 243/30/29/36/29/24/95); the description is what overstates.

### F5 — INFO — C's Gate evidence lives in Ca's file (one-directional dependency)

C's predicate requires each cited row's quote to be "quoted in the round lesson Gate"; the 13 Gate rows sit in
`corpus/lessons/round-71.md`, which is Ca's surface (single writer, so no segment collision). The dependency is
one-directional: `accept-ca.py` reads SOURCES.md only for the S860 line and never needs C's rows. No cycle, but
C's claim is not self-contained: an edit to Ca's lesson changes C's evidence.

### F6 — INFO (already self-recorded) — D's no-git predicate is broader than the guard

```
$ mkdir -p /tmp/sep71/nestroot && cd /tmp/sep71/nestroot && git init -q . \
    && git -c user.email=t@t -c user.name=t commit -q --allow-empty -m init
$ mkdir copy && tar --exclude=.git -C <lane> -cf - . | tar -C copy -xf -
$ cd copy && python3 -B reports/round-71/accept-d.py --selftest
DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)
SELFTEST: 1/2            exit 1
```

A `.git`-less copy *nested inside another git work tree* still false-reds, because `_git_available()` only asks
`rev-parse --is-inside-work-tree`. The claim's wording ("in a .git-less copy of the tree prints
COULD-NOT-EVALUATE and exits 2") is true only for a copy outside any work tree. The lesson already records this
as its `guard-gap` Mistake row; noted here so the predicate wording is not read as universal.

### F7 — INFO — Ca's declared shell counting command is not the counter that produced the receipt

`claims.json` Ca `counting_command`'s last leg
`awk -F'|' '$1 ~ /S[0-9]+/ && $2 ~ /^(PRESENT|REFUSED|UNVERIFIABLE)$/' reports/round-71/telemetry/quarantine-verdicts.md`
prints **0** (markdown rows begin with `|`, so the id lands in field 2). The receipt's result block is an earlier
`accept-ca.py` output, not the output of the declared one-liner. The lesson records this as its
`declared-counter defect` row. Separation is unaffected — the declared command still cannot pass by reading C's
bytes.

### F8 — MEDIUM — the re-stamped Ca receipt has no current result; its only result line is stale

`57e0a72` ("append-only receipt re-stamps") prepends an eight-line header block plus the marker to
`reports/round-71/telemetry/measures-ca.txt` and appends **no new output**:

```
$ git show 57e0a72 -- reports/round-71/telemetry/measures-ca.txt | grep -cE '^\+[^+]'
8            # six header lines + re-stamp line + marker — header only, no result output
$ grep -nE 'ACCEPT-CA|QUARANTINE' reports/round-71/telemetry/measures-ca.txt
16:ACCEPT-CA-71: PASS
22:QUARANTINE: rows=21 unique=21 labels-ok (PRESENT 10 / REFUSED 6 / UNVERIFIABLE 5)   <- preserved body
$ python3 -B reports/round-71/accept-ca.py | tail -2
     rows=21 unique-ids=21 labels-ok=True class-ok=True (want 21/21/True/True)
ACCEPT-CA-71: PASS
```

So the committed receipt (a) carries no output for the current counter/tree (the `class-ok` leg never appears)
and (b) states the pre-`57e0a72` tally `10 / 6 / 5` where the landed table and the live counter give
`10 / 7 / 4`. The green control ("the counting command is run … and its output is committed as the receipt")
is not met by a header-only prepend. `measures-c.txt` has the same header-only shape, but its preserved body
still matches the live output (counter and measured revision unchanged), so only Ca's receipt is materially
stale. No separation impact: the file belongs to Ca alone.

Still true at 27db4ce: `git show 27db4ce -- reports/round-71/telemetry/measures-ca.txt | grep -cE '^\+[^+]'`
→ **0** (the commit lists the path but changes nothing), so the stale body remains the receipt's only result.

## Residual risk

1. **Registry-tail adjacency.** C's rows start one line after the line Ca rewrites. Any future rebase, reorder,
   or re-append that moves the S860 anchor re-couples the two claims; the mutual diff-context dependency means
   the order C→Ca must be preserved if either patch is ever replayed.
2. **Item-10 map.** The map itself is now correct for adoption (`next_free S874`, span `S874→S1005`); the
   residue is its understated `collisions` list and the stale `S861→S992` citations in the lesson, LOG and
   quarantine footer (F1).
3. **Moving tree.** The lane landed six commits during this seat. All verdicts are stamped 27db4ce; a later
   commit touching `corpus/SOURCES.md`, the entry, the lesson, a counter, the map, or the quarantine table
   requires re-running the two isolation commands above.

## Verification gaps

- The 13 source URLs were not re-fetched (claim C's quote fidelity is `RevEntry`/`RevRows` scope). I verified
  citation structure: row exists, status `mined`, `used-by` names the entry, `used-by` path exists,
  `tools/check-cited-lines.py` exit 0, `accept-c.py` PASS.
- Round-70 receipt "original bytes preserved below the marker" was checked for marker presence and first-line
  shape, not full byte equality against the pre-round-71 blob.
- `acc2d614` was verified for the S860 blob; its tree was not rebuilt.
- No web/GitHub access was needed; no tool was installed (pacman paused, nothing attempted).
