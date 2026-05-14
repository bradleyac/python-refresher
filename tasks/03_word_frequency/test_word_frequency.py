from word_frequency import count_words, top_n


def test_count_words_basic():
    assert count_words("Cats and dogs and CATS!") == {"cats": 2, "and": 2, "dogs": 1}


def test_count_words_empty():
    assert count_words("") == {}


def test_count_words_punctuation_and_digits():
    assert count_words("hello, hello world! 42 42 42") == {
        "hello": 2,
        "world": 1,
        "42": 3,
    }


def test_top_n_orders_by_count_then_word():
    counts = {"a": 3, "b": 3, "c": 1, "d": 2}
    assert top_n(counts, 3) == [("a", 3), ("b", 3), ("d", 2)]


def test_top_n_larger_than_input():
    assert top_n({"x": 1}, 5) == [("x", 1)]


if __name__ == "__main__":
    test_count_words_basic()
    test_count_words_empty()
    test_count_words_punctuation_and_digits()
    test_top_n_orders_by_count_then_word()
    test_top_n_larger_than_input()
    print("ok")
