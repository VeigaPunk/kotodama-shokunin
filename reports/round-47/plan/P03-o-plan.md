# P03 — O-claim plan: durable `tools/harness/claims-freshness.py`

- Seat: `P03` | role planner | claim `O` (operability) | round 47, loop 2
- Out path: `reports/round-47/plan/P03-o-plan.md` (this seat's only write)
- Declared baseline: `6e9a30d` (`reports/round-47/claims.json:7`; resolves to `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`)
- Evidence cut: 2026-10-19T17:57Z (UTC), lane HEAD `6e9a30d`
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root
- Status of the deliverable: **not built**. This is the architecture and the acceptance control set; `tools/harness/claims-freshness.py` does not exist at `6e9a30d` (verified: `git cat-file -e 6e9a30d:tools/harness/claims-freshness.py` → absent). Every verdict below comes from a scratch probe or the r44 scratch prototype, and is labelled as such.

This plan is written to be consumed by O01–O04 (tool authors), O05–O07 (demonstrators), O08–O11/O13–O15 (verifiers), O12 (scribe), W01 (landing spec) and the integrator. It fixes the semantics, the schema, the build seams, the regression matrix and the selftest control set; it does not write the tool.

---

## 0. The defect this claim must close, re-measured

R01-43-12 (`reports/round-43/review/R01-review.md:400`): r43 dispatched two claims whose `before` was already false at `7ceff59`. The numbers, re-derived by this seat read-only:

| fact at `7ceff59` | measured | command |
|---|---|---|
| corpus entries | 223 | `git ls-tree -r --name-only 7ceff59 -- corpus/knowledge \| grep -c '\.md$'` |
| myth-symbol entries | 26 | same, `-- corpus/knowledge/myth-symbol` |
| couples witness exists | yes, sha256 `d8d23a26…` | `git show 7ceff59:tools/harness/couples-reference-extractor.py \| sha256sum` |
| witness declares the policy | yes, line 8 | `… \| grep -n 'basename-couples'` → `8:Policy implemented: reports/round-39/calib/basename-couples-policy.md` |
| witness has block extraction | yes, line 50 | `… \| grep -n 'def couples_block'` → `50:def couples_block(text):` |
| lithic owner | `mineral-stone-symbolism.md`, sha `c99f44ca…` | `git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md \| sha256sum` |
| lithic ownership rows | H1 line 1 + `- topic:` line 5 | `… \| sed -n '1p;5p'` |
| r43 Ca disposition artifact | absent | `git cat-file -e 7ceff59:reports/round-43/calib/dispositions-r38-r39.json` → fatal |

So the exact claim clauses are false as follows (`reports/round-43/claims.json:27,40,53`):

- **O** — "no durable instrument implements the r39 basename-couples policy" **false**; "the only resolver … lives in ephemeral .scratch" **false**. The witness is durable and green (`d8d23a26…`). 0/2.
- **C** — "myth-symbol 26" **true**, "total 223" **true**, "lithic slot named but unbuilt" **false** (owner exists). 2/3.
- **Ca** — "have no per-finding disposition on record" **true at `7ceff59`**: the named artifact is absent. 1/1.

The r44 declarations are the negative control (`reports/round-44/claims.json:7,27,40,52`): at `c9f4eaa` the four-class authority is absent (`git grep -l 'four_class' c9f4eaa -- tools/` → no output), the witness is the only `.py` in the couples family, the total is 223, and the lithic/r43 facts hold. A correct gate does not flag r44.

**Why naive gates fail.** X01 implemented path and count gates and measured **0 of 2** r43 stale claims caught (`reports/round-44/cross/X01-trades.md:247-320`): r43 O's named target `basename-couples-resolver.py` was absent at baseline, and r43 C's numeric literals were correct. The only catching predicates were capability-level (the policy name in the witness) and ownership-level (`lithic` in the owner's topic line). The durable tool must therefore have a **capability leg** and a **topic-ownership leg**, with each clause declaring its own polarity.

---

## 1. Design law: measurement is not assertion

The central failure mode is polarity. This seat's own first probe encoded `capability_present` for r43 O's "no durable instrument" clause and returned **FRESH** — the measurement (capability present) was correct, the *claim* asserted its absence, and the probe had no declared polarity. The r44 R01 review recorded the same bug independently: "my first probe run marked O's first premise 'fresh' because I encoded `asserted=True` for 'resolver exists' when the claim asserts absence" (`reports/round-44/review/R01-review.md:240`).

The schema therefore separates:

1. **Measurement** — what the baseline reader observes: a path's presence, a glob count, grep hits, a blob digest, topic-owner hits, capability-marker hits.
2. **Assertion (`polarity` + value)** — what the clause claims about that measurement: `absent` / `present` / `eq` / `ne`, with `value` for equality kinds.

A check is **malformed** (exit 2) if the polarity is missing or contradicts the kind. The seven kind names in the r47 contract are retained as *presets* that expand to (measurement, polarity); their complements are added because r43 O is an absence-of-capability claim and cannot be expressed by `capability_present` without inverting the result in code — the exact theater the contract is meant to prevent.

Preset expansion:

| preset `kind` | measurement | declared `polarity` | args | `value` |
|---|---|---|---|---|
| `path_absent` | path | `absent` | `path` | — |
| `path_present` | path | `present` | `path` | — |
| `grep_absent` | grep | `absent` | `glob`, `regex`, optional `max_lines` | — |
| `grep_present` | grep | `present` | `glob`, `regex`, optional `max_lines` | — |
| `count_eq` | glob count | `eq` | `glob` | integer |
| `sha256_eq` | blob digest | `eq` | `path` | 64-hex |
| `topic_owner_absent` | topic owner | `absent` | `terms[]`, optional `scope` | — |
| `topic_owner_present` | topic owner | `present` | `terms[]`, optional `scope` | — |
| `capability_present` | capability | `present` | `markers[]`, `mode` | — |
| `capability_absent` | capability | `absent` | `markers[]`, `mode` | — |
| `glob_present` / `glob_absent` | glob | `present` / `absent` | `glob` | — |

The complements `grep_present`, `topic_owner_present`, `capability_absent`, `glob_absent` are additions to the r47 named set; the r47 set is a subset, not a ceiling. Document this in the tool docstring and the O12 receipt.

**The exact bug, reproduced.** Scratch probe v1 (`.scratch/p03/probe.py`, this seat) returned `FRESH` for r43 O because the check measured `capability_present` and the verdict compared it directly. Probe v2 (`.scratch/p03/probe2.py`) added `polarity` and returned `STALE` for the same measurement. The delta is the whole design.

---

## 2. CLI and input contract

```
python3 tools/harness/claims-freshness.py --selftest
python3 tools/harness/claims-freshness.py --regress [--root .]
python3 tools/harness/claims-freshness.py --claims <claims.json> [--checks <sidecar.json>]
        [--root .] [--at <commit-ish>] [--json] [--require-complete] [--allow-empty-glob]
```

- `--selftest` — hermetic controls (§8 A–E, G). No lane history required. Exit 0 only at N/N.
- `--regress` — live controls (§8 F): r43, r44, mutations, r47 self-check. Requires commits `7ceff59` and `c9f4eaa`. Exit 0 only if every expected verdict/exit matches.
- `--claims` — evaluate a claims file. The declared baseline is `claims.json.baseline_commit`; `--at` is an explicit reproduction override and is recorded as a deviation.
- `--checks` — a sidecar of declared checks for historical claims. Never edits the claims file. A sidecar's `baseline_commit`/`round`, if present, must equal the claims file's or exit 2.
- `--require-complete` — any ungrounded clause downgrades the claim from FRESH to could-not-evaluate (exit 3). New rounds should use this; legacy r43/r44 runs do not.
- `--allow-empty-glob` — permit a `grep_absent`/`glob_absent` check on a glob that matches zero files (default: could-not-evaluate, never vacuous pass).

### 2.1 `claims.json` (read-only)

Required: `round` (int), `baseline_commit` (non-empty string), `claims` (non-empty list).
Per claim: `id`, `axis`, `before` (non-empty string). `after_required`, `counting_commands` are optional for the gate; `before_checks` is optional and authoritative when present.

```json
{
  "id": "O",
  "axis": "operability",
  "before": "no durable instrument implements the r39 basename-couples policy; …",
  "before_checks": [
    {
      "clause": "no durable instrument implements the r39 basename-couples policy",
      "kind": "capability_absent",
      "polarity": "absent",
      "args": {
        "markers": [
          {"glob": "tools/**/*.py", "field": "path", "regex": "couples"},
          {"glob": "tools/**/*.py", "field": "content", "max_lines": 40,
           "regex": "basename-couples"}
        ],
        "mode": "all",
        "exclude": ["tools/gates/frozen/**", "**/__pycache__/**"]
      }
    }
  ]
}
```

Rules:

1. `clause` must be a whitespace-normalized substring of the claim's `before`. A check that does not quote the claim is malformed (exit 2) — this stops a sidecar from asserting unrelated premises.
2. `kind` must be in the closed registry; `polarity` must be present and equal the preset's polarity.
3. Unknown args, unknown marker fields, a regex that does not compile, a `value` of the wrong type, or an empty `markers` list → exit 2.
4. An empty `before_checks: []` on a claim is **could-not-evaluate** (exit 3), never fresh.
5. Precedence: declared `before_checks` > `--checks` sidecar > legacy miner (§5). The report labels each check `declared` or `mined`.

### 2.2 Sidecar shape

```json
{
  "round": 43,
  "baseline_commit": "7ceff59",
  "claims": {
    "O": {"checks": [ … ]},
    "C": {"checks": [ … ]},
    "Ca": {"checks": [ … ]}
  }
}
```

The sidecar may omit claims; omitted claims fall back to mining. It may not name a claim id absent from the claims file (exit 2).

---

## 3. Baseline reader — git tree only

The `before` describes the declared commit, not the worktree. The reader is the only component allowed to touch git; every probe consumes it.

```
resolve_baseline(root, declared, at=None):
    sha = git -C root rev-parse --verify --quiet "<at or declared>^{commit}"
    if sha fails: Malformed("baseline-unresolvable", declared)
    if at and at != declared: record deviation (declared, at, sha)
    files = git -C root ls-tree -r -z --name-only <sha>
    return Baseline(root, sha, files)

Baseline.read(path):
    git -C root show <sha>:<path>            # bytes, cached
Baseline.sha256(path):
    sha256(git -C root show <sha>:<path>)    # cached
```

Implementation constraints:

- **Never `open()` a probe path under a commit.** Only `git show`. The selftest proves this with a worktree-only file (§8 A2).
- **Resolve to a 40-hex commit sha.** A tag or branch is accepted only if `^{commit}` resolves; the report prints both `baseline_declared` and `baseline_resolved`. A tree sha, blob sha or unknown ref → exit 2.
- **`Baseline` itself accepts any tree object id**, because `git show <tree>:<path>` and `git ls-tree <tree>` work identically. This is a test seam only: `resolve_baseline` (the production entry point) always requires `^{commit}`, so the hermetic selftest can build a synthetic `git write-tree` object without creating a commit or a ref (§8.1). No production path accepts a bare tree.
- **Record `worktree_head` and `worktree_dirty` as provenance, never as input.** The verdict is independent of them. `--at worktree` is not supported; `--at` must resolve through `^{commit}`.
- **Glob semantics:** `*` does not cross `/`; `**` does. Implement with a translated regex (`re.escape` then expand `**` before `*`), not `fnmatch` (whose `*` crosses `/` and would miscount nested paths). The corpus is flat today, so this is a correctness guard, not a count change.
- **NUL-separated `ls-tree -z`** to survive odd names; decode UTF-8 with replacement.
- **Performance:** cache every blob read; a full-corpus ownership scan reads 223 blobs. Target < 10 s cold, < 2 s warm; no network, no temp files.
- **Read-only:** no writes to the repo, no `.pyc` (`sys.dont_write_bytecode = True`), no locks. `--selftest` writes only inside `tempfile.mkdtemp(dir=TMPDIR)` and removes it.

---

## 4. Probe registry

Every probe returns a `Measurement` with `observed`, `evidence[]` (path:line or digest), and `reproduce` (an equivalent read-only git command). The verdict layer compares `observed` to the declared polarity/value.

| measurement | fields | observed | passes when | could-not-evaluate when |
|---|---|---|---|---|
| `path` | `path` | `present` / `absent` | observed == polarity | path empty/malformed |
| `glob` | `glob` | count | count == value (`count_eq`); non-empty for `present` | glob malformed |
| `grep` | `glob`, `regex`, `max_lines` (default 0 = all) | list of `path:line` hits | hits non-empty for `present`, empty for `absent` | glob matches 0 files (unless `--allow-empty-glob`); regex invalid → exit 2 |
| `sha256` | `path`, `value` | 64-hex digest or `missing` | digest == value | path absent at baseline |
| `topic_owner` | `terms[]`, `scope` (default `corpus/knowledge/*/*.md`) | hit rows `(path, line, field, term)` | 0 rows for `absent`, ≥1 for `present` | terms empty; every term generic (see 4.1) |
| `capability` | `markers[]`, `mode` (`all`/`any`), `exclude[]` | per-marker first hit or `None` | all/any markers hit for `present`; none for `absent` | zero markers → exit 2; all markers excluded → could-not-evaluate |

### 4.1 Topic ownership — field policy

Owner fields are **H1 (line 1 beginning `# `) and `- topic:` lines only**. `- gap filled:` is excluded. Evidence:

- `mineral-stone-symbolism.md` at `7ceff59` owns `lithic` on H1 (line 1) and `- topic:` (line 5); its `- gap filled:` (line 3) also names it. Excluding gap-filled still yields 2 owner rows, so the r43 C verdict is unchanged and the evidence is cleaner.
- A cartography sweep at `6e9a30d` over H1 + topic lines with `cartograph|mapmaking|map-making` returns **0** hits; adding the generic term `survey` returns hits in `number-symbolism.md:3` (a variance survey, not mapmaking) and two `- gap filled:` mentions in linguistics entries. The gate must not expand synonyms; the claim author supplies discriminating terms. This seat verified 0 hits for the precise term set (§11 A5).
- The r44 dream/divination adjacency (`reports/round-44/review/R01-review.md:167-169`) is a deliberate over-fire: a `dream` term would hit `divination-omen-systems.md`'s H1/topic line. The gate reports the hits; an explicit integrator ruling, not a term allowlist, decides adjacency. The safe direction for a pre-dispatch gate is to flag and require the ruling.

Matching is case-insensitive, whole-token (`\b`), no stemming. The report lists up to 20 rows with the total count; the full row set goes to `--json`.

### 4.2 Capability — marker policy

A capability is a set of markers, each `{glob, field, regex, max_lines?}`:

- `field: "path"` — match against the repo-relative filename (stem included).
- `field: "content"` — match against the first `max_lines` lines of the blob (default 40).
- `mode: "all"` (default) requires every marker; `mode: "any"` requires one.
- Default `exclude`: `tools/gates/frozen/**`, `**/__pycache__/**`, `**/*.pyc`. Frozen gates are historical snapshots and must not satisfy a live capability.

This closes two measured prototype defects:

- The prototype counted `tools/gates/provenance-audit.py:12` as a couples-family candidate because its body mentions a missing `- couples:` header (`R01-review.md:241`; prototype output in §11 A3). A filename-field marker for `couples` rejects it; a content marker for `basename-couples` also rejects it.
- The prototype's `tool_family_absent` returned **pass** when the derived stem list was empty (all tokens were stopwords). The durable registry treats an empty marker set as malformed (exit 2) and an empty family as could-not-evaluate, never pass.

The capability probe is a **proxy**, not a behavioral test: it proves a signature exists at baseline, not that the tool runs. The report labels it `proxy: true`; behavioral gaps stay `to-verify`.

**Qualifier rule.** A declared capability check must carry at least two markers, one of which is a qualifier marker (a hyphenated capability name, a function signature, or a policy reference) rather than the bare family token; a mined check derives that qualifier from the pre-noun phrase. This is what distinguishes r44 O's "no **four-class** census authority" (true: the witness lacks `four_class`) from r43 O's "no durable instrument … **basename-couples** policy" (false: the witness declares it). A probe on the family token alone would false-flag r44 O against the witness, so a single family-only marker is treated as could-not-evaluate, not as evidence.

### 4.3 No vacuous truth

`grep_absent` over an empty glob is a **could-not-evaluate**, not a pass. This is the root cause of the prototype's failing selftest control "grep_absent hit fails": its fixture `corpus/knowledge/beta/*.md` did not exist, so no hit was possible (`R02-review.md:216-227`; prototype `run_selftest` line 797). The same bug in production would let a renamed corpus directory turn the gate green. `--allow-empty-glob` is the only escape, and it is reported.

The same rule applies to `glob_absent` and to a topic scan over a scope with zero files.

---

## 5. Legacy miner (historical claims only; advisory)

The r43/r44 files have no `before_checks`. The claim's counting command runs the gate on `reports/round-43/claims.json` without a sidecar, so mining is required for the demonstration. It is explicitly **advisory**: every mined check is labelled `mined:<extractor>` and carries the quoted clause; declared checks are authoritative for future rounds.

### 5.1 Extractors

| id | clause pattern | synthesized check | catches |
|---|---|---|---|
| E1a | `no <phrase> (instrument\|tool\|authority\|check\|resolver\|mechanism\|gate)` | `capability_absent`; family tokens from the **clause**, qualifiers from the hyphenated pre-noun phrase | r43 O clause 1 |
| E1b | `the only <noun> … lives in …/.scratch` | `capability_absent` on the durable copy | r43 O clause 2 |
| E1c | `have no … on record` + a `reports/...` path in `after_required` | `path_absent` on the first named artifact | r43 Ca |
| E2a | `total N` | `count_eq` over `corpus/knowledge/*/*.md` | r43 C, r44 C |
| E2b | `<partition> N` | `count_eq` over that partition | r43 C |
| E3a | `<topic> (slot\|register slot) (is\|was)? (unbuilt\|unowned\|empty\|unfilled)` **adjacent** | `topic_owner_absent` on the captured topic | r43 C |
| E3b | `<topic> … already owned` / `<topic> slot … was owned` | `topic_owner_present` | r44 C historical premise |
| E4a | `the only <tool\|extractor\|resolver\|instrument>` | `count_eq 1` over the family `tools/**/*<family>*.py` | r44 O |
| E5a | a `tools/…py` path in the clause | `path_present` | named-tool existence premises |
| E5b | a bare `<name>.py:NN` citation | `path_present` for `tools/**/<name>` | citations |
| E6 | anything else | ungrounded warning | — |

### 5.2 Hardening rules (each closes a measured false positive/negative)

1. **Family from `before` first.** r43 O's family ("basename-couples" → `couples`) must come from the premise clause, not from `after_required`. This makes anti-theater mutation M1 (rename the named target to the witness) still flag: the premise still says basename-couples, the witness satisfies it.
2. **Topic capture prefers the hyphenated compound and rejects pronouns/generic heads.** The prototype parsed r44 C's "its topic was already owned … verified-unowned gap" as topic `its` and produced **64 owner hits** (§11 A4), a false STALE on a true `before`. The durable pattern requires adjacency (`<topic> (register )?slot is/was unbuilt|unowned|…`) and rejects `its|this|that|the|a|an|topic|slot|register|entry|gap|field|domain`. A rejected topic → could-not-evaluate, never STALE.
3. **Empty stems → could-not-evaluate.** The prototype's `tool_family_absent` passed vacuously when all family tokens were stopwords.
4. **Empty glob → could-not-evaluate** for absence probes (§4.3).
5. **Probe errors are malformed (exit 2), not STALE.** The prototype catches `KeyError/ValueError` and sets `passed=False`, turning an input bug into a stale verdict and the wrong exit code.
6. **Ungrounded clauses are warnings, not assertions.** A claim is FRESH only if at least one check is grounded and every grounded check passes; ungrounded clauses are printed and counted. `--require-complete` turns any ungrounded clause into could-not-evaluate. The r43 O run legitimately leaves clauses 3–4 ungrounded (2 grounds) and the r43 Ca run leaves the narrative ungrounded (1 ground); both still reach the required verdicts. A claim whose `before` yields **zero** grounds is could-not-evaluate (exit 3).

**Residual limit, stated honestly.** Mining is a typed-adapter over prose, not a parser of the author's intent. A clause that is grammatically a prescription ("the correct move is a fresh, unowned gap") must not be mined as a premise; the adjacency rule and the pronoun stoplist are the guard. Every mined verdict is advisory and the receipt must print the ungrounded clauses so the integrator sees what was not measured.

---

## 6. Verdict algebra and exit contract

### 6.1 Per claim

```
checks = declared (if before_checks present) else sidecar (if --checks) else mined
grounded = checks with a valid measurement
failed   = grounded checks whose observed != expected
ungrounded = clauses with no check

if any check malformed / baseline unresolvable / schema error:
    claim = MALFORMED            (whole run exits 2)
elif failed:
    claim = STALE
elif grounded and ungrounded and --require-complete:
    claim = COULD-NOT-EVALUATE
elif grounded:
    claim = FRESH                (with warnings for ungrounded)
else:
    claim = COULD-NOT-EVALUATE
```

A claim is FRESH only if **all** declared/grounded clauses match. Any mismatch is STALE — the existential rule R01 asked for.

### 6.2 Exit codes

| code | state | precedence | stdout tail |
|---|---|---|---|
| `0` | every claim FRESH (≥1 grounded check each) | last | `FRESH: N/N claims` |
| `1` | at least one STALE | 2nd | `REFUSE: claims <ids> have a before already false at <sha>` |
| `2` | malformed input / baseline unresolvable / usage | 1st | `MALFORMED: <detail>` |
| `3` | no STALE, at least one COULD-NOT-EVALUATE | 3rd | `REFUSE (unverifiable): claims <ids> declare no groundable check` |

Precedence is `2 > 1 > 3 > 0`: a malformed run cannot be trusted even if another claim is stale; a stale claim is the stronger refusal than an unverifiable one. `could-not-evaluate != green` is satisfied by exit 3; `exits non-zero on stale` by exit 1.

This renumbers the scratch prototype (which used `1` usage, `2` stale, `3` unverifiable). The durable contract is R01 §4.3's `0/1/2` plus the explicit `3` that r47's O threshold requires. Record the renumbering in the tool docstring and the receipt so no verifier tests the prototype's numbering by mistake.

### 6.3 Report

Human output, per claim:

```
[O] operability -- STALE (0/2 checks hold; 2 ungrounded)
  x capability_absent  "no durable instrument implements the r39 basename-couples policy"
      measured: capability=present
      evidence: tools/harness/couples-reference-extractor.py:8: Policy implemented: …basename-couples-policy.md
      reproduce: git show 7ceff59:tools/harness/couples-reference-extractor.py | grep -n basename-couples
  ~ ungrounded: "the single wrapped couples field reads 0/4 tokens"
baseline: declared 7ceff59  resolved 7ceff59a0216a8ea21ee43262d9fc72abf770cee  source git-tree
worktree: 6e9a30d (dirty: reports/round-47/ untracked)   [provenance only]
```

`--json` emits the same rows plus `observed`, `expected`, `evidence[]`, `reproduce`, `grounded`, `ungrounded[]`, `extractor`, `declared|mined`, `baseline_declared`, `baseline_resolved`, `worktree_head`, `generated_at`, `summary{...}`, `exit`. The verdict and exit are pure functions of the inputs; `generated_at` is the only non-deterministic field. The determinism control compares `summary` + `exit` only.

---

## 7. Required regression matrix

All commands from the lane root, `PYTHONDONTWRITEBYTECODE=1`. The expected values below are this seat's measurements; the tool must reproduce them.

| id | command / input | expected | why |
|---|---|---|---|
| R1 | `--claims reports/round-43/claims.json` (mined) | exit **1**; O STALE 0/2; C STALE 2/3; Ca FRESH 1/1; 2 ungrounded | the positive regression |
| R2 | same + `--checks reports/round-47/calib/freshness-demo-r43.json` | exit **1**; O STALE (2 checks, both fail); C STALE (ownership); Ca FRESH | declared-check path; the demo |
| R3 | `--claims reports/round-44/claims.json` (mined) | exit **0**; O FRESH; C FRESH; Ca FRESH | negative control; the prototype false-flags C (§11 A4) — the durable tool must not |
| R4 | `--claims reports/round-47/claims.json --at 6e9a30d` | exit **0**; C FRESH (223 + cartography unowned); O FRESH (no durable gate); Ca FRESH | the round's own premises at declaration |
| R5 | M1: r43 O copy, `after_required` target renamed to `couples-reference-extractor.py`, `before` unchanged | exit **1**; O STALE | anti-theater: flag from capability, not the named path |
| R6 | M2: r43 C copy with `26` and `223` deleted from `before` | exit **1**; C STALE | anti-theater: flag from ownership, not arithmetic |
| R7 | M3: r44 C copy with the "already owned" narrative removed, keeping `total 223` | exit **0**; FRESH | anti-false-positive: a prescription is not a premise |
| R8 | M4: a one-claim file `"the llama-herding register slot is unbuilt"` at `c9f4eaa` | exit **0**; FRESH; parsed topic `llama-herding`, 0 owners | the R02 novel-phrasing trap (`R02-review.md:207-227`) |
| R9 | determinism: run R1 twice | identical `summary` + `exit` | no ordering/random dependence |
| R10 | read-only: run R1 from a clean tree | no new files under the repo; `git status` unchanged except `reports/round-47/` | no writes |

**M1 implementation note.** The mutation edits only `after_required` (the named target), not `before`. If the miner derives the family from `after_required`, the tokens become stopwords and the check is vacuously absent — the prototype's failure mode. The rule "family from `before` first" (§5.2.1) is what makes M1 meaningful.

**R3 implementation note.** The prototype currently returns C STALE with `topic "its"` and 64 owners. The durable tool must parse r44 C's groundable premise as `total 223` (+ the historical ownership fact in `-` clause 2, which is true at `c9f4eaa`), and leave the prescription ungrounded. Any STALE on r44 is a false-positive failure of the deliverable.

---

## 8. Selftest control set

### 8.1 Hermetic fixture

No commits, no refs, no network:

```
tmp = mkdtemp(dir=TMPDIR); git -C tmp init -q
write corpus/knowledge/alpha/one.md, corpus/knowledge/beta/two.md (lithic owner),
      corpus/knowledge/beta/three.md, tools/harness/example-couples-resolver.py,
      tools/gates/frozen/example-couples-resolver.py (a frozen decoy),
      reports/demo/artifact.json
git -C tmp add -A; tree = git -C tmp write-tree      # tree object, no commit
Baseline(tmp, tree)                                  # test seam, bypasses resolve_baseline
```

The fixture deliberately constructs `Baseline` directly from the tree object: production `resolve_baseline` requires `^{commit}` (§3), and no commit is created anywhere. A file written after `write-tree` but not added is the worktree-only control (A2). The frozen decoy shares the capability markers and must be excluded (C5). Cleanup with `shutil.rmtree`. If `git` is unavailable, `--selftest` fails with a named error; it never skips to green.

### 8.2 Controls

The count is derived from the control registry (`len(CONTROLS)`), never hardcoded — the prototype's stale `seventeen checks collected (18)` is the defect this rule closes.

**A. Baseline (8)**

| id | control | expected |
|---|---|---|
| A1 | `path_present` on a tracked fixture | pass |
| A2 | `path_present` on a worktree-only file | fail (baseline ≠ worktree) |
| A3 | `ls-tree` count of the fixture corpus | 3 |
| A4 | `**` matches a nested fixture | pass |
| A5 | `*` does not cross `/` | pass |
| A6 | `sha256_eq` on a fixture blob | pass |
| A7 | a short tree-object id resolves to the full 40-hex id and `Baseline` reads it | pass |
| A8 | `resolve_baseline` on a tree id or unknown ref | exit 2 (not a commit) |

**B. Probes (18)**

| id | control | expected |
|---|---|---|
| B1 | `path_absent` missing | pass |
| B2 | `path_absent` present | fail |
| B3 | `path_present` present | pass |
| B4 | `count_eq` match | pass |
| B5 | `count_eq` mismatch | fail |
| B6 | `grep_absent` with a hit | fail |
| B7 | `grep_absent` without a hit (non-empty glob) | pass |
| B8 | `grep_absent` over an empty glob | **CNE** (not pass) |
| B9 | `grep_present` with a hit | pass |
| B10 | `grep_present` without a hit | fail |
| B11 | `sha256_eq` match | pass |
| B12 | `sha256_eq` mismatch | fail |
| B13 | `sha256_eq` missing path | **CNE** |
| B14 | `topic_owner_absent` with an H1 owner | fail |
| B15 | `topic_owner_absent` with a `- topic:` owner | fail |
| B16 | `topic_owner_absent` with no owner | pass |
| B17 | whole-token: `lith` does not match `lithic` | pass |
| B18 | `- gap filled:` mention is not an owner | pass |

**C. Capability (6)**

| id | control | expected |
|---|---|---|
| C1 | all markers present | `capability_present` pass |
| C2 | same measurement under `capability_absent` | fail (polarity works) |
| C3 | `mode: any` with one of two markers | pass |
| C4 | qualifier-absent candidate (the r44 O shape) | pass (no false flag) |
| C5 | frozen decoy excluded | pass |
| C6 | zero markers | exit 2 |

**D. Schema (9)**

| id | control | expected |
|---|---|---|
| D1 | missing `polarity` | exit 2 |
| D2 | polarity contradicts kind | exit 2 |
| D3 | unknown kind | exit 2 |
| D4 | claim missing `before` | exit 2 |
| D5 | claims file missing `baseline_commit` | exit 2 |
| D6 | non-JSON | exit 2 |
| D7 | `claims` not a list | exit 2 |
| D8 | sidecar clause not a substring of `before` | exit 2 |
| D9 | `before_checks: []` | exit 3 |

**E. Verdict/exit (8)**

| id | control | expected |
|---|---|---|
| E1 | all grounded checks pass | FRESH, exit 0 |
| E2 | one check fails | STALE, exit 1 |
| E3 | fail among passes | STALE, failing clause named |
| E4 | grounded pass + ungrounded clause (no `--require-complete`) | FRESH + warning |
| E5 | same with `--require-complete` | CNE, exit 3 |
| E6 | malformed check + a stale claim | exit 2 (malformed wins) |
| E7 | stale + CNE | exit 1 (stale wins) |
| E8 | two identical runs | same summary + exit |

**F. Live regression (9)** — R1, R3, R4, R5, R6, R7, R8, R9, R10 from §7.

**G. Hygiene (4)**

| id | control | expected |
|---|---|---|
| G1 | no files created under the repo by a run | pass |
| G2 | no `__pycache__` / `.pyc` written | pass |
| G3 | source anti-theater grep: the tool body contains none of `7ceff59`, `c9f4eaa`, `lithic`, `basename-couples` | pass |
| G4 | cold run on 223 entries | < 10 s |

Hermetic total: A8 + B18 + C6 + D9 + E8 + G4 = **53**. Live: **9**. The tool prints `selftest 53/53 PASS` and `regress 9/9 PASS`; both are asserted from the registry.

G3 is the structural anti-theater guarantee: the durable tool contains **no claim-specific data**. The r43/r44 literals live only in the demo sidecars and the claims files. If G3 fails, the tool is a lookup table.

---

## 9. Build, assembly and landing plan

### 9.1 Seams (function names fixed; parts compose without edits)

| part | owner | contents |
|---|---|---|
| 1 | O01 | shebang, docstring (contract + exit codes), imports, `VERSION`, `Baseline`, `resolve_baseline`, `load_claims`, `Malformed` exception |
| 2 | O02 | `PROBE_KINDS`, `validate_check`, `measure` (path/glob/grep/sha256/topic/capability), `topic_owners`, `capability_hits`, `mine_checks` (E1a–E6), `normalize_clause` |
| 3 | O03 | `CheckResult`, `analyze_claim`, `claim_verdict`, `build_report`, `render`, `main`, exit-code mapping, sidecar loading/validation |
| 4 | O04 | `build_fixture`, `CONTROLS`, `run_selftest`, `run_regress`, `REGRESS_CASES`, `__main__` guard |

Seam signatures (all plain Python 3.8+, stdlib only, `from __future__ import annotations` optional):

```python
class Malformed(Exception): ...
def resolve_baseline(root: str, declared: str, at=None) -> tuple[Baseline, dict]
def load_claims(path: str) -> dict
def normalize_clause(text: str) -> str
def validate_check(check: dict) -> dict
def measure(check: dict, baseline: Baseline) -> dict
def topic_owners(baseline: Baseline, terms, scope, exclude) -> list[dict]
def capability_hits(baseline: Baseline, markers, mode, exclude) -> dict
def mine_checks(claim: dict) -> tuple[list[dict], list[str]]
def analyze_claim(claim: dict, baseline: Baseline, sidecar: dict|None,
                  require_complete: bool, allow_empty_glob: bool) -> dict
def build_report(claims_path, root, checks_path, at, require_complete,
                 allow_empty_glob) -> dict
def render(report: dict) -> str
def run_selftest() -> int
def run_regress(root: str) -> int
def main(argv=None) -> int
```

### 9.2 Demo artifacts (fenced in seats; integrator extracts)

- `reports/round-47/calib/freshness-demo-r43.json` — sidecar with the exact checks for O/C/Ca (§9.3). Owner: O05.
- `reports/round-47/calib/freshness-negative-r44.json` — the one-claim r44 O control (optional; the whole-file R3 run needs no sidecar). Owner: O06.
- `reports/round-47/calib/freshness-mutations/m1-rename.json`, `m2-no-numerics.json`, `m3-no-narrative.json`, `m4-llama.json`. Owner: O07.
- `reports/round-47/calib/freshness-receipt.md` — commands, captured stdout, exit codes, `baseline_resolved`, tool sha256, the ungrounded clauses, and the mutation before/after. Owner: O12/W01, assembled by the integrator.

### 9.3 The r43 sidecar (exact clauses)

O:
1. clause `no durable instrument implements the r39 basename-couples policy` → `capability_absent`; markers: filename `couples` + first 40 lines `basename-couples`; mode all; exclude frozen.
2. clause `the only resolver that ever ran (r39 I-C05) lives in ephemeral .scratch` → same capability check.
   Clauses 3 (`the verbatim policy landing lacks block extraction + a disposition leg`) and 4 (`the single wrapped couples field reads 0/4 tokens`) stay ungrounded: the capability proxy shows block extraction exists, but the policy-text claim and the 0/4 token count are not expressible in the probe vocabulary. Record them as ungrounded warnings; the two failing checks already establish STALE.

C:
1. clause `myth-symbol 26` → `count_eq` 26, `corpus/knowledge/myth-symbol/*.md`.
2. clause `total 223` → `count_eq` 223, `corpus/knowledge/*/*.md`.
3. clause `lithic slot named but unbuilt` → `topic_owner_absent`, terms `["lithic"]`, default scope.

Ca:
1. clause `have no per-finding disposition on record` → `path_absent`, `reports/round-43/calib/dispositions-r38-r39.json`. The `(or .md)` alternative does not exist at baseline either; note it in evidence.

Expected declared run: O 0/2, C 2/3, Ca 1/1 → exit 1.

### 9.4 Integration sequence

1. O01–O04 file their fenced parts. O12 concatenates in the order 1→4, appends exactly one LF, and records the sha256 of the assembled bytes.
2. The integrator extracts the block to `.scratch/round-47/claims-freshness.py`, runs `python3 -m py_compile`, `--selftest` (53/53), and `--regress` (9/9) from that path.
3. Apply to `tools/harness/claims-freshness.py` byte-exact; verify the sha256 against O12's pin; run both commands again **from the durable path**.
4. Extract the demo sidecars to `reports/round-47/calib/`; run R1–R8; file `freshness-receipt.md` with captured output and the durable tool digest.
5. `chmod +x` is optional; the counting commands invoke `python3`. Do not add a shebang-only path dependency.
6. No corpus write, no packet-surface change, no frozen-gate re-freeze, no filed-byte edit. The only durable tool delta is `tools/harness/claims-freshness.py`; the only report delta is under `reports/round-47/`.

### 9.5 Acceptance checklist (the O verdict)

- [ ] `python3 tools/harness/claims-freshness.py --selftest` → `53/53 PASS`, exit 0.
- [ ] `--regress` → `9/9 PASS`, exit 0.
- [ ] `--claims reports/round-43/claims.json` → exit 1; O STALE, C STALE, Ca FRESH; the output prints `baseline 7ceff59a0216a8ea21ee43262d9fc72abf770cee` and `source git-tree`.
- [ ] `--claims reports/round-44/claims.json` → exit 0; O/C/Ca FRESH (the prototype fails C; the durable tool must not).
- [ ] M1/M2 → STALE; M3/M4 → FRESH.
- [ ] `--claims reports/round-47/claims.json --at 6e9a30d` → exit 0.
- [ ] Read-only: `git status --porcelain` after a run shows only `reports/round-47/`.
- [ ] G3 source grep clean.
- [ ] Two independent verifiers (O08, O09/O10/O11/O13–O15) reproduce the flags; a non-author reviewer (R04) judges the tool implements the contract, not a lookup.

If any of these is red, O is `unprovable-but-better` at best, not improved.

---

## 10. Risks, residual limits, and explicit to-verify items

1. **Mining is heuristic.** Declared `before_checks` are the durable path. The r43/r44 runs are the only mined regressions; new rounds should embed checks and run `--require-complete`. A mined FRESH is advisory, not a dispatch license.
2. **Ownership adjacency over-fires by design.** A `dream` term would flag `divination-omen-systems.md`; the gate reports and a human rules. This is the safe direction, but it means ownership terms must be discriminating (`lithic` yes; `survey` no — measured false hits at `number-symbolism.md:3`). `to-verify`: the r47 C term set excludes `survey`; the integrator should adopt exactly `cartograph|mapmaking|map-making` or the K01-measured equivalent.
3. **Capability is a marker proxy.** It does not execute the tool at baseline. A stub with the right header passes. Two markers plus the qualifier rule reduce, not eliminate, this. Record `proxy: true`; behavioral verification stays with the round's verifiers.
4. **Exit code 3 is additive to R01 §4.3.** R01 named 0/1/2; r47 requires `could-not-evaluate != green`. The renumbering from the prototype (2=stale) is a named deviation; any verifier testing the prototype's codes is testing the wrong contract.
5. **The r43 O clauses 3–4 are ungrounded.** The demo flags on clauses 1–2. Do not claim "all four clauses re-derived"; the receipt must print the two ungrounded clauses.
6. **The r44 whole-file negative control is stronger than O06's single-claim control.** Adopt both: the single-claim file for the mission's named control, the whole file for R3. The prototype's C false STALE is a live defect the durable tool must close.
7. **No tag exists in the lane to test tag resolution against.** `to-verify` at O09: the `^{commit}` path accepts a tag-to-commit and rejects a tree; the selftest tests the tree rejection (A7/A8). If a tag is created later, add a live control.
8. **Performance and repo size.** 223 blobs is small; a future corpus at 10× may need `git grep <sha>` rather than per-blob `show`. Not a v1 requirement; record the measured cold time in the receipt.
9. **This plan did not run `reports/round-47/run-validation.py`** (forbidden in-tree; the runner may not exist yet). The O counting command names it; the integrator runs it out-of-tree and must treat the gate's exit 1 on r43 as the expected refusal, not a validation failure.

---

## 11. Evidence appendix (commands this seat ran, read-only except `.scratch`)

A1 — r43 baseline facts:

```
$ git ls-tree -r --name-only 7ceff59 -- corpus/knowledge | grep -c '\.md$'
223
$ git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol | grep -c '\.md$'
26
$ git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  -
$ git show 7ceff59:tools/harness/couples-reference-extractor.py | grep -n 'basename-couples\|def couples_block'
8:Policy implemented: reports/round-39/calib/basename-couples-policy.md
50:def couples_block(text):
$ git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | sha256sum
c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f  -
$ git cat-file -e 7ceff59:tools/harness/basename-couples-resolver.py
fatal: path 'tools/harness/basename-couples-resolver.py' exists on disk, but not in '7ceff59'
$ git cat-file -e 7ceff59:reports/round-43/calib/dispositions-r38-r39.json
fatal: … not in '7ceff59'
```

A2 — r44 baseline facts:

```
$ git cat-file -e c9f4eaa:tools/harness/basename-couples-resolver.py   → absent
$ git grep -l 'four_class' c9f4eaa -- tools/                            → no output
$ git ls-tree -r --name-only c9f4eaa -- corpus/knowledge | grep -c '\.md$' → 223
```

A3 — r44 prototype on r43 (read-only; `.scratch/ca01/claims-freshness.py`):

```
[O] STALE (0/2 premises hold)
  x E1a … tool_family_absent … 2 family candidate(s)
    evidence: tools/gates/provenance-audit.py:12: * `- couples:` header line absent -> missing-couples
    evidence: tools/harness/couples-reference-extractor.py:2: """Successor couples-reference resolver…
[C] STALE (2/3 premises hold)
  x E3a … topic_unowned lithic -> 3 owner hit(s)
    evidence: …/mineral-stone-symbolism.md:1 (H1) …
    evidence: …:3 (gap filled) …
    evidence: …:5 (topic) …
[Ca] FRESH (1/1 premises hold)
summary: 1 fresh, 2 stale, 0 unverifiable, 2 ungrounded clause(s)
exit 2
```

A4 — the prototype's r44 false positive (the durable tool must close it):

```
$ python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-44/claims.json
[O] FRESH (3/3 premises hold)
[C] STALE (2/3 premises hold)
  x E3a … topic_unowned topic "its" -> 64 owner hit(s)
[Ca] FRESH (2/2 premises hold)
exit 2
```

`reports/round-44/claims.json:40` is a true `before`; the 64-hit `its` parse is a false STALE. This is a stronger negative-control requirement than O06's single-claim file.

A5 — ownership term discrimination at `6e9a30d`:

```
H1/topic owner hits for cartograph|cartographic|mapmaking|map-making: 0
with terms + survey: 3 hits, at least two of them `- gap filled:` lines
  corpus/knowledge/linguistics/dialect-register-consistency.md:4 (- gap filled: … map-drawing workflow …)
  corpus/knowledge/linguistics/sacred-registers-liturgical-language.md:4 (- gap filled: …)
  corpus/knowledge/myth-symbol/number-symbolism.md:3 (- topic: … a variance survey of 3, 4, 5 …)
```

A6 — this seat's corrected probe (` .scratch/p03/probe2.py`):

```
== r43 O @7ceff59 ==      STALE  (capability absent failed; present via witness)
== r43 C @7ceff59 ==      STALE  (223, 26 pass; lithic unowned failed; 2 owner rows)
== r43 Ca @7ceff59 ==     FRESH  (artifact absent)
== r44 O @c9f4eaa ==      FRESH  (four_class absent, one couples .py, 223)
== M1 rename target ==    STALE  (capability from before)
== M2 no numerics ==      STALE  (ownership)
== r47 C @6e9a30d ==      FRESH  (223; cartography 0 owners)
```

Probe v1 (`.scratch/p03/probe.py`) returned r43 O **FRESH** because it had no declared polarity; v2's `STALE` with the same measurement is the design law in §1.

A7 — prototype selftest, red:

```
$ python3 -B .scratch/ca01/claims-freshness.py --selftest
FAIL  grep_absent hit fails
FAIL  seventeen checks collected (18)
selftest 17/19 FAIL   RC=1
```

The first failure is the empty-glob fixture (§4.3); the second is the stale literal count (§8.2). Both are repaired by rules, not by editing the prototype.

A8 — repo state at this seat's cut:

```
$ git rev-parse HEAD       6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git status --porcelain   ?? reports/round-47/
$ find corpus/knowledge -name '*.md' | wc -l   223
$ ls corpus/knowledge/culture-material/*.md | wc -l   25
```

No filed byte edited; no corpus staging; no tool/corpus delta; the only writes by this seat are this file and `.scratch/p03/` (ephemeral). A later `git status` also shows `?? reports/round-46/review/` (mtime 14:48, before this seat's first write; not created by this seat; reported for the write-surface audit, not touched).

---

## 12. Non-goals

No corpus landing (C is a different seat), no README edit, no `run-validation.py` in-tree, no re-freeze, no packet surface, no canon/promotion/closure, no git commit/push, no network, no install. This seat does not claim O is delivered; it delivers the architecture, the verified regression expectations, and the control set the deliverable will be judged by.
