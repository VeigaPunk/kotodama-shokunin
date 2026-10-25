# CritAssimilationContract — round 72 w1

Seat: critic (leaf). Target: the adoption plan for claim C (heritage-taxonomy, two entries,
staged rows re-pointed to lane ids S874/S875) against the round prompt §10 assimilation
contract, clause by clause. Sources read: `.ufo/prompts/kotodama-round-72.md` §10 (ll. 400–463),
`reports/round-72/claims.json` (frozen claim C), `.ufo/waves/round-72/w1/spec.json` items
(ExecScratchMirror, ExecRenumber, ScribeEntries, ScribeLesson, MutRegistryCollision,
SimplifierRows, ScoutMergeScan, ScoutRegisterMap, RevEntryCoupling), staged bytes under
`/home/vgpnk/Projects/shokuknow/merge/kotodama/` (read-only), lane `corpus/SOURCES.md`,
`/home/vgpnk/Projects/shokunin/CORPUS.md`, `corpus/QUALITY.md` criterion 18,
`reports/round-71/telemetry/quarantine-verdicts.md`, `tools/check-cited-lines.py`,
`scripts/sources-census.sh`.

Verification I ran myself (read-only): live probes + capture greps (results below), the
contract's exact collision commands (outputs to `/tmp/CritAssimilationContract/`), pipe/cell
counts on the planned rows and staged rows, existence checks on every corpus path the staged
entries name, citation greps on both refused staged entries.

## Verdict up front

Nine clauses reviewed: 7 compliant (two with mandatory scoping notes), **2 violation-risks that
must be fixed before append, one of which is fabrication-class (V1)**. The plan's skeleton is
sound; the pre-drafted ROW1 text is falsified by today's evidence, and three provenance/dangling
details in the staged entries need owners (two have them, one does not).

---

## Clause-by-clause

### 1. One theme + 1–3 entries — COMPLIANT

The staged theme is one: `heritage-taxonomy-models.md` (canonical) +
`heritage-taxonomy-models.amend-2026-10-24-r13.md` (its own amendment, couples line points back
at the canonical). Two entries ≤ the 1–3 cap; the amendment is not a second theme, it is a dated
addition to the same surface (state heritage taxonomy, ihchina document family). I verified the
two staged files are the only heritage-taxonomy files in the staged `culture-material/` dir and
that no lane file matches `corpus/knowledge/culture-material/heritage-taxonomy-models*` at HEAD.

Caveats (not violations): (a) both staged bodies are outlines (`### Proposed body`, §1–§7
one-liners) — the contract's per-entry QUALITY gate cannot pass on outlines; the scribes must
write real bodies from the round-72 re-open evidence, which is exactly what ScribeEntries +
ExecRenumber instruct; (b) the amendment is admitted only together with the canonical (it
amends it) — the ROWS leg's "exactly two" is coherent only as a pair.

### 2. Re-grounding — are S874/S875 really re-pointed BY DOCUMENT? — COMPLIANT

- staged S863 source URL = `https://www.ihchina.cn/project.html` (bare); planned S874 row names
  the same bare URL + two captures of it → same document, id follows the URL. ✓
- staged S967 = `web.archive.org/web/20200216023423id_/http://www.ihchina.cn/project.html`
  with live original `https://www.ihchina.cn/project.html` — same document family; criterion 18
  sanctions live-URL + same-page capture rows, and ExecRenumber's rule (amendment's capture
  citations re-point to S874 with capture timestamps named in text) is by-document, not
  arithmetic. ✓
- staged S867 = `https://online.bunka.go.jp/db/heritages/search`; planned S875 names the same
  URL. ✓
- Re-opens this round: `/tmp/ihchina-2020.html`, `/tmp/ihchina-2026.html`, `/tmp/bunka.html`
  all carry today's mtime (2026-10-25 11:14–11:15). Anchor honesty spot-checked: the 2020
  capture names 四批, the 2026 capture and today's live page both name 五批, both carry
  十大门类 + 罗马数字代表所属门类; bunka evidence carries 令和 / 伝統的建造物群 / 材質・構造・技法.

Residual risk (fixable): the canonical's staged `source:` line cites `…project.html?tid=4`,
and the campaign's own staged recheck for S863 warns the `?tid=4` view "intermittently serves
a truncated body to plain clients — the parameterless URL is the stable one". The final entry
should cite the row's parameterless URL (criterion 18's query-aware normalization covers the
identity, but the entry should not canonically name the unstable view).

### 3. 'Append only the rows the admitted entries cite' — does the amendment force a third row? — COMPLIANT, no third row

Verified by direct read: the canonical cites only staged S863 + S867; the amendment cites only
staged S967. No other staged row is cited between them, so used-by exclusivity holds and no
third row is forced. The staged S967 folds into S874 defensibly: it is the same page at a dated
state, criterion 18's same-page-capture rule is the governing precedent, and ROW1's anchor
names both dated states ("as captured 2020-02-16 (四批) and 2026-10-20 (五批)") — keep that
anchor wording, since staged S967 is a distinct claim ("the register as it stood in 2020") and
the fold is honest only because the row says so. SimplifierRows' option (b) is the right call.
The refused entries' rows (S870, S899, S900) are cited by no admitted entry → not appended. ✓

### 4. Gate ≥1 admit ≥1 reject — COMPLIANT

Plan: 2 admits (the pair above) + 2 refuses with reason + flip (ScribeLesson drafts the reject
table). I verified the refusal grounds myself: `narrative-structure-frameworks.md:32` cites
staged S870, which reg-to-staged.txt maps to register S787 — round-71 verdict **REFUSED**
(quoted span absent; quarantine-verdicts.md). `worldbuilding-setting-practice.amend-2026-10-23.md:4,5`
cite staged S899/S900 → registers S816/S817 — both **REFUSED**. Grounds are committed
round-71 evidence, not fresh fabrication.

Residual note: the refused entries' chinawriter URLs were not re-opened today; the refusal
rests on quarantine-REFUSED staged rows, so no re-open is required for a refusal — but the Gate
should say exactly that ("refusal inherited from round-71 committed verdicts; the staged row is
REFUSED, so the entry cannot ground its rows"), or a literal reading of the kill rule ("any
cited source not opened this round") can be aimed at it.

### 5. Used-by exactness — COMPLIANT as drafted

ROW1 used-by = both admitted entries; ROW2 used-by = canonical only. This matches the
citations exactly (the amendment never cites the bunka row). Exact repo-relative path strings;
census E11 (used-by path exists) is satisfiable in the mirror. No fix needed.

### 6. Recheck-cell normalization — COMPLIANT

Staged recheck cells are prose (`180d — `curl …` (ran 2026-10-23)`, plus for S863 a
tid=4-stability note); planned rows carry bare `180d` / `90d` — valid `NNd` per census E09.
The stripped prose must land in the lesson's Gate block (ScribeLesson covers it; §10 requires
the re-verify conditions be recorded there). Structural note: this package's staged rows are
13-pipe/12-cell (campaign adds a round cell), not the kengaku escaped-pipe failure — a
byte-exact append would fail census E01 on NF!=13; the planned 12-pipe/11-column rows are the
correct normalization. No cell in either planned row contains a literal or escaped `|`
(pipe count verified: 12 each).

### 7. Id collision check (0–3 leading spaces pattern) — COMPLIANT, with a mandatory scoping note

I ran the contract's exact commands against the real files (outputs in
`/tmp/CritAssimilationContract/{reg-ids,staged-ids,collisions}`):

- reg-ids: 797; staged-ids: 132; **raw intersection = 15 ids: S859–S873** — the pre-existing
  staged-vs-lane collisions, none adopted this round.
- Adopted ids: **S874/S875 absent from the lane registry (0 matches)** → the adoption's new ids
  are clean. **But S874 and S875 both EXIST in the staged set** — as *different documents*:
  staged S874 = register S791 (UNVERIFIABLE, truncated DOI, unfetchable); staged S875 =
  register S792 (REFUSED).

Two consequences the plan must absorb, or a reviewer blocks it:

(a) The raw `collisions` file is NONEMPTY (15 ids). Claim C's COLLCHECK leg scopes emptiness to
"the adopted rows' new ids" — the receipt must show both the full 15-id intersection (guard
works; MutRegistryCollision fixture (c) predicts exactly this) and the adopted-id filter
empty. Paste both, plus the renumber map.

(b) False-provenance guard: the report's renumber map must state explicitly that staged
S874/S875 are **not adopted** (their register rows are quarantined unverifiable/refused and
wait for a later round per §10) and that lane S874←staged S863, lane S875←staged S867 by
document. Otherwise the adopted ids read as an identity change against the staged namespace.

The contract's "prove the guard once" fixture (an indented `  | S874 |` row must produce a
nonempty collisions) is owned by MutRegistryCollision — required before append, unchanged.

### 8. Scratch mirror census gate BEFORE append — COMPLIANT in design, two execution risks

Design matches the contract: rsync `corpus/` → `/tmp/r72-mirror/corpus`, append the two rows +
entries, `sources-census.sh validate --file`, exit 0 before the first real registry append,
receipt at `.ufo/waves/round-72/assimilation/validate-receipt.txt` (claim leg SCRATCHMIRROR).

Risk 8a (vacuity): ExecScratchMirror step 3 allows **placeholder entry bodies** ("if absent,
create placeholders with a marker body"). Census validates the registry, not entry prose, so a
mirror holding placeholders passes while proving nothing about the admitted bytes. Fix: the
receipt must record which entry bytes were mirrored (sha or note "placeholders"), and if
placeholders were used the L1 re-runs the mirror with the final entries before the real append
— otherwise the gate is theater.

Risk 8b (ordering): the receipt must demonstrably predate the registry append (commit it as
wave evidence first, or timestamp + name the sequence in the report).

### 9. Source repo read-only — COMPLIANT

Every plan write targets `/tmp` (`r72-mirror`, `r72-entries`, `r72-entries-scribe`,
`r72-lesson`, `r72-corrections`) or the lane; no item runs a campaign tool in shokuknow
(renumber-staged.py / merge-plan.py / quote-lint.py / absent-defect-register.py are all
"read their outputs; run nothing"). Scouts fetch to /tmp. Quarantine-first is satisfied:
round-71 telemetry shows the full 21-row kotodama slice verdicted (10 PRESENT / 7 REFUSED /
4 UNVERIFIABLE, re-derived by RevQuarantine) with adoption explicitly CLOSED — round 72 is
the contract's "later round" in which package adoption may start. (Note: round-71's prompt
already carried §10, confirming round 71 was this lane's quarantine-first round.)

---

## Violation-risks (must fix before append)

### V1 — FABRICATION-CLASS: ROW1's "live page unreachable from the lane host 2026-10-25" is false

The pre-drafted ROW1 in ExecScratchMirror's item asserts, in the anchor cell,
"live page unreachable from the lane host 2026-10-25". I probed it from this host:
`curl https://www.ihchina.cn/project.html` → **HTTP 200, 43,230 B, 2.9 s**, body names
五批 + 十大门类 + 罗马数字代表所属门类 (saved as
`/tmp/CritAssimilationContract/ihchina-live-2026-10-25.html`). It is byte-identical in size
to the 2026-10-20 capture (43,230 B). The claim is falsified by direct evidence.

If ExecScratchMirror writes the provided row verbatim, the registry lands a false empirical
claim (CORPUS.md: "a corpus entry is falsifiable or marked opinion" — this one is falsifiable
and false), §10 rule 1 is breached in spirit (the row asserts a property of this lane's access
that this lane can and did test), and the amendment's "reachable stand-in" framing inherits a
false premise. ExecRenumber's item does not own the row text — nothing in the plan currently
forces this fix.

Smallest correction: rewrite ROW1's anchor to the true state — "page as served live
2026-10-25 (HTTP 200) and as captured 2020-02-16 (四批) / 2026-10-20 (五批)" — and have the
Gate record the live page's access date 2026-10-25 with its ≤25-word located quote (this also
makes the GATE leg satisfiable for all four named URLs: live + 2 captures + bunka). The
amendment's §N+1 keeps the capture as the durable citation but must state the live page WAS
reachable on the 2026-10-25 re-open (its "unreachable" claims survive only as campaign-round
11/12 history).

### V2 — FALSE-PROVENANCE / DANGLING DETAILS in the adopted entries (two owned, one unowned)

Owned (ExecRenumber item explicitly routes them — verified in its full text): the amendment's
"the lane's row S837" (in THIS lane S837 is the BBC Sikhism row — keep the rewrite to name the
ihchina document); the amendment's couple `culture-material/calendar-festival-systems.amend-2026-10-24-r10.md`
(missing in lane; re-point to `corpus/knowledge/culture-material/calendar-festival-systems.md`,
which exists); the canonical's "643-row registry" sweep (real: 797 — re-run and record);
both recheck fields referencing the campaign's `SOURCES-PROPOSED.md`.

**Unowned:** the canonical's `couples:` line names `myth-symbol/calendar-festival-systems.md` —
I verified this path does **not** exist in the lane (only `culture-material/calendar-festival-systems.md`
does). No seat item instructs fixing the canonical's couple (ExecRenumber covers only the
amendment's). Also the canonical's `ground:` cell speaks in campaign voice ("the wave brief's
fifth scoped domain") with no owning instruction. Fix: L1 integration duty — re-point the
canonical's couple and rewrite `ground:` in lane voice before landing, and add both to
RevEntryCoupling's acceptance check.

### V3 — CITEDLINES leg is one sentence away from failing

`tools/check-cited-lines.py` flags **MULTI-ID** when one line carries ≥2 distinct S-ids. The
re-pointed entries concentrate on S874/S875; any single sentence naming both (a natural
"the two states' models (S874, S875)" topic line) fails claim leg CITEDLINES. No seat item
instructs line-scoping of ids. Fix: run `python3 -B tools/check-cited-lines.py` over the
`/tmp/r72-entries{,-scribe}` drafts before integration; keep each line to one S-id.

## Non-§10 but claim-internal (flag for ExecCCounter / L1)

GROUND leg says the gap sweep "is re-run at the 797-row registry … and returns 0 owners" — at
`<lands>` the registry will name ihchina/bunka, so a naive re-run at lands fails the leg.
The counter or receipt must pin the sweep to base `b60c7b1` (or to pre-append bytes); this is
the frozen claim's wording, not §10's, and it is fixable in the counter's implementation.

---

## Summary table

| §10 clause | Verdict | Fix |
|---|---|---|
| One theme + 1–3 entries | Compliant | none (bodies must be real, not outlines) |
| Re-grounding by document | Compliant | cite parameterless ihchina URL, not `?tid=4` |
| Append only cited rows / third row | Compliant | keep both captures named in ROW1 anchor |
| Gate ≥1 admit ≥1 reject | Compliant | state refusals inherit round-71 quarantine verdicts |
| Used-by exactness | Compliant | none |
| Recheck normalization | Compliant | prose to lesson Gate block (planned) |
| Id collision check 0–3 spaces | Compliant w/ note | receipt shows full 15-id intersection + adopted-id empty + renumber map naming staged S874/S875 as not-adopted |
| Scratch mirror gate before append | Compliant w/ risks | no placeholder-only receipt; receipt predates append |
| Source repo read-only | Compliant | none |
| V1 row text falsified | **Violation-risk** | rewrite ROW1 anchor + Gate live quote (fabrication-class) |
| V2 provenance/dangling | **Violation-risk** | S837 rewrite (owned); canonical couple + ground: need an owner |
| V3 CITEDLINES scoping | **Violation-risk** | lint drafts with check-cited-lines.py |

Impacted axes: coverage (claim C legs ENTRIES, REPOINTED, GATE, CITEDLINES, SCRATCHMIRROR,
COLLCHECK at risk; ROWS, REJECTS, GROUND sound). Calibration (Ca) untouched.

Tooling: no installs/upgrades needed (system grep/awk/curl/python3 only). Downloads:
`/tmp/CritAssimilationContract/ihchina-live-2026-10-25.html` (live ihchina 清单页, fetched
2026-10-25 for the reachability counterexample) plus the three contract-command outputs
(`reg-ids`, `staged-ids`, `collisions`) in the same dir.
