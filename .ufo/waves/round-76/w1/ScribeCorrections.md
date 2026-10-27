# ScribeCorrections — round 76, wave 1 (kotodama, hyaku run 10)

**Seat.** ScribeCorrections (leaf, no dispatch, no background jobs). **Lane.** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
**Base.** `98c486bdb4650ba5b8e651d332910e8ee60ad121`. **Scratch.** `/fast/scratch/hyaku/kotodama-r76/ScribeCorrections` (removed at exit).
**Verdict.** Drafts delivered: the SCORECARD `## Corrections — round 76` block (15 ANNOTATE rows) and the one REPAIR
statement edit (`SKILL.md:707`) as a unified diff against base. All 16 ledger pairs re-measured red at base; the
ledger itself carries one duplicated pair and leaves four round-75 red statements uncovered (findings 2 and 4).
No lane byte, fleet byte, jj/git state, or index was touched.

---

## 1. Inputs read (no writes)

| input | read | shape |
|---|---|---|
| `.ufo/waves/round-76/CLAIMS-DRAFT.md` | whole file | Ca: `>= 10` pairs, REPAIR (SHONEN.md, SKILL.md, README) or ANNOTATE (lesson, LOG, SCORECARD, QUALITY) |
| `.ufo/waves/round-76/w1/stage/ScoutLedgerA/pairs.json` | 9904 B | bare JSON **list**, 8 pairs, L76-01…L76-08, all ANNOTATE |
| `.ufo/waves/round-76/w1/stage/ScoutLedgerB/pairs.json` | 6045 B | **dict** `{round,claim,axis,base,status,pairs}`, `status: "DRAFT — base observations executed against the pinned revision"`, 8 pairs, L76-09…L76-16, 7 ANNOTATE + 1 REPAIR |
| `SCORECARD.md:1468-1505` | round-75 block | table shape `id \| old token \| new token \| re-derivation command` |
| `.ufo/waves/round-75/w3/ExecCountsSweep.md` | whole file | F1–F13 (fallback source; **not used** — both pair files arrived) |
| `corpus/lessons/round-75-verifier-spotcheck.md` §7 | whole section | routed defects 1–7 |
| `corpus/lessons/round-75.md` `## Routed to round 76` | whole section | items 1–8 |

Pair-file presence sweep: `ls …/stage/ScoutLedgerA/pairs.json` and `…/ScoutLedgerB/pairs.json` failed at
18:33/18:35/18:36; A appeared at 18:36 (9904 B), B at 18:38 (0 B then 6045 B). Total wait inside the
25-minute budget: `sleep 300` once (backgrounded, completed) plus two `[ -f ]` poll loops returning in 36 s and
16 s. **Number: 2 stage files — `ls -la .ufo/waves/round-76/w1/stage/ScoutLedger*/pairs.json`.**

## 2. Every ledger pair re-derived at base

Method: one `--shared` clone of the lane, checked out at base, inside the seat scratch.

```
git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin "$S/clone"
git -C "$S/clone" rev-parse --show-toplevel   -> /fast/scratch/hyaku/kotodama-r76/ScribeCorrections/clone
git -C "$S/clone" checkout -q -B base 98c486bdb4650ba5b8e651d332910e8ee60ad121
git -C "$S/clone" rev-parse HEAD              -> 98c486bdb4650ba5b8e651d332910e8ee60ad121
```

Each pair's own `observe_cmd` argv was executed with `cwd=<clone>` and its own `parse` applied to stdout
(script `$S/checkpairs.py`, retained at `.ufo/waves/round-76/w1/stage/ScribeCorrections/checkpairs.py` with its
output in `pairs-verify.txt` beside it). Result, verbatim tail of the run:

```
pairs: 16
L76-01 ANNOTATE exp='present'                        got='present'                          OK rc=0 count=227
L76-02 ANNOTATE exp='FINAL'                          got='FINAL'                            OK rc=0
L76-03 ANNOTATE exp='blob'                           got='blob'                             OK rc=0
L76-04 ANNOTATE exp='blob'                           got='blob'                             OK rc=0
L76-05 ANNOTATE exp='30920'                          got='30920'                            OK rc=0
L76-06 ANNOTATE exp='whole-document'                 got='whole-document'                   OK rc=0
L76-07 ANNOTATE exp='amend-2026-10-23b'              got='amend-2026-10-23b'                OK rc=0
L76-08 ANNOTATE exp='3266'                           got='3266'                             OK rc=0
L76-09 ANNOTATE exp='3266'                           got='3266'                             OK rc=0
L76-10 ANNOTATE exp='4096'                           got='4096'                             OK rc=0
L76-11 ANNOTATE exp='109588'                         got='109588'                           OK rc=0
L76-12 ANNOTATE exp='116878'                         got='116878'                           OK rc=0
L76-13 ANNOTATE exp='109588'                         got='109588'                           OK rc=0
L76-14 ANNOTATE exp='corpus/SOURCES.md'              got='corpus/SOURCES.md'                OK rc=0
L76-15 ANNOTATE exp='marrone%20age%20dor---2.pdf'    got='marrone%20age%20dor---2.pdf'      OK rc=0
L76-16 REPAIR   exp='315c5f3f27fd'                   got='315c5f3f27fd'                     OK rc=0
mismatches: 0
```

**Numbers: 16 pairs, 15 ANNOTATE / 1 REPAIR, 0 mismatches, every `observe_cmd` exit 0 —**
`python3 -B $S/checkpairs.py` (output above). This also proves each pair's `parse` compiles and captures, which
is what the counter will re-run.

## 3. Drafts produced

### 3.1 `.ufo/waves/round-76/w1/drafts/scorecard-corrections.md` (10774 B)

The full `## Corrections — round 76` block: preamble (ledger path, 16 pairs, counter invocation with
`--combined` named), the round-75-shaped table with one row per ANNOTATE pair (id, old token, new token, the
pair's `rederive` string verbatim, unquoted as in round 75), per-row notes naming file:line and the defect,
the REPAIR paragraph pointing at the diff, and a fenced block of the sixteen pasted raw outputs.

Row tokens (old → new), all read from the pairs' `stated_parse` capture and verified `observe_cmd` output:

| id | stated_at | old | new |
|---|---|---|---|
| L76-01 | `corpus/lessons/round-75.md:4` | absent | present |
| L76-02 | `:15` | DRAFT | FINAL |
| L76-03 | `:312` | fails | blob |
| L76-04 | `:332` | fails | blob |
| L76-05 | `:92` | 6862 | 30920 |
| L76-06 | `:55` | excerpt | whole-document |
| L76-07 | `:246` | amend-2026-10-23 | amend-2026-10-23b |
| L76-08 | `:47` | 10 | 3266 |
| L76-09 | `:47` | 10 | 3266 |
| L76-10 | `:31` | 4097 | 4096 |
| L76-11 | `:28` | 111486 | 109588 |
| L76-12 | `:30` | 118776 | 116878 |
| L76-13 | `corpus/knowledge/myth-symbol/narrative-structure-frameworks.md:8` | 111487 | 109588 |
| L76-14 | `:23` | .ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md | corpus/SOURCES.md |
| L76-15 | `:251` | marrone%20age% | marrone%20age%20dor---2.pdf |
| L76-16 (REPAIR) | `SKILL.md:707` | fa5060b91bdb | 315c5f3f27fd |

The SCORECARD block carries **no** row for L76-16 (REPAIR pairs carry a diff instead), matching round-75's rule.

### 3.2 `.ufo/waves/round-76/w1/drafts/repairs.diff` (10202 B, 11 lines, one hunk)

Produced as `diff -u -L a/SKILL.md -L b/SKILL.md <base blob> <repaired blob>`:

```
--- a/SKILL.md
+++ b/SKILL.md
@@ -704,7 +704,7 @@
```
Changed lines: **2 — `diff db/SKILL.md dn/SKILL.md | grep -c '^[<>]'` → `2`**; files touched in the diff:
**1 — `grep -c '^--- a/' repairs.diff` → `1`**. The patch applies to a clean base worktree:
**`git -C $S/clone apply --check drafts/repairs.diff` → `APPLY-CHECK OK`** (exit 0).

The repaired sentence at `SKILL.md:707` now reads: the `fa5060b91bdb…` sha is named as *the pre-freeze byte
recorded on line 2 of `reports/round-75/telemetry/selftest-c.txt`*, and the committed counter's sha
`315c5f3f27fd…` is given with its re-derivation (`sha256sum reports/round-75/accept-c.py`). Evidence:

```
$ sha256sum reports/round-75/accept-c.py
315c5f3f27fd36b7ee92cb5bff9c34c27a5013e28218d9481ee7f74b5c7ce261  reports/round-75/accept-c.py
$ git show 98c486b…:reports/round-75/telemetry/selftest-c.txt | head -2
# selftest-c.txt — python3 -B reports/round-75/accept-c.py --selftest (run from the lane, 2026-10-27, before the freeze)
# counter sha256 fa5060b91bdb6e76947aa7a0daab6d037b40a3be9f978e257783c7180c314d3f
```

No historical line was rewritten: the lesson, LOG, QUALITY, SCORECARD history and the frozen round-75 bytes
stand; the only edit target is a mutable `SKILL.md` line.

## 4. Findings

**F-1 — The ledger's two halves use different JSON shapes.** A is a bare list; B is a ledger dict with
`status: "DRAFT — base observations executed against the pinned revision"`. Any assembler must normalise
(`d["pairs"] if isinstance(d, dict) else d`). Measured:
`python3 -c "…;print(type(json.load(open(A))).__name__, type(json.load(open(B))).__name__)"` → `list dict`.

**F-2 — L76-08 and L76-09 are the same pair.** Both cite `corpus/lessons/round-75.md:47`, both state
`chars=4097 before=10`, both resolve to `3266`; the only difference is the regex flavour
(`before=(\d+)` vs `before=([0-9]+)`) and the `git grep -o -E` vs `-h -E` argv. Both ids are carried as rows in
the draft because both are in the ledger; the L1 should decide whether the frozen ledger keeps 16 ids or drops
one to 15. Measured: the two `pairs` entries read back as shown in §2 (both `OK … 3266`).

**F-3 — Only one REPAIR pair, so only `SKILL.md` gets an edit.** `SHONEN.md` and `corpus/README.md` carry no
pair. Two round-75 statements in `SHONEN.md:6` are still red at base and are **not** in either ledger file, so
this seat did not draft edits for them (the ledger is the authority, and it is fixed before data):

```
$ git show 98c486b…:reports/round-75/telemetry/census-start.txt | grep -c 'exit'
0
$ git show 98c486b…:reports/round-75/telemetry/census-end.txt | grep -c 'exit=0'
1
$ git show 98c486b…:reports/round-75/telemetry/census-end.txt | grep -c 817
0
```

`SHONEN.md:6` says "census exit 0 in `…census-start.txt`" (that file carries no `exit` line) and "close counts
… re-derived at `…census-end.txt`" (that file never prints `817`; it is 35 lines of W04/W01 notices —
`| wc -l` → `35`). Reported, not fixed: adding them as pairs is a ledger decision above this seat.

**F-4 — Four round-75 red statements are uncovered by the ledger.** The union L76-01…L76-16 covers F1, F2, F3,
F4, F5 (head entry only), F7, F8, F9 (S888 two ways), F10 (bytes only), F11, F12, F13. Uncovered:

1. **lesson:48-49, S892's window.** Stated `chars=4097 before=284`; landed
   `window: chars=4097 min=4096 pad=400 before=2020 after=2026` —
   `git show 98c486b…:reports/round-75/evidence/S892.txt | grep -E '^window: chars='` (output pasted).
   The stated `before=284` is red by **1736 characters**.
2. **F6, the Ca printed command.** lesson:14 claims `accept-ca.py` prints `PASS legs=12/12` from the printed
   argv, which omits `--combined`. **Not run by this seat** (round-75's ExecCountsSweep measured `FAIL legs=10/12`);
   reported as sourced, not observed here.
3. **F10's digests.** Only byte counts are ledgered (L76-11, L76-12); the companion sha values
   (`2bcdd019…` vs committed `20b571d7…`, `fbf48ad2…` vs `e0560649…`) have no pair.
4. **F5's two sibling sizes.** L76-05 ledgers only `6862 → 30920`; `5933`/`2514` vs `24166`/`23049` are red on
   the same line and unpaired.

**F-5 — L76-13's command is byte-identical to L76-11's.** Both are
`git grep -h -E '^bytes: ' … -- reports/round-75/evidence/S885.txt`; the pairs differ only in `stated_at`
(lesson:28 vs the entry's `:8`). The draft keeps both because the corrected *statements* differ. Flagged
because round-71's K71 defects included counter-sha miss-pairing — a counter that keys rows by command rather
than by id would collapse these two.

**F-6 — Two pairs print more than one line.** L76-15's file carries the same URL twice, so the command prints
`marrone%20age%20dor---2.pdf` and `marrone%20age%20dor---2.pdf,`; the parse takes the first. L76-01's count is
227 lines of `claims.json` and the `count-presence` parser maps it to `present`.

**F-7 — L76-14's parse depends on `git grep -l`'s revision prefix.** The raw line is
`98c486bdb4650ba5b8e651d332910e8ee60ad121:corpus/SOURCES.md`; the parse `:([^:\s]+)$` returns
`corpus/SOURCES.md`. A counter that runs `observe_cmd` with `cwd=<root>` but without `-C`/revision semantics
would produce `corpus/SOURCES.md` with no prefix and the parse would return nothing. The pair is correct as
written; the counter must run the argv verbatim.

## 5. Claims verified for the note text (so the notes are not hearsay)

| note claim | command | output |
|---|---|---|
| S885 committed bytes | `git show 98c486b…:reports/round-75/evidence/S885.txt \| sed -n 's/^bytes: //p'` | `109588` |
| S887 committed bytes | same, `S887.txt` | `116878` |
| S888, S889, S890, S893 bytes match the entry's other four counts | same, per file | `225123`, `1085244`, `697092`, `45238` |
| S893 is the article page (45238) | same, `S893.txt` | `45238` |
| whole-document census | per-file `grep '^window-scope:'` | whole-document ×4 (S885,S886,S887,S891), excerpt ×5 (S888,S889,S890,S892,S893) |
| S885 used-by cell names `amend-2026-10-23b` | `git show …:corpus/SOURCES.md \| grep -E '^\| S885 ' \| awk -F'\|' '{print $12}'` | base + amend-23 + **amend-23b** |
| S891/S892 used-by is the `b` amendment | same, `S891`/`S892` | `…amend-2026-10-23b.md` |
| validate/ never existed | `git log --all --oneline -- '.ufo/waves/round-75/assimilation/validate/*' \| wc -l` | `0` |
| the "URL wrap" defect is absent | `git show …:…amend-2026-10-23.md \| grep -c '%$'` | `0` |

## 6. Out of scope / not done

- **Not run:** the round-76 counters (`accept-ca.py`, `accept-c.py`) — they do not exist at base; the drafts are
  pre-freeze artifacts. **Not run:** the round-75 `accept-ca.py` with and without `--combined` (F6 above is
  sourced from the round-75 sweep, and this seat's measurement of it would have been a second data point, not
  the pair's token).
- **Not edited:** `SCORECARD.md`, `SHONEN.md`, `corpus/**`, `reports/round-75/**`, `reports/round-76/**`,
  `LOG.md`, `SKILL.md` in the lane, `.ufo/state`, `.ufo/watchdog.log`, the fleet repo, `scripts/`, `templates/`,
  `/home/vgpnk/Projects/shokuknow/**`.
- **Not committed:** no git/jj mutation anywhere; the base clone was read-only apart from `git apply --check`
  (no write) and the checkout of the clone's own worktree at base.
- No tool was installed, no `pacman` invocation, no model passed anywhere.

## 7. Touched surfaces (writes)

| path | bytes | note |
|---|---|---|
| `.ufo/waves/round-76/w1/drafts/scorecard-corrections.md` | 10774 | the SCORECARD block draft |
| `.ufo/waves/round-76/w1/drafts/repairs.diff` | 10202 | one hunk, `SKILL.md:707` |
| `.ufo/waves/round-76/w1/ScribeCorrections.md` | this file | seat report |
| `.ufo/waves/round-76/w1/stage/ScribeCorrections/checkpairs.py` | 1130 | the pair runner (copy of the scratch script) |
| `.ufo/waves/round-76/w1/stage/ScribeCorrections/pairs-verify.txt` | 1894 | its output: 16 pairs, 0 mismatches, every rc=0 |

Scratch `/fast/scratch/hyaku/kotodama-r76/ScribeCorrections` (clone + `db/` + `dn/` + three helper scripts) is
removed before yield; the two drafts were copied into the wave dir first and their digests re-checked there.

## 8. Known limits

- The draft block's table cells are the pairs' `rederive` strings **as the seats wrote them**; I verified their
  `observe_cmd` argv and `parse`, which is what the counter executes, and separately ran the `rederive` strings
  by hand. Where the two differ (L76-16's rederive uses a relative path, its `observe_cmd` is the same argv),
  the argv is the graded one.
- The token cells for L76-03/L76-04 read `fails → blob`; that vocabulary mismatch is inherent (an argv with no
  pipe cannot print an exit status) and is explained in the block's notes, not smoothed over.
- `L76-08`/`L76-09` duplication (F-2) is carried, not resolved; resolving it changes the ledger, which is the
  seats' file to fix before the freeze.
