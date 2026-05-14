"""Task 1: FizzBuzz.

Implement `fizzbuzz(n)` so that it returns a list of length `n` where:

- the i-th element (1-indexed) is "FizzBuzz" if i is divisible by both 3 and 5,
- "Fizz" if divisible by 3 only,
- "Buzz" if divisible by 5 only,
- otherwise the number i as a string.

Example:
    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']
"""


def fizzbuzz(n: int) -> list[str]:
    raise NotImplementedError


if __name__ == "__main__":
    for line in fizzbuzz(20):
        print(line)
