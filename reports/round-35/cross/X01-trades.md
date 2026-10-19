- Seat: X01 | critic | cross | date 2026-10-19 | baseline 4a7aede

# X01 — trade hunter across C / O / A

Mission (`reports/round-35/targets.json`, seat `X01`): "Trade hunter across C/O/A."
Out path `reports/round-35/cross/X01-trades.md`. Claim under hunt: `cross`.

This is a **trade register**: every place where a declared axis-move buys one axis at a
cost on another, with the gain, the cost, the evidence and the owner. A trade is
**reported, never averaged into an accept** (`REGIMEN.md`, per-round contract). Nothing
here is an axis verdict, round acceptance, or a promotion/canon/clearance/closure
statement — it is NON-CANON engineering evidence for the integrator's per-axis judging.

Dependency state: at this seat's first cut the round directory held the pre-dispatch files
plus 17 landed fragments (C11, C15, C16, K03, O08, O10, A05, A06, A09, A10, A11, R06,
S01, S02, S03, S05, X02); §4 reconciles the further fragments that landed while this seat
wrote. The C-entry drafts (C01–C10), the O patch drafts (O01–O04),
the A slices A01–A04/A07/A08 and the review fragments R01–R05/R07–R09 were **not on
disk**; every trade below is therefore measured against the *declared* claims
(`reports/round-35/claims.json`) and live bytes at HEAD, and the ones that can only be
settled on the delivered revision are re-listed under `## Owed`.

## 0. First-hand measurements (this seat's own runs at HEAD `4a7aede`)

All commands from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.
No `reports/round-*/run-validation.py` executed (F-C13-1); no `--freeze` executed; the
renderer was run only in non-freeze modes and its write contract is "a fresh directory
under `TMPDIR`" (`tools/exercise-handoff-e2e.py:93-94`), confirmed by
`git status --porcelain` → `?? reports/round-35/` only.

| # | command | observed |
|---|---|---|
| M1 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | **exit 1**, stdout empty, stderr a raw traceback ending `KeyError: 'reports/round-20/handoff/claims-map.md'` raised at `tools/exercise-handoff-e2e.py:3822` in `v3_exercise` |
| M2 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | **exit 0**; `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` |
| M3 | `python3 -B tools/exercise-handoff-e2e.py --selftest` (the bare command declared at `claims.json:47`) | **exit 0**, header `selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0) plus 17 controls:`, `grep -c '^  - '` = 18; the control text names "the 21 read-set files" → the **v1** selftest |
| M4 | `python3 -B -c` probe: import the renderer, compare `set(V3_READ_SET)` against the r6/r7 baselines' `inputs` | live 58 / r7 58 / r6 58; **r7 vs live: difference empty in both directions**; r6 vs live: baseline-only `['reports/round-20/handoff/claims-map.md']`, live-only `['reports/round-34/handoff/declared-in-r7/claims-map.md']`; renderer **not** a member; `corpus/knowledge` members = the contract file only; no `README` member |
| M5 | `sha256sum tools/exercise-handoff-e2e.py` | `34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9` — equals `reports/round-34/handoff/repin.json:12` `surface_sha256_after` and O08's B4 pre-patch value |
| M6 | `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md \| wc -l; done`; `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | 21/19/18/29/20/94 = **201**; inventory `totals.files 201`, `marker_occurrences 655`, `raw_lines 717`, `lines 36395` |

Line anchors for the defect (read, not guessed): `:3819` computes the drift set with a
tolerant `assembly.digests.get(rel)`; `:3822` is the message-formatting subscript
`assembly.digests[rel]` that raises; `:3823` is the designed
`raise Failed("E2E-DIGEST", …)`. `:4485-4486` — `--profile` **default is `v1`**;
`:4524-4525` dispatch to `v1_selftest()`, `:4563-4564` to `v3_selftest()`.

## 1. Trade register

### T1 — REAL, decidable now. Operability gain vs two filed/declared readings (exit-code choice)

- **Gain:** the r6-row replay stops crashing and emits a named diagnostic (claim O).
- **Cost:** whichever class the O block lands, one of two *immutable* readings is
  superseded, and the round must say which:
  - `reports/round-34/handoff/repin.json:19-21` files the r6-row control at `"exit": 1`
    and states "the designed E2E-DIGEST leg is unreachable for this class".
  - `reports/round-35/claims.json:48` declares the command as
    "`… --baseline reports/round-30/handoff/declared-in-r6/expected.json` (expect: exit 1,
    named diagnostic)".
- **The two landed fragments disagree on the outcome.** O08 §4 argues exit **2** is
  "convention-correct" and writes the leg to accept `{1, 2}`; S02's L1 requires exit **1**.
  Exit 2 contradicts both readings above (repin's filed `exit: 1`; claims.json:48's declared
  expectation) and would need a named deviation row (O08 §4 already anticipates this).
- **Live-code evidence for the exit-1 route being the *designed* one:** the drift set is
  already computed correctly at `:3819`; only the reporting line `:3822` throws; the next
  line `:3823` is the designed `E2E-DIGEST` refusal. The named member's file still exists
  on disk (`reports/round-20/handoff/claims-map.md`, 24 888 bytes, mtime Oct 18 10:11), so
  the exit-2 class `E2E-ARTIFACT` ("missing/unreadable read-set file", docstring `:92`)
  would *misdescribe* the condition — nothing is unreadable; the member left the read set.
- **Owner/route:** O01–O04 + S04's validator legs. The claim text permits either
  ("E2E-READSET or the renderer's existing diagnostic convention", `claims.json:45`), so
  this is a decision to **name**, not a defect. Cheapest no-trade option: fix only the
  formatting line so the existing `E2E-DIGEST` raise fires — exit stays 1, no new code
  vocabulary, both readings stay reproducible, and the diagnostic text must then say
  "unresolvable / no longer in the read set", not "changed" (K03 §3: the bytes did not
  change).

### T2 — REAL. Operability gain vs the claim's own instrument (selftest profile)

- **Gain:** two new controls covering the superseded-row refusal and the preserved
  E2E-DIGEST path.
- **Cost:** the claim's declared counting command is the **bare** `--selftest`
  (`claims.json:47`), whose profile default is `v1` (`:4485-4486`) — measured 17 controls,
  none touching `v3_exercise` (M3). The defect lives in the v3 path, and O08's O2 leg
  measures `--profile v3 --selftest` (39 controls pre-patch, N ≥ 41 post-patch). S02's L2
  instead expects the *bare* command to print "plus 19 controls". The two landed fragments
  cannot both be right after the patch: if the new controls land only in `v3_selftest`,
  S02-L2 fails and the claim's own command shows no deliverable; if only in `v1_selftest`,
  O08-O2 fails.
- **Owner/route:** integrator + O02. Either land the two controls in both selftests (the
  v1 mirror at `:1440` carries the identical unsafe subscript and is latent only because
  the v1 baseline is a subset of `V1_READ_SET` — K03 §2), making the declared bare command
  truthful at 19 controls; or keep them v3-only and (a) correct S02-L2, (b) have the
  validator use `--profile v3 --selftest`, (c) record the deviation from `claims.json:47`.

### T3 — REAL, mitigated in draft. Coverage gain vs the README's present-tense readings

- **Gain:** +6 culture-material / +4 myth-symbol, 201 → 211.
- **Cost:** five present-tense surfaces go stale at once in `corpus/README.md`: the
  revision 1.9 block (`:3-15`), `## myth-symbol/ (19)` (`:147`), `## culture-material/ (18)`
  (`:169`), `Total knowledge entries: 201.` (`:469`) and the counts footer `(total 201
  files; directory totals 21/19/18/29/20/94)` (`:471-473`). The lane has a documented
  instrument blind spot for exactly this class: the round-27 sweep "checks rows, section
  headers, row topics and the totals line, but never reads the counts footer, so it went
  green over a stale claim" (`corpus/README.md:27-31`); the footer leg exists only in
  `reports/round-28/readme/sweep.py`.
- **Mitigation present:** C11 drafts all five edits (E1–E5 + row generator) and proves the
  procedure on a synthetic +10 tree with negative controls (C11 §4: 211 rows vs 211 files,
  `footer_ok True`, `header_drift {}`; controls: a deleted row → exit 1, a reverted totals
  line → exit 1). Residual risk is integration-only: applying a *subset* of the five edits
  (rows + totals without the footer) re-opens the round-28 defect class, and the acceptance
  instrument is a filed round-28 artifact that must be run from the repo root and its
  reading recorded in the round record.
- **Secondary, to-verify:** the inventory's non-`files` totals move with the new entries
  (M6 baseline: `marker_occurrences 655`, `raw_lines 717`). The claim pins only
  `totals.files == 211`; any validator leg that pins the other totals needs a post-landing
  re-measure, never the pre-landing number.
- **Owner/route:** C11/C12 + S01 + S04's validator legs.

### T4 — REAL, structural, partly mitigated. Adjacency gain vs scope (round-35's own landings are outside the A census)

- **Gain:** the bleed-scope audit of every r33/34 touched surface.
- **Cost:** the surfaces *this round* creates — 10 new corpus entries, the README
  revision-2.0 block, the renderer patch's new diagnostic wording — are outside the A
  census by construction: A09 §2 derives the census from the r33/r34 commit diffs
  (`139e3b6..da68a6d`, `da68a6d..4a7aede`, 13 surfaces, all r33/34). Claim A's
  `after_required` says "zero unfiled cross-domain bleed on the new/changed surfaces"
  (`claims.json:60`) where "new/changed" means *the last two rounds'* surfaces.
- **Mitigation:** C-block entry audits include a no-bleed check (C12's runbook) and R01/R02
  review the entries; R04/R05 review the patch. Residual: no language scan in this round
  covers the new diagnostic text or the new README revision block.
- **Owner/route:** integrator/S04 — either add a one-line language leg over the r35 landing
  surfaces to the validator, or state the scope limit in the A receipt so the adjacency
  verdict is not read as covering r35's own artifacts.

### T5 — REAL, mild. Adjacency gain vs its own stamp (PROVINCE "at HEAD")

- **Gain:** PROVINCE owns/refuses lists re-verified against the tree.
- **Cost:** every A fragment measures at `4a7aede` pre-landing (A09 §1, A11 §1). The
  post-landing tree has 211 files and a patched renderer. The owns list is partition-level
  (`PROVINCE.md:9-11` names the six directories) so +10 files inside named partitions
  cannot falsify it, and the renderer stays in-lane under "this lane's own gates"
  (A11 §1a) — the cost is only that the phrase "PROVINCE accuracy re-verified at HEAD"
  (`claims.json:64`) will be read against a *later* HEAD than the one measured.
- **Owner/route:** S03/S04 — name the stamp (baseline `4a7aede`) in the receipt, or
  re-run the owns-list census after C/O land (one `ls`-per-partition command, M6).

### T6 — REAL, scope trade. Operability gain vs regression surface (the v1 mirror + the one-directional leg)

- **Gain:** one class of unhandled crash closed.
- **Costs of the two scope choices:**
  - *Narrow* (only `:3822`): the identical unsafe subscript at `:1440` stays (latent — the
    v1 baseline is a subset of `V1_READ_SET`, K03 §2), and S02-F1's direction-A gap stays:
    a live read-set member the baseline never pinned is silently unchecked while the record
    text at `:3824` claims `len(V3_READ_SET)` compared.
  - *Wide* (both directions, both sites): a wider refusal surface that must remain a no-op
    on the r7 chain.
- **Evidence the wide option is safe:** r7 baseline vs live read set is empty-difference in
  both directions (M4, 58/58), so a two-direction membership check provably cannot change
  the r7 chain's result; the regression leg M2 (exit 0, `packet_sha256=45f57132…`) stays
  checkable.
- **Owner/route:** O-block/integrator. Not adopting the wide option is acceptable only if
  the narrow scope is *named* (S02-F1 has an owner), not silently left.

### T7 — REAL, minor, mitigation exists. Operability gain vs a filed digest reading

- **Gain:** the patch.
- **Cost:** `reports/round-34/handoff/repin.json:12` records
  `surface_sha256_after: 34c85f57…` for the renderer, which is the live file's digest today
  (M5). The patch necessarily makes that filed reading stale, and round-34 bytes are
  immutable — no in-place correction is possible or permitted.
- **Mitigation:** O08's O5 static leg already requires the post-patch renderer sha to be
  recorded in the receipt. The trade is discharged by *stating the supersession*, not by
  repairing the filed row.

## 2. What this puts on the O block and the validator (actionable)

1. Decide the exit class and **name it**: exit 1 keeps `repin.json:20` and
   `claims.json:48` reproducible; exit 2 requires an explicit deviation row plus the
   repin supersession note.
2. If `E2E-READSET` is a *new* code, extend the documented exit-code table
   (`tools/exercise-handoff-e2e.py:89-93`) — otherwise the tool's own contract drifts
   (O08 §3 makes this a static leg).
3. Reconcile the selftest profile with `claims.json:47` (T2), and decide whether the v1
   mirror `:1440` is fixed in the same patch.
4. Keep M2 byte-stable: exit 0 and `packet_sha256=45f57132…` (measured pre-patch).
5. Any two-direction membership refusal must be a no-op on the r7 chain — provable from
   M4's empty set difference; re-run M2 after the patch and compare.

## 3. Negative findings (no trade — checked, not assumed)

- **N1 — the r7 freeze is not exposed to either landing.** Live `V3_READ_SET` = 58 = the
  r7 baseline's 58 inputs, empty difference both ways (M4). The only `corpus/knowledge`
  member is the contract file; `corpus/README.md` is not a member; the renderer is not a
  member. So +10 entries in culture-material/myth-symbol and the renderer patch cannot
  drift the r7 baseline by digest. Guard (cheap, worth a leg): the C drafts must not touch
  a read-set member — the contract, `corpus/lessons/round-6-sources/{03,05,09,13}.json`,
  `reports/round-6/parent-reconciliation.json`, `reports/round-19/validation.json`,
  `reports/round-34/handoff/declared-in-r7/claims-map.md` — i.e. assert
  `git diff --name-only 4a7aede..HEAD` ∩ read-set = ∅.
- **N2 — the lessons index is not exposed to claim C.** `corpus/lessons/README.md:105`
  ("Rows: 33. Files: 33.") and `:305` ("146 files under nine directories") count only
  `corpus/lessons/**`; a `grep` for `culture-material|myth-symbol|201|199|200` over that
  file returns no lines. The +10 knowledge entries cannot drift it. Residual, outside
  claim C: filing the round-35 lesson file itself moves the 33 count — that is the
  integrator's filing step, governed by the open item `corpus/lessons/README.md:234`
  (Q-30-2).
- **N3 — no live gate auto-scans the corpus partitions.** `tools/gates/provenance-audit.py`
  expands *argv* paths (`:338-350`), and `tools/check-gate-battery.py` looks for
  `expected.json`/`*.expected.json` under a baseline root (`:468-475`); the other gates
  reference `corpus/knowledge/**` files as spec text, not as globbed inputs. Adding ten
  `.md` entries therefore trips no live gate — the coverage gain carries no hidden
  operability cost there.

## 4. Post-cut reconciliation (fragments that landed while this seat wrote)

Seventeen further fragments appeared after §0–§3 were drafted. Re-read for the trades
above; this section records where each trade stands against the landed designs.

**T1 — resolved in the exit-1 direction, with a new cost already stated by the designer.**
`op/O02-controls.md:51-52` fixes the interface as `(EXIT_FAIL, "E2E-READSET", records)` —
exit **1** — and `:55` requires `E2E-READSET` in the docstring census (`:90-92`);
`review/R04-o-review.md` §3 recommends the same shape (S2) and rejects S1 ("keeps a false
statement"), S3 (evaluates the superseded member as if live and prints a false parity
record) and a broad `except KeyError` (relabels unrelated faults, S4). So `claims.json:48`
and `repin.json:20` stay reproducible and O08 §4's exit-2 route is declined. Residual, to
be stated in the O receipt: `repin.json:21`'s filed phrase "the designed E2E-DIGEST leg is
unreachable for this class" now coexists with a *new* code `E2E-READSET`; the round must
name E2E-READSET as the sanctioned successor for this class, or the r34 finding and the
r35 fix read as contradictory (R04 §5 carries the supersession obligation;
`repin.json:45-48` is the `reading_changed_not_verdict` precedent).
**New cost, stated by the designer:** `O02:69` hoists the `handoff-v3: {code}: {detail}`
print out of the `not args.quiet` guard (`:4603`), so a *failing* `--quiet` v3 run gains a
stdout line. Checked: the only filed pin of the r6 replay is `repin.json:19-21`, which
records exit + mechanism, not stdout/stderr digests, and the filed validators parse
`packet_sha256=` from *successful* quiet runs — the cost is bounded and discharged by
stating it in the receipt.

**T2 — still open, now a three-way disagreement.** `O02:108` inserts the new controls
(m13a/m13b) inside `v3_selftest`; `O08`'s O2 leg measures `--profile v3 --selftest`
(39 pre-patch, N ≥ 41); `S04-integration-draft.md:400-413` flags exactly this gap
("`claims.json:47` omits `--profile v3` while its threshold requires the v3 [suite]") but
its own leg at `:568` still expects the bare `--selftest` to print "control count >= 19
(was 17)" — the bare command runs the v1 suite (`:4485-4486`; M3 = 17 controls). The
integrator must pick one: land the controls in both suites (the v1 mirror `:1440` carries
the identical pattern; R04 §3 leaves the v1-only-vs-both choice to the integrator), or keep
them v3-only and correct S04's leg plus the declared counting command.

**T6 — narrowed by R04, and the S02-F1 recommendation now conflicts with it.** R04 §2
widens the class to nine filed v3 baselines (r20, r22×2, r26×3, r27, r28, r30 — all
`unresolvable=[round-20 claims-map]`; four reproduced, five predicted), so the hardening's
blast radius is nine rows, all changing from traceback to named refusal — none is the r7
chain, so the regression floor M2 is untouched. R04 then forbids the live-only direction of
the set check ("must not start reporting live-only members"), while `S02-o-receipt.md` §3
recommends refusing on set inequality in **either** direction and making the `:3824`
record state the number actually compared. Minimal-harm resolution (improves count honesty,
adds no refusal class, harms no axis): keep the refusal one-way per R04 and change only the
count text — `len(V3_READ_SET)` → the number of baseline members actually compared. If the
integrator declines, S02-F1 must be filed as a named finding with an owner, not silently
left.

**T7 — unchanged and already mitigated:** `O08`'s O5 static leg requires the post-patch
renderer sha to be recorded; `repin.json:12`'s `34c85f57…` becomes a superseded filed
reading, stated not repaired.

**New corroboration for N1 (no trade):** `O04-regressions.md` §1 classifies the r6 row as
`unresolvable: 1 / drifted: 0 / matched: 57`, and R04 §3's S3 shows why measure-on-demand is
not a fix — the superseded member's bytes are unchanged, so it would evaluate as live and
print a false parity record. Both agree with M4's set measurement.

## Owed

Missing dependency fragments at this cut (all paths under `reports/round-35/`). Still
absent after the post-cut scan: the entry drafts `cov/C01-entry-1.md`, `cov/C04-entry-4.md`,
`cov/C07-entry-7.md` … `cov/C10-entry-10.md` and the auditor `cov/C13-audit-1-5.md`; the O
patch set `op/O01-patch-draft.md` (the binding patch), `op/O03-isolated-verify.md`,
`op/O05-verify.md`, `op/O06-receipt.md`, `op/O07-gap-fill.md`, `op/O09-gap-fill.md`,
`op/O11-verify-2.md`; the A slices `adj/A02-adoption-tool.md`, `adj/A03-examples.md`,
`adj/A04-skill-agents.md`, `adj/A08-audit-draft.md`; the reviews `review/R01-c-review.md`,
`R02-c-review.md`, `R05-o-review.md`, `R08-cross-review.md`; `plan/P01-c-plan.md`.
Landed and folded in §4: `op/O02-controls.md`, `op/O04-regressions.md`,
`review/R04-o-review.md`, `scribe/S04-integration-draft.md`.
Post-landing re-measurement this seat cannot do at HEAD, to be closed by the integrator
against the delivered revision:

1. T1/T2/T6 — the post-patch exit code and diagnostic token at the r6 replay, the selftest
   profile that actually prints the two new controls, whether `:1440` was fixed, and
   whether the `:3824` count text was corrected or S02-F1 filed as a named finding.
2. T3 — the README's five surfaces re-read by the r28 sweep after C11's edits land
   (`footer_ok True`, `totals_line 211`, `header_drift {}`), plus the post-landing
   inventory totals.
3. T5 — the owns-list census re-run on the delivered tree (211 files, patched renderer).
4. N1 — the read-set-membership guard against `git diff --name-only 4a7aede..<delivered>`.

## Citations

- `reports/round-35/claims.json:21-35` (claim C), `:38-51` (claim O), `:54-65` (claim A);
  `:45`, `:47`, `:48`, `:51`, `:60`, `:64`.
- `reports/round-35/targets.json` (seat X01 mission/out; shared rules).
- `reports/round-35/scout/K03-keyerror-path.md` §1-§3 (traceback, `:3822`/`:3823`/`:1440`,
  membership-vs-content, v1 latent).
- `reports/round-35/op/O08-validation-legs.md` §1 B1-B6, §2 O1/O2/O5/O6, §3, §4 (exit-code
  ambiguity), `## Owed`.
- `reports/round-35/scribe/S02-o-receipt.md` §3 (S02-F1), §4 L1/L2/L3/L5, §5-§6.
- `reports/round-35/cov/C11-readme-delta.md` §0-§5 (five edits, synthetic +10 proof,
  drafted revision 2.0 block).
- `reports/round-35/adj/A09-receipt.md` §1-§2 (census from the r33/34 commit diffs);
  `reports/round-35/adj/A11-verify-2.md` §1a-§1b (PROVINCE at HEAD).
- `reports/round-35/scribe/S01-c-receipt.md` §1-§2; `scribe/S03-a-receipt.md` §1.
- `reports/round-35/op/O02-controls.md` §1-§3 (chosen shape S2, exit-1 interface, `--quiet`
  print hoist, m13a/m13b placement in `v3_selftest`); `op/O04-regressions.md` §0-§2
  (r6-row classification `unresolvable 1 / drifted 0 / matched 57`).
- `reports/round-35/review/R04-o-review.md` §1-§3 (nine-baseline census, shapes S1-S4,
  one-way direction, v1 twin) and §5 (integration obligations).
- `reports/round-35/scribe/S04-integration-draft.md:400-413`, `:568`, §6-§7 (claim-O legs,
  the `--profile v3` gap).
- `tools/exercise-handoff-e2e.py:89-94`, `:184`, `:1933-1934`, `:3819-3824`, `:1440-1441`,
  `:4485-4486`, `:4524-4525`, `:4563-4564`, `:4603`.
- `reports/round-34/handoff/repin.json:7-14`, `:15-21`, `:32-39`, `:50`.
- `reports/round-34/handoff/declared-in-r7/expected.json` (`inputs`, 58 members).
- `reports/round-30/handoff/declared-in-r6/expected.json` (`inputs`, 58 members).
- `corpus/README.md:3-15`, `:27-31`, `:147`, `:169`, `:469`, `:471-473`.
- `corpus/lessons/README.md:105`, `:234`, `:305`.
- `PROVINCE.md:9-11`.
- `tools/gates/provenance-audit.py:338-350`; `tools/check-gate-battery.py:468-475`.
- Commands: M1-M6 as tabulated in §0 (all run by this seat at HEAD `4a7aede`,
  `git rev-parse HEAD` = `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`).
