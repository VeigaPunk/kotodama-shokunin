# Fixture: gate row with a bare-dash self-test cell and no reason (expected FAIL SELFTEST-BARE)

| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|---|
| fixture-selftest | gate | `python3 -B tools/present.py <packet.yml>` | 0 pass / 1 fail / 2 usage-env. | — | tools/present.py sha256 pinned at freeze | read-only | kotodama-shokunin |
