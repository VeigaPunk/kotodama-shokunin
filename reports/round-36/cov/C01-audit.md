- Seat: C01 | executor | claim C | date 2026-10-19 | baseline ce103bf

# C01 — audit of the round-35 timekeeping spare (claim C / coverage)

- Round 36, seat **C01**, role **executor**, claim **C**. Mission (verbatim,
  `reports/round-36/targets.json` → `seats[id=C01].mission`): *"Audit the
  timekeeping spare draft against the round-35 runbook (two independent reads;
  defects filed)."* Out path: `reports/round-36/cov/C01-audit.md`.
- Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  `git rev-parse HEAD` → `ce103bf5885af00023cdc4a174c17602476cdcf8`;
  `git status --porcelain` → `?? reports/round-36/` (no corpus byte moved by this seat).
- **Canon: NON-CANON.** This seat audits bytes and reports; it admits no entry,
  certifies no round, promotes nothing, and is not promotion verification. A green
  reading below is a structural reading of the bytes at a named digest — never a
  verdict on the scholarship, never canon (`PROVINCE.md`).
- **Writes**: this file only, plus gitignored scratch under `.scratch/c01/`. No
  `corpus/**`, no `tools/**`, no filed round-1..35 byte, no `.ufo/**`. No commit,
  no push, no install, no network.
- **F-C13-1 / freeze rule honoured**: no `reports/round-*/run-validation.py` was
  executed anywhere, in-tree or in a copy; no `--freeze` of
  `reports/round-34/handoff/declared-in-r7` was run. The only filed code executed
  is the read-only `reports/round-28/readme/sweep.py`, run from an isolated
  `git archive` copy (§5).

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | the spare **is not landed**; `corpus/knowledge/culture-material/timekeeping-instruments.md` does not exist | measured |
| 2 | the spare **passes the structural contract on two independent instruments** (I-C12 `PASS/review`; I-C14 `bar_pass true`); its one review item is a **false positive** | measured |
| 3 | **28/28 cited repo paths resolve; 0 unresolved; 20 attached `path:line` citations, 30 line numbers, 0 out-of-range** | measured |
| 4 | the spare's **quoted absence sweep reproduces exactly at the pinned authoring HEAD `4a7aede`**: all 26 quoted instrument terms → **0 files** | measured |
| 5 | the spare's **near-miss counts reproduce exactly at `4a7aede`**: astrolabe 2, star clock 2, chronometer 2, obelisk 1, meridian 1, time zone 1, bell 81, `hour -w` 8, clock-in-culture-material 6 | measured |
| 6 | **all quoted counts have drifted since** because round 35 landed the ten entries — every drifted term is a **landing-drift** reading, not an authoring error | §4 |
| 7 | **defects filed: F1 (stager mis-target, S2), F2 (`hour`-count reading note, S3), F3 (`28` vs `26` terms, S3), F4 (drift disclosure owed, S3), F5 (no declared target path, S3)** | §3 |
| 8 | **the spare is a legitimate held alternate** of the landed plan, not a duplicate of any live entry (0 near-duplicates at Jaccard > 0.30) | measured |
| 9 | a **transient in-tree re-run of a filed round runner** moved `reports/round-34/validation.json` to `acceptance: false` mid-run and it was **reverted to committed bytes** — filed bytes are intact; the *process* event is recorded, not repaired | §4b |

## 1. The audited bytes, and their provenance

| field | value |
|---|---|
| fragment | `reports/round-35/cov/C04-timekeeping-spare.md` |
| fragment sha256 | `258fb166e35f3b0f92854dcb7c5e08fcfc285c51a42aa828cb79f3f761f5bcd2` |
| fragment bytes / lines | 40 646 / 150 |
| fenced block | one, 3-backtick ` ```markdown ` open / ` ``` ` close; **no** 4-backtick fence |
| extracted entry bytes | **40 234** |
| extracted entry sha256 | `9805c0b854334ed396119476b6278cc4f58eb1014a0b06eb6bba561def05f0a6` |
| extracted entry sha256[:16] | `9805c0b854334ed3` |
| staged at | `.scratch/c01/stage/corpus/knowledge/culture-material/timekeeping-instruments.md` |
| entry title | `# Timekeeping Material Culture — the Instruments of the Hour: …` |
| declared status | `- ` header line 3 of the fragment: *"Timekeeping Material Culture (ALTERNATE DRAFT — NOT LANDED)"* |

**Provenance re-derived, not taken on trust.** The fragment is a *routed spare*
from round-35 seat C04: C04 drafted it per P01's held-alternates list and filed it
under `cov/C04-timekeeping-spare.md` because landing it would break the declared
10-entry / 211 counts. Two independent checks confirm the routing:

- **Not a copy of C04's landed entry.** `cov/C04-entry-4.md` carries two fenced
  entry blocks; block 0 (38 837 B, sha `15f2ea5de5bb9406…`) is the **bathing**
  entry that actually landed, block 1 (40 234 B, sha `9805c0b854334ed3…`) is the
  timekeeping spare verbatim. The two blocks are **not identical** (different
  titles, different partitions of content), so the spare is a genuine second draft,
  not an accidental re-fence of the landed bytes.
- **P01 landed and names it.** `reports/round-35/plan/P01-c-plan.md:91-93` records
  what the plan *drops from its own first draft* — "timekeeping-instruments,
  games-and-play, incense-aromatics, magic-and-witchcraft, sacred-kingship,
  bathing-hygiene" — "recorded in §7 as evidence-carrying alternates with swap
  rules, not deleted"; and `:529-531` gives the swap evidence
  (`sundial|gnomon|clepsydra|water clock|hourglass` → 0 files, 0 owners, with
  `calendar-festival-systems` named the partial owner of time machinery).
- **The landed corpus confirms the alternate status**: `test -e
  corpus/knowledge/culture-material/timekeeping-instruments.md` → **absent**;
  `ls corpus/knowledge/culture-material/*.md | grep -iE 'time|clock|hour'` → rc=1
  (no match). The landed C04 slot became `bathing-and-body-hygiene.md` instead.

## 2. The round-35 runbook check list, with observed results

"Two independent reads" is discharged by running **two instruments built by two
different seats**, each installed from its own filed bytes and digest-verified
before use. Their readings are reported separately, never merged.

- **I-C12** — the round-35 runbook instrument (`reports/round-35/cov/C12-audit-runbook.md`
  §5), installed by the runbook's own step-0 command
  `awk '/^```python$/{f=1;next} /^```$/{f=0} f'` →
  `.scratch/c01/c12-instrument.py`, sha256
  **`973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d`**, 663 lines
  — **byte-identical to the digest the runbook declares** (`:99,184`).
  `--selftest` → **exit 0**, "SELFTEST PASS: 3 positive controls … and 4 negative
  controls … behave".
- **I-C14** — the second independent auditor's instrument
  (`reports/round-35/cov/C14-audit-6-10.md` §2), installed the same way →
  `.scratch/c01/audit-v2.py`, sha256
  `3e255037cc70878d6707f908849173d08014839a5c5ae76c54609f52a2319fe2`, 370 lines.
  `--selftest` → **exit 0, 13/13 PASS**, four of them negative controls.

| runbook family (`cov/C12-audit-runbook.md:33-44`) | reading | observed on the staged spare |
|---|---|---|
| 1a | `R35-4F-1` frontmatter 4/4 (source\|sources, verified-at, recheck, couples\|scope) | **pass** (`4of4=True`) |
| 1b | `R35-5F-1` round-10 field set 5/5 | **pass** (`5f=True`) |
| 1c | no empty scalar field; `verified-at` ISO-dated | pass / ISO (`2026-10-19`) |
| 2 | repo-path pointers resolve | **25/25 resolved** (I-C12); **28 unique paths, 0 unresolved** (I-C14, my own resolver) |
| 2b | digest pins compared / stale candidates | **0 / 0** (no pin token on any pointer line) |
| 3 | decision record present | **pass** — `## 9. Decision record — the timekeeping decisions this entry fixes`, DR-TK-1…DR-TK-12 |
| 4 | gap statement present | **pass** — `- gap filled:` at line 4 |
| 5a | bleed strict candidates | **0** (`bleed=0/4` = four *negated* mentions) |
| 5b | ownership-assertion candidates | **0** |
| 5c | unnegated `canon` mentions | 4 (**all false positives** — §3 F-P1) |
| 6 | canon boundary named | **pass** (`non-canon`, `lore-shokunin`, `canon decisions belong`) |
| — | **I-C12 verdict** | **`PASS/review`** — `4of4=True 5f=True src=1/1 ptr=25/25 gap=True dec=True bleed=0/4` |
| — | **I-C14 verdict** | **`bar_pass: true`** — `frontmatter_missing: []`, `gap_leg_r10: true`, `decision_leg_r10: true`, `couples 25/25`, `couples_unresolved: []`, `repo_paths_dead: []`, `n_locators: 29`, `bleed_hits: []` |

**Frontmatter detail (I-C14).** Seven fields present — `topic`, `sources`,
`source`, `couples`, `verified-at`, `recheck`, `scope`. This is the **only** draft
of the round-35 ten to carry a literal `- scope:` field
(`C13-audit-1-5.md:212-217` records the same for the C04 landed block), so the
spare satisfies even the literal four-field reading the claim's shorthand implies,
not only the substituted `R35-4F-1` reading.

**Where the two instruments agree.** They agree on every graded value:
frontmatter 4/4 and 5/5, no empty field, ISO `verified-at`, gap present, decision
record present, canon boundary named, zero unresolved pointers, zero bleed, zero
ownership assertions. They **differ in coverage, not verdict**: I-C12's pointer leg
sees 25 bare-path tokens; my own resolver additionally sees 3 more paths inside
`couples:` prose and all 20 `path:line` citations. That coverage gap is
`C13-audit-1-5.md`'s **F12** re-derived (§3 F6).

## 3. Independent legs this seat ran, beyond both instruments

Every leg below is a command over bytes, not a re-reading of the spare's own
self-audit.

### 3.1 Citation resolution — 28/28 paths, 0 unresolved, 0 out-of-range

```
28 unique backticked repo-path tokens, 0 unresolved
20 attached `path.md:<lines>` citations; 30 line numbers checked; 0 out-of-range
15 bare `.md` tokens (no partition segment); all 15 resolve in the six partitions
0 detached (`path` + `:lines`) citations
```

Bare-name resolution was attempted against all six partitions
(`linguistics`, `myth-symbol`, `culture-material`, `synthesis`, `verification`,
`civilizations`), so a bare token that names a real entry is not counted as
dangling. The spare's own frontmatter cites its authority paths in full
(`corpus/knowledge/…`), which is why 28 of its tokens resolve on the first base.

### 3.2 Needle checks — cited lines say what the spare claims

Ten sampled citations read with `sed -n '<line>p'`; **10/10 match** the claim the
spare attaches to them:

| citation | observed at that line | claim it carries |
|---|---|---|
| `myth-symbol/celestial-symbolism-calendars.md:83` | "Egypt's 36 **decans** (star groups marking…" | decans as star clocks |
| `linguistics/numerals-and-measures.md:135` | "…sexagesimal counting underlies Babylonian time and angle units…" | the base-60 inheritance |
| `civilizations/aksum-ethiopia.md:98` | "## Calendar and hour-counting: separate calendrical and clock differences" | hour-label precedent |
| `culture-material/architecture-settlement-lexicon.md:90` | "…**minaret** < *manāra* 'light/beacon place'." | tower vocabulary, :90 |
| `myth-symbol/animal-symbolism.md:79` | "…decans as 10-day star clocks…" | "star clock" near-miss |
| `civilizations/benin.md:67` | "…bells, and lineage staffs…" | bell as ritual object, not time signal |
| `culture-material/calendar-festival-systems.md:23` | "## 1. The three clocks and the unavoidable lie" | the sibling's §1 |
| `linguistics/semantics-pragmatics.md:115` | "Bühler (1934): the deictic **origo**…" | temporal deixis |
| `culture-material/transport-mobility-lexicon.md:18` | "…Chaucer's English version in the *Treatise on the Astrolabe* prologue." | astrolabe as Chaucer title |
| `civilizations/persia-sasanian.md:98` | "…Chaucer, *A Treatise on the Astrolabe* i.19)…" | astrolabe as etymological aside |

The two `astrolabe` citations are the spare's own disposition of a near-miss
("both as a Chaucer title and an etymological aside") — **confirmed correct by
reading both lines**.

### 3.3 The quoted absence sweep reproduces exactly at the pinned HEAD

The spare quotes a 26-term loop and asserts **0 for every term**. Re-run verbatim
against an isolated `git archive 4a7aede` copy (pre-landing):

```
26 quoted terms: water clock, clepsydra, clepsammia, gnomon, sundial, escapement,
  pendulum, hourglass, "incense clock", curfew, "bell tower", "canonical hour",
  clockmaker, muwaqqit, wadokei, shichen, "toki no kane", horologium, foliot,
  quadrant, sandglass, "candle clock", "night clock", "standard time",
  "railway time", vigilia
observed at 4a7aede: 0 files for 25 of 26 terms; curfew → 1 file
```

`curfew` returns **1** — and that file is `corpus/knowledge/culture-material/fire-fuel-light.md`,
which **landed in round 35** (`git grep -ril -- "curfew" 4a7aede` → **no match**;
`git grep … ce103bf` → 1). So the spare's `0` is **correct at its own authoring
revision**, and the single non-zero is landing drift (§4), not an error.

### 3.4 The near-miss counts reproduce exactly at the pinned HEAD

The spare's `- gap filled:` line reports near-misses. Re-run verbatim at
`4a7aede` vs now:

| term | spare reports | at `4a7aede` | at `ce103bf` (now) | class |
|---|---|---|---|---|
| `astrolabe` | 2 | **2** | 2 | exact |
| `"star clock"` | 2 | **2** | 2 | exact |
| `chronometer` | 2 | **2** | 4 | landing drift |
| `obelisk` | 1 | **1** | 1 | exact |
| `meridian` | 1 | **1** | 1 | exact |
| `"time zone"` | 1 | **1** | 1 | exact |
| `bell` | 81 | **81** | 87 | landing drift |
| `hour` (word-boundary) | 8 | **8** | 11 | landing drift |
| `clock` in culture-material | 6 | **6** | 10 | landing drift |
| `"night watch"` | 1 | **1** | 2 | landing drift |

**All nine near-miss figures are exact at the spare's own authoring revision.**
Every divergence at the current HEAD is a file *added by round 35*, not a
miscounted citation.

### 3.5 Duplication and target-collision checks

- **No live-entry duplication.** Jaccard token overlap of the spare's 1696-char
  `- topic:` against all 211 live topics: **no candidate above 0.30**, no identical
  prefix. The spare extends its named neighbours, it does not restate one.
- **No slug collision.** `timekeeping-instruments.md` collides with no existing
  filename in any partition.
- **Ladder-tag / couples hygiene**: all 25 `couples:` targets resolve (I-C14
  `couples_unresolved: []`), including the two synthetic-cross-partition references
  (`synthesis/era-language-staging.md`, `verification/to-verify-triage-protocol.md`).

### 3.6 The README delta the landing would require (arithmetic, not measured)

The spare is **not landed**, so this is the delta the integrator would owe if the
spare were routed into the corpus — computed from the current pinned README, not
asserted as done. Current state: `culture-material 24`, total `211`, README rev
**2.0**, sha256 `51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`.

| surface | current (measured) | after a +1 culture-material landing |
|---|---|---|
| `## culture-material/` heading (`README.md:186`) | `(24)` | `(25)` |
| `Total knowledge entries:` (`:492`) | `211.` | `212.` |
| counts footer (`:496`) | `(total 211 files; directory totals 21/23/24/29/20/94).` | `(total 212 files; directory totals 21/23/25/29/20/94).` |
| revision block | `2.0` | a new `2.1` block, appended above 2.0 |

This **matches the round-36 claim C's own `after_required`** ("CM 25 / total 212;
README rev 2.1 sweep-green (212 rows == 212 files)"; `reports/round-36/claims.json:25`).
The delta is C02/C03's to draft and the integrator's to apply; it is recorded here
only so the audit's numbers are not confused with the landed state.

### 3.7 The round-35 index instrument still reads green post-landing

Run from an isolated `git archive ce103bf` copy (never in-tree):
`python3 -B reports/round-28/readme/sweep.py` → `rows 211 files 211`,
`missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`,
`totals_line 211 totals_ok True`, `footer_ok True`, exit 0. The spare's landing
would be measured against this instrument, not against prose.

## 3b. Findings, severity-ranked

Severity follows the runbook's own tiering (`cov/C12-audit-runbook.md:28-29`):
**S1** = blocker (fails the structural contract), **S2** = major/precision,
**S3** = review-tier observation. **No S1 finding: the spare clears the structural
contract on both instruments.**

| # | sev | finding | evidence | owner |
|---|---|---|---|---|
| **F1** | **S2** | **The round-35 runbook's stager mis-targets this spare.** Run per the runbook's own §4 step 2 (`--fragments` over a directory holding only the spare), I-C12 emits `STAGED … -> .scratch/c01/stage-c12/corpus/knowledge/culture-material/**calendar-festival-systems.md** (40235 bytes)` — an **existing, filed entry**, not the spare's own intended slug. The stager takes the *first* `corpus/knowledge/<partition>/<slug>.md` anywhere in the fragment (runbook fragment `:763`; installed instrument `c12-instrument.py:575` — the instrument bytes start at fragment `:188`), and this spare names no landing target, so the first corpus path in the text — a `couples:` target — is taken as the target. The stage step **silently overwrites a live entry's path** in the staging tree and audits the wrong slug. | the `STAGED` line above; `C13-audit-1-5.md` **F11** is the same defect class (stager fence/target limits) | integrator / C12 runbook (the runbook is filed bytes; the integrator decides repair) |
| **F2** | **S3** | **The spare's `hour` = 8 carries an unnamed reading.** It is reproducible only under word boundaries: `grep -rilw -- "hour"` → **8** at `4a7aede`; the plain-substring count is **12** at `4a7aede` (17 now) and the culture-material-only count is 4. The spare does not quote the `-w`. Same class as `C13-audit-1-5.md` **F1** and its §7 C04 note. | the three commands, run at both revisions | C04 (filed; note only) / integrator |
| **F3** | **S3** | **The spare's `- verified-at:` says "all 28 instrument terms"; its own quoted loop has 26.** Parsing the quoted `for kw in …` list yields exactly **26** terms (`c12` block §3.3). The sweep *reproduces*; the term count is off by two. Independently observed for the same draft at `C13-audit-1-5.md:203` ("the draft's `- verified-at:` line calls them '28 instrument terms' … S3"). | the parsed term list; the two readings agree | C04 (filed) |
| **F4** | **S3** | **No drift disclosure on a live spare.** Every quoted count in the spare is a **pinned reading at `4a7aede`** and the spare says so ("run 2026-10-19 at HEAD 4a7aede", `- source:`), but it does not state that the corpus **has since moved** — and it has, because the ten round-35 entries landed at `ce103bf` and five of the spare's own near-miss counts are now different (§4). Any reader re-running the quoted loops on the current tree reads different numbers. | §4 table; the two HEAD pins | integrator (a routing note, not a byte rewrite) |
| **F5** | **S3** | **The spare declares no landing target path.** It names its slug only in prose (`# Timekeeping Material Culture — …`) and in the filing header, never as a `corpus/knowledge/<partition>/<slug>.md` target marker, so no stager can resolve its intended path without a human decision — which is what produced F1. | the fragment's corpus tokens (first is `culture-material/calendar-festival-systems.md`, a couples target) | C04 (filed) / integrator |
| **F6** | **S3 (interop, re-derived)** | **I-C12's pointer leg undercounts.** It compares **25** bare-path tokens where the spare carries **28** unique repo paths and **20** `path:line` citations. This is `C13-audit-1-5.md` **F12** ("the pointer leg reads only bare-path tokens, not `path:line` citations … 26 pointers compared against 322 citations") independently re-derived on a different draft. | I-C12 `ptr=25/25` vs my resolver's 28 paths / 20 citations | integrator / C12 runbook |

### 3c. Review-tier hits, adjudicated (false positives, read in full)

| id | flagged | adjudication |
|---|---|---|
| **F-P1** | I-C12 `canon-mention-unnegated:canon,canonical` (4 hits) | **False positive, all four.** The hits are: (a) `- scope:` line 10 — "names no **canon** fact, makes no promotion or clearance verdict" (an explicit *negation*); (b) line 87 — "the partition's **canon** tags from `material-culture-inference-method.md` §2" (the ladder-tag sense, an in-corpus term); (c) line 117 — "a **canon** tag (HARD/SOFT/DOCTRINE/DESIGN)" (same sense); (d) line 134 — "**NON-CANON** — a demonstration, not a world decision" (a refusal). None asserts a lane canon. This is the polysemy the runbook itself anticipates (`:41,60`) and the same reading `C13-audit-1-5.md:207-210` reached for the C04 landed block. |
| — | I-C12 `bleed=0/4` | Four *negated* mentions, all ordinary boundary prose — expected, not a finding. |
| — | I-C14 `bleed_hits: []` | Zero affirmative-frame hits. Agrees with I-C12. |

**Cross-instrument agreement ledger.**

| reading | I-C12 | I-C14 | this seat's resolver | resolution |
|---|---|---|---|---|
| frontmatter 4/4 & 5/5 | pass | `frontmatter_missing: []` | 7 fields incl. literal `scope` | **agree** |
| gap named | `gap=True` | `gap_leg_r10: true` | `- gap filled:` line 4 | **agree** |
| decision record | `dec=True` | `decision_leg_r10: true` | `## 9. Decision record`, DR-TK-1..12 | **agree** |
| pointers resolve | `ptr=25/25` | `couples 25/25`, `repo_paths_dead: []` | 28 paths, 0 unresolved, 0 out-of-range | **agree** (coverage differs, F6) |
| bleed / ownership | 0 / 0 | 0 | 0 affirmative | **agree** |
| canon mentions | 4 unnegated | not graded | 4, all non-lane senses | **agree after reading** |

## 4. Landing drift — stated rather than hidden

Round 35 landed the ten thin-partition entries at `ce103bf`, moving the corpus from
201 to 211 files. The spare is a **live artifact written at `4a7aede`**, so any of
its quoted counts that touches a *landed* file reads differently today. The drift
is fully accounted for and **none of it is an authoring error**:

| quoted reading | spare | at `4a7aede` | at `ce103bf` | caused by |
|---|---|---|---|---|
| `curfew` | 0 files | **0** | 1 | `fire-fuel-light.md` (landed r35) |
| `night watch` | 1 | **1** | 2 | `fire-fuel-light.md` |
| `chronometer` | 2 | **2** | 4 | `funerary-material-culture.md`, `writing-media-surface-economy.md` |
| `bell` | 81 | **81** | 87 | six landed entries |
| `hour` (`-w`) | 8 | **8** | 11 | landed entries |
| `clock` in culture-material | 6 | **6** | 10 | landed entries |

The five instrument terms that stay at 0, and the four near-misses that stay
exact, are the load-bearing part of the gap claim: **the corpus still owns no
timekeeping instrument** (`water clock`, `clepsydra`, `gnomon`, `sundial`,
`escapement` → 0 files at both revisions). The gap the spare claims is still open.

### 4b. A filed byte moved during this seat's run, then reverted — recorded, not touched

`git status --porcelain` at this seat's start showed only `?? reports/round-36/`;
mid-run it also showed **` M reports/round-34/validation.json`**, modified at
`2026-10-19 06:28:02` — during this seat's run and **not by this seat** (this seat
wrote only `reports/round-36/cov/C01-audit.md` and gitignored `.scratch/c01/`). By
`06:28:15` the same file was **byte-identical to `HEAD` again** and
`git status --porcelain reports/round-34/` was clean, so the modification was
**transient** and left no residue.

| field | committed (`HEAD`) | observed mid-run `06:28:02` | now `06:28:15`+ |
|---|---|---|---|
| `acceptance_checks_passed` | `true` | **`false`** | `true` (restored) |
| `claims.O.passed` | `true` | **`false`** | `true` (restored) |
| `claims.O…O1-O5.status` | `green` | **`failed`** | `green` (restored) |
| `class_counts` | `{'guarded-refresh': 18, 'unguarded-in-place': 11}` | `{'guarded-refresh': 19, 'unguarded-in-place': 11}` | `{'guarded-refresh': 18, …}` (restored) |

The transient failure text was `O1-O5: O2: inventory counts differ: 30 runners,
{'guarded-refresh': 19, 'unguarded-in-place': 11}` — a round-34 `O` leg reading
**19 guarded-refresh runners where 18 were filed**. Two readings follow, and they
are reported separately rather than merged:

- **The filed bytes are intact.** `git diff --stat reports/round-34/validation.json`
  → no output; the committed verdict (`acceptance_checks_passed: true`) is what the
  tree holds now. Claim C's "zero other count surfaces drift" leg is therefore **not
  breached by a standing edit**, and no correction is owed on this file.
- **A transient in-tree re-run of a filed round runner did occur.** That is exactly
  what `shared_rules[4]` and `F-C13-1` bar (`run-validation.py` in-tree; isolated
  `git archive` copies only), and it is the mechanism by which a *19th*
  guarded-refresh runner was momentarily counted. This seat did not perform it
  (its only executed filed code is `reports/round-28/readme/sweep.py`, read-only,
  in an isolated `git archive` copy) and takes no position on who did. Filed here
  so the integrator can decide whether a process finding is owed; the *count* is
  now consistent with the committed bytes.

Owner: integrator.

## 5. Recipe — reproduce this audit in one command

All from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

```sh
# install both instruments from filed bytes and verify their digests
awk '/^```python$/{f=1;next} /^```$/{f=0} f' \
  reports/round-35/cov/C12-audit-runbook.md > .scratch/c01/c12-instrument.py
awk '/^```python$/{f=1;next} /^```$/{f=0} f' \
  reports/round-35/cov/C14-audit-6-10.md      > .scratch/c01/audit-v2.py
sha256sum .scratch/c01/c12-instrument.py .scratch/c01/audit-v2.py
#   expect 973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d (663 lines)
#   expect 3e255037cc70878d6707f908849173d08014839a5c5ae76c54609f52a2319fe2 (370 lines)
python3 -B .scratch/c01/c12-instrument.py --selftest     # SELFTEST PASS, exit 0
python3 -B .scratch/c01/audit-v2.py --selftest           # 13/13 PASS, exit 0

# stage the spare's fenced block and audit it on both instruments
python3 -B - <<'PY'
import re, pathlib
t = pathlib.Path("reports/round-35/cov/C04-timekeeping-spare.md").read_text(encoding="utf-8")
b = re.findall(r"(?m)^```(?:markdown|md)\s*$\n([\s\S]*?)^```\s*$", t)[0]
out = pathlib.Path(".scratch/c01/stage/corpus/knowledge/culture-material/timekeeping-instruments.md")
out.parent.mkdir(parents=True, exist_ok=True); out.write_text(b, encoding="utf-8")
PY
python3 -B .scratch/c01/c12-instrument.py .scratch/c01/stage/corpus/knowledge/culture-material/timekeeping-instruments.md
python3 -B .scratch/c01/audit-v2.py --drafts reports/round-35/cov/C04-timekeeping-spare.md --json

# the drift comparison (isolated copy; never in-tree for a round runner)
mkdir -p .scratch/c01/iso && git archive 4a7aede | tar -x -C .scratch/c01/iso
cd .scratch/c01/iso && for kw in curfew "night watch" chronometer bell; do
  printf '%s %s\n' "$kw" "$(grep -ril -- "$kw" corpus/knowledge/*/*.md | wc -l)"; done
```

Expected: I-C12 `PASS/review` with `4of4=True 5f=True ptr=25/25 gap=True dec=True
bleed=0/4`; I-C14 `bar_pass true`, `couples_unresolved []`, `repo_paths_dead []`.

## 6. Limits — what this audit does not say

- **No network.** Every external citation in the spare (Landes, Dohrn-van Rossum,
  Cipolla, Needham, Price, Bedini, King, White, Thompson, Mumford, the OED) is
  checked for presence, form and the spare's own `(to-verify)` marking; **no work
  was fetched, no page checked, no OED entry consulted**. The spare discloses this
  itself in `- source:` and `- verified-at:`; this audit confirms the disclosure is
  honest and complete, not that the scholarship is right.
- **Structural, not scholarly.** `PASS` is a reading of bytes; it is not admission,
  clearance, promotion or canon (`PROVINCE.md:20-27`; `corpus/QUALITY.md:18-20`).
- **The spare is unlanded.** Nothing here writes a corpus byte; §3.6's README delta
  is arithmetic the integrator would owe, not a measurement of a landing.
- **This is not claim C's second independent auditor.** C02 owns the second audit
  and the README delta draft, C03 verifies both. This seat's second read is of the
  *spare*, per its mission, and the two readings above are two *instruments* on one
  artifact, not two seats.

## Owed

- **The spare's landing decision** — not this seat's to take. The spare is
  structurally clean on two instruments; whether it becomes claim C's 25th
  culture-material entry, and therefore whether the README moves to rev 2.1 with
  totals 212, is the integrator's, gated on C02's delta draft and C03's verification.
- **`reports/round-36/cov/C02-audit-delta.md`** — the second independent audit and
  the README delta draft; absent at this seat's snapshot. My §3.6 arithmetic is
  stated so the two can be compared, not so it can stand in.
- **F1's repair** — the runbook stager is filed round-35 bytes and its fix is the
  integrator's; the minimal repair is a target-path marker convention (F5) plus a
  stager rule that prefers an explicit target over the first corpus path in the text.
- **`reports/round-36/run-validation.py`** — claim C's counting command
  (`reports/round-36/claims.json:20,32`); absent, and per `shared_rules[4]` it may
  only ever be executed from an isolated `git archive` copy, never in-tree.

## Citations

- `reports/round-36/targets.json` — `seats[id=C01].mission`, `shared_rules[]`;
  `reports/round-36/claims.json:16-33` — claim C (`:22` claim text, `:25`
  `after_required` incl. "CM 25 / total 212 … README rev 2.1", `:26-27` counting
  commands, `:28` thresholds), `:6-8` baseline `ce103bf`.
- `REGIMEN.md:25-50,52-58` — the per-round contract and the done-when clause.
- `reports/round-35/cov/C04-timekeeping-spare.md` — the audited artifact; sha256
  `258fb166e35f3b0f92854dcb7c5e08fcfc285c51a42aa828cb79f3f761f5bcd2`; extracted
  entry sha256 `9805c0b854334ed396119476b6278cc4f58eb1014a0b06eb6bba561def05f0a6`.
- `reports/round-35/cov/C04-entry-4.md` — the landed sibling; its two fenced blocks
  (sha `15f2ea5de5bb9406…` = the landed bathing entry, sha `9805c0b854334ed3…` =
  the spare) are how §1 proves the spare is a distinct draft.
- `reports/round-35/cov/C12-audit-runbook.md:26-49` (check families 1a–6 and tiers),
  `:84-128` (the §4 recipe and exit codes), `:182-187` (instrument bytes, sha256
  `973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d`, 663 lines),
  `:763` (the stager's target regex — F1/F5; installed instrument `:575`),
  `:766` (its fenced-block regex; installed instrument `:578`).
- `reports/round-35/cov/C14-audit-6-10.md` §2 — the second instrument (sha256
  `3e255037cc70878d6707f908849173d08014839a5c5ae76c54609f52a2319fe2`, 370 lines);
  §3 — its calibration runs; §4 — the two checks an instrument cannot make.
- `reports/round-35/cov/C13-audit-1-5.md` — `:203` (the "28 vs 26 terms" note on the
  same draft), `:207-217` (C04 adjudications and the literal `- scope:` field),
  `:129-132` (**F11** stager fence/target limit, **F12** pointer-leg coverage),
  `:109` (**F1** the occurrence-vs-file count class).
- `reports/round-35/plan/P01-c-plan.md:91-96,167-172,524-544` — the held alternates
  with evidence and the swap rule; `timekeeping-instruments` named at `:91,:529-531`.
- `reports/round-25/argot/execution-4.md:35,130` — "**zero register forms to
  replay** … the register-form leg has no input on the delivered tree" (read for
  context; the round-36 claim D record, not this seat's claim).
- `corpus/QUALITY.md:3-23` — the admission bar this audit reads structurally.
- `corpus/README.md:3,186,492,494,496` — rev 2.0 block, `## culture-material/ (24)`,
  totals `211`, footer `(total 211 files; directory totals 21/23/24/29/20/94)`;
  sha256 `51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`.
- `reports/round-28/readme/sweep.py` — the lane's index instrument of record,
  run only from an isolated `git archive` copy (§3.7, §5).
- `reports/round-34/validation.json` — committed bytes only, read for §4b: the
  committed `acceptance_checks_passed: true` / `class_counts {'guarded-refresh': 18,
  'unguarded-in-place': 11}`; the transient working-tree state was observed by
  `git diff --stat` and reverted at `06:28:15` (no byte written by this seat).
- `PROVINCE.md:20-27` — the owns/refuses boundary this audit stays inside.
- **Commands run** (2026-10-19, lane root,
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, HEAD `ce103bf`):
  `git rev-parse HEAD` → `ce103bf5885af00023cdc4a174c17602476cdcf8`;
  `git status --porcelain` → `?? reports/round-36/` only;
  `sha256sum` over the fragment and both instruments; both `--selftest` runs;
  `python3 -B .scratch/c01/c12-instrument.py <staged>` → `PASS/review`;
  `python3 -B .scratch/c01/audit-v2.py --drafts … --json` → `bar_pass true`;
  `python3 -B .scratch/c01/c12-instrument.py --fragments .scratch/c01/drafts
  --stage .scratch/c01/stage-c12` → the F1 `STAGED … calendar-festival-systems.md` line;
  the 26-term sweep loop; the near-miss loop at both HEADs via `git grep … 4a7aede`;
  the citation resolver (28 paths, 20 `path:line`, 30 line numbers, 0 out-of-range);
  ten `sed -n '<line>p'` needle reads; the Jaccard topic comparator over 211 entries;
  `git archive 4a7aede | tar -x -C .scratch/c01/iso` then the sweep in that copy;
  `git status --porcelain` and `git diff --stat reports/round-34/validation.json`
  at `06:28:02` (transient ` M`, `acceptance: false`) and again at `06:28:15`
  (clean, `acceptance: true`, no diff) — §4b.
- **Not run, deliberately**: any `reports/round-*/run-validation.py` (F-C13-1); any
  `--freeze` of `reports/round-34/handoff/declared-in-r7`; no network call.
