# R14-O04 — round-10 draft status and entry-count reconciliation

- Date: 2026-10-17.
- Axis: O / operability; assignment: draft reconciliation.
- Routed finding: `reports/round-12/defects/routed.md:66-72`, R10-SWEEP F-05; detailed finding: `reports/round-12/defects/sweep-r10.md:39-45`.
- Disposition: **resolved-by-documentation**, with the read-only positive/negative and preservation controls below. This is a new integration record, not a rewrite or new admission of round 10.

## Draft status: superseded-by-final-report

`reports/round-10/report-draft.md` is **superseded-by-final-report**. Retain it as the X04 in-flight draft, not the settled admission report: its heading and disclaimer explicitly identify a draft, refreshed at 21:38Z on 2026-10-17, and say “Nothing here is an admission” (`report-draft.md:1-9`). Its provisional failures, SHONEN skeleton, and orchestrator open items must not be read as the final round state.

The draft names `.ufo/reports/round-10/kotodama.md` as the final destination (`report-draft.md:8-9`). That is a **fleet-root** report, not a missing lane-local deliverable. The later in-lane `reports/round-11/adjacency.md:24-30` records fleet-root checks on 2026-10-17 and explicitly says that final-report path and the L0 surface “are committed (porcelain 0).” This is historical, indirect filing evidence; this lane-only assignment did not open the external report, inspect its final SHONEN text, or verify its digest. The earlier sweep's absence-of-local-copy observation does not establish absence of the fleet filing.

The settled state is independently available within the lane: admission commit `94ca098b8ab03be52ec80f6925538e5e2c0ed327` (2026-10-17T18:57:36-03:00), `LOG.md:2987-3008`, and `SCORECARD.md:160-182` record round 10 **admitted, C/F/O passing**. The filed `reports/round-10/validation.json` has `acceptance_checks_passed: true` and each claim's `passed: true`. These supersede the draft's earlier floor receipt, not the historical bytes that describe it. This note does not resolve the separate baseline-label, author-classification, stale-fixed-ledger, or transient-runner-hash findings.

## Eight versus ten

The SHONEN skeleton's “8 new entries” (`reports/round-10/report-draft.md:240-241`) is a stale draft count, not the settled result. The same draft's coverage section already says “10 new `corpus/knowledge/` entries” (`report-draft.md:34-42`). There is no basis here to assign the eight-entry bullet a separately verified timestamp or reinterpret it as the final total.

**Correct settled reading: ten added knowledge entries**, split linguistics 3, myth-symbol 3, culture-material 2, verification 2. Command/date: the control below, run on 2026-10-17T20:58:40-03:00, compares added Markdown paths between the declared baseline `9dc18ec1339bffd6f81e74f1a5742464ef578749` and the admission commit, then checks `claims.C.measurement.new_entries` in both the live and admission-commit receipts. All agree with that reading. The filed receipt's original counting command is `python3 reports/round-10/run-validation.py`, dated 2026-10-17; **it was not rerun**, because it writes the filed receipt.

The same ten-entry split is recorded in `reports/round-10/coverage/index-update.md:26-41`; that fragment supplies its original 2026-10-17 counting date and command. Counts of coverage fragments are a separate measurement channel and do not change the number of added knowledge entries.

## SHONEN evidence carried forward

These are lane assertions with evidence pointers, **not** independently verified promotion marks. Under `SHONEN.md:10-11`, no `[x]` is earned without a named non-author verifier; this erratum awards none and does not change the checklist file.

- [~] Real decision/error/checklist material: `SKILL.md`, especially Error patterns (`:75-100`), Boundaries (`:102-113`), and Checklist (`:115-127`). The checklist explicitly identifies a prose-only item; do not infer universal executable enforcement.
- [~] End-to-end domain work executed and logged: the settled entry additions above, their `reports/round-10/coverage/C*.md` author evidence and `review-C*.md` reviews, and the round-10 admission entry at `LOG.md:2987-3008`. Use the corrected entry total, not the draft skeleton's eight.
- [~] Runnable instructions/evidence contract: `reports/round-10/run-validation.py:9-44`, its declared counting command, and the retained passing `validation.json`. This is historical structural acceptance evidence, not a fresh round-14 execution, source-truth certification, or proof that every prose checklist item is automated.
- [~] Province remains the boundary: `PROVINCE.md:9-31`; `reports/round-10/adjacency.md:18-28` records X02's dated boundary verdicts. Its live-window limits remain in force (`adjacency.md:319-329`); this note does not manufacture a fresh cross-repository audit or erase the recorded receipt-mutation incidents.

## Reproducible control — read-only, no receipt writer

Run from the lane root. The positive control requires the settled count and partition split to agree with the filed receipt; the negative control rejects the obsolete eight-entry candidate without writing a fixture. Preservation checks compare the draft and receipt byte-for-byte to the admission commit, so a current or future silent rewrite fails the control. The filing-pointer check verifies only the in-lane attestation, not the external file's contents.

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
from collections import Counter
from datetime import datetime
from hashlib import sha256
import json
from pathlib import Path
import subprocess

base = '9dc18ec1339bffd6f81e74f1a5742464ef578749'
close = '94ca098b8ab03be52ec80f6925538e5e2c0ed327'
def git(*args):
    return subprocess.check_output(['git', *args])

print('observed_at=' + datetime.now().astimezone().isoformat())
receipt_path = 'reports/round-10/validation.json'
receipt = json.loads(Path(receipt_path).read_text())
filed = json.loads(git('show', close + ':' + receipt_path))
added = git('diff', '--name-only', '--diff-filter=A', base, close,
            '--', 'corpus/knowledge').decode().splitlines()
entries = [p for p in added if p.endswith('.md')]
parts = dict(sorted(Counter(Path(p).parts[2] for p in entries).items()))
expected = {'culture-material': 2, 'linguistics': 3,
            'myth-symbol': 3, 'verification': 2}
def count_agrees(candidate):
    return candidate == len(entries) == receipt['claims']['C']['measurement']['new_entries']

assert count_agrees(10) and parts == expected
assert not count_agrees(8)
assert receipt == filed and receipt['acceptance_checks_passed'] is True
assert all(receipt['claims'][claim]['passed'] for claim in ('C', 'F', 'O'))
draft = Path('reports/round-10/report-draft.md').read_text()
assert 'DRAFT BODY — orchestrator finalizes' in draft
assert 'executed and logged — 8 new entries' in draft
assert '**10 new `corpus/knowledge/` entries**' in draft
pointer = '.ufo/reports/round-10/kotodama.md'
assert pointer in draft
adjacency = Path('reports/round-11/adjacency.md').read_text()
assert pointer in adjacency and 'are committed (porcelain 0)' in adjacency
for name in ('reports/round-10/report-draft.md', receipt_path):
    blob = Path(name).read_bytes()
    assert blob == git('show', close + ':' + name), name
    print('preserved=' + name + ' sha256=' + sha256(blob).hexdigest())
print('settled_count_10=PASS partitions=' + json.dumps(parts, sort_keys=True))
print('obsolete_count_8=REJECTED')
print('supersession_pointer=PASS (historical in-lane attestation only)')
print('draft_and_receipt_filed_bytes=UNCHANGED')
PY
```

Observed result on **2026-10-17T20:58:40-03:00: exit 0**:

```text
preserved=reports/round-10/report-draft.md sha256=40fe0738d69e58b380006aacf38551a29889349c455b31dc7df9819f7b07675e
preserved=reports/round-10/validation.json sha256=e8571db918b2c3237256342bd95f241be5661a96019e460990c7d1fe2fc32f94
settled_count_10=PASS partitions={"culture-material": 2, "linguistics": 3, "myth-symbol": 3, "verification": 2}
obsolete_count_8=REJECTED
supersession_pointer=PASS (historical in-lane attestation only)
draft_and_receipt_filed_bytes=UNCHANGED
```

Only this new erratum is this worker's deliverable. Filed draft/receipt bytes and all other round-8–12 artifacts were not written by this worker. The parent integrator carries this disposition into the round-14 resolution ledger and append-only LOG entry; external report content/digest verification, if required, remains with its authorized fleet owner.
