# MutEntry — mutation probe of the scent entry against `reports/round-66/accept-c.py` (ACCEPT-C-66)

Seat: mutation-tester, wave w1, round 66 (hyaku run 5). Lane base `94209e8f8096…b8616`.
Target instrument: `reports/round-66/accept-c.py`, sha256 `0726b4bc99eefe05a81c92cb6fd1bb3819a041b68679466aa6278350c19dda86`
(frozen pre-data counter; identical hash before and after this probe). Detector = the unmodified
counter, run exactly as the claim declares: `python3 -B reports/round-66/accept-c.py --root .`.

Assigned mutants, all on the entry's smallest behaviour-bearing points:
1. one bullet's citation id changed to a base registry row (S750);
2. one bullet deleted;
3. the `- topic:` line paraphrased.
Plus one in-scope loophole probe (**M3b**): topic line truncated to a proper prefix of the README
index text.

## Dependency finding (read this first)

**The real entry had not landed inside my 15-minute box.** At every check (start, +6 min, +12 min,
+14 min) `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` was absent in the lane
and `corpus/SOURCES.md` carried only S1–S776 (`grep -c '^| S\(7[7-9][0-9]\|800\) '` → 6, i.e.
S771–S776). A bounded watcher polled the entry + the `| S800` row every 5 s for 450 s and ended
`NOT-LANDED after 450s`; a post-watcher check at +20 min was still absent (rows count unchanged, 6).
No scribe draft existed under `.ufo/waves/round-66/` either (`find … -name '*scent*'` → empty;
only `w1/ScribeEntrySpec.md`, a spec with no entry bytes). So the three assigned mutants could not be applied to real entry bytes within the box.

To still answer the assigned question with measured, not asserted, evidence I ran the **same frozen
counter** (same sha256) on a **contract-faithful fixture entry** in an isolated scratch copy of the
lane, and I report the per-leg deltas (mutated minus baseline). The legs under test read only three
things: the entry file, `corpus/SOURCES.md` rows S777–S800, `corpus/README.md` + `sweep.py`. The
fixture reproduces all three, so the catch set transfers verbatim to the real entry; the exact
`S###` ids in the details will differ. **Replay recipe is at the bottom — the L1 should run it on
real bytes after integration; if any leg below fails to move there, treat this report as superseded.**

## Method (same detector on pristine, mutated, restored bytes)

- Scratch clone (mine, disposable): `.ufo/waves/round-66/w1/mut-entry-scratch/` — `rsync -a` copy of
  the lane (`corpus/`, `tools/`, `.git/`, `reports/round-28`, `reports/round-66`; `out/` and the
  sibling 447 MB `reports/` tree excluded). `git rev-parse main` inside it = `94209e8f8096…b8616`.
  The lane itself was only ever read; no lane file, jj state or Git index was written.
- Fixture land state: 24 registry rows S777–S800 cloned from base rows S750–S773 (11 cells, kind,
  tier A/B, `mined`, `2026-10-24`, used-by the entry, distinct live URL + `web.archive.org/web/…id_/`
  capture), 24 bullets each carrying ≥3 in-order words of its row's anchor quote plus one novel
  word, `- topic:` line, README index row carrying the topic verbatim.
- Detector parity check: run on the scratch **before** any fixture bytes, the counter printed the
  fresh `sha256 0726b4bc…` and legs byte-identical to
  `reports/round-66/telemetry/dry-run-c.txt` (`FILE FAIL unreadable …`, `SET FAIL missing=[S777…S800]`,
  `ONEID/RESTATE/HOSTS/CAPTURE/TOPIC FAIL`, `ROWS/LINK/APPEND/NOHARM/SWEEP PASS`, `ACCEPT-C-66: FAIL`).
  Same instrument, same readings → the harness is the frozen counter, not a lookalike.
- Fixture baseline (mutant reference state), entry sha256
  `71394e0b2cee0c19ff01dab182f0b86d5015fbda0175d461fbe8907a6f1c0e7b`:
  `FILE/SET/ONEID/RESTATE/TOPIC/CAPTURE/HOSTS/APPEND/NOHARM PASS`; `ACCEPT-C-66: FAIL` on
  `ROWS` (used-by still names the games entry in the cloned rows), `LINK` (cloned live URLs collide)
  and `SWEEP` (README *footer totals* still `239`/`32` — I did not rewrite the counts footer).
  Those three are **baseline failures by construction and are excluded from every delta below**;
  `SWEEP`'s *topic* sub-check is measured separately as `topic_mismatch <n>` — baseline `0 []`.

## Results (per-leg, mutated vs baseline)

| mutant | mutated bytes | legs that moved to FAIL | legs that stayed PASS | verdict |
|---|---|---|---|---|
| **M1** citation → base row | `(S784)` → `(S750)` (first bullet of §1) | `ONEID FAIL bad=['S784:citations=0']`, `RESTATE FAIL bad=['S784:bullets=0']` | `FILE SET ROWS CAPTURE HOSTS APPEND NOHARM TOPIC`, `SWEEP topic_mismatch 0` | **KILLED** (2 legs) |
| **M2** bullet deleted | line `- … comparanda note. (S795)` removed (lines 38→37) | `ONEID FAIL bad=['S795:citations=0']`, `RESTATE FAIL bad=['S795:bullets=0']` | `FILE SET ROWS CAPTURE HOSTS APPEND NOHARM TOPIC`, `SWEEP topic_mismatch 0` | **KILLED** (2 legs) |
| **M3** topic paraphrased | `- topic:` → `olfaction as social code: how scent materials, blends, and incense mark status, ritual, and memory in a fictional setting.` | `TOPIC FAIL`, `SWEEP topic_mismatch 1 ['culture-material/scent-perfume-aromatics-codes.md']` | `FILE SET ROWS ONEID RESTATE CAPTURE HOSTS APPEND NOHARM` | **KILLED** (2 legs) |
| **M3b** topic truncated to prefix | `- topic: scent, perfume, aromatics and incense` | `SWEEP topic_mismatch 1` | **`TOPIC PASS`** (substring test satisfied), `FILE SET ROWS ONEID RESTATE …` | **KILLED by SWEEP only** — coverage finding 2 |

Raw mutant verdict lines: `ACCEPT-C-66: FAIL`, exit 1, for all four (same as fixture baseline, since
it starts from a baseline with three fixture failures — the kill signal is the **delta**, listed
above, not the verdict line). For M1/M2 the counter's leg *set* is a strict superset of baseline by
exactly `{ONEID, RESTATE}`; for M3 by `{TOPIC}` plus the `topic_mismatch 0→1` change inside `SWEEP`;
for M3b by only the `topic_mismatch 0→1` change.

Restoration evidence (exact bytes, verified per mutant, before and after):

```
entry sha256 before each mutant : 71394e0b2cee0c19ff01dab182f0b86d5015fbda0175d461fbe8907a6f1c0e7b
entry sha256 after  restore     : 71394e0b2cee0c19ff01dab182f0b86d5015fbda0175d461fbe8907a6f1c0e7b  (M1, M2, M3, M3b — all restored_ok True)
pristine counter sha256          : 0726b4bc99eefe05a81c92cb6fd1bb3819a041b68679466aa6278350c19dda86 (unchanged: I never edited the instrument)
```

## Which accept-c legs catch each (the assigned answer)

- **M1 (citation id → base row S750): `ONEID` + `RESTATE` only.** `ONEID` because S784 now has
  `citations=0`; `RESTATE` because `bullets(S784)=0`. Nothing else moves: no leg reads the *set* of
  ids a bullet cites beyond counting new ids exactly once, so **citing a base row is nowhere
  forbidden** — a second body sentence `(S750)` would be accepted (and is legitimate: the SWEEP/APPEND
  legs are registry-side, not entry-side).
- **M2 (bullet deleted): `ONEID` + `RESTATE` only.** Same detail shape. There is **no minimum bullet
  count, word budget, or register-coverage leg** — the deletion is caught solely because the deleted
  bullet was that id's single citation. Consequence (analytic, not run): delete a bullet *and* re-inject
  its id into a rebuilt line carrying ≥3 of that row's quote words + a novel word, and both legs go
  back to PASS — the counter proves *anchor presence*, never *claim identity*.
- **M3 (topic paraphrased): `TOPIC` + `SWEEP`.** `TOPIC` fails because the new text is not a substring
  of the README row; `SWEEP` fails with `topic_mismatch 1` because sweep compares the `- topic:` text
  for **exact equality** against the index row.

## Findings (coverage gaps this probe proves — report, not contract change)

1. **`TOPIC` is a substring test, not an equality test; the equality is delegated to `SWEEP`.**
   `accept-c.py` does `tline[len("- topic:"):].strip() in row`. Proven by M3b: a topic line truncated
   to `scent, perfume, aromatics and incense` makes `TOPIC PASS` while `SWEEP` (exact equality) is the
   only leg that notices (`topic_mismatch 1`). So if a round ever weakens/stubs/skips the SWEEP leg —
   round-66's own `MutCounterC` seat had to stub sweep for its fixtures, and the O claim's bounded
   modes skip work by design — **the topic can be silently narrowed to any prefix of the README row
   and C still stamps PASS.** Fix direction (not mine to make): make `TOPIC` compare equality or
   require `row` to end with the topic text, and keep SWEEP as the second, independent check.
2. **Both M1 and M2 are single-class kills.** The only entry-body semantic guard is `RESTATE`, and its
   tests are quote-word presence (≥3), a coverage ceiling (<0.8 of teaches), and one novel word. An
   entry whose bullets are *only* quote words plus filler passes by construction (the fixture proves
   it: bullets are exactly `" ".join(quote_words[:12]) + " comparanda note"` and `RESTATE PASS`). C
   therefore certifies "each row's anchor is restated", not "each row's teaches content is carried".
   This is why the claim's `review_only` list ("blind per-row support of the 24 new sources") is
   load-bearing and cannot be discharged by the counter.
3. **`NOHARM` and `APPEND` are vacuous on a tree whose lands are not yet committed.** In the scratch
   (`main` == BASE) the counter printed `APPEND PASS missing_old=0 appended=0` while `corpus/SOURCES.md`
   carried 24 appended rows in the working tree, and `NOHARM PASS diff=[]` while the entry file
   existed. Both legs read refs (`git diff BASE main`), while `FILE/SET/ROWS/ONEID/RESTATE/TOPIC`
   read the working tree. **A predicate stamp taken on the L1's uncommitted integration tree is a
   false stamp**: the two legs that carry the "append-only / no-harm" guarantees cannot fail there.
   ACCEPT-C-66 must be run only after the lands commit exists on `main`.
4. **`measured revision` follows the process CWD, not `--root`.** `accept-c.py` calls
   `git rev-parse main` with no `-C root`/`cwd=root` (all other git calls use `git -C root`). Decisive
   measurement: `cd /tmp && python3 -B …/accept-c.py --root …/mut-entry-scratch` prints
   `# measured revision (lane main): unresolvable` while every leg still reads the overlay and
   `FILE PASS`. So any counterfactual/overlay run (O's separation mode, a receipt taken with `--root`
   pointing at a copy) stamps a revision that is *not the tree it measured*. Directly relevant to
   Ca's D2 leg ("that commit's parent equals the receipt's stamped measured revision") — a receipt
   can be internally consistent and still name the wrong tree. Fix direction: `git -C root rev-parse main`
   (one line), or refuse to print legs when the revision is unresolvable.

## Cross-check against the entry spec (only artifact present at my deadline)

`w1/ScribeEntrySpec.md` exists at +17 min (spec only — no draft bytes anywhere under
`.ufo/waves/round-66/`), and its own preflight already enumerates `h1=1`, `h2≤16`, `h3=0`,
`- topic:`, 24 `SLOT S777…S800` markers, zero `(S` outside the 24 slots, and
"sweep.ROW_RE matches the produced index row and its captured topic equals the entry's `- topic:`".
Two observations:
- The **spec's preflight** is the equality check that kills M3b; **`TOPIC` in the frozen counter is
  not** (finding 1). A scribe checking only `TOPIC`-shaped substring logic would let M3b through; the
  spec as written would not. Keep both, and do not let the preflight substitute for `SWEEP` in the
  predicate (the predicate is `accept-c.py` only).
- The spec's bullet targets (`quote_words=6 teaches_cov≈0.38 novel=5`, three distinct quote words)
  sit comfortably inside `RESTATE`, which confirms finding 2 is a *counter* ceiling, not a spec
  defect: the counter would still pass a bullet built only from quote words + filler.

## Replay on real bytes (for the L1, after the entry + S777–S800 land)

```sh
SCR=.ufo/waves/round-66/w1/mut-entry-scratch      # already a lane copy with .git and main==BASE
rsync -a corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md \
         "$SCR/corpus/knowledge/culture-material/"
rsync -a corpus/SOURCES.md corpus/README.md "$SCR/corpus/"
cd "$SCR"
python3 -B reports/round-66/accept-c.py --root .            # baseline (expect all legs PASS)
# M1: first bullet's (S78x) -> (S750)     expect ONEID + RESTATE FAIL
# M2: delete one bullet line               expect ONEID + RESTATE FAIL
# M3: reword the - topic: line             expect TOPIC FAIL + SWEEP topic_mismatch 1
# restore, re-sha; do not commit in the lane
```

(README sync is `corpus/README.md`; the two-word rsync above lists it for brevity's sake — use
`corpus/README.md`. The scratch also needs `reports/round-66/` and `reports/round-28/`, both present.)

## Lane hygiene

- Writes: only `.ufo/waves/round-66/w1/mut-entry-scratch/` (my disposable scratch) and this report.
  No lane source file edited, no `git`/`jj` write, no commit, no index touch; the lane was read with
  `ls`/`grep`/`git rev-parse`/`git show` only.
- No tools installed or upgraded (stdlib `python3` + `rsync` already present).
- Out of scope / not attacked: the registry rows themselves (`MutRegistry`), the counter's legs
  (`MutCounterC`), and O's tool (`MutCounterO`, `MutTool`).

Report: .ufo/waves/round-66/w1/MutEntry.md
