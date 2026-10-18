# Round 27 — SCRIBE X52 report draft

**Scope:** independent settled-tree rerun plus this draft; only `report-draft.md` and
`rerun.json` are assigned to X52. **Measurement date:** 2026-10-18.
**Declared baseline:** `4f09c990d4c17f23b5e2cda0871f81db875635fc` (round-26 admit);
declaration HEAD `b95fca1e40f32f7346937ab6426f9ccca60e319f` ("round-27: declare claims
D/O/C", 19:11:04Z). All executions ran in isolated clones under `.scratch/x52/` after
`export TMPDIR=$PWD/.scratch`. Counts below carry their commands and dates; full evidence
and per-command streams are in [`rerun.json`](rerun.json). This is a rerun record and an
integration draft, **not** a round-27 acceptance: the parent owns admission, shared
LOG/SCORECARD integration, and the final post-integration rerun.

## Summary

The tree is **operationally green on the filed surface** and the round-27 counting command
reads **D pass, C pass, O fail**. I reproduced that verdict independently in three isolated
overlay clones, and the filed receipt agrees with my read on all three claims.

| claim | axis | state at close | reason |
|---|---|---|---|
| **D** | depth | **PASS** | the register law landed as an owned component; the gate's `syllabify` is fixed and agrees with the design on every delivered form |
| **C** | coverage | **PASS** | `register-strata-attestation.md` landed frontmatter-complete and gap-named; `corpus/README.md` revision 1.7 indexes it |
| **O** | operability | **FAIL — one leg** | the D landing rewrote the D4 packet, so handoff-v3's v3 read-set baseline drifts; the pin sweep itself is otherwise clean (140 green / 92 historical drift / 0 un-re-pinned) |

## Preservation — clean

`python3 .scratch/x52/capture.py protect` compared all **1,460** tracked filed paths
(`reports/round-{8..26}` plus `tools/gates/frozen/round-{8..26}`) to the declared baseline
at **19:12:34Z**, **19:16:10Z**, **19:18Z** and **19:28Z**: **0 mismatches** each time,
identical manifest `e408361bcc3c5318…`, `protected_status` empty. The round-27 runner's own
preservation leg agrees: `protected_paths 1460`, `differences_total 0`, `passed true`. The
round-27 watch seat (X51, `reports/round-27/scope.md`) reaches the same count independently.

## Regressions — 34/35 green; the one red is the O failure

The round-26 runner's own `REGRESSIONS` tuple (35 commands), run in the checkpoint-d overlay
clone (HEAD `b95fca1` + live surfaces after the D/C landing):

- battery selftest **35/35**; battery **pass 7 / fail 0 / unevaluable 0**, coverage 9/9, 19
  baselines pinned;
- assembly selftests 42/42, 85/85, **81/81**; adapters 11/11, 12/12; replay 79/79;
  projector **163/163**; typed-gate selftests 19/19 and 16/16;
- D2 gate **16/16**, **D4 gate 20/20 legs** (including the new `L3b-argot` leg), D4 label
  gate exit 0, D4 assembly gate exit 0;
- **argot gate selftest 27/27** (was 21/21 before the syllabify fix) and its D4 run exit 0
  (`records=175 register_scoped=14 derived_pairs=8 borrow_pairs=6 violations=0 rule_holds=0`);
- handoff v2 50/50 links, exit 0;
- **`handoff-v3` exit 1** — `E2E-DIGEST: 5 read-set file(s) changed since the baseline was
  frozen` (`01-brief.yml`, `expected-holds.json`, `packet.d4.typed.yml`, `packet.d4.yml`,
  `typed-labels.d4.yml`). This is the O failure, below.

## Claim D — depth: the register law landed and syllabify is fixed

**The law is owned and machine-readable.** A new component
`examples/culture-d4/components/13-register-law.yml` (8,870 B) declares five speech-act rows
`RGL-01..05`; the runner measures `component_ids == packet_ids` and `rows_equal: true`, so
the packet's law rows are that component's rows id for id. The three clauses the claim names
are all present — `admissibility`, `agent`, `consequence` — over 5 speech-act rows and 9
total register rows, every one carrying the universal fields (`id`, `axis`, `evidence`,
`follows`); `law_text_bytes` 3,178. The packet now carries **14** `RGL`/`QREG` tokens (was
0 `RGL` at the start of this round).

**The syllabify disagreement is fixed.** The gate now implements the design's stated
legality-constrained maximal onset, and it agrees with the design reading on every delivered
form. Measured directly:

```
tikmes  ['tik','mes']      kalker  ['kal','ker']      tumhai  ['tum','ha','i']
saalumi ['saa','lu','mi']  haitun  ['ha','i','tun']   mesar   ['me','sar']
```

`head2(saalumi) = saalu` still reproduces (the design's one worked row). The runner's own
independent re-derivation finds zero disagreements and zero illegal syllables, with the
pre-fix reading as its control.

**Determinism holds.** The assembler, typed adapter and projector each regenerate their
artefact byte-for-byte (`d4-assembly`, `d4-adapter`, `d4-projection` all exit 0), and the D4
typed gate is 20/20 with the register leg present. The hold set carries a round-27 revision
note whose counts agree with the projection: `{hold: 12, note: 0, fail: 0}` over
`labels_by_kind {native-form 64, translated-label 12, borrowed-strata 6}`, `findings_total 12`.

**What I measured before the landing, for the record.** At 19:18Z the law was design-only:
`grep -c 'RGL-0' examples/culture-d4/packet.d4.yml` → 0, and the peer auditor R27-X59's own
instrument emitted `L6 HOLD — the register block declares the register IDENTITY (QREG-*) but
no speech-act law rows (RGL-01..05)`. The landing closed exactly that gap. Two rounds of this
seat's own measurement — one pre-landing, one post — are both recorded in `rerun.json` so the
delta is auditable rather than asserted.

## Claim C — coverage: the entry landed and the README is reconciled

`corpus/knowledge/linguistics/register-strata-attestation.md` (54,284 B) landed
frontmatter-complete (`topic`, `sources`, `verified-at`, `recheck`, `couples`), gap-named,
and decision-record carrying. Its gap statement is a measured absence sweep (five
`grep -rl … | wc -l` commands each returning 0 over `corpus/knowledge/` minus the entry),
and its source block distinguishes repo artefacts (by digest) from external literature. It
makes no canon claim.

`corpus/README.md` is now **revision 1.7**, names the entry, and its partition arithmetic
reproduces the measured tree: linguistics 20 (was 19), civilizations 94, culture-material 18,
myth-symbol 19, synthesis 29, verification 20 — 200 files, zero mismatches. The readme
sweep (`reports/round-27/readme/sweep.py`) is green on the same numbers.

## Claim O — operability: one leg red, and it is a D/O interaction

**The pin sweep is otherwise clean.** The runner's own sweep reads **232 rows naming a D4
surface: 140 green, 92 historical drift, 0 un-re-pinned**. All six current D4 surfaces are
re-pinned by round-27 rows carrying the live digest:

```
repinned: 01-brief.yml, 04-lexicon.yml, expected-holds.json,
          packet.d4.typed.yml, packet.d4.yml, typed-labels.d4.yml
unrepinned: []
```

The 92 drifted rows are the **historical** round-18/22/25/26 generations, which correctly
pin the bytes of their own revision — that is the append-only convention, not a defect.

**The one failure is `handoff-v3`, and it is structural.** The D landing rewrote the D4
packet (`dd25077b…` → `86079a67…`), which invalidates the v3 read-set baseline the tool
reads by default:

```
v3_baseline: path reports/round-26/handoff/declared-in-r5/expected.json
             declared_packet_sha256 e3fb1ca500d62981b59129f898ef7e4b2843b1fa5ab7d12e8fc16818d1f764b8
             live_packet_sha256     86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc
             reading: drift
```

The O seat has frozen a round-27 successor at `reports/round-27/pinsweep/v3-baseline-r27/`,
but **against the pre-law packet** (`packet_sha256 e3fb1ca5…` — the round-26 register
packet, per its own `freeze.txt`), so it does not close the drift either. This is the same
D/O interaction round 26 hit and reported: the D seat's write to `examples/culture-d4/`
invalidates the O seat's baseline within minutes, and no O seat can freeze a baseline that
survives a later D landing. It is a sequencing problem, not a broken instrument.

**Disposition for the parent.** Either (a) re-freeze the v3 baseline as a round-27 row
against the final packet `86079a67…` **after** the D landing is frozen, or (b) declare the
v3 read-set baseline order-dependent and record the drift as a named consequence of the D
landing. What should not happen is admitting O on a receipt whose own v3 leg reads exit 1.

## X52-F1 — a round-26 filed green that does not reproduce

Independent of the round-27 verdict, I found and report a defect on the surface claim O
exists to sweep:

```
TMPDIR=/tmp/x52-replay python3 tools/replay-frozen.py tools/gates/frozen/round-26/gate-input/MANIFEST.tsv
ROW 2 mismatch input=examples/culture-d4/packet.d4.yml  exit=2/0  count=0/12  bytes=differ
ROW 3 mismatch input=examples/culture-d4/packet.d4.typed.yml  exit=2/0  count=0/12  bytes=differ
REPLAY MISMATCH: 2 mismatch, 4 reproduced of 6
```

- the pinned snapshot is the **pre-register** packet
  (`e7ecd2045ef0e5f9…`, byte-identical to `git show fc13cd2:examples/culture-d4/packet.d4.yml`);
- replaying it through the live gate reads **exit 2, FAIL L1-assembler** — *"packet bytes
  e7ecd2045ef0 are not tools/assemble-culture-d4.py's deterministic assembly (dd25077bc016)"*;
- the recorded output `d4-source.out` (`5b67905b67ca…`) equals neither the live run
  (`3eb9042e0664…`) nor the snapshot's run — a third artefact;
- the sibling generation `tools/gates/frozen/round-26/post-register/` pins the live packet
  and replays **6/6 reproduced**. One round, one correct generation and one defective one.

This is the round-26 mid-window freeze the round-26 report-draft already named, left
un-superseded. **Disposition: re-pin `tools/gates/frozen/round-26/gate-input` as a NEW
generation; never edit the filed bytes.**

**An operational trap worth carrying forward.** `tools/replay-frozen.py` refuses an in-repo
temporary mirror root as `mirror_unsafe`, so the lane's prescribed `TMPDIR=$PWD/.scratch`
makes **every** frozen row `could-not-evaluate`. Measured: the round-26 post-register
manifest reads `6 could-not-evaluate, 0 reproduced` under the in-repo TMPDIR and `6/6
reproduced` under `TMPDIR=/tmp/…`. A sweep that stops at that precondition reports "0
mismatch" and means nothing.

## What the parent should weigh

1. **D and C are the strongest part of this round.** The law is a real owned component with
   id-for-id packet agreement, the syllabify fix is measurable form by form, and the coverage
   entry is gap-named with a reproducible absence sweep. I reproduced all three independently.
2. **O fails on one leg, and the leg is a sequencing problem, not a broken instrument.** The
   v3 baseline must be re-frozen against the *final* packet after the D landing settles —
   otherwise every D landing re-reds it.
3. **X52-F1 should be dispositioned in round 27, not carried.** It is exactly the kind of
   filed green a pin sweep exists to find.
4. **Carry the outside-repo TMPDIR** into any round-27 O replay, or the sweep will report a
   meaningless "0 mismatch".
5. Where this seat overlaps the peer auditors (preservation, the law gap pre-landing, the
   syllabify figures, the pin drift) we agree; the only difference is the exact syllabify
   count I reported mid-round (12 by my port, 15 by the round-26 port), which the landing
   has since made moot.

## Limits

- The runner landed mid-window (19:20:34Z) and was still being revised while I measured; my
  independent reads are bound to the runner sha256 named in each `rerun.json` entry, and the
  filed receipt is another seat's.
- The battery measures overlay-clone bytes; the live tree kept moving after each stamp.
- The preservation sample is a tracked-bytes-and-modes comparison at four stamps; it does not
  exclude a transient write-and-restore between them.
- My pre-landing D and O measurements describe a tree that no longer exists; they are kept as
  the auditable delta, never as the verdict.
- NON-CANON engineering evidence: no source-freshness certification, rights clearance, lore
  acceptance or promotion is claimed.
- No commit, no push, no shared bookkeeping, no filed round-8–26 write by this seat.

Scratch: `.scratch/x52/{capture.py,syl-indep.py,syl-indep.json,syl-corrected.py,pin-sweep.py,pin-sweep.json,protected-initial.json,checkpoint-a..e/,-capture.json,-results.json,-runs/}`,
`.scratch/x52-commands.json`, and the two probe receipts `/tmp/x52-r27{a,b,c,d,e}.json`.
