# R10-O05 — findings fixer: tracker idx 3 (R9-F2) and idx 11 (R8-S13)

- seat: R10-O05 (findings fixer, claim O), round 10 (loop 1 of 3, build round 3 of 4), 2026-10-17
- assignment (verbatim): "FINDINGS R10-O05 (fixer): tracker indices 3 and 11. reports/round-10/fix-05.md."
- tracker read: `reports/round-10/findings-tracker.json` (R10-O01, `compiled_at_utc` 2026-10-17T21:27Z; 24 rows; **0-based** `idx` 0–23; tracker sha256 `3bfd40181ca98c83…` at my read, 21:33Z). Rows taken: **idx 3** = `reports/round-9/d3/findings-10.md` §2 **F2** (acceptance-affecting) and **idx 11** = `reports/round-8/depth/findings.md` §S13 (low).
- write scope: this file, plus the two tracker rows it dispositions (the target instructs fixers to "update the tracker row"; update receipt in §4). No other byte in the repo was written by this seat.
- live tree at measurement: HEAD `e3a1ec9435787328ac9f828f96cb6390e4916b8f`; `git diff --stat 9dc18ec HEAD` = only `reports/round-10/{claims,targets,availability-attempt-1..3}` (5 files, 127 insertions) — no artifact bytes differ from the declared round-10 baseline `9dc18ec…` at the time of these measurements. Scratch: `.scratch/o05/` (`TMPDIR=$PWD/.scratch` exported; `/tmp` not used).
- canon: NON-CANON engineering evidence. No filed report byte was rewritten — per the round's standard, corrections are new entries (this file).
- method note: every claim below was re-measured by this seat on the live tree; nothing is quoted from a fragment without naming its location.

## 0. Rows taken

| idx | source | finding | severity | disposition |
|---|---|---|---|---|
| 3 | `reports/round-9/d3/findings-10.md` §2 F2 (lines 132-169) | the D3 frozen pin is red on this tree (3 × `D3-SNAPSHOT`) | acceptance-affecting | **fixed-with-control** |
| 11 | `reports/round-8/depth/findings.md` §S13 (lines 98-102) | pinned digests and line locators invalidated by concurrent edits | low | **fixed-with-control** (correction-as-new-entry; sub-item (c) not-a-defect) |

---

## 1. idx 3 — R9-F2: D3 frozen pin red → fixed-with-control

### 1.1 The red, as filed (source close, round 9)

`reports/round-9/d3/findings-10.md` §2 F2 (re-run 20:52:10Z): `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` → exit 2, exactly 3 × `D3-SNAPSHOT` (contract `50c4c2f2…`; costume gate `29a9361c…`; naming gate `8c5afb0a…`), with the circularity warning: never regenerate the manifest from live bytes; re-acknowledge per input citing the causing commit. `reports/round-9/d3/findings.md` §2 S1 supplies the minimum record a legitimate re-pin must carry.

### 1.2 State now (2026-10-17, ~21:30Z)

```sh
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
        --frozen examples/culture-d3/expected.json          # exit 0
# stdout (sha256 e282a0688498034144fb…):
# {"counts": {"total": 0}, "exit": 0, "findings": [], "profile": "kotodama-d3-evidence-coupling/1"}
python3 -c "import hashlib,json;m=json.load(open('examples/culture-d3/expected.json'))['manifest'];\
print(len(m), [k for k,v in m.items() if hashlib.sha256(open(k,'rb').read()).hexdigest()!=v])"
# 24 []          ← independent manifest sweep, no guard code; 0 mismatches
```

The pin was re-acknowledged by the orchestrator at the round-9 admit commit `9dc18ec` ("D3 pins refreshed" in `LOG.md`, round-9 entry).

### 1.3 Demonstrated control — the re-pin carries the record R9-D09 §2 S1 prescribed

1. **Pre-refresh token of the freeze itself**: `74496aa8aa7db2d7…` (git blob `c420ac4c…`) — recorded at `reports/round-9/d3/evidence-coupling.md:16` and `reports/round-9/baselines/handoff-packet-check/packet.md:65`; matches `reports/round-9/d3/findings.md` §1.
2. **Three keys, old → new, with the causing commit and the change**: `reports/round-9/d3/check-diagnosis.md:73-75` —

   | path | declared (old) | actual (new) | causing commit | change |
   |---|---|---|---|---|
   | `corpus/knowledge/synthesis/worldbible-integration-contract.md` | `50c4c2f2…` | `5f4c02bf…` | `e1694ba` | round-8 metadata pass (header fields only) |
   | `tools/gates/costume-era-consistency-gate.py` | `29a9361c…` | `e6bffd70…` | `e1694ba` | round-8 O-shard parser hardening |
   | `tools/gates/naming-collision-gate.py` | `8c5afb0a…` | `d9e4e8f4…` | `e1694ba` | round-8 O-shard parser hardening |

3. **Verdict preservation over the D3 projection — re-run independently by this seat** (not quoted): round-7 gate bytes extracted with `git show 57c3ce6:<path>` hash exactly to the pre-refresh pins (`29a9361c…` / `8c5afb0a…`); both old and current gates run on `examples/culture-d3/packet.gates.yml`:

   ```sh
   python3 .scratch/o05/costume-r7.py examples/culture-d3/packet.gates.yml  # exit 1
   python3 tools/gates/costume-era-consistency-gate.py …                   # exit 1, cmp byte-identical (sha256 40d4048c326e10373b84…)
   python3 .scratch/o05/naming-r7.py examples/culture-d3/packet.gates.yml   # exit 1
   python3 tools/gates/naming-collision-gate.py …                           # exit 1, cmp byte-identical (sha256 506d163231051f294b22…)
   ```

   The round-8 repairs are behavior-neutral on this artifact; the re-pin hides no verdict change. (These raw-pipe hashes match the convention note in `reports/round-9/d3/findings.md` §6.)
4. **`expected_exit` / `finding_ids` unchanged**: `git show 57c3ce6:examples/culture-d3/expected.json` → `expected_exit 0`, `finding_ids []`; current file → `expected_exit 0`, `finding_ids []` (both read 2026-10-17).
5. **Stamped revision + date**: commit `9dc18ec`, `LOG.md` round-9 entry, and the acceptance runner's own receipt (`reports/round-9/validation.json` `input_sha256` carries the post-refresh freeze token `562b76cb48f14bdb…`; claims D `passed: true` — re-run by the acceptance runner, a different seat than the re-pin act).

The circularity the review existed to catch (a manifest regenerated from live bytes to bless a tamper) did **not** occur: the manifest values correspond to documented legitimate changes, and the frozen re-run was performed by a different artifact than the re-pinner's hand.

### 1.4 Residual recorded (new observation — not in any filed finding)

The landed re-pin is **not** the minimal three-line edit the round-9 recommendation described ("the diff of the freeze shown to be exactly the three digest lines", `reports/round-9/d3/findings.md` §2 S1):

```sh
git diff 57c3ce6 HEAD -- examples/culture-d3/expected.json
# 3 digest values changed (table above) PLUS a re-serialization:
#   indent 2 spaces → 1 space per level; trailing newline dropped; 34 → 33 lines
```

Semantically identical (verified: `expected_exit`/`finding_ids` unchanged; 24-entry manifest with 0 mismatches; frozen run exit 0), so no control breaks — but any acceptance ledger or future re-pin record must not claim "the diff is exactly the three digest lines" without this caveat. Owner: orchestrator (the re-pin act); recorded here because filed bytes are not rewritten.

---

## 2. idx 11 — R8-S13: pinned digests and line locators invalidated → fixed-with-control

The finding has three parts; measured state of each:

### 2.1 (a) The two pins — resolution route now recorded

As filed: `design-spec.md` §9 pins `era-language-staging.md` `226e1104…` and `loanword-material-dating.md` `bb08d458…`, "both are exactly the HEAD bytes … while the worktree now holds `621b7a33…` / `5b1d75ab…`".

Measured now (2026-10-17): the worktree values were subsequently **committed** at the round-8 admit `e1694ba`, so the worktree and HEAD both hold `621b7a33c06ff15f…` / `5b1d75abd29422b1…`; the pinned values resolve at revision **`291c714144f239db9d4efe14627b6cf07e5cffb8`**:

```sh
git show 291c714:corpus/knowledge/synthesis/era-language-staging.md | sha256sum   # 226e11049b7361d8… == the pin
git show 291c714:corpus/knowledge/synthesis/loanword-material-dating.md | sha256sum # bb08d4585033d856… == the pin
git rev-list HEAD -- corpus/knowledge/synthesis/era-language-staging.md | head -1   # e1694ba (current bytes)
```

The design-spec ledger is honest about its scope ("sha256 read with `sha256sum` on 2026-10-17 (working tree, pre-integration)", `reports/round-8/depth/design-spec.md` §9) — the values are revision-scoped by declaration, and the missing piece was a resolution route. The fix is this new entry (filed bytes not rewritten): the pinned values resolve at `291c714` by command, the current values are `621b7a33…`/`5b1d75ab…` at HEAD, and the standing rule for re-runners is to resolve any pinned digest via `git show <rev>:<path> | sha256sum`.

**Demonstrated control**: the three commands above (resolution exact-match + current-value identity), re-runnable as-is.

### 2.2 (b) D14's line locators — the reviewer's own correction is confirmed

S13b corrected the reviewer's earlier reading: D14's locators are correct against the bytes D14 measured. Verified independently against revision `291c714` (the revision the pins resolve at) and against HEAD:

| locator | at `291c714` | at HEAD / worktree |
|---|---|---|
| "Separate **ultimate etymon** from **immediate donor** and **carrier**" | line **44** (as S13b states) | line 47 |
| "Recipient form reflects a donor innovation" | line **54** (as S13b states) | line 57 |

The +3 shift is exactly the metadata sweep: `git diff --stat 291c714 e1694ba -- corpus/knowledge/synthesis/loanword-material-dating.md` → 3 insertions (`- source:`, `- verified-at:`, `- recheck:`). No defect in D14; the correction stands.

### 2.3 (c) The churn record — not-a-defect

The sub-item is a churn record, not a finding against any reviewed revision (`reports/round-8/depth/findings.md` §S13c says so itself). Current `sha256sum examples/culture-d2/components/11-costumes.yml` → `b6e2c5c29cc5d689…`, matching the "bytes were" side of the record (the intermediate revision `1756e8c0` misreported `bd7eeb08…`; fixed by `623b5b1f`). Disposition: **not-a-defect** (recorded, not actionable).

### 2.4 No live consumer of the stale-looking values (sweep)

`grep -rn "226e1104\|bb08d458"` (2026-10-17) outside `.scratch/` and the filed `design-spec.md`/`findings*.md`/tracker/drift-shard carriers lands on exactly one live-input file: `examples/supplement-opencode-1/sound-change-vs-taboo.json:8-11`, which carries `bb08d458…` as `secondary_entries_sha256_before` — an explicitly labeled historical baseline ("baseline hashes are recorded below"; `entry_scope_note` names the resolution method `git show <rev>:<path> | sha256sum`). The live checker does not consume it: `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` → exit 0 ("OK all checks passed (audits=7, mech_cases=11, derivations=9, approx_checks_runner=37)"), and the field name occurs 0 times in `tools/check-craft-exercise.py`. So the S13 values are historical annotations, never live pins — the residual risk is documentation-only.

---

## 3. Adjacent measurement (not this seat's rows — recorded for the owning fixer)

While enumerating the tracker I ran the differential control for **idx 4** (R8-S6, "a supplied `native_form` is still not read"), in case the owning seat can reuse it. It is **not** dispositioned here. On a mirror packet (`.scratch/o05/packet-native-inject.d2.yml`, GAR-01 with `native_form: "vinter"` injected; sha256 `2a79a893d7c0be3e…`), `python3 tools/d2-typed-labels.py --packet <mirror> --json` vs the live-packet run: a full JSON walk finds **exactly one** difference — the echoed `packet` path string; every finding, stat and label block is identical (base `880d0e45…` vs mirror `8cfa555b…`, the delta being the path echo). The injected supplied form is not read at tool revision `0da0015f700345c9…`. Also: `grep -rn "native_form" examples/culture-d2/` → **0 occurrences** (the channel does not exist in the corpus). Scratch artifacts remain under `.scratch/o05/`.

---

## 4. Tracker update receipt

Rows idx 3 and 11 updated in `reports/round-10/findings-tracker.json` (single read-modify-write, atomic `os.replace`; all 22 other rows byte-preserved — verified by comparing the pre/post JSON of the untouched rows):

- idx 3: `disposition: "fixed-with-control"`, `control: "reports/round-10/fix-05.md"`, `control_command: "python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json → exit 0, findings [] (sha256 e282a0688498034144fb…); independent manifest sweep 24/24 match"`, `note` names the re-serialization residual (§1.4), `verified_at`/`verified_by` stamped.
- idx 11: `disposition: "fixed-with-control"`, `control: "reports/round-10/fix-05.md"`, `control_command: "git show 291c714:corpus/knowledge/synthesis/era-language-staging.md | sha256sum → 226e1104… (pin exact-match); current HEAD bytes 621b7a33…; locators :44/:54 at 291c714 confirmed"`, `note` records the (c) not-a-defect sub-item and the no-live-consumer sweep, `verified_at`/`verified_by` stamped.

Both labels match the harness vocabulary (`reports/round-10/run-validation.py:104-108`: `FIXED_LABELS` ⊃ "fixed"; evidence fields satisfy the `python3 |exit|sha256` text rule at :764-779).

### 4.1 Concurrency disclosure (tracker was rewritten by other seats during this round)

The tracker is a shared row surface and several fixer seats hold read-modify-write cycles on it; observed sequence (all 2026-10-17, local): original `3bfd40181ca98c83…` (19,091 B, indent-2, logical key order — preserved at `.scratch/fix07/tree/…`) → my write `d0136d1deb6a66d2…` (26,038 B) → a peer rewrite `2cbb08c62c648571…` (29,323 B) → a further rewrite `43338715b4dc82f0…` (28,816 B) at my close. Two disclosures:

- **My write used `indent=1`** while the original file was indent-2 (a formatting deviation of the same class as the D3 re-pin residual in §1.4 — flagged rather than hidden; the file has since been rewritten by other seats with different formatting, so no single seat's style now holds).
- **My rows survived every subsequent rewrite**: in the latest revision I read (sha256 `43338715b4dc82f0…`, 24 rows, all rows carrying the five harness-required fields), idx 3 and idx 11 both read `disposition: "fixed-with-control"`, `control: "reports/round-10/fix-05.md"`, with this seat's `control_command`/`note`/`verified_by` fields intact. A harness-style dry run over that revision (pending/`FIXED_LABELS`/`DOCUMENTED_LABELS` + evidence/reason rules of `run-validation.py:104-108, 752-806`) returns `pending: [2,4,5,7,10,12,13,15,16,17,18,19,20,21,22,23]`, `fixed-without-control: []`, `documented-without-reason: []`, `bad labels: []` — i.e. no row of mine can fail the O check. Final tracker state belongs to the O14 scribe; if any later rewrite drops these fields, the values to restore are exactly those in this section.

## 5. Reproduction

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
# idx 3
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json   # exit 0
python3 -c "import hashlib,json;m=json.load(open('examples/culture-d3/expected.json'))['manifest'];print(len(m),[k for k,v in m.items() if hashlib.sha256(open(k,'rb').read()).hexdigest()!=v])"
git diff 57c3ce6 HEAD -- examples/culture-d3/expected.json          # 3 digests + re-serialization
git show 57c3ce6:tools/gates/costume-era-consistency-gate.py > /dev/null && git diff --stat 291c714 e1694ba
# idx 11
git show 291c714:corpus/knowledge/synthesis/era-language-staging.md | sha256sum
git show 291c714:corpus/knowledge/synthesis/loanword-material-dating.md | sha256sum
git show 291c714:corpus/knowledge/synthesis/loanword-material-dating.md | sed -n '44p;54p'
sha256sum examples/culture-d2/components/11-costumes.yml
python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json   # exit 0
```

## 6. Limits

- Filed report bytes (`reports/round-9/d3/findings-10.md`, `reports/round-8/depth/findings.md`, `reports/round-8/depth/design-spec.md`) were read, never rewritten; corrections live in this entry per the round's standard.
- The re-pin itself was an orchestrator act in round 9; this seat verified the record and reproduced the controls, and did not re-pin anything.
- The S13 fix is a documentation correction; it does not change any tool, gate or corpus byte (the values concerned have no live consumer — sweep in §2.4).
- This file adjudicates nothing out of province (no canon, no real-world rights, no gate mechanics).

FILES: reports/round-10/fix-05.md | SUMMARY: R10-O05 fixer — tracker idx 3 (R9-F2, D3 frozen pin red) and idx 11 (R8-S13, pinned digests/locators) both dispositioned fixed-with-control with re-run controls (frozen run exit 0 + 24/24 manifest sweep + old-vs-new gate differential byte-identical; both S13 pins resolve exactly at revision 291c714, current HEAD bytes recorded, locators :44/:54 confirmed, no live consumer), one new residual recorded (the round-9 re-pin re-serialized expected.json: indent 2→1, trailing newline dropped), tracker rows 3 and 11 updated with harness-accepted labels.
