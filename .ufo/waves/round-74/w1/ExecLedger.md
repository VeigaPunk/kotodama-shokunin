# ExecLedger — draft calibration ledger for round 74 (claim Ca)

Seat `ExecLedger` (leaf executor, hyaku run 7). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
base `f7104cbce186bc2e1522abf0cfd619cc834628bb` (= lane `HEAD`, detached, `ahead=0`). Fleet root read-only.

**Written (only these):**

- `.ufo/waves/round-74/drafts/ledger-draft.json` — 39 453 B, sha256 `1e26536e8a6392a1f46c4ce3e342216c674544f9fca919d4b7bdd8b551f44cb4`
- this report.

Nothing else in the lane or the fleet root was written. The six inherited round-73 w2 worktree files were read
only (sha256 taken; no edit, no commit). Lane `git status --porcelain` before and after this seat is identical
(5 `M` + `RevengerOrigins.md` untracked + the two round-74 dirs). No git state, index, or jj state touched.
No tool installed; `pacman` not run.

---

## 1. What the draft contains

| part | count | note |
|---|---|---|
| `pairs` (BASEMISMATCH-class, red at base, r3-compatible schema) | **14** | ids `LC-01 … LC-14`; 3 `REPAIR`, 11 `ANNOTATE` |
| `content_pins` (the six round-73 w2 files; sha256/absent at base → pinned expected_after) | **6** | `CP-01 … CP-06` |
| `annotate_rows` (proposed `## Corrections — round 74` rows, id + stated token + observed token + re-derivation verbatim) | **11** | one per ANNOTATE pair |
| `grammar_requirements` | 9 | R1–R9; the counter does not exist yet, and three of them are load-bearing (R1, R6, R7) |
| `controls` | 6 | green/duplicate/explicitly-closed sweep lines, kept out of `pairs` |
| `dropped_candidates` | 5 | with the reason each cannot be an honest pair |
| `fleet_pin` | 1 | `dad39efd27988bd28b1fe41f5e327529f0472d3c` (see §7 finding F1) |
| `must_track` | 6 | the six w2 paths |

Base-pinned reads are by full 40-hex; the two counters' receipts are read at `HEAD` because they must be able to
turn green at `<lands>`. Nothing in the file names a claim-C artefact, and no cited row id exceeds S880, so a
SEPARABLE scan at 881 is clean (verified mechanically, §5).

## 2. Pairs — rationale table

`stated → observed` is the parsed token of the statement's own text at base (`stated_parse`) against the token the
`observe_cmd` prints **at base, now**. Every row below was executed; outputs in §4.

| id | stated_at | stated → observed | disp | why (short) |
|---|---|---|---|---|
| LC-01 | `SHONEN.md:6` | `412` → `804` | REPAIR | Box 1 is the only statement of registry size; 412/367/35/10 is the round-56 figure (exact at `c8af23f`), base is 804 rows (last id S880). SHONEN is not append-only. The repair must state the **dated** figure "804 rows after round 73 — 709 mined, 58 queued, 37 rejected"; a "latest" figure would move with claim C's four new rows and destroy the base pin. |
| LC-02 | `LOG.md:4297` | `9` → `10` | ANNOTATE | Freeze bullet says "Ca 9 scenarios"; counter r3 prints `SELFTEST OK: 10 scenarios` and the committed r3 receipt says 10. True only of the freeze-time r1 receipt. LOG is append-only. |
| LC-03 | fleet `kotodama.md:10` | `9` → `10` | ANNOTATE | Second site of the same drift, in the fleet report. The lane cannot edit the fleet tree; only a lane-side row can name it. The "C 29/29" half of the sentence is true and is not attacked. |
| LC-04 | `SCORECARD.md:1430` | `PASS legs=11/11` → `0` | ANNOTATE | The row asserts a PASS-at-lands, but the committed round-73 telemetry holds **zero** PASS verdict lines (4 verdict lines total, all FAIL controls). After-state is a committed receipt, not a text edit. |
| LC-05 | `SCORECARD.md:1431` | `PASS legs=9/9` → `0` | ANNOTATE | Same absence for the Ca counter (r3). Reproducing PASS needs the clone's local `main` **at** `2d1cd91` (STAMP compares `measured` = main tip with `--lands`); elsewhere the same command prints `FAIL legs=8/9`. |
| LC-13 | `LOG.md:4301` | `PASS legs=11/11` → `0` | ANNOTATE | The standing LOG record states the same unreceipted PASS. |
| LC-14 | `LOG.md:4301` | `PASS legs=9/9` → `0` | ANNOTATE | Same line, Ca half. |
| LC-06 | `corpus/README.md:732` | `243` → `247` | ANNOTATE | First totals footer; round-73 L01's `245` is pin-correct and now stale (base 247). Live footer `:775`. |
| LC-07 | `corpus/README.md:736` | `243` → `247` | ANNOTATE | First counts-checked vector; round-73 L03 pinned 245. Live vector `:777` = 32/29/38/29/24/95. |
| LC-08 | `corpus/README.md:344` | `30` → `32` | ANNOTATE | `## linguistics/ (30)` was never in any ledger; round 73 took it to 32. README mentions the same two entries at `:768`, so an in-place repair would leave a second stale site. |
| LC-09 | `SKILL.md:594` | `94` → `95` | REPAIR | Live-false in the corpus map since round 56; `corpus/README.md:503` already says `(95)`. Needs the SKILL.md in-place span widened (§6). |
| LC-10 | `SKILL.md:594` | `92` → `93` | REPAIR | Second token on the same line: 95 = 93 bases + 2 `*primary-sources.md` maps. Split from LC-09 so a half-repair cannot pass. |
| LC-11 | `corpus/lessons/round-73.md:38` | `23443` → `97656` | ANNOTATE | The Gate paragraph calls the durability capture a shell that does not carry the span; 23443 is the gzip wire size, the decoded payload is 97656 B and does carry it. The registry row carrying the same falsehood **cannot** be the pair: `stated_at` would name a claim-C artefact and the SEPARABLE scan reads the whole ledger (§7 F3). |
| LC-12 | `reports/round-73/claims.json:11` | `no` → `two` | ANNOTATE | The frozen round-73 claims file grounds a cut row on "no Wayback capture of the same page"; the same round's lesson was repaired to "HAS two status-200 Wayback captures" (20241106195515, 20241107004043) and no correction row names the claims file. Frozen bytes are not rewritten. |

Mandatory coverage as assigned: (a) the 9-vs-10 scenario drift → LC-02 (LOG) + LC-03 (fleet report); SCORECARD has
**zero** occurrences of "scenarios" (measured, control K4), so the "SCORECARD/LOG/fleet report" sweep is closed
explicitly rather than narrowed silently. (b) PASS legs for both round-73 counters → LC-04/LC-05 (SCORECARD) with a
grep count of 0 against an expected 1, plus LC-13/LC-14 (LOG). (c) the six w2 files → §3. (d) SHONEN 412 → LC-01
(REPAIR, decided). (e) README footers → §8 (the last footer is live, so it is a **control**, not a pair; the stale
sites are LC-06/LC-07/LC-08).

## 3. Content pins (the six round-73 w2 files)

Byte facts measured at base vs the inherited worktree (blob ids are git object names, sha256 is the same content
under a second hash; both recorded so the counter can check without checkout-filter worries):

| id | path (`.ufo/waves/round-73/w2/…`) | base | worktree = `expected_after` | bytes |
|---|---|---|---|---|
| CP-01 | `CritEntryAmendFinal.md` | `sha256 246de174…` / blob `eeb33447` | `sha256 290a6ccd…` / blob `d219fca4` | 41 013 |
| CP-02 | `ExecSelftestAll.md` | `sha256 0d24aeed…` / blob `20df0f0b` | `sha256 dfc8fe0d…` / blob `9f887fd9` | 37 204 |
| CP-03 | `ScribeLogScorecard.md` | `sha256 f4f14669…` / blob `7fd5ae05` | `sha256 db254d88…` / blob `36c7b31b` | 23 535 |
| CP-04 | `SimplifierEntries.md` | `sha256 985dd883…` / blob `5afdac54` | `sha256 9469d4d6…` / blob `c0fbaa9e` | 20 039 |
| CP-05 | `drafts/log-entry.md` | `sha256 01d50325…` / blob `3e9af53d` | `sha256 079728a5…` / blob `5ca8eedd` | 10 810 |
| CP-06 | `RevengerOrigins.md` | **absent** (`git rev-parse <base>:<path>` → fatal) | `sha256 7d145919…` / blob `2c1c9cd8` | 26 043 |

`observe_cmd` for CP-01…CP-05 is `sha256sum <path>` in the graded checkout (red at base: the base hash differs from
the pin); for CP-06 it is `git ls-tree -r --name-only HEAD -- <path>` (red at base: empty output, recorded as the
sentinel `absent`). My numbers were taken independently and agree with wave-1 `ScoutLedgerSweepC` §1 cell for cell.
`must_track` carries the same six paths.

Why pins and not pairs: there is no document statement whose *token* could be compared to a content hash — a
word-versus-hash "mismatch" is trivially red and worthless. Grading them as content pins keeps the BASEMISMATCH
leg honest and still makes the six files a hard after-state (R6).

## 4. Evidence at base (exact argv → output)

Every command below was run with cwd = a materialised base checkout
(`/tmp/ExecLedger/clone`, `git clone --shared` of the lane, `checkout --detach f7104cb…`, `HEAD` verified).

```
$ git grep -h -o -E 'Registry: 799 → 804 rows' f7104cb… -- corpus/README.md
Registry: 799 → 804 rows                                            [rc=0]   → 804  (LC-01)

$ git grep -h -o -E 'SELFTEST OK: [0-9]+ scenarios' f7104cb… -- reports/round-73/telemetry/selftest-r3.txt
SELFTEST OK: 10 scenarios                                           [rc=0]   → 10   (LC-02, LC-03)

$ git grep -c -E '^ACCEPT-C-73: PASS legs=11/11$' HEAD -- reports/round-73/telemetry
                                                                    [rc=1, empty] → 0  (LC-04, LC-13, R1)
$ git grep -c -E '^ACCEPT-CA-73: PASS legs=9/9$' HEAD -- reports/round-73/telemetry
                                                                    [rc=1, empty] → 0  (LC-05, LC-14, R1)

$ git grep -n -E 'ACCEPT-(C|CA)-73: [A-Z]+' HEAD -- reports/round-73/telemetry
HEAD:reports/round-73/telemetry/controls-c.txt:39:ACCEPT-C-73: FAIL legs=1/11
HEAD:reports/round-73/telemetry/controls-ca-r2.txt:41:ACCEPT-CA-73: FAIL legs=4/9
HEAD:reports/round-73/telemetry/controls-ca-r3.txt:41:ACCEPT-CA-73: FAIL legs=4/9
HEAD:reports/round-73/telemetry/controls-ca.txt:41:ACCEPT-CA-73: FAIL legs=5/9
                                                              (control K6: exactly 4 verdict lines, all FAIL)

$ git diff --shortstat 4b825dc… f7104cb… -- 'corpus/knowledge/*.md'
 247 files changed, 43426 insertions(+)                                   (LC-06, LC-07)
$ git diff --shortstat 4b825dc… f7104cb… -- 'corpus/knowledge/linguistics/*.md'
 32 files changed, 5689 insertions(+)                                     (LC-08)
$ git diff --shortstat 4b825dc… f7104cb… -- 'corpus/knowledge/civilizations/*.md'
 95 files changed, 18546 insertions(+)                                    (LC-09)
$ … same pathspec plus ':(exclude)*primary-sources.md'
 93 files changed, 18198 insertions(+)                                    (LC-10)

$ git grep -h -o -E 'gzip.decompress -> 23443 -> [0-9]+ bytes' f7104cb… -- .ufo/waves/round-73/w2/ScoutReopenS879.md
gzip.decompress -> 23443 -> 97656 bytes                             [rc=0] → 97656 (LC-11)
$ git grep -h -o -E 'HAS two status-200 Wayback captures' f7104cb… -- corpus/lessons/round-73.md
HAS two status-200 Wayback captures                                 [rc=0] → two   (LC-12)
```

Statement anchors were verified line by line (`git grep -n -F`): `SHONEN.md:6`, `LOG.md:4297`, `LOG.md:4301`,
`SCORECARD.md:1430`, `SCORECARD.md:1431`, `corpus/README.md:344/732/736`, `SKILL.md:594`,
`corpus/lessons/round-73.md:38`, `reports/round-73/claims.json:11`; the fleet line at
`dad39efd:.ufo/reports/round-73/kotodama.md:10`. Per-directory counts 32/29/38/29/24/95 = 247 reconcile with
`corpus/README.md:777`; last footer `:775` `Total knowledge entries: 247.` is live (control K1).

Mechanical re-check (scratch, `/tmp/ExecLedger/check.py`): 14/14 pairs red **and** observable at base,
6/6 pins red, 11/11 rows contain stated token + observed token + the exact re-derivation string, 0 problems.
`reports/round-28/readme/sweep.py` run on the base checkout prints `totals_line 243 totals_ok False`,
`footer_live 247`, `footer_ok False` and **exits 1** (baseline for R4).

## 5. After-state proof (fixture, not the lane)

Because the counter does not exist yet, I proved the *shapes* can turn green: fixture repo
`D=$(mktemp -d /tmp/ExecLedger/lands.XXXXXX)` → `git init -q`, `rev-parse --show-toplevel == $D` verified before the
first commit, base tree extracted into it, the three REPAIR edits and the two receipts applied, the six worktree
files copied in, one commit with a throwaway identity **inside `$D` only**, then `git fetch` of the base commit so
the base-pinned argv resolve (a counter that clones history gets this for free — a fixture built by `git archive`
alone does not, which is worth knowing).

Result (`/tmp/ExecLedger/lands_check.py`), 0 problems:

- LC-01 → `statement_after` = 804 = lands observation, ≠ base statement 412 → REPAIR green.
- LC-09 / LC-10 → 95 / 93, ≠ 94 / 92 → REPAIR green.
- LC-04/05/13/14 → `1` (was 0); all base-pinned pairs unchanged at lands (LC-02/03/06/07/08/11/12 still 10/10/247/247/32/97656/two).
- CP-01…CP-06 → each `sha256sum` equals `expected_after`; CP-06 prints the path.

## 6. What the counter must freeze before data (R1–R9, condensed)

- **R1 absence semantics** — `git grep -c|-l` exit 1 with empty stdout = **zero matches**, token `"0"`; anything
  else empty+nonzero stays *unobservable*. Without this, LC-04/05/13/14 are unobservable and the BASEMISMATCH leg
  (which fails on any unobservable pair) cannot pass. Selftest: one present pattern → count, one absent → `0`.
- **R2 allowlist** `{git, grep, wc, sha256sum}` — drop `python3` (round-73 survivor: constant printers). Counting
  idiom: `git diff --shortstat <empty-tree> <rev> -- '<glob>'`.
- **R3 revision discipline** — after-state reads use `HEAD`/repo-relative paths; base reads pin the full 40-hex.
  Reject a mutable ref in place of the base hash.
- **R4 last occurrence** — `(?s).*PATTERN` for statement re-reads (two footers in `corpus/README.md`; `sweep.py`
  exits 1 on this tree for reading the first).
- **R5 fleet stated side** — `stated_at` of the form `fleet:<path>:<line>` plus `stated_fleet{path,line,pin,sha256}`;
  branch **before** the lane `path:line` check; resolve via `git -C <fleet_root> show <pin>:<path>`; also assert the
  report bytes at fleet HEAD equal the pin with zero removed lines.
- **R6 CONTENTPIN leg** — lands must equal `expected_after`, base must differ (absence = sentinel `absent`);
  a pin green at base is dropped, never kept.
- **R7 make the drop rule a leg** — FAIL if *any* pair or pin is green at base. Round 73 only demanded
  `mismatched >= min_pairs`, so green pairs could ride along while the claim says "every pair red".
- **R8 SEPARABLE operand** — keep the whole-ledger scan; freeze the separator to the lowest id the coverage claim
  appends this round (read it from the frozen claim; 876 is round 73's number and would let this round's own rows be
  cited). This draft cites nothing above S880 and names no claim-C artefact.
- **R9** counter constants from the frozen commit, not the graded tree (round-73 survivor 1).

**In-place spans (blocking for LC-09/LC-10, and recommended for LC-01).** The round-73 `APPENDONLY` guard allows
SKILL.md hunks only inside *§Gates and probes*; `SKILL.md:594` sits in *§Corpus map* (`## Corpus map`, lines
578–601 at base), so the repair would fail the leg. Make the SKILL.md span a **list** (`§Gates and probes` +
`§Corpus map`), and add `SHONEN.md` to the in-place path set with an explicit box-1 span (`footer_range()` degrades
to the whole 15-line file). Documented fallback if the L1 prefers the single span: reclassify LC-09/LC-10 as
ANNOTATE and drop the SKILL.md edit; LC-01 must stay REPAIR.

**Receipts the after-state needs** (named in `receipts_required`): `reports/round-73/telemetry/pass-at-lands-c.txt`
and `pass-at-lands-ca.txt`, each with `stamped=evaluated=measured=2d1cd9140d3a6c42296d71e4f29587582a4a88c0`, the
command line, and the verdict line. The Ca one must be produced in a clone whose local `main` is **at** `2d1cd91` (wave-1 `ScoutLedgerSweepB` row 3 measured `FAIL legs=8/9` otherwise; this seat did not re-run the r3 counters).

## 7. Findings for the L1 (inherited-instrument defects)

- **F1 — round-73's `fleet_pin` cannot carry round 73's statement sites.** `80d8c9b5…` does not contain
  `.ufo/reports/round-73/kotodama.md` (`git show` → fatal); it holds only the round-72 report, which is why the r3
  counter's constant is `FLEET_R72_REPORT`. The draft pin is `dad39efd27988bd28b1fe41f5e327529f0472d3c` (the commit
  that added the report; blob `d104dfa4…`, sha256 `000bab3a…`), an ancestor of fleet HEAD, bytes unchanged at HEAD
  (measured twice, fleet HEAD moved from `dd51f523` to `ebccb441` during this seat — the fleet repo is live).
- **F2 — the APPENDONLY SKILL.md span blocks a live-false count.** See §6.
- **F3 — the SEPARABLE scan is a string scan over the whole ledger**, so a pair cannot even *name* a claim-C file in
  `stated_at`; a base-pinned read of one is indistinguishable from a dependency. Consequence: the false registry-row
  text for S879 can only be paired at its second site (LC-11). Either freeze that consequence in the claim's wording
  or narrow the operand.
- **F4 — r3's BASEMISMATCH has no "all pairs red" condition** (R7).
- **F5 — r3's absence blind spot** (R1) is the reason a "no receipt exists" defect was unrepresentable in round 73
  at all; R1 plus a red-before receipt closes it.
- **F6 — index completeness is a real defect with no honest pair**: 245 index rows vs 247 files (2 heritage entries
  never indexed, 2 conlang rows mis-attributed to the civilizations section; `sweep.py` prints
  `missing_from_index 4 / orphan_rows 2`). No numeric statement contradicts it, so it stays out of `pairs`
  (`dropped_candidates`); it still needs the two appended rows plus a correction row naming `corpus/README.md`.

## 8. Controls and dropped candidates (why a mandatory site is *not* a pair)

| control | observed at base | kept out because |
|---|---|---|
| K1 `corpus/README.md:775` `Total knowledge entries: 247.` | 247 = 247 | **green** — the mandatory "last footer is live" item, dropped under the drop rule; kept as a control (after claim C the live count is 249, so the last-footer read must be re-done) |
| K2 `corpus/README.md:777` vector | 32/29/38/29/24/95 | green (reconciles with the six per-directory counts) |
| K3 `corpus/README.md:407` `(36)` | 38 | red but **already annotated** by round-73 L02 with the identical token pair → duplicate, not re-paired |
| K4 "scenarios" in SCORECARD | 0 matches | nothing to pair; closes the mandatory sweep explicitly |
| K5 `SKILL.md:704` `10 scenarios` | 10 | already repaired in round 73 |
| K6 round-73 verdict lines | 4, all FAIL | baseline proving any later PASS line is the receipt |

Dropped as pairs: registry row S879 (SEPARABLE, F3); README revision blocks `753→776` / `752→776` (same SEPARABLE
problem, and they are historical-as-filed notes); README index completeness (F6); fleet `:3` lane-HEAD
`ls-remote` parenthetical (needs the network) and fleet `:13` "RevengerOrigins returned no report" (true of committed
bytes at base — becomes false only after landing, so it is not red at base; the content pins record the change);
`SKILL.md:703` "measured 10/11" (environment artefact — a clone outside the fleet tree loses the census script —
and unreceipted).

## 9. Sweep inputs

Wave-1 sweeps existed when I finished and were used as input (never trusted): `ScoutLedgerSweepA` (M4→LC-01, M2→LC-08,
M1→F6, M3→R4+K1, M8/M9 dropped), `ScoutLedgerSweepB` (rows 1→LC-02, 2→LC-03, 4→LC-04/05/13/14, 8→LC-09/10,
3→receipt caveat, 6→truncated-receipt note; rows 5/7/9/28 rejected with reasons), `ScoutLedgerSweepC`
(its LC-01…LC-16 re-mapped to LC-01…LC-12, G1→R1, G2→R2, §1 pin table→`content_pins`, independently re-measured:
identical values; LC-04/LC-16 rejected). Per-row mapping is stored in the draft's `sweep_inputs`.

## 10. Honest limits (what is *not* verified)

- No round-74 counter exists; nothing here was run through `accept-ca.py`. My two checkers
  (`/tmp/ExecLedger/check.py`, `lands_check.py`) reimplement the r3 leg arithmetic for the pair shapes only.
- I did **not** run the round-73 counters or their selftests (no receipt duty in this seat; `SELFTEST: 29/29` is
  therefore cited as wave-1 evidence, not as my run). I did not re-fetch anything live: no page, no Wayback probe,
  so no User-Agent applies to this seat.
- The six worktree sha256 are pins of the *current* worktree bytes; if a seat touches those files before the
  integrator commits them, the pins go stale and must be re-taken **before freeze**, not after.
- `/tmp` was 100 % full when this seat started; a full clone failed (`No space left on device`) and I used
  `git clone --shared` (alternates) instead — 171 MB. Scratch under `/tmp/ExecLedger/` (`clone/`, `lands.*/`,
  `build.py`, `check.py`, `lands.sh`, `lands_check.py`, `sweep.out`) is disposable.
