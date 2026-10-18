# R30-O09..O10 — tokenless speaker control and the law selftest

- Date: 2026-10-18.
- Worker write scope: this report only. No shared tool, packet, pin, filed round-8..29 artifact, or bookkeeping file was written by this worker.
- Disposition: **verified candidate; orchestrator must land the tool edit and register the runner control before claiming fixed-with-control.** The executable amendment below constructs the exact candidate in memory, runs its real CLI entry point, and does not write a candidate tool. This is not evidence that the delivered tool has already changed.
- Axes: operability (tokenless tamper changes emitted finding lines), control quality (positive, negative, record-resolution, and unchanged-field controls), preservation (historical artifacts remain untouched).

## Reproduction and integration collision

At `2026-10-18T18:52:35-03:00`, command `export TMPDIR="$PWD/.scratch"; python3 -B tools/gates/register-law-gate.py --selftest` returned exit 0, `selftest: 33/33 checks passed`. Its speaker fixtures retained `(ZZ-99)`, so that result did not test the tokenless case. Source: `tools/gates/register-law-gate.py:277-287,412-415,478-495`; routed defect: `reports/round-29/defects/fix-15.md`.

During the parallel QREG landing, the clean packet became finding-free and gained identity-row speech fields before `register_law`. At `2026-10-18T18:54:12-03:00`, paired real CLI calls through `python3 -B tools/gates/register-law-gate.py --packet /dev/stdin`, with one field changed **inside the top-level `register_law` block**, gave:

| input | changed law fields | exit | emitted finding lines |
|---|---:|---:|---|
| clean | 0 | 0 | 0 |
| RGL-01 `speaker: "no-such-speaker"` | 1 | 0 | 0 — identical to clean |
| RGL-01 `speaker: "nobody-nowhere (ZZ-99)"` | 1 | 1 | 1 — `D4L-LAW-SPEAKER`, names RGL-01 and ZZ-99 |

The command used `re.search(r'(?m)^register_law:\n(?:[ \t]+[^\n]*(?:\n|$)|\n)*', text)` to isolate the law block, then `re.subn(r'(?m)^([ \t]+)speaker:[ \t]*[^\n]*$', ..., block, count=1)`. It asserted one replacement, tokenless finding-line equality, and exactly one added ID-bearing control line. Gate SHA-256: `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026`; packet SHA-256: `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`.

A prior broad first-`speaker` mutation at `2026-10-18T18:53:51-03:00` changed a QREG identity row instead. Its ID-bearing control failed; that failed probe is **not** counted as a successful reproduction. It exposes a second necessary repair: the existing selftest's broad first-field substitutions now hit QREG rows, not RGL-01. Its `bool(base)` clean replay condition also rejects a genuinely clean packet. The delivered selftest at this integration snapshot returned exit 1, **29/33**, failing `delivered-packet-replays` and all delivered force/speaker/consequence controls.

## Amendment contract

The candidate below is for **`tools/gates/register-law-gate.py` only**, to be landed by the orchestrator with the normal edit mechanism. It does not modify the law component or manufacture new speaker records.

- Declare a closed, exact **speaker/holder clause vocabulary**, with references to delivered records: stamp-holder/furnace-master → RK-03; broker/market-goer → RK-04; mold-keeper → OR-02; admitted-by clause → RGL-01/RGL-03. Authority: `examples/culture-d4/components/09-costumes.yml:143-144`, `03-orthography.yml:70`, and `13-register-law.yml:45-49`. The licensed class expressions are design policy, not inferred natural-language semantics or canon.
- Normalize case, whitespace, and syntactically recognized parenthesized ID annotations, then require the **whole clause** to match. Unknown, empty, and mixed known/unknown clauses fail; a valid ID cannot launder an unknown class. Existing explicit-ID resolution remains a distinct check.
- Require each declared clause's records to exist. This distinguishes a closed whitelist from an actual reference resolver. The oath holder's explicit `none` clause is a declared non-speaker, not an unchecked wildcard.
- Replace the old synthetic `any speaker` wildcard with the delivered admitted-by clause. A missing optional synthetic `holder` stays optional; a present holder is resolved exactly like a speaker.
- Scope text mutations to `register_law`, check parsed equality against a packet differing only in RGL-01's named field, and compare **formatted emitted finding lines**, not only class IDs or message text. Keep a separate ID-bearing speaker control.
- Accept a clean replay with zero findings; require successful evaluation and the declared law-row coverage instead. Do not demand historical dangles to keep a selftest green.

Limit: this is an explicit closed clause grammar. It does not interpret arbitrary office prose, execute an utterance's admissibility, validate rank-record contents beyond record existence, or prove the admitted-by graph is semantically acyclic. A new expression requires a deliberate vocabulary amendment. Existing force/consequence prose limitations are unchanged.

## Executable candidate and controls

Run this exact no-write verification command from the lane root. It reads the following fenced block from this report, builds the candidate in memory, invokes its CLI in subprocesses, and verifies the result against the unchanged delivered tool. It prints the run date and input digests, so counts are bound to the observed bytes.

```bash
export TMPDIR="$PWD/.scratch"
python3 -B - <<'PY'
from pathlib import Path
report = Path('reports/round-30/fixes/speaker-tamper.md').read_text()
code = report.split('```python\n', 1)[1].split('\n```', 1)[0]
ns = {'__name__': 'r30_speaker_control'}
exec(compile(code, 'reports/round-30/fixes/speaker-tamper.md', 'exec'), ns)
ns['verify']()
PY
```

```python
import datetime
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

GATE = Path('tools/gates/register-law-gate.py')
PACKET = Path('examples/culture-d4/packet.d4.yml')


def build_candidate(source):
    def replace(old, new):
        nonlocal source
        assert source.count(old) == 1, ('candidate anchor moved', old[:100])
        source = source.replace(old, new, 1)

    replace('    speaker      every agent token `Name (ID)` must name an id the packet carries\n'
            '                 as a record — the RL-4 `mold-keeper (OR-02, component-only)`\n'
            '                 shape, which became resolvable when RL-4 was repaired',
            '    speaker      every speaker/holder clause must name a declared expression\n'
            '                 and its delivered records; explicit `Name (ID)` tokens\n'
            '                 must independently resolve to delivered records')
    replace('    D4L-LAW-SPEAKER      an agent id resolves to no delivered record      [FAIL]',
            '    D4L-LAW-SPEAKER      a clause or its record references do not resolve [FAIL]')
    replace('  * the speaker resolution reads the `Name (ID)` shape only; a bare office name\n'
            '    with no id token is not resolved (there is no roster to resolve it against);',
            '  * speaker resolution uses a declared closed clause vocabulary and record\n'
            '    existence, not arbitrary prose interpretation or utterance admissibility;')
    replace('''- **A clean packet may carry findings, and does.** The delivered rows' `design_row`
  tokens `QREG-05..08` name the sibling design seats' proposed rows, which never
  landed as packet records (the landed rows are `RGL-01..05`). That is four honest
  `D4L-LAW-DANGLING` HOLDs, reported rather than repaired: the citing component is
  a filed round-27 artifact and is not this gate's to rewrite. Exit 0 here means
  "every resolution the gate performs found nothing to report", not "the law is
  complete" — the design's own position (`review.md` section 9).''',
            '''- **A clean packet may carry findings.** At round-28 landing, `design_row`
  tokens `QREG-05..08` named proposed records that had not landed, giving four
  `D4L-LAW-DANGLING` HOLDs. Round 30 adds those records rather than rewriting the
  filed law rows. The selftest accepts either evaluated baseline and measures a
  tamper's delta over emitted finding lines. Exit 0 means every resolution this
  gate performs found nothing to report, not that the law is complete
  (`reports/round-27/law/review.md` section 9).''')
    replace('AGENT_ID_RE = re.compile(r"\\(\\s*([A-Z]{2,4}-\\d{2,3})\\b")',
            '''# Closed clauses: components/13-register-law.yml RGL-01..05; record bindings:
# components/09-costumes.yml RK-03/RK-04, components/03-orthography.yml OR-02.
DECLARED_SPEAKER_CLAUSES = {
    "stamp-holder": ("RK-03",),
    "furnace-master": ("RK-03",),
    "mold-keeper": ("OR-02",),
    "broker": ("RK-04",),
    "market-goer": ("RK-04",),
    "stamp-holder, furnace-master, mold-keeper": ("RK-03", "OR-02"),
    "stamp-holder only — no master, no delegate": ("RK-03",),
    "broker, market-goer, at market days": ("RK-04",),
    "any speaker admitted by rgl-01 or rgl-03": ("RGL-01", "RGL-03"),
    "a stamp-holder, or a speaker the stamp-holder is attesting": ("RK-03",),
    "none — the register admits no binding oath": (),
    "a guest broker, speaking under a stamp-name": ("RK-04",),
}
AGENT_ANNOTATION_RE = re.compile(
    r"\\s*\\(\\s*[A-Z]{2,4}-\\d{2,3}(?:\\s*,\\s*component-only)?\\s*\\)")
AGENT_ID_RE = re.compile(r"\\(\\s*([A-Z]{2,4}-\\d{2,3})\\b")''')
    replace('''        for field in ("speaker", "holder"):
            value = text_of(row.get(field))
            for token in AGENT_ID_RE.findall(value):''',
            '''        for field in ("speaker", "holder"):
            if field == "holder" and field not in row:
                continue
            value = text_of(row.get(field))
            clause = " ".join(AGENT_ANNOTATION_RE.sub("", value).lower().split())
            required = DECLARED_SPEAKER_CLAUSES.get(clause)
            counters["speaker_clauses"] += 1
            if required is None:
                counters["speaker_failures"] += 1
                findings.append(finding(
                    "D4L-LAW-SPEAKER", "FAIL",
                    "%s %s clause %r is outside the declared speaker/holder vocabulary"
                    % (rid, field, value)))
            else:
                missing = sorted(set(required) - record_ids)
                if missing:
                    counters["speaker_failures"] += 1
                    findings.append(finding(
                        "D4L-LAW-SPEAKER", "FAIL",
                        "%s %s clause %r requires absent delivered records %s"
                        % (rid, field, value, "/".join(missing))))
            for token in AGENT_ID_RE.findall(value):''')
    replace('speaker: "any speaker", ',
            'speaker: "any speaker admitted by RGL-01 or RGL-03", ')
    replace('    _, tampered, _ = run(_packet(speaker="nobody-nowhere (ZZ-99)"))',
            '    _, tampered, _ = run(_packet(speaker="stamp-holder (ZZ-99)"))')
    replace('''    _, tampered, _ = run(_packet(consequence="the act evaporates silently"))''',
            '''    clean_lines = {format_finding(item) for item in run(_packet())[1]}
    for name, value in (
        ("tokenless", "no-such-speaker"),
        ("mixed", "stamp-holder, no-such-speaker"),
        ("known-id", "no-such-speaker (RK-03)"),
        ("empty", ""),
    ):
        code, tampered, _ = run(_packet(speaker=value))
        fired = _classes(tampered, "D4L-LAW-SPEAKER")
        added = {format_finding(item) for item in tampered} - clean_lines
        checks.append(("speaker-class-%s-changes-finding-lines" % name,
                       code == EXIT_FINDINGS and len(fired) == 1
                       and "RGL-01 speaker" in fired[0]["message"]
                       and repr(value) in fired[0]["message"]
                       and added == {format_finding(item) for item in fired}))
    code, clean_class, _ = run(_packet(speaker="stamp-holder"))
    checks.append(("declared-tokenless-speaker-resolves",
                   code == EXIT_CLEAN and not clean_class))
    missing = _packet(speaker="stamp-holder").replace(
        "  - {id: RK-03}", "  - {id: RK-99}")
    fired = _classes(run(missing)[1], "D4L-LAW-SPEAKER")
    checks.append(("declared-speaker-requires-delivered-record",
                   len(fired) == 1 and "RK-03" in fired[0]["message"]
                   and "requires absent delivered records" in fired[0]["message"]))

    _, tampered, _ = run(_packet(consequence="the act evaporates silently"))''')
    replace('''def selftest():
''', '''def _tamper_law_field(text, field, value):
    block = re.search(r"(?m)^register_law:\\n(?:[ \\t]+[^\\n]*(?:\\n|$)|\\n)*", text)
    if block is None:
        return text, 0
    pattern = r"(?m)^([ \\t]+)%s:[ \\t]*[^\\n]*$" % re.escape(field)
    altered, count = re.subn(
        pattern, lambda match: '%s%s: "%s"' % (match.group(1), field, value),
        block.group(), count=1)
    return text[:block.start()] + altered + text[block.end():], count


def selftest():
''')
    start = source.index('        import re as _re\n')
    end = source.index('    else:\n        checks.append(("delivered-packet-present", False))', start)
    old = source[start:end]
    replace(old, '''        text = live.read_text(encoding="utf-8")
        base_code, base_findings, base_counters = run(text)
        base = {format_finding(item) for item in base_findings}
        original = naming["load_yaml"](text)
        checks.append(("delivered-packet-replays",
                       base_code in (EXIT_CLEAN, EXIT_FINDINGS)
                       and base_counters["law_rows"] == len(LAW_DECLARED_ROWS)))
        for name, field, value, fid in (
            ("force", "force", "no-such-force", "D4L-LAW-FORCE"),
            ("speaker", "speaker", "no-such-speaker", "D4L-LAW-SPEAKER"),
            ("speaker-id", "speaker", "stamp-holder (ZZ-99)", "D4L-LAW-SPEAKER"),
            ("consequence", "consequence", "the act evaporates silently",
             "D4L-LAW-CONSEQUENCE"),
        ):
            tampered_text, count = _tamper_law_field(text, field, value)
            actual = naming["load_yaml"](tampered_text)
            first = original["register_law"][0]
            expected = {**original, "register_law": [
                {**first, field: value}, *original["register_law"][1:]]}
            checks.append(("delivered-%s-changes-only-law-field" % name,
                           count == 1 and first.get("id") == "RGL-01"
                           and actual == expected))
            code, changed, _ = run(tampered_text)
            added = {format_finding(item) for item in changed} - base
            checks.append(("delivered-%s-tamper-adds-a-line" % name,
                           code == EXIT_FINDINGS and len(added) == 1
                           and all(line.startswith("FINDING %s:" % fid)
                                   and "RGL-01" in line for line in added)))
        checks.append(("delivered-unchanged-control-identical-lines",
                       {format_finding(item) for item in run(text)[1]} == base))
''')
    return source


def finding_lines(stdout):
    return sorted(line for line in stdout.splitlines()
                  if line.startswith('FINDING D4L-LAW-'))


def verify():
    source = GATE.read_text()
    candidate = build_candidate(source)
    compile(candidate, str(GATE.resolve()), 'exec')
    launch = ('import sys; scope={"__name__":"__main__","__file__":%r}; '
              'exec(compile(sys.argv.pop(1),%r,"exec"),scope)'
              % (str(GATE.resolve()), str(GATE.resolve())))

    def invoke(code, args, packet=None):
        result = subprocess.run(
            [sys.executable, '-B', '-c', launch, code, *args],
            input=packet, text=True, capture_output=True)
        assert not result.stderr, result.stderr
        return result

    delivered_test = invoke(source, ['--selftest'])
    candidate_test = invoke(candidate, ['--selftest'])
    print('date:', datetime.datetime.now().astimezone().isoformat(timespec='seconds'))
    print('delivered_gate_sha256:', hashlib.sha256(source.encode()).hexdigest())
    print('candidate_gate_sha256:', hashlib.sha256(candidate.encode()).hexdigest())
    print('packet_sha256:', hashlib.sha256(PACKET.read_bytes()).hexdigest())
    print('delivered_selftest_exit:', delivered_test.returncode)
    print(delivered_test.stdout.splitlines()[-1])
    print('candidate_selftest_exit:', candidate_test.returncode)
    print(candidate_test.stdout, end='')
    assert candidate_test.returncode == 0

    scope = {'__name__': 'r30_candidate', '__file__': str(GATE.resolve())}
    exec(compile(candidate, str(GATE.resolve()), 'exec'), scope)
    loader = scope['load_naming']()['load_yaml']
    text = PACKET.read_text()
    original = loader(text)
    source_clean = invoke(source, ['--packet', '/dev/stdin'], text)
    clean = invoke(candidate, ['--packet', '/dev/stdin'], text)
    assert (clean.returncode, finding_lines(clean.stdout)) == (
        source_clean.returncode, finding_lines(source_clean.stdout))
    base = set(finding_lines(clean.stdout))
    observed = []
    for rid in scope['LAW_DECLARED_ROWS']:
        for field in ('speaker', 'holder'):
            rows = original['register_law']
            index = next(i for i, row in enumerate(rows) if row['id'] == rid)
            block = re.search(r'(?m)^register_law:\n(?:[ \t]+[^\n]*(?:\n|$)|\n)*', text)
            assert block
            fields = list(re.finditer(
                r'(?m)^([ \t]+)' + field + r':[ \t]*[^\n]*$', block.group()))
            match = fields[index]
            value = 'no-such-speaker'
            at = block.start() + match.start()
            until = block.start() + match.end()
            altered = text[:at] + match.group(1) + field + ': "' + value + '"' + text[until:]
            expected_rows = [dict(row) for row in rows]
            expected_rows[index][field] = value
            assert loader(altered) == {**original, 'register_law': expected_rows}
            before = invoke(source, ['--packet', '/dev/stdin'], altered)
            after = invoke(candidate, ['--packet', '/dev/stdin'], altered)
            assert finding_lines(before.stdout) == finding_lines(source_clean.stdout)
            added = set(finding_lines(after.stdout)) - base
            assert after.returncode == 1 and len(added) == 1
            assert all('FINDING D4L-LAW-SPEAKER:' in line
                       and rid + ' ' + field in line for line in added)
            observed.append({'row': rid, 'field': field, 'delivered_exit': before.returncode,
                             'candidate_exit': after.returncode, 'added_lines': sorted(added)})
    assert finding_lines(invoke(candidate, ['--packet', '/dev/stdin'], text).stdout) == sorted(base)
    print('paired_tokenless_cli_controls:', json.dumps(observed, indent=2))
    print('clean_candidate_exit:', clean.returncode)
    print('clean_candidate_findings:', len(base))
    print('all_controls_passed:', len(observed))
```

## Verification results and remaining integration

The exact no-write command above completed at **2026-10-18T18:56:31-03:00**, exit 0:

- Delivered source: `selftest: 29/33 checks passed`, exit 1. This remains a delivered defect, not a green regression.
- Candidate: **45/45** selftest checks passed, exit 0. Candidate SHA-256: `15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169`.
- Candidate clean packet: exit 0, **0** finding lines, equal to the original gate's clean reading. Packet SHA-256: `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`.
- **10/10 independent paired tokenless CLI controls** passed: RGL-01..RGL-05 × speaker/holder. Every original-gate mutation stayed exit 0 with the clean finding lines; every candidate mutation changed exactly the named parsed field, returned exit 1, and added **exactly one** `D4L-LAW-SPEAKER` line naming its row and field. The unchanged candidate packet replayed identically.
- Representative emitted line: `FINDING D4L-LAW-SPEAKER: FAIL — RGL-01 speaker clause 'no-such-speaker' is outside the declared speaker/holder vocabulary`.

Historical-baseline control at **2026-10-18T18:56:33-03:00**: command `git show 87bfc9956f0fc60e6821fe53b622d0043e28be10:examples/culture-d4/packet.d4.yml` supplied packet text directly to the original/candidate in-memory CLI launch used above (`--packet /dev/stdin`), then `_tamper_law_field(text, 'speaker', 'no-such-speaker')` supplied the single-field negative control. No files were materialized. Historical packet SHA-256: `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f`. Original and candidate both returned exit 1 with the **same four** dangling finding lines. The candidate tokenless tamper returned exit 1 with those same four plus **one** named speaker line (**5** total). Thus the selftest repair does not depend on deleting the old baseline findings or merely changing an exit code.

Adjacent regressions, with `TMPDIR=$PWD/.scratch`:

- At `2026-10-18T18:56:33-03:00`, command `python3 -B tools/assemble-culture-d4.py --check`: exit 0, byte-identical deterministic assembly.
- At `2026-10-18T18:56:33-03:00`, command `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml`: exit 0; `records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0`.
- At `2026-10-18T18:53:51-03:00`, command `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` initially returned exit 2 at `L1-profile` during the concurrent packet/projection landing: pinned packet `543d68a82640` versus live `aac91246cede`; pinned projection `339bfd83bf66` versus live `c23b0ab532cf`.
- At **2026-10-18T18:55:37-03:00**, the **same typed-pipeline command** returned exit 0, **20/20 legs passed**, after another worker updated the current profile to `expected-holds.r30-qreg.json`. Profile prefix: `b42ebfaf9016`. This worker made no pin or profile changes. The transient failure is retained above rather than hidden.

The no-write verifier intentionally requires the unamended gate's exact edit anchors; it constructs, but does not install, the candidate. After landing the tool the orchestrator should run the delivered `--selftest` and an independent tokenless law-block tamper, not reapply the candidate builder to already-amended source. The lane-wide Round-30 runner was not run by this report-only worker because its shared output is outside the assignment.

**Remaining owner: Round-30 orchestrator.** Land the candidate edits in the shared tool using the normal edit mechanism; the `build_candidate(source)` function supplies the exact desired source for a reviewed diff. Ensure the Round-30 runner mutates the **law block**, not the newly populated QREG identity rows, and registers both tokenless and ID-bearing controls. Replay the delivered selftest, clean packet, and independent tamper with emitted-line deltas; add any required **new** pin rows. Only then mark this routed item `fixed-with-control`. Until that delivery-level replay, retain `verified candidate / integration required`: report-only write scope is the reason the shared tool was not edited here.
