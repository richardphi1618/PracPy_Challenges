from day5 import gender_count, my_discount


def test_my_discount() -> None:
    assert my_discount(150, 15) == 127.5


def test_gender_count() -> None:
    students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female',
                'male', 'Female', 'Male', 'Female', 'Male', 'female']
    assert gender_count(students) == [('Male', 7), ('female', 6)]
