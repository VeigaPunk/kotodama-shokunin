# X64 — entry source-resolvability: independent cold leg (round 28)

- round 28 (operator: loop 3 of 3, build 4 of 4 — the last build round; 64 workers
  per `reports/round-28/claims.json`) · seat **X64** (SCRIBE X64 — ceiling-entry
  auditor, source resolvability, cold leg) · owner: L2 worker, kotodama-shokunin
  lane.
- assignment (verbatim): "SCRIBE X63..X64: ceiling-entry auditors."
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`
  (`reports/round-28/claims.json:5`); declaration HEAD
  `69cecbc7dcf575a29f29660ecac470e05260fd86`.
- canon: NON-CANON engineering evidence. This seat audits and reports; it admits
  no claim, certifies no round, disposes no candidate.
- writes: **this file**, its instrument
  `reports/round-28/audit/x64-cold-rerun.py`, and gitignored scratch under
  `.scratch/` (including the clone). **No `corpus/**` byte written.** No filed
  round-8–27 artifact, tool, gate, packet or component edited. No commit, no push.
- **This seat authored neither the documents it audits nor the instrument it
  cross-checks.** X63 wrote `x63-entry-source-resolvability.py` and its fragment;
  this seat re-derives the same readings with different machinery, so that an
  agreement between the two is evidence and not a shared bug.

## 0. Headline

Both round-28 claim-C documents **landed** and the two instruments **agree on
every load-bearing reading**: same bytes, same gap verdict, same decision-record
verdict, **zero unresolved locators on both legs**, the same four re-derived pins,
the same append-only amendment (`added 123, deleted 0`), and — the round's new
surface — **the same class for all four non-reproducing sweeps**. The only
difference is a token-labeling convention, named in §3 rather than reconciled
away.

## 1. Why a second instrument, and how it differs

An audit that re-runs its own tool measures its own tool. The two instruments
must not share a failure mode, and they differ on every load-bearing surface:

| reading | X63 instrument | this cold leg |
|---|---|---|
| locator extraction | one compiled regex over the text | **two** regexes (backticked and bare), resolved by `test -e` **in a shell** |
| passage/brace handling | suffix strip + brace expansion in Python | the same conventions, independently implemented, resolved per-expansion by `test -e` |
| pin re-derivation | `hashlib.sha256` in-process | `sha256sum(1)` **subprocess** |
| absence sweep | `os.walk` + `re.search` (BRE→Python translated) | `grep -rln` **subprocess** — the real tool the documents quote |
| sweep classification | `git grep -G` at the baseline, in the worktree | `git grep -G` at the baseline, **inside the clone** |
| amendment discipline | `difflib.SequenceMatcher` line diff | `git diff --numstat` over the baseline blob |
| ceiling record | regex over the live text | `grep -c` over the document |
| tree | the live lane worktree | a `git clone --shared` **with the worktree overlaid** |

Two differences are decisive:

- **The sweep leg runs the real `grep`.** The documents quote `grep`, and the
  quoted pattern is a POSIX **BRE**. X63 must translate BRE→Python; this leg runs
  `grep` itself and cannot make that translation error at all. Where the two agree
  on a sweep's class, the BRE question is settled by construction.
- **The amendment leg is `git diff`.** X63 computes a line diff in Python; this
  leg asks git for the numstat. X63's own amendment leg was **wrong** on first
  write (§4, X64-H1) and this leg is what caught it from outside.

## 2. The instrument, and its controls

`reports/round-28/audit/x64-cold-rerun.py` — read-only over the repo, stdlib
only, exit 0 clean / 1 findings / 2 could-not-evaluate.

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/audit/x64-cold-rerun.py --selftest
python3 -B reports/round-28/audit/x64-cold-rerun.py \
    --baseline 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede \
    --out .scratch/r28-x64-entry.json --scratch .scratch/x64r28 \
    --x63 .scratch/r28-x63-entry.json
```

`--selftest` controls: both locator regexes, all three sweep forms (double-quote,
single-quote, and the `| wc -l` piped form with `-i`), the declared-absent
exemption firing and staying silent, the gap and decision heading forms, and the
ceiling/constraint shapes (the record must fire; a bare ceiling mention without
constraint language must not).

## 3. The two documents, audited — and the X63↔X64 agreement matrix

```
clone_head 69cecbc7dcf575a29f29660ecac470e05260fd86
counts {'baseline': 20, 'live': 21, 'new': 1, 'amended': 1}
overlaid 136 paths (the wave's uncommitted work; both claim-C documents among them)
register-lexicon-ceilings.md      bb579d51cea0a900…   34400 B / 289 lines   locators 31, 0 unresolved
register-strata-attestation.md    645d692932edec50…   64928 B / 436 lines   locators 56, 0 unresolved
pins: 4 re-derived, 0 drift        amendment: added 123, deleted 0, append_only true
sweeps: 4 rows do not reproduce — 1 authoring-defect, 3 sibling-landing (same as X63)
```

The agreement matrix, read from `x63_comparison.rows`:

| column | ceilings entry | strata entry | meaning |
|---|---|---|---|
| `sha256_agree` | **true** | **true** | both legs audited the same bytes — the precondition for every other column |
| `gap_agree` | **true** | **true** | both see the gap statement |
| `decision_agree` | **true** | **true** | both see the decision-record heading |
| `unresolved_set_agree` | **true** | **true** | **both find zero unresolved locators** — the load-bearing column |
| `amendment_agree` | **true** | **true** | both agree on which document is the amendment |
| `ceiling_agree` | **true** | **true** | both see the ceiling recorded as a constraint |
| `resolved_set_agree` | false | false | a token-labeling convention, not a disagreement — see below |

**The `false` column, explained rather than reconciled away.** The two legs keep
a **different token form** for the same citation. X63 records a passage locator
under its stripped form (`examples/culture-d4/components/02-phonology.yml`) and a
brace-compressed citation under its expanded form; the cold leg keeps the suffix
and the brace form as part of the token
(`examples/culture-d4/components/02-phonology.yml:82`,
`reports/round-26/register/{design,rules,review}.md`). So the cold leg reports 31
and 56 resolved tokens where X63 reports 25 and 46, and the set difference is
**two tokens, each present in both legs under its other spelling** — measured:

```
ceilings  x63_only  corpus/knowledge/synthesis/dialect-faction-map-workflow.md
          cold_only corpus/knowledge/synthesis/dialect-faction-map-workflow.md:122
strata    x63_only  examples/culture-d4/components/02-phonology.yml
          cold_only examples/culture-d4/components/02-phonology.yml:82
```

The six- and ten-token surpluses are entirely suffix/brace tokens the cold
leg resolved *per expansion*. **Both legs agree that every cited path exists**,
and a consumer should read `unresolved_set_agree`, not `resolved_set_agree`, as
the resolution verdict.

### 3.1 The four sweep rows, independently classified

This is the round's new surface, and both legs reach the same class for all four
rows with different machinery (`os.walk`+Python vs. real `grep`; `git grep` in the
worktree vs. in the clone):

| pattern | document | X63 class | X64 class | agree |
|---|---|---|---|---|
| `lexicon ceiling` | ceilings (new) | sibling-landing | sibling-landing | **yes** |
| `which semantic fields` | ceilings (new) | authoring-defect | authoring-defect | **yes** |
| `attestation register\|attestation speech` | strata (amended) | sibling-landing | sibling-landing | **yes** |
| `register law\|register-law` | strata (amended) | sibling-landing | sibling-landing | **yes** |

The cold leg confirms the authoring defect from its own clone: `git grep -G` at
`6c0ac448…` inside the clone returns
`corpus/knowledge/linguistics/sound-symbolism.md` for `which semantic fields`, and
returns **nothing** for the other three once the audited document is excluded.
X63's finding X63-F2 is therefore independently confirmed, and X63-F1/F3/F4 are
independently confirmed as properties of the wave rather than of the author.

## 4. Findings in this instrument — one way a cold leg can bless what it audits

### X64-H1 — the clone could not see uncommitted work (guarded, and it caught a peer defect)

A `git clone` carries **committed** content only, so anything the wave has written
but not committed does not exist inside the clone. Two failure modes follow, and
the second is the dangerous one:

- a new entry that has not been committed is invisible, so the harness would
  report `no-target` while the artifact sits on disk in the lane;
- a **modified** tracked surface is still present at its committed bytes, so a pin
  that the live worktree has already invalidated **re-derives clean in the
  clone**. **A cold leg that cannot see uncommitted work blesses exactly the stale
  pins a live round creates.**

Both sets are therefore overlaid (`untracked ∪ modified-vs-HEAD`), and the receipt
carries `worktree_overlaid_count` (136 paths at this run) and the
`untracked_overlaid` list, which names both claim-C documents — the clone is
worktree-equivalent rather than commit-pinned, and a consumer can see that. The
round-27 cold leg's own record documents this defect class (its X64-H2); this seat
carries the guard forward rather than rediscovering it.

The guard is also what let this leg **catch X63's amendment defect from outside**:
X63's first amendment leg (a greedy pointer walk) reported `deleted_or_rewritten:
311` for a one-line rewrite, while this leg's `git diff --numstat` reported the
true `deleted: 1`. X63 fixed it with `difflib.SequenceMatcher` and added a
magnitude control; on the real amendment both legs now agree on
`added 123, deleted 0`.

## 5. What this seat did not do

- It **adjudicates no claim.** Claim C's verdict belongs to the round's runner and
  auditor; this fragment is evidence.
- It **repairs nothing.** X63-F2 (the authoring defect) is routed by X63, not
  fixed here; the sibling-landing rows are reported, not "fixed".
- It **does not re-derive the ceiling arithmetic** (19/8 vs 18/9) or read the
  documents for merit — that is the C seat's measurement and D20's review surface.
- It **writes no corpus byte** and touches no filed round-8–27 artifact.
- It **does not run the round-28 counting command** (`python3
  reports/round-28/run-validation.py`): a counting command can itself be a writer,
  and its receipt belongs to the assigned runner.
- It **did not author** the documents, the X63 instrument or the X63 fragment.

## 6. Limits

- **The overlay makes the clone worktree-equivalent, not hermetic.** Copying
  modified files in means the clone is a point-in-time copy of a moving tree; the
  receipt's `clone_head` plus `worktree_overlaid_count` bind the reading, and a
  later run is a new measurement. The `--shared` clone also carries the lane's
  object store at clone time.
- The comparison leg compares the **same bytes**; a `sha256_agree: false` row is
  void rather than informative, and says so. Both rows here are `true`.
- The cold leg's sweep leg uses `grep` and therefore handles BRE correctly, but
  its sweep *recogniser* accepts the same two forms as X63's
  (`grep -rln "…" <path> → 0` and `grep -rl -i "…" <path> | wc -l → 0`). A sweep
  written as prose, or piped to something other than `wc -l`, is scored by
  neither leg.
- Both legs share one blind spot by construction: a locator shape that neither
  regex matches is invisible to both. The two-regex, two-machinery difference
  narrows it; it does not close it.
- This is a **re-run record**, not round acceptance. The parent owns the verdict
  and must take it on the final settled tree.

## 7. Reproduce

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/audit/x64-cold-rerun.py --selftest
python3 -B reports/round-28/audit/x63-entry-source-resolvability.py --offline --json \
    --baseline 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede > .scratch/r28-x63-entry.json
python3 -B reports/round-28/audit/x64-cold-rerun.py \
    --baseline 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede \
    --out .scratch/r28-x64-entry.json --scratch .scratch/x64r28 \
    --x63 .scratch/r28-x63-entry.json
```

---

*Receipts: `.scratch/r28-x64-entry.json` (both documents + agreement matrix).
Fragment written 2026-10-18.*
