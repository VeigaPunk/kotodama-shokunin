# Gate frozen-run standard — the two-evidences clause for this lane

- topic: How kotodama-shokunin satisfies the fleet gate standard's two-evidences clause: every gate in `tools/gates/` ships a self-test (capability) AND a frozen run (measurement) — a run over a committed input snapshot with a committed, digest-pinned expected verdict that a later hand-edit contradicts; the layout under `tools/gates/frozen/`, the freeze/verify procedure, and a worked example measured on `myth-consistency-gate`.
- sources:
  - KTD-FR-S-0001 — fleet `PROTOCOL.md` §“Gate standard” (the two-evidences bullet) and §“Evidence standard” (resolvable pointers, claimed ≠ re-executed); read-only fleet surface at the fleet root (`../PROTOCOL.md`). The lane's *registry home* for gate rows is its own `SKILL.md` §Gates. Line numbers are pinned in the fleet appendix, not here.
  - KTD-FR-S-0002 — fleet `PROTOCOL-APPENDIX.md`, row “Frozen inputs” (rounds 12–13): round-12 `expected.json` pinned only the debt set, so flipping a status inside `frozen/post/MANIFEST.json` still read `baseline: match`, exit 0 (identified as labrat H2); round-13 baselines pin every input digest and an edit reads `snapshot_tampered`, exit 2; three round-12 baselines remain `unpinned (legacy)`.
  - KTD-FR-S-0003 — fleet `PROTOCOL-APPENDIX.md`, row “Gate standard” (round 12): a gate that grades the tree it runs against flipped FAIL→PASS when the lane landed its evidence — why a verdict must name its revision and a frozen input must be a copy, not a live path.
  - KTD-FR-S-0004 — `corpus/knowledge/verification/verification-method-overview.md` §3 (rule locator must preserve the reviewed file version or digest), §6 (fail-closed verdicts: UNKNOWN is not PASS), §8 (reference/design clock: a proposal version is a clock), §10 step 1 (freeze the proposed input packet and the corpus rule version).
  - KTD-FR-S-0005 — `corpus/knowledge/synthesis/worldbible-integration-contract.md` §4 (“Freeze the manifest before review; changing a referenced file invalidates that delivery's digest even if its filename stays unchanged”) and §9 (pinned versions, no auto-upgrade). Digest of the file as read: `sha256:50c4c2f2…8fb7268c1`.
  - KTD-FR-S-0006 — NIST (2015). *Secure Hash Standard (SHS)*, FIPS PUB 180-4. National Institute of Standards and Technology. [PDF](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf). Defines SHA-256; cited for digest construction only, not as a truth measure for content.
  - KTD-FR-S-0007 — Thompson, Ken (1984). “Reflections on Trusting Trust.” *Communications of the ACM* 27(8): 761–763. DOI 10.1145/358198.358210. The verifier belongs to the trusted base: a digest proves the bytes, never the tool that reads them.
  - KTD-FR-S-0008 — Reproducible Builds project. “Reproducible Builds — a set of software development practices” documentation, [reproducible-builds.org/docs/](https://reproducible-builds.org/docs/) (accessed 2026-10-17). Deterministic re-execution is what makes a recorded verdict re-checkable by a stranger.
  - KTD-FR-S-0009 — Stevens, Marc, Elie Bursztein, Pierre Karpman, Ange Albertini, and Yarik Markov (2017). “The first collision for full SHA-1.” In Jonathan Katz and Hovav Shacham (eds.), *Advances in Cryptology – CRYPTO 2017*, Proceedings, Part I, pp. 570–596. Springer, Cham. [DOI: 10.1007/978-3-319-63688-7_19](https://doi.org/10.1007/978-3-319-63688-7_19); [shattered.io](https://shattered.io/). Grounds the ban on MD5/SHA-1 pins below; it is not a claim that SHA-256 is unbreakable.
  - KTD-FR-S-0010 — Chacon, Scott, and Ben Straub (2014). *Pro Git*, 2nd ed. Apress. [Official text](https://git-scm.com/book/en/v2). Git addresses content, not paths: a commit hash pins bytes; a path alone pins nothing.
- couples: gates and fixtures — `tools/gates/*.py`, `tools/gates/fixtures/`; gate specifications — `corpus/knowledge/verification/*-gate.md`; registry and scoreboard — `SKILL.md` §Gates, `SCORECARD.md` operability row; method — `verification-method-overview.md`; lore adjacency — `synthesis/worldbible-integration-contract.md`; D2 drill — the shared culture-packet contract fields (phonology/morphology/lexicon/pantheon/symbols/costumes/names/eras), which the first real baselines will grade.
- follows: `corpus/knowledge/verification/verification-method-overview.md` §3 (rule locator / preserve the reviewed version or digest), §6 (fail-closed verdicts), §8 (reference/design clock), §10 step 1 (freeze the input packet and rule version); `corpus/knowledge/synthesis/worldbible-integration-contract.md` §4 (freeze the manifest; a changed referenced file invalidates the digest) and §9 (pinned versions, no auto-upgrade); `corpus/knowledge/verification/provenance-audit-ledger-format.md` §8 (append-only, active-view reconstruction); fleet `PROTOCOL.md` §Gate standard (two-evidences clause) and §Evidence standard — read-only fleet surface.
- canon: not canonized (D2 design drill)
- verified-at: 2026-10-17 — re-executed against lane revision `16887909ed66e8e4fb4c82a20d0d18084f430518`: all seven gate `--selftest` runs exit 0 (7/7); a scratch freeze of the `myth-consistency-gate` fixture produced exit 1 with the six expected finding IDs, and the tamper step produced a digest mismatch (transcript in §7). No gate in `tools/gates/frozen/` exists yet — §8 records that as an open, fail-closed obligation.

"Two evidences" is fleet policy (KTD-FR-S-0001): a green self-test is **capability**, not a
measurement. Every gate in this lane grades a mutable artifact — a culture packet under active
design, or corpus files under active triage — so each must also ship a **frozen run**: a
committed copy of the exact input, a committed expected verdict, and a digest pin that makes a
later hand-edit contradict the run instead of silently re-blessing it.

## 1. Scope: which gates owe a frozen run

- In scope: all seven registered gates (`SKILL.md` §Gates); their inputs are mutable by
  construction, and `handoff-packet-check` grades a sample packet this lane can edit.
- Out of scope: anything that cannot fail is a **probe**, not a gate (fleet clause); a probe
  is never registered with a frozen run it cannot earn.
- A frozen run never replaces the self-test, and a self-test never stands in for a frozen run.
  Release rule (`verification-method-overview.md` §6) is unchanged: a missing frozen run is
  UNKNOWN, and UNKNOWN blocks the conformance claim rather than caveating it.
- A frozen run is **lane-local engineering evidence**: these exact bytes, graded by this exact
  gate revision, produced this exact verdict — nothing about design quality or canon.

## 2. The two evidences, named

| Evidence | What it proves | What it never proves | Where it lives |
|---|---|---|---|
| Self-test (`--selftest`) | the gate can fail: planted defects yield the declared exit and finding IDs on isolated fixtures | that any real artifact was measured; that the current corpus/packet passes | `tools/gates/fixtures/`, run at build/review time |
| Frozen run | the committed snapshot, under the named gate revision, produced the committed verdict | that the snapshot is a good design, that a claim in it is true, or that lore accepted anything | one directory per baseline under `tools/gates/frozen/` |

- Both evidences name a **revision**: the self-test the commit carrying its fixtures, the frozen
  run the commit carrying its baseline (§4 field `revision`).
- Neither authorizes changing a sibling file, the corpus, or the world bible.

## 3. Directory layout under `tools/gates/frozen/`

```text
tools/gates/frozen/
  README.md                          # index: baseline id → gate, revision, verdict class
  <gate-name>/                       # directory name == registry row name, verbatim
    <baseline-id>/                   # e.g. r3-pre, r4-post — <round>-<phase>, lowercase
      packet.yml                     # committed input snapshot (byte copy, role-named)
      expected.json                  # digest pin + expected verdict (§4)
      run.log                        # observed gate stdout at freeze time, verbatim
      freeze.txt                     # frozen_by / frozen_at / command / revision / check result
```

- **Input snapshot.** A byte copy of the graded input, committed inside the baseline.
  `packet.yml` names a culture-packet input; a corpus-grading gate (e.g. `provenance-audit`)
  copies each graded file under the baseline's own subpaths (for example
  `corpus/verification/citation-format-and-source-registry.md`) and lists them in `inputs`.
  No excerpts, no reformatting, no live paths: a baseline that points at `corpus/…` instead
  of holding the copy re-inherits every later edit (KTD-FR-S-0003).
- **Naming and resolution.** `<gate-name>` is the registry row name; `<baseline-id>` is
  `<round>-<phase>` with phase `pre` (before the round's edits land) or `post` (after). A
  bare baseline id must resolve under exactly one gate directory; two candidates fail
  closed, and the run is not compared. Ids are never reused.
- **Append-only.** A later gate revision or input edit produces a **new** baseline. Existing
  baselines are never rewritten to match a new run — the old verdict stays legible next to
  its revision (same discipline as `provenance-audit-ledger-format.md` §8).
- **Content rules.** Snapshots carry no secrets, no environment files, no absolute home paths;
  `run.log` is the gate's stdout verbatim, with any stderr kept out (stderr differences are
  not part of the verdict contract).

## 4. `expected.json` — required fields

| Field | Required contents |
|---|---|
| `schema` | `kotodama-frozen-run-v1` (this entry's version) |
| `gate` | registry row name, matching the directory name |
| `gate_sha256` | digest of the gate script at freeze time (lane convention, not in the fleet clause) |
| `revision` | commit hash carrying this baseline; the verdict names what it was measured against |
| `frozen_at`, `frozen_by` | ISO-8601 local timestamp and the role/round that froze it (no personal identifiers) |
| `inputs` | map `path → sha256` for **every** file in the baseline that the gate reads |
| `expected.exit` | `0` or `1` for the compared verdict (`2` is reserved for could-not-evaluate, §6) |
| `expected.class` | `clean` (exit 0) or `findings` (exit 1) |
| `expected.findings` | the stable finding IDs as a **set**, order-insensitive |
| `stdout_sha256` | optional; advisory whole-output pin, never the finding contract |

- Compare by **finding-ID set**, not stdout order: the measured run of `myth-consistency-gate`
  prints `…M02` before `…M01`, while its committed `.expected` lists `M01` before `M02`. A
  byte equality check on stdout would call a healthy run a mismatch.
- Digests are SHA-256 (KTD-FR-S-0006); MD5 and SHA-1 pins are inadmissible (KTD-FR-S-0009).
- A baseline whose `inputs` map is empty or absent is `unpinned (legacy)`: retained for
  reading, barred from any conformance claim, and never silently re-pinned (KTD-FR-S-0002).

## 5. Freeze procedure

1. Confirm the tree is clean around the gate and the input (`git status --porcelain`); a dirty
   fixture is not a snapshot.
2. Run `--selftest` and record it — a gate that cannot fail has no measurement to freeze.
3. Copy the graded input **byte-identically** into the new baseline; compute the `inputs`
   digests and `gate_sha256`; never edit the copy afterwards.
4. Run the gate over the **snapshot copy** (never the live path); capture stdout as `run.log`
   and the exit code.
5. Write `expected.exit` / `expected.class` / `expected.findings` from what was observed —
   never from memory (fleet: claimed ≠ re-executed).
6. Record `revision`, `frozen_at`, `frozen_by`, and the command in `freeze.txt`; re-run the
   digest check against the snapshot (§6 step 1).
7. Commit the baseline with its README index row, then cite the commit in the round log — a
   worktree-only baseline is not evidence.

## 6. Verify procedure, tamper semantics, and class mapping

1. **Digest check first.** Recompute `inputs` against `expected.json`; any difference is
   `snapshot_tampered` — could-not-evaluate, exit 2, comparison refused. Until the gates verify
   digests internally, the report says which interim check ran.
2. **Gate-revision check.** `gate_sha256` differs → `gate_revised` — could-not-evaluate: re-freeze
   under the new revision; never compare across an unnamed one.
3. **Compare verdicts only after 1–2 pass** — `expected.exit` and the finding-ID set.

| Condition | Reading | Class / exit |
|---|---|---|
| digests match; observed exit and finding set equal the expected | compared verdict, match | `clean` / `findings` per `expected.exit`; check exits 0 |
| digests match; observed differs from expected | real drift — revise the gate or the artifact, and preserve the failure | `failed`; check exits 1 |
| any input digest differs | an edit to a frozen snapshot | `snapshot_tampered`; check exits 2 |
| `gate_sha256` differs | an unnamed gate revision | `gate_revised`; check exits 2 |
| `inputs` absent/empty, expected verdict present | legacy baseline | `unpinned (legacy)`; check exits 2 |
| `expected.json` missing, unreadable, or malformed | no baseline | could-not-evaluate; check exits 2 |

- The measured reason the digest step is load-bearing: after one comment line is appended to a
  frozen `packet.yml`, the gate **still prints the same six findings** — an orchestrator
  comparing only stdout would call this a match. Only the digest check turns it into
  `snapshot_tampered`.
- Fail-closed consequence: a gate with a self-test but no committed baseline does not meet the
  two-evidences clause; its registry row and any round claim must say so, and the gap is
  routed as a conformance defect, not smoothed into “green”.

## 7. Worked example — `myth-consistency-gate`, baseline `r3-pre`

Measured 2026-10-17 at revision `16887909ed66e8e4fb4c82a20d0d18084f430518`, in a scratch
tree (`/tmp`), presented as the drill's target shape — **the directory below is not yet
committed**:

```text
tools/gates/frozen/myth-consistency-gate/r3-pre/
  packet.yml        # byte copy of tools/gates/fixtures/myth-consistency-gate.yml
                    #   sha256 f94a700cc2d6cfadf91d8c96493fdc1e87dd50e53aa117d7598f12f524197086
  expected.json     # gate_sha256 26d246e9936db4375c31c6eb260545bf55051d11ec00bb1e757458399b1b55c5
                    # revision 16887909ed66e8e4fb4c82a20d0d18084f430518
                    # expected {exit: 1, class: findings,
                    #   findings: [MC-P01, MC-P02, MC-M01, MC-M02, MC-S01, MC-S02]}
  run.log           # six FINDING lines, exit 1 (verbatim stdout)
  freeze.txt        # command, revision, frozen_at, digest-check result
```

Commands, in order, with observed results:

| # | Command (from the lane root, then inside the scratch baseline) | Observed |
|---|---|---|
| 1 | `python3 tools/gates/myth-consistency-gate.py --selftest` | `selftest: OK — fixture exit 1; planted IDs present: MC-P01, MC-P02, MC-M01, MC-M02, MC-S01, MC-S02; clean control exit 0`; exit 0. `git status --porcelain` empty afterwards (the selftest rewrites fixture and expected deterministically) |
| 2 | `cp tools/gates/fixtures/myth-consistency-gate.yml …/r3-pre/packet.yml` | copy digest equals the fixture digest `f94a700c…` |
| 3 | `sha256sum packet.yml > digests.sha256; sha256sum -c digests.sha256` | `packet.yml: OK`; exit 0 |
| 4 | `python3 …/myth-consistency-gate.py packet.yml > run.log` | exit 1; six FINDING lines (MC-P01, MC-P02, MC-M02, MC-M01, MC-S01, MC-S02) |
| 5 | `printf '\n# tampered byte\n' >> packet.yml; sha256sum -c digests.sha256` | `packet.yml: FAILED`, exit 1 — `snapshot_tampered` |
| 6 | re-run the gate over the tampered copy | still exit 1, same six findings — the run cannot see the edit; only step 5 can |

- The example uses the committed fixture because it is reproducible from the repository with one
  command; the *first real* baseline should use a D2 protocol packet (§9) once one exists.
- `expected.findings` comes from the gate's committed `.expected` set, not stdout order (§4).
- What the example does **not** claim: that the frozen directory already exists, that the gates
  verify digests internally today, or that a clean frozen run means the D2 packet is good
  design. It is the format, executed once for real.

## 8. Status and what remains unbuilt

| Piece | Status 2026-10-17 | Consequence |
|---|---|---|
| self-tests green for all seven gates | implemented (rounds 1–2); re-run 2026-10-17: 7/7 exit 0 | capability evidence only |
| `tools/gates/frozen/` layout and first baseline | **not implemented** — this entry specifies it | two-evidences clause **UNMET** for every gate; no conformance claim may be made |
| gate-internal digest verification (a gate run that reads `expected.json` and returns `snapshot_tampered`) | not implemented; interim external `sha256sum -c` documented | the freeze procedure must state which check ran and by whom |
| registry rows naming the frozen baseline path | not yet updated | the registry row still lists only fixture self-test paths; update with the first baseline |

- Proposed next-round moves (round owner, not this entry): commit one baseline for a
  packet-grading gate and one for `provenance-audit`; add a `--frozen <baseline-dir>` mode to
  one gate as the reference implementation; then extend the registry rows.

## 9. D2 coupling

- The design drill's spine is **verticality and wind**: two seasonal poles (valley shelter /
  high pasture) and a record that must be re-speakable rather than remembered. The D2
  pre-writing tally-knot record is the in-world analog of the frozen baseline — its meaning
  lives in the committed *sequence* (the digests), not in recollection of the run. The analogy
  is declared, not imported as scholarship.
- The first real baseline should grade the **D2 culture packet**, whose contract fields are
  fixed by the drill: `phonology{consonants, vowels, phonotactics, tones, notable_rules}`,
  `morphology{type, alignment, word_order}`, `lexicon[{term, gloss, field, etymology,
  layer}]`, `pantheon[{name, role, domain, era}]`, `symbols[{sign, domain, era, notes}]`,
  `costumes[{garment, material, wearer_rank, rite, era}]`, `names[{name, type, etymology}]`,
  `eras`.
- Gate order for the D2 packet freeze: `phonology-sanity-gate` → `lexicon-coverage-audit` →
  `naming-collision-gate` → `myth-consistency-gate` → `costume-era-consistency-gate` →
  `handoff-packet-check` (`synthesis/worldbible-integration-contract.md` §4 envelope).
- No D1 imagery is imported: the standard freezes and re-checks; it does not bind, braid, or
  channel. Where a metaphor is needed, use the two poles and the re-spoken record.

## 10. Calibration

- **Policy vs convention.** The two-evidences obligation, the `0/1` verdict codes, the
  `snapshot_tampered` reading, and the ban on comparing across unnamed revisions are fleet
  policy (KTD-FR-S-0001/0002). The directory shape, baseline ids, `gate_sha256`/`gate_revised`,
  and the `expected.json` schema name are lane conventions; a fleet amendment wins over them,
  and this entry then needs an edit.
- **Digests are integrity, not truth.** A matching digest proves byte identity, not that the
  packet is coherent, that its sources are real, or that the design is worth keeping. Do not
  launder a frozen run into a design PASS; the twice-checked distinction lives in
  `verification-method-overview.md` §1–§2.
- **Trusted base.** The verifier is part of the trusted base (KTD-FR-S-0007): a digest chain
  cannot prove the gate itself is honest, which is why self-test and revision pin are separate
  requirements; deterministic re-execution lets a stranger reproduce the run (KTD-FR-S-0008).
- **Algorithm choice.** SHA-256 is the pin; SHA-1 collisions are demonstrated (KTD-FR-S-0009),
  so MD5/SHA-1 or hand-rolled checksums do not satisfy §4. Nothing here claims SHA-256 is
  future-proof — a future migration is a new `schema` version, not a silent re-pin.
- **False confidence check.** The round-12 incident is the calibration case: a pin that covered
  only part of the inputs read `match` while the artifact had been edited. The rule “pin
  **every** input the gate reads” exists because the near-miss was measured, not imagined.
- **Thin knowledge.** This entry is process method: no fact about real cultures, no
  cryptographic expertise beyond the cited standards, no claim that this layout matches any
  other lane's.

## 11. Canon boundary and handoff

- Nothing here decides what is true in any world. A frozen run is lane-local engineering
  evidence; it never enters the world bible, never marks a design accepted, and never
  substitutes for lore-shokunin's consistency verification or canon rulings (lane
  `AGENTS.md`, `PROVINCE.md`).
- Handoff: the round report and `LOG.md` carry the baseline ids, the command re-executed, the
  observed exit and finding set, and the falsifiable status of §8. The registry row
  (`SKILL.md` §Gates) gains the frozen-baseline path when the first baseline lands; until
  then the honest registry line is “self-test only — two-evidences UNMET”.
- Contested scope (for example, a fleet amendment that moves the frozen root, or a sibling
  lane's expectation that a bare baseline name resolves across lanes) is **reported to the
  integrator, never absorbed here** — the same stop rule this lane applies to every coupled
  system.