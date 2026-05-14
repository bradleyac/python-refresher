"""Task 3: Word frequency counter.

Implement two functions:

- `count_words(text)` returns a dict mapping each lowercase word in `text` to
  the number of times it appears. A "word" is any run of letters or digits.
  Words are compared case-insensitively.

- `top_n(counts, n)` returns the top `n` (word, count) pairs from a counts
  dict, sorted by count descending and then by word ascending for ties.

Example:
    >>> count_words("Cats and dogs and CATS!")
    {'cats': 2, 'and': 2, 'dogs': 1}
    >>> top_n({'a': 3, 'b': 3, 'c': 1}, 2)
    [('a', 3), ('b', 3)]
"""


def count_words(text: str) -> dict[str, int]:
    raise NotImplementedError


def top_n(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    raise NotImplementedError


if __name__ == "__main__":
    from pathlib import Path

    text = Path(__file__).with_name("sample.txt").read_text()
    counts = count_words(text)
    for word, count in top_n(counts, 5):
        print(f"{word}: {count}")
