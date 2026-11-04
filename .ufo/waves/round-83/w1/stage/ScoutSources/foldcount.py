#!/usr/bin/env python3
"""Count a span in a fetched document under the QUALITY 30 rule.

usage: foldcount.py <file|-> <quote>

raw    = occurrences in the document as served (gzip decoded when the
         served bytes are gzip; no other normalization).
folded = script/style elements dropped, tags -> ONE space, HTML entities
         decoded (HTML pages only), U+00A0 and U+2003 -> space, whitespace
         runs -> one space, then count.  A plain-text document (no markup)
         is folded by whitespace only.

Prints one line:
  bytes=<decoded bytes> sha256=<decoded sha256> raw=<n> folded=<m> words=<w> chars=<c>
and exits 1 when folded != 1 (a span that is not unique is not citable).
"""
import gzip
import hashlib
import html
import re
import sys


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    path, quote = sys.argv[1], sys.argv[2]
    served = sys.stdin.buffer.read() if path == "-" else open(path, "rb").read()
    decoded = gzip.decompress(served) if served[:2] == b"\x1f\x8b" else served
    text = decoded.decode("utf-8", "replace")

    is_markup = bool(re.search(r"(?i)<(!doctype|html|head|body|p|div|pre)\b", text[:4096]))
    if is_markup:
        text = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", text)
        text = re.sub(r"(?s)<[^>]+>", " ", text)
        text = html.unescape(text)
    text = text.replace("\u00a0", " ").replace("\u2003", " ")
    folded = re.sub(r"\s+", " ", text)

    raw = decoded.decode("utf-8", "replace").count(quote)
    folded_n = folded.count(quote)
    print(
        f"bytes={len(decoded)} sha256={hashlib.sha256(decoded).hexdigest()} "
        f"raw={raw} folded={folded_n} words={len(quote.split())} chars={len(quote)}"
    )
    return 0 if folded_n == 1 else 1


if __name__ == "__main__":
    sys.exit(main())
