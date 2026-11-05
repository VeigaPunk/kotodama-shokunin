# ExecQuarantineA — kotodama round 91 w1 — quarantine hand-check verdicts

Seat: leaf executor, quarantine hand-check of ten kotodama register rows in the shokuknow absent-defect register (slice.tsv). Adopted nothing; every row got its own verdict. Freeze materials (claims.json, measure91.py) read for context; untouched. No production file, registry row, or sibling path written; no git/jj mutation; no pacman; no sysctls; no tools installed.

## Verdicts (all rows registered class `payload-absent`)

| id | verdict | http | bytes | found/total | gist |
|---|---|---|---|---|---|
| S776 | PARTIAL | 200 | 24058 | 4/5 | openstd GB/T 33661 page carries the metadata payload; the one fold-miss is a tag-split (`标准状态：现行`), 5/5 under the no-whitespace check — contradicts the registered class |
| S778 | LOCATED | 200 | 10291 | 2/2 | koyomi portal (EUC-JP) contains both quoted sentences — contradicts the registered class |
| S779 | ABSENT | 200 | 22950 | 0/2 | quote is about China ICH national lists; the page is a Japanese calendar news item — wrong-source citation, class confirmed |
| S786 | ABSENT | 200 | 753374 | 0/2 | conlang.org 26c3.pdf: pdftotext (42219 chars) contains the Chinese sentence but NOT the English gloss `conlanging (n): …` |
| S787 | ABSENT | 200 | 45238 | 0/1 | chinawriter page lacks the quoted clause even whitespace-free |
| S791 | UNREACHABLE | 400 | 786 | — | server rejects the URL with HTTP 400; registered URL ends in a bare `%` (malformed percent-encoding) |
| S792 | UNREACHABLE | 200* | 130538 | — | curl rc=28, operation timed out at 40001 ms mid-transfer (200 in flight); fragment also absent from the partial body |
| S795 | ABSENT | 200 | 357913 | 0/1 | obirin PDF: extraction (19163 chars) lacks the 生前の名前 enumeration |
| S796 | ABSENT | 200 | 108503 | 0/1 | kankyo-u PDF: extraction (12314 chars) lacks the 姓と氏 sentence |
| S804 | ABSENT | 200 | 212285 | 0/1 | kotobank 苗字 page lacks the quoted definition sentence even whitespace-free |

Spread: 1 LOCATED, 1 PARTIAL, 6 ABSENT, 2 UNREACHABLE. Against the registered class: S776 and S778 contradict `payload-absent` (payload present); S779, S786, S787, S795, S796, S804 confirm it (6/6 with pdftotext deciding the three PDFs); S791, S792 are untestable as registered.

## Numbers and commands

- 10 URLs, each fetched exactly once (2026-11-05, 08:13:13–08:13:53 -03:00; instants are exact mtimes of the captured bodies): `curl -sS -L --max-time 40 -o <stage>/caps/<id>.bin -w '%{http_code} %{size_download} %{content_type}' '<url>'` — rc=0 ×9, rc=28 ×1 (S792). Per-row `-w` outputs, sha256, fragments and booleans: `verdicts-A.json`; full command lines: `verdicts-A.md`.
- Supplementary: `pdftotext -q caps/S786.bin -` (42219 chars), `caps/S795.bin` (19163), `caps/S796.bin` (12314) — rc=0 each. Declared-charset decode for S778 (EUC-JP). No-whitespace CJK variant recorded per fragment. Mechanical verdicts follow the seat procedure exactly; supplements live in notes only.
- Tooling: curl 8.23.0, Python 3.14.8 stdlib, pdftotext 26.10.0 — all preinstalled; zero installs.

## Deviations declared

1. Fragment split also breaks on the cell-level `<br>` joiner and strips the TSV's backtick quoting markers (file format, not cited text); without this every fragment false-negatives — first pass had S778 ABSENT purely from a backtick artifact.
2. `fetched_at` is the capture file's mtime (exact local instant, offset -03:00) because pass-1 did not persist wall-clock per row; no URL was refetched.

## Files written

- `verdicts-A.json`, `verdicts-A.md`, `caps/S{776,778,779,786,787,791,792,795,796,804}.bin` — all under `.ufo/waves/round-91/w1/stage/ExecQuarantineA/`
- This trailer. Scratch `/fast/scratch/hyaku/kotodama-r91/ExecQuarantineA/` deleted before yield.

## Risks

- S792 is UNREACHABLE by the mandated 40 s bound, not by server refusal; a longer window would likely finish the transfer (200 + 130 KB already in flight).
- S791's payload may exist behind a well-formed URL; as registered it is malformed, so the row is untestable without a registry-side URL repair (out of my scope).
- PDF "absent" verdicts rest on poppler extraction quality; both extracts were large and complete-looking, and notes say absence is w.r.t. extracted text.
