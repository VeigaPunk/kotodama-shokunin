# ExecSoundLaws — round 84 w1, claim O (ordered sound-law applier)

Status: **complete, staged, uncommitted**. The L1 lands every byte. No blockers.

## 1. What was built

`tools/apply-sound-laws.py`: a deterministic, dependency-free applier for ordered sound
laws over a segment-tokenised proto-lexicon, with one change record per replacement, a
real 36-check in-process selftest, and a committed two-era derivation under
`examples/sound-laws/` that the tool reproduces byte-for-byte.

Nine files are staged under `.ufo/waves/round-84/w1/stage/ExecSoundLaws/`:

| Staged file | Lands at | Bytes | sha256 |
|---|---|---|---|
| `apply-sound-laws.py` | `tools/apply-sound-laws.py` | 26296 | `46c3dd6bbdf04a0d0b09947f556c2ef977729e3ba86b5702b1391d4219276602` |
| `rules.json` | `examples/sound-laws/rules.json` | 627 | `9a48a2c7f15bc095c29a3d2cac8c27a419eeb6996f148fd9e77b3d560319888e` |
| `proto-lexicon.tsv` | `examples/sound-laws/proto-lexicon.tsv` | 489 | `192ef7e7044ba1c6c10eeb27aaf8c28e3e633e209980af4fffc71f43fdabd5b2` |
| `expected.tsv` | `examples/sound-laws/expected.tsv` | 196 | `241f0edf43a83a981510f829f5a18d5b51c360f3e43094c0c09aa6dc7bc393ab` |
| `expected-trace.tsv` | `examples/sound-laws/expected-trace.tsv` | 487 | `bf87cf871307ce8d6eaf0879ea069a4f8266906b67dae9ed3aee3afbfd124f63` |
| `selftest.txt` | evidence only | 80 | `263237d50852eb02b84453692923ee812b43aa6ecdf5be55cb429af7a4b43de3` |
| `demo.txt` | evidence only | 1008 | `95bcb7aca913f3c40cb2eb1b62373897c327f0e7edc5ce9d3cb1bada06c159da` |
| `negatives.txt` | evidence only | 1296 | `1619e72dad40ed0240b4e403152ade414f9ca5ef4dc88c4fa82cf2d83c245694` |
| `notes.md` | evidence only | 19151 | — (grounding, hand derivations, landing order) |

## 2. Contract conformance

- CLI: `python3 tools/apply-sound-laws.py selftest` and
  `apply --rules PATH --input PATH --out PATH [--trace PATH]`. The frozen acceptor
  invokes `--selftest`, so that spelling is accepted too; both exit 0 with
  `SELFTEST: PASS (36 checks)`.
- Input TSV: `gloss<TAB>seg1 seg2 ...`; `#` comment lines and blank lines are skipped;
  a line without a TAB and a record with an empty segment field are refused.
- Rules JSON: ordered `{"rules":[{"name","from","to","pre","post"}]}`; `from` is one
  segment, `to` is zero or more space-separated segments (`""` deletes), `#` in
  `pre`/`post` anchors the context at the word edge. One left-to-right non-overlapping
  pass per rule; a replacement is never rescanned by the rule that produced it.
- Output TSV keeps input order and glosses; the change record is
  `gloss<TAB>index<TAB>rule<TAB>before<TAB>after`, one line per replacement.
- Refusals (all exit 2, `SOUNDLAW_ERROR: <label>: <detail>` on stderr, no traceback,
  and no output path written): missing rules file, non-JSON rules, missing/empty
  `from`, missing/empty `name`, `pre`/`post` not lists (and bad elements or misplaced
  `#`), duplicate rule names, input line without a TAB, empty word, empty lexicon,
  output path inside the rules/input directory.
- Stdlib only (`json`, `os`, `re`, `sys`); no network; the only writes are `--out` and
  the optional log path.

## 3. The committed example (claim O's DEMO object)

`proto-lexicon.tsv` is era I: 16 proto-words over vowels `a e i o u` and consonants
`p t k b d g m n s r l w`. `rules.json` is seven ordered laws: `intervocalic-voicing`
(`p > b / a _ a`), `initial-w-to-v` (`w > v / # _`), `kt-cluster-simplification`
(`k > ∅ / _ t`), `i-umlaut` (`a > e / _ i`), `nasal-place-assimilation`
(`n > m / _ p`), `intervocalic-s-rhotacism` (`s > r / a _ a`), `final-a-loss`
(`a > ∅ / _ #`). `expected.tsv` is era II.

Tool output on the example:

```
SOUNDLAWS: 16 words / 7 rules / 19 changes
```

7/7 rule names fire (12 final-a-loss, 2 i-umlaut, and one each of the other five);
19 log lines equal the 19 changes. Hand-checked against the rules: `water a k w a ->
a k w`, `night n o k t i -> n o t i`, `hemp k a n p a -> k a m p`,
`father a p a -> a b`, `ash a s a -> a r`. The rule order is load-bearing: with
`final-a-loss` before rhotacism, `ash` would end `a s` and rhotacism would never fire
— the §7 step 2 "ordering is where chronology lives" made checkable. Grounding quotes
and the full derivations are in `stage/ExecSoundLaws/notes.md` §2 and §4.

## 4. Evidence (all commands repo-relative, windows removed)

`selftest.txt`:

```
$ python3 -B tools/apply-sound-laws.py selftest
SELFTEST: PASS (36 checks)
rc=0
```

`demo.txt` (run from a repo-shaped copy whose `tools/` and `examples/sound-laws/` are
the staged bytes, so the commands are exactly the post-landing ones):

```
$ python3 -B tools/apply-sound-laws.py apply --rules examples/sound-laws/rules.json --input examples/sound-laws/proto-lexicon.tsv --out out/derived.tsv --trace out/derived-trace.tsv
SOUNDLAWS: 16 words / 7 rules / 19 changes
rc=0

$ cmp out/derived.tsv examples/sound-laws/expected.tsv
byte-identical

$ cmp out/derived-trace.tsv examples/sound-laws/expected-trace.tsv
byte-identical
```

`negatives.txt` — three malformed inputs, each rc 2, label present, no stack dump, and
`ls` proving no output path was created:

```
rules-missing: out/absent.json: No such file or directory
rules-json: out/bad.json is not JSON: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
rule-from-empty: out/empty-from.json: rule 'x' has an empty from
```

Additional measured proof not carried as a committed receipt:

- The frozen counter's Python legs were replayed with constants read from
  `3ca2cf288fb593618e0559ea86a36e2dd3110eb8:reports/round-84/claims.json`:
  `TOOL` PASS (26296 bytes, `SOUNDLAW_ERROR:`, `--selftest`, `def main(` present),
  `SELFTEST` PASS (36 checks >= floor 20), `DEMO` PASS (one summary line, derived and
  log byte-identical, 19 trace lines == 19 changes, 7/7 rules fired),
  `NEGATIVE` PASS (three cases rc 2, no traceback).
- Junk mutants from `reports/round-84/accept-o84.py` measured against the staged bytes:
  `m_no_trace` leaves the tool running with the correct lexicon and summary but writes
  no log -> DEMO fails "no trace file"; `m_copy` produces derived != expected and no
  log -> DEMO fails. Both killed for the right reason. The first occurrence of the
  string `trace` in the source is deliberately the log-write guard so that this is a
  behavioural kill rather than a syntax error.
- Absolute `--out`/`--trace` paths (the acceptor's shape) and a run from a foreign
  working directory both reproduce `expected.tsv` byte-identically; the example is
  cwd-independent.

## 5. L1 landing instructions

1. Land `apply-sound-laws.py` at `tools/apply-sound-laws.py`; land
   `rules.json`, `proto-lexicon.tsv`, `expected.tsv` and `expected-trace.tsv` under
   `examples/sound-laws/`.
2. Append **three** `## Gates and probes` rows in the same commit: the
   `apply-sound-laws` row naming `tools/apply-sound-laws.py` in its entry-command cell,
   plus rows for `reports/round-84/accept-d84.py` and `reports/round-84/accept-o84.py`.
   Exact suggested 8-cell row text is in `stage/ExecSoundLaws/notes.md` §7. The O
   REGISTRY leg is graded at the O lands revision and requires
   `GATE-REGISTRY: 0 missing` over the whole instrument set; at base the two round-84
   counters are the missing rows, so they must ride the O commit. Expected audit line
   at O lands: `GATE-REGISTRY: 0 missing / 77 registered / 63 instruments / 0 dead`,
   `GATE-REGISTRY-INFO: 24 tools without a row`.
3. Land O and D as **separate commits** and grade each at its own `--lands`. A single
   commit carrying both claims fails both SEPARABLE legs (each claim's foreign paths
   move). With separate commits either order works, because the other claim's paths are
   untouched between the claim's span parent and its lands.
4. Do not let `tools/apply-sound-laws.py` or `examples/sound-laws/` move in the D
   commit, and do not move `corpus/SOURCES.md`, the D entry, or `SKILL.md` outside the
   O commit's three new rows.

## 6. Risks / review notes

- `expected.tsv` is committed beside `rules.json`, but the tool refuses to write
  `--out` inside the rules/input directory (a frozen negative), so regeneration must
  target another directory — `demo.txt` does exactly that.
- `index` in the change record is the position in the current pass output; a deletion
  earlier in the same pass shifts later indices in that pass. This is documented in
  the tool docstring, `notes.md` §1, and the hand derivations.
- `#` in `pre`/`post` anchors the *context* at the word edge; a lone `["#"]` is the
  familiar "target at the boundary" reading, and `["#","a"]` means the word starts
  with `a` and the target follows it.
- An empty `rules` list is an accepted no-op (0 rules, output == input); an empty
  lexicon is refused.
- No tool installs or upgrades were needed; interpreter is the host `python3` 3.14.8
  and only the standard library is imported.

## 7. Cleanup

Scratch was removed after the three receipts were copied into the stage; nothing is
left behind outside the staging directory and the L1's landing targets. No absolute
scratch path appears in any staged text: the staged `*.md` and `*.txt` files were
scanned with the scratch-path pattern of `tools/check-cited-records.py` and returned
no hits.
