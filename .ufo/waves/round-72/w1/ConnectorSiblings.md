# ConnectorSiblings — round 72 w1 — sibling-overlap scan: heritage-taxonomy / state-classification-of-culture

Seat: L1Kotodama72.ConnectorSiblings (leaf; read-only everywhere except this report).
Basis: frozen claims `reports/round-72/claims.json` (Ca calibration, C coverage) at base b60c7b1; all paths below fleet-root-relative unless noted.

## Verdict

**In-lane. Uncontested.** The UNESCO ICH / state-heritage-register surface — reading state-published classification schemes (PRC 十大门类 intangible-heritage taxonomy, Japan 文化庁 分野 tree + 時代 ladder) as design models — is kotodama's by province bytes, and the sibling that would most plausibly contest it (lore) has already declared the split the other way in its own province.

No arbitration is owed. If a sibling ever claims it: contract §10 route — report to the **fleet integrator** (scope ruling; neither lane absorbs; "freeze only disputed output/import; continue separable reference work"), consistent with both lanes' "Out of province → report, never absorb" lines.

## Evidence — sibling claims

| Surface checked | Result |
|---|---|
| `kotodama-shokunin/PROVINCE.md` | Owns `corpus/knowledge/{…,culture-material,…}`; the two entries land in `corpus/knowledge/culture-material/` — exactly the owned partition. Refuses canon → lore; contested scope → integrator. |
| `lore-shokunin/PROVINCE.md` (round-103 map) | Adjacent paragraph assigns culture-material design knowledge **to kotodama by path** (`kotodama-shokunin/corpus/knowledge/culture-material/calendar-festival-systems.md`, `era-periodization-models.md`); "lore owns the names and dates recorded on landed entities and events." Lore owns fictional-world canon records, not real-world classification models. |
| `chousa-shokunin/PROVINCE.md` | Owns research **method** only (question framing, source hierarchy, citation chaining). No domain-content claim. Only touchpoint: external live-target fetch discipline — this round's fetches ran under the fleet census/gate, and the ihchina live-unreachable case is carried by dated Archive captures recorded in row S874. Method discipline, not surface ownership. |
| `kasegi-shokunin/PROVINCE.md` | Bounty/security domain only. Zero contact. |
| Word-boundary grep `\b(heritage|UNESCO|intangible|ICH|folklore)\b` over **all** sibling `*/PROVINCE.md` | **0 matches** (a bare `ich` pattern false-positives inside "which" — use word boundaries). |
| Same pattern over `lore-shokunin/SKILL.md` and `chousa-shokunin/SKILL.md` | **0 matches.** |
| `lore-shokunin/corpus/README.md` coverage map | No heritage/ICH row exists. CM-12 is lore's *own* real-world reference ledger (ETCSL, Kojiki, Völuspá — literary canon sources), not ownership of state heritage classification. Lore's one kotodama-facing row is CM-g **intake** (receives packets; does not own their content). |

Second-order note: the C claim's GROUND leg ("gap sweep … returns 0 owners at the 797-row registry") can only detect **in-lane** ownership gaps; it is structurally blind to a sibling claim. This scan is the cross-lane half of that leg, and it comes back clean.

## Handoff-obligation analysis (worldbible-integration-contract.md)

**No lore handoff obligation is created by admitting these entries.** Chain of evidence:

1. **Direction.** Rows S874/S875 are used-by the two lane-internal entries (S874 → both; S875 → the canonical entry). The entries are method/reference records, self-scoped: "a reference method for the culture-material partition … decides no world's canon"; the amend "decides no world's canon." No packet fields exist anywhere (no `packet_id`, no `baseline_bible_ref`, no lore entity refs).
2. **Contract trigger.** §8 step 1: a transfer begins with *lore's* brief (pull model). §4: unbound research material "may be retained as reference but cannot be imported as canon without a lore baseline." Corpus admission is not a transfer; the contract has no clause making admission a packet.
3. **Activation state (lore-side, current).** Lore coverage map CM-g: "intake of kotodama handoff packets | uncovered … lore has no acknowledgement record"; Known gaps: contract `kotodama-lore-adjacency` "sits at unacknowledged digest 5f4c02bf…"; frontier row: "acknowledge the contract at its current digest per its §1 fields, then define a packet-consumability intake check **before any import**." Lore's LOG.md is untouched for ~5 days — nothing newer than the round-103 (2026-10-19) statement.
4. **What the entries DO create** — a conditional future obligation only: if these ever feed a **first real packet**, then §1's both-lane re-read/acknowledge at the pinned digest, §4's envelope (dependency_manifest must carry these entries + row digests), §8's procedure, and §9's impact traversal all fire. Until then, nothing is owed to lore.

### Contradiction stated, not smoothed

Canonical entry §7 says "An invented culture's taxonomy lands in lore through the handoff contract" — present tense, as if the route were active — while contract §1 and lore CM-g say the interface is **unactivated** (bilateral acknowledgement pending). Not a byte-level contradiction, but a reading hazard: a future seat could read §7 as authorization to send. The entries are hash-pinned (`assimilation/validate/entry-pins.txt`: b2995163…, 9e4f804e…) — **editing the entries to add a caveat would invalidate the pins and the SCRATCHMIRROR/CITEDLINES legs.** The caveat must land outside the pinned bytes.

## Proposed move (one, bounded)

**Append a two-line sibling-overlap + activation note to `corpus/lessons/round-72.md`, after the `## Gate` section's per-row records** (scribe-owned file; appended as new trailing lines, existing Gate lines byte-unchanged). Lift-ready text:

> Sibling overlap (round-72 w1 scan): the heritage-taxonomy / state-classification-of-culture surface is in-lane — kotodama PROVINCE owns `corpus/knowledge/culture-material/`; lore PROVINCE (round-103 Adjacent) assigns culture-material models to kotodama by path; word-boundary grep finds zero heritage/UNESCO/intangible/ICH/folklore claims in any sibling PROVINCE or in lore/chousa SKILL.md. The C GROUND leg sweeps only the lane registry and cannot see sibling claims; this note closes that half.
> Activation caveat: both entries route any invented-taxonomy handoff through `synthesis/worldbible-integration-contract.md`, whose §1 bilateral acknowledgement is pending (lore CM-g uncovered; digest 5f4c02bf… unacknowledged; contract §8.1 is brief-first/pull). Admission of S874/S875 and the two entries creates no lore handoff obligation, and no packet may be sent until lore's §1 read-record exists.

**Axes affected:** coverage (C) only — completes the claim's ownership story at zero byte-cost to any pinned surface. **Harms none:** the round-72 lesson is outside Ca's APPENDONLY path set (`LOG.md`, `corpus/lessons/round-71.md`, `corpus/QUALITY.md`), outside the entry pins, and outside every C leg's byte-exact checks if appended without reformatting existing Gate lines. Coordination: the file is ScribeLesson/RevAppendOnly territory — this report is the handoff; the scribe lifts the text verbatim or reformulates without changing the two factual claims.

## Risks

- **Gate-format collision:** the GATE leg pins per-URL quote + admit/reject records in `## Gate`. The note must be appended, not interleaved; no existing line may move.
- **Pin drift:** anyone "fixing" §7 in the entry itself breaks entry pins (b2995163…/9e4f804e…) and the SCRATCHMIRROR/pins legs. Entry bytes are frozen for this round; the note is the only safe vehicle.
- **Freshness:** if lore acknowledged the contract between 2026-10-19 and today, the caveat's premise weakens. Evidence as of this scan says no (lore README frontier row still demands acknowledgement; LOG.md 5d stale). The note carries its evidence pointers so it ages honestly.
- **Misroute risk (chousa):** future register fetches are fleet-census fetch discipline, not chousa domain ownership; naming this in the note pre-empts a future misroute of the surface.

## Verification (for main / executing seats)

1. `grep -riE '\b(heritage|unesco|intangible|ich|folklore)\b' /home/vgpnk/Projects/shokunin/*/PROVINCE.md` → no matches.
2. After any append: `sha256sum corpus/knowledge/culture-material/heritage-taxonomy-models.md{,.amend-2026-10-24-r13.md}` still b2995163… / 9e4f804e… (entry pins intact).
3. `git diff -U0 b60c7b1..<lands> -- LOG.md corpus/lessons/round-71.md corpus/QUALITY.md` still shows appends only (Ca APPENDONLY untouched by the note).
4. `python3 -B reports/round-72/accept-c.py --root . --lands <lands>` still PASS 10/10; census validate exit 0 unchanged.

## Tooling record

No tools installed or updated (read-only scans sufficed; pacman paused per orchestrator 2026-10-20 — not invoked).
