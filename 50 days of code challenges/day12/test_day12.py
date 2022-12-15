from day12 import count_dots, age_in_minutes


def test_four_count_dots() -> None:
    assert count_dots('h.e.l.p.') == 4


def test_two_count_dots() -> None:
    assert count_dots('he.lp.') == 2


def test_age_in_minutes() -> None:
    assert age_in_minutes(1930) > 48355200


def test_age_in_minutes_invalid_year() -> None:
    try:
        age_in_minutes(19300)
        assert False
    except ValueError as e:
        assert e.args[0] == "Invalid year. Year can only be 4 digits"


def test_age_in_minutes_year_too_early() -> None:
    try:
        age_in_minutes(1800)
        assert False
    except ValueError as e:
        assert e.args[0] == "Year Must be after 1900"
