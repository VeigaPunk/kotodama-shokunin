# R26-D13 — argot execution 1: the positive replay over the enriched register domain

- **Seat:** R26-D13 (D axis, argot execution 1 of 4), round 26, loop 3 build 2 of 4
  (`devin/deepseek-v4-1-flash-high`), claim **D** `register-stratum`
  (`reports/round-26/claims.json:14-23`).
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`
  (round-25 admit); worktree HEAD `1ad491a1a4b0aef9ebdc1861dfb8237727503825`.
  Every stamp below is UTC.
- **Write scope:** `reports/round-26/register/execution-{1..4}.md` only. Scratch
  under `.scratch/r26-d13/` (`export TMPDIR=$PWD/.scratch` preceded every
  scratch write). No tool, gate, fixture, component, packet, pin file or filed
  rounds 8–25 byte was written; no commit, no push. The enriched candidate this
  file replays is **scratch-only** (`.scratch/r26-d13/enriched-d4.yml`); it is
  not a delivered artifact and this seat did not land it.
- **Canon:** NON-CANON engineering evidence. No real language, institution,
  script or argot is described, cited or approximated.

## 1. What "the enriched D4" is, and why this seat built one

The assignment is to "run the round-25 argot leg over the enriched D4". At every
stamp this seat took, **the enriched D4 was not on disk** — the packet was
byte-still at `e7ecd204…`, `04-lexicon.yml` at `74c2561b…`, and
`grep -rl "D4L-REGISTER-UNRESOLVED" examples/ tools/` returned nothing. Twelve
D-register seats were live and polling for the same landing
(`.scratch/r26d/poll-register.sh`, `.scratch/x60/poll-register.py`, this seat's
own `.scratch/r26-d13/argot-watch.py`), and the register *design* landed as
`reports/round-26/register/{design,forms,rules,review}.md` while the *data* did
not.

An execution that only re-measured `derived_pairs=0` would be the round-25
finding restated. So this seat did what the leg needs: it **built the candidate
the design specifies, from the delivered bytes, by text transform only**, and
ran the leg over it. The builder is `.scratch/r26-d13/argot-enrich.py`
(sha256 `f53b914c…`); it reads the delivered packet, never re-serializes it, and
inserts exactly:

| insertion | source of the shape |
|---|---|
| the 8 `stamp` lexicon records `RF-01..RF-08` | `reports/round-26/register/forms.md` §1 (authoritative table) |
| the `LENGTHEN` `pattern`/`output` row in `morphology.derivation_rules` | `reports/round-26/register/rules.md` §3 |
| `derived_from`/`derivation`/`register` in `contract.record_fields.lexicon` | `reports/round-26/register/design.md` §6 owner table |
| a `registers:` block declaring `plain` (unmarked) and `stamp` (marked) | `reports/round-26/register/rules.md` §1 |

Command and result (2026-10-18T18:12:57Z):

```
$ export TMPDIR=$PWD/.scratch
$ python3 .scratch/r26-d13/argot-enrich.py \
      --packet examples/culture-d4/packet.d4.yml \
      --out    .scratch/r26-d13/enriched-d4.yml
wrote .scratch/r26-d13/enriched-d4.yml (86751 bytes, 2865 lines)
```

The candidate is the delivered 82,859-byte packet plus 3,892 bytes of inserted
text; every delivered byte is preserved (the transform is pure insertion, no
replacement), so the replay below is a replay of the delivered packet's own
records plus the register stratum.

## 2. The replay, and the one defect that changes its verdict

The gate replays a record's `derivation.op` against the packet's declared rule
ids **by exact string**. The design's own two files spell that token two ways:
`rules.md` §2's rule says `op = "lengthen"` (lowercase), while `rules.md` §3's
registry entry — the row a packet carries — is `id: "LENGTHEN"` (uppercase).
The two spellings are both "the design", and they do not agree.

The run labels A/B/C below are the same ones execution 4 §4 uses, so the two
files cannot be read against each other by mistake: **A** is the delivered
packet, **B** and **C** are the two spellings of the candidate.

**Run A — the delivered packet (for contrast; no register pair to replay):**

```
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: … records=156 register_scoped=6 derived_pairs=0 claimed_chains=8
          borrow_pairs=6 violations=0 rule_holds=0
exit 0
```

**Run B — the candidate as the design's §2 spells it (`op: lengthen`):**

```
$ python3 tools/gates/argot-derivation-gate.py .scratch/r26-d13/enriched-d4.yml
FINDING D4L-ARGOT-RULE: HOLD — register-scoped form RF-01 'tuum': declared
  derivation 'lengthen' is neither a declared argot operation (head2, reverse)
  nor a licensed packet rule (CX-01, CX-02, CX-03, LENGTHEN); replay is not possible
   … the same HOLD for RF-04 'nees', RF-05 'huum', RF-06 'mees', RF-07 'reek',
     RF-08 'saam' (6 rows) …
coverage: … records=166 register_scoped=14 derived_pairs=8 claimed_chains=8
          borrow_pairs=6 violations=0 rule_holds=6
exit 1
```

**Run C — the same candidate with the op re-spelled to the registry id
(`op: LENGTHEN`, one token changed, nothing else):**

```
$ python3 tools/gates/argot-derivation-gate.py .scratch/r26-d13/enriched-d4-upper.yml
coverage: … records=166 register_scoped=14 derived_pairs=8 claimed_chains=8
          borrow_pairs=6 violations=0 rule_holds=0
exit 0
```

**Both runs replay all 8 register derivations clean** (`derived_pairs=8`,
`violations=0`). The two `reverse` rows (`RF-02 kit ← tik`, `RF-03 lom ← mol`)
are computed by the gate's own operation table and pass in both runs. The 6
`lengthen` rows pass under Run C and are held under Run B, **not because any
arithmetic is wrong but because the declared operation name does not match the
declared rule id.**

This is the round-17 forecast's own rule working as designed — "a derivation is
replayable only when the replay names every input" (`SKILL.md:189-217`) — and it
is the **first live instance of `D4L-ARGOT-RULE` on a designed stratum rather
than a fixture**. It is a finding about the *design's cross-file consistency*,
and it is named here, not smoothed: a landing that copies `rules.md` §2's
lowercase op into the records while copying §3's uppercase id into the registry
lands 6 HOLDs and a red gate.

## 3. The replay row by row

`.scratch/r26-d13/argot-census.py` (sha256 `a3ef4ffd…`), which reads the packet
with the gate's own YAML subset loader so the census and the gate cannot
disagree about what the packet says, reports over the candidate:

| id | form | register | declared chain | op | base | replayed | verdict |
|---|---|---|---|---|---|---|---|
| RF-01 | `tuum` | `stamp` | `lengthen` | lengthen | `tum` | `tuum` | clean (Run C) / HOLD (Run B) |
| RF-02 | `kit` | `stamp` | `reverse` | reverse | `tik` | `kit` | **clean (both runs)** |
| RF-03 | `lom` | `stamp` | `reverse` | reverse | `mol` | `lom` | **clean (both runs)** |
| RF-04 | `nees` | `stamp` | `lengthen` | lengthen | `nes` | `nees` | clean (Run C) / HOLD (Run B) |
| RF-05 | `huum` | `stamp` | `lengthen` | lengthen | `hum` | `huum` | clean (Run C) / HOLD (Run B) |
| RF-06 | `mees` | `stamp` | `lengthen` | lengthen | `mes` | `mees` | clean (Run C) / HOLD (Run B) |
| RF-07 | `reek` | `stamp` | `lengthen` | lengthen | `rek` | `reek` | clean (Run C) / HOLD (Run B) |
| RF-08 | `saam` | `stamp` | `lengthen` | lengthen | `sam` | `saam` | clean (Run C) / HOLD (Run B) |

Every base resolves to a delivered record of the same packet (`tum` L-02,
`tik` L-42, `mol` L-38, `nes` L-16, `hum` L-09, `mes` L-43, `rek` L-37,
`sam` L-39) and no record is its own base, so the round-25 review's 6A.2/6A.3
false-green classes do not apply here.

The delivered base→form surface is untouched by the candidate and still replays:
`claimed_chains=8` (`NM-01..NM-08`, all `CX-01`) and `borrow_pairs=6` are
identical in the delivered run and both candidate runs.

## 4. Independent corroboration

- The lane's own acceptance runner (`reports/round-26/run-validation.py`) reads
  the same candidate differently. **It is under concurrent edit** — this seat
  observed its sha256 move `10fafb94…` (18:12Z) → `fe6671a2…` (18:15Z) — so the
  reading below binds to the `10fafb94…` bytes, not a live sha. In those bytes
  its `packet_rule_operations` (`:554-573`) **lowercases** every rule id and also
  indexes a rule by any of the tokens `lengthen`/`head2`/`reverse` found in its
  `kind`/`name`/`note`, and its `apply_operation` (`:574-592`) hard-codes
  `operation == "lengthen"`. Run over both candidates it reports
  `packet_rule_operations=['cx-01','cx-02','cx-03','lengthen']`, `pairs 8`,
  `half 0`, and **zero disagreements** — so on Run B it would score the stratum
  green where the argot gate emits 6 HOLDs. The two instruments disagree about
  the same bytes; both readings are recorded here and the disagreement is named
  as an operability item, not resolved by this seat. Whether the runner's
  case-folding is the right convention is itself the question the defect raises:
  the gate's exact match is what the replay discipline requires, and the
  runner's tolerance means a landing can pass acceptance while failing the leg.
- The register design's own probe receipts agree with Run C: the design records
  `probe-rule2.yml` → `derived_pairs=8 … violations=0 rule_holds=0`, exit 0
  (`reports/round-26/register/rules.md` §7). This seat reproduced that receipt
  independently over `.scratch/r26-d-reg/probe-rule2.yml` at 18:11Z (exit 0,
  `rule_holds=0`), and reproduced Run B's 6 HOLDs over `.scratch/r26-d-reg/probe.yml`.

## 5. Limits

- The replay grades **self-consistency**: a rule set that is wrong but
  self-consistent passes. It cannot tell whether `lengthen` is the operation the
  language would "really" use; that is a design question and the design labels
  it a design choice (`forms.md` CAL-1/CAL-2).
- The candidate is **this seat's reconstruction of the design**, not the
  delivered stratum. If the landing differs from `forms.md` §1, this file's rows
  bind to the design's table, not to the landing. The landing must be re-measured
  when it exists; that is the re-read event named in execution 4.
- Readings bind to the digests in execution 4 §5; a later edit to the packet,
  the gate or the design is a re-read event.
