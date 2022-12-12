from day8 import odd_even, prime_numbers


def test_odd_even() -> None:
    assert odd_even([1, 2, 4, 6]) == 5


def test_prime_numbers() -> None:
    assert prime_numbers(10) == [2, 3, 5, 7]
