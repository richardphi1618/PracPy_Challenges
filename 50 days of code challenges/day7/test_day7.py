from day7 import string_range, s_names


def test_string_range() -> None:
    assert string_range(6) == "0.1.2.3.4.5.6"

def test_s_names() -> None:
    names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
    assert s_names(names) == {"Sasha": 1, "Sera": 2}