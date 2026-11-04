# Claim O staging notes — `tools/apply-sound-laws.py`

Round 84 (hyaku run 15), wave w1, seat ExecSoundLaws. These notes accompany the nine
files staged in this directory; the L1 lands them and nothing here is committed by the
seat.

## 0. Files staged

| File | Bytes | sha256 |
|---|---|---|
| `apply-sound-laws.py` | 26296 | `46c3dd6bbdf04a0d0b09947f556c2ef977729e3ba86b5702b1391d4219276602` |
| `rules.json` | 627 | `9a48a2c7f15bc095c29a3d2cac8c27a419eeb6996f148fd9e77b3d560319888e` |
| `proto-lexicon.tsv` | 489 | `192ef7e7044ba1c6c10eeb27aaf8c28e3e633e209980af4fffc71f43fdabd5b2` |
| `expected.tsv` | 196 | `241f0edf43a83a981510f829f5a18d5b51c360f3e43094c0c09aa6dc7bc393ab` |
| `expected-trace.tsv` | 487 | `bf87cf871307ce8d6eaf0879ea069a4f8266906b67dae9ed3aee3afbfd124f63` |
| `selftest.txt` | 80 | `263237d50852eb02b84453692923ee812b43aa6ecdf5be55cb429af7a4b43de3` |
| `demo.txt` | 1008 | `95bcb7aca913f3c40cb2eb1b62373897c327f0e7edc5ce9d3cb1bada06c159da` |
| `negatives.txt` | 1296 | `1619e72dad40ed0240b4e403152ade414f9ca5ef4dc88c4fa82cf2d83c245694` |
| `notes.md` | — | this file |

Landing map: `apply-sound-laws.py` goes to `tools/apply-sound-laws.py`; the other four
artifacts go to `examples/sound-laws/`.

## 1. Frozen contract and where each clause lives

| Contract clause | Implementation |
|---|---|
| `python3 tools/apply-sound-laws.py selftest` | `main()` dispatches `["selftest"]`; also accepts `--selftest`, the spelling the frozen `reports/round-84/accept-o84.py` invokes |
| `apply --rules PATH --input PATH --out PATH [--trace PATH]` | `parse_apply_argv()` + `run_apply()`; `--trace` is optional |
| input TSV `gloss<TAB>seg1 seg2 ...`, `#` comments, blank lines ignored | `parse_input()`; a record whose segment field is empty is refused as `input-empty-word` |
| rules JSON with `name`, `from`, `to`, `pre`, `post`; rules in file order | `parse_rules()` builds an ordered list; no sorting anywhere |
| one left-to-right non-overlapping pass per rule | `derive_word()` iterates the word once per rule and never rescans the replacement; `non-overlap-no-cascade` checks `a > a a` fires once |
| `to` may be `""` (deletion) | `target = ""` gives an empty segment list; the change record keeps an empty `after` field |
| output TSV `gloss<TAB>derived segments`, input order preserved | `render_lexicon()`; the entry list is never reordered |
| change record `gloss<TAB>index<TAB>rule<TAB>before<TAB>after` | `render_changes()`; one line per replacement; line count equals the summary's change count |
| `SOUNDLAW_ERROR: <label>: <detail>` on stderr, exit 2, never a traceback | `InputError` + the `ERROR_PREFIX` handler in `main()`; `OSError` is folded into an `io` label |
| refuse missing rules file | label `rules-missing` |
| refuse rules file that is not JSON | label `rules-json` |
| refuse a missing or empty `from` / `name` | labels `rule-from-missing`, `rule-from-empty`, `rule-name-missing`, `rule-name-empty` |
| refuse `pre`/`post` that are not lists | label `rule-context` (also bad elements and misplaced `#`) |
| refuse duplicate rule names | label `rule-duplicate` |
| refuse an input line without a TAB | label `input-syntax` |
| refuse an output path inside the rules/input directory | label `output-path`; the check runs before any write |
| `selftest` prints `SELFTEST: PASS (<n> checks)`, exit 0 | 36 in-process checks over the real parser/deriver/renderers; failures print `SELFTEST FAIL <case>` on stderr and exit 1 |
| stdlib only, no network, writes only `--out` and the optional log path | imports are `json`, `os`, `re`, `sys`; the only `open(..., "w")` calls are in `write_text()` |

Two semantics worth pinning because the JSON notation is terse:

- `#` in `pre`/`post` is a boundary marker on the *context*: a leading `#` in `pre`
  asserts that the context immediately before the target begins at the word start; a
  trailing `#` in `post` asserts that the context after the target ends at the word
  end. A lone `["#"]` therefore means "target at index 0", and a lone `post: ["#"]`
  means "target at the last index"; `["#", "a"]` means "word starts with `a` and the
  target follows it".
- `index` in the change record is the 0-based position in the current pass output
  where the replacement is written (i.e. after any earlier change of the same pass).
  For a first-pass, one-for-one change this equals the input position; after a
  deletion earlier in the same pass it is the shifted position. The trace is
  self-consistent and the hand derivations below agree with it.

## 2. Grounding in the knowledge base

`corpus/knowledge/linguistics/historical-linguistics.md` at base
`81499ee45b5751d388fefc78583810878de01ecd`, §7 "Constructing proto-languages and
daughter languages", steps 2–3, quoted verbatim:

> 2. Per branch, write an **ordered law list** (L1, L2, …). Track
>    **feeding/bleeding**: L2 may destroy (bleed) or create (feed) the
>    environment for L3. Ordering is where chronology lives.
> 3. Derive daughter forms mechanically. Then apply analogical cleanup where a
>    paradigm would be intolerably opaque.

§3's lesson is the second anchor:

> One branch-wide law gives every daughter word a "family resemblance" no
> ad-hoc conlang achieves.

§3 also names the natural change types the example uses ("assimilation, lenition,
palatalization — common cross-linguistically"), and §9's "Divine names obey the laws"
supplies the `god` entry, whose `w > v` is the same law list as the common nouns.
The tool is exactly §7 step 3 made mechanical; the example's rule order is the §7
step 2 chronology.

## 3. The example: a two-era derivation

Era I is `proto-lexicon.tsv`: 16 proto-words over the inventory

- vowels `a e i o u`
- consonants `p t k b d g m n s r l w`

Era II is `expected.tsv`: the same 16 glosses after the seven ordered laws in
`rules.json`. Row order is preserved, so the two files read as a proto/daughter pair.

| # | Rule | Change | Context | Type (§3/§7) |
|---|---|---|---|---|
| 1 | `intervocalic-voicing` | `p > b` | `a _ a` | intervocalic lenition/voicing |
| 2 | `initial-w-to-v` | `w > v` | `# _` | word-initial change |
| 3 | `kt-cluster-simplification` | `k > ∅` | `_ t` | cluster simplification (deletion) |
| 4 | `i-umlaut` | `a > e` | `_ i` | umlaut (V raises before a high front vowel) |
| 5 | `nasal-place-assimilation` | `n > m` | `_ p` | place assimilation |
| 6 | `intervocalic-s-rhotacism` | `s > r` | `a _ a` | lenition (rhotacism) |
| 7 | `final-a-loss` | `a > ∅` | `_ #` | final vowel loss (deletion) |

Derivation totals, printed by the tool and reproduced in `demo.txt`:

```
SOUNDLAWS: 16 words / 7 rules / 19 changes
```

Fire counts from `expected-trace.tsv` (7/7 rule names fire):

```
12 final-a-loss
 2 i-umlaut
 1 initial-w-to-v
 1 intervocalic-s-rhotacism
 1 intervocalic-voicing
 1 kt-cluster-simplification
 1 nasal-place-assimilation
```

## 4. Hand derivations (five words checked against the rules)

Rule numbers are the table above; each arrow names the rule and the trace index.

- **water** `a k w a`
  - R2 `initial-w-to-v`: `w` is at index 2, not word-initial → no match.
  - R7 `final-a-loss`: final `a` at index 3 → `a k w`. Trace `water 3 final-a-loss a ""`.
- **night** `n o k t i`
  - R3 `kt-cluster-simplification`: `k` at index 2 is followed by `t` → deleted →
    `n o t i`. Trace `night 2 kt-cluster-simplification k ""`.
- **hemp** `k a n p a`
  - R5 `nasal-place-assimilation`: `n` at index 2 is followed by `p` → `m` →
    `k a m p a`. Trace `hemp 2 nasal-place-assimilation n m`.
  - R7 `final-a-loss`: final `a` at index 4 → `k a m p`. Trace `hemp 4 final-a-loss a ""`.
- **father** `a p a`
  - R1 `intervocalic-voicing`: `p` at index 1 stands between `a` and `a` → `b` →
    `a b a`. Trace `father 1 intervocalic-voicing p b`.
  - R7 `final-a-loss`: final `a` at index 2 → `a b`. Trace `father 2 final-a-loss a ""`.
- **ash** `a s a`
  - R6 `intervocalic-s-rhotacism`: `s` at index 1 between `a` and `a` → `r` → `a r a`.
    Trace `ash 1 intervocalic-s-rhotacism s r`.
  - R7 `final-a-loss`: final `a` at index 2 → `a r`. Trace `ash 2 final-a-loss a ""`.

**The ordering is load-bearing (bleeding).** If `final-a-loss` ran before rhotacism,
`ash` would become `a s` and R6's `a _ a` environment would be destroyed: rhotacism
would fire zero times and the rule set would fail its own "every rule fires" check.
The committed order applies rhotacism first and final loss last — the §7 step 2
statement that "ordering is where chronology lives", made checkable. The selftest's
`rule-ordering` case proves the same property synthetically (two rules whose order
changes the output, and whose trace order follows file order).

## 5. Evidence retained

### `selftest.txt`

```
$ python3 -B tools/apply-sound-laws.py selftest
SELFTEST: PASS (36 checks)
rc=0
```

The 36 cases (in source order): `single-segment-change`, `deletion`,
`insertion-new-segment`, `word-start-anchor`, `word-start-context-anchor`,
`word-end-anchor`, `word-end-context-anchor`, `pre-and-post-context`,
`no-match-preservation`, `multi-segment-word`, `non-overlap-no-cascade`,
`rule-ordering`, `many-changes-one-pass`, `initial-deletion-index`,
`empty-word-refusal`, `input-no-tab-refusal`, `input-comments-and-blanks`,
`input-empty-refusal`, `rules-not-json-refusal`, `rules-root-shape-refusal`,
`rule-name-missing-refusal`, `rule-name-empty-refusal`, `rule-from-missing-refusal`,
`rule-from-empty-refusal`, `rule-from-shape-refusal`,
`rule-context-not-list-refusal`, `rule-context-bad-element-refusal`,
`rule-duplicate-refusal`, `rules-missing-file-refusal`, `output-path-refusal`,
`change-record-shape`, `derive-to-record`, `summary-shape`, `empty-rules-noop`,
`render-lexicon`, `single-segment-word`. These cover every refusal the seat names,
the five boundary/context shapes, non-overlap, ordering, and the record shape; they
run fully in process and write no file.

### `demo.txt`

Commands, then their real output:

```
$ python3 -B tools/apply-sound-laws.py apply --rules examples/sound-laws/rules.json --input examples/sound-laws/proto-lexicon.tsv --out out/derived.tsv --trace out/derived-trace.tsv
SOUNDLAWS: 16 words / 7 rules / 19 changes
rc=0

$ cmp out/derived.tsv examples/sound-laws/expected.tsv
byte-identical

$ cmp out/derived-trace.tsv examples/sound-laws/expected-trace.tsv
byte-identical
```

The fire-count block follows, and the receipt ends `7/7 rule names fired; 19 log lines
== 19 changes`. The demo was run from a repo-shaped copy whose `tools/` and
`examples/sound-laws/` entries are the staged bytes, so the commands above are exactly
the post-landing commands.

### `negatives.txt`

Three malformed inputs, each `rc=2`, a `SOUNDLAW_ERROR:` label, no stack dump, and no
output file created:

```
missing rules file  -> SOUNDLAW_ERROR: rules-missing: out/absent.json: No such file or directory
rules file not JSON -> SOUNDLAW_ERROR: rules-json: out/bad.json is not JSON: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
rule with empty from-> SOUNDLAW_ERROR: rule-from-empty: out/empty-from.json: rule 'x' has an empty from
```

The receipt ends with `ls` proving `out/n1.tsv`, `out/n2.tsv`, `out/n3.tsv` do not
exist: refusal happens before any write.

### Mutant falsification (measured, not committed)

The frozen acceptor's junk battery was replayed against the staged bytes. Its
`m_no_trace` mutation replaces the first line containing `trace` with
`pass  # trace disabled`; in the staged tool that first line is the log-write guard
`if opts.get("trace"): write_text(opts["trace"], changes_text)`. Measured after the
mutation: exit 0, the derived lexicon still byte-identical to `expected.tsv`, the
summary still `SOUNDLAWS: 16 words / 7 rules / 19 changes`, and **no log file** — so
the acceptor's DEMO leg fails on "no trace file" and the mutation is killed by
behaviour, not by a syntax error. Its `m_copy` mutation (a stub that copies the input
to `--out` and prints `SOUNDLAWS: 12 words / 6 rules / 99 changes`) is killed twice
over: the derived file is the input, not `expected.tsv`, and no log is written.

The frozen counter's other four Python legs were replayed in process with the
constants read from `3ca2cf288fb593618e0559ea86a36e2dd3110eb8:reports/round-84/claims.json`:
`TOOL` (26296 bytes, three markers present), `SELFTEST` (exit 0, 36 checks, floor 20),
`DEMO` (one summary line, 19 trace lines, 7/7 rules fired, derived and log both
byte-identical), `NEGATIVE` (three refusals, rc 2, label present, no traceback). All
four pass. `FROZENCFG`, `BEFORE`, `REGISTRY` and `SEPARABLE` are git legs and belong
to the L1's lands run.

## 6. Reproduce after landing

From the lane root, with `tools/apply-sound-laws.py` and `examples/sound-laws/` in
place:

```
python3 -B tools/apply-sound-laws.py selftest
python3 -B tools/apply-sound-laws.py apply --rules examples/sound-laws/rules.json --input examples/sound-laws/proto-lexicon.tsv --out <tmpdir>/derived.tsv --trace <tmpdir>/trace.tsv
cmp <tmpdir>/derived.tsv examples/sound-laws/expected.tsv
cmp <tmpdir>/trace.tsv examples/sound-laws/expected-trace.tsv
```

`<tmpdir>` must not be `examples/sound-laws/` itself: the tool refuses an `--out`
inside the rules/input directory (`output-path`). That refusal is deliberate — it is
one of the frozen negatives — and is why the demo regenerates into `out/` rather than
overwriting `expected.tsv` in place.

## 7. L1 landing instructions

1. Copy `apply-sound-laws.py` to `tools/apply-sound-laws.py`.
2. Copy `proto-lexicon.tsv`, `rules.json`, `expected.tsv`, `expected-trace.tsv` to
   `examples/sound-laws/`.
3. Append three rows under `## Gates and probes` in `SKILL.md` **in the same commit**
   as steps 1–2. The registry leg of `reports/round-84/accept-o84.py` grades
   `GATE-REGISTRY: 0 missing` over the whole instrument set at the O lands revision,
   and the two round-84 counters are missing rows at the freeze commit. Suggested
   rows, 8 cells each, `tools/apply-sound-laws.py` present in the entry-command cell:

```
| apply-sound-laws | gate | `python3 -B tools/apply-sound-laws.py selftest` then `python3 -B tools/apply-sound-laws.py apply --rules examples/sound-laws/rules.json --input examples/sound-laws/proto-lexicon.tsv --out <dir>/derived.tsv --trace <dir>/trace.tsv` | `SELFTEST: PASS (<n> checks)` on stdout, exit 0; the apply run prints one `SOUNDLAWS: 16 words / 7 rules / 19 changes` line and reproduces `examples/sound-laws/expected.tsv` and `expected-trace.tsv` byte-for-byte; 7/7 rule names fire | `python3 -B tools/apply-sound-laws.py selftest` (36 in-process checks: parsing, context anchors, non-overlap, ordering, every refusal, record shape) | floors 12 words / 6 rules / 12 changes; example carries 16 / 7 / 19; log line count == change count | read-only over the two example inputs; writes only `--out` and `--trace`; refuses an output path inside the rules/input directory | kotodama-shokunin |
| accept-d-84 | gate | `python3 -B reports/round-84/accept-d84.py --root . --lands <40-hex> --freeze <40-hex> --work <dir>` | Output ends `ACCEPT-D-84: PASS legs=10/10` or `: FAIL legs=<n>/10`; 0 pass / 1 fail. A refusal prints `ACCEPT-D-84: FAIL legs=0/10 (refused: …)` and exits 2: non-40-hex revision, `--work` not an existing directory, unreadable or incomplete frozen config, LEGCOUNT, lands equal to the frozen base, freeze not an ancestor of lands, or lands not an ancestor of `main`. | — (no `--selftest`) | entry `corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md`; 16000-byte floor; 7 sections; 6 decision rows; 20 anchors over >= 4 S-ids; SOURCES 837 -> >= 841; S914–S917 mined | read-only against committed objects; materialized lands and base trees plus fixtures under `--work` | kotodama-shokunin |
| accept-o-84 | gate | `python3 -B reports/round-84/accept-o84.py --root . --lands <40-hex> --freeze <40-hex> --work <dir>` | Output ends `ACCEPT-O-84: PASS legs=8/8` or `: FAIL legs=<n>/8`; 0 pass / 1 fail. A refusal prints `ACCEPT-O-84: FAIL legs=0/8 (refused: …)` and exits 2 on the same refusal set including lands equal to the frozen base. | — (no `--selftest`) | tool byte floor 5000; selftest floor 20 checks; 12 words / 6 rules / 12 changes / 6 rules fired; registry 0 missing / >= 77 registered / >= 63 instruments / 0 dead; unrowed tools <= 25 | read-only; demo and negatives in `--work`; junk battery `--junk` | kotodama-shokunin |
```

   Those row texts are advisory; the two constants that must hold are: cell 3 (index
   2) contains `tools/apply-sound-laws.py`, and the `check-gate-registry.py` auditor
   finds no dead `tools/*.py` token. At the O lands the expected audit line is
   `GATE-REGISTRY: 0 missing / 77 registered / 63 instruments / 0 dead` with
   `GATE-REGISTRY-INFO: 24 tools without a row`.

4. Landing order. Land O and D as **separate commits**, and grade each claim at its own
   `--lands` revision. The SEPARABLE legs of both counters compare foreign paths
   between the claim's span parent and its lands, so one commit carrying both claims
   fails both. With separate commits either order works: D-first leaves
   `tools/apply-sound-laws.py` absent at D's lands, and O-first leaves the D entry and
   `corpus/SOURCES.md` unchanged at O's lands. The three SKILL.md rows must ride the O
   commit because the O REGISTRY leg is graded at the O lands revision.

5. Do not move `corpus/SOURCES.md`, the D entry, `SKILL.md` or the two counters in the
   O commit beyond the three new rows, and do not let `tools/apply-sound-laws.py` or
   `examples/sound-laws/` move in the D commit.

## 8. Risks and review notes

- The seat contract spells the first subcommand `selftest`; the frozen acceptor calls
  `--selftest`. Both spellings are accepted, so the two documents do not fight.
- `expected.tsv` is committed beside `rules.json`; the tool's own output-path refusal
  means it cannot be regenerated in place. That is the frozen negative, not an
  accident.
- Determinism: no timestamps, locale, environment or hash-order dependence; the rule
  list order is the only ordering, and `newline="\n"` fixes the line endings. The
  lexicon and trace bytes are functions of the two input files alone.
- The tool refuses an empty lexicon (`input-empty`) and an empty `from`/`name`; it
  accepts an empty `rules` list as a no-op derivation (0 rules, output == input).
- `#` is only a boundary marker in context lists; a `#` in `from` or `to` is refused.
- The first occurrence of the string `trace` in the source is deliberately the
  log-write guard, so the acceptor's `m_no_trace` mutation produces a runnable tool
  that silently omits the log and is killed by the DEMO leg.
- No tool installs or upgrades were needed for this seat; the reference interpreter is
  the host `python3` (3.14.8) and the tool imports only the standard library.

## 9. Left behind

Nothing in the lane outside `tools/apply-sound-laws.py` and `examples/sound-laws/`
(the L1's copies) and this staging directory. Scratch was removed after the receipts
above were copied here; no committed report cites a scratch path.
