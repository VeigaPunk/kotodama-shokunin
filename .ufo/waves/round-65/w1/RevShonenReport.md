# RevShonenReport — round-65 report readiness (section-by-section)

Seat `kotodama-r65.RevShonenReport` (leaf; no delegation). Lane `kotodama-shokunin`, base
`17c32302c6845c8f164b985a8cb312d3181c8788`. Read-only over lane and fleet; no git/jj writes; no
tool installs (host `git`/`python3`/`bash` only; pacman untouched per the host-wide pause). The
`lsp` device is not exposed in this seat's toolset (no `lsp` tool in the inventory); every check
below is a command or textual citation, recorded as such — not presented as semantic proof.

Mandate: list the round-65 report's required sections and pre-compute the SHONEN lines that change
(registry rows, capability additions). Model: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-64/kotodama.md`
(fleet, read-only) and the canonical contract `.ufo/prompts/kotodama-round-65.md:100-125` (+
`:326-341` extras, `:175-220` wave-shape). Lane copy of SHONEN: `SHONEN.md` (15 lines, 4 boxes).

## T0 state measured (report is NOT yet writable honestly)

- Wave live: 33 of 64 seat reports under `.ufo/waves/round-65/w1/`; `stage/` has `entry-draft.md`,
  `gate-spec.md`, `readme-patch.md`, `mut-o/`, `mut-ca/`; `rows/` holds 2 seat dirs; **no** entry,
  no S750-S775 registry row, no `corpus/lessons/round-65.md`.
- Registry at base, measured: **675 rows, tier A 421 / B 244 / C 10, status mined 592 / queued 61
  / rejected 22** — `bash scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kotodama`
  (prints `kotodama rows …` then `tier.*`/`status.*`; read-only per its header). Corpus: **238**
  entries (`ls corpus/knowledge/*/*.md | wc -l`), culture-material **31**.
- Counters are a moving target during this review: sha256 at first read `accept-c 8f44b649…` /
  `accept-o 2a03a2fe…` / `accept-ca a60b75ae…` / tool `0e2200e5…`; at last read `bc35de5c…` /
  `20d06dd6…` / `550c89a4…` / `9fe025fe…`. Legs: claims say **C 10, O 26, Ca 9**, but the current
  Ca counter prints **10** (`RECEIPTS` added) — see F3.
- Base dry-run tallies (from the receipts, not re-run): C 7 FAIL / 3 vacuous PASS (`RESTATE`,
  `HOSTS`, `LINK` pass over 0 lines/rows); O 24 PASS / 2 FAIL (`FULL`, `MUTEX`), `FRAG` a vacuous
  PASS over 0 files; Ca 0 PASS / 9 FAIL at the 01:20 receipt, 10 FAIL at the 01:55 receipt after
  `RECEIPTS` landed (`QUOTES` exit 2 on the missing lesson file).
- Telemetry at T0: `census-start.txt`, `controls-{c,o,ca}.txt`, `dry-run-{c,ca,o}.txt`
  (`controls-ca.txt` landed 01:55, after my first read).
  Absent: `final-measures-{c,o,ca}.txt`, `census-end.txt`, `exactness-sweep-o65.txt`,
  `separability-manifest.json` (the exact path `claims.json`'s `check` names —
  `.ufo/waves/round-65/stage/` lacks it too).
- Ca targets unlanded at T0: `reports/round-64/telemetry/final-measures-ca.txt` has **0** `tree:`
  lines; no `statement_correction` in `reports/round-64/claims.json`; no `Correction (round 65`
  entry in `reports/round-63/telemetry/revisions.txt` or `corpus/lessons/round-64.md`;
  `corpus/knowledge/linguistics/language-socialization-and-acquisition.md:5` still reads
  `verified-at: 2026-10-23 — skeleton structure prepared; cited source claims await L1 insertion…`;
  `corpus/QUALITY.md` has no criterion 17 (`:51` holds criterion 16's hold note).
- Lane HEAD `17c3230` (the round-64 non-author verifier spot-check commit). Untracked round-65
  instrument paths: `reports/round-65/`, `.ufo/waves/round-65/`, `tools/check-row-fragments.py`.

## 1. Required sections, in order (canonical), with round-65 content and readiness

Contract: `.ufo/prompts/kotodama-round-65.md:100-118` (six sections; `Sources & frontier` and
`Trend verdicts` are conformance items, not marker predicates; a contentless/missing-section
report fails the round). Lane-specific additions are marked (extra).

| # | Section | Must contain for round 65 | Ready now? | Blocker / owner |
|---|---|---|---|---|
| 0 | Header line | Lane; round 65 = hyaku run 5, 2026-10-24; **base `17c32302…`**; declaration path `reports/round-65/claims.json`; measured-at revision(s); lane HEAD + pushed state (`jj-lane.sh state`: local=remote, ahead=0); shape = **ONE v2 wave, 64 seats** | ✗ | measured-at/HEAD exist only after the L1 commit+push |
| 1 | Work performed | Opens with the 3 declared claims (C coverage/sourced, O operability/capability, Ca calibration/records) and their targets; then one bullet per work item **with an evidence pointer**: 26 row seats S750-S775, entry assemble + gate + README drafts, three counters (rev 2/rev 3 per claim), `tools/check-row-fragments.py`, R1-R7 fix drafts, separability, sibling scans, the 29-seat attack ring, L1 integration; the **wave-shape line** (see §2.4) and dead seats belong here or in Extras | ✗ | drafts only; seat reports still landing |
| 2 | Landed changes | Every change tied to a `LOG.md` entry **and** the carrying commit hash. Expected commit set: (a) instruments + wave evidence + tool; (b) claim-C lands (entry, `corpus/SOURCES.md` +26, `corpus/README.md`); (c) claim-Ca lands (re-stamped receipt, `revisions.txt`, round-64 `claims.json` correction, `control-o` binding, lesson R6 note, entry R7 line, `QUALITY.md` 17, `corpus/lessons/round-65.md`); (d) records (lesson/LOG/SCORECARD/SHONEN); report last on the fleet repo | ✗ | all four commits pending |
| 3 | Before → after measurements | One block per claim, each with the counting command, the **bytes/commit measured**, and the receipt: C 10 legs, O 26, Ca 10 (numbers in §2.3); include the erratum for the round-64 Ca receipt | ✗ | final receipts absent; receipts predate the current counter bytes (F4) |
| 4 | Sources & frontier | `SOURCES.md` 675 → 701 with the counting command; rows added by tier (A a / B b, a+b=26 — measure, do not reuse round-64's 14/12); rows touched old→new (**none** in place: `APPEND` proves all 675 base lines verbatim; `NOHARM` diff = exactly the new entry); frontier rows advanced S750-S775 (mined, used-by the entry) + `## Gate` 26 rows in `corpus/lessons/round-65.md` (URL, access 2026-10-24, ≤25-word quote); README 238→239, culture-material 31→32, index row, frontier bullet | partial | counts measured above; entries/rows pending |
| 5 | Trend verdicts | One verdict each for `expansion`, `quality`, `discernment`, each with evidence, no scalar. Round-65 material: expansion 238→239 + 26 rows (with the F1 caveat); quality 10/10+26/26+10/10 frozen predicates, upgraded FULL/MUTEX/FRAG legs, ring repairs; discernment pre-data rev-2/3 controls on all three counters + R1-R7 dispositions + the filed-report erratum. Spec lists six axes (`spec-v2.json`) — depth/freshness/adjacency get an explicit `unchanged` line with reason (freshness pause in force) | ✗ | depends on final PASS receipts |
| 6 | SHONEN | One line per box of `SHONEN.md`; marks stay `[~]` (non-author verifier required for `[x]`); pre-computed text in §3 | pre-written | numbers in §2.1, capability rows in §3.4 |
| 7 | Erratum (extra; required by Ca) | The two corrections to the **filed** fleet report `round-64/kotodama.md`, byte-preserved otherwise: (i) `:32` cites `w2/ReviewerCa.md` — actual `w1/ReviewerCa.md` (R3); (ii) Ca measured revision — `:3`/`:32` say `95c9194e`, the re-stamped receipt binds `8bab271c…` (R1). Name the route decision (lane write scope cannot edit the filed report; operator may choose in-place fix) | ✗ | depends on the re-stamped receipt landing |
| 8 | Extras (extra) | `Stale-lane` line (respawn-per-round driver; no other mission open); tool installs (none — record); L0 questions (none so far); dead seats by id (watchdog at T0: only `launch kotodama round=65 … attempt=1`, no `lane-dead` line); inherited state (base HEAD is the non-author spot-check commit; the three untracked round-65 path groups must be committed under this round's entry and named); capability rows (§3.4) | partial | dead-seat tally final only at report time |

## 2. Pre-computed values (grounded in commands above)

### 2.1 Registry rows — the SHONEN box-1 figure

- Before (base, measured): `675 rows — A 421 / B 244 / C 10 — mined 592 / queued 61 / rejected 22`.
- After (frozen claim C): `675 + 26 = 701 rows`; `mined 592 + 26 = 618`; `queued 61`; `rejected 22`.
- Tiers after: `A = 421 + a`, `B = 244 + b`, `C = 10`, with `a + b = 26` — **a and b must be
  measured at the end** (`sources-census.sh census` prints `tier.A/B/C`); do not copy round-64's
  14/12.
- Commands to paste in the report:
  - `bash scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kotodama`
  - `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` (exit 0)
- Corpus: `238 → 239` (`ls corpus/knowledge/*/*.md | wc -l`), culture-material `31 → 32`.

### 2.2 Claim-C gap numbers (claims.json already corrected — see F1)

The frozen statement (statement revision 1, pre-data) uses the **word-bounded** census; re-measured
at base: filename scan → **0**, `- topic:` scan → **0**. The superseded substring censuses printed
2 filename hits and 37 raw topic-line hits — all incidental substring matches. `claims.json`
records the 2 filename matches and states the predicate is unchanged; the 37 raw topic-line hits are
recorded nowhere, so the report may name them as history but must cite the word-bounded command as
the gap evidence.

### 2.3 Leg counts and base tallies (report "before" evidence)

| Claim | Legs | Base result (receipt) | After target |
|---|---|---|---|
| C | 10 (`FILE ROWS ONEID RESTATE HOSTS LINK APPEND NOHARM SWEEP LIVE`) | 7 FAIL; `RESTATE/HOSTS/LINK` vacuous PASS at 0 lines/rows; `ROWS` checked=26 | PASS 10/10, `ACCEPT-C-65`, exit 0 |
| O | 26 (`… EDGE_* DRIP MUT FULL MUTEX FRAG`) | 24 PASS / 2 FAIL; `FRAG` vacuous PASS 0 files (rev-1 bytes) | PASS 26/26, exit 0 |
| Ca | 10 (`R1..R7 CRITERION QUOTES RECEIPTS`; claims list 9 — F3) | 0 PASS / 10 FAIL (receipt 01:55; `QUOTES` exit 2 on the absent lesson) | PASS 10/10, exit 0 |

Receipts to write: `reports/round-65/telemetry/final-measures-{c,o,ca}.txt` (+ `census-end.txt`,
`exactness-sweep-o65.txt`), each carrying timestamp, command, counter sha256, measured revision, a
`tree:` hash of read inputs, and the **lands commit (`main^`)** — the Ca counter's `RECEIPTS` leg
checks exactly these (control 6, `controls-ca.txt`) — plus wall and exit code.

### 2.4 Wave-shape numbers (report must name shape + mix)

`spec-v2.json`: 64 items — scout 19, reviewer 14, critic 9, mutation-tester 6, scribe 5, executor 4,
sentinel 2, simplifier 2, revenger 2, connector 1. Attack roles = reviewer+critic+mutation-tester =
**29/64 = 45%** (v2 floor 25%). Shape: one v2 wave, band 64–128 (`ufo-wave-policy-v2.json`); L1
holds the planner seat (validator rejects `planner`); no residual call at T0; v1 32+32 shape not
used this round.

### 2.5 Ca leg → land map (report's per-defect evidence column)

| Leg | Land it counts | State at T0 |
|---|---|---|
| R1 | `reports/round-64/telemetry/final-measures-ca.txt` re-stamped `8bab271c…` + tree hash, original bytes preserved; repeats fixed in LOG/SCORECARD/`w2/LessonFinal.md` | receipt exists, 0 `tree:` lines; repeats still wrong (`LOG.md:4162`) |
| R2 | `reports/round-63/telemetry/revisions.txt` named append-only correction | absent |
| R3 | lane records name `w1/ReviewerCa.md` (filed report corrected by erratum) | absent |
| R4 | `reports/round-64/claims.json` `statement_correction` for claim O ("at least their pinned leg", m1/m2 extras), predicate bytes untouched | absent |
| R5 | committed record binding `control-o.txt` to rev3 `c27a9fef…` / measured `b7d22703` | absent |
| R6 | `corpus/lessons/round-64.md` "Correction (round 65, R6)" after R64-M12 | absent |
| R7 | round-64 entry `verified-at:` line no longer reads "skeleton structure prepared…" | still reads it (`:5`) |
| CRITERION | `corpus/QUALITY.md` criterion 17 (receipt pins measured revision + tree hash of read inputs) | absent (criterion 16 hold note at `:51`) |
| QUOTES | `tools/check-gate-quotes.py` 0 findings on `corpus/lessons/round-65.md` | file absent |
| RECEIPTS | each `final-measures-*.txt` names the lands commit (`main^`), its tree, and the producing counter sha256 | absent (all three receipts) |

## 3. SHONEN lines that change — exact text

All four boxes stay `[~]` (no named non-author verifier signed this round; the closure spot-check is
the prior round's chain). Pre-computed report lines:

### 3.1 Box 1 (registry rows + capability additions) — the line that changes

> - Box 1 `[~]` — SKILL.md decision tables/error patterns/checklists unchanged this round
>   (`SKILL.md:20`, `:468`, `:522`); registry re-measured at **701 rows — 618 mined, 61 queued, 22
>   rejected** (`bash scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kotodama`,
>   receipt `reports/round-65/telemetry/census-end.txt`; 675 = 592/61/22 after round 64); tiers
>   `A 421+a / B 244+b / C 10`, `a+b=26`, measured at the same run; capability additions demonstrated
>   this round enter `SCORECARD.md`'s `capabilities:` table (`row-fragment-check`,
>   `filtered-run-guard`, `mutant-exclusivity-sweep`, `receipt-attribution`; §3.4); `SHONEN.md:6`
>   updated 412 (round 56) → 701 (old→new logged); pointer: `SHONEN.md:6`, `SCORECARD.md`
>   capabilities, `w1/RevShonenReport.md`.

### 3.2 `SHONEN.md:6` replacement (if the lane lands the stale-figure fix)

Keep the historical chain, prepend the current figure (one line, byte-exact draft):

> `  asserted: \`SKILL.md:20\` (Decision table), \`:468\` (Error patterns), \`:522\` (Checklist); sources registered in \`corpus/SOURCES.md\` (701 rows after round 65 — 618 mined, 61 queued, 22 rejected — census exit 0 in \`reports/round-65/telemetry/census-end.txt\`; 675 rows, 592/61/22 after round 64; 412 rows, 367/35/10 after round 56; 358 rows, 313/35/10 after round 55; 284 rows, 240/34/10 after round 54; the round-53 figure 194/35/9 became 194/34/10 in the round-54 prerequisite \`d761ee8\`); no non-author verifier on record.`

It is **not** in any claim's `lands`: if edited, name it in Landed changes with old→new and the LOG
entry; no accept leg reads `SHONEN.md`, and `NOHARM` is `corpus/knowledge`-only, so the edit cannot
move a predicate. If not edited, the box-1 report line must say the file figure stays stale and why.

### 3.3 Boxes 2–4 (pointer lines change every round)

> - Box 2 `[~]` — end-to-end round: claims declared (`reports/round-65/claims.json`, frozen
>   predicates C/O/Ca) → ONE v2 wave of 64 seats (29 attack = 45%, build+attack together; spec
>   `.ufo/waves/round-65/spec-v2.json`, taskcall `taskcall-v2.json`) → L1 integration → acceptance
>   (`final-measures-{c,o,ca}.txt`) → records (`corpus/lessons/round-65.md`, LOG, SCORECARD);
>   pointer: `LOG.md` round-65, `reports/round-65/telemetry/final-measures-*.txt`.

> - Box 3 `[~]` — cold executability: all 64 items ran from committed spec bytes alone (each item
>   carries context + task; the two wave-rule lines verbatim); the new durable checkers run from
>   written usage (`tools/check-row-fragments.py --selftest`, `accept-o.py --only` fail-closed,
>   `FULL` subprocess re-execution, `accept-ca` `RECEIPTS`, `check-claim-separability.py` on the
>   manifest); remaining conditions named: base dry-run receipts predate the revision-2/3 counter
>   bytes (F4).

> - Box 4 `[~]` — province accuracy: `PROVINCE.md` unchanged; two independent sibling scans found 0
>   semantic owners of the games register (`w1/ConnectorSiblings.md`, `w1/ScoutGapGames.md`; the
>   frozen "0 filename owners" command prints 2 lexical false positives and 37 raw topic-line hits,
>   all substring FPs); lore handoff one-way in the entry's final section; contested scope: none
>   found.

### 3.4 Capability rows (enter only with a passing demonstration in this round — AXES.md §Capabilities)

`SCORECARD.md` has **no** `capabilities:` table today (grep finds none; round-64 tables are axis
rows only), so the round-65 report must create it with these rows, each only after PASS:

| capability | what it can now do | evidence pointer | first-working round |
|---|---|---|---|
| `row-fragment-check` | scan pre-integration row fragments for teaches-cell over-length and query/fragment URL twins, incl. capture-vs-live mismatch | `python3 -B tools/check-row-fragments.py --selftest` exit 0; scan 0 findings over 26 fragments; `accept-o` `FRAG` PASS | 65 |
| `filtered-run-guard` | re-execute the complete battery in a subprocess so a filtered `--only` green cannot stand as the verdict | `accept-o` `FULL` PASS (revision 2 tolerates exactly the three self-recursion SKIPs) | 65 |
| `mutant-exclusivity-sweep` | sweep all ten counter mutants through every edge/DRIP fixture and pin the disclosed non-exclusive table | `accept-o` `MUTEX` PASS + `reports/round-65/telemetry/exactness-sweep-o65.txt` | 65 |
| `receipt-attribution` | receipts pin the measured revision, a tree hash of read inputs and the lands commit, not only a counter sha | `corpus/QUALITY.md` criterion 17 + `accept-ca` `CRITERION` and `RECEIPTS` PASS | 65 |

## 4. Findings (severity, evidence)

**F1 — LOW, claim-C gap wording (already corrected in `claims.json`; residual documentation).**
The C statement now reads `0 filename owners under the word-bounded census` and carries
`statement_revision: revision 1 (pre-data)`, naming the 2 incidental substring matches (`display`,
`transport`) found by `w1/ScoutGapGames.md`; predicate sentence unchanged. Re-measured at base:
word-bounded filename scan → **0**, word-bounded `- topic:` scan → **0**. Residual: the 37 raw hits
of the superseded *substring* topic scan are recorded nowhere, and a report paragraph quoting the old
census would read false. Cite the word-bounded command from the statement; do not restate the
substring figure as the gap, and do not present the topic-line check as if the substring scan were
the evidence.

**F2 — MED, O unverified; m6/m7 digit-blind regex repaired pre-data (rev 3).** `dry-run-o.txt`
(01:41) shows `MUTEX FAIL … m6:measured=[] … m7:measured=[]` while its own `MUT` leg shows
`m6->EDGE_308 FAIL`, `m7->EDGE_5TH200 FAIL`; cause: the rev-1/2 leg-line regex `[A-Z_]+` is blind to
the digits in `EDGE_308`/`EDGE_5TH200`. The current `accept-o.py:109` history entry
`revision 3: digit-aware leg-line regexes in FULL and MUTEX` (forcing control `w1/RevCounterO.md`,
which measured m6/m7 as NONE) repairs exactly that class, and MUTEX now requires sweep exit 1 and no
traceback. So this is a demonstrated pre-data repair, not an open inconsistency — **but no receipt
shows MUTEX measuring m6/m7**: `dry-run-o.txt` predates the rev-3 bytes. O stays unverified until a
run over the final rev-3 bytes prints every leg PASS with the committed sweep; until then the report
must not claim O or enter the `mutant-exclusivity-sweep` capability row.

**F3 — MED, counter revision/legs provenance drift.** (i) All three module headers still read
`revision 1 (pre-data)` while the histories and claims carry later revisions: `accept-c.py:2` vs
`:54` (rev 2, "every new row cited"), `accept-o.py:2` vs `:105/:109` (**rev 3**, digit-aware),
`accept-ca.py:2` vs `:50` (rev 2, R1 hardened). (ii) `accept-o.py` has a duplicated
`Revision history (pre-data):` heading (`:105`, `:108`) and its entries are out of order — rev 1,
then **rev 3**, then rev 2. (iii) `claims.json` lists the Ca legs as **9** (`R1..R7 CRITERION
QUOTES`) while the counter prints **10**: `RECEIPTS` was added (each final receipt must name the
lands commit `main^`, its tree, and the producing counter sha256 — `controls-ca.txt` control 6).
No predicate sentence changes, but final receipts must stamp the **sha256 + actual revision**, the
report must name "accept-c rev 2, accept-o rev 3, accept-ca rev 2", and the claims `legs` array
should gain `RECEIPTS`. Do not edit the header/docstring at this point without re-running every
receipt: the shas move, and `controls-ca.txt` already stamps `74077e40…`, which matches no on-disk
byte state.

**F4 — MED, every base receipt predates the frozen bytes.** The instruments moved during this review
(≈12 min): accept-c `8f44b649…`→`bc35de5c…`, accept-o `2a03a2fe…`→`20d06dd6…`, accept-ca
`a60b75ae…`→`550c89a4…`, tool `0e2200e5…`→`9fe025fe…`. `dry-run-c`/`dry-run-ca` (01:20) and
`dry-run-o` (01:41) therefore measured superseded bytes — the old `accept-c` receipt even emits a
`SyntaxWarning` at `accept-c.py:99` that current bytes do not — and `controls-ca.txt` stamps a counter
sha (`74077e40…`) that no current file matches. Required: freeze the instruments, re-run the three
base dry-runs at the final shas, and stamp every control/dry-run with counter sha256 + measured
revision + timestamp; otherwise the report's "FAIL at base" evidence is unauditable.

**F5 — MED, separability manifest missing at the referenced path.** `claims.json` `separability.check`
names `reports/round-65/separability-manifest.json`; the file is absent and `stage/` holds no draft at
T0 (`ExecSeparability` running). Without it the report has no separability receipt (the round-63
record-dependency precedent is the model: `reports/round-63/telemetry/rev-separability.txt`). Land the
manifest under `reports/round-65/` and run `python3 -B tools/check-claim-separability.py` on it.

**F6 — MED, census receipts carry no counts.** `reports/round-65/telemetry/census-start.txt` is 28
lines: duplicate-URL warnings + `kotodama ok …` — no rows line. Round-64's `census-end.txt` has the
same shape, yet the filed report cited "675 rows" from it. Required: write `census-end.txt` with the
`census` mode's count lines (`rows`, `tier.A/B/C`, `status.*`) plus `validate` exit 0 and the tree
hash, so the 701 figure is re-derivable from the receipt alone.

**F7 — MED, `SHONEN.md:6` figure stale.** It still says 412 rows after round 56 while 675 are
measured at base. Replacement draft in §3.2. If not landed, the box-1 line must say the file stayed
stale and why (round-64 precedent: noted, not fixed). Any edit: LOG entry + old→new in Landed changes.

**F8 — LOW, capability register absent.** `AXES.md:57-61` requires `SCORECARD.md` to carry a
`capabilities:` table; none exists. Claim O is framed as a capability acquisition, so the table must
be created (§3.4) — rows only after their demonstration passes; a pre-PASS row is pre-claiming.

**F9 — LOW, Ca base evidence read correctly.** `QUOTES FAIL exit=2 out=['GATE_QUOTES: 0 findings']`
is a missing-file exit, not a quote finding; `R1 FAIL … tree=0ec0e50e…` and the absent criterion 17
are unlanded lands, not counter misfires. The report must not describe the base Ca run as "the
checker found seven defects".

**F10 — LOW, `dry-run-o.txt` header contradicts its body.** The header says "FULL/MUTEX/FRAG must
FAIL"; the body shows `FRAG PASS … 0 file(s)` (vacuous), and MUTEX's failure includes the
uncommitted sweep file. The report must separate capability gap (FULL filtered-green, MUTEX
inconsistency F2) from missing land (`exactness-sweep-o65.txt`).

**F11 — INFO, runtime budget.** `FULL` subprocess wall 426.3 s; the final O receipt needs ~7+ min.
Record wall in the receipt; do not quote the leg as instant.

**F12 — INFO, tooling.** No tool installed or updated (pacman paused by orchestrator ruling; no uv/npx
needed). No `lsp` device in this seat's toolset; caller/definition/diagnostic checks were performed as
commands + textual citations, which is recorded as a verification gap, not semantic proof.

## 5. "Do-not-say" list for the L1 (each item has a receipt above)

1. Quoting the superseded substring census as the gap evidence — cite the word-bounded census (0)
   and the recorded 2 incidental filename matches (F1).
2. "FULL/MUTEX/FRAG all failed at base" — FRAG passed vacuously over 0 files (F10).
3. "ACCEPT-O-65 PASS" before a run on the final rev-3 bytes shows MUTEX measuring m6→EDGE_308 /
   m7→EDGE_5TH200 (F2).
4. "Counter revision 1" — claims name accept-c rev 2 and accept-o rev 3; headers are stale (F3).
5. "Census receipts record N rows" when the receipt has no count line (F6).
6. "Separability verified" before the manifest exists at the referenced path (F5).
7. "Criterion 17 landed" while `QUALITY.md` has none (F9).
8. "`SHONEN.md` figures current" if the stale line is left unfixed (F7).
9. "Ca PASS 9/9" — the counter prints 10 legs (`RECEIPTS`); claims.json still lists 9 (F3).

## 6. Residual risk and verification gaps

- **Everything "after" is unverified.** The wave is mid-flight (33/64 reports at T0). I did not run
  the acceptance batteries: at base they are already recorded FAIL by the dry-runs, and running them
  now would measure nothing the L1's final run does not. Every after-value in §2 is a frozen target,
  not a measurement.
- **O's PASS is unverified** (F2). No receipt yet shows the rev-3 MUTEX measuring m6/m7; if the final
  run still cannot, the honest report says O is `unprovable` with the exact receipt evidence, keeps
  the FULL/FRAG/rev-3 repairs as landed capability work, and does not enter the MUTEX capability row.
- **Erratum route** is an operator decision (`review_only_global`: in-place fleet fix vs round-65
  erratum). The report must carry the erratum either way and name the lane's write-scope bound.
- **Dead-seat count** is not final; watchdog shows only the launch line at T0 (`.ufo/watchdog.log`).
- **No semantic (lsp) checks** were possible; finding F1's "all substring false positives" is read
  from the 37 matched lines, and the per-row support/sentence-fidelity judgments remain review-only
  per `claims.json` (`review_only`, `review_only_global`).
- Fleet repo untouched; this file is the only write (lane `.ufo/waves/round-65/w1/RevShonenReport.md`).
