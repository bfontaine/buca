# Buca

**Buca** is a small Python script to blank some words in a text. I feed it with
lyrics and it gives me a text with blanks I can then fill when listening to the
song. It’s very helpful for vocabulary when learning a new language.

## Usage

    python3 buca.py [--ratio RATIO] [--fixed-size] [--numbers] <your input>

* `--ratio RATIO`: change the default blank-to-word ratio. The default is 0.12,
  i.e. about 12% of the words are removed.
* `--fixed-size`: by default, missing words are replaced with a sequence of `_`
  of the length of the word. Using this option changes that to a fixed length
  that doesn’t depend on the word.
* `--numbers`: prefix blanks with an index, starting at 1. If you don’t want to
  print the text, you can report those numbers on a piece of paper.

Because it relies on randomness, each invocation of the script on the same text
should have different results.

Note that a word is defined as a sequence of two or more alphanumerical
characters, without diacritics. I might change that but for now it covers the
letters used in the language I’m currently learning (Italian).
