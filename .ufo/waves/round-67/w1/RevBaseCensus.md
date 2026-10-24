# RevBaseCensus — independent claim-C ownership census at base

Seat: `L1-kotodama-r67.RevBaseCensus` · 2026-10-24 · base `ad5b52b0ab5691358cd38718ab75649dc9916f9a`
Scope: falsify or confirm claim C's *premise* — "the medicine / healing / physician / remedy register
is unowned in `corpus/knowledge` at the base" — using a **different and wider** pattern than the
claim's own census, plus a topic-line sweep and an index sweep.
Read-only: no git/jj writes, no lane mutation, no tool installs (none needed).

## Verdict

**Claim C's base premise HOLDS.** There is **no whole-register filename owner** of the medicine /
healing register anywhere in `corpus/knowledge` at base under (a) the claim's own pattern, (b) the
assignment's wider pattern, and (c) a union-stem pattern that additionally covers `herb`, `physic`,
`apothec`, `pharmac`, `midwif`, `diet`, `hygien`, `wellness`, `ailment`, `illness`, `quarantin`,
`wound`, `poison`, `infect`, `contag`, `pregnan`, `childbirth`. The **only** filename hit in the union
census is `culture-material/bathing-and-body-hygiene.md`, matched by `hygien` — an entry the claim
itself already declares a partial-scope mention. **No statement in claim C is false on this evidence.**
Two evidence-integrity findings follow (F1, F2); neither invalidates the claim.

## Evidence — four independent censuses at the base revision

All commands run from the lane root against the pinned tree (`git ls-tree`/`git grep` at
`ad5b52b0…`), never the worktree.

| # | Census | Pattern | Result |
|---|---|---|---|
| 1 | claim's own (reproduced) | `(^\|[^a-z])(medicin\|healing\|physician\|remedy\|remedie\|surgery\|surgical\|apothec\|hospital\|leech\|physick\|medicine\|doctor\|shaman\|curander\|herbal)([^a-z]\|$)` over `git ls-tree -r --name-only BASE -- corpus/knowledge` | **0** (exit 1), 240 paths scanned |
| 2 | assignment's wider | `medicine\|medical\|health\|heal\|cure\|disease\|sick\|remed\|surg\|anatom\|plague\|epidemic` | **0** whole-path hits, **0** basename hits |
| 3 | union stems | (2) + `herb\|physic\|apothec\|pharmac\|midwif\|diet\|hygien\|wellness\|ailment\|illness\|pregnan\|childbirth\|wound\|poison\|infect\|contag\|quarantin` | **1**: `culture-material/bathing-and-body-hygiene.md` (`hygien`) — already declared partial scope |
| 4 | repo-wide (outside `corpus/knowledge`, excluding `.ufo/`) | pattern (2) | **0** — no medicine entry hides elsewhere in the lane either |

Adjacent-register probes (no medical-stem name but plausible owner): `humour\|humor\|miasm\|alchem\|
lazar\|quack\|panacea\|elixir\|triage\|hygi\|bath\|scent\|purif` → `bathing-and-body-hygiene.md`,
`scent-perfume-aromatics-codes.md`, `verification/to-verify-triage-protocol.md` (workflow triage, not
clinical). All three are cross-cutting, none owns the register.

Base counts, verified against the claim's arithmetic:

- `corpus/knowledge`: **240** files, all `.md` → declared 241 after `+1` entry ✓
- `corpus/knowledge/culture-material`: **33** → declared 34 ✓
- `corpus/SOURCES.md`: **724** row-shaped lines / **724** distinct ids, max id **S800** → declared 752
  (`724 + 4` disposition rows `S801-S804` + `24` new `S805-S828` = `752`) ✓ — arithmetic consistent
  with the claim's "728 + 24" phrasing; no `S8xx` id above S800 exists at base, so S805-S828 are
  unoccupied ✓
- Tier distribution at base: **A 442 / B 272 / C 10** → the claim's "each tier A or B" is
  **non-vacuous** (C-tier rows exist; a C-tier row among S805-S828 would violate the claim, and
  `SOURCES.md:16-18` states "C — lead only, never sole support for an admitted entry")
- `SOURCES.md` carries no prose total that the append + D2 move would leave stale (checked; the only
  numbers in the header are contract references)

## F1 — MEDIUM, evidence integrity: the claim's "only partial-scope mentions" list is **not exhaustive**

Claim statement (claims.json, C.statement) says the topic-line sweep "finds only partial-scope
mentions — bathing-and-body-hygiene, scent-perfume-aromatics prophylaxis, myth-symbol purity — not
whole-register owners". The *conclusion* ("not whole-register owners") survives my sweep; the
*enumeration* does not. Independent heading + `- topic:` + body sweeps at base add five in-corpus
anchors that carry real medical/healing content and are not named:

| Path:line at base | Evidence |
|---|---|
| `myth-symbol/amulets-talismans-apotropaic-marks.md:45` | heading `## 4. What the object answers: the danger-to-remedy table` — a table with rows for **plague** (S605), **"demons that cause ailments"** (S626), **"evil spirits and diseases"** (S638), **infertility and infant death** (S640). This file has the **highest medical-stem density in the corpus at base: 19 hits** |
| `myth-symbol/divination-omen-systems.md:89,126` | Greek incubation at Asclepieia; `:126` "a healing institution with a case archive (the *iamata*)"; `:89` "the sanctuary-as-hospital" |
| `myth-symbol/sacred-topography-pilgrimage.md:52,77` | `\| 6 \| healing / incubation shrine \|`; ":77 … 'medicine from incubation cases'" |
| `myth-symbol/animal-symbolism.md:100` | `\| Healing / sovereignty \| Rod of Asclepius … Hygieia's bowl …` |
| `myth-symbol/number-symbolism.md:44` | "four elements (Empedocles) → four humors (Galen) — medicine inherits the map" |
| `culture-material/bathing-and-body-hygiene.md:86` | heading `## 8. Health, medicine and the hygiene revolution` — substantive: emic bathing-as-therapy, **Semmelweis 1847**, **Snow 1854**, germ theory timing, the public-bath/wash-house acts, the dated cleanliness revolution (not a passing mention) |

Density ranking at base (medical-stem body hits, top of 240): amulets 19, bathing 18, then only
civilization entries and `taboo-euphemism-lifecycle` at ≤13 and mostly single mentions
(`ainu` epidemic deaths, `lakota-plains` whooping cough 1813-14, `levant-canaan` Eshmun "merely 'the
Phoenician Asclepius'", `maya-classic` ritual bloodletting — ritual, not clinical).

Why this matters for this round, concretely:

1. The claim text must not be quoted in the closure as an *exhaustion* claim. It is a *sufficiency*
   claim: no owner exists. Correct that reading in the LOG/SCORECARD wording if it is copied there.
2. The new entry and its `## Boundaries` section must reconcile with these six anchors, above all
   **Semmelweis/Snow/germ theory** (bathing §8) and **Asclepieia/iamata/incubation** (divination
   `:126`, pilgrimage `:52,:77`) — otherwise the new entry duplicates owned material and the coverage
   gain is partly illusory. Sibling seat `w1/CriticMedicineScope.md` already maps the neighbor
   boundaries one-way; its map is consistent with this census and should be the operative list.
3. Any S805-S828 row mined from amulet-side "danger/remedy" material must not restate the amulet
   table as a medical treatment taxonomy (`RESTATE` leg is the only mechanical guard, and it checks
   quote overlap, not register boundary).

## F2 — MEDIUM, instrument gap: the frozen counter does not pin its own premise

`reports/round-67/accept-c.py` legs are `STAMP, FILE, SET, ROWS, ONEID, RESTATE, HOSTS, LINK,
APPEND, NOHARM, SWEEP, CAPTURE, TOPIC` (docstring lines 18-44; `leg(...)` call sites at
`:202,220,252,278,290,322,335,347,373,384,395,417,431`). **There is no census leg.** The "0 filename
owners at base" premise exists only as prose in the docstring (`:4-6`) and in `claims.json`. Therefore
`ACCEPT-C-67: PASS` cannot detect a false premise: the counter would print PASS on a lane where a
medicine owner had existed all along.

- Consequence for this round: this report is the evidence for that clause, not the counter. The
  closure should cite `w1/RevBaseCensus.md` when it states the register was unowned at base.
- Not a fixable defect inside the frozen predicate (adding a `CENSUS` leg would change the predicate
  after freeze). Record it as a **carry-forward** for r68: a coverage claim's "unowned" premise
  should be a mechanical leg (`git ls-tree` at `--lands` + wide regex expecting 0), since the premise
  is exactly the part a data seat is most motivated to be lazy about.
- Related, weaker: at base the do-nothing control passes `LINK`, `APPEND`, `NOHARM`, `SWEEP`
  (`telemetry/dry-run-c.txt`) because no rows/entry exist yet. That is expected for a "no harm"
  class of leg, but it means four of thirteen legs carry no falsifying power pre-data; the control's
  value rests entirely on `FILE/SET/ONEID/RESTATE/HOSTS/CAPTURE/TOPIC` failing, which it does
  (verified in the same file).

## F3 — LOW, corroboration: the R66-D2 census defect is quantitatively exact at base

Independent computation from the base blob (`corpus/SOURCES.md`, 852 lines): sections at
`## Registry` 26, `## Paths` 733, `## Search log` 768, `## Leads (unopened)` 780. Row-shaped lines
**after** line 780: exactly **23** — `S776, S779…S800` — i.e. 23 E12 "row outside Registry section"
instances, matching `telemetry/census-start.txt` line-for-line, plus `E11 S753 missing used-by -`.
So the D2 disposition ("S776/S779-S800 moved into ## Registry and S753's used-by flipped to '—'")
addresses precisely the observed set and size, and the total row count 724 includes those 23 (the
move must not change the count — consistent with the claim's unchanged 724 base).

## F4 — Adjacent instrument check: the C-APPEND / Ca-D4 id conflict and the lands-separation resolution

Raised by `CriticFrontier` mid-seat; verified here from source because it touches claim C's own
`APPEND` leg.

- Code facts (not paraphrase): `accept-c.py:67` `NEW_IDS = S805..S828`; `:70`
  `EXTRA_IDS = {"S801".."S804"}`; `:357` `allowed_new = set(NEW_IDS) | EXTRA_IDS`; `:359-372` any
  appended id outside that union lands in `extra_ids` → **APPEND FAIL**. `accept-ca.py:68`
  `R66_REJECTS = S801..S804` (len 4); `:235` threshold `rej_opened_today < len(R66_REJECTS) + 2`,
  i.e. **≥6** rows with `status == rejected` and `opened == 2026-10-24`, counted over every registry
  line (not section-scoped). `:231` `new_rejects` is assigned and never read — dead.
- Therefore the two predicates are only jointly satisfiable by **evaluation-revision separation**, and
  L1 has ruled exactly that (no counter/claims revision): `A_r` (S801-S804 + r66 dispositions) →
  `A_c` (only S805-S828 append; `ACCEPT-C-67` evaluated in a clone at `A_c`, `evaluated == stamped
  == A_c`) → `A_ca` (S829+ rejects + round-67 lesson; `ACCEPT-CA-67` at `A_ca` sees ≥6). This is
  honest, not a bypass: `STAMP` fails if C's counter is pointed at any later revision, so a
  moved-past-lands PASS is impossible by construction.
- Conditions the closure must hold (both mechanical):
  1. Name all three lands revisions, and scope the counts: **752 rows at `A_c`**, **≥754 at `A_ca`**.
     `claims.json` C's "724 → 752" is lands-scoped while Ca's D4 needs the later count; quoted
     without their lands revisions the two statements read as contradictory.
  2. `S829+` rejects must sit **inside `## Registry`**: `accept-ca.py:169-172` runs
     `sources-census.sh validate --file <clone>/corpus/SOURCES.md` and requires exit 0, which flags
     `E12 row outside Registry section`; D4 alone would not catch a reject row parked under
     `## Leads` because it counts registry lines globally. A reject row under Leads would pass D4 and
     fail D2.
- Robustness nit (low): `accept-ca.py:54` `CENSUS` is a host-absolute path **outside** the lane repo
  (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`); if it is absent the counter raises
  instead of printing a `D2 FAIL`. `reg_path` correctly joins `root` (`:164`), so the clone's bytes
  are validated — no moved-worktree leak on that leg.

## Residual risk / verification gaps

- **Registered non-finding:** the premise is verified at *filename*, *heading/topic-line*, and
  *index-row* granularity plus a body-density ranking, not by full semantic read of all 240 entries
  (time-box). A register owner hiding under a completely non-medical name with a large section
  cannot be excluded by construction; the density heuristic bounds it (the only two files with ≥18
  medical-stem hits were read, and both are declared or now listed in F1).
- Heading sweep found no medical section anywhere except bathing §8 (and the ritual-bloodletting
  heading in `maya-classic.md:153`, which is ritual, not clinical).
- `corpus/knowledge` has no non-`.md` files at base, so no "entries vs files" counting ambiguity.
- `accept-c.py`'s premise gap (F2) is a permanent property of the frozen predicate: the `--lands`
  protocol pins *what* was measured, never *whether the premise was true*; my census is a one-shot
  manual control, not a repeatable leg.
- No dependency on another seat was needed; nothing was absent.

Report: .ufo/waves/round-67/w1/RevBaseCensus.md
