import random

from main import divide_or_square


def test_example():
    assert divide_or_square(10) == 3.16


def test_return_remainder():
    for i in range(100):
        if i % 5 != 0:
            num = random.choice(range(1, 4))
            print(f"{i} * {num} = {i * num}")
            assert divide_or_square(i * num) in (1, 2, 3, 4)


def test_return_sqrt():
    for i in range(100):
        multiple_of_5 = i * 5
        assert round(divide_or_square(multiple_of_5) ** 2, 0) == multiple_of_5
