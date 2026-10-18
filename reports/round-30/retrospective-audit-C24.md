# R30-C24 — independent number audit and anti-inflation controls

Date: **2026-10-18**. Axis: calibration, with filed-byte preservation as a constraint. This is not round-30 admission. C23 audits pointers; C25 supplies parent-only bookkeeping drafts.

## Independently recovered census

Command, executed **2026-10-18T21:54:17Z**, exit **0**:

```sh
export TMPDIR="$PWD/.scratch" PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-30/retrospective-audit-C23-C25.py --numbers --selftest --protected
```

The executable is read-only. It reads stored JSON, independently recomputes the eight R26 pair transformations, and compares receipt/protected bytes with Git objects at the declared R30 baseline. It does not execute or import an old round validator.

- **Closed rounds 8–29:** 18 admitted, three rejected (**11, 17, 22**), one operator-skipped (**13**). Loop 1 = seven admitted / one rejected / one skip; loop 2 = six admitted / two rejected; loop 3 through R29 = five admitted. R30 remains under integration; R31/R32 remain future slots. Rounds 8–32 are 25 round numbers, but the amended regimen has 24 dispatch slots plus the skipped R13; do not call 25 completed rounds or the third loop complete.
- **Receipt population:** 20 lane-local final `validation.json` files, 55 true / two false claim flags. R22 has no lane-local final validation receipt; its O/C-verified, D-rejected closure is parent prose at `LOG.md:3298-3310`, with the source-state correction at `LOG.md:3312-3324`. Adding those separately attributed three flags yields a parent/receipt composite, not 60 JSON claim flags. R25–29 have 15 true flags in five filed receipts; this does not recertify every literal historical contract.
- **Request population:** the declarations for non-skipped R8–29 sum to 1,088 requested worker seat-rounds. This is not measured launches, concurrency, unique workers, or completions. R13's 128-seat abandoned declaration is excluded; do not present it as a completed batch.
- **Recount populations:** R12 = 89 rows (12 match + 77 disposition); R21 = 63 (39 match + 24 disposition); R29 = 26 (nine match + 16 disposition + one historical coverage-limit). They have different command/grouping units and are not three comparable freshness scores or an aggregate exact-replay denominator.
- **R29 defect ledger:** 24 unique IDs; status 16 open / three closed / three observation / two superseded; class 14 conformance / nine process / one bookkeeping. R30's declared five-item worklist is a scoped integration contract, not all 16 open defects or all review-level routes.
- **Availability:** R25–28 each declare 64 and route `devin/deepseek-v4-1-flash-high`, while `launched_workers` and `completed_workers` remain null in all four records. Parent LOG reports 26/24/24/24 completions (98 of 256 declared build seats); adding R29's reported 17 yields 115 of 320 for R25–29. These are parent-reported figures, not independently observed dispatch traces.
- **Amendments:** four resolving amendment commits: two structural (`51e5901`, `3dba77a`) and two provider designations (`9437788` for R19/Hyper; `eb4295c` for R25–28/Devin). Five build rounds fall under the latter designations; a provider designation is neither an extra admission nor evidence of a performance advantage. R10's three pre-launch 402 attempt receipts are separate availability events, not additional completed rounds or a fifth structural amendment.
- **Freshness:** R11's 192 rows contain 189 byte-comparable rows and 147 stable. Comparable ratio = 147/189 = 0.7777777777777778; all-row ratio = 147/192 = 0.765625. Both fail 0.95. Neither a denominator correction, explained drift nor a future policy recommendation readmits R11.
- **Register arithmetic:** R26's delivered eight-pair stratum independently recomputes as **two reverse + six lengthen**, all eight outputs equal their recorded `term` and `replayed`. No delivered pair uses `head2`. The eleven R17 worked pairs are a separate algorithm-test population, not eleven packet forms.
- **Law calibration:** R29's final receipt preserves six design-probe findings versus four delivered findings, exit 1, all four `D4L-LAW-DANGLING`. A zero-finding R30 successor must be reported as a new controlled repair, never as the historical R28/R29 reading.

The twelve pointer controls and nine numeric anti-inflation controls all passed. These include rejecting absent paths/keys/headings/revisions, bad line ranges, altered bytes, retroactive admissions, completion inference from null fields, the six-versus-four conflation, and recount dispositions as exact matches. Protected sample: **1,764 paths, zero mismatches**, manifest SHA-256 `7d4b532e5080e7783b1d544fe06afea5e84d33de9ac8ffa997fbea6b1c7577eb`.

## Required qualifications in the retrospective

These are guardrails, not claims that the incoming retrospective already violates them. The owner should incorporate or explicitly disposition them; auditors do not edit the owner's text.

- **C24-F01 — R29 availability disposition prose overstates its JSON source.** `reports/round-29/devin-availability-disposition.md:9-15` says the four durable records carry completed counts 26/24/24/24 and wall times. The actual completion fields are null. Cite those counts to the parent LOG instead, preserve the raw-sample `could-not-evaluate` result, and do not amend the filed R29 document.
- **C24-F02 — R22 source correction is not a changed verdict.** Its source implementation was present at close commit `0e81d9d`, despite the earlier “never implemented” wording; the append-only correction explains that the required verification path was unmet at close. Retain the rejection and both evidence channels. Absence of a JSON receipt must not erase the round or invent receipt flags.
- **C24-F03 — do not repeat R25's stale design-language attribution.** The filed R17 design-language now states COUNT × QUOTE at `reports/round-17/d4/design-language.md:32-49,68-70`, whereas `reports/round-25/argot/delta.md:17-27,58,65-70` quotes a stale TIDE + LEDGER text at line 61. The real, supported forecast/delivery fork is COUNT × QUOTE weigh-court versus FIRE × MARK furnace-league. A path resolving does not make an outdated quoted line correct.
- **C24-F04 — ceiling counts have two readers.** `reports/round-28/ceiling/C41.md:25-37,61-85,110-138` distinguishes filed R27 18 legal / nine illegal, abstract class zero/five, from delivered-reader 19/eight, abstract class one/four. Only **four of five** abstractions still refuse reverse; `L-45 tikmes → semkit` is the one-row correction. The oath example `L-30 gis → sig` remains illegal. Do not repeat the R28 declaration's “five refuse” as the final measured count or claim impossibility for every register operation.
- **C24-F05 — historical coverage limit and later parent control both stand, with an unresolved count mismatch.** The R29 recount ledger still has one `coverage-limit` row, and its worker audit says the R27 full sweep was not rerun at wave time. The later parent addition `reports/round-29/recount/r27-full-sweep-reproduction.json` actually contains **117 surfaces / 31 finding rows / exit 1** at revision `e923d6e…`; `reports/round-29/recount/C11.md:45-59` instead attributes **41 findings over 41 drifted surfaces** to that receipt, while quoting the historical 113/31 baseline. Read-only control at **2026-10-18T21:55:48Z**: `python3 -B -c 'import json; d=json.load(open("reports/round-29/recount/r27-full-sweep-reproduction.json")); print(d["date"], d["revision"], d["summary"], len(d["findings"]))'`, exit 0, emits 117/31/1 and 31 rows. The R29 retrospective shard correctly preserves this disagreement. My first C24 draft had repeated the historical 113-surface total as the new JSON result; this independent selector control corrects that auditor attribution. Keep the worker limitation, late executed sweep and mismatched prose separately attributed; none warrants rewriting the ledger to 100% exact matches. R28's independently red 121-surface / 39-finding / 11-of-12-nonzero replay result is another generation and remains red even though R28's aggregate validator was green.
- **C24-F06 / C23-F01 — CLOSED by the shard owner and independent rerun.** The first R29 shard block exited 1 with `KeyError: 'requested_model'` at **2026-10-18T21:55:48Z**. The owner changed its lookup to the real availability field `route`; the complete read-only block then passed at **2026-10-18T21:56:24Z** against SHA-256 `c0434d49729c20f442cc53f540be5a18096d18789caeba26323082804daa5228`. No historical JSON was modified. This paired failure/success is a control-pointer repair, not a provider result.

## First consolidated-text review

At **2026-10-18T21:56:24Z**, both M1/M2 blocks in `reports/round-30/loop3-retrospective.md` passed at SHA-256 `d298a4944c2cad1300ba5d8ce9fcd9c1d457de1bed1e02d9ebfcaf69ad7af737` with the report unchanged during execution. The three upstream shard blocks now all pass independently. The consolidated source agrees with the core historical state/flag/queue/null-worker controls and offers a concrete prospective split freshness contract while retaining the pause and old rejections.

**C24-F05 — CLOSED as a retrospective-attribution defect, not as a historical source correction.** The owner now preserves C11's 41/41 prose beside the JSON's 117 surfaces / 31 findings / exit 1, explicitly says exact agreement is not established, and adds a read-only M2 assertion of both source channels. The historical disagreement remains an integration follow-up; neither source was rewritten.

## Consolidated numeric verdict

**PASS at final SHA-256 `edda7ba51a6793e88f7ce30500cc7ee4e7065cbd2550640c2d7b45d260a7a6f2`**, observed **2026-10-18T21:59:26Z**. Both consolidated M1/M2 blocks and all three inspected upstream shard blocks ran concurrently, **5/5 exit 0**, with every input document byte unchanged during execution. The superseded `487514f2…` binding was rejected. M2 now asserts the exact 117/31/1 JSON summary, 31 finding rows, the named revision, preserved 41-count C11 prose, and the bounded 11/11 R29 direct-regression inventory. All count units and substantive qualifications C24-F01–F06 are incorporated or explicitly retained as historical limitations.

The concrete recommendation is calibrated and prospective: separate immutable settled-tree replay from authorized build-change accounting; retain ≥95% raw replay stability over all preregistered rows, full attempted/accounted coverage, exits and both streams, semantic/protected-byte vetoes, and paired adversarial controls; require operator ratification and a pilot before resuming F claims. No three-loop freshness percentage is fabricated.

C23-F02 is now closed by the owner and independently controlled: the citation uses R29's actual lines 11–22 and heading. The final pointer audit passes **41 citations / 40 paths / 12 revision pointers**, with no missing target, bad range or bad revision. The independent numeric/negative/preservation control was also repeated at **2026-10-18T21:58:52Z**, exit 0: twelve pointer controls, nine numeric controls, 1,764 protected paths and zero mismatches. Three additional absence-policy controls passed at **21:57:47Z**, rejecting invented positive citations without planting a file.

The dependency watch began at **2026-10-18T21:53:04Z**, checked every 60 seconds and observed the report at **21:56:04Z**, within three minutes. The section-correction watch completed at **21:59:11Z** after a single 60-second interval. Neither watcher remains running. No late dependency was invented or skipped; the original observations remain above.

## Hash-bound five-block replay

The shell command below repeats the exact inspected count blocks and rejects changed report bytes before executing them. Executed once more after filing this audit; the date is emitted by the command. A parent edit requires a fresh audit and binding, not removal of the digest assertion. This is not a command to run any historical validator.

```sh
export TMPDIR="$PWD/.scratch" PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import re, subprocess
expected = {
    'reports/round-30/loop3-retrospective.md': 'edda7ba51a6793e88f7ce30500cc7ee4e7065cbd2550640c2d7b45d260a7a6f2',
    'reports/round-30/retro/r25-26.md': 'b81d6524fc5c64515c92f09b994dea2fb59c58a44f48fb89df7bcd2f046ea25c',
    'reports/round-30/retro/r27-28.md': 'b36ca943bf938a9ea1c50c3c3b797f9cd460f39cb7dd60b98ae765921a3b91e7',
    'reports/round-30/retro/r29.md': 'c0434d49729c20f442cc53f540be5a18096d18789caeba26323082804daa5228',
}
original, jobs = {}, []
for name, digest in expected.items():
    raw = Path(name).read_bytes()
    assert sha256(raw).hexdigest() == digest, name
    original[name] = raw
    for index, block in enumerate(re.findall(r'```sh\n(.*?)\n```', raw.decode(), re.S), 1):
        jobs.append((name, index, block))
assert len(jobs) == 5
assert expected['reports/round-30/loop3-retrospective.md'] != '487514f29644fa6555f19699619658432fd91b19878353d06fc6afbf325bb118'
def execute(job):
    name, index, block = job
    result = subprocess.run(['bash', '-c', block], text=True, capture_output=True, timeout=60)
    return name, index, result
print('AUDIT_UTC', datetime.now(timezone.utc).isoformat())
with ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(execute, jobs))
for name, index, result in results:
    print(name, index, 'exit', result.returncode)
    print(result.stdout, end='')
    print(result.stderr, end='')
assert all(result.returncode == 0 for _, _, result in results)
assert all(Path(name).read_bytes() == raw for name, raw in original.items())
print('C24 PASS: five safe count blocks; digest bindings unchanged')
PY
```

