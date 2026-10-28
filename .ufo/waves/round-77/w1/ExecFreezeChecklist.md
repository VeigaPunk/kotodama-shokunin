# ExecFreezeChecklist — round 77 (hyaku run 10), wave 1 BUILD

Seat: `ExecFreezeChecklist` (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
base `211f9526800906e0c585d878d265c37e5e090c15`. Assignment: the round-77 freeze
manifest — the file list the freeze commit must carry, with sha256 placeholders, plus the
LEGCOUNT rule binding the frozen `claims.json` `legs[]` lists to the counters' own leg tables.

**Verdict: delivered.** The manifest, its gate, its LEGCOUNT check, the checklist and a
22-expectation controls receipt are under
`.ufo/waves/round-77/w1/stage/ExecFreezeChecklist/`. At build the gate reports
`MANIFEST r77: PENDING files=0/18 pinned=0 missing=17 unpinned=1 mismatched=0 legs=0/2`
(exit 3) — correct, because 17 of the 18 core files are freeze-installed inputs that do not
exist yet. No round-77 leg, digest or census number is claimed as measured.

## 1. Files written

| path (relative to the lane) | sha256 | what |
|---|---|---|
| `.ufo/…/ExecFreezeChecklist/manifest.json` | `23aa04ad130a078c9b37c4857c73696a1bfc3d5919c76cc2ba0eae2bd7aae29c` | 18 gated files with `<sha256-at-freeze>` placeholders, consumers, producers; the LEGCOUNT rule + 4 emitted one-liners + 2 script forms; 6 advisory (non-gated) provenance paths; 4 recorded base measurements; the 4 freeze blockers |
| `.ufo/…/ExecFreezeChecklist/manifest-check.py` | `aa96c58e241fc3ec9fdb803dbf5699d640d6ab9c138d0c9701c28765d4040aa9` | the gate: `--record` (pin worktree digests) / `--freeze <sha>` (re-read committed blobs), schema guards, delegates LEGCOUNT |
| `.ufo/…/ExecFreezeChecklist/legcount.py` | `474bb063a6c79c21b764244e44153085ad1edf3d691866ed8b32ddaa092906b6` | LEGCOUNT check: `ast`-parses the counter's leg-table literal, compares with the frozen `legs[]` (order and multiplicity included) |
| `.ufo/…/ExecFreezeChecklist/controls.sh` | `473648d524863adfb1f09583bb7faf51a9a238b7067d62ec46e0dbe062fd8360` | rebuilds every control in its own scratch dir, removes it on exit, honours `HYAKU_SCRATCH`/`--scratch` |
| `.ufo/…/ExecFreezeChecklist/controls-receipt.txt` | `6daf82e70b9d9331d49b72917f42a40248b8f965aa900fc8e3345d42cd5bd57c` | the measured receipt: 22 expectations, all met; prints the sha256 of the three scripts |
| `.ufo/…/ExecFreezeChecklist/build-state-receipt.txt` | `ce4538b15869c3b27198298762bdab7e5286bb541c7dcba907d8f4dd4a245ba3` | `manifest-check.py --root .` today (PENDING, exit 3) |
| `.ufo/…/ExecFreezeChecklist/CHECKLIST.md` | `590b7d06d0ed4efd2640505af95722f506ef518d979e665550f510a895ea598a` | the ordered freeze checklist (install → LEGCOUNT → record → commit → `--freeze`) |
| `.ufo/waves/round-77/w1/drafts/reports/round-77/telemetry/census-start-counts.txt` | (draft, unpinned) | `census-start-counts.txt` measured at the base, so the manifest's entry 15 is not a placeholder |
| `.ufo/waves/round-77/w1/ExecFreezeChecklist.md` | (this report) | — |

`sha256sum .ufo/waves/round-77/w1/stage/ExecFreezeChecklist/*` produced those digests
(manifest.json re-hashed after the last edit). Nothing outside the two wave-1 write roots
(`.ufo/waves/round-77/w1/stage/ExecFreezeChecklist/`, `.ufo/waves/round-77/w1/drafts/`) and
this report was written; no tool was installed; the scratch dir was removed:

```
$ rm -rf -- /fast/scratch/hyaku/kotodama-r77/ExecFreezeChecklist && ls /fast/scratch/hyaku/kotodama-r77/
ExecAdaptC
ExecAdaptCa
ExecAdaptCapture
ExecAdaptJunk
ExecTmpAudit
L1
RevQualityFit-2
RevSeparability
ScoutDocS897
ScoutLedgerA
ScoutLedgerB
ScoutLedgerC
ScribeEntryA
ScribeMistakes
ScribeQuality30
SentinelSources
tmp.dABqfvlIm7
$ test ! -e /fast/scratch/hyaku/kotodama-r77/ExecFreezeChecklist && echo removed
removed
```

(sibling seats' scratch dirs untouched; `/fast/scratch/hyaku/kotodama-r77` itself kept).

## 2. What the manifest gates, and why those files

18 paths, exactly the seat-spec core. Each entry carries `consumers` and `why`, so the L1 can
see which claim leg loses its measurement when a file is missing. The mapping is grounded in
the round-76 counters and claims, not guessed:

- `claims.json` → both counters read predicates, `row_set`, base and `legs[]` from the
  `<freeze>` blob (round-76 `accept-c.py` FROZENCFG; `accept-ca.py` `load_frozen`).
- `ledger.json` → `accept-ca.py` only.
- `accept-c.py` / `accept-ca.py` → their own `LEGS` / `REQUIRED_LEGS` tables are the LEGCOUNT
  authority.
- `counters/capture-evidence.py` → named by round-76 `accept-c.py` (EVIDENCE driver).
- `counters/junk-fixtures.py` → named by round-76 `accept-c.py`; produces `junk-c`/`junk-ca`.
- `fixtures/r1exempt-{green,mixed,red}.json` → the Ca R1EXEMPT/SEPARABLE/APPENDONLY fixtures
  (round-76 contents read: green = `used-by` edit `expect green`, mixed = `teaches`+`used-by`
  `expect red`, red = `teaches` `expect red`); the draft requires them committed with the
  freeze.
- the 9 telemetry receipts → the draft's `green/red fixtures committed with the freeze`,
  the Ca RECEIPTS routing fix (round 76 shipped receipts only in the worktree), and claim C's
  GROUND/COUNTS/CENSUS start side.

Digest rule recorded and implemented: **sha256 of the committed blob**
(`git show <freeze>:<path> | sha256sum`), the same discipline round-76's FROZENCFG applies to
its by-document map. `--record` pins from the worktree; `--freeze` re-reads the commit. The
divergence is a named verdict (`MISMATCH`), not a silent pass.

## 3. LEGCOUNT — the rule, the checks, the proof

Rule: the `legs[]` frozen in `reports/round-77/claims.json` must equal the counter's own leg
table — same names, same order, duplicates included. Both round-76 counters refuse `exit 2`
with `FAIL legs=0/N` on a mismatch, so a divergence means the claim never runs.

Why the gate exists — the round-76 freeze was actually blocked by this, caught only at
freeze-control time:

```
$ grep -m1 'REFUSED: LEGCOUNT' .ufo/waves/round-76/w1/stage/L1/freeze-control-legcount-redbefore.txt
REFUSED: LEGCOUNT: the frozen claims.json lists 13 legs (ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,INDEX,COLLCHECK,FROZENCFG,INDEX); this counter implements 13 (ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,SCRATCHMIRROR,COLLCHECK,FROZENCFG,INDEX)
```

Emitted checks (both in `manifest.json` `legcount.checks`, quoted in CHECKLIST Step 2), in the
requested `python3 -c "… assert sorted(F)==sorted(LEGS)"` style, with `LEGS` **derived from the
counter source by `ast`** instead of typed. Claim C:

```
python3 -c "import ast,json;t=ast.parse(open('reports/round-77/accept-c.py').read());g=[n.value for n in t.body if isinstance(n,ast.Assign) and any(getattr(x,'id','')=='LEGS' for x in n.targets)][0];LEGS=[e.elts[0].value for e in g.elts];c=json.load(open('reports/round-77/claims.json'));F=[l.split(':',1)[0].strip() for l in c['claims'][0]['legs']];assert sorted(F)==sorted(LEGS),(F,LEGS)"
```

Claim Ca is the same with `REQUIRED_LEGS` / `e.value` / `claims[1]`. Each also ships an
order-included variant (`assert F==LEGS`) because round-76's C table legitimately repeats
`INDEX`, so a set-only test cannot see a slot swap; and the script form
`legcount.py --claim C|Ca [--rev <freeze>]`.

Proof the emitted strings execute (not dead text) — the same argv shape against the round-76
pair, receipt Section B:

```
$ python3 -c "…sorted(F)==sorted(LEGS)…"   # claim C
$ python3 -c "…F==LEGS…"                    # claim C, order included
$ python3 -c "…sorted(F)==sorted(LEGS)…"   # claim Ca
$ python3 -c "…F==LEGS…"                    # claim Ca, order included
EXPECT B-C-set    0 (got 0)
EXPECT B-C-order  0 (got 0)
EXPECT B-Ca-set   0 (got 0)
EXPECT B-Ca-order 0 (got 0)
```

Script form, positive control on the real round-76 pair (duplicate `INDEX` handled):

```
$ python3 -B …/legcount.py --claim C --claims reports/round-76/claims.json --counter reports/round-76/accept-c.py
LEGCOUNT C: frozen (13): ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,INDEX,COLLCHECK,FROZENCFG,INDEX
LEGCOUNT C: counter (13): ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,INDEX,COLLCHECK,FROZENCFG,INDEX
LEGCOUNT C: NOTE frozen lists 'INDEX' more than once (the counter's order decides the position)
LEGCOUNT C: PASS (order and set equal)
exit=0
```

Negative controls (Section A3, mutated copies under the scratch root; receipt lines verbatim):

```
EXPECT n1-renamed 1 (got 1)      # SCRATCHMIRROR at slot 9 — the round-76 refusal, reproduced
EXPECT n2-reordered 1 (got 1)    # set equal, order differs → DIVERGES at index 0 (set equal)
EXPECT n3-short   1 (got 1)      # one leg missing
EXPECT n4-duplicated 1 (got 1)   # extra leg appended
EXPECT n5-placeholder 1 (got 1)  # LEDGELIST? → "not UPPER_SNAKE — an unresolved placeholder cannot be frozen"
EXPECT n6         2 (got 2)      # LEGS = tuple(NAMES): not a literal → ERROR, exit 2
EXPECT n7         2 (got 2)      # unparsable counter → ERROR, exit 2
```

`--print counter` regenerates the frozen order from the counter alone and works before
`claims.json` exists:

```
$ legcount.py --claim C --counter reports/round-76/accept-c.py --claims /nonexistent.json --print counter
ENTRIES ROWS REPOINTED GATE EVIDENCE REJECTS GROUND CITEDLINES CENSUS INDEX COLLCHECK FROZENCFG INDEX
exit=0
```

Every legname also passes an `UPPER_SNAKE` guard, so a frozen list cannot carry a typed
placeholder (`?`, spaces, lowercase).

## 4. Base measurements recorded (not claims of round-77 data)

```
$ git -C . show 211f952…:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
820
$ git -C . ls-tree -r --name-only 211f952… -- corpus/knowledge | grep -c '\.md$'
253
$ git -C . show 211f952…:corpus/SOURCES.md | awk -F'|' '… tier/status …' | sort | uniq -c
    725 status=mined
     58 status=queued
     37 status=rejected
    493 tier=A
    311 tier=B
     16 tier=C
```

These match the draft's `253 -> 254` knowledge files and `820 -> 822` rows, so the manifest's
`census-start-counts.txt` entry was drafted from them at
`.ufo/waves/round-77/w1/drafts/reports/round-77/telemetry/census-start-counts.txt` (receipt
shape copied from `reports/round-76/telemetry/census-start-counts.txt`; `reports/round-77/`
is L1 territory, so it is a draft, not an install).

`reports/round-77/telemetry/census-start.txt` is already present (3769 bytes, last line
`kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`); the manifest
leaves it **unpinned on purpose** — pin at the freeze, so a legitimate census re-run does not
read as digest drift.

## 5. Build-state verdict (the honest non-pass)

```
$ python3 -B .ufo/waves/round-77/w1/stage/ExecFreezeChecklist/manifest-check.py --root .
MANIFEST-FILE MISSING   reports/round-77/claims.json absent in the worktree
… (16 more MISSING: ledger, both counters, counters/*, 3 fixtures, 8 telemetry)
MANIFEST-FILE UNPINNED  reports/round-77/telemetry/census-start.txt placeholder <sha256-at-freeze>
MANIFEST-LEGCOUNT C PENDING
  | LEGCOUNT C: PENDING — absent: reports/round-77/accept-c.py, reports/round-77/claims.json
MANIFEST-LEGCOUNT Ca PENDING
MANIFEST r77: PENDING files=0/18 pinned=0 missing=17 unpinned=1 mismatched=0 legs=0/2
exit=3
```

## 6. End-to-end gate controls (fixture repo, scratch, fixture-local identity)

Receipt Section C — the freeze path proven both ways on a throwaway repo whose toplevel was
asserted equal to the fixture dir before the first commit:

```
EXPECT C1-record  0 (got 0)            # 18 digests pinned from the worktree
EXPECT C2-freeze-pass 0 (got 0)        # MANIFEST r77: PASS files=18/18 … legs=2/2
EXPECT C3-blob-authority 0 (got 0)     # worktree tampered, NOT committed → still PASS (--freeze reads blobs)
EXPECT C4-committed-tamper 1 (got 1)   # MISMATCH files=17/18 mismatched=1
EXPECT C5-revert-pass 0 (got 0)        # revert committed → PASS, no re-record needed
EXPECT C6-committed-drop 1 (got 1)     # MISSING files=16/18 pinned=17 missing=1
EXPECT C7-leg-drift 1 (got 1)          # BETA→GAMMA re-spelled, digests re-pinned → only LEGCOUNT red (legs=1/2)
EXPECT C8-legcount-direct 1 (got 1)    # legcount.py --claim C --rev HEAD names the divergence
CONTROLS: all expectations met
```

Schema guards (unsafe/duplicate paths, wrong round) also fail closed:

```
$ manifest-check.py --root . --manifest <bad copy>
MANIFEST-PROBLEM manifest round is 76, not 77
MANIFEST-PROBLEM files[18] path '../escape.txt' is not a safe repo-relative path
MANIFEST-PROBLEM files[19] path '/abs.txt' is not a safe repo-relative path
MANIFEST-PROBLEM files[20] repeats path reports/round-77/claims.json (also files[0])
MANIFEST r77: FAIL files=0/21 … legs=0/2
exit=1
```

## 7. Freeze blockers the L1 must clear (also `manifest.json` `freeze_blockers[]`)

- **FMB-1** — `CLAIMS-DRAFT.md` line 62 has `LEDGELIST?` in claim C's list and line 106 has
  `LEDGELIST` in claim Ca's. `LEDGELIST?` cannot be frozen (the guard refuses it) and neither
  name exists in any counter table yet.
- **FMB-2** — the draft's leg lists are designs, not the counters' tables. Round 76's design vs
  implementation diverged at one slot and the freeze refused `legs=0/13`. After installing both
  counters: `legcount.py --claim C|Ca --print counter`, write the prose in that order, then
  re-check at the freeze commit with `--rev <freeze>`.
- **FMB-3** — `census-start-counts.txt` is absent from the worktree; the draft at
  `.ufo/waves/round-77/w1/drafts/…` is measured and ready to install.
- **FMB-4** — 17/18 core files absent; the freeze is only complete when
  `manifest-check.py --root . --freeze <freeze>` prints `PASS files=18/18 … legs=2/2`.

## 8. Risks and unrun checks

- **Unrun (cannot run yet):** every round-77 leg, digest, census and ledger count. The counters,
  `claims.json` and `ledger.json` do not exist; the gate says PENDING, never PASS.
- **Unverified for round 77:** the selftest/controls CLI shapes
  (`--selftest`, `--combined`, `--work`) are the round-76 counter flags, confirmed present in
  round-76 `accept-c.py` / `accept-ca.py`; the round-77 counters must confirm them with
  `--help` before those receipts are recorded. The manifest and CHECKLIST say so at the entry.
- **Deliberate non-pin:** `census-start.txt` and every other present-but-not-frozen receipt stay
  `<sha256-at-freeze>` until `--record`; pinning early would turn a legitimate re-run into a
  false drift blocker.
- **Overlap:** `census-start-counts.txt` (FMB-3) may also be produced by a census seat
  (`ExecCensusEnd-75` is live); only the draft is mine, and the L1 owns the install.
- **No installs** (no pacman, no uv/npx/official binary) were needed; no model or route was
  passed; the fleet repo, sibling lanes, `reports/round-76/**`, `.ufo/state`, `LOG.md`,
  `SCORECARD.md`, `corpus/**` and every git/jj state were left untouched (read-only `git show`
  / `git -C <fixture>` only).
