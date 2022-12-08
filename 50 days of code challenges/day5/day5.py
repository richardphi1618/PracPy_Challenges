
def my_discount(price: float, percent_discount: float) -> float:
    return price - ((percent_discount / 100) * price)


def gender_count(students: list[str]) -> list[tuple]:
    case_checked_students = list(map(lambda x: x.lower(), students))
    final_count_dict = {i: case_checked_students.count(i) for i in case_checked_students}
    XY_count = ('Male', final_count_dict["male"])
    XX_count = ('female', final_count_dict["female"])
    return [XY_count, XX_count]


if __name__ == "__main__":
    price = float(input("What is the price? \n"))
    percent_discount = float(input("what is the discount(%)? \n"))
    print(my_discount(price, percent_discount))
