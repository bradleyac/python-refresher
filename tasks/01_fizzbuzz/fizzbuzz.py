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

def fizzbuzzStr(n: int) -> str:
    match n:
        case fb if n % 15 == 0:
            return "FizzBuzz";
        case f if n % 3 == 0:
            return "Fizz";
        case b if n % 5 == 0:
            return "Buzz";
        case other:
            return str(other);

def fizzbuzz(n: int) -> list[str]:
    return [fizzbuzzStr(i + 1) for i in range(n)]


if __name__ == "__main__":
    for line in fizzbuzz(20):
        print(line)
