# R30-D32 — fragment ledger for parent integration

Date: 2026-10-18. Assignment group: R30-D30..D32 (reviewers + scribe). Axes: evidence completeness, scoped provenance, and D / depth integration. This is a **read-time census**, not an admission, promotion decision, fragment certification or declaration that every worker has finished. No outside-repo path, shared bookkeeping, implementation, pin or filed round-8–29 artifact was written by this worker. No commit or push.

## Census boundary

At **2026-10-18T21:57:44Z**, lane HEAD was `44145d5f337dea425c20dccafee98e0882678660`; the declared baseline remains `87bfc9956f0fc60e6821fe53b622d0043e28be10`. The command below measured **47 files / 808,330 bytes** under the current round. It excludes `__pycache__` and the ledger's own files to avoid a self-hash cycle. The census is sequential and the wave was still writing: each row describes bytes read at this cut, not an atomic or final tree. Re-measure before integration instead of inheriting these hashes.

Partition counts at that cut: **audit 3; craft 6; fixes 5; retro 3; scribe 1; telemetry 10; top-level 19**. All counts and row fingerprints use this command, run on **2026-10-18** with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import hashlib, json, subprocess
base = Path('reports/round-30')
exclude = {str(base / 'scribe/fragment-ledger.md'),
           str(base / 'scribe/fragment-ledger.json')}
rows = []
for path in sorted(base.rglob('*')):
    if not path.is_file() or '__pycache__' in path.parts or str(path) in exclude:
        continue
    data = path.read_bytes()
    rows.append({'path': str(path), 'bytes': len(data),
        'lines': len(data.splitlines()), 'sha256': hashlib.sha256(data).hexdigest(),
        'mtime_utc': datetime.fromtimestamp(path.stat().st_mtime,
            timezone.utc).isoformat(timespec='seconds')})
partitions = Counter((Path(r['path']).relative_to(base).parts[0]
    if len(Path(r['path']).relative_to(base).parts) > 1 else 'top-level') for r in rows)
print(json.dumps({'census_utc': datetime.now(timezone.utc).isoformat(),
    'lane_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
    'files': len(rows), 'bytes': sum(r['bytes'] for r in rows),
    'partitions': dict(sorted(partitions.items())), 'rows': rows}, indent=2))
PY
```

The table paths below are relative to `reports/round-30/`. SHA prefixes are 12 hexadecimal characters for readability; the command emits full SHA-256 values. A fingerprint printer is an inventory, not a new drift gate or an expected verdict.

| Fragment path | Bytes at cut | SHA-256 prefix | mtime UTC |
|---|---:|---|---|
| `adjacency.md` | 11085 | `0d585b9351d6` | 21:55:13 |
| `audit/x38-law-gate-baseline.json` | 43682 | `52a557ad3388` | 21:53:45 |
| `audit/x38-law-gate-clean-state.md` | 4290 | `b6d5f4e9d416` | 21:54:33 |
| `audit/x38-law-gate-clean-state.py` | 10096 | `c17b45f3860f` | 21:54:04 |
| `claims.json` | 2987 | `d506b87b5ff0` | 21:51:37 |
| `craft/review-D26.md` | 7187 | `d967ad0f122b` | 21:57:43 |
| `craft/review-D27.md` | 7349 | `b436e755e7dd` | 21:56:10 |
| `craft/review-D28.md` | 6400 | `580c81283f5b` | 21:57:43 |
| `craft/review-D29-box1.md` | 7678 | `c22d6afaa070` | 21:56:52 |
| `craft/review-D30.md` | 10200 | `dad82c7b42ae` | 21:57:26 |
| `craft/skill-draft.md` | 17665 | `02b820a9fc48` | 21:57:36 |
| `fixes/battery-registration.md` | 9133 | `cef83065d6b8` | 21:56:58 |
| `fixes/qreg-dangles.md` | 3619 | `0fffe1581be5` | 21:54:43 |
| `fixes/speaker-tamper.md` | 23337 | `f2070a10425a` | 21:57:05 |
| `fixes/telemetry-convention.md` | 5353 | `ab25fd06b1b9` | 21:55:23 |
| `fixes/x63-f2.md` | 8442 | `10c2b9f2fdf3` | 21:53:40 |
| `log-draft.md` | 3754 | `0435e7523ad0` | 21:55:48 |
| `loop3-retrospective.md` | 35929 | `92a36bcd1763` | 21:57:25 |
| `regression-initial.json` | 116620 | `aff2cba3b7c5` | 21:55:30 |
| `regression.json` | 116620 | `aff2cba3b7c5` | 21:54:35 |
| `report-draft.md` | 9740 | `489fa2c1e4e4` | 21:57:39 |
| `rerun.json` | 17014 | `bc1dd07e4364` | 21:57:39 |
| `retro/r25-26.md` | 12120 | `b81d6524fc5c` | 21:54:07 |
| `retro/r27-28.md` | 13148 | `b36ca943bf93` | 21:55:29 |
| `retro/r29.md` | 13594 | `c0434d49729c` | 21:56:07 |
| `retrospective-audit-C23-C25.py` | 14354 | `316afc30dadd` | 21:57:31 |
| `retrospective-audit-C23.md` | 6434 | `d4a676b8c4ed` | 21:56:54 |
| `retrospective-audit-C24.md` | 10040 | `09661dba0347` | 21:56:54 |
| `retrospective-audit-C25.md` | 2011 | `ebfcf37a8220` | 21:55:25 |
| `run-validation.py` | 44455 | `7b45181842b4` | 21:57:15 |
| `scope.md` | 15253 | `9adcb8c66bc1` | 21:57:07 |
| `scorecard-draft.md` | 4422 | `cbb1c49b988f` | 21:55:25 |
| `scribe/capability-row.md` | 5063 | `be9ccf009481` | 21:57:26 |
| `targets.json` | 174 | `c03e9c9563a9` | 21:51:37 |
| `telemetry/check-dispatch.py` | 7784 | `c13a04051846` | 21:54:54 |
| `telemetry/check.json` | 219 | `032e4a5c4a87` | 21:54:42 |
| `telemetry/control-receipt.json` | 3225 | `c897ab16e63d` | 21:55:11 |
| `telemetry/controls.json` | 1934 | `d5df29a0766f` | 21:54:42 |
| `telemetry/dispatch-declaration-x37.json` | 3688 | `4b7a9c13f1e4` | 21:54:54 |
| `telemetry/dispatch-stats.json` | 2389 | `a1f8ec193661` | 21:54:42 |
| `telemetry/dispatch-telemetry.py` | 10531 | `a177757b3680` | 21:54:10 |
| `telemetry/inputs/claims.json` | 2987 | `d506b87b5ff0` | 21:54:32 |
| `telemetry/inputs/targets.json` | 174 | `c03e9c9563a9` | 21:54:32 |
| `telemetry/worker-observation.json` | 1207 | `bfcd8693dca9` | 21:54:10 |
| `validation.json` | 123245 | `c2560021d57e` | 21:56:22 |
| `verify-operability.py` | 28267 | `ba2ea0b974d9` | 21:57:41 |
| `verify.md` | 3432 | `08d60251e863` | 21:56:58 |

## Integration map and ownership qualifications

These are routing pointers, not authorizations to edit another seat's files. Ownership outside this worker's files is inferred from the declaration/path/fragment role; the parent remains integrator of record.

- **O / routed fixes:** `reports/round-30/fixes/qreg-dangles.md`, `reports/round-30/fixes/battery-registration.md`, `reports/round-30/fixes/speaker-tamper.md`, `reports/round-30/fixes/x63-f2.md`, `reports/round-30/fixes/telemetry-convention.md`. Combine the actual owner receipts into the parent-owned routed-resolution ledger; presence alone is not closure. The broader R29 open queue is not exhausted by this bounded list.
- **C / retrospective:** `reports/round-30/retro/r25-26.md`, `reports/round-30/retro/r27-28.md`, `reports/round-30/retro/r29.md` feed `reports/round-30/loop3-retrospective.md`; the `retrospective-audit-C23.md`, `retrospective-audit-C24.md`, and `retrospective-audit-C25.md` reports are independent facets, not automatic approval of a later unseen edit.
- **D / synthesis:** `reports/round-30/craft/skill-draft.md` is the orchestrator's landing input. The D26 stratum, D27 law, D28 composition, D29 box-1 and D30 adversarial reviews retain their own dates and scope. `reports/round-30/scribe/capability-row.md` is a repertoire-row draft, not a new admitted capability or a promotion mark.
- **Cross-cutting:** `reports/round-30/scope.md`, `reports/round-30/adjacency.md`, `reports/round-30/verify.md`, `reports/round-30/audit/x38-law-gate-clean-state.md` and the actual command receipts qualify different claims. `reports/round-30/report-draft.md`, `reports/round-30/log-draft.md`, `reports/round-30/scorecard-draft.md` are parent integration drafts, not shared-bookkeeping writes by this scribe.
- **Telemetry:** files are durable under the declared round's telemetry partition. A dispatch declaration, a single worker's local observation, and measured completed worker usage are different evidence types; no fleet-wide availability/completion count is inferred from their presence.

## Read-set movement and remaining integration

This census immediately became historical: at the **2026-10-18T21:58:44Z** dependency poll, the synthesis draft was already `a6e8a69a4d465de9087752c5c533c9f4138d79e846d1cd5d0668a6fdbc02b5ad` rather than the table's `02b820a9…`. At **21:59:04Z**, its citation/control reproduction was checked again; `reports/round-30/craft/review-D30.md` records the later review and the addressed historical-packet wording. That follow-up also changed this worker's review and capability draft after the census. The older rows are preserved here rather than falsely presented as their final hashes.

The same poll still found pre-integration `SKILL.md` SHA-256 `2d85bfea6e6a7503b4267b84fda5f393ed14e1a3f5eae108940e7fad8adb6048`, with no landed Register craft subsection. The parent owns that landing and the **post-landing** box-1 re-survey and counting-command run. A virtual append or a draft review is not that delivered result. Final acceptance remains `python3 reports/round-30/run-validation.py` on the settled deliverable; this ledger cannot substitute for it.

Dependencies were sampled on 60-second polls while this worker performed its other review work. This handoff deliberately does not block on the parent's own integration, and declares no incomplete O dependency green. The worker's authored deliverables are confined to `reports/round-30/craft/review-D30.md`, `reports/round-30/scribe/capability-row.md`, and this ledger.

## Final handoff checks (2026-10-18T22:00Z)

At **22:00:07Z**, this ledger's actual command was extracted from its delivered Markdown and executed. The live recount was **51 files / 972,035 bytes**, still excluding the ledger's own files and caches, with partitions audit 4 / craft 6 / fixes 5 / retro 3 / scribe 1 / telemetry 10 / top-level 22. This later census supersedes neither the earlier table nor any historical result; it demonstrates why the parent must re-measure the moving wave. A separate assertion over the filed Markdown table confirmed its **47 rows sum to 808,330 bytes**.

The same check used the actual round runner's `local_references` and `audit_candidates` functions: all concrete local citations in this worker's three deliverables resolved, and the D30 review qualified as a dated, evidence-carrying Register craft review. The complete synthesis was then re-read at **22:00:28Z**, SHA-256 `e14e27fb90042b20d218a184a9d992f3063491720da74d82919d1dd9df72c519`: both D30 precision conditions are now addressed. The review records the final composition verdict and actual adapter/acceptance-selftest controls. At **22:00:20Z** the parent-owned SKILL landing was still pending; the capability row remains conditional on that landing and the final delivery checks.
