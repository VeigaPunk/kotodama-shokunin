# ExecDCounterControls — D counting and acceptance controls (round 52)

**Seat:** `KotodamaR52.ExecDCounterControls` (executor, leaf)
**Date:** 2026-10-22
**Scope:** instrument controls for claim D's counting command and claim D's acceptance argv, run only against copies of the entry inside a private sandbox clone. No lane file was edited; no lane git/jj state was touched.
**Judged axis:** depth.

## 1. Sandbox

```
git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin \
    /fast/scratch/hyaku/kotodama-r52/ExecDCounterControls
```
Sandbox path: `/fast/scratch/hyaku/kotodama-r52/ExecDCounterControls`, checked out at `d9f73c80744bb5e483f6d9d39069fe064dc5dffe` (the declaration commit named in the assignment).

The entry file is byte-identical at base and at the declaration commit, so the declaration tree is a valid stand-in for base:

```
$ git diff --stat 147cfde85eb13256438c1ed04d92e8d2ad09b76e d9f73c80744bb5e483f6d9d39069fe064dc5dffe \
    -- corpus/knowledge/linguistics/sign-languages-manual-modality.md
(empty)
$ git show 147cfde8...:corpus/knowledge/linguistics/sign-languages-manual-modality.md | md5sum
c10889dadd98cc1b4e0a432e4643f586
$ md5sum corpus/knowledge/linguistics/sign-languages-manual-modality.md   # at d9f73c8
c10889dadd98cc1b4e0a432e4643f586
```

Every control below was run with `cwd` = sandbox root (both argv use repo-relative paths), and every edit was confined to the sandbox copy of `corpus/knowledge/linguistics/sign-languages-manual-modality.md`. The sandbox copy was restored with `git checkout --` after each control; the final tree is back at `d9f73c8` with only the two untracked driver artifacts (`control_drive.py`, `control_results.json`) added inside the sandbox.

## 2. Commands as declared

D counting command — `reports/round-52/claims.json` (claims[0].counting_command), run through `sh -c`:

```
awk '/S094/{n++} END{print n+0}' corpus/knowledge/linguistics/sign-languages-manual-modality.md
```

D acceptance argv — `reports/round-52/separability-manifest.json` (claims[id=D].acceptance), verbatim:

```json
["sh", "-c", "n=$(awk '/S094/{n++} END{print n+0}' corpus/knowledge/linguistics/sign-languages-manual-modality.md); echo S094_lines=$n; test \"$n\" -eq 0 && ! grep -qE '\\bS(13[4-9]|1[4-9][0-9]|[2-9][0-9][0-9])\\b' corpus/knowledge/linguistics/sign-languages-manual-modality.md"]
```

Both were executed via Python `subprocess` with the argv exactly as listed, never through a shell wrapper of my own.

## 3. Baseline (base `147cfde`, and declaration `d9f73c8`)

| tree | counting stdout | counting exit | acceptance stdout | acceptance exit |
|---|---|---|---|---|
| base `147cfde85eb13256438c1ed04d92e8d2ad09b76e` | `5` | 0 | `S094_lines=5` | **1** (expected: 5 and exit 1) |
| declaration `d9f73c80744bb5e483f6d9d39069fe064dc5dffe` | `5` | 0 | `S094_lines=5` | **1** |
| landed D `dea5ece` (already in history) | `0` | 0 | `S094_lines=0` | **0** |

Baseline matches the assignment's expectation. The landed D commit also carries zero `S134+` ids: `grep -cE '\bS(13[4-9]|1[4-9][0-9]|[2-9][0-9][0-9])\b'` on the `dea5ece` version of the entry returns 0 (highest id present is `S126`).

## 4. Controls

Each control mutated only the sandbox copy of the entry. "count" is the D counting command's stdout; "accept" is the D acceptance argv's stdout and exit code.

| control | edit to the sandbox entry | count | count exit | accept stdout | accept exit | expected | verdict |
|---|---|---|---|---|---|---|---|
| a | all five S094-citing lines cleaned (every `S094` token dropped) | `0` | 0 | `S094_lines=0` | **0** | 0 / exit 0 | as expected |
| b | one S094 cite left (line 83 keeps its cites; lines 87, 90, 92, 93 cleaned) | `1` | 0 | `S094_lines=1` | **1** | 1 / exit 1 | as expected |
| c | S094 removed, `S134` added on one new table row | `0` | 0 | `S094_lines=0` | **1** | acceptance exit 1 | as expected — the S134 guard fires even though the counter reads 0 |
| d | base entry untouched, one extra line containing `S0945` | `6` | 0 | `S094_lines=6` | **1** | report whether the counter counts it | **the counter counts it** (6 = 5 real lines + 1 new `S0945` line) |
| d2 | S094 removed everywhere, one line containing only `S0945` | `1` | 0 | `S094_lines=1` | **1** | — | **the counter counts `S0945` as an S094 line** |
| e | S094 removed everywhere, one line containing `` `S094` `` in a backtick code span | `1` | 0 | `S094_lines=1` | **1** | — | **the counter counts S094 inside a code span** |
| e2 | base entry with the line-93 cite moved to `` `S094` `` (backticked) | `5` | 0 | `S094_lines=5` | **1** | — | a backticked cite still counts; the counter is formatting-blind |
| f | line 93 given three `S094` tokens on that one line | `5` | 0 | `S094_lines=5` | **1** | — | the counter increments **per line**, not per occurrence |

Restored sandbox after all controls: count `5`, acceptance exit `1` — back to the baseline.

## 5. Plain statements about the instrument

**The counter is a substring match.** `awk '/S094/{n++} END{print n+0}'` matches the literal characters `S094` anywhere in a line, with no word boundary. `S0945` is therefore counted as an S094 line (controls d and d2 above: count 6 and count 1 respectively, where only `S0945` remained). Any future edit that writes `S0945`, `S094a`, or `S0940` will inflate the count and fail the acceptance even though no genuine S094 citation survives. A false positive here is a fail-safe direction (it fails closed), not a false pass.

**The counter counts lines, not citations.** The base entry has **7** occurrences of `S094` on **5** lines (line 83 carries three occurrences: `(S071, S094; ...)`, `plus palm orientation (S094)`, and `pairs that differ in one parameter (S096, S094)`; lines 87, 90, 92, 93 carry one each). Control f confirms the mechanism: three cites on one line still add 1. The declared `before` value of 5 is therefore a line count, not an occurrence count, and the fix must remove all 7 tokens across 5 lines to read 0.

**The counter is formatting-blind.** A cite inside a backtick code span (`` `S094` ``) still counts (controls e and e2). The counter does not parse Markdown, so it cannot distinguish a live citation from a quoted, code-fenced or otherwise inert mention.

**The acceptance has two independent legs, and only one is about S094.** Leg one is `test "$n" -eq 0` on the counter. Leg two is `! grep -qE '\bS(13[4-9]|1[4-9][0-9]|[2-9][0-9][0-9])\b'` over the entry. Control c shows leg two firing on its own: with every S094 cite removed and one `S134` added, the counter reads `0` but the acceptance still exits 1. That is the guard that keeps claim D clear of the C claim's new id space.

**The S134+ guard uses word boundaries, unlike the S094 counter.** Boundary probes on the cleaned entry (count `0` in every case):

| inserted id | acceptance exit |
|---|---|
| `S133` (below the threshold) | 0 |
| `S134` (exact) | **1** |
| `S1340` | 0 |
| `S1345` | 0 |
| `S140` | **1** |
| `S199` | **1** |
| `S200` | **1** |

So the S134+ guard fires on `S134`, `S140`, `S199`, `S200` and does not fire on `S133`, `S1340`, `S1345`. Note the asymmetry: an id with four digits such as `S1340` escapes the guard (the `\b` after the three-digit group fails) while `S0945` is caught by the S094 counter. The two legs do not use the same tokenization, so a single generic "S-id" matcher over both would be a stricter instrument than either leg alone.

## 6. What the controls say about claim D

- The instrument is sound as a *necessary* condition: at base it reads 5 and exits 1; with all S094 tokens gone it reads 0 and exits 0 (control a); the landed D commit `dea5ece` reads 0 and exits 0.
- The instrument is **not** a sufficient condition for the claim's falsifier clause "a detail that lost its S094 citation and now rests on a row whose re-opened page does not carry it". Nothing in either leg inspects whether the replacement citation actually supports the detail. That half of D's falsifier is not mechanically checkable by the counter and stays with review. This is the depth-axis caveat worth passing to the L1: D's counter measures *removal*, not *re-grounding*.
- The instrument over-counts in the fail-closed direction on any `S094`-prefixed token, and it cannot see code spans. No control showed a false pass: no variant with zero genuine S094 citations returned acceptance exit 0 while still citing S094.

## 7. Evidence index

| fact | where |
|---|---|
| entry file identical at base and declaration | `git diff --stat 147cfde d9f73c8 -- corpus/knowledge/linguistics/sign-languages-manual-modality.md` (empty); md5 `c10889dadd98cc1b4e0a432e4643f586` both sides |
| base S094 lines 83, 87, 90, 92, 93 | `awk '/S094/{n++} END{print n+0}'` → 5; `grep -n 'S094'` → 83, 87, 90, 92, 93 |
| 7 occurrences on 5 lines | `grep -o 'S094' <file> | wc -l` → 7; per-line counts 3, 1, 1, 1, 1 |
| D counting command | `reports/round-52/claims.json`, claims[id=D].counting_command |
| D acceptance argv | `reports/round-52/separability-manifest.json`, claims[id=D].acceptance |
| driver and machine-readable results | `/fast/scratch/hyaku/kotodama-r52/ExecDCounterControls/control_drive.py`, `/fast/scratch/hyaku/kotodama-r52/ExecDCounterControls/control_results.json` |
| landed D commit already present in lane history | `git log --oneline` at `dea5ece` in the sandbox |

## 8. Checks I did not run

- The full round-52 dry-run receipt (`reports/round-52/dry-run.py run`) was executed once in the sandbox at the declaration tree as a cross-check of the declared-command harness; it reproduced the D counting value 5 and the D acceptance exit 1, and confirmed the C acceptance exit 1 with `knowledge_files=227`. I did not run the receipt `check` mode or the separability/agreement legs as claims, because they are the L1's gate, not this seat's.
- No lint, formatter, build or test suite was run; the lane's post-integration gate remains with the parent.
- No tool was installed or upgraded for this assignment; the stock `git`, `awk`, `grep`, `sh` and `python3` on the host were sufficient.

## 9. Result

Measured, no change to any lane file. All seven required controls behaved as expected: base 5 / exit 1; (a) 0 / exit 0; (b) 1 / exit 1; (c) count 0 but acceptance exit 1 from the S134 guard; (d) the counter **does** count `S0945` (it is a plain substring match); (e) the counter **does** count `S094` inside a backtick code span. Three further findings are recorded: the counter counts lines rather than occurrences (7 tokens across 5 lines at base), the S134+ guard uses word boundaries while the S094 counter does not, and neither leg of the acceptance can check whether a replacement citation actually supports the detail it was substituted for.

**Risk carried to the L1:** D's counter measures removal, not re-grounding. A reviewer, not the counter, must confirm that each re-cited detail rests on a row whose re-opened page carries it, or carries an inline `(to-verify)` mark.

**Blockers:** none.
