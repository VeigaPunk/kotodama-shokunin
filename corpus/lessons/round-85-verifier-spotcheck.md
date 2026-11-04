# Round 85 — non-author verifier spot-check

author: hyaku closure (non-author integrator, @m_zfl)

Reviewed 2026-11-04. Lane-authored revision: `798ed60e6752287cd03750672b35833273d7f6eb`; base: `0d181583b18ae94e80a251ca5ab5f3055b16c74c`; frozen declaration/counter: `ed816e71a97dde9b65f9265276b77c7583274671`. Reviewer is not the round author. Read-only source-review seat: CloseKotodamaR85.KotoSpotR85; closure integrator independently reopened S919 and S923 as well. No lane gate or selftest executed.

## Closure judgment

**status=ok; admitted=false; verdict=rejected-honest-stop.** D verifies. O has useful demonstrated additions, but its frozen before-premise says the existing checker reads the first footer; the pinned base already selects the last footer. Consequently the complete declared before→after does not verify. This is not harm and does not turn a substantive report into a marker. Do not silently replace the frozen claim with only its surviving additions. Counter weaknesses, attribution and timing defects below are separately status-neutral conformance defects, not the rejection predicate.

## Step-1 conformance

- Fleet `git log --format='%an %ae %H' -- .ufo/reports/round-85/kotodama.md` returned `kotodama-shokunin kotodama@shokunin.local 42d5fc51509b04985155f0b719f63030f43b3241`; report path had empty porcelain. Report has substantive work, LOG-linked commits, six required sections and four SHONEN `[~]` assessment lines, not self-granted `[x]` marks.
- `git cat-file -e HASH^{commit}` and `git merge-base --is-ancestor HASH refs/heads/main` succeeded for `ed816e71`, `bd520d85`, `228e3a4c`, `5abe1072`, `76ff0707`, `150f6be7`, `798ed60e`, and historical repair `012e8d3c`. Ancestry was tested against the branch ref, not detached HEAD's nonexistent upstream.
- `scripts/hyaku/jj-lane.sh state <lane>` returned `branch=main local=798ed60e6752287cd03750672b35833273d7f6eb remote=798ed60e6752287cd03750672b35833273d7f6eb ahead=0 behind=0 head=detached tracked=0 untracked=0`. Lane `git status --porcelain` was empty. `git ls-remote origin refs/heads/main` returned that same full hash before this verifier artifact.
- Dispatched prompt matches the rendered template sections 1–5 and carries campaign addendum section 6. Mission/axes binding, 1–3 distinct claims, minimum eight batched L2 seats, report pathname, LOG/commit citations, SHONEN assessment, commit/push order, scope and L0 channel are present. MISSION.md's minimum eight and shokunin.conf's kotodama depth/coverage declaration agree. Report discloses one twelve-seat wave, seven empty deliveries, and parent-held planner role rather than claiming a separate planner seat. Minimum role-split discrepancy (planner held by L1 rather than L2) is routed below; no model actually answering an individual seat is inferred from configured routes.
- LOG Round 85 items 1–7 resolve to the changes and receipts cited in the report. No promotion review is granted: known counter conformance gaps remain, so not all SHONEN assertions are unqualifiedly checkable.

Durable dispatch/completion digest (copied from the mutable watchdog log, independently observed):

```text
2026-11-04T11:12:02-03:00 launch kotodama round=85 pgid=3498074 driver=hyaku-inline attempt=1
2026-11-04T12:22:05-03:00 complete kotodama round=85; hyaku-inline attempt=1
```

## Independent plain re-measurements

Commands below read committed blobs, not live lane-gate output. Run Python with `subprocess.check_output(['git','-C',LANE,...])`, where LANE is this repository's absolute path, B is the base above and H is the reviewed lane revision above.

1. For each R in B,H: `git ls-tree -r --name-only R corpus/knowledge`; count returned paths. Read `git show R:corpus/SOURCES.md` and count `re.findall(r'^ {0,3}\\|\\s*S\\d{3,}\\s*\\|', text, re.M)` (ordinary Python raw-regex notation: single backslashes in the executable expression). Observed **258→259 knowledge files; 842→847 source rows**. Basename regex `metallurg|smelt|smith|foundry|alloy` matched **0→1** owners.
2. `git show H:corpus/knowledge/culture-material/metallurgy-metal-register.md`: UTF-8 blob length **27,848 bytes**; `re.findall('^## ',text,re.M)` **10**; section 2 has **six** decision data rows (after header/separator); section 3 has **20** `- ` anchors with unique source-id set **S919,S920,S921,S922**, all registered. These match the report. Source/body judgment is distinct from structural counts; source sample below agrees with the limited dated-terminology use.
3. For R in B,`228e3a4c27ac2ea8e373de02a315cb5d94222d9b`,H, count `re.findall(r'^- `([^`]+\\.md)` — (.*)$', readme,re.M)` over `git show R:corpus/README.md`, and compare filenames to committed knowledge-tree basenames. Observed rows/files **253/258 → 258/258 → 259/259**. Base missing set: guest-right-hospitality-law.md, maritime-seafaring-lexicon.md, marriage-alliance-bridewealth.md, ordeal-judicial-proof-rituals.md, witchcraft-sorcery-accusation-institution.md; later missing sets empty. Final footer totals/vectors: **253 (32/32/41/29/24/95) → 258 (32/36/42/29/24/95) → 259 (32/36/43/29/24/95)**.
4. `git show B:reports/round-28/readme/sweep.py` contains **`m = matches[-1]`** and **`totals_matches[-1]`**. This independently falsifies O's frozen first-footer premise. Source-reading `tools/check-corpus-index.py` confirms it explicitly attributes inherited last-footer/supplemental semantics and adds the explicit-root, duplicate-failure and malformed-final-footer boundaries. Useful surviving additions are acknowledged, not treated as proof of the full frozen before→after.
5. `git diff --name-status B H -- corpus/knowledge` returned only `A corpus/knowledge/culture-material/metallurgy-metal-register.md`. Comparing all 842 old registry row strings by id yielded **0 changed old rows**. `git show B:PROVINCE.md` equals `git show H:PROVINCE.md`. `git diff B H -- SCORECARD.md` adds capability/correction/claim records without deleting prior axis evidence. Entry scope separates fictional design from dated source authority, engineering and lore-owned canon.
6. SHA256 of `git show H:reports/round-85/measure85.py` is **f4611703c3b031a36fb8c3f2342be0659ee1d6840084022079e62d76195e2871**, matching the report; freeze and H counter bytes are equal. No counter run by this reviewer.

### Gate evidence verified, not re-executed

- `reports/round-85/lands-d.txt`: evaluated/stamped/measured revision `5abe107204f1a98c754d49289e6a3c75ee3dfa44`, counter hash above, D PASS **8/8**, bytes 27848, decisions 6, anchors 20, unknown ids empty, citation lint 0, exit 0.
- `reports/round-85/lands-o.txt`: evaluated/stamped/measured revision `228e3a4c27ac2ea8e373de02a315cb5d94222d9b`, same counter hash, selftest **23 checks**, real index **258 files/258 rows/0 findings**, O PASS **10/10**, exit 0. Missing/duplicate/footer controls carry expected nonclean results in the committed receipt. Tool's selftest tally is evidence-verified, not independently re-executed.
- `final-checks.json` binds combined index **259/259/0**, registry **0 missing/79 registered/0 dead**, cited records **0 empty/0 scratch**, census exit 0 to data revision `76ff07078c4a13d2f9ddad0b9aaf72fd62db71ba`.
- `craft-ledger-red-green.json` commits the same field-completeness command and input hashes: twelve incomplete records/exit 1 → zero incomplete/exit 0. `noharm.json` records five historical footer blocks retained and reviewed/delivered entry SHA equality. These are preserved receipts, not fresh gate executions.
- Counter has no conformant isolated selftest; CriticClaims F1/F2 demonstrate inadequate-tool acceptance, missing freeze-ancestry/LEGCOUNT authority and variable O denominator. Synthetic scratch-commit critic experiments violated the seat's no-mutation restriction and are not promoted to compliant acceptance. Pre-data controls landed after freeze but before dispatch; separability was run after dispatch. Report honestly retains these limits. Gate standard makes these routed conformance defects, not automatic harm or marker status.

## Per-axis verdicts

| axis | verdict | reason |
|---|---|---|
| depth | improved | D's structural measurements reproduce; source sample and scoped design decisions support the new ore-to-metal register. |
| operability | unprovable | Useful explicit-root/duplicate/malformed-footer additions and committed passing demonstrations exist, but O's full frozen before-premise is false. |
| coverage | unchanged | New entry is claimed as D, not a separately proven coverage-axis move. |
| freshness | unchanged | Existing pause retained; no fresh axis move asserted. |
| calibration | unchanged | Honest append-only repairs are recorded without a new scored axis claim; the original false premise remains visible. |
| adjacency | unchanged | Province byte-identical; lore canon and research-method ownership not absorbed. |

No axis is graded harmed. No exploratory claim was declared. No full acquisition is admitted by this closure (`capabilities_added=[]`); the author-added auditor row and its useful demonstrated behavior remain on record, subject to the rejection qualification above.

## Discernment/source spot-check

Access date: 2026-11-04. Canonical URLs below were reopened, not merely the lane's captures. The reviewer seat reopened all five; integrator independently reopened Metallurgy and Bronze Age. Reader-output sizes are not raw HTML-transfer sizes; this review does not certify the lane's historical byte-size/hash metadata.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S919 | admit B, dated terminology | https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Metallurgy | agree | General Sequence of Operations, after Wet Processes, contains “Few methods of metal extraction at once yield a pure product.” Exact 11-word quote; extraction/refining distinction supports the explicitly dated teaching. |
| S920 | admit B, dated terminology | https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Iron | agree, locator defect | The 12-word commercial-varieties quote is present after whitespace folding. It is in the second article paragraph, not the opening paragraph; scoped terminology remains supported. |
| S921 | admit B, dated terminology | https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Bronze | agree | Exact 20-word χαλκός quotation in the second paragraph supports acknowledged translation ambiguity, not a modern assay or universal recipe. |
| S922 | admit B, dated terminology | https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Alloys | agree | Opening definition contains the 22-word nonuniformity quotation after line folding; source distinguishes mixtures from homogeneous compounds. |
| S923 | reject C, stage/diffusion teaching | https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Bronze_Age | agree, scope wording caution | Exact 16-word quote appears in the opening paragraph's Phoenician/Greek diffusion argument. Source says bronze knowledge came to Europe's races from outside and “most races” passed the stage. Rejection as neutral present-day historical teaching is justified. “Universal” overstates literal scope: source also acknowledges overlap and different chronologies. |

Thus at least one admit and one reject are independently checked, and all five newly written SOURCES-row quote lengths/presence were sampled. S919 independently satisfies the new-row ≤25-word quote requirement without relying on the lane's receipt.

Required census freshly executed: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → **exit 0**, final `kotodama ok .../corpus/SOURCES.md`; inherited W04 duplicate-URL warnings and W01 tier-C-mined warnings, no E-code.

## Learning trends

- **expansion: improved** — 258→259 knowledge entries, four new B/mined rows supporting an uncovered naming-chain surface and indexed new entry. This does not override the O claim rejection.
- **quality: unchanged** — no old knowledge files changed/re-verified/superseded; record repairs and a new instrument do not establish the quality observable.
- **discernment: improved** — outside spot-check agrees on admits and reject; actual missing-ledger-field mistake grounds QUALITY 32 with committed same-command red/green. Locator/scope wording defects are routed, not hidden.

## Routed defects for kotodama's next round

1. R85-C1: Preserve and correct the false frozen O before-premise by append-only reference; do not re-claim acquired last-footer selection. Any new claim must distinguish inherited capability from explicit-root/duplicate/malformed-footer additions. Current report/lesson already disclose the correction; the frozen record remains intentionally unchanged.
2. R85-C2: Repair counter authority/kill-power under a new declared revision: isolated counter selftest, frozen leg inventory, freeze ancestry/refusal discipline and independent named failure controls. Preserve old counter and receipts. Do not retroactively rescore r85 with new predicates.
3. R85-C3: Keep pre-data controls and separability evidence at the required stage in future rounds; disclose actual timing. The current after-dispatch check cannot become pre-dispatch evidence.
4. R85-C4: Correct S920's “opening paragraph” locator via a new superseding source row and append-only lesson correction, not immutable-cell editing. The quote is present; this is a locator defect, not false scholarship.
5. R85-C5: Narrow “universal” in S923-related narrative to the source's broad racial-stage/Europe-diffusion model; explicitly retain its “most races,” overlap and chronology qualifications. Use new correction records where source cells are immutable.
6. R85-C6: Enforce no-mutating-git/jj seat boundaries and maintain separate attribution for synthetic out-of-protocol evidence; report actual answering-model/status metadata only when supplied.
7. R85-C7: Meet the template's L2 planner-seat role split or obtain a recorded authorized exception before claiming full wave-shape conformance; parent-held planning is not a dispatched L2 planner.

No lane-authored files changed by closure, no SHONEN marks written, no promotion/mint. Tool installs/upgrades: none.
