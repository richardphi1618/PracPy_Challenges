from day11 import equal_strings, swap_values


def test_equal_strings() -> None:
    assert equal_strings('love', 'evol')


def test_swap_values() -> None:
    assert swap_values([2, 4, 67, 7]) == [7, 4, 67, 2]
