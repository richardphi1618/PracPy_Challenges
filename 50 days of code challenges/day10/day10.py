
def hide_password(password: str) -> tuple[str, int]:
    password_length = len(password)
    secure_string = '*' * password_length
    return (secure_string, password_length)


def convert_numbers(input: list[int]) -> list[str]:
    output = []
    for idx, i in enumerate(input):
        output.append('{:,}'.format(i))
    return output
