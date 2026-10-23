# CriticRevCa — Ca counter falsification and historical overcorrection review

## Scope, axes, and revision dependency

- **Calibration:** correction assertions must match the filed measurements and revision provenance.
- **Operability:** NITS must discriminate a correction from a records-only append; the base must retain all seven failures.
- **Coverage:** no source/entry coverage was changed or evaluated by these Ca controls.

Critic only: no counter/record patch, integration, claim judgment, admission, commit, lane-index/jj mutation, subagent, alternate runtime, or live URL run. Only this report is written in the lane. Scratch is exclusively `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/CriticRevCa/`. No tools installed or updated.

**Dependency:** the assigned rev2 did not exist when this seat captured the canonical file. It was still rev1, SHA-256 `f222648ea45517d5e4f7cf27c888e686253fdc67741b23ab458e9ef82081d678`. Parent explicitly acknowledged the missing artifact and instructed: attack observed rev1, record the dependency, never patch or wait. Therefore none of the executions below is represented as a rev2 result. RevCounters owns the pending revision. This is an unavailable prerequisite, not evidence that rev2 itself passes or fails.

Read the wave-1 Ca critic/reviewer receipts and routed defect list, plus the supplied cross-claim attack findings. They are evidence, not authority to weaken the frozen predicate.

## Executed controls

Setup: a scratch `git clone --shared --no-checkout --no-hardlinks` supplies historical objects. Each fixture has its own files and a `.git` pointer to that scratch clone, never the lane administrative directory. `LOG.md`, `SCORECARD.md`, and `corpus/LOG.md` are extracted with `git show ff30a205c8d23b35f1ac533740121a955a9fda96:<path>`; the base has no `revisions.txt`, which is deliberately absent. Mutations only append bytes to the first two files. No original byte is removed.

Command:

```sh
python3 -B /home/vgpnk/.cache/hyaku/kotodama-r64-w2/CriticRevCa/attack_controls.py
```

The runner pins an exact counter copy before launching the six independent controls concurrently. Each child runs:

```text
/usr/bin/python3 -B <scratch>/counter-snapshots/f222648ea45517d5e4f7cf27c888e686253fdc67741b23ab458e9ef82081d678.py --root <scratch>/fixtures/<fixture>
```

Exact appends, argv, input SHA-256 values, stdout/stderr and exit status are preserved in `<scratch>/results/f222648ea45517d5e4f7cf27c888e686253fdc67741b23ab458e9ef82081d678/<fixture>.json`.

| fixture | CANONLOG | NITS | PTRS / HISTOGRAM / DISPO / REVNAMES / R63SEP | whole predicate / exit |
|---|---|---|---|---|
| `base` | FAIL | FAIL | all FAIL | FAIL / 1 |
| `records-bare-tokens` | PASS | **PASS** | all FAIL | FAIL / 1 |
| `records-seat-phrase-wrong` | PASS | **PASS** | all FAIL | FAIL / 1 |
| `records-negated-exact-phrases` | PASS | **PASS** | all FAIL | FAIL / 1 |
| `records-out-of-scope-phrases` | PASS | **PASS** | all FAIL | FAIL / 1 |
| `nits-positive-only` | PASS | PASS | all FAIL | FAIL / 1 |

No stderr was emitted. These isolate a NITS false pass; **none bypasses ACCEPT-CA-64 as a whole**. The positive control supplies only the three genuine numeric corrections and is not expected to pass the other repairs.

### D1 — bare tokens still substitute for correction in observed rev1

**Counterexample:** after a Round-64 heading and canonical-to-stray pointer, append:

> Bookkeeping labels only: 47 / 27 / 9 / W04. No measured correction was made.

Append a `### Round-63 corrections` table to SCORECARD whose `numeric nits` row says:

> Record labels only: 47 / 27 / 9 / W04. No correction was made.

Observed:

```text
NITS PASS seat_reports_nit=True w04_nit=True
ACCEPT-CA-64: FAIL
exit=1
```

`accept-ca.py:144-145` searches the entire canonical log for `45`, `47`, `W04`, `27`; historical `45` already exists. It neither checks the SCORECARD correction row nor the 6→9 dry-run correction. This independently extends wave-1's bare-W04 witness to all specifically assigned bare tokens.

**Impacted axes:** calibration and counter operability. **Classification:** fixable instrument defect; no axis trade is justified by the false-positive leg.

**Smallest safe correction, not applied:** receipt-forced pre-data revision that binds all three old→new facts to the named Round-64 correction and Round-63 SCORECARD correction row, preserves all other legs, and makes this exact fixture NITS-FAIL while retaining the genuine numeric positive. L1 must stamp and commit the forcing receipt with the revision. Rev2 remains untested here.

### D2 — “47 seat reports” is not a semantic discriminator

`records-seat-phrase-wrong` explicitly says `47 seat reports` is only a filing example, that round 63 still had 45, that W04 still means only S650/S651, and that the actual dry run still had six FAIL legs. It nevertheless prints the same NITS PASS line. No true numeric correction is made.

The stronger `records-negated-exact-phrases` append, placed in both named records, says:

> Round 63 did not land 47 seat reports (it had 45); W04 did not cover 27 duplicate-URL rows (it names only S650/S651); the ACCEPT-O-63 dry run did not have 9 FAIL legs (it had 6). These are denials of the proposed corrections, not corrections.

It also NITS-passes. `records-out-of-scope-phrases` supplies the affirmative exact value/unit phrases but expressly attributes them to an unrelated round/toy run, not the historical receipts; it also NITS-passes.

**Honest semantic limit:** scoped token/phrase pinning can establish that named strings appear in the intended block, not whether they are asserted, negated, merely quoted, attributed to another round, or supported by the referenced receipt. Exact phrase matching alone cannot distinguish the denial above from a correction. Rejecting this particular denial would not establish general semantic completeness. These rev1 controls are also ready-made challenges for rev2; no rev2 outcome is inferred.

**Impacted axes:** calibration and operability. **Smallest safe correction:** preserve these negative controls, bind value/unit/round/old→new associations and validate their receipt-derived quantities; retain independent content review for assertion/provenance rather than describing lexical PASS as semantic verification. Do not silently narrow the frozen Ca statement or add a review-only escape to obtain green results.

### Base still fails all seven legs — observed rev1 only

Complete executed base output:

```text
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

This is seven emitted failures, unlike the inherited six-leg rev0 dry-run receipt. It does not establish rev2's before-vector.

## Historical overcorrection hazards — rounds 51–63

Executed the read-only `history_audit.py` in this seat's scratch. Its full results are preserved as `<scratch>/history-audit.json`; it uses fixed-revision `git show`, `rev-parse`, `ls-tree`, `log`, plain counts, and working-tree byte comparisons. No historical acceptance/selftest was rerun.

### D3 — genuine corrections must not erase filed history to satisfy PTRS

Observed comparisons against the declared base:

```text
score_rounds51_62_byte_unchanged=true
score_round63_only_pointer_replacement=true
canonical_log_base_is_exact_prefix=true
stray_log_base_is_exact_prefix=false
```

Thus the SCORECARD content before its Round-63 heading is byte-identical, the original Round-63 axes block changes only its O receipt pointer, and root LOG is append-only. But `corpus/LOG.md` original lines 4, 5 and 7 are replaced (two receipt pointers and the false R63-M2 disposition attribution). This confirms the wave-1 historical-preservation conflict remains in the sampled repair; it is not evidence of a new change to rounds 51–62.

Rev1 PTRS (`:95-102`) requires the dead filename to disappear from the entire Round-63 SCORECARD block and stray log. Consequently preserving the filed text and merely appending an explicit superseding pointer cannot pass. Correct target filenames do not make historical byte replacement append-only.

**Impacted axis:** calibration. **Classification:** contract/instrument conflict, not a harmless trade this critic can authorize. **Smallest safe correction:** preserve the originals and append scoped errata; an authorized receipt-forced pre-data PTRS revision must recognize the explicitly superseded pointer and check its replacement targets. The canonical Rust judge retains adjudication; historical preservation must not be silently traded away for green legs.

### D4 — inherited “only” overcorrection and new false-provenance prose

1. `SCORECARD.md:1095` says 24/24 is the selftest at `454a2dc` **only**. Historical blob identities are:

   ```text
   454a2dc:tools/check-gate-quotes.py = fc6964282441e0b4cd77cc00b9277fcf887778aa
   eb0a331:tools/check-gate-quotes.py = fc6964282441e0b4cd77cc00b9277fcf887778aa
   173cab6:tools/check-gate-quotes.py = a3bca98d52e94b585bda6394f63215ebff142862
   2935c47:tools/check-gate-quotes.py = a3bca98d52e94b585bda6394f63215ebff142862
   ```

   `.ufo/waves/round-56/build/ScribeScorecardNits.md:40-52` records 24/24 at the measured O land and 27/27 later. **[INFERENCE]** the identical executable at `eb0a331` has the same selftest under the same environment. The exclusive-revision wording is therefore overstrong, although the measured-checkpoint distinction is supported. This defect is inherited, not introduced by the sampled round-64 append. Smallest correction: append “24/24 at the measured `454a2dc` checkpoint; 27/27 at the later checker/tip,” without claiming exclusivity or rewriting the filed row.

2. `reports/round-63/telemetry/revisions.txt:12-14` says the C receipt and commit subject **both name** `8d2041fa`, and the counter is unchanged between that land and the records commit. The filed C receipt contains leg outputs and exit status but no revision. The measured historical counter blobs actually differ:

   ```text
   8d2041fa:reports/round-63/accept-c.py = 4a8791ba857b6a809a11084dcd2ff4b3a6c67ae0
   0c892ce:reports/round-63/accept-c.py = e6322538ce618170839c1e8cb1b1259f302ff715
   ```

   The final-measures commit subject does name C's land, but that cannot make the original receipt name it. O's final-measures carrying commit is `80ff34c`, one second before `38ec1316`; only the separability manifest changes between them. That supports a content-equivalence reference, not contemporaneously recorded exact measurement identity. Smallest correction: an explicit provenance erratum distinguishing receipt contents, data-land revision, counter revision, first-carrying commit and inferred/equivalent-tree reference. Do not overwrite unsigned historical receipts to pretend they originally carried hashes.

3. The filed Round-63 O row still describes the earlier `0d965ccb` tool at `dd81fd29`, while the final freeze receipt pins `c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0` (`reports/round-63/telemetry/freeze-sha256.txt:4`; also flagged in wave-1 ExecCounterO). Smallest correction: append the build-versus-final-tool distinction, not a retroactive replacement that makes the filed historical statement look like the final measured identity.

**Impacted axis:** calibration; fixable attribution/wording defects, not evidence that the historical PASS outputs were fabricated. NITS/REVNAMES token membership cannot resolve these provenance issues.

### Sampled historical truths that must remain intact

- Round-51 correction: at `2b956d7`, S071–S131 are **52 mined / 9 queued**, including S081 queued; the appended correction is supported.
- Round-55 six-mistake correction and Round-61 seven-mistake correction match the six/seven named rows in the base lessons.
- Round-58's exact filed history command, `git log '91fb8fd9^..80f48c2c' -- reports/round-58/accept-c.py`, returns six entries including omitted `31cf8b6`; do not erase that omission erratum. The round-59 lesson separately qualifies the 123-control claim as whole-predicate, not uniform support discrimination.
- Round-59 correction remains **MISSED on the as-reviewed object**: filed `as-reviewed-c.txt` says SUPPORT FAIL for S602/S616/S623/S643 and ACCEPT-C-59 FAIL. A later narrowed object cannot retroactively turn that record into a pass.
- Round-60's qualified set contains 13 seats including SupportX60; the filed support line shows the 11 void seats split 5 cwd / 4 `deny:chr(` / 1 `kotodama` / 1 bare X2. The corrective breakdown is supported.
- Round-62's named residual O receipt records **32 checks, 0 failures** at lines 45–89. S693 remains kind `docs`, S692 `book`; no kind overcorrection is called for.
- Round-63 numeric corrections are supported by fixed base evidence: **47** wave-1 report paths from `git ls-tree`; **27** W04 warning rows in filed `census-end.txt`; **9** dry-run FAIL legs: GEN, ORDER, BOUND, REDIRECT, MALFORMED, GZIP, TRUNC, TIMEOUT, REVIEW. HISTOGRAM's executed base census is **A13/B11**. Preserve the original erroneous claims as filed and explicitly supersede them, rather than presenting 45, two W04 rows, six FAILs or A14/B10 as current truth.

These are scoped receipt/history comparisons, not an exhaustive recertification of every cell in rounds 51–63. No new destructive rewrite of rounds 51–62 was observed; it would be false to label all filed historical prose unqualifiedly true given D4.

## Handoff limit

The only acceptance executions were the six explicitly assigned scratch Ca controls above; no current-lane all-green Ca run, C/O acceptance, historical gate/selftest, native judgment, build, formatter, linter or smoke run was performed. All controls are reproducible under a pinned counter hash. Remaining evidence prerequisite is the actual rev2 artifact: its bare-token and semantic negative results and all-seven-base-FAIL result cannot be claimed from rev1 output. This seat did not wait for or patch that artifact.

## Postscript — actual rev2 arrived; dependency resolved and attacked

RevCounters notified this seat after the initial report. Per the parent's instruction, I re-read the canonical counter once and reran the same six independent controls against an exact new snapshot, without modifying the lane counter. Observed SHA-256 matches the owner notification:

```text
a8088092cf62107566b5bdcb3b34af65b750e8e46899742514724c4f34f9060c
```

This postscript supersedes the earlier missing-artifact limitation. There are now **12** scratch Ca invocations: six per pinned counter. Rev2 receipts are under `<scratch>/results/a8088092cf62107566b5bdcb3b34af65b750e8e46899742514724c4f34f9060c/`, with the same fixture names and exact argv/input digests/appends/output/exit metadata. The runner snapshots source bytes before launching the children, so concurrent lane editing cannot change their counter identity.

### Actual rev2 results

| fixture | rev2 NITS | observed detail |
|---|---|---|
| `base` | FAIL | `seat_reports_nit=False duplicate_url_nit=False fail_legs_nit=False` |
| `records-bare-tokens` | **FAIL** | `seat_reports_nit=False duplicate_url_nit=True fail_legs_nit=False` |
| `records-seat-phrase-wrong` | **PASS — counterexample** | `seat_reports_nit=True duplicate_url_nit=True fail_legs_nit=True` |
| `records-negated-exact-phrases` | **PASS — counterexample** | same three True values |
| `records-out-of-scope-phrases` | **PASS — counterexample** | same three True values |
| `nits-positive-only` | PASS | same three True values |

Every fixture still prints `ACCEPT-CA-64: FAIL`, exit 1, with no stderr. All non-NITS results match the earlier matrix: records appends pass CANONLOG but fail PTRS/HISTOGRAM/DISPO/REVNAMES/R63SEP. **No whole-predicate bypass is claimed.**

Assigned item 1 is satisfied by the executed bare-token negative. Assigned item 2 is **falsified** by the executed wrong-substance control, not merely left as a hypothetical semantic limitation. The exact canonical-log append is:

> The label 47 seat reports is merely a filing example; round 63 still had 45. W04 has 27 illustrative tokens, but the filed warning is still only S650/S651. The number 9 labels a hypothetical FAIL total; the actual ACCEPT-O-63 dry run still had 6 FAIL legs. No measured correction is made.

The appended SCORECARD row likewise says 47 is an example, W04 still means only S650/S651, and six is the actual dry-run FAIL total. It is not a genuine repair under either record. Yet the rev2 leg reports all three correction flags True.

**Mechanism (`accept-ca.py:150-172`):** rev2 scopes to the first Round-64 heading, then uses independent value/context searches within up to 120 characters. The W04 branch accepts `W04 ... 27` without duplicate-row substance. The FAIL branch can pair the hypothetical 9 with the assertion that the actual count was six. It checks no old→new association, no positive assertion, no correct Round-63 attribution within that block, and no SCORECARD correction row. The exact-phrase negation and unrelated-round controls independently demonstrate the assertion/mention and attribution holes.

**Smallest safe correction, not applied:** retain the successful bare-token pin, preserve these three new forcing negatives, and bind an explicit affirmative correction record's round/item/old→new/unit/receipt association in both named records. Validate the numeric tuples against the frozen count/receipt evidence rather than widening windows or adding a blacklist of this fixture's negation words. Such a bounded record check still must not be advertised as arbitrary natural-language semantic verification; contradictory explanatory prose/provenance needs explicit content review. Only an authorized receipt-forced pre-data revision may change the frozen instrument. Calibration and counter operability are impacted; this is a fixable proof defect, not grounds to weaken a counter leg or accept an axis trade.

### Actual rev2 base output — all seven FAIL

```text
CANONLOG FAIL r64_at=-1 stray_has_r63=True points_at_stray=False prior_rounds=0
PTRS FAIL score_dead=True stray_dead=True o_fixed=False c_fixed=False
HISTOGRAM FAIL tiers={'A': 13, 'B': 11} correction_present=False
DISPO FAIL items5_7=False s687_flip=False s693_kind=True
REVNAMES FAIL missing=['8d2041fa', '38ec1316', '0c892ce', '80ff34c', 'final-measures-c.txt', 'final-measures-o.txt', 'rev-separability.txt', 'census-end.txt']
NITS FAIL seat_reports_nit=False duplicate_url_nit=False fail_legs_nit=False
R63SEP FAIL result_cited=False dep_class_named=False
ACCEPT-CA-64: FAIL
exit=1
```

Assigned item 3 is therefore observed for rev2, not inferred from rev1. Assigned item 4's historical hazard findings D3/D4 stand: rev2 changes NITS, not PTRS/provenance or historical records. No historical audit, source counter, or production-tool run was repeated for this postscript.

## Late handoff — later byte state, peer-executed evidence only

After this seat completed its pinned attacks, RevVerifyCa reported a further NITS revision, also called “revision 2,” SHA-256 `7319ff4b9c7eb2cd23f866eb4db62d469a539b8dd99b8326fb6bae8f1cb0d4c5`. I read `.ufo/waves/round-64/w2/RevVerifyCa.md:9-79,103-128`; I did **not** rerun a counter, re-audit the lane, or patch source for this late note.

The peer's executed final-pin evidence supersedes the earlier `a8088092` result **for the reproduced wrong-substance fixture**: it now NITS-fails, as do bare tokens and a vacuous phrase list; the peer also records all-seven-base-FAIL and a working-tree 7/7 PASS. The stricter form requires a labelled `Round-63 numeric corrections:` line containing all three exact old→new phrases. The peer explicitly did not rerun this seat's original negated/out-of-scope fixtures on the later bytes; do not promote those outcomes to independently executed evidence.

The semantic boundary remains demonstrated at the later hash by the peer's two **new executed** controls: the exact labelled correction sentences followed by “quoting a false proposal; no measured correction was made,” and the same sentences attributed to a hypothetical round and expressly not claimed for Round 63, both NITS-pass (`new-mut-quoted-denial.txt`, `new-mut-attributed.txt` in that report). Those are peer-executed results, not additional runs by this critic. The remaining limit is assertion/mention and attribution, not the earlier bare-token or 120-character pairing weakness. A shape pin must not be described as proof of arbitrary prose semantics; the canonical judge retains interpretation of the frozen repair claim.

**Provenance correction:** future handoff must identify the counter by hash. `a8088092…` and `7319ff4b…` are distinct instrument states sharing the “revision 2” label. Regularize their distinct stamped pre-data revisions and forcing receipts before claim measurement; do not erase the superseded false-pass evidence. Historical hazards D3/D4 are not resolved by a NITS-only change.

Report: .ufo/waves/round-64/w2/CriticRevCa.md
