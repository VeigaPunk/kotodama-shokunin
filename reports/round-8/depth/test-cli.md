# R8-D10 — CLI surface tests: `tools/d2-typed-labels.py`

- round 8 (loop 1, build 1 of 4) · date 2026-10-17 · shard R8-D10
  (`reports/round-8/targets.json` R8-D06..D11 test shards; claim D,
  `reports/round-8/claims.json`)
- revision under test: `tools/d2-typed-labels.py` sha256
  `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`
  (2915 lines), working tree at HEAD `cf338a713060f274269cdacb18cdc0085bb06aeb`
  (2026-10-17 17:36 -03:00). The tool is D02's uncommitted deliverable; this
  doc binds to that exact hash and is superseded by any later revision.
- test environment: Python 3.14.7, Linux; commands run 2026-10-17
  17:33–17:36 -03:00. All runs in an isolated copy of the needed tree
  (`/home/vgpnk/.cache/r8d10/repo`: the tool, `costume-era-consistency-gate.py`,
  `packet.d2.yml` sha256 `8da90b0788f86fd1…`, and components 05/09/11/12).
  `/tmp` was inode-exhausted during this shard (§6), so the scratch tree lives
  under `$HOME/.cache`; no lane file, gate, component or packet was edited.
- scope: CLI surface only — argument handling, input-file errors, exit codes,
  output modes. Domain correctness, determinism and the selftest's control
  matrix are other shards' claims (R8-D06..D13).

## 1. Assigned cases — verdicts

| assigned case | command | exit | receipt (stdout/stderr first line) |
|---|---|---|---|
| `--help` | `python3 tools/d2-typed-labels.py --help` | **0** | `usage: d2-typed-labels.py [-h] [--packet PACKET] [--json] [--emit PATH] [--check [PATH]] [--selftest]` |
| missing args (value) | `… --packet` | **2** | stderr `d2-typed-labels.py: error: argument --packet: expected one argument` |
| missing args (unknown flag) | `… --bogus` | **2** | stderr `d2-typed-labels.py: error: unrecognized arguments: --bogus` |
| invalid JSON input | `… --packet bad-json.json` (`{"a": `) | **2** | `FINDING D2L-DATA: [fail] … — content '{"a":' is not a mapping line` |
| wrong root key (JSON) | `… --packet wrong-root-key.json` (`{"wrong_root": …}`) | **2** | `FINDING D2L-DATA: [fail] … — content '{"wrong_root": {"x": 1}}' is not a mapping line` |
| wrong root key (YAML) | `… --packet wrong-root-key.yml` (`wrong_root:\n  x: 1`) | **2** | stderr `d2-typed-labels error: packet.eras: expected a non-empty list of era tags` |
| wrong root key (real packet, `eras:` renamed `erasX:`) | `… --packet renamed-root.yml` | **2** | stderr `d2-typed-labels error: packet.eras: expected a non-empty list of era tags` |

All seven assigned-case runs produced stable diagnostics and no traceback
(sweep in §4).

## 2. Surface as shipped (verbatim, exit 0)

`python3 tools/d2-typed-labels.py --help` (2026-10-17, tool hash `0da0015f…`):

```text
usage: d2-typed-labels.py [-h] [--packet PACKET] [--json] [--emit PATH]
                          [--check [PATH]] [--selftest]

d2-typed-labels — typed translated-label/native-form handling for D2 (R8-D02).

options:
  -h, --help            show this help message and exit
  --packet PACKET       packet to read (default: <repo>/examples/culture-d2/packet.d2.yml)
  --json                print one JSON document instead of the report
  --emit PATH           write the deterministic projection to PATH
  --check [PATH]        byte-compare the projection; writes nothing
  --selftest, --self-test
                        fixture + control matrix
```

- `-h` is identical to `--help`, exit 0 (argparse default).
- No positional arguments exist; every mode is a flag, so "missing args" can
  only be a missing option value or an unknown/extra token (§1, §4).
- Mode precedence (observed, **not documented in `--help`**): `--check` wins
  over `--json`; `--json` wins over `--emit` (`--json --emit X` printed JSON
  and `X` was not created — `test -f` returned "no"); otherwise the default
  mode prints the human report.
- `--selftest` is exclusive in effect but not enforced by argparse: extra
  tokens after it exit 2 as unrecognized arguments.

## 3. Exit codes (documented contract, as observed)

| code | meaning in this tool | receipts |
|---|---|---|
| 0 | clean: no HOLD/FAIL findings; `--check` byte-identical; `--selftest` all controls pass | `--check <fresh emit>` → 0 `…: byte-identical deterministic projection`; `--selftest` (TMPDIR writable) → 0, `39/39 checks passed` |
| 1 | findings emitted (report/`--json`/`--emit` modes), or `--check` byte-drift | default mode → 1 with `FINDING D2L-FORM-UNRESOLVED …`; `--check` with missing target → 1, stderr `…typed-labels.d2.yml differs from the deterministic projection` |
| 2 | usage error (argparse) **or** could-not-evaluate: unreadable/non-UTF-8/unparsable packet, missing required root keys, `--emit`/`--check` path errors | `--bogus` → 2; `--packet <missing>` → 2 `D2L-DATA`; `--emit <unwritable>` → 2 `d2-typed-labels error: [Errno 2] …` |

Convention cross-check: the lane's documented convention is 0 / 1 / 2 with
"2" reserved for could-not-evaluate (`SKILL.md:132` per
`reports/round-8/depth/design-spec.md:71-77`; `corpus/knowledge/verification/gate-frozen-run-standard.md:90`
"`2` is reserved for could-not-evaluate"; `reports/round-8/depth/shard-parser.md:749`
expected `--packet` malformed → exit 2). The shipped tool matches.

Two mode-specific nuances worth stating because a consumer keying on the exit
code alone can be surprised:

- `--check` answers **byte-identity only**: on a fresh artifact it exits 0
  even though the same projection carries 15 HOLD/FAIL findings
  (`--check <fresh emit>` → 0; report mode on the same packet → 1, coverage
  `findings_hold_or_fail=15`). This matches the tool's own docstring
  (`--check  # exit 0 identical / 1 drift / 2 error`) and its inline comment
  "check answers byte-identity; findings are the report's job" (line 2754).
- `--json` prints one JSON document whose `exit_code` field equals the process
  exit code in both tested classes (`exit_code: 1` for findings; `exit_code:
  2, ok: false` for the malformed packet).

## 4. Full case matrix

Battery script `/home/vgpnk/.cache/r8d10/run-battery.sh` (23 cases) plus 7
supplemental cases, all against the copy of hash `0da0015f…`. Exit codes:

| # | case | exit | first line (stdout unless "err") |
|---|---|---|---|
| 1 | `--help` | 0 | usage: … |
| 2 | `-h` | 0 | usage: … |
| 3 | no args (report) | 1 | `FINDING D2L-FORM-UNRESOLVED: [hold] GAR-01 — …` |
| 4 | `--json` | 1 | `{"exit_code": 1, "findings": …` |
| 5 | `--emit <file>` | 1 | `Wrote /…/projection.out.yml` |
| 6 | `--check` (default target missing in mirror) | 1 | err: `…typed-labels.d2.yml differs from the deterministic projection` |
| 7 | `--check <fresh emit>` | 0 | `…: byte-identical deterministic projection` |
| 8 | `--bogus` | 2 | err: argparse usage + `unrecognized arguments: --bogus` |
| 9 | `--packet` (no value) | 2 | err: argparse `expected one argument` |
| 10 | `--packet <missing file>` | 2 | `FINDING D2L-DATA: [fail] … — [Errno 2] No such file…` |
| 11 | `--packet` invalid JSON | 2 | `FINDING D2L-DATA: … not a mapping line` |
| 12 | `--packet` JSON array root `[1, 2, 3]` | 2 | `FINDING D2L-DATA: … not a mapping line` |
| 13 | `--packet` JSON mapping, unknown root key | 2 | `FINDING D2L-DATA: … not a mapping line` |
| 14 | `--packet` YAML mapping, unknown root key | 2 | err: `d2-typed-labels error: packet.eras: expected a non-empty list of era tags` |
| 15 | `--packet` minimal YAML `costumes: []` | 2 | err: `…packet.eras: expected a non-empty list of era tags` |
| 16 | `--packet` empty file | 2 | `FINDING D2L-DATA: … — no content lines` |
| 17 | `--packet <directory>` | 2 | `FINDING D2L-DATA: … — [Errno 21] Is a directory…` |
| 18 | `--emit <missing dir>/x.yml` | 2 | err: `d2-typed-labels error: [Errno 2] …` |
| 19 | `--emit <directory>` | 2 | err: `d2-typed-labels error: [Errno 21] Is a directory…` |
| 20 | `--json --emit X` | 1 | JSON printed; `X` not created (precedence, §2) |
| 21 | `--check <fresh> --json` | 0 | check message; no JSON (precedence) |
| 22 | `--check <directory>` | 2 | err: `d2-typed-labels error: [Errno 21] …` |
| 23 | `--selftest extra` | 2 | err: argparse `unrecognized arguments: extra` |
| 24 | `--selftest` (TMPDIR on a writable fs) | 0 | `selftest: 39/39 checks passed — …` |
| 25 | `--packet` real packet, `eras:`→`erasX:` | 2 | err: `packet.eras: expected a non-empty list of era tags` |
| 26 | `--packet` Latin-1 bytes | 2 | `FINDING D2L-DATA: … 'utf-8' codec can't decode byte 0xe9…` |
| 27 | `--json --packet` malformed | 2 | `{"exit_code": 2, …, "ok": false, …}` |
| 28 | `--emit X --packet` malformed | 2 | err: `could-not-evaluate: nothing to emit` |
| 29 | `--check X --packet` malformed | 2 | err: `could-not-evaluate: [{'id': 'D2L-DATA', …}]` |
| 30 | no args (report tail) | 1 | coverage line: `coverage: conflicts=4, findings_hold_or_fail=15, findings_total=16, … typed_labels=58` |

Sweep for tracebacks over the battery log (23 cases):
`grep -c "Traceback" /home/vgpnk/.cache/r8d10/out/battery.log` → `0`
(2026-10-17). Cases 24–30 were run separately; case 27–29's JSON/emit/check
paths also produced no traceback.

## 5. Observations

- **O1 — help is healthy.** `--help`/`-h` exit 0 and list every flag. Contrast:
  the lane's `tools/check-craft-exercise.py --help` exits 2
  (`CLI-ERROR CRAFT-CLI-USAGE: unknown option '--help'`), and
  `tools/check-evidence-coupling.py --help` exits 2 as well; this tool follows
  the argparse convention instead. (Sibling probes in §7.)
- **O2 — usage errors are argparse-stable.** Unknown flag, missing option
  value and extra positional all exit 2 with usage on stderr, matching the
  lane's 0/1/2 convention.
- **O3 — JSON is not an input format.** The loader is the YAML-subset reader:
  *valid* JSON is rejected too — `{"costumes": []}` exits 2 with "content …
  is not a mapping line" (case 15). So the assigned "invalid JSON input" case
  is really "a JSON document is not a legal packet at all"; the failure is
  clean and stable (exit 2, `D2L-DATA`, no traceback), but a caller cannot
  pass a JSON packet. This is a documented input-format limit, not a crash.
- **O4 — wrong root key fails closed, naming the key.** Two flavors:
  (a) JSON-shaped roots die in the loader as "not a mapping line";
  (b) YAML mapping roots die in the schema check with the missing key named —
  `packet.eras: expected a non-empty list of era tags` — reproduced both with
  a synthetic file (case 14) and with the real packet's `eras:` renamed to
  `erasX:` (case 25). Exit 2 either way, no traceback.
- **O5 — `--check` deliberately ignores findings.** Byte-identity is the only
  question `--check` answers (exit 0 on a fresh artifact that still carries 15
  findings). Consumers must use report/`--json` for finding status. Not a
  defect — it is the tool's own documented contract — but it is the one
  place where exit 0 does not mean "no findings".
- **O6 — flag precedence is undocumented.** `--check` > `--json` > `--emit` >
  report is observable (cases 20–21, 28–29) but absent from `--help`. A caller
  combining `--json --emit X` gets JSON and no file; that silently drops the
  requested write. Worth one help-text line (report to D02, not absorbed).
- **O7 — output-path errors are stable.** `--emit`/`--check` against missing
  directories or directories exit 2 with `d2-typed-labels error: [Errno …]`
  on stderr (cases 18–19, 22); malformed packets in those modes exit 2 with
  `could-not-evaluate: …` (cases 28–29).
- **O8 — no tracebacks** across 30 cases (sweep in §4), including every
  malformed-input class tested.
- **O9 — selftest needs a writable temp dir.** See §6.
- **O10 — JSON document and process exit agree** (`exit_code` field, cases 4
  and 27).

## 6. Environment caveat: `/tmp` inode exhaustion (2026-10-17)

The first battery run (tool hash `e9209f28…`, 17:31 -03:00) reported
`--selftest` exit 1 with a traceback:

```text
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp6dvrg5d2/repo/tools/gates'
```

Cause: `/tmp` was 100% inode-full (`df -i /tmp` → `IUse% 100%`; `touch
/tmp/probe-$$` → "No space left on device"), so the selftest's
`tempfile.TemporaryDirectory()` could not `mkdir`. With `TMPDIR` pointed at a
writable filesystem the same selftest exits 0:
`TMPDIR=/home/vgpnk/.cache/r8d10/tmp python3 tools/d2-typed-labels.py --selftest`
→ `selftest: 39/39 checks passed …`, empty stderr. This is an environment
failure, **not** a tool defect; recorded so no one misreads the v1 traceback,
and as a note that any worker running selftests this round needs a writable
`TMPDIR` (all selftests here use `tempfile`).

## 7. Baseline: lane exit-code convention (sibling probes, 2026-10-17)

Commands run in the lane repo (read-only), for context only:

| tool | probe | exit |
|---|---|---|
| `tools/assemble-d2.py` | `--help` / `--check` / `--selftest` / `--bogus` | 0 / 0 / 0 / 2 |
| `tools/replay-frozen.py` | `--help` / no manifest / unreadable manifest | 0 / 2 / 2 (`COULD-NOT-EVALUATE manifest_unreadable`) |
| `tools/check-craft-exercise.py` | `--help` / missing file / invalid JSON / wrong root shape | **2** / 2 / 2 / 2 (`CRAFT-CLI-*` diagnostics) |
| `tools/check-evidence-coupling.py` | `--help` | **2** (`CLI-ERROR D3-DATA usage: unknown option '--help'`) |
| `tools/check-gate-battery.py` | `--help` / `--selftest` | 0 / 0 |
| `tools/gates/myth-consistency-gate.py` etc. | `--help` treated as a file path | 2 (`FINDING G-DATA: cannot read --help`) |

So: 0/1/2 is the lane convention, argparse tools exit 0 on `--help`, and
several hand-rolled parsers (check-craft-exercise, check-evidence-coupling,
three gates) treat `--help` as a bad argument and exit 2. The D2 tool sits on
the argparse side of that split.

## 8. Reproduction

```sh
# 1. isolated tree (never test in the lane working tree)
R=/home/vgpnk/Projects/shokunin/kotodama-shokunin
T=$HOME/.cache/r8d10/repo && mkdir -p "$T/tools/gates" "$T/examples/culture-d2/components"
cp "$R/tools/d2-typed-labels.py" "$T/tools/"
cp "$R/tools/gates/costume-era-consistency-gate.py" "$T/tools/gates/"
cp "$R/examples/culture-d2/packet.d2.yml" "$T/examples/culture-d2/"
for f in 12-rank-rules.yml 11-costumes.yml 09-eras-calendar.yml 05-lexicon.yml; do
  cp "$R/examples/culture-d2/components/$f" "$T/examples/culture-d2/components/"; done

# 2. battery (23 cases) — script saved at $HOME/.cache/r8d10/run-battery.sh
bash "$HOME/.cache/r8d10/run-battery.sh"

# 3. selftest needs a writable TMPDIR
TMPDIR="$HOME/.cache/r8d10/tmp" python3 "$T/tools/d2-typed-labels.py" --selftest
```

Fixtures used for the input cases: `{"a": ` (invalid JSON), `[1, 2, 3]`
(array root), `{"wrong_root": {"x": 1}}` (JSON wrong root), `wrong_root:\n  x:
1` (YAML wrong root), `costumes: []` (minimal YAML), empty file, a directory,
and the real packet with `eras:` renamed `erasX:`.

## 9. Limits

- Revision-bound: everything above describes hash `0da0015f…` (2915 lines).
  The tool was still being integrated during this shard: a 20 s-interval
  stability watch observed at least 24 distinct sha256 values between
  17:19:49 and 17:33:51 -03:00; the hash has held from 17:33:51 through at
  least 17:37:51. Any later revision must be re-tested, and this doc must not
  be cited for a different hash.
- Only CLI surface behavior was tested. Domain correctness, the selftest's
  control matrix, determinism and frozen replay are other shards' claims
  (R8-D06..D13); no canon, attribution or rights claim is made or implied
  (`PROVINCE.md`; `AGENTS.md`).
- Scratch artifacts live outside the lane repo (`$HOME/.cache/r8d10/`); the
  lane tree was read-only for this shard. No `git` state was changed.
