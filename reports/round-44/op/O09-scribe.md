# O09 — claim-O evidence chain, assembled for integration

- Seat: `O09` | role: scribe | claim **O** | round 44 | date 2026-10-19 | baseline `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d` | out `reports/round-44/op/O09-scribe.md`
- Status: integration-ready summary. Sibling O files present at close: O02, O03, O04, O06, O07, O08, O10. Absent: O01, O05. Where an absent seat owns a required artifact, this file assembles it and labels the provenance `scribe-assembled`.
- Every command below ran read-only from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. This seat wrote only its out path; probes live in `.scratch/o44/` (gitignored). No filed byte, corpus byte, or in-tree instrument byte was edited; nothing was staged under `corpus/`; no `reports/round-*/run-validation.py` was executed; no git/network/install action.
- Verdict on claim O: **PASS, integration-ready.** The r43 O09 body extracts byte-exact at the claim pin, is 27/27 green, produces the policy four-class census `2556+166+0+7=2729` plus one quarantined glob artifact (`2730` refs), lists all 50 fallback mappings and reasons all 7 unresolved rows, reads the wrapped field 4/4 by identity, and parses token-for-token against the r42 witness with differences solely the documented subclass separation.

## 0. Bottom line for the integrator

1. **The bytes are exact.** `reports/round-43/op/O09-scribe.md:356-870` (fence opens `:355`, closes `:871`) is 515 lines, sha256 `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64` — the claim's pin. Two extraction methods (`sed`, `awk`) agree byte-for-byte (O02 §1); O03, O06, O07, O08, O10 independently extracted the same digest.
2. **The landing target is free and the body needs no adjustment.** `tools/harness/basename-couples-resolver.py` does not exist at `c9f4eaa` (`git ls-files tools/harness/` lists seven files, none the resolver). The body's lane-root walk resolves `tools/harness/` → repo root in 2 upward steps; its docstring policy/defect references all resolve. Land byte-exact; do not merge a second body (claims.json:68).
3. **27/27 controls pass**, including the four the claim names: ambiguous (S3a/S3b), indented-prose boundary (S7c), glob precedence over ambiguous (S8b), wrapped identity (S1b is set equality, not arity).
4. **Census at the live 223-entry tree:** `entries=223 refs=2730`, four-class `direct=2556 fallback=166 ambiguous=0 unresolved=7` = 2729, plus `glob-fragment=1` quarantined = 2730, `conservation: True`. O10 reproduced this with a second implementation that does not import the body; the fold closes.
5. **The census artifact is bound by O06.** `reports/round-44/calib/couples-census-r44.json`, schema `kotodama-couples-census-v4`, file sha256 `c0ee791a89883f0958c62fb46755397a6c8f8f64f0a26e1c31227b30b4940699`, `content_sha256` `3ee551fca0b5c88f8dacdf37a544fcd658a23bb7619c9f3850129f773d896a9` (this seat verified the file and all 12 computed checks true). One field conflict is flagged in §6.5: its `corpus_fingerprint` uses a newline-terminated rule (`7675c724…`) and does not reproduce the documented r43 anchor (`444ff801…`).
6. **Disposition leg complete:** 50 distinct fallback mappings / 166 occurrences, all listed; 7 unresolved rows (5 `declared-prospective-seed`, 2 `dangling-reference`) and 1 glob artifact (`extractor-artifact`, `c12=not-applicable`) each carry a non-empty reason; `misaligned: []`.
7. **Parity is token-level clean.** The r42 witness's six classes fold to the successor's four plus artifact with one documented substitution: `prospective(5) → unresolved`, giving `unresolved=7`; direct 2556, fallback 166, glob 1 identical; 0 token diffs, 0 mapping mismatches, same 25 zero-token entries (O07 §5, re-run by this seat §5.3).
8. **Witness demotion is by record only.** `tools/harness/couples-reference-extractor.py` remains byte-identical at `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`; no seat edited it. Wording for the LOG is in §5.1.
9. **Ordering constraint:** generate and file the census at **223 entries after landing the resolver and before the C landing**. The claim pins the 223 arithmetic; a post-C census is a successor artifact, not a rewrite. See §8.

## 1. Evidence chain at this cut

| seat | artifact | status | what it establishes |
|---|---|---|---|
| K01 | `scout/K01-resolver-scout.md` | absent | landing spec assembled here from the body and the live tree (§2) |
| O01 | `op/O01-landing-spec.md` | absent | §2 is the scribe-assembled landing spec |
| O02 | `op/O02-verify.md` | **present** | byte extraction (two methods), clean-root check, 27/27, four-class census, independent fold from `entries_detail`, wrapped identity, determinism, read-only attestation |
| O03 | `op/O03-defects-verify.md` | **present** | D1–D6 fixed/present with line refs; live-vs-latent over-capture qualifier; residual docstring overclaim |
| O04 | `op/O04-witness-demotion.md` | **present** | demotion as a record-level act; five clauses W1–W5; exact insertion for the artifact, LOG, and optional SKILL index; measured 2730/2730 parity, 0 unexplained differences |
| O05 | `op/O05-traps.md` | absent | trap coverage via the body's controls (§4) and O08's floor simulation; no independent filing at this cut |
| O06 | `op/O06-census-artifact.md` | **present** | binding v4 artifact (223, 50 mappings, 7 rows, 12 checks), reproduced and re-verified by this seat (§6) |
| O07 | `op/O07-parity.md` | **present** | both tools live; six→four reconciliation; 0 token/mapping diffs; shadow-root hazard |
| O08 | `op/O08-negative-proof.md` | **present** | AST write scan, 2,921-file manifest NO-DIFF, git-status snapshot, floor simulation at the landed path shape, five integration notes N1–N5 |
| O10 | `op/O10-census-verify.md` | **present** | independent non-importing fold PASS; conservation-tautology caveat; filing fields checklist |

## 2. Landing spec (claim O)

### 2.1 Source bytes

```
$ grep -n '^````' reports/round-43/op/O09-scribe.md
355:````python
871:````
$ sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/o44/basename-couples-resolver.py
$ wc -l .scratch/o44/basename-couples-resolver.py
515
$ sha256sum .scratch/o44/basename-couples-resolver.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
```

The extracted file begins `#!/usr/bin/env python3` and ends `    sys.exit(main())\n`; fence backticks and the language tag are excluded. Source note digest (read-only, unchanged): `956d478bfe7abbaac6598a0d272a7cb524e3d2bc7fa70cc27be41b538e0cb341`.

### 2.2 Target

| item | value |
|---|---|
| path | `tools/harness/basename-couples-resolver.py` |
| state at `c9f4eaa` | absent (`git ls-files tools/harness/` has no such entry) |
| mode | `0644` (stdlib-only; no chmod needed) |
| lines / bytes | 515 / 21,732 |
| sha256 | `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64` |
| imports | argparse, glob, hashlib, os, re, sys, tempfile — stdlib only |
| write surface | read-only; see §7 |

### 2.3 No header/path adjustment is sanctioned or needed

The body's docstring cites `reports/round-42/calib/basename-couples-policy-full.md`, `reports/round-19/audit/entry-audit.py:75`, `reports/round-39/calib/Ca04-verify.md`, and the predecessor path — all exist at `c9f4eaa`. Its lane-root walk from `tools/harness` visits `tools/harness` → `tools` → repo root and stops there (2 upward moves), so `LANE` is the repo root after landing, exactly as in the verified scratch runs. Do not add a header, rewrite the docstring, or change the hardcoded `"round": 43` (see §6.5).

### 2.4 Apply + verify

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
sed -n '356,870p' reports/round-43/op/O09-scribe.md > tools/harness/basename-couples-resolver.py
sha256sum tools/harness/basename-couples-resolver.py   # must equal 43ce341f…ad64
python3 -B tools/harness/basename-couples-resolver.py --selftest   # SELFTEST OK: 27/27
python3 -B tools/harness/basename-couples-resolver.py --census     # 223 / 2730, 2556+166+0+7 +1 glob
sha256sum tools/harness/couples-reference-extractor.py             # d8d23a26… unchanged
```

Do not copy another seat's scratch body over this one; do not create a second resolver path; do not edit the r42 extractor. O08's N1 is binding: the r43 integration line that names `reports/round-43/calib/couples-census-r43.json` must not be followed in r44; the artifact goes under `reports/round-44/calib/`.

## 3. Independent verification (O02, O10, and this seat)

O02, from a clean `.scratch/o02-run/` whose only `corpus/knowledge` ancestor is the repo root:

- two independent extractions (`sed`, `awk`) are byte-identical at the pin;
- the census population is exactly the live tree: `find corpus/knowledge -name '*.md' | wc -l` = 223; `entries_detail` paths = 223; `comm` of sorted path lists = 0 lines;
- `--selftest` = 27 PASS lines, exit 0 (control count 6+3+3+3+4+1+3+2+1+1 = 27);
- `--census` = `entries=223 refs=2730`, `direct=2556 fallback=166 ambiguous=0 unresolved=7`, `glob-fragment=1`, `conservation: True (sum=2730 refs=2730)`;
- an independent fold from per-entry detail (not the tool's totals) reproduces every class count; fallback occurrence sum 166; disposition rows 8; 50 distinct fallback tokens; no row missing a reason; no fallback row with a null mapping; no unknown class;
- 25 entries contribute zero couples tokens; they are counted entries with no couples token, not dropped tokens;
- wrapped field at `corpus/knowledge/linguistics/phonetics-phonology.md:72` reads exactly `{sound-change.md, sound-symbolism.md, tone-prosody.md, writing-systems.md}`; S1b is `tokens == LIVE_TOKENS` (body:328-330), and a same-arity decoy fails it;
- determinism: three plain runs byte-identical; two JSON runs identical.

O10 reproduced the fold with a second, policy-derived implementation that does **not** import the body: 2730 refs, 2556/166/0/7, `2729 + 1 = 2730`. Its caveat is binding on the LOG: the tool's `conservation` boolean is tautological by construction (`sum of the classes it just counted == refs`), so it is not by itself zero-drop evidence; O10's independent fold is.

This seat re-ran the body from `.scratch/o44/` and from `.scratch/o44/lanecheck/` (different depth, same repo-root lane) and got identical token-level class assignments and the same `2556/166/0/7 + 1` totals.

## 4. Defect verification (O03 line refs, body coordinates)

Line references are `body:N` = line in the extracted 515-line file; `r43:N` is the same line in `reports/round-43/op/O09-scribe.md` (`r43 = 355 + body`).

| # | Live-extractor defect | Successor evidence | Verdict |
|---|---|---|---|
| D1 | blank-line over-capture: blank lines are skipped, so later indented prose joins the field (`couples-reference-extractor.py:63-65`, `continue` at `:65`) | blank sets `saw_blank`; an indented line is accepted only when `not saw_blank` (or a same-part hyphen soft wrap, itself gated on `not saw_blank`), else `break` — body:66-78, r43:421-433 | **FIXED** (code path); **0 live incidence** |
| D2 | glob fragment classified by lower branches: slash → basename → ambiguous → glob (`couples-reference-extractor.py:134-150`, glob at `:146-147`) | glob check precedes the slash gate and the basename index — body:149-150, r43:504-505 | **FIXED**; S8b body:420-424 |
| D3 | no ambiguous control (the branch exists at `:144-145`, but the 8-check selftest never exercises it) | synthetic two-hit index body:289-295; S3a/S3b body:369-371 | **PRESENT** |
| D4 | no indented-prose control (r42's `OVER_CAPTURE_TRAP:231-239` is non-indented and is cut off by the next header field, so it never reaches the blank-line path) | S7a/S7b/S7c body:402-415, incl. blank + indented prose | **PRESENT** |
| D5 | no policy four-class census: r42 reports six classes (`census` totals at `:189-191`) | `CLASSES`/`ARTIFACTS` body:140-141; `four_class_totals`/`artifact_totals`/`conservation` body:254-262; CLI body:467-476 | **PRESENT** |
| D6 | no disposition leg: no per-token reason, no fallback mapping list | disposition assignment body:183-188; `_reason` body:200-216; rows body:239-250; mapping rows body:234-238; CLI body:479-487 | **PRESENT** |

Required qualifier (O03 §2, "D1 honesty qualifier"): D1 is a confirmed **code-path** defect, not a present count error. O03's whole-corpus differential found 0 part-level and 0 token-level differences between the two tools; 19 entries have `couples` as the last header field (latent exposure), and 0 entries currently contain a blank line followed by an indented line before the next field. The claim's "confirmed blank-line over-capture" must be read that way in the LOG.

Trap controls present: S4a Tier-1 direct wins over a same-basename hit elsewhere; S4c corpus-relative path is direct; S6 slash-bearing token stays unresolved; S2 phantom tokens are visible, not zeroed; S8/S8b glob is an artifact and beats ambiguous.

## 5. Witness demotion and parity

### 5.1 Demotion wording (record only; no byte edit)

`tools/harness/couples-reference-extractor.py` (r42, 332 lines, sha256 `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`, `--selftest` 8/8, tracked blob `1ded489bbb2bb90b3ad883ec0cd052822d870225`) is demoted to **N6 regression witness and historical 223/2730 six-class recorder**. It is not the r44 census authority, it is not imported by the successor, and its bytes are not edited. The census authority is `tools/harness/basename-couples-resolver.py` (515 lines, sha256 `43ce341f…ad64`, 27/27, four-class + quarantined artifact).

O04 binds the demotion as five checkable clauses: W1 single authority (r44+ census citations name the authority only); W2 not imported/not shelled out (the authority runs 27/27 and censuses with no witness present); W3 bytes frozen (`d8d23a26…`; a later edit is a detectable digest mismatch); W4 live witness (its selftest keeps the N6 live-field guard; its six buckets are an independent cross-check); W5 vocabulary rule (its `prospective` and `glob-fragment` are witness buckets, folded `prospective → unresolved` and `glob-fragment → artifact`, never quoted as policy classes).

Record the demotion in three durable places: (a) the r44 `LOG.md` entry (O04 §3.3 wording; keep both digests); (b) the parity receipt `op/O07-parity.md` (already states demotion-by-record at §1); (c) the filed census artifact's `tool` block (O06 §5 carries path/digest/role; O04 §3.2 specifies additional `selftest`, `buckets`, `fold`, `parity`, `body_round` fields — see §6.3 for the digest consequence). Optional, non-load-bearing: two rows in `SKILL.md:446-454` (the lane's instrument index; neither tool is listed today). Do not edit the witness's own `:2` self-description ("Successor couples-reference resolver…"): it is r42 status, not current authority, and the demotion record states that. Do not write a second resolver, add a shim, rename, or delete the witness.

### 5.2 Six-class → four-class parity

| r42 witness class | count | r44 resolver class | count | separation |
|---|---:|---|---:|---|
| direct | 2556 | direct | 2556 | none |
| fallback | 166 | fallback | 166 | none; 50 distinct mappings, 0 mismatches |
| ambiguous | 0 | ambiguous | 0 | none (0 = 0 live) |
| unresolved | 2 | unresolved | 7 | the 5 `prospective` tokens fold in |
| prospective | 5 | *(folded into unresolved)* | — | documented subclass separation; each row keeps a disposition |
| glob-fragment | 1 | artifact `glob-fragment`, excluded from four-class totals | 1 | documented artifact separation, policy §5.6 |

Arithmetic: `2556 + 166 + 0 + 7 = 2729`; `+ 1` glob artifact = `2730` refs; conservation true.

### 5.3 Token-level proof (this seat's re-run)

Both modules were imported in one process and run over the same 223 sorted paths. After mapping `prospective → unresolved` (the only allowed substitution):

```
entries new/old: 223 223
refs new/old:    2730 2730
token-set differences per entry: 0
class diffs after documented mapping: 0
fallback distinct/occurrences: 50 / 166 both; mapping identical: True
unresolved rosters (entry, token): identical, 7 rows both
wrapped fields: 1 both
```

This matches O07 §5 (class-pair table, 0 token/detail diffs, 0 mapping mismatches, 25 zero-token entries both). Differences that are **not** subclass separation are implementation deltas with zero live effect, enumerated in O07 §6: glob precedence (latent), blank termination (latent), per-token vs entry-level prospective scope (same 5 tokens land unresolved), ambiguous control (0 live).

### 5.4 Run-environment hazards (assert the lane root; do not assume it)

- O07 observed `.scratch/o07/` as a full repository snapshot with a 212-entry corpus: running there silently produced `entries=212 refs=2508`. Discarded.
- O06 hit the same shadow at `.scratch/o06/` (`212/2508`) and re-ran from `.scratch/o06c/`.
- O04 hit a full repo mirror at `.scratch/o04/` (the authority relativized paths to the shadow root, so `path_sets_identical` failed against the live witness) and re-ran from `.scratch/o04-clean/`.
- This seat observed the inverse trap: a fake root made by symlinking `corpus/` into a scratch root makes the lane-root walk stop early; 18 `AGENTS.md` tokens flip `direct → unresolved`.
- O08's floor simulation reproduced the same class of error from the other direction: without lane-root `.md` files and `reports/`, the landed-path simulation read `2,538/25`; adding the lane-root files restored `2556/166/0/7`. Tier 1 legitimately includes the lane root.
- Rule: run the census from the landed `tools/harness/` path (or a scratch dir with no `corpus/knowledge` ancestor except the real root) and assert `KNOW` resolves to `<repo>/corpus/knowledge`. The default text output does not print the resolved root; the JSON `tool` field plus a one-line path assertion are the check.

## 6. The ONE census artifact (O06 binding)

### 6.1 File and identity

| item | value |
|---|---|
| path | `reports/round-44/calib/couples-census-r44.json` |
| schema | `kotodama-couples-census-v4` |
| entries / refs | 223 / 2730 |
| file sha256 | `c0ee791a89883f0958c62fb46755397a6c8f8f64f0a26e1c31227b30b4940699` (26,595 bytes) |
| `content_sha256` | `3ee551fca0b5c88f8dacdf37a544fcd658a23bb7619c9f3850129f773d896a9` |
| `baseline_commit` | `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d` |
| tool | `tools/harness/basename-couples-resolver.py`, sha256 `43ce341f…ad64`, `selftest 27/27`, role `single census authority` |
| witness | `tools/harness/couples-reference-extractor.py`, sha256 `d8d23a26…`, role `N6 regression witness only; bytes untouched; not the census authority` |
| four-class | `direct 2556, fallback 166, ambiguous 0, unresolved 7` |
| artifact | `glob-fragment 1` |
| conservation | four-class sum 2729 + 1 = 2730; `holds: true`; `unaccounted: 0` |
| fallback | 50 rows, occurrences sum 166 |
| rows | 7 unresolved, 0 ambiguous, 1 glob |
| checks | 12 computed booleans, all `true` (I1–I12) |

O06's §5 JSON is the binding filing block; it is generated programmatically and its assembly script refuses to write if any I1–I12 check fails. This seat independently loaded `.scratch/o06c/census-artifact.json` and confirmed: file digest `c0ee791a…`; `content_sha256` recomputes as sha256 of the compact `sort_keys` dump minus `date` and `content_sha256`; 50 mapping rows summing 166; 7 unresolved + 0 ambiguous + 1 glob; all 12 checks true. The block is not hand-typed.

**Merge decision (O04 §3.2).** O04 specifies additional `tool` fields for the same artifact: `body_round: 43`, `witness.selftest: "8/8 PASS"`, `witness.buckets` (2556/166/0/2/5/1), `witness.fold`, `witness.not_authority/not_imported/bytes_untouched`, and a `tool.parity` block naming `op/O07-parity.md`. The integrator has two mutually exclusive options:

- **A — file O06's §5 block verbatim.** Digest `c0ee791a…` / `content_sha256` `3ee551fc…` stand. The demotion is carried by the body docstring, the LOG entry, and the parity receipt, all of which name the witness; O04 §3.2's fields stay out of the artifact.
- **B — apply O04 §3.2 during generation.** Regenerate the artifact (do not hand-edit O06's file), then re-pin its file digest and `content_sha256`; the `c0ee791a…` pin is void and must be replaced everywhere it is quoted.

Do not mix: an artifact that carries the extra fields while claiming `c0ee791a…` is a digest mismatch. This scribe recommends **B** only if the integrator wants the demotion checkable inside the artifact itself; otherwise **A** is the lower-risk, byte-verifiable filing and still satisfies the claim's "parity receipt naming couples-reference-extractor.py witness-only".

### 6.2 What the artifact carries

Header fields: schema, round 44, claim O, date, artifact path, baseline commit, entries, refs. Policy block (path + sha256 `8c3d7c356ea7c1df3bcaab414ccc2035f6dc90272aaed305e4edf35b2890cdd6`). Tool block incl. selftest and witness. Corpus block: 223 entries, partition counts `94/25/25/26/29/24`, index scope `corpus/knowledge/*/*.md`, fingerprint, state note. Totals, conservation identity, wrapped field (`phonetics-phonology.md`, 4 tokens), `misaligned: []`, 50 fallback mapping rows with occurrences and carrier lists, 7 unresolved rows with row ids, dispositions, verbatim reasons and `c12`, `unresolved_summary` (5 prospective / 2 dangling), `ambiguous: []`, one glob row, `checks` I1–I12, `tool_payload` provenance, `content_sha256`.

The 7 unresolved rows (all `c12=blocker`):

| row | token | entry | disposition |
|---|---|---|---|
| U-001 | `honorifics-and-register.md` | `corpus/knowledge/linguistics/language-contact.md` | declared-prospective-seed |
| U-002 | `naming-and-onomastics.md` | `corpus/knowledge/linguistics/language-contact.md` | declared-prospective-seed |
| U-003 | `phonology-basics.md` | `corpus/knowledge/linguistics/language-contact.md` | declared-prospective-seed |
| U-004 | `sound-change.md` | `corpus/knowledge/linguistics/phonetics-phonology.md` | declared-prospective-seed |
| U-005 | `tone-prosody.md` | `corpus/knowledge/linguistics/phonetics-phonology.md` | declared-prospective-seed |
| U-006 | `../linguistics/phonology-sanity.md` | `corpus/knowledge/synthesis/typed-label-routing-workflow.md` | dangling-reference |
| U-007 | `../linguistics/phonology-sanity.md` | `corpus/knowledge/verification/label-channel-routing-verification.md` | dangling-reference |

Glob row: `-gate.md` in `corpus/knowledge/verification/gate-frozen-run-standard.md` → `extractor-artifact`, `c12=not-applicable`.

The 50 distinct fallback mappings (occurrences sum 166; this seat regenerated the list from the artifact):

```
adornment-body-codes.md                  x2   -> corpus/knowledge/culture-material/adornment-body-codes.md
animal-symbolism.md                      x1   -> corpus/knowledge/myth-symbol/animal-symbolism.md
architecture-settlement-lexicon.md       x4   -> corpus/knowledge/culture-material/architecture-settlement-lexicon.md
calendar-festival-systems.md             x2   -> corpus/knowledge/culture-material/calendar-festival-systems.md
calibration-registry.md                  x2   -> corpus/knowledge/verification/calibration-registry.md
color-symbolism.md                       x3   -> corpus/knowledge/myth-symbol/color-symbolism.md
comparative-frameworks.md                x4   -> corpus/knowledge/myth-symbol/comparative-frameworks.md
consistency-verification-checklist.md    x1   -> corpus/knowledge/synthesis/consistency-verification-checklist.md
cosmology-cosmography.md                 x2   -> corpus/knowledge/myth-symbol/cosmology-cosmography.md
costume-semiotics.md                     x8   -> corpus/knowledge/culture-material/costume-semiotics.md
coupling-model.md                        x1   -> corpus/knowledge/synthesis/coupling-model.md
creation-myths-taxonomy.md               x1   -> corpus/knowledge/myth-symbol/creation-myths-taxonomy.md
dress-through-eras.md                    x5   -> corpus/knowledge/culture-material/dress-through-eras.md
era-language-staging.md                  x1   -> corpus/knowledge/synthesis/era-language-staging.md
era-periodization-models.md              x1   -> corpus/knowledge/culture-material/era-periodization-models.md
garment-lexicon-crosslinguistic.md       x3   -> corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md
historical-linguistics.md                x9   -> corpus/knowledge/linguistics/historical-linguistics.md
inca.md                                  x1   -> corpus/knowledge/civilizations/inca.md
kinship-terminology.md                   x1   -> corpus/knowledge/linguistics/kinship-terminology.md
language-contact.md                      x10  -> corpus/knowledge/linguistics/language-contact.md
lexicon-coverage-audit.md                x1   -> corpus/knowledge/verification/lexicon-coverage-audit.md
loanword-material-dating.md              x1   -> corpus/knowledge/synthesis/loanword-material-dating.md
material-culture-inference-method.md     x10  -> corpus/knowledge/culture-material/material-culture-inference-method.md
maya-classic.md                          x1   -> corpus/knowledge/civilizations/maya-classic.md
mesopotamia-sumer-akkad.md               x1   -> corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md
morphological-typology.md                x2   -> corpus/knowledge/linguistics/morphological-typology.md
music-instrument-lexicon.md              x1   -> corpus/knowledge/culture-material/music-instrument-lexicon.md
myth-ritual-theories.md                  x1   -> corpus/knowledge/myth-symbol/myth-ritual-theories.md
myth-to-language-derivation.md           x1   -> corpus/knowledge/synthesis/myth-to-language-derivation.md
naming-systems.md                        x14  -> corpus/knowledge/linguistics/naming-systems.md
number-symbolism.md                      x1   -> corpus/knowledge/myth-symbol/number-symbolism.md
orality-formulaic-language.md            x4   -> corpus/knowledge/linguistics/orality-formulaic-language.md
pantheon-archetypes.md                   x5   -> corpus/knowledge/myth-symbol/pantheon-archetypes.md
phonetics-phonology.md                   x1   -> corpus/knowledge/linguistics/phonetics-phonology.md
politeness-taboo-euphemism.md            x2   -> corpus/knowledge/linguistics/politeness-taboo-euphemism.md
real-world-inspiration-boundaries.md     x2   -> corpus/knowledge/verification/real-world-inspiration-boundaries.md
register-strata-attestation.md           x1   -> corpus/knowledge/linguistics/register-strata-attestation.md
religion-language-co-evolution.md        x1   -> corpus/knowledge/synthesis/religion-language-co-evolution.md
ritual-garments.md                       x6   -> corpus/knowledge/culture-material/ritual-garments.md
ritual-liminality.md                     x2   -> corpus/knowledge/myth-symbol/ritual-liminality.md
semantics-pragmatics.md                  x3   -> corpus/knowledge/linguistics/semantics-pragmatics.md
sociolinguistics-registers.md            x7   -> corpus/knowledge/linguistics/sociolinguistics-registers.md
source-discipline-calibration.md         x1   -> corpus/knowledge/synthesis/source-discipline-calibration.md
sumptuary-law-rank-display.md            x3   -> corpus/knowledge/culture-material/sumptuary-law-rank-display.md
symbolism-synthesis-method.md            x10  -> corpus/knowledge/myth-symbol/symbolism-synthesis-method.md
taboo-euphemism-lifecycle.md             x1   -> corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md
textile-technology.md                    x4   -> corpus/knowledge/culture-material/textile-technology.md
trade-economy-lexicon.md                 x3   -> corpus/knowledge/culture-material/trade-economy-lexicon.md
warrior-material-culture.md              x1   -> corpus/knowledge/culture-material/warrior-material-culture.md
writing-systems.md                       x13  -> corpus/knowledge/linguistics/writing-systems.md
```

### 6.3 How to file

1. Land the body (§2.4), verify digest/selftest/census.
2. Choose the artifact variant first (§6.1 merge decision): **A** = O06's §5 block verbatim, verify file sha256 `c0ee791a…` and `content_sha256` `3ee551fc…`; **B** = add O04 §3.2's `tool` fields during generation, then re-pin both digests. Never hand-edit an existing artifact to move between variants.
3. Do not file a second census under another name (the r43 F4 two-name conflict is not repeated). A human summary, if wanted, is the same basename with `.md`, not a second JSON.
4. If the integrator prefers a different wrapper, that is a named filing decision: record the new digest and why; do not hand-edit totals.

### 6.4 Round and provenance stamps

- The artifact's `round` is 44; the body's raw `--json` hardcodes `round: 43` (body:461). The artifact keeps the body bytes pinned and records round 44 authoritatively; do not edit the body.
- O06's artifact carries `tool.run_path: .scratch/o06c/basename-couples-resolver.py` and `tool_payload.sha256: ef90ef86…`. These are **provenance of the generating run**, not dependencies: the body is stdlib-only and reads no scratch path. If a durable artifact should not point at cleaned scratch, the integrator may replace `run_path` with the landed path in a new artifact revision and re-pin; do not present the scratch path as the authority.
- `tool_payload.sha256` will not reproduce after landing because the raw payload's `tool` field changes; the artifact's `tool.sha256` (over the file bytes) is the stable pin.

### 6.5 Flagged conflict: `corpus_fingerprint`

O06's artifact records `corpus.corpus_fingerprint = 7675c7246cf0ac62072d083443fba6b9b699e6108f100476284e44c0972953ba` under the rule "sha256 over sorted `<repo-relative-path>:<file-sha256>\n` lines" — i.e. newline-terminated lines. This seat reproduced that value under that rule. It does **not** reproduce the documented r43 anchor `444ff801727604b614e1eca302ff77314ebbd0f5f064a82d1c167e7f02125e35`, which is `sha256("\n".join(rows))` with no trailing newline (`reports/round-43/op/O10-census-artifact.md:544-552`; O10 §1.2 calls `444ff801…` the r44 reproduction of the r43 population digest). Both values are internally consistent with their respective rules; they are not the same digest.

Resolution for the integrator (non-blocking, but must be named, not silent): either (a) keep O06's newline-terminated rule and add `corpus.anchor_sha256: 444ff801…` plus a one-line rule note, recording that the v4 fingerprint rule supersedes the r43 recipe; or (b) recompute the field to `444ff801…` using the r43 recipe and re-pin the artifact's file and `content_sha256`. Do not file a field that claims to reproduce the r43 anchor while carrying the other rule's value. The claim's thresholds do not require a fingerprint, so this is a provenance-consistency item.

## 7. Negative proof (O08 PASS; this seat's corroboration)

### 7.1 Static write surface

O08's AST scan found exactly three `open` calls and no write-capable call:

```
(164, 'open', ['path', "'rb'"])        # entry read
(322, 'open', ['LIVE_PATH'])           # selftest live read
(463, 'open', ['__file__', "'rb'"])    # self-digest
```

No `write`, `writelines`, `os.remove/rename/unlink/mkdir/makedirs`, `shutil.*`, `subprocess.*`, or pathlib write methods. `sys.dont_write_bytecode = True` (body:25). This seat's grep agrees: only lines 11 (docstring), 25, 164, 322, 463.

### 7.2 Dynamic

O08 took a 2,921-file sha256 manifest of `corpus/`, `tools/`, and every filed round `reports/round-1..43/**`, exercised `--selftest`, `--census`, `--census --json`, and one entry path, and re-took the manifest:

```
manifest-before sha256 = manifest-after sha256 = 3006cd77a57ec77eda1d52022fb2dd7d3b4d9f42c1f1a5143e323014fce4911c
diff before after -> TREE NO-DIFF
git status --porcelain -uall before == after (5ef42ce6…)
git diff --stat HEAD -> empty
```

The only untracked non-scratch paths were r44 round metadata. At this seat's cut: `git status --porcelain` → `?? reports/round-44/` only; r42 digest `d8d23a26…`; wrapped-entry digest `b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b`; `tools/harness/basename-couples-resolver.py` absent.

### 7.3 No second competing resolver

- Durable tree at `c9f4eaa`: `git ls-files | grep -E 'basename-couples-resolver|couples-resolver'` → none; `git ls-files tools/harness | grep -i couples` → only `couples-reference-extractor.py`.
- O08's floor simulation placed the body at `<lane>/tools/harness/basename-couples-resolver.py` and compared ten JSON keys field-for-field: all `SAME`, `tool: tools/harness/basename-couples-resolver.py`, digest pinned.
- Scratch copies (`find .scratch -name 'basename-couples-resolver.py'` → 19, all gitignored and untracked) are probe artifacts, not authorities. The invalid symlinked-root copy used in this seat's early probe was deleted.
- The contract names exactly one resolver path: `claims.json` has 4 occurrences, `targets.json` 2 (plus the Ca gate `claims-freshness.py`, which is not a resolver).

### 7.4 N1–N5 from O08

N1: do not follow the r43 line writing to `reports/round-43/calib/couples-census-r43.json`; target `reports/round-44/calib/`. N2: body hardcodes `round: 43` and schema v3; record provenance, do not edit bytes. N3: denominator ordering — take the O census pre-C. N4: if reusing the r43 O12 gate, re-scope `ALLOWED_PREFIXES` to `reports/round-44/`. N5: file the `r39-ic05-resolver-durability` successor record under `reports/round-44/`; never edit `reports/round-40/op/defect-queue-v2.json`.

## 8. Cross-claim ordering: the census denominator is 223, not 224

Claim O pins `2556+166+0+7` over the baseline partition; claim C adds one entry (223 → 224). Order the integration:

1. land the resolver (`tools/harness/basename-couples-resolver.py`);
2. run `--selftest` and `--census` **before** the C landing;
3. file `reports/round-44/calib/couples-census-r44.json` (O06 §5) with `entries: 223` and the pre-C `state_note`;
4. then apply the C landing and its README rev 2.5;
5. if a post-C census is wanted, file it as a **successor** artifact with its own `entries: 224` and provenance — never rewrite the 223 artifact.

Why: the census is live-tree-derived, so a C entry carrying couples tokens changes the totals. O03 §7.4, O06 §6.5, and O08 N3 state the same constraint. The resolver's selftest is robust to the C landing (S9 recomputes conservation; S10 is the wrapped entry), but the claim's pinned arithmetic is not.

## 9. Integration sequence

1. Apply §2.4; verify digest, selftest, census, witness digest.
2. File the census artifact at 223 in the chosen variant (§6.1/§6.3): **A** keeps O06's `c0ee791a…` / `3ee551fc…`; **B** merges O04 §3.2 and re-pins. Resolve or annotate §6.5 in the same step.
3. Record O04's demotion records: the §5.1 wording in the r44 LOG, `op/O07-parity.md` as the parity receipt, and the artifact `tool` block under the chosen variant (plus the optional two SKILL.md index rows). File O08's N5 successor record.
4. Apply the C landing (separate claim) and README rev 2.5.
5. Run the round's validation (authored by the integrator; never in-tree from a seat) with §10.
6. Negative-proof sweep: `git status` shows only the resolver + `reports/round-44/**`; r42 and corpus digests unchanged.

## 10. Acceptance checks for the round's validation O leg

- O1: `tools/harness/basename-couples-resolver.py` exists; sha256 `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`.
- O2: `--selftest` exit 0 and exactly `SELFTEST OK: 27/27 controls`; `grep -c '^PASS'` = 27.
- O3: `--census` first line `entries=223 refs=2730`; four-class line `direct=2556 fallback=166 ambiguous=0 unresolved=7`; artifact line `glob-fragment=1`; `conservation: True`.
- O4: per-entry on `corpus/knowledge/linguistics/phonetics-phonology.md` prints exactly the four tokens with classes `direct, direct, unresolved, unresolved`; no `prosody.md` / `toneprosody.md`.
- O5: the filed artifact has `entries: 223`, `refs: 2730`, four-class totals, artifact total 1, 50 fallback rows summing 166, 7 unresolved rows each with a non-empty reason and disposition, 0 ambiguous, 1 glob, `misaligned: []`, and all 12 `checks` true. Variant **A**: sha256 `c0ee791a…` and `content_sha256` `3ee551fc…`. Variant **B**: the re-pinned digests recorded by the integrator, with the O04 §3.2 fields present.
- O6: the artifact's `tool.sha256` equals O1 and `tool.witness.sha256` equals `d8d23a26…`; `baseline_commit` present. Under variant B also `tool.body_round = 43` and `tool.witness.buckets` = `{direct:2556, fallback:166, ambiguous:0, unresolved:2, prospective:5, glob-fragment:1}`.
- O7: `sha256sum tools/harness/couples-reference-extractor.py` = `d8d23a26…`; `git status --porcelain` has no `M` under `corpus/` or `tools/`.
- O8: no second resolver path is tracked; no scratch path is a runtime dependency of the landed tool.

## 11. Owed / to-verify

- **O01/O05 seat files were absent at this cut.** §2 (landing spec) and the trap coverage are `scribe-assembled`; O04 is now present and §5.1 cites it. If O01/O05 file, cross-read rather than merge duplicate specs. Do not file two census artifacts or two tool bodies.
- **Artifact variant A/B (§6.1).** Choose one before filing and record it; do not claim O06's `c0ee791a…` while carrying O04 §3.2's extra fields. `to-verify` at integration.
- **`corpus_fingerprint` rule conflict (§6.5).** O06's `7675c724…` is newline-terminated; the r43/O10 anchor is `444ff801…`. Name the adopted rule or recompute; do not silently ship a field that claims the anchor while using the other rule.
- **O06 artifact's `tool.run_path` / `tool_payload.sha256` point at `.scratch/o06c/`.** Provenance only; the file should not be read as depending on scratch. Consider replacing with the landed path in a revised artifact and re-pinning.
- **Docstring overclaim (O03 §7 item 1):** the body's docstring says a blank line terminates the field "unless the previous part ends in a hyphen soft wrap and the next line is indented" (body:54-59), but `soft_wrap` is gated on `not saw_blank` (body:73), so that exception is unreachable; `tone-` / blank / indented `prosody.md` yields `[]`. 0 live blank-separated continuations, so no data loss. The body must land byte-exact at the pin; record as a **successor-record note**, not an edit. Owner: next O-round.
- **`"round": 43` hardcode** (body:461): the filed artifact's `round` is 44; the body stays pinned. Provenance decision, not a defect.
- **S1a is corpus-coupled** (body:325-326, 272): the selftest asserts the embedded fixture equals the live bytes of `phonetics-phonology.md:72`. A future edit to that entry turns the selftest red by design. The C landing does not touch it.
- **`AGENTS.md` tokens:** 18 entries carry `AGENTS.md` in their couples fields, resolved `direct` via the lane root. They are real census content; a shifted lane root misclasses them (§5.4, O08 §5).
- **Post-C 224 census** is not measured here; if wanted, it is a successor artifact. `to-verify` at integration.
- **No `reports/round-44/run-validation.py` was executed** (prohibited in-tree for seats); §10 is the proposed O leg, not a claimed pass.

## 12. Citations and reproduce

- Claim contract: `reports/round-44/claims.json:25-35` (claim O), `:4-13` (dispatch/axes), `:60-70` (non-goals).
- Source body: `reports/round-43/op/O09-scribe.md:356-870` (515 lines; fence `:355`/`:871`; source digest `956d478b…`).
- Policy: `reports/round-42/calib/basename-couples-policy-full.md` §2 `:27-48` (two tiers, four classes), §3 `:50-58` (reporting rules; fallback count beside the count), §5.6 `:100-102` (glob artifact, not unresolved, not fallback).
- Witness: `tools/harness/couples-reference-extractor.py` (332 lines; `couples_block:50-73`, blank `continue:63-65`, `classify:134-150`, glob `:146-147`, `census:186-211`, `selftest:242-296`).
- Wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72` (digest `b4f9b003…`), tokens `sound-change.md`, `tone-prosody.md` (unresolved/declared-prospective), `sound-symbolism.md`, `writing-systems.md` (direct).
- Seat evidence: `op/O02-verify.md`; `op/O03-defects-verify.md`; `op/O04-witness-demotion.md` (§2 W1–W5, §3 demotion records, §5 measured parity); `op/O06-census-artifact.md` §5 (binding artifact); `op/O07-parity.md`; `op/O08-negative-proof.md` (W1–W4, N1–N5); `op/O10-census-verify.md` (§1.2 population anchor, §3.4 conservation caveat, §6 filing fields).
- Baseline: `git rev-parse --short HEAD` → `c9f4eaa` (full `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d`); `git status --porcelain` → `?? reports/round-44/`; `find corpus/knowledge -name '*.md' | wc -l` → 223.
- This seat's probes: `.scratch/o44/basename-couples-resolver.py` (pin), `.scratch/o44/census.json`, `.scratch/o44/census-lanecheck.json`, `.scratch/o44/lanecheck/tool.py`; O06's artifact was re-read at `.scratch/o06c/census-artifact.json`. All gitignored; none is a durable dependency.

Reproduce the census:

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/o44/basename-couples-resolver.py
sha256sum .scratch/o44/basename-couples-resolver.py        # 43ce341f…ad64
python3 -B .scratch/o44/basename-couples-resolver.py --selftest   # 27/27, exit 0
python3 -B .scratch/o44/basename-couples-resolver.py --census     # 223/2730; 2556+166+0+7 +1
python3 -B .scratch/o44/basename-couples-resolver.py --census --json > .scratch/o44/census.json
```

Observation window for this file: 2026-10-19T17:19Z-17:25Z. All numbers above are measured at that window; none is inferred.
