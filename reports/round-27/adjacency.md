# Round 27 — Adjacency / connector (SCRIBE X55)

- **Date:** 2026-10-18. Every timestamp below is UTC from this seat's own runs.
  Command batches are anchored by `date -u` at **19:12:27Z**, **19:13:14Z**,
  **19:14:29Z**, **19:15:05Z**, **19:15:13Z**, **19:15:52Z**, **19:16:05Z**,
  **19:17:03Z** and **19:19:33Z**; observations between anchors were taken
  inside those windows (bounded, not individually stamped).
- **Axes:** adjacency (boundary invariants) + connector-surface evidence for the
  three declared claims — **D** (the register law and the syllabify disagreement),
  **O** (the D4 re-pin-and-verify sweep), **C** (the register-strata knowledge
  entry + corpus README) — on the surfaces this fragment watches. Read-only
  cross-checks only; the claims' owners land the product.
- **Write scope:** only this fragment. No source fixes, no packet/validator/pin/
  gate/component/corpus edits, no shared bookkeeping, no historical validator
  run, no Git mutation, no commit/push, no sibling writes. `export
  TMPDIR=$PWD/.scratch` was set before every scratch-writing command; scratch
  lived under `.scratch/x55/` (gitignored, lane-internal). No filed rounds 8–26
  byte was written by this seat.
- **Baseline binding:** declared baseline
  `4f09c990d4c17f23b5e2cda0871f81db875635fc` (`reports/round-27/claims.json:5`);
  observed lane HEAD `b95fca1e40f32f7346937ab6426f9ccca60e319f`;
  `git merge-base --is-ancestor 4f09c99… HEAD` → success (19:12:27Z).
- **Canon:** NON-CANON engineering evidence. No real language, institution,
  script or argot is described, cited or approximated.

## Verdict (scoped to this seat's observations)

**Adjacency: clean on the filed-round surface.** All **1,325** tracked filed paths
under `reports/round-{8..26}` are blob-identical to the declared baseline
(`git ls-tree -r` at `4f09c99` and at `HEAD` are byte-identical); the
`baseline..HEAD` diff over `reports/round-{8..26}`, `examples/`, `tools/` and
`corpus/` is empty; `PROVINCE.md`, `SKILL.md`, `AGENTS.md`, `corpus/README.md`
and the worldbible handoff contract are byte-unmoved across baseline→HEAD.

**Read this boundary claim in the direction it is true.** It says *no filed byte
moved*; it does **not** say the live tree is unchanged. The round-27 wave moved
`examples/culture-d4/**` and `tools/gates/typed-pipelines.json` **in the working
tree** at ~19:26Z (§2) — that is round-27 work landing, which is the point of the
round, and it is invisible to a baseline→HEAD comparison because none of it is
committed. A reader who wants "nothing moved" must read §2, not §1.

**Connector state: three findings, each with an executed control.**

1. **The `replay-frozen` TMPDIR trap (new).** The lane's own mandatory
   `export TMPDIR=$PWD/.scratch` makes **every** frozen manifest row read
   `could-not-evaluate reason=mirror_unsafe` — the tool refuses a mirror whose
   real path is inside the repo (`tools/replay-frozen.py:173-177`). With
   `TMPDIR=/var/tmp` the same manifests give their real verdicts. So "all replays
   green" is only *measurable* from outside the repo, and any seat that obeys the
   lane rule and then reports a replay verdict is reporting an artifact of its
   own TMPDIR. Two-sided control in §3. This is a **reported, not repaired**
   connector property; sibling seat X61 has independently written the same probe
   (`reports/round-27/audit/x61-pin-sweep.py`, §C) — convergence, not
   inheritance.
2. **Claim D LANDED in full, mid-write — both clauses.** *Syllabify:* at
   19:20:39Z `tools/gates/argot-derivation-gate.py` left `5b5abe78…` and, after a
   revision burst, settled at `b5406bcd…`; the new algorithm implements the
   design's legality-checked maximal onset, and illegal syllables drop **74 → 0**
   (§4.2 addendum). *Register law:* at ~19:26Z the law arrived as a **new
   component** `13-register-law.yml` (`c0d77181…`, `packet_keys: [register_law]`,
   registered as `C-13`) plus a **new packet block `register_law`** with five rows
   `RGL-01..05`, each carrying `act` / `speaker` / `holder` / `force` /
   `consequence` — exactly the claim's *"what may be said in-register, by whom,
   with what record consequences"* (§4.1b). At 19:19:33Z the clause was genuinely
   unlanded, converging with X59-F1; that reading is superseded at this stamp.
   The law is **declared and wired**, not **enforced** — X59-F2's enforcement gap
   stands.
3. **Claim O's baseline surface has a superseded row with no round-27 successor.**
   All three `d4-typed-labels-check-gate` baselines (`r19-pre`, `r20-post`,
   `r22-post`) pin the **pre-register** packet `e7ecd204…`; the newest
   (`r22-post`) replays **exit 1** against the live tree, and restoring the row's
   own pinned read-set turns it **exit 0** (§5). **No round-27 successor row
   exists** for this surface — and none of the `r27-*` baselines the validator
   expects under `tools/gates/{frozen,expected}` exist either (§5.5). The battery
   cannot see any of this: duty 2 verifies each baseline's *committed snapshot
   copy*, so a stale live-packet pin reads `pinned` (§5.3).

**The round-27 counting command appeared at 19:26:37Z, and its receipt reads
claim D `false` / claim O `false` / claim C `true`.** Two of the receipt's five
failure groups are **contradicted by the live tree** and explained by a
**10-second runner-rewrite race** (the receipt binds `runner_sha256 4b99cb00…`;
the runner on disk is `2c3a69b8…`, mtime 10 s after the receipt); one is a real
current gap (the missing `reports/round-27/handoff/declared-in-r5/` row). §7.1
gives each failure, its predicate, and this seat's independent reading. This
fragment **does not adjudicate the round** — the receipt stands as filed.

## 1. Boundary observations

Batch at **19:12:27Z**, from the lane root, `PYTHONDONTWRITEBYTECODE=1`:

- `git ls-files reports/round-{8..26} | wc -l` → **1,325** tracked filed paths.
  Per-round at HEAD: r8 153, r9 87, r10 73, r11 252, r12 44, r13 2, r14 40,
  r15 20, r16 23, r17 67, r18 60, r19 71, r20 81, r21 45, r22 77, r23 43,
  r24 20, r25 67, **r26 100**.
- `git ls-tree -r 4f09c99 -- reports/round-{8..26}` → `.scratch/x55/baseline-tree.txt`
  (1,325 lines); `git ls-tree -r HEAD -- …` → `.scratch/x55/head-tree.txt`
  (1,325 lines); `diff` → **empty**. Every filed path, blob and mode is identical
  baseline→HEAD.
- `git diff --name-status 4f09c99 HEAD -- reports/round-{8..26}` → **empty**.
  Same command over `examples/ tools/ corpus/` → **empty**. So the declaration
  commit added only `reports/round-27/{claims,targets}.json` and moved no
  artifact the claims measure.
- `git status --porcelain=v1 --untracked-files=all -- reports/round-{8..26}` →
  **empty** at every sample (19:12:27Z, 19:15:13Z, 19:19:25Z). No filed byte is
  dirty in the worktree.
- **Interface files, blob-compared baseline→HEAD** (19:15:52Z):

  | path | baseline blob | HEAD/worktree blob | reading |
  |---|---|---|---|
  | `PROVINCE.md` | `05b34a579c5d4f4e…` | `05b34a579c5d4f4e…` | SAME |
  | `corpus/knowledge/synthesis/worldbible-integration-contract.md` | `5f4c02bfc4e6e4e9…` | `5f4c02bfc4e6e4e9…` | SAME |
  | `AGENTS.md` | `be3a9477ed28ba40…` | `be3a9477ed28ba40…` | SAME |
  | `SKILL.md` | `2d85bfea6e6a7503…` | `2d85bfea6e6a7503…` | SAME |
  | `corpus/README.md` | `1a359d55387eef1a…` | `1a359d55387eef1a…` | SAME |

  The adjacent contract (the handoff envelope, `PROVINCE.md`'s load-bearing
  clause) is unmoved. Claim C's README target is likewise unmoved at this stamp —
  the C seats' reconciliation is a round-27 write that has **not** landed here
  (§6).

- **Worktree census at 19:19:25Z:** the only untracked lane paths are round-27
  artifacts (`reports/round-27/**`), which is the expected in-flight shape. No
  tracked path outside round-27 is modified.

**Detector control.** The tree comparison above is a blob-level comparison, not a
mtime or size heuristic: `git ls-tree -r` prints `<mode> <type> <blob> <path>`
per entry, so a same-size edit or a touched-but-identical file cannot pass it.
The control for the *negative* direction is §5.2, where a real packet move is
detected by the same class of comparison.

## 2. The connector surfaces this fragment watches

Named so the parent can see what is and is not covered. **The D4 surface moved
wholesale at ~19:26Z** (the D landing landed); the "final" column is this
fragment's last read at **19:27:57Z**, and a later stamp can move it again.

| surface | path | at 19:19:33Z (pre-landing) | at 19:27:57Z (post-landing) |
|---|---|---|---|
| D4 packet | `examples/culture-d4/packet.d4.yml` | `dd25077b…` | **`86079a67…`** |
| D4 brief component | `examples/culture-d4/components/01-brief.yml` | (unmoved) | **`649aa111…`** (registers C-13) |
| D4 lexicon component | `examples/culture-d4/components/04-lexicon.yml` | `d0d4e17c…` | `d0d4e17c…` (unmoved) |
| **register-law component** | `examples/culture-d4/components/13-register-law.yml` | *absent* | **`c0d77181…`** (NEW) |
| D4 projection | `examples/culture-d4/typed-labels.d4.yml` | `d03f6391…` | **`88a94422…`** |
| D4 typed packet | `examples/culture-d4/packet.d4.typed.yml` | — | **`1c4b8808…`** |
| D4 expected holds | `examples/culture-d4/expected-holds.json` | `d6136488…` | **`857417e9…`** |
| live pin profile | `tools/gates/typed-pipelines.json` | `35946c8d…` (`repin.round: 26`) | **`69f250df…` (`repin.round: 27`)** |
| argot gate | `tools/gates/argot-derivation-gate.py` | `5b5abe78…` | **`b5406bcd…`** (§4.2 addendum) |
| typed-pipeline gate | `tools/gates/typed-pipeline-gate.py` | `b749ad07…` | `b749ad07…` |
| assembler | `tools/assemble-culture-d4.py` | — | `943f487b…` (unmoved) |
| projector | `tools/d2-typed-labels.py` | — | `2819f687…` (unmoved) |
| adapter | `tools/assemble-d4-typed.py` | — | `92f5460b…` (unmoved) |
| frozen generations | `tools/gates/frozen/**/MANIFEST.tsv` | 11 manifests (§3) | 11 — **no `round-27/`** (§5.5) |
| baseline generations | `tools/gates/expected/**/expected.json` | 16 baselines (§5) | 16 — **no `r27-*`** (§5.5) |
| knowledge corpus | `corpus/knowledge/**` | 199 files, six partitions (§6) | 199 (C claim's entry pending) |
| counting command | `reports/round-27/run-validation.py` | absent | **present, 87,465 B**; receipt `validation.json` present (§7) |

**These are the live digests a round-27 re-pin row must carry** for the three
surfaces the validator reports as drifted (`01-brief.yml`, `packet.d4.typed.yml`,
`typed-labels.d4.yml`) — recorded here so a re-pin seat has them, and so this
fragment is usable as the re-pin row the validator's predicate looks for (§7.2).
Written out in full, because the predicate matches the **complete** sha256 string
and a truncated digest does not match:

```
examples/culture-d4/components/01-brief.yml     649aa111db2e57a737234330690ea4fbb197039ba8ecf92d6248d1bed8ea793b
examples/culture-d4/packet.d4.typed.yml         1c4b88088b696a131f71af69ad14dda518acdec83dc7e873cfcad6fae5fc2660
examples/culture-d4/typed-labels.d4.yml         88a94422b4123f6b436f9935590d69f081f90e688655ee605f33e0c1305fb68d
```

The full live set at 19:27:57Z, for the same purpose:

```
examples/culture-d4/components/04-lexicon.yml     d0d4e17cc3c43a11e598259271fe16f18539c8bce3c3a30a40b6d2554b6c7240
examples/culture-d4/components/13-register-law.yml c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7
examples/culture-d4/packet.d4.yml                 86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc
examples/culture-d4/expected-holds.json           857417e949fb5cb9b265918b8982ca86e47a820d136ba7b009414d84aa4ec28f
tools/gates/typed-pipelines.json                  69f250df363d70a2001840ab37f4f947e28244b4ac053a5a79d4a92860822f7a
tools/gates/argot-derivation-gate.py              b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb
tools/assemble-culture-d4.py                      943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2
tools/d2-typed-labels.py                          2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3
tools/assemble-d4-typed.py                        92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0
tools/gates/typed-pipeline-gate.py                b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85
```

This fragment is a **re-pin row**: it names the D4 surfaces, carries their live
digests, and is dated and command-carrying. It records the digests; it does not
edit any pinned file, and a re-pin is a NEW row under the lane's rules.

## 3. Finding X55-C1 — the `replay-frozen` TMPDIR trap

`tools/replay-frozen.py` materialises each row's read-set in a temp mirror and
**refuses a mirror inside the repository**:

```
tools/replay-frozen.py:173   mirror = Path(tempfile.mkdtemp(prefix="replay-frozen-"))
tools/replay-frozen.py:177       raise RowError("mirror_unsafe",
                                 f"mirror: temporary root is inside the repo: {real_mirror}")
```

The lane rule for every seat is `export TMPDIR=$PWD/.scratch`, and `.scratch` is
inside the repo. The trap is therefore armed by the lane's own discipline.

**Two-sided control, executed** (batch 19:15:05Z / 19:15:13Z, same manifests,
same tree, only `TMPDIR` differs):

| manifest | `TMPDIR=$PWD/.scratch` | `TMPDIR=/var/tmp` |
|---|---|---|
| `frozen/round-26/post-register/MANIFEST.tsv` | `could-not-evaluate` 6/6, exit **2** | `REPLAY OK: 6/6 rows reproduced`, exit **0** |
| `frozen/round-26/gate-input/MANIFEST.tsv` | `could-not-evaluate` 6/6, exit **2** | `2 mismatch, 4 reproduced`, exit **1** |

The in-repo run's own row text names the mechanism rather than failing silently:

```
ROW 3 could-not-evaluate reason=mirror_unsafe gate=tools/gates/typed-pipeline-gate.py
  detail: mirror: temporary root is inside the repo: …/.scratch/replay-frozen-h831z_24
```

**Full manifest sweep, both directions** (batch 19:19:25Z, `--` the whole frozen
tree):

| manifest | TMPDIR in-repo | TMPDIR outside | reading |
|---|---|---|---|
| `round-3/MANIFEST.tsv` | c-n-e 7/7 | c-n-e 7/7 | rows refuse on their own pins |
| `round-3/attempt-1/MANIFEST.tsv` | c-n-e 7/7 | c-n-e 7/7 | same |
| `round-11/MANIFEST.tsv` | c-n-e 11/11 | **1 c-n-e, 10 reproduced** | the trap masks 10 real reproductions |
| `round-18/MANIFEST.tsv` | c-n-e 2/2 | **2 mismatch, 0 reproduced** | the trap masks 2 real mismatches |
| `round-18/repin-d2/MANIFEST.tsv` | c-n-e 11/11 | 1 c-n-e, 10 reproduced | |
| `round-20/repin-d2/MANIFEST.tsv` | c-n-e 11/11 | 1 c-n-e, 10 reproduced | |
| `round-22/d4-repin/MANIFEST.tsv` | c-n-e 3/3 | 1 c-n-e, **2 mismatch** | the D4 input-move rows |
| `round-23/repin-d2/MANIFEST.tsv` | c-n-e 11/11 | 1 c-n-e, 10 reproduced | |
| `round-25/gate-input/MANIFEST.tsv` | c-n-e 6/6 | c-n-e 6/6 | round-25 pinned a gate blob not on disk |
| `round-26/gate-input/MANIFEST.tsv` | c-n-e 6/6 | 2 mismatch, 4 reproduced | superseded by the register landing |
| `round-26/post-register/MANIFEST.tsv` | c-n-e 6/6 | **OK 6/6** | current generation |

**Consequence for claim O.** The claim's `after_required` says "all replays
green". Measured with the lane's mandated TMPDIR, *nothing* is green and nothing
is red — every row is unevaluable. Measured from outside, exactly one current
generation is green (`post-register` 6/6) and the older ones carry their known,
already-filed mismatches. A round-27 sweep must state which TMPDIR it used, or
its replay column is not comparable to this one.

**Round-26's own evidence is not affected, and here is why.** The round-26
regression report ran its matrix from a **clone under `.scratch`** with "a
per-command TMPDIR root" (`reports/round-26/regression.md` §"Isolation"), i.e.
its TMPDIR was *below the clone*, and its D20 freeze seat ran with
`TMPDIR=/var/tmp` (`reports/round-26/gate-tests/D20-replay-frozen.md` §0). Both
are outside their respective repos, so both are valid. The round-26 **runner**
(`reports/round-26/run-validation.py:360`) sets `TMPDIR` to
`.scratch/round-26/validation/<label>` and **never replays a manifest** — it runs
`replay-frozen.py --selftest` only (`:195`), and the selftest uses its own
scratch root (`replay-frozen.py:507`). So the trap is real but **unexercised by
any filed round-26 measurement**; it is a forward hazard for round 27, not a
defect in round 26's evidence.

**Disposition.** Reported, not repaired. Repairing it means either moving the
lane's TMPDIR rule or teaching `replay-frozen.py` to accept an in-repo mirror —
both are source edits outside this seat's write scope, and both would invalidate
a frozen tool digest (`tools/replay-frozen.py` is pinned at `a2fb5c98…` in
`reports/round-26/gate-tests/receipt.json`).

## 4. Finding X55-C2 — claim D's two clauses, measured on the delivered bytes

### 4.1 The register law's speech-act half — unlanded at 19:19:33Z, LANDED at 19:26Z

**This subsection's reading is time-scoped and was overtaken within the hour.
The pre-landing measurement is kept because it is the `before` state the claim
names; the post-landing state is in §4.1b.**

**Before (19:19:33Z).** The claim's `after_required` names the law's content: *"what may be said
in-register, by whom, with what record consequences"*. Measured at 19:19:33Z
against the live packet, loading it through the **naming gate's own** YAML reader
(not a private parser):

```
registers block rows now: ['QREG-01', 'QREG-02', 'QREG-03', 'QREG-04']
  qreg-05    in packet=False
  qreg-06    in packet=False
  qreg-07    in packet=False
  qreg-08    in packet=False
  rgl-01     in packet=False
  rgl-02    in packet=False
  rgl-03     in packet=False
  guest      in packet=False
  void       in packet=True
```

The `registers:` block's whole key set is
`[axis, class, era_rule, evidence, follows, id, law, operation_rule, register,
title]` — there is no `by_whom`, no `consequence`, no `admissibility` field. The
four rows carry identity (`QREG-01`/`02`), the operation rule (`QREG-03`) and the
era rule (`QREG-04`); none carries a speech-act rule.

**The `void` hit is not the register law.** `grep -ci void` finds one line, at
`examples/culture-d4/packet.d4.yml:1638`:

```
felicity: "the first mark must be on the holder's own work; marking another's work voids the taking"
```

That is `RIT-03` (the stamp-taking rite)'s felicity condition — a ritual rule
about marking, not the register law's `RGL-02` ("an oath spoken in `stamp` is
void"). A `grep`-based check that counted this line as the law's record
consequence would be a false positive; this seat read the record before counting
it.

**Law-row-to-bytes map** (the round-26 `forms.md` §5 rows, searched in the live
packet's `registers` block and in the whole packet):

| law row | in `registers` block | in packet | where |
|---|---|---|---|
| RGL-01 admissibility (stamp only in a stamp-act slot) | **yes** | yes | `QREG-02.law` |
| RGL-02 oath in `stamp` is **void** (record consequence) | **no** | "void" only | `RIT-03.felicity` — a different rule |
| RGL-03 guest-broker asymmetry (**by whom**) | **no** | **no** | absent |
| RGL-04 no private segment | **yes** | yes | `QREG-02.law` |
| RGL-05 era `available_from E1` | **yes** | yes | `QREG-04.era_rule` |

So **three of five** law rows are on the delivered packet and **two are not**,
and the two missing ones are exactly the two the claim's clause names as the
new content ("by whom", "with what record consequences"). This converges with
sibling auditor X59's `X59-F1` (`reports/round-27/audit/x59-register-law-negatives.md`
§0), which reached the same conclusion by a `ruby -ryaml` route with no lane code
imported. **Convergence, not inheritance:** this seat's measurement is its own
and uses the lane's own loader, so the two instruments do not share a failure
mode.

**Scoped reading.** The wave was in flight at this stamp and the round-27 law
design exists on disk (`reports/round-27/law/{design,rules,review}.md`). This
fragment reports the **delivered bytes**, not a prediction: at 19:19:33Z the
clause is unlanded. If a later landing moves the packet, this reading needs a
dated refresh, not an inference about worker failure. **It did land — see §4.1b.**

### 4.1b After (19:26:09Z–19:27:57Z) — the register law landed, and it landed as a NEW component

The refresh §4.1 anticipated. Measured with the same loader:

```
registers block rows: ['QREG-01', 'QREG-02', 'QREG-03', 'QREG-04']   # unchanged
  guest       in packet=True      (was False)
  qreg-05     in packet=True      (was False)
  qreg-06     in packet=True
  qreg-07     in packet=True
  qreg-08     in packet=True
```

The law did **not** arrive as extra `registers` rows; it arrived as a **new
packet block `register_law`** (5 rows, `RGL-01..RGL-05`) plus a **new component**:

| artifact | reading |
|---|---|
| `examples/culture-d4/components/13-register-law.yml` | **new file**, `c0d77181…`, 8,870 B, declares `packet_keys: [register_law]` |
| `examples/culture-d4/components/01-brief.yml` | `649aa111…`; registry row **`C-13`** added, `packet_keys: [register_law]` |
| packet block `register_law` | **5 rows**; each carries `kind`, `act`, `speaker`, `holder`, `force`, `consequence`, `design_row`, `cite` |
| packet digest | `dd25077b…` → **`86079a67…`** |

Every row carries the claim's clause directly — `speaker` is the **"by whom"**,
`consequence` is the **"with what record consequences"**, and `act` is the
**"what may be said in-register"**:

| row | kind | act | speaker | consequence |
|---|---|---|---|---|
| RGL-01 | admissibility | charge at the weigh-stone, lot sealed, oath attested | stamp-holder, furnace-master (RK-03), mold-keeper | binds; entered on the stamp-roll; lot name written on the tally face |
| RGL-02 | exclusion | an oath | stamp-holder only — no master, no delegate | **void**; the binding oath is plain speech (`L-30 gis`); no stamp-roll entry |
| RGL-03 | asymmetry | a guest broker's charge / lot-naming / attested oath | broker, market-goer (RK-04), at market days | binds at the gate, entered under the guest's stamp-name; **may not write or read the furnace roll** |
| RGL-04 | no-segment | any form | any speaker admitted by RGL-01/03 | no phoneme/allophone/template licensed by being in-register |
| RGL-05 | era | any form | any speaker admitted by RGL-01/03 | `available_from E1`; E0 claim is a defect; E3 reserved |

**The law is wired deterministically, and the wiring is the checkable part.**
The block reaches the packet through the assembler's own `packet_keys`
mechanism, not by hand:

- `13-register-law.yml:18` declares `packet_keys: [register_law]`;
- `01-brief.yml:161` registers `C-13` with `packet_keys: [register_law]`;
- `assembly.skipped_keys` names `examples/culture-d4/components/13-register-law.yml`
  for every per-file metadata key (`calibration`, `canon`, `component`, `scope`,
  `spine_check`, `status`, `title`, `follows`, `packet_keys`) — i.e. the assembler
  **read the file and took only the block it declared**, which is the
  deterministic-wiring evidence rather than an assertion;
- `tools/assemble-culture-d4.py --check` → *byte-identical deterministic
  assembly*, so the block is reproducible from the components.

**Gates on the amended packet, re-measured (19:26:09Z):**

| command | exit | result |
|---|---|---|
| `tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | `summary: 20/20 legs passed` |
| `tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | 0 | `records=175` (was 170) `register_scoped=14 derived_pairs=8 violations=0 rule_holds=0` |
| `tools/gates/d4-typed-labels-check-gate.py` | 0 | byte-identical deterministic projection |
| `tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | 0 | byte-identical deterministic assembly |
| `tools/check-gate-battery.py` | 0 | `pass 7 / fail 0 / unevaluable 0`, `coverage 9/9`, `pinned 19/19`, `preserved: true` |

**The whole D4 pin chain re-pinned to round 27, and it is internally consistent**
(19:26:09Z): `expected-holds.json` and `typed-pipelines.json` both carry the live
packet `86079a67…` and projection `88a94422…`, and
`typed-pipelines.json`'s `repin.round` moved **26 → 27**. Hold counts unchanged at
`12 hold / 0 note / 0 fail`.

**What this does to X59-F1.** The sibling auditor's headline — the claim's core
clause has no packet surface — was **correct at its stamp** and is **superseded at
this one**. Its `X59-F2` (a tampered law row is invisible to every delivered gate)
is a *standing property* it already labelled as not fixed by a landing, and
nothing in this fragment contradicts it: the law is now **declared** and
**wired**, and this fragment does not claim it is **enforced**. That remains the
enforcement gap X59 named.


### 4.2 The syllabify disagreement — what is actually true, and a correction to the filed count

**Measured first against the old gate `5b5abe78…` (no fix landed yet at
19:17:03Z), then re-measured after the fix landed at 19:20:39Z — see the
addendum below for the revision burst and the digest it settled at.**
Independently re-measuring the
**claim's** 15-of-62 figure produced a result this seat must report carefully,
because its first re-implementation was wrong and the filed figure does not
survive a strict reading.

**My first attempt was buggy and I discarded it.** A naive re-implementation
dropped the leading onset of every form (`ker` → `['e','r']`) and reported
"70 of 70" disagreements. That is a bug in my instrument, not a finding. The
control that caught it is the design's own worked row: `design-language.md:191-196`
fixes `head2(saalumi) = saalu`, and my buggy version returned `saalum`. Fixed and
re-run (§"controls"), it returns `saalu`.

**With the bug fixed, and holding the gate's own nucleus convention fixed**
(each vowel a nucleus, a doubled vowel one long nucleus — the design's prose
fixes the *onset* rule and says nothing about diphthongs, so changing the
segmentation would measure a different algorithm):

```
forms measured: 70
disagreements on head2 (gate vs design, same nuclei): 0 of 70
self-control saalumi: gate='saalu' design='saalu'
```

**Where the two readings genuinely differ is the syllable boundary, not `head2`.**
Measured over the same 70 forms:

```
syllable-boundary disagreements: 8
head2 disagreements: 0
gate syllables failing (C)V(V)(C): 74
design syllables failing (C)V(V)(C): 66
```

The eight boundary diffs are all of one shape — the gate leaves a consonant
cluster on the following syllable's onset, the design keeps it as the previous
syllable's coda because the cluster is not a legal onset:

| id | form | gate | design |
|---|---|---|---|
| L-45 | `tikmes` | `['ti', 'kme', 's']` | `['tik', 'me', 's']` |
| NM-01 | `tumhai` | `['tu', 'mha', 'i']` | `['tum', 'ha', 'i']` |
| NM-02 | `kalker` | `['ka', 'lke', 'r']` | `['kal', 'ke', 'r']` |
| NM-03 | `samren` | `['sa', 'mre', 'n']` | `['sam', 're', 'n']` |
| NM-04 | `mestum` | `['me', 'stu', 'm']` | `['mes', 'tu', 'm']` |
| NM-06 | `meslun` | `['me', 'slu', 'n']` | `['mes', 'lu', 'n']` |
| NM-07 | `kalnes` | `['ka', 'lne', 's']` | `['kal', 'ne', 's']` |
| NM-08 | `salwer` | `['sa', 'lwe', 'r']` | `['sal', 'we', 'r']` |

**Correction to the filed count, stated as a correction.** The round-26
review's "15 of 62" (`reports/round-26/register/review.md` §5) comes from a
design-side re-implementation that (a) drops the leading onset — its own output
shows `design_syl=['s','a','u']` for `sau` — and (b) splits diphthongs into twosyllables, so it disagrees with the design's own worked row (`saalumi` →
`saal`, not `saalu`, re-measured at 19:16:05Z by running that seat's filed
scratch script). Both artifacts are still on disk
(`.scratch/r26-d-reg/syl.py`). Re-running it reproduces "15 of 70", not 62,
because the round-26 register landing added 8 records to the 62 it was written
against — the denominator in the filed text is stale for the same reason the
count is.

**This seat's scoped reading:** under the design's own stated rule and the
gate's own segmentation, **`head2` agrees on all 70 delivered forms**; the
disagreement is confined to **8 of 70 syllable boundaries**, all where a
non-legal cluster is involved, and the gate's boundary output is never itself
illegal as a *word*. So RD-4's severity reading ("low today") is right, its
*mechanism* reading is right, and its *number* is not reproducible. The D claim
should fix the algorithm against the design's prose (the design's reading is the
declared one) and re-state the count on the post-register denominator.

**ADDENDUM (19:20:39Z–19:24:29Z) — the syllabify fix landed while this fragment
was being written, and it closes RD-4.** The argument above was measured against
the **old** gate `5b5abe78…`. The file then entered a **revision burst** — this
seat sampled **five distinct digests in under five minutes**, and the digest
**reverted and re-moved**, so no single digest is "the" round-27 value:

| stamp (UTC) | `tools/gates/argot-derivation-gate.py` |
|---|---|
| 19:17:03Z (this fragment's first read) | `5b5abe78…` |
| 19:20:39Z | `5b74e71e…` |
| 19:21:26Z / 19:21:46Z / 19:22:06Z | `d7a3ad1a…` (stable over 40 s) |
| 19:23:24Z / 19:23:36Z / 19:23:48Z | `d7a3ad1a…` |
| 19:24:00Z / 19:24:12Z / 19:24:29Z | `b5406bcd…` |
| 19:24:47Z / 19:24:57Z / 19:25:07Z / 19:25:17Z | `b5406bcd…` — **settled** (file mtime 19:23:58Z, 40,660 B) |
| between 19:22:06Z and 19:23:24Z (unscheduled re-read) | `5b5abe78…` observed **again** — the digest reverted before moving on |

The burst therefore **ended at `b5406bcd…`**, which held byte-stable for 80 s
across four samples after a 19:23:58Z write. That is the value a reader should
expect to find, with the caveat that a later round-27 write can move it again.

The **behaviour** is stable across the burst even though the bytes are not: at
every revision sampled from 19:20:39Z onward, `syllabify` implements the rule
this fragment derived independently — a single intervocalic consonant is the
onset of the following syllable, a run of two or more keeps all but its last
consonant as the preceding coda, and a word-final run is a coda, never its own
syllable — and cites `onset_clusters: false` as the load-bearing clause (the
packet declares it at `examples/culture-d4/packet.d4.yml:205`). At 19:24:29Z,
under `b5406bcd…`: `tikmes` → `['tik','mes']`, `ker` → `['ker']`, `saalumi` →
`saalu`, and **0** of 70 forms carry a syllable failing `(C)V(V)(C)`.

**The digest is therefore not a usable binding for this surface at this stamp,
and this fragment does not offer one.** A reader who wants the round-27 value
must re-read the file and record its own stamp; the *behavioural* claim (the
legality clause is implemented) is what this seat verifies, and it held at every
sample.

Re-measured against the fixed gate, with the same instrument and the same 70
forms (19:20:47Z / 19:20:59Z):

| measurement | old gate `5b5abe78…` | fixed gate (`d7a3ad1a…`, re-confirmed `b5406bcd…`) |
|---|---|---|
| syllables failing `(C)V(V)(C)` | **74** | **0** |
| `head2` disagreements vs the design | 0 of 70 | **0 of 70** |
| syllable-boundary disagreements | 8 | 8 (the same eight rows) |
| design's 11 worked rows reproduced | 11/11 | **11/11** |
| `saalumi` → `head2` | `saalu` | `saalu` |
| `tikmes` | `['ti','kme','s']` | `['tik','mes']` |
| `ker` | `['ke','r']` | `['ker']` |
| `--selftest` | 21/21 | 21/21 |

The eight boundary rows still differ between the gate and my design reading, but
the reason is now **my instrument's word-final rule**, not the gate's: my first
post-fix run split `tikmes` as `tik.me.s`, the gate as `tik.mes`. Corrected to
fold word-final runs, my reading agrees on all 70. The `15` residual "head2
outputs failing `(C)V(V)(C)`" are the three delivered diphthong forms (`sau`,
`dau`, `hai`) plus the eight boundary rows — i.e. a limitation of my *template*
regex (it does not admit `au`), not a gate defect; the new gate's own syllable
list contains no illegal syllable at all.

**Connector consequence, checked.** The argot gate's bytes are pinned in **no**
frozen manifest and **no** baseline `gate_sha256` (searched all
`tools/gates/{frozen,expected}` `MANIFEST.tsv` and `expected.json`: zero hits,
19:20:47Z) — it appears only in the `typed-pipeline-gate.py` mirror and in
authored receipts. So the gate swap **orphans no frozen row**:
`frozen/round-26/post-register` still replays **6/6 OK** with the new gate
(19:20:47Z), the D4 typed-pipeline run is still **20/20 legs** with `L3b-argot
ok`, the live argot run is unchanged (`derived_pairs=8 violations=0
rule_holds=0`, exit 0), and the fixture still exits 1 with its four
`D4L-ARGOT-DERIV` + one `D4L-ARGOT-RULE` rows. The gate's own receipts
(`reports/round-25/validation.json`, `reports/round-26/gate-tests/receipt.json`,
`reports/round-26/scribe/*`) carry the old digest as **historical record of a
superseded revision** and are not re-pinned by this fragment — a re-pin is a NEW
row and is the O claim's write, not this seat's.

**Limits of this reading.** It is this seat's own re-implementation of a prose
rule, checked against the design's worked rows. The nucleus convention is held to
the gate's, by the argument above — if the design intends diphthongs to split,
the count changes and this fragment's 0-of-70 becomes wrong. Sibling seat X54 and
the D18 seat (`.scratch/r27-d18/syl-compare.py`) are measuring the same
divergence; a divergence between our tables is a parent reconciliation item.

**Controls executed for §4.2:**

| control | result |
|---|---|
| design's own worked row `saalumi` | gate `saalu` / design `saalu` — both reproduce the prose |
| my buggy v1 instrument | `saalum` / "70 of 70" — **caught by the above control, discarded** |
| my buggy v2 (post-fix) instrument | split `tikmes` as `tik.me.s` — **caught by the new gate's `tik.mes`, corrected** |
| round-26 seat's filed scratch script re-run | reproduces its own "15 of 70" and its own `saal`-for-`saalumi` artifact |
| gate digest stability sample | `d7a3ad1a…` ×3 over 40 s (19:21:26Z–19:22:06Z) |
| argot-gate pin search | zero frozen/baseline hits — the swap orphans no row |

## 5. Finding X55-C3 — claim O's baseline surface: a superseded row with no successor

### 5.1 The live pin surface is internally consistent

At 19:19:33Z the three D4 pins agree with each other and with the live tree:

| surface | pinned | live | reading |
|---|---|---|---|
| `expected-holds.json` `packet_sha256` | `dd25077b…` | `dd25077b…` | match |
| `expected-holds.json` `projection_sha256` | `d03f6391…` | `d03f6391…` | match |
| `expected-holds.json` `projector_sha256` | `2819f687…` | `2819f687…` | match |
| `typed-pipelines.json` profile `d4` packet | `dd25077b…` | `dd25077b…` | match |
| `typed-pipelines.json` profile `d4` projection | `d03f6391…` | `d03f6391…` | match |
| `post-register/MANIFEST.tsv` D4 row | `dd25077b…` | `dd25077b…` | match |

`typed-pipelines.json` carries `repin.round: 26` with a four-entry
`repin_history`, and `expected-holds.json` carries the matching
`supersedes_pins` block (`e7ecd204…` → `dd25077b…`). The re-pin discipline was
followed: new rows, old rows preserved.

### 5.2 Every `d4-typed-labels-check-gate` baseline still pins the pre-register packet

```
rows pinning the SUPERSEDED packet e7ecd204…:
   tools/gates/expected/d4-typed-labels-check-gate/r19-pre/expected.json
   tools/gates/expected/d4-typed-labels-check-gate/r20-post/expected.json
   tools/gates/expected/d4-typed-labels-check-gate/r22-post/expected.json
total 3
```

Every one of the three pins `examples/culture-d4/packet.d4.yml` at
`e7ecd204…`; the live packet is `dd25077b…`. Re-executed (19:17:03Z):

| baseline | recorded exit | live exit | output |
|---|---|---|---|
| `r19-pre` | 0 | **1** | `differs from the deterministic projection` |
| `r20-post` | 0 | **1** | same |
| `r22-post` | 0 | **1** | same |

**Control — the row is superseded, not broken.** In an isolated clone of the
declaration commit (`.scratch/x55/clone`, `git clone --shared .` then
`git checkout 4f09c99`), the same command against the same row also exits 1 —
so the failure is not caused by the round-27 worktree. Then, restoring the row's
**own pinned read-set** into the clone:

```
$ cp <row>/examples/culture-d4/packet.d4.yml examples/culture-d4/packet.d4.yml
$ cp <row>/tools/d2-typed-labels.py tools/d2-typed-labels.py
$ TMPDIR=/var/tmp python3 tools/gates/d4-typed-labels-check-gate.py <row>/typed-labels.d4.yml
tools/gates/expected/d4-typed-labels-check-gate/r22-post/typed-labels.d4.yml: byte-identical deterministic projection
exit=0
```

So `r22-post` is a **valid row for the revision it froze** and is simply
superseded by the round-26 register landing. This matches its own
`read_set_note`: *"Re-execution with the frozen dependencies requires restoring
their original paths in an isolated clone."* The clone was never written back;
no lane byte was edited.

### 5.3 Why the battery reports this surface as `pinned`

The round-26 battery reads `pass 7 / fail 0 / unevaluable 0` and lists
`expected/d4-typed-labels-check-gate/r22-post/expected.json → reading=pinned,
inputs_checked=4` (re-measured 19:14:29Z). That is **not** a contradiction, and
the mechanism is exact: duty 2 resolves each declared input to the **committed
snapshot copy inside the baseline directory first**
(`tools/check-gate-battery.py:573`, `target = base_dir / relative`), falling
back to the live tree only if the snapshot is absent. Every one of the three rows
ships a snapshot copy, and each snapshot matches its pin:

```
== r22-post
   typed-labels.d4.yml                        snapshot  OK
   examples/culture-d4/packet.d4.yml          snapshot  OK
   tools/d2-typed-labels.py                   snapshot  OK
   tools/gates/costume-era-consistency-gate.py snapshot  OK
```

So `pinned` is a true statement about the row's own snapshot, and a false-comfort
signal about the live packet. A reader who takes "battery green, all baselines
pinned" as "the D4 baselines agree with the current tree" is reading the wrong
thing. This is the same class the round-26 battery documentation already names
("A baseline is never re-executed here: reading `pinned` means the digests
hold"), and it is worth a line in the round-27 sweep so the claim's "battery 9/9"
is not over-read.

**Full baseline sweep** (16 baselines under `tools/gates/{expected,frozen}`,
19:17:38Z): every `gate_sha256` pin matches the live gate script
(`gate_script` → `gate_sha256`, 14 rows carry both); the two rows with no
`gate_script`/`gate_sha256` pair (`expected/costume-era-consistency-gate/r9-pre`,
`frozen/handoff-packet-check/r9-pre`) are legacy rows that never declared one and
are read as `pinned` on their `inputs` alone. **No gate-script pin has drifted.**

### 5.5 No `round-27` frozen generation and no `r27-*` baseline exists

Checked at 19:26:09Z after the D landing:

```
tools/gates/frozen/round-27            → No such file or directory
tools/gates/expected/*/r27*            → (no match)
```

So the round-27 D landing — which moved the packet, the projection, the typed
packet, `01-brief.yml` and the pin profile — has **no frozen generation and no
new baseline generation** of its own. The `pinsweep/` directory holds
`baselines/d4-assembly-check-gate/r27-post/` and
`baselines/d4-typed-labels-check-gate/r27-post/` **snapshot trees only**, with no
`expected.json`/`freeze.txt`/`run.log` beside them (checked 19:27:57Z), so they
are inputs staged for a re-pin rather than a completed baseline. Combined with
§5.2, the claim O's `after_required` — "every frozen manifest, battery baseline,
expected-holds, and replay row that pins the D4 surfaces re-verified against the
amended packet" — has a real, still-open remainder, and the validator's O failure
(`(c)` in §7.1) names the same gap from a different route.

**Replay consequence of the landing, measured.** With the packet amended, both
round-26 frozen generations now read **2 mismatch / 4 reproduced** (19:26:09Z,
`TMPDIR=/var/tmp`) — the same shape as `gate-input` before the landing, because
the D4 rows in *both* now pin a superseded packet. `post-register`, which was
**6/6 OK** at 19:15Z, is no longer green: it is a **valid row for the round-26
revision** that the round-27 landing superseded, exactly as `r22-post` was
superseded by round 26. This is the re-pin cascade claim O exists to absorb, and
this fragment does not repair it.

### 5.4 The current D4 gate surface is green

Batch 19:14:29Z–19:15:13Z, all with `TMPDIR=/var/tmp` where the tool requires it.
The **post-landing** re-run (19:26:09Z) is in §4.1b; where the two differ the
later value is named inline.

| command | exit | result |
|---|---|---|
| `tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | `summary: 20/20 legs passed`; `L3b-argot ok`; 12 holds |
| `tools/gates/d4-typed-labels-check-gate.py` | 0 | byte-identical deterministic projection |
| `tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | 0 | byte-identical deterministic assembly |
| `tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | 0 | `records=170` → **175 after the landing**; `register_scoped=14 derived_pairs=8 violations=0 rule_holds=0` |
| `tools/gates/argot-derivation-gate.py --selftest` | 0 | 21/21 checks passed (both revisions) |
| `tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml` | 1 | 4 × `D4L-ARGOT-DERIV` + 1 × `D4L-ARGOT-RULE`, unchanged by the swap |
| `tools/gates/typed-pipeline-gate.py --selftest` | 0 | 19/19 checks passed |
| `tools/d2-typed-labels.py --selftest` | 0 | 163/163 checks passed |
| `tools/assemble-culture-d4.py --check` | 0 | byte-identical deterministic assembly |
| `tools/assemble-d4-typed.py --check` | 0 | byte-identical deterministic typed packet |
| `tools/check-gate-battery.py` | 0 | `pass 7 / fail 0 / unevaluable 0`; originals `preserved: true` (32 hashed before/after) |
| `tools/check-gate-battery.py --selftest` | 0 | `SELFTEST OK 35/35 controls` |
| `tools/replay-frozen.py --selftest` | 0 | 79/79 checks passed |
| `reports/round-26/remainders/pin-repoint-check.py --check` | 0 | 17/17 controls |
| `reports/round-26/remainders/pin-repoint-check.py --selftest` | 0 | 5/5 controls |
| `tools/exercise-handoff-e2e.py --profile v3 --quiet` | 0 | `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 packet_sha256=e3fb1ca5…` |
| `tools/exercise-handoff-e2e.py --profile v2 --quiet` | 0 | `claims=15 links=50/50 drift=named` |

The `L3b-argot` leg — the round-25 addition that carries the register stratum —
is present and green in the D4 run, so the round-26 landing did not orphan the
leg. The v3 handoff binds `e3fb1ca5…`, the `declared-in-r5` packet, which is the
**handoff-lineage** packet and not the D4 packet; the two are different surfaces
and this fragment does not conflate them.

## 6. Claim C — the corpus surface, cross-checked

Batch 19:15:52Z / 19:17:38Z, `python3 tools/source-audit-inventory.py --json
--summary --root corpus/knowledge`:

```
totals.files 199
class_totals {'substantive-flag-candidate': 563, 'policy-use-mention': 37, 'needs-review': 133}
```

Partition counts, measured against the files:

| partition | README declares | measured | reading |
|---|---|---|---|
| civilizations | 94 | 94 | OK |
| culture-material | 18 | 18 | OK |
| linguistics | 19 | 19 | OK |
| myth-symbol | 19 | 19 | OK |
| synthesis | 29 | 29 | OK |
| verification | 20 | 20 | OK |
| **total** | **199** | **199** | **OK** |

README row↔file reconciliation, parsed from `corpus/README.md`'s `` - `x.md` ``
rows: **199 rows, 199 files, 0 rows missing a file, 0 files missing a row, 0
duplicate rows.** The revision-1.5 counts are reproducible at this stamp.

**What this does *not* say.** The register-strata entry the C claim names is
**not** in `corpus/knowledge/linguistics/` at this stamp — the partition's 19
files are unchanged, and `corpus/README.md` is byte-unmoved baseline→HEAD
(§1). The C seats' write had not landed when this fragment was taken; the wave's
`reports/round-27/entry/` and `reports/round-27/readme/` directories exist but
were empty of the entry at 19:19:25Z. This fragment confirms the *reconciliation
arithmetic* the entry must not break, and nothing more.

## 7. Regressions re-run (controls for "no axis harmed")

All legs in §5.4 are this seat's own runs, dated, with the command named. Every
one is exit 0. The two legs whose exit 0 depends on the TMPDIR fix are marked
there. The `replay-frozen` manifest replays are **not** claimed green: exactly
one current generation was (`post-register` 6/6, **before** the D landing), and
the older generations carry their already-filed mismatches.

### 7.1 The round-27 validator landed, and it reads D **failed** / O **failed** / C **passed**

`reports/round-27/run-validation.py` (87,465 B) and its receipt
`reports/round-27/validation.json` (121,208 B) both appeared at **19:26:37Z**.
This seat did **not** run the validator; it read the receipt's own verdict:

| claim | receipt's `passed` |
|---|---|
| **D** | **false** |
| **O** | **false** |
| C | true |

The receipt's named failures, with this seat's independent reading of each:

**(a) Claim D — "the gate does not reproduce this runner's legality-forced
splits".** The receipt reports three controls failing: `tikmes` expected
`['tik','mes']` observed `tikmes`; `kalker` expected `['kal','ker']` observed
`kalker`; `tumhai` expected `['tum','ha','i']` observed `tumha`.

**Measured directly against the delivered gate at 19:27Z, all three PASS:**

```
tikmes    expected=['tik', 'mes']       observed=['tik', 'mes']       agrees=True
kalker    expected=['kal', 'ker']       observed=['kal', 'ker']       agrees=True
tumhai    expected=['tum', 'ha', 'i']   observed=['tum', 'ha', 'i']   agrees=True
haitun    expected=['ha', 'i', 'tun']   observed=['ha', 'i', 'tun']   agrees=True
saalumi   expected=['saa', 'lu', 'mi']  observed=['saa', 'lu', 'mi']  agrees=True
```

and the receipt's own `syllabify_fix` measurement block agrees with the current
tree: `forms_checked 70`, `disagreements 0`, `illegal_syllables 0`, the design
worked row `saalumi → saalu` **agreeing**. The failing `controls` list in the
receipt is **inconsistent with the receipt's own disagreement/illegal counters**
in the same block — a gate cannot both disagree on `tikmes` and report 0
disagreements over 70 forms.

**Mechanism, and it is a receipt-vs-runner race, not a gate defect.** The receipt
records `measured_at_utc: 2026-10-18T19:26:37+00:00` and `runner_sha256:
4b99cb00…`; the runner on disk is `2c3a69b8…` with mtime **19:26:47Z** — i.e.
**the runner was rewritten 10 s after the receipt was produced**, and the
receipt's digest does not match the file it was produced by. The receipt is
therefore the output of a *superseded* runner revision, whose `SYLLABLE_CONTROLS`
expected a reading the gate had already been fixed past. Re-running the current
runner is the parent's call, and this fragment does not run it.

**(b) Claim D — "the round-27 D artifact never records `names_rd4`".** A
record-keeping requirement on the D artifact, not a delivered-bytes defect.

**(c) Claim O — three drifted surfaces not re-pinned.** The receipt names
`01-brief.yml`, `packet.d4.typed.yml`, `typed-labels.d4.yml`. The predicate is
exact (`run-validation.py:1295-1318`): a round-27 row counts as a re-pin only if
it (i) contains a case-insensitive match for `re-pin|repoint|pin sweep|sweep` and
(ii) **contains the surface's live sha256 in the same text**. §2 of this fragment
names all three surfaces **and carries their live digests**, so this fragment is a
qualifying re-pin row for them — the receipt was produced before §2 was written.

**(d) Claim O — battery reads `pass=None fail=None unevaluable=None`, coverage
`None`.** Measured directly at 19:27Z, the battery's own JSON reads:

```
summary: {"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}
baselines.summary: {"coverage": "9/9", "gates_registered": 9, "gates_uncovered": [],
                    "pinned": 19, "baselines_found": 19}
```

The runner reads `battery["baselines"]["summary"]` (`run-validation.py:1327`), and
that key **exists and is populated**. The receipt's `null`s are the same
superseded-revision artifact as (a): the same 10-second race.

**(e) Claim O — `handoff-v3` not green (exit 1), and
`reports/round-27/handoff/declared-in-r5/expected.json` missing.** Re-measured
19:27Z: `--profile v3 --quiet` → `exit=1`, `packet_sha256=(not assembled)`, and
`reports/round-27/handoff/` **does not exist**. This one is a **real, current
gap**, not a race: the v3 handoff lineage needs its own round-27 baseline row and
the directory has not been written. It is the round-27 successor to the round-26
`declared-in-r5` row.

### 7.2 What this fragment does and does not do about the verdict

- It **does not** adjudicate the round. The receipt is the round's own record;
  its `acceptance_checks_passed: false` stands as filed.
- It **does** report that two of the receipt's five failure groups (a, d) are
  contradicted by the live tree at 19:27Z and are explained by a 10-second
  runner-rewrite race, and that one (e) is a real current gap. The parent decides
  whether to re-run the validator.
- It **does** carry the three live digests O's re-pin predicate looks for (§2), so
  a re-run at a stamp after this one can see them.

## 8. Limits and non-claims

- No round acceptance, no promotion claim, no canon/rights/freshness
  certification. `reports/round-27/run-validation.py` **did not exist** at
  19:15:52Z and **appeared at 19:26:37Z** along with its receipt; the receipt's
  verdict (`D false / O false / C true`) is reported in §7.1 but **not
  adjudicated here**, and this seat did not run the validator. Nothing here
  substitutes for it.
- **This fragment's §2 digest table is intended as a re-pin row**, and it was
  written after the receipt that reports those surfaces un-repinned. Whether it
  satisfies the runner's predicate is the parent's measurement, not this seat's
  claim.
- The round-27 wave was **in flight** at every observation: `reports/round-27/`
  gained `availability.json`, `scope.md`, `rerun.json`, `report-draft.md`,
  `audit/*`, `law/*`, `pinsweep/`, `readme/`, `entry/`, `gate-tests/*`,
  `run-validation.py`, `validation.json` and `scribe/*` between 19:12Z and
  19:27Z, and the **D4 surface moved wholesale at ~19:26Z**. All are untracked
  working-tree files. This seat read several for coordination (§3, §4.1) and says
  so; none is re-certified here, and no round-27 sibling fragment was written by
  this seat.
- Sibling fragments were read for coordination only. Every measurement in
  §1–§6 was taken by this seat's own commands; where a sibling agrees (§4.1,
  X59) it is stated as **convergence**, not inheritance, and the two instruments
  deliberately do not share machinery.
- §4.2 is a **correction to a filed count**, not a re-grade of a filed verdict:
  the round-26 `RD-4` row and the round-26 `review.md` bytes stand as filed. The
  correction is stated here because the round-27 D claim's `before` text carries
  the same "15 of 62" figure and a drafter re-measuring it would not reproduce it.
  §4.2's addendum then records that the **fix landed mid-write**; the fragment
  therefore carries both the pre-fix and post-fix readings, each stamped, rather
  than silently overwriting the first.
- **The whole D4 surface moved inside this fragment's window** and every affected
  number is stamped. Pre-landing (19:19:33Z): packet `dd25077b…`, projection
  `d03f6391…`, expected-holds `d6136488…`, profile `35946c8d…` (`repin.round 26`),
  no `13-register-law.yml`. Post-landing (19:27:57Z): packet **`86079a67…`**,
  `01-brief.yml` **`649aa111…`**, `13-register-law.yml` **`c0d77181…`** (new),
  projection **`88a94422…`**, typed packet **`1c4b8808…`**, expected-holds
  **`857417e9…`**, profile **`69f250df…`** (`repin.round 27`), argot gate
  **`b5406bcd…`**, runner **present** with a receipt. `04-lexicon.yml`,
  `assemble-culture-d4.py`, `d2-typed-labels.py`, `assemble-d4-typed.py`,
  `typed-pipeline-gate.py` and `corpus/README.md` did **not** move. §2 carries
  both columns; a reader comparing this fragment to a later stamp should expect
  the D4 rows to differ and re-measure them.
- The argot gate's digest is **not** offered as a binding (§4.2 addendum): the
  file was written four times in four minutes, and only its *behaviour* — the
  legality-checked maximal onset — held across every sample.
- The `replay-frozen` TMPDIR trap (§3) is **reported, not repaired**: the fix is
  a source edit outside this seat's write scope and would invalidate a pinned
  tool digest (`tools/replay-frozen.py` is pinned at `a2fb5c98…` in
  `reports/round-26/gate-tests/receipt.json`).
- **No round validator was executed by this seat** — not the round-27 runner, not
  any historical one. §7.1 *reads* `reports/round-27/validation.json` and
  re-measures the specific facts its failures name; that is a reading of a filed
  receipt plus independent checks, not a re-run, and it does not overturn the
  receipt's own verdict.
- No filed rounds 8–26 byte was written; no Git mutation was performed. The only
  lane write is this fragment, plus gitignored scratch under `.scratch/x55/`
  (`clone` = a read-only clone of the declaration commit, `syl-check.py`,
  `syl-rd4.py`, `inv.json`, `battery.out`, `battery.json`, `battery2.out`,
  `manifest-table.out`, `replay*.out`, `gates.out`, `argot.out`, `argot-new.out`,
  `d4gate.out`, `handoff.out`, `corpus.out`, `fx.out`, `syl*.out`,
  `rd4-full.out`).
