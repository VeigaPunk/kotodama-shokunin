# ConnectorAdjacency — round 74 wave 2 (falsify; hyaku run 7)

Seat: `ConnectorAdjacency` (leaf; no delegation, no subagents, no background jobs).
Duty: re-verify the **wave-1** `ConnectorSiblings` verdict (`.ufo/waves/round-74/w1/ConnectorSiblings.md`) against **lore-shokunin's CURRENT corpus and PROVINCE**, and check for any **NEW** overlap created by the **landed** files.
Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Fleet root: `/home/vgpnk/Projects/shokunin`. Lore repo: `/home/vgpnk/Projects/shokunin/lore-shokunin`.
Read-only everywhere except this file and scratch under `/tmp/connectoradjacency/`.

---

## 0. What was re-verified, and at which tree

The lane moved under this seat twice while the scan ran, so every count below is pinned to a stated revision.

| artifact | revision | note |
|---|---|---|
| round-74 base | `f7104cbce186bc2e1522abf0cfd619cc834628bb` | claim C/Ca "before" |
| operative freeze F3 | `00c408a0af2fa5ddf65af2224152ce258b26d896` | frozen `claims.json` |
| claim C lands | `c4bf61a8d722f9168ce0fd8021a6261c000610c5` | entries + rows + README index + lesson |
| claim Ca lands | `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3` | SCORECARD corrections, SKILL rows |
| wave-1 C landing | `d7a3840` | |
| wave-1 junk-receipt commit | `1d7add3` | |
| wave-2 repairs | `9d4d478b260e27c1b65e2e9b95342315c42a981b` | lesson corrections, QUALITY 26, entry edits |
| lane HEAD at scan end | `6ec552b33e891f87b6bb998f8cd84349cf3d65ae` | = `origin/main`; adds `measures-{c,ca}-head.txt` only |
| kotoba HEAD at scan end | `559ee76` (round-74) | **moved mid-scan**, see F1 |
| lore HEAD | `380ef3abc7c7af11d7f23e9f9c82bb1937e1f695` | last lore commit 2026-10-21; lore has not run since round 103 |

**Counter re-run (isolated clone, per dispatch).** `D=$(mktemp -d) && git -C "$D" init -q` → toplevel printed `$D`; cloned to `$D/lane`; `git checkout --detach <lands>` then `git branch -f main <lands>` inside the clone only.

```
=== ACCEPT-C at claim C lands ===
ACCEPT-C-74: PASS legs=13/13     (exit 0)
=== ACCEPT-CA at claim Ca lands ===
ACCEPT-CA-74: PASS legs=11/11    (exit 0)
```

Both counters pass **at their own landings**. The lane's own wave-2 receipts record `ACCEPT-C-74: PASS legs=13/13` at head and `ACCEPT-CA-74: FAIL legs=10/11` at the combined tree (APPENDONLY red) — that is a Ca-side matter, out of this seat's lane, but it bounds what "landed" means for the two claims: **C is green at `c4bf61a`, Ca is green at `5e4796c`, and the two are not jointly green at head.** Neither counter reads a sibling lane's corpus, so neither can see an overlap; the sibling scan is this seat's exclusive instrument.

---

## 1. Verdict per sibling (re-verified against CURRENT trees)

Method (read-only, no writes): for every lane under the fleet root except kotodama, grep the lane's own `corpus/` tree for the w1 six-term set **and** for the landed files' distinguishing strings (entry filename, both `- topic:` texts, the three source hosts, `設定ノート`, `設定資料集`, `S881`–`S884`).

```
### FINAL discriminating sibling sweep (post-landing) ###
audio-shokunin         0        kama-shokunin          0
chousa-shokunin        0        kasegi-shokunin        0
game-dev-2d-shokunin   0        kengaku-shokunin       0
game-dev-3d-shokunin   0        kotoba-shokunin        0
kagi-shokunin          0        kumitate-shokunin      0
kaidoku-shokunin       0        lore-shokunin          0
kake-shokunin          0        mado-shokunin          0
kama-shokunin          0        mori-shokunin          0
revenger-shokunin      0        souji-shokunin         0
tabi-shokunin          0        tameshi-shokunin       0
                        tsukuroi-shokunin 0
### sibling SOURCES rows S881-S884 anywhere ###
kotodama-shokunin/corpus/SOURCES.md        (only the lane that owns them)
```

**Verdict: no sibling lane contests the worldbuilding-setting-practice surface, and the landed files created no new sibling overlap.** This is the w1 verdict's central proposition, and it **survives** re-verification.

| sibling | verdict | evidence (path:line) | note |
|---|---|---|---|
| **lore-shokunin** | **partial** (unchanged) | `lore-shokunin/PROVINCE.md:3` (owns entities/relations/timeline), `:19` (CM-f and CM-g stay `uncovered`), `:23` (frontier), `:28` (kotodama adjacent: handoff packets, naming, calendar/era); `lore-shokunin/corpus/README.md:72` (CM-f), `:73` (CM-g), `:79` (digest `5f4c02bf`), `:90` (CM-f frontier), `:94` (packet-intake frontier); `lore-shokunin/SKILL.md:7` ("Lore owns fictional-world entities, relations, timeline and integration") | see §2, §3 — the CM-f contact is now **sharper** than w1 recorded |
| **kotoba-shokunin** | **adjacent, none on this surface** | `kotoba-shokunin/PROVINCE.md:66` (kotodama row: "kotodama owns generative linguistic-cultural worldbuilding for fictional worlds and refuses prompt/skill craft by name (SKILL.md:3, PROVINCE.md:19-20)"), `:3` (domain: prompt & skill craft) | **the w1 citation `PROVINCE.md:3, 61` is stale** — see F1 |
| chousa-shokunin | none | `chousa-shokunin/PROVINCE.md:3` (deep-research method), `:10-15` (refusals: bounty/model-quality/orchestration/secrets) | |
| kengaku-shokunin | none | `kengaku-shokunin/PROVINCE.md:3`, `:24-34` | its 16 `SSOT` hits are its own eval-craft "single source of truth" notes (`corpus/evidence/round25-calibration/…`, `corpus/lessons/round-16-recensus.md:23`) — **false positives, not this surface** |
| kumitate-shokunin | none | `kumitate-shokunin/PROVINCE.md:3`, `:25-29` | |
| tameshi-shokunin | none | `tameshi-shokunin/PROVINCE.md:3-6`, `:14-18` (refuses product domains) | |
| kake-shokunin | none | `kake-shokunin/PROVINCE.md:3`, `:33-42` | |
| mado-shokunin | none | `mado-shokunin/PROVINCE.md:3-16`, `:67-81` (round-36 localization refusal) | |
| kagi-shokunin | none | `kagi-shokunin/PROVINCE.md:3`, `:59-60`, `:67-68` ("report, don't absorb") | |
| souji-shokunin | none | `souji-shokunin/PROVINCE.md:3`, `:34-47`, `:79-87` | |
| audio, game-dev-2d, game-dev-3d, kaidoku, kama, kasegi, mori, revenger, tabi, tsukuroi | none | grep 0 across all `corpus/` trees; no PROVINCE line claims the surface | |

---

## 2. The lore boundary, re-verified against lore's CURRENT state

The w1 report's lore analysis was written against lore's round-103 tree. Lore's HEAD is unchanged (`380ef3a`, 2026-10-21), so the corpus facts still hold — but the **landed kotodama files changed what lore is being asked to own**, and that is where the finding is.

**F2 (HIGH) — The landed amendment hands lore a "disclosure plan" as a lore-owned world-bible record, while lore's own current coverage map lists that exact surface as `uncovered` and its own queued source says the two must be kept apart.**

The amendment's `couples:` line and its §6 both assert, in the present tense and as a settled ownership, that a disclosure plan is a record lore owns:

- `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md:12` — "where a derived ladder and a disclosure plan become world-bible records that lore owns" (14 tokens, 86 chars)
- `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md:91` — "the derived ladder, the laws behind it and any disclosure plan are records for a world bible, which `synthesis/worldbible-integration-contract.md` hands to lore"

Lore's current corpus says the opposite about the *record class*, not just the state:

- `lore-shokunin/corpus/README.md:72` — "CM-f | reveal (narrative) order vs chronology | uncovered | none — zero governing hits for spoiler/reveal order/narrative order/fabula/syuzhet in knowledge or SKILL"
- `lore-shokunin/corpus/README.md:90` — the CM-f frontier: "the schema encodes integer event ticks only; nothing separates reader-facing reveal order from event order, so spoiler/discourse-order errors are uncheckable"
- `lore-shokunin/corpus/SOURCES.md:18` (S010, queued) — "A reader-belief graph is a different object from an authorial canon graph; reveal-order and character-knowledge work must keep the two apart."

A "disclosure plan" (when the reader is told what, across roughly twenty chapters — `…amend…md:58`, 「把它放在前面大概20章之内慢慢来，我觉得是问题不大的。」, 1 token / 27 chars) **is** reader-facing reveal order. Lore's schema has no field for it: `lore-shokunin/corpus/fixtures/check_bible.py:26-32` defines `sources`, `entities`, `relations`, `timeline` (integer `tick` only), `contradictions` — nothing for a per-chapter reader-reveal schedule.

Two things are therefore true at once, and w1 recorded only the first:
1. **w1's demarcation still holds**: the disclosure schedule is *authorial pacing advice* (a tier-C lead), and kotodama does not claim to verify reveal order. `…amend…md:88` says so — "rests on one tier-C row and is a lead", "never quotable as a rule of serial fiction" (two spans from the same sentence, each verbatim; the whole sentence is 27 tokens, so it is quoted in two parts to stay inside the 25-token cap).
2. **but the landed text asserts an ownership transfer that lore's own current map contradicts.** w1 §3.1 Contact Point C read the staged bytes, where the amendment had **zero** occurrences of `lore|handoff|worldbible|contract`; the landed amendment has three. The coupling line naming "a disclosure plan" as a lore-owned record is **new text introduced at landing** and lands exactly on lore's open CM-f frontier.

This is the *same* contradiction w1 §5.2 raised — "Both lanes now treat 'order of disclosure to reader' as an explicit subject" — but the landed bytes make it concrete in a way the staged bytes did not, and w1's proposed mitigation (a lesson section) was never applied (F3).

**F3 (MEDIUM) — w1's proposed mitigation was never applied, and the lesson file records zero sibling/boundary content.**

w1 §6 proposed appending a "Sibling overlap and lore boundary (round-74 w1 connector scan)" section to `corpus/lessons/round-74.md`. Measured at the landed lesson and at head:

```
$ grep -c -iE 'sibling|boundary|CM-f|CM-g|lore' corpus/lessons/round-74.md
0
$ grep -rn 'Sibling overlap and lore boundary' . --include='*.md'
./.ufo/waves/round-74/w1/ConnectorSiblings.md:115:### Sibling overlap and lore boundary (round-74 w1 connector scan)
```

The only place the boundary is written is the wave-1 seat file, which is **not a durable corpus surface** (`.ufo/waves/` is scratch). The durable surfaces that would carry it are empty of a round-74 boundary record:

```
$ for f in corpus/lessons/round-74.md corpus/README.md LOG.md SCORECARD.md PROVINCE.md SKILL.md; do
    printf "%-30s %s\n" "$f" "$(grep -c -iE 'sibling overlap|CM-f|CM-g|kotodama-lore-adjacency' "$f")"
  done
corpus/lessons/round-74.md     0
corpus/README.md               0
LOG.md                         0
SCORECARD.md                   1
PROVINCE.md                    0
SKILL.md                       0
```

The single SCORECARD hit is `SCORECARD.md:1285`, and it is **not** a round-74 record: it is the round-66 axes row ("## Axes — round 66 … L1 KotodamaR66") citing that round's own `w1/ConnectorSiblings.md` and `w1/RevLoreHandoff.md` (both present under `.ufo/waves/round-66/w1/`; the round-74 tree has a `w1/ConnectorSiblings.md` but **no** `w1/RevLoreHandoff.md`). It predates this round and carries no CM-f/CM-g demarcation. `corpus/README.md` does mention "lore" 41 times and `LOG.md` 17 times, but those are prior rounds' contract/handoff history — none of them is a round-74 sibling-overlap or CM-f/CM-g record.

The landed base entry's own `couples:` line does point at the contract (`…worldbuilding-setting-practice.md:12`), and the base entry §9 says "the checklist that owns conflict and variant statuses takes a note like this as its input and hands findings to lore" (`:255`) — but neither states that lore's world-bible verification is *lore's* to rule on and that the entries decide no canon in a way the reader can check. The base entry's `refuses:` (`:14`) does say "canon for any world", and `scope:` (`:13`) says "it decides no world's canon" — that part is correctly recorded in the entry itself.

So the residual is narrow and specific: **the CM-f/CM-g demarcation and the "handoff is unactivated" status are recorded nowhere durable**, while the entries assert an active handoff in present tense.

**F4 (MEDIUM) — the contract the entries couple to is, by lore's own current record, unactivated and unacknowledged; the entries do not say so.**

- `lore-shokunin/corpus/README.md:79` — "CM-g kotodama packet intake is uncovered: contract `kotodama-lore-adjacency` sits at unacknowledged digest 5f4c02bf… and lore holds zero durable-surface acknowledgement records." (13 tokens / 115 chars)
- Verified: `git -C lore-shokunin grep -l 'kotodama-lore-adjacency' -- corpus/knowledge SKILL.md` → **exit 1, no files match**; the digest claim is live — the current file hashes `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`, matching lore's recorded `5f4c02bf`.
- `lore-shokunin/corpus/README.md:73` — CM-g "uncovered"; `lore-shokunin/PROVINCE.md:19` — "CM-f reveal order vs chronology and CM-g kotodama packet intake stay `uncovered`".
- The contract itself says the same: `corpus/knowledge/synthesis/worldbible-integration-contract.md:15` — "Initial bilateral acknowledgement is **pending** until those records exist; writing this file is not a substitute for lore's read." (19 tokens / 130 chars) and `:14` (both lanes must record `lane, contract_id, revision, file_sha256, reader, read_at, evidence_pointer` before the first transfer; 24 tokens / 178 chars verbatim).

So the base entry's `couples:` line (`:12`) naming the contract, and its §10 "Hand off under `synthesis/worldbible-integration-contract.md`" (`:265`), describe a conduit lore has not activated and has not acknowledged. The contract's own §1 makes acknowledgement a **precondition of the first transfer**, and lore's side of it is empty. This is w1's §4 analysis, re-verified and still true — and it is the correct provincial reading.

**What must stay reported-not-absorbed (the durable reading, with paths):**
1. **Fictional canon — lore's alone.** `lore-shokunin/PROVINCE.md:3`, `kotodama-shokunin/PROVINCE.md:16` ("Refuses: claiming or recording canon — that is lore-shokunin"). Both landed entries honour it (`…practice.md:13-14`, `…amend…md:13`).
2. **World-bible consistency verification — lore's alone.** `lore-shokunin/PROVINCE.md:17` (CM-01…CM-12), `lore-shokunin/corpus/fixtures/check_bible.py:26-32`. Kotodama's `synthesis/consistency-verification-checklist.md:2` already routes findings to lore and stops at handoff — that is the right shape and it is a **lane-internal** checklist, not the new entries'.
3. **Reveal-order / disclosure scheduling — must stay a practitioner lead, never a lore record.** `lore-shokunin/corpus/README.md:72,90`; `lore-shokunin/corpus/SOURCES.md:18`. Kotodama's amendment already grades it tier-C and non-binding (`:51`, `:88`); the *coupling* wording at `:12` and `:91` is what must be narrowed.
4. **The handoff is one-way and unactivated.** Contract `:124-137` (§8 transfer procedure) is pull-based — "Lore supplies a scoped brief… absent inputs become explicit questions" (`:126`); `:69` (unbound research packet may be retained as reference but cannot be imported as canon without a lore baseline and a new reviewed handoff); `:165` (both-lanes-claim-ownership escalates to the integrator).

**Is any L0 question warranted?** **No new L0.** The contract's own §10 route (`:159-172`) is the lane-correct escalation path for the CM-f boundary, and the L0 queue already carries the open thread: `.ufo/l0-questions.md:45` — "kotodama | round-8 | worldbible-integration-contract digest drift vs lore's open round-93 ratification — who owns the contract digest update, and does lore's r93 ratification subsume it?" — and lore's own `lore-shokunin/l0-questions.md:5-7` (round-89/93 lines on the same digest). A new L0 row would duplicate an open question. What is missing is not an operator ruling but a **lane-internal correction of two coupling sentences** — the kind of thing the connector seat can record in the round lesson and the entries' `couples:`/`scope:` fields.

---

## 3. New overlap created by the landed files

**No new sibling overlap.** Measured (F-table in §1): all 20 sibling lanes 0 for the discriminating term set; lore 0; no sibling registry carries S881–S884.

**F1 (MEDIUM) — the w1 report's own verification recipe is unreproducible, and its two cited anchors are stale because kotoba moved under the round.**

The w1 report's §8 verification block prints:

```
grep -riE 'worldview|world-view|worldbuilding|setting-note|世界観|世界观|設定ノート' \
  /home/vgpnk/Projects/shokunin/*-shokunin/corpus/knowledge/
```
with "*Expected outcome:* 0 matches". Run verbatim at the current tree this returns **171** matching lines, not 0 — because the glob includes kotodama-shokunin's own tree, whose base already carried 87 files matching that six-term set (149 lines) and now carries 89 files. The w1 body text (§1.3, §2 "0 matches" per sibling) is the correct reading — it is the *recipe* that cannot produce its own stated outcome, because it does not exclude the subject lane. A reviewer copying §8 verbatim would see 171 hits and could not tell them from a real sibling collision. Corrected command and its output are in §5 below.

The same recipe's §8.3 anchor is stale for the same reason — kotoba landed its **own** round-74 during this round (`2c81137`, 2026-10-25 23:27:34, "PROVINCE Adjacent re-pin"), after w1 was frozen at `de93d91` (20:47:05). At w1's writing time the kotodama row in `kotoba-shokunin/PROVINCE.md` was at **line 61** with the text "worldbuilding and naming"; it is now at **line 66** with different text, and the phrase "worldbuilding and naming" no longer occurs in kotoba's PROVINCE at all:

```
$ git -C kotoba-shokunin show a0f7f17:PROVINCE.md | grep -n '^| kotodama '
61:| kotodama | adjacent | 35f0d49f96f1d51f8b006136a8e1d0e8d0919a7a | worldbuilding and naming; …
$ grep -c 'worldbuilding and naming' kotoba-shokunin/PROVINCE.md
0
$ grep -n '^| kotodama ' kotoba-shokunin/PROVINCE.md
66:| kotodama | adjacent | f7104cbce186bc2e1522abf0cfd619cc834628bb | kotodama owns generative linguistic-cultural worldbuilding …
```

Consequence for the round: kotoba's new row quotes kotodama's **base** `SKILL.md:3` (`35f0d49f` = `f7104cbc` pin), which is byte-identical at base and at the C lands — so kotoba's scope quote still describes kotodama accurately, and kotoba's own census row for kotodama carries the string "worldbuilding" twice (`kotoba-shokunin/corpus/knowledge/sibling-overlap-census-round74.md:63` and `:94`). Those two hits are the *only* sibling-tree matches for the six-term set anywhere in the fleet, and they are a **sibling quoting kotodama's own scope description back**, not a scope contest. That is why the final discriminating sweep in §1 returns 0: it filters on the landed files' distinguishing strings, which kotoba does not carry.

**F5 (LOW) — the landed base entry's `couples:` line names two sibling-free lanes correctly, but its §9/§10 wording overstates what lore has accepted.** Already covered by F3/F4; recorded here because it is the *text-level* carrier: `…worldbuilding-setting-practice.md:255` ("hands findings to lore") and `:265` ("lore decides which of them a given world adopts, records the canon, and verifies consistency"). The second half of `:265` is accurate as a statement of the *contract's* division of labour and is the line w1 analysed; what is missing is the activation qualifier.

---

## 4. ATTACKS THAT FAILED (the claim and the w1 verdict survived)

| attack | result | evidence |
|---|---|---|
| A1. A sibling lane contests the setting-practice surface | **FAILED** | §1 sweep: 20/20 siblings 0 for filename + both topic texts + three hosts + `設定ノート`/`設定資料集` + `worldview`/`world-view`; lore 0 |
| A2. A sibling registry now carries S881–S884 (id collision) | **FAILED** | `grep -rlE '^\| ?S(881|882|883|884) ' *-shokunin/corpus/SOURCES.md` → only `kotodama-shokunin/corpus/SOURCES.md`; sibling id spaces are independent and much lower (lore max S032, chousa S112, kotoba S225, tameshi S264) |
| A3. Lore has acknowledged the contract / CM-f is now governed | **FAILED** | `git -C lore-shokunin grep -l 'kotodama-lore-adjacency' -- corpus/knowledge SKILL.md` → exit 1; `lore/corpus/README.md:72,73` both `uncovered`; digest `5f4c02bf` still the recorded one and still the file's actual hash |
| A4. The kotoba row now says kotodama owns setting practice (a new contest) | **FAILED** | `kotoba-shokunin/PROVINCE.md:66` names only "generative linguistic-cultural worldbuilding"; kotoba's own domain is "prompt & skill craft" (`PROVINCE.md:3`); the two new entries touch neither SKILL.md shape nor trigger fidelity |
| A5. The w1 §8.2/§8.3 verification commands are wrong about lore | **FAILED** (they are right) | `grep -nE 'CM-[fg]\|kotodama-lore-adjacency' lore/corpus/README.md` → `:72 :73 :79 :90 :94`; `grep -n 'Adjacent contract' kotodama/PROVINCE.md` → `:22`; `grep -n 'kotodama' lore/PROVINCE.md` → `:19 :23 :28` — all three as w1 cited them |
| A6. The claim's GROUND leg is blind to sibling overlap | **CONFIRMED, not refuted** | `accept-c.py:1358-1416` re-derives the gap only inside kotodama's own base tree (`mat_base`, `corpus/knowledge`) and its registry; no sibling path is read. The counter cannot see a sibling claim; this connector scan is the only fleet-wide instrument. w1 §5.3 stated this correctly |
| A7. Contract citations in w1 are misnumbered | **FAILED** | `contract:11` (contract id), `:17` (ownership split), `:38` (work-item table), `:58` (`baseline_bible_ref` row), `:126` (§8 step 1 pull-model), `:209` (§13 division of labour), `:14-15` (§1 read/acknowledgement), `:69` (§4.69 unbound-packet rule) — all confirmed at those exact lines |
| A8. The claim's C counter fails | **FAILED** | `ACCEPT-C-74: PASS legs=13/13` at `c4bf61a` in an isolated clone |

---

## 5. Reproducible verification commands

Run from the fleet root `/home/vgpnk/Projects/shokunin`. All are read-only.

**V1 — the corrected fleet-wide sibling scan (w1 §8.1 with the subject lane excluded; this is the form that yields 0):**
```bash
for d in /home/vgpnk/Projects/shokunin/*-shokunin; do
  [ "$(basename "$d")" = "kotodama-shokunin" ] && continue
  n=$(grep -rilE 'worldbuilding-setting-practice|build order one Chinese web-fiction author|Japanese practitioner craft of specifying a setting|litmemo|tuduku|chinawriter|設定ノート|設定資料集|worldview|world-view' "$d/corpus/" 2>/dev/null | wc -l)
  printf "%-22s %s\n" "$(basename "$d")" "$n"
done
```
Expected: `0` for all 20 siblings (output in §1).

**V2 — why the uncorrected form fails (F1):**
```bash
grep -riE 'worldview|world-view|worldbuilding|setting-note|世界观|世界观|設定ノート' \
  /home/vgpnk/Projects/shokunin/*-shokunin/corpus/knowledge/ | wc -l     # → 171, not 0
cd /tmp/r74base && grep -rilE 'worldview|world-view|worldbuilding|setting-note|世界观|世界观|設定ノート' corpus/knowledge/ | wc -l   # → 87 files (149 lines) at base
```
The 87 base files are kotodama's own: 72 match on the English word `worldbuilding` alone (`corpus/knowledge/civilizations/*.md`, `corpus/knowledge/culture-material/*` etc.) and the other 15 on `worldview` alone (`civilizations/africa-primary-sources.md`, `linguistics/morphological-typology.md`, `synthesis/cultural-translation-protocol.md`, …); **0** match the CJK terms. The claim's own `ground` fragments (`litmemo.com`, `tuduku.space`, `chinawriter.com.cn`) and CJK terms are the discriminating set, and those are 0 at base — which is why claim C's GROUND leg is sound and why the CJK-only reading is the right one.

**V3 — lore's CM-g acknowledgement state (F4):**
```bash
git -C /home/vgpnk/Projects/shokunin/lore-shokunin grep -l 'kotodama-lore-adjacency' -- corpus/knowledge SKILL.md; echo "exit=$?"
# → exit=1, no files match
sha256sum /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md | cut -c1-16
# → 5f4c02bfc4e6e4e9   (matches lore/corpus/README.md:79's recorded digest)
grep -nE 'CM-[fg]|kotodama-lore-adjacency' /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/README.md
# → :72 CM-f uncovered, :73 CM-g uncovered, :79 digest, :90 CM-f frontier, :94 packet-intake frontier
```

**V4 — the F2 coupling sentences and lore's contrary record:**
```bash
sed -n '12p;91p' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
sed -n '72p;90p' /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/README.md
sed -n '18p' /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/SOURCES.md
sed -n '26,32p' /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/check_bible.py
```

**V5 — F3 (no durable boundary record):**
```bash
grep -c -iE 'sibling|boundary|CM-f|CM-g|lore' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/lessons/round-74.md   # → 0
grep -rn 'Sibling overlap and lore boundary' /home/vgpnk/Projects/shokunin/kotodama-shokunin --include='*.md'                   # → only the w1 scratch file
```
The lesson's `## Gate` / `## Quarantine` / `## Mistakes` sections do carry `S883` (15 occurrences) and `S884` (15) — but those are the *lane* ids for the chinawriter documents, and `S899` (6) / `S900` (5) appear alongside them only as the *campaign* ids being refused. None of these lines is a sibling-overlap or CM-f/CM-g boundary line: the lesson carries no sibling, boundary, CM-f or CM-g mention at all.

**V6 — F1 (stale kotoba anchor):**
```bash
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show a0f7f17:PROVINCE.md | grep -n '^| kotodama '   # → 61
grep -n '^| kotodama ' /home/vgpnk/Projects/shokunin/kotoba-shokunin/PROVINCE.md                        # → 66
grep -c 'worldbuilding and naming' /home/vgpnk/Projects/shokunin/kotoba-shokunin/PROVINCE.md          # → 0
```

---

## 6. Affected axes

* **Coverage (C):** unaffected by this seat — no sibling holds this ground; claim C's counter is green at its own landing. The finding here is *not* a coverage failure.
* **Calibration (Ca):** the affected axis. F2–F4 are calibration defects: the durable corpus asserts a lore-owned record class and an active handoff that lore's own current map and the contract's own activation clause contradict. Ca's counter cannot see this (it reads only kotodama's tree), and Ca is red at the combined tree for an unrelated reason, so the lane-level fix must not be routed through Ca's leg set.
* **Coverage axis (C) is also affected in one narrow, provable way:** the landed `couples:` line names a lore-owned record class that no lane's corpus defines a schema for (`check_bible.py:26-32`).

## 7. Proposed fix (one, bounded) — **RECOMMENDED, NOT APPLIED**

This seat is a read-only connector: it does not edit the lane. The proposed move is for the lane's L1/scribe.

**Append a bounded "Sibling overlap and lore boundary" section to `corpus/lessons/round-74.md`** (the exact surface w1 §6 named), **and** narrow two sentences in the landed amendment's coupling language. Both halves are needed: the lesson carries the fleet-wide evidence (which only a connector seat can gather), the entry carries the machine-visible qualifier.

1. `corpus/lessons/round-74.md` — append (after `## Routed to round 75`, so the existing `## Gate` / `## Quarantine` / `## Mistakes` sections keep their bytes and the GATE/REJECTS legs are unaffected) a section recording, with the paths above:
   - the fleet-wide sibling scan result (20/20 siblings 0 for the discriminating term set; the only two hits anywhere are kotoba quoting kotodama's own scope description back at `sibling-overlap-census-round74.md:63,94`);
   - the CM-f demarcation: the disclosure schedule is a tier-C authorial lead (`…amend…md:51,88`), **not** a lore record; lore's `CM-f` stays `uncovered` (`lore/corpus/README.md:72,90`) and lore's queued S010 keeps reader-belief and canon-graph work apart (`lore/corpus/SOURCES.md:18`);
   - the activation status: the contract is at unacknowledged digest `5f4c02bf` with zero lore acknowledgement records (`lore/corpus/README.md:79`; contract `:14-15`), so no packet is owed and none is transmitted;
   - the contract's own pull-based route (`contract:126`) and §10 escalation (`:159-172`).
2. Narrow the amendment's coupling so it asserts a **procedure**, not an **ownership already granted**: at `…amend…md:12` and `:91`, replace "become world-bible records that lore owns" / "hands to lore" with wording that makes the handoff conditional on lore's contract activation ("a lore-owned record *class*, pending the contract's activation, if lore requests it under §8"). Keep `:88` (the tier-C lead) and keep `:13` (`scope:` refuses canon) as they stand.
3. Mirror the same qualifier in the base entry's `couples:`/§10 (`…worldbuilding-setting-practice.md:12,255,265`) so the two files agree.

**Containment / risk.**
* **Do not** edit `…amend…md` `couples:`/`scope:` in a way that changes the header field *order* or the `- topic:` text: claim C's INDEX leg reads `corpus/README.md` rows and requires each row body to be the entry's own `- topic:` text **verbatim** (`accept-c.py` INDEX leg). Editing `couples:` is safe for INDEX; editing `topic:` is not, without also editing the README row — and the README is byte-checked by INDEX.
* `accept-c.py` has **no** sha256 pin on either entry file (no `entry sha256`/`DIGEST` constant exists in the counter; the ENTRIES leg is a shape/length gate, `accept-c.py:747-780`), so narrowing `couples:` does not by itself break the C counter. It does change the entry bytes, so the GATE/REJECTS/INDEX legs must be re-run at the new lands.
* The lesson append must not touch the `## Gate`, `## Quarantine` or `## Mistakes` sections: the GATE leg parses the `## Gate` block specifically (`accept-c.py:400-414`, `gate_section`), and REJECTS reads `refused_staged` ids and each family's reason+flip across the whole file (`accept-c.py:1279-1310+`). Appending after `## Routed to round 75` keeps both parsers' inputs byte-identical.
* Ca's APPENDONLY leg covers `corpus/lessons/round-74.md` as a protected file with **zero removed lines** required (`accept-ca.py` APPENDONLY, `protected=[… 'corpus/lessons/round-74.md' …]`). An append satisfies that; a rewrite of any existing line does not.
* **No L0 row** (see §2): the open thread is already at `.ufo/l0-questions.md:45` and `lore/l0-questions.md:5-7`; this is a lane-internal correction plus a §10-routeable boundary note, not an operator decision.
* **Do not** touch the contract file: its digest `5f4c02bf` is what lore's `corpus/README.md:79` records; changing it re-opens the drift question the round-8 L0 already carries.

## 8. Tooling record

* No tools installed, removed, or updated. `pacman` was **not** invoked (host-wide pause, orchestrator ruling 2026-10-20).
* No web fetch was performed by this seat; every source of evidence is a local file or a `git` object. No UA was needed and no "no capture" ruling is made here (the CDX/no-capture discipline belongs to the scout seats that re-opened S881–S884).
* Scratch used: `/tmp/r74base` (a clone of the lane checked out at base `f7104cb`) and two `mktemp -d` clones used for the counter re-runs; the fleet repo was not written to.
* The lane repo was read only. The single file this seat wrote is this report, under the assigned path `.ufo/waves/round-74/w2/ConnectorAdjacency.md`.
