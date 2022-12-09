def user_name(input: str) -> str:
    return input.split("@")[0]


def zeroed_code(input: list[int]) -> list[int]:
    input[0] = 0
    input[-1] = 0
    return input


if __name__ == "__main__":
    email = str(input("What is email \n"))
    print(f"username is: {user_name(email)}")
