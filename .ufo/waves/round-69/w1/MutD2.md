# Round-69 W1 / MutD2 — mutation test of `accept-d.py`'s SIGNATURES leg

Seat: leaf, depth axis. Question: can the error-signature linkage (decision-table
signature names must also appear under SKILL.md `## Error patterns`) be skipped?

All lane access was read-only; every mutation below lives in `/tmp/mutd2`. No
production file was edited; no git/jj state was touched (read-only
`rev-parse`/`status`/`log` only). No tool installs; no network.

## Environment facts (observed)

- Counter under test: `reports/round-69/accept-d.py`,
  sha256 `06b0352a0288be7a788bb65f243980c77e107e2e4795743b4c4e1a40cd490c10`.
- `git rev-parse HEAD` → `6a98d7d042b6c58d2165773b1585069798111035`
  ("round-69: declaration + three NEW counters …"); `git status --porcelain --
  reports/round-69/accept-d.py` → empty (worktree copy clean vs index). The
  goal text's base revision `793f797…` differs from the working-copy HEAD;
  recorded as observed, not resolved further (out of seat scope).
- Lane `SKILL.md`: has `## Error patterns` at line 468; 0 occurrences of any of
  the five signature names (data not landed yet, as stated in the round brief).
- `corpus/SOURCES.md`: no `S859` row yet.

## The mutation

One-line patch of the copy, anchor found exactly once
(`/tmp/mutd2/build.py`, asserts count==1):

```diff
-    res.add("SIGNATURES", not missing_sig,
-            "missing=%s" % (missing_sig or "none"))
+    res.add("SIGNATURES", True,
+            "MUTATED linkage-dropped would_be_missing=%s" % (missing_sig or "none"))
```

Mutant sha256 `23efe0c0b790aaff06f3e70fe61ee4a4359e4d9b0dfc827466d3b95866dd89cc`.

## Fixtures (all under /tmp/mutd2, built by `/tmp/mutd2/build.py`)

Shared tree: lane `SKILL.md` + `FIXTURE_TABLE` inserted immediately before
`## Error patterns` (no signature rows added to that section); `corpus/SOURCES.md`
= lane copy + appended fixture row `| S859 | … | mined | … | SKILL.md |`;
`tools/check-supersession-settlement.py` copied (EVIDENCE path target).

Proof the fixture is faithful to "signatures appear nowhere [in the linkage
target]": builder asserts each of the five names (`chain-left-pending`,
`entry-not-repointed`, `retired-row-mined`, `closed-chain-kept`,
`scope-limiter-missing`) occurs exactly once in the fixture SKILL.md — in the
table's Error-signature column, which `TABLE`/`STATES`/`FIELDS` require — and
zero times inside the `## Error patterns` section span. (If the names appeared
nowhere at all, `FIELDS` would fail on empty cells first, so table-only is the
exact isolating fixture for the SIGNATURES leg.)

- `fixture-a/` — committed counter copy = **mutant** bytes.
- `fixture-b/` — committed counter copy = **original** bytes.
- `fixture-c/` — committed counter copy = **original** bytes.

Note: the mutant must be executed as a file named `accept-d.py`
(`/tmp/mutd2/mutant/accept-d.py`) because `STAMP` resolves the committed copy
as `root/reports/round-69/<basename(__file__)>`; a foreign basename yields
`committed=none` and fails STAMP for the wrong reason.

## Runs (verbatim output)

### RUN A — mutant counter on fixture-a (linkage dropped, signatures nowhere in `## Error patterns`)

```
$ python3 /tmp/mutd2/mutant/accept-d.py --root /tmp/mutd2/fixture-a
LEG PASS STAMP self=23efe0c0b790 committed=23efe0c0b790
LEG PASS SECTION heading=### Registry correction chains
LEG PASS TABLE header=5 rows=5
LEG PASS STATES states=['pending', 'settled-active', 'settled-retired', 'settled-closed', 'settled-split']
LEG PASS FIELDS empty=none short=none
LEG PASS SIGNATURES MUTATED linkage-dropped would_be_missing=['chain-left-pending', 'entry-not-repointed', 'retired-row-mined', 'closed-chain-kept', 'scope-limiter-missing']
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', 'S859', 'S859', 'S859', 'S859']
ACCEPT-D-69: PASS legs=8/8
exit=0
```

### RUN B — unmodified lane counter on fixture-b (identical tree, original committed copy)

```
$ python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-69/accept-d.py --root /tmp/mutd2/fixture-b
LEG PASS STAMP self=06b0352a0288 committed=06b0352a0288
LEG PASS SECTION heading=### Registry correction chains
LEG PASS TABLE header=5 rows=5
LEG PASS STATES states=['pending', 'settled-active', 'settled-retired', 'settled-closed', 'settled-split']
LEG PASS FIELDS empty=none short=none
LEG FAIL SIGNATURES missing=['chain-left-pending', 'entry-not-repointed', 'retired-row-mined', 'closed-chain-kept', 'scope-limiter-missing']
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', 'S859', 'S859', 'S859', 'S859']
ACCEPT-D-69: FAIL legs=7/8
exit=1
```

### RUN C — mutant counter against fixture-c (intact committed counter copy)

```
$ python3 /tmp/mutd2/mutant/accept-d.py --root /tmp/mutd2/fixture-c
LEG FAIL STAMP self=23efe0c0b790 committed=06b0352a0288
LEG PASS SECTION heading=### Registry correction chains
LEG PASS TABLE header=5 rows=5
LEG PASS STATES states=['pending', 'settled-active', 'settled-retired', 'settled-closed', 'settled-split']
LEG PASS FIELDS empty=none short=none
LEG PASS SIGNATURES MUTATED linkage-dropped would_be_missing=['chain-left-pending', 'entry-not-repointed', 'retired-row-mined', 'closed-chain-kept', 'scope-limiter-missing']
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', 'S859', 'S859', 'S859', 'S859']
ACCEPT-D-69: FAIL legs=7/8
exit=1
```

### RUN D — unmodified counter, `--selftest` (as requested)

```
$ python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-69/accept-d.py --selftest
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8)
SELFTEST: 2/2
exit=0
```

### Context — unmodified counter on the real pre-data lane

```
$ python3 reports/round-69/accept-d.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin
LEG PASS STAMP self=06b0352a0288 committed=06b0352a0288
LEG FAIL SECTION heading=### Registry correction chains
LEG FAIL TABLE no decision table
LEG FAIL STATES no decision table
LEG FAIL FIELDS no decision table
LEG FAIL SIGNATURES no decision table
LEG FAIL EVIDENCE no decision table
LEG FAIL SOURCE no decision table
ACCEPT-D-69: FAIL legs=1/8
exit=1
```

(Expected pre-data state: only STAMP passes; every data leg rejects the absent table.)

## Findings

- VERDICT: PASS — the SIGNATURES linkage **is** skippable by counter mutation.
  SIGNATURES is the only leg that reads `## Error patterns`; no other leg
  (SECTION/TABLE/STATES/FIELDS/EVIDENCE/SOURCE) inspects that section, so
  dropping the one-line requirement lets a decision table whose five signature
  names appear nowhere under `## Error patterns` pass 8/8 (RUN A).
- VERDICT: FAIL (control, as required) — the unmodified counter kills the same
  tree at exactly SIGNATURES, listing all five names missing (RUN B). The leg is
  load-bearing and RUN A's pass is attributable to the mutation alone.
- VERDICT: PASS (tamper-evidence) — the skip is **not silent**. STAMP hashes the
  executed counter against the committed copy `reports/round-69/accept-d.py`;
  with the committed copy intact the mutant fails STAMP
  (`self=23efe0c0… committed=06b0352a…`, RUN C). That copy is committed at HEAD
  `6a98d7d…` and clean vs index, so skipping the linkage requires mutating a
  committed production byte — a working-copy change visible to `jj diff` /
  `git status`. Enforcement is tamper-evident, not tamper-proof: an actor who
  edits both runner and committed copy and records the change can pass, but that
  is an auditable production-file change outside this wave's worker write scope.
- Answer to the seat question: the error-signature linkage cannot be skipped
  against the frozen, committed counter; it can only be skipped by mutating the
  counter itself and replacing the committed counter copy, which is detectable
  as a production diff. Within a single counter invocation the linkage rests
  entirely on that one leg.
- Design notes (non-blocking, for the L1):
  - SIGNATURES matching is substring containment in the whole `## Error
    patterns` section: any occurrence of each name anywhere in the section
    satisfies the unmodified leg (e.g. one bullet listing the five names with no
    observation/reading structure). Weakest-possible enforcement form; only the
    name linkage is checked, not shape.
  - If the `## Error patterns` heading is absent entirely, `ep_text` is empty
    and the leg fails for any non-empty signature — correct direction.
  - STAMP anchors to `basename(__file__)`, not to a VCS digest: a counter run
    under any other name fails STAMP with `committed=none` (observed in my
    first mutant run). The real history anchor is the VCS itself; STAMP only
    binds executed file to tree copy. One-line L1 hardening option: have STAMP
    also compare against `git rev-parse HEAD:reports/round-69/accept-d.py`
    content (read-only), making even a working-copy counter swap fail.
  - Cosmetic: SOURCE prints the S-id once per row (`S859` ×5).

## Reproduction artifacts (scratch, /tmp/mutd2)

`build.py` (builder + assertions), `orig-accept-d.py` (byte-identical counter
copy), `mutant-accept-d.py` and `mutant/accept-d.py` (mutant),
`fixture-a|b|c/` (fixture trees). Re-run: `python3 /tmp/mutd2/build.py`, then
RUN A/B/C/D commands above.
