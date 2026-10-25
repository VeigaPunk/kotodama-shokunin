# ExecJunkFixtures — junk-landing fixture generator (kotodama round 74, wave 1)

Seat: ExecJunkFixtures (leaf). Deliverable: `.ufo/waves/round-74/counters/junk-fixtures.py` plus this
report. Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`, round-73 counter bytes unchanged
(`accept-c.py` sha256 `95aee881…`, `accept-ca.py` sha256 `222d4dd6…`).

## Verdict up front

The generator is built, exercised and deterministic. **Five of the eight junk landings are accepted by
the round-73 counters**: J3 (config read from the graded tree), J4b (evasive constant printer), J5
(correction row naming only an id), J6 (in-place edit of an unguarded frozen receipt) and J7 (a Ca byte
citing claim-C ids incidentally). J1, J2 and J4 are rejected by the round-73 counters, so they are
controls that already work at round 73 and that the round-74 counters must keep rejecting.

| artifact | value |
|---|---|
| generator | `.ufo/waves/round-74/counters/junk-fixtures.py` |
| sha256 | `d4789c39740de5b6679e63f8fe0b2c54794f9eb358c8e8ab4660de622de9693f` |
| size / language | 774 lines, Python 3 stdlib only (no third-party import, no network) |
| interpreter / git | Python 3.14.8, git 2.56.0 |
| baseline replay tree | `9b10fa06a2d3756c8bacfc8fc7b2115921370d97` (= round-73 landed tree) |
| CLI | `--run-r73 [--only J1,J3] [--keep] [--workroot DIR]`, `--list` |
| exit | 0 when the harness baseline is green and every fixture graded; 2 on harness error |

## How a fixture is materialized (mktemp rule)

Each fixture is a private `git clone --no-checkout` of the lane under a fresh
`mktemp -d` (`tempfile.mkdtemp`), verified before the first commit:
`git -C <repo> rev-parse --show-toplevel` must equal the clone path, else the generator refuses to
commit. Every git call names `-C <repo>`; commits use the throwaway identity
`junk-fixtures <junk@fixture.invalid>` set per command inside the clone only. Nothing is committed,
checked out or referenced in the lane or fleet repositories.

The clone then replays the **real landed round-73 tree in the two-commit order the counters
themselves require**:

1. `A` — landed artefacts (`read-tree` of `0316b888…`) with `corpus/SOURCES.md` restored to its base
   bytes (the registry append is deferred);
2. `B` — the registry append, restoring the full landed tree (`tree == 9b10fa06…`, asserted);
3. `C` — the fixture's junk, one commit on top of `B`. `Fixture.rev` is `C`.

A one-commit fixture would fail claim C's SCRATCHMIRROR leg for the wrong reason (it reads
`git log -S S876 -- corpus/SOURCES.md` and `--diff-filter=A -- …/validate-receipt.txt` and requires the
receipt strictly before the append), so every leg the fixture does not name is exercised against real
landed bytes. `--run-r73` first grades the unjunked replay (P0) and the claim-C do-nothing control
(P0b) and refuses to tabulate fixtures if either deviates.

## Red-before: `--run-r73` output (verbatim, final bytes)

```
# junk-landing fixtures — round-73 red-before
# lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin
# base: 8841ad3b896a0227674fa0725b818c999118046f  landed tree: 9b10fa06a2d3756c8bacfc8fc7b2115921370d97
# fleet-root: /home/vgpnk/Projects/shokunin
# counters: reports/round-73/accept-c.py ; reports/round-73/accept-ca.py

P0  baseline landing (no junk)          C: PASS legs=11/11 exit=0 | Ca: PASS legs=9/9 exit=0
P0b do-nothing control (C, --lands=base)   FAIL legs=1/11 exit=1 red=ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,SCRATCHMIRROR,COLLCHECK

| fixture | claim | junk paths | expected (correct counter) | round-73 counter | accepted? |
|---|---|---|---|---|---|
| J1 | C | corpus/SOURCES.md, corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md, corpus/knowledge/linguistics/conlang-scholarship.md, reports/round-73/claims.json | FAIL: two header-only stub entries stand in for the mined prose (body word floor) though their header is complete | FAIL legs=10/11 exit=1 red=ENTRIES | no |
| J2 | C | corpus/lessons/round-73.md | FAIL: every Gate admit quote is absent from its evidence window (the quote/URL mispairing class) | FAIL legs=10/11 exit=1 red=EVIDENCE | no |
| J3 | C | corpus/SOURCES.md, reports/round-73/claims.json | FAIL: claims.json inside the graded tree shrinks the claim to two rows and one entry; the contract must come from the frozen commit | PASS legs=11/11 exit=0 | YES (survivor) |
| J4 | Ca | reports/round-73/ledger.json | FAIL: every observe_cmd constant-prints expected_after (literal python3 -c print / echo) instead of reading clone bytes | FAIL legs=4/9 exit=1 red=LEDGER,BASEMISMATCH,REPAIR,ANNOTATE,NOSTUB | no |
| J4b | Ca | reports/round-73/ledger.json | FAIL: evasive constant printer (import os;print(str(...))) passes the argv guard but reads no clone byte | PASS legs=9/9 exit=0 | YES (survivor) |
| J5 | Ca | SCORECARD.md | FAIL: a correction row names only its id; ANNOTATE/NOSTUB must require id + stated token + observed token + re-derivation | PASS legs=9/9 exit=0 | YES (survivor) |
| J6 | Ca | reports/round-72/telemetry/measures-ca.txt | FAIL: a frozen receipt outside both protected sets is edited in place (ACCEPT-CA-72 FAIL->PASS) | PASS legs=9/9 exit=0 | YES (survivor) |
| J7 | Ca | SCORECARD.md | FAIL: a Ca correction-section note cites claim-C rows S876..S880 incidentally; SEPARABLE must scan the whole Ca byte set | PASS legs=9/9 exit=0 | YES (survivor) |

# fixture repositories were removed after grading (re-run with --keep to retain them)
...
SURVIVORS (round-73 counter accepted the junk landing): J3 J4b J5 J6 J7
```

(The `# J<n> repo=… lands=…` / `# J<n> cmd: …` lines the tool prints after the table are omitted here
only for width; `--keep` retains each repo and the full invocation. Full log:
`/tmp/ExecJunkFixtures/red-before.log`.)

Harness fidelity: P0 `PASS 11/11` / `PASS 9/9` reproduces both filed round-73 receipts, and P0b
`FAIL legs=1/11` (only CENSUS green) reproduces `reports/round-73/telemetry/controls-c.txt`.

## Survivors — what each accepted junk landing falsifies

### J3 — the counter reads its acceptance contract from the graded tree (claim C)

Junk (`corpus/SOURCES.md`, `reports/round-73/claims.json`): the land's `claims.json` is rewritten so
claim C's `row_set` is `S876, S877` and `entries` names only the base entry, and the registry drops
`S878..S880` to match. The counter's own receipt at that lands reads:

```
# config source: lands tree: row_set, entries, rejects.refused_staged, rejects.refused_files, rejects.families, rejects.forbidden_ids, ground.fragments
# adopted rows: S876 S877
# entries: corpus/knowledge/linguistics/conlang-scholarship.md
ACCEPT-C-73: PASS legs=11/11     exit=0
```

`claims.json` is not pinned to a digest or blob: a landing shrinks the set it is graded against and
passes. This is the same class as the round-73 wave-2 P7b survivor; the round-74 counter must load its
constants from the frozen commit (`--freeze`) and reject a graded-tree config edit. The landed tree's
diff explains the shape: `corpus/SOURCES.md -3`, `reports/round-73/claims.json` narrowed.

### J4b — the evasive constant printer (claim Ca)

Junk (`reports/round-73/ledger.json`): every pair's `observe_cmd` becomes
`["python3","-c","import os;assert os.sep;print(str(\"<expected_after>\"))"]`. The argv guard passes
(there is no literal `print("…")` and `os.` is present), nothing is read from the clone, and the
counter prints:

```
PAIR L01 disposition=ANNOTATE stated_at=corpus/README.md:732 stated='243' observed_base='245' observed_lands='245' expected_after='245'
PAIR L04 disposition=REPAIR stated_at=SHONEN.md:6 stated='468' observed_base='505' observed_lands='505' expected_after='505'
LEG PASS LEDGER / BASEMISMATCH / REPAIR …
ACCEPT-CA-73: PASS legs=9/9
```

The base observation equals the truth constant, so BASEMISMATCH is satisfied by construction. This
reproduces the round-73 `M1b`/`M9` survivor with all eight pairs. A correct counter must bind the
observation to clone bytes (canary re-run in a clone with the watched file changed, or an argv target
that must resolve at the pinned base).

### J5 — a correction row naming only its id (claim Ca)

Junk (`SCORECARD.md`): the L01 correction row is replaced by `| L01 |` — line 1415 of the junk
landing's `SCORECARD.md`, nothing else in the row. The counter prints `LEG PASS ANNOTATE`,
`LEG PASS NOSTUB`, `ACCEPT-CA-73: PASS legs=9/9`: the L03 row ("same 243 → 245 drift as L01 …") names
L01 in prose and carries both tokens plus a re-derivation whose first clause is L01's own command, so
the gutted row is still evidenced. Root cause is the round-73 `M01`/`M02`/`M03` survivor class:
pair↔row matching is substring-anywhere over the section, not id-cell anchored and not column-aware.
A correct counter must anchor the id to the row's id cell and require the row's own token cells.

### J6 — an in-place edit of a frozen receipt outside both protected sets (claim Ca)

Junk (`reports/round-72/telemetry/measures-ca.txt`): `ACCEPT-CA-72: FAIL` → `ACCEPT-CA-72: PASS` in
the landed round-72 receipt (line 29 of that file at the junk lands). The counter prints
`PAIR L06 … stated='PASS' observed_base='FAIL' observed_lands='PASS'`, then `LEG PASS ANNOTATE`,
`LEG PASS APPENDONLY`, `LEG PASS SEPARABLE`, `ACCEPT-CA-73: PASS legs=9/9`.

Two Ca consequences are now false and unguarded: the filed `SCORECARD.md:1401` statement becomes
"true" by editing its evidence, and the committed L06 correction row (`SCORECARD.md:1418`) still
asserts the *committed* receipt reads `FAIL` while the bytes at lands read `PASS`. `APPENDONLY` covers
only `LOG.md`, `SCORECARD.md`, the round-71/72 lessons and `INPLACE_PATHS`; the round-72 telemetry
directory is in neither set, and `SEPARABLE` scans only Ca telemetry basenames containing "ca" for
S-ids. This reproduces the round-73 `M10` survivor. A correct counter must place every frozen receipt
under the append-only/zero-removal rule and must not let the truth side be an author-editable file
outside it.

### J7 — SEPARABLE is narrower than its own frozen wording (claim Ca)

Junk (`SCORECARD.md`): one note is appended to the end of `## Corrections — round 73` (line 1424):

```
- Round-73 close note: the conlang rows S876..S880 are claim C's registry rows; no calibration pair reads them.
```

This row is a byte the Ca legs read (ANNOTATE/NOSTUB iterate the section's rows), and it cites lane
ids ≥ 876, which the claim's SEPARABLE leg text forbids ("no byte the Ca legs READ … cites a lane S-id
≥ 876"). The implementation filters the section to rows that *name a ledger pair id* before scanning,
so the note is never read by the scan: `LEG PASS SEPARABLE`, `ACCEPT-CA-73: PASS legs=9/9`. A correct
counter must scan the whole corrections section (and any other Ca byte it reads), not only rows that
happen to name a pair.

## Caught controls (J1, J2, J4) — round 73 already rejects them

- **J1** (two header-only stubs, `row_set` narrowed to the four materialized rows so that the stub —
  not the row count — is the defect): `ENTRIES` fails on the body word floor (0 < 478 = the smallest
  knowledge entry at base); everything else, including ROWS/REPOINTED/GATE/EVIDENCE with used-by
  pointing at the stubs, is green. `PASS` at ENTRIES is impossible, which is why the round-73 counter
  catches it while its 561-word-filler variant (P1) survived.
- **J2** (every Gate admit row's quoted span replaced by one phrase no evidence window carries):
  `GATE` stays green (`EVIDENCE` is the only red leg: "S876…S880 Gate row does not carry the evidence
  quote"). The three-file quote triangle is cross-checked, so this mispairing class dies here.
- **J4** (literal `python3 -c print("…")` / `echo` constant printers): `LEDGER` fails with
  "python3 -c code must read the clone" and "argv[0] 'echo' not in the observe allowlist", cascading to
  BASEMISMATCH/REPAIR/ANNOTATE/NOSTUB (observed token unobservable) — `FAIL legs=4/9`. This is why the
  evasive form exists as the separate companion J4b.

## Library API (for the round-74 counters' selftests)

The file name contains a hyphen, so import by path (documented in the module docstring):

```python
import importlib.util, os
spec = importlib.util.spec_from_file_location(
    "junk_fixtures", os.path.join(HERE, "junk-fixtures.py"))
jf = importlib.util.module_from_spec(spec); spec.loader.exec_module(jf)
fx = jf.build("J3")                      # -> Fixture(name, claim, repo, rev, expected, paths)
try:
    res = jf.run_counter(fx.repo, jf.C_COUNTER, fx.rev)
    assert res["verdict"] == "FAIL", res       # what a correct counter must return
finally:
    jf.cleanup(fx)                        # removes the mktemp dir; API leaves no temp root behind
```

`build()` is verified working from a foreign cwd; `cleanup()` removes the whole fixture directory.
Because a round-74 landing has its own base/lands/config layout, the module also exposes the
building blocks a round-74 selftest can compose instead of the fixed round-73 trees:
`clone_lane`, `landing_replay(repo, base, lands, defer_path)`, `commit_all`, `run_counter`, and the
pure transforms `drop_rows`, `row_ids`, `rewrite_cell`, `truncate_to_header`, `replace_gate_quotes`,
`shrink_claims`, `rewrite_ledger_observe(doc, "literal"|"evasive")`, `stub_correction_row`,
`insert_note`, `replace_text`. Each `Fixture.expected` is the one-line expected verdict of a correct
counter (always `FAIL:`), so a selftest can assert on it directly.

## What I did NOT check / residual risks

- **Source truth is out of scope**: fixtures are byte-level; no page was fetched, no quote was
  re-verified against a live page. J2 is judged by the counter's own cross-file rule, not by the web.
- **Not hermetic in one inherited respect**: the landed `.ufo/waves/round-73/assimilation/guard-proof/`
  trees contain symlinks (`mirror/SKILL.md`, `mirror-a3/SKILL.md`) whose target is the live lane
  workspace path; `COLLCHECK`'s recursive read follows them (the round-73 wave-2 observation). The
  replay reproduces those bytes and the same reads; I did not change them. Every fixture still graded
  identically to its non-symlink legs, but a fully hermetic replay would have to rewrite those targets.
- **Only the claim-matched counter was run per fixture** (C for J1–J3, Ca for J4–J7). Running the other
  counter at the same lands would report on a surface the fixture does not attack.
- **Fleet state dependency**: claim Ca's APPENDONLY leg hashes the fleet round-72 report at the ledger's
  fleet pin (`80d8c9b5…`) against fleet HEAD; it was green in every run here. If the fleet repository
  moves that file, Ca fixtures would redden on an environmental leg unrelated to the junk.
- No counter was run in selftest mode by this seat; the round-73 counters' own fixture suites are
  outside the item.

## Tooling and bounds

- No tool installed or upgraded (python3/git already present); pacman never run; no downloads; no
  network fetches; no background jobs; no subagent/task spawns; no peer messaging.
- Writes: `.ufo/waves/round-74/counters/junk-fixtures.py`, this report, and `/tmp/ExecJunkFixtures/`
  (scratch logs; run logs at `/tmp/ExecJunkFixtures/red-before.log` and `run-r73.log`) plus mktemp
  fixture repositories created and removed by the tool. `/home/vgpnk/Projects/shokunin/**` other than
  the two lane files above was not written; shokuknow was not touched.
- Lane state after the work: `git -C <lane> rev-parse HEAD` = `f7104cb…` (unchanged);
  `git status --porcelain` shows only the inherited six round-73 w2 changes plus the untracked
  `.ufo/waves/round-74/` and `reports/round-74/` directories. No tracked byte of the lane, no index
  entry and no jj/git ref was modified by this seat.
- Blockers: none. Everything exercised is reported above; nothing in this report is inferred from a
  run I did not perform.
