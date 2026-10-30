# Fixture: registry header with the owner column dropped — no table matches the required header (expected exit 2, no verdict)

| name | kind | entry command | verdict map | self-test | pinned values | write scope |
|---|---|---|---|---|---|---|
| fixture-noowner | gate | `python3 -B tools/present.py <p>` | 0 pass / 1 fail / 2 usage-env. | `python3 -B tools/present.py --selftest` | pinned | read-only |
