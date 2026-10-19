- Seat: K01 | scout | claim O | date 2026-10-19 | baseline `7ceff59`

# K01 — resolver scout: policy classes, wrapped-field bytes, parse defect, fix surface

**Mission** (`reports/round-43/targets.json` seat `K01`): read the full
basename-couples policy (incl. §4 group alignment + §5 classes), the r42
successor doc, and the verbatim r39 landing it corrects; locate the wrapped
field's exact bytes (`corpus/knowledge/linguistics/phonetics-phonology.md:72-77`),
the r19 filed instrument's parse code that zeroes it, and the fix surface;
report the four policy classes and what a conformant tool must output.

**Method / boundary.** All measurements read-only, lane root, HEAD
`7ceff59a0216a8ea21ee43262d9fc72abf770cee`, `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`. This seat wrote only this file plus disposable
`.scratch/k01/`. No filed byte edited; no `reports/round-*/run-validation.py`
executed; no corpus byte staged; no git/network/install action.

**Headline.** Claim O's `before` sentence is **factually stale at HEAD**: a
durable resolver implementing the block/hyphen rules already exists at
`tools/harness/couples-reference-extractor.py`, tracked in `7ceff59` ("round-42:
… N6 successor extractor … O verified"), selftest 8/8 PASS, census over 223
entries. The claim is still partly alive — the landed tool violates the r43
contract in four measurable ways, including one confirmed over-capture edge its
own wave specified but did not implement. The round should **harden the existing
tool**, not mint a duplicate `basename-couples-resolver.py`.

## 0. Pointer corrections (dispatch vs files)

1. `reports/round-39/calib/basename-couples-policy-full.md` **does not exist**
   (`ls reports/round-39/calib/` → no such path). The full 263-line policy is at
   `reports/round-42/calib/basename-couples-policy-full.md`.
2. The verbatim r39 landing it corrects is
   `reports/round-39/calib/basename-couples-policy.md` — **107 lines / 5832
   bytes**, sha256 `105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`,
   ending mid-§6 at line 107. §6's fence and all of §7 are absent (r42 K01 D1e;
   r42 O12 §1 independently proved the prefix relation).
3. The r42 "full" document is **not a corrected policy**: `diff` of its bytes
   against r39 draft lines 41–303 is empty
   (`sed -n '41,303p' reports/round-39/calib/Ca03-basename-policy.md >
   .scratch/k01/r39-draft-body.md; diff -q …` → `prefix_relation_rc=0`, both 263
   lines). It restores §6/§7 but still states the defect rule in §1 (finding F3).

## 1. The four policy classes (as written)

Policy §2 (`reports/round-42/calib/basename-couples-policy-full.md:27-48`; same
text in the landed §2 at `reports/round-39/calib/basename-couples-policy.md:27-48`):

| class | rule | carried evidence |
|---|---|---|
| `direct` | Tier 1: `<entry dir>/<token>`, `<lane root>/<token>`, or `corpus/knowledge/<token>` is an existing file (`entry-audit.py:87-95`) | token only |
| `fallback` | Tier 1 failed **and** token is slash-free **and** exactly one file under `corpus/knowledge/*/*.md` carries that basename | **explicit mapping `token -> corpus-relative path`** (§2, §3.3) |
| `ambiguous` | Tier 1 failed, slash-free, **two or more** index hits | never resolved, never dropped; candidate paths must be named |
| `unresolved` | Tier 1 failed, slash-free, **zero** index hits | never dropped or guessed; named reason required (§3.1, D2/C12 row 2) |

Additional policy constraints:
- **§3.1** four classes reported separately, per entry and in totals; a "zero
  unresolved" claim must state the fallback count beside it.
- **§3.2** fallback never merged into path-resolved (direct) counts.
- **§3.3** every fallback mapping listed, not only counted.
- **§4** every fallback token must map into the partition named by the nearest
  preceding group label (`myth-symbol —`, `linguistics —`, …); mismatch is an
  `alignment` finding, not a resolution.
- **§5.1** slash-bearing tokens never enter the fallback; they stay `unresolved`.
- **§5.5** Tier 1 is never relaxed; a directly resolvable token stays `direct`.
- **§5.6** glob fragments (`-gate.md` from `*-gate.md`) are an extractor
  artifact: skip them or class them separately; **never count them as unresolved
  couples findings**.
- **§1 unit**: per-entry deduplicated, brace-expanded one level; `:NN` anchor not
  part of the token.

**The wrapped-field reading is not in the policy.** Both the landed and full
documents say §1: "the `- couples:` line … (**single physical line**; extraction
per `entry-audit.py:75`)" (`basename-couples-policy-full.md:16-17`). Block
extraction is Ca04 **D1** (`reports/round-39/calib/Ca04-verify.md:78-93`) and the
r42 tool's extension, not policy text. A tool that "implements the r39 policy"
literally reproduces the defect. This must be stated in any r43 census note.

## 2. Wrapped field — exact bytes and token identity

`corpus/knowledge/linguistics/phonetics-phonology.md:72-77`, sha256 of the file
`b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b`; six physical
lines, continuations indented two spaces, line 76 ends in `tone-`:

```
72  - couples: language (this file, core method); myth (divine/true names, taboo
73    naming, onomatopoeic etiologies); symbol (sound symbolism, name-shape,
74    bouba/kiki iconography); era (Neolithic bite → f/v, sound-change dating of
75    strata); costume (masks/mouthgear vs articulation, whistle & drum channels);
76    environment/anatomy design; prospective sibling files: sound-change.md, tone-
77    prosody.md, sound-symbolism.md, writing-systems.md
```

Token identity (4 named targets, measured `ls corpus/knowledge/*/`):

| token | exists? | policy class | r42 tool class |
|---|---|---|---|
| `sound-change.md` | ABSENT (zero index hits) | `unresolved` | `prospective` |
| `tone-prosody.md` | ABSENT (zero index hits) | `unresolved` | `prospective` |
| `sound-symbolism.md` | EXISTS (`corpus/knowledge/linguistics/`) | `direct` | `direct` |
| `writing-systems.md` | EXISTS (`corpus/knowledge/linguistics/`) | `direct` | `direct` |

Live tool output (command in §5): `wrapped=True tokens=4`, exactly those four
names. The hyphen join is load-bearing: `tone-` + `prosody.md` must become
`tone-prosody.md`; a space/newline join yields the phantom `prosody.md`, and
deleting the hyphen mints `toneprosody.md` (r42 K01 §4; r42 O05 F1/F6/F9).

## 3. The r19 parse defect (still live, by design)

`reports/round-19/audit/entry-audit.py`:

- `:75` — `m = re.search(r"^- couples:\s*(.*)$", text, re.M)`. With `re.M`, `$`
  stops at the first newline; the capture is one physical line.
- `:80-82` — `MDREF_RE.findall(line)` over that one line; `MDREF_RE` at `:31`;
  brace expansion `:34-42`.
- `:87-95` — Tier 1 only (entry dir → lane root → `corpus/knowledge`); no
  fallback.
- `:105,118-119,130` — the call site; `quality_bar` includes
  `and not unresolved` (`:130`), so a zeroed field silently removes tokens from
  the gate instead of failing them.

Measured today on the wrapped entry:

```
$ python3 -B reports/round-19/audit/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md
FAIL corpus/knowledge/linguistics/phonetics-phonology.md src=15/15 couples=0 unresolved=[] gap=False dec=True
TOTAL 0/1 clear the bar
R19_RC=2
```

`couples=0 unresolved=[]` is the signature: the field is reported **empty**, not
dangling. The r19 selftest (`:151-182`) has only a single-line fixture
(`:168-170`), so it stays green over the defect. The r19 file is filed bytes and
must not be edited; the durable successor is the fix surface.

## 4. The durable successor already exists — claim O `before` is stale

Evidence:

```
$ git log --oneline -6
7ceff59 round-42: NOT ADMITTED on C (O verified) — N6 successor extractor, 3 myth-symbol entries, collision ruling + overwrite restore
…
$ git log --oneline --follow -- tools/harness/couples-reference-extractor.py
7ceff59 round-42: NOT ADMITTED on C (O verified) — N6 successor extractor, …
$ git cat-file -e HEAD:tools/harness/couples-reference-extractor.py && echo TRACKED_AT_HEAD
TRACKED_AT_HEAD
$ sha256sum tools/harness/couples-reference-extractor.py
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1
  332 lines / 12223 bytes
```

Its selftest is green (8 checks) and its census reads the wrapped field whole:

```
$ python3 -B tools/harness/couples-reference-extractor.py --selftest
PASS wrapped positive 4/4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS wrapped positive heals soft wrap
PASS unwrapped regression
PASS over-capture trap (prose excluded) ['sound-symbolism.md']
PASS phantom negative: absent wrapped targets are visible, not zeroed
PASS N6 regression guard: single-line capture still yields 0 tokens
PASS N6 regression guard: block read yields 4 tokens
PASS glob fragment classified
SELFTEST_RC=0

$ python3 -B tools/harness/couples-reference-extractor.py --census
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
  misaligned: none
```

`reports/round-42/validation.json` records claim O `"passed": true`, leg `O1-O3`
green, and `reports/round-42/op/couples-extractor-census.json` is the filed
stdout above (4 lines). Therefore the r43 `before` phrases "no durable instrument
implements the r39 basename-couples policy" and "the only resolver that ever ran
… lives in ephemeral `.scratch`" are contradicted by bytes at HEAD.

**The I-C05 conflation.** r39 I-C05 is a **source-pointer/citation resolver**
(`reports/round-39/cov/C05-audit.md:30`: "I-C05 (resolver …) … fence-run …
attached/bare/detached citations; out-of-range; dangling"), not a couples
resolver. Queue row `r39-ic05-resolver-durability`
(`reports/round-40/op/defect-queue-v2.json:382`) is about that citation
instrument. It is a different defect and must not be cited as the missing
couples resolver's predecessor.

## 5. What is still wrong with the landed tool (r43-valid work)

Conformance against claim O's `after_required`
(`reports/round-43/claims.json:28`), measured:

| requirement | verdict | evidence |
|---|---|---|
| durable tool under `tools/harness/` | **PASS** | tracked `7ceff59`, 332 lines, sha `d8d23a26…` |
| `--selftest` green with wrapped positive | **PASS** | 4/4 token identity, hyphen healed |
| synthetic **phantom** negative | **PASS (re-labelled)** | phantom present but classed `prospective`, not policy `unresolved` (`selftest:268-279`) |
| synthetic **ambiguous** negative | **FAIL — absent** | no ambiguous control in `selftest:242-295`; live basename index has **223 entries / 0 duplicate basenames**, so `ambiguous` is untested live too (`.scratch/k01/overcapture.py` output) |
| wrapped field reads 4/4 | **PASS** | `paths` output, §2 table |
| four policy classes separately, per entry and totals | **PARTIAL/FAIL** | census emits **six** buckets (`census:189-191`); `unresolved=2` hides 8 raw policy-unresolved (2 + 5 `prospective` + 1 `glob-fragment`); no four-class reconciliation is printed |
| every fallback mapping listed | **FAIL in census** | `--census` prints only counts (`main:306-319`); the 166 mappings appear only in per-entry `paths` mode (`resolve_entry:175-182`) |
| unresolved/ambiguous carry a named reason or mapping | **FAIL** | token record has `class`/`mapping`/`group`/`alignment`/`documented`, no `reason` and no carrier line (`resolve_entry:175-182`) |
| census filed at `reports/round-43/calib/` | **NOT YET** | tool has no writer/`--json`/`--out`; r42 artifact is hand-redirected stdout (4 lines) |
| zero tokens dropped/guessed | **PASS on live; latent FAIL** | 2730 refs = 2556+166+2+5+1; but see F5 over-capture |

### F5 — confirmed over-capture: blank line then indented prose

`couples_block` **skips** blank lines instead of terminating at them
(`tools/harness/couples-reference-extractor.py:64-65`,
`if not following.strip(): continue`). Its own docstring rationalizes this as
"blank-separated continuation still joins" (`:51-57`), but r42's controls and
trap audit both require the opposite:

- `reports/round-42/op/O02-controls.md:27` — control 4
  `field-boundary-negative`: "single-line field, blank line, body prose naming
  three `.md` files → only the field's token; all three prose names absent."
- `reports/round-42/op/O02-controls.md:90-105` — reference `block_field_raw`
  breaks on `if not l.strip()`.
- `reports/round-42/op/O05-traps.md:190-196` — "The fix's block parser should
  stop at a blank line, not skip it"; fixture F15, sha `302dad7e97ce4305`.
  O05's §7 repeats it as an integrator obligation (`:307-308`).

Reproduced against the landed tool:

```
$ python3 -B .scratch/k01/overcapture.py
block parts: ['language — `writing-systems.md`', 'This indented paragraph after a BLANK line mentions `sound-change.md` in prose.']
joined: 'language — `writing-systems.md` This indented paragraph after a BLANK line mentions `sound-change.md` in prose.'
tokens: ['sound-change.md', 'writing-systems.md']
```

The prose token is swallowed. The live corpus has 0 such fields today (so the
current 2730 figure is not wrong), but the tool's selftest does not include the
discriminating fixture — its `OVER_CAPTURE_TRAP` (`:231-239`) uses **non-indented**
prose, which is stopped by `INDENT_RE`. The r42 gate is blind to this: the O2
leg only greps the selftest tail for `"N6 regression guard"`
(`reports/round-42/run-validation.py:94-101`), and no r42 verifier ran F15
against the landed tool. This is the same shape as the r39 truncation: a green
gate over an unexercised rule.

### F6 — policy text still prescribes the defect

The restored §6 recipe in the 263-line successor doc still uses the single-line
`couples_field()` (`reports/round-42/calib/basename-couples-policy-full.md:148-150`),
and Parts 1/2 call it (`:170,197`). Anyone reproducing the policy's arithmetic
today gets the **single-line** census (`2607 -> 2435/166/0/6` at 220 entries),
not the corrected one. r43's O03 must not use §6 as the census recipe. A
successor note is needed to record that §1 single-line + §6's recipe are
superseded by block extraction / hyphen-retained join (filed r39 bytes cannot be
edited; r42 full doc is a filed successor but still carries the old text).

## 6. What a conformant tool must output

The four classes are the reporting spine; sub-dispositions are allowed only if
reconciled to them. Minimum contract:

```json
{
  "entries": 223, "refs": 2730,
  "totals": {"direct": 2556, "fallback": 166, "ambiguous": 0, "unresolved": 8},
  "subclasses": {"unresolved_glob_fragment": 1, "unresolved_declared_prospective": 5,
                  "unresolved_true": 2},
  "wrapped_fields": [{"path": "corpus/knowledge/linguistics/phonetics-phonology.md",
                       "parts": 6, "tokens": ["sound-change.md", "tone-prosody.md",
                                              "sound-symbolism.md", "writing-systems.md"]}],
  "entries_detail": [{
    "path": "…", "wrapped": false,
    "tokens": [{"token": "…", "class": "direct|fallback|ambiguous|unresolved",
                 "tier": 1, "mapping": "corpus/…/x.md|null",
                 "reason": "unique-basename|zero-index-hits|multi-index-hits|slash-bearing|glob-fragment|declared-prospective",
                 "carrier_line": 37, "group": "linguistics|null",
                 "alignment": "ok|MISALIGNED|null",
                 "disposition": "blocker|documented|non-blocker"}]}],
  "fallback_mappings": [{"token": "…", "path": "corpus/…/x.md", "entry": "…", "group": "…", "alignment": "ok"}],
  "ambiguous": [{"token": "…", "candidates": ["corpus/…/a.md", "corpus/…/b.md"], "carriers": ["…:NN"]}],
  "unresolved": [{"token": "…", "count": 2, "carriers": ["…:14", "…:16"], "reason": "…"}]
}
```

Rules the artifact must satisfy:
1. `direct + fallback + ambiguous + unresolved == refs` (2730 at HEAD). The six
   buckets must reconcile into these four, not replace them.
2. Every fallback row carries `token -> path` (§3.3), and `alignment` against
   the nearest preceding group label (§4).
3. Every unresolved/ambiguous row carries a **named reason** and its carrier
   `entry:line`; none dropped (§3.1, D2/C12 row 2). A `(to-verify` marker on the
   same line makes it `documented`/non-blocker, otherwise `blocker`
   (`reports/round-35/cov/C12-audit-runbook.md:37`).
4. Glob fragments are reported separately and excluded from the finding count
   (§5.6). Declared-prospective seeds are an r42 extension (`resolve_entry:159`)
   and must be shown as a sub-reason of `unresolved`, not a fifth policy class.
5. Selftest must include: wrapped positive 4/4 with **token identity** (not just
   count), hyphen-heal (`tone-prosody.md` present, `prosody.md` absent),
   phantom negative (0 hits → `unresolved` with reason), **ambiguous synthetic**
   (two files same basename in two partition dirs → `ambiguous`, both candidates
   listed), direct positive, unwrapped regression, and the **blank-line
   field-boundary negative** (§5 F5).

## 7. Fix surface — exact lines in the durable tool

`tools/harness/couples-reference-extractor.py` (sha `d8d23a26…`):

| change | line(s) | current | required |
|---|---|---|---|
| blank-line termination | `:64-65` | `if not following.strip(): continue` | `break` (per O02 control 4, O05 F15) |
| four-class totals + reconciliation | `:189-191` | six keys in `totals` | four policy keys + `subclasses`, assert sum == refs |
| per-token reason + carrier | `:175-182` | no `reason`, no line | add `reason`, `carrier_line`, `disposition` |
| fallback mapping list | `:186-210` | local `unresolved`/`misaligned` only | collect `fallback_mappings`, `ambiguous` candidates |
| census artifact | `:298-328` (`main`) | stdout only | `--json PATH` / `--out DIR`; write `reports/round-43/calib/census-r43.json` + `.md` |
| ambiguous selftest | `:242-295` | none | synthetic two-partition fixture, both candidates asserted |
| blank-line selftest | `:231-239` | non-indented prose only | blank line + indented prose naming a `.md`; assert absent |
| policy reconciliation note | — | docstring `:8-13` names the r39 policy as implemented | state §1/§6 are superseded by D1 block extraction; cite the successor note |

Do **not** mint `tools/harness/basename-couples-resolver.py` as a second live
resolver: the r43 claim allows a "wave-named equivalent", and a second copy
re-creates the D1d divergence problem (r42 K01 §6: three filed instruments
already carry the single-line parse). Either patch the existing path or land an
explicit alias/supersession record.

## 8. Recommendation to the integrator

Re-scope claim O's `before`/`after_required` before execution:

- **Before:** "the r42 durable extractor exists and is green, but its census
  fails the r39 four-class reporting contract: six buckets with no
  reconciliation, no fallback-mapping list, no per-token reason/carrier, no
  ambiguous control, and a confirmed blank-line over-capture that its own r42
  controls (O02 #4) and trap audit (O05 F15) required but the landed code does
  not implement."
- **After:** "the same tool emits the §6 contract above, selftest adds ambiguous
  + blank-line controls, census-43 is filed, and a successor note records that
  policy §1/§6 single-line extraction is superseded by block/hyphen-retained
  extraction."
- Keep the counting command `python3 tools/harness/couples-reference-extractor.py
  --selftest` and `--census`; add `--json reports/round-43/calib/census-r43.json`.
- Do not use the policy's §6 script for the census (F6); it reads 0/4 on the
  wrapped field and 2607/2435/166/0/6 at 220 entries, not the corrected
  `2730 = 2556 + 166 + 0 + 8` (223 entries, with 5 prospective + 1 glob
  sub-disposition).

## Owed / to-verify

- **Integrator:** amend the r43 O claim text (stale before; I-C05 conflation).
  Without this, the round will "build" a tool that already exists and may
  overwrite or fork it.
- **O01/O02/O06 seats:** patch the existing path, not a new resolver; land the
  ambiguous and blank-line controls; add the reason/carrier columns.
- **O03:** predict against 223 entries and the four-class reconciliation
  `2556 / 166 / 0 / 8` (raw), not the r39 policy's 212-entry 2504 figure and not
  its single-line 2607 figure.
- **Policy owner:** successor note for D1 (block extraction) and D2 (C12 row 2),
  because the filed r39 policy is truncated and the r42 full doc still prescribes
  single-line extraction. This seat does not edit either.
- **to-verify:** whether the r42 tool's `prospective` class is allowed to carry
  5 tokens out of the policy's `unresolved` count without an explicit successor
  policy clause; this seat recommends reporting it as a sub-reason and keeping
  the four-class total at 8.
- **to-verify:** the r42 tool's docstring says "measured: 0 such cases" for
  blank-separated continuations; this seat confirms 0 live today but did not
  re-scan every field for blank-line-adjacent indented prose.

## Citations

- Claim/seat: `reports/round-43/claims.json:24-34` (claim O),
  `reports/round-43/targets.json:13` (K01 mission).
- Four classes: `reports/round-42/calib/basename-couples-policy-full.md:27-48`;
  landed §2 `reports/round-39/calib/basename-couples-policy.md:27-48`.
- Reporting rules §3: full doc `:50-58`; §4 `:60-69`; §5.1 `:73-81`; §5.6
  `:97-102`; §6 recipe `:104-218` (single-line at `:148-150`).
- Landed r39 policy: 107 lines / 5832 bytes, sha `105dfff6…`; §6 lead-in only
  `:104-107`. Prefix relation: `sed -n '41,303p' Ca03-basename-policy.md` ==
  `reports/round-42/calib/basename-couples-policy-full.md` (263 lines, diff rc 0).
- Wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (blank `:78`, `## 1.` heading `:79`), sha `b4f9b003…`.
- r19 defect: `reports/round-19/audit/entry-audit.py:31,34-42,74-96`
  (capture `:75`, findall `:80-82`, Tier 1 `:87-95`, gate conjunction `:130`,
  selftest `:151-182` with single-line fixture `:168-170`).
- Durable successor: `tools/harness/couples-reference-extractor.py` (332 lines,
  sha `d8d23a26…`), tracked in `7ceff59`; block `:50-73`, join `:76-92`,
  classify `:134-150`, record `:153-183`, census `:186-210`, selftest `:242-295`,
  CLI `:298-328`.
- r42 acceptance: `reports/round-42/validation.json` (claim O passed, legs
  O1-O3 green); `reports/round-42/op/couples-extractor-census.json` (4-line
  stdout artifact); `reports/round-42/run-validation.py:94-101` (gate tests
  selftest tail + live entry only).
- r42 controls/traps: `reports/round-42/op/O02-controls.md:27,90-105`;
  `reports/round-42/op/O05-traps.md:142,190-196,307-308`;
  `reports/round-42/scout/K01-n6-scout.md:73-101,131-158,160-216`.
- Ca04 D1/D2: `reports/round-39/calib/Ca04-verify.md:78-105,94-101`.
- Queue rows: `reports/round-40/op/defect-queue-v2.json`
  `r39-basename-successor-instrument`, `r39-ic05-resolver-durability` (:382),
  `N6-couples-extractor-wrapped-field`.
- C12 disposition leg: `reports/round-35/cov/C12-audit-runbook.md:37`.
- Command outputs (this seat, 2026-10-19, HEAD `7ceff59`, read-only):
  `--selftest` 8 PASS rc 0; `--census` `223/2730 -> 2556/166/2/5/1`, wrapped 1;
  `paths` on phonetics → 4 tokens (2 direct, 2 prospective); `paths` on
  sacred-kingship → 36 tokens with 15 fallback mappings printed; r19 gate →
  `couples=0`, `TOTAL 0/1`, rc 2; over-capture fixture → prose token captured;
  live basename index 223 entries / 0 duplicate basenames; `git log --follow` →
  `7ceff59`; `git cat-file -e HEAD:…` → TRACKED_AT_HEAD.
