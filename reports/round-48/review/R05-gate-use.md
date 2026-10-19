# R05 — freshness gate: first live use (non-author review)

- Seat: `R05` | role: reviewer | claim: **cross** | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7` (`a01405d`)
- Out path: `reports/round-48/review/R05-gate-use.md` (this file)
- Non-author statement: I wrote no claim fragment, no overlay, and no tool byte. I read the filed and scratch artifacts and re-ran the gate read-only. Every number below is a command output in §9.

**One-line judgment.** The gate **instrument** is sound — `--selftest` 62/62, r43 regression correctly red (O, C stale, exit 1), r47 negative control correctly green (3 fresh, exit 0), and two identical runs produce the same decision digest. Its **first live use is not a valid measurement**: C's clearance is real; Ca's is **vacuous** (a `count_eq` over a single-file glob that counts files, not headings, and cannot see the duplicate H1); O's STALE is a **false red** produced by a sandboxed `--selftest` returning 1 for live-corpus reasons, while direct measurement shows the declared blank-separated premise is **true**. The run is also **not durably reproducible**: the overlay and the pre-drop candidates exist only in `.scratch/`, carry no claims-byte pin, and cannot be replayed against the filed `claims.json`. So: **the gate did not rubber-stamp all three — it rubber-stamped Ca and mis-reded O.** The declaration's story ("the gate caught a stale premise") should not be filed as calibration evidence without correction.

---

## 1. What I reviewed

| Artifact | What it is | Size / digest |
|---|---|---|
| `reports/round-48/claims.json` | filed claims (C, Ca; O dropped) | 5545 B, sha256 `bf8df21b641c1a49a7b71eb46504210a58096dda3f2cefa6c7618b1200535292` |
| `reports/round-48/telemetry/dispatch-declared.json` | dispatch declaration | 1239 B; its `declared_artifacts` digests match the two files above |
| `.scratch/r48-claims-skel.json` | pre-drop candidate claims (C, O, Ca) | 438 B, sha256 `65b8644146f235e51d70211c4d2650fd97a699db6a089668d3edfa1f254a5080`, mtime 2026-10-19 16:35:51 |
| `.scratch/r48-freshness-check.json` | the `--checks` overlay actually used | 1806 B, sha256 `7acbd8ca5fa79d3fff5efee3738e4111e8a6a3de3ace490195b4664982813c13`, mtime 2026-10-19 16:35:51 |
| `tools/harness/claims-freshness.py` | the gate | 105529 B, read in the cited regions |

The declaration (`claims.json:21-24`, `telemetry/dispatch-declared.json:18-20`) records the command with placeholders — `--claims <candidates> --checks <overlay>` — and the result "C FRESH …, Ca FRESH …, O STALE". Neither path is filed under `reports/round-48/telemetry/`; the only copies are the two `.scratch/` files above. R01 independently found the reproducibility gap (`reports/round-48/review/R01-review.md:192-205`); I confirm it and additionally show **what the missing overlay actually measured**.

---

## 2. Reproduction — the verdict is real, the measurement is not

Replaying the scratch pair reproduces the declared disposition exactly:

```
$ python3 -B tools/harness/claims-freshness.py \
    --claims .scratch/r48-claims-skel.json \
    --checks .scratch/r48-freshness-check.json --json
… decision_sha256 a7739149914edea215b8ce6f3048982497e0c6057967dcde4284319fba84bb93
… run_verdict stale, exit_code 1
  C  fresh  2/2 clauses hold
  O  stale  1/1 clause contradicted
  Ca fresh  1/1 clause holds
```

Two consecutive runs give the same `decision_sha256` and exit 1 (determinism holds). But the replay **cannot be made from the filed round**:

```
$ python3 -B tools/harness/claims-freshness.py --claims reports/round-48/claims.json
  [C]  COULD-NOT-EVALUATE no before_checks declared; a claim with no declared checks is not fresh
  [Ca] COULD-NOT-EVALUATE no before_checks declared; …
REFUSE: … could not be evaluated at a01405d …; exit 3

$ python3 -B tools/harness/claims-freshness.py --claims reports/round-48/claims.json \
    --checks .scratch/r48-freshness-check.json
error: overlay names claim 'O', absent from the claims file
REFUSE: input is malformed at a01405d …; exit 2
```

So there are three states on disk: the **filed claims** (no checks → CNE, exit 3), the **filed claims + used overlay** (malformed, exit 2, because O was dropped after the gate ran), and the **scratch candidates + overlay** (reproduces). Only the third is evidence, and it is not durable.

---

## 3. The three checks, measured

### 3.1 C — the clearance is real

`topic_owner_absent` over `culture-material`, fields `H1|topic|gap filled`, topics `[cartography, mapmaking, portolan, cadastral]`:

```
reason: 0 owner(s): none
status: HOLDS (expect true)
```

and `count_eq` on `corpus/knowledge/culture-material/*.md`:

```
reason: corpus/knowledge/culture-material/*.md -> 25 file(s); paths_sha256=1fe4b716a9db9a97
status: HOLDS (expected 25, measured 25)
```

My independent corpus-wide probe agrees: `grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/` → **0 lines**. C's clearance is not a rubber stamp.

Two scope caveats, neither fatal this round:

- The check scans **only `culture-material`**, while the claim's `before` says "cartography verified-fresh unowned" corpus-wide. My corpus-wide probe happens to confirm it, but the gate did not.
- Word mode is exact-word (`claims-freshness.py:759-762`): alias `cartography` does **not** match "cartographic" (I verified the regex directly). r47's overlay used the stem `cartograph`, which also fails to match "cartographic" under word mode. A future entry titled "Cartographic practice" would evade both. Use `all_tokens` or declare both forms.

### 3.2 Ca — the clearance is vacuous

The overlay declares (line numbers in `.scratch/r48-freshness-check.json`):

```
63  "clause": "README duplicate heading",
64  "probe_kind": "count_eq",
66  "glob": "corpus/README.md",
67  "value": 1
69  "expect": false
```

`count_eq` does not read file content. It counts **paths matched by the glob** and compares to the value:

```
tools/harness/claims-freshness.py:1053  def _probe_count_eq(check, tree):
1055      paths = sorted(_glob(tree, target["glob"]))
1056      value = len(paths)
1061      value == check["expect"],
```

The glob names exactly one file, so the measured value is always 1. Worse, `_coerce_check` **overwrites the declared polarity** before validation:

```
tools/harness/claims-freshness.py:2193  if kind == "count_eq" and "value" in target:
2194      check["expect"] = target.pop("value")
```

The raw `"expect": false` is discarded; the report records `expected: 1, measured: 1, HOLDS`. The `evidence_command` — `grep -c '^# kotodama-shokunin corpus index' corpus/README.md -> 2` — is validated as a string but never executed (`claims-freshness.py:930-936` validates; `:1010` records; no probe runs it).

Vacuity control: the same check pointed at a file with no duplicate heading passes.

```
$ cat vac-overlay.json   # count_eq glob corpus/QUALITY.md value 1, expect false,
                         # evidence_command = the README grep (nonsense for this file)
$ python3 -B tools/harness/claims-freshness.py --claims vac.json --checks vac-overlay.json
  [Ca] FRESH  1/1 clauses hold
exit 0
```

So "Ca FRESH (README duplicate-heading holds)" (`claims.json:23`) is **not something the gate established**. The underlying fact is true independently — `grep -c '^# kotodama-shokunin corpus index' corpus/README.md` → **2**, at the worktree and at `a01405d` (`:1` and `:3`) — but the gate's clearance would have been produced identically if the defect were absent.

### 3.3 O — the STALE is a false red

The overlay's O check (`r48-freshness-check.json:40-61`) is a `capability_present` probe: run `tools/harness/basename-couples-resolver.py --selftest` in a temp tree containing one fixture, and require `returncode == 0` **and** `success_regex = drops|0 tokens|prosody` (`claims-freshness.py:1180`).

Measured:

```
reason: 0/1 candidate(s) pass the declared behavior
status: CONTRADICTED (expect true)
```

The reason is **not** the regex. The resolver's selftest has live-corpus controls; in the one-file sandbox it fails 6 of 27 and exits 1:

```
$ # isolated tree, exact fixture, --selftest
SELFTEST FAIL: 21/27 controls
failed: S1a …, S1f …, S4a …, S4b …, S4c …, S10 …
rc=1
$ python3 -c "import re;print(bool(re.search('drops|0 tokens|prosody', out)))"
regex matches: True
```

This resolver's `--selftest` fails six live-corpus controls in the one-file sandbox and exits 1, so the check is structurally red for this candidate. It would red a true claim.

And the premise it reded is **true**. Direct measurement on the declared fixture:

```
# blank-separated hyphen soft-wrap:  "- couples: … tone-\n\n  prosody.md"
wrapped False
tokens ['x.md']            # tone-prosody.md is absent — the continuation was dropped

# no blank line:                     "- couples: … tone-\n  prosody.md"
wrapped True
tokens ['tone-prosody.md', 'x.md']
```

The mechanism is visible in the resolver: the documented hyphen exception is unreachable because `soft_wrap` itself requires `not saw_blank`:

```
tools/harness/basename-couples-resolver.py:55-59  "A blank line terminates the block
    unless the previous part ends in a hyphen soft wrap and the next line is indented"
tools/harness/basename-couples-resolver.py:73     soft_wrap = parts[-1].endswith("-") and not saw_blank
tools/harness/basename-couples-resolver.py:74     if INDENT_RE.match(following) and (not saw_blank or soft_wrap):
```

After a blank line `saw_blank` is True, so `soft_wrap` is False and the continuation is dropped — the exact latent edge the pre-drop candidate names (`r48-claims-skel.json:13`: "resolver drops blank-separated hyphen soft-wrap tokens (latent edge)"). The measured signature `wrapped=False tokens=1` recorded at `claims.json:19` is therefore **evidence for** the premise, not against it. The narrative "premise false as framed — the resolver yields wrapped=False tokens=1, a different edge" conflates the working **non-blank** soft-wrap with the broken **blank-separated** one. If the original premise had been the unqualified "resolver drops hyphen soft-wrap", it would be false (non-blank heals); as filed, it is the narrower blank-separated claim and it holds.

**Consequence:** the O drop removed a **live, verified operability edge** from the round on a false negative. That is calibration harm, not a gate success.

A repaired probe that actually measures the edge (verified, §7):

```
argv: ["--census","--json","corpus/knowledge/linguistics/phonetics-phonology.md"]
success_regex: '"wrapped": true'
expect: false                      # bug present: blank-separated continuation is not healed
→ [O] FRESH  1/1 clauses hold, exit 0
```

---

## 4. Defects

| ID | Severity | Finding | Evidence | Fix |
|---|---|---|---|---|
| **G1** | blocking to "first live use correct" | **Ca clearance is vacuous.** `count_eq` over `corpus/README.md` counts matching files (always 1), not headings; the declared `expect:false` is silently replaced by `value:1`. The gate would clear the claim with the defect absent. | overlay `:63-69`; probe `claims-freshness.py:1053-1064`; coercion `:2193-2196`; my `corpus/QUALITY.md` control → FRESH | Declare a content-count check (new `grep_count_eq` probe, or a sweep leg), or record Ca's premise as verified by command, not by the gate. Do not cite the gate for the duplicate heading. |
| **G2** | blocking | **O STALE is a false red.** The capability probe runs a live-corpus-dependent `--selftest` in a one-file sandbox; `returncode != 0` alone defeats the regex (which does match). Direct census shows the blank-separated hyphen continuation is dropped — the premise is true. | `claims-freshness.py:1180`; sandbox 21/27 rc 1; census `wrapped False / ['x.md']`; resolver `:73`; control probe in §7 | Re-run O with a census-based probe (§7) and restore the edge as a candidate, or record the drop as `dropped-on-invalid-measurement`. |
| **G3** | blocking to reproducibility | **No durable evidence.** Candidate file and overlay live only in `.scratch/`; the overlay has no `claims_sha256` pin (unlike `reports/round-47/calib/r43-checks.json:5`); the declared command has placeholders. Filed claims alone → exit 3; filed claims + the used overlay → exit 2. | `AGENTS.md:17-18`; replay outputs §2; `dispatch-declared.json:18-20` | File the candidate file, overlay, and JSON report under `reports/round-48/telemetry/freshness-r48/` with their sha256, the baseline, and the exit code; add `claims_sha256`. |
| **G4** | P2 | **Narrative overstates the gate.** `claims.json:23` says "Ca FRESH (README duplicate-heading holds)"; the check never measured headings. `telemetry:20` says "caught a stale premise"; the premise it named holds. | §3.2, §3.3 | Correct the wording in a successor record (do not rewrite the filed declaration): "C cleared; Ca not measurable by this probe; O dropped on an invalid probe — edge re-verified true". |
| **G5** | P2 | **Topic alias misses morphology.** Word mode matches whole words only; `cartography` does not match "cartographic", and r47's `cartograph` does not either. | `claims-freshness.py:759-762`; direct regex test | Include both forms, or use `all_tokens`/`phrase` on a stem list; note in the overlay's `note`. |
| **G6** | P3 | **C's check scope is narrower than its premise.** The probe scans `culture-material` only; the claim asserts corpus-wide freshness. My independent corpus-wide grep confirms 0, but that is not the gate's measurement. | §3.1 | Add a second `topic_owner_absent` over all partitions, or narrow the `before` wording. |
| **G7** | note | **`--selftest` is the wrong surface for a capability probe.** Any tool whose selftest depends on live corpus will be structurally red in the gate's sandbox; the `rc == 0` gate also makes regex design secondary. | resolver selftest 6 live-dependent FAILs | Prefer a targeted subcommand with deterministic output (`--census --json` on a fixture). |

No defect is in the gate's *input contract* (exit 0/1/2/3, no worktree read, deterministic) — the r47 instrument is good. The defects are in **this use** and in **one probe-design assumption**.

---

## 5. Anti-rubber-stamp controls (the instrument still discriminates)

| Control | Result |
|---|---|
| `--selftest` | `PROBE-REGISTRY SELFTEST: 43/43`; `SELFTEST OK: registry 43/43 + seam 19/19`; exit 0 |
| r43 regression (`reports/round-43/claims.json` + `calib/r43-checks.json`) | O and C stale, Ca fresh; `REFUSE … exit 1` — correctly red |
| r47 negative control (`reports/round-47/claims.json` + `calib/r47-checks.json`) | 3 fresh, exit 0 — correctly green |
| Polarity control (`divination` in `myth-symbol`, expect unowned) | CONTRADICTED, 4 owners found — correctly red |
| Fresh control (`zzznotatopic`, expect unowned) | HOLDS — correctly green |
| `count_eq` file-count control (2 expected on a 1-file glob) | CONTRADICTED, measured 1 — proves it counts files, not headings |
| Machinery control (`--help` + `usage:` regex, expect true) | HOLDS — capability execution works |
| Determinism | two runs → same `decision_sha256`, same exit |

The gate can go red and green for the right reason on filed overlays. The r48 result failed because of **probe choice**, not because the gate is broken.

---

## 6. Verdict and axis consequence

- **C (coverage):** gate clearance **confirmed**. The gate measured ownership and partition count correctly, and independent probes agree. No harm.
- **Ca (calibration):** gate clearance **not confirmed** — vacuous check. The claim's underlying fact is true by command (`grep -c` = 2), but the gate is not its evidence.
- **O (operability, dropped):** gate verdict **not confirmed and likely wrong** — false red; the edge is real. Dropping O is defensible only if the round decides the edge is out of scope; it is not defensible as "the premise was false".
- **Calibration axis consequence:** unchanged in the sense that no corpus byte is harmed; but the round's calibration evidence is weaker than declared. The honest record is: *C verified; Ca verified by command, not gate; O edge verified true, dropped on an invalid probe.*

**Recommendation to the integrator:** do not file "the gate's first live use was correct" as a closed calibration fact. File the three-state reproducibility gap (G3) and the two probe-design defects (G1/G2) as a queue row, and either re-run O with the §7 probe or record the drop as invalid-measurement. This is a successor record, not an edit to `reports/round-48/claims.json`.

---

## 7. Repair recipe (drafted, not applied)

1. **Durability (G3).** Copy, do not move, into `reports/round-48/telemetry/freshness-r48/`:
   - `candidates.json` ← `.scratch/r48-claims-skel.json` (sha256 `65b86441…`)
   - `overlay.json` ← `.scratch/r48-freshness-check.json` (sha256 `7acbd8ca…`) plus `"claims_sha256": "<sha of candidates.json>"`
   - `report-observed.json` ← the `--json` output whose `decision_sha256` is `a7739149…`, exit 1, with the note that Ca's check is vacuous and O's is structurally red.
2. **Corrected Ca declaration.** The gate cannot count content with the current vocabulary (`claims-freshness.py:96-106`). Either add a `grep_count_eq` probe (`target: {glob, regex, value}`; measured = number of matching lines; expect = integer), or record Ca's premise as command-verified (`grep -c … = 2`) with no gate claim.
3. **Corrected O probe (verified above).**

```json
{"clause": "blank-separated hyphen soft-wrap is dropped",
 "probe_kind": "capability_present",
 "target": {"globs": ["tools/harness/basename-couples-resolver.py"],
            "exclude_globs": [],
            "argv": ["--census", "--json",
                     "corpus/knowledge/linguistics/phonetics-phonology.md"],
            "fixture": {"corpus/knowledge/linguistics/phonetics-phonology.md":
                        "- couples: a — `x.md`; prospective sibling files: tone-\n\n  prosody.md\n"},
            "success_regex": "\"wrapped\": true",
            "timeout_s": 30, "max_candidates": 4},
 "expect": false,
 "evidence_command": "census of the blank-separated fixture"}
```

Result: `[O] FRESH 1/1 clauses hold; exit 0` — i.e. the bug is present. This is a measurement, not a selftest return code.

4. **Resolver edge (for the O successor, not this round):** `tools/harness/basename-couples-resolver.py:73` makes the docstring's hyphen exception (`:55-59`) unreachable. The one-line fix is `soft_wrap = parts[-1].endswith("-")` (or hoist the `not saw_blank` out), with S7c re-read: S7c asserts blank-line exclusion for *prose*, so the fixture must keep the hyphen case distinct from prose. That is an operability change and needs its own claim.

---

## 8. What I did not verify

- The original candidate `claims.json` *before* `.scratch/r48-claims-skel.json`. The skel is the only pre-drop artifact; if the real candidate's `before` was the unqualified "drops hyphen soft-wrap", O's drop is more defensible. The evidence supports the skel's narrower wording, and that wording is true.
- Whether O01/O04 reached the same conclusions; their out files were absent at my cut. R01 independently found the durability gap (`R01-review.md:192-205`).
- The gate's behavior under `--at` (deviation recording); not exercised here.
- Any claim about the corpus content beyond the probes in §3; my independent checks are limited to topic-line greps and the README heading count.
- Long-run stability: I ran the gate repeatedly today (selftest, replay twice, five control runs); no concurrency or clock dependence observed, but I did not fuzz it.

---

## 9. Commands and write-surface statement

Run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ sha256sum reports/round-48/claims.json reports/round-48/targets.json
bf8df21b641c1a49a7b71eb46504210a58096dda3f2cefa6c7618b1200535292  reports/round-48/claims.json
d029eaa1e37481918c10c20bb7ced3e3e31a8886a207cca05cb55ee3aaa20446  reports/round-48/targets.json
$ sha256sum .scratch/r48-claims-skel.json .scratch/r48-freshness-check.json
65b8644146f235e51d70211c4d2650fd97a699db6a089668d3edfa1f254a5080  .scratch/r48-claims-skel.json
7acbd8ca5fa79d3fff5efee3738e4111e8a6a3de3ace490195b4664982813c13  .scratch/r48-freshness-check.json
$ python3 -B tools/harness/claims-freshness.py --selftest | tail -2
PROBE-REGISTRY SELFTEST: 43/43
SELFTEST OK: registry 43/43 + seam 19/19 controls
$ python3 -B tools/harness/claims-freshness.py --claims .scratch/r48-claims-skel.json \
    --checks .scratch/r48-freshness-check.json --json
decision_sha256 a7739149914edea215b8ce6f3048982497e0c6057967dcde4284319fba84bb93; exit 1
$ python3 -B tools/harness/claims-freshness.py --claims reports/round-48/claims.json
[C] COULD-NOT-EVALUATE …; [Ca] COULD-NOT-EVALUATE …; exit 3
$ python3 -B tools/harness/claims-freshness.py --claims reports/round-48/claims.json \
    --checks .scratch/r48-freshness-check.json
error: overlay names claim 'O', absent from the claims file; exit 2
$ python3 -B tools/harness/claims-freshness.py --claims reports/round-43/claims.json \
    --checks reports/round-47/calib/r43-checks.json
1 fresh, 2 stale …; REFUSE: claims O, C …; exit 1
$ python3 -B tools/harness/claims-freshness.py --claims reports/round-47/claims.json \
    --checks reports/round-47/calib/r47-checks.json
3 fresh, 0 stale …; exit 0
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2                      # and 2 for `git show a01405d:corpus/README.md | grep -c …`
$ grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/ | wc -l
0
$ # direct resolver census, blank-separated fixture
wrapped False; tokens ['x.md']
$ # direct resolver census, no blank line
wrapped True; tokens ['tone-prosody.md', 'x.md']
$ # isolated --selftest
SELFTEST FAIL: 21/27 controls; rc=1; regex 'drops|0 tokens|prosody' matches: True
$ # vacuity control: count_eq on corpus/QUALITY.md, value 1, expect false
[Ca] FRESH 1/1 clauses holds; exit 0
$ # repaired O probe (§7)
[O] FRESH 1/1 clauses holds; exit 0
```

**Write surface:** this file only — `reports/round-48/review/R05-gate-use.md`. Probes and their outputs were written to `.scratch/r05-*` (temporary, not filed). No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network, no `run-validation.py` in-tree. `git status --porcelain` at my cut: `?? reports/round-46/review/`, `?? reports/round-48/` only.
