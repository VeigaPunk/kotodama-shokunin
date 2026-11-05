# CriticClaims — falsification of the two frozen claims (round 90, w2)

Seat `CriticClaims` (leaf, no dispatch). Revisions: freeze `d0b6f2a7f9cc36272682749a9b047b739406f0c8`, base `6b0b86e45ae902331aca75863db380f2991458c4`, lands `7f3a7aa6615624afadc2cc2d2d4f7ad225f44761`. Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, read-only; every mutation below happened in `/fast/scratch/hyaku/kotodama-r90/CriticClaims/` (TMPDIR set explicitly, `git rev-parse --show-toplevel` asserted in every scratch repo before its first commit). Nothing in the lane, `~/.local/bin`, the fleet root or `.ufo/state` was written. Tooling installed: none (pacman paused host-wide; python3/git/tar/grep sufficed).

Instrument identity is part of every reading below:

```
$ sha256sum reports/round-90/measure90.py
6e1ea6a5f96c6e92660e7a18c18b896d46dee3bf6368231e1a4a8fd7895406cd   # worktree == lands (rev 6)
$ git show d0b6f2a7:reports/round-90/measure90.py | sha256sum
4091cda9e0b5af399e99e85898f3040b9070d4225cf11584a601fe4c19caf0ce   # freeze (rev 1)
```

Frozen claims at the freeze are byte-identical to the worktree copy (`sha256 9c161eee…`); claims were not amended.

## Verdict summary

| # | finding | verdict | command |
|---|---|---|---|
| F1 | O reproduces 6/6 at LANDS | PASS | `measure90.py … --claim O --work workO` → `MEASURE90-O: PASS legs=6/6` rc=0 |
| F2 | C reproduces 4/4 at LANDS | PASS | `measure90.py … --claim C --work workC` → `MEASURE90-C: PASS legs=4/4` rc=0 |
| F3 | `MATERIALIZE` discriminates nothing (passes at BASE for both claims) | FAIL | `measure90.py … --lands 6b0b86e4 --claim C` → `LEG PASS MATERIALIZE` |
| F4 | `SELFTEST` and `REFUSALS` are self-attested; a 10-line do-nothing tool passes both | FAIL | counterfeit-tree run below → `LEG PASS SELFTEST`, `LEG PASS REFUSALS` |
| F5 | `STUB` passes a receipt that records the stub **passing** everything | FAIL | counterfeit-receipt run → `LEG PASS STUB … observed=recorded` |
| F6 | claims.json O.after_target/predicate say the stub receipt records a SELFTEST **failure**; the bytes record `SELFTEST PASS 67/67` | FAIL | `cat reports/round-90/controls/stub-tool.txt` |
| F7 | Does F6 change the O verdict? | UNPROVABLE as written / PASS as measured | kill_rule enumeration excludes STUB; counter prints `MEASURE90-O: PASS legs=6/6` |
| F8 | C.surface "inside **six** entries" is not what its named command returns (five files, seven lines) | FAIL | `git grep -niE '^#{1,6} .*\b(prayer\|petition\|votive\|supplicat)' 6b0b86e4 -- corpus/knowledge` |
| F9 | C's `MATERIALIZE` and `INDEX` legs also pass at BASE (INDEX is global well-formedness, not a C landing signal) | FAIL | `measure90.py … --lands 6b0b86e4 --claim C` → `LEG PASS INDEX` |
| F10 | Separability: O is independent of C; C is instrument-coupled to O's graded tool, and the frozen sentence misdescribes the sandbox | FAIL as stated / PASS at landing level | `separability90.py … --receipt …/separability-mine.txt` → `SEPARABILITY: PASS`, `SHARED … tools/check-advance-evidence.py` |
| F11 | O.before cites `reports/round-89/mutation-score.txt`, which does not exist at BASE | FAIL | `git cat-file -e 6b0b86e4:reports/round-89/mutation-score.txt` → fatal |
| F12 | The counter named in claims.json as "freeze-pinned" cannot grade either claim; C was graded by rev 6, committed in the landing commit | FAIL | run of `git show d0b6f2a7:reports/round-90/measure90.py` → `UnicodeDecodeError` |

## 0. Reproduction (both claims, own runs)

```
$ python3 -B reports/round-90/measure90.py --root <lane> --freeze d0b6f2a7… \
    --lands 7f3a7aa6… --claim O --work …/workO --receipt …/O-lands.txt
LEG PASS MATERIALIZE …  LEG PASS TOOL (sha 121888f0…)  LEG PASS SELFTEST (SELFTEST PASS 67/67)
LEG PASS REFUSALS (all ok)  LEG PASS MUTATION (43/43 killed, 0 survived, 0 broken-pattern)
LEG PASS STUB … observed=recorded
MEASURE90-O: PASS legs=6/6                    rc=0   (217.7 s)

$ … --claim C --work …/workC
LEG PASS MATERIALIZE … LEG PASS ENTRY (clean) LEG PASS INDEX (CORPUS-INDEX: OK files=262 rows=262 findings=0)
LEG PASS APPENDONLY (clean)
MEASURE90-C: PASS legs=4/4                    rc=0
```

Direct selftest, not through the counter:

```
$ python3 -B mat-lands/tools/check-advance-evidence.py --selftest --work …/st-direct
rc=0; 67 lines `  ok <name>: rc=N`; each of the 13 frozen refusal-case names appears exactly once.
$ git show 6b0b86e4:tools/check-advance-evidence.py
fatal: path 'tools/check-advance-evidence.py' exists on disk, but not in '6b0b86e4…'
```

C's registry delta is also real and not a counter artifact: base 865 rows, lands 873, new ids `S942…S949`; S942–S948 are tier A/A/A/B/A/A/A, `mined`, `opened 2026-11-04`, `used-by corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`; S949 is tier C, `rejected`, used by the lesson; zero base rows removed or cell-changed; the entry is 19 930 bytes with 9 headings and a 5-row × 4-col table; the linguistics partition goes 34 → 35; all seven LOCATED gate quotes occur verbatim in `reports/round-90/evidence/S94{2..8}.txt` under the grader's own `norm()` (NFKC, ’→', whitespace collapse, casefold). So F1/F2 are not disputed — the question is what the six and four legs actually test.

## 1. Which legs pass for the wrong reason

A leg is vacuous when it is satisfied by both the honest landing and a counterfeit. Operationally: build a do-nothing tree, run the frozen counter, and see which legs still go green.

Counterfeit A — a 10-line `tools/check-advance-evidence.py` that prints `SELFTEST PASS 67/67`, prints the 13 `  ok <case>:` lines, exits 0, and implements nothing (scratch repo `…/faketool`, freeze tree copied, one commit with the fake tool):

```
LEG PASS MATERIALIZE …  LEG FAIL TOOL (10ccc4bc… != 121888f0…)  LEG PASS SELFTEST
LEG PASS REFUSALS …     LEG FAIL MUTATION (0/43 killed, 43 broken-pattern)  LEG PASS STUB
MEASURE90-O: FAIL legs=4/6 failed=TOOL,MUTATION
```

Counterfeit B — the same fake tool plus a `controls/stub-tool.txt` that records the stub **passing** `SELFTEST`, `REFUSALS` (13/13) and `MUTATION` (43/43), with the token `FAIL` only inside the sentence "no FAIL occurs in this receipt" (scratch repo `…/fakeboth`):

```
LEG PASS MATERIALIZE … LEG FAIL TOOL … LEG PASS SELFTEST … LEG PASS REFUSALS … LEG FAIL MUTATION
LEG PASS STUB expected=…records the stub failing SELFTEST and MUTATION observed=recorded
MEASURE90-O: FAIL legs=4/6 failed=TOOL,MUTATION
```

Read against `reports/round-90/measure90.py`:

- `MATERIALIZE` is `os.path.isdir(mat/corpus)` (`measure90.py:113`, `:171`). It passes on the **base** tree too: my `--lands 6b0b86e4 --claim C` run prints `LEG PASS MATERIALIZE` (and the committed `controls/at-freeze-O-base.txt` prints it for O). **F3 FAIL as a discriminator.**
- `SELFTEST` is a regex over the tool's own stdout plus `rc==0` (`:129-136`); `REFUSALS` is `^  ok <case>:` over the same stdout (`:137-142`). Both are self-attestations: Counterfeit A passes both while doing nothing. The only reason A is caught is `TOOL` (sha pin) and `MUTATION` (`broken-pattern`). **F4 FAIL as independent evidence.**
- `STUB` is `ok = ('SELFTEST' in text and 'FAIL' in text and 'MUTATION' in text and 'broken-pattern' in text)` (`:157-165`) over `mat/controls/stub-tool.txt`. Counterfeit B passes it with a receipt that records the opposite of the leg's own sentence. **F5 FAIL.** Note also that this leg reads the **lands** copy of the receipt (`mat/…`), not the freeze copy, so a landing commit may rewrite it (here the bytes are unchanged: both freeze and lands carry `sha256 1331a899…`, verified with `git show <rev>:reports/round-90/controls/stub-tool.txt | sha256sum`).
- `TOOL` (sha256 equality with the frozen pin) and `MUTATION` (43 textual mutants, `killed==total>=42`, 0 survived, 0 broken-pattern) are the two discriminating legs. That is the honest core of O: *these exact bytes*, whose selftest is demonstrably sensitive to 43 named source lines. The claim's own `bounds` says the selftest's 67 checks are not exhaustively proven; nothing in the counter contradicts that.

C's legs on the same test:

- At base the counter prints `LEG PASS MATERIALIZE` and `LEG PASS INDEX (files=261 rows=261 findings=0)`, `LEG FAIL ENTRY`, `LEG FAIL APPENDONLY` (`…/C-base.txt`; the committed `controls/at-freeze-C-base.txt` agrees). `INDEX` is a whole-corpus consistency check, green on any coherent tree, so it is not evidence that C landed. **F9.** The two legs that do discriminate for C are `ENTRY` (frozen tool over the materialised lands tree) and `APPENDONLY` (registry diff + citation, computed in the counter itself, `:216-251`).
- `ENTRY` aggregates six `LEG PASS` lines emitted by `tools/check-advance-evidence.py` — that is, by the object O grades. This is the coupling taken up in §4.
- `GATE`/`CAPTURE` iterate only the *qualifying cited* rows (`measure90` passes `--graded corpus/SOURCES.md --graded corpus/lessons/round-90.md`; `check-advance-evidence.py:462-482` loops `for rid in qualifying`). The rejected S949 gate line is therefore never checked: its quote is not a substring of `evidence/S949.txt` under `norm()` because HTML tags sit inside the sentence (raw capture line 770: `A <b id="mwIw">votive offering</b> or <b id="mwJA">votive deposit</b> is one or more objects…`). No C leg depends on it — S949 is tier C and `rejected` — but a reader treating the lesson's gate block as fully capture-bound would be wrong.

## 2. The stub receipt against the frozen text

The committed receipt, all eight lines:

```
# Stub control (claim O, cheapest do-nothing landing)
# stub bytes sha256 52ae4b62…   # command: python3 -B <stub> --selftest --work <dir>
# rc=0 stdout='SELFTEST PASS 67/67'
# refusal cases printed ok by the stub: 0/13 -> REFUSALS leg FAIL
# command: python3 -B reports/round-90/mutants.py --root <stub-tree> …
# rc=1 MUTATION-SCORE: 0/43 killed, 0 survived, 43 broken-pattern
# -> MUTATION leg FAIL (every mutant is broken-pattern: …)
```

Frozen text (`claims.json` line 42, `O.after_target`): "STUB control records the stub failing **SELFTEST** and MUTATION." Line 43 (`O.predicate`): "… and `reports/round-90/controls/stub-tool.txt` records the stub's **SELFTEST** and MUTATION failures."

- The bytes record `SELFTEST PASS 67/67` (`rc=0`) — a **fabricated pass**, exactly as the lane's own later reproduction states (`controls/stub-tool-reproduced.txt`: "that stub printed the same fabricated `SELFTEST PASS 67/67` line; the refusal cases, not the tally, catch it"). The stub fails `REFUSALS` and `MUTATION`, never `SELFTEST`. **F6 FAIL: the frozen text is inaccurate to the bytes, and the inaccuracy is self-documented in the lane but the frozen text cannot be amended.**
- Does that change the O verdict? Not by the counter, and not by the kill rule either: `O.kill_rule` says "Any FAIL leg kills O" but enumerates the failing conditions as sha mismatch, tally below the frozen count, surviving/broken-pattern mutant, refusal case not printed ok — **STUB is absent from the enumeration**. The counter's STUB leg passes on a four-token substring. So the measured verdict stays `PASS legs=6/6`, while the predicate as written is false at its last conjunct. **F7: the claim cannot be certified PASS against its own predicate text, and cannot be certified FAIL against its own kill rule — UNPROVABLE as written, PASS as measured.** The smallest honest description is the receipt's own: the stub *fakes* SELFTEST and is caught by REFUSALS and MUTATION. That sentence is written in `controls/stub-tool-reproduced.txt` and in `corpus/lessons/round-90.md`; it never reaches `claims.json`.

## 3. C.surface, re-measured at BASE

The command the claim names is `git show 6b0b86e4:corpus/knowledge` + a word-boundary grep. Run against a `git archive` extraction of base:

```
$ git grep -niE '^#{1,6} .*\b(prayer|petition|votive|supplicat)' 6b0b86e4 -- corpus/knowledge | wc -l
7
$ … | awk -F: '{print $2}' | sort -u | wc -l
5        carthage.md  tibet.md  direction-symbolism.md  sacred-topography-pilgrimage.md  religion-language-co-evolution.md
$ git ls-tree -r --name-only 6b0b86e4 corpus/knowledge | grep -Ei 'prayer|petition|votive|supplicat' | wc -l
0
$ git ls-tree -r --name-only 6b0b86e4 corpus/knowledge/linguistics | wc -l
34
$ git show 6b0b86e4:corpus/SOURCES.md | grep -cE '^ {0,3}\|[ ]*S[0-9]{3,}[ ]*\|'
865
```

- The claim's parenthetical references are exact: all seven lines, in those five files, at those line numbers.
- "no knowledge filename carries prayer|petition|votive|supplicat (0 owners)", "linguistics partition 34 files", "registry 865 rows" all hold.
- "the surface exists only as sub-sections inside **six** entries" does **not** hold for the named command: it is **five** files. `reports/round-90/base-surface.txt` repeats the error ("7 lines over 6 files"). The "six" appears to be carried over from the *unbounded* form of the same grep (`grep -rn -i -E '^#+ .*(prayer|petition|votive|supplicat)'`, the command printed in the lesson), which returns **9 lines over 6 files** — six because `culture-material/garment-lexicon-crosslinguistic.md:1` and `:56` match *com*-petition. So the frozen surface sentence mixes a count from the unbounded run with references from the word-bounded run; neither command yields "six entries" plus those seven references. (`corpus/lessons/round-90.md` R90-M8 records the same class of miscount — "nine lines in five entries" — which is also wrong: nine lines, six files, five of them topical.) **F8 FAIL on the count, PASS on every other element of the sentence.**

## 4. Causal separability on the committed bytes

Exact file sets each claim's legs read (`measure90.py`, not the separability docstring):

- **O** — lands tree: `tools/check-advance-evidence.py` (TOOL sha, executed for SELFTEST, its stdout for REFUSALS), `reports/round-90/controls/stub-tool.txt` (STUB). Freeze: `reports/round-90/claims.json` (cfg), `reports/round-90/mutants.py` (written to work, then run over the lands tool). Work copies only otherwise. `reports/round-90/mutation-score.{txt,json}` — named in `claims.json` separability and inside the O overlay — are **read by no leg**; the counter recomputes the score into `--work` (`:146-152`).
- **C** — lands tree: `corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`, `corpus/SOURCES.md`, `corpus/lessons/round-90.md`, `reports/round-90/evidence/manifest.json` + the capture files, `corpus/README.md`. Base: `corpus/SOURCES.md` (`git show`). Freeze: `tools/check-advance-evidence.py` (**the entry grader**), `tools/check-corpus-index.py`. Plus the whole `corpus/knowledge/**` tree, because `check-corpus-index.py` counts files against README.

Verdicts:

Own run of the harness (`separability90.py --repo <lane> --freeze d0b6f2a7… --lands 7f3a7aa6… --work …/sepwork2 --receipt …/separability-mine.txt`, rc=0, 141 s):

```
COUNTER: source=worktree sha256=6e1ea6a5… rev=6
VERDICT O: PASS legs=6/6     SANDBOX O: paths=8  graded=7  substrate=0  structural=['corpus/.overlay-keep']
ABSENT other-claim paths in overlay O: 6/6 absent -> <all six C paths>
VERDICT C: PASS legs=4/4     SANDBOX C: paths=278 graded=9  substrate=1
ABSENT other-claim paths in overlay C: 4/4 absent -> mutants.py, mutation-score.txt/.json, controls/stub-tool.txt
SHARED declared in both overlays: reports/round-90/claims.json, reports/round-90/measure90.py, tools/check-advance-evidence.py
SEPARABILITY: PASS           CLAIMS: BOTH-PASS
```

- **O is causally independent of C's landing.** No O leg reads a C path; the committed `final/separability.txt` shows the O overlay passing with `C.other_missing` naming every C path, and my own `separability90.py` run above repeats it (overlay O paths=8, every C path absent, `MATERIALIZED O … none`).
- **C is not independent of O's instrument.** Its ENTRY leg is graded by `tools/check-advance-evidence.py`, the exact file O grades, taken from the freeze. C's overlay therefore contains O's graded object: `c_paths()` includes `TOOL` (`separability90.py:152-155`), and both overlays carry `SHARED = (claims.json, measure90.py, tools/check-advance-evidence.py)` (`:68`). The harness's disjointness test subtracts exactly that tuple before comparing (`other = … p not in SHARED`, `:429-430`), so `SEPARABILITY: PASS` is computed on a set from which the coupling has been removed by construction. The coupling is declared, not hidden — but a counterfeit grader that printed six `LEG PASS ENTRY…` lines would pass C's ENTRY leg, which is the same self-attestation weakness as F4, one level up. What the harness does prove: C is independent of O's *landing* (the freeze copy, not the lands copy, is used).
- The frozen sentence is still wrong as written: "A sandbox **at the freeze** overlaid with **only one claim's paths** must pass that claim" (`claims.json:74`). The harness overlays onto the **lands** commit (`commit_overlay(repo, lands, …)`, `:250`), C's sandbox additionally carries `corpus/knowledge` (all other entries) and `tools/check-advance-evidence.py`, and O's carries `corpus/.overlay-keep`. For C a freeze-based sandbox cannot pass at all — the entry does not exist at the freeze. **F10 FAIL as stated; PASS for the landing-level property the harness actually tests.**

## 5. Two provenance defects in the claim text

- `O.before`: "its mutation score was 10/41 (`reports/round-89/mutation-score.txt`)". The path does not exist at base (`git cat-file -e 6b0b86e4:reports/round-89/mutation-score.txt` → fatal); the 10/41 figure exists only as prose in `corpus/lessons/round-89.md:116` (R89-M5). The number is right, the citation is invented. **F11 FAIL.**
- `claims.json` card/`O.bounds`/`C.surface` call `reports/round-90/measure90.py` "the freeze-pinned counter" and "frozen with both". It is not: freeze sha `4091cda9…`, lands and worktree sha `6e1ea6a5…`. Running the frozen revision against the lands revision crashes before any leg:

```
$ git show d0b6f2a7:reports/round-90/measure90.py > measure90-freeze.py   # sha 4091cda9…
$ python3 -B measure90-freeze.py --root <lane> --freeze d0b6f2a7… --lands 7f3a7aa6… --claim C --work …
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc7 in position 68868618: invalid continuation byte
```

  The receipts at lands (`final/lands-O.txt`, `final/lands-C.txt`) can only have been produced by a post-freeze revision — rev 1 crashes before the first leg — and the worktree/lands copy (rev 6, whose ENTRY-leg parser fix is the change that makes C passable at all) reproduces both of them line for line in my runs above (`counter-revisions.md` rev 6 records that rev 1 read every C leg as missing). The revision chain is documented and the diff I ran (`git diff d0b6f2a7 7f3a7aa -- reports/round-90/measure90.py`) touches only absent-artifact branches plus that parser — no leg name, threshold or constant — so the fix is not data-tuning. But the frozen claim's own instrument reference is not reproducible from the freeze. **F12 FAIL as a provenance statement, no effect on the leg outcomes.**

## 6. What this means for the two claims

- **O**: the operability acquisition is real — the sha-pinned bytes carry a 67-check selftest with 13 named refusal negatives, a 43/43 mutation receipt that I recomputed, and a do-nothing tool is caught by `TOOL`+`MUTATION`. Four of its six legs carry no discriminating weight, and one of them (`STUB`) is described in the frozen text as recording the opposite of what it records. A reviewer reading `claims.json` alone is told something false about the committed control; the counter's own docstring repeats it (`measure90.py:20-21`).
- **C**: the coverage landing is real and reproduces end to end (entry, seven mined rows, one retained rejection, seven verbatim gate quotes, index, README, partition 34→35). Its two non-vacuous legs are `ENTRY` and `APPENDONLY`; `ENTRY` is graded by O's instrument. The base surface sentence is correct except for a count that its own command contradicts.
- **Calibration**: both claims are frozen at a commit where their named counter does not run, and both quote at least one committed artifact inaccurately (O: the stub receipt; C: the surface count; plus O's round-89 path). None of these flips an operability or coverage leg; all of them are exactly the class QUALITY36 exists to catch, and none can be repaired in the frozen text.

Residual risk / limits of this review: the 67-check selftest was read and run but not audited check-by-check for double-counting; `mutants.py` kills mutants only through the selftest, so a selftest with no independent oracle is not disproved here; freshness was not touched (pause respected), and no registry row was re-verified, re-dated or repaired.

Machine copy of this report and the receipts: `.ufo/waves/round-90/w2/stage/CriticClaims/`.
