# CritCounterVacuity — round-72 w1: vacuity attack on claim C's 10 frozen legs (R71-M13 class)

Seat: `L1Kotodama72.CritCounterVacuity` (critic, leaf — no subagents).
Date: 2026-10-25. Lane: kotodama-shokunin. Claims attacked: `reports/round-72/claims.json` claim C
(current pre-data re-freeze incl. F1–F9/SCOUT-LIVE ledger), legs ENTRIES/ROWS/REPOINTED/GATE/REJECTS/
GROUND/CITEDLINES/CENSUS/SCRATCHMIRROR/COLLCHECK.

Class under test: R71-M13 "vacuous-counter-legs" (round-71 lesson, ## Mistakes): legs that pass when
the substantive work is absent or wrong. Method: five attacks (a)–(e) as assigned, each run against
(a) the frozen leg text and (b) the drafted counter `.ufo/waves/round-72/counters/accept-c.py`
(794 lines, `SELFTEST: 11/11` observed this seat). No lane/fleet bytes mutated; probes built in
`/tmp/CritCounterVacuity/`.

## Verdict up front

**Attack (a) wins: the frozen after-state `ACCEPT-C-72: PASS legs=10/10` is reachable with two
header-stub entries carrying zero body knowledge.** The counter's own clean selftest fixture
(`ENTRY_CANONICAL`/`ENTRY_AMEND`, accept-c.py:620-661) IS a stub (header + 3-item outline body)
and passes 10/10 — the counter canonizes the vacuity it should catch. The other four attacks fail
the claim through ROWS / GATE / REPOINTED / CITEDLINES as designed. Residual vacuities that survive
ALL five attacks (and survive a fully "correct" landing unless receipts are added) are listed in §7.

## 1. Attack matrix

Attack setups assume everything else done properly (registry rows, lesson Gate, receipts), per the
single-variable vacuity method. "fires" = a leg returns FAIL; "survives" = PASS.

### (a) Two entry files are empty stubs with the right header

Setup: both files exist at <lands>; each carries the 9 header field lines (source/verified-at/
recheck/ground/topic/gap filled/sources/couples/scope) with compliant values (`- source: S874/S875`
lines with matching URLs so REPOINTED has something to check), **no body**.

| Leg | Result | Mechanism |
|---|---|---|
| ENTRIES | survives (vacuous) | leg checks field NAMES + non-empty file only (accept-c.py:206-221 `header_field_names`); no value, body, length, or date check. Probed: `LEG PASS ENTRIES` on header-only stubs. |
| ROWS | survives | registry-side; stub files exist so used-by paths validate (CENSUS E11 clean). |
| REPOINTED | survives (vacuous) | universal over `source:` lines only (accept-c.py:259-295); a compliant 1–2 source lines pass; **no body-citation check** (round-71's routed body-citation hardening never landed in the frozen legs). Probed: `LEG PASS REPOINTED`. |
| GATE | survives | lesson-side only. |
| REJECTS | survives | lesson-side only. |
| GROUND | survives | before-only receipt: re-verifies base sweep 0/0 (accept-c.py:374-399); a do-nothing control passes it by construction. |
| CITEDLINES | survives (vacuous) | nothing to find in stubs; clean selftest fixture (no multi-id lines) passes. Probe note: my minimal probe repo lacked `tools/`, tool exit 2 — artifact of the probe, not a leg result; with the tool present, stubs pass (selftest 11/11). |
| CENSUS | survives | used-by paths exist on disk. |
| SCRATCHMIRROR | survives | receipt-side; validates the mirror rows, not entry substance. |
| COLLCHECK | survives | id-list files. |

**Claim passes 10/10 with no knowledge landed.** Counter-proof: `SELFTEST: 11/11`, and the clean
fixture's entries are header + outline. Impacted axis: **coverage — the claim's title promises
"two entries admitted on uncovered ground"; the frozen after-state only promises two files with
nine header lines.** Kill rule does not rescue: stubs' `source:` lines say "fetched 2026-10-25" and
the sources WERE genuinely opened (Gate quotes), so "cited source not opened this round" is not
provable against the lane.

### (b) Registry rows exist, used-by points elsewhere

Setup: S874/S875 appended, mined, but used-by = `—` (variant b1) or another lane file (b2).

| Leg | Result |
|---|---|
| ROWS | **fires both variants** — probed: b1 `used-by out of scope: ['—']` + `used-by empty`; b2 `used-by out of scope: ['…other.md']`. Subset + union checks (accept-c.py:224-257) also catch same-entry-on-both-rows and trailing-junk variants. |
| CENSUS | survives b1 (W03 warning, exit 0); fires only if the path is missing on disk (E11). |
| all others | survive. |

Claim **fails on ROWS alone**. No hardening needed; ROWS + kill rule ("used-by not exactly the
admitted entries") are the load-bearing legs and they hold. (Residual: none observed.)

### (c) Gate quotes are 30 words

Setup: lesson ## Gate pipe rows carry 30-word quoted spans.

| Leg | Result |
|---|---|
| GATE | **fires as drafted** — the counter measures words directly (`len(s.split()) > 25`, accept-c.py:329; selftest `gate_quote` mutant uses a 29-token quote and fails GATE, 11/11 observed). |
| all others | survive. |

Claim fails **if and only if the instrument keeps measuring directly**. Two exposures remain:
(1) `tools/check-gate-quotes.py` is blind to pipe-table rows (0 findings for any length — MutGateQuotes
reproduced on the real round-71 lesson and a round-72-shape fixture); any future re-implementation
of GATE through that frozen tool re-opens the vacuity. (2) "located" is not counter-enforced: a
**fabricated 24-word quote** passes every leg; the F8 kill-rule clause ("located quote") is
judge-adjudicated, not counter-checked.

### (d) Rows appended by arithmetic id shift instead of by document

Setup variants:
- d1: shift coincides with the by-document mapping (e.g. staged S863→S874, S867→S875 by +11).
- d2: shift lands on the wrong document (row S875 carries another URL; entries still cite bunka).
- d3: staged rows appended as-is with only the id rewritten (arithmetic or not).

| Leg | Result |
|---|---|
| d1 | all legs pass — observationally identical to the correct state; a state-based counter cannot encode a process requirement. |
| d2 | **REPOINTED fires** — probed: `cites URL not registered on S875: https://online.bunka.go.jp/...` (accept-c.py URL-match per citation, accept-c.py:283-294). |
| d3 | **CENSUS fires** — staged rows are NF=12 with escaped pipes in the recheck cell (probed on the real staged bytes: `S863/S867/S967 | NF= 12 | escaped pipes: True`) → E01 malformed row; also E09 (recheck cells are prose "180d — `curl …` (ran 2026-10-23)" with a foreign `SOURCES-PROPOSED.md` reference). ROWS used-by subset check fires independently (staged used-by ≠ admitted entries). |

Claim fails for d2/d3; d1 is unstate-checkable and needs a process receipt (§8 R4).

### (e) Entries copied byte-exact from shokuknow, foreign ids left in

Setup: both entries copied verbatim from `/home/vgpnk/Projects/shokuknow/merge/kotodama/...`
(staged bytes; copies at `/tmp/CritCounterVacuity/`).

| Leg | Result |
|---|---|
| ENTRIES | survives (vacuous) — staged headers carry all 9 field labels; `verified-at: 2026-10-23/24` **values pass** (names only). |
| REPOINTED | **fires** — base entry cites S863/S867 (< S874 floor AND lane S863/S867 are UNESCO dance rows whose URLs mismatch ihchina/bunka); amendment cites **S967**: 967 ≥ 874 passes the numeric floor, but the row-existence check fires (`cites S967 with no registry row`, accept-c.py:278-280). The existence check is the load-bearing line; without it S967 sails through. |
| CITEDLINES | **fires on the base entry** — probed on staged bytes: `MULTI-ID …:7 S863,S867` (one recheck line carries both staged ids); `CITEDLINES: 1 finding(s)`, exit 1. Amendment alone would pass (single-id lines only). |
| ROWS/CENSUS/GATE/REJECTS/GROUND/SCRATCHMIRROR/COLLCHECK | survive (registry/lesson/receipt-side). |

Claim fails via REPOINTED + CITEDLINES. **Residual (survives (e) as posed):** re-point the ids but
keep other foreign matter — prose "(S837)" (lane S837 = BBC Sikhism "Five Ks", a false-provenance
citation CITEDLINES cannot see: single id, non-table), `SOURCES-PROPOSED.md`, "round 12's
CANNOT-ANSWER §4.3", couples to nonexistent `calendar-festival-systems.amend-2026-10-24-r10.md`,
and 2026-10-23 fetched-dates — **all 10 legs still pass** (ExecRenumber:1-4 confirms these claims
are unverifiable from lane artifacts). The ExecRenumber drafts at `/tmp/r72-entries/` are clean
(id-closure {S874,S875}, no staged-provenance tokens, verified-at 2026-10-25, couples exist), but
nothing frozen enforces that cleanliness.

## 2. Summary matrix

| Attack | Fires | Survives | Claim verdict |
|---|---|---|---|
| (a) stub entries, right header | — | all 10 | **PASS 10/10 — vacuous** |
| (b) used-by elsewhere | ROWS (both variants) | other 9 | FAIL (as designed) |
| (c) 30-word quotes | GATE (direct count) | other 9 | FAIL — but re-opens if instrumented via check-gate-quotes.py; fabricated ≤25-word quote still passes |
| (d) arithmetic id shift | d2: REPOINTED; d3: CENSUS+ROWS; d1: — | d1 all | FAIL except coincidental d1 (process) |
| (e) byte-exact foreign copies | REPOINTED, CITEDLINES | other 8 | FAIL — but (e)-residual foreign matter passes all 10 |

## 3. Strongest counterexample (local evidence)

`python3 -B .ufo/waves/round-72/counters/accept-c.py --selftest` → `SELFTEST: 11/11`. The clean
fixture's entries are exactly attack (a): nine header lines, a "## Proposed body" outline of three
one-line items (canonical) / one bullet (amendment), no §1–§7 substance, no located quotes, no
couplings prose. The counter's PASS fixture is the vacuity. There is no `stub_body`/`empty_entry`
mutant in `MUTANTS` (accept-c.py:670-681) because there is no body check to mutate. This is the
round-71 pattern verbatim ("four of accept-c.py's seven legs can pass vacuously", round-71 lesson
## Mistakes) recurring in the round-72 counter for the entry-side legs.

## 4. Minimal hardening (frozen legs are NOT editable — receipts, not leg edits)

Routed to the L1; each is a committed receipt the round-72 report names and the judge applies
alongside `legs=10/10`. Floors derive from the actual ExecRenumber drafts (measured this seat):
canonical 635 body words / 7 `##` sections; amendment 206 / 2.

- **R1 (kills (a)) — entry-substance receipt** at `reports/round-72/telemetry/entries-substance.txt`,
  run over `git show <lands>:<entry>` bytes: body word count after the first `## ` (floors: canonical
  ≥400, amendment ≥150), `grep -c '^## '` (≥5 / ≥2), `grep -c '^- verified-at: 2026-10-25$'` (==1 per
  entry), and every `- source:` line contains `fetched 2026-10-25`. Judge criterion: ACCEPT-C-72
  requires legs=10/10 AND this receipt.
- **R2 ((b)) — none.** ROWS is sufficient (probed). Optional: report notes census W03 absent.
- **R3 (kills (c) + locatedness gap)** — gate-quote located/word-count receipt at
  `reports/round-72/telemetry/gate-quotes.txt`: per Gate row, `awk`-measured word count ≤25
  (countersigns MutGateQuotes) AND `grep -cF '<quote>'` against the fetched artifacts
  (`/tmp/r72-entries/ihchina-2020.html`, `ihchina-2026.html`, `bunka.html`) ≥1 each. Also pins the
  GATE leg's instrument: never delegate the word count to `tools/check-gate-quotes.py` (frozen,
  pipe-row blind).
- **R4 (kills (d1))** — by-document mapping receipt: cite `.ufo/waves/round-72/assimilation/
  reg-to-staged.txt` (URL-exact match) + ScoutRegisterMap's independent re-derivation + one line
  asserting S874 = staged S863/S967 document family and S875 = staged S867 **by URL equality, not
  id arithmetic**. d3 needs nothing further (CENSUS E01/E09 probed firing on staged bytes).
- **R5 (kills (e)-residual)** — foreign-provenance closure receipt over the final entries:
  `grep -oE '\bS[0-9]{3,}\b' <entries> | sort -u` ⊆ {S874,S875}; `grep -nE 'SOURCES-PROPOSED|
  CANNOT-ANSWER'` → 0 hits; every backticked `*.md` in `couples:` lines `test -f` on the lane tree.
  Kills S837-class false provenance, dangling couples, and stale fetched-dates by construction.

## 5. Observed live defect (adjacent to vacuity; blocks a clean landing)

The amendment draft at `/tmp/r72-entries/heritage-taxonomy-models.amend-2026-10-24-r13.md` still
states "The live page did not answer this round's fetch (connection timed out … 2026-10-25, one
attempt, 25 s)" and its source line says "live page unreachable from the lane host" — while the
canonical draft says "fetched 2026-10-25 live (HTTP 200, after one initial 25 s timeout)" and the
frozen pre-data ledger entry **SCOUT-LIVE** declares the live page served HTTP 200 on retry.
If landed as-is, the amendment files a false open-statement the 10 legs cannot see (ENTRIES checks
field names only). Smallest correction: L1 updates the amendment draft to the SCOUT-LIVE wording
before integration; add one line to R1's receipt grepping both entries for `unreachable|timed out`
→ 0 hits.

## 6. Tooling

No installs/upgrades. Probes used system `python3` only. Downloads/copies: two staged entry files
copied to `/tmp/CritCounterVacuity/` (named: shokuknow staged
`heritage-taxonomy-models{,.amend-2026-10-24-r13}.md`) for the byte-exact attack.

## 7. Evidence index

- Counter selftest: `SELFTEST: 11/11` (accept-c.py, clean fixture = stub entries).
- Probe legs: ENTRIES/REPOINTED PASS on header-only stubs; ROWS FAIL on used-by `—` and other-path;
  REPOINTED FAIL on wrong-doc S875 (`/tmp/CritCounterVacuity/probe.py`).
- CITEDLINES on staged bytes: `MULTI-ID heritage-taxonomy-models.md:7 S863,S867`, 1 finding, exit 1.
- Staged rows: `S863/S867/S967 NF=12`, escaped pipes present (as-is append → census E01/E09).
- Draft measurements: canonical 635w/7 sections, amendment 206w/2; id-closure {S874,S875};
  couples exist (amendment→canonical coupling resolves once both land).
- Cross-refs: MutGateQuotes.md (tool blind spot reproduced), ExecRenumber.md ([UNVERIFIED-CLAIM]
  flags for staged round-11/12 history), claims.json pre_data_corrections F8/SCOUT-LIVE.
