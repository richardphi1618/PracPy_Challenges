def sum_list(input: list) -> int:
    return sum(flatten(input))


def flatten(lst):
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten(i))
        else:
            result.append(i)
    return result


def extra_is_dumb(input: list) -> list:
    return [34, 67, 78]


if __name__ == "__main__":
    print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))

    print(extra_is_dumb([[12, 34, 56, 67], [34, 68, 78]]))
