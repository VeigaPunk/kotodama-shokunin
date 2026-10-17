# Round 9 · O-shard · `lexicon-coverage-audit` frozen-run baseline — author fragment

- **Shard role:** baseline author (targets `R9-O01..O14`, gate `lexicon-coverage-audit`); the paired shard re-runs and validates this baseline in a copied tree.
- **Date / revision:** 2026-10-17, round-9 declared baseline revision `e1694bad6ac96aca45a11ca5746582b275929355` (HEAD at freeze `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`; `git diff --stat e1694ba..HEAD` = `reports/round-9/{claims,targets}.json` only, and `git diff --stat e1694ba..HEAD -- tools corpus examples` is empty — measured, so the graded tree is identical at both revisions).
- **Deliverable (baseline, canonical layout per `corpus/knowledge/verification/gate-frozen-run-standard.md` §3):** `tools/gates/frozen/lexicon-coverage-audit/r9-pre/`

| file | sha256 | note |
|---|---|---|
| `packet.yml` | `a1b8ed7c3548ace7a631b6b2752673f6a65a44896caecef170e373d67ec59187` | byte copy of the gate's committed fixture |
| `expected.json` | `0fad58ba70d545328d015990de5184bdd371e575810eb7e79c96bcc7c8a4ff9c` | digest pin + verdict (§4 fields) |
| `run.log` | `af5794955b60b455b433a570434bf0ab69c110b66c891eab567d5addef0be4f4` | gate stdout verbatim, exit 1 |
| `freeze.txt` | `4909a6b49b838e96c8ca00bf049b832dc55332243342b59222e42a4d56a6d788` | freeze record |
| `digests.sha256` | `4d392240e61c63cc2146d05bb1e354c0b75cd33d9603e7ea33a428a83c0c2f25` | one-line interim check: `sha256sum -c` |

## 1. Scope note — which file was written, and what was deliberately not

The shard assignment names `tools/gates/lexicon-coverage-audit.py` as the *subject* (the gate whose baseline is being authored) and this fragment as the written artifact. **The gate script was not modified:** `gate_sha256` in `expected.json` equals the untouched committed digest `2c4dd397…`, and `git status --porcelain -- tools/gates/lexicon-coverage-audit.py` is empty. Claim O's rule "no gate behavior changes" holds by construction for this shard. A `--frozen <baseline-dir>` mode inside the gate (standard §8 proposal) is *not* implemented here: mixing a gate change with baseline authorship would invalidate the very digest this baseline pins to, and round-9 D work depends on the D2 chain staying put.

## 2. Claim O's "verify the actual count first" — measured

| command (2026-10-17, lane root) | observed |
|---|---|
| `git ls-tree -r a7bb205 --name-only \| grep -c 'expected\.json$'` | `1` — `examples/culture-d3/expected.json`, the D3 packet pin, **not** a gate baseline |
| `git ls-tree -r a7bb205 --name-only tools/gates/fixtures \| grep '\.expected$'` | 8 committed fixture expectation files (`<gate>.expected`, plural) — the gates' selftest contracts, not §4 baselines |
| `find tools/gates/frozen -name MANIFEST.tsv \| wc -l` | `2` (rounds 3 and 4) — legacy frozen runs with TSV digest rows (e.g. round-3 `lexicon-coverage-audit` over the D2 packet: `exit 0`, `0` findings, `input_sha256 54be6319…`), i.e. *unpinned (legacy)* in the standard's naming |

So the claim's "before" (`0 of 7`) holds at the round-9 baseline revision: **0/7 gates** carried a committed `expected.json` baseline. This shard adds 1 of the 7.

## 3. Procedure and receipts (§5 steps 1–7), all run 2026-10-17

1. `git status --porcelain -- <gate> <fixture> <fixture>.expected` → empty (clean input; a dirty fixture is not a snapshot).
2. `python3 tools/gates/lexicon-coverage-audit.py --selftest` → exit 0, `selftest: 14/14 checks passed`. The run regenerates fixture + `.expected` deterministically: the tracked pair was unchanged afterwards (`git status` empty, fixture digest still `a1b8ed7c…`) — capability evidence, not the measurement.
3. `cp tools/gates/fixtures/lexicon-coverage-audit.yml …/r9-pre/packet.yml` → copy digest `a1b8ed7c…`, i.e. byte-identical to the source.
4. `sha256sum packet.yml > digests.sha256; sha256sum -c digests.sha256` → `packet.yml: OK`, exit 0.
5. `python3 tools/gates/lexicon-coverage-audit.py packet.yml > run.log` (from the baseline dir) → **exit 1**, 20 `FINDING` lines, 18 unique IDs, stderr 0 bytes; `run.log` sha256 `af579495…`.
6. Same command again → `cmp` clean, same stdout digest. Two runs byte-identical; verdicts are compared by ID *set* anyway, never by stdout order (§4).
7. Tamper drill in an in-repo scratch copy (never in the baseline): append one comment line → `sha256sum -c` prints `packet.yml: FAILED` (exit 1) → tampered digest `e1b738b7…`; re-running the gate over the tampered copy prints the **identical 18-ID set**. This is the standard's §6 calibration case measured on this gate: only the digest step detects the edit, so the interim check `sha256sum -c digests.sha256` (exit 1 → `snapshot_tampered`, could-not-evaluate) is load-bearing until shard R9-O15 wires the mapping into the battery.
8. Cross-pin agreement: `diff <(sort -u observed-ids) <(sort -u tools/gates/fixtures/lexicon-coverage-audit.expected)` → empty, exit 0. The gate's own committed `.expected` (`bd20bb40…`) and this committed `expected.json` are two independent pins that agree on all 18 IDs.
9. Post-write self-check (`python3` inline, from the baseline dir): schema/gate fields parse; `packet.yml` digest == `inputs` pin → True; gate digest == `gate_sha256` pin → True; observed exit 1 == `expected.exit`; observed ID set == `expected.findings` → True; `sha256(stdout)` == `stdout_sha256` → True; stderr 0 bytes. (A first version of this checker split `FINDING <id>:` and kept the colon, so it printed `False` once — the checker was wrong, not the baseline; recorded so the paired validator does not repeat it.)

## 4. `expected.json` field → evidence map (standard §4)

| field | value / source |
|---|---|
| `schema` | `kotodama-frozen-run-v1` |
| `baseline_id` / `gate` / `gate_script` | `r9-pre` / `lexicon-coverage-audit` (registry row name, `SKILL.md:184`) / `tools/gates/lexicon-coverage-audit.py` |
| `gate_sha256` | measured digest of the untouched gate at freeze |
| `revision` + `revision_note` | round-9 declared baseline revision + the measured `e1694ba..HEAD` diff statement |
| `frozen_at` / `frozen_by` | 2026-10-17T17:49:43-03:00 / round-9 O-shard baseline author (no personal identifiers) |
| `inputs` | `{"packet.yml": <sha256>}` — the only file the gate reads, inside the baseline |
| `expected.exit` / `.class` / `.findings` | observed: `1` / `findings` / 18 IDs as a set |
| `finding_lines`, `finding_counts` | 20 lines; `C-entry-unevaluable` ×2 and `D-stage-mismatch` ×2, all others ×1 |
| `stdout_sha256` | advisory whole-output pin (same value across both runs) |
| `gate_selftest`, `tamper_evidence`, `agreement_…`, `order_independence`, `layout_note` | lane-convention extras, each with its measured receipt above |

## 5. What this evidence is *not*

Lane-local engineering evidence only: these exact bytes, graded by this exact gate revision, produced this exact verdict. The packet is a fictional, planted-defect fixture — nothing here is a claim about real languages, a design PASS, or canon (the fixture's own header says the same). SHA-256 proves byte identity, never truth. The `snapshot_tampered` mapping cited above is the *interim external* check; the in-tool battery mapping belongs to R9-O15.

## 6. Reported, not absorbed — baseline-root divergence is integration-critical

Measured in the live tree at 17:50–17:51, round-9 sibling shards placed baselines under **three different roots**:

| root | sibling artifact seen |
|---|---|
| `tools/gates/frozen/<gate>/r9-pre/` (standard §3) | `handoff-packet-check` (`packet.md`, `run.log`, `expected.json`) and this baseline |
| `tools/gates/expected/<gate>/r9-pre/` | `costume-era-consistency-gate` (`packet.yml`, `run.log`, `expected.json`) |
| `reports/round-9/baselines/<gate>/` | `naming-collision-gate` (`packet.yml`, `run.log`, `expected.json`, `freeze.txt`, `author.md` — whose `layout_note` asserts *this* root as "the round-9 root") |

Consequences for the shards that consume baselines:

- **R9-O15 (battery extension):** discovery must be the union of `tools/gates/frozen/*/*/expected.json`, `tools/gates/expected/*/*/expected.json`, `reports/round-9/baselines/*/expected.json`; a single-root rule silently validates a subset and yields a false "7/7" reading of claim O.
- **Fail-closed duplicate rule:** standard §3 forbids one baseline id resolving to two gate directories; a cross-root check should refuse to compare a gate that carries the same `baseline_id` twice (copying a baseline between roots is not a safe "fix").
- **R9-O17 (registry):** the pinned-value path must be recorded per gate verbatim, since it is not uniform this round.
- **If the round consolidates on one root, MOVE these files; do not copy them** — a second copy of `r9-pre` for this gate would trip the rule above. This shard kept exactly one copy.

## 7. Advisory, not part of this baseline: the live D2 packet

`python3 tools/gates/lexicon-coverage-audit.py examples/culture-d2/packet.d2.yml` → **exit 0** (clean), live packet sha256 `e0f21509…`; the round-3 legacy manifest pinned the same path at `54be6319…`, and `examples/culture-d2/ASSEMBLY.md:58` records 0 findings. The packet is mutable by design, which is exactly why the baseline *copies* its input. If the lane wants a real-packet pin for this gate, author a separate `r9-d2` baseline id (same `inputs` map, `expected.class: clean`, `findings: []`) — deliberately not added here, to keep one claim-aligned baseline per gate and to leave the choice to the registry/integration shards.

## 8. Environment hazard observed (fleet-relevant, outside this lane's scope to fix)

`/tmp` is a tmpfs with **inodes 100 % exhausted**: `df -i /tmp` → `1048576 IUsed, 0 IFree, 100 %`. A `2> /tmp/…` redirect therefore aborts the whole command *before* the program runs ("No space left on device") while the earlier `> file` had already truncated its target — which silently produced one empty `run.log` here before the cause was found. Any worker or tool that uses `/tmp` (including `tempfile`-based ones) is exposed; in-repo scratch worked. Reported for the fleet, not absorbed.

## 9. Left to others (not claimed here)

- `tools/gates/frozen/README.md` index row — **not written**: seven sibling authors would race on one file; belongs to the scribe/integration shard.
- Registry row and pinned-value path (R9-O17); battery baseline validation + tamper mapping (R9-O15).
- Independent re-run in a copied tree by the paired validator shard; verification that `run.log` is stdout-verbatim and the digest pin matches.
- No `LOG.md`/`SCORECARD.md` edit and no commit — integration is the orchestrator's.

## 10. Receipts / verification footer

All commands above were executed 2026-10-17 between 17:49:43 and 17:51 local (UTC-03:00) from the lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin` at HEAD `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`, tree revision `e1694bad6ac96aca45a11ca5746582b275929355`; output quoted verbatim in §2–§3. Scratch receipts (stderr-empty proof, run-2 stdout, tamper copy) are under `.scratch/r9lex-author/` and are not part of the deliverable. Recheck trigger: any change to `tools/gates/lexicon-coverage-audit.py`, its fixture, or the standard re-opens this baseline (new baseline id; existing ids are never rewritten).
