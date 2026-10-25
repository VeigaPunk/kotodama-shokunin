# ConnectorSiblings — round 74 w1 — sibling-overlap scan: worldbuilding-setting-practice / practitioner craft

Seat: `L1Kotodama74.ConnectorSiblings` (leaf seat; read-only everywhere except this report).
Basis: draft claims in `reports/round-74/claims.json` (C coverage, Ca calibration) at base revision `f7104cbce186bc2e1522abf0cfd619cc834628bb`; fleet root `/home/vgpnk/Projects/shokunin`.
Theme surface: **worldbuilding-setting-practice** (how a fictional setting is specified: layered world-view, settings-note tables, single-source-of-truth documents, build order, delivery schedule — from Japanese and Chinese practitioner guides S883, S884, S899, S900, paired with scholarly anchors S882/S877 and S895).

---

## 1. Overall Verdict

**In-lane (Kotodama), with an explicit provincial boundary and partial adjacency to `lore-shokunin`.**

1. **Kotodama ownership:** Kotodama owns the authorial, generative, and coupling craft of specifying settings (`kotodama-shokunin/PROVINCE.md:9-11`). The four-layer causal chain (自然環境 → 社会の仕組み → 文化 → 個人の経験; S883), the setting-note template schema (設定ノートの構成例; S884), the premise-driven build order (世界观 → 升级体系 → 升级体现; S899), and narrative delivery pacing heuristics (20章之内慢慢来; S900) are author-facing reference methodology. They live legitimately in `corpus/knowledge/culture-material/`.
2. **Lore boundary:** `lore-shokunin` owns fictional-world records (entities, relations, timeline events), the canonical world bible, and bible-wide consistency verification (`lore-shokunin/PROVINCE.md:3, 17-23, 28`). Lore does not own general setting-authoring craft or practitioner guides. However, because S884 describes data structures that mirror lore's entity tables, and S900 discusses delivery schedule while lore lists reveal order vs chronology (CM-f) as an uncovered frontier, this boundary must be explicitly delineated.
3. **No sibling contests this surface:** A comprehensive word-boundary grep across all sibling knowledge trees (`corpus/knowledge/`) for `worldview`, `world-view`, `worldbuilding`, `setting-note`, `世界観`, `世界观`, and `設定ノート` yields **0 matches**.
4. **Handoff status:** **No lore handoff obligation fires.** Contract `worldbible-integration-contract.md` is pull-based (§8.1), treats reference entries as unbound research packets (§4.69), and requires bilateral read-acknowledgement (§1.14-15) which lore has not completed (lore CM-g is uncovered; digest `5f4c02bf...` unacknowledged).

---

## 2. Verdict per Sibling Lane

| Sibling lane | Verdict | Boundary summary | Primary evidence (path:line) |
|---|---|---|---|
| **lore-shokunin** | **partial** | Lore owns fictional-world records (entities, relations, timeline events), world-bible consistency verification, and reveal order vs chronology verification (CM-f). Kotodama owns generative craft, setting-authoring methodology, and practitioner guides. Canon records stay with lore; reference craft stays with kotodama. | `lore-shokunin/PROVINCE.md:3, 17-23, 28`<br>`lore-shokunin/corpus/README.md:71-73, 90, 94`<br>`lore-shokunin/SKILL.md:6-11`<br>`kotodama-shokunin/PROVINCE.md:9, 16, 22`<br>`contract:11, 17, 38, 58, 126, 209` |
| **chousa-shokunin** | **none** | Chousa owns deep-research method (question framing, source hierarchy, citation hopping). Zero ownership of worldbuilding craft. Kotodama applies source-tier discipline (Tier B scholarly vs Tier C practitioner leads) without absorbing research methodology. | `chousa-shokunin/PROVINCE.md:3-8, 10-15`<br>`corpus/knowledge/` grep: 0 matches |
| **kotoba-shokunin** | **none** | Kotoba owns prompt and skill craft (SKILL.md/AGENTS.md quality, trigger fidelity). Kotoba explicitly names kotodama as adjacent for "worldbuilding and naming" (`PROVINCE.md:61`), refusing it. | `kotoba-shokunin/PROVINCE.md:3, 61`<br>`corpus/knowledge/` grep: 0 matches |
| **kengaku-shokunin** | **none** | Kengaku owns LLM/model evaluation and benchmark task-spec audits. Zero contact with worldbuilding craft or fictional setting specification. | `kengaku-shokunin/PROVINCE.md:3, 24-34`<br>`corpus/knowledge/` grep: 0 matches |
| **kumitate-shokunin** | **none** | Kumitate owns swarm orchestration, dispatch runtime, worktree isolation, and task coordination. Zero contact with fictional setting craft. | `kumitate-shokunin/PROVINCE.md:3, 25-29`<br>`corpus/knowledge/` grep: 0 matches |
| **tameshi-shokunin** | **none** | Tameshi owns reusable verification-fixture craft and mutation testing. Explicitly refuses product domains (`PROVINCE.md:14-18`). Does not contest worldbuilding craft. | `tameshi-shokunin/PROVINCE.md:3-6, 14-18`<br>`corpus/knowledge/` grep: 0 matches |
| **kake-shokunin** | **none** | Kake owns web properties, publishing platform semantics, Pages deploys, and sitemaps. Zero contact with worldbuilding craft. | `kake-shokunin/PROVINCE.md:3, 33-42`<br>`corpus/knowledge/` grep: 0 matches |
| **mado-shokunin** | **none** | Mado owns desktop and compositor craft (Hyprland, waybar, walker). Round-36 refinement explicitly refuses documentation-localization mechanics (`PROVINCE.md:67-81`). Zero contact. | `mado-shokunin/PROVINCE.md:3-16, 67-81`<br>`corpus/knowledge/` grep: 0 matches |
| **kagi-shokunin** | **none** | Kagi owns secrets and vault operations (the-janitor flows, credential hygiene). Zero contact with worldbuilding craft. | `kagi-shokunin/PROVINCE.md:3, 59-60, 67-68`<br>`corpus/knowledge/` grep: 0 matches |
| **souji-shokunin** | **none** | Souji owns fleet repository and workspace hygiene (receipt-gated removal of stale artifacts). Zero contact with worldbuilding craft. | `souji-shokunin/PROVINCE.md:3, 34-47, 79-87`<br>`corpus/knowledge/` grep: 0 matches |

*(Additional fleet lanes checked for completeness: `audio-shokunin`, `game-dev-2d-shokunin`, `game-dev-3d-shokunin`, `kama-shokunin`, `kasegi-shokunin`, `kaidoku-shokunin`, `mori-shokunin`, `revenger-shokunin`, `tabi-shokunin`, `tsukuroi-shokunin` — all return **none** on domain definition and 0 grep matches across their knowledge bases).*

---

## 3. Deep-Dive: The `lore-shokunin` Boundary Analysis

### 3.1. Surface Comparison and Potential Boundary Tensions

The assimilation of the worldbuilding-setting-practice package introduces five practitioner concepts into kotodama's `culture-material/` partition:
1. **Four-layer worldview causal chain (S883 / LitMemo):** Natural environment (自然環境) → social structures (社会の仕組み) → culture (文化) → individual values/experience (個人の価値観・経験).
2. **Setting-note structural tables (S884 / tuduku.space):** Setting notes (設定ノート) comprising world maps/place names (世界地図・地名一覧), chronology (年表), ability lists (魔法・能力一覧), character profiles (人物一覧), and institutional glossaries (社会制度・用語集).
3. **Single-source-of-truth discipline (S883 / LitMemo):** Maintaining a single canonical settings manual (設定資料集) per series to prevent drift between drafting text and established rules.
4. **Premise-driven build order (S899 / Chinawriter 2025):** Establishing the worldview rules first, deriving progression mechanics from the world premise, and determining character expression last.
5. **Delivery schedule heuristics (S900 / Chinawriter 2022):** Disclosing rules gradually within the opening chapters (roughly within the first 20 chapters) with narrative hooks, avoiding immediate rule dumps or prolonged concealment.

This surface touches `lore-shokunin`'s province across three direct contact points:

* **Contact Point A: Setting Notes vs. World Bible Tables.**
  S884 outlines the concrete tables an author uses: character lists, place names, chronology, and faction power balances. In `lore-shokunin`, these exact concepts form the Core governed schema: `entities.json` (characters, places, factions, items), `timeline.json` (events, integer ticks, dependencies), and `relations.json` (directed links, reciprocal alliances).
  * *Provincial resolution:* S884 provides an *authorial note-taking heuristic* (how a novelist drafts and files their preliminary notes). Lore owns the *authoritative in-world records and their mechanical verification*. Kotodama records the method of structuring notes; lore records and validates the landed world facts.

* **Contact Point B: Single Source of Truth (設定資料集) vs. Canon Consistency.**
  S883 argues for maintaining a single authoritative settings book to keep long-form fiction consistent. In `lore-shokunin`, consistency is enforced mechanically by `fixtures/check_bible.py` and procedural gates (CM-01 through CM-12, CM-e canon supersession in `r103-canon-status-and-supersession.md`).
  * *Provincial resolution:* Kotodama records the practitioner advice that authors should maintain an SSOT; Lore *is* the fleet's implementation of an SSOT and its consistency checking. Kotodama does not enforce bible consistency or maintain canon records.

* **Contact Point C: Delivery Schedule vs. CM-f Reveal Order.**
  S900 discusses authorial disclosure timing ("release the world's rules gradually and early — inside roughly the first twenty chapters"). In `lore-shokunin/corpus/README.md:72, 90`, lore lists `CM-f reveal (narrative) order vs chronology (fabula/syuzhet)` as an **uncovered frontier item** ("nothing separates reader-facing reveal order from event order, so spoiler/discourse-order errors are uncheckable").
  * *Provincial resolution:* S900 provides *narrative pacing advice for novelists* (a craft rule of thumb). Lore's CM-f is a *data model and consistency checker* to prevent narrative anachronisms or spoiler leaks in story records. Kotodama's entry records authorial guidance; it does not define an event-order schema, model character knowledge states over time, or check narrative spoiler safety.

### 3.2. What Stays Reported-Not-Absorbed

In strict adherence to `kotodama-shokunin/PROVINCE.md:16-25` ("Refuses: claiming or recording canon — that is lore-shokunin") and `corpus/knowledge/synthesis/worldbible-integration-contract.md`:
1. **Fictional canon entities and facts:** Any character, faction, event date, place, or historical occurrence generated or referenced as a worked example remains non-canon fiction. Kotodama never asserts in-world fact.
2. **In-world bible consistency enforcement:** Kotodama does not run or absorb bible-wide consistency checks (entity reference validation, relation reciprocity, timeline topological sorting). That remains lore's exclusive domain (`check_bible.py`).
3. **Mechanical reveal-order verification (CM-f):** Kotodama records S900's craft heuristics on chapter disclosure, but refuses any automated reader-revelation checker or event-tick spoiler validator.

---

## 4. Handoff-Obligation Analysis (`worldbible-integration-contract.md`)

**Does admitting the worldbuilding-setting-practice entries create a lore handoff obligation? NO.**

Evidence from `corpus/knowledge/synthesis/worldbible-integration-contract.md`:

1. **Pull Model (§8.1):**
   * Section 8, Step 1 explicitly specifies: *"Lore supplies a scoped brief, baseline bible reference, existing entity/era keys, constraints, canon policy, and the actual authorized receipt surface; absent inputs become explicit questions."*
   * A transfer is initiated by lore requesting a system, not by kotodama unilaterally pushing newly mined craft methods.
2. **Reference vs. Canon Packets (§4.69):**
   * Section 4 states: *"An unbound research packet may be retained as reference but cannot be imported as canon without a lore baseline and a new reviewed handoff."*
   * The staged entries are self-declared reference methods (`worldbuilding-setting-practice.md:15`: *"scope: a reference method for the culture-material partition. It records how practitioners specify and maintain a setting; it decides no culture's canon"*). They contain no packet envelope fields (`packet_id`, `baseline_bible_ref`, `artifact_manifest`, `dependency_manifest`).
3. **Bilateral Activation Status (§1.14-15):**
   * Section 1 states: *"Before the first transfer, both lanes read the whole file and record `lane, contract_id, revision, file_sha256, reader, read_at, evidence_pointer` in their own permitted records. Initial bilateral acknowledgement is pending until those records exist; writing this file is not a substitute for lore's read."*
   * `lore-shokunin/corpus/README.md:73, 79, 94` records coverage row `CM-g kotodama packet intake` as **uncovered**: *"contract `kotodama-lore-adjacency` sits at unacknowledged digest 5f4c02bf… and lore holds zero durable-surface acknowledgement records."*
   * Because lore has not acknowledged the contract, the interface is formally **unactivated**. No packet can be validly transmitted or received.

---

## 5. Contradictions Stated Explicitly (Never Smoothed)

1. **Active-Tone Handoff Section vs. Unactivated Contract:**
   * In staged `worldbuilding-setting-practice.md`, Section 6 is titled `§6 Coupling to the world bible — the handoff to lore-shokunin and what stays on this side`.
   * Stating a handoff section in active present tense creates a false impression that an operational conduit is currently flowing to lore.
   * *Contradiction:* Kotodama's entry text outlines a handoff path, while `lore-shokunin/corpus/README.md:79` confirms that CM-g is uncovered and contract digest `5f4c02bf...` is unacknowledged.
2. **Practitioner Delivery Schedule (S900) vs. Lore Frontier (CM-f):**
   * Staged `worldbuilding-setting-practice.amend-2026-10-23.md` mines S900 for the "delivery schedule" (releasing setting details gradually within ~20 chapters).
   * Meanwhile, `lore-shokunin` maintains `CM-f reveal (narrative) order vs chronology` on its active Frontier (`corpus/README.md:90`).
   * *Contradiction:* Both lanes now treat "order of disclosure to reader" as an explicit subject. If uncalibrated, an external observer or aggregator could view kotodama's adoption of S900 as an encroachment onto lore's CM-f frontier.
3. **Registry Ground Leg Blindness:**
   * Claim C's `ground` leg in `reports/round-74/claims.json:63-74` validates that `worldbuilding-setting*` and `設定ノート|世界観|世界观` do not exist within kotodama's own base tree (`corpus/knowledge/`).
   * That check confirms an in-lane gap, but is structurally blind to whether another fleet lane claims the ground. This connector scan provides the fleet-wide verification that no sibling holds this ground.

---

## 6. Proposed Move (One, Bounded)

**Append a bounded sibling-overlap and lore-boundary clarification to `corpus/lessons/round-74.md`** (the scribe-owned round lesson surface), capturing the provincial split, the CM-f distinction, and the handoff status.

### Proposed Text for `corpus/lessons/round-74.md`:

```markdown
### Sibling overlap and lore boundary (round-74 w1 connector scan)

- **Provincial split (kotodama vs lore):** The worldbuilding-setting-practice surface (adopting staged S883/S884/S899/S900 as lane rows S881–S884) is in-lane for kotodama under `PROVINCE.md:9` (culture-material generative craft). It records authorial practitioner methods: the four-layer worldview causal chain, setting-note table templates, SSOT authorial discipline, and premise-driven build order. Lore owns the fictional-world records, canon decisions, world-bible entities/relations/timeline, and consistency verification (`lore-shokunin/PROVINCE.md:3, 17-23, 28`). S884's note templates describe how an author drafts notes, not canon entity instances.
- **Reveal order vs delivery schedule (CM-f demarcation):** S900's delivery schedule (disclosing setting gradually within early chapters) is authorial narrative pacing advice. It does not encroach upon lore's CM-f frontier (`reveal order vs chronology`, `lore-shokunin/corpus/README.md:72, 90`), which governs mechanical verification of reader-revelation vs event ticks over world-bible records. Lore retains exclusive ownership of CM-f verification.
- **Contract activation and handoff status:** Admitting the worldbuilding-setting-practice entries creates NO handoff obligation to lore. Under `worldbible-integration-contract.md` §1.14-15, bilateral acknowledgement is pending (lore coverage CM-g uncovered; contract digest unacknowledged); under §8.1, transfers are pull-only based on a lore brief; and under §4.69, unbound reference methods do not constitute canon imports. No packet is owed or transmitted.
- **Fleet scan:** Word-boundary grep across all 20 sibling knowledge bases for worldview/worldbuilding/setting-note/世界観/世界观/設定ノート yields 0 matches. The surface is uncontested.
```

### Affected Axes:
* **Calibration (Ca):** Positively advances calibration by explicitly ledgering the boundary with lore, eliminating reading hazards regarding CM-f, and documenting that no phantom handoff obligation exists under `worldbible-integration-contract.md`.
* **Coverage (C):** Protects coverage by establishing the unambiguous provincial legitimacy of the two assimilated entries within kotodama's `culture-material/` partition.
* **Harms None:** Lands strictly on an append-only scribe surface (`corpus/lessons/round-74.md`), leaving the byte-exact entry pins (`entry-pins.txt`), scratch mirrors, and Ca's `APPENDONLY` baseline files (`LOG.md`, `SCORECARD.md`, `corpus/lessons/round-73.md`, `corpus/QUALITY.md`) completely untouched.

---

## 7. Risks and Containment

1. **Risk: Breaking Entry Hash Pins.**
   * *Mechanism:* Attempting to insert boundary caveats directly into `worldbuilding-setting-practice.md` or its amendment would alter their SHA-256 digests and fail Claim C's `pins` and `SCRATCHMIRROR` legs.
   * *Containment:* All boundary clarifications and handoff caveats must reside exclusively in the round lesson (`corpus/lessons/round-74.md`), leaving the assimilated entries byte-identical to their staged pins.
2. **Risk: Scribe Lesson Section Collisions.**
   * *Mechanism:* Interleaving connector findings into the scribe's `## Gate` or `## Mistakes` sections could corrupt structured parsers or verification sweeps.
   * *Containment:* The proposed text is self-contained and formatted for append-only placement at the end of the round lesson file.
3. **Risk: Stale Activation Assumptions.**
   * *Mechanism:* Lore could theoretically acknowledge `worldbible-integration-contract.md` in a concurrent round, making the "unactivated" status obsolete.
   * *Containment:* Lore's repository state was re-verified during this scan (Lore `LOG.md` and `corpus/README.md` have been unedited for 5+ days; CM-g remains uncovered). The note explicitly cites the evidence pointers so its rationale remains fully auditable.

---

## 8. Verification (for Main and Reviewer Seats)

1. **Sibling Knowledge Grep (Zero Collisions):**
   ```bash
   grep -riE 'worldview|world-view|worldbuilding|setting-note|世界観|世界观|設定ノート' \
     /home/vgpnk/Projects/shokunin/*-shokunin/corpus/knowledge/
   ```
   *Expected outcome:* 0 matches.
2. **Lore Frontier & Contract Intake Status:**
   ```bash
   grep -nE 'CM-[fg]|kotodama-lore-adjacency' /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/README.md
   ```
   *Expected outcome:* CM-f and CM-g both confirmed `uncovered`; contract digest unacknowledged.
3. **Provincial Boundaries Checked:**
   ```bash
   grep -n 'Adjacent contract' /home/vgpnk/Projects/shokunin/kotodama-shokunin/PROVINCE.md
   grep -n 'kotodama' /home/vgpnk/Projects/shokunin/lore-shokunin/PROVINCE.md
   ```
   *Expected outcome:* Verified against lines cited in Section 2.
4. **Append-Only Safety:**
   * Verify that no modifications touch `corpus/knowledge/culture-material/worldbuilding-setting-practice*.md`.
   * Verify that `git diff f7104cbce186bc2e1522abf0cfd619cc834628bb -- LOG.md SCORECARD.md corpus/QUALITY.md corpus/lessons/round-73.md` contains only append lines.

---

## 9. Tooling Record

* No tools installed, removed, or updated.
* `pacman` was not invoked (respecting the 2026-10-20 host-wide pause).
* All scans performed using built-in read and grep tools.
