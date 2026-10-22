# ScribeErrataDoubled — the 13 round-54 Gate rows that quote their own locator

- seat: `KotodamaR55.ScribeErrataDoubled` (scribe, axis calibration)
- round: kotodama 55 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `8eda9543e940bdc4938fad90182ee6a6fe271d0f`, claim base `f4015e70b829523ed81e14ce4279bfab0e0233e4`
- file of record: `corpus/lessons/round-54.md` (200 lines, read at declaration `8eda9543`)
- assignment: routed defect 2 in `corpus/lessons/round-54-verifier-spotcheck.md` section 5

## Result

All 13 named rows exist, one per id, and every one carries exactly the defect named: its citation field holds two quoted
spans, the first being the locator's own section name (plus the locator tail) re-emitted with double quotes before the real
quote. `duplicate == '"' + section + '"' + locator-tail` holds character for character on 13 of 13 rows. Dropping the
duplicate leaves the locator untouched and the real quote byte-exact; the 13 corrected quotes run 8 to 20 words, inside the
lane's 25-word cap.

No file in the lane was modified by this seat. The errata and the paste-ready fragments below are the deliverable; the L1
integrates them into `corpus/lessons/round-54.md`.

## The 13 errata lines

Line numbers are from `corpus/lessons/round-54.md` as declared. Each quote is copied byte-exact out of that file; the count
after it is `wc -w` on the byte-exact copy (see the counts block below).

- S239 (round-54.md:23): locator 'Transformations', ¶1; quote "draw an ontological distinction between the ability of masks to conceal or disguise a body" (15 words). The second quoted span in the row is "Transformations", ¶1 — the locator's section name and tail repeated, not part of the quote.
- S240 (round-54.md:24): locator 'The African Masking Configuration', ¶2; quote "a “mask” is the entire costumed appearance, consisting of headpiece, costume, any adornment, and whatever is held in the hands" (20 words). The second quoted span in the row is "The African Masking Configuration", ¶2 — the locator's section name and tail repeated, not part of the quote.
- S243 (round-54.md:27): locator p. 856, section 2 'Nanfeng Nuo Dance Masks'; quote "Artisans primarily use willow and camphor woods, shaping various forms through meticulous carving techniques." (14 words). The second quoted span in the row is "Nanfeng Nuo Dance Masks" — the locator's section name repeated, not part of the quote.
- S246 (round-54.md:30): locator 'History of use', first paragraph; quote "Outer face opened by means of strings inside at the appropriate moment to reveal the inner character." (17 words). The second quoted span in the row is "History of use", first paragraph — the locator's section name and tail repeated, not part of the quote.
- S249 (round-54.md:33): locator p. 101, section 'Belief System', symbolic components; quote "When performers don them, they temporarily take on divine agency—an act of embodiment central to ritual efficacy." (17 words). The second quoted span in the row is "Belief System", symbolic components — the locator's section name and tail repeated, not part of the quote.
- S259 (round-54.md:43): locator opening section, paragraph beginning 'I did not know of firam'; quote "in some villages, every Lak male, from age 5 or 6 on, was an initiate in the secret society" (19 words). The second quoted span in the row is "I did not know of firam" — the locator's anchor phrase repeated, not part of the quote.
- S262 (round-54.md:46): locator paragraph 2 (beginning 'My focus on the carved headpiece'); quote "The Mende, like most African peoples, do not have a separate word for “mask,”" (14 words). The second quoted span in the row is "My focus on the carved headpiece") — the locator's anchor repeated, and it also swallows the closing parenthesis of the locator's `(beginning ...)`.
- S265 (round-54.md:49): locator 'Status of Masks', paragraph 1; quote "By their very nature, masks are empowered the moment they are made." (12 words). The second quoted span in the row is "Status of Masks", paragraph 1 — the locator's section name and tail repeated, not part of the quote.
- S266 (round-54.md:50): locator 'Intellectual Property Rights' ¶2; quote "Katsinas dolls have also been duplicated from Hopi dancers seen at Hopi." (12 words). The second quoted span in the row is "Intellectual Property Rights" ¶2 — the locator's section name and tail repeated, not part of the quote.
- S267 (round-54.md:51): locator §'Sources of power within the Mande buzz aesthetic', paragraph on jow masks; quote "non-initiates (normally women and children) who are forbidden from seeing the headpieces" (12 words). The second quoted span in the row is "Sources of power within the Mande buzz aesthetic", paragraph on jow masks — the locator's section name and tail repeated, not part of the quote.
- S268 (round-54.md:52): locator §'The Boki voice-disguiser – an object of design?', paragraph on Lo-Bamijoko's Igbo classification; quote "they are at once musical instruments, social tools and metaphysical manifestations" (11 words). The second quoted span in the row is "The Boki voice-disguiser – an object of design?", paragraph on Lo-Bamijoko's Igbo classification — the locator's section name and tail repeated, not part of the quote.
- S275 (round-54.md:59): locator 'Malagan traditions', paragraph after the Michael Gunn attribution; quote "these highly elaborate objects were only used once" (8 words). The second quoted span in the row is "Malagan traditions", paragraph after the Michael Gunn attribution — the locator's section name and tail repeated, not part of the quote.
- S277 (round-54.md:61): locator 'Happy is he who dreams of forest spirits', final paragraph; quote "these spirits only reveal themselves to the initiated" (8 words). The second quoted span in the row is "Happy is he who dreams of forest spirits", final paragraph — the locator's section name and tail repeated, not part of the quote.

## Paste-ready replacement citation fields

Each fragment replaces only the text between `— accessed 2026-10-22 — ` and `. Grounds:` on its row, so the URL, the
access date and the Grounds text stay as they are. Leaving `Grounds:` alone matters: routed defect 1 (Grounds truncated
mid-sentence) also covers S259, S265, S275 and S277, and that repair belongs to its own seat.

- S239 → `'Transformations', ¶1: "draw an ontological distinction between the ability of masks to conceal or disguise a body"`
- S240 → `'The African Masking Configuration', ¶2: "a “mask” is the entire costumed appearance, consisting of headpiece, costume, any adornment, and whatever is held in the hands"`
- S243 → `p. 856, section 2 'Nanfeng Nuo Dance Masks': "Artisans primarily use willow and camphor woods, shaping various forms through meticulous carving techniques."`
- S246 → `'History of use', first paragraph: "Outer face opened by means of strings inside at the appropriate moment to reveal the inner character."`
- S249 → `p. 101, section 'Belief System', symbolic components: "When performers don them, they temporarily take on divine agency—an act of embodiment central to ritual efficacy."`
- S259 → `opening section, paragraph beginning 'I did not know of firam': "in some villages, every Lak male, from age 5 or 6 on, was an initiate in the secret society"`
- S262 → `paragraph 2 (beginning 'My focus on the carved headpiece'): "The Mende, like most African peoples, do not have a separate word for “mask,”"`
- S265 → `'Status of Masks', paragraph 1: "By their very nature, masks are empowered the moment they are made."`
- S266 → `'Intellectual Property Rights' ¶2: "Katsinas dolls have also been duplicated from Hopi dancers seen at Hopi."`
- S267 → `§'Sources of power within the Mande buzz aesthetic', paragraph on jow masks: "non-initiates (normally women and children) who are forbidden from seeing the headpieces"`
- S268 → `§'The Boki voice-disguiser – an object of design?', paragraph on Lo-Bamijoko's Igbo classification: "they are at once musical instruments, social tools and metaphysical manifestations"`
- S275 → `'Malagan traditions', paragraph after the Michael Gunn attribution: "these highly elaborate objects were only used once"`
- S277 → `'Happy is he who dreams of forest spirits', final paragraph: "these spirits only reveal themselves to the initiated"`

## Word counts (command output)

```
  15 quote-S239.txt
  20 quote-S240.txt
  14 quote-S243.txt
  17 quote-S246.txt
  17 quote-S249.txt
  19 quote-S259.txt
  14 quote-S262.txt
  12 quote-S265.txt
  12 quote-S266.txt
  12 quote-S267.txt
  11 quote-S268.txt
   8 quote-S275.txt
   8 quote-S277.txt
 179 total
```

sha256 of the counted files, so the bytes that were counted can be re-derived:

```
4f695b661c7262fc88b783dce8e3d6008438cddf0a38bbf0184668bf53dd1d41  quote-S239.txt
6d5d1c79ce697db577891199ad98006cfe76ce930606248481a297bd79946fef  quote-S240.txt
b2a5d9aba82b1c007d5f8b10c10b922f8853be1257e4df6b2f295c20db3bcf63  quote-S243.txt
ced52048ac8aa31ebfab6e4deed02ef8d45c050fea4df39dc34937d44270ea34  quote-S246.txt
65e467fefbc93e44de400ba26ae54e892dda5148725827c7d681af0edb4dc0e4  quote-S249.txt
97882b5018e9f21e2f6862125dcd9f3b5b971c46d1bd1663677ed2296a18834d  quote-S259.txt
bc9fcf45cfbb16bd744a5b14ed70f12cc10b87d2cf04993115e510f300167cc7  quote-S262.txt
eabf8b7d65af18419e8434bb13a8b50acff9d17dd3a7656d33bbd4d5a1c49f86  quote-S265.txt
27a2bd5ac37f57b2d445c6ad39adc65f35bb26a578406b0f0954ce5e55b8b03f  quote-S266.txt
c6969ccc2d7ae8280936e6c3672284d28fd4699711a18d29d89f24b32db2fcde  quote-S267.txt
ac8208b0d803a8ef04a11b07a406c3c2e3f6283bb55a63e8ffa941b3b2b1ae36  quote-S268.txt
cc90b2354348ae0e9fc09fbb6d35e6e3fa1cc7fe7d1eaee601b817e18ae91d77  quote-S275.txt
e7d2aef4a27253fe6c71a3e975510bcc9ca344883f57d434048e29143c751165  quote-S277.txt
```

Counting caveat, S249 only: the quote carries `agency—an` with an unspaced em dash, so `wc -w` returns 17 and an em-dash
split returns 18. Both are under 25. Every other quote counts the same either way.

## Verification performed

| check | command or method | observed |
|---|---|---|
| Gate rows present | scan from `## Gate` to the next `## ` | 46 `- S` rows |
| rows with a doubled span | count lines holding 2 or more `: "` separators over all 200 lines | exactly 13, all inside `## Gate`, all `- S` rows, ids equal to the routed list |
| duplicate is the locator | `dup == '"' + section + '"' + tail` per row | 13/13 identical |
| quotes byte-exact | each quote extracted from the row, written to a file, counted | `in_src` true for 13/13; counts and sha256 above |
| base checker blind | `python3 -B tools/check-gate-quotes.py corpus/lessons/round-54.md` | `GATE_QUOTES: 0 findings`, exit 0 |
| checker self-test healthy | `python3 -B tools/check-gate-quotes.py --selftest` | `SELFTEST: 12/12 pass`, exit 0 |
| correction is sufficient | patch all 13 citation fields in memory, re-scan the patched text | 0 lines with 2 or more `: "`; id, URL, access date and Grounds byte-identical on all 13 |

## Findings

1. **The duplicate is mechanical.** The doubled span is the locator's single-quoted section name, re-emitted with double
   quotes, then whatever tail the locator already carried: `, ¶1` (S239), `, ¶2` (S240), `, first paragraph` (S246),
   `, symbolic components` (S249), ` ¶2` (S266), `, paragraph 1` (S265), `, paragraph on jow masks` (S267),
   `, paragraph on Lo-Bamijoko's Igbo classification` (S268), `, paragraph after the Michael Gunn attribution` (S275),
   `, final paragraph` (S277). Three rows carry an empty tail: S243 repeats only `"Nanfeng Nuo Dance Masks"` after the
   `p. 856, section 2` prefix, S259 only the anchor `"I did not know of firam"`, and S262 reproduces the locator's closing
   parenthesis inside the quoted span, so a careless deletion there would also unbalance the locator.
2. **Why the cap check never fired.** `tools/check-gate-quotes.py` groups quoted spans into runs and breaks a run only on
   wordish text between spans (`WORDISH` at tools/check-gate-quotes.py:75-76); it reports `over-cap` above 25 words
   (`MAX_WORDS = 25` at :67, finding at :144) and `ellipsis-joined` (:146). On these rows the duplicated span either
   splits the line into two short runs or merges into one run that stays at or under the cap. The checker's own
   segmentation of the declared file:

   | row | quoted spans | runs | run words | over-cap |
   |---|---|---|---|---|
   | S239 | 2 | 2 | 1, 15 | no |
   | S240 | 2 | 2 | 4, 20 | no |
   | S243 | 2 | 1 | 18 | no |
   | S246 | 2 | 2 | 3, 17 | no |
   | S249 | 2 | 2 | 2, 17 | no |
   | S259 | 2 | 1 | 25 | no |
   | S262 | 2 | 1 | 20 | no |
   | S265 | 2 | 2 | 3, 12 | no |
   | S266 | 2 | 2 | 3, 12 | no |
   | S267 | 2 | 2 | 8, 12 | no |
   | S268 | 2 | 2 | 8, 11 | no |
   | S275 | 2 | 2 | 2, 8 | no |
   | S277 | 2 | 2 | 8, 8 | no |

   S259 is the tightest case: its two spans sit either side of `: ` only, so they merge into a single run of exactly 25
   words — the cap line, which the check permits because it fires only above 25. The real quote alone is 19 words. A
   shape class is therefore needed, not a smaller cap: the duplicated locator can hide a joined run at the cap. S259 is the
   case to keep as a `doubled-locator` fixture: a correct implementation must flag it while a cap-only check cannot.
3. **The routed list is complete.** The 13-row scan finds nothing the routed defect missed: no fourteenth doubled row and
   no instance outside `## Gate` anywhere in the file.
4. **Overlap with routed defect 1.** S259, S265, S275 and S277 also end their `Grounds:` mid-sentence (S265 shows the
   shape `... a. Seat:`). The two repairs are independent; the fragments above never touch `Grounds:`.
5. **What these errata do not assert.** Removing the duplicate restores readability only. Whether each locator and quote
   still describes the page it points at was round-54 discernment work and is not re-opened here; no source was fetched.

## Not run / out of scope

- Did not edit `corpus/lessons/round-54.md`; the L1 integrates these fragments.
- Did not run `reports/round-55/accept-c.py` or `reports/round-55/accept-o.py`.
- Did not run git or jj writes anywhere; the one git call in the lane was `git log -1 --format` (read-only).
- No tools installed or upgraded, no external network read, no browser.

## Artifacts

- `/fast/scratch/hyaku/kotodama-r55/KotodamaR55.ScribeErrataDoubled/records.json` — 13 records: line, locator, removed span, quote, `wc -w` count, sha256 prefix, corrected fragment.
- `/fast/scratch/hyaku/kotodama-r55/KotodamaR55.ScribeErrataDoubled/runs.json` — checker span/run segmentation per row.
- `/fast/scratch/hyaku/kotodama-r55/KotodamaR55.ScribeErrataDoubled/quote-<S-id>.txt` — the 13 counted quote files.

unopened: none attempted — this assignment is a lane-internal byte-copy repair and needs no external source.
