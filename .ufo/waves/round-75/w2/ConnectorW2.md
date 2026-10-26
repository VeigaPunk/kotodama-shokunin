# ConnectorW2 — cross-claim pattern finder and sibling-overlap re-verification (round 75, wave 2)

Seat: ConnectorW2 (connector, leaf, no delegation). Lane: kotodama-shokunin. Base: f556d1049fe651d3d63975600b13acd9fb686f15.
Inputs read: wave 1 reports in `.ufo/waves/round-75/w1/` (42 files), `corpus/lessons/round-74-verifier-spotcheck.md`, `reports/round-75/claims.json`, `reports/round-75/ledger.json`, `.ufo/waves/round-75/counters/accept-c.py` (PART A, lines 1–510), `accept-ca.py`, the wave-2 parts in `.ufo/waves/round-75/w2/parts/`, the nine staged rows in `.ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md` (lines 840–848), the staged entries (validate mirror and `w2/stage`), the lore boundary (`lore-shokunin/PROVINCE.md`, `corpus/README.md`, `corpus/SOURCES.md`, `corpus/lessons/round-103.md`), and the shokuknow campaign pool (read-only).

**Grading hashes (moving target).** `reports/round-75/claims.json` changed twice during this seat (first read: no `pre_data_corrections`; then 16:53, FINAL with W2-F1/W2-F2 corrections; then 221 lines). Every instance below is pinned to `claims.json` sha256 `b7923cd6780ee54401140f2b33de0e56a1fdc26ec0e30383d8ef65cdb2d8c669`. Other hashes: `ledger.json` `a820f2117409a4e4a5c9f0b2b24511c85fd6e9d54d79b0159b3140e3518cc926` (163 lines, mtime 14:55, status still "DRAFT for wave 1"); `accept-c.py` `5e65ba73e88c422980f2bab1b78ee612540cd424c3d4a98af9969d9547bddc8a`; `w2/parts/leg-index.py` `ac7848f35955c38f2c53a1fa08c6de5fc3608a4d82b07ce68424fbd009a66a07`. Nothing in the lane tree is committed beyond base; the untracked round-75 files are the working tree.

## Verdict in brief

Five recurring patterns survive against the current bytes. Each has at least one live instance. Two are blocking for the freeze as written (P1 ownership gap, P5 mirror/stage drift on `used-by`). The rest are wording or scope defects with one-line fixes. Three checks were not triggered: seat-name collision, receipts printing forbidden strings (no receipts exist yet), and README partition-heading crossing (handled, but see P2).

The ledger's ten observe commands were re-run at base and reproduce their stated observed tokens (808; 32; 40; 247; 713; 58; 37; present; present; 44). Ledger stated_at lines SHONEN.md:6, README.md:344/407/813, lesson round-74.md:37/38, LOG.md:4318 exist at base with the quoted text.

---

## P1 — Prose promises a write that the claim's ownership denies (ledger prose vs claim ownership)

**Instances (current bytes):**
- `reports/round-75/ledger.json:29` (L75-01 `why`): "claim C later appends nine rows and updates the same line to the final 817, which is separately checked by claim C." This assigns SHONEN.md:6 to claim C.
- `reports/round-75/claims.json:11` (W2-F1): "C INDEX no longer grades SHONEN.md:6 (Ca-owned); Ca `after` states the Ca-alone tuple 808/713/58/37 and the combined 817/722/58/37 expectation".
- `reports/round-75/claims.json:155` (C `owned_inplace`): lists only `corpus/README.md:376`. SHONEN.md is not in C's owned set.
- `reports/round-75/claims.json:41` (C `after`): "Registry 808 -> 817 rows" with the SHONEN line described as checked without Ca.
- `reports/round-75/claims.json` (Ca `after`, the 'combined revision; claim C never grades SHONEN' clause): so the combined 817 SHONEN figure has no grading owner and no writer.

Net: the ledger assigns the 817 write to C; the claims say C never touches SHONEN; Ca lands 808. At the combined tree SHONEN.md:6 reads 808 and nothing is expected to change it, yet Ca's after-text names 817 as the combined expectation.

**Smallest fix (pick one; (a) is minimal):**
- (a) Drop the 817 SHONEN expectation from Ca's combined tuple (SHONEN stays at Ca's 808; state the combined registry total only in C's `after`), and rewrite `ledger.json:29` to say "SHONEN.md:6 reflects the registry at Ca's landing (808); claim C does not write it." The ledger is frozen with the claims, so both edits belong in the same freeze commit.
- (b) Add `{"path": "SHONEN.md", "base_line": 6, ...}` to C's `owned_inplace` and a C INDEX/REPAIR-style leg. This contradicts W2-F1, so only if the L1 wants the 817 write back in C.

**Secondary (same pattern, lower risk):** `ledger.json:6` status says "DRAFT for wave 1" while `claims.json:3` says "FINAL — ... frozen by the commit". Update the ledger status string in the freeze commit.

---

## P2 — Counter wording stricter or weaker than the claim text

**Instances:**
- `.ufo/waves/round-75/w2/parts/leg-index.py:22`: "its four index-gap rows; both are exempt". The index-gap set is two, not four. Recomputed by basename under `LC_ALL=C`: files with no README index row at base are `culture-material/heritage-taxonomy-models.md` and `culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md`; no ghost rows. `ledger.json:73` (L75-04) and `claims.json` W2-F2 both say the right count in prose.
- `.ufo/waves/round-75/w2/parts/leg-index.py:262–263`: exempts any README row whose basename is in `base_knowledge` (any knowledge file that exists at base). The claim text (`claims.json:149`, INDEX leg) exempts only "index rows naming a knowledge file that exists at base (claim Ca's index-gap rows)", which in intent is the two heritage rows. As coded, a new duplicate or unrelated row for any existing base file (e.g. a second `trickster.md` row) passes the INDEX leg. The leg is weaker than its text.
- `.ufo/waves/round-75/counters/accept-c.py:5–6` (module docstring): "eight adopted rows (S885..S892), two entries under corpus/knowledge/myth-symbol/". The frozen claim is nine rows (S885..S893) and three entries (`claims.json` C `row_set`, `entries`). The docstring is stale; code reads the frozen config, so this is wording, not grading.
- `accept-c.py:64–71` (H4 INDEX): describes the exemption as "claim Ca's pairs L75-02 / L75-03" for heading parentheticals. This matches `leg-index.py:257–259`, which exempts partition-heading lines only when the base section name is present. Consistent; no defect beyond the broader row exemption above.

**Smallest fix:**
- `leg-index.py:262–263`: exempt only the two basenames frozen in the claim (frozen list in `claims.json` C INDEX text), not any base knowledge file.
- `leg-index.py:22`: "four" → "two".
- `accept-c.py:5–6`: "eight adopted rows (S885..S892), two entries" → "nine adopted rows (S885..S893), three entries".

---

## P3 — Campaign-namespace ids vs lane ids (same number, different documents)

**Base lane rows that share a staged number (base `corpus/SOURCES.md`):**
- S864 (line 819) UNESCO ICH, Carnival of Oruro; S865 (820) UNESCO ICH, Flamenco; S866 (821) UNESCO ICH, Talchum; S870 (825) ICKL, Labanotation; S876 (831) Enguehard, conlang teaching.
- Claim C's staged ids (`claims.json` row_set: S876, S864, S865, S866, S870, S885, S902, S904, S905, S917, S919, S921) are campaign-pool numbers. Several collide with live lane rows at base (S864, S865, S866, S870, S876). Claim C does not adopt these numbers, so the ROWS leg is unaffected. The by-document renumber map resolves S876→S885 and S870→S893.
- The campaign pool itself reuses S885–S893 for other documents. `merge/kotodama/SOURCES.append.md:33–41`: S885 is Barthes (same document as the lane's S885); S886 苗字 (Kotobank), S887 平安時代, S888 現代日本人名大辞典, S889 日本人名大辞典, S890 Kałużyńska, S891 Zhao et al., S892 Новиков (lane S892 is Marrone), S893 Костюхин (lane S893 is 三九音域). Only S885 and the S870-essay coincide by document.

**Sibling-report defect (ConnectorSiblings.md §4, line 62):** "S729 (round 1) = S761 = S787 = S870 (same URL and title)".
- Base lane S729 (line 684), S761 (717), S787 (741) are three different documents (Neer et al. infant speech; Hudson Museum ballgame; Koiso fragrance). The campaign pool file that names S729 is `.ufo/scopes/corpus-expansion-1/ScoutKotodama.md:87` (世界观 practitioner term), a different numbering space.
- The S870 part of the equivalence holds: campaign `SOURCES.append.md:18` S870 and the lane's staged S870 are the same 三九音域 essay URL. The S761/S787 part is unsupported: no `^| S(729|761|787) ` row in `SOURCES.append.md`.

**Smallest fix:** the freeze keys rows by document (already the stated plan). Add S864, S865, S866, S870 and S876 to the COLLCHECK leg's named base-collision set (the reg-ids guard fires on them, but the leg text does not name them). Correct the sibling report's §4 equivalence to "S870 only".

---

## P4 — One located quote per row vs multi-page documents (page cites outrun the evidence window)

**Instances:**
- S885 (staged row `validate/corpus/SOURCES.md:840`): anchor is article p. 1, quote «Innombrables sont les récits du monde.» The `teaches` cell cites transcription pages p. 5, p. 6, p. 11. The counter checks only the Gate quote in one window (`claims.json` EVIDENCE leg), not the page cites. Entry `narrative-structure-frameworks.amend-2026-10-23.md:4` cites S885 "p. 5".
- S892 (`validate/corpus/SOURCES.md:847`): anchor is "PDF p. 7 of 25", quote «Mais combien, et de quelle nature, sont ces codes ?». The entry `narrative-structure-frameworks.amend-2026-10-23.md:12` cites the same quote as "p. 58". The row gives PDF pagination of a 25-page capture; the entry gives printed pagination (article 57–72). The two systems are not reconciled in either place. [INFERENCE: if PDF p. 7 corresponds to printed p. 58 the offset is 51 and both are right; the offset is not written down anywhere in the round.]

**Smallest fix:** state the page system in each cite (for S892: "PDF p. 7 of 25 = printed p. 58" if the offset is verified against the capture; otherwise pick one). For S885/S886/S887 cite the anchor page in the entry and name the transcription pages as "read on" pages, or split the row. No change to the frozen counter is needed.

---

## P5 — Mirror vs stage drift on the entry set and `used-by` (kill-rule failure)

This is the only pattern that breaks a frozen kill rule as the tree stands.

**Evidence:**
- `claims.json` C `entries` lists three paths including `narrative-structure-frameworks.amend-2026-10-23b.md`. The validate mirror (`.ufo/waves/round-75/assimilation/validate/corpus/knowledge/myth-symbol/`) contains only `narrative-structure-frameworks.md` and `narrative-structure-frameworks.amend-2026-10-23.md`. The 23b file exists only in `w2/stage/corpus/knowledge/myth-symbol/` and `drafts/`.
- Source lines per file:
  - validate `amend-2026-10-23.md`: S885 S886 S887 **S891 S892**.
  - stage `amend-2026-10-23.md`: S885 S886 S887.
  - stage `amend-2026-10-23b.md`: S885 **S891 S892**.
  - `narrative-structure-frameworks.md` (validate and stage): S885 S888 S889 S890 S893 (identical).
- `used-by` in validate `SOURCES.md`: S885 (line 840) lists `amend-2026-10-23.md` and `narrative-structure-frameworks.md`, missing the 23b entry that cites it in stage. S891 (846) and S892 (847) list `amend-2026-10-23.md` only; the stage cites them only in 23b.
- Kill rule (`claims.json` C `kill_rule`): "used-by not exactly the citing entries" fails the claim. On the current bytes, S885, S891 and S892 fail it under either tree.

**Smallest fix:** choose one canonical entry set and regenerate both the validate mirror and the stage from it: either (a) move S891/S892 into `amend-2026-10-23b.md` in the validate mirror and add the 23b file there, and set S885/S891/S892 `used-by` to exactly the citing set; or (b) drop the 23b entry and the S891/S892 cites, which makes `claims.json` C `entries` and the claims rejects text ("folded into the admitted amend-2026-10-23b entry") both wrong. (a) matches the claim text. Re-run the used-by check before freezing.

---

## Not triggered (checked, clean)

- **Seat-name collision.** `ConnectorW2` appears in `w2/dispatch.json` (3 times), `w2/spec.json`, `w2/swarm-registry.json`, and wave-2 build files. The dispatch has 34 names and no duplicates. No `ConnectorW2` in `.ufo/waves/round-74/w2/`.
- **Receipts printing forbidden strings.** No round-75 receipts exist yet: `reports/round-75/telemetry/` is empty and `reports/round-75/evidence/` does not exist. Forbidden-token lists appear as text in `claims.json` (C leg NOSTUB, Ca leg ENTRIES) and in `accept-ca.py:2756–2757`, which is leg text, not receipt output. Recheck when receipts land.
- **README partition-heading crossing.** Claim C owns `corpus/README.md:376` (`## myth-symbol/ (29)` → `(32)`); claim Ca owns `:344` and `:407`. The H4 exemption covers Ca's parentheticals. The residual defect is P2's broad row exemption.

---

## Sibling-overlap duty: ConnectorSiblings.md re-verified against lore

Verdict re-check: **CONTESTED with lore-shokunin, narrow — stands, and understated for time axes.** Details:

**Confirmed (current lore bytes):**
- `lore-shokunin/PROVINCE.md:19`: "CM-f reveal order vs chronology … stay `uncovered`". Matches (sibling quoted it with an ellipsis).
- `lore-shokunin/PROVINCE.md:23` (Frontier): reveal order vs chronology; knowledge/memory state; ConStory-Bench crosswalk. Confirmed.
- `lore-shokunin/corpus/README.md:72` (CM-f row), `:78` ("the schema encodes integer ticks only … zero durable-surface hits"), `:90` ("define a non-tick reveal-order field or a per-cluster narrative-order map"), `:92` (character knowledge/memory state over time), `:93` (ConStory-Bench crosswalk). All confirmed.
- `lore-shokunin/corpus/SOURCES.md:18–20`: S010, S011, S012 all `queued`. Confirmed.
- `lore-shokunin/corpus/lessons/round-103.md:52`: S015, S016, S017 rejected. Confirmed (S017 is the ConStory-Checker LLM-judge row).
- `shokuknow/.ufo/scopes/corpus-expansion-1/ScoutLore.md:19` (S033 → CM-f), `:26–29` (S040, S041, S043 → character knowledge state), `:38` (proposed `corpus/knowledge/narrative-order-and-chronology.md`), `:40` (character-knowledge-state entry), `:46–57` (discourse vs chronology argument). All confirmed.
- `lore-art.md` (sibling cites `.ufo/waves/kaika-w1/lore-art.md:18–19, :45–49, :57`) lives at the **fleet root** `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika-w1/lore-art.md`, not inside the lore repo. Lines match. Path should be stated as fleet-root-relative.
- Shokuknow campaign narrative entry scope line (sibling §2 quote, "decides no culture's story (lore-shokunin owns canon)"): confirmed in both the campaign copy and the lane's staged copy (line 29).

**Corrections and new findings:**
1. **The sibling quoted §6 and §9 from the campaign copy, not the lane's staged entry.** Campaign `narrative-structure-frameworks.md:50` ("§6 A three-layer spec format … the format a world bible can actually store") and `:53` ("§9 Coupling to the world bible"). The lane's staged entry has neither phrase: its §6 is "Calibration limits" (stage line 46) and it has no §9. The lane's risk is at stage line 40 (§3, 三层 description format ストーリー / クエスト / シーン); I did not read that paragraph in full [INFERENCE: whether it proposes a storage shape is unverified].
2. **Time-axis overlap is stronger than the sibling said.** The lane's staged topic (stage line 39) names "the three time axes 次序 / 时长 / 频率". Lore's CM-f cites S044 for the Chinese triad 时序/时距/频率 (`ScoutLore.md:46–57`). Same Genette triad, different Chinese terms. This is the concept lore calls reveal-order-vs-chronology, so the overlap is on the axis set itself, not only on the story/discourse distinction.
3. **The required guard is absent.** The sibling's §6/§7.3 recommendation (a scope line stating the entry supplies no reveal-order schema, no knowledge-state gate and no canon ruling, pointing to CM-f) is not in either staged entry. Grep for `reveal|schema|knowledge state|CM-|gate` returns 0 hits in both. Smallest fix: add one scope line to `narrative-structure-frameworks.md` (line 29 area) with the pointer to `lore-shokunin/corpus/README.md` CM-f and `PROVINCE.md:19,23`.
4. **Claim C BEFORE text: already corrected.** The sibling's §3 defect ("neither names a structuralist narrative source", `claims.json`) no longer appears in current claims (grep returns 0). The current BEFORE cites `comparative-frameworks.md` as already citing Greimas/Propp. Resolved; no action.
5. **Other sibling secondaries not re-verified.** kengaku, chousa, game-dev-2d/3d, audio, revenger, kotoba: I read the sibling's quotes only for lore. Those claims were not re-checked here.

Lore boundary contract: the table in ConnectorSiblings.md §6 is still the right split for the integrator; it is not ruled here (no entry decides canon).

---

## Summary table

| # | Pattern | Live instances (path:line) | Blocking? | Smallest fix |
|---|---|---|---|---|
| P1 | Prose promises a write the claim denies | ledger.json:29; claims.json:11, :41, :155; Ca after (combined 817) | Yes (SHONEN 817 has no writer) | Drop 817 SHONEN from Ca combined tuple; rewrite ledger:29; ledger status string |
| P2 | Counter wording stricter/weaker than claim | leg-index.py:22 ("four"), :262–263 (broad exemption); accept-c.py:5–6 ("eight"/"two") | Weaker-than-claim: yes for :262; others wording | Restrict exemption to the two frozen basenames; fix "four"→"two"; fix docstring |
| P3 | Campaign id vs lane id (same number, other document) | SOURCES.md:819–821, 825, 831 (base lane); SOURCES.append.md:33–41; sibling §4 line 62 | No (ROWS unaffected); sibling claim wrong | COLLCHECK names S864/S865/S866/S870/S876; correct sibling §4 to "S870 only" |
| P4 | One window vs multi-page page cites | validate SOURCES.md:840 (S885), :847 (S892); amend-2026-10-23.md:4, :12 | No (quote check passes); page cites inconsistent | State page system per cite; confirm PDF-to-printed offset for S892 |
| P5 | Mirror vs stage drift on entries and used-by | validate/…/myth-symbol/ (no 23b); validate SOURCES.md:840, :846, :847; stage amend-2026-10-23b.md | Yes (used-by kill rule fails) | Regenerate validate mirror and used-by from one entry set; re-check |

## Evidence scope and limits

- Read-only throughout. No writes to the fleet root, sibling lanes, shokuknow, the lane's git or index, the lane's claims/ledger/counters, or the round-75 assimilation tree. No staged or part files were written by this seat (the item named only this report).
- Source documents were not fetched; no source-content claims are made here. Page-number statements rely on the committed rows and entry text.
- The claims file changed during the seat (16:53 and again before the final pin). The hash above is the one graded. If `claims.json` changes again, re-run P1 and P2 against the new bytes.
- Install record: none. No tools installed or updated.
- Scratch `/fast/scratch/hyaku/kotodama-r75/ConnectorW2/` holds only read-only snapshots and throwaway probes; it is removed before yield. No receipts were copied to the wave dir (the receipts are the inline command outputs summarized above).

Checks for the main agent to run after the freeze: `python3 -B reports/round-75/accept-c.py` and `accept-ca.py` at the staged lands; a used-by exact-match check on `SOURCES.md:840–848`; `comm` on the README index against `corpus/knowledge/*.md` basenames (expects gap = the two heritage-taxonomy files).
