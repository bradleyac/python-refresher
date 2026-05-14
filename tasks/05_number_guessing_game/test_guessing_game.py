from guessing_game import evaluate_guess, play


def test_evaluate_low():
    assert evaluate_guess(5, 10) == "low"


def test_evaluate_high():
    assert evaluate_guess(15, 10) == "high"


def test_evaluate_correct():
    assert evaluate_guess(10, 10) == "correct"


def test_play_finds_target():
    assert play(7, iter([1, 7, 99])) == 2


def test_play_first_guess():
    assert play(42, iter([42])) == 1


def test_play_out_of_guesses():
    assert play(7, iter([1, 2, 3])) is None


if __name__ == "__main__":
    test_evaluate_low()
    test_evaluate_high()
    test_evaluate_correct()
    test_play_finds_target()
    test_play_first_guess()
    test_play_out_of_guesses()
    print("ok")
