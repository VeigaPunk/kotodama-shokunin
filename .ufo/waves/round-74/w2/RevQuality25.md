# RevQuality25 — falsify attack on QUALITY criterion 25 (round 74, wave 2)

Seat: RevQuality25 (leaf). Target: `corpus/QUALITY.md` criterion 25, lines 81–123, landed at
`5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3` (claim Ca lands; `git log -S` confirms the commit).
Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; operative freeze
`00c408a0af2fa5ddf65af2224152ce258b26d896`; claim C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`.
Counters: `reports/round-74/accept-c.py` sha256 `8d30487fa4692261edfee549d2ba07517fc8b3c9fc4f5af5f0562a504ca5433a`,
`reports/round-74/accept-ca.py` sha256 `8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f`
(both equal the criterion's measured table).

Method: read the frozen criterion and both counter sources, then executed the counters only inside a
disposable clone (`/tmp/tmp.MhlkpoGwqN/lane`, `git clone` of the lane, local `main` moved per probe as
the counters require). No lane byte was written except this report; no fleet byte was written. No tool
was installed; pacman was not run. No `lsp` device is mounted (`read xd://lsp` → "No such tool";
mounted devices: ast_edit, debug, tripo_*, unity_cli_status), so caller/definition checks were done by
reading the counter source and by executing it; `grep` was used only to locate literals.

## Verdict

The criterion does **not** survive. Two BLOCKERs (F1, F2), two HIGHs (F3, F4), three MEDIUMs
(F5–F7), two LOWs (F8, F9). F1 and F2 are self-falsifications: the criterion's own definition of
"the freeze commit" matches no commit in the round, and its own acceptance sentence ("A fixture the
round-74 counter does not fail on its named leg fails this criterion", line 84) is failed by the
J4/J4b receipts it cites.

---

## F1 — BLOCKER — the freeze-artifact claim is false on three counts

**Text** (lines 82 and 84): "the freeze commit is the commit that adds `claims.json`, `ledger.json`,
both counters, the do-nothing receipts and the junk-landing receipts"; "The freeze commit carries
`counters/junk-fixtures.py` and four receipts under `reports/round-<N>/telemetry/`: `junk-c.txt` …,
`junk-ca.txt` …, `controls-c.txt` and `controls-ca.txt`."

**Shipped**:

```
$ git ls-tree -r --name-only 00c408a0af2fa5ddf65af2224152ce258b26d896 | grep -E 'round-74/telemetry/(junk|controls)'
reports/round-74/telemetry/controls-c.txt
reports/round-74/telemetry/controls-ca.txt

$ git log --oneline --diff-filter=A -- reports/round-74/telemetry/junk-c.txt
1d7add3 round-74: junk-landing receipts, measured receipts at each claim's own landing, wave-2 builder

$ git cat-file -e 00c408a0af2fa5ddf65af2224152ce258b26d896:counters/junk-fixtures.py
fatal: path 'counters/junk-fixtures.py' does not exist in '00c408a0af2fa5ddf65af2224152ce258b26d896'

$ git ls-tree -r --name-only 00c408a0af2fa5ddf65af2224152ce258b26d896 | grep junk-fixtures
.ufo/waves/round-74/counters/junk-fixtures.py

$ git show --stat --oneline 00c408a0af2fa5ddf65af2224152ce258b26d896
 .ufo/waves/round-74/counters/accept-ca.py | 172 +++++++++++++++++++----------
 .ufo/waves/round-74/w1/ExecCaCounter.md    |  97 ++++++++++++++++
 reports/round-74/accept-ca.py              | 172 +++++++++++++++++++----------
 reports/round-74/telemetry/selftest-ca.txt |   4 +-
 4 files changed, 331 insertions(+), 114 deletions(-)
```

(i) No `counters/junk-fixtures.py` exists anywhere in the lane or the fleet root (`ls` → no such
directory); the generator is `.ufo/waves/round-74/counters/junk-fixtures.py`.
(ii) `junk-c.txt` and `junk-ca.txt` are **not** at the operative freeze; they were added at
`1d7add3`, after both claim landings (`5e4796c`, `c4bf61a`).
(iii) The operative freeze adds none of the artifacts the definition names — only `accept-ca.py` and
`selftest-ca.txt`. No commit adds all six: `de93d91` adds claims/ledger/counters/generator,
`3595c91` adds the two control receipts, `1d7add3` adds the junk receipts.
(iv) The freeze's generator is not the generator that produced the receipts:

```
$ for c in de93d91 3595c91 00c408a0 1d7add3; do git show "$c:.ufo/waves/round-74/counters/junk-fixtures.py" | sha256sum; done
d4789c39740de5b6679e63f8fe0b2c54794f9eb358c8e8ab4660de622de9693f  -
d4789c39740de5b6679e63f8fe0b2c54794f9eb358c8e8ab4660de622de9693f  -
d4789c39740de5b6679e63f8fe0b2c54794f9eb358c8e8ab4660de622de9693f  -
ce6505fc7d973ced8ad663ee5201eae4931129684dd9794744f115a49fba6d76  -
```

The receipts name `generator sha256 ce6505fc…` (junk-c.txt:1, junk-ca.txt:1), i.e. the `1d7add3`
bytes, not the freeze's `d4789c39…`.

Answering the seat's receipt question directly: **both `junk-c.txt` and `junk-ca.txt` exist**
(`git cat-file -e HEAD:reports/round-74/telemetry/junk-c.txt` and `…junk-ca.txt` both exit 0; they are
committed at `1d7add3`). The defect is not an invented receipt; it is the criterion's claim that the
**freeze** carries them, plus the nonexistent generator path.

**Why it matters**: a reviewer who applies the criterion to round 74 as written looks for the junk
receipts at the freeze and finds them absent, or runs the freeze's generator and gets a different
fixture set than the filed receipts. The Ca junk receipts cannot be pre-data in principle: they
measure the Ca landing at its own commit (junk-ca.txt:64-66, `measures-ca.txt`), so the requirement is
unsatisfiable for claim Ca as the criterion states it.

**Proposed rewrite** (replace lines 82 and the first sentence of (b)):

> Scope: … the freeze is the commit that adds `claims.json`, `ledger.json`, both counters and the
> do-nothing receipts (`controls-c.txt`, `controls-ca.txt`); it also carries the generator revision
> present before data. The junk-landing receipts are post-records evidence: they are committed after
> both claims land, in a named receipts commit that carries the generator revision which produced
> them, and no frozen predicate cites them. Round 74: freeze `00c408a0…` carries the generator at
> `.ufo/waves/round-74/counters/junk-fixtures.py` sha256 `d4789c39…`; receipts commit `1d7add3`
> carries generator sha256 `ce6505fc…`, which is the sha the two junk receipts name.
>
> (b) **The junk landings the counter must reject are filed with their generator.** `junk-c.txt` and
> `junk-ca.txt` sit under `reports/round-<N>/telemetry/` at the receipts commit; each receipt names
> the generator's sha256, which equals `git show <receipts>:<generator> | sha256sum`, and each
> fixture's commit. A receipt whose generator sha does not equal the bytes at the receipts commit is
> a typed receipt and does not count.

(If the round wants the criterion's original strength, the only honest alternative is to re-cut a
freeze that carries the junk receipts — impossible for the Ca fixtures that measure a landing commit,
which is why the post-records shape is the accurate one.)

---

## F2 — BLOCKER — J4 and J4b never fail on their named leg (LEDGER)

**Text** (line 84 + table lines 91-92): "A fixture the round-74 counter does not fail on its named leg
fails this criterion"; `| J4 | every observe_cmd constant-prints … | LEDGER |`;
`| J4b | evasive constant printer … | LEDGER |`.

**Shipped** (`reports/round-74/telemetry/junk-ca.txt`):

```
$ awk '/^fixture:/{f=$2} /^LEG FAIL/{print f, $3}' reports/round-74/telemetry/junk-ca.txt
J4 APPENDONLY
J4 SEPARABLE
J4 FROZENCFG
J4b APPENDONLY
J4b SEPARABLE
J4b FROZENCFG
J5 ANNOTATE
…
$ grep -c "LEG FAIL LEDGER" reports/round-74/telemetry/junk-ca.txt
0
```

J4's own block (junk-ca.txt:71-85) reads
`LEG FAIL FROZENCFG … problems=1 ['reports/round-74/ledger.json was edited in the graded tree after freeze …']`
and `expected: FAIL: graded-tree ledger observe_cmds constant-print expected_after (FROZENCFG; LEDGER if read from the tree)`.
So the receipt itself says the named leg is FROZENCFG, not LEDGER.

**Why it cannot be otherwise as built**: the LEDGER leg reads the ledger at the freeze —
`measures-ca.txt` prints `LEG PASS LEDGER … source=freeze`, and `accept-ca.py`'s `load_frozen` reads
`git show <freeze>:reports/round-74/ledger.json`. A fixture that edits the ledger only in the graded
tree can never make LEDGER read the constant printers; FROZENCFG rejects the tree first. The fixture
tests a different channel than the table claims.

**Why it matters**: by the criterion's own sentence, round 74 fails criterion 25. The class the
criterion exists to close (round-73 M1b constant printers accepted by LEDGER) has no shipped fixture
that exercises LEDGER with a junk ledger.

**Proposed fix** (rebuild the fixture, then align the table):

1. Build J4/J4b so the **freeze commit** carries the constant-printer ledger (the generator already
   builds per-fixture freezes; use the fixture's own freeze, not a graded-tree edit), and land a child
   commit whose ledger matches that freeze. The counter then reads the junk ledger through
   `source=freeze` and LEDGER must go red. Keep the graded-tree edit as a third fixture.
2. Rewrite the table rows exactly:

> | J4 | the fixture's freeze commit carries a ledger whose every `observe_cmd` constant-prints
> `expected_after` (literal `python3 -c print` / `echo`), and the graded tree's ledger matches that
> freeze | LEDGER |
> | J4b | same, with the evasive printer (`import os;print(str(…))`) | LEDGER |
> | J4c | the graded tree's `ledger.json` is edited after freeze (constant printers) | FROZENCFG |

3. Add the differential requirement (see F3) so a green-at-T0 leg is a precondition.

---

## F3 — HIGH — J6 and J7 are not differential: their named legs are already red at T0

**Text** (line 84): "A fixture the round-74 counter does not fail on its named leg fails this
criterion." The sentence checks only that the leg is red, not that the junk caused it.

**Shipped**:

```
$ grep -n "^T0 Ca:" reports/round-74/telemetry/junk-ca.txt
58:T0 Ca: FAIL legs=9/11 exit=1 red=APPENDONLY,SEPARABLE
```

At the reference landing T0 (no junk) Ca is already red on APPENDONLY and SEPARABLE — the two legs
J6 and J7 are supposed to test. J6's APPENDONLY detail (junk-ca.txt:125-126) carries the baseline
problem `corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]` **plus** the junk's
`reports/round-73/telemetry/measures-ca72-rerun.txt` problem; J7's SEPARABLE detail carries the
baseline `cites <redacted lane id> in reports/round-74/telemetry/controls-ca.txt` **plus** the junk's
`corrections-rows` citation. A counter that ignored the junk entirely would print the same two
`LEG FAIL` lines and the same verdict shape. The receipt's own NOTE (junk-ca.txt:64-66) discloses
why: the combined landing kit conflicts with claim C's used-by edit, so Ca is red at T0 and is only
green at its own landing commit (`measures-ca.txt`, PASS 11/11).

**Why it matters**: the fixtures cannot show that the counter detects the J6/J7 junk; the red is
inherited. (J5 is differential — ANNOTATE is green at T0 — and J8/J9 are differential for RECEIPTS and
FROZENCFG.)

**Proposed fix** — add to (b), after the "fails on its named leg" sentence:

> Each fixture is differential: at the reference landing its named leg is green, and it is red only
> when the junk is applied. A fixture whose named leg is already red at the reference landing is not a
> control and does not count. Round 74: build the Ca fixtures on the Ca-only landing tree, where the
> reference landing prints `ACCEPT-CA-74: PASS legs=11/11` (`measures-ca.txt`), not on the combined
> landing kit where APPENDONLY and SEPARABLE are red for claim-conflict reasons (junk-ca.txt:58, :64-66).

---

## F4 — HIGH — `accept-c.py` returns PASS at `--lands == --freeze`; `accept-ca.py` refuses

**Text** (line 83): "(`<lands>` equal to `<freeze>` is graded, never passed: it is the do-nothing
control)".

**Shipped** — C grades and **passes** at the claim-C landing used as its own freeze:

```
$ python3 -B reports/round-74/accept-c.py --root . \
    --lands c4bf61a8d722f9168ce0fd8021a6261c000610c5 \
    --freeze c4bf61a8d722f9168ce0fd8021a6261c000610c5 \
    --fleet-root /home/vgpnk/Projects/shokunin
…
LEG PASS FROZENCFG
     constants from git show c4bf61a8d722:reports/round-74/claims.json (sha256 270e31790e2932c8): …
LEG PASS INDEX
ACCEPT-C-74: PASS legs=13/13
exit=0
```

Ca refuses the same shape (its guard, `accept-ca.py:2045-2047`):

```
LEG PASS … (11 legs)
ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: freeze == lands and every leg green: the do-nothing shape cannot pass)
exit=2
```

C has no post-run guard: `grep -n "do-nothing\|lands == freeze\|freeze == lands\|cannot pass"
reports/round-74/accept-c.py` returns only a comment (line 50), the base refusal (line 1947), a
selftest fixture (lines 2534-2538), and the selftest scenario (lines 2901, 2975-2980). Its
`freeze-eq-lands` scenario (lines 2900-2913) covers only the pre-landing freeze
(`--lands == --freeze == 00c408a`), where the data legs fail; it never exercises the all-green shape.

**Why it matters**: with `--freeze == --lands`, `load_frozen_config` (`accept-c.py:542`) computes
`frozen_sha256` from the same bytes `leg_frozencfg` compares against (`accept-c.py:1692`), so the
FROZENCFG pin is vacuous. A caller who passes a landing commit as its own freeze grades the landing
against its own `claims.json` — the exact "a landing can shrink its own test" channel the criterion
was written to close (J3 proves the real freeze catches it; this invocation bypasses the pin). The
filed do-nothing control itself is correct (`controls-c.txt:34-59`, FAIL 4/13 at
`--lands == --freeze == 00c408a`), so this is a caller-reachable hole, not a wrong receipt.

**Proposed fix** — port Ca's guard into C, after `passed, total, _results = run_legs(ctx)` in `main`:

```python
    ok = passed == total
    if ok and lands == freeze:
        return refuse("lands == freeze and every leg green: the do-nothing shape cannot pass")
```

and add the selftest scenario (mirroring `accept-ca.py:2045` and the round-74 C selftest style):

```python
    scenario("freeze-eq-lands-green")
    r = _run_counter(lane, fleet, lands, lands)   # a landing commit as its own freeze
    if r.returncode != 2 or "the do-nothing shape cannot pass" not in r.stdout:
        failures.append("lands==freeze green: expected a refusal, got %d\n%s"
                        % (r.returncode, r.stdout))
```

(The criterion's parenthetical then becomes true for both counters. If the round prefers the
"graded, never passed" wording, the guard must force `FAIL` with `legs=<n>/<n>` instead of refusing;
the two must agree.)

---

## F5 — MEDIUM — the refusal verdict line is missing on input errors, and Ca's template differs

**Text** (line 83): "refuses to grade — exit 2, verdict line `FAIL legs=0/<n> (refused: …)`, never a
PASS — when a revision is not a 40-hex commit, … when the frozen `claims.json` cannot be read at
`<freeze>`".

**Shipped**:

```
$ python3 -B reports/round-74/accept-c.py --root . --lands deadbeef --freeze 00c408a0… --fleet-root …
ERROR: --lands must be a 40-hex commit (the worktree is never graded, QUALITY 19)
exit=2

$ python3 -B reports/round-74/accept-ca.py --root . --lands deadbeef --freeze 00c408a0… --fleet-root …
ERROR: --lands must be 40 hex
exit=2

$ python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0… --freeze f7104cbce186… --fleet-root …
ERROR: claims file reports/round-74/claims.json is not committed at --freeze f7104cbce186bc2e1522abf0cfd619cc834628bb
exit=2
```

No verdict line is printed for the malformed revision (both counters), for a 40-hex non-commit
(both), or for Ca's unreadable frozen claims. C's unreadable-claims path does refuse with the line
(`ACCEPT-C-74: FAIL legs=0/13 (refused: cannot read reports/round-74/claims.json at freeze …)`).

Also, Ca's refusals use `(REFUSED:` (uppercase) and its LEGCOUNT line does not carry the literal
token `LEGCOUNT`:

```
$ python3 -B reports/round-74/accept-ca.py --root . --lands 9a59bf03… --freeze 9a59bf03… --fleet-root …
ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: leg table ['LEDGER', …] != the frozen 11 legs ['LEDGER', …, 'STAMP'])
exit=2
```

so a literal check for `FAIL legs=0/<n> (refused: LEGCOUNT …)` (clause (c)) fails on Ca.

**Proposed fix** (counter side, because the uniform contract is the stronger bar): route the
remaining input errors through the refusal printer — C: the 40-hex, not-a-commit and frozen-base
paths at `accept-c.py:1925-1959`; Ca: the argument and 40-hex paths at `accept-ca.py:2827-2838`
and the `load_frozen` error at `accept-ca.py:1947-1951`; make Ca's LEGCOUNT message begin
`LEGCOUNT: ` and use lowercase `refused:`. If the round prefers the shipped split, rewrite line 83 to:

> … refuses to grade (exit 2) with `ERROR: …` on stderr and no verdict line when a revision is
> malformed, is not a commit, or is not found; and with the verdict line
> `FAIL legs=0/<n> (refused: …)` when `<lands>` equals the frozen base, the frozen config cannot be
> read, LEGCOUNT disagrees, or the do-nothing shape is all green.

---

## F6 — MEDIUM — a freeze off the lands first-parent chain is a FROZENCFG leg FAIL, not a refusal; the criterion contradicts itself

**Text** (line 83, refusal list): "refuses to grade — exit 2, verdict line `FAIL legs=0/<n> (refused:
…)` … when `<freeze>` is not an ancestor of `<lands>` on the lands first-parent chain". The same
clause's FROZENCFG bullet says: "The FROZENCFG leg fails when … `<freeze>` is not on the lands
first-parent chain". Both cannot hold.

**Shipped** (freeze `3232093e…`, an ancestor-but-off-chain commit built in the clone):

```
$ python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8… --freeze 3232093e85e6362643151d46f01a3a9dbac980d5 --fleet-root …
LEG FAIL FROZENCFG
     freeze 3232093e85e6 is not on lands' first-parent chain | constants from git show 3232093e85e6:reports/round-74/claims.json …
ACCEPT-C-74: FAIL legs=12/13
exit=1

$ python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0… --freeze 3232093e85e6… --fleet-root …
LEG FAIL FROZENCFG
     … problems=1 ['--freeze 3232093e85e6 is not an ancestor of --lands 5e4796c0cb6a']
ACCEPT-CA-74: FAIL legs=10/11
exit=1
```

The counters' own selftests agree with the leg, not the refusal: C's `freeze-descendant` scenario
(`accept-c.py:2917-2921`) expects `LEG FAIL FROZENCFG`; Ca's `freeze-off-first-parent` scenario
(`accept-ca.py:2547-2556`) expects exit 1 with `FROZENCFG` FAIL.

**Proposed fix** — delete the chain condition from the refusal list in line 83 and leave it only in
the FROZENCFG bullet:

> … refuses to grade — exit 2, verdict line `FAIL legs=0/<n> (refused: …)`, never a PASS — when a
> revision is not a 40-hex commit, when `<lands>` equals the frozen base, when the frozen
> `claims.json` cannot be read at `<freeze>`, when the frozen leg list and the counter's own leg
> table disagree (LEGCOUNT, clause (c)), or when `<lands>` equals `<freeze>` and every leg is green
> (the do-nothing shape). A `<freeze>` off the lands first-parent chain is a FROZENCFG leg FAIL
> (exit 1), not a refusal.

---

## F7 — MEDIUM — `accept-ca.py` does not print `# frozen legs: <n> (<NAMES>)`

**Text** (line 97): "the counter … prints `# frozen legs: <n> (<NAMES>)` in the receipt".

**Shipped**:

```
$ grep -n "frozen legs" reports/round-74/accept-ca.py
(no output)
$ grep -l "frozen legs" reports/round-74/telemetry/*.txt
reports/round-74/telemetry/controls-c.txt
reports/round-74/telemetry/measures-c.txt
```

Only the C counter and C receipts carry the line; `measures-ca.txt`'s header has no leg list. On a
green Ca receipt the frozen leg set is invisible (it appears only inside a red FROZENCFG detail).

**Proposed fix** — add to Ca's receipt header, after the ledger line (`accept-ca.py:2004`):

```python
        print("# frozen legs: %d (%s)" % (len(cfg["leg_names"]),
                                          ",".join(cfg["leg_names"])))
```

or narrow the sentence to "claim C's counter prints …".

---

## F8 — LOW — the one-liner's gloss claims more than the regex tests

**Text** (lines 99-101): the line "meaning: a `git show <rev>:<path>` call is present, a `--freeze`
argument exists, and no `claims.json` path is joined from the graded materialization or the root."

**Shipped**: the third arm only matches a join that ends in the `CLAIMS` identifier. A join with an
inline path passes:

```
$ cat /tmp/RevQuality25/d4_inline_path.py   # --freeze present, real ("show","%s:%s"), graded read:
def load(mat, lands, freeze):
    _frozen = show(freeze, "reports/round-74/claims.json")
    return open(os.path.join(mat, "reports/round-74/claims.json")).read()

$ sh -c 'grep -q -- --freeze "$1" && grep -qE "\"show\", *\"%s:%s\"" "$1" && ! grep -qE "os\.path\.join\((mat|root|clone|treework)[^)]*CLAIMS" "$1"' _ /tmp/RevQuality25/d4_inline_path.py
exit=0
```

The stated limits (lines 116-121) cover this in spirit ("grep reads shape, not dataflow, so a counter
can pass this one-liner while reading the graded tree"), but the gloss asserts the absence of a
graded-root join, and the table's "why" column ("no graded-root join") states it as established.

**Proposed fix** — replace the gloss with:

> … and no `claims.json` path is joined from the graded materialization or the root **through the
> `CLAIMS` identifier** (an inline path or an aliased constant passes the one-liner; see Limits and
> the D4 row below).

and add the measured row `| decoy: `--freeze` + real show + `os.path.join(mat, "<literal claims path>")` | **0** | the stated limit |`.

---

## F9 — LOW — receipt enumeration, "one line", and "the same fixture" do not match the receipts

**Text** (line 84): "`junk-c.txt` (J1–J3), `junk-ca.txt` (J4, J4b, J5–J7)"; "one line naming the
fixture, its commit and the command …"; "the verdict the round-73 counters returned on the same
fixture — the red-before".

**Shipped**:

* `junk-c.txt` also carries J9 (`fixture: J9`, section C); `junk-ca.txt` also carries J8 and J9
  (lines 149-179). The parentheticals are incomplete.
* The per-fixture block is multi-line (`fixture:`, `section:`, `claim:`, `lands:`, `command:`,
  `exit:`, `LEG FAIL`, `verdict:`, `expected:`, `accepted:`), not one line.
* The red-before table is the round-73 analogue, not the same fixture: its junk paths are round-73
  paths (`reports/round-73/claims.json`, `corpus/knowledge/linguistics/conlang-scholarship…`,
  junk-c.txt:20-29), while the round-74 sections use round-74 paths and the wave-1 landing kit.
  The J6 row's example `(`ACCEPT-CA-72` FAIL→PASS)` is the round-73 red-before's target; the round-74
  J6 edits `reports/round-73/telemetry/measures-ca72-rerun.txt`, whose committed content is
  `ACCEPT-CA-72: PASS legs=12/12` (`git show 1d7add3:reports/round-73/telemetry/measures-ca72-rerun.txt`).

**Proposed fix** — rewrite line 84's parentheticals and phrasing:

> `junk-c.txt` (J1–J3, J9), `junk-ca.txt` (J4, J4b, J5–J9). Each junk receipt carries, per fixture,
> one block naming the fixture, its commit and the command, the counter's own `LEG FAIL <LEG>` line
> and its exit code, and the verdict the round-73 counters returned on the corresponding round-73
> analogue — the red-before. The red-before is a round-73 fixture built from round-73 bytes, never the
> round-74 fixture replayed, and the receipt says so.

and replace the J6 example with the round-74 target (`measures-ca72-rerun.txt`, in-place edit of a
round-73 rerun receipt outside both protected sets).

---

## Attacks that FAILED (the claim survived) — evidence

1. **The one-line check on the four counters: `0 0 1 1` as stated.**
   ```
   $ for f in reports/round-74/accept-c.py reports/round-74/accept-ca.py reports/round-73/accept-c.py reports/round-73/accept-ca.py; do sh -c 'grep -q -- --freeze "$1" && grep -qE "\"show\", *\"%s:%s\"" "$1" && ! grep -qE "os\.path\.join\((mat|root|clone|treework)[^)]*CLAIMS" "$1"' _ "$f"; echo "$? $f"; done
   0 reports/round-74/accept-c.py
   0 reports/round-74/accept-ca.py
   1 reports/round-73/accept-c.py
   1 reports/round-73/accept-ca.py
   ```
   The table's shas also match the freeze bytes (`8d30487f…`, `8052f1e2…`).
2. **Decoys D1 (comment-only literal, no `--freeze`) and D2 (`--freeze` + comment literal +
   `open(os.path.join(mat, CLAIMS))`) are caught**: exit 1 each (`/tmp/RevQuality25/d1_comment.py`,
   `d2_freeze_graded.py`), matching the two decoy rows in the table.
3. **Decoys D3 (`--freeze` + real show + graded literal read) and D5 (show called with `--lands`) pass
   the one-liner (exit 0)** — this is the criterion's stated limit, and it is stated honestly:
   "The one-liner also cannot prove the `git show` argument is the `--freeze` value, nor that a
   second read path is absent" (lines 118-120).
4. **The constants really are read at the freeze.** C: `load_frozen_config` at
   `accept-c.py:540-542`, map at `leg_frozencfg:1675-1690`; Ca: claims/ledger at
   `accept-ca.py:408, 557`. Receipts carry the promised lines:
   `# config source: git show 00c408a0…:reports/round-74/claims.json (never the graded tree)` and
   `# config sha256 (frozen claims.json): 270e31790e2932c8…` (controls-c.txt:12-13);
   `# freeze: 00c408a0… (config read at this commit only)` and
   `# ledger: reports/round-74/ledger.json source=freeze sha256=88d5fd52…` (measures-ca.txt:7,12).
5. **LEGCOUNT refusal works** (wording aside, F5): C `FAIL legs=0/13 (refused: LEGCOUNT: the frozen
   claims.json lists 12 legs …)`, exit 2; Ca `FAIL legs=0/11 (REFUSED: leg table … != the frozen 11
   legs …)`, exit 2, on a fixture freeze with one leg removed from each claim.
6. **`--lands == frozen base` is refused with the verdict line**: C
   `ACCEPT-C-74: FAIL legs=0/13 (refused: lands f7104cbce186 is the frozen claim base …)`, exit 2;
   Ca `ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: --lands equals the frozen base f7104cbce186)`, exit 2.
7. **C's unreadable frozen claims refuses with the verdict line** (P6); only Ca prints `ERROR:` (F5).
8. **No junk landing is accepted by the round-74 counters**: `junk-c.txt` ends
   `# ACCEPTED JUNK LANDINGS: none`; `junk-ca.txt` ends the same. J1/J2/J3 fail ENTRIES/EVIDENCE/
   FROZENCFG; J5 fails ANNOTATE; J8 fails RECEIPTS; J9 fails FROZENCFG. (Only J4/J4b and the
   differential issue in J6/J7 remain, F2/F3.)
9. **The round-73 red-before is measured, five survivors as cited**: `ExecJunkFixtures.md:9` says
   "Five of the eight junk landings are accepted"; line 73 is the SURVIVORS line `J3 J4b J5 J6 J7`;
   the receipt table shows J3/J4b/J5/J6/J7 `PASS legs=… exit=0`.
10. **Round-73 citations are correct**: `reports/round-73/accept-ca.py:45` reads
    `LEGS (8, fixed at freeze)`, and `MutLandedCa.md:115` is the docstring/driver mismatch the
    criterion cites. The fleet round-73 report records `af65165` (seven hex).

## Residual risk and verification gaps

* **J3-against-its-own-freeze demo (F4, stronger form) is not run here.** The structural argument is
  exact — with `--freeze == --lands`, `frozen_sha256` is computed from the same bytes FROZENCFG
  compares against (`accept-c.py:542` vs `:1692`) — but the demonstration that a *junk* landing
  (J3's two-row/one-entry shrink) passes when used as its own freeze was not completed inside this
  seat's time. A reviewer can run the generator's J3 with `--keep` and re-run
  `accept-c.py --lands <J3 lands> --freeze <J3 lands>`; if it prints PASS, F4 escalates to BLOCKER.
* The junk receipts were not regenerated. I verified the committed receipt lines, the generator sha,
  and the fixture commits, but the fixture repos were removed (`junk-c.txt:44`), and the generator at
  the freeze (`d4789c39…`) differs from the one that produced the receipts (`ce6505fc…`, F1). A fresh
  `--keep` run is the closure's replay.
* I did not re-run the two counters' declared PASS commands (`legs=13/13`, `legs=11/11`); that is the
  main agent's acceptance check. My runs were refusal probes plus one all-green `lands==freeze` probe,
  all inside the clone.
* No `lsp` device is mounted, so no server-backed `references`/`definition`/`diagnostics` evidence
  exists for this attack; every claim above is backed by the committed source bytes, a git query, or
  the counter's own executed output. `grep` is used only to locate literals, never as semantic proof.
* Writes: this report, `/tmp/RevQuality25/*` (scratch and the generator workroot). No tool installed,
  no pacman, no fleet or lane mutation.
