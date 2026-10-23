# ScoutCaptionRows — caption re-scope candidates and tier-C sole support

Recon only. No SOURCES, knowledge, or tool edits. No installs. Revision read: working tree of `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (round-62 base named in the brief as `f0173481047a93c46798f90b68d71d4f169d2642`; this seat did not run git).

Axes kept: recall of real caption/label locators; precision against lexical "label" and depiction "image"; sole-support as a knowledge-line fact, not as the W01 predicate.

## How counted

Registry parse of `corpus/SOURCES.md` `## Registry`: 619 data rows, every row 11 cells, 0 malformed. Cells used for the pattern are **anchor** and **teaches** only.

Broad pattern (case-insensitive): `caption`, `alt text`, `thumbnail`, `image caption`, `label`/`labels`, `image`/`images`. **51 rows.**

Knowledge citations: `\bS\d{3,}\b` on every line under `corpus/knowledge/**/*.md`. A line is sole support when that is its only S-id.

Census (W01 only):

```
timeout 180 bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
```

piped to awk field 2 == `W01`. Pipeline exit 0. Complete W01 stdout:

```
kotodama	W01	S687 tierC mined used-by=corpus/knowledge/culture-material/footwear-codes-terminology.md
```

W01 in `scripts/sources-census.sh` (around line 669) is `tier==C && status==mined && used-by != —`. It does **not** test "only id on the line".

`alt text`: 0 registry rows. `thumbnail`: 0 registry rows. The round-61 note that S665's quote sits in `thumbnail-description` is in `corpus/lessons/round-61-verifier-spotcheck.md` §5, not in the row.

## Candidates (later caption re-scope)

A candidate is a row whose anchor or teaches locates the quoted words in a caption, a figure/table/photo caption, or a gallery / object / overview label. Fifteen rows. Two further "label" hits are listed as borderlines, not as the S665 class.

### A. Whole anchor is the caption or gallery label — footwear, each line sole

Same failure class as round-61 §7 item 1 (S665): the entry can read as body fact.

| id | tier | status | SOURCES line | knowledge line | entry names caption/label? |
|---|---|---|---|---|---|
| S665 | A | mined | 620 | `footwear-codes-terminology.md:74` sole | No. Teaches does: "The museum caption says…". Anchor: `Persian, 17th century image caption: "The heel was not a European invention…"`. Already routed. |
| S663 | B | mined | 618 | `:72` sole | No. Anchor is only `‘Oldest item in the collection’ caption: "The red heels and soles…"`. Teaches says "The FIT page associates…". |
| S661 | A | mined | 616 | `:70` sole | No. Anchor is only the 2015–2016 gallery label `‘On a Pedestal’` (chopines hidden under skirts). Teaches drops "label". |
| S677 | A | mined | 632 | `:78` sole | No. Teaches keeps "the V&A label says". Anchor is only the gallery label `‘Silver Sandals for the Bride’`. |
| S673 | A | mined | 628 | `:58` sole | **Yes.** Line is `The caption lists Nêhiyawak moccasins…`. Anchor is only `Caption: "Moccasins, Nêhiyawak, 1920…"`. Already scoped; still caption-sourced. |

Entry lines, observed:

- `:58` `- The caption lists Nêhiyawak moccasins dated 1920 as a gift of the Art Association of Montreal. (S673)`
- `:70` `- Higher chopines hidden under skirts required more dress cloth and signaled status. (S661)`
- `:72` `- The red heels and soles of latchet shoes were associated with Louis XIV and his court. (S663)`
- `:74` `- A heel originated in Western Asia for horseback riding before Europeans adopted it. (S665)`
- `:78` `- A bride might receive toe-knob paduka among the often extravagant presents. (S677)`

### B. Borderline "label" (not caption-only on the row's own wording)

- **S674** A mined, SOURCES line 629, `footwear-codes-terminology.md:59` sole: `- A child's kamik made over 2,500 years ago is among the oldest footwear found in the Canadian Arctic. (S674)`. Anchor: `story paragraph below the 2500 Years Ago label:` plus the quote. The row says the quote is the story paragraph, not the label. Do not treat as caption-only without a re-open.
- **S278** B mined, SOURCES line 307. Teaches: "this label says the kavat is the mask that is *not* burned". Scope also says "its label's account". Anchor calls the text `Commentary`, not caption. `masks-masquerade.md:108` already says "the Horniman label says…" and cites S275, S276, S277, S278 together. Not sole. Already a recorded disagreement with S277.

### C. Mixed locators — caption or label is one anchor among others

Not sole unless noted. Knowledge sometimes already names the label.

| id | tier | what the anchor calls out | knowledge lines | note |
|---|---|---|---|---|
| S161 | B | `Table 9 and Table 10 captions ("whistled by a girl")` plus a section | `speech-surrogates-whistled-drummed.md:108` **sole** | Entry repeats the caption parenthetical: `whistled by a girl (S161)`. Strongest non-footwear candidate. |
| S169 | B | photo caption on Halil Cindik, plus a named segment and a closing paragraph | `:123`, `:124` (with other ids) | Love-talk quote and the household-transmission clause. Which of the three locators holds which sentence is not decidable from the row. Gap. |
| S154 | B | `Figure 2 caption` plus two section titles | `:94`, `:95`, `:98` (with other ids) | Entry uses the 800–4000 Hz band and the ~70% / 80–90% figures. Whether those sit in the figure caption is not decidable here. Gap. |
| S244 | A | `Table 1 caption` plus body quotes on pp. 6, 7, 9, 11 | `masks-masquerade.md:22` (`p. 7, Table 1`, with S243); `:80` (p. 9 and p. 11, with S257) | Caption sentence is the table title. The p. 9/p. 11 cites are body. |
| S317 | A | Description field and `Curator's comments, label text` | `monsters-hybrid-beings.md:72` (`Curator's comments`, with S302, S301) | Entry names the curator's comments. Scope also calls the record a gallery label. |
| S386 | A | title fields and `KMS7 gallery label` | `kongo-kingdom.md:102` (`gallery labels 1-2`, with S387); `:111` (`gallery label 1`, with S374, S387) | Already named as labels. |
| S399 | A | entire anchor is `Overview label, object 318318` | `kongo-kingdom.md:84` (`Overview label`, with S384) | Already named. Queued twin **S488** (SOURCES line 491, teaches `supersedes S399`, used-by `—`) has **zero** knowledge cites. |
| S400 | A | `object label` paragraphs plus an audio transcript | `kongo-kingdom.md:90` (`object label`, with S402, S395, S401) | Label part already named. Transcript is not a label. |
| S387 | A | `fig. 46 caption` (`Antonio Manuel… 1629. Marble.`) plus the p. 104 body | `kongo-kingdom.md:102`, `:111` cite `S387, p. 104` | Claim used is the raffia passage, not the caption sentence. Low priority. |

## Not candidates (broad pattern, wrong sense)

Lexical or heraldic "label" in anchor or teaches (16): S022 (queued, uncited), S053, S071, S113, S131 (queued, uncited), S190, S202, S203, S215, S274, S351, S378, S403, S413 (the heraldic charge: "The eldest son bears this label"), S449, S560 (queued, supersedes S413, same charge, uncited).

"image"/"images" as portrait, depiction, or picture-content, not an image caption (18): S029 (rejected tier C), S241, S242, S276, S279, S296, S304, S307, S309, S314, S335, S340, S341, S342, S450, S611, S614, S634.

Scope mentions "caption" but anchor/teaches do not (out of the assigned cells): S251 ("the single collection object it captions"), S261 (tier note "with figure captions"; `masks-masquerade.md:109` cites the Sande section, not a caption), S409 ("one dated object caption" in scope; anchors are body paragraphs).

## Tier C and sole support

Nine tier-C rows. Eight are not W01 because status is not mined (used-by `—`): S009 queued, S011 queued, S028 rejected, S029 rejected, S030 rejected, S043 rejected, S047 rejected, S178 rejected. None of those eight appear as an S-id under `corpus/knowledge/`.

The only W01 row is **S687** (docs, tier C, mined, SOURCES line 642). Anchor is section prose, not a caption: `WINGED BOOTS & CAP OF HERMES section, first sentence: "Hermes wore winged, short leather boots…"`. Teaches: `Theoi says Hermes wore winged short leather boots…`.

Knowledge scan agrees with "sole" and does not add hidden cases:

- Exactly one knowledge line has a tier-C id as its only S-id.
- Exactly one knowledge line has every cited id tier C.
- Both are the same line, and it is the only S687 cite:

`corpus/knowledge/culture-material/footwear-codes-terminology.md:93`

`- Hermes' talaria were winged leather boots. (S687)`

Next line is a different id (`:94` S688). S687's defect is tier-C sole support, already in lesson §7 item 1. It is not a caption re-scope.

## Confidence and gaps

High: registry counts, the fifteen caption/label rows, the footwear lines, the single W01 line, and the single tier-C sole line (all read from the files).

Unresolved, because pages were not re-opened: whether S154's recognition percentages are the Figure 2 caption, and which of S169's three locators holds the love-talk sentence. S674 stays borderline until a re-open shows the quote is or is not body text.
