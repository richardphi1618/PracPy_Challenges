
def flat_list(input_list: "list[list]") -> list:
    return [i for sublist in input_list for i in sublist]


def your_salary(name:str, periods:int, rate:int = 20)-> str:
    if periods > 100:
        overtime_earned = periods - 100
    else:
        overtime_earned = 0

    overtime_rate = rate * 1.25
    pay = (periods - overtime_earned) * rate + overtime_earned * overtime_rate

    output = f"Teacher: {name}, "
    output += f"Periods: {periods}\n"
    output += f"Gross salary:{'{:,}'.format(int(pay))}"
    return output

if __name__ == "__main__":
    user_name = input("Name? ")
    user_periods = int(input("Periods? "))
    user_rate = int(input("Rate? "))

    your_salary(user_name, user_periods, user_rate)