# python-refresher

Five small tasks to practice core Python. Each lives in its own folder under
`tasks/` and ships with a stub module and a test file.

## Layout

```
tasks/
  01_fizzbuzz/
  02_palindrome/
  03_word_frequency/
  04_temperature_converter/
  05_number_guessing_game/
```

## How to work on a task

1. Open the task folder and read the docstrings in the stub module.
2. Replace each `raise NotImplementedError` with a real implementation.
3. Run the test file to check yourself:

   ```
   python tasks/01_fizzbuzz/test_fizzbuzz.py
   ```

   Or run them all with `pytest`:

   ```
   pytest tasks/
   ```

## The tasks

| # | Folder | What you'll practice |
|---|--------|----------------------|
| 1 | `01_fizzbuzz` | loops, conditionals, modulo |
| 2 | `02_palindrome` | string slicing, normalization |
| 3 | `03_word_frequency` | dicts, file I/O, string methods |
| 4 | `04_temperature_converter` | functions, basic math |
| 5 | `05_number_guessing_game` | loops, `input()`, `random` |
