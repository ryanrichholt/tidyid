"""Tidy IDs are sample identifiers that are easy to read and write. """
import argparse
import string
from functools import wraps

confusing_characters = 'BDEILNOQRSTUVZ'
clear_characters = '0123456789ACFGHJKMPWXY'


def int_to_tid(n):
    """encodes base10 integer as baseN string using clear characters"""
    if not isinstance(n, int) or n < 1:
        raise TypeError('n must be integer >= 1')

    res = ''
    base = len(clear_characters)
    while n > 0:
        n, idx = divmod(n, base)
        res = clear_characters[idx] + res

    return res.upper()


def tid_to_int(tid):
    """decode tidyid to integer value"""
    total = 0
    base = len(clear_characters)
    for i, c in enumerate(reversed(tid)):
        cval = clear_characters.index(c)
        pval = cval * (base ** i)
        total += pval

    return total


def split_into_groups(s, length=3):
    """splits given string into groups of length"""
    if length < 0:
        raise TypeError('split length must be >= 0')
    s = ''.join(reversed(s))
    groups = [s[i:i + length] for i in range(0, len(s), length)]
    return [''.join(reversed(g)) for g in reversed(groups)]


def gen_ids(n, start=1, pad=0, split=0, delim='-'):
    """generate several tidy ids"""
    m = 0
    i = start
    while m < n:
        tid = int_to_tid(i)

        if pad:
            tid = tid.rjust(pad, '0')

        if split:
            groups = split_into_groups(tid, length=split)
            tid = delim.join(groups)

        yield i, tid

        m += 1
        i += 1


def validate_tid(tid):
    for c in tid:
        if c not in clear_characters:
            raise ValueError(f'contains invalid character "{c}"')


def clean_tid(tid, validate=True):
    tid = tid.replace('-', '')
    tid = tid.lstrip('0')
    tid = tid.upper()

    if validate:
        validate_tid(tid)

    return tid


def get_parser():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        'n',
        help='generate this many ids'
    )

    parser.add_argument(
        '-p', '--pad',
        type=int,
        default=0,
        help='pad ids with zeros so that they are at least this many '
            'characters long'
    )

    parser.add_argument(
        '-r', '--reverse',
        action='store_true',
        help='reverse lookup the integer value of an existing id. n should be '
            'the id to lookup.'
    )

    parser.add_argument(
        '-s', '--split',
        type=int,
        default=0,
        help='split ids into groups of this many characters'
    )

    parser.add_argument(
        '--start-at',
        type=int,
        default=1,
        help='generate ids starting at this with this integer value'
    )

    parser.add_argument(
        '--start-id',
        help='generate ids starting from a previous id'
    )

    return parser


def main(args=None):
    parser = get_parser()
    args = parser.parse_args(args)

    if args.reverse:
        tid = clean_tid(args.n)
        print(tid_to_int(tid))
    else:
        if args.start_id:
            start = tid_to_int(args.start_id)
        elif args.start_at:
            start = args.start_at

        n = int(args.n)
        gen = gen_ids(n, start=start, pad=args.pad, split=args.split)
        for i, tid in gen:
            print(f'{i}\t{tid}')


if __name__ == '__main__':
    main()
