def register_check(input: dict) -> int:
    num = 0
    for keys, values in input.items():
        if values == "Yes" or values == "yes":
            print(values)
            num += 1
    return num


def lower_case(input: "list[str]") -> tuple:
    answer = ()
    for i in input:
        if i[0].islower():
            answer = answer + (i,)
    return answer
