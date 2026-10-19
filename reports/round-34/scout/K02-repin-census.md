- Seat: K02 | scout | claim D | date 2026-10-19 | baseline da68a6d

# K02 — Re-pin cascade census: every surface that pins `reports/round-30/handoff/declared-in-r6`

**Scope of the sweep.** Three orthogonal greps over the working tree (plus, read-only, the
fleet root one level up), because a pin can name the pair by *path*, by *packet digest*, or by
the baseline's *own* digest. All three were run; a surface that used a fourth encoding would be
missed by all three, so the coverage claim is stated as "these three encodings", not "any pin".

| grep | pattern | result |
|---|---|---|
| path | `declared-in-r6` | 4 live/actionable lines in 3 files — `tools/exercise-handoff-e2e.py:1933,1934`, `LOG.md:3428`, `SCORECARD.md:400` (the tree-wide grep's remaining hits are the r6 pair itself, its self-citation at `packet.md:295`, this round's own declaration files, filed round-33 fragment prose, and ephemeral `.scratch` copies — all classified in §C/§D/§F) |
| packet digest | `6ced88ad` | no hits under `tools/`, `corpus/`, `examples/`, `*.md` (other than the r6 pair + filed round-3x receipts) |
| baseline self-digest | `714b41fc` | exactly 1 file in the tree: r6's own `expected.json` — nothing external pins r6 by its own digest |

**Headline.** The cascade is **2 mutable lines**, not a tree-wide sweep. Only
`tools/exercise-handoff-e2e.py:1933-1934` *selects which generation the v3 profile validates
against*; every other surface either (a) consumes those same two constants inside the same file,
(b) is a filed byte that stays frozen and gets a *new* supersession row, or (c) does not read the
pair at all. The integrator's D10 diff is therefore small and reviewable; the risk is not breadth,
it is the **must-move-together coupling** proved in §B.

Pin-kind taxonomy used below:
`PM` mutable default (must change) · `PC` consumer of a PM inside the same tool (moves implicitly) ·
`PR` filed record (immutable; re-pointed as a new row, never edited) ·
`PS` prose / state-of-record (append-only ledger gets a new row) ·
`PN` non-pin (names or copies the pair, reads nothing from it).

---

## A. PM — the only mutable pins

| # | path:line | live text | why it is the pin |
|---|---|---|---|
| A1 | `tools/exercise-handoff-e2e.py:1933` | `V3_BASELINE_DEFAULT = "reports/round-30/handoff/declared-in-r6/expected.json"` | the v3 profile's baseline default: `v3_exercise(root=ROOT, baseline_rel=V3_BASELINE_DEFAULT)` (`:3806`) and the CLI fallback `args.baseline or baseline_default` (`:4577`) both read it |
| A2 | `tools/exercise-handoff-e2e.py:1934` | `V3_FROZEN_DIR_DEFAULT = "reports/round-30/handoff/declared-in-r6"` | the freeze target dir: `v3_freeze(target, target / V3_FROZEN_DIR_DEFAULT)` (`:4149`) and the selftest fixture baseline path (`:4172`) |

After the move the pair reads `reports/round-34/handoff/declared-in-r7` in both slots. Nothing
else in `tools/` carries the string — `grep -rn "declared-in-r6\|round-30/handoff" --include=*.py .`
returns only `tools/exercise-handoff-e2e.py:1933,1934` in the live tree.

**Shape precedent for the draft (D10).** The v1 profile keeps the identical two-constant shape at
`tools/exercise-handoff-e2e.py:460-461` (`V1_BASELINE_DEFAULT = "reports/round-11/handoff/expected.json"`,
`V1_FROZEN_DIR_DEFAULT = "reports/round-11/handoff"`) and is *deliberately not re-pointed* —
the module docstring says so at `:22-23` ("The default stays v1 so the filed round-11 path is not
re-pointed"). The r7 move is therefore the **third** application of an established pattern
(`v1`→round-11 stays; `v3` r27→r28→r6→r7 moves), not a new mechanism.

## B. PC — consumers of A1/A2 inside the same file (move together; no third literal exists)

| # | path:line | text (live) | coupling |
|---|---|---|---|
| B1 | `tools/exercise-handoff-e2e.py:3185` | `f"baseline in \`{V3_BASELINE_DEFAULT}\`, whose run log records the verdict of the run it froze"` | the **rendered packet body** names its own baseline path. Proof of effect: r6's `packet.md:295` carries exactly this sentence with `reports/round-30/handoff/declared-in-r6/expected.json`, and it is the **only** self-citation of the r6 dir inside the whole r6 pair (`grep -n "declared-in-r6\|round-30/handoff"` over packet/twin/expected/freeze/run.log → `packet.md:295` alone). A r7 render therefore self-names `declared-in-r7` with no hand edit — the packet-prose consistency leg of claim D rides on this line, not on D03/D04 |
| B2 | `tools/exercise-handoff-e2e.py:3806` | `def v3_exercise(root=ROOT, baseline_rel=V3_BASELINE_DEFAULT):` | signature default |
| B3 | `tools/exercise-handoff-e2e.py:4149` | `baseline, _, _, _ = v3_freeze(target, target / V3_FROZEN_DIR_DEFAULT)` | selftest fixture freeze target |
| B4 | `tools/exercise-handoff-e2e.py:4172` | `baseline_rel = V3_FROZEN_DIR_DEFAULT + "/expected.json"` | selftest baseline path inside the frozen copy |
| B5 | `tools/exercise-handoff-e2e.py:4561` | `baseline_default, frozen_default = V3_BASELINE_DEFAULT, V3_FROZEN_DIR_DEFAULT` | CLI binding; consumed at `:4577` and in the `--freeze` branch |
| B6 | `tools/exercise-handoff-e2e.py:4488` | `parser.add_argument("--baseline", metavar="PATH", help="baseline override (profile default otherwise)")` | **not** a pin — but it is the documented escape hatch that lets a re-run bind r6 explicitly after the move (`SKILL.md:448` documents the same `<authorized-successor>` pattern) |
| B7 | `tools/exercise-handoff-e2e.py:3526-3533` | hardcoded `OQ-V3-05` literal: `"D4's inherited and own holds stay open: twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts — kotodama; blocking for …"` | **not a path pin — a content literal in the same shared file.** The r6 packet's stale OQ text is *not* read from `reports/round-20/handoff/claims-map.md` (that file supplies only the twelve D4 claim rows, `:2290-2303`); it is this literal, so closing OQ-V3-05 needs a **third** renderer edit beyond A1/A2. Bounds §H1: the *pin cascade* is two blocks, the *round's shared-file diff* is not. Independently found by K01 (`scout/K01-packet-state.md:241-243`) and cross-checked here against the source |

### B-coupling proof: A1 and A2 must move together (falsifiable)

`v3_load_baseline` resolves a relative baseline against the run root:
`path = Path(baseline_rel) if Path(baseline_rel).is_absolute() else Path(root) / baseline_rel`
(`tools/exercise-handoff-e2e.py:3771-3772`). The selftest then re-runs the CLI as a subprocess
with `--root <frozen_root>` and **no `--baseline`** (`:4183-4189`), so it falls back to
`baseline_default` = A1 resolved against the *fixture* root, and the fixture root only contains
that baseline because B3 wrote it at `<frozen_root>/<A2>` moments earlier (`v3_freezed_copy`
`:4146-4150`).

- Move **A1 only** → the selftest subprocess looks for `<frozen_root>/reports/round-34/handoff/declared-in-r7/expected.json` while B3 still froze into `…/declared-in-r6/` → the isolation leg must go red.
- Move **A2 only** → the unfrozen default (`…/declared-in-r6/expected.json`) is still what the CLI reads, while the freeze writes r7 → the new pair is never exercised by the default chain (`# after_required` unmet).
- Move **both** → self-consistent; the temp fixture paths are synthetic and no fixture file needs to pre-exist under the new name, because the fixture is built by copying `V3_READ_SET` (`v3_build_fixture_root`, `:4130-4143`), which contains no handoff-baseline entry.

This is the check D19/D17 can run against the drafted diff (before-blocks must match live bytes;
after-blocks must change *both* lines). Not executed here — I do not edit shared files.

## C. PR — filed records that pin the pair or its digests (immutable; supersession rows only)

`packet_sha256 = 6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` is
byte-verified at census time: `sha256sum …/declared-in-r6/packet.md` → `6ced88ad009f1cfc…`
(matches `freeze.txt:2` and `expected.json.packet_sha256`). Companion digests:
`expected.json` = `ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0`,
`freeze.txt` = `6fe70c0c2b3a03ee82181a4906dc9670f73424c54efddec8fc632d213cca5d59`,
self-digest field `baseline_digest = 714b41fc5859…` (no external reader — see §E).

| # | path | pinned field | recorded value |
|---|---|---|---|
| C1 | `reports/round-30/handoff/declared-in-r6/{expected.json,freeze.txt,run.log}` | `packet_sha256`, `twin_sha256`, `baseline_digest`, `inputs{}` (58 files), `links{}`, `uncertainty{}`, `cross_refs.gate_*` | the baseline generation itself |
| C2 | `reports/round-30/validation.json` | `/claims/O/measurement/regressions[25]/stdout` | `handoff-v3: exit=0 … packet_sha256=6ced88ad009f1cfc…` |
| C3 | `reports/round-31/validation.json` | `/claims/O/measurement/recorded_reruns[33]/stdout` | same summary line |
| C4 | `reports/round-32/validation.json` | `/claims/O/measurement/recorded_reruns[33]/stdout` | same summary line |
| C5 | `reports/round-31/sweep/sweep-receipt.json` | `/rows[33]/summary_line` | same summary line |
| C6 | `reports/round-32/sweep/sweep-receipt.json`, `sweep/receipt-O06.json`, `receipt-O07.json`, `receipt-O08.json` | `/rows[33]/summary_line` | same summary line (4 files) |
| C7 | `reports/round-32/sweep-audit-O09.json`, `sweep-audit-O10.json` | `/results[33]/stdout_head` | same summary line (2 files) |
| C8 | `reports/round-32/final-sweep.md:89-90`, `sweep-audit-O09O10.md:98-99`, `dossier-d11-shonen-boxes.md:111` | stdout digests `b4c57165a3bf0545…`, `49110716cba565e0…` | the sweep table rows |
| C9 | `reports/round-32/sweep/commands.txt:44-45` | the re-run command lines | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` and `… --selftest --quiet` — **no `--baseline`**, i.e. the default-consuming manifest |
| C10 | `reports/round-27/validation.json` | `/claims/O/measurement/v3_baseline_default.path`, `/…/v3_replay.default_baseline` | `reports/round-27/pinsweep/v3-baseline-r27/expected.json` |
| C11 | `reports/round-28/validation.json` | `/claims/O/measurement/v3_baseline_default.path`, `/…/v3_replay.default_baseline` | `reports/round-28/pinsweep/v3-baseline-r28/expected.json` |
| C12 | `reports/round-30/handoff/declared-in-r6/packet.md:295` | the packet's own gate bullet | names `reports/round-30/handoff/declared-in-r6/expected.json` (self-citation; regenerated by B1 in r7) |
| C13 | `reports/round-33/adj/A02-handoff.md:19-20,94,153-154` (filed) | the A02-H1 finding + the boundary determination | names the r6 default as the *current* pair and files the staleness obligation this round closes |

### C-filed-readers: two filed runners read the default **live** (reproducibility note, not a bug)

| # | path:line | mechanism | consequence of the move |
|---|---|---|---|
| C14 | `reports/round-27/run-validation.py:1388-1389` | `re.search(r'V3_BASELINE_DEFAULT\s*=\s*"([^"]+)"', tool_text)` over the **live** tool source | a re-run of the filed r27 runner records `v3_baseline_default.path = …/declared-in-r7/expected.json`. Verdict text unchanged: the leg fails only when `v3_run.get("exit") != 0` and no successor replays green (`:1441`) |
| C15 | `reports/round-28/run-validation.py:1348-1349` | same regex | same: reading changes to r7; the failure branch (`:1408-1410`) is armed only by a **red** default replay. `V3_BASELINE_FALLBACK` (`:110`) is used only if the regex misses |
| C16 | `reports/round-27/run-validation.py:1431`, `reports/round-28/run-validation.py:1398` | successor replays pass an explicit `--baseline <row>` | **unaffected** by the default move (they iterate the round's own `**/expected.json` rows) |

**Honest consequence for the integrator.** After the move, an isolated re-run of C14/C15 produces a
*different reading* in a *filed* field name than the filed receipt shows, while every verdict stays
green (given a green r7 replay). This is the "verdict-stable, reading-changed" class: the filed
receipts are immutable and must **not** be rewritten; the round-34 record must state the re-run
reading it produced, and any validator leg that compares filed readings to live readings must be
written knowingly. `reports/round-27/validation.json` already demonstrates the pattern in the other
direction (it filed a `v3_baseline` **drift** reading, `declared_packet_sha256` ≠
`live_packet_sha256`, and the round was admitted because the replay itself was green).

## D. PS — prose / state-of-record (new rows; never edits)

| # | path:line | text | treatment |
|---|---|---|---|
| D1 | `LOG.md:3428` (round-30 admission entry) | "the v3 default chain re-pointed to declared-in-r6" | append-only: the round-34 LOG entry records the r7 re-point as a new entry |
| D2 | `SCORECARD.md:400` (round-30 operability row) | "the v3 default chain re-pointed to declared-in-r6 after diagnosing the profile-row baseline drift" | append-only: new row |
| D3 | `../.ufo/reports/round-30/kotodama.md:14-18` (fleet root, outside this repo) | same sentence, fleet-report copy | outside the lane repo — read-only here; new fleet report for round 34 |
| D4 | `reports/round-30/handoff/declared-in-r6/packet.md:295` | see C12 | filed byte; regenerated in r7 via B1 |

## E. PN — searched, zero pins (negative evidence; these are the surfaces the cascade does *not* touch)

| # | surface searched | result | command |
|---|---|---|---|
| E1 | `AGENTS.md` | 0 hits for the pair, digests, or "declared-in"; only unrelated "worker handoff" prose at `:19` | `grep -n "round-30\|declared-in\|handoff" AGENTS.md` |
| E2 | `SKILL.md` | `:448` documents `tools/exercise-handoff-e2e.py` and the `--baseline <authorized-successor>/expected.json` escape hatch but names **no** generation path; `:397` is a `reports/round-30/fixes/x63-f2.md` prose reference, unrelated to the handoff pair; `:216` is the freeze-artifact *naming* law (a non-battery freeze receipt is not named `expected.json` under a battery root) — a constraint on where r7's freeze artifacts may live, not a pin | `grep -n "round-30\|declared-in\|v3 default chain\|exercise-handoff-e2e" SKILL.md` |
| E3 | `corpus/**` | 0 hits | tree-wide greps §Scope |
| E4 | `examples/**` | 0 hits for the pair/digests; the `reports/round-30/fixes/qreg-dangles.md` references in `culture-d4/**` are D4 *evidence* refs, not handoff pins | tree-wide greps §Scope |
| E5 | `tools/gates/**` | no baseline-path discovery of the handoff pairs; `handoff-packet-check.py` takes the packet as a positional argument (`:868`) with only `--selftest` besides — so the **gate does not pin which generation it is handed**, which is exactly why r6 can be "shape-green but semantically stale" | `grep -n "add_argument\|default=" tools/gates/handoff-packet-check.py` |
| E6 | `tools/harness/*.py` | `packet_links.py:737,744` take `--repo-root`/`--packet` explicitly (defaults: cwd, verify mode); `packet_uncertainty.py:42` default is `DEFAULT_MIN_BASIS_LEN = 40`. No generation default | `grep -rn "default\|DEFAULT" tools/harness/packet_links.py tools/harness/packet_uncertainty.py` |
| E7 | `tools/check-gate-battery.py` | `GATE_NAMES` (`:117-132`) lists `handoff-packet-check.py` as a **gate name** only; no handoff-pair baseline discovery | `grep -n "handoff\|declared-in\|NAME" tools/check-gate-battery.py` |
| E8 | `tools/replay-frozen.py` | 0 hits | `grep -n "handoff\|declared-in\|round-30" tools/replay-frozen.py` |
| E9 | `tools/gates/frozen/**` | only `tools/gates/frozen/round-18/freeze-receipt.json` exists; its rows are D4 gates/inputs (typed-labels, d4-assembly, …), no handoff pair | `find tools/gates -maxdepth 3 -name 'expected.json' -o -name 'freeze*'` |
| E10 | `tools/gates/expected/**` | 5 dirs: `costume-era-consistency-gate`, `d4-assembly-check-gate`, `d4-typed-labels-check-gate`, `phonology-sanity-gate`, `register-law-gate` — **no handoff dir** | `ls tools/gates/expected/` |
| E11 | fleet `../MANIFEST.json` (256 482 B) and `.scratch/MANIFEST.json` | `grep -c "declared-in-r6\|6ced88ad"` → **0** and **0**. (No `MANIFEST.json` exists at this repo's root; `find . -maxdepth 3 -name MANIFEST.json` → `./.scratch/MANIFEST.json` only) | `grep -c … ../MANIFEST.json .scratch/MANIFEST.json` |
| E12 | `reports/round-33/validation.json` | 0 hits for `declared-in` / `6ced88ad` — round 33's receipt does **not** pin the pair by digest | python walk of the JSON |

## F. PN — duplicates excluded as non-durable (named so nobody mistakes them for pins)

`.scratch/r30-run/**`, `.scratch/r31-run/**`, `.scratch/c05-iso/**` are isolated `git archive`
copies of the tool + the r6 pair from earlier rounds' validations; each contains the *pre-move*
constants at `tools/exercise-handoff-e2e.py:1933-1934`. They are ephemeral scratch, not durable
evidence, and must not be cited as pins or as a reproduction path. Also excluded: filed round-33
fragment prose (`adj/A02-handoff.md`, `A11-verify-a01-a03.md:88-89`, `A10-receipt.md`,
`K04-method-scout.md`) which *names* the r6 default as the then-current pair — record-class (§C13),
and `reports/round-31/scope.md:55`, which names r6's `run.log` as an ignored-path watch row.

## G. Pin-chain history (empirical, from filed receipts + live bytes — the "new row" to land)

| generation | default baseline | evidence |
|---|---|---|
| round-11 (v1 only) | `reports/round-11/handoff/expected.json` | `tools/exercise-handoff-e2e.py:460`; docstring `:22-23` |
| `declared-in-r2` (round-22, renderer 3.1.1) | documented in the module docstring | `tools/exercise-handoff-e2e.py:38-40` ("its current baseline is under `reports/round-22/handoff/declared-in-r2/`") |
| `declared-in-r5` (round-26) | — | filed enumeration `reports/round-33/adj/A11-verify-a01-a03.md:89` (six `declared-in*` dirs) |
| `v3-baseline-r27` | `reports/round-27/pinsweep/v3-baseline-r27/expected.json` | `reports/round-27/validation.json` §C10 |
| `v3-baseline-r28` | `reports/round-28/pinsweep/v3-baseline-r28/expected.json` | `reports/round-28/validation.json` §C11 |
| `declared-in-r6` (round-30) | `reports/round-30/handoff/declared-in-r6/expected.json` | `tools/exercise-handoff-e2e.py:1933-1934`; `SCORECARD.md:400`; `LOG.md:3428` |
| `declared-in-r7` (this round) | `reports/round-34/handoff/declared-in-r7/expected.json` | **to-verify** — the directory does not exist at census time (`ls reports/round-34/` → `claims.json targets.json telemetry`; the D-seats build it this round) |

The move is authorized upstream, not invented here: the obligation is a filed finding —
`reports/round-33/adj/A02-handoff.md:94` ("The current default pair is shape-green and semantically
stale") and `reports/round-29/defects/routed.md:113-115` ("Fresh v3 renderer claim drift — …
Refresh the claims-map source and renderer from measured projection fields"). Both filed rows name
**no** r6 path or digest, so they are not themselves pins — they are the debt this round pays.

## H. Handoff notes for D10 / P01 / the integrator

1. **Draft the *pin cascade* as exactly two before→after blocks** (§A). Every other live surface is §B and inherits the change; no third literal pins a *path* (verified by `--include=*.py` grep). Scope note: this bounds the re-pin cascade only — the round's shared-file diff is **not** two lines, because B7 (the hardcoded `OQ-V3-05` literal at `:3526-3533`) needs its own before/after block for claim D's number-rewrite leg, and that one belongs to D03/D04.
2. **Move both lines or neither** (§B-coupling). State in the after-block that the selftest fixture path at `:4149`/`:4172` follows automatically and that `v3_build_fixture_root` needs no new fixture file.
3. **Do not touch** C1–C16: filed bytes stay frozen. Reproduce the r6 reading after the move with the explicit escape hatch `--baseline reports/round-30/handoff/declared-in-r6/expected.json` (§B6, `SKILL.md:448`) if a verification leg needs it.
4. **New rows owed**: `LOG.md` (round-34 entry), `SCORECARD.md` (round-34 depth row), the fleet report for round 34, and — if the round-34 validator re-runs the default chain — a leg that records which generation the default resolved to (`v3_replay.default_baseline`), so the "verdict-stable, reading-changed" class in §C is filed rather than discovered later.
5. **Forward-looking surface (to-verify).** `reports/round-34/run-validation.py` does not exist yet (S04 drafts its leg spec). If any leg of it hard-codes the r6 path, it becomes a pin the moment it lands — that file is the one place this census cannot check.

## Owed

none — this census is self-contained: no other seat's fragment was a precondition. One
cross-check was performed *after* my own sweep completed, and it improved the result rather than
being owed to it: `reports/round-34/scout/K01-packet-state.md:29-32,241-243` independently flagged
the hardcoded `OQ-V3-05` literal, which I verified at `tools/exercise-handoff-e2e.py:3526-3533` and
recorded as row B7 + the §H1 scope note. K01's two renderer-default cross-references (`:3185`
prose interpolation, `:4561` binding) match my §B1/§B5 line-for-line. Downstream: P01/D10 consume
§A/§B/§G; D19 verifies §B-coupling against the drafted diff; R02 re-runs the sweep independently
(the three encodings in §Scope are the ones to repeat). One item is explicitly forward-looking
rather than owed: §H5.

## Citations

Commands run (all from `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `grep -n "quarantine handles\|thirteen unresolved rank items\|hold-or-fail" tools/exercise-handoff-e2e.py` → the B7 hits at `:951,957,1154,1155,3132,3133,3144,3145,3527`; `sed -n '3505,3535p' …` → the OQ-V3-05 literal; `grep -n "CLAIMS_MAP\|claims-map" …` → `:184,1957,2290-2303` (claims-map supplies D4 claim rows only)
- `git log --oneline -3` → `da68a6d round-33: admit O/C/A …`; `git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`
- `grep -rn "declared-in-r6" .` (tree-wide, path encoding) and `grep -rn "declared-in-r6\|round-30/handoff" tools/ .ufo/ *.md corpus/ examples/ MANIFEST.json`
- `grep -rln "6ced88ad" . --exclude-dir=.git`; `grep -rln "714b41fc" . --exclude-dir=.git --exclude-dir=.scratch`
- `grep -rn "declared-in-r6\|6ced88ad" --include=*.py .`; `grep -rn '\-\-baseline' reports/round-*/run-validation.py` (grep printed "stray \ before -" and returned its rows anyway)
- `grep -c "declared-in-r6\|6ced88ad" ../MANIFEST.json .scratch/MANIFEST.json` → `0`, `0`; `find . -maxdepth 3 -name 'MANIFEST.json' -not -path './.git/*'` → `./.scratch/MANIFEST.json`
- `sha256sum reports/round-30/handoff/declared-in-r6/{expected.json,freeze.txt,packet.md}` → `ea1e2927…`, `6fe70c0c…`, `6ced88ad…`
- python `json` walkers over `reports/round-{27,28,30,31,32,33}/validation.json`, `reports/round-{31,32}/sweep/*.json`, `reports/round-32/sweep-audit-O09.json`, `sweep-audit-O10.json` for the paths/digests in §C
- `ls reports/round-34/` → `claims.json targets.json telemetry`; `ls -la reports/round-30/handoff/declared-in-r6/`
- `sed -n` at `30,45p`, `1,60p`, `1900,1975p`, `3178,3192p`, `3800,3812p`, `4100,4148p`, `4140,4180p`, `4180,4215p`, `4550,4575p`, `4575,4610p` of `tools/exercise-handoff-e2e.py`; `grep -n "V3_BASELINE_DEFAULT\|V3_FROZEN_DIR_DEFAULT\|def v3_build_fixture_root\|def v3_load_baseline\|def v3_freeze" tools/exercise-handoff-e2e.py`; `python3 -c "import json; d=json.load(open('reports/round-30/handoff/declared-in-r6/expected.json')); print(len(d['inputs']))"` → `58`; `nl -ba …/freeze.txt`

Paths relied on:

- `tools/exercise-handoff-e2e.py:16,22-23,38-40,460-461,4488,4561,4577,3185,3764-3792,3806,3978-3988,4073-4084,4146-4150,4153-4190,4444`
- `reports/round-30/handoff/declared-in-r6/{packet.md:295,expected.json,freeze.txt:1-8,run.log}`
- `reports/round-{27,28,30,31,32,33}/validation.json` (`/claims/O/measurement/…` as cited)
- `reports/round-{27,28}/run-validation.py:110,1348-1349,1388-1389,1398,1408-1410,1431,1441`
- `reports/round-32/{final-sweep.md:89-90,sweep/commands.txt:44-45,sweep-audit-O09O10.md:98-99,dossier-d11-shonen-boxes.md:111}`
- `reports/round-33/{adj/A02-handoff.md:13,19-21,94,153-154,adj/A11-verify-a01-a03.md:88-89,adj/A10-receipt.md:50}`
- `reports/round-34/scout/K01-packet-state.md:19-32,241-243` (cross-check performed after my own sweep; agreed on `:3185`/`:4561`, added the B7 literal)
- `reports/round-29/defects/routed.md:113-115`; `reports/round-31/scope.md:55`
- `LOG.md:3428`; `SCORECARD.md:400`; `SKILL.md:216,397,448`; `AGENTS.md:19`
- `tools/gates/handoff-packet-check.py:868-869`; `tools/check-gate-battery.py:117-132`; `tools/harness/packet_links.py:737,744`; `tools/harness/packet_uncertainty.py:42`; `tools/gates/frozen/round-18/freeze-receipt.json`
- `/home/vgpnk/Projects/shokunin/.ufo/reports/round-30/kotodama.md:14-18`; `/home/vgpnk/Projects/shokunin/MANIFEST.json` (read-only, outside the lane repo)
