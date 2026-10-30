# Fixture: one red row per remaining field rule (each row is graded separately)

| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|---|
| fixture-cmd-empty | gate | — | 0 pass / 1 fail / 2 usage-env. | `python3 -B tools/present.py --selftest` | pinned | read-only | kotodama-shokunin |
| fixture-verdict | gate | `python3 -B tools/present.py <p>` | pass or fail | `python3 -B tools/present.py --selftest` | pinned | read-only | kotodama-shokunin |
| fixture-write-empty | gate | `python3 -B tools/present.py <p>` | 0 pass / 1 fail / 2 usage-env. | `python3 -B tools/present.py --selftest` | pinned | — | kotodama-shokunin |
| fixture-write-noscope | gate | `python3 -B tools/present.py <p>` | 0 pass / 1 fail / 2 usage-env. | `python3 -B tools/present.py --selftest` | pinned | as needed | kotodama-shokunin |
| fixture-kind | tool | `python3 -B tools/present.py <p>` | 0 pass / 1 fail / 2 usage-env. | `python3 -B tools/present.py --selftest` | pinned | read-only | kotodama-shokunin |
| fixture-dup | gate | `python3 -B tools/present.py <p>` | 0 pass / 1 fail / 2 usage-env. | `python3 -B tools/present.py --selftest` | pinned | read-only | kotodama-shokunin |
| fixture-dup | gate | `python3 -B tools/present.py <p>` | 0 pass / 1 fail / 2 usage-env. | `python3 -B tools/present.py --selftest` | pinned | read-only | kotodama-shokunin |
|  | gate | `python3 -B tools/present.py <p>` | 0 pass / 1 fail / 2 usage-env. | `python3 -B tools/present.py --selftest` | pinned | read-only | kotodama-shokunin |
