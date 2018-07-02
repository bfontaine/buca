# -*- coding: UTF-8 -*-

import re
import sys
import argparse
from random import random

DEFAULT_HOLE_SIZE = 5

class WordReplacer:
    def __init__(self, ratio, fixed_size=True, numbers=False):
        self.ratio = ratio
        self.fixed_size = fixed_size
        self.numbers = numbers

        self._index = 0

    def replace_match(self, match):
        return self.replace_word(match.group(0))

    def replace_word(self, word):
        if random() >= self.ratio:
            return word

        return self.make_hole(word)

    def make_hole(self, word):
        self._index += 1

        size = DEFAULT_HOLE_SIZE if self.fixed_size else len(word)
        hole = "_" * size
        if self.numbers:
            hole = "(%d) %s" % (self._index, hole)

        return hole

def main():
    p = argparse.ArgumentParser()
    p.add_argument("file", default=sys.stdin, type=argparse.FileType('r'))
    p.add_argument("--ratio", "-r", type=float, default=0.12,
        help="Holes ratio")
    p.add_argument("--fixed-size", action="store_true",
        help="Make holes of a fixed size instead of the length of the original word")
    p.add_argument("--numbers", "-n", action="store_true")
    args = p.parse_args()

    ratio = args.ratio
    if ratio < 0 or ratio > 1:
        raise ValueError("The ratio must be in [0;1]")

    text = args.file.read()
    args.file.close()

    replacer = WordReplacer(ratio,
            numbers=args.numbers,
            fixed_size=args.fixed_size)

    text_with_holes = re.sub(r"[a-zA-Z0-9àè]{2,}", replacer.replace_match, text)
    print(text_with_holes)


if __name__ == "__main__":
    main()
