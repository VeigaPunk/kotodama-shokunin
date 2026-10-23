# CaReceipts — claim Ca receipt, instrument and reverse-hazard audit

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (jj-colocated; read-only git).
Base: `ff30a205c8d23b35f1ac533740121a955a9fda96`. Declaration: `097c21d`.
Scratch: `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/CaReceipts/` (snapshots, fixtures, saved outputs).
Reviewer only: no lane file, row, counter, record, index or jj state was modified; nothing committed.
No tool was installed or updated.

Axes named: **calibration** (correction prose vs filed measurements — primary), **operability**
(whether ACCEPT-CA-64 discriminates a repair from records-only prose, and whether it runs at all),
**coverage** (only the inputs this claim reads; no entry/row/support judgment).

LSP is **not mounted** on this seat (`read xd://lsp` → `No such tool: xd://lsp`; mounted: ast_edit,
debug), so no semantic `references`/`definition`/`diagnostics` pass was possible. The counter has no
code callers (only `claims.json:55`, wave-spec JSON and its own docstring name it); text checks are the
fallback and are not presented as semantic proof.

## 1. Instrument churn during the audit (five fingerprints, ~5 minutes)

```text
rev1  f222648e…  first read; same bytes w1 ReviewerCa/CriticCa attacked
rev2  a8088092…  first NITS rewrite (value↔context phrases, entry-scoped)
      63510c4d…  second rewrite, BROKEN: `NameError: name 'r64_log' is not defined`
final 7319ff4b…  fixed: r64_log defined; NITS requires the affirmative old→new record
HEAD 097c21d:reports/round-64/accept-ca.py = rev0 3a5a79d1… (CANONLOG needs >60 `## Round`; cannot PASS)
```

Runs on the lane (saved: `run-lane-rev2.txt`, `run-lane-rev3-crash.txt`):

- rev1 → **7/7 PASS**, exit 0.
- rev2 `a8088092` → **7/7 PASS**, exit 0 (`NITS PASS seat_reports_nit=True duplicate_url_nit=True fail_legs_nit=True`).
- broken `63510c4d` → five legs PASS, then `NameError: name 'r64_log' is not defined`, **no
  `ACCEPT-CA-64:` verdict printed, exit 1** (traceback only). It stayed broken for the ≥20 s I
  watched; it is superseded now.
- final `7319ff4b` (current) → **7/7 PASS**, exit 0:

```text
CANONLOG PASS r64_at=272051 stray_has_r63=True points_at_stray=True prior_rounds=56
PTRS PASS score_dead=False stray_dead=False o_fixed=True c_fixed=True
HISTOGRAM PASS tiers={'A': 13, 'B': 11} correction_present=True
DISPO PASS items5_7=True s687_flip=True s693_kind=True
REVNAMES PASS missing=[]
NITS PASS correction_record=True seat_reports_nit=True duplicate_url_nit=True fail_legs_nit=True
R63SEP PASS result_cited=True dep_class_named=True
ACCEPT-CA-64: PASS
EXIT=0
```

**There is still no Ca acceptance receipt on disk.** `reports/round-64/telemetry/` holds only
`dry-run-ca.txt` (rev0, six legs, committed at `097c21d`); no `final-measures-ca.txt` exists anywhere,
and claim Ca's `lands` list names no receipt path. The "rev2 full-run receipt" does not exist; both
revisions were run here instead.

## 2. Diff audit — `git diff ff30a205 -- LOG.md SCORECARD.md corpus/LOG.md`

```text
11  0  LOG.md          pure append (one Round-64 entry)
10  1  SCORECARD.md    1 filed row corrected in place + appended corrections block
3   3  corpus/LOG.md   3 filed lines corrected in place
```

`git diff --name-only ff30a205` lists no other tracked path beyond the declaration artifacts and
`corpus/SOURCES.md` (the S687 `mined → queued` flip for claim C, exactly one line). The in-place edits
are exactly routed defects 2 and 4; nothing unrelated is touched.

| defect (r63 spotcheck §6) | where the round-64 bytes name it | independent check |
|---|---|---|
| 1 canonical LOG | `LOG.md:4152` heading, :4154 canonical/stray sentence | base `LOG.md` has 0 `Round 6[34]` headings; stray has `## Round 63` |
| 2 dead pointer | `LOG.md:4158`; SCORECARD r63 operability row; `corpus/LOG.md:2,3` | base SCORECARD cites `final-measures.txt` 14×, stray 2×; dead file absent at base; `-o`/`-c` both exist (`git cat-file -e`) |
| 3 tier histogram | `LOG.md:4159`; SCORECARD corrections row | awk over `ff30a205:corpus/SOURCES.md` → `A=13 B=11`; S702 tier `B` kind `docs` |
| 4 r62 items 5–7 | `LOG.md:4156`; `corpus/LOG.md:7` erratum | `resid/KotodamaR62.ResidRerunO.md` + `ResidRerunD.md` exist; `ResidRerunO.md:88` `32 checks, 0 failures`; R63-M2 at `corpus/lessons/round-63.md:57` is "stale instrument pins" |
| 8 revisions | `reports/round-63/telemetry/revisions.txt` (untracked); `LOG.md` bullet | mapping correct, prose false — §3 |
| 9 numeric nits | `LOG.md:4160`; SCORECARD corrections row | 47 `.md` reports under `.ufo/waves/round-63/w1/`; W04 = 27 (r63 `census-end.txt` **and** `reports/round-64/telemetry/census-start.txt`); dry-run legs GEN/ORDER/BOUND/REDIRECT/MALFORMED/GZIP/TRUNC/TIMEOUT/REVIEW = **9** (`grep -c FAIL` = 10 only because the verdict line also matches) |
| 10 separability | `LOG.md:4161`; SCORECARD corrections row | `rev-separability.txt` prints `SEPARABILITY: 2 findings`, `exit=1`, `C->REC`, `O-><base>` |

## 3. `reports/round-63/telemetry/revisions.txt` vs reality (sha `56aea045…`, unchanged all audit)

Mapping correct: `8d2041fa` is the claim-C land commit; `final-measures-c.txt` added by `0c892ce`;
`final-measures-o.txt` added by `80ff34c`; `80ff34c..38ec1316` touches only
`separability-manifest.json`; `accept-o.py` blob `934bb052143e787ae0feb572679e66dfcf6300ff` at
`0c892ce`, `9e9885d`, `80ff34c`.

Three prose clauses are contradicted by the repository:

- `:12-13` "the receipt's 10 legs and the commit subject both name it" — `final-measures-c.txt` has
  ten leg lines, the verdict and `exit=0`, and **zero** occurrences of `8d2041fa`
  (`grep -nE '8d2041fa|revision'` → no match). Only the commit subject names it. That is precisely the
  round-63 defect-8 omission this file is supposed to repair.
- `:13-14` "reports/round-63/accept-c.py is unchanged between 8d2041fa and the records commit" —
  blob `4a8791ba…` at `8d2041fa` vs `e6322538…` at `0c892ce` and `80ff34c`. It changed.
- `:17` rev-separability "recorded by 38ec1316" — `git log -- path` shows the file added at `0c892ce`
  and last modified at `80ff34c` (5+/2−); `38ec1316` touches only the manifest. Only that commit's
  *subject* mentions the file, contradicting the file's own stated basis ("added or last carried").

`REVNAMES` cannot catch any of these (unordered token membership), so the claim passes while its own
defect-8 repair file misstates provenance.

## 4. NITS control matrix (executed; base bytes + appended records-only prose)

| instrument | CriticCa generic `W04` append | label-only "47 seat reports / 27 duplicate-URL rows / 9 FAIL legs / No measured correction" | honest land |
|---|---|---|---|
| rev1 `f222648e` | NITS **PASS** (w1 CriticCa; reproduced by RevVerifyCa) | PASS (holds by construction) | PASS |
| rev2 `a8088092` | NITS **FAIL** (executed) | NITS **PASS** — false pass (`/CaReceipts/fx2`) | PASS |
| final `7319ff4b` | NITS **FAIL**, `correction_record=False` | NITS **FAIL**, `correction_record=False` | PASS |

Final NITS requires the affirmative record line
`- **Round-63 numeric corrections:**` with `47 seat reports landed, not 45`,
`W04 covers 27 duplicate-URL rows, not [just ]S650/S651`,
`ACCEPT-O-63 dry run had 9 FAIL legs … not 6`. Both records-only controls now fail the leg. Residual,
inherent to any text leg: an append that copies that exact affirmative sentence passes, because the
sentence *is* the correction content; the leg cannot recompute 47/27/9. It is also exact-phrase
brittle — an editorially improved correction (e.g. comma or wording change) would fail a true repair.
Disclose; acceptable at this granularity.

## 5. Reverse hazard — is any filed row now false?

- SCORECARD r63 operability row now cites `final-measures-o.txt`, which exists at base and prints
  `ACCEPT-O-63: PASS` / `exit=0`. Not false.
- `corpus/LOG.md` O/C pointers resolve; the erratum ("R63-M2 concerns stale instrument pins") matches
  `corpus/lessons/round-63.md:57`.
- The LOG's S687 sentence ("enacted in `corpus/SOURCES.md` by this round's claim C land") is **true in
  the worktree**: `corpus/SOURCES.md:642` status `queued`, used-by `—` (the whole file diff is that
  line). It was premature at w1 (CriticCa item C); integration must keep that flip or the sentence
  becomes false.
- The corrections block's cross-references are true: the coverage row does say "A 14 / B 10"; "Both
  exist at `ff30a20`" is true (`git cat-file -e`); the coverage row count of 47 holds.
- **No filed row is made false by round-64 bytes.** One inherited overstatement remains:
  `SCORECARD.md:1095` "24/24 is the selftest at `454a2dc` **only**", while `eb0a331` carries the same
  blob `fc696428…`. It predates this round and is outside Ca's routed list — named, not counted.

## Findings by severity

### HIGH C1 — `revisions.txt` asserts receipt provenance the receipts do not carry
`:12-14` and `:17` (§3) are checkably false. This is a Ca land and the defect-8 repair; it was left
unchanged by the only Ca seat in `w2-spec` (`B2ExecCaRepair`: "Those files were left unchanged"), and
no other seat owns it. Impact: calibration — the repair repeats the routed defect's false premise, and
`REVNAMES` is blind to it. Fix (L1, pre-data): correct the three clauses in place or append an
erratum; keep the revision map.

### MEDIUM C2 — the acceptance instrument mutated through a broken state with no revision bump
Three distinct byte streams carried the label "revision 2" within ~5 minutes (`a8088092`, `63510c4d`,
`7319ff4b`); `63510c4d` crashed with `NameError` and printed **no verdict** (fail-closed by exit 1, not
by a leg). The docstring still says "revision 2". Any Ca receipt must cite the content sha, not the
label. Recommend the L1 stamp the final bytes (`7319ff4b`) as rev3 with this audit's control evidence.

### MEDIUM C3 — no committed Ca receipt; the passing instrument is uncommitted
`097c21d` carries rev0, which cannot pass; rev1/rev2/final exist only as worktree bytes. No receipt of
any full Ca run is committed, and the final revision's forcing controls are three wave reports, not a
telemetry receipt. Claim Ca's `lands` list has no receipt path. Integration should commit the final
counter and a control receipt (records-only controls → NITS FAIL; lane → 7/7 PASS) with the revision,
so the predicate is reproducible from committed bytes.

### LOW C4 — token-membership legs cannot bind associations
`REVNAMES` (`need` tokens anywhere in one file), `DISPO` (`item 5/6/7`, `S687`+`queued`, `S693`+`docs`
anywhere in a 276 KB log) and `R63SEP` (`REC` + `record dependency`, `SEPARABILITY: 2 findings` +
`exit=1` anywhere) test presence, not correspondence; a swapped receipt↔revision pair or a duplicate
sentence in another entry would still pass. Frozen and disclosed.

### LOW C5 — filed bytes rewritten rather than errata appended
`corpus/LOG.md` 3/3 and `SCORECARD.md` 10/1 replace filed historical lines. The replacements resolve
and are the routed repairs, but strict append-only correction discipline is violated, and a frozen
`PTRS` that must delete the dead string can never pass with the original bytes preserved. Surface to
the judge (same conflict as CriticCa item D); not counted against this claim.

### INFO C6 — "dead pointer removed" scope
True for the round-63 SCORECARD block (its `final-measures.txt` occurrence removed; the 13 remaining
are rounds 51–58, legitimate) and for the stray log (2 → 0).

### INFO C7 — `HISTOGRAM` registry half reads the base
`accept-ca.py` recomputes tiers from `ff30a205:corpus/SOURCES.md`, so that half is insensitive to the
current registry by design; the correction half is a whole-SCORECARD substring.

## Residual risk and verification gaps

- LSP unavailable; no semantic reference/definition analysis. The counter has no code callers.
- No round-63 acceptance counter was re-executed; round-63 claims rest on committed receipts.
- The 27-W04 figure is corroborated by two committed census receipts (r63 `census-end.txt`, r64
  `census-start.txt`), not a fresh census.
- Instrument churn: only the shas listed in §1 were audited. `run-lane-rev2.txt` and
  `run-lane-rev3-crash.txt` preserve the two non-final observations; the final run is reproduced above.
- Reverse-hazard scope: tracked bytes in `LOG.md`, `SCORECARD.md`, `corpus/LOG.md`,
  `reports/round-63/telemetry/revisions.txt`, plus `corpus/SOURCES.md` for the S687 sentence. Wave
  artifacts under `.ufo/` were not audited.
- NITS controls use synthetic base-byte fixtures; they test instrument discrimination, not the honest
  land, whose three values are independently verified in §2.

Report: .ufo/waves/round-64/w2/CaReceipts.md
