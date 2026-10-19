# O01 — the freshness gate's first live use: replay, controls, and what the probes actually measured

- Seat: `O01` | role verifier | claim: **cross** | round 48, loop 2, position 2
- Mission (`reports/round-48/targets.json`, seat O01): "re-run `tools/harness/claims-freshness.py` on the r48 candidates overlay; confirm it flags the dropped O claim stale and would flag a stale C/Ca; document the gate's first live use."
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, seat start; equals `reports/round-48/claims.json:7`)
- Out path: `reports/round-48/op/O01-gate-live.md` — the only durable write by this seat. All scaffolding is under `.scratch/o01-r48/`; no corpus/tools edit, no filed-byte edit, no `run-validation.py`, no git mutation, install, or network.
- Environment: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, Python 3.14.7, commands from the lane root.

**Verdict. The declared verdicts reproduce; only one of the three checks measures its clause.** At `a01405d`, using the surviving declaration inputs, the gate returns exactly **O stale, C fresh, Ca fresh, exit 1**, and its controls are sound: a fresh-only run exits 0, a polarity mutant turns C and Ca stale, an uncheckable claim exits 3, malformed input exits 2, `--no-exec` cannot manufacture freshness, repeated runs are byte-identical, and measurement is baseline-only. But the O check is an **isolation artefact** (it runs the resolver's `--selftest` in a one-file corpus and reads the non-zero exit, not the fixture) and the Ca check is a **tautology** (it counts files, not headings, and its declared `expect: false` is silently overwritten by `target.value`). Only C's checks measure what their clauses say. The three factual dispositions still hold when re-measured with valid probes — the O drop is real, the README duplicate is real, cartography is unowned — but the first live use did not establish them. Inputs survive only in `.scratch`, not in any filed path.

---

## 1. Tool identity and self-test

```
$ sha256sum tools/harness/claims-freshness.py
466aa60d247293e33907d608b565fe8acd91a04b6e38049e1bffdb6d5bfa858d
$ python3 -B tools/harness/claims-freshness.py --selftest ; echo rc=$?
SELFTEST OK: registry 43/43 + seam 19/19 controls
rc=0
$ grep -c '^PASS ' .scratch/o01-r48/selftest.out   # 62
$ grep -c '^FAIL ' .scratch/o01-r48/selftest.out   # 0
```

The closed probe vocabulary at `tools/harness/claims-freshness.py:96` is the seven kinds the round names: `path_absent`, `path_present`, `grep_absent`, `count_eq`, `sha256_eq`, `topic_owner_absent`, `capability_present`. Exit constants are `0/1/2/3` (`:89-92`); the overlay loader and its `claims_sha256` pin are at `:2324`.

**G1 (minor contract deviation, non-blocking).** The landed tool sets `VERSION = "2.0-part1"` (`:87`) but exposes no `--version` flag, and the JSON report has no `version` field (report keys observed: `baseline_commit, baseline_sha, claims, decision_sha256, errors, exit_code, refusal, refuse, round, run_verdict, schema, summary`).

```
$ python3 -B tools/harness/claims-freshness.py --version
claims-freshness.py: error: unrecognized arguments: --version
rc=2
```

`reports/round-47/scout/K03-gate-spec.md:95` requires "`--version` | print version and exit 0". No verdict depends on it (the tool is identified by sha), but a successor row should carry it: owner integrator, next touch next tool edit, evidence this command. Do not re-freeze the tool this round.

## 2. The declaration's inputs: recoverable only from `.scratch`

The r47 round landed and demonstrated the gate as a regression on r43's claims; r48 is its first use to decide a round's dispatch. The declaration records the command but not its inputs:

```
$ grep -n '<candidates>\|<overlay>' reports/round-48/claims.json
22:  "command": "python3 tools/harness/claims-freshness.py --claims <candidates> --checks <overlay>",
$ grep -n 'freshness_gate_first_live_use' -A 3 reports/round-48/telemetry/dispatch-declared.json
18: "freshness_gate_first_live_use": {
19:  "command": "python3 tools/harness/claims-freshness.py --claims <candidates> --checks <overlay>",
20:  "result": "O STALE (candidate premise false — dropped from the round, not dispatched); C FRESH; Ca FRESH. ..."
$ find reports/round-48 -iname '*candidate*' -o -iname '*overlay*' | wc -l
0
```

Two scratch files carry the closest surviving bytes, both mtime `2026-10-19 16:35:51 -0300` = `19:35:51Z`, nine minutes before `declared_at_utc 19:45:00Z`:

| supposed role | path | sha256 |
|---|---|---|
| candidates skeleton | `.scratch/r48-claims-skel.json` | `65b8644146f235e51d70211c4d2650fd97a699db6a089668d3edfa1f254a5080` |
| checks overlay | `.scratch/r48-freshness-check.json` | `7acbd8ca5fa79d3fff5efee3738e4111e8a6a3de3ace490195b4664982813c13` |

Nothing pins them to the declaration: the overlay carries no `claims_sha256`, and `load_overlay` only verifies a pin when one is present (`tools/harness/claims-freshness.py:2330-2339`). Their plausibility rests on mtime and content. This is the condition AGENTS.md forbids for dispatch evidence ("land the … native dispatch/result extracts needed to reproduce every reported count … never only `.scratch`"). **Recommendation to the integrator/S02:** file both under `reports/round-48/telemetry/` as a new append-only snapshot with shas and the caveat that pinning is unavailable; do not rewrite the declaration.

## 3. Two input sets, reproduced in full

### 3.1 Set D — the surviving declaration inputs

`.scratch/r48-claims-skel.json` (sha256 `65b86441…`):

```json
{
 "round": 48,
 "baseline_commit": "a01405d",
 "claims": [
  {"id": "C", "axis": "coverage", "before": "total 223; cartography verified-fresh unowned gap"},
  {"id": "O", "axis": "operability", "before": "resolver drops blank-separated hyphen soft-wrap tokens (latent edge)"},
  {"id": "Ca", "axis": "calibration", "before": "README duplicate-heading + r47 over-build defect undispositioned"}
 ]
}
```

`.scratch/r48-freshness-check.json` (sha256 `7acbd8ca…`), verbatim:

```json
{
 "schema": "kotodama-claims-freshness-checks-v1",
 "round": 48,
 "baseline_commit": "a01405d",
 "checks": {
  "C": [
   {"clause": "cartography unowned", "probe_kind": "topic_owner_absent",
    "target": {"topics": ["cartography", "mapmaking", "portolan", "cadastral"],
               "partition": "culture-material", "fields": ["H1", "topic", "gap filled"]},
    "expect": true,
    "evidence_command": "git grep -niE 'cartograph|mapmak|portolan|cadastr' a01405d -- corpus/knowledge/culture-material/"},
   {"clause": "culture-material 25", "probe_kind": "count_eq",
    "target": {"glob": "corpus/knowledge/culture-material/*.md", "value": 25}, "expect": true,
    "evidence_command": "git ls-tree -r --name-only a01405d -- corpus/knowledge/culture-material | wc -l"}
  ],
  "O": [
   {"clause": "resolver blank-hyphen edge", "probe_kind": "capability_present",
    "target": {"globs": ["tools/harness/basename-couples-resolver.py"], "exclude_globs": [],
               "argv": ["--selftest"],
               "fixture": {"corpus/knowledge/linguistics/phonetics-phonology.md":
                           "- couples: a — `x.md`; prospective sibling files: tone-\n\n  prosody.md\n"},
               "success_regex": "drops|0 tokens|prosody", "timeout_s": 30, "max_candidates": 4},
    "expect": true, "evidence_command": "resolver selftest on blank-separated hyphen fixture"}
  ],
  "Ca": [
   {"clause": "README duplicate heading", "probe_kind": "count_eq",
    "target": {"glob": "corpus/README.md", "value": 1}, "expect": false,
    "evidence_command": "grep -c '^# kotodama-shokunin corpus index' corpus/README.md -> 2"}
  ]
 }
}
```

### 3.2 Set R — my corrected overlay

`C` and `Ca` `before` strings are byte-copies of `reports/round-48/claims.json`; O carries its own reconstruction label. `candidates.json` sha256 `4c576bc85bd02832b05206cc8a088063e3ee9225cc866ada142a82297a451238`:

```json
{
 "round": 48, "baseline_commit": "a01405d",
 "replay_note": "O01 corrected replay. C and Ca `before` are byte-copied from reports/round-48/claims.json. O's `before` is a reconstruction because the original candidate prose is not filed.",
 "claims": [
  {"id": "C", "axis": "coverage",
   "before": "total 223; cartography verified-fresh unowned (gate-confirmed at declaration); r47's draft was over-built + defective and was correctly not landed"},
  {"id": "Ca", "axis": "calibration",
   "before": "README carries a duplicate H1 (lines 1 and 3, verified grep count 2); the r47 over-build defect (draft 790 lines + R03 B1-B9) is undispositioned; no heading-count control exists in the sweep"},
  {"id": "O", "axis": "operability",
   "before": "Reconstruction (original candidate bytes not filed; see reports/round-48/claims.json:19): the resolver treats a blank-separated hyphen continuation in a couples field as a hyphen soft-wrap — the field is reported wrapped=True with both tokens and no reference is dropped."}
 ]
}
```

`overlay.json` sha256 `4099dbe26926fed74ea3025377a494542abcb60c7338096b3c4079d406cdf68b`:

```json
{
 "schema": "kotodama-claims-freshness-checks-v1",
 "round": 48, "baseline_commit": "a01405d",
 "claims_sha256": "4c576bc85bd02832b05206cc8a088063e3ee9225cc866ada142a82297a451238",
 "checks": {
  "C": [
   {"id": "c-total-223", "clause": "total 223", "probe_kind": "count_eq",
    "target": {"glob": "corpus/knowledge/*/*.md"}, "expect": 223,
    "evidence_command": "git ls-tree -r --name-only a01405d -- corpus/knowledge | grep -c '\\.md$'"},
   {"id": "c-cartography-unowned", "clause": "cartography verified-fresh unowned",
    "probe_kind": "topic_owner_absent",
    "target": {"topic": ["cartograph", "mapmaking", "portolan", "cadastral"],
               "partitions": ["civilizations", "culture-material", "linguistics", "myth-symbol", "synthesis", "verification"],
               "fields": ["h1", "topic", "gap filled"], "mode": "word"},
    "expect": true,
    "evidence_command": "grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/"},
   {"id": "c-slug-free", "clause": "cartography verified-fresh unowned", "probe_kind": "path_absent",
    "target": {"path": "corpus/knowledge/culture-material/cartography-and-mapmaking.md"}, "expect": true,
    "evidence_command": "ls corpus/knowledge/culture-material/cartography-and-mapmaking.md"}
  ],
  "Ca": [
   {"id": "ca-dup-h1-present", "clause": "README carries a duplicate H1 (lines 1 and 3, verified grep count 2)",
    "probe_kind": "grep_absent", "target": {"glob": "corpus/README.md", "regex": "^# kotodama-shokunin corpus index"},
    "expect": false, "evidence_command": "grep -c '^# kotodama-shokunin corpus index' corpus/README.md"},
   {"id": "ca-no-heading-control", "clause": "no heading-count control exists in the sweep",
    "probe_kind": "grep_absent", "target": {"glob": "reports/round-28/readme/sweep.py", "regex": "heading"},
    "expect": true, "evidence_command": "grep -ni heading reports/round-28/readme/sweep.py"},
   {"id": "ca-readme-pin", "clause": "README carries a duplicate H1 (lines 1 and 3, verified grep count 2)",
    "probe_kind": "sha256_eq", "target": {"path": "corpus/README.md"},
    "expect": "7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd",
    "evidence_command": "git cat-file blob a01405d:corpus/README.md | sha256sum"}
  ],
  "O": [
   {"id": "o-blank-hyphen-classified-wrapped",
    "clause": "the resolver treats a blank-separated hyphen continuation in a couples field as a hyphen soft-wrap",
    "probe_kind": "capability_present",
    "target": {"globs": ["tools/harness/basename-couples-resolver.py"], "exclude_globs": [],
               "argv": ["corpus/knowledge/culture-material/zz-fixture.md"],
               "fixture": {"corpus/knowledge/culture-material/zz-fixture.md":
                           "# Fixture\n\n- topic: fixture\n- couples: method — `writing-systems.md`; language — `tone-\n\n  prosody.md`\n- verified-at: 2026-10-19\n",
                           "corpus/knowledge/linguistics/writing-systems.md": "# Writing systems\n\n- topic: writing systems\n"},
               "success_regex": "wrapped=True tokens=2", "timeout_s": 20, "max_candidates": 4},
    "expect": true,
    "evidence_command": "python3 -B tools/harness/basename-couples-resolver.py <blank-hyphen fixture>"}
  ]
 }
}
```

## 4. Live run matrix at `a01405d`

All runs used `--json`; `exit` is the process exit code (not the shell's `$?` after a pipe).

| run | inputs | O | C | Ca | run verdict | exit | decision sha256 (first 16) |
|---|---|---|---|---|---|---|---|
| **D** | surviving declaration set (§3.1) | stale | fresh | fresh | stale | **1** | `a7739149914edea2` |
| R | corrected set (§3.2) | stale | fresh | fresh | stale | **1** | `1029225e7db8dd91` |
| R2 | same, repeated | stale | fresh | fresh | stale | 1 | `1029225e7db8dd91` (identical) |
| fresh control | C+Ca only, true premises | — | fresh | fresh | fresh | **0** | `1dbc95a3531eac7f` |
| mutant | C/Ca declared polarity flipped | stale | **stale** | **stale** | stale | **1** | `28307a547003ca4f` |
| no checks | candidates, no `--checks` | CNE | CNE | CNE | could-not-evaluate | **3** | `a11f9a3b596adce6` |
| malformed | unknown `probe_kind` | — | — | — | malformed | **2** | `b1a91a53fab2fef5` |
| `--no-exec` | candidates + overlay | CNE | fresh | fresh | could-not-evaluate | **3** | `3d5ac6accdea8561` |

Run D's refusal line is exactly the contract's:

```
REFUSE: claim(s) O have a `before` already false at a01405d; do not dispatch.
```

Per-clause detail for D:

```
C  HOLDS topic_owner_absent  measured=True  (0 owner(s): none)
C  HOLDS count_eq            measured=25    (culture-material/*.md -> 25 file(s))
Ca HOLDS count_eq            measured=1     (corpus/README.md -> 1 file(s))   <- tautology, see §6-§7
O  CONTRADICTED capability_present measured=False (0/1 candidate(s) pass)    <- artefact, see §5
```

Per-clause detail for R (same verdicts, valid probes):

```
C  HOLDS count_eq            measured=223 expected=223  (paths_sha256=2cb71c5e211c8421)
C  HOLDS topic_owner_absent  measured=True              (0 owner(s): none)
C  HOLDS path_absent         measured=True              (cartography-and-mapmaking.md is absent)
Ca HOLDS grep_absent         measured=False expected=False (corpus/README.md ... -> 2 hit(s))
Ca HOLDS grep_absent         measured=True              (reports/round-28/readme/sweep.py /heading/ -> 0 hit(s))
Ca HOLDS sha256_eq           measured=7c788a1d… expected=7c788a1d…
O  CONTRADICTED capability_present measured=False expected=True (0/1 candidate(s) pass)
```

## 5. The O check measured isolation, not the blank-hyphen edge

The resolver fixture is the blank-separated hyphen continuation from the r47 latent-edge record, with a complete reference before the wrap so the field is non-empty:

```
- couples: method — `writing-systems.md`; language — `tone-

  prosody.md`
```

Direct measurement (`.scratch/o01-r48/hyphen_blank_2tok.md`):

```
$ python3 -B tools/harness/basename-couples-resolver.py .scratch/o01-r48/hyphen_blank_2tok.md
... wrapped=False tokens=1
    writing-systems.md   fallback   corpus/knowledge/linguistics/writing-systems.md
```

The code path is `tools/harness/basename-couples-resolver.py:73`, `soft_wrap = parts[-1].endswith("-") and not saw_blank`: the blank line suppresses the hyphen exception, so the indented continuation is never joined and one reference is silently lost. The non-blank control heals as designed:

```
$ python3 -B tools/harness/basename-couples-resolver.py .scratch/o01-r48/hyphen_noblank.md
... wrapped=True tokens=2
    tone-prosody.md   unresolved   dangling-reference
    writing-systems.md   fallback  corpus/knowledge/linguistics/writing-systems.md
```

**Why the declared check says stale anyway.** Set D uses `capability_present` with `argv: ["--selftest"]` and `success_regex: "drops|0 tokens|prosody"`. The probe copies the resolver into a temp tree containing only the fixture and runs the selftest there. In that one-file corpus the selftest fails 6/27 controls and exits 1:

```
$ cd .scratch/o01-r48/iso && python3 -I -B tools/harness/basename-couples-resolver.py --selftest | tail -2
SELFTEST FAIL: 21/27 controls
  failed: S1a embedded fixture == live bytes at :1, S1f live field resolves 2 direct + 2 unresolved …, S4a …, S4b …, S4c …, S10 …
exit=1
```

`_probe_capability_present` requires `returncode == 0 AND success_regex` (`tools/harness/claims-freshness.py:1180`), so `measured=False` follows from the isolation exit code. The regex is not innocuous either: the selftest output on the real corpus contains `prosody` (control S1c), so had the probe run in-tree it would have matched incidental text and measured **true** without ever reading the fixture. Either way the check does not observe the blank-hyphen behavior.

**Consequence for the round record.** The surviving skeleton states the premise as "resolver drops blank-separated hyphen soft-wrap tokens (latent edge)" — and that premise is **true** by direct measurement (`tokens=1` instead of 2: one token is dropped). The declaration's "premise was false as framed" is therefore not established by the run it cites. The drop of claim O may still be the right *dispatch* decision (the edge is a carried, already-filed latent defect with 0/223 live incidence, as the r47 Ca02 record measured), but the gate is not its evidence. Independent seats reached the same split: `reports/round-48/op/O02-resolver-edge.md` ("the drop is correct as a dispatch decision … the stated ground is wrong") and `reports/round-48/op/O04-gate-replay.md` ("O contradicts for a corpus-isolation artefact"). My corrected probe (set R) reproduces `stale` honestly, but only because it declares the narrower, false half — that the field is reported `wrapped=True tokens=2`.

## 6. C and Ca: what actually held

- **C is gate-sound.** It holds on three independent measurements: 223 two-level entries (`count_eq`), zero owners of the cartography terms across all six partitions' `h1`/`topic`/`gap filled` fields (`topic_owner_absent`), and absence of the proposed slug (`path_absent`). The gate is also baseline-only: `reports/round-48/claims.json` exists in the worktree but a `path_present` check for it at `a01405d` measures false (`claims-worktree-control.json`, exit 0).
- **Ca is vacuous in the declaration and presence-only in my correction.** Set D's Ca check is `count_eq` on `corpus/README.md`: that counts the one file named `corpus/README.md`, which is 1 regardless of how many H1 lines it contains; the declared `expect: false` never participates because `_coerce_check` replaces `expect` with `target.value` (`tools/harness/claims-freshness.py:2193-2196`). My corrected check at least measures heading presence and reports `2 hit(s)`, but it is still boolean. The duplicate itself is verified independently: `grep -c '^# kotodama-shokunin corpus index' corpus/README.md` → `2`, at lines 1 and 3, and the baseline blob is pinned at `7c788a1d…`. The fix's acceptance test must remain that external `grep -c` (2 → 1), not any gate check.

## 7. Two measured limits (and one input-integrity footgun)

**(a) No in-file occurrence count.** `count_eq` counts **files** (`:1053`); `grep_absent` is boolean over any hit (`:1039`). Using the tool's own `FixtureTree` and probe functions:

```
headings=1 | grep_absent expect=False -> holds (measured=False, ... -> 1 hit(s)) | count_eq expect=1 -> holds (measured=1)
headings=2 | grep_absent expect=False -> holds (measured=False, ... -> 2 hit(s)) | count_eq expect=1 -> holds (measured=1)
headings=3 | grep_absent expect=False -> holds (measured=False, ... -> 3 hit(s)) | count_eq expect=1 -> holds (measured=1)
```

A `count_eq` check on `corpus/README.md` is therefore vacuous as a duplicate-heading guard: it holds on zero, one, or five headings.

**(b) `expect` is silently discarded for `count_eq` with `value`.** `_coerce_check` (`:2193-2196`) overwrites the declared boolean with `target.value`, so an overlay can declare `expect: false` beside `value: 1` and the tool neither errors nor records the contradiction. That is exactly what happened in Set D's Ca check. Any successor should either reject the combination (`expect` and `value` both present and disagreeing) or document that `value` wins; today the overwrite is invisible in the report.

**(c) Recommendation.** The heading-count control (seat Ca05) must live outside the seven-probe vocabulary this round — in `reports/round-28/readme/sweep.py` or as a separate one-line assertion — and a future gate extension (`line_count_eq` or `regex_count_eq` with an exact integer, plus the `expect`/`value` guard) should be filed as a queue successor with owner + evidence, not implied by this round's wording.

## 8. Assessment of the first live use

The gate's **mechanics** are sound: it refused dispatch, did not flag the claims whose premises held, caught polarity flips, never turned an absent check green, aborted malformed input before verdicts, and produced a byte-identical decision digest on repeat. Its **probe quality** is the weak link: of the three checks in the declaration, one (C) measured its clause, one (O) measured the test harness's own isolation, and one (Ca) measured an unrelated file count. The correct reading of the first live use is therefore: the gate produced the declared verdicts, but only the C verdict is evidence; the O drop and the Ca defect are supported by independent measurements, and the round record should not cite the gate as having refuted the O premise. It also remains a **topic-ownership/freshness** guard, not an entry-quality guard: none of the seven probes measures draft length, arithmetic, or citation anchoring, so the r47 over-build class (790 lines, R03 B1-B9) is outside its scope and still needs the separate disposition the Ca claim assigns.

## 9. Reproduction

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
# Set D (surviving declaration inputs)
python3 -B tools/harness/claims-freshness.py --claims .scratch/r48-claims-skel.json \
        --checks .scratch/r48-freshness-check.json --json ; echo rc=$?   # rc=1, digest a7739149…
# Set R (corrected probes; fenced in §3.2)
python3 -B tools/harness/claims-freshness.py --claims .scratch/o01-r48/candidates.json \
        --checks .scratch/o01-r48/overlay.json --json ; echo rc=$?       # rc=1 (R)
python3 -B tools/harness/claims-freshness.py --claims .scratch/o01-r48/claims-fresh-only.json \
        --checks .scratch/o01-r48/overlay-fresh-only.json --json ; echo rc=$?  # rc=0
python3 -B tools/harness/claims-freshness.py --claims .scratch/o01-r48/candidates.json \
        --checks .scratch/o01-r48/overlay-mutant.json --json ; echo rc=$?  # rc=1, C+Ca stale
python3 -B tools/harness/claims-freshness.py --claims .scratch/o01-r48/candidates.json --json ; echo rc=$?  # rc=3
python3 -B tools/harness/claims-freshness.py --claims .scratch/o01-r48/candidates.json \
        --checks .scratch/o01-r48/overlay-malformed.json --json ; echo rc=$?  # rc=2
python3 -B tools/harness/claims-freshness.py --selftest ; echo rc=$?      # rc=0, 62/62
```

Recorded digests: tool `466aa60d…`; declaration skeleton `65b86441…`; declaration overlay `7acbd8ca…`; corrected candidates `4c576bc8…`; corrected overlay `4099dbe2…`; overlay-fresh-only `9d0e1e0b…`; overlay-mutant `61c6d78e…`; overlay-malformed `d4f89e2d…`; claims-fresh-only `ade31828…`. Probe timestamps are absent by design (selftest control 12); `date -u` at seat work read `2026-10-19T19:40Z`, four minutes before the declaration's `recorded_at_utc` of `19:45Z` — a clock/provenance observation for X04/S02, not a gate result.

## Owed

- **Durability:** file `.scratch/r48-claims-skel.json` + `.scratch/r48-freshness-check.json` under `reports/round-48/telemetry/` as an append-only snapshot with shas; record that no pin to the declaration exists and that the O candidate prose is `to-verify`.
- **O ground:** the round record should not state that the gate refuted the O premise. The drop stands on the carried/0-incidence ground (`reports/round-47/calib/Ca02-resolver-edge.md`; `reports/round-48/op/O02-resolver-edge.md`).
- **Successor rows:** G1 (`--version`/report version vs `reports/round-47/scout/K03-gate-spec.md:95`); G2 (`count_eq` `value` overwriting `expect`, `:2193-2196`); G3 (no in-file occurrence probe). Owner integrator, evidence this file §7 and the commands above. No tool change this round.
- **Ca05:** the heading-count control must not be implemented as a `count_eq` check; the external `grep -c` remains the acceptance test.
