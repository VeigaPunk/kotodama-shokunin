# Round 57 residual falsify — rerun ACCEPT-O-57 (agent KotodamaR57.RerunAcceptO57)

Date: 2026-10-22. Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin (HEAD `78d83b5`). Claim O land: `43f1e781d8bd382241f5e0eb8a8761e8bcb128bc`.

## Method / canonical runtime

- Fresh clone: `git clone /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r57/RerunAcceptO57/clone`, then `git checkout --detach 43f1e781` → `rev-parse HEAD` = `43f1e781d8bd382241f5e0eb8a8761e8bcb128bc`. `git status --porcelain` empty throughout between mutants.
- `sha256sum tools/check-gate-quotes.py` in the clone = `54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7`, byte-identical to the hash accept-o itself prints (`# tool tools/check-gate-quotes.py sha256 54981859…`).
- Drift check: `git diff --stat 43f1e781..HEAD -- tools/check-gate-quotes.py reports/round-57/accept-o.py` in the lane → empty (no drift in either claim-O file since the land).
- GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE were unset (`env -u`) for every git invocation. No git writes in the lane; sandbox git only in the clone. No installs performed. No lsp device in this leaf; text grep used as literal fallback and labelled as such.

## Findings

**None actionable.** Every measured leg of the landed claim O state behaved as claimed:

1. ACCEPT-O-57 (frozen predicate, run WITHOUT --seed, three independent runs): PASS, exit 0 each run, on distinct random seeds each time (seeds printed per run below).
2. Unmutated `--selftest`: exit 0, `SELFTEST: 52/52 pass`.
3. All three canonical mutants (applied as SOURCE EDITS to the clone's `tools/check-gate-quotes.py`, tested in isolation, reverted after each — sha256 restored to `54981859…` after every revert):
   - double-decode in `decode_html_references` (line 127 `return HTML_REFERENCE.sub(decode, HTML_REFERENCE.sub(decode, line)), found`) → selftest FAIL `51/52`, exit 1.
   - stop-after-first-unreadable in `check` (lines 320/323 `continue` → `break` in both unreadable branches) → selftest FAIL `51/52`, exit 1.
   - label-rename in `run` (line 349 added: `detail = "html_entity" if detail == "html-entity" else detail`) → selftest FAIL `50/52`, exit 1.
4. Introspection grep of the landed file (`/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py`, whole file including selftest lines 363–580): pattern `\bdis\b|\binspect\b|\bhashlib\b|__code__|co_consts|__file__` → **zero matches**. The selftest kills by input/output behaviour only; the grep result is text evidence, not semantic proof (no lsp server in this leaf).

## Outputs (verbatim)

### accept-o, run 1 — `python3 -B reports/round-57/accept-o.py` (no --seed), exit=0

```
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [529197933, 529197934, 529197935, 529197936, 529197937] real-seeds [529198033, 529198034, 529198035]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

### accept-o, run 2 — exit=0

```
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [3426233305, 3426233306, 3426233307, 3426233308, 3426233309] real-seeds [3426233405, 3426233406, 3426233407]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

### accept-o, run 3 — exit=0

```
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [187976393, 187976394, 187976395, 187976396, 187976397] real-seeds [187976493, 187976494, 187976495]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
```

### `python3 -B tools/check-gate-quotes.py --selftest`, unmutated — exit=0

```
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
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /tmp/check-gate-quotes-selftest-jbcnh7wf/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/tmp/check-gate-quotes-selftest-jbcnh7wf/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/tmp/check-gate-quotes-selftest-jbcnh7wf/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /tmp/check-gate-quotes-selftest-jbcnh7wf/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
```

### Mutant 1 — double-decode (`clone/tools/check-gate-quotes.py:127` → `return HTML_REFERENCE.sub(decode, HTML_REFERENCE.sub(decode, line)), found`) — exit=1

Diff from unmutated output (all other 51 cases identical PASS):

```
FAIL double-encoded-ellipsis-decoded-once want=('html-entity',) got=html-entity,ellipsis-joined
SELFTEST: 51/52 pass
exit=1
```

### Mutant 2 — stop-at-first-bad-file (`check`, lines 320 and 323 `continue` → `break`) — exit=1, stderr empty

```
… (cases short-quote through utf8-valid-green: identical PASS, 50 lines)
PASS utf8-invalid-red want=error-exit-2 got=GATE_QUOTES_ERROR: /tmp/check-gate-quotes-selftest-6ypu561c/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)
PASS utf8-valid-green want=exit-0 got=0
PASS behavioural-entity-label want=html-entity got=['/tmp/check-gate-quotes-selftest-6ypu561c/entity.md:5 S901 html-entity', 'GATE_QUOTES: 1 findings']
FAIL behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, 'GATE_QUOTES: 0 findings\n', "GATE_QUOTES_ERROR: /tmp/check-gate-quotes-selftest-6ypu561c/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 51/52 pass
exit=1
```

(The stop-at-first mutant is caught because `run([invalid, valid])` then emits zero findings: the checker stopped at the first unreadable path, so the valid lesson's findings vanished from stdout.)

Capture note, recorded honestly: the first M2 invocation's harness capture ended after `utf8-valid-green` with `exit=1` and no trailing lines; the rerun above with both streams captured via `subprocess(capture_output=True)` shows the complete 52-case output and empty stderr. Same source mutant both times; the truncation was a capture artifact of the first shell, not tool behaviour.

### Mutant 3 — label-rename (`run`, line 349 added: `detail = "html_entity" if detail == "html-entity" else detail`) — exit=1, stderr empty

Diff from unmutated output (all other 50 cases identical PASS):

```
FAIL behavioural-entity-label want=html-entity got=['/tmp/check-gate-quotes-selftest-a3_izr7n/entity.md:5 S901 html_entity', 'GATE_QUOTES: 1 findings']
FAIL behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/tmp/check-gate-quotes-selftest-a3_izr7n/entity.md:5 S901 html_entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /tmp/check-gate-quotes-selftest-a3_izr7n/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 50/52 pass
exit=1
```

### Introspection grep — landed file `/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py`

Command (grep tool, case-sensitive, whole file incl. selftest 363–580): pattern `\bdis\b|\binspect\b|\bhashlib\b|__code__|co_consts|__file__`

```
No matches found
```

Zero hits for all six tokens anywhere in the file, so the selftest contains no `dis`, no `inspect`, no `__code__`/`co_consts` bytecode inspection, no `__file__` self-reading, no hashlib. Text-level evidence only (no lsp server in this leaf).

## Verdict

**AGREE** with what landed at 43f1e781 for claim O. The frozen predicate ACCEPT-O-57, run without --seed, passes on three independent runs (exit 0, `ACCEPT-O-57: PASS`, all seven legs PASS, distinct random seeds); the selftest kills each of the three canonical mutants by behaviour (exit 1 each: double-decode via the decoded-once case, stop-at-first-bad-file via the continue-after-unreadable case, label-rename via both behavioural-label cases) and the selftest carries no introspection tokens. No fixes required. No predicate was amended; everything above is measured.

## Residual risk / verification gaps

- I measured claim O only; claim C (LOCATE leg) was not in this seat's scope.
- Introspection absence is grep (text) evidence over the whole file, not just the selftest body; a semantic review of every selftest assertion was not performed line-by-line, but the two behavioural cases and the decoded-once case demonstrably carry the kills.
- First M2 capture was incomplete (harness artifact); the complete separated-stream rerun is the record.
- accept-o's in-process mutant runner patches the loaded module, never the file on disk; my SOURCE-EDIT route confirms the same three behaviours kill the on-disk selftest too, which is the stronger of the two surfaces.
