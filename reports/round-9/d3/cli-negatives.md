# R9-D05 — D3 CLI negatives: malformed component inputs → stable exit-2, no tracebacks

- Round: 9 (claim **D** / depth, capability `culture-d3-acceptance`), date `2026-10-17`.
- Lane: kotodama-shokunin (`/home/vgpnk/Projects/shokunin/kotodama-shokunin`), HEAD `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`.
- Surface under test: `tools/assemble-culture-d3.py` (the D3 assembler CLI). The tool was **not modified**: sha256 `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014` before and after this run.
- Contract lines this evidence checks: `tools/assemble-culture-d3.py:27` ("`--check` compares bytes without writing: exit 0 equal / 1 drift / 2 error"), `:28` ("A missing or malformed component fails closed with exit 2 before any write"), and `reports/round-7/d3-contract.json` → `assembly` ("`--check` is read-only and exits 0 equal / 1 drift / 2 error").

## Verdict

**Holds.** 29 malformed/defective-input cases driven through the real CLI all exit **2**, all print a one-line `assembly error: …` diagnostic naming the offending file/key, none print a traceback, and none write, truncate or delete an output file. Diagnostics are byte-identical across repeated runs.

| quantity | value | command |
| --- | --- | --- |
| battery cases | 32 (29 negatives + 3 controls) | `python3 /home/vgpnk/.cache/r9-d05/cli_negatives_v2.py` |
| cases meeting declared expectation | 32/32 | same |
| negatives observed exit code | `[2]` (single value across all 29) | same |
| `no_traceback` | 32/32 | same |
| `stable_repeat` (two subprocess runs per case, identical exit+stdout+stderr) | 32/32 | same |
| `no_outputs_from_failing_run` | 32/32 | same |
| full battery runs, same totals each time | 5/5 (`32/32` on the final 32-case revision; `30/30` on the four earlier runs of the 30-case revision, from which the last two cases were then added) | `python3 /home/vgpnk/.cache/r9-d05/cli_negatives_v2.py` (repeated) |

## Method (why the evidence is about the delivered tree)

Each case copies the **delivered** `tools/assemble-culture-d3.py`, `tools/assemble-d2.py` and the four real `examples/culture-d3/components/*.json` into a throwaway tree, applies exactly one mutation to that copy, then runs the real CLI from inside the copy (twice per case). Copy digests are asserted against the delivered files before each case, so a mutation can never leak into the repo. Nothing in the repo is written by the battery; scratch lives in `/home/vgpnk/.cache/r9-d05/` (outside the repo).

Consequence to state plainly: the case bodies are derived from the *delivered* components (real keys, real counts, real anchors), but the mutations are applied to copies — the delivered components themselves were never corrupted.

## Delivered-tree baselines (no behavior change)

| receipt | command | output | exit |
| --- | --- | --- | --- |
| clean tree before battery | `python3 tools/assemble-culture-d3.py --check` | `packet.json: byte-identical deterministic assembly; packet.gates.yml: byte-identical deterministic assembly` | 0 |
| clean tree after battery | same | same | 0 |
| fixture selftest, default temp dir | `python3 tools/assemble-culture-d3.py --selftest` | `selftest: 85/85 checks passed — …` | 0 |
| fixture selftest, redirected temp dir | `TMPDIR=/home/vgpnk/.cache/r9-d05/selftest-tmp python3 tools/assemble-culture-d3.py --selftest` | `selftest: 85/85 checks passed — …` | 0 |

Digests of the surface, unchanged before and after (`sha256sum`):

```
ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014  tools/assemble-culture-d3.py
8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d  tools/assemble-d2.py
fee4ad61a6aa9ca524c627a04ddbe61653a4058261aadf352f3b16a63b4dacfa  examples/culture-d3/components/04-language.json
20ec0b1ffbc64a04fba2b031ddb3d8023c4610951382acdb85e2294c43320b2d  examples/culture-d3/components/05-ritual.json
ba9866e37448b18e00710d490000ef662a07a41325109841a7d755f146d9eee7  examples/culture-d3/components/06-material.json
1579aa84c3c924e91d4ea383b5bff1e1d75367a35ad0cbbd0533b9bc9725e8a3  examples/culture-d3/components/07-evidence.json
bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829  examples/culture-d3/packet.json
306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425  examples/culture-d3/packet.gates.yml
```

Interpreter: `Python 3.14.7` (`python3 -V`). All timestamps below are UTC, `2026-10-17T20:48Z`–`20:52Z`.

## Case results

`<TMP>` is the throwaway copy root, normalized in the recorded stderr so the diagnostics compare byte-for-byte between runs. Message column is the first stderr line (long messages truncated to 110 chars with `...`).

| case | argv | expected exit | observed exit | first stderr (or stdout for exit-0/1 controls) |
| --- | --- | --- | --- | --- |
| `control/clean-copy-default` | `[]` | 0 | 0 | `Wrote examples/culture-d3/packet.json (37222 bytes)` |
| `control/check-after-generate` | `['--check']` | 0 | 0 | `packet.json: byte-identical deterministic assembly; packet.gates.yml: byte-identical deterministic assembly` |
| `control/check-without-outputs` | `['--check']` | 1 | 1 | `examples/culture-d3/packet.json differs from deterministic assembly` |
| `binary/bad-json-truncated` | `[]` | 2 | 2 | `assembly error: 06-material.json: invalid JSON (Expecting value: line 1 column 11 (char 10))` |
| `binary/bad-json-empty-file` | `[]` | 2 | 2 | `assembly error: 04-language.json: invalid JSON (Expecting value: line 1 column 1 (char 0))` |
| `binary/utf8-bom-rejected` | `[]` | 2 | 2 | `assembly error: 04-language.json: invalid JSON (Unexpected UTF-8 BOM (decode using utf-8-sig): line 1 colum...` |
| `binary/invalid-utf8` | `[]` | 2 | 2 | `assembly error: 05-ritual.json: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 0: invali...` |
| `binary/root-array` | `[]` | 2 | 2 | `assembly error: 04-language.json: root must be a JSON object` |
| `binary/root-string` | `[]` | 2 | 2 | `assembly error: 06-material.json: root must be a JSON object` |
| `binary/root-null` | `[]` | 2 | 2 | `assembly error: 05-ritual.json: root must be a JSON object` |
| `structural/missing-assigned-key` | `[]` | 2 | 2 | `assembly error: 05-ritual.json: top-level keys must be exactly ['beliefs', 'naming_rule', 'speech_rules', '...` |
| `structural/all-keys-missing` | `[]` | 2 | 2 | `assembly error: 04-language.json: top-level keys must be exactly ['lexicon', 'names', 'phonology', 'sound_c...` |
| `structural/nested-record-not-object` | `[]` | 2 | 2 | `assembly error: materials[None]: missing non-empty string 'gate_name' needed for projection` |
| `structural/unexpected-extra-key` | `[]` | 2 | 2 | `assembly error: 05-ritual.json: top-level keys must be exactly ['beliefs', 'naming_rule', 'speech_rules', '...` |
| `structural/type-bool-for-object` | `[]` | 2 | 2 | `assembly error: 04-language.json.phonology: expected dict` |
| `structural/type-object-for-list` | `[]` | 2 | 2 | `assembly error: 04-language.json.lexicon: expected list` |
| `structural/below-minimum-count` | `[]` | 2 | 2 | `assembly error: lexicon: 5 records, below the declared minimum of 20` |
| `io/missing-component` | `[]` | 2 | 2 | `assembly error: missing component: examples/culture-d3/components/07-evidence.json` |
| `io/component-path-is-directory` | `[]` | 2 | 2 | `assembly error: missing component: examples/culture-d3/components/06-material.json` |
| `io/component-unreadable-mode-000` | `[]` | 2 | 2 | `assembly error: [Errno 13] Permission denied: '<TMP>/examples/culture-d3/components/06-material.json'` |
| `io/missing-d2-serializer` | `[]` | 2 | 2 | `assembly error: yaml serializer not found: tools/assemble-d2.py` |
| `io/output-packet-path-is-directory` | `[]` | 2 | 2 | `assembly error: [Errno 21] Is a directory: '<TMP>/examples/culture-d3/packet.json'` |
| `projection/lexeme-without-E1` | `[]` | 2 | 2 | `assembly error: lexicon: record 'L01' lacks a string forms.E1 needed for projection` |
| `projection/unknown-material-id` | `[]` | 2 | 2 | `assembly error: costumes[C01]: material_id 'M99' has no declared material` |
| `projection/name-bases-not-a-pair` | `[]` | 2 | 2 | `assembly error: names[N01]: formation.bases must be a pair of lexeme ids` |
| `merge/component-key-collision` | `[]` | 2 | 2 | `assembly error: component collision: 'phonology' defined by both 04-language.json and 05-ritual.json; refus...` |
| `mode/check-flag-with-bad-json` | `['--check']` | 2 | 2 | `assembly error: 06-material.json: invalid JSON (Expecting value: line 1 column 11 (char 10))` |
| `mode/check-flag-with-bad-json-foreign-cwd` | `['--check']` | 2 | 2 | `assembly error: 06-material.json: invalid JSON (Expecting value: line 1 column 11 (char 10))` |
| `mode/check-flag-with-missing-key` | `['--check']` | 2 | 2 | `assembly error: 05-ritual.json: top-level keys must be exactly ['beliefs', 'naming_rule', 'speech_rules', '...` |
| `io/failing-run-preserves-existing-outputs` | `[]` | 2 | 2 | `assembly error: 06-material.json: invalid JSON (Expecting value: line 1 column 11 (char 10))` |
| `argv/unknown-flag` | `['--nope']` | 2 | 2 | `usage: assemble-culture-d3.py [-h] [--check \| --selftest]` |
| `argv/mutually-exclusive-flags` | `['--check', '--selftest']` | 2 | 2 | `usage: assemble-culture-d3.py [-h] [--check \| --selftest]` |

Class totals (29 negatives): binary 7, structural 7, io 6, projection 3, mode 3, merge 1, argv 2.

### Mutation catalogue (exactly what each case changed in the copy)

- `binary/bad-json-truncated`: `06-material.json` ← `{"eras": [`
- `binary/bad-json-empty-file`: `04-language.json` ← zero bytes
- `binary/utf8-bom-rejected`: `04-language.json` ← same bytes prefixed with `EF BB BF`
- `binary/invalid-utf8`: `05-ritual.json` ← raw bytes `ff fe 7b 7d`
- `binary/root-array|root-string|root-null`: `04-language.json` ← `[]`, `06-material.json` ← `"material"`, `05-ritual.json` ← `null`
- `structural/missing-assigned-key`: `05-ritual.json` with `symbols` removed
- `structural/all-keys-missing`: `04-language.json` ← `{}`
- `structural/nested-record-not-object`: `06-material.json` `materials[0]` ← `"felt"` (string)
- `structural/unexpected-extra-key`: `05-ritual.json` gains `"debug": true`
- `structural/type-bool-for-object`: `04-language.json` `phonology` ← `true` (bool rejected, not treated as dict)
- `structural/type-object-for-list`: `04-language.json` `lexicon` ← `{}`
- `structural/below-minimum-count`: `04-language.json` `lexicon` truncated to 5 records (minimum 20)
- `io/missing-component`: `07-evidence.json` unlinked
- `io/component-path-is-directory`: `06-material.json` unlinked, directory created at that path
- `io/component-unreadable-mode-000`: `06-material.json` `chmod 000` (running as uid 1000, not root), restored to `0644` after the case
- `io/missing-d2-serializer`: `tools/assemble-d2.py` unlinked from the copy
- `io/output-packet-path-is-directory`: directory created at `examples/culture-d3/packet.json`
- `io/failing-run-preserves-existing-outputs`: both outputs pre-seeded with sentinel bytes `SENTINEL: pre-existing output must not be touched by a failing run\n`, then `06-material.json` malformed
- `projection/lexeme-without-E1`: `04-language.json` `lexicon[0].forms.E1` removed
- `projection/unknown-material-id`: `06-material.json` `costumes[0].material_id` ← `"M99"`
- `projection/name-bases-not-a-pair`: `04-language.json` `names[0].formation.bases` ← `["L01"]`
- `merge/component-key-collision`: the copy's `COMPONENT_KEYS` patched so `05-ritual.json` also claims `phonology`, and `05-ritual.json` given a `phonology` key. The merge-collision branch is unreachable through the delivered contract (its key sets are disjoint), so reaching it required patching the **copy**; the delivered script is untouched (digest above).
- `mode/*`: `--check` over the same malformed inputs; the foreign-cwd variant ran the copy from `cwd=/` to show the diagnostics and exit code do not depend on the working directory.
- `argv/*`: argparse-level misuse (unknown flag; mutually exclusive flags). These are the only cases whose diagnostic does not start with `assembly error:` — argparse prints `usage: …` + `error: …` and exits 2.

## What the numbers mean beyond exit codes

- **Stable diagnostics** — every case was executed twice, each time as a fresh subprocess. Exit code, stdout and stderr were byte-identical across the two runs for all 32 cases (`stable_repeat` 32/32). The recorded stderr differs from run to run only by the throwaway path, which is normalized; the copy root is in no case baked into a diagnostic other than through the OS `Permission denied` / `Is a directory` errors that necessarily carry an absolute path.
- **Fail-closed, not just non-zero** — for every malformed-input case the run left `packet.json` and `packet.gates.yml` absent, so no partial or stale output can be mistaken for a successful assembly.
- **Existing outputs survive a failing run** — `io/failing-run-preserves-existing-outputs` pre-seeded both outputs with sentinel bytes; after the exit-2 run both files were still byte-identical to the sentinel (`sentinel_preserved` true). A failed assembly therefore cannot silently bless previously generated bytes.
- **`--check` stays read-only on bad input** — `mode/*` exit 2 without creating either output, including when run from a different working directory.
- The whole envelope is `tools/assemble-culture-d3.py:917-938` (`try:` around `assemble()`/`--check`, `except (ValueError, OSError)` → `assembly error: …` on stderr → `return 2`); the diagnostics above all come from `fail()` (`:126`) and the boundary checks in `load_components` (`:151-192`).

## Cross-surface check (D3 coupling guard)

The sibling D3 surface `tools/check-evidence-coupling.py` was probed with the same malformed kinds, using inputs derived from the delivered `examples/culture-d3/packet.json` (its own domain controls belong to R9-D03, not here). Command: `python3 tools/check-evidence-coupling.py <tmp>/packet.json`.

| case | exit | stdout JSON | finding ids | message |
| --- | --- | --- | --- | --- |
| `guard/bad-json` | 2 | valid, `json_stdout` true | `['D3-DATA']` | `packet is not valid JSON: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)` |
| `guard/root-array` | 2 | valid | `['D3-DATA']` | `packet root must be a JSON object, got list` |
| `guard/empty-file` | 2 | valid | `['D3-DATA']` | `packet is not valid JSON: Expecting value: line 1 column 1 (char 0)` |
| `guard/missing-file` | 2 | valid | `['D3-DATA']` | `packet cannot be read: No such file or directory` |

No traceback, empty stderr, machine-readable exit-2 diagnostics on stdout — consistent with the assembler's behaviour on the same malformed kinds.

## Neighbouring boundary probed — one finding (not a fix; outside my write scope)

Fault injection (a shadow `tempfile` module on `PYTHONPATH` whose `TemporaryDirectory` raises `OSError(28)`, applied only to a throwaway copy) shows the CLI's error envelope covers the assembly path but **not** the selftest path:

- `python3 tools/assemble-culture-d3.py` under the injected fault → exit 0, both outputs written (the assembly path never uses `tempfile`).
- `python3 tools/assemble-culture-d3.py --check` under the injected fault → exit 0, byte-identical report.
- `python3 tools/assemble-culture-d3.py --selftest` under the injected fault → **traceback on stderr, exit 1**:

```
  File "…/tools/assemble-culture-d3.py", line 943, in <module>
    sys.exit(main())
  File "…/tools/assemble-culture-d3.py", line 916, in main
    return selftest()
  File "…/tools/assemble-culture-d3.py", line 600, in selftest
    with tempfile.TemporaryDirectory(prefix="assemble-culture-d3-selftest-") as tmpdir:
  File "…/faults/tempfile.py", line 17, in TemporaryDirectory
    raise OSError(28, "No space left on device: '/tmp'")
OSError: [Errno 28] No space left on device: '/tmp'
```

Cause: `main()` calls `selftest()` at `tools/assemble-culture-d3.py:915-916`, i.e. *before* the `try:` at `:917` whose `except (ValueError, OSError)` at `:936` produces the fail-closed exit-2 diagnostic. Nothing in the malformed-component-input claim is affected (assembly and `--check` keep their exits under the same fault), so this is reported as a neighbouring robustness gap for the assembler's owner (round 10 or whoever holds D3 CLI maintenance): wrapping the `selftest()` call in the same envelope would make it `exit 2` + one-line diagnostic instead of a traceback. **No change was made** — the assignment allows reporting only.

## Environment receipts (why scratch is not in `/tmp`)

- `df -i /tmp` → `tmpfs 1048576 1048576 0 100% /tmp` and `touch /tmp/r9d05-probe` → `touch: cannot touch '/tmp/r9d05-probe': No space left on device` (both at `2026-10-17T20:50Z`).
- `python3 -c "import tempfile;print(tempfile.gettempdir())"` → `/var/tmp`: Python skips the unusable `/tmp` and falls back, which is why `--selftest` still passes 85/85 at default settings despite the inode exhaustion.
- The battery therefore keeps every copy under `/home/vgpnk/.cache/r9-d05/` (782 GB free on `/home`).

## Residuals / to-verify

- `to-verify`: a symlinked component path — a component path that is a symlink to a dangling target (expect `missing component`, exit 2, same as `io/component-path-is-directory`) and to a file outside the repo (expect its bytes to be parsed like any other input; the assembler has no path-containment check, unlike `check-evidence-coupling.py`). Not exercised here; no receipt exists either way, and no claim is made.
- `to-verify`: the behaviour of `--selftest` when *every* temp-dir candidate is unusable (this needs an environment where `TMPDIR`, `/tmp`, `/var/tmp` and `/usr/tmp` all fail, which cannot be arranged without root). The single-candidate failure above is the measured receipt.
- The `--selftest` coverage itself (fixture negatives, gate replay) is *not* re-audited here; R9-D03 owns `--selftest` evidence for the coupling guard, R9-D01 owns the delivered-tree `--check` diagnosis. This fragment contributes the negative-input envelope only.
- Not tested: non-UTF-8 encodings other than UTF-8-with-BOM and invalid UTF-8 bytes (e.g. UTF-16 component files) — `json.loads` is fed decoded UTF-8 text only, so a UTF-16 file is expected to fail as `invalid JSON` or `not valid UTF-8`; no receipt.

## Reproduction

Battery (outside the repo, so the repo's tools digest list stays valid):

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
python3 /home/vgpnk/.cache/r9-d05/cli_negatives_v2.py | python3 -m json.tool | head -40
```

Headline single case, by hand (bad JSON in `06-material.json`, driven from a copy):

```bash
T=$(mktemp -d -p /home/vgpnk/.cache/r9-d05)
mkdir -p "$T/tools" "$T/examples/culture-d3/components"
cp tools/assemble-culture-d3.py tools/assemble-d2.py "$T/tools/"
cp examples/culture-d3/components/*.json "$T/examples/culture-d3/components/"
printf '{"eras": [' > "$T/examples/culture-d3/components/06-material.json"
cd "$T" && python3 tools/assemble-culture-d3.py ; echo "exit=$?"   # exit=2, "assembly error: 06-material.json: invalid JSON (…)"
```

The full harness (`/home/vgpnk/.cache/r9-d05/cli_negatives_v2.py`) is scratch, outside the repo, and may be cleaned up; the mutation catalogue above plus the two commands are enough to rebuild any case by hand. Every number in this fragment carries the command that produced it, as required by the corpus rules.
