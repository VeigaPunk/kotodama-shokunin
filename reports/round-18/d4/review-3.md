# R18-D19 — reviewer 3/4: cross-check against the D2/D3 lessons and the round-11 doctrine

- round: 18 (loop 2 of 3, build 2 of 4; 64 workers, `opencode-go-2/deepseek-v4.1-flash`),
  lane `kotodama-shokunin`, claim **D**.
- assignment (verbatim): "D R18-D17..D20 (reviewers x4): hold-set hand
  re-derivation; circularity (did the re-pin bless its own change?); cross-check
  vs D2/D3 lessons; SKILL/capability-row drafts; reports/round-18/d4/review-{1..4}.md."
- date: 2026-10-18, stamps UTC; evidence window 10:19:20Z–10:31:00Z; HEAD
  `c66ac3c951b346a2a56f9386e3324b4f5fe33902`. The O-seat's generalized gate was
  **landing while this file was written** (sha `d102fd1d…` before 10:29Z,
  `b4232690…` at 10:29:11Z, `bba60bc1…` at 10:29:43Z) — every post-change
  reading below names its gate sha.
- canon: NON-CANON engineering review; no clearance, no canon, no handoff.
- writes: **this file only** plus gitignored scratch `.scratch/r18d/`. No commit.

## 0. Verdict

**The D2/round-11 protections hold up under measurement; the D4 leg is
half-landed and must not be read as complete.** The default D2 gate path is
byte-identical through the generalization (measured, §2), the D2/D3 assemblers
are byte-identical green, and the round-11 frozen row reproduces exactly. The
D4 arm of claim D, at this stamp, is **not executable end-to-end**: the D4
packet fails L1 at the D2 identity leg, and the D4 pipeline's own typed packet /
adapter do not exist, so the L3 equality the claim promises has no product to
grade yet. The reconciliation artifacts (hold set, derivation, delta
dispositions) are in place and honest; the instrument that was supposed to read
them is still moving.

## 1. The lesson set applied

| id | lesson (source) | requirement being checked |
|---|---|---|
| L-D1 | R17 lesson §Gate-D 1; D3 `expected.json` `declared_expectation`; `design-brief.md` §7.2 rule 1 | the hold set is a pre-registration with a checkable ordering: named before implementation, amendments recorded, never a silent post-run edit |
| L-D2 | R17 lesson §Gate-D 2; design `§4.4(2)-(3)` | "exactly equal" is set equality on `(id, severity, where)` **with details pinned**; a laundered/renamed/deleted hold fails |
| L-D3 | R17 lesson §Gate-D 3 | determinism is a twice-run byte comparison on delivered bytes |
| L-D4 | R17 lesson §Gate-D 4; `frozen/round-11/README.md` | replay green names the manifest, the digests and the date; a later edit invalidates the row until a new dated receipt re-freezes it |
| L-D5 | R17 lesson §Gate-D 5 | d2/d3 "untouched" is byte equality against pinned digests; "green" is the two assembler `--check` commands |
| L-D6 | R17 lesson §Gate-D 6 | NON-CANON wording: exit 0 is a structural pass with open holds, never a clearance |
| L-D7 | R17 lesson §Gate-D 7 | the typed-channel rule is exercised on D4's own routed set, not inherited |
| L-D8 | R17 lesson §Gate-D 8 | twelve components: declared partition, collision refusal, fail-closed before any write |
| L-D9 | R17 lesson §Gate-D 9 | round-13's interrupt is before-state; no retroactive credit |
| L-R11 | design §5.2 circularity guard; §4.5 committed-baseline idiom; §8.4 detail-pinning trade-off | freeze record never authored by the step that decides the expectation; detail pinning is deliberate and re-pins are explicit |
| L-R12/14/15 | rounds 12/14/15 lessons | receipts are append-only; the receipt guard exists; moved bytes are superseded, never silently inherited |

## 2. Findings, by lesson

**L-D1 — pre-registration: present, exercised, and *permissive by rule*.** The
locus exists and predates the tool run: `01-brief.yml`
`contract.hold_set_declaration` (`:195-208`, A-07 `:224`, delivered bytes sha
`a2bc3111…`, named 2026-10-18), plus `design-brief.md` §7.1/§7.2 and the frozen
fragment (`reports/round-17/d4/expected-holds.fragment.json`, A-19-1). The
landed file deviates from the delivered-tree declaration (+9 holds, +1 note,
`D2L-*` spelling) and `reports/round-18/d4/holds.md` §3/§4 dispositions every
delta — including the honest statement that "the declared '0 notes' cannot hold
for any packet through this projector" (§4.3). What a reviewer should notice is
the *rule* that licensed the spelling change: `typed-support-2.md:80-88` — "The
expected file must carry **exactly the ids the delivered D4 projector emits** …
The contract is the equality, not the spelling." That rule was written in
round 17, by the design seat, predicting the emitted vocabulary
(`typed-support-1.md:190-192` pre-authorizes the `D4L-*` → `D2L-*`
substitution). So the substitution is pre-registered, not post-hoc — **but the
same rule is a blank cheque for set *content***: read literally it says any set
the projector emits is the contract. The remedy is not to delete the rule but to
bound it: it may license *renames of records the design named*, never the
addition of classes the design did not name. The four D2 rank rows entered under
that blank cheque (holds.md §5 attributes them correctly, but the file still
carries them as D4 expectations).

**L-D2 — set equality with pinned details: satisfied mechanically, and the
details question is decided by transcription.** `examples/culture-d4/expected-holds.json`
pins all 16 `detail` strings, and they are the projector's strings verbatim
(measured: 0 only-expected / 0 only-emitted on the 4-tuple key; review-2 §2).
The round-17 placeholder (`"detail": null`, fragment `derivation` note) is
superseded. This is the design's own trade-off (`§4.4(3)`, §8.4: "a prose
rewrite re-pins the baseline explicitly") — with the difference that for D2 the
prose came from a design table, while here it came from the tool. The four
cancel by construction, so nothing is broken; but "details pinned" should not be
reported as independent verification of the D4 set.

**L-D3 — determinism.** Measured here: two fresh D4 emissions
(`--packet examples/culture-d4/packet.d4.yml --emit …`) are byte-identical
(`cmp` clean); the committed projection is a byte-identical regeneration of the
delivered bytes (`--packet … --check …` exit 0, gate sha independent); the D2
default path is byte-identical twice (see §3). Not yet measurable: the D4 gate
run itself, which does not execute at this stamp.

**L-D4 — replay-frozen.** The round-11 row reproduces **byte-identically**:
`python3 tools/gates/typed-pipeline-gate.py tools/gates/frozen/round-11/typed-pipeline/packet.d2.typed.yml`
→ exit 0, stdout sha256 `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606`,
`cmp` against `tools/gates/frozen/round-11/typed-pipeline/run.log` clean — equal
to the receipt's `stdout_sha256` and to `reports/round-18/d4/interop-1.md` §0.
That statement is true at gate sha `d102fd1d…` **and at the generalized sha**
(§3). The D4 frozen row/manifest for round 18 had not landed at my last stamp;
the re-pin discipline (L-D4 + `scribe-1.md`: row 1 of the round-11 manifest pins
the *pre*-change gate, so the re-pin is the O-seat's declared target) is the
thing to check when it lands — row added, never substituted in place.

**L-D5 — d2/d3 untouched and green.** Measured 10:22Z:
`python3 tools/assemble-d2.py --check` → exit 0 "packet.d2.yml: byte-identical
deterministic assembly"; `python3 tools/assemble-culture-d3.py --check` → exit 0
"byte-identical deterministic assembly" (both files); D2 tool pins equal the
round-11 receipt (`d102fd1d`-era: projector `0da0015f…`, adapter `c7e5a749…`,
serializer `8ea6bdde…`); `git status --porcelain` clean at every measurement.
The packer's own D4 analogue is also green: `assemble-culture-d4.py --check`
exit 0.

**L-D6 — NON-CANON.** No clearance claim in any landed round-18 artifact I read;
the expected file carries no canon key. The one wording risk is the *round table*
that will eventually say "D4 gate exit 0": the gate banner's own discipline
("exit 0 is not a clearance; every hold below is still open design debt")
travels with the D2 path and must travel with the D4 path too — a checker should
assert the D4 run prints the banner and the holds verbatim.

**L-D7 — the channel rule on D4's routed set: not yet exercised, and it needs
a product that does not exist.** The D2 L2 leg needs a legacy/typed pair with a
declared routed set (10 `GAR-*` records). For D4 the analogue requires
`examples/culture-d4/packet.d4.typed.yml` (absent) and an adapter
`tools/assemble-d4-typed.py` (absent; `holds.md` §7.1 records both as
"not landed", `ASSEMBLY.md:69-77` as "pending"). The D4 projection's own
`typed_channel` equivalent is the routing the adapter would write. **This is the
structural piece of claim D that no artifact in the tree yet carries** — and it
is the piece that makes the six owed-slot holds *routed* rather than merely
emitted. Until it lands, "the generalized gate runs over
`examples/culture-d4/packet.d4.yml`" cannot be a full pipeline statement; at
best it is an L3/L4 statement over the projector's output.

**L-D8 — twelve components, fail-closed.** The D4 assembler's contract is
delivered and green (`--check` exit 0 on the delivered tree; round-17 recorded
81/81 selftest controls; the packet's `assembly` block names
`sources`/`skipped_keys`/`normalizations`). The era-shape normalization is
recorded in the packet's own `assembly` block, which is the round-16
"re-freeze after a canonicalization divergence" lesson applied correctly.

**L-D9 — round-13 skip.** Unchanged: no round-13 artifact is cited as D4 work
by any artifact I read.

**L-R11 — the freeze/expectation separation.** Covered in review-2; the D4 file
is authored by the same step that decided its content. The design's own guard
says a re-pin that changes the hold set is "reported as a finding, not a pass" —
for D4 *the whole file is new*, so the finding is the reconciliation itself
(holds.md), and it is filed. That is the right shape; the parent should now
decide the open question holds.md §7.3 routes (supersede A-07 or re-declare the
component), because until then two delivered artifacts disagree about the D4
debt and neither is edited.

**L-R12/14/15 — append-only and moving bytes.** The landed expected file is a
*new* file for a new family; the round-17 fragment is untouched (new bytes were
not written into it); the round-11 manifest/receipt are untouched; the round-17
packet copy under `reports/round-17/tests/frozen/` is pre-normalization and is
now a stale *record*, which `scribe-1.md` §0 row 2 flags rather than repairs.
That is the round-15 lesson followed.

## 3. Post-generalization measurements (gate sha `b4232690…` then `bba60bc1…`)

The O-seat's generalization landed at 10:29:11Z and kept moving (10:29:43Z).
Measured against it immediately (cwd = lane root, `TMPDIR=$PWD/.scratch`):

| command | observed |
|---|---|
| `sha256sum tools/gates/typed-pipeline-gate.py` | `b423269017523a08f1fb74d6ae6409a732e01bc3d76394400e29ccd8c6bcf24f` (10:29:11Z) then `bba60bc18ebc128223f933b1495edfea059df923ab1b2e3872e617d13efa8409` (10:29:43Z, 35200 bytes) — **the file was still being written** |
| default D2 path (post-change) | exit **0**, stdout sha `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b` — **byte-identical to the pre-change run** (measured twice, `cmp` clean), 16/16 legs |
| round-11 frozen row (post-change) | exit **0**, stdout sha `9a69985a…ada4606` — byte-identical to the recorded `run.log` |
| `--selftest` (post-change) | exit 0, **12/12** — the D4 additions named in `tests-1.md` §6 were not in this revision |
| D4 path `typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit **2**, `FAIL L1-assembler_identity: packet bytes are not assemble-d2.py's deterministic assembly (e7ecd2045ef0 vs e0f21509e14a)` — the resolver and the docstring's declared-pin story are in, but the CLI flags (`--assembler/--projection/--expected`) were not yet registered (`argparse` rejected them: "unrecognized arguments") and no D4 adapter exists |

So at 10:30Z: **the O half of the protection is demonstrated and the D half is
not.** The D2/round-11 legs are byte-identical; the D4 legs (gate run, D4 frozen
manifest, D4 channel leg) have no execution to point at yet. `tests-1.md` §6
names exactly the right three re-runs for the O side; the D side needs its own
three: D4 gate run exit 0 with the banner + 15 holds, D4 frozen row replay, and
the D4 routed-set channel leg (L-D7).

## 4. Limits

- Post-change readings are pinned by sha because the gate file was mid-write; a
  later revision supersedes them (round-15 lesson) and the reviewer who lands
  after this seat should re-measure rather than quote this section as current.
- I did not run the round-18 validation runner (not landed at my last stamp;
  and running another seat's counting command is not my leg).
- NON-CANON throughout; nothing here is a clearance or a canon statement.
