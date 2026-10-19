- Seat: D01 | executor | claim D | date 2026-10-19 | baseline da68a6d

# D01 — declared-in-r7 layout + build-script sketch

Mission: the exact file set of `reports/round-34/handoff/declared-in-r7/`, mirroring
`declared-in-r6`'s shape, and how the renderer is invoked to produce those bytes from the
**current** D2/D3/D4 artifacts. Read-only on all filed bytes; every probe below ran under
`TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` with `python3 -B`, writing only into
`.scratch/d01/**`. No filed round runner was executed (F-C13-1 rule) — the tool run is
`tools/exercise-handoff-e2e.py`, not a `run-validation.py`.

## 1. The decisive measurement: the renderer at HEAD *is* the r6 revision

`declared-in-r6` is not an authored document — it is the renderer's output. So the first
question for an r7 layout is whether it can differ from r6 at all without changing the
renderer's inputs. Measured (probe `.scratch/d01/r7-probe`, seeded with r6's `expected.json`
so the re-freeze diff is exercised):

```
python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch/d01/r7-probe
→ exit 0; froze .scratch/d01/r7-probe: packet sha256 6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb
```

- the fresh render is **byte-identical** to r6: `cmp` exit 0 on `packet.md`; `sha256sum` =
  `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` for
  `reports/round-30/handoff/declared-in-r6/packet.md` **and** `.scratch/d01/r7-probe/packet.md`;
  `twin.json` = `6633443d70ce44ed2bb43ab58aa60a1c98e4bbc79b2f577a63181c89dc16fd4e` on both;
- identical sizes (expected.json 10,856 B; freeze.txt 521 B; packet.md 105,584 B; run.log 1,603 B;
  twin.json 103,625 B) versus r6's 10,856 / 586 / 105,584 / 1,603 / 103,625;
- `freeze.txt:8` = `no tracked value changed since the previous freeze`.

**Consequence for the layout:** an r7 revision whose bytes are produced by the renderer *as it
stands* is impossible — the delta r7 must carry lives in exactly two renderer inputs, both
filed or literal (see §4). A "build script" for r7 is therefore a three-part move: new
claims-map bytes → renderer re-points (drafted, integrator-applied) → freeze + controls.

## 2. The layout — exact file set (mirroring declared-in-r6)

`v3_freeze` (`tools/exercise-handoff-e2e.py:3978-4127`) writes exactly five files, one command,
no partial state: `expected.json` (:4084), `packet.md` (:4085), `twin.json` (:4086),
`run.log` (:4104), `freeze.txt` (:4126).

| file | producer line | role | r6 size |
|---|---|---|---|
| `packet.md` | :4085 | the rendered Markdown packet: 16 envelope fields, §artifact_manifest (58 rows), claim_ledger (27 rows), coupling_edges (88 rows), open_questions, glossary | 105,584 B |
| `twin.json` | :4086 | the machine twin re-parsed from the rendered Markdown; judged by both harness validators | 103,625 B |
| `expected.json` | :4084 | the frozen baseline: declared expectations, `packet_sha256`/`twin_sha256`, 58 read-set input digests, `field_digests`, census, `baseline_digest` self-pin | 10,856 B |
| `freeze.txt` | :4126 | human receipt: freeze date/by, packet+twin sha256, gate scan, semantics, claims census, read set, and the **re-freeze diff rows** | 586 B in r6 (521 B when no diff) |
| `run.log` | :4104 | leg ledger: gate invocation+verdict, uncertainty/links, v2-subset digest, alias state, digests, read set, the four D4 legs, gate stdout | 1,603 B |

**Recommendation:** keep the r7 directory to those five files and nothing else — the frozen dir
is a frozen-dir convention (A02's census: `find reports -type d -name 'declared-in*'` → six
dirs, r2/r3/r4/r5/r6 + the r2 alias), and nothing in the tool enumerates the directory, so any
extra file is convention debt with no compensating check. The build script, the claims-map
revision and the build receipt belong **beside** it, not inside it:

```
reports/round-34/handoff/
├── declared-in-r7/                 # exactly 5 files, renderer-written, frozen
│   ├── packet.md  twin.json  expected.json  freeze.txt  run.log
├── claims-map-v3-next.md           # NEW claims-map revision (renderer input, §4)
├── build-declared-in-r7.sh         # the build script (§3), run once
└── build-declared-in-r7.receipt.json / .log   # command, exits, digests, tamper matrix, inputs-key diff
```

## 3. Build script sketch (recipe; every step below was exercised except the renderer edits)

```sh
#!/bin/sh
# reports/round-34/handoff/build-declared-in-r7.sh  — run once, from the repo root
set -eu
export TMPDIR="$PWD/.scratch" PYTHONDONTWRITEBYTECODE=1
R7=reports/round-34/handoff/declared-in-r7
R6=reports/round-30/handoff/declared-in-r6

# 0. preconditions the freeze itself re-checks, run early for a clean failure
python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest --quiet   # 39 controls, exit 0
python3 -B tools/assemble-culture-d4.py --check
python3 -B tools/assemble-d4-typed.py --check

# 1. seed the predecessor baseline so freeze.txt carries an honest before→after
mkdir -p "$R7"; cp "$R6/expected.json" "$R7/expected.json"

# 2. render + freeze: this single command writes all five files from the live D2/D3/D4 bytes
python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze "$R7"     # exit 0 or it refuses

# 3. shape gate over the NEW packet, filed convention (also re-run inside the freeze)
python3 -B tools/gates/handoff-packet-check.py "$R7/packet.md"           # want fields=16/16, findings=0

# 4. default-chain replay against the NEW baseline (claim D counting command 2)
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet            # exit 0

# 5. byte-integrity control (see §5 — the e2e does NOT read the on-disk packet.md)
sha256sum "$R7/packet.md" "$R7/twin.json"
python3 - "$R7" <<'PY'
import json,sys,hashlib,pathlib
d=pathlib.Path(sys.argv[1]); b=json.loads((d/"expected.json").read_text())
for name,key in (("packet.md","packet_sha256"),("twin.json","twin_sha256")):
    live=hashlib.sha256((d/name).read_bytes()).hexdigest()
    assert live==b[key], f"{name}: {live} != expected.json.{key} {b[key]}"; print(f"{name} {live} == expected.json.{key}")
PY

# 6. tamper control: a pinned baseline is refused, never honoured (exit 2, E2E-BASELINE)
cp -r "$R7" "$TMPDIR/r7-tamper"
python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline "$TMPDIR/r7-tamper/expected.json" --quiet
#   → exit 2 only after expected.json is edited in the copy (probe §5 shows the two arms)
```

What the freeze refuses to do (fail-closed, all before any byte is written) — from
`tools/exercise-handoff-e2e.py:3981-4004`: preflight problems, gate exit ≠ 0 or any finding,
scan ≠ declared (`fields 16/16`, `glossary_entries 20`, `findings 0`), uncertainty findings
under `--require-oq`, or links unresolved/mismatched. `V3Assembly` raises earlier for: gate
`FIELD_NAMES` vs contract §4 disagreement (:3487-3496), ≠15 v2 rows (:3509-3510), failing D4
legs (:3548-3550), alias witnesses below 50/12 (:3552-3556), manifest-digest inequality
(:3640-3657), v2 subset inequality (:3659-3676), ≠12 candidate refs (:3631-3638), and a D4
ledger ≠12 rows (:3678).

**Diff-row caveat (measured).** `freeze.txt`'s diff iterates only the *new* inputs
(`:4106-4112`), and a key absent from the previous baseline prints as `None…`. Probe
`.scratch/d01/r7-diff` (seeded previous: packet pin zeroed, one input digest zeroed, one key
deleted) produced:

```
re-frozen packet_sha256: 0000000000000000000000000000000000000000… -> 6ced88ad009f1cfc94f7fc9e5656555f7da6682c…
re-frozen input reports/round-19/validation.json: ffffffffffff… -> 7dbc346ccab1…
re-frozen input reports/round-20/handoff/claims-map.md: None… -> 4b1b9a35a18f…
```

So the claims-map path swap will surface as a `None… -> <digest>` row (good), but a path
*dropped from the read set* prints nothing at all — the receipt must carry an explicit
old-vs-new `expected.json.inputs` key diff. `freeze.txt` alone is not a complete change list.

## 4. Where the r7 bytes' content comes from, and the two inputs that are stale

The renderer is a pure function of (live artifacts + `V3_READ_SET` of 58 files + two hard-coded
inputs). `expected.json.counts` is already live (`d4_typed_labels: 82`), which is why r6 is
shape-green while its prose is stale:

| r7 surface | source | live value |
|---|---|---|
| digest rows, sizes, counts, §validation | measured at render time | auto-correct |
| 15 v2 claim rows, 34 v2 edge rows | `reports/round-15/handoff/packet-v2-05.yml` (filed, correct) | unchanged |
| **12 D4 claim rows** (statement, kind, evidence status, `{status, basis}`, links) | `CLAIMS_MAP` = `reports/round-20/handoff/claims-map.md` (:184), read by `v3_parse_claims_map` (:2289-2319) | **stale on 4 of 12 rows (§6)** |
| **OQ-V3-05** | literal string in `V3Assembly.__init__` (:3524-3531) | **stale** |
| header prose naming the claims map (`packet.md:3`) | plain literal (:2699-2700) | path must be re-pointed |

Both stale inputs are *filed or literal*, hence two required source moves:

**(a) new claims-map bytes.** `CLAIMS_MAP` is a count of one file path; the new revision goes to
an unfiled path (`reports/round-34/handoff/claims-map-v3-next.md`) and is swapped **in the same
tuple slot** in `V3_READ_SET` (:1957) so the read set stays 58 files and the manifest row id
stays `A-57` (r6 `packet.md:95`; digest `4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8`).
Its grammar is fixed by `D4_ROW_RE` (:2286)
`^### (D4-CL\d\d) — (.+?) — (.+?) — \`([a-z]+)\`$` with exactly 12 matches, each row carrying
`- **statement:**`, `- **u.basis:**` and `- **links:**` bullets (:2293-2319) — a new file that
misses any of these raises `ArtifactError` before a byte is written.

**(b) drafted shared-file hunks (integrator applies; this seat never edits shared files).**
Four hunks in `tools/exercise-handoff-e2e.py`, before → after:

```
:184
- CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"
+ CLAIMS_MAP = "reports/round-34/handoff/claims-map-v3-next.md"

:2700 (header prose, currently a plain literal inside the add(...) argument list)
-        "from `reports/round-20/handoff/claims-map.md`. The ledger carries the round-15 uncertainty dimension "
+        f"from `{CLAIMS_MAP}`. The ledger carries the round-15 uncertainty dimension "

:1933-1934 (the re-pin cascade named by reports/round-34/claims.json; applied AFTER the freeze is green)
- V3_BASELINE_DEFAULT = "reports/round-30/handoff/declared-in-r6/expected.json"
- V3_FROZEN_DIR_DEFAULT = "reports/round-30/handoff/declared-in-r6"
+ V3_BASELINE_DEFAULT = "reports/round-34/handoff/declared-in-r7/expected.json"
+ V3_FROZEN_DIR_DEFAULT = "reports/round-34/handoff/declared-in-r7"

:3524-3531 (OQ-V3-05 — derive from the already-mined live values instead of a literal;
self.d4_labels and self.d4_holds are both populated well before this point, :3503-3504)
-            {
-                "id": "OQ-V3-05",
-                "question": (
-                    "D4's inherited and own holds stay open: twelve form holds + three rank holds + one "
-                    "note, thirteen unresolved rank items, three quarantine handles and four conflicts — "
-                    "kotodama; blocking for the affected D2 rank records and the six garment terms, not for "
-                    "this envelope"
-                ),
-                "unresolved_claims": "D4-CL09",
-            },
+            {
+                "id": "OQ-V3-05",
+                "question": (
+                    f"D4's own holds stay open: {self.d4_holds['hold']} form holds, "
+                    f"0 rank holds and {self.d4_holds['note']} note(s); the rank coverage block carries "
+                    f"{self.d4_labels['unresolved_items']} unresolved rank items, "
+                    f"{self.d4_labels['quarantine']} quarantine handles and {self.d4_labels['conflicts']} "
+                    f"conflicts — kotodama; blocking for the affected D2 rank records and the six garment "
+                    f"terms, not for this envelope"
+                ),
+                "unresolved_claims": "D4-CL09",
+            },
```

Only three tool sites hard-code the claims-map path: the `CLAIMS_MAP` constant (:184), the header
prose literal (:2700) and three docstrings (:34, :57, `v3_parse_claims_map`'s :2290). The
manifest row role (:2566), the §validation digest line (:2881) and the claim_ledger prose
(:2934) already interpolate `CLAIMS_MAP` and follow the constant automatically. `:2712`'s
`reports/round-20/handoff/packet.md` 3.0.0 sentence is a *different* artifact (the filed
round-20 exercise) and stays true — do not "fix" it (`packet.md:5`).

Re-pin safety check: `V3_FROZEN_DIR_DEFAULT` is also used by the selftest's throwaway fixture
(`v3_freezed_copy` :4146-4150), which freezes **inside** the copied fixture tree, so re-pointing
the constant makes the selftest write into a temp mirror only; the selftest is green at HEAD
(`--profile v3 --selftest --quiet` exit 0, 37.7 s, 39 controls incl. `m12a`/`m12b` tamper rows).

## 5. Controls this layout needs, and one the e2e cannot give

Measured tamper matrix on the frozen probe (both arms, `--baseline <copy>/expected.json --quiet`):

| arm | observed |
|---|---|
| `expected.json.packet_sha256` edited in a copy | **exit 2**, `E2E-BASELINE: baseline integrity digest mismatch — the baseline file was edited without re-freezing`, check `verdict` FAIL |
| `packet.md` byte-edited **on disk** in a copy, baseline untouched | **exit 0** — the exercise never reads the frozen dir's `packet.md` |

The second row is the layout's one gap: the e2e proves the bytes are *reproducible from the live
inputs*, not that the bytes *on disk* are the frozen ones. The build recipe therefore carries
step 5 (explicit `sha256sum`/`hashlib` comparison of `packet.md`/`twin.json` against
`expected.json`'s pins and `freeze.txt:2-3`). A claim-D verdict that quotes only `--quiet exit 0`
would be unprovable on this point.

## 6. Staleness census to be zeroed by the r7 revision (my own measurement, not copied)

Fresh render = r6 bytes, so the census is over `reports/round-30/handoff/declared-in-r6/packet.md`
(and its twin), against live bytes:

| packet.md | stale text | live bytes |
|---|---|---|
| :148 D4-CL05 | `typed_labels 74`, `native-form 56 / 12 / 6`, `findings_total 16`, `findings_hold_or_fail 15`, `labels 74` | `typed-labels.d4.yml:29-46` → `typed_labels 82`, `native-form 64 / translated-label 12 / borrowed-strata 6`, `findings_total 12`, `findings_hold_or_fail 12`, `label_findings_fail 0` |
| :149 D4-CL06 | `(hold 15, note 1, fail 0)`, "15 holds, 1 note", "+9 hold / +1 note delta" | `expected-holds.json.counts` `{hold 12, note 0, fail 0}`; `holds` = 12 rows, all `id: D2L-FORM-UNRESOLVED`; `notes: []` |
| :150 D4-CL07 | `conflicts (4)`, `quarantine handles (3)` | `conflicts 0` (`:30`), `rank_quarantine_handles 0` (`:40`); `reconciliation_records 6` (`:45`) still true |
| :152 D4-CL09 | `rank_rules_unresolved_items 13`, `rank_quarantine_handles 3`, `conflicts 4`, "thirteen unresolved rank items" | `:44` → `0`; `:40` → `0`; `:30` → `0` |
| :307 OQ-V3-05 | "twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts" | hold 12 / note 0; 0 / 0 / 0 |
| twin.json | `thirteen unresolved rank items` ×2, `74 labels` ×1, `hold 15` ×1 | same corrections |

**A finding beyond A02-H1 — the D4-CL09 *premise* is stale, not just its numbers.** The row
grounds on "`examples/culture-d4/typed-labels.d4.yml#rank_rules`, whose act rows carry
`adapt_status: cannot-evaluate`". Live: `rank_rules.gate_rank_rules` = 4 rows, `adapt_status`
distribution `{executable: 4}`; `unresolved`, `quarantine`, `residuals`, `act_rules`,
`assay_gaps`, `calibration_flags`, `jurisdiction_gaps`, `entitlement_edges` all empty;
`skipped` len 1; `normalized_rules` = RK-01..RK-04. So the v-next row must be **re-grounded**,
not just re-numbered, and its `unresolved` status may no longer be supportable. That is a
claims-map-owner decision (it moves the census frozen at `freeze.txt:7` = `16/7/4`), **not mine
to make** — recorded here so the builder does not silently re-word a row whose grounding no
longer exists.

**Trap for the builder:** `packet.md:129` (D2-CL01) also carries `findings_total 16`,
`conflicts 4`-class numbers — those are the **D2** family's and are live
(`examples/culture-d2/typed-labels.d2.yml#coverage` → `typed_labels 58`, `findings_total 16`,
`findings_hold_or_fail 15`, `conflicts 4`, `rank_quarantine_handles 3`,
`rank_rules_unresolved_items 13`). The D4 rows were written by copying the D2 family's numbers;
the fix must not "correct" the D2 rows (`OQ-V2-03` likewise) — its scope is D4-CL05/06/07/09 +
OQ-V3-05 only.

## 7. Owed actions for the integrator (not owed fragments)

1. Land `reports/round-34/handoff/claims-map-v3-next.md` (12 rows, round-20 grammar), with the
   D4-CL09 re-grounding decision recorded as a census-moving row, and re-run the row checks the
   round-20 file used (`packet_uncertainty.py --claims-json`, `packet_links.py --links`).
2. Apply the §4 hunks (claim D names the 1933-1934 re-pin as integrator-applied; the other three
   hunks are the same class) and re-run `--profile v3 --selftest --quiet`.
3. Run the §3 build once against the delivered revision; file the receipt with the inputs-key
   diff; then run step 4 (default-chain replay) and step 6 (tamper arm).
4. Two independent seats must audit the new packet's prose against live bytes (claim D threshold
   "zero stale figures … by two independent seats"); this fragment supplies one census, not the
   audit.

## Owed: none

No fragment this mission depends on is missing: `reports/round-33/adj/A02-handoff.md` (A02-H1,
the finding this claim closes) and `reports/round-33/adj/A11-verify-a01-a03.md` (independent
re-measurement of both columns) both exist and were read. The r7 bytes themselves, the
claims-map revision and the renderer hunks are other seats'/the integrator's work per §7 —
this fragment is the layout and the script sketch that were asked of D01.

## Citations

- `tools/exercise-handoff-e2e.py`: 20-60 (v3 docstring, 58-file read set), 184 (`CLAIMS_MAP`),
  1930-1934 (`V3_BASELINE_DEFAULT`/`V3_FROZEN_DIR_DEFAULT`), 1935-1959 (`V3_READ_SET`, slot 57 =
  `CLAIMS_MAP`), 1960-1976 (`V3_DECLARED`), 2161-2203 (`v3_mine_d4_labels`/`v3_mine_d4_holds`
  field sets), 2286-2319 (`D4_ROW_RE`, `v3_parse_claims_map`), 2566 / 2881 / 2934 (manifest role,
  §validation line, claim_ledger prose — all interpolate `CLAIMS_MAP`), 2691-2712 (header prose,
  path literal at `:2700`; round-20 3.0.0 sentence at `:2712`), 3487-3531 (`V3Assembly.__init__`
  guards, D4 mining at `:3503-3504`, v2-row guard `:3509-3510`, OQ-V3-05 literal `:3524-3531`),
  3548-3556 (D4 legs, alias witnesses), 3577-3603 (packet build, twin ids `:3602-3603`),
  3631-3678 (candidate/manifest/subset/D4-row assertions), 3771-3805 (`v3_load_baseline`,
  integrity pin), 3978-4127 (`v3_freeze`: refusals :3981-4004, five writes, diff loop
  :4106-4112), 4130-4150 (selftest fixture + `v3_freezed_copy`), 4540-4580 (CLI freeze branch
  `:4564`)
- `reports/round-30/handoff/declared-in-r6/{packet.md:5,95,113,125,129,148,149,150,152,307, expected.json, freeze.txt:1-8, run.log, twin.json}`
- `reports/round-20/handoff/claims-map.md:1-40,97-165` (D4 row grammar and stale wording)
- `examples/culture-d4/typed-labels.d4.yml:29-46` (coverage), `:306` region (second coverage
  block), `rank_rules` block (`gate_rank_rules` 4× `executable`, empty `unresolved`/`quarantine`/
  `residuals`); `examples/culture-d4/expected-holds.json` (`counts`, `holds`, `notes`)
- `examples/culture-d2/typed-labels.d2.yml` coverage (the D2 numbers that are live, not stale)
- `reports/round-33/adj/A02-handoff.md:1-181`; `reports/round-33/adj/A11-verify-a01-a03.md:85-112`
- `reports/round-34/claims.json` (claim D before/after, counting commands, thresholds);
  `reports/round-34/targets.json` (D01 mission/out, shared_rules)
- Commands (2026-10-19, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all `python3 -B`):
  - `python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch/d01/r7-probe` → exit 0,
    packet `6ced88ad…`, `freeze.txt:8` "no tracked value changed since the previous freeze"
  - `cmp`/`sha256sum` over `reports/round-30/handoff/declared-in-r6/{packet.md,twin.json}` vs
    `.scratch/d01/r7-probe/*` → identical digests, `packet.md` byte-identical
  - `python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline .scratch/d01/r7-tamper/expected.json --quiet`
    after (i) `packet.md` byte edit → exit 0; (ii) `expected.json.packet_sha256 = '0'*64` → exit 2
    `E2E-BASELINE: baseline integrity digest mismatch …`
  - `python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch/d01/r7-diff` with a
    seeded previous baseline (zeroed pin, zeroed input digest, deleted input key) → the three
    `re-frozen …` rows quoted in §3
  - `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest --quiet` → exit 0 (37.7 s; 39
    controls incl. `m12a`/`m12b` tamper rows); `git status --porcelain` → only `reports/round-34/`
    untracked, no filed byte touched
  - `python3 -c` JSON reads of `expected.json` (inputs keys, counts, `baseline_digest`),
    `examples/culture-d4/{typed-labels.d4.yml,expected-holds.json}`,
    `examples/culture-d2/typed-labels.d2.yml`; `grep -n`/`grep -c` censuses over the r6 packet and
    twin; `ls -la` of the r6 and probe dirs
