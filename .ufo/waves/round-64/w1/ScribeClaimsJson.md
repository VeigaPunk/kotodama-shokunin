# ScribeClaimsJson — round 64 declaration

## Behavior and deliverables

Created a round-64 declaration with C (coverage / learning), O (operability / capability), and Ca (calibration / calibration), including each falsifiable before→after statement, frozen predicate, acceptance command, declared lands, exported id block, review-only clauses, and base revision `ff30a205c8d23b35f1ac533740121a955a9fda96`.

Created a Sources & frontier extract recording 643 rows before, 675 as the planned after-count (+26 mined and +6 rejected), the six rejection candidates, and the count/validation commands. The 675 value is a target from the acceptance contract, not a count measured by this seat.

The claims declaration is `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeClaimsJson/claims.json`. Its top-level keys are `round`, `attempt`, `campaign`, `declared_at`, `round_base`, `separability_manifest`, `separability_command`, and `claims`. The checker-compatible input is `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeClaimsJson/separability-manifest.json` (top-level keys: `schema`, `base`, `claims`); the lane checker requires this strict manifest shape, rather than the round-63 declaration shape.

## Gates and exact outcome

Ran once:

```text
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-claim-separability.py /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeClaimsJson/separability-manifest.json --lane /home/vgpnk/Projects/shokunin/kotodama-shokunin --root /home/vgpnk/Projects/shokunin/kotodama-shokunin
```

Verbatim output:

```text
SEPARABILITY_INPUT_ERROR unit C lands 'corpus/knowledge/linguistics/language-socialization-and-acquisition.md', which is absent from the worktree under '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
```

Exit code: `2`. The checker could not evaluate the manifest because the declared C entry was absent from the lane worktree at execution time; no separability verdict was produced. No acceptance predicate or source census was run by this seat.

## Lands, overlap, and touched surfaces

The declared land sets are pairwise disjoint by literal path comparison; no C/O/Ca land overlap is declared. The checker did not reach overlap evaluation, so this is a comparison of the declarations, not a checker finding.

Files written:

- `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeClaimsJson/claims.json`
- `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeClaimsJson/sources-frontier.md`
- `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeClaimsJson/separability-manifest.json`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-64/w1/ScribeClaimsJson.md`

No product code, registry, knowledge entry, counter, or claim land was edited. The declaration and frontier summary are scratch artifacts; the only lane write is this explicitly requested wave report.

## Provenance and limits

The declaration format was compared with `reports/round-63/claims.json`; the round-64 predicates and leg contracts were taken from `reports/round-64/accept-c.py`, `accept-o.py`, and `accept-ca.py`. The declared round-64 lands and commands were read from the existing `reports/round-64/claims.json`. Rejection names were taken from `.ufo/waves/round-64/gen-w1.py`; the registry census/validation command was cross-checked against `scripts/sources-census.sh` and the round-63 verifier spotcheck.

The source count after integration, ordinary re-open evidence for rejected candidates, acceptance outcomes, and a complete separability result remain unobserved here. No tool install or update was needed.