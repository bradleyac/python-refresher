from palindrome import is_palindrome


def test_simple_palindrome():
    assert is_palindrome("racecar") is True


def test_simple_non_palindrome():
    assert is_palindrome("hello") is False


def test_mixed_case_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_empty_string():
    assert is_palindrome("") is True


def test_single_character():
    assert is_palindrome("x") is True


def test_alphanumeric():
    assert is_palindrome("1A2 b2a1") is True


if __name__ == "__main__":
    test_simple_palindrome()
    test_simple_non_palindrome()
    test_mixed_case_and_punctuation()
    test_empty_string()
    test_single_character()
    test_alphanumeric()
    print("ok")
