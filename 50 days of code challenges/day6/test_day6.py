from day6 import user_name, zeroed_code


def test_user_name() -> None:
    assert user_name("ben@gmail.com") == "ben"


def test_zeroed_code() -> None:
    assert zeroed_code([2, 5, 7, 8, 9]) == [0, 5, 7, 8, 0]
