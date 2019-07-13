# -*- coding: UTF-8 -*-

import re
import sys
import argparse
from random import random

__version__ = "0.0.2"

DEFAULT_BLANK_SIZE = 5
WORD_RE = re.compile(r"\w{2,}")

class WordReplacer:
    def __init__(self, ratio, fixed_size=False, numbers=False, max_count=-1):
        self.ratio = ratio
        self.fixed_size = fixed_size
        self.numbers = numbers
        self.max_count = max_count

        self._index = 0

    def replace_match(self, match):
        return self.replace_word(match.group(0))

    def replace_word(self, word):
        if self._index == self.max_count:
            return word

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

    def run(self, text):
        return WORD_RE.sub(self.replace_match, text)

def main():
    p = argparse.ArgumentParser(description="Blank random words in a text")
    p.add_argument("file", default=sys.stdin, type=argparse.FileType('r'),
        help="Input file")
    p.add_argument("--ratio", "-r", type=float, default=0.12,
        help="Blanks ratio")
    p.add_argument("--fixed-size", "-F", action="store_true",
        help="Make blanks of a fixed size instead of the length of the original word")
    p.add_argument("--numbers", "-n", action="store_true",
        help="Prefix blanks with their index, starting at 1.")
    p.add_argument("--max-count", "-c", type=int, default=-1,
        help="Stop after this number of words.")
    args = p.parse_args()

    ratio = args.ratio
    if ratio < 0 or ratio > 1:
        raise ValueError("The ratio must be in [0;1]")

    text = args.file.read()
    args.file.close()

    replacer = WordReplacer(ratio,
            numbers=args.numbers,
            max_count=args.max_count,
            fixed_size=args.fixed_size)

    print(replacer.run(text))


if __name__ == "__main__":
    main()
