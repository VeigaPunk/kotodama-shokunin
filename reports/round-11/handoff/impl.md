# Handoff-e2e exercise — implementation report (R11-O02..O05)

- shard: round-11 claim O (operability), targets **R11-O02..O05** (implementation,
  single writer of the exercise tool). Round 11, loop 1 of 3, build round 4 of 4,
  2026-10-17.
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; every command below ran from
  the lane root with `export TMPDIR=$PWD/.scratch`. No commit, push, or filed-artifact
  edit was made by this shard.
- owns / wrote: `tools/exercise-handoff-e2e.py` (the exercise, sole writer),
  `reports/round-11/handoff/{expected.json,packet.md,run.log,freeze.txt}` (its frozen
  baseline and the bytes that baseline pins), and this file. Read-only everywhere else —
  `examples/**`, `corpus/**`, `tools/gates/**`, `reports/round-{8,9,10}/**` were never
  modified.
- implements: `reports/round-11/handoff/design.md` (R11-O01) — §2 read set, §3 field map,
  §4 recognition hazards, §5 glossary rule, §6 cross-reference assertions, §8 baseline and
  tamper controls, §9 control matrix, §10 CLI/exit surface.
- verified-at: 2026-10-17 19:17 (local, UTC−3). Commands and observed output are quoted
  verbatim in §4–§7 below.

## 0. What the deliverable is

`tools/exercise-handoff-e2e.py` assembles a world-bible handoff packet **from the live D2
and D3 drill artifacts** — no hand-written packet body, every field derived from bytes on
disk — copies it into an isolated directory outside the repository, and runs the committed
contract gate `tools/gates/handoff-packet-check.py` over that copy from that foreign
working directory. The exercise passes only when the gate reports
`fields=16/16 glossary-entries=20 findings=0` at exit 0 **and** everything else the run
observed equals the committed frozen baseline. It is not a gate, not a canon decision, and
not lore acceptance: it emits `not canonized` and never a producer-side canon
certification (contract §6, §8.7, §11).

Two gaps the gate structurally cannot close are closed on the exercise's own side
(design §1):

1. the gate counts glossary rows it sees, it does not know how many there should be — the
   exercise asserts 20 rows against the live lexicon's id set and per-record status;
2. the gate checks digest *presence*, never digest *equality* — the exercise re-measures
   every digest it emits and asserts equality with the bytes it read.

## 1. Files, paths and digests (measured 2026-10-17T19:17-03:00, `sha256sum`)

| file | role | sha256 |
|---|---|---|
| `tools/exercise-handoff-e2e.py` | the exercise (single writer: this shard) | `a21934ade22b2cda338645ee389c7f848256348446d8a79f38a9c9ff827d2005` |
| `reports/round-11/handoff/expected.json` | frozen baseline (`inputs`, `packet_sha256`, `glossary_entry_ids`, `declared`, `baseline_digest`) | `a94f9ded9d0938ec1510a1834b83162635c9e94a04b70461d5db0b98a0031d7a` |
| `reports/round-11/handoff/packet.md` | the exact packet bytes the baseline pins | `6583b6bdbf5e3fe039d1eee1d9f53d63ef09a04e3eeb5c98ae4943ed1771a64f` |
| `reports/round-11/handoff/run.log` | the gate's stdout for the frozen run | `60d2965858c1f25c6d76f44bafdabbb2ea512fb271154274b943d7f6de21047e` |
| `reports/round-11/handoff/freeze.txt` | freeze stamp plus the re-freeze diff | `c3d1393fdd3b81c4db52a2aa4a36abfe0555c8e170d3df87c6c32d58d14b8f40` |

Baseline path is `reports/round-11/handoff/expected.json` per design §8, and deliberately
**not** under `tools/gates/{expected,frozen}/**`: `tools/check-gate-battery.py` reads every
`expected.json` under those two roots as a gate baseline
(`BASELINE_ROOTS = (GATES_DIR / "expected", GATES_DIR / "frozen")`, battery `:114`;
discovery `:387–394`), and a baseline naming no gate from its seven-name `GATE_NAMES` tuple
is a could-not-evaluate finding. A tool baseline there would break the battery. Confirmed
in the current round's own runner output, which already reads one such `unevaluable`
baseline from those roots (`reports/round-11/validation.json`, claim D failures).

## 2. Design conformance (what the tool does, and where the design fixed the form)

- **Read set (design §2):** 21 files — the pinned contract, the D3 packet and legacy
  projection, D3 `controls.json` and `expected.json`, the four D3 components, the D2 packet
  and `typed-labels.d2.yml`, the four closed round-6 source ledgers,
  `reports/round-6/parent-reconciliation.json`, the gate, and the four remaining tools.
  Every digest is measured in-run; none is copied from a document. `examples/culture-d3/handoff.md`
  and both `README`s are deliberately outside the read set (documentation surfaces, stale
  digests per design §7).
- **16 fields (design §3):** nine supplied as `| field | value |` table rows
  (`packet_id`, `packet_version`, `contract_ref`, `producer`, `recipient`, `request_ref`,
  `baseline_bible_ref`, `subject_refs`, `scope`) and seven as exact `## field_name`
  sections carrying the table payloads (`artifact_manifest`, `dependency_manifest`,
  `claim_ledger`, `coupling_edges`, `requested_decisions`, `validation`, `open_questions`).
  `packet_id` is `kotodama.handoff.d2d3-e2e`, `packet_version` `1.0.0` "pure function of
  the pinned read set; no wall-clock content" — the packet contains no date, so two runs
  are byte-identical.
- **Glossary (design §5):** one inline table, header
  `| entry_id | E0 form | E1 form | gloss (packet) | etymology |`, exactly 20 data rows in
  source order from `packet.json` `lexicon[]`; each etymology cell is
  `status: <the record's own status> — E0 *<E0> → E1 <E1> (<changed by SC1 …|unchanged into
  E1>); available_from <era>`. Live statuses are 20/20 `constructed`. The manifest's
  `A-GLOSS` row identifies the payload's source bytes and the word `inline`, so no
  `INFO glossary-external` line claims the profile is unchecked. The packet never
  self-digests.
- **Cross-reference assertions (design §6):** the §4 field-name set is parsed from the
  contract's own table **and** from the gate's `FIELD_NAMES` tuple and compared with the
  set the packet supplies (three-way agreement, enforced before any gate run); the
  `contract_ref` digest is compared with the contract bytes measured in the same run;
  every `claim_ledger` kind token is checked against the contract §6 kinds; the
  `dependency_manifest` is rejected if it carries an unnegated version float; all eight
  `subject_refs` are `cand:`-namespaced and the text says unresolved; every
  `artifact_manifest` row digest is compared with the named file's measured bytes.
- **Baseline and tamper controls (design §8):** `expected.json` carries the declared
  expectations plus measured inputs, packet digest, glossary ids, per-field digests,
  cross-refs, counts, a `limits` statement, and a `baseline_digest` self-checksum; an
  edited baseline body is refused as `E2E-BASELINE` (exit 2) instead of being re-blessed;
  a re-signed expectation that disagrees with the code's declared constants is refused the
  same way.
- **CLI and exit codes (design §10):** `--selftest`, `--root DIR`, `--baseline PATH`,
  `--keep DIR`, `--json`, `--quiet`, plus `--freeze DIR` (an explicit admin action that
  prints the old→new diff before re-pinning). Exit 0 clean; 1 `E2E-DIGEST` / `E2E-COUNT` /
  `E2E-GATE` / `E2E-SCAN`; 2 `E2E-ARTIFACT` / `E2E-BASELINE` / `E2E-DATA`. No traceback
  escapes: every failure is a named code plus a one-line message. One stable summary line
  for the parent runner:
  `handoff-e2e: exit=0 fields=16/16 glossary=20/20 findings=0 packet_sha256=<…>`.
- **Hazards honoured (design §4):** section headings use the exact underscore names; the
  §scope detail table sits under `## delivered record sets` so no heading carries a field
  token (an in-repo hazard probe reproduces the gate-side hijack and proves the renderer
  emits none); the placeholders set is avoided in every value; canon-claim regex traps are
  pattern-checked before the gate runs; manifest rows carry `artifact_id` so they are never
  read as a glossary payload.

## 3. Repository state and the live drift this shard hit

While this shard was implementing, the D-claim workstream regenerated
`examples/culture-d2/typed-labels.d2.yml` and added `examples/culture-d2/packet.d2.typed.yml`
and `examples/culture-d2/typed-gate.expected.json`. The exercise caught it, as designed:

```
$ python3 tools/exercise-handoff-e2e.py
FAIL input-digest: examples/culture-d2/typed-labels.d2.yml: frozen e70ba1477dbe… live a3aa452cd5ae…
FAIL verdict: 1 read-set file(s) changed since the baseline was frozen: examples/culture-d2/typed-labels.d2.yml
handoff-e2e: exit=1 fields=? glossary=?/20 findings=? packet_sha256=(not assembled)
handoff-e2e: E2E-DIGEST: 1 read-set file(s) changed since the baseline was frozen: …
```

That is the intended behaviour, not a defect: design §11 fixes the ordering — the baseline
is re-pinned **after** the D2 side stops moving. A stability poll over
`packet.d2.yml`, `typed-labels.d2.yml` and `tools/d2-typed-labels.py` (three consecutive
30 s polls, `sha256sum` compared) went quiet at 19:16:33 local, and the re-freeze was run
then. The re-freeze diff is retained in `freeze.txt`:

```
re-frozen packet_sha256: 87523e3db7ec1b5b738f9ff38952236a76c908e9… -> 72739729786a21fd7d3d41c6291c8137efa8dfa8…
re-frozen input examples/culture-d2/typed-labels.d2.yml: e70ba1477dbe… -> a3aa452cd5ae…
```

(The final packet digest in §1, `6583b6bd…`, is later than the `7273972978…` of that
re-freeze because one further defect fix — §5 item 4 — changed the rendered bytes. Note
that `freeze.txt` is rewritten by each freeze and therefore retains only the **most recent**
diff (`7273972978… -> 6583b6bd…`); the earlier diff is quoted here, in this report,
because the freeze log does not accumulate. Three freezes ran in total: the initial one, the
D2-drift re-pin, and the defect-4 re-pin.)

**Standing dependency:** the read set includes D2 artifacts that another claim is still
editing. Any further D2 change re-drifts the baseline and the exercise will exit 1
`E2E-DIGEST` naming the file. The fix is always the same and always explicit:
wait for stability, then `--freeze reports/round-11/handoff`, then read the printed diff.

## 4. Positive run — observed

```
$ export TMPDIR=$PWD/.scratch
$ python3 tools/exercise-handoff-e2e.py
OK   input-digest: 21 read-set digests match the frozen baseline
OK   preflight: 16 fields supplied, non-canon marker present, glossary vocabulary licensed, no floating version reference
OK   cross-references: contract §4 names = gate FIELD_NAMES = supplied fields; contract digest measured; claim kinds in the §6 set; 13/13 component digests matched; manifest digests equal bytes for 21 files
OK   gate-exit: tools/gates/handoff-packet-check.py exit 0 (expected 0) over the isolated copy at …/.scratch/handoff-e2e-xoit0b0a/isolated
OK   gate-scan: fields=16/16 glossary-entries=20 findings=0
OK   frozen-packet: packet sha256 6583b6bdbf5e3fe039d1eee1d9f53d63ef09a04e3eeb5c98ae4943ed1771a64f
OK   frozen-glossary: 20 entry ids match the baseline
OK   preservation: the 21 read-set files are byte-identical before and after the run
handoff-e2e: exit=0 fields=16/16 glossary=20/20 findings=0 packet_sha256=6583b6bdbf5e3fe039d1eee1d9f53d63ef09a04e3eeb5c98ae4943ed1771a64f
$ echo $?
0
```

(The isolated-directory suffix changes per run; it is a fresh directory under `TMPDIR`
every time. The transcript above is the run against the frozen bytes of §1 — the same
digest `run.log` records, with `fields=16/16 glossary-entries=20 findings=0`.)
`--json` prints a receipt document (`profile`, `root`, `baseline`, `exit`, `code`,
`checks`); `--keep DIR` retains the isolated copy for inspection; `TMPDIR` is honoured for
every write.

## 5. Defects found by running it (all fixed, none filed elsewhere)

| # | symptom | cause | fix |
|---|---|---|---|
| 1 | `TypeError: object of type 'int' has no len()` | a count used with `len()` in a coupling row | used the count directly |
| 2 | contract digest rendered as `sha256:5` | `digests[rel][0]` indexed the hex string's first character | use the digest string directly (12 sites) |
| 3 | `TypeError: cannot unpack non-iterable int` | manifest builder received `(digest, size)` tuples in one path and a size map in another | single signature: digests map + sizes map |
| 4 | manifest roles rendered as Python tuple reprs, e.g. `('pinned adjacency contract …',)` — **visible in the first frozen packet.md** | trailing commas made single-element tuples | removed the commas, re-froze, re-verified the frozen bytes (no tuple repr remains) |
| 5 | `--selftest` fixture failed on missing D2/D3 component files | fixture copied only read-set files, but the exercise re-measures the components named in the assemblers' manifests | fixture now derives and copies those component paths too |

Defect 4 is why the packet was re-frozen after a first freeze; `freeze.txt` keeps only the
most recent diff, so the earlier one is quoted in §3 rather than silently overwritten.

## 6. Selftest — observed, exit 0, 17 controls

```
$ python3 tools/exercise-handoff-e2e.py --selftest
selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0) plus 17 controls:
  - positive: exit 0 — fields=16/16 glossary-entries=20 findings=0
  - isolation: the CLI run from a foreign cwd exits 0 with the same scan
  - malformed-01 dropped request_ref row: gate exit 1, HO-MISSING
  - malformed-02 blank scope value: gate exit 1, HO-EMPTY
  - malformed-03 floating version: gate exit 1, HO-DEP-FLOAT
  - malformed-04 canon marker removed: gate exit 1, HO-CANON-CLAIM+HO-CANON-MARKER
  - malformed-05 producer canon claim: gate exit 1, HO-CANON-CLAIM
  - malformed-06 unlicensed etymology status: gate exit 1, HO-GLOSS-ETYM
  - malformed-07 dropped glossary row: the gate counts 19 rows silently; preflight fails closed
  - malformed-08 hyphenated coupling_edges heading: gate exit 1, HO-MISSING
  - malformed-09 renamed open_questions heading: gate exit 1, HO-MISSING
  - malformed-10 malformed input (no heading): gate exit 2, HO-DATA
  - hazard probe: a `scope-notes` heading is read as a `scope` supply with exit still 0; the renderer emits no heading carrying a field-name token
  - preservation: the 21 read-set files are byte-identical before and after a run
  - tamper baseline: exit 2 E2E-BASELINE (integrity digest mismatch), never a pass
  - tamper read-set: exit 1 E2E-DIGEST naming the changed file
  - tamper scan expectation: exit 2 E2E-BASELINE (a re-signed expectation is refused, not honoured)
  - missing artifact: exit 2 E2E-ARTIFACT naming the unreadable path
$ echo $?
0
```

The whole matrix runs against throwaway copies inside one temporary directory; the lane
tree is untouched (the preservation control measures that).

## 7. Parent-runner conformance and the design's open item

`reports/round-11/run-validation.py` (X03) discovers the exercise at `tools/exercise-handoff-e2e.py`,
runs `--selftest` (exit 0, malformed and positive controls named, no failing `n/m` count),
then a plain run, and reads the numbers `16/16`, `20/20` and `findings=0` out of the
output plus a mention of `handoff-packet-check`; it then looks for a parseable
`expected.json` under `reports/round-11/handoff/**`. This tool satisfies each of those, and
one fix was made for it: the plain run now names the gate path in its output rather than
only the isolated directory.

Design §11 left one item `to-verify` for the implementers ("cannot run with `TMPDIR`
unset"). Measured: with `env -u TMPDIR`, the run still exits 0 with identical numbers
(Python 3.14.7), so the `/tmp` inode exhaustion does not break this tool. The lane rule
still requires the redirect, and the tool honours it — every temporary directory, including
the isolated packet copy, lands under `TMPDIR` when it is set.

## 8. Limits and what this shard did not do

- The exercise pins **drift**, not quality: a packet that is internally consistent and
  passes the gate can still be poor anthropology. Content judgement stays with the domain
  reviewers (design §2 limit, contract §8.5).
- The packet's `validation` field states the checks this run performed and the declared
  expectation; the *observed* verdict for the frozen bytes lives in `run.log` and
  `expected.json`, not inside the packet, so the packet stays a pure function of the read
  set with no self-reference.
- Nothing here decides canon, rights, or lore acceptance; out-of-province items stay
  reported, not absorbed.
- **Interaction to flag, not fix:** two O-claim shards already ran an *earlier* revision of
  this tool (`reports/round-11/handoff/tamper-control.sh|log`, `frozen-rerun.md`) against a
  baseline at `tools/gates/expected/handoff-exercise/r11/expected.json` — the path design
  §8 later ruled out, and which no longer exists. Their receipts therefore cite a stale
  tool digest and an absent baseline path; re-running them against the current tool and
  `reports/round-11/handoff/expected.json` is the correct repair. Their filed bytes were
  not edited by this shard.
- No `LOG.md` entry was appended and nothing was committed: during a parallel wave the
  parent integrates and records (lane `AGENTS.md`).

## 9. Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch

python3 tools/exercise-handoff-e2e.py            # exit 0, 16/16, 20/20, findings 0
python3 tools/exercise-handoff-e2e.py --selftest # exit 0, 17 controls
python3 tools/exercise-handoff-e2e.py --json     # receipt document
sha256sum reports/round-11/handoff/{packet.md,expected.json,run.log,freeze.txt}

# only after the D2 artifacts stop moving, and only deliberately:
python3 tools/exercise-handoff-e2e.py --freeze reports/round-11/handoff
```

Counts carry their commands and date: 21 read-set files, 16 §4 fields, 20 glossary rows,
13 component digests re-measured (9 D2 + 4 D3), 8 namespaced subject refs, 17 selftest
controls, 58 D2 typed labels / 16 findings / 13 unresolved rank items / 9
`R-MAT-BRIDGE-MISSING` holds (measured 2026-10-17 by the commands above and by the packed
rows' own sources).
