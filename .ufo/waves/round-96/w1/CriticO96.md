# CriticO96 — Report (round 96, wave w1)

Attack seat on grader v7 with fresh counterfeit classes battery96 does not carry. Full detail,
table and recipes: `.ufo/waves/round-96/w1/stage/CriticO96/attacks.md`.

- Dependency: `stage/ExecGraderV7/DONE` reached via the bounded 45x60 s loop (`DEP-READY after 31 polls`, rc 0); battery96.py (sha256 9f80f59481861b104f166a838222fcdf300e55a27fc841b5217e1980b5e91c21) read only after it landed, used read-only for its fixture builders and `grade()` shape.
- v7 under attack in place: `tools/check-advance-evidence.py` sha256 2e28a289746812b14a07a0645e568f0cee9dfb1789af6cfe6ce88f80c8f053ec; v6 baseline `stage/ExecGraderV7/v6-base.py` sha256 f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec (all `sha256sum` rc 0).
- Driver: `stage/CriticO96/attacks_critic96.py` — 19 fresh classes + G0 + ZWNJ1, fixtures under scratch only, both runs rc 0.
- Tally: v7 `CRITIC-O96 survivors=7 unnamed=0 refused=12 traceback=0`; v6 do-nothing over identical fixtures `survivors=11 unnamed=0 refused=8 traceback=0`. tb_classes=0 in both results JSONs (extraction rc 0).
- v7 closes exactly 4 of my 11 v6 survivors (FS1/GS1/RS1/PS1 -> VERDICT-LINESEP) and renames FWS1 (VERDICT-COMBINE -> ID-NONASCII); 7 survivors are byte-identical across v6->v7: CR1 (U+000D severs, not blocklisted), US1 (U+001F), OGH1 (U+1680), IS1 (U+3000, NFKC twin of NBSP), NUL1 (U+0000), CM1 (combining mark on heading number defeats `_NUM2`), CMW2 (junk marked first token anchors the span floor).
- Three most dangerous survivors routed to round 97 (not implemented): CM1 (fix: NFKD-strip Mn before the `_NUM2` shape test), CR1 (fix: add U+000D to the verdict-window blocklist, or take CriticO95's structural rule: refuse any verdict window keeping a non-letter byte between letters after NFKC+strip+fold — closes CR1/US1/OGH1/IS1/NUL1 at once), IS1 (fix: blocklist over the NFKC-folded span, refuse any Zs/Cc inside it).
- Routing nit: ZWJ1/FWID1 refuse but under key-splitting — the diagnostic names the mis-keyed lookalike id (`S００１`), not S001; NFKC-folding the id key in `dispositions()` is cheap r97 hardening.
- Controls G0 and ZWNJ1 CLEAN rc 0 on both versions; battery96 remains the frozen predicate and was not edited or re-run; claims.json/predispatch.py/round-95 files untouched; no commits.
- Tooling installed: none. No pacman, no sysctl writes, no git/jj mutations (read-only sha256sum/grep/diff/sed -n/cat only).
- Scratch `/fast/scratch/hyaku/kotodama-r96/CriticO96` deleted before yield; commands in attacks.md regenerate fixtures and results.

Stage files: `stage/CriticO96/attacks_critic96.py`, `stage/CriticO96/attacks.md`, `stage/CriticO96/DONE` (written last, sha256 of attacks.md).
