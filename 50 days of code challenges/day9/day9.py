
def biggest_odd(input: str) -> int:
    odds = []
    for i in input:
        if int(i) % 2 != 0:
            odds.append(int(i))
    return max(odds)


def zeros_last(input: list[int]) -> list[int]:
    zeros_cnt = input.count(0)
    if zeros_cnt != 0:
        for i in range(zeros_cnt):
            input.append(input.pop(input.index(0)))
    else:
        input.sort()

    return input
