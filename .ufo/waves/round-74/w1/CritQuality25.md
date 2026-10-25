# CritQuality25 — attack on the QUALITY-25 plan (round 74 / hyaku run 7, wave 1)

Seat: CritQuality25 (leaf; no delegation, no background jobs, no peer messages). Read-only on the lane; the
only writes are this report and `/tmp/CritQuality25/` fixtures.

**Verdict: REJECT AS DRAFTED — fixable, not a tradeoff.** The draft
(`.ufo/waves/round-74/drafts/quality-25.md`, seat ScribeQuality25) closes the round-73 survivor class
*in words*: each of its three clauses is checked by grepping text the author of the counter writes. Measured
below: the draft's own red-before checker prints `CONFIG: PASS / JUNK: PASS / LEGTEXT: PASS`, exit 0, for a
counter that grades the graded tree, whose five "junk landings" were typed by hand and never run, and whose
verdict on the same bytes is `ACCEPT-C-74: FAIL legs=0/2`. Append it as filed and round 74 would enter
history as having fixed the class it leaves open — premature saturation, not a calibration gain.

What I read: `corpus/QUALITY.md` criteria 9, 11, 17, 19, 23 (/24 for the check idiom);
`corpus/lessons/round-73.md` (`## Mistakes` R73-M1..M8, `## Corrections`, the routed-defect list);
`corpus/lessons/round-73-verifier-spotcheck.md` §6 item 4; `reports/round-73/accept-c.py`
(`load_config`, :432-470; the `# config source:` printer :1146; the selftest's own forbidden literal :1646);
`reports/round-73/telemetry/controls-c.txt:13`; `.ufo/waves/round-73/w2/MutPredicateC.md` (F1, P7b);
`reports/round-74/claims.json`; the draft and the scribe report.

---

## 1. The three counter descriptions (lesson form) and the grep red-before

Each text is the form a `## Mistakes` row or a claim's `counter` field would carry. They are exactly the
artifacts the assignment names: (a) constants from the graded tree, (b) constants from the freeze with no junk
controls, (c) both requirements met. `text-a` describes the real round-73 counter; `text-b`/`text-c` are the draft's
shape, synthetic, with the measured fixture's freeze revision.

```
$ cat texts/a.txt
Counter r1 (round 73, real: reports/round-73/accept-c.py load_config, MutPredicateC F1). Takes --lands only; opens
reports/round-73/claims.json from the materialized tree and derives row_set, entries, rejects.* and
ground.fragments from it. No freeze commit, no junk landings: any landing rewrites the file it grades against.

$ cat texts/b.txt
Counter r2 (synthetic: the draft's clause (a) without clause (b)). Takes --freeze, refuses unless it is a strict
ancestor of --lands, and reads git show d0d5a44368534548f9e4c8c6b26cff7f9918e505:reports/round-74/claims.json.
Ships no junk landings and no fixture builder, so nothing shows its legs able to fail.

$ cat texts/c.txt
Counter r3 (synthetic: the full draft). Takes --freeze, refuses unless it is a strict ancestor of --lands, reads
git show d0d5a44368534548f9e4c8c6b26cff7f9918e505:reports/round-74/claims.json, and ships five junk landings
under reports/round-74/telemetry/junk/, each committed at the freeze, one receipt each:
CONTROL stub-entries: FAIL ENTRIES
CONTROL rows-from-staged: FAIL ROWS
CONTROL quote-outside-window: FAIL EVIDENCE
CONTROL config-edit-in-graded-tree: FAIL FROZENCFG
CONTROL constant-observe: FAIL LEDGER
```

**What the check must match.** Three occurrence counts per text (`grep -Eo … | wc -l`, never `grep -c`: a
wrapped record must not read as one hit — the `-c` form scores `text-c` as 5 only because each control happens
to sit on its own line, and scores a three-on-one-line record as 1):

| id | pattern | required | why |
|---|---|---|---|
| SHOW | `git show [0-9a-f]{40}:reports/round-[0-9]+/claims\.json` | ≥ 1 | a freeze read is named |
| TREE | `config source: (lands tree\|lane worktree)\|from the (materialized\|graded) tree` | = 0 | the graded tree is named as the constant source |
| CTL | `CONTROL [a-z-]+: FAIL (ENTRIES\|ROWS\|EVIDENCE\|FROZENCFG\|LEDGER)` | = 5 | five junk landings, each naming its own leg |

PASS iff `SHOW ≥ 1 ∧ TREE = 0 ∧ CTL = 5`.

```
$ for t in a b c; do s=$(grep -Eo "$SHOW" texts/$t.txt | wc -l); r=$(grep -Eo "$TREE" texts/$t.txt | wc -l);
>   k=$(grep -Eo "$CTL" texts/$t.txt | wc -l); echo "text-$t SHOW=$s TREE=$r CONTROLS=$k"; done
text-a SHOW=0 TREE=1 CONTROLS=0
text-b SHOW=1 TREE=0 CONTROLS=0
text-c SHOW=1 TREE=0 CONTROLS=5
$ for t in a b c; do echo "-- $t"; grep -En "$SHOW|$TREE|$CTL" texts/$t.txt; done
-- a
2:reports/round-73/claims.json from the materialized tree and derives row_set, entries, rejects.* and
-- b
2:ancestor of --lands, and reads git show d0d5a44368534548f9e4c8c6b26cff7f9918e505:reports/round-74/claims.json.
-- c
2:git show d0d5a44368534548f9e4c8c6b26cff7f9918e505:reports/round-74/claims.json, and ships five junk landings
4:CONTROL stub-entries: FAIL ENTRIES
5:CONTROL rows-from-staged: FAIL ROWS
6:CONTROL quote-outside-window: FAIL EVIDENCE
7:CONTROL config-edit-in-graded-tree: FAIL FROZENCFG
8:CONTROL constant-observe: FAIL LEDGER
```

So the predicate fails (a) on two counts (no freeze read, a named tree read), fails (b) on one (no controls),
and passes only (c) — **on prose**. That is the whole of the draft's red-before, and prose is not the artifact
under test. Section 2 runs the scribe's own `check25.sh` — the executable form of the same three clauses —
against counter *sources*.

---

## 2. Counterexamples, all measured on one fixture

Fixture: `/tmp/CritQuality25/fx/lane`, `git init -q` at that path, `git rev-parse --show-toplevel` = the same
path, identity `fixture-crit <crit@crit.invalid>` local to it; three commits
`base 5d4cc199… → freeze d0d5a443… → lands ec6a4452…`. The freeze commit carries
`reports/round-74/claims.json` (two legs with `label`+`leg_sha256`, as the draft's clause (c) demands), the
counter `reports/round-74/accept-c.py` (71 lines, sha256 `607572598045251acc7a98e607cb02f9ec7c482a2f0a5a15db16a1975cb18619`,
source listed in §6), and five
`reports/round-74/telemetry/junk/<slug>.txt` receipts. **The five receipts were typed by hand; no counter run
produced them.** Builder `mk.py` sha256 `d843f7bc…f2b9`; the scribe's checker copied verbatim,
`sha256 7fb19a999ac904db9ef6eb700a3e7bd7b6b5fb28b3e79c43f13cda06d060360d` = the sha quoted in the scribe
report.

The one counter has a run-time switch `CFG=` (test scaffolding only — the point is that the *source bytes* and
the *receipt* are identical across modes):

- `freeze` — constants from `git show <freeze>:reports/round-74/claims.json` (the honest counter);
- `tree` — constants from the graded tree, and the receipt's digest names the bytes it actually read;
- `tree-decoy` — constants from the graded tree, but the receipt's digest is computed from the freeze blob;
- `partial` — `row_set` from the freeze, `entries` from the graded tree.

### 2.1 The draft's check passes all four, at the lands revision

```
$ L=$(…lands…); F=$(…freeze…); R=reports/round-74; C=$R/accept-c.py    # values from /tmp/CritQuality25/fx-shas.json
$ for m in freeze tree tree-decoy partial; do
>   CFG=$m python3 -B $C --root . --lands $L --freeze $F > $R/telemetry/measures-c.txt; ce=$?
>   ck=$(sh check25.sh . $L $F c 2>&1); cke=$?
>   echo "mode=$m counter_exit=$ce verdict=$(tail -1 $R/telemetry/measures-c.txt) | check25_exit=$cke"; done
mode=freeze     counter_exit=0 verdict=ACCEPT-C-74: PASS legs=2/2 | check25_exit=0
mode=tree       counter_exit=0 verdict=ACCEPT-C-74: PASS legs=2/2 | check25_exit=0
mode=tree-decoy counter_exit=0 verdict=ACCEPT-C-74: PASS legs=2/2 | check25_exit=0
mode=partial    counter_exit=0 verdict=ACCEPT-C-74: PASS legs=2/2 | check25_exit=0

$ sh check25.sh . $L $F c            # the tree-reading counter's receipt
CONFIG: PASS ground=1 shape=1 forbidden=0 ancestor=yes stamped=1 evaluated=1
JUNK: PASS controls=5/5
LEGTEXT: PASS claims=2 names=2 divergent=0
```

Why each leg is blind:

- **CONFIG** reads the *receipt* for the `config source:` line and greps the *counter source* only for two
  forbidden literals. A counter that prints the line without any `git show` passes — **no tree read is
  required to be replaced, only a string to be written**. Round 73 was caught because its counter honestly
  disclosed itself (`reports/round-73/telemetry/controls-c.txt:13`, `# config source: lane worktree: …`); the
  defect class is *non-disclosure*, and a check keyed on disclosure cannot see it. The five constant classes
  in that line (`rejects`, `ground`, `allowlists` included) are **asserted**: this fixture's counter has no
  `rejects` and no `allowlists` code at all and `shape=1`.
- **JUNK** requires `git cat-file -e <freeze>:<receipt>` plus one line beginning `CONTROL <slug>: FAIL <LEG>`.
  It never re-runs anything and never binds the receipt to the counter bytes; five typed files satisfy it.
  The draft's own Limits line concedes the neighbouring case ("a receipt committed at the freeze can still
  have been produced from a later counter") but not this one: it can have been produced by *nothing*.
- **LEGTEXT** compares three author-written copies of a digest. It requires the counter's **source text** to
  carry column-0 `LEG-TEXT <NAME> sha256=<64hex>` lines, i.e. it *forces* a hard-coded digest table into the
  counter — the `constant-observe` class (`"truth" is a hardcoded constant`, MutLedgerCa.md:17) that the same
  criterion's junk landing is meant to catch. It also does not bind the sentence to the implementation: this
  fixture's ENTRIES leg sentence promises the provenance header, no placeholders, and a body at least as long
  as the smallest base entry, while its implementation checks `git cat-file -e` only — and LEGTEXT reports
  `divergent=0`.

### 2.2 The check passes a receipt whose own counter says FAIL

`L'` = a descendant of lands (ancestry preserved, as clause (a) demands) whose tree `claims.json` carries one
phantom id in `row_set` and one phantom path in `entries`:

```
$ for m in freeze tree tree-decoy partial; do CFG=$m python3 -B fx/l2/reports/round-74/accept-c.py \
>   --root fx/l2 --lands $LP --freeze $F > lp-$m.txt; echo "mode=$m exit=$? sha=$(sed -n 's/^# config sha256: //p' lp-$m.txt) $(tail -1 lp-$m.txt)"; done
freeze blob sha: 61ce7c87eb4b94a61786bae6316a70dd01f6a463c8dfb0c742d3020f0e7ff049
mode=freeze     exit=0 sha=61ce7c87…049 ACCEPT-C-74: PASS legs=2/2
mode=tree       exit=1 sha=f6fbb8c9…3d4 ACCEPT-C-74: FAIL legs=0/2
mode=tree-decoy exit=1 sha=61ce7c87…049 ACCEPT-C-74: FAIL legs=0/2
mode=partial    exit=1 sha=61ce7c87…049 ACCEPT-C-74: FAIL legs=1/2

$ cp lp-tree-decoy.txt fx/l2/reports/round-74/telemetry/measures-c.txt
$ sh check25.sh fx/l2 $LP $F c
CONFIG: PASS ground=1 shape=1 forbidden=0 ancestor=yes stamped=1 evaluated=1
JUNK: PASS controls=5/5
LEGTEXT: PASS claims=2 names=2 divergent=0
                                       # exit 0, while the receipt's own last line is ACCEPT-C-74: FAIL legs=0/2
```

The checker never reads the counter's verdict line, so a **failing** counter satisfies every QUALITY-25 clause
it defines. A criterion whose red-before is green on a FAIL receipt is not a criterion.

### 2.3 Two further measured defects in the check as written

- **Duplicate authority, weaker stand-in (QUALITY 11).** With `# tree:` set to forty zeros, check25 prints
  `CONFIG: PASS`, exit 0; the lane's existing `tools/check-receipt-seq.py` — which owns exactly this header
  grammar under QUALITY 17/19 — prints `TREE-… FAIL recorded=00000000 actual=b152f013 / RECEIPT-SEQ: FAIL`,
  exit 1. Two authorities over one receipt, and the round would quote the weaker one's PASS.
- **The forbidden-literal leg is self-defeating under QUALITY 23.** Appending one line to the counter,
  `# red-before note: the r73 counter printed "config source: lane worktree: row_set, entries"`, flips the
  verdict to `CONFIG: FAIL … forbidden=1`, exit 1 — same behaviour, only documentation. QUALITY 23 *requires*
  a red-before scenario that reproduces the old behaviour, and round-73's own counter already holds the literal
  at `reports/round-73/accept-c.py:1646`. As worded, (a) forbids the evidence (b)/(23) demands.
- **A fixed source regex cannot name the command anyway.** On the honest counter source,
  `grep -Eo 'git show [0-9a-f]{40}:reports/round-[0-9]+/claims\.json'` = 0 and even the variable-tolerant
  `git show [^ ]*:reports/round-[0-9]+/claims\.json` = 0: the call is an argv list
  (`g("show", "%s:%s" % (freeze, CLAIMS))`). Any literal pattern over source is one refactor away from a false
  negative, and the looser pattern that does match (`"show".*CLAIMS` = 1) is satisfied by the decoy.

---

## 3. Smallest wording that prose cannot satisfy, and the reviewer one-liner

Replace clause (a)'s method sentence ("Every constant … is read with
`git show <freeze>:reports/round-<N>/claims.json`") — satisfiable by a docstring — with a **value the counter
must print and the checker must re-derive**, plus one behavioural twin:

> (a) **The config is a value, not a claim.** The receipt prints `# config sha256: <h>`, the sha256 of the
> exact bytes the counter graded with, and the check requires
> `h = sha256($(git -C <lane> show <freeze>:reports/round-<N>/claims.json))`. **The freeze blob is
> load-bearing:** on a descendant of `<lands>` whose tree `claims.json` carries one phantom id in `row_set`
> and one phantom path in `entries`, the counter's verdict is unchanged. A clause that moves the verdict is
> read from the tree; the counter is not PASS unless both hold.

The number cannot be written, only produced by running the command (measured: the honest counter's receipt
carries `61ce7c87…049`, exactly `git show <freeze>:…claims.json | sha256sum`). The number alone is forgeable
(measured: the decoy prints the same one); the twin run is what kills the forger, and it must vary **every**
constant class, not just `row_set` — measured: with a `row_set`-only phantom, the `partial` reader (its
`entries` from the tree) still prints `ACCEPT-C-74: PASS legs=2/2`, and the same phantom with both classes
moves it to `FAIL legs=1/2`.

**Reviewer one-liner** (one physical line; run from the lane root with `L`, `F`, `R`, `C` set; tested on all
four fixture counters):

```
h=$(sed -n 's/^# config sha256: //p' "$R/telemetry/measures-c.txt"); [ "$h" = "$(git -C . show "$F:$R/claims.json" | sha256sum | cut -d' ' -f1)" ] && d=$(mktemp -d) && git clone -q . "$d/l" && git -C "$d/l" checkout -q "$L" && python3 -B -c 'import json,sys;p=sys.argv[1];d=json.load(open(p));c=[x for x in d["claims"] if x["id"]=="C"][0];c["row_set"].append({"id":"S999"});c["entries"].append("corpus/knowledge/culture-material/phantom.md");json.dump(d,open(p,"w"),indent=1)' "$d/l/$R/claims.json" && git -C "$d/l" -c user.name=r -c user.email=r@r.invalid commit -qam phantom && python3 -B "$d/l/$C" --root "$d/l" --lands "$(git -C "$d/l" rev-parse HEAD)" --freeze "$F" | grep -q "^ACCEPT-C-74: PASS" && echo "QUALITY-25-CFG: PASS" || echo "QUALITY-25-CFG: FAIL"
```

Measured against the same four counters, at the same lands revision, with the same receipts:

```
mode=freeze     | check25_exit=0 | QUALITY-25-CFG: PASS
mode=tree       | check25_exit=0 | QUALITY-25-CFG: FAIL
mode=tree-decoy | check25_exit=0 | QUALITY-25-CFG: FAIL
mode=partial    | check25_exit=0 | QUALITY-25-CFG: FAIL
```

It is round-agnostic in shape (`R`/`C` change per round; the phantom entry path is built in the claim's own
entry directory), needs no commit the reviewer does not already have, and the
`L'` clone is a plain descendant of `<lands>`, so clause (a)'s strict-ancestor gate is respected. It also
closes §2.2: a counter that prints its own FAIL cannot pass the `grep -q "^ACCEPT-C-74: PASS"` leg.

---

## 4. What in the draft must change (smallest safe correction)

1. **(a)** — adopt the §3 wording: printed `# config sha256:` + checker re-derivation + the phantom-descendant
   run that varies every class. Drop the two forbidden literals as verdict-bearing (they punish documenting the
   red-before, measured in §2.3); a `lane worktree` read is what the divergence run detects, whatever the source
   says.
2. **(b)** — a receipt is not a control. Either the checker re-runs a frozen builder
   (`sh tools/junk-landings.sh <lane> <freeze>`, `exit 0` only if each of the five fails its named leg) and
   compares its verdict lines with the committed receipts, or each receipt carries `# counter sha256 (self):`
   compared against `git show <freeze>:<counter>` and the exact command the reviewer repeats. Typed files must
   not count. Note also: `reports/round-74/claims.json`'s claim-C `do_nothing_control` names **four** junk
   landings; the draft requires **five** slugs. Freeze them to one number.
3. **(c)** — a digest of a sentence is not a check of the code. Keep it only if the leg's implementation is
   also re-derived (a reviewer reads the leg and the sentence; the draft's own Limits). As filed, LEGTEXT
   passes a counter whose ENTRIES implementation does a tenth of what its sentence promises (§2.1), and it
   forces a hard-coded table into the counter source. If kept, at least state that it compares copies, not
   semantics, and never let it support a `PASS` on its own.
4. **CONFIG vs `tools/check-receipt-seq.py`** (§2.3): do not re-implement the header leg. Require the
   receipt-seq tool's verdict in the same check (`python3 -B tools/check-receipt-seq.py --root <lane>
   <receipt> <counter>`), so one authority owns the grammar.
5. **Binds-from wording.** QUALITY 23 already requires the counter run at the freeze and a red-before per fix;
   QUALITY 17/19 already own the stamp. Q25's *new* content is exactly (i) the freeze blob is load-bearing and
   (ii) the controls are executions. Keep those two, cite 17/19/23 for the rest, and the criterion stops
   duplicating authorities that can disagree.

With (1)+(2) applied, the fixture's tree/decoy/partial counters are red and the honest one green (measured
above), the hand-typed receipts are red, and the round-73 red-before still works (round 73's receipt prints
`# config source: lane worktree: …`, and its counter prints no `# config sha256:`, so it is red on the value
clause as well).

---

## 5. Impacted axes

- **calibration (Ca):** the plan's record-repair content is untouched; the *discernment* half of the round's
  self-assessment is what Q25 would mis-state. Appending Q25 as drafted and marking the survivor class "fixed"
  is a premature saturation of a real, measured hole.
- **quality:** unchanged — no entry moves.
- **coverage (C):** indirectly. Claim C's `FROZENCFG` leg is the draft's clause (a) in one sentence
  ("read from claims.json AT the `<freeze>` commit (git show), never from the graded tree"), and claim C's
  counter is the artifact the whole criterion is about; if the leg's check is a text check, C's 12-legged PASS
  can be earned by a counter that grades its own graded tree — the P7b hole reopened under a new name.
- **QUALITY 9/11/17/19/23:** 11 is violated in the draft's own check (weaker stand-ins standing in for the
  mechanism); 23 is contradicted by the forbidden-literal leg (§2.3); 17/19 have a second, disagreeing authority
  (§2.3). 9 (two-way receipt↔declaration) is not touched by the draft at all, and the draft's check is one-way
  by construction: it validates the receipt's wording, never the counter's behaviour.

## 6. Fixture source (for reproduction) and honesty

The counter under test (`/tmp/CritQuality25/fx/lane/reports/round-74/accept-c.py`, = the freeze blob's copy) is
71 lines; the four modes differ only in which document feeds `claim["row_set"]`/`claim["entries"]`. The
`CFG=` switch is test scaffolding: the source bytes, the receipt format and the five junk receipts are
identical for all four modes, which is the point — the criterion's check cannot tell them apart.

Honest bounds, stated:

- Everything in §2 is a run on this fixture, on 2026-10-25; the numbers pasted are verbatim output, and the
  fixture is synthetic. What is **real** is the defect class and the surviving bytes it was built from
  (`MutPredicateC.md` F1/P7b, `.ufo/waves/round-73/w2/`; `controls-c.txt:13`; `accept-c.py:1646`).
- Not tested: a real round-74 counter (none exists; `.ufo/waves/round-74/counters/` absent), a freeze in a
  different lane, a counter whose freeze blob is unreadable, and a counter that hard-codes the freeze digest
  *and* grades the freeze blob (legitimate under the §3 wording — it is then frozen constants, and the
  divergence run cannot see it; [INFERENCE] from the code shape, not measured).
- Residual, stated: the §3 one-liner detects a class read from the tree only if the phantom edits that class;
  a reader that takes one uncovered class from the tree survives. It also scores a counter that *crashes* on the
  phantom (traceback instead of a `LEG FAIL` verdict) as FAIL, which is the right verdict for the wrong reason —
  the counter must answer, not raise. The only closure I can name is structural —
  the harness passes the config (`--config <file>`) and the counter has no other path to it — and I did not
  build that variant.
- No live fetches, no captures, no UA claim; nothing in this assignment needed the web.
- No tools installed (python3 3.14, git 2.56, POSIX sh sufficed); pacman untouched.
- Writes: this report; `/tmp/CritQuality25/{mk.py,check25.sh (copy),oneliner.sh,fx/…,texts/…,*.txt}`. No lane,
  fleet, `reports/round-74/claims.json`, `corpus/`, `tools/`, jj or git-index writes; the fixture repo is the
  only git state touched, and every call names `-C` it.
