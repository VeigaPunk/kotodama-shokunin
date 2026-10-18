# R27-C48 — entry audit: no filler, sources resolve (round 27)

- **seat:** R27-C48 (C-audit). **lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  **assignment (verbatim):** "C R27-C47..C48 (README + audit): corpus/README
  reconciled; entry audit (no filler, sources resolve)."
- **date:** 2026-10-18. **declared baseline:** `4f09c990d4c17f23b5e2cda0871f81db875635fc`;
  **HEAD at measurement:** `b95fca1e40f32f7346937ab6426f9ccca60e319f`.
  **measurement stamps:** 19:19:25Z (pre-landing), **19:22:46Z (final, binding,
  after the round-27 register entry and the D seat's law component landed)**.
- **canon:** NON-CANON engineering evidence. This audit admits nothing, certifies
  no round, blesses no source, and adjudicates no entry's scholarship.
- **writes:** `reports/round-27/audit/entry-audit.py`, this file,
  `reports/round-27/audit/x-c48-receipt.json`, and scratch under `.scratch/`.
  **No `corpus/**` byte written.** No commit, no push.
- **instrument:** `python3 reports/round-27/audit/entry-audit.py`
  (sha256 `fb589b28cf4769ac2ce39d820640bb464a93601f4486f54268d31e1c4c06bcda`
  at the final stamp; re-check the digest before quoting any reading below — the
  instrument was revised seven times during calibration, §4).

## 0. Headline

All **200** entries audited (the round-27 register entry landed at 19:20Z and is
included). Two legs, reported separately because they have different force:

| leg | result | force |
|---|---|---|
| **sources resolve** | **0 unresolved path refs**; 1,187 of 1,219 source bullets carry a locator; 3 ambiguous class-names; 5 repo-pin mismatches, all dated round-19 pins (§2) | a hard check — a broken path is a defect |
| **no filler** | 27/200 entries name a gap (14 as a frontmatter field, 13 in prose/heading only); 173 name none (§3) | an **admission rule for new entries**, not a retroactive verdict — see §3 |

**The round-27 register entry clears every leg and the full admission bar**
(`bar=True`, `filler=False`, `src=19/19`, `refs_unres=0`, `digests_bad=0`,
`couples_unres=0` at 19:22:46Z). It is gap-named with a measured absence sweep,
frontmatter-complete, decision-record carrying, calibration-flagged, and every
one of its 19 source bullets carries a locator. Its six sha256 pins all match at
this stamp — the three that mismatched at 19:20Z were peer round-27 files still
being written, and the peer refreshed them inside the round (recorded in §2.3b
as the coordination event it was, not as a defect).

The second row is the one that needs care. Reporting "174 filler entries" would
be false: the lane's gap-naming discipline was introduced in round 10 and
extended in round 19, and most of the corpus predates it. The honest reading is
given in §3.

## 1. Method

```sh
export TMPDIR=$PWD/.scratch
python3 reports/round-27/audit/entry-audit.py --selftest          # 11/11, exit 0
python3 reports/round-27/audit/entry-audit.py \
    --partition linguistics --partition myth-symbol --partition culture-material \
    --partition synthesis --partition verification --partition civilizations --json
```

The instrument checks each entry against `corpus/QUALITY.md` and this round's
claim-C requirements: required header fields (`topic`/`sources`/`couples`), the
`verified-at`+`recheck` tail, locator presence on every source bullet, repo-path
resolution, sha256 pin classification, `couples:` resolution, a named gap, a
decision record, calibration vocabulary, and canon hygiene.

## 2. The sources-resolve leg

### 2.1 Path references

**0 unresolved.** The first pass reported 12; every one was an instrument
artifact, not a corpus defect, and the fixes are recorded in §4 because an
instrument that manufactures findings is itself the finding.

| ref shape | example | resolution base |
|---|---|---|
| partition-relative | `../linguistics/writing-systems.md` | entry dir |
| partition-prefixed | `linguistics/{a,b}.md` | lane root |
| bare basename after a dir group | `packet.d4.yml` | dir named earlier in the bullet |
| lane-relative | `tools/d2-typed-labels.py` | lane root |
| fleet surface | `PROTOCOL.md` | fleet root, one level up |
| fleet-wave internal | `frozen/post/MANIFEST.json` | unique hit under `.ufo/waves/*/` |

**4 ambiguous names** are reported, not failed: `expected.json` (×3) and
`01-brief.yml` (×1). These name a *class* — the lane commits 17 baseline files
named `expected.json` — so a single-file resolution is not the right test. The
instrument reports the match count and leaves the judgement to a reader.

### 2.2 Source bullets and locators

1,219 source bullets across 200 entries; **1,187 carry a locator** (URL, year,
backticked path, or digest). The 32 without one are concentrated in 20 entries
(`divination-omen-systems.md` 7, `calendar-festival-systems.md` 3,
`celestial-symbolism-calendars.md` and `cosmology-cosmography.md` 2 each, the
rest 1 each). This is reported as a distribution, not as a failure: the
`QUALITY.md` bar is "every factual claim carries a cited, checkable source", and
a bullet without a year or URL may still carry an author+title. **No entry has
zero locator-bearing bullets**, and every entry has at least one — the round-27
register entry included (19/19).

### 2.3 sha256 pins

Digests were classified rather than blanket-failed, because the corpus uses them
for three different things:

| class | count | meaning |
|---|---|---|
| `repo_matched` | 9 | the digest matches the file the same bullet names |
| `repo_mismatch` | 5 | the bullet names a resolved repo file; the digest is not that file's |
| `external_uncheckable` | 2 | the bullet also names a URL — a fetched page or offline artefact |
| `abbrev` | 16 | a truncated digest (`94b6bdaf…`), not re-checkable by construction |

All 5 `repo_mismatch` rows are **round-19 pins superseded by round 20 and round
26**, in `synthesis/typed-label-routing-workflow.md` (1),
`verification/label-channel-routing-verification.md` (3), and
`verification/pre-declared-hold-set-reconciliation.md` (1).

**These are dated pins, not laundering.** Each digest was traced across the
rounds by re-hashing the file at each revision:

```sh
for rev in caf1bea 35b6797 4f09c99 b95fca1; do
  printf "%s " $rev; git show $rev:tools/d2-typed-labels.py | sha256sum | cut -c1-16; done
# caf1bea 0da0015f700345c9   ← the pinned value
# 35b6797 76536a924280ad41   ← round 20 moved it
# 4f09c99 2819f68769dfc0b5   ← round 26 moved it again
# b95fca1 2819f68769dfc0b5
```

The same trace holds for `typed-labels.d4.yml` (`a59990bb…` at `caf1bea` →
`d03f6391…` today) and `expected-holds.json` (`09490a27…` → `d6136488…`). Every
pinned value **matches the round-19 commit exactly** and then moved when round
20 and round 26 re-pinned the D4 surfaces. So the entries are accurate at their
own stamp and stale at today's; the correct disposition is a dated qualifier or
a new row (the lane's corrections-are-new-rows rule), never an in-place edit.
The entries' own `recheck:` lines anticipate exactly this.

**(b) A same-round race, resolved inside the round — recorded because it is the
class the integrator will hit again.** At the 19:20:45Z stamp the register entry
showed **3** mismatching pins: `reports/round-27/law/design.md` (`00f201b3…`
pinned), `reports/round-27/law/rules.md` (`9b0d1415…` pinned) and
`reports/round-27/audit/x59-register-law-negatives.py` (`f5f5d46a…` pinned). All
three files existed and resolved; the peer seats were still writing them while
the entry was authored, so the entry pinned an earlier stamp of the same round.
By 19:22:46Z the peer had refreshed the pins and **all three match**
(`9d5c1dd7…`, `c6935957…`, `7e3b3559…` at this stamp). This is reported as a
**coordination artifact of the parallel wave, measured and closed within the
round**, not as a defect: it is precisely why the lane's pins must be re-checked
at the close stamp rather than at their own write stamp, and why a reading that
quotes only one stamp is not evidence about a live tree.

### 2.4 `couples:` resolution

**6 genuine phantom refs** remain after calibration, in 4 entries:

| entry | phantom ref |
|---|---|
| `linguistics/language-contact.md` | `honorifics-and-register.md`, `naming-and-onomastics.md`, `phonology-basics.md` |
| `synthesis/typed-label-routing-workflow.md` | `linguistics/phonology-sanity.md` |
| `verification/label-channel-routing-verification.md` | `linguistics/phonology-sanity.md` |
| `verification/gate-frozen-run-standard.md` | `gate.md` |

The `linguistics/phonology-sanity.md` pair is the **same finding round 19
measured** (X26-1): the file is `verification/phonology-sanity-gate.md`, and
these two entries point at a wrong name in a wrong partition. It was reported
then as a correction for the integrator; it is **still present** at this pin, so
it is carried forward rather than closed. The other four are the same defect
class in older entries.

## 3. The no-filler leg — an admission rule, not a verdict

`QUALITY.md` does not require a gap statement; the round-10 and round-19 C
claims required it of **the entries those rounds landed**. Measured against the
whole corpus it returns 27/200, which says nothing useful about the other 173.

The reading that is actually supported — and the two forms must be counted
separately, which my first draft got wrong:

```sh
# the frontmatter form (the round-10/19 discipline as a machine-readable field)
grep -rl -e '^- gap filled:' -e '^- gap:' corpus/knowledge | wc -l    # 14
# the instrument criterion: frontmatter field OR prose/heading gap statement
python3 reports/round-27/audit/entry-audit.py ... --json \
  | grep -c '"gap_named": true'                                       # 27
```

- **14 entries carry the frontmatter gap field** (`- gap filled:` / `- gap:`).
  These are the entries the discipline was applied to as a machine-readable
  requirement, the round-27 register entry among them.
- **13 further entries name their gap in prose or a body heading** — `## 1. The
  gap this entry fills`, `## 13. Decision record — gap filled …`, `## Provenance
  cautions and known gaps`. 14 + 13 = **27**, the instrument's count. Both
  numbers are correct for their own definition; a receipt quoting only one would
  be misleading, so both are given.
- **The rule fires correctly on a new entry.** The instrument's selftest plants
  an entry with no gap statement and asserts rejection (`filler is True`,
  `quality_bar is False`); that control passes. The round-27 register entry's
  `- gap filled:` line carries a **measured absence sweep** (`grep -rl -i
  "illocutionary" corpus/knowledge/ | wc -l` → 0, and four more such greps),
  which is the discipline working as designed rather than as a slogan.
- **173 entries name no gap in either form.** They are not filler by that fact.
  An entry with a `- topic:` naming the partition's subject, complete sources,
  and a decision record is doing its job under the bar as written.
- **No actionable defect in the landed entry**: claim C required it to be
  gap-named, and it is, in the frontmatter form.

## 4. Instrument calibration — seven manufactured-finding classes, fixed

Recorded because an audit instrument's bugs are evidence about the audit:

1. **Brace groups mangled.** The token regex excluded commas, so
   `linguistics/{a,b}.md` tokenized as `naming-systems}.md`. This manufactured
   ~360 phantom couples refs (372 → 6 after the fix).
2. **Bare basenames unresolved.** `historical-linguistics.md` written after a
   directory group in the same bullet was not resolved against that directory.
3. **Fleet surface unreachable.** `PROTOCOL.md` lives one level above the lane;
   the resolver stopped at the lane root.
4. **Filesystem walk counted mirrors.** The basename index walked `.scratch` and
   the disposable export under `reports/supplement-opencode-1/scratch/`, finding
   **7,421** files named `expected.json`. Rebuilt from `git ls-files` (tracked
   files only) plus the fleet `.ufo/waves` surface.
5. **Fetch digests misread as repo pins.** A digest in a bullet that also names
   a URL is not re-checkable from the tree; now classified
   `external_uncheckable`.
6. **A declared `- gap:` field was not read as a gap statement.** The instrument's
   `GAP_RE` matched prose patterns only, so `transport-mobility-lexicon.md` —
   which declares `- gap: transport/mobility register absent from culture-material
   … — this entry fills it` — was counted as naming no gap. Fixed by treating a
   declared `- gap:` / `- gap filled:` field as a gap statement in its own right
   (14 frontmatter + 13 prose = 27, reconciled exactly).
7. **A receipt cross-check was wrong, not the instrument.** This audit's first
   draft asserted the instrument's `gap_named` count equalled
   `grep -rl '^- gap filled:\|^- gap:' corpus/knowledge | wc -l`. That grep
   returns **14** — it matches only the frontmatter field. The instrument was
   right (once item 6 was fixed) and the draft's cross-check was wrong. Both
   counts are now stated with their definitions (§3), and the discrepancy is
   explained rather than smoothed over. Recorded because a receipt that quotes a
   number without its definition is exactly the failure this lane's counting
   discipline exists to prevent.

Each fix was validated by the selftest's planted controls, which are unchanged
across the fixes (11/11 before and after) — the controls assert the *verdicts*,
not the implementation, so they cannot be satisfied by loosening a check.

## 5. Limits

- **Same-seat.** This seat wrote the instrument and ran it; `x-c48-receipt.json`
  is its own output. Independent-seat verification is the X63/X64 auditors' leg
  (their instruments are different machinery against the same tree).
- **Not a merits audit.** A locator that resolves is reported as resolved even
  when the source it names is weak; the instrument never judges whether a source
  is the right source or a calibration is warranted.
- **Pin-relative.** Every reading binds to HEAD `b95fca1` and stamp
  19:20:45Z. The round-27 register-strata entry landed at 19:20Z and is included
  (200 entries); its three same-round pins were still racing peer writers, so
  they are reported as coordination items rather than re-checked later by this
  seat.
- **No `corpus/**` byte written** by this seat, per the lane rule that
  corrections are new rows and filed artifacts of rounds 8–26 are never edited.
  The 6 phantom `couples:` refs and the 5 superseded round-19 pins are therefore
  **reported for the integrator**, not fixed here.
