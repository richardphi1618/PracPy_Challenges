from main import lower_case, register_check


def test_register_check() -> None:
    register = {"Michael": "yes", "John": "no", "Peter": "Yes", "Mary": "Yes"}
    assert register_check(register) == 3


def test_lower_case() -> None:
    names = ["John", "Mary", "carol", "Rose", "adam", "kerry", "dickson"]
    assert lower_case(names) == ("kerry", "dickson", "carol", "adam")
