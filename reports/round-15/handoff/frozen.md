# R15-O08 — frozen baseline for handoff packet v2 + tamper control + isolated rerun

- seat: **R15-O08** (round 15, claim **O / operability**, targets.json "O-frozen": 1).
  Assignment, verbatim: "expected.json baseline for v2 + tamper control + isolated
  rerun; reports/round-15/handoff/frozen.md" — this file, the baseline bytes
  (`expected.json`), and the control tool (`frozen-verify.py`) are the seat's
  writes. No packet, tool, corpus, or filed round-8..14 artifact was written by
  this seat.
- date: **2026-10-17**; measurement window 21:36–22:11 -03 (`date -Is`).
  Lane revision throughout: `c60b17c21a77182a5c1f0251e98b4ea42e563c3e`
  (`git rev-parse HEAD`) plus the round's untracked worker output; no commit was
  made by this seat. All scratch under `export TMPDIR=$PWD/.scratch`
  (`.scratch/r15o08/`, gitignored).
- what this is: the committed frozen run of the round-15 handoff-v2 verification
  legs — shape gate `tools/gates/handoff-packet-check.py` over
  `reports/round-15/handoff/packet-v2-05.md`, plus
  `tools/harness/packet_uncertainty.py` and `tools/harness/packet_links.py` over
  the machine twin — frozen per
  `corpus/knowledge/verification/gate-frozen-run-standard.md` §§5–6 (freeze from
  measured bytes, digest-first verification, fail-closed tamper classes), plus a
  falsifiability drill and an isolated-tree rerun. Lane-local engineering
  evidence; not canon, not lore acceptance, not round completion (standard §10).
- dependencies at freeze: the O02 durable builder
  (`tools/build-handoff-v2.py`, design `reports/round-15/handoff/v2-design.md`
  §6) had **not landed** by 22:10:59 -03 after three 60s-cadence poll windows
  (~40 min). `reports/round-15/handoff/review-10.md` F10-2 (:52–53) had already
  named this gap with owner "O-impl + O-frozen seats" and control "the tool
  exists, --selftest exits 0, and a first frozen baseline file is committed
  in-lane; --root isolated tamper probes pass". This seat exercised its half:
  the freeze/verify/tamper entry point below is durable, deterministic, and
  self-tested; the builder leg itself stays open with O-impl (§5, G1).

## 1. The baseline — bytes, home, verdict

`python3 reports/round-15/handoff/frozen-verify.py --freeze` (tool sha256
`f6e3b4ae25e821dd88e3f5de4fb96c5310fcbe6daca0678743225cfc47c1d10d`) measured the
live tree twice and refused to write on any movement, then wrote:

| file | sha256 (2026-10-17 22:09 -03) | role |
|---|---|---|
| `reports/round-15/handoff/expected.json` | `b927db311370c27a0b40d25729cf6ec020398e76634eeb3c2feb0a47fcf162e6` | the frozen baseline (schema `kotodama-frozen-run-v1`, profile `kotodama-handoff-v2/1`) |

Baseline content (all values measured from bytes, none copied from a printed
verdict): `packet_sha256 24f9dd39bdadf05fcd7961d3c7b63f5aadc047330ba4b25a5bc5d61d35d38d3b`
(gate-facing markdown twin) and `packet_yml_sha256 39cf4d53b02a1a9026e3a9a302cd1031d1b6a55fc2b8ea9d7b7eb877fa1dfcd6`
— the exact bytes review-9 (:15–16), review-10 (:7) and the contract-audit
re-run (`contract-v2-audit.md`, measured 00:59:33Z) pinned; `expected_exit 0`;
`expected_scan {fields 16/16, glossary_entries 20, findings 0}`;
`gate_stdout_sha256` (whole-stdout pin); `census {claims 15, statuses
{supported 8, partial 5, unresolved 2}}` — this seat's independent textual
census of the yml twin's `claim_ledger:` block, matching review-9's independent
census (:34); `uncertainty {claims 15, findings 0, require_oq_findings 0}`
(the stronger `--require-oq` mode the audit used); `links {links_checked 50,
resolved 50, findings 0}`; `manifest_rows 26` file-backed rows re-hashed live
(27 manifest rows total; the 1 inline payload row carries no path — the same
split the audit re-hash counted); `inputs` = **28 pinned digests** (the packet
twins, the gate `e2fa3223…`, both harness validators `f81bc9f7…`/`cdcc1931…` —
byte-equal to the audit's dependency_manifest pins — and every file-backed
artifact-manifest path, contract `5f4c02bf…` included); `baseline_digest
` integrity digest over the baseline's own content; `frozen_at 2026-10-17`;
`frozen_by R15-O08 reports/round-15/handoff/frozen-verify.py --freeze`.

Siting: the baseline lives under `reports/round-15/handoff/` and is **invisible
to the gate battery** by construction (`tools/check-gate-battery.py` output
contains 0 occurrences of the path, post-freeze receipt
`.scratch/r15o08/battery-post.txt` `6701e2f4…`) — the round-11 lesson
(`tools/gates/expected/**` home tripped `BASELINE-GATE-UNCOVERED`) applied as
the design's siting rule (`v2-design.md` §6). Battery pre/post receipts are
identical in verdict: `battery_exit 0, pass 7, pinned 8, unevaluable 0`
(pre `10651aa3…`, post `6701e2f4…`).

Trackedness: `git status --porcelain reports/round-15/handoff/` →
`?? reports/round-15/handoff/` — both files are new untracked files at this
stamp; the orchestrator's round-15 integration commit is what makes them
committed evidence.

## 2. Freeze and verify receipts (commands verbatim, lane root)

| # | command | observed |
|---|---|---|
| 1 | `python3 reports/round-15/handoff/frozen-verify.py --freeze` | exit 0; wrote the baseline; `inputs: 28 pinned; manifest rows 26; census {supported 8, unresolved 2, partial 5}; links 50/50` (`.scratch/r15o08/freeze.out`) |
| 2 | `python3 reports/round-15/handoff/frozen-verify.py` | exit 0; `frozen-v2: exit=0 fields=16/16 glossary=20/20 findings=0 claims=15/15 statuses={…} links=50/50 packet_sha256=24f9dd39bdad…` |
| 3 | `python3 reports/round-15/handoff/frozen-verify.py --selftest` | exit 0; `selftest: 24/24 checks passed` (§3) |
| 4 | `python3 tools/gates/handoff-packet-check.py reports/round-15/handoff/packet-v2-05.md` | exit 0; `INFO scan: fields=16/16 glossary-entries=20 findings=0` |
| 5 | `python3 tools/harness/packet_uncertainty.py --packet reports/round-15/handoff/packet-v2-05.yml --json` (and `--require-oq --json`) | exit 0; `claims=15 findings=0` both modes |
| 6 | `python3 tools/harness/packet_links.py --packet reports/round-15/handoff/packet-v2-05.yml --repo-root . --json` | exit 0; `links_checked=50 resolved=50 findings=0` |
| 7 | `python3 tools/check-gate-battery.py` | exit 0; `pinned 8, unevaluable 0`; my baseline undiscovered (siting, §1) |

The freeze is deterministic: three `--freeze` executions (two in-lane, one in a
copied tree, §4) all produced byte-identical `expected.json` (`b927db31…`).

## 3. Tamper control — fail-closed and drift classes on the committed bytes

Instrument: `reports/round-15/handoff/frozen-verify.py --selftest` — twelve
scenarios, each in a fresh isolated copy of `tools/ examples/ corpus/ reports/`
under `$TMPDIR`, one mutation each, expectations recorded before running
(`.scratch/r15o08/selftest.out` `ad22b322…`, 24/24, exit 0):

| scenario | mutation (copy only) | observed | class |
|---|---|---|---|
| s0 positive | none | exit 0, all pins match | — |
| s1 | baseline removed | **exit 2** | `V2F-BASELINE` |
| s2 | baseline → `{ not json` | **exit 2** | `V2F-BASELINE` |
| s3 | baseline `packet_sha256` → `000…0`, integrity digest re-signed | exit **1** | `V2F-PIN` (baseline-vs-live disagreement: evaluable, wrong) |
| s4 | a pinned `corpus/` read-set file deleted | **exit 2** | `V2F-ARTIFACT` |
| s5 | a pinned `examples/` read-set file edited | **exit 2** | `V2F-DIGEST` (standard §6 `snapshot_tampered`) |
| s6 | one comment appended to the gate | **exit 2** | `V2F-DIGEST` |
| s7 | one comment appended to `tools/harness/packet_links.py` | **exit 2** | `V2F-DIGEST` |
| s8 | packet markdown twin edited | **exit 2** | `V2F-DIGEST` |
| s9 | baseline `expected_scan.findings` 0→1, re-signed | exit **1** | `V2F-GATE` (a legitimately re-pinned but wrong expectation reads as drift, never silent pass) |
| s10 | baseline census `supported` 8→9, re-signed | exit **1** | `V2F-COUNT` |
| s11 | none (two `--verify` runs) | stdout byte-identical | determinism |

Class mapping, per the standard's §6 table: missing/malformed/edited baseline
and any pinned-byte change → could-not-evaluate (exit 2, comparison refused);
a re-signed-but-wrong expectation → drift (exit 1, named leg). There is no
mutation class that leaves the run at exit 0. The could-not-evaluate drills
(s1–s8) are the ones this control exists to show: a changed read set or an
edited baseline refuses to verdict instead of being re-blessed.

The canon-wording hazard on basis cells is not re-drilled here because the md
twin is digest-pinned (s8 shows any md edit is refused before the gate runs);
the before/after control for that hazard is review-9 §3 (21:47 bytes: gate exit
1 `HO-CANON-CLAIM` at the A-17 row; 21:55 bytes: reworded, exit 0) — cited, not
re-measured.

## 4. Isolated rerun — the copied tree

```sh
S=$PWD/.scratch/r15o08
sh $S/copy-tree.sh $S/tree        # tools/ examples/ corpus/ reports/, no .git/.scratch
cd $S/tree && export TMPDIR=$PWD/.scratch-tmp && mkdir -p .scratch-tmp
```

| leg | command (in the copy) | observed |
|---|---|---|
| A replay | `python3 reports/round-15/handoff/frozen-verify.py` | exit 0; same summary line as in-lane (`fields=16/16 glossary=20/20 findings=0 claims=15/15 links=50/50 packet_sha256=24f9dd39…`) — receipt `rerun-verify.out` `500e5a3e…` |
| B independent re-freeze | `… --freeze --baseline .scratch-tmp/independent-expected.json` | exit 0; **byte-identical** to the committed baseline (`b927db31…` both; `python3 -m json.tool` diff empty) — the baseline is reproducible from the live bytes, not hand-tuned — receipt `rerun-freeze.out` `24a26b36…` |
| C selftest in the copy's own tool revision | run by the matrix itself (s0–s11 execute each tree's own `frozen-verify.py`) | 24/24 |

Leg A/B re-execution in a tree this seat copied cannot certify the underlying
tools' internals — the gate and both validators were authored by lane peers this
round; this is reproducibility evidence, not a truth claim (standard §10,
KTD-FR-S-0007).

## 5. Findings and named gaps (reported, not absorbed)

- **G1 — the O02 durable builder has not landed (owner: O-impl; joint
  ownership named in review-10 F10-2).** `tools/build-handoff-v2.py` absent at
  22:10:59 -03 after three poll windows (60s cadence, started 21:36). The
  claim's `after_required` ("a durable builder tool with --selftest and a
  frozen expected.json baseline lands") is therefore half-met at this stamp:
  the frozen baseline exists (this file), the durable re-runnable entry point
  for it exists (`frozen-verify.py`, `--freeze/--verify/--selftest`, 24/24),
  but the packet *builder* (render → link checks → gate → baseline compare,
  `v2-design.md` §6) is still owned by O-impl. When it lands it should adopt or
  supersede `expected.json` explicitly (re-pin only with recorded reason,
  design §9); this baseline's pins survive that landing unchanged unless the
  packet bytes move. `reports/round-15/run-validation.py` builder discovery
  (probed in-process 22:09) currently finds **0 candidates** — with
  `frozen-verify.py` deliberately named to fall outside `pick_builder`'s
  profile (name carries "verify") so the builder lane stays unambiguous.
- **G2 — harness churn inside the window (resolved; history retained).**
  `tools/harness/packet_uncertainty.py --selftest` was **red** at this seat's
  21:38:16 measurement (revision `2e9dd1a5…` then on disk: fixture X3/X5/X9
  expectation mismatches + a bare-dash `open_questions` misparse) and green
  ~30s later at `11d74ac4…` (19/19); the owner's shard-1 defect list (:66–80)
  records the same repairs with controls. Final pinned revisions
  `cdcc1931…` (uncertainty) / `f81bc9f7…` (links) pass their selftests
  (19/19, 31/31) and are byte-equal to the audit's and this baseline's pins.
- **G3 — packet naming vs the runner (resolved in-flight).** The landed packet
  is `packet-v2-05.{md,yml}`; the runner I read at 21:30 matched only exact
  `packet-v2.{md,yml}` names, which would have hidden the packet. The runner
  was revised at 22:00:34 (sha `5323a8d36ada8addcbcba90e1a874e118bb7099720c345cd4974c7bed7418b67`)
  to rank `packet*` candidates with final names first (probed in-process:
  `find_packet` → the `-05` pair). My baseline pins bytes, not paths, so the
  pin survives either resolution.
- **G4 — packet iteration during the window (converged before freeze).** The
  twins moved at 21:47 → 21:52 → 21:55:57 (this seat measured all three
  states: gate 0/16 → 16/16; uncertainty 26 grammar findings → 0; links 34
  `E-EDGE-NO-CLAIM` → 0 at 40 then 50 links). Freeze happened only after the
  21:55:57 bytes had been stable ~13 min and were independently pinned by
  review-9, review-10 and the contract-audit re-run. The freeze's own
  double-measurement guard refuses to write on any movement.
- **Adjacent, out of this seat's claim:** the D-knowledge draft
  (`reports/round-15/knowledge/uncertainty-table-draft.md`) and the contract
  audit re-run exist and are cited by the packet; this seat judged neither.

## 6. What the baseline does and does not prove

- Proves: these exact committed bytes (baseline `b927db31…` + the 28 pinned
  inputs), under gate `e2fa3223…` and validators `f81bc9f7…`/`cdcc1931…`,
  produce exit 0 with 16/16 fields, 20/20 glossary entries, zero findings, a
  15-claim ledger typed 8/5/2 across supported/partial/unresolved, and 50/50
  resolving claim-to-record links; and that edits to the baseline, the read
  set, the gate, or the validators change the reading (s1–s10).
- Does not prove: that the packet is good design, that any claim inside it is
  true, that lore accepted anything, or that the round is complete — the
  round-12 audit's bilateral-acknowledgment and L0 items stay open with their
  named owners (`contract-v2-audit.md`); the digest is integrity, not truth
  (standard §10). All artifacts remain NON-CANON; freshness axis-move claims
  stay paused.
- Re-freeze protocol: any pinned input or the control tool changing makes the
  verdict invalid (reads `V2F-DIGEST`, exit 2) — re-freeze explicitly with
  `--freeze` and record the new stamp; never hand-edit `expected.json` (an
  edit is refused by the integrity digest, `V2F-BASELINE`, exit 2).

## Receipts

```sh
# 2026-10-17 21:36–22:11 -03, lane root, export TMPDIR=$PWD/.scratch
python3 reports/round-15/handoff/frozen-verify.py --freeze   # exit 0, baseline b927db31… (28 inputs)
python3 reports/round-15/handoff/frozen-verify.py             # exit 0, 16/16, 20/20, 15 claims 8/5/2, links 50/50
python3 reports/round-15/handoff/frozen-verify.py --selftest  # exit 0, 24/24 controls
python3 tools/check-gate-battery.py                           # exit 0 pre and post; baseline invisible
# scratch receipts (.scratch/r15o08/, gitignored): freeze.out, selftest.out ad22b322…,
# rerun-verify.out 500e5a3e…, rerun-freeze.out 24a26b36…, battery-pre.txt 10651aa3…,
# battery-post.txt 6701e2f4…, movement-watch-{1,2,3}.txt, copy-tree.sh
```
