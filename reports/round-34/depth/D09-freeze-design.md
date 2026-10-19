- Seat: D09 | executor | claim D | date 2026-10-19 | baseline da68a6d

## Mission (targets.json, seat D09, verbatim)

"Freeze design: freeze.txt format (sha256 lines) + the tamper-control design (mutated byte → gate red), mirroring the declared-in-r6 freeze receipt pattern."

Method: read the freeze writer and the gate in the live tree; measured the r6 receipt's exact byte
shape; re-ran the writer into `.scratch` (both arms); built an 8-case single-byte mutation matrix
against `.scratch` copies of the filed r6 pair and ran the real gate + a digest audit on each; ran
three live e2e tamper arms. No filed byte was edited; no `reports/round-*/run-validation.py` was
executed (F-C13-1); every mutation lived in a scratch copy.

## 1. freeze.txt format spec for `reports/round-34/handoff/declared-in-r7/`

**Writer.** `v3_freeze` (`tools/exercise-handoff-e2e.py:3978-4127`) writes five files into the
target dir, in this order: `expected.json` (:4084), `packet.md` (:4085), `twin.json` (:4086),
`run.log` (:4104), `freeze.txt` (:4126). Refusal is fail-closed before any write: preflight
problems (:3981-3983), gate exit ≠ declared or any finding (:3987-3988), scan ≠ declared
(:3989-3995), uncertainty findings (:3998-3999), links unresolved (:4000-4005).

**Encoding.** `"\n".join(freeze_lines) + "\n"` (:4126), UTF-8. Ellipsis is U+2026 (`…`), not three
dots — measured: r6 `freeze.txt` line 6 and line 8 each carry one/two `0x2026` codepoints.
Measured sizes: r6 receipt 8 lines / 586 B (last line is a diff row); a fresh-dir receipt is
8 lines / 521 B (last line is the fixed sentence). *(Correction for the record: D02-render.md §2
calls its 521 B receipt "9 lines"; the measured line count is 8 — `wc -lc
.scratch/d09/r7-probe/freeze.txt` → `8 521`.)*

**Line grammar** (line → template → source):

| # | template | source |
|---|---|---|
| 1 | `frozen: {YYYY-MM-DD} by tools/exercise-handoff-e2e.py --profile v3` | :4114; date from `datetime.date.today().isoformat()` :4012 |
| 2 | `packet_sha256: {64 hex}` | :4115 ← `assembly.packet_sha256` :4015 |
| 3 | `twin_sha256: {64 hex}` | :4116 ← `assembly.twin_sha256` :4016 |
| 4 | `gate: exit {e}, fields={f}/{ft}, glossary-entries={g}, findings={n}` | :4117-4118 |
| 5 | `semantics: uncertainty exit {e}, links {resolved}/{checked} resolved` | :4119 |
| 6 | `claims: {n} statuses {supported}/{partial}/{unresolved}; v2-subset {digest[:16]}…; alias leg {state}` | :4120-4121 |
| 7 | `read set: {len(V3_READ_SET)} files; component digests {matched}/{checked}; d4 pins {matched}/{checked}` | :4122-4123 |
| 8+ | diff rows, else the fixed sentence `no tracked value changed since the previous freeze` | :4125 |

**Terminal lines.** Diff key order is fixed at :4107 (`packet_sha256`, `twin_sha256`, `claim_ids`,
`glossary_entry_ids`, `v2_subset_digest`, `alias_state`), then `inputs` sorted (:4110); row forms
`re-frozen {key}: {prev[:40]}… -> {new[:40]}…` (:4109) and
`re-frozen input {rel}: {prev[:12]}… -> {digest[:12]}…` (:4112). `previous` is read from the target
dir's own `expected.json` (:4079-4083) — so the diff is against the receipt's predecessor **in the
same directory**, not against r6. Two shipped classes, both measured today:

- **pre-seeded arm** (r6 `expected.json` copied in first, D01-layout.md §3 step 1): with today's
  bytes unchanged the freeze still prints line 8 = `no tracked value changed since the previous
  freeze` — and it is *true*: the seeded vs frozen `expected.json` differ only in `/frozen_at` and
  `/baseline_digest`, `inputs` identical (`json` probe, `.scratch/d09/r7-seeded`). A changed packet
  or changed input surfaces as `re-frozen …` rows (D01's `.scratch/d01/r7-diff` probe).
- **fresh-dir arm** (no expected.json): `previous=None` → the same fixed sentence, which then
  reads as provenance it does not have (D02-render.md §8 raised the same wart).

**Recommendation (binding on the build script, integrator-owned):** use the pre-seeded arm, so the
line is honest either way, and record in the receipt which arm ran. Caveat from D01-layout.md §3:
`freeze.txt`'s diff iterates only the *new* inputs, so a path **dropped** from the read set prints
nothing; the receipt must also carry the old-vs-new `expected.json.inputs` key diff.

**r7 instance** (values measured 2026-10-19 at da68a6d; digests `to-verify` — they are whatever the
applied drafts produce, and today's unmodified render reproduces r6's exactly, §2):

```
frozen: 2026-10-19 by tools/exercise-handoff-e2e.py --profile v3
packet_sha256: <to-verify: 64 hex; 6ced88ad… if no source draft lands>
twin_sha256: <to-verify: 64 hex; 6633443d… if no source draft lands>
gate: exit 0, fields=16/16, glossary-entries=20, findings=0
semantics: uncertainty exit 0, links 105/105 resolved
claims: 27 statuses 16/7/4; v2-subset ad35c860acf3b452…; alias leg landed
read set: 58 files; component digests 26/26; d4 pins 8/8
<diff rows | no tracked value changed since the previous freeze>
```

## 2. Freeze lines 2-3 are claim D's falsifier

Measured today: `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` → `exit=0 …
packet_sha256=6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb`, i.e. the live
render is byte-identical to r6, and a fresh `--freeze` reproduces r6's `packet.md` / `twin.json` /
`run.log` bytes exactly (D02-render.md §2, independently reproduced by my `.scratch/d09/r7-probe`).
Cause: the 12 D4 ledger rows are parsed **verbatim from a filed round-20 artifact**
(`CLAIMS_MAP` `tools/exercise-handoff-e2e.py:184`, parsed `:2289-2321`, concatenated :2599-2611) and
OQ-V3-05 is a literal (`:3524-3533`); read-set drift is 0 (D02 §2 probe).

Consequence: **if `reports/round-34/handoff/declared-in-r7/freeze.txt:2` reads `6ced88ad…`, the
stale prose was not fixed** — byte-identical bytes cannot carry rewritten rows, so claim D's
`after_required` ("zero stale figures") is unmet by construction. The receipt therefore carries its
own falsification test; the only ways to move line 2 are the integrator-applied source drafts
(route A/B, D02 §5, D01-layout.md §4), and no seat may move it by editing filed bytes. Exact check:

```bash
sed -n '2p' reports/round-34/handoff/declared-in-r7/freeze.txt
python3 tools/exercise-handoff-e2e.py --profile v3 --baseline reports/round-34/handoff/declared-in-r7/expected.json --quiet
# the reported packet_sha256 must equal the freeze.txt value, and must differ from 6ced88ad… once the drafts land
```

Note the asymmetry: the e2e's `frozen-packet` leg compares the **assembled** packet (:3934-3939),
never the stored `packet.md`; the stored bytes are pinned only by the receipt (below).

## 3. Tamper-control design

### 3.1 The measured blind spot

Eight single-byte mutations of the filed r6 packet copy, each run through the real gate
(`python3 tools/gates/handoff-packet-check.py packet.md`, foreign cwd) plus the receipt audit
(§3.2). Commands: `.scratch/d09/mut-control.py`, `.scratch/d09/tamper-matrix.py`.

| case (one byte changed) | gate exit | receipt-audit exit |
|---|---|---|
| pos — unmutated copy | 0 | 0 |
| t1 `packet_version` row label → `packet_versions` | **1** (`FINDING HO-MISSING`) | 1 |
| t2 `contract digest sha256:` → `sha257:` | **0** | 1 |
| t3 manifest digest byte `aac91246` → `aac91247` (:106) | **0** | 1 |
| t4 `- canon_standing:` → `- canon_standingx:` | **0** | 1 |
| t5 prose word `operability exercise` → `… exercises` | **0** | 1 |
| t6 one `\n` appended | **0** | 1 |
| t7 manifest digest hex case `e2fa3223b2aa` → `E2fa3223b2aa` | **0** | 1 |

**7 of 8 mutations pass the shape gate green.** The gate checks the §4 envelope (field presence,
canon markers, glossary vocabulary, digest *format*); it does not compare digests or figures
against the bytes they name, so a mutated byte stays green unless it breaks structure (t1). The
mission's phrase "mutated byte → gate red" therefore holds only for structural mutation: the
binding detector for the delivered copy is the receipt digest leg, and this is the design gap the
receipt covers. *(A15-audit-style hazard note: D02 §7.5 shows the same blindness on the link leg —
anchors resolve, currency is not checked.)*

### 3.2 Four-anchor receipt audit (the leg the tree does not have)

The same two digests are recorded in four places inside the frozen dir: the bytes on disk
(`packet.md`, `twin.json`, written :4085-4086), `freeze.txt:2-3` (:4115-4116),
`expected.json.packet_sha256/twin_sha256` (:4015-4016), and `run.log`'s `packet sha256:` /
`twin sha256:` rows (:4096-4097). No tool reads them: `grep -rn "freeze.txt" tools/*.py
tools/harness/*.py tools/gates/*.py` returns only the two writer sites (:1610, :4126). No tool
reads the stored copy automatically: the e2e gates an isolated copy of its own assembly
(:3855-3860) and only the shape gate, when a caller points it at the path, opens the filed
`packet.md`. Audit rule: exit 0 iff all four anchors agree per digest; exit 1 naming the
disagreeing anchors; exit 2 (could-not-evaluate) if an anchor is missing. Measured, one mutated
file per case, r6 copy (`.scratch/d09/anchor-matrix.py`):

| case | audit exit | first line |
|---|---|---|
| pos — unmutated | 0 | `OK — packet_sha256 and twin_sha256 agree across 4 anchors` |
| a1 `packet.md` byte | 1 | `TAMPER packet_sha256: disk=f6721441…; expected.json=6ced88ad…; freeze.txt=6ced88ad…; run.log=6ced88ad…` |
| a2 `twin.json` byte | 1 | `TAMPER twin_sha256: disk=90ef745f…; expected.json=6633443d…; …` |
| a3 `freeze.txt` line-2 byte | 1 | `TAMPER packet_sha256: disk=6ced88ad…; expected.json=6ced88ad…; freeze.txt=6ced88ae…; run.log=6ced88ad…` |
| a4 `expected.json` field | 1 | `TAMPER packet_sha256: disk=6ced88ad…; expected.json=0000…; …` |
| a5 `run.log` line | 1 | `TAMPER packet_sha256: disk=6ced88ad…; …; run.log=6ced88ae…` |

Why the loop closes (no consistent single-file edit escapes): editing disk + `freeze.txt` +
`run.log` alone leaves `expected.json` disagreeing (a4-style red); also fixing `expected.json`'s
`packet_sha256` to the mutant without re-signing hits the integrity pin (:3792-3796) → measured
exit 2 `E2E-BASELINE`; re-signing the mutant pin → measured exit 1 `E2E-DIGEST`, `FAIL
frozen-packet: assembled 6ced88ad009f… vs frozen 000000000000…` (:3934-3938), because the
*assembled* packet is what `expected.json` pins; re-signing a declared expectation
(`expected_scan`, :3797-3802) is refused outright (selftest control "tamper scan expectation").
Moving the bytes and all four anchors consistently is not tamper — it is the sanctioned re-freeze,
and it changes the receipt the round record pins (§3.4).

### 3.3 The control matrix to run against the r7 pair

| id | control | command | expected (measured model) |
|---|---|---|---|
| T-A | structural mutation → shape gate red | gate over a copy with a renamed §4 field row | exit 1, `HO-MISSING` (t1) |
| T-B | byte mutation → gate blind, receipt red | gate + audit over a copy with one prose byte changed | gate **0**, audit **1** (t5) |
| T-C | `twin.json` byte mutation | audit | exit 1, twin anchor named (a2) |
| T-D | receipt-line mutation (`freeze.txt`/`run.log`) | audit | exit 1, that anchor named (a3/a5) |
| T-E | `expected.json` pinned-value mutation | `e2e --profile v3 --baseline <mutated copy> --json` | exit **2**, code `E2E-BASELINE`, "baseline integrity digest mismatch — the baseline file was edited without re-freezing" |
| T-F | read-set drift | mutate one read-set file in a copy | exit **1**, `E2E-DIGEST` naming the file (selftest m12b, `:4424-4429`; r30 precedent `reports/round-30/regression.md:36`) |
| T-G | re-signed mutant pin | mutate pin + recompute `baseline_digest`, run e2e | exit **1**, `E2E-DIGEST`, `frozen-packet` mismatch |
| T-H | declared-expectation re-sign | mutate `expected_scan` + re-sign | exit **2**, `E2E-BASELINE` (selftest control, `:4440-4448`) |

T-E and T-G were run live by this seat on copies of the r6 pair (§3.2); T-F/T-H are the tool's own
filed controls, re-run green today (`--selftest` → exit 0, 39 controls, incl. `m12a`, `m12b`).

### 3.4 Residual, stated honestly

All four anchors live **inside** the frozen dir, so they bound single-file edits, not a wholesale
re-freeze (which is legitimate by design). The dir-level anchor must therefore be an external,
round-owned row: the **sha256 of `freeze.txt` itself**, recorded in the round-34 receipt and
validation (new rows; integrator-owned — seats cannot append to shared bookkeeping). The audit
prints exactly that value (`… freeze.txt sha256 6fe70c0c…` for r6) so the row can be transcribed
without a second measurement.

## 4. Control set for the r7 receipt (exact, re-runnable)

```sh
R7=reports/round-34/handoff/declared-in-r7
cp reports/round-30/handoff/declared-in-r6/expected.json "$R7/expected.json"   # pre-seed (§1)
python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze "$R7"           # writes 5 files, refuses on red
python3 -B tools/gates/handoff-packet-check.py "$R7/packet.md"                 # exit 0, 16/16, 20, 0
python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline "$R7/expected.json" --quiet
python3 -B tools/harness/handoff_freeze_audit.py "$R7"                         # candidate tool (§5), exit 0
sed -n '2p' "$R7/freeze.txt"                                                   # must equal the --quiet digest, ≠ 6ced88ad…
```

Controls T-A…T-H run on **copies** under `$TMPDIR`; their exits and first lines belong in the
round-34 receipt (D12) and validation as new rows — **not** appended to `run.log`, which the
writer owns (:4087-4104) and whose bytes are the fourth anchor.

## 5. Draft for the integrator (new file; no shared bytes edited)

Path: `tools/harness/handoff_freeze_audit.py` (new file — nothing to supersede). Candidate source
is the exact prototype measured in §3.2 (`.scratch/d09/freeze-audit2.py`), with
`DIGEST_LINE`/`RUNLOG_LINE` regexes:
`^(packet_sha256|twin_sha256):\s*([0-9a-f]{64})\s*$` and
`^(packet|twin) sha256:\s*([0-9a-f]{64})\s*$`
Exit contract 0/1/2 as in §3.2. Landing is integrator-owned (shared-file rule); this seat verified
the logic against the filed r6 pair, a fresh `.scratch` freeze, and all five mutation cases.

## Owed

- `reports/round-34/handoff/declared-in-r7/` — the executed freeze (never mine to run against filed
  paths; integrator runs the §4 command set after the source drafts land).
- Integrator decisions recorded here but not landable by a seat: the pre-seed step, the
  `tools/harness/handoff_freeze_audit.py` landing (§5), and the `freeze.txt` sha256 row (§3.4).
- `reports/round-34/depth/D05-packet-draft.md`, `D06-twin-expected.md`, `D13-negatives.md`,
  `D15/D16-gap-fill.md`, `D17/D19/D20` — absent at 04:12 (`ls reports/round-34/depth/`); if D06
  narrows the file set, §1's five files and §4's command set must be reconciled with it. My §2
  digest expectation (line 2 ≠ `6ced88ad…` after the drafts) is the cross-check.
- `to-verify`: the r7 digests and the D03/D04 row texts they fold; the D13 negatives seat should
  reuse §3.1's gate-blind cases as its negative controls.

## Citations

Paths (relative to `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, baseline da68a6d):

- `tools/exercise-handoff-e2e.py:184`, `:2289-2321`, `:2599-2611` (CLAIMS_MAP route), `:3510-3540`
  (OQ literals), `:1602-1610` / `:4113-4126` (freeze.txt writers, v1/v3), `:1933-1934` (v3
  defaults), `:3763-3803` (`v3_baseline_digest`, `v3_load_baseline`, integrity pin), `:3806-3977`
  (`v3_exercise`, incl. `:3814-3852` digest/preflight legs, `:3925-3947` frozen
  packet/twin legs), `:3978-4127` (`v3_freeze`), `:4130-4150` (`v3_build_fixture_root`,
  `v3_freezed_copy`), `:4407-4456` (tamper controls m12a/m12b/m8/scan-expectation), `:4475-4608`
  (CLI, `--freeze`/`--quiet`/`--json`)
- `tools/gates/handoff-packet-check.py:122-139` (`FIELD_NAMES`), `:164-167` (`DIGEST_RE`),
  `:469-609` (`evaluate_text`), `:884-897` (CLI)
- `reports/round-30/handoff/declared-in-r6/{freeze.txt,packet.md:148-152,307, twin.json,
  expected.json, run.log}` (filed r6 pair; freeze.txt 8 lines/586 B)
- `reports/round-34/depth/D01-layout.md` (§3 build sketch, §4 sources, §3 diff caveat),
  `D02-render.md` (§2 byte-identity table, §5 routes A/B, §7 coherence, §8 freeze.txt wart)
- `reports/round-34/claims.json` (claim D before/after, counting commands), `targets.json` (D09
  mission, shared_rules 0-5), `REGIMEN.md` (round contract)
- `.scratch/d09/{mut-control.py,tamper-matrix.py,freeze-audit.py,freeze-audit2.py,anchor-matrix.py}`
  (non-durable prototypes; outputs `.scratch/d09/*.out`, `.scratch/d09/runs/`, `.scratch/d09/matrix/`,
  `.scratch/d09/anchors/`)

Commands (this seat, 2026-10-19, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0, `packet_sha256=6ced88ad…`
- `python3 tools/exercise-handoff-e2e.py --profile v3 --json` → exit 0, 15/15 checks OK (58 read-set
  digests, 26/26 component, 8/8 d4 pins, 105/105 links, 27 claims 16/7/4)
- `python3 tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch/d09/r7-probe` → exit 0, five
  files; freeze.txt 8 lines/521 B; line 8 = `no tracked value changed since the previous freeze`
- seeded arm: `cp r6/expected.json .scratch/d09/r7-seeded/` + `--freeze` → 8 lines/521 B, same line 8;
  `expected.json` differs from r6 only in `/frozen_at`, `/baseline_digest`; `inputs` identical
- `python3 .scratch/d09/mut-control.py`, `python3 .scratch/d09/tamper-matrix.py` → §3.1 matrix
- `python3 .scratch/d09/anchor-matrix.py` → §3.2 audit matrix
- `python3 tools/exercise-handoff-e2e.py --profile v3 --baseline .scratch/d09/baseline-tamper/expected.json --json`
  → exit 2, `E2E-BASELINE`, "baseline integrity digest mismatch"
- `python3 tools/exercise-handoff-e2e.py --profile v3 --baseline .scratch/d09/resign/expected.json`
  → exit 1, `E2E-DIGEST`, `FAIL frozen-packet: assembled 6ced88ad009f… vs frozen 000000000000…`
- `python3 tools/exercise-handoff-e2e.py --profile v3 --selftest` → exit 0, 39 controls listed
  (incl. `m12a tamper baseline: exit 2 E2E-BASELINE`, `m12b tamper read-set … exit 1 E2E-DIGEST`)
- `sha256sum reports/round-30/handoff/declared-in-r6/*` → freeze.txt `6fe70c0c…`, packet `6ced88ad…`,
  twin `6633443d…`, expected `ea1e2927…`, run.log `b5ee3351…`
- `wc -lc reports/round-30/handoff/declared-in-r6/freeze.txt` → `8 586`; `od -c` tail → trailing
  `\n`, `0x2026` ellipses
- `grep -rn "freeze.txt" tools/*.py tools/harness/*.py tools/gates/*.py` → only `:1610`, `:4126`
