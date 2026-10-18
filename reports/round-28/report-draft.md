# Round 28 — SCRIBE X52 report draft

**Scope:** independent settled-tree rerun plus this draft; only `report-draft.md` and
`rerun.json` are assigned to X52. **Measurement date:** 2026-10-18.
**Declared baseline:** `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede` (round-27 admit);
declaration HEAD `69cecbc7dcf575a29f29660ecac470e05260fd86` ("round-28: declare claims
D/O/C", 20:10:20Z). All executions ran in isolated clones under `.scratch/x52r28/` after
`export TMPDIR=$PWD/.scratch`. Counts below carry their commands and dates; full evidence
and per-command streams are in [`rerun.json`](rerun.json). This is a rerun record and an
integration draft, **not** a round-28 acceptance: the parent owns admission, shared
LOG/SCORECARD integration, and the final post-integration rerun.

## Summary

The round-28 counting command reads **D pass, C pass, O pass** —
`acceptance_checks_passed: true`, `missing_dependencies: []`. I reproduced that verdict
independently in **two** isolated overlay clones, and the filed receipt agrees with my read
on all three claims. This is the first round since the pin cascade began where all three
axes close green **and** the receipt binds the live runner bytes.

| claim | axis | state at close | reason |
|---|---|---|---|
| **D** | depth | **PASS** | the register law has a replay leg with teeth (RL-1 closed) and the RL-4 `packet_keys` gap is fixed |
| **C** | coverage | **PASS** | the ceiling is recorded as a §13 amendment and a new sourced entry; README revision 1.9 indexes it |
| **O** | operability | **PASS** | every current D4 surface re-pinned as a new row; the v3 baseline re-frozen against the final packet; battery 35/35 |

**The binding hazard is closed this round.** The round-28 runner was revised nine times
while the wave landed (`0a215dc4 → … → 20e09ea8`), then stabilised at `20e09ea8…` from
20:28:32Z. The final receipt (20:36:46Z) carries that same sha256, so unlike round 27 the
filed verdict **does** bind the live runner bytes — the round-20 lesson satisfied.

## Preservation — clean

`python3 .scratch/x52r28/capture.py protect` compared all **1,587** tracked filed paths
(`reports/round-{8..27}` plus `tools/gates/frozen/round-{8..27}`) to the declared baseline
at **20:11:25Z** and **20:34:28Z**: **0 mismatches** each time, identical manifest
`e169ce6c82c59da7…`, `protected_status` empty. The runner's own preservation leg agrees:
`protected_paths 1587`, `differences_total 0`, `passed true`. The surface grew from round
27's 1,460 to 1,587 because round 27 was admitted (`6c0ac44`) and its trees are now inside
the protected set.

## Regressions — 35/35 green in both clones

The round-27 runner's own `REGRESSIONS` tuple (35 commands), run in two overlay clones
(HEAD `69cecbc` overlaid with the settled live surfaces):

- battery selftest green; battery **pass 7 / fail 0 / unevaluable 0**, coverage 9/9, 19
  baselines pinned; assembly selftests 42/42, 85/85, 81/81; adapters 11/11, 12/12;
  replay 79/79; projector 163/163; typed-gate selftests 19/19 and 16/16;
- D2 gate 16/16, **D4 gate 20/20 legs** (the `L3b-argot` register leg present), D4 label
  gate exit 0, D4 assembly gate exit 0;
- argot gate selftest 27/27 and its D4 run exit 0
  (`records=183 register_scoped=14 derived_pairs=8 borrow_pairs=6 violations=0 rule_holds=0`);
- handoff v2 exit 0;
- **`handoff-v3` exit 0** — `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
  statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=a20ae059…` — and its
  selftest exit 0. Both were red in round 27; this is the O claim's headline repair.

## Claim D — depth: the law has a replay leg and RL-4 is fixed

**RL-1 is closed by a delivered checking leg, not a promise.** A new tool
`tools/gates/register-law-gate.py` (27,090 B) declares ten `D4L-LAW-*` finding classes and
resolves the law's own fields against delivered records. Its selftest is **33/33**, and it
names its own tamper controls (`delivered-force-tamper-adds-a-line`,
`delivered-speaker-tamper-adds-a-line`, `delivered-consequence-tamper-adds-a-line`).

I built my own three tampers independently of the runner's, editing exactly one named
field of the delivered packet text each, and measured the **line-level delta**:

```
clean packet       exit 1   classes {D4L-LAW-DANGLING: 4}
force tamper       exit 1   classes {D4L-LAW-DANGLING: 4, D4L-LAW-FORCE: 1}
speaker tamper     exit 1   classes {D4L-LAW-DANGLING: 4, D4L-LAW-SPEAKER: 1}
consequence tamper exit 1   classes {D4L-LAW-CONSEQUENCE: 1, D4L-LAW-DANGLING: 4}
```

Each tamper adds exactly one FAIL line of its own class over the clean set, and the clean
set carries zero of each FAIL class. **A tampered law row is now a named finding** — the
exact behaviour round 27's RL-1 measured as absent.

**A reading trap worth carrying forward.** The gate exits **1 on the clean delivered
packet**, by design. The four `design_row` tokens `QREG-05..08` cite sibling design seats'
proposed rows that never landed as packet records, so the gate emits four honest
`D4L-LAW-DANGLING` HOLDs and says so in its own calibration header: *"exit 0 here means
'every resolution the gate performs found nothing to report', not 'the law is complete'."*
The claim's teeth test is therefore the **delta**, never the clean packet's silence — and
the runner states the same grading rule. A reader who treats exit 0 as the only green will
misread this gate.

**RL-4 is fixed.** `03-orthography.yml` now declares
`packet_keys: [orthography, records, literacy_institutions]` and `09-costumes.yml` declares
`packet_keys: [costumes, materials, cloth_sources, rank_rules, form_slots, enforcement]`.
Measured on the live packet:

```
OR 3 ['OR-01','OR-02','OR-03']    LI 3 ['LI-01','LI-02','LI-03']
EN 2 ['EN-01','EN-02']            RGL 5 ['RGL-01'..'RGL-05']
```

Round 27's RL-4 measured these recorded under `assembly.skipped_keys` and visible to no
gate; they now reach the packet. Determinism holds (`d4-assembly`, `d4-adapter`,
`d4-projection` each exit 0) and the hold set carries a round-28 revision note naming both
the landing and the fix (`{hold: 12, note: 0, fail: 0}`).

**One follow-up, not a defect in the claim as declared:** the new gate is not in the
battery's registered set (`tools/gates/typed-pipelines.json`). Its 33/33 selftest and the
round-28 gate-tests runner are where the law leg is exercised. Worth registering in a later
round so the battery sweeps it.

## Claim O — operability: the pin cascade closes

**Every current D4 surface is re-pinned as a new row.** The round-28 sweep
(`reports/round-28/sweep/sweep-receipt.json`, `reports/round-28/pinsweep/d4-pins.json`,
seat R28-O25..O32) enumerates 121 surfaces and re-pins all eight drifted D4 surfaces:

```
repinned: 01-brief.yml, 03-orthography.yml, 04-lexicon.yml, 09-costumes.yml,
          expected-holds.json, packet.d4.typed.yml, packet.d4.yml, typed-labels.d4.yml
unrepinned: []
```

The live digests are `packet.d4.yml 543d68a8…`, `packet.d4.typed.yml 15c81ec1…`,
`typed-labels.d4.yml 339bfd83…`, `expected-holds.json 65f5a03e…`; the superseded rows
(`86079a67…` packet, `88a94422…` typed packet, both round-27 admits) stay byte-identical as
filed rows. The residual drift rows are **historical** generations pinning their own
revision's bytes — the append-only convention, not a defect.

**The v3 baseline is re-frozen against the final packet.** Round 27's one red was a D/O
sequencing problem: the D landing rewrote the packet the v3 read set pins, so `handoff-v3`
exited 1. Round 28 does what round 27's report-draft asked the parent to choose (option a):
`reports/round-28/pinsweep/v3-baseline-r28/expected.json` is frozen against the **final**
packet (`packet_sha256 a20ae059…`, matching the live handoff packet), the tool's default
pointer now names it, and `handoff-v3` exits 0. Its `freeze.txt` records the read set (58
files, component digests 26/26, d4 pins 8/8) and "no tracked value changed since the
previous freeze".

**A new frozen replay generation replays 4/4.** `reports/round-28/pinsweep/frozen/r28-post/`
(schema `kotodama-r28-d4-leg-freeze-v1`, 4 rows) replays clean:

```
REPLAY OK: 4/4 rows reproduced the recorded verdicts
```

It supersedes the round-18 and round-22 generations (which replay **MISMATCH 2/6**, the
round-27 X52-F1 defect) and extends the re-pin surface to the typed-pipeline gate's two D4
rows, which round 27's generation and this sweep's first pass had both left without a
successor (round-28 audit X61 finding X61R28-A2). The two historical MISMATCH generations
remain filed and are the append-only convention; a reproduced red verdict stays red.

## Claim C — coverage: the ceiling becomes craft knowledge

`corpus/knowledge/linguistics/register-strata-attestation.md` gains **§13. Amendment
(round 28): the register-lexicon ceiling, re-measured, with its mechanism** — a new section,
not an in-place rewrite: `git diff --numstat` reads `123 0`, and the section-header count
moves 12 → 13 with the prefix preserved (bytes 57,996 → 64,928).

A new entry `corpus/knowledge/linguistics/register-lexicon-ceilings.md` (34,400 B) landed
frontmatter-complete (topic, gap filled, sources, couples, source, verified-at, recheck),
gap-named (a five-grep absence sweep each returning 0), and carrying its craft lesson —
**a register's derivation operation constrains which semantic fields it can natively
spell**. It cites repo artefacts and external literature (Dixon, Halliday, Gotowski,
Aronoff, Bauer, Labov, Irvine & Gal) and makes no canon claim.

The ceiling instrument (`reports/round-28/ceiling/measure-ceiling.py`, selftest **10/10**)
re-derives the round-27 measurement and states the mechanism:

```
population: mark-axis plain words = 27
delivered gate  legal=19 illegal=8      filed round 27: legal=18 illegal=9 (pre-fix reader)
delta vs delivered: {L-45}
mechanism: reverse is legal <=> the base-initial consonant is a licensed coda -> True (27/27)
  onsets=14 codas=8 never-coda=b,g,h,j,p,w
```

Four of the five legal/institutional abstractions (`L-15 wer`, `L-30 gis`, `L-44 wad`,
`L-51 gul`) refuse `reverse`; only `L-45 tikmes` is legal — and it became legal precisely
because the gate's legality predicate was fixed, which is why the count moved 18→19. The
ceiling is real, re-measured, and now generalised as a design constraint.

`corpus/README.md` is **revision 1.9**; the readme sweep reproduces the measured tree:
linguistics 21 (was 20), civilizations 94, culture-material 18, myth-symbol 19, synthesis
29, verification 20 — 201 rows / 201 files, `missing_from_index 0`, `topic_mismatch 0`,
`orphan_rows 0`, `totals_ok True`, `footer_ok True`.

## What the parent should weigh

1. **All three axes close green, and the receipt binds the live runner.** Unlike round 27,
   the runner stopped moving before the receipt landed. The verdict is reproducible: I read
   it twice in independent clones.
2. **D is the strongest part of the round, and its shape is unusual.** The law now has a
   delivered checking leg with a 33/33 selftest and three working tamper controls — but the
   gate exits 1 on the clean packet by design. Admit the claim on the **delta**, and carry
   the exit-1-by-design fact into any LOG/SCORECARD wording so a later reader does not read
   the clean exit as a red.
3. **O closes a two-round-old interaction.** The v3 baseline is now frozen against the
   *final* packet, so the sequencing trap round 26 and round 27 both hit is closed for this
   round — but it will reopen the moment a later D landing rewrites the packet again. The
   discipline is "freeze the v3 baseline after the D landing settles", and it belongs in the
   round ritual, not in one round's heroics.
4. **X52-F1 (round 27) is now superseded, not merely reported.** The r28-post generation is
   the successor the round-27 report asked for. The historical MISMATCH generations stay
   filed, by convention.
5. **Two small follow-ups.** The register-law gate is not in the battery's registered set;
   and the round-26 `gate-input` generation still replays MISMATCH 2/6 (now superseded by
   r28-post but not removed — correctly, it is a filed artifact).

## Limits

- The runner was revised nine times while the wave landed; my independent reads are bound to
  the runner sha256 named in each `rerun.json` entry, and the filed receipt is another
  seat's. My read agrees with it claim for claim.
- The battery measures overlay-clone bytes; four round-28 files moved between my two
  checkpoints (three scribe artifacts and `validation.json`; the runner did not).
- The preservation sample is a tracked-bytes-and-modes comparison at two stamps; it does not
  exclude a transient write-and-restore between them.
- The frozen replay legs required TMPDIR outside the repository; the lane's prescribed
  `TMPDIR=$PWD/.scratch` makes every row `mirror_unsafe` and cannot evaluate any frozen row.
- My law tampers are my own text edits; the runner builds its own three independently. The
  two agree on the delta classes; neither is a design quote.
- The ceiling instrument's pre-fix reader is a labelled reconstruction (the pre-fix gate
  declares no legality predicate), and it is labelled as one wherever it is used.
- NON-CANON engineering evidence: no source-freshness certification, rights clearance, lore
  acceptance or promotion is claimed.
- No commit, no push, no shared bookkeeping, no filed round-8–27 write by this seat.

Scratch: `.scratch/x52r28/{capture.py,protected-initial.json,checkpoint-a,checkpoint-b,-capture.json,-results.json,-runs/,tamper/}`,
`.scratch/x52r28-commands.json`, `.scratch/r28-ceiling.json`, and the outside-repo probe
root `/tmp/x52r28-replay`.
