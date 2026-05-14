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

import re;
import itertools;


def count_words(text: str) -> dict[str, int]:
    clean = re.sub(r"[^\s\w\d]", "", text.lower()).split()
    clean.sort()
    return {k: sum(1 for _ in group) for k, group in itertools.groupby(clean)}

def top_n(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    sorted = list(counts.items())
    sorted.sort(key = lambda kv: (-kv[1],kv[0]))
    return sorted[:n]


if __name__ == "__main__":
    from pathlib import Path

    text = Path(__file__).with_name("sample.txt").read_text()
    counts = count_words(text)
    for word, count in top_n(counts, 5):
        print(f"{word}: {count}")
