# bundles.md — ExecBeforeBundles synthetic counterfeit fixtures (2026-11-05)

Three entry-mode fixture bundles under `bundles/`. **All bundles are synthetic
counterfeits built to exercise the two graders; nothing in them is evidence about any
real source.** Registry rows S952–S954 here are invented fixture ids and their URLs are
`fixture.example.org` placeholders (except the deliberate shadow, below); they are
unrelated to the real round-91 evidence S952–S955 captured in `reports/round-91/evidence/`.

## Common shape (all three bundles)

Each bundle mirrors the layout the frozen counter materializes for claim C:

```
bundles/<name>/
  corpus/SOURCES.md            # base d39434b3 registry bytes (875 rows, S900..S951)
                               # + three appended synthetic rows: S952, S953, S954,
                               #   tier A, status mined, opened 2026-11-05, used-by
                               #   corpus/knowledge/bakery-rota.md
  corpus/lessons/round-91.md   # one `- S9xx LOCATED — "<quote>" — <url> accessed
                               #   2026-11-05, section 2; ...` gate line per row
  corpus/knowledge/bakery-rota.md   # the same 12,889-byte synthetic off-topic entry
                                    # in all three bundles (17 h2, header keys, 6x4
                                    # table, 16 shared content words with the declared
                                    # round-91 topic, filename stems present)
  reports/round-91/evidence/S952.txt S953.txt S954.txt   # captures carrying each gate quote
  reports/round-91/evidence/manifest.json                # sha256 + http_status 200 +
                                     # fetched_at 2026-11-05T12:00:00-03:00 per capture
```

The entry is genuinely about sourdough bakery scheduling; the words it shares with the
declared topic (`secret, registers, argot, cant, closed, social, structure,
conversation, reversal, word, play, design, games, style, procedure, ...`) are used in
bakery senses. That is the point: v1's TOPIC leg counts content-word overlap only, and a
non-linguistics entry clears its threshold.

## The three bundles

- **bundle-bakery** — the off-topic counterfeit. Registry, lesson and captures are all
  clean by v1's rules. Purpose: show that v1's entry mode grades an off-topic bakery
  entry as PASS on all six of its legs, while v2 refuses it on TOPIC (the
  phrase-anchor rule requires >=4 of the 6 declared sub-topic phrases in h2 headings or
  table cells; this entry carries exactly 2: `argot`, `cant`).
- **bundle-shadow** — the same bundle, but row S954's URL is the URL of an existing base
  row (S900's Wikisource URL). Purpose: show that v1 has no URL-uniqueness leg and passes
  the shadow/duplicate-source class, while v2's UNIQUENESS leg names
  `S954: url shadows base row S900`.
- **bundle-selfquote** — the same bundle, but S953's gate quote equals that row's
  teaching cell text. Purpose: show that v1's GATE leg never compares the quote to the
  teaching cell and passes the self-quote class, while v2's GATE leg names
  `S953: gate quote is the row teaching cell (self-quote)`.

## How they are run

`build_and_run.py` (this stage dir) builds all three bundles and invokes both graders
with the argument list the frozen counter `reports/round-91/measure91.py::grade_c`
uses; for v1 the three arguments its CLI does not accept (`--topic-phrases`,
`--min-topic-phrases`, `--base-lesson`) are dropped. Full commands, stdout, stderr and
rc values are in `before-bundles.txt`.

## Observed result (measured 2026-11-05)

| grader x bundle | rc | verdict |
|---|---|---|
| v1 x bundle-bakery | 0 | ENTRY-EVIDENCE: PASS legs=6/6 |
| v2 x bundle-bakery | 1 | ENTRY-EVIDENCE: FAIL legs=7/8 failed=TOPIC |
| v1 x bundle-shadow | 0 | ENTRY-EVIDENCE: PASS legs=6/6 |
| v2 x bundle-shadow | 1 | ENTRY-EVIDENCE: FAIL legs=6/8 failed=TOPIC,UNIQUENESS |
| v1 x bundle-selfquote | 0 | ENTRY-EVIDENCE: PASS legs=6/6 |
| v2 x bundle-selfquote | 1 | ENTRY-EVIDENCE: FAIL legs=6/8 failed=TOPIC,GATE |

v2 fails TOPIC on all three bundles because the same off-topic entry text is reused in
each (per the assignment: shadow and selfquote are "the same" as bakery apart from the
named mutation); the discriminating refusal for shadow is UNIQUENESS and for selfquote
is GATE. Before-state of claim O: the v1 grader's entry mode passes all three
counterfeit classes the round-91 claim says v2 refuses by name.
