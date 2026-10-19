- Seat: O04 | executor | claim O | date 2026-10-19 | baseline `c9f4eaa`
- Status: spec + measured parity evidence. This seat landed only this file.

# O04 — Witness demotion: `couples-reference-extractor.py` -> N6 regression witness

**Verdict.** The demotion is a **record-level act, not a byte edit**. The witness
keeps its r42 bytes (`d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`,
332 lines, tracked blob `1ded489bbb2bb90b3ad883ec0cd052822d870225`, mode 100644,
`git status --porcelain -- tools/harness/` empty at `2026-10-19T17:23Z`). The
successor body already carries the witness sentence it needs
(`reports/round-43/op/O09-scribe.md:362-364`), and this seat measured the
six-bucket-vs-four-class parity over all 223 entries: **2730/2730 tokens compared,
0 unexplained differences** (§5). The demotion is completed by three successor
records (§3) plus the O07 parity receipt (§4).

This is the lane's standard successor-record pattern: filed bytes stay as filed,
the correction is a new record (`corpus/lessons/round-28.md:96`, "filed bytes are
read-only; the correction is a new revision file").

## 1. Measured state of the witness (before any r44 record)

| property | value | command / source |
|---|---|---|
| path | `tools/harness/couples-reference-extractor.py` | — |
| sha256 | `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1` | `sha256sum` |
| size | 332 lines, 12223 bytes | `wc -l`; `ls -l` |
| tracked | blob `1ded489b…`, mode 100644 | `git ls-files -s` |
| selftest | 8/8 PASS, exit 0 | `python3 -B tools/harness/couples-reference-extractor.py --selftest` |
| census | `entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1` | `--census` |
| wrapped fields | 1 (`corpus/knowledge/linguistics/phonetics-phonology.md`) | `--census` |
| unresolved distinct | 1 (`../linguistics/phonology-sanity.md` x2) | `--census` |
| misaligned | none | `--census` |

The witness's own bytes say it is a **successor**: `:2` reads `"""Successor
couples-reference resolver + census (N6 fix; r42 claim O).` That sentence is
historically true (it succeeded the r19/r27 single-line capture) and is **not
amended**. After r44 it must be read as r42 status, not current authority; the
demotion record states this explicitly (§3.3). Do not try to reconcile it by
editing the file.

**What the witness actually guards, still live.** Its selftest re-reads the live
wrapped field, not a frozen fixture:

- `tools/harness/couples-reference-extractor.py:286-289` — `N6 regression guard:
  single-line capture still yields 0 tokens` and `block read yields 4 tokens`.
- `tools/harness/couples-reference-extractor.py:64-65` — the blank-line
  `continue` that over-captures blank-separated indented prose (the authority
  replaces it with a break; §6).
- `tools/harness/couples-reference-extractor.py:142-146` — basename-hit
  fallback/ambiguous tests run **before** the glob test; the authority reverses
  that order (§6).

**Live consumers.** Only filed runners invoke it: `reports/round-42/run-validation.py:94-99`
and `reports/round-43/run-validation.py:64-66`. Both are filed and uneditable;
because the witness bytes do not move, they keep passing. Nothing under `tools/`
imports it (`rg -n "couples-reference-extractor" tools/ templates/` -> no hits).

## 2. What "witness-only" means (binding rule)

Five clauses; each is checkable, not rhetorical.

| # | clause | check |
|---|---|---|
| W1 | **Single authority.** Policy census counts are cited from `tools/harness/basename-couples-resolver.py` / `reports/round-44/calib/couples-census-r44.json` only. | any r44+ doc citing a census names the authority |
| W2 | **Not imported, not shelled out.** The authority must not `import`, `exec`, or `subprocess` the witness. | measured: the only occurrence of the witness path in the authority is its docstring line 8; the authority ran 27/27 + census from `.scratch/o04-clean/` with **no `tools/` tree and no witness present** |
| W3 | **Bytes frozen.** Witness sha256 stays `d8d23a26…`; the digest is pinned in the census artifact, the parity receipt, and the LOG entry. | `sha256sum` at every later round; a mismatch is a detectable edit |
| W4 | **Live witness, not a museum copy.** Its selftest keeps the N6 guard on live bytes and its six buckets are an independent cross-check folded into the authority. | `--selftest` 8/8; O07 parity re-run |
| W5 | **Vocabulary rule.** The witness's `prospective` and `glob-fragment` are **witness buckets**, not policy classes. Any quotation folds `prospective -> unresolved` (a disposition of the unresolved class) and treats `glob-fragment` as an artifact. | parity receipt fold table; never write "five/six classes" as the policy |

Why keep it running at all: it is the only instrument that re-checks the exact
N6 defect shape on the live field, and it is a second, independently-authored
parser for the parity cross-check. Two implementations that *agree* are evidence;
two that share an author are not (the lane's r27/r28 lesson). The authority and
witness are one-author-apart in time (r42 vs r43 body), not copied at run time.

## 3. The demotion records (exact insertions)

### 3.1 Already present in the authority body — no edit

`reports/round-43/op/O09-scribe.md:362-364` (body lines 7-9), preserved verbatim
by the byte-exact landing:

```
Predecessor (NOT edited, NOT imported): tools/harness/
couples-reference-extractor.py (r42, sha256 d8d23a26...), which remains the N6
regression witness.
```

This is the document-level statement inside the authority. The records below make
it externally discoverable without touching either tool.

### 3.2 Census artifact block — merge into O06's ONE artifact

O06's filed shape (`reports/round-44/op/O06-census-artifact.md` §5) already nests
the witness under `tool`, not at top level. Keep that shape; the demotion needs
these fields present through application. Target artifact:
`reports/round-44/calib/couples-census-r44.json` (O06's name; do not file a
second census under another name).

```json
"tool": {
  "path": "tools/harness/basename-couples-resolver.py",
  "sha256": "43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64",
  "source": "reports/round-43/op/O09-scribe.md:356-870",
  "selftest": "27/27 PASS",
  "role": "single census authority",
  "body_round": 43,
  "witness": {
    "path": "tools/harness/couples-reference-extractor.py",
    "sha256": "d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1",
    "selftest": "8/8 PASS",
    "role": "N6 regression witness only; bytes untouched; not the census authority; not imported",
    "not_authority": true,
    "not_imported": true,
    "bytes_untouched": true,
    "buckets": {
      "direct": 2556, "fallback": 166, "ambiguous": 0,
      "unresolved": 2, "prospective": 5, "glob-fragment": 1
    },
    "fold": {"prospective": "unresolved", "glob-fragment": "artifact"}
  },
  "parity": {
    "receipt": "reports/round-44/op/O07-parity.md",
    "tokens_compared": 2730,
    "unexplained_differences": 0,
    "fallback_mapping_identity": "166/166 occurrences, 50 distinct"
  }
}
```

O06's current `tool.witness` carries path, sha256 and role; this block adds the
selftest, buckets, fold and parity fields that make the demotion checkable. O06
also notes the body hardcodes `"round": 43` (`reports/round-43/op/O09-scribe.md:816`);
record `tool.body_round: 43` and the artifact's top-level `round: 44` rather than
editing the tool, so the landed digest stays `43ce341f…`. The tool's self-hash in
its payload is the landed digest; leave it alone.

### 3.3 LOG.md round-44 entry — append-only, integrator-owned

Add to the O bullet (the exact wording is the integrator's to place, but the
facts and digests must survive):

```
`couples-reference-extractor.py` (sha256 `d8d23a26…`, 332 lines) is demoted by
record to the **N6 regression witness** — bytes untouched, not imported, not the
census authority. `tools/harness/basename-couples-resolver.py` (sha256
`43ce341f…`, selftest 27/27) is the single census authority; parity receipt
`reports/round-44/op/O07-parity.md` reconciles 2730/2730 tokens with 0
unexplained differences (`prospective=5` is a disposition of `unresolved=7`;
`glob-fragment=1` is an artifact). The witness's `:2` self-description is r42
status, not current authority.
```

Do not edit the r42/r43 LOG bullets or the SCORECARD r42/r43 rows; they are
history and remain true as of their stamps.

### 3.4 Instrument index note — optional, recommended

`SKILL.md:446-454` is the lane's only instrument index (a supporting-surface
table). Neither couples tool is listed there today. If the integrator wants the
demotion discoverable from the index, append these two rows after `r8_checks.py`:

```markdown
| `tools/harness/basename-couples-resolver.py` | single census authority for the basename-couples policy: four classes `direct/fallback/ambiguous/unresolved` plus the `glob-fragment` artifact; every fallback mapping listed, every unresolved/ambiguous row carries a named disposition; `--census --json` is the filed-artifact source; read-only | module docstring §§Modes,Policy; `reports/round-44/calib/couples-census-r44.json`; body `reports/round-43/op/O09-scribe.md:356-870` |
| `tools/harness/couples-reference-extractor.py` | **N6 regression witness only** — bytes frozen at r42 (`d8d23a26…`), not imported, not the census authority; its selftest holds the live N6 guard and its six buckets fold `prospective → unresolved` in the parity receipt | module docstring; `reports/round-44/op/O07-parity.md`; `reports/round-44/calib/couples-census-r44.json` |
```

This is **not load-bearing**: the demotion is complete under §3.1-§3.3 without it.
Do not create `tools/harness/README.md`; that would be a new surface, not an index.

### 3.5 O07 parity receipt — separate report, not a second census artifact

Target: `reports/round-44/op/O07-parity.md`. Shape in §4. "ONE census artifact"
in the claim means one machine census at `calib/`; the parity receipt is the
report that certifies the demotion and may embed a fenced JSON block. Do not file
a second census JSON under `calib/`.

## 4. O07 parity-receipt shape

The receipt must prove **token identity**, not only totals. The r42 lesson is
explicit: "the census totals cannot distinguish a correct fix from a mangling
one; only the token *identity* can"
(`reports/round-42/op/O06-receipt.md:88,96`, finding F-O06-2). A totals-only
parity would pass a witness that renamed `tone-prosody.md` to `prosody.md`.

Fenced block to embed in `op/O07-parity.md` (values marked `MEASURED` are this
seat's run at `2026-10-19T17:23Z`; O07 must re-derive them independently and
either reproduce or file the divergence):

```json
{
  "schema": "kotodama-couples-parity-v1",
  "round": 44,
  "baseline_commit": "c9f4eaa",
  "observed_at_utc": "<O07 stamp>",
  "input": {
    "entries": 223,
    "refs": 2730,
    "unit": "per-entry dedup, brace-expanded .md tokens",
    "glob": "corpus/knowledge/*/*.md"
  },
  "authority": {
    "path": "tools/harness/basename-couples-resolver.py",
    "sha256": "43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64",
    "selftest": "27/27",
    "census_schema": "kotodama-couples-census-v3",
    "four_class_totals": {"direct": 2556, "fallback": 166, "ambiguous": 0, "unresolved": 7},
    "artifact_totals": {"glob-fragment": 1},
    "conservation": true,
    "fallback_mappings_distinct": 50,
    "fallback_occurrences": 166,
    "disposition_counts": {"declared-prospective-seed": 5, "dangling-reference": 2, "extractor-artifact": 1}
  },
  "witness": {
    "path": "tools/harness/couples-reference-extractor.py",
    "sha256": "d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1",
    "selftest": "8/8",
    "role": "N6 regression witness only",
    "buckets": {"direct": 2556, "fallback": 166, "ambiguous": 0, "unresolved": 2, "prospective": 5, "glob-fragment": 1}
  },
  "reconciliation": {
    "entries_both": 223,
    "path_sets_identical": true,
    "wrapped_flags_identical": true,
    "tokens_compared": 2730,
    "token_set_mismatches": 0,
    "class_fold_mismatches": 0,
    "fallback_mapping_mismatches": 0,
    "fold_counts": {
      "direct->direct": 2556,
      "fallback->fallback": 166,
      "unresolved->unresolved": 2,
      "prospective->unresolved": 5,
      "glob-fragment->glob-fragment": 1
    },
    "unexplained_differences": 0
  },
  "latent_only_differences": [
    "blank-line terminator: witness continues past a blank line (:64-65); authority breaks unless the previous part is a hyphen soft-wrap. Live blank-separated continuations = 0; control S7c (O09:768).",
    "glob precedence: witness tests basename hits before glob (:142-146); authority tests glob first (O09:504 before :509). Live glob token has zero basename hits, so live effect = 0; control S8b (O09:777).",
    "ambiguous exposure: authority exposes the class with controls S3a/S3b (O09:725-726); witness has the bucket, live count 0 in both.",
    "prospective scope: witness flags the whole entry if the marker appears anywhere (:159); authority assigns the disposition positionally after the marker (O09:523,540). Live effect = 0 (all 5 prospective tokens follow their marker).",
    "disposition reasons: authority names a reason per unresolved/ambiguous/artifact row (O09:555-573); witness names none. No count effect.",
    "serialization: authority emits JSON v3 (O09:815-819); witness emits text only."
  ],
  "commands": [
    "python3 -B tools/harness/basename-couples-resolver.py --selftest",
    "python3 -B tools/harness/basename-couples-resolver.py --census --json",
    "python3 -B tools/harness/basename-couples-resolver.py --json $(find corpus/knowledge -name '*.md' | sort)",
    "python3 -B tools/harness/couples-reference-extractor.py --selftest",
    "python3 -B tools/harness/couples-reference-extractor.py --census",
    "python3 -B tools/harness/couples-reference-extractor.py $(find corpus/knowledge -name '*.md' | sort)"
  ],
  "verdict": "PARITY"
}
```

Receipt rules:

1. Run the authority from a scratch directory **with no `corpus/` above it**
   (`.scratch/o04-clean/` here). A directory containing a repo mirror resolves
   the authority's root discovery to the shadow corpus; the first attempt in
   `.scratch/o04/` did exactly that (see §9).
2. Quote both tool digests; a parity claim without the witness digest is not a
   demotion record.
3. Compare per-entry token **sets**, then classes under the fold, then fallback
   **mappings** token-by-token. Totals alone are insufficient.
4. `unexplained_differences` counts path-set, token-set, class-fold, mapping and
   wrapped-flag mismatches. It must be 0, not "0 by construction".

## 5. Measured parity (this seat's run, `2026-10-19T17:2xZ`)

Authority: body extracted to `.scratch/o04-clean/basename-couples-resolver.py`,
sha256 `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`,
515 lines, `SELFTEST OK: 27/27 controls`, `--census` exit 0.
Witness: the tracked file, unchanged, 8/8, exit 0.
Comparison: `.scratch/o04-clean/parity-compare-clean.py` (111 lines of JSON
output, sha256 `67de8483d1a5cc6122feb221e90e3c90d7034acc478346af8e691ae814f83d0f`).

```
tokens_compared                 2730
path_sets_identical             true   (223/223)
wrapped_flags_identical         true
token_set_mismatches            0
class_fold_mismatches           0
fallback_mapping_mismatches     0
unexplained_differences         0

fold_counts
  direct        -> direct          2556
  fallback      -> fallback         166
  unresolved    -> unresolved         2
  prospective   -> unresolved         5
  glob-fragment -> glob-fragment      1
```

Disposition leg (authority): 5 `declared-prospective-seed` + 2
`dangling-reference` = 7 unresolved rows, each with a reason; 1
`extractor-artifact` row (`-gate.md`); 0 ambiguous rows. Fallback mappings:
50 distinct / 166 occurrences, identical between tools (0 mismatches).

Worked example — the live wrapped field
(`corpus/knowledge/linguistics/phonetics-phonology.md`), same 4 tokens:

| token | witness bucket | authority class + disposition |
|---|---|---|
| `sound-change.md` | `prospective` | `unresolved` / `declared-prospective-seed` |
| `tone-prosody.md` | `prospective` | `unresolved` / `declared-prospective-seed` |
| `sound-symbolism.md` | `direct` | `direct` |
| `writing-systems.md` | `direct` | `direct` |

This is the subclass separation in one row: the witness's `prospective` is not a
fifth policy class; it is the authority's unresolved class carrying the
declared-prospective disposition.

## 6. Latent-only differences and why their live effect is zero

| difference | witness | authority | live effect | control |
|---|---|---|---|---|
| blank line inside a wrapped field | `continue` (`:64-65`) -> over-captures indented prose | break unless hyphen soft-wrap (`O09:396-421`) | 0 blank-separated continuations in the live corpus (r42 O06 §2.5) | `S7c` (`O09:768`) |
| glob vs basename order | basename hits first (`:142-146`) | glob first (`O09:504` before `:509`) | 0: the one glob token `-gate.md` has zero basename hits (`ls corpus/knowledge/*/-gate.md` -> no match) | `S8b` (`O09:777`) |
| ambiguous class | bucket exists, no dedicated control in r42 | class + `S3a`/`S3b` controls | 0 both | `O09:725-726` |
| prospective scope | entry-global flag (`:159`) | positional disposition (`O09:523,540`) | 0: all 5 prospective tokens follow their marker | `S1f`, `S2c` |
| per-token reason | none | every unresolved/ambiguous/artifact row reasoned | count-neutral | disposition table |
| output shape | text | JSON v3 | — | `O09:815-819` |

The receipt records these as `latent_only_differences`, not as parity failures:
they are the documented semantic hardening of the successor, and each has a
synthetic control. The live corpus cannot distinguish them, which is exactly why
the controls must be cited rather than the totals.

Live glob token provenance: `corpus/knowledge/verification/gate-frozen-run-standard.md:15`
names `corpus/knowledge/verification/*-gate.md`; the extracted token is
`-gate.md`; no file with that basename exists, so the witness would have reached
its glob branch anyway. The precedence fix is real but latent today.

## 7. Negative controls that prove the demotion is not just wording

1. **Standalone authority.** The authority ran 27/27 and produced the 223/2730
   census from `.scratch/o04-clean/`, which contains no `tools/` tree and no
   witness file. A hidden import or shell-out would fail there.
2. **Source grep.** In the authority, `couples-reference-extractor` occurs only
   in the docstring (line 8); no `subprocess`, `importlib`, or `exec` path
   touches it.
3. **Digest pin.** Witness sha256 `d8d23a26…` is recorded in the census artifact,
   the parity receipt and the LOG entry. Any later in-place edit is a detectable
   digest mismatch.
4. **Git tracking.** `git ls-files -s` -> blob `1ded489b…`, mode 100644;
   `git status --porcelain -- tools/harness/` empty. The witness is tracked and
   unmodified at the baseline.
5. **Filed-runner compatibility.** `reports/round-42/run-validation.py:94-99` and
   `reports/round-43/run-validation.py:64-66` still run the witness; since its
   bytes do not move, those historical receipts remain reproducible.
6. **No second authority path.** The O09 body lands only at
   `tools/harness/basename-couples-resolver.py` (`reports/round-43/op/O09-scribe.md`
   §6 step 1); it is not copied to a second path.

## 8. Anti-patterns (do not)

- Do not edit the witness to add "witness-only" to its docstring; that breaks the
  r42/r43 filed runners' digest expectations and violates filed-byte discipline.
- Do not rename, copy, or symlink the witness.
- Do not land the O09 body at a second path "for backup"; the claim names one
  authority path.
- Do not import/shell out to the witness from the authority (the body already
  says NOT imported).
- Do not create `tools/harness/README.md` as an index; `SKILL.md:446-454` is the
  existing index.
- Do not quote the witness's six buckets as "the census"; fold
  `prospective -> unresolved` and keep `glob-fragment` as an artifact.
- Do not edit the authority's hardcoded `round: 43`; wrap it in the artifact
  (`round: 44`, `tool_body_round: 43`) so the tool digest stays `43ce341f…`.
- Do not file a second census JSON under `calib/`; one artifact, one parity
  report (`op/O07-parity.md`).

## 9. Cross-seat notes

- **O07:** use §4's shape and re-derive §5 independently; the receipt is
  load-bearing for the demotion. Run the authority from a clean scratch
  directory. Warning: `.scratch/o04/` already contained a full repo mirror from
  earlier work; the first authority run there resolved `LANE` to that shadow
  corpus (`path_sets_identical` failed against the live witness because the
  authority relativized paths to the shadow root). The clean rerun in
  `.scratch/o04-clean/` fixed it. Do not reuse a scratch dir containing `corpus/`.
- **O06:** merge §3.2's block into the one census artifact; the tool's own JSON
  says `round: 43`, so the wrapper fields are required.
- **O01:** landing must be byte-exact; the expected digest is `43ce341f…`, and
  the witness sentence at `O09:362-364` is part of the landed body.
- **O08:** the negative proof should assert the witness digest, the git blob,
  the absence of a second resolver path, and no corpus write.
- **O05:** two untested trap combinations worth a vector: a slash-bearing glob
  token (witness: unresolved; authority: artifact) and a blank line ending in a
  hyphen soft-wrap (witness: continues; authority: continues only if the next
  line is indented). Neither occurs live.
- **S01 / LOG:** §3.3 is the sentence to carry; keep the two digests.
- **Ca (freshness gate):** the witness digest is a cheap freshness anchor for the
  O claim — a `before` asserting "no resolver" is false while
  `basename-couples-resolver.py` exists and is green.

## 10. Reproducibility

Environment for every command: `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`, run from the lane root.

```
# witness (unchanged)
sha256sum tools/harness/couples-reference-extractor.py
git ls-files -s tools/harness/couples-reference-extractor.py
python3 -B tools/harness/couples-reference-extractor.py --selftest
python3 -B tools/harness/couples-reference-extractor.py --census

# authority (from the body; clean scratch, no corpus above it)
sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/o04-clean/basename-couples-resolver.py
sha256sum .scratch/o04-clean/basename-couples-resolver.py
python3 -B .scratch/o04-clean/basename-couples-resolver.py --selftest
python3 -B .scratch/o04-clean/basename-couples-resolver.py --census --json
python3 -B .scratch/o04-clean/basename-couples-resolver.py --json $(find corpus/knowledge -name '*.md' | sort)

# per-token parity
python3 -B tools/harness/couples-reference-extractor.py $(find corpus/knowledge -name '*.md' | sort)
python3 -B .scratch/o04-clean/parity-compare-clean.py
```

Scratch evidence (ephemeral; the durable record is the commands + quoted outputs
above): `.scratch/o04-clean/authority-census.json`
(`0b7babd7…`), `witness-census.txt` (`e94f3a4e…`), `parity-measure.json`
(`67de8483…`).

## 11. Residual / `to-verify`

- Landed authority digest must equal `43ce341f…` after integration; `to-verify`
  until O01/O08 measure the landed byte.
- Whether the integrator adopts the optional SKILL index rows (§3.4) is their
  call; the demotion does not depend on it.
- The authority's JSON `round: 43` is intentional byte-exact carry-over; the
  artifact wrapper must state both rounds or the filed census will look
  mis-dated.
- The slash-bearing-glob trap (§9, O05) is unmeasured live (0 occurrences);
  marked for a synthetic control, not a defect.

## 12. Status

Claim O demotion specification complete and measured: witness state pinned,
parity 2730/2730 with 0 unexplained differences, demotion records specified in
three durable locations plus the optional index, and the O07 receipt shape ready
for independent re-derivation. Nothing outside this file was written by this
seat; no corpus or instrument byte was staged.
