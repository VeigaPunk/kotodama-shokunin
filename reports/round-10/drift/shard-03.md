# Drift shard 03 — SKILL.md lines 41-60

- seat: R10-F03 (freshness drift shard 03)
- date: 2026-10-17; run clock 2026-10-17T21:29–21:32Z (`date -u`)
- lane revision: `e3a1ec9435787328ac9f828f96cb6390e4916b8f` (`git rev-parse HEAD`);
  `git status --porcelain` → only untracked `.scratch/` (no tracked byte modified)
- shard region: `SKILL.md:41-60` — sha256
  `9bfca7a70fe12273167c39e52a7dd87bd2a36e150d2583944d7fc843ebac2c24`
  (`sed -n '41,60p' SKILL.md | sha256sum`); whole file as measured `2bce468d…351df1b`.
  Post-measurement, a concurrent worker edited SKILL.md (lines 70+ only, 18+/9-);
  region re-checked at 21:35Z: unchanged (`9bfca7a7…`), so every row in §2 stands
  against the current tree; current whole-file sha256 `17d1326c…f6197c59`.
- scratch: `export TMPDIR=$PWD/.scratch` (in-lane); every command below run from
  the lane root. No file outside the lane was touched; no repo file was edited.

## 1. What the shard contains, and its runnable set

Lines 41-60 are the label-typing decision-table rows (translated-label,
native-form, borrowed-strata conditions, lines 42-47) and the T1–T4 threshold
text (49-60). A backtick sweep of the region (regex over lines 41-60) finds
**no shell-command literal** — the tokens are kind/status names and one
file-line citation. The region's executable content is reached through the
table's authority line `SKILL.md:35` (`tools/d2-typed-labels.py --selftest`)
and through the receipts the table cites (`reports/round-8/depth/skill-table-draft.md`
§2.1, §7, §8). The ledger rows below are that runnable set, carried by those
receipts; each was re-run today.

Boundary: the table header/authority (`SKILL.md:33-40`) and the B4/`D2L-BORROW`
spill (`SKILL.md:61-62`) sit in adjacent shards; recorded here only so the
ledger scribe does not double-count them.

## 2. Ledger rows

| # | command | source locator | exit | observed | output sha256 | verdict |
|---|---|---|---|---|---|---|
| S03-R1 | `grep -c "PHON-INVENTORY" tools/gates/frozen/round-4/naming-collision-gate.out` | SKILL.md:42 claim; receipt skill-table-draft.md:54 | 0 | `10` | stdout `917df3320d778ddbaa5c5c7742bc4046bf803c36ed2b050f30844ed206783469` | current |
| S03-R2 | `grep "PHON-INVENTORY" tools/gates/frozen/round-4/naming-collision-gate.out \| grep -c "GAR-"` | receipt skill-table-draft.md:56; SKILL.md:42 | 0 | `10` | stdout `917df332…783469` | current |
| S03-R3 | `sha256sum tools/gates/frozen/round-4/naming-collision-gate.out` | receipt skill-table-draft.md:52 / §8 pin | 0 | `4d70252bdf7745dea76af07b41a94560b5789ff278cdbb5af4bf6924688bb19e` = receipt pin, byte-equal | stdout `c95330e1a84a00b93b5dea2b70d44cd5284287a055e523caab47ba3c2db9b489` | current |
| S03-R4 | `python3 tools/d2-typed-labels.py --selftest` | SKILL.md:35 (table authority); receipt skill-table-draft.md:285-292 | 0 | `selftest: 39/39 checks passed — …no file outside the temporary directory touched`; stderr 0 bytes | stdout `7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252` | current |
| S03-R5 | citation resolution: `corpus/knowledge/synthesis/loanword-material-dating.md:43-57` | SKILL.md:58 (T3) | n/a (read) | lines 43-57 = §3 header + items 1-6 + diagnostic-table rows 53-57; all five T3 discriminators present | region `de242da40c9badf7073b9c53bb684be808ab9b18ec1edb2f123c20222882cce2`; file `5b1d75ab…6103db4d58` | current |

Notes:

- R1+R2 verify the SKILL.md:42 claim "10/10 of the frozen round-4
  `PHON-INVENTORY` class are this": the ten findings were read in full
  (`tools/gates/frozen/round-4/naming-collision-gate.out:8-17`) and each names
  an English `GAR-*` garment label. The file is legacy-unpinned by the replay
  protocol (`SKILL.md:178-179`), so the hash agreement is receipt-level, not a
  MANIFEST pin.
- R4 hash equality: byte-identical to the round-8 admitted value in
  `reports/round-8/validation.json` (claims.D selftest stdout sha256) and to
  `reports/round-9/d3/interop.md:41` — a reproduction, not a new run result.
- R5 line map for T3: dated witness + usage status `:46`; channel separation
  (etymon/donor/carrier) `:47`; recurring correspondences `:48`; donor-side
  chronology `:49`; field/register clustering `:51`.

## 3. Named checks in rows 42-47 / T1-T4 vs the live executable

Live authority `tools/d2-typed-labels.py` sha256
`0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`.

- Row 42 routing (declared gloss / whitespace-gloss syntax / out-of-inventory
  segment routes off the sound channel): selftest control `live packet: no GAR
  label is graded on the sound channel` (`tools/d2-typed-labels.py:2670`).
- Row 43 "native bytes govern; still FAIL": hold branch `label_id … has no
  supplied native/borrowed form` (`:793`, `hold=True`); selftest `live packet:
  the owed form slots stay held, never passed` (`:2668`).
- Row 44 `D2L-FORM-UNRESOLVED`: constant `:426`, finding class `:423`, code map
  `:2241-2242` (`E-LABEL-GLOSS`, `W-LABEL-TOVERIFY`), hold branches `:793`,
  `:796`.
- Row 45 five borrow-ledger checks in `check_borrow` (`:692-731`): layer
  resolves `:701-704` (FAIL); donor separated `:706-710` (HOLD); substitutions
  reproduce `:711-719` (FAIL; selftest `spec B3: substitutions that do not
  derive the form are D2L-BORROW`); clocks ordered `:720-724` (FAIL;
  design-spec B4 `reports/round-8/depth/design-spec.md:210-217`); **domain/
  register declared — no validating branch (finding S03-01)**.
- Row 46 `to-verify` with one discriminator: same D2L-FORM-UNRESOLVED hold
  path; T3/T5 counts are house policy, not executable — the receipt itself
  says so (`skill-table-draft.md:282-284`), consistent with observed tool
  behaviour.

## 4. Findings

### S03-01 — SKILL.md:45 "domain/register declared" is carried but not gated (low; control demonstrated)

- Claim under test: SKILL.md:45 checked channel lists borrow-ledger checks
  including "domain/register declared".
- Observation: `check_borrow` has no branch testing register or channel;
  `grep -n 'B5' tools/d2-typed-labels.py` → 0 hits. The projection sets
  `register` ← `entry.field` (`:558`) and `channel` ← the layer record (`:576`)
  but nothing validates their presence. Design-spec B5
  (`reports/round-8/depth/design-spec.md:219-222`) requires the borrow record
  to carry register/domain, and the receipt sentence "the executable tool
  enforces the declaration, hold and borrow-ledger rules"
  (`skill-table-draft.md:283-284`) reads as covering it.
- Control (demonstrated, mutant vs baseline):
  - baseline: `python3 tools/d2-typed-labels.py --packet examples/culture-d2/packet.d2.yml --json`
    → exit 1; stats `{fail 0, hold 15, note 1, labels 58}`; stdout sha256
    `880d0e45f75f1c14c9528a80a70ff1b6d1c034145ed741796f7038f03c124624`.
  - mutant: `.scratch/ctrl-packet.yml` = packet copy with `field:` removed from
    both loan entries (`kas` :841, `per` :857) and both layer `channel:` lines
    removed (:2545, :2561); same command → exit 1, identical stats, findings
    set symmetric-difference **0**; stdout sha256
    `7bd56fb9050e0b9698fc8dcc980edbf098c8643fdb6430f3d2cd53adecec1ff7`.
  - mutant labels L-26 `kas`, L-27 `per`: still `kind: borrowed-strata`,
    `register=None`, `channel=None` (module-level projection check).
- Disposition recommended for F15–F18: either add a B5 branch (register/domain
  presence on a supplied borrowed-strata record) or amend the SKILL.md/receipt
  wording to "declared by the author, carried by the projection — not gated".
  Do not leave silent.

### S03-02 — receipt hash pins are historical snapshots, not live pins (documented; no live staleness)

`skill-table-draft.md` §7/§8 (hashes "as read 2026-10-17 … 20:19–20:25Z",
working tree `cf338a7`) record `tools/d2-typed-labels.py` at `623b5b1f…` with
`32/32 checks passed`, and `loanword-material-dating.md` at `bb08d458…`.
Live/committed values: tool `0da0015f…` (39/39, == round-8 `validation.json`
and `reports/round-9/d3/interop.md:51`); corpus file `5b1d75ab…` (== at
`e1694ba` and at HEAD). `git log` on both paths: last commit `e1694ba`
(round-8 admission) — the receipt pins are pre-commit mid-shard reads,
superseded by the admitted receipts. Verdict: **stale-documented** (historical
receipt; filed report bytes not rewritten, per the F rule; nothing to fix on a
live surface).

Boundary, not a shard command: `tools/d2-typed-labels.py --check` exits 1 with
a stale one-line packet pin — already recorded in `reports/round-9/d3/scribe.md:90`
(D06 §4); `--check` is not cited in SKILL.md:41-60.

## 5. Negative sweeps

- Web-only citations in the region: **0** (`sed -n '41,60p' SKILL.md | grep -c 'http'`
  → `0`), so no access attempt is owed for this shard.
- Shell-command literals in the region: **0** (backtick sweep, §1) — the
  region's runnable set is exactly the five rows in §2.

## 6. Ledger handoff (for R10-F14 merge)

```json
[
 {"command": "grep -c \"PHON-INVENTORY\" tools/gates/frozen/round-4/naming-collision-gate.out",
  "source_locator": "SKILL.md:42 via reports/round-8/depth/skill-table-draft.md:54",
  "round10_verdict": "current",
  "output_sha256": "917df3320d778ddbaa5c5c7742bc4046bf803c36ed2b050f30844ed206783469", "exit": 0},
 {"command": "grep \"PHON-INVENTORY\" tools/gates/frozen/round-4/naming-collision-gate.out | grep -c \"GAR-\"",
  "source_locator": "reports/round-8/depth/skill-table-draft.md:56; SKILL.md:42",
  "round10_verdict": "current",
  "output_sha256": "917df3320d778ddbaa5c5c7742bc4046bf803c36ed2b050f30844ed206783469", "exit": 0},
 {"command": "sha256sum tools/gates/frozen/round-4/naming-collision-gate.out",
  "source_locator": "reports/round-8/depth/skill-table-draft.md:52 / §8 pin",
  "round10_verdict": "current",
  "output_sha256": "c95330e1a84a00b93b5dea2b70d44cd5284287a055e523caab47ba3c2db9b489", "exit": 0},
 {"command": "python3 tools/d2-typed-labels.py --selftest",
  "source_locator": "SKILL.md:35 (table authority); reports/round-8/depth/skill-table-draft.md:285-292",
  "round10_verdict": "current",
  "output_sha256": "7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252", "exit": 0},
 {"command": "sed -n '43,57p' corpus/knowledge/synthesis/loanword-material-dating.md (citation resolution)",
  "source_locator": "SKILL.md:58",
  "round10_verdict": "current",
  "output_sha256": "de242da40c9badf7073b9c53bb684be808ab9b18ec1edb2f123c20222882cce2", "exit": 0}
]
```

Shard summary: 5/5 re-run items current; 1 enforcement finding (S03-01, control
demonstrated); 1 documented historical-pin item (S03-02); zero silent
staleness.
