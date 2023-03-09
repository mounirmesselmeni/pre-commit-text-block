from __future__ import annotations
import sys
import argparse
from typing import Sequence


def check_file_for_bulk_create(filenames: Sequence[str], texts: list[str]) -> list[dict]:
    bad_files = []

    for filename in filenames:
        with open(filename, 'rb') as content:
            text_body = content.read()
            for text in texts:
                if text.encode() in text_body:
                    bad_files.append({'filename': filename, 'text': text})
    return bad_files


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='+', help='Filenames to run')
    parser.add_argument(
        '--text',
        dest='texts',
        action='append',
        default=[],
        help=('Text content you want to prevent'),
    )
    args = parser.parse_args(argv)

    if not args.texts:
        sys.stdout.write('No text to search for\n')
        return 1

    bad_filenames = check_file_for_bulk_create(args.filenames, args.texts)
    if bad_filenames:
        for bad_file in bad_filenames:
            sys.stdout.write(f"\033[1;31m{bad_file['text']} found in {bad_file['filename']}\033[m\n")
        return 1
    else:
        return 0


if __name__ == '__main__':
    raise SystemExit(main())
