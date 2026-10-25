# Round-71 wave-1 — Connector (sibling-overlap scan)

Seat: L1Kotodama71.ConnectorSiblings (leaf; no subagents). Report scope: sibling-overlap
map for the round-71 declared registers, plus the lore handoff-boundary check for claim C.
Read-only; no sibling file was touched.

## 0. Scope and method

- Swept: all 21 sibling `PROVINCE.md` files under `/home/vgpnk/Projects/shokunin/*-shokunin/`
  (audio, chousa, game-dev-2d, game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku,
  kotoba, kotodama[self], kumitate, lore, mado, mori, revenger, souji, tabi, tameshi,
  tsukuroi), plus every sibling `corpus/knowledge/` tree (grep-only, word-bounded where
  possible). No writes outside this report file.
- Re-verified claim-C base state on the frozen base (lane repo, unchanged): culture-material
  partition = 35 files; `find … -name '*danc*'` = 0; registry = 784 rows; knowledge corpus =
  242 `.md` files. All match the claim's declared before-state.

## 1. Dance / performance / movement register (claim C surface)

**No sibling owns it.** Sweep:
- Filename sweep across all sibling knowledge trees (danc/choreogr/movement/perform/ritual/
  festiv/calendar/receipt/selftest): no dance/movement-register file anywhere.
- Content grep, word-bounded (`\bdance|choreograph|movement culture|performing arts|performance art`)
  over all 20 non-kotodama sibling knowledge trees: **0 matches**.
- `PROVINCE.md` greps: no lane declares a dance/performance/movement register.

Adjacent-but-not-owners (named for the map):
- `game-dev-3d-shokunin` — owns *engine* movement/collision and animation mechanics
  (`PROVINCE.md:3-7,51-53`; executable fixtures), not a cultural register.
- `audio-shokunin` — "movement" appears only as SFX category (`PROVINCE.md:3`).
- `kake-shokunin` — `corpus/knowledge/field-performance-cwv.md` is Web performance (Core Web
  Vitals), not movement.

Internal nuance (own lane, not a sibling): kotodama's own `civilizations/` partition discusses
dance/performance as *source material* (Sun Dance, haka, Khon, Sebeïba …). None is a register
owner and none lives in the claim's swept scope (culture-material). The claim's gap is real.

**Claim-C sweep caveat (report, don't smooth):** the frozen before-command
`grep -rniE '^- topic:.*(danc|choreograph|movement culture)' corpus/knowledge/culture-material/*.md`
does **not** print nothing on today's base: it prints one line,
`culture-material/funerary-material-culture.md:4`, whose topic contains "avoidance terms"
(death-register avoidance terms) — the substring `danc` inside *avoidance*. Word-bounded
version prints 0. The substantive before-state (no dedicated filename, no true topic-line
owner) holds; the literal command does not. Frozen claims cannot be edited; flag for the
reviewer/verifier.

## 2. Ritual-calendar / festival cycle register

**Owner is kotodama itself, not a sibling:** `culture-material/calendar-festival-systems.md`
and `culture-material/era-periodization-models.md` (both lanes' PROVINCEs name kotodama as
owner; lore agrees). Claim C adds to the same culture-material partition but touches neither
file and no festival/calendar ground.

Sibling sweep: `ritual|festiv|calendrical` in sibling knowledge returns only *process* rituals
(mori admission ritual, chousa gate ritual, mado theme-set ritual, kotoba "round-ritual") — none
is a cultural festival cycle. `kasegi-shokunin/corpus/knowledge/repo-git-state.md:14` quotes an
external repo's commit message ("Halley Comet Festival") — an upstream observation, not an
owner. Lore's side of this register is *dates recorded on landed entities/events* (canon),
per lore `PROVINCE.md:28`.

## 3. Record-receipt discipline

Fleet-wide universal pattern; each lane owns receipts for its own surfaces. Named owners and
exact surfaces:
- `souji-shokunin` — domain is receipt-gated removal; `jj-colocation-receipts.md` (receipt
  roots; plain-git repo without `.jj` unchanged).
- `chousa-shokunin` — `receipt-binding-r38.md`, `receipt-expectation-digests-r40.md`,
  `receipt-verifier-subject-r39.md`.
- `tabi-shokunin` — `archive-receipt-r5/8/10.md` (receipts check content by quote).
- `tsukuroi-shokunin` — ".pkg.tar.zst receipt discipline" (`PROVINCE.md:9`);
  `aur-drift-receipt-r9.md`, `census-closeout-receipt-r10.md`.
- `mado-shokunin` — `gate-standing-use.md` "Receipt discipline (measured): receipts are never
  overwritten"; `snapshot-diff-receipt-r9.md`.
- `mori-shokunin` — offline receipt review; admission/receipt binding is parent-owned
  (`progressing-weak-r2.md`).
- `tameshi-shokunin` — receipt discipline inside the verification method (cite the pin that
  ran; read the block, not the last line).
- `kagi-shokunin` — offline receipt check (`tac-check`), ledger/release-clock receipts.
- `kake-shokunin` — `receipt-integrity.md`; `receipts.json` source rows.
- `kumitate-shokunin` — `receipt-identity-canonicalization.md`; wave/receipt lifecycle.
- `kaidoku-shokunin` — snapshot-specific receipt binding (r19 replay note).
- `kengaku-shokunin` — P1 receipts sha256-pinned; receipt logs indexed.

None of these owns or gates kotodama's telemetry-receipt instrument; claim Ca repairs
kotodama's **own** round-70 receipts (17/19 header). The shared fleet contract (fleet-root
`CORPUS.md`: "A count carries its command", append-only corrections; SOURCES-CONTRACT-v1) is
the common discipline both sides comply with; neither claim modifies it.

## 4. No-git selftest guards (claim D surface)

**No sibling owns a no-git guard.** Nearest documented surfaces:
- `kotoba-shokunin` — `corpus-integrity-round11.md`: *documents the same failure class*:
  `git archive HEAD | tar -x` + `git init` produces a repo with no history → spurious DRIFT
  ("would report a defect that does not exist"). Their resolution converts the archive into a
  repo; they do not detect `.git` absence. `harness-independent-round37.md`: blind tree from
  `git archive HEAD` ("no `.git/` → the history channel is closed").
- `kake-shokunin` — `accessibility-review-packet.md`: "A source change is could-not-evaluate,
  not a newly trusted standard"; exit-64 typed non-verdicts — same *could-not-evaluate*
  vocabulary as claim D's `COULD-NOT-EVALUATE`, triggered by source change, not git absence.
- `kama-shokunin` — `error-is-not-a-verdict.md`: a git timeout / broken git is marked fatal
  (no distinct cannot-evaluate code).
- `game-dev-3d-shokunin` — `engines.md` uses `git archive` to isolate runs (peer receipts);
  no `.git`-presence guard.
- `souji-shokunin` — handles repos *without `.jj`* (plain git, unchanged receipt paths), not
  repos without `.git`.

Claim D's move (new counter with a declared no-git path, exit 2) is unique in the fleet.

## 5. Lore handoff-contract boundary vs. claim C

- Contract: `kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md`
  (canonical copy in kotodama; lore reads it read-only; bilateral acknowledgment still pending —
  lore coverage row CM-g, unrelated to claim C).
- Boundary: kotodama proposes/traces systems; lore selects, records, verifies canon (§13;
  §3 ownership table; §6 canon standing is lore-only).
- Claim C writes only `corpus/knowledge/culture-material/dance-performance-movement-codes.md` +
  new SOURCES rows + README/lesson/scorecard/log appends — all inside kotodama's own repo. Its
  NOHARM diff is bounded to that repo. No byte touches lore's repo, the world bible, or the
  contract file. **Boundary untouched as a file/byte matter.**
- Content guardrail (not a write-risk): the entry must stay on codes/rules/terminology (the
  system side, cf. contract §3 "Symbol / costume" row: kotodama supplies sign rules and
  lexicon; lore records actual institutions/wearers/events) and must not assert canon events
  (who performed what, where, when). No claim leg requires any event/canon assertion.
- Lore's R10 register (`cross-cluster-contradictions.md`, per `r101-r10-register-first-entry.md`)
  is a canon-contradiction register — unrelated to movement registers and untouched.

## 6. Overlap map (summary)

| Register | Sibling owner? | Exact surface / note |
|---|---|---|
| Dance/performance/movement | **None** | 0 word-bounded matches in any sibling tree; adjacent: game-dev-3d (engine animation), audio (SFX), kake (web performance). Caveat: frozen sweep command false-positives on "avoidance" (funerary:4). |
| Ritual-calendar/festival | **None** (owner = kotodama itself) | `calendar-festival-systems.md`, `era-periodization-models.md`; siblings only process-rituals; lore owns event *dates* (canon). |
| Record-receipt discipline | Many (per-surface) | souji, chousa, tabi, tsukuroi, mado, mori, tameshi, kagi, kake, kumitate, kaidoku, kengaku — all own their own receipts; none owns kotodama's instrument. |
| No-git selftest guards | **None** | Nearest: kotoba (round-11 git-archive-no-history lesson — same failure class), kake/kama (could-not-evaluate conventions), game-dev-3d (git archive runs), souji (no-`.jj` handling). |

No sibling edit was made. All paths are fleet-root-relative.
