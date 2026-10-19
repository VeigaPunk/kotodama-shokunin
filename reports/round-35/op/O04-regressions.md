- Seat: O04 | executor | claim O | date 2026-10-19 | baseline 4a7aede

# O04 — Regression census: every v3/e2e behavior the R34-N1 patch must NOT change

Claim O (`reports/round-35/claims.json:37-52`) hardens the v3 replay path against
R34-N1 (`reports/round-34/handoff/repin.json:15-22,50`: "r6-row refusal surfaces as
an unhandled KeyError, not the designed E2E-DIGEST leg", state `routed`). This
fragment is the census side of that claim: the surfaces the patch must leave
exactly as they are, each with the command that proves it and the observed
before-state at 4a7aede.

## 0. Method and write discipline

- All commands run from the repo root with
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, tree = 4a7aede plus
  untracked `reports/round-35/` (`git status --porcelain` = `?? reports/round-35/`).
- The renderer was run **in-tree in non-freeze modes only** (read-only: it writes
  only under `TMPDIR`; `tools/exercise-handoff-e2e.py:92-94`). The one `--freeze`
  leg was run in an **isolated `git archive 4a7aede` copy** under
  `.scratch/o04/iso/`, never in-tree (the declared-in-r7 freeze bytes are pinned).
- No `reports/round-*/run-validation.py` was executed in-tree or anywhere
  (F-C13-1); filed validators were only **read**.
- Scratch evidence kept at `.scratch/o04/` (`selftest.out`, `selftest.err`,
  `drift_r6b.py`, `v3json.out`, `iso/`). Nothing durable was written outside this
  fragment; the raw outputs needed to reproduce every number below are inlined.

## 1. Before-state: the defect and its exact site

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
      --baseline reports/round-30/handoff/declared-in-r6/expected.json
Traceback (most recent call last):
  ...
  File ".../tools/exercise-handoff-e2e.py", line 3822, in v3_exercise
    record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
KeyError: 'reports/round-20/handoff/claims-map.md'
exit=1
```

- Site: `tools/exercise-handoff-e2e.py:3822` — the per-file drift record indexes
  `assembly.digests[rel]` directly, while the gate condition on `:3819` uses
  `.get(rel)`. `assembly.digests` is keyed by the **live** `V3_READ_SET`
  (`:3481-3484`), so a baseline row naming a member the renderer no longer
  measures reaches the record with no key.
- Classification of the r6 row against the live read set (script
  `.scratch/o04/drift_r6b.py`, importing the renderer read-only):
  `unresolvable-by-read-set: ['reports/round-20/handoff/claims-map.md']`,
  `drifted: []`, `matched: 57`. **The unresolvable member is the row's only
  defect** — no other member drifted, so post-patch the r6 replay must refuse
  with exactly one named diagnostic and zero drift records.
- The refusal class is fixed by the renderer's own documented contract:
  `:89-95` — "Exit codes (stable messages, no traceback): 0 clean; 1 mismatch —
  `E2E-DIGEST`, `E2E-COUNT`, `E2E-GATE`, `E2E-SCAN`, `E2E-UNC`, `E2E-LINK`;
  2 could-not-evaluate — `E2E-ARTIFACT` (missing/unreadable read-set file),
  `E2E-BASELINE` (absent or edited baseline), `E2E-DATA`". A traceback is a
  contract breach, not a diagnostic.

## 2. Regression surfaces (what must not change)

Each row: surface → why the patch can move it → pinned before-state (observed
2026-10-19 at 4a7aede) → fail signature to watch.

| # | Surface | Why it can move | Pinned before-state | Fail signature |
|---|---|---|---|---|
| R1 | r7 default chain (`--profile v3 --quiet`) | the patch edits `v3_exercise`'s drift branch, which every run passes through | exit 0; `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` | any non-zero exit, any changed token, or a moved `packet_sha256` |
| R2 | read-set leg + preservation leg | the same loop and the `snapshot_before/after` pair (`:3816`, `:3958-3968`) | `input-digest: 58 read-set digests match the frozen baseline`; `preservation: the 58 read-set files are byte-identical before and after the run` | a new record on a clean run; a shorter/renamed record |
| R3 | r6-row replay (the patch's own target) | this is the changed path | exit 1, raw traceback, `KeyError` (above) | **after the patch**: non-zero exit, no `Traceback`/`KeyError`, one named diagnostic carrying `reports/round-20/handoff/claims-map.md` (code `E2E-READSET` per `claims.json:40`, reconciled with O08's leg spec); exit 0 is refused in every case |
| R4 | tamper/refusal controls in the selftest | they exercise the same drift loop and the neighbouring legs | `m12a tamper baseline: exit 2 E2E-BASELINE`; `m12b tamper read-set (D4 projection): exit 1 E2E-DIGEST naming the changed file`; `m8 re-typed v2 row: exit 1 E2E-DIGEST`; `tamper scan expectation: exit 2 E2E-BASELINE`; `missing D4 artifact: exit 2 E2E-ARTIFACT naming the unreadable path` | the new branch capturing the **resolvable-but-drifted** class: `m12b`/`m8` losing `E2E-DIGEST` or exit 1 (see §3) |
| R5 | freeze semantics | `v3_freeze` (`:3979-4128`) reuses assembly, gate, semantics and the same read set | isolated copy: freeze #1 exit 0 writing `expected.json`+`packet.md`+`twin.json`+`run.log`+`freeze.txt`, packet `45f571…`, expected `bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55`; re-freeze exit 0 with `no tracked value changed since the previous freeze`; refusals preflight/gate/scan/uncertainty/links (`:3983-4006`) unchanged | a different digest from the same bytes; a changed refusal code; any in-tree `--freeze` of declared-in-r7 |
| R6 | r34 selftest suite | the patch adds two controls to `v3_selftest` (`:4154-4468`) | exit 0; header `selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0, links=105/105, claims=27, statuses=16/7/4, v2_subset=equal, alias_leg=landed) plus 39 controls:`; **40 `  - ` result lines** (the header subtracts `results[0]`, the witness-parser control) | any pre-existing control line disappearing or changing text; the witness-parser control (`:4156-4169`) no longer refusing partial/undersized/unparsed/nonzero-exit suites |
| R7 | D4 witness legs inside assembly | `V3Assembly` runs 4 subprocess legs and gates `alias_state` on two of them (`:3543-3560`) | `tools/d2-typed-labels.py --selftest` → exit 0, `selftest: 163/163 checks passed`; `tools/assemble-d4-typed.py --selftest` → exit 0, `selftest: 12/12 checks passed`; witness minimums 50 and 12 (`:3553`) | either sub-tool's count dropping below its minimum or the `selftest: N/N checks passed` shape changing |
| R8 | CLI/output contract consumed by filed validators | the patch may be tempted to add text to the summary or error lines | `--quiet` prints the summary line only; `--json` prints 15 `checks` and top-level keys `['baseline','checks','code','exit','profile','root']`; error line only when not `--quiet` (see §4) | changed field order/regex (e.g. `reports/round-22/run-validation.py:706` needs `fields=(\d+)/(\d+)\s+glossary=(\d+)/(\d+)\s+findings=(\d+)`, `:705` needs `links=(\d+)/(\d+)`; `reports/round-20/run-validation.py:1377-1379`; `reports/round-20/run-validation.py:765` needs the `selftest: OK` prefix) |
| R9 | v1/v2 profiles | the patch touches shared helpers (`main` branches, `v3_*` only — but a careless shared edit can reach them) | `--profile v2 --quiet` exit 0, `handoff-v2: exit=0 claims=15 links=50/50 drift=named(tools/harness/packet_links.py round-16)`; `--profile v1 --quiet` exit 1, `handoff-e2e: exit=1 fields=? … packet_sha256=(not assembled)`; `--profile v1 --selftest` exit 0, `plus 17 controls`; `--profile v2 --freeze DIR` exit 2, `could not freeze: E2E-DATA the v2 baseline is a filed round-15 artifact (read-only)`, no directory written | v1's pre-existing `E2E-DIGEST` (frozen `tools/d2-typed-labels.py` `0da0015f…` vs live `2819f687…`) silently "fixed" or changed; v2 baseline re-frozen |
| R10 | gate/harness collateral | the read set includes the gate and both harness tools; the patch must not touch them | tamper control `tools/gates/handoff-packet-check.py` on a `packet_id`-dropped copy → exit 1, `HO-MISSING`, `scan: fields=15/16 … findings=1`; `tools/check-gate-battery.py --selftest` → exit 0, `SELFTEST OK 44/44` | any edit under `tools/gates/**`, `tools/harness/**`, or the read-set members |

## 3. The critical coupling: the drift loop is shared by R3 and R4

`m12b` (tamper a read-set member) and `m8` (re-typed v2 row) reach the **same**
loop as the r6 row. The patch must therefore key the new branch on the
*absent-from-read-set* class only:

- member **absent** from `V3_READ_SET` → new named diagnostic (`E2E-READSET`),
  naming the path;
- member **present but digest-different** → unchanged `E2E-DIGEST`, exit 1, the
  per-file `input-digest` record with frozen/live digests (`:3820-3823`), which
  `m12b`/`m8` assert by code and `reports/round-34/run-validation.py`-style legs
  assert by control line.

A fix that collapses both classes (e.g. `E2E-READSET` for any drift, or exit 2
for all of them) breaks R4 — this is the regression most likely to be introduced
by the patch, and it is invisible to the r6-row acceptance leg alone.

## 4. Finding O04-F1: under `--quiet` the diagnostic code is not printed at all

`main()` guards the error line with `not args.quiet` in all three profiles
(`:4515-4516` v2, `:4554-4555` v1, `:4603-4604` v3), so today:

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v1 --quiet     # exit=1
handoff-e2e: exit=1 fields=? glossary=?/20 findings=? packet_sha256=(not assembled)
$ python3 -B tools/exercise-handoff-e2e.py --profile v1             # verbose
handoff-e2e: E2E-DIGEST: 1 read-set file(s) changed since the baseline was frozen: tools/d2-typed-labels.py
```

The O08 acceptance leg runs the r6 replay **with `--quiet`** and requires the
`E2E-READSET` token and the member path on stdout
(`reports/round-35/op/O08-validation-legs.md:55-66,212-213`). With the quiet
guard as it stands, a post-patch `Failed("E2E-READSET", …)` would print **no**
code under `--quiet` — only `handoff-v3: exit=1 …` — and that leg would fail for
a reason unrelated to the fix. Three resolutions, all of which must be recorded
as a deliberate output-contract decision (none is mine to take):

1. print the `handoff-v3: {err}: …` line regardless of `--quiet` (adds a line to
   the quiet contract; additive, and no filed validator's regex is anchored on
   "quiet prints exactly one line");
2. carry the code into the summary line (changes an existing line that filed
   validators regex — riskier);
3. drop `--quiet` from the acceptance leg (zero renderer change; the leg then
   reads the existing error line).

My census's requirement is only the invariant: **whichever option lands, the
verbose (`--json`) run must still emit `handoff-v3: exit=N fields=… packet_sha256=…`
with the same field order, and the code must be readable by a consumer that does
not parse a traceback.**

## 5. Finding O04-F2 (trap): the frozen packet preamble names the superseded round-20 map

`tools/exercise-handoff-e2e.py:2698-2700` is a packet **preamble literal**:

> "…the twelve D4 rows are carried from `reports/round-20/handoff/claims-map.md`."

That exact sentence is byte 3 of the frozen packet
(`reports/round-34/handoff/declared-in-r7/packet.md:3`, sha256
`45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`; the twin
carries 0 occurrences of the string — `grep -c` on `twin.json`). The same
constant is interpolated correctly elsewhere (`:2934` uses `{CLAIMS_MAP}`;
packet lines 95/113/125 name the r7 map).

**A "cleanup" of the stale round-20 name at `:2698-2700` moves `packet_sha256`
and breaks the pinned r7 row and the R34-D-default-pointer control
(`reports/round-34/handoff/repin.json:7-14,23-31`).** The patch must not touch
it; the stale string is part of the frozen bytes and can only be corrected by a
future re-freeze row with a recorded reason, which is a non-goal of round 35
(`claims.json:71`).

## 6. Finding O04-F3 (documentation drift, not frozen bytes)

The module docstring still lists the round-20 map as a read-set member:
`:34` and `:57-59` ("…the two harness validators,
reports/round-20/handoff/claims-map.md (the D4 rows' copy surface) and
reports/round-19/validation.json … — 58 files"), while `CLAIMS_MAP` is the r7
map (`:184`). Docstrings are not packet bytes, so correcting `:34`/`:57` is safe
and is the natural companion to the docstring edit the exit-code table needs
(`:89-95` must gain `E2E-READSET`). Owner: the patch's docstring update
(O01/integrator); it must be recorded as a docstring edit, not silently bundled.

## 7. Regression command list (runnable; run at the delivered revision)

Run from the repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.
"Before" values are the 4a7aede observations in §2; "after" is the requirement.

| # | Command | Before (4a7aede) | After (required) |
|---|---|---|---|
| 1 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0, packet `45f571…` | **identical line and digest** |
| 2 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | exit 1, traceback, `KeyError` | non-zero, **no traceback**, `E2E-READSET` + `reports/round-20/handoff/claims-map.md` on one line |
| 3 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` | exit 0, `plus 39 controls`, 40 result lines | exit 0, `plus 41 controls`, 42 lines, all 40 prior lines present verbatim + the two new controls |
| 4 | `python3 -B tools/exercise-handoff-e2e.py --profile v2 --quiet` | exit 0, `links=50/50 claims=15` | identical |
| 5 | `python3 -B tools/exercise-handoff-e2e.py --profile v1 --quiet` | exit 1, `packet_sha256=(not assembled)` | identical (the drift is pre-existing and out of scope) |
| 6 | `python3 -B tools/exercise-handoff-e2e.py --profile v1 --selftest` | exit 0, `plus 17 controls` | identical |
| 7 | `python3 -B tools/exercise-handoff-e2e.py --profile v2 --freeze .scratch/o04/v2freeze` | exit 2, `E2E-DATA … filed round-15 artifact`, no dir | identical |
| 8 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline .scratch/o04/nope.json` | exit 2 (`E2E-BASELINE`, "frozen baseline not found") | identical |
| 9 | isolated copy only: `git archive 4a7aede \| tar -x -C .scratch/o04/iso && (cd .scratch/o04/iso && python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze reports/o04-tmp/declared-in-r7)` twice | freeze #1 exit 0 packet `45f571…`, expected `bbe158…`; re-freeze exit 0, `no tracked value changed` | identical digests from the delivered renderer (proves the patch does not feed the packet bytes) |
| 10 | `sha256sum reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json,freeze.txt,claims-map.md}` | `45f571…`, `0e229138…`, `bbe158…`, `3969954b…`, `d181de28…` | **all five unchanged** |
| 11 | `sha256sum reports/round-30/handoff/declared-in-r6/{packet.md,expected.json}` | `6ced88ad…`, `ea1e2927…` | unchanged (r6 bytes stay filed) |
| 12 | `python3 -B tools/gates/handoff-packet-check.py <tampered packet copy>`; `python3 -B tools/check-gate-battery.py --selftest` | exit 1 `HO-MISSING`; exit 0 `44/44` | identical (patch touches neither) |
| 13 | `python3 -B tools/d2-typed-labels.py --selftest`; `python3 -B tools/assemble-d4-typed.py --selftest` | exit 0 `163/163`; exit 0 `12/12` | identical (witness minimums 50/12 still satisfied) |

Rows 9-12 are the freeze-byte and collateral legs; rows 1-3 are the patch's own
before/after; rows 4-8 are the "no collateral movement" legs.

## 8. Agreement with the acceptance side (O08) and deltas

`reports/round-35/op/O08-validation-legs.md:53-66,138-175,206-234` pins
`E2E-READSET` + member path on one line, exit 1 **or** 2 (its preference is 2 by
the could-not-evaluate convention, with `claims.json:48`'s "(expect: exit 1)"
recorded as a named deviation if 2 lands), no traceback, and preservation of the
`m12a`/`m12b` control lines. This census agrees and adds three things it does not
cover: (a) the `--quiet` suppression of the code (§4) makes its own leg
unreachable unless the output contract changes; (b) the shared drift loop means
the new branch must not capture the drifted class (§3); (c) the frozen preamble
at `:2698-2700` is a no-touch zone (§5). No contradiction between the two
fragments was found.

## 9. Observations (not requirements)

- `--keep DIR` (`:4490`) is accepted but referenced nowhere else in the file
  (`grep -n "args\.keep"` → only the definition): a dead flag. It must not start
  behaving differently as a side effect of this patch; wiring it is an unclaimed
  behavior change and belongs to a future claim.
- The renderer is **not** in `V3_READ_SET` (verified: the r7 `inputs` has no
  self-reference, 58 keys, `reports/round-34/handoff/declared-in-r7/claims-map.md`
  the only claims-map key) — this is what lets the patch land without moving any
  frozen digest, and it must stay that way.

## Owed

- `reports/round-35/op/O01-patch-draft.md` — missing at write time (dir `op/`
  existed, file absent). Rows 2-3 and 9-13 of §7 can only be executed post-patch;
  O03/O05/O11 (isolated verify) or the integrator must run the §7 after-column
  and record the observed outputs. My census pins the expectations they check
  against, so the owed item is the after-state evidence, not the census.
- `reports/round-35/scout/K03-keyerror-path.md` — missing (no `scout/` dir at
  write time). My traceback capture is first-hand (in-tree, non-freeze, read-only
  run reproduced above), so nothing here blocks on it; K03 should cross-check the
  `:3822` site and the "57 matched / 0 drifted / 1 unresolvable" split.
- `reports/round-35/plan/P02-oa-plan.md` — missing (no `plan/` dir at write time);
  the convention choice in §4 is its call to make explicit.
- `.scratch/o04/` is scratch evidence, not durable telemetry; if the integrator
  wants the raw outputs filed, the inline blocks in §1/§2/§4 are the citable
  record and the scratch copy must be landed by the parent under
  `reports/round-35/telemetry/` per `AGENTS.md` before scratch cleanup.

## Citations

- `REGIMEN.md:25-50` — per-round contract (declared claims, verdicts, no forced pass).
- `reports/round-35/claims.json:37-52` — claim O, before/after, thresholds, counting commands.
- `reports/round-35/claims.json:71` — non-goal: no re-freeze of declared-in-r7.
- `reports/round-35/targets.json` (seat O04 mission + `shared_rules`) — write boundary, no in-tree filed-runner execution.
- `reports/round-34/handoff/repin.json:7-31,49-52` — R34-D rows, pinned r7 digests, R34-N1 finding.
- `reports/round-34/handoff/declared-in-r7/freeze.txt` — freeze lines, claims/statuses, re-freeze diff.
- `reports/round-34/handoff/declared-in-r7/packet.md:3,95,113,125` — frozen preamble naming round-20 map; manifest/ledger rows naming r7 map.
- `tools/exercise-handoff-e2e.py:34,57-59,63,89-95` — docstring read-set list, drift contract, exit-code table ("stable messages, no traceback").
- `tools/exercise-handoff-e2e.py:184,1930-1967` — `CLAIMS_MAP`, `V3_PROFILE`/`V3_PACKET_VERSION`/defaults/`V3_READ_SET`/`V3_DECLARED`.
- `tools/exercise-handoff-e2e.py:2698-2700,2934` — preamble literal (frozen) vs interpolated ledger description.
- `tools/exercise-handoff-e2e.py:3481-3484,3816-3824` — `assembly.digests` construction; drift gate (`.get`) and the `KeyError` record.
- `tools/exercise-handoff-e2e.py:3855-3968` — gate/semantics/scan/uncertainty/links/census/digest/preservation legs and their codes.
- `tools/exercise-handoff-e2e.py:3979-4006,4009-4128` — freeze refusals, baseline payload, written files, re-freeze diff.
- `tools/exercise-handoff-e2e.py:4154-4169,4459-4468` — selftest witness parser and the 39-control suite.
- `tools/exercise-handoff-e2e.py:4476-4609` — CLI: `--quiet`/`--json`/`--keep`/`--freeze`, per-profile branches, quiet-guarded error lines (`:4515,:4554,:4603`).
- Commands (all run at 4a7aede, 2026-10-19): `--profile v3 --quiet` (exit 0, packet `45f571…`); `--profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` (exit 1, KeyError at `:3822`); `--profile v3 --selftest` (exit 0, 39 controls/40 lines, 39.4 s); `--profile v3 --json` (15 checks); `--profile v1 --quiet` (exit 1) and verbose (E2E-DIGEST naming `tools/d2-typed-labels.py`); `--profile v1 --selftest` (exit 0, 17 controls); `--profile v2 --quiet` (exit 0, 50/50, claims=15); `--profile v2 --freeze` (exit 2, no dir); `--profile v3 --quiet --baseline .scratch/o04/nope.json` (exit 2); `tools/d2-typed-labels.py --selftest` (163/163); `tools/assemble-d4-typed.py --selftest` (12/12); gate tamper copy (exit 1 HO-MISSING, fields=15/16); `tools/check-gate-battery.py --selftest` (44/44); `sha256sum` over the r6/r7 pinned files; isolated `git archive 4a7aede` freeze ×2 (packet `45f571…`, expected `bbe158…`, no diff).
- `.scratch/o04/drift_r6b.py` — r6-row classification script (57 matched / 0 drifted / 1 unresolvable).
- `reports/round-22/run-validation.py:705-706`, `reports/round-20/run-validation.py:765,1377-1379` — filed consumers of the renderer's summary/selftest lines (read-only).
- `reports/round-34/run-validation.py:176-182` — filed leg asserting the renderer defaults and the quiet packet sha (read-only).
- `reports/round-35/op/O08-validation-legs.md:53-66,138-175,206-234` — acceptance legs (sibling fragment, read-only).
