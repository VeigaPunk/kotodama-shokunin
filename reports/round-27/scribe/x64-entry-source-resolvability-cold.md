# X64 — entry source-resolvability: independent cold leg (round 27)

- round 27 (operator: loop 3 of 3, build 3 of 4; 64 workers per
  `reports/round-27/claims.json`) · seat **X64** (SCRIBE X64 — entry auditor,
  source resolvability, cold leg) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X63..X64: entry auditors (source resolvability)."
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`
  (`reports/round-27/claims.json:5`); declaration HEAD
  `b95fca1e40f32f7346937ab6426f9ccca60e319f`.
- canon: NON-CANON engineering evidence. This seat audits and reports; it admits
  no claim, certifies no round, disposes no candidate.
- writes: **this file**, its instrument
  `reports/round-27/audit/x64-cold-rerun.py`, and gitignored scratch under
  `.scratch/` (including the clone). **No `corpus/**` byte written.** No filed
  round-8–26 artifact, tool, gate, packet or component edited. No commit, no push.
- **This seat authored neither the entry it audits nor the instrument it
  cross-checks.** X63 wrote `x63-entry-source-resolvability.py` and its fragment;
  this seat re-derives the same readings with different machinery, so that an
  agreement between the two is evidence and not a shared bug.

## 0. Headline

The round-27 claim-C entry **landed** and the two instruments **agree on every
load-bearing reading**: same bytes, same gap verdict, same decision-record
verdict, **zero unresolved locators on both legs**, and the same single red pin.
The one remaining difference is a token-labeling convention, named in §3 rather
than reconciled away.

The cold leg also found and fixed **two defects in itself that made it bless what
it was built to catch** — a clone that could not see uncommitted work, and a
tracked-only listing that could not see the new entry at all (§4).

## 1. Why a second instrument, and how it differs

An audit that re-runs its own tool measures its own tool. The two instruments
must not share a failure mode, and they differ on every load-bearing surface:

| reading | X63 instrument | this cold leg |
|---|---|---|
| locator extraction | one compiled regex over the text | **two** regexes (backticked and bare), resolved by `test -e` **in a shell** |
| passage/brace handling | suffix strip + brace expansion in Python | the same conventions, independently implemented, resolved per-expansion by `test -e` |
| pin re-derivation | `hashlib.sha256` in-process | `sha256sum(1)` **subprocess** |
| absence sweep | `os.walk` + `re.search` (BRE→Python translated) | `grep -rln` **subprocess** — the real tool the entries quote |
| gap / decision | field regex + heading regex | independent regexes + a heading-line scan |
| tree | the live lane worktree | a `git clone --shared` **with the worktree overlaid** |

Two differences are decisive:

- **The sweep leg runs the real `grep`.** The entries quote `grep`, and the
  quoted pattern is a POSIX **BRE**. X63 must translate BRE→Python (its finding
  X63-H2); this leg runs `grep` itself and cannot make that translation error at
  all. Where the two agree, the BRE question is settled by construction.
- **The measurement tree is a clone.** The lane worktree moved throughout the
  wave, so every number below binds to the clone's `rev-parse HEAD` plus the
  overlay manifest (§4).

## 2. The instrument, and its controls

`reports/round-27/audit/x64-cold-rerun.py` — read-only over the repo, stdlib
only, exit 0 clean / 1 findings / 2 could-not-evaluate.

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-27/audit/x64-cold-rerun.py --selftest          # 0 failures, exit 0
python3 -B reports/round-27/audit/x64-cold-rerun.py \
    --baseline 4f09c990d4c17f23b5e2cda0871f81db875635fc \
    --out .scratch/x64-entry.json --scratch .scratch/x64cold \
    --x63 .scratch/x63-entry.json
```

**The entry is located by set difference, never by a guessed filename.**
`git ls-tree` at the declared baseline vs `git ls-files --cached --others
--exclude-standard` in the clone; the difference is the audit target. A round
that lands two entries audits both; a round that lands none reports
`no-new-entry`.

`--selftest` controls: tick regex, bare regex, both sweep quote styles, the
declared-absent exemption firing and staying silent, gap field form, gap heading
form, decision form.

## 3. The round-27 entry, audited — and the X63↔X64 agreement matrix

```
clone_head b95fca1e40   counts {'baseline': 19, 'live': 20, 'new': 1}
new: ['corpus/knowledge/linguistics/register-strata-attestation.md']
overlaid: 93 paths (the wave's uncommitted work; see §4)
entry sha256 8dd62923af4208e4319b0c61c8623a0595f9a5f10adf6cd7f81f8b7c43148f6a
gap_named: true      decision_record: true
locators: 41 resolved, 0 unresolved, 0 declared-absent
pins: 4 re-derived, 1 drift
findings: 1 (X64-E, the same pin row X63 reports)
```

The agreement matrix, read from `x63_comparison.rows[0]`:

| column | value | meaning |
|---|---|---|
| `sha256_agree` | **true** | both instruments audited the same bytes — the precondition for the rest of the row |
| `gap_agree` | **true** | both see the gap statement |
| `decision_agree` | **true** | both see the decision-record heading |
| `unresolved_set_agree` | **true** | **both find zero unresolved locators** — the load-bearing column |
| `resolved_set_agree` | false | a token-labeling convention, not a disagreement: see below |
| `x63_only_resolved` | `[]` | X63 resolved nothing the cold leg did not |

**The one `false`, explained rather than reconciled away.** The cold leg's
extractor keeps the passage suffix and the brace form as part of the token
(`semantics-pragmatics.md:88-98`, `{design,forms,rules,review}.md`), so it
reports 41 resolved tokens where X63 — which records the same citations under
their stripped/expanded forms — reports 32. `x63_only_resolved` is empty, so X63
resolved nothing the cold leg missed; the nine-token surplus is entirely
suffix/brace tokens that the cold leg resolved *per expansion*. **Both legs agree
that every cited path exists.** A consumer should read `unresolved_set_agree`,
not `resolved_set_agree`, as the resolution verdict.

### 3.1 The pin row both legs report

```
pin  examples/culture-d4/packet.d4.yml  dd25077bc016…  -> c5441e3d0b237f331cfabe8002ad3bf4db7694e2666c21ba8c723ac66bf21f6a
```

Both instruments, with different digest machinery, report the same row. The
analysis and disposition are X63's finding X63-E1; this seat confirms it
independently and adds the measurement that makes it unambiguous:

```sh
sha256sum examples/culture-d4/packet.d4.yml \
  tools/gates/frozen/round-26/post-register/inputs/examples/culture-d4/packet.d4.yml
# live worktree   c5441e3d0b237f331cfabe80…
# frozen copy     dd25077bc01681bc17f4586b…
git show HEAD:examples/culture-d4/packet.d4.yml | sha256sum
# committed       dd25077bc01681bc17f4586b…
```

The entry's digest is the **committed/frozen** digest; the live worktree packet
moved when the round-27 D-claim landed the register law
(`examples/culture-d4/components/13-register-law.yml`). The pin was honest when
taken. It is stale now.

## 4. Findings in this instrument — two ways a cold leg can bless what it audits

### X64-H1 — the clone could not see the new entry at all (fixed)

`git ls-files` lists **tracked** paths only. The round-27 entry landed untracked
(`?? corpus/knowledge/linguistics/register-strata-attestation.md`), so the first
run reported:

```
counts {'baseline': 19, 'live': 19, 'new': 0}
note no-new-entry: the partition is unchanged against the baseline
```

**The harness reported an empty audit while the artifact sat on disk.** Fixed:
the listing uses `--cached --others --exclude-standard`, and the untracked files
are overlaid into the clone (a `git clone` carries committed content only).
Measured after the fix: `live: 20, new: 1`.

This is worth recording because the *pre-fix* output was not an error — it was a
clean `no-new-entry` with exit 0, exactly the shape a careless consumer reads as
"nothing to audit, therefore nothing wrong".

### X64-H2 — the clone could not see uncommitted changes, and blessed a stale pin (fixed)

The serious one. A `git clone` carries **committed** content, so a tracked
surface that the live wave has modified is present in the clone at its committed
bytes. Measured, before the fix:

| leg | `examples/culture-d4/packet.d4.yml` | pin verdict |
|---|---|---|
| cold leg, clone only | `dd25077bc01681bc…` (committed) | **`re-derived`** |
| X63, live worktree | `c5441e3d0b237f331c…` (modified) | **`drift`** |

**The cold leg reported green on a pin the live tree had already invalidated** —
and the invalidation was caused by the very round under audit. A cold leg that
cannot see uncommitted work systematically under-reports exactly the stale pins a
live round creates.

Fixed: `overlay_untracked` now copies the union of untracked **and
modified-vs-HEAD** paths, and the receipt carries `worktree_overlaid_count` (93
paths at this run) so a consumer can see the clone is worktree-equivalent rather
than commit-pinned. After the fix both legs report the same red pin.

**This is why the agreement matrix carries `sha256_agree` first.** Before the
fix the two legs disagreed on the pin and agreed on nothing else; the row's
`sha256_agree: true` is the signal that the comparison is now meaningful.

### X64-H3 — passage locators and brace citations read as dead links (fixed)

The cold leg's extractor originally kept the whole backticked token, so
`file.md:88-98` (a line range inside an existing file) and
`{design,forms,rules,review}.md` (several files at once) resolved nowhere and
produced nine spurious unresolved tokens. Fixed with suffix stripping and brace
expansion, resolved per expansion by `test -e`, so a genuinely dead branch of a
compressed citation is still named. This was the same defect class X63 found in
its own extractor (X63-H4), independently — and it is the reason
`unresolved_set_agree` is the column to read.

## 5. What this seat did not do

- It **adjudicates no claim.** Claim C's verdict belongs to the round's runner and
  auditor; this fragment is evidence.
- It **repairs nothing.** The red pin is routed, not fixed.
- It **writes no corpus byte** and touches no filed round-8–26 artifact.
- It **does not run the round-27 counting command** (`python3
  reports/round-27/run-validation.py`): a counting command can itself be a writer
  (round-14 established this), and its receipt belongs to the assigned runner.
- It **did not author** the entry, the X63 instrument or the X63 fragment.

## 6. Limits

- **The overlay makes the clone worktree-equivalent, not hermetic.** Copying
  modified files in means the clone is a point-in-time copy of a moving tree; the
  receipt's `clone_head` plus `worktree_overlaid_count` bind the reading, and a
  later run is a new measurement. The `--shared` clone also carries the lane's
  object store at clone time.
- The comparison leg compares the **same bytes**; a `sha256_agree: false` row is
  void rather than informative, and says so.
- The cold leg's sweep leg uses `grep` and therefore handles BRE correctly, but
  its sweep *recogniser* is the same narrow `grep -rln "…" <path> → 0` shape as
  X63's, so the round-27 entry's `grep -rl -i … | wc -l` sweeps are not scored by
  either leg. X63 §3.2 re-ran those five by hand; this seat confirms the
  conclusion (all five reproduce at 0) and records the same limit.
- Both legs share one blind spot by construction: a locator shape that neither
  regex matches is invisible to both. The two-regex, two-machinery difference
  narrows it; it does not close it.
- This is a **re-run record**, not round acceptance. The parent owns the verdict
  and must take it on the final settled tree.

## 7. Reproduce

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-27/audit/x64-cold-rerun.py --selftest
python3 -B reports/round-27/audit/x63-entry-source-resolvability.py --offline --json \
    corpus/knowledge/linguistics/register-strata-attestation.md > .scratch/x63-entry.json
python3 -B reports/round-27/audit/x64-cold-rerun.py \
    --baseline 4f09c990d4c17f23b5e2cda0871f81db875635fc \
    --out .scratch/x64-entry.json --scratch .scratch/x64cold \
    --x63 .scratch/x63-entry.json
```

---

*Receipts: `.scratch/x64-entry.json` (the audited entry + agreement matrix),
`.scratch/x64-control-empty.json` (the earlier `no-new-entry` control).
Fragment written 2026-10-18.*
