# CriticCa — claim Ca falsification and reverse-hazard review

## Scope and axes

- **Calibration:** correspondence between correction prose, recorded measurements and historical evidence; primary axis of this review.
- **Operability:** whether the frozen bookkeeping counter discriminates the named repairs from generic records-only prose.
- **Coverage:** no new entry/source-support review here; S687 enactment belongs to C and must not be pre-claimed by Ca.

Critic only: no claim judgment, admission, integration, counter edit, runtime dispatch, commit, lane-index or jj mutation. The only lane write is this report. Scratch: `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticCa/`. No tools installed or updated.

## 1. Executed records-only control: overall FAIL, but NITS falsely passes

**Counterexample.** Appending plausible reconciliation prose with the token `W04`, but without either new numeric correction or a record-dependency sentence, changes **NITS FAIL → PASS**. PTRS, HISTOGRAM, REVNAMES and R63SEP remain FAIL, as do DISPO and the whole predicate. Thus the three legs explicitly promised by `claims.json:72` resist this control, but the assignment's stronger NITS expectation does not.

The restriction applies to appended bytes, not the untouched historical log. Historical `47` and `27` already occur in unrelated entries. In particular, root LOG line 4140 records the round-61 wave's 47 seats; line 4081 records a round-55 selftest of 27/27. `accept-ca.py:144-145` searches the **entire** canonical log for substrings `45`, `47`, `W04`, `27`; it does not associate them with round-63 corrections. It also checks neither the 6→9 dry-run correction nor SCORECARD's numeric correction row.

### Setup command

```sh
mkdir -p /home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticCa
git clone --shared --no-checkout --no-hardlinks --quiet /home/vgpnk/Projects/shokunin/kotodama-shokunin /home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticCa/lane && git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin archive ff30a205c8d23b35f1ac533740121a955a9fda96 LOG.md SCORECARD.md corpus/LOG.md | tar -x -C /home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticCa/lane
```

Both commands exited 0 with no output. The scratch root contains the three counter-read text files from the declared base and an independent scratch git administrative directory with shared read-only objects. The absent base `reports/round-63/telemetry/revisions.txt` was deliberately not supplied. No scratch checkout or commit was needed. HISTOGRAM's `git show BASE:corpus/SOURCES.md` resolves through the scratch clone.

The same unchanged lane counter was used before and after. Observed fingerprint:

```text
$ sha256sum reports/round-64/accept-ca.py
f222648ea45517d5e4f7cf27c888e686253fdc67741b23ab458e9ef82081d678  reports/round-64/accept-ca.py
```

### Before: command and complete leg output

```text
$ python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-64/accept-ca.py --root /home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticCa/lane
CANONLOG FAIL r64_at=-1 stray_has_r63=True points_at_stray=False prior_rounds=0
PTRS FAIL score_dead=True stray_dead=True o_fixed=False c_fixed=False
HISTOGRAM FAIL tiers={'A': 13, 'B': 11} correction_present=False
DISPO FAIL items5_7=False s687_flip=False s693_kind=True
REVNAMES FAIL missing=['8d2041fa', '38ec1316', '0c892ce', '80ff34c', 'final-measures-c.txt', 'final-measures-o.txt', 'rev-separability.txt', 'census-end.txt']
NITS FAIL seat_reports_nit=True w04_nit=False
R63SEP FAIL result_cited=False dep_class_named=False
ACCEPT-CA-64: FAIL
exit=1
```

### Exact appended mutation

Applied with the edit tool, exclusively after the base files' final lines. No original byte was replaced.

Append to scratch `LOG.md`:

```markdown

## Round 64 — records reconciliation control

The canonical root log points to `corpus/LOG.md` as the historical stray Round-63 entry; future records belong here.

The closure's receipt pointers, tier histogram, revision provenance and seat-report tally have been reviewed. The W04 duplicate-URL warning tally has been reconciled against the census. The residual receipt names and selftest wording are dispositioned; the online dictionary kind is retained and the unused source lead is queued. Separability was reviewed as an instrument-level observation. These are records-only updates: counters and corpus behavior are unchanged.
```

Append to scratch `SCORECARD.md`:

```markdown

## Axes — round 64 records-only control

Calibration records now distinguish historical reporting from executable evidence. Receipt pointers, tier assignments, revision provenance, numeric nits and separability disclosures have been reviewed; the substantive corpus and tool claims are unchanged.
```

Neither append contains `47`, `27`, `A=13 B=11`, their histogram substitute `13 / 11`, a measured receipt/hash association, or the sentence/phrase `record dependency`.

### After: command and complete leg output

```text
$ python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-64/accept-ca.py --root /home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticCa/lane
CANONLOG PASS r64_at=272051 stray_has_r63=True points_at_stray=True prior_rounds=56
PTRS FAIL score_dead=True stray_dead=True o_fixed=False c_fixed=False
HISTOGRAM FAIL tiers={'A': 13, 'B': 11} correction_present=False
DISPO FAIL items5_7=False s687_flip=False s693_kind=True
REVNAMES FAIL missing=['8d2041fa', '38ec1316', '0c892ce', '80ff34c', 'final-measures-c.txt', 'final-measures-o.txt', 'rev-separability.txt', 'census-end.txt']
NITS PASS seat_reports_nit=True w04_nit=True
R63SEP FAIL result_cited=False dep_class_named=False
ACCEPT-CA-64: FAIL
exit=1
```

Transcriptions are also preserved as scratch `before-ca.txt` and `after-ca.txt`.

**Impacted axes:** calibration and counter operability. This is a fixable proof defect, not evidence that the whole records-only control meets ACCEPT-CA-64.

**Smallest safe correction:** preserve this receipt and disclose the frozen NITS defect; do not edit the counter during this data wave. For an authorized next pre-data revision, scope checks to the Round-64 canonical correction and named Round-63 SCORECARD correction row, require each old→new association (45→47 reports, S650/S651→27 W04 rows, 6→9 FAIL legs) in its proper context, and pin this base-plus-generic-W04 append as a forcing NITS-FAIL control. Pair it with the genuine correction as a positive control. Those proposed controls were not run against a redesigned instrument.

**Inherited attempt-1 evidence defect:** `reports/round-64/telemetry/dry-run-ca.txt:2-8` prints only six legs and omits REVNAMES. It cannot be cited as seven observed failures under rev1. The fresh before run above supplies all seven failures without changing that filed receipt. The inherited broad-token weakness noted in `.ufo/waves/round-64/w2/B2CriticClaims.md:33-34` is now an executed NITS witness rather than just an inference.

## 2. Reverse hazard: historical correction rows

Read all appended correction blocks in `SCORECARD.md:1024-1225` and the canonical Round-64 append, distinguishing their claims from their cited receipts. `git diff ff30a205c8d23b35f1ac533740121a955a9fda96 -- LOG.md SCORECARD.md corpus/LOG.md reports/round-63/telemetry/revisions.txt` showed no changed round-51–62 SCORECARD rows: the new scorecard block is round 63, plus a replacement of its original O evidence pointer. The older corrections therefore must not be falsely attributed to this round.

### A. Concrete inherited overstatement: round-55 selftest “only”

`SCORECARD.md:1095` says “24/24 is the selftest at `454a2dc` **only**.” A distinct later revision `eb0a331` carries exactly the same executable blob:

```text
$ git rev-parse 454a2dc:tools/check-gate-quotes.py eb0a331:tools/check-gate-quotes.py 173cab6:tools/check-gate-quotes.py 2935c47:tools/check-gate-quotes.py
fc6964282441e0b4cd77cc00b9277fcf887778aa
fc6964282441e0b4cd77cc00b9277fcf887778aa
a3bca98d52e94b585bda6394f63215ebff142862
a3bca98d52e94b585bda6394f63215ebff142862
$ git log --format='%h %s' 454a2dc..2935c47 -- tools/check-gate-quotes.py
173cab6 round-55: records — falsify fixes to the entry, registry and checker; lesson, lessons index rev 12, SCORECARD, LOG, SHONEN; final measures; build and falsify wave records
```

The cited report `.ufo/waves/round-56/build/ScribeScorecardNits.md:34-52` supplies observed 24/24 at `454a2dc` and 27/27 at the later tool revision/tip. **[INFERENCE]** the identical selftest artifact also produces 24/24 at `eb0a331` under the same invocation/environment; no historical selftest was rerun here. The literal exclusive-revision wording is therefore too strong, although the intended earlier-tool-versus-tip correction is supported. This is inherited round-56 wording, not a new round-64 regression.

**Smallest safe correction:** append “24/24 at the measured `454a2dc` checkpoint and other revisions carrying blob `fc696428…`; 27/27 at `173cab6` and `2935c47`.” Do not erase the filed row. Impact: calibration; a fixable wording defect, not a tradeoff.

### B. Provenance reconstruction is not observed measurement identity

`reports/round-63/telemetry/revisions.txt:3-8` derives “measured” revisions from receipt-addition history and counter blobs. Its lines 12–14 say the C receipt's ten legs and the commit subject “both name” `8d2041fa`, but `final-measures-c.txt:1-12` contains **no revision at all**. `final-measures-o.txt:1-17` likewise has no revision. This is the very omission the round-63 closure names at lines 43 and 101.

Observed chronology:

```text
$ git log -8 --format='%H %ad %s' --date=iso 38ec1316859850afc605bd21ce38b6a766716e4e
38ec1316859850afc605bd21ce38b6a766716e4e 2026-10-23 16:53:40 -0300 round-63: separability manifest — REC lands carry the round counters (named record dependency; rev-separability.txt recorded)
80ff34c572bd394b6377cbbe2c0315096efe40b9 2026-10-23 16:53:39 -0300 round-63: final measures — ACCEPT-O-63 PASS 15/15 at the records tip (first full run), ACCEPT-C-63 PASS 10/10 at 8d2041fa; separability re-run recorded
```

The command returned eight lines; only the two relevant lines are excerpted above. `git diff --name-status 80ff34c572bd394b6377cbbe2c0315096efe40b9 38ec1316859850afc605bd21ce38b6a766716e4e` printed only `M reports/round-63/separability-manifest.json`. Thus the later tree can be a useful **content-equivalence reference** for O, not proof that its exact committed hash was recorded at run time. An uncommitted tree later committed as `38ec1316` is possible; chronology alone does not falsify that possibility. The receipt/commit subject supports reconstructing C's candidate tree but not the claim that the receipt itself names its hash.

**Smallest safe correction:** append a provenance erratum distinguishing observed receipt contents, first-carrying commit, and inferred/content-equivalent measured-tree references; remove the assertion that the original receipt names the hash. Retain the frozen counter and original receipts. REVNAMES checks unordered token membership (`accept-ca.py:131-141`), not truthful associations or this distinction. No swapped-map mutation was run. Impact: calibration; false-provenance risk, not proof that the historical claim outputs were fabricated.

### C. Premature S687 enactment assertion

At the sampled working tree, `LOG.md:4156` says the S687 `mined -> queued` change is “enacted in `corpus/SOURCES.md` by this round's claim C land and logged old -> new.” The sampled registry line 642 still said `mined` with `used-by` `—`. Ca's DISPO checks text only; it cannot establish enactment. The integration executor was notified to enact the permitted C status flip and lesson log, or leave Ca's wording as a selected/pending disposition. Integration is concurrent; no later status is claimed by this report.

**Smallest safe correction:** make the actual C land match the enactment sentence before recording completion, or append a correction saying the disposition is selected but not yet enacted. Do not add a dependency on C's current registry to Ca's frozen counter. Impact: calibration and C bookkeeping attribution.

### D. Filed-byte preservation conflicts with the frozen PTRS test

The sampled repair replaces the original round-63 SCORECARD O pointer and rewrites three filed `corpus/LOG.md` lines, rather than exclusively appending errata. The replacements point to real receipts, but they change filed historical bytes. Root LOG's append-only header and the canonical correction discipline require corrections as new entries. `accept-ca.py:97-102` searches for the dead filename anywhere in the round-63 SCORECARD block and anywhere in the stray log: preserving the original bytes and merely appending correct superseding pointers can never pass PTRS.

**This is a contract conflict, not a harmless factual correction or something the critic can authorize.** Surface it to the canonical judge; do not silently trade away historical preservation to obtain green legs. The smallest proposed authorized pre-data instrument correction is to recognize an explicit superseding correction record, require its O/C targets to resolve, and pin an append-only repair with unchanged original bytes as the forcing positive control, paired with an unresolved-pointer negative. No counter or filed record was changed by this critic.

### Supported numerical/history corrections; no opposite-value error found in these checks

- Round-63 tiers: the executed HISTOGRAM leg derives `{'A': 13, 'B': 11}` from the declared frozen base. Registry S702 is `docs`, tier B. The 14/10 filed row is correctly superseded, not silently presented as current truth.
- Seat count: `git ls-tree -r --name-only ff30a205c8d23b35f1ac533740121a955a9fda96 .ufo/waves/round-63/w1 | wc -l` printed **47**; the preceding uncounted listing contained the 47 `.md` report paths.
- W04: `reports/round-63/telemetry/census-end.txt:1-27` contains the 27 W04 warning rows, including but not limited to S650/S651; line 28 is the separate S687 W03 warning. This is receipt-verified, not a census rerun.
- O dry run: `declaration-dry-run-o.txt:3-15` carries precisely the nine named FAIL legs, not six. Receipt-verified only.
- Separability: `rev-separability.txt:1-5` has the two findings and exit 1 exactly as corrected. The `38ec1316` manifest puts both counters in REC lands. No separability rerun was performed.
- R62 dispositions: the exact residual filenames exist, and `KotodamaR62.ResidRerunO.md:45-89` records “32 checks, 0 failures”; the 28-versus-32 explanation matches the r62 closure. The S693 `docs`/S692 `book` distinction matches their registered source identities; no kind-cell rewrite was proposed.
- Older appended corrections: round-51's S081 queue correction matches `round-51.md:127`; the R55 six-mistake correction matches its six mistake rows; round-58's omitted TOPIC revision is visible in the six-entry git history slice; round-59's as-reviewed FAIL and narrowed-object/run-2 distinction match the receipts and closure; round-60's qualification breakdown and counted SupportX60 match the full final-measure line; SupportB60 P01→S646/P07→PLANTED matches the committed key and verdict; R61 has seven mistake rows. These are scoped source/receipt comparisons, not an exhaustive recertification of rounds 51–63.

## Limits and handoff

Only the two explicitly assigned Ca acceptance invocations ran. No current-working-tree all-green Ca run, C/O acceptance, historical gate/selftest, live fetch, build, formatter or linter ran. Nothing here admits/rejects a claim or substitutes token coverage for outside review. Main should preserve the observed NITS false-pass receipt and resolve the historical-preservation/provenance issues under the frozen-counter procedure before claiming complete bookkeeping repair.

Report: .ufo/waves/round-64/w1/CriticCa.md
