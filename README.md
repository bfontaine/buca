# Buca

**Buca** is a small Python script to blank some words in a text. I feed it with
lyrics and it gives me a text with blanks I can then fill when listening to the
song. It’s very helpful for vocabulary when learning a new language.

## Usage

    python3 buca.py [--ratio RATIO] [--fixed-size] [--numbers] [<file>]

* `--ratio RATIO`: change the default blank-to-word ratio. The default is 0.12,
  i.e. about 12% of the words are removed.
* `--fixed-size`: by default, missing words are replaced with a sequence of `_`
  of the length of the word. Using this option changes that to a fixed length
  that doesn’t depend on the word.
* `--numbers`: prefix blanks with an index, starting at 1. If you don’t want to
  print the text, you can report those numbers on a piece of paper.

If `<file>` is not provided or if it’s `-`, the script reads on `STDIN`.

Because it relies on randomness, each invocation of the script on the same text
should have different results. The number of blanked words may also change.

Note that a word is defined as a sequence of two or more alphanumerical
characters, without diacritics. I might change that but for now it covers the
letters used in the language I’m currently learning (Italian).

## Examples

Raw text:
```
Le cose che abbiamo in comune sono 4850
le conto da sempre, da quando mi hai detto
"ma dai, pure tu sei degli anno '60?"
abbiamo due braccia, due mani
due gambe, due piedi
due orecchie ed un solo cervello
```

### Default parameters

```
$ python3 buca.py example.txt
```

```
Le cose che abbiamo in comune sono 4850
le conto da sempre, da ______ __ hai detto
"ma dai, pure tu sei degli anno '__?"
abbiamo due braccia, due mani
___ gambe, due piedi
due orecchie ed un solo cervello
```

### Increased ratio

```
$ python3 buca.py --ratio 0.2 example.txt
```

```
Le cose che abbiamo __ comune sono ____
le conto da sempre, da quando __ hai detto
"ma dai, pure tu sei degli ____ '60?"
_______ due braccia, ___ ____
due gambe, due piedi
due ________ __ un solo cervello
```

### Fixed-size

```
$ python3 buca.py --fixed-size example.txt
```

```
Le cose che abbiamo in comune sono 4850
_____ conto da sempre, da quando mi hai _____
"ma dai, pure tu sei degli anno '60?"
abbiamo due braccia, due _____
due gambe, due piedi
due orecchie ed un solo cervello
```

### With numbers

```
$ python3 buca.py --numbers example.txt
```

```
Le (1) ____ che abbiamo in comune sono (2) ____
le conto da sempre, da quando mi hai detto
"ma dai, pure tu sei degli anno '60?"
abbiamo due braccia, due mani
(3) ___ gambe, due piedi
due orecchie (4) __ un solo cervello
```
