def odd_even(input: list[int]) -> int:
    evens = []
    odds = []
    for i in input:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    answer = max(evens) - min(odds)
    return answer


def prime_numbers(input: int) -> list[int]:
    answer = []
    for num in range(2, input):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            answer.append(num)
    return answer
