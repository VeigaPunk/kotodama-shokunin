- Seat: A05 | executor | claim A | date 2026-10-19 | baseline 139e3b6

# A05 — Corpus boundary check: partitions vs PROVINCE owns-list, `examples/` non-canon, verification/civilizations drift

**Assignment (`reports/round-33/targets.json`, seat `A05`):** "Corpus boundary
check: partitions on disk vs PROVINCE owns-list; examples/ dirs are in-lane
non-canon (confirm); no verification/civilizations partition drift into foreign
ownership."

**Snapshot.** `date -u '+%Y-%m-%dT%H:%M:%SZ'` → `2026-10-19T03:59:02Z`;
`git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb` (== the declared
baseline, `reports/round-33/claims.json:8`). Pins read at this snapshot:
`PROVINCE.md` sha256 `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`
(31 lines, 1636 bytes); `corpus/README.md` sha256
`053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`;
`corpus/QUALITY.md` sha256 `6aab8800986f37ca26a23ac8a0e3563e2dcb9f62975eb1c05e4a78d2b56f7bca`.
All commands read-only, run at the lane root; my only write is this fragment.

## Check A05-1 — partitions on disk vs the PROVINCE owns-list — PASS (exact set match, both directions)

`PROVINCE.md:9-11` names the owns-list as
`` `corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}` ``.
Set-diffed against the live directory (`os.listdir('corpus/knowledge')`, run in
this session):

| probe | result |
|---|---|
| declared (parsed from `PROVINCE.md:10`) | `civilizations, culture-material, linguistics, myth-symbol, synthesis, verification` |
| on disk | `civilizations, culture-material, linguistics, myth-symbol, synthesis, verification` |
| declared-not-on-disk | `[]` |
| on-disk-not-declared | `[]` |
| `MATCH` | `True` |

**Verdict: PASS.** Six declared, six on disk, empty diff in both directions —
no unowned partition on disk and no owned partition missing. This is the
sharper form of `reports/round-33/adj/A01-province.md` §A01-2's "exactly those
six, no seventh": A01 measured the directory count, this check also measures
the *name sets*, so a rename (six dirs, one wrong name) would fail here.

Supporting shape probes, all clean: `corpus/knowledge/` holds **only** the six
directories and no files (`ls -la corpus/knowledge/` → six `drwxr-xr-x` rows,
no regular files); `find corpus/knowledge -type f ! -name '*.md'` → empty, so
no non-entry artifact (script, JSON, image) has been parked inside an owned
knowledge partition.

## Check A05-2 — `examples/` directories are in-lane non-canon — CONFIRMED

`PROVINCE.md:11` claims "non-canon examples" as lane-owned. Live inventory
(`ls examples/`, `git ls-files examples | wc -l` → **68 tracked files**):

| artifact | non-canon declaration |
|---|---|
| `examples/culture-d2/` (35 tracked) | `examples/culture-d2/ASSEMBLY.md:3` "Non-canon design drill. This is a gate packet, not an accepted culture or a lore handoff."; per-component `canon: not canonized (D2 design drill)` at `examples/culture-d2/components/01-brief.yml:6`; `examples/culture-d2/components/01-brief.yml:332` "NON-CANON. This file is a design drill record" |
| `examples/culture-d3/` (10 tracked) | `examples/culture-d3/README.md:1` title suffix `(NON-CANON)`; `:10-12` "**This is not canon, not a world-bible entry, and not accepted by lore-shokunin.** The packet is `canon_status: NON-CANON`, `handoff_status: prepared-not-accepted`"; `examples/culture-d3/packet.json:291` `"canon_status": "NON-CANON"`; `:876` "No lore receipt … No baseline bible binding, acceptance, promotion verification or canonization is claimed anywhere in the D3 artifacts." |
| `examples/culture-d4/` (20 tracked) | `examples/culture-d4/README.md:1` title suffix `(NON-CANON)`; `:4` "**NON-CANON**: not canon, not a world-bible entry, not accepted by"; `examples/culture-d4/ASSEMBLY.md:3` "Non-canon design drill … not an [accepted culture]" |
| `examples/supplement-opencode-1/` (1 tracked) | `examples/supplement-opencode-1/sound-change-vs-taboo.json:12` `"canon_status": "non-canon"`; `:246` "Non-canon: all forms, dates, roles, and rules are design variables." |
| `examples/handoff-packet.sample.md` | `:3` "NON-CANON sample world-bible handoff packet"; `:15` "canon_standing: not canonized — lore disposition required (lore-shokunin owns canon)" |
| `examples/handoff-packet.sample.yml` | `:1` "# handoff-packet.sample.yml — NON-CANON sample world-bible handoff packet"; `:70-71` `packet_status: "sample — non-canon; unbound; never submitted to lore"`, `canon_status: "not canonized (contract §6: canon standing is lore's alone)"` |

**Verdict: CONFIRMED in-lane non-canon, with one named coverage note.**
Directory-level and artifact-level declarations are present on all four
directories and both loose samples. Six *leaf* files carry no inline marker and
inherit their status from the declaring `README.md`/`ASSEMBLY.md`:
`examples/culture-d2/expected-holds.json`,
`examples/culture-d3/components/04-language.json`,
`examples/culture-d3/components/05-ritual.json`,
`examples/culture-d3/components/06-material.json`,
`examples/culture-d3/expected.json`,
`examples/culture-d4/expected-holds.json` — each is a pure machine-generated
data/expected artifact inside a declared NON-CANON directory. I record this as
a coverage note, **not** a defect and **not** a fix request: the mission asks to
*confirm* the directories are in-lane non-canon, and they are; adding markers to
generated fixtures would change delivered bytes for no ownership gain.

Foreign-domain content probe inside `examples/`:
`grep -rniE '(chousa|kake|kotoba|game-dev|sibling repo)' examples/` → **0
matches**. The only out-of-lane names that appear are *routing recipients*
(`examples/culture-d2/components/03-morphosyntax.yml:331` `{id: Q-05, to:
"lore-shokunin", question: "canon adoption, …"}`), which is the required
direction of travel, not absorption. No `examples/` file references a sibling
repository path.

## Check A05-3 — verification/civilizations drift into foreign ownership — PASS (zero drift; all 17 classifier residuals reviewed line-by-line)

`PROVINCE.md:12-14` constrains exactly this: "The verification and civilization
partitions support linguistic-cultural coupling; they do not expand ownership
into general research method, fleet protocol, historical truth certification or
lore's canon."

Method: for every `.md` file in both partitions, each line matching
`(canon|world bible|world-bible|chousa|kake|kotoba|game-dev|fleet protocol|lore-shokunin|historical truth|rights ruling|attribution ruling|general research method)`
was classified by a boundary-marker heuristic (`never|not|no|owns|routed|hand
off|handoff|refuse|outside|sibling|lore's|separate|only|does not|this lane|
boundary|without|beyond|leave|deliver|decides|alone|pending|propos|option|
fixture|caution|limit|out of scope|stop before|preserve|recheck`). Everything
the heuristic did *not* mark was then read in context — no residual was left
unclassified.

| partition | files | term-lines | boundary-marked | residual | residual reviewed | drift found |
|---|---|---|---|---|---|---|
| `verification` | 20 | 132 | 125 | 7 | 7/7 | 0 |
| `civilizations` | 94 | 369 | 359 | 10 | 10/10 | 0 |

All 17 residuals, with the reason each is *not* drift:

*verification (7)*
- `calibration-registry.md:87` — "label that an invented supernatural premise **for lore-shokunin to accept or reject**" → route-to-lore.
- `gate-frozen-run-standard.md:37` — "nothing about design quality or canon" → negation.
- `gate-frozen-run-standard.md:240` — "it **never** enters the world bible, **never** marks a design accepted, and **never** substitutes for lore-shokunin's consistency verification or canon rulings (lane `AGENTS.md`, `PROVINCE.md`)" → negation, self-cites this lane's own boundary.
- `header-conformance-readings.md:149` — asks *which reading* produced a "sourced and dated" claim → method question, no ownership claim.
- `label-channel-routing-verification.md:8` — cites an in-lane drill artifact `examples/culture-d4/typed-labels.d4.yml`, tail "NON-CANON" → in-lane citation.
- `pre-declared-hold-set-reconciliation.md:6` — cites `examples/culture-d4/components/01-brief.yml`, "NON-CANON drill artifact" → in-lane citation.
- `to-verify-triage-protocol.md:52` — lists "Literal historical truth of a myth" as a **non-permitted** inference in its table → explicit refusal of truth certification.

*civilizations (10)*
- `anatolia-hittite.md:155` — "invent the rule first, then generate new forms **instead of pasting historical names into canon**" → design guidance avoiding canon.
- `byzantium.md:182` — "**Lore-shokunin selects canon; this entry selects none.**" → explicit non-selection.
- `hawaii.md:85` — "Keep competing interpretations **visible to lore-shokunin**" → routing.
- `java-majapahit.md:136` — "Supernatural efficacy can remain a character's belief **unless lore-shokunin explicitly chooses otherwise**" → routing.
- `java-majapahit.md:192` — "rather than assuming one original 'canon'" → philological/textual sense of canon (a corpus of received texts), not fictional-world canon; adjacent line `:193` supplies the handoff schema and says "Supply no accepted world-bible facts from this entry alone."
- `korea-three-kingdoms-goryeo.md:133` — "carving a **textual** canon from recording a vernacular language" → historical Buddhist textual canon.
- `mesoamerica-primary-sources.md:155` — "maps each source class onto canon tags" → the *lane's own* tag vocabulary, owned by `corpus/knowledge/culture-material/material-culture-inference-method.md:3` ("the eight-tier inference-confidence ladder … with canon tags for lore handoff"); its misuse is separately forbidden at `corpus/knowledge/verification/citation-format-and-source-registry.md:21` ("Citation confidence must not silently become a canon tag").
- `persia-achaemenid.md:54` — heading "Imperial trilingualism as a canon-language case study" → explicitly analogical; `:61` "an analogy for authorized versions of a ruling narrative, **not** evidence that royal inscriptions were one standardized sacred scripture."
- `swahili-coast.md:195` — "**Nothing** in this entry establishes fictional canon; unresolved choices remain for lore-shokunin." → negation.
- `thrace-dacia.md:173` — "offer alternatives **to lore-shokunin**" → routing.

The partition-level posture is likewise explicit and in-lane, not merely
implicit: `corpus/knowledge/verification/provenance-audit-ledger-format.md:15`
("Lore-shokunin decides fictional truth. … it never changes the world bible."),
`corpus/knowledge/verification/verification-method-overview.md:206` ("Final
invariant: **no observation → inference laundering; no unknown → fact
laundering; no design → attestation laundering; no local PASS → canon
laundering.**"), `corpus/knowledge/synthesis/worldbible-integration-contract.md:17-18`
("lore owns world-bible entities, relations, chronology, canon decisions, and
bible-wide consistency verification … A request from lore does not grant
kotodama world-bible write access; a receipt does not delegate canon
authority."), and `corpus/QUALITY.md:18-20` ("**Canon hygiene** — no entry
decides what is true in any world.").

**Verdict: PASS — zero drift.** No line in either partition claims general
research method, fleet protocol authorship, historical-truth certification, or
lore's canon; every term-line is either a boundary statement, a route-to-lore,
a negation, an in-lane artifact citation, or a historical/textual use of the
word *canon*.

## Check A05-4 — out-of-repo reference inventory in the corpus — PASS (2 read-only citations, both declared)

Drift into foreign ownership would also show as the corpus depending on a
surface outside this repo. Full sweep for out-of-repo paths
(`(\.\./){3,}`, `/home/…`, `~/…`, `(\.\./)*(lore-shokunin|chousa-shokunin|kake|kotoba)/`)
over `corpus/knowledge` returned exactly **two** hits:

| hit | reading |
|---|---|
| `corpus/knowledge/verification/internal-consistency-audit.md:11` — `../../../PROVINCE.md` | resolves *inside* this repo to `PROVINCE.md`; in-lane self-reference |
| `corpus/knowledge/verification/header-conformance-readings.md:4` — `/home/vgpnk/Projects/shokunin/CORPUS.md:17` | an absolute host path to the fleet-root contract; the file exists (`-rw-r--r-- 3223 bytes, 2026-10-13 16:46`), read-only citation, and the entry's own `recheck:` clause names the dependency (`header-conformance-readings.md:6`: "recheck this entry … if `CORPUS.md` is amended") |

The fleet-protocol adjacency is likewise a *citation*, not authorship:
`corpus/knowledge/verification/gate-frozen-run-standard.md:6-8` sources the
lane's gate standard from fleet `PROTOCOL.md` §"Gate standard" /
`PROTOCOL-APPENDIX.md` (read-only, `../PROTOCOL.md`) while naming this lane as
the registry home — "The lane's *registry home* for gate rows is its own
`SKILL.md` §Gates. Line numbers are pinned in the fleet appendix, not here."
`PROVINCE.md:27-29` permits reading those surfaces; no corpus entry writes
them.

**Verdict: PASS with one observation for the integrator (not a defect).** The
corpus's only non-repo dependency is the absolute host path at
`header-conformance-readings.md:4`. It is a read-only citation with a declared
recheck trigger, so it is not drift; if a portability pass is ever scheduled, a
repo-relative or fleet-root-relative pointer would be the bounded fix, and the
`recheck:` clause already carries the owner. I do not propose editing filed
corpus bytes here.

## Check A05-5 — round-33 write window: `corpus/` and `examples/` untouched — PASS

`git status --porcelain corpus examples` → **empty** (no modified, added or
deleted path). Partition directory mtimes are all pre-round-33:
`civilizations` 2026-10-17 12:09, `culture-material` 2026-10-17 18:36,
`myth-symbol` 2026-10-17 18:37, `verification` 2026-10-18 08:35, `synthesis`
2026-10-18 08:37, `linguistics` 2026-10-18 17:20 — all earlier than the round-33
declaration stamp `2026-10-19T03:49:01Z` (`reports/round-33/claims.json:6`).
Tracked-path baseline reproduces: `git ls-files | wc -l` → **2655**, matching
`reports/round-33/claims.json:64`'s "2655 at baseline commit 139e3b6".

**Verdict: PASS.** No partition file was created, edited or deleted during the
round-33 window, so no boundary drift could have been introduced by this wave.

## Check A05-6 — corpus index integrity cross-check, resolving A01's stale-prose item — PASS

A01 left an open item: "the 19/19/18/29/20/94 census in `corpus/README.md:95`
is a *previous revision's* reading … a stale-prose item"
(`reports/round-33/adj/A01-province.md` §A01-2). My evidence resolves it — the
census at `corpus/README.md:90-91` sits inside the **revision log**, not the
live claim surface, and the live surfaces are current:

- Re-ran the filed instrument verbatim: `python3 -B reports/round-28/readme/sweep.py`
  → `exit=0`, `parts {"civilizations": 94, "culture-material": 18, "linguistics": 21, "myth-symbol": 19, "synthesis": 29, "verification": 20}`,
  `rows 201 files 201`, `missing_from_index 0 []`, `topic_mismatch 0 []`,
  `orphan_rows 0 []`, `header_drift {}`, `totals_line 201 totals_ok True`,
  `footer_live {"total": 201, "dir_totals": [21, 19, 18, 29, 20, 94]}`, `footer_ok True`,
  `readme_sha256 053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`.
- Independent second method: `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` reports the same per-partition counts; plain `os.listdir` counting in this session gives the same 21/19/18/29/20/94 = **201**.
- The live totals line reads **201** and the live counts footer (from `corpus/README.md:471`, "Counts checked 2026-10-18 from the repo root") reads **201** / `21/19/18/29/20/94`.

**Verdict: PASS — no live index drift; A01's stale-prose item is closed as
"dated reading inside the revision log, superseded in-file by revision 1.9".**
Ownership note: the *lessons* index is a different file
(`corpus/lessons/README.md`) and belongs to claim O's C-seat legs; I did not
audit it and make no verdict on it.

## Verdict table

| check | verdict | basis |
|---|---|---|
| A05-1 partitions vs owns-list | **PASS** | empty set diff both directions; only the six directories, no stray files |
| A05-2 `examples/` in-lane non-canon | **CONFIRMED** | declarations at dir + artifact level on all 4 dirs and both samples; 0 foreign-domain references; 6 generated leaf fixtures inherit dir status (coverage note, not a defect) |
| A05-3 verification/civilizations drift | **PASS** | 501 term-lines across 114 files; 17 residuals read line-by-line, 0 drift; boundary invariants explicit in-file |
| A05-4 out-of-repo references | **PASS + 1 observation** | exactly 2 hits, both read-only in-lane/fleet citations with declared recheck triggers |
| A05-5 round-33 write window | **PASS** | `git status` clean for `corpus/ examples/`; all partition mtimes pre-declaration; 2655 tracked paths |
| A05-6 corpus index integrity | **PASS** | round-28 sweep exit 0, 201 rows vs 201 files, footer 201 / 21-19-18-29-20-94; closes A01's open item |

Net for claim A's adjacency leg: **the corpus boundary is intact at HEAD** —
no unfiled bleed, no unowned partition, no foreign-ownership expansion, and no
promotion/canon/closure language introduced by this round's corpus surface.
This fragment asserts nothing about promotion, canon or closure, and reports no
contested scope: the one boundary-adjacent item (the absolute path at
`header-conformance-readings.md:4`) is already declared in-file with an owner
and a recheck trigger, so it is routed, not absorbed.

## Limits / to-verify

- The drift classifier is a heuristic: 484 of 501 term-lines were auto-marked
  as boundary statements, and I read all 17 unmarked ones in context. A line
  that *agrees* with a boundary marker while asserting the opposite in a
  different clause would survive this pass; I found none in the 17, but the
  guarantee is "every flagged line was read", not "every line was read".
- `to-verify`: whether `corpus/knowledge/civilizations/*.md` entries ever
  assert real-world historical truth in the *body* prose (my sweep only covers
  lines carrying the enumerated ownership terms). A full truth-claim audit is a
  different check and I did not run it.
- `to-verify`: `examples/culture-d3/controls.json:47` declares a control named
  `domain-D3-CANON-canon-status-promoted` — I read this as a *negative control*
  (a planted defect the drill expects the gate to catch) from its position in
  the controls list and the packet's `canon_status: NON-CANON`
  (`examples/culture-d3/packet.json:291`), but I did not execute the D3 runner
  to confirm the control is expected-to-fail.

## Owed: none

## Citations

Paths
- `PROVINCE.md:9-11` (owns-list), `:12-14` (no expansion into general research method / fleet protocol / historical truth / canon), `:16-20` (refusals), `:22-25` (lore adjacency), `:27-29` (write scope), `:31` (out-of-province rule)
- `reports/round-33/targets.json` (seat `A05` mission/out; `shared_rules`), `reports/round-33/claims.json:6,8,64` (declaration stamp, baseline commit, 2655 tracked paths)
- `reports/round-33/telemetry/dispatch-declared.json` (round-33 observation window)
- `reports/round-33/adj/A01-province.md` §A01-2 (six partitions, open stale-prose item) — read, not edited
- `corpus/QUALITY.md:3` (admission into `corpus/knowledge/`), `:18-20` (canon hygiene), `:22` (rejections in `lessons/`)
- `corpus/README.md:3-15` (revision 1.9 live reading), `:90-91` (revision-log census, dated), `:471` + tail (live counts footer)
- `corpus/knowledge/verification/{provenance-audit-ledger-format.md:15, citation-format-and-source-registry.md:21, verification-method-overview.md:206, gate-frozen-run-standard.md:6-8, header-conformance-readings.md:4,6, internal-consistency-audit.md:11, to-verify-triage-protocol.md:52}`
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:17-18`
- `corpus/knowledge/culture-material/material-culture-inference-method.md:3` (canon-tag vocabulary owner)
- `examples/culture-d2/ASSEMBLY.md:3`; `examples/culture-d2/components/01-brief.yml:6,332`; `examples/culture-d2/components/03-morphosyntax.yml:331`
- `examples/culture-d3/README.md:1,10-12`; `examples/culture-d3/packet.json:291,876`; `examples/culture-d3/controls.json:47`
- `examples/culture-d4/README.md:1,4`; `examples/culture-d4/ASSEMBLY.md:3`
- `examples/supplement-opencode-1/sound-change-vs-taboo.json:12,246`
- `examples/handoff-packet.sample.md:3,15`; `examples/handoff-packet.sample.yml:1,70-71`

Commands (all at the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`)
- `date -u '+%Y-%m-%dT%H:%M:%SZ'` → `2026-10-19T03:59:02Z`; `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`
- `sha256sum PROVINCE.md corpus/README.md corpus/QUALITY.md` → `05b34a57…b942d6`, `053966a2…d57c`, `6aab8800…7bca`
- python set-diff of `PROVINCE.md:10` brace-list vs `os.listdir('corpus/knowledge')` → both diffs `[]`, `MATCH True`
- `find corpus/knowledge -maxdepth 1 -mindepth 1 -type d -printf '%f\n' | sort` → the six; `find corpus/knowledge -type f ! -name '*.md'` → empty
- python drift classifier over `corpus/knowledge/{verification,civilizations}/*.md` → `verification: files=20 term-lines=132 boundary-marked=125 residual=7`; `civilizations: files=94 term-lines=369 boundary-marked=359 residual=10`; each residual `sed -n` read in context
- `grep -rniE '(chousa|kake|kotoba|game-dev|sibling repo)' examples/ | wc -l` → `0`
- `grep -rnoE '(\.\./){3,}[A-Za-z0-9_.-]+|/home/[A-Za-z0-9_./-]+|~/[A-Za-z0-9_./-]+' corpus/knowledge` → 2 hits (listed in A05-4); `ls -la /home/vgpnk/Projects/shokunin/CORPUS.md` → 3223 bytes, exists
- `git status --porcelain corpus examples` → empty; `find corpus/knowledge -maxdepth 1 -type d -printf '%TY-%Tm-%Td %TH:%TM %p\n' | sort` → all pre-2026-10-19
- `git ls-files | wc -l` → `2655`; `git ls-files examples | wc -l` → `68`
- `python3 -B reports/round-28/readme/sweep.py` → exit 0, full reading quoted in A05-6
- `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → per-partition counts 21/19/18/29/20/94
