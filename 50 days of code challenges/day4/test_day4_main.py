from main import only_floats, word_index


def test_only_floats() -> None:
    test_tup = (12.1, 23)
    assert only_floats(test_tup) == 1


def test_word_index() -> None:
    words1 = ["Hate", "remorse", "vengeance"]
    assert word_index(words1) == 2

    words2 = ["Love", "Hate"]
    assert word_index(words2) == 0
