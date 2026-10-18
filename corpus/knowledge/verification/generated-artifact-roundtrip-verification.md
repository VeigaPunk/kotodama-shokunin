# Generated-artifact round-trip verification — byte-identity, `--check`, and the corruption class

- topic: The verification procedure for **generated artifacts**: an artifact produced by a tool from authored sources (a packet from components, a projection from a packet) is verified by regenerating it and comparing bytes, by running the tool's own `--check` mode, and by proving the check can fail. Covers the round-trip corruption class — a re-serialization that keeps a document's shape while changing its meaning — the digest pins that make a hand-edit contradict the record, and the rule that a byte-identical regeneration proves determinism, not soundness. Method and lane policy only; canon belongs to lore-shokunin.
- gap filled: the partition carries frozen-run verification (`gate-frozen-run-standard.md`) and the re-pin/independence record (`verification-independence-anti-circularity.md`), but no entry states the **round-trip verification of a generated artifact** — regeneration byte-identity, `--check`, and the corruption class a re-serialization can hide. Absence sweep 2026-10-18: `grep -rln "round-trip\|roundtrip\|serializer" corpus/knowledge/verification/` → 0 files.
- sources:
  - KTD-GA-S-0001 — `examples/culture-d4/ASSEMBLY.md` §1–§3: the artifact chain (12 authored components → `tools/assemble-culture-d4.py` → `packet.d4.yml`; → `tools/d2-typed-labels.py` → `typed-labels.d4.yml`) and the rule “never hand-edit a generated file; after any component edit, rebuild and re-run `--check` plus the gates”. NON-CANON drill record.
  - KTD-GA-S-0002 — measured this round, 2026-10-18, lane root, `export TMPDIR=$PWD/.scratch`: `python3 tools/assemble-culture-d4.py --check` → exit 0, `packet.d4.yml: byte-identical deterministic assembly`; `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` → exit 0, same line; `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` → exit 0, `byte-identical deterministic projection`.
  - KTD-GA-S-0003 — `reports/round-18/d4/determinism.md` §0–§1: two consecutive runs of the projector, the D4 assembler, and the generalized gate each produced byte-identical output; the comparison is on stdout bytes and the `--json` document, because “a gate whose interface is stdout plus an exit code is deterministic exactly when those bytes repeat”.
  - KTD-GA-S-0004 — `tools/gates/frozen/round-18/MANIFEST.tsv` (rows 2–3) and `tools/gates/frozen/round-18/README.md`: the two check legs are pinned as frozen rows with `gate_sha256`, `input_sha256` and `output_sha256`; a later gate edit turns the row red by design, and “a re-freeze is a new recording, never an in-place edit”.
  - KTD-GA-S-0005 — `tools/gates/d4-typed-labels-check-gate.py` (module docstring) and `tools/gates/d4-assembly-check-gate.py`: the thin adapter pattern — each gate calls the peer's own `--check` path (loaded by path, never re-implemented) and forwards stdout/stderr/exit unchanged, so the input path string and the peer's `<path>: byte-identical …` line stay stable across recording and replay.
  - KTD-GA-S-0006 — `corpus/knowledge/verification/gate-frozen-run-standard.md` §3–§6 (input snapshots, digest pins, tamper semantics: the digest check runs before the verdict compare) and §10 (a digest proves the bytes, never the tool that reads them). These supply the freeze mechanics; this entry supplies the regeneration/round-trip procedure they assume.
  - KTD-GA-S-0007 — Reproducible Builds project documentation, [reproducible-builds.org/docs/](https://reproducible-builds.org/docs/) (accessed 2026-10-18). Byte-for-byte reproducibility is what lets a stranger regenerate an artifact and compare; cited as the discipline, not as a claim about content.
  - KTD-GA-S-0008 — Ken Thompson (1984), “Reflections on Trusting Trust,” *Communications of the ACM* 27(8): 761–763, doi:10.1145/358198.358210. The generator and the checker belong to the trusted base: regeneration proves the generator is deterministic, not that its output is correct.
  - KTD-GA-S-0009 — NIST (2015), *Secure Hash Standard (SHS)*, FIPS PUB 180-4, [PDF](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf). Defines SHA-256; cited for digest construction only, never as a truth measure for content.
- calibration: round-trip verification is this lane's house policy, not a published standard; Thompson (1984), NIST FIPS 180-4 and the Reproducible Builds documentation are engineering references for digests, determinism and the trusted base only — never truth measures for content; the D4 artifacts are NON-CANON.
- couples: verification — `gate-frozen-run-standard.md`, `verification-independence-anti-circularity.md`, `verification-method-overview.md`, `internal-consistency-audit.md`; synthesis — `../synthesis/generated-artifact-lifecycle.md`, `../synthesis/hold-set-contract-in-brief.md`, `../synthesis/worldbible-integration-contract.md` §4/§9; tooling — `tools/assemble-culture-d4.py`, `tools/d2-typed-labels.py`, `tools/gates/d4-assembly-check-gate.py`, `tools/gates/d4-typed-labels-check-gate.py`, `tools/replay-frozen.py`, `tools/gates/frozen/round-18/`; siblings — lore-shokunin owns canon; chousa-shokunin owns general research method.
- source: the D4 artifact chain and its round-18 receipts, plus this round's re-measurement of the three `--check` legs; the round-trip procedure is this lane's house method, not a finding attributed to the cited works.
- verified-at: 2026-10-18 — re-measured at HEAD `169c616`, lane root, `export TMPDIR=$PWD/.scratch`: the three `--check`/gate legs above all exit 0; `python3 tools/gates/d4-typed-labels-check-gate.py --selftest` → exit 0, `39/39 checks passed`; `python3 tools/gates/d4-assembly-check-gate.py --selftest` → exit 2, `No such file or directory: '--selftest'` (this gate ships no selftest; recorded as an open obligation in §6). Header fields and cross-reference targets checked for resolution; all cited repo paths exist. The round-18 receipts were read by path, not re-executed.
- recheck: whenever an assembler, projector, gate adapter, packet, or projection changes; before quoting a “byte-identical” line as though it certified content; and whenever the missing-selftest obligation is discharged (corrections are new entries, never rewrites).

## 1. What this entry licenses

- A **regeneration check**, not a correctness proof: it tells a reviewer how to show that an artifact is exactly what its tool produces from its sources, and how to make a hand-edit contradict that claim.
- The scope is **generated** artifacts only. An authored source (a component, an entry) has no generator to re-run; it is verified by its own review, not by round-trip.
- A green round-trip is **lane-local engineering evidence**: these bytes are this tool's output from these sources at this revision — nothing about design quality or canon.

## 2. The artifact chain and its verification points

| stage | artifact | produced by | verification |
|---|---|---|---|
| source | 12 components under `examples/culture-d4/components/` | authored (round-17 seats) | authored-source review; never regenerated |
| assembly | `examples/culture-d4/packet.d4.yml` | `tools/assemble-culture-d4.py` | `--check` byte-identity; `d4-assembly-check-gate` forwards it; frozen row 3 |
| projection | `examples/culture-d4/typed-labels.d4.yml` | `tools/d2-typed-labels.py` | `--emit` then `cmp`; `--check` byte-identity; `d4-typed-labels-check-gate`; frozen row 2 |
| pinned set | `examples/culture-d4/expected-holds.json` | derived, never copied | `packet_sha256` / `projection_sha256` pins; equality checks in `reports/round-18/d4/holds.md` §6 |

The measured chain closes: every `--check` leg exits 0, and the two check legs are
pinned in `tools/gates/frozen/round-18/MANIFEST.tsv` with input digests
(`typed-labels.d4.yml` `a59990bb…`, `packet.d4.yml` `e7ecd204…`).

## 3. The round-trip corruption class

A **round-trip corruption** is a change that survives regeneration — or that
regeneration cannot detect — while altering meaning. Named classes and their
controls:

| class | how it arises | why byte-identity alone may not catch it | control |
|---|---|---|---|
| C1 silent re-serialization | a tool rebuilds the document with a different key order, number format, or string escape | the document parses to the same object but the bytes differ — caught only if the check compares bytes, not values | `--check` must compare bytes; a value-level comparison is declared insufficient |
| C2 default insertion | a serializer emits a field the source omitted (a default era, an empty list) | regeneration is “deterministic” and the artifact gains a field the author never wrote | `--check` against the **committed** artifact, not against a freshly written one |
| C3 lossy normalization | the tool normalizes whitespace/Unicode in a way the source did not intend | the normalized form is stable, so re-running agrees with itself | pin the source digest too; a normalized artifact whose source digest moved is a finding |
| C4 check-that-cannot-fail | a `--check` that compares the artifact with a copy the same run just wrote | always green | the check must read the committed artifact and a fresh build from **different** code paths (the adapter pattern), and a tamper must turn it red |
| C5 generator self-agreement | two runs of a broken generator agree | green with a wrong artifact | round-trip proves determinism only; correctness needs the gates and the declared set |

Measured against C4: the projector's own selftest includes `cli: --check exit 1
on a changed byte` and `cli: --check exit 0 after restore` (39/39, exit 0), so the
check demonstrably can fail.

## 4. Controls — what makes a round-trip check real

| control | planted condition | required result |
|---|---|---|
| tamper | change one byte of the committed artifact | `--check` exits 1 (measured: projector selftest `--check exit 1 on a changed byte`) |
| restore | restore the byte | `--check` exits 0 again |
| two-build | build twice from the same sources | byte-identical (`cmp`) |
| cross-path | compare the committed artifact against a fresh build, not against a copy of itself | mismatch on any C1–C3 drift |
| source-digest | move an authored component but keep the artifact | the source digest changes; the pin is stale and must be re-recorded, not silently re-blessed |
| gate-vs-peer | run the thin gate and the peer's own `--check` | identical stdout and exit (the adapter forwards, never re-implements) |

## 5. What a round-trip never proves

- **Determinism is not correctness.** Two identical runs of a wrong generator are still wrong (C5; Thompson).
- **A digest is not truth.** A `sha256` pin proves the bytes, never that the bytes are sound (`gate-frozen-run-standard.md` §10).
- **`--check` green is not the artifact being reviewable.** It says the committed artifact equals the tool's output; whether that output satisfies the gates and the declared hold set is a separate measurement.
- **A hand-edit is not a fix.** Editing a generated file makes it stop being that tool's output; the correct move is to edit the source and regenerate (§2).

## 6. Decision record — the round-trip rules this entry adopts

1. **Adopted:** a generated artifact is verified by regenerating it and comparing **bytes**, plus the tool's own `--check` against the **committed** artifact (§3 C1/C4). Consequence: a value-level comparison is declared insufficient and a check that compares against its own fresh copy is not a check.
2. **Adopted:** generated files are never hand-edited; a change goes to the source, then the artifact is rebuilt and `--check` re-run (`examples/culture-d4/ASSEMBLY.md` §1). Consequence: a hand-edited artifact is a defect even when its content looks right.
3. **Adopted:** every check leg that a frozen row pins runs through a thin adapter that calls the peer's own check path (loaded by path, never re-implemented) and forwards its output unchanged (`tools/gates/d4-typed-labels-check-gate.py` docstring). Consequence: the replay's `<path>: byte-identical …` line is stable across recording and replay.
4. **Adopted:** a round-trip green is reported as “byte-identity of a NON-CANON artifact”, never as soundness or clearance (§5; the gate docstring says the same).
5. **Rejected:** accepting a `--check` that writes its own comparison target in the same run. Reason: it cannot fail (C4), so it is not evidence.
6. **Open (to-verify):** `tools/gates/d4-assembly-check-gate.py` ships **no** `--selftest` (measured: `--selftest` → exit 2, `No such file or directory: '--selftest'`), so the fleet two-evidences clause is met for the D4 typed-labels leg (39/39) but not for the D4 assembly leg. Owner: this lane's O axis; recorded here as an obligation, not repaired by this entry.
