# -*- coding: UTF-8 -*-

import re
import sys
import argparse
from random import random

def make_word_replacer(ratio):
    def replace_word(match):
        word = match.group(0)
        if random() < ratio:
            return "_" * len(word)
        return word
    return replace_word

def main():
    p = argparse.ArgumentParser()
    p.add_argument("file", default=sys.stdin, type=argparse.FileType('r'))
    p.add_argument("--ratio", "-r", type=float, default=0.12)
    args = p.parse_args()

    ratio = args.ratio
    if ratio < 0 or ratio > 1:
        raise ValueError("The ratio must be in [0;1]")

    text = args.file.read()
    args.file.close()

    text_with_holes = re.sub(r"[a-zA-Z0-9]{2,}", make_word_replacer(ratio), text)
    print(text_with_holes)


if __name__ == "__main__":
    main()
