# RevIntegrity — r67 integration-risk review (claim bytes outside the counters' view)

Seat: `L1-kotodama-r67.RevIntegrity` · lane base `ad5b52b0` · instruments read at tip `b78f8b8`
· 2026-10-24. Verdict: **the frozen instruments admit PASS on bytes that never land (HIGH); the
single-revision C/Ca conflict is real and is resolved only by the ruled A_r→A_c→A_ca sequencing,
which the frozen files never declare and whose A_c→A_ca delta no leg grades (HIGH); and the counter
bytes already moved without a claims revision (HIGH).** All demonstrated against the frozen rev0
counters, whose bytes I verified hash-equal to the pre-wave dry-run receipts (`accept-c.py` sha256
`3e5f1a58…a97a5`, `accept-ca.py` sha256 `5e8915ac…36118`, matching
`reports/round-67/telemetry/dry-run-{c,ca}.txt` header lines). Line cites are to those frozen bytes;
the lane worktree's `accept-ca.py` has since changed (`5382ffed…`, HIGH-1b).

Axes: (1) claim-byte containment, (2) receipt/evidence honesty, (3) cross-claim satisfiability,
(4) draft→landed fidelity. All four have actionable findings.

## Method

No lane writes; read-only git only. A scratch clone
(`git clone --no-local <lane> /tmp/r67int-lane`) was set to `main = ad5b52b0` (BASE), the rev0
counters were extracted byte-identically from `b78f8b8:reports/round-67/`, and claim bytes were
fabricated **in the scratch worktree** (24 rows S805–S828 on 24 hosts with same-page archive
captures, 24 bullets, README index row + counts, rejects S801–S804). Every observation below is
real counter output at `--lands ad5b52b0ab5691358cd38718ab75649dc9916f9a`, not a reimplementation.
The 24-row fixture reaches `CAPTURE PASS`, `HOSTS hosts=24`, `SWEEP PASS`, `TOPIC PASS`, so it is a
faithful stand-in for a competent integration — the failures found are not fixture artefacts.

## HIGH-1 — ACCEPT-C-67 and ACCEPT-CA-67 cannot both PASS at one lands revision (single-revision proof; resolved only by per-claim lands sequencing, which no frozen file declares)

> L1 has since ruled a per-claim lands separation: `A_r` (S801–S804 + r66 dispositions) →
> `A_c` (claim C: only S805–S828 append; C's receipt is stamped here) → `A_ca` (Ca: adds the S829+
> reject rows and the r67 lesson; Ca's receipt is stamped here). I reproduced that sequence
> mechanically against the frozen rev0 counters: at `A_c` content the C predicate prints PASS with
> `appended=28 extra=[]`; at `A_ca` content the same counter prints `APPEND FAIL extra=['S829','S830']`,
> while Ca's D4 prints `opened_today=6` PASS. **The joint predicate is satisfiable as sequenced**
> (conflict class downgraded to a design finding), but three integration gaps remain and are
> recorded as HIGH-1a/1b below. `claims.json` declares one lands command and one `lands` array per
> claim and never names `A_r`/`A_c`/`A_ca`; a verifier re-running C at the round's final tip gets
> FAIL, which is the stale-receipt shape the protocol exists to prevent. The final report must name
> all three shas explicitly.

### HIGH-1a — no leg guards the A_c→A_ca delta: claim C's certified bytes are ungraded at the final lands commit

Ca has no constant or leg that reads the entry or any of the 24 mined rows (`accept-ca.py` constants
and body: `CENSUS, MANIFEST, REGISTRY, LOG, SCORECARD, QUALITY, LESSON, QUOTE_TOOL, SEQ_TOOL,
COUNTERS`; the only claims-data read is the registry's reject rows in D4 and the census's
registry-only validation in D2). Claim C is not re-run at `A_ca` — and by construction it cannot be
(`APPEND` fails there). Therefore everything `A_c` certified can change between the two commits
without any counter objecting. Observed at fixture `A_ca` content:

```
# entry file DELETED, S819 teaches cell rewritten to " TAMPERED teaches at A_ca"
D2 FAIL bad=["census_exit=1 E=[…E12…]"]        # identical to the pre-deletion run (registry-only census)
D4 FAIL bad=["nonunique=[…]", 'rejected_opened_today=0']   # identical; D4 reads rejects only
```

D2/D4 output is byte-identical with and without the entry and with a tampered row, so at the round's
final lands revision the entry may be absent or the rows rewritten and Ca still passes. The
sequencing decision needs a delta leg, e.g. Ca must assert
`git diff --name-status A_c..A_ca -- corpus/knowledge corpus/SOURCES.md` is bounded to the declared
reject-row additions and the lesson, or `A_ca` must re-run C with a corrected append bound.

### HIGH-1b — the frozen instrument has already moved without a claims revision

The lane worktree carries `reports/round-67/accept-ca.py` modified and uncommitted: sha256
`5382ffed…3653c` versus the frozen dry-run `5e8915ac…36118`; the diff is the QUOTES capture-group
fix (`\bS(8[0-2]\d)\b` → `\b(S8[0-2]\d)\b` at line 272). The ruling is "no counter/claims revision",
but the bytes under the predicate are no longer the bytes the base dry-run recorded, and nothing
(see HIGH-3) binds a lands receipt to the frozen sha. Either the claims file records revision 1 with
the new sha, or the pre-wave receipt no longer describes the instrument that will produce the lands
verdict. This is exactly the class the receipt protocol claims to close.

### Single-revision evidence (frozen rev0)

Ca leg D4 requires **six** rejected rows opened `2026-10-24`
(`accept-ca.py:212-236`: `rej_opened_today` counts every 11-cell row with `status=rejected` and
`opened=2026-10-24`, and must be `>= len(R66_REJECTS)+2`). Only four — S801–S804 — are inside C's
append bound. The two additional rejects must carry ids outside `{S801..S828}`:

- S805–S828 cannot host a reject: `ROWS` requires `status == "mined"` for every one of them
  (`accept-c.py:267-268`), and a duplicate line would fail `SET` non-unique.
- Any other new id is by definition in `appended_ids`, and `allowed_new = NEW_IDS | EXTRA_IDS`
  makes it `extra` → `APPEND` FAIL (`accept-c.py:353-358,372`). Even an unused gap id ≤ S800 fails.

The spec instructs exactly this shape: `gen-spec.py:92,96` tell ScoutReject1/2 to mint
`row-S829 … row-S832` with `status 'rejected'`. So following the wave contract makes C fail.

Observed, same fixture, registry differs only by the two reject rows:

```
# variant B (S801-S804 + S805-S828 + S829,S830 canonical rows)
APPEND FAIL missing_old=[] appended=30 extra=['S829', 'S830'] immutable_violations=[]
ACCEPT-C-67: FAIL
D4 PASS bad=[] r66_rejects=4 opened_today=6          # accept-ca
# variant A (reject rows S829/S830 removed)
APPEND PASS missing_old=[] appended=28 extra=[] immutable_violations=[]
ACCEPT-C-67: PASS
D4 FAIL bad=['rejected_opened_today=4'] r66_rejects=4 opened_today=4
```

Consequence: the round cannot honestly record three PASS verdicts; one of C/Ca must be filed FAIL
by construction, and the wave's own taskcall guarantees that outcome. This is the first thing L1
must resolve (re-freeze one counter's bound, or move r67 rejects into the S801–S804 disposition
slots and re-open the r66 frontier ids — a claims-level decision, not an integration choice).

Secondary defect in the same leg: `once` reports **absent** ids under the label `nonunique`
(`accept-ca.py:228-231`; base dry run printed `nonunique=['S801',…]` for rows that do not exist at
base). Also `rej_opened_today` counts *lines*, not distinct ids, so two duplicate lines of one new
reject id satisfy "+2 new first-class rejected rows" for Ca in isolation (only S801–S804 are
de-duplicated).

## HIGH-2 — STAMP passes on a dirty worktree; all measured bytes are uncommitted

`dirty_flag` is computed and printed but is **not** part of `stamp_ok` (`accept-c.py:181-205`), and
`accept-ca.py` never computes it at all (`:98-120`). Entry, registry, README and the SWEEP script
are read from the worktree; only `BASE` bytes and `--lands^{tree}` come from git. The receipt
therefore pins a tree that need not contain the bytes that produced the verdict.

Observed — full PASS with nothing committed and `main == BASE`:

```
# stamped revision: ad5b52b0…   # evaluated revision: ad5b52b0…   # tree: de353b04…
# worktree dirty (tracked): True
STAMP PASS stamped=ad5b52b0 evaluated=ad5b52b0 equal=True tree=de353b04 dirty_tracked=True
… APPEND PASS … SWEEP PASS … TOPIC PASS
ACCEPT-C-67: PASS
```

`de353b04` is the BASE tree; it contains no entry, no S805–S828 row, no README row. The receipt's
identity evidence (revision + tree + counter sha) authenticates bytes that were never measured.
This is the r66 sequencing class inverted: PASS authored outside the lands tree, indistinguishable
in the record. Related: "measured revision" is literally a second `git rev-parse main`
(`accept-c.py:175-188`), identical to "evaluated" by construction, so the protocol records two
revisions plus whatever the worktree happens to hold.

Minimum fix: STAMP must fail on `dirty_flag` (or every content read must go through
`git show <lands>:<path>` with a hash equality against the worktree), and the header must not call
a `rev-parse main` result "measured". **Sequencing note:** the A_r→A_c→A_ca ruling multiplies this
hole by three — each per-claim stamp is only as good as its clone's cleanliness, and C's stamp (the
one that certifies the entry) is precisely the one whose `A_c` clone is easiest to leave dirty,
because nothing downstream looks at C's bytes again (HIGH-1a).

## HIGH-3 — nothing pins the lands counter bytes to the frozen pre-wave counter sha

Both counters print `# counter sha256 (self)` but no leg compares it to the dry-run receipt
(`3e5f1a58…` / `5e8915ac…`); `claims.json` carries no counter-sha field; Ca's `SEQ` leg only greps
three source strings and `mv_rev == lands` (`accept-ca.py:243-250`). A one-line semantic edit that
keeps those strings is invisible to the record:

```
real   : APPEND FAIL … extra=['S829', 'S830']            ACCEPT-C-67: FAIL
mutant : APPEND PASS … extra=['S829', 'S830']            ACCEPT-C-67: PASS   # append_ok = True
Ca SEQ : per-counter string checks pass for the mutant file (only the absent accept-ca copy flagged)
```

Note the mutant's PASS line still *prints* `extra=['S829','S830']` — the evidence of the bypass is
in the receipt and nothing reads it. Ca's own counter is protected by the same string test, so a
weakened accept-ca is equally admissible. **Live instance:** the lane's `accept-ca.py` is already
modified uncommitted (`5382ffed…` vs frozen `5e8915ac…`, HIGH-1b) and no leg can tell. Recommendation:
pin `counter_sha256` for all three counters in `claims.json`/the lands manifest and fail STAMP on
mismatch; keep the mutant selftests as independent evidence.

## MEDIUM-1 — APPEND's mutable-cell allowance is wider than the frozen claim text

The claim leg says "the one declared in-place flip is S753's used-by cell"; the code allows
`status` (c7), `recheck` (c9) and `used-by` (c10) flips on **all 724 base rows**
(`accept-c.py:368-370`). Observed:

```
# base row S100 only: status mined -> rejected, used-by extended to the new entry
APPEND PASS missing_old=[] appended=28 extra=[] immutable_violations=[]
ACCEPT-C-67: PASS
```

So the new entry can be made to appear used-by hundreds of base rows, and base rows can be silently
retired, while the claim text says the registry is append-only apart from S753. Conversely the
immutability guard that does exist works: a `teaches`-cell tamper on S101 yields
`immutable_violations=['S101']` and FAIL. Either narrow the mutable set to exactly `{S753 used-by}`
plus the 4 disposition rows, or restate the claim leg to match the code — the current pair is a
claim/code mismatch that a verifier reading only the claim would not catch.

## MEDIUM-2 — non-canonical row formats carry extra registry rows past C *and* Ca

Both counters match rows with `^\|\s*(S\d+)\s*\|` (`accept-c.py:73`, `accept-ca.py:66`). Rows that
are indented or lowercase are invisible to `SET`, `ROWS`, `CAPTURE`, `APPEND` and to Ca's `D4`.
Observed with a genuinely indented `  | S829 | …` and a lowercase `| s830 | …` appended to the
variant-A registry:

```
SET PASS missing=[] non-unique=[]
APPEND PASS missing_old=[] appended=28 extra=[] immutable_violations=[]
ACCEPT-C-67: PASS
```

`sources-census.sh:619` gates its validate pass on the same shape (`^\|[ \t]*S[0-9]{3,}[ \t]*\|`), so
it cannot catch them either; `sweep.py` audits only the README index. Net: the registry can carry
additional rows (including rejects) that no instrument sees, and Ca can never be satisfied by such
rows. Fix: one shared row parser for counters + census, and fail on any pipe-leading line in the
registry sections that does not parse as a row.

## MEDIUM-3 — the SWEEP leg delegates to an unpinned, forgeable script outside every land set

`SWEEP` shells out to `reports/round-28/readme/sweep.py` in the measured root and trusts the
substring `totals_ok True` (`accept-c.py:386-395`). That file is in no claim's `lands` list and not
under `NOHARM` (which covers only `corpus/knowledge`). Observed: replaced sweep.py with a two-line
stub and deleted an unrelated README index row (`games-play-sport-contests.md`):

```
SWEEP PASS exit=0 totals_ok True
TOPIC PASS entry topic text appears verbatim in the README row
ACCEPT-C-67: PASS        # README index is now 240 rows against 241 files
```

The counter's only README coverage is its own entry's row, so all *other* index drift is guarded
solely by the forgeable delegate. Fix: pin sweep.py's sha (or add `reports/round-28/readme/sweep.py`
to NOHARM), and assert its JSON receipt (`rows`, `files`, `missing_from_index`, `orphan_rows`,
`topic_mismatch`, `header_drift`) numerically instead of string-matching one line.

## MEDIUM-4 — bullets citing the wrong id pass when quotes share three ordered content words

`RESTATE` binds bullet→row only through `ordered_hits(quote_words, bullet_words) >= 3`
(non-contiguous, no rarity weighting — `accept-c.py:128-137,308-321`), and `ONEID` counts only
parenthesized `(S###)`. Two rows with quotes `ancient medicine healing tradition` /
`ancient medicine healing practice` and their bullets semantically swapped, each parenthesized once:

```
ONEID PASS bad=[]
RESTATE PASS bad=[]
ACCEPT-C-67: PASS
```

In a register entry whose subject *is* medicine/healing, topic-generic quote words make this binding
nearly non-discriminating: a bullet about source A can be filed under source B and the counter
certifies it. This is exactly the "cited exactly once / restated" property the claim asserts, so it
is blind-review-only today (the claim lists per-row support as `review_only`). Cheap hardening:
require the bullet to carry a longest common contiguous phrase (≥4 words) with the anchor quote, or
require the *distinctive* quote words (those absent from the other 23 rows' quotes) to appear.

Bare-id prose is likewise uncounted: adding `Prose may cite S829 and S830 and S799 without
parentheses; only (S###) is counted.` to the entry leaves `ONEID PASS` and `ACCEPT-C-67: PASS`, so an
entry can assert references to ids that are not in the claim set (and Ca's `QUOTES` leg only counts
S805–S828 occurrences, it never bounds S829+ mentions in the lesson).

## MEDIUM-5 — ROW= draft→landed drift is structurally invisible (dependency finding)

Rows are drafted at `.ufo/waves/round-67/rows/<SEAT>/row-<SID>.txt` (`gen-spec.py:56-62,92,96`) and
hand-assembled by L1 into `corpus/SOURCES.md` and the entry bullets. **No counter reads
`.ufo/waves/round-67/rows/**`**: the only `.ufo` reads in the three counters are accept-o's
`.ufo/waves/round-67/stage/mut-o` (`accept-o.py:46`) and Ca D1's *round-66* w1 manifest regex
(`accept-ca.py:139-140`). Ca D1 requires tracked round-66 seat reports and does not cover this
round's row fragments. Consequently an id remap, URL swap, quote rewrite, or teaches rewrite between
the reviewed fragment and the landed line is graded by nothing: every leg checks the landed bytes
against each other, never against the draft the attack seats reviewed. This is the r66 "claim bytes
outside the counter's view" pattern at the integration seam.

Fix options (in order of preference): (a) make integration a mechanical transform of the fragments
and commit a `row-file→registry-line` sha256 map that a leg verifies; (b) add the r67 row fragments
to Ca D1's INCLUDE manifest and assert each landed row's live URL and anchor quote appear in its
fragment; (c) at minimum, require the fragment files to be tracked so a verifier can diff them.

## How each attack class is (or is not) caught

| Attack | Caught by | Evidence |
|---|---|---|
| wrong id count (0 or 2 citations) | `ONEID` (`citations != 1`) + `RESTATE` (`bullets != 1`) | fixture: `S819:citations=0, S820:citations=2` |
| foreign id in parentheses `(S829)`/`(S799)` | `ONEID` `out_of_claim_set` | code `accept-c.py:287-289` |
| foreign id in prose without parentheses | **not caught** | observed `ONEID PASS` with S829/S830/S799 in prose |
| canonical reject row S829+ in registry | `APPEND` (`extra`) | observed `extra=['S829','S830']` |
| indented / lowercase extra row | **not caught** by C, Ca, or census | observed `APPEND PASS appended=28` |
| base-row used-by/status/recheck flip | **not caught** | observed `APPEND PASS` on S100 flip |
| base-row teaches/anchor/source/tier flip | `APPEND` (`immutable_violations`) | observed `S101` FAIL |
| uncommitted bytes at a clean-looking lands rev | **not caught** (`STAMP` ignores dirty) | observed PASS with `dirty_tracked=True` |
| weakened counter (keeps SEQ strings) | **not caught** (no sha pin) | observed mutant PASS; Ca SEQ passes its lines |
| forged `sweep.py` + unrelated README drift | **not caught** | observed `SWEEP PASS` against a 2-line stub |
| bullet semantically on row A, citing B | **not caught** when quotes share 3 ordered words | observed `RESTATE PASS`, `ONEID PASS` |
| draft fragment ≠ landed row | **not caught** (no counter reads the fragments) | grep: no `.ufo/waves/round-67/rows` reader |
| entry/rows mutated or deleted between A_c and A_ca | **not caught** (Ca never reads C's bytes; C cannot run at A_ca) | observed identical D2/D4 with the entry deleted |
| counter bytes changed after the pre-wave dry run | **not caught** (no sha pin) | lane `accept-ca.py` already `5382ffed…` ≠ frozen `5e8915ac…` |

## Residual risk / verification gaps

- I did not exercise `accept-o.py` or `tools/check-receipt-seq.py` behaviour beyond confirming the
  bytes sha-match the receipts; `RevCounterO` owns that slice. The no-sha-pin finding (HIGH-3)
  applies to O symmetrically.
- The fixture registry has no `## Registry` section, so `sources-census.sh validate` reports E12 on
  every row; my census claim is therefore limited to its **row-matching regex**, not to a clean
  validate run. Whether census has a second, stricter parser behind that gate is unverified.
- The 24-row fixture is synthetic (example.org hosts, invented quotes); RESTATE/HOSTS/LINK/CAPTURE
  semantics were exercised faithfully by construction, but this is not evidence about the real
  mined rows, which do not exist yet (pre-data).
- All fabricated artifacts live only under `/tmp/r67int*`; the lane, its jj state and its git index
  were not modified. No tools were installed or upgraded (none needed).
- HIGH-1a is supported by two independent observations — `accept-ca.py` contains no reference to the
  entry/claim-C rows at all, and the fixture's D2/D4 output is byte-identical with the entry deleted
  and a mined row rewritten. I did not build a fully green `A_ca` fixture (D1/D3/CRITERION/QUOTES
  need real records), so "Ca would still print PASS" is inferred from the leg inventory, not observed
  end-to-end; the blindness itself is observed.
- The exact fixture and both counter verdicts are reproducible from the commands in §Method; the
  scratch clone remains at `/tmp/r67int-lane` (uncommitted claim bytes, `main = ad5b52b0`, dirty).

## Recommendations (for L1, in order)

1. Make the sequencing explicit in the record: name `A_r`, `A_c`, `A_ca` shas in the final report and
   in each receipt line, and add the missing delta leg (HIGH-1a) — Ca must bound
   `git diff A_c..A_ca -- corpus/knowledge corpus/SOURCES.md` to the declared reject rows + lesson,
   because C cannot re-run at `A_ca` and no Ca leg reads the entry at all.
2. Declare the counter revision: `accept-ca.py` already differs from its frozen bytes (HIGH-1b).
   Record revision 1 with the new sha, or revert before lands; then pin `counter_sha256` for all
   three counters in the lands manifest and fail STAMP on mismatch.
3. Add `dirty_tracked` to STAMP's failure condition (or read all claim bytes via `git show`); a
   dirty per-claim clone otherwise defeats the sequencing ruling for free.
4. Narrow `APPEND`'s mutable set to the declared flips, or amend the claim leg text.
5. Pin `sweep.py` and assert its JSON receipt numerically; extend `NOHARM` to the lands-list paths.
6. Share one row parser across counters/census and fail on unparsed pipe rows; dedupe D4 by id.
7. Bind fragments to landed rows (ROW= manifest with sha map) and strengthen RESTATE to a
   contiguous/distinctive-phrase test.
