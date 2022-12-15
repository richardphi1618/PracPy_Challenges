
def my_discount(price: float, percent_discount: float) -> float:
    return price - ((percent_discount / 100) * price)


def gender_count(students: list[str]) -> list[tuple]:
    case_checked_students = list(map(lambda x: x.lower(), students))
    XY_count = ('Male', case_checked_students.count("male"))
    XX_count = ('female', case_checked_students.count("female"))
    return [XY_count, XX_count]


if __name__ == "__main__":
    price = float(input("What is the price? \n"))
    percent_discount = float(input("what is the discount(%)? \n"))
    print(my_discount(price, percent_discount))
