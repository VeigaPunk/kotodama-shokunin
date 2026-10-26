# CritTrendObservables2 — pre-file attack on the round-75 trend verdicts (kotodama, wave 2)

Seat: critic, leaf. Lane base `f556d1049fe651d3d63975600b13acd9fb686f15`. Inputs read: `/home/vgpnk/Projects/shokunin/LEARNING.md` (the trend table, lines 26-38), prompt §4 (`.ufo/prompts/kotodama-round-75.md:116-117`), QUALITY 20, `corpus/lessons/round-74.md`, `round-74-verifier-spotcheck.md`, the r69-r74 filed trend lines and the r70-r74 closure rulings, `reports/round-75/claims.json` and `ledger.json` (read only), the staged lesson/QUALITY/entries under `w2/stage/`, the staged shokuknow tree. Nothing in the lane was written except this report. The lane worktree still equals base plus uncommitted edits that I did not grade. Tools installed: none (`pdftotext` was already on the host). Scratch `/fast/scratch/hyaku/kotodama-r75/CritTrendObservables2` removed before yield.

Axes: (1) does each verdict sit on a LEARNING.md observable; (2) is the observable machine-checkable; (3) does the evidence exist at base or only after landing; (4) what falsifies it.

## 0. Verdicts, in one table

| trend | candidate | what the evidence supports | exact words to file |
|---|---|---|---|
| expansion | improved if C lands | **improved**, with the one-ground caveat the r72-r74 closures required, and with the "uncovered" wording narrowed (Greimas/Propp are held at base) | §2 |
| quality | unchanged, or improved only via Ca | **unchanged.** Ca's repairs cannot be a quality observable (QUALITY 20) | §3 |
| discernment | improved only if the rejects are shown by committed evidence | the stated condition is **not an observable**. Discernment is `improved` on LEARNING clause 2 (disagreement → lesson → grounded criterion) via QUALITY 27, **only after the S870 reject row is reworded** (F1); the filed report must say no round-75 outside spot-check has run | §4 |

"37 refused staged files" and "4 refused amendment shapes" must not be filed as discernment evidence (F2, F3).

## 1. Findings that change what may be filed (ranked)

### F1 — the staged S870 reject reason is the round-74 S899/S900 error again, in the round that lands QUALITY 27 (HIGH; affects discernment and claim-C kill rule wording)

Observed (plain GET, UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`, 2026-10-27):

- `https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html` → 200, 45238 B, sha256 `51251e22c617617a…` (= the lesson's 45238 B / `51251e22…`).
- The span the lesson calls "staged S870's quote", `作品中的人物名字和地名也一样…`: **0 hits** on that page (NFKC + whitespace fold). Agrees with the lesson.
- But that span is **not staged S870's anchor.** `/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md:18` (staged S870) carries the anchor 「我喜欢把写小说想象成邀请读者走进一个由我搭建的幻想屋…」 and the recheck `grep -c '世间万物运转的方式'` → 1. On the page I get **1** hit for the anchor, **1** for the recheck term (raw `grep -c` over lines = 1 as well), 0 for the lesson's span.
- The span `作品中的人物名字和地名也一样…` is the anchor of **staged S871** (Douban, `https://read.douban.com/submit/writing_guide`, §4「取个好名字」; `/home/vgpnk/Projects/shokuknow/lanes/kotodama/SOURCES-PROPOSED.md:125`). Plain GET of that Douban URL → 200, 70838 B, **1 hit** for the span.
- The register binds it to the chinawriter URL: `absent-defect-register.md:122` (register S787, chinawriter URL, that span) while register S786 (:121) carries S870's anchor on the conlang.org URL — the same one-row positional shift as register S816/S817 (R74-M5), and `census-adjudication.json` lists the same pair as `binding: positional`.

So the lesson row (`w2/stage/corpus/lessons/round-75.md:73`: "staged S870's quote `作品中的人物名字和地名也一样…` is absent from the page it is bound to") files a reason observed on one artifact (the chinawriter page tested against S871's span, via register S787) against another (staged S870, whose own anchor is on that page). That is exactly QUALITY 27's text. The round-72 closure (`round-72-verifier-spotcheck.md:52`) agreed with the same wrong-artifact reasoning (it tested 「作品中的人物名字和地名」 → 0), so "outside agreed" does not protect it.

Why QUALITY 27's own check does not catch it: its scan prints `<row-id> <own-url> <count>` and requires 0 for an absence reason. Here the count on the row's own URL is 0, so the row passes the scan; criterion 27's limits paragraph concedes "a grep cannot tell whose clause a quoted span means". The criterion has no red-before on this row.

Consequences:
1. A non-author closure that re-tests S870's own anchor will record `disagree` on the reason, the same class as r74 — a new disagreement in the very round that adds the criterion, which is the `harmed` clause if left unlearned.
2. Claim C `kill_rule` says "the staged S870 quote is treated as located rather than refused". Staged S870's own anchor **is** located (1 hit). The frozen text only stays true if "staged S870 quote" means the register-bound span. The lesson must say which.
3. True and sturdy reasons exist and are cheaper: (i) staged id S870 collides with lane row S870 at base (ICKL: `git show base:corpus/SOURCES.md | grep -E '^ {0,3}\| *S870 '` → `International Council of Kinetography Laban`), so it cannot be appended as staged whatever the quote does; (ii) the span the register ties to this URL belongs to staged S871 and is present on its Douban page (1 hit), the mispairing is register S787's (as lesson R74-M5 says for S816/S817).

Smallest safe correction (lesson text only; claims/ledger untouched): rewrite the S870 Gate reject row and the S870 disposition paragraph and Quarantine S787 row to state: the span tested, whose anchor it is (staged S871), the artifact it was tested on (chinawriter page: 0; Douban page: 1), the register pairing that bridges them, and the collision reason; keep "not appended as staged; document re-opened as S893 with a fresh quote". Add one `## Mistakes` row (class attribution; evidence this finding; captured-by `none` — QUALITY 27's scan cannot see it; fix: the per-row scan prints the count on the span owner's own URL as well, or the criterion states the check is review-only for whose-span). A fix counts only once shown able to fail (QUALITY 12): the scan over the *old* S870 row must print 0 on the page and 1 on the owner's page.

### F2 — "37 refused staged files" overstates; the frozen claim text holds 31 (MEDIUM)

`claims.json` `rejects.refused_files_pending_triage` names 11 + 3 + 2 + 9 + 3 + 1 + 2 = **31** files. The staged lesson's `Refused (37) = 31 by family + 6 path-present with differing staged bytes` adds six files that are **already in the lane**. I re-measured the staged tree: 40 files, 34 absent at base, **6 present with differing bytes** (matches the lesson), and two of those six (`worldbuilding-setting-practice.md` and its amend) were *adopted* in round 74 (`round-74-verifier-spotcheck.md` §2 claim C) — counting them as refused contradicts the round-74 record. Round 74's own triage used three buckets (2 adopted / 4 path-present / 34 refused). Round 75's REJECTS leg forces adopted + refused == total, which produces 37; that is a leg-shape artefact, not a decision.

File: "3 adopted, 31 refused, 6 path-present with differing staged bytes (byte-level decision routed)". Never "37 refused".

### F3 — reasons on the refused families are partly false as written (MEDIUM; same class as F1)

Checked against the staged bytes and the base tree:
- **verification amendments (9)**: reason "lane-internal process texts, not source-backed domain knowledge; no registry row can support them". True for 4 (r10, r11, r12, reopen-gate: their `source:` lines are lane-local paths such as `lanes/kotodama/round10/gate10-report.txt`). **False for 5** (citation-format r13, r14, r15, r16 and journal-serial r16 cite external URLs: cir.nii.ac.jp, douban, play.google.com, k10plus SRU). Flip text "an own-work source path … or keep them as lessons" does not fit them. Also, `journal-serial-catalogue-records` and `reopen-gate` have no parent at base (`git cat-file -e` → absent), so for those two the "amendment" is a new path, not an amendment.
- **conlang (3 + 1)**: "staged bytes differ from the lane's" — all four amendment paths are **absent at base** (`git cat-file -e` for each), so there are no lane bytes to differ from; the lane's *parent* `conlang-scholarship.md` differs, which is a different artifact.
- **calendar-festival-systems amendments (3)**: "parent entry and sources are not lane rows". `calendar-festival-systems.md` exists at base; and `amend-2026-10-24` cites S919 and S921 — the Marrone and Persée pages that this round lands as S892 and S885 (staged file lines 59-60). After landing, 2 of its 5 sources **are** lane rows.
- naming-systems (11): "no lane row holds the document" — re-derived true (URL overlap with the base registry: 0 of 8 sampled amendments' URLs in lane; one conlang-scholarship amend shares 3 of 4).

So the rejects are not "shown by committed evidence"; at best the outcome (do not land) is defensible and the reasons need the artifact named per file.

### F4 — "4 refused amendment shapes" has no referent (LOW)

`grep` over `w1/`, `w2/`, `drafts/`, `reports/round-75/` finds the phrase only in this seat's spec. The lesson names 6 families (naming, calendar, era, verification, conlang, narrative 23c/24) plus the path-present bucket. No four-item list exists. Mark `unprovable`; do not file it.

### F5 — deep claims of the entries have no committed capture (LOW for the verdict, HIGH for a "tier A / page by page" sentence)

`reports/round-75/evidence/S885.txt` (staged) is a `whole-document` window of the **notice** page (3720 visible chars). In that window `noyaux` 0, `catalyses` 0, `trois niveaux` 0, `données pures` 0, `Innombrables` 1. The entry's method claims (three levels, noyaux/catalyses, four classes) and the row's scope "Tier A because the printed article was opened page by page" rest on the Persée transcription pages (`…/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0006_0000` and `…_T1_0011_0000`), which have no committed evidence file. I re-opened them live today: p. 6 → 200, 3811 B, `trois niveaux de description` 1, `actions` 1; p. 11 → 200, 4061 B, `noyaux` 2, `catalyses` 3, `indices` 3, `informants` 3. True live, uncommitted. The EVIDENCE leg (anchor-only) is satisfied; the bar the entries were admitted under (Gate quote located per row, QUALITY 18 anchor on the named page) is met, so this is not an `expansion: harmed` observable. It is a durability gap a closure can find: the claim of page-level reading is not reproducible from committed bytes.

Committed-evidence statement to use: "page-level claims were re-opened live by plain GET on 2026-10-27; only the notice window is committed" (or have the evidence builder add `T1_0006`/`T1_0011` windows before freeze).

### F6 — S877 stays unmarked in the entry (carried, LOW)

The base entry `worldbuilding-setting-practice.md` cites S877 outside the row's scope cell (r74 wave-2 finding). It is recorded in the r74 lesson and as open routed item 3 of the staged r75 lesson, but the entry itself carries no marker and no superseding row is in the round-75 row set. Not a falsity finding (a scope overreach), so not `quality: harmed`; but disclose it beside `quality: unchanged`.

## 2. expansion

- **Observable (LEARNING.md:33):** admitted `knowledge/` entries on ground the coverage map did not hold, each `source:` citing a `mined` registry row; harmed iff an admitted entry fails the bar it was admitted under.
- **Supports improved:**
  - At base (all re-run by me against `f556d10`): `git ls-tree -r --name-only $B corpus/knowledge | grep -ci narrative` → 0; registry 808 rows; 249 `.md`; `git grep -l -i -E 'Todorov|narratolog|叙事学|物語論|lexie|catalyse' $B -- corpus/knowledge | wc -l` → **0**. After landing (claim C): 252 files, 817 rows, rows S885-S893 `mined`, each cited by an entry's `source:` line.
  - The three entries land on new ground (Barthes/Todorov/Greimas as narrative-structure scholarship; CJK narratology; the S/Z and Marrone five-codes material).
- **Narrow the wording:** the ground is not zero for Greimas/Propp. `comparative-frameworks.md:15,78` carries Greimas's six actants and Propp's 31 functions; `costume-semiotics.md` carries Barthes's fashion semiotics; three files mention "narrative structure" incidentally. `git grep -il actant $B -- corpus/knowledge` → 4 files. So file "uncovered" for the narrative-structure scholarship, not for structuralist sources generally.
- **Caveat that every closure since r72 required:** base file + two dated amendments are one ground; 249 → 252 counts files, not three independent grounds.
- **Falsifies it:** any landed entry whose `source:` cites an id outside S885-S893 or a row not `mined`; a Gate quote not found in its stored window; an entry modified or deleted at base (`git diff --name-status $B <lands> -- corpus/knowledge` must be exactly 3 `A`); the counter's `ACCEPT-C-75` below 13/13. F5 is the only live risk: if a reviewer holds "page by page" to committed bytes, the Tier-A scope sentence of S885 is overstated; the verdict (improved) survives, the tier wording does not.
- **Exists:** ground at base; the three entries and rows only after landing (`reports/round-75/accept-c.py` is the machine check).
- **Words to file:** "**expansion: improved** — three admitted files on one newly entered ground (narrative-structure scholarship: 0 narrative-named files, 0 files naming Todorov/narratology/叙事学/物語論 at base; Greimas's actants and Propp's functions were already held in `comparative-frameworks.md`), citing nine rows mined this round (S885-S893), 808 → 817 rows, 249 → 252 files. Caveat: the base entry and its two amendments are one ground; page-level locators were re-opened live and only the notice windows are committed."

## 3. quality

- **Observable (LEARNING.md:34):** an entry re-verified, deepened, or superseded by a stronger one, or stale entries re-verified, with no admitted entry failing its re-check.
- **Round-75 changes:** SHONEN/README count repairs, `sweep.py` last-footer read, QUALITY 23 addendum + 27 (+28 staged), SCORECARD annotations, round-74 Gate annotation. All are record/instrument repairs: QUALITY 20 (`corpus/QUALITY.md:61`) says they "are calibration work, never quality or discernment observables" and a round repairing records "must declare `unchanged`".
- **No pre-existing entry** is touched by C (3 `A` paths) or named by Ca's fixed surfaces. The only candidate, the S877 supersede, is routed, not done.
- **Falsifies `unchanged`:** a diff of `corpus/knowledge` at `<lands>` that modifies or supersedes a base entry with a stronger one. **Falsifies "not harmed":** an entry found false or stale and left unmarked. Today's known item is F6 (scope overreach, recorded in the lesson, not on the entry).
- **Exists:** at base (the Ca repairs' read set); `improved` could never exist for a repair-only round.
- **Words to file:** "**quality: unchanged** — no existing entry re-verified, deepened or superseded; Ca's repairs (README/SHONEN counts, last-footer sweep, QUALITY 23 addendum and 27) are calibration work (QUALITY 20). Not harmed; the S877 scope overreach in the round-74 entry stays routed (lesson `## Routed to round 76`), not repaired."

## 4. discernment

- **Observable (LEARNING.md:35):** the outside spot-check agrees with the gate on admits and rejects, **or** a disagreement becomes a lesson that adds a grounded `QUALITY.md` criterion. Harmed iff a disagreement is left unlearned or a criterion is added with no lesson behind it.
- **The candidate condition ("improved only if the round's rejects are shown by committed evidence") is not a LEARNING observable.** A subagent the lane dispatched is still the lane (LEARNING.md:45-46); r71's closure refused wave-2 seats as the outside check. Lane-side proof that rejects are well-founded is gate hygiene (calibration). Mark that condition **unprovable** as a discernment observable.
- **The observable that does fire (clause 2):** the r74 non-author closure recorded 2 disagreements (staged S899/S900 reasons) at base: `corpus/lessons/round-74-verifier-spotcheck.md` §3 and routed item 2 (R2, line 100); the lesson side exists at base (`corpus/lessons/round-74.md` R74-M5 and `## Quarantine`). The criterion exists only after landing: `git grep -c '^27\. ' <Ca-lands> -- corpus/QUALITY.md` → 1 (base: 0), grounded in R2/R74-M5 (staged criterion 27's "Grounded in" cites `round-74-verifier-spotcheck.md:100` and R74-M5). Precedent: r72 filed `improved` on criterion 21 (K71-8); r73 `improved` on 22/23/24; r74 `unchanged` because 26 was lane-authored from lane-internal wave-2 findings and the closure said `improved` "is not earned" while the disagreement was only routed. Round 75 is the round that turns that routed disagreement into a criterion, so `improved` fits clause 2 provided the S870 row is fixed (F1).
- **Do not claim:** clause 1 (agreement). No round-75 outside spot-check has run; it is the closure's. Criterion 28 and the 23 addendum come from lane-internal wave-1/r74 mistakes and add nothing to this observable.
- **Falsifies `improved`:** (a) criterion 27 uncommitted or not citing a committed lesson (r71 K71-1 class: criterion only in the worktree); (b) the closure finds a new disagreement in this round's Gate left unlearned. F1 is that case today: S870's reason is wrong-artifact and criterion 27's scan passes it. F3's family reasons are the same class. If F1 is not fixed before landing, file `unchanged` and route F1.
- **Exists:** disagreement + lesson at base; the criterion only after landing; the round-75 spot-check only after the report.
- **Words to file (after F1 is fixed):** "**discernment: improved** — QUALITY 27 lands, grounded in the round-74 non-author closure's two disagreements on the S899/S900 reject reasons (`corpus/lessons/round-74-verifier-spotcheck.md` §3, R2) and the round-74 lesson R74-M5; the round-75 Gate re-states the S870 reject with the artifact each span was tested on (F1). No round-75 outside spot-check has run: agreement on this round's admits and rejects is the closure's, and the 31 refused staged files (3 adopted, 6 path-present with a routed byte-level decision) are lane-side reasoning, not an observable." If F1 stays unfixed: "**discernment: unchanged** — QUALITY 27 lands but the same round's S870 reject row repeats the wrong-artifact class it describes (routed)".

## 5. Smallest safe corrections, in order

1. Lesson S870 Gate row, S870 disposition paragraph, Quarantine S787 row (`w2/stage/corpus/lessons/round-75.md:73,115-118,139`): name the span, its owner (staged S871), the artifact tested (chinawriter 0 / Douban 1), the register S787 bridge, and the id collision with lane S870; add the `## Mistakes` row (F1).
2. Lesson triage paragraph (`:82-87`) and `## Sources & frontier`: "3 adopted / 31 refused / 6 path-present, two of them adopted in round 74" (F2).
3. Lesson verification and conlang family rows: split verification into 4 own-work + 5 external-source files, drop "no registry row can support them" for the 5, change conlang's "staged bytes differ from the lane's" to "no lane copy of the amendment; the lane's parent differs", note calendar `amend-2026-10-24`'s S919/S921 now lane rows S892/S885 (F3).
4. Evidence: add committed windows for the three Persée page URLs cited by the entries (T1_0005/0006/0011 for S885; the Todorov and Greimas page URLs for S886/S887), or soften "Tier A, page by page" (F5). Not a claim change.
5. Do not file "37 refused" or "4 refused amendment shapes".

## 6. Fetch records (QUALITY 22: one UA, bound to each response)

UA for every request: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`; one plain `curl -sL`, no retry, no challenge solved or passed.

| URL | status | bytes | note |
|---|---|---|---|
| chinawriter …/c404024-40083104.html | 200 | 45238 | sha256 `51251e22c617617af797d164684e8927dc792a06140ff35fbaebc158515415f0`; S870 anchor 1, recheck term 1, register span 0 |
| read.douban.com/submit/writing_guide | 200 | 70838 | register-span 1 |
| persee …/doc/comm_…_1113 (notice) | 200 | 109589 | `Innombrables…` 1 |
| persee …/doc/page/comm_…_1113/comm_…_T1_0006_0000 | 200 | 3811 | `trois niveaux de description` 1 |
| persee …/doc/page/comm_…_1113/comm_…_T1_0011_0000 | 200 | 4061 | `noyaux` 2 |
| persee …/docAsPDF/comm_…_1120.pdf | 403 | 294 | altcha interstitial: challenge met, not passed; not used |
| unige.ch …/barth70.html | 200 | 43233 / 41840 (two requests) | `bobcmn` shell, no `lexies`: challenge met, not passed |
| iris.unipa.it …/2014 marrone age dor---2.pdf | 403 | 5867 | Cloudflare "Just a moment": challenge met, not passed |
| web.archive.org/web/20251111222249if_/…marrone… | 200 | 763802 | `pdftotext`: `Mais combien, et de quelle nature, sont ces codes` 1 |

Probing a first page-URL shape without the `…_1113/` directory returned a 200 shell without article text (27519 B); the lesson's directory form is the one that serves text.

Report: .ufo/waves/round-75/w2/CritTrendObservables2.md
