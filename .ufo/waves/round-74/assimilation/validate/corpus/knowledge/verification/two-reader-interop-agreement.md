# Two-reader interop agreement — verifying that independent readers of one artifact agree

- topic: The verification procedure for **interop agreement**: when two independently implemented readers consume the same artifact — a thin gate and the peer tool it adapts, a projector's projection and the gate that checks it, a run and a previously recorded run — their verdicts must be compared, not assumed, and a divergence must be dispositioned as reader-drift, input-drift, or a real defect. Covers the agreement shapes (byte-identical stdout, field-for-field verdict, set equality), the standing-regression reading (“same bytes as when the capability was admitted”), and the rule that agreement is a consistency result, never correctness. Method and lane policy only; canon belongs to lore-shokunin.
- gap filled: the partition carries single-tool verification (`verification-method-overview.md`), independence discipline (`verification-independence-anti-circularity.md`) and cross-file coherence audit (`internal-consistency-audit.md`), but no entry states the **interop agreement check** — two independent readers of one artifact, the agreement shapes, and how a divergence is dispositioned. Absence sweep 2026-10-18: `grep -rln "interop\|two readers\|reader agreement" corpus/knowledge/` → 0 files.
- sources:
  - KTD-IA-S-0001 — `reports/round-18/d4/interop-1.md` §0–§1: the D2 typed-gate path reproduces round-11's recorded verdict byte-for-byte on both recorded byte artifacts and field-for-field on the verdict; the seat also **independently re-parsed** the plain stdout against the committed expected set rather than re-running the gate's own assertion — an independent reading, not a re-run.
  - KTD-IA-S-0002 — `reports/round-18/d4/interop-2.md` §0–§1: both named assemblers' `--check` exit 0 with stdout identical to round-11's own recording, and all 13 commands of the standing regression set exit 0 with empty stderr; 12 of 13 stdout sha256 values match a previous round's recorded value exactly, the exception being the battery run whose stdout embeds its temp mirror path and is documented non-byte-stable.
  - KTD-IA-S-0003 — `reports/round-18/d4/interop-3.md` §0–§1: the battery exits 0 with all seven gate selftests passing, 8/8 committed baselines pinned and 0 uncovered; the round-11 frozen generation replays 11/11 rows.
  - KTD-IA-S-0004 — measured this round, 2026-10-18, lane root, `export TMPDIR=$PWD/.scratch`: the two thin adapters and their peers agree — `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` → exit 0, `…: byte-identical deterministic projection`; `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` → exit 0, `…: byte-identical deterministic assembly`; the peers' own modes (`assemble-culture-d4.py --check`, `d2-typed-labels.py --check`) produce the same lines.
  - KTD-IA-S-0005 — `tools/gates/d4-typed-labels-check-gate.py` docstring and `tools/gates/frozen/round-18/README.md`: the adapter pattern — the gate calls the peer's own check path (loaded by path, never re-implemented) and forwards stdout/stderr/exit unchanged. This is what makes agreement meaningful: two readers that share code agree trivially; the adapter forwards, and the *recording* against a previous run is the second reader.
  - KTD-IA-S-0006 — `corpus/knowledge/verification/verification-independence-anti-circularity.md` §1–§3 (independence is a property of failure sources; `claim ≠ anchor`) and §4 (control sensitivity). Supplies the reason a shared-code agreement is weak evidence; this entry supplies the interop comparison shape.
  - KTD-IA-S-0007 — John C. Knight and Nancy G. Leveson (1986), “An Experimental Evaluation of the Assumption of Independence in Multiversion Programming,” *IEEE Transactions on Software Engineering* SE-12(1): 96–109, [doi:10.1109/TSE.1986.6312924](https://doi.org/10.1109/TSE.1986.6312924). Nominally independent implementations failed together far more often than independence assumptions predict; the classic is cited as a calibration warning (with its documented methodological debate), not as a law.
  - KTD-IA-S-0008 — Reproducible Builds project documentation, [reproducible-builds.org/docs/](https://reproducible-builds.org/docs/) (accessed 2026-10-18). Reproducibility is what lets a *later* reader compare against an earlier one; the standing-regression reading is that discipline applied across rounds.
  - KTD-IA-S-0009 — Dijkstra, Edsger W. (1972), “The Humble Programmer,” *Communications of the ACM* 15(10): 859–866, doi:10.1145/355604.361591. Agreement between two readers shows neither is diverging here; it shows nothing about whether both are right.
- calibration: interop reading is this lane's house policy, not a published standard; Knight–Leveson (1986) is a classic with a documented methodological debate, cited as a calibration warning, not a law; the Reproducible Builds documentation and Dijkstra are engineering references; no real culture is described.
- couples: verification — `verification-method-overview.md`, `verification-independence-anti-circularity.md`, `internal-consistency-audit.md`, `gate-frozen-run-standard.md`, `gate-battery-surface-verification.md`, `generated-artifact-roundtrip-verification.md`; synthesis — `../synthesis/generated-artifact-lifecycle.md`, `../synthesis/worldbible-integration-contract.md`; tooling — `tools/gates/d4-typed-labels-check-gate.py`, `tools/gates/d4-assembly-check-gate.py`, `tools/assemble-culture-d4.py`, `tools/d2-typed-labels.py`, `tools/replay-frozen.py`, `tools/gates/frozen/round-18/`; siblings — lore-shokunin owns canon; chousa-shokunin owns general research method.
- source: the round-18 interop receipts and this round's re-measurement of the two adapter/peer pairs; the interop comparison procedure is this lane's house method, not a finding attributed to the cited works.
- verified-at: 2026-10-18 — re-measured at HEAD `169c616`, lane root, `export TMPDIR=$PWD/.scratch`: the two D4 adapter legs exit 0 with the peers' own `byte-identical …` lines, and the peers' `--check` modes produce the same lines; the cited interop receipts were read by path, not re-executed. Header fields and cross-reference targets checked for resolution; all cited repo paths exist.
- recheck: whenever a gate adapter, peer tool, or frozen manifest changes; before quoting an agreement as “the same as when it was admitted”; and whenever a divergence between two readers is observed (corrections are new entries, never rewrites).

## 1. What this entry licenses

- A **comparison procedure**, not a correctness proof: it tells a reviewer how to compare two readers of one artifact, what “agree” can mean, and how to dispose of a divergence.
- Agreement is **consistency, not truth**: two readers that share code, share inputs, or share a prior recording can agree while both are wrong (Knight & Leveson as a calibration warning; Dijkstra).
- The strongest agreement available in this lane is a **cross-round recording**: the same bytes as when the capability was admitted (`reports/round-18/d4/interop-2.md` §0). That is the reading to prefer over “commands exit 0 today”.

## 2. Agreement shapes — from weakest to strongest

| shape | how it is measured | what it does not catch |
|---|---|---|
| E1 both exit 0 | exit codes only | any output difference; an exit code is one bit |
| E2 verdict-field agreement | the finding set compared field-for-field (`id`, `severity`, `where`) | byte drift inside a field; a field the comparison omits |
| E3 set equality | `(id, severity, where)` set equality against a committed set, checked independently of the reader's own assertion | ordering, duplicates, and formatting drift |
| E4 byte-identical stdout | stdout `sha256` compared against a recorded value | a shared generator bug (both readers produce the same wrong bytes) |
| E5 cross-round byte recording | E4 against **another round's** recorded value, with the reader's revision pinned | nothing about correctness; it asserts stability of the admitted capability |

The measured D4 legs reach E4/E5: the adapter forwards the peer's own
`<path>: byte-identical …` line, and the frozen rows pin `output_sha256`
(`tools/gates/frozen/round-18/MANIFEST.tsv` rows 2–3). The round-18 interop seat
reached E3 independently (re-parsing stdout rather than re-running the gate's
assertion) and E5 for the standing regression set.

## 3. Divergence disposition

When two readers disagree, the divergence is classified before anything is
“fixed”:

| class | signature | disposition |
|---|---|---|
| reader-drift | one reader's revision moved; the artifact is unchanged | re-record the pin as a **new** row; never edit the recorded row in place |
| input-drift | the artifact digest moved | re-freeze the input snapshot; the old verdict stays the old verdict |
| adapter-drift | the adapter and its peer disagree although both were unchanged | a defect in the adapter — it must forward, never re-implement (KTD-IA-S-0005) |
| shared-bug | both readers agree on wrong output | invisible to interop; requires an independent control or a gate with different semantics |
| non-byte-stable output | the reader's stdout embeds a temp path or timing | documented as non-byte-stable and excluded from E4/E5, never silently compared (the battery case, `reports/round-18/d4/interop-2.md`) |

## 4. Controls — what makes an agreement check real

| control | planted condition | required result |
|---|---|---|
| one-bit | make both readers exit 0 with different output | E1 passes, E2–E4 must fail — reading only exit codes is declared insufficient |
| tamper | change one byte of the artifact | both readers change; the recorded comparison fails |
| reader-move | change a reader's revision, leave the artifact | the pin reads stale/`gate_digest_mismatch`, not “agreement” |
| adapter-reimplementation | make the adapter compute its own answer | the adapter/peer comparison must be able to fail — the adapter is required to forward |
| non-byte-stable | point a reader at a temp path | the reading is excluded, not force-matched |

## 5. What interop agreement never proves

- **Agreement is not correctness.** Two readers can share a bug; interop cannot see it (§3, shared-bug).
- **A shared-code agreement is weak.** If both readers run the same function, E1–E4 are near-tautological; the independent reading (re-parsing, a different tool) is what adds information.
- **A reproduced verdict stays a verdict.** A reproduced red is red; a reproduced green is green at that revision — neither is a clearance.
- **A non-byte-stable reader is not a failure.** It is excluded from byte comparison with a documented reason, not force-matched or silently dropped.

## 6. Decision record — the interop rules this entry adopts

1. **Adopted:** interop agreement is checked at E2–E4 at minimum, and E1 alone is never reported as agreement (§2, §4). Consequence: “both exit 0” is not an interop result.
2. **Adopted:** the preferred reading is the **cross-round byte recording** — the same bytes as when the capability was admitted (§1, E5). Consequence: a today-green run that differs from the admission recording is a finding, not a refresh.
3. **Adopted:** a divergence is classified (reader-drift / input-drift / adapter-drift / shared-bug / non-byte-stable) before any fix, and reader-drift is re-recorded as a **new** row (§3). Consequence: no recorded row is edited in place.
4. **Adopted:** the adapter pattern — a thin gate forwards its peer's stdout/stderr/exit unchanged and is never re-implemented (`tools/gates/d4-typed-labels-check-gate.py`) — is what makes adapter/peer agreement non-tautological (§3). Consequence: an adapter that computes its own answer is a defect.
5. **Rejected:** treating agreement as correctness or as clearance. Reason: shared-bug is invisible to interop (§5; Knight & Leveson as a calibration warning).
6. **Open (to-verify):** whether the standing regression set's 13 commands (12 byte-stable, 1 documented non-byte-stable) should be re-run as a first-class interop leg each round rather than cited from a prior receipt. Owner: this lane's O/D boundary; not disposed here.
