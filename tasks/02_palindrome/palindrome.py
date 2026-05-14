"""Task 2: Palindrome checker.

Implement `is_palindrome(text)` so that it returns True if `text` reads the
same forwards and backwards, ignoring case and any character that is not a
letter or digit.

Examples:
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("hello")
    False
"""


def is_palindrome(text: str) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    for sample in ["racecar", "hello", "A man, a plan, a canal: Panama"]:
        print(f"{sample!r} -> {is_palindrome(sample)}")
