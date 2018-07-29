# -*- coding: UTF-8 -*-

import re
import sys
import argparse
from random import random

DEFAULT_BLANK_SIZE = 5

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

        return self.make_blank(word)

    def make_blank(self, word):
        self._index += 1

        size = DEFAULT_BLANK_SIZE if self.fixed_size else len(word)
        blank = "_" * size
        if self.numbers:
            blank = "(%d) %s" % (self._index, blank)

        return blank

def main():
    p = argparse.ArgumentParser(description="Blank random words in a text")
    p.add_argument("file", default=sys.stdin, type=argparse.FileType('r'),
        help="Input file")
    p.add_argument("--ratio", "-r", type=float, default=0.12,
        help="Blanks ratio")
    p.add_argument("--fixed-size", action="store_true",
        help="Make blanks of a fixed size instead of the length of the original word")
    p.add_argument("--numbers", "-n", action="store_true",
        help="Prefix blanks with their index, starting at 1.")
    args = p.parse_args()

    ratio = args.ratio
    if ratio < 0 or ratio > 1:
        raise ValueError("The ratio must be in [0;1]")

    text = args.file.read()
    args.file.close()

    replacer = WordReplacer(ratio,
            numbers=args.numbers,
            fixed_size=args.fixed_size)

    text_with_blanks = re.sub(r"[a-zA-Z0-9àè]{2,}", replacer.replace_match, text)
    print(text_with_blanks)


if __name__ == "__main__":
    main()
