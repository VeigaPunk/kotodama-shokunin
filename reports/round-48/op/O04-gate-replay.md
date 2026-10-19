# O04 — freshness-gate replay (round 48)

- Seat `O04` | role verifier | claim **cross** | out `reports/round-48/op/O04-gate-replay.md`
- Baseline `a01405d` = `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19T19:41Z; no drift: `git diff --stat a01405d..HEAD` empty, `git status --porcelain -- corpus/ tools/` empty)
- Observed 2026-10-19T19:38–19:42Z
- Gate `tools/harness/claims-freshness.py` sha256 `466aa60d247293e33907d608b565fe8acd91a04b6e38049e1bffdb6d5bfa858d`, 2717 lines
- Non-author: I drafted no fragment I review and wrote no corpus byte. This file is the only path I wrote.

**Judgment.** The declared verdicts — `C FRESH`, `Ca FRESH`, `O STALE` — **do reproduce** (`exit 1`, decision digest `4165d34d13d15cb71c1a047c151b241a3c53cfcc010a8c09c9c6bee4abf996ff`, identical across two runs). But reproduction required a **reconstructed** candidates document: the declaration's candidates file was never filed. The exact declared inputs against the filed bytes are **malformed, exit 2**. Two of the three checks also do not measure what their clauses say: **Ca is a tautology** (it counts files, not headings) and **O contradicts for a corpus-isolation artefact**, not the blank-hyphen edge. Only **C** is gate-sound. The factual dispositions happen to be right for Ca and O; the gate is not what establishes them.

## 1. Inputs and their durability

| Input | Path | sha256 | Filed? |
|---|---|---|---|
| claims (post-gate) | `reports/round-48/claims.json` | `bf8df21b641c1a49a7b71eb46504210a58096dda3f2cefa6c7618b1200535292` | yes (untracked round dir) |
| checks overlay | `.scratch/r48-freshness-check.json` | `7acbd8ca5fa79d3fff5efee3738e4111e8a6a3de3ace490195b4664982813c13` | **no — only `.scratch`** |
| declaration candidates doc | **absent** | — | **no** |
| replay candidates (mine) | `.scratch/o04/claims-replay.json` | `5dc5ef1773ff202b374cc5e557f238e305134e3ac556a5d49b16152fad2c9429` | no — drafted in §6 |
| replay report (mine) | `.scratch/o04/replay.json` | `074bf9fd3de5bd980f64c4791402988dddb2af9aa72d73cfeaafac14b523d0a0` | no — drafted in §6 |

The overlay mtime is `2026-10-19 16:35:51 -0300` = `19:35:51Z`, nine minutes before `declared_at_utc 19:45:00Z` (`reports/round-48/claims.json:6`), so it is plausibly the declaration's bytes. Nothing pins it: the overlay carries no `claims_sha256` (`tools/harness/claims-freshness.py:2330-2339` only checks a pin when present). `AGENTS.md:17-19` requires dispatch evidence under `reports/round-48/telemetry/`, "never only `.scratch`"; the declaration filed only the *result* (`reports/round-48/telemetry/dispatch-declared.json:18-20`) and neither input.

## 2. Exact replay against the filed bytes — malformed, exit 2

```console
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ python3 -B tools/harness/claims-freshness.py \
    --claims reports/round-48/claims.json \
    --checks .scratch/r48-freshness-check.json
claims-freshness: round 48 baseline a01405d (unresolved)
summary: 0 fresh, 0 stale, 0 could-not-evaluate, 0 malformed; clauses 0 (0 hold, 0 contradict, 0 not evaluated); 1 document error(s)
error: .scratch/r48-freshness-check.json: overlay names claim 'O', absent from the claims file
REFUSE: input is malformed at a01405d: ...; exit 2 -- no freshness verdict is possible.
exit 2
```

This is the gate working as designed: `load_overlay` refuses an overlay naming a claim absent from the document (`tools/harness/claims-freshness.py:2340-2343`), because `reports/round-48/claims.json` retains only C (`:27`) and Ca (`:41`) after the O candidate was dropped. Two consequences:

1. The declaration's exact command (`reports/round-48/telemetry/dispatch-declared.json:19`) is **not replayable from filed artifacts**. The `<candidates>` document it consumed is gone.
2. `--claims reports/round-48/claims.json` alone is also not a verdict: both claims declare no `before_checks`, so the gate returns **`could-not-evaluate`, exit 3**, with `REFUSE: claim(s) C, Ca could not be evaluated`. The filed claims file is a *record of the claim*, not a runnable gate input.

## 3. Reconstructed replay — verdicts reproduce deterministically

I rebuilt a 3-claim document from filed facts: C and Ca use the `before` strings verbatim from `reports/round-48/claims.json:30,44`; O's `before` is an explicit **label** because the original candidate prose is not filed. No probe reads the `before` text — `_load_check` explicitly accepts a non-verbatim clause as a label (`tools/harness/claims-freshness.py:2221-2238`), and every check here is target-driven.

```console
$ python3 -B tools/harness/claims-freshness.py \
    --claims .scratch/o04/claims-replay.json \
    --checks .scratch/r48-freshness-check.json
claims-freshness: round 48 baseline a01405d (a01405dd36367292255c2652ac0a601f4cd6a0af)
  [C] FRESH             2/2 clauses hold
  [Ca] FRESH            1/1 clauses hold
  [O] STALE             1/1 clauses contradict
      clause 0 (capability_present): measured=False expected=True -- resolver blank-hyphen edge
summary: 2 fresh, 1 stale, 0 could-not-evaluate, 0 malformed; clauses 4 (3 hold, 1 contradict, 0 not evaluated)
REFUSE: claim(s) O have a `before` already false at a01405d; do not dispatch.
exit 1
```

| Claim | Clause | Probe | Measured | Expected | Status |
|---|---|---|---|---|---|
| C | cartography unowned | `topic_owner_absent` | 0 owner(s) | true | HOLDS |
| C | culture-material 25 | `count_eq` | 25 files | 25 | HOLDS |
| Ca | README duplicate heading | `count_eq` | 1 file | 1 | HOLDS |
| O | resolver blank-hyphen edge | `capability_present` | false | true | CONTRADICTED |

Determinism: two independent processes produced `decision_sha256 = 4165d34d…` with no timestamp field. `--no-exec` flips O to `could-not-evaluate` (`exit 3`), confirming the O verdict depends on executing the candidate tool. Gate selftest: `SELFTEST OK: registry 43/43 + seam 19/19`, exit 0.

## 4. Soundness of each verdict

### 4.1 C — sound

- Positive control: a synthetic entry whose H1/topic names cartography makes `topic_owner_absent` return `mismatch` ("1 owner(s)"), so the probe detects ownership rather than greening absence.
- Independent ground truth at `a01405d`: `git grep -niE '^[- ]*topic:.*(cartograph|mapmak|portolan|cadastr)' a01405d -- corpus/knowledge/` → 0 lines; `git ls-tree -r --name-only a01405d -- corpus/knowledge | grep -iE 'cartograph|mapmak|portolan|cadastr'` → 0; the four remaining word hits are the cosmography disclaimers. Culture-material count → 25.
- Caveat, not a defect: the C ownership probe is **partition-scoped** (`"partition": "culture-material"` in the overlay). The filed claim's "verified-fresh unowned" is global. The probe does not establish the global leg; I did, independently, above.

### 4.2 Ca — vacuous (blocking anti-theater defect)

The check is `count_eq` with `target.glob = corpus/README.md`, `target.value = 1`, `expect = false`. Two transforms make it a tautology:

1. `_coerce_check` rewrites `count_eq` + `value` as `check["expect"] = target.pop("value")` (`tools/harness/claims-freshness.py:2193-2196`). The overlay's `"expect": false` is **silently discarded** and replaced by `1`. The loaded check is:
   ```json
   {"clause": "README duplicate heading", "probe_kind": "count_eq",
    "target": {"glob": "corpus/README.md"}, "expect": 1, "clause_match": "label"}
   ```
2. `_probe_count_eq` counts **files matching the glob**, never file content (`tools/harness/claims-freshness.py:1053-1064`).

Measured on fixtures: a README with **0**, **1**, or **2** H1 lines all measure `1` and all return `holds`. The `evidence_command` records `grep -c '^# kotodama-shokunin corpus index' … -> 2`, but the probe never runs grep. **`Ca FRESH` is guaranteed by the existence of `corpus/README.md`.** It would stay green if the duplicate heading were fixed or if fifty duplicates appeared.

Ground truth the gate did not measure: `grep -n '^# kotodama-shokunin corpus index' corpus/README.md` → `1:` and `3:`, count **2** at both `a01405d` and the worktree. So the premise is true; the verdict is right by accident, and the declaration's sentence "Ca FRESH (README duplicate-heading holds)" (`reports/round-48/claims.json:23`) is not gate-proven.

### 4.3 O — right answer, wrong mechanism

The probe is `capability_present` on `tools/harness/basename-couples-resolver.py` with `argv: ["--selftest"]` in a temporary tree containing only the one-file fixture (`tools/harness/claims-freshness.py:1129-1200`; subprocess at `:1172`). The resolver's selftest is **not self-contained**: S1a, S1f, S4a–S4c and S10 read live corpus bytes (`tools/harness/basename-couples-resolver.py:325,348,378,432`; "one read-only live read" at `:271`). In the gate's one-file tree those six controls cannot pass:

```console
$ (isolated one-file tree, exact gate fixture)
SELFTEST FAIL: 21/27 controls
  failed: S1a ..., S1f ..., S4a ..., S4b ..., S4c ..., S10 ...
exit 1
$ (real lane root, live corpus)
SELFTEST OK: 27/27 controls
exit 0
```

So `measured=False` reports **"the fixture tree is not the corpus"**, not "the resolver drops a hyphen soft-wrap". Confirmation that the mechanism is wrong: `--no-exec` turns the same clause into `could-not-evaluate`, not `stale`.

The factual disposition is nevertheless correct. Running the resolver directly on the exact fixture (positional path, no selftest):

```console
$ python3 -B tools/harness/basename-couples-resolver.py .scratch/o04/fixture.md --json
[{"path": ".scratch/o04/fixture.md", "tokens": {"x.md": {...}},
  "wrapped": false}]
```

`wrapped=false`, one token — matching `reports/round-48/claims.json:19` ("the resolver yields wrapped=False tokens=1, a different edge"). The premise "the resolver drops hyphen soft-wrap" is false, so dropping O was right; the gate's `O STALE` is not evidence for it. A sound probe would run the resolver on the fixture path and assert output structure (`wrapped`/`tokens`), which `capability_present` cannot do: it only regex-matches stdout (`success_regex`). The declared regex `drops|0 tokens|prosody` would not match the true output `wrapped=False tokens=1` either — independent of the isolation bug, this probe could not have confirmed the edge.

## 5. Independent ground-truth measurements

| Fact | Command | Result |
|---|---|---|
| Baseline == HEAD, no corpus drift | `git rev-parse HEAD`; `git diff --stat a01405d..HEAD` | `a01405dd…`; empty |
| README duplicate H1 | `grep -n '^# kotodama-shokunin corpus index' corpus/README.md` | `1:` and `3:`; count 2 |
| Cartography topic owners (global) | `git grep -niE '^[- ]*topic:.*(cartograph\|mapmak\|portolan\|cadastr)' a01405d -- corpus/knowledge/` | 0 |
| Cartography filenames | `git ls-tree -r --name-only a01405d -- corpus/knowledge \| grep -iE …` | 0 |
| Culture-material entries | `ls corpus/knowledge/culture-material/*.md \| wc -l` | 25 |
| Resolver at HEAD | `python3 -B tools/harness/basename-couples-resolver.py --selftest` | `27/27`, exit 0 |
| Resolver on fixture | positional run `--json` | `wrapped=false`, 1 token |
| Gate selftest | `python3 -B tools/harness/claims-freshness.py --selftest` | `43/43 + 19/19`, exit 0 |

## 6. Durable artifacts (drafted here; integrator applies)

I may write only my out path, so both inputs are embedded below. Each listed sha256 is over the **fenced bytes plus one trailing newline**, so it can be checked against the fence itself; the JSON parses to the same document that produced the replayed verdicts. The `.scratch` originals differ only in JSON whitespace and `\u2014` escape spelling (file shas in §1). Recommended landing paths, both under `reports/round-48/telemetry/` per `AGENTS.md:17-19`:

- `reports/round-48/telemetry/r48-freshness-overlay.json` — fence sha256 `099bc1a223b054bb6b6419f451f5de478403f227822b765e44d185df589ffcea`
- `reports/round-48/telemetry/r48-freshness-replay-claims.json` — fence sha256 `5b58520712e7ea6d8ba3c8291b257b7096813e7d48206add7ef3738b3716c43e` (label it a reconstruction, not the lost original)

Overlay bytes:

```json
{
 "schema": "kotodama-claims-freshness-checks-v1",
 "round": 48,
 "baseline_commit": "a01405d",
 "checks": {
  "C": [
   {
    "clause": "cartography unowned",
    "probe_kind": "topic_owner_absent",
    "target": {
     "topics": ["cartography", "mapmaking", "portolan", "cadastral"],
     "partition": "culture-material",
     "fields": ["H1", "topic", "gap filled"]
    },
    "expect": true,
    "evidence_command": "git grep -niE 'cartograph|mapmak|portolan|cadastr' a01405d -- corpus/knowledge/culture-material/"
   },
   {
    "clause": "culture-material 25",
    "probe_kind": "count_eq",
    "target": {"glob": "corpus/knowledge/culture-material/*.md", "value": 25},
    "expect": true,
    "evidence_command": "git ls-tree -r --name-only a01405d -- corpus/knowledge/culture-material | wc -l"
   }
  ],
  "O": [
   {
    "clause": "resolver blank-hyphen edge",
    "probe_kind": "capability_present",
    "target": {
     "globs": ["tools/harness/basename-couples-resolver.py"],
     "exclude_globs": [],
     "argv": ["--selftest"],
     "fixture": {"corpus/knowledge/linguistics/phonetics-phonology.md": "- couples: a — `x.md`; prospective sibling files: tone-\n\n  prosody.md\n"},
     "success_regex": "drops|0 tokens|prosody",
     "timeout_s": 30,
     "max_candidates": 4
    },
    "expect": true,
    "evidence_command": "resolver selftest on blank-separated hyphen fixture"
   }
  ],
  "Ca": [
   {
    "clause": "README duplicate heading",
    "probe_kind": "count_eq",
    "target": {"glob": "corpus/README.md", "value": 1},
    "expect": false,
    "evidence_command": "grep -c '^# kotodama-shokunin corpus index' corpus/README.md -> 2"
   }
  ]
 }
}
```

Replay claims bytes (C/Ca `before` are verbatim from the filed claims; O's is a label):

```json
{
 "round": 48,
 "baseline_commit": "a01405d",
 "replay_note": "Reconstructed by O04 from reports/round-48/claims.json plus .scratch/r48-freshness-check.json; O's before is a label, not the original candidate prose. No probe reads the before text.",
 "claims": [
  {"id": "C", "axis": "coverage", "before": "total 223; cartography verified-fresh unowned (gate-confirmed at declaration); r47's draft was over-built + defective and was correctly not landed"},
  {"id": "Ca", "axis": "calibration", "before": "README carries a duplicate H1 (lines 1 and 3, verified grep count 2); the r47 over-build defect (draft 790 lines + R03 B1-B9) is undispositioned; no heading-count control exists in the sweep"},
  {"id": "O", "axis": "operability", "before": "Reconstructed replay label only (original r48 candidates document is not filed): the resolver drops a hyphen soft-wrap. Fielded premise description: reports/round-48/claims.json:19 'the resolver yields wrapped=False tokens=1, a different edge'."}
 ]
}
```

## 7. Findings

| id | Severity | Finding | Owner | Next touch |
|---|---|---|---|---|
| O04-F1 | blocking for the evidence chain | Declaration inputs are not durable: overlay only in `.scratch`, candidates doc absent. Exact replay is impossible from filed bytes. | integrator | File the two artifacts in §6 under `reports/round-48/telemetry/`; record their shas in `validation.json`. |
| O04-F2 | blocking anti-theater | Ca's check is a tautology: `count_eq` counts files; `_coerce_check` discards `expect:false` in favour of `target.value:1` (`claims-freshness.py:2193-2196`, `:1053-1064`). It cannot observe a heading. | Ca01/Ca05 + gate owner | Replace with a content-sensitive probe (regex-count or heading-count control); re-run and file the new verdict. Do not cite `Ca FRESH` as heading evidence. |
| O04-F3 | non-blocking for dispatch, blocking for "first live use" | O's contradiction is produced by running `--selftest` in a corpus-less tree (21/27), not by the blank-hyphen edge (27/27 live; fixture `wrapped=false`). The stale disposition is factually right but not gate-established. | O01/O02/W01 | Probe by positional fixture run and assert `wrapped`/`tokens`; or declare the O premise directly as `wrapped=false, tokens=1` with a probe that can read it. |
| O04-F4 | process | `evidence_command` is documentation, not execution: the Ca row records a grep the gate never runs, so the printed evidence overstates what was measured. | gate owner | Add a check that the evidence command and probe kind agree, or drop the field from human rendering. |
| O04-F5 | non-blocking | Overlay has no `claims_sha256` pin (`claims-freshness.py:2330-2339`); the same overlay could be silently replayed against different claims. | integrator | Pin the overlay to the replay claims file when filing. |

Not a finding: C's two checks are sound (positive control detects a planted owner; independent global sweep confirms 0 owners), the gate selftest is fully green, and the decision digest is deterministic.

## 8. Not verified / to-verify

- **to-verify**: the original candidates `before` prose for O. It was not filed; my replay substitutes a labelled sentence. This does not change any measurement, because no probe reads `before`.
- **to-verify**: that the `.scratch` overlay bytes are byte-identical to the declaration's. The mtime is consistent (19:35:51Z vs 19:45:00Z declaration) and the recorded verdicts match, but there is no declaration-time digest of the overlay.
- **to-verify**: whether the Ca probe was intended as a file-count sanity check rather than a heading check. Its `evidence_command` and clause both say heading, so I treat it as a defect, not a deliberate scope limit.

## 9. Reproduction commands

```console
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
# 1 gate health
python3 -B tools/harness/claims-freshness.py --selftest
# 2 exact filed inputs (expected exit 2)
python3 -B tools/harness/claims-freshness.py --claims reports/round-48/claims.json \
  --checks .scratch/r48-freshness-check.json
# 3 reconstructed replay (expected exit 1, digest 4165d34d…)
python3 -B tools/harness/claims-freshness.py --claims .scratch/o04/claims-replay.json \
  --checks .scratch/r48-freshness-check.json
# 4 ground truths
grep -n '^# kotodama-shokunin corpus index' corpus/README.md
python3 -B tools/harness/basename-couples-resolver.py --selftest
python3 -B tools/harness/basename-couples-resolver.py .scratch/o04/fixture.md --json
```

## 10. Write surface

This file only. I created `.scratch/o04/{claims-replay.json,replay.json,fixture.md,cap/}` as disposable replay state; no `corpus/`, `tools/`, or filed-report byte was modified. `git status --porcelain` shows only untracked `reports/round-46/review/` and `reports/round-48/`.
