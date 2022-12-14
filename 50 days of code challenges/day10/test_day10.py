from day10 import convert_numbers, hide_password


def test_hide_password() -> None:
    assert hide_password('hello') == ('*****', 5)


def test_convert_numbers() -> None:
    input = [1000000, 2356989, 2354672, 9878098]
    output = ['1,000,000', '2,356,989', '2,354,672', '9,878,098']
    assert convert_numbers(input) == output
