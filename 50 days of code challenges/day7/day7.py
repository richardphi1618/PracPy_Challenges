def string_range(input: int) -> str:
    return ".".join(map(str, list(range(0, input + 1, 1))))


def s_names(input: "list[str]") -> dict:
    output = {}
    for i in input:
        if i[0] == "s" or i[0] == "S":
            if i not in output.keys():
                output[i] = 1
            else:
                output[i] += 1
    return output
