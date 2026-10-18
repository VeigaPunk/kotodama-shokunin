# X63 — entry source-resolvability audit (round 27)

- round 27 (operator: loop 3 of 3, build 3 of 4; 64 workers per
  `reports/round-27/claims.json`) · seat **X63** (SCRIBE X63 — entry auditor,
  source resolvability) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X63..X64: entry auditors (source resolvability)."
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc` (round-26 admit,
  `reports/round-27/claims.json:5`); declaration HEAD
  `b95fca1e40f32f7346937ab6426f9ccca60e319f`.
- canon: NON-CANON engineering evidence. This audit admits nothing, certifies no
  round, blesses no entry, and grants no promotion.
- writes: **this file**, its read-only instrument
  `reports/round-27/audit/x63-entry-source-resolvability.py`, and gitignored
  scratch under `.scratch/`. **No `corpus/**` byte was written or edited by this
  seat.** No filed round-8–26 artifact, tool, gate, packet or component edited.
  No commit, no push.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | the instrument is green on **15 planted controls** (count reported by the tool itself, not asserted) — a clean entry, six defect classes, the declared-absent exemption, a reproducing sweep, a BRE-alternation sweep, a historical self-digest, a remote-artifact digest, a non-adjacent path, a still-caught adjacent drift, two refusal controls and the read-only control | measured |
| 2 | the round-27 claim-C entry **landed** and audits **clean on every surface this instrument grades** | measured |
| 3 | all **five** of the entry's absence sweeps reproduce exactly (`0 0 0 0 0`) | measured |
| 4 | **one pin row is red**: `examples/culture-d4/packet.d4.yml` pinned at `dd25077b…`, live `c5441e3d…` | **finding X63-E1** |
| 5 | **three false-green defects in this instrument were found and fixed by its own controls and by cross-tool comparison** — a pin leg that scored historical self-digests and remote-artifact digests as drift, and a sweep leg that read POSIX BRE `\|` as a literal pipe | **findings X63-H1, X63-H2, X63-H3** |

## 1. The entry

| field | value |
|---|---|
| path | `corpus/knowledge/linguistics/register-strata-attestation.md` |
| sha256 | `8dd62923af4208e4319b0c61c8623a0595f9a5f10adf6cd7f81f8b7c43148f6a` |
| bytes / lines | 44 136 / 234 |
| mtime | 2026-10-18T19:21Z |
| status | untracked (`??`), settled — two 30-second reads 30 s apart returned this digest |

The partition moved 19 → **20** files; `corpus/README.md` was revised to
revision 1.7 (`## linguistics/ (20)`, `Total knowledge entries: 200.`).

## 2. The instrument

`reports/round-27/audit/x63-entry-source-resolvability.py` — read-only, stdlib
only, exit 0 clean / 1 findings / 2 could-not-evaluate.

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-27/audit/x63-entry-source-resolvability.py --selftest   # 15/15, exit 0
python3 -B reports/round-27/audit/x63-entry-source-resolvability.py --offline --json <entry>
```

| id | surface | green means |
|---|---|---|
| X63-A | frontmatter | every lane-bar field (`topic`, `sources`, `verified-at`, `recheck`, `couples`) present and non-empty |
| X63-B | gap | the entry names the gap it fills, field form or heading form |
| X63-C | decision record | a `## … decision record …` heading exists |
| X63-D | locators | every repo-path locator resolves on disk |
| X63-E | pins | every `sha256` bound to a named repo path re-derives |
| X63-F | sweeps | every quoted absence sweep reproduces against the tree minus the entry |

**Scope of the claim.** This is a **resolvability** instrument, not a merits
instrument. A locator that resolves is reported resolved even when the source it
names is weak. It never says a source is the right source, never says a
calibration is warranted, and never says a gap is worth filling. A finding is
only ever "the entry says X and the bytes say not-X".

## 3. The round-27 entry, audited

```
sha256 8dd62923af4208e4   bytes 44136   lines 234
frontmatter missing []          gap named: yes (field form)     decision record: yes
calibration vocabulary: present
locators: 32 resolved, 0 unresolved, 0 declared-absent
pins: 4 re-derived, 1 drift
findings: 1 (X63-E1)
```

### 3.1 The three criteria of the round-10/round-19 audit bar

| criterion | verdict | evidence |
|---|---|---|
| names the gap it fills | **pass** | `:4` `- gap filled:` names the four neighbouring frameworks by path *and line range*, states what none of them covers ("no entry covers the attestation register as a design object, and none states the register law"), and backs it with five quoted sweeps |
| carries a decision record | **pass** | a `## … decision record …` heading is present and the instrument's heading probe fires |
| sources resolve | **pass with one red pin** | 32 locators, 0 unresolved; 4 of 5 pins re-derive; X63-E1 below |

### 3.2 The absence sweeps — all five reproduce

The entry quotes five sweeps, each `grep -rl -i "<pattern>" corpus/knowledge/ | wc -l` → **0**.
Re-run from the lane root at 2026-10-18T19:2xZ, excluding the entry itself:

| pattern | entry claims | measured | reproduces |
|---|---|---|---|
| `illocutionary` | 0 | 0 | **yes** |
| `constitutive rule` | 0 | 0 | **yes** |
| `deontic` | 0 | 0 | **yes** |
| `attestation register\|attestation speech` | 0 | 0 | **yes** |
| `register law\|register-law` | 0 | 0 | **yes** |

The entry's own honest qualification also holds: it says "the word `felicity`
occurs twice, both as a one-clause aside in a larger framework
(`semantics-pragmatics.md:88`; `ritual-liminality.md:112`) and never as a
designed rule set". Measured: `grep -rl -i felicity corpus/knowledge/ | wc -l` →
**3** — the two named entries plus this entry itself, which is exactly what the
entry's sentence implies. **The entry names the exception to its own sweep
rather than hiding it**, which is the round-10 auditor's disposition for a
non-reproducing sweep arrived at by the author first.

**Note the sweep form.** These are `grep -rl -i … | wc -l` with a `\|`
alternation in two of them. The instrument's sweep leg only recognises the
`grep -rln "…" <path> → 0 files` form, so it did **not** score these five; this
seat re-ran them by hand, and §6 states the limit that follows.

### 3.3 X63-E1 — one pin is red (finding)

```
pin  examples/culture-d4/packet.d4.yml  dd25077bc016…  -> live c5441e3d0b237f331cfabe8002ad3bf4db7694e2666c21ba8c723ac66bf21f6a
```

`KTD-RSA-S-0009` (`:14`) reads: `` `examples/culture-d4/packet.d4.yml` (sha256
`dd25077bc01681bc…`), `registers:` block rows `QREG-01..QREG-04`; and
`tools/gates/frozen/round-26/post-register/inputs/examples/culture-d4/packet.d4.yml`
(same digest, the frozen copy) ``.

**The digest is correct — for the frozen copy.** Measured:

| path | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` (live worktree) | `c5441e3d0b237f331cfabe80…` |
| `tools/gates/frozen/round-26/post-register/inputs/examples/culture-d4/packet.d4.yml` | `dd25077bc01681bc17f4586b…` |
| `git show HEAD:examples/culture-d4/packet.d4.yml` | `dd25077bc01681bc17f4586b…` |

So `dd25077b…` is the digest of the **committed** packet, which the frozen copy
still holds. The entry's own sentence is accurate about the frozen copy. What
makes the row red is that the entry binds the digest to the **live** path first
and only then mentions the frozen copy — and the live path no longer carries it.

**This is a real and dated condition, not an instrument artifact.** At the moment
the entry was written (19:19–19:21Z) the worktree packet *was* `dd25077b…`; the
round-27 D-claim then landed the register law into the packet
(`examples/culture-d4/components/13-register-law.yml`, `git status` → ` M
examples/culture-d4/packet.d4.yml`) and moved it to `c5441e3d…`. The pin was
honest when taken and is stale now — the round-25 lesson's own class ("a pin
taken on bytes that are still moving is not a pin"), showing up inside the round
that created the movement.

**Disposition.** The repair is one line in the entry (bind the digest to the
frozen copy, or state it as the pre-law digest). It is a **corpus write** and
this seat does not make it; the parent owns disposition. The finding is routed
with its command:

```sh
sha256sum examples/culture-d4/packet.d4.yml \
  tools/gates/frozen/round-26/post-register/inputs/examples/culture-d4/packet.d4.yml
git show HEAD:examples/culture-d4/packet.d4.yml | sha256sum
```

### 3.4 The four pins that re-derive

`reports/round-26/register/{design,forms,rules,review}.md` are pinned at
`27d23fa67d0b…`, `06635a1c123e…`, `535cf7a981c5…`, `0082f08b6298…` and all four
re-derive byte-equal. The entry also **declares two citations as revision-bound
rather than digest-pinned** (`KTD-RSA-S-0005`, `KTD-RSA-S-0006`: "Cited by
revision, not by digest … this file was still being written while this entry was
authored"). That is the correct handling of a moving surface and this seat
records it as a strength, not a gap: the author named the instability instead of
pinning a digest that would have gone stale within the hour.

## 4. Findings in this instrument

### X63-H1 — the pin leg scored historical self-digests as drift (fixed)

`color-terminology.md:116` records "entry sha256 **before append** `8272a8f6…`"
— a past state of the file itself, *supposed* not to match today's bytes. The
first version reported `pin-drift`. Fixed: a digest the clause marks as a past
state is reported `historical-self-digest` and never graded.

### X63-H2 — the sweep leg read POSIX BRE `\|` as a literal pipe (fixed)

**The serious one.** The entries quote shell commands, so the quoted pattern is a
**basic** regular expression, where `\|` is alternation and a bare `|` is a
literal pipe — the inverse of Python's `re`. The first version compiled the
quoted string directly, so
`grep -rln "check-gate-battery\|gate battery\|battery_exit" corpus/knowledge/ → 0 files`
(`gate-battery-surface-verification.md:4`) read `\|` as a literal pipe, found no
match, and reported the sweep **green** — while real `grep` returns a hit. The
leg was silently blessing false absence sweeps.

Fixed with an explicit BRE→ERE translation. **External control:** re-running the
fixed leg over the round-19 entries now reproduces `reports/round-19/audit-1.md`
§4's published verdicts — V4 and V5 red, with the same hits
(`verification-independence-anti-circularity.md`;
`myth-symbol/divination-omen-systems.md:201`). Before the fix both read green.

### X63-H3 — the pin leg bound digests to non-adjacent paths (fixed)

The first version bound a digest to the last repo path on the line. The lane's
convention is that a bullet's source is the path right after its id prefix
(`` - KTD-XX-S-NNNN — `path` (sha256 `abc…`): prose ``). Three measured false
positives followed, all now verified byte-by-byte:

| entry | what the digest really is | measured |
|---|---|---|
| `civilizations/maya-classic.md` | a downloaded PDF's digest (`49,858,925 bytes`) | `reports/round-17/civ/maya-classic.md` is a *trail* on the same line |
| `civilizations/mesoamerica-primary-sources.md` | a **web.archive.org raw snapshot** digest | a repo path is cited as a trail before it |
| `verification/verification-independence-anti-circularity.md` | both digests **do** match live bytes | `01c27fde…` = `reports/round-8/depth/findings.md`; `27ba8c2f…` = `reports/round-9/d3/findings.md` |

Fixed by scoping the binding to the bullet's opening path, classifying
remote-artifact and revision-bound digests, and grading a resolvable path even
when the bullet also names a revision. The three regression guards are planted in
`--selftest` (controls for remote-artifact, non-adjacent, and the still-caught
adjacent drift).

**A cross-tool note worth carrying.** The sibling seat's
`reports/round-27/audit/entry-audit.py` reports the mesoamerica row red too
(`source_digests_mismatched: ['27d6a210bfc3…']`). This seat's reading is that
**both tools are wrong on that row** — the digest belongs to a web-archive
snapshot and the repo path on the bullet is a trail. Recorded rather than
silently diverged.

### X63-H4 — passage locators and brace-compressed citations (fixed)

Two lane conventions read as dead links if taken literally: a **passage
locator** (`file.md:88-98`, `file.md:92,121`) names a line range inside a file
that exists, and a **brace-compressed citation**
(`{design,forms,rules,review}.md`) names several files at once. The first version
reported nine such tokens unresolved. Fixed with line-suffix stripping and brace
expansion; **0 unresolved** after the fix, and each expansion is resolved
individually so a genuinely dead branch of a compressed citation is still named.

## 5. What this seat did not do

- It **adjudicates no claim.** Claim C's C-criterion is measured here (§3) but
  the verdict belongs to the round's runner and auditor. This fragment is
  evidence, not acceptance.
- It **repairs nothing.** X63-E1 is a corpus write and is routed; the filed-corpus
  debt in §6 is routed. Repairing a filed entry belongs to the seat that owns it.
- It **does not re-derive the entry's domain claims**, does not read it in full,
  and takes no position on whether its register-law content is correct — that is
  the D claim's surface.
- It **writes no shared bookkeeping** and touches no filed round-8–26 artifact.

## 6. The filed corpus at the baseline — context for the entry's pin

Run over all **199** tracked `corpus/knowledge/**/*.md` at HEAD `b95fca1`,
`--offline`:

```
entries 199  findings 369
  no-decision-record      179   <- the new-entry bar, reported not graded
  gap-not-named           172   <- the new-entry bar, reported not graded
  sweep-does-not-reproduce  8
  pin-drift                 5
  unresolved-locator        3
  missing-frontmatter       2
pin verdicts: drift 5, re-derived 4, remote-artifact 3, historical-self-digest 2, revision-bound 2, unbound 1
```

The 179/172 rows are the round-10/round-19 **new-entry** bar applied to a corpus
that predates it; the corpus was admitted under `corpus/QUALITY.md`, which
requires provenance, calibration, coupling and usability — not a decision-record
heading. Reported so a consumer sees the instrument's reach; grading them would
invent a retroactive bar.

The **substantive** rows (all defects under any bar):

| class | count | rows |
|---|---:|---|
| stale pin | 5 | `synthesis/typed-label-routing-workflow.md`; `verification/label-channel-routing-verification.md` ×3; `verification/pre-declared-hold-set-reconciliation.md` — the round-19 entries pin the round-18 digests of `tools/d2-typed-labels.py` (`0da0015f…` vs live `2819f687…`), `typed-labels.d4.yml` (`a59990bb…` vs live `d03f6391…`) and `expected-holds.json` (`09490a27…` vs live `d6136488…`) |
| dead locator | 3 | `myth-symbol/flood-traditions.md` → `corpus/myth-symbol/comparative-frameworks.md`; `verification/gate-frozen-run-standard.md` → `corpus/verification/citation-format-and-source-registry.md`; `verification/provenance-audit-ledger-format.md` → `corpus/lessons/provenance-audit-ledger.md` |
| sweep does not reproduce | 8 | `synthesis/{era-material-scoped-reconciliation,finding-disposition-workflow,generated-artifact-lifecycle,hold-set-contract-in-brief}.md`; `verification/{gate-battery-surface-verification,generated-artifact-roundtrip-verification,pre-declared-hold-set-reconciliation,two-reader-interop-agreement}.md` |

**Cross-tool agreement on the pin class.** The sibling `entry-audit.py`'s
`source_digests_mismatched` set is `{mesoamerica-primary-sources,
typed-label-routing-workflow, label-channel-routing-verification,
pre-declared-hold-set-reconciliation}` — its four are a subset of this seat's
five after the X63-H3 fix, and the extra row on each side is explained
(mesoamerica: a shared false positive, §4 X63-H3; `label-channel-routing ×3`:
this seat counts three digests where the sibling counts three as well). Two
independently written instruments converge on the same four entries, which is the
strongest available evidence that the class is real.

## 7. Limits

- The gap and decision-record criteria are the round-10/round-19 **new-entry**
  bar. §6's 179/172 counts are that bar over an older corpus; a consumer must not
  read them as defects.
- **The sweep leg recognises only the `grep -rln "…" <path> → 0 files` form.**
  The round-27 entry uses `grep -rl -i "…" corpus/knowledge/ | wc -l` → **0**,
  which this leg does **not** match, so §3.2's five sweeps were re-run by hand,
  not by the instrument. A consumer must not read the entry's green sweep column
  as instrument-produced. Extending the leg to the `| wc -l` form is the next
  improvement.
- The pin leg grades only digests bound to a named repo path. A digest written
  as prose with no path is reported `unbound` and not scored — the leg errs
  toward silence, so a green pin column is "no bound pin drifted", not "no pin is
  stale".
- URL locators are probed with a bounded HEAD request and the outcome is an
  **observation**, never a finding: a failed fetch cannot distinguish a dead link
  from a dead network. §3's run used `--offline`, so no URL was probed.
- The corpus is a live surface and the round-27 wave was writing throughout.
  Every count binds to the digest printed beside it; a re-read is a new
  measurement. The entry settled at `8dd62923…` after two 30-second reads, and
  X63-E1's live value `c5441e3d…` was re-measured at the final pass.

---

*Receipts: `.scratch/x63-entry.json` (the entry), `.scratch/x63-full-corpus.json`
(199 entries), `.scratch/x63-control-r19entries.json` (the round-19 external
control). Fragment written 2026-10-18.*
