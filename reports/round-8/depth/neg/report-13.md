# R8-D13 — Negative example: a plausible-but-unsupported era/material scope claim

- round: 8 (loop 1 of 3, build round 1 of 4) · shard: D13 (negative examples)
- owner: L2 worker, kotodama-shokunin lane
- date: 2026-10-17 (local stamps -03; the tree's own clock, restated in the receipts)
- baseline revision: `e7ca0faeb6680fa9891b907be628d9db578c28f4` (`reports/round-8/claims.json:5`)
- canon: NON-CANON synthetic control. Nothing here is a culture design, a canon
  record, a handoff, or a claim about any real material, era or culture. The
  fixture is a lane-owned test packet; no source file was edited.
- tool under test: `tools/d2-typed-labels.py` — D02 owns it and was editing it
  throughout this shard. Every receipt below is pinned to the sha256 of the
  revision that produced it; the revision log is §5.
- sibling shard in the same directory: D12's malformed-packet fixtures
  (`packet-12a.*`, `packet-12b.*`, `report.md`, `run-negatives.sh`). This
  shard's files are the `packet-13.*` / `run-13-*` set and this report.

## 1. The claim under test

Fixture: `reports/round-8/depth/neg/packet-13.era-material-scope.yml`
(sha256 `595cc73fec891b7bb094770ff8c0d7985768f2b0b799c89ab34896782f504867`).

The packet declares three era tags (E0/E1/E2), two materials and two costumes.
Exactly one record carries the claim:

| Record | Declared era | Declared material | Packet's own material facts |
|---|---|---|---|
| `GAR-R13-01` (clean control) | E0 | `felt` (`CMAT-13-01`) | route `RT-13-01` covers E0, E1, E2 |
| `GAR-R13-02` (**claim**) | E0 | `lowland plant-thread cloth` (`CMAT-13-02`) | `excluded_eras: [E0]`; only route `RT-13-02` covers E1, E2 |

**Claim:** "a coat of imported lowland plant-thread cloth is in scope at E0."

**Why it is plausible.** The valley coat is an E0 garment in this packet — the
felt control sits at E0 — so an author can copy the era value onto the
imported-cloth variant without the record looking wrong. The material
reference resolves to a declared record (it is not a dangling name), the
record is well formed, and the run emits no `D2L-DATA` finding for it. The
claim is not a typo and not a schema violation; it is an ordinary-looking
scope declaration.

**Why it is unsupported.** The packet's own material record for the imported
cloth declares `excluded_eras: [E0]` and a single route covering E1 and E2.
No declared route supplies the cloth in E0. The exclusion is a closed
inventory declaration, not absent evidence (the same reading the frozen
costume gate applies: "a declaration of exclusion is a closed inventory, not
an absent-evidence guess").

## 2. What the reconciliation path does with it

### 2.1 The claim is flagged — tool run on the fixture

Revision `11e23ca9d77f66f5a95bfabeed48e253ddcdb37308b9bd204d81dd33c1c24b41`,
observed 2026-10-17T17:29:48-03:00.

```sh
python3 tools/d2-typed-labels.py --packet reports/round-8/depth/neg/packet-13.era-material-scope.yml --json
# exit 1
python3 tools/d2-typed-labels.py --packet reports/round-8/depth/neg/packet-13.era-material-scope.yml
# exit 1
```

Observed finding (report mode, verbatim; receipt `run-13-observed.txt`,
sha256 `0f5755061b6ce89931047053dc4ef79234363d7fbdd46aa2cd74f629d4ce5875`):

```
FINDING D2L-MATERIAL: [reject] GAR-R13-02 — CMAT-13-02 is not available in E0: excluded_eras declares E0
```

The JSON document (receipt `run-13-observed.json`, sha256
`162d080b7362bad79f52bd96540568103fa81a41afd2b1b9d53d817cc9ec4f85`) carries
the same finding with the raw shard code:

```json
{"code": "R-MAT-ERA-EXCLUDED", "detail": "CMAT-13-02 is not available in E0: excluded_eras declares E0",
 "id": "D2L-MATERIAL", "severity": "reject", "where": "GAR-R13-02"}
```

Counts from that document (same command as above, 2026-10-17):

```sh
python3 -c "import json; d=json.load(open('reports/round-8/depth/neg/run-13-observed.json'));
print(d['exit_code'], len([f for f in d['findings'] if f['id']=='D2L-MATERIAL']))"
# 1 1
```

- `D2L-MATERIAL` findings: **1** (the claim, `reject`).
- Findings where `GAR-R13-01` (clean control): only the label-side hold
  `D2L-FORM-UNRESOLVED` — **no material finding** for the control.
- Total findings in the document: 7 = 1 material + 2 form-slot holds
  (`D2L-FORM-UNRESOLVED`, expected for `(to-verify)` form slots) + 4 rank
  conflicts (`R-RANK-CONFLICT`, the tool's static rank ledger; present on the
  live default packet too).

### 2.2 Fail-before / pass-after: the corrected twin loses the finding

A twin of the fixture with **only** `GAR-R13-02`'s era changed E0 → E1 (the
cloth's actual entry stage) was run at the same revision
(`scratch/packet-13-corrected.yml`, sha256
`5fac5090933c2d8f2a59b1640ad420e36f328a9b6c1b6f51f57b1336037450ee`; receipt
`scratch/run-13-corrected.json`, sha256
`fba5017776f5b18a4819d3b780bd9f6c53f70b025e8c33e4558ccd833ecf4eef`):

```sh
python3 tools/d2-typed-labels.py --packet reports/round-8/depth/neg/scratch/packet-13-corrected.yml --json
# exit 1; D2L-MATERIAL findings: 0; GAR-R13-02 now carries only D2L-FORM-UNRESOLVED
```

The `D2L-MATERIAL` finding disappears when — and only when — the unsupported
era scope is corrected. The flag is causally tied to the claim, not to the
record's presence or to background noise.

### 2.3 Independent corroboration — the frozen costume gate

The lane's already-frozen `tools/gates/costume-era-consistency-gate.py`, run
on the same fixture (2026-10-17T17:29:48-03:00; receipt `run-13-gate.txt`,
sha256 `231c95eda7ffa6218147bae0f0d8b02e511a72eb9c5ca137df22ae65bff6726b`):

```sh
python3 tools/gates/costume-era-consistency-gate.py reports/round-8/depth/neg/packet-13.era-material-scope.yml
# exit 1
```

```
FINDING MAT-02: [reject] GAR-R13-02: material 'lowland plant-thread cloth' is explicitly excluded in E0 by `excluded_eras: E0`; a declaration of exclusion is a closed inventory, not an absent-evidence guess
```

Two independent kernels agree on the same record; the new tool's
`R-MAT-ERA-EXCLUDED` and the frozen gate's `MAT-02` are the same verdict in
their own vocabularies.

### 2.4 Re-runnable verifier

`reports/round-8/depth/neg/run-13-reconcile.sh` (sha256
`2d3001d58955f0918f836b5ffadf2759b61d7a1bbdd8698871cb2dc63d797e9c`) asserts
the three expectations above (claim flagged; control unflagged and corrected
twin unflagged; frozen gate agrees) and prints the tool digest it ran. Run at
revision `3548185cd9c10c01523f872930feb407fb9dca58e7d854c295e3a77b0a7a703e`
(2026-10-17T17:30, after D02's next edit):

```sh
sh reports/round-8/depth/neg/run-13-reconcile.sh
# PASS: the reconciliation path flags the claim, the corrected twin passes, the frozen gate agrees.
# exit 0
```

Re-run at revision
`e9209f280c6d765561a47efdee074d0cff5f3e786e5f4f9ae7c96cc65df4a282`
(2026-10-17T17:31, receipt `scratch/run-13-last.txt`): same PASS, and the
fixture-run and gate outputs of that run are byte-identical (`cmp`) to the
`11e23ca9` receipts above — the flagged finding is stable across the observed
revisions, not an artifact of one build.

Expectations are stated on FINDING lines, not exit codes: every tool run also
carries rank-conflict findings from the static rank ledger, so exit codes
alone would not isolate this claim.

## 3. Counts (each with its command and date)

| Count | Value | Command | Date |
|---|---:|---|---|
| claims under test in the fixture | 1 (`GAR-R13-02`) | `grep -c "id: GAR-R13-02" reports/round-8/depth/neg/packet-13.era-material-scope.yml` → `1` | 2026-10-17 |
| clean controls | 1 (`GAR-R13-01`) | `grep -c "id: GAR-R13-01" …` → `1` | 2026-10-17 |
| `D2L-MATERIAL` findings on the fixture | 1 (reject) | §2.1 `python3 -c … len([f for f in … if f['id']=='D2L-MATERIAL'])` → `1 1` | 2026-10-17 |
| `D2L-MATERIAL` findings on the corrected twin | 0 | §2.2 command → `0` | 2026-10-17 |
| material findings on the clean control | 0 | §2.1 (only `D2L-FORM-UNRESOLVED` on `GAR-R13-01`) | 2026-10-17 |
| independent gate findings on the fixture | 1 (`MAT-02` reject) | §2.3 command | 2026-10-17 |

## 4. Where the fixture sits in the D2 schema

The packet is written in the interface the tool consumes: `eras` (tags),
`era_records` (emic names), `materials` (records with `excluded_eras` and
`routes[].eras`), `costumes` (`{id, era, material}`, projected to
reconciliation claims by `claims_from_packet`). The `negative_control` block
at the top of the fixture documents the claim, the plausibility argument, the
unsupportedness basis and the expected flag; it is inert data for the tool.
`form_slot` values are required for the label projection (`_SLOT_RE`,
`LEX-GAR-\d\d`), which is why each costume carries one.

## 5. Revision log and tool-side observations

D02 owns `tools/d2-typed-labels.py` and edited it continuously during this
shard. Observed states, in order:

| Time (-03) | Tool sha256 (short) | Fixture behaviour observed |
|---|---|---|
| 17:26 | `61b61eb4` | exit 2; `D2L-DATA` "costume label carries no label_id for its form slot" ×2 (the fixture then lacked `form_slot`; added) plus 9 rank-shape `D2L-DATA` on the static ledger (also on the live default packet at that revision) |
| 17:27 | `77db23fe` | exit 1; claim flagged (`R-MAT-ERA-EXCLUDED` → `D2L-MATERIAL` reject); corrected twin clean |
| 17:28–17:29 | `6a80ffe4` | fixture: exit 2, stdout empty, stderr `d2-typed-labels error: packet-eras: era scope names must map name -> declared tag` — a transient mid-edit state (the same revision ran the live default packet to exit 1). Evidence: `rev-6a80ffe4-error.txt` |
| 17:29 | `11e23ca9` | exit 1; claim flagged; all receipts refreshed to this revision (`run-13-tool-revision.txt`) |
| 17:30 | `3548185c` | `run-13-reconcile.sh` → PASS (all three expectations) |
| 17:31 | `e9209f28` | runner re-run → PASS; fixture-run and gate outputs byte-identical to the `11e23ca9` receipts (`cmp`; `scratch/run-13-last.txt`) |

`--selftest` was red at every revision where it was attempted
(`scratch/selftest-r8d13.txt`, sha256
`9631d3c5e51610573edfd88a5b39c09d3b9ebc10b9e3a546a519a0809fc843e8`):

- `5d87d346` and `6a80ffe4`: `RecursionError: maximum recursion depth
  exceeded` inside `selftest` (stdout redirection frame repeated).
- `11e23ca9`: `FileNotFoundError: … '/var/tmp/tmpa4obturb/repo/examples/culture-d2/typed-labels.d2.yml'`
  in the fixture mirror.

These are D02's file and D02's acceptance criterion; this shard reports them,
does not repair them, and pins them to hashes so the round's D verdict can be
read against the revision it was measured on.

Environment note: `/tmp` (tmpfs, 1,048,576 inodes) was inode-exhausted by
concurrent workers at 17:13–17:14 and again at 17:27 (`df -i /tmp` →
`1048576 1048576 0 100%`), so scratch evidence for this shard is written
in-lane under `reports/round-8/depth/neg/scratch/`. Any tempfile-based
selftest in the fleet is affected at those times; the 11e23ca9 selftest
failure above uses `/var/tmp` and is not explained by that exhaustion alone.

## 6. Limits

- The fixture is synthetic and NON-CANON. "Unsupported" here means *not
  supported by the packet's own declared facts* (a closed-inventory
  exclusion); it is not a historical claim about any real cloth.
- Receipts are revision-pinned; a later tool revision may produce different
  surrounding findings. The runner re-pins the digest on every run.
- Background findings (`D2L-FORM-UNRESOLVED` ×2, `R-RANK-CONFLICT` ×4) are
  not caused by this fixture and are excluded from the runner's expectations;
  the live default packet shows the same classes.
- Only the era-scope leg is exercised here. The material-merge-by-label
  refusal (`reconcile_material`, "merged by slot id, never by label") was
  observed in an earlier experiment against the tool's previous interface but
  is not part of this shard's receipt set; D12's malformed controls and the
  tool's own selftest carry the loader-side refusals.

## 7. Files written by this shard

| File | sha256 |
|---|---|
| `reports/round-8/depth/neg/packet-13.era-material-scope.yml` | `595cc73fec891b7bb094770ff8c0d7985768f2b0b799c89ab34896782f504867` |
| `reports/round-8/depth/neg/run-13-reconcile.sh` | `2d3001d58955f0918f836b5ffadf2759b61d7a1bbdd8698871cb2dc63d797e9c` |
| `reports/round-8/depth/neg/run-13-observed.txt` | `0f5755061b6ce89931047053dc4ef79234363d7fbdd46aa2cd74f629d4ce5875` |
| `reports/round-8/depth/neg/run-13-observed.json` | `162d080b7362bad79f52bd96540568103fa81a41afd2b1b9d53d817cc9ec4f85` |
| `reports/round-8/depth/neg/run-13-observed.err` | empty (0 bytes) |
| `reports/round-8/depth/neg/run-13-gate.txt` | `231c95eda7ffa6218147bae0f0d8b02e511a72eb9c5ca137df22ae65bff6726b` |
| `reports/round-8/depth/neg/run-13-tool-revision.txt` | `1b5f815bff625b11c4434d5caeecd476273e1bd02dc327e1252d7ce7643c8935` |
| `reports/round-8/depth/neg/rev-6a80ffe4-error.txt` | `4fa00fb72b3fe53dcb4ddd62398f6e2c42a114a465ce71b487080aaba012f846` |
| `reports/round-8/depth/neg/scratch/packet-13-corrected.yml` | `5fac5090933c2d8f2a59b1640ad420e36f328a9b6c1b6f51f57b1336037450ee` |
| `reports/round-8/depth/neg/scratch/run-13-corrected.json` | `fba5017776f5b18a4819d3b780bd9f6c53f70b025e8c33e4558ccd833ecf4eef` |
| `reports/round-8/depth/neg/scratch/selftest-r8d13.txt` | `9631d3c5e51610573edfd88a5b39c09d3b9ebc10b9e3a546a519a0809fc843e8` |
| `reports/round-8/depth/neg/scratch/run-13-check.txt` | `0f5755061b6ce89931047053dc4ef79234363d7fbdd46aa2cd74f629d4ce5875` (runner copy of the fixture run) |
| `reports/round-8/depth/neg/scratch/run-13-corrected-check.txt` | `21daa3323ef6a82dad3f310490cf3a4ca60c5c7ae7356c2851f7a8a225a90766` |
| `reports/round-8/depth/neg/scratch/run-13-gate-check.txt` | `231c95eda7ffa6218147bae0f0d8b02e511a72eb9c5ca137df22ae65bff6726b` |
| `reports/round-8/depth/neg/scratch/run-13-last.txt` | `d0a89ddee35c0da37d7151589967ac19db0e38d80fc18075fae6553267e085e9` (runner output at `e9209f28`) |
| `reports/round-8/depth/neg/report-13.md` | this file |

Reproduce end to end: `sh reports/round-8/depth/neg/run-13-reconcile.sh`.
