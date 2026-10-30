# Fixture: complete rows (expected PASS)

| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|---|
| fixture-gate | gate | `python3 -B tools/present.py <packet.yml>` | 0 clean / 1 findings / 2 could-not-evaluate | `python3 -B tools/present.py --selftest` | tools/present.py sha256 pinned at freeze | read-only; selftest scratch | kotodama-shokunin |
| fixture-probe | probe | `python3 -B tools/present.py --json` | 0 inventory produced / 1 findings / 2 could-not-evaluate | `python3 -B tools/present.py --selftest` | exact-count constants in script | read-only | kotodama-shokunin |
| fixture-note | note | — | Base rows stand; corrections to how rows are run. | — | — | — | kotodama-shokunin |
