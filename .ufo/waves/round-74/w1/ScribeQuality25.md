# ScribeQuality25 — QUALITY criterion 25 draft (round 74, wave 1 / scribe, hyaku run 7)

Seat: ScribeQuality25 (leaf; no delegation, no background jobs, no peer messages, no writes outside the two
assigned paths and `/tmp/ScribeQuality25/`).

**Report file:** `.ufo/waves/round-74/w1/ScribeQuality25.md` (this file).
**Draft written:** `.ufo/waves/round-74/drafts/quality-25.md` (11,448 B; sha256
`2582cf4f6d0d9eb8382fc10926cedf75f34fb6ca6ee538192c5ecb877d6ffe5c`). `corpus/QUALITY.md` was **not** written
(append-only, forbidden to this seat; the draft names where the block appends).

## Behavior

Drafted QUALITY criterion 25 in the shape of criteria 20-24 (bold title · "adds to criterion N" · Scope ·
lettered clauses · Check (red-before) · Limits, stated · Binds from · Grounded in), grounded in round-73 closure
routed defect 4 and the four wave-2 mutation reports, with the three required elements:

1. **The criterion text** — the append-ready block in `.ufo/waves/round-74/drafts/quality-25.md` §"The criterion,
   as it would be appended".
2. **A grep-able red-before check** — `/tmp/ScribeQuality25/check25.sh` (full source in Appendix A), reduced to
   three clause verdict lines: `CONFIG:`, `JUNK:`, `LEGTEXT:`.
3. **A one-line statement of what it does not cover** — draft §"What it does not cover (one line)".

The criterion's three requirements, as worded in the draft:

- **(a) Constants from the freeze commit** — required `--freeze <40hex>` beside `--lands`; refuses unless
  `git merge-base --is-ancestor <freeze> <lands>` exits 0 *and* `<freeze> != <lands>`; every constant class
  (`row_set` incl. staged pairing and renumber map, `entries` incl. word floor, `rejects` incl. families and
  forbidden ids, `ground` incl. fragments and base counts, `allowlists` incl. observe binaries/tool paths/dates)
  read with `git show <freeze>:reports/round-<N>/claims.json`; exactly one receipt line
  `# config source: claims.json @ <freeze-40hex> (freeze, strict ancestor of <lands-40hex>); constants: row_set, entries, rejects, ground, allowlists`;
  zero occurrences of `config source: lands tree` / `config source: lane worktree` in any receipt or counter.
- **(b) Five junk landings frozen with the counter** — `stub-entries`→ENTRIES, `rows-from-staged`→ROWS,
  `quote-outside-window`→EVIDENCE, `config-edit-in-graded-tree`→FROZENCFG, `constant-observe`→LEDGER; one receipt
  each under `reports/round-<N>/telemetry/junk/<slug>.txt`, present at the freeze commit
  (`git cat-file -e <freeze>:<receipt>` — a receipt committed with the lands does not count), each opening with
  `CONTROL <slug>: FAIL <LEG> ` followed by the counter's own `LEG FAIL <LEG>` line and `exit=1`.
- **(c) One text** — claims.json carries `"label"` + `"leg_sha256"` per leg; the counter holds the same
  name/digest and recomputes the digest from the freeze claims.json at run time; the receipt prints
  `LEG-TEXT <NAME> sha256=<digest>` once per leg and reports legs only for names printed there; one digest per
  name across the three places.

## Gates (what the criterion demands, and the evidence each was exercised)

| gate | requirement | how it was exercised | result |
|---|---|---|---|
| G1 freeze ancestry | freeze strictly ancestor of lands | `check25.sh` `ancestor=` clause; `good` fixture run with `freeze = <lands>` | `ancestor=yes` on the valid pair, `ancestor=no` + `CONFIG: FAIL` when sealed — exercised |
| G2 config source | one line, five classes, no tree/worktree source | `good` vs `mut-a`; round-73 committed telemetry | `mut-a` → `CONFIG: FAIL ground=1 shape=0 forbidden=1`, exit 1 — exercised |
| G3 stamp agreement | receipt's `stamped`/`evaluated` == `<lands>` | `good`; round-73 red-before | `stamped=1 evaluated=1` green; round 73 → `0/0` red — exercised |
| G4 five controls | 5/5 present at freeze, slug↔leg pairing exact | `mut-b` (none), `mut-d` (post-data), `mut-e` (mispaired) | `controls=0/5 malformed=5`, `0/5 malformed=5`, `5/5 malformed=1` — three distinct reds, exit 1 each |
| G5 leg-text identity | one digest per name, three copies, count == claims legs | `mut-c` (counter table drifted), `mut-c2` (receipt drifted) | `LEGTEXT: FAIL claims=4 names=4 divergent=1` both, exit 1 |
| G6 green control | compliant round-74-shaped fixture passes everything | `good` | `CONFIG/JUNK/LEGTEXT: PASS`, exit 0 |

Verbatim run log (all seven fixtures, the sealed-freeze case, the valid case): `/tmp/ScribeQuality25/runs.txt`
(sha256 `f5e41319b7873ac2bbdbeb5980844c9cc19f67993f32ca7d6eed86da59d38126`); fixture generator
`/tmp/ScribeQuality25/mk.py` (sha256 `5cf83d5556c55ccd8f40e0f7721fdc7a5c2748e25e6486b5e7954b524d94ca54`);
checker `check25.sh` (sha256 `7fb19a999ac904db9ef6eb700a3e7bd7b6b5fb28b3e79c43f13cda06d060360d`).

### Red-before on real bytes

Round 73's own committed bytes (`lands 0316b8883b4f8d44b8efd720140e7f52f734a102`, `freeze
af65165cf269db346ef872e16a656eccd7264d01`, receipt `reports/round-73/telemetry/controls-c.txt`):

```
CONFIG: FAIL ground=1 shape=0 forbidden=2 ancestor=yes stamped=0 evaluated=0
JUNK: FAIL controls=0/5 malformed=5
LEGTEXT: FAIL claims=0 names=0 divergent=0
exit=1
```

The round-74 DRAFT as filed is red on clause (c): `grep -c '"leg_sha256"\|"label"' reports/round-74/claims.json`
= `0`, and `.ufo/waves/round-74/counters/` does not exist — so the freeze commit is the point at which this
criterion must turn green.

## Touched surfaces

- wrote `.ufo/waves/round-74/drafts/quality-25.md` (new).
- wrote `.ufo/waves/round-74/w1/ScribeQuality25.md` (this file).
- wrote `/tmp/ScribeQuality25/{mk.py,check25.sh,runs.txt,fx/*}` (throwaway; seven fixture repos under
  `/tmp/ScribeQuality25/fx/<name>/lane`, each `git init`-ed at its own path, identity `fx <fx@fx.invalid>` used
  only there).
- read-only: `reports/round-74/claims.json`, `corpus/QUALITY.md`, `corpus/lessons/round-73.md`,
  `corpus/lessons/round-73-verifier-spotcheck.md`, `.ufo/waves/round-73/w2/Mut*.md`,
  `reports/round-73/{accept-c.py,accept-ca.py,telemetry/*}`, `.ufo/waves/round-74/{build-w1.py,spec.json}`.
- no writes to the fleet repo, `/home/vgpnk/Projects/shokuknow`, `corpus/QUALITY.md`, `reports/round-74/claims.json`,
  `.ufo/state`, `SKILL.md`, `LOG.md`, `SCORECARD.md`; no git index or jj state change (only read-only `git
  rev-parse`/`rev-list`/`cat-file`/`merge-base` against the lane and the fixtures).

## Findings

1. **The round-74 draft claims cannot satisfy clause (c) as filed.** `reports/round-74/claims.json` has no
   `label`/`leg_sha256` key on any leg (12 claim-C legs, 11 claim-Ca legs, all plain strings). Either the frozen
   claims.json adds both keys, or the counter derives the digest from the leg sentence and prints it — the draft
   requires the former so the grep check can compare copies. Reported, not fixed (claims.json is not my write
   path).
2. **Round 73's counter hard-codes the forbidden literal in its own selftest.** `reports/round-73/accept-c.py:1646`
   reads `elif "# config source: lands tree: row_set, entries" not in r.stdout:` — under clause (a) that selftest
   fixture becomes a forbidden shape and the round-74 counter's scenario must assert the freeze-shape line
   instead. (This is also why the round-73 red-before prints `forbidden=2`: one receipt line plus this counter
   line.)
3. **Claim Ca's counter prints no `config source:` line at all.** `accept-ca.py` reports
   `# ledger: … source=lands sha256=…` instead; under clause (a) as worded, `G=0` → `CONFIG: FAIL`. That is
   intended (the criterion binds every counter), but the round-74 Ca counter must adopt the same header line —
   worth one line in the freeze dispatch so the executor does not discover it at grade time.
4. **Round 73 committed no PASS-at-lands receipt** (routed defect 2), so its red-before is taken over
   `controls-c.txt`; `stamped=0 evaluated=0` there is one finding (missing receipt) and not a second
   (wrong stamp). Stated in the draft's honesty block.
5. **The five controls span both counters**: `constant-observe`→LEDGER is a claim-Ca leg while the other four are
   claim-C legs. The criterion words the set per round ("the freeze commit ships five"), and the checker looks
   them up independently of `--cid`, so a split per counter would under-serve clause (b). No change needed; noted
   so the fixture builder is written once, not twice.

## Quotes used in the draft (verbatim, ≤25 words, with location and count)

| quote | location | `wc -w` |
|---|---|---|
| `the counter reads its acceptance contract from the graded tree; a landing can rewrite the frozen claims.json and shrink its own test` | `.ufo/waves/round-73/w2/MutPredicateC.md:71` | 22 |
| `eight junk landings pass 11/11 (stub bodies, forged evidence windows, shrunk row_set)` | `corpus/lessons/round-73.md:168` | 12 |
| `"truth" is a hardcoded constant` | `.ufo/waves/round-73/w2/MutLedgerCa.md:17` | 5 |
| `What the leg should check: classify every row of the refuse table` | `.ufo/waves/round-73/w2/MutLandedC.md:92` | 12 |
| `the three survivors are **counter-coverage gaps**, not proof the claim is wrong` | `.ufo/waves/round-73/w2/MutLandedC.md:10` | 12 |
| `` `leg_annotate` accepts any correction row that names the pair id `` | `.ufo/waves/round-73/w2/MutLandedCa.md:74` | 10 |
| `and *requires* 9 legs` | `.ufo/waves/round-73/w2/MutLandedCa.md:115` | 4 |
| `16 mutants, 4 survivors, 1 partial (M02).` | `.ufo/waves/round-73/w2/MutLandedCa.md:69` | 7 |
| `junk landings pass 11/11, config read from graded tree, ledger constant-printers` | `corpus/lessons/round-73-verifier-spotcheck.md:87` | 11 |

Each was checked for verbatim presence with `grep -Fn` against the file before it was quoted; counts are
`printf '%s' "<quote>" | wc -w`.

## Out of scope / not done (declared)

- **Did not write `corpus/QUALITY.md`** (forbidden to this seat and to this round's wave-1 scribes); the draft is
  append-ready but unwritten.
- **Did not edit `reports/round-74/claims.json`** (attack/check-only, per assignment).
- **Did not build or run a round-74 counter** (none exists at `.ufo/waves/round-74/counters/`); the check was
  exercised on purpose-built fixtures of the round-74 shape and on round-73's committed bytes.
- **Did not verify** that a real counter's `LEG-TEXT` block can be produced mechanically from claims.json (no
  counter exists to try), nor behaviour when the freeze claims file is unreadable, nor a cross-lane `--freeze`.
- No live fetches, no downloads, no captures — nothing in this assignment needed the web; no UA recording applies.
- No tools installed (python3 3.14 / git 2.56 / POSIX sh sufficed); pacman untouched.

## Appendix A — `/tmp/ScribeQuality25/check25.sh` (verbatim, sha256 `7fb19a99…060360d`)

```sh
#!/bin/sh
# check25.sh <lane-root> <lands> <freeze> <counter-id> [round] [receipt-path]
# The QUALITY-25 check (draft quality-25.md), one verdict line per clause:
#   CONFIG  — <freeze> is a strict ancestor of <lands>; the receipt's stamped/evaluated revisions are <lands>;
#             the config-source line names the freeze commit for all five constant classes;
#             no graded-tree or worktree config source appears in the receipt or the counter source
#   JUNK    — five junk landings, one committed receipt each present at the freeze commit,
#             each naming its own leg, one control line apiece
#   LEGTEXT — one digest per leg name across claims.json, the counter's leg table and the receipt
# Exit 0 only when all three clauses pass; a missing input fails closed.
set -u
ROOT=$1
LANDS=$2
FREEZE=$3
CID=$4
ROUND=${5:-74}
R=reports/round-$ROUND
CLAIMS=$R/claims.json
RECEIPT=${6:-$R/telemetry/measures-$CID.txt}
COUNTER=$R/accept-$CID.py
fail=0

G=$(grep -Ec 'config source:' "$ROOT/$RECEIPT" 2>/dev/null); G=${G:-0}
S=$(grep -Ec "config source: claims\\.json @ [0-9a-f]{40} \\(freeze, strict ancestor of [0-9a-f]{40}\\); constants: (row_set|entries|rejects|ground|allowlists)(, (row_set|entries|rejects|ground|allowlists)){4}\$" "$ROOT/$RECEIPT" 2>/dev/null); S=${S:-0}
F=$(grep -E 'config source: (lands tree|lane worktree)' "$ROOT/$RECEIPT" "$ROOT/$COUNTER" 2>/dev/null | wc -l)
ST=$(grep -Ec "^# stamped revision: $LANDS\$" "$ROOT/$RECEIPT" 2>/dev/null); ST=${ST:-0}
EV=$(grep -Ec "^# evaluated revision: $LANDS\$" "$ROOT/$RECEIPT" 2>/dev/null); EV=${EV:-0}
ANC=no
if [ "$FREEZE" != "$LANDS" ] && git -C "$ROOT" merge-base --is-ancestor "$FREEZE" "$LANDS" 2>/dev/null; then ANC=yes; fi
if [ "$G" -ge 1 ] && [ "$G" -eq "$S" ] && [ "$F" -eq 0 ] && [ "$ANC" = yes ] && [ "$ST" -eq 1 ] && [ "$EV" -eq 1 ]; then
  echo "CONFIG: PASS ground=$G shape=$S forbidden=$F ancestor=$ANC stamped=$ST evaluated=$EV"
else
  echo "CONFIG: FAIL ground=$G shape=$S forbidden=$F ancestor=$ANC stamped=$ST evaluated=$EV"; fail=1
fi

J=0; JBAD=0
for pair in stub-entries:ENTRIES rows-from-staged:ROWS quote-outside-window:EVIDENCE config-edit-in-graded-tree:FROZENCFG constant-observe:LEDGER; do
  slug=${pair%%:*}; leg=${pair##*:}
  git -C "$ROOT" cat-file -e "$FREEZE:$R/telemetry/junk/$slug.txt" 2>/dev/null || { JBAD=$((JBAD+1)); continue; }
  n=$(grep -Ec "^CONTROL $slug: FAIL $leg( |\$)" "$ROOT/$R/telemetry/junk/$slug.txt")
  [ "$n" -eq 1 ] || JBAD=$((JBAD+1))
  J=$((J+1))
done
if [ "$J" -eq 5 ] && [ "$JBAD" -eq 0 ]; then
  echo "JUNK: PASS controls=5/5"
else
  echo "JUNK: FAIL controls=$J/5 malformed=$JBAD"; fail=1
fi

L=$(grep -cE '"leg_sha256":' "$ROOT/$CLAIMS" 2>/dev/null); L=${L:-0}
NAMES=$(grep -h -oE '^LEG-TEXT [A-Z]+ sha256=[0-9a-f]{64}$' "$ROOT/$COUNTER" "$ROOT/$RECEIPT" 2>/dev/null | awk '{print $2}' | sort -u)
W=0; C=0
for n in $NAMES; do
  C=$((C+1))
  u=$(grep -h -oE "LEG-TEXT $n sha256=[0-9a-f]{64}" "$ROOT/$COUNTER" "$ROOT/$RECEIPT" 2>/dev/null | sed 's/.*sha256=//' | sort -u | wc -l)
  [ "$u" -eq 1 ] || W=$((W+1))
done
if [ "$C" -eq "$L" ] && [ "$W" -eq 0 ] && [ "$L" -gt 0 ]; then
  echo "LEGTEXT: PASS claims=$L names=$C divergent=$W"
else
  echo "LEGTEXT: FAIL claims=$L names=$C divergent=$W"; fail=1
fi

exit $fail
```

## Post-wave update (L1 follow-up, 2026-10-25 22:09 local)

The draft at `.ufo/waves/round-74/drafts/quality-25.md` is now **revision 2**: 13522 B, sha256
`0739c68b794d6b07b12ca223a5b780ae315d54a1fee0c078389d386a9a7c2a31` (revision 1 was 11,448 B, sha256
`2582cf4f…d7ffe5c`; every statement about revision 1 above is kept as history, not as the current text).

### What I read before rewriting

`.ufo/waves/round-74/w1/CritQuality25.md` (REJECT AS DRAFTED — fixable, not a tradeoff; measured that r1's own
checker passed a counter grading the graded tree, a receipt whose counter printed `ACCEPT-C-74: FAIL legs=0/2`,
and hand-typed junk receipts), `CritFrozenCfg.md` §4–§5 (the freeze scheme and the R0–R6 red-before commands),
`CritMistakeFix.md` (F4: r1's mandatory five slugs are not the round's J1–J7; F8: r1's forbidden-literal clause
fails on the round's own control receipts and r1's `leg_sha256` requirement is a foregone fail),
`RevClaimsFidelity.md` (F1: counter path), `ExecJunkFixtures.md` (the J1–J7 fixtures and the five survivors),
`drafts/mistakes.md` (R74-M3), and the shipped counters themselves.

### Re-measured shipped state (this is what the criterion now describes)

| fact | value / evidence |
|---|---|
| `.ufo/waves/round-74/counters/accept-c.py` | sha256 `b2dc1b64…`; 13 legs incl. `INDEX`; LEGCOUNT enforced in order (`LEGCOUNT: the frozen claims.json lists %d legs`); refusal `ACCEPT-C-74: FAIL legs=0/13 (refused: …)`, exit 2 |
| C constants | `git show <freeze>:reports/round-74/claims.json`; map via `git show <freeze>:<map.path>` hashed against frozen `map.sha256` |
| C FROZENCFG | fails when `<freeze>` not on `rev-list --first-parent <lands>`, base not an ancestor, map sha mismatch, or `claims.json` at `<lands>` sha256 ≠ frozen |
| C receipt | `# freeze revision:`, `# config sha256 (frozen claims.json):`, `# config source: git show <freeze>:reports/round-74/claims.json (never the graded tree)`, `# frozen legs: 13 (…)`, `# frozen map: …` |
| `.ufo/waves/round-74/counters/accept-ca.py` | sha256 `76d00b88…`; 11 legs; LEGCOUNT compares count+name set; refusal `ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: …)` |
| Ca FROZENCFG | freeze ancestor + first-parent chain, base ancestor of `<freeze>`, `claims.json`/`ledger.json` blob ids equal at `<freeze>` and `<lands>` (absent/mismatched → FAIL) |
| Ca receipt | `# freeze: <freeze> (config read at this commit only)`, `# ledger: reports/round-74/ledger.json source=freeze sha256=<h>` |
| junk fixtures | `counters/junk-fixtures.py` sha256 `d4789c39…`; J1–J7 (+J4b); the counters do not run them |
| the four receipts | **absent** — `reports/round-74/telemetry/` holds only `census-start.txt` |
| counter paths | bytes live at `.ufo/waves/round-74/counters/`; the criterion names `reports/round-74/accept-{c,ca}.py` per the L1 ruling and `RevClaimsFidelity` F1 |

### The grep-able one-liner (replaces r1's three-clause checker)

```
sh -c 'grep -q -- --freeze "$1" && grep -qE "\"show\", *\"%s:%s\"" "$1" && ! grep -qE "os\.path\.join\((mat|root|clone|treework)[^)]*CLAIMS" "$1"' _ <counter>
```

Measured runs (verbatim exit codes, 2026-10-25): shipped C `0`; shipped Ca `0`; `reports/round-73/accept-c.py`
`1` (no `--freeze`, joins `mat`/`root` with `CLAIMS`); `reports/round-73/accept-ca.py` `1` (no `--freeze`);
comment-decoy without `--freeze` `1`; decoy with `--freeze` + comment literal + `open(os.path.join(mat, CLAIMS))`
`1`; and the stated limit, a counter reading the graded tree under a literal path with a decoy `git show`, `0`.
Decoys: `/tmp/ScribeQuality25/{decoy.py,decoy2.py,limit.py}`.

### What revision 2 dropped or demoted, and why

- **Dropped:** r1's five slugs (`stub-entries`, `rows-from-staged`, `quote-outside-window`,
  `config-edit-in-graded-tree`, `constant-observe`) — the round ships J1–J7 (+J4b), and `CritMistakeFix` F4
  measured that r1's slug list and the round's fixtures differ; r1's per-leg `label`/`leg_sha256` + `LEG-TEXT`
  digest scheme — not shipped (`grep -c '"leg_sha256"\|"label"' reports/round-74/claims.json` = 0) and, per
  `CritQuality25` §2.1, satisfiable by prose while forcing a hard-coded digest into the counter; r1's
  forbidden-literal clause scoped over all receipts — `CritMistakeFix` F8 showed it reds on a correct round whose
  config control must print that literal.
- **Marked `proposed, not shipped`:** the `freeze.json` sidecar, the fleet-root freeze pin file, the
  counter-bytes pin with a `counter-revisions.md` door, the phantom-descendant divergence run and the checker's
  re-derivation of `# config sha256:`. None is implemented by the counters as shipped; the criterion does not
  require them.
- **Kept, as the L1 instructed:** constants via `git show <freeze>:…` (claims + ledger + map sha256), the refusal
  set (non-40-hex, non-ancestor / off the first-parent chain, lands == frozen base, unreadable frozen claims,
  LEGCOUNT), the L1–L7 junk controls with their four receipts, and one grep-able one-liner.
- **What the criterion does not cover, as worded:** a rewritten freeze commit is not lane-detectable — only an
  external pin can decide it, and today the fleet report records the freeze hash (7 hex in round 73); also not
  covered: that the freeze predates the first scoring seat, or that a fixture fails *only* its named leg.

### Findings from this update

1. **The counters moved three times during the revision** — C `e5290e51…` → `507b365b…` → `b2dc1b64…`, Ca
   `5b76e006…` → `fd0ad795…` → `76d00b88…`. At `507b365b…` C's docstring promised 13 legs while its table had 12 and loaded the frozen
   `legs[]` without comparing it; at `b2dc1b64…` both are fixed. Consequence: the criterion and any closure
   receipt must be stamped with the counter sha it describes, and r1's design (fixed line numbers, fixed leg
   count, printed digest table) is invalidated by exactly this churn — revision 2 phrases the rule behaviourally.
2. **The four control receipts the criterion requires do not exist yet** (`reports/round-74/telemetry/` holds
   only `census-start.txt`); the freeze commit must add `junk-c.txt`, `junk-ca.txt`, `controls-c.txt`,
   `controls-ca.txt`, or clause (b) is unverified.
3. **Neither counter runs the junk fixtures** (no reference to `junk-fixtures.py` in either source): the receipts
   must come from running the generator against the counters, and a hand-typed receipt is what `CritQuality25`
   §2.1 showed r1 could not tell apart. Revision 2 says so in clause (b).
4. **Path split unresolved in the tree:** the criterion names `reports/round-74/accept-{c,ca}.py`;
   the shipped bytes are at `.ufo/waves/round-74/counters/`. The freeze must land them at the named path
   (`RevClaimsFidelity` F1), otherwise Scope names a file that does not exist.

### Bounds of this update

- Writes: the draft (revision 2) and this appended section only; `/tmp/ScribeQuality25/` scratch. No QUALITY.md,
  no claims.json, no counter, no telemetry file, no git index or ref touched; the counters were read, never run.
- Everything above is a read of the named bytes at the named sha, plus seven runs of the pasted one-liner; the
  J1–J7 verdicts are `ExecJunkFixtures`' filed runs, not mine, and the round-74 junk receipts are predicted to
  fail their legs, not observed.
- No live fetch, no tool installed, pacman untouched.
