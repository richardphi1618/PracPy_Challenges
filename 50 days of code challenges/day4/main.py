

def only_floats(input: tuple) -> int:
    num = 0
    for i in input:
        if isinstance(i, float):
            num += 1
    return num


def word_index(input: list[str]) -> int:
    num = 0
    longest_word = max(input)
    num = input.index(longest_word)
    return num
