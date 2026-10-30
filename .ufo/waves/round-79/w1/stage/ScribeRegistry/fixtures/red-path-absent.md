# Fixture: command names a script not in the tree (expected FAIL CMD-PATH-ABSENT)

| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|---|
| fixture-absent | gate | `python3 -B tools/absent.py <packet.yml>` | 0 pass / 1 fail / 2 usage-env. | `python3 -B tools/absent.py --selftest` | tools/absent.py sha256 pinned at freeze | read-only | kotodama-shokunin |
