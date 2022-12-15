import pendulum


def count_dots(input: str) -> int:
    dot_cnt = 0
    for i in input:
        if i == '.':
            dot_cnt += 1
    return dot_cnt


def age_in_minutes(input_year: int, input_month: int = 1, input_day: int = 1) -> int:
    now = pendulum.now()
    input = pendulum.local(input_year, input_month, input_day)
    output = now.diff(input).in_minutes()
    return output
