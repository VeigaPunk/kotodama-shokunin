- Seat: R02 | reviewer | claim cross | date 2026-10-19 | baseline ac47c78

# R02 — second adversarial review of both r42 blocks

Independent read-only review of claim O (N6 wrapped-field extractor fix) and claim C
(myth-symbol +4). Every number below was re-derived by this seat on the live tree at
`ac47c78` (`git log --oneline -3` → `ac47c78`; working tree clean except untracked
`reports/round-42/`). No filed byte edited; no `run-validation.py` executed; no git,
network or install action. Commands run 2026-10-19, repo root,
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

## Verdict

**Claim O — the premise and the before-state verify; the after-state as written has two
false-green traps and one unsatisfiable threshold.** The defect host, the wrapped field
and the "0 vs 4" gap all reproduce. But (i) the fix's join rule is unspecified and the
obvious join — the host's *own* `field_block` idiom — still mangles the token; (ii) the
"4 named targets" phrase hides that only 2 exist; (iii) the after_required threshold
("reproduces the r39 policy's arithmetic") is falsified by the live tree state (220
entries, not the policy's 212). One lawful durable host exists and the mission's
candidate list does not name it.

**Claim C — the partition, the total and the sweep all verify; the C06 mission's vector
bytes are arithmetically wrong and will make the README sweep red.** The correct vector
is `25/27/25/29/24/94`, not the mission's `25/23/27/25/24/94`.

## Claim O — checks performed

1. **Defect host confirmed.** `reports/round-19/audit/entry-audit.py:75` is
   `m = re.search(r"^- couples:\s*(.*)$", text, re.M)` inside `couples_targets`
   (`:74-96`); token regex `MDREF_RE` at `:31`, one-level brace expansion `:33-42`. A
   single-line capture cannot read a wrapped field. Matches `Ca04-verify.md` D1.
2. **The wrapped field is real and is the only one.** `corpus/knowledge/linguistics/
   phonetics-phonology.md:72-77` is 6 physical lines. My probe (re-implementing
   `entry-audit.py:75` + `:31`): single-line capture at `:72` yields value
   `'language (this file, core method); myth (divine/true names, taboo'` and **0 tokens**;
   the 6-line block yields **4** tokens. Consistent with `Ca04-verify.md` D1 and the v2
   queue row `N6-couples-extractor-wrapped-field`
   (`reports/round-40/op/defect-queue-v2.json:362-369`).
3. **Trap A — de-hyphenation creates a NEW phantom.** The continuation `tone-\nprosody.md`
   spans the `:76-77` line break. A naive soft-hyphen strip (`-\n\s*` → ``) yields
   `toneprosody.md` — a token that exists nowhere, i.e. the "fix" would mint a phantom
   instead of reading the real one. Measured: strip → `['sound-change.md',
   'toneprosody.md', 'sound-symbolism.md', 'writing-systems.md']`. A fix that joins by
   deleting the hyphen is **wrong**.
4. **Trap B (the serious one) — the host's own idiom still mangles the token.** The
   natural model for a block parser is the already-shipped
   `tools/gates/provenance-audit.py:244-260` `field_block`, which joins continuations with
   `" ".join(part for part in parts if part)` (`:259`). I imported that module and called
   `field_block(lines, "couples")` on the live file: it returns `present=True` and content
   containing `...; prospective sibling files: sound-change.md, tone- prosody.md,
   sound-symbolism.md, writing-systems.md`. The regex `[A-Za-z0-9_./{},\-]+\.md` cannot
   match across the space, so it captures `prosody.md` — **still 4 tokens, still the
   wrong 4**. A patch that copies the host idiom would pass a naive "does it read the
   block?" test while reproducing the mangling: a false green. Only two join rules read
   the field whole, and both were measured: hyphen-aware (`out+s if out.endswith('-')`
   else `out+' '+s`) → `tone-prosody.md`; newline-and-indent strip with no space →
   `tone-prosody.md`. O01's fenced patch must specify the rule and O02/O05 must carry the
   space-join negative control, or the fix is unverifiable.
5. **"4 named targets" is 2 real + 2 phantom, not 4 real.** `ls` of
   `corpus/knowledge/linguistics/`: `sound-symbolism.md` and `writing-systems.md` exist;
   `sound-change.md` and `tone-prosody.md` do not. So the field reads 4 tokens, 2
   `direct` + 2 `unresolved`. The claim's `before` ("2 phantom attributions") is accurate;
   the mission's phrasing "4 named targets" is not, and a threshold reading "the wrapped
   field reads 4/4 targets" as *resolution* is unsatisfiable. It must be read as
   *extraction* (4 of 4 tokens captured). Flagged so the wave fixes the wording.
6. **The 2 phantoms are self-dispositioned by the field's own text.** The field opens the
   clause with `prospective sibling files:` — the two absent targets are declared
   prospective seeds, not broken references. This matches the C12 row-2 rule
   (`reports/round-35/cov/C12-audit-runbook.md:37`, cited at `Ca04-verify.md` D2): a
   dangling token is a blocker unless the same line documents it, then non-blocker. So
   the correct disposition is "documented prospective seeds", and the claim's "zero
   phantom attributions remaining or each dispositioned" is satisfied by the second leg.
7. **Live recount (this seat, 220 entries).** Read-only re-implementation over
   `corpus/knowledge/*/*.md` (220 files), two-tier resolution per `basename-couples-policy.md`
   §2 (Tier-1 three candidates; Tier-2 unique-basename over one partition level):
   - single-line extraction: refs **2607** → direct **2435** / fallback **166** /
     ambiguous **0** / unresolved **6**; distinct **400**
   - block extraction (hyphen-aware): refs **2611** → direct **2437** / fallback **166** /
     ambiguous **0** / unresolved **8**; distinct **403**
   - delta is exactly the wrapped field: +4 refs, +2 direct (`sound-symbolism.md`,
     `writing-systems.md`), +2 unresolved (`sound-change.md`, `tone-prosody.md`).
   The block set's 8 unresolved rows resolve to 7 distinct tokens: 3 never-written seeds
   at `corpus/knowledge/linguistics/language-contact.md:7` (`phonology-basics.md`,
   `naming-and-onomastics.md`, `honorifics-and-register.md`); the 2 wrapped-field phantoms;
   the X26-1 phantom `../linguistics/phonology-sanity.md` ×2
   (`verification/label-channel-routing-verification.md:14`,
   `synthesis/typed-label-routing-workflow.md` — the real file is
   `phonology-sanity-gate.md`); and the glob fragment `-gate.md`
   (`verification/gate-frozen-run-standard.md:15`), which §5.6 orders skipped, not counted.
8. **Trap C — the after_required threshold cannot reproduce.** `claims.json:19-22` says the
   corrected census "reproduces the r39 policy's arithmetic minus the phantoms" and
   `before` cites "the r39 policy's 2504 = 2335 + 163 + 0 + 6". That arithmetic was
   measured at **212 entries** (`reports/round-39/calib/basename-couples-policy.md` §5.5
   "212 files at adoption"; `Ca04-verify.md` check 1 Part 2 `entries=212 refs=2504`). The
   live tree is **220** — r39 landed 4 verification entries (212→216,
   `corpus/README.md` rev 2.2) and r40 landed 4 linguistics entries (216→220, rev 2.3).
   At 220 the single-line total is 2607, not 2504. So "reproduces the r39 policy's
   arithmetic" is falsified as written; the honest after-state is "re-derived at the live
   220-entry tree, with the +8-entry delta reconciled to the r39 212-entry reading". The
   wave must restate the threshold or the round will be reported rejected on a threshold
   that no correct fix can meet.
9. **Host durability — the mission's candidate list does not name a lawful host.**
   `grep -ln "couples" tools/harness/*.py` → empty: there is **no** couples checker under
   `tools/harness/`. The only `tools/` couples logic is `tools/gates/provenance-audit.py`,
   and it extracts the field for an `empty-couples` *presence* check (`:318-323`) — it does
   **not** resolve reference targets. Reference *resolution* exists only in filed round
   scripts (`reports/round-19/audit/entry-audit.py`, `reports/round-27/audit/entry-audit.py`),
   in the r35 fragment `reports/round-35/cov/C14-audit-6-10.md` (a record, not an
   instrument), and in the ephemeral `.scratch/c05/c05-audit.py` (r39 I-C05, filed
   non-durable by row `r39-ic05-resolver-durability`,
   `reports/round-40/op/defect-queue-v2.json`). `reports/round-1..41/**` is never-edit
   filed bytes, so O01's "fenced diff against the confirmed host" **cannot** land in place
   in `entry-audit.py`. The only lawful durable host is a **new** resolver under `tools/`
   (naturally `tools/harness/`), which also discharges the r40 A01 owed durability row.
   O01/O06 should say so explicitly; a patch framed as an in-place edit of r19 is
   unlandable.

## Claim C — checks performed

10. **Partition and total verified.** `ls corpus/knowledge/myth-symbol/*.md | wc -l` → 23;
    `corpus/README.md:196` → `## myth-symbol/ (23)`; README rows 220 vs files 220.
11. **Sweep is green at baseline.** `python3 -B reports/round-28/readme/sweep.py` →
    `rows 220 files 220`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`,
    `header_drift {}`, `totals_line 220 totals_ok True`, `footer_ok True`, footer
    `{"total": 220, "dir_totals": [25,23,25,29,24,94]}`, readme sha
    `d2eed26b30e8e62189d95446dae7d5503b6c6a398bb8e77348f878c947a5ac4f`.
12. **Trap D — the C06 mission's vector is arithmetically wrong.** `targets.json` C06
    specifies "vector `25/23/27/25/24/94`". The README's canonical partition order is
    `[linguistics, myth-symbol, culture-material, synthesis, verification, civilizations]`
    (`reports/round-28/readme/sweep.py:44-51`; footer live order echoed by the sweep). The
    current vector is `25/23/25/29/24/94` (sum 220). Landing 4 into myth-symbol must give
    **`25/27/25/29/24/94`** (sum 224). The mission's vector instead leaves myth-symbol at
    23, moves culture-material 25→27 and synthesis 29→25 (both wrong), and **sums to 218**.
    The sweep's footer leg compares `footer["dir_totals"]` to the live per-partition counts
    in that order (`sweep.py:179-190`), so a README built to the mission vector is
    sweep-RED. C06/C07 must use `25/27/25/29/24/94`; the totals line
    (`corpus/README.md:532` `Total knowledge entries: 220.`) → 224 and the footer
    (`:534-536` `(total 220 files; directory totals 25/23/25/29/24/94)`) →
    `(total 224 files; directory totals 25/27/25/29/24/94)`.
13. **Entry contract is uniform and checkable.** All 23 existing myth-symbol entries carry
    the three admission fields (`- topic:`, `- sources:`, `- couples:`) — grep count 3/3
    per file, all 23 — plus `- source:` / `- verified-at:` / `- recheck:` on the inspected
    sample (`myth-symbol/trickster.md:3-8`). C05's audit should read the four new entries
    against `corpus/QUALITY.md:1-20` items 1-5 (provenance, calibration, coupling,
    usability, canon hygiene) as prior rounds did.
14. **Caveat on claim C's evidence, not a defect.** C's `counting_commands`
    (`ls ... | wc -l`, the r28 sweep) are runnable by seats; O's sole counting command is
    the in-tree `reports/round-42/run-validation.py`, which does not yet exist
    (`ls reports/round-42/` → claims.json, targets.json, telemetry/) and which seats are
    forbidden to execute. O's seat-level evidence is therefore necessarily O03's synthetic
    recount + O04/O05 isolated verification; that is the plan and it is sound, but O cannot
    be marked verified from a seat — only the integrator's runner can close it.

## Cross-block notes

- **N6 is overloaded across r40 records.** The v2 queue's `N6` is the *extractor defect*
  (`defect-queue-v2.json:362`, `class: carried-with-owner`, owner "future resolver round").
  The r40 Ca03 receipt (`reports/round-40/calib/Ca03-receipt.md:88`) and the r40 R01/R02
  reviews use `N6` for a **different** item — the corpus couples-*phantom repair* rollup —
  and call the extractor D1 `N4` (`Ca03-receipt.md:86`) with D2 as `N5` (`:87`). O08's mission
  ("Queue-v2 N6 row re-class draft") must target the v2 row id
  `N6-couples-extractor-wrapped-field` and say so; conflating it with the receipt's N6
  rollup would file a wrong re-class.
- **The phantom-repair rollup has no v2 row.** My block recount reproduces all three
  phantom families (3 `language-contact.md:7` seeds, 2 wrapped-field phantoms, X26-1 ×2)
  and confirms no v2 row mentions `phonology-sanity` or `language-contact`. So r40 R02-1's
  finding stands at r42: the corpus-side repair dispositions remain unrowed. This round's
  O block documents the wrapped-field pair; the other three families stay owed.

## Owed

- **O01/O02/O05 (via integrator):** specify the join rule explicitly (hyphen-aware or
  no-space newline strip), and include the **space-join negative control** — the host
  `field_block` idiom (`tools/gates/provenance-audit.py:259`) is a false-green generator
  on this field. Evidence: §3, §4 above.
- **Integrator:** restate claim O's `after_required`/threshold — the r39 212-entry
  arithmetic (`2504 = 2335+163+0+6`) is not reproducible at the live 220-entry tree
  (this seat: 2607/2435/166/0/6 single-line; 2611/2437/166/0/8 block). Evidence: §8.
- **Integrator:** the durable fix host must be a NEW `tools/` resolver; `reports/round-19/**`
  is never-edit filed bytes, so an in-place diff is unlandable. Evidence: §9.
- **C06/C07/integrator:** use vector `25/27/25/29/24/94` (sum 224), not the mission's
  `25/23/27/25/24/94` (sum 218). Evidence: §12.
- **O08/integrator:** disambiguate the two N6 senses before re-classing the v2 row.
  Evidence: cross-block note 1.
- **to-verify (this seat):** the r39 policy Part 2's exact `212`-entry population was not
  re-executed here (filed bytes read only); the `212` figure is taken from
  `basename-couples-policy.md` §5.5 and `Ca04-verify.md` check 1, not re-measured.

## Citations

- Defect host: `reports/round-19/audit/entry-audit.py:31,33-42,74-96` (`:75` the
  single-line `re.search`).
- Wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`; absent
  targets confirmed by `ls corpus/knowledge/linguistics/` (this seat, 2026-10-19).
- Host-idiom trap: `tools/gates/provenance-audit.py:244-260` (`:259` the space join),
  `:318-323` (couples used for presence only); imported and called on the live file.
- Policy/arithmetic: `reports/round-39/calib/basename-couples-policy.md` §1, §2, §5.5,
  §5.6, §6; `reports/round-39/calib/Ca04-verify.md` D1, D2, check 1, check 6.
- Disposition rule: `reports/round-35/cov/C12-audit-runbook.md:37`.
- Queue: `reports/round-40/op/defect-queue-v2.json:362-369` (N6 extractor);
  `reports/round-40/calib/Ca03-receipt.md:86,87,88` (N4/N5/N6 senses);
  `reports/round-40/review/R02-review.md:90-98` (the phantom-repair N6).
- Durable-host gap: `reports/round-35/cov/C14-audit-6-10.md:227-236,249-288`;
  `.scratch/c05/c05-audit.py` (present but ephemeral, 15656 bytes);
  `grep -ln "couples" tools/harness/*.py` → empty.
- README/sweep: `corpus/README.md:196` (`## myth-symbol/ (23)`), `:532`
  (`Total knowledge entries: 220.`), `:534-536` (counts footer);
  `reports/round-28/readme/sweep.py:44-51,150-190` (partition order, footer leg).
- Entry contract: `corpus/QUALITY.md:1-20`; `corpus/knowledge/myth-symbol/trickster.md:3-8`;
  23/23 files carry the three admission fields (grep count, this seat).
- Command outputs (this seat, 2026-10-19, repo root at `ac47c78`, all read-only):
  (a) single-line probe on `phonetics-phonology.md` → 0 tokens vs block 4;
  (b) join-rule matrix → hyphen-aware/no-space-nl `tone-prosody.md`, space-join
  `prosody.md`, soft-hyphen-strip `toneprosody.md`; (c) full 220-entry recount → the two
  rows in §7; (d) `provenance-audit.field_block` import call → content with
  `tone- prosody.md`, 4 tokens incl. `prosody.md`; (e)
  `python3 -B reports/round-28/readme/sweep.py` → 220/220, footer_ok True;
  (f) partition vector arithmetic → claim tgt sums 218, correct tgt sums 224.
