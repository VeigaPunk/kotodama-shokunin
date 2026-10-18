# R18-D18 — reviewer 2/4: circularity — did the re-pin bless its own change?

- round: 18 (loop 2 of 3, build 2 of 4; 64 workers, `opencode-go-2/deepseek-v4.1-flash`),
  lane `kotodama-shokunin`, claim **D**.
- assignment (verbatim): "D R18-D17..D20 (reviewers x4): hold-set hand
  re-derivation; circularity (did the re-pin bless its own change?); cross-check
  vs D2/D3 lessons; SKILL/capability-row drafts; reports/round-18/d4/review-{1..4}.md."
- date: 2026-10-18, stamps UTC; evidence window 10:19:20Z–10:27:30Z; HEAD
  `c66ac3c951b346a2a56f9386e3324b4f5fe33902`.
- canon: NON-CANON engineering review; no clearance, no canon, no handoff.
- writes: **this file only** plus gitignored scratch `.scratch/r18d/`. Nothing
  under `examples/`, `tools/`, `reports/round-{8..17}/` was written. No commit.

## 0. Verdict

**On the evidence present at 10:27Z: the D4 expectation artifact is a
transcription of the tool it gates, and the D4 equality leg therefore has no
content teeth — only drift teeth.** The landed
`examples/culture-d4/expected-holds.json` equals the projector's live output
exactly, tuple for tuple including every `detail` string (measured, §2), and
carries no reconciliation, amendment or derivation key. Meanwhile the
pre-implementation locus in the delivered tree (`01-brief.yml` A-07) names six
holds, zero notes. The round has not yet said which authority the D4 baseline
rides on, so "findings exactly equal the expected set" cannot, as of this
stamp, discriminate between *the set is right* and *the set is a copy of the
thing that produces it*.

**On the re-pin procedure, the shape I could observe is correct** — the sibling
O11 arm re-pins by *digest-only substitution into a scratch copy of the manifest
while keeping the recorded verdict bytes at their round-11 values*
(`reports/round-18/gate/tests-1.md` §2; verified shape, not a re-run of their
experiment). That is exactly the shape the round-11 design demands (§1). The
circularity finding is about the **D4 expectation**, not about the re-pin
mechanics seen so far.

## 1. The doctrine this review applies

- `reports/round-11/depth/design.md` §5.2, "Circularity guard (D22's target)":
  "The freeze record must never be authored by the same step that decides the
  expectation… if a re-pin were used to bless a new hold, both the adapter's
  coverage check (§2.2) and L2's channel differential (§3.1) would have to move
  with it, and the reviewers can see that in the diff of two frozen revisions.
  **A re-pin that changes the hold set is reported as a finding, not a pass.**"
- `reports/round-11/depth/design.md` §4.2/§4.3: the D2 hold set was fixed as a
  *table in the design* (15 holds, 1 excluded note) **before** the file was
  written; §4.5 then writes `expected-holds.json` from the projector output
  with the constant asserted equal to the file in both directions. The file is
  a transcription **of an expectation already decided elsewhere** — that is what
  makes the transcription safe.
- `examples/culture-d3/expected.json` `declared_expectation`: "…fixed before
  tool implementation … hashes measured from actual inputs, **not generated
  from a printed verdict**."

## 2. Measurement — the landed D4 file is the emission verbatim

Commands (cwd = lane root, `TMPDIR=$PWD/.scratch`, 2026-10-18T10:23–10:25Z):

```sh
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json   # 16 findings
python3 - <<'EOF'  # .scratch/r18d/transcription-check.txt
... set/key comparison of the emitted findings against examples/culture-d4/expected-holds.json
EOF
```

| check | observed |
|---|---|
| expected rows vs emitted rows on `(id, severity, where, detail)` | **equal** — 16 vs 16, 0 only-expected, 0 only-emitted |
| counts | `{hold 15, note 1, fail 0}` in both artifacts |
| provenance keys in the landed file | `schema, packet_sha256, projection_sha256, projector_sha256, counts, holds, notes` — **no** reconciliation/amendment/derivation key |
| pins inside the file | `packet_sha256 e7ecd204…` = sha256(`packet.d4.yml`) ✓; `projection_sha256 a59990bb…` = sha256(`typed-labels.d4.yml`) ✓; `projector_sha256 0da0015f…` = sha256(`tools/d2-typed-labels.py`) ✓ |
| overlap with the round-17 frozen fragment (17+1, `D4L-*`, `GD-/AL-/RG-/SM-`) | **0 of 18** rows |
| occurrences in the D4 packet of the four rank rows' records | `TR-04` 0, `TR-06` 0, `WR-02` 0, `WR-08` 0, `WR-09` 0, `SR-01` 0 |

The pins verifying is *not* the problem — a pin is a hash, not an expectation.
The problem is that the **set** (ids, severities, `where` values, details) has
no author other than the tool: with the tool's own output as the only frozen
record, L3 checks the tool against itself. The D2 file is structurally
identical but semantically different: its set was decided by §4.2/§4.3 before
the file existed, and a reader can point at the decision.

## 3. The three circularity channels, and their status now

| channel | what it would look like | status at this stamp |
|---|---|---|
| **C-a: expectation-from-output** | the committed expected set has no locus predating the tool run | **present** for the 15/1 D4 file — the only predating locus, A-07, disagrees (6/0/0) and is undispositioned |
| **C-b: pin-from-output** | a pin computed from the artifact it certifies | present but benign: the projection pin and projector pin are plain digests of delivered bytes; the D2 idiom does the same |
| **C-c: re-pin blessing a changed hold set** | a re-pin that quietly moves the set | **not yet observable** — the generalization has not landed (gate still `d102fd1d…` at 10:27:30Z). The D4 file is by construction a *new* hold set relative to every earlier locus, so when the re-pin cascade lands, the diff between old and new frozen rows is the artifact a reviewer must read, and any set movement must be reported as a finding (doctrine §5.2), not absorbed |

## 4. Tests that give the gate teeth once the generalization lands

These are phrased as accept criteria for whoever reviews the landed O/D work;
they are cheap and none of them writes to a filed artifact:

1. **D2 byte-identity under the changed gate.** Re-run the three round-11
   invocations and compare stdout bytes to the pre-change shas measured here:
   default `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b`,
   frozen row `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606`
   (my runs; the second agrees field-for-field with `reports/round-18/d4/interop-1.md`
   §0). Any byte change on the default path is a claim-O regression.
2. **D4 drift teeth.** In a scratch mirror, tamper one held record in the D4
   typed packet (or one row of the typed projection) so that a hold's `where`
   moves; the D4 gate run must exit 1 on L3 and name the missing/extra row.
   Without this, the D4 leg could be passing because it never compares anything.
3. **Wrongness teeth — the test the gate cannot pass by design.** Add a
   *fabricated* hold named after a record outside the packet (e.g.
   `WR-02#g|WR-09#g`) to a scratch copy of the expected file; the gate will
   happily accept it if the D4 leg's constant/baseline is loaded from the same
   family of artifacts, because the fabrication is baked into both. This is why
   the *content* question must be answered by the reconciliation record
   (review-1 §5), not by the gate.
4. **New-row discipline for the cascade.** The round-11 row, the round-9
   baselines and the round-16 `v2-07` expected file must each be re-pinned as a
   **new row / new snapshot directory** with before/after digests; the filed
   rows stay as filed. The filed `typed-pipeline/run-receipt.json` and
   `run.log` (verified here: the round-11 row reproduces byte-identically,
   `cmp` vs `run.log` clean) must not gain a re-stamped digest in place.

## 5. A foot-gun worth recording (my own first reading was wrong)

`python3 tools/d2-typed-labels.py --check examples/culture-d4/typed-labels.d4.yml`
returns **exit 1, "differs from the deterministic projection"** — because
`--check` without `--packet` evaluates the **D2** packet
(`tools/d2-typed-labels.py:2873`, `PROJECTION_DEFAULT`), not the file's own
source. With the packet named —
`--packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml`
— it returns **exit 0, "byte-identical deterministic projection"**. Any
acceptance command or review that quotes a bare `--check` on a D4 file is
measuring the wrong pair; the D4 checks must always name their packet. This
matters for the round's counting command too.

## 6. Limits

- I did not run the O-arm's re-pin experiment; I read its documented shape and
  measured the baseline myself. When the generalized gate lands, channels C-c
  and the drift/negatives in §4 are the reviewer's first stops.
- "Circular" here is a statement about *evidence structure*, not about anyone's
  intent, and not a claim that the landed 15-hold set is wrong for the
  pipeline — the twelve label rows are genuine per-packet views (review-1 §4);
  the rank rows are the contested part.
- NON-CANON throughout.

## 7. Addendum — the reconciliation landed; post-change re-measurements (10:24–10:33Z)

- **§0's "no reconciliation … undispositioned" is superseded in part.**
  `reports/round-18/d4/holds.md` (landed 10:24:55Z) dispositions the deltas row
  by row against both the round-17 union and the delivered declaration, and
  routes the A-07 decision to the parent. The circularity *structure* measured
  in §2 is unchanged — the expected file is still the emission verbatim, tuple
  for tuple — but the round now carries a filed reconciliation whose §5 states
  plainly that the rank rows are D2's and packet-independent. Credit that
  record; read its §4.3 as the same finding as this review's §4(3).
- **The generalized gate's expected-holds leg is a self-consistency check, not
  a provenance check.** `tools/gates/typed-pipeline-gate.py:363-385`
  (`L1-expected-holds`) asserts schema, counts and list lengths agree inside the
  declared file, sets the L3 expectation from it, and leaves provenance alone.
  A set copied from the thing it gates passes this leg by construction, which is
  why channels C-a/C-c remain the ones to watch and why the reconciliation
  record is the only content authority the round has.
- **Post-change D2 byte-identity held at every revision measured**
  (`b4232690…`, `bba60bc1…`, `edfec5f3…`, `7fad95e0…`, `7a3bb816…`, all
  10:29–10:33Z): default stdout `15cdfbda…` and frozen-row stdout
  `9a69985a…`, both `cmp`-identical to the pre-change runs. Channel C-c shows no
  observable movement yet; when the D4 frozen row and the re-pinned round-11 row
  land, their diff is the artifact to read.
- **D4 run status at 10:33Z:** `ok L1-assembler`, `ok L1-expected-holds`,
  `FAIL L1-build: adapter missing: tools/assemble-d4-typed.py` (exit 2). The
  drift test (§4.2) and the wrongness test (§4.3) still await a D4 L3 that
  executes.
