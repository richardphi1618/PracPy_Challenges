import math


def divide_or_square(input: int) -> float:
    remainder = input % 5
    if remainder == 0:
        return round(math.sqrt(input), 2)
    else:
        return remainder
