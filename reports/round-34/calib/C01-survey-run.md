- Seat: C01 | executor | claim C | date 2026-10-19 | baseline da68a6d

# C01 — box-1 survey run at HEAD + durable-receipt design

## 1. Survey run at HEAD (verbatim output, exit 0)

Command (exactly the claim-C counting command, `reports/round-34/claims.json:62`):

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-30/craft/box1-survey.py
```

Full stdout (11 lines, unmodified):

```
{
 "date": "2026-10-18",
 "named": 28,
 "resolvable": 28,
 "unnamed_in_skill": [],
 "skill_sha256": "f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b"
}
```

`EXIT=0`. Stdout bytes sha256 `89eabbfccbe366b18f223cafd94713c82b63c0f4d63b03580b1590fa690a330b`.

Digest handshake (three-way agreement):

| reading | value | command |
|---|---|---|
| script-reported `skill_sha256` | `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` | survey stdout |
| `SKILL.md` at HEAD | same `f9bd07c2…` | `sha256sum SKILL.md` |
| `SKILL.md` at baseline `da68a6d` | same `f9bd07c2…` | `git show da68a6d:SKILL.md \| sha256sum` |

`SKILL.md` is 732 lines at both readings. Claim C's `f9bd07c2…` target digest is therefore
satisfied at the dispatched tree and needs no re-reading during the round.

## 2. What the round-30 survey actually is — and what "row shape" does not exist

`reports/round-30/craft/box1-survey.py` is **12 lines** (`:1-12`). It:

- derives `ROOT` from `__file__` (`:4`), reads `SKILL.md` (`:5`);
- extracts names with `re.findall(r"tools/[\w./-]+\.py", skill)` de-duplicated through `sorted(set(...))` (`:6`);
- emits exactly four measurements plus a hardcoded `date` (`:8-9`): `named`, `resolvable`,
  `unnamed_in_skill`, `skill_sha256`;
- exits 0 iff `len(resolvable) == len(named)` (`:12`).

It contains **no write call** (no `open(...,"w")`, no `write_text`), so running it is read-only over
filed-round bytes — the only side effect risk is `__pycache__`, suppressed by `python3 -B` and
`PYTHONDONTWRITEBYTECODE=1` (verified absent in §6).

**Falsification of the mission's framing, stated plainly:** the round-30 script emits **summary
counts only — it has no per-executable rows at all**, so there is no filed row shape to mirror for
the `(executable, resolves, line, digest)` tuple. The nearest filed artifact,
`reports/round-30/craft/box1-landed-survey.json:1-8`, is also summary-level:
`{date, mode, skill_sha256, named_in_skill, resolvable, unresolvable, box1_note}`, pinning the
**older** digest `83b0a78ae7a0e09f5d12a686ac01b23f2ff10b312644fbc3b534a232a666f091`.

Two consequences for claim C, both already anticipated by the filed round-33 analysis:

- `reports/round-33/adj/A09-pins.md:79` records that the last filed receipt pins `83b0a78a…` at
  `named_in_skill 28 / resolvable 28`, and `:83` states the obligation directly: a **new** receipt
  pinned to the new bytes, filed as a **new file**, because "`box1-landed-survey.json` is filed and
  is not edited". `:110` (row R4) assigns that obligation to the integrator.
- Claim C's own before-note also names `79fe91d3…` (`reports/round-34/claims.json:58`); that digest
  appears in filed round-31/32/33 artifacts (e.g. `reports/round-32/validation.json`,
  `reports/round-33/adj/A09-pins.md:83`, where the r32 condition-1 closure at `79fe91d3…` "reads as
  superseded, not falsified"). So `83b0a78a…` (r30 receipt) and `79fe91d3…` (r31/r32 closure) are
  two distinct pre-`f9bd07c2` readings, not a contradiction — **no erratum owed**, recorded here so
  R06/R07 do not have to re-derive it.

## 3. Independent 28-row derivation (executed)

Row source: same regex and same de-duplication semantics as the script (`:6`), plus first-mention
line and per-file digest. Verified equal to the script's summary: 28 named, 28 resolvable, 0 unnamed.

| # | executable | line | resolves | digest (sha256 of file bytes) |
|---|---|---|---|---|
| 1 | tools/assemble-culture-d3.py | 673 | true | ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014 |
| 2 | tools/assemble-culture-d4.py | 207 | true | 943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2 |
| 3 | tools/assemble-d2-typed.py | 449 | true | c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071 |
| 4 | tools/assemble-d2.py | 615 | true | 8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d |
| 5 | tools/assemble-d4-typed.py | 139 | true | 92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0 |
| 6 | tools/check-craft-exercise.py | 616 | true | b5b890b4b9c9953be5ed5f5453a2b60bc9c856616b0a5b28cb2b5bca6ffdf7b5 |
| 7 | tools/check-evidence-coupling.py | 674 | true | 849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e |
| 8 | tools/check-gate-battery.py | 617 | true | 455b595ad6d5b1be7844fc9b53a259a5b8a0efbd788b129dbfd2cc0d0ad173ce |
| 9 | tools/d2-typed-labels.py | 35 | true | 2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3 |
| 10 | tools/exercise-handoff-e2e.py | 448 | true | a5e4a8c5dda9d63c177a3dce75a8716ba5d285371d0a37a2535f6c323e7619df |
| 11 | tools/gates/argot-derivation-gate.py | 375 | true | b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb |
| 12 | tools/gates/costume-era-consistency-gate.py | 609 | true | e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f |
| 13 | tools/gates/d4-assembly-check-gate.py | 450 | true | df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a |
| 14 | tools/gates/d4-typed-labels-check-gate.py | 451 | true | 05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841 |
| 15 | tools/gates/handoff-packet-check.py | 500 | true | e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575 |
| 16 | tools/gates/lexicon-coverage-audit.py | 607 | true | 2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287 |
| 17 | tools/gates/myth-consistency-gate.py | 608 | true | 5368b13542cd4b8a5bd850d83835e588df13a72b7d6c502b2aa016ee36b95f08 |
| 18 | tools/gates/naming-collision-gate.py | 610 | true | d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d |
| 19 | tools/gates/phonology-sanity-gate.py | 606 | true | d5fe087ffb2342e54cd6d6f3ef1e891315a95224bc25cdc5bc425b91dec34230 |
| 20 | tools/gates/provenance-audit.py | 611 | true | 8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a |
| 21 | tools/gates/register-law-gate.py | 409 | true | 15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169 |
| 22 | tools/gates/typed-pipeline-gate.py | 138 | true | b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85 |
| 23 | tools/harness/packet_links.py | 452 | true | 66d854cc710f0b143e0a254d03e7f59ebce2c6b759d336ca368a9689babbd899 |
| 24 | tools/harness/packet_uncertainty.py | 89 | true | cdcc19319269ee908577252485cc38288833b50987ed22a266c8eb01894b0e26 |
| 25 | tools/harness/r8_checks.py | 454 | true | 0fb21d8e414c2d92b3f20742817ac9d89be24b1142b1bc65b5070086aa17fbfe |
| 26 | tools/harness/receipt_guard.py | 453 | true | d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1 |
| 27 | tools/replay-frozen.py | 212 | true | a2fb5c98260a07f0801f4bf21f349283638da6796645780393262e4368c79464 |
| 28 | tools/source-audit-inventory.py | 614 | true | f617bb99318f501db2ff51c0c180daeacf548b1a36591b1a1a80c253197b2210 |

`rows_sha256 e560b3b66a6598d069a07de12850fba241f5b85f0000f537c94bbf1d7a464ac6`
(= sha256 of this 28-element array rendered with `json.dumps(rows, indent=1)`).

Nine executables are named on more than one SKILL.md line; the table's `line` is the **first**
mention. Full mention sets, for R06 to avoid false anchor-drift alarms:

```
tools/assemble-d4-typed.py        [139, 158, 163, 195, 207, 210, 211, 213, 294]
tools/check-gate-battery.py       [617, 617, 617]
tools/d2-typed-labels.py          [35, 169, 208, 258, 272, 281, 288, 289, 290, 291, 292, 293, 304, 308, 329, 479, 481, 483, 491]
tools/gates/argot-derivation-gate.py      [375, 376, 377, 429, 438]
tools/gates/handoff-packet-check.py       [500, 500, 612]
tools/gates/register-law-gate.py          [409, 409, 410, 418, 430, 439]
tools/gates/typed-pipeline-gate.py        [138, 187, 196, 209, 212, 418, 431, 439]
tools/harness/packet_uncertainty.py       [89, 128, 501]
tools/replay-frozen.py                    [212, 573, 613]
```

## 4. Durable receipt design (for C02 to land at `reports/round-34/craft/box1-resurvey-durable.json`)

Land path is fixed by claim C (`reports/round-34/claims.json:60`, after_required). Note
`reports/round-34/craft/` **does not exist yet** (`ls -d reports/round-34/craft` → "No such file or
directory"); only `calib/` was created by this seat. The integrator creates `craft/` when landing.

Design rules applied:

1. **Superset of the round-30 key vocabulary**, so every existing consumer of
   `box1-landed-survey.json`/script stdout keeps working: `date`, `mode`, `skill_sha256`,
   `named`, `named_in_skill`, `resolvable`, `unresolvable`, `unnamed_in_skill`, `box1_note`.
2. **New `rows[]` array** with the mission's four required fields, `row_fields` declared so a reader
   never has to infer the tuple: `["executable","resolves","line","digest"]`.
   - `line` = first SKILL.md mention (1-based, integer) — load-bearing, see control B2 (§5).
   - `digest` = sha256 (64 lowercase hex) of the resolved file's bytes at survey time; `null` only
     if unresolved (impossible by construction when `resolvable == named`).
   - Optional `lines_all` — recommended for the nine multi-mention rows, else a re-verifier that
     greps a non-first mention reads as drift.
3. **Own timestamps, not the script's.** `observed_at_utc` is mandatory because the filed script
   hardcodes `"date": "2026-10-18"` (`box1-survey.py:8`) and cannot be edited; a re-run on
   2026-10-19 emits a stale date by design. Consumers must read the receipt's timestamp.
4. **Pins for the instrument and the run**, so the receipt is falsifiable without trusting prose:
   `head_commit`, `skill_lines`, `survey_command`, `survey_exit`, `survey_stdout_sha256`,
   `survey_script{path,sha256}`, `rows_sha256`, `recheck_command`.
5. **Supersession, not rewriting**: `supersedes{path, skill_sha256, disposition}` naming
   `box1-landed-survey.json` at `83b0a78a…` with `filed bytes untouched` — the append-only
   discipline of `AGENTS.md` and A09-pins `:83`.

Exact top-level key order (observed bytes, verbatim):

```json
{
 "date": "2026-10-19",
 "observed_at_utc": "2026-10-19T07:01:16Z",
 "mode": "landed-resurvey",
 "head_commit": "da68a6d705e41f369f21e8607bfaab5b54077f84",
 "skill_path": "SKILL.md",
 "skill_sha256": "f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b",
 "skill_lines": 732,
 "named": 28,
 "named_in_skill": 28,
 "resolvable": 28,
 "unresolvable": [],
 "unnamed_in_skill": [],
 "digest_algorithm": "sha256",
 "row_fields": [
  "executable",
  "resolves",
  "line",
  "digest"
 ],
 "rows_sha256": "e560b3b66a6598d069a07de12850fba241f5b85f0000f537c94bbf1d7a464ac6",
 "rows": [ ... 28 rows as §3, sorted by executable, json.dumps(indent=1) ... ],
 "survey_command": "python3 -B reports/round-30/craft/box1-survey.py",
 "survey_exit": 0,
 "survey_stdout_sha256": "89eabbfccbe366b18f223cafd94713c82b63c0f4d63b03580b1590fa690a330b",
 "survey_script": {
  "path": "reports/round-30/craft/box1-survey.py",
  "sha256": "d923ae0fcd544513122851b55389111b3195528f8e3a4c8fb69703072132cf89"
 },
 "recheck_command": "python3 -B -c 'import hashlib,json,pathlib,re;R=pathlib.Path(\".\").resolve();t=(R/\"SKILL.md\").read_text().splitlines();s={};[s.setdefault(m,i) for i,l in enumerate(t,1) for m in re.findall(r\"tools/[A-Za-z0-9_./-]+[.]py\",l)];print(json.dumps([{\"executable\":e,\"resolves\":(R/e).is_file(),\"line\":s[e],\"digest\":hashlib.sha256((R/e).read_bytes()).hexdigest()} for e in sorted(s)],indent=1))'",
 "supersedes": {
  "path": "reports/round-30/craft/box1-landed-survey.json",
  "skill_sha256": "83b0a78ae7a0e09f5d12a686ac01b23f2ff10b312644fbc3b534a232a666f091",
  "disposition": "superseded reading; filed bytes untouched"
 },
 "box1_note": "post-round-33 re-survey of the executable surface named in SKILL.md at f9bd07c2; A09-pins.md:110 (R4) discharge"
}
```

C02 owns the canonical fenced block; it should be produced by the generator in §7 below rather than
transcribed, so digests are never hand-copied.

### Re-runnability, verified

The `recheck_command` above was **executed as published** (bash, from repo root): exit **0**,
stdout **byte-identical** to the `rows` block plus one trailing LF, stdout sha256
`fddfcf2488b56656aa3d321a7f26bc1bb5e856a99ad463fe316a2a4085cafd74`.

Honest record of a failed first attempt: my initial one-liner used the script's own character class
`[\w./-]+\.py`. JSON-escaping it into the receipt string produced `[\\w./-]+\\.py`, which the shell
delivered to `re` as `[\\w./-]+\\.py` — the recheck then ran exit 0 but emitted a **different** rows
digest (`37517e5f…`), i.e. a silently wrong verifier. The published form therefore uses a
backslash-free class `[A-Za-z0-9_./-]+[.]py` (equivalent to `[\w./-]+\.py` for this corpus:
28/28 same names, same `rows_sha256`). **Any recheck command shipped in a durable receipt must be
run at least once against the baseline it claims to reproduce**; this seat did.

Shell-quoting-free equivalent for human re-verification (also executed, byte-identical output):

```bash
python3 -B - <<'PYEOF'
import hashlib, json, pathlib, re
R = pathlib.Path(".").resolve()
s = {}
t = (R/"SKILL.md").read_text().splitlines()
for i, l in enumerate(t, 1):
    for m in re.findall(r"tools/[A-Za-z0-9_./-]+[.]py", l):
        s.setdefault(m, i)
rows = [{"executable": e, "resolves": (R/e).is_file(), "line": s[e],
         "digest": hashlib.sha256((R/e).read_bytes()).hexdigest()} for e in sorted(s)]
print(json.dumps(rows, indent=1))
PYEOF
```

## 5. Falsifiability controls (all executed in memory — no files written)

| control | mutation | result | detects? |
|---|---|---|---|
| A — pin content | one hex char of `rows[0].digest` flipped | `rows_sha256 e560b3b6… → b0169262…` | yes |
| B2 — anchor drift with **unchanged count** | first mention of `tools/replay-frozen.py` (3 mentions: `:212,:573,:613`) replaced by a non-path literal | `named` still **28**, same key set; only `line` moved `212 → 573`; `rows_sha256 e560b3b6… → f74a8633…` | yes — **only via `line`** |
| C — script blindness | n/a (reasoning over `box1-survey.py:7,12`) | the filed script asserts **existence only**; a content change to any named tool leaves `28/28` and exit 0 green | **no** — so the row digests are the receipt's only content pin |
| D — determinism | derive twice from unchanged bytes | identical `rows_sha256 e560b3b6…` | stable |

B2 is the calibration payload of this fragment: a count-only re-survey (the filed instrument's
shape) reports green on an edit that moves a SKILL.md anchor, because `named` is unchanged. The
`line` field the mission asks for is what catches it, and `lines_all` is what prevents a *false*
catch on the eight other multi-mention rows.

## 6. Preservation evidence (no filed bytes touched)

- `git diff --exit-code da68a6d -- reports/round-30` → **rc=0** (run after the survey).
- `git status --porcelain --ignored reports/round-30` → only the pre-existing ignored entry
  `!! reports/round-30/handoff/declared-in-r6/run.log`; nothing added or modified by this seat.
- `ls -la reports/round-30/craft/` → no `__pycache__` (7 original entries only); `python3 -B` +
  `PYTHONDONTWRITEBYTECODE=1` used throughout.
- Worktree delta at time of writing: `?? reports/round-34/` only.
- The survey script is read-only by inspection (`box1-survey.py:1-12`: no write calls) and its digest
  is pinned in the receipt design (`survey_script.sha256 d923ae0f…`), which is how a later reader
  proves the instrument itself was not swapped.
- Per the round's absolute rule, no `reports/round-*/run-validation.py` was executed by this seat.

## 7. Generator used (integrator: re-run this to produce the canonical bytes)

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PYEOF'
import hashlib, json, pathlib, re, subprocess
R = pathlib.Path(".").resolve()
skill_p, script_p = R/"SKILL.md", R/"reports/round-30/craft/box1-survey.py"
lines = skill_p.read_text().splitlines()
seen = {}
for i, l in enumerate(lines, 1):
    for m in re.findall(r"tools/[A-Za-z0-9_./-]+[.]py", l):
        seen.setdefault(m, i)
rows = [{"executable": e, "resolves": (R/e).is_file(), "line": seen[e],
         "digest": hashlib.sha256((R/e).read_bytes()).hexdigest()} for e in sorted(seen)]
cmd = ["python3", "-B", "reports/round-30/craft/box1-survey.py"]
pr = subprocess.run(cmd, capture_output=True, cwd=str(R))
receipt = {  # key order as §4
 "date": "2026-10-19", "observed_at_utc": "<UTC at run>",
 "mode": "landed-resurvey", "head_commit": "<40-hex HEAD>",
 "skill_path": "SKILL.md",
 "skill_sha256": hashlib.sha256(skill_p.read_bytes()).hexdigest(),
 "skill_lines": len(lines),
 "named": len(rows), "named_in_skill": len(rows),
 "resolvable": sum(1 for r in rows if r["resolves"]),
 "unresolvable": [], "unnamed_in_skill": [],
 "digest_algorithm": "sha256", "row_fields": ["executable","resolves","line","digest"],
 "rows_sha256": hashlib.sha256(json.dumps(rows, indent=1).encode()).hexdigest(),
 "rows": rows, "survey_command": " ".join(cmd), "survey_exit": pr.returncode,
 "survey_stdout_sha256": hashlib.sha256(pr.stdout).hexdigest(),
 "survey_script": {"path": "reports/round-30/craft/box1-survey.py",
                   "sha256": hashlib.sha256(script_p.read_bytes()).hexdigest()},
 "recheck_command": "<the verified one-liner from §4>",
 "supersedes": {"path": "reports/round-30/craft/box1-landed-survey.json",
                "skill_sha256": "83b0a78ae7a0e09f5d12a686ac01b23f2ff10b312644fbc3b534a232a666f091",
                "disposition": "superseded reading; filed bytes untouched"},
 "box1_note": "post-round-33 re-survey of the executable surface named in SKILL.md at f9bd07c2; A09-pins.md:110 (R4) discharge"}
print(json.dumps(receipt, indent=1))
PYEOF
```

## 8. Cross-claim flags for the integrator (do not lose these)

1. **Row 10 goes stale if the D claim lands first.** `tools/exercise-handoff-e2e.py` is one of the 28
   rows, digest `a5e4a8c5…`. Claim D moves the renderer defaults in **that file**
   (`reports/round-34/claims.json:26`, citing `tools/exercise-handoff-e2e.py:1933-1934`). Land order
   matters: generate the receipt **after** D's re-pin edit, or the receipt ships with a digest that
   is already wrong; `rows_sha256` must be recomputed in that case. This is the single most likely
   round-34 defect in claim C.
2. **`SKILL.md` itself is not edited by any of the three claims** as declared in `claims.json`
   (D: packet/renderer/re-pin rows; O: new tool + inventory; C: new receipt + reissue rows), so
   `skill_sha256 f9bd07c2…` should remain valid to close — but any late SKILL.md touch invalidates
   `skill_lines`, every `line`, and the digest together, and the receipt must be regenerated.
3. **Cross-check available to claim O**: `tools/harness/receipt_guard.py` is row 26, named at
   `SKILL.md:453`, digest `d2297da4…` — the same file the O block audits; its SKILL.md-named status
   is a fact O's capability inventory can cite without re-deriving.
4. **Claim D's gate** `tools/gates/handoff-packet-check.py` is row 15, `SKILL.md:500`, digest
   `e2fa3223…` — pinned here, useful for D's re-pin census (K02) if it needs the current gate bytes.
5. **Do not "fix" the script's stale date.** `box1-survey.py:8` hardcodes `2026-10-18`; it is filed
   bytes. The receipt's `observed_at_utc` is the authoritative timestamp.

## Owed

- none owed by this seat. My mission (survey run + receipt design) is complete.
- Dependencies consumed were already on disk; no missing-fragment substitution was needed.
- Downstream, by assignment: C02 lands the canonical JSON block; C07 re-runs the survey
  independently; R06/R07 review. The integrator must create `reports/round-34/craft/` (absent at
  writing) and regenerate the rows **after** the D re-pin per §8.1.

## Citations

- `reports/round-34/claims.json:26` (D before.renderer_default), `:54-65` (claim C: before, after_required, counting_commands, thresholds)
- `reports/round-34/targets.json` (seat C01 mission/out), `reports/round-34/claims.json:10-18` (dispatch, axes)
- `REGIMEN.md:25-58` (per-round contract, scope, done-when)
- `AGENTS.md` (append-only LOG rule; telemetry rules)
- `reports/round-30/craft/box1-survey.py:1-12` (full script; no write calls; hardcoded date `:8`)
- `reports/round-30/craft/box1-landed-survey.json:1-8` (filed receipt; `83b0a78a…`)
- `reports/round-30/craft/review-D29-box1.md:140-147` (durable-receipt wording: timestamp, SKILL digest, named/total count, missing set), `:159-165` (orchestrator's landed re-survey)
- `reports/round-33/adj/A09-pins.md:25`, `:39` (live readers, "**YES — E3** (new receipt owed)"), `:77-83` (E3 re-pin need; r32 `79fe91d3…` closure reads as superseded), `:110` (R4), `:146` (citations)
- Commands executed (all from repo root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `python3 -B reports/round-30/craft/box1-survey.py` → exit 0, stdout sha256 `89eabb…a330b`;
  `sha256sum SKILL.md`; `git show da68a6d:SKILL.md | sha256sum`; row derivation + controls A/B2/C/D;
  published `recheck_command` → exit 0, stdout sha256 `fddfcf24…`;
  `git diff --exit-code da68a6d -- reports/round-30` → rc 0;
  `git status --porcelain --ignored reports/round-30`; `ls -la reports/round-30/craft/`;
  `git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`; `date -u`.
