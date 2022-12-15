from day12 import count_dots, age_in_minutes


def test_four_count_dots() -> None:
    assert count_dots('h.e.l.p.') == 4


def test_two_count_dots() -> None:
    assert count_dots('he.lp.') == 2


def test_age_in_minutes() -> None:
    assert age_in_minutes(1930) > 48355200
