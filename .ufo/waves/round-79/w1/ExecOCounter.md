# ExecOCounter — round-79 W1: draft accept-o.py for claim O

Seat: ExecOCounter (leaf, wave-1 pre-data build/recon). Lane
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` at base
`44f76d456c1b326a71ffdb381590af825cbf11be` (read-only; no git/jj mutation
anywhere — the only git writes were fixture repositories initialized inside
explicit scratch with a verified `rev-parse --show-toplevel`). Scratch
`/fast/scratch/hyaku/kotodama-r79/ExecOCounter/` was removed after the
receipts below were copied into the stage.

Read first: `/home/vgpnk/.omp/agent/RULES.md`, `.ufo/waves/round-79/CLAIMS-DRAFT.md`,
`corpus/QUALITY.md` (criteria 7–29, especially 11/17/19/23/25/26/28), the
round-77 evidence the guard targets (`.ufo/waves/round-77/w2/ScoutLogPairs.md`:
ten pairs with fabricated recorded `observed_at_base` `"1"` vs actual `"149"`,
pair D11 green at base with stated == observed), and the r76 counter
(`reports/round-76/accept-ca.py`) for the established refusal/selftest/receipt
shapes.

## Files written (all under `.ufo/waves/round-79/w1/stage/ExecOCounter/`)

| file | what |
|---|---|
| `accept-o.py` | the claim-O acceptance counter (1671 lines), self-contained stdlib-only |
| `selftest-o.txt` / `selftest-o.err` | isolated selftest receipt, exit 0, stderr empty |
| `e2e-fixture-clean.txt` | a subprocess (not in-process) grade of the selftest fixture lane at its O-lands: `ACCEPT-O-79: PASS legs=8/8` |
| `schema-to-ExecGuard.md` | the compact behavioural contract for the guard (also summarised below) |
| `apparatus-draft/` | byte-identical freeze-apparatus dump (claims.json O section, fixtures, junk/controls receipts, reference guard) + `README.md` assembly notes for L1 |

## Counter design

`accept-o.py` grades claim O at `--lands` with every constant from
`git show <freeze>:reports/round-79/claims.json` (QUALITY 25(a)/26). Required
`--lands`/`--freeze` (40-hex), explicit `--work`/`$HYAKU_SCRATCH`/`$TMPDIR`
scratch (refuses rather than inventing a temp dir), `--main` default `main`.

Refusals (exit 2, `ACCEPT-O-79: FAIL legs=0/8 (refused: …)`, never a PASS):
non-commit/non-hex revisions; `--lands` equals the frozen base; `--freeze`
not on the lands first-parent chain; frozen claims unreadable; frozen
`legs[]` ≠ the counter's table (LEGCOUNT, order included).
`--lands == --freeze` is **graded**, never passed — the do-nothing control.

Legs (8, frozen list is authoritative):

- **FROZENCFG** — ancestry/first-parent, frozen base ancestor of freeze,
  and byte-identity of claims.json, the counter, the guard and every
  fixture-manifest file between freeze and lands.
- **GREEN** — the counter materializes the guarded-object repo from
  committed fixture bytes in explicit scratch (verified toplevel before any
  relative write), re-derives every stated token, every stated_text-on-line
  (git blob reads) and every observation (the pair's own argv with
  `{base}` → the fixture commit), asserts the committed green ledger is
  truthful (recorded `observed_at_base` == re-derived), then runs the guard
  extracted from `<lands>` bytes: exit 0, the exact verdict line, and a
  per-pair `--emit` that must equal the counter's re-derivation. A stub that
  prints the verdict line without observing fails here.
- **REDOBS / REDSTATED** — the committed mut-observed / mut-stated fixtures
  must be counter-verified genuinely false (recorded ≠ actual; stated ==
  observed) and the guard must reject them exit 1 with `OBS_MISMATCH` /
  `NOT_RED` naming the pair, emit status agreeing with the counter.
- **REDGRAM** — echo/python3 constant-printer fixtures and a `HEAD`-revision
  fixture, each counter-verified present in committed bytes, refused by the
  guard exit 2.
- **SELFTEST** — committed `telemetry/selftest-guard.txt` at lands names the
  lands guard blob sha256; the live `--selftest` re-run (lands bytes,
  explicit scratch) exits 0 and reproduces the receipt's `SELFTEST:` line.
- **RECEIPTS** — junk/controls receipts byte-identical to the freeze blobs
  and carrying the frozen `junk_expect`/`controls_expect` lines (fixture id,
  its commit, the command, the counter's own `LEG FAIL <leg>` line, exit
  code — QUALITY 25(b) shape); the counter's committed selftest receipt
  names a green clean scenario; LOG.md carries the round-79 claim-O row.
- **STAMP** — live receipt headers `stamped == evaluated == measured ==
  <lands>`, lands tree, and this counter's sha256 (also compared against the
  counter blob at lands).

Review-only (QUALITY 11, named in the docstring): the guard's documented
timeout/output caps are not exercised by a fixture; the counter-selftest
receipt check is a shape check (the real receipt is this run's product);
"no arbitrary argv execution" is covered only via the grammar fixtures.

## Guard contract signalled to ExecGuard

In `stage/ExecOCounter/schema-to-ExecGuard.md` (also messaged to ExecGuard-4):
CLI `--ledger --repo --base --work [--emit] [--selftest]`; ledger pair
grammar (argv observe_cmd, `{base}` substituted anywhere in an element,
pinning at `--base` after substitution, read-only git subcommands, no
interpreters/constant printers/shell metacharacters/mutable revisions);
exits 0/1/2 with `LEDGER-GUARD-79: PASS|FAIL (refused: …)` and per-pair
`OBS_MISMATCH`/`NOT_RED` lines; `--emit` strict JSON the counter compares
against its own git-blob re-derivation; `--selftest` exits 0 with a
deterministic `SELFTEST:` line. The counter grades behaviour only — it never
parses the guard's source, so the production guard (ExecGuard) and my
embedded reference fixture are interchangeable at `<lands>` bytes.

## Evidence (observed, not inferred)

- `python3 -B …/accept-o.py --selftest` in isolated scratch
  (`HYAKU_SCRATCH=/fast/scratch/hyaku/kotodama-r79/ExecOCounter/…`):
  **exit 0, `SELFTEST: 65/65 scenarios ok`**, stderr 0 bytes
  (`stage/ExecOCounter/selftest-o.txt`). Receipt lines 1–2 are the
  do-nothing (`exit=1 … SELFTEST=FAIL RECEIPTS=FAIL`) and clean
  (`exit=0`, all PASS) scenarios — the QUALITY 23-addendum green-first shape.
- Scenario coverage: do-nothing; clean; four graded junk landings
  (stub-guard→FROZENCFG, lying green fixture→GREEN, post-freeze fixture
  tamper→FROZENCFG, forged guard-selftest receipt→SELFTEST); a junk receipt
  forged to green→RECEIPTS; a verdict-printing stub guard swapped into the
  graded tree→FROZENCFG; six controls (do-nothing, no-scratch, legcount,
  legorder, lands-eq-base, freeze-off-first-parent) all refused/red as
  expected.
- Subprocess end-to-end grade of the fixture lane (not in-process):
  `ACCEPT-O-79: PASS legs=8/8` with the full QUALITY 17/19 header grammar
  (`stage/ExecOCounter/e2e-fixture-clean.txt`).
- QUALITY 25 one-liner over the counter source exits 0 (`--freeze` present,
  `"show", "%s:%s"` git-show pattern present, no graded-root `CLAIMS` join).
- Counter sha256: `588e448406a22ea3f6ad2e42bde2d683f990544beacdf320a23c7384a6eae844`
  (fixture ledgers carry exactly the contract's example fields — top-level
  `round/claim/base/pairs`, per-pair the ten example keys — matching the
  production guard's strict key set; selftest re-run 65/65 after the strip).
- Tool installs: none (python 3.14.8 and git 2.56.0 already present; no
  pacman, no host changes).

## Peer alignment (ExecGuard-4 reply)

ExecGuard reports contract satisfaction (selftest 24/24; real-base check at
`211f952…`: recorded `'1'` → `OBS_MISMATCH` actual `'149'` exit 1, corrected
→ PASS with matching `--emit`). Their flagged choices were checked against my
fixtures: (1) `STATED_MISMATCH` on stated_text≠line — all my fixture
stated_texts equal their blob lines, no divergence; (2) stated_parse
no-match = exit-2 — all fixture parses match; (3) disposition/expected_after/
rederive unexecuted — my legs do not grade them; (4) `re.M|re.S` parse flags
— fixture observations are single-line, token-identical either way; (5) emit
on refusals — my REDGRAM leg ignores emit. One real divergence found and
fixed on my side: my fixture ledgers carried a `why` pair key and a top-level
`status` key outside the strict set — stripped, fixtures regenerated,
selftest re-run 65/65, e2e still `PASS legs=8/8`.

**Cross-implementation close-out (final):** ExecGuard's production guard
(`stage/ExecGuard/tools/ledger-token-guard.py`, sha256
`ccb4ef5e37175b25bf07568f05e7c5dd8e1fb096ea2f961364548a8c10d2a986`) was
swapped into the counter's own selftest harness in place of the reference
fixture: **65/65 scenarios ok, exit 0, stderr 0 bytes** — the clean landing
grades `ACCEPT-O-79: PASS legs=8/8` and every junk/control case runs red on
the production bytes (`stage/ExecOCounter/cross-selftest-production-guard.txt`).

## Risks / notes for L1

1. `apparatus-draft/tools/ledger-token-guard.py` is the **reference fixture**;
   L1 must substitute ExecGuard's production guard, then regenerate
   `selftest-guard.txt` (same `# guard sha256:` header) and the junk/controls
   receipts against the junk trees with the production guard in place
   (README §1–3).
2. `apparatus-draft/reports/round-79/claims.json` carries the synthetic
   fixture-base hash; regenerate with base `44f76d456c1b…` and keep legs /
   manifest / expectations byte-stable (README §4).
3. The counter-selftest receipt committed at the production O-lands is my
   staged `selftest-o.txt` (the real run); the RECEIPTS check on it is a
   shape check — falsify-wave seats should attack the junk/controls
   receipts instead, which carry machine-checked expectations.
4. Do-nothing at the real freeze is red via SELFTEST + RECEIPTS (receipts and
   the LOG row land only at the O-lands); FROZENCFG/GREEN legitimately pass
   at do-nothing because the freeze carries the apparatus — the verdict can
   never be PASS.
