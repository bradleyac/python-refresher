"""Task 5: Number guessing game.

You'll build a "guess the number" game in two layers so it stays testable.

1. `evaluate_guess(guess, target)` returns one of: "low", "high", or "correct".

2. `play(target, guesses)` runs a single game without doing any I/O. It is
   given the secret `target` and an iterable of `guesses` (ints) to feed in
   one at a time. It returns the number of guesses it took to land on
   `target`, or `None` if the player ran out of guesses without succeeding.

3. `main()` is the interactive entry point that picks a random number between
   1 and 100, prompts the user with `input()`, and prints feedback after each
   guess. Use the helpers above so this layer stays tiny.

Examples:
    >>> evaluate_guess(5, 10)
    'low'
    >>> evaluate_guess(42, 42)
    'correct'
    >>> play(7, iter([1, 7, 99]))
    2
    >>> play(7, iter([1, 2, 3])) is None
    True
"""

from __future__ import annotations

import random
from typing import Iterable


def evaluate_guess(guess: int, target: int) -> str:
    if guess == target:
        return "correct"
    if guess < target:
        return "low"
    return "high"


def play(target: int, guesses: Iterable[int]) -> int | None:
    for i, guess in enumerate(guesses, start=1):
        if evaluate_guess(guess, target) == "correct":
            return i
    return None


def prompt() -> int:
    while True:
        raw = input("Guess a number from 1 to 100: ").strip()
        try:
            value = int(raw)
        except ValueError:
            print("That wasn't a number.")
            continue
        if 1 <= value <= 100:
            return value
        print("That wasn't between 1 and 100")


def main() -> None:
    target = random.randint(1, 100)
    while True:
        feedback = evaluate_guess(prompt(), target)
        print(feedback)
        if feedback == "correct":
            return


if __name__ == "__main__":
    main()
