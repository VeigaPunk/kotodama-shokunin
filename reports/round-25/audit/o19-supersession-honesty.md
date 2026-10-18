# R25-O19 — adversarial review: supersession honesty

- Seat **R25-O19** (reviewer 2 of 3, supersession honesty). Round 25 (operator:
  loop 3 of 3, build 1 of 4; 64 workers on `devin/deepseek-v4-1-flash-high` —
  `reports/round-25/targets.json`).
- Date **2026-10-18**. Declared baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`;
  lane HEAD at review start `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- Assignment (verbatim): "O R25-O18..O20 (reviewers x3): adversarial pass on
  both fixes (bypass paths, supersession honesty)."
- **Write scope: this fragment only.** No `tools/**`, `examples/**`, `corpus/**`,
  `SKILL.md`, or filed round-8–24 byte is edited; no Git mutation. NON-CANON
  engineering evidence.
- **This seat authored none of the artifacts it reviews** — not
  `reports/round-25/v3-supersession/**`, not `build-revision.py`, not
  `v3-supersession-check.py`, not `reports/round-25/run-validation.py`.
- Scratch: `.scratch/r25-o18/` (`TMPDIR=$PWD/.scratch` on every scratch write).
- **Revision binding.** The artifact under review —
  `reports/round-25/v3-supersession/declared-in-r4/packet.md` — was **unchanged**
  across this review (sha
  `5f58db4a52b688568eac054b1c75e9bd110843370a1943cf4353fff75b46aa03`, re-checked
  at 17:42Z). The *runner* (`reports/round-25/run-validation.py`) moved from
  `d6e27b91…` to `4cd6f066…` mid-review; §4-§5 record both readings.

## 0. Verdict at a glance

| # | reading | verdict |
|---|---|---|
| 1 | `declared-in-r4/packet.md` exists, sha `5f58db4a…`, **exactly 5 ledger lines + 1 note** differ from the r3 parent | **holds** |
| 2 | the five D4/OQ rows now carry the family-clean values, matching the live bytes | **holds** |
| 3 | the r3 parent is unmodified and is correctly named as the superseded parent | **holds** |
| 4 | census preserved (27 rows, 16/7/4); links and uncertainty grammar intact | **holds** |
| 5 | **the renderer still emits the stale prose** — r4 is a filed *revision*, not a corrected *source* | **FAIL (structural)** |
| 6 | the counting command reported claim O as FAIL at 14:37Z, on a `D2-CL01` flag | **was FAIL; green at 14:38Z** |
| 7 | the counting command's `D2-CL01` flag was a **false positive** on correct-for-D2 numbers | **FAIL (runner-side, new) — fixed at 14:38Z** |
| 8 | the r4 note's cited `expected.json` + `v3-supersession-check.py` now exist (they did not at 14:30Z) | **resolved mid-flight** |
| 9 | the counting command now reports **O/D/C all PASS** (`acceptance_checks_passed: True`) at the final revision | **holds** |

The revision itself is a **clean, honest, byte-provable supersession of the
filed r3 packet**: the delta is exactly what it declares, the parent is
untouched, and the corrected numbers are the live ones. What does **not** hold
is the stronger reading a reader could take from the claim — that the v3
handoff's stale prose is *fixed*. The generator is untouched, so a fresh
`--profile v3` render still contains the stale sentences (§4); r4 corrects a
**filed artifact**, not the **producer**.

## 1. What was stale, and against which live surface

Measured 2026-10-18 from the delivered bytes:

| surface | live value |
|---|---|
| `examples/culture-d4/expected-holds.json#counts` | `{hold: 12, note: 0, fail: 0}` |
| `typed-labels.d4.yml#coverage.findings_total` | **12** (was 16) |
| `…#coverage.findings_hold_or_fail` | **12** (was 15) |
| `…#coverage.conflicts` | **0** (was 4) |
| `…#coverage.rank_rules_unresolved_items` | **0** (was 13) |
| `…#coverage.rank_quarantine_handles` | **0** (was 3) |

This agrees with the sibling audit `reports/round-25/audit/x48-v3-supersession.md`
R25-X48-1 independently.

## 2. The revision's declared delta — verified exactly

`build-revision.py --check` → `EQUAL`, sha `5f58db4a…` filed = rebuilt, 109,817
bytes. An independent `diff` against the r3 parent shows **6 changed regions and
nothing else**:

| line (r3 → r4) | change |
|---|---|
| — → 9 (new) | the `declared-in-r4` provenance note |
| 150 → 151 | D4-CL05 row |
| 151 → 152 | D4-CL06 row |
| 152 → 153 | D4-CL07 row |
| 154 → 155 | D4-CL09 row |
| 309 → 310 | OQ-V3-05 line |

The parent `reports/round-23/wording/declared-in-r3/packet.md` is **byte-identical
to its filed digest** `084dc5db9a8d923b…` (the runner's `parent_binding` control
re-measures this and agrees). No claim status, link, edge, or glossary row moved:
census stays 27 rows / 16 supported / 7 partial / 4 unresolved.

The corrected numbers in the five rows are the live ones from §1 — checked
token by token, not taken on trust.

## 3. What the revision does NOT do — the renderer is untouched

`tools/exercise-handoff-e2e.py:184` still reads the **immutable round-20**
claim map:

```python
CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"
```

`v3_parse_claims_map()` re-reads that file on every build, and
`v3_build_packet()` renders the D4 rows from it verbatim. Therefore a **fresh**
v3 render reproduces the stale prose:

```
$ export TMPDIR=$PWD/.scratch
$ python3 tools/exercise-handoff-e2e.py --profile v3 --freeze "$PWD/.scratch/r25-o18/frz2"
$ grep -c "findings_total 16\|hold 15, note 1\|three rank holds" …/frz2/packet.md
4
```

The generator's output is still `a97a0f0a0a497cb4…` — byte-identical to the
filed `declared-in-r2` packet — so the newly rendered packet carries D4-CL05/06/
09 and OQ-V3-05 in their pre-family-clean wording.

There is **no corrected claim map anywhere under `reports/round-25/`** (the only
`*claim*` path there is `claims.json`, the round declaration). So the r4 revision
is a **terminal artifact**: it is not wired to the renderer, and the renderer
cannot reproduce it.

**Consequence.** The r4 revision is honest about *what it is* (a claim-prose
revision of a filed packet, explicitly "not a renderer build"), and its own note
says so. But the round's claim (b) asks that "v3 claims prose [be] corrected to
the family-clean present state **and re-pinned as a new revision**". Only the
second half is delivered as a *producible* thing: the next `--profile v3` run
regenerates the stale bytes. A reader must not conclude the v3 handoff now
carries correct prose in general — only that one filed revision does.

## 4. The counting command reported claim O as FAIL at 14:37Z

Run in an isolated clone with the then-current bytes
(`reports/round-25/run-validation.py` sha `d6e27b91…`), `TMPDIR` under the clone:

```
claim O: FAIL
claim D: PASS
claim C: PASS
acceptance_checks_passed: False
```

Claim O's failure list:

```
v3-supersession: D2-CL01 carries undispositioned passenger prose (15 hold-or-fail)
```

Notably the **D4 rows passed even then**: the runner's per-row `claim_rows` block
reports `states_family_clean_value: true` and
`undispositioned_stale_sentences: []` for D4-CL05/06/07/09, and
`oq_v3_05.disposition_marked: true`. The revision cleared the D4 half of the
claim and was caught only on a D2 row.

**At the final revision** (runner sha `4cd6f066…`, 14:38Z) the same run is green:
`claim O: PASS`, `acceptance_checks_passed: True`. §5 records what changed.

## 5. The `D2-CL01` flag was a false positive (runner-side defect, since fixed)

`STALE_PASSENGER_TOKENS` (`reports/round-25/run-validation.py:99-105`) includes
the D4-specific tokens `"16 findings"` and `"15 hold-or-fail"`. `D2-CL01`'s row
legitimately says "findings_total 16 with 15 hold-or-fail" — which are **D2's own
live values**:

```
examples/culture-d2/typed-labels.d2.yml#coverage.findings_total       = 16
examples/culture-d2/typed-labels.d2.yml#coverage.findings_hold_or_fail = 15
```

The token set was applied to **every** claim row, so a D2 row asserting D2's
correct numbers was flagged as "stale D4 passenger prose". The `watched` D4 rows
are exempted by id; the blanket loop was not family-scoped.

**Fixed at 14:38Z** — the loop now carries the family guard, with a comment that
matches this finding:

```python
for claim_id, row in rows.items():
    if claim_id in watched:
        continue
    if not claim_id.startswith("D4-"):
        continue  # the stale-passenger prose is a D4-ownership question; D2's own
        #           live bytes legitimately carry 16 findings / 15 hold-or-fail
```

Verified by re-running the counting command at the final revision (§4). Recorded
because the flag held claim O red for a reason that was not a defect in the
supersession, and because the token pair cannot distinguish D2's correct numbers
from D4's stale ones — a genuine D2-CL01 staleness of that shape would have been
invisible too.

This is the same class of defect the round is fixing: a detector that fires on
correct evidence. It was **runner-side and new this round** (the round-25
validator is the round's own artifact, not a filed one). The applied repair was
the family guard above.

Severity: **medium while live** — it did not corrupt an artifact, but it held
claim O red for a reason that was not a defect in the supersession, and it would
have masked a genuine D2-CL01 staleness of that shape.

## 6. Timing findings (since resolved)

- At **14:30Z** the r4 note cited `reports/round-25/v3-supersession/declared-in-r4/expected.json`
  and `v3-supersession-check.py`, and **neither existed**. Both are present at
  the current revision, so the note is no longer ahead of its own artifacts.
  Recorded because a reader sampling at 14:30Z would have seen a note promising
  a checker that was not on disk — the failure mode is real even though the
  window closed.
- At **14:31–14:35Z** the counting command's `find_v3_successor()` required
  `twin.json` alongside `packet.md` + `expected.json`, and r4 ships no twin; the
  command then reported "no superseding v3 row landed". The runner was revised
  at **14:37Z** to accept a `packet.md` + `expected.json` row, and it now finds
  `reports/round-25/v3-supersession/declared-in-r4`. Recorded because the
  requirement was never satisfiable by this seat's artifact shape and would have
  been a hard red on a correct deliverable.

## 7. What this review does NOT establish

- It does not certify the D4 numbers in the r4 rows beyond the token-level
  re-read in §2; the sibling audit `x48` carries the full census.
- It does not audit the argot leg (R25-O20's surface).
- It did not run the round-23 successor validator end-to-end (it needs an
  isolated clone and rewrites receipts); the r4 note's claim that
  `v3-supersession-check.py` re-verifies the bytes is therefore taken as
  **reported, not reproduced** here. The `build-revision.py --check` byte
  equality in §2 is this seat's own.

## 8. Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
# 1. the revision's delta is exactly as declared
python3 reports/round-25/v3-supersession/build-revision.py --check      # EQUAL
diff reports/round-23/wording/declared-in-r3/packet.md \
     reports/round-25/v3-supersession/declared-in-r4/packet.md          # 6 regions
# 2. the renderer is untouched and still emits the stale prose
python3 tools/exercise-handoff-e2e.py --profile v3 --freeze "$PWD/.scratch/frz"
grep -c "findings_total 16\|hold 15, note 1\|three rank holds" "$PWD/.scratch/frz/packet.md"
# 3. the counting command's verdict, in an isolated clone
python3 reports/round-25/run-validation.py                              # O/D/C PASS
```

Assertions: step 1 prints `EQUAL` and a 6-region diff; step 2 prints a non-zero
count; step 3 prints `acceptance_checks_passed: True`. At 14:37Z step 3 printed
`claim O: FAIL` with the `D2-CL01` message (§5) — the difference between the two
runs is the runner revision, not the artifact.
