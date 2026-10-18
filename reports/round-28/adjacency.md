# Round 28 — Adjacency / connector (SCRIBE X55)

- **Date:** 2026-10-18. Every timestamp below is UTC from this seat's own runs.
  Command batches are anchored by `date -u` at **20:11:10Z**, **20:11:42Z**,
  **20:13:08Z**, **20:13:25Z**, **20:13:54Z**, **20:14:07Z**, **20:14:26Z** and
  **20:14:28Z**; observations between anchors were taken inside those windows
  (bounded, not individually stamped).
- **Axes:** adjacency (boundary invariants) + connector-surface evidence for the
  three declared claims — **D** (the law replay leg + the RL-4 `packet_keys`
  fix), **O** (the final pin sweep), **C** (the ceiling as craft knowledge) — on
  the surfaces this fragment watches. Read-only cross-checks only; the claims'
  owners land the product.
- **Write scope:** only this fragment. No source fixes, no packet/validator/pin/
  gate/component/corpus edits, no shared bookkeeping, no historical validator
  run, no Git mutation, no commit/push, no sibling writes. `export
  TMPDIR=$PWD/.scratch` was set before every scratch-writing command; scratch
  lived under `.scratch/x55/` (gitignored, lane-internal). No filed rounds 8–27
  byte was written **by this seat** — but see §1, where another seat did.
- **Baseline binding:** declared baseline
  `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede` (`reports/round-28/claims.json:5`);
  observed lane HEAD `69cecbc7dcf575a29f29660ecac470e05260fd86`;
  `git merge-base --is-ancestor 6c0ac44… HEAD` → success (20:11:10Z).
- **Canon:** NON-CANON engineering evidence. No real language, institution,
  script or argot is described, cited or approximated.

## Verdict (scoped to this seat's observations)

**Adjacency: CLEAN at the baseline; TRANSIENTLY BREACHED in the worktree, then
RESTORED before this fragment was filed.**

At 20:11:10Z the round-28 declaration commit `69cecbc7` is a **clean** successor
to the baseline: `git diff --name-status 6c0ac44 HEAD` over
`reports/round-{8..27}`, `examples/`, `tools/` and `corpus/` is **empty**, and the
worktree is **fully clean** (`git status --porcelain=v1 --untracked-files=all` →
0 rows). The only new tracked path is `reports/round-28/{claims,targets}.json`.

Between 20:12:33Z and 20:14:42Z a **filed round-27 artifact was dirty in the
worktree**: `reports/round-27/gate-tests/receipt.json` moved `bdb8d31c…` →
`71e3f455…` (mtime 20:12:33Z), reverting to the committed blob `bdb8d31c…` by
20:14:42Z. §1 shows the change was **verdict-identical** (dates, the `head`
revision and one scratch-path name only). **The breach was transient and is now
healed** — the filed byte is byte-identical to the baseline blob again, so the
end-of-round tree is clean on this path. Two independent records of the window
survive it:

- the **round-28 validator** (20:13:51Z) sampled inside the window and named this
  exact path as its own preservation failure, with
  `baseline_blob 854ed1a3… / observed_blob fbc1f4b6…` (§7.1(i));
- this seat's own `git status` at 20:13:08Z (§1).

Both instruments agree on what moved and on the blob pair, by different methods.
A reader taking the end state alone would see nothing wrong; the window is
recorded here because a validator receipt already preserves it and because the
restore is itself evidence that someone noticed.

**Connector state: four findings, each with an executed control.**

1. **The RL-4 fix landed mid-write, and it is PARTIAL** (§4.1). The packet moved
   `86079a67…` → **`543d68a8…`** (records 175 → 183) when
   `03-orthography.yml` gained `packet_keys: [orthography, records,
   literacy_institutions]` (`de1820b0…` → `0f2ff454…`) and `09-costumes.yml`
   added `enforcement` (`82fb92ad…` → `f61cc684…`). **32 rows now reach the
   packet; 41 rows still do not** — `signs` (20 rows) and `orthography_rules`
   (7) are the bulk. So RL-4 is *closed for the records the round-27 review
   named* (OR-01..03, LI-01..03, EN-01..02 — all eight are now in the packet)
   and *open for the component blocks nobody declared*.
2. **RL-1 stands, re-confirmed on the amended bytes, three ways** (§4.2). A
   tampered law row (`force: "no-such-force"`, and separately
   `speaker: "no-such-speaker"`) produces **byte-identical findings** to the
   unmodified control: 12 vs 12. No tool under `tools/` names a `D4L-LAW-*`
   finding id (`grep -rl D4L-LAW tools/` → **0 files**). The claim's replay leg
   has not landed on the surfaces this seat watches.
3. **The RL-4 landing broke the pin chain and the v3 handoff** (§5, §6). Every
   D4 pin still binds `86079a67…` while the live packet is `543d68a8…`, so
   `typed-pipeline-gate.py` now **FAILs `L1-profile`** (it passed at 20:11:42Z
   on the pre-landing bytes), and `exercise-handoff-e2e.py --profile v3` flipped
   from **exit 0** (20:11:42Z) to **exit 1** (20:13:54Z) with
   `packet_sha256=(not assembled)`. This is the O claim's cascade, arriving
   mid-round, not repaired here.
4. **A path-dependent finding count in `d2-typed-labels.py`** (§3) — a
   methodological trap for any seat that copies the packet to scratch to tamper
   it. The projector infers the family from the **parent directory name**
   (`tools/d2-typed-labels.py:2477-2486`), so a copy under `.scratch/…` silently
   resolves as family `d2` and reports **16** findings instead of **12**. This
   seat's own first RL-1 probe was polluted by it and is discarded (§4.2).

**The round-28 validator landed at 20:13:51Z and reads D `false` / O `false` /
C `false`** (`acceptance_checks_passed: false`, 19 failures). §7 gives each
failure group and this seat's independent reading. The receipt is the round's own
record; this fragment does not adjudicate it.

## 1. Boundary observations

Batch at **20:11:10Z**, from the lane root, `PYTHONDONTWRITEBYTECODE=1`:

- `git rev-parse HEAD` → `69cecbc7dcf575a29f29660ecac470e05260fd86`;
  `git log --oneline -2` → `69cecbc round-28: declare claims D/O/C …`, then
  `6c0ac44 round-27: admit D/O/C …` (the declared baseline).
- `git merge-base --is-ancestor 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede HEAD`
  → **success**. The baseline is an ancestor, not a sibling.
- `git diff --name-status 6c0ac44 HEAD -- reports/round-8 … reports/round-27`
  → **empty**. Same command over `examples/ tools/ corpus/` → **empty**. So the
  declaration commit added only `reports/round-28/{claims,targets}.json` and
  moved no artifact the claims measure.
- `git status --porcelain=v1 --untracked-files=all | wc -l` → **0** at
  20:11:10Z. The tree was fully clean, including untracked files.
- **Interface files, blob-compared baseline→HEAD:** `corpus/README.md`
  `d9d97d7f…` at both baseline and HEAD (SAME at that stamp; it moved later —
  §5.4); `reports/round-27/gate-tests/receipt.json` `bdb8d31c…` at baseline and
  HEAD, i.e. the *committed* blob is untouched; the worktree copy is what moved.

**The breach, measured.** At 20:13:08Z:

```
$ git status --porcelain=v1 --untracked-files=no
 M corpus/README.md
 M reports/round-27/gate-tests/receipt.json
```

`reports/round-27/gate-tests/receipt.json`: committed blob `bdb8d31c…`, worktree
`71e3f455…`, mtime 20:12:33Z. Its writer is the file's own re-runner:
`reports/round-27/gate-tests/run-gate-tests.py:820-821` writes
`HERE / "receipt.json"` in place. Whoever re-ran it therefore rewrote a filed
round-27 artifact.

**The control that scopes the breach (executed).** Stripping only the volatile
keys (`date`, `head`, `copy`) from both revisions and comparing the rest as
canonical JSON:

```
verdict-identical after stripping date/head/copy: True
```

and the raw line-level diff is exactly 24 removed / 24 added lines, of which the
only non-`date` rows are:

```
- "head": "b95fca1e40f32f7346937ab6426f9ccca60e319f",
+ "head": "69cecbc7dcf575a29f29660ecac470e05260fd86",
-  "copy": ".scratch/r27-d13/law-tree-616939",
+  "copy": ".scratch/r27-d13/law-tree-84893",
```

So: **no verdict, exit code, finding id or command changed** — every measured
value in the receipt is the same. The breach was one of *form* (a filed byte
moved in place) and not of *content*. Both readings are reported; a reader who
wants "nothing of substance moved" has it, and a reader who wants "the
re-pin-is-a-NEW-row rule was honoured" does not — for the window, at least.

**The restore, measured.** At 20:15:06Z the path is clean again:

```
$ sha256sum reports/round-27/gate-tests/receipt.json
bdb8d31c1cdf503e598bdcd55fdfb756b6dd8c12b0f50ff2acfafd7fa9883e28  reports/round-27/gate-tests/receipt.json
$ git show HEAD:reports/round-27/gate-tests/receipt.json | sha256sum
bdb8d31c1cdf503e598bdcd55fdfb756b6dd8c12b0f50ff2acfafd7fa9883e28  -
$ git status --porcelain=v1 --untracked-files=no -- reports/round-27/
(empty)
```

mtime 20:14:42Z. The worktree byte equals the committed blob again, so the
end-of-round tree carries **no** filed-round-8-27 modification. The window is
recorded rather than retracted because the validator's receipt (sampled inside
it) is a filed artifact that already preserves it, and because a later reader
comparing the receipt to the tree needs to know the receipt describes a state
the tree no longer has.

**The round-28 validator agrees, independently.** `reports/round-28/validation.json`
(20:13:51Z) carries its own preservation block naming this exact path and no
other (§7.1).

## 2. The connector surfaces this fragment watches

The "before" column is this seat's first read (20:11:42Z, pre-landing); the
"after" column is its last read (**20:14:26Z**). A later stamp can move them
again. **Every digest below is the full sha256**, because the validator's re-pin
predicate matches the complete string and a truncated digest does not match.

| surface | path | at 20:11:42Z | at 20:14:26Z |
|---|---|---|---|
| D4 packet | `examples/culture-d4/packet.d4.yml` | `86079a67…` | **`543d68a8…`** |
| orthography component | `examples/culture-d4/components/03-orthography.yml` | `de1820b0…` | **`0f2ff454…`** |
| costumes component | `examples/culture-d4/components/09-costumes.yml` | `82fb92ad…` | **`f61cc684…`** |
| brief component | `examples/culture-d4/components/01-brief.yml` | `649aa111…` | `649aa111…` (unmoved) |
| lexicon component | `examples/culture-d4/components/04-lexicon.yml` | `d0d4e17c…` | `d0d4e17c…` (unmoved) |
| register-law component | `examples/culture-d4/components/13-register-law.yml` | `c0d77181…` | `c0d77181…` (unmoved) |
| D4 projection | `examples/culture-d4/typed-labels.d4.yml` | `88a94422…` | **`339bfd83…`** |
| D4 typed packet | `examples/culture-d4/packet.d4.typed.yml` | `1c4b8808…` | **`15c81ec1…`** |
| D4 expected holds | `examples/culture-d4/expected-holds.json` | `857417e9…` | `857417e9…` (unmoved) |
| live pin profile | `tools/gates/typed-pipelines.json` | `69f250df…` (`repin.round: 27`) | `69f250df…` — **now STALE** |
| argot gate | `tools/gates/argot-derivation-gate.py` | `b5406bcd…` | `b5406bcd…` (unmoved) |
| typed-pipeline gate | `tools/gates/typed-pipeline-gate.py` | `b749ad07…` | `b749ad07…` (unmoved) |
| assembler | `tools/assemble-culture-d4.py` | `943f487b…` | `943f487b…` (unmoved) |
| corpus README | `corpus/README.md` | `d9d97d7f…` | **`d62e6404…`** (revision 1.8) |
| register-strata entry | `corpus/knowledge/linguistics/register-strata-attestation.md` | `0d993a26…` (12 sections) | `0d993a26…` (unmoved) |
| round-27 gate receipt | `reports/round-27/gate-tests/receipt.json` | `bdb8d31c…` | **`fbc1f4b6…`** at 20:13:08Z, **restored to `bdb8d31c…`** by 20:14:42Z (§1) |
| frozen generations | `tools/gates/frozen/**/MANIFEST.tsv` | 11 manifests | 11 — **no `round-27/`, no `round-28/`** |
| baseline generations | `tools/gates/expected/**/expected.json` | 16 baselines | 16 — **no `r27-*`, no `r28-*`** |
| knowledge corpus | `corpus/knowledge/**` | 200 files | 200 files |
| counting command | `reports/round-28/run-validation.py` | absent | **present, 93,407 B**; receipt present (§7) |

Full digests of the moved surfaces, written out for a re-pin seat:

```
examples/culture-d4/packet.d4.yml                  543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f
examples/culture-d4/components/03-orthography.yml  0f2ff45439fd7db3e9014bd1012bd917e42d042f457b8cef2bed2c9a791d4e1b
examples/culture-d4/components/09-costumes.yml     f61cc6845518d44f50e5179339a1a2fda2c5290efb52d6badb28cbec87768c23
examples/culture-d4/typed-labels.d4.yml            339bfd83bf66832479b5b8ffbbce708c8be15e13b08967fa7049b848661a3cf8
examples/culture-d4/packet.d4.typed.yml            15c81ec11b42efaa7d683dd9320bfc7cd9b5d1e812e042d99dbf8d8726ec5da6
corpus/README.md                                   d62e6404aef8a8d7143e23c95f134b813341d240c1b705efcea4fcf61f2b21a0
```

Unmoved surfaces, same purpose (a re-pin seat should not move these):

```
examples/culture-d4/components/01-brief.yml        649aa111db2e57a737234330690ea4fbb197039ba8ecf92d6248d1bed8ea793b
examples/culture-d4/components/04-lexicon.yml      d0d4e17cc3c43a11e598259271fe16f18539c8bce3c3a30a40b6d2554b6c7240
examples/culture-d4/components/13-register-law.yml c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7
examples/culture-d4/expected-holds.json            857417e949fb5cb9b265918b8982ca86e47a820d136ba7b009414d84aa4ec28f
tools/gates/typed-pipelines.json                   69f250df363d70a2001840ab37f4f947e28244b4ac053a5a79d4a92860822f7a
tools/gates/argot-derivation-gate.py               b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb
tools/gates/typed-pipeline-gate.py                 b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85
tools/assemble-culture-d4.py                       943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2
```

**This fragment is a re-pin row.** It names the drifted surfaces and carries
their live digests, dated and command-carrying. It records the digests; it edits
no pinned file, and a re-pin is a NEW row under the lane's rules.

## 3. Finding X55-C1 — the `d2-typed-labels.py` path-dependent finding count

**The trap.** `tools/d2-typed-labels.py` resolves the pipeline family from the
packet's **parent directory name**, not from its contents:

```
tools/d2-typed-labels.py:2477  def packet_family(packet_path):
tools/d2-typed-labels.py:2484      match = re.fullmatch(r"culture-([a-z0-9]+)",
                                   pathlib.Path(packet_path).parent.name)
tools/d2-typed-labels.py:2486      return match.group(1) if match else DEFAULT_FAMILY
tools/d2-typed-labels.py:2471  DEFAULT_FAMILY = "d2"
```

So any copy of the D4 packet whose parent directory is not named `culture-d4`
silently resolves as family **`d2`** and is graded by the D2 rank machinery.

**Two-sided control, executed** (20:13:25Z / 20:14:07Z; same bytes, only the
parent directory name differs):

| packet | parent dir | family resolved | `grep -c FINDING` |
|---|---|---|---|
| `examples/culture-d4/packet.d4.yml` | `culture-d4` | `d4` | **12** |
| `.scratch/x55/A/control.yml` | `x55` | `d2` | **16** |
| `.scratch/x55/fam/culture-d4/control.yml` | `culture-d4` | `d4` | **12** |
| `examples/culture-d4/.x55-probe.yml` | `culture-d4` | `d4` | **12** |

The four extra rows the mis-resolved copy emits are all D2 rank findings:

```
> FINDING D2L-RANK: [hold] TR-04#a|TR-06#a — act-collision: genuine-priority-gap
> FINDING D2L-RANK: [hold] WR-02#g|WR-09#g — R-05-class: genuine-priority-gap
> FINDING D2L-RANK: [hold] WR-08#g|WR-09#g — R-05-class: genuine-priority-gap
> FINDING D2L-RANK: [note] SR-01#a|SR-01#b — act-collision: band-keyed-pair
```

**Consequence, and it is a trap for this round specifically.** Round 28's D claim
requires tamper controls, and the cheapest way to tamper is to copy the packet
to scratch and edit one field. Done naively, the *control* copy already reports
16 findings while the live packet reports 12 — so a seat comparing
`control` to `tamper` sees a difference caused entirely by the copy's path, and
a seat comparing `live` to `tamper` sees four spurious "new" findings. **A tamper
control must keep the copy's parent directory named `culture-d4`.** This seat's
own first probe fell into it and is discarded in §4.2.

**Disposition.** Reported, not repaired. The behaviour is deliberate and
documented in the function's own docstring ("A packet outside that convention
keeps the D2 default, so every pre-round-20 invocation resolves exactly as it
did"), and the same convention is used by
`tools/gates/typed-pipeline-gate.py`'s `family_of`. Changing it is a source edit
outside this seat's write scope and would move a pinned tool digest.

## 4. Claim D's two clauses, measured on the delivered bytes

### 4.1 The RL-4 `packet_keys` fix — LANDED, and partial

**Before (20:11:42Z).** Neither component declared the blocks the round-27 review
named. Measured with the assembler's own declaration rule
(`tools/assemble-culture-d4.py:258-266`: a component contributes exactly its
declared `packet_keys`, else the whole `PACKET_KEYS` tuple):

```
examples/culture-d4/components/03-orthography.yml   no top-level packet_keys
examples/culture-d4/components/09-costumes.yml      packet_keys: [costumes, materials, cloth_sources, rank_rules, form_slots]
examples/culture-d4/components/01-brief.yml:157     C-09 registers [costumes, materials, cloth_sources, rank_rules]
```

Both facts are load-bearing and they are **different facts**:

- `03-orthography.yml` declared **no** `packet_keys` at all, so the assembler
  should have fallen back to `PACKET_KEYS` and shipped everything it could —
  but `records`, `signs`, `orthography_rules`, `numeral_register`,
  `literacy_institutions`, `lexicon_requests`, `consistency_checks` and
  `open_questions` are **none of them in `PACKET_KEYS`** (46 keys, measured by
  parsing the tuple), so they were all recorded under `assembly.skipped_keys`
  instead.
- `09-costumes.yml` declared `form_slots` but **not** `enforcement`; `01-brief.yml`'s
  registry row for `C-09` omitted `form_slots` too, so the registry and the
  component **disagreed** — the component's own declaration is what the
  assembler honours (`:258`), and it carried `form_slots` into the packet, so
  `form_slots` was never actually lost. `enforcement` and `legibility` were.

**After (20:13:25Z).** The fix landed as a declaration change on both components:

```
examples/culture-d4/components/03-orthography.yml:24  packet_keys: [orthography, records, literacy_institutions]
examples/culture-d4/components/09-costumes.yml:22     packet_keys: [costumes, materials, cloth_sources, rank_rules, form_slots, enforcement]
```

and the packet gained exactly three new top-level blocks, measured by diffing the
top-level key set of `HEAD:` against the live file:

```
added blocks: ['enforcement', 'literacy_institutions', 'records']
removed blocks: []
```

**The eight records the round-27 review named are all now in the packet.** Counted
by `grep -c` on the live packet (20:13:25Z):

| id | round-27 status | now |
|---|---|---|
| OR-01 / OR-02 / OR-03 | absent | **2 / 3 / 3 hits** |
| LI-01 / LI-02 / LI-03 | absent | **1 / 1 / 1 hits** |
| EN-01 / EN-02 | absent | **1 / 1 hits** |

The argot gate's own coverage line confirms the packet grew:
`records=175` → **`records=183`** (20:13:25Z), with
`register_scoped=14 derived_pairs=8 violations=0 rule_holds=0` unchanged.

**What the fix did NOT close.** Counting the component blocks that still never
reach the packet, by the same declaration rule:

| component | block | rows | in packet? |
|---|---|---|---|
| `03-orthography.yml` | `records` | 3 | **yes** (fixed) |
| `03-orthography.yml` | `literacy_institutions` | 3 | **yes** (fixed) |
| `03-orthography.yml` | `signs` | **20** | **no** |
| `03-orthography.yml` | `orthography_rules` | **7** | **no** |
| `03-orthography.yml` | `lexicon_requests` | 4 | **no** |
| `03-orthography.yml` | `consistency_checks` | 4 | **no** |
| `03-orthography.yml` | `numeral_register` | 0 | **no** |
| `03-orthography.yml` | `open_questions` | 3 | **no** |
| `09-costumes.yml` | `enforcement` | 2 | **yes** (fixed) |
| `09-costumes.yml` | `legibility` | 1 | **no** |
| `09-costumes.yml` | `form_slots_note`, `rank_rules_note` | 1+1 | **no** |
| `09-costumes.yml` | `open_questions` | 2 | **no** |

So **32 rows now reach the packet and 41 still do not.** The residual is not a
`packet_keys` defect on the named records — it is the *undeclared remainder*:
`signs` alone is 20 of the 41, and the twenty sign records are the script's own
inventory, which a consumer of the packet would reasonably expect. The claim's
`after_required` says "the components declare `packet_keys`; the records reach
the packet" — **true for the records the `before` text names, false for the
component blocks as a whole.** A later round that wants the script inventory in
the packet must declare `signs` (and `orthography_rules`) as well, and
`PACKET_KEYS` does not contain either name, so declaring them is the only route.

**Honesty of the named-holds set, checked.** The claim asks the named-holds set
be "updated honestly". `examples/culture-d4/expected-holds.json` is **unmoved**
(`857417e9…` at both stamps) and still reads `12 hold / 0 note / 0 fail` with a
`revision_note` that names the **round-27** landing and says nothing about
round 28 or RL-4. The validator names this too (§7, failure 7). A packet that
gained three blocks and eight records without moving its hold set is internally
consistent — a law row and an institution row are not forms — but the note is
now stale about which round produced the bytes it pins.

### 4.2 The law's replay leg — RL-1 stands, re-confirmed on the amended bytes

**The probe.** Take the live packet, rewrite exactly one field of the first law
row, and compare the findings the delivered typed pipeline emits. The copy's
parent directory is named `culture-d4` so §3's family trap does not pollute the
measurement.

```
control   = packet.d4.yml, byte-identical copy at .scratch/x55/fam/culture-d4/control.yml
tamper    = same bytes with RGL-01 force: "directive-binding for the charge…" → "no-such-force"
tamper2   = same bytes with RGL-02 speaker: "stamp-holder only — no master, no delegate" → "no-such-speaker"
```

| packet | `grep -c FINDING` | reading |
|---|---|---|
| `control` (unmodified, family-correct path) | **12** | baseline |
| `tamper` (illegal `force`) | **12** | **indistinguishable** |
| `tamper2` (illegal `speaker`) | **12** | **indistinguishable** |

and the finding sets are identical row-for-row (`diff … >/dev/null` → equal).

**The control that makes this a measurement rather than an artifact.** A first
probe copied the packet to `.scratch/x55/A/` (parent dir `x55`), where §3's trap
made *both* the control and the tamper report 16 — the comparison was then
meaningless. Re-run with the parent directory named `culture-d4`, the count is
12/12/12. **The discarded run is reported because it is the reason the second run
exists**, and because it is exactly the trap a sibling tamper seat will hit.

**Second route, no lane code.** `grep -rl D4L-LAW tools/` → **0 files**; the
string exists only in round-28's own auditor scripts and the runner
(`reports/round-28/audit/x59-register-law-negatives.py`,
`reports/round-28/scribe/x54-law-negatives-spotcheck.py`,
`reports/round-28/run-validation.py`). So the claim's named `D4L-LAW-*` finding
class is a **requirement**, not a delivered artifact, at 20:14:07Z.

**Third route — the gate's own exit, controlled.** `typed-pipeline-gate.py` on the
tampered copy reports `FAIL L1-profile`; so does the gate on the **unmodified**
control copy and on the live packet, with an identical message naming the same
two pinned-vs-live digests:

```
FAIL L1-profile: packet: pins 86079a6708a0, live 543d68a82640 (examples/culture-d4/packet.d4.yml);
                 projection: pins 88a94422b412, live 339bfd83bf66 (examples/culture-d4/typed-labels.d4.yml)
```

The `FAIL` is **pin drift from the RL-4 landing (§5)**, not tamper detection: it
is byte-identical across all three inputs. A seat that read this `FAIL` as "the
gate caught my tamper" would be reporting the wrong cause.

**Scoped reading.** RL-1's `before` text — *"a tampered law row … emits the same
12 findings as a clean one"* — **reproduces exactly**, on the amended packet, at
20:14:07Z, under three independent instruments. The law is declared and wired; it
is still not enforced, and the claim's replay leg has not landed on any surface
this fragment watches.

## 5. Claim O's pin surface: the cascade is mid-flight and real

### 5.1 The live pin surface is now stale, and it was consistent two minutes earlier

At **20:11:42Z** (pre-landing) the D4 pins agreed with the tree and the
typed-pipeline gate was green: `summary: 20/20 legs passed`, exit 0.

At **20:13:25Z**, after the RL-4 landing:

| surface | pinned | live | reading |
|---|---|---|---|
| `typed-pipelines.json` profile `d4` packet | `86079a67…` | `543d68a8…` | **DRIFT** |
| `typed-pipelines.json` profile `d4` projection | `88a94422…` | `339bfd83…` | **DRIFT** |
| `expected-holds.json` `packet_sha256` | `86079a67…` | `543d68a8…` | **DRIFT** |
| `expected-holds.json` `projection_sha256` | `88a94422…` | `339bfd83…` | **DRIFT** |
| `typed-pipelines.json` `repin.round` | `27` | round-28 landing | **stale** |

```
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
FAIL L1-profile: packet: pins 86079a6708a0, live 543d68a82640 …
```

**Both clauses of the same command, two stamps apart**, is the control: the
`FAIL` is caused by the landing, not by the tool, the TMPDIR or the invocation.
The typed packet still runs green (`examples/culture-d4/packet.d4.typed.yml` →
exit 0, 17 legs) because it is the *other* surface.

### 5.2 `typed-pipelines.json` and `expected-holds.json` did not move

Both files are byte-unmoved (`69f250df…`, `857417e9…`). The re-pin discipline
("a re-pin is a NEW row") has not been exercised this round on these two: their
pins are simply stale. That is the O claim's outstanding work, and it is
**mid-flight** at this stamp, not absent.

### 5.3 No round-28 frozen generation and no `r28-*` baseline exists

```
tools/gates/frozen/round-27  → absent        tools/gates/frozen/round-28  → absent
tools/gates/expected/*/r27*  → no match      tools/gates/expected/*/r28*  → no match
```

11 frozen manifests and 16 baselines, unchanged from round 27. The round-27
`pinsweep/baselines/{d4-assembly-check-gate,d4-typed-labels-check-gate}/r27-post/`
snapshot trees are committed under `reports/round-27/` and are **superseded** —
they freeze the pre-RL-4 packet.

### 5.4 `corpus/README.md` moved — the C surface

`corpus/README.md` `d9d97d7f…` → **`d62e6404…`** (mtime 20:12:xxZ), gaining a
`revision: 1.8` block and correcting the counts footer from `(total 199 files;
directory totals 19/19/18/29/20/94)` to **`(total 200 files; directory totals
20/19/18/29/20/94)`**, preserving the superseded reading beneath it as a dated
record. This seat's own census at 20:11:42Z had already measured **200 files**
with directory totals 94/20/19/29/18/20 — so the footer correction is right and
the superseded 199 was the stale claim. It is a new revision block, not an
in-place edit of revision 1.7, which is the correct form.

### 5.5 The current gate surface, measured

| command | stamp | exit | result |
|---|---|---|---|
| `tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 20:11:42Z | 0 | `20/20 legs passed` |
| same | 20:13:54Z | 0 | `FAIL L1-profile` (pin drift) |
| `tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | 20:11:42Z | 0 | `records=175 … violations=0 rule_holds=0` |
| same | 20:13:25Z | 0 | `records=183 … violations=0 rule_holds=0` |
| `tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | 20:13:25Z | 0 | 17 legs, exit 0 |
| `tools/check-gate-battery.py` | 20:13:54Z | 0 | `pass 7 / fail 0 / unevaluable 0`, `coverage 9/9`, `pinned 19/19`, `preserved: true` |
| `tools/exercise-handoff-e2e.py --profile v3 --quiet` | 20:11:42Z | 0 | `fields=16/16 … packet_sha256=6ea03f42…` |
| same | 20:13:54Z | 1 | `packet_sha256=(not assembled)` |
| `tools/exercise-handoff-e2e.py --profile v2 --quiet` | 20:11:42Z | 0 | `claims=15 links=50/50 drift=named` |

**The battery reads `pinned 19/19` while `typed-pipeline-gate.py` FAILs**, and
that is not a contradiction: the battery verifies each baseline's **committed
snapshot copy** (`tools/check-gate-battery.py:573`, `target = base_dir /
relative`), never the live tree. It is the same false-comfort signal round 27
named. **A green battery is not evidence the live pins hold.**

**The v3 flip is the clearest single control in this fragment.** The identical
command, same TMPDIR, same shell, two minutes apart, flips 0 → 1, and the
selftest names the exact cause:

```
Failed: examples/culture-d4/expected-holds.json packet_sha256: the tree recorded 86079a6708a0… for
        examples/culture-d4/packet.d4.yml but the bytes measure 543d68a82640…
```

That is the RL-4 landing breaking the handoff baseline — the cascade claim O
exists to absorb.

### 5.6 The replay matrix, both TMPDIR directions

Round 27's finding X55-C1 (the `replay-frozen` TMPDIR trap) **reproduces**: with
the lane's mandated `export TMPDIR=$PWD/.scratch`, every row reads
`could-not-evaluate reason=mirror_unsafe`. With `TMPDIR=/var/tmp`, the same
manifests give real verdicts. All 11 manifests, outside-TMPDIR direction
(20:11:42Z, `TMPDIR=/var/tmp`):

| manifest | exit | reproduced | mismatch | could-not-evaluate |
|---|---:|---:|---:|---:|
| `round-3/MANIFEST.tsv` | 2 | 0 | 0 | 7 |
| `round-3/attempt-1/MANIFEST.tsv` | 2 | 0 | 0 | 7 |
| `round-11/MANIFEST.tsv` | 2 | 10 | 0 | 1 |
| `round-18/MANIFEST.tsv` | 1 | 0 | **2** | 0 |
| `round-18/repin-d2/MANIFEST.tsv` | 2 | 10 | 0 | 1 |
| `round-20/repin-d2/MANIFEST.tsv` | 2 | 10 | 0 | 1 |
| `round-22/d4-repin/MANIFEST.tsv` | 2 | 0 | **2** | 1 |
| `round-23/repin-d2/MANIFEST.tsv` | 2 | 10 | 0 | 1 |
| `round-25/gate-input/MANIFEST.tsv` | 2 | 0 | 0 | 6 |
| `round-26/gate-input/MANIFEST.tsv` | 1 | 4 | **2** | 0 |
| `round-26/post-register/MANIFEST.tsv` | 1 | 4 | **2** | 0 |

**No generation is green.** The two round-26 generations were `4 reproduced / 2
mismatch` **before** the RL-4 landing too (measured at 20:11:42Z on the
pre-landing bytes) — so this is not new damage from round 28; it is the
already-filed cascade from the round-27 register landing, which round 27's own
fragment recorded. `post-register` was 6/6 OK at round-27's 19:15Z and has been
red since the round-27 D landing. The O claim's "all replays green" remains
**unmet**, and it is unmet for a reason that predates this round.

Sibling seat `reports/round-28/sweep/_prelanding-census.md` reproduces the same
matrix from its own instrument (121 surfaces, 31 findings) — **convergence, not
inheritance**; the two sweeps share no code.

## 6. Claim C — the corpus surface, cross-checked

Batch 20:11:42Z / 20:14:07Z, `python3 tools/source-audit-inventory.py --json
--summary --root corpus/knowledge`:

```
totals.files 200
```

| partition | measured | README 1.7 declares | README 1.8 declares |
|---|---|---|---|
| civilizations | 94 | 94 | 94 |
| culture-material | 18 | 18 | 18 |
| linguistics | **20** | 20 | 20 |
| myth-symbol | 19 | 19 | 19 |
| synthesis | 29 | 29 | 29 |
| verification | 20 | 20 | 20 |
| **total** | **200** | **200** | **200** |

README row↔file reconciliation, parsed from the `` - `x.md` `` rows:

```
README rows: 200    files: 200
rows missing a file: []   files missing a row: []   duplicate rows: []
```

**The C claim's product has NOT landed.** `corpus/knowledge/linguistics/` holds
**20** files at both stamps — the same 20 the baseline had (the entry that landed
in round 27 is `register-strata-attestation.md`, committed at `6c0ac44`). The
named ceiling-amendment target is byte-unmoved: `register-strata-attestation.md`
`0d993a26…` at 20:11:42Z and at 20:14:26Z, **12 `## ` sections**, no new
section. The validator agrees and names it (§7).

**What is true on this surface.** Round 27's `register-strata-attestation.md`
*already* carries the ceiling as craft knowledge — measured by `grep`:

- `:222-236` §6 states the constraint and the general lesson ("A register's
  derivational mechanism silently decides which semantic classes can enter the
  register"), with the measured `27 plain / 18 reverse-legal / 9 reverse-ILLEGAL`;
- `:288` the `RSA-4` rule row names "§6, measured `0 legal / 5 illegal` over the
  drill's institutional abstractions".

So the *substance* the C claim wants recorded is on disk — in the round-27
entry, as a section of it. What is missing is the **form** the claim asks for: a
round-28 **amendment entry** (a new section) plus a **separate new sourced
knowledge entry** on register-lexicon ceilings. Those are absent at this stamp.

## 7. Regressions re-run (controls for "no axis harmed")

All legs in §5.5 are this seat's own runs, dated, with the command named. Every
leg whose exit is 0 at its stamp is marked; the two that flip are marked with
both readings and their cause. **The `replay-frozen` manifests are NOT claimed
green** (§5.6).

### 7.1 The round-28 validator landed at 20:13:51Z and reads D/O/C all `false`

`reports/round-28/run-validation.py` (93,407 B, `f673f7a7…`) appeared at
20:13:38Z; `reports/round-28/validation.json` (227,034 B) at 20:13:51Z. The
receipt's `runner_sha256` `f673f7a7…` **matches** the runner on disk — so,
unlike round 27's 10-second rewrite race, this receipt and this runner are the
same revision. This seat did **not** run the validator; it read the receipt.

| claim | receipt's `passed` |
|---|---|
| **D** | **false** |
| **O** | **false** |
| **C** | **false** |

`acceptance_checks_passed: false`, 19 failures. Each group, with this seat's
independent reading:

**(a) Claim D — "this runner's own law reader reports 7 finding(s) on the
delivered packet."** The receipt's reader flags `register: "stamp"` as "names no
declared register id" on RGL-01..03 and `RGL-04`'s consequence as naming no
roll/rank machinery. **This is a reader disagreement, not a delivered-bytes
defect**, and the runner says so itself in its `limits`: it "reports both
readings rather than adjudicating silently". Measured directly at 20:14:07Z:
`register: "stamp"` **is** the declared register id — `13-register-law.yml:54`
states `register: "stamp (04-lexicon.yml registers QREG-02, class marked…)"`,
and the packet's `registers` block carries `QREG-02` with `register: stamp`.
RGL-04's consequence is a **negative** rule ("the register owns no segment"), so
"names no roll/rank machinery" is true of a rule whose whole content is that it
names none. Both are the runner's own reading of prose, as its limits declare.

**(b) Claim D — "no tool under `tools/` names a `D4L-LAW-*` finding id."**
**Reproduced independently** by this seat: `grep -rl D4L-LAW tools/` → **0
files** (20:14:07Z). This is the same fact as this fragment's §4.2 third route.

**(c) Claim D — "the delivered checking leg names no `D4L-LAW-*` finding on the
force / speaker / consequence tamper."** **Reproduced independently** by this
seat: 12 findings on the clean packet, 12 on each tamper, identical sets (§4.2).
The receipt's three tampers are its own construction; this seat's are its own,
with the family-path trap controlled.

**(d) Claim D — "d4-gate is not green (exit 2)" and "the D4 hold set's revision
note does not name the round-28 landing / the RL-4 fix."** The gate's `FAIL` is
pin drift, measured above (§5.1, §5.5) and shown to be independent of any
tamper. The hold-set note is genuinely stale (§4.1, last paragraph) — a real
record-keeping gap, correctly named.

**(e) Claim O — "8 D4 surface(s) drifted and no round-28 structured re-pin row
landed."** The drift list the receipt names (`01-brief.yml`, `03-orthography.yml`,
`04-lexicon.yml`, `09-costumes.yml`, `expected-holds.json`,
`packet.d4.typed.yml`) is a superset of what this seat measured as moved (§2):
this seat's moved set is `{packet.d4.yml, 03-orthography.yml, 09-costumes.yml,
typed-labels.d4.yml, packet.d4.typed.yml}`, and `01-brief.yml` / `04-lexicon.yml`
/ `expected-holds.json` are **unmoved** here (`649aa111…`, `d0d4e17c…`,
`857417e9…`). §2 of this fragment **is** a re-pin row for the moved surfaces and
carries their live digests in full.

**(f) Claim O — "replay handoff-v3 is not green (exit 1)" / "handoff-v3-selftest
is not green (exit 1)" / "the v3 replay is red and no round-28 successor baseline
replays green."** **Reproduced independently** by this seat (§5.5, §5.6): v3 was
exit 0 at 20:11:42Z and exit 1 at 20:13:54Z, with the selftest naming the
`expected-holds.json packet_sha256` mismatch as the cause. The receipt's
`handoff-v3-selftest` exit 1 is the same fact from the runner's route.

**(g) Claim O — "Regression failed: typed-pipeline-gate.py … (exit 2, exit 1)."**
The receipt records exit 2; this seat measured exit 0 with a `FAIL L1-profile`
line at 20:13:54Z, and exit 0 with `20/20 legs passed` at 20:11:42Z. The gate
prints `FAIL` and still exits 0 in this seat's invocation; the runner's exit 2
is a different invocation (likely with a TMPDIR or path it sets itself). Both
readings are reported; this seat does not adjudicate which is canonical.

**(h) Claim C — "no new section was added … the ceiling is not recorded as an
amendment entry" / "no new entry landed under `corpus/knowledge/linguistics`."**
**Reproduced independently** by this seat (§6): the entry is byte-unmoved at
`0d993a26…` with 12 sections at both stamps, and `linguistics/` holds 20 files at
both. The receipt's `amendment_sections: []`, `baseline_sections: 12`,
`live_sections: 12`, `bytes_before == bytes_after == 57996` matches this seat's
`grep -c "^## "` → 12 and the unchanged digest.

**(i) Preservation — "Filed rounds 8-27 or their frozen generations differ from
the declared baseline."** The receipt names exactly one path:

```
"baseline_blob": "854ed1a37805a7f848ca2d17e8f005a34788b592",
"observed_blob": "fbc1f4b6c0fa1edbbde738cd7f801575079b881a14f25a1b94e684a35fd5a8f0",
"path": "reports/round-27/gate-tests/receipt.json"
```

with `protected_paths: 1587`, `differences_total: 1`,
`protected_status_rows: 1`. **This is the same breach this seat found
independently at 20:13:08Z, by a different instrument** (§1) — the runner
compares protected Git blobs to working bytes, this seat compared
`git status` plus a key-stripped JSON diff. Convergence, not inheritance; the
two instruments do not share machinery.

**The receipt is therefore stale about the tree, in the direction of being
worse.** The path was restored to the committed blob at 20:14:42Z, **after** the
receipt was written at 20:13:51Z, so the receipt's preservation failure describes
a window that has closed. This is a real reading hazard for the parent: a
re-run of the same runner after 20:14:42Z would report `differences_total: 0` on
this path, and the receipt's `1` would look unreproducible. It is not
unreproducible — it is a timestamped observation of a transient state, and §1
carries both stamps.

### 7.2 What this fragment does and does not do about the verdict

- It **does not** adjudicate the round. The receipt stands as filed.
- It **does** report that three of the receipt's failure groups are
  **independently reproduced** by this seat's own instruments (b, c, f, h) and
  that one (i) is corroborated by a different method.
- It **does** report that two groups are **reader disagreements rather than
  delivered-bytes defects** (a), as the runner's own `limits` declare, and that
  one (g) is an invocation difference this seat cannot reconcile without running
  the runner.
- It **does** carry the moved surfaces' live digests in full (§2), so a re-pin
  seat and a re-run at a later stamp have them.

## 8. Limits and non-claims

- No round acceptance, no promotion claim, no canon/rights/freshness
  certification. `reports/round-28/run-validation.py` **did not exist** at
  20:11:10Z and appeared at 20:13:38Z; its receipt's verdict (D/O/C all
  `false`) is reported in §7.1 but **not adjudicated here**, and this seat did
  not run the validator. Nothing here substitutes for it.
- **This fragment's §2 digest table is intended as a re-pin row.** Whether it
  satisfies the runner's predicate is the parent's measurement, not this seat's
  claim.
- **The round-28 wave was in flight at every observation.** `reports/round-28/`
  gained `audit/*`, `sweep/*`, `readme/*`, `scribe/*`, `availability.json`,
  `run-validation.py`, `validation.json` and `gate-tests/receipt.json` between
  20:11Z and 20:16Z, and the **D4 surface moved at ~20:12–20:13Z** (§4.1). The C
  and O products had **not** landed at 20:16:03Z (§5.3, §5.4, §6): the
  register-strata entry is still byte-unmoved at 12 sections, `linguistics/`
  still holds 20 files, no `reports/round-28/handoff/` directory exists, and the
  D4 pins are still stale. One further worktree path moved late —
  `tools/exercise-handoff-e2e.py` appeared modified at 20:16:03Z, and the v3
  handoff then read **exit 2** (was exit 1 at 20:13:54Z, exit 0 at 20:11:42Z),
  i.e. a seat is actively working the v3 re-point. Every number in this fragment
  is stamped, and a reader comparing it to a later stamp should expect the D4 and
  v3 rows to differ and re-measure them.
- **The breach in §1 is a reported observation of a closed window, not an
  accusation.** This seat did not identify which seat re-ran the round-27
  receipt; it measured that a filed byte moved in the worktree between 20:12:33Z
  and 20:14:42Z, that the committed blob never changed, that the change was
  verdict-identical, and that the worktree byte was **restored** to the committed
  blob before this fragment was filed. The end state is clean. The window is
  recorded because the round-28 validator's own receipt preserves it. Whether
  anything is to be repaired or recorded is the parent's call.
- **§3 is a reported connector property, not a defect claim.** The family
  convention is documented in the tool's own docstring and shared with
  `typed-pipeline-gate.py`. It is reported because it silently pollutes tamper
  controls, which this round's D claim requires.
- **§4.1's "41 rows still do not reach the packet" counts component blocks by
  declaration**, using the assembler's own rule. Some of those rows are
  *deliberately* per-file metadata (`form_slots_note`, `rank_rules_note`,
  `open_questions`, `calibration`) and are correctly skipped; `signs` (20) and
  `orthography_rules` (7) are **not** metadata, and they are the substance of
  the residual.
- **§4.2 is a re-confirmation, not a new finding.** RL-1 was filed in round 27;
  this fragment measures it on the amended bytes and adds the family-path
  control. The claim's `after_required` asks for the replay leg to land; it has
  not, on the surfaces this seat watches.
- **No round validator was executed by this seat** — not the round-28 runner, not
  any historical one. §7.1 *reads* `reports/round-28/validation.json` and
  re-measures the specific facts its failures name; that is a reading of a filed
  receipt plus independent checks, not a re-run, and it does not overturn the
  receipt's own verdict.
- **The `replay-frozen` TMPDIR trap (§5.6) is reported, not repaired**: the fix
  is a source edit outside this seat's write scope and would invalidate a pinned
  tool digest (`tools/replay-frozen.py` at `a2fb5c98…`).
- No filed rounds 8–27 byte was written **by this seat**; no Git mutation was
  performed; no commit, no push. The only lane write is this fragment, plus
  gitignored scratch under `.scratch/x55/` (`A/`, `B/`, `C/`, `fam/`,
  `replay/` — copies used for the tamper and family controls, and the one
  discarded first probe). `export TMPDIR=$PWD/.scratch` preceded every
  scratch-writing command.
