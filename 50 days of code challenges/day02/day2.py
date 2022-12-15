def convert_add(input: list[str]) -> int:
    num = 0
    for i in input:
        num += int(i)
    return num


def check_duplicates(input: list[str]) -> list[str]:
    seen = set()
    dupes = []

    for x in input:
        if x in seen:
            dupes.append(x)
        else:
            seen.add(x)

    if len(dupes) > 0:
        return dupes
    else:
        return ["no duplicates"]
