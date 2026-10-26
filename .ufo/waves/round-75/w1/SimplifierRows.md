# SimplifierRows — minimality attack on claim C's row set and entry set (round 75, wave 1)

Seat: SimplifierRows (simplifier, leaf). Lane base `f556d1049fe651d3d63975600b13acd9fb686f15`.
Read only: `reports/round-75/claims.json`, `reports/round-75/ledger.json` (DRAFT, not edited), the staged package at
`/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/myth-symbol/narrative-structure-frameworks*.md`
(5 files), the two entry drafts under `.ufo/waves/round-75/drafts/`, the wave-1 scout and scribe reports, and the
round-74 counter `reports/round-74/accept-c.py` (the leg implementations the round-75 counter will be built from).
No network fetch. No installs. Scratch `/fast/scratch/hyaku/kotodama-r75/SimplifierRows/` used for one word-count
run and removed before yield. No lane file, registry, index, lesson or claim was modified.

Every leg citation below is a line in `reports/round-74/accept-c.py`, read as the template for round 75.

## 1. Verdict

| Question | Answer |
|---|---|
| Rows honestly needed | **9** — `S885`..`S893`, contiguous, one row per document |
| Entries honestly needed | **3** — base, `amend-2026-10-23`, and the combined amendment (23b+23c+2026-10-24) |
| Rows in the DRAFT row_set | 8 (`S885`..`S892`) — one short, and internally orphaned as drafted |
| Rows that may carry the Barthes 1966 article | **1** (`S885`) |
| Distinct staged claims covered | 14 of 19; 3 deferred with a flip, 2 cut as false/stale |
| Orphan rows the counter will *not* catch | `S891`, `S892` (see §2.8) |

The DRAFT is one row short, not one row long. The row count is forced by three things the scouts have now settled
and by one mechanical rule the DRAFT does not state.

## 2. Row by row — does a drafted entry sentence need it?

Citing sentences are from `.ufo/waves/round-75/drafts/narrative-structure-frameworks.md` (base, 21,705 B) and
`.ufo/waves/round-75/drafts/narrative-structure-frameworks.amend-2026-10-23.md` (amendment, 11,308 B).

| Row | Document | Needed? | Citing sentence (draft) | Scout verdict | Consequence if kept / dropped |
|---|---|---|---|---|---|
| S885 | persee `…_8_1_1113` (Barthes 1966) | **yes** | base §1 "narrative is a formal object … levels of description"; amend §3 (p. 5 quotes, p. 26 quotes) | ScoutPersee1113 still running | Keep. One row, one window — see §4. |
| S886 | persee `…_8_1_1120` (Todorov) | **yes** | amend §1 (three categories, temporal deformation, pp. 139–141) | ADMIT (`ScoutPersee1120.md:5`) | Keep. |
| S887 | persee `…_8_1_1114` (Greimas) | **yes** | amend §2 (two isotopies, two readings, pp. 29–31) | ADMIT (`ScoutPersee1114.md:5`) | Keep; anchor must reach p. 31, not p. 29–30 alone. |
| S888 | `jw.ucass.edu.cn/…/xushixue.pdf` | **yes** | base §3, §4, §5, §7, §12 | ADMIT; all four syllabus claims locate (`ScoutUcass.md:5,30-40`) | Keep. Wording must follow the scout: 三个维度 not "axes"; 查特曼的六种参与者 not "grid". |
| S889 | jstage jcss 25(2) 25_200 | **yes, conditional** | base §8 (three-layer format — **wrong row**) and §9 (generation side — **right row**) | **REFUSE as staged**, flip to ADMIT on the anchor correction (`ScoutJstageJcss.md:84`) | Keep only with the corrected locator (`1. まえがき` / English abstract / §4.1). Its own row carries the generation side; the three-layer format is S890's. |
| S890 | jstage jsik 32(2) 32_2022_017 | **yes, conditional** | base §8 (three-layer format — **right row**), §6 if 起承転結 lives there | ScoutJstageJsik still running | Keep on ADMIT. If it refuses, §8's three-layer format has **no row** → cut §8, and S890 drops to 8 rows. |
| S891 | unige S/Z excerpt | **yes, only if the combined amendment is adopted** | none in the two frozen entries; the five codes are the amendment's only source | ADMIT via an ordinary Wayback capture; live page met a bot challenge, not passed (`ScoutUnigeSZ.md:5,40-44`) | Keep. Without it the lane's five-code enumeration stays open a fourth round. |
| S892 | iris.unipa.it Marrone (wayback PDF) | **yes, only if the combined amendment is adopted** | none in the two frozen entries | ADMIT; both origin claims locate on printed p. 58 (`ScoutUnipaWayback.md:23,46`) | Keep. It is the only document that states the five-codes/levels relation. |
| S893 | chinawriter 2023 (三九音域) | **yes** | base §10, §12 (世界观 vocabulary) | **ADMIT**; the heading locates, `世界观是打开小说幻想屋的钥匙`, 14 chars (`ScoutChinawriter2023.md:3,36`) | Keep. The round-72 refusal's flip condition is met; leaving it refused now would be a false refusal. |

### 2.1 The contiguity coupling the DRAFT misses

`leg_rows` requires the added ids to be contiguous and to start above the base's last id
(`accept-c.py:820-822`). With `S893` admitted, the added block is `S885..S893`. Dropping `S891`/`S892` while
keeping `S893` yields `S885..S890, S893` — **non-contiguous → ROWS FAILS**. So the chinawriter row is
mechanically coupled to the two amendment rows:

- adopt all three (9 rows), **or**
- refuse chinawriter and renumber it away (7 rows `S885..S891`), **or**
- renumber chinawriter to `S891` (7 rows, contiguous) — which requires editing the frozen entry text and the
  seat prompts that already say `S893`.

Since every one of the three documents opened this round, the 9-row block is the only honest member of that set.

### 2.2 `S891`/`S892` are orphans in the DRAFT as written — and the counter will not say so

`claims.json.claims[C].entries` lists **two** paths. `_entry_citations` iterates only `cfg["entries"]`
(`accept-c.py:732-741`), so a row cited by no configured entry gets `want_used = set()`, and `row_usedby` on a
dash cell also returns `set()` — the equality at `accept-c.py:915` **passes**. Two rows could therefore be
appended with an empty `used-by` and every leg green. That is a registry row claiming coverage no entry delivers:
counter-legal, contract-illegal (SOURCES: `used-by` names the citing paths). The only thing that catches it is a
reviewer, so the fix belongs in the freeze, not in the counter.

### 2.3 The DRAFT `entries` list is also one short

The dispatched `ScribeEntryAmend` task writes a **third** entry,
`narrative-structure-frameworks.amend-2026-10-23b.md` (dispatch.json, `taskCall.tasks[ScribeEntryAmend]`:
"draft a combined second amendment at …amend-2026-10-23b.md ONLY if the scouts confirm the documents").
`claims.json.entries` does not name it, and `claims.json`'s `after` clause counts `249 + (number of frozen
entries)`. Freeze must add the path or the entry lands outside the graded set (no `ENTRIES` shape check, no
`REPOINTED` check, no index row requirement, and a live file count the INDEX footer must still match).

## 3. Staged amendment files — duplicate, distinct, or contradictory

| File | Rows | Verdict against the base entry and each other |
|---|---|---|
| `amend-2026-10-23` | S885, S886, S887 | **Adopt.** Distinct on all three documents. Its §N+3 ("the five-code enumeration is still not recovered") becomes **stale the moment 23b lands** — replace with a pointer, do not keep both. |
| `amend-2026-10-23b` | S891 | **Adopt in reduced form.** §N (the five codes) is distinct and closes a gap open since round 3. §N+1 ("the 1966 article's own four levels — fonctions, actions, indices, informants") is **false and self-contradicting within the family**: `amend-2026-10-23c` places indices/informants *inside* the functional level, and `amend-2026-10-24` quotes the article naming *three* levels. Cut §N+1 entirely. The scout adds a second correction: the page's names are French (`herméneutique`, `sémique`, `symbolique`, `proaïrétique`, `gnomique`) — the staged English "semantic/cultural" is a gloss, not the page's words. |
| `amend-2026-10-23c` | S885 (p. 11) | **Refuse with flip.** Its claim (noyaux/catalyses/indices/informants) is distinct, but it needs a *second* page of the document `S885` already owns, and one row carries one evidence window (§4). Flip: re-point `S885`'s window to p. 11 in a later round and re-quote; the four classes stay queued, not asserted. |
| `amend-2026-10-24` | S892, S885 (p. 6) | **Adopt in reduced form.** §N+1 (Marrone) is distinct, locatable, and is the round's calibration payload. §N (the article's own three-level list, p. 6) needs a second page of `S885` → same one-window conflict as 23c. §N+2 ("the four-level formulation is not the article's own list") is a *conclusion from* §N and cannot stand once §N is deferred. Keep §N+1; defer §N and §N+2 with the same flip. |

Duplication that survives all cuts:

- **"Two readings" is stated twice from two documents.** Barthes p. 26 (`la dystaxie oriente une lecture
  « horizontale » … une lecture « verticale »`) and Greimas p. 30 (`deux lectures différentes, l'une sur le plan
  discursif, l'autre, sur le plan structural`). Both drafts quote both. This is one proposition; Greimas's is the
  one whose page is the row's evidence window, and Barthes's is the one the one-window rule cannot carry. **Cut
  the Barthes p. 26 quotes**, keep Greimas's, and let §4 of the amendment state the contrast as the file's
  reading. That removes a duplicate *and* resolves the `S885` window conflict in one move.
- **The premise is stated twice.** Base §1 (notice + opening paragraph, tier B) and amend §3 (p. 5, method grade)
  assert the same "levels of description" claim. Keep one quoted: the amendment's. Base §1 becomes a
  paraphrase-with-locator or a pointer (§5 below).

## 4. How many rows may honestly carry the Barthes article: one

The four staged ids are one document (`comm_0588-8018_1966_num_8_1_1113`): `S876` (notice), `S885` (p. 5/p. 26),
`S917` (p. 11), `S921` (p. 6). The row's identity in this registry is the document, so **one row** — and the DRAFT
gets this right. What the DRAFT does not state is the two mechanical consequences, both of which bite:

1. **Every page-level URL must appear in the row's source cell.** `norm_url` keys on `(netloc, path)`
   (`accept-c.py:235-239`), so `…/doc/page/…_T1_0011_0000` and `…/doc/…_1113` are different keys. `REPOINTED`
   requires every URL in a `source:` line to be in the row's URL keys (`accept-c.py:1060-1066`), and `EVIDENCE`
   requires the evidence file's `fetch:` line to name the row URL (`accept-c.py:1193`). If an entry cites a
   page-level URL and the source cell carries only the doc URL, **REPOINTED fails**. If the capture fetches a
   page-level URL and the source cell carries only the doc URL, **EVIDENCE fails**.
   → `S885`'s source cell must carry the doc URL plus every page-level URL used, and the by-document map must
   record each staged id with its own URL (the map's URL is checked verbatim against the source cell at
   `accept-c.py:930`).
2. **One row = one evidence file = one fetch = one page.** `_evidence` reads exactly
   `reports/round-75/evidence/<id>.txt` (`accept-c.py:694-720`), and each persee page-level URL serves one page
   per request (`ScoutPersee1120.md:12-40`: HTTP 200, 3,939 bytes for p. 139). The article PDF is behind an
   altcha wall and is not openable by ordinary means (`ScoutPersee1120.md:45-59`). `excerpt` has a floor of
   4,096 characters and **no ceiling** (`accept-c.py:1214-1228`), so a long window is allowed — but a window is
   one fetch's text, and no single ordinary fetch returns pp. 5, 6, 11 and 26.
   → **At most one page's quotes can be committed.** The other pages' quotes locate (the scouts read them) but
   are not in the stored window, so they rest on a Gate record that evidences a different page.

**Which page gets the window.** Take the page whose quote carries the most claims no other row can carry, and
which the round's correction depends on:

- p. 5 — levels of description, no level alone, horizontal/vertical reading (amend §3; base §1's premise).
- p. 26 — two readings, double membership (duplicates Greimas p. 30 → cut, §3).
- p. 6 — the article's own three-level list (supports the 2026-10-24 correction).
- p. 11 — the four classes of the functional level (23c).

**Recommendation: p. 5.** It carries the amendment's core and the base entry's premise; p. 26 is a duplicate;
p. 6 and p. 11 each carry one deferred claim. The row's `scope` cell then reads p. 5 (plus the notice for
metadata), and the flip for the deferred pages is a one-line re-point of the same row in a later round.

If the L1 prefers p. 6 (the correction's linchpin) or p. 11 (the plot-spec vocabulary) instead, the arithmetic is
the same: exactly one page is quoted, the other two claims defer, and the Barthes p. 26 quotes are cut either way.

## 5. The opposite test — sentences left without a row

The base draft is honest about most of this (`loc: PENDING` on 26 lines), but four sentences cite a source for
something the source does not say. Each is a review-level defect the counter cannot see (REPOINTED checks only
that the id resolves to a row whose URL matches).

| Sentence | Problem | Fix |
|---|---|---|
| base §1 "The route is an admission question … a transcription reached through an access control is not an opened source (S885)" | cites S885 for a QUALITY-10 rule the source cannot state | drop the id; keep the sentence as method text |
| base §4 "…it is a vocabulary for a culture's roles that is not a moral one (S888)" | the scout says the syllabus only *schedules* 行动元 under 第三讲 and does not explain it (`ScoutUcass.md:34`) | keep "schedules 行动元 under its actant lecture" as the S888 claim; mark the moral-vocabulary point as this file's reading, id-free |
| base §5 "three time axes … (S888)" and §7 "查特曼's participant grid (S888)" | the page says 三个维度 and 六种参与者; "axes"/"grid" are the file's glosses | use the page's terms; keep the glosses id-free (the draft already marks the glosses pending — extend that to the id) |
| base §6 "起承転結 as a completable minimal unit (S889)" | neither located section of the jcss paper names 起承転結 (`ScoutJstageJcss.md:36` lists まえがき, 物語とは何か, 物語生成システム, 物語生成の物語論のための構図, 4.1, あとがき) | if ScoutJstageJsik does not locate the term either, **cut §6** — it is a staged claim with no row, and the draft itself says it moves or is struck |
| base §8 "three-layer … ストーリー/クエスト/シーン (S889)" and §9 "narrative generation (S890)" | **swapped**. The jcss paper *is* the narrative-generation/post-narratology paper; `クエスト`/`シーン` are absent from it and belong to the jsik paper (`ScoutJstageJcss.md:36,44`) | swap the ids: three-layer format → S890, generation side → S889 |

The swap does not change the row count — both rows are still needed — but it is a wrong-document citation that no
leg catches, and it is the one place where the draft's claim set and the row set disagree in *content* rather
than in *number*.

## 6. Cuts, each with the kill-rule consequence

| # | Cut | If not cut |
|---|---|---|
| 1 | Base §10, its §12 line, and the `S893` source line **unless** the freeze adds `S893` | `REPOINTED` FAILS twice (`accept-c.py:1049-1050` id outside `allowed_ids`; `:1067-1068` inline id; `:1070` forbidden id) and `ROWS` FAILS once (`accept-c.py:886`). Two legs, one cut. |
| 2 | `S891` + `S892` if the third entry is refused | Nothing fires — the rows pass with an empty `used-by` (§2.2). That is the trap: the counter is green and the registry claims coverage no entry delivers. |
| 3 | 23b §N+1 ("the article's own four levels") | The corpus asserts a list the article does not print, contradicted by 23c's own subclassing and by Marrone's attributed "quatre niveaux … fonctions, actions, indices et informants" (`ScoutUnipaWayback.md:23`). This is the round-74 "staged quote adopted that does not locate" class, at the level of a claim rather than a string. |
| 4 | amend-23 §N+3 ("five codes still not recovered") once 23b lands | Two entries disagree about the state of the same question; the REJECTS/Gate narrative has to carry the flip anyway. |
| 5 | Barthes p. 26 quotes (two readings, double membership) | Duplicate of Greimas p. 30–31, and outside `S885`'s single window → the entry quotes a span the committed evidence does not contain. |
| 6 | 23c (p. 11) and 2026-10-24 §N/§N+2 (p. 6), deferred with flip | Same window conflict. Counter-legal if the Gate quote is p. 5; review-illegal, because the quoted span is not in the stored window. |
| 7 | 23b's English code labels ("semantic", "cultural") | The page says `sémique` and `gnomique`; the English is a gloss and the scout says so explicitly (`ScoutUnigeSZ.md:44`). |
| 8 | Base §6 (起承転結) if no row locates it | An uncited staged claim; the draft's own rule ("a claim the Gate cannot place is struck rather than softened") makes keeping it a self-contradiction. |

## 7. The smallest honest set

**Rows: 9** (`S885`..`S893`, contiguous). **Entries: 3.**

| Entry | Rows cited | Distinct claims |
|---|---|---|
| `myth-symbol/narrative-structure-frameworks.md` | S888, S889, S890, S893 | story/discourse split; actantial notation as scheduled; three time dimensions; focalisation + Chatman's six participants; 起承転結 (conditional); three-layer format; hierarchical description; narrative generation; 世界观 vocabulary |
| `…amend-2026-10-23.md` | S885, S886, S887 | Barthes levels of description (p. 5); Todorov's three categories and temporal deformation; Greimas's two isotopies and the equivalence to establish |
| `…amend-2026-10-23b.md` (combined) | S885, S891, S892 | the five codes in the page's French names; Marrone's partial-reformulation relation and the proairetic synthesis |

That is 14 distinct claims over 9 rows and 3 files. The two smaller packages both cost more than they save:

- **2 entries / 8 rows** (the DRAFT as written): `S891`/`S892` orphaned, the third entry written but ungraded, the
  five-code gap open a fourth round, and a registry that claims two sources nothing cites.
- **2 entries / 6 rows** (drop `S891`/`S892` and refuse chinawriter): non-contiguous only if `S893` stays; with
  `S893` gone it is coherent, but it refuses a document that opened and loses the round's only calibration
  payload. It is the honest fallback **only** if `S891` or `S892` fails to open.

Cost note for the third entry: `ENTRIES` requires a body of at least 478 words from the first `## `
(`accept-c.py:746-792`; floor = 478, the smallest knowledge file at base). The staged 23b (366 words total) and
23c (324) and 2026-10-24 (512) each fail that shape as staged — which is a second, independent reason the four
files must land as **one** combined amendment rather than four entries.

## 8. What is still open, and what flips the answer

| Pending | Flips |
|---|---|
| `ScoutPersee1113` | which page can be `S885`'s window; whether the page-level service is usable for 1113 at all (if it is gated, the amendment's Barthes section is refused and `S885` keeps only the notice — the base entry then owns `S885`) |
| `ScoutJstageJsik` | `S890` admission; whether 起承転結 has any row (§5, cut 8); the §8/§9 swap's target |
| Freeze decisions the L1 must make | (a) `entries` 2 → 3; (b) `row_set` 8 → 9 with `S893`; (c) `REPOINTED`'s forbidden-id text — the DRAFT says "staged ids `S864..S876` and `S885..S921` appear in neither entry as lane rows", which forbids the lane ids `S885..S893` themselves; the round-74 counter derives `forbidden_ids = staged_ids - lane_ids` (`accept-c.py:649`), so the prose and the implementation disagree on the face of the frozen text. Replace the range with the explicit set (`S864, S865, S866, S870, S876, S902, S904, S905, S917, S919, S921`) minus any adopted lane id — noting `S885` is both staged and lane (identity mapping) and must not be forbidden. |

## 9. Nothing installed, nothing left behind

No tool install or upgrade (nothing needed; `git`, `python3`, `wc` sufficed). No network request. Scratch
`/fast/scratch/hyaku/kotodama-r75/SimplifierRows/` removed. No file outside this report was written.
