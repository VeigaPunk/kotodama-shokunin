# Fixture: verdict text with an escaped pipe inside a code span (expected PASS)

| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|---|
| fixture-escaped | gate | `python3 -B tools/present.py <packet.yml>` | Output ends `ACCEPT-C: PASS\|FAIL`; exit 0/1, or 2 on unusable input. | `python3 -B tools/present.py --selftest` | tools/present.py sha256 pinned at freeze | read-only; selftest scratch | kotodama-shokunin |
