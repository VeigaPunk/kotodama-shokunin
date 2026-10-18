# R25-D05 — argot-derivation leg, impl 4 of 6: the fixture, and positive+negative selftests

- **Seat:** R25-D05, round 25, claim **D**. Date 2026-10-18.
- **Write scope:** `tools/gates/fixtures/argot-derivation-gate.yml`,
  `tools/gates/fixtures/argot-derivation-gate.expected`, and the selftest inside
  `tools/gates/argot-derivation-gate.py`.
- **Canon:** NON-CANON engineering evidence. The fixture is fixture-only and
  states no language.

## 1. The committed fixture

`tools/gates/fixtures/argot-derivation-gate.yml` (sha256
`c4c35294d581b204482427b3776776c57d1e7f83065a0b5f8f3906c38d8c2ccd`), with the
pinned id set in `…-gate.expected` (sha256
`38a283ff3b7cef4336418237f345f3602c4faeee197baca4d1ebc1bb0f78a018`):

| row | kind | planted verdict |
|---|---|---|
| `Q-01` `saalu` head2←`saalumi`; `Q-02` `nim` reverse←`min`; `Q-03` `numas` reverse←`samun`; `Q-04` `sunel` CX-01←`su+nel` | positive derivations | none |
| `B-01` `res`←`resh` (LY-01), `B-02` `gal`←`gol` (LY-02) | positive borrows | none |
| `Q-11` `saalum` head2←`saalumi` | **the design's own trap** — maximal-coda would give `saalum` | `D4L-ARGOT-DERIV` |
| `Q-12` `kin` reverse←`kin` | wrong candidate | `D4L-ARGOT-DERIV` |
| `Q-13` `suk` reverse←`sun` | wrong base | `D4L-ARGOT-DERIV` |
| `B-03` `gal`←`gol` under LY-01 | wrong layer's substitutions | `D4L-ARGOT-DERIV` |
| `Q-20` `nuka` derivation `someop` | declared but not replayable | `D4L-ARGOT-RULE` |
| `P-01` `makun` reverse←`makun`, `register: plain` | **scope control** — unmarked register, must not grade | none |
| `SYM-01` `form:` prose, `register: quote` | **scope control** — not a language form | none |

`Q-11` is deliberately the design's own named disagreement row: `head2` is
maximal-onset by `design-language.md` §5, and `saalum` is what the maximal-coda
reading yields. A leg that "replays" the wrong reading fails its own design.

## 2. Selftest — positive and negative

```
$ python3 tools/gates/argot-derivation-gate.py --selftest
design-table-rederived-11              ok
head2-maximal-onset                    ok
head2-maximal-coda-differs             ok
head2-single-syllable                  ok
reverse-involution                     ok
leg-discriminates                      ok
fixture-exits-1                        ok
fixture-ids-match-expected-file        ok
fixture-counts-pinned                  ok
fixture-names-the-violating-form       ok
positive-control-clean                 ok
positive-control-replayed-pairs        ok
positive-control-replayed-borrows      ok
formation-control-clean                ok
formation-control-rules-lost-held      ok
formation-control-bad-stem-fails       ok
coverage-hold-fires                    ok
malformed-root-is-a-string-exit-2      ok
malformed-unclosed-flow-exit-2         ok
malformed-tab-indent-exit-2            ok
c-02-negative-control-rejected         ok
selftest: 21/21 checks passed
exit 0
```

**Positive controls:** the design's own 11 worked derivations re-derive
(`design-table-rederived-11`); a clean packet with all four derivation forms, one
licensed rule, and one clean borrow is silent (`positive-control-clean`);
D2's and D4's own eight name formations replay with zero violations
(`impl-1` §3).

**Negative controls:** the committed fixture's four planted violations and one
unreplayable declaration are pinned by exact id and count
(`fixture-counts-pinned`, `fixture-ids-match-expected-file`); losing the declared
rule set turns a claimed chain into a named `D4L-ARGOT-RULE`
(`formation-control-rules-lost-held`); a bad stem fails
(`formation-control-bad-stem-fails`); a declared-but-undelivered relation is a
named HOLD (`coverage-hold-fires`); the three malformed inputs exit 2 with
`D4L-ARGOT-DATA` and no traceback; and the forecast's own control C-02
(`apply(op, base) != form` must be rejected) is asserted directly
(`c-02-negative-control-rejected`).

## 3. Two selftest assertions that were themselves wrong, and were fixed

Recorded because a control that asserts the wrong thing is worse than none:

1. `fixture-names-the-violating-form` first named `Q-12` while the `saalum` row
   is `Q-11` — the check was corrected, the gate was not.
2. `formation-control-rules-lost-fails` first expected `D4L-ARGOT-DERIV` for a
   *lost* rule set. A lost rule set is not a violation — nothing can be replayed
   — so the correct class is the HOLD the naming gate also uses (`DERIV-HOLD`).
   Renamed to `formation-control-rules-lost-held` and re-pointed at
   `D4L-ARGOT-RULE`. The gate's behaviour was right; the assertion was wrong.

## 4. Byte pins

| file | sha256 |
|---|---|
| `tools/gates/fixtures/argot-derivation-gate.yml` | `c4c35294d581b204482427b3776776c57d1e7f83065a0b5f8f3906c38d8c2ccd` |
| `tools/gates/fixtures/argot-derivation-gate.expected` | `38a283ff3b7cef4336418237f345f3602c4faeee197baca4d1ebc1bb0f78a018` |

Measured 2026-10-18, lane root, `TMPDIR=$PWD/.scratch`.
