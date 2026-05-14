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


def _fizzbuzz_term(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def fizzbuzz(n: int) -> list[str]:
    return [_fizzbuzz_term(i) for i in range(1, n + 1)]


if __name__ == "__main__":
    for line in fizzbuzz(20):
        print(line)
