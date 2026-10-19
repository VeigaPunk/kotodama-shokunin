- Seat: O08 | verifier | claim O | date 2026-10-19 | baseline 4a7aede

# O08 — acceptance legs for `reports/round-35/run-validation.py` (claim O, R34-N1 hardening)

**Mission** (`reports/round-35/targets.json:236`). Verify the final
(post-integrator-application) state will be checkable: define the acceptance legs
for `run-validation.py` — named-diagnostic regex, exit codes, selftest counts — so
the validator author can implement them.

**Dependency status.** No O-block fragment is landed at write time
(`find reports/round-35 -type f` → `claims.json`, `targets.json`,
`telemetry/availability-attempt-{1,2,3}.json`, `telemetry/dispatch-declared.json`
only), and `reports/round-35/run-validation.py` does not exist
(`ls reports/round-35/run-validation.py` → no such file). The renderer is
unpatched: live `tools/exercise-handoff-e2e.py` sha256
`34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9` equals
`git show HEAD:tools/exercise-handoff-e2e.py | sha256sum` (HEAD = `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`).
Everything below is therefore measured on the **pre-patch** bytes and written as
**content-addressed** legs (regex / exit code / counts / live digests), so they
hold after the patch. What depends on the patch's exact wording is under `## Owed`.

## 1. Pre-patch measurements (the "before" every leg is defined against)

All commands run from the lane root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. No filed round runner was
executed; only `tools/exercise-handoff-e2e.py` (non-freeze modes).

| # | command | observed |
|---|---|---|
| B1 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | **exit 1**, raw traceback on stderr, `KeyError: 'reports/round-20/handoff/claims-map.md'` raised at `tools/exercise-handoff-e2e.py:3822` (`live {assembly.digests[rel][:12]}…`) — the defect, not a diagnostic |
| B2 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | **exit 0**; `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` |
| B3 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` | **exit 0**; header verbatim `selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0, links=105/105, claims=27, statuses=16/7/4, v2_subset=equal, alias_leg=landed) plus 39 controls:`; `grep -c '^  - '` = **40** result lines = 1 positive + 39 controls |
| B4 | per-file `sha256sum` vs `git show HEAD:<path>` for `reports/round-30/handoff/declared-in-r6/{expected.json,packet.md,twin.json,freeze.txt}` and `reports/round-34/handoff/declared-in-r7/{expected.json,packet.md,twin.json,freeze.txt,claims-map.md}` | all **9 tracked files SAME as HEAD**; r6 `packet.md` = `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` |
| B5 | `git check-ignore -v …/declared-in-{r6,r7}/run.log` | both ignored by `.gitignore:3` (`*.log`) → **no HEAD reference exists** for `run.log`; only a before/after digest leg is possible |
| B6 | `git status --porcelain` | `?? reports/round-35/` only — no tracked byte moved |

Defect provenance: `reports/round-34/handoff/repin.json:50` (R34-N1, state
`routed`, owner "renderer hardening (future round)") and the recorded control at
`reports/round-34/handoff/repin.json:19-21`. The r6 row's member is
`reports/round-20/handoff/claims-map.md` with frozen digest
`4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8`
(`reports/round-30/handoff/declared-in-r6/expected.json` `inputs`), while the
current renderer's read set names the successor
`reports/round-34/handoff/declared-in-r7/claims-map.md` (`tools/exercise-handoff-e2e.py:184`,
`d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c`).

## 2. The binding acceptance legs

Group `O` of the validator; names `O1`…`O6`. Legs O1–O4 are **behavioural**
(binding). O5–O6 are **static corroboration** (a failure is a named finding; a
green does not substitute for O1–O4).

### O1 — r6 replay raises the named diagnostic (the claim's core leg)

- command: `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json`
- required, on `stdout + stderr` combined:
  - exit code **non-zero and in {1, 2}** — never 0, never a Python crash code from an unhandled exception;
  - token `\bE2E-READSET\b` present;
  - **one single line** carries both the token and the literal member path
    `reports/round-20/handoff/claims-map.md`:
    `^.*\bE2E-READSET\b.*reports/round-20/handoff/claims-map\.md.*$` (multiline);
  - **no** `Traceback (most recent call last)` and **no** `\bKeyError\b` anywhere in the combined output.
- refused: exit 0; any traceback/`KeyError` (B1, unfixed); a non-zero exit whose
  message names no code, or a code that names no member path
  (`reports/round-35/claims.json:45` requires the diagnostic to carry the
  unresolvable path).

### O2 — selftest green with the two new controls

- command: `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` (allow ≥ 300 s; measured 38.6 s pre-patch)
- required:
  - exit 0;
  - header matches
    `^selftest: OK — positive run \(exit 0, fields=16/16, glossary-entries=20, findings=0, links=105/105, claims=27, statuses=16/7/4, v2_subset=equal, alias_leg=landed\) plus (\d+) controls:$`
    with **N ≥ 41** (pre-patch N = 39, B3; the claim adds exactly two controls);
  - count of lines matching `^  - ` equals **N + 1** (pre-patch 40 = 39 + 1, B3);
  - **new control (superseded-row refusal):** at least one `^  - ` line contains
    `E2E-READSET` and names the superseded row
    (`(?i)superseded|declared-in-r6|round-30|unresolvable`) and names the exit code
    (`exit 1` or `exit 2`);
  - **preserved digest path:** at least one `^  - ` line contains `E2E-DIGEST` and
    `exit 1` (pre-patch `  - m12b tamper read-set (D4 projection): exit 1 E2E-DIGEST naming the changed file`);
  - **preserved flipped-sha control:** a line containing
    `m12a tamper baseline: exit 2 E2E-BASELINE` (pre-patch present).
- refused: N < 41 (patch not landed); a "control" that merely raises without
  asserting the code and the exit (vacuity); the m12a/m12b lines disappearing
  (`reports/round-35/claims.json:45` makes both the named refusal and the
  unchanged E2E-DIGEST/E2E-BASELINE paths binding).

### O3 — r7 default chain regression

- command: `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet`
- required: exit 0; stdout matches
  `^handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=([0-9a-f]{64})$`;
  captured sha equals the live `sha256sum reports/round-34/handoff/declared-in-r7/packet.md`
  (B2/B4: `45f57132…`), i.e. the patch neither moves the packet nor the frozen row.
- refused: any non-zero exit, any summary-shape change, any packet-sha drift.

### O4 — no freeze bytes move

- required:
  - for the 9 tracked files in `reports/round-30/handoff/declared-in-r6/` and
    `reports/round-34/handoff/declared-in-r7/` (`expected.json`, `packet.md`,
    `twin.json`, `freeze.txt`, `claims-map.md` where present): live sha256 ==
    `git show HEAD:<path>` sha256 (all SAME at B4);
  - `git status --porcelain -- reports/round-30/handoff/declared-in-r6 reports/round-34/handoff/declared-in-r7` empty;
  - `run.log` in both dirs: digest snapshot **before** and **after** the
    validator's own renderer runs must be equal, recorded with
    `status = could-not-evaluate` for the HEAD comparison and reason
    "gitignored (.gitignore:3 `*.log`): no HEAD reference exists" (B5) — never a
    silent green, never a claim of HEAD equality;
  - the validator must not have run `--freeze` against either dir (see O6).
- refused: any moved byte; a re-freeze of declared-in-r7 to make the r6 replay
  pass; an edit of the r6 baseline (both are non-goals,
  `reports/round-35/claims.json:56-62` and the shared rules' "never edit filed
  round bytes").

### O5 — the patch is present and is a renderer-only edit (static)

- required: live renderer sha != `34c85f57…` (pre-patch) and
  `git show HEAD:tools/exercise-handoff-e2e.py` sha == `34c85f57…`; renderer source
  contains `E2E-READSET`; the receipt records the post-patch renderer sha256.
- refused: renderer unchanged (patch not applied); the token present only in a
  comment while O1 still crashes (O1 is binding).

### O6 — the validator itself stays inside the fences (static, F-C13-1 / freeze ban)

- required: the validator source contains no quoted `--freeze` argv literal
  (`'"--freeze"'` / `"'--freeze'"`) and no filed round-runner path
  `reports/round-(?:[1-9]|[12]\d|3[0-4])/run-validation\.py` (its own round-35 path
  is exempt); the receipt records the commands it ran.
- refused: any in-tree execution of a filed round runner (ABSOLUTE rule, shared
  rules line "never execute any reports/round-*/run-validation.py in-tree"), and
  any re-freeze of the pinned declared-in-r7 bytes.

## 3. The named diagnostic — required shape and recommended wording

Binding: the code token `E2E-READSET` and the member path must appear on one line
(§2 O1). The code is *new*: it is not in the renderer's documented exit-code table
(`tools/exercise-handoff-e2e.py:89-93` lists only `E2E-DIGEST, E2E-COUNT,
E2E-GATE, E2E-SCAN, E2E-UNC, E2E-LINK` at exit 1 and `E2E-ARTIFACT,
E2E-BASELINE, E2E-DATA` at exit 2), so the patch must extend that table and the
module docstring; the validator may check that the docstring names `E2E-READSET`
(O5, static, optional).

Recommended canonical message (the validator must not require this exact wording,
only §2 O1):

```
FAIL input-digest: reports/round-20/handoff/claims-map.md: frozen 4b1b9a35a18f… but this renderer's
read set does not name it (superseded by reports/round-34/handoff/declared-in-r7/claims-map.md)
handoff-v3: exit=2 …
handoff-v3: E2E-READSET: 1 baseline read-set member(s) unresolvable in this renderer's read set: reports/round-20/handoff/claims-map.md
```

The per-row `record(...)` detail line and the summary diagnostic line may be one
line or two; the leg only requires that at least one line carries both tokens.

## 4. Exit-code policy (the one genuine ambiguity, resolved)

- `reports/round-35/claims.json:48` declares `(expect: exit 1, named diagnostic)`;
  `reports/round-35/claims.json:45` requires only "exits non-zero with a named
  diagnostic", and `:51` requires "named diagnostic at the r6 replay".
- The renderer's own convention (`tools/exercise-handoff-e2e.py:89-93`) puts
  *could-not-evaluate* classes at exit 2. An unresolvable baseline member is
  exactly that class (cf. `E2E-BASELINE` for an unusable baseline, exit 2), so
  **exit 2 with `E2E-READSET` is the convention-correct implementation**; exit 1
  (a `Failed`-class refusal) also satisfies the binding text.
- **Leg policy:** accept `{1, 2}` when the code token and the member path are
  present (O1); record the observed value in the receipt; if the implementation
  lands on 2, record the `claims.json:48` "(expect: exit 1)" string as a **named
  deviation in the receipt** — claims.json is a declared artifact of this round
  and is not edited in place (the round-34 precedent for declared deviations is
  `reports/round-34/run-validation.py:124-126`).
- Refused in every case: exit 0; exit 1 via an unhandled `KeyError`; any exit with
  no named code.

## 5. Selftest counts (exact numbers the validator should assert)

| quantity | pre-patch (measured, B3) | post-patch required |
|---|---|---|
| selftest exit | 0 | 0 |
| `plus (\d+) controls` | 39 | ≥ 41 |
| `^  - ` result lines | 40 | N + 1 |
| new `E2E-READSET` control lines | 0 | ≥ 1, naming the superseded row and the exit code |
| `E2E-DIGEST` + `exit 1` control lines | 1 (`m12b`) | ≥ 1 |
| `m12a tamper baseline: exit 2 E2E-BASELINE` | present | present |

The exact post-patch count depends on the integrator's control wording (O02); the
validator should assert the ≥ 41 floor plus the content anchors, not an exact
number, so a third corroborating control does not read as a failure. If the
landed count is exactly 41 with both anchors, that is the expected shape.

## 6. Paste-ready leg implementation (draft for the validator author)

Stdlib-only, matching the round-34 runner idioms (`run_command` uses
`sys.executable -B`; `sha_file`/`read`/`git` as in
`reports/round-34/run-validation.py:29-70`). The integrator applies this into
`reports/round-35/run-validation.py`; I write no `tools/**` or `reports/**`
runner myself.

```python
# --- claim-O legs (drafted by O08; see reports/round-35/op/O08-validation-legs.md) ---
RENDERER = "tools/exercise-handoff-e2e.py"
RENDERER_PRE_PATCH = "34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9"
R6_DIR = "reports/round-30/handoff/declared-in-r6"
R6_BASELINE = f"{R6_DIR}/expected.json"
R6_MEMBER = "reports/round-20/handoff/claims-map.md"
R7_DIR = "reports/round-34/handoff/declared-in-r7"
FREEZE_FILES = ("expected.json", "packet.md", "twin.json", "freeze.txt", "claims-map.md")

READSET_CODE = re.compile(r"\bE2E-READSET\b")
READSET_LINE = re.compile(r"^.*\bE2E-READSET\b.*" + re.escape(R6_MEMBER) + r".*$", re.M)
CRASH_RE = re.compile(r"Traceback \(most recent call last\)|\bKeyError\b")
SELFTEST_HEADER = re.compile(
    r"^selftest: OK — positive run \(exit 0, fields=16/16, glossary-entries=20, findings=0, "
    r"links=105/105, claims=27, statuses=16/7/4, v2_subset=equal, alias_leg=landed\) plus (\d+) controls:$", re.M)
V3_SUMMARY = re.compile(
    r"^handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 "
    r"statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=([0-9a-f]{64})$", re.M)
FILED_RUNNER = re.compile(r"reports/round-(?:[1-9]|[12]\d|3[0-4])/run-validation\.py")


def leg_o1_readset_refusal():
    failures, m = [], {}
    run = run_command("O1-readset",
                      [RENDERER, "--profile", "v3", "--quiet", "--baseline", R6_BASELINE])
    out = run["stdout"] + run["stderr"]
    m["exit_code"] = run["exit_code"]
    m["named_code"] = bool(READSET_CODE.search(out))
    if run["exit_code"] not in (1, 2):
        failures.append(f"O1: r6 replay exit {run['exit_code']}, expected non-zero 1 or 2")
    if CRASH_RE.search(out):
        failures.append("O1: r6 replay still surfaces a traceback/KeyError (R34-N1 unfixed)")
    if not m["named_code"]:
        failures.append("O1: no E2E-READSET token on the r6 replay output")
    if not READSET_LINE.search(out):
        failures.append(f"O1: no single line carries E2E-READSET and {R6_MEMBER}")
    return failures, m


def leg_o2_selftest():
    failures, m = [], {}
    run = run_command("O2-selftest", [RENDERER, "--profile", "v3", "--selftest"], timeout=300)
    out = run["stdout"] + run["stderr"]
    header = SELFTEST_HEADER.search(out)
    lines = [l for l in out.splitlines() if l.startswith("  - ")]
    controls = int(header.group(1)) if header else None
    m.update({"exit_code": run["exit_code"], "controls": controls, "result_lines": len(lines)})
    if run["exit_code"] != 0:
        failures.append(f"O2: selftest exit {run['exit_code']}")
    if header is None:
        failures.append("O2: selftest header changed shape (positive-run summary or 'plus N controls' gone)")
    elif controls < 41:
        failures.append(f"O2: only {controls} controls; the two new controls are not landed (pre-patch 39)")
    if controls is not None and lines and len(lines) != controls + 1:
        failures.append(f"O2: {len(lines)} result lines != controls+1 ({controls}+1)")
    new = [l for l in lines if "E2E-READSET" in l
           and re.search(r"(?i)superseded|declared-in-r6|round-30|unresolvable", l)
           and re.search(r"exit [12]\b", l)]
    m["readset_controls"] = new
    if not new:
        failures.append("O2: no control line asserts the superseded-row refusal (E2E-READSET + row + exit)")
    if not [l for l in lines if "E2E-DIGEST" in l and re.search(r"exit 1\b", l)]:
        failures.append("O2: the content-tampered read-set E2E-DIGEST path has no control line")
    if not [l for l in lines if "m12a tamper baseline: exit 2 E2E-BASELINE" in l]:
        failures.append("O2: the flipped-sha expectation control (m12a) is gone")
    return failures, m


def leg_o3_r7_regression():
    failures, m = [], {}
    run = run_command("O3-r7", [RENDERER, "--profile", "v3", "--quiet"])
    summary = V3_SUMMARY.search(run["stdout"])
    m["exit_code"] = run["exit_code"]
    m["packet_sha256"] = summary.group(1) if summary else None
    if run["exit_code"] != 0:
        failures.append(f"O3: r7 default chain exit {run['exit_code']}")
    if summary is None:
        failures.append("O3: r7 summary line changed shape")
    elif summary.group(1) != sha_file(f"{R7_DIR}/packet.md"):
        failures.append("O3: r7 packet sha != on-disk frozen packet")
    return failures, m


def leg_o4_freeze():
    failures, m = [], {}
    moved = []
    for rel_dir in (R6_DIR, R7_DIR):
        for name in FREEZE_FILES:
            path = f"{rel_dir}/{name}"
            live, head = sha_file(path), sha_bytes(git("show", f"HEAD:{path}").stdout)
            if live is None:
                continue
            if live != head:
                moved.append(path)
    m["moved"] = moved
    if moved:
        failures.append(f"O4: filed freeze bytes moved: {moved}")
    proc = git("status", "--porcelain", "--", R6_DIR, R7_DIR)
    if proc.returncode == 0 and proc.stdout.strip():
        failures.append("O4: git status reports changes under the freeze dirs")
    m["run_log"] = {f"{d}/run.log": sha_file(f"{d}/run.log") for d in (R6_DIR, R7_DIR)}
    m["run_log_head_check"] = {"status": "could-not-evaluate",
                               "reason": "gitignored (.gitignore:3 *.log): no HEAD reference exists"}
    return failures, m


def leg_o5_patch_present():
    failures, m = [], {}
    live = sha_file(RENDERER)
    head = sha_bytes(git("show", f"HEAD:{RENDERER}").stdout)
    m.update({"live_sha256": live, "head_sha256": head})
    if head != RENDERER_PRE_PATCH:
        failures.append("O5: baseline renderer bytes differ from the measured pre-patch sha")
    if live == RENDERER_PRE_PATCH:
        failures.append("O5: renderer unchanged — the patch is not applied")
    if "E2E-READSET" not in read(RENDERER):
        failures.append("O5: renderer source carries no E2E-READSET token")
    return failures, m


def leg_o6_fences():
    failures, m = [], {}
    src = read(f"{ROUND}/run-validation.py")
    if '"--freeze"' in src or "'--freeze'" in src:
        failures.append("O6: the validator names a --freeze argv literal (declared-in-r7 bytes are pinned)")
    if FILED_RUNNER.search(src):
        failures.append("O6: the validator names a filed round runner (F-C13-1: never executed in-tree)")
    m["renderer_sha256"] = sha_file(RENDERER)
    return failures, m
```

## 7. What must be refused (anti-defect list for the reviewer seats O05/O11)

- R-a exit 0 on the r6 replay (a superseded row silently accepted).
- R-b any `KeyError`/traceback on the r6 replay (R34-N1 unfixed) — the current B1 state.
- R-c a non-zero exit with no code token, or a code token on a different line from the member path.
- R-d "fixing" the r6 replay by re-freezing or editing `reports/round-30/handoff/declared-in-r6/**` or `reports/round-34/handoff/declared-in-r7/**` (both pinned; re-freeze forbidden).
- R-e a selftest accepted below 41 controls, or a control that raises without asserting code + exit (vacuity).
- R-f a validator that executes any filed round runner in-tree (F-C13-1 class) or that reports `run.log` as HEAD-verified.

## 8. to-verify

- The exact post-patch control wording and count (owes O02); my anchors are
  content-based, so wording drift is tolerated, count < 41 is not.
- The integrator's exit-code choice (1 vs 2) — both accepted; if 2, the
  `claims.json:48` string is a named deviation, recorded not edited.
- Whether the patched renderer also exposes `E2E-READSET` as the `code` field of
  its `--json` receipt (`tools/exercise-handoff-e2e.py:4605-4608` prints
  `{"code": err}`; on an `Unevaluatable` the code is the exception's `code`
  attribute, `:3974-3976`). Optional secondary assertion; O1 is binding without it.
- Whether the patched renderer's docstring/exit table (`:89-93`) names
  `E2E-READSET` — recommended, not required by the claim text.

## 9. Leg self-check (this fragment's own controls)

Every regex above was exercised against the measured bytes before filing (one
`python3 -B` control run from the lane root):

- the §6 snippet extracts from this fragment and `compile()`s clean (129 lines, 0 errors);
- `SELFTEST_HEADER` matches the B3 header verbatim and captures `39`; the
  `^  - ` line count is `40` = 39 + 1; both the `m12a` (`exit 2 E2E-BASELINE`)
  and `m12b` (`exit 1 E2E-DIGEST`) anchors are found in the pre-patch suite;
- `V3_SUMMARY` matches the B2 line and its captured sha equals
  `sha256sum reports/round-34/handoff/declared-in-r7/packet.md`;
- against the B1 pre-patch r6 replay, the O1 leg fails as designed: exit 1,
  `CRASH_RE` true, `E2E-READSET` token absent, single-line code+member regex false;
- against a synthetic post-patch diagnostic line
  (`handoff-v3: E2E-READSET: 1 baseline read-set member(s) unresolvable: reports/round-20/handoff/claims-map.md`)
  the O1 leg's token, single-line and no-crash conditions all hold — so the leg is
  satisfiable by the shape §3 recommends and cannot be satisfied by the pre-patch
  bytes.

## Owed

- `op/O01-patch-draft.md` — the exact diagnostic wording/class the patch lands
  (my O1 regexes must be reconciled with it; if the landed wording cannot put the
  code and the member path on one line, the leg's single-line requirement is the
  point to renegotiate, not the code/path requirement itself).
- `op/O02-controls.md` — the two new controls' wording, so the O2 anchors
  (`E2E-READSET` + superseded-row token + exit) can be pinned to the landed lines.
- `op/O03-isolated-verify.md`, `op/O05-verify.md`, `op/O11-verify-2.md` — observed
  post-patch outputs (r6 replay exit/code/line; r7 summary; selftest count) for
  reconciliation with §2; any deviation is a defect row against claim O.
- `reports/round-35/run-validation.py` — does not exist at write time; §6 is the
  draft spec for its claim-O group.

## Citations

- `reports/round-35/targets.json:233-237` (seat O08 id/role/claim/mission/out);
  `reports/round-35/targets.json` `shared_rules` (out-path fence, filed-byte fence,
  F-C13-1 rule, draft-only corpus/tool edits).
- `reports/round-35/claims.json:40` (claim O text), `:45` (`after_required`),
  `:48` (counting command with `expect: exit 1`), `:51` (thresholds), `:56-62`
  (non-goals: no re-freeze, no filed-round edits).
- `REGIMEN.md:25-50` (per-round contract), `:52-58` (done-when incl.
  `run-validation.py` exits 0 at close).
- `tools/exercise-handoff-e2e.py:89-93` (exit-code table), `:184` (CLAIMS_MAP =
  declared-in-r7), `:1933-1934` (v3 baseline/frozen dir defaults),
  `:3819-3824` (the drifted-member loop; defect site `:3822`), `:3971-3976`
  (Failed/Unevaluatable return), `:4578-4608` (v3 CLI summary/JSON).
- `reports/round-34/handoff/repin.json:19-21` (recorded r6-replay control and the
  KeyError mechanism), `:50` (R34-N1 routed, owner renderer hardening).
- `reports/round-34/run-validation.py:29-70` (runner idioms), `:124-126`
  (declared-deviation precedent), `:197-235` (O-group leg precedent).
- Commands/measurements: B1–B6 in §1 (r6 replay traceback + exit 1; r7 summary
  line + exit 0; selftest header + `grep -c '^  - '` = 40; per-file
  `sha256sum` vs `git show HEAD:<path>` all SAME; `git check-ignore -v` →
  `.gitignore:3 *.log`; `git status --porcelain` → `?? reports/round-35/`);
  `git show HEAD:tools/exercise-handoff-e2e.py | sha256sum` = `34c85f57…`;
  r6 frozen member digest `4b1b9a35…` and r7 successor `d181de28…` read from the
  two `expected.json` `inputs` blocks.
