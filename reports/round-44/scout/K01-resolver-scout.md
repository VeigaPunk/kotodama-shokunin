- Seat: K01 | scout | claim O | date 2026-10-19 | baseline `c9f4eaa` | out `reports/round-44/scout/K01-resolver-scout.md`
- Status: read-only scout. This file is the only report path written. Disposable probes live under `.scratch/k01/` (gitignored). No filed byte, corpus byte, or harness byte was edited; nothing staged under `corpus/`; no `run-validation.py` executed; no git/network/install action.

# K01 — resolver scout: landing spec for the r43 O09 successor body

## 0. Bottom line

1. **The body extracts byte-exactly and its digest is confirmed.** Lines 356–870 of
   `reports/round-43/op/O09-scribe.md` (between the ````python fence at `:355` and
   the closing fence at `:871`) are 515 lines; written with exactly one trailing
   LF they hash to
   `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`, matching
   the claim's `43ce341f…` and O09's own pin at `op/O09-scribe.md:887`. The
   trailing-byte variants are distinct: one extra LF → `06ea6318…` (21733 B);
   final LF stripped → `c6821cf1…` (21731 B). Only the 21732-byte `sed` output
   is the pinned artifact.
2. **The body runs green independently.** From a clean `.scratch/k01/` copy:
   `--selftest` → `SELFTEST OK: 27/27 controls`, rc 0; `--census` →
   `entries=223 refs=2730`; `policy four-class: direct=2556 fallback=166
   ambiguous=0 unresolved=7`; `glob-fragment=1`; `conservation: True
   (sum=2730 refs=2730)`; 50 distinct fallback mappings; 7 reasoned unresolved
   rows.
3. **The target path is free.** `tools/harness/basename-couples-resolver.py` does
   not exist at `c9f4eaa` (`ls` → `No such file or directory`). The file is a new
   file; no existing instrument is overwritten.
4. **The r42 extractor is untouched and needs no byte edit to be demoted.** Its
   digest before and after this scout's runs is
   `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1` (332
   lines). Demotion is by record (new file's docstring + parity receipt + LOG /
   SCORECARD rows), not by rewriting its bytes (see §4).
5. **Parity is exact, not approximate.** A per-entry, per-token diff over all 223
   entries: 2730 live token rows vs 2730 successor token rows, **0 class shifts**
   under the four-class fold, identical 422 distinct tokens, **0 fallback mapping
   mismatches**. The only visible difference is presentation: r42 prints
   `prospective` as a sixth bucket; the successor folds those 5 occurrences into
   `unresolved` with disposition `declared-prospective-seed`.
6. **Ordering constraint for the integrator.** `--census` always reads the live
   `corpus/knowledge/*/*.md` tree (no path filter on `--census`; O09:576,
   `:811-812`). The filed census must therefore be captured **before** the claim-C
   entry lands, or the tool will read 224 entries and the claim's 223-denominator
   arithmetic will not reproduce. See §3.4.

## 1. Source verification

### 1.1 Extraction and digest

Commands run from the lane root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

```
sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/k01/body-nonl.py
printf '\n' >> .scratch/k01/body-nonl.py
sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/k01/body-lf.py
sha256sum .scratch/k01/body-nonl.py .scratch/k01/body-lf.py
```

```
06ea6318a04b1049b7e3d4187cac2a9429fef067c23872d147a49b1d972cae24  .scratch/k01/body-nonl.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64  .scratch/k01/body-lf.py
```

`body-lf.py`: 515 lines, 21732 bytes, mode 0644, first line
`#!/usr/bin/env python3`, last line `    sys.exit(main())`. The fenced block has
no indentation prefix and no embedded fence, so `sed` extraction is byte-exact.

### 1.2 Selftest (27/27, rc 0)

```
$ python3 -B .scratch/k01/body-lf.py --selftest
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
SELFTEST_RC=0
```

S1b compares the extracted token **set** to `LIVE_TOKENS`
(`sound-change.md`, `tone-prosody.md`, `sound-symbolism.md`,
`writing-systems.md`; O09:636-638), not a count, so a drop-plus-mangle that kept
arity at 4 would fail. S1a additionally compares the embedded fixture to the
live field bytes at `corpus/knowledge/linguistics/phonetics-phonology.md:72`
(O09:657-681); it passes.

### 1.3 Census (223 entries, rc 0)

```
$ python3 -B .scratch/k01/body-lf.py --census
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  fallback mappings (50 distinct):
    ...50 mapping lines, full table at op/O09-scribe.md:238-289...
  unresolved (7 rows):
    honorifics-and-register.md           corpus/knowledge/linguistics/language-contact.md     declared-prospective-seed    c12=blocker
    naming-and-onomastics.md             corpus/knowledge/linguistics/language-contact.md     declared-prospective-seed    c12=blocker
    phonology-basics.md                  corpus/knowledge/linguistics/language-contact.md     declared-prospective-seed    c12=blocker
    sound-change.md                      corpus/knowledge/linguistics/phonetics-phonology.md  declared-prospective-seed    c12=blocker
    tone-prosody.md                      corpus/knowledge/linguistics/phonetics-phonology.md  declared-prospective-seed    c12=blocker
    ../linguistics/phonology-sanity.md   corpus/knowledge/synthesis/typed-label-routing-workflow.md      dangling-reference  c12=blocker
    ../linguistics/phonology-sanity.md   corpus/knowledge/verification/label-channel-routing-verification.md dangling-reference c12=blocker
  ambiguous (0 rows):
  glob-fragment (1 rows):
    -gate.md                             corpus/knowledge/verification/gate-frozen-run-standard.md  extractor-artifact  c12=not-applicable
  misaligned: none
CENSUS_RC=0
```

`--census --json` assertions read back from `.scratch/k01/census.json`:

```
entries 223 refs 2730 four {'ambiguous': 0, 'direct': 2556, 'fallback': 166, 'unresolved': 7}
art {'glob-fragment': 1} cons True
fallback_mappings 50
unresolved dispositions Counter({'declared-prospective-seed': 5, 'dangling-reference': 2})
c12 Counter({'blocker': 7})
all reasons nonempty True
```

The JSON carries `schema: kotodama-couples-census-v3`, `round: 43`, `tool`,
`tool_sha256`, `wrapped_fields`, `fallback_mappings`, `disposition`,
`misaligned`, `entries_detail` (O09:809-821). `tool_sha256` is computed from the
running file's own bytes (O09:818-819), which makes the landed digest
self-checking.

### 1.4 Live r42 witness, measured (read-only)

```
$ python3 -B tools/harness/couples-reference-extractor.py --census
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
  misaligned: none
LIVE_RC=0
```

`ambiguous` is absent from the printed line because its value is 0 (the print
filters zero-valued buckets, `couples-reference-extractor.py:309-312`). So the
claim's shorthand `2556/166/2/5/1` maps to direct/fallback/unresolved/
prospective/glob-fragment — **not** to "2 ambiguous". The numbers are right; the
label order in the claim's `before` line should be read this way.

Witness selftest is 8/8 green (`--selftest | grep -c '^PASS'` → 8, rc 0).

### 1.5 Parity diff (independent probe)

Imported both modules in-process (no writes), resolved all 223 entries, folded
r42's six classes onto the policy four (`prospective` → `unresolved`,
`glob-fragment` stays an artifact):

```
live token rows 2730 new token rows 2730 class-shift rows 0
distinct tokens live/new 422 422 only-live [] only-new []
fallback mapping mismatches 0 []
```

This is the parity evidence O07's receipt should quote: same input, same tokens,
same mappings; the subclass separation is exactly the 5 `prospective` →
`unresolved`/`declared-prospective-seed` rows. Zero tokens dropped.

## 2. Defects the O09 body fixes vs the live extractor

All line references are to the durable sources:
`tools/harness/couples-reference-extractor.py` (r42 witness) and
`reports/round-43/op/O09-scribe.md` (successor body, fenced `:356-870`).

| # | defect | r42 witness | O09 successor | measured proof |
|---|---|---|---|---|
| D1 | **blank-line over-capture** | `couples_block` skips a blank line with `continue` (`:64-65`), then accepts the next indented line (`:68-69`) — body prose after a blank line becomes a couples token | `couples_block` sets `saw_blank` (`O09:421-425`); an indented continuation after a blank is accepted only under the hyphen soft-wrap exception (`O09:428-432`), otherwise `break` (`:433`) | fixture `.scratch/k01/fixture/linguistics/overcap.md` (field, blank, indented prose naming 2 more `.md`): r42 reads **3** tokens (`writing-systems.md`, `sound-symbolism.md`, `phonetics-phonology.md`); successor reads **1** (`writing-systems.md`) |
| D2 | **no ambiguous control** | `classify(ref, entry_dir, prospective=False)` reads the global `basename_index()` (`:124-131`, `:134-150`); the live corpus has 0 duplicate basenames, so the ambiguous branch is untestable | `classify(ref, entry_dir, index=None)` accepts an injected index (`O09:499-514`); S3a/S3b inject two hits (`O09:724-726`), S5 ambiguous no-drop (`:741-751`) | successor selftest S3a/S3b PASS; live census ambiguous=0 |
| D3 | **glob precedence** | glob check runs only **after** slash and basename-hit checks (`:139-147`), so a glob fragment whose basename has one hit becomes `fallback` and with two hits becomes `ambiguous` | glob check runs before the slash/hit tiers (`O09:504-505`), per policy §5.6 (`reports/round-42/calib/basename-couples-policy-full.md:97-102`) | S8 (`O09:772-774`) and S8b with two injected hits (`:775-779`) PASS |
| D4 | **four-class census** | six buckets, printed with `unresolved`/`prospective` as separate classes; no artifact/class split (`:186-210`, `:306-312`) | `four_class_totals` + `artifact_totals`, conservation identity (`O09:609-623`), headline print (`:822-831`) | successor: `2556+166+0+7=2729`, `+1 glob=2730`, `conservation: True` |
| D5 | **disposition leg** | `census` returns only an unresolved count map (`:199-202`); no reasons, no ambiguous rows, no fallback mapping list | `_reason` names a reason per class (`O09:555-571`); `disposition` rows carry `entry/token/mapping/disposition/reason/c12` (`:594-605`); `fallback_mappings` aggregates every mapping (`:589-593`); CLI prints all of it (`:834-843`) | 50 mappings listed; 7 unresolved rows all have non-empty reasons; 5 `declared-prospective-seed` + 2 `dangling-reference`; 1 glob row; 0 ambiguous rows |
| D6 | **indented-prose control** | the over-capture fixture uses a **non-indented** paragraph (`:231-239`), so it passes even with the blank-skip bug; no indented-prose control | S7c is an explicit blank + indented prose fixture (`O09:766-770`) | S7c PASS |
| D7 | **wrapped identity, not arity** | wrapped positive checks sorted token list equals 4 names (`:252-257`), which is identity, but no live-byte equality check and no "before" single-line zero check | S1a byte-equality with the live field; S1b set identity against `LIVE_TOKENS`; S1d documents the single-line 0-token before-state; S10 length 4 (`O09:680-709`, `:786-789`) | all PASS |
| D8 | **last-header control** | no explicit control; behavior is correct because a non-indented line breaks the loop | S7b explicit (`O09:761-764`) | PASS; my independent fixture also reads 1 token in both tools |
| D9 | **slash gate** | `if "/" in ref: unresolved` (`:139-140`) | same, before the index (`O09:506-507`), with S6 (`:753-755`) | PASS |
| D10 | **phantom visibility** | `prospective` fifth class for declared seeds (`:148-149`) | folds declared seeds into `unresolved` + `declared-prospective-seed` disposition; phantom tokens survive 2/2 (`O09:711-722`) | successor rows show both phantom tokens as unresolved/declared-prospective-seed |

Not a defect claim: both tools keep the hyphen-retained soft-wrap heal
(`tone-` + `prosody.md` → `tone-prosody.md`, r42 `:76-93`, O09 `:438-454`); the
successor carries it unchanged, and S1c/S2b guard it.

## 3. Landing spec

### 3.1 Target and bytes

| item | value |
|---|---|
| target path | `tools/harness/basename-couples-resolver.py` |
| action | create new file; do **not** touch `tools/harness/couples-reference-extractor.py` |
| source bytes | `reports/round-43/op/O09-scribe.md:356-870`, inclusive; `sed` emits the block's own final LF — append nothing |
| expected sha256 | `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64` |
| expected size / lines | 21732 bytes / 515 lines |
| mode | 0644 (no chmod needed) |
| imports | stdlib only (`argparse`, `glob`, `hashlib`, `json`, `os`, `re`, `sys`); no import of the r42 tool, no `.scratch` read, no subprocess/network |
| write surface | none: corpus files opened `"rb"` for reading; `sys.dont_write_bytecode = True` (`O09:380`) |

Apply command (integrator, from the lane root):

```
sed -n '356,870p' reports/round-43/op/O09-scribe.md > tools/harness/basename-couples-resolver.py
sha256sum tools/harness/basename-couples-resolver.py
# must print 43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
```

**Do not append a newline.** `sed` already writes the terminating LF of line
870. The three measured variants are:

| trailing bytes | size | sha256 |
|---|---|---|
| exactly one LF (correct; `sed` output) | 21732 | `43ce341f…ad64` |
| two LFs (`sed` + `printf '\n' >>`) | 21733 | `06ea6318…ae24` |
| no final LF (`head -c -1`) | 21731 | `c6821cf1…f0c7` |

Only the first is the claim's pinned artifact. If the extraction is done by
copy/paste instead, ensure exactly one final newline.

### 3.2 No header/path adjustment is sanctioned by the body

The body's docstring hardcodes the policy path
(`reports/round-42/calib/basename-couples-policy-full.md`), the defect provenance
(`reports/round-19/audit/entry-audit.py:75`,
`reports/round-39/calib/Ca04-verify.md` D1/D2), and the predecessor path + digest
(`couples-reference-extractor.py`, `d8d23a26…`, "remains the N6 regression
witness") — all correct at `c9f4eaa` (`O09:357-369`; I verified each cited line:
`entry-audit.py:75` is the single-line regex, Ca04 D1/D2 at
`reports/round-39/calib/Ca04-verify.md:78-106`, wrapped field at
`corpus/knowledge/linguistics/phonetics-phonology.md:72-77`). It makes no claim
about its own install path; root discovery is positional
(`os.path.realpath(__file__)` upward, `O09:382-390`).

The one stale metadata field is `payload["round"] = 43` in the `--census --json`
payload (`O09:816`). It is a provenance label, not behavior. Recommendation:
**land verbatim** (the claim pins these bytes and a byte edit would require a new
digest + re-verification), and have the filed artifact carry `round: 44`,
`baseline_commit: c9f4eaa`, and `tool_internal_round: 43` with a one-line note.
If the integrator instead edits the field to 44, that is a new artifact: re-pin
its digest and re-run the full §5 checklist; do not keep both digests as
"the" tool.

### 3.3 Preconditions (verified at this cut)

- `tools/harness/basename-couples-resolver.py` absent — `ls` returns
  `No such file or directory`.
- `corpus/knowledge` entry total is 223 — `find corpus/knowledge -name '*.md' |
  wc -l` → `223`.
- r42 witness digest is `d8d23a26…` and unchanged after every read-only run in
  this scout.
- `reports/round-44/run-validation.py` is **absent** at this cut; the claim's
  third counting command cannot run until the integrator authors it. Treat its
  O-leg assertions as the checklist in §5.

### 3.4 Ordering: capture the 223-census before the C landing

`census()` defaults to a live glob over `KNOW` (`O09:574-577`) and the CLI's
`--census` mode takes no path filter (`O09:811-812`); the positional `PATH`
mode resolves individual entries only. Therefore:

1. apply the resolver;
2. run `--selftest` and `--census --json` while the tree is still 223 entries;
3. file the single census artifact at `reports/round-44/calib/` (recommended
   basename `couples-census-r44.json`; O06 may bind the exact name, but exactly
   **one** JSON may be filed);
4. only then apply the claim-C entry and README rev 2.5.

If C lands first, a fresh `--census` reads 224 and the four-class totals change
by the new entry's tokens; the claim's `2556+166+0+7=2729 +1 glob` would no
longer reproduce from the live tree. The artifact must state
`entries: 223`, `baseline_commit: c9f4eaa`, and a `state_note` that it is the
pre-C-landing census. The `run-validation.py` O leg should verify the **filed
artifact** (or run its O checks before its C checks), not re-census the 224 tree
and compare to 223.

## 4. Demoting `couples-reference-extractor.py` to witness-only without editing its bytes

### 4.1 Why no byte edit is needed

The r42 tool is a green, tracked instrument (8/8 selftest, `d8d23a26…`,
`SCORECARD.md:822`). The distinction between "census authority" and "regression
witness" is a **role** distinction, not a code distinction: both read the same
corpus, but only the successor's output is filed as the census and only the
successor is named by the runner. Nothing in the r42 code must change for that.

### 4.2 Records that perform the demotion (append-only, no filed-byte edits)

| surface | content | owner |
|---|---|---|
| landed successor docstring | already says: predecessor "NOT edited, NOT imported", "remains the N6 regression witness" (`O09:362-364`) — this is in the **new** file's bytes | integrator (by landing) |
| parity receipt | one record under `reports/round-44/calib/` (O07): both runs quoted, same 223/2730 input, differences explained solely by the four-class-vs-six-class subclass separation (`prospective` → `unresolved`/`declared-prospective-seed`), r42 labeled **witness-only** and not a census authority | O07 + integrator |
| census artifact | names `tool: tools/harness/basename-couples-resolver.py`, `tool_sha256: 43ce341f…`; the witness does not appear as a census producer | O06 + integrator |
| `LOG.md` r44 entry | one sentence: new authority landed; `couples-reference-extractor.py` demoted **by record** to N6 witness, bytes at `d8d23a26…` untouched | integrator |
| `SCORECARD.md` r44 operability row | names the new authority; may cite the witness digest as the unchanged predecessor | integrator (if the round is admitted) |
| optional discoverability | `SKILL.md` harness table (`SKILL.md:452-454` is the existing table area) gains a row for the resolver; not required by claim O and not a packet-surface change | integrator, optional |

### 4.3 Forbidden demotion moves (would violate "bytes untouched" or fork authority)

- Do not rename, move, delete, chmod, or reformat
  `tools/harness/couples-reference-extractor.py`; its digest must stay
  `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`.
- Do not add a shim/wrapper named after the old tool, and do not import it from
  the successor (the successor is standalone by construction, `O09:186-188`).
- Do not file two census JSONs (one from each tool) as authorities. The r42 run
  appears only inside the parity receipt as a witness quote.
- Do not leave the `.scratch/k01/body-lf.py` copy as a second durable resolver;
  `.scratch` is disposable and must not be referenced by the runner.

## 5. Acceptance checklist (for the integrator / O02 / O07 / O10)

Run from the lane root with `PYTHONDONTWRITEBYTECODE=1`:

1. `sha256sum tools/harness/basename-couples-resolver.py` →
   `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`.
2. `python3 -B tools/harness/basename-couples-resolver.py --selftest` → rc 0,
   27 `PASS` lines, `SELFTEST OK: 27/27 controls`.
3. `python3 -B tools/harness/basename-couples-resolver.py --census` → rc 0, first
   line `entries=223 refs=2730`, four-class line
   `direct=2556 fallback=166 ambiguous=0 unresolved=7`, artifact line
   `glob-fragment=1`, `conservation: True`, exactly 50 mapping lines.
4. `--census --json` parses; `four_class_totals` and `artifact_totals` as above;
   `len(fallback_mappings)==50`; `len(disposition["unresolved"])==7`; every
   disposition row has a non-empty `reason`; `disposition["ambiguous"]==[]`
   (the ambiguous control is synthetic, S3a/S3b).
5. Per-entry wrapped read:
   `... corpus/knowledge/linguistics/phonetics-phonology.md` → `wrapped=True
   tokens=4`, `sound-symbolism.md` + `writing-systems.md` direct,
   `sound-change.md` + `tone-prosody.md` unresolved/declared-prospective-seed,
   no standalone `prosody.md`.
6. `sha256sum tools/harness/couples-reference-extractor.py` → unchanged
   `d8d23a26…`; its `--census` still prints `wrapped fields: 1` and the same four
   token names (witness cross-check).
7. `git status --porcelain` shows no modification under `corpus/`, no
   `M tools/harness/couples-reference-extractor.py`, and only the expected
   new files.
8. One census artifact, one parity receipt; both name the authority and the
   witness as above.

## 6. Risks, limits, `to-verify`

- **Ambiguous live rows are zero.** The claim's disposition leg covers
  "unresolved/ambiguous" rows, but at 223 entries there are no ambiguous rows
  (0 duplicate basenames). The ambiguous path is exercised only synthetically
  (S3a/S3b, injected index). Any future duplicate basename changes the census;
  policy §5.5 (`basename-couples-policy-full.md:93-96`) already requires
  re-adjudication then. This is coverage by control, not by live data — state it
  that way in the parity receipt.
- **`joined.find(ref)` group labels** are best-effort for brace-expanded tokens
  not present literally (`O09:941-942`); live `misaligned=0`, so no finding
  depends on it. `to-verify` only if a per-token `group` field is made binding.
- **`tone-prosody.md`** remains an authorial-intent reading, not a filed rule;
  in-file witness `corpus/knowledge/linguistics/phonetics-phonology.md:279`
  writes the name in full. Inherited `to-verify`.
- **The 223 denominator is pre-C.** If the round lands C first, the census
  arithmetic is not reproducible from the live tree (§3.4). This is the single
  ordering risk in claim O.
- **`payload["round"] = 43`** is internal metadata (§3.2). Verbatim landing keeps
  the pinned digest; the filed artifact must carry the r44 provenance.
- **`reports/round-44/run-validation.py` is absent** at this cut; the claim's
  counting command cannot be run until it exists. `to-verify` at integration.
- **Not verified here:** a true no-corpus-above isolation run (would require a
  path outside the repo); O02 owns that. This scout ran the body from
  `.scratch/k01/`, where upward discovery correctly finds the lane root.

## 7. Commands run (all read-only except `.scratch` writes)

```
git rev-parse --short HEAD                                   -> c9f4eaa
sha256sum tools/harness/couples-reference-extractor.py       -> d8d23a26…cf1
find corpus/knowledge -name '*.md' | wc -l                   -> 223
sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/k01/body-lf.py
sha256sum .scratch/k01/body-lf.py                            -> 43ce341f…ad64 (515 lines, 21732 bytes)
python3 -B .scratch/k01/body-lf.py --selftest                -> 27/27, rc 0
python3 -B .scratch/k01/body-lf.py --census                  -> 223/2730, 2556+166+0+7, glob=1, conservation True
python3 -B .scratch/k01/body-lf.py --census --json           -> 50 mappings, 7 unresolved rows, all reasons non-empty
python3 -B tools/harness/couples-reference-extractor.py --census
                                                             -> 2556/166/unresolved=2/prospective=5/glob=1
python3 -B tools/harness/couples-reference-extractor.py --selftest -> 8/8, rc 0
python3 -B tools/harness/couples-reference-extractor.py .scratch/k01/fixture/linguistics/overcap.md
                                                             -> 3 tokens (over-capture)
python3 -B .scratch/k01/body-lf.py .scratch/k01/fixture/linguistics/overcap.md
                                                             -> 1 token (fixed)
# in-process per-token parity over 223 entries
                                                             -> 2730/2730 rows, 0 class shifts, 422/422 tokens, 0 mapping mismatches
git status --porcelain                                       -> ?? reports/round-44/ (only)
```
