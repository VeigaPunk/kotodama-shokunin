- Seat: C07 | verifier | claim C | date 2026-10-19 | baseline da68a6d

# C07 — independent verification of the box-1 executable-surface survey

Scope (my mission): independently re-run the box-1 survey; verify 28/28 at
`SKILL.md` sha256 `f9bd07c2…`; verify C02's JSON rows against my own run
row-for-row. I verified nothing outside claim C.

**Result: 28/28 CONFIRMED independently, at `f9bd07c2…` (732 lines), on the
delivered baseline `da68a6d` with a clean tree for `SKILL.md` + `tools/`.**
Two mutually independent extraction methods agree row-for-row, the check is
demonstrated falsifiable (isolated negative control → 27/28, exit 1), and all
28 paths are HEAD-tracked, so resolution cannot be an artefact of untracked
local files.

## 1. Method A — the filed survey tool, re-run

```
$ python3 -B reports/round-30/craft/box1-survey.py ; echo EXIT=$?
{
 "date": "2026-10-18",
 "named": 28,
 "resolvable": 28,
 "unnamed_in_skill": [],
 "skill_sha256": "f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b"
}
EXIT=0
```

- Run twice; `diff run1.txt run2.txt` → **identical** (deterministic, no
  clock/UUID in output beyond the hardcoded date — see §6.1).
- `sha256sum SKILL.md` → `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`,
  which equals the tool's own `skill_sha256` field → the tool measured the
  live bytes at the claimed digest.
- `wc -l SKILL.md` → `732` (matches the claim's 715 → 732 movement).
- `git status --porcelain SKILL.md tools/` → empty; `git diff --stat HEAD -- SKILL.md tools/`
  → empty; `git rev-parse --short HEAD` → `da68a6d`. The measurement is on the
  filed revision, not a working-tree variant.

## 2. Method B — independent re-derivation through a different code path

The filed tool extracts names with `re.findall(r"tools/[\w./-]+\.py", skill)`
(`reports/round-30/craft/box1-survey.py:6`). I deliberately did **not** reuse
that mechanism:

- token-split scan (`re.split(r"[`\s()\[\]|,;:]+", skill)`, keep `tools/…*.py`
  tokens) + `pathlib.Path.is_file()` for resolution, plus a second bash pass
  using `grep -nEo` + `test -f` per row;
- result: **28 named / 28 resolvable / 0 unresolvable**, same first-occurrence
  line anchors as the filed tool (`filed-tool named set == my named set: True`);
- canonical row comparison (`LC_ALL=C sort` on both row files, then `diff`) →
  **empty**: row-for-row identical; sha256 of the canonical row file
  `b65f0a1e6a5c4fe19e8d8a5ee62024f6a98cc12d0b8e9a3b9a573a9ccbad99a9`
  (`py.canon` and `bash.canon` md5 both `c678f4f82fc880aa4a2cbd0a171a1437`);
- raw-occurrence count: 78 `tools/*.py` occurrences collapse to 28 unique
  paths (so the count is deduplicated, not a raw mention count).

A naive `diff` first showed one ordering difference in
`tools/assemble-d2*.py`: `sort` collation puts `-`/`.` differently from
Python's ASCII `sorted`. Set content is identical — recorded so a future seat
does not misread it as a mismatch.

## 3. Falsifiability controls (isolated copy, no repo writes)

Staging: `.scratch/c07/ctrl/tree/` = `SKILL.md` + the 28 executables + a copy of
`box1-survey.py` at `reports/round-30/craft/` so the tool's
`parents[3]` root resolves to the copy (`box1-survey.py:4`).

- **Parity control** (unmodified copy): `named 28, resolvable 28, unnamed []`,
  exit 0 — my staging is faithful, the tool reproduces itself off-tree.
- **Negative control**: one named path mutated
  (`tools/replay-frozen.py` → `tools/replay-FROZEN-missing.py`, all 3
  occurrences) → `named 28, resolvable 27, "unnamed_in_skill":
  ["tools/replay-FROZEN-missing.py"]`, **exit 1**, and the tool's own
  `skill_sha256` field tracked the mutation (`406ab3c2…`).
  So the survey's green is a real pass/fail contract bound to the live bytes,
  not a constant — the strongest available answer to "could this check ever
  go red?".

## 4. Row set at `f9bd07c2…` (authoritative for the C02 row-for-row diff)

| # | executable | SKILL line | resolves | sha256 (first 16) |
|---|---|---|---|---|
| 1 | `tools/assemble-culture-d3.py` | 673 | yes | `ba8d19d5855fe670` |
| 2 | `tools/assemble-culture-d4.py` | 207 | yes | `943f487ba991d45d` |
| 3 | `tools/assemble-d2-typed.py` | 449 | yes | `c7e5a7493601d331` |
| 4 | `tools/assemble-d2.py` | 615 | yes | `8ea6bdde9514ee96` |
| 5 | `tools/assemble-d4-typed.py` | 139 | yes | `92f5460bcc34ffbb` |
| 6 | `tools/check-craft-exercise.py` | 616 | yes | `b5b890b4b9c9953b` |
| 7 | `tools/check-evidence-coupling.py` | 674 | yes | `849494b0c4113885` |
| 8 | `tools/check-gate-battery.py` | 617 | yes | `455b595ad6d5b1be` |
| 9 | `tools/d2-typed-labels.py` | 35 | yes | `2819f68769dfc0b5` |
| 10 | `tools/exercise-handoff-e2e.py` | 448 | yes | `a5e4a8c5dda9d63c` |
| 11 | `tools/gates/argot-derivation-gate.py` | 375 | yes | `b5406bcdaf41c595` |
| 12 | `tools/gates/costume-era-consistency-gate.py` | 609 | yes | `e6bffd7020c0b116` |
| 13 | `tools/gates/d4-assembly-check-gate.py` | 450 | yes | `df1a364b3970365c` |
| 14 | `tools/gates/d4-typed-labels-check-gate.py` | 451 | yes | `05f99629d870280c` |
| 15 | `tools/gates/handoff-packet-check.py` | 500 | yes | `e2fa3223b2aa5738` |
| 16 | `tools/gates/lexicon-coverage-audit.py` | 607 | yes | `2c4dd39702a15ea3` |
| 17 | `tools/gates/myth-consistency-gate.py` | 608 | yes | `5368b13542cd4b8a` |
| 18 | `tools/gates/naming-collision-gate.py` | 610 | yes | `d9e4e8f4f93a21b3` |
| 19 | `tools/gates/phonology-sanity-gate.py` | 606 | yes | `d5fe087ffb2342e5` |
| 20 | `tools/gates/provenance-audit.py` | 611 | yes | `8a96aaf4ccd14ef4` |
| 21 | `tools/gates/register-law-gate.py` | 409 | yes | `15f8b23251ca2ad0` |
| 22 | `tools/gates/typed-pipeline-gate.py` | 138 | yes | `b749ad07cf171027` |
| 23 | `tools/harness/packet_links.py` | 452 | yes | `66d854cc710f0b14` |
| 24 | `tools/harness/packet_uncertainty.py` | 89 | yes | `cdcc19319269ee90` |
| 25 | `tools/harness/r8_checks.py` | 454 | yes | `0fb21d8e414c2d92` |
| 26 | `tools/harness/receipt_guard.py` | 453 | yes | `d2297da4e6ceabb2` |
| 27 | `tools/replay-frozen.py` | 212 | yes | `a2fb5c98260a07f0` |
| 28 | `tools/source-audit-inventory.py` | 614 | yes | `f617bb99318f501d` |

Machine-comparable form of the same rows (this is what C02's block must match;
the comparator in §7 consumes exactly this shape):

```json
{
 "skill_sha256": "f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b",
 "skill_lines": 732,
 "git_head": "da68a6d",
 "date": "2026-10-19",
 "named": 28,
 "resolvable": 28,
 "unnamed_in_skill": [],
 "rows": [
  {"executable": "tools/assemble-culture-d3.py", "first_line": 673, "resolves": true, "sha256": "ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014"},
  {"executable": "tools/assemble-culture-d4.py", "first_line": 207, "resolves": true, "sha256": "943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2"},
  {"executable": "tools/assemble-d2-typed.py", "first_line": 449, "resolves": true, "sha256": "c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071"},
  {"executable": "tools/assemble-d2.py", "first_line": 615, "resolves": true, "sha256": "8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d"},
  {"executable": "tools/assemble-d4-typed.py", "first_line": 139, "resolves": true, "sha256": "92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0"},
  {"executable": "tools/check-craft-exercise.py", "first_line": 616, "resolves": true, "sha256": "b5b890b4b9c9953be5ed5f5453a2b60bc9c856616b0a5b28cb2b5bca6ffdf7b5"},
  {"executable": "tools/check-evidence-coupling.py", "first_line": 674, "resolves": true, "sha256": "849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e"},
  {"executable": "tools/check-gate-battery.py", "first_line": 617, "resolves": true, "sha256": "455b595ad6d5b1be7844fc9b53a259a5b8a0efbd788b129dbfd2cc0d0ad173ce"},
  {"executable": "tools/d2-typed-labels.py", "first_line": 35, "resolves": true, "sha256": "2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3"},
  {"executable": "tools/exercise-handoff-e2e.py", "first_line": 448, "resolves": true, "sha256": "a5e4a8c5dda9d63c177a3dce75a8716ba5d285371d0a37a2535f6c323e7619df"},
  {"executable": "tools/gates/argot-derivation-gate.py", "first_line": 375, "resolves": true, "sha256": "b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb"},
  {"executable": "tools/gates/costume-era-consistency-gate.py", "first_line": 609, "resolves": true, "sha256": "e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f"},
  {"executable": "tools/gates/d4-assembly-check-gate.py", "first_line": 450, "resolves": true, "sha256": "df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a"},
  {"executable": "tools/gates/d4-typed-labels-check-gate.py", "first_line": 451, "resolves": true, "sha256": "05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841"},
  {"executable": "tools/gates/handoff-packet-check.py", "first_line": 500, "resolves": true, "sha256": "e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575"},
  {"executable": "tools/gates/lexicon-coverage-audit.py", "first_line": 607, "resolves": true, "sha256": "2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287"},
  {"executable": "tools/gates/myth-consistency-gate.py", "first_line": 608, "resolves": true, "sha256": "5368b13542cd4b8a5bd850d83835e588df13a72b7d6c502b2aa016ee36b95f08"},
  {"executable": "tools/gates/naming-collision-gate.py", "first_line": 610, "resolves": true, "sha256": "d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d"},
  {"executable": "tools/gates/phonology-sanity-gate.py", "first_line": 606, "resolves": true, "sha256": "d5fe087ffb2342e54cd6d6f3ef1e891315a95224bc25cdc5bc425b91dec34230"},
  {"executable": "tools/gates/provenance-audit.py", "first_line": 611, "resolves": true, "sha256": "8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a"},
  {"executable": "tools/gates/register-law-gate.py", "first_line": 409, "resolves": true, "sha256": "15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169"},
  {"executable": "tools/gates/typed-pipeline-gate.py", "first_line": 138, "resolves": true, "sha256": "b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85"},
  {"executable": "tools/harness/packet_links.py", "first_line": 452, "resolves": true, "sha256": "66d854cc710f0b143e0a254d03e7f59ebce2c6b759d336ca368a9689babbd899"},
  {"executable": "tools/harness/packet_uncertainty.py", "first_line": 89, "resolves": true, "sha256": "cdcc19319269ee908577252485cc38288833b50987ed22a266c8eb01894b0e26"},
  {"executable": "tools/harness/r8_checks.py", "first_line": 454, "resolves": true, "sha256": "0fb21d8e414c2d92b3f20742817ac9d89be24b1142b1bc65b5070086aa17fbfe"},
  {"executable": "tools/harness/receipt_guard.py", "first_line": 453, "resolves": true, "sha256": "d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1"},
  {"executable": "tools/replay-frozen.py", "first_line": 212, "resolves": true, "sha256": "a2fb5c98260a07f0801f4bf21f349283638da6796645780393262e4368c79464"},
  {"executable": "tools/source-audit-inventory.py", "first_line": 614, "resolves": true, "sha256": "f617bb99318f501db2ff51c0c180daeacf548b1a36591b1a1a80c253197b2210"}
 ]
}
```

## 5. Tracked-at-HEAD check (resolution is not an untracked-file artefact)

`git ls-tree -r --name-only HEAD` lists 2735 paths; 0 of my 28 named
executables are absent from that set. Command output:

```
named rows: 28
tracked@HEAD total: 2735
named executables NOT tracked at HEAD: 0 []
all 28 named executables are HEAD-tracked: True
```

So every "resolves: yes" verdict is satisfied by a file that exists in the
filed revision's tree, not by a stray local file.

## 6. Findings for the integrator (accuracy, not blockers)

1. **The tool's `date` field is hardcoded, not measured.**
   `reports/round-30/craft/box1-survey.py:8` sets `"date": "2026-10-18"`, so
   the re-run's console output still says 2026-10-18 even though it ran today;
   the live `skill_sha256` field is read from disk on `:10`. The durable
   round-34 receipt must carry its own **2026-10-19** date field (and should
   not be described as "the tool's output, dated"). C02's receipt handles this
   correctly: its `survey_stdout.date` is kept as the script's filing date and
   the run date is carried in `measured_at_utc`
   (`reports/round-34/calib/C02-receipt-json.md:29,:45,:51`); I verified both
   citations against the tool's source (`grep -n 'date\|skill_sha256'`).
2. **Name the three digests precisely.** The durable r30 artifact pins
   `83b0a78a…` (`reports/round-30/craft/box1-landed-survey.json:4`, also
   `reports/round-30/validation.json:1420`); the r32/r33 re-verifications were
   console-only at `79fe91d3…` (`reports/round-32/final-dossier.md:46`,
   `LOG.md:3577`); HEAD is `f9bd07c2…`. Claim C's "before" prose is best
   worded as: the *durable* pin is two revisions stale (r30 bytes) and every
   interim green is console-only at `79fe91d3…`; `f9bd07c2…` is the first
   durable pin.
3. **28 is scoped to these bytes, not a constant.** If claim O lands
   `tools/harness/receipt_guard_adoption.py` and a later `SKILL.md` edit names
   it, the named set becomes 29 and the tool's exit-1 contract applies to the
   new set. At HEAD `grep -n receipt_guard_adoption SKILL.md` → no match
   (0 occurrences), so 28 is correct at `f9bd07c2…`. The durable JSON should
   therefore carry `skill_sha256` **and** `skill_lines` (732) as its scope pin,
   exactly as the tool does.
4. **Box-1 here is the SKILL-named executable surface only.** None of the 28
   paths is under `tools/gates/frozen/**`; the survey says nothing about the
   frozen battery or about `tools/*.py` files that SKILL.md does *not* name.
5. **`unnamed_in_skill: []` is a checked claim, not a default.** The
   negative control (§3) produced a non-empty `unnamed_in_skill` list from the
   same code path, so the empty list at `f9bd07c2…` is measured.

## 7. Row-for-row comparison with C02 — DONE, green

`reports/round-34/calib/C02-receipt-json.md` first landed at 2026-10-19T07:07Z
and was re-emitted by its author at 2026-10-19T07:10:37Z. I compared against
**both** revisions and record the digest I compared:

| compared C02 revision | C02 file sha256 | C02 `measured_at_utc` | rows | mismatches |
|---|---|---|---|---|
| 1st | (block `:26-363`) | 2026-10-19T07:07:09Z | 28 | 0 |
| 2nd | `e26b301513679058831175e2104036548e42715045c37ff7dd3c86f027d002bb` | 2026-10-19T07:10:37Z | 28 | 0 |
| 3rd (current at 07:11Z) | `3e7edaa2970341bba1401c910f700a61f222f32cc276df47c6feb1e84f6337b3` | 2026-10-19T07:11:01Z | 28 | 0 |

C02 re-emitted its fragment three times inside five minutes while I was
verifying; **all three revisions carry identical row content** (same 28
executables, same line anchors, same digests). My verdict therefore attaches to
the row content, not to one file digest: if C02 re-emits again, re-run the
self-tested comparator (§7 code) against the new revision — a mismatch in
`resolves`, `line`, `lines[]` or per-executable `sha256` is a claim-C blocker.

(Line anchors move between revisions — the current block is at `:32-369` with
top-level pins at `:34-58` — so a future check should key on the file digest,
not the line numbers.)

**Pass 1 (naive key match) — insufficient, recorded for honesty.** A first
comparator matched only key names present in both fragments; C02's rows use
`line`/`lines` while mine used `first_line`, so the line check silently
no-op'd. It reported `0 field mismatches`, which on its own did **not** prove
line agreement. I caught this and re-ran with normalized key names.

**Pass 2 (strict, normalized) — the binding result, re-confirmed on the
current C02 bytes (`e26b3015…`):**

```
compared C02 revision sha256: e26b301513679058831175e2104036548e42715045c37ff7dd3c86f027d002bb
C02 measured_at_utc: 2026-10-19T07:10:37Z
C07 rows: 28 | C02 rows: 28
missing in C02: [] | extra in C02: []
per-row mismatches (resolves/line/lines[]/sha256): 0 []
C02 skill_sha256 match: True | skill_lines: True | 28/28/0: True
survey script digest match: True
C02 survey_stdout == my re-run stdout: True
rows whose digest != HEAD blob: 0 []
C02 fence lines: [32, 369, 373, 395]
```

The first revision's run produced the same per-row verdict (`per-row field
mismatches (resolves/line/lines[]/sha256): 0`, `C02 date: 2026-10-19 |
measured_at_utc: 2026-10-19T07:07:09Z`), plus this scan observation, kept here
because it documents that C02's `lines[]` arrays carried the duplicate
same-line occurrences rather than deduplicating them:

```
occurrence lists differing from single-line: {'tools/d2-typed-labels.py': [35, 169, 208, 258, 272, 281, 288, 289, 290, 291, 292, 293, 304, 308, 329, 479, 481, 483, 491], 'tools/harness/packet_uncertainty.py': [89, 128, 501], 'tools/gates/typed-pipeline-gate.py': [138, 187, 196, 209, 212, 418, 431, 439], 'tools/assemble-d4-typed.py': [139, 158, 163, 195, 207, 210, 211, 213, 294], 'tools/replay-frozen.py': [212, 573, 613], 'tools/gates/argot-derivation-gate.py': [375, 376, 377, 429, 438], 'tools/gates/register-law-gate.py': [409, 409, 410, 418, 430, 439], 'tools/gates/handoff-packet-check.py': [500, 500, 612], 'tools/check-gate-battery.py': [617, 617, 617]}
```

9 of the 28 paths are named on more than one SKILL.md line, and three of them
repeat a path twice on one line; C02's `lines[]` matched my scan on all 28 rows
under both revisions. Nothing in these blocks is reconstructed.

So: **28/28 rows agree** on `resolves`, first-occurrence line, all-occurrence
line lists, and per-executable sha256; C02's scope pins
(`skill_sha256` `f9bd07c2…`, `skill_lines` 732, 28/28/0) equal my independent
readings; C02's captured `survey_stdout` equals the stdout of my own re-run
field for field, including the hardcoded `"date": "2026-10-18"` and the empty
`unnamed_in_skill`.

**Independent re-hash of C02's digests against the filed revision**
(not the working tree):

```
rows checked against HEAD blob: 28 | digests differing from HEAD blob: 0 []
```

i.e. `git cat-file -p HEAD:<path>` reproduces every per-executable digest in
C02's rows. Nothing in C02's row set came from a local, untracked or modified
file.

The comparator itself was self-tested before use: against an identical fixture
it reports `0 field mismatches`, against a fixture with one mutated row it
reports `MISMATCH tools/assemble-d4-typed.py first_line 139 != 999` — so the
green result is a measurement, not a vacuous pass.

For the record, the digest of my own 28-row canonical TSV (a cheap
anti-tamper anchor for the comparison) is
`b65f0a1e6a5c4fe19e8d8a5ee62024f6a98cc12d0b8e9a3b9a573a9ccbad99a9`
(`.scratch/c07/py.canon`, regenerable from §4).

## Owed: none

(`reports/round-34/calib/C02-receipt-json.md` landed during my run; the
row-for-row verification it was owed is reported complete in §7.)

## Citations

- `SKILL.md` (sha256 `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`,
  732 lines) — the verified surface; lines 35, 89, 138, 139, 207, 212, 375,
  409, 448–454, 500, 606–611, 614–617, 673, 674 are the first occurrences
  named in §4.
- `reports/round-30/craft/box1-survey.py:4` (root via `parents[3]`), `:6`
  (regex extraction), `:7` (`is_file()` resolution), `:8` (hardcoded date),
  `:10` (live `skill_sha256` read) — the filed survey tool, sha256
  `d923ae0fcd544513122851b55389111b3195528f8e3a4c8fb69703072132cf89`.
- `reports/round-34/calib/C02-receipt-json.md` — the compared artifact, in two
  revisions: first (28-row JSON block `:26-363`, `survey_stdout` at `:45-51`,
  `measured_at_utc` 2026-10-19T07:07:09Z at `:28-29`) and current
  (sha256 `e26b301513679058831175e2104036548e42715045c37ff7dd3c86f027d002bb`,
  block `:32-369`, pins `:34-58`, `measured_at_utc` 2026-10-19T07:10:37Z).
  Line anchors move between revisions — key on the digest.
- `reports/round-30/craft/box1-landed-survey.json:4` — durable r30 pin
  `83b0a78a…`.
- `reports/round-30/validation.json:1420` — r30 receipt pin `83b0a78a…`.
- `reports/round-32/final-dossier.md:46` — r32 green recorded as console output
  at `79fe91d3…`.
- `LOG.md:3577` — digest movement `79fe91d3…` → `f9bd07c2…` at round 33.
- `reports/round-34/claims.json` (claim C `counting_commands`, thresholds) and
  `reports/round-34/targets.json` (seat C07 mission/out) — the binding ask.
- Commands run (all in
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, `TMPDIR=$PWD/.scratch`,
  `PYTHONDONTWRITEBYTECODE=1`): `sha256sum SKILL.md`;
  `sha256sum reports/round-30/craft/box1-survey.py`; `wc -l SKILL.md`;
  `git rev-parse --short HEAD`; `git status --porcelain SKILL.md tools/`;
  `git diff --stat HEAD -- SKILL.md tools/`; `git ls-tree -r --name-only HEAD`;
  `git cat-file -p HEAD:<path>` (28×, digest check);
  `python3 -B reports/round-30/craft/box1-survey.py` (twice, `diff` of outputs);
  `python3 -B .scratch/c07/indep_survey.py` (independent token-split method);
  `grep -nEo "tools/[A-Za-z0-9_./-]+\.py" SKILL.md` + per-row `test -f`;
  `LC_ALL=C sort` + `diff` of the two row files; isolated-copy parity and
  negative controls under `.scratch/c07/ctrl/tree/` (filed tool copy, mutated
  `SKILL.md`); `.scratch/c07/compare.py` self-tested on identical and mutated
  fixtures; strict normalized row comparison vs C02 (§7);
  `grep -n receipt_guard_adoption SKILL.md`.
- No filed bytes were written; the only artifact I produced is this file.
