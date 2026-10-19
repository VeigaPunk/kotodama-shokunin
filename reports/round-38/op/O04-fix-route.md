- Seat: O04 | executor | claim O | date 2026-10-19 | baseline 9bccc9b

# O04 — fix route: how the next re-freeze absorbs `13-register-law.yml`

**Verdict.** The read-set roster defect (`R36-R7-READSET-13`) cannot be fixed by a
read-set edit alone: adding the member makes the *filed* r7 row stale and the
default chain red. The fix route is a **paired move** — read-set add **plus** a
new baseline row with the two default constants re-pointed — landed by the next
re-freeze. Measured in three isolated `git archive` copies of `9bccc9b`; **zero
filed bytes moved, no in-tree round-runner executed, no re-freeze of
`declared-in-r7`.**

## 1. The defect, mechanically

- `tools/exercise-handoff-e2e.py:157-170` — `D4_COMPONENTS` lists **12** paths.
  `:1939-1965` splices that tuple into `V3_READ_SET`, so the live read set has
  **58** members and omits `examples/culture-d4/components/13-register-law.yml`
  (live sha256 `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`).
- The packet's **component** manifest (`examples/culture-d4/packet.d4.yml:2888`)
  and its **source** manifest (`:2914`) both carry all **13** authored components;
  `examples/culture-d4/ASSEMBLY.md:12-24` and the renderer inventory comment
  (`tools/exercise-handoff-e2e.py:51-59`) still say "twelve" / "58 files".
- The packet's **artifact_manifest** is *not* the mismatched surface: it holds
  exactly 58 rows (`A-01`…`A-58`), because `assert_manifest_equality`
  (`:3646-3662`) hard-requires `checked == len(V3_READ_SET)`. The disagreement is
  **component manifest (13) vs read set (58 members, 12 of them D4 components)**.
  O01's guard must compare *that* pair, not the artifact manifest against the read
  set — the latter is read-set-derived and trivially in sync.

## 2. Measured cascade (isolated archives, `TMPDIR=$PWD/.scratch`)

Three variants, each a fresh `git archive HEAD` of `9bccc9b`:

| variant | edit | packet sha256 | twin sha256 | inputs | A-NN renumbered | default chain |
|---|---|---|---|---|---|---|
| A | member spliced **into `D4_COMPONENTS`** (position 13) | `7f0e47909a77ad7f2d82507e8d64b6476a0152e3177d3c45e9d3ef36ba9468ff` | `9ad1f6db80731529167dce31f00afe6cdfc837cd06641c07eb79502be94d2bdc` | 59 | **13** (`A-46`…`A-58` shift +1) | n/a (baseline not re-pointed) |
| B | member **appended at the tail** (position 59) | `7ca92109e390d8e73c36156893bab451ec95b343be2e6ce825adcd504d2b8f64` | `90b7f5f2f868db1549e09968b77dfda7d7028115cc30b2493d427fe9cda6cefb` | 59 | **0** | n/a |
| **C (recommended)** | A **plus** `V3_BASELINE_DEFAULT`/`V3_FROZEN_DIR_DEFAULT` → `reports/round-39/handoff/declared-in-r8`, `CLAIMS_MAP` **untouched** | `b102aa708a23d3ba7010af3056259989c7b130f213364d3a77c624b1b21aa6e2` | `9ad1f6db80731529167dce31f00afe6cdfc837cd06641c07eb79502be94d2bdc` | 59 | 13 | **exit 0** |

Key measurements:

- **The read-set edit alone breaks the filed r7 row.** With the member added and
  the constants left at r7, `python3 -B tools/exercise-handoff-e2e.py --profile v3
  --quiet` → **exit 1**, `handoff-v3: E2E-DIGEST: the assembled packet does not
  match the frozen packet digest`. The r7 `expected.json` pins the pre-fix packet
  digest `45f57132…`, so a read-set-only fix is a **red** default chain.
- **Ordering is a free frontier move, not a coin flip.** Variant A renumbers
  `A-46`→`A-47` … `A-58`→`A-59` (13 rows) and leaves `A-57` pointing at a
  claims-map path; Variant B adds `A-59` with **zero renumbering** and no
  path/row drift for any existing id. A *narrower* diff at equal functional
  coverage. A is measured for completeness; **B is the cheaper insert**.
- **The twin is id-mapping-only.** Variants A and C produce the identical twin
  sha (`9ad1f6db…`) although their packet sha differs (`7f0e4790…` vs
  `b102aa70…`): the twin's `artifact_manifest` carries `{path, artifact_id,
  sha256}` (`:3608`, `:2633-2645`) and the `A-NN` mapping is the same in both.
  So the twin digest is sensitive to the *insertion point*, not to `CLAIMS_MAP`.
- **The renderer selftest survives the paired move.** `python3 -B
  tools/exercise-handoff-e2e.py --profile v3 --selftest` → exit **0** both on the
  unpatched tree and on variant C (the added member and the moved default ride
  through the whole control matrix, which builds its fixture from the live read
  set, `:4165-4168`). No new selftest control is owed for the member add itself —
  the guard O01 lands is what needs the fixtures.
- **`CLAIMS_MAP` must not move in the same step as the read-set add.** Re-pointing
  it in the same edit (variant C + `CLAIMS_MAP` → the r8 dir) removes the r7
  member `reports/round-34/handoff/declared-in-r7/claims-map.md` from the live
  read set and the r7 row is then refused by the *existing* roster guard with
  `E2E-READSET: … claims-map.md — the baseline row is superseded` (`:3823-3836`),
  not by `E2E-DIGEST`. Either refusal is correct; keeping `CLAIMS_MAP` at r7
  keeps the change to the one file it is about.

## 3. `expected.json` diff (variant C vs the filed r7 row)

```
CHANGED .baseline_digest                          1fce3820148430dc… -> 116cf7da63a259ab… (B) / e4e6d370f1307ed4… (A)
CHANGED .field_digests.artifact_manifest          7220047dcb1ab2f3… -> 77345d5f9efa1be8… (B) / eb728d1c10a08056… (A)
CHANGED .field_digests.validation                 d34fa62ffee1f291… -> 2f97a07f42d0beac…
ADDED   .inputs.examples/culture-d4/components/13-register-law.yml
                                                  c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7
CHANGED .packet_sha256                            45f5713261762a95… -> 7ca92109e390d8e7… (B) / b102aa708a23d3ba… (C)
CHANGED .twin_sha256                              0e22913850cd85bc… -> 90b7f5f2f868db15… (B) / 9ad1f6db80731529… (C)
inputs count                                      58 -> 59
```

Every other key is unchanged: `claim_ids`, `glossary_entry_ids`, `v2_subset_digest`
(`ad35c860acf3b452…`), `alias_state` (`landed`), `counts`, `links` (105/105),
`uncertainty` (27 / 16-7-4), `cross_refs` component digests **26/26**, d4 pins
**8/8**. `counts.d4_*` are mined from the packet's own sections, not the read set.

## 4. The edit list (exact, for the landing seat)

| # | surface | line | before → after |
|---|---|---|---|
| 1 | `tools/exercise-handoff-e2e.py` | `1939-1965` | `V3_READ_SET` gains `"examples/culture-d4/components/13-register-law.yml"` (variant B: appended after `"reports/round-19/validation.json"`) |
| 2 | `tools/exercise-handoff-e2e.py` | `1937` | `V3_BASELINE_DEFAULT` → `<new-row>/expected.json` |
| 3 | `tools/exercise-handoff-e2e.py` | `1938` | `V3_FROZEN_DIR_DEFAULT` → `<new-row>` |
| 4 | `tools/exercise-handoff-e2e.py` | `52,59` | inventory prose: `the twelve D4 components` → `thirteen`; `— 58 files.` → `— 59 files.` (docstring only, no digest impact; variant B changes the count alone, not the A-NN map) |
| 5 | `tools/exercise-handoff-e2e.py` | `2783` | **already correct** — `thirteen authored components` (the r34 landing at `reports/round-34/handoff/repin.json:32-38` fixed this cell; `grep -n "authored components"` → one hit, `2783`, already 13). No edit owed |
| 6 | new dir | `<new-row>/` | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze <new-row>`, twice (the second run's `freeze.txt` must read `no tracked value changed since the previous freeze`) |
| — | `CLAIMS_MAP` (`:184`) | — | **unchanged** this step (see §2) |
| — | `reports/round-34/handoff/declared-in-r7/**` | — | **0 bytes moved** |

**Sequencing (binding):** edit 1 must land in the same step as edits 2–3 and 6,
otherwise the default chain is red between them. Land **after** the D claim's
register artifacts are stable — a re-freeze taken mid-wave is stale the moment
the register law lands (`reports/round-27/pinsweep/repin.py` docstring states the
same rule).

## 5. `repin.json`-style row (draft — `schema: kotodama-pin-repoint-v1`)

```json
{
 "schema": "kotodama-pin-repoint-v1",
 "round": 39, "date": "2026-10-19", "axis": "operability",
 "baseline_commit": "<head-at-landing>",
 "kind": "re-point as a NEW row; the filed r2..r7 rows stay byte-identical",
 "canon": "NON-CANON engineering evidence; a pin is integrity, never truth and never clearance",
 "closes": "R36-R7-READSET-13",
 "rows": [
  {"id": "R39-O-default-pointer",
   "surface": "tools/exercise-handoff-e2e.py:1937-1938",
   "was": "reports/round-34/handoff/declared-in-r7/{expected.json,}",
   "now": "reports/round-39/handoff/declared-in-r8/{expected.json,}",
   "control": {"command": "python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet",
               "exit": 0, "packet_sha256": "b102aa708a23d3ba7010af3056259989c7b130f213364d3a77c624b1b21aa6e2",
               "reading": "fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4"}},
  {"id": "R39-O-readset-member",
   "surface": "tools/exercise-handoff-e2e.py:1939-1965 (V3_READ_SET)",
   "was": "58 members; examples/culture-d4/components/13-register-law.yml absent",
   "now": "59 members; member present, pinned at c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7",
   "insertion": "appended at the tail (position 59) — zero A-NN renumbering; the D4_COMPONENTS splice would renumber A-46..A-58 (measured)",
   "cascade_measured": {"A-46..A-58": "unchanged under tail insert; +1 under the D4_COMPONENTS splice"},
   "control": {"command": "python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-39/handoff/declared-in-r8",
               "exit": 0, "reading": "read set: 59 files; component digests 26/26; d4 pins 8/8"}},
  {"id": "R39-O-filed-r7-row",
   "surface": "reports/round-34/handoff/declared-in-r7/**",
   "surface_sha256": {"expected.json": "bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55",
                      "packet.md": "45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19",
                      "twin.json": "0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599",
                      "claims-map.md": "d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c"},
   "reading": "reading changed, verdict unchanged — the r7 row is superseded, never rewritten",
   "control": {"command": "python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-34/handoff/declared-in-r7/expected.json",
               "exit_before_fix": 0, "exit_after_fix": 1,
               "code": "E2E-DIGEST: the assembled packet does not match the frozen packet digest",
               "note": "the refusal is the control: a read-set-only edit leaves the default chain red, which is why the fix is a paired move"}},
  {"id": "R39-O-preservation",
   "surface": "reports/round-1..38/**, corpus/lessons/*.md, tools/gates/frozen/**",
   "observed": "0 modified rows; no re-freeze of reports/round-34/handoff/declared-in-r7",
   "precedent": "reports/round-34/handoff/repin.json (R34-D-history) and reports/round-29/defects/regression.md:52 — earlier baselines are named superseded, never rewritten"}
 ],
 "named_findings": [
  {"id": "R39-O-N1",
   "finding": "the packet's artifact_manifest is read-set-derived, so the guard must compare the packet's COMPONENT manifest (13) against the read set, not the artifact manifest against the read set",
   "owner": "O01 guard design (this round)", "state": "routed"},
  {"id": "R39-O-N2",
   "finding": "V3_READ_SET carries no assertion tying its length to the D4 component count; the renderer inventory prose and the tuple can drift apart silently, as they did here",
   "owner": "O01 guard design / renderer selftest", "state": "routed"}
 ],
 "limits": "pins the cascade surfaces only; not canon, not lore acceptance, not round admission"
}
```

## 6. Why a successor row and not an in-place re-freeze

`reports/round-34/handoff/declared-in-r7/**` is a filed round's bytes, and the
lane's standing rule is that earlier baselines are named superseded, never
rewritten (`reports/round-34/handoff/repin.json` R34-D-history;
`reports/round-29/defects/regression.md:52`). The predecessor row's read-set
membership is *also* what makes it replayable today: replaying it against the
live tree pre-fix exits **0** (`packet_sha256=45f57132…`), and post-fix exits
**1** by digest. Both readings are honest; the row itself must not change.

## Owed

- **Dependency (blocking the actual freeze):** the new row cannot be frozen until
  the D claim's register artifacts (`examples/culture-d4/packet.d4.yml` and
  dependents) are final, since a mid-wave freeze is stale on landing
  (`reports/round-27/pinsweep/repin.py` docstring). Owed to the integrator: run
  §4 edits 1–6 in one step after D lands, then file the §5 row.
- **Owed (handoff):** O05's verification of this route — re-measure §2's table
  against the renderer's freeze mechanics independently; the three variants'
  digests above are one seat's readings, not two.
- **Owed (cross-claim):** `R39-O-N1` is an input to O01's guard; if O01's guard
  compares artifact-manifest vs read set it will be vacuous (the two are
  read-set-derived and always equal). Flagged to R02/R03.
- **Not owed / out of scope:** no `CLAIMS_MAP` move, no re-freeze this round, no
  freshness axis-move, no filed-byte rewrite.

## Citations

- `tools/exercise-handoff-e2e.py:33,51-59,157-170,184,1937-1938,1939-1965,2045-2056,2208-2222,2294,2570,2588,2633-2645,2703,2779,2885,2938,3608,3646-3662,3811-3841,3997-4135`
- `examples/culture-d4/packet.d4.yml:2888,2914`; `examples/culture-d4/packet.d4.typed.yml:2891,3203`; `examples/culture-d4/ASSEMBLY.md:12-24`
- `reports/round-34/handoff/declared-in-r7/{expected.json,packet.md,twin.json,freeze.txt,claims-map.md}`; `reports/round-34/handoff/repin.json:31-38,49-52`
- `reports/round-37/adj/A01-freeze-adjudication.md:5,19,26-35`; `reports/round-37/op/defect-queue.json` (`R36-R7-READSET-13`); `reports/round-37/op/O01-queue-draft.md:305`
- `reports/round-27/pinsweep/repin.py:1-24`; `reports/round-28/sweep/repin-rows.json`; `reports/round-29/defects/regression.md:45-58`; `reports/round-34/depth/D10-repin-drafts.md:95-140`
- Commands (all in isolated `git archive` copies of `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`, `TMPDIR=$PWD/.scratch`):
  - `.scratch/o04/base2` (unpatched): `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit **0**, `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`
  - `.scratch/o04/base2`: `… --profile v3 --quiet --baseline reports/round-34/handoff/declared-in-r7/expected.json` → exit **0**
  - `.scratch/o04/base` (variant A): `… --profile v3 --quiet` → exit **1**, `E2E-DIGEST: the assembled packet does not match the frozen packet digest`
  - `.scratch/o04/base` (variant A): `… --profile v3 --freeze .scratch/o04/refreeze2` → exit 0, `read set: 59 files; component digests 26/26; d4 pins 8/8`, `re-frozen packet_sha256: 45f57132… -> 7f0e4790…`, `re-frozen input …13-register-law.yml: None… -> c0d77181ac56…`
  - `.scratch/o04/v2` (variant B): `… --freeze .scratch/o04/refreeze-v2` → exit 0, packet `7ca92109e390d8e73c36156893bab451ec95b343be2e6ce825adcd504d2b8f64`; `… --quiet --baseline …declared-in-r7/expected.json` → exit **1** `E2E-DIGEST`
  - `.scratch/o04/vC` (variant C): `… --freeze reports/round-39/handoff/declared-in-r8` → exit 0, packet `b102aa708a23d3ba7010af3056259989c7b130f213364d3a77c624b1b21aa6e2`, twin `9ad1f6db80731529167dce31f00afe6cdfc837cd06641c07eb79502be94d2bdc`; `… --quiet` → exit **0**; `… --quiet --baseline …declared-in-r7/expected.json` → exit **1** `E2E-DIGEST`
  - `.scratch/o04/base2`: `… --profile v3 --selftest` → exit **0** (unchanged baseline; the member add is not expected to need a new control)
  - `.scratch/o04/vC` (variant C, read-set add + re-point): `… --profile v3 --selftest` → exit **0** (the whole control matrix still green with the added member and the moved default; 59-file fixture)
  - `git rev-parse HEAD` → `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`; `git status --short` → only `?? reports/round-38/`
  - `sha256sum` (filed bytes, unmoved): `tools/exercise-handoff-e2e.py` `bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9`; r7 `expected.json` `bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55`; r7 `packet.md` `45f57132…`; r7 `twin.json` `0e229138…`; r7 `claims-map.md` `d181de28…`; `examples/culture-d4/components/13-register-law.yml` `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`
