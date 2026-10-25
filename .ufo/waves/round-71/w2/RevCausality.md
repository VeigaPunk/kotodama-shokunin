# RevCausality — round-71 claim-C dependency & do-nothing-control falsify seat (wave 2)

- Seat: `L1Kotodama71.RevCausality` (leaf reviewer; lane read-only, this file the only lane write)
- Date: 2026-10-25 · anchor revision `64da9e14e5fa512c7f9c1d7695f48b6d34009b47` (HEAD moved
  `14c88d9` → `edd7895` → `64da9e1` during this seat; every measurement below is re-anchored at
  `64da9e1` from `git archive`, plus the frozen base `b94a543c70f40dba7e49fff96d05bfb8bbd8c678`)
- Counter measured: `reports/round-71/accept-c.py` sha256
  `80b4ca093a1d1c8436c7e5ff8a0fdb4be7f01a6517ac9dfec35cf05577650ed8`
- Scope: (a) does the C entry depend on **only** rows S861–S873 and the word-bounded sweep;
  (b) does any claim's after-state reach its target **without its own work** (do-nothing controls
  `controls-{c,ca,d}.txt` at base must fail).
- Method: re-extracted base `b94a543c`, lands `8c203bd`, and HEAD `64da9e1` with
  `git archive | tar -x` into `/tmp`; ran every declared command and every counter on those trees;
  mutated only `/tmp` copies (the lane worktree was never written).

## Verdict summary

| check | result | verdict |
|---|---|---|
| entry cites only rows S861–S873 | 13 distinct ids, set == {S861..S873}; no other S-id anywhere in the entry | **PASS** |
| those rows are new this round | `S861–S873` absent at base (0 rows), all `status=mined`, all `opened=2026-10-25`, all `used-by` name the entry | **PASS** |
| no other registry row depends on the entry | exactly 13 rows in the whole registry name the entry — the same 13 | **PASS** |
| registry delta == cited count | 784 (base) → 797 (HEAD) = +13 | **PASS** |
| word-bounded sweep at base prints nothing | filename `*danc*` 0; `\b(danc|choreograph|movement culture|performance)\b` topic 0 (rc=1); unbound variant matches `funerary-material-culture.md:4` "avoidance" | **PASS** |
| sweep at HEAD has exactly one owner, the entry | filename owner = entry; topic owner = `entry:20` only | **PASS** |
| `- gap filled:` names the word-bounded sweeps verbatim | both commands quoted verbatim, plus the unbound false-match note; one partial-owner count wrong (F9) | **PASS** |
| counts 35→36 / 242→243 by the declared `find` + `wc -l` | base 35/242, HEAD 36/243 | **PASS** |
| `tools/check-cited-lines.py` on the entry | exit 0, `0 finding(s)` | **PASS** |
| after-state reproduces at the receipt's stamped revision | `accept-c.py` PASS at materialized `8c203bd`; receipt self-sha `1df995…` == counter at `8c203bd` | **PASS** |
| do-nothing control C at base fails | 35 / 242 / 784 / entry absent / 0 / 0; counter exit 1 | **PASS** |
| do-nothing control Ca at base fails | six receipts 0 header lines each, `acc2d614` 0, quote 27 words, 0 trend rows, no lesson, no verdict table; counter 6×`LEG FAIL` | **PASS** |
| do-nothing control D at base fails | in-archive leg file-not-found rc=2; frozen `ACCEPT-D-69` 8/8 rc=0 | **PASS**, but leg 2 is vacuous (F4) |
| C counter enforces "≥12 **new** rows opened this round" | **no** — passes with zero new rows (F1) | **FAIL (instrument)** |
| C counter enforces the `- gap filled:` / topic-line clause | **no** — passes with both lines deleted (F2) | **FAIL (instrument)** |
| Ca's *declared* counting command reaches its verdict target | prints `0`, target 21 (F3) | **FAIL (declaration)** |
| D's *declared* counting command is base-parameterized | no — no-git leg copies the live lane; from base it emits the after-state line (F4) | **FAIL (declaration)** |
| entry↔row anchor agreement | S861: entry `paragraph 1` vs registry/Gate `paragraph 2` (F5) | **FAIL (one cell)** |

Answer to the seat question: **the landed C entry does depend only on S861–S873 and the
word-bounded sweep** — verified row-by-row and against base. **No landed after-state is reachable
without its own work.** The instruments are weaker than the claim: C's counter can report the
target with zero new rows and with the gap statement deleted (F1/F2), and two declared counting
commands are not tree-parameterized / field-correct (F3/F4).

## Cross-claim separability (does one claim's work reach another's target?)

- **C's work does not reach Ca's target.** At the C-lands commit `8c203bd` every Ca leg is still at
  its base value: six round-70 receipts `0` header lines each, `acc2d614` `0`, `round-71.md`
  absent, `quarantine-verdicts.md` absent, `accept-ca.py` absent. C's landing is 100 % on its own
  surface (entry + 13 rows + README + lesson + log), so Ca's target is unreachable without Ca's own
  repairs.
- **Ca's work does not reach C's target.** `1d1b432` (Ca records) touches `corpus/SOURCES.md` on
  exactly one line — the **S860** `verify-at` cell (V70-2) — and none of S861–S873, and it does not
  touch the entry: `git diff --stat 8c203bd 1d1b432 -- corpus/knowledge/culture-material/dance-performance-movement-codes.md corpus/SOURCES.md`
  → `corpus/SOURCES.md | 2 +-` only. C's target was already reached at `8c203bd` and cannot be
  reached by Ca's records.
- **D's work touches neither surface** (new counter + receipts only).

The one place a claim's after-state can be reported without its own work is inside the
**instruments**, not between claims: F1/F2 (C counter) and F4 (D's second leg). F3 is the same class
for Ca's declared command.

## Findings by severity

### F1 — HIGH (instrument): the C counter passes an entry that opens **zero** new rows

`reports/round-71/accept-c.py` leg `CITED`/`ROWS` accepts **any** mined row whose `used-by` names
the entry (`cells[8] == "mined"`, `ENTRY in cells[11]`). It never checks the id range (`>= S861`),
the `opened` date, or the registry delta, so the claim's own-work clause ("≥12 **new** SOURCES rows
opened this round", target "registry ≥ 784+12", kill rule "any row opened for the claim not opened
this round") is not machine-checked at all.

Reproduction (scratch copy of `64da9e1`, lane untouched): delete the 13 rows S861–S873 from
`corpus/SOURCES.md` (registry back to **784**), rewrite the entry's 13 `S86x` tokens to 13
pre-existing mined rows (`S001 S002 S003 S007 S008 S013 S016 S018 S031 S032 S033 S035 S036`) and
append the entry path to those rows' `used-by`:

```
LEG PASS ENTRY / COUNTS / CITED / ROWS / USEDBY-PATHS / CITED-LINES / SWEEP
ACCEPT-C-71: PASS            (EXIT=0, registry=784)
```

The same run with the 13 rows kept and the ids rewritten also passes (registry 797 unchanged). So
a fabricated dependency on old rows scores green: the counter cannot distinguish "13 rows opened
today" from "13 rows retro-fitted".

Smallest fix (owning lane): add `NEW_FLOOR = 861` and require every cited id `>= NEW_FLOOR` with
`cells[9] == "2026-10-25"`; add a `REGISTRY-DELTA` leg asserting
`registry_rows == 784 + len(cited)` (or `>= 796`); add a selftest fixture that cites `S001` and
must FAIL. Until then the newness fact rests on out-of-band inspection only (which this seat did:
see the PASS rows above).

### F2 — MEDIUM (instrument): the `SWEEP` leg is satisfied with **no** topic line and **no** `- gap filled:` line

`accept-c.py:118-125` computes `topic_owners` and accepts `len(topic_owners) <= 1` — **0 is
accepted** — and nothing in the counter reads the entry's `- gap filled:` line, although the
predicate requires "its `- gap filled:` line names the sweep that showed the gap".

Reproduction (scratch copy of `64da9e1`): delete the two lines `- gap filled: …` and `- topic: …`
from the entry:

```
LEG PASS SWEEP   topic-owners=[]
ACCEPT-C-71: PASS            (EXIT=0)
```

Consequence: the "0 word-bounded topic-line owners before this entry" half of the gap claim is not
tied to the entry that fills it; the entry could ship with no register claim and the counter would
still be green. Smallest fix: require `topic_owners == [ENTRY + ":" + <line of - topic:>]`
(i.e. exactly one owner, the entry) and add a `GAP-FILLED` leg grepping the `- gap filled:` line
for both sweep commands (filename sweep and the word-bounded topic sweep) plus the
`\b`-bounded form. The landed entry satisfies both (verified independently: `- gap filled:` at
line 19 quotes both commands verbatim and names the unbound `avoidance` false-match).

### F3 — MEDIUM (declaration): Ca's declared counting command's verdict leg prints `0` against a target of `21`

`reports/round-71/claims.json` claim `Ca.counting_command` ends with

```
awk -F'|' '$1 ~ /S[0-9]+/ && $2 ~ /^(PRESENT|REFUSED|UNVERIFIABLE)$/ {n++} END{print n+0}' reports/round-71/telemetry/quarantine-verdicts.md
```

The table rows are `| S776 | PRESENT | … |`, so with `-F'|'` `$1` is the empty leading field and
`$2` is the id — the condition never fires. Run verbatim at `64da9e1`:

```
$ for f in reports/round-70/telemetry/measures-{o,ca,d}.txt reports/round-70/telemetry/controls-{o,ca,d}.txt; do grep -cE '^# (counter sha256|stamped revision|evaluated revision|measured revision|tree|worktree dirty)' "$f" || echo MISSING:$f; done | sort | uniq -c
      6 6
$ grep -c 'acc2d614' corpus/SOURCES.md                       -> 1
$ awk -F'|' 'NR==13 {print $4}' corpus/lessons/round-70.md | wc -w  -> 25
$ grep -c 'round-70 trend-correction' SCORECARD.md           -> 1
$ grep -c 'rejected this round:' corpus/lessons/round-71.md  -> 1
$ awk … (verdict leg, above)                                 -> 0        # target 21
```

`accept-ca.py` itself parses correctly (`rows=21 unique-ids=21 labels-ok=True`, and after `75d1675`
it pins the exact 21-id slice), so the claim's substance holds; the **declared** command does not
reach its declared target and cannot be used by a controller. Fix: `$2`/`$3` offsets (or
`gsub` the cells), and record the corrected command in the round-71 report (the frozen predicate
and target need no change).

### F4 — MEDIUM (declaration): D's declared no-git leg is not tree-parameterized and emits the after-state when run from base

`claims.json` claim `D.counting_command` leg 2 hard-codes the live lane:

```
tar --exclude=.git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin -cf - . | tar -C $T -xf -; cd $T; python3 -B reports/round-71/accept-d.py --selftest
```

Executed **verbatim from the base tree** (cwd `/tmp/r71base`, `b94a543c`):

```
SELFTEST: COULD-NOT-EVALUATE (no git)
EXIT=2
```

i.e. the base control prints the after-state's no-git target, because the copy source is the live
lane, not the tree under test. The composite target is still not reached from base (leg 1 is
file-not-found rc=2, and the target needs `SELFTEST: 2/2` + exit 0), so the control is not
*passing* at base — but its second leg is vacuous and would stay vacuous in any future round.
`controls-d.txt` rev 3 already discloses this as **R71-M11** and routes a parameterized form
(`tar -C .` from the tree under test); the declared bytes in `claims.json` still carry the
hard-coded lane. Fix: make the copy source `.` (or `$PWD`) and regenerate `controls-d.txt` leg 2
from the base archive — where it must print the frozen counter's
`DO-NOTHING FIXTURE: PASS (unexpected) / SELFTEST: 1/2`, rc=1 (reproduced by this seat at base:
`reports/round-69/accept-d.py --selftest` in a `.git`-less base copy → exactly that, rc=1).

### F5 — MEDIUM (dependency): S861's anchor disagrees between the entry and the row it cites

- entry line 3: `- source: S861 — … — element record 00258, inscription narrative, paragraph 1 — fetched 2026-10-25`
- registry row S861 (`corpus/SOURCES.md`): `…, inscription narrative, paragraph 2`
- lesson Gate row: `element record 00258, inscription narrative ¶2; Wayback capture 20260925201518`

Commit `64da9e1` ("S861 anchor ¶2 fix") corrected the registry and the lesson but not the entry's
`- source:` line, so the file that carries the quote now points a reader at ¶1 while the row it
depends on (and the Gate that quotes it) says ¶2. Every other row's anchor is the same text modulo
abbreviation (`S868` drops the word "paragraph"; `S870`/`S871`/`S872`/`S873` abbreviate; no
contradiction). Fix: change the entry's S861 anchor to `paragraph 2` (one line) — or revert the
registry if ¶1 is the true location, but the Gate's re-located quote says ¶2.

### F6 — LOW: the C counter crashes instead of printing a red receipt on a base tree

`accept-c.py:72` does `open(ENTRY)` unconditionally, so on a tree without the entry the run dies:

```
LEG FAIL ENTRY
LEG FAIL COUNTS
Traceback (most recent call last): … FileNotFoundError: … dance-performance-movement-codes.md
EXIT=1
```

Legs 3–7 are never evaluated, so the base control cannot show *which* legs would fail, and the
docstring's contract ("1 any leg fails; 2 input error") is met only by accident of Python's exit
code. Guard leg 3 with `if not entry_exists: leg("CITED", False, "entry absent"); return 1` (or set
`text = ""`).

### F7 — LOW: two different count measures in one claim

`COUNTS` uses `os.listdir` per partition (top-level `*.md` only); the declared command uses
`find corpus/knowledge -type f -name '*.md'` (recursive). They agree today — `find
corpus/knowledge -mindepth 3 -type f -name '*.md' | wc -l` → `0` — but a nested `.md` would make the
counter and the receipt disagree. Use the `find` form (or `os.walk`) in the counter.

### F8 — INFORMATIONAL: receipt/evidence drift observed while HEAD advanced (all transient, all now clean)

- At `14c88d9` `reports/round-71/telemetry/measures-c.txt` was **untracked** (`git status` `??`,
  `git log --all -- <path>` empty) although the entry's `- source:`/`recheck:` lines call it
  "commit receipts". It is tracked at `64da9e1`; its `# counter sha256 (self)` `1df995…` matches the
  counter **at its stamped revision `8c203bd`**, not at HEAD (`80b4ca…`, docstring-only change in
  `edd7895`) — consistent with QUALITY 17/19 ("run at the revision you stamp"), verified by
  re-running the counter in a materialized `8c203bd` clone (PASS, all 7 legs).
- At `edd7895` the committed `census-end.txt` contained the 28-line `W04` block **twice**
  (`grep -c W04` → 56, unique ids 28); `75d1675` deduped it (now 30 lines, 28 `W04`, id set
  identical to `census-start.txt`). The receipt line "census exit=0 (W04=28 same as base)" is true
  only of the deduped file.
- `controls-c.txt` / `controls-ca.txt` are hand-shaped summaries, not the verbatim output of the
  declared counting commands (claims.json `controls.do_nothing` says the command is run and
  committed as the receipt). Their numbers agree with my base re-run leg for leg (C: 0/0/35/242/784/
  absent; Ca: 0×6, 0, 27, 0, absent, absent), so this is a form defect, not a numeric one.

### F9 — LOW (gap statement): the partial-owner inventory miscounts one token

The `- gap filled:` line says `dress-through-eras.md` carries "the single "choreograph" token".
That file has **three** occurrences of the bare token on one line
(`corpus/knowledge/culture-material/dress-through-eras.md:13`: "draped cultures choreograph
movement; tailored cultures choreograph posture; layered cultures choreograph *opacity*"):

```
$ grep -oiE '\bchoreograph\w*' corpus/knowledge/culture-material/dress-through-eras.md | sort | uniq -c
      3 choreograph
```

The other three partial owners check out (`masks-masquerade.md`: 5 "dance" + 3 "dancer" + 4
"dancers" + 4 "dances"; `gesture-co-speech-pointing.md`: 7 movement mentions;
`transport-mobility-lexicon.md:3`: "movement vocabulary"), and none of the four has a `- topic:`
line matching the word-bounded regex (rc=1), so the sweep result itself is unaffected. Fix: say
"three "choreograph" tokens on one line" (or drop the count).

## Verification gaps / residual risk

- **Quote-vs-claim grounding** (out of this seat's scope, flagged): the entry's S868 sentence
  ("arm positions diverge by school") and S864 sentence ("a full twenty hours without interruption")
  go beyond the ≤25-word Gate quotes recorded for those rows (S868's quote is only the
  feet-standard sentence; S864's is only the four-kilometre sentence). `check-gate-quotes.py` cannot
  catch this — per RevGate's F1 it does not parse table rows at all — so neither the counter nor the
  Gate proves the extra figures. Not a dependency defect (both rows are in S861–S873 and are the
  entry's own new rows); it is a grounding residual.
- **Newness is established out-of-band.** F1 means the counter alone cannot prove "opened this
  round"; this seat proved it from base (`git show b94a543c:corpus/SOURCES.md` has 0 rows in
  S861–S873, 1 row S860; the 13 rows carry `opened=2026-10-25`, `status=mined`; exactly 13 registry
  rows name the entry). Any future C round should not treat the counter as sufficient.
- **Live lane.** HEAD advanced three times during this seat and peers hold uncommitted edits
  (`accept-ca.py`, entry, `README.md`). All findings above are anchored to committed bytes at
  `64da9e1`; a re-run after further commits should re-check F3/F5 first (both are one-line fixes
  already in flight in the lane's own hardening commits).
- No tool installs or updates were made (pacman paused per the wave directive).
