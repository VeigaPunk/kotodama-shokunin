# O03 — Defects verifier: does the r43 O09 successor body fix the live extractor's defects?

- **Seat:** O03 (verifier 2, claim O) · round 44 · baseline commit `c9f4eaa` · 2026-10-19
- **Subject:** `reports/round-43/op/O09-scribe.md:356-870` (the fenced successor body)
- **Witness:** `tools/harness/couples-reference-extractor.py` (r42, read-only; sha256 unchanged)
- **Policy:** `reports/round-42/calib/basename-couples-policy-full.md` §2 (four classes), §5.6 (glob fragments), lines 98-102
- **Method:** byte-extracted the O09 body into `.scratch/o03/basename-couples-resolver.py`, loaded both tools as modules, ran four targeted defect fixtures plus a whole-corpus differential. No filed byte edited; no corpus write.

## 0. Identity of the artifact under test

```
$ sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/o03/basename-couples-resolver.py
$ sha256sum .scratch/o03/basename-couples-resolver.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64  .scratch/o03/basename-couples-resolver.py
$ wc -l .scratch/o03/basename-couples-resolver.py
515 .scratch/o03/basename-couples-resolver.py
$ python3 -B .scratch/o03/basename-couples-resolver.py --selftest | tail -1
SELFTEST OK: 27/27 controls
$ grep -c '^PASS' <(python3 -B .scratch/o03/basename-couples-resolver.py --selftest)
27
```

Digest matches the claim-pinned `43ce341f…`; 27 executed controls (24 `check()` source
sites, one of which — S5 — runs over 4 fixtures).

Witness digest before and after every run in this seat:

```
$ sha256sum tools/harness/couples-reference-extractor.py
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1
```

## 1. Verdict matrix

| # | Defect claimed in the live extractor | Fixed / present in O09 body | Verdict |
|---|---|---|---|
| D1 | blank-line over-capture (`continue` at the blank line) | break-at-blank via `saw_blank`, O09 `:423-425`, `:429`, `:433` | **FIXED** (fixture-proven; 0 live incidence) |
| D2 | glob-fragment resolved/classed by lower branches instead of precedence | `GLOB_FRAG_RE` checked before `/` and before the basename index, O09 `:504-505` vs live `:139-147` | **FIXED** |
| D3 | no ambiguous control in the selftest | S3a/S3b, O09 `:724-726`; fixture index `:644-650` | **PRESENT** |
| D4 | no indented-prose control | S7c, O09 `:766-770` | **PRESENT** |
| D5 | no four-class census | `CLASSES`/`ARTIFACTS` `:495-496`; `four_class_totals`/`artifact_totals`/`conservation` `:609-617` | **PRESENT** |
| D6 | no disposition leg (no per-token reason) | `disposition` `:538-543`; `_reason` `:555-571`; rows `:595-605` | **PRESENT** |

Every item the claim asserted is confirmed. Details and reproductions below.

## 2. D1 — blank-line over-capture

**Live code path** (`couples-reference-extractor.py:63-65`):

```python
for following in lines[index + 1:]:
    if not following.strip():
        continue
```

A blank line is skipped, so an indented line after it (before the next header field) is
still captured. **O09 code path** (`reports/round-43/op/O09-scribe.md:422-433`): the blank
line sets `saw_blank`, and the indentation branch requires `(not saw_blank or soft_wrap)`;
with `soft_wrap` itself gated on `not saw_blank` (`:428`), any blank line reaches `break`
at `:433`.

Fixture (couples as the last header field, then a blank line, then indented body prose):

```python
D1 = ("- topic: fixture\n"
      "- couples: method — `writing-systems.md`\n"
      "\n"
      "  Indented body prose names `sound-symbolism.md` and `tone-prosody.md`.\n")
```

Observed:

```
live parts = ['method — `writing-systems.md`', 'Indented body prose names `sound-symbolism.md` and `tone-prosody.md`.']
new  parts = ['method — `writing-systems.md`']
live refs  = ['sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
new  refs  = ['writing-systems.md']
```

Same result when a header field follows the indented prose (`D1b`): live captures
`prose names sound-symbolism.md`, O09 captures only the field. **D1 fixed.**

### D1 honesty qualifier — latent, not live

The trap is **not currently realized anywhere in the 223-entry corpus**:

- Part-level differential `live.couples_block(text)` vs `new.couples_block(text)` over all
  223 files: `live parts > new parts: 0`, `new parts > live parts: 0`,
  `wrapped-flag disagreements: 0`.
- Token-set differential: per-entry token sum `2730` both sides; entries where live
  captures tokens new does not: **0**; entries where new captures tokens live does not: **0**.
- Structural exposure: **19 entries have `couples` as the last header field**
  (e.g. `linguistics/color-terminology.md`, `linguistics/conlang-methodology.md`), i.e. a
  future indented paragraph after the field would trip live's over-capture. Entries
  currently containing a blank line followed by an indented line before the next field:
  **0**.

So the defect is a live code path with zero present incidence; the O09 body closes it as a
latent trap. Reading the claim's "confirmed blank-line over-capture" as a *code-path*
confirmation is correct; reading it as a *present count error* would not be.

### D1b — why the live selftest never caught it

Live `OVER_CAPTURE_TRAP` (`couples-reference-extractor.py:231-239`) puts
`- verified-at: 2026-10-19` immediately after the couples field, so `FIELD_RE` breaks the
block (`:66-67`) before the blank-line logic is ever reached; its prose is also
non-indented, which the `INDENT_RE` branch rejects anyway. The control passes for reasons
unrelated to blank handling. O09's S7a/S7b/S7c (`:757-770`) exercise the three shapes
directly.

## 3. D2 — glob-fragment precedence (policy §5.6)

Policy text (`basename-couples-policy-full.md:100-102`): glob fragments must be "skip[ped]
or separately class[ed]"; the policy "forbids counting them as unresolved couples findings
or resolving them via the fallback."

Branch order, live (`couples-reference-extractor.py:134-150`):

```
direct (136-138) -> "/" unresolved (139-140) -> one-hit fallback (141-143)
-> multi-hit ambiguous (144-145) -> glob-fragment (146-147) -> prospective (148-149)
-> unresolved (150)
```

Branch order, O09 (`reports/round-43/op/O09-scribe.md:499-514`):

```
direct (501-503) -> glob-fragment (504-505) -> "/" unresolved (506-507)
-> one-hit fallback / multi-hit ambiguous / zero-hit unresolved (508-514)
```

Because live `classify()` reads a module-level index and takes no index parameter, the
two-hit/one-hit cases cannot occur with the real corpus (`-gate.md` has zero hits). I
injected synthetic indexes at runtime in `.scratch` — no filed byte edited:

```
== D2 glob precedence, injected two-hit index ==
live classify = ('ambiguous', None)
new  classify = ('glob-fragment', None)
== D2 glob precedence, injected one-hit index ==
live classify = ('fallback', 'corpus/knowledge/verification/-gate.md')
new  classify = ('glob-fragment', None)
== D2b slash-bearing glob fragment ==
live classify = ('unresolved', None)
new  classify = ('glob-fragment', None)
```

`fallback` here is exactly the policy-forbidden resolution; `ambiguous`/`unresolved` are the
forbidden counting. **D2 fixed** — O09 gives glob-fragment precedence over all three lower
branches, including the ambiguous branch (S8b, `:772-779`).

## 4. D3 — ambiguous control

- Live: the `ambiguous` branch exists (`:144-145`) but the selftest has **8 `check()` sites**
  and none exercises it (`inspect.getsource(live.selftest)` contains no `ambiguous`);
  `grep` of the selftest source confirms.
- O09: fixture index with two hits (`:644-650`) plus
  `S3a two basename hits -> ambiguous` and `S3b ambiguous is not guessed to one path`
  (`:724-726`), both PASS. The census also emits an `ambiguous` row list (0 rows at HEAD).

**D3 present.** (Live's branch is correct in isolation; what it lacked was the control.)

## 5. D4 — indented-prose control

- Live: no control for the blank+indented shape (see D1b); 8 selftest checks total.
- O09: `S7c blank line + indented prose is excluded (no over-capture)`, `:766-770`, PASS.
  Backed by S7a (`:757-760`, non-indented body prose) and S7b (`:761-764`, couples as last
  header field).

**D4 present.**

## 6. D5/D6 — four-class census and disposition leg

`--census` on the extracted body:

```
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  fallback mappings (50 distinct):
    ... 50 mapping lines ...
  unresolved (7 rows):
    honorifics-and-register.md           corpus/knowledge/linguistics/language-contact.md     declared-prospective-seed    c12=blocker
    naming-and-onomastics.md             corpus/knowledge/linguistics/language-contact.md     declared-prospective-seed    c12=blocker
    phonology-basics.md                  corpus/knowledge/linguistics/language-contact.md     declared-prospective-seed    c12=blocker
    sound-change.md                      corpus/knowledge/linguistics/phonetics-phonology.md  declared-prospective-seed    c12=blocker
    tone-prosody.md                      corpus/knowledge/linguistics/phonetics-phonology.md  declared-prospective-seed    c12=blocker
    ../linguistics/phonology-sanity.md   corpus/knowledge/synthesis/typed-label-routing-workflow.md dangling-reference           c12=blocker
    ../linguistics/phonology-sanity.md   corpus/knowledge/verification/label-channel-routing-verification.md dangling-reference           c12=blocker
  ambiguous (0 rows):
  glob-fragment (1 rows):
    -gate.md                             corpus/knowledge/verification/gate-frozen-run-standard.md extractor-artifact           c12=not-applicable
  misaligned: none
```

`--census --json` parses; `conservation: true`; every unresolved and glob row carries a
non-empty `reason` and a `c12` value; `fallback_mappings` has 50 distinct entries. Schema
reports `kotodama-couples-census-v3`, `entries=223`, `refs=2730`,
`four={'direct':2556,'fallback':166,'ambiguous':0,'unresolved':7}`,
`artifacts={'glob-fragment':1}`, `misaligned=[]`, `wrapped=1`.

Live comparator (`couples-reference-extractor.py --census`):

```
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
  misaligned: none
```

The class arithmetic reconciles exactly: live's fifth `prospective` class (5 tokens, all in
`language-contact.md` / `phonetics-phonology.md`) folds into O09's `unresolved` with the
`declared-prospective-seed` disposition; live's `unresolved=2` are O09's
`dangling-reference` rows. `2556+166+0+2+5+1 = 2556+166+0+7+1 = 2730`. No token is dropped,
added, or guessed. **D5/D6 present.**

## 7. Residual findings (non-blocking; do not change the pinned bytes)

1. **Docstring overclaims an exception the code does not implement.** O09 `:411-414`
   says a blank line terminates the block "unless the previous part ends in a hyphen soft
   wrap and the next line is indented", but `soft_wrap` is defined as
   `parts[-1].endswith("-") and not saw_blank` (`:428`), so after a blank line `soft_wrap`
   is always false and the exception is unreachable. Fixture `D1c` (`tone-` / blank /
   indented `prosody.md`) yields `new refs = []`. There are **0** blank-separated
   continuations in the live corpus, so nothing is lost today; the behavior (blank always
   terminates) is the safe one for the defect being fixed. Since the body must land
   byte-exact at `43ce341f…`, this is a **successor-record note**, not an edit now.
2. **`--census --json` hardcodes `"round": 43`** (O09 `:816`). A round-44 census artifact
   produced by the landed tool will carry `round: 43` unless the integrator records it as
   the tool's authoring provenance or overrides it in the filing wrapper. Do not edit the
   pinned body; O06/the integrator should name this in the artifact header.
3. **Selftest S1a is corpus-coupled**: it asserts the embedded fixture equals the live
   bytes of `corpus/knowledge/linguistics/phonetics-phonology.md` (`:627-638`, `:677-681`).
   Any future edit to that entry's couples block turns `--selftest` red. This is by design
   (a drift alarm), but it means the resolver is not corpus-stable; worth a note where
   durability is claimed. The C landing (one new entry elsewhere) does not touch it; S9/S10
   only assert conservation and the wrapped record, so a 223→224 total does not break the
   selftest.
4. **Census denominator**: all numbers above are at HEAD `c9f4eaa`, 223 entries / 2730 refs,
   before C's landing. If the census artifact is filed after C lands, its denominator is
   224 and its totals will not match the claim's `2556+166+0+7`; the artifact must pin its
   own `entries` value and say which tree it was measured on.

## 8. Attestations

- `tools/harness/couples-reference-extractor.py` bytes untouched: sha256
  `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1` before and after all
  runs.
- No file written outside `.scratch/o03/` and this out path. No corpus staging, no git, no
  network, no in-tree validation runner.
- Synthetic index injection was done by assigning `live.basename_index` at runtime in the
  `.scratch` driver; no filed byte was modified to produce the D2 evidence.

## 9. Reproduce

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
mkdir -p .scratch/o03
sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/o03/basename-couples-resolver.py
sha256sum .scratch/o03/basename-couples-resolver.py   # 43ce341f…
python3 -B .scratch/o03/basename-couples-resolver.py --selftest
python3 -B .scratch/o03/basename-couples-resolver.py --census
python3 -B .scratch/o03/diff2.py                      # D1/D1b/D1c/D2/D3 + part-level differential
python3 -B .scratch/o03/diff.py                       # D5 token-set differential + D6 census shape
```

Driver scripts are scratch-only; the evidence that matters is transcribed above with its
command output.
