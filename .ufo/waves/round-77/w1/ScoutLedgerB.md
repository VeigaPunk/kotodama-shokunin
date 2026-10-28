# ScoutLedgerB — round 77 wave-1 Ca recon

Base: `211f9526800906e0c585d878d265c37e5e090c15`. Command `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD` → `211f9526800906e0c585d878d265c37e5e090c15`. Four distinct round-75 statements are red at base; all are ANNOTATE candidates. No install. No git/jj mutation. No paths outside the seat's stage and report were written in the lane. Scratch removed before yield.

Pairs: `.ufo/waves/round-77/w1/stage/ScoutLedgerB/pairs.json` (L77-B01..B04). They use argv-only git observations pinned to the base; `stated_at` locations/text and statement/observation parsers were self-checked against base, and each observed token equalled `expected_after` while differing from the stated token. Prior round-76 exclusions checked against its base ledger: L76-01..08, 10..15, 17..21 include lesson lines 4,15,28,30,31,47,48,92,93,94,244,246,251,312,332; none shares an identical stated line/token with these pairs.

## Verified pairs and raw observations

- **L77-B01**, `corpus/lessons/round-75.md:44`, says anchor quotes are “absent from” stored windows (continued at line 45 with S888/S892); stated token `absent`, observed `yes`. Command: `git grep -h -o -E '^quote-found: [a-z]+' 211f9526800906e0c585d878d265c37e5e090c15 -- reports/round-75/evidence/S888.txt` → raw stdout `quote-found: yes` (rc 0). The committed evidence window payload also contains the anchor; direct command `git grep -F -n -e '故事是一种深层的抽象结构' 211f9526800906e0c585d878d265c37e5e090c15 -- reports/round-75/evidence/S888.txt` printed lines 33, 35 and 37, including the anchor in the window payload at line 37.
- **L77-B02**, `corpus/lessons/round-75.md:35`, states S892's anchor is **not** in its stored window; stated token `not`, observed `yes`. Command: `git grep -h -o -E '^quote-found: [a-z]+' 211f9526800906e0c585d878d265c37e5e090c15 -- reports/round-75/evidence/S892.txt` → raw stdout `quote-found: yes` (rc 0). Direct payload check: `git grep -F -n -e 'Mais combien, et de quelle nature, sont ces codes' 211f9526800906e0c585d878d265c37e5e090c15 -- reports/round-75/evidence/S892.txt` printed lines 33, 35 and 37, with the anchor in the window payload at line 37. Distinct statement from L76-19's before-offset on lesson line 48.
- **L77-B03**, `corpus/lessons/round-75.md:245`, maps S885 `used-by` to base plus `amend-2026-10-23`; stated token `amend-2026-10-23`, observed omitted sibling `amend-2026-10-23b`. Command: `git grep -F -o -e amend-2026-10-23b.md 211f9526800906e0c585d878d265c37e5e090c15 -- corpus/SOURCES.md` → raw stdout (three matches): `…:corpus/SOURCES.md:amend-2026-10-23b.md` (three lines; path prefix is the full base/path). The S885 used-by cell at SOURCES.md line 840 lists base, amend-23 and amend-23b; the b amendment's own source line is `S885` (`git grep -n -F -e S885 <base> -- corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md` → line 3). This pair is line 245; L76-07 is line 246.
- **L77-B04**, `corpus/lessons/round-75.md:251`, says the S892 URL line ends after `2014%20marrone%20age%`; stated token is that truncated prefix, observed full suffix `2014%20marrone%20age%20dor---2.pdf`. Command: `git grep -h -F -o -e 2014%20marrone%20age%20dor---2.pdf 211f9526800906e0c585d878d265c37e5e090c15 -- corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md` → raw stdout has two lines, each `2014%20marrone%20age%20dor---2.pdf` (rc 0). At base the S892 source row is in the b amendment, with the full URL on one line; the claimed truncation is stale.

Self-verification output from the pair checker (each `on_line=True`, rc 0, stated token differs from observed token, and observation equals expected):
```
L77-B01 on_line=True stated=absent rc=0 observed=yes expected=yes
L77-B02 on_line=True stated=not rc=0 observed=yes expected=yes
L77-B03 on_line=True stated=amend-2026-10-23 rc=0 observed=amend-2026-10-23b expected=amend-2026-10-23b
L77-B04 on_line=True stated=2014%20marrone%20age% rc=0 observed=2014%20marrone%20age%20dor---2.pdf expected=2014%20marrone%20age%20dor---2.pdf
```

No unresolved pair uncertainty. No checks beyond these read-only base observations and self-verification were run.

Report: .ufo/waves/round-77/w1/ScoutLedgerB.md
