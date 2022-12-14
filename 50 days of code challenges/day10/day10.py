
def hide_password(password: str) -> tuple[str, int]:
    return ('*' * len(password), len(password))


def convert_numbers(input: list[int]) -> list[str]:
    output = []
    for i in input:
        output.append('{:,}'.format(i))
    return output
