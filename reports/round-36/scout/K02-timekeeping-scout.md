- Seat: K02 | scout | claim C | date 2026-10-19 | baseline ce103bf

# K02 — timekeeping scout: the spare's gap statement and couples re-measured against the CURRENT tree (post-r35), and the README delta the landing needs

Mission: re-verify the routed spare's gap statement and its `couples:` against the
tree as it stands **after** round 35, and specify what the README delta needs
(+1 culture-material row, totals 212, rev 2.1). This seat wrote no corpus byte and
ran no filed round runner. Every reading below is a command run 2026-10-19 from
the lane root at HEAD `ce103bf5885af00023cdc4a174c17602476cdcf8`, with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

## 0. The artifact under audit, pinned

| item | value |
|---|---|
| spare fragment | `reports/round-35/cov/C04-timekeeping-spare.md`, sha256 `258fb166e35f3b0f92854dcb7c5e08fcfc285c51a42aa828cb79f3f761f5bcd2` |
| fenced entry bytes | 40 234 B / 140 lines, sha256 `9805c0b854334ed396119476b6278cc4f58eb1014a0b06eb6bba561def05f0a6` (with trailing newline) |
| intended slug | `timekeeping-instruments.md` (the fragment's own preamble names the target; the fenced block carries no path) |
| entry digest cross-check | R01 recorded the same entry digest `9805c0b854334ed3…` and the same size (141 lines / 40 234 B) at `reports/round-35/review/R01-c-review.md:159` — the bytes this scout measures are the bytes R01 passed clean, unmodified |
| r35 review verdict on the entry | `reports/round-35/review/R01-c-review.md:25` — "gap ✓ decision ✓ pointers 0-unresolved couples 0-unresolved | **pass clean** (§3.4)" |

The spare's fenced block is the **same** entry C04 offered as its secondary draft
(`reports/round-35/cov/C04-entry-4.md`, "Secondary draft (offered, not claimed)");
C04's PRIMARY was `bathing-and-body-hygiene`, which landed. The timekeeping bytes
were never landed. This scout confirms that state and measures what landing them
now would cost.

## 1. Finding K02-F1 (load-bearing) — the spare's gap statement is STALE in five measured places

The spare's `- gap filled:` line (`reports/round-35/cov/C04-timekeeping-spare.md:13`)
asserts a sweep taken at HEAD `4a7aede`, i.e. **before the round-35 wave landed**.
Re-running its own commands over the current 211-file tree:

| spare's claim (`:13`) | re-measured 2026-10-19 at `ce103bf` | delta |
|---|---|---|
| `(201 files at HEAD 4a7aede)` | **211 files** | stale corpus size |
| the 28-term instrument sweep → "**0 for every term**" | 27 of 28 terms still 0; **`curfew` → 1 file** (`corpus/knowledge/culture-material/fire-fuel-light.md`) | the "0 for every term" sentence is now **false** |
| `` `astrolabe` 2 files `` | **2** — unchanged, both still incidental (`civilizations/persia-sasanian.md:98`; `culture-material/transport-mobility-lexicon.md:18`) | matches |
| `` `"star clock"` 2 `` | **2** — unchanged (`myth-symbol/animal-symbolism.md:79`; `myth-symbol/celestial-symbolism-calendars.md:83`) | matches |
| `` `chronometer` 2 `` | **4** | stale |
| `` `obelisk` 1 / `meridian` 1 / `"time zone"` 1 `` | **1 / 1 / 1** | matches |
| `` `hour` 8 files `` | **17** | stale |
| `` `bell` 81 files `` | **87** | stale |
| `` `clock` 6 files inside culture-material `` | **10** | stale |
| "the night-watch institution appears once in the corpus (`grep -ril "night watch"` → 1 file)" (§5 table) | **2 files** (`culture-material/fire-fuel-light.md`; `myth-symbol/ritual-liminality.md`) | stale |

Reproduction commands (lane root, 2026-10-19, HEAD `ce103bf`):

```sh
# the spare's own 28-term sweep, re-run verbatim
for kw in "water clock" clepsydra clepsammia gnomon sundial escapement pendulum hourglass \
  "incense clock" curfew "bell tower" "canonical hour" clockmaker muwaqqit wadokei shichen \
  "toki no kane" horologium foliot quadrant sandglass "candle clock" "night clock" \
  "standard time" "railway time" vigilia; do
  printf "%-20s %s\n" "$kw" "$(grep -ril -- "$kw" corpus/knowledge/*/*.md | wc -l)"; done
# -> curfew 1, every other term 0

# the near-miss vector, re-run verbatim
for kw in astrolabe "star clock" chronometer obelisk meridian "time zone" hour bell; do
  printf "%-14s %s\n" "$kw" "$(grep -ril -- "$kw" corpus/knowledge/*/*.md | wc -l)"; done
# -> 2 2 4 1 1 1 17 87

grep -ril "night watch" corpus/knowledge/*/*.md | wc -l      # -> 2
grep -ril "clock" corpus/knowledge/culture-material/*.md | wc -l   # -> 10
for p in linguistics myth-symbol culture-material synthesis verification civilizations; do
  ls corpus/knowledge/$p/*.md | wc -l; done                  # -> 21 23 24 29 20 94
```

**Why the deltas moved.** Every drift traces to the ten round-35 entries:
`fire-fuel-light.md` introduces `curfew` (13 mentions), `night watch`, and
`watch and ward` into the partition; the six new culture-material entries take the
`clock`-in-culture-material count 6 → 10; `hour` rises with the new entries' own
topic lines; `bell` rises with the four new myth-symbol entries.

**Disposition.** The *domain claim* survives — no entry in the corpus owns the
**instrument** (all 28 instrument terms remain 0 except the single `curfew`
institution-word, and no file owns a sundial, clepsydra, escapement, gnomon,
astrolabe-as-instrument, or clock-as-device). What fails is the **sweep receipt**:
its corpus size, its "0 for every term" sentence, its `hour`/`bell`/`chronometer`
near-miss counts, and its night-watch count. Landing the fenced bytes unedited
would write a present-tense false measurement into the corpus — the same defect
class as the round-28 counts-footer case (`corpus/README.md:30-49`,
`corpus/lessons/round-28.md:80`: "A green over a stale claim is the false-green
class one level up, and the fix was to widen the instrument, not to restate the
number"). **The gap line must be re-measured, not arithmetic-adjusted** — the
rule the round-19 lesson states at `corpus/lessons/round-19.md:115`.

## 2. Finding K02-F2 (load-bearing) — the spare's `couples:` predates the wave and MISSES a landed sibling that owns the same surface

The spare's `- couples:` line names **24** `corpus/knowledge/…` paths. All 24
resolve at `ce103bf` (0 unresolved — confirming R01's "couples 0-unresolved" at
`reports/round-35/review/R01-c-review.md:25`). But **none of the 24 is any of the
ten round-35 entries**:

```
r35 entries named in the spare's couples: []  (0 of 10)
```

The load-bearing one is `corpus/knowledge/culture-material/fire-fuel-light.md`
(sha256 `481cf1c24734c1251879f3e2928fb9d470db7eae11a375982786602ed74c6558`), which
landed in round 35 and **owns the night-watch / curfew / risk-apparatus surface
the spare also claims**:

| term | spare entry | `fire-fuel-light.md` |
|---|---|---|
| `curfew` | 14 | **13** |
| `night watch` | 4 | 2 |
| `vigiles` | 0 | **4** |
| `watch and ward` | 0 | 2 |
| `lamplighter` | 0 | **7** |
| `hearth` | 1 | **53** |
| `lamp` | 5 | **50** |
| `fire mark` | 0 | 9 |
| `insurance` | 0 | 5 |

Shared 5+ character content terms: 421; Jaccard **0.211** — nearly double the
0.118 topic-Jaccard at which R01 passed the spare against the then-201-file
baseline (`reports/round-35/review/R01-c-review.md:181`). The overlap is not
topic-level (topic Jaccard vs the current tree peaks at 0.120, see §4) but
**section-level**: both entries write the curfew, the night watch, and the watch
institution.

The two entries are not duplicates — `fire-fuel-light.md:4` frames itself as the
**fire** system and puts the curfew in it as "a fire ordinance that became a time
ordinance" (`:82`), while the spare frames the same word as a time institution.
But the spare's own §5 table presents curfew, night watch and the risk apparatus
as **its** institutions, and its `- couples:` names no fire entry, so a reader of
the landed spare would have no pointer to the sibling that already carries the
fire side. `fire-fuel-light.md` in turn names no timekeeping entry (it could not:
the spare is unlanded).

**Disposition (routed, not absorbed).** Landing the spare without amending its
`couples:` would ship a second entry writing the same institution with no
boundary statement between them — the adjacency defect the lane's own rule
forbids (AGENTS.md: "reports contested scope instead of absorbing it"). The
minimum repair is a **boundary clause** in the spare's `- couples:` and §5: the
fire entry owns the *fire ordinance and its risk apparatus*; the time entry owns
the *instrument, its resolution, and the institution that publishes the hour*.
Whether that repair is authored in round 36 or the spare is held is the
integrator's decision — this scout records the finding and its measurement, and
does not decide it.

## 3. What the README delta needs — measured, and simulation-verified

Live state at `ce103bf`: README sha256
`51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`, 523 lines,
revision **2.0**. The round-28 instrument reads it clean:

```sh
python3 -B reports/round-28/readme/sweep.py
# parts {"civilizations": 94, "culture-material": 24, "linguistics": 21,
#        "myth-symbol": 23, "synthesis": 29, "verification": 20}
# rows 211 files 211 ; missing_from_index 0 ; topic_mismatch 0 ; orphan_rows 0
# header_drift {} ; totals_line 211 totals_ok True ; footer_ok True ; exit 0
python3 -B reports/round-28/readme/sweep.py --selftest   # 12/12 checks passed
```

Instrument digest `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`.
The next revision value is **2.1** by the file's own 0.1-step convention
(`1.4→…→1.9→2.0` at `corpus/README.md:3,30,50,62,82,108,118`), matching C02's
declared target (`reports/round-36/targets.json`, seat C02).

### 3.1 Row anchor (measured, not guessed)

`timekeeping-instruments.md` sorts between `textile-technology.md` and
`trade-economy-lexicon.md`:

```sh
python3 -c "
import os
n=sorted(os.listdir('corpus/knowledge/culture-material'))
m=sorted([x for x in n if x.endswith('.md')]+['timekeeping-instruments.md'])
i=m.index('timekeeping-instruments.md'); print(m[i-1],'<',m[i],'<',m[i+1])"
# -> textile-technology.md < timekeeping-instruments.md < trade-economy-lexicon.md
```

In the pinned README those rows are **line 206** (`textile-technology.md`) and
**line 207** (`trade-economy-lexicon.md`). The new row therefore inserts **after
line 206**. Its bytes are the entry's own continuation-joined `- topic:` text
(1 696 chars), which the instrument requires byte-equal
(`reports/round-28/readme/sweep.py:21,22,74-79,140`, control
`continuation lines space-joined` at `:398-401`). Total row length
1 729 B.

### 3.2 The six edit families

| # | surface | line (pinned) | before | after |
|---|---|---|---|---|
| E1 | newest revision block | after **2**, before **3** | — | new `revision: 2.1 — …` block |
| E2 | culture-material header | **186** | `## culture-material/ (24)` | `## culture-material/ (25)` |
| E3 | index row | after **206** | — | `- \`timekeeping-instruments.md\` — <entry's own \`- topic:\` text>` |
| E4 | totals line | **492** | `Total knowledge entries: 211.` | `Total knowledge entries: 212.` |
| E5a | footer vector | **496** | `(total 211 files; directory totals 21/23/24/29/20/94).` | `(total 212 files; directory totals 21/23/25/29/20/94).` |
| E5b | superseded-reading paragraph | after **505** | ends "…with the ten round-35 entries." | append a `Revision 2.1 moved …` sentence |
| E6 | dated index paragraph | after **523** | — | new `Index rows re-measured 2026-10-19 …` paragraph |

Unchanged: line **494** `Counts checked 2026-10-19 …` (the date is already today's),
line **495** (the inventory command), line **497** (`The inventory counts markers…`),
and the 199/19 superseded record at **498-503** (append-only per the file's own rule
and `corpus/lessons/round-19.md:115`).

Deliberately **not** in the delta: a new `## Known gaps (frontier)` bullet. C11 made
the same call (`reports/round-35/cov/C11-readme-delta.md`, "Deliberately **not** in
this delta"); revisions 1.7–2.0 added none. If the integrator wants one it is an
addition to route, not a reconciliation gap.

### 3.3 Simulation — the delta measured end-to-end, repo bytes untouched

This seat built an isolated tree under `.scratch/k02-iso/` (a copy of
`corpus/knowledge`, the spare's fenced block written as
`culture-material/timekeeping-instruments.md`, and a reconciled README copy) and ran
a **root-redirected copy** of the round-28 instrument against it. No repo byte was
written; no filed runner was executed.

```
parts {"civilizations": 94, "culture-material": 25, "linguistics": 21,
       "myth-symbol": 23, "synthesis": 29, "verification": 20}
rows 212 files 212 ; missing_from_index 0 ; topic_mismatch 0 ; orphan_rows 0
header_drift {} ; totals_line 212 totals_ok True ; footer_ok True ; exit 0
footer {"date":"2026-10-19","total":212,"dir_totals":[21,23,25,29,20,94]}
readme_sha256 8e820cfdee3e887f35dc7a06db84007631e958aaa9633c56e2eabe8abc46a564
```

Lane inventory over the isolated tree:
`python3 -B tools/source-audit-inventory.py --json --summary --root .scratch/k02-iso/knowledge`
→ `totals.files 212`.

Three negative controls, all fire (exit 1) as designed:

| control | reading |
|---|---|
| header reverted to `(24)` | `header_drift {'culture-material': {'declared': 24, 'files': 25}}`, exit 1 |
| the new row deleted | `missing_from_index 1 ['culture-material/timekeeping-instruments.md']`, exit 1 |
| the new row paraphrased | `topic_mismatch 1 ['culture-material/timekeeping-instruments.md']`, exit 1 |

**The delta is sound and the instrument detects its failure modes.** The simulation
also proves the entry's own `- topic:` bytes satisfy the equality leg without
hand-editing, which is the round-19/20 defect the delta must not repeat.

### 3.4 Entry-level checks against the round-10 C legs

Replicated (read-only, **not** by executing the filed runner) from
`reports/round-10/run-validation.py:81-82,349-377` against the isolated entry:

| leg | reading |
|---|---|
| frontmatter `topic / sources / verified-at / recheck / couples` | **5/5 present** (the entry also carries `source`, `scope`, and `- gap filled:`) |
| gap named | **true** (`- gap filled:` matches the leg's regex) |
| decision-record section | **true** — `## 9. Decision record — the timekeeping decisions this entry fixes` |
| retrievable locators | **28** resolving `corpus/…` paths (0 URLs) |
| `couples:` refs | **24**, 0 unresolved |
| `path:line` citations | **8**, all in-bounds |
| DR rows | **12** (`DR-TK-1` … `DR-TK-12`) |
| sections | 11 (`## 1.` … `## 11.`) |

## 4. Duplication re-check against the post-r35 tree

Topic-Jaccard of the spare's `- topic:` text against all 211 current entries:

| rank | Jaccard | file |
|---|---|---|
| 1 | 0.120 | `myth-symbol/divination-omen-systems.md` |
| 2 | 0.112 | `culture-material/writing-media-surface-economy.md` |
| 3 | 0.111 | `culture-material/furniture-interior-lexicon.md` |
| 4 | 0.106 | `myth-symbol/binding-speech-complex.md` |
| 5 | 0.102 | `myth-symbol/eschatology-world-end-systems.md` |

Peak 0.120 vs the 0.118 R01 recorded against the 201-file baseline
(`reports/round-35/review/R01-c-review.md:181`) — the topic-level separation
survives the wave. The risk is **not** topic-level; it is the §2 section-level
overlap with `fire-fuel-light.md`. Note that two of the top five are round-35
entries the spare has never been compared against before this scout.

## 5. Count surfaces the landing moves — and the ones that must NOT be edited

Live surfaces carrying the count:

| surface | state | action |
|---|---|---|
| `corpus/README.md:492,496` | 211 / `21/23/24/29/20/94` | E4/E5a above |
| `corpus/README.md:504-505` | rev 2.0 prose | E5b append |
| `reports/round-35/run-validation.py:28` (`EXPECTED_COUNTS`), `:160` (`!= 211`), `:168` (needle list) | hardcode 211 / CM 24 | **FILED round-35 bytes — must NOT be edited**; round 36 needs its own 212 expectations |
| `SCORECARD.md:640` | r35 coverage row reading 211 | filed row; round 36 appends a new row, never edits this one |
| `LOG.md` | append-only, parent-owned | not a seat surface |

Exactly one file in the live tree carries a literal `^Total knowledge entries: `
line — `corpus/README.md:492` (`grep -rln '^Total knowledge entries: ' --include=*.md .`
outside `.scratch`). The phrase appears as quoted prose inside filed records
(`corpus/lessons/round-{19,20,27,28}.md`, `reports/round-10/**`, `reports/round-27/**`,
`reports/round-28/**`); those are dated readings, not count surfaces, and take no edit.

**The r7 freeze is not disturbed by this delta.** `corpus/README.md` appears in no
read-set member (`grep -c "corpus/README" reports/round-34/handoff/declared-in-r7/*`
→ 0 for `claims-map.md`, `packet.md`, `expected.json`, `twin.json`), and the only
`corpus/knowledge` path in the r7 artifact manifest is
`corpus/knowledge/synthesis/worldbible-integration-contract.md`
(`reports/round-34/handoff/declared-in-r7/twin.json`, artifact `A-01`) — untouched by
this landing. The freeze read set is 58 files / 26 component digests
(`reports/round-34/handoff/declared-in-r7/freeze.txt`); a new
`culture-material/timekeeping-instruments.md` is not a member. **No re-freeze of
`declared-in-r7` is implied or performed.**

## 6. Cross-seat reconciliation — two peers landed after this seat started, and they corroborate §1 and §2

Peers wrote into `reports/round-36/` while this seat worked; their readings were
re-checked against the commands in §1–§2 and they **agree** on both load-bearing
findings:

- `reports/round-36/cov/C03-verify.md:136-143` — the 28-term sweep re-run returns
  0 for 26 of 27 terms with **`curfew` → 1**; it concludes the spare's gap statement
  is "accurate as written *at its own baseline*" and that the `curfew` hit is "a new
  landing". Same disposition as §1.
- `reports/round-36/cov/C03-verify.md:143-160` — the couples drift: the spare's
  sibling set "is now one landing stale", and the closest new sibling is
  `culture-material/fire-fuel-light.md`, carrying the `curfew`/`couvre-feu` etymology,
  the "light is bought by the hour" claim, the risk-word row, and the explicit
  "is the curfew a fire rule or a time rule" build step — i.e. the same collision
  §2 measures. Same disposition.
- `reports/round-36/cov/C01-audit.md:181-185` — `curfew` → 1 file, identified as
  `fire-fuel-light.md`, with `git grep -ril -- "curfew" 4a7aede` → no match.
- `reports/round-36/cov/C01-audit.md:258-262` — an additional defect this scout did
  **not** find: **F1**, the round-35 runbook's stager resolves the spare's landing
  target to `culture-material/calendar-festival-systems.md` (an existing filed entry,
  the first `corpus/knowledge/<partition>/<slug>.md` token in the text — a `couples:`
  target), because the spare names no explicit target path (C01's F5). **This is a
  second, independent reason the spare cannot be landed mechanically:** any stager
  must be given the slug explicitly. This scout confirms the precondition C01 states
  (the fenced block carries no path — §0) and routes the stager repair to the
  integrator, since the runbook is filed bytes.
- `reports/round-36/cov/C01-audit.md:232-236` and
  `reports/round-36/cov/C03-verify.md:69-76` — the README delta matches §3.2 exactly:
  totals `211.` → `212.`, footer vector → `21/23/25/29/20/94`, "moves **exactly one**
  element", rev 2.1. No disagreement with E4/E5a.

### 6.1 One countable disagreement, filed rather than smoothed

Three seats count the spare's `couples:` differently on the **same** artifact:

| seat | reading | where |
|---|---|---|
| this scout | **24** unique `corpus/knowledge/…` paths in the `- couples:` line | §2 above |
| C01 | `couples 25/25` | `reports/round-36/cov/C01-audit.md:111,218` |
| C03 | "names **20** corpus siblings" / "**31** distinct `corpus/knowledge/**` paths with line anchors" | `reports/round-36/cov/C03-verify.md:117,145` |

This seat measured six plausible methods over the entry bytes and **none reproduces
25 or 31**:

| method | reading |
|---|---|
| `- couples:` line, `corpus/knowledge/`-prefixed, unique | **24** |
| `- couples:` line, prefixed + bare `partition/slug.md`, unique | 24 |
| whole entry, prefixed, unique | 27 |
| whole entry, prefixed + bare `partition/slug.md`, unique | 28 |
| whole entry, prefixed, **occurrences** | 46 |
| whole entry, all `*.md` tokens, unique / occurrences | 45 / 77 |

So C03's 31 is not reproducible from the entry text under any method tried, and
C01's 25 differs from the couples-line count by one. The three seats may be counting
different scopes (couples line vs whole entry; unique vs occurrence; bare vs
prefixed), and C03 itself reports two different numbers for its own artifact (20 and
31). **Disposition: the count is `unprovable-as-stated` for the peers and 24 for this
seat, with the method named.** This scout does not declare the peers wrong — it
records the disagreement, its method, and the command, so the integrator can settle
it rather than average it. It does not change either finding: 0 unresolved under
every method tried.

## 7. What this scout does not decide

- It does not land, admit, or clear anything; it writes no corpus byte and no README byte.
- It does not decide whether the spare lands in round 36 or is held; it records the
  two blocking findings (K02-F1 stale receipt, K02-F2 unamended couples collision)
  and the measured delta.
- It does not author the revision-2.1 prose, the boundary clause, or the row bytes;
  those belong to the C block (C01/C02/C03) and the integrator.
- It does not re-verify the entry's external sources. R01 records 33 `to-verify`
  occurrences / 23 lines and one unresolved DOI marked in-line
  (`reports/round-35/review/R01-c-review.md:159`, §3.4); no network exists in this
  run, so nothing here changes that status. **Every external date, precision figure
  and etymology in the entry remains `to-verify`.**

## Owed

- `reports/round-36/cov/C01-audit.md` — the first independent audit of the spare
  against the round-35 runbook. **Landed during this seat's run** (read and reconciled
  in §6); its F1 stager defect and F5 missing-target finding are routed to the
  integrator.
- `reports/round-36/cov/C02-audit-delta.md` — the second audit plus the README delta
  draft (rev 2.1). **Absent at this seat's close** (`reports/round-36/cov/` held
  `C01-audit.md`, `C03-verify.md`); owed by C02. This scout supplies the delta
  measurements (§3) that C02's draft needs.
- `reports/round-36/cov/C03-verify.md` — independent verification of both audits and
  the delta numbers. **Landed during this seat's run** (read and reconciled in §6);
  its couples count disagrees with this seat's and is filed as `unprovable-as-stated`
  in §6.1.
- The **re-measured** replacement for the spare's `- gap filled:` line (stale counts
  per §1) and the `couples:` boundary clause vs `fire-fuel-light.md` (per §2) —
  authored bytes, owed to whoever lands the entry. This scout supplies the readings;
  it does not write the prose.
- The **stager repair** (C01's F1): a landing of this spare must be given the slug
  explicitly, since the runbook's stager resolves it to an existing filed entry.
  Owed to the integrator (the runbook is filed bytes).
- A **settlement of the three-way couples count** (24 / 25 / 31 per §6.1), owed to
  the integrator; this seat records its own method and does not declare the peers wrong.

## Citations

- `reports/round-36/cov/C01-audit.md:111,181-185,218,232-236,258-262` — peer audit:
  `couples 25/25`, `curfew` → 1 (`fire-fuel-light.md`, 0 at `4a7aede`), the README
  delta, and its F1 stager / F5 missing-target defects (read after this seat started;
  reconciled in §6)
- `reports/round-36/cov/C03-verify.md:69-76,113-117,136-160` — peer verification: the
  same `curfew` finding, the "sibling set one landing stale" couples drift, the
  one-element footer move, and the 20/31 couples readings filed in §6.1
- `reports/round-35/cov/C04-timekeeping-spare.md:12,13,14,18` — the entry's topic,
  **stale gap line**, sources, recheck; fragment sha256 `258fb166e35f3b0f…`, fenced
  entry sha256 `9805c0b854334ed3…` (40 234 B / 140 lines)
- `reports/round-35/cov/C04-entry-4.md` — the same bytes offered as C04's secondary
  draft; PRIMARY `bathing-and-body-hygiene` landed, timekeeping did not
- `reports/round-35/review/R01-c-review.md:25,159,181` — R01's pass-clean verdict,
  the matching entry digest, and the 0.118 baseline Jaccard
- `reports/round-35/plan/P01-c-plan.md:526-541` — held alternates with evidence,
  `timekeeping-instruments` among them, and the swap rule
- `corpus/README.md:3,186,206,207,492,494,496,504-505,520-523` — revision 2.0,
  CM header, the two anchor rows, totals line, footer, superseded-reading paragraph,
  the r35 index re-measure; pinned sha256 `51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`
- `reports/round-28/readme/sweep.py:21,22,74-79,140,398-401` — the row/topic equality
  contract and its continuation control; instrument sha256 `9b2ccac0046831fd…`
- `corpus/knowledge/culture-material/fire-fuel-light.md:3,4,17,27,81,82,112,141-147`
  — the landed sibling: its gap line, topic, couples, curfew-as-fire-ordinance,
  night watch, risk vocabulary, DR-FF-01..07; sha256 `481cf1c24734c125…`
- `reports/round-34/handoff/declared-in-r7/freeze.txt` — read set 58 files,
  component digests 26/26, packet/twin digests; `twin.json` artifact `A-01`
  (`corpus/knowledge/synthesis/worldbible-integration-contract.md`)
- `reports/round-10/run-validation.py:81-82,349-377` — the C-leg frontmatter/gap/
  decision/locator checks, replicated read-only
- `reports/round-35/run-validation.py:28,160,168` — the hardcoded 211 / CM 24 that
  **round 36 must not edit** (filed bytes)
- `corpus/lessons/round-19.md:115` — "must re-measure, not arithmetic-guess … append
  a new dated block"
- `corpus/lessons/round-28.md:80`, `corpus/README.md:30-49` — the false-green class
  and the footer defect precedent
- `corpus/knowledge/civilizations/persia-sasanian.md:98`,
  `corpus/knowledge/culture-material/transport-mobility-lexicon.md:18` — the two
  `astrolabe` near-misses, re-read and still incidental
- `corpus/knowledge/myth-symbol/animal-symbolism.md:79`,
  `corpus/knowledge/myth-symbol/celestial-symbolism-calendars.md:83` — the two
  `star clock` near-misses, still calendar apparatus
- `corpus/knowledge/linguistics/numerals-and-measures.md:135`,
  `corpus/knowledge/civilizations/aksum-ethiopia.md:98-114` — the spare's two
  in-corpus precedent citations, re-read and accurate
- Commands run (lane root, 2026-10-19, HEAD `ce103bf5885af00023cdc4a174c17602476cdcf8`,
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  - the spare's 28-term sweep re-run → `curfew 1`, all others 0
  - the near-miss vector re-run → `2 2 4 1 1 1 17 87`
  - `grep -ril "night watch" corpus/knowledge/*/*.md | wc -l` → 2
  - `grep -ril "clock" corpus/knowledge/culture-material/*.md | wc -l` → 10
  - partition census → `21 23 24 29 20 94` (total 211)
  - `python3 -B reports/round-28/readme/sweep.py` → 211/211, all legs green, exit 0
  - `python3 -B reports/round-28/readme/sweep.py --selftest` → 12/12
  - `python3 -B .scratch/k02-iso/sweep-iso.py` (root-redirected copy) → 212/212, exit 0
  - `python3 -B .scratch/k02-iso/sweep-iso.py --readme …/README.neg{1,2,3}.md` → exit 1 ×3
  - `python3 -B tools/source-audit-inventory.py --json --summary --root .scratch/k02-iso/knowledge`
    → `totals.files 212`
  - couples/line-cite/Jaccard/DR-row checks (scripted, read-only)
- Scratch (disposable, not evidence): `.scratch/k02-iso/{knowledge,README.md,sweep-iso.py,README.neg*.md}`
