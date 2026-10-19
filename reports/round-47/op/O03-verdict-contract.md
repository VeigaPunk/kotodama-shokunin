# O03 — verdict + exit contract (freshness gate, part 3/3)

- Seat: `O03` | role executor | claim `O` | round 47, loop 2
- Out path: `reports/round-47/op/O03-verdict-contract.md` — the only file this seat writes under `reports/round-47/`
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`; `git rev-parse 6e9a30d^{commit}` returned the same)
- Date: 2026-10-19
- Boundary: no filed byte edited, nothing staged under `corpus/`, no round runner executed, no git-mutating or network command. Executions were read-only inspection commands plus `python3 -B` on files under `.scratch/o03/`.

## 1. What this fragment owns

Part 3/3 of `tools/harness/claims-freshness.py`, per `reports/round-47/targets.json:35` and the O claim at `reports/round-47/claims.json:37-47`. This block owns the **decision layer only**:

- normalization of a probe result into `HOLDS | CONTRADICTED | NOT_EVALUATED`;
- the per-claim verdict and the run-level verdict;
- the exit-code mapping and the refusal sentence;
- the machine-readable report shape and the human render.

It does **not** own claim parsing or baseline resolution (part 1, O01), the probe vocabulary and `before_checks` schema (part 2, O02), the selftest control set (O04), the r43 demonstration (O05), the negative control (O06), the anti-theater mutation (O07), or the integrator's apply (W01). It is deliberately pure: no `git`, no filesystem, no import of the probe registry. That is what makes the decision rules testable without a corpus, and what keeps them from drifting when probe implementations change.

## 2. The contract in one table

| condition | per-claim verdict | run verdict | exit | dispatch |
|---|---|---|---|---|
| schema error, missing/blank `before`, duplicate id, bad baseline sha | `malformed` | `malformed` if it is the highest | 2 | refuse |
| `claims` is empty | — | `malformed` | 2 | refuse |
| any clause `CONTRADICTED` | `stale` | `stale` unless a malformed exists | 1 | refuse |
| no contradiction, any clause `NOT_EVALUATED` | `could-not-evaluate` | `could-not-evaluate` unless stale/malformed exists | 3 | refuse |
| `before_checks` missing or empty | `could-not-evaluate` | as above | 3 | refuse |
| every declared clause `HOLDS` (at least one) | `fresh` | `fresh` only if every claim is fresh | 0 | allow |

Precedence, high to low: **malformed > stale > could-not-evaluate > fresh**. Cross-claim aggregation is `max` under that order; the report keeps every claim's individual verdict.

Two edges are the reason this contract exists:

1. **A claim with no checks is not fresh.** Zero declared checks is `could-not-evaluate`, a distinct non-zero outcome. The round's own threshold says it: "could-not-evaluate != green (exits non-zero when no checks declared)" (`reports/round-47/claims.json:47`). The r44 contract says the same: "`could-not-evaluate` must not exit 0" (`reports/round-44/review/R01-review.md:246`).
2. **One contradiction dominates.** A claim whose counts hold but whose ownership clause is false is `stale`; partial truth is not freshness. That is exactly the r43 C shape — myth-symbol 26 and total 223 held, the lithic ownership premise did not (`reports/round-44/review/R01-review.md:228-231`).

## 3. Clause-level rules

- **Closed status set.** `HOLDS`, `CONTRADICTED`, `NOT_EVALUATED`, case-insensitively normalized. Anything else — `PASS`, `OK`, `None`, a missing key — is an evaluator contract violation and becomes `NOT_EVALUATED`, never `HOLDS`. A probe that returns nonsense cannot make a claim green.
- **`CONTRADICTED` is the only path to `STALE`.** It means the probe measured a value that contradicts the claim's declared `expected` polarity.
- **`NOT_EVALUATED` carries a reason.** If a probe omits one, the layer supplies `not-evaluated: probe supplied no reason`.
- **Strict JSON projection.** Measured/expected values pass through `json_safe`: tuples/sets become sorted lists, dict keys are string-sorted, non-finite floats (`NaN`, `Infinity`) and foreign objects are rejected. If projection fails, the clause becomes `NOT_EVALUATED` with the type error as its reason — an unrepresentable measurement is not a pass.
- **Cardinality.**
  - Fewer results than checks: the missing clauses are padded `NOT_EVALUATED` (`not-run: the harness returned no result`), so the claim is `could-not-evaluate`.
  - More results than checks: the claim is `could-not-evaluate` with `result-count-exceeds-checks`; extras are not silently dropped.
- **Counters.** `checks_declared` counts declared clauses; `checks_evaluated` counts results actually supplied; `holds + contradicted + not_evaluated == checks_declared` always.

What this block cannot do: catch an exception thrown inside a probe evaluator. Part 1/2 must wrap each `evaluate_check` call and return `NOT_EVALUATED` with the exception text. An exception that escapes to `main` must produce exit 2 or 3, never 0. This is repeated in §10 because it is the one hole the pure layer cannot close.

## 4. Exit contract

| code | constant | meaning | green? |
|---|---|---|---|
| 0 | `EXIT_FRESH` | every claim fresh; every declared clause holds at the declared baseline | yes |
| 1 | `EXIT_STALE` | at least one contradicted clause; no malformed input | no |
| 2 | `EXIT_MALFORMED` | the input cannot be evaluated as declared: unreadable/non-JSON, missing `baseline_commit`, unresolvable baseline ref, missing `before`, unknown probe kind, missing polarity, duplicate claim id, empty `claims`, non-40-hex resolved sha | no |
| 3 | `EXIT_NOT_EVALUATED` | no contradiction and no malformed input, but at least one claim has no checks or an unevaluated clause | no |

**Why a fourth code.** The six-part contract names 0/1/2 and requires `could-not-evaluate` to be non-zero (`reports/round-44/review/R01-review.md:246`). It does not assign the unevaluated state a code. Reusing 2 would conflate "the input is broken" with "the input is valid but incomplete", and the repo's gate convention already uses 2 for unevaluated (`tools/gates/argot-derivation-gate.py:105-107`: `EXIT_UNEVALUATED = 2`). Code 3 preserves the mandated 0/1/2 and gives the unevaluated state its own non-zero value. `tools/harness/receipt_guard.py:34` already uses 3 as a refusal code, so the number has precedent in this tree.

**The scratch prototype's exit map is not the durable contract.** `.scratch/ca01/claims-freshness.py:69-76` defines `1 = usage/input`, `2 = stale`, `3 = unverifiable`, and offers `--allow-unverifiable` (`:74`, `:890`) to "downgrade" it. The r47 contract mandates `1 = stale`, `2 = malformed`; a direct port would invert the two most consequential outcomes, and the downgrade flag would let `could-not-evaluate` exit 0. Keep the prototype's method — baseline evaluation through git, typed probes — and replace its exit surface and its allow flags.

**No green escape hatches.** The durable CLI must not offer `--force`, `--allow-stale`, `--allow-unverifiable`, or any option that returns 0 with a non-fresh verdict. If part 1 retains a diagnostic `--at REF`, it must (a) record `deviation` in the report and (b) cap the best possible exit at 3; it may still return 1 on a contradiction, never 0. The prototype's `--at worktree` (`:888`) is precisely the worktree-evaluation path the r47 contract forbids (`reports/round-47/claims.json:39`).

## 5. Report shape

`build_report` emits:

- `schema` — `kotodama-claims-freshness-report-v1`
- `round`, `baseline_commit` (as declared), `baseline_sha` (resolved 40-hex)
- `run_verdict`, `exit_code`, `refuse`, `refusal`
- `summary` — claim counts by verdict, clause counts by status, `document_errors`
- `claims[]` — `id`, `axis`, `before`, `owner`, `verdict`, `checks_declared`, `checks_evaluated`, `counts`, `clauses[]`, `failing_clauses[]`, `not_evaluated_clauses[]`, `errors[]`, and `unevaluated_reason` when applicable
- `errors[]` — document-level malformed reasons
- `decision_sha256` — SHA-256 over the canonical JSON of the report minus this field (`sort_keys`, compact separators, UTF-8)

There is no timestamp in the decision surface. Two runs on identical inputs produce the same `decision_sha256` and the same exit code, so O14 can assert digest equality rather than "both runs looked stale". Claim order is input order; clause order is declaration order; failing-clause lists preserve declaration order.

The human render is line-oriented: one line per claim, indented lines for failing/unevaluated clauses, a summary line, then the refusal (if any) and `exit N`.

## 6. Tool draft — part 3/3

The block below is the deliverable. It is byte-identical to the tested `.scratch/o03/verdict_part3.py` (487 lines, sha256 `097a31987cc334d93eaa117e60d7112cddeb7fbf9a356d10ca4dc178721cfcef`).

````python
# =============================================================================
# Part 3/3 -- verdict + exit contract        (r47 claim O; defect R01-43-12)
# =============================================================================
# Integration seam.  This block is pure decision algebra and imports neither
# git nor the probe registry:
#
#   part 1 (core)   load_claims(path) -> (header, claims)
#                   resolve_baseline(ref) -> 40-hex sha
#   part 2 (probes) validate_check(check, claim_id, index) -> list[str]
#                   evaluate_check(check, baseline) -> ClauseResult
#   part 3 (this)   judge_claim / run_verdict / build_report / render_human
#
# ClauseResult is duck-typed: a mapping or object carrying
#   status    HOLDS | CONTRADICTED | NOT_EVALUATED
#   measured  value re-derived at baseline_commit
#   expected  value declared by the claim (the polarity)
#   reason    required prose for NOT_EVALUATED
# Any other status is an evaluator contract violation and is downgraded to
# NOT_EVALUATED -- never to HOLDS.
# =============================================================================

from __future__ import annotations

import hashlib
import json
import math

FRESH = "fresh"
STALE = "stale"
COULD_NOT_EVALUATE = "could-not-evaluate"
MALFORMED = "malformed"

EXIT_FRESH = 0
EXIT_STALE = 1
EXIT_MALFORMED = 2
EXIT_NOT_EVALUATED = 3

EXIT_BY_VERDICT = {
    FRESH: EXIT_FRESH,
    STALE: EXIT_STALE,
    MALFORMED: EXIT_MALFORMED,
    COULD_NOT_EVALUATE: EXIT_NOT_EVALUATED,
}

# Precedence, low to high.  A malformed file cannot yield a trustworthy
# verdict at all; a measured contradiction outranks "not evaluated"; an
# unevaluated claim outranks "fresh".
_RANK = {FRESH: 0, COULD_NOT_EVALUATE: 1, STALE: 2, MALFORMED: 3}

REPORT_SCHEMA = "kotodama-claims-freshness-report-v1"

_CLAUSE_STATUS = ("HOLDS", "CONTRADICTED", "NOT_EVALUATED")


def _get(obj, name, default=None):
    if isinstance(obj, dict):
        return obj.get(name, default)
    return getattr(obj, name, default)


def _clip(text, limit=240):
    text = " ".join(str(text or "").split())
    return text if len(text) <= limit else text[: limit - 1] + "\u2026"


def json_safe(value):
    """Deterministic JSON projection.  Raises TypeError on foreign objects."""
    if value is None or isinstance(value, (bool, int, str)):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise TypeError("non-finite float is not strict JSON: %r" % value)
        return value
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return [json_safe(item) for item in sorted(value, key=repr)]
    if isinstance(value, dict):
        return {
            str(key): json_safe(value[key])
            for key in sorted(value, key=lambda k: str(k))
        }
    raise TypeError("not JSON-serialisable: %s" % type(value).__name__)


def normalise_clause_result(result):
    """(status, measured, expected, reason) with status in _CLAUSE_STATUS."""
    status = _get(result, "status", "")
    status = status.strip().upper() if isinstance(status, str) else ""
    measured = _get(result, "measured")
    expected = _get(result, "expected")
    reason = _get(result, "reason", "") or ""
    if status not in _CLAUSE_STATUS:
        return (
            "NOT_EVALUATED",
            measured,
            expected,
            "evaluator-contract-violation: status %r is not one of %s"
            % (status, "/".join(_CLAUSE_STATUS)),
        )
    if status == "NOT_EVALUATED" and not reason:
        reason = "not-evaluated: probe supplied no reason"
    return status, measured, expected, reason


def _target_text(check):
    if not isinstance(check, dict):
        return ""
    target = check.get("target", check.get("path", check.get("glob", "")))
    try:
        return _clip(json.dumps(target, sort_keys=True))
    except (TypeError, ValueError):
        return _clip(target)


def clause_row(index, check, result):
    """One auditable row; measured/expected are JSON-safe or NOT_EVALUATED."""
    status, measured, expected, reason = normalise_clause_result(result)
    check = check if isinstance(check, dict) else {}
    try:
        measured = json_safe(measured)
        expected = json_safe(expected)
    except TypeError as exc:
        status = "NOT_EVALUATED"
        reason = ("%s; " % reason if reason else "") + str(exc)
        measured, expected = None, None
    return {
        "index": index,
        "clause": _clip(check.get("clause", "")),
        "probe": str(
            check.get("probe", check.get("probe_kind", check.get("kind", "?")))
        ),
        "target": _target_text(check),
        "status": status,
        "expected": expected,
        "measured": measured,
        "reason": _clip(reason, 400),
        "evidence": _clip(check.get("evidence", "")),
    }


def judge_claim(
    claim_id,
    checks,
    results=None,
    *,
    axis=None,
    before="",
    schema_errors=(),
    owner=None,
):
    """Return the per-claim verdict row.

    Rules, in order:
      * any schema error or a missing/blank `before` -> MALFORMED
      * zero declared checks                         -> COULD_NOT_EVALUATE
      * any CONTRADICTED clause                      -> STALE
      * any NOT_EVALUATED clause                     -> COULD_NOT_EVALUATE
      * every clause HOLDS                           -> FRESH
    """
    checks = list(checks or [])
    results = list(results or [])
    errors = [str(err) for err in (schema_errors or [])]
    if not isinstance(claim_id, str) or not claim_id.strip():
        errors.append("claim id is missing or not a string")
    if not isinstance(before, str) or not before.strip():
        errors.append("claim has no non-empty `before` assertion")
    if errors:
        return {
            "id": claim_id,
            "axis": axis,
            "before": before,
            "owner": owner or claim_id,
            "verdict": MALFORMED,
            "checks_declared": len(checks),
            "checks_evaluated": 0,
            "counts": {"holds": 0, "contradicted": 0, "not_evaluated": 0},
            "clauses": [],
            "failing_clauses": [],
            "not_evaluated_clauses": [],
            "errors": errors,
        }

    if not checks:
        return {
            "id": claim_id,
            "axis": axis,
            "before": before,
            "owner": owner or claim_id,
            "verdict": COULD_NOT_EVALUATE,
            "checks_declared": 0,
            "checks_evaluated": 0,
            "counts": {"holds": 0, "contradicted": 0, "not_evaluated": 0},
            "clauses": [],
            "failing_clauses": [],
            "not_evaluated_clauses": [],
            "unevaluated_reason": (
                "no before_checks declared; a claim with no declared checks "
                "is not fresh"
            ),
            "errors": [],
        }

    if len(results) > len(checks):
        return {
            "id": claim_id,
            "axis": axis,
            "before": before,
            "owner": owner or claim_id,
            "verdict": COULD_NOT_EVALUATE,
            "checks_declared": len(checks),
            "checks_evaluated": 0,
            "counts": {"holds": 0, "contradicted": 0, "not_evaluated": len(checks)},
            "clauses": [],
            "failing_clauses": [],
            "not_evaluated_clauses": [],
            "unevaluated_reason": (
                "result-count-exceeds-checks: %d results for %d checks"
                % (len(results), len(checks))
            ),
            "errors": [],
        }

    rows = []
    for index, check in enumerate(checks):
        if index < len(results):
            rows.append(clause_row(index, check, results[index]))
        else:
            rows.append(
                clause_row(
                    index,
                    check,
                    {
                        "status": "NOT_EVALUATED",
                        "reason": "not-run: the harness returned no result",
                    },
                )
            )

    failing = [row for row in rows if row["status"] == "CONTRADICTED"]
    unevaluated = [row for row in rows if row["status"] == "NOT_EVALUATED"]
    holds = [row for row in rows if row["status"] == "HOLDS"]

    if failing:
        verdict = STALE
    elif unevaluated:
        verdict = COULD_NOT_EVALUATE
    else:
        verdict = FRESH

    row = {
        "id": claim_id,
        "axis": axis,
        "before": before,
        "owner": owner or claim_id,
        "verdict": verdict,
        "checks_declared": len(checks),
        "checks_evaluated": min(len(results), len(checks)),
        "counts": {
            "holds": len(holds),
            "contradicted": len(failing),
            "not_evaluated": len(unevaluated),
        },
        "clauses": rows,
        "failing_clauses": failing,
        "not_evaluated_clauses": unevaluated,
        "errors": [],
    }
    if verdict == COULD_NOT_EVALUATE:
        row["unevaluated_reason"] = (
            "%d of %d declared clauses not evaluated"
            % (len(unevaluated), len(checks))
        )
    return row


def run_verdict(claim_rows):
    """Aggregate per-claim verdicts; malformed > stale > unevaluated > fresh."""
    rows = list(claim_rows or [])
    if not rows:
        return MALFORMED
    return max((row["verdict"] for row in rows), key=_RANK.__getitem__)


def exit_code(verdict):
    try:
        return EXIT_BY_VERDICT[verdict]
    except KeyError:
        raise ValueError("unknown verdict: %r" % (verdict,))


def _refusal(verdict, rows, baseline_commit, errors=()):
    at = baseline_commit or "unresolved baseline"
    if verdict == FRESH:
        return None
    if verdict == MALFORMED:
        bad = [row["id"] for row in rows if row["verdict"] == MALFORMED]
        subject = "claim(s) %s are" % ", ".join(map(str, bad)) if bad else "input is"
        detail = "; ".join(str(err) for err in errors[:3])
        suffix = (": " + detail) if detail else ""
        return (
            "REFUSE: %s malformed at %s%s; exit 2 -- no freshness verdict is "
            "possible." % (subject, at, suffix)
        )
    if verdict == STALE:
        stale = [row["id"] for row in rows if row["verdict"] == STALE]
        text = (
            "REFUSE: claim(s) %s have a `before` already false at %s; "
            "do not dispatch." % (", ".join(map(str, stale)), at)
        )
        stuck = [row["id"] for row in rows if row["verdict"] == COULD_NOT_EVALUATE]
        if stuck:
            text += (
                " Claim(s) %s could not be evaluated either."
                % ", ".join(map(str, stuck))
            )
        return text
    stuck = [row["id"] for row in rows if row["verdict"] == COULD_NOT_EVALUATE]
    return (
        "REFUSE: claim(s) %s could not be evaluated at %s (no declared checks "
        "or probe failure); absence of a verdict is not freshness."
        % (", ".join(map(str, stuck)), at)
    )


def _summary(rows, errors=()):
    summary = {
        "claims": len(rows),
        "fresh": 0,
        "stale": 0,
        "could_not_evaluate": 0,
        "malformed": 0,
        "clauses": 0,
        "holds": 0,
        "contradicted": 0,
        "not_evaluated": 0,
        "document_errors": len(errors),
    }
    for row in rows:
        key = row["verdict"].replace("-", "_")
        if key in summary:
            summary[key] += 1
        counts = row.get("counts", {})
        summary["clauses"] += row.get("checks_declared", 0)
        summary["holds"] += counts.get("holds", 0)
        summary["contradicted"] += counts.get("contradicted", 0)
        summary["not_evaluated"] += counts.get("not_evaluated", 0)
    return summary


def _decision_digest(report):
    body = {key: value for key, value in report.items() if key != "decision_sha256"}
    canonical = json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def build_report(
    claim_rows,
    *,
    round_id=None,
    baseline_commit=None,
    baseline_sha=None,
    document_errors=(),
):
    """Assemble the machine-readable report from per-claim verdict rows."""
    rows = list(claim_rows or [])
    errors = [str(err) for err in (document_errors or [])]

    seen = set()
    for row in rows:
        claim_id = row.get("id")
        if claim_id in seen:
            errors.append("duplicate claim id: %s" % claim_id)
        seen.add(claim_id)

    if baseline_sha is not None and (
        not isinstance(baseline_sha, str)
        or len(baseline_sha) != 40
        or any(ch not in "0123456789abcdef" for ch in baseline_sha)
    ):
        errors.append(
            "baseline_sha is not a 40-hex commit id: %r" % (baseline_sha,)
        )

    verdict = run_verdict(rows)
    if errors:
        verdict = MALFORMED

    report = {
        "schema": REPORT_SCHEMA,
        "round": round_id,
        "baseline_commit": baseline_commit,
        "baseline_sha": baseline_sha,
        "run_verdict": verdict,
        "exit_code": exit_code(verdict),
        "refuse": verdict != FRESH,
        "refusal": _refusal(verdict, rows, baseline_commit, errors),
        "summary": _summary(rows, errors),
        "claims": rows,
        "errors": errors,
    }
    report["decision_sha256"] = _decision_digest(report)
    return report


def malformed_report(reason, *, round_id=None, baseline_commit=None):
    """Uniform report for input that never reached claim evaluation (exit 2)."""
    return build_report(
        [],
        round_id=round_id,
        baseline_commit=baseline_commit,
        baseline_sha=None,
        document_errors=[reason],
    )


def render_human(report):
    lines = [
        "claims-freshness: round %s baseline %s (%s)"
        % (
            report.get("round"),
            report.get("baseline_commit") or "unresolved",
            report.get("baseline_sha") or "unresolved",
        )
    ]
    for row in report.get("claims", []):
        counts = row.get("counts", {})
        verdict = row["verdict"]
        if verdict == FRESH:
            detail = "%d/%d clauses hold" % (
                counts.get("holds", 0),
                row.get("checks_declared", 0),
            )
        elif verdict == STALE:
            detail = "%d/%d clauses contradict" % (
                counts.get("contradicted", 0),
                row.get("checks_declared", 0),
            )
        elif verdict == COULD_NOT_EVALUATE:
            detail = row.get("unevaluated_reason") or "%d clause(s) not evaluated" % (
                counts.get("not_evaluated", 0),
            )
        else:
            detail = "; ".join(row.get("errors", [])) or "malformed"
        lines.append("  [%s] %-17s %s" % (row.get("id"), verdict.upper(), detail))
        for clause in row.get("failing_clauses", []):
            lines.append(
                "      clause %d (%s): measured=%r expected=%r -- %s"
                % (
                    clause["index"],
                    clause["probe"],
                    clause["measured"],
                    clause["expected"],
                    clause["clause"],
                )
            )
        for clause in row.get("not_evaluated_clauses", []):
            lines.append(
                "      clause %d (%s) NOT EVALUATED: %s"
                % (clause["index"], clause["probe"], clause["reason"])
            )
    summary = report.get("summary", {})
    text = (
        "summary: %d fresh, %d stale, %d could-not-evaluate, %d malformed; "
        "clauses %d (%d hold, %d contradict, %d not evaluated)"
        % (
            summary.get("fresh", 0),
            summary.get("stale", 0),
            summary.get("could_not_evaluate", 0),
            summary.get("malformed", 0),
            summary.get("clauses", 0),
            summary.get("holds", 0),
            summary.get("contradicted", 0),
            summary.get("not_evaluated", 0),
        )
    )
    if summary.get("document_errors"):
        text += "; %d document error(s)" % summary["document_errors"]
    lines.append(text)
    for error in report.get("errors", []):
        lines.append("error: %s" % error)
    if report.get("refusal"):
        lines.append(report["refusal"])
    lines.append("exit %d" % report["exit_code"])
    return "\n".join(lines)
````

## 7. Evidence: what I actually ran

Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root.

```
$ python3 -B .scratch/o03/drive_o03.py
ok    r43 run verdict is STALE
ok    r43 exit code is 1
ok    r43 O is STALE
ok    r43 C is STALE
ok    r43 Ca is FRESH (not flagged)
ok    r43 summary 1 fresh / 2 stale
ok    r43 refusal names O and C, not Ca
ok    negative control is FRESH
ok    negative control exits 0
ok    fresh report has no refusal
ok    zero checks -> COULD-NOT-EVALUATE
ok    zero checks -> exit 3 (non-zero)
ok    zero checks refuses
ok    one not-evaluated clause -> CNE
ok    contradiction outranks not-evaluated within a claim
ok    stale outranks CNE across claims
ok    missing `before` -> MALFORMED
ok    schema error -> MALFORMED
ok    malformed outranks stale across claims
ok    duplicate claim ids -> MALFORMED
ok    short baseline_sha -> MALFORMED
ok    unparseable JSON report -> exit 2
ok    malformed report carries the reason
ok    unknown evaluator status downgrades to CNE, never HOLDS
ok    missing evaluator result -> CNE
ok    extra evaluator result -> CNE
ok    non-JSON measured value -> CNE
ok    non-finite float -> CNE
ok    checks_evaluated counts only supplied results
ok    empty claims list -> MALFORMED exit 2
ok    same inputs -> same decision digest
ok    same inputs -> same exit
ok    report carries no timestamp

selftest 33/33 PASS
$ echo $?
0
```

### 7.1 r43 positive-regression fixture

The fixture values are the measurements R01 recorded at `7ceff59` (`reports/round-44/review/R01-review.md:222-235`), transcribed into `ClauseResult` objects. **This seat did not re-measure git**; the control proves the verdict rules, not the probe registry. O05/O08 must re-derive the same values through the assembled tool against `reports/round-43/claims.json`.

- O: two clauses, both contradicted — durable resolver exists (measured `True` vs expected `False`); the wrapped field reads 4 tokens (measured `4` vs expected `0`).
- C: three clauses, one contradicted — myth-symbol 26 holds, total 223 holds, the lithic ownership-absence probe measured `False` (an owner exists) against the asserted `True` (unowned).
- Ca: one clause holds — the dispositions artifact is absent at `7ceff59`.

Rendered report:

```
claims-freshness: round 43 baseline 7ceff59 (7ceff59a0216a8ea21ee43262d9fc72abf770cee)
  [O] STALE             2/2 clauses contradict
      clause 0 (capability_present): measured=True expected=False -- no durable instrument implements the basename-couples policy
      clause 1 (count_eq): measured=4 expected=0 -- the single wrapped couples field reads 0/4 tokens
  [C] STALE             1/3 clauses contradict
      clause 2 (topic_owner_absent): measured=False expected=True -- lithic slot named but unbuilt
  [Ca] FRESH             1/1 clauses hold
summary: 1 fresh, 2 stale, 0 could-not-evaluate, 0 malformed; clauses 6 (3 hold, 3 contradict, 0 not evaluated)
REFUSE: claim(s) O, C have a `before` already false at 7ceff59; do not dispatch.
exit 1
```

### 7.2 Negative control

Three claims, four clauses, all hold at `c9f4eaa` → `fresh`, exit 0, no refusal:

```
claims-freshness: round 47 baseline c9f4eaa (c9f4eaa707b6e977ff6e1616463e91f4b8afea5d)
  [O] FRESH             2/2 clauses hold
  [C] FRESH             1/1 clauses hold
  [Ca] FRESH             1/1 clauses hold
summary: 3 fresh, 0 stale, 0 could-not-evaluate, 0 malformed; clauses 4 (4 hold, 0 contradict, 0 not evaluated)
exit 0
```

### 7.3 Could-not-evaluate

Zero declared checks:

```
claims-freshness: round 47 baseline 6e9a30d (6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe)
  [U] COULD-NOT-EVALUATE no before_checks declared; a claim with no declared checks is not fresh
summary: 0 fresh, 0 stale, 1 could-not-evaluate, 0 malformed; clauses 0 (0 hold, 0 contradict, 0 not evaluated)
REFUSE: claim(s) U could not be evaluated at 6e9a30d (no declared checks or probe failure); absence of a verdict is not freshness.
exit 3
```

### 7.4 Malformed

Unparseable JSON, through `malformed_report`:

```
claims-freshness: round 47 baseline unresolved (unresolved)
summary: 0 fresh, 0 stale, 0 could-not-evaluate, 0 malformed; clauses 0 (0 hold, 0 contradict, 0 not evaluated); 1 document error(s)
error: Expecting value: line 1 column 1 (char 0)
REFUSE: input is malformed at unresolved baseline: Expecting value: line 1 column 1 (char 0); exit 2 -- no freshness verdict is possible.
exit 2
```

## 8. Integration seam

The assembled `main` should look like this. The names are the contract between O01, O02 and this block; if their fragments choose different names, the adapter belongs in the assembly, not in a rewrite of the decision rules.

```python
header, claims = load_claims(path)                          # part 1
baseline_sha = resolve_baseline(header["baseline_commit"])   # part 1
rows = []
for claim in claims:
    checks = claim.get("before_checks", [])
    errors = []
    for index, check in enumerate(checks):
        errors += validate_check(check, claim["id"], index)  # part 2
    results = [] if errors else [
        evaluate_check(check, baseline) for check in checks  # part 2
    ]
    rows.append(
        judge_claim(
            claim["id"], checks, results,
            axis=claim.get("axis"),
            before=claim.get("before", ""),
            schema_errors=errors,
        )
    )
report = build_report(
    rows,
    round_id=header.get("round"),
    baseline_commit=header["baseline_commit"],
    baseline_sha=baseline_sha,
)
print(json.dumps(report, indent=2, sort_keys=True) if args.json else render_human(report))
return report["exit_code"]
```

On a parse or baseline-resolution failure, part 1 must return the uniform shape:

```python
report = malformed_report(str(exc), round_id=header.get("round"),
                          baseline_commit=header.get("baseline_commit"))
print(json.dumps(report, indent=2, sort_keys=True) if args.json else render_human(report))
return 2
```

Collision notes for the assembler:

- If part 1 defines `MalformedInput`, keep that one class. Part 3 does not define an exception class.
- `json_safe`, `_clip`, `_get`, `clause_row`, `judge_claim`, `run_verdict`, `exit_code`, `build_report`, `malformed_report`, `render_human` are the public/private names this block introduces. If part 2 defines a same-named helper, keep one copy; the semantics above are the requirement.
- Probe-kind key: this block accepts `probe`, `probe_kind`, or `kind` for display only. O02's `validate_check` is authoritative; pick one canonical key in the schema and use it in the demos.
- Splice order: part 1, part 2, part 3. If a constant name collides (`FRESH`, `STALE`), the integrator should rename the part-3 constants with a `CLAIM_` prefix rather than duplicate them.

## 9. Verifier hooks

| seat | assertion this block supports |
|---|---|
| O08 | assembled tool on `reports/round-43/claims.json` → O and C `stale`, Ca `fresh`, exit 1; negative control → exit 0 |
| O10 | exit 0 only when every claim is fresh; 1 on stale; 2 on malformed; 3 on could-not-evaluate; no combination returns 0 with a non-fresh verdict |
| O13 | an unknown probe kind must reach this block as a schema error → malformed (2), not as a silent `NOT_EVALUATED` |
| O14 | two identical runs → identical `decision_sha256` and exit; the report carries no timestamp |
| O15 | no `baseline_commit`, a claim without `before`, and non-JSON → each exit 2 via `malformed_report` or `judge_claim`'s malformed path |
| X03 | the verdict is a function of `measured` vs `expected`; no prose is parsed. Mutating prose or tool names cannot change a verdict unless the underlying measured state changes |

## 10. Open items and `to-verify`

- **The full tool does not exist yet.** This is part 3 of a three-part draft; parts 1 and 2 are separate seats. The seam in §8 is a proposal until their fragments land. Integration must reconcile names, then re-run the controls.
- **Exit 3 is a completion, not a literal.** The r47 claim names `0/1/2` only; R01 requires `could-not-evaluate` to be non-zero without assigning it a code. If the integrator insists on exactly 0/1/2, the unevaluated state must still be non-zero; reusing 1 would conflate stale with unevaluated, so 3 is the recommended choice. Record the decision in W01/`validation.json`.
- **The r43 values in §7.1 are cited from R01, not re-measured here.** The real positive regression remains O05/O08; this seat's evidence is the decision algebra.
- **Probe exceptions are outside this layer.** Part 1/2 must catch them per clause and return `NOT_EVALUATED`; an escaping exception must not become exit 0.
- **`--at` policy belongs to part 1.** If retained, it must set `deviation` and cap the exit at 3. The prototype's `--at worktree` must not survive.
- **Prototype port hazard.** The scratch prototype's `--allow-unverifiable` and its 1/2/3 map are anti-contract (`.scratch/ca01/claims-freshness.py:69-76,888-890`). Keep the method, replace the surface.
- **`checks_evaluated` means "results supplied".** It is not `holds + contradicted`; a padded not-run clause is counted in `not_evaluated`, not in `checks_evaluated`.

## 11. Evidence register

| evidence | location |
|---|---|
| O claim text, thresholds, 7 probe kinds | `reports/round-47/claims.json:37-47` |
| O03 mission (exit 0 fresh / 1 stale / 2 malformed) | `reports/round-47/targets.json:35` |
| O02 mission (same 7 probe kinds) | `reports/round-47/targets.json:34` |
| six-part durable contract | `reports/round-44/review/R01-review.md:243-250` |
| r43 measured premises (O 2/2 false, C 2/3 hold, Ca fresh) | `reports/round-44/review/R01-review.md:222-235` |
| r43 baseline and `before` lines | `reports/round-43/claims.json:7,27,40,53` |
| prototype exit map and downgrade flag | `.scratch/ca01/claims-freshness.py:69-76,888-890` |
| repo gate convention `EXIT_UNEVALUATED = 2` | `tools/gates/argot-derivation-gate.py:105-107` |
| refusal code 3 precedent | `tools/harness/receipt_guard.py:34` |
| tested body | `.scratch/o03/verdict_part3.py`, 487 lines, sha256 `097a31987cc334d93eaa117e60d7112cddeb7fbf9a356d10ca4dc178721cfcef` |
| control run | `python3 -B .scratch/o03/drive_o03.py` → 33/33 PASS, exit 0 |

## 12. Seat self-audit

- Wrote only `reports/round-47/op/O03-verdict-contract.md` under the round tree. Scratch work stayed under `.scratch/o03/`.
- Edited no filed byte; staged nothing under `corpus/`; changed no tool under `tools/`.
- Ran no `reports/round-*/run-validation.py`, no git commit/push, no install, no network command.
- The fenced body is the exact tested bytes, not a retyped approximation: the assembly spliced `.scratch/o03/verdict_part3.py` into §6 and the pinned digest covers the result.
- Claims that could not be verified here are marked above: the real r43 re-measurement (O05/O08), the assembled tool's existence, and the integrator's acceptance of exit 3.
