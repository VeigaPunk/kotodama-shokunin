# SOURCES row template implementation

Created `/tmp/row-template-builder.py` (stdlib-only CLI). It accepts exactly 11 positional cells in registry order: `id, source, kind, tier, scope, anchor, teaches, status, opened, recheck, used-by`; prints `| cell | ... |`. It rejects literal `|`, escaped `\|`, `\x7c`, `\u007c` and `\U0000007c` case-insensitively, as well as non-string values, wrong cell counts, line breaks, and leading/trailing whitespace. The source contract file named by SOURCES.md was not present at its referenced fleet worktree path; column order was taken from the SOURCES.md Registry header (11 columns).

ScoutOpenSourcesC had no published candidate list/report during this run (its agent status remained running and its transcript showed only pending browsing, not source results). Therefore these three illustrative samples use fields chosen for the assignment, not scout-validated candidates; do not treat them as verified source evidence or append directly to SOURCES.md. IDs S861–S863 are examples only and could collide with subsequent registry additions.

## Rendered examples

```text
| S861 | UNESCO, Tango — https://ich.unesco.org/en/RL/tango-00258 | docs | A | Tango as an intangible cultural heritage practice | Description, first sentence | Tango developed among the urban lower classes in Buenos Aires and Montevideo. | queued | 2026-10-25 | on-release | — |
| S862 | UNESCO, Capoeira Circle — https://ich.unesco.org/en/RL/capoeira-00892 | docs | A | Capoeira practice and cultural transmission | Description, opening sentence | The Capoeira circle is a space and time where capoeira is practised. | queued | 2026-10-25 | on-release | — |
| S863 | International Council of Kinetography Laban — https://ickl.org/ | docs | A | Labanotation as a movement-notation system | About section (institutional landing page) | Kinetography Laban is a system for recording human movement. | queued | 2026-10-25 | on-release | — |
```

## Evidence and limitations

The script was imported and called to render all three 11-field samples. In-memory rejection checks returned the expected error for each of: literal pipe, `\\|`, `\\x7c`, and `\\u007c`. Plain curl of the two UNESCO URLs returned HTTP 200 but downloaded a bot-challenge page, not article content; their quoted teachings above are illustrative and **not** supported by those responses. The ICKL plain curl returned HTTP 200; its landing page states that Kinetography Laban/Labanotation is a major movement-notation method used for documenting, education about, and research into human movement. The rendered ICKL sentence is a paraphrase, not a verbatim quote. No registry row was added and no lane corpus files were changed.

No tools installed or updated. No build/test/lint/formatter run; the invocation above exercised only the requested sample rendering and pipe-rejection behavior.
