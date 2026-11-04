#!/usr/bin/env python3
"""Locate a quote in one MediaWiki article's nonempty paragraphs.

Read-only except --selftest, which uses a temporary directory under existing
--work. Standard library only; no network. Exit 0 match, 1 verdict failure,
2 PARAGRAPH_ERROR (arguments, input or article scope cannot be evaluated).
"""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
import sys
import tempfile


VOID = frozenset('area base br col embed hr img input link meta param source track wbr'.split())
BLOCK = frozenset('address article aside blockquote div dl fieldset figure footer form h1 h2 h3 h4 h5 h6 header hr main nav ol p pre section table ul'.split())
EXCLUDED_TAGS = frozenset('figure figcaption nav aside header footer caption script style template noscript'.split())
EXCLUDED_CLASSES = frozenset('navbox vertical-navbox navigation navigation-not-searchable noprint ws-noexport toc thumb thumbcaption tright tleft mw-editsection mw-empty-elt'.split())


def fold(text):
    return ' '.join(text.split())


class ArticleParser(HTMLParser):
    """Track ancestry, not text patterns or an assumed first quote occurrence."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []  # (tag, inside parser output, excluded subtree)
        self.roots = 0
        self.paragraphs = []
        self.parts = None
        self.paragraph_depth = None

    def finish_paragraph(self):
        if self.parts is not None:
            text = fold(''.join(self.parts))
            if text:
                self.paragraphs.append(text)
        self.parts = None
        self.paragraph_depth = None

    def handle_starttag(self, tag, attrs):
        # HTML permits omitted </p> before another paragraph/block element.
        if tag in BLOCK and self.parts is not None:
            depth = self.paragraph_depth
            self.finish_paragraph()
            del self.stack[depth:]
        attrs = dict(attrs)
        classes = set((attrs.get('class') or '').split())
        parent_article = bool(self.stack and self.stack[-1][1])
        parent_excluded = bool(self.stack and self.stack[-1][2])
        root = 'mw-parser-output' in classes
        if root:
            self.roots += 1
        article = parent_article or root
        excluded = (parent_excluded or tag in EXCLUDED_TAGS
                    or bool(classes & EXCLUDED_CLASSES)
                    or any(c.endswith('caption') or c.endswith('-navbox') for c in classes)
                    or attrs.get('role') in ('navigation', 'banner', 'contentinfo')
                    or 'hidden' in attrs or attrs.get('aria-hidden') == 'true')
        if tag == 'br' and self.parts is not None and not excluded:
            self.parts.append(' ')
        if tag not in VOID:
            self.stack.append((tag, article, excluded))
        if tag == 'p' and article and not excluded:
            self.parts = []
            self.paragraph_depth = len(self.stack) - 1

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                if self.parts is not None and index <= self.paragraph_depth:
                    self.finish_paragraph()
                del self.stack[index:]
                break

    def handle_data(self, data):
        if self.parts is not None and self.stack and not self.stack[-1][2]:
            self.parts.append(data)

    def article_paragraphs(self, html):
        self.feed(html)
        self.close()
        self.finish_paragraph()
        if self.roots != 1:
            raise ValueError(f'expected one .mw-parser-output article, found {self.roots}')
        return self.paragraphs


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)


def selftest(work):
    tool = str(Path(__file__).resolve())
    checks = 0
    with tempfile.TemporaryDirectory(prefix='paragraph-selftest-', dir=work) as directory:
        root = Path(directory)

        def run(name, html, quote, expected, code, marker, extra=None):
            nonlocal checks
            case = root / f'{checks:02d}'
            case.mkdir()
            path = case / 'article.html'
            path.write_bytes(html.encode('utf-8') if isinstance(html, str) else html)
            args = ['--html', str(path), '--quote', quote, '--expect', str(expected)]
            if extra is not None:
                args = extra
            result = subprocess.run([sys.executable, '-B', tool, *args], cwd=case,
                                    capture_output=True, text=True, timeout=10)
            combined = result.stdout + result.stderr
            if result.returncode != code or marker not in combined or 'Traceback' in combined:
                raise ValueError(f'selftest {name}: exit={result.returncode}; {combined!r}')
            checks += 1
            print(f'selftest: {name} exit={result.returncode}')

        def article(body):
            return '<div class="mw-parser-output">' + body + '</div>'

        basic = article('<p>first anchor</p><p>second <b>needle</b> tail</p>')
        run('second paragraph', basic, 'second needle tail', 2, 0, 'ordinal=2')
        run('ordinal mismatch', basic, 'needle', 1, 1, 'ordinal=2')
        run('absent quote', basic, 'absent', 1, 1, 'absent')
        run('ambiguous paragraphs', article('<p>needle</p><p>needle</p>'), 'needle', 1, 1, 'ambiguous')
        run('nested inline and entities', article('<p>café <b>A<i>&amp;</i>B</b>&nbsp; tail</p>'), 'café A&B tail', 1, 0, 'ordinal=1')
        run('whitespace folding', article('<p>first\n\t needle<br> tail</p>'), ' first\tneedle  tail ', 1, 0, 'ordinal=1')
        run('figure and navigation excluded', article('<nav><p>needle</p></nav><figure><p>needle</p><figcaption><p>needle</p></figcaption></figure><p>needle</p>'), 'needle', 1, 0, 'ordinal=1')
        run('caption classes excluded', article('<div class="thumbcaption"><p>needle</p></div><p>needle</p>'), 'needle', 1, 0, 'ordinal=1')
        run('disclaimer excluded', article('<div class="ws-noexport"><p>needle</p></div><div class="prp-pages-output"><p>needle</p></div>'), 'needle', 1, 0, 'ordinal=1')
        run('outside article excluded', '<p>needle</p>' + basic + '<p>needle</p>', 'needle', 2, 0, 'ordinal=2')
        run('script and style excluded', article('<p>nee<script>bad()</script><style>bad{}</style>dle</p>'), 'needle', 1, 0, 'ordinal=1')
        run('publisher caption suffix excluded', article('<p>first</p><div class="image-caption"><p>needle</p></div><p>needle</p>'), 'needle', 2, 0, 'ordinal=2')
        run('empty paragraphs ignored', article('<p> \n </p><p>needle</p>'), 'needle', 1, 0, 'ordinal=1')
        run('omitted paragraph close', article('<p>first<p>needle'), 'needle', 2, 0, 'ordinal=2')
        run('cross paragraph rejected', article('<p>first</p><p>needle</p>'), 'first needle', 1, 1, 'absent')
        run('repeated in one paragraph', article('<p>needle needle</p>'), 'needle', 1, 0, 'ordinal=1')
        run('missing article', '<p>needle</p>', 'needle', 1, 2, 'PARAGRAPH_ERROR')
        run('multiple articles', basic + basic, 'needle', 1, 2, 'PARAGRAPH_ERROR')
        run('malformed UTF8', b'\xff', 'needle', 1, 2, 'PARAGRAPH_ERROR')
        for expected in ('0', '-1', 'bad', '1.0'):
            run(f'invalid expect {expected}', basic, 'needle', expected, 2, 'PARAGRAPH_ERROR')
        run('empty quote', basic, ' \t ', 1, 2, 'PARAGRAPH_ERROR')
        run('missing arguments', basic, 'needle', 1, 2, 'PARAGRAPH_ERROR', [])
        run('unreadable input', basic, 'needle', 1, 2, 'PARAGRAPH_ERROR',
            ['--html', str(root / 'missing'), '--quote', 'needle', '--expect', '1'])
        run('missing work', basic, 'needle', 1, 2, 'PARAGRAPH_ERROR', ['--selftest'])
        run('nonexistent work', basic, 'needle', 1, 2, 'PARAGRAPH_ERROR',
            ['--selftest', '--work', str(root / 'missing')])
        run('mixed modes', basic, 'needle', 1, 2, 'PARAGRAPH_ERROR',
            ['--selftest', '--work', str(root), '--expect', '1'])
    print(f'SELFTEST: PASS ({checks} checks)')
    return 0


def main():
    parser = Parser(description=__doc__, allow_abbrev=False)
    parser.add_argument('--html', type=Path)
    parser.add_argument('--quote')
    parser.add_argument('--expect')
    parser.add_argument('--selftest', action='store_true')
    parser.add_argument('--work', type=Path)
    try:
        args = parser.parse_args()
        if args.selftest:
            if args.html is not None or args.quote is not None or args.expect is not None:
                raise ValueError('--selftest cannot be combined with locator arguments')
            if args.work is None or not args.work.is_dir():
                raise ValueError('--selftest requires existing --work directory')
            return selftest(args.work)
        if args.html is None or args.quote is None or args.expect is None or args.work is not None:
            raise ValueError('use --html PATH --quote TEXT --expect N, or --selftest --work PATH')
        if not re.fullmatch(r'[1-9][0-9]*', args.expect):
            raise ValueError('--expect must be a positive decimal integer')
        expected = int(args.expect)
        quote = fold(args.quote)
        if not quote:
            raise ValueError('--quote must contain non-whitespace text')
        paragraphs = ArticleParser().article_paragraphs(args.html.read_text(encoding='utf-8'))
        matches = [index for index, text in enumerate(paragraphs, 1) if quote in text]
        if len(matches) != 1:
            reason = 'absent' if not matches else 'ambiguous'
            print(f'PARAGRAPH: FAIL {reason} matches={len(matches)} quote={quote!r}')
            return 1
        ordinal = matches[0]
        passed = ordinal == expected
        print(f'PARAGRAPH: {"PASS" if passed else "FAIL"} ordinal={ordinal} expect={expected} quote={quote!r}')
        return 0 if passed else 1
    except (OSError, UnicodeError, ValueError, subprocess.SubprocessError) as error:
        print(f'PARAGRAPH_ERROR: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
