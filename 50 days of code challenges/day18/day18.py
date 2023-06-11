def any_number(input:list[int or float]) -> float:
    return sum(input) / len(input)


def add_reverse(inputA: list[int or float], inputB: list[int or float]) -> list[int or float]:
    if len(inputA) != len(inputB):
        return ValueError("Input lists must be of same length") 
    output = [inputA[i] + inputB[i] for i in range(len(inputA))]
    return output[::-1]



if __name__ == "__main__":
    print(any_number([12, 90, 12, 34]))
    print(any_number([12, 90]))

    print(add_reverse([10, 12, 34], [12, 56, 78]))
    print(add_reverse([10, 34], [12, 56, 78]))