
def equal_strings(x_word: str, y_word: str) -> bool:
    return sorted(x_word) == sorted(y_word)


def swap_values(input: list[int]) -> list[int]:
    output = []
    for i in input:
        output.append(i)
    output[0] = input[-1]
    output[-1] = input[0]
    return output
