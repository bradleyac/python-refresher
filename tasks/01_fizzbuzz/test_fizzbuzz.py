from fizzbuzz import fizzbuzz


def test_first_fifteen():
    expected = [
        "1", "2", "Fizz", "4", "Buzz",
        "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz",
    ]
    assert fizzbuzz(15) == expected


def test_empty():
    assert fizzbuzz(0) == []


def test_only_one():
    assert fizzbuzz(1) == ["1"]


if __name__ == "__main__":
    test_first_fifteen()
    test_empty()
    test_only_one()
    print("ok")
