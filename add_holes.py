# -*- coding: UTF-8 -*-

import re
import sys
import argparse
from random import random

DEFAULT_HOLE_SIZE = 5


def make_word_replacer(ratio, fixed_size=True):
    def replace_word(match):
        word = match.group(0)
        if random() < ratio:
            size = DEFAULT_HOLE_SIZE if fixed_size else len(word)
            return "_" * size
        return word
    return replace_word

def main():
    p = argparse.ArgumentParser()
    p.add_argument("file", default=sys.stdin, type=argparse.FileType('r'))
    p.add_argument("--ratio", "-r", type=float, default=0.12,
        help="Holes ratio")
    p.add_argument("--fixed-size", action="store_true",
        help="Make holes of a fixed size instead of the length of the original word")
    args = p.parse_args()

    ratio = args.ratio
    if ratio < 0 or ratio > 1:
        raise ValueError("The ratio must be in [0;1]")

    text = args.file.read()
    args.file.close()

    replacer = make_word_replacer(ratio, fixed_size=args.fixed_size)

    text_with_holes = re.sub(r"[a-zA-Z0-9]{2,}", replacer, text)
    print(text_with_holes)


if __name__ == "__main__":
    main()
