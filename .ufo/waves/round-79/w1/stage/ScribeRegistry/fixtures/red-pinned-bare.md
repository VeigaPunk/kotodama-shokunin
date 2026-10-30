# Fixture: gate row with a bare-dash pinned-values cell (expected FAIL PINNED-BARE)

| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|---|
| fixture-pinned | gate | `python3 -B tools/present.py <packet.yml>` | 0 pass / 1 fail / 2 usage-env. | `python3 -B tools/present.py --selftest` | — | read-only | kotodama-shokunin |
