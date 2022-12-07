import json
import random

from day1 import divide_or_square, longest_value


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


def test_longest_value():
    fruits = {"fruit": "apple", "color": "green"}
    assert longest_value(fruits) == "apple"


def test_longest_value_from_file():
    # gave up on this idea after I had to think about how to capture the correct answer
    all_tests = []
    with open("./50 days of code challenges/day1/sample data/bonus_challenge_data.txt") as f:
        lines = f.readlines()
        for i in lines:
            input = i.replace(" ", "").split("=")
            all_tests.append({input[0]: json.loads(input[1].replace("'", '"'))})
