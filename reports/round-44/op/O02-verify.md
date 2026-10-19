# O02 — Independent verification 1: byte-extract, `--selftest`, `--census`

- Seat: `O02` (verifier, claim **O**)
- Round: 44, claim O — land the r43 O09 successor body as
  `tools/harness/basename-couples-resolver.py`
- Baseline commit: `c9f4eaa` (`git rev-parse --short HEAD` → `c9f4eaa`)
- Observation time: `2026-10-19T17:20:53Z`
- Environment: Linux, CPython 3.14.7, `PYTHONDONTWRITEBYTECODE=1`,
  `TMPDIR=$PWD/.scratch`
- Verdict: **PASS** — body extracts byte-exact (`43ce341f…ad64`), selftest
  **27/27**, census **2556+166+0+7 = 2729 + 1 glob = 2730**, conservation
  `True`, wrapped field **4/4 by identity** (not arity).

I did not edit any tracked byte. All work products are under
`.scratch/o02-run/`; this file is the durable record.

## 0. Method

The r43 O09 fenced draft was extracted to a fresh scratch directory that is
*not* under any synthetic corpus tree, and all measurements were taken there.
Nothing was imported from the in-tree tools; the body was executed from the
scratch copy. The r42 witness
(`tools/harness/couples-reference-extractor.py`) was **not** run and **not**
touched — parity is O07's seat, defect line-refs are O03's seat.

```
workdir  .scratch/o02-run/
body     .scratch/o02-run/basename-couples-resolver.py
outputs  census.out, census.json, live-entry.json, c1.out, c2.out, census2.json
```

## 1. Byte extraction — exact, fence-bounded

Fence boundaries in `reports/round-43/op/O09-scribe.md`:

```
$ grep -n '^````' reports/round-43/op/O09-scribe.md
355:````python
871:````
```

Body = lines **356–870 inclusive** = **515 lines**.

```
$ sed -n '356,870p' reports/round-43/op/O09-scribe.md \
    > .scratch/o02-run/basename-couples-resolver.py
$ wc -l .scratch/o02-run/basename-couples-resolver.py
515 .scratch/o02-run/basename-couples-resolver.py
$ sha256sum .scratch/o02-run/basename-couples-resolver.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64  …/basename-couples-resolver.py
```

Expected digest per claim/round-43 O09 §6 step 5 is
`43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64` —
**exact match**.

Second, independent extraction method (`awk 'NR>=356 && NR<=870'`) yields a
byte-identical file:

```
$ awk 'NR>=356 && NR<=870' reports/round-43/op/O09-scribe.md > alt-extract.py
$ sha256sum alt-extract.py basename-couples-resolver.py
43ce341f…ad64  alt-extract.py
43ce341f…ad64  basename-couples-resolver.py
$ cmp alt-extract.py basename-couples-resolver.py && echo BYTE-IDENTICAL
BYTE-IDENTICAL
```

The extract starts with `#!/usr/bin/env python3` and ends with
`sys.exit(main())\n` — the fence backticks are not included and the trailing
newline is present.

Source file digest for the whole scribe note (unchanged, read-only):
`956d478bfe7abbaac6598a0d272a7cb524e3d2bc7fa70cc27be41b538e0cb341`.

## 2. Clean-directory / no corpus-shadow check

The resolver locates the lane by walking upward from `__file__` until it finds
`corpus/knowledge` (`basename-couples-resolver.py:28-34`). A synthetic
`corpus/knowledge` anywhere above the scratch copy would silently change the
denominator. Ancestor walk from `.scratch/o02-run/`:

```
$ d=$(realpath .scratch/o02-run)
$ while [ "$d" != "/" ]; do [ -d "$d/corpus/knowledge" ] && echo "$d"; d=$(dirname "$d"); done
/home/vgpnk/Projects/shokunin/kotodama-shokunin
```

The only ancestor that carries `corpus/knowledge` is the **real repo root**.
`.scratch/` and `.scratch/o02-run/` carry none. (`.scratch` does contain
unrelated nested clones such as `.scratch/r22-*/…/corpus/knowledge`, but none
of them is an ancestor of `o02-run`, so they cannot shadow the lookup.)

Denominator agreement — the census counted exactly the live partition:

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ python3 -c "... sorted(e['path'] for e in entries_detail) ..."  # from census.json
223 unique paths
$ LC_ALL=C sort find-paths.txt > find-c.txt
$ LC_ALL=C sort census-paths.txt > census-c.txt
$ comm -3 find-c.txt census-c.txt | wc -l
0
```

Note on a false alarm: a plain `diff` of the two path lists showed one
reordered line (`symbol-lexicon-colexification.md` vs
`symbolism-consistency-rules.md`). That is GNU `sort` locale collation, not a
set difference; under `LC_ALL=C` the sets are identical (0 lines of `comm`
output).

## 3. `--selftest` — 27/27 green

```
$ cd .scratch/o02-run && python3 -B basename-couples-resolver.py --selftest
PASS S1a embedded fixture == live bytes at :72
PASS S1b wrapped field extracts 4/4 by identity (not arity)
PASS S1c no mangled token (prosody.md / toneprosody.md / space split)
PASS S1d before-state: the filed single-line capture yields 0 tokens
PASS S1e space-join is the rejected shape (prosody.md, never tone-prosody.md)
PASS S1f live field resolves 2 direct + 2 unresolved (four-class policy)
PASS S2a phantom tokens survive extraction 2/2
PASS S2b hyphen-wrapped phantom heals to synthetic-phantom-beta.md
PASS S2c zero basename hits -> unresolved (both, not dropped)
PASS S3a two basename hits -> ambiguous
PASS S3b ambiguous is not guessed to one path
PASS S3c one basename hit -> fallback with its explicit mapping
PASS S4a Tier-1 direct wins over a same-basename hit elsewhere (5.4)
PASS S4b direct carries no fallback mapping
PASS S4c corpus-relative path token -> direct (Tier-1 base 3)
PASS S5 no-drop live: 4/4 tokens classed
PASS S5 no-drop phantom: 2/2 tokens classed
PASS S5 no-drop ambiguous: 1/1 tokens classed
PASS S5 no-drop direct: 1/1 tokens classed
PASS S6 slash-bearing token stays unresolved despite a unique basename elsewhere
PASS S7a body prose after a blank line is excluded
PASS S7b couples as the last header field does not swallow the body
PASS S7c blank line + indented prose is excluded (no over-capture)
PASS S8 glob fragment is an artifact, not an unresolved finding (5.6)
PASS S8b glob fragment wins over the ambiguous branch (5.6)
PASS S9 live census conservation (four classes + artifacts == refs)
PASS S10 live wrapped entry reads 4 tokens (2 direct + 2 unresolved)
SELFTEST OK: 27/27 controls
RC=0
```

Control count adds up: S1a–f = 6, S2a–c = 3, S3a–c = 3, S4a–c = 3,
S5 × 4 = 4, S6 = 1, S7a–c = 3, S8/S8b = 2, S9 = 1, S10 = 1 → **27**.
`grep -c '^PASS '` returns 27; exit code 0.

## 4. `--census` — four-class totals and conservation

```
$ cd .scratch/o02-run && python3 -B basename-couples-resolver.py --census
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  fallback mappings (50 distinct):
    … 50 lines …
  unresolved (7 rows):
    honorifics-and-register.md           corpus/knowledge/linguistics/language-contact.md     declared-prospective-seed    c12=blocker
    naming-and-onomastics.md             corpus/knowledge/linguistics/language-contact.md     declared-prospective-seed    c12=blocker
    phonology-basics.md                  corpus/knowledge/linguistics/language-contact.md     declared-prospective-seed    c12=blocker
    sound-change.md                      corpus/knowledge/linguistics/phonetics-phonology.md  declared-prospective-seed    c12=blocker
    tone-prosody.md                      corpus/knowledge/linguistics/phonetics-phonology.md  declared-prospective-seed    c12=blocker
    ../linguistics/phonology-sanity.md   corpus/knowledge/synthesis/typed-label-routing-workflow.md     dangling-reference  c12=blocker
    ../linguistics/phonology-sanity.md   corpus/knowledge/verification/label-channel-routing-verification.md  dangling-reference  c12=blocker
  ambiguous (0 rows):
  glob-fragment (1 rows):
    -gate.md                             corpus/knowledge/verification/gate-frozen-run-standard.md  extractor-artifact  c12=not-applicable
  misaligned: none
RC=0
```

Arithmetic, checked explicitly:

```
four-class sum  2556 + 166 + 0 + 7          = 2729
artifacts       + 1 glob-fragment           = 2730
refs reported                                = 2730
conservation    True (sum=2730 refs=2730)
```

### 4.1 Independent fold from per-entry detail (not trusting the tool's totals)

The JSON census (`--census --json`) carries `entries_detail`, one record per
entry. Recomputing the totals from that raw detail reproduces every published
number:

```
entries_detail records       223
sum(len(tokens))             2730
class fold                   {'direct': 2556, 'fallback': 166,
                              'unresolved': 7, 'glob-fragment': 1}
tool's four_class_totals     {'direct': 2556, 'fallback': 166,
                              'ambiguous': 0, 'unresolved': 7}
tool's artifact_totals       {'glob-fragment': 1}
fallback occurrence sum      166  (== fallback class count)
disposition row sum          8    (7 unresolved + 0 ambiguous + 1 glob)
fallback distinct tokens     50
rows missing reason          none
fallback rows with null map  none
unknown classes              none
misaligned                   []
```

The 50 mapping rows sum to exactly the 166 fallback tokens, so no fallback
token is double-counted or dropped. The 7 unresolved rows each carry a
non-empty `disposition` (`declared-prospective-seed` ×5,
`dangling-reference` ×2) and a non-empty `reason`; the single glob row carries
`extractor-artifact`. This satisfies the claim's "every fallback mapping
listed, every unresolved/ambiguous row reasoned" for the census side.

### 4.2 JSON artifact fields

```
schema       kotodama-couples-census-v3
round        43
tool         .scratch/o02-run/basename-couples-resolver.py
tool_sha256  43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
entries      223
refs         2730
conservation True
```

Determinism: three plain runs produced byte-identical stdout
(`census.out`, `c1.out`, `c2.out` all sha256 `87ef57d5…c7867`); two JSON runs
produced identical JSON (`census.json` == `census2.json`, sha256
`f53899ea…478d`, Python object equality `True`).

### 4.3 Note on zero-token entries

25 entries contribute zero couples tokens (listed in `entries_detail` with an
empty `tokens` dict). Inspection shows these are entries with no `- couples:`
field (or no `.md` token in it), not tokens silently dropped: they are in the
counted 223, and the 2730 refs are exactly the union of the per-entry token
sets. This is the expected shape of the partition, not a coverage loss.

## 5. Wrapped field — 4/4 by identity, not arity

Live wrapped entry is `corpus/knowledge/linguistics/phonetics-phonology.md`.
Its block begins at **line 72** (`- couples:`), matching selftest S1a's
`live_line=72`.

```
$ cd .scratch/o02-run && python3 -B basename-couples-resolver.py --json \
    ../../corpus/knowledge/linguistics/phonetics-phonology.md
[
 {
  "path": "corpus/knowledge/linguistics/phonetics-phonology.md",
  "tokens": {
   "sound-change.md":    {"class": "unresolved", "disposition": "declared-prospective-seed", ...},
   "sound-symbolism.md": {"class": "direct", ...},
   "tone-prosody.md":    {"class": "unresolved", "disposition": "declared-prospective-seed", ...},
   "writing-systems.md":  {"class": "direct", ...}
  },
  "wrapped": true
 }
]
```

Token set by exact string identity:
`{sound-change.md, sound-symbolism.md, tone-prosody.md, writing-systems.md}` —
4/4, with the two soft-wrapped tokens healed (`tone-` + `prosody.md` →
`tone-prosody.md`; `sound-` + `change.md` → `sound-change.md`), and no
`prosody.md` / `toneprosody.md` fragment.

**Identity, not arity — demonstrated.** The S1b predicate is a set equality,
not a count (`basename-couples-resolver.py:328-330`):

```python
tokens = field_refs(LIVE_WRAPPED)
check("S1b wrapped field extracts 4/4 by identity (not arity)",
      tokens == LIVE_TOKENS, sorted(tokens))
```

A decoy token set with the same arity but wrong membership fails that
predicate:

```
tokens                                     ['sound-change.md','sound-symbolism.md','tone-prosody.md','writing-systems.md']
S1b predicate tokens == LIVE_TOKENS        True
len(tokens)                                4
decoy arity 4 passes len==4                True
decoy passes identity predicate            False
```

So a body that merely returned four arbitrary tokens would fail S1b. S10
(`:432`, `len(wrapped_record["tokens"]) == 4`) is the arity corroboration, not
the primary check.

Wrapped detection is structural (`basename-couples-resolver.py:197`:
`"wrapped": len(parts) > 1`), and the census reports exactly one wrapped field
— the same entry — consistent with the selftest.

## 6. Read-only attestation

- No write calls in the body: `grep -nE "open\([^)]*['\"][wax]|\.write\(|shutil|subprocess"`
  → none. The tool opens entries with `"rb"` and writes only `sys.stdout`.
- `git status --porcelain -- corpus tools/harness reports/round-43 reports/round-44`
  → `?? reports/round-44/` only (this round's untracked directory); no tracked
  file modified.
- r42 witness bytes unchanged:
  `sha256sum tools/harness/couples-reference-extractor.py` →
  `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`
  (matches the claim's `d8d23a26…`).
- `reports/round-43/op/O09-scribe.md` digest still `956d478b…cb341`;
  mtime `2026-10-19 14:02`.

## 7. Findings and caveats for integration

1. **The body is byte-exact and green in isolation.** sha256 matches the
   expected `43ce341f…ad64`; selftest 27/27; census four-class 2556/166/0/7
   + 1 glob = 2730 with conservation True. Nothing in my run contradicts
   landing it at `tools/harness/basename-couples-resolver.py`.
2. **Census JSON fields are location- and round-stamped, not content-stamped.**
   `payload["round"] = 43` is hardcoded (`basename-couples-resolver.py:461`)
   and `payload["tool"]` is `relpath(__file__, LANE)`
   (`:462`). When the integrator lands the body at `tools/harness/`, the JSON
   `tool` will read `tools/harness/basename-couples-resolver.py`, while
   `round` will still say `43`. `tool_sha256` is over the file bytes and stays
   `43ce341f…`. The filed r44 census artifact should either carry `round: 43`
   as the body emits it or be amended by the integrator's artifact step —
   that is a filing decision, not a body defect; `to-verify` for O06/O09.
3. **The scratch run's `tool` field** (`.scratch/o02-run/…`) is evidence that
   the measurement was taken from the scratch copy, not from an in-tree
   resolver. The in-tree path does not exist yet at this baseline.
4. **Scope boundaries honored:** parity against the r42 witness (O07), the
   defect-fix line refs (O03), the 4-class disposition schema (O06), and the
   negative-proof gate (O08) are other seats. I did not run the r42 extractor
   and did not write under `corpus/` or `tools/`.

## 8. Reproduce

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
mkdir -p .scratch/o02-run
sed -n '356,870p' reports/round-43/op/O09-scribe.md \
  > .scratch/o02-run/basename-couples-resolver.py
sha256sum .scratch/o02-run/basename-couples-resolver.py   # 43ce341f…ad64
cd .scratch/o02-run
python3 -B basename-couples-resolver.py --selftest        # SELFTEST OK: 27/27
python3 -B basename-couples-resolver.py --census          # 2556/166/0/7 +1 glob
python3 -B basename-couples-resolver.py --census --json > census.json
```

Artifact digests recorded at observation time:

```
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64  basename-couples-resolver.py
87ef57d5db28676563dbb94df838bdc0979482bc1dc4229548357c20adfc7867  census.out (== c1.out == c2.out)
f53899ea1b695d52170bffe541cda2cdd621dd09c1526bc6557b25ee398d478d  census.json (== census2.json)
7d452a85483b8d6771d81262a3f171eb0961cd8a9b026688b88bf8dcf3aaedef  live-entry.json
```
