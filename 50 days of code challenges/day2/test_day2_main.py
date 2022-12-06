from main import check_duplicates, convert_add


def test_convert_add() -> None:
    #  [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.
    test_list = ['1', '3', '5']
    assert convert_add(test_list) == 9


def test_check_duplicates() -> None:
    # the list of fruits below should return apple as a duplicate and list of names should return "no duplicates".

    fruits = ['apple', 'orange', 'banana', 'apple']
    names = ['Yoda', 'Moses', 'Joshua', 'Mark']

    assert check_duplicates(fruits) == ["apple"]
    assert check_duplicates(names) == ["no duplicates"]
