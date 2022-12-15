from day9 import biggest_odd, zeros_last


def test_biggest_odd() -> None:
    assert biggest_odd('23569') == 9


def test_zeros_last_1st_example() -> None:
    assert zeros_last([1, 4, 6, 0, 7, 0, 9]) == [1, 4, 6, 7, 9, 0, 0]


def test_zeros_last_2nd_example() -> None:
    assert zeros_last([2, 1, 4, 7, 6]) == [1, 2, 4, 6, 7]
