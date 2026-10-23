# Claim-O residual mutation probe — MutateBareNumeric57

## Findings

- **No contract defect found in this probe.** Seven independent one-line mutants (all six requested classes, plus broad report-without-decoding) were **killed by both `--selftest` and the unchanged full ACCEPT-O-57 predicate**. Overall survivors: **none**; scored inconclusive mutants: **none**.
- **Informational coverage boundary:** M4 (bare references reported but not decoded) prints `GEN PASS lessons=5 failing=0 []` and `REAL PASS lessons=3 failing=0 []`, but the same acceptance run prints `SELFTEST FAIL exit=1 SELFTEST: 48/52 pass` and `ACCEPT-O-57: FAIL` (exit **1**). Thus its standalone input/output legs do not detect that defect; the selftest-based legs do. This is not a survivor of either requested detector.
- **Harness correction, not a mutant kill:** the first pristine acceptance attempt exited **2** with `ACCEPT_O_INPUT_ERROR ... [Errno 11] Resource temporarily unavailable` because an initial per-UID process limit of 64 was below existing host usage. That attempt is retained below as **inconclusive**. Before any mutation, the limit was corrected uniformly to 2,623 (2,111 observed user tasks + 512), and every mutant received passing pristine and restored runs under that same corrected bound.

## Verdict

**Agree with the landed claim O within these seven mutation probes. Required fixes: none.** No predicate, contract, lane source, caller, documentation or test was edited. The M4 coverage observation does not change the frozen predicate or the verdict.

## Scope, axes and bounds

- Axes: detector sensitivity, defect isolation, exact-byte restoration, bounded resource use.
- Tested landed commit: `43f1e781d8bd382241f5e0eb8a8761e8bcb128bc`, detached in the isolated shared-object clone below; no source-lane git writes.
- Scratch clone: `/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/lane`.
- Mutated target: `/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/lane/tools/check-gate-quotes.py` (one line at a time; each fully restored before the next baseline).
- Acceptance instrument: `/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/lane/reports/round-57/accept-o.py`; sha256 `efd2276744538b4e4807084901d556c269d23df2b426a28909afc3c4093fa48b` throughout. Its bytes match the source lane instrument.
- Every acceptance invocation ran **without `--seed`**. The captured fresh random seeds are in the actual stdout transcripts.
- Per-child bounds: 55-second detector timeout, 30 CPU seconds, 512 MiB address space, 2,623 per-UID tasks, 128 open files, zero core size; native library thread counts set to 1. The harness runs sequentially, with no background jobs, delegation or external-runtime calls. The counter itself invokes one tool child at a time.
- Tools installed or updated: **none**.

## Commands (same argv for pristine, mutated and restored)

Working directory: `/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/lane`.

```sh
python3 -B /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/lane/tools/check-gate-quotes.py --selftest
python3 -B reports/round-57/accept-o.py --tool /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/lane/tools/check-gate-quotes.py
```

Exit 0 on pristine/restored and exit 1 on the mutant is counted as a kill; baseline failure, timeout, input error or restoration failure is inconclusive, never a kill.

## Per-mutant results

| Mutant | Source line | `--selftest` mutant output / exit | Full acceptance mutant exit | Failing acceptance legs | Verdicts |
|---|---:|---|---:|---|---|
| M1-decimal-requires-semicolon | 111 | `SELFTEST: 50/52 pass` / 1 | 1 | GEN, REAL, MUTANTS, SELFTEST | KILLED / KILLED |
| M2-hex-requires-semicolon | 111 | `SELFTEST: 50/52 pass` / 1 | 1 | GEN, REAL, MUTANTS, SELFTEST | KILLED / KILLED |
| M3-decode-bare-without-reporting | 123 | `SELFTEST: 48/52 pass` / 1 | 1 | GEN, REAL, MUTANTS, SELFTEST | KILLED / KILLED |
| M4-report-bare-without-decoding | 124 | `SELFTEST: 48/52 pass` / 1 | 1 | MUTANTS, SELFTEST | KILLED / KILLED |
| M5-named-without-semicolon | 111 | `SELFTEST: 51/52 pass` / 1 | 1 | GEN, MUTANTS, SELFTEST | KILLED / KILLED |
| M6-empty-decimal-is-reference | 111 | `SELFTEST: 51/52 pass` / 1 | 1 | GEN, MUTANTS, SELFTEST | KILLED / KILLED |
| M7-report-all-without-decoding | 124 | `SELFTEST: 41/52 pass` / 1 | 1 | GEN, MUTANTS, SELFTEST | KILLED / KILLED |

**Survivors:** selftest: none; full acceptance: none. Every pristine/restored run exited 0 in both detectors; all seven acceptance legs passed on every pristine/restored run.

## Exact mutations and expected detectors

### M1-decimal-requires-semicolon

Location: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py:111` (mutation applied only to the isolated scratch copy).

Drop the optional-semicolon marker only on decimal numerics.

Replacement line:

```python
HTML_REFERENCE = re.compile(r"&(?:#[0-9]+;|#[xX][0-9A-Fa-f]+;?|[A-Za-z][A-Za-z0-9]*;)")
```

Expected detector: numeric-decimal-bare-before-space / numeric-decimal-bare-before-letter; GEN and REAL missing html-entity.

### M2-hex-requires-semicolon

Location: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py:111` (mutation applied only to the isolated scratch copy).

Drop the optional-semicolon marker only on hexadecimal numerics.

Replacement line:

```python
HTML_REFERENCE = re.compile(r"&(?:#[0-9]+;?|#[xX][0-9A-Fa-f]+;|[A-Za-z][A-Za-z0-9]*;)")
```

Expected detector: numeric-hex-bare-before-space / numeric-hex-bare-before-nonhex; GEN and REAL missing html-entity.

### M3-decode-bare-without-reporting

Location: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py:123` (mutation applied only to the isolated scratch copy).

Decode bare numeric references, but set the reporting flag only for semicolon-terminated references.

Replacement line:

```python
            found = found or reference.endswith(";")
```

Expected detector: All four bare-numeric decoded-value/flag cases; GEN and REAL missing html-entity.

### M4-report-bare-without-decoding

Location: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py:124` (mutation applied only to the isolated scratch copy).

Report bare numeric references, but do not decode them; semicolon-terminated references still decode.

Replacement line:

```python
            return html.unescape(reference) if reference.endswith(";") else reference
```

Expected detector: All four bare-numeric decoded-value/flag cases. The full acceptance predicate must reject through SELFTEST/MUTANTS; GEN/REAL need not reject letter-only references.

### M5-named-without-semicolon

Location: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py:111` (mutation applied only to the isolated scratch copy).

Make the named-reference closing semicolon optional, admitting legacy HTML5 names such as &copy.

Replacement line:

```python
HTML_REFERENCE = re.compile(r"&(?:#[0-9]+;?|#[xX][0-9A-Fa-f]+;?|[A-Za-z][A-Za-z0-9]*;?)")
```

Expected detector: named-reference-requires-semicolon; GEN named-no-semicolon row has an extra html-entity.

### M6-empty-decimal-is-reference

Location: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py:111` (mutation applied only to the isolated scratch copy).

Add precisely &#; to the recognized grammar (no other malformed-numeric or numeric-semicolon changes).

Replacement line:

```python
HTML_REFERENCE = re.compile(r"&(?:#[0-9]+;?|#;|#[xX][0-9A-Fa-f]+;?|[A-Za-z][A-Za-z0-9]*;)")
```

Expected detector: malformed-decimal-reference; GEN bare-ampersand row has an extra html-entity.

### M7-report-all-without-decoding

Location: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py:124` (mutation applied only to the isolated scratch copy).

Additional broad report-without-decoding mutant: replace decoding with returning the reference unchanged.

Replacement line:

```python
            return reference
```

Expected detector: Decoded numeric/codepoint value checks and downstream quote-rule cases; GEN loses words=<n> and truncated-grounds findings.

## Before / mutated / restored SHA-256

Pristine and restored byte arrays were compared directly, not merely by hash. Each matched exactly.

| Mutant | Before | Mutated | Restored |
|---|---|---|---|
| M1-decimal-requires-semicolon | `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` | `adb075f058f4bd2aa779d16536f4972655ccc3e8b51613b00311ba812c5fb9c0` | `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` |
| M2-hex-requires-semicolon | `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` | `8de098b6d43d99ada90c1dd4fe0792eb2d317146319cce8d54e930035a2560d5` | `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` |
| M3-decode-bare-without-reporting | `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` | `bd589a461d8276ebaf4e67ddc8043d94ba93a8800e9f2e79dafeacd81e6ee264` | `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` |
| M4-report-bare-without-decoding | `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` | `8ba87964490291f7043d73ac598fdea7d27d7a28019eef8a7e44f7bcbbd0fb30` | `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` |
| M5-named-without-semicolon | `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` | `4522e1ca8461d5f459644e8f1393b07f650f4bf9b83e2de0b348a4bef02dbed8` | `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` |
| M6-empty-decimal-is-reference | `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` | `aa752347689c7cf086afe89e02c2ee7e8fb98283bcd04b402c6538d330ad5a48` | `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` |
| M7-report-all-without-decoding | `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` | `16939da22cdfafd0946980f3080fe2ddd6cae19ee29e9c85d51e6d5d1538148d` | `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` |

Final scratch tool equals the original immutable in-memory byte array: **true**.

Source lane files, read only and never edited:

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py` — `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7` (same as initial read).
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/accept-o.py` — `efd2276744538b4e4807084901d556c269d23df2b426a28909afc3c4093fa48b` (same as initial read).

## Actual detector outputs

Complete captured stdout and stderr follow, without omitted passing tests or truncated long diagnostic lines. Commands are exactly those above; each block records phase, exit and tool hash. Temporary paths in the outputs refer only to scratch fixtures.

### M1-decimal-requires-semicolon — pristine

Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.

#### selftest: exit 0; elapsed 0.145s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-czefal31/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-czefal31/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-czefal31/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-czefal31/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 0; elapsed 4.578s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [511052029, 511052030, 511052031, 511052032, 511052033] real-seeds [511052129, 511052130, 511052131]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

stderr:

```text
(empty)
```


### M1-decimal-requires-semicolon — mutated

Tool SHA-256: `adb075f058f4bd2aa779d16536f4972655ccc3e8b51613b00311ba812c5fb9c0`.

#### selftest: exit 1; elapsed 0.153s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
FAIL numeric-decimal-bare-before-space want=('é ', True) got=('&#233 ', False)
FAIL numeric-decimal-bare-before-letter want=('éw', True) got=('&#233w', False)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-5mfshzod/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-5mfshzod/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-5mfshzod/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-5mfshzod/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 50/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 1; elapsed 5.012s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 adb075f058f4bd2aa779d16536f4972655ccc3e8b51613b00311ba812c5fb9c0
# seeds [1903293243, 1903293244, 1903293245, 1903293246, 1903293247] real-seeds [1903293343, 1903293344, 1903293345]
GEN FAIL lessons=5 failing=5 ["seed=1903293243 exit=1 missing=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-0gjuhfty/tmp55fni5ni/lessons/survival-88.md', 7, 'S862', 'html-entity')] extra=[]", "seed=1903293244 exit=1 missing=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-0gjuhfty/tmpt300by37/lessons/acknowledged-38.md', 8, 'S649', 'html-entity')] extra=[]"]
REAL FAIL lessons=3 failing=3 ["seed=1903293343 exit=1 missing=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-0gjuhfty/tmpr6w9y97n/lessons/duplicates-24.md', 55, 'S390', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-0gjuhfty/tmpr6w9y97n/lessons/duplicates-24.md', 64, 'S399', 'html-entity')] extra=[]", "seed=1903293344 exit=1 missing=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-0gjuhfty/tmpu8pa66xk/lessons/filhos-24.md', 31, 'S366', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-0gjuhfty/tmpu8pa66xk/lessons/filhos-24.md', 56, 'S391', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-0gjuhfty/tmpu8pa66xk/lessons/filhos-24.md', 69, 'S404', 'html-entity')] extra=[]"]
MULTI PASS runs=10 failing=[]
MUTANTS FAIL unmutated_selftest_exit=1 survivors=[] neutral_failing=['neutral-decode', 'neutral-check', 'neutral-run'] unpatched=[] exits={'none': 1, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 1, 'neutral-check': 1, 'neutral-run': 1}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST FAIL exit=1 SELFTEST: 50/52 pass
ACCEPT-O-57: FAIL
```

stderr:

```text
(empty)
```


### M1-decimal-requires-semicolon — restored

Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.

#### selftest: exit 0; elapsed 0.558s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-zninlk_l/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-zninlk_l/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-zninlk_l/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-zninlk_l/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 0; elapsed 8.045s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [3868854547, 3868854548, 3868854549, 3868854550, 3868854551] real-seeds [3868854647, 3868854648, 3868854649]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

stderr:

```text
(empty)
```


### M2-hex-requires-semicolon — pristine

Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.

#### selftest: exit 0; elapsed 0.284s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-_j0vofj3/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-_j0vofj3/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-_j0vofj3/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-_j0vofj3/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 0; elapsed 7.017s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [2895212634, 2895212635, 2895212636, 2895212637, 2895212638] real-seeds [2895212734, 2895212735, 2895212736]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

stderr:

```text
(empty)
```


### M2-hex-requires-semicolon — mutated

Tool SHA-256: `8de098b6d43d99ada90c1dd4fe0792eb2d317146319cce8d54e930035a2560d5`.

#### selftest: exit 1; elapsed 0.132s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
FAIL numeric-hex-bare-before-space want=('é ', True) got=('&#xE9 ', False)
FAIL numeric-hex-bare-before-nonhex want=('éz', True) got=('&#xE9z', False)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-ksl5buwr/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-ksl5buwr/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-ksl5buwr/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-ksl5buwr/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 50/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 1; elapsed 5.032s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 8de098b6d43d99ada90c1dd4fe0792eb2d317146319cce8d54e930035a2560d5
# seeds [3549845035, 3549845036, 3549845037, 3549845038, 3549845039] real-seeds [3549845135, 3549845136, 3549845137]
GEN FAIL lessons=5 failing=5 ["seed=3549845035 exit=1 missing=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-5n43g32r/tmps7skf_zy/lessons/existence-27.md', 5, 'S697', 'html-entity')] extra=[]", "seed=3549845036 exit=1 missing=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-5n43g32r/tmpiggk6gu0/lessons/belonging-35.md', 6, 'S613', 'html-entity')] extra=[]"]
REAL FAIL lessons=3 failing=3 ["seed=3549845135 exit=1 missing=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-5n43g32r/tmpksl0uxvn/lessons/flesh-30.md', 24, 'S359', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-5n43g32r/tmpksl0uxvn/lessons/flesh-30.md', 37, 'S372', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-5n43g32r/tmpksl0uxvn/lessons/flesh-30.md', 60, 'S395', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-5n43g32r/tmpksl0uxvn/lessons/flesh-30.md', 67, 'S402', 'html-entity')] extra=[]", "seed=3549845136 exit=1 missing=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-5n43g32r/tmp4xhj2kph/lessons/todas-64.md', 36, 'S371', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-5n43g32r/tmp4xhj2kph/lessons/todas-64.md', 56, 'S391', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-5n43g32r/tmp4xhj2kph/lessons/todas-64.md', 59, 'S394', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-5n43g32r/tmp4xhj2kph/lessons/todas-64.md', 66, 'S401', 'html-entity')] extra=[]"]
MULTI PASS runs=10 failing=[]
MUTANTS FAIL unmutated_selftest_exit=1 survivors=[] neutral_failing=['neutral-decode', 'neutral-check', 'neutral-run'] unpatched=[] exits={'none': 1, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 1, 'neutral-check': 1, 'neutral-run': 1}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST FAIL exit=1 SELFTEST: 50/52 pass
ACCEPT-O-57: FAIL
```

stderr:

```text
(empty)
```


### M2-hex-requires-semicolon — restored

Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.

#### selftest: exit 0; elapsed 0.102s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-wvahypoa/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-wvahypoa/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-wvahypoa/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-wvahypoa/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 0; elapsed 3.98s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [3153554385, 3153554386, 3153554387, 3153554388, 3153554389] real-seeds [3153554485, 3153554486, 3153554487]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

stderr:

```text
(empty)
```


### M3-decode-bare-without-reporting — pristine

Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.

#### selftest: exit 0; elapsed 0.079s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-ytshirt_/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-ytshirt_/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-ytshirt_/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-ytshirt_/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 0; elapsed 4.278s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [1266269733, 1266269734, 1266269735, 1266269736, 1266269737] real-seeds [1266269833, 1266269834, 1266269835]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

stderr:

```text
(empty)
```


### M3-decode-bare-without-reporting — mutated

Tool SHA-256: `bd589a461d8276ebaf4e67ddc8043d94ba93a8800e9f2e79dafeacd81e6ee264`.

#### selftest: exit 1; elapsed 0.305s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
FAIL numeric-decimal-bare-before-space want=('é ', True) got=('é ', False)
FAIL numeric-decimal-bare-before-letter want=('éw', True) got=('éw', False)
FAIL numeric-hex-bare-before-space want=('é ', True) got=('é ', False)
FAIL numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', False)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-wkkpdbg6/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-wkkpdbg6/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-wkkpdbg6/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-wkkpdbg6/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 48/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 1; elapsed 3.667s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 bd589a461d8276ebaf4e67ddc8043d94ba93a8800e9f2e79dafeacd81e6ee264
# seeds [2138311811, 2138311812, 2138311813, 2138311814, 2138311815] real-seeds [2138311911, 2138311912, 2138311913]
GEN FAIL lessons=5 failing=5 ["seed=2138311811 exit=1 missing=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmppowyyzho/lessons/reconciled-20.md', 6, 'S602', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmppowyyzho/lessons/reconciled-20.md', 7, 'S542', 'html-entity')] extra=[]", "seed=2138311812 exit=1 missing=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmpj2q95c63/lessons/execution-79.md', 9, 'S533', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmpj2q95c63/lessons/execution-79.md', 12, 'S722', 'html-entity')] extra=[]"]
REAL FAIL lessons=3 failing=3 ["seed=2138311911 exit=0 missing=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmpddskc4hh/lessons/identify-93.md', 33, 'S368', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmpddskc4hh/lessons/identify-93.md', 54, 'S389', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmpddskc4hh/lessons/identify-93.md', 56, 'S391', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmpddskc4hh/lessons/identify-93.md', 60, 'S395', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmpddskc4hh/lessons/identify-93.md', 74, 'S409', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmpddskc4hh/lessons/identify-93.md', 75, 'S410', 'html-entity')] extra=[]", "seed=2138311912 exit=0 missing=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmpwjwn9lnj/lessons/pdf-77.md', 28, 'S363', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmpwjwn9lnj/lessons/pdf-77.md', 31, 'S366', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmpwjwn9lnj/lessons/pdf-77.md', 53, 'S388', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmpwjwn9lnj/lessons/pdf-77.md', 54, 'S389', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmpwjwn9lnj/lessons/pdf-77.md', 69, 'S404', 'html-entity'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-9xbcxfsd/tmpwjwn9lnj/lessons/pdf-77.md', 76, 'S411', 'html-entity')] extra=[]"]
MULTI PASS runs=10 failing=[]
MUTANTS FAIL unmutated_selftest_exit=1 survivors=[] neutral_failing=['neutral-decode', 'neutral-check', 'neutral-run'] unpatched=[] exits={'none': 1, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 1, 'neutral-check': 1, 'neutral-run': 1}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST FAIL exit=1 SELFTEST: 48/52 pass
ACCEPT-O-57: FAIL
```

stderr:

```text
(empty)
```


### M3-decode-bare-without-reporting — restored

Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.

#### selftest: exit 0; elapsed 0.101s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-5eoq90se/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-5eoq90se/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-5eoq90se/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-5eoq90se/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 0; elapsed 3.361s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [1729239550, 1729239551, 1729239552, 1729239553, 1729239554] real-seeds [1729239650, 1729239651, 1729239652]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

stderr:

```text
(empty)
```


### M4-report-bare-without-decoding — pristine

Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.

#### selftest: exit 0; elapsed 0.058s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-nlig40uv/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-nlig40uv/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-nlig40uv/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-nlig40uv/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 0; elapsed 3.42s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [3792378018, 3792378019, 3792378020, 3792378021, 3792378022] real-seeds [3792378118, 3792378119, 3792378120]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

stderr:

```text
(empty)
```


### M4-report-bare-without-decoding — mutated

Tool SHA-256: `8ba87964490291f7043d73ac598fdea7d27d7a28019eef8a7e44f7bcbbd0fb30`.

#### selftest: exit 1; elapsed 0.049s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
FAIL numeric-decimal-bare-before-space want=('é ', True) got=('&#233 ', True)
FAIL numeric-decimal-bare-before-letter want=('éw', True) got=('&#233w', True)
FAIL numeric-hex-bare-before-space want=('é ', True) got=('&#xE9 ', True)
FAIL numeric-hex-bare-before-nonhex want=('éz', True) got=('&#xE9z', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-iv6dzpye/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-iv6dzpye/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-iv6dzpye/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-iv6dzpye/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 48/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 1; elapsed 1.718s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 8ba87964490291f7043d73ac598fdea7d27d7a28019eef8a7e44f7bcbbd0fb30
# seeds [3584436397, 3584436398, 3584436399, 3584436400, 3584436401] real-seeds [3584436497, 3584436498, 3584436499]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS FAIL unmutated_selftest_exit=1 survivors=[] neutral_failing=['neutral-decode', 'neutral-check', 'neutral-run'] unpatched=[] exits={'none': 1, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 1, 'neutral-check': 1, 'neutral-run': 1}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST FAIL exit=1 SELFTEST: 48/52 pass
ACCEPT-O-57: FAIL
```

stderr:

```text
(empty)
```


### M4-report-bare-without-decoding — restored

Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.

#### selftest: exit 0; elapsed 0.096s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-a6wqqhdn/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-a6wqqhdn/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-a6wqqhdn/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-a6wqqhdn/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 0; elapsed 3.061s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [2821825088, 2821825089, 2821825090, 2821825091, 2821825092] real-seeds [2821825188, 2821825189, 2821825190]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

stderr:

```text
(empty)
```


### M5-named-without-semicolon — pristine

Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.

#### selftest: exit 0; elapsed 0.077s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-cuij4z3i/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-cuij4z3i/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-cuij4z3i/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-cuij4z3i/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 0; elapsed 3.033s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [200344591, 200344592, 200344593, 200344594, 200344595] real-seeds [200344691, 200344692, 200344693]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

stderr:

```text
(empty)
```


### M5-named-without-semicolon — mutated

Tool SHA-256: `4522e1ca8461d5f459644e8f1393b07f650f4bf9b83e2de0b348a4bef02dbed8`.

#### selftest: exit 1; elapsed 0.101s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
FAIL named-reference-requires-semicolon want=('&copy ', False) got=('© ', True)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-x1sxsfnv/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-x1sxsfnv/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-x1sxsfnv/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-x1sxsfnv/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 51/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 1; elapsed 2.631s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 4522e1ca8461d5f459644e8f1393b07f650f4bf9b83e2de0b348a4bef02dbed8
# seeds [3542509270, 3542509271, 3542509272, 3542509273, 3542509274] real-seeds [3542509370, 3542509371, 3542509372]
GEN FAIL lessons=5 failing=5 ["seed=3542509270 exit=1 missing=[] extra=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-_tle9jt0/tmprko_bbz3/lessons/jobs-62.md', 10, 'S518', 'html-entity')]", "seed=3542509271 exit=1 missing=[] extra=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-_tle9jt0/tmpztx5xtf1/lessons/page-82.md', 8, 'S981', 'html-entity')]"]
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS FAIL unmutated_selftest_exit=1 survivors=[] neutral_failing=['neutral-decode', 'neutral-check', 'neutral-run'] unpatched=[] exits={'none': 1, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 1, 'neutral-check': 1, 'neutral-run': 1}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST FAIL exit=1 SELFTEST: 51/52 pass
ACCEPT-O-57: FAIL
```

stderr:

```text
(empty)
```


### M5-named-without-semicolon — restored

Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.

#### selftest: exit 0; elapsed 0.112s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-1xmtuixt/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-1xmtuixt/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-1xmtuixt/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-1xmtuixt/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 0; elapsed 4.012s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [2908926988, 2908926989, 2908926990, 2908926991, 2908926992] real-seeds [2908927088, 2908927089, 2908927090]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

stderr:

```text
(empty)
```


### M6-empty-decimal-is-reference — pristine

Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.

#### selftest: exit 0; elapsed 0.149s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-8kleo00j/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-8kleo00j/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-8kleo00j/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-8kleo00j/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 0; elapsed 2.553s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [3106046336, 3106046337, 3106046338, 3106046339, 3106046340] real-seeds [3106046436, 3106046437, 3106046438]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

stderr:

```text
(empty)
```


### M6-empty-decimal-is-reference — mutated

Tool SHA-256: `aa752347689c7cf086afe89e02c2ee7e8fb98283bcd04b402c6538d330ad5a48`.

#### selftest: exit 1; elapsed 0.068s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
FAIL malformed-decimal-reference want=('&#;', False) got=('&#;', True)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-f7j6wn2k/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-f7j6wn2k/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-f7j6wn2k/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-f7j6wn2k/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 51/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 1; elapsed 2.357s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 aa752347689c7cf086afe89e02c2ee7e8fb98283bcd04b402c6538d330ad5a48
# seeds [647850868, 647850869, 647850870, 647850871, 647850872] real-seeds [647850968, 647850969, 647850970]
GEN FAIL lessons=5 failing=5 ["seed=647850868 exit=1 missing=[] extra=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-5m2revyh/tmpq2wgz4ok/lessons/draft-51.md', 12, 'S930', 'html-entity')]", "seed=647850869 exit=1 missing=[] extra=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-5m2revyh/tmp6s92zo34/lessons/desert-58.md', 19, 'S608', 'html-entity')]"]
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS FAIL unmutated_selftest_exit=1 survivors=[] neutral_failing=['neutral-decode', 'neutral-check', 'neutral-run'] unpatched=[] exits={'none': 1, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 1, 'neutral-check': 1, 'neutral-run': 1}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST FAIL exit=1 SELFTEST: 51/52 pass
ACCEPT-O-57: FAIL
```

stderr:

```text
(empty)
```


### M6-empty-decimal-is-reference — restored

Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.

#### selftest: exit 0; elapsed 0.109s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-gorybokr/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-gorybokr/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-gorybokr/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-gorybokr/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 0; elapsed 2.375s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [1109147439, 1109147440, 1109147441, 1109147442, 1109147443] real-seeds [1109147539, 1109147540, 1109147541]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

stderr:

```text
(empty)
```


### M7-report-all-without-decoding — pristine

Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.

#### selftest: exit 0; elapsed 0.048s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-4v63wdjj/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-4v63wdjj/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-4v63wdjj/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-4v63wdjj/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 0; elapsed 1.623s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [2197578010, 2197578011, 2197578012, 2197578013, 2197578014] real-seeds [2197578110, 2197578111, 2197578112]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

stderr:

```text
(empty)
```


### M7-report-all-without-decoding — mutated

Tool SHA-256: `16939da22cdfafd0946980f3080fe2ddd6cae19ee29e9c85d51e6d5d1538148d`.

#### selftest: exit 1; elapsed 0.099s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
FAIL numeric-decimal-bare-before-space want=('é ', True) got=('&#233 ', True)
FAIL numeric-decimal-bare-before-letter want=('éw', True) got=('&#233w', True)
FAIL numeric-hex-bare-before-space want=('é ', True) got=('&#xE9 ', True)
FAIL numeric-hex-bare-before-nonhex want=('éz', True) got=('&#xE9z', True)
FAIL invalid-zero-codepoint want=('�', True) got=('&#0;', True)
FAIL invalid-surrogate-codepoint want=('�', True) got=('&#xD800;', True)
FAIL invalid-out-of-range-codepoint want=('�', True) got=('&#1114112;', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
FAIL decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
FAIL decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
FAIL decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity
FAIL decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-yvbacjzd/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-yvbacjzd/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-yvbacjzd/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-yvbacjzd/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 41/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 1; elapsed 2.53s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 16939da22cdfafd0946980f3080fe2ddd6cae19ee29e9c85d51e6d5d1538148d
# seeds [1151278158, 1151278159, 1151278160, 1151278161, 1151278162] real-seeds [1151278258, 1151278259, 1151278260]
GEN FAIL lessons=5 failing=5 ["seed=1151278158 exit=1 missing=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-zyb5hwdy/tmphw97g6gx/lessons/provider-12.md', 10, 'S707', 'words=28'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-zyb5hwdy/tmphw97g6gx/lessons/provider-12.md', 12, 'S220', 'truncated-grounds')] extra=[]", "seed=1151278159 exit=1 missing=[('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-zyb5hwdy/tmpiswn7him/lessons/cargo-79.md', 14, 'S779', 'words=27'), ('/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-zyb5hwdy/tmpiswn7him/lessons/cargo-79.md', 16, 'S719', 'truncated-grounds')] extra=[]"]
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS FAIL unmutated_selftest_exit=1 survivors=[] neutral_failing=['neutral-decode', 'neutral-check', 'neutral-run'] unpatched=[] exits={'none': 1, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 1, 'neutral-check': 1, 'neutral-run': 1}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST FAIL exit=1 SELFTEST: 41/52 pass
ACCEPT-O-57: FAIL
```

stderr:

```text
(empty)
```


### M7-report-all-without-decoding — restored

Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`.

#### selftest: exit 0; elapsed 0.252s

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-kngp121k/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-kngp121k/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-kngp121k/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-kngp121k/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

#### accept-o: exit 0; elapsed 4.211s

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [3833904327, 3833904328, 3833904329, 3833904330, 3833904331] real-seeds [3833904427, 3833904428, 3833904429]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

stderr:

```text
(empty)
```

## Retained initial inconclusive harness attempt

This preceded every mutation and was excluded from all kill counts. Tool SHA-256: `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`. Initial `RLIMIT_NPROC=64`; all subsequent runs used 2,623.

### selftest: exit 0

stdout:

```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS numeric-decimal-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-decimal-bare-before-letter want=('éw', True) got=('éw', True)
PASS numeric-hex-bare-before-space want=('é ', True) got=('é ', True)
PASS numeric-hex-bare-before-nonhex want=('éz', True) got=('éz', True)
PASS invalid-zero-codepoint want=('�', True) got=('�', True)
PASS invalid-surrogate-codepoint want=('�', True) got=('�', True)
PASS invalid-out-of-range-codepoint want=('�', True) got=('�', True)
PASS malformed-decimal-reference want=('&#;', False) got=('&#;', False)
PASS malformed-hex-reference-empty want=('&#x;', False) got=('&#x;', False)
PASS malformed-hex-reference-nondigit want=('&#xg', False) got=('&#xg', False)
PASS named-reference-requires-semicolon want=('&copy ', False) got=('&copy ', False)
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
PASS truncated-grounds-shorter-not-prefix-green want=none got=none
PASS doubled-locator-single-span-green want=none got=none
PASS doubled-locator-wayback-note-red want=doubled-locator got=doubled-locator
PASS html-entity-named-red want=html-entity got=html-entity
PASS html-entity-once-per-row want=('html-entity',) got=html-entity
PASS double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity
PASS html-entity-bare-ampersands-green want=none got=none
PASS decoded-truncated-grounds-red want=('html-entity', 'truncated-grounds') got=html-entity,truncated-grounds
PASS decoded-whole-grounds-green want=('html-entity',) got=html-entity
PASS decoded-quote-marks-over-cap-red want=('html-entity', 'over-cap') got=html-entity,over-cap
PASS decoded-quote-marks-short-green want=('html-entity',) got=html-entity
PASS decoded-ellipsis-red want=('html-entity', 'ellipsis-joined') got=html-entity,ellipsis-joined
PASS decoded-doubled-locator-red want=('html-entity', 'doubled-locator') got=html-entity,doubled-locator
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-q9xsdtit/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-q9xsdtit/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-q9xsdtit/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/check-gate-quotes-selftest-q9xsdtit/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

stderr:

```text
(empty)
```

### accept-o: exit 2

stdout:

```text
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [1895820288, 1895820289, 1895820290, 1895820291, 1895820292] real-seeds [1895820388, 1895820389, 1895820390]
```

stderr:

```text
ACCEPT_O_INPUT_ERROR /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/lane/tools/check-gate-quotes.py /fast/scratch/hyaku/kotodama-r57/MutateBareNumeric57/gq-78tkyagn/tmpe8nigff5/lessons/substitute-51.md [Errno 11] Resource temporarily unavailable
```
