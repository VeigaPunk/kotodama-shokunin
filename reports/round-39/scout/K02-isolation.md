- Seat: K02 | scout | claim Ca | date 2026-10-19 | baseline dfb0719

# K02 — Isolation scout: O12 mechanics, the r37 c-n-r rows, root-pattern contrast, protocol design inputs

Scope: read-only inputs for Ca01 (protocol author) and Ca02 (replay verifier). No round runner
was executed in-tree or elsewhere; all runner statements below are quoted from filed source bytes.

## 1. The O12 hazard, mechanically

**The absolute root + import-time chdir.** Three filed runners hardcode the live checkout and
chdir to it at module import, before any measurement:

- r34: `ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"` (`reports/round-34/run-validation.py:10`) and module-level `os.chdir(ROOT)` (`:26`).
- r35: same constant (`reports/round-35/run-validation.py:9`) and `os.chdir(ROOT)` (`:36`).
- r36: same shape (`reports/round-36/run-validation.py:8,13`).

Consequence: an invocation launched from any copy (git archive, clone, worktree) re-anchors the
process cwd to the **live checkout** at import; every subsequent relative read
(`f"{ROUND}/claims.json"` etc.) resolves in the live tree, so the copy is never what gets
measured. r34 additionally reads fleet-root inputs by absolute path — `FLEET_REPORT` and
`MANIFEST` at `/home/vgpnk/Projects/shokunin/...` (`reports/round-34/run-validation.py:21-22`) —
which are outside the lane repo entirely (contrast r33's `FLEET_ROOT = ROOT.parent`,
`reports/round-33/run-validation.py:24`).

**Mode-dependent blast radius.**

- `--check`: r34 reaches `--check` only after `measure()` (`reports/round-34/run-validation.py:522-531`; r35 `:492-508`; r36 `:256-264`). Under the chdir escape, `--check` prints a receipt computed from the **live tree** — measurement contamination with no byte write. This is why "«--check» alone does not isolate it" (`reports/round-37/calib/Ca02-r34.md:18`).
- default (publish) mode: r34 measures, then `guard_receipt()` and writes `{ROUND}/validation.json` (`:527-538`; r35 `:492-508`; r36 `:256-270`). Post-chdir, the guard binds to the **live** repo, where the receipt is already committed at HEAD: `receipt_guard` refuses with `RECEIPT-GUARD-COMMITTED` (exit 3) unless the exact env `REFRESH_RECEIPTS=1` is set (`tools/harness/receipt_guard.py:7-8,144-149`) — and with that env it would **overwrite the live filed receipt**.
- The clobber has happened once: r38's scribe records that "a seat that ran them from inside a `git archive` copy still wrote the **live** receipt — the conformance incident recorded at `reports/round-36/scribe/S01-integration-draft.md §0.2` and still open as defect `O12`" (`reports/round-38/scribe/S01-integration-draft.md:418-425`). O12's own disposition names it an extant runner-design hazard, resolution owed to a successor mechanism or runner generation, filed bytes preserved (`reports/round-37/op/O12-gap-fill.md:8-11`; SCORECARD reference at `reports/round-37/op/O12-gap-fill.md:25`).
- `GIT_CEILING_DIRECTORIES` is **not** containment: a probe returned the live checkout root for `git -C <archive> rev-parse --show-toplevel` (`reports/round-37/calib/Ca08-verify.md:25`).

## 2. The four could-not-reproduce rows (r37 ledger)

`reports/round-37/calib/recount-ledger.json` summary: 5 dispositioned-mismatch, 25 match,
**4 could-not-reproduce** (`:451-455`). The four are all round-34 receipt rows:

| id | group | filed command | filed result | citation |
|---|---|---|---|---|
| R37-Ca-05 | C | `python3 reports/round-34/run-validation.py` | `passed=true` | ledger `:60-72`; `reports/round-34/validation.json:2,6-9,25` |
| R37-Ca-06 | D | same | `passed=true` | ledger `:73-85`; `reports/round-34/validation.json:27-30,45` |
| R37-Ca-07 | O | same | `passed=true` | ledger `:86-98`; `reports/round-34/validation.json:47-50,65` |
| R37-Ca-08 | cross | same; CO6 could-not-evaluate | `passed=true` | ledger `:99-111`; `reports/round-34/validation.json:2,67-71,122-129,159` |

All four carry cause "absolute-root chdir makes an unmodified git-archive invocation exit before
measuring (the O12 isolation hazard)" with owner Ca02 and evidence `Ca02-r34.md` (ledger `:70,83,96,108`).
Ca02's durable fragment words it as "an unmodified invocation launched from a `git archive` copy
escapes that copy" (`reports/round-37/calib/Ca02-r34.md:18`). The precise early-exit traceback is
not reconstructible from filed bytes — Ca02's raw archive-session outputs were scratch-only — so
**the exact observed failure signature is `to-verify`**; §1's source-derived mechanics
(escape-then-measure-live, guard-refusal exit 3 on publish) are what the runner bytes support.

**Partial supersession already on file:** Ca08 (independent verifier) reproduced r34 **C and D**
under a `bwrap --unshare-all` namespace — archive bound over the runners' checkout path, sibling
`.ufo` an empty mount, `MANIFEST` masked with `/dev/null`, local git metadata from a scratch-only
bundle, runners unpatched — and recorded "Ca02's `could-not-reproduce` disposition is not sustained
for this row" for C and D (`reports/round-37/calib/Ca08-verify.md:13-14,23`). **O and cross were
not part of that sample** and "remain unverified"; cross additionally cannot reproduce under a
masked fleet (X1 reads the absolute fleet report) (`Ca08-verify.md:27,32`). The r39 successor
ledger must carry this split state: C/D have a namespace reproduction; O needs one; cross needs a
declared fleet-input policy before its result is interpretable.

## 3. Root-pattern contrast (r33 vs r34/r35)

- **r33 relative shape (safe):** `ROOT = Path(__file__).resolve().parents[2]` — derived from the runner's own file location, so any copy measures itself; chdir happens only inside `main()` and to that derived root (`reports/round-33/run-validation.py:23,1454`). Archive replays of r33 measure the archive. Its residual fleet dependency is separate: `REPORT = ".ufo/reports/round-33/kotodama.md"` resolved via `FLEET_ROOT = ROOT.parent` (`:24,45`), which is why r37-Ca-04's plain-archive rerun failed X1 (missing fleet input — a dependency, not a root escape; ledger `:47-59`).
- **r34/r35/r36 absolute shape (the hazard):** §1. r38's ruling for successor runners: copy the r33 relative-ROOT shape, "never the r34/r35 absolute `os.chdir` shape — `S01 §5`, defect `O12`" (`reports/round-38/cross/X01-trades.md:367-369`; `reports/round-38/scribe/S01-integration-draft.md:418-425`). The r39 protocol is the replay-side complement: contain the filed absolute shape without editing it.

## 4. Protocol design inputs for Ca01/Ca02

**Replay target pins (verified this session by command output):**

- r34 close commit: `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (`git log --oneline -- reports/round-34/validation.json` → `4a7aede round-34: admit D/O/C …`). r35 close: `ce103bf5885af00023cdc4a174c17602476cdcf8`; r36 close: `57c8409ba16d9f9e692297198d95e8f2ce5a1937`; r39 baseline HEAD: `dfb0719711204b5943432034bd80c8dc248acddd`.
- The live filed r34 receipt is still the close-state bytes: `git cat-file -p 4a7aede:reports/round-34/validation.json | sha256sum` and `sha256sum reports/round-34/validation.json` both give `ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a`.
- The r34 runner is un-drifted: live file and close-commit blob both hash `be11ff46f1fe399cbedcba956d39134a39e25fcfbb74e4b3dc958f2ab47090f9`, equal to the filed `runner_sha256` (`reports/round-34/validation.json:195-196` per `reports/round-37/calib/Ca02-r34.md:18`). A `--check` stdout comparison against the filed receipt's measurement sections is therefore well-posed.
- Lane working tree at write time: clean except `?? reports/round-39/` (`git status --porcelain`).

**Containment requirement:** the absolute ROOT path must resolve to the snapshot **inside** the
isolation namespace. The only filed precedent that achieves this on unmodified runner source is
Ca08's: `bwrap --unshare-all` with the archive bind-mounted over the runners' checkout path,
probes recorded (namespace: `external_fleet_visible=no manifest_content_bytes=0`; snapshot git:
HEAD `4a7aede…` + zero status rows; post-run: zero status rows, live receipts unchanged, live
`git status --short` showing only the then-untracked round dir) (`reports/round-37/calib/Ca08-verify.md:23,25`). Ca02's redirected-`ROOT` copy was explicitly "not counted as a recount"
(altered source, digest `097bf238…`, `reports/round-37/calib/Ca02-r34.md:20`); Ca04's r36
publish-mode replay used the same altered-source route plus `REFRESH_RECEIPTS=1` inside the copy
(`reports/round-37/calib/Ca04-r36.md:9-22`) — a named-delta precedent, not an unmodified-source one.

**Design decisions Ca01 must codify (inputs, not verdicts):**

1. **Substrate vs the shared rule.** r39 `shared_rules` say "git worktrees at close commits only", but a linked worktree's `.git` file points into the **live** repo's `.git/worktrees/<id>`; bind-mounting only the worktree into a namespace breaks git inside it, and leaving the live `.git` reachable must be declared (read-only) or replaced. Ca08's precedent sidesteps this with a fresh `git archive` extract plus scratch-only bundle alternates and **no live `.git` alternate** (`Ca08-verify.md:23`). Whichever substrate is chosen, the protocol needs the probe set: `git -C <snapshot> rev-parse --show-toplevel` == snapshot root; namespace probe (fleet invisible); snapshot HEAD == close commit; post-run zero status; live receipt digest unchanged before/after.
2. **Mode: `--check` only** against filed runners. Default publish mode on unmodified source is the clobber path (§1); the guard's refusal is the only thing between a copy-run and the live receipt, and `REFRESH_RECEIPTS=1` defeats it. Publish-mode replays belong inside the disposable snapshot only, as the r36 precedent shows.
3. **Unmodified source only** for counted rows: P01's r37 rule — do not run an escaped runner, do not alter the measured source (`reports/round-37/plan/P01-ca-plan.md:19-24` via `reports/round-37/calib/Ca02-r34.md:18`).
4. **Fleet-input policy for the cross row.** X1 needs `FLEET_REPORT` at the absolute fleet path and `MANIFEST` (`reports/round-34/run-validation.py:21-22`); both live outside the lane repo and outside lane-git versioning, so their r34-close-state availability is `to-verify`. Masked mounts make X1 fail by construction (`Ca08-verify.md:23,32`). The protocol must declare per-row whether fleet inputs are bind-mounted read-only or masked, and how either choice is recorded (reproduced vs named-delta).
5. **Environment:** `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` before Python (r39 shared_rules). Note the runners differ: r33 sets these itself (`reports/round-33/run-validation.py:1455-1457`); r34/r35 expect them from the invocation environment (r34 docstring `reports/round-34/run-validation.py:6`).
6. **Never:** in-tree execution (r39 ABSOLUTE); any byte change under `reports/round-34/handoff/declared-in-r7` — the r34 D-leg reads those bytes read-only and their digests are pinned (`reports/round-35/run-validation.py:22-27`); no network, no installs.
7. **Successor-ledger shape for the four rows:** each of R37-Ca-05..08 gets one of `reproduced-under-protocol` (with the replay's receipt diff/identity evidence) or `confirmed-could-not-reproduce` (with owner + reason), plus the Ca08 C/D namespace evidence carried forward rather than discarded (`Ca08-verify.md:13-14`).

## Owed

- Ca01: the protocol document must resolve §4 items 1-4 (substrate/worktree-vs-namespace reconciliation, `--check`-only rule, unmodified-source rule, fleet-input policy) before Ca02 runs anything.
- Ca02: fresh namespace replays for r34 **O** and **cross** remain unverified anywhere in the filed record; the protocol's replay recipe should produce that evidence, not just re-run C/D.
- `to-verify`: the exact early-exit failure signature Ca02 observed on the plain-archive invocation (ledger cause wording vs the measure()-first ordering in runner source; raw scratch outputs not durable).
- `to-verify`: close-state availability of the fleet-root inputs (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-34/kotodama.md`, `MANIFEST.json`) for a cross-row replay.

## Citations

- `reports/round-34/run-validation.py:6,10,21-22,26,522-538` — env expectation, absolute ROOT, absolute fleet paths, import-time chdir, check ordering, guarded publish write.
- `reports/round-35/run-validation.py:9,22-27,36,492-508` — same shape; r7 pin block.
- `reports/round-36/run-validation.py:8,13,256-270` — same shape; measure→guard→write ordering.
- `reports/round-33/run-validation.py:23-24,45,1454-1457` — relative ROOT shape, FLEET_ROOT, self-set env.
- `tools/harness/receipt_guard.py:7-8,144-149` — committed-receipt refusal, exact `REFRESH_RECEIPTS=1` gate.
- `reports/round-37/calib/recount-ledger.json:60-111,451-455` — the four c-n-r rows and summary counts.
- `reports/round-37/calib/Ca02-r34.md:11-20,36,45` — escape finding, not-counted diagnostic, owed state, close-commit citation.
- `reports/round-37/calib/Ca08-verify.md:13-14,23,25,27,32` — namespace method, C/D reproduction, ceiling insufficiency, O/cross gap.
- `reports/round-37/calib/Ca04-r36.md:9-22` — r36 publish-mode replay precedent (redirected ROOT + REFRESH_RECEIPTS=1).
- `reports/round-37/op/O12-gap-fill.md:7-12,21-24` — O12 disposition, carried row, next-touch routing.
- `reports/round-38/cross/X01-trades.md:367-369`; `reports/round-38/scribe/S01-integration-draft.md:418-425` — r38 routing: r33 shape mandatory; O12 still open; conformance-incident pointer (`reports/round-36/scribe/S01-integration-draft.md §0.2`).
- Command output (this session, read-only git): `git log --oneline -3 -- reports/round-34/validation.json` → `4a7aede round-34: admit D/O/C …`; `git rev-parse` pins `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`, `ce103bf5885af00023cdc4a174c17602476cdcf8`, `57c8409ba16d9f9e692297198d95e8f2ce5a1937`, HEAD `dfb0719711204b5943432034bd80c8dc248acddd`; receipt/runner digest equalities listed in §4.
- `reports/round-37/plan/P01-ca-plan.md:19-24` (via `Ca02-r34.md:18`) — unmodified-source rule.
