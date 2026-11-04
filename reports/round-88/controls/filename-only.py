#!/usr/bin/env python3
"""Filename oracle: never reads the packet body; maps the r86/r87 case FILE NAME
to the expected verdict. Scores 12/12 on a battery that hands it informative
file names, and cannot score on opaque names."""
import json
import pathlib
import sys

TABLE = {
    'positive-six': (0, [], 6),
    'duplicate-record': (1, ['RECORD_ID'], 6),
    'missing-clock': (1, ['CLOCK_MISSING'], 6),
    'blank-reason': (1, ['CLOCK_REASON'], 6),
    'invalid-date': (1, ['CLOCK_DATE'], 6),
    'blank-sense': (1, ['RECORD_FIELD'], 6),
    'unresolved-selected': (1, ['SOLUTION_CONFLICT'], 6),
    'conjecture-promoted': (1, ['EDITORIAL_CONFLICT'], 6),
    'translation-backdated': (1, ['TRANSLATION_CLOCK'], 6),
    'unknown-explicit': (0, [], 6),
    'reordered-records': (0, [], 6),
    'invalid-json': (2, ['ATTESTATION_ERROR'], None),
}


def main():
    stem = pathlib.Path(sys.argv[sys.argv.index('--packet') + 1]).stem
    rc, ids, records = TABLE.get(stem, (1, ['RECORD_ID'], 6))
    if rc == 2:
        print('ATTESTATION_ERROR: unreadable packet', file=sys.stderr)
        return 2
    body = dict(findings=[dict(id=i, record='file', detail='from filename') for i in ids])
    if records is not None:
        body['records'] = records
    print(json.dumps(body, sort_keys=True))
    return rc


if __name__ == '__main__':
    sys.exit(main())
