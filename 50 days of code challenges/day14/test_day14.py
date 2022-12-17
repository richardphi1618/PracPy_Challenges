from day14 import flat_list, your_salary


def test_flat_list_example() -> None:
    assert flat_list([[2, 4, 5, 6]]) == [2, 4, 5, 6]

def test_flat_list_multiple_lists() -> None:
    assert flat_list([[2, 4, 5, 6], [2, 6], [2, 4]]) == [2, 4, 5, 6, 2, 6, 2, 4]

def test_your_salary() -> None:
    output = "Teacher: John Kelly, Periods: 105\nGross salary:2,125"
    assert your_salary("John Kelly", 105, 20) == output