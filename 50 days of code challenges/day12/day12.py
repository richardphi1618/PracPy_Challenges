import pendulum


def count_dots(input: str) -> int:
    dot_cnt = 0
    for i in input:
        if i == '.':
            dot_cnt += 1
    return dot_cnt


def age_in_minutes(input_year: int, input_month: int = 1, input_day: int = 1) -> int:
    if input_year < 1900:
        raise ValueError("Year Must be after 1900")

    if len(str(input_year)) != 4:
        raise ValueError("Invalid year. Year can only be 4 digits")

    now = pendulum.now()
    input = pendulum.local(input_year, input_month, input_day)
    output = now.diff(input).in_minutes()
    return output


if __name__ == "__main__":
    answer = None
    while answer is None:
        try:
            year = int(input("What year would you like? "))
        except Exception as e:
            print(e)

        month = input("What month would you like? ")
        day = input("What day would you like? ")

        if month == '':
            month = 1
        else:
            month = int(month)
        if day == '':
            day = 1
        else:
            day = int(day)

        try:
            answer = age_in_minutes(year, month, day)
            print(answer)
        except Exception as e:
            print(e)
            answer = None
