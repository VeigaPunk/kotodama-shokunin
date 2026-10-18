# R27-C47/C48 verify — independent re-measurement of the README reconciliation and the entry audit

- **seat:** R27-C47..C48 verify leg. **lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- **date:** 2026-10-18. **HEAD:** `b95fca1e40f32f7346937ab6426f9ccca60e319f`.
  **stamps:** 19:19:25Z (pre-landing), **19:20:45Z (final, binding)**.
- **canon:** NON-CANON engineering evidence; admits nothing, certifies no round.
- **what this file is:** the reconciliation's and the audit's measurements re-run
  from fresh processes, with before/after and negative controls. It is
  **same-seat** verification — a re-measurement with controls, not
  independent-seat review — and that limit is restated in §5 rather than hidden.

## V1 — the sweep re-run (fresh process)

```sh
export TMPDIR=$PWD/.scratch
python3 reports/round-27/readme/sweep.py            # exit 0
# parts {"civilizations": 94, "culture-material": 18, "linguistics": 20,
#        "myth-symbol": 19, "synthesis": 29, "verification": 20}
# rows 200 files 200
# missing_from_index 0 []   topic_mismatch 0 []
# orphan_rows 0 []          header_drift {}
# totals_line 200 totals_ok True
# readme_sha256 d9d97d7f860c15bb00e9fca4e6b4df5469b62d6233b9168582481b353dd7c4e5
python3 reports/round-27/readme/sweep.py --json     # same result as JSON
python3 reports/round-27/readme/sweep.py --selftest # exit 0, 9/9
```

## V2 — counts re-derived by a second, independent method

```sh
python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge
# totals.files 200; per-dir 94/18/20/19/29/20
for d in linguistics myth-symbol culture-material synthesis verification civilizations; do
  find corpus/knowledge/$d -maxdepth 1 -name '*.md' -type f | wc -l; done
# 20 19 18 29 20 94
```

Both agree with the vector revision 1.7 carries and with the `Total knowledge
entries: 200.` line.

## V3 — the landing edit is exactly three changes (before/after)

The landing's own claim is falsifiable and was tested by reconstruction, not by
re-reading the receipt. `HEAD` is the committed tree, which holds revision 1.5,
so this diff shows **both** round-27 revision blocks plus the landing edits —
i.e. the whole round-27 delta, not the landing alone:

```sh
git show HEAD:corpus/README.md > .scratch/r27-readme-before.md
diff .scratch/r27-readme-before.md corpus/README.md    # 43 diff lines
# + revision 1.7 block (landing)
# + revision 1.6 block (re-measurement)
# - ## linguistics/ (19)          + ## linguistics/ (20)
# + - `register-strata-attestation.md` — …   (the new row)
# - Total knowledge entries: 199. + Total knowledge entries: 200.
```

The **landing alone** is the last three of those, and it is measured directly
against the pre-landing revision-1.6 state by the two sweep runs in V1:

| edit | before → after | verified by |
|---|---|---|
| `## linguistics/` header | `(19)` → `(20)` | sweep `header_drift {}` at both stamps |
| one new row | absent → present, in filename order | pre-landing `missing_from_index []`; final `topic_mismatch []` |
| totals line | `199.` → `200.` | pre-landing `totals_line 199`; final `totals_line 200 totals_ok True` |

The row is byte-equal to the entry's own `- topic:` head-block text (1,193
chars) because it was **generated from that head block**, not typed
(`.scratch/r27-c-insert.py`). The pre-landing README digest `1a359d55…` equals
the digest round-20's `verify.md` records at 13:07:53Z, so nothing in the README
had drifted before the landing — the landing is the only content change.

## V4 — controls (both instruments can fail)

**Sweep** — `--selftest` plants, in memory only, one defect per leg and requires
detection: planted paraphrase → 1 mismatch; **truncated rewrite** (the round-19
defect class) → 1 mismatch; ghost row → 1 orphan; deleted row → 1 missing file;
wrong header count → 1 drift; wrong totals line → rejected; continuation lines
not joined → 1 mismatch; duplicate row → reported. Plus the live leg. **9/9,
exit 0.**

**Entry audit** — `--selftest` plants one clean entry and one per defect class:
no `sources` field → bar fails; phantom source path → unresolved; **digest pinned
to the wrong file** → flagged `repo_mismatch`; **filler (no gap statement)** →
rejected; phantom `couples:` path → unresolved; plus a live-entry positive
control. **11/11, exit 0.**

Both control sets assert *verdicts*, not implementation, so they cannot be
satisfied by loosening a check.

## V5 — the round-27 entry's legs, re-derived

```sh
python3 reports/round-27/audit/entry-audit.py corpus/knowledge/linguistics/register-strata-attestation.md
# bar=True filler=False src=19/19 refs_unres=0 digests_bad=0 couples_unres=0   (19:22:46Z)
```

| leg | measured | reading |
|---|---|---|
| filler | `filler=False`, `gap_named=True`, `gap_field=True` | **passes** — the `- gap filled:` line carries a measured absence sweep |
| sources resolve | 19/19 bullets with a locator; 0 unresolved paths; 0 unresolved `couples:` | **passes** |
| header | no missing required field; `verified-at`+`recheck` tail present | **passes** |
| decision record / calibration / canon hygiene | all true | **passes** |
| sha256 pins | **all 6 match** at the final stamp | **passes** |

At the earlier 19:20:45Z stamp the same command read `digests_bad=3`: the entry
pinned `reports/round-27/law/design.md`, `reports/round-27/law/rules.md` and
`reports/round-27/audit/x59-register-law-negatives.py` while peer seats were
still writing them. The peer refreshed the pins inside the round, and at
19:22:46Z they match (`9d5c1dd7…`, `c6935957…`, `7e3b3559…`). The two stamps are
both carried because the difference between them **is** the evidence: a
same-round pin race, measured and closed, not a scholarship defect.

## V6 — the reported findings re-checked (not just re-read)

```sh
# the round-19 pins really are dated, not laundered
for rev in caf1bea 35b6797 4f09c99 b95fca1; do
  printf "%s " $rev; git show $rev:tools/d2-typed-labels.py | sha256sum | cut -c1-16; done
# caf1bea 0da0015f700345c9  ← the pinned value, exact match
# 35b6797 76536a924280ad41  ← round 20 moved it
# 4f09c99 2819f68769dfc0b5  ← round 26 moved it again
# b95fca1 2819f68769dfc0b5

# the phantom couples pair is still present (round-19 finding X26-1, not closed)
grep -n "phonology-sanity.md" corpus/knowledge/synthesis/typed-label-routing-workflow.md \
                               corpus/knowledge/verification/label-channel-routing-verification.md
# both point at linguistics/phonology-sanity.md; the file is
# verification/phonology-sanity-gate.md
```

## V7 — the gap counts, re-derived by a third method, both forms

```sh
grep -rl -e '^- gap filled:' -e '^- gap:' corpus/knowledge | wc -l   # 14 (frontmatter form)
python3 reports/round-27/audit/entry-audit.py --partition ... --json \
  | grep -c '"gap_named": true'                                     # 27 (instrument criterion)
```

The 14 are the entries carrying the machine-readable gap field; the 13 others
name their gap in prose or a body heading (`## 1. The gap this entry fills`,
`## Provenance cautions and known gaps`). 14 + 13 = 27. Both counts are correct
for their own definition and both are carried in the audit (§3) — quoting only
one would misstate the corpus.

**Correction recorded.** This receipt's first draft asserted the instrument's
count equalled `grep -rl '^- gap filled:\|^- gap:' | wc -l`. That grep returns
14, and the draft's claim that the two matched was **false**. Reading the
discrepancy showed the instrument was itself wrong in one direction (it missed
`transport-mobility-lexicon.md`, whose `- gap:` field says "this entry fills it"
in wording its prose patterns did not match — audit §4 item 6) and the draft's
cross-check was wrong in the other (the grep sees only the frontmatter form).
Both were fixed: the instrument now treats a declared `- gap:` field as a gap
statement, and the receipt states both counts with their definitions.

## V8 — limits

- **Same-seat.** This seat wrote both instruments and ran them; V1–V7 are its own
  re-measurements with controls, not independent-seat review. The independent
  legs are the round-27 X63/X64 auditors (different machinery, same tree).
- **Pin-relative.** Every reading binds to HEAD `b95fca1` and stamp 19:20:45Z.
  A later write to `corpus/README.md` or `corpus/knowledge/**` invalidates them
  until the sweep is re-run.
- **The instrument is versioned.** `entry-audit.py` was revised seven times
  during calibration (audit §4). Any quoted reading must name the digest
  (`fb589b28cf4769ac2ce39d820640bb464a93601f4486f54268d31e1c4c06bcda` at the
  final stamp) or it cannot be reproduced.

## V9 — the round runner's own C verdict (corroboration)

```sh
export TMPDIR=$PWD/.scratch
python3 reports/round-27/run-validation.py --check      # measure only, no receipt write
# claim C: passed true, failures []
# corpus_readme.revision_head "1.7"; partition headers 94/18/20/19/29/20
# corpus_readme.total_files 200; mismatches {}; names_the_entry true
# frontmatter {topic, sources, couples, verified-at, recheck} all true
# entry sha256 65cce441834e3e58467edf0981abc156dcd0fc6cda4d053bbe57af521b95774a
```

The runner is a **different instrument** from the two in this seat, measuring
the same surfaces independently. It agrees with V1/V2/V5 on every C reading, so
the agreement is evidence rather than a shared bug. The runner's D and O claims
fail on their own seats' in-flight artifacts (gate/legality splits, un-re-pinned
D4 surfaces, battery not yet reporting) — those are not C's legs and are not
restated here as this seat's findings.

The runner also read `Evidence changed while being measured:
reports/round-27/gate-tests/D15-law-negative.md` — a peer artifact written
during the run. That is the same wave-liveness condition named in §5, and it is
why every reading here is pinned to a stamp.
