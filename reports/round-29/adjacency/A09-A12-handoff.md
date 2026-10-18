# Round 29 — A09–A12 adjacency ledger and verdict

- **Date:** 2026-10-18. **Axes:** adjacency isolation, province accuracy, evidence completeness.
- **Scope:** the round-27 register-law component and its assembled D4 packet block; the two linguistics knowledge entries required by the round-27/28 claims; their corpus-index rows; and `PROVINCE.md`.
- **Method:** read-only source-boundary review. This is not a general D4 artifact-tree audit, real-world legal/rights review, canon adjudication, or round-admission verdict. No historical validator was run and no filed round-8–28 artifact was changed.

## Verdict

**ADJACENCY PASS within the declared slice, with one separate evidence defect filed.** The register law is explicitly an in-world, NON-CANON design rule; both knowledge entries are in-province linguistic-cultural reference/design methods; `PROVINCE.md` remains accurate and unchanged. No out-of-province content or unfiled bleed was found. The ceilings entry's `which semantic fields` absence claim was already contradicted at the round-28 baseline and is filed as an evidence/reporting defect, not adjacency bleed. The other three absence sweeps were baseline-clean and became matches only after sibling entries landed; these are time-scoped sibling landings, not authoring defects or bleed. The four-sweep baseline/current reconstruction is dated **2026-10-18T21:21:18Z** (commands and hits below); no corpus correction is made in this seat.

This is a scoped result, not a claim that every D4 surface is free of fixture bleed. `reports/round-21/adjacency/ledger.json` previously filed `A21-D4-XF-01` on `examples/culture-d4/typed-labels.d4.yml`; this audit does not re-audit or declare that finding resolved. The ledger's zero-unfiled-bleed result applies only to the paths enumerated in the accompanying JSON.

## Evidence

- The register-law component identifies itself as a D4 design drill and NON-CANON (`examples/culture-d4/components/13-register-law.yml:2-3,13-18`). Its calibration says no real institution, court, or register is described, cited, or approximated (`:60-63`); its canon boundary says no real-world language, institution, community, or rights question is decided or implied (`:65-70`). The law itself is marked `design-choice` (`:45-49`).
- The law block is present in the D4 packet under `register_law:` (`examples/culture-d4/packet.d4.yml:2710`). The five IDs `RGL-01` through `RGL-05` were independently extracted from both the component and packet: each surface returned those **5 unique IDs**. Command and date: `2026-10-18T21:03:06Z`, the inline Python block below. The packet header calls the drill NON-CANON (`:1-5`). References to “furnace right” are fictional institutions in this drill; they do not adjudicate actual rights.
- `corpus/knowledge/linguistics/register-strata-attestation.md` is a linguistics design/reference entry. It expressly declines canon and real-community claims (`:34-45`), names its NON-CANON drill and limits (`:298-307`), and hands canon/world truth to lore-shokunin (`:309-313`). Searle's “rights, duties, permissions” appears as theoretical terminology in its description of deontic powers (`:17`), not as a ruling about any real-world right.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md` is a linguistic derivation/semantic-field design method; its calibration analogues are bounded and its transferable claim is the procedure, not the D4 numbers (`:176-189`). It labels the drill NON-CANON and makes no claim about real-world registers (`:241-248`), and reserves canon decisions to lore-shokunin (`:274-289`).
- Both entry filenames have one corpus-index filename row. Command and date: `2026-10-18T21:03:06Z`, the same inline Python block below. The rows are at `corpus/README.md:138-139`; the revision notes distinguish craft knowledge from canon or historical-truth certification (`:3-15,37-45`).
- `PROVINCE.md` assigns this lane linguistic-cultural craft, its knowledge corpus, gates, non-canon examples, and reports (`:3-11`); it refuses canon and real-world rights/attribution rulings and keeps the adjacent world-bible contract load-bearing (`:16-25`). These boundaries match the audited files. At `2026-10-18T20:53:38Z`, `git diff --quiet -- PROVINCE.md` exited 0 and `sha256sum PROVINCE.md` returned `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`.

### Measured commands

RGL IDs, filename rows, and boundary sentinels were read-only checks. At **2026-10-18T21:03:06Z**, this command returned the exact ID sets and index-row counts reported above:

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
date -u '+AUDIT_UTC=%Y-%m-%dT%H:%M:%SZ'
python3 - <<'PY'
from pathlib import Path
import re
law_paths = ('examples/culture-d4/components/13-register-law.yml', 'examples/culture-d4/packet.d4.yml')
markers = ('- {id: RGL-', 'id: "RGL-')
for path in law_paths:
    ids = [re.search(r'RGL-0[1-5]', line).group(0) for line in Path(path).read_text().splitlines() if line.strip().startswith(markers)]
    print(f'{path}: ids={ids} count={len(ids)} unique={len(set(ids))}')
readme = Path('corpus/README.md').read_text().splitlines()
for name in ('register-strata-attestation.md', 'register-lexicon-ceilings.md'):
    prefix = '- `' + name + '` —'
    print(f'index {name}: rows={sum(line.startswith(prefix) for line in readme)}')
for path in ('corpus/knowledge/linguistics/register-strata-attestation.md', 'corpus/knowledge/linguistics/register-lexicon-ceilings.md'):
    text = Path(path).read_text()
    print(f'entry {path}: noncanon={"NON-CANON" in text} canon_boundary={"Canon boundary and handoff" in text} explicit_real_world_limit={"real" in text.lower()}')
component = Path(law_paths[0]).read_text()
packet = Path(law_paths[1]).read_text()
print(f'law disclaimers: component_no_real_world_rights={"No real-world language, institution, community, or rights question is decided" in component}; packet_noncanon={"canon: \"not canonized (D4 NON-CANON design drill)\"" in packet}')
PY
```

The preliminary probes are disclosed, not used as source evidence: at **2026-10-18T20:57:22Z**, an over-escaped regex returned no RGL matches and raw README substring counts included revision-note mentions rather than just index rows. At **2026-10-18T21:00:16Z**, a display slice printed line suffixes instead of the RGL IDs. Both were auditor-instrument mistakes; the exact-anchor extraction above supersedes them. No content mismatch was patched or hidden.

The PROVINCE check at **2026-10-18T20:53:38Z** was:

```bash
git diff --quiet -- PROVINCE.md
sha256sum PROVINCE.md
```

### Reconstructed quoted absence sweeps

At **2026-10-18T21:21:18Z**, I reconstructed the four quoted absence sweeps against the declared round-28 baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede` and the current corpus. Each scan excludes the entry making the claim. This is a read-only scan, not a historical validator:

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
date -u '+AUDIT_UTC=%Y-%m-%dT%H:%M:%SZ'
python3 - <<'PY'
from pathlib import Path
import re, subprocess
base='6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede'
targets={
    'register-lexicon-ceilings.md': ('lexicon ceiling', 'which semantic fields'),
    'register-strata-attestation.md': ('attestation register|attestation speech', 'register law|register-law'),
}
paths=subprocess.check_output(['git','ls-tree','-r','--name-only',base,'--','corpus/knowledge'],text=True).splitlines()
queries=[('RLC lexicon ceiling', 'lexicon ceiling', 'register-lexicon-ceilings.md'),('RLC which semantic fields','which semantic fields','register-lexicon-ceilings.md'),('RSA attestation register|attestation speech','attestation register|attestation speech','register-strata-attestation.md'),('RSA register law|register-law','register law|register-law','register-strata-attestation.md')]
for label, pattern, target in queries:
    rx=re.compile(pattern, re.I)
    found={}
    for path in paths:
        if not path.endswith('.md') or path.endswith('/'+target):
            continue
        try:
            text=subprocess.check_output(['git','show',f'{base}:{path}'],text=True,stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            continue
        lines=[i for i,line in enumerate(text.splitlines(),1) if rx.search(line)]
        if lines: found[path]=lines
    current={}
    for path in Path('corpus/knowledge').rglob('*.md'):
        if path.name == target: continue
        text=path.read_text(errors='replace')
        lines=[i for i,line in enumerate(text.splitlines(),1) if rx.search(line)]
        if lines: current[path.as_posix()]=lines
    print(f'{label}: baseline={found}; current={current}')
PY
```

Output:

```text
AUDIT_UTC=2026-10-18T21:21:18Z
RLC lexicon ceiling: baseline={}; current={'corpus/knowledge/linguistics/register-strata-attestation.md': [315]}
RLC which semantic fields: baseline={'corpus/knowledge/linguistics/sound-symbolism.md': [106]}; current={'corpus/knowledge/linguistics/sound-symbolism.md': [106], 'corpus/knowledge/linguistics/register-strata-attestation.md': [399]}
RSA attestation register|attestation speech: baseline={}; current={'corpus/knowledge/linguistics/register-lexicon-ceilings.md': [125]}
RSA register law|register-law: baseline={}; current={'corpus/knowledge/linguistics/register-lexicon-ceilings.md': [4, 9, 17]}
```

`register-lexicon-ceilings.md:4` reports zero for `which semantic fields`, but baseline `sound-symbolism.md:106` already says to assign which semantic fields carry ideophones. That is one false-at-authoring evidence claim, filed as `A29-ADJ-EVID-01`; it is not bleed. The other three sweeps had no baseline hits and only match the later sibling entry in the current corpus. They are time-scoped sibling landings, not authoring defects. No corpus file is edited in this seat; route an append-only evidence correction to the entry owner/Round 30.

The earlier **21:05:40Z** census was run before this finding was discovered and filed; its zero-finding count is superseded. An attempted one-line census at **21:06:07Z** failed to parse because of shell/Python quote escaping (`SyntaxError`) and produced no measurement. Both are disclosed as instrument-history only, not final evidence.

### Final ledger census

At **2026-10-18T21:22:57Z**, the final ledger census checked scoped-path counts, province/bleed booleans, finding filing, and all four sweep dispositions:

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
date -u '+AUDIT_UTC=%Y-%m-%dT%H:%M:%SZ'
python3 - <<'PY'
import json
from pathlib import Path
p = Path('reports/round-29/adjacency/ledger.json')
d = json.loads(p.read_text())
records = d['entries'] + d['rows'] + d['audits']
findings = {x['id']: x for x in d['findings']}
bleeds = [x for x in records if x['bleed']]
unfiled = [x for x in bleeds if not findings.get(x.get('finding_id'), {}).get('filed', x.get('filed', False))]
assert (len(d['entries']), len(d['rows']), len(d['audits'])) == (2, 0, 4)
assert len(records) == 6
assert all(x['out_of_province'] is False and x['bleed'] is False for x in records)
assert len(d['findings']) == 1
finding = d['findings'][0]
assert finding['id'] == 'A29-ADJ-EVID-01' and finding['filed'] is True
assert finding['out_of_province'] is False and finding['bleed'] is False
assert len(d['sweep_dispositions']) == 4
assert len(unfiled) == 0 and d['unfiled_bleed'] == 0
print(f'ledger_paths={len(records)} entries={len(d["entries"])} rows={len(d["rows"])} audits={len(d["audits"])} bleed={len(bleeds)} unfiled_bleed={len(unfiled)} filed_non_bleed_findings={len(d["findings"])} sweep_dispositions={len(d["sweep_dispositions"])}')
print('ledger JSON: valid; scoped boundaries, finding filing, and sweep dispositions: PASS')
PY
```

Output: `ledger_paths=6 entries=2 rows=0 audits=4 bleed=0 unfiled_bleed=0 filed_non_bleed_findings=1 sweep_dispositions=4`; JSON parsing, boundary assertions, and filing/disposition assertions passed.

## Disposition and limits

No adjacency or province correction is proposed. The two entries remain in linguistic-cultural craft; the register-law rows remain a fictional system proposal, not real-world rights rulings. Keep `A29-ADJ-EVID-01` filed for an append-only evidence correction by the entry owner/Round 30; do not edit the corpus in this seat. The three baseline-clean sibling landings are recorded without corpus edits. The already-filed `A21-D4-XF-01` is outside this audit's slice and is neither re-evaluated nor closed here. This report does not certify the law's enforcement, source truth, canon status, D4 fixture isolation as a whole, or the round's acceptance.

FILES: reports/round-29/adjacency/ledger.json, reports/round-29/adjacency/A09-A12-handoff.md | SUMMARY: Scoped adjacency pass; six audited paths remain in-province with zero bleed, one baseline-false absence claim is filed as a non-bleed evidence defect, and three other sweeps are time-scoped sibling landings.
