# R8-F08 — freshness recheck receipt (companion)

- **id:** R8-F08 · **targets_index:** freshness[7] · **prior row:** R6-06-B (round 6, SOURCE SCOUT worker 06)
- **entry:** `corpus/knowledge/civilizations/china-shang-zhou.md` (line 116 bi/cong formula → now line 117; line 99 rank-ladder caution → now line 100; shift explained below)
- **entry sha256 at receipt:** `905710ba79bb8c7ceae7f42562d5ae8177f14988d2f7c78ce0a14b619dfccb0b` — **equal** to the round-6 baseline hash recorded in `corpus/lessons/round-6-sources/06.json` (`entry_sha256_before`) when this receipt checked it.
- **entry sha256 live at handoff:** `334f935b0759c8122fb992f0ec005fc1665b8975cdfb065d9460bbbfd2bef899` — after this receipt's hash check, the round-8 metadata-sweep shard inserted **one frontmatter line** (`- source: the sources ledger above — …`); `git diff --stat` for the file = 1 insertion, frontmatter only. The receipted body claims are unchanged in content and shifted by one line (99→100, 116→117). This F-shard touched no corpus bytes and made no tracked modifications.
- **accessed-at:** 2026-10-17 (status sweep at `2026-10-17T20:13:15Z`)
- **receipt_head:** `7cbce6c3d638b3749c73c7b2864c7d3795dcfa81` = sha1 of the canonical JSON of the prior row R6-06-B. Re-check with:
  `python3 -c "import json,hashlib; d=json.load(open('corpus/lessons/round-6-sources/06.json')); r=[a for a in d['audits'] if a['id']=='R6-06-B'][0]; print(hashlib.sha1(json.dumps(r,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest())"`
  The sibling R8-F09 receipt's `receipt_head` could not be reproduced by any construction tested, so the definition used here is stated explicitly.

## Verdict

**partial-support (upgraded).** Raw round-6 label preserved: verdict `supported`, `support_scope` `partial` (targets.json reconciled label: `partial-support`).

Round 6 confirmed only that the transcription contains the cited formula and prescriptive language; it explicitly left the compilation date, the Neolithic/Shang meaning and any critical apparatus unread. This round retrieves passages for **both named limits** plus a fresh main-source retrieval. Passage support is kept separate from whole-claim support.

## Legs (each with source, location, what it supports and what it does not)

### 1. Formula wording and attribution — re-verified
- **Source:** Wikisource 周禮/春官宗伯, HTTP 200 (curl sweep), 196,564 bytes on re-fetch.
- **Location:** 大宗伯之職 section, clause `以玉作六器，以禮天地四方…`.
- **Excerpt:** `以玉作六器，以禮天地四方：以蒼璧禮天，以黃琮禮地，以青圭禮東方，以赤璋禮南方，以白琥禮西方，以玄璜禮北方。皆有牲幣，各放其器之色。`
- **Supports:** the entry's attribution of `以蒼璧禮天，以黃琮禮地` to 春官宗伯 as transmitted text — verbatim, fresh, dated. Adds the full six-jade scheme and the `皆有牲幣` clause round 6 did not quote.
- **Does not support:** any dating of the text or any meaning for any excavated object; this page carries no apparatus.

### 2. Prescriptive genre incl. numerical ladders
- **Same page.** `以九儀之命正邦國之位：壹命受職…九命作伯`; `以玉作六瑞，以等邦國：王執鎮圭…男執蒲璧`; 典命 `上公九命為伯，其國家、宮室、車旗、衣服、禮儀，皆以九為節` (侯伯七命, 子男五命); 司服 graded 冕服 code.
- **Supports:** the entry's line 99/116 warning — these are imperative prescriptions (`以…正邦國之位`, `以等邦國`), not records of an excavated assemblage.
- **Does not support:** practice in any period.

### 3. "A later prescriptive text" — compilation date (prior limit #1, now covered)
- **chinaknowledge.de** (Ulrich Theobald; cites Boltz 1993, Liu Qiyu 1992, Nylan 2001): *"It was compiled during the Warring States period 戰國 (5th cent.-221 BCE)"*; records the controversy — *"Zheng Xuan believed in the authenticity of the Zhouli as a book compiled on the order of the Duke of Zhou…, while many others considered it to be a forgery or a text concocted at a much later date"* — and concludes *"only a few parts of the text were compiled during the Han…"*.
- **Wikipedia, Rites of Zhou** (oldid 1352754096): *"the majority follow Qian Mu and Gu Jiegang in assigning the work to about the 3rd century BC"*; Yu Yingshi's late-Warring-States argument; "Zhou" = royal State of Zhou reading.
- **四庫全書總目提要 卷019**, 《周禮注疏》 entry: `《周禮》一書，上自河間獻王。於諸經之中，其出最晚。其真偽亦紛如聚訟`.
- **Supports:** the "later" half of line 116 — majority dating puts the transmitted text centuries after the Neolithic/Shang specimens.
- **Does not support:** a single agreed date; a date for the bi/cong clause individually; the forgery theory as fact.

### 4. Neolithic/Shang original meaning — non-projection caution (prior limit #2, now covered)
- **World History Encyclopedia, "Liangzhu Culture Jade"** (author meta tag: Joshua J. Mark): *"there is no documentation from the Liangzhu Culture linking the objects directly to the concepts of earth and heaven. The earth-heaven motif is understood to have developed later during the Shang Dynasty, and those who challenge a cosmological interpretation of the cong and bi point out that one cannot interpret Neolithic artwork from the later perspective of the Shang."* Also records that the Childs-Johnson cosmological reading is *"by no means accepted universally"*.
- **Bogna Łakomska, "The meaning of animal motifs in Neolithic China…", Art of the Orient 9 (2020): 7–26** (heiJOURNALS PDF): *"Congs may have been used in Earth's thanksgiving rituals. The form of the earth was then perceived as rectangular and the sky as round."* and the competing hypotheses: *"As suggested by David Keightley, the congs… could have been used as a 'stalk container for offering plants', or, as Deng Shuping suggests, plinths, or joints for wooden posts."*
- **Jessica Rawson, Life and Afterlife in Ancient China (2023), publisher sample, Introduction p. xxii:** *"The abundant transmitted writings, generally taken as the foundation of early history, were not usually from the same time as the events they described. They were compiled, sometimes centuries later, handed down and edited over hundreds of years."*
- **Supports:** the entry's caution — the Heaven/Earth reading is a later-dated interpretive layer with no Liangzhu documentation, competing function hypotheses exist, and transmitted texts post-date the events they describe (stated by the entry's own R95 author).
- **Does not support:** what any specific specimen meant. The Lopes 2014 abstract (UH Press) frames the debate generally and does **not** itself state the cong/bi argument (sweep S4).

### 5. Critical apparatus and textual variants (prior limit #3, now covered)
- **欽定周官義疏 (四庫全書本), 卷首** — 御製三禮義疏序 (乾隆十三年 = 1748), 凡例, 目録, and closing collation note (乾隆四十年九月, 總纂官紀昀等):
  - variants listed: `一周官有古文今文異本…其杜子春鄭司農所讀有異同者竝列焉` (故書/古文 vs 今文 readings collated);
  - the lost chapter ruled on: `漢人以考工記附之名曰冬官非其實也` (the Han substitution of the Kaogongji for the 冬官 "is not the fact");
  - seven rubric classes 正義/辨正/通論/餘論/存疑/存異/總論.
- **四庫全書總目提要 卷019** — 《周禮注疏》: `《周禮》一書不盡原文，而非出依託，可概睹矣。` plus concrete contradictions with other classics (`《儀禮•聘禮》…與《掌客》之文不同`; `《大射禮》…與《司射》之文不同`; `《禮記•雜記》…與《典瑞》之文不同`; `《禮器》…與《司幾筵》之文不同`) and internal dating of the 考工記 (`鄭之刀`/`秦無廬` → `其非周公之舊典，已無疑義`). 《欽定周官義疏》 entry: `其源確出周公，而流傳既久，不免有所竄亂`.
- **Supports:** the entry's requirement of "a dated textual argument" — the transmitted text has a documented editorial/variant history and a worked example of internal dating.
- **Does not support:** a modern collation; the apparatus is an 18th-century imperial product with its own commitments.

## Negative sweeps (each command run 2026-10-17 against real page bytes)

| # | claim | result |
|---|---|---|
| S1 | Wikisource 春官宗伯 carries no compilation-date/authorship statement | 196,564 bytes fetched; `戰國\|秦漢\|成書\|周公\|六國\|年代\|作於` → 0 matches |
| S2 | chinaknowledge Zhouli page does not address Neolithic jade meaning | 20,817 bytes; `neolithic\|liangzhu\|jade disc\|jade tube` → 0 matches |
| S3 | WHE Liangzhu article does not cite the Zhouli/春官宗伯 clause | 202,473 bytes; `zhouli\|rites of zhou\|zhou li\|zongbo\|chun guan\|chunguan` → 0 matches |
| S4 | Lopes 2014 abstract does not state the cong/bi Heaven-Earth argument | 122,368 bytes; `cong\|liangzhu\|bi disc\|heaven` → 0 matches |

## Blocked access (documented failures — legitimate receipts)

- `ctext.org/rites-of-zhou/chun-guan-zong-bo` — HTTP 200 but anti-scraping interstitial; no passage.
- `researchgate.net/publication/287955376` — FetchURL 403.
- `jstor.org/stable/24569921` — 200 but "Client Challenge" bot wall.
- `api.semanticscholar.org/…CorpusID:96457018` — 429.
- `hasp.ub.uni-heidelberg.de/journals/ao/article/view/16113` (landing page) — bot wall; direct PDF path succeeded (200) and was used.
- `metmuseum.org/art/collection/search/44783` — 429 (round-6 repeat).
- `smarthistory.org/tomb-of-fu-hao/` — 403 (round-6 repeat).
- `britannica.com/topic/Zhouli` — 403 (round-6 repeat).

## Whole-claim support

**Supported this round:** formula wording/attribution; prescriptive genre incl. rank ladders; "later prescriptive text" dating; both named prior limits (compilation date; critical apparatus/variants); the non-projection caution now carries retrieved scholarly wording.

**Not established:** any intention/application of the formula to Neolithic or Shang specimens; a single compilation date (or a date for the clause itself); object-level evidence (Met/Smarthistory still blocked); a modern critical edition.

## Limits

No first-hand Neolithic/Shang object or inscription record retrieved this round; no modern critical edition inspected; the clause is not individually dated by any source; Wikisource proofreading-status banner not located (grep for quality/proofread markers → no match); classical Chinese read without a published translation (gloss is the worker's own); chinaknowledge is a reference work (not peer-reviewed) and WHE is tertiary; the Łakomska journal identification rests on the repository path plus a citing source because the landing page was bot-walled.

## Handoff

Verdict **partial-support (upgraded)**; raw label `supported` preserved. Both prior limits are now receipted, so the entry's line-116 caution stands unchanged and is better evidenced; strongest retrieved anchors if the entry ever cites its dating support: chinaknowledge + 欽定周官義疏 凡例. Open item for the parent: an object-level Neolithic/Shang jade record (Met/Smarthistory re-fetch still blocked). No corpus bytes touched; no shared bookkeeping written.
